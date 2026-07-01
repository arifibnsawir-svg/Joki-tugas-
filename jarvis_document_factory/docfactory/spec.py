"""SPEC data model, parsing, round-tripping, and style resolution.

The SPEC is the single source of truth for every renderer. It generalizes the
content-as-data pattern from konten.py into typed JSON. Container objects are
dataclasses; content blocks stay as tagged dicts (a discriminated union keyed
by "type") so they round-trip losslessly and match the JSON on the wire.

Also defines the shared result dataclasses (RenderResult, CheckResult,
GateVerdict) used across renderers and the gate.
"""
from __future__ import annotations

import copy
from dataclasses import dataclass, field
from typing import Any

from .constants import ACADEMIC_STYLE_DEFAULTS


# --------------------------------------------------------------------------
# Shared result types (design Components section)
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class RenderResult:
    fmt: str
    out_path: str
    page_count: int
    word_count: int = 0
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class CheckResult:
    check_id: str
    passed: bool
    detail: str


@dataclass(frozen=True)
class GateVerdict:
    verdict: str  # "PASS" | "FAIL"
    failed_checks: list[CheckResult]
    page_count: int
    word_count: int = 0

    @property
    def is_pass(self) -> bool:
        return self.verdict == "PASS"


# --------------------------------------------------------------------------
# SPEC container dataclasses
# --------------------------------------------------------------------------
@dataclass
class Identity:
    title: str = ""
    subtitle: str = ""
    course: str = ""
    lecturer: str = ""
    authors: list[dict] = field(default_factory=list)  # [{name, id}]
    program: str = ""
    faculty: str = ""
    institution: str = ""
    year: str = ""
    logo: str = ""  # figure ref or path, optional

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "subtitle": self.subtitle,
            "course": self.course,
            "lecturer": self.lecturer,
            "authors": [dict(a) for a in self.authors],
            "program": self.program,
            "faculty": self.faculty,
            "institution": self.institution,
            "year": self.year,
            "logo": self.logo,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Identity":
        d = d or {}
        return cls(
            title=d.get("title", ""),
            subtitle=d.get("subtitle", ""),
            course=d.get("course", ""),
            lecturer=d.get("lecturer", ""),
            authors=[dict(a) for a in d.get("authors", [])],
            program=d.get("program", ""),
            faculty=d.get("faculty", ""),
            institution=d.get("institution", ""),
            year=d.get("year", ""),
            logo=d.get("logo", ""),
        )


@dataclass
class Style:
    page_size: str | None = None
    font: str | None = None
    font_size_pt: float | None = None
    line_spacing: float | None = None
    body_align: str | None = None
    page_numbers: str | None = None
    margins_cm: dict | None = None
    accent_color: str | None = None

    def to_dict(self) -> dict:
        out = {}
        for k in (
            "page_size", "font", "font_size_pt", "line_spacing",
            "body_align", "page_numbers", "margins_cm", "accent_color",
        ):
            v = getattr(self, k)
            if v is not None:
                out[k] = copy.deepcopy(v)
        return out

    @classmethod
    def from_dict(cls, d: dict) -> "Style":
        d = d or {}
        return cls(
            page_size=d.get("page_size"),
            font=d.get("font"),
            font_size_pt=d.get("font_size_pt"),
            line_spacing=d.get("line_spacing"),
            body_align=d.get("body_align"),
            page_numbers=d.get("page_numbers"),
            margins_cm=copy.deepcopy(d.get("margins_cm")),
            accent_color=d.get("accent_color"),
        )


@dataclass
class Section:
    id: str
    title: str
    kind: str = "chapter"
    number: str = ""
    blocks: list[dict] = field(default_factory=list)  # tagged block dicts
    pptx: dict = field(default_factory=dict)  # {layout?, notes?}

    def to_dict(self) -> dict:
        out = {
            "id": self.id,
            "kind": self.kind,
            "number": self.number,
            "title": self.title,
            "blocks": copy.deepcopy(self.blocks),
        }
        if self.pptx:
            out["pptx"] = copy.deepcopy(self.pptx)
        return out

    @classmethod
    def from_dict(cls, d: dict) -> "Section":
        return cls(
            id=d.get("id", ""),
            title=d.get("title", ""),
            kind=d.get("kind", "chapter"),
            number=d.get("number", ""),
            blocks=[dict(b) for b in d.get("blocks", [])],
            pptx=dict(d.get("pptx", {})),
        )


