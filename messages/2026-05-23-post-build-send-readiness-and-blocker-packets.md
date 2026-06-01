# Post-Build Send-Readiness + Blocker Packets - 2026-05-23

Owner: Codex / Post-Build Operations  
Mode: remote-week board clearing  
Source ledger: `gtmdot-sites/messages`  
Generated: 2026-05-23T12:55:00-04:00  

## Scope

Prepare coordination artifacts only for the closest QA-approved prospects and
the seven active blockers. No sends, CRM writes, Paperclip mutations, deploys,
prospect contact, git push, DNS/domain/hosting/billing changes, or Stripe
actions were performed.

Read-only sources used:
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-away-mode-coordinator-roadmap.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md`
- Public CRM read-only prospect API and `preview_postcard_payload` preview action
- Public `gtmdot.com` claim lookup / checkout URLs
- Public `gtmdot-postcards.pages.dev` postcard image URLs
- `/private/tmp/gtmdot-postcard-asset-audit.json`
- `/private/tmp/gtmdot-remote-week-packet-data.json`

## Current State

Post-Build currently has 38 of 45 active/non-dead prospects passing the postcard
asset and claim/checkout checks. The four closest QA-approved prospects are all
technically send-ready from a Post-Build perspective, but none are approved for
channels in CRM yet (`approvedFor: []`).

Closest-to-revenue item:
`smartwire-solutions`, because it is QA-approved, has a clean postcard payload,
all three Poplar image URLs resolve as real `image/jpeg`, claim lookup resolves,
checkout loads, and it has no email on file, making the next decision simple:
postcard-only approval or hold.

Current blocker:
The blocker is not Post-Build assets for the closest four. The blocker is Jesse
approval/channel truth: all four have `approvedFor: []`, so no send should happen
until Jesse explicitly approves the channel(s).

Exact safe next action performed:
Prepared this packet for the main coordinator and Jesse. No production-impacting
action was performed.

## Send-Readiness Packets

### 1. `smartwire-solutions`

- Business: SmartWire Solutions
- Stage: `qa_approved`
- CRM approved channels: none (`approvedFor: []`)
- Email on file: none
- Postcard status: `not_submitted`
- Claim code: `SMAR1182`
- Preview URL: `https://smart-wire-solutions.pages.dev/`
- Checkout URL: `https://gtmdot.com/checkout?code=SMAR1182&site=smartwire-solutions`
- Claim lookup: OK, resolves to `smartwire-solutions`
- Checkout check: OK, `200 text/html`
- Payload preview: OK, `200`
- Recipient in payload: Terry Henry, 730 Peachtree St NE, Ste 570, Atlanta, GA 30308
- Desktop screenshot: OK, `image/jpeg`, 341,870 bytes
- Mobile screenshot: OK, `image/jpeg`, 155,869 bytes
- Hero image: OK, `image/jpeg`, 532,894 bytes
- Recommended channel: postcard only, because no email is currently on file
- Send-readiness verdict: technically ready, waiting on Jesse approval

Exact Jesse approval needed:
`Approved: smartwire-solutions postcard-only outreach. Allowed: set/confirm postcard approval as needed, submit one Poplar postcard using claim code SMAR1182, verify provider response and CRM/provider state afterward. Still prohibited: email/SMS, prospect contact outside Poplar, unrelated CRM edits, deploys, git push, DNS/domain/hosting/billing changes, and Stripe actions.`

### 2. `cityboys`

- Business: City Boys R Us
- Stage: `qa_approved`
- CRM approved channels: none (`approvedFor: []`)
- Email on file: `info@cityboysrus.com`
- Postcard status: `not_submitted`
- Claim code: `CITY6612`
- Preview URL: `https://cityboys.pages.dev`
- Checkout URL: `https://gtmdot.com/checkout?code=CITY6612&site=cityboys`
- Claim lookup: OK, resolves to `cityboys`
- Checkout check: OK, `200 text/html`
- Payload preview: OK, `200`
- Recipient in payload: Curtis, 3348 Peachtree Rd NE #700, Atlanta, GA 30326
- Desktop screenshot: OK, `image/jpeg`, 115,011 bytes
- Mobile screenshot: OK, `image/jpeg`, 59,334 bytes
- Hero image: OK, `image/jpeg`, 591,157 bytes
- Recommended channel: Jesse decision needed; postcard is technically ready,
  email is possible because an email exists
