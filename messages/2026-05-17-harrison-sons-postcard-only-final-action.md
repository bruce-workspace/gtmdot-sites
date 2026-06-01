# Harrison & Sons Postcard-Only Final Action Prep

Date: 2026-05-17 America/New_York
Lane: Outreach Operations
Mode: read-only final-action prep

## Guardrails honored

- No postcard submitted or sent.
- No email sent.
- No CRM writes.
- No deploys.
- No Paperclip mutations.
- No prospect/customer contact.
- No git push.

## Jesse decision recorded

Jesse manually reviewed the live Harrison & Sons Electrical site.

Decision:

- The missing claim modal popup flag is stale; the popup exists.
- The old Unsplash/stock-image concern is not a blocker for postcard-only outreach.
- The April 4 notes are stale enough that they should not block outreach.
- Site is good enough for postcard-only outreach despite not being multi-page.
- Postcard preview looks good.
- Claim code and claim UI were already verified in the GTM-12 packet.

Approved direction:

Treat Harrison & Sons as Jesse-approved for postcard-only outreach readiness, pending the normal final no-send preflight. No email is available, so this is postcard-only.

## Current operational snapshot

Source: GTM-12 packet and `/private/tmp/detail-harrison-sons-electrical.json`.

- Prospect ID: `d2790267-0458-4007-9ba9-9cab70747710`
- Business: `Harrison & Sons Electrical Service LLC`
- Slug: `harrison-sons-electrical`
- Stage: `outreach_staged`
- Claim code: `HARR2423`
- Preview URL: `https://harrison-sons-electrical.pages.dev`
- Address: `3695 Cascade Rd #6250, Atlanta, GA 30331`
- Email: none
- Approved channels: `postcard`
- Postcard status: `not_submitted`
- Outreach events: none

GTM-12 verified:

- Live site returns `200 text/html`.
- Claim lookup for `HARR2423` returns `found:true`, slug `harrison-sons-electrical`, URL `https://harrison-sons-electrical.pages.dev`.
- Site hero and postcard hero both return `200 image/jpeg`, same byte size `1,156,010`.
- Desktop screenshot returns `200 image/jpeg`, `457,286` bytes.
- Mobile screenshot returns `200 image/jpeg`, `178,998` bytes.
- Live HTML includes `HARR2423`, shared claim bar, shared claim popup, `$49`, and `$149`.

## Stale-note reconciliation plan

Do not delete notes. Reconcile with explicit resolution/override text so the audit trail remains intact.

Recommended CRM note actions, when CRM writes are separately approved:

1. Resolve note `35be8766-f39d-41cd-84ba-7369f8b67620`.
   - Existing concern: missing `gtmdot-claim-popup` modal.
   - Resolution: stale; Jesse manually verified popup exists; GTM-12 packet verified live HTML includes shared claim popup, popup markup, claim code, and popup CTA.

2. Resolve note `96c7d242-c97f-44ba-974e-6d3aa1023451`.
   - Existing concern: visible Unsplash stock image.
   - Resolution: stale/non-blocking for postcard-only; Jesse approved postcard-only outreach despite old stock-image concern; GTM-12 live HTML found no `images.unsplash.com` reference.

3. Resolve or override note `7ecc5478-6275-4a5c-a09f-7e9654bb4cc9` for postcard-only outreach.
   - Existing concern: stock photos and fabricated-looking testimonials.
   - Resolution: April-era concern no longer blocks postcard-only outreach. Jesse manually approved postcard-only readiness. Do not use this as a blocker for postcard send. Keep any future site-polish concern as non-blocking if desired.

4. Resolve or override note `06709239-733f-4c44-aa1c-19dec3245c4a`.
   - Existing concern: all content below hero invisible.
   - Resolution: stale/false positive; GTM-12 live packet and Jesse manual review confirm site is usable for postcard-only outreach.

5. Add one concise decision note, if CRM writes are approved:

```text
Jesse decision 2026-05-17: Harrison & Sons Electrical approved for postcard-only outreach readiness. Missing popup flag is stale; popup exists. Old Unsplash/stock-image and April 4 notes do not block postcard-only outreach. Site is acceptable despite single-page structure. Non-blocking UX notes remain: immediate popup timing, FAQ accordion awkwardness, weak/low-context gallery image, tight review spacing. No email available; postcard-only path.
```

## Non-blocking UX notes to preserve

These should not block postcard submission, but can be kept as future polish context:

- Claim popup appears immediately on page load; not ideal.
- FAQ accordion behavior is awkward: answer text partially shows before expanding.
- Gallery/on-the-job photos lack context, and one porch/outdoor image feels weak.
- Reviews section has tight spacing between subheader and large pull quote.

Recommended handling:

Do not keep these as high-priority outreach blockers. If recorded, use low-priority non-blocking polish notes or a post-send improvement note.

## Normal final no-send preflight

Run immediately before requesting/performing the actual postcard submission:

1. Confirm no postcard event already exists for prospect `d2790267-0458-4007-9ba9-9cab70747710`.
2. Confirm stage is still `outreach_staged` and approved channels still include only `postcard`.
3. Confirm no email is on file; do not attempt email outreach.
4. Confirm mailing address is parseable as:
   - street: `3695 Cascade Rd #6250`
   - city: `Atlanta`
   - state: `GA`
   - zip: `30331`
5. Confirm live site `https://harrison-sons-electrical.pages.dev` returns `200`.
6. Confirm claim lookup for `HARR2423` returns `found:true` and slug `harrison-sons-electrical`.
7. Confirm postcard assets return `200 image/jpeg`:
   - `https://gtmdot-postcards.pages.dev/harrison-sons-electrical-hero.jpg`
   - `https://gtmdot-postcards.pages.dev/screenshots/harrison-sons-electrical-desktop.jpg`
   - `https://gtmdot-postcards.pages.dev/screenshots/harrison-sons-electrical-mobile.jpg`
8. Confirm stale notes are either resolved/overridden in CRM or Jesse explicitly approves sending with note reconciliation to follow.
9. Confirm Poplar send is explicitly approved by Jesse.

## Exact final action once separately approved

When Jesse separately approves CRM writes and Poplar postcard submission, submit the postcard through the current CRM action path for prospect `d2790267-0458-4007-9ba9-9cab70747710`:

```http
POST /api/prospects/d2790267-0458-4007-9ba9-9cab70747710/actions
Content-Type: application/json

{"action":"submit_postcard"}
```

Expected side effects of that action, based on current CRM code:

- Calls Poplar postcard submission.
- Inserts `outreach_events` row with `channel=postcard`, `event_type=submitted`, `sequence_number=1`, and Poplar `orderId` metadata.
- Inserts activity item `postcard_submitted`.
- Moves prospect from `outreach_staged` to `outreach_sent`.

Because these are live side effects, do not perform this action until Jesse separately approves the send/write.

## Recommended next action

Ask Jesse for one explicit combined approval, if ready:

`Approve Harrison & Sons stale-note reconciliation and Poplar postcard submission after final no-send preflight.`

If approval is split, do the CRM stale-note reconciliation first, then request/execute postcard submission separately.
