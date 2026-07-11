# Reusable Patterns

## Market-specific (change per location/niche)

| Item | Springfield value | Where set |
|---|---|---|
| Business name | Springfield Junk Removal Service | Page copy, schema |
| Phone | (417) 242-5370 | All pages |
| Domain | springfieldjunkremovalservice.com | Canonical, Formspree `site` field |
| Market | Springfield, MO | Formspree `market` field |
| Niche | Junk Removal | Formspree `niche` field |
| GTM ID | GTM-GDJF54DV | Page `<head>` |
| Formspree ID | mojzdkvg | Form `action` |
| Service list | 18 services + 5 cities | Hub pages, sitemap |
| Service areas | Greene County cities | Service areas hub |

## Reusable (copy across niches)

### Page shell
- Header with logo + phone
- Breadcrumb
- Hero (H1 + CTA row)
- Content sections
- Trust/process block (`#trust-process`)
- Two-col quote form
- FAQ + JSON-LD
- Footer with hub links

### Trust/process block (full)
Documented in `scripts/fix-claims.py` as `TRUST_FULL`. Five elements:
1. How quote request works
2. Information to include
3. Items requiring confirmation
4. Service area and availability
5. No-obligation quote language

### Trust/process block (compact)
Single paragraph before FAQ on child pages.

### Claim-safe language rules
- "Your request can be reviewed for availability"
- "Pickup scope and accepted items are confirmed during the quote process"
- Avoid "a local provider can…" unless lead model supports it
- Avoid crew, truck, license, insurance, guaranteed availability
- Specialty services: confirm scope during quote

### Hub page generator
`scripts/create-hubs.py` — adapt `PAGES` array and grid content for new markets.

### QA scripts
- `scripts/qa-check.sh` — technical + claim-risk scan
- `scripts/link-check.sh` — internal link validation

### Documentation template
Copy `docs/` folder structure for each new market under the site repo or `11_projects/{market}/`.

## Future refactor options (not in scope)

- Extract shared CSS to `styles.css`
- Extract shared header/footer via build step
- Move to Next.js component model (see Auburn Septic in parent RankRentOS repo)