- Send-readiness verdict: technically ready, waiting on Jesse channel approval

Exact Jesse approval needed:
`Approved: cityboys outreach with channels: <postcard only | email only | postcard + email>. Allowed: set/confirm the approved channel(s), submit/send only the approved channel(s), then verify provider and CRM/provider state afterward. Still prohibited: unapproved channels, SMS, unrelated CRM edits, deploys, git push, DNS/domain/hosting/billing changes, and Stripe actions.`

### 3. `dream-steam`

- Business: Dream Steam
- Stage: `qa_approved`
- CRM approved channels: none (`approvedFor: []`)
- Email on file: none
- Postcard status: `not_submitted`
- Claim code: `ILIM2208`
- Preview URL: `https://dream-steam.pages.dev`
- Checkout URL: `https://gtmdot.com/checkout?code=ILIM2208&site=dream-steam`
- Claim lookup: OK, resolves to `dream-steam`
- Checkout check: OK, `200 text/html`
- Payload preview: OK, `200`
- Recipient in payload: Reuben, 2250 N Druid Hills Rd Ste 265, Atlanta, GA 30329
- Desktop screenshot: OK, `image/jpeg`, 157,080 bytes
- Mobile screenshot: OK, `image/jpeg`, 68,442 bytes
- Hero image: OK, `image/jpeg`, 948,238 bytes
- Recommended channel: postcard only, because no email is currently on file
- Send-readiness verdict: technically ready, waiting on Jesse approval

Exact Jesse approval needed:
`Approved: dream-steam postcard-only outreach. Allowed: set/confirm postcard approval as needed, submit one Poplar postcard using claim code ILIM2208, verify provider response and CRM/provider state afterward. Still prohibited: email/SMS, prospect contact outside Poplar, unrelated CRM edits, deploys, git push, DNS/domain/hosting/billing changes, and Stripe actions.`

### 4. `handy-dandy-atlanta`

- Business: Handy Dandy Atlanta
- Stage: `qa_approved`
- CRM approved channels: none (`approvedFor: []`)
- Email on file: none
- Postcard status: `not_submitted`
- Claim code: `HBSR0716`
- Preview URL: `https://handy-dandy-atlanta.pages.dev`
- Checkout URL: `https://gtmdot.com/checkout?code=HBSR0716&site=handy-dandy-atlanta`
- Claim lookup: OK, resolves to `handy-dandy-atlanta`
- Checkout check: OK, `200 text/html`
- Payload preview: OK, `200`
- Recipient in payload: Ruslan, 296 Possum Trot Rd, Barnesville, GA 30204
- Desktop screenshot: OK, `image/jpeg`, 130,199 bytes
- Mobile screenshot: OK, `image/jpeg`, 71,680 bytes
- Hero image: OK, `image/jpeg`, 933,136 bytes
- Recommended channel: postcard only, because no email is currently on file
- Note: business slug/name says Atlanta but CRM mailing address is Barnesville;
  payload is technically valid, but Jesse may want a quick human sanity check
  before send.
- Send-readiness verdict: technically ready, waiting on Jesse approval

Exact Jesse approval needed:
`Approved: handy-dandy-atlanta postcard-only outreach to the current CRM mailing address. Allowed: set/confirm postcard approval as needed, submit one Poplar postcard using claim code HBSR0716, verify provider response and CRM/provider state afterward. Still prohibited: email/SMS, prospect contact outside Poplar, unrelated CRM edits, deploys, git push, DNS/domain/hosting/billing changes, and Stripe actions.`

## Seven Active Blockers By Repair Type

### `raiden-electrical`

- Stage: `needs_approval`
- Repair type: preview URL/source repair, then screenshot regeneration
- Current CRM preview URL: `https://preview.gtmdot.com/raiden-electrical/`
- Current failure: DNS fails for the CRM preview URL; desktop/mobile screenshot
  URLs still return HTML fallback because screenshots cannot be generated from
  the source-of-truth URL
- What is already OK: claim lookup, checkout, payload preview, hero image
- Safe next action: find the deployed Pages URL or approved source URL and
  prepare a CRM preview URL repair approval packet
- Approval needed: CRM previewSiteUrl write and postcard screenshot regeneration
  if the corrected URL is approved

