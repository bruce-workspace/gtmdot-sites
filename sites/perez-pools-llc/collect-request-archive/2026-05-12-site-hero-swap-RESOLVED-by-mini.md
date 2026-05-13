---
slug: perez-pools-llc
requested_by: mini
requested_at: 2026-05-12T23:00:00Z
priority: high
type: site-hero-swap
---

# Collect-request — Perez Pools (swap site hero to use postcard hero)

## Why

Jesse reviewed the postcard preview and the site side-by-side. The
**postcard hero** (`sites/perez-pools-llc/photos-generated/hero-postcard.jpg`,
3840×2160, gpt-image-2, infinity pool at sunset with mountain backdrop) is
strikingly better than the current site hero — which appears to be a generic
empty-pool photo with a "Perez Pools" logo overlay slapped on top. The
overlay screams "stock template" and undermines the rest of the site.

We want the same beautiful postcard hero used on the live site's hero
section, so the prospect (Chris Perez) gets a coherent message: same
strong visual on the postcard he holds, same strong visual when he visits
the URL.

## What we need

1. **Copy** `sites/perez-pools-llc/photos-generated/hero-postcard.jpg`
   over the current `photos/hero.jpg` in whatever source the
   `perez-pools-llc.pages.dev` deploy uses
2. **Rebuild/redeploy** the prospect site
3. **Verify** `https://perez-pools-llc.pages.dev/photos/hero.jpg` now
   returns the new hero (3840×2160)
4. **Drop a sentinel** so Mini knows to re-capture postcard screenshots
   afterward (the site-screenshot thumbnails on the postcard back need
   to reflect the new hero too)

## §11.11.5 reminder

The postcard hero's `intended_slot_context` includes `aspirational-business-OK`,
which covers the site hero slot. License note ("Synthetic image. Do not
represent as actual company work.") stays in `bruce-asset-intel.json` for
provenance — the hero is allowed in aspirational positions but never as
real-job proof or before/after.

## Budget

- max_wallclock_minutes: 5

## Output

- Updated photos/hero.jpg on the prospect site deploy
- `bruce-collected.md` appended with "## Site hero swap v1 (2026-05-12) — postcard hero promoted to site hero"
- Sentinel: `messages/2026-05-12-r1vs-perez-pools-hero-swapped.md`

— Mini

---

## RESOLUTION (Mini, 2026-05-12 19:08 PDT)

Resolved by Mini directly (not by Bruce). Per HANDOFF-CONTRACT §11.11.2:
deploy-integration into photos/ is Mini's lane, not Bruce's. This request
was mis-routed.

Action taken:
- Downloaded live prospect site from <slug>.pages.dev
- Copied gtmdot/postcards/<slug>-hero.jpg into photos/hero.jpg
- wrangler pages deploy <slug>
- Re-captured desktop + mobile screenshots
- Redeployed gtmdot-postcards CDN

Verified: https://<slug>.pages.dev/photos/hero.jpg matches
https://gtmdot-postcards.pages.dev/<slug>-hero.jpg (same byte size).

Bruce: archive without action.
