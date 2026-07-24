# Internal Link Authority Plan — Springfield Content Clusters

**Status:** Planning complete; priority authority links and the Springfield disposal/recycling guide are **deployed** and live-QA verified
**Date:** 2026-07-17; construction-debris deploy/indexing update 2026-07-18; yard-waste and accepted-items updates 2026-07-19; commercial update 2026-07-21; junk-removal-cost deploy/indexing update 2026-07-22; apartment-cleanout and eviction-cleanout deploy/indexing updates 2026-07-23
**Scope:** Construction debris, yard waste, accepted items, commercial junk removal, junk removal cost, and the deployed disposal guide

## Springfield disposal-guide links — deployed 2026-07-23

The deployed `springfield-junk-disposal-guide.html` links contextually to the guides hub, accepted-items guide, cost guide, quote-process guide, core junk-removal page, furniture, appliance, mattress, yard-waste, construction-debris, commercial, and `#quote` destinations.

The production integration added exactly one inbound card from `junk-removal-guides-springfield-mo.html`, added the extensionless guide URL to `sitemap.xml`, and updated fixed-count QA expectations from 30 to 31. No service page, navigation menu, footer, or unrelated inbound link was changed.

The guide remains broader than the accepted-items page and links to, rather than replacing, the detailed yard-waste, construction-debris, cost, and commercial pages.

Official outbound references are limited to Springfield and Missouri DNR resources. Facility and program requirements must be reverified before future content changes. PR #48 merged at `69ab96fd0e8f367d9e0996315fa1db15ba6caa21`; the live guide returned HTTP 200 and byte-matched the merged file. The guides-hub card and 31-URL sitemap were verified live. Repository QA passed 222 checks with 0 failures and 702 internal links with 0 broken. No indexing request or sitemap resubmission occurred.

## Apartment-cleanout authority deployment — 2026-07-22–23

| Source section | Destination | Anchor | Purpose | Status |
|---|---|---|---|---|
| Authorization guidance | Missouri Attorney General landlord-tenant resource | Missouri Attorney General landlord-tenant resource | Official rights-and-responsibilities context without legal advice | Deployed and live-verified |
| Authorization guidance | Missouri Revised Statutes § 441.065 | Missouri Revised Statutes section 441.065 | Identify that a state procedure may apply to abandoned premises | Deployed and live-verified |
| Disposal research | Springfield Waste Wizard | Waste Wizard | Current item-specific reuse/disposal research | Deployed and live-verified |
| Related services | `/eviction-cleanout-springfield-mo` | Eviction Cleanouts | Separate court/possession-driven intent | Deployed and live-verified |
| Related services | `/commercial-junk-removal-springfield-mo` | Commercial Junk Removal | Property-manager and multifamily crossover | Deployed and live-verified |
| Helpful guides | `/junk-removal-cost-springfield-mo` | Apartment Cleanout Cost Factors | Quote education | Deployed and live-verified |
| Helpful guides | `/what-items-can-be-removed-springfield-mo` | Accepted Items & Restrictions | Material qualification | Deployed and live-verified |

No inbound page, navigation, footer, sitemap, or new production URL was changed. Deployment completed through PR #42 at merge commit `2b68e6d77252ff76452906d73929c033d2c6ae74`. The extensionless production URL returned HTTP 200 and byte-matched `main`; live QA passed. Google Search Console reported **URL is on Google** and **Page is indexed** for the exact extensionless URL. Discovery showed no referring sitemap or referring page. The last crawl was July 20, 2026 at 1:50:16 AM by Googlebot smartphone; crawling was allowed, the page fetch succeeded, and indexing was allowed. The user-declared canonical matched the extensionless URL, and Google selected the inspected URL as canonical. One indexing request was submitted successfully and added to the priority crawl queue. No second request or sitemap resubmission occurred. Await recrawl and refreshed search data; do not repeat the request now.

## Guardrails

- This plan documents proposed links for remaining clusters.
- Construction-debris page links listed below were implemented, deployed on `ca32eca`, and verified live on 2026-07-18.
- Yard-waste page links listed below were implemented, deployed on `90e7249`, and verified live on 2026-07-19.
- Accepted-items page links listed below were implemented, deployed on `f908715`, and verified live on 2026-07-19.
- Accepted-items GSC status is a **non-blocking indexing-URL variance** on the `.html` variant; the canonical extensionless URL was **not** confirmed as requested.
- Commercial page links were implemented, deployed, live-verified, and submitted once for indexing through the exact extensionless URL.
- Junk-removal-cost page links were implemented, deployed on `502e087`, and verified live on 2026-07-22. One indexing request was submitted for the exact extensionless URL; do not repeat it now.
- No sitemap, hub navigation, or unrelated production link changes were made in these batches.
- Any additional link implementation requires separate approval and QA.

