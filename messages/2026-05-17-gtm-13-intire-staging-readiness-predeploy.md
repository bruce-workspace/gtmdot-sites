---
from: codex
to: post-build-operations / paperclip-v2 / jesse
date: 2026-05-17
type: staging-readiness
paperclip: GTM-3, GTM-13, GTM-14
subject: InTire Mobile Tire Shop asset-fix path requires deploy/CDN approval
---

# InTire Mobile Tire Shop - Staging Readiness Pre-Deploy Packet

Verdict: **BLOCKED PENDING DEPLOY/CDN APPROVAL**

InTire remains the best next `qa_approved` prospect to move toward
`outreach_staged`, but the minimum fixes require a prospect-site deploy and a
postcard CDN deploy. Per Jesse's instruction, execution stopped before those
actions.

## Current CRM / Channel State

- Slug: `intire-mobile-tire-shop`
- Business: InTire Mobile Tire Shop
- Stage: `qa_approved`
- Claim code: `INTR-AJ01`
- Preview URL: `https://intire-mobile-tire-shop.pages.dev`
- Email: `intiremobile@gmail.com`
- Address: `2425 Columbia Dr, Decatur, GA 30032`
- Open tasks: `0`
- Outreach events: none
- Postcard status: not submitted
- Email sent count: `0`

## Current Live Checks

Probe artifact: `/private/tmp/check-intire-mobile-tire-shop.txt`

- Live site: `200 text/html; charset=utf-8`, 61,218 bytes.
- Claim lookup: `200 application/json`, lookup returned `found:true`.
- Lookup slug: `intire-mobile-tire-shop`.
- Lookup URL: `https://intire-mobile-tire-shop.pages.dev`.
- Live site hero: `200 image/jpeg`, 545,786 bytes.
- Postcard hero CDN: `200 image/jpeg`, 759,387 bytes.
- Desktop screenshot CDN: `200 text/html; charset=utf-8`, 20,050 bytes.
- Mobile screenshot CDN: `200 text/html; charset=utf-8`, 20,050 bytes.

## Local Source / Asset Findings

- Local `gtmdot/sites/intire-mobile-tire-shop/index.html` exactly matches live
  HTML by SHA-256.
- The current local site source references `photos/hero.jpg`.
- Local `gtmdot/sites/intire-mobile-tire-shop/photos/hero.jpg` is missing.
- Local `gtmdot/sites/intire-mobile-tire-shop/hero.jpg` is also missing in the
  current working tree, though it is tracked in git history.
- The approved generated/postcard hero exists in both places and hashes match:
  - `/Users/bruce/.openclaw/workspace/gtmdot/postcards/intire-mobile-tire-shop-hero.jpg`
  - `/Users/bruce/.openclaw/workspace/gtmdot-sites/sites/intire-mobile-tire-shop/photos-generated/hero-postcard.jpg`
- Hero hash: `c4e43a09331b08d773e5f3a9604c7e2205ecf487b722769f47e843e4dd373166`.
- Hero dimensions: 3840 x 2160.
- `bruce-asset-intel.json` records `model_stack.image_generation = "openai/gpt-image-2"`.

## GTM-14 Preflight Result

Pass:

- Stage is eligible: `qa_approved`.
- Claim code resolves through live lookup endpoint.
- Email present.
- Address present.
- No open CRM tasks surfaced.
- Live page includes claim bar, popup, `INTR-AJ01`, `$49`, and `$149`.
- Postcard hero exists and is print-sized.
- Hero provenance is gpt-image-2.

Blocked:

- Site hero and postcard hero do not match.
- Desktop screenshot CDN path returns Cloudflare HTML fallback, not image/jpeg.
- Mobile screenshot CDN path returns Cloudflare HTML fallback, not image/jpeg.
- The fixes require deployment/upload, so execution stopped before mutation.

## Required Approval To Execute

Approval needed: **Prospect-site deploy plus postcard screenshot/CDN repair for
`intire-mobile-tire-shop` only.**

Intended file changes:

