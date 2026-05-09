---
from: mini-to-bruce
to: cloakanddagger_bot
date: 2026-05-08
subject: Email research — 5 outreach_staged prospects missing email addresses
priority: high
refs:
  - Jesse 2026-05-08 directive: "All prospects in outreach_staged should have ability to send both email AND postcard"
  - HANDOFF-CONTRACT.md §11 (Bruce-as-Collector)
---

# Email research — 5 outreach_staged prospects missing email

## Context

Jesse wants every `outreach_staged` prospect to be sendable on both channels (postcard + email). Of the 12 prospects currently at `outreach_staged`, **5 have no email address on file** in CRM. Postcard sends will work for them; email sends are blocked at the UI level (button disabled) until an email is populated.

Mini's quick scrape attempt on the 2 that have websites returned no public mailto. The Harrison & Sons site has only a contact form. Atlantadrywall1.com isn't reachable from the Mini's IP (Firecrawl returned engine failures across all proxies — possibly geo-blocked or down).

This is squarely Bruce's research/enrichment lane. Asking Bruce to source verified emails for these 5.

## The 5 prospects

| Slug | Business | Phone | Address | Website | Notes |
|---|---|---|---|---|---|
| `atl-mobile-mechanics` | Atl Mobile Mechanics | (470) 809-3146 | 8816 Countryside Way, Douglasville GA 30134 | none | Owner: Joseph (also owner of Douglasville Mobile Mechanics — same address+phone) |
| `atlanta-drywall-1` | Atlanta Drywall | (678) 508-6846 | 6652 Ramgates Way NW, Norcross GA 30093 | https://atlantadrywall1.com (Mini couldn't fetch; try directly) | Has GBP at https://www.google.com/maps?cid=11264907972791059949 |
| `done-right-drywall` | Done Right Drywall | (404) 903-3346 | 228 Triumph Dr NW, Atlanta GA 30327 | none | |
| `harrison-sons-electrical` | Harrison & Sons Electrical Service LLC | (404) 574-5123 | 3695 Cascade Rd #6250, Atlanta GA | https://harrisonelectrical.homes (no public mailto, only contact form) | Owner family name: Harrison. Site says "Serving Atlanta since 2005" |
| `roberts-mobile-services` | Roberts Mobile Services | (678) 663-4130 | 1598 Donald Lee Hollowell Pkwy NW, Atlanta GA 30318 | none | |

## What I'd ask Bruce to try (in priority order)

1. **Owner-site direct fetch** — for harrison-sons-electrical and atlanta-drywall-1, fetch their site (homepage + /contact + /about + /get-quote / similar) with full JS rendering and look for any email pattern, including JS-obfuscated ones. atlantadrywall1.com may need a different proxy / location.

2. **Google Business Profile** — for any prospect with a GBP listing, check the GBP for an email field. For atlanta-drywall-1 specifically: GBP `cid=11264907972791059949`. Some GBP listings expose email in the contact section even when the site doesn't.

3. **Apollo enrichment** — for owner-operated trades, Apollo's people-search by phone or business-name + city + state often returns the owner's work email. The 2 most likely to have Apollo-discoverable emails:
   - `harrison-sons-electrical` (LLC, has been in business since 2005, larger business — likely registered)
   - `atl-mobile-mechanics` (Joseph, owner-operator — phone-based search may work)

4. **HubSpot / Public registries** — GA Secretary of State business registry lists registered agent contact info for LLCs. Harrison & Sons is an LLC; could yield an email there.

5. **Yelp / Nextdoor / Thumbtack** — sometimes owners list a contact email on their profile pages even when their website doesn't.

6. **Facebook business page** — same — owner emails sometimes surface on FB about pages.

## What "found" means

For each prospect Bruce successfully sources an email for:

1. **Update the prospect in Supabase:**
   ```sql
   UPDATE public.prospects
   SET email = '<verified-email>',
       contact_verified = TRUE,
       updated_at = NOW()
   WHERE slug = '<slug>';
   ```
   The `has_email` column is generated from `email`, so it'll auto-update.

2. **Source the email in a comment/note** on the prospect record so we have provenance:
   ```sql
   INSERT INTO public.notes (prospect_id, author, body, status, note_type)
   SELECT id, 'bruce', 'Email sourced via <method>: <email>. <citation/url>', 'complete', 'general'
   FROM public.prospects WHERE slug = '<slug>';
   ```

3. **Don't fabricate.** If Bruce can't find a verified email, write a `bruce-email-research-blocked-<slug>.md` note describing what was tried and what was returned. Postcard-only campaigns are valid for those — Jesse can decide whether to still send postcard, or to mark them as needs-email-research and hold.

## Don't touch

- The 7 prospects in outreach_staged that DO have emails (no-op for those)
- Any prospect outside `outreach_staged`
- The hero regen request from earlier today (commit `c755099`) — that's a separate batch in flight

## Time pressure

Jesse wants outreach to start moving. Each found email unblocks a real send. Even if Bruce can only get 2-3 of 5, the other 2-3 default to postcard-only and the queue moves.

## When done

Write `messages/<date>-bruce-email-research-results-<batch-id>.md` summarizing:
- Found emails per prospect (with provenance)
- Failed prospects with reason
- Any duplicate / conflict signals (e.g., atl-mobile-mechanics shares phone with douglasville-mobile-mechanics — emails should differ if both are real)

Mini will pick up the deltas on next pull and verify the email previews render for each newly-sourced prospect.

— Mini Claude