## Existing Link Context

| Current pattern | Notes |
|---|---|
| Services hub | Links to all service pages, including construction debris, yard waste, and commercial junk removal. |
| Guides hub | Links to `junk-removal-cost-springfield-mo.html`, `what-items-can-be-removed-springfield-mo.html`, `how-junk-removal-works-springfield-mo.html`, and selected commercial-intent services. |
| Money page | Links to all major services, hubs, city pages, and guides. |
| Cost guide | Already links to yard waste, construction debris, accepted-items, process guide, and several city pages. |
| Accepted-items guide | Already links to yard waste, construction debris, cost guide, process guide, and several service pages. |
| Commercial page | Already links to construction debris, cost guide, accepted-items, process guide, hubs, and city pages; does not currently link to apartment or eviction pages in extracted link list. |

## Proposed Link Map

| Source page | Destination page | Suggested anchor text | Placement | Reason | Already exists? |
|---|---|---|---|---|---|
| `construction-debris-removal-springfield-mo.html` | `/what-items-can-be-removed-springfield-mo` | what items can be removed | Local disposal-rules or FAQ section | Send broad item/restricted-material questions to accepted-items guide | No |
| `construction-debris-removal-springfield-mo.html` | `/junk-removal-cost-springfield-mo` | construction debris removal cost factors | Cost paragraph | Connect weight/disposal complexity to quote education | No |
| `construction-debris-removal-springfield-mo.html` | `/yard-waste-removal-springfield-mo` | yard waste removal | Clean fill / not construction debris note | Distinguish organic yard debris from C&D debris | Yes |
| `construction-debris-removal-springfield-mo.html` | `/commercial-junk-removal-springfield-mo` | commercial junk removal | Contractor/property manager paragraph | Bridge contractor/business intent | No |
| `yard-waste-removal-springfield-mo.html` | `/what-items-can-be-removed-springfield-mo` | what junk removal can take | Not-yard-waste section | Route mixed outdoor loads to broader accepted-items guide | No |
| `yard-waste-removal-springfield-mo.html` | `/junk-removal-cost-springfield-mo` | yard waste removal cost factors | Quote/cost section | Explain volume, access, bagging, and disposal-rule impact | No |
| `yard-waste-removal-springfield-mo.html` | `/construction-debris-removal-springfield-mo` | construction debris removal | Not accepted / non-yard items section | Prevent overlap with lumber, pallets, remodel debris | Yes |
| `yard-waste-removal-springfield-mo.html` | `/garage-cleanout-springfield-mo` | garage cleanout | Mixed cleanup section | Yard/garage cleanup crossover | Yes |
| `what-items-can-be-removed-springfield-mo.html` | `/yard-waste-removal-springfield-mo` | yard waste removal | Yard waste row / section | Deepen local yard-waste rules | Yes |
| `what-items-can-be-removed-springfield-mo.html` | `/construction-debris-removal-springfield-mo` | construction debris removal | Construction debris row / section | Deepen C&D rules | Yes |
| `what-items-can-be-removed-springfield-mo.html` | `/junk-removal-cost-springfield-mo` | junk removal cost | Quote-prep / cost note | Explain item type and access affect pricing | Yes |
| `what-items-can-be-removed-springfield-mo.html` | `/mattress-removal-springfield-mo` | mattress removal | Accepted/confirm table | Connect common bulky item to service page | No |
| `what-items-can-be-removed-springfield-mo.html` | `/commercial-junk-removal-springfield-mo` | commercial junk removal | Business items section | Route B2B items to commercial page | No |
| `commercial-junk-removal-springfield-mo.html` | `/apartment-cleanout-springfield-mo` | apartment cleanouts | Property-manager section | Capture rental-turnover intent | No |
| `commercial-junk-removal-springfield-mo.html` | `/eviction-cleanout-springfield-mo` | eviction cleanouts | Property-manager section | Capture landlord/PM abandonment/turnover intent | No |
| `commercial-junk-removal-springfield-mo.html` | `/construction-debris-removal-springfield-mo` | construction debris removal | Business renovation section | Already adjacent; reinforce contractor intent | Yes |
| `commercial-junk-removal-springfield-mo.html` | `/junk-removal-cost-springfield-mo` | commercial junk removal cost factors | Quote-prep checklist | Educate B2B quote requests | Yes |
| `commercial-junk-removal-springfield-mo.html` | `/what-items-can-be-removed-springfield-mo` | what items can be removed | Restricted item note | Avoid unverified acceptance claims | Yes |
| `junk-removal-cost-springfield-mo.html` | `/construction-debris-removal-springfield-mo` | construction debris removal | Service-specific cost factors | Weight/disposal authority path | Yes |
| `junk-removal-cost-springfield-mo.html` | `/yard-waste-removal-springfield-mo` | yard waste removal | Service-specific cost factors | Seasonal/volume/access authority path | Yes |
| `junk-removal-cost-springfield-mo.html` | `/commercial-junk-removal-springfield-mo` | commercial junk removal | Service-specific cost factors | B2B quote path | No |
| `junk-removal-cost-springfield-mo.html` | `/what-items-can-be-removed-springfield-mo` | what items can be removed | Restricted-item cost caveat | Explain why some items need confirmation | Yes |
| `junk-removal-guides-springfield-mo.html` | `/construction-debris-removal-springfield-mo` | construction debris disposal rules | New local-rules guide card or text link | Lift strongest GSC signal from guide hub | No |
| `junk-removal-guides-springfield-mo.html` | `/yard-waste-removal-springfield-mo` | yard waste disposal rules | New local-rules guide card or text link | Lift early click signal | No |
| `junk-removal-guides-springfield-mo.html` | `/springfield-junk-disposal-guide` | Springfield junk disposal guide | Guide card | Add linkable local-resource asset | Yes |
| `junk-removal-springfield-mo.html` | `/construction-debris-removal-springfield-mo` | construction debris removal | Existing services section or local authority section | Already supports primary cluster | Yes |
| `junk-removal-springfield-mo.html` | `/yard-waste-removal-springfield-mo` | yard waste removal | Existing services section or local authority section | Already supports secondary cluster | Yes |
| `junk-removal-springfield-mo.html` | `/springfield-junk-disposal-guide` | Springfield disposal guide | Future local-resource section | Support broad informational intent after new page exists | N/A |

