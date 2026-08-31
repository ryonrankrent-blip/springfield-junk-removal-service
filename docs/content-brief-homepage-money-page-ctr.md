# Springfield Homepage and Main-Page CTR Brief

**Prepared:** 2026-08-06
**Renter-neutral correction:** 2026-08-26
**Status:** Five-file proposal committed locally at `19b5c44c1c320a1a57f6a3aa55b6197ca1731689` on `cursor/springfield-renter-neutral-ctr-update`; push, PR, deployment, and indexing require separate approval.

## Scope

- `index.html`
- `junk-removal-springfield-mo.html`
- Supporting documentation only

No URL, canonical, H1, sitemap, phone, form, GTM, analytics, DNS, routing, or external-system change is included.

## Search Console evidence

Google Search Console property: `springfieldjunkremovalservice.com`
Search type: Web
Window: July 8-August 4, 2026 (28 days)

| Page | Clicks | Impressions | CTR | Average position |
|---|---:|---:|---:|---:|
| Homepage | 0 | 1,821 | 0% | 31.2 |
| `/junk-removal-springfield-mo` | 0 | 744 | 0% | 60.8 |

### Homepage query signals

| Query | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| junk removal | 0 | 169 | 0% | 17.0 |
| junk hauling | 0 | 85 | 0% | 18.5 |
| junk removal springfield mo | 0 | 76 | 0% | 54.9 |
| junk hauling springfield mo | 0 | 69 | 0% | 49.7 |
| junk removal near me | 0 | 51 | 0% | 19.4 |
| commercial junk removal | 0 | 39 | 0% | 19.0 |
| junk haulers near me | 0 | 32 | 0% | 16.2 |
| junk and furniture removal | 0 | 30 | 0% | 17.6 |

### Main junk-removal page query signals

| Query | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| junk removal service springfield | 0 | 106 | 0% | 75.5 |
| junk removal springfield mo | 0 | 59 | 0% | 75.2 |
| junk hauling | 0 | 58 | 0% | 39.4 |
| junk hauling springfield mo | 0 | 54 | 0% | 67.5 |
| junk removal | 0 | 39 | 0% | 40.1 |
| springfield junk removal | 0 | 21 | 0% | 64.3 |

## Page-role decision

- Homepage: primary broad Springfield market page for `junk removal`, `junk hauling`, near-me intent, service discovery, and conversion entry.
- Main page: detailed Springfield service-request page for project scope, household/business use, quote preparation, access, loading requirements, and scheduling confirmation.
- Supported near-me evidence is limited to `junk removal near me` at 51 impressions / 0 clicks / position 19.4 and `junk haulers near me` at 32 impressions / 0 clicks / position 16.2.
- The combined 83-impression near-me cohort remains assigned to the existing homepage. Do not create a new near-me route or page.
- Preserve both extensionless URLs and their existing canonical tags.
- Preserve one H1 per page. The shared H1 remains unchanged during this focused snippet pass; page-role differentiation is established through title, description, opening copy, and supporting headings.

## Implemented draft changes

### Homepage

- Replaced the title with `Junk Removal Springfield MO | Hauling & Cleanout Quotes`.
- Rewrote meta and Open Graph descriptions around broad removal categories, the Springfield market, and quote intent.
- Replaced LocalBusiness markup with neutral WebSite schema aligned to the information/request-intake model.

### Main junk-removal page

- Replaced the repetitive title with `Junk Removal Services Springfield MO | Request a Quote`.
- Corrected malformed meta and Open Graph descriptions.
- Replaced LocalBusiness markup with neutral WebPage schema linked to the site through `isPartOf`.
- Rewrote the hero and process copy to remove direct loading, hauling, one-visit, and operator implications.
- Replaced the unverified `Springfield's Go-To` claim.
- Softened supporting service-card and quote language while retaining conversion intent.

## Measurement plan

- Establish the deployment date as the measurement boundary if this draft is approved and deployed.
- Do not request indexing automatically; inspect each exact extensionless URL first and obtain separate approval for any request.
- Compare the first complete 28-day period after production deployment with this baseline. Review homepage/main-page clicks, impressions, CTR, average position, query mix, near-me cohort performance, page allocation, and technical/conversion regressions.
- At the complete 84-day checkpoint, compare three complete 28-day blocks and the aggregate 84-day window for direction, stability, page allocation, protected-query effects, and available aggregate qualified-call/form indicators.
- Keep this CTR treatment isolated from authority, citation, backlink, verified-proof, routing, analytics-configuration, indexing, new-page, major internal-link, and additional content work. If any such change occurs, log it as contamination and do not attribute results solely to the CTR correction.
- Primary measures: impressions, clicks, CTR, average position, query mix, near-me query allocation, and whether both URLs continue competing for the same core queries.
- Avoid further title changes until enough post-deployment data exists unless a technical or claim-safety defect is found.

## Guardrails

- No guaranteed rankings, clicks, availability, acceptance, pricing, hauling, or pickup outcomes.
- No crew, truck, license, insurance, ownership, experience, partnership, or market-leadership claims.
- No new page, URL, redirect, canonical, sitemap entry, or external citation; schema is corrected from unsupported LocalBusiness markup to neutral WebSite/WebPage markup.
- No commit, push, deployment, indexing, outreach, listing, routing, tracking, or spending action is authorized by this draft.

## Renter-neutral correction checkpoint — 2026-08-26

- Reconstructed the five-file CTR proposal on live `main` commit `3eb8a63812517d17aecb9ba76d207d0fec1a39a5` while preserving the merged hybrid-review documentation.
- Replaced unsupported `LocalBusiness` markup with neutral `WebSite` markup on the homepage and `WebPage` markup on the main request page.
- Removed unqualified free-quote language and changed form/CTA wording to request-intake language.
- Removed same-day and next-day fulfillment implications; time-sensitive language now states that no service window is promised.
- Expressed pricing only as factors a potential provider may consider, with pricing and terms requiring provider confirmation.
- Removed or qualified language implying this website quotes, schedules, accepts, loads, hauls, or performs the requested work.
- Preserved URLs, canonicals, H1s, phone/form destinations, GTM, analytics, sitemap, and routing/deployment locks.
