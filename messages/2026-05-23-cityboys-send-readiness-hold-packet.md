# Cityboys Send-Readiness Hold Packet - 2026-05-23

Owner: Codex / Post-Build + Outreach  
Status: hold, not approved for send  
Reason for packet: Jesse explicitly excluded Cityboys from the approved first
batch because he recently saw confusing or wrong postcard imagery.

## Current State

- Prospect: `cityboys`
- Business: City Boys R Us
- Stage: `qa_approved`
- Approved channels: `[]`
- Postcard status: `not_submitted`
- Email on file: `info@cityboysrus.com`
- Emails sent: `0`
- Claim code: `CITY6612`
- Preview URL: `https://cityboys.pages.dev`
- Checkout URL: `https://gtmdot.com/checkout?code=CITY6612&site=cityboys`

## Technical Readiness

All mechanical checks pass as of the latest read-only packet:

- Claim lookup: OK, resolves to `cityboys`
- Checkout URL: OK, `200 text/html`, 78,627 bytes
- Payload preview: OK, `200`
- Recipient: Curtis, 3348 Peachtree Rd NE #700, Atlanta, GA 30326
- Desktop screenshot: OK, `200 image/jpeg`, 115,011 bytes
- Mobile screenshot: OK, `200 image/jpeg`, 59,334 bytes
- Hero image: OK, `200 image/jpeg`, 591,157 bytes

Poplar merge-tag image URLs:
- `https://gtmdot-postcards.pages.dev/screenshots/cityboys-desktop.jpg`
- `https://gtmdot-postcards.pages.dev/screenshots/cityboys-mobile.jpg`
- `https://gtmdot-postcards.pages.dev/cityboys-hero.jpg`

## Current Blocker

The blocker is not a mechanical asset/CDN failure. The blocker is visual/truth
QA: Jesse saw confusing or wrong postcard imagery. This needs a fresh visual
review before Cityboys is approved for any send.

## Recommended Safe Next Action

Post-Build should prepare a visual QA artifact for Cityboys showing:
- Current postcard preview front/back if available.
- Current desktop screenshot image.
- Current mobile screenshot image.
- Current hero image.
- Whether the hero/postcard imagery matches City Boys R Us and does not appear
  to belong to another trade/prospect.

No send should occur until Jesse approves Cityboys after that visual review.

## Exact Approval Needed From Jesse

If the visual QA passes, the clean approval would be:

`Approved: cityboys postcard-only outreach after visual QA. Allowed: submit one Poplar postcard using claim code CITY6612, verify provider response and CRM/provider state afterward, and write a completion artifact. Still prohibited: email/SMS, prospect contact outside Poplar, unrelated CRM edits, deploys, git push, DNS/domain/hosting/billing changes, and Stripe actions.`

Email should remain separately approved because Cityboys has an email on file.

## Explicit No-Action Statement

No CRM/Supabase writes, Paperclip mutations, deploys, Poplar/Resend/SMS sends,
prospect/customer contact, git pushes, DNS/domain/hosting/billing changes, or
Stripe actions were performed for Cityboys.