## Anchor Text Guidance

- Use natural anchors that match page intent, not repeated exact-match anchors in every paragraph.
- Prefer descriptive anchors such as "construction debris removal," "yard waste removal," "what items can be removed," and "junk removal cost factors."
- Avoid anchors implying official endorsement, such as "city-approved junk removal."
- For future disposal guide links, use informational anchors: "Springfield disposal guide," "local disposal options," or "recycling and donation resources."

## Implementation Notes

| Page | Recommended link changes when approved |
|---|---|
| Construction debris | Add links to accepted-items, cost, and commercial pages; keep existing yard-waste link. |
| Yard waste | Add links to accepted-items and cost; keep existing construction/garage links. |
| Accepted items | Deployed mattress, commercial, furniture, appliance, garage, yard, construction, cost, and money-page links; live-QA verified on 2026-07-19. |
| Commercial | Add links to apartment and eviction cleanout pages in a property-manager section. |
| Cost | Add link to commercial page in service-specific cost factors. |
| Guides hub | Consider adding local authority cards/links after the first two page updates are published and approved. |

## 2026-07-18 Construction Debris Deployed Link Changes

| Source section | Destination | Anchor text | Reason | Status |
|---|---|---|---|---|
| Official local resources | City C&D PDF | City construction and demolition waste guidance | Supports local C&D planning, separation, reuse/recycling, and asbestos-caution context | Deployed and live-verified |
| Official local resources | City Material Know How | City Material Know How landfill restrictions and clean-fill notes | Supports clean-fill and landfill-banned item cautions | Deployed and live-verified |
| Official local resources | Noble Hill Sanitary Landfill | Noble Hill Sanitary Landfill customer information | Supports facility hours, guidelines, fee-category, and acceptance-caution context | Deployed and live-verified |
| Official local resources | Missouri DNR PUB2045 | Missouri DNR construction and demolition waste guidance | Supports clean-fill, recovered-materials, regulated C&D waste, hazardous-material, and asbestos distinctions | Deployed and live-verified |
| Official local resources | Waste Wizard | Springfield Waste Wizard item lookup | Gives users an official item-specific lookup without copying item database content | Deployed and live-verified |
| Helpful related pages | `/what-items-can-be-removed-springfield-mo` | What Items Can Be Removed | Routes broad item/restricted-material questions to the accepted-items guide | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/junk-removal-cost-springfield-mo` | Junk Removal Cost Factors | Connects weight, volume, access, and disposal requirements to quote education | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/commercial-junk-removal-springfield-mo` | Commercial Junk Removal | Routes contractor/business remodel intent to B2B page | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/apartment-cleanout-springfield-mo` | Apartment Cleanouts | Routes landlord/property-manager turnover intent | Deployed and live-verified (HTTP 200) |
| Construction debris examples | `/junk-removal-springfield-mo` | junk removal in Springfield, MO | Routes broader mixed-junk requests back to the money page | Deployed and live-verified (HTTP 200) |

No sitemap, hub navigation, footer, or new-page links were changed in this batch. Production deployment for the construction-debris page completed on commit `ca32eca` (2026-07-18T06:01:28Z). Live QA PASS. GSC indexing requested once; awaiting Google recrawl.

## 2026-07-19 Yard Waste Deployed Link Changes

| Source section | Destination | Anchor text | Reason | Status |
|---|---|---|---|---|
| Official local resources | City Yardwaste Recycling Center | City Yardwaste Recycling Center | Supports city yard-waste drop-off, brush guidelines, and bag/container notes | Deployed and live-verified |
| Official local resources | City Material Know How | City Material Know How landfill restrictions for yardwaste | Supports landfill ban for leaves, grass, limbs, and brush | Deployed and live-verified |
| Official local resources | Noble Hill Sanitary Landfill | Noble Hill Sanitary Landfill customer information | Supports landfill customer-guideline and Material Know How referral context | Deployed and live-verified |
| Official local resources | Waste Wizard | Springfield Waste Wizard item lookup | Gives users an official item-specific lookup without copying item database content | Deployed and live-verified |
| Official local resources | Missouri DNR PUB2050 | Missouri DNR special waste / landfill exclusion guidance | Supports state landfill-exclusion context for yard waste | Deployed and live-verified |
| Helpful related pages | `/junk-removal-springfield-mo` | General Junk Removal | Routes broader mixed-junk requests back to the money page | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/what-items-can-be-removed-springfield-mo` | What Items Can Be Removed | Routes mixed outdoor / restricted-material questions to accepted-items guide | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/junk-removal-cost-springfield-mo` | Junk Removal Cost Factors | Connects volume, access, bagging, and disposal requirements to quote education | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/construction-debris-removal-springfield-mo` | Construction Debris Removal | Distinguishes organic yard waste from lumber/remodel debris | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/garage-cleanout-springfield-mo` | Garage Cleanouts | Routes outdoor/garage cleanup crossover | Deployed and live-verified (HTTP 200) |
| Materials section | `/construction-debris-removal-springfield-mo` | construction debris removal | Routes lumber, fencing, pallets, remodel leftovers | Deployed and live-verified |
| Materials section | `/what-items-can-be-removed-springfield-mo` | what items can be removed | Routes broader outdoor clutter questions | Deployed and live-verified |
| Materials section | `/garage-cleanout-springfield-mo` | garage cleanout | Routes garage/outdoor clutter crossover | Deployed and live-verified |
| Examples section | `/junk-removal-cost-springfield-mo` | junk removal cost guide | Explains volume/access/disposal quote factors | Deployed and live-verified |
| Examples section | `/junk-removal-springfield-mo` | junk removal in Springfield, MO | Routes broader service requests to the money page | Deployed and live-verified |

No sitemap, hub navigation, footer, or new-page links were changed in this batch. Production deployment for the yard-waste page completed on commit `90e7249` (2026-07-19T06:00:22Z). Live QA PASS. GSC indexing requested once; awaiting Google recrawl.

## 2026-07-19 Accepted Items Deployed Link Changes

| Source section | Destination | Anchor text | Reason | Status |
|---|---|---|---|---|
| Official local resources | City Material Know How | City Material Know How landfill restrictions | Supports landfill-banned / specially handled material context | Deployed and live-verified |
| Official local resources | Waste Wizard | Springfield Waste Wizard item lookup | Gives users an official item-specific lookup without copying item database content | Deployed and live-verified |
| Official local resources | Household Chemical Collection Center | Household Chemical Collection Center | Routes household chemical questions to official appointment-based guidance | Deployed and live-verified |
| Official local resources | City Mattress Recycling | City mattress recycling information | Supports mattress/box-spring disposal research without quoting permanent fees | Deployed and live-verified |
| Official local resources | Missouri DNR HHW | Missouri DNR household hazardous waste guidance | Supports paint, battery, chemical, pesticide, and related HHW referral | Deployed and live-verified |
| Helpful related pages | `/junk-removal-springfield-mo` | General Junk Removal | Routes broader mixed-junk requests to the money page | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/junk-removal-cost-springfield-mo` | Junk Removal Cost Factors | Connects item type, volume, access, and disposal requirements to quote education | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/furniture-removal-springfield-mo` | Furniture Removal | Furniture-specific conversion path | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/appliance-removal-springfield-mo` | Appliance Removal | Confirm-first appliance path | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/mattress-removal-springfield-mo` | Mattress Removal | Mattress-focused path | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/garage-cleanout-springfield-mo` | Garage Cleanouts | Common cleanup path | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/yard-waste-removal-springfield-mo` | Yard Waste Removal | Deepens yard-waste local rules without replacing the yard page | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/construction-debris-removal-springfield-mo` | Construction Debris Removal | Deepens C&D local rules without replacing the debris page | Deployed and live-verified (HTTP 200) |
| Helpful related pages | `/commercial-junk-removal-springfield-mo` | Commercial Junk Removal | Routes business/office loads to commercial page | Deployed and live-verified (HTTP 200) |
| Appliances section | `/appliance-removal-springfield-mo` | appliance removal | Confirm-first appliance detail | Deployed and live-verified |
| Yard waste section | `/yard-waste-removal-springfield-mo` | yard waste removal | Local-rule depth for organic debris | Deployed and live-verified |
| Construction section | `/construction-debris-removal-springfield-mo` | construction debris removal | Local-rule depth for remodel debris | Deployed and live-verified |
| Mattresses section | `/mattress-removal-springfield-mo` | mattress removal | Mattress-focused requests | Deployed and live-verified |
| Business section | `/commercial-junk-removal-springfield-mo` | commercial junk removal | Broader business scope | Deployed and live-verified |
| Local examples | `/junk-removal-cost-springfield-mo` | junk removal cost guide | Explains item/access/disposal quote factors | Deployed and live-verified |
| Local examples | `/junk-removal-springfield-mo` | junk removal in Springfield, MO | Routes broader service requests to the money page | Deployed and live-verified |
| Hero / quote | `#quote` | Get a Free Quote | Conversion path | Deployed and live-verified |

