---
slug: handy-dandy-atlanta
requested_by: mini
requested_at: 2026-04-21T06:10:00Z
priority: normal
---

# Collect-request — Handy Dandy Atlanta LLC (Ruslan)

## Why this request

Rule1 shipped a text-only empty-shell build — no RESEARCH.md, no
photos/ directory, no hero image, no gallery section, no image refs
anywhere in HTML. Mini-reachable sources failed:

- **Places API** `findplacefromtext` with multiple queries
  (business name, phone, "handyman Ruslan") → ZERO_RESULTS on all
- No owner website referenced in the HTML (hero has no image URL)
- Reviews.json is empty

Bruce with Scrapfly is the right tool here. Yelp/Facebook/Nextdoor
frequently host handyman portfolio photos that Mini can't reach.

## Business identity (from intake HTML schema.org block)

- **Name:** Handy Dandy Atlanta LLC
- **Owner:** Ruslan (first name only surfaced — last name not public)
- **Phone:** (404) 919-3833
- **City:** Atlanta, GA
- **Founded:** 2021
- **Service area:** Atlanta, Ellenwood, Stockbridge, McDonough,
  Forest Park, Jonesboro
- **Trade:** Handyman (one-man-with-a-truck positioning — drywall,
  plumbing, electrical, lighting, decks, mailboxes, repairs)

## Requested sources (priority order)

1. **google maps cid** — `findplacefromtext` ZERO_RESULTS, but try
   `textsearch` with `"Handy Dandy Atlanta"`, `"Handy Dandy handyman
   Atlanta"`, and by phone `(404) 919-3833`. If resolved, pull photos
   + reviews. Download refs immediately.

2. **facebook.com** — search "Handy Dandy Atlanta" + "Ruslan
   handyman Atlanta". Pull photos + reviews.

3. **yelp.com** — search "Handy Dandy Atlanta" and "Ruslan handyman
   Atlanta". Scrapfly with `render_js=true country=us`.

4. **nextdoor.com** — search "Handy Dandy" in Atlanta neighborhoods.
   Handymen frequently surface on Nextdoor with word-of-mouth photo
   recommendations.

5. **thumbtack.com / homeadvisor.com / angi.com** — search for
   Ruslan handyman in Atlanta metro.

6. **instagram.com** — search `@handydandyatlanta` or similar.

## Budget

- max_photos_total: 15
- max_reviews_total: 20
- max_wallclock_minutes: 10

## Photo slots Mini needs

HTML is a pure text-build, no gallery exists yet. Mini will add one on
next cycle. Target slots once photos land:

- **hero** — Ruslan on a job (owner-in-action) or clean finished work
- **gbp-1** drywall repair (before/after preferred)
- **gbp-2** plumbing fixture install (faucet, toilet, valve)
- **gbp-3** electrical install (ceiling fan, outlet, light fixture)
- **gbp-4** deck or carpentry repair (wood rot, board replacement)
- **gbp-5** mailbox or exterior repair
- **gbp-6** Ruslan-with-tools / truck shot (only if branded as "Handy
  Dandy" — otherwise skip)

## Brand-integrity guardrail

If any truck / uniform shows a company name OTHER than "Handy Dandy"
or "Handy Dandy Atlanta", flag in the completion report and exclude.
Owner founded 2021 so DBA rebrand risk is low, but still verify.

## Reviews Mini wants

reviews.json is empty. Any verified review text Bruce can capture
(name + date + star rating + body) is net gain. Target 3+ for the
site to pass design-heuristics §5 review-section requirements.

## What Mini will do next cycle

When Bruce writes `sites/handy-dandy-atlanta/bruce-collected.md`:

1. Add a gallery section to index.html (mirror the pattern used in
   other deployed handyman sites — e.g., atlanta-pro-repairs)
2. Pick best photo per slot per DESIGN-HEURISTICS §2
3. Write subject-matter captions ("Ceiling fan install with cable
   routing", not "Service Visit")
4. Add a hero-bg CSS rule pointing to photos/hero.jpg with the
   standard vertical filter
5. Merge any captured reviews into reviews.json
6. Deploy via process-intake.sh

Per HANDOFF-CONTRACT §11.4.
