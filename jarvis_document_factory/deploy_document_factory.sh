#!/usr/bin/env bash
# Deploy the Jarvis Document Factory as a no-restart Hermes skill.
#
# Copies this skill folder to ~/.hermes/skills/productivity/jarvis-document-factory/
# and installs the one missing runtime dependency (weasyprint) into the Hermes
# virtualenv. No Jarvis restart is needed: Hermes discovers skills from the
# skills directory on the next turn.
#
# Run this ON THE ACER SERVER (Jarvis host), not from Kiro.
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${HERMES_SKILLS_DIR:-$HOME/.hermes/skills/productivity}/jarvis-document-factory"
VENV_PY="${HERMES_VENV_PY:-$HOME/.hermes/hermes-agent/venv/bin/python}"

echo "== Jarvis Document Factory deploy =="
echo "source: $SRC"
echo "dest:   $DEST"
echo "python: $VENV_PY"

# 1) copy skill (exclude tests, caches, examples output)
mkdir -p "$DEST"
if command -v rsync >/dev/null 2>&1; then
  rsync -a --delete \
    --exclude '__pycache__' --exclude '.pytest_cache' --exclude '.hypothesis' \
    --exclude 'tests' --exclude '*.pyc' \
    "$SRC"/ "$DEST"/
else
  rm -rf "$DEST"/docfactory "$DEST"/SKILL.md "$DEST"/run.py "$DEST"/requirements.txt "$DEST"/examples
  cp -r "$SRC"/docfactory "$SRC"/SKILL.md "$SRC"/run.py "$SRC"/requirements.txt "$SRC"/examples "$DEST"/
  find "$DEST" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
fi

# 2) ensure runtime deps in the Hermes venv (only weasyprint is missing per grounding)
echo "== checking runtime deps in Hermes venv =="
"$VENV_PY" - <<'PY'
import importlib.util as u
missing = [m for m in ["weasyprint", "docx", "pptx", "pypdf", "jinja2"] if u.find_spec(m) is None]
print("missing:", missing or "none")
open("/tmp/_dcf_missing.txt", "w").write(" ".join(missing))
PY
MISSING="$(cat /tmp/_dcf_missing.txt)"
if echo "$MISSING" | grep -qw weasyprint; then
  echo "installing weasyprint into Hermes venv..."
  "$VENV_PY" -m pip install --quiet weasyprint
fi

# 3) verify import + render_deck reachability
echo "== verify =="
HERMES_RENDER_DECK="${HERMES_RENDER_DECK:-$HOME/.hermes/scripts/render_deck.py}" \
"$VENV_PY" - <<PY
import sys
sys.path.insert(0, "$DEST")
from docfactory.orchestrator import run_pipeline
from docfactory.renderers.pptx import _load_render_deck
print("docfactory import: OK")
try:
    _load_render_deck(); print("render_deck reachable: OK")
except Exception as e:
    print("render_deck reachable: WARN ->", e)
PY

echo "== DONE. Skill at: $DEST =="
echo "Verify no-restart: start a NEW Jarvis turn and ask it to make a PDF/DOCX/PPTX."
