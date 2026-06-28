# -*- coding: utf-8 -*-
"""Render Buku #2 (Naila) -> PDF via WeasyPrint, lalu tempel cover via merge.
DNA: tabel berwarna, nomor halaman POJOK KANAN BAWAH, daftar isi BERTINGKAT (bab+subbab).
Isi dirender TANPA cover => penomoran mulai 1, target-counter TOC akurat.
"""
import os, zipfile, html as _html, base64, json
from io import BytesIO
from konten import KATA_PENGANTAR, BAB, DAFTAR_PUSTAKA

SRC = "drive_buku/Joki buku pkn/MINI_BOOK_PKN_NAILA_FINAL_V10_COVER_INTEGRATED finish.docx"
OUTDIR = "Joki-tugas-/FINAL"
OUTPDF = os.path.join(OUTDIR, "Buku 2 - Naila - PKN - FINISH.pdf")
PAGEMAP = "build_naila/page_real.json"

def covers():
    z = zipfile.ZipFile(SRC)
    media = sorted([n for n in z.namelist() if n.startswith("word/media/image")])
    out = []
    for m in media:
        ext = os.path.splitext(m)[1].lstrip('.').lower()
        mime = 'image/png' if ext == 'png' else 'image/jpeg'
        out.append("data:%s;base64,%s" % (mime, base64.b64encode(z.read(m)).decode()))
    return out

def esc(t): return _html.escape(t)

CSS = r"""
@page { size: A4; margin: 3cm 3cm 2.5cm 3.5cm;
  @bottom-right { content: counter(page); font-family:'Liberation Serif',serif; font-size:11pt; } }
body { font-family:'Liberation Serif','Times New Roman',serif; font-size:12pt; line-height:1.6;
  text-align:justify; color:#000; hyphens:none; }
p { margin:0 0 12pt 0; orphans:2; widows:2; }
h1.major { font-size:16pt; font-weight:bold; text-align:center; margin:0 0 18pt 0; }
.frontsec { break-before:page; }
#kp { break-before:avoid; }
/* daftar isi bertingkat */
.toc { list-style:none; padding:0; margin:0; }
.toc li { margin:0 0 8pt 0; }
.toc li.lvl2 { margin-left:1.2cm; font-size:11pt; }
.toc a { color:#000; text-decoration:none; }
.toc a::after { content: leader('.') target-counter(attr(href url), page); }
.toc li.lvl1 a { font-weight:bold; }
/* bab */
.bab { break-before:page; }
.babhead { text-align:center; margin:0 0 20pt 0; break-after:avoid; }
.babhead .babno, .babhead .babtitle { font-size:16pt; font-weight:bold; }
.babhead .babtitle { margin-top:4pt; }
h2 { font-size:13pt; font-weight:bold; margin:14pt 0 6pt 0; break-after:avoid; break-inside:avoid; }
/* tabel berwarna (lembut, profesional) */
table.t { width:100%; border-collapse:collapse; margin:6pt 0 14pt 0; font-size:11pt; break-inside:avoid; }
table.t caption { caption-side:top; font-style:italic; font-size:10.5pt; text-align:left; margin-bottom:5pt; color:#1f3864; }
table.t th { background:#d9e2f3; border:1px solid #7f9bc7; padding:6pt 8pt; text-align:left; font-weight:bold; color:#1f3864; }
table.t td { border:1px solid #b9c4dd; padding:6pt 8pt; vertical-align:top; }
table.t tr:nth-child(even) td { background:#f2f6fc; }
/* daftar pustaka IEEE bernomor */
ol.ref { padding-left:0; margin:0; counter-reset: refnum; list-style:none; }
ol.ref li { margin:0 0 10pt 0; padding-left:1.3cm; text-indent:-1.3cm; }
ol.ref li::before { content:"["counter(refnum)"] "; counter-increment:refnum; font-weight:bold; }
"""

COVER_CSS = "@page{size:A4;margin:0;} body{margin:0;} img{width:21cm;height:29.7cm;display:block;object-fit:cover;}"

