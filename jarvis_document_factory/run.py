#!/usr/bin/env python3
"""Entry point for the Jarvis Document Factory skill.

Reads a SPEC (JSON) and produces the requested PPTX/DOCX/PDF files through the
Router, the four-stage loop, and the deterministic gate.

PIPA4 auto-wiring: untuk dokumen akademik (is_academic=true), PIPA4 council
(LLM audit via jarvis-reason) otomatis dipicu setelah factory gate PASS.
Hasilnya di JSON output. Fail-open. Kill-switch: PIPA4_AUTO=off.

Usage:
    run.py SPEC.json --out OUTDIR [--basename NAME] [--request "..."]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

_SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
if _SKILL_DIR not in sys.path:
    sys.path.insert(0, _SKILL_DIR)

from docfactory.orchestrator import run_pipeline  # noqa: E402


def main(argv=None):
    parser = argparse.ArgumentParser(description="Jarvis Document Factory")
    parser.add_argument("spec", help="path to a SPEC JSON file")
    parser.add_argument("--out", required=True, help="output directory")
    parser.add_argument("--basename", default="document", help="output file base name")
    parser.add_argument("--request", default="", help="raw request text")
    args = parser.parse_args(argv)

    with open(args.spec, "r", encoding="utf-8") as f:
        spec_dict = json.load(f)

    result = run_pipeline(spec_dict, args.out, basename=args.basename, request=args.request)

    report = {
        "status": result.status,
        "iterations": result.iterations,
        "route": {
            "formats": result.route.formats,
            "pptx_style": result.route.pptx_style,
            "delegate": result.route.delegate,
        },
        "consistency": result.consistency,
        "outputs": {
            fmt: {
                "path": r.out_path,
                "page_count": r.page_count,
                "word_count": r.word_count,
                "verdict": result.verdicts[fmt].verdict,
                "failed_checks": [{"check": c.check_id, "detail": c.detail}
                                  for c in result.verdicts[fmt].failed_checks],
            }
            for fmt, r in result.results.items()
        },
    }
    if result.pipa4:
        report["pipa4_council"] = result.pipa4
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if result.status == "DONE" else 1


if __name__ == "__main__":
    sys.exit(main())
