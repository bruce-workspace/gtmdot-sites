# Outreach Operations -> Main GTMDot Session Summary: GTM-8

Date: 2026-05-16 America/New_York
From: Outreach Operations Codex lane
To: Main GTMDot session / quarterback
Related Paperclip issues: GTM-2, GTM-8, GTM-9, GTM-19, GTM-20

## What Was Handled

GTM-8 was completed as a read-only provider/CRM inspection and recommendation pass.

Created durable artifact:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-gtm-8-poplar-postcard-progression.md`

## Scope Completed

For all 13 `outreach_sent` postcard order IDs from GTM-7, the artifact records:

- prospect name and slug
- CRM stage
- Poplar order ID
- CRM postcard state
- Poplar provider state
- normalized postcard state
- evidence source
- exact next action

## Key Results

- CRM still shows all 13 postcards as `submitted` only.
- Poplar provider currently shows 11 orders as `state=in_transit`.
- Poplar provider currently shows 2 orders as `state=exception`.
- No Poplar provider deliveries yet.
- No provider returns yet.
- No provider suppressions/cancellations found.
- All 11 in-transit orders have expected delivery date `2026-05-19`.
- The two exception orders have `total_cost=0.00` and no expected delivery date.

## Exception Orders

- Atlanta Drywall — order `6deb9d29-ba56-40cd-9027-1ca5dfc9ac10`
- Perez Pools LLC — order `7158568c-2f52-4a2d-84ce-b5e7783715e1`

Recommended action: do not resend automatically. Investigate exception reason in Poplar UI/support, then decide whether to fix and resubmit only with Jesse approval.

## In-Transit Orders

- Atlanta Pro Repairs
- Tech On The Way
- Atl Mobile Mechanics
- Affordable Concrete & Repair
- Locksmith Atlanta Pro
- Golden Choice Pro Wash
- Morales Landscape & Construction
- Roberts Mobile Services
- Done Right Drywall
- Membreno's Pro Home Repair
- Moonstone Pressure Washing

Recommended action: treat operationally as `mailed / in_transit`, expected delivery `2026-05-19`, but do not backfill CRM without explicit approval.

## Main Finding

Poplar progression is real, but CRM is stale. CRM has `postcard/submitted` only, while Poplar already shows `in_transit` or `exception` for every submitted order.

The current Poplar webhook path may not be receiving or mapping the provider states. The webhook maps submitted/in_production/mailed/delivered/returned/suppressed, but does not explicitly map `in_transit`, and no post-submission postcard events are present in CRM.

The legacy checker polls Poplar but writes `gtmdot/poplar-sends.json`, not CRM `outreach_events`, so it does not solve channel-state truth.

## Recommended Next Action

Proceed to GTM-9: verify GTMDot email/reply watcher with a controlled internal alias test, not prospect contact.

Parallel/platform follow-up for GTM-19/GTM-20:

- Add provider postcard state to CRM channel-state model.
- Add dry-run-first Poplar reconciliation that proposes CRM backfills before writing.
- Add webhook mapping for provider `in_transit` if Poplar emits that state.
- Add dashboard distinction between CRM submitted state and provider current state.

## Actions Explicitly Not Performed

- No CRM writes.
- No Paperclip writes.
- No Poplar submissions.
- No Poplar status backfills.
- No Resend/email sends.
- No SMS sends.
- No prospect/customer contact.
- No deploys, production edits, or git pushes.