### `piedmont-tires`

- Stage: `qa_approved`
- Repair type: CRM mailing field reconciliation
- Current missing field: ZIP
- Current CRM fields: address `3483 Clairmont Rd`, city `Chamblee`, state `GA`,
  zip `null`
- What is already OK: preview URL, claim lookup, checkout, desktop screenshot,
  mobile screenshot, hero image
- Safe next action: gather source-backed ZIP evidence for `3483 Clairmont Rd,
  Chamblee, GA`; prepare exact CRM write approval
- Approval needed: CRM ZIP write before any Poplar postcard action

### `forest-park-collision`

- Stage: `needs_approval`
- Repair type: CRM mailing field reconciliation
- Current missing fields: street address, state, ZIP
- Current CRM fields: address `null`, city `Atlanta`, state `null`, zip `null`
- What is already OK: preview URL, claim lookup, checkout, desktop screenshot,
  mobile screenshot, hero image
- Safe next action: route to enrichment/source lookup for authoritative mailing
  address
- Approval needed: CRM address/state/ZIP writes and Jesse approval to move
  forward from `needs_approval`

### `pine-peach-painting`

- Stage: `needs_approval`
- Repair type: CRM mailing field reconciliation
- Current missing fields: street address and ZIP
- Current CRM fields: address `null`, city `Atlanta`, state `GA`, zip `null`
- What is already OK: preview URL, claim lookup, checkout, desktop screenshot,
  mobile screenshot, hero image
- Safe next action: route to enrichment/source lookup for authoritative mailing
  address
- Approval needed: CRM address/ZIP writes and Jesse approval to move forward
  from `needs_approval`

### `jack-glass-electric`

- Stage: `needs_enrichment`
- Repair type: CRM mailing field reconciliation / enrichment
- Current missing fields: street address and ZIP
- Current CRM fields: address `null`, city `Sandy Springs`, state `GA`, zip `null`
- What is already OK: preview URL, claim lookup, checkout, desktop screenshot,
  mobile screenshot, hero image
- Safe next action: route to Bruce/enrichment for source-backed address evidence
- Approval needed: CRM address/ZIP writes and later stage decision

### `total-repair-service`

- Stage: `needs_decision`
- Repair type: CRM mailing field reconciliation plus separate site-quality
  recovery-build blocker
- Current missing fields: street address, state, ZIP
- Current CRM fields: address `null`, city `Atlanta`, state `null`, zip `null`
- What is already OK: preview URL, claim lookup, checkout, desktop screenshot,
  mobile screenshot, hero image
- Safe next action: do not send; keep in rework/decision lane and prepare
  source-backed address evidence only if coordinator asks
- Approval needed: CRM address/state/ZIP writes, plus separate Jesse decision
  that the one-page recovery build is complete before QA/outreach

### `sandy-springs-plumbing`

- Stage: `outreach_sent`
- Repair type: channel/data reconciliation, not postcard asset repair
- Current missing fields: street address, city, state, ZIP are all blank
- What is already OK: preview URL, claim lookup, checkout, desktop screenshot,
  mobile screenshot, hero image
- Safe next action: read-only provider/CRM event reconciliation to determine
  whether the postcard already went out and whether CRM mailing fields were
  lost/stale
- Approval needed: any CRM address write, resend/retry, or provider action

## Exact Safe Next Action Recommended

Main coordinator should ask Jesse for exactly one decision first:

`Approved: smartwire-solutions postcard-only outreach. Allowed: set/confirm postcard approval as needed, submit one Poplar postcard using claim code SMAR1182, verify provider response and CRM/provider state afterward, and write a completion artifact. Still prohibited: email/SMS, prospect contact outside Poplar, unrelated CRM edits, deploys, git push, DNS/domain/hosting/billing changes, and Stripe actions.`

If Jesse does not want to approve a send while remote, the next safe no-approval
work is blocker research only: collect authoritative address evidence for
`piedmont-tires` first, because it is already `qa_approved` and all non-address
Post-Build checks pass.

## Explicit No-Action Statement

No CRM/Supabase writes, Paperclip mutations, deploys, Poplar/Resend/SMS sends,
prospect/customer contact, git pushes, DNS/domain/hosting/billing changes, or
Stripe actions were performed while preparing this packet.
