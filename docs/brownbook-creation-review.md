# Brownbook Creation Review — Springfield

**Status:** Pre-submission inspection complete — field decisions approved — **listing creation not authorized**  
**Main commit:** `5486caae19d7f35ec9808f8f19a92d4915bdd897`  
**Creation review date:** 2026-07-12  
**Pre-submission inspection date:** 2026-07-12  
**Mode:** Read-only policy reverification, claim-safe draft, live pre-submission inspection  
**Identity source:** `citation-identity-sheet.md` (owner-approved 2026-07-12)  
**Duplicate inspection:** `tier-a-duplicate-inspection.md` — Brownbook: **0 matches**

---

## Guardrails observed

- No Brownbook account created
- No login, listing create/claim/edit/submit/verify
- No credentials entered during inspection
- No address entered
- No private contact information published
- No images uploaded
- No Brownbook support contact
- No spend
- No production, DNS, tracking, routing, or form changes
- No commit, push, or deploy in this batch

**Stop for owner approval before any Brownbook account creation, listing submission, or commit of this documentation.**

---

## Owner-approved Brownbook field configuration (2026-07-12)

| Field | Approved value | Notes |
|---|---|---|
| **Business name** | Springfield Junk Removal Service | Public listing identity |
| **Category (Brownbook label)** | **Other Waste Collection** | Owner-approved |
| **Category breadcrumb** | Administrative and Support and Waste Management and Remediation Services > Waste Management and Remediation Services > Waste Collection > Other Waste Collection | Brownbook displays label + breadcrumb, **not NAICS code** |
| **Standard NAICS reference** | **562119** | Reference only — not shown in Brownbook UI |
| **Public address** | **Leave blank** | No invented address |
| **City** | Springfield | |
| **Country** | United States | Select **United States of America** in UI |
| **Zip Code** | **Leave blank** | |
| **Phone** | (417) 242-5370 | Approved CallRail number |
| **Website** | https://springfieldjunkremovalservice.com | |
| **Display Website** | https://springfieldjunkremovalservice.com | Same URL |
| **Public listing email** | **Leave blank** | Optional listing email is public when entered |
| **Private account/login email** | ryon.rankrent@gmail.com | Account step only — **not registered** |
| **Account Name*** | Ryon O'Neill | Required for truthful private registration as asset owner and authorized representative |
| **Public owner/contact name** | **Omit** | Do not add to listing |
| **Hours** | **Omit** | |
| **Description / Business overview** | **Defer** — add only later if published listing supports editing | Approved draft text retained below for future use |
| **Logo / photos** | **Defer** | |
| **Business tags** | junk removal; furniture removal; appliance removal; garage cleanout; construction debris removal | Trim at submission if needed |
| **Location tags** | Springfield; Greene County; Missouri | |

### Account-owner boundaries (approved)

- Ryon O'Neill is the **private account owner and authorized representative** of the lead-generation asset.
- **Do not** imply he is the hauling contractor, service provider, dispatcher, crew operator, or local field operator.
- **Do not** publish personal address, private phone number, or personal email on the listing.
- **Execution stop rule:** If the live workflow indicates Ryon O'Neill will be **publicly displayed** as business owner, operator, or contact, **stop** before account creation or listing submission.

### Authorization gates (unchanged)

| Action | Status |
|---|---|
| Documentation update | This batch |
| Account creation | **Not authorized** |
| Listing creation / submission | **Not authorized** |
| Claiming / verification | **Not authorized** |
| GBP | **Blocked / not eligible now** |

---

## 1. Live pre-submission inspection findings (2026-07-12)

**URL inspected:** https://www.brownbook.net/add-business  
**Method:** Public browser inspection only — advanced to step 2 without account creation, CAPTCHA, or listing publish.

### Category typeahead results

Placeholder: **“Type to search categories (min 2 characters)…”**  
Brownbook shows **category label + breadcrumb only** — NAICS codes are not displayed in the UI.

| Search query | Result |
|---|---|
| **Junk Removal Service** | **No junk-removal label.** False positives matching “Service” (Postal Service, Limousine Service, Food Service Contractors, etc.) |
| **Junk Removal** | **No junk-removal label.** Same irrelevant “Service” matches |
| **Debris Removal** | **No debris/waste category label** returned |
| **Waste Collection** | Waste Collection; Solid Waste Collection; Hazardous Waste Collection; **Other Waste Collection**; plus tangential matches (Collection Agencies, landfills, septic, etc.) |
| **Other Waste Collection** | Same waste-related labels as above |

**Available relevant labels observed:**
- Waste Collection
- Solid Waste Collection
- Hazardous Waste Collection
- **Other Waste Collection**

