# Poplar Provider-State Production Fix Complete

Date: 2026-06-01
Owner: Codex
Mode: approved production fix + approved exception reconciliation

## Completed

Deployed the local Poplar provider-state fix to the public CRM runtime.

- Worker: `gtmdot-crm-v3`
- Version ID: `2baeeb71-cc9b-4176-8495-117a7acb9097`
- Public Worker URL: `https://gtmdot-crm-v3.jesse-ef7.workers.dev`
- Public CRM domain: `https://crm.cloakanddagger.co`

The deployed CRM now treats Poplar provider failure states as failures instead of successful postcard submits.

Provider failure states handled:

- `exception`
- `failed`
- `failure`
- `error`
- `invalid`
- `validation_failed`
- `suppressed`
- `cancelled`
- `canceled`

## Reconciled Known Exceptions

Added a postcard `suppressed` outreach event and matching activity entry for each known Poplar exception record.

| Slug | Business | Poplar Order | Reconciliation Event |
|---|---|---|---|
| `24-hrs-mobile-tire-services` | 24 hrs Mobile Tire Services | `8b46f6b0-07a9-4242-851e-7fd3d488ff72` | `55cf9ac4-5c0a-41b9-ac74-e3f27330926b` |
| `atlanta-drywall-1` | Atlanta Drywall | `6deb9d29-ba56-40cd-9027-1ca5dfc9ac10` | `997f3b64-97cb-478f-bd12-ad28b9de9aef` |
| `perez-pools-llc` | Perez Pools LLC | `7158568c-2f52-4a2d-84ce-b5e7783715e1` | `340feeef-bab9-4964-92df-a1f1a207bb94` |

## Post-Reconciliation Audit

After reconciliation, public CRM now derives these three as `postcardStatus: suppressed`, not `submitted`.

| Slug | CRM Postcard Status | Poplar State | Cost | Expected Delivery |
|---|---|---|---|---|
| `24-hrs-mobile-tire-services` | `suppressed` | `exception` | `0.00` | `null` |
| `atlanta-drywall-1` | `suppressed` | `exception` | `0.00` | `null` |
| `perez-pools-llc` | `suppressed` | `exception` | `0.00` | `null` |

Total Poplar orders audited: `24`

Known exception records after reconciliation: `3`, all now correctly marked `suppressed` in CRM.

## Retry Readiness Notes

Read-only payload previews and asset checks were run for the three exception records. No Poplar retry was performed.

### 24 Hrs Mobile Tire Services

- Payload preview: `200`
- Recipient first_name: `24 hrs Mobile Tire`
- Address payload appears clean:
  - `396 Piedmont Ave NE`
  - `Atlanta, GA 30308`
- Hero, desktop screenshot, mobile screenshot, and preview URL all return `200`.
- Next likely step: retry candidate after Jesse approval, unless Poplar UI/support reveals a hidden deliverability issue.

### Atlanta Drywall

- Payload preview: `200`
- Recipient first_name: `Wilber`
- Address payload likely still problematic because `address_1` includes duplicated city/state/ZIP:
  - `6652 Ramgates Way NW, Norcross GA 30093`
  - city/state/ZIP also separately sent as `Norcross, GA 30093`
- Hero, desktop screenshot, mobile screenshot, and preview URL all return `200`.
- Next likely step: clean CRM street address to `6652 Ramgates Way NW` before any retry.

### Perez Pools LLC

- Payload preview: `200`
- Recipient first_name: `Chris`
- Address payload may also be problematic because `address_1` includes city/state/ZIP:
  - `900 Riverbend Club Dr SE, Atlanta, GA 30339`
  - city/state/ZIP also separately sent as `Atlanta, GA 30339`
- Hero, desktop screenshot, mobile screenshot, and preview URL all return `200`.
- Next likely step: clean CRM street address to `900 Riverbend Club Dr SE` before any retry.

## Verification

- `npm run build` passed.
- `opennextjs-cloudflare build` passed.
- `wrangler deploy` succeeded.
- Public CRM provider-truth audit rerun after reconciliation.
- Read-only payload previews passed for all three exception records.
- Read-only asset checks returned `200` for hero, desktop screenshot, mobile screenshot, and preview URLs for all three exception records.

## Explicit No-Action Statement

No Poplar retry/resubmit, Resend/SMS send, prospect/customer contact, Paperclip mutation, git push, DNS/domain/hosting/billing change, Stripe action, or unrelated production edit was performed.
