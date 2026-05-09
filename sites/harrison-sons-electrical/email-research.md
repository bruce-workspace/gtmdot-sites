---
slug: harrison-sons-electrical
researched_at: 2026-05-09T02:31:58Z
status: no_verified_email_found
---

# Email Research — Harrison & Sons Electrical Service LLC

## Summary

No verified public email was found within the one-attempt-per-source rule. Do not write Supabase from this result.

## Source attempts

### 1. GA Secretary of State business registry — FAILED
- Reason code: `blocked-by-robots-txt`
- Attempt: Direct registry lookup page at `https://ecorp.sos.ga.gov/BusinessSearch` for “Harrison & Sons Electrical Service” LLC.
- Result: HTTP 403 from registry endpoint. Browser navigation was also blocked by policy before page load. No bypass or retry attempted.

### 2. Apollo enrichment — FAILED
- Reason code: `login-wall`
- Attempt: No authenticated Apollo enrichment surface/API was available in this runtime. Public web search for exact business name + email returned no email-bearing result.
- Result: No email found.

### 3. Owner-site full-render scrape — FAILED
- Reason code: `not-found`
- Attempt: Render/scrape pass on `https://harrisonelectrical.homes/contact-us/`, `/about/`, and `/our-services/` using Firecrawl JS rendering, plus static fetch.
- Result: No `mailto:` or email address found. Contact page exposes phone, address, and a form only. `/about/` returned effectively empty/404-equivalent content.

### 4. Google Business Profile / Places API — FAILED
- Reason code: `not-found`
- Attempt: Places API search for “Harrison & Sons Electrical Atlanta”.
- Result: GBP matched `place_id: ChIJG6FR32Mf9YgRP06hlpa90jg`, operational, address and phone confirmed. Details response exposed no website/email field and no email field is available through the selected Places details fields.

### 5. LinkedIn / Apollo people-search — FAILED
- Reason code: `not-found`
- Attempt: Web search for LinkedIn profiles matching Harrison + electrician + Atlanta.
- Result: Results included unrelated or weak matches; no profile was confidently tied to Harrison & Sons Electrical Service LLC and no work email was surfaced.

## Verified business details confirmed during research

- Name: Harrison & Sons Electrical Service LLC
- Phone: (404) 574-5123
- Address: 3695 Cascade Rd #6250 / STE 6250, Atlanta, GA 30331
- Website: `https://harrisonelectrical.homes`
- Google place ID: `ChIJG6FR32Mf9YgRP06hlpa90jg`

## Email result

- Verified email: none found
