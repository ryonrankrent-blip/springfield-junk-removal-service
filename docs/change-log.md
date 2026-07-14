# Change Log

## 2026-07-14 — Bing Places creation review completed

### Production state
- Main commit: `09331c2` (PR #24 Brownbook listing-completion documentation merge)
- No HTML, scripts, tracking, DNS, routing, forms, or production configuration changes

### Research and draft outcome
- **Bing Places status:** Creation review complete — **creation deferred**
- **Duplicate recheck:** No exact match found for approved name, domain, or phone
- **Current fit:** Suitable only after specific missing information is resolved
- **Creation authorization:** Not granted in this batch

### Key requirements recorded
- Bing Places supports service-area businesses and hidden public addresses
- A legitimate private verification address appears required before creation/verification
- Verification methods may include phone, email, postcard/mail, or other options, but are controlled by Bing Places
- Exact live category label for junk removal remains unresolved until owner-approved live review
- Google Business Profile import is offered by Bing Places but remains inappropriate because GBP is blocked / not eligible now

### Not performed
- No Bing Places account created or signed into
- No Microsoft or Google account connected
- No Google Business Profile import
- No listing created, claimed, edited, submitted, or verified
- No address, private contact information, support request, payment, advertising, commit, push, or deploy action

### Documentation updated
- `bing-places-creation-review.md`
- `citation-tracker-template.md`
- `citation-candidate-research.md`
- `renter-readiness-checklist.md`
- `change-log.md` (this entry)

---

## 2026-07-14 — Brownbook listing live and claimed

### Production state
- Main commit: `ee89700` (PR #23 Brownbook CAPTCHA blocker documentation merge)
- No HTML, scripts, tracking, DNS, routing, forms, or production configuration changes

### Owner-confirmed execution result
- **Brownbook status:** **Live and claimed**
- **Citation creation:** **Complete**
- **Manual owner-browser execution:** **Successful**
- **Duplicate risk:** None
- **Listing URL:** Not provided in owner confirmation; record when available
- **No further Brownbook edits authorized** in this batch
- **GBP:** Remains blocked / not eligible now

### Public fields confirmed
- Business name: Springfield Junk Removal Service
- Category: Other Waste Collection
- City / country: Springfield, United States
- Phone: (417) 242-5370
- Website: https://springfieldjunkremovalservice.com
- Street address, postal code, public listing email, and hours: blank
- Description: approved claim-safe language added
- Logo/photos: none uploaded

### Public-name exception
- Ryon O'Neill is visible publicly on the Brownbook account/listing interface.
- Owner reviewed and explicitly accepted this, consistent with the owner's Auburn Septic citation-account approach.
- This is an owner-approved exception to the earlier public-name stop condition and must not be interpreted as a claim that Ryon O'Neill personally performs hauling, operates crews, owns trucks, or directly fulfills junk-removal services.

### Not performed
- No paid upgrade, Profile+, advertising, partner enrollment, billing, outreach, DNS, routing, tracking, form, code, commit, push, or deploy action
- No license, insurance, crew, truck, years-in-business, locally owned, family-owned, or direct-service claims added
- No logo, photos, public email, hours, street address, or postal code added

### Documentation updated
- `brownbook-creation-review.md`
- `citation-tracker-template.md`
- `citation-candidate-research.md`
- `renter-readiness-checklist.md`
- `change-log.md` (this entry)

---

## 2026-07-13 — Brownbook automated execution blocked by CAPTCHA

### Production state
- Main commit: `aae9062` (PR #22 Brownbook pre-submission decisions merge)
- No HTML, scripts, tracking, DNS, routing, forms, or production configuration changes

### Execution outcome recorded
- **Brownbook automated execution:** **Blocked**
- **Blocker:** CAPTCHA could not be completed normally
- **Platform suitability:** Still viable
- **Automated retry:** Not authorized
- **Recommended next step:** Optional single manual owner-browser attempt
- **Listing creation status:** Not completed

### Attempt details
- Duplicate recheck found no exact duplicate listing
- Passive promotions were present but optional; no payment, subscription, trial, or mandatory partner enrollment appeared
- Step 1 fields were prepared using the approved configuration
- Step 2 account fields were filled temporarily but never submitted
- One normal reCAPTCHA checkbox attempt was made; CAPTCHA remained unchecked and Next remained disabled
- No second CAPTCHA or submission attempt was made
- All unsubmitted account fields were cleared

### Not performed
- No Brownbook account created
- No email verification occurred
- No listing submitted, published, claimed, edited, enriched, or verified
- No owner name, private address, or private email became public
- No outreach, spend, DNS, routing, tracking, form, code, commit, push, or deploy action

### Documentation updated
- `brownbook-creation-review.md`
- `citation-tracker-template.md`
- `renter-readiness-checklist.md`
- `change-log.md` (this entry)

---

## 2026-07-12 — Brownbook pre-submission inspection documented (read-only)

### Production state
- Main commit: `5486caa` (PR #21 Brownbook creation review merge)
- No HTML, scripts, tracking, DNS, or production configuration changes

### Inspection and owner decisions recorded
- **Pre-submission inspection:** complete 2026-07-12 (live add-business workflow)
- **Category approved:** Other Waste Collection (NAICS reference 562119; Brownbook shows label + breadcrumb only)
- **Private account email approved:** private account email not documented here (account/login only — not registered)
- **Account Name* approved:** Ryon O'Neill (private registration as asset owner and authorized representative)
- **Public listing email:** leave blank
- **Public address:** leave blank; city Springfield; country United States
- **Description / logo:** defer
- **Account creation, listing submission, claiming, verification:** **not authorized**

### Key live findings
- No Junk Removal Service, Junk Removal, or Debris Removal category labels in typeahead
- Step 1 Next advances to account creation only — does not publish listing
- Step 2 requires email, password, password confirm, Name, terms, reCAPTCHA; email verification after registration
- Listing email is public when entered — must remain blank
- Account-name public exposure unconfirmed; claim-name visibility unresolved
- reCAPTCHA quota warning observed — possible execution blocker
- No account created; no credentials entered; no listing published

### Not performed
- No Brownbook account, listing, claim, verification, CAPTCHA completion, or spend
- No commit, push, or deploy in this batch (pending owner approval)

### Documentation updated
- `brownbook-creation-review.md`
- `citation-identity-approval-packet.md`
- `citation-tracker-template.md`
- `citation-candidate-research.md`
- `renter-readiness-checklist.md`
- `change-log.md` (this entry)

---

## 2026-07-12 — Brownbook creation review (read-only)

### Production state
- Main commit: `dc97558` (PR #20 owner-approved identity configuration merge)
- No HTML, scripts, tracking, DNS, or production configuration changes

### Review completed
- **Brownbook policy reverified** on live add-business form, terms, about, register, and free-claim pages (2026-07-12)
- **Duplicate status reconfirmed:** 0 results for approved name, domain, phone
- **Claim-safe draft** prepared from owner-approved identity sheet
- **Suitability:** suitable only after specific missing information is resolved
- **Creation approval:** deferred — listing creation not authorized

### Key findings
- Add-business URL: https://www.brownbook.net/add-business (step 1 of 2)
- Required fields: business name, NAICS category, country — **address optional**
- Free basic listing + free claim; paid Profile+ optional
- Account + email verification required to claim and lock edits
- Description / Business overview supported; hours not on step 1
- Terms allow authorized representatives/agents; 5-listing SEO commercial limit N/A for single asset
- Unresolved before submission: exact NAICS category label, private account email, claim UI name privacy, step 2 reverify at submit

### Not performed
- No Brownbook account, login, listing create/claim/edit/submit/verify
- No address entry, private contact entry, image upload, support contact, or spend
- No commit, push, or deploy in this batch (pending owner approval)

### Documentation updated
- `brownbook-creation-review.md` (new)
- `citation-tracker-template.md`
- `citation-candidate-research.md`
- `renter-readiness-checklist.md`
- `change-log.md` (this entry)

---

## 2026-07-12 — Citation identity owner decisions approved

### Production state
- Main commit: `a494e92` (PR #19 citation identity approval packet merge)
- No HTML, scripts, tracking, DNS, or production configuration changes

### Owner decisions approved
- **Public identity:** Springfield Junk Removal Service; (417) 242-5370; https://springfieldjunkremovalservice.com; no public address; Springfield + Greene County service area
- **Category policy:** Junk Removal Service primary; one closely related secondary at most
- **Omit:** hours, public email, public owner name (unless platform requires)
- **Descriptions:** request-and-confirm language only; approved short/long drafts
- **Images:** bundled site icon/logo assets only
- **Platform decisions:** Facebook defer; Nextdoor defer; GBP blocked
- **First creation-review candidate:** Brownbook (separate task — not creation-authorized)

### Account-owner strategy approved
- **Private account owner / authorized representative:** Ryon O'Neill (lead-generation asset)
- **Not established as:** hauling contractor, service provider, dispatcher, crew operator, or field operator
- **Do not publish:** personal address, private phone, personal email
- **Public fields:** approved public business identity only

### Operational facts still unresolved
- Verified hauling / service-provider business or entity
- Local field operator / renter handoff
- Legitimate private verification address (where required)
- License, insurance, crews, trucks, years in business

### Not performed
- No listings created, claimed, edited, submitted, or verified
- No Brownbook login or creation review
- No commit, push, or deploy in this batch (pending approval)

### Documentation updated
- `citation-identity-approval-packet.md`
- `citation-identity-sheet.md`
- `citation-tracker-template.md`
- `renter-readiness-checklist.md`
- `change-log.md` (this entry)

---

## 2026-07-11 — ShowMeLocal human follow-up (read-only)

### Production state
- Main commit: `95eb46a` (PR #17 Tier A duplicate inspection merge)
- No HTML, scripts, tracking, DNS, or production configuration changes

### Follow-up completed
- **ShowMeLocal human on-platform search** — public browser session; read-only
- **Queries checked:** `Springfield Junk Removal Service` + Springfield, MO; `springfieldjunkremovalservice.com` + Springfield, MO; `417-242-5370` + Springfield, MO; `junk removal` + Springfield, MO
- **Result:** No matching listing; no exact match; no possible match; no identity conflict
- **Tier A status:** Duplicate inspection now **complete across all six platforms**

### Key findings
- **ShowMeLocal final status:** No result
- **Duplicate risk:** None (upgraded from inconclusive/low)
- **Exact matches:** 0
- **Possible matches:** 0
- **Identity conflicts:** none
- **Listing creation:** not authorized
- **GBP:** not eligible now

### Not performed
- No account login, claim, edit, verification request, or listing creation
- No production, renter, or support contact
- No commit, push, or deploy in this batch (pending approval)

### Documentation updated
- `tier-a-duplicate-inspection.md`
- `citation-candidate-research.md`
- `citation-tracker-template.md`
- `authority-gap-review.md`
- `renter-readiness-checklist.md`
- `change-log.md` (this entry)

---

## 2026-07-11 — Tier A citation duplicate inspection (read-only)

### Production state
- Main commit: `7eeaf73` (PR #16 authority research merge)
- No HTML, scripts, tracking, DNS, or production configuration changes

### Inspection completed
- **Tier A duplicate inspection** — read-only public search across Bing Places, ShowMeLocal, Yelp, Facebook, Nextdoor, Brownbook
- **General web search** — approved business name, domain, and phone
- **Result:** 0 exact matches, 0 possible matches (≥2 identifiers), 0 identity conflicts
- **Identity sheet:** unchanged (`citation-identity-sheet.md`)

### Key findings
- **Bing Places:** No listing for approved name, phone, or domain; unrelated MO competitors visible on Maps
- **ShowMeLocal:** No indexed matches; on-platform search blocked by bot protection — follow-up needed
- **Yelp / Facebook / Nextdoor:** No indexed listings for approved identifiers
- **Brownbook:** Direct search returned 0 for name, domain, and phone
- **Unrelated collisions:** springfieldjunkremoval.com (MA), springfieldjunkremoval.org, springfieldjunkremovalco.com (different phone), 417 Junk and Debris, etc.

### Not performed
- No listings created, claimed, edited, or verified
- No platform logins, claims, address entry, or spend
- No production, renter, or support contact
- No commit, push, or deploy in this batch (pending approval)

### Documentation created/updated
- `tier-a-duplicate-inspection.md` (new)
- `citation-tracker-template.md` (updated — Tier A status → Inspected)
- `citation-candidate-research.md` (updated — inspection results)
- `authority-gap-review.md` (updated)
- `renter-readiness-checklist.md` (updated)
- `change-log.md` (this entry)

---

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