- Create/copy:
  `/Users/bruce/.openclaw/workspace/gtmdot/sites/intire-mobile-tire-shop/photos/hero.jpg`
  from:
  `/Users/bruce/.openclaw/workspace/gtmdot/postcards/intire-mobile-tire-shop-hero.jpg`
- Generate:
  `/Users/bruce/.openclaw/workspace/gtmdot/postcards/screenshots/intire-mobile-tire-shop-desktop.jpg`
- Generate:
  `/Users/bruce/.openclaw/workspace/gtmdot/postcards/screenshots/intire-mobile-tire-shop-mobile.jpg`

Commands involved:

```bash
mkdir -p /Users/bruce/.openclaw/workspace/gtmdot/sites/intire-mobile-tire-shop/photos
cp /Users/bruce/.openclaw/workspace/gtmdot/postcards/intire-mobile-tire-shop-hero.jpg \
  /Users/bruce/.openclaw/workspace/gtmdot/sites/intire-mobile-tire-shop/photos/hero.jpg

npx wrangler pages deploy \
  /Users/bruce/.openclaw/workspace/gtmdot/sites/intire-mobile-tire-shop \
  --project-name=intire-mobile-tire-shop \
  --commit-dirty=true

cd /Users/bruce/.openclaw/workspace/brucecom-v3
npx tsx scripts/generate-postcard-screenshots.ts --slug=intire-mobile-tire-shop

cd /Users/bruce/.openclaw/workspace/gtmdot/postcards
npx wrangler pages deploy . --project-name=gtmdot-postcards --commit-dirty=true
```

Required post-execution verification:

```bash
curl -sS -L -o /dev/null -w '%{http_code} %{content_type} %{size_download}\n' \
  https://intire-mobile-tire-shop.pages.dev/photos/hero.jpg

curl -sS -L -o /dev/null -w '%{http_code} %{content_type} %{size_download}\n' \
  https://gtmdot-postcards.pages.dev/intire-mobile-tire-shop-hero.jpg

curl -sS -L -o /dev/null -w '%{http_code} %{content_type} %{size_download}\n' \
  https://gtmdot-postcards.pages.dev/screenshots/intire-mobile-tire-shop-desktop.jpg

curl -sS -L -o /dev/null -w '%{http_code} %{content_type} %{size_download}\n' \
  https://gtmdot-postcards.pages.dev/screenshots/intire-mobile-tire-shop-mobile.jpg
```

Expected result:

- Live site hero returns `image/jpeg` with byte-size matching the postcard hero
  or otherwise verified as the same approved asset.
- Desktop/mobile screenshot URLs return `image/jpeg`, not HTML fallback.
- Re-run GTM-14 preflight returns safe-to-stage technically.

## Risk Summary

- The local InTire site directory is already dirty from previous work. The local
  `index.html` matches live exactly, but tracked non-runtime files are deleted
  in the working tree. Deploying the current directory should affect the live
  site bundle, so approval should be explicit.
- `deploy-site.sh` is not the right command for this repair because the current
  source no longer has the old `BUILD-CHECKLIST.md` gate file. A direct Wrangler
  Pages deploy is the practical minimum.
- Screenshot generation depends on the local CRM API at `http://localhost:3002`.
  It is currently reachable.
- No CRM movement, Poplar submission, or email send is part of this approval.

## Safe-To-Stage Verdict

Current verdict: **not safe to move toward `outreach_staged` yet**.

If Jesse approves the deploy/CDN repair and the post-execution checks pass,
InTire should become safe to move toward `outreach_staged`, pending Jesse's
separate business approval for actual outreach.

## Actions Explicitly Not Performed

- No CRM/Supabase writes.
- No Paperclip mutations.
- No prospect-site deploy.
- No postcard CDN deploy.
- No Poplar postcard submissions.
- No Resend/email sends.
- No SMS sends.
- No prospect/customer contact.
- No production site edits.
- No git pushes.
- No DNS/domain/hosting/billing changes.
- No Stripe actions.
