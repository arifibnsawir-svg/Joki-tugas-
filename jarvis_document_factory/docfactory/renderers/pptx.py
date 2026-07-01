"""PPTX_Renderer: SPEC to a designed 16:9 deck by REUSING the house render_deck.py.

This renderer does not draw slides itself. It maps the SPEC sections in order to
the slide-spec dict that render_deck.py consumes, then calls render_deck. The
default is the house designed deck; the minimal style is applied only when the
request explicitly instructs minimal or plain formatting (Requirements 3.5, 3.6).
Only verified images are ever placed on a slide.
"""
from __future__ import annotations

import importlib.util
import os

from ..images import verified_figure_refs
from ..spec import RenderResult

DECK_LAYOUTS = ("cover", "section", "bullets", "two_col", "closing", "image")
_MAX_BULLETS = 6


def _load_render_deck():
    """Locate and import the house render_deck.py without reimplementing it."""
    candidates = [
        os.environ.get("HERMES_RENDER_DECK"),
        os.path.expanduser("~/.hermes/scripts/render_deck.py"),
        "/projects/sandbox/jarvis/renderer/render_deck.py",
    ]
    for path in candidates:
        if path and os.path.exists(path):
            spec = importlib.util.spec_from_file_location("render_deck_house", path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module.render_deck
    raise FileNotFoundError(
        "render_deck.py not found. Set HERMES_RENDER_DECK or install it at "
        "~/.hermes/scripts/render_deck.py"
    )


def resolve_pptx_style(request: str = "") -> str:
    """Return 'minimal' iff the request explicitly instructs minimal/plain formatting.

    A bare 'default slides' or 'plain default' request keeps the house designed
    deck (Requirement 3.5); an explicit minimal/plain formatting instruction
    switches to minimal (Requirement 3.6).
    """
    r = (request or "").lower()
    if "minimal" in r:
        return "minimal"
    if "plain" in r and "default" not in r:
        return "minimal"
    return "house"


def _chunks(items, n):
    for i in range(0, len(items), n):
        yield items[i:i + n]


def _bullets_from_section(section) -> list[str]:
    bullets: list[str] = []
    for b in section.blocks:
        t = b.get("type")
        if t == "heading":
            txt = b.get("text", "").strip()
            if txt:
                bullets.append(txt)
        elif t in ("paragraph", "lead", "callout"):
            txt = b.get("text", "").strip()
            if txt:
                bullets.append(txt if len(txt) <= 160 else txt[:157] + "...")
        elif t == "list":
            bullets.extend(str(x) for x in b.get("items", []))
    return bullets


def _section_slides(spec, section, verified_refs) -> list[dict]:
    slides: list[dict] = []
    hint = (section.pptx or {}).get("layout")

    if section.kind == "references":
        bullets = [r.apa for r in spec.references]
    else:
        bullets = _bullets_from_section(section)

    if hint == "cover":
        slides.append({"layout": "cover", "title": section.title,
                       "subtitle": bullets[0] if bullets else ""})
    elif hint == "closing":
        slides.append({"layout": "closing", "title": section.title,
                       "subtitle": bullets[0] if bullets else ""})
    elif hint == "section":
        slides.append({"layout": "section", "number": section.number or "",
                       "title": section.title, "subtitle": ""})
    elif hint == "two_col" and bullets:
        mid = (len(bullets) + 1) // 2
        slides.append({"layout": "two_col", "title": section.title,
                       "left": {"bullets": bullets[:mid]},
                       "right": {"bullets": bullets[mid:]}})
    elif hint == "bullets":
        for chunk in _chunks(bullets, _MAX_BULLETS) or [[]]:
            slides.append({"layout": "bullets", "title": section.title, "bullets": chunk})
    else:
        # default mapping from section kind
        if section.kind == "chapter":
            slides.append({"layout": "section", "number": section.number or "",
                           "title": section.title, "subtitle": ""})
        if bullets:
            for chunk in _chunks(bullets, _MAX_BULLETS):
                slides.append({"layout": "bullets", "title": section.title, "bullets": chunk})
        elif section.kind != "chapter":
            # a titled section with no content still deserves a slide
            slides.append({"layout": "bullets", "title": section.title, "bullets": []})

    # image slides for verified figures in this section
    for b in section.blocks:
        if b.get("type") == "figure":
            ref = b.get("ref", "")
            fig = spec.figure_by_ref(ref)
            if fig is not None and ref in verified_refs:
                slides.append({"layout": "image",
                               "title": fig.caption or section.title,
                               "image_path": fig.path})
    return slides


def build_deck_spec(spec, style_mode: str = "house") -> dict:
    idn = spec.identity
    verified_refs = verified_figure_refs(spec)

    meta = [a.get("name", "") for a in idn.authors][:3]
    if idn.year:
        meta.append(idn.year)
    if idn.institution:
        meta.append(idn.institution)

    slides: list[dict] = [{
        "layout": "cover",
        "eyebrow": idn.course or "",
        "title": idn.title,
        "subtitle": idn.subtitle or "",
        "meta": meta,
    }]
    for section in spec.sections:
        if section.kind == "toc":
            continue
        slides.extend(_section_slides(spec, section, verified_refs))
    slides.append({"layout": "closing", "title": "Terima Kasih",
                   "subtitle": idn.institution or ""})

    deck = {
        "preset": "academic",
        "footer": idn.institution or idn.title,
        "slides": slides,
    }
    if style_mode == "minimal":
        # Minimal style still goes through the house renderer; the accents are
        # neutralized so the deck reads plain rather than designed.
        deck["theme"] = {"accent": "888888", "accent2": "666666", "head_font": "Calibri"}
    return deck


def render(spec, out_path: str, *, pdf_path: str | None = None, request: str = "") -> RenderResult:
    render_deck = _load_render_deck()
    style_mode = resolve_pptx_style(request)
    deck_spec = build_deck_spec(spec, style_mode)
    out_dir = os.path.dirname(os.path.abspath(out_path))
    os.makedirs(out_dir, exist_ok=True)
    facts = render_deck(deck_spec, out_path)
    return RenderResult(
        fmt="pptx",
        out_path=out_path,
        page_count=int(facts.get("slide_count", 0)),
        warnings=[],
    )
