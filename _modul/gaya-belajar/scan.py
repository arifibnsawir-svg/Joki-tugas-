# -*- coding: utf-8 -*-
"""Scan PDF final modul -> page_real.json (nomor halaman utk Daftar Isi/Tabel/Gambar versi DOCX).
Printed page = index PDF (cover idx0 tak bernomor, Kata Pengantar idx1 = halaman 1).
Pencocokan pakai metode TANPA-SPASI agar tahan artefak letter-spacing (mis. 'B A B I', 'V AK').
"""
import re, json, sys
from pypdf import PdfReader
sys.path.insert(0, "Joki-tugas-/_modul/gaya-belajar")
import konten as K

PDF = "Joki-tugas-/MODUL_FINAL/Modul Gaya Belajar - Kelompok 10 - BnP - FINAL.pdf"
OUT = "Joki-tugas-/_modul/gaya-belajar/page_real.json"

r = PdfReader(PDF)
n = len(r.pages)
pages = [(r.pages[i].extract_text() or "") for i in range(n)]
def ns(s): return re.sub(r"\s+", "", s).lower()
nspage = [ns(p) for p in pages]
nstop = [ns(" ".join(p.split())[:70]) for p in pages]

pr = {}

def head_start(label, start=1):
    key = ns(label)
    for i in range(start, n):
        if nstop[i].startswith(key):
            return i
    for i in range(start, n):
        if key in nspage[i]:
            return i
    return None

pr["kp"] = head_start("KATA PENGANTAR", 1)
pr["dtab"] = head_start("DAFTAR TABEL", 1)
pr["dgam"] = head_start("DAFTAR GAMBAR", 1)
pr["pend"] = head_start("PENDAHULUAN", 1)

# Bab: halaman pembuka diawali "BAB <no>" (nospace startswith, halaman bab sendiri muncul paling awal)
bab_start = {}
for bab in K.BAB:
    key = ns("BAB " + bab["no"])
    pg = next((i for i in range(1, n) if nstop[i].startswith(key)), None)
    bab_start[bab["no"]] = pg
    pr["bab_%s" % bab["no"]] = pg

first_bab = min([p for p in bab_start.values() if p], default=8)

pr["refleksi"] = head_start("REFLEKSI", first_bab)
pr["evaluasi"] = head_start("EVALUASI", first_bab)
pr["pustaka"] = head_start("DAFTAR PUSTAKA", first_bab)
pr["penutup"] = head_start("PENUTUP", first_bab)

def content_page(text, start):
    key = ns(text)
    for i in range(start, n):
        if key in nspage[i]:
            return i
    return None

miss = []
for bab in K.BAB:
    bstart = bab_start.get(bab["no"]) or first_bab
    k = 0
    for blk in bab["isi"]:
        if blk[0] == "h2":
            k += 1
            cp = content_page(blk[1], bstart)
            pr["s_%s_%d" % (bab["no"], k)] = cp
            if cp is None: miss.append("s_%s_%d(%s)" % (bab["no"], k, blk[1][:20]))
        elif blk[0] == "table":
            no = blk[1]["no"]
            cp = content_page("Tabel %s" % no, bstart)
            pr["tb_" + no.replace(".", "_")] = cp
            if cp is None: miss.append("tb_" + no)
        elif blk[0] == "fig":
            no = blk[1]["no"]
            cp = content_page("Gambar %s" % no, bstart)
            pr["fg_" + no.replace(".", "_")] = cp
            if cp is None: miss.append("fg_" + no)

blank = [i for i in range(1, n) if len(pages[i].strip()) < 5]
print("total pages:", n)
print("kp=%s dtab=%s dgam=%s pend=%s" % (pr["kp"], pr["dtab"], pr["dgam"], pr["pend"]))
print("bab:", {b["no"]: pr["bab_%s" % b["no"]] for b in K.BAB})
print("refleksi=%s evaluasi=%s pustaka=%s penutup=%s" % (pr["refleksi"], pr["evaluasi"], pr["pustaka"], pr["penutup"]))
print("halaman kosong:", blank if blank else "tidak ada")
print("heading tak ketemu:", miss if miss else "semua ketemu")
json.dump(pr, open(OUT, "w"), indent=2, ensure_ascii=False)
print("SAVED:", OUT)
