#!/usr/bin/env bash
# Springfield Junk Removal Service — local QA integrity checks
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PASS=0
FAIL=0
WARN=0

ok()   { echo "  OK: $1"; PASS=$((PASS + 1)); }
bad()  { echo "  FAIL: $1"; FAIL=$((FAIL + 1)); }
warn() { echo "  WARN: $1"; WARN=$((WARN + 1)); }

echo "=== Springfield Junk Removal QA ==="
echo "Root: $ROOT"
echo

# --- HTML page count ---
HTML_COUNT=$(ls -1 *.html 2>/dev/null | wc -l | tr -d ' ')
echo "--- Page inventory ---"
echo "HTML files: $HTML_COUNT"
if [ "$HTML_COUNT" -eq 32 ]; then
  ok "32 HTML pages present"
else
  bad "Expected 32 HTML pages, found $HTML_COUNT"
fi

# --- Sitemap ---
echo
echo "--- Sitemap ---"
SITEMAP_COUNT=$(grep -c '<loc>' sitemap.xml || true)
if [ "$SITEMAP_COUNT" -eq 32 ]; then
  ok "sitemap.xml contains exactly 32 URLs"
else
  bad "sitemap.xml has $SITEMAP_COUNT URLs (expected 32)"
fi

# --- robots.txt ---
echo
echo "--- robots.txt ---"
if grep -q 'Allow: /' robots.txt && grep -q 'sitemap.xml' robots.txt; then
  ok "robots.txt allows crawl and references sitemap"
else
  bad "robots.txt missing Allow or sitemap reference"
fi

# --- Per-page technical checks ---
echo
echo "--- Per-page technical (GTM, tel, canonical, favicon, analytics) ---"
for f in *.html; do
  gtm=$(grep -c 'GTM-GDJF54DV' "$f" || true)
  if [ "$gtm" -ne 2 ]; then bad "$f: GTM hits=$gtm (expected 2)"; else ok "$f: GTM"; fi

  if ! grep -q 'tel:4172425370' "$f"; then bad "$f: missing tel:4172425370"; else ok "$f: tel"; fi

  if ! grep -q 'rel="canonical"' "$f"; then bad "$f: missing canonical"; else ok "$f: canonical"; fi

  if ! grep -q 'favicon.ico' "$f"; then bad "$f: missing favicon"; else ok "$f: favicon"; fi

  if ! grep -q 'analytics-events.js' "$f"; then bad "$f: missing analytics-events.js"; else ok "$f: analytics"; fi

  if grep -q '<form' "$f"; then
    if ! grep -q 'formspree.io/f/mojzdkvg' "$f"; then bad "$f: form missing Formspree endpoint"; else ok "$f: Formspree"; fi
  fi
done

# --- Protected values unchanged ---
echo
echo "--- Protected values ---"
if grep -r 'GTM-' *.html 2>/dev/null | grep -v 'GTM-GDJF54DV' | grep -q .; then
  bad "Unexpected GTM ID found"
else
  ok "GTM ID unchanged (GTM-GDJF54DV only)"
fi

if grep -r 'formspree.io/f/' *.html 2>/dev/null | grep -v 'mojzdkvg' | grep -q .; then
  bad "Unexpected Formspree endpoint found"
else
  ok "Formspree endpoint unchanged"
fi

# --- Claim-risk grep ---
echo
echo "--- Claim-risk scan (should be 0 or only safe negations) ---"
RISK_PATTERNS=(
  'our crew'
  'our truck'
  'we haul'
  'we load'
  'we clear'
  'we handle'
  'we bring'
  'we disconnect'
  'we tear down'
  'we dismantle'
  'we demolish'
  'licensed'
  'insured'
  'guaranteed availability'
  'same-day guarantee'
  'guaranteed same-day'
  'a local provider can'
)

for pat in "${RISK_PATTERNS[@]}"; do
  count=$(grep -riE "$pat" *.html 2>/dev/null | grep -viE 'not guaranteed|isn.t guaranteed|not assume|not included|not provided|do not|don.t provide|aren.t assumed|is not assumed|require separate confirmation|confirmed during the quote' | wc -l | tr -d ' ')
  if [ "$count" -gt 0 ]; then
    bad "Risk pattern '$pat': $count hit(s)"
    grep -rinE "$pat" *.html 2>/dev/null | grep -viE 'not guaranteed|isn.t guaranteed|not assume|not included|not provided|do not|don.t provide|aren.t assumed|is not assumed|require separate confirmation|confirmed during the quote' | head -5 || true
  else
    ok "No risky hits for '$pat'"
  fi
done

# --- Hub pages exist ---
echo
echo "--- Hub pages ---"
for hub in junk-removal-services-springfield-mo.html junk-removal-service-areas-springfield-mo.html junk-removal-guides-springfield-mo.html; do
  if [ -f "$hub" ]; then ok "Hub exists: $hub"; else bad "Missing hub: $hub"; fi
done

# --- Docs ---
echo
echo "--- Documentation ---"
for doc in springfield-baseline-audit.md page-inventory.md claim-correction-log.md internal-link-map.md indexing-priority-tracker.md citation-tracker-template.md proof-of-life-checklist.md renter-readiness-checklist.md deployment-qa-checklist.md change-log.md reusable-patterns.md; do
  if [ -f "docs/$doc" ]; then ok "docs/$doc"; else bad "Missing docs/$doc"; fi
done

echo
echo "=== Summary: $PASS passed, $FAIL failed, $WARN warnings ==="
if [ "$FAIL" -gt 0 ]; then exit 1; fi
