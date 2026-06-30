# -*- coding: utf-8 -*-
"""Render Buku 6 (Revalina Damayanti) -> PDF via WeasyPrint.
Cover depan & belakang DIDESAIN (maroon + Garuda emas), tanpa kata 'minibook'.
Sampul belakang seirama + biografi penulis. Isi tema maroon, no.halaman POJOK KANAN ATAS,
daftar isi NOMOR RATA KANAN + GARIS tiap bab (tanpa dot-leader), pustaka Vancouver.
Isi dirender TANPA cover => penomoran mulai 1 & target-counter TOC akurat. TANPA counter-reset.
"""
import os, html as _html, base64
from io import BytesIO
from konten import (KATA_PENGANTAR, BAB, DAFTAR_PUSTAKA, BIOGRAFI,
                    PENULIS, NPM, PRODI, KAMPUS, TAHUN)

OUTDIR = "Joki-tugas-/FINAL"
OUTPDF = os.path.join(OUTDIR, "Buku 6 - Revalina Damayanti - PKN - FINISH.pdf")
ASSET = "Joki-tugas-/_generator/buku6/assets/garuda.png"
JUDUL = "PENDIDIKAN KEWARGANEGARAAN"
JUDUL2 = "DI PERGURUAN TINGGI"

def esc(t): return _html.escape(t)

def garuda_uri():
    return "data:image/png;base64,%s" % base64.b64encode(open(ASSET, "rb").read()).decode()

# ------------------------------- ISI -------------------------------
CSS = r"""
@page { size: A4; margin: 3cm 3cm 2.5cm 3.5cm;
  @top-right { content: counter(page); font-family:'Liberation Serif',serif; font-size:11pt;
    color:#6e1423; font-weight:bold; } }
body { font-family:'Liberation Serif','Times New Roman',serif; font-size:12pt; line-height:2.25;
  text-align:justify; color:#16100f; hyphens:none; }
p { margin:0 0 14pt 0; orphans:2; widows:2; }
h1.major { font-size:16pt; font-weight:bold; text-align:center; margin:0 0 18pt 0; color:#6e1423;
  letter-spacing:0.5pt; }
.frontsec { break-before:page; }
#kp { break-before:avoid; }
/* DAFTAR ISI: nomor rata kanan + GARIS tipis tiap bab, tanpa titik-titik */
.toc { list-style:none; padding:0; margin:0; }
.toc a { color:#16100f; text-decoration:none; display:flex; justify-content:space-between; align-items:baseline; }
.toc a::after { content: target-counter(attr(href url), page); padding-left:12pt; color:#6e1423; }
.toc li.tbab { margin:9pt 0 2pt 0; padding-bottom:3pt; border-bottom:0.75pt solid #c8a24a; }
.toc li.tbab a { font-weight:bold; color:#6e1423; text-transform:uppercase; font-size:11.5pt; }
.toc li.sub { margin:2pt 0 2pt 0.9cm; font-size:11pt; }
.toc li.sub a { color:#3a2a22; }
.toc li.sub a::after { color:#9a7b33; }
/* BAB */
.bab { break-before:page; }
.babhead { text-align:center; margin:0 0 20pt 0; break-after:avoid; }
.babhead .babno { font-size:13pt; font-weight:bold; color:#c8a24a; letter-spacing:2pt; }
.babhead .babtitle { font-size:16.5pt; font-weight:bold; color:#6e1423; margin-top:5pt; }
.babhead .rule { width:3.2cm; height:2.5pt; background:#c8a24a; margin:9pt auto 0 auto; }
h2 { font-size:13pt; font-weight:bold; margin:14pt 0 6pt 0; break-after:avoid; break-inside:avoid;
  color:#6e1423; padding-left:8pt; border-left:4pt solid #c8a24a; }
/* kotak Akar Masalah (maroon) */
.akar { border:1pt solid #b9485a; border-left:6pt solid #6e1423; background:#f7ebed;
  padding:9pt 15pt 5pt 15pt; margin:10pt 0 15pt 0; break-inside:avoid; }
.akar .jdl { font-weight:bold; font-size:12pt; margin:0 0 6pt 0; color:#6e1423; }
.akar ul { margin:0; padding-left:1.0cm; }
.akar li { font-size:11pt; margin:0 0 5pt 0; text-align:justify; }
/* kotak Langkah Solusi (emas/krem) */
.solusi { border:1pt solid #c8a24a; border-left:6pt solid #a87f23; background:#fbf4e3;
  padding:9pt 15pt 5pt 15pt; margin:10pt 0 15pt 0; break-inside:avoid; }
.solusi .jdl { font-weight:bold; font-size:12pt; margin:0 0 6pt 0; color:#7a5b12; }
.solusi ul { margin:0; padding-left:1.0cm; }
.solusi li { font-size:11pt; margin:0 0 5pt 0; text-align:justify; }
/* DAFTAR PUSTAKA Vancouver: hanging indent */
.refvanc p { margin:0 0 11pt 0; padding-left:1.0cm; text-indent:-1.0cm; font-size:11.5pt; }
"""

