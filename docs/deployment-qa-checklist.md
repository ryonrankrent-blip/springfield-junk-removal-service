# Deployment QA Checklist

## Pre-deploy

- [x] Run `./scripts/qa-check.sh` — all checks pass (216 passed, 0 failed)
- [x] Run `./scripts/link-check.sh` — no broken internal links (691 checked)
- [x] Verify sitemap = 30 URLs
- [x] Spot-check 10 priority pages locally
- [x] PR #11 reviewed and approved
- [x] Confirm protected values unchanged (phone, Formspree, GTM, canonical)

## Deploy steps — completed 2026-07-11

- [x] Merge PR #11 to `main` (`2006f8b`)
- [x] Cloudflare Pages production deploy — success
- [x] Verify HTTPS certificate (live)
- [x] No CDN purge required (auto-deploy from main)

## Post-deploy — production verified 2026-07-11

- [x] Homepage loads over HTTPS (200)
- [x] All 30 sitemap URLs return 200 (after 308 redirect follow where applicable)
- [x] `robots.txt` returns 200 with sitemap reference
- [x] `sitemap.xml` lists 30 URLs
- [x] Canonical URLs use `springfieldjunkremovalservice.com`
- [x] Phone `tel:4172425370` on all pages
- [x] Formspree `mojzdkvg` on all form pages
- [x] GTM `GTM-GDJF54DV` on all pages
- [x] `analytics-events.js` on all pages
- [x] Mobile viewport meta on all pages
- [x] 1 H1 per page confirmed live
- [ ] Run proof-of-life checklist (conversion tests — **awaiting separate approval**)
- [ ] Test form submission end-to-end (**awaiting separate approval**)
- [ ] Test phone click on mobile (**awaiting separate approval**)
- [ ] Verify GTM preview mode events (**awaiting separate approval**)
- [ ] Verify existing GSC property and sitemap status (read-only — do not submit)

## Known sitemap / canonical alignment note

The live `sitemap.xml` lists `.html` URLs that **308-redirect** to extensionless canonical URLs.

| Classification | Detail |
|---|---|
| Live site | **Non-blocking** — final pages return 200 |
| Cleanup | **Recommended** — align sitemap locs to extensionless 200 URLs in a **separate approved production change** |
| This batch | Do not edit `sitemap.xml` |

Inspect GSC using extensionless canonical URLs per `indexing-priority-tracker.md`.

## GSC workflow (existing property)

- [ ] Verify existing Search Console property (do not create new)
- [ ] Confirm current sitemap submission status (read-only)
- [ ] Capture Page Indexing baseline
- [ ] Inspect Tier 1 extensionless canonical URLs
- [ ] Request indexing only after separate approval

## External systems — unchanged

- [x] DNS — not changed
- [x] CallRail routing — not changed
- [x] Formspree endpoint — not changed
- [x] GTM / GA4 container — not changed
- [x] Citations / listings — not created

## Rollback triggers

- Formspree submissions fail
- GTM container missing
- Broken phone link
- Unsupported operator claims reappear on live site

## Reference

- Production baseline: `docs/production-baseline-2026-07-11.md`
- Conversion tests: `docs/conversion-verification-checklist.md`
