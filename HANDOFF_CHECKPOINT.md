# HANDOFF / CHECKPOINT - Project Joki Mini Book PKN

Dokumen ini WAJIB dibaca lebih dulu oleh sesi/agen baru agar nyambung dengan pekerjaan sebelumnya dan TIDAK berhalusinasi. Semua aturan, pemetaan, pipeline teknis, dan progres tercatat di sini.

## 1. Gambaran Umum
- Tujuan: merevisi 5 mini book "Pendidikan Kewarganegaraan di Perguruan Tinggi" milik 5 mahasiswa agar sesuai silabus dosen, lalu hasilkan 2 format (PDF + DOCX) per buku.
- Repo: `arifibnsawir-svg/Joki-tugas-` (GitHub). PENTING: akun yang punya akses push lewat Kiro adalah `arifibnsawir-svg`, BUKAN `arifbudiman575-ship-it` (akun itu kena 403 saat push).
- Hasil jadi disimpan di folder `FINAL/` dengan nama berakhiran `FINISH` (PDF + DOCX). File mentah ada di `SUMBER_ASLI (jangan dikumpulkan)/`.

## 2. Aturan (lihat juga .kiro/steering/aturan-buku-pkn.md)
Aturan DOSEN (wajib PASS):
1. Judul: "PENDIDIKAN KEWARGANEGARAAN DI PERGURUAN TINGGI".
2. Minimal 60 halaman ISI DI LUAR cover depan & belakang.
3. 8 bab urut: (1) Hakikat PKn, (2) Identitas Nasional, (3) Integrasi Nasional, (4) Negara dan Konstitusi, (5) Hak dan Kewajiban Warga Negara, (6) Penegakan Hukum yang Berkeadilan, (7) Geopolitik dan Geostrategi, (8) Anti Korupsi.
   - JUDUL BAB HARUS PERSIS silabus. Contoh: Bab 5 = "HAK DAN KEWAJIBAN WARGA NEGARA" (HAM boleh jadi sub-bab di dalam, TAPI jangan masuk judul bab).
4. Sistematika: Cover -> Kata Pengantar -> Daftar Isi -> Bab 1-8 -> Daftar Pustaka -> Biografi penulis (sampul belakang).

Aturan PEMILIK PROJECT:
- Pakai skill humanizer (TANPA em-dash/en-dash, tanpa kutip keriting, tanpa emoji, hindari pola ala-AI & rule-of-three).
- Bab yang materinya SUDAH sesuai silabus: cukup di-humanize (pertahankan kedalaman). Bab yang TIDAK sesuai/tidak ada: tulis ulang.
- ATURAN BARU (terbaru): jika isi sudah sesuai aturan dosen, selain humanize BOLEH menambah konten sendiri (agar halaman cukup), ASAL sumber valid & kredibel dan link bisa dicek manual.
- Referensi: kredibel, ada tautan yang bisa dibuka manual. Verifikasi tiap link dulu (HTTP 200) sebelum dipakai.
- Dua format: PDF (versi final tampilan, dipakai dikumpulkan; identik di semua perangkat) + DOCX (editable).
- Daftar isi: nomor halaman MANUAL/tercetak (bukan TOC field yang harus di-update murid). Di PDF otomatis via target-counter; di DOCX diketik dari hasil scan PDF.
- TIDAK boleh ada halaman kosong / heading menggantung. (DOCX: pakai spasi ~1.5-1.6, keepLines, keep_with_next, tabel cantSplit + caption keep-with-next, widowControl. Hindari spasi dobel karena bikin gap besar di Word.)
- Cover depan + biografi belakang ASLI tiap penulis WAJIB dipertahankan. Kata pengantar Buku 2-5 boleh di-humanize.
- Tiap buku selesai: jalankan QA PASS/FAIL, semua HARUS PASS.

## 3. DNA pembeda tiap buku (WAJIB beda, anti-plagiat/Turnitin)
Yang SAMA antar buku hanya judul bab. Selebihnya WAJIB beda: kalimat, contoh, sudut bahas, DAN format/DNA.

| Buku | Penulis | Gaya tulisan | Posisi no. halaman | Elemen isi | Daftar Isi | Daftar Pustaka | Status |
|------|---------|--------------|--------------------|------------|------------|----------------|--------|
| 1 | Nurul Syifa | Naratif-reflektif | Tengah bawah | Prosa + refleksi | Dot leader rata (bab) | APA | SELESAI |
| 2 | Naila Diyana Nabilah | Akademik-terstruktur | Pojok kanan bawah | Tabel berwarna (header biru lembut) | Bertingkat (bab+subbab) | IEEE [n] | SELESAI |
| 3 | Balqis Sandra Lejla | Kontekstual-aplikatif | Pojok luar (kiri-kanan ganti) | Poin-poin/bullet + kotak studi kasus | Leader titik format beda | Harvard | BELUM |
| 4 | Lidya Ellen Febriasalsa | Dialogis/tanya-jawab | Tengah atas (header) | Kotak tanya-jawab + tabel ringkas | Tanpa leader, indentasi | MLA | BELUM |
| 5 | Nurjali Sangadji | KHUSUS: file asli 100% GAMBAR (62 gambar, 0 teks). Perlu dibangun ulang jadi teks. | ditentukan | ditentukan | ditentukan | ditentukan | BELUM |
| 6 | Revalina Damayanti | Tematik problem-solusi | Pojok kanan atas (header) | Kotak Akar Masalah + Langkah Solusi (maroon/emas) | Nomor rata kanan + garis tiap bab | Vancouver | SELESAI (PR buku6-revalina) |

