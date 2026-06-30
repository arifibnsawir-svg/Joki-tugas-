# -*- coding: utf-8 -*-
# Scan posisi heading di PDF final Balqis -> page_real.json untuk DOCX manual TOC.
# Sekaligus deteksi halaman kosong & verifikasi heading.
import re, json, sys
from pypdf import PdfReader
sys.path.insert(0, "Joki-tugas-/_generator/buku3")
import konten

PDF = "Joki-tugas-/FINAL/Buku 3 - Balqis Sandra Lejla - PKN - FINISH.pdf"
OUT = "Joki-tugas-/_generator/buku3/build_balqis/page_real.json"
r = PdfReader(PDF)
n = len(r.pages)
pages = [(r.pages[i].extract_text() or "") for i in range(n)]

print("total pdf pages:", n)
print("cover depan kosong:", len(pages[0].strip()) == 0, "| cover belakang kosong:", len(pages[-1].strip()) == 0)

di_pages = [i for i, t in enumerate(pages) if 'DAFTAR ISI' in t[:40].upper()]
toc_end = max(di_pages) if di_pages else 1

def content_no_of(target, start_after):
    for i in range(start_after + 1, n - 1):
        t = " ".join(pages[i].split())
        if target in t:
            return i
    return None

page_real = {}
for i in range(1, n - 1):
    if 'KATA PENGANTAR' in pages[i][:40].upper():
        page_real['kp'] = i; break

miss = []
for b in konten.BAB:
    bp = None
    for i in range(toc_end + 1, n - 1):
        t = " ".join(pages[i].split())
        if re.match(rf"BAB {b['no']}\b", t):
            bp = i; break
    page_real['bab' + b['no']] = bp
    if bp is None: miss.append('bab' + b['no'])
    k = 0
    for blk in b['isi']:
        if blk[0] == 'h2':
            k += 1
            cp = content_no_of(blk[1], toc_end)
            page_real["s%s_%d" % (b['no'], k)] = cp
            if cp is None: miss.append("s%s_%d (%s)" % (b['no'], k, blk[1]))
for i in range(toc_end + 1, n):
    if 'DAFTAR PUSTAKA' in pages[i][:40].upper():
        page_real['dp'] = i; break

blank = [i + 1 for i in range(1, n - 1) if len(pages[i].strip()) < 5]
print("halaman kosong di isi:", blank if blank else "tidak ada")
print("heading tak ketemu:", miss if miss else "semua ketemu")
print("bab1=%s bab8=%s dp=%s kp=%s" % (page_real.get('bab1'), page_real.get('bab8'), page_real.get('dp'), page_real.get('kp')))
json.dump(page_real, open(OUT, "w"), indent=2, ensure_ascii=False)
print("SAVED:", OUT)
