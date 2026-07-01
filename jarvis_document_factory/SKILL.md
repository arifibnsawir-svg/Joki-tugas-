---
name: jarvis-document-factory
description: "Hasilkan dokumen PPTX, DOCX, dan PDF kualitas one-shot dari satu SPEC terstruktur. Dipicu saat diminta membuat/menyusun presentasi (.pptx), Word (.docx), atau PDF: laporan, makalah, modul, mini-book, slide sidang. Model mengeluarkan SPEC (JSON) lalu renderer deterministik yang membuat file; gate deterministik (Python) satu-satunya penentu DONE. Humanizer + cite-or-abstain selalu nyala; gambar hanya dari path yang benar-benar ada (anti-halu)."
version: 1.0.0
license: MIT
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
metadata:
  layer: production
  no_key: true
  deps: [weasyprint, python-docx, python-pptx, pypdf, jinja2]
  reuses: [humanizer, render_deck.py]
---

# JARVIS DOCUMENT FACTORY - satu SPEC, banyak format, gate deterministik

## Kapan dipakai
Tiap kali diminta MEMBUAT FILE dokumen jadi dalam salah satu dari tiga format:
- PowerPoint (.pptx) - deck 16:9 berdesain (bukan slide polos default).
- Word (.docx) - laporan/makalah/modul editable.
- PDF - versi cetak/acuan dengan Daftar Isi bernomor akurat.

Contoh pemicu: "buatkan PPT sidang", "susun laporan Word", "bikin makalah PDF",
"render deck + docx dari materi ini", "mini-book PDF dan Word".

## Prinsip inti (WAJIB)
1. **Structure-Before-Render.** Model TIDAK PERNAH menulis file biner langsung.
   Model mengeluarkan SPEC (JSON); renderer deterministik yang membuat file.
2. **Gate satu-satunya penentu DONE.** Output baru final setelah `gate` mengembalikan
   PASS. Sebelum itu, sebut status **AWAITING_GATE**, jangan sebut "selesai".
3. **Reuse, jangan bikin ulang.** Humanizer pakai skill `humanizer` yang sudah ada
   (`~/.hermes/skills/humanizer/`). PPTX pakai house renderer
   `~/.hermes/scripts/render_deck.py`. Skill ini TIDAK mengimplementasi ulang keduanya.
4. **Humanizer always-on** (tanpa em-dash, en-dash, kutip keriting, emoji) +
   **cite-or-abstain** (sumber terverifikasi, utamakan Indonesia, format APA) sebagai
   lapis yang selalu jalan sebelum render.
5. **Anti-halu gambar.** Gambar hanya dari path file yang benar-benar ada; referensi
   ke path yang tidak ada => error sebelum render, bukan gambar karangan.
6. **Scope ketat:** hanya PPTX, DOCX, PDF. Satu SPEC, satu renderer per format, satu gate.

## Alur (Router -> ARSI loop -> Gate)
1. **Audit:** baca permintaan + sumber, tentukan format & apakah butuh sumber ilmiah.
   Kalau akademik, panggil skill `academic-search` DULU untuk sumber terverifikasi.
2. **Rancang:** susun SPEC (identity, sections berurut, blocks, tables, figures, references).
3. **Sistemasi:** terapkan humanizer + citation + image-resolver, validasi, render tiap format.
4. **Iterasi:** jalankan `gate`; kalau FAIL, perbaiki SPEC dari daftar cek yang gagal lalu
   render ulang. Ulang sampai gate PASS.

## Kontrak SPEC (ringkas)
SPEC = objek JSON, sumber kebenaran tunggal semua renderer:
```
{ "doc_id", "formats": ["pdf"|"docx"|"pptx", ...], "doc_type", "is_academic",
  "identity": { "title"(wajib), "subtitle","course","lecturer","authors":[{name,id}],
                "program","faculty","institution","year","logo" },
  "style": { "page_size","font","font_size_pt","line_spacing","body_align",
             "page_numbers","margins_cm":{top,bottom,left,right},"accent_color" },
  "sections": [ { "id"(wajib,unik), "kind":"frontmatter|toc|chapter|references|appendix",
                  "number","title"(wajib), "blocks":[...], "pptx":{"layout"} } ],
  "references": [ {"id","apa"(APA),"url","verified"(harus true agar lolos)} ],
  "figures": [ {"ref","path","caption","verified_path"} ] }
```
Block (tagged by "type"): `heading{level:2|3,id,text}`, `paragraph{text}`, `lead{text}`,
`list{ordered,items}`, `table{caption,header,rows}`, `callout{text}`, `figure{ref}`.
Default akademik (kalau `is_academic` dan tak dioverride): A4, Times New Roman 12,
spasi 1.5, rata kiri-kanan, nomor halaman Arab, margin 3/3/4/3 cm.

