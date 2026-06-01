# 24 Hrs Mobile Tire Services Postcard Exception / UI Diagnosis - 2026-05-31

Owner: Codex / GTMDot quarterback  
Mode: read-only diagnosis  
Status: confirmed broken state; no retry performed

## Question

Jesse saw that `24-hrs-mobile-tire-services` looks ready and the postcard proof
looks fine, but the CRM UI does not expose a send button.

## Current CRM State

Public CRM list:

- Slug: `24-hrs-mobile-tire-services`
- Stage: `outreach_staged`
- `postcardStatus`: `submitted`
- Email: `null`
- Address: `396 Piedmont Ave NE, Atlanta, GA 30308`
- Phone: `(470) 502-8141`
- Preview URL: `https://24-hrs-mobile-tire-services.pages.dev`
- Claim code: `HMTS3276`

CRM detail outreach events:

- One postcard event exists:
  - `eventType`: `submitted`
  - Created: `2026-05-23T19:01:37.142818+00:00`
  - Poplar order ID: `8b46f6b0-07a9-4242-851e-7fd3d488ff72`

Important mismatch:

- CRM list derives `postcardStatus=submitted` from the event.
- CRM detail raw prospect still shows `postcardStatus=not_submitted`.
- The detail UI passes `postcardsSent={outreach.filter(e => e.channel === 'postcard').length}`, so one postcard event disables the send button even if the provider order is in exception.

## Current Poplar State

Fetched Poplar read-only:

- Order ID: `8b46f6b0-07a9-4242-851e-7fd3d488ff72`
- State: `exception`
- Cost: `$0.00`
- Expected delivery date: `null`
- Created: `2026-05-23T19:01:37Z`
- `send_at`: `null`

Address in Poplar:

```text
Current Resident
396 PIEDMONT AVE NE
ATLANTA, GA 30308
```

Poplar API did not expose the exact exception reason in the fetched response.

## Asset Checks

Read-only URL checks:

- `https://gtmdot-postcards.pages.dev/24-hrs-mobile-tire-services-hero.jpg`
  returned `200 image/jpeg`.
- `https://gtmdot-postcards.pages.dev/screenshots/24-hrs-mobile-tire-services-mobile.jpg`
  returned `200 image/jpeg`.
- `https://gtmdot-postcards.pages.dev/screenshots/24-hrs-mobile-tire-services-desktop.jpg`
  returned `200 image/jpeg`.
- Preview site returned `200 text/html`.
- Checkout URL returned `200 text/html`.

Interpretation:

- The exception is unlikely to be a missing postcard image asset.
- It is more likely address/deliverability/provider validation or another
  Poplar-side exception not exposed by the API.

## Email Enrichment State

No deeper current email enrichment evidence was found in local artifacts.

Current CRM has:

- `email=null`
- `hasEmail=false`

The site/business has strong phone/address/GBP enrichment and good photo
enrichment, but no email channel is currently available.

## Why The Button Is Missing

The button is disabled because the UI treats any postcard event as sent.

Current local UI logic:

- `ProspectDetail.tsx` passes `postcardsSent` as count of all postcard outreach
  events.
- `ActionButtons.tsx` allows send only when `postcardsSent === 0`.
- Since the failed/exception Poplar attempt created a `submitted` event, the UI
  renders the postcard as already sent.

This is too blunt. The UI needs provider-aware state:

- submitted / accepted by provider,
- exception,
- in transit,
- delivered,
- retry approved,
- retry prohibited.

## Current Operational Answer

Do not send or retry from the UI right now.

`24-hrs-mobile-tire-services` has already had a Poplar submission attempt, but
the provider state is `exception`, so it has not progressed like a healthy
postcard. The CRM stage `outreach_staged` is reasonable only if it means
"provider exception needs resolution before outreach is complete."

## Recommended Fix

1. Add a visible provider-exception state in the CRM UI.
2. For postcard events with Poplar `exception`, show:
   - order ID,
   - provider state,
   - "Retry blocked until diagnosis/approval",
   - a "Prepare retry packet" action.
3. Do not hide behind "Postcard Sent" when provider state is exception.
4. Stage logic should distinguish:
   - `outreach_staged`: ready/needs send,
   - `outreach_exception`: attempted but provider failed,
   - `outreach_sent`: provider accepted/in transit/delivered.

## Exact Approval Needed For Next Step

```text
Approved: diagnose 24 Hrs Mobile Tire Services Poplar exception only.

Allowed:
1. Re-fetch Poplar order 8b46f6b0-07a9-4242-851e-7fd3d488ff72 read-only.
2. Inspect asset URLs, preview URL, checkout URL, and postcard payload dry-run.
3. Check whether the exception is address/deliverability/provider-side or payload-related.
4. Write a retry recommendation packet.

Still prohibited:
Poplar retry/resubmit, CRM writes, Paperclip mutations, deploys, sends,
prospect contact, git pushes, DNS/domain/hosting/billing changes, and Stripe
actions.
```

## Explicit No-Action Statement

No CRM/Supabase writes, Paperclip mutations, deploys, Poplar retries/sends,
Resend/SMS sends, prospect/customer contact, git pushes, production site edits,
DNS/domain/hosting/billing changes, Stripe actions, or destructive cleanup were
performed.
