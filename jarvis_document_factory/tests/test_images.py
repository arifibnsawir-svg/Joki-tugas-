"""Property tests for the image resolver and the missing-image guard."""
from __future__ import annotations

import os
import tempfile

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from docfactory.errors import MissingImageError
from docfactory.images import (
    assert_referenced_images_exist,
    resolve_figures,
    verified_figure_refs,
)
from docfactory.spec import parse_spec


def _spec_with_figures(figures, figure_blocks=True):
    sections = [{"id": "s0", "kind": "appendix", "title": "Lampiran", "blocks": []}]
    if figure_blocks:
        sections[0]["blocks"] = [{"type": "figure", "ref": f["ref"]} for f in figures]
    return parse_spec({
        "doc_id": "img", "formats": ["pdf"], "is_academic": False,
        "identity": {"title": "T"}, "style": {"page_size": "A4", "font": "Times New Roman"},
        "sections": sections, "references": [], "figures": figures,
    })


# Feature: jarvis-document-factory, Property 25: Image resolver marks verified iff the path exists
@settings(max_examples=100, deadline=None)
@given(st.lists(st.booleans(), min_size=0, max_size=6))
def test_property_25_resolver_verified_iff_exists(exists_flags):
    with tempfile.TemporaryDirectory() as d:
        figures = []
        for i, exists in enumerate(exists_flags):
            path = os.path.join(d, "f%d.png" % i)
            if exists:
                with open(path, "wb") as fh:
                    fh.write(b"\x89PNG\r\n")
            figures.append({"ref": "g%d" % i, "path": path, "caption": "", "verified_path": False})
        spec = _spec_with_figures(figures, figure_blocks=False)
        resolve_figures(spec)
        for fig, exists in zip(spec.figures, exists_flags):
            assert fig.verified_path == exists
        verified = verified_figure_refs(spec)
        assert verified == {"g%d" % i for i, e in enumerate(exists_flags) if e}


# Feature: jarvis-document-factory, Property 26: Missing image fails before rendering
@settings(max_examples=100, deadline=None)
@given(st.integers(min_value=0, max_value=5), st.integers(min_value=0, max_value=5))
def test_property_26_missing_image_fails_before_render(n_ok, n_missing):
    with tempfile.TemporaryDirectory() as d:
        figures = []
        for i in range(n_ok):
            path = os.path.join(d, "ok%d.png" % i)
            with open(path, "wb") as fh:
                fh.write(b"\x89PNG\r\n")
            figures.append({"ref": "ok%d" % i, "path": path, "caption": "", "verified_path": False})
        for i in range(n_missing):
            figures.append({"ref": "miss%d" % i, "path": os.path.join(d, "nope%d.png" % i),
                            "caption": "", "verified_path": False})
        spec = _spec_with_figures(figures, figure_blocks=True)
        resolve_figures(spec)
        if n_missing > 0:
            with pytest.raises(MissingImageError) as ei:
                assert_referenced_images_exist(spec)
            assert ei.value.ref.startswith("miss")
        else:
            assert_referenced_images_exist(spec) is spec
