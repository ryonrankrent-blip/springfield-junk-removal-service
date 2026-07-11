# Conversion Verification Checklist — Production

**Site:** https://springfieldjunkremovalservice.com  
**Date prepared:** 2026-07-11  
**Status:** Manual test plan only — **do not run live tests without separate explicit approval**

## Guardrails

- Do **not** place a real test call unless approved
- Do **not** submit a live Formspree form unless approved
- Do **not** change GTM, GA4, Formspree, or CallRail settings during testing
- Use GTM Preview / GA4 DebugView for event verification when approved

---

## 1. Click-to-call event

| Step | Action | Expected result |
|---|---|---|
| 1 | Open GTM Preview mode (or GA4 DebugView) on production homepage | Container `GTM-GDJF54DV` loads |
| 2 | Click header phone link `(417) 242-5370` | Device dialer opens with `tel:4172425370` |
| 3 | Check `dataLayer` or GA4 events | Event `click_call` fires with `phone_number: 4172425370`, `page_path` set |
| 4 | Repeat on money page and one service page | Same event fires sitewide |

**Pass criteria:** `click_call` visible in GTM/GA4 debug tools; correct phone number in event payload.

---

## 2. Quote button click event

| Step | Action | Expected result |
|---|---|---|
| 1 | On homepage, click `Get a Free Quote` (or `#quote` CTA) | Page scrolls to quote form |
| 2 | Check analytics debug | Event `click_quote_button` fires with `destination: #quote` |
| 3 | Repeat from hero CTA on a child service page | Event fires with correct `page_path` |

**Pass criteria:** `click_quote_button` fires before form interaction.

---

## 3. Quote form submission (Formspree)

| Step | Action | Expected result |
|---|---|---|
| 1 | Open quote form on homepage or service page | Form `action` = `https://formspree.io/f/mojzdkvg` |
| 2 | Verify hidden fields | `site`, `market`, `niche` present; `service` on service pages |
| 3 | **Only if approved:** submit test lead with clear test identifier in message | Formspree accepts submission |
| 4 | Check Formspree inbox | Test submission appears with correct hidden field values |
| 5 | Check analytics debug | Event `submit_lead_form` fires with `market`, `niche`, `service` if applicable |

**Pass criteria:** Formspree delivery confirmed; `submit_lead_form` event fires on submit.

**Note:** Formspree may redirect to a thank-you page or show inline success depending on form settings — record observed behavior.

---

## 4. GA4 realtime event visibility

| Step | Action | Expected result |
|---|---|---|
| 1 | Confirm GA4 property receives GTM data (via GTM tags) | Realtime report shows active user |
| 2 | Trigger `click_call` in debug session | Event appears in Realtime within ~60 seconds |
| 3 | Trigger `click_quote_button` | Event appears in Realtime |
| 4 | If approved form test: trigger `submit_lead_form` | Event appears; map to GA4 key event if configured |

**Pass criteria:** All three custom events visible in GA4 Realtime or DebugView.

**Auburn parity note:** Auburn maps these to key events `click_call`, `click_quote_button`, `generate_lead`. Confirm Springfield GA4 key event mapping when GSC/GA4 access is available.

---

## 5. GTM preview / debug

| Step | Action | Expected result |
|---|---|---|
| 1 | Launch GTM Preview for production URL | Preview panel connects |
| 2 | Verify `gtm.js?id=GTM-GDJF54DV` loads on page view | Container loads without errors |
| 3 | Click phone link | `click_call` in dataLayer |
| 4 | Click quote CTA | `click_quote_button` in dataLayer |
| 5 | Submit form (if approved) | `submit_lead_form` in dataLayer before navigation |

**Pass criteria:** No GTM errors; all three events pushed to `dataLayer`.

---

## 6. Thank-you / success-state behavior

| Step | Action | Expected result |
|---|---|---|
| 1 | Inspect Formspree form settings for redirect URL or inline thank-you | Document configured behavior |
| 2 | If approved test submit: observe post-submit UX | User sees confirmation (redirect or inline message) |
| 3 | Confirm no broken redirect after submit | No 404 on thank-you page |

**Pass criteria:** Post-submit UX is clear; no error state.

---

## 7. Mobile phone-button behavior

| Step | Action | Expected result |
|---|---|---|
| 1 | Open production site on mobile device (or responsive mode) | Layout renders; viewport meta present |
| 2 | Tap header phone number | Native dialer opens with `4172425370` |
| 3 | Tap hero `Call` button | Same dialer behavior |
| 4 | Verify tap target size and visibility | Button readable and tappable |
| 5 | Check `click_call` in mobile debug session | Event fires on mobile tap |

**Pass criteria:** One-tap calling works; analytics event fires on mobile.

---

## Sign-off table

| Test area | Tester | Date | Result | Notes |
|---|---|---|---|---|
| Click-to-call | | | Pending | |
| Quote button | | | Pending | |
| Formspree delivery | | | Pending | Requires approval |
| GA4 realtime | | | Pending | |
| GTM preview | | | Pending | |
| Thank-you state | | | Pending | |
| Mobile phone | | | Pending | |
