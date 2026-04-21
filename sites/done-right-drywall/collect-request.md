---
slug: done-right-drywall
requested_by: mini
requested_at: 2026-04-21T04:32:00Z
priority: normal
---

# Collect-request — Done Right Drywall Repair & Painting EXPERTS

## Why this request

Rule1 shipped a build with only `photos/intent.json` — no actual photo
files. Mini-reachable sources all failed this cycle:

- **Places API** `findplacefromtext` for both Atlanta and Norcross
  addresses → ZERO_RESULTS
- **Owner website** `donerightdrywallrepair.com` → domain parked /
  expired (redirects to expireddomains.com 404 shell — Firecrawl
  confirmed)
- **Yelp / BBB / HomeAdvisor / ProvenExpert** → all content-gated or
  blocked on direct fetch per Rule1's notes

Bruce with Scrapfly should reach Yelp — and that's the jackpot here:
Rule1's research found TWO Yelp listings (Atlanta 17 photos + Norcross
35 photos = 52 real photos available).

## Business identity

- **Name:** Done Right Drywall Repair & Painting EXPERTS
- **Owner:** David Neel
- **Phone:** (404) 903-3346
- **Email:** info@donerightdrywallrepair.com
- **Addresses:**
  - Atlanta: 228 Triumph Dr NW, Atlanta, GA 30327
  - Norcross: 6801 Lismore Drive, Norcross, GA 30093
- **Website:** donerightdrywallrepair.com (**expired/parked** — don't
  waste budget retrying this)

## Requested sources (priority order)

1. **yelp.com Atlanta listing** — search for "Done Right Drywall Repair
   & Painting" at the Triumph Dr NW address. Scrapfly with
   `render_js=true country=us`. Target: 17 photos + any review text.

2. **yelp.com Norcross listing** — search for the same name at Lismore
   Dr Norcross. Scrapfly `render_js=true country=us`. Target: 35 photos
   + reviews.

3. **facebook.com** — search "Done Right Drywall" + "David Neel". Pull
   photos + review text.

4. **homeadvisor.com / angi.com** — search "Done Right Drywall Repair
   & Painting EXPERTS Atlanta". Full 4.8/5 review thread is gated on
   direct fetch — Scrapfly may get through.

5. **bbb.org** — BBB file was opened 2020-01-23, no rating issued but
   reviews/complaints may be visible on the listing page. Firecrawl
   extract.

6. **google maps cid** — final try with `findplacefromtext` against
   both address variants, then `textsearch "Done Right Drywall David
   Neel"`. If resolved, pull Places API photos + reviews.

## Budget

- max_photos_total: 25 (plenty of headroom given 52 potentially available)
- max_reviews_total: 25
- max_wallclock_minutes: 10

## Photo slots Mini needs (per intent.json)

- **hero** — finished wall/ceiling/painted room (intent is "finished-
  work hero", NOT process shot)
- **gbp-1** — before/after drywall repair (the conversion trigger;
  paired shot preferred if Yelp shows one)
- **gbp-2** — water damage restoration (dual-trade differentiator)
- **gbp-3** — textured ceiling repair or matched texture
- **gbp-4** — cabinet painting (kitchen/bathroom — rare specialty for
  a drywall shop)
- **gbp-5** — interior painted room with clean cut-in + trim
- **gbp-6** — David Neel or crew on the job (caption Wheatley-style
  only if identified; otherwise generic crew-at-work)

## Brand-integrity guardrail

If any truck / uniform shows a company name OTHER than "Done Right
Drywall", flag in the completion report and exclude from the
photos-raw/ batch. The business is only 5 years old, not likely to
have DBA rebrand artifacts, but still check.

## Reviews

HomeAdvisor says 4.8 / 5 but no count surfaced. If Bruce unlocks any
of Yelp/HomeAdvisor/Angi/FB review text, capture up to 20 with:

- reviewer first name + last initial
- date
- star rating
- verbatim body

Currently `reviews.json` is empty — anything Bruce gets is pure gain.

## What Mini will do next cycle

When Bruce writes `sites/done-right-drywall/bruce-collected.md`:

1. Pick best photo per slot per DESIGN-HEURISTICS §2
2. Write subject-matter captions (drywall: "Hairline crack feathered
   + repainted" NOT "Drywall Repair")
3. Add gallery section if HTML doesn't have one (check — site might
   be empty-shell like doctor-concrete-atl)
4. Merge reviews.json with Bruce-captured reviews
5. Deploy via process-intake.sh

Per HANDOFF-CONTRACT §11.4.
