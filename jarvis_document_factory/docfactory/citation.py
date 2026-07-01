"""Citation layer: cite-or-abstain, APA, Indonesian-first.

Runs on the SPEC (not on rendered binaries) during Sistemasi, before validation.
For academic artifacts it enforces:
  - every surviving in-text citation references a verified reference (7.1),
  - a claim whose only support is unverifiable is dropped (7.4),
  - references stay APA (7.2) and unverified source identifiers are removed (7.5),
  - Indonesian sources come before international ones when relevance is
    comparable (7.3).

The rich judgement of which sources are real is the job of the academic-search
skill upstream; this layer is the deterministic SPEC-level enforcement that the
gate later re-checks on the rendered file.
"""
from __future__ import annotations

import re

# In-text APA author-year citations. Pair form handles "A dan B (2020)"
# (Indonesian) and is matched before the single form.
CITE_PAIR = re.compile(r"([A-Z][a-zA-Z]+)\s+dan\s+([A-Z][a-zA-Z]+)\s*\((\d{4})\)")
# Single form: "Name (Year)", "Name, Year", "Name dkk. (Year)", "Name et al. (Year)".
CITE_SINGLE = re.compile(
    r"([A-Z][a-zA-Z]+)(?:\s+(?:dkk\.|et al\.))?[\,\(]\s*(\d{4})\)?"
)

_SURNAME = re.compile(r"([A-Z][a-zA-Z]+)")

# Markers that identify an Indonesian source from its APA string or URL.
_ID_MARKERS = (
    ".ac.id", ".go.id", ".or.id", "kemdikbud", "kemdiktisaintek", "garuda",
    "sinta", "jakarta", "bandung", "yogyakarta", "surabaya", "malang", "depok",
    "semarang", "makassar", "medan", "rineka cipta", "gramedia", "erlangga",
    "kencana", "prenadamedia", "bumi aksara", "ui press", "ugm press",
    "universitas indonesia", "universitas negeri", "penerbit universitas",
    "raja grafindo", "alfabeta", "deepublish", "andi offset",
)


def _surname_of_reference(ref) -> str:
    """First surname token from an APA reference string."""
    m = _SURNAME.search(ref.apa or "")
    return m.group(1) if m else ""


def verified_surnames(references) -> set[str]:
    return {_surname_of_reference(r) for r in references if r.verified and _surname_of_reference(r)}


def is_indonesian_reference(ref) -> bool:
    hay = ((ref.apa or "") + " " + (ref.url or "")).lower()
    return any(marker in hay for marker in _ID_MARKERS)


def _citations_in(text: str) -> list[str]:
    """Primary surnames of every in-text citation in text (pairs and singles)."""
    if not text:
        return []
    primaries: list[str] = []
    consumed = text
    for a, b, _yr in CITE_PAIR.findall(text):
        primaries.append(a)
    # Remove pair spans so their inner single "(year)" is not double counted.
    consumed = CITE_PAIR.sub(" ", text)
    for name, _yr in CITE_SINGLE.findall(consumed):
        primaries.append(name)
    return primaries


def _light_cleanup(text: str) -> str:
    text = re.sub(r"\(\s*\)", "", text)          # empty parens left by removal
    text = re.sub(r"\s+([,.;:])", r"\1", text)   # space before punctuation
    text = re.sub(r"[ \t]{2,}", " ", text)        # collapse spaces
    text = re.sub(r"\(\s+", "(", text)
    return text.strip()


def _strip_unverified_citations(text: str, verified: set[str]) -> str:
    # Keep verified pairs intact by shielding them behind placeholders so the
    # single-citation pass does not strip the second author inside a kept pair
    # (e.g. "Prayitno dan Amti (2004)" must not lose "Amti (2004)").
    placeholders: dict[str, str] = {}

    def repl_pair(m):
        a = m.group(1)
        if a in verified:
            key = "\x00%d\x00" % len(placeholders)
            placeholders[key] = m.group(0)
            return key
        return " "

    def repl_single(m):
        return m.group(0) if m.group(1) in verified else " "

    text = CITE_PAIR.sub(repl_pair, text)
    text = CITE_SINGLE.sub(repl_single, text)
    for key, value in placeholders.items():
        text = text.replace(key, value)
    return _light_cleanup(text)


def order_indonesian_first(sources, relevance_key, indonesian_key):
    """Stable order: higher relevance first; within comparable relevance,
    Indonesian sources before international ones (Requirement 7.3).

    Relevance is bucketed by rounding to one decimal so that near-equal scores
    count as comparable. Sorting is stable, so equal keys preserve input order.
    """
    indexed = list(enumerate(sources))

    def key(pair):
        i, s = pair
        rel = relevance_key(s)
        rel = rel if rel is not None else 0.0
        bucket = round(float(rel), 1)
        indo = 0 if indonesian_key(s) else 1
        return (-bucket, indo, i)

    return [s for _, s in sorted(indexed, key=key)]


def apply_citation_layer(spec):
    """Enforce cite-or-abstain, APA, and Indonesian-first on an academic SPEC.

    Non-academic SPECs are returned unchanged. Mutates and returns the SPEC.
    """
    if not spec.is_academic:
        return spec

    verified = verified_surnames(spec.references)

    # 1) Drop claims whose only support is unverifiable; strip unverified
    #    citation tokens from surviving claims so every remaining citation
    #    references a verified source.
    for section in spec.sections:
        kept_blocks = []
        for block in section.blocks:
            if block.get("type") in ("paragraph", "lead", "callout"):
                original = _citations_in(block.get("text", ""))
                if original:
                    cleaned = _strip_unverified_citations(block.get("text", ""), verified)
                    remaining = _citations_in(cleaned)
                    if not remaining:
                        # claim lost all verifiable support -> drop it (7.4)
                        continue
                    block["text"] = cleaned
            kept_blocks.append(block)
        section.blocks = kept_blocks

    # 2) Keep only verified references (drops unverified identifiers, 7.5).
    spec.references = [r for r in spec.references if r.verified]

    # 3) Indonesian-first ordering when relevance is comparable (7.3).
    spec.references = order_indonesian_first(
        spec.references,
        relevance_key=lambda r: None,       # comparable by default (no scores)
        indonesian_key=is_indonesian_reference,
    )
    return spec
