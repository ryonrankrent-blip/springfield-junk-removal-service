# Proof-of-Life Weekly Tracker — Springfield

**Site:** https://springfieldjunkremovalservice.com  
**Started:** 2026-07-11 (post PR #11 production deploy)  
**GSC baseline captured:** 2026-07-11  
**Recheck window:** July 18–25, 2026  
**Update cadence:** Weekly (Monday recommended)

---

## Weekly log

| Week ending | Indexed pages | Impressions | Clicks | Avg position | Top queries | Top landing pages | Phone calls | Form leads | Spam leads | Citations live | Backlinks found | Renter-readiness | Notes / actions |
|---|---:|---:|---:|---:|---|---|---|---:|---:|---:|---:|---|---|
| 2026-07-11 | 37 | 4.64K (28d) / 1.47K (7d) | 6 (28d) / 2 (7d) | 41.4 (28d) / 40.9 (7d) | construction debris removal (~5.9); commercial junk removal (~15.7); yard waste removal services (1 click, 10.0); junk removal (75 imp, 24.2) | Pending export | — | — | — | 0 | — | Not renter-ready | PR #12+13 deployed; GSC baseline captured; 4 Tier 1 indexed, 8 indexing requests submitted; hub JSON-LD fixed; recheck July 18–25 |
| 2026-07-18 | | | | | | | | | | | | | |
| 2026-07-25 | | | | | | | | | | | | | |
| 2026-08-01 | 33 | 5,697 (28d) | 8 (28d) | 37.8 (28d) | garage cleaning services (1 click / 2 imp); yard waste removal services (1 / 2); shed tear down and removal near me (1 / 2); junk removal (0 / 280); commercial junk removal (0 / 147) | yard waste (3 clicks / 461 imp); garage cleanout (2 / 271); eviction cleanout (1 / 398); mattress removal (1 / 86); shed removal (1 / 42); homepage (0 / 1,866); money page (0 / 715) | 0 (Jul 25-Aug 1) | 0 real; latest inbox entries are tests | 3 total, all obvious solicitations/spam | 0 | 0 in GSC | Not renter-ready | GSC growth vs Jul 11 baseline: impressions +22.8%, clicks +33.3%, avg position improved 3.6. GA4 last 7d: 16 active users, 21 views, 69 events, 1 key event, 1 click_quote_button. Six outreach prospects still pending with no detected reply. Review 5 redirect errors, 1 canonical mismatch, and high-impression/zero-click homepage and money page before further changes. |
| 2026-08-08 | | | | | | | | | | | | | |
| 2026-08-15 | | | | | | | | | | | | | |

---

## Data sources

| Metric | Source | Notes |
|---|---|---|
| Indexed pages | Google Search Console → Pages | Also check Bing Webmaster |
| Impressions / clicks / position | GSC Performance (28-day rolling) | Export top queries + landing pages |
| Top queries | GSC Performance | Focus: junk removal springfield mo, furniture removal, cleanout |
| Top landing pages | GSC Performance | Compare homepage vs money page vs hubs |
| Phone calls | CallRail | Do not change routing; read-only |
| Form leads | Formspree inbox | Tag test leads separately |
| Spam leads | Formspree + manual review | Count obvious spam/test |
| Citations live | `citation-candidate-research.md` tracker | Update when listings go live |
| Backlinks | GSC Links + manual check | Record linking domains |
| Renter-readiness | `renter-readiness-checklist.md` | Summarize blockers |

---

## Weekly action template

1. Record GSC coverage changes (new indexed / dropped URLs)
2. Record top 5 queries and whether position moved
3. Record call + form volume (even if zero)
4. Note any live-site defects (do not fix without approval)
5. Flag citation or authority tasks ready for approval
6. Update `indexing-priority-tracker.md` GSC status column for Tier 1 **extensionless canonical** URLs

---

## Alert thresholds (manual review)

| Signal | Action |
|---|---|
| Money page not indexed after 14 days | Inspect URL in GSC; check canonical/redirect |
| Form submissions = 0 for 30+ days with impressions | Run conversion verification checklist |
| Call volume = 0 with 500+ impressions | Review SERP position + CTA visibility |
| Unsupported operator claims on live site | Stop citations/outreach; report defect first |
| New spam spike in Formspree | Document; do not change endpoint without approval |
