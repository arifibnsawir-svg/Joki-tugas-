# -*- coding: utf-8 -*-
# Scan posisi heading di PDF final Buku 6 (Revalina) -> page_real.json untuk DOCX manual TOC.
# Cover depan & belakang DIDESAIN (punya teks), jadi cek halaman kosong hanya untuk halaman ISI.
import re, json, sys
from pypdf import PdfReader
sys.path.insert(0, "Joki-tugas-/_generator/buku6")
import konten

PDF = "Joki-tugas-/FINAL/Buku 6 - Revalina Damayanti - PKN - FINISH.pdf"
OUT = "Joki-tugas-/_generator/buku6/page_real.json"
r = PdfReader(PDF)
n = len(r.pages)
pages = [(r.pages[i].extract_text() or "") for i in range(n)]
print("total pdf pages:", n)

def joined(i): return " ".join(pages[i].split())

page_real = {}
bab_pages = {}
for b in konten.BAB:
    # paragraf pertama tiap bab unik & hanya ada di ISI (tak muncul di Daftar Isi)
    first_p = next((blk[1] for blk in b['isi'] if blk[0] == 'p'), None)
    probe = " ".join(first_p.split())[:55] if first_p else None
    for i in range(1, n - 1):
        if probe and probe in joined(i):
            bab_pages[b['no']] = i
            break
    page_real['bab' + b['no']] = bab_pages.get(b['no'])

toc_end = min(bab_pages.values()) - 1 if bab_pages else 1
for i in range(1, n - 1):
    if 'KATA PENGANTAR' in pages[i][:40].upper():
        page_real['kp'] = i
        break

def content_no_of(target, start_after):
    for i in range(start_after + 1, n - 1):
        if target in joined(i):
            return i
    return None

miss = []
for b in konten.BAB:
    if page_real.get('bab' + b['no']) is None:
        miss.append('bab' + b['no'])
    k = 0
    for blk in b['isi']:
        if blk[0] == 'h2':
            k += 1
            cp = content_no_of(blk[1], toc_end)
            page_real["s%s_%d" % (b['no'], k)] = cp
            if cp is None:
                miss.append("s%s_%d (%s)" % (b['no'], k, blk[1]))
for i in range(toc_end + 1, n):
    if pages[i].strip().upper().startswith('DAFTAR PUSTAKA'):
        page_real['dp'] = i
        break

# halaman kosong hanya di rentang ISI (1 .. n-2), cover di 0 dan n-1 memang berisi desain
blank = [i + 1 for i in range(1, n - 1) if len(pages[i].strip()) < 5]
print("cover depan teks ada:", len(pages[0].strip()) > 0, "| cover belakang teks ada:", len(pages[-1].strip()) > 0)
print("toc_end:", toc_end, "| halaman kosong isi:", blank if blank else "tidak ada")
print("heading tak ketemu:", miss if miss else "semua ketemu")
print("kp=%s bab1=%s bab8=%s dp=%s" % (page_real.get('kp'), page_real.get('bab1'), page_real.get('bab8'), page_real.get('dp')))
json.dump(page_real, open(OUT, "w"), indent=2, ensure_ascii=False)
print("SAVED:", OUT)