No sitemap, hub navigation, footer, or new-page links were changed in this batch. Production deployment for the accepted-items page completed on commit `f908715` (2026-07-19T06:34:30Z). Live QA PASS. GSC has a non-blocking indexing-URL variance on the `.html` variant; the canonical extensionless URL was not confirmed as requested. Do not request either accepted-items URL again now.

## 2026-07-23 Rental Turnover Checklist Deployed Links

| Source | Destination | Anchor purpose | Status |
|---|---|---|---|
| Checklist breadcrumb and related links | `/junk-removal-guides-springfield-mo` | Guide hierarchy | Deployed and live-verified |
| Common turnover requests | `/what-items-can-be-removed-springfield-mo` | Item eligibility and restrictions | Deployed and live-verified |
| Common turnover requests | `/apartment-cleanout-springfield-mo` | Ordinary unit-turnover intent | Deployed and live-verified |
| Common turnover requests | `/eviction-cleanout-springfield-mo` | Completed legal-process cleanout context | Deployed and live-verified |
| Official resources | `/springfield-junk-disposal-guide` | Local disposal research | Deployed and live-verified |
| Related links | `/commercial-junk-removal-springfield-mo` | Managed-property and multi-unit path | Deployed and live-verified |
| Related links | `/junk-removal-cost-springfield-mo` | Quote factors | Deployed and live-verified |
| CTA | `#quote` | Photo-and-scope quote path | Deployed and live-verified |
| Guides hub | `/rental-turnover-cleanout-checklist-springfield-mo` | New checklist discovery | Deployed and live-verified |

