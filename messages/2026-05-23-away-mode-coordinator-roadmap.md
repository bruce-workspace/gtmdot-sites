# GTMDot Away-Mode Coordinator Roadmap - 2026-05-23

Owner: Codex / GTMDot quarterback  
Mode: remote-week operating plan  
Canonical ledger: `gtmdot-sites/messages` + lane status files  
Notification mirrors: Telegram/Slack only  

## Purpose

Jesse will be remote for roughly one week. The goal is to keep GTMDot moving without making Jesse manually copy status between project folders, while preserving hard approval boundaries around production, CRM truth, sends, deploys, billing, and prospect contact.

This plan turns the current lane handoffs into an operating queue:

1. Clear the near-revenue board.
2. Repair source-backed blockers that do not require strategic truth decisions.
3. Prepare exact approval packets for any send, CRM write, deploy, or production action.
4. Keep CRM v2, Paperclip, Telegram, and Experiments useful but subordinate to board clearing.

## Current Control Plane

- Paperclip is up locally at `http://127.0.0.1:3199/GTM/dashboard`.
- Paperclip health is reported as `ok`.
- Paperclip runtime LaunchAgent is loaded as `com.gtmdot.paperclip`.
- Dispatcher LaunchAgent is loaded as `com.gtmdot.dispatcher-bridge`.
- Latest known Paperclip backup: `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox/data/backups/paperclip-20260523-093015.sql.gz`.
- Dispatcher digest: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/2026-05-23-0932-dispatcher-digest.md`.
- Telegram bridge diagnostics show exactly one `MiniClaudeGTMBot` poller and clean `.in_use` state as of the latest read-only check.

## Operating Model

- Git/message files are the durable coordination ledger.
- Paperclip is the visible state, gate, and audit layer.
- CRM/Supabase remains prospect truth.
- Poplar/Resend/Gmail remain provider/channel truth.
- Telegram/Slack are notification and ACK mirrors only.
- Codex owns quarterbacking, routing, synthesis, and approval packets.
- Bruce owns enrichment/photo/review/asset intelligence when specifically routed.
- R1VS owns structured multi-page scaffolds from canonical packets only.
- Post-Build owns live-site, asset, claim, screenshot, and outreach-readiness gates.
- Outreach owns provider truth, send recommendations, reply/bounce monitoring, and no-send safety.
- CRM v2 remains lab-only.

## Priority Queue

### 1. Near-Revenue Board Clearing

Highest leverage this week is moving already-built or nearly-ready prospects into clean, approved outreach decisions.

- `harrison-sons-electrical`: Jesse reported the postcard retry worked after the public CRM Poplar first-name patch. Next safe action is read-only verification of CRM/Poplar event state, then status artifact update. Do not infer email follow-up or stage truth without evidence.
- `intire-mobile-tire-shop`: GTM-14 technical readiness passed. Next action is a Jesse decision: move toward `outreach_staged` or hold, and approve postcard/email/both as separate channel actions.
- QA-approved and asset-ready batch: `smartwire-solutions`, `cityboys`, `dream-steam`, `handy-dandy-atlanta`. Next action is to prepare one send packet per prospect with current preview URL, claim lookup, checkout URL, desktop/mobile screenshot, hero, payload preview, and channel recommendation. No sends without approval.
- Needs-approval and asset-ready review candidates: `24-hrs-mobile-tire-services`, `bravo-plumbing-solutions`, `browning-electrical-services`, `chrissy-s-mobile-detailing`, `rooter-pro-plumbing-drain`, `thermys-mobile-tire-and-brakes`, `tuxedo-mechanical-plumbing`. Next action is Jesse-facing review packets, not sends.

### 2. Active Blocker Repair

Post-Build reports 38/45 active non-dead prospects ready across key asset/preflight checks, with 7 active blockers.

- `raiden-electrical`: preview URL/source repair needed because `https://preview.gtmdot.com/raiden-electrical/` fails DNS; screenshots cannot be generated from the CRM source URL.
- `piedmont-tires`: postcard assets are ready, but CRM payload fails because ZIP is missing.
- `forest-park-collision`: mailing fields incomplete.
- `pine-peach-painting`: mailing fields incomplete.
- `jack-glass-electric`: mailing fields incomplete.
- `total-repair-service`: mailing fields incomplete plus separate site-quality/recovery-build blocker.
- `sandy-springs-plumbing`: mailing fields blank despite `outreach_sent`; treat as channel/data reconciliation, not a postcard asset issue.

Safe work: collect evidence, identify likely authoritative public sources, draft field repair packets, and route to Jesse for approval.  
Not safe without approval: writing CRM fields, changing stage, sending, or deciding disputed business truth.

### 3. Outreach Scale Blockers

- Prospect detail API can still show stale `postcardStatus` even when outreach events prove postcard submitted. This needs local code diagnosis and a no-deploy fix proposal.
- Reply monitoring to `hello@gtmdot.com` is not proven end-to-end. Email follow-up scale should remain paused unless Jesse accepts manual-monitoring risk or a safe internal test proves pause-on-reply.
- Atlanta Expert Appliance was reconciled to `outreach_sent` after a submitted postcard, but `nextEmailAt` remains `null`. Do not schedule email without a separate decision.

