"""Property, determinism, and anti-regression tests for the Output_Gate."""
from __future__ import annotations

import copy
import os
import tempfile

from hypothesis import given, settings
from hypothesis import strategies as st

from docfactory import gate as G
from docfactory.gate import (
    check_citation_consistency,
    check_humanizer_clean,
    check_images_real,
    check_no_blank_page,
    check_no_dangling_heading,
    check_structure_order,
    check_toc_accurate,
    gate,
)
from docfactory.renderers import pdf as pdf_renderer
from docfactory.spec import GateVerdict, parse_spec
from strategies import dirty_text
from test_renderers import _prepare, small_spec

LABEL_POOL = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel"]
SURNAME_POOL = ["Rogers", "Corey", "Brammer", "Prayitno", "Willis", "Gladding"]


# Feature: jarvis-document-factory, Property 14: Structure and order check
@settings(max_examples=100)
@given(st.lists(st.sampled_from(LABEL_POOL), min_size=1, max_size=6, unique=True), st.randoms())
def test_property_14_structure_order(labels, rnd):
    perm = labels[:]
    rnd.shuffle(perm)
    flat = " filler ".join(perm)
    ok, _ = check_structure_order(labels, flat)
    assert ok == (perm == labels)


def test_property_14_missing_label_fails():
    ok, _ = check_structure_order(["Alpha", "Bravo"], "Alpha only here")
    assert ok is False


# Feature: jarvis-document-factory, Property 15: Two-way citation-reference consistency check
@settings(max_examples=100)
@given(
    st.sets(st.sampled_from(SURNAME_POOL), max_size=6),
    st.sets(st.sampled_from(SURNAME_POOL), max_size=6),
)
def test_property_15_citation_consistency(cited, refs):
    ok, _ = check_citation_consistency(cited, refs)
    assert ok == (cited == refs)


# Feature: jarvis-document-factory, Property 16: Humanizer-clean gate check
@settings(max_examples=100)
@given(st.one_of(dirty_text, st.text(alphabet="abcdefg .,'\"", max_size=40)))
def test_property_16_humanizer_clean_check(text):
    from docfactory.humanizer import is_humanizer_clean

    ok, _ = check_humanizer_clean(text)
    assert ok == is_humanizer_clean(text)


# Feature: jarvis-document-factory, Property 17: No blank or near-empty page check
@settings(max_examples=100)
@given(st.lists(st.text(alphabet="abcde ", min_size=0, max_size=30), min_size=1, max_size=8))
def test_property_17_no_blank_page(pages):
    threshold = G.NEAR_EMPTY_THRESHOLD
    ok, _ = check_no_blank_page(pages, threshold)
    expected = all(len(" ".join(p.split())) >= threshold for p in pages)
    assert ok == expected


# Feature: jarvis-document-factory, Property 18: No dangling heading check
@settings(max_examples=100)
@given(st.lists(st.one_of(
    st.sampled_from(["BAB I", "BAB II", "BAB III", "BAB IV"]),
    st.text(alphabet="abcde ", min_size=15, max_size=40),
), min_size=1, max_size=8))
def test_property_18_no_dangling_heading(pages):
    ok, _ = check_no_dangling_heading(pages)
    import re
    expected = not any(re.fullmatch(r"BAB [IVXLCDM]+", " ".join(p.split())) for p in pages)
    assert ok == expected


# Feature: jarvis-document-factory, Property 19: Table-of-contents accuracy check
@settings(max_examples=100)
@given(
    st.lists(st.tuples(st.sampled_from(LABEL_POOL), st.integers(1, 50)), max_size=6),
    st.booleans(),
    st.booleans(),
)
def test_property_19_toc_accurate(raw_entries, fits, corrupt):
    # dedupe labels, build a consistent actual_map, then optionally corrupt one number
    entries = []
    actual_map = {}
    seen = set()
    for label, page in raw_entries:
        if label in seen:
            continue
        seen.add(label)
        entries.append((label, page))
        actual_map[label] = page
    if corrupt and entries:
        label, page = entries[0]
        entries[0] = (label, page + 1)  # claimed != actual
    ok, _ = check_toc_accurate(entries, actual_map, fits)
    all_match = all(actual_map.get(l) == c for l, c in entries)
    assert ok == (fits and all_match)


