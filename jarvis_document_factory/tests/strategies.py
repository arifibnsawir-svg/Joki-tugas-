"""Hypothesis strategies and builders shared across property tests."""
from __future__ import annotations

import string

from hypothesis import strategies as st

# Clean text: never contains an em-dash, en-dash, curly quote, or emoji.
CLEAN_ALPHABET = string.ascii_letters + string.digits + " .,:;'\"()-/"

# A grab bag of forbidden characters for the humanizer / gate cleanliness tests.
DIRTY_CHARS = [
    "\u2014",      # em-dash
    "\u2013",      # en-dash
    "\u201c", "\u201d",  # curly double quotes
    "\u2018", "\u2019",  # curly single quotes
    "\U0001F600",  # grinning face emoji
    "\U0001F4A1",  # light bulb emoji
    "\u2600",      # sun (symbol range treated as emoji)
    "\u2764",      # heavy black heart
]


def _nonempty(s: str) -> str:
    s = (s or "").strip()
    return s or "x"


clean_text = st.text(alphabet=CLEAN_ALPHABET, min_size=1, max_size=60).map(_nonempty)

# Realistic titles/headings: alphabetic words, reliably extractable from a PDF.
# (pypdf text extraction is unreliable for 1-2 char or punctuation-only strings;
# such degenerate titles are not what the factory targets.)
phrase = st.lists(
    st.text(alphabet=string.ascii_uppercase + string.ascii_lowercase, min_size=3, max_size=9),
    min_size=1, max_size=4,
).map(lambda ws: " ".join(ws))

dirty_text = st.lists(
    st.one_of(
        st.sampled_from(DIRTY_CHARS),
        st.text(alphabet=CLEAN_ALPHABET, min_size=0, max_size=6),
    ),
    min_size=1,
    max_size=12,
).map("".join)


# ---- block strategies (no figure blocks; images tested separately) ----
def _heading_block():
    return st.fixed_dictionaries({
        "type": st.just("heading"),
        "level": st.sampled_from([2, 3]),
        "text": clean_text,
    })


def _para_block(kind):
    return st.fixed_dictionaries({"type": st.just(kind), "text": clean_text})


def _list_block():
    return st.fixed_dictionaries({
        "type": st.just("list"),
        "ordered": st.booleans(),
        "items": st.lists(clean_text, min_size=1, max_size=5),
    })


def _table_block():
    return st.integers(min_value=1, max_value=4).flatmap(
        lambda ncol: st.fixed_dictionaries({
            "type": st.just("table"),
            "caption": clean_text,
            "header": st.lists(clean_text, min_size=ncol, max_size=ncol),
            "rows": st.lists(
                st.lists(clean_text, min_size=ncol, max_size=ncol),
                min_size=1, max_size=4,
            ),
        })
    )


def block_strategy():
    return st.one_of(
        _heading_block(),
        _para_block("paragraph"),
        _para_block("lead"),
        _para_block("callout"),
        _list_block(),
        _table_block(),
    )


def _reference(i):
    return st.fixed_dictionaries({
        "id": st.just("ref%d" % i),
        "apa": clean_text,
        "url": st.one_of(st.just(""), st.just("https://example.ac.id/x")),
        "verified": st.booleans(),
    })


@st.composite
def valid_spec_dicts(draw, require_academic=None):
    """Generate a SPEC dict that passes validate() (no figure blocks)."""
    formats = draw(st.lists(st.sampled_from(["pdf", "docx", "pptx"]),
                            min_size=1, max_size=3, unique=True))
    is_academic = draw(st.booleans()) if require_academic is None else require_academic

    nsec = draw(st.integers(min_value=1, max_value=4))
    sections = []
    for i in range(nsec):
        blocks = draw(st.lists(block_strategy(), min_size=0, max_size=4))
        sections.append({
            "id": "s%d" % i,
            "kind": draw(st.sampled_from(["frontmatter", "chapter", "appendix", "references"])),
            "number": "",
            "title": draw(clean_text),
            "blocks": blocks,
        })

    # style: sometimes provide overrides, sometimes leave to defaults
    style = {}
    if draw(st.booleans()):
        style["page_size"] = "A4"
    if draw(st.booleans()):
        style["font"] = draw(st.sampled_from(["Times New Roman", "Georgia"]))
    if not is_academic:
        # non-academic needs explicit page_size/font when pdf/docx requested
        if "pdf" in formats or "docx" in formats:
            style["page_size"] = "A4"
            style["font"] = "Times New Roman"

    references = []
    if is_academic:
        n = draw(st.integers(min_value=1, max_value=4))
        for i in range(n):
            references.append(draw(_reference(i)))

    return {
        "spec_version": "1.0",
        "doc_id": draw(clean_text),
        "formats": formats,
        "doc_type": draw(st.sampled_from(["academic", "report", "deck", "module"])),
        "is_academic": is_academic,
        "identity": {"title": draw(clean_text), "authors": []},
        "style": style,
        "sections": sections,
        "references": references,
        "figures": [],
    }
