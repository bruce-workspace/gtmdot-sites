---
from: mini
to: jesse
date: 2026-04-20
subject: Moonstone Pressure Washing redeployed — first site under new §11 Bruce-as-Collector contract
priority: normal
---

## Deployed

- **Live:** https://moonstone-pressure-washing.pages.dev
- **Claim code:** `MOON4729`
- **Commit:** `c803d8c` on `intake/moonstone-pressure-washing`
- **Supabase stage:** `ready_for_review` (unchanged — just refreshed timestamp)

## What changed in this pass

### Photo/caption match (DESIGN-HEURISTICS §2)

Every gallery slot rewired so the caption describes what's actually in the photo. Before/after:

| Slot | OLD caption | OLD photo content | NEW caption | NEW photo content |
|---|---|---|---|---|
| Hero | (n/a — truck photo) | Parked Moonstone truck + trailer on grass | (n/a — better hero) | Navy-blue cottage w/ orange door, post-wash result |
| work-1 | House Soft Wash / Exterior | Driveway before/after (wrong caption) | Roof & Exterior / Full soft-wash result | Full back-of-house after-wash, clean roof visible |
| work-2 | Driveway Wash / Concrete + Pavers | Duplicate of hero truck (wasted slot) | House Soft Wash / Siding before & after | Siding before/after composite |
| work-3 | Roof Cleaning / AMRA-Compliant | Dirty siding (not a roof) | Driveway Restoration / Concrete before & after | Driveway before/after with pressure washer visible |
| work-4 | Patio & Walkway / Restoration | Dirty soffit (not patio or walkway) | Deck Cleaning / Wood soft-wash | Wood deck with dog (real home vibe) |
| work-5 | Fence Restoration / Wood + Vinyl | Clean back patio (no fence) | Walkway / Concrete before & after | Walkway before/after, weeds to clean |
| work-6 | Full Exterior / House + Drive | Clean front walkway (not full exterior) | On the Job / Alonzo at work | Alonzo soft-washing a stone-fronted home |

### Reviews (5 fresh merged)

Places API returned 5 verbatim reviews not in the existing file:

- **Larry Cooley** (5★): "Mr. Alonzo and his team did a great job, and were very professional..."
- **Tequila Giles** (5★): "I had my house pressure washed by Mr. Alonzo. He did a fantastic job..."
- **Nick Parry** (5★): "Fantastic service! Professional, friendly, and made the siding on my house look..."
- **Ivy Nix** (5★): "Alonzo was very good at communicating and fast at giving me a quote..."
- **Melanie Gross** (5★): "We can't compliment this team enough. They were thorough with perfect attention..."

All name Alonzo — good for named-owner signal per DESIGN-HEURISTICS §3. Merged into `reviews.json`, total verbatim now 13 (was 8). Aggregate rating unchanged at 5.0.

### Services coverage

| Service | Gallery slot | Notes |
|---|---|---|
| Houses (soft wash) | work-2 | siding before/after |
| Driveways (pressure wash) | work-3 | concrete before/after |
| Decks | work-4 | wood soft-wash |
| Walkways | work-5 | walkway before/after |
| Roofs | work-1 | full exterior including roof |
| Full exterior | work-1 | same |
| On-the-job | work-6 | owner in action |
| **Fences** | **not in gallery** | no real fence photo exists; kept in service copy, omitted from gallery |

## Source attribution (what came from where)

- **Moonstone's own website** (`moonstonepressurewashing.com`): only stock GettyImages photos found. Not usable.
- **Google Places API**: returned 10 real GBP photos + 5 fresh reviews. Used 2 gbp photos (work-2 siding, work-6 worker-on-job). Used all 5 reviews.
- **Jesse's manual browse** (GBP + Yelp + Nextdoor): contributed the hero (navy house), work-1 (roof+exterior after), work-4 (deck with dog), work-5 (Yelp walkway before/after). Source-of-truth proof that these existed — Jesse found in 5 min what I couldn't reach.
- **Existing intake branch**: work-3 (driveway before/after) kept from prior enrichment.

## What's staged for overnight

- `/tmp/bruce-cron-new-prompt.txt` — new Bruce cron prompt you can paste into `~/.openclaw/cron/jobs.json` in the morning to switch Bruce to Collector-only mode
- Overnight /loop will process as many other sites as possible using what's reachable from this session
- For sites that need Yelp/Nextdoor, I'll stage `sites/<slug>/collect-request.md` files for Bruce to pick up once the new cron is live

## What I'm NOT touching

- No stage transitions past `ready_for_review`
- No outreach triggers (email, postcard)
- No Bruce cron edits (drafted the new prompt but left application to you)
- No CRM writes beyond what `process-intake.sh` does

## Eyeball asks for the morning

1. Check https://moonstone-pressure-washing.pages.dev on mobile — does the navy-blue house hero land?
2. Scroll the gallery — do all 6 captions match the photos?
3. Reviews carousel — do the 5 new ones show up?
4. Claim-bar "Claim Now" button — does it go to `gtmdot.com/checkout?code=MOON4729`?

If anything's off, flag it and I'll fix before anything else goes live.

— Mini
