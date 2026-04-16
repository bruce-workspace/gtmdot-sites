# R1VS Rebuild Brief — 51 Sites

**Date:** April 16, 2026
**From:** Mac Mini Claude (via Jesse)
**Repo:** github.com/bruce-workspace/gtmdot-sites

## Mission

Rebuild all 51 prospect sites in the GTMDot pipeline. You already built 3 (Jack Glass Electric, Pine Peach Painting, Cleveland Electric) that passed quality review. Now do the same for the rest.

## Priority Order

Work through the tiers in order. Tier 1 prospects were closest to conversion before outreach was paused.

| Tier | Count | Description |
|------|-------|-------------|
| **Tier 1** | 14 | `outreach_sent` — had active email sequences, rebuild first |
| **Tier 2** | 5 | `outreach_staged` + `qa_approved` — were next in line |
| **Tier 3** | 32 | `ready_for_review` — earlier in pipeline |

The full structured list with business details is in `rebuild-queue.json` in this repo.

## Site Structure (same as your 3 finished sites)

```
sites/<slug>/
  index.html          # Single file — inline CSS, inline JS, inline SVG icons
  photos/
    gbp-1.jpg         # Real GBP photos
    gbp-2.jpg
    ...
```

## Quality Requirements

These are the rules that caused every previous build to fail Jesse's review. Follow them exactly.

### Must Have
- **Google Reviews section** — real verbatim reviews pulled from GBP. REQUIRED unless the business has fewer than 5 reviews.
- **GBP photo gallery** — "Our Work" section with real GBP photos. REQUIRED for photo-heavy trades (landscaping, painting, pool, pressure washing, detailing, concrete, fencing, electrical, plumbing). If GBP only has office/building exteriors, skip the gallery and use a contextual Unsplash hero instead (like you did for Cleveland Electric).
- **Lucide SVG icons only** — inline SVGs from the Lucide set. No Font Awesome, no Material Icons, no hand-drawn, no mixed libraries.
- **Single Google Fonts link** — pick fonts that match the business personality. No system fonts, no Inter/Roboto defaults.
- **Mobile-first responsive** — sites must look great on phone first. Hamburger menu, floating phone CTA, tap-friendly buttons.
- **Real business data** — correct business name, phone, address, services from GBP. No placeholder content.

### Must NOT Have
- **No claim bar / popup / cookie banner** — Mac Mini injects these post-build using a shared template. Do NOT build your own.
- **No stock photos in service cards** — service cards are text-only or with icons. Gallery is the only place for photos.
- **No framework dependencies** — no React, no Tailwind CDN, no external JS. Everything inline.
- **No `<!-- CLAIM_BAR_ANCHOR -->` needed** — Mac Mini will find `</body>` and inject before it.

## Git Workflow

For each rebuilt site:

1. **Create a branch:** `git checkout -b intake/<slug>`
2. **Add files:** `sites/<slug>/index.html` + `sites/<slug>/photos/gbp-*.jpg`
3. **Commit and push:** `git push -u origin intake/<slug>`
4. **POST metadata** to the intake API (details below)

### Intake API

```
POST https://crm.cloakanddagger.co/api/site-intake
Authorization: Bearer <INTAKE_BEARER_TOKEN>
Content-Type: application/json

{
  "slug": "affordable-concrete-repair",
  "business_name": "Affordable Concrete & Repair",
  "trade_category": "concrete",
  "city": "Hawthorne",
  "state": "FL",
  "gbp_url": "https://maps.google.com/...",
  "gbp_place_id": "ChIJ...",
  "owner_name": null,
  "phone": "(555) 123-4567",
  "email": null,
  "source_notes": "Brief description of business from GBP research",
  "proposer_version": "1.0.0",
  "proposal_sha": "<git commit SHA of the intake branch>",
  "git_branch": "intake/affordable-concrete-repair",
  "manifest": {
    "proposed_services": ["Concrete Repair", "Driveway Resurfacing"],
    "photo_urls": ["photos/gbp-1.jpg", "photos/gbp-2.jpg"],
    "raw_gbp": {}
  }
}
```

**Responses:**
- `201` — accepted, site intake created
- `200` — replay (same slug + SHA already submitted)
- `400` — validation error: `{ error, field, code }` where code is one of: `MISSING_REQUIRED_FIELD`, `INVALID_SLUG`, `INVALID_STATE`, `INVALID_EMAIL`, `INVALID_VERSION`, `PAYLOAD_TOO_LARGE`
- `409` — slug already exists with different SHA: `{ error, field: "slug", code: "DUPLICATE_SLUG" }`
- `401` — bad or missing bearer token

**Auth token:** Jesse will provide the INTAKE_BEARER_TOKEN value. Store it for the session.

## What Happens After You POST

1. Mac Mini receives the metadata and records it in `site_intake` table
2. Jesse reviews the site in the CRM
3. Mac Mini pulls your git branch, injects the claim bar, and deploys to `<slug>.pages.dev`
4. Site moves through the pipeline: `received` -> `reviewing` -> `accepted` -> `built` -> `deployed`

## Data Source

Use the `rebuild-queue.json` file in this repo for the full prospect list. Each entry has:
- `slug` — use this as the folder name and git branch name
- `business_name`, `trade_category`, `city`, `state` — for the site content
- `gbp_url` — start your GBP research here (some are null — use Google Maps search)
- `email`, `phone`, `owner_name` — may be null, enrich from GBP
- `claim_code` — DO NOT use in the site; Mac Mini handles claim codes
- `current_stage` — for your reference only

## Batching

Build and submit sites one at a time. No need to batch. If you can do 5-10 per session, that's great. The intake API handles them as they come in.

## Questions?

Post to #site-build in Slack. Mac Mini monitors that channel.
