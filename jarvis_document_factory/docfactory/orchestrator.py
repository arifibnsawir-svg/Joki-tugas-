"""Orchestrator: multi-format render dispatch and cross-format consistency.

render_all produces exactly one file per requested format from the same
validated SPEC. The Audit/Rancang/Sistemasi/Iterasi loop and the gate wiring
live in run_pipeline.

PIPA4 auto-wiring (CHECKPOINT 12.29 / RESUME): after factory gate PASS for
academic docs, auto-trigger PIPA4 council via pipa4_gate.sh. Hook lives in
~/.hermes/scripts/pipa4_hook.py (repo jarvis/scripts/). Fail-open: jika
PIPA4 tidak terpasang di Acer, skip graceful.
"""
from __future__ import annotations

import os
import sys

from .readers import read_text
from .renderers import docx as docx_renderer
from .renderers import pdf as pdf_renderer
from .renderers import pptx as pptx_renderer
from .citation import apply_citation_layer
from .gate import gate as run_gate
from .humanizer import humanize_spec
from .images import assert_referenced_images_exist, resolve_figures
from .router import select_route
from .spec import parse_spec
from .validation import validate

_TOC_SCAN_TMP = "._toc_scan.pdf"


def _has_toc(spec) -> bool:
    return any(s.kind == "toc" for s in spec.sections)


def render_all(spec, out_dir: str, basename: str = "document", *, request: str = "") -> dict:
    os.makedirs(out_dir, exist_ok=True)
    fmts = list(spec.formats)
    results = {}
    warnings: list[str] = []
    pdf_path_for_docx = None
    temp_pdf = None

    if "pdf" in fmts:
        pdf_out = os.path.join(out_dir, basename + ".pdf")
        results["pdf"] = pdf_renderer.render(spec, pdf_out)
        pdf_path_for_docx = pdf_out

    if "docx" in fmts and _has_toc(spec) and pdf_path_for_docx is None:
        temp_pdf = os.path.join(out_dir, _TOC_SCAN_TMP)
        pdf_renderer.render(spec, temp_pdf)
        pdf_path_for_docx = temp_pdf

    if "docx" in fmts:
        docx_out = os.path.join(out_dir, basename + ".docx")
        results["docx"] = docx_renderer.render(spec, docx_out, pdf_path=pdf_path_for_docx)

    if "pptx" in fmts:
        pptx_out = os.path.join(out_dir, basename + ".pptx")
        results["pptx"] = pptx_renderer.render(spec, pptx_out, request=request)

    if temp_pdf and os.path.exists(temp_pdf):
        os.remove(temp_pdf)

    consistency = check_consistency(spec, results)
    return {"results": results, "consistency": consistency, "warnings": warnings}


def _expected_facts(spec) -> dict:
    return {
        "title": spec.identity.title,
        "section_titles": [s.title for s in spec.sections if s.kind != "toc"],
        "references": [r.apa for r in spec.references],
    }


def extract_presence(fmt: str, path: str, spec) -> dict:
    text = read_text(fmt, path)
    flat = "".join(text.split()).casefold()
    expected = _expected_facts(spec)

    def norm(s):
        return "".join(str(s).split()).casefold()

    return {
        "title": norm(expected["title"]) in flat,
        "section_titles": [t for t in expected["section_titles"] if norm(t) in flat],
        "references_present": all(norm(r)[:40] in flat for r in expected["references"]),
    }


def check_consistency(spec, results: dict) -> dict:
    fmts = list(results.keys())
    if len(fmts) < 2:
        return {"matched": ["title", "section_order", "references"], "unmatched": []}
    presences = {fmt: extract_presence(fmt, results[fmt].out_path, spec) for fmt in fmts}
    return diff_consistency(presences)


def diff_consistency(presences: dict) -> dict:
    fmts = list(presences.keys())
    matched: list[str] = []
    unmatched: list[str] = []
    title_vals = {presences[f]["title"] for f in fmts}
    (matched if len(title_vals) == 1 else unmatched).append("title")
    order_vals = {tuple(presences[f]["section_titles"]) for f in fmts}
    (matched if len(order_vals) == 1 else unmatched).append("section_order")
    ref_vals = {presences[f]["references_present"] for f in fmts}
    (matched if len(ref_vals) == 1 else unmatched).append("references")
    return {"matched": matched, "unmatched": unmatched}


