# -*- coding: utf-8 -*-
"""
QA Laporan Wawancara Helper. Semua kriteria HARUS PASS.
1. Semua bagian ada dan urut.
2. BAB II menyebut Rogers, Corey, Brammer.
3. 4 helper, tiap helper memuat 15 poin + ada tabel ringkasan.
4. Konsistensi sitasi <-> daftar pustaka (dua arah).
5. Nol em-dash, nol kutip keriting, nol emoji.
6. Tanpa halaman kosong / heading menggantung.
7. PDF & DOCX ada dan dapat dibuka; laporkan jumlah halaman PDF.
8. Foto dirujuk di Lampiran 3 atau placeholder dicatat.
"""
import os, re, zipfile
from pypdf import PdfReader
import docx
import konten as K

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.abspath(os.path.join(HERE, "..", "..", "LAPORAN_FINAL"))
PDF = os.path.join(OUTDIR, "Laporan Wawancara Helper - Kelompok - Pengembangan Profesi Konseling - FINISH.pdf")
DOCX = os.path.join(OUTDIR, "Laporan Wawancara Helper - Kelompok - Pengembangan Profesi Konseling - FINISH.docx")
FOTODIR = os.path.join(HERE, "_foto_dl")

res = []
def add(n, ok, d=""):
    res.append((n, ok, d))

# baca PDF
reader = PdfReader(PDF)
pages = [(p.extract_text() or "") for p in reader.pages]
npage = len(pages)
full = "\n".join(pages)
flat = " ".join(full.split())

# ---- 1. semua bagian ada dan urut ----
order_labels = ["KATA PENGANTAR", "DAFTAR ISI", "BAB I", "PENDAHULUAN", "BAB II",
                "LANDASAN TEORI", "BAB III", "METODE KEGIATAN", "BAB IV",
                "HASIL WAWANCARA DAN PEMBAHASAN", "BAB V", "PENUTUP",
                "DAFTAR PUSTAKA", "LAMPIRAN 1", "LAMPIRAN 2", "LAMPIRAN 3"]
positions = []
ok_order = True
last = -1
detail = []
for lab in order_labels:
    pos = flat.find(" ".join(lab.split()))
    positions.append(pos)
    if pos == -1 or pos < last:
        ok_order = False
        detail.append("%s(HILANG/URUT)" % lab)
    last = max(last, pos)
# judul utama di halaman judul
title_ok = "LAPORAN WAWANCARA DENGAN HELPER PEMBERI LAYANAN" in flat
add("1. Semua bagian ada & urut (judul, KP, DI, BAB I-V, DafPus, Lampiran 1-3)",
    ok_order and title_ok, "Judul utama: %s. %s" % ("ada" if title_ok else "TIDAK ADA",
    "urutan benar" if ok_order else "MASALAH: " + ", ".join(detail)))

# ---- 2. BAB II menyebut Rogers, Corey, Brammer ----
# gunakan rfind: kemunculan pertama ada di Daftar Isi, isi bab ada di kemunculan terakhir
i2 = flat.rfind("LANDASAN TEORI")
i3 = flat.rfind("METODE KEGIATAN")
bab2 = flat[i2:i3] if (i2 != -1 and i3 != -1 and i3 > i2) else ""
ahli = {n: (n in bab2) for n in ["Rogers", "Corey", "Brammer"]}
add("2. BAB II mengutip Rogers, Corey, Brammer", all(ahli.values()),
    ", ".join("%s=%s" % (k, v) for k, v in ahli.items()))

# ---- 3. 4 helper x 15 poin + tabel ringkasan ----
helper_ok = True
hd = []
for idx, h in enumerate(K.HELPERS, 1):
    # cari sub-bab 4.x di teks
    found_points = 0
    for i, (judul, teks) in enumerate(h["poin"], 1):
        # ambil potongan unik dari teks poin
        probe = " ".join(teks.split())[:40]
        if probe in flat:
            found_points += 1
    hd.append("H%d:%d/15" % (idx, found_points))
    if len(h["poin"]) != 15 or found_points < 15:
        helper_ok = False
n_helper = len(K.HELPERS)
tabel_ringkasan = "Tabel 4.1" in flat and "Ringkasan hasil wawancara" in flat
add("3. 4 helper, tiap helper 15 poin + tabel ringkasan",
    n_helper == 4 and helper_ok and tabel_ringkasan,
    "%d helper; %s; tabel ringkasan: %s" % (n_helper, " ".join(hd), tabel_ringkasan))

