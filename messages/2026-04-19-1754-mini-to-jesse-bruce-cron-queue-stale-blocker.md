---
from: mini
to: jesse
date: 2026-04-19
subject: BLOCKER — Bruce cron queue is stale; Phase B (15 sites) + my retry queue (4 sites) aren't in Bruce's prompt
priority: medium (blocks Mini pass-3 deploy on the entire new Phase B batch)
---

## What I found this cycle

Bruce's `photo-brief-processor` cron has been firing every 20 min and returning `"no work this run"` on every cycle since R1VS's 19:14 finalization landed. Last 4 run logs all report the same thing:

> "i loaded the required files, synced main, and checked the urgent rebuilds plus the full tier 2 queue again. there are still no eligible slugs left without an enriched.md or blocked.md, so I exited cleanly with no changes."

The queue iterator works — it's checking for `bruce-to-mini-<slug>-enriched.md` or `-blocked.md` per slug correctly. The problem is the slug *list* Bruce iterates over is **hardcoded in the cron prompt** (`~/.openclaw/cron/jobs.json` → `photo-brief-processor.payload.message`), not pulled from `rebuild-queue.json` or from the messages/ finalization list.

## Bruce's current hardcoded queue (stale)

From the cron prompt:

- **Tier 2 Priority (14 slugs):** affordable-concrete-repair, tire-and-ride-mobile, locksmith-atlanta-pro, cityboys, intire-mobile-tire-shop, membrenos-pro-home-repair, tech-on-the-way, tuckers-home-services, plugged-electricians-atl, azer-pool, dream-steam, 24-hrs-mobile-tire-services, professional-gutter-cleaning, doctor-concrete-atl
- **Urgent Rebuilds (3):** moonstone-pressure-washing, perez-pools-llc, the-appliance-gals
- **Skip list:** atlanta-drywall-1, bravo-plumbing-solutions, chrissy-s-mobile-detailing, es-tree-service, forest-park-collision, hvac-guyz-plumbing-inc, jack-glass-electric, rooter-pro-plumbing-drain, trushyne-mobile-detailing, atlanta-expert-appliance, pine-peach-painting, sandy-springs-plumbing, handy-dandy-atlanta

Every single one of those slugs already has either enriched.md, blocked.md, or is intentionally skipped. So Bruce has literally nothing to do under its current prompt.

## What's missing from Bruce's queue

### 1. The 15 Phase B sites from R1VS's `2026-04-19-1914` finalization
atl-mobile-mechanics, atlanta-pro-repairs, done-right-drywall, golden-choice-prowash, harrison-sons-electrical, morales-landscape-construction, piedmont-tires, plumbingpro-north-atlanta, roberts-mobile-services, roswell-pro-plumber, sandy-springs-plumber-sewer-septic, sumptuous-mobile-detailing, tgp-home-services, the-smart-company-llc, thermys-mobile-tire-and-brakes

All 15 are in `rebuild-queue.json` tier_3_pipeline but Bruce's prompt only iterates tier 2.

### 2. The 4 retry sites from my `2026-04-19-1420` message
atlanta-drywall-1 (on skip list — correct for photos, but I asked for a **review-only** retry since reviews.json has captured=1), premier-tv-mounting-atl, bravo-plumbing-solutions (on skip list), es-tree-service (on skip list).

My message asked Bruce to retry Places API for reviews specifically on those 4 — Bruce's current prompt only does the full photo waterfall and treats "already has photos" as "done".

## The fix — Jesse-owned per §2

Bruce's cron prompt needs an edit. Two candidate fixes:

**Option A (small, fastest):** Replace/append the hardcoded Tier 2 list with explicit Phase B slugs, and add a line routing atlanta-drywall-1 / premier-tv-mounting-atl / bravo-plumbing-solutions / es-tree-service to the **review-retry** side of the waterfall (Phase 1b Places API reviews only, skip photos where they already exist).

**Option B (durable):** Change Bruce's Step 1 from a hardcoded list to a dynamic scan of `rebuild-queue.json` tier_3_pipeline for slugs that have `index.html` on `origin/intake/<slug>` but no `bruce-to-mini-<slug>-enriched.md` or `-blocked.md` yet. That way future R1VS finalizations don't require a cron-prompt edit.

I can draft the new prompt text if you want — just say which option. I won't touch `jobs.json` without your explicit ACK per CLAUDE.md §80-99 (cron config feels equivalent to a source-of-truth amendment, and unilateral cron edits by Mini would reintroduce the exact drift that killed the 2-pass variant earlier today).

## What's unblocked vs blocked right now

- **Unblocked (still live, healthy):** bobs-hvac, doctor-concrete-atl, rooter-pro-plumbing-drain, the 24 R1VS overnight+morning sites
- **Blocked by this:** the 15 Phase B sites sitting in intake branches with real HTML but no Bruce enrichment yet, and the 4 retry sites still waiting on reviews

No data loss — Bruce will process everything fine once the prompt is updated. Just wanted to surface this before you assume Bruce is actively working the new queue.

## /loop

Will keep heart-beating on 25-min cadence. If you take action on the cron prompt before my next fire, I'll see the enrichment messages start flowing and pick them up. If not, I'll idle until there's Mini-side work.

— Mac Mini Claude
