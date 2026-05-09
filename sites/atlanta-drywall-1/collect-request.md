---
slug: atlanta-drywall-1
requested_by: mini
requested_at: 2026-05-09T02:30:00Z
priority: high
type: email-research
---

# Collect-request — Atlanta Drywall

## Why this request

`outreach_staged` prospect with no email on file. Mini's quick scrape attempt on `https://atlantadrywall1.com` returned engine failures across all Firecrawl proxies — site may be geo-blocked, down, or have aggressive anti-bot. Bruce has more rendering options (real browser session, proxy rotation, etc.).

## Business identity

- **Name:** Atlanta Drywall
- **Phone:** (678) 508-6846
- **Address:** 6652 Ramgates Way NW, Norcross GA 30093
- **Website:** https://atlantadrywall1.com (Mini couldn't reach)
- **GBP:** https://www.google.com/maps?cid=11264907972791059949 (use this for Google Places API email lookup)
- **Claim code:** FHWL8920

## Requested sources (priority order)

1. **Owner site direct fetch** — try `https://atlantadrywall1.com`, `/contact`, `/about`, `/contact-us`. Bruce's persistent-browser rendering may succeed where Mini's failed. Look for mailto: links + contact form mailto fallback + footer email.
2. **Google Business Profile** via GBP cid `11264907972791059949` — Places API call may return an email field that's not exposed on GBP web UI.
3. **Apollo** — search by phone (678) 508-6846 or by business name + Norcross GA.
4. **GA Secretary of State** — search "Atlanta Drywall" registrations. The `1` suffix in the slug suggests there are multiple entities; identify the right LLC.
5. **Yelp / Nextdoor / Thumbtack / Angi** — drywall contractors are common on these platforms; owner email sometimes surfaces.

## Budget

- max_wallclock_minutes: 8
- max_sources_attempted: 6

## Output expected

Verified email → update Supabase `prospects.email` for slug `atlanta-drywall-1` + contact_verified=TRUE + provenance note.

If blocked → `messages/<date>-bruce-email-research-blocked-atlanta-drywall-1.md` describing engine failures vs site genuinely lacking email.

— Mini