## Cara pakai (entry point)
```
python3 run.py SPEC.json --out OUTDIR [--basename NAMA] [--request "minimal slides"]
```
Exit 0 hanya jika gate PASS untuk semua format (status DONE); selain itu non-zero
(AWAITING_GATE) dengan daftar cek yang gagal.

### Hasil: baca dari JSON report, jangan menebak
run.py mencetak JSON report yang berisi `page_count` DAN `word_count` untuk tiap
output — dihitung langsung dari teks FILE JADI (bukan estimasi dari SPEC). Selalu
baca dari sana, jangan pernah menebak panjang/jumlah kata dari teks SPEC mentah.

### Pra-cek SPEC (WAJIB sebelum run.py)
Sebelum memanggil run.py, jalankan validator pra-render untuk menangkap SPEC
yang salah dengan pesan JELAS (field apa yang kurang), bukan crash misterius:
```
python3 validate_spec.py SPEC.json      # tambah --json untuk output mesin
```
Exit 0 = SPEC siap dirender. Exit 1 = ada masalah (tiap masalah disebut + hint
perbaikan). Exit 2 = file tak terbaca / bukan JSON valid. Perbaiki SPEC sampai
validate_spec.py exit 0, BARU jalankan run.py. Validator ini memeriksa skema +
validasi + citation_consistency di level SPEC; gate tetap penentu akhir pada file jadi.

### Kalau run.py GAGAL (AWAITING_GATE / error) - ANTI-FALLBACK
JANGAN beralih ke freehand (python-docx / render_deck.py langsung / tulis file
biner manual). Itu pola gagal yang sudah terbukti. Sebaliknya:
1. Jalankan `validate_spec.py SPEC.json` untuk membaca masalah SPEC.
2. Baca `failed_checks` dari output run.py, perbaiki SPEC (bukan bikin file manual).
3. Jalankan ulang run.py. Maksimal 5 iterasi.
4. Kalau setelah 5 iterasi masih gagal: BERHENTI, minta bantuan Arif, lampirkan
   SPEC terakhir + output run.py + output validate_spec.py. Jangan klaim selesai.
Template struktur makalah 4 bab (Kata Pengantar, Daftar Isi, BAB I-IV, Daftar
Pustaka) ada di `examples/makalah_4bab_spec.json` - pakai sebagai acuan, jangan menebak.

## Yang dicek gate (semua harus PASS)
`structure_order` (struktur & urutan), `citation_consistency` (dua arah sitasi<->pustaka),
`humanizer_clean` (nol em-dash/en-dash/kutip keriting/emoji), `no_blank_page`,
`no_dangling_heading` (tak ada halaman cuma "BAB X"), `toc_accurate` (Daftar Isi muat &
nomor cocok), `images_real` (semua gambar dari file nyata).

## Detail renderer
- **PDF:** WeasyPrint satu-pass; `target-counter` untuk Daftar Isi TANPA `counter-reset`;
  `hyphens:none` agar patah baris cocok dengan DOCX; font Liberation Serif (metrik Times).
- **DOCX:** python-docx mirror PDF; `page_break_before` per bab; footer field PAGE;
  Daftar Isi manual dengan nomor hasil scan PDF acuan (PDF dirender lebih dulu).
- **PPTX:** panggil `render_deck.py` (deck 16:9 berdesain: aksen, accent bar, footer,
  nomor). Default = desain rumah; gaya minimal HANYA jika diminta eksplisit.

## Beda dengan skill lain (hindari rancu)
- `academic-document-factory` (sudah ada): panduan/berbasis-referensi. Skill INI berbeda:
  pipeline SPEC->renderer->gate deterministik yang benar-benar menghasilkan file + memvonis PASS/FAIL.
- `pptx-slides-creation-guard`: mewajibkan PPTX lewat `render_deck`. Skill ini MELAKUKAN itu,
  jadi saling melengkapi, bukan bertabrakan.
- `humanizer`: di-reuse sebagai lapis prosa, bukan diduplikasi di sini.

## Checklist verifikasi
- [ ] SPEC dikeluarkan lebih dulu; tidak ada penulisan biner manual.
- [ ] validate_spec.py exit 0 sebelum run.py.
- [ ] Humanizer + cite-or-abstain jalan sebelum render.
- [ ] Semua figure punya path yang ada (kalau tidak: perbaiki SPEC, jangan paksa).
- [ ] `gate` PASS untuk tiap format sebelum menyebut DONE.
- [ ] `word_count` dibaca dari JSON report run.py, bukan ditebak dari teks SPEC.
