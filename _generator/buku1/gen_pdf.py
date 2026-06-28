# -*- coding: utf-8 -*-
"""Render mini book -> PDF rapi via WeasyPrint, lalu tempel cover via merge.
- Isi dirender TANPA cover => penomoran mulai 1 di Kata Pengantar, TOC target-counter akurat.
- Cover depan & belakang (gambar asli) ditempel sebagai halaman terpisah (tak bernomor, tak dihitung).
- Menyimpan peta nomor halaman tiap bagian -> page_of.json (dipakai Daftar Isi manual DOCX).
"""
import os, zipfile, html as _html, base64, json
from io import BytesIO
from konten import KATA_PENGANTAR, BAB, DAFTAR_PUSTAKA

SRC = "drive_buku/Joki buku pkn/5_6183913965983112173.docx"
OUTDIR = "Joki-tugas-/FINAL"
OUTPDF = os.path.join(OUTDIR, "Buku 1 - Nurul Syifa - PKN - FINISH.pdf")
PAGEMAP = "build_nurul/page_of.json"

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
  @bottom-center { content: counter(page); font-family:'Liberation Serif',serif; font-size:11pt; } }
body { font-family:'Liberation Serif','Times New Roman',serif; font-size:12pt; line-height:1.75;
  text-align:justify; color:#000; hyphens:none; }
p { margin:0 0 12pt 0; orphans:2; widows:2; }
h1.major { font-size:16pt; font-weight:bold; text-align:center; margin:0 0 18pt 0; }
.frontsec { break-before:page; }
#kp { break-before:avoid; }
.toc { list-style:none; padding:0; margin:0; }
.toc li { margin:0 0 12pt 0; }
.toc a { color:#000; text-decoration:none; }
.toc a::after { content: leader('.') target-counter(attr(href url), page); }
.bab { break-before:page; }
.babhead { text-align:center; margin:0 0 20pt 0; break-after:avoid; }
.babhead .babno, .babhead .babtitle { font-size:16pt; font-weight:bold; }
.babhead .babtitle { margin-top:4pt; }
h2 { font-size:13pt; font-weight:bold; margin:14pt 0 6pt 0; break-after:avoid; break-inside:avoid; }
.ref { padding-left:1cm; text-indent:-1cm; margin-bottom:8pt; }
"""

COVER_CSS = "@page{size:A4;margin:0;} body{margin:0;} img{width:21cm;height:29.7cm;display:block;object-fit:cover;}"

def content_html():
    p = ['<!DOCTYPE html><html lang=id><head><meta charset=utf-8><style>%s</style></head><body>' % CSS]
    p.append('<section class=frontsec id=kp><h1 class=major>KATA PENGANTAR</h1>')
    for t in KATA_PENGANTAR: p.append('<p>%s</p>' % esc(t))
    p.append('</section>')
    p.append('<section class="frontsec" id=di><h1 class=major>DAFTAR ISI</h1><ul class=toc>')
    p.append('<li><a href="#kp">KATA PENGANTAR</a></li>')
    for b in BAB:
        p.append('<li><a href="#bab%s">BAB %s &nbsp;%s</a></li>' % (b['no'], b['no'], esc(b['judul'])))
    p.append('<li><a href="#dp">DAFTAR PUSTAKA</a></li></ul></section>')
    for b in BAB:
        p.append('<section class=bab id=bab%s>' % b['no'])
        p.append('<header class=babhead><div class=babno>BAB %s</div><div class=babtitle>%s</div></header>' % (b['no'], esc(b['judul'])))
        for k, t in b['isi']:
            p.append(('<h2>%s</h2>' if k == 'h2' else '<p>%s</p>') % esc(t))
        p.append('</section>')
    p.append('<section class="bab" id=dp><header class=babhead><div class=babtitle>DAFTAR PUSTAKA</div></header>')
    for r in DAFTAR_PUSTAKA: p.append('<p class=ref>%s</p>' % esc(r))
    p.append('</section></body></html>')
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
    # peta anchor -> nomor halaman
    page_of = {}
    for i, page in enumerate(doc.pages, start=1):
        try:
            for a in page.anchors:
                page_of[a] = i
        except Exception:
            pass
    print("Halaman ISI:", content_pages)
    print("page_of:", page_of)

    content_pdf = BytesIO(); doc.write_pdf(content_pdf); content_pdf.seek(0)
    front_pdf = BytesIO(); HTML(string=cover_html(front)).write_pdf(front_pdf); front_pdf.seek(0)
    back_pdf = BytesIO(); HTML(string=cover_html(back)).write_pdf(back_pdf); back_pdf.seek(0)

    w = PdfWriter()
    for src in (front_pdf, content_pdf, back_pdf):
        for pg in PdfReader(src).pages:
            w.add_page(pg)
    with open(OUTPDF, 'wb') as f:
        w.write(f)
    print("TOTAL halaman (dengan cover):", content_pages + 2)
    print("SAVED:", OUTPDF, os.path.getsize(OUTPDF), "bytes")

    json.dump({"content_pages": content_pages, "page_of": page_of},
              open(PAGEMAP, 'w'), indent=2, ensure_ascii=False)
    print("page map ->", PAGEMAP)

if __name__ == "__main__":
    main()
