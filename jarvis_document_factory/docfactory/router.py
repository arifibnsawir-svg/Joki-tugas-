"""Router: lightweight route selection. Never blocks input, never declares DONE.

The Router is a separate component from the Output_Gate. It picks the generation
route (which formats, single-shot vs delegated) and decides whether delegation is
worth the cost. It leaves the finished decision entirely to the gate.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .renderers.pptx import resolve_pptx_style

# A job at or above this many sections is considered large enough to be worth
# delegating to workers (Requirement 10.1, 10.3, 10.4).
DELEGATION_SECTION_THRESHOLD = 12


@dataclass(frozen=True)
class Route:
    formats: list[str]
    pptx_style: str            # "house" | "minimal"
    delegate: bool             # whether delegation is worth the cost
    reason: str = ""
    notes: list[str] = field(default_factory=list)


def select_route(spec, *, request: str = "") -> Route:
    """Select a route for a document request without ever blocking the input.

    The Router never rejects a request here; validation (a separate step) is what
    raises on a bad SPEC. The Router only chooses how to run the job.
    """
    formats = list(spec.formats)
    pptx_style = resolve_pptx_style(request)
    n_sections = len(spec.sections)
    delegate = n_sections >= DELEGATION_SECTION_THRESHOLD
    reason = ("large job (%d sections >= %d): delegation worthwhile"
              % (n_sections, DELEGATION_SECTION_THRESHOLD)) if delegate else \
             ("small job (%d sections < %d): run directly"
              % (n_sections, DELEGATION_SECTION_THRESHOLD))
    return Route(formats=formats, pptx_style=pptx_style, delegate=delegate, reason=reason)
