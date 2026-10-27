#!/usr/bin/env bash
# Springfield Junk Removal Service — local QA for the lean business site
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PASS=0
FAIL=0

ok()  { echo "  OK: $1"; PASS=$((PASS + 1)); }
bad() { echo "  FAIL: $1"; FAIL=$((FAIL + 1)); }

echo "=== Springfield Junk Removal QA ==="

EXPECTED_HTML=(
  index.html
  residential-junk-removal-springfield-mo.html
  cleanouts-springfield-mo.html
  apartment-cleanout-springfield-mo.html
  estate-cleanout-springfield-mo.html
  house-cleanout-springfield-mo.html
  garage-cleanout-springfield-mo.html
  commercial-junk-removal-springfield-mo.html
  construction-debris-removal-springfield-mo.html
  yard-waste-removal-springfield-mo.html
  shed-removal-springfield-mo.html
  junk-removal-service-areas-springfield-mo.html
  junk-removal-battlefield-mo.html
  junk-removal-nixa-mo.html
  junk-removal-cost-springfield-mo.html
  springfield-junk-disposal-guide.html
  contact.html
  404.html
)

echo
echo "--- Page inventory ---"
HTML_COUNT=$(ls -1 *.html 2>/dev/null | wc -l | tr -d ' ')
if [ "$HTML_COUNT" -eq 18 ]; then ok "18 HTML pages"; else bad "Expected 18 HTML pages, found $HTML_COUNT"; fi
for f in "${EXPECTED_HTML[@]}"; do
  if [ -f "$f" ]; then ok "present $f"; else bad "missing $f"; fi
done

echo
echo "--- Sitemap, robots, llms, redirects ---"
SITEMAP_COUNT=$(grep -c '<loc>' sitemap.xml || true)
if [ "$SITEMAP_COUNT" -eq 17 ]; then ok "sitemap has 17 URLs"; else bad "sitemap has $SITEMAP_COUNT URLs"; fi
if grep -q '404.html' sitemap.xml; then bad "sitemap includes 404"; else ok "sitemap omits 404"; fi
if grep -q 'Allow: /' robots.txt && grep -q 'GPTBot' robots.txt && grep -q 'sitemap.xml' robots.txt; then
  ok "robots.txt allows search and AI crawlers"
else
  bad "robots.txt missing Allow, GPTBot, or sitemap"
fi
if [ -f llms.txt ] && grep -q 'Springfield Junk Removal Service' llms.txt; then
  ok "llms.txt present"
else
  bad "llms.txt missing"
fi
if grep -q ' 301' _redirects; then ok "_redirects has 301s"; else bad "_redirects missing 301"; fi

