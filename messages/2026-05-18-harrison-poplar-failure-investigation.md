---
from: codex-outreach-operations
to: jesse / gtmdot-quarterback / outreach-operations
date: 2026-05-18T06:43:10-04:00
type: no-send-poplar-failure-investigation
prospect: harrison-sons-electrical
subject: Harrison & Sons Electrical postcard submit failure investigation and corrected payload recommendation
---

# Harrison & Sons Electrical - Poplar Failure Investigation

Mode: read-only investigation only. Do not retry without fresh Jesse approval.

## Guardrails honored

- No Poplar submit retry.
- No CRM writes.
- No note deletion.
- No deploys.
- No prospect/customer contact.
- No email/SMS.
- No git push.

## Current verified CRM state after failed attempt

Source: local CRM detail API, read-only pull at 2026-05-18T06:43 ET.

- Prospect ID: `d2790267-0458-4007-9ba9-9cab70747710`
- Business: `Harrison & Sons Electrical Service LLC`
- Slug: `harrison-sons-electrical`
- Stage: `outreach_staged`
- Postcard status: `not_submitted`
- Outreach events: none
- Email: none
- Approved channel: `postcard`
- Claim code: `HARR2423`
- Preview URL: `https://harrison-sons-electrical.pages.dev`
- CRM address fields:
  - address: `3695 Cascade Rd #6250`
  - city: `Atlanta`
  - state: `GA`
  - zip: `30331`

Conclusion: the failed CRM attempt did not create a CRM postcard submitted event, did not move the prospect to `outreach_sent`, and did not change CRM postcard state.

## Poplar provider check

Read-only provider checks performed:

1. `GET https://api.heypoplar.com/v1/mailing?limit=25`
   - Result: `405 MethodNotAllowed`; endpoint allows `OPTIONS, POST`, not list GET.
2. `GET https://api.heypoplar.com/v1/campaign/{POPLAR_CAMPAIGN_ID}/mailings`
   - Result: `200`; campaign contains 37 mailings over 8 pages.
3. Searched all 8 campaign mailing pages for any match on:
   - claim code `HARR2423`
   - preview URL containing `harrison-sons-electrical`
   - address containing `CASCADE`
   - address line 2 containing `6250`
   - Harrison business name plus `30331`

Result: no matching Poplar mailing found.

Conclusion: available read-only Poplar evidence shows no Harrison mailing was created in the campaign despite the failed CRM submit attempt.

## Exact error status/body

Not captured from available local evidence.

What I checked:

- `brucecom-v3/.next/dev/logs/next-development.log`: no Poplar error body/status present.
- Current Codex app terminal for this thread: no attached app terminal session.
- CRM state: no saved failed-attempt record and no outreach event metadata.

The active route would return errors as:

```text
Postcard failed: Poplar API error: <status> <body>
```

But the exact `<status> <body>` is only available from the browser toast/network response or the terminal/session that handled the failed click. It is not persisted in CRM today.

CRM v2/ops recommendation: failed send attempts should be logged separately from successful outreach events, including provider status code, body, payload fingerprint, and timestamp. A failed submit should not create `postcard/submitted`, but it should leave an audit trail.

## Payload that current CRM helper would send

Source: `brucecom-v3/src/app/api/prospects/[id]/actions/route.ts` and `brucecom-v3/src/lib/poplar.ts`.

Current helper payload shape:

```json
{
  "campaign_id": "1bef734d-17b0-45fc-a7da-4b13f52e17d4",
  "recipient": {
    "first_name": "Harrison & Sons Electrical Service LLC",
    "last_name": "",
    "address_1": "3695 Cascade Rd #6250",
    "city": "Atlanta",
    "state": "GA",
    "postal_code": "30331"
  },
  "merge_tags": {
    "business_name": "Harrison & Sons Electrical Service LLC",
    "claim_code": "HARR2423",
    "preview_site_url": "https://harrison-sons-electrical.pages.dev?utm_source=postcard&utm_medium=direct_mail&utm_campaign=gtmdot",
    "hostname": "harrison-sons-electrical.pages.dev",
    "desktop_screenshot_url": "https://gtmdot-postcards.pages.dev/screenshots/harrison-sons-electrical-desktop.jpg",
    "mobile_screenshot_url": "https://gtmdot-postcards.pages.dev/screenshots/harrison-sons-electrical-mobile.jpg",
    "hero_image_url": "https://gtmdot-postcards.pages.dev/harrison-sons-electrical-hero.jpg"
  }
}
```

Dry helper verification before the submit attempt showed:

- Missing merge fields: none.
- Hero image URL: `200`.
- Desktop screenshot URL: `200`.
- Mobile screenshot URL: `200`.

## Asset / QR / claim-code verification