**Owner-approved and recommended label:**
- **Other Waste Collection** (standard NAICS reference: **562119**)

**Avoid:**
- Solid Waste Collection — municipal garbage connotation
- Hazardous Waste Collection — wrong service type
- Broad parent **Waste Collection** — too generic
- Collection Agencies — debt collection, not hauling

### Step 1 requirements (verified live)

| Field | Required? |
|---|---|
| Business name* | **Yes** |
| Business category* | **Yes** |
| Country* | **Yes** |
| Address, City, Zip, Phone, Website, Email, social, tags | Optional |

Clicking **Next** with only name + category + country advances to step 2. **Does not publish the listing.**

### Step 2 requirements (verified live)

**Heading:** `Confirm changes (step 2 of 2)`

**Subheading:** `Create an account to validate your email address and complete your listing.`

| Field | Required? | Notes |
|---|---|---|
| Email* | **Yes** | Private account email — approved: `ryon.rankrent@gmail.com` (not entered) |
| Password* | **Yes** | Not entered |
| Password (Confirm)* | **Yes** | Observed in form DOM |
| Name* | **Yes** | Approved: Ryon O'Neill (not entered) |
| I've read and accept terms and conditions | **Yes** | Checkbox |
| reCAPTCHA | **Yes** | Required before Next |
| Next | — | Creates account; listing publishes only after email VERIFY link |

**Alternate path:** Already have an account? **Login** (Email*, Password*, Remember Me)

**Not on step 2:** description, phone, website, address, logo, hours

### Inspection actions not performed

- No account created
- No email or name entered
- No CAPTCHA completed
- No listing published (post-inspection search: **0 results** for approved business name)

### Operational blocker observed

Live reCAPTCHA displayed:

> **This site is exceeding reCAPTCHA Enterprise free quota.**

Treat as a **possible execution blocker**. Do not attempt repeated CAPTCHA submissions.

---

## 2. Privacy findings (verified live)

| Item | Finding |
|---|---|
| **Listing email** (step 1, optional) | **Public when entered** — example listings show email under Contact Details. **Must remain blank.** |
| **Account email** (step 2) | **Private** — login and email verification only; separate from listing email |
| **Account Name*** (step 2) | **Required** for registration. **Public exposure unconfirmed** — stop if live workflow shows name as public owner/operator/contact |
| **Claim-step name** | BrightLocal (2023, secondary): claim may ask full name + confirmation checkbox. **Claim-name public visibility unresolved** |
| **Private address / personal contact** | **Must not be published** on listing |

---

## 3. Current Brownbook policy and workflow (reverified 2026-07-12)