# Every retired path in _redirects should not still be an HTML file, and the target should exist.
echo
echo "--- Redirect targets ---"
while read -r src dest code; do
  [[ "$src" == \#* || -z "${src:-}" ]] && continue
  [ "$code" = "301" ] || bad "redirect is not 301: $src"
  base="${src#/}"
  base="${base%.html}"
  base="${base%/}"
  if [ -f "${base}.html" ]; then bad "redirect source still exists as HTML: $base.html"; fi
  if [ "$dest" = "/" ]; then
    [ -f index.html ] || bad "redirect target / missing index.html"
  else
    t="${dest#/}"
    [ -f "${t}.html" ] || bad "redirect target missing: $dest"
  fi
done < _redirects
ok "redirect file parsed"

RESTORED=(
  apartment-cleanout-springfield-mo
  estate-cleanout-springfield-mo
  house-cleanout-springfield-mo
  garage-cleanout-springfield-mo
  shed-removal-springfield-mo
  construction-debris-removal-springfield-mo
  junk-removal-battlefield-mo
  junk-removal-nixa-mo
)
for slug in "${RESTORED[@]}"; do
  if grep -q "/${slug}" _redirects; then bad "restored URL still redirected: $slug"; else ok "no redirect for $slug"; fi
  if grep -q "https://springfieldjunkremovalservice.com/${slug}" sitemap.xml; then ok "sitemap lists $slug"; else bad "sitemap missing $slug"; fi
  if grep -q "href=\"https://springfieldjunkremovalservice.com/${slug}\"" "${slug}.html"; then
    ok "$slug self canonical"
  else
    bad "$slug canonical is not itself"
  fi
done

echo
echo "--- Per-page technical ---"
TITLES=""
H1S=""
for f in *.html; do
  if [ "$f" = "404.html" ]; then
    grep -q 'noindex' "$f" && ok "404 noindex" || bad "404 missing noindex"
    if grep -q 'rel="canonical"' "$f"; then bad "404 has a canonical"; else ok "404 has no canonical"; fi
    grep -q 'tel:4172425370' "$f" && ok "404 tel" || bad "404 missing tel"
    grep -q 'GTM-GDJF54DV' "$f" && ok "404 GTM" || bad "404 missing GTM"
    h1=$(grep -c '<h1>' "$f" || true)
    if [ "$h1" -eq 1 ]; then ok "404 one H1"; else bad "404 H1 count=$h1"; fi
    continue
  fi
  gtm=$(grep -c 'GTM-GDJF54DV' "$f" || true)
  if [ "$gtm" -ge 2 ]; then ok "$f GTM"; else bad "$f GTM hits=$gtm"; fi
  grep -q 'tel:4172425370' "$f" && ok "$f tel" || bad "$f missing tel"
  grep -q 'rel="canonical"' "$f" && ok "$f canonical" || bad "$f missing canonical"
  grep -q 'favicon.ico' "$f" && ok "$f favicon" || bad "$f missing favicon"
  grep -q 'analytics-events.js' "$f" && ok "$f analytics" || bad "$f missing analytics"
  grep -q '541475893' "$f" && ok "$f GA4 placeholder note" || bad "$f missing GA4 placeholder"
  grep -q 'formspree.io/f/mojzdkvg' "$f" && ok "$f Formspree" || bad "$f missing Formspree"
  grep -q '"@type": "LocalBusiness"' "$f" && ok "$f LocalBusiness" || bad "$f missing LocalBusiness"
  grep -q 'areaServed' "$f" && ok "$f areaServed" || bad "$f missing areaServed"
  grep -q '"@type": "FAQPage"' "$f" && ok "$f FAQPage" || bad "$f missing FAQPage"
  h1=$(grep -c '<h1>' "$f" || true)
  if [ "$h1" -eq 1 ]; then ok "$f one H1"; else bad "$f H1 count=$h1"; fi
  if grep -q 'streetAddress\|PostalAddress\|AggregateRating' "$f"; then bad "$f has forbidden schema"; else ok "$f no address/rating schema"; fi
  title=$(sed -n 's/.*<title>\(.*\)<\/title>.*/\1/p' "$f" | head -1)
  h1text=$(sed -n 's/.*<h1>\(.*\)<\/h1>.*/\1/p' "$f" | head -1)
  TITLES="$TITLES|$title"
  H1S="$H1S|$h1text"
done

# Homepage must name Springfield, MO in title and H1
if grep -q '<title>Junk Removal in Springfield, MO' index.html && grep -q '<h1>Junk Removal in Springfield, MO</h1>' index.html; then
  ok "homepage title and H1 include Springfield, MO"
else
  bad "homepage title or H1 missing Springfield, MO"
fi

python3 - << 'PY'
import re, collections, pathlib, sys
titles=[]
h1s=[]
for p in pathlib.Path('.').glob('*.html'):
    t=p.read_text()
    titles.append(re.search(r'<title>(.*?)</title>', t).group(1))
    h1s.append(re.search(r'<h1>(.*?)</h1>', t).group(1))
    blocks=re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', t, re.S)
    import json
    for b in blocks:
        json.loads(b)
bad=False
for label, vals in (('title', titles), ('h1', h1s)):
    dup=[k for k,v in collections.Counter(vals).items() if v>1]
    if dup:
        print('DUP', label, dup)
        bad=True
if bad:
    sys.exit(1)
print('unique titles and h1s; JSON-LD parses')
PY
if [ $? -eq 0 ]; then ok "unique titles, H1s, valid JSON-LD"; else bad "duplicate titles/H1s or bad JSON-LD"; fi

echo
echo "--- Claim and tracking guardrails ---"
if grep -R 'formspree.io/f/' --include='*.html' -n . | grep -v mojzdkvg | grep -q .; then
  bad "unexpected Formspree id"
else
  ok "Formspree id only mojzdkvg"
fi
if grep -R 'GTM-' --include='*.html' -n . | grep -v 'GTM-GDJF54DV' | grep -q .; then
  bad "unexpected GTM id"
else
  ok "GTM id unchanged"
fi
if grep -R -E -i 'licensed|insured|aggregateRating|5-star|years in business|same-day guarantee' --include='*.html' . | grep -q .; then
  bad "unsupported claim language found"
else
  ok "no license, rating, or guarantee claims"
fi
if grep -R -E -i 'text us|sms' --include='*.html' . | grep -q .; then
  bad "SMS language found"
else
  ok "no SMS"
fi
if grep -q 'GA4_MEASUREMENT_ID_PROPERTY_541475893 = ""' analytics-events.js; then
  ok "GA4 measurement ID left blank (property 541475893 not in repo)"
else
  bad "GA4 placeholder constant missing or filled"
fi
if grep -q 'click_call' analytics-events.js && grep -q 'submit_lead_form' analytics-events.js; then
  ok "tel and form events present"
else
  bad "missing click or form events"
fi

echo
echo "=== Summary: $PASS passed, $FAIL failed ==="
if [ "$FAIL" -gt 0 ]; then exit 1; fi