Live checks performed during final preflight:

- Live site: `https://harrison-sons-electrical.pages.dev/` returned `200 text/html`, 60,919 bytes.
- Lookup: `https://gtmdot.com/api/lookup-code?code=HARR2423` returned `found:true`, slug `harrison-sons-electrical`, URL `https://harrison-sons-electrical.pages.dev`.
- Live site hero: `https://harrison-sons-electrical.pages.dev/photos/hero.jpg` returned `200 image/jpeg`, 1,156,010 bytes.
- Postcard hero: `https://gtmdot-postcards.pages.dev/harrison-sons-electrical-hero.jpg` returned `200 image/jpeg`, 1,156,010 bytes, 3360 x 1872.
- Desktop screenshot: `https://gtmdot-postcards.pages.dev/screenshots/harrison-sons-electrical-desktop.jpg` returned `200 image/jpeg`, 457,286 bytes, 2880 x 1800.
- Mobile screenshot: `https://gtmdot-postcards.pages.dev/screenshots/harrison-sons-electrical-mobile.jpg` returned `200 image/jpeg`, 178,998 bytes, 780 x 1688.
- Live HTML includes `HARR2423`, shared claim popup, shared claim bar, `$49`, `$149`, and checkout links to `https://gtmdot.com/checkout?code=HARR2423`.
- Poplar back template QR source is `{{custom.preview_site_url}}`; under the current helper the QR target should be:
  `https://harrison-sons-electrical.pages.dev?utm_source=postcard&utm_medium=direct_mail&utm_campaign=gtmdot`.

## Likely failure area

Most likely: recipient address validation/normalization.

Evidence:

- CRM payload currently sends `address_1: 3695 Cascade Rd #6250`.
- Current live site/schema/footer render the address as `3695 Cascade Rd STE 6250`.
- Poplar may reject or fail validation on `#6250`, or may prefer suite/unit data as `address_2`.

Other possible causes:

- Provider-side validation error collapsed by CRM UI into a generic error.
- Payload contract difference: current helper sends `merge_tags`; Poplar template docs refer to `custom.*` tags. However, existing successful campaign mailings also show `merge_tags`, so this is less likely than address validation.
- Credential/campaign ID issue is unlikely because existing campaign mailings are present and prior postcards submitted through the same path.

## Recommended corrected payload

Preferred corrected provider payload if helper supports `address_2`:

```json
{
  "campaign_id": "1bef734d-17b0-45fc-a7da-4b13f52e17d4",
  "recipient": {
    "first_name": "Harrison & Sons Electrical Service LLC",
    "last_name": "",
    "address_1": "3695 Cascade Rd",
    "address_2": "Ste 6250",
    "city": "Atlanta",
    "state": "GA",
    "postal_code": "30331"
  },
  "merge_tags": {
    "business_name": "Harrison & Sons Electrical Service LLC",
    "claim_code": "HARR2423",
    "preview_site_url": "https://harrison-sons-electrical.pages.dev?utm_source=postcard&utm_medium=direct_mail&utm_campaign=gtmdot",
    "hostname": "harrison-sons-electrical.pages.dev",
    "desktop_screenshot_url": "https://gtmdot-postcards.pages.dev/screenshots/harrison-sons-electrical-desktop.jpg",
    "mobile_screenshot_url": "https://gtmdot-postcards.pages.dev/screenshots/harrison-sons-electrical-mobile.jpg",
    "hero_image_url": "https://gtmdot-postcards.pages.dev/harrison-sons-electrical-hero.jpg"
  }
}
```

Fallback if the current helper cannot send `address_2` without code changes:

```json
{
  "recipient": {
    "first_name": "Harrison & Sons Electrical Service LLC",
    "last_name": "",
    "address_1": "3695 Cascade Rd Ste 6250",
    "city": "Atlanta",
    "state": "GA",
    "postal_code": "30331"
  }
}
```

Do not apply either correction to CRM or code without separate approval.

## Remaining blocker

The exact Poplar API error body/status is still missing. The safest next action is to capture it from the browser network response or the terminal that handled the failed CRM click before any retry.

Operational blocker for submit: yes, until one of these is true:

1. Exact provider error confirms a non-address cause and the corrected fix is known; or
2. Jesse explicitly approves retry using the normalized `Ste 6250` payload despite the missing captured error body.

## Explicit approval text Jesse must provide if ready to retry

Use this only after deciding the corrected payload is acceptable:

```text
I approve a single Harrison & Sons Electrical Poplar postcard resubmit attempt using the normalized suite address payload: 3695 Cascade Rd Ste 6250, Atlanta, GA 30331. Do not send email/SMS. If Poplar returns an error, stop and capture the exact provider status/body before any further retry.
```
