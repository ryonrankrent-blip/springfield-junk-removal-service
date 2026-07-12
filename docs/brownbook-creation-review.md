# Brownbook Creation Review — Springfield

**Status:** Research and draft complete — **listing creation not authorized**  
**Main commit:** `dc97558024c46b08683dc9899ebe041c92494628`  
**Review date:** 2026-07-12  
**Mode:** Read-only policy reverification + claim-safe draft preparation  
**Identity source:** `citation-identity-sheet.md` (owner-approved 2026-07-12)  
**Duplicate inspection:** `tier-a-duplicate-inspection.md` — Brownbook: **0 matches**

---

## Guardrails observed

- No Brownbook account created
- No login, listing create/claim/edit/submit/verify
- No address entered
- No private contact information entered
- No images uploaded
- No Brownbook support contact
- No spend
- No production, DNS, tracking, routing, or form changes
- No commit, push, or deploy in this batch

**Stop for owner approval before any Brownbook submission or commit of this documentation.**

---

## 1. Current Brownbook policy and workflow (reverified 2026-07-12)

| Item | Finding |
|---|---|
| **Official add-business URL** | https://www.brownbook.net/add-business (step 1 of 2) |
| **Official register URL** | https://www.brownbook.net/register |
| **Official claim info URL** | https://www.brownbook.net/free-claim |
| **Free or paid** | **Free basic listing** and **free claim** advertised. Paid **Profile+** and partner upsells (Uberall Listing Manager, BLINX) exist but are optional. |
| **Account required** | **Not required** to add a basic listing anonymously. **Required** to claim, lock edits, add logo/photos, and manage listing long-term. Register/login available at https://www.brownbook.net/login |
| **Email verification required** | **Yes for registered accounts** — register page states user must click VERIFY link in email before account is active. Listing email field on add form is separate and optional. |
| **Public address required or optional** | **Optional on step 1** — only Business name*, Business category*, and Country* are marked required. Address, City, and Zip Code have no asterisk and JS validation treats them as optional. |
| **Service-area business compatibility** | **Partial / informal** — no dedicated service-area field. Location is conveyed via optional **City**, **Location Tags**, and published city/country display. Listings without street address are possible; example profiles show city + state only. |
| **Website allowed** | **Yes** — Website and Display Website fields on add form. |
| **Phone allowed** | **Yes** — Phone and Mobile fields on add form. |
| **Owner/contact name public** | **Not on add-business step 1.** BrightLocal documentation (2023) reports claim confirmation asks for **full name** with checkbox that business is yours — this appears to be **account/claim verification**, not a published listing owner field. **Reverify at claim time.** |
| **Business description supported** | **Yes** — add-business form schema includes `description` field. Published listings display **Business overview** (see example: Movin and Removin). Long text appears supported post-create and on profile pages. |
| **Category options** | **NAICS-based typeahead** — UI placeholder: “Search for a category…” / “Select category”. Uses `naics_code`, `naics_title`, `naics_category_breadcrumb`. Exact “Junk Removal Service” label **not confirmed live** without interactive typeahead (blocked from form submission during this review). Likely matches: **562119 Other Waste Collection** (debris/rubble removal) or **562111 Solid Waste Collection** — **owner must confirm exact label at submission.** |
| **Image/logo support** | **Yes after claim** — homepage and free-claim page advertise logos, photos, video via claim/Profile+. Not part of required step-1 fields. |
| **Business tags / location tags** | **Optional** — combobox fields; custom tags allowed (min 2 characters). |
| **Hours field** | **Not observed** on add-business step 1. |
| **Service list field** | **Not observed** as structured multi-select on step 1. Services may be expressed in description and business tags only. |
| **Claim/edit workflow** | 1) Add listing (anonymous or logged in) → 2) Listing publishes → 3) **Claim this listing for FREE** → 4) Registered user confirms identity (full name + confirmation checkbox per BrightLocal) → 5) Claimed & Verified badge → 6) Edit/add overview, logo, photos via account dashboard |
| **Step 2 of add-business** | UI shows “step 1 of 2”. Step 2 not fully observed without submitting form. JS confirms **reCAPTCHA** on submit and confirm/final dialogs (`confirmDialogOpen`, `finalDialogOpen`). Description field exists in form schema. |
| **Moderation / rejection risk** | Terms require **genuine listings**, accurate updates, and authorized add/claim only. Brownbook may remove obscene/illegal content; no heavy pre-vetting stated. **False claim disputes** can transfer listing to rightful claimant with forfeiture of paid claim period. User-generated edits mean vandalism/spam risk on unclaimed listings. |
| **Lead-generation / intermediary restrictions** | Terms **do not explicitly ban** lead-generation or rank-and-rent sites. Terms **do** require genuine business listings and authorized representation. **Limit:** no more than **5 listings for commercial gain** (SEO services for others) without official API/commercial agreement — **not applicable** to a single Springfield asset. About page explicitly welcomes **business owners and their agents**. |
| **Current policy sources** | https://www.brownbook.net/add-business (live form, 2026-07-12); https://www.brownbook.net/terms-conditions (last updated **2022-08-24**); https://www.brownbook.net/about; https://www.brownbook.net/register; https://www.brownbook.net/free-claim; BrightLocal claim guide (2023-07-03, secondary); example listing https://brownbook.net/business/54043832/movin-and-removin |

