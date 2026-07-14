# Renter-Readiness Checklist

**Conversion verification phase:** 2026-07-11 — **live tests PASS**  
**Authority/citation research phase:** 2026-07-11 — **research complete** (no listings created)  
**Tier A duplicate inspection:** 2026-07-11 — **complete** (all six platforms)  
**Citation identity:** 2026-07-12 — **owner-approved** (see `citation-identity-approval-packet.md`)  
**Live conversion tests:** Complete — see `conversion-verification-checklist.md`  
**Technical lead-readiness:** **Yes** (call, form, GTM, GA4 verified)  
**Full renter-readiness:** **No** — citations, operator handoff, and proof-of-life lead volume still required

## Site quality

- [x] Claim-safe request-and-confirm copy sitewide
- [x] Trust/process sections on key pages
- [x] Hub IA (services, areas, guides)
- [x] Internal linking strengthened
- [x] Technical integrity verified locally (GTM, Formspree, tel, canonical)
- [x] Documentation in `docs/`
- [x] Live deployment verified (2026-07-11, PR #11–#13)
- [x] GSC baseline captured (2026-07-11)
- [x] CallRail routing confirmed on production (2026-07-11 live test)
- [x] Conversion events verified live (GTM Tag Assistant + GA4 Realtime)
- [ ] Real reviews/testimonials (placeholder acceptable for launch)

## Lead routing

- [x] Formspree endpoint configured (`mojzdkvg`)
- [x] Per-page `service` hidden field on 29 service pages
- [x] Homepage `service` dropdown on form
- [x] Static audit: `analytics-events.js` tracks `submit_lead_form` with market/niche/service
- [x] Live Formspree test submission confirmed (one controlled test — **not a real lead**)
- [x] `click_call` and `click_quote_button` confirmed in GTM/GA4
- [ ] Renter notified of lead flow
- [ ] Renter agreement / offer documented

## Conversion verification results (2026-07-11)

| Area | Result |
|---|---|
| Conversion path | **PASS** |
| Call path | **PASS** |
| Form path | **PASS** |
| GTM (`GTM-GDJF54DV` → `G-GWT8GR7QJC`) | **PASS** |
| GA4 Realtime (all 3 key events) | **PASS** |
| Duplicate-event check | **PASS** |
| CallRail routing | **PASS** — no configuration changes |
| Production code changes | **None required** |

## Authority / citation research (2026-07-11)

- [x] Citation identity sheet drafted — `citation-identity-sheet.md`
- [x] Citation identity approval packet — `citation-identity-approval-packet.md`
- [x] Platform candidate research with tiers A/B/C/Reject — `citation-candidate-research.md`
- [x] GBP eligibility review — **not eligible now** — `gbp-eligibility-review.md`
- [x] Local authority opportunities mapped — `local-authority-opportunities.md`
- [x] Content authority roadmap (GSC-driven) — `content-authority-roadmap.md`
- [x] Backlink research framework — `backlink-research-framework.md`
- [x] Citation tracker template prepared — `citation-tracker-template.md`
- [x] Tier A duplicate inspection — **complete** — `tier-a-duplicate-inspection.md`
- [x] ShowMeLocal human on-platform follow-up — no matching listing found
- [x] Owner approval of citation identity configuration — 2026-07-12
- [x] Account-owner strategy approved — Ryon O'Neill (lead-generation asset; private)
- [ ] Verified service provider identified for fulfilled jobs
- [x] Brownbook creation review completed — `brownbook-creation-review.md` (2026-07-12)
- [x] Brownbook pre-submission inspection completed (2026-07-12)
- [x] Brownbook field decisions approved — category, account email, account Name*
- [x] Brownbook account/listing creation approved for one automated attempt (2026-07-13)
- [x] Brownbook automated execution attempted and blocked by CAPTCHA (2026-07-13)
- [x] Brownbook account created manually by owner (2026-07-14)
- [x] Brownbook listing submitted manually by owner (2026-07-14)
- [x] Brownbook listing live and claimed (2026-07-14)
- [x] Public-name visibility owner-approved exception recorded
- [x] Any live citation submitted
- [x] Bing Places creation review completed in research/draft mode only (2026-07-14)
- [x] Bing Places duplicate recheck completed — no exact match
- [ ] Bing Places creation approved
- [ ] Legitimate private verification address confirmed for Bing Places
- [ ] Verified service provider / operating entity confirmed for Bing Places

## Remaining blockers (renter-readiness)

| Blocker | Status |
|---|---|
| Authority / citations | **Brownbook live and claimed**; Bing Places creation review complete but **deferred**; broader citation footprint still limited |
| GBP eligibility | **Blocked / not eligible now** |
| Service provider / renter operator | **Not established** — blocks Bing Places creation approval |
| Proof-of-life lead volume (real leads over time) | Not yet sufficient |
| Renter notification / agreement | Not started |
| Real reviews/testimonials | Placeholder acceptable; not yet added |
| Authority content clusters | Roadmap drafted — **publish pending approval** |

## Conversion test log

| Test date | Tester | Page | Device / browser | Event observed | CallRail result | Formspree result | GA4 result | Pass / fail | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2026-07-11 | RankRentOS | `/` | Desktop / Chrome | `click_call`, `click_quote_button`, `submit_lead_form` | Pass | Pass — test only | Pass — key events | Pass | Formspree success page confirmed |
| 2026-07-11 | RankRentOS | `/junk-removal-springfield-mo` | Desktop / Chrome | `click_call` | N/A | N/A | Pass | Pass | Money-page `page_path` correct |
| 2026-07-11 | RankRentOS | `/` | Mobile emulation | `click_call` | N/A | N/A | Pass | Pass | Mobile dialer behavior correct |

## GA4 account note (non-blocking)

- Unused property/tag `G-XPH099Y4DW` created during account recovery — not installed on site, not connected to production
- No action required in this batch
- Live site: `GTM-GDJF54DV` → `G-GWT8GR7QJC` only

## Compliance

- [x] No unverified license/insurance claims
- [x] No guaranteed same-day availability claims
- [x] Specialty services require confirmation language
- [x] Biohazard/hazmat not assumed on hoarder page

## Handoff materials

- [x] Page inventory
- [x] Claim correction log
- [x] Deployment QA checklist
- [x] Conversion verification checklist (live results recorded)
- [x] Citation/listing research plan (2026-07-11 — not executed)
- [ ] Citation submissions (awaiting owner + operator approval)
