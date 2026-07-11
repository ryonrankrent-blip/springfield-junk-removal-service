# Springfield Baseline Audit

**Date:** 2026-07-11  
**Site:** springfieldjunkremovalservice.com  
**Batch:** RankRentOS claim-safe + hub IA pass

## Summary

Converted 27 existing pages to claim-safe request-and-confirm language, added 3 hub pages (30 total), standardized trust/process sections, strengthened internal linking, and added QA tooling plus documentation.

## Technical baseline (unchanged)

| Item | Status |
|---|---|
| GTM `GTM-GDJF54DV` | OK — 2 hits/page |
| Formspree `mojzdkvg` | OK — all forms |
| Phone `tel:4172425370` | OK — all pages |
| `analytics-events.js` | OK — all pages |
| Canonical domain | OK |
| `robots.txt` | OK |
| Favicon tags | OK — all pages |

## IA changes

- Added `junk-removal-services-springfield-mo.html` (services hub)
- Added `junk-removal-service-areas-springfield-mo.html` (service areas hub)
- Added `junk-removal-guides-springfield-mo.html` (guides hub)
- Homepage links to all 3 hubs
- `sitemap.xml` updated to 30 URLs

## Claim-risk remediation

| Risk category | Before (approx.) | After |
|---|---|---|
| Operator verbs (we haul/load/handle/clear) | 120+ | 0 |
| Crew/truck claims | 13 | 0 |
| Disconnect/demolition operator claims | 36 | Scoped to quote confirmation |
| Donation/recycling guarantees | 36 | Conditional language |
| Hoarding specialization | 21 | Heavy clutter + hazmat disclaimer |
| Licensed/insured | 0 | 0 |

## Reusability

Market-specific values live in page comments and Formspree hidden fields. Reusable patterns documented in `reusable-patterns.md`. Scripts in `scripts/` can be adapted for future niches/locations.

## Production baseline (2026-07-11)

| Item | Live status |
|---|---|
| Deploy | PR #11 `2006f8b` + PR #12 `57b7b8c` + PR #13 `ef037f3` merged; Cloudflare success |
| Homepage | 200 OK |
| Sitemap URLs | 30/30 extensionless; 0 `.html` locs |
| robots.txt / sitemap.xml | 200 OK |
| H1 per page | 1 on all 30 pages |
| Internal links | 691 local check, 0 broken |
| GTM / Formspree / tel / analytics | Verified on all HTML pages |
| Schema | LocalBusiness all pages; FAQPage where FAQ exists |

**Routing:** Cloudflare serves 308 from `.html` to extensionless URLs. Full URL canonical-alignment **deployed** (PR #12, `57b7b8c`).

**GSC:** Existing **verified domain property** (`springfieldjunkremovalservice.com`). Baseline captured 2026-07-11:

| Item | Value |
|---|---|
| Sitemap | Success; 30 discovered; read July 11, 2026; extensionless URLs |
| Performance (28d) | 6 clicks, 4.64K impressions, 0.1% CTR, avg position 41.4 |
| Performance (7d) | 2 clicks, 1.47K impressions, 0.1% CTR, avg position 40.9 |
| Page indexing | 37 indexed, 35 not indexed |
| Notable exclusions | 14 redirect, 9 alternate canonical, 8 redirect error, 3 crawled-not-indexed, 1 discovered-not-indexed |
| Redirect errors | Legacy `.html` URLs crawled pre-PR #12 — recheck after recrawl, not active production defect |
| Hub JSON-LD | Unparsable structured data on 3 hubs → fixed PR #13 (`ef037f3`); live tests passed |
| Indexing requests | 8 URLs submitted 2026-07-11 (3 hubs + 5 service pages) |
| Recheck window | July 18–25, 2026 |

Full record: `production-baseline-2026-07-11.md`, `indexing-priority-tracker.md`

## Current phase

**Post-baseline monitoring + conversion verification + authority preparation**

Proof-of-life: technically live, indexed, receiving impressions/clicks, early rankings visible. **Not yet renter-ready** — call/form conversion verification and authority/citation work incomplete.

## Outstanding watch items

- Meta keywords still include SEO terms like `hoarding`, `demolition` — intentional for URL/search targeting, not body operator claims
- Same-day page retains FAQ question "Is same-day service guaranteed?" with explicit **No** answer
- Static HTML duplicates CSS per page — acceptable for current repo pattern; future refactor could extract shared stylesheet
- Recheck GSC indexing for eight requested URLs — **July 18–25, 2026**
- Monitor legacy `.html` redirect-error coverage clearing after PR #12 recrawl
- Conversion tests (call/form) not yet run live — awaiting separate approval
- Citations: research prepared, zero live listings
- Additional indexing requests — **require separate approval**