### 4. CRM v2 Lab Alignment

CRM v2 is useful this week as a read-only lab for the problems we keep hitting:

- Channel truth separate from CRM stage.
- Provider truth separate from CRM event truth.
- Stale-note handling.
- Paperclip issue/artifact links.
- Payload 400 and address/name validation warnings.
- Reply monitoring state and pause-on-reply visibility.
- New prospect routing state from intake to R1VS to Post-Build to Outreach.

CRM v2 should not replace live CRM while Jesse is remote.

### 5. GTMDot Marketing Site

The marketing site has local, undeployed conversion-flow updates. Keep this lane local unless Jesse approves deployment.

Safe work:
- Draft multi-page GTMDot.com roadmap.
- Tighten local copy/design.
- Verify claim-code-to-checkout in safe test mode.

Hold:
- Public deploy.
- Checkout/billing/pricing logic changes.
- DNS/hosting changes.

### 6. Pre-Build / R1VS / Browserbase

Pre-Build remains ready but subordinate to board clearing.

Safe work:
- Finalize reusable pre-build template.
- Standardize Browserbase evidence packet schema.
- Prepare R1VS packet template.
- Keep R1VS trigger contract: Paperclip issue plus Git/message build packet, not Telegram alone.

Hold unless board clearing stabilizes:
- Mbanugo continuation.
- New clean prospect build queue.
- Any R1VS build start without a canonical packet.

### 7. Experiments

Experiments remain local-only R&D.

Safe work:
- AI receptionist dry-run prompt QA.
- Graduation checklist.
- Candidate-fit matrix.

Hold:
- Retell live resources.
- Twilio/Resend tests.
- Worker deploys.
- Chat embeds.
- Billing/Stripe.
- Any customer-facing pilot.

## What Codex Can Keep Doing While Jesse Is Remote

Allowed under the current safe operating model:

- Read lane status files and recent artifacts.
- Read-only CRM/API/provider/file audits where credentials and access already exist.
- Generate coordination artifacts, send packets, blocker packets, and status updates under `gtmdot-sites/messages`.
- Run non-destructive verification commands.
- Run Paperclip, dispatcher, and Telegram health checks.
- Build local-only code patches and test them without deploying.
- Prepare exact approval text for Jesse to approve from mobile.
- Create Bruce/R1VS/Post-Build/Outreach packets, but not ask them to perform prohibited actions.
- Use Browserbase/Scrapfly only for evidence packets where previously approved, not CRM truth.

## Actions That Still Need Explicit Jesse Approval

- CRM/Supabase writes or stage moves.
- Paperclip issue/comment/status mutations.
- Poplar postcard submit/resubmit/retry.
- Resend email sends or sequence resume.
- SMS sends.
- Prospect/customer contact.
- Production deploys.
- Public GTMDot marketing-site deploy.
- DNS/domain/hosting/billing changes.
- Stripe changes.
- Git pushes.
- Strategic business-truth decisions, including disputed contact/address/owner/email/service claims.

## Recommended Daily Loop

1. Read `quarterback-latest.md`, `paperclip-runtime-latest.md`, newest dispatcher digest, and latest lane statuses.
2. Refresh read-only provider/CRM truth for the top 3 near-revenue prospects.
3. Produce or update one artifact per decision: send packet, blocker packet, repair packet, or approval packet.
4. Update `quarterback-latest.md` with next action and approval queue.
5. If approval is needed, ask Jesse for one exact approval at a time from mobile.
6. If no approval is needed, continue evidence gathering, local-only remediation, or packet preparation.

## Best Next Moves

1. Verify Harrison's successful postcard state read-only, then record it as cleared or follow-up-needed.
2. Prepare Jesse approval packet for InTire: hold vs postcard vs email vs both.
3. Prepare send-readiness packets for `smartwire-solutions`, `cityboys`, `dream-steam`, and `handy-dandy-atlanta`.
4. Open repair packets for the 7 active blockers, especially mailing-field `payload_400` cases.
5. Draft CRM v2 field/API contract for stale notes, provider events, reply monitoring, Paperclip links, and payload validation warnings.
6. Keep Paperclip/dispatcher/Telegram health monitored so coordination does not collapse back into manual copy-paste.

## Remote Approval Pattern

Use this pattern when an action is ready:

```text
Approved: <exact prospect/lane/action>.

Allowed:
1. <specific file/API/provider action>
2. <specific verification>
3. <specific artifact/status update>

Still prohibited:
CRM writes unless listed above, Paperclip mutations unless listed above, deploys unless listed above, Poplar/Resend/SMS sends unless listed above, prospect/customer contact, git push, DNS/domain/hosting/billing changes, and Stripe actions.
```

## Immediate Ask For Lanes

Each lane should stop sending broad summaries and instead produce:

- Current state.
- Closest-to-revenue item.
- Current blocker.
- Exact safe next action.
- Exact approval needed, if any.
- Artifact path.
- No-action statement.

That shape lets the coordinator route work without Jesse becoming the clipboard.
