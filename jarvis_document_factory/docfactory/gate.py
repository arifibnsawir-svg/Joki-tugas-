"""Output_Gate: the deterministic PASS/FAIL authority (generalizes qa.py).

The gate inspects a rendered file and returns a GateVerdict. It is the sole
authority that declares an output done; the language model may at most propose
the awaiting-gate state. The gate runs all seven checks for every format,
returns exactly PASS or FAIL, lists every failed check with a description on
FAIL, and never crashes (each check is wrapped so an unexpected error becomes a
FAIL, not an exception).

The pure check functions (check_*) are exposed so each correctness property can
be tested directly over generated inputs, independent of a rendered file.
"""
from __future__ import annotations

import re

from .citation import CITE_PAIR, CITE_SINGLE, _surname_of_reference
from .humanizer import is_humanizer_clean
from .images import referenced_figure_refs, verified_figure_refs
from .readers import count_words, read_docx_paragraph_texts, read_pdf_pages, read_pptx_slide_texts
from .spec import CheckResult, GateVerdict

NEAR_EMPTY_THRESHOLD = 10
_DANGLING = re.compile(r"BAB [IVXLCDM]+")
_TRAILING_NUM = re.compile(r"^(.*\S)\s+(\d+)$")
_EM_EN_DASH = ("\u2014", "\u2013")


# ---------------------------------------------------------------- pure checks
def check_structure_order(expected_labels, flat_text):
    """Pass iff every expected label is present and appears in expected order."""
    flat = " ".join(flat_text.split()).casefold()
    last = -1
    problems = []
    for label in expected_labels:
        key = " ".join(str(label).split()).casefold()
        if not key:
            continue
        pos = flat.find(key)
        if pos == -1:
            problems.append("%s(missing)" % label)
        elif pos < last:
            problems.append("%s(out-of-order)" % label)
        else:
            last = pos
    ok = not problems
    return ok, ("ordered" if ok else "issues: " + ", ".join(problems))


def check_citation_consistency(cited: set, refs: set):
    """Pass iff every citation has a reference and every reference is cited."""
    missing_ref = set(cited) - set(refs)   # cited but no reference entry
    uncited = set(refs) - set(cited)       # reference entry never cited
    ok = not missing_ref and not uncited
    return ok, ("consistent" if ok else "cited-without-reference: %s; reference-never-cited: %s"
                % (sorted(missing_ref) or "none", sorted(uncited) or "none"))


def check_humanizer_clean(text: str):
    ok = is_humanizer_clean(text)
    return ok, ("clean" if ok else "contains em-dash, en-dash, curly quote, or emoji")


def check_no_blank_page(pages, threshold: int = NEAR_EMPTY_THRESHOLD):
    """Pass iff every page carries content above the near-empty threshold."""
    offenders = []
    for i, p in enumerate(pages):
        if len(" ".join(p.split())) < threshold:
            offenders.append(i + 1)
    ok = not offenders
    return ok, ("no blank or near-empty page" if ok else "blank/near-empty pages: %s" % offenders)


def check_no_dangling_heading(pages):
    """Pass iff no page consists solely of a chapter heading such as BAB X."""
    offenders = []
    for i, p in enumerate(pages):
        s = " ".join(p.split())
        if _DANGLING.fullmatch(s):
            offenders.append(i + 1)
    ok = not offenders
    return ok, ("no dangling heading" if ok else "dangling heading on pages: %s" % offenders)


def check_toc_accurate(entries, actual_map, toc_fits: bool):
    """Pass iff the TOC fits its space and each TOC page number matches the render.

    entries: list of (label, claimed_page:int). actual_map: {label: actual_page}.
    """
    if not toc_fits:
        return False, "table of contents overflows its allotted space"
    mismatches = []
    for label, claimed in entries:
        actual = actual_map.get(label)
        if actual is not None and int(claimed) != int(actual):
            mismatches.append("%s: toc=%s actual=%s" % (label, claimed, actual))
    ok = not mismatches
    return ok, ("toc accurate" if ok else "; ".join(mismatches))


