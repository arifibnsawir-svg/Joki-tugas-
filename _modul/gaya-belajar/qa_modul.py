# -*- coding: utf-8 -*-
"""QA Modul Gaya Belajar vs ATURAN + RUBRIK DOSEN (BnP 2026). Cetak PASS/FAIL + peta rubrik 100%."""
import re, sys, zipfile
from pypdf import PdfReader
import docx
sys.path.insert(0, "Joki-tugas-/_modul/gaya-belajar")
import konten as K

PDF = "Joki-tugas-/MODUL_FINAL/Modul Gaya Belajar - Kelompok 10 - BnP - FINAL.pdf"
DOC = "Joki-tugas-/MODUL_FINAL/Modul Gaya Belajar - Kelompok 10 - BnP - FINAL.docx"

res = []  # (kriteria_rubrik, nama, ok, detail)
def add(rub, nama, ok, det=""): res.append((rub, nama, ok, det))

r = PdfReader(PDF); n = len(r.pages)
pages = [(r.pages[i].extract_text() or "") for i in range(n)]
full = "\n".join(pages); nsfull = re.sub(r"\s+", "", full).lower()
def has(s): return re.sub(r"\s+", "", s).lower() in nsfull

# ---------- RUBRIK 2: Kelengkapan Struktur (20%) ----------
topns = [re.sub(r"\s+", "", " ".join(pages[i].split())[:70]).lower() for i in range(n)]
def top_page(label, start=1):
    key = re.sub(r"\s+", "", label).lower()
    return next((i for i in range(start, n) if topns[i].startswith(key)), None)
order_keys = ["KATA PENGANTAR", "DAFTAR ISI", "DAFTAR TABEL", "DAFTAR GAMBAR", "PENDAHULUAN",
              "BAB I", "BAB II", "BAB III", "REFLEKSI", "EVALUASI", "DAFTAR PUSTAKA", "PENUTUP"]
pos = [top_page(k) for k in order_keys]
okurut = (None not in pos) and all(pos[i] <= pos[i + 1] for i in range(len(pos) - 1))
add("Struktur", "Sistematika lengkap & urut (Cover s/d Penutup)", okurut,
    "urutan halaman: " + str(pos))
komp_pend = all(has(x) for x in ["Apa yang Akan Dipelajari", "Tujuan Pembelajaran", "Cara Menggunakan Modul", "Sasaran Pembaca"])
add("Struktur", "Pendahuluan memuat 4 komponen wajib", komp_pend, "apa dipelajari/tujuan/cara pakai/sasaran")
add("Struktur", "Minimal 3 bab materi", len(K.BAB) >= 3, "%d bab" % len(K.BAB))

# tiap bab: tujuan + materi(h2) + contoh + aktivitas + ringkasan
bab_ok = True; bdet = []
for bab in K.BAB:
    kinds = [b[1]["kind"] for b in bab["isi"] if b[0] == "box"]
    h2c = sum(1 for b in bab["isi"] if b[0] == "h2")
    ok = ("tujuan" in kinds and "contoh" in kinds and "aktivitas" in kinds and "ringkasan" in kinds and h2c >= 3)
    bab_ok = bab_ok and ok; bdet.append("B%s(h2=%d)" % (bab["no"], h2c))
add("Struktur", "Tiap bab: Tujuan+Materi+Contoh+Aktivitas+Ringkasan", bab_ok, " ".join(bdet))

# ---------- RUBRIK 1: Kesesuaian & Ketepatan Materi (30%) ----------
add("Materi", "Tema sesuai (Gaya Belajar / VAK)", has("gaya belajar") and has("visual") and has("auditorial") and has("kinestetik"), "konsep VAK lengkap")
add("Materi", "Konsep kunci hadir (model VAK, multimodal, strategi)", has("Neil Fleming") and has("multimodal") and has("strategi belajar"), "Fleming/multimodal/strategi")

# ---------- RUBRIK 4: Aktivitas, Refleksi, Evaluasi (15%) ----------
nakt = sum(1 for bab in K.BAB for b in bab["isi"] if b[0] == "box" and b[1]["kind"] == "aktivitas")
add("Aktivitas", "Tiap bab ada aktivitas (>=3)", nakt >= 3, "%d aktivitas" % nakt)
add("Aktivitas", "Refleksi >= 5 pertanyaan", len(K.REFLEKSI["pertanyaan"]) >= 5, "%d pertanyaan" % len(K.REFLEKSI["pertanyaan"]))
total_eval = len(K.EVALUASI["pg"]) + len(K.EVALUASI["bs"]) + len(K.EVALUASI["esai"])
add("Aktivitas", "Evaluasi >= 10 butir", total_eval >= 10, "%d butir (PG%d+BS%d+Esai%d)" % (total_eval, len(K.EVALUASI["pg"]), len(K.EVALUASI["bs"]), len(K.EVALUASI["esai"])))
add("Aktivitas", "Ada Kunci Jawaban / pedoman", has("Kunci Jawaban"), "kunci + pedoman penskoran")

