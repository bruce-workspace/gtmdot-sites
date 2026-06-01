# Poplar Exceptions And GTM-24 Readiness Follow-Up

Date: 2026-05-17 America/New_York
Lane: Outreach Operations
Mode: read-only follow-up

## Guardrails honored

- No follow-up emails sent.
- No postcards submitted or resubmitted.
- No CRM writes.
- No deploys.
- No Paperclip mutations.
- No prospect/customer contact.
- No git push.

## 1. Poplar exception explanation and next action

### Atlanta Drywall

Prospect slug: `atlanta-drywall-1`
Poplar order: `6deb9d29-ba56-40cd-9027-1ca5dfc9ac10`
Current Poplar state: `exception`
Total cost: `0.00`
Expected delivery date: `null`
Created at: `2026-05-13T01:28:14Z`

Poplar returned address:

- name: `Wilber Tejada Garcia`
- address_1: `6652 RAMGATES WAY NW NORCROSS GA`
- city: `NORCROSS`
- state: `GA`
- postal_code: `30093`

Asset checks:

- `https://gtmdot-postcards.pages.dev/atlanta-drywall-1-hero.jpg` -> `200 image/jpeg`
- `https://gtmdot-postcards.pages.dev/screenshots/atlanta-drywall-1-mobile.jpg` -> `200 image/jpeg`
- `https://gtmdot-postcards.pages.dev/screenshots/atlanta-drywall-1-desktop.jpg` -> `200 image/jpeg`

Explanation:

The Poplar API does not expose the exact exception reason. Based on the returned payload, the most likely issue is mailing-address formatting/normalization, not postcard assets. The CRM prospect `address` field contains `6652 Ramgates Way NW, Norcross GA 30093` while separate `city/state/zip` fields also exist. The submit path constructs `fullAddress = address + city/state/zip`, so this can duplicate city/state/zip and produce an `address_1` containing `NORCROSS GA` instead of a clean street line.

Recommended next action:

Do not resubmit automatically. First, fix/confirm the mailing fields so street address is only `6652 Ramgates Way NW`, with `city=Norcross`, `state=GA`, `zip=30093`. Then run a dry-run Poplar payload check and, only with separate Jesse approval, resubmit or create a replacement postcard order. If available, also inspect Poplar UI/support for the provider's exact exception reason before resubmission.

### Perez Pools LLC

Prospect slug: `perez-pools-llc`
Poplar order: `7158568c-2f52-4a2d-84ce-b5e7783715e1`
Current Poplar state: `exception`
Total cost: `0.00`
Expected delivery date: `null`
Created at: `2026-05-13T01:41:07Z`

Poplar returned address:

- name: `Chris Perez`
- address_1: `900 RIVERBEND CLUB DR SE`
- city: `ATLANTA`
- state: `GA`
- postal_code: `30339`

Asset checks:

- `https://gtmdot-postcards.pages.dev/perez-pools-llc-hero.jpg` -> `200 image/jpeg`
- `https://gtmdot-postcards.pages.dev/screenshots/perez-pools-llc-mobile.jpg` -> `200 image/jpeg`
- `https://gtmdot-postcards.pages.dev/screenshots/perez-pools-llc-desktop.jpg` -> `200 image/jpeg`

Explanation:

The Poplar API does not expose the exact exception reason. The returned address is cleaner than Atlanta Drywall and all referenced assets resolve with `200 image/jpeg`, so this does not look like an asset failure from the evidence available. The likely remaining causes are provider-side address deliverability/normalization, an address/recipient issue not exposed by the API, or a Poplar-side exception that must be viewed in Poplar UI/support.

Recommended next action:

Do not resubmit automatically. Verify the mailing address deliverability for `900 Riverbend Club Dr SE, Atlanta, GA 30339`, including whether a suite/unit/recipient detail is required. Check Poplar UI/support for the exact exception reason. After the address/reason is confirmed, resubmit only with separate Jesse approval.

## 2. Do the 11 in-transit postcards need action before May 19, 2026?

No immediate action is needed before May 19, 2026.

Read-only Poplar refresh on 2026-05-17 confirmed all 11 non-exception orders remain `in_transit`, each with expected delivery `2026-05-19` and cost `0.92`:

