"""PDF_Renderer: SPEC to PDF via WeasyPrint (generalizes gen_pdf.py).

One HTML document with embedded CSS, rendered in a single WeasyPrint pass so the
table-of-contents target-counter resolves accurately. No counter-reset, no
counter-set. hyphens:none so line breaks match the DOCX. A4 academic defaults.
Body text black; colour only in table header and zebra rows. Verified images
inline as base64 data URIs.
"""
from __future__ import annotations

import os

from ..images import verified_figure_refs
from ..readers import count_words
from ..spec import RenderResult, resolve_style
from .base import esc, image_data_uri, resolve_logo_path, slug, stable_epoch


def _page_number_content(page_numbers: str) -> str:
    if page_numbers == "none":
        return "normal"
    if page_numbers == "roman":
        return "counter(page, lower-roman)"
    return "counter(page)"


def _css(style: dict) -> str:
    m = style["margins_cm"]
    font = style["font"]
    size = style["font_size_pt"]
    lh = style["line_spacing"]
    align = style["body_align"]
    page_content = _page_number_content(style["page_numbers"])
    # @page margin order is top right bottom left.
    margin = "%gcm %gcm %gcm %gcm" % (m["top"], m["right"], m["bottom"], m["left"])
    return r"""
@page {
  size: %(page_size)s;
  margin: %(margin)s;
  @bottom-center { content: %(page_content)s; font-family:'%(font)s','Liberation Serif',serif; font-size:11pt; color:#000; }
}
@page :first { margin: 2.2cm 2.5cm; @bottom-center { content: normal; } }

html { font-family:'%(font)s','Liberation Serif','Times New Roman',serif; }
body { font-size:%(size)gpt; line-height:%(lh)g; text-align:%(align)s; color:#000; hyphens:none; }
p { margin:0 0 6pt 0; orphans:2; widows:2; text-indent:0; }
p.lead { margin:0 0 8pt 0; }

.titlepage { page-break-after:always; box-sizing:border-box; text-align:center; color:#000; }
.titlepage .judul { font-size:18pt; font-weight:bold; margin-top:0.6cm; line-height:1.4; text-transform:uppercase; }
.titlepage .subjudul { font-size:12.5pt; font-style:italic; margin:14pt 0.6cm 0 0.6cm; line-height:1.5; }
.titlepage .label { font-size:12pt; margin-top:16pt; line-height:1.5; }
.titlepage .logo-wrap { margin:0.9cm 0; }
.titlepage .logo-wrap img { width:4.0cm; height:auto; }
.titlepage .penyusun-head { font-size:12pt; margin-top:6pt; font-weight:bold; }
.titlepage .mhs { margin:7pt 0; line-height:1.35; }
.titlepage .mhs .nm { font-size:12.5pt; font-weight:bold; }
.titlepage .mhs .nim { font-size:11.5pt; }
.titlepage .footer { font-size:13pt; font-weight:bold; margin-top:0.9cm; line-height:1.55; text-transform:uppercase; }

h1.major { font-size:14pt; font-weight:bold; text-align:center; margin:0 0 16pt 0; padding-bottom:6pt;
  text-transform:uppercase; break-after:avoid; border-bottom:0.75pt solid #000; }
.babhead { text-align:center; margin:0 0 18pt 0; padding-bottom:8pt; break-after:avoid; border-bottom:0.75pt solid #000; }
.babhead .babno { font-size:14pt; font-weight:bold; letter-spacing:1pt; }
.babhead .babtitle { font-size:14pt; font-weight:bold; margin-top:4pt; }
h2 { font-size:%(size)gpt; font-weight:bold; margin:12pt 0 6pt 0; break-after:avoid; }
h3 { font-size:%(size)gpt; font-weight:bold; font-style:italic; margin:10pt 0 4pt 0; break-after:avoid; }
.sec { break-before:page; }

ul.toc { list-style:none; padding:0; margin:0; line-height:1.22; }
ul.toc li { margin:0 0 2pt 0; line-height:1.22; }
ul.toc li.lvl2 { margin-left:0.9cm; }
ul.toc a { color:#000; text-decoration:none; display:block; }
ul.toc a::after { content: leader('.') target-counter(attr(href url), page); }
ul.toc li.lvl1 > a { font-weight:bold; }
#toc-section h1.major { margin-bottom:10pt; }

ol.num, ul.bul { margin:0 0 8pt 0; padding-left:1.2cm; }
ol.num li, ul.bul li { margin:0 0 4pt 0; }

.callout { background:#F7F7F7; border-left:3pt solid #CCCCCC; padding:7pt 10pt; margin:4pt 0 10pt 0;
  break-inside:avoid; text-align:justify; }

table.t { width:100%%; border-collapse:collapse; margin:6pt 0 12pt 0; font-size:11pt; break-inside:avoid; }
table.t caption { caption-side:top; font-style:italic; font-size:11pt; text-align:left; margin-bottom:5pt; }
table.t th { background:#ECECEC; border:1px solid #CCCCCC; padding:5pt 7pt; text-align:left; font-weight:bold; }
table.t td { border:1px solid #CCCCCC; padding:5pt 7pt; vertical-align:top; }
table.t tr:nth-child(even) td { background:#F7F7F7; }

ul.ref { list-style:none; padding:0; margin:0; }
ul.ref li { margin:0 0 10pt 0; padding-left:1.2cm; text-indent:-1.2cm; overflow-wrap:break-word; }

.foto { text-align:center; margin:12pt 0 16pt 0; break-inside:avoid; }
.foto img { max-width:11cm; max-height:9cm; border:1px solid #CCCCCC; padding:2pt; }
.foto .cap { font-size:11pt; font-style:italic; margin-top:5pt; }
""" % {
        "page_size": style["page_size"], "margin": margin, "page_content": page_content,
        "font": font, "size": size, "lh": lh, "align": align,
    }


