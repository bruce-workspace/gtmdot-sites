# GTMDot New Chat Structure and Transfer Briefs

Date: 2026-06-09
Purpose: preserve GTMDot operating context while the main chat is near context limits.

## Plain English Summary

The current chat has become three things at once:

1. GTMDot business and site-production memory.
2. CRM v2 product rebuild direction.
3. Cross-lane operations coordination for Pre-Build, Post-Build, Outreach, Platform, Experiments, and Paperclip.

That is too much for one chat. The safer move is not to start one giant replacement chat. Start one lightweight quarterback chat plus focused lane chats, and point them at durable files instead of relying on chat memory.

## Current Folder Map

### `/Users/bruce/.openclaw/workspace/gtmdot`

Legacy/canonical GTMDot operating folder.

Contains:
- Business/product docs: `CLAUDE.md`, `SITE-BUILD-PROCESS-V2.md`, `DESIGN-STANDARDS.md`, `ICON-MAPPING.md`, `INDUSTRY-REFERENCE.md`.
- Prospect research: `research/`.
- Site source/content and older site artifacts: `sites/`, `deploy-sites/`, `deploy/`, `v2-site/`.
- Postcard assets and generated postcard HTML/images: `postcards/`, `postcard-previews/`, `paper-assets/`, `paper-exports/`.
- Outreach/email assets: `email-sequences/`, `email-assets/`, `email-worker/`.
- Build/deploy/check scripts: `scripts/`, including `deploy-site.sh`, `crm-sync-watcher.js`, `send-poplar.js`, `sequence-scheduler.js`.

Use for:
- Site builds.
- Postcard asset work.
- GTMDot marketing-site / checkout / legal/pricing context.
- Historical research and source files.

### `/Users/bruce/.openclaw/workspace/gtmdot-sites`

Newer operations/control-plane folder.

Contains:
- Lane status ledger: `messages/status/`.
- Dispatcher artifacts: `messages/dispatcher/`.
- Cross-lane handoff messages: `messages/`.
- R1VS/site-builder pipeline: `PIPELINE.md`, `R1VS-REBUILD-BRIEF.md`, `HANDOFF-CONTRACT.md`, `SKILL.md`.
- Build/enrichment scripts: `scripts/`.
- Per-site operational packets: `sites/`.
- Proposals/reports: `proposals/`, `reports/`.

Use for:
- Current GTMDot operating memory.
- Lane status and handoffs.
- Paperclip/dispatcher coordination.
- Pre-Build/Post-Build/Outreach/Platform/Experiments status.

### `/Users/bruce/.openclaw/workspace/brucecom-v3`

Current CRM/live app codebase.

Contains:
- Public CRM/API routes.
- Local CRM v2 lab at `src/app/lab/crm-v2/`.
- CRM v2 docs at `docs/CRM-V2-PRODUCT-BRIEF.md`.

Use for:
- CRM v2 rebuild.
- Local app verification at `http://127.0.0.1:3001/lab/crm-v2`.
- CRM/API changes, only when explicitly approved.

### `/Users/bruce/.openclaw/workspace/gtmdot-crm`

Older CRM project/reference folder.

Contains:
- Prior CRM implementation/tasks.
- Historical build briefs and tasks.

Use for:
- Reference/mining old CRM requirements only.
- Avoid making this the active CRM v2 home unless explicitly decided.

### `/Users/bruce/.openclaw/workspace/paperclip-sandbox`

Paperclip dry-run/artifact sandbox.

Use for:
- Safe packet artifacts.
- Paperclip experiments or rehydration outputs.
- No live Paperclip mutation unless explicitly approved.

## Recommended New Conversation Structure

### 1. GTMDot Quarterback / Control Plane

This should be the new main chat.

Scope:
- Read lane statuses.
- Decide which lane needs work next.
- Keep approval boundaries clean.
- Update durable handoff/status files.
- Route work to focused chats.

Start with:
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md`
- This file.

Do not do deep implementation here unless the change is tiny. This chat should stay context-light.

### 2. CRM v2 Product Rebuild

Scope:
- Rebuild `/lab/crm-v2` around Jesse-actionable decisions and agent/Paperclip orchestration.
- Compact cards.
- Compact company cockpit.
- Clear owner/next action.
- Hide non-actionable raw metadata.

Start with:
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/docs/CRM-V2-PRODUCT-BRIEF.md`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/`
- CRM brief below.

### 3. GTMDot Site Factory / Pre-Build

Scope:
- Prospect intake.
- Research packets.
- Browserbase evidence.
- R1VS build packets.
- Source-of-truth checks.

Start with:
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/pre-build-coordination-latest.md`
- `/Users/bruce/.openclaw/workspace/gtmdot/SITE-BUILD-PROCESS-V2.md`
- `/Users/bruce/.openclaw/workspace/gtmdot/CLAUDE.md`

