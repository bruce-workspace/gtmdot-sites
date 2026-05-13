---
slug: harrison-sons-electrical
requested_by: mini
requested_at: 2026-05-12T23:15:00Z
priority: high
type: site-hero-swap
---

# Collect-request — harrison-sons-electrical (swap site hero to use postcard hero)

## Why

Jesse policy decision 2026-05-12: **the gpt-image-2 postcard hero should also be the site hero** for every prospect. The gpt-image-2 model produces a more polished hero than any sourced/GBP photo we'd find. The single hero per prospect lives in two places (postcard + site) and they must match.

Right now the site hero is a different (older, lower-quality, or in some cases tiny/broken) file. Time-sensitive for this batch since outreach is going out today and tomorrow — when the prospect clicks through from the postcard, they should land on the same beautiful hero.

## What we need

1. **Copy** `sites/harrison-sons-electrical/photos-generated/hero-postcard.jpg` (3840×2160 or 3360×1872, gpt-image-2) over the current `photos/hero.jpg` in whatever source the `harrison-sons-electrical.pages.dev` deploy uses
2. **Rebuild and redeploy** the prospect site
3. **Verify** `https://harrison-sons-electrical.pages.dev/photos/hero.jpg` returns the new hero (size should match `https://gtmdot-postcards.pages.dev/harrison-sons-electrical-hero.jpg`)
4. **Drop a sentinel** message so Mini knows to re-capture postcard screenshots

## §11.11.5

The postcard hero's `intended_slot_context` includes `aspirational-business-OK`, which covers the site hero slot. License note ("Synthetic image. Do not represent as actual company work.") stays in `bruce-asset-intel.json` — the hero is allowed in aspirational positions, never as real-job proof or before/after.

## Budget

- max_wallclock_minutes: 5

## Output

- Updated `photos/hero.jpg` on the prospect site deploy
- `bruce-collected.md` appended with "## Site hero swap v1 (2026-05-12) — postcard hero promoted to site hero"
- Sentinel message in `messages/`

— Mini (batch swap, 13 prospects, policy: site hero == postcard hero)
