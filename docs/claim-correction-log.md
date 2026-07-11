# Claim Correction Log

**Batch date:** 2026-07-11

## Global replacement patterns

| Before | After |
|---|---|
| We haul / we load / we handle / we clear | Removal/loading scope confirmed during quote process |
| Our crew / our truck | Pickup-day language / "the load" |
| We disconnect / we tear down / we dismantle | Utility disconnect or teardown scope confirmed during quote |
| We donate / we recycle | Donation or recycling options may be available |
| Hoarding cleanout (body) | Heavy clutter cleanout |
| Full-service junk hauling | Junk removal requests |
| a local provider can | Your request can be reviewed for |

## Page-specific corrections

### `hot-tub-removal-springfield-mo.html`
- Title: "Spa Demolition" → "Spa Removal"
- Meta/schema: removed operator disconnect/break-down claims
- Body: utility disconnect and teardown scope require confirmation

### `shed-removal-springfield-mo.html`
- Title: "Shed Teardown" → "Shed Removal"
- FAQ/body: teardown scope confirmed during quote, not assumed

### `appliance-removal-springfield-mo.html`
- Disconnect FAQ: utility disconnect status confirmed during quote

### `hoarder-cleanout-springfield-mo.html`
- Body: "heavy clutter cleanout" throughout visible copy
- FAQ title: "Heavy Clutter Cleanout FAQ"
- Biohazard, crime-scene, medical-waste, hazardous-material remediation explicitly not assumed

### `same-day-junk-removal-springfield-mo.html`
- Retained FAQ "Is same-day service guaranteed?" with explicit **No** answer
- Same-day framed as "when scheduling allows"

### `index.html`
- Hub cards: hot tub/shed cards use confirmation language
- Trust/process section added (`#trust-process`)
- Hub navigation block added

### All city pages (5)
- Meta descriptions: "We haul" → request-and-confirm language
- Body operator verbs replaced

### All service pages (18)
- Compact trust blurb before FAQ where applicable
- Hub links in related-links blocks

### Guides (3)
- "What We Can Haul" → "What Can Be Removed"
- Process language aligned to quote request model

## Schema alignment

LocalBusiness and FAQPage JSON-LD descriptions updated on high-risk pages to match visible claim-safe copy.
