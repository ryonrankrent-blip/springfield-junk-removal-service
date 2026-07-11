# Proof-of-Life Weekly Tracker — Springfield

**Site:** https://springfieldjunkremovalservice.com  
**Started:** 2026-07-11 (post PR #11 production deploy)  
**Update cadence:** Weekly (Monday recommended)

Leave metric cells blank until data is collected manually. Do not invent numbers.

---

## Weekly log

| Week ending | Indexed pages | Impressions | Clicks | Avg position | Top queries | Top landing pages | Phone calls | Form leads | Spam leads | Citations live | Backlinks found | Renter-readiness | Notes / actions |
|---|---:|---:|---:|---:|---|---|---|---:|---:|---:|---:|---|---|
| 2026-07-11 | | | | | | | | | | 0 | | Pre-launch baseline | Production live; verify existing GSC property + baseline |
| 2026-07-18 | | | | | | | | | | | | | |
| 2026-07-25 | | | | | | | | | | | | | |
| 2026-08-01 | | | | | | | | | | | | | |
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
