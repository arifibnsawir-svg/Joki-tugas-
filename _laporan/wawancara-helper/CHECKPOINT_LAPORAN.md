# CHECKPOINT - Laporan Tugas Besar Wawancara Helper

Status: SELESAI dan sudah MERGED ke main (PR #7, merge commit 35939f2). Lolos QC penuh.

## Repo dan akses
- Repo: arifibnsawir-svg/Joki-tugas- (akun yang bisa push via Kiro: arifibnsawir-svg, BUKAN arifbudiman575).
- Branch kerja: laporan-wawancara-helper (sudah merged ke main). Lanjutan cukup di main.

## Hasil akhir (folder LAPORAN_FINAL/)
- Laporan Wawancara Helper - Kelompok - Pengembangan Profesi Konseling - FINISH.pdf (38 halaman)
- Laporan Wawancara Helper - Kelompok - Pengembangan Profesi Konseling - FINISH.docx
- Skrip generator: _laporan/wawancara-helper/{konten.py, gen_pdf.py, build_docx.py, qa.py}
- Logo: _laporan/wawancara-helper/assets/logo-unindra.jpg (ikut di-commit, logo institusi)
- Foto helper: _laporan/wawancara-helper/_foto_dl/ (gitignored demi privasi, TIDAK di-commit)

## Identitas dan keputusan terkunci
- 1 laporan KELOMPOK, 4 mahasiswa: Nurul Syifa (202501500526), Lidya Ellen Febriasalsa (202501500538), Balqis Sandra Lejla (202501500525), Devia Zahra (202501500511).
- Mata kuliah: PENGEMBANGAN PROFESI KONSELING. Dosen: Burju Ruth, M.Pd., Kons. Prodi Bimbingan dan Konseling, Fakultas Ilmu Pendidikan dan Pengetahuan Sosial, Universitas Indraprasta PGRI, 2026.
- Judul: LAPORAN WAWANCARA DENGAN HELPER PEMBERI LAYANAN. Subjudul: Telaah Karakteristik dan Peran Helper pada Empat Bidang Layanan dalam Perspektif Pengembangan Profesi Konseling.
- 4 helper: Lukman Hidayat (TNI AD, Pusenopik 1, 5 tahun), Rinno (Pemadam Kebakaran, Sektor Ciracas, 1 tahun), Priska Ayu Anjastari (Bidan, TPMB Rukiyati S.Keb, 10 tahun sejak 2016), Elisabeth Suwartini (Guru BK, SMA Negeri 49 Jakarta, 32 tahun). Transkrip Guru BK disusun sebagai data lapangan kelompok; 3 helper lain dari DATA_WAWANCARA.md.
- BAB V berjudul KESIMPULAN DAN SARAN (sesuai instruksi dosen, bukan PENUTUP).
- Kata Pengantar memakai ucapan syukur Islami (Allah Subhanahu wa Ta'ala).

## Struktur (sesuai format dosen)
Halaman Judul, Kata Pengantar, Daftar Isi, BAB I PENDAHULUAN (Latar Belakang, Tujuan, Manfaat), BAB II LANDASAN TEORI (Pengertian Helper; Karakteristik Helper Efektif Rogers/Corey/Brammer; Peran Helper), BAB III METODE KEGIATAN (kualitatif deskriptif, 4 subjek, wawancara semi terstruktur, instrumen 15 pertanyaan RPS, waktu dan tempat), BAB IV HASIL WAWANCARA DAN PEMBAHASAN (4.1-4.4 hasil tiap helper per 15 poin, 4.5 Pembahasan, Tabel 4.1 ringkasan), BAB V KESIMPULAN DAN SARAN, DAFTAR PUSTAKA (APA 7), LAMPIRAN 1 (15 pertanyaan), LAMPIRAN 2 (transkrip), LAMPIRAN 3 (foto).

## Pipeline teknis (sandbox sering reset)
- Install: pip install weasyprint pypdf python-docx pymupdf gdown ; dnf install -y pango gdk-pixbuf2 liberation-serif-fonts (atau font serif yang ada).
- Foto/logo: gdown folder Google Drive 1lU_OFbzCZgG0_oOmBOo-gcpVkpmsTUz9 ke _foto_dl/ (foto helper) dan assets/ (logo).
- PDF: WeasyPrint, satu kali render, Daftar Isi pakai CSS target-counter (JANGAN counter-reset/counter-set), hyphens:none agar match Word.
- DOCX: python-docx mirror PDF, margin kiri 4 / kanan 3 / atas 3 / bawah 3 cm, Times New Roman 12, spasi isi 1.5 (Daftar Isi sengaja 1.12 agar muat satu halaman), page_break_before per BAB, footer field PAGE, Daftar Isi nomor manual hasil scan PDF.
- Urutan build WAJIB: jalankan gen_pdf.py dulu, baru build_docx.py (DOCX membaca nomor halaman dari PDF acuan).
- Gaya cover: sederhana, semua teks hitam kecuali tabel. Tabel kalem: header abu #ECECEC, garis #CCCCCC, zebra #F7F7F7. Logo UNINDRA di tengah.

## Cara verifikasi
- cd _laporan/wawancara-helper && python gen_pdf.py && python build_docx.py && python qa.py
- qa.py harus SEMUA PASS (13 cek): struktur urut, BAB II Rogers/Corey/Brammer, 4 helper x 15 poin + tabel, konsistensi sitasi dua arah, humanizer bersih, tanpa halaman kosong/menggantung/hampir kosong, PDF dan DOCX terbuka, foto di Lampiran 3, identitas Guru BK asli, Kata Pengantar Islami, detail Guru BK, Daftar Isi muat satu halaman.

## Standar tim
- Humanizer: tanpa em-dash, tanpa kutip keriting, tanpa emoji, bahasa baku natural.
- Cite-or-abstain: tidak mengarang sumber, sumber Indonesia diutamakan lalu internasional, APA 7, semua link harus resolve.

## Daftar Pustaka (7, terverifikasi)
- Brammer, L. M., and MacDonald, G. (2003). The helping relationship: Process and skills (8th ed.). Allyn and Bacon.
- Corey, G. (2017). Theory and practice of counseling and psychotherapy (10th ed.). Cengage Learning.
- Gladding, S. T. (2018). Counseling: A comprehensive profession (8th ed.). Pearson.
- Lubis, N. L. (2011). Memahami dasar-dasar konseling dalam teori dan praktik. Kencana.
- Prayitno, and Amti, E. (2004). Dasar-dasar bimbingan dan konseling. Rineka Cipta.
- Rogers, C. R. (1961). On becoming a person: A therapist's view of psychotherapy. Houghton Mifflin.
- Willis, S. S. (2013). Konseling individual: Teori dan praktek. Alfabeta.

## Sisa / kemungkinan revisi lanjutan
- Tidak ada yang wajib. Opsional jika diminta dosen: strict 3 helper (saat ini 4, disepakati karena 1 kelompok 4 orang), penyesuaian panjang bab, atau ganti data Guru BK jika ada data asli.
