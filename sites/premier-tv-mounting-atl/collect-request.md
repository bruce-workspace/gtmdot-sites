---
slug: premier-tv-mounting-atl
requested_by: mini
requested_at: 2026-04-21T08:20:00Z
priority: normal
---

# Collect-request — Premier TV Mounting Atl (Marcus)

## Why this request

Rule1 shipped a text-only build with no photos/ directory and no
image references in the HTML at all. Mini-reachable sources all
failed this cycle:

- **Places API** `findplacefromtext` for 2 query variants →
  ZERO_RESULTS
- **Owner website** `premiertvmountingatl.com` → HTTP 000 (DNS
  unresolved — was also noted offline during Rule1 research)

RESEARCH.md flagged the strong candidate sources Bruce with Scrapfly
should be able to unlock:

- Facebook (blocked on direct fetch)
- Instagram (@premiertvmountingatl)
- TikTok (Premier TV Mounting Atlanta)
- Yelp listing (misfiled under "Lugoff, South Carolina" — legacy
  artifact; still has photos)
- Square booking subdomain (may have portfolio images)

## Business identity

- **Name:** Premier TV Mounting Atl (legal: Premier Tv Mounting LLC)
- **Owner / primary tech:** Marcus (first name only confirmed)
- **Phone:** (404) 606-2066
- **Email:** Premiertvmountingatl1@gmail.com
- **Service model:** Mobile / at-customer location, no storefront
- **Market:** Atlanta, GA metro (despite Yelp mis-geo to Lugoff SC)

## Requested sources (priority order)

1. **facebook.com** — search "Premier Tv Mounting Atl" on Facebook.
   Scrapfly with `render_js=true country=us`. Pull photos + review
   snippets. Named-reviewer capture priority (reviewer names + dates
   were paraphrased by search summarizer per RESEARCH).

2. **instagram.com** — @premiertvmountingatl (or similar). Scrapfly
   `render_js=true`. Pull grid shots of TV installs — ceilings, stone
   walls, outdoor mounts, bracket-only pre-mount shots.

3. **tiktok.com** — "Premier TV Mounting Atlanta" search. Scrapfly.
   Unusual for photo pulls but TikTok profile banner + pinned post
   thumbnails may be usable.

4. **yelp.com** — `yelp.com/biz/premier-tv-mounting-atl-lugoff-3`
   (note the weird Lugoff, SC URL slug — it's still the Atlanta
   business). Scrapfly `render_js=true country=us`.

5. **squarebooking** — whatever subdomain Rule1 noted (premier-tv-
   mounting-llc.square.site or similar). Firecrawl scrape for
   portfolio images.

6. **google maps cid** — retry `findplacefromtext` + `textsearch`
   with Scrapfly US proxy. Mobile-only service without a storefront
   sometimes doesn't index; low priority retry.

## Budget

- max_photos_total: 15
- max_reviews_total: 20
- max_wallclock_minutes: 10

## Photo slots Mini needs

HTML is pure text-pattern-background currently. Mini will add a
hero + 6-slot gallery once Bruce delivers. Target:

- **hero** — Marcus on a job, or a beautifully-mounted TV above a
  stone fireplace / brick wall (the "clean install" money shot)
- **gbp-1** — above-fireplace TV mount with wires concealed
- **gbp-2** — articulating wall mount mid-install
- **gbp-3** — stone or brick-wall anchor install (harder-than-
  drywall differentiator)
- **gbp-4** — outdoor / patio TV install (weatherproof bracket)
- **gbp-5** — Marcus with tools/stud-finder on a job
- **gbp-6** — before/after (bare wall → mounted TV + wire concealment)

## Brand-integrity guardrail

No trucks likely since mobile-only service. If any uniform/shirt
shows a non-"Premier" brand, flag and exclude.

## Reviews status

reviews.json is blank. RESEARCH.md documented that review content
was "paraphrased by search summarizer, NOT verbatim." Anything Bruce
pulls with reviewer name + date + verbatim body is net gain.

## What Mini will do next cycle

1. Add hero CSS rule pointing to `photos/hero.jpg` with standard
   vertical filter
2. Add gallery section to HTML (mirror pattern used on deployed
   handyman/fixture sites like jack-glass-electric or atl-mobile-
   mechanics)
3. Pick best photo per slot from Bruce's batch
4. Write subject-matter captions
5. Merge any captured reviews into reviews.json
6. Deploy via process-intake.sh

Per HANDOFF-CONTRACT §11.4.
