# -*- coding: utf-8 -*-
"""Render Buku #4 (Lidya Ellen Febriasalsa) -> PDF via WeasyPrint, lalu tempel cover via merge.
DNA: dialogis/tanya-jawab, kotak tanya-jawab + tabel ringkas, nomor halaman TENGAH ATAS,
daftar isi TANPA leader (flex, indentasi rapi), daftar pustaka MLA.
Isi dirender TANPA cover => penomoran mulai 1, target-counter TOC akurat. TANPA counter-reset.
"""
import os, html as _html, base64
from io import BytesIO
from konten import KATA_PENGANTAR, BAB, DAFTAR_PUSTAKA

OUTDIR = "Joki-tugas-/FINAL"
OUTPDF = os.path.join(OUTDIR, "Buku 4 - Lidya Ellen Febriasalsa - PKN - FINISH.pdf")
IMGDIR = "Joki-tugas-/_generator/buku4/build_lidya/img"

def covers():
    out = []
    for name in ("cv1.png", "cv2.png"):
        p = os.path.join(IMGDIR, name)
        out.append("data:image/png;base64,%s" % base64.b64encode(open(p, "rb").read()).decode())
    return out

def esc(t): return _html.escape(t)

CSS = r"""
@page { size: A4; margin: 3cm 3cm 2.5cm 3.5cm;
  @top-center { content: counter(page); font-family:'Liberation Serif',serif; font-size:11pt; } }
body { font-family:'Liberation Serif','Times New Roman',serif; font-size:12pt; line-height:1.9;
  text-align:justify; color:#000; hyphens:none; }
p { margin:0 0 12pt 0; orphans:2; widows:2; }
h1.major { font-size:16pt; font-weight:bold; text-align:center; margin:0 0 18pt 0; }
.frontsec { break-before:page; }
#kp { break-before:avoid; }
/* daftar isi: TANPA leader titik, indentasi rapi, nomor halaman rata kanan via flex */
.toc { list-style:none; padding:0; margin:0; }
.toc li { margin:0 0 7pt 0; }
.toc a { color:#000; text-decoration:none; display:flex; justify-content:space-between; align-items:baseline; }
.toc a::after { content: target-counter(attr(href url), page); padding-left:10pt; }
.toc li.tbab a { font-weight:bold; }
.toc li.sub { margin-left:1.1cm; font-size:11pt; }
/* bab */
.bab { break-before:page; }
.babhead { text-align:center; margin:0 0 20pt 0; break-after:avoid; }
.babhead .babno, .babhead .babtitle { font-size:16pt; font-weight:bold; }
.babhead .babtitle { margin-top:4pt; }
h2 { font-size:13pt; font-weight:bold; margin:14pt 0 6pt 0; break-after:avoid; break-inside:avoid; }
/* kotak tanya-jawab (aksen hijau teal, beda dari kotak hangat Buku 3 & tabel biru Buku 2) */
.tanya { border:1px solid #9cc7c0; border-left:5px solid #2e8b78; background:#eef7f5;
  padding:9pt 13pt 5pt 13pt; margin:8pt 0 15pt 0; break-inside:avoid; }
.tanya .jdl { font-weight:bold; font-size:11.5pt; margin:0 0 7pt 0; color:#1f5e54; }
.tanya .q { font-size:11pt; margin:0 0 2pt 0; }
.tanya .q b { color:#1f5e54; }
.tanya .a { font-size:11pt; margin:0 0 9pt 0; }
.tanya .a b { color:#1f5e54; }
/* tabel ringkas (header hijau-abu lembut) */
table.t { width:100%; border-collapse:collapse; margin:6pt 0 14pt 0; font-size:10.5pt; break-inside:avoid; }
table.t caption { caption-side:top; font-style:italic; font-size:10pt; text-align:left; margin-bottom:4pt; color:#3a3a3a; }
table.t th { background:#e4ece4; border:1px solid #9bb39b; padding:5pt 8pt; text-align:left; font-weight:bold; color:#2f4a2f; }
table.t td { border:1px solid #c7d2c7; padding:5pt 8pt; vertical-align:top; }
/* daftar pustaka MLA: hanging indent, tanpa nomor */
.refmla p { margin:0 0 11pt 0; padding-left:1.3cm; text-indent:-1.3cm; font-size:11.5pt; }
"""

COVER_CSS = "@page{size:A4;margin:0;} body{margin:0;} img{width:21cm;height:29.7cm;display:block;object-fit:cover;}"

def render_tanya(t):
    h = ['<div class=tanya><div class=jdl>%s</div>' % esc(t['judul'])]
    for q, a in t['pairs']:
        h.append('<p class=q><b>Tanya:</b> %s</p>' % esc(q))
        h.append('<p class=a><b>Jawab:</b> %s</p>' % esc(a))
    h.append('</div>')
    return ''.join(h)

def render_tabel(tb):
    h = ['<table class="t"><caption>%s</caption>' % esc(tb['judul'])]
    h.append('<thead><tr>' + ''.join('<th>%s</th>' % esc(c) for c in tb['head']) + '</tr></thead><tbody>')
    for row in tb['rows']:
        h.append('<tr>' + ''.join('<td>%s</td>' % esc(c) for c in row) + '</tr>')
    h.append('</tbody></table>')
    return ''.join(h)

def content_html():
    p = ['<!DOCTYPE html><html lang=id><head><meta charset=utf-8><style>%s</style></head><body>' % CSS]
    p.append('<section class=frontsec id=kp><h1 class=major>KATA PENGANTAR</h1>')
    for t in KATA_PENGANTAR: p.append('<p>%s</p>' % esc(t))
    p.append('</section>')
    # DAFTAR ISI tanpa leader
    p.append('<section class="frontsec" id=di><h1 class=major>DAFTAR ISI</h1><ul class=toc>')
    p.append('<li class=tbab><a href="#kp">Kata Pengantar</a></li>')
    for b in BAB:
        p.append('<li class=tbab><a href="#bab%s">BAB %s &nbsp; %s</a></li>' % (b['no'], b['no'], esc(b['judul'].title())))
        k = 0
        for blk in b['isi']:
            if blk[0] == 'h2':
                k += 1
                p.append('<li class=sub><a href="#s%s_%d">%s</a></li>' % (b['no'], k, esc(blk[1])))
    p.append('<li class=tbab><a href="#dp">Daftar Pustaka</a></li>')
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
            elif blk[0] == 'tanya':
                p.append(render_tanya(blk[1]))
            elif blk[0] == 'tabel':
                p.append(render_tabel(blk[1]))
            else:
                p.append('<p>%s</p>' % esc(blk[1]))
        p.append('</section>')
    # DAFTAR PUSTAKA (MLA)
    p.append('<section class="bab" id=dp><header class=babhead><div class=babtitle>DAFTAR PUSTAKA</div></header><div class=refmla>')
    for pre, title, post in DAFTAR_PUSTAKA:
        p.append('<p>%s<i>%s</i>%s</p>' % (esc(pre), esc(title), esc(post)))
    p.append('</div></section></body></html>')
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
