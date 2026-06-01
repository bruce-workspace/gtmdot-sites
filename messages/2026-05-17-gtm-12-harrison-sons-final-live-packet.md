---
from: codex
to: post-build-operations / paperclip-v2 / jesse
date: 2026-05-17
type: final-live-packet
paperclip: GTM-3, GTM-12
subject: Harrison & Sons Electrical read-only final live reconciliation
---

# GTM-12 - Harrison & Sons Electrical Final Live Packet

Verdict: **READY FOR JESSE POSTCARD DECISION**

Harrison & Sons Electrical is technically ready for Jesse's postcard-only
decision under the 2026-05-17 stale-note policy. No email address is present, so
email outreach is not available from current CRM data.

## CRM Snapshot

- Prospect: Harrison & Sons Electrical Service LLC
- Slug: `harrison-sons-electrical`
- Stage: `outreach_staged`
- Claim code: `HARR2423`
- Preview URL: `https://harrison-sons-electrical.pages.dev`
- Address present: yes
- Email present: no
- Approved channels: `postcard`
- Detail API outreach events: none
- CRM list caveat: `/api/prospects` can display `postcardStatus=submitted`
  when `approvedFor` includes `postcard` even with no postcard event. The
  detail/event data shows no submitted postcard event for Harrison.

## Live Checks

Source files:

- CRM detail: `/private/tmp/detail-harrison-sons-electrical.json`
- Live HTML: `/private/tmp/live-harrison-sons-electrical.html`
- Live probe: `/private/tmp/check-harrison-sons-electrical.txt`
- Lookup result: `/private/tmp/lookup-harrison-sons-electrical.json`

Results:

- Live site: `200 text/html; charset=utf-8`, 60,919 bytes.
- Claim lookup: `https://gtmdot.com/api/lookup-code?code=HARR2423` returned
  `found:true`, slug `harrison-sons-electrical`, URL
  `https://harrison-sons-electrical.pages.dev`.
- Site hero: `https://harrison-sons-electrical.pages.dev/photos/hero.jpg`
  returned `200 image/jpeg`, 1,156,010 bytes.
- Postcard hero:
  `https://gtmdot-postcards.pages.dev/harrison-sons-electrical-hero.jpg`
  returned `200 image/jpeg`, 1,156,010 bytes.
- Hero parity: pass. Site hero and postcard hero byte-size match.
- Local postcard hero dimensions: 3360 x 1872.
- Desktop screenshot:
  `https://gtmdot-postcards.pages.dev/screenshots/harrison-sons-electrical-desktop.jpg`
  returned `200 image/jpeg`, 457,286 bytes.
- Mobile screenshot:
  `https://gtmdot-postcards.pages.dev/screenshots/harrison-sons-electrical-mobile.jpg`
  returned `200 image/jpeg`, 178,998 bytes.
- Hero display: live CSS uses `photos/hero.jpg` in the hero background.
- Claim bar/popup/pricing: live HTML includes `HARR2423`, shared claim bar,
  shared claim popup, `$49`, and `$149`.
- Unsplash stock reference: no `images.unsplash.com` reference found in live HTML.

## Note Reconciliation Under 7-Day Stale Rule

Per Jesse's 2026-05-17 policy, CRM notes/flags/blockers older than 7 days are
stale by default and do not block QA, staging, or outreach unless revalidated
against current live evidence.

Observed notes:

- Missing popup note: **stale/resolved in artifact**. Current live HTML contains
  `gtmdot-claim-popup`, popup CSS/JS, popup markup, claim code, and popup CTA.
  Recommended CRM action: mark stale/resolved if CRM writes are later approved.
- Unsplash stock-image note: **stale/resolved in artifact**. No Unsplash URL was
  found in the current live HTML. Recommended CRM action: mark stale/resolved if
  CRM writes are later approved.
- Earlier generic/fabricated testimonial concern: **not a current blocker based
  on this artifact**. Live page now shows a scrolling review feed with named
  Google-labeled reviewers rather than older generic "South Fulton Homeowner"
  style labels.
- One live review mentions "Bobby": **non-blocking Jesse UX/editorial review**.
  It appears inside a named Google-labeled review snippet, so it should not be
  treated as a blocker unless Jesse wants it removed or re-sourced.

Current blocker status from old notes: **none revalidated as current blockers**.

## Readiness Verdict

Technical status: **ready for Jesse postcard-only decision**

Hard technical blockers found:

- None from live claim lookup, claim UI, hero parity, screenshots, or pricing.

Remaining non-technical constraints:

- No email is available.
- Channel-state truth needs clarification because list-level `postcardStatus`
  can imply submitted from `approvedFor`, while events show no postcard submit.

## Recommended Owner / Next Action

- Owner: Codex/Post-Build for read-only packet handoff.
- Owner: Jesse for final postcard-only outreach decision.
- Owner: Outreach/Mini only after approval for actual postcard launch.

Recommended next action:

Ask Jesse to review this packet and decide whether to authorize postcard-only
launch. Do not send until Jesse approves the postcard action. If CRM writes are
later approved, mark the stale April notes stale/resolved/overridden without
deleting history.

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
