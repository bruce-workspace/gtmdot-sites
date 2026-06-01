# GTM-8 Poplar Postcard Progression Artifact

Date: 2026-05-16 America/New_York
UTC evidence pull: 2026-05-17T00:59Z-2026-05-17T01:17Z
Lane: Outreach Operations
Paperclip: GTM-8 — Verify Poplar postcard progression after submit
Mode: read-only provider/CRM inspection and recommendation only

## Guardrails

Performed:
- Read-only local code inspection for Poplar status ownership.
- Read-only CRM/Supabase outreach_events review from prior GTM-7 dataset.
- Read-only Poplar API lookups with `GET https://api.heypoplar.com/v1/mailing/{orderId}`.
- File-ledger artifact write.

Explicitly not performed:
- No CRM writes.
- No Paperclip writes.
- No Poplar submissions.
- No Poplar status backfills.
- No Resend/email sends.
- No SMS sends.
- No prospect/customer contact.
- No deploys, production edits, or git pushes.

## Evidence Sources

- CRM `outreach_events`: all 13 records have `channel=postcard`, `event_type=submitted`, and `metadata.orderId`.
- Poplar provider API: `GET /v1/mailing/{orderId}` for all 13 order IDs.
- Local status code owner:
  - `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/webhooks/poplar/route.ts`
  - `/Users/bruce/.openclaw/workspace/gtmdot/scripts/check-poplar-status.js`

Provider detail note: Poplar's main mailing endpoint returned `state`, `expected_delivery_date`, `total_cost`, and `created_at`. Probed `/events` and `/status` subpaths returned 404, so this artifact does not claim detailed transition history beyond the current provider state.

## Rollup

- Total submitted postcard orders checked: 13.
- CRM current postcard state for all 13: `submitted` only.
- Poplar provider `state=in_transit`: 11.
- Poplar provider `state=exception`: 2.
- Poplar provider delivered: 0.
- Poplar provider returned: 0.
- Poplar provider suppressed/cancelled: 0.
- Expected delivery date for all `in_transit` orders: 2026-05-19.
- Cost on `in_transit` orders: 0.92 each.
- Cost on `exception` orders: 0.00 each.

## State Mapping Used

| Poplar provider state | GTM-8 normalized state | Rationale |
|---|---|---|
| `in_transit` | `mailed / in_transit` | Provider indicates postcard has moved beyond submit and is expected to deliver. It is not yet delivered. |
| `exception` | `failed / exception` | Provider indicates order did not enter normal paid transit; cost is 0.00 and no expected delivery date was returned. Exact exception reason was not present in the API payload. |
| no provider state | `unknown` | Not encountered in this GTM-8 pull. |

## Per-Order Status

