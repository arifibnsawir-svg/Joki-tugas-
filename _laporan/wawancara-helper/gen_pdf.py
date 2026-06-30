# -*- coding: utf-8 -*-
"""
Render Laporan Wawancara Helper -> PDF via WeasyPrint.
Seluruh dokumen dirender dalam satu kali proses agar target-counter (Daftar Isi)
akurat. TANPA counter-reset/counter-set. hyphens:none. Halaman A4, Liberation Serif 12pt.
Halaman judul dibuat dari teks (bukan gambar). Foto dokumentasi disisipkan di Lampiran 3.
"""
import os, html as _html, base64
import konten as K

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "LAPORAN_FINAL")
OUTDIR = os.path.abspath(OUTDIR)
OUTPDF = os.path.join(OUTDIR, "Laporan Wawancara Helper - Kelompok - Pengembangan Profesi Konseling - FINISH.pdf")
FOTODIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_foto_dl")

def esc(t):
    return _html.escape(str(t))

CSS = r"""
@page {
  size: A4;
  margin: 3cm 3cm 3cm 4cm;
  @bottom-center { content: counter(page); font-family:'Liberation Serif',serif; font-size:11pt; }
}
@page :first { @bottom-center { content: normal; } }

html { font-family:'Liberation Serif','Times New Roman',serif; }
body { font-size:12pt; line-height:1.5; text-align:justify; color:#000; hyphens:none; }
p { margin:0 0 6pt 0; orphans:2; widows:2; text-indent:0; }
p.lead { margin:0 0 8pt 0; }

/* HALAMAN JUDUL */
.titlepage { text-align:center; page-break-after:always; height:100%; }
.titlepage .judul { font-size:16pt; font-weight:bold; margin-top:1.5cm; line-height:1.4; text-transform:uppercase; }
.titlepage .subjudul { font-size:12pt; font-style:italic; margin:14pt 1.5cm 0 1.5cm; line-height:1.4; }
.titlepage .label { font-size:12pt; margin-top:24pt; }
.titlepage .logo { font-size:12pt; font-weight:bold; margin:24pt 0; }
.titlepage .penyusun { font-size:12pt; margin-top:18pt; line-height:1.5; }
.titlepage .footer { font-size:14pt; font-weight:bold; margin-top:24pt; line-height:1.5; text-transform:uppercase; }

/* JUDUL BAGIAN & BAB */
h1.major { font-size:14pt; font-weight:bold; text-align:center; margin:0 0 16pt 0; text-transform:uppercase; break-after:avoid; }
.babhead { text-align:center; margin:0 0 18pt 0; break-after:avoid; }
.babhead .babno { font-size:14pt; font-weight:bold; }
.babhead .babtitle { font-size:14pt; font-weight:bold; margin-top:4pt; }
h2 { font-size:12pt; font-weight:bold; margin:12pt 0 6pt 0; break-after:avoid; }
h3 { font-size:12pt; font-weight:bold; font-style:italic; margin:10pt 0 4pt 0; break-after:avoid; }
.sec { break-before:page; }

/* DAFTAR ISI */
ul.toc { list-style:none; padding:0; margin:0; }
ul.toc li { margin:0 0 6pt 0; line-height:1.4; }
ul.toc li.lvl2 { margin-left:0.9cm; }
ul.toc a { color:#000; text-decoration:none; display:block; }
ul.toc a::after { content: leader('.') target-counter(attr(href url), page); }
ul.toc li.lvl1 > a { font-weight:bold; }

/* DAFTAR & NOMOR */
ol.num { margin:0 0 8pt 0; padding-left:1.2cm; }
ol.num li { margin:0 0 4pt 0; }

/* TABEL */
table.t { width:100%; border-collapse:collapse; margin:6pt 0 12pt 0; font-size:11pt; break-inside:avoid; }
table.t caption { caption-side:top; font-style:italic; font-size:11pt; text-align:left; margin-bottom:5pt; }
table.t th { background:#dfe6f0; border:1px solid #6f86ad; padding:5pt 7pt; text-align:left; font-weight:bold; }
table.t td { border:1px solid #aab6cc; padding:5pt 7pt; vertical-align:top; }
table.t tr:nth-child(even) td { background:#f3f6fb; }

/* DAFTAR PUSTAKA (APA hanging indent) */
ul.ref { list-style:none; padding:0; margin:0; }
ul.ref li { margin:0 0 10pt 0; padding-left:1.2cm; text-indent:-1.2cm; word-break:break-word; }

/* LAMPIRAN */
.qa { margin:0 0 8pt 0; }
.qa .q { font-weight:bold; }
.foto { text-align:center; margin:12pt 0 16pt 0; break-inside:avoid; }
.foto img { max-width:11cm; max-height:9cm; border:1px solid #888; }
.foto .cap { font-size:11pt; font-style:italic; margin-top:5pt; }
.placeholder { width:10cm; height:6cm; border:1px dashed #888; margin:0 auto; line-height:6cm; color:#555; }
"""

