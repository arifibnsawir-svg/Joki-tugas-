# Scan posisi heading di PDF final Naila -> page_real.json untuk DOCX manual TOC.
import re, json
from pypdf import PdfReader
import sys
sys.path.insert(0, "build_naila")
import konten

PDF = "Joki-tugas-/FINAL/Buku 2 - Naila - PKN - FINISH.pdf"
r = PdfReader(PDF)
n = len(r.pages)
pages = [(r.pages[i].extract_text() or "") for i in range(n)]

# cover = halaman 1 & terakhir (teks kosong)
print("total pdf pages:", n)
print("cover depan kosong:", len(pages[0].strip()) == 0, "| cover belakang kosong:", len(pages[-1].strip()) == 0)

# halaman daftar isi (untuk dilewati saat cari heading asli): cari halaman pertama yang memuat 'DAFTAR ISI'
di_pages = [i for i,t in enumerate(pages) if 'DAFTAR ISI' in t[:40].upper()]
toc_end = max(di_pages) if di_pages else 1

def content_no_of(target, start_after):
    # cari halaman pertama (content) > start_after yang memuat target
    for i in range(start_after+1, n-1):
        t = " ".join(pages[i].split())
        if target in t:
            return i  # content_no = pdf 0-based index (cover depan=0 => content1=index1)
    return None

page_real = {}
# kata pengantar (sebelum TOC)
for i in range(1, n-1):
    if 'KATA PENGANTAR' in pages[i][:40].upper():
        page_real['kp'] = i; break
# bab & subbab (setelah halaman TOC)
miss = []
for b in konten.BAB:
    bp = None
    for i in range(toc_end+1, n-1):
        t = " ".join(pages[i].split())
        if re.match(rf"BAB {b['no']}\b", t):
            bp = i; break
    page_real['bab'+b['no']] = bp
    if bp is None: miss.append('bab'+b['no'])
    # subbab
    k=0
    for blk in b['isi']:
        if blk[0]=='h2':
            k+=1
            cp = content_no_of(blk[1], toc_end)
            page_real[f"s{b['no']}_{k}"] = cp
            if cp is None: miss.append(f"s{b['no']}_{k} ({blk[1]})")
# daftar pustaka
for i in range(toc_end+1, n):
    if 'DAFTAR PUSTAKA' in pages[i][:40].upper():
        page_real['dp'] = i; break

# blank pages di isi
blank = [i+1 for i in range(1, n-1) if len(pages[i].strip()) < 5]
print("halaman kosong di isi:", blank if blank else "tidak ada")
print("heading tak ketemu:", miss if miss else "semua ketemu")
print("contoh: bab1=%s bab8=%s dp=%s" % (page_real.get('bab1'), page_real.get('bab8'), page_real.get('dp')))
json.dump(page_real, open("build_naila/page_real.json","w"), indent=2, ensure_ascii=False)

# tampilkan daftar isi tercetak (halaman2 TOC)
print("--- DAFTAR ISI tercetak (cuplikan) ---")
for i in di_pages:
    print(pages[i][:1500])
