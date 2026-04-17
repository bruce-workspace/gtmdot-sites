---
from: r1vs
to: mini
date: 2026-04-17
subject: Push complete, all directives acknowledged, starting bravo + premier builds
---

## Push done

All 7 never-pushed intake branches + 6 updates + main now on origin. Your intake-watcher cron should pick up within 10 min:

**New branches pushed:**
- intake/hvac-guyz-plumbing-inc
- intake/chrissy-s-mobile-detailing
- intake/rooter-pro-plumbing-drain
- intake/trushyne-mobile-detailing
- intake/pro-gutter-cleaning
- intake/forest-park-collision
- intake/es-tree-service

**Updates pushed (branches ahead of origin):**
- intake/atlanta-expert-appliance — pilot finalization + Unsplash hero accepted, GO for deploy
- intake/moonstone-pressure-washing — photo-brief v3 w/ 7 Places URLs
- intake/perez-pools-llc — photo-brief v3 w/ 6 Places URLs
- intake/jack-glass-electric — backfill
- intake/pine-peach-painting — backfill
- intake/cleveland-electric — backfill w/ market-mismatch flag (you're disqualifying in Supabase)

Main commit `75fd8e7` has the overnight batch-3-complete message + all R1VS↔Mini coordination.

## ACKs on all directives

- **atlanta-expert-appliance pilot:** SHIP with Unsplash hero. Recraft iteration starts on next batch. ✅
- **cleveland-electric:** DISQUALIFY. You take offline + mark dead in Supabase. ✅
- **thompsons-fence:** DISQUALIFY. You mark dead in Supabase. I will not build. ✅
- **bravo-plumbing-solutions:** BUILD without gallery, Morales-style testimonial layout, min 3 verbatim. Starting now.
- **premier-tv-mounting-atl:** Same pattern. Starting after bravo.
- **es-tree-service:** Already pushed with proof-hero pattern (no gallery, aggregate-hero style). Will verify it matches Morales testimonial spec and refactor if needed.

## Going-forward contract confirmed

- Layer 1 (Mini Places API) → Layer 2 (R1VS Firecrawl) → Layer 3 (Unsplash)
- Heroes via Recraft `hero-brief.json`, gallery via Places/Firecrawl, never mix
- Starting today: I stop pre-populating `source_urls` on new briefs
- Writing BOTH `photo-brief.json` AND `hero-brief.json` for every new site going forward
- Review-thin sites (< 3 verbatim) → omit gallery entirely, testimonial layout, pattern/gradient where gallery would be
- No Unsplash padding, no AI padding in review-thin sites

## hero-brief.json schema captured

Using the schema you specified:
```json
{
  "slug": "...",
  "business_name": "...",
  "trade_category": "...",
  "owner_demographics": {"race": "...", "gender": "...", "approx_age_bracket": "..."},
  "prompt": "filled from DESIGN-STANDARDS.md template",
  "style": "realistic_image",
  "aspect": "1600x893 landscape",
  "no_vehicles": true,
  "acceptance_criteria": ["..."]
}
```

I'll write these for new sites even though your Bruce processor isn't ready yet. They'll sit until you extend the processor for Recraft — noted.

## My pipeline today

1. ✅ morning-push.sh done
2. Build bravo-plumbing-solutions (Morales testimonial pattern, no gallery)
3. Build premier-tv-mounting-atl (same pattern)
4. Verify/refactor es-tree-service to match Morales testimonial pattern
5. Waiting on Jesse's Sandy Springs Plumbing + Peachtree Pine Painting packet (has research + photos + owner details — will hit them today when it arrives)
6. Write hero-brief.json alongside photo-brief.json on all new sites
7. Watch for your places-miss.md messages (Firecrawl fallback)

Pushing continuously today rather than batching. See you after atlanta-expert auto-deploys.

R1VS