Production deployment completed through PR #53 at merge commit `04a1748104c1df996b0b737d58252cbd3112cb87` on 2026-07-23. The live checklist returned HTTP 200 and byte-matched the merged file. The sitemap and guides-hub link are live, and desktop/mobile QA passed without console errors or horizontal overflow. No service-page inbound links were added. Indexing was not requested, and outreach remains prohibited without separate approval.

## QA Checklist for Future Link Edits

- Confirm every destination exists and uses extensionless canonical URL paths.
- Run local link QA after production HTML edits.
- Avoid adding links to a future page until that page exists and is approved.
- Keep hub navigation stable unless a separate IA update is approved.
- Confirm link additions do not trigger sitemap changes unless a new page is separately approved.

*Construction-debris, yard-waste, and accepted-items links are deployed and live-verified. Remaining cluster link proposals still require separate approval. Do not request indexing again for the correctly requested construction-debris or yard-waste pages. Do not request either accepted-items URL again now while the `.html` indexing-URL variance is settling; later inspect only the extensionless canonical.*

## 2026-07-24 Student Move-Out Checklist Production Links

| Source | Destination | Purpose | Status |
|---|---|---|---|
| Guides hub | `/springfield-student-move-out-donation-disposal-checklist` | Discover the new neutral student resource | Deployed and live-verified |
| Checklist breadcrumb and related links | `/junk-removal-guides-springfield-mo` | Guide hierarchy | Deployed and live-verified |
| Bulky-item planning | `/furniture-removal-springfield-mo` | Furniture-specific path | Deployed and live-verified |
| Mattress planning | `/mattress-removal-springfield-mo` | Mattress-specific path | Deployed and live-verified |
| Appliance planning | `/appliance-removal-springfield-mo` | Appliance-specific path | Deployed and live-verified |
| Official research | `/springfield-junk-disposal-guide` | Broader local disposal resource | Deployed and live-verified |
| Official research | `/what-items-can-be-removed-springfield-mo` | Confirm-first item guidance | Deployed and live-verified |
| Related requests | `/apartment-cleanout-springfield-mo` | Off-campus apartment path | Deployed and live-verified |
| Related guidance | `/junk-removal-cost-springfield-mo` | Quote factors | Deployed and live-verified |
| CTA | `#quote` | Photo-and-scope quote path | Deployed and live-verified |

