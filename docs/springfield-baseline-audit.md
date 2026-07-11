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
| Deploy | PR #11 merged; Cloudflare success on `2006f8b` |
| Homepage | 200 OK |
| Sitemap URLs | 30/30 return 200 (after 308 redirect follow) |
| robots.txt / sitemap.xml | 200 OK |
| H1 per page | 1 on all 30 pages |
| Internal links | 691 local check, 0 broken |
| GTM / Formspree / tel / analytics | Verified on all HTML pages |
| Schema | LocalBusiness all pages; FAQPage where FAQ exists |

**Routing note:** Production serves 308 from `.html` to extensionless URLs. Full URL canonical-alignment (sitemap, canonical tags, Open Graph page URLs, JSON-LD page URLs, internal navigation) **prepared on branch `cursor/springfield-sitemap-canonical-alignment`, not deployed**. Local HTML source filenames remain `*.html`.

**GSC:** Property already set up — verify existing property, confirm sitemap status, capture baseline; do not create new property or submit indexing requests without approval.

Full record: `production-baseline-2026-07-11.md`

## Current phase

**Indexing + tracking verification + authority preparation** (mirrors Auburn post-launch workflow)

## Outstanding watch items

- Meta keywords still include SEO terms like `hoarding`, `demolition` — intentional for URL/search targeting, not body operator claims
- Same-day page retains FAQ question "Is same-day service guaranteed?" with explicit **No** answer
- Static HTML duplicates CSS per page — acceptable for current repo pattern; future refactor could extract shared stylesheet
- GSC baseline not yet captured in docs — verify existing property (do not create new)
- Full URL canonical-alignment prepared on branch — **not deployed**; local source filenames remain `*.html`
- Conversion tests (call/form) not yet run live — awaiting separate approval
- Citations: research prepared, zero live listings
