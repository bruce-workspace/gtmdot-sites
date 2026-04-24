# Multi-page template scaffold

Per SKILL.md §3b, every R1VS site ships multi-page, not single-page. This
folder is the structural skeleton every build starts from.

## Why multi-page matters

Owners Google `[service] [city]` (e.g., "refrigerator repair Atlanta"). That
search rewards dedicated per-service URLs with unique content. One-pagers with
hash anchors don't compete. Every site we ship as a one-pager is pre-lost in
search.

## Pages in the scaffold

| File | Purpose |
|---|---|
| `index.html` | Homepage — hero, 3-5 service teasers, reviews bar, CTA |
| `services.html` | All services grid with links to per-service pages |
| `about.html` | Owner bio + service area + years in business + team |
| `contact.html` | Form + hours + phone + map + upload module |
| `service-page.html` | Template for ONE service page — copy per service |
| `_base.css` | Shared design tokens + layout + `.gtmdot-photo-slot` |

## Per-service pages (the SEO lever)

For each service in the business's vertical, create a dedicated page:

- HVAC example: `/ac-repair-atlanta.html`, `/heating-repair-atlanta.html`, `/thermostat-install-atlanta.html`, etc.
- Plumbing example: `/water-heater-repair-atlanta.html`, `/drain-cleaning-atlanta.html`, `/leak-detection-atlanta.html`
- Appliance example: `/refrigerator-repair-atlanta.html`, `/washer-dryer-repair-atlanta.html`

Each per-service page MUST have:

1. **Unique `<title>`** — includes service + city keywords
2. **Unique `<meta name="description">`** — 140-160 chars, includes service + city + trust signal
3. **Unique `<h1>`** — matches title intent
4. **JSON-LD `Service` schema** — references the parent LocalBusiness
5. **URL slug with keyword** — `/refrigerator-repair-atlanta.html`, not `/service-1.html`
6. **400-600 words of unique content** — not duplicated across service pages
7. **Specific photos** via `.gtmdot-photo-slot` with `data-context` matching the service
8. **Service-specific FAQs** (3-5) for long-tail queries

## Replacement tokens

Throughout the scaffold, `{{TOKEN_NAME}}` marks spots to fill in:

- `{{BUSINESS_NAME}}` — full business name
- `{{BUSINESS_NAME_SHORT}}` — short name (e.g., "Pine Peach" vs "Pine Peach Painting LLC")
- `{{CITY}}` — primary city
- `{{PHONE}}` — primary phone (in tel: format and display format)
- `{{EMAIL}}` — contact email
- `{{ADDRESS}}` — full mailing address
- `{{SERVICE_AREAS}}` — comma-separated cities/neighborhoods served
- `{{PRIMARY_CTA}}` — CTA verb from `TERMINOLOGY-MAPPING.md` (e.g., "Get a Free Estimate")
- `{{YEAR_FOUNDED}}` — founding year (or "YYYY" if unknown, flag it)
- `{{OWNER_NAME}}` — primary contact / owner name
- `{{OWNER_BIO}}` — 2-3 sentence owner bio
- `{{SERVICE_NAME}}` — specific service (per-service page only)
- `{{SERVICE_DESCRIPTION}}` — 400-600 word unique description
- `{{SERVICE_SCHEMA_URL}}` — URL of the service page itself
- `{{VERTICAL_ACCENT_COLOR}}` — hex color per `DESIGN-HEURISTICS.md` vertical palette

## Do NOT ship without

- `{{...}}` tokens filled in (pre-push-gate will reject if any remain)
- Per-service pages for every service in the vertical
- JSON-LD schema validated (paste into schema.org validator)
- Ambiguous photo slots with `data-context` (NO pre-written `<figcaption>`)

## Build flow with this scaffold

1. Copy `templates/multi-page/*` → `sites/<slug>/`
2. Replace `{{TOKEN_NAME}}` placeholders using RESEARCH.md + legitimacy-check.json + gbp_snapshot.json
3. Duplicate `service-page.html` once per service in the vertical, rename to `/service-slug.html`
4. Run `./scripts/pre-push-gate.sh <slug>` — must pass
5. Run `./scripts/verify-build.sh <slug>` — must pass
6. Push intake branch + write finalization message
