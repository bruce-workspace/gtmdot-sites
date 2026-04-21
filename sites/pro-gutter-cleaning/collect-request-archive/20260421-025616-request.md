---
slug: pro-gutter-cleaning
requested_by: mini
requested_at: 2026-04-21T08:45:00Z
priority: normal
---

# Collect-request — Pro Gutter Cleaning and Repair LLC (Matt)

## Why this request

Rule1 shipped a build with no photos/ directory and an **Unsplash stock
URL hardcoded into the hero-bg CSS** (`.hero-bg { background:
url('https://images.unsplash.com/photo-1558618666-fcd25c85cd64...') }`).
Same ship-blocker pattern I caught on forest-park-collision last cycle.

Mini-reachable sources all failed:
- **Places API** findplacefromtext for "Pro Gutter Cleaning Carrollton
  GA" → ZERO_RESULTS
- **Owner website** `proguttercleaningnow.com` → resolved, but it's a
  thin GoDaddy template with one generic placeholder image from
  GoDaddy's own stock library (`img1.wsimg.com/isteam/stock/DjDmbPd`).
  No portfolio photos.

Yelp has 38 photos across two listings per RESEARCH + HomeAdvisor
has "Elite Service" + "Top Rated Pro" badges with reviews. Bruce
Scrapfly is needed.

## Business identity

- **Name:** Pro Gutter Cleaning and Repair LLC
- **Sister entity:** Pro Roof Gutters and Siding LLC (same phone +
  address — related/parent per Carroll County Chamber)
- **Owner:** Matt (last name unconfirmed; named in multiple reviews as
  "Matt the owner came out and measured my home")
- **Team:** Nick, Johnny (tech names surfaced in reviews)
- **Phone:** (404) 606-2950
- **Address:** 3394 Carrollton Villa Rica Hwy, Carrollton, GA 30116
- **Founded:** 25+ years in business per owner site

## Requested sources (priority order)

1. **yelp.com #1** — search for "Pro Gutter Cleaning & Repair
   Carrollton" — the main listing has **10 photos + 10 reviews**.
   Scrapfly `render_js=true country=us`.

2. **yelp.com #2** — the sister listing "Pro Gutter Cleaning"
   Carrollton has **28 photos**. Also scrapfly.

3. **instagram.com** — @proguttercleaningrepair (URL confirmed on
   owner website footer). Scrapfly `render_js=true`.

4. **facebook.com** — page ID 101996181608668 (confirmed on owner
   site). Scrapfly.

5. **homeadvisor.com** — "Pro Gutter Roof Siding" Carrollton listing
   (sister entity, same phone). Elite Service + Top Rated Pro badges.
   26 reviews noted in RESEARCH. Firecrawl extract.

6. **birdeye** — retry with Scrapfly for the named Nick review and
   any others RESEARCH mentioned.

## Budget

- max_photos_total: 20 (plenty of headroom given 38 potentially available)
- max_reviews_total: 30
- max_wallclock_minutes: 10

## Photo slots Mini needs

HTML currently has a hero with a stock CSS background and no gallery
section. Mini will expand once Bruce delivers:

- **hero** — clean finished gutter install, or Matt/crew on a job
- **gbp-1** gutter-cleaning-in-progress (leaves being cleared,
  blower on roof)
- **gbp-2** seamless gutter install (fresh aluminum, freshly
  finished)
- **gbp-3** gutter repair (downspout re-anchor, soffit fix)
- **gbp-4** roof work (badges mention "Pro Gutter Roof Siding")
- **gbp-5** before/after (clogged gutter → clear)
- **gbp-6** truck or crew on a job (branded)

Also need to fix the hero-bg CSS: swap Unsplash URL to
`url('photos/hero.jpg')` once hero.jpg is placed.

## Brand-integrity guardrail

Watch for "Pro Roof Gutters and Siding LLC" branded trucks/uniforms
(sister entity, same owner). That branding is fine to include given
the documented parent-entity relationship — but call it out in the
bruce-collected.md report so Mini can decide whether to show or
crop.

## Reviews status

reviews.json is blank. Bruce pulls with reviewer name + date +
rating + verbatim body is pure gain.

## What Mini will do next cycle

1. Swap hero-bg CSS from Unsplash URL to photos/hero.jpg (§2
   template-bug-b fix)
2. Add gallery section to HTML
3. Pick best photo per slot from Bruce's batch
4. Write subject-matter captions
5. Merge reviews into reviews.json
6. Deploy via process-intake.sh

Per HANDOFF-CONTRACT §11.4.
