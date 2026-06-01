# Next Needs-Approval Review + Batch Proposal - 2026-05-23

Owner: Codex / Post-Build + Outreach  
Mode: remote-week board clearing  
Status: corrected review packet only, no sends  
Generated: 2026-05-23T13:42:00-04:00  

## Scope

Jesse approved continued bounded autonomy, but `needs_approval` prospects require
a Jesse-review packet first and may not be sent until Jesse gives mobile
approval for the named prospect or named batch.

This corrected artifact applies the current live gates and the 7-day stale-note
policy. Old notes were not allowed to block by default, but concrete old claims
were rechecked against current live HTML/assets before classification.

No postcard sends, email sends, SMS, CRM truth edits, Paperclip mutations,
deploys, prospect/customer contact, DNS/domain/hosting/billing changes, Stripe
actions, or git pushes were performed while preparing this packet.

## Current State

- Additional `qa_approved` sendable prospects: none.
- `cityboys` remains technically ready but explicitly held for visual QA.
- `piedmont-tires` remains blocked by `preview_postcard_payload` 400 because ZIP
  is missing.
- Six `needs_approval` prospects pass the mechanical postcard payload/asset
  gates.
- One `needs_approval` prospect, `rooter-pro-plumbing-drain`, fails the hero
  print-spec gate and should not be included in a send batch.

## Corrected Review Queue

Cleanest candidates for Jesse mobile review:

1. `24-hrs-mobile-tire-services`
2. `bravo-plumbing-solutions`
3. `browning-electrical-services`

Secondary candidates needing explicit visual/content override before any send:

1. `chrissy-s-mobile-detailing`
2. `thermys-mobile-tire-and-brakes`
3. `tuxedo-mechanical-plumbing`

Blocked:

1. `rooter-pro-plumbing-drain`
2. `cityboys`
3. `piedmont-tires`

## Review Packets

### `24-hrs-mobile-tire-services`

- Business: 24 hrs Mobile Tire Services
- Stage: `needs_approval`
- Email on file: none
- Postcard status: `not_submitted`
- Claim code: `HMTS3276`
- Preview URL: `https://24-hrs-mobile-tire-services.pages.dev`
- Recipient: `24 hrs Mobile Tire`, `396 Piedmont Ave NE`, Atlanta GA `30308`
- Payload preview: 200 / valid
- Desktop screenshot: `image/jpeg`, 351167 bytes
- Mobile screenshot: `image/jpeg`, 178698 bytes
- Hero image: `image/jpeg`, 667699 bytes
- Current recheck: old H1 spacing note is no longer visible; current HTML has 6
  `<img>` tags and the claim code is present.
- Recommendation: review-ready for postcard-only approval.

### `bravo-plumbing-solutions`

- Business: Bravo Plumbing Solutions
- Stage: `needs_approval`
- Email on file: none
- Postcard status: `not_submitted`
- Claim code: `BPST1027`
- Preview URL: `https://bravo-plumbing-solutions.pages.dev`
- Recipient: `Forrell Hillery`, `105 Bond Dr`, Ellenwood GA `30294`
- Payload preview: 200 / valid
- Desktop screenshot: `image/jpeg`, 207432 bytes
- Mobile screenshot: `image/jpeg`, 109657 bytes
- Hero image: `image/jpeg`, 474333 bytes
- Current recheck: current HTML contains `BPST1027` and no longer contains the
  stale `BRVO4706` claim-code mismatch. Current HTML has 6 `<img>` tags.
- Recommendation: review-ready for postcard-only approval.

### `browning-electrical-services`

- Business: Browning Electrical Services
- Stage: `needs_approval`
- Email on file: none
- Postcard status: `not_submitted`
- Claim code: `TPSA5780`
- Preview URL: `https://browning-electrical-services.pages.dev`
- Recipient: `Browning Electrical`, `3742 Bittercreek Way SW`, Lilburn GA
  `30047`
- Payload preview: 200 / valid
- Desktop screenshot: `image/jpeg`, 333177 bytes
- Mobile screenshot: `image/jpeg`, 173621 bytes
- Hero image: `image/jpeg`, 599406 bytes
- Current recheck: claim code is present; no open detail-note blocker found.
- Caveat: CRM `siteNotes` still says business may not still be live and recent
  activity may be worth checking. Treat as Jesse-review-ready, with a business
  confidence caveat.
- Recommendation: review-ready for postcard-only approval if Jesse accepts the
  business-confidence caveat.

### `chrissy-s-mobile-detailing`

- Business: Chrissy's Mobile Detailing
- Stage: `needs_approval`
- Email on file: `miamistyledetailllc@gmail.com`
- Postcard status: `not_submitted`
- Claim code: `CMDW5642`
- Preview URL: `https://chrissy-s-mobile-detailing.pages.dev`
- Recipient: `Chrissy`, `3455 Peachtree Rd NE`, Atlanta GA `30326`
- Payload preview: 200 / valid
- Desktop screenshot: `image/jpeg`, 396019 bytes
- Mobile screenshot: `image/jpeg`, 194074 bytes
- Hero image: `image/jpeg`, 724857 bytes
- Current recheck: old H1 spacing issue is no longer visible, and current HTML
  has 6 `<img>` tags. Current HTML still contains both `117 Google Reviews` and
  `133`, so the old review-count inconsistency may remain current.
