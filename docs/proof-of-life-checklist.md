# Proof-of-Life Checklist

Run after deployment to confirm the live site is functional.

## Core functionality

- [ ] Homepage loads over HTTPS
- [ ] Phone link `tel:4172425370` works on mobile
- [ ] Quote form submits to Formspree (`mojzdkvg`)
- [ ] Form hidden fields present: site, market, niche, service
- [ ] GTM container loads (`GTM-GDJF54DV`)
- [ ] `analytics-events.js` fires on call click and form submit

## New hub pages

- [ ] `/junk-removal-services-springfield-mo.html` returns 200
- [ ] `/junk-removal-service-areas-springfield-mo.html` returns 200
- [ ] `/junk-removal-guides-springfield-mo.html` returns 200

## SEO files

- [ ] `/sitemap.xml` lists 30 URLs
- [ ] `/robots.txt` references sitemap
- [ ] Favicon displays in browser tab

## Spot-check pages

- [ ] Homepage hub links work
- [ ] Money page form works
- [ ] Hot tub page — no operator disconnect claims in hero
- [ ] Hoarder page — heavy clutter + hazmat disclaimer visible

## CallRail (do not change without approval)

- [ ] Website calls route to expected tracking number
- [ ] Call events appear in analytics pipeline
