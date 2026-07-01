"""Standalone CLI tests for validate_spec.py (the pre-render SPEC validator).

Uses only the stdlib (unittest + tempfile) so it needs NO extra deps (no pytest)
and can be run directly in the Hermes production venv on Acer:

    python tests/test_validate_cli.py                 # standalone
    python -m pytest tests/test_validate_cli.py -q    # also works if pytest present

Proves the three exit-code contracts an author relies on: 0 = render-ready,
1 = fixable SPEC problem, 2 = file/JSON could not be loaded.
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest

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


class ValidateCliTest(unittest.TestCase):
    def _write(self, obj_or_text):
        fd, path = tempfile.mkstemp(suffix=".json")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(
                obj_or_text if isinstance(obj_or_text, str) else json.dumps(obj_or_text)
            )
        self.addCleanup(lambda: os.path.exists(path) and os.remove(path))
        return path

    def test_valid_spec_exit_0(self):
        self.assertEqual(validate_spec.main([self._write(_valid_spec())]), 0)

    def test_missing_title_exit_1(self):
        data = _valid_spec()
        data["identity"]["title"] = "   "
        self.assertEqual(validate_spec.main([self._write(data)]), 1)

    def test_bad_json_exit_2(self):
        self.assertEqual(validate_spec.main([self._write("{not valid json")]), 2)

    def test_toc_without_chapter_exit_1(self):
        data = _valid_spec()
        data["sections"] = [
            {"id": "toc", "kind": "toc", "title": "Daftar Isi", "blocks": []}
        ]
        self.assertEqual(validate_spec.main([self._write(data)]), 1)

    def test_academic_missing_references_exit_1(self):
        data = _valid_spec()
        data["is_academic"] = True
        data["references"] = []
        self.assertEqual(validate_spec.main([self._write(data)]), 1)


if __name__ == "__main__":
    unittest.main()
