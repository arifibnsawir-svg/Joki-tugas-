#!/usr/bin/env python3
"""Pre-render SPEC validator for the Jarvis Document Factory.

Runs the SAME pre-render pipeline that run.py runs (humanizer -> citation ->
image resolution -> validation) but stops BEFORE any renderer and reports
problems in clear, human-readable Indonesian instead of crashing with a raw
traceback. Use it to check a SPEC before calling run.py so a broken SPEC is
fixed up front, not discovered as a mysterious stack trace mid-render.

    python3 validate_spec.py SPEC.json
    python3 validate_spec.py SPEC.json --json

Exit 0 = SPEC render-ready (run.py won't fail at validation; the gate still has
         the final say on the rendered file).
Exit 1 = SPEC has problems (each is named with a fix hint).
Exit 2 = SPEC file could not be read or parsed as JSON.

This does NOT render and is NOT a substitute for the gate. It previews the SPEC
schema/validation plus the citation_consistency check that can be judged from
the SPEC alone; the deterministic gate remains the sole authority for DONE.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

_SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
if _SKILL_DIR not in sys.path:
    sys.path.insert(0, _SKILL_DIR)

from docfactory.citation import apply_citation_layer  # noqa: E402
from docfactory.constants import SUPPORTED_FORMATS  # noqa: E402
from docfactory.errors import (  # noqa: E402
    MissingImageError,
    SpecValidationError,
    UnsupportedFormatError,
)
from docfactory.gate import (  # noqa: E402
    _cited_surnames,
    _ref_surnames,
    _spec_body_text,
    check_citation_consistency,
)
from docfactory.humanizer import humanize_spec  # noqa: E402
from docfactory.images import (  # noqa: E402
    assert_referenced_images_exist,
    resolve_figures,
)
from docfactory.spec import parse_spec  # noqa: E402
from docfactory.validation import validate  # noqa: E402


def _fmt_list() -> str:
    return ", ".join(SUPPORTED_FORMATS)


def scan_structural_issues(spec):
    """Cheap, non-fatal scan so an author sees the common problems all at once
    instead of fixing one, re-running, and hitting the next.

    These mirror the authoritative rules in docfactory/validation.py; the real
    validate() below stays the single source of truth and has the final say.
    """
    issues = []

    if not spec.formats:
        issues.append("formats: kosong. Minta minimal satu dari: %s." % _fmt_list())
    for token in spec.formats:
        if token not in SUPPORTED_FORMATS:
            issues.append(
                "formats: %r tidak didukung. Pilihan: %s." % (token, _fmt_list())
            )

    if not (getattr(spec.identity, "title", "") or "").strip():
        issues.append("identity.title: kosong. Judul dokumen wajib diisi.")

    if not spec.sections:
        issues.append("sections: kosong. Minimal satu section wajib ada.")

    seen = set()
    for i, s in enumerate(spec.sections):
        sid = (s.id or "").strip()
        if not sid:
            issues.append("sections[%d].id: kosong. Tiap section butuh id unik." % i)
        elif sid in seen:
            issues.append(
                "sections[%d].id: %r duplikat. id section harus unik." % (i, s.id)
            )
        else:
            seen.add(sid)
        if not (s.title or "").strip():
            issues.append("sections[%d] (id=%r): title kosong." % (i, s.id))

    kinds = {s.kind for s in spec.sections}
    if "toc" in kinds and "chapter" not in kinds:
        issues.append(
            "sections: ada 'toc' tapi tidak ada 'chapter'. Daftar Isi butuh minimal satu bab (kind='chapter')."
        )

    if spec.is_academic:
        if not spec.references:
            issues.append(
                "references: kosong. Dokumen akademik wajib punya daftar pustaka (verified=true)."
            )
        for r in spec.references:
            if not getattr(r, "verified", False):
                issues.append(
                    "references[id=%r]: verified=false. Sumber tak terverifikasi akan dibuang & bikin gate FAIL."
                    % getattr(r, "id", "?")
                )

    registered = {getattr(f, "ref", None) for f in spec.figures}
    for s in spec.sections:
        for b in s.blocks:
            if isinstance(b, dict) and b.get("type") == "figure":
                ref = b.get("ref")
                if ref not in registered:
                    issues.append(
                        "sections[id=%r]: figure block ref=%r tidak terdaftar di figures[]. Daftarkan figure + path yang ADA."
                        % (s.id, ref)
                    )
    return issues


def _describe(e) -> str:
    if isinstance(e, SpecValidationError):
        fmt = (" (format %r)" % e.fmt) if getattr(e, "fmt", None) else ""
        detail = getattr(e, "detail", "") or "tidak valid"
        return "field %r%s: %s" % (getattr(e, "field", "?"), fmt, detail)
    if isinstance(e, UnsupportedFormatError):
        supported = ", ".join(getattr(e, "supported", SUPPORTED_FORMATS))
        return "format %r tidak didukung. Pilihan: %s." % (
            getattr(e, "token", "?"),
            supported,
        )
    if isinstance(e, MissingImageError):
        return (
            "figure %r menunjuk path gambar yang tidak ada: %r. Perbaiki path atau hapus figure (anti-halu gambar)."
            % (getattr(e, "ref", "?"), getattr(e, "path", "?"))
        )
    return "%s: %s" % (type(e).__name__, e)


def _emit(ok, problems, spec_path, as_json):
    if as_json:
        print(
            json.dumps(
                {"ok": ok, "spec": spec_path, "problems": problems},
                ensure_ascii=False,
                indent=2,
            )
        )
        return
    if ok:
        print("OK: SPEC siap dirender. run.py tidak akan gagal di tahap validasi.")
        print("(Gate deterministik tetap penentu akhir DONE saat file sudah dirender.)")
    else:
        print("SPEC BELUM VALID - %d masalah:" % len(problems))
        for i, m in enumerate(problems, 1):
            print("  %d. %s" % (i, m))
        print("")
        print("Perbaiki SPEC lalu jalankan validate_spec.py lagi sampai OK, baru run.py.")
        print("JANGAN fallback ke freehand (python-docx / render_deck langsung / tulis file manual).")


def _fail_load(msg, as_json):
    _emit(False, [msg], None, as_json)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Pra-cek SPEC Jarvis Document Factory sebelum run.py"
    )
    ap.add_argument("spec", help="path ke file SPEC JSON")
    ap.add_argument("--json", action="store_true", help="cetak laporan sebagai JSON")
    args = ap.parse_args(argv)

    try:
        with open(args.spec, "r", encoding="utf-8") as fh:
            raw = fh.read()
    except OSError as e:
        _fail_load("tidak bisa membaca file SPEC %r: %s" % (args.spec, e), args.json)
        return 2

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        _fail_load(
            "SPEC bukan JSON valid (baris %d, kolom %d): %s" % (e.lineno, e.colno, e.msg),
            args.json,
        )
        return 2

    try:
        spec = parse_spec(data)
    except Exception as e:  # struktur dasar tak bisa di-parse
        _fail_load(
            "struktur SPEC tidak bisa dibaca: %s: %s" % (type(e).__name__, e), args.json
        )
        return 2

    problems = scan_structural_issues(spec)

    # Authoritative pre-render sequence (mirrors orchestrator). Only run when the
    # cheap scan is clean, so we do not trip over an issue already reported.
    if not problems:
        try:
            humanize_spec(spec)
            apply_citation_layer(spec)
            resolve_figures(spec)
            assert_referenced_images_exist(spec)
            validate(spec)
        except (SpecValidationError, UnsupportedFormatError, MissingImageError) as e:
            problems.append(_describe(e))
        except Exception as e:  # pragma: no cover - unexpected
            problems.append(
                "error tak terduga saat validasi: %s: %s" % (type(e).__name__, e)
            )

    # SPEC-level citation_consistency preview (the top academic failure). Runs on
    # the post-citation-layer SPEC, exactly what the gate checks on the rendered
    # body. Catches "reference added but never cited" up front.
    if not problems and spec.is_academic:
        ok_cite, detail = check_citation_consistency(
            _cited_surnames(_spec_body_text(spec)), _ref_surnames(spec)
        )
        if not ok_cite:
            problems.append(
                "citation_consistency: %s (tiap sitasi butuh pustaka & tiap pustaka wajib disitir)."
                % detail
            )

    ok = not problems
    _emit(ok, problems, args.spec, args.json)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