No service-page inbound links, global navigation, footer, or unrelated page links changed. Deployment completed through PR #62. No indexing request or outreach has been authorized or performed for this page.

## 2026-07-21 Commercial Junk Local-Draft Links

| Source section | Destination | Anchor text | Reason | Status |
|---|---|---|---|---|
| Property-manager details | `/apartment-cleanout-springfield-mo` | apartment cleanout | Rental-turnover path | Deployed and live-verified |
| Property-manager details | `/eviction-cleanout-springfield-mo` | eviction cleanout | Landlord/authorization path | Deployed and live-verified |
| Related services | `/construction-debris-removal-springfield-mo` | Construction Debris | Business renovation path | Deployed and live-verified |
| Helpful guides | `/junk-removal-cost-springfield-mo` | Commercial Quote Factors | B2B quote preparation | Deployed and live-verified |
| Materials section | `/what-items-can-be-removed-springfield-mo` | accepted-items guide | Confirm unusual or regulated items | Deployed and live-verified |
| Helpful guides | `/how-junk-removal-works-springfield-mo` | How Quote Requests Work | Process reassurance | Deployed and live-verified |
| Related services | `/junk-removal-springfield-mo` | General Junk Removal | Core commercial-intent path | Deployed and live-verified |

No inbound pages, hubs, sitemap, navigation, or footer were changed. Production deployment completed through PR #35 at merge commit `388504b` on 2026-07-21. Live page returned HTTP 200 and byte-matched the merged file. GSC inspection on 2026-07-21 confirmed **URL is on Google** / **Page is indexed**. The July 4 crawl snapshot showed crawl allowed, successful fetch, indexing allowed, a legacy `.html` user-declared canonical, and the inspected extensionless URL as Google-selected canonical. One approved indexing request was submitted for the exact extensionless URL and added to the priority crawl queue. No second request or sitemap resubmission occurred; await recrawl and refreshed search data.

## Eviction-cleanout outbound links — deployed 2026-07-23

