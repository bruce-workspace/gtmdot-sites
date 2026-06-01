# Poplar Provider Truth Audit

Date: 2026-06-01
Owner: Codex
Mode: read-only audit

## Summary

Codex compared public CRM postcard events/order IDs against Poplar provider truth.

Result:

- Poplar orders audited: `24`
- Provider exception / not actually healthy mail: `3`
- Healthy provider states: `21`

## Provider Exceptions

These postcards were recorded in CRM as postcard `submitted`, but Poplar currently reports provider `exception`, `total_cost = 0.00`, and no expected delivery date.

| Slug | Business | CRM Stage | CRM Postcard Status | Poplar Order | Poplar State |
|---|---|---|---|---|---|
| `24-hrs-mobile-tire-services` | 24 hrs Mobile Tire Services | `outreach_staged` | `submitted` | `8b46f6b0-07a9-4242-851e-7fd3d488ff72` | `exception` |
| `atlanta-drywall-1` | Atlanta Drywall | `outreach_sent` | `submitted` | `6deb9d29-ba56-40cd-9027-1ca5dfc9ac10` | `exception` |
| `perez-pools-llc` | Perez Pools LLC | `outreach_sent` | `submitted` | `7158568c-2f52-4a2d-84ce-b5e7783715e1` | `exception` |

## Healthy Provider States Found

The remaining audited postcard orders are in Poplar states such as `delivered`, `in_transit`, or otherwise costed with an expected delivery date.

Examples:

- `intire-mobile-tire-shop`: `delivered`, cost `0.92`, expected delivery `2026-05-25`
- `harrison-sons-electrical`: `in_transit`, cost `0.92`, expected delivery `2026-05-30`
- `smartwire-solutions`: `in_transit`, cost `0.92`, expected delivery `2026-05-30`
- `bravo-plumbing-solutions`: `in_transit`, cost `0.92`, expected delivery `2026-05-30`
- `browning-electrical-services`: `in_transit`, cost `0.92`, expected delivery `2026-05-30`

## Interpretation

This is not a total Poplar outage. Poplar is accepting and processing most mailings.

The integration bug is that the CRM previously treated Poplar HTTP 200 as successful send truth, even if the returned provider state was already `exception`.

The local code fix in `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-31-poplar-provider-state-integration-fix.md` prevents this class of bug going forward once deployed.

## Recommended Broad Fix

Approve a bounded production fix, not unlimited postcard retries:

1. Deploy the local Poplar provider-state handling fix to the public CRM runtime.
2. Reconcile the three known exception records by adding provider-failure state using existing postcard event type `suppressed`.
3. Keep retries separately named and gated because retries create external provider actions and can spend money.
4. After deploy/reconciliation, run the provider-truth audit again and produce a clean exception list.

## Explicit No-Action Statement

No CRM/Supabase writes, Poplar retries/resubmits, Resend/SMS sends, prospect contact, deploys, Paperclip mutations, git pushes, DNS/domain/hosting/billing changes, or Stripe actions were performed.