# Feature: jarvis-document-factory, Property 20: Embedded images are real (gate)
@settings(max_examples=100, deadline=None)
@given(st.lists(st.booleans(), min_size=0, max_size=6))
def test_property_20_images_real(exists_flags):
    with tempfile.TemporaryDirectory() as d:
        paths = []
        for i, exists in enumerate(exists_flags):
            p = os.path.join(d, "img%d.png" % i)
            if exists:
                with open(p, "wb") as fh:
                    fh.write(b"x")
            paths.append(p)
        ok, _ = check_images_real(paths)
        assert ok == all(exists_flags)


# ---- gate-level properties (render real files) ----
# Feature: jarvis-document-factory, Property 10: Gate totality
@settings(max_examples=40, deadline=None)
@given(small_spec())
def test_property_10_gate_totality(data):
    spec = _prepare(data)
    from docfactory.orchestrator import render_all

    with tempfile.TemporaryDirectory() as d:
        res = render_all(spec, d, basename="doc")
        pdf_path = res["results"].get("pdf")
        pdf_path = pdf_path.out_path if pdf_path else None
        for fmt, r in res["results"].items():
            verdict = gate(spec, fmt, r.out_path, pdf_path=pdf_path)
            assert isinstance(verdict, GateVerdict)
            assert verdict.verdict in ("PASS", "FAIL")


# Feature: jarvis-document-factory, Property 12: Gate FAIL returns a described check list
def test_property_12_pass_empty_fail_described():
    # a clean, well-formed document passes with an empty failed list
    good = {
        "doc_id": "g", "formats": ["pdf"], "is_academic": False,
        "identity": {"title": "Judul Dokumen", "authors": []},
        "style": {"page_size": "A4", "font": "Times New Roman"},
        "sections": [
            {"id": "kp", "kind": "frontmatter", "title": "KATA PENGANTAR",
             "blocks": [{"type": "paragraph", "text": "Kalimat pengantar yang cukup panjang untuk mengisi halaman."}]},
            {"id": "b1", "kind": "chapter", "number": "I", "title": "PENDAHULUAN",
             "blocks": [{"type": "paragraph", "text": "Isi bab satu yang memadai panjangnya untuk halaman penuh."}]},
        ],
        "references": [], "figures": [],
    }
    spec = _prepare(copy.deepcopy(good))
    with tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "good.pdf")
        pdf_renderer.render(spec, out)
        v = gate(spec, "pdf", out)
        assert v.verdict == "PASS"
        assert v.failed_checks == []

    # a document with an em-dash injected AFTER humanizing fails, with descriptions
    dirty_spec = _prepare(copy.deepcopy(good))
    dirty_spec.sections[1].blocks[0]["text"] = "Kalimat dengan em dash \u2014 yang bocor ke prosa."
    with tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "dirty.pdf")
        pdf_renderer.render(dirty_spec, out)
        v = gate(dirty_spec, "pdf", out)
        assert v.verdict == "FAIL"
        assert len(v.failed_checks) >= 1
        assert all(c.detail for c in v.failed_checks)
        assert any(c.check_id == "humanizer_clean" for c in v.failed_checks)


# Feature: jarvis-document-factory, Property 13: Gate determinism
@settings(max_examples=30, deadline=None)
@given(small_spec(formats=["pdf"]))
def test_property_13_gate_determinism(data):
    spec = _prepare(data)
    with tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "doc.pdf")
        pdf_renderer.render(spec, out)
        v1 = gate(spec, "pdf", out)
        v2 = gate(spec, "pdf", out)
        assert v1.verdict == v2.verdict
        assert [(c.check_id, c.passed, c.detail) for c in v1.failed_checks] == \
               [(c.check_id, c.passed, c.detail) for c in v2.failed_checks]


# ---- anti-regression: seeded with the real defects qa.py / qa_buku*.py catch ----
def test_seed_dangling_bab_heading():
    ok, _ = check_no_dangling_heading(["Isi normal yang panjang", "BAB II", "lanjut isi"])
    assert ok is False


def test_seed_toc_overflow():
    # TOC fits=False must fail regardless of numbers
    ok, _ = check_toc_accurate([("Alpha", 3)], {"Alpha": 3}, toc_fits=False)
    assert ok is False


def test_seed_one_directional_citation_gap():
    # citation without a reference entry
    ok, _ = check_citation_consistency({"Rogers"}, set())
    assert ok is False
    # reference entry never cited
    ok2, _ = check_citation_consistency(set(), {"Rogers"})
    assert ok2 is False


def test_seed_emdash_and_curly_leak():
    assert check_humanizer_clean("teks dengan \u2014 em-dash")[0] is False
    assert check_humanizer_clean("kutipan \u201ckeriting\u201d")[0] is False
    assert check_humanizer_clean("teks bersih biasa saja")[0] is True