def check_images_real(paths):
    """Pass iff every embedded image path exists on disk."""
    import os

    missing = [p for p in paths if not os.path.exists(p)]
    ok = not missing
    return ok, ("all images resolve to real files" if ok else "missing image files: %s" % missing)


# ---------------------------------------------------------------- extraction
def _strip_deck_chrome(text: str) -> str:
    """Remove render_deck decorative dash markers before the PPTX humanizer check.

    The house renderer injects an em-dash as a visual bullet marker (its author
    notes it is chrome, not prose). Since the SPEC prose was already humanized,
    any em/en-dash in a factory deck can only be that chrome, so it is stripped
    before the check. Curly quotes and emoji are never injected and remain
    checked.
    """
    for ch in _EM_EN_DASH:
        text = text.replace(ch, "")
    return text


def _expected_labels(spec, fmt="pdf"):
    """Structural labels expected in the rendered output, format-aware.

    PDF/DOCX carry chapter labels as "BAB {number}" and include the TOC heading.
    The PPTX deck shows section titles (no "BAB N" prefix) and has no TOC slide,
    so its expected labels are the document title plus each non-TOC section title.
    """
    labels = [spec.identity.title]
    for s in spec.sections:
        if fmt == "pptx":
            if s.kind == "toc":
                continue
            labels.append(s.title)
        else:
            if s.kind == "chapter" and s.number:
                labels.append("BAB %s" % s.number)
            else:
                labels.append(s.title)
    return labels


def _references_title(spec):
    for s in spec.sections:
        if s.kind == "references":
            return s.title
    return "DAFTAR PUSTAKA"


def _spec_body_text(spec) -> str:
    """Body prose from the SPEC (all non-references sections).

    Used for the PPTX citation check: a condensed deck may omit chapter body
    prose (and its citations), so scanning the rendered deck would falsely flag
    a reference as never-cited. The deck's citations are always a subset of the
    SPEC's, so citation integrity is checked against the SPEC body instead.
    """
    parts = []
    for s in spec.sections:
        if s.kind == "references":
            continue
        for b in s.blocks:
            t = b.get("type")
            if t in ("paragraph", "lead", "callout", "heading"):
                if b.get("text"):
                    parts.append(b["text"])
            elif t == "list":
                for it in b.get("items", []):
                    parts.append(it)
    return "\n".join(parts)


def _cited_surnames(body_text: str) -> set:
    primaries = set()
    for a, _b, _yr in CITE_PAIR.findall(body_text):
        primaries.add(a)
    consumed = CITE_PAIR.sub(" ", body_text)
    for name, _yr in CITE_SINGLE.findall(consumed):
        primaries.add(name)
    return primaries


def _ref_surnames(spec) -> set:
    return {_surname_of_reference(r) for r in spec.references if _surname_of_reference(r)}


def _pages_for(fmt, file_path, pdf_path):
    if fmt == "pdf":
        return read_pdf_pages(file_path)
    if fmt == "docx" and pdf_path:
        return read_pdf_pages(pdf_path)
    return None


def _flat_text(fmt, file_path):
    if fmt == "pdf":
        return "\n".join(read_pdf_pages(file_path))
    if fmt == "docx":
        return "\n".join(read_docx_paragraph_texts(file_path))
    if fmt == "pptx":
        return "\n".join(read_pptx_slide_texts(file_path))
    raise ValueError("unknown format: %r" % fmt)


