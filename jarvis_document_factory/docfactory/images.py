"""Image resolver and anti-hallucination guard.

Mirrors the os.path.exists guard in the proven renderers, promoted to a hard
pre-render error. There is no path by which an invented image reaches output:
a figure is embedded only if its file exists on disk.
"""
from __future__ import annotations

import os

from .errors import MissingImageError


def resolve_figures(spec):
    """Set verified_path True iff the figure path exists on disk (Requirement 8.1).

    Mutates and returns the SPEC.
    """
    for fig in spec.figures:
        fig.verified_path = bool(fig.path) and os.path.exists(fig.path)
    return spec


def referenced_figure_refs(spec) -> set[str]:
    """Refs actually used by a figure block or by identity.logo."""
    refs: set[str] = set()
    for section in spec.sections:
        for block in section.blocks:
            if block.get("type") == "figure" and block.get("ref"):
                refs.add(block["ref"])
    logo = getattr(spec.identity, "logo", "")
    if logo and spec.figure_by_ref(logo) is not None:
        refs.add(logo)
    return refs


def assert_referenced_images_exist(spec):
    """Raise MissingImageError for any referenced figure whose path is missing.

    Runs before any renderer (Requirement 8.2). resolve_figures should be called
    first so verified_path is current.
    """
    for ref in sorted(referenced_figure_refs(spec)):
        fig = spec.figure_by_ref(ref)
        if fig is None:
            raise MissingImageError(ref, "<no figure registry entry>")
        if not fig.verified_path:
            raise MissingImageError(ref, fig.path)
    return spec


def verified_figure_refs(spec) -> set[str]:
    """Refs whose paths the resolver verified. Renderers embed only these."""
    return {f.ref for f in spec.figures if f.verified_path}