def render_akar(d):
    h = ['<div class=akar><div class=jdl>%s</div><ul>' % esc(d['judul'])]
    for it in d['items']: h.append('<li>%s</li>' % esc(it))
    h.append('</ul></div>')
    return ''.join(h)

def render_solusi(d):
    h = ['<div class=solusi><div class=jdl>%s</div><ul>' % esc(d['judul'])]
    for it in d['items']: h.append('<li>%s</li>' % esc(it))
    h.append('</ul></div>')
    return ''.join(h)

def content_html():
    p = ['<!DOCTYPE html><html lang=id><head><meta charset=utf-8><style>%s</style></head><body>' % CSS]
    # KATA PENGANTAR
    p.append('<section class=frontsec id=kp><h1 class=major>KATA PENGANTAR</h1>')
    for t in KATA_PENGANTAR: p.append('<p>%s</p>' % esc(t))
    p.append('</section>')
    # DAFTAR ISI (ruled)
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
        p.append('<header class=babhead><div class=babno>BAB %s</div><div class=babtitle>%s</div><div class=rule></div></header>' % (b['no'], esc(b['judul'])))
        k = 0
        for blk in b['isi']:
            if blk[0] == 'h2':
                k += 1
                p.append('<h2 id="s%s_%d">%s</h2>' % (b['no'], k, esc(blk[1])))
            elif blk[0] == 'akar':
                p.append(render_akar(blk[1]))
            elif blk[0] == 'solusi':
                p.append(render_solusi(blk[1]))
            else:
                p.append('<p>%s</p>' % esc(blk[1]))
        p.append('</section>')
    # DAFTAR PUSTAKA
    p.append('<section class="bab" id=dp><header class=babhead><div class=babtitle>DAFTAR PUSTAKA</div><div class=rule></div></header><div class=refvanc>')
    for pre, title, post in DAFTAR_PUSTAKA:
        p.append('<p>%s<i>%s</i>%s</p>' % (esc(pre), esc(title), esc(post)))
    p.append('</div></section></body></html>')
    return ''.join(p)

