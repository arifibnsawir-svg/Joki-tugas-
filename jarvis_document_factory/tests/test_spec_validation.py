"""Property tests for SPEC schema, style resolution, validation, format rejection."""
from __future__ import annotations

import copy

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from docfactory.constants import ACADEMIC_STYLE_DEFAULTS
from docfactory.errors import SpecValidationError, UnsupportedFormatError
from docfactory.spec import Identity, Reference, Section, parse_spec, resolve_style, spec_to_dict
from docfactory.validation import validate
from strategies import clean_text, valid_spec_dicts


# Feature: jarvis-document-factory, Property 4: SPEC schema conformance
@settings(max_examples=100)
@given(valid_spec_dicts())
def test_property_4_spec_schema_conformance(data):
    spec = parse_spec(data)
    assert isinstance(spec.identity, Identity)
    assert isinstance(spec.sections, list) and len(spec.sections) >= 1
    for s in spec.sections:
        assert isinstance(s, Section)
        assert isinstance(s.blocks, list)
    assert isinstance(spec.references, list)
    assert all(isinstance(r, Reference) for r in spec.references)
    assert isinstance(spec.figures, list)
    # ordered sections: round-trip preserves the exact section order
    round_tripped = parse_spec(spec_to_dict(spec))
    assert [s.id for s in round_tripped.sections] == [s.id for s in spec.sections]
    assert spec_to_dict(round_tripped) == spec_to_dict(spec)


# Strategy: academic SPEC with a random subset of explicit style overrides.
@st.composite
def academic_spec_with_overrides(draw):
    data = draw(valid_spec_dicts(require_academic=True))
    overrides = {}
    if draw(st.booleans()):
        overrides["font"] = draw(st.sampled_from(["Georgia", "Arial", "Cambria"]))
    if draw(st.booleans()):
        overrides["font_size_pt"] = draw(st.sampled_from([10, 11, 13, 14]))
    if draw(st.booleans()):
        overrides["line_spacing"] = draw(st.sampled_from([1.0, 1.15, 2.0]))
    if draw(st.booleans()):
        overrides["body_align"] = draw(st.sampled_from(["left", "center"]))
    if draw(st.booleans()):
        overrides["page_numbers"] = draw(st.sampled_from(["roman", "none"]))
    if draw(st.booleans()):
        overrides["accent_color"] = draw(st.sampled_from(["#000000", "#2563EB"]))
    data["style"] = overrides
    return data, overrides


# Feature: jarvis-document-factory, Property 28: Academic style resolution
@settings(max_examples=100)
@given(academic_spec_with_overrides())
def test_property_28_academic_style_resolution(pair):
    data, overrides = pair
    spec = parse_spec(data)
    resolved = resolve_style(spec)
    for key, default in ACADEMIC_STYLE_DEFAULTS.items():
        if key in overrides and overrides[key] is not None:
            assert resolved[key] == overrides[key], key
        else:
            assert resolved[key] == default, key


# Feature: jarvis-document-factory, Property 5: Missing required field fails before rendering
@settings(max_examples=100)
@given(valid_spec_dicts())
def test_property_5_missing_title_fails(data):
    # sanity: the unmodified spec validates
    validate(parse_spec(data))
    broken = copy.deepcopy(data)
    broken["identity"]["title"] = "   "
    with pytest.raises(SpecValidationError) as ei:
        validate(parse_spec(broken))
    assert ei.value.field == "identity.title"


@settings(max_examples=100)
@given(valid_spec_dicts(require_academic=True))
def test_property_5_missing_references_fails_for_academic(data):
    broken = copy.deepcopy(data)
    broken["references"] = []
    with pytest.raises(SpecValidationError) as ei:
        validate(parse_spec(broken))
    assert ei.value.field == "references"


def test_property_5_missing_pagesize_fails_for_nonacademic_pdf():
    data = {
        "doc_id": "x", "formats": ["pdf"], "is_academic": False,
        "identity": {"title": "A Title"},
        "style": {"font": "Times New Roman"},  # no page_size
        "sections": [{"id": "s0", "kind": "chapter", "title": "Intro", "blocks": []}],
        "references": [], "figures": [],
    }
    with pytest.raises(SpecValidationError) as ei:
        validate(parse_spec(data))
    assert ei.value.field == "style.page_size"
    assert ei.value.fmt == "pdf"


def test_toc_without_chapter_fails():
    data = {
        "doc_id": "x", "formats": ["pdf"], "is_academic": False,
        "identity": {"title": "A Title"},
        "style": {"page_size": "A4", "font": "Times New Roman"},
        "sections": [{"id": "toc", "kind": "toc", "title": "Daftar Isi", "blocks": []}],
        "references": [], "figures": [],
    }
    with pytest.raises(SpecValidationError) as ei:
        validate(parse_spec(data))
    assert ei.value.field == "sections[chapter]"


# Feature: jarvis-document-factory, Property 2: Unsupported format is rejected by name
@settings(max_examples=100)
@given(valid_spec_dicts(), st.text(min_size=1, max_size=8).filter(lambda t: t not in ("pdf", "docx", "pptx")))
def test_property_2_unsupported_format_rejected_by_name(data, bad_token):
    broken = copy.deepcopy(data)
    broken["formats"] = [bad_token]
    with pytest.raises(UnsupportedFormatError) as ei:
        validate(parse_spec(broken))
    msg = str(ei.value)
    assert "pdf" in msg and "docx" in msg and "pptx" in msg
