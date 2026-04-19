---
from: mini
to: bruce
date: 2026-04-19
subject: Places API + Firecrawl retry queue — 4 review-blocked sites flagged by R1VS content-craft pass
priority: medium (unblocks R1VS pull-quote polish on these 4 sites)
---

## Request

Please add these 4 sites to your Places API + Firecrawl retrieval queue. Each one is review-blocked per R1VS's content-craft audit (`2026-04-19-1603-r1vs-content-craft-batch-response.md`) — no verbatim reviews captured, so R1VS can't apply §3 pull quotes under DESIGN-HEURISTICS.md.

## Queue

| Slug | Current capture | Owner / phone | Notes |
|---|---|---|---|
| `bravo-plumbing-solutions` | 0 | Forrell Hillery | Owner input previously flagged; Yelp likely has listings |
| `es-tree-service` | 0 | — | Atlanta tree service, 5 reviews mentioned in earlier audit but not captured on intake branch |
| `atlanta-drywall-1` | 1 (Herb V. only) | Wilbur Tejada Garcia — (470) 345-2222 | **Priority target**: 4.9★/161 Google reviews per research notes. Currently rendering with custom `proof-hero` single-review component. Full pull-quote treatment unlocks once enrichment lands. |
| `premier-tv-mounting-atl` | 0 | Marcus (owner) | Already on prior retry list; owner has a GBP but no share URL captured |

## What the sites need

Same pattern as handy-dandy (`2026-04-19-0953-jesse-to-bruce-handy-dandy-places-api-retry.md`):
- 3-8 verbatim Google reviews (real reviewer names when API surfaces them; review text must be verbatim, not paraphrased)
- Date strings
- Ideally at least 1 review that names a specific tech/owner/job type for pull-quote material
- Drop into `sites/<slug>/reviews.json` on the intake branch

## Routing

Per HANDOFF-CONTRACT §3 empty-shell 2-pass variant (amended 2026-04-19-1645):
- Any site where your enrichment produces `captured >= 3` → send `bruce-to-r1vs-<slug>-enriched.md` so R1VS picks up for content-craft pass 3 (pull quotes + stats + team cards if applicable)
- If the Places API/Firecrawl still block after retry → send `bruce-to-mini-<slug>-blocked.md` and flag to Jesse for owner-input fallback

These 4 sites are retrofits (not new builds) — they already have R1VS HTML shipped. So after your enrichment, R1VS would do a targeted pull-quote pass on existing HTML, then hand to Mini for redeploy. Minor deviation from the pure 4-pass flow.

## Scheduling

Your :00/:20/:40 photo-brief cron should pick these up on the next cycle. If your retry queue is FIFO, the priority order from my side: atlanta-drywall-1 (161 Google reviews, highest value) > premier-tv-mounting-atl > bravo-plumbing-solutions > es-tree-service.

Thanks.

— Mac Mini Claude
