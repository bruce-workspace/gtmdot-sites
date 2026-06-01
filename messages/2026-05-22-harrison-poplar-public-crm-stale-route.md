# Harrison Poplar Submit Error - Public CRM Stale Route

Generated: 2026-05-23T02:36:27Z

## Summary

Jesse retried the Harrison & Sons Electrical Service postcard submit from the browser and still received the Poplar API 400 error that `first_name` is too long.

The local CRM code has already been patched and verified. The retry is still failing because the public CRM hostname is not serving the patched local handler.

## Evidence

Local patched endpoint:

```txt
POST http://127.0.0.1:3002/api/prospects/d2790267-0458-4007-9ba9-9cab70747710/actions
body: {"action":"preview_postcard_payload"}
```

Returns:

```json
{
  "success": true,
  "payload": {
    "recipient": {
      "first_name": "Harrison & Sons",
      "last_name": "",
      "address_1": "3695 Cascade Rd #6250",
      "city": "Atlanta",
      "state": "GA",
      "postal_code": "30331"
    }
  }
}
```

Public stale endpoint:

```txt
POST https://crm.cloakanddagger.co/api/prospects/d2790267-0458-4007-9ba9-9cab70747710/actions
body: {"action":"preview_postcard_payload"}
```

Returns the old generic action response with `success: true` and `prospect`, not the new read-only `payload` response.

Header comparison:

- Local `127.0.0.1:3002`: no `x-opennext` header.
- Public `crm.cloakanddagger.co`: includes `x-opennext: 1`.

## Current Diagnosis

`crm.cloakanddagger.co` is currently serving an OpenNext/Cloudflare deployment path or stale public runtime, not the patched local Next server that was verified on port `3002`.

This means browser retries against `crm.cloakanddagger.co` will continue using the old Poplar payload code until the public runtime is updated or rerouted.

## Impact

- Harrison postcard submit still fails in the public CRM.
- The local fix is valid: `first_name` is now shortened to `Harrison & Sons`, under Poplar's 20-character limit.
- No successful Harrison postcard submission has been performed by Codex.
- No CRM writes, Poplar sends, deploys, git pushes, DNS changes, or prospect contact were performed by Codex while diagnosing.

## Recommended Next Action

Get explicit Jesse approval to make the public CRM serve the patched code. The least ambiguous next step is a production CRM runtime update for `crm.cloakanddagger.co`, followed by a verification POST to `preview_postcard_payload`.

Do not retry Harrison from the public CRM until the public endpoint returns the patched payload shape.

## Resolution

Resolved: 2026-05-23T02:55:39Z

Codex created a clean temporary worktree from committed CRM state, applied only the Poplar recipient-name fix and read-only `preview_postcard_payload` action, built the OpenNext Cloudflare bundle, and deployed only the CRM Worker runtime.

Deployment:

```txt
Worker: gtmdot-crm-v3
Version ID: a30c184e-3c4d-4853-9fd1-124ec3bda554
Public URL verified: https://crm.cloakanddagger.co
```

Public verification:

```txt
POST https://crm.cloakanddagger.co/api/prospects/d2790267-0458-4007-9ba9-9cab70747710/actions
body: {"action":"preview_postcard_payload"}
```

Returned:

```json
{
  "success": true,
  "payload": {
    "recipient": {
      "first_name": "Harrison & Sons",
      "last_name": "",
      "address_1": "3695 Cascade Rd #6250",
      "city": "Atlanta",
      "state": "GA",
      "postal_code": "30331"
    }
  }
}
```

Actions explicitly not performed:

- No Poplar submit retry.
- No CRM/Supabase data writes.
- No Resend/SMS sends.
- No prospect/customer contact.
- No git push.
- No DNS/domain/hosting/billing changes.
- No Stripe actions.
- No unrelated production site edits.
