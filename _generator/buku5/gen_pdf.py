# -*- coding: utf-8 -*-
"""Render Buku #5 (Nurjali Sangadji) -> PDF via WeasyPrint, lalu tempel cover via merge.
DNA: ekspositori + kotak Poin Inti (bernomor) + kotak Istilah Kunci, warna indigo/slate,
nomor halaman BAWAH-TENGAH (dgn garis), daftar isi BANDED (tanpa titik), pustaka Chicago.
Isi dirender TANPA cover => penomoran mulai 1, target-counter TOC akurat. TANPA counter-reset.
"""
import os, html as _html, base64
from io import BytesIO
from konten import KATA_PENGANTAR, BAB, DAFTAR_PUSTAKA

OUTDIR = "Joki-tugas-/FINAL"
OUTPDF = os.path.join(OUTDIR, "Buku 5 - Nurjali Sangadji - PKN - FINISH.pdf")
IMGDIR = "Joki-tugas-/_generator/buku5/build_nurjali/img"

def covers():
    out = []
    for name in ("cv1.jpg", "cv2.jpg"):
        p = os.path.join(IMGDIR, name)
        out.append("data:image/jpeg;base64,%s" % base64.b64encode(open(p, "rb").read()).decode())
    return out

def esc(t): return _html.escape(t)

CSS = r"""
@page { size: A4; margin: 3cm 3cm 2.5cm 3.5cm;
  @bottom-center { content: counter(page); font-family:'Liberation Serif',serif; font-size:11pt;
    border-top:0.5pt solid #8a8fb5; padding-top:3pt; color:#2b2f5e; } }
body { font-family:'Liberation Serif','Times New Roman',serif; font-size:12pt; line-height:1.9;
  text-align:justify; color:#000; hyphens:none; }
p { margin:0 0 12pt 0; orphans:2; widows:2; }
h1.major { font-size:16pt; font-weight:bold; text-align:center; margin:0 0 18pt 0; color:#2b2f5e; }
.frontsec { break-before:page; }
#kp { break-before:avoid; }
/* daftar isi BANDED: bab pakai pita warna lembut, tanpa titik-titik, nomor rata kanan */
.toc { list-style:none; padding:0; margin:0; }
.toc li { margin:0 0 4pt 0; }
.toc a { color:#000; text-decoration:none; display:flex; justify-content:space-between; align-items:baseline; }
.toc a::after { content: target-counter(attr(href url), page); padding-left:10pt; font-weight:normal; }
.toc li.tbab { background:#e9ebf6; padding:4pt 8pt; margin-top:6pt; border-left:3pt solid #4a4f93; }
.toc li.tbab a { font-weight:bold; color:#2b2f5e; }
.toc li.sub { margin-left:1.0cm; font-size:11pt; }
/* bab */
.bab { break-before:page; }
.babhead { text-align:center; margin:0 0 20pt 0; break-after:avoid; }
.babhead .babno, .babhead .babtitle { font-size:16pt; font-weight:bold; color:#2b2f5e; }
.babhead .babtitle { margin-top:4pt; }
h2 { font-size:13pt; font-weight:bold; margin:14pt 0 6pt 0; break-after:avoid; break-inside:avoid; color:#2b2f5e; }
/* kotak Poin Inti (indigo, daftar bernomor) */
.poin { border:1px solid #a9aede; border-left:5px solid #4a4f93; background:#eef0f8;
  padding:8pt 14pt 8pt 14pt; margin:8pt 0 15pt 0; break-inside:avoid; }
.poin .jdl { font-weight:bold; font-size:11.5pt; margin:0 0 5pt 0; color:#2b2f5e; }
.poin ol { margin:0; padding-left:1.1cm; }
.poin li { font-size:11pt; margin:0 0 4pt 0; text-align:justify; }
/* kotak Istilah Kunci (indigo lebih lembut) */
.istilah { border:1px dashed #8a8fc4; background:#f5f6fb; padding:8pt 14pt 4pt 14pt; margin:8pt 0 15pt 0; break-inside:avoid; }
.istilah .jdl { font-weight:bold; font-size:11.5pt; margin:0 0 5pt 0; color:#3a3f80; }
.istilah p { font-size:11pt; margin:0 0 6pt 0; }
.istilah .term { font-weight:bold; color:#2b2f5e; }
/* daftar pustaka Chicago: hanging indent, tanpa nomor */
.refchicago p { margin:0 0 11pt 0; padding-left:1.3cm; text-indent:-1.3cm; font-size:11.5pt; }
"""

COVER_CSS = "@page{size:A4;margin:0;} body{margin:0;} img{width:21cm;height:29.7cm;display:block;object-fit:cover;}"

def render_poin(p):
    h = ['<div class=poin><div class=jdl>%s</div><ol>' % esc(p['judul'])]
    for it in p['items']: h.append('<li>%s</li>' % esc(it))
    h.append('</ol></div>')
    return ''.join(h)

def render_istilah(t):
    h = ['<div class=istilah><div class=jdl>%s</div>' % esc(t['judul'])]
    for term, arti in t['pairs']:
        h.append('<p><span class=term>%s:</span> %s</p>' % (esc(term), esc(arti)))
    h.append('</div>')
    return ''.join(h)

def content_html():
    p = ['<!DOCTYPE html><html lang=id><head><meta charset=utf-8><style>%s</style></head><body>' % CSS]
    p.append('<section class=frontsec id=kp><h1 class=major>KATA PENGANTAR</h1>')
    for t in KATA_PENGANTAR: p.append('<p>%s</p>' % esc(t))
    p.append('</section>')
    # DAFTAR ISI banded
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
            elif blk[0] == 'poin':
                p.append(render_poin(blk[1]))
            elif blk[0] == 'istilah':
                p.append(render_istilah(blk[1]))
            else:
                p.append('<p>%s</p>' % esc(blk[1]))
        p.append('</section>')
    # DAFTAR PUSTAKA (Chicago)
    p.append('<section class="bab" id=dp><header class=babhead><div class=babtitle>DAFTAR PUSTAKA</div></header><div class=refchicago>')
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
