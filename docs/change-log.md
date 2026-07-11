# Change Log

## 2026-07-11 — Production deploy (PR #11)

### Deployed
- Merged PR #11 to `main` — merge commit `2006f8bc8baff01a9c8c050be72e893d07473ccf`
- Cloudflare Pages production deployment — success
- Live site: https://springfieldjunkremovalservice.com
- 30 sitemap URLs verified live (200 after redirect follow)

### Protected values (unchanged)
- Phone: (417) 242-5370 / `tel:4172425370`
- Formspree: `mojzdkvg`
- GTM: `GTM-GDJF54DV`
- Canonical domain: springfieldjunkremovalservice.com
- `analytics-events.js` event hooks

### External systems (unchanged)
- DNS, CallRail routing, GA4/GTM config, citations, listings, renter outreach

### Known routing note
- Cloudflare 308: `.html` sitemap locs → extensionless canonical URLs (non-blocking; recommended sitemap/canonical alignment in separate approved production change)

### Documentation correction (pre-commit)
- Indexing tracker URLs updated to extensionless canonical form
- GSC workflow corrected for existing property
- Citation guardrails strengthened (planning research only)

### Post-deploy documentation added (local, not committed)
- `production-baseline-2026-07-11.md`
- `conversion-verification-checklist.md`
- `proof-of-life-weekly-tracker.md`
- `citation-candidate-research.md`
- `authority-gap-review.md`
- Updated indexing, deployment QA, proof-of-life checklists

---

## 2026-07-11 — RankRentOS claim-safe + hub IA batch

### Added
- 3 hub pages: services, service areas, guides
- `docs/` folder (11 documentation files)
- `scripts/qa-check.sh`, `scripts/link-check.sh`, `scripts/fix-claims.py`, `scripts/create-hubs.py`, cleanup passes

### Changed
- All 27 existing HTML pages: claim-safe copy, trust sections, hub links
- `sitemap.xml`: 27 → 30 URLs
- `README.md`: project overview and QA instructions

### Unchanged (by design)
- Phone, Formspree, GTM, analytics-events.js, canonical domain
- All existing page URLs preserved
- `hoarder-cleanout-springfield-mo.html` URL retained

### Not performed
- No commit, push, deploy, DNS, CallRail, citations, or external account changes
