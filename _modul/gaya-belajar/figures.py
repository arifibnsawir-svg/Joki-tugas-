# -*- coding: utf-8 -*-
"""Bikin 3 diagram/infografik ORIGINAL untuk modul (HTML/CSS -> PDF via WeasyPrint -> PNG via pymupdf).
Output: assets/fig_1_1.png, fig_2_1.png, fig_3_1.png. Tema warna ber-kode VAK.
"""
import os
from io import BytesIO
from weasyprint import HTML
import fitz

OUT = "Joki-tugas-/_modul/gaya-belajar/assets"
V = "#2563eb"; A = "#ea7317"; K = "#15a34a"; RW = "#7c3aed"
INDIGO = "#1f3c88"; TEAL = "#0e7490"; GOLD = "#c8a24a"
INK = "#1c2536"

BASE = """
@page { size: %(w)scm %(h)scm; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Caladea','Liberation Serif',serif; color: %(ink)s; background: #ffffff; }
.wrap { width: %(w)scm; height: %(h)scm; padding: 0.5cm; display: flex; flex-direction: column; }
""" % {"w": "%(w)s", "h": "%(h)s", "ink": INK}  # placeholder, diisi per figur


def render(html_body, css_extra, w_cm, h_cm, outfile, dpi=200):
    page = "@page { size: %scm %scm; margin: 0; }" % (w_cm, h_cm)
    base = ("* {box-sizing:border-box;margin:0;padding:0;}"
            "body{font-family:'Caladea','Liberation Serif',serif;color:%s;background:#fff;}"
            ".wrap{width:%scm;height:%scm;padding:0.45cm;}" % (INK, w_cm, h_cm))
    doc = ("<!DOCTYPE html><html><head><meta charset=utf-8><style>%s %s %s</style></head>"
           "<body><div class=wrap>%s</div></body></html>" % (page, base, css_extra, html_body))
    pdf = BytesIO(); HTML(string=doc).write_pdf(pdf); pdf.seek(0)
    d = fitz.open("pdf", pdf.read())
    pix = d[0].get_pixmap(matrix=fitz.Matrix(dpi/72, dpi/72), alpha=False)
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, outfile)
    pix.save(path)
    print("SAVED", path, pix.width, "x", pix.height)


# ---------------- Gambar 1.1 : Skema Proses Belajar ----------------
def fig_1_1():
    css = """
    .flow{display:flex;align-items:stretch;height:100%%;gap:0;}
    .stage{flex:1;border-radius:12px;color:#fff;padding:12px;display:flex;align-items:center;
      justify-content:center;text-align:center;box-shadow:0 2px 4px rgba(0,0,0,.12);}
    .stage .inner{width:100%%;}
    .stage .t{font-weight:700;font-size:12.5pt;line-height:1.25;}
    .stage .s{font-size:9.5pt;margin-top:6px;opacity:.95;line-height:1.25;}
    .arrow{align-self:center;width:0;height:0;border-top:13px solid transparent;
      border-bottom:13px solid transparent;border-left:18px solid %(gold)s;margin:0 5px;}
    .chips{display:flex;gap:5px;justify-content:center;margin-top:7px;}
    .chip{width:24px;height:24px;border-radius:50%%;color:#fff;font-weight:700;font-size:10.5pt;
      display:flex;align-items:center;justify-content:center;border:2px solid rgba(255,255,255,.85);}
    """ % {"gold": GOLD}
    body = """
    <div class=flow>
      <div class=stage style="background:%(teal)s"><div class=inner><div class=t>Stimulus dan Informasi</div><div class=s>datang dari lingkungan belajar</div></div></div>
      <div class=arrow></div>
      <div class=stage style="background:%(indigo)s"><div class=inner><div class=t>Diterima oleh Indra</div><div class=s>penglihatan, pendengaran, gerak</div></div></div>
      <div class=arrow></div>
      <div class=stage style="background:#3b4cb8"><div class=inner><div class=t>Diproses sesuai Gaya Belajar</div>
        <div class=chips><span class=chip style="background:%(V)s">V</span><span class=chip style="background:%(A)s">A</span><span class=chip style="background:%(K)s">K</span></div></div></div>
      <div class=arrow></div>
      <div class=stage style="background:%(K)s"><div class=inner><div class=t>Tersimpan jadi Pengetahuan</div><div class=s>di memori jangka panjang</div></div></div>
    </div>
    """ % {"teal": TEAL, "indigo": INDIGO, "V": V, "A": A, "K": K}
    render(body, css, 19, 5.4, "fig_1_1.png")