def _title_page(spec) -> str:
    idn = spec.identity
    p = ['<section class="titlepage">']
    p.append('<div class="judul">%s</div>' % esc(idn.title))
    if idn.subtitle:
        p.append('<div class="subjudul">%s</div>' % esc(idn.subtitle))
    if idn.course:
        p.append('<div class="label">Disusun untuk memenuhi tugas mata kuliah<br><strong>%s</strong></div>' % esc(idn.course))
    if idn.lecturer:
        p.append('<div class="label">Dosen Pengampu: %s</div>' % esc(idn.lecturer))
    logo = resolve_logo_path(spec)
    if logo:
        p.append('<div class="logo-wrap"><img src="%s" alt="logo"></div>' % image_data_uri(logo))
    if idn.authors:
        p.append('<div class="penyusun-head">Disusun oleh:</div>')
        for a in idn.authors:
            nm = esc(a.get("name", ""))
            nim = a.get("id", "")
            p.append('<div class="mhs"><div class="nm">%s</div>%s</div>' % (
                nm, ('<div class="nim">NIM. %s</div>' % esc(nim)) if nim else ""))
    footer_lines = [x for x in (idn.program, idn.faculty, idn.institution, idn.year) if x]
    if footer_lines:
        p.append('<div class="footer">%s</div>' % "<br>".join(esc(x) for x in footer_lines))
    p.append("</section>")
    return "".join(p)


def _heading_id(block) -> str:
    return block.get("id") or slug(block.get("text", ""))


def _render_blocks(spec, blocks, verified_refs) -> str:
    out = []
    for b in blocks:
        t = b.get("type")
        if t == "heading":
            level = b.get("level", 2)
            if level == 3:
                out.append("<h3>%s</h3>" % esc(b.get("text", "")))
            else:
                out.append('<h2 id="%s">%s</h2>' % (_heading_id(b), esc(b.get("text", ""))))
        elif t == "paragraph":
            out.append("<p>%s</p>" % esc(b.get("text", "")))
        elif t == "lead":
            out.append('<p class="lead">%s</p>' % esc(b.get("text", "")))
        elif t == "callout":
            out.append('<div class="callout">%s</div>' % esc(b.get("text", "")))
        elif t == "list":
            tag = "ol" if b.get("ordered") else "ul"
            cls = "num" if b.get("ordered") else "bul"
            out.append('<%s class="%s">%s</%s>' % (
                tag, cls, "".join("<li>%s</li>" % esc(x) for x in b.get("items", [])), tag))
        elif t == "table":
            out.append(_render_table(b))
        elif t == "figure":
            ref = b.get("ref", "")
            fig = spec.figure_by_ref(ref)
            if fig is not None and ref in verified_refs:
                cap = ('<div class="cap">%s</div>' % esc(fig.caption)) if fig.caption else ""
                out.append('<div class="foto"><img src="%s">%s</div>' % (image_data_uri(fig.path), cap))
    return "".join(out)