### 4. Post-Build + Outreach Operations

Scope:
- Current site fixes.
- Postcard proofs/assets.
- Poplar provider truth.
- Resend/email sequences.
- Reply/bounce monitoring.
- Explicit send/retry approval packets.

Start with:
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md`

This can be one chat unless it becomes too large; if split, keep Post-Build about assets/fixes and Outreach about provider/channel/reply truth.

### 5. Experiments

Scope:
- AI Receptionist.
- Elfsight/widgets.
- Future add-ons.
- Local-only R&D.

Start with:
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/experiments-latest.md`

Keep parked unless board-clearing work is stable.

## Folder Structure Recommendation

Do not physically reorganize the active folders yet. Too many scripts, status files, and handoffs already reference absolute paths.

Instead:

1. Treat `gtmdot-sites/messages/status/` as the canonical memory spine.
2. Put new handoff/transfer docs in `gtmdot-sites/messages/`.
3. Keep CRM v2 code in `brucecom-v3/src/app/lab/crm-v2/`.
4. Keep site/postcard/build assets in `gtmdot/`.
5. Keep operational lane artifacts in `gtmdot-sites/`.
6. Later, create an index doc that links the canonical locations instead of moving files.

Suggested future index:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/START-HERE.md`

That file should point new chats to the five active lane status files and this transfer brief.

## Brief 1: CRM v2 Rebuild

### Where the work lives

Code:
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/`

Local URL:
- `http://127.0.0.1:3001/lab/crm-v2`

Current state:
- CRM v2 is lab-only.
- It reads current CRM prospect data.
- It must not write CRM/Supabase, mutate Paperclip, send via Poplar/Resend/SMS, contact prospects, deploy, or replace production without explicit approval.

Recent issue:
- The implementation is visually improved but still workflow-wrong.
- It feels like a prettier old CRM instead of a decision/orchestration system.

Jesse's core critique:
- Cards show raw URL and claim code even when they are not actionable.
- Cards show labels like `history only`, `open item`, and `missing email` that do not tell Jesse what to do.
- Missing email / needs enrichment should be agent-owned, not Jesse-owned.
- Bad postcard / missing address / source evidence should route through Paperclip/Codex/Bruce, not become ambiguous human work.
- Needs Decision vs Needs Approval is unclear.
- Company pages are far too long and redundant.
- Jesse should not have to inspect an hour of sections per company.

CRM v2 north star:
- The board should answer: who owns the next action, what exactly must happen next, and whether Jesse has to decide anything.

Design direction:
- Default board should be Jesse-actionable, not all-data.
- Agent-owned work should be visible as queued/running/blocked, not presented as Jesse's work.
- Cards should show company, trade, next-action owner, one plain-English next action, and a clear CTA when Jesse must act.
- Hide raw URL, claim code, stale/history-only labels, and raw open-item counts from cards unless directly actionable.
- Company workspace should become a compact decision cockpit above the fold.
- Use tabs or collapsed panels for details/history/diagnostics.
- Advanced diagnostics should not dominate the default company page.

Stage model to clarify:
- Research: agent/intake-owned unless identity/source decision needed.
- Site Built: agent QA/recheck-owned.
- Needs Enrichment: Paperclip/Codex/Bruce-owned by default.
- Needs Decision: first true Jesse human-judgment lane.
- Needs Approval: site/channel ready for Jesse yes/no approval.
- QA Approved: approved, but outreach/channel staging may still be agent-owned.
- Outreach Staged/Sent: operations/provider/reply monitoring; Jesse only sees retry/send/response decisions.
- Out of Pipeline: hidden by default unless disposition is needed.

Next implementation move:
- Rework CRM v2 around `Action owner` and `Jesse required?`.
- Add/derive owner categories: Jesse, Codex, Bruce, Paperclip, Outreach, Provider.
- Replace current company sheet with one-screen decision cockpit plus tabs.
- Move redundant existing panels behind tabs/collapsed debug.

## Brief 2: Non-CRM GTMDot Setup

### Business model

GTMDot builds personalized preview websites for Atlanta local service businesses, then drives them to claim the site through direct mail postcards, email, and claim flows.

Core offer:
- Pay monthly: `$49` first month, then `$149/mo`.
- Make it yours: `$1,999` one-time permanent license.
- Hosting/maintenance add-on: `$99/mo` for one-time buyers.

Canonical contact/business details:
- GTMDot address: `5600 Roswell Rd, Building C, Sandy Springs, GA 30342`.
- GTMDot phone: `(404) 500-8414`.
- Reply/contact email: `hello@gtmdot.com`.
- Checkout/claim flow and pricing are sensitive; do not alter without approval.

### Site build rules

