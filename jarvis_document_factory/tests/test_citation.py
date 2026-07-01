"""Property tests for the citation layer (cite-or-abstain, exclude unverified, Indonesian-first)."""
from __future__ import annotations

from hypothesis import given, settings
from hypothesis import strategies as st

from docfactory.citation import (
    _citations_in,
    apply_citation_layer,
    order_indonesian_first,
    verified_surnames,
)
from docfactory.spec import parse_spec

SURNAME_POOL = [
    "Rogers", "Corey", "Brammer", "Prayitno", "Willis",
    "Gladding", "Lubis", "Sukardi", "Hidayat", "Nurihsan",
]


@st.composite
def academic_citation_spec(draw):
    authors = draw(st.lists(st.sampled_from(SURNAME_POOL), min_size=1, max_size=6, unique=True))
    verified_map = {a: draw(st.booleans()) for a in authors}
    references = [
        {"id": "r%d" % i, "apa": "%s, X. (2020). Judul karya. Penerbit." % a,
         "url": "", "verified": verified_map[a]}
        for i, a in enumerate(authors)
    ]
    nsec = draw(st.integers(min_value=1, max_value=3))
    sections = []
    for si in range(nsec):
        blocks = []
        for _ in range(draw(st.integers(min_value=1, max_value=3))):
            cite = draw(st.lists(st.sampled_from(authors), min_size=0, max_size=3, unique=True))
            text = "Pembahasan teori. " + " ".join("%s (2020)" % a for a in cite) + " menjelaskan hal."
            blocks.append({"type": "paragraph", "text": text})
        sections.append({"id": "s%d" % si, "kind": "chapter", "title": "Bab", "blocks": blocks})
    data = {
        "doc_id": "c", "formats": ["pdf"], "is_academic": True,
        "identity": {"title": "T"},
        "style": {"page_size": "A4", "font": "Times New Roman"},
        "sections": sections, "references": references, "figures": [],
    }
    return data, verified_map


# Feature: jarvis-document-factory, Property 22: Only verifiable citations survive
@settings(max_examples=100)
@given(academic_citation_spec())
def test_property_22_only_verifiable_citations_survive(pair):
    data, verified_map = pair
    spec = parse_spec(data)
    apply_citation_layer(spec)
    verified = {a for a, ok in verified_map.items() if ok}
    for section in spec.sections:
        for block in section.blocks:
            if block.get("type") in ("paragraph", "lead", "callout"):
                for surname in _citations_in(block.get("text", "")):
                    assert surname in verified, (surname, verified)


# Feature: jarvis-document-factory, Property 23: Unverified source identifiers are excluded
@settings(max_examples=100)
@given(academic_citation_spec())
def test_property_23_unverified_identifiers_excluded(pair):
    data, _ = pair
    spec = parse_spec(data)
    apply_citation_layer(spec)
    # every surviving reference is verified, so any surviving url/doi belongs to one
    assert all(r.verified for r in spec.references)
    surviving = verified_surnames(spec.references)
    for r in spec.references:
        assert r.verified is True
    # no reference carries an identifier without being verified
    for r in spec.references:
        if r.url:
            assert r.verified


# Feature: jarvis-document-factory, Property 24: Indonesian-first source ordering
@settings(max_examples=100)
@given(st.lists(
    st.fixed_dictionaries({
        "relevance": st.sampled_from([0.2, 0.5, 0.8, 1.0]),
        "indonesian": st.booleans(),
        "tag": st.integers(min_value=0, max_value=999),
    }),
    min_size=0, max_size=12,
))
def test_property_24_indonesian_first_ordering(sources):
    ordered = order_indonesian_first(
        sources,
        relevance_key=lambda s: s["relevance"],
        indonesian_key=lambda s: s["indonesian"],
    )
    buckets = [round(s["relevance"], 1) for s in ordered]
    # relevance buckets are non-increasing (higher relevance first)
    assert buckets == sorted(buckets, reverse=True)
    # within any comparable (equal) bucket, no international precedes an Indonesian
    for i in range(len(ordered)):
        for j in range(i + 1, len(ordered)):
            if buckets[i] == buckets[j]:
                assert not (ordered[i]["indonesian"] is False and ordered[j]["indonesian"] is True)


def test_non_academic_citation_layer_is_noop():
    data = {
        "doc_id": "c", "formats": ["pdf"], "is_academic": False,
        "identity": {"title": "T"}, "style": {"page_size": "A4", "font": "Times New Roman"},
        "sections": [{"id": "s0", "kind": "chapter", "title": "Bab",
                      "blocks": [{"type": "paragraph", "text": "Teori X (2020) penting."}]}],
        "references": [{"id": "r0", "apa": "X (2020).", "url": "", "verified": False}],
        "figures": [],
    }
    spec = parse_spec(data)
    apply_citation_layer(spec)
    # unchanged: unverified reference stays because the doc is not academic
    assert len(spec.references) == 1
