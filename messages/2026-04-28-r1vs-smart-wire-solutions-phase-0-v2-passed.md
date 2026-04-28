---
from: r1vs (MacBook Claude Code)
to: bruce, mini, jesse
date: 2026-04-28
subject: SmartWire Solutions — Phase 0 v2 PASSED (supersedes prior DQ at commit e49aa7a)
priority: normal
slug: smart-wire-solutions
phase: 0 — legitimacy-screen
result: passed=true
gate: HOLDING before Phase 1 per Jesse's instruction
refs:
 - sites/smart-wire-solutions/legitimacy-check.json (overwritten with passed=true)
 - sites/smart-wire-solutions/gbp-data-from-kp.json (manual verification input)
 - sites/smart-wire-solutions/phase-0-evidence-google-kp.png (screenshot evidence)
 - 2026-04-27 e49aa7a → messages/2026-04-28-r1vs-smart-wire-solutions-dq-recommended.md (PRIOR DQ — INVALIDATED)
 - https://share.google/odJwB0uvcD08lbYxb (Jesse-supplied GBP share URL)
 - kgmid /g/11j61b1qy5
---

## TL;DR

Re-ran Phase 0 with the GBP share URL Jesse supplied. **Passed.** All six
legitimacy rules cleared. The prior DQ recommendation (commit e49aa7a) is
invalidated — Phase 0 v1 used Places API only, which can't surface this
particular GBP listing because it's a service-area-business with `ftid=0x0`,
a known blind spot in `findplacefromtext` + `textsearch`. Once I rendered the
share URL in a JS-aware browser (chrome-devtools MCP), the actual Google
Knowledge Panel showed the full listing.

**Holding before Phase 1 per Jesse's gate.** Awaiting either explicit
"proceed to Phase 1" approval or a confirmed Paperclip-wired approval gate.

## What changed between v1 and v2

| Surface | Phase 0 v1 (DQ'd) | Phase 0 v2 (passed) |
|---|---|---|
| Identity input | name + phone + city | GBP share URL → kgmid → rendered Knowledge Panel |
| Lookup method | Places API `findplacefromtext` + `textsearch` (13 query variants) | Chrome DevTools render of `https://share.google/odJwB0uvcD08lbYxb` |
| GBP found | NO (ZERO_RESULTS on every query) | YES (KP rendered with rating, reviews, address, hours) |
| Rating | unknown | 5.0 ★ |
| Total reviews | 0 (unknown) | 17 |
| Address | "Atlanta, GA" (city-only, supplied) | 730 Peachtree St NE, Ste 570, Atlanta, GA 30308 (cross-confirmed via Yelp listing on same KP) |
| GBP match | false | true |
| Result | DQ recommended | passed |

## Why the Places API missed it (root cause)

The cid extracted from the KP's Maps link is `0x0:0x41524a050c3d29f4`. The
leading `0x0` ftid (place feature type ID hash) is the signature of a
**service-area-business GBP** — a listing without a verified physical
storefront geocode. SAB listings frequently don't surface in standard Places
API geographic queries because there's no geocoded centroid for the API to
match against. They DO surface in Knowledge Graph + direct Maps `data=` URL
lookups, which is what the share URL resolved to.

**This is a known Phase 0 blind spot.** R1VS-side recommendation: extend
`scripts/legitimacy-screen.py` with a `--share-url` input mode (resolve →
KP scrape → JSON build) so future Paperclip-orchestrated runs don't hit the
same false negative. Out-of-scope for this pilot; flagging as a follow-up.

## What I extracted from the rendered KP

Saved verbatim to `sites/smart-wire-solutions/gbp-data-from-kp.json`:

```json
{
  "name": "SmartWire Solutions",
  "address": "730 Peachtree St NE, Ste 570, Atlanta, GA 30308",
  "rating": 5.0,
  "total_reviews": 17,
  "gbp_match": true,
  "place_id": "0x0:0x41524a050c3d29f4",
  "kgmid": "/g/11j61b1qy5",
  "phone_kp": "(404) 635-6301",
  "phone_jesse_supplied": "(404) 382-9847",
  "hours": "Open 24 hours",
  "owner": "Terry Henry",
  "owner_role": "Master Electrician, US Air Force veteran, owner-operator",
  "secondary_contact": "Maria Henry, VP (BBB)",
  "vertical": "electrical",
  "cross_source_signals": {
    "facebook": "facebook.com/SmartWire365 (480+ followers)",
    "instagram": "instagram.com/smartwire365 (230+ followers)",
    "youtube": "@smartwiresolutions6624",
    "yelp": "yelp.com/biz/smartwire-solutions-atlanta",
    "bbb": "bbb.org/.../smartwire-solutions-llc-0443-28141526",
    "linkedin_owner": "linkedin.com/in/terry-henry-b761bb25"
  },
  "website": "https://smartwire365.com (parked per Jesse, but referenced across all socials → was live, currently down)"
}
```

Screenshot evidence: `sites/smart-wire-solutions/phase-0-evidence-google-kp.png`

## Findings to feed forward to Phase 1 / Bruce

When Phase 1 (or Paperclip) approves continuation, R1VS will inherit:

1. **Two phone numbers exist.** (404) 635-6301 on Google KP. (404) 382-9847
   on Yelp, Facebook, the business's own copy, and Jesse's handoff. Both
   are real; Phase 1 / Paperclip should decide which is the primary "call
   us" number for the site (suggestion: 404-382-9847 since that's what the
   business itself promotes in its own copy).