| Slug | Poplar order | State | Expected delivery | Cost |
|---|---|---|---|---|
| `atlanta-pro-repairs` | `1cffb204-fa41-4b99-a881-bd005c58b1b3` | `in_transit` | `2026-05-19` | `0.92` |
| `tech-on-the-way` | `7e387657-ba5a-4749-935a-e674375f6494` | `in_transit` | `2026-05-19` | `0.92` |
| `atl-mobile-mechanics` | `c8095580-36c4-44c7-91d2-0c39a0abef86` | `in_transit` | `2026-05-19` | `0.92` |
| `affordable-concrete-repair` | `fb2b082b-231f-49ec-b759-fe9215014f56` | `in_transit` | `2026-05-19` | `0.92` |
| `locksmith-atlanta-pro` | `9b251df0-4acd-4642-ba91-4ad11e86ae2e` | `in_transit` | `2026-05-19` | `0.92` |
| `golden-choice-prowash` | `2b1676aa-86e8-4c5b-b0c3-a6bfea69e3d5` | `in_transit` | `2026-05-19` | `0.92` |
| `morales-landscape-construction` | `b54954c9-c541-478e-981f-09771b5f150f` | `in_transit` | `2026-05-19` | `0.92` |
| `roberts-mobile-services` | `ebbb659d-027b-45e1-9a97-7eb258537068` | `in_transit` | `2026-05-19` | `0.92` |
| `done-right-drywall` | `e2e88b75-574e-4e1f-a8af-54505ba37f03` | `in_transit` | `2026-05-19` | `0.92` |
| `membrenos-pro-home-repair` | `3cace5b9-37ab-478b-89b6-da2c2b846c7e` | `in_transit` | `2026-05-19` | `0.92` |
| `moonstone-pressure-washing` | `c89c2b26-0067-4156-8710-bcda0d836a01` | `in_transit` | `2026-05-19` | `0.92` |

Recommended next action:

Monitor only. Do not resubmit or intervene before May 19. On or after May 19, run a read-only status refresh for delivered/returned/failed state and then decide whether CRM backfill/reconciliation is needed. CRM still likely shows only `submitted` unless webhook/reconciliation has been fixed or approved.

## 3. Remaining steps before Email 2 follow-ups can safely resume

Email 2 follow-ups should not resume at scale yet.

Exact remaining steps/approval needed:

1. Deploy approval for GTM-24 Phase 1 if Jesse wants the reply-to fix live. Phase 1 is complete locally, but no deploy was approved or performed.
2. Re-run static guard before deploy: `npm run check:gtmdot-outreach-reply-to`.
3. Deploy only with separate approval.
4. Verify the deployed send helper uses `replyTo: hello@gtmdot.com`; do this with a non-sending/static or internal-only method, not a prospect send.
5. Decide the reply-monitoring risk posture:
   - safest path: wait until reply monitoring is proven end-to-end before resuming scaled follow-ups;
   - manual-risk path: Jesse explicitly accepts manual monitoring risk, and someone checks `hello@gtmdot.com`/mailbox state before each follow-up batch.
6. Keep Morales suppressed/paused because the email hard-bounced permanently.
7. For the paused Email 2 cohort from GTM-7, Jesse must explicitly approve resume/send per prospect or as a named batch. The paused cohort was Atlanta Pro Repairs, Golden Choice Pro Wash, Locksmith Atlanta Pro, Membreno's Pro Home Repair, and Moonstone Pressure Washing.
8. Do not send Email 3 early for Perez Pools LLC or Tech On The Way. Those had Email 2 already sent/delivered and Email 3 was scheduled for May 20, 2026 in GTM-7 evidence.
9. Do not create a false all-clear from postcard status: postcard delivery is still pending until May 19, and two postcard exceptions need separate resolution.

Recommended next action:

Ask Jesse for one of two explicit decisions before any follow-up resumes:

- `Deploy GTM-24 Phase 1 reply-to fix only` and keep follow-ups paused; or
- `Accept manual reply-monitoring risk for a named Email 2 batch` after deployment/static verification and mailbox check.

Absent that approval, keep follow-ups paused and continue read-only monitoring/artifact work.
