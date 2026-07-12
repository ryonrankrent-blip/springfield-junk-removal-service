# Change Log

## 2026-07-11 — Authority and citation research phase (research only)

### Production state
- Main commit: `4d5d955` (PR #15 docs merge)
- No HTML, scripts, tracking, DNS, or production configuration changes

### Research completed
- **Citation identity sheet** — proposed NAP, descriptions, services, assets; address blank; owner-approval flags
- **Citation candidate research** — 20+ platforms reviewed with current policy sources; tiers A/B/C/Reject
- **GBP eligibility review** — recommendation: **not eligible now** (lead-gen model; no verified operator/address)
- **Local authority opportunities** — Springfield city/county disposal, recycling, donation, hazmat resources mapped
- **Content authority roadmap** — GSC-driven clusters for construction debris, commercial, yard waste, cost, items, cleanouts
- **Backlink research framework** — read-only SERP/citation/backlink process with scoring matrix
- **Citation tracker template** — submission tracker with approval column (all blank)
- **Authority gap review** — updated post-conversion status

### Key findings
- **Tier A (first inspection batch):** Bing Places, ShowMeLocal, Yelp, Facebook Page, Nextdoor, Brownbook
- **Tier B (defer):** GBP, Apple Business Connect, YP/MapQuest, Foursquare, BBB, Chamber
- **Reject:** Angi, HomeAdvisor, Thumbtack paid leads; fake/virtual addresses; lead aggregators
- Springfield remains **technically lead-ready** but **not fully renter-ready**

### Not performed
- No listings created or claimed
- No GBP, Bing, Yelp, or any platform submission
- No outreach, spend, renter contact, or content publish
- No commit, push, or deploy in this batch

### Documentation created/updated
- `citation-identity-sheet.md` (new)
- `gbp-eligibility-review.md` (new)
- `local-authority-opportunities.md` (new)
- `content-authority-roadmap.md` (new)
- `backlink-research-framework.md` (new)
- `citation-candidate-research.md` (updated)
- `citation-tracker-template.md` (updated)
- `authority-gap-review.md` (updated)
- `renter-readiness-checklist.md` (updated)
- `change-log.md` (this entry)

---

## 2026-07-11 — Conversion verification live tests complete (PASS)

### Production state
- Main commit tested: `c0573a1` (PR #14 docs merge)
- No production HTML, scripts, or configuration changes required or made

### Live test results (2026-07-11)
- **Conversion path:** PASS — call, quote, and form paths verified end-to-end
- **Call path:** PASS — desktop homepage, money page (`/junk-removal-springfield-mo`), and mobile `tel:` dialer behavior correct; `click_call` with correct `page_path`
- **Form path:** PASS — one controlled Formspree test submission; hosted success page ("Thanks! The form was submitted successfully."); `submit_lead_form` fired once; **test not counted as a real lead**; no second submission
- **GTM:** PASS — Tag Assistant connected to `GTM-GDJF54DV`; GA4 destination `G-GWT8GR7QJC`; GA4 Google Tag fired once; `click_call`, `click_quote_button`, and `submit_lead_form` tags each fired once per tested action; Tags Not Fired: None
- **GA4:** PASS — correct Springfield property under RankRentOS account; Realtime received all three events as key events; traffic and page views present; event totals reflected deliberate test actions, not duplicate firing
- **CallRail:** PASS — `(417) 242-5370` routing verified; call appeared in dashboard; logging correct; no routing/voicemail/forwarding/recording changes
- **Duplicate-event check:** PASS — no duplicate custom-event firing in Tag Assistant
- **Mobile:** PASS — `tel:` link opened dialer correctly
- **Quote button:** PASS — `Get a Free Quote` moved to `#quote`; `click_quote_button` fired once per action

### GA4 account note (non-blocking)
- Unused property/tag `G-XPH099Y4DW` accidentally created during account recovery
- Not installed on site; not connected to production; no action required
- Live site remains on `GTM-GDJF54DV` → `G-GWT8GR7QJC` only

### Assessment
- Springfield is **technically lead-ready**
- **Not fully renter-ready** until authority/citation work and sufficient proof-of-life lead volume are completed

### Not performed
- No production file changes, commit, push, or deploy
- No GTM publish, GA4 config changes, Formspree settings changes, or CallRail routing changes
- No citations, listings, or renter outreach

### Documentation updated
- `conversion-verification-checklist.md` — live results, test log, sign-off table
- `proof-of-life-checklist.md` — conversion and CallRail sections marked PASS
- `renter-readiness-checklist.md` — lead-routing verified; renter blockers updated
- `change-log.md` — this entry

---

## 2026-07-11 — Conversion verification phase started (read-only audit)

### Production state
- Main commit audited: `c0573a1` (PR #14 docs merge)
- Production HTML/tracking unchanged since PR #13 (`ef037f3`)

### Read-only conversion audit
- Reviewed `analytics-events.js` and all 30 HTML pages
- **Custom events:** `click_call`, `click_quote_button`, `submit_lead_form` (no others)
- **Static validation:** 30/30 pass — `tel:4172425370`, Formspree `mojzdkvg`, GTM `GTM-GDJF54DV`, `analytics-events.js`, `#quote` CTAs
- **Listener model:** Single delegated document listeners; no duplicate script tags or inline `onclick`
- **Form fields:** Hidden `site`, `market`, `niche` on all pages; hidden `service` on 29 service pages; homepage uses `select name="service"`
- **Post-submit UX:** No `_next` redirect in HTML — Formspree dashboard behavior TBD on live test

### Manual test plan prepared (not run)
- Desktop/mobile call click, quote-button click, safe form submit, GTM Preview, dataLayer, GA4 Realtime/DebugView, duplicate-event check, CallRail read-only verification
- Blank test-log fields added to conversion docs

### Not performed
- No live calls, form submissions, GTM Preview, GA4 sessions
- No production file changes, commit, push, or deploy
- No CallRail, Formspree, GTM, or GA4 configuration changes

### Documentation updated
- `conversion-verification-checklist.md` — audit findings + manual test procedures + test log
- `proof-of-life-checklist.md` — conversion verification section
- `renter-readiness-checklist.md` — conversion blockers + test log
- `change-log.md` — this entry

---

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
