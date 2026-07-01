"""CLI tests for validate_spec.py (the pre-render SPEC validator).

Proves the three exit-code contracts an author relies on: 0 = render-ready,
1 = fixable SPEC problem, 2 = file/JSON could not be loaded.
"""
from __future__ import annotations

import json
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

import validate_spec  # noqa: E402


def _valid_spec():
    return {
        "doc_id": "t",
        "formats": ["pdf"],
        "is_academic": False,
        "identity": {"title": "Judul Uji"},
        "style": {"page_size": "A4", "font": "Times New Roman"},
        "sections": [
            {
                "id": "s0",
                "kind": "chapter",
                "number": "I",
                "title": "Pendahuluan",
                "blocks": [
                    {"type": "paragraph", "text": "Isi paragraf yang cukup panjang untuk uji."}
                ],
            }
        ],
        "references": [],
        "figures": [],
    }


def _write(tmp_path, obj_or_text):
    p = tmp_path / "spec.json"
    if isinstance(obj_or_text, str):
        p.write_text(obj_or_text, encoding="utf-8")
    else:
        p.write_text(json.dumps(obj_or_text), encoding="utf-8")
    return str(p)


def test_valid_spec_exit_0(tmp_path):
    assert validate_spec.main([_write(tmp_path, _valid_spec())]) == 0


def test_missing_title_exit_1(tmp_path):
    data = _valid_spec()
    data["identity"]["title"] = "   "
    assert validate_spec.main([_write(tmp_path, data)]) == 1


def test_bad_json_exit_2(tmp_path):
    assert validate_spec.main([_write(tmp_path, "{not valid json")]) == 2


def test_toc_without_chapter_exit_1(tmp_path):
    data = _valid_spec()
    data["sections"] = [
        {"id": "toc", "kind": "toc", "title": "Daftar Isi", "blocks": []}
    ]
    assert validate_spec.main([_write(tmp_path, data)]) == 1


def test_academic_missing_references_exit_1(tmp_path):
    data = _valid_spec()
    data["is_academic"] = True
    data["references"] = []
    assert validate_spec.main([_write(tmp_path, data)]) == 1
