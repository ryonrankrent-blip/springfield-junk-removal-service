# Authority / Content Gap Review — Springfield vs Auburn

**Date:** 2026-07-11  
**Springfield site:** https://springfieldjunkremovalservice.com (30 pages, static HTML)  
**Auburn reference:** auburnsepticpumping.com (57+ pages, Next.js, post-launch authority system)  
**Purpose:** Identify what Springfield has, what Auburn has that Springfield lacks, and a guarded 30-day plan.

---

## 1. What Springfield already has

| Capability | Springfield status |
|---|---|
| Claim-safe copy sitewide | ✅ Complete (PR #11) |
| Hub IA (services / areas / guides) | ✅ 3 hub pages |
| Money page + 18 services | ✅ |
| 5 city pages | ✅ Greene County satellites |
| 3 guide pages | ✅ Cost, items, process |
| Trust/process blocks | ✅ Homepage + child pages |
| FAQ + JSON-LD | ✅ LocalBusiness + FAQPage |
| Sitemap (30 URLs) | ✅ Live |
| QA scripts | ✅ `qa-check.sh`, `link-check.sh` |
| RankRentOS docs folder | ✅ 11+ files |
| Production deploy | ✅ Cloudflare Pages `2006f8b` |
| GTM + analytics-events.js | ✅ Event hooks in place |
| Citation research template | ✅ Prepared (not executed) |

---

## 2. What Auburn has that Springfield lacks

| Gap | Auburn | Springfield | Reusable? | Niche-specific? |
|---|---|---|---|---|
| **Search Console baseline** | GSC verified, performance snapshots | Property exists — baseline not yet captured in docs | ✅ Yes | No |
| **Bing Webmaster Tools** | Connected | Not documented | ✅ Yes | No |
| **GA4 key events mapped** | `click_call`, `click_quote_button`, `generate_lead` | Events fire via `analytics-events.js`; GA4 mapping unconfirmed | ✅ Yes | No |
| **Blog / content hub** | 20 blog posts + `/blog/` hub | 3 static guides only | ✅ Pattern | Content topics differ |
| **City depth** | 17 service-area pages | 5 city pages | ✅ Pattern | Geo names differ |
| **Citations live** | 7 listings | 0 | ✅ Process | Platform selection differs |
| **Backlink / linkable asset plan** | Placer County checklist asset + outreach logs | None | ✅ Pattern | Asset topic differs |
| **Ranking baseline** | Manual SERP + GSC snapshots | None yet | ✅ Yes | Queries differ |
| **Proof-of-life weekly tracker** | Work logs + GSC metrics | Template created (empty) | ✅ Yes | No |
| **Renter-readiness pipeline** | Audit, pool, offer, outreach scripts | Checklist only | ✅ Yes | Offer terms differ |
| **Maintenance growth audit** | AUBURN_MAINTENANCE_GROWTH_AUDIT_001 | Production baseline started | ✅ Yes | No |
| **Next.js / shared components** | Component model, `lib/site.ts` | Static HTML per page | Future refactor | No |
| **Internal link scale** | 57 pages, GSC reports 43+ internal links | 30 pages, 691 local links | ✅ Pattern | No |

---

## 3. Recommended 30-day authority plan

| # | Task | Est. time | Approval required | Reusable | Notes |
|---|---|---:|---|---|---|
| 1 | Verify existing GSC property + confirm sitemap status | 30 min | No (read-only) | ✅ | Property already set up — do not create new |
| 2 | Capture GSC Page Indexing baseline | 20 min | No | ✅ | Record indexed / not indexed counts |
| 3 | Inspect Tier 1 extensionless canonical URLs | 30 min | **Yes** for indexing requests | ✅ | Do not bulk-submit |
| 4 | Connect Bing Webmaster + sitemap | 20 min | No | ✅ | Secondary index |
| 5 | Run conversion verification (manual) | 45 min | **Yes** — separate approval for live form/call test | ✅ | Use `conversion-verification-checklist.md` |
| 6 | Record week-1 proof-of-life metrics | 20 min/week | No | ✅ | `proof-of-life-weekly-tracker.md` |
| 7 | Citation platform inspection (top 4) | 2 hrs | **Yes** before any claim/submit | ✅ | Research only — no listing creation authorized |
| 8 | Manual SERP baseline (5 queries) | 45 min | No | ✅ | junk removal springfield mo, etc. |
| 9 | Prepare sitemap canonical-alignment fix | 1 hr | **Yes** before production edit | ✅ | Do not edit sitemap in doc batch |
| 10 | Linkable asset plan (1 checklist/guide) | 3 hrs | **Yes** before publish/outreach | ✅ | e.g. "Springfield move-out junk checklist" |

**Estimated total (30 days):** ~15–20 hours execution + ~1 hr/week monitoring

---

## 4. Priority order (matches Auburn phase: Indexing → Authority → Conversion)

### Week 1
- Verify existing GSC property + confirm sitemap status (read-only)
- Capture GSC Page Indexing baseline
- Inspect Tier 1 extensionless canonical URLs
- Week-1 proof-of-life row

### Week 2
- Manual SERP baseline
- Citation candidate inspection (read-only)
- GA4/GTM event confirmation

### Week 3–4
- Linkable asset plan draft (no outreach)
- Evaluate guide expansion vs citation corrections first
- Renter-readiness snapshot after metrics exist

---

## 5. Junk-removal-specific opportunities (not in Auburn)

| Opportunity | Rationale |
|---|---|
| Item acceptance guide depth | `what-items-can-be-removed` supports long-tail "what will junk removal take" |
| Move-out / rental cleanout cluster | apartment + eviction pages support property-manager queries |
| Heavy-clutter page (URL retained) | Differentiated from standard hoarding operator claims |
| Single-item pages (mattress, couch, hot tub) | Long-tail pickup intent |
| Same-day FAQ with explicit "not guaranteed" | Claim-safe urgency page |

---

## 6. Items deliberately deferred

- Google Business Profile creation/editing
- Any paid directory or lead platform
- CallRail or DNS changes
- Production content edits (unless verified defect)
- Renter contact or outreach

---

## 7. Recommended next action

1. Commit the corrected documentation batch
2. Verify the existing GSC property and current sitemap status
3. Capture GSC baseline data
4. Manually inspect Tier 1 extensionless canonical URLs
5. Prepare, but do not execute, a sitemap canonical-alignment correction
6. Request separate approval for live conversion tests and indexing requests

---

*Comparison based on Auburn Septic files in `RankRentOS/11_projects/auburn-septic-ca/` and Springfield `docs/` + live production verification 2026-07-11.*
