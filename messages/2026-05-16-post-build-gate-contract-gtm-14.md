---
from: codex
to: post-build-operations / paperclip-v2 / jesse
date: 2026-05-16
type: gate-contract
paperclip: GTM-3, GTM-11, GTM-12, GTM-13, GTM-14
subject: Post-Build Operations reusable gate contract
---

# Post-Build Operations Gate Contract

This artifact codifies the post-build checks required before any GTMDot prospect
moves toward Jesse approval, outreach staging, postcard submission, or email
send. It is intentionally independent of the Paperclip v2 schema so the
orchestration layer can attach these named artifacts without blocking board
clearing.

## Operating Rules

- HTTP 200 is not proof that an asset exists.
- Every asset check must verify content-type, byte-size, and body shape.
- Cloudflare Pages fallback HTML at image paths is a blocker.
- Screenshot URL null, missing, or HTML-backed screenshot paths are blockers.
- The site must actually display the intended hero above the fold.
- Claim-code lookup must resolve live through `https://gtmdot.com/api/lookup-code?code=<CODE>`.
- `https://gtmdot.com/codes.json` is not the readiness resolver.
- Generated images need provenance and must not be represented as real customer work.
- Jesse approval is separate from technical readiness.
- CRM stage does not currently express full channel truth; postcard and email state must be audited separately.
- CRM notes/flags/blockers older than 7 days are stale by default. Old notes do
  not automatically block QA, staging, or outreach. Before treating an old note
  as a blocker, re-check it against the current live site, current CRM, and
  current assets. Preserve historical notes, but only current evidence-backed
  blockers should hold the board.

## Stale Note Policy

Effective 2026-05-17 per Jesse:

- Any CRM note, flag, or blocker older than 7 days is stale by default.
- Old notes do not automatically block QA, staging, or outreach.
- Before treating an old note as a blocker, re-check it against current live
  site, current CRM, and current assets.
- If the issue is resolved or no longer visible, mark it stale/resolved/overridden
  in the artifact and recommend CRM closure.
- If the issue is still real, create or preserve a current blocker with today's
  evidence.
- If the issue is minor polish, classify it as non-blocking UX feedback.
- Do not delete historical notes. Preserve the audit trail.
- Do not write CRM unless separately approved.
- For current board clearing, stale notes should not hold up outreach unless
  revalidated as current blockers.

Artifact fields for note reconciliation:

- Note age.
- Last verified date, if known.
- Current artifact status: `open`, `stale`, `resolved`, `overridden`,
  `current blocker`, or `non-blocking UX`.
- Evidence link or screenshot.
- Owner.
- Blocking vs non-blocking.
- Recommended CRM action.

CRM v2 requirement:

- Add explicit stale-note handling with note age, last verified date, current
  status, evidence link/screenshot, owner, blocking flag, and one-click actions
  for `revalidate`, `mark stale`, and `convert to current blocker`.

## Required Gate Artifacts

### `source-of-truth-check.md`

Purpose: prevent wrong-source deployments and stale live sites.

Required evidence:

- CRM slug and business name.
- Canonical source path, if present.
- Mini/deploy working-copy path, if present.
- Live preview URL.
- Latest relevant commit or file timestamp.
- Whether live HTML appears to match canonical, Mini working copy, or neither.
- Verdict: `pass`, `blocked`, or `needs-human`.

Blocks on:

- Missing approved source for a new multi-page cohort build.
- Live site deployed from stale or alternate source.
- Slug drift between CRM, source folder, live URL, postcard assets, or lookup-code result.

### `claim-path-check.md`

Purpose: verify the owner can claim the correct site from every customer-facing path.

Required evidence:

- Supabase `prospects.claim_code`.
- `gtmdot.com/api/lookup-code` result.
- `lookup-code.js` source entry when local source is available.
- Live site claim bar presence.
- Live popup presence.
- Checkout CTA URLs.
- Claim code found in site HTML.

Blocks on:

- Lookup result missing or wrong slug.
- Claim bar missing when required.
- Popup missing when required.
- CTA points to wrong code or wrong site.
- Site HTML uses stale claim code.

Soft warning:

- Checkout URLs omit `site=<slug>` if the current batch policy expects the claim-code plus site pattern.

### `asset-integrity-check.md`

Purpose: prove postcard/site assets are real, current, and print-safe.

Required evidence:

- Live site hero URL status, content-type, byte-size, dimensions.
- Postcard hero CDN URL status, content-type, byte-size, dimensions.
- Desktop screenshot URL status, content-type, byte-size.
- Mobile screenshot URL status, content-type, byte-size.
- Postcard rendering URLs, if available.
- Local source paths for matching assets.

Blocks on:

- Asset returns HTML, empty body, or tiny byte-size.
- Postcard hero below print-safe dimensions.
- Missing desktop or mobile screenshot.
- Missing postcard rendering when that channel is being sent.
- File exists locally but is not live on the expected CDN path.

### `hero-display-check.md`

Purpose: catch the failure where `photos/hero.jpg` exists but the site does not
use it as the hero.

Required evidence:

- Live hero section selector or structural description.
- Whether the above-the-fold hero uses the approved hero image.
- Screenshot or HTML/CSS evidence.
- Comparison against postcard hero when postcard hero is intended to be reused.

