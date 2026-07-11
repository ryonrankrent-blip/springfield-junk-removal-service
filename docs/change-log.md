# Change Log

## 2026-07-11 — GSC baseline captured + Tier 1 indexing requests

### Production state
- Latest merge: PR #13 → `ef037f3` (hub JSON-LD fix deployed after PR #12 `57b7b8c`)
- Live sitemap: 30 unique extensionless URLs; 0 `.html` locs

### GSC baseline (verified 2026-07-11)
- Property: **existing verified domain property** — `springfieldjunkremovalservice.com`
- Sitemap: `https://springfieldjunkremovalservice.com/sitemap.xml` — submitted/read July 11, 2026; **Success**; **30 discovered pages**; extensionless URLs
- Performance (28d): 6 clicks, 4.64K impressions, 0.1% CTR, avg position 41.4
- Performance (7d): 2 clicks, 1.47K impressions, 0.1% CTR, avg position 40.9
- Page indexing: 37 indexed, 35 not indexed (14 redirect, 9 alternate canonical, 8 redirect error, 3 crawled-not-indexed, 1 discovered-not-indexed)
- Redirect-error examples are legacy `.html` URLs last crawled **before** July 11 canonical-alignment deploy — recheck after recrawl, not an active production defect

### Hub JSON-LD fix (PR #13)
- Three hub pages originally showed **unparsable structured data** (double-brace `{{` / `}}` delimiters)
- Fixed in PR #13 (`42c704d` → merge `ef037f3`); live production tests passed
- Indexing requests for the three hubs submitted successfully after fix

### Indexing actions (2026-07-11)
- **Already indexed (no request):** homepage, junk-removal-springfield-mo, furniture-removal-springfield-mo, commercial-junk-removal-springfield-mo
- **Indexing requested:** junk-removal-services-springfield-mo, junk-removal-guides-springfield-mo, junk-removal-service-areas-springfield-mo, appliance-removal-springfield-mo, house-cleanout-springfield-mo, estate-cleanout-springfield-mo, construction-debris-removal-springfield-mo, yard-waste-removal-springfield-mo
- **Recheck window:** July 18–25, 2026

### Proof-of-life assessment
- Technically live, indexed, receiving impressions/clicks, early rankings visible
- **Not yet renter-ready:** call/form conversion verification and authority/citation work incomplete

### Not performed
- No additional indexing requests beyond the eight above
- No DNS/routing/tracking changes, citations, listings, renter outreach, sitemap resubmit

### Documentation updated
- `indexing-priority-tracker.md` — GSC baseline + Tier 1/2 inspection table
- `proof-of-life-weekly-tracker.md` — week ending 2026-07-11 row
- `proof-of-life-checklist.md` — search visibility checklist progress
- `springfield-baseline-audit.md` — phase + GSC status
- `change-log.md` — this entry

---

## 2026-07-11 — Hub JSON-LD fix deployed (PR #13)

### Deployed
- Merged PR #13 to `main` — merge commit `ef037f3ba4765ac76e76b2ec90e0b13f1cd30824`
- Cloudflare Pages production deployment — success
- Fixed invalid double-brace JSON-LD delimiters on three hub pages only

### Files changed
- `junk-removal-services-springfield-mo.html`
- `junk-removal-guides-springfield-mo.html`
- `junk-removal-service-areas-springfield-mo.html`

### Protected values (unchanged)
- Phone, Formspree, GTM, analytics-events.js, canonicals, visible copy, layout

---

## 2026-07-11 — URL canonical alignment deployed (PR #12)

### Deployed
- Merged PR #12 to `main` — merge commit `57b7b8c897d8f84ab273aceee6d5e9321a398506`
- Cloudflare Pages production deployment — success
- `sitemap.xml`, canonical tags, `og:url`, JSON-LD page URLs, and internal navigation aligned to extensionless URLs
- Local HTML source filenames remain `*.html`

### Protected values (unchanged)
- Phone, Formspree, GTM, analytics-events.js, canonical domain

### External systems (unchanged)
- DNS, CallRail routing, GA4/GTM config, citations, listings, renter outreach

---

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

### Known routing note (resolved PR #12)
- Cloudflare 308: `.html` paths → extensionless URLs (preserved)
- Sitemap, canonicals, and internal links now aligned to extensionless 200 destinations

### Sitemap canonical-alignment — deployed PR #12
- Merge commit `57b7b8c` — see PR #12 section above

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
