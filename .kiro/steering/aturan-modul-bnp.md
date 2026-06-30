# Aturan Penyusunan MODUL - Belajar dan Pembelajaran (BnP) 2026

Panduan kerja untuk semua tugas MODUL mata kuliah Belajar dan Pembelajaran (Prodi Bimbingan dan Konseling, FIPPS, Universitas Indraprasta PGRI). Sumber: "FORMAT MODUL BnP 2026" dari dosen. Pakai folder `_modul/<topik>/` untuk skrip dan `MODUL_FINAL/` untuk output.

## Aturan dosen (WAJIB)
- Disusun berkelompok; tema dari daftar (mis. Gaya Belajar, Manajemen Waktu, Motivasi Belajar, dll).
- Format: A4; font **Cambria 12pt**; spasi **1,5**; rata kanan-kiri (justify); margin **kiri 4 cm, kanan 3 cm, atas 3 cm, bawah 3 cm**; nomor halaman **angka Arab**; bahasa EYD/PUEBI.
- Jumlah halaman ISI awalnya 20-25 (di luar cover, kata pengantar, daftar isi/tabel/gambar, daftar pustaka). REVISI DOSEN: tidak ada batas maksimum, asal wajar dan masuk akal.
- Sistematika: Cover -> Kata Pengantar -> Daftar Isi -> Daftar Tabel -> Daftar Gambar -> Pendahuluan -> minimal 3 Bab materi -> Refleksi -> Evaluasi -> Daftar Pustaka -> Penutup.
- Pendahuluan memuat: Apa yang Akan Dipelajari, Tujuan Pembelajaran, Cara Menggunakan Modul, Sasaran Pembaca.
- Tiap bab: Tujuan Pembelajaran -> Materi -> Contoh/Ilustrasi -> Aktivitas/Tugas -> Ringkasan.
- Refleksi: minimal 5 pertanyaan reflektif (boleh tabel/jurnal).
- Evaluasi: minimal 10 butir (PG, benar-salah, isian, esai, studi kasus) + kunci jawaban/pedoman penskoran.
- Daftar Pustaka: minimal 5 sumber kredibel, format **APA 7th edition**, urut alfabetis, semua tautan dapat dicek (HTTP 200).
- Wajib ada gambar/diagram/tabel/infografis relevan; cantumkan "Sumber" pada tiap gambar/tabel/kutipan.
- Cover: judul menarik + nama anggota + Prodi BK + FIPPS + UNINDRA + tahun, desain visual menarik.

## Rubrik penilaian (target 100%)
| Kriteria | Bobot |
|---|---|
| Kesesuaian & ketepatan materi | 30% |
| Kelengkapan struktur modul | 20% |
| Kualitas penyajian materi | 15% |
| Aktivitas, refleksi, evaluasi | 15% |
| Kreativitas & tampilan | 10% |
| Referensi & ketepatan penulisan | 10% |

## Standar tim (cara kerja)
- Pakai skill humanizer: tanpa em-dash/en-dash, tanpa kutip keriting, tanpa emoji, hindari pola AI.
- Premium: tema warna konsisten, kotak (Tujuan/Contoh/Aktivitas/Ringkasan/Tips), tabel berwarna (header + zebra), diagram/infografik ORIGINAL.
- Boleh menambah konten relevan agar premium dan padat, ASAL sumber valid + kredibel + tautan bisa dicek.
- Orisinalitas: konten ditulis ulang/humanized; jangan menyalin verbatim dari sumber. Antar-kelompok beda topik, jadi fokus anti-plagiasi = tidak menjiplak sumber.
- Output 2 format: PDF (versi premium acuan) + DOCX (editable).

## Pipeline teknis (proven, folder `_modul/<topik>/`)
1. `konten.py` - semua konten via block DSL: `('p')`, `('h2')`, `('nlist')`, `('blist')`, `('table',{no,judul,head,rows,sumber})`, `('fig',{no,judul,file,sumber})`, `('box',{kind,judul,body})` (kind: tujuan|contoh|aktivitas|ringkasan|tips). Plus KATA_PENGANTAR, PENDAHULUAN, BAB[], REFLEKSI, EVALUASI, DAFTAR_PUSTAKA (tuple `(pre,judul_italic,post,url)`), PENUTUP, MOTTO, metadata cover.
2. `figures.py` - diagram/infografik ORIGINAL (HTML/CSS -> PDF via WeasyPrint -> PNG via pymupdf, 200 dpi) ke `assets/`.
3. `gen_pdf.py` - render PDF premium (WeasyPrint). Render ISI tanpa cover lalu merge cover via pypdf (penomoran mulai 1, target-counter Daftar Isi/Tabel/Gambar akurat, TANPA counter-reset). Nomor halaman @bottom-center angka Arab.
4. `scan.py` - scan PDF final -> `page_real.json` (nomor halaman; pakai pencocokan TANPA-SPASI + top-of-page agar tahan artefak letter-spacing dan tidak ke-match ke halaman daftar).
5. `build_docx.py` - DOCX editable mirror (python-docx). Font dideklarasikan **Cambria**, margin 4/3/3/3, spasi 1,5, footer PAGE field, kotak = single-cell shaded table, tabel berwarna via shading XML, gambar disisipkan, daftar isi/tabel/gambar manual dari `page_real.json`. Cover dirasterisasi dari PDF (pymupdf) lalu disisip full-page.
6. `qa_modul.py` - cek PASS/FAIL terhadap aturan + rubrik (harus 100%).

## Catatan lingkungan (sandbox sering reset)
- Reinstall: `pip install weasyprint pypdf python-docx pymupdf gdown`.
- `dnf install pango gdk-pixbuf2 liberation-serif-fonts`.
- Font **Cambria** tidak ada di Linux. Untuk PDF pakai **Caladea** (metrik-kompatibel Cambria); unduh TTF dari `github.com/google/fonts/ofl/caladea` ke `~/.fonts` lalu `fc-cache -f`. DOCX tetap deklarasi font "Cambria" agar pas di Word pengguna.
- WeasyPrint: JANGAN pakai `flex-direction:column` + `overflow:hidden` (konten kepotong/menumpuk). Pakai layout BLOCK untuk kartu; flex hanya untuk baris sederhana.

## Status pekerjaan modul
- Modul 1 "Gaya Belajar" (Kelompok 10: Balqis Sandra Lejla, Motiara Sangadji, Nurjali Sangadji): SELESAI, QA rubrik 100% PASS. Output di `MODUL_FINAL/`. Skrip di `_modul/gaya-belajar/`.
