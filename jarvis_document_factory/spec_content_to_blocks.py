#!/usr/bin/env python3
"""SPEC converter: "content": "string" → "blocks": [...]

Fixes the ROOT CAUSE of the 20-iteration debug hell experienced on 2026-07-02.

Jarvis naturally writes:  "content": "Paragraf satu. Paragraf dua."
Factory needs:           "blocks": [{"type":"paragraph", "text":"Paragraf satu."}, ...]

This script bridges the gap. Run BEFORE validate_spec.
Report-only by default (--fix to convert). Safe: always writes to new file.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

# Markers that indicate structural content
_HEADING_PATTERN = re.compile(r"^(#+\s+|(?:\d+\.)+\s+)(.+)", re.MULTILINE)
_LIST_PATTERN = re.compile(r"^[-*]\s+(.+)", re.MULTILINE)
_ORDERED_PATTERN = re.compile(r"^\d+\.\s+(.+)", re.MULTILINE)


def count_blocks(spec: dict) -> dict:
    """Count sections using blocks vs content format."""
    blocks_count = 0
    content_count = 0
    for s in spec.get("sections", []):
        if s.get("blocks"):
            blocks_count += 1
        elif s.get("content"):
            content_count += 1
    return {"blocks": blocks_count, "content": content_count}


def convert_content_to_blocks(content: str) -> list[dict]:
    """Convert a content string into blocks array.
    
    Simple heuristics:
    - Double newline = new paragraph
    - Single newline within paragraph = same paragraph
    - Lines starting with # or digits. = heading (level 3)
    - Lines starting with - or * = unordered list
    - Lines starting with digit. = ordered list
    """
    if not content or not content.strip():
        return []
    
    blocks = []
    paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
    
    for para in paragraphs:
        # Check if it looks like a heading
        heading_match = _HEADING_PATTERN.match(para)
        if heading_match:
            blocks.append({
                "type": "heading",
                "level": 2 if not heading_match.group(2).startswith("#") else 3,
                "id": "h-" + re.sub(r"[^a-z0-9]+", "-", heading_match.group(2).lower())[:40],
                "text": heading_match.group(2).strip()
            })
            continue
        
        # Check if it's all list items
        lines = para.split("\n")
        if all(_LIST_PATTERN.match(l.strip()) for l in lines if l.strip()):
            items = [_LIST_PATTERN.match(l.strip()).group(1) for l in lines if l.strip()]
            blocks.append({"type": "list", "ordered": False, "items": items})
            continue
        
        if all(_ORDERED_PATTERN.match(l.strip()) for l in lines if l.strip()):
            items = [_ORDERED_PATTERN.match(l.strip()).group(1) for l in lines if l.strip()]
            blocks.append({"type": "list", "ordered": True, "items": items})
            continue
        
        # Default: paragraph
        blocks.append({"type": "paragraph", "text": para})
    
    return blocks


def convert_spec(spec: dict, dry_run: bool = True) -> dict:
    """Convert all 'content' sections to 'blocks'. Returns report."""
    sections = spec.get("sections", [])
    converted = 0
    unchanged = 0
    new_spec = json.loads(json.dumps(spec))
    
    for i, section in enumerate(new_spec.get("sections", [])):
        content = section.get("content")
        existing_blocks = section.get("blocks")
        
        if content and not existing_blocks:
            new_blocks = convert_content_to_blocks(content)
            section["blocks"] = new_blocks
            section.pop("content", None)
            converted += 1
        elif existing_blocks:
            unchanged += 1
    
    return {
        "spec": new_spec,
        "converted": converted,
        "unchanged": unchanged,
        "total_sections": len(sections),
        "has_content_sections": count_blocks(spec)["content"] > 0,
    }


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Convert SPEC 'content': 'string' → 'blocks': [...] format"
    )
    ap.add_argument("spec", help="Path to SPEC JSON file")
    ap.add_argument("--fix", action="store_true",
                    help="Write converted SPEC (with .fixed.json suffix)")
    ap.add_argument("--json", action="store_true", help="Output JSON")
    args = ap.parse_args()
    
    try:
        with open(args.spec, "r", encoding="utf-8") as f:
            spec = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: File not found: {args.spec}")
        return 2
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}")
        return 2
    
    counts = count_blocks(spec)
    
    if counts["content"] == 0:
        if args.json:
            print(json.dumps({"status": "ok", "message": "All sections use blocks format",
                             "counts": counts}, indent=2))
        else:
            print(f"OK: All {counts['blocks']} sections use blocks format. No conversion needed.")
        return 0
    
    result = convert_spec(spec, dry_run=not args.fix)
    
    if args.json:
        print(json.dumps({
            "status": "converted" if args.fix else "needs_conversion",
            "counts_before": counts,
            "counts_after": count_blocks(result["spec"]),
            "converted_sections": result["converted"],
            "unchanged_sections": result["unchanged"],
        }, indent=2))
    else:
        print(f"Found {counts['content']} section(s) using 'content': 'string' format")
        print(f"  (factory CANNOT read this — it needs 'blocks': [...] format)")
        print(f"  {result['converted']} will be converted if using --fix")
        if args.fix:
            out_path = args.spec.replace(".json", ".fixed.json")
            if out_path == args.spec:
                out_path = args.spec + ".fixed"
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(result["spec"], f, ensure_ascii=False, indent=2)
            print(f"\nConverted SPEC saved to: {out_path}")
            print(f"Run: validate_spec.py {out_path}")
            return 0
        else:
            print(f"\nRun with --fix to convert. Or use --json for machine output.")
            return 1
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