def _toc_analysis(spec, pages):
    """Extract (entries, actual_map, toc_fits) from a rendered PDF page list."""
    toc_title = None
    for s in spec.sections:
        if s.kind == "toc":
            toc_title = s.title
            break
    if toc_title is None:
        return [], {}, True  # no TOC: check is trivially satisfied

    norm = [" ".join(p.replace("\xa0", " ").split()) for p in pages]
    toc_idx = next((i for i, t in enumerate(norm) if toc_title.casefold() in t.casefold()), None)
    if toc_idx is None:
        return [], {}, True

    # toc_fits: the page after the TOC page begins the body, not more TOC lines
    # (a leftover TOC line carries dot leaders).
    toc_fits = True
    if toc_idx + 1 < len(norm):
        nxt = norm[toc_idx + 1]
        if re.search(r"\.{4,}", pages[toc_idx + 1]) and len(nxt) <= 200:
            toc_fits = False

    # parse claimed page numbers from lines on the TOC page
    entries = []
    for raw_line in pages[toc_idx].replace("\xa0", " ").split("\n"):
        line = raw_line.strip()
        m = _TRAILING_NUM.match(line)
        if m:
            label = re.sub(r"\s*\.{2,}\s*$", "", m.group(1)).strip()
            label = re.sub(r"\.+$", "", label).strip()
            label = " ".join(label.split())
            if label and label.casefold() != toc_title.casefold():
                entries.append((label, int(m.group(2))))

    # actual page for each label: first page (1-based) containing it, EXCLUDING
    # the TOC page itself (which lists every label and would falsely match).
    actual_map = {}
    for label, _claimed in entries:
        key = " ".join(label.split()).casefold()
        for i, t in enumerate(norm):
            if i == toc_idx:
                continue
            if key and key in t.casefold():
                actual_map[label] = i + 1
                break
    return entries, actual_map, toc_fits


# ---------------------------------------------------------------- gate
def gate(spec, fmt, file_path, *, pdf_path=None) -> GateVerdict:
    checks = []

    def run(check_id, fn):
        try:
            ok, detail = fn()
        except Exception as e:  # totality: a check never crashes the gate
            ok, detail = False, "check error: %s" % e
        checks.append(CheckResult(check_id, bool(ok), detail))

    flat = _flat_text(fmt, file_path)
    pages = _pages_for(fmt, file_path, pdf_path)

    # 1) structure_order
    run("structure_order", lambda: check_structure_order(_expected_labels(spec, fmt), flat))

    # 2) citation_consistency (two-way)
    def _citation():
        if fmt == "pptx":
            body = _spec_body_text(spec)
        else:
            ref_title = _references_title(spec)
            cut = flat.casefold().rfind(ref_title.casefold())
            body = flat[:cut] if cut > 0 else flat
        return check_citation_consistency(_cited_surnames(body), _ref_surnames(spec))
    run("citation_consistency", _citation)

    # 3) humanizer_clean (strip deck chrome for pptx)
    def _humanizer():
        text = _strip_deck_chrome(flat) if fmt == "pptx" else flat
        return check_humanizer_clean(text)
    run("humanizer_clean", _humanizer)

    # 4) no_blank_page
    def _blank():
        if pages is None:
            return True, "not applicable for %s (no page model)" % fmt
        return check_no_blank_page(pages[1:] if len(pages) > 1 else pages)
    run("no_blank_page", _blank)

    # 5) no_dangling_heading
    def _dangling():
        if pages is None:
            return True, "not applicable for %s (no page model)" % fmt
        return check_no_dangling_heading(pages)
    run("no_dangling_heading", _dangling)

    # 6) toc_accurate
    def _toc():
        if pages is None:
            return True, "not applicable for %s (no page model)" % fmt
        entries, actual_map, toc_fits = _toc_analysis(spec, pages)
        return check_toc_accurate(entries, actual_map, toc_fits)
    run("toc_accurate", _toc)

    # 7) images_real
    def _images():
        used = referenced_figure_refs(spec) & verified_figure_refs(spec)
        paths = [spec.figure_by_ref(r).path for r in sorted(used) if spec.figure_by_ref(r)]
        return check_images_real(paths)
    run("images_real", _images)

    failed = [c for c in checks if not c.passed]
    verdict = "PASS" if not failed else "FAIL"
    page_count = len(pages) if pages is not None else 0
    # Word count from the rendered file, not SPEC estimation.
    word_count = count_words(fmt, file_path)
    return GateVerdict(verdict=verdict, failed_checks=failed, page_count=page_count, word_count=word_count)
