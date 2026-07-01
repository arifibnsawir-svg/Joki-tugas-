"""SPEC validation and required-field-per-format rules.

Validation runs after the always-on layers and image resolution, and before
any renderer. It raises a structured error naming the first problem, so a bad
SPEC never reaches a binary writer (Requirements 1.5, 2.4, 8.2, 11.1, 12.3).
"""
from __future__ import annotations

from .constants import ACADEMIC_STYLE_DEFAULTS, SUPPORTED_FORMATS
from .errors import MissingImageError, SpecValidationError, UnsupportedFormatError
from .spec import SPEC


def _first_fmt(spec: SPEC) -> str:
    return spec.formats[0] if spec.formats else "pdf"


def _effective_style_value(spec: SPEC, key: str):
    """Value of a style field considering explicit value then academic default.

    A non-academic SPEC gets no automatic academic default here, so a missing
    field required by a format is a real validation failure it can hit.
    """
    provided = spec.style.to_dict()
    if key in provided and provided[key] is not None:
        return provided[key]
    if spec.is_academic:
        return ACADEMIC_STYLE_DEFAULTS.get(key)
    return None


def _has_content_block(section) -> bool:
    for b in section.blocks:
        if b.get("type") in ("list", "paragraph", "lead"):
            return True
    return False


def validate(spec: SPEC) -> None:
    """Validate a SPEC, raising on the first problem. Returns None on success."""
    # ---- formats: presence + supported tokens (checked first) ----
    if not spec.formats:
        raise SpecValidationError("formats", _first_fmt(spec), "no output format requested")
    for token in spec.formats:
        if token not in SUPPORTED_FORMATS:
            raise UnsupportedFormatError(token)

    # ---- common: identity.title ----
    if not (spec.identity.title or "").strip():
        raise SpecValidationError("identity.title", _first_fmt(spec), "document title is empty")

    # ---- common: sections present, unique ids, titled ----
    if not spec.sections:
        raise SpecValidationError("sections", _first_fmt(spec), "at least one section is required")
    seen_ids: set[str] = set()
    for i, s in enumerate(spec.sections):
        if not (s.id or "").strip():
            raise SpecValidationError("sections[%d].id" % i, _first_fmt(spec), "section id is empty")
        if s.id in seen_ids:
            raise SpecValidationError(
                "sections[%d].id" % i, _first_fmt(spec), "duplicate section id %r" % s.id
            )
        seen_ids.add(s.id)
        if not (s.title or "").strip():
            raise SpecValidationError(
                "sections[%d].title" % i, _first_fmt(spec), "section %r has no title" % s.id
            )

    # ---- common: figure blocks must reference a verified figure ----
    for s in spec.sections:
        for b in s.blocks:
            if b.get("type") == "figure":
                ref = b.get("ref", "")
                fig = spec.figure_by_ref(ref)
                if fig is None:
                    raise MissingImageError(ref, "<no figure registry entry>")
                if not fig.verified_path:
                    raise MissingImageError(ref, fig.path)

    # ---- academic: non-empty references ----
    if spec.is_academic and not spec.references:
        raise SpecValidationError("references", "academic", "academic document needs references")

    has_toc = any(s.kind == "toc" for s in spec.sections)
    has_chapter = any(s.kind == "chapter" for s in spec.sections)

    # ---- per-format: pdf and docx ----
    for fmt in ("pdf", "docx"):
        if fmt in spec.formats:
            if _effective_style_value(spec, "page_size") is None:
                raise SpecValidationError("style.page_size", fmt, "page size is required")
            if _effective_style_value(spec, "font") is None:
                raise SpecValidationError("style.font", fmt, "font is required")
            if has_toc and not has_chapter:
                raise SpecValidationError(
                    "sections[chapter]", fmt,
                    "a table-of-contents section requires at least one chapter section",
                )

    # ---- per-format: pptx ----
    if "pptx" in spec.formats:
        for s in spec.sections:
            layout = (s.pptx or {}).get("layout")
            if layout == "bullets" and not _has_content_block(s):
                raise SpecValidationError(
                    "sections[%s].blocks" % s.id, "pptx",
                    "bullets layout needs at least one list or paragraph block",
                )
