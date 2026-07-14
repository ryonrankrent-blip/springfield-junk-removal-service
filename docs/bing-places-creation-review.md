# Bing Places Creation Review — Springfield

**Status:** Research and draft complete — **Bing Places creation not authorized**  
**Main commit:** `09331c2ae5f88e286cc9813ce98605e30d3e42ad`  
**Review date:** 2026-07-14  
**Mode:** Read-only policy research, duplicate recheck, claim-safe draft preparation  
**Identity source:** `citation-identity-sheet.md` / `citation-identity-approval-packet.md`  
**Current citation state:** Brownbook live and claimed; GBP blocked / not eligible now

---

## Guardrails observed

- No Bing Places account created
- No Microsoft or Google account sign-in
- No Google Business Profile import
- No listing created, claimed, edited, submitted, or verified
- No address, private contact information, credentials, or payment entered
- No support contact, advertising, or spend
- No production, DNS, tracking, routing, or form changes
- No commit, push, or deploy in this batch

**Stop for owner approval before any Bing Places account connection, import, creation, claim, verification, or commit of this documentation.**

---

## 1. Current Bing Places requirements (reverified 2026-07-14)

| Item | Finding |
|---|---|
| **Official creation / claim URL** | https://www.bingplaces.com/ and https://www.bingplaces.com/Dashboard/SearchBusiness |
| **Official Microsoft support URL** | https://support.microsoft.com/en-us/bing/add-and-manage-your-business-listing |
| **Free or paid** | Bing Places business listing management is free; no paid step observed in public docs reviewed |
| **Microsoft account requirement** | Required to sign in / create / manage a Bing Places listing |
| **Google Business Profile import** | Offered as a creation path; requires Google sign-in and permissions; not appropriate now because GBP is blocked / not eligible |
| **Manual creation path** | Available after sign-in; public docs describe searching for an existing business, then creating if not listed |
| **Service-area business support** | Supported for businesses serving customers at their locations; service areas and `HideAddress` are supported |
| **Public address hiding** | Supported via hide-address setting; API exposes `HideAddress`; public docs say hidden listings show city/ZIP rather than full address |
| **Private verification address** | Likely mandatory. Bing API requires `AddressLine1`, `City`, `StateOrProvince`, `Country`, and `ZipCode` for business creation; secondary guidance says all businesses must provide a valid physical address for verification |
| **Verification methods** | Bing may offer phone, email, postal mail/postcard, and/or other options depending on listing/account data; available methods are controlled by Bing Places |
| **Required fields (API evidence)** | Business name, address line 1, city, state/province, country, zip code, categories. Store ID is API-only. |
| **Phone / website** | Phone is optional in API schema but strategically required for NAP consistency; website is optional in API schema but approved and should be used |
| **Categories** | Bing requires at least one category. Exact live dashboard label for junk removal remains unresolved. Candidate labels from legacy/category references include `Waste Management Services`, `Cleaning & Waste Management`, and `Industrial Waste Disposal & Recycling`; exact label must be selected live before submission |
| **Hours** | Supported; can also skip displaying hours per secondary guidance. Owner-approved value is omit |
| **Description** | Supported; API rich attributes include `Description` up to 4000 characters. Use claim-safe request-and-confirm copy only |
| **Image / logo support** | Supported; secondary guidance says up to 100 photos. Upload is deferred unless separately approved |
| **Public owner/contact-name behavior** | Not confirmed without sign-in. Public owner/contact name should be omitted unless required and owner-reviewed |
| **Moderation / suspension risks** | Bing data quality guidance warns listings may be suspended if content is misleading. Risks include fake/private address, mismatched category, unsupported operator claims, reseller/partner phone concerns, and unverified business/operator model |
| **Lead-gen / intermediary restrictions** | No explicit lead-gen ban found in public sources reviewed. However, Bing appears to expect a real business with a valid physical verification address and accurate representation |

### Current policy sources

