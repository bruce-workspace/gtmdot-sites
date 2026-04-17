# Sandy Springs Plumbing, Heating, and Air Conditioning — Research

## Identity decision (Jesse 2026-04-17)

Two overlapping listings surfaced online. Jesse made the call to **consolidate both as a single business entity under Jack Sr.'s operation**:

- **Authoritative identity:** Sandy Springs Plumbing, Heating, and Air Conditioning — Jack Sr. at 165 Hilderbrand Dr
- **Rating to use:** 4.9 / 25 Google reviews (from the 56 Perimeter Center GBP listing, treated as the authoritative service rating)
- **Excluded from site copy:** the Yelp 1.0 / 2 rating (stale, unrepresentative, do not surface)
- **Tenure anchor:** 1968 founding → 58+ years family-run → eligible for timeline section

This is a volume play. Identity consolidation is imperfect but intentional; the 58-year family story is the strongest hook.

## Basic Info

- **Name:** Sandy Springs Plumbing, Heating, and Air Conditioning
- **Owner:** Jack Sr. (last name unknown — last initial "S." shown on Yelp "Business Owner" profile)
- **Address:** 165 Hilderbrand Dr, Atlanta, GA 30328 (Sandy Springs zip)
- **Phone:** (770) 896-9852
- **Founded:** 1968 (58+ years in business)
- **Service area:** Sandy Springs + metro Atlanta (per GBP "Serves Sandy Springs and nearby areas" + Yelp map showing Atlanta metro ring)

## Rating & Reviews

- **Google:** 4.9 ★ / 25 reviews — review distribution: overwhelming majority 5-star, small 4-star band, minimal 3/2/1
- **Verbatim captured:** 0 (GBP screenshot shows summary only; Reviews tab not expanded)
- **Action needed:** Jesse or Jack to capture 3-8 verbatim review texts from the GBP Reviews tab. Until then, `reviews.json` flags `owner_input_required_before_publish`.

## Hours

- **Google listing:** Open 24 hours
- **Yelp listing:** varies by day (Mon 8-4, Tue 8-3, Wed 8-5, Thu 8:30-3, Fri 7-5, Sat 6-2, Sun 1-4:30)

Using Google's 24-hour framing for emergency-service positioning. Note in FAQ that after-hours may be triage/call-back rather than live.

## Services (consolidated from both listings)

From Google Services list:
- Drain cleaning
- Faucet installation
- Faucet repair
- Garbage disposal installation
- Garbage disposal repair
- + more

From Yelp "Services Offered" (Verified by Business):
- Bathtub installation & repair
- Drain installation & repair
- Faucet installation & repair
- Garbage disposal repair
- Gas line installation
- + 18 more (Yelp hides them behind "See 18 More")

From Yelp "About the Business" copy (Jack Sr.):
> "Full Service Plumbing Heating Air Conditioning Sewer drain cleaning camera Locate Faucet Replace Toilet Expert"

**Service list to feature:**
1. Emergency plumbing (24/7 framing)
2. Drain cleaning + sewer camera
3. Water heater service (tank + tankless)
4. Faucet / fixture install & repair
5. Gas line installation & service
6. Toilet install & repair
7. Garbage disposal install & repair
8. HVAC / Heating & Air Conditioning (full service)
9. Bathtub install & repair
10. Sewer line locate + repair

## Photos

- **Owner-supplied:** None yet. Jesse has no direct photos for this site.
- **GBP photos visible in screenshot:** (a) blue-tape pipe repair against brick, (b) sewer line excavation with mini-excavator and exposed septic tank + pipes. Low-res screenshot only, not usable as assets.
- **Action plan:**
  1. Attempt Firecrawl Layer 2 pull from GBP (blocked historically but worth trying)
  2. If fails, write hero-brief.json for Recraft AI-generated hero
  3. Ask Jack directly for phone-camera photos of recent work (same approach as Fernando at Pine Peach)

## Owner & Legacy

- **Jack Sr.** — Business Owner per Yelp verified profile
- **1968 founding** = likely father → son or multi-generational trade operation
- **58 years** in Atlanta metro is real differentiation vs. franchise chains
- **Timeline section:** eligible. Use decade anchors: 1968 founding, 1970s-90s growth, 2000s HVAC expansion, current 24/7 emergency ops. Frame as "three generations" if generationally verified; otherwise "58 years, family-run."

## Differentiators (for copy)

- 58 years in business, family-owned
- Full-service: plumbing + HVAC under one roof (one call)
- Jack Sr. still the face — "ask for Jack" copy angle
- 24-hour availability (real emergency line)
- 4.9 / 25 on Google (5-star dominant distribution)
- Sandy Springs + metro Atlanta
- Accepts credit cards (Yelp verified)

## Brand Direction

- **Primary color:** muted traditional blue — `#1a4d80` (deep water-main navy)
- **Accent:** warm antique copper — `#c8893f` (distinguishes from Bravo's similar palette)
- **Typography:** per CLAUDE.md standards (Cormorant Garamond + Plus Jakarta Sans)
- **Vibe:** traditional trade company that's been around forever, not flashy, credible-by-longevity

## Open Questions for Jesse to Close With Jack

1. Full last name (currently "Jack Sr. S.")
2. 5-8 verbatim Google reviews with reviewer first names (copy from GBP Reviews tab)
3. 1968 founding year confirmation
4. Generational detail — is this Jack Jr. now running it? Still Jack Sr.? How many generations?
5. Georgia plumbing license number
6. HVAC license (separate from plumbing in GA)
7. Bonded and insured certificate info for footer
8. Photos — phone camera shots of recent jobs (plumbing + HVAC)
9. Hours: 24-hour real answer-the-phone, or triage/call-back at night?
10. Warranty terms on plumbing + HVAC work
11. Service-call fee or free estimates?
12. Payment methods beyond credit cards (financing? checks?)

## Data Sources

- GBP screenshot supplied by Jesse 2026-04-17 (listing: "Sandy Springs Plumbing Heating Air Condi...", 4.9/25, 56 Perimeter Center E Ste 150-C Dunwoody — treated as the authoritative rating surface but NOT as the address)
- Yelp screenshot supplied by Jesse 2026-04-17 (listing: "SandySprings Heating Plumbing", 1.0/2, 165 Hilderbrand Dr Atlanta 30328 — treated as the authoritative address surface; 1.0 rating excluded)
- Jack Sr.'s direct phone: (770) 896-9852 (supplied by Jesse)

## Flags for reviews.json

- `owner_input_required_before_publish` — verbatim reviews needed
- `owner_full_name_needed` — Jack's last name
- `identity_consolidated_from_two_listings` — Jesse decision 2026-04-17
- `photos_pending` — no owner-supplied photos yet