### Duplicate status (reconfirmed)

| Query | Result |
|---|---|
| `Springfield Junk Removal Service` on Brownbook | 0 results |
| `springfieldjunkremovalservice.com` | 0 results |
| `(417) 242-5370` | 0 results |
| `junk removal springfield missouri` on Brownbook | 0 results |

Full inspection record: `tier-a-duplicate-inspection.md`.

---

## 2. Field map (every observed Brownbook field)

| Field name (Brownbook UI) | Required? | Approved value | Omit | Unresolved | Risk | Approval needed |
|---|---|---|---|---|---|---|
| **Business name*** | **Yes** | Springfield Junk Removal Service | | | Low — matches approved identity | **Approved** |
| **Business category*** (NAICS typeahead) | **Yes** | Map to closest NAICS match for junk/debris removal | | **Exact NAICS label** — must pick live from typeahead | Medium — wrong category weakens relevance | **Yes — owner confirms label at submission** |
| **Address** | Optional | — | **Omit** | | Low if omitted; inventing address is prohibited | **Approved omit** |
| **City** | Optional | Springfield | | Whether city alone is sufficient for Greene County coverage | Low–medium — may under-represent county-wide service | **Approved** (city only) |
| **Country*** | **Yes** | United States | | | Low | **Approved** |
| **Zip Code** | Optional | — | **Omit** (no public address) | | Low if omitted | **Approved omit** |
| **Phone** | Optional | (417) 242-5370 | | | Low — approved CallRail number | **Approved** |
| **Mobile** | Optional | — | **Omit** | | Low | **Approved omit** |
| **Fax** | Optional | — | **Omit** | | Low | **Approved omit** |
| **Email** (listing) | Optional | — | **Omit** from public display | | Low | **Approved omit** |
| **Website** | Optional | https://springfieldjunkremovalservice.com | | | Low | **Approved** |
| **Display Website** | Optional | https://springfieldjunkremovalservice.com | | Duplicate of Website — use same URL or omit | Low | **Approved** (same URL) |
| **Blog** | Optional | — | **Omit** | | Low | **Approved omit** |
| **Twitter** | Optional | — | **Omit** | | Low | **Approved omit** |
| **Facebook** | Optional | — | **Omit** (platform deferred) | | Low | **Approved omit** |
| **Instagram** | Optional | — | **Omit** | | Low | **Approved omit** |
| **LinkedIn** | Optional | — | **Omit** | | Low | **Approved omit** |
| **TikTok** | Optional | — | **Omit** | | Low | **Approved omit** |
| **Video** (Skype/video calling) | Optional | — | **Omit** | | Low | **Approved omit** |
| **Instant messenger** | Optional | — | **Omit** | | Low | **Approved omit** |
| **Business Tags** | Optional | `junk removal`, `furniture removal`, `cleanout`, `debris removal` (subset) | | Final tag list vs platform suggestions | Low — keep claim-safe | **Approved subset** — trim at submission if needed |
| **Location Tags** | Optional | `Springfield`, `Greene County`, `Missouri` | | | Low | **Approved** |
| **Description / Business overview** | Optional (form schema) | See claim-safe drafts below | | Whether required on step 2 | Low if claim-safe text used | **Approved** (text below) |
| **Hours** | Not on step 1 | — | **Omit** | | Low | **Approved omit** |
| **Logo / photos** | Post-claim / Profile+ | `site-icon-512.png` only when authorized | **Omit at create** | Upload not authorized in this review | Low — defer to post-claim task | **Separate approval for upload** |
| **reCAPTCHA** (step 2) | Expected at submit | Complete at submission only | | | Low | **At submission** |
| **Register: account email** | Required to claim | Private operations email — **not specified in identity sheet** | | Which email to use | Medium — account recovery, verification | **Yes — owner designates private account email** |
| **Register: password** | Required to claim | Private — not documented | | | Low | **At account creation** |
| **Claim: full name** | Reported at claim step | Ryon O'Neill — **private account only** | **Do not publish on listing** | Whether Brownbook displays claimant name publicly | Medium — privacy boundary | **Yes — confirm claim UI before entering** |
| **Claim: “this is your business” checkbox** | At claim | Authorized representative attestation | | Wording vs lead-gen asset model | Medium — must be truthful as asset representative, not as hauling operator | **Yes — owner/legal comfort check** |
| **Secondary category** | Not observed | — | **Omit** | Brownbook appears single-category (NAICS) | Low | **Approved omit** |
| **Structured service list** | Not observed | — | Use description + tags only | | Low | N/A |
| **License / insurance / employees / trucks / years** | Not observed | — | **Omit** | | High if invented | **Approved prohibit** |