Catatan: tabel/warna dibuat lembut & profesional. Tiap buku tetap WAJIB lolos QA penuh.

## 4. Pemetaan bab tiap penulis (humanize vs tulis ulang)
- Cek isi asli tiap file di `SUMBER_ASLI (jangan dikumpulkan)/`. Petakan ke 8 topik silabus. Yang cocok -> humanize + boleh tambah. Yang tak ada -> tulis baru.
- Buku 3 Balqis Lejla (file: "Mini Book Finish Balqis Lejla.docx"): bab aslinya Pendahuluan, Identitas, Konstitusi, Hak&Kewajiban, Demokrasi, Negara Hukum&Penegakan Hukum, Wawasan Nusantara&Ketahanan, Integrasi. TIDAK ada Anti Korupsi & Hakikat PKn -> Bab 1 (Hakikat) & Bab 8 (Anti Korupsi) tulis baru; sisanya petakan + humanize.
- Buku 4 Lidya (file: "Mini Book Teman Balqis.docx"): bab asli Hakikat, Pancasila, UUD, Negara/Bangsa/Konstitusi, Demokrasi, HAM, Wawasan Nusantara, Etika&Budaya Politik. Anti Korupsi belum berdiri sendiri -> tulis baru; Identitas/Integrasi/Penegakan Hukum perlu disusun dari materi terkait.
- Buku 5 Nurjali (file: "NURJALI_SANGADJI_FINAL_Mini Book V4.docx"): 100% gambar. Bab asli (dari kata pengantar): konsep PKn, Pancasila, UUD, HAM, Wawasan Nusantara, Bela Negara, Demokrasi, Otonomi Daerah. Hampir semua harus DITULIS ULANG agar sesuai 8 topik silabus. Cover & biografi tetap diambil dari gambar aslinya.

## 5. Referensi terverifikasi (HTTP 200) - pakai ini
- Wikisource Indonesia (teks lengkap UU), format: https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_X_Tahun_Y
  - Terverifikasi: UU 12/2012 (Pendidikan Tinggi), 20/2003 (Sisdiknas), 24/2009, 12/2006, 12/2011, 39/1999 (HAM), 3/2002 (Pertahanan), 2/2002 (Polri), 31/1999 & 20/2001 (Korupsi).
  - UUD 1945: https://id.wikisource.org/wiki/Undang-Undang_Dasar_Negara_Republik_Indonesia_Tahun_1945
- Wikimedia Commons PDF: UU 48/2009 (Kekuasaan Kehakiman) -> https://commons.wikimedia.org/wiki/File:Undang-Undang_Republik_Indonesia_Nomor_48_Tahun_2009.pdf
- KPK ACLC: https://aclc.kpk.go.id/ dan https://aclc.kpk.go.id/materi-pembelajaran
- UN UDHR: https://www.un.org/en/about-us/universal-declaration-of-human-rights
- CATATAN: situs gov peraturan.bpk.go.id, dpr.go.id, mkri.id MEMBLOKIR bot (HTTP 403) -> jangan andalkan, pakai Wikisource. Link bpk tetap hidup di browser bila perlu dicantumkan.

## 6. Pipeline teknis (PROVEN) - ada di folder `_generator/`
Lingkungan sandbox AL2023. LibreOffice TIDAK tersedia. Yang perlu di-install di sesi baru:
```
pip install -q weasyprint pypdf python-docx gdown
dnf install -y pango gdk-pixbuf2 google-noto-serif-fonts dejavu-serif-fonts liberation-serif-fonts liberation-sans-fonts
```
- Font: pakai Liberation Serif (metric-compatible dengan Times New Roman) di WeasyPrint; di DOCX set font "Times New Roman".
- File sumber 5 docx ada di repo folder `SUMBER_ASLI (jangan dikumpulkan)/`. (Bisa juga unduh ulang dari Google Drive folder milik user via gdown jika perlu.)

