"""Jarvis Document Factory (docfactory).

SPEC-first document generation: the language model emits a structured SPEC,
deterministic renderers turn that SPEC into PPTX, DOCX, and PDF files, and a
deterministic gate decides PASS or FAIL. Two always-on layers (humanizer and
cite-or-abstain) apply to every artifact.

This package generalizes the proven scripts in this repository
(gen_pdf.py, build_docx.py, qa.py, konten.py) and reuses the house
render_deck.py for PPTX. It does not reimplement any of them.
"""
from __future__ import annotations

from .constants import SUPPORTED_FORMATS

__version__ = "1.0.0"

__all__ = ["SUPPORTED_FORMATS", "__version__"]
