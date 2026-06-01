---
from: codex
to: post-build-operations / paperclip-v2 / jesse
date: 2026-05-18
type: repair-complete
paperclip: GTM-3, GTM-13, GTM-14
subject: InTire Mobile Tire Shop deploy/CDN repair complete
---

# InTire Mobile Tire Shop - Post-Build Repair Complete

Verdict: **READY FOR JESSE STAGE/OUTREACH DECISION**

The approved InTire Mobile Tire Shop Post-Build repair package was executed.
The site hero now matches the postcard hero, desktop/mobile screenshot CDN paths
serve real `image/jpeg` assets, and the GTM-14 readiness gate passed.

## Actions Performed

Approved actions executed:

- Copied:
  `/Users/bruce/.openclaw/workspace/gtmdot/postcards/intire-mobile-tire-shop-hero.jpg`
  to:
  `/Users/bruce/.openclaw/workspace/gtmdot/sites/intire-mobile-tire-shop/photos/hero.jpg`
- Deployed only:
  `/Users/bruce/.openclaw/workspace/gtmdot/sites/intire-mobile-tire-shop`
  to Cloudflare Pages project `intire-mobile-tire-shop` with
  `--commit-dirty=true`.
- Ran screenshot generation for `--slug=intire-mobile-tire-shop` only.
- Applied the known screenshot-output workaround by copying only the two InTire
  generated screenshots from the doubled `.openclaw` output path into the
  canonical `gtmdot/postcards/screenshots/` directory.
- Deployed:
  `/Users/bruce/.openclaw/workspace/gtmdot/postcards`
  to Cloudflare Pages project `gtmdot-postcards` with `--commit-dirty=true`.
- Reran the GTM-14/outreach readiness gate for `intire-mobile-tire-shop`.

## Deploy Results

InTire Pages deploy:

- Command:
  `npx wrangler pages deploy /Users/bruce/.openclaw/workspace/gtmdot/sites/intire-mobile-tire-shop --project-name=intire-mobile-tire-shop --commit-dirty=true`
- Result: success.
- Uploaded: 1 file, 1 already uploaded.
- Preview: `https://49a3850a.intire-mobile-tire-shop.pages.dev`

Postcards CDN deploy:

- Command:
  `npx wrangler pages deploy . --project-name=gtmdot-postcards --commit-dirty=true`
- Workdir: `/Users/bruce/.openclaw/workspace/gtmdot/postcards`
- Result: success.
- Uploaded: 2 files, 253 already uploaded.
- Preview: `https://820090db.gtmdot-postcards.pages.dev`

## Verification

Live checks after deploy:

- Live site: `200 text/html; charset=utf-8`, 61,218 bytes.
- Claim lookup: `200 application/json`, `found:true`, slug
  `intire-mobile-tire-shop`, URL `https://intire-mobile-tire-shop.pages.dev`.
- Live site hero:
  `https://intire-mobile-tire-shop.pages.dev/photos/hero.jpg`
  returned `200 image/jpeg`, 759,387 bytes.
- Postcard hero:
  `https://gtmdot-postcards.pages.dev/intire-mobile-tire-shop-hero.jpg`
  returned `200 image/jpeg`, 759,387 bytes.
- Hero parity: pass. Site hero and postcard hero byte-size match.
- Desktop screenshot:
  `https://gtmdot-postcards.pages.dev/screenshots/intire-mobile-tire-shop-desktop.jpg`
  returned `200 image/jpeg`, 375,807 bytes.
- Mobile screenshot:
  `https://gtmdot-postcards.pages.dev/screenshots/intire-mobile-tire-shop-mobile.jpg`
  returned `200 image/jpeg`, 165,827 bytes.
- Desktop screenshot dimensions: 2880 x 1800.
- Mobile screenshot dimensions: 780 x 1688.
- Live HTML includes `INTR-AJ01`, `photos/hero.jpg`, shared claim bar, shared
  claim popup, `$49`, and `$149`.
- CRM detail snapshot still shows `qa_approved`, email present, address present,
  open task count `0`, email sent count `0`, and no outreach events.

## Gate Result

`outreach-readiness-gate.sh intire-mobile-tire-shop` result:

- Claim-code resolves: pass.
- Desktop screenshot: pass.
- Mobile screenshot: pass.
- Postcard hero content-type: pass.
- Postcard hero dimensions: pass, 3840 x 2160.
- Hero provenance: pass, `openai/gpt-image-2`.
- Postcard mockup asset pattern: pass.
- Email present: pass, `intiremobile@gmail.com`.
- Email preview UI endpoint: warning, HTTP 404. Existing gate notes actual send
  via `/actions` still works; in-CRM preview endpoint is unavailable.
- Technical checks: passed.

## Remaining Blockers

Hard technical blockers: **none found after repair**.

Remaining non-technical approvals:

- Jesse must approve any CRM stage move.
- Jesse must approve postcard submission.
- Jesse must approve Resend/email trigger.
- Jesse must approve any billing/subscription-related action.

## Safe-To-Stage

It is technically safe to move InTire toward `outreach_staged` if Jesse approves
the stage move and outreach plan. Do not send postcard or email until separately
approved.

## Actions Explicitly Not Performed

- No CRM/Supabase writes.
- No Paperclip mutations.
- No Poplar postcard submissions.
- No Resend/email sends.
- No SMS sends.
- No prospect/customer contact.
- No git pushes.
- No DNS/domain/hosting/billing changes.
- No Stripe actions.
