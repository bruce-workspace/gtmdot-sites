# Approved Three-Prospect Postcard Batch Completion

Date: 2026-05-23
Lane: Outreach Operations
Mode: approved postcard-only execution with stop-on-error

## Scope

Jesse approved postcard-only Poplar submission for exactly:

- `24-hrs-mobile-tire-services`
- `bravo-plumbing-solutions`
- `browning-electrical-services`

No Resend/email sends, SMS, prospect/customer contact, manual CRM/Supabase truth
edits, Paperclip mutations, deploys, postcard CDN repairs, DNS/domain/hosting
changes, billing/Stripe actions, or git pushes were performed.

## Final Gates

Immediately before submit, all three prospects passed:

- canonical `outreach-readiness-gate.sh`
- preview URL live check
- claim-code/checkout lookup
- desktop screenshot `image/jpeg`
- mobile screenshot `image/jpeg`
- hero image `image/jpeg`
- `preview_postcard_payload` 200
- recipient/address constraint check
- stale-note recheck against current evidence

## Submit Results

| Prospect | CRM event | Poplar order ID | Provider state | Cost | Action |
| --- | --- | --- | --- | --- | --- |
| `24-hrs-mobile-tire-services` | postcard `submitted` at `2026-05-23T19:01:37.142818+00:00` | `8b46f6b0-07a9-4242-851e-7fd3d488ff72` | `exception` | `$0.00` | Stop, do not retry |
| `bravo-plumbing-solutions` | postcard `submitted` at `2026-05-23T19:01:44.788904+00:00` | `f8edcd41-3cfd-4d2e-b099-abd6e4a33f33` | `processing` | `$0.92` | Monitor provider progression |
| `browning-electrical-services` | postcard `submitted` at `2026-05-23T19:01:49.034522+00:00` | `e4c06518-961b-4663-b0ac-3def18321328` | `processing` | `$0.92` | Monitor provider progression |

## Provider Evidence

### `24-hrs-mobile-tire-services`

- Order ID: `8b46f6b0-07a9-4242-851e-7fd3d488ff72`
- State: `exception`
- Created: `2026-05-23T19:01:37Z`
- Address normalized by Poplar:
  - `Current Resident`
  - `396 PIEDMONT AVE NE`
  - `ATLANTA, GA 30308`
- Merge tags:
  - `claim_code`: `HMTS3276`
  - `hostname`: `24-hrs-mobile-tire-services.pages.dev`
  - `business_name`: `24 hrs Mobile Tire Services`
- Exact next action: do not retry. Investigate Poplar exception reason from
  provider UI/API, then prepare a corrected payload only if needed.

### `bravo-plumbing-solutions`

- Order ID: `f8edcd41-3cfd-4d2e-b099-abd6e4a33f33`
- State: `processing`
- Created: `2026-05-23T19:01:44Z`
- Address normalized by Poplar:
  - `Forrell Hillery`
  - `105 BOND DR`
  - `ELLENWOOD, GA 30294`
- Merge tags:
  - `claim_code`: `BPST1027`
  - `hostname`: `bravo-plumbing-solutions.pages.dev`
  - `business_name`: `Bravo Plumbing Solutions`
- Exact next action: monitor provider progression from `processing` to
  production/mailed/delivered or exception.

### `browning-electrical-services`

- Order ID: `e4c06518-961b-4663-b0ac-3def18321328`
- State: `processing`
- Created: `2026-05-23T19:01:48Z`
- Address normalized by Poplar:
  - `Current Resident`
  - `3742 BITTERCREEK WAY SW`
  - `LILBURN, GA 30047`
- Merge tags:
  - `claim_code`: `TPSA5780`
  - `hostname`: `browning-electrical-services.pages.dev`
  - `business_name`: `Browning Electrical Services`
- Exact next action: monitor provider progression from `processing` to
  production/mailed/delivered or exception.

## CRM Channel Truth

The CRM detail endpoint now contains postcard `submitted` outreach events for
all three. The CRM list endpoint derives `postcardStatus: submitted` for all
three.

Important mismatch: all three prospects still appear in CRM stage
`needs_approval` after successful `submit_postcard` calls. This means the
production action path did not advance `needs_approval` to `outreach_sent`, even
though the channel event exists. No manual CRM backfill was performed.

Recommended next action: coordinator should record a CRM/platform blocker for
successful postcard sends from `needs_approval` not advancing stage, and decide
whether to approve a narrow backfill. Until then, channel truth should come from
outreach events/provider state, not stage alone.

## Explicit No-Action Statement

No retry was attempted for the `24-hrs-mobile-tire-services` Poplar exception.
No email, SMS, prospect/customer contact, manual CRM/Supabase truth edit,
Paperclip mutation, deploy, git push, DNS/domain/hosting/billing change, or
Stripe action was performed.