def render_table(tb):
    h = ['<table class="t"><caption>%s</caption>' % esc(tb['judul'])]
    h.append('<thead><tr>' + ''.join('<th>%s</th>' % esc(c) for c in tb['head']) + '</tr></thead><tbody>')
    for row in tb['rows']:
        h.append('<tr>' + ''.join('<td>%s</td>' % esc(c) for c in row) + '</tr>')
    h.append('</tbody></table>')
    return ''.join(h)

def content_html():
    p = ['<!DOCTYPE html><html lang=id><head><meta charset=utf-8><style>%s</style></head><body>' % CSS]
    # KATA PENGANTAR
    p.append('<section class=frontsec id=kp><h1 class=major>KATA PENGANTAR</h1>')
    for t in KATA_PENGANTAR: p.append('<p>%s</p>' % esc(t))
    p.append('</section>')
    # DAFTAR ISI bertingkat
    p.append('<section class="frontsec" id=di><h1 class=major>DAFTAR ISI</h1><ul class=toc>')
    p.append('<li class=lvl1><a href="#kp">KATA PENGANTAR</a></li>')
    for b in BAB:
        p.append('<li class=lvl1><a href="#bab%s">BAB %s &nbsp;%s</a></li>' % (b['no'], b['no'], esc(b['judul'])))
        k = 0
        for blk in b['isi']:
            if blk[0] == 'h2':
                k += 1
                p.append('<li class=lvl2><a href="#s%s_%d">%s</a></li>' % (b['no'], k, esc(blk[1])))
    p.append('<li class=lvl1><a href="#dp">DAFTAR PUSTAKA</a></li>')
    p.append('</ul></section>')
    # BAB
    for b in BAB:
        p.append('<section class=bab id=bab%s>' % b['no'])
        p.append('<header class=babhead><div class=babno>BAB %s</div><div class=babtitle>%s</div></header>' % (b['no'], esc(b['judul'])))
        k = 0
        for blk in b['isi']:
            if blk[0] == 'h2':
                k += 1
                p.append('<h2 id="s%s_%d">%s</h2>' % (b['no'], k, esc(blk[1])))
            elif blk[0] == 'table':
                p.append(render_table(blk[1]))
            else:
                p.append('<p>%s</p>' % esc(blk[1]))
        p.append('</section>')
    # DAFTAR PUSTAKA (IEEE bernomor)
    p.append('<section class="bab" id=dp><header class=babhead><div class=babtitle>DAFTAR PUSTAKA</div></header><ol class=ref>')
    for r in DAFTAR_PUSTAKA: p.append('<li>%s</li>' % esc(r))
    p.append('</ol></section></body></html>')
    return ''.join(p)

def cover_html(uri):
    return '<!DOCTYPE html><html><head><meta charset=utf-8><style>%s</style></head><body><img src="%s"></body></html>' % (COVER_CSS, uri)

def main():
    from weasyprint import HTML
    from pypdf import PdfReader, PdfWriter
    os.makedirs(OUTDIR, exist_ok=True)
    front, back = covers()
    doc = HTML(string=content_html()).render()
    content_pages = len(doc.pages)
    print("Halaman ISI:", content_pages)
    content_pdf = BytesIO(); doc.write_pdf(content_pdf); content_pdf.seek(0)
    front_pdf = BytesIO(); HTML(string=cover_html(front)).write_pdf(front_pdf); front_pdf.seek(0)
    back_pdf = BytesIO(); HTML(string=cover_html(back)).write_pdf(back_pdf); back_pdf.seek(0)
    w = PdfWriter()
    for src in (front_pdf, content_pdf, back_pdf):
        for pg in PdfReader(src).pages: w.add_page(pg)
    with open(OUTPDF, 'wb') as f: w.write(f)
    print("TOTAL halaman (dgn cover):", content_pages + 2)
    print("SAVED:", OUTPDF, os.path.getsize(OUTPDF), "bytes")

if __name__ == "__main__":
    main()
