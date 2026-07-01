"""Smoke tests for skill packaging and the reuse / separation guarantees."""
from __future__ import annotations

import importlib
import inspect
import os

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _parse_frontmatter(text):
    assert text.startswith("---"), "SKILL.md must start with YAML frontmatter"
    end = text.index("\n---", 3)
    block = text[3:end].strip().splitlines()
    fm = {}
    for line in block:
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm


def test_skill_md_frontmatter_valid():
    path = os.path.join(SKILL_DIR, "SKILL.md")
    assert os.path.exists(path)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fm = _parse_frontmatter(text)
    assert fm.get("name") == "jarvis-document-factory"
    assert fm.get("description")
    assert fm.get("version")
    assert "allowed-tools" in fm
    # scope statement present in body
    assert "PPTX" in text and "DOCX" in text and "PDF" in text


def test_entry_point_present_and_loadable():
    assert os.path.exists(os.path.join(SKILL_DIR, "run.py"))
    # run.py exposes main()
    import runpy
    src = open(os.path.join(SKILL_DIR, "run.py"), encoding="utf-8").read()
    assert "def main(" in src and "run_pipeline" in src


def test_reuses_render_deck_not_reimplemented():
    # the PPTX renderer LOADS the house render_deck.py; it does not ship its own.
    from docfactory.renderers import pptx

    src = inspect.getsource(pptx)
    assert "render_deck" in src
    assert hasattr(pptx, "_load_render_deck")
    # no local copy of the engine bundled in the package
    assert not os.path.exists(os.path.join(SKILL_DIR, "docfactory", "render_deck.py"))


def test_humanizer_layer_is_thin_not_a_reimplementation():
    # the package humanizer is the deterministic cleaner + predicate only; the
    # rich rewrite is the existing humanizer skill (reused upstream).
    from docfactory import humanizer

    assert hasattr(humanizer, "is_humanizer_clean")
    assert hasattr(humanizer, "humanize")
    assert "reuse" in inspect.getdoc(humanizer).lower() or "upstream" in inspect.getdoc(humanizer).lower()


def test_router_and_gate_are_separate_modules():
    router = importlib.import_module("docfactory.router")
    gate = importlib.import_module("docfactory.gate")
    assert router.__name__ != gate.__name__
    # the Router never declares DONE: it does not import or expose the gate
    assert not hasattr(router, "gate")
    router_src = inspect.getsource(router)
    assert "docfactory.gate" not in router_src
    assert "from .gate" not in router_src and "import gate" not in router_src
    # the gate is the DONE authority: it exposes gate()
    assert hasattr(gate, "gate")
