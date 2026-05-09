---
slug: atl-mobile-mechanics
requested_by: mini
requested_at: 2026-05-09T02:30:00Z
priority: high
type: email-research
---

# Collect-request — ATL Mobile Mechanics (Joseph)

## Why this request

Per Jesse 2026-05-08 directive: every `outreach_staged` prospect needs both email + postcard send capability. ATL Mobile Mechanics is at `outreach_staged` but `prospects.email` is NULL — Send Email button is gated off. This is enrichment work in Bruce's lane (§11) — Mini can't autonomously source contact info.

Owner-operator. Phone-based businesses sometimes have owner email surfaced via Apollo, GA Secretary of State business registry, or social profiles.

## Business identity

- **Name:** ATL Mobile Mechanics
- **Owner:** Joseph
- **Phone:** (470) 809-3146
- **Address:** 8816 Countryside Way, Douglasville GA 30134
- **GBP:** none captured in CRM — Bruce search may surface
- **Existing website:** none captured
- **Claim code:** SVYG3351
- **Note:** same address + phone as `douglasville-mobile-mechanics` (separate prospect, same owner Joseph). Open duplicate-decision flag in CRM is for Jesse — DO NOT mark dead. This collect-request is for email only.

## Requested sources (priority order)

1. **Apollo enrichment** — search by phone (470) 809-3146 OR by business name + city + state (ATL Mobile Mechanics, Douglasville, GA). Apollo often returns owner work email for owner-operated trades.
2. **GA Secretary of State** — `https://ecorp.sos.ga.gov/BusinessSearch/` — search "ATL Mobile Mechanics" or "Mobile Mechanics" in Douglasville. LLC registrations include registered-agent contact info which often has email.
3. **Google Business Profile** — search Google Maps for "ATL Mobile Mechanics Douglasville GA". GBP listing's "Contact" section sometimes exposes email.
4. **Yelp / Nextdoor / Thumbtack / Angi / Facebook** — owner profile pages on these platforms occasionally list email.

## What "found" means

Verified email = an address that's clearly the owner's business contact (not generic CMS noreply, not a random scraped string). Provenance citation in the response file.

## Budget

- max_wallclock_minutes: 8
- max_sources_attempted: 6
- DO NOT scrape photos / reviews — this request is email-only

## Output expected

If found: update Supabase `prospects.email` for slug `atl-mobile-mechanics` with the verified address, set `contact_verified=TRUE`, and add a note with provenance.

If not found: write `messages/<date>-bruce-email-research-blocked-atl-mobile-mechanics.md` with what was tried + failure modes.

— Mini
