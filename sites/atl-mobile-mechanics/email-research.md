---
slug: atl-mobile-mechanics
collected_at: 2026-05-09T02:34:13Z
collector: bruce
status: partial
email_found: false
---

# Email Research — ATL Mobile Mechanics

## Result

No verified owner/business email found in the allowed one-pass source waterfall.

## Source attempts

### Apollo enrichment — FAILED
- Reason code: `login-wall`
- Attempt: checked runtime for Apollo credentials/API access and searched public web by phone/name.
- Detail: No authenticated Apollo enrichment surface/API was available in this runtime. Exact public searches for `(470) 809-3146`, `ATL Mobile Mechanics`, `Douglasville`, and `Joseph` did not surface a verified email.

### GA Secretary of State business registry — FAILED
- Reason code: `captcha`
- Attempt: loaded `https://ecorp.sos.ga.gov/BusinessSearch` with Scrapfly render and attempted a one-pass business-name search for `ATL Mobile Mechanics`.
- Detail: Initial render loaded the search form, but direct browser access was blocked by policy and the rendered search execution failed behind the registry's anti-bot/Cloudflare flow. No retry or bypass attempted.

### Google Business Profile / Google Maps — FAILED
- Reason code: `not-found`
- Attempt: Google Places API search for `ATL Mobile Mechanics Douglasville GA`.
- Detail: Places API returned `ZERO_RESULTS`. Public web search did surface a current owner website at `https://atlmobilemechanics.com/`, but no Google Maps/GBP profile exposing an email was found.

### Owner website — FAILED
- Reason code: `not-found`
- Attempt: fetched `https://atlmobilemechanics.com/`.
- Detail: The site confirms `ATL Mobile Mechanics`, phone `470-809-3146`, address `8816 Countryside Way, Douglasville, GA`, 24/7 hours, contact form, newsletter form, and Facebook link. No email address or `mailto:` was present in extracted page content.

### Yelp / Chamber / Facebook / Nextdoor / Thumbtack / Angi — FAILED
- Reason code: `not-found`
- Attempt: searched and/or fetched platform pages once each where available.
- Detail: Yelp and Chamber profiles were found in search results but fetches returned JS/anti-bot interstitials and did not expose email. Facebook links returned errors/no public extractable email. Source-specific searches for Thumbtack, Angi, and Nextdoor returned no matching profile with email.

## Discovered contact/context

- Website: `https://atlmobilemechanics.com/`
- Website Facebook link: `https://www.facebook.com/700681096468925`
- Search-result Facebook page: `https://www.facebook.com/61578289512852`
- Yelp: `https://www.yelp.com/biz/atl-mobile-mechanics-douglasville`
- Chamber: `https://www.chamberofcommerce.com/business-directory/georgia/douglasville/car-repair-and-maintenance/2033840603-atl-mobile-mechanics`

## Email handoff

- Verified email: none found
- Supabase write: not performed by Bruce
