"""Property test for the humanizer layer cleanliness."""
from __future__ import annotations

from hypothesis import given, settings

from docfactory.humanizer import humanize, is_humanizer_clean
from strategies import dirty_text


# Feature: jarvis-document-factory, Property 21: Humanizer output is clean
@settings(max_examples=100)
@given(dirty_text)
def test_property_21_humanizer_output_is_clean(text):
    cleaned = humanize(text)
    assert is_humanizer_clean(cleaned)
    # no forbidden character survives
    for ch in ("\u2014", "\u2013", "\u201c", "\u201d", "\u2018", "\u2019"):
        assert ch not in cleaned


def test_humanizer_preserves_plain_text():
    s = "Rogers (1961) menjelaskan hubungan membantu yang tulus."
    assert humanize(s) == s
    assert is_humanizer_clean(s)


def test_is_humanizer_clean_detects_each_class():
    assert not is_humanizer_clean("a\u2014b")
    assert not is_humanizer_clean("a\u2013b")
    assert not is_humanizer_clean("a\u201cb\u201d")
    assert not is_humanizer_clean("it\u2019s")
    assert not is_humanizer_clean("nice \U0001F600")
    assert is_humanizer_clean("straight 'quotes' and \"double\" are fine")