| Item | Finding |
|---|---|
| **Official add-business URL** | https://www.brownbook.net/add-business (step 1 of 2) |
| **Official register URL** | https://www.brownbook.net/register |
| **Official claim info URL** | https://www.brownbook.net/free-claim |
| **Free or paid** | Free basic listing + free claim; optional paid Profile+ / partner upsells |
| **Account required to complete listing** | **Yes** — step 2 requires account creation or login + email verification |
| **Public address** | **Optional** on step 1 |
| **Service-area compatibility** | Informal — City + Location Tags; no dedicated service-area field |
| **Website / phone** | Allowed |
| **Business description** | Supported post-publish as **Business overview** — not on step 2 |
| **Image/logo** | Post-claim / Profile+ — deferred |
| **Claim workflow** | Add → account + email verify → listing publishes → claim → edit/enrich |
| **Lead-gen restrictions** | No explicit ban; agents allowed; 5-listing SEO commercial limit N/A for single asset |
| **Policy sources** | Live add-business form (2026-07-12); [Terms 2022-08-24](https://www.brownbook.net/terms-conditions); [About](https://www.brownbook.net/about); [Register](https://www.brownbook.net/register); [Free claim](https://www.brownbook.net/free-claim) |

### Duplicate status (reconfirmed)

| Query | Result |
|---|---|
| `Springfield Junk Removal Service` on Brownbook | 0 results |
| `springfieldjunkremovalservice.com` | 0 results |
| `(417) 242-5370` | 0 results |
| Post-inspection search (2026-07-12) | 0 results |

---

## 4. Field map (updated after pre-submission inspection)

| Field name (Brownbook UI) | Required? | Approved value | Omit | Unresolved | Approval |
|---|---|---|---|---|---|
| **Business name*** | **Yes** | Springfield Junk Removal Service | | | **Approved** |
| **Business category*** | **Yes** | **Other Waste Collection** (NAICS ref 562119) | | | **Approved** |
| **Address** | Optional | — | **Omit** | | **Approved omit** |
| **City** | Optional | Springfield | | | **Approved** |
| **Country*** | **Yes** | United States | | | **Approved** |
| **Zip Code** | Optional | — | **Omit** | | **Approved omit** |
| **Phone** | Optional | (417) 242-5370 | | | **Approved** |
| **Email** (listing) | Optional | — | **Omit** | | **Approved omit** |
| **Website** | Optional | https://springfieldjunkremovalservice.com | | | **Approved** |
| **Display Website** | Optional | Same as website | | | **Approved** |
| **Social / blog / IM** | Optional | — | **Omit** | | **Approved omit** |
| **Business Tags** | Optional | Approved subset (see above) | | | **Approved** |
| **Location Tags** | Optional | Springfield; Greene County; Missouri | | | **Approved** |
| **Description / overview** | Post-publish | Defer — use approved draft later if editable | **Defer at create** | | **Deferred** |
| **Hours** | Not on form | — | **Omit** | | **Approved omit** |
| **Logo / photos** | Post-claim | — | **Defer** | | **Deferred** |
| **Account email** (step 2) | **Yes** | ryon.rankrent@gmail.com | | | **Approved** (not registered) |
| **Account Name*** (step 2) | **Yes** | Ryon O'Neill | | Public exposure unconfirmed | **Approved** (private registration) |
| **Account password** | **Yes** | Private — at execution | | | **At execution** |
| **reCAPTCHA** (step 2) | **Yes** | — | | Quota blocker possible | **Check at execution** |
| **Claim: full name** | At claim | — | | Public visibility unresolved | **Stop-check at claim** |
| **License / insurance / crews / trucks** | — | — | **Omit** | | **Prohibited** |

---

## 5. Claim-safe draft text (retained for post-publish edit)

Use only if Business overview editing is confirmed after listing is live.

**Short (~150 chars):**
> Junk removal requests in Springfield, MO and nearby Greene County areas. Furniture, appliances, cleanouts, yard waste, and construction debris. Call or request a quote online.

**Long (~400 chars):**
> Springfield Junk Removal Service helps homeowners, renters, landlords, and businesses request junk hauling and cleanout help in Springfield, MO and nearby communities. Services can include furniture removal, appliance pickup, garage and house cleanouts, yard waste hauling, and construction debris removal. Call (417) 242-5370 or use the online quote form for a free estimate. Availability and scope are confirmed before scheduling.

---

## 6. Suitability and readiness

### Platform fit: **Viable for no-public-address model**

Brownbook remains the **strongest Tier A fit**: address optional, phone + website supported, duplicate risk none, agents explicitly allowed, category decision resolved.

### Readiness status

| Item | Status |
|---|---|
| Pre-submission inspection | **Complete** |
| Category decision | **Approved** — Other Waste Collection |
| Private email strategy | **Approved** — `ryon.rankrent@gmail.com` (account only) |
| Account-name strategy | **Approved** — Ryon O'Neill (private registration; not public listing identity) |
| Step 2 workflow | **Documented** |
| Account creation | **Not authorized** |
| Listing submission | **Not authorized** |
| Claiming / verification | **Not authorized** |
| GBP | **Blocked** |

### Execution-time stop conditions

1. **Public account-name exposure** — if step 2 or post-login UI shows Ryon O'Neill as public owner/operator/contact → **stop**
2. **Claim-name public visibility** — unresolved; confirm at claim before proceeding → **stop if public**
3. **reCAPTCHA quota error** — if quota message persists → **stop**; do not retry repeatedly
4. **Verified service-provider entity** — still not established (cross-platform representation risk)
5. **Any prompt for private address** — do not invent; **stop**

---

## 7. Creation approval gate

| Decision | Status |
|---|---|
| **Pre-submission inspection** | **Complete** |
| **Field configuration** | **Owner-approved** |
| **Account creation** | **Not authorized** — separate explicit approval required |
| **Listing creation** | **Not authorized** |
| **Commit of this documentation** | **Deferred** — await owner approval |

### Proposed next approval action

1. Owner reviews this update and approves **doc commit** (if desired).
2. Owner separately approves **Brownbook account + listing execution** as a distinct decision.
3. At execution: reverify live form; confirm reCAPTCHA works; confirm account Name* is not publicly displayed; submit step 1 with approved fields; complete step 2 account creation only if stop conditions pass; omit listing email and address; defer description and logo; claim only after separate approval.

---

*Pre-submission inspection complete. No account, listing, claim, or verification performed. No commit in this batch unless owner approves.*
