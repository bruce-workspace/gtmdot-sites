---
from: r1vs (MacBook Claude Code)
to: bruce, mini, jesse
date: 2026-04-28
subject: SmartWire Solutions — Phase 0 DQ recommended (no GBP match found)
priority: normal
slug: smart-wire-solutions
phase: 0 — legitimacy-screen
result: passed=false
refs:
 - sites/smart-wire-solutions/legitimacy-check.json (artifact)
 - paperclip-sandbox/artifacts/smartwire-02-research.md (Paperclip context, not pulled)
 - paperclip-sandbox/artifacts/smartwire-03-data-photos.md (Paperclip context, not pulled)
 - HANDOFF-CONTRACT.md §11.1 / scripts/legitimacy-screen.py
---

## TL;DR

Phase 0 ran for SmartWire Solutions. **Three DQ rules triggered**, all rooted
in the same finding: **no Google Business Profile listing can be located for
this business** by any of the variants I tried. Per the approved R1VS arc, I
am stopping before Phase 1 and filing this DQ recommendation. **No site has
been built. No CRM stage has been moved. No external action taken.**

This is a recommendation, not a unilateral DQ. If Bruce or Jesse can supply
a street address (which would let me re-query GBP within proximity) or a
business-name variant we haven't tried, R1VS can re-run Phase 0 cleanly.

## Inputs

From Jesse's handoff:

- **Business name:** SmartWire Solutions LLC / SmartWire Solutions
- **Vertical:** Electrician / electrical contractor
- **Website:** https://smartwire365.com — flagged as parked/broken
- **Phone:** (404) 382-9847
- **Service area:** Atlanta / Midtown Atlanta / South Fulton / Metro Atlanta
- **Owner:** Terry Henry
- **Secondary contact (BBB):** Maria Henry, VP
- **Street address:** not confirmed (do not invent)
- **GBP place_id:** not confirmed

## Phase 0 rules

`scripts/legitimacy-screen.py` applies these auto-DQ rules:

| Rule | Threshold | Result |
|---|---|---|
| 1. rating | ≥ 4.5 | **FAIL** — no rating in data (no GBP) |
| 2. review count | ≥ 10 | **FAIL** — `total_reviews 0 < 10` (insufficient signal) |
| 3. farm pattern | < 50% in any 30-day window | n/a — no reviews |
| 4. GBP at claimed address | true | **FAIL** — no candidate returned by Places API |
| 5. dormancy | latest review ≤ 24 mo | n/a — no reviews |
| 6. vertical blocklist | not in `{lead-gen-broker, franchise-unverified, referral-funnel}` | PASS — `electrical` not blocklisted |

## What I tried

Read-only Google Places API `findplacefromtext` lookups (the only external
action I'm authorized to take in Phase 0 per Jesse's handoff). All eleven
queries returned `ZERO_RESULTS`:

| Query | Result |
|---|---|
| `SmartWire Solutions LLC Atlanta, GA` (script default) | ZERO_RESULTS |
| `SmartWire Solutions Atlanta GA` | ZERO_RESULTS |
| `+14043829847` (phone E.164) | ZERO_RESULTS |
| `(404) 382-9847` (phone formatted) | ZERO_RESULTS |
| `SmartWire Solutions LLC (404) 382-9847` (name + phone) | ZERO_RESULTS |
| `SmartWire Solutions Midtown Atlanta` | ZERO_RESULTS |
| `SmartWire Solutions South Fulton GA` | ZERO_RESULTS |
| `smartwire365.com` (domain query) | ZERO_RESULTS |
| `SmartWire 365 Atlanta` (domain-derived name) | ZERO_RESULTS |
| `Smart Wire LLC Atlanta` (deconcatenated name) | ZERO_RESULTS |
| `Henry Electric Atlanta GA` (owner-surname pattern) | ZERO_RESULTS |
| `Terry Henry Electric Atlanta` (owner-name pattern) | ZERO_RESULTS |
| `Terry Henry electrician Atlanta` (owner-trade pattern) | OK — 1 candidate, but it's `Henry County Electric Services Company LLC`, a county-named business in Henry County GA, NOT Terry Henry's SmartWire Solutions. Coincidental "Henry" overlap. Not a real match. |

## Contributing context (from Jesse + the Paperclip artifacts referenced)

- **Website is parked/broken.** `smartwire365.com` doesn't serve a real site
  per Jesse's note. That's consistent with a business that either (a) shut
  down operations recently, (b) operates entirely off-platform (BBB +
  word-of-mouth + phone), or (c) rebranded under a different name we don't
  have. Phase 1 research could disambiguate, but the GBP signal is the
  Phase 0 gate, and it's missing.
- **BBB listing exists.** Per Jesse, the BBB has a record with Maria Henry
  listed as VP. BBB is a real signal that the business exists somewhere —
  but BBB is not part of the Phase 0 rule set. The GBP gate is what governs
  whether we can build a SEO/local-trade site for them. A business with no
  GBP can't realistically be promoted by the kind of site GTMDot ships.

## Recommendation

**Stage:** R1VS recommends **stop**. Do not proceed to Phase 1 research, do
not write `RESEARCH.md`, do not allocate Bruce's collection budget, do not
build a site. The prospect lacks the public proof footprint (GBP) that the
multi-page scaffold's hero/trust strip/reviews-bar are designed to surface.
Building a site for a business with no GBP and a parked website would
produce a site whose own gates can't validate it (`reviews.json captured: 0`
under Path C empty-state, no real photos in `photos-raw/`, no ratings to
populate the trust strip).

**For Bruce + Jesse to consider before final DQ:**

1. **Is the business name correct?** If SmartWire Solutions actually operates
   on GBP under a different listing name — e.g., "Terry Henry Electric"
   without "SmartWire" branding, or a different LLC name — supply that and
   I'll re-run Phase 0.
2. **Is there a confirmed street address?** A street address would let the
   Places API search by proximity rather than name match. The free-text
   query may have failed because the business uses a different display name
   on GBP than its legal name.
3. **Is the business still operating?** A parked website plus no GBP plus a
   BBB listing is consistent with a business that's been wound down. If
   that's the case, the right CRM action is `dead`, not `disqualified`.

If none of those produce a clean GBP signal, the Phase 0 finding is final
and the recommendation is to mark this prospect `dead` (or `disqualified`,
per the killed-stages migration) in the CRM.

## What was created

- `sites/smart-wire-solutions/legitimacy-check.json` — Phase 0 artifact
  containing the full rule application, snapshot data, and timestamp. Will
  be committed alongside this message.

## What was NOT created

- No `RESEARCH.md`, no `BRAND.md`, no `business-data.json`, no `icon-intent.json`
- No `index.html` or other rendered site
- No `collect-request.md` (Bruce's budget not engaged)
- No CRM mutation
- No outreach
- No deploy

## Next-step decision tree

| If… | Then… |
|---|---|
| Bruce or Jesse confirm a different business name / address | I re-run Phase 0 with the new inputs |
| Confirmation that SmartWire really has no GBP and is operating off-platform | Mark CRM `dead` or `disqualified`; no GTMDot fit |
| Paperclip is the gate-arbiter | Surface this DQ recommendation as a Paperclip-checkpoint blocker, await human approval to either retry or close |
| No further info comes | Default action is **close** (no GTMDot fit), not **build anyway** |

— R1VS
