---
name: jarvis-document-factory
description: "Hasilkan dokumen PPTX, DOCX, dan PDF kualitas one-shot dari satu SPEC terstruktur. Dipicu saat diminta membuat/menyusun presentasi (.pptx), Word (.docx), atau PDF: laporan, makalah, modul, mini-book, slide sidang. Model mengeluarkan SPEC (JSON) lalu renderer deterministik yang membuat file; gate deterministik (Python) satu-satunya penentu DONE. Untuk dokumen akademik (is_academic=true), PIPA4 council (LLM audit via jarvis-reason) otomatis dipicu setelah factory gate PASS. Humanizer + cite-or-abstain selalu nyala; gambar hanya dari path yang benar-benar ada (anti-halu)."
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

## Alur (Router -> ARSI loop -> Gate -> PIPA4)
1. **Audit:** baca permintaan + sumber, tentukan format & apakah butuh sumber ilmiah.
   Kalau akademik, panggil skill `academic-search` DULU untuk sumber terverifikasi.
2. **Rancang:** susun SPEC (identity, sections berurut, blocks, tables, figures, references).
3. **Sistemasi:** terapkan humanizer + citation + image-resolver, validasi, render tiap format.
4. **Iterasi:** jalankan `gate`; kalau FAIL, perbaiki SPEC dari daftar cek yang gagal lalu
   render ulang. Ulang sampai gate PASS.
5. **PIPA4 Council (auto, akademik saja):** setelah factory gate PASS untuk `is_academic=true`,
   PIPA4 council otomatis dipicu lewat `pipa4_gate.sh` (LLM audit via jarvis-reason).
   Hasilnya di JSON output (`pipa4_council`). Fail-open: kalau PIPA4 tidak terpasang
   di Acer, skip graceful — tidak menggagalkan factory gate. Kill-switch: `PIPA4_AUTO=off`.

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
  "figures": [ {"ref","path","caption","verified_path"} ],
  "pipa4_constraint": "academic_book.json" (opsional, default otomatis) }
```
Block (tagged by "type"): `heading{level:2|3,id,text}`, `paragraph{text}`, `lead{text}`,
`list{ordered,items}`, `table{caption,header,rows}`, `callout{text}`, `figure{ref}`.
Default akademik (kalau `is_academic` dan tak dioverride): A4, Times New Roman 12,
spasi 1.5, rata kiri-kanan, nomor halaman Arab, margin 3/3/4/3 cm.

## Cara pakai (entry point)
```
python3 run.py SPEC.json --out OUTDIR [--basename NAMA] [--request "minimal slides"]
```
Exit 0 hanya jika gate PASS untuk semua format (status DONE). Untuk akademik,
PIPA4 council otomatis setelah gate PASS (lihat JSON `pipa4_council`).

### Hasil: baca dari JSON report, jangan menebak
run.py mencetak JSON report dengan `page_count` DAN `word_count` — dihitung dari
FILE JADI. Selalu baca dari situ, jangan menebak dari teks SPEC mentah.

### Pra-cek SPEC (WAJIB sebelum run.py)
```
python3 validate_spec.py SPEC.json      # --json untuk output mesin
```
Exit 0 = siap render. Exit 1 = ada masalah + hint. Exit 2 = file/JSON rusak.

### Kalau run.py GAGAL (AWAITING_GATE / error) - ANTI-FALLBACK
JANGAN freehand. validate_spec -> perbaiki SPEC -> re-run (maks 5 iterasi) ->
berhenti + lapor Arif. Template di `examples/makalah_4bab_spec.json`.

## Yang dicek gate (semua harus PASS)
`structure_order`, `citation_consistency`, `humanizer_clean`, `no_blank_page`,
`no_dangling_heading`, `toc_accurate`, `images_real`.

## PIPA4 Council (auto untuk dokumen akademik)
Setelah 7 cek gate PASS dan `is_academic=true`, council PIPA4 otomatis:
- Subprocess `bash ~/.hermes/scripts/pipa4_gate.sh <file> <constraint.json>`
- LLM audit via `jarvis-reason` (phase6a + council phase6c/6d)
- Verdict: PASS (READY_FOR_HUMAN_REVIEW + 0 false-READY) / NEEDS_WORK / ERROR
- Hasil: `pipa4_council.verdict`, `.final_status`, `.false_ready_count`

Council = ADVISORY. Factory gate tetap otoritas DONE. NEEDS_WORK = sinyal
perbaikan, bukan kegagalan. PIPA4 berat (~300s) — hanya final akademik.
Fail-open + kill-switch `PIPA4_AUTO=off`.

## Detail renderer
- **PDF:** WeasyPrint A4, target-counter TOC, hyphens:none, Liberation Serif.
- **DOCX:** python-docx mirror PDF, footer PAGE field, TOC scan dari PDF.
- **PPTX:** render_deck.py 16:9, akademik/business/dark preset.

## Beda dengan skill lain
- `academic-document-factory`: panduan/referensi. Skill INI: pipeline SPEC->renderer->gate.
- `pptx-slides-creation-guard`: mewajibkan render_deck. Skill ini MELAKUKAN itu.
- `humanizer`: di-reuse, tidak diduplikasi.

## Checklist verifikasi
- [ ] SPEC dulu, tidak ada penulisan biner manual.
- [ ] validate_spec.py exit 0 sebelum run.py.
- [ ] Humanizer + cite-or-abstain jalan.
- [ ] Semua figure punya path nyata.
- [ ] `gate` PASS sebelum menyebut DONE.
- [ ] `word_count` dari JSON report, bukan tebakan.
- [ ] Untuk akademik: `pipa4_council` dicek di JSON.
