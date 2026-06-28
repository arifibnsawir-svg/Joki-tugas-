# -*- coding: utf-8 -*-
"""Render Buku #3 (Balqis Lejla) -> PDF via WeasyPrint, lalu tempel cover via merge.
DNA: kontekstual-aplikatif, poin-poin/bullet + kotak studi kasus, nomor halaman POJOK LUAR
berganti (kiri-kanan), daftar isi leader titik dengan nomor bab berformat (zero-pad), Harvard.
Isi dirender TANPA cover => penomoran mulai 1, target-counter TOC akurat. TANPA counter-reset.
"""
import os, html as _html, base64
from io import BytesIO
from konten import KATA_PENGANTAR, BAB, DAFTAR_PUSTAKA

OUTDIR = "Joki-tugas-/FINAL"
OUTPDF = os.path.join(OUTDIR, "Buku 3 - Balqis Lejla - PKN - FINISH.pdf")
IMGDIR = "Joki-tugas-/_generator/buku3/build_balqis/img"

def covers():
    out = []
    for name in ("cv1.png", "cv2.png"):
        p = os.path.join(IMGDIR, name)
        out.append("data:image/png;base64,%s" % base64.b64encode(open(p, "rb").read()).decode())
    return out

def esc(t): return _html.escape(t)

CSS = r"""
@page { size: A4; margin: 3cm 3cm 2.5cm 3.5cm; }
/* nomor halaman pojok LUAR berganti: kanan untuk halaman ganjil, kiri untuk genap */
@page :right { @bottom-right { content: counter(page); font-family:'Liberation Serif',serif; font-size:11pt; } }
@page :left  { @bottom-left  { content: counter(page); font-family:'Liberation Serif',serif; font-size:11pt; } }
body { font-family:'Liberation Serif','Times New Roman',serif; font-size:12pt; line-height:1.9;
  text-align:justify; color:#000; hyphens:none; }
p { margin:0 0 12pt 0; orphans:2; widows:2; }
h1.major { font-size:16pt; font-weight:bold; text-align:center; margin:0 0 18pt 0; }
.frontsec { break-before:page; }
#kp { break-before:avoid; }
/* daftar isi: leader titik, nomor bab berformat (zero-pad pada kotak) */
.toc { list-style:none; padding:0; margin:0; }
.toc li { margin:0 0 7pt 0; }
.toc a { color:#000; text-decoration:none; }
.toc a::after { content: leader('.') target-counter(attr(href url), page); }
.toc li.tbab a { font-weight:bold; }
.toc .bno { display:inline-block; min-width:1.0cm; font-weight:bold; color:#7a4a00; }
.toc li.sub { margin-left:1.4cm; font-size:11pt; }
/* bab */
.bab { break-before:page; }
.babhead { text-align:center; margin:0 0 20pt 0; break-after:avoid; }
.babhead .babno, .babhead .babtitle { font-size:16pt; font-weight:bold; }
.babhead .babtitle { margin-top:4pt; }
h2 { font-size:13pt; font-weight:bold; margin:14pt 0 6pt 0; break-after:avoid; break-inside:avoid; }
/* poin-poin / bullet */
ul.poin { margin:4pt 0 12pt 0; padding-left:0.95cm; }
ul.poin li { margin:0 0 5pt 0; text-align:justify; padding-left:2pt; }
/* kotak studi kasus (warna lembut hangat, beda dari tabel biru Buku 2) */
.kasus { border:1px solid #d2b48c; border-left:5px solid #b8860b; background:#fbf6ec;
  padding:9pt 13pt 4pt 13pt; margin:8pt 0 15pt 0; break-inside:avoid; }
.kasus .ktitle { font-weight:bold; font-size:11.5pt; margin:0 0 6pt 0; color:#6b4500; }
.kasus p { margin:0 0 8pt 0; font-size:11pt; }
.kasus .krefleksi { font-style:italic; font-size:10.5pt; margin:0 0 8pt 0; color:#5a3d00; }
/* daftar pustaka Harvard: hanging indent, tanpa nomor */
.refharvard p { margin:0 0 10pt 0; padding-left:1.3cm; text-indent:-1.3cm; font-size:11.5pt; }
"""

COVER_CSS = "@page{size:A4;margin:0;} body{margin:0;} img{width:21cm;height:29.7cm;display:block;object-fit:cover;}"

def render_ul(items):
    return '<ul class=poin>' + ''.join('<li>%s</li>' % esc(x) for x in items) + '</ul>'

def render_kasus(k):
    h = ['<div class=kasus><div class=ktitle>%s</div>' % esc(k['judul'])]
    for par in k['isi']:
        h.append('<p>%s</p>' % esc(par))
    h.append('<p class=krefleksi>Refleksi: %s</p>' % esc(k['refleksi']))
    h.append('</div>')
    return ''.join(h)

def content_html():
    p = ['<!DOCTYPE html><html lang=id><head><meta charset=utf-8><style>%s</style></head><body>' % CSS]
    # KATA PENGANTAR
    p.append('<section class=frontsec id=kp><h1 class=major>KATA PENGANTAR</h1>')
    for t in KATA_PENGANTAR: p.append('<p>%s</p>' % esc(t))
    p.append('</section>')
    # DAFTAR ISI (leader titik, nomor bab zero-pad)
    p.append('<section class="frontsec" id=di><h1 class=major>DAFTAR ISI</h1><ul class=toc>')
    p.append('<li class=tbab><a href="#kp">Kata Pengantar</a></li>')
    for b in BAB:
        p.append('<li class=tbab><a href="#bab%s"><span class=bno>%02d</span>%s</a></li>'
                 % (b['no'], int(b['no']), esc(b['judul'].title())))
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
        p.append('<header class=babhead><div class=babno>BAB %s</div><div class=babtitle>%s</div></header>'
                 % (b['no'], esc(b['judul'])))
        k = 0
        for blk in b['isi']:
            if blk[0] == 'h2':
                k += 1
                p.append('<h2 id="s%s_%d">%s</h2>' % (b['no'], k, esc(blk[1])))
            elif blk[0] == 'ul':
                p.append(render_ul(blk[1]))
            elif blk[0] == 'kasus':
                p.append(render_kasus(blk[1]))
            else:
                p.append('<p>%s</p>' % esc(blk[1]))
        p.append('</section>')
    # DAFTAR PUSTAKA (Harvard)
    p.append('<section class="bab" id=dp><header class=babhead><div class=babtitle>DAFTAR PUSTAKA</div></header><div class=refharvard>')
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