| Source section | Destination | Anchor purpose | Status |
|---|---|---|---|
| Materials requiring confirmation | `/what-items-can-be-removed-springfield-mo` | Route restrictions and acceptance questions | Deployed and live-verified |
| Related services | `/apartment-cleanout-springfield-mo` | Separate ordinary move-out intent from eviction intent | Deployed and live-verified |
| Related services | `/commercial-junk-removal-springfield-mo` | Route property-manager and multi-unit requests | Deployed and live-verified |
| Related services | `/house-cleanout-springfield-mo` | Route larger residential cleanouts | Deployed and live-verified |
| Related services | `/furniture-removal-springfield-mo` | Route furniture-specific requests | Deployed and live-verified |
| Quote preparation | `/junk-removal-cost-springfield-mo` | Explain volume, labor, access, and disposal factors | Deployed and live-verified |
| Related services | `/junk-removal-springfield-mo` | Return broader requests to the core money page | Deployed and live-verified |

No inbound pages, navigation, footer, sitemap, or new URL changed. Production deployment completed through PR #45 at merge commit `f317e19ba3517db06ff38e76ca6dee6e3d562d5d` on 2026-07-23. Cloudflare Pages deployment succeeded at `2026-07-23T06:11:45Z`. The extensionless production URL returned HTTP 200 and byte-matched the merged file; live QA passed with no blocking defect. GSC reported **URL is on Google** and **Page is indexed** for the exact extensionless URL. Discovery showed no referring sitemap or referring page. The last crawl was July 4, 2026 at 3:32:44 PM by Googlebot smartphone; crawling was allowed, the page fetch succeeded, and indexing was allowed. That older crawl reported the legacy `.html` URL as user-declared canonical, while Google selected the inspected extensionless URL. One indexing request was submitted successfully for the exact extensionless URL and added to the priority crawl queue. No second request, other URL submission, or sitemap resubmission occurred; no quota warning appeared. Await recrawl and refreshed canonical/search data; do not repeat the request now.

## 2026-07-22 Junk Removal Cost Deployed Links

| Source section | Destination | Anchor text | Reason | Status |
|---|---|---|---|---|
| Local rules | `/what-items-can-be-removed-springfield-mo` | what items require confirmation | Connects restricted materials to quote eligibility | Deployed and live-verified |
| Project factors | `/furniture-removal-springfield-mo` | furniture | Furniture-specific size/access factors | Deployed and live-verified |
| Project factors | `/mattress-removal-springfield-mo` | mattress removal | Mattress-specific condition/disposal context | Deployed and live-verified |
| Project factors | `/appliance-removal-springfield-mo` | appliance removal | Appliance weight, utility, and refrigerant confirmation | Deployed and live-verified |
| Project factors | `/garage-cleanout-springfield-mo` | garage cleanout | Mixed-clutter and access factors | Deployed and live-verified |
| Project factors | `/yard-waste-removal-springfield-mo` | yard waste removal | Brush, bag, stump, soil, and facility-rule factors | Deployed and live-verified |
| Project factors | `/construction-debris-removal-springfield-mo` | construction debris guide | Dense and material-specific debris factors | Deployed and live-verified |
| Project factors | `/commercial-junk-removal-springfield-mo` | commercial junk removal | Authorization, access-window, and B2B quote path | Deployed and live-verified |
| DIY comparison | `/what-items-can-be-removed-springfield-mo` | accepted-items and confirmation guide | Routes unusual materials to the central qualification page | Deployed and live-verified |
| DIY comparison | `/how-junk-removal-works-springfield-mo` | how junk removal works | Explains request, review, and scheduling | Deployed and live-verified |
| Related services | `/junk-removal-springfield-mo` | General junk removal path already present through site navigation | Core conversion path | Deployed and live-verified |

Official outbound references: Noble Hill Sanitary Landfill, Yardwaste Recycling Center, Springfield mattress recycling, and Material Know How. No inbound pages, sitemap, navigation, footer, or new page was changed. Production deployment completed through PR #38 at merge commit `502e0876eb78b1deac2e90d0bcae66fec2c8ba9b` on 2026-07-22. The extensionless production URL returned HTTP 200 with no redirect and byte-matched the merged file. Live QA passed with no blocking defects. GSC initially reported **URL is not on Google** and **URL is unknown to Google**, with no referring sitemap/page and crawl, fetch, indexing-permission, and canonical fields shown as `N/A`. One indexing request was then submitted successfully for the exact extensionless URL, and Google added it to the priority crawl queue. No second request or sitemap resubmission occurred; await initial crawl/index processing and refreshed data.
