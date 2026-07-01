"""Pytest bootstrap: make the skill folder importable as `docfactory`.

The skill deploys to a hyphenated folder (jarvis-document-factory), so tests
import the underscore-safe inner package `docfactory` by putting the skill
folder (the parent of this tests dir) on sys.path.
"""
import os
import sys

_SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SKILL_DIR not in sys.path:
    sys.path.insert(0, _SKILL_DIR)
