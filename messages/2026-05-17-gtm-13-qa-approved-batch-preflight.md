---
from: codex
to: post-build-operations / paperclip-v2 / jesse
date: 2026-05-17
type: batch-preflight
paperclip: GTM-3, GTM-13
subject: QA-approved batch read-only preflight
---

# GTM-13 - QA-Approved Batch Preflight

Verdict: **no QA-approved prospect should move to outreach_staged yet without a
fix or Jesse override.**

The cleanest next prospect to move toward outreach staging is **InTire Mobile
Tire Shop**, but only after Mini/Post-Build fixes screenshot CDN assets and site
hero/postcard hero parity. It has the best combination of no open notes, email
present, address present, and valid claim lookup.

## Inputs

- CRM list snapshot: `/private/tmp/gtmdot-crm-prospects-check.json`
- CRM detail snapshots: `/private/tmp/detail-<slug>.json`
- Live HTML snapshots: `/private/tmp/live-<slug>.html`
- Live probe outputs: `/private/tmp/check-<slug>.txt`
- Lookup outputs: `/private/tmp/lookup-<slug>.json`

## Batch Table

| Prospect | Current stage | Claim status | Postcard status | Email status | Hero / screenshot status | Blocker | Next action |
|---|---|---|---|---|---|---|---|
| `cityboys` | `qa_approved` | Pass: `CITY6612` lookup resolves to `cityboys`. | Not submitted. Postcard hero and desktop/mobile screenshots return images. | Email present: `info@cityboysrus.com`. | Site hero and postcard hero do not match: 259,804 bytes vs 591,157 bytes. Screenshots are present. | Open notes: duplicate postcard warning and gallery-label/photo mismatch. Hero parity failure. | Post-Build/Mini: fix hero parity and reconcile notes before staging. Outreach/Jesse: verify duplicate-postcard note before any send. |
| `sandy-springs-plumbing` | `qa_approved` | Pass: `SSPL4817` lookup resolves to `sandy-springs-plumbing`. | Postcard blocked: no address in CRM. Postcard hero/screenshots return images. | Email present: `Jack@ontimefix.com`. | Site hero path returns HTML fallback, not an image. Postcard hero and screenshots are present. | Missing address blocks postcard. Site hero missing/fallback. | Bruce/Browserbase or CRM owner: resolve address. Mini: repair site hero if email-only or postcard path continues. |
| `dream-steam` | `qa_approved` | Pass: `ILIM2208` lookup resolves to `dream-steam`. | Not submitted. Address present. Postcard hero and screenshots return images. | No email. | Site hero and postcard hero do not match: 64,910 bytes vs 948,238 bytes. Screenshots are present. | Open note: gallery labels use CityBoys anti-pattern. Hero parity failure. | Mini/Post-Build: hero parity and gallery/editorial note reconciliation before postcard-only staging. |
| `handy-dandy-atlanta` | `qa_approved` | Pass: `HBSR0716` lookup resolves to `handy-dandy-atlanta`. | Not submitted. Address present. Postcard hero and screenshots return images. | No email. | Site hero and postcard hero do not match: 221,202 bytes vs 933,136 bytes. Screenshots are present. | Open notes: popup note likely stale, plus Jesse hero/form blocker. Hero parity failure. | Bruce/Mini: resolve contextual hero/form blocker, then Mini verifies popup/hero parity. |
| `tuckers-home-services` | `qa_approved` | Pass: `SHBJ5366` lookup resolves to `tuckers-home-services`. | Not submitted. Address present. Postcard hero and screenshots return images. | Email present: `tuckerhomeservices@yahoo.com`. | Site hero and postcard hero do not match: 58,276 bytes vs 999,136 bytes. Screenshots are present. | Open Jesse note: better existing-site photos should be pulled/used. Hero parity failure. | Bruce: photo/source enrichment from existing site. Mini: wire approved photos/hero and rerun preflight. |
| `intire-mobile-tire-shop` | `qa_approved` | Pass: `INTR-AJ01` lookup resolves to `intire-mobile-tire-shop`. | Not submitted. Address present. Postcard hero returns image. Desktop/mobile screenshot CDN paths return HTML fallback, not images. | Email present: `intiremobile@gmail.com`. | Site hero and postcard hero do not match: 545,786 bytes vs 759,387 bytes. Screenshots missing on CDN. | Screenshot CDN assets missing/HTML fallback. Hero parity failure. | **Recommended next prospect.** Mini/Post-Build: sync site hero to postcard hero, regenerate desktop/mobile screenshots, redeploy postcard CDN only after approval. |
| `smartwire-solutions` | `qa_approved` | Partial/fail: `SMAR1182` lookup returns found, but URL is `https://smartwire-solutions.pages.dev`, which did not resolve. CRM preview URL is `https://smart-wire-solutions.pages.dev/`, which does resolve. | Not submitted. Address present. Postcard hero returns image. Desktop/mobile screenshot CDN paths return HTML fallback, not images. | No email. | CRM preview URL hero returns image, but it does not match postcard hero: 509,720 bytes vs 532,894 bytes. Screenshots missing on CDN. | Slug/lookup URL drift, missing screenshots, hero parity failure, no email. | Platform/Post-Build: reconcile lookup-code URL vs CRM preview URL before any staging. Mini: then fix screenshots/hero parity. |

## Cross-Batch Findings

- All seven `qa_approved` claim codes return `found:true` from the live lookup
  endpoint, but SmartWire has URL drift.
- Multiple sites have postcard hero assets but the live site hero does not match
  the postcard hero. This is now a named blocker under the Post-Build gate.
- InTire and SmartWire screenshot CDN paths return HTML fallback with HTTP 200,
  proving again that HTTP status alone is not sufficient.
- Several open notes appear potentially stale, but they still block until
  reconciled or overridden.
- CRM stage alone is insufficient for channel truth. Email/postcard readiness
  must be tracked separately.

## Single Recommended Next Prospect

Recommended next prospect toward `outreach_staged`: **InTire Mobile Tire Shop**.

Reason:

- Stage is `qa_approved`.
- Claim lookup resolves correctly.
- Email is present.
- Address is present.
- No open notes surfaced in the detail API.
- Postcard hero exists and is print-sized locally.
- Remaining blockers are concrete Mini/Post-Build asset tasks: hero parity and
  screenshot CDN repair.

Do not move it yet. The recommended next action is to request approval for Mini
to fix hero parity, regenerate/upload screenshots, and rerun preflight.

## Actions Explicitly Not Performed

- No CRM/Supabase writes.
- No deploys.
- No Poplar postcard submissions.
- No Resend/email sends.
- No prospect/customer contact.
- No production site edits.
- No git pushes.
- No DNS/domain/hosting/billing changes.
- No Stripe actions.