- Recommendation: secondary review candidate. Do not send email during remote
  week; postcard-only requires Jesse to accept or override the review-count
  inconsistency.

### `thermys-mobile-tire-and-brakes`

- Business: Thermys Mobile Tire and Brakes LLC
- Stage: `needs_approval`
- Email on file: none
- Postcard status: `not_submitted`
- Claim code: `THMY-QW01`
- Preview URL: `https://thermys-mobile-tire-and-brakes.pages.dev`
- Recipient: `Quartisha Williams`, `125 Milton Ave SE`, Atlanta GA `30315`
- Payload preview: 200 / valid
- Desktop screenshot: `image/jpeg`, 354750 bytes
- Mobile screenshot: `image/jpeg`, 181505 bytes
- Hero image: `image/jpeg`, 363488 bytes
- Current recheck: old copy-spacing strings are no longer visible, but current
  HTML still has zero `<img>` tags. The old high-priority photo/content note is
  therefore revalidated as a current visual/content gap.
- Recommendation: hold for Jesse visual/content override or Post-Build repair.

### `tuxedo-mechanical-plumbing`

- Business: Tuxedo Mechanical & Plumbing
- Stage: `needs_approval`
- Email on file: `whuckabee@bellsouth.net`
- Postcard status: `not_submitted`
- Claim code: `TXDO3912`
- Preview URL: `https://tuxedo-mechanical-plumbing.pages.dev`
- Recipient: `Wayne M. Huckabee`, `3905 Longview Dr`, Chamblee GA `30341`
- Payload preview: 200 / valid
- Desktop screenshot: `image/jpeg`, 362015 bytes
- Mobile screenshot: `image/jpeg`, 177973 bytes
- Hero image: `image/jpeg`, 493456 bytes
- Current recheck: copyright is now `2026` and claim code is present. Current
  HTML still has zero `<img>` tags and references the older Unsplash-style hero
  asset ID `photo-1504328345606`, so the photo/source concern remains current.
- Recommendation: hold for Jesse visual/content override or Post-Build repair.
  Do not send email during remote week.

## Failed Or Held Gates

### `rooter-pro-plumbing-drain`

- Stage: `needs_approval`
- Payload preview: not used for send recommendation
- Failure: postcard hero dimensions are `2048x1152`, below the 3000x1700
  minimum required by the readiness gate.
- Asset byte sizes alone are not enough: the hero URL returns a large JPEG, but
  the dimensions fail print-spec.
- Safe next action: Post-Build hero repair packet; do not include in a send
  batch.

### `cityboys`

- Stage: `qa_approved`
- Gate status: mechanically ready
- Failure/hold: explicit Jesse hold pending visual QA for confusing/wrong
  postcard imagery
- Safe next action: prepare visual QA artifact; do not send

### `piedmont-tires`

- Stage: `qa_approved`
- Gate status: failed
- Failure: `preview_postcard_payload` returns 400 because mailing fields are
  incomplete; ZIP is missing from CRM
- Safe next action: source-backed ZIP repair packet; do not send

## Exact Approval Text For Jesse

For review only:

```text
Approved: needs_approval postcard review queue.

Review these prospects for postcard-only outreach readiness:
1. 24-hrs-mobile-tire-services
2. bravo-plumbing-solutions
3. browning-electrical-services

If I approve a named prospect after review, Outreach may run final live gates
immediately before send and submit that named postcard only if all gates pass.

Still prohibited:
Resend/email sends, SMS, prospect/customer contact outside approved Poplar
postcards, unrelated CRM/Supabase truth edits, Paperclip mutations, deploys, git
pushes, DNS/domain/hosting/billing changes, and Stripe actions.
```

For immediate named postcard-only send approval after Jesse review:

```text
Approved: Submit postcard-only outreach for <exact slug or named batch>.

Allowed:
1. Run final live gates immediately before send.
2. Submit Poplar postcard only for the named approved prospect(s) whose gates pass.
3. Stop on any failed gate or Poplar error with no retry.
4. Verify CRM/provider state and update Outreach status/artifact.

Still prohibited:
Resend/email sends, SMS, prospect/customer replies, unrelated CRM/Supabase truth
edits, Paperclip mutations, deploys, git pushes, DNS/domain/hosting/billing
changes, and Stripe actions.
```

## Explicit No-Action Statement

No postcard sends, Resend/email sends, SMS, prospect/customer contact,
CRM/Supabase writes, Paperclip mutations, deploys, DNS/domain/hosting/billing
changes, Stripe actions, or git pushes were performed while preparing this
packet.