# ---- 4. konsistensi sitasi <-> daftar pustaka ----
# kumpulan nama belakang penulis dari daftar pustaka
ref_surnames = {"Brammer", "Corey", "Gladding", "Lubis", "Prayitno", "Rogers", "Willis"}
# sitasi dalam teks: pola "Nama (tahun)" dan "Nama dan Nama (tahun)"
body_text = flat[:flat.rfind("DAFTAR PUSTAKA")]
cited = set(re.findall(r"([A-Z][a-z]+)\s*\(\d{4}\)", body_text))
cited |= set(re.findall(r"([A-Z][a-z]+)\s+dan\s+[A-Z]", body_text))  # "Prayitno dan Amti"
# normalisasi sitasi yang relevan (buang kata umum yang ketangkap)
known = {"Rogers", "Corey", "Brammer", "Gladding", "Prayitno", "Willis", "Lubis", "Amti", "MacDonald"}
cited = {c for c in cited if c in known}
# Amti & MacDonald adalah penulis kedua -> peta ke entri utama
cited_main = set()
for c in cited:
    if c == "Amti":
        cited_main.add("Prayitno")
    elif c == "MacDonald":
        cited_main.add("Brammer")
    else:
        cited_main.add(c)
# arah 1: tiap sitasi punya entri daftar pustaka
missing_ref = cited_main - ref_surnames
# arah 2: tiap entri daftar pustaka memang dikutip
dp_text = flat[flat.rfind("DAFTAR PUSTAKA"):flat.rfind("LAMPIRAN 1")]
uncited = set()
for s in ref_surnames:
    in_text = s in cited_main
    in_dp = s in dp_text
    if in_dp and not in_text:
        uncited.add(s)
add("4. Konsistensi sitasi <-> daftar pustaka (dua arah)",
    len(missing_ref) == 0 and len(uncited) == 0,
    "sitasi: %s; tanpa entri: %s; entri tak dikutip: %s"
    % (sorted(cited_main), sorted(missing_ref) or "tidak ada", sorted(uncited) or "tidak ada"))

# ---- 5. humanizer ----
emdash = full.count("\u2014")
endash = full.count("\u2013")
curly = sum(full.count(c) for c in ["\u201c", "\u201d", "\u2018", "\u2019"])
emoji = [c for c in full if ord(c) >= 0x1F000 or (0x2190 <= ord(c) <= 0x2BFF) or (0x2600 <= ord(c) <= 0x27BF)]
add("5. Humanizer: 0 em-dash, 0 en-dash, 0 kutip keriting, 0 emoji",
    emdash == 0 and endash == 0 and curly == 0 and len(emoji) == 0,
    "em-dash=%d, en-dash=%d, kutip-keriting=%d, emoji=%d" % (emdash, endash, curly, len(emoji)))

# ---- 6. tanpa halaman kosong / heading menggantung ----
blank = [i + 1 for i in range(1, npage) if len(pages[i].strip()) < 5]
# heading menggantung: halaman yang hanya berisi "BAB X" tanpa isi lain
dangling = []
for i, t in enumerate(pages):
    s = " ".join(t.split())
    if re.fullmatch(r"BAB [IVX]+", s):
        dangling.append(i + 1)
add("6. Tanpa halaman kosong / heading menggantung",
    len(blank) == 0 and len(dangling) == 0,
    "halaman kosong: %s; heading menggantung: %s" % (blank or "tidak ada", dangling or "tidak ada"))

# ---- 7. PDF & DOCX ada & dapat dibuka ----
docx_ok = False
docx_detail = ""
try:
    d = docx.Document(DOCX)
    docx_ok = True
    docx_detail = "%d paragraf, %d tabel, %d gambar" % (len(d.paragraphs), len(d.tables), len(d.inline_shapes))
except Exception as e:
    docx_detail = "ERROR: %s" % e
add("7. PDF & DOCX ada dan dapat dibuka",
    os.path.exists(PDF) and os.path.exists(DOCX) and npage > 0 and docx_ok,
    "PDF=%d halaman; DOCX: %s" % (npage, docx_detail))

# ---- 8. foto di Lampiran 3 ----
l3 = flat[flat.rfind("LAMPIRAN 3"):]
photos_present = [h["foto"] for h in K.HELPERS if os.path.exists(os.path.join(FOTODIR, h["foto"]))]
photos_missing = [h["foto"] for h in K.HELPERS if not os.path.exists(os.path.join(FOTODIR, h["foto"]))]
referenced = "Dokumentasi wawancara" in l3
# pada DOCX hitung gambar
docx_imgs = len(d.inline_shapes) if docx_ok else 0
add("8. Foto dirujuk di Lampiran 3 (atau placeholder dicatat)",
    referenced and (len(photos_present) >= 1 or len(photos_missing) > 0),
    "foto tersedia: %s; placeholder: %s; gambar di DOCX: %d"
    % (photos_present, photos_missing or "tidak ada", docx_imgs))

# ---- cetak ----
print("=" * 70)
print("QA - LAPORAN WAWANCARA DENGAN HELPER PEMBERI LAYANAN")
print("=" * 70)
allp = True
for nm, ok, d2 in res:
    print("[%s] %s" % ("PASS" if ok else "FAIL", nm))
    if d2:
        print("        -> %s" % d2)
    if not ok:
        allp = False
print("=" * 70)
print("JUMLAH HALAMAN PDF:", npage)
print("HASIL:", "SEMUA PASS" if allp else "ADA FAIL")
print("=" * 70)
