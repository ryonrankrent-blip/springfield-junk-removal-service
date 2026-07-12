# Conversion Verification Checklist — Production

**Site:** https://springfieldjunkremovalservice.com  
**Main commit tested:** `c0573a1` (PR #14 docs merge; production code unchanged since PR #13 `ef037f3`)  
**Phase started:** 2026-07-11  
**Live tests completed:** 2026-07-11  
**Status:** **PASS** — conversion path, call path, form path, GTM, GA4, and duplicate-event checks all verified live

## Guardrails (observed during live tests)

- One controlled test form submitted; marked as test — **not counted as a real lead**
- One controlled test call placed; routing verified — **no routing/configuration changes**
- GTM Preview (Tag Assistant) used read-only — **no publish or tag edits**
- GA4 Realtime reviewed — **no configuration changes**
- No production HTML, scripts, GTM, GA4, Formspree, CallRail, or DNS changes made

---

## Live verification summary (2026-07-11)

| Area | Result | Notes |
|---|---|---|
| Conversion path | **PASS** | Call, quote, and form paths verified end-to-end |
| Call path | **PASS** | Desktop, money page, and mobile `tel:` behavior correct |
| Form path | **PASS** | One controlled Formspree submission; hosted success page |
| GTM | **PASS** | Tag Assistant connected; all tags fired; no duplicates |
| GA4 | **PASS** | Realtime received all three key events |
| Duplicate-event check | **PASS** | No duplicate custom-event firing in Tag Assistant |
| Production code changes | **None required** | Tracking worked as deployed |

**Overall:** Springfield is **technically lead-ready**. Not fully renter-ready until authority/citation work and sufficient proof-of-life lead volume are completed.

### GA4 account note (non-blocking)

- An unused GA4 property/tag `G-XPH099Y4DW` was accidentally created during account recovery
- It was **not** installed on the site and is **not** connected to production
- **No action required** in this batch
- Live site remains connected only through `GTM-GDJF54DV` → `G-GWT8GR7QJC`

---

## Read-only implementation audit (2026-07-11)

### Tracking script

| Item | Finding |
|---|---|
| File | `analytics-events.js` (loaded once per page, before `</body>`) |
| Listener model | Single `document` delegated `click` listener + single `submit` listener (`capture: true`) |
| Duplicate script refs | **0** — exactly 1 reference per page across 30 HTML files |
| Inline `onclick` handlers | **0** across all pages |
| GTM container | `GTM-GDJF54DV` in `<head>` + noscript iframe in `<body>` on all 30 pages |

### Custom events (only these three)

| Event | Trigger | Payload fields |
|---|---|---|
| `click_call` | Click any `a[href^="tel:"]` where digits-only href equals `4172425370` | `page_path`, `link_text`, `destination`, `phone_number` |
| `click_quote_button` | Click any `a[href*="#quote"]` or `a[href*="#contact"]` | `page_path`, `link_text`, `destination` |
| `submit_lead_form` | Form `submit` (capture phase) when `action` contains `formspree.io` | `page_path`, `market` (`Springfield, MO`), `niche` (`Junk Removal`), `service` (if `[name="service"]` has value) |

**Delivery path:** If `window.google_tag_manager` exists → `dataLayer.push({ event, ...params })`. Else if `gtag` → `gtag('event', ...)`. Else queue on `dataLayer` for later GTM pickup.

**No additional custom events** are defined in `analytics-events.js`.

### Phone links

| Check | Result |
|---|---|
| `tel:4172425370` on all 30 pages | **Pass** |
| Wrong/alternate tel hrefs | **None found** |
| Tel links per page | 5–8 (header, hero, quote section, footer, in-copy) |
| Hero pattern | Text link + `class="button"` tel CTA on service pages; homepage also has `#quote` secondary button |

### Quote buttons / anchors

| Check | Result |
|---|---|
| `#quote` section present | **30/30** pages (`id="quote"` on quote box) |
| Primary quote CTA | `Get a Free Quote` → `href="#quote"` on all 30 pages |
| `click_quote_button` scope | Only `#quote` / `#contact` anchor clicks — not hero `Call` buttons (those fire `click_call`) |
| Non-tracked CTAs | e.g. homepage `href="#services"` — by design, no `click_quote_button` |

### Forms (Formspree)

| Check | Result |
|---|---|
| Action | `https://formspree.io/f/mojzdkvg` on **30/30** forms |
| Method | `POST` on all forms |
| Hidden fields (all pages) | `site=springfieldjunkremovalservice.com`, `market=Springfield, MO`, `niche=Junk Removal` |
| Service capture | **29/29** service pages: hidden `name="service"` with page-specific value; **homepage**: visible `<select name="service" required>` (no hidden service field) |
| Required visible fields | `name`, `phone`, `message` required; `email` optional; homepage also requires `service` select |
| `_next` / thank-you redirect in HTML | **None** — post-submit UX is Formspree-hosted (verified live) |
| Inline success/error handling in HTML | **None** — default Formspree POST behavior confirmed |

### Landing-page / source fields

| Field | Present |
|---|---|
| `site` | Yes (hidden) |
| `market` | Yes (hidden) |
| `niche` | Yes (hidden) |
| `service` | Yes (hidden on service pages; select on homepage) |
| UTM / `landing_page` / `source` | **Not in HTML** — rely on GTM/GA4 page URL if configured |

### Static validation summary (30 pages)

| Check | Pass |
|---|---:|
| GTM `GTM-GDJF54DV` | 30/30 |
| `analytics-events.js` | 30/30 |
| `tel:4172425370` only | 30/30 |
| Formspree `mojzdkvg` | 30/30 |
| `#quote` anchor CTA | 30/30 |
| Duplicate listener risk (HTML) | Low — single delegated listeners, no duplicate script tags |

---

## Live test results by area

### 1. Desktop call-click test — **PASS**

| Step | Result |
|---|---|
| GTM Preview on homepage | Container `GTM-GDJF54DV` connected via Tag Assistant |
| Header phone link click | `tel:4172425370` invoked; one `click_call` with `page_path: /` |
| Money page (`/junk-removal-springfield-mo`) | `click_call` fired with correct service-page `page_path` |
| Duplicate check | No duplicate `click_call` per action |

### 2. Mobile call-tap test — **PASS**

| Step | Result |
|---|---|
| Mobile emulation / tap | Header `tel:` link opened dialer with `(417) 242-5370` |
| Event | One `click_call` per tap; correct `page_path` and `phone_number` |
| Duplicate check | No duplicate firing |

### 3. Quote-button click test — **PASS**

| Step | Result |
|---|---|
| Homepage `Get a Free Quote` | Page moved to `#quote`; one `click_quote_button` with `destination: #quote` |
| Hero `Call` button (control) | `click_call` fired; no `click_quote_button` |
| Duplicate check | No duplicate `click_quote_button` per action |

### 4. Controlled Formspree test — **PASS**

| Step | Result |
|---|---|
| Test submission | **One** controlled test submitted on homepage; **no second submission** |
| `submit_lead_form` | Fired once with `market`, `niche`, `service`, and `page_path` |
| Post-submit UX | Formspree hosted page: **"Thanks! The form was submitted successfully."** |
| Lead classification | **Test only — do not count as a real lead** |
| Hidden fields | `site`, `market`, `niche` confirmed present before submit |

### 5. GTM Preview / Tag Assistant — **PASS**

| Item | Result |
|---|---|
| Container | `GTM-GDJF54DV` |
| GA4 destination | `G-GWT8GR7QJC` |
| Tag Assistant connection | Connected successfully |
| GA4 Google Tag | Fired once |
| GA4 Event — `click_call` | Fired once per tested phone action |
| GA4 Event — `click_quote_button` | Fired once per tested quote action |
| GA4 Event — `submit_lead_form` | Fired once for completed test submission |
| Tags Not Fired | **None** |
| Duplicate custom events | **None observed** in Tag Assistant |

### 6. GA4 Realtime — **PASS**

| Item | Result |
|---|---|
| Property | Correct Springfield property under RankRentOS Google account (`G-GWT8GR7QJC`) |
| Realtime — `click_call` | Received; shown as **key event** |
| Realtime — `click_quote_button` | Received; shown as **key event** |
| Realtime — `submit_lead_form` | Received; shown as **key event** |
| Realtime traffic | Page views and active traffic present during test session |
| Event totals | Reflected multiple deliberate test actions — **not** duplicate firing |

### 7. CallRail verification — **PASS**

| Item | Result |
|---|---|
| Tracking number | `(417) 242-5370` / `tel:4172425370` |
| Controlled live call | Routing worked as configured |
| CallRail dashboard | Call appeared; logging/status behavior correct |
| Configuration changes | **None** — routing, voicemail, forwarding, and recording unchanged |
| Private numbers | Caller/forwarding numbers **not recorded** in this documentation |

### 8. Thank-you / success-state behavior — **PASS**

| Item | Result |
|---|---|
| Post-submit experience | Formspree hosted success page displayed |
| Broken redirect | None observed |

---

## Per-event test log

| Test date | Tester | Page | Device / browser | Event observed | CallRail result | Formspree result | GA4 result | Pass / fail | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2026-07-11 | RankRentOS | `/` (homepage) | Desktop / Chrome | `click_call`, `click_quote_button` | N/A | N/A | Key events received | Pass | Quote → `#quote`; phone `page_path: /` |
| 2026-07-11 | RankRentOS | `/junk-removal-springfield-mo` | Desktop / Chrome | `click_call` | N/A | N/A | Key event received | Pass | Correct service-page `page_path` |
| 2026-07-11 | RankRentOS | `/` (homepage) | Mobile emulation (390px) | `click_call` | N/A | N/A | Key event received | Pass | Dialer opened with correct number |
| 2026-07-11 | RankRentOS | `/` (homepage) | Desktop / Chrome | `submit_lead_form` | N/A | Success page displayed | Key event received | Pass | **Test submission — not a real lead** |
| 2026-07-11 | RankRentOS | All tested pages | Desktop + mobile | GTM tags | Pass — call logged | Pass — one test submit | Pass — all 3 key events | Pass | Tag Assistant: Tags Not Fired = None |

---

## Sign-off table

| Test area | Tester | Date | Result | Notes |
|---|---|---|---|---|
| Static HTML audit | Cursor (read-only) | 2026-07-11 | Pass | 30/30 pages validated |
| Desktop `click_call` | RankRentOS | 2026-07-11 | Pass | Homepage + money page |
| Mobile `click_call` | RankRentOS | 2026-07-11 | Pass | Dialer opened correctly |
| `click_quote_button` | RankRentOS | 2026-07-11 | Pass | `#quote` navigation confirmed |
| Formspree delivery | RankRentOS | 2026-07-11 | Pass | One test submit; hosted success page |
| `submit_lead_form` event | RankRentOS | 2026-07-11 | Pass | Fired once; GTM + GA4 confirmed |
| GTM Preview / Tag Assistant | RankRentOS | 2026-07-11 | Pass | All tags fired; none skipped |
| GA4 Realtime | RankRentOS | 2026-07-11 | Pass | All 3 events as key events |
| Duplicate-event check | RankRentOS | 2026-07-11 | Pass | No duplicate custom events |
| CallRail routing | RankRentOS | 2026-07-11 | Pass | No config changes; private numbers redacted |
| Thank-you / post-submit UX | RankRentOS | 2026-07-11 | Pass | Formspree hosted success message |

**Conversion path status: PASS**
