"""Property + unit tests for Router, the ARSI loop, DONE authority, delegation."""
from __future__ import annotations

import os
import tempfile

from hypothesis import given, settings
from hypothesis import strategies as st

from docfactory.delegation import (
    accept_worker_result,
    brief_for_section,
    make_brief,
    WorkerResult,
)
from docfactory.orchestrator import OutputState, run_pipeline
from docfactory.router import DELEGATION_SECTION_THRESHOLD, select_route
from docfactory.spec import parse_spec


def _spec_with_sections(n, formats=("pdf",)):
    roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
             "XI", "XII", "XIII", "XIV", "XV", "XVI"]
    sections = [
        {"id": "b%d" % i, "kind": "chapter",
         "number": roman[i] if i < len(roman) else str(i + 1), "title": "Bab %d" % i,
         "blocks": [{"type": "paragraph", "text": "Isi bab yang memadai panjangnya."}]}
        for i in range(n)
    ]
    return parse_spec({
        "doc_id": "x", "formats": list(formats), "is_academic": False,
        "identity": {"title": "Judul Dokumen", "authors": []},
        "style": {"page_size": "A4", "font": "Times New Roman"},
        "sections": sections, "references": [], "figures": [],
    })


# Feature: jarvis-document-factory, Property 11: DONE authority rests with the gate
@settings(max_examples=100)
@given(st.lists(st.sampled_from(["PASS", "FAIL"]), min_size=1, max_size=8))
def test_property_11_done_authority(verdicts):
    state = OutputState()
    for v in verdicts:
        state.record(v)
    assert state.is_done == (verdicts[-1] == "PASS")
    assert state.status == ("DONE" if verdicts[-1] == "PASS" else "AWAITING_GATE")


def test_property_11_no_verdict_is_not_done():
    state = OutputState()
    assert state.is_done is False
    assert state.status == "AWAITING_GATE"


# Feature: jarvis-document-factory, Property 29: Delegation brief completeness
@settings(max_examples=100)
@given(st.integers(min_value=1, max_value=6))
def test_property_29_brief_completeness(n):
    spec = _spec_with_sections(n)
    for section in spec.sections:
        brief = brief_for_section(spec, section)
        assert brief.is_complete()
        assert brief.context.strip()
        assert len(brief.pass_criteria) > 0


def test_property_29_incomplete_brief_detected():
    assert make_brief("s", "", ["ok"]).is_complete() is False
    assert make_brief("s", "context here", []).is_complete() is False


# Feature: jarvis-document-factory, Property 30: Small jobs run directly
@settings(max_examples=100)
@given(st.integers(min_value=1, max_value=20))
def test_property_30_small_jobs_run_directly(n):
    spec = _spec_with_sections(n)
    route = select_route(spec)
    assert route.delegate == (n >= DELEGATION_SECTION_THRESHOLD)
    if n < DELEGATION_SECTION_THRESHOLD:
        assert route.delegate is False


# Feature: jarvis-document-factory, Property 31: Worker results are accepted only on PASS
@settings(max_examples=100)
@given(
    st.lists(st.sampled_from(["a", "b", "c", "d"]), min_size=1, max_size=4, unique=True),
    st.lists(st.sampled_from(["a", "b", "c", "d"]), min_size=0, max_size=4, unique=True),
)
def test_property_31_worker_accept_iff_pass(pass_criteria, satisfied):
    brief = make_brief("s", "ctx", pass_criteria)
    result = WorkerResult(subtask_id="s", satisfied_criteria=satisfied)
    accepted = accept_worker_result(brief, result)
    assert accepted == set(pass_criteria).issubset(set(satisfied))


# ---- ARSI loop ordering ----
def test_loop_ordering_happy_path():
    spec = _spec_with_sections(2)
    with tempfile.TemporaryDirectory() as d:
        res = run_pipeline(spec, d, basename="doc")
        assert res.trace == ["audit", "rancang", "sistemasi", "iterasi"]
        assert res.status == "DONE"
        assert res.iterations == 1


def test_loop_rerenders_only_after_fail():
    # academic SPEC with a verified reference that is never cited -> gate FAIL
    data = {
        "doc_id": "fix", "formats": ["pdf"], "is_academic": True,
        "identity": {"title": "Judul Dokumen", "authors": []},
        "style": {"page_size": "A4", "font": "Times New Roman"},
        "sections": [
            {"id": "b1", "kind": "chapter", "number": "I", "title": "PENDAHULUAN",
             "blocks": [{"type": "paragraph", "text": "Isi bab tanpa sitasi apa pun di dalamnya."}]},
            {"id": "dp", "kind": "references", "title": "DAFTAR PUSTAKA", "blocks": []},
        ],
        "references": [{"id": "r", "apa": "Rogers, C. R. (1961). On becoming a person. Houghton Mifflin.",
                        "url": "", "verified": True}],
        "figures": [],
    }

    def fix_fn(spec, failed):
        # correction: drop the uncited reference and mark non-academic
        spec.is_academic = False
        spec.references = []
        return spec

    spec = parse_spec(data)
    with tempfile.TemporaryDirectory() as d:
        res = run_pipeline(spec, d, basename="doc", fix_fn=fix_fn, max_iterations=3)
        assert res.status == "DONE"
        assert res.iterations == 2
        # two full Sistemasi/Iterasi cycles: fail then fixed
        assert res.trace == ["audit", "rancang", "sistemasi", "iterasi", "sistemasi", "iterasi"]


def test_pipeline_awaiting_gate_without_fix():
    # same failing SPEC, but no fix_fn -> stays AWAITING_GATE (model cannot declare DONE)
    data = {
        "doc_id": "await", "formats": ["pdf"], "is_academic": True,
        "identity": {"title": "Judul Dokumen", "authors": []},
        "style": {"page_size": "A4", "font": "Times New Roman"},
        "sections": [
            {"id": "b1", "kind": "chapter", "number": "I", "title": "PENDAHULUAN",
             "blocks": [{"type": "paragraph", "text": "Isi bab tanpa sitasi sama sekali."}]},
            {"id": "dp", "kind": "references", "title": "DAFTAR PUSTAKA", "blocks": []},
        ],
        "references": [{"id": "r", "apa": "Rogers, C. R. (1961). On becoming a person. Houghton Mifflin.",
                        "url": "", "verified": True}],
        "figures": [],
    }
    spec = parse_spec(data)
    with tempfile.TemporaryDirectory() as d:
        res = run_pipeline(spec, d, basename="doc")
        assert res.status == "AWAITING_GATE"
        assert res.iterations == 1