Important files:
- `/Users/bruce/.openclaw/workspace/gtmdot/CLAUDE.md`
- `/Users/bruce/.openclaw/workspace/gtmdot/SITE-BUILD-PROCESS-V2.md`
- `/Users/bruce/.openclaw/workspace/gtmdot/DESIGN-STANDARDS.md`
- `/Users/bruce/.openclaw/workspace/gtmdot/ICON-MAPPING.md`
- `/Users/bruce/.openclaw/workspace/gtmdot/INDUSTRY-REFERENCE.md`

Hard rules:
- Check open CRM flags before new site work.
- Use `./scripts/deploy-site.sh [slug]`; do not call Wrangler directly for GTMDot sites.
- Real data only.
- Verbatim reviews only, with real names.
- GBP photos first, then approved fallback sources.
- No invented reviews, awards, claims, owner names, emails, or unsupported facts.
- Every service icon must come from `ICON-MAPPING.md`.
- Pricing must be current: `$49/$149`, not old `$99/$299`.
- Claim bar, popup, checkout URL, TCPA consent, cookie banner, GTMDot footer address, and upload-enabled quote form matter.

Gold standard:
- `sandy-springs-plumbing-share.pages.dev`

### Current operational lanes

Quarterback:
- Current state lives in `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md`.
- Dispatcher B1.0 generated dry-run digest only.
- No CRM/Paperclip/deploy/send/contact mutations were performed by the dispatcher.
- Active lanes are stale and need refresh.

Pre-Build:
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/pre-build-coordination-latest.md`.
- Focus: evidence packets, Browserbase evidence, R1VS build packets, source-of-truth checks.
- Board clearing takes priority over new pre-build work.
- Mbanugo remains unresolved/pilot context but should not distract unless prioritized.

Post-Build:
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md`.
- Current state is stale/expired-cadence safety hold.
- Needs fresh verification before acting on old repair/send assumptions.
- Prior repair queue included Cityboys, Piedmont Tires, Rooter Pro, Thermys, Tuxedo, Chrissy's.

Outreach:
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md`.
- Poplar provider-state fix was deployed.
- Known suppressed/exception handling was improved.
- Provider/channel truth remains critical.
- No sends, retries, email resume, CRM truth edits, or prospect contact without explicit approval.
- Existing issues include provider exceptions, reply monitoring risk, stage/channel mismatches, and held send candidates.

Experiments:
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/experiments-latest.md`.
- AI Receptionist and Elfsight-style widget work is local-only/parked.
- Do not move to live widgets, Retell/Twilio/Resend, worker deploys, billing, or prospect-facing tests without explicit approval.

### Paperclip / orchestration principle

Paperclip should be treated as the durable orchestrator for:
- enrichment,
- site repair,
- postcard repair,
- provider incident handling,
- stale-note revalidation,
- decision packets,
- audit trail.

But until safe-update mode is explicitly approved:
- write evidence packets and handoff files,
- do not mutate Paperclip live state.

### Global guardrails

Unless explicitly approved:
- No CRM/Supabase writes.
- No Paperclip mutations.
- No Poplar submits/retries.
- No Resend/email sends or sequence resumes.
- No SMS.
- No prospect/customer contact.
- No deploys or production replacements.
- No DNS/domain/hosting/billing/Stripe changes.
- No git push.

## Recommended First Prompt for the New Quarterback Chat

Paste this:

```text
You are taking over as GTMDot Quarterback. Start by reading:

1. /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-new-chat-structure-and-transfer-briefs.md
2. /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md
3. /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md
4. /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/pre-build-coordination-latest.md
5. /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md
6. /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md
7. /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/experiments-latest.md

Do not mutate CRM, Paperclip, providers, sends, deployments, DNS, billing, Stripe, git, or prospect/customer contact without explicit approval.

Your first job is to recommend which focused chat/lane should be opened next and what exact brief should be given to it.
```

## Recommended First Prompt for the CRM v2 Chat

Paste this:

```text
You are taking over the GTMDot CRM v2 rebuild.

Read:
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-new-chat-structure-and-transfer-briefs.md
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md
- /Users/bruce/.openclaw/workspace/brucecom-v3/docs/CRM-V2-PRODUCT-BRIEF.md
- /Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/

Core critique to solve:
The current CRM v2 is visually improved but workflow-wrong. Cards and company pages still expose too much raw CRM data and too little decision clarity. Rebuild around next-action owner and whether Jesse is required. Agent-owned work should be orchestrated through Paperclip/Codex/Bruce/OpenClaw, not displayed as Jesse's manual workload.

Do not preserve the current long company page structure just because it exists.
Do not perform CRM/Supabase writes, Paperclip mutations, sends, deploys, provider calls, or prospect/customer contact without explicit approval.
```

