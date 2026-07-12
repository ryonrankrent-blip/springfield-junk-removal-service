# Proof-of-Life Checklist

Run after deployment to confirm the live site is functional.

**Production deploy:** 2026-07-11 (PR #11 `2006f8b`; PR #12 `57b7b8c` URL alignment; PR #13 `ef037f3` hub JSON-LD fix)  
**GSC baseline:** 2026-07-11 (verified)  
**Conversion verification:** 2026-07-11 — **live tests PASS**  
**Recheck window:** July 18–25, 2026  
**Weekly tracking:** `proof-of-life-weekly-tracker.md`  
**Conversion tests:** `conversion-verification-checklist.md`

## Core functionality

- [x] Homepage loads over HTTPS
- [x] All 30 sitemap URLs load (200 after redirect)
- [x] Static audit: `tel:4172425370` present on all 30 pages (5–8 links/page)
- [x] Static audit: Formspree `mojzdkvg` on all 30 forms; hidden `site`, `market`, `niche` present
- [x] Static audit: GTM `GTM-GDJF54DV` + `analytics-events.js` on all 30 pages
- [x] Static audit: quote CTAs use `Get a Free Quote` → `#quote` on all 30 pages
- [x] Phone link works on mobile (live tap) — dialer opened with `(417) 242-5370`
- [x] Quote form submits to Formspree (live test) — one controlled test; hosted success page
- [x] `click_call` / `click_quote_button` / `submit_lead_form` verified in GTM Tag Assistant

## Hub pages (live — extensionless canonical URLs)

- [x] `/junk-removal-services-springfield-mo` returns 200
- [x] `/junk-removal-service-areas-springfield-mo` returns 200
- [x] `/junk-removal-guides-springfield-mo` returns 200

## SEO files

- [x] `/sitemap.xml` lists 30 URLs
- [x] `/robots.txt` references sitemap
- [x] Favicon tags present in HTML

## Spot-check pages (live copy)

- [x] Homepage hub links present
- [x] Homepage corrected copy visible (claim-safe cards)
- [x] Money page loads
- [x] Hot tub page — scope confirmation language in production HTML
- [x] Hoarder page — heavy-clutter + hazmat disclaimer visible

## Conversion verification (live — 2026-07-11)

- [x] `analytics-events.js` reviewed — 3 custom events: `click_call`, `click_quote_button`, `submit_lead_form`
- [x] Delegated listeners only — no duplicate script tags or inline `onclick` handlers
- [x] Homepage uses `select name="service"`; service pages use hidden `service` field
- [x] Post-submit UX verified — Formspree hosted success page ("Thanks! The form was submitted successfully.")
- [x] Desktop call-click test — **PASS** (homepage + money page; correct `page_path`)
- [x] Mobile call-tap test — **PASS** (dialer opened correctly)
- [x] Quote-button click test — **PASS** (`#quote` navigation + `click_quote_button`)
- [x] Safe test form submission — **PASS** (one test; not counted as real lead)
- [x] GTM Tag Assistant — **PASS** (`GTM-GDJF54DV` → `G-GWT8GR7QJC`; all tags fired)
- [x] GA4 Realtime — **PASS** (all 3 events received as key events)
- [x] Duplicate-event detection — **PASS** (no duplicate custom events in Tag Assistant)

## CallRail (verified — no configuration changes)

- [x] Website calls route to expected tracking number `(417) 242-5370`
- [x] Controlled live call — routing worked as configured; call appeared in CallRail
- [x] Logging/status behavior correct
- [x] No routing, voicemail, forwarding, or recording changes made
- [x] Call events appear in analytics pipeline (`click_call` confirmed in GTM + GA4)

## Search visibility (verified 2026-07-11)

- [x] DNS `google-site-verification` TXT present on apex domain
- [x] Existing Google Search Console **domain property** verified — `springfieldjunkremovalservice.com`
- [x] Sitemap submitted — `https://springfieldjunkremovalservice.com/sitemap.xml`; **Success**; 30 discovered pages; read July 11, 2026
- [x] Page Indexing baseline captured — 37 indexed, 35 not indexed
- [x] Performance baseline captured — 28d: 4.64K imp / 6 clicks / 0.1% CTR / pos 41.4; 7d: 1.47K imp / 2 clicks / 0.1% CTR / pos 40.9
- [x] Tier 1 extensionless canonical URLs inspected — see `indexing-priority-tracker.md`
- [x] Hub JSON-LD unparsable structured data fixed (PR #13) and live-verified
- [x] Indexing requests submitted for eight approved URLs (2026-07-11) — see tracker
- [x] Week-1 metrics recorded in `proof-of-life-weekly-tracker.md`
- [ ] Recheck indexing status — **July 18–25, 2026**
- [ ] Additional indexing requests — **not performed; requires separate approval**

## Proof-of-life assessment (2026-07-11)

| Signal | Status |
|---|---|
| Technically live | Yes — 30/30 URLs, HTTPS, extensionless canonicals |
| Indexed | Yes — 37 pages indexed in GSC |
| Impressions / clicks | Yes — 4.64K impressions / 6 clicks (28d); early query signals visible |
| Early rankings | Yes — e.g. construction debris ~5.9, commercial junk ~15.7, yard waste 1 click @ 10.0 |
| Conversion path verified | Yes — call, quote, and form paths PASS (2026-07-11 live tests) |
| Technically lead-ready | **Yes** — GTM, GA4, Formspree, and CallRail verified |
| Renter-ready | **No** — authority/citation work and sufficient proof-of-life lead volume still incomplete |

### GA4 account note (non-blocking)

- Unused property/tag `G-XPH099Y4DW` created during account recovery — not installed, not connected to production; no action required
- Live site uses `GTM-GDJF54DV` → `G-GWT8GR7QJC` only

## Conversion test log

| Test date | Tester | Page | Device / browser | Event observed | CallRail result | Formspree result | GA4 result | Pass / fail | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2026-07-11 | RankRentOS | `/` | Desktop / Chrome | `click_call`, `click_quote_button`, `submit_lead_form` | Pass | Pass — test only | Pass — key events | Pass | No production code changes required |
| 2026-07-11 | RankRentOS | `/junk-removal-springfield-mo` | Desktop / Chrome | `click_call` | N/A | N/A | Pass | Pass | Correct `page_path` |
| 2026-07-11 | RankRentOS | `/` | Mobile emulation | `click_call` | N/A | N/A | Pass | Pass | Dialer opened correctly |
