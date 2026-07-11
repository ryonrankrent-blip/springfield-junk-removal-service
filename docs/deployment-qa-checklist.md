# Deployment QA Checklist

## Pre-deploy

- [x] Run `./scripts/qa-check.sh` — all checks pass
- [x] Run `./scripts/link-check.sh` — no broken internal links
- [x] Verify sitemap = 30 URLs
- [x] Spot-check 10 priority pages locally
- [ ] Confirm no unintended files in deploy bundle
- [ ] Confirm `docs/` and `scripts/` inclusion policy (optional on static host)

## Deploy steps (awaiting approval)

- [ ] Push to hosting provider
- [ ] Verify HTTPS certificate
- [ ] Purge CDN cache if applicable

## Post-deploy

- [ ] Run proof-of-life checklist
- [ ] Test form submission end-to-end
- [ ] Test phone click on mobile
- [ ] Verify GTM preview mode events
- [ ] Submit updated sitemap to Search Console

## Rollback triggers

- Formspree submissions fail
- GTM container missing
- Broken phone link
- Unsupported operator claims reappear on live site
