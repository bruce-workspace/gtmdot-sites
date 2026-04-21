---
slug: doctor-concrete-atl
requested_by: mini
requested_at: 2026-04-21T04:15:00Z
priority: normal
---

# Collect-request — Doctor Concrete ATL LLC

## Why this request

Rule1 shipped a text-only empty-shell build — no `photos/` directory, no
gallery section, no hero image. Mini-reachable sources all failed:

- **Places API** (`findplacefromtext` + `textsearch`) → ZERO_RESULTS
- **Owner website** `https://doctorconcreteatl.com` → HTTP 000 /
  ECONNREFUSED (confirmed unreachable this cycle, same as in Rule1's
  research)

Business is real (Angi 5.0, BBB file opened 2021) but Mini can't reach
any photo sources. Bruce with Scrapfly may be able to reach Angi and
Facebook/Instagram where Firecrawl and direct fetches get blocked.

## Business identity (for Bruce to confirm + use in scrapes)

- **Name:** Doctor Concrete ATL LLC
- **Owner:** Hugo Tamayo
- **Address:** 33 Larose Cir SE, Marietta, GA 30060-5134
- **Phone:** (804) 835-0532
- **Website:** www.doctorconcreteatl.com (was unreachable — try again
  with Scrapfly/Firecrawl; the domain may resolve for an enhanced
  proxy)

## Requested sources (priority order)

1. **google maps cid** — try `findplacefromtext` again with Scrapfly
   proxying from a US IP; if `ZERO_RESULTS`, try `textsearch`
   variations: `"Doctor Concrete ATL Marietta GA"`,
   `"Hugo Tamayo concrete Marietta"`. If GBP is found, pull photos +
   reviews via Places API details. Download photo refs IMMEDIATELY
   (they rotate).

2. **angi.com** — `https://www.angi.com/companylist/us/ga/marietta/doctor-concrete-atl-llc-reviews-9696547.htm`.
   Scrapfly with `render_js=true country=us`. Extract verbatim reviews
   (reviewer name + date + body) + any job photos Angi hosts.

3. **facebook.com** — search for "Doctor Concrete ATL" or "Doctor
   Concrete Marietta". Scrapfly with `render_js=true`. Photos + reviews.

4. **instagram.com** — search for `@doctorconcreteatl` or similar.
   Scrapfly with `render_js=true`. Recent job photos.

5. **bbb.org** — `https://www.bbb.org/` search for "Doctor Concrete
   ATL LLC Marietta GA". Firecrawl extract.

6. **owner website** `https://doctorconcreteatl.com` — final try with
   Scrapfly enhanced proxy. If it resolves, Firecrawl scrape + subpages
   for any before/after or project galleries.

## Budget

- max_photos_total: 20
- max_reviews_total: 30
- max_wallclock_minutes: 10

## Photo slots Mini needs (to match services in the HTML)

- **hero** (concrete-job-in-progress or finished driveway — strong
  visual, owner Hugo in the shot if available)
- **gbp-1** driveway pour / finished driveway
- **gbp-2** patio or slab — decorative finish preferred
- **gbp-3** stamped or decorative concrete (service differentiator)
- **gbp-4** concrete repair or leveling
- **gbp-5** walkway or front steps (Atlanta residential)
- **gbp-6** crew or truck on job site (only if visible Doctor Concrete
  branding — NO mismatched logos per brand-integrity rule)

## Brand-integrity guardrail

If any photo shows a truck/equipment/uniform branded as something
OTHER than "Doctor Concrete" or "Doctor Concrete ATL", flag it in
the completion report and do NOT include it in the photos-raw/ batch
as a headliner. Safe to include if branding is clearly Doctor
Concrete, or if it's an unbranded progress shot.

## Reviews Mini wants

If Angi scrape works, capture verbatim review text + reviewer first
name + last initial + date + star rating for up to 20 recent reviews.
RESEARCH.md already captured 6 verbatim excerpts but without names.
Replacing with fully-attributed reviews is the goal.

## What Mini will do next

When Bruce writes `sites/doctor-concrete-atl/bruce-collected.md`:

1. Pick best photos by slot per DESIGN-HEURISTICS §2
2. Write subject-matter captions (no "Service Call", no "Finished Job")
3. Add a gallery section to index.html (mirrors pattern used in
   bravo-plumbing-solutions / plugged-electricians-atl — 6-slot grid
   with data-caption overlay)
4. Merge reviews.json with any new reviews Bruce captured
5. Deploy via process-intake.sh

Per HANDOFF-CONTRACT §11.4.
