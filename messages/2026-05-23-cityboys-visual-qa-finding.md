# Cityboys Visual QA Finding - 2026-05-23

Owner: Codex / GTMDot quarterback  
Mode: visual QA artifact only  
Status: blocked before send  

## Purpose

Resolve the Cityboys hold with current visual evidence. Jesse previously flagged confusing/wrong postcard imagery. This check confirms the concern is valid.

No CRM writes, sends, deploys, Paperclip mutations, prospect contact, git push, DNS/domain/hosting/billing changes, Stripe actions, or production edits were performed.

## Current Prospect State

- Slug: `cityboys`
- Business: City Boys R Us
- Stage: `qa_approved`
- Email: `info@cityboysrus.com`
- Claim code: `CITY6612`
- Preview URL: `https://cityboys.pages.dev`
- Checkout URL: `https://gtmdot.com/checkout?code=CITY6612&site=cityboys`
- Postcard status: `not_submitted`

## Evidence Checked

Downloaded current public postcard assets to `/private/tmp` for visual inspection:

- `/private/tmp/cityboys-desktop.jpg`
- `/private/tmp/cityboys-mobile.jpg`
- `/private/tmp/cityboys-hero.jpg`

Public URLs:

- `https://gtmdot-postcards.pages.dev/screenshots/cityboys-desktop.jpg`
- `https://gtmdot-postcards.pages.dev/screenshots/cityboys-mobile.jpg`
- `https://gtmdot-postcards.pages.dev/cityboys-hero.jpg`

Also checked the live site HTML at `https://cityboys.pages.dev`.

## Findings

### Website Screenshots

The desktop and mobile screenshot assets show an appliance-repair website:

- Headline: `Atlanta's Appliance Repair Since 2008. Ask for Curtis.`
- Business label: `City Boys R Us`
- CTA phone: `(404) 454-4680`
- Visual: appliance repair technician in a laundry/home setting.

These screenshots appear consistent with the current live Cityboys website positioning.

### Postcard Hero

The current postcard hero asset shows a classic black car in a driveway. It does not visually match:

- Appliance repair.
- The live website hero.
- The screenshot assets.
- The likely service expectation for City Boys R Us.

Local source-backed postcard hero path also contains the same car image:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/sites/cityboys/photos-generated/hero-postcard.jpg`

## Verdict

`cityboys` should remain held. The mechanical gates pass, but the postcard hero is visually mismatched and would likely create confusion or reduce trust.

## Recommended Repair

Prepare a Cityboys image repair package before any send:

1. Replace the postcard hero with an appliance-repair-aligned image that matches the live website direction.
2. Regenerate or verify postcard preview assets after replacement.
3. Recheck public `cityboys-hero.jpg`, desktop screenshot, mobile screenshot, claim lookup, checkout, and payload.
4. Only then request Jesse approval for postcard-only send.

## Approval Needed For Repair

Not ready to execute yet. The safe next step is to identify the intended replacement image and produce a narrow repair/deploy approval packet. Any deploy or postcard CDN repair still requires separate explicit approval.

## Explicit No-Action Statement

No CRM/Supabase writes, Paperclip mutations, deploys, Poplar/Resend/SMS sends, prospect/customer contact, DNS/domain/hosting/billing changes, Stripe actions, git pushes, or production-impacting edits were performed.
