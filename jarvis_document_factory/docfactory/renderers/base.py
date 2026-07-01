"""Shared renderer contract and reproducibility helpers.

Every renderer implements render(spec, out_path, *, pdf_path=None) -> RenderResult,
reads content only from the SPEC and verified referenced paths, embeds only
verified images, and writes no wall-clock timestamps, random IDs, or
locale-dependent values. Metadata dates are pinned to a fixed value derived
from doc_id so the same SPEC renders byte-equivalent output (Requirements 2.6,
12.2).
"""
from __future__ import annotations

import base64
import datetime
import hashlib
import html as _html
import os
import re

# A fixed reference instant. The pinned date is offset from this by a stable
# amount derived from doc_id, so output is reproducible but still per-document.
_EPOCH_BASE = 1_600_000_000  # 2020-09-13T12:26:40Z, an arbitrary fixed anchor


def stable_epoch(doc_id: str) -> int:
    """A deterministic POSIX timestamp derived from doc_id (never wall clock)."""
    h = hashlib.md5((doc_id or "doc").encode("utf-8")).hexdigest()
    offset = int(h[:6], 16)  # 0 .. ~16.7M seconds
    return _EPOCH_BASE + offset


def pinned_datetime(doc_id: str) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(stable_epoch(doc_id), tz=datetime.timezone.utc)


def esc(text) -> str:
    return _html.escape(str(text))


def slug(text: str) -> str:
    s = "".join(ch.lower() if ch.isalnum() else "-" for ch in str(text))
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")[:50] or "x"


def image_data_uri(path: str) -> str:
    ext = os.path.splitext(path)[1].lstrip(".").lower()
    mime = "image/png" if ext == "png" else "image/jpeg"
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode())


def resolve_logo_path(spec) -> str:
    """Return an existing file path for identity.logo, or empty string.

    Accepts either a figure ref (resolved through the verified registry) or a
    raw path. Never returns a path that does not exist (anti-hallucination).
    """
    logo = getattr(spec.identity, "logo", "") or ""
    if not logo:
        return ""
    fig = spec.figure_by_ref(logo)
    if fig is not None:
        return fig.path if fig.verified_path else ""
    return logo if os.path.exists(logo) else ""


_ROMAN = re.compile(r"^[IVXLCDM]+$")
