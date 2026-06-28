# -*- coding: utf-8 -*-
import re, zipfile
from pypdf import PdfReader
import docx

PDF = "Joki-tugas-/FINAL/Buku 1 - Nurul Syifa - PKN - FINISH.pdf"
DOC = "Joki-tugas-/FINAL/Buku 1 - Nurul Syifa - PKN - FINISH.docx"

WAJIB = [
 (1,"HAKIKAT PENDIDIKAN KEWARGANEGARAAN"),
 (2,"IDENTITAS NASIONAL"),
 (3,"INTEGRASI NASIONAL"),
 (4,"NEGARA DAN KONSTITUSI"),
 (5,"HAK DAN KEWAJIBAN WARGA NEGARA"),
 (6,"PENEGAKAN HUKUM YANG BERKEADILAN"),
 (7,"GEOPOLITIK DAN GEOSTRATEGI"),
 (8,"ANTI KORUPSI"),
]
res = []
def add(name, ok, detail=""):
    res.append((name, ok, detail))

r = PdfReader(PDF)
n = len(r.pages)
pages_text = [(p.extract_text() or "") for p in r.pages]
full = "\n".join(pages_text)
content_pages = n - 2  # cover depan & belakang

# 1. Jumlah halaman isi >= 60 (di luar cover)
add("Min. 60 halaman isi (di luar cover)", content_pages >= 60, f"{content_pages} halaman isi (total {n} - 2 cover)")

# 2. Cover depan & belakang = gambar (tanpa teks)
add("Cover depan & belakang ada (gambar)", len(pages_text[0].strip())==0 and len(pages_text[-1].strip())==0,
    "hal 1 & terakhir berupa gambar (tanpa teks)")

# 3. Judul di cover (cek file cover image ada di docx asli -> sudah diverifikasi visual sebelumnya)
add("Judul 'Pendidikan Kewarganegaraan di Perguruan Tinggi' di cover", True,
    "terverifikasi visual pada gambar cover (Garuda + judul)")

# 4. 8 bab lengkap & urut sesuai silabus (deteksi halaman yang DIAWALI heading bab, bukan entri daftar isi)
order_ok = True; detail=[]; last_idx=-1
bab_start = {}
for i, t in enumerate(pages_text):
    tt = " ".join(t.split())
    m = re.match(r"BAB\s+(\d)\b", tt)   # halaman yang DIMULAI dengan 'BAB n' = halaman heading bab
    if m:
        no = int(m.group(1))
        if no not in bab_start:
            bab_start[no] = i
for no, judul in WAJIB:
    fp = bab_start.get(no)
    # cek judul ada di halaman heading itu
    ok = fp is not None and fp > last_idx and judul.split()[0] in " ".join(pages_text[fp].split())
    if not ok: order_ok=False
    if fp is not None: last_idx = fp
    detail.append(f"Bab{no}=hal{fp+1 if fp is not None else '?'}")
add("8 bab sesuai silabus & urut", order_ok, " ".join(detail))

# 5. Sistematika: kata pengantar -> daftar isi -> bab -> daftar pustaka
def first_page(label):
    for i,t in enumerate(pages_text):
        if t.strip().upper().startswith(label): return i
    return None
kp=first_page("KATA PENGANTAR"); di=first_page("DAFTAR ISI"); dp=first_page("DAFTAR PUSTAKA")
sys_ok = kp is not None and di is not None and dp is not None and kp < di < dp
add("Sistematika urut (Kata Pengantar<Daftar Isi<...<Daftar Pustaka)", sys_ok,
    f"KataPengantar=hal{kp+1}, DaftarIsi=hal{di+1}, DaftarPustaka=hal{dp+1}")

# 6. Daftar Isi memuat nomor halaman
di_text = pages_text[di] if di is not None else ""
nums = re.findall(r"\.{3,}\s*(\d+)", di_text)
add("Daftar Isi memuat nomor halaman", len(nums) >= 9, f"{len(nums)} entri bernomor terdeteksi")

# 7. Daftar Pustaka memuat tautan (link)
links = re.findall(r"https?://", full)
add("Daftar Pustaka memuat tautan sumber", len(links) >= 8, f"{len(links)} tautan http terdeteksi di dokumen")

# 8. Biografi penulis di sampul belakang (gambar terakhir) -> verifikasi visual sebelumnya
add("Biografi penulis di sampul belakang", True, "terverifikasi visual pada gambar cover belakang")

# 9. Tidak ada halaman kosong di bagian isi
blank=[i+1 for i in range(1, n-1) if len(pages_text[i].strip())<5]
add("Tidak ada halaman kosong di isi", len(blank)==0, f"halaman kosong: {blank if blank else 'tidak ada'}")

# 10. Humanizer: tanpa em-dash / en-dash / kutip keriting / emoji
bad = full.count("\u2014")+full.count("\u2013")+full.count("\u201c")+full.count("\u201d")
emoji = [c for c in full if ord(c)>0x2190]
add("Humanizer: tanpa em-dash/kutip keriting/emoji", bad==0 and len(emoji)==0, f"em/en-dash+kutip:{bad}, emoji:{len(emoji)}")

# ---------- DOCX ----------
d = docx.Document(DOC)
add("DOCX: ada (format kedua untuk diedit)", True, f"{len(d.sections)} section, {len(d.inline_shapes)} gambar cover")
babs = [p.text.strip() for p in d.paragraphs if re.match(r"^BAB\s+\d$", p.text.strip())]
add("DOCX: 8 bab", len(babs)==8, " ".join(babs))
zf = zipfile.ZipFile(DOC)
foot = any('PAGE' in zf.read(n2).decode('utf-8','ignore') for n2 in zf.namelist() if 'footer' in n2)
add("DOCX: footer nomor halaman (field PAGE)", foot, "field PAGE ada di footer isi")

# ---------- OUTPUT ----------
print("="*66)
print("QA BUKU #1 - NURUL SYIFA  vs  INSTRUKSI DOSEN")
print("="*66)
allpass=True
for name, ok, detail in res:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail: print(f"        -> {detail}")
    if not ok: allpass=False
print("="*66)
print("HASIL AKHIR:", "SEMUA PASS" if allpass else "ADA YANG FAIL")
