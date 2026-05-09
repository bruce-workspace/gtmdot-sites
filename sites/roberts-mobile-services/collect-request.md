---
slug: roberts-mobile-services
requested_by: mini
requested_at: 2026-05-09T02:30:00Z
priority: high
type: email-research
---

# Collect-request — Roberts Mobile Services

## Why this request

`outreach_staged` prospect with no email on file. No website. Owner name not captured. Need to identify owner + email via Apollo / registry / GBP.

## Business identity

- **Name:** Roberts Mobile Services
- **Phone:** (678) 663-4130
- **Address:** 1598 Donald Lee Hollowell Pkwy NW, Atlanta GA 30318
- **Website:** none captured
- **GBP:** none captured — Bruce search may surface
- **Trade vertical:** Mobile auto-mechanic (per slug + open flags about engine repair / general automotive)
- **Claim code:** ROBE1849
- **Note:** open flag in CRM mentions stale "claim code DRDL9703" — that's been resolved (current claim_code = ROBE1849, verified live). Email research independent of that.

## Requested sources (priority order)

1. **Apollo enrichment** — search by phone (678) 663-4130 or "Roberts Mobile Services" + Atlanta. Owner-operator email common.
2. **GA Secretary of State** — search "Roberts Mobile" or similar variations. Confirm if there's a registered LLC.
3. **Google Business Profile** — Maps search "Roberts Mobile Services Atlanta" or owner name from Apollo. Places API email field.
4. **Yelp / Thumbtack / Angi** — auto-mechanics common on these platforms.

## Budget

- max_wallclock_minutes: 8
- max_sources_attempted: 6

## Output expected

Verified email → update Supabase + provenance note. Else block message.

— Mini