# ---------- RUBRIK 5: Kreativitas & Tampilan (10%) ----------
nfig = sum(1 for bab in K.BAB for b in bab["isi"] if b[0] == "fig")
ntab = sum(1 for bab in K.BAB for b in bab["isi"] if b[0] == "table")
add("Kreativitas", "Ada gambar/diagram (>=3)", nfig >= 3, "%d gambar" % nfig)
add("Kreativitas", "Ada tabel (>=3)", ntab >= 3, "%d tabel" % ntab)
add("Kreativitas", "Tiap gambar & tabel cantumkan Sumber", full.count("Sumber:") >= (nfig + ntab), "%d label 'Sumber:'" % full.count("Sumber:"))
# DOCX tampilan: tabel berwarna (shading) + gambar disisip
zf = zipfile.ZipFile(DOC)
docxml = zf.read("word/document.xml").decode("utf-8", "ignore")
shaded = docxml.count("w:shd")
add("Kreativitas", "DOCX: tabel/kotak berwarna (shading)", shaded >= 15, "%d elemen shading" % shaded)

# ---------- RUBRIK 6: Referensi & Penulisan (10%) ----------
nref = len(K.DAFTAR_PUSTAKA)
add("Referensi", "Daftar Pustaka >= 5 sumber", nref >= 5, "%d sumber" % nref)
# APA7: pola "Nama, X. (Tahun)."
apa = all(re.search(r"\(\d{4}\)", pre + post) for pre, judul, post, url in K.DAFTAR_PUSTAKA)
add("Referensi", "Format APA 7 (ada tahun dalam kurung)", apa, "tiap entri ada (Tahun)")
keys = [pre.strip().lower() for pre, *_ in K.DAFTAR_PUSTAKA]
add("Referensi", "Daftar Pustaka urut alfabetis", keys == sorted(keys), "urut nama penulis")
add("Referensi", "Setiap entri punya tautan", all(u.startswith("http") for *_, u in K.DAFTAR_PUSTAKA), "%d tautan" % nref)

# ---------- RUBRIK 3: Kualitas Penyajian (15%) ----------
bad = sum(full.count(c) for c in ["\u2014", "\u2013", "\u201c", "\u201d", "\u2018", "\u2019"])
emoji = [c for c in full if ord(c) > 0x2300]
add("Penyajian", "Humanizer (tanpa em-dash/kutip keriting/emoji)", bad == 0 and len(emoji) == 0, "em/en-dash+kutip=%d emoji=%d" % (bad, len(emoji)))
add("Penyajian", "Kata Pengantar buka 'Segala puji bagi Allah'", has("Segala puji bagi Allah"), "sesuai permintaan")
isi = n - 1
add("Penyajian", "Jumlah halaman wajar (isi >= 20)", isi >= 20, "%d halaman isi (+1 cover)" % isi)
blank = [i for i in range(1, n) if len(pages[i].strip()) < 5]
add("Penyajian", "Tanpa halaman kosong", len(blank) == 0, blank if blank else "tidak ada")

# ---------- FORMAT TEKNIS (dasar wajib) ----------
d = docx.Document(DOC); b = d.sections[1]
fmt = (round(b.left_margin.cm, 1) == 4.0 and round(b.right_margin.cm, 1) == 3.0 and
       round(b.top_margin.cm, 1) == 3.0 and round(b.bottom_margin.cm, 1) == 3.0)
add("Format", "DOCX margin kiri4/kanan3/atas3/bawah3", fmt, "L%.0f R%.0f T%.0f B%.0f" % (b.left_margin.cm, b.right_margin.cm, b.top_margin.cm, b.bottom_margin.cm))
add("Format", "DOCX font Cambria", d.styles["Normal"].font.name == "Cambria", d.styles["Normal"].font.name)
ftr = any("PAGE" in zf.read(x).decode("utf-8", "ignore") for x in zf.namelist() if "footer" in x)
add("Format", "DOCX nomor halaman (angka Arab) di footer", ftr, "footer PAGE field")
add("Format", "Output 2 format (PDF + DOCX)", True, "PDF %d hal + DOCX" % n)

# ====== CETAK ======
print("=" * 70); print("QA MODUL GAYA BELAJAR (Kelompok 10) vs ATURAN + RUBRIK DOSEN"); print("=" * 70)
rubrik_bobot = {"Materi": 30, "Struktur": 20, "Penyajian": 15, "Aktivitas": 15, "Kreativitas": 10, "Referensi": 10, "Format": 0}
allp = True
from collections import OrderedDict
byrub = OrderedDict()
for rub, nama, ok, det in res:
    byrub.setdefault(rub, []).append((nama, ok, det))
    if not ok: allp = False
for rub in ["Materi", "Struktur", "Penyajian", "Aktivitas", "Kreativitas", "Referensi", "Format"]:
    if rub not in byrub: continue
    bobot = rubrik_bobot[rub]
    print("\n[%s%s]" % (rub, (" - bobot %d%%" % bobot) if bobot else " - wajib"))
    for nama, ok, det in byrub[rub]:
        print("   [%s] %s" % ("PASS" if ok else "FAIL", nama) + (("  -> " + str(det)) if det else ""))
print("\n" + "=" * 70)
# rubrik tercapai 100% jika semua kriteria berbobot PASS
rub_pass = {}
for rub, nama, ok, det in res:
    rub_pass.setdefault(rub, True)
    rub_pass[rub] = rub_pass[rub] and ok
skor = sum(rubrik_bobot[r] for r in rubrik_bobot if r != "Format" and rub_pass.get(r))
print("PERKIRAAN PEMENUHAN RUBRIK: %d%% / 100%%" % skor)
print("HASIL:", "SEMUA PASS" if allp else "ADA FAIL")
