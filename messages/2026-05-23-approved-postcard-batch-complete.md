# Approved Postcard Batch Complete - 2026-05-23

Owner: Codex / Post-Build + Outreach execution  
Approval source: Jesse remote-week bounded postcard execution approval  
Execution window: 2026-05-23T16:55:00Z  

## Scope

Approved first batch only:
- `smartwire-solutions`
- `dream-steam`
- `handy-dandy-atlanta`

Cityboys was explicitly not approved and was not sent.

## Result

All three approved postcards passed the required live gates immediately before
send, were submitted through the public CRM `submit_postcard` action endpoint,
returned `dryRun: false`, created the normal postcard outreach event, and now
read back from CRM as `outreach_sent` with `postcardStatus: submitted`.

## Submitted Postcards

### `smartwire-solutions`

- Business: SmartWire Solutions
- Claim code: `SMAR1182`
- Gate result: PASS
- Preview URL: `200 text/html`, 34,597 bytes
- Checkout URL: `200 text/html`, 78,627 bytes
- Desktop screenshot: `200 image/jpeg`, 341,870 bytes
- Mobile screenshot: `200 image/jpeg`, 155,869 bytes
- Hero image: `200 image/jpeg`, 532,894 bytes
- Payload preview: PASS
- Recipient: Terry Henry, 730 Peachtree St NE, Ste 570, Atlanta, GA 30308
- Current open notes: 0
- Stale open notes ignored under 7-day stale-note policy: 1
- Submit response: `200`, `success: true`, `dryRun: false`
- Poplar order ID: `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`
- CRM event: postcard `submitted` at `2026-05-23T16:55:07.041044+00:00`
- CRM stage after submit: `outreach_sent`
- CRM postcard status after submit: `submitted`
- Provider read-back: Poplar mailing exists, campaign
  `1bef734d-17b0-45fc-a7da-4b13f52e17d4`, created `2026-05-23T16:55:06Z`

### `dream-steam`

- Business: Dream Steam
- Claim code: `ILIM2208`
- Gate result: PASS
- Preview URL: `200 text/html`, 60,336 bytes
- Checkout URL: `200 text/html`, 78,627 bytes
- Desktop screenshot: `200 image/jpeg`, 157,080 bytes
- Mobile screenshot: `200 image/jpeg`, 68,442 bytes
- Hero image: `200 image/jpeg`, 948,238 bytes
- Payload preview: PASS
- Recipient: Reuben, 2250 N Druid Hills Rd Ste 265, Atlanta, GA 30329
- Current open notes: 0
- Stale open notes ignored under 7-day stale-note policy: 3
- Submit response: `200`, `success: true`, `dryRun: false`
- Poplar order ID: `6ea9b53f-9d32-48f4-8cd2-aaefca56a730`
- CRM event: postcard `submitted` at `2026-05-23T16:55:09.01356+00:00`
- CRM stage after submit: `outreach_sent`
- CRM postcard status after submit: `submitted`
- Provider read-back: Poplar mailing exists, campaign
  `1bef734d-17b0-45fc-a7da-4b13f52e17d4`, created `2026-05-23T16:55:08Z`

### `handy-dandy-atlanta`

- Business: Handy Dandy Atlanta
- Claim code: `HBSR0716`
- Gate result: PASS
- Preview URL: `200 text/html`, 51,282 bytes
- Checkout URL: `200 text/html`, 78,627 bytes
- Desktop screenshot: `200 image/jpeg`, 130,199 bytes
- Mobile screenshot: `200 image/jpeg`, 71,680 bytes
- Hero image: `200 image/jpeg`, 933,136 bytes
- Payload preview: PASS
- Recipient: Ruslan, 296 Possum Trot Rd, Barnesville, GA 30204
- Current open notes: 0
- Stale open notes ignored under 7-day stale-note policy: 9
- Submit response: `200`, `success: true`, `dryRun: false`
- Poplar order ID: `f90f45dd-8483-4948-b19b-97968317ee8f`
- CRM event: postcard `submitted` at `2026-05-23T16:55:10.971774+00:00`
- CRM stage after submit: `outreach_sent`
- CRM postcard status after submit: `submitted`
- Provider read-back: Poplar mailing exists, campaign
  `1bef734d-17b0-45fc-a7da-4b13f52e17d4`, created `2026-05-23T16:55:10Z`

## Cityboys Hold Confirmation

`cityboys` was not submitted. Public CRM read-back after the batch:
- Stage: `qa_approved`
- Postcard status: `not_submitted`
- Approved channels: `[]`
- Emails sent: `0`

A separate Cityboys readiness/hold packet was prepared because Jesse recently
saw confusing or wrong postcard imagery.

## Temporary Execution Artifacts

- `/private/tmp/gtmdot-approved-postcard-batch-results.json`
- `/private/tmp/gtmdot-postcard-batch-crm-after.json`

## Explicit No-Action Statement

No Resend/email sends, email sequence resumes, SMS, prospect/customer contact
outside the three approved Poplar postcard submissions, manual CRM/Supabase
truth edits, Paperclip mutations, deploys, DNS/domain/hosting/billing changes,
Stripe actions, or git pushes were performed.