def render_blocks(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "h2":
            out.append('<h2 id="%s">%s</h2>' % (slug(b[1]), esc(b[1])))
        elif kind == "h3":
            out.append("<h3>%s</h3>" % esc(b[1]))
        elif kind == "p":
            out.append("<p>%s</p>" % esc(b[1]))
        elif kind == "lead":
            out.append('<p class="lead">%s</p>' % esc(b[1]))
        elif kind == "num":
            out.append("<ol class=num>" + "".join("<li>%s</li>" % esc(x) for x in b[1]) + "</ol>")
        elif kind == "table":
            out.append(render_table(b[1]))
    return "".join(out)

def render_table(tb):
    h = ['<table class="t"><caption>%s</caption><thead><tr>' % esc(tb["judul"])]
    h.append("".join("<th>%s</th>" % esc(c) for c in tb["head"]))
    h.append("</tr></thead><tbody>")
    for row in tb["rows"]:
        h.append("<tr>" + "".join("<td>%s</td>" % esc(c) for c in row) + "</tr>")
    h.append("</tbody></table>")
    return "".join(h)

def slug(text):
    s = "".join(ch.lower() if ch.isalnum() else "-" for ch in text)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")[:50]

def img_data_uri(path):
    ext = os.path.splitext(path)[1].lstrip(".").lower()
    mime = "image/png" if ext == "png" else "image/jpeg"
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode())

def title_page():
    I = K.IDENTITAS
    p = ['<section class="titlepage">']
    p.append('<div class="judul">%s</div>' % esc(I["judul"]))
    p.append('<div class="subjudul">%s</div>' % esc(I["subjudul"]))
    p.append('<div class="label">Disusun untuk memenuhi tugas mata kuliah<br>%s</div>' % esc(I["matakuliah"]))
    p.append('<div class="label">Dosen Pengampu: %s</div>' % esc(I["dosen"]))
    p.append('<div class="logo">UNIVERSITAS INDRAPRASTA PGRI</div>')
    rows = "".join("%s &nbsp;&nbsp; %s<br>" % (esc(n), esc(nim)) for n, nim in I["penyusun"])
    p.append('<div class="penyusun">Disusun oleh:<br>%s</div>' % rows)
    p.append('<div class="footer">%s<br>%s<br>%s<br>%s</div>' % (
        esc(I["prodi"]), esc(I["fakultas"]), esc(I["universitas"]), esc(I["tahun"])))
    p.append("</section>")
    return "".join(p)

def toc():
    p = ['<section class="sec" id="di"><h1 class="major">DAFTAR ISI</h1><ul class="toc">']
    p.append('<li class="lvl1"><a href="#kp">KATA PENGANTAR</a></li>')
    for b in K.BAB_LIST:
        p.append('<li class="lvl1"><a href="#bab%s">BAB %s &nbsp;%s</a></li>' % (b["no"], b["no"], esc(b["judul"])))
        for blk in b["isi"]:
            if blk[0] == "h2":
                p.append('<li class="lvl2"><a href="#%s">%s</a></li>' % (slug(blk[1]), esc(blk[1])))
    p.append('<li class="lvl1"><a href="#dp">DAFTAR PUSTAKA</a></li>')
    p.append('<li class="lvl1"><a href="#lamp1">LAMPIRAN 1: Daftar Pertanyaan Wawancara</a></li>')
    p.append('<li class="lvl1"><a href="#lamp2">LAMPIRAN 2: Transkrip Wawancara</a></li>')
    p.append('<li class="lvl1"><a href="#lamp3">LAMPIRAN 3: Dokumentasi Kegiatan</a></li>')
    p.append("</ul></section>")
    return "".join(p)