ALUR per buku (lihat contoh `_generator/buku2/`):
1. `konten.py`: berisi PENULIS, KATA_PENGANTAR (humanized), DAFTAR_PUSTAKA (format sesuai DNA), BAB = list 8 bab. Tiap blok: ('p',teks) | ('h2',teks) | ('table',{judul,head,rows}). Sub-bab dinomori X.Y otomatis lewat fungsi splice+renumber.
2. `gen_pdf.py` (WeasyPrint): RENDER ISI TANPA COVER dulu -> penomoran mulai 1 & TOC target-counter akurat. JANGAN pakai counter-reset/counter-set (merusak target-counter). Set `hyphens:none` agar pemenggalan baris match Word. Lalu MERGE cover depan+belakang (gambar asli, A4 penuh) via pypdf. Atur line-height supaya halaman ISI >= 60 (di luar 2 cover). Nomor halaman via @bottom-center / @bottom-right / @bottom-left sesuai DNA.
3. `scan.py`: scan PDF final -> page_real.json (nomor halaman tiap heading & subbab) untuk daftar isi MANUAL di DOCX. Sekaligus deteksi halaman kosong & verifikasi heading.
4. `build_docx.py` (python-docx): MIRROR layout PDF (A4, margin 3/3/2.5/3.5cm, Times New Roman 12, line spacing samakan dgn PDF ~1.5-1.6). Cover depan+belakang gambar (section margin 0, tanpa footer). Section isi: pgNumType start=1, footer PAGE field LENGKAP (begin/instrText ' PAGE '/separate/hasil/end) + settings updateFields=true, alignment footer sesuai DNA. Daftar isi MANUAL (tab stop kanan + dot leader) pakai nomor dari page_real.json. ANTI-GANTUNG: heading keep_with_next+keepLines+widowControl; tabel rows cantSplit + tblHeader + caption keep_with_next. Daftar pustaka sesuai format DNA.
5. QA: skrip `qa_bukuN.py` -> cetak PASS/FAIL semua kriteria. HARUS semua PASS.
6. Output ke `FINAL/Buku N - <Nama> - PKN - FINISH.pdf/.docx`. Commit + push via tool github push_to_remote (path repo, owner arifibnsawir-svg, branch main).

GOTCHA penting:
- target-counter WeasyPrint hanya benar TANPA counter-reset/counter-set apa pun.
- DOCX & PDF tidak akan identik 100% paginasinya; karena itu daftar isi DOCX diambil dari scan PDF (acuan = PDF). Beri tahu user PDF adalah versi acuan.
- Spasi dobel (2.0) bikin banyak gap "terkesan kosong" di Word -> pakai 1.5-1.6 + tambah konten bila halaman kurang.
- Nomor halaman footer DOCX adalah field; di preview HP sederhana bisa tampil "1" semua, tapi benar di MS Word & saat export PDF. PDF = versi aman lintas perangkat.

## 7. Progres
- Buku 1 (Nurul Syifa): SELESAI, QA 13/13 PASS. FINAL/Buku 1 - Nurul Syifa - PKN - FINISH.pdf & .docx. 64 hal isi. DNA naratif-reflektif, APA.
- Buku 2 (Naila): SELESAI, QA 16/16 PASS. 62 hal isi. DNA akademik + 10 tabel berwarna + no.halaman kanan + daftar isi bertingkat + IEEE. Bab 5 sudah sesuai silabus (HAM jadi sub-bab).
- Buku 3, 4, 5: SELESAI di PR terpisah (buku3-balqis-lejla, buku4-lidya-ellen, buku5-nurjali).
- Buku 6 (Revalina Damayanti, NPM 202501500541): SELESAI, QA 20/20 PASS. 65 hal isi. DIBANGUN DARI NOL 100% (tanpa file sumber). DNA tematik problem-solusi + kotak Akar Masalah/Langkah Solusi (tema maroon/emas) + no.halaman pojok kanan atas + TOC nomor rata kanan & bergaris + pustaka Vancouver. Cover DIDESAIN (maroon + Garuda Pancasila domain publik, TANPA kata minibook), sampul belakang seirama + biografi penulis. Anti-plagiat (sekelas BK UNINDRA): overlap 8-gram vs B1 0.42%, B2 0.71%, B3 0.36%, B4 0.53%, B5 0.40% (semua <1%). Pipeline self-contained di _generator/buku6/ (konten.py, gen_pdf.py [WeasyPrint, cover didesain+merge], scan.py, build_docx.py [cover dirasterisasi via pymupdf], assets/garuda.png) + qa_buku6.py. (PR branch buku6-revalina)

## 8. Cara melanjutkan di sesi baru
1. Clone repo arifibnsawir-svg/Joki-tugas-.
2. BACA file ini + .kiro/steering/aturan-buku-pkn.md.
3. Install dependency (bagian 6). Ambil file asli dari `SUMBER_ASLI (jangan dikumpulkan)/`.
4. Tiru pipeline `_generator/buku2/` untuk Buku 3 (Balqis Lejla) dengan DNA-nya (kontekstual-aplikatif, no.halaman pojok luar, poin-poin+kotak studi kasus, daftar pustaka Harvard).
5. Verifikasi link referensi (200) sebelum dipakai. Jalankan QA sampai semua PASS. Commit + push ke FINAL/.
6. Lanjut Buku 4 (MLA, dialogis) lalu Buku 5 (kasus gambar).