- Microsoft Support: [Add and manage your business listing](https://support.microsoft.com/en-us/bing/add-and-manage-your-business-listing)
- Bing Places dashboard/search entry: https://www.bingplaces.com/Dashboard/SearchBusiness
- Bing Places home: https://www.bingplaces.com/
- Bing Places API documentation: https://cdn.bingplaces.com/tpshared/BingPlaces_API_Latest.pdf
- Secondary operational guide used for UI details and guideline excerpts: Whitespark Bing Places guide (2025)

---

## 2. Duplicate recheck (read-only, 2026-07-14)

| Query | Result | Duplicate risk |
|---|---|---|
| `Springfield Junk Removal Service` | No exact Bing Places/business result found; unrelated Springfield junk-removal competitors surfaced | None |
| `springfieldjunkremovalservice.com` | No Bing Places duplicate found for the approved domain | None |
| `(417) 242-5370` | No Bing Places duplicate found for the approved phone | None |
| `Springfield MO junk removal` | Competitors surfaced, including 1-800-GOT-JUNK?, Junk King, Mission Junk Removal, Easy Cleanouts, 417 Junk & Debris, Pack-Haul, and similar businesses | None for approved identity |

**Conclusion:** No exact duplicate found for the approved name, phone, or domain. Unrelated competitors remain visible in the market and must not be claimed or edited.

---

## 3. Field map

| Bing Places field | Required? | Approved value | Omit | Unresolved | Risk | Owner approval required |
|---|---|---|---|---|---|---|
| Microsoft account | Required to create/manage | Ryon O'Neill as authorized representative if owner approves | | Which Microsoft account to use | Account ownership / renter handoff | **Yes** |
| Google Business Profile import | Optional path | — | **Omit / do not import** | | GBP is blocked; import could pull in invalid data or require Google sign-in | **Yes before any import** |
| Business name | Required | Springfield Junk Removal Service | | | Low if exact | Approved |
| Business type / segment | Likely required in UI | Professionals & Services or closest service-business segment | | Exact live segment label | Wrong taxonomy | **Yes at submission** |
| Primary category | Required | Junk Removal Service if available; otherwise closest safe waste/hauling category | | Exact Bing category label | Wrong category may weaken relevance or imply municipal/hazardous waste | **Yes at submission** |
| Secondary categories | Optional | One closely related category at most | Omit unless exact safe label is available | Exact labels | Category overreach | **Yes** |
| Public street address | Required privately / hideable publicly | — | **Hide public address** | Legitimate private verification address not established | Critical if invented or exposed | **Yes** |
| Private verification address | Likely mandatory | None established | — | Legitimate address and owner approval | Critical; cannot invent | **Yes** |
| City | Required | Springfield | | | Low | Approved |
| State | Required | Missouri | | | Low | Approved |
| Country | Required | United States | | | Low | Approved |
| Zip / postal code | Required privately by API; public display may show city/ZIP when address hidden | — | Public postal code should be omitted if possible | Legitimate private ZIP if verification address required | Address leakage / verification failure | **Yes** |
| Service areas | Optional / SAB support | Springfield, Missouri; Greene County, Missouri | | Exact UI limits / radius model | Under- or over-stating coverage | Approved concept; verify UI |
| Hide address | Optional / supported | Enable hide address | | Exact UI placement | Public address exposure | **Yes before submit** |
| Phone | API optional; NAP-critical | (417) 242-5370 | | Whether Bing flags as partner/reseller number | CallRail/lead-gen representation risk | Approved |
| Website | API optional; NAP-critical | https://springfieldjunkremovalservice.com | | Bing may normalize display URL | Low | Approved |
| Public email | Optional | — | **Omit** | Whether Bing requires contact email | Public personal/contact exposure | Approved omit |
| Description | Optional / supported | Claim-safe draft below | | Character limit in live UI | Direct-service/operator implication if careless | Approved style; review final |
| Hours | Optional / supported | — | **Omit** | Whether UI allows skip | False availability if invented | Approved omit |
| Photos / logo | Optional / supported | — | **Defer** | Upload workflow | Asset/public branding risk | Separate approval |
| Social links | Optional | — | **Omit** | | Unsupported platform claims | Approved omit |
| Business relationships | Optional | — | **Omit** | | Wrong parent/department relationship | N/A |
| Rich attributes / amenities | Optional | — | **Omit** | | Unsupported claims | N/A |
| Year established | Optional rich attribute | — | **Omit** | | Unsupported operating-history claim | N/A |
| License / insurance | Not core field but may appear as attributes/docs | — | **Omit / do not claim** | | Unsupported claim | N/A |
| Claim / verification method | Required after creation/claim | Use only owner-approved method | | Available methods; private address likely required | Verification failure; private info exposure | **Yes** |
| Public owner/contact name | Unknown | Omit unless required and owner-reviewed | | Whether Ryon O'Neill appears publicly | Misread as operator/hauler | **Yes if visible** |

---

## 4. Claim-safe draft

### Public listing fields

| Field | Draft value |
|---|---|
| **Business name** | Springfield Junk Removal Service |
| **Phone** | (417) 242-5370 |
| **Website** | https://springfieldjunkremovalservice.com |
| **Public address** | Hide / leave public street address blank |
| **Service area** | Springfield, Missouri and Greene County, Missouri |
| **Primary category** | Select exact Bing label closest to Junk Removal Service; unresolved until live category search |
| **Secondary category** | Omit unless one safe, closely related label is available |
| **Hours** | Omit |
| **Public email** | Omit |
| **Images** | Defer |

### Short description

> Junk removal requests in Springfield, MO and nearby Greene County areas. Furniture, appliances, cleanouts, yard waste, and construction debris. Call or request a quote online.

### Long description

> Springfield Junk Removal Service helps homeowners, renters, landlords, and businesses request junk hauling and cleanout help in Springfield, MO and nearby communities. Services can include furniture removal, appliance pickup, garage and house cleanouts, yard waste hauling, and construction debris removal. Call (417) 242-5370 or use the online quote form for a free estimate. Availability and scope are confirmed before scheduling.

### Explicitly prohibited

- Fake, private, or public street address
- Public email
- Unsupported hours
- License, insurance, employees, crews, trucks, years in business
- Locally owned / family-owned claims
- Guaranteed service, same-day availability, direct hauling, or direct fulfillment claims
- Google Business Profile import
- Photos or logo upload without separate approval

---

## 5. Public / private information risks

| Risk | Severity | Mitigation |
|---|---|---|
| Private verification address required | **Critical** | Do not proceed until legitimate private verification address is confirmed and owner-approved |
| Address accidentally shown publicly | **Critical** | Use hide-address option; stop if public address cannot be hidden |
| Account owner displayed publicly as operator | **High** | Stop for owner review if Ryon O'Neill's name would be public; do not imply he hauls, dispatches, owns trucks, or fulfills jobs |
| Google import pulls invalid GBP data | **High** | Do not import GBP; GBP remains blocked / not eligible now |
| Category mismatch | **Medium** | Select exact live Bing label only after owner review |
| Phone interpreted as reseller/partner number | **Medium** | Use approved CallRail number but acknowledge representative/lead-gen model risk |
| Listing without verified service provider | **High** | Keep request-and-confirm copy; resolve operator/renter strategy before aggressive citation expansion |
| Unverified hours or operating history | **Medium** | Omit hours and year-established claims |

---

## 6. Suitability assessment

### Recommendation: **Suitable only after specific missing information is resolved**

Bing Places is a strong local citation target and supports service-area businesses with hidden addresses. However, it appears to require a legitimate physical/private address for verification, and the current project still lacks a verified service-provider entity and private verification address strategy.

| Resolved now | Still unresolved before creation |
|---|---|
| No exact Bing duplicate found | Legitimate private verification address |
| Public NAP and claim-safe descriptions approved | Verified service-provider / operating entity |
| Hide-address support exists | Exact live Bing category label |
| Service-area support exists | Public account-name behavior |
| Phone and website are approved | Verification method available for this listing |
| Brownbook is live and claimed | Renter/operator handoff plan |

### Creation approval recommendation

**Defer.** Do not create or claim Bing Places now. Approve a future Bing Places execution only after:

1. Owner confirms a legitimate private verification address that can be used without public display.
2. Owner confirms verified service-provider / operating entity comfort for Bing's business-realness expectations.
3. Owner reviews live category options and chooses the exact category.
4. Owner approves the Microsoft account and any public-name exposure behavior.
5. Owner explicitly authorizes account sign-in, listing creation, verification, and any required address workflow.

---

*Research and draft only. Bing Places creation, claim, verification, Google import, account sign-in, support contact, and submission are not authorized by this review.*
