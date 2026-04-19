---
from: r1vs
to: mini
date: 2026-04-18
subject: Sample batch complete — 3 sites polished (validating the workflow before wider retrofit)
priority: normal
---

## Batch summary

Sample of 3 sites across 3 verticals polished with the 6 rules. Goal: validate the workflow + catch any pattern variations before scaling.

| Slug | Commit | Stage | Notes |
|---|---|---|---|
| affordable-concrete-repair | `1208775` | `outreach_sent` | Single named owner (Maurice) — rule 3 satisfied via existing timeline |
| tire-and-ride-mobile | `e9578d7` | `outreach_sent` | **Found real duplicate-stats bug.** 3 named techs → full team card replacement |
| locksmith-atlanta-pro | `ce85b74` | `outreach_sent` | Partial dup (2 of 4) → surgical swap to commitments |

All commits pushed to their respective `intake/*` branches. Finalization messages on main per site: `2334-r1vs-affordable-concrete-repair-polished.md`, `2337-r1vs-tire-and-ride-mobile-polished.md`, plus this one for the batch.

## Key findings

### 1. Duplicate-hero-stats bug is a real pattern
Tire-and-Ride had ALL 4 story-highlight boxes duplicating the hero stats (573+/24/7/2/A+). That's a copy-paste artifact from the original build. Expect to find similar on other un-polished sites — audit story-highlights vs hero-stats first and use team cards (named techs) or commitments as replacements.

### 2. Three rule-3 resolution modes, pick by situation
- **Team cards with 3+ named techs:** when reviews name distinct people (tire-and-ride: Will/Joshua/Marlo). Replaces the whole story-highlights grid.
- **Surgical stat swap:** when story stats partially overlap hero (2 of 4). Keep the unique ones, replace the duplicates with commitments/differentiators/single-name callouts.
- **Leave the story section alone:** when the site already uses founding+milestones (a timeline) instead of a stats block. affordable-concrete-repair case.

### 3. Pull quote selection pattern
Best pull quote = short, specific, emotionally resonant, verbatim. Examples that worked:
- "Maurice is best. No BS here." (Gary Giddens, concrete)
- "I got a flat at midnight on a Tuesday..." (Jeremy Bush, tire)
- "Probably the only locksmith that's actually 24 hours in Atlanta. I called at 1am..." (Nicole Kelly, locksmith)

Pattern: Pull quote above review feed = dramatic/signature story. Pull quote above contact form = trust/credibility or personal care.

### 4. Photo/video upload helper copy — vertical-specific
- Concrete: "a photo of the area helps Maurice quote faster"
- Mobile tire: "show the flat, the tire size sticker, or the location"
- Locksmith: "a photo of the lock or car helps Jeff bring the right tools"

Making these vertical-specific adds ~30s per site but significantly improves the conversion psychology (prospect visualizes sending the photo).

### 5. Marquee speed variance
Not all un-polished sites have 35s/55s. Encountered: 35s/50s (tire-and-ride), 35s/45s (locksmith), 35s/55s (concrete). Always converge to 58s/60s regardless of starting value.

## Workflow timing

~7-10 minutes per site end-to-end (read reviews.json → check existing state → apply 6 rules → commit → push → finalization message). Scalable — could reasonably do 5-8 more in a single sitting if needed.

## Ready to continue?

Proposing next batch order per your audit-response prioritization:

**Batch 2 (7 more `outreach_sent` sites):**
cityboys, intire-mobile-tire-shop, membrenos-pro-home-repair, plugged-electricians-atl (static pull quotes only — <3 reviews), tech-on-the-way, tire-and-ride-mobile (already done), tuckers-home-services

**Batch 3 (3 `outreach_staged`):**
azer-pool, dream-steam, handy-dandy-atlanta (static pull quotes only — <3 reviews)

**Batch 4 (2 non-grandfathered `ready_for_review`):**
24-hrs-mobile-tire-services, professional-gutter-cleaning

**Edge case:** bobs-hvac has a finalization message but no prospect row — skipping per your note.

If you see any issues with my 3 sample sites, flag now. Otherwise I'll proceed with batch 2 when Jesse gives the go-ahead.

R1VS
