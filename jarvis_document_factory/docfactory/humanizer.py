"""Humanizer layer: deterministic char-level cleaner + shared clean predicate.

The rich, meaning-level rewrite ("sound like a human, remove AI tells") is done
UPSTREAM by the existing Jarvis humanizer skill
(~/.hermes/skills/humanizer/SKILL.md). This module does NOT reimplement that
skill. It is the deterministic guarantee layer: a char-level cleaner that makes
any text Humanizer_Clean, plus the is_humanizer_clean predicate the gate reuses
so the layer and the gate agree on exactly one definition of "clean".

Humanizer_Clean means zero em-dashes, zero en-dashes, zero curly or smart
quotes, and zero emoji (Requirements 6.2, 6.3).
"""
from __future__ import annotations

import re

EM_DASH = "\u2014"
EN_DASH = "\u2013"
CURLY_DOUBLE = ("\u201c", "\u201d")  # left/right double quotation marks
CURLY_SINGLE = ("\u2018", "\u2019")  # left/right single quotation marks / apostrophe

_MULTISPACE = re.compile(r"[ \t]{2,}")


def _is_emoji(ch: str) -> bool:
    """Emoji / pictographic detection, identical to the proven qa.py rule.

    Kept byte-for-byte consistent with the gate so the layer and the gate never
    disagree on a character.
    """
    o = ord(ch)
    return o >= 0x1F000 or (0x2190 <= o <= 0x2BFF) or (0x2600 <= o <= 0x27BF)


def is_humanizer_clean(text: str) -> bool:
    """True iff text has zero em-dash, en-dash, curly/smart quote, and emoji."""
    if text is None:
        return True
    for ch in text:
        if ch == EM_DASH or ch == EN_DASH:
            return False
        if ch in CURLY_DOUBLE or ch in CURLY_SINGLE:
            return False
        if _is_emoji(ch):
            return False
    return True


def humanize(text: str) -> str:
    """Return a Humanizer_Clean version of text, preserving meaning and coverage.

    Replacements are conservative and readable:
      em-dash  -> " - "   (a spaced hyphen keeps clause separation legible)
      en-dash  -> "-"     (ranges like 10-20 stay intact)
      curly "  -> "       (straight double quote)
      curly '  -> '       (straight apostrophe / single quote)
      emoji    -> removed
    Redundant whitespace introduced by the replacements is collapsed, without
    touching line breaks.
    """
    if not text:
        return text or ""
    out_chars: list[str] = []
    for ch in text:
        if ch == EM_DASH:
            out_chars.append(" - ")
        elif ch == EN_DASH:
            out_chars.append("-")
        elif ch in CURLY_DOUBLE:
            out_chars.append('"')
        elif ch in CURLY_SINGLE:
            out_chars.append("'")
        elif _is_emoji(ch):
            continue  # drop emoji
        else:
            out_chars.append(ch)
    result = "".join(out_chars)
    # Collapse runs of spaces/tabs (but keep newlines) that the em-dash spacing
    # may have introduced.
    result = _MULTISPACE.sub(" ", result)
    return result


def _clean_list_of_str(items):
    return [humanize(x) if isinstance(x, str) else x for x in items]


def humanize_block(block: dict) -> dict:
    """Humanize every prose field of one content block in place."""
    t = block.get("type")
    if t in ("paragraph", "lead", "callout"):
        if isinstance(block.get("text"), str):
            block["text"] = humanize(block["text"])
    elif t == "heading":
        if isinstance(block.get("text"), str):
            block["text"] = humanize(block["text"])
    elif t == "list":
        block["items"] = _clean_list_of_str(block.get("items", []))
    elif t == "table":
        if isinstance(block.get("caption"), str):
            block["caption"] = humanize(block["caption"])
        block["header"] = _clean_list_of_str(block.get("header", []))
        block["rows"] = [_clean_list_of_str(row) for row in block.get("rows", [])]
    return block


def humanize_spec(spec):
    """Walk every prose field in the SPEC and make it Humanizer_Clean.

    Runs on the SPEC before validation and rendering, so the SPEC that reaches
    the renderers already carries clean text. Mutates and returns the SPEC.
    """
    idn = spec.identity
    for attr in ("title", "subtitle", "course", "lecturer", "program",
                 "faculty", "institution", "year"):
        val = getattr(idn, attr)
        if isinstance(val, str):
            setattr(idn, attr, humanize(val))
    for author in idn.authors:
        if isinstance(author.get("name"), str):
            author["name"] = humanize(author["name"])

    for section in spec.sections:
        section.title = humanize(section.title)
        for block in section.blocks:
            humanize_block(block)

    for ref in spec.references:
        ref.apa = humanize(ref.apa)

    for fig in spec.figures:
        if isinstance(fig.caption, str):
            fig.caption = humanize(fig.caption)

    return spec