# ------------------------------- COVER -------------------------------
COVER_CSS = r"""
@page { size:A4; margin:0; }
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Liberation Sans','Helvetica',sans-serif; }
.page { width:21cm; height:29.7cm; background:#6e1423;
  background-image:radial-gradient(circle at 50% 30%, #87202f 0%, #6e1423 55%, #560d1a 100%);
  position:relative; color:#fff; }
.frame { position:absolute; top:1.0cm; left:1.0cm; right:1.0cm; bottom:1.0cm;
  border:2.5pt solid #c8a24a; }
.frame::after { content:""; position:absolute; top:5pt; left:5pt; right:5pt; bottom:5pt;
  border:0.75pt solid #c8a24a; opacity:0.7; }
/* DEPAN */
.f-title { position:absolute; top:3.2cm; left:2.2cm; right:2.2cm; text-align:center; }
.f-title .t1 { font-size:30pt; font-weight:bold; letter-spacing:1pt; line-height:1.15;
  color:#ffffff; text-shadow:0 1pt 2pt rgba(0,0,0,0.35); }
.f-title .t2 { font-size:17pt; font-weight:bold; letter-spacing:3pt; margin-top:10pt; color:#f1cf7a; }
.f-garuda { position:absolute; top:9.6cm; left:0; right:0; text-align:center; }
.f-garuda img { height:11.5cm; }
.f-author { position:absolute; bottom:2.6cm; left:2cm; right:2cm; text-align:center; }
.f-author .lbl { font-size:12pt; letter-spacing:1pt; color:#f1cf7a; }
.f-author .nm { font-size:19pt; font-weight:bold; margin-top:4pt; color:#ffffff; }
.f-author .npm { font-size:12.5pt; margin-top:2pt; color:#f4e6c2; }
.f-author .org { font-size:12.5pt; margin-top:10pt; line-height:1.45; color:#ffffff; }
.f-author .org b { color:#f1cf7a; }
/* BELAKANG */
.b-wrap { position:absolute; top:2.4cm; left:2.2cm; right:2.2cm; }
.b-head { text-align:center; }
.b-head .bg { height:2.7cm; opacity:0.92; }
.b-head .h { font-size:18pt; font-weight:bold; letter-spacing:3pt; color:#f1cf7a; margin-top:9pt; }
.b-head .hr { width:3.5cm; height:2pt; background:#c8a24a; margin:8pt auto 0 auto; }
.b-panel { margin-top:0.7cm; background:#fbf4e3; color:#2a1a14; border:1pt solid #c8a24a;
  padding:0.7cm 0.85cm; text-align:justify; }
.b-panel p { font-size:11.5pt; line-height:1.6; margin-bottom:9pt; font-family:'Liberation Serif',serif; }
.b-panel p:last-child { margin-bottom:0; }
.b-sign { margin-top:0.9cm; text-align:center; color:#fff; }
.b-sign .nm { font-size:14pt; font-weight:bold; color:#f1cf7a; }
.b-sign .org { font-size:11.5pt; margin-top:3pt; line-height:1.5; }
"""

def front_html(g):
    return (
      '<!DOCTYPE html><html><head><meta charset=utf-8><style>%s</style></head><body>'
      '<div class=page><div class=frame></div>'
      '<div class=f-title><div class=t1>%s</div><div class=t2>%s</div></div>'
      '<div class=f-garuda><img src="%s"></div>'
      '<div class=f-author>'
      '<div class=lbl>Disusun oleh</div>'
      '<div class=nm>%s</div>'
      '<div class=npm>NPM %s</div>'
      '<div class=org>%s<br><b>%s</b><br>%s</div>'
      '</div></div></body></html>'
    ) % (COVER_CSS, esc(JUDUL), esc(JUDUL2), g, esc(PENULIS), esc(NPM), esc(PRODI), esc(KAMPUS), esc(TAHUN))

def back_html(g):
    bio = ''.join('<p>%s</p>' % esc(t) for t in BIOGRAFI)
    return (
      '<!DOCTYPE html><html><head><meta charset=utf-8><style>%s</style></head><body>'
      '<div class=page><div class=frame></div>'
      '<div class=b-wrap>'
      '<div class=b-head><img class=bg src="%s"><div class=h>BIOGRAFI PENULIS</div><div class=hr></div></div>'
      '<div class=b-panel>%s</div>'
      '<div class=b-sign><div class=nm>%s</div><div class=org>NPM %s<br>%s<br>%s</div></div>'
      '</div></div></body></html>'
    ) % (COVER_CSS, g, bio, esc(PENULIS), esc(NPM), esc(PRODI), esc(KAMPUS))

def main():
    from weasyprint import HTML
    from pypdf import PdfReader, PdfWriter
    os.makedirs(OUTDIR, exist_ok=True)
    g = garuda_uri()
    doc = HTML(string=content_html()).render()
    content_pages = len(doc.pages)
    print("Halaman ISI:", content_pages)
    content_pdf = BytesIO(); doc.write_pdf(content_pdf); content_pdf.seek(0)
    front_pdf = BytesIO(); HTML(string=front_html(g)).write_pdf(front_pdf); front_pdf.seek(0)
    back_pdf = BytesIO(); HTML(string=back_html(g)).write_pdf(back_pdf); back_pdf.seek(0)
    w = PdfWriter()
    for src in (front_pdf, content_pdf, back_pdf):
        for pg in PdfReader(src).pages: w.add_page(pg)
    with open(OUTPDF, 'wb') as f: w.write(f)
    print("TOTAL halaman (dgn cover):", content_pages + 2)
    print("SAVED:", OUTPDF, os.path.getsize(OUTPDF), "bytes")

if __name__ == "__main__":
    main()