# ---------------- Gambar 2.1 : Ilustrasi Tiga Tipe VAK ----------------
def card(letter, color, title, subtitle, items):
    lis = "".join("<li>%s</li>" % it for it in items)
    return ("""<div class=card>
      <div class=head style="background:%(c)s">
        <div class=badge>%(L)s</div><div class=ht><div class=hn>%(title)s</div><div class=hs>%(sub)s</div></div>
      </div>
      <ul class=body>%(lis)s</ul>
    </div>""" % {"c": color, "L": letter, "title": title, "sub": subtitle, "lis": lis})

def fig_2_1():
    css = """
    .cards{display:flex;gap:0.5cm;align-items:flex-start;}
    .card{flex:1;border:1.5px solid #e3e7f0;border-radius:14px;
      box-shadow:0 2px 5px rgba(0,0,0,.10);background:#fff;}
    .head{display:flex;align-items:center;gap:10px;padding:12px 12px;color:#fff;border-radius:13px 13px 0 0;}
    .badge{width:42px;height:42px;border-radius:50%%;background:rgba(255,255,255,.22);
      border:2px solid rgba(255,255,255,.9);display:flex;align-items:center;justify-content:center;
      font-weight:700;font-size:19pt;flex:none;}
    .hn{font-weight:700;font-size:14pt;line-height:1;}
    .hs{font-size:9.5pt;margin-top:3px;opacity:.95;}
    .body{list-style:none;padding:12px 14px;margin:0;}
    .body li{font-size:10.5pt;line-height:1.5;padding-left:16px;position:relative;margin-bottom:5px;}
    .body li:before{content:"";position:absolute;left:0;top:7px;width:7px;height:7px;border-radius:50%%;background:#9aa3b8;}
    """
    body = "<div class=cards>%s%s%s</div>" % (
        card("V", V, "Visual", "Belajar lewat penglihatan",
             ["Suka gambar, diagram, dan warna", "Mudah mengingat wajah dan peta", "Cocok dengan video dan infografis"]),
        card("A", A, "Auditorial", "Belajar lewat suara",
             ["Suka berdiskusi dan bertanya", "Mudah mengingat penjelasan lisan", "Cocok dengan podcast dan rekaman"]),
        card("K", K, "Kinestetik", "Belajar lewat gerakan",
             ["Suka praktik dan mencoba langsung", "Sulit duduk diam terlalu lama", "Cocok dengan simulasi dan alat peraga"]),
    )
    render(body, css, 18, 7.2, "fig_2_1.png")


# ---------------- Gambar 3.1 : Diagram Pemilihan Strategi Belajar ----------------
def col(letter, color, title, items):
    lis = "".join("<li>%s</li>" % it for it in items)
    return ("""<div class=col>
      <div class=ch style="background:%(c)s"><span class=cb>%(L)s</span> %(title)s</div>
      <ul class=cl>%(lis)s</ul>
    </div>""" % {"c": color, "L": letter, "title": title, "lis": lis})

def fig_3_1():
    css = """
    .top{background:%(indigo)s;color:#fff;border-radius:12px;text-align:center;padding:12px;
      font-weight:700;font-size:13pt;}
    .down{align-self:center;width:0;height:0;border-left:13px solid transparent;border-right:13px solid transparent;
      border-top:16px solid %(gold)s;margin:8px auto;}
    .cols{display:flex;gap:0.5cm;align-items:flex-start;}
    .col{flex:1;border:1.5px solid #e3e7f0;border-radius:12px;background:#fff;
      box-shadow:0 2px 5px rgba(0,0,0,.10);}
    .ch{color:#fff;font-weight:700;font-size:12.5pt;padding:10px 12px;display:flex;align-items:center;gap:9px;border-radius:11px 11px 0 0;}
    .cb{width:28px;height:28px;border-radius:50%%;background:rgba(255,255,255,.22);
      border:2px solid rgba(255,255,255,.9);display:inline-flex;align-items:center;justify-content:center;font-size:13pt;}
    .cl{list-style:none;margin:0;padding:11px 14px;}
    .cl li{font-size:10.5pt;line-height:1.5;padding-left:16px;position:relative;margin-bottom:6px;}
    .cl li:before{content:"";position:absolute;left:0;top:7px;width:7px;height:7px;border-radius:2px;background:%(gold)s;}
    .lead{display:flex;flex-direction:column;}
    """ % {"indigo": INDIGO, "gold": GOLD}
    body = """
    <div class=lead>
      <div class=top>Kenali gaya belajar dominan Anda</div>
      <div class=down></div>
      <div class=cols>%s%s%s</div>
    </div>
    """ % (
        col("V", V, "Visual", ["Buat peta pikiran berwarna", "Ubah materi jadi diagram", "Manfaatkan video belajar"]),
        col("A", A, "Auditorial", ["Rekam dan dengar ulang", "Aktif berdiskusi", "Jelaskan ulang ke teman"]),
        col("K", K, "Kinestetik", ["Lakukan praktik langsung", "Gunakan simulasi", "Belajar sambil bergerak"]),
    )
    render(body, css, 18, 7.2, "fig_3_1.png")