---

## 3. Claim-safe Brownbook draft listing

### Public fields (submission-ready copy)

| Field | Draft value |
|---|---|
| **Business name** | Springfield Junk Removal Service |
| **Phone** | (417) 242-5370 |
| **Website** | https://springfieldjunkremovalservice.com |
| **Display Website** | https://springfieldjunkremovalservice.com |
| **Country** | United States |
| **City** | Springfield |
| **Address** | *(leave blank)* |
| **Zip Code** | *(leave blank)* |
| **Email** | *(leave blank)* |
| **Primary category** | *[Select at submission — prefer NAICS title closest to “Junk Removal” or “Other Waste Collection” / debris removal; avoid unrelated categories]* |
| **Business tags** | junk removal; furniture removal; appliance removal; garage cleanout; construction debris removal |
| **Location tags** | Springfield; Greene County; Missouri |

### Short description (~150 chars)

> Junk removal requests in Springfield, MO and nearby Greene County areas. Furniture, appliances, cleanouts, yard waste, and construction debris. Call or request a quote online.

### Long description / Business overview (~400 chars)

> Springfield Junk Removal Service helps homeowners, renters, landlords, and businesses request junk hauling and cleanout help in Springfield, MO and nearby communities. Services can include furniture removal, appliance pickup, garage and house cleanouts, yard waste hauling, and construction debris removal. Call (417) 242-5370 or use the online quote form for a free estimate. Availability and scope are confirmed before scheduling.

### Service list (narrative — no structured field)

Use in description or tags only:

- General junk removal
- Furniture removal
- Appliance removal
- Garage cleanout
- House cleanout
- Estate cleanout
- Commercial junk removal
- Construction debris removal
- Yard waste removal
- Trash removal

### Explicitly omitted

- Hours
- Public email
- Street address, suite, map pin
- License, insurance, employees, crews, trucks
- Years in business
- Locally owned / family-owned
- Direct-service, dispatcher, or operator identity claims
- Social profiles (Facebook deferred; others not approved)
- Logo/photo upload (defer until separate upload approval)

---

## 4. Suitability assessment

### Recommendation: **Suitable only after specific missing information is resolved**

Brownbook is the **strongest Tier A fit** for the approved no-public-address model (address optional; phone + website supported; duplicate risk none; agents explicitly allowed). It is **not** blocked like GBP. However, submission should wait until the unresolved items below are closed.

| Resolved now | Still unresolved before submission |
|---|---|
| Approved public NAP + descriptions | Exact **NAICS category label** from live typeahead |
| No duplicate listing | **Private Brownbook account email** for register/verify |
| Terms allow authorized representatives | **Claim-step UI** — confirm full name is private, not published |
| Address can be omitted | **Step 2 fields** — reverify immediately before submit (not fully observed without submission) |
| Identity sheet approved | **Verified hauling/service-provider entity** still not established (moderate representation risk across all directories) |
| | **Logo upload** — separate approval if desired post-claim |

### Not recommended as unsuitable

Brownbook does **not** require a public storefront address and does **not** explicitly prohibit lead-generation asset listings under current terms. Deferral is due to **execution gaps**, not platform incompatibility.

---

## 5. Creation approval gate

| Decision | Status |
|---|---|
| **Documentation / draft** | Complete in this file |
| **Listing creation on Brownbook** | **Not authorized** |
| **Owner creation approval** | **Deferred** — await explicit go-ahead after resolving unresolved fields |
| **Commit of this documentation** | **Deferred** — await owner approval |

### Proposed next approval action

1. Owner reviews this document and sections A–J in the task response.
2. Owner approves **doc commit** (if desired) and/or **Brownbook creation** as separate decisions.
3. If creation approved: designate **private account email**; reverify add-business form live; select **NAICS category**; submit step 1–2 with claim-safe draft; **omit address and public email**; claim listing with authorized-representative attestation; **do not upload logo** until upload separately approved.
4. If creation not approved: remain at **Inspected + creation-review complete** in tracker; proceed to next Tier A creation review (Bing Places or Yelp).

---

## 6. Public / private information risk summary

| Risk | Severity | Mitigation |
|---|---|---|
| Invented address | **High** | Omit address, city only |
| Public owner as hauling operator | **High** | Use business name only; no operator claims in descriptions |
| Account owner name published | **Medium** | Confirm claim UI; use name only if required for private claim verification |
| Personal email/phone exposed | **Medium** | Use designated ops email for account; omit listing email |
| Category mismatch | **Medium** | Live NAICS selection with owner sign-off |
| Unclaimed listing vandalism | **Low–medium** | Claim promptly after create |
| Lead-gen / genuine-business representation | **Medium** | Request-and-confirm copy only; no crew/truck/license claims |
| SEO agency 5-listing limit | **Low** | Single asset — within terms |
| Paid upsell traps | **Low** | Decline Profile+/Uberall unless separately approved |

---

*Research and draft only. No listing created. No commit performed in this batch unless owner approves.*
