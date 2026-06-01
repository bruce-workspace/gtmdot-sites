# Poplar Provider-State Integration Fix

Date: 2026-05-31
Owner: Codex
Mode: local code fix, no deploy, no send

## Problem

The CRM postcard submit path treated a successful Poplar HTTP response as a successful mailing. Poplar can return HTTP 200 and still create the mailing in a provider failure state such as `exception`.

That is what happened with `24-hrs-mobile-tire-services`:

- CRM event: `submitted`
- CRM list status: `submitted`
- CRM stage: `outreach_staged`
- Poplar order: `8b46f6b0-07a9-4242-851e-7fd3d488ff72`
- Poplar provider state: `exception`
- Cost: `0.00`
- Expected delivery: `null`

The UI then hid the normal send button because it counted any postcard event as already sent, even though provider truth was not healthy.

## Local Fix Implemented

Updated `brucecom-v3` locally:

- `src/lib/poplar.ts`
  - Live `submitPostcard()` now preserves Poplar `state` / `status`, expected delivery date, total cost, and raw response body.
  - Return type now distinguishes live submit results from dry-run results.

- `src/app/api/prospects/[id]/actions/route.ts`
  - Poplar provider failure states are now detected after a live submit:
    - `exception`
    - `failed`
    - `failure`
    - `error`
    - `invalid`
    - `validation_failed`
    - `suppressed`
    - `cancelled`
    - `canceled`
  - Provider failures are recorded as postcard event type `suppressed` instead of `submitted`.
  - Provider failures do not auto-advance the prospect to `outreach_sent`.
  - The action returns HTTP 502 with an explicit provider-exception message so the UI no longer treats the click as successful.
  - Event metadata now includes `orderId`, `providerState`, `expectedDeliveryDate`, `totalCost`, and Poplar raw response.

- `src/app/api/webhooks/poplar/route.ts`
  - Poplar webhook statuses like `exception`, `failed`, `invalid`, and `validation_failed` now map to existing postcard event type `suppressed`.
  - A visible activity item is written when a provider exception webhook arrives.

- `src/app/api/prospects/route.ts`
  - Derived postcard status now prioritizes failure states (`suppressed`, `returned`) over submitted/in-production states.

- `src/components/prospect/ProspectDetail.tsx`
  - The action button now separates healthy postcard events from provider failure events.

- `src/components/prospect/ActionButtons.tsx`
  - Provider-failed postcards display as `Postcard Exception` instead of `Postcard Sent`.
  - Retry remains disabled until the exception is diagnosed and explicitly approved.

## Verification

Passed:

- `npx tsx` local payload check confirms long recipient names are shortened safely:
  - Input: `Harrison & Sons Electrical Service`
  - Output first_name: `Harrison & Sons`
  - Length: `15`
- `npx tsx` import check loaded the changed Poplar webhook route and prospect action route successfully:
  - `src/app/api/webhooks/poplar/route.ts`
  - `src/app/api/prospects/[id]/actions/route.ts`

Blocked by unrelated repo state:

- `npm run build` is blocked by missing CRM v2 sandbox import:
  - `src/app/lab/crm-v2/sandbox.tsx`
  - missing `./components/CockpitHeader`
- `./node_modules/.bin/tsc --noEmit --pretty false` is blocked by the same missing CRM v2 import plus existing test import-extension errors.

These failures are not from the Poplar files changed in this patch.

## Current 24 Hrs State

This local code fix prevents the next Poplar `exception` from being mis-recorded as a successful submit. It does not retroactively repair the existing `24-hrs-mobile-tire-services` CRM event because that would be a CRM/Supabase truth write.

Recommended next approval, after review:

```text
Approved: reconcile 24-hrs-mobile-tire-services Poplar exception state in CRM.

Allowed:
1. Add a postcard outreach event for 24-hrs-mobile-tire-services using existing event type suppressed, with Poplar order ID 8b46f6b0-07a9-4242-851e-7fd3d488ff72 and providerState exception.
2. Add a matching activity/note that the Poplar mailing is in provider exception and must not be counted as successfully sent.
3. Do not retry or resubmit the postcard.
4. Do not send email/SMS or contact the prospect.
5. Do not deploy, push git, mutate Paperclip, or change unrelated CRM fields.
```

Separate approval would be needed to deploy the code fix to the public CRM runtime and/or retry the postcard.

## Explicit No-Action Statement

No deploy, Poplar send/retry/resubmit, Resend/SMS send, prospect contact, Paperclip mutation, git push, DNS/domain/hosting/billing change, Stripe action, or CRM/Supabase write was performed for this fix.
