---
name: jarvis-document-factory
description: "Hasilkan dokumen PPTX, DOCX, dan PDF kualitas one-shot dari satu SPEC terstruktur. Dipicu saat diminta membuat/menyusun presentasi (.pptx), Word (.docx), atau PDF: laporan, makalah, modul, mini-book, slide sidang, business report, proposal. Model mengeluarkan SPEC (JSON) lalu renderer deterministik yang membuat file; gate deterministik (Python) satu-satunya penentu DONE. Setelah gate PASS, PIPA4 council (LLM audit via jarvis-reason) otomatis dipicu untuk SEMUA deliverable final — hook di ~/.hermes/scripts/pipa4_hook.py (repo jarvis, fail-open, kill-switch PIPA4_AUTO=off). Humanizer + cite-or-abstain selalu nyala; gambar hanya dari path yang benar-benar ada (anti-halu)."
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
Tiap kali diminta MEMBUAT FILE dokumen jadi: PowerPoint (.pptx), Word (.docx), PDF.
Mencakup: laporan, makalah, modul, mini-book, slide sidang, business report,
proposal, strategi, dan dokumen profesional lainnya.

## Prinsip inti (WAJIB)
1. **Structure-Before-Render.** Model TIDAK PERNAH menulis file biner langsung.
2. **Gate satu-satunya penentu DONE.** Output final setelah gate PASS.
3. **Reuse, jangan bikin ulang.** Humanizer + render_deck.py.
4. **Humanizer always-on + cite-or-abstain.**
5. **Anti-halu gambar.** Path harus ada.
6. **Scope:** PPTX, DOCX, PDF.

## Alur (Router -> ARSI loop -> Gate -> PIPA4)
1. Audit → 2. Rancang (SPEC) → 3. Sistemasi (humanizer+citation+render) →
4. Iterasi (gate, perbaiki, re-gate) → 5. PIPA4 Council (auto setelah gate PASS)

PIPA4 council dipicu untuk SEMUA deliverable final (akademik, bisnis, proposal,
dll), bukan hanya is_academic. Constraint auto-deteksi dari doc_type.

## Kontrak SPEC
`doc_type`: "report", "business_report", "proposal", "academic_paper", dll.
`is_academic`: true/false — nentuin style default + citation enforcement.
`references`: [] untuk non-akademik — gate citation_consistency auto-skip.
`pipa4_constraint`: opsional, auto-deteksi dari doc_type.

## CARA PAKAI
```
python3 run.py SPEC.json --out OUTDIR [--basename NAMA]
```
Exit 0 = gate PASS semua format. JSON punya `pipa4_council` setelah gate PASS.

### Pra-cek + ANTI-FALLBACK
validate_spec.py dulu. Kalau run.py gagal → JANGAN freehand.

## Gate (7 cek)
structure_order, citation_consistency (auto-skip kalau references: []),
humanizer_clean, no_blank_page, no_dangling_heading, toc_accurate, images_real.

## PIPA4 Council (auto untuk semua deliverable)
Setelah gate PASS → PIPA4 council auto-fire via pipa4_gate.sh.
Fail-open + kill-switch PIPA4_AUTO=off.

## Checklist
- [ ] SPEC dulu, tidak ada freehand.
- [ ] validate_spec exit 0.
- [ ] gate PASS (EXIT=0).
- [ ] word_count dari JSON, bukan tebakan.
- [ ] pipa4_council dicek di JSON (setelah gate PASS).
