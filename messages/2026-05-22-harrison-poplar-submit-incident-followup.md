---
from: codex-quarterback
to: jesse / outreach-operations / post-build-operations
date: 2026-05-22T06:47:58-04:00
type: poplar-submit-incident-followup
prospect: harrison-sons-electrical
paperclip: GTM-12
subject: Harrison & Sons Poplar submit failure remediated locally, no send performed
---

# Harrison & Sons Poplar Submit Incident Follow-Up

Mode: local code remediation and verification only.

## Why this exists

Jesse retried the Harrison & Sons Electrical postcard from the CRM and still hit the
Poplar API 400 failure where `first_name` cannot exceed 20 characters. This was a
recurring board-clearing blocker and needed to become an incident artifact rather
than another loose note.

## Findings

- The active CRM server is local `brucecom-v3` on port `3002`.
- Harrison detail API still shows no postcard events and `postcardStatus:
  "not_submitted"`.
- The prospect list API previously showed Harrison as `submitted` because
  `approvedFor: ["postcard"]` was treated as provider proof. That was wrong.
- The corrected live local preview payload now produces:

```json
{
  "recipient": {
    "first_name": "Harrison & Sons",
    "last_name": "",
    "address_1": "3695 Cascade Rd #6250",
    "city": "Atlanta",
    "state": "GA",
    "postal_code": "30331"
  }
}
```

`Harrison & Sons` is 15 characters, so the Poplar 20-character first-name rule is
satisfied from this code path.

## Local code changes

Updated in both CRM code trees:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/prospects/route.ts`
- `/Users/bruce/.openclaw/workspace/gtmdot-crm/src/app/api/prospects/route.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/prospects/[id]/actions/route.ts`
- `/Users/bruce/.openclaw/workspace/gtmdot-crm/src/app/api/prospects/[id]/actions/route.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/lib/poplar.ts`
- `/Users/bruce/.openclaw/workspace/gtmdot-crm/src/lib/poplar.ts`

Changes:

- Fixed postcard list status: `approvedFor: ["postcard"]` no longer displays as
  `submitted` without a real postcard outreach/provider event.
- Added reusable Poplar payload builder with a hard guard that prevents
  `recipient.first_name` longer than 20 characters.
- Added safe `last_name` truncation.
- Added a read-only `preview_postcard_payload` action for no-send payload
  verification before a Poplar attempt.
- Added sanitized Poplar error logging on failed provider responses.

## Verification

- `npm run build` passed for `brucecom-v3`.
- Existing Turbopack warning remains about `next.config.ts` / `src/lib/vault.ts`;
  this is pre-existing and unrelated to the Poplar fix.
- Local CRM server was restarted and is listening on port `3002`.
- Read-only payload preview call returned `first_name: "Harrison & Sons"`.
- Read-only list API now reports Harrison as `postcardStatus: "not_submitted"`,
  matching the detail API.

## Still not performed

- No Poplar submit retry.
- No CRM/Supabase data writes.
- No Paperclip mutation.
- No deploy.
- No email/SMS send.
- No prospect/customer contact.
- No git push.
- No DNS/domain/hosting/billing/Stripe action.

## Recommended next action

If Jesse wants to retry from the CRM, refresh the CRM page first so the browser is
using the restarted server and current bundle. If Poplar still rejects the
request, stop and capture the exact API body now that the server logs sanitized
provider status/body/recipient details.

If this is promoted into Paperclip, attach this artifact to `GTM-12` and mark the
remaining Harrison blocker as: `awaiting one Jesse-approved retry / provider
response capture`.