def _render_table(tb) -> str:
    h = ['<table class="t">']
    if tb.get("caption"):
        h.append("<caption>%s</caption>" % esc(tb["caption"]))
    h.append("<thead><tr>")
    h.append("".join("<th>%s</th>" % esc(c) for c in tb.get("header", [])))
    h.append("</tr></thead><tbody>")
    for row in tb.get("rows", []):
        h.append("<tr>" + "".join("<td>%s</td>" % esc(c) for c in row) + "</tr>")
    h.append("</tbody></table>")
    return "".join(h)


def _toc_html(spec) -> str:
    p = ['<ul class="toc">']
    for s in spec.sections:
        if s.kind == "toc":
            continue
        if s.kind == "chapter" and s.number:
            label = "BAB %s &nbsp;%s" % (esc(s.number), esc(s.title))
        else:
            label = esc(s.title)
        p.append('<li class="lvl1"><a href="#%s">%s</a></li>' % (esc(s.id), label))
        if s.kind == "chapter":
            for b in s.blocks:
                if b.get("type") == "heading" and b.get("level", 2) == 2:
                    p.append('<li class="lvl2"><a href="#%s">%s</a></li>' % (
                        _heading_id(b), esc(b.get("text", ""))))
    p.append("</ul>")
    return "".join(p)


def build_html(spec) -> str:
    style = resolve_style(spec)
    verified_refs = verified_figure_refs(spec)
    parts = ['<!DOCTYPE html><html lang="id"><head><meta charset="utf-8"><style>%s</style></head><body>' % _css(style)]
    parts.append(_title_page(spec))
    for s in spec.sections:
        sid = esc(s.id)
        if s.kind == "toc":
            parts.append('<section class="sec" id="toc-section"><div id="%s"></div><h1 class="major">%s</h1>%s</section>' % (
                sid, esc(s.title), _toc_html(spec)))
        elif s.kind == "chapter":
            babno = ('<div class="babno">BAB %s</div>' % esc(s.number)) if s.number else ""
            parts.append('<section class="sec" id="%s"><div class="babhead">%s<div class="babtitle">%s</div></div>%s</section>' % (
                sid, babno, esc(s.title), _render_blocks(spec, s.blocks, verified_refs)))
        elif s.kind == "references":
            refs = "".join("<li>%s</li>" % esc(r.apa) for r in spec.references)
            parts.append('<section class="sec" id="%s"><h1 class="major">%s</h1><ul class="ref">%s</ul></section>' % (
                sid, esc(s.title), refs))
        else:  # frontmatter, appendix
            parts.append('<section class="sec" id="%s"><h1 class="major">%s</h1>%s</section>' % (
                sid, esc(s.title), _render_blocks(spec, s.blocks, verified_refs)))
    parts.append("</body></html>")
    return "".join(parts)


def render(spec, out_path: str, *, pdf_path: str | None = None) -> RenderResult:
    from weasyprint import HTML

    # Reproducible PDF date: WeasyPrint honours SOURCE_DATE_EPOCH.
    prev = os.environ.get("SOURCE_DATE_EPOCH")
    os.environ["SOURCE_DATE_EPOCH"] = str(stable_epoch(spec.doc_id))
    try:
        html = build_html(spec)
        document = HTML(string=html).render()
        page_count = len(document.pages)
        out_dir = os.path.dirname(os.path.abspath(out_path))
        os.makedirs(out_dir, exist_ok=True)
        document.write_pdf(out_path)
    finally:
        if prev is None:
            os.environ.pop("SOURCE_DATE_EPOCH", None)
        else:
            os.environ["SOURCE_DATE_EPOCH"] = prev

    # Word count from the rendered file, not SPEC estimation.
    word_count = count_words("pdf", out_path)
    return RenderResult(fmt="pdf", out_path=out_path, page_count=page_count, word_count=word_count, warnings=[])
