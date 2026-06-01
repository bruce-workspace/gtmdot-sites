# Codex Remote-Week High-Autonomy Approval - 2026-05-23

Approved by: Jesse  
Applies to: Codex / GTMDot quarterback  
Effective: 2026-05-23  
Expires: 2026-05-30 23:59:59 America/New_York, unless revoked earlier  

## Primary Goal

Keep GTMDot board-clearing, outreach readiness, CRM v2 sandbox, Paperclip/dispatcher coordination, and local repair work moving while Jesse is remote.

## Approved Autonomy

Codex may:

- Read and audit local files, CRM/API/provider state, Paperclip runtime state, lane status files, logs, and artifacts.
- Create, update, and organize coordination artifacts, status files, send packets, blocker packets, repair packets, runbooks, scripts, and local diagnostics under GTMDot workspaces.
- Run non-destructive verification commands, builds, tests, type checks, lint checks, local servers, local scripts, and read-only API checks.
- Make local-only code changes, UI changes, scripts, diagnostics, and sandbox changes when they do not deploy, send, write CRM truth, contact prospects, or alter production state.
- Continue CRM v2 sandbox development under `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/`, including refactors, components, read-only API consumers, derived models, and local verification.
- Continue Paperclip/dispatcher/Telegram health checks and local control-plane improvements that do not mutate Paperclip issues or send messages.
- Prepare and update Post-Build/Outreach readiness packets for prospects.
- Prepare source-backed field repair packets for missing mailing/contact fields, but not write them to CRM without explicit approval.
- Use Browserbase for limited read-only public enrichment and Scrapfly as fallback when Browserbase fails, writing evidence packets only.
- Use approved credentialed APIs in read-only mode for Poplar, Resend, CRM, Supabase, Gmail, Browserbase, and related GTMDot services where credentials already exist.
- For already approved postcard batches, execute only the specifically approved Poplar postcard submissions through existing CRM actions, then verify and write artifacts.
- Request additional approval only when an action crosses into live production, sends, CRM truth, billing, or irreversible external effects.

## Still Requires Separate Explicit Approval

Codex may not do the following without separate explicit approval:

- CRM/Supabase writes, stage moves, contact truth edits, field backfills, or strategic data decisions.
- Paperclip issue/comment/status mutations.
- Poplar postcard submits/resubmits/retries except for a named batch already explicitly approved.
- Resend/email sends, email sequence resume/pause, SMS sends, or prospect/customer contact.
- Deploys, production runtime restarts, production site edits, Cloudflare Pages/Workers deploys, DNS/domain/hosting changes, or billing changes.
- Stripe actions.
- Git pushes, commits, branch publication, PR creation, or destructive git operations.
- Destructive cleanup, file deletion outside clearly temporary generated artifacts, or reverting changes made by other sessions.
- Live Retell/Twilio/AI receptionist resource creation, phone number purchase, chat widget embed, or production experiment graduation.
- Any action that spends money, contacts a prospect/customer, changes public production behavior, or changes CRM truth unless the exact action is separately approved.

## Bounded Postcard Autonomy

For Post-Build/Outreach, Codex may prepare named postcard-only batches for approval.

Execution requires either:

- Separate named batch approval from Jesse.
- Prior explicit approval listing exact slugs.

## Stop-On-Error Rule

If any gate fails, provider returns an error, data conflicts, dirty repo blast radius is unclear, or another agent/session changes the same files in a conflicting way, Codex must stop that action, capture evidence, write a blocker artifact, and ask Jesse.

## Reporting

Codex should keep status current in:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md`
- Relevant lane status files under `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/`

Codex should summarize completed work, blockers, and exact next approvals when Jesse checks in from mobile.
