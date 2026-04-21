---
slug: atl-mobile-mechanics
requested_at: 2026-04-20T20:10:00-07:00
requested_by: mini
---

# Collect Request — ATL Mobile Mechanics LLC

## Business context

- Name: ATL Mobile Mechanics, LLC
- Trade: Mobile auto repair (family-owned, American-owned, 24/7)
- Owner: Joseph
- Address: 8816 Countryside Way, Douglasville, GA 30134
- Phone: (470) 809-3146
- Website: atlmobilemechanics.com (GoDaddy one-pager, no useful photos — GettyImages stock only)
- **Key differentiator:** specialty vehicles (diesel, commercial, fire truck, emergency vehicle, ATV, motorcycle, marine engines, lawn equipment)

## Current state — NO photos exist on intake branch

- `photos/intent.json` present (R1VS wrote)
- `photos/hero.jpg` through `photos/gbp-6.jpg` referenced in HTML but **do not exist as files**
- Site cannot deploy without photos — every gallery slot + hero would 404

## Why Mini is handing to Bruce

- Google Places API returns ZERO_RESULTS for the business name + address (likely unclaimed GBP)
- Owner website is a basic GoDaddy template with only stock imagery
- Yelp listing exists with **13 photos per intent.json notes** — this is the primary target
- Yelp is anti-bot; Mini's basic scrape can't reach it; Bruce's Scrapfly `render_js=true country=us` can

## Requested sources (priority order)

1. **yelp.com** — search "ATL Mobile Mechanics Douglasville GA" or phone (470) 809-3146. 13 photos expected per intent.json notes. **Primary target.**
2. **facebook.com** — search "ATL Mobile Mechanics" + Douglasville. Could have owner/team photos.
3. **nextdoor.com** — business pages, may have customer-shared photos
4. **Any Google Maps CID lookup** — try `https://www.google.com/maps/search/ATL+Mobile+Mechanics+Douglasville+GA` via Scrapfly

## What to collect per source (prioritize photos matching intent.json)

Per the intent.json, Mini needs photos matching these 6 slots:
- **hero**: technician in action (Joseph if visible), mobile service setup, customer driveway
- **gbp-1**: specialty vehicle — diesel truck / commercial vehicle
- **gbp-2**: specialty vehicle — fire truck / emergency vehicle (highest-tier differentiator)
- **gbp-3**: specialty vehicle — motorcycle / ATV / marine engine
- **gbp-4**: mobile service setup — tech in customer driveway with equipment
- **gbp-5**: 24/7 context — nighttime/evening shot if available
- **gbp-6**: completed repair / before-after

Any variety of the above is fine. If Bruce finds 5+ good photos across these categories, that's enough to deploy.

Also collect reviews if available from Yelp / Nextdoor — ATL Mobile Mechanics has `captured: 0` in reviews.json per the RESEARCH file. Any real reviews are a win.

## Budget

- Max 15 photos total across all sources
- Max 20 reviews total
- Max 10 minutes wall-clock

## Skip if blocked

If any source returns captcha / login-wall / rate-limit / 5xx: mark failed in `bruce-collected.md` with reason code, move to next. Do not bypass.

## Handoff back to Mini

When done, Mini will:
1. Review Bruce's `photos-raw/` inventory against `intent.json` slot targets
2. Pick best photos per slot (priority to specialty vehicles per intent notes)
3. Write subject-matter captions describing what's actually in each photo
4. If Bruce found <4 real photos, fall back to Recraft (last resort per §11) using the `recraft_prompt_if_needed` in intent.json
5. Merge any new reviews into `reviews.json`
6. Deploy to Cloudflare Pages, update Supabase to ready_for_review

Site is currently **not deployable** — either Bruce delivers real photos or Mini uses Recraft fallback.