def lampiran():
    p = []
    # Lampiran 1
    p.append('<section class="sec" id="lamp1"><h1 class="major">LAMPIRAN 1: DAFTAR PERTANYAAN WAWANCARA</h1>')
    p.append("<p>Berikut lima belas butir pertanyaan yang disusun berdasarkan Rencana Pembelajaran Semester dan diajukan kepada seluruh narasumber dengan penyesuaian bahasa sesuai profesi.</p>")
    p.append("<ol class=num>" + "".join("<li>%s</li>" % esc(q) for q in K.PERTANYAAN) + "</ol></section>")
    # Lampiran 2
    p.append('<section class="sec" id="lamp2"><h1 class="major">LAMPIRAN 2: TRANSKRIP WAWANCARA</h1>')
    for h in K.HELPERS:
        p.append('<h2>Transkrip %s: %s (%s)</h2>' % (esc(h["kode"]), esc(h["nama"]), esc(h["profesi"])))
        for i, (judul, teks) in enumerate(h["poin"], 1):
            p.append('<div class="qa"><div class="q">%d. %s</div><div>%s</div></div>' % (i, esc(K.PERTANYAAN[i-1]), esc(teks)))
    p.append("</section>")
    # Lampiran 3 (foto)
    p.append('<section class="sec" id="lamp3"><h1 class="major">LAMPIRAN 3: DOKUMENTASI KEGIATAN</h1>')
    p.append("<p>Berikut dokumentasi kegiatan wawancara bersama keempat narasumber.</p>")
    missing = []
    for h in K.HELPERS:
        path = os.path.join(FOTODIR, h["foto"])
        cap = "Dokumentasi wawancara dengan %s (%s)" % (h["nama"], h["profesi"])
        if os.path.exists(path):
            p.append('<div class="foto"><img src="%s"><div class="cap">%s</div></div>' % (img_data_uri(path), esc(cap)))
        else:
            missing.append(h["foto"])
            p.append('<div class="foto"><div class="placeholder">[Foto belum tersedia]</div><div class="cap">%s</div></div>' % esc(cap))
    p.append("</section>")
    if missing:
        print("PERINGATAN: foto tidak ditemukan ->", missing)
    return "".join(p)

def content_html():
    p = ['<!DOCTYPE html><html lang="id"><head><meta charset="utf-8"><style>%s</style></head><body>' % CSS]
    p.append(title_page())
    # Kata Pengantar
    p.append('<section class="sec" id="kp"><h1 class="major">KATA PENGANTAR</h1>')
    for t in K.KATA_PENGANTAR:
        p.append("<p>%s</p>" % esc(t))
    p.append("</section>")
    # Daftar Isi
    p.append(toc())
    # BAB I - V
    for b in K.BAB_LIST:
        p.append('<section class="sec" id="bab%s">' % b["no"])
        p.append('<div class="babhead"><div class="babno">BAB %s</div><div class="babtitle">%s</div></div>' % (b["no"], esc(b["judul"])))
        p.append(render_blocks(b["isi"]))
        p.append("</section>")
    # Daftar Pustaka
    p.append('<section class="sec" id="dp"><h1 class="major">DAFTAR PUSTAKA</h1><ul class="ref">')
    for r in K.DAFTAR_PUSTAKA:
        p.append("<li>%s</li>" % esc(r))
    p.append("</ul></section>")
    # Lampiran
    p.append(lampiran())
    p.append("</body></html>")
    return "".join(p)

def main():
    from weasyprint import HTML
    os.makedirs(OUTDIR, exist_ok=True)
    html = content_html()
    doc = HTML(string=html).render()
    print("Total halaman PDF:", len(doc.pages))
    doc.write_pdf(OUTPDF)
    print("SAVED:", OUTPDF, os.path.getsize(OUTPDF), "bytes")

if __name__ == "__main__":
    main()
