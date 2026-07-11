#!/usr/bin/env bash
# Broken internal link checker for static HTML site
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

BROKEN=0
CHECKED=0

echo "=== Internal Link Check ==="

for f in *.html; do
  # Extract href values pointing to local .html files
  while IFS= read -r href; do
    # Strip query/fragment
    target="${href%%#*}"
    target="${target%%\?*}"
    [ -z "$target" ] && continue
    [[ "$target" == http* ]] && continue
    [[ "$target" == mailto:* ]] && continue
    [[ "$target" == tel:* ]] && continue

    CHECKED=$((CHECKED + 1))

    if [[ "$target" == "/" ]]; then
      if [ ! -f "index.html" ]; then
        echo "BROKEN: $f -> $href (index.html missing)"
        BROKEN=$((BROKEN + 1))
      fi
      continue
    fi

    # Normalize leading slash
    target="${target#/}"

    # Extensionless internal paths map to local *.html source files
    if [[ "$target" == *.html ]]; then
      if [ ! -f "$target" ]; then
        echo "BROKEN: $f -> $href"
        BROKEN=$((BROKEN + 1))
      fi
      continue
    fi

    if [ -f "${target}.html" ]; then
      continue
    fi

    if [ ! -f "$target" ]; then
      echo "BROKEN: $f -> $href"
      BROKEN=$((BROKEN + 1))
    fi
  done < <(grep -oE 'href="[^"]+"' "$f" | sed 's/href="//;s/"$//')
done

echo
echo "Checked $CHECKED internal links"
if [ "$BROKEN" -eq 0 ]; then
  echo "OK: No broken internal links"
else
  echo "FAIL: $BROKEN broken link(s)"
  exit 1
fi
