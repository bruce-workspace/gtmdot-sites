# CRM v2 Codex Takeover / Control-Plane Reset

Date: 2026-06-01
Owner: Codex / GTMDot quarterback
Mode: coordination reset, no production switch

## Decision

Codex should take over practical direction of the CRM rebuild from the main GTMDot thread.

Reason: the current live CRM is too clunky for board clearing. Jesse is being forced to remember hidden workflow mechanics:

- where to put repair feedback,
- how to approve a site,
- when a postcard can be retried,
- which notes are stale,
- which prospects need enrichment,
- which providers actually accepted mail,
- which stage is real vs just historical drift.

That is not scalable. The CRM needs to become the control panel, not another place Jesse has to decode.

## Project Folder Decision

CRM v2 code already lives in the main GTMDot web app project:

`/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/`

Keep it there.

Do not move CRM v2 into a separate project folder. The separation should be by route and feature flag, not by repo/chat silo. The main Codex/GTMDot thread should be the coordinating owner because it has the full context across Outreach, Post-Build, Pre-Build, Paperclip, Poplar, and CRM v1 pain.

## North Star

CRM v2 must answer this question for every prospect:

> What is the exact next action, who owns it, what evidence supports it, and can Jesse approve/send/fix it from here without leaving the page?

If the answer is no, CRM v2 is not done.

## Non-Negotiable UX Requirements

### 1. Feedback Must Become Work

When Jesse sees something like:

- "Thermys hero image looks like a dude throwing a gang sign in front of a car."
- "Tuxedo has no nav bar."
- "Tuxedo hero looks like welding, not mechanical/plumbing."
- "Raiden site does not open."

There must be a visible action:

`Needs Fix`

That action should create a structured repair item with:

- prospect slug,
- issue preset,
- freeform note,
- optional screenshot/evidence,
- blocking vs non-blocking,
- owner,
- current stage impact,
- created/last verified timestamps.

This cannot disappear into chat history.

### 2. Approval Must Be One Button

If a prospect is in `needs_approval`, `needs_decision`, `ready_for_review`, or `qa_approved`, Jesse should see:

`Approve for Outreach`

The current "Move Stage" workaround is not acceptable as the primary path.

### 3. Enrichment Must Not Wait On Jesse

Prospects in `needs_enrichment` should show:

`Run Enrichment`

The CRM should make it clear whether enrichment means:

- missing email,
- missing phone,
- missing/dirty address,
- bad hero/source gap,
- missing screenshot,
- missing claim/postcard asset,
- stale data needing revalidation.

If enrichment can safely run without Jesse, it should be queued or triggered by Codex/Bruce/dispatcher without making Jesse babysit it.

### 4. Provider Truth Must Override CRM Fiction

Poplar `exception` means the postcard did not enter healthy mail flow. It must not look like a clean sent postcard.

CRM v2 should show:

- CRM event state,
- Poplar provider state,
- cost,
- expected delivery,
- retry eligibility,
- payload/address problems,
- last verification time.

### 5. Stale Notes Cannot Block Forever

Notes older than 7 days are stale by default unless revalidated with current evidence.

CRM v2 needs visible actions:

- mark stale,
- revalidate,
- convert to current blocker,
- resolve,
- override as non-blocking.

### 6. Board Clearing Beats Perfect Design

For old single-page sites, "good enough to send" is an allowed Jesse decision.

If Jesse says Rooter Pro's hero is good enough, CRM should support an override path rather than re-blocking on strict historical image dimensions.

## Immediate Live CRM Bridge

A local live CRM patch has already been prepared in `brucecom-v3`:

- `Approve for Outreach`
- `Needs Fix`
- `Run Enrichment`

Artifact:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-01-crm-review-ux-and-current-board-friction.md`

Recommended next step is to deploy that bridge patch so the current board is usable while CRM v2 continues.

## CRM v2 Build Priority

CRM v2 should stop being only a read-only showcase and become a staged command center:

1. Read-only proof surface: keep the current `/lab/crm-v2` model.
2. Safe write pilot: add only low-risk writes first:
   - create repair feedback task,
   - mark stale/non-blocking,
   - approve for outreach,
   - run enrichment where already supported.
3. Provider truth pilot:
   - show Poplar provider state from stored events and/or read-only provider audit artifacts,
   - expose retry eligibility,
   - separate retry approval from provider diagnosis.
4. Board-clearing mode:
   - show "ready to approve", "ready to send postcard", "needs repair", "needs enrichment", "provider exception", and "monitor only" queues.
5. Only after this should CRM v2 replace live CRM.

## Current Prospect Pain Captured

### `thermys-mobile-tire-and-brakes`

Jesse has repeatedly flagged the hero as unacceptable:

> Hero looks like a dude throwing a gang sign in front of a car.

This needs to become a visible repair task and remain visible until fixed or explicitly overridden.

### `tuxedo-mechanical-plumbing`

Jesse-observed current issues:

- no nav bar,
- hero appears to show welding rather than mechanical/plumbing,
- site otherwise possibly usable but not approval-clean.

### `raiden-electrical`

Jesse-observed current issue:

- site does not open.

Existing evidence also says the CRM preview URL is `https://preview.gtmdot.com/raiden-electrical/`, which has known preview/DNS failure history.

### `browning-electrical-services`

Observed workflow issue:

- It is still in `needs_approval` even though postcard outreach already has provider-active history.

This is a channel/stage mismatch and should not present as a normal untouched approval card.

### `rooter-pro-plumbing-drain`

Jesse says:

- site looks good,
- hero is good enough,
- previous strict hero-dimension blocker should not stop progress if Jesse approves.

CRM needs an override path for this.

## Guardrails

Still prohibited without explicit approval:

- replacing live CRM with CRM v2,
- broad CRM/Supabase data writes,
- Poplar retries/sends,
- Resend/SMS sends,
- prospect/customer contact,
- Paperclip mutations,
- git pushes,
- DNS/domain/hosting/billing changes,
- Stripe actions.

## Explicit No-Action Statement

No deploy, CRM/Supabase write, Paperclip mutation, Poplar/Resend/SMS send, prospect contact, git push, DNS/domain/hosting/billing change, Stripe action, or production CRM replacement was performed by this reset.
