---
slug: atl-mobile-mechanics
request_id: 2026-05-09T02:30:00Z
collected_at: 2026-05-09T02:34:13Z
collector: bruce
status: partial
---

# Bruce Collected — ATL Mobile Mechanics

## Summary

Completed the email research waterfall and generated the postcard hero. No verified email was found. The postcard hero was generated with `openai/gpt-image-2`, resized to the required print spec, and saved in `photos-generated/`.

## Email research results

### Apollo enrichment — FAILED
- Reason code: `login-wall`
- Detail: No authenticated Apollo enrichment surface/API available in runtime. Public exact-match searches by phone/name did not surface an email.

### GA Secretary of State business registry — FAILED
- Reason code: `captcha`
- Detail: Registry search form rendered via Scrapfly, but the submitted search was blocked/failed behind the anti-bot flow. Browser navigation to the registry was blocked by policy. No retry or bypass attempted.

### Google Business Profile / Google Maps — FAILED
- Reason code: `not-found`
- Detail: Google Places API search for `ATL Mobile Mechanics Douglasville GA` returned `ZERO_RESULTS`. No GBP email surfaced.

### Owner website — FAILED
- Reason code: `not-found`
- Detail: `https://atlmobilemechanics.com/` confirms the business, phone, address, 24/7 hours, contact form, newsletter form, and Facebook link, but exposes no email or `mailto:`.

### Yelp / Chamber / Facebook / Nextdoor / Thumbtack / Angi — FAILED
- Reason code: `not-found`
- Detail: Yelp and Chamber were found but fetches returned JS/anti-bot interstitials with no email. Facebook pages errored/no extractable public email. Thumbtack, Angi, and Nextdoor searches found no matching email-bearing profile.

## Email handoff

- Verified email: none found
- Supabase write: not performed by Bruce
- Details: `sites/atl-mobile-mechanics/email-research.md`

## Postcard hero

- Status: success
- File: `sites/atl-mobile-mechanics/photos-generated/hero-postcard.jpg`
- Dimensions: 3360×1872 px
- Format: JPEG, quality 90, RGB/sRGB-compatible
- Model stack: `openai/gpt-image-2`
- Guardrail license note: Synthetic image. Do not represent as actual company work.
- Intended slot context: aspirational-business-OK | atmosphere-OK
- QA: dimensions and format verified with `sips`/`file`.

## Files written

- `sites/atl-mobile-mechanics/email-research.md`
- `sites/atl-mobile-mechanics/photos-generated/hero-postcard.jpg`
- `sites/atl-mobile-mechanics/bruce-asset-intel.json`
- `sites/atl-mobile-mechanics/bruce-asset-intel.md`
- `sites/atl-mobile-mechanics/bruce-collected.md`

## Reviews (2026-05-13 scrape)

Source: Google Business Profile / Google Places Details API for `Atl Mobile Mechanic's,We Come To U!!` (`cid=4964704970564788666`), rating 4.0 across 174 Google reviews at scrape time. Returned listing phone/address differ from the site record, but the review content names Joseph and matches Mini's requested owner context.

### "Joseph is great 10/10 definitely recommend"
- text: Joseph is great 10/10 definitely recommend!! My new mechanic He gets the job done fast!! Price are reasonable. Definitely can count on him anyday and time!!
- reviewer: A'leetra Woods
- rating: 5
- source: Google Business Profile
- scraped_at: 2026-05-13T02:21:22Z

### "Fair pricing and knowledgeable"
- text: Great service, can tell he takes pride in what he does man is a actual mechanic that is fair in pricing and knowledgeable would recommend to anyone.
- reviewer: Matt Ruffino
- rating: 5
- source: Google Business Profile
- scraped_at: 2026-05-13T02:21:22Z

### "No one could get my car running right until I called"
- text: I went to several mechanics. No one could get my car running right until I called this service and he found other issues that I didn’t know. I had definitely would use it again best mechanic ever.
- reviewer: KING LION
- rating: 5
- source: Google Business Profile
- scraped_at: 2026-05-13T02:21:22Z

### "Had an issue with an alternator"
- text: Professionalism to the core with expert guidance in helping with the trouble of vehicles these days. Had an issue with an alternator, called, Mr Joseph gave his analytics, gave a time as to when he could come and have it prepared with the breakdown of pricing and have been smooth sailing since then .

I highly recommend them in ATL. Referred some of my family members, we even mentioned that he offered us a family referal discount lol 😆.
- reviewer: Keevian Burnette
- rating: 5
- source: Google Business Profile
- scraped_at: 2026-05-13T02:21:22Z

