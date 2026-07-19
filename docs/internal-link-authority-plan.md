# Internal Link Authority Plan — Springfield Content Clusters

**Status:** Planning complete; construction-debris authority links **deployed**; yard-waste draft links implemented locally — **not deployed**
**Date:** 2026-07-17; construction-debris deploy/indexing update 2026-07-18; yard-waste draft update 2026-07-18
**Scope:** Construction debris, yard waste, accepted items, commercial junk removal, junk removal cost, and future disposal guide

## Guardrails

- This plan documents proposed links for remaining clusters.
- Construction-debris page links listed below were implemented, deployed on `ca32eca`, and verified live on 2026-07-18.
- Yard-waste page links listed below were added in the 2026-07-18 local draft only and are **not deployed**.
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
| `junk-removal-guides-springfield-mo.html` | `/springfield-junk-disposal-guide` | Springfield junk disposal guide | Future guide card | Add linkable asset after approval | N/A |
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
| Accepted items | Add links to mattress and commercial pages if relevant sections are added. |
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

## 2026-07-18 Yard Waste Draft Link Changes

| Source section | Destination | Anchor text | Reason | Status |
|---|---|---|---|---|
| Official local resources | City Yardwaste Recycling Center | City Yardwaste Recycling Center | Supports city yard-waste drop-off, brush guidelines, and bag/container notes | Added in local draft |
| Official local resources | City Material Know How | City Material Know How landfill restrictions for yardwaste | Supports landfill ban for leaves, grass, limbs, and brush | Added in local draft |
| Official local resources | Noble Hill Sanitary Landfill | Noble Hill Sanitary Landfill customer information | Supports landfill customer-guideline and Material Know How referral context | Added in local draft |
| Official local resources | Waste Wizard | Springfield Waste Wizard item lookup | Gives users an official item-specific lookup without copying item database content | Added in local draft |
| Official local resources | Missouri DNR PUB2050 | Missouri DNR special waste / landfill exclusion guidance | Supports state landfill-exclusion context for yard waste | Added in local draft |
| Helpful related pages | `/junk-removal-springfield-mo` | General Junk Removal | Routes broader mixed-junk requests back to the money page | Added in local draft |
| Helpful related pages | `/what-items-can-be-removed-springfield-mo` | What Items Can Be Removed | Routes mixed outdoor / restricted-material questions to accepted-items guide | Added in local draft |
| Helpful related pages | `/junk-removal-cost-springfield-mo` | Junk Removal Cost Factors | Connects volume, access, bagging, and disposal requirements to quote education | Added in local draft |
| Helpful related pages | `/construction-debris-removal-springfield-mo` | Construction Debris Removal | Distinguishes organic yard waste from lumber/remodel debris | Added/retained in local draft |
| Helpful related pages | `/garage-cleanout-springfield-mo` | Garage Cleanouts | Routes outdoor/garage cleanup crossover | Added/retained in local draft |
| Materials section | `/construction-debris-removal-springfield-mo` | construction debris removal | Routes lumber, fencing, pallets, remodel leftovers | Added in local draft |
| Materials section | `/what-items-can-be-removed-springfield-mo` | what items can be removed | Routes broader outdoor clutter questions | Added in local draft |
| Materials section | `/garage-cleanout-springfield-mo` | garage cleanout | Routes garage/outdoor clutter crossover | Added in local draft |
| Examples section | `/junk-removal-cost-springfield-mo` | junk removal cost guide | Explains volume/access/disposal quote factors | Added in local draft |
| Examples section | `/junk-removal-springfield-mo` | junk removal in Springfield, MO | Routes broader service requests to the money page | Added in local draft |

No sitemap, hub navigation, footer, or new-page links were changed in the yard-waste draft. Deployment and indexing were not performed.

## QA Checklist for Future Link Edits

- Confirm every destination exists and uses extensionless canonical URL paths.
- Run local link QA after production HTML edits.
- Avoid adding links to a future page until that page exists and is approved.
- Keep hub navigation stable unless a separate IA update is approved.
- Confirm link additions do not trigger sitemap changes unless a new page is separately approved.

*Construction-debris links are deployed and live-verified. Yard-waste draft links are local only and not deployed. Remaining cluster link proposals still require separate approval. Do not request construction-debris indexing again.*