Blocks on:

- Text-only or gradient-only hero when approved hero art exists.
- Hero section uses different, stale, weak, or web-only image.
- Hero image appears only in a lower gallery/card section.

### `editorial-qa-check.md`

Purpose: remove generic, internal, stale, or misleading copy before Jesse review.

Required evidence:

- Visible copy scan.
- JSON-LD scan.
- Meta/alt text scan.
- Hidden text or template-token scan.
- Review/source integrity scan.
- Generated-image disclosure/provenance scan.

Blocks or needs human review on:

- Placeholder text.
- Internal process copy such as "Data captured".
- Generic GTMDot framing such as "a real local operator deserves...".
- Stale source copy, for example "no public email found" after a source-backed email was captured.
- Fake-sounding review attributions.
- Generated image represented as real job/customer work.
- JSON-LD facts that contradict CRM or source packet facts.

### `responsive-accessibility-check.md`

Purpose: verify the site works for the postcard recipient on mobile and desktop.

Required evidence:

- Desktop screenshot.
- Mobile screenshot.
- Mobile nav/tap target check.
- Axe/WCAG serious and critical violation status.
- Popup/claim bar behavior on mobile.

Blocks on:

- Critical or serious accessibility violations.
- Broken mobile layout.
- Claim UI unusable on mobile.
- Screenshot proves missing hero, blank top section, or wrong site.

### `pricing-check.md`

Purpose: prevent offer mismatch.

Required evidence:

- Live copy showing `$49` first month.
- Live copy showing `$149/mo` after first month.
- Any approved exception from Jesse.

Blocks on:

- Missing pricing where the current GTMDot offer should be visible.
- Wrong first-month or monthly price.
- Conflicting pricing between site, popup, claim bar, postcard, or email.

### `review-integrity-check.md`

Purpose: preserve source-backed social proof without inventing reviews.

Required evidence:

- Review source labels.
- Review snippets used.
- Whether snippets are from Google, Yelp, Yahoo Local, Facebook, or another source.
- Whether review counts/ratings are source-backed.

Blocks on:

- Invented Google reviews.
- Source labels that imply a platform not actually captured.
- Review snippets not found in the source packet.
- Static cards using placeholder/fake reviewer names.

### `channel-readiness-check.md`

Purpose: separate postcard readiness, email readiness, and already-sent channel state.

Required evidence:

- Postcard-ready: address, postcard assets, renderings, claim path, approved postcard copy.
- Email-ready: email, preview, sequence state, unsubscribe/legal footer, claim path.
- Already-sent postcard events.
- Already-sent email events, bounce/delivery state, sequence count.

Blocks on:

- Treating `outreach_sent` as proof that both postcard and email were sent.
- Missing address for postcard channel.
- Missing or low-confidence email for email channel.
- Bounce state without human decision.
- Duplicate send risk.

### `final-live-review.md`

Purpose: create the Jesse-facing packet.

Required evidence:

- Links to all gate artifacts above.
- Final live site URL.
- Claim URL.
- Postcard preview/rendering URLs.
- Email preview URL, if email channel is in scope.
- Remaining warnings.
- Explicit statement that no outreach has been sent unless already recorded.

Blocks on:

- Any missing required artifact.
- Any unresolved hard blocker.
- Any unresolved Jesse decision.

## Browserbase Email Enrichment Lane

Browserbase can be used for public-source enrichment, including email discovery
and confirmation, but it should remain separate from post-build QA execution.

Allowed without prospect contact:

- Public website contact/about/service pages.
- Public Yelp/Facebook/BBB/Yahoo Local/Nextdoor/Thumbtack/Angi pages when accessible.
- Public search result pages.
- Public source screenshots/evidence packets.

Not allowed without explicit approval:

- Paid scraping beyond approved Browserbase session usage.
- Login bypass.
- Captcha bypass.
- CRM writes.
- Email sends.
- Claim/contact forms.
- Any prospect/customer contact.

Required Browserbase output per prospect:

- `browserbase-evidence.json`.
- `browserbase-enrichment.md`.
- Source URLs.
- Timestamps.
- Extracted email/phone/address candidates.
- Confidence level and provenance for each candidate.
- Known unknowns and blocked sources.

## Current Board-Clearing Defaults

Immediate post-build priorities:

- `GTM-11`: The Appliance Gals, blocked by hero-display failure.
- `GTM-12`: Harrison & Sons Electrical, likely closest but needs open-note reconciliation.
- `GTM-13`: QA-approved batch preflight before staging.
- `GTM-14`: reusable post-build QA artifact contract and gate codification.

Recommended near-term order:

1. Fix and verify The Appliance Gals hero display before further send action.
2. Reconcile Harrison & Sons stale open notes and produce final live packet.
3. Repair missing screenshots for SmartWire Solutions and InTire Mobile Tire Shop.
4. Run this gate contract against the remaining `qa_approved` queue.
5. Route Browserbase/email enrichment as Bruce/Paperclip tasks, not as silent QA side effects.

## Actions Explicitly Not Performed

- No CRM writes.
- No deploys.
- No Poplar postcard submissions.
- No Resend/email sends.
- No prospect/customer contact.
- No production site edits.
- No git pushes.
- No DNS/domain/hosting/billing changes.
- No Stripe actions.