| Prospect | Slug | CRM stage | Poplar order ID | CRM postcard state | Poplar provider state | Normalized current postcard state | Evidence source | Exact next action |
|---|---|---|---|---|---|---|---|---|
| Atlanta Drywall | `atlanta-drywall-1` | `outreach_sent` | `6deb9d29-ba56-40cd-9027-1ca5dfc9ac10` | `submitted` only | `exception`; cost `0.00`; no expected delivery date | `failed / exception` | CRM submitted event 2026-05-13T01:28:14Z; Poplar GET `/v1/mailing/6deb9d29-ba56-40cd-9027-1ca5dfc9ac10` | Do not resend automatically. Investigate Poplar exception reason/address/template in Poplar UI or support; decide whether to fix and resubmit with Jesse approval. |
| Atlanta Pro Repairs | `atlanta-pro-repairs` | `outreach_sent` | `1cffb204-fa41-4b99-a881-bd005c58b1b3` | `submitted` only | `in_transit`; expected delivery `2026-05-19`; cost `0.92` | `mailed / in_transit` | CRM submitted event 2026-05-13T01:29:12Z; Poplar GET `/v1/mailing/1cffb204-fa41-4b99-a881-bd005c58b1b3` | Monitor for delivery/return. CRM needs approved backfill or webhook/polling path to reflect provider state. |
| Tech On The Way | `tech-on-the-way` | `outreach_sent` | `7e387657-ba5a-4749-935a-e674375f6494` | `submitted` only | `in_transit`; expected delivery `2026-05-19`; cost `0.92` | `mailed / in_transit` | CRM submitted event 2026-05-13T01:31:08Z; Poplar GET `/v1/mailing/7e387657-ba5a-4749-935a-e674375f6494` | Monitor for delivery/return. CRM needs approved backfill or webhook/polling path to reflect provider state. |
| Perez Pools LLC | `perez-pools-llc` | `outreach_sent` | `7158568c-2f52-4a2d-84ce-b5e7783715e1` | `submitted` only | `exception`; cost `0.00`; no expected delivery date | `failed / exception` | CRM submitted event 2026-05-13T01:41:07Z; Poplar GET `/v1/mailing/7158568c-2f52-4a2d-84ce-b5e7783715e1` | Do not resend automatically. Investigate Poplar exception reason/address/template in Poplar UI or support; decide whether to fix and resubmit with Jesse approval. |
| Atl Mobile Mechanics | `atl-mobile-mechanics` | `outreach_sent` | `c8095580-36c4-44c7-91d2-0c39a0abef86` | `submitted` only | `in_transit`; expected delivery `2026-05-19`; cost `0.92` | `mailed / in_transit` | CRM submitted event 2026-05-13T01:43:36Z; Poplar GET `/v1/mailing/c8095580-36c4-44c7-91d2-0c39a0abef86` | Monitor for delivery/return. Keep separate Jesse decision on duplicate/business-quality issue. |
| Affordable Concrete & Repair | `affordable-concrete-repair` | `outreach_sent` | `fb2b082b-231f-49ec-b759-fe9215014f56` | `submitted` only | `in_transit`; expected delivery `2026-05-19`; cost `0.92` | `mailed / in_transit` | CRM submitted event 2026-05-13T01:43:59Z; Poplar GET `/v1/mailing/fb2b082b-231f-49ec-b759-fe9215014f56` | Monitor for delivery/return. Keep separate Jesse decision on whether Email 1 should send or remain held for photos. |
| Locksmith Atlanta Pro | `locksmith-atlanta-pro` | `outreach_sent` | `9b251df0-4acd-4642-ba91-4ad11e86ae2e` | `submitted` only | `in_transit`; expected delivery `2026-05-19`; cost `0.92` | `mailed / in_transit` | CRM submitted event 2026-05-13T01:45:26Z; Poplar GET `/v1/mailing/9b251df0-4acd-4642-ba91-4ad11e86ae2e` | Monitor for delivery/return. CRM needs approved backfill or webhook/polling path to reflect provider state. |
| Golden Choice Pro Wash | `golden-choice-prowash` | `outreach_sent` | `2b1676aa-86e8-4c5b-b0c3-a6bfea69e3d5` | `submitted` only | `in_transit`; expected delivery `2026-05-19`; cost `0.92` | `mailed / in_transit` | CRM submitted event 2026-05-13T02:04:06Z; Poplar GET `/v1/mailing/2b1676aa-86e8-4c5b-b0c3-a6bfea69e3d5` | Monitor for delivery/return. Keep Email 2 paused until Jesse approval. |
| Morales Landscape & Construction | `morales-landscape-construction` | `outreach_sent` | `b54954c9-c541-478e-981f-09771b5f150f` | `submitted` only | `in_transit`; expected delivery `2026-05-19`; cost `0.92` | `mailed / in_transit` | CRM submitted event 2026-05-13T02:05:40Z; Poplar GET `/v1/mailing/b54954c9-c541-478e-981f-09771b5f150f` | Monitor postcard delivery/return. Keep email suppressed/paused separately due Resend hard bounce. |
| Roberts Mobile Services | `roberts-mobile-services` | `outreach_sent` | `ebbb659d-027b-45e1-9a97-7eb258537068` | `submitted` only | `in_transit`; expected delivery `2026-05-19`; cost `0.92` | `mailed / in_transit` | CRM submitted event 2026-05-13T02:06:33Z; Poplar GET `/v1/mailing/ebbb659d-027b-45e1-9a97-7eb258537068` | Monitor for delivery/return. CRM needs approved backfill or webhook/polling path to reflect provider state. |
| Done Right Drywall | `done-right-drywall` | `outreach_sent` | `e2e88b75-574e-4e1f-a8af-54505ba37f03` | `submitted` only | `in_transit`; expected delivery `2026-05-19`; cost `0.92` | `mailed / in_transit` | CRM submitted event 2026-05-13T02:06:59Z; Poplar GET `/v1/mailing/e2e88b75-574e-4e1f-a8af-54505ba37f03` | Monitor for delivery/return. CRM needs approved backfill or webhook/polling path to reflect provider state. |
| Membreno's Pro Home Repair | `membrenos-pro-home-repair` | `outreach_sent` | `3cace5b9-37ab-478b-89b6-da2c2b846c7e` | `submitted` only | `in_transit`; expected delivery `2026-05-19`; cost `0.92` | `mailed / in_transit` | CRM submitted event 2026-05-13T02:12:13Z; Poplar GET `/v1/mailing/3cace5b9-37ab-478b-89b6-da2c2b846c7e` | Monitor for delivery/return. Keep Email 2 paused until Jesse approval. |
| Moonstone Pressure Washing | `moonstone-pressure-washing` | `outreach_sent` | `c89c2b26-0067-4156-8710-bcda0d836a01` | `submitted` only | `in_transit`; expected delivery `2026-05-19`; cost `0.92` | `mailed / in_transit` | CRM submitted event 2026-05-13T02:13:56Z; Poplar GET `/v1/mailing/c89c2b26-0067-4156-8710-bcda0d836a01` | Monitor for delivery/return. Keep Email 2 paused until Jesse approval. |

