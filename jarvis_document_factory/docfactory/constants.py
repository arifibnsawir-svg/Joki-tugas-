"""Shared constants and academic defaults (single source of truth)."""
from __future__ import annotations

SUPPORTED_FORMATS = ("pdf", "docx", "pptx")

DOC_TYPES = ("academic", "report", "deck", "module")

SECTION_KINDS = ("frontmatter", "toc", "chapter", "references", "appendix")

BLOCK_TYPES = ("heading", "paragraph", "lead", "list", "table", "callout", "figure")

PPTX_LAYOUTS = ("cover", "section", "bullets", "two_col", "closing")

# Academic formatting defaults (Requirement 11.1). Margins are top/bottom/left/right
# in centimetres, matching the proven build_docx.py (top 3, bottom 3, left 4, right 3).
ACADEMIC_STYLE_DEFAULTS = {
    "page_size": "A4",
    "font": "Times New Roman",
    "font_size_pt": 12,
    "line_spacing": 1.5,
    "body_align": "justify",
    "page_numbers": "arabic",
    "margins_cm": {"top": 3.0, "bottom": 3.0, "left": 4.0, "right": 3.0},
    "accent_color": "#1F4E79",
}