# ---------------- Gambar 1.2 : Faktor yang Memengaruhi Gaya Belajar ----------------
def fig_1_2():
    css = """
    .pills{display:flex;gap:0.4cm;align-items:flex-start;}
    .pill{flex:1;border-radius:12px;color:#fff;padding:12px 10px;text-align:center;
      box-shadow:0 2px 4px rgba(0,0,0,.12);}
    .pill .num{width:30px;height:30px;border-radius:50%%;background:rgba(255,255,255,.25);
      border:2px solid rgba(255,255,255,.9);margin:0 auto 7px auto;font-weight:700;font-size:13pt;
      line-height:26px;}
    .pill .lb{font-weight:700;font-size:11pt;line-height:1.25;}
    """
    cols = [INDIGO, "#2563eb", "#0e7490", "#15a34a", "#ea7317"]
    labels = ["Biologis dan Genetik", "Lingkungan", "Pengalaman Belajar", "Sosial Budaya", "Motivasi dan Kepribadian"]
    pills = "".join('<div class=pill style="background:%s"><div class=num>%d</div><div class=lb>%s</div></div>'
                    % (cols[i], i + 1, labels[i]) for i in range(5))
    render("<div class=pills>%s</div>" % pills, css, 18, 4.0, "fig_1_2.png")


# ---------------- Gambar 2.2 : Empat Modalitas VARK ----------------
def fig_2_2():
    css = """
    .vark{display:flex;gap:0.5cm;align-items:flex-start;}
    .vk{flex:1;border-radius:12px;color:#fff;padding:14px 10px;text-align:center;
      box-shadow:0 2px 4px rgba(0,0,0,.12);}
    .vk .lt{font-size:26pt;font-weight:700;line-height:1;}
    .vk .nm{font-size:12pt;font-weight:700;margin-top:6px;}
    .vk .ds{font-size:9.5pt;margin-top:3px;opacity:.95;}
    """
    data = [("V", V, "Visual", "Melihat"), ("A", A, "Auditorial", "Mendengar"),
            ("R", RW, "Read/Write", "Membaca-Menulis"), ("K", K, "Kinestetik", "Bergerak")]
    cards = "".join('<div class=vk style="background:%s"><div class=lt>%s</div><div class=nm>%s</div><div class=ds>%s</div></div>'
                    % (c, l, nm, ds) for l, c, nm, ds in data)
    render("<div class=vark>%s</div>" % cards, css, 18, 4.2, "fig_2_2.png")


# ---------------- Gambar 3.2 : Siklus Membangun Kebiasaan Belajar ----------------
def fig_3_2():
    css = """
    .flow{display:flex;align-items:stretch;gap:0;}
    .st{flex:1;border-radius:12px;color:#fff;padding:11px 9px;text-align:center;
      display:flex;align-items:center;justify-content:center;box-shadow:0 2px 4px rgba(0,0,0,.12);}
    .st .in{width:100%%;font-weight:700;font-size:10.5pt;line-height:1.25;}
    .ar{align-self:center;width:0;height:0;border-top:11px solid transparent;border-bottom:11px solid transparent;
      border-left:15px solid %(gold)s;margin:0 4px;}
    """ % {"gold": GOLD}
    steps = [("Mulai dari target kecil", INDIGO), ("Kaitkan dengan rutinitas", "#2563eb"),
             ("Beri penghargaan kecil", "#0e7490"), ("Catat kemajuan", "#15a34a"), ("Jaga konsistensi", "#ea7317")]
    parts = []
    for i, (t, c) in enumerate(steps):
        parts.append('<div class=st style="background:%s"><div class=in>%s</div></div>' % (c, t))
        if i < len(steps) - 1:
            parts.append('<div class=ar></div>')
    render("<div class=flow>%s</div>" % "".join(parts), css, 19, 3.6, "fig_3_2.png")


if __name__ == "__main__":
    fig_1_1()
    fig_1_2()
    fig_2_1()
    fig_2_2()
    fig_3_1()
    fig_3_2()
    print("Selesai membuat 6 gambar.")