@dataclass
class Reference:
    id: str
    apa: str
    url: str = ""
    verified: bool = False

    def to_dict(self) -> dict:
        return {"id": self.id, "apa": self.apa, "url": self.url, "verified": self.verified}

    @classmethod
    def from_dict(cls, d: dict) -> "Reference":
        return cls(
            id=d.get("id", ""),
            apa=d.get("apa", ""),
            url=d.get("url", ""),
            verified=bool(d.get("verified", False)),
        )


@dataclass
class Figure:
    ref: str
    path: str
    caption: str = ""
    verified_path: bool = False

    def to_dict(self) -> dict:
        return {
            "ref": self.ref,
            "path": self.path,
            "caption": self.caption,
            "verified_path": self.verified_path,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Figure":
        return cls(
            ref=d.get("ref", ""),
            path=d.get("path", ""),
            caption=d.get("caption", ""),
            verified_path=bool(d.get("verified_path", False)),
        )


@dataclass
class SPEC:
    doc_id: str
    formats: list[str]
    identity: Identity
    spec_version: str = "1.0"
    doc_type: str = "report"
    is_academic: bool = False
    style: Style = field(default_factory=Style)
    sections: list[Section] = field(default_factory=list)
    references: list[Reference] = field(default_factory=list)
    figures: list[Figure] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "spec_version": self.spec_version,
            "doc_id": self.doc_id,
            "formats": list(self.formats),
            "doc_type": self.doc_type,
            "is_academic": self.is_academic,
            "identity": self.identity.to_dict(),
            "style": self.style.to_dict(),
            "sections": [s.to_dict() for s in self.sections],
            "references": [r.to_dict() for r in self.references],
            "figures": [f.to_dict() for f in self.figures],
        }

    def figure_by_ref(self, ref: str) -> Figure | None:
        for f in self.figures:
            if f.ref == ref:
                return f
        return None


def parse_spec(data: dict) -> SPEC:
    """Read a JSON-compatible dict into the typed SPEC model."""
    if not isinstance(data, dict):
        raise TypeError("SPEC data must be a dict, got %r" % type(data).__name__)
    return SPEC(
        doc_id=data.get("doc_id", ""),
        formats=list(data.get("formats", [])),
        identity=Identity.from_dict(data.get("identity", {})),
        spec_version=data.get("spec_version", "1.0"),
        doc_type=data.get("doc_type", "report"),
        is_academic=bool(data.get("is_academic", False)),
        style=Style.from_dict(data.get("style", {})),
        sections=[Section.from_dict(s) for s in data.get("sections", [])],
        references=[Reference.from_dict(r) for r in data.get("references", [])],
        figures=[Figure.from_dict(f) for f in data.get("figures", [])],
    )


def spec_to_dict(spec: SPEC) -> dict:
    """Inverse of parse_spec for round-tripping."""
    return spec.to_dict()


def resolve_style(spec: SPEC) -> dict:
    """Return the effective style, filling academic defaults where not overridden.

    For any academic SPEC, each style field resolves to the request value when
    provided and otherwise to the academic default (Requirements 11.1, 11.2).
    Non-academic SPECs still receive sensible defaults so renderers always have
    a complete style, but only academic SPECs are guaranteed the academic set.
    """
    resolved: dict[str, Any] = {}
    provided = spec.style.to_dict()
    use_defaults = spec.is_academic
    for key, default in ACADEMIC_STYLE_DEFAULTS.items():
        if key in provided and provided[key] is not None:
            resolved[key] = copy.deepcopy(provided[key])
        elif use_defaults:
            resolved[key] = copy.deepcopy(default)
        else:
            # non-academic: still fall back to the same defaults so renderers
            # have a complete style block to work with.
            resolved[key] = copy.deepcopy(default)
    return resolved