from dataclasses import dataclass, field  # noqa: E402


class OutputState:
    def __init__(self):
        self._verdicts: list[str] = []

    def record(self, verdict: str) -> None:
        self._verdicts.append(verdict)

    @property
    def has_verdict(self) -> bool:
        return bool(self._verdicts)

    @property
    def is_done(self) -> bool:
        return bool(self._verdicts) and self._verdicts[-1] == "PASS"

    @property
    def status(self) -> str:
        return "DONE" if self.is_done else "AWAITING_GATE"


@dataclass
class PipelineResult:
    status: str
    route: object
    results: dict = field(default_factory=dict)
    verdicts: dict = field(default_factory=dict)
    consistency: dict = field(default_factory=dict)
    trace: list = field(default_factory=list)
    iterations: int = 0
    pipa4: dict = field(default_factory=dict)


def _apply_layers_and_validate(spec):
    humanize_spec(spec)
    apply_citation_layer(spec)
    resolve_figures(spec)
    assert_referenced_images_exist(spec)
    validate(spec)
    return spec


def _load_pipa4_hook():
    """Load PIPA4 hook from ~/.hermes/scripts/ (repo jarvis/scripts/).

    Fail-open: returns None jika PIPA4 tidak terpasang di Acer.
    """
    candidates = [
        os.path.expanduser("~/.hermes/scripts/pipa4_hook.py"),
        os.path.expanduser("~/jarvis/scripts/pipa4_hook.py"),
    ]
    for path in candidates:
        if path and os.path.isfile(path):
            import importlib.util

            spec = importlib.util.spec_from_file_location("pipa4_hook", path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
    return None


def run_pipeline(spec_or_dict, out_dir, basename="document", *, request="",
                 fix_fn=None, max_iterations=3):
    trace = []
    trace.append("audit")
    spec = parse_spec(spec_or_dict) if isinstance(spec_or_dict, dict) else spec_or_dict
    route = select_route(spec, request=request)
    trace.append("rancang")

    states = {fmt: OutputState() for fmt in spec.formats}
    results = {}
    verdicts = {}
    consistency = {}
    iterations = 0

    for attempt in range(1, max_iterations + 1):
        trace.append("sistemasi")
        _apply_layers_and_validate(spec)
        rendered = render_all(spec, out_dir, basename=basename, request=request)
        results = rendered["results"]
        consistency = rendered["consistency"]
        pdf_path = results["pdf"].out_path if "pdf" in results else None

        trace.append("iterasi")
        iterations = attempt
        verdicts = {}
        any_fail = False
        for fmt, r in results.items():
            verdict = run_gate(spec, fmt, r.out_path, pdf_path=pdf_path)
            verdicts[fmt] = verdict
            states[fmt].record(verdict.verdict)
            if not verdict.is_pass:
                any_fail = True

        if not any_fail:
            break
        if fix_fn is None:
            break
        failed = {fmt: v.failed_checks for fmt, v in verdicts.items() if not v.is_pass}
        fixed = fix_fn(spec, failed)
        if fixed is None:
            break
        spec = fixed

    status = "DONE" if all(s.is_done for s in states.values()) and states else "AWAITING_GATE"

    # ---- PIPA4 auto-wiring (academic only, after factory gate PASS) ----
    pipa4_result = {}
    is_academic = getattr(spec, "is_academic", False)
    all_pass = status == "DONE"
    if is_academic and all_pass:
        trace.append("pipa4_council")
        pipa4_mod = _load_pipa4_hook()
        if pipa4_mod is not None:
            target_fmt = "pdf" if "pdf" in results else ("docx" if "docx" in results else None)
            if target_fmt:
                target_path = results[target_fmt].out_path
                constraint = getattr(spec, "pipa4_constraint", None) or None
                pipa4_result = pipa4_mod.run(target_path, constraint_name=constraint)
        else:
            pipa4_result = {
                "triggered": False, "verdict": "SKIPPED",
                "reason_skipped": "pipa4_hook.py tidak ditemukan di ~/.hermes/scripts/",
            }

    return PipelineResult(
        status=status, route=route, results=results, verdicts=verdicts,
        consistency=consistency, trace=trace, iterations=iterations,
        pipa4=pipa4_result,
    )
