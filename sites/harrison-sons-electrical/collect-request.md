---
slug: harrison-sons-electrical
requested_by: mini
requested_at: 2026-05-09T02:30:00Z
priority: high
type: email-research
---

# Collect-request — Harrison & Sons Electrical Service LLC

## Why this request

`outreach_staged` LLC with no email on file. Mini scraped `https://harrisonelectrical.homes` and `/contact-us/` — only phone + a contact form, no public mailto. LLCs almost always have a registered-agent email on the GA SoS registry; that's the most likely source.

This site has **separate FTC-risk concerns** (Unsplash stock photos + fake testimonial attributions) flagged in CRM and tracked. Email research is independent of those — proceed regardless.

## Business identity

- **Name:** Harrison & Sons Electrical Service LLC
- **Phone:** (404) 574-5123
- **Address:** 3695 Cascade Rd STE 6250, Atlanta GA 30331
- **Website:** https://harrisonelectrical.homes (verified live, no public mailto)
- **GBP:** none captured
- **Owner family:** Harrison
- **In business:** since 2005 per the website
- **Claim code:** HARR2423

## Requested sources (priority order)

1. **GA Secretary of State business registry** — search "Harrison & Sons Electrical Service" LLC. Registered-agent contact info is public and often includes the owner's email. This is the highest-confidence source for an LLC of this age.
2. **Apollo enrichment** — search by phone (404) 574-5123 or by business name + Atlanta. Older LLCs (2005) usually have someone on Apollo.
3. **Owner-site full-render scrape** — Bruce with persistent-browser session, JS-rendered. Try `https://harrisonelectrical.homes/contact-us/`, `/about/`, `/our-services/`. Sometimes contact forms have a hidden mailto fallback or owner email in the HTML source that Mini's static fetch missed.
4. **Google Business Profile** — Maps search "Harrison & Sons Electrical Atlanta". Places API email field if exposed.
5. **LinkedIn / Apollo people-search** — "Harrison" + electrician + Atlanta — surfaces an owner profile sometimes with work email.

## Budget

- max_wallclock_minutes: 10 (slightly longer because GA SoS lookup is the priority — give it time)
- max_sources_attempted: 6

## Output expected

Verified email → update Supabase + provenance note. Else block message.

— Mini