## Findings

1. CRM is stale for postcards. It shows all 13 as `submitted`, while Poplar now shows 11 in transit and 2 exceptions.

2. Poplar progression is happening, but CRM is not receiving or recording provider status progression. No `postcard/mailed`, `postcard/delivered`, `postcard/returned`, or `postcard/suppressed` events were found in CRM for these orders.

3. The current webhook maps `mailing.mailed`, `mailing.delivered`, `mailing.returned`, and `mailing.suppressed`, but no such events appear in CRM. Either Poplar webhook is not configured/firing, the provider uses `in_transit` rather than mapped event names, or webhook delivery is not reaching the app.

4. The legacy checker `/Users/bruce/.openclaw/workspace/gtmdot/scripts/check-poplar-status.js` polls Poplar but writes `gtmdot/poplar-sends.json`, not CRM `outreach_events`. It is not sufficient for current CRM channel truth.

5. Atlanta Drywall and Perez Pools LLC are not merely pending; provider state is `exception`. They need exception investigation before any resend or status backfill.

## Recommendations

1. Treat 11 orders as `mailed / in_transit` operationally, expected delivery 2026-05-19, but do not write CRM without explicit approval.

2. Treat Atlanta Drywall and Perez Pools LLC as `failed / exception` operationally. Do not resend automatically. Investigate in Poplar UI/support for exact exception reason.

3. Create an approved dry-run-first CRM reconciliation script that reads Poplar order IDs from `outreach_events`, fetches provider state, maps states, and proposes CRM `outreach_events` backfills without writing unless Jesse approves.

4. Update Poplar webhook mapping to include provider `in_transit` if Poplar sends that state by webhook. Current mapper does not explicitly map `in_transit`.

5. Proceed next to GTM-9: verify GTMDot email/reply watcher. GTM-8 confirms postcard provider state; reply state remains unproven.