2. **Website is parked.** `smartwire365.com` is referenced everywhere as
   the canonical URL, but Jesse confirmed it's down. R1VS won't be able to
   pull RESEARCH.md material from it; will need to lean on Facebook,
   Instagram, BBB, LinkedIn, and the KP description copy.

3. **20+ year tenure claim** in the KP description: *"top rated electricians
   in Atlanta that have been providing quality electrical services to the
   Metro Area for over 20yrs."* This is a strong proof point for the hero
   kicker / trust strip. Year-founded estimate: ~2003-2006.

4. **Owner story is a real differentiator.** Terry Henry — Master Electrician,
   US Air Force veteran, owner-operator. Maria Henry serves as VP. Family-run.
   That's exactly the brand-voice cluster the multi-page scaffold is tuned for.

5. **Service area is multi-zone.** KP description says "Metro Area." Yelp
   address is Midtown (Peachtree St NE). Owner LinkedIn says Atlanta-based.
   Instagram bio says "South Fulton Electrician." Service area likely covers
   Atlanta proper + South Fulton + intown neighborhoods. Phase 1 research
   should disambiguate.

6. **5.0 ★ rating is unusually clean.** 17 reviews at exactly 5.0 means no
   negative reviews. That's either authentic (small electrician, hand-curated
   client base, AF-veteran reputation effect) or worth a Phase 0 farm-pattern
   sanity check that I couldn't run because the KP doesn't expose individual
   review dates without scrolling/expansion. Not a DQ trigger today; flagging
   for Phase 1 / Bruce to corroborate when scraping reviews.

## What was NOT created

Holding the line per Jesse's gate:

- ❌ No `RESEARCH.md`
- ❌ No `BRAND.md` / brand voice notes
- ❌ No `business-data.json`
- ❌ No `icon-intent.json`
- ❌ No rendered HTML
- ❌ No `collect-request.md` (Bruce's budget not engaged)
- ❌ No CRM mutation
- ❌ No outreach
- ❌ No deploy

## What WAS created (Phase 0 v2 artifacts)

- `sites/smart-wire-solutions/legitimacy-check.json` — overwrites the prior
  failed Phase 0 v1; now contains `passed: true`, all 6 rules clean
- `sites/smart-wire-solutions/gbp-data-from-kp.json` — the manual-verification
  input fed to `legitimacy-screen.py --gbp-json` (full audit trail)
- `sites/smart-wire-solutions/phase-0-evidence-google-kp.png` — screenshot
  of the rendered Knowledge Panel showing rating + reviews + hours + profile
  links. Preserved as evidence in case rendered KP content changes later.

## Decision points for Bruce + Jesse

1. **Approve Phase 1.** R1VS proceeds with WebSearch/WebFetch research
   pulling from Facebook, Instagram, LinkedIn, KP description, BBB profile,
   and the cached version of smartwire365.com (if Wayback has snapshots).
   Writes `RESEARCH.md` + brand voice notes. Pauses again at end of Phase 1
   if you want a checkpoint, or continues into Phase 2-3.

2. **Hold and have Paperclip wire the approval gate.** I stay parked at
   Phase 0 v2 passed. Paperclip's gate becomes the trigger. Nothing
   irreversible; the legitimacy-check.json is committed but no business
   work proceeds.

3. **Address ambiguity check first.** If you want to confirm the 730 Peachtree
   St NE Ste 570 address is the actual service base (vs. a virtual / coworking
   address — Peachtree St in Midtown is a busy commercial strip with several
   shared-office buildings at #730), I can do a Maps proximity probe via
   Places API now that I have a real coordinate to anchor on.

## Recommended next action

R1VS recommends **Option 1 (approve Phase 1)** with one optional pre-step:
have Bruce or you confirm "proceed" via this message thread before I write
the first byte of `RESEARCH.md`. That keeps the human-in-the-loop pattern
Bruce specified for the Paperclip pilot intact while not stalling on a
Paperclip wiring exercise that's still in flight.

— R1VS
