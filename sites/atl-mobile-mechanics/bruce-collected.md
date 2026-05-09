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
