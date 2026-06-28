# -*- coding: utf-8 -*-
"""Render Modul Gaya Belajar (Kelompok 10) -> PDF PREMIUM via WeasyPrint.
Tema warna ber-kode VAK. Cover didesain. Font Caladea (metrik Cambria). Margin kiri4/kanan3/atas3/bawah3.
Nomor halaman angka Arab di bawah-tengah. Isi dirender TANPA cover lalu cover di-merge via pypdf
supaya penomoran mulai 1 dan target-counter (Daftar Isi/Tabel/Gambar) akurat. TANPA counter-reset.
Layout BLOCK (hindari bug flex WeasyPrint).
"""
import os, html as _html, base64
from io import BytesIO
import konten as K

OUT = "Joki-tugas-/MODUL_FINAL"
OUTPDF = os.path.join(OUT, "Modul Gaya Belajar - Kelompok 10 - BnP - FINAL.pdf")
ASSET = "Joki-tugas-/_modul/gaya-belajar/assets"

def esc(t): return _html.escape(str(t))

def img_uri(name):
    with open(os.path.join(ASSET, name), "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

BOXSTYLE = {  # kind -> (warna garis/judul, warna latar)
    "tujuan":    ("#1f3c88", "#eef1fb"),
    "contoh":    ("#0e7490", "#e6f6fa"),
    "aktivitas": ("#ea7317", "#fdf1e6"),
    "ringkasan": ("#15a34a", "#e9f7ee"),
    "tips":      ("#7c3aed", "#f3edfd"),
}
BOXLABEL = {"tujuan": "Tujuan", "contoh": "Contoh", "aktivitas": "Aktivitas", "ringkasan": "Ringkasan", "tips": "Info"}

CSS = """
@page { size: A4; margin: 3cm 3cm 3cm 4cm;
  @bottom-center { content: counter(page); font-family:'Caladea',serif; font-size:11pt; color:#1f3c88; } }
@page:first { @bottom-center { content: counter(page); } }
* { box-sizing: border-box; }
body { font-family:'Caladea','Liberation Serif',serif; font-size:12pt; line-height:1.5; text-align:justify;
  color:#1c2536; hyphens:none; }
p { margin:0 0 9pt 0; orphans:2; widows:2; }
h1.major { font-size:17pt; font-weight:bold; color:#1f3c88; text-align:center; margin:0 0 16pt 0;
  letter-spacing:.5pt; padding-bottom:8pt; border-bottom:2.5pt solid #c8a24a; break-after:avoid; }
.sec { break-before:page; }
ol.nl, ul.bl { margin:0 0 9pt 0; padding-left:1.05cm; }
ol.nl li, ul.bl li { margin:0 0 5pt 0; line-height:1.5; }
ul.bl li { list-style:none; padding-left:14px; position:relative; }
ul.bl li:before { content:""; position:absolute; left:0; top:8px; width:7px; height:7px;
  background:#c8a24a; border-radius:2px; }
/* DAFTAR ISI / TABEL / GAMBAR */
.row { display:flex; align-items:baseline; text-decoration:none; color:#1c2536; margin:3pt 0; font-size:11.5pt; }
.row.bab { font-weight:bold; color:#1f3c88; margin-top:8pt; }
.row.sub { padding-left:0.9cm; font-size:11pt; }
.row .t { white-space:nowrap; }
.row .dots { flex:1 1 auto; border-bottom:1.5pt dotted #b9bfce; margin:0 5px; transform:translateY(-3px); }
.row .pg { text-decoration:none; color:#1f3c88; font-weight:600; }
.row .pg:after { content: target-counter(attr(href url), page); }
/* BAB divider */
.babwrap { break-before:page; }
.babhead { background:#1f3c88; color:#fff; border-radius:12px; padding:16pt 18pt; margin:0 0 16pt 0;
  break-after:avoid; }
.babhead .bno { font-size:12pt; letter-spacing:3pt; color:#c8a24a; font-weight:bold; }
.babhead .bttl { font-size:17pt; font-weight:bold; margin-top:4pt; line-height:1.2; }
h2.sub { font-size:13pt; font-weight:bold; color:#1f3c88; margin:13pt 0 6pt 0;
  padding-left:9pt; border-left:4pt solid #c8a24a; break-after:avoid; }
/* KOTAK */
.box { border:1pt solid #dfe3ee; border-left:5pt solid #1f3c88; background:#eef1fb;
  border-radius:8px; padding:9pt 13pt 5pt 13pt; margin:10pt 0 12pt 0; break-inside:avoid; }
.box .bx-ttl { font-weight:bold; font-size:12pt; margin:0 0 5pt 0; }
.box p { margin:0 0 6pt 0; }
/* TABEL */
.tbl-cap { font-weight:bold; font-size:11pt; color:#1f3c88; margin:10pt 0 4pt 0; break-after:avoid; }
table.data { width:100%; border-collapse:collapse; margin:0 0 4pt 0; font-size:10.5pt; break-inside:avoid; }
table.data th { background:#1f3c88; color:#fff; font-weight:bold; padding:6pt 7pt; text-align:left;
  border:0.75pt solid #1f3c88; line-height:1.3; }
table.data td { padding:5pt 7pt; border:0.75pt solid #cfd6e6; vertical-align:top; line-height:1.35; }
table.data tr:nth-child(even) td { background:#f1f4fb; }
.src { font-size:9.5pt; color:#5a6477; font-style:italic; margin:0 0 11pt 0; }
/* GAMBAR */
figure { margin:11pt 0; text-align:center; break-inside:avoid; }
figure img { width:100%; max-width:15cm; border:1pt solid #e3e7f0; border-radius:8px; }
figcaption { font-weight:bold; font-size:11pt; color:#1f3c88; margin-top:5pt; }
/* PUSTAKA */
.ref { padding-left:1.0cm; text-indent:-1.0cm; margin:0 0 8pt 0; font-size:11.5pt; }
.ref a { color:#1f3c88; text-decoration:none; word-break:break-all; }
/* MOTTO */
.motto { margin-top:14pt; padding:12pt 16pt; background:#eef1fb; border-left:5pt solid #c8a24a;
  border-radius:8px; font-style:italic; font-size:12.5pt; color:#1f3c88; text-align:center; }
.signoff { break-before:avoid; text-align:right; margin-top:14pt; line-height:1.5; }
"""

def r_blocks(blocks, sub_ids=None, bno=None):
    """render list blok -> html. sub_ids: dict utk simpan id subbab (TOC)."""
    out = []
    h2idx = [0]
    for blk in blocks:
        k = blk[0]
        if k == "p":
            out.append("<p>%s</p>" % esc(blk[1]))
        elif k == "h2":
            h2idx[0] += 1
            sid = "s_%s_%d" % (bno, h2idx[0]) if bno else "h_%d" % h2idx[0]
            if sub_ids is not None:
                sub_ids.append((sid, blk[1]))
            out.append('<h2 class=sub id="%s">%s</h2>' % (sid, esc(blk[1])))
        elif k == "nlist":
            out.append("<ol class=nl>" + "".join("<li>%s</li>" % esc(x) for x in blk[1]) + "</ol>")
        elif k == "blist":
            out.append("<ul class=bl>" + "".join("<li>%s</li>" % esc(x) for x in blk[1]) + "</ul>")
        elif k == "table":
            out.append(r_table(blk[1]))
        elif k == "fig":
            out.append(r_fig(blk[1]))
        elif k == "box":
            out.append(r_box(blk[1]))
    return "".join(out)

def r_table(d):
    tid = "tb_" + d["no"].replace(".", "_")
    h = ['<div class=tbl-cap id="%s">Tabel %s &nbsp;%s</div>' % (tid, esc(d["no"]), esc(d["judul"]))]
    h.append("<table class=data><thead><tr>" + "".join("<th>%s</th>" % esc(c) for c in d["head"]) + "</tr></thead><tbody>")
    for row in d["rows"]:
        h.append("<tr>" + "".join("<td>%s</td>" % esc(c) for c in row) + "</tr>")
    h.append("</tbody></table>")
    h.append('<div class=src>Sumber: %s</div>' % esc(d.get("sumber", "")))
    return "".join(h)

def r_fig(d):
    fid = "fg_" + d["no"].replace(".", "_")
    return ('<figure><img src="%s" alt="%s"><figcaption id="%s">Gambar %s &nbsp;%s</figcaption>'
            '<div class=src>Sumber: %s</div></figure>'
            ) % (img_uri(d["file"]), esc(d["judul"]), fid, esc(d["no"]), esc(d["judul"]), esc(d.get("sumber", "")))

def r_box(d):
    line, bg = BOXSTYLE[d["kind"]]
    label = BOXLABEL[d["kind"]]
    style = "border-left-color:%s;background:%s;" % (line, bg)
    ttl = '<div class=bx-ttl style="color:%s">%s</div>' % (line, esc(d["judul"]))
    body = r_blocks(d["body"])
    return '<div class=box style="%s">%s%s</div>' % (style, ttl, body)

def row(cls, title, hid):
    return ('<div class="row %s"><span class=t>%s</span><span class=dots></span>'
            '<a class=pg href="#%s"></a></div>') % (cls, esc(title), hid)

def build_content():
    p = ['<!DOCTYPE html><html lang=id><head><meta charset=utf-8><style>%s</style></head><body>' % CSS]

    # 1. KATA PENGANTAR
    p.append('<section class=sec id=kp><h1 class=major>KATA PENGANTAR</h1>')
    for t in K.KATA_PENGANTAR:
        p.append("<p>%s</p>" % esc(t))
    p.append('<p class=signoff>Jakarta, %s<br>Tim Penyusun,<br>%s</p>' % ("Juni 2026", esc(K.KELOMPOK)))
    p.append("</section>")

    # kumpulkan id subbab tiap bab dulu (perlu utk TOC) -> render bab ke string + simpan struktur
    bab_html = []
    bab_meta = []  # (babid, "BAB I", judul, [(sid,judul_sub)])
    tabel_list = []  # (tid, "Tabel x.x Judul")
    gambar_list = []
    for bab in K.BAB:
        bid = "bab_%s" % bab["no"]
        subs = []
        # scan tabel & gambar utk daftar
        for blk in bab["isi"]:
            if blk[0] == "table":
                tabel_list.append(("tb_" + blk[1]["no"].replace(".", "_"), "Tabel %s  %s" % (blk[1]["no"], blk[1]["judul"])))
            elif blk[0] == "fig":
                gambar_list.append(("fg_" + blk[1]["no"].replace(".", "_"), "Gambar %s  %s" % (blk[1]["no"], blk[1]["judul"])))
        body = r_blocks(bab["isi"], sub_ids=subs, bno=bab["no"])
        bab_meta.append((bid, "BAB %s" % bab["no"], bab["judul"], subs))
        bab_html.append('<section class=babwrap id="%s"><div class=babhead><div class=bno>BAB %s</div>'
                        '<div class=bttl>%s</div></div>%s</section>' % (bid, esc(bab["no"]), esc(bab["judul"]), body))

    # 2. DAFTAR ISI
    p.append('<section class=sec id=daftarisi><h1 class=major>DAFTAR ISI</h1>')
    p.append(row("", "Kata Pengantar", "kp"))
    p.append(row("", "Daftar Tabel", "dtab"))
    p.append(row("", "Daftar Gambar", "dgam"))
    p.append(row("", "Pendahuluan", "pend"))
    for bid, blabel, bjudul, subs in bab_meta:
        p.append(row("bab", "%s  %s" % (blabel, bjudul), bid))
        for sid, sjudul in subs:
            p.append(row("sub", sjudul, sid))
    p.append(row("bab", "Refleksi", "refleksi"))
    p.append(row("bab", "Evaluasi", "evaluasi"))
    p.append(row("bab", "Daftar Pustaka", "pustaka"))
    p.append(row("bab", "Penutup", "penutup"))
    p.append("</section>")

    # 3. DAFTAR TABEL
    p.append('<section class=sec id=dtab><h1 class=major>DAFTAR TABEL</h1>')
    for tid, label in tabel_list:
        p.append(row("", label, tid))
    p.append("</section>")
    # 4. DAFTAR GAMBAR
    p.append('<section class=sec id=dgam><h1 class=major>DAFTAR GAMBAR</h1>')
    for fid, label in gambar_list:
        p.append(row("", label, fid))
    p.append("</section>")

    # 5. PENDAHULUAN
    p.append('<section class=sec id=pend><h1 class=major>PENDAHULUAN</h1>')
    p.append(r_blocks(K.PENDAHULUAN))
    p.append("</section>")

    # 6. BAB I-III
    p.extend(bab_html)

    # 7. REFLEKSI
    R = K.REFLEKSI
    p.append('<section class=sec id=refleksi><h1 class=major>REFLEKSI</h1>')
    p.append("<p>%s</p>" % esc(R["intro"]))
    p.append("<ol class=nl>" + "".join("<li>%s</li>" % esc(q) for q in R["pertanyaan"]) + "</ol>")
    p.append('<div class=tbl-cap>%s</div>' % esc(R["tabel_judul"]))
    p.append("<p>%s</p>" % esc(R["tabel_intro"]))
    p.append("<table class=data><thead><tr>" + "".join("<th>%s</th>" % esc(c) for c in R["tabel"]["head"]) + "</tr></thead><tbody>")
    for rr in R["tabel"]["rows"]:
        p.append("<tr>" + "".join("<td>%s</td>" % (esc(c) if c else "&nbsp;") for c in rr) + "</tr>")
    p.append("</tbody></table></section>")

    # 8. EVALUASI
    E = K.EVALUASI
    p.append('<section class=sec id=evaluasi><h1 class=major>EVALUASI</h1>')
    p.append("<p>%s</p>" % esc(E["intro"]))
    p.append('<h2 class=sub>A. Pilihan Ganda</h2><p>Pilihlah satu jawaban yang paling tepat.</p><ol class=nl>')
    for q, opts, _ in E["pg"]:
        letters = "ABCD"
        op = "<br>".join("%s. %s" % (letters[i], esc(o)) for i, o in enumerate(opts))
        p.append("<li>%s<br>%s</li>" % (esc(q), op))
    p.append("</ol>")
    p.append('<h2 class=sub>B. Benar atau Salah</h2><p>Tentukan apakah pernyataan berikut benar (B) atau salah (S).</p><ol class=nl>')
    for s, _ in E["bs"]:
        p.append("<li>%s ( ... )</li>" % esc(s))
    p.append("</ol>")
    p.append('<h2 class=sub>C. Esai Singkat</h2><p>Jawablah dengan jelas dan ringkas dalam tiga sampai lima kalimat.</p><ol class=nl>')
    for q in E["esai"]:
        p.append("<li>%s</li>" % esc(q))
    p.append("</ol>")
    # Kunci
    pg_key = "  ".join("%d.%s" % (i + 1, "ABCD"[k]) for i, (_, _, k) in enumerate(E["pg"]))
    bs_key = "  ".join("%d.%s" % (i + 1, "B" if v else "S") for i, (_, v) in enumerate(E["bs"]))
    p.append('<div class=box style="border-left-color:#15a34a;background:#e9f7ee">'
             '<div class=bx-ttl style="color:#15a34a">Kunci Jawaban</div>'
             '<p><b>A. Pilihan Ganda:</b> %s</p><p><b>B. Benar/Salah:</b> %s</p><p><b>C. Esai:</b> %s</p></div>'
             % (esc(pg_key), esc(bs_key), esc(E["pedoman_esai"])))
    p.append("</section>")

    # 9. DAFTAR PUSTAKA
    p.append('<section class=sec id=pustaka><h1 class=major>DAFTAR PUSTAKA</h1>')
    for pre, judul, post, url in K.DAFTAR_PUSTAKA:
        p.append('<div class=ref>%s<i>%s</i>%s <a href="%s">%s</a></div>'
                 % (esc(pre), esc(judul), esc(post), esc(url), esc(url)))
    p.append("</section>")

    # 10. PENUTUP
    p.append('<section class=sec id=penutup><h1 class=major>PENUTUP</h1>')
    for t in K.PENUTUP:
        p.append("<p>%s</p>" % esc(t))
    p.append('<div class=motto>%s</div>' % esc(K.MOTTO))
    p.append('<p class=signoff>Jakarta, Juni 2026<br>Tim Penyusun, %s</p>' % esc(K.KELOMPOK))
    p.append("</section>")

    p.append("</body></html>")
    return "".join(p)

# --------------------------- COVER ---------------------------
COVER_CSS = """
@page { size:A4; margin:0; }
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Caladea','Liberation Serif',serif; }
.page { width:21cm; height:29.7cm; position:relative; background:#ffffff; }
.top { position:absolute; top:0; left:0; right:0; height:9.2cm;
  background:linear-gradient(135deg,#1f3c88 0%,#2a4ba0 60%,#0e7490 100%); color:#fff; }
.top .tag { position:absolute; top:1.3cm; left:0; right:0; text-align:center; font-size:12.5pt; letter-spacing:3pt; color:#cdd6f4; }
.top .mk { position:absolute; top:2.2cm; left:0; right:0; text-align:center; font-size:12pt; color:#e7ecfb; }
.top .big { position:absolute; top:3.7cm; left:1.5cm; right:1.5cm; text-align:center; font-size:40pt; font-weight:bold; letter-spacing:1pt; }
.top .sub { position:absolute; top:6.6cm; left:2cm; right:2cm; text-align:center; font-size:15pt; color:#f1cf7a; }
.band { position:absolute; top:9.2cm; left:0; right:0; height:0.32cm; background:#c8a24a; }
.cards { position:absolute; top:10.6cm; left:2.2cm; right:2.2cm; display:flex; gap:0.5cm; }
.vc { flex:1; border-radius:12px; color:#fff; padding:12pt 8pt; text-align:center; }
.vc .lt { font-size:24pt; font-weight:bold; }
.vc .nm { font-size:11.5pt; margin-top:3pt; }
.author { position:absolute; top:16.0cm; left:2.5cm; right:2.5cm; text-align:center; }
.author .lbl { font-size:12pt; color:#1f3c88; letter-spacing:2pt; font-weight:bold; }
.author .nm { font-size:13.5pt; margin-top:6pt; color:#1c2536; line-height:1.7; }
.foot { position:absolute; bottom:1.6cm; left:2cm; right:2cm; text-align:center; color:#1c2536; line-height:1.55; }
.foot .org { font-size:13pt; font-weight:bold; color:#1f3c88; }
.foot .yr { font-size:13pt; font-weight:bold; margin-top:4pt; }
.frame { position:absolute; bottom:1.0cm; left:1.0cm; right:1.0cm; top:1.0cm; border:2pt solid #1f3c88; border-radius:6px; pointer-events:none; }
"""

def build_cover():
    tim = "".join('<div class=nm>%s (%s)</div>' % (esc(n), esc(npm)) for n, npm in K.TIM)
    return ("""<!DOCTYPE html><html><head><meta charset=utf-8><style>%s</style></head><body><div class=page>
    <div class=top>
      <div class=tag>MODUL BELAJAR</div>
      <div class=mk>%s</div>
      <div class=big>%s</div>
      <div class=sub>%s</div>
    </div>
    <div class=band></div>
    <div class=cards>
      <div class=vc style="background:#2563eb"><div class=lt>V</div><div class=nm>Visual</div></div>
      <div class=vc style="background:#ea7317"><div class=lt>A</div><div class=nm>Auditorial</div></div>
      <div class=vc style="background:#15a34a"><div class=lt>K</div><div class=nm>Kinestetik</div></div>
    </div>
    <div class=author><div class=lbl>Disusun oleh Tim Penyusun</div>%s</div>
    <div class=foot><div class=org>%s</div><div class=org>%s</div><div class=org>%s</div><div class=yr>%s</div></div>
    <div class=frame></div>
    </div></body></html>""" % (COVER_CSS, esc(K.MATKUL), esc(K.JUDUL), esc(K.SUBJUDUL), tim,
                                esc(K.PRODI), esc(K.FAKULTAS), esc(K.KAMPUS), esc(K.TAHUN)))

def main():
    from weasyprint import HTML
    from pypdf import PdfReader, PdfWriter
    os.makedirs(OUT, exist_ok=True)
    doc = HTML(string=build_content()).render()
    isi = len(doc.pages)
    print("Halaman ISI:", isi)
    cbuf = BytesIO(); doc.write_pdf(cbuf); cbuf.seek(0)
    cover = BytesIO(); HTML(string=build_cover()).write_pdf(cover); cover.seek(0)
    w = PdfWriter()
    for pg in PdfReader(cover).pages: w.add_page(pg)
    for pg in PdfReader(cbuf).pages: w.add_page(pg)
    with open(OUTPDF, "wb") as f: w.write(f)
    print("TOTAL (dgn cover):", isi + 1)
    print("SAVED:", OUTPDF, os.path.getsize(OUTPDF), "bytes")

if __name__ == "__main__":
    main()
