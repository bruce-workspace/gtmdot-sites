Lane: Experiments
Session: Experimental Modules lane / voice-chat module worktree
Updated: 2026-05-23T15:17:28-04:00
Owner: Codex Experiments lane
Mode: parked as local-only R&D; daily/spare-bandwidth cadence

Current objective:
Keep experimental GTMDot features isolated from production while clarifying what is real, what is only dry-run proven, and what can be advanced safely during Jesse's away-mode week.

Current lane status:
Experiments is parked as local-only R&D while board-clearing lanes take priority. Per `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-remote-week-cadence-protocol.md`, this lane should update daily or only when spare bandwidth produces meaningful local-only progress. The active experiment remains the local `gtmdot/ai-receptionist/` prototype. Elfsight has been evaluated as a future module for new GTMDot sites and CRM v2 planning only, not current pipeline sites or board clearing. Manual Elfsight embed snippets look simpler than SDK integration for a near-term MVP; the SDK appears more useful later if CRM v2 needs embedded catalog/editor/widget-management flows. No live Elfsight, Retell, Twilio, Resend, Stripe, call forwarding, or prospect-site embed has been executed.

Active blockers:
- `gtmdot/ai-receptionist/worker/customer-registry.js` is still empty, so no agent is wired to an owner record.
- `gtmdot/ai-receptionist/worker/wrangler.toml` still has a placeholder KV namespace id and the worker has never been deployed.
- `gtmdot/ai-receptionist/scripts/provision_agent.py --commit` has never been run against the real Retell API, so endpoint/body assumptions remain unproven.
- The safest verified path today is offline only; the documented webhook test path would send SMS/email if real secrets and registry entries are used.
- Extracted FAQ content can conflict with intake guardrails like `never_quote`, after-hours policy, and callback promises, so prompt QA is still required per target prospect.

Prospects/items closest to revenue:
- AI Receptionist add-on itself: documented as `$200/mo bundled` or `$125/mo standalone`, but still not approved for live sell-through or activation.
- Elfsight-powered demo lead-capture form for future new GTMDot sites: promising as a conversion demo, but not approved for current pipeline retrofits or live preview placement.
- `bobs-hvac`: strongest local dry-run seed. KB extraction and prompt rendering both succeeded locally.
- `thompsons-fence`: second local seed with fixture intake + extractor coverage; useful for proving chat/voice prompt generation, but still fixture-grade and not live-approved.

What can be safely advanced without Jesse present:
- Only if spare bandwidth exists after board-clearing lanes: tighten the graduation checklist.
- Only if spare bandwidth exists after board-clearing lanes: add additional dry-run-only candidate notes.
- Only if spare bandwidth exists after board-clearing lanes: surface CRM v2 field/UX implications for future AI Receptionist status.
- Only if spare bandwidth exists after board-clearing lanes: refine the local-only Elfsight demo-form MVP spec and CRM v2 widget field/UX notes for future new sites only.
- Otherwise hold and do not advance the experiment.

What requires explicit Jesse approval:
- Any move beyond local-only R&D.
- Any Elfsight widget creation, embed, public preview placement, live routing, or customer-facing demo.
- Any attempt to retrofit Elfsight onto current pipeline sites.
- Any `--commit` run that creates live Retell resources or buys a phone number.
- Any Cloudflare Worker deploy, secret setup, KV creation, or webhook endpoint exposure.
- Any chat-widget insertion into a prospect site or production GTMDot site.
- Any live phone forwarding, SMS/email notification test, prospect/customer contact, vendor/billing/Stripe action, or production graduation decision.
- Any decision to treat the AI receptionist as revenue-ready, board-clearing work, or a real offer to route across lanes.

Files/artifacts changed:
- Added `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-experiments-elfsight-widget-layer-evaluation.md`.
- Added `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-experiments-ai-receptionist-local-graduation-packet.md`.
- Updated `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/experiments-latest.md`.
- No experiment code or production files changed in this update.

Latest artifacts:
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-experiments-elfsight-widget-layer-evaluation.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-experiments-ai-receptionist-local-graduation-packet.md`
- `/Users/bruce/.openclaw/workspace/gtmdot/.claude/worktrees/goofy-newton-1d9241/gtmdot/ai-receptionist/README.md`
- `/Users/bruce/.openclaw/workspace/gtmdot/.claude/worktrees/goofy-newton-1d9241/gtmdot/ai-receptionist/HANDOFF.md`
- `/Users/bruce/.openclaw/workspace/gtmdot/.claude/worktrees/goofy-newton-1d9241/gtmdot/ai-receptionist/worker/index.js`
- `/Users/bruce/.openclaw/workspace/gtmdot/.claude/worktrees/goofy-newton-1d9241/gtmdot/ai-receptionist/scripts/provision_agent.py`
- `/Users/bruce/.openclaw/workspace/gtmdot/.claude/worktrees/goofy-newton-1d9241/gtmdot/ai-receptionist/scripts/out/bobs-hvac.kb.json`
- `/Users/bruce/.openclaw/workspace/gtmdot/.claude/worktrees/goofy-newton-1d9241/gtmdot/ai-receptionist/scripts/out/thompsons-fence.kb.json`

Paperclip issues:
- No lane-owned Paperclip mutations made.
- Quarterback previously reported no experiment GTM ids detected; this lane is still artifact-led rather than Paperclip-led.

Actions completed since last update:
- Recorded updated Elfsight direction: future new-site module and CRM v2 planning only; do not prioritize for current pipeline or board clearing.
- Evaluated Elfsight as a future GTMDot widget/add-on layer using public Elfsight docs and the provided Embed SDK reference.
- Created the local-only Elfsight widget layer evaluation artifact, including recommended MVP path and CRM v2 field/UX implications.
- Recorded the remote-week cadence protocol for Experiments: daily or spare-bandwidth-only updates, no 15-minute loop unless an urgent scheduled email/provider incident changes the coordinator's needs.
- Recorded Jesse's remote-week hold directive: Experiments remains parked as local-only R&D unless spare bandwidth exists after board-clearing work.
- Read the local experiment files enough to map the current state of the voice/chat module worktree.
- Verified that the extractor and provisioning dry-run path work locally without touching live systems.
- Confirmed the experiment remains isolated from production and is still not wired to any live owner/contact path.
- Ran local-only dry-run prompt QA for `bobs-hvac` and `thompsons-fence`.
- Created the AI Receptionist local graduation packet with criteria, candidate-fit matrix, and dry-run QA notes.
- Refreshed this lane status for away-mode coordination.

Actions explicitly not performed:
- No Elfsight widget creation, dashboard action, embed, or live routing.
- No Retell API calls.
- No Twilio/Resend sends.
- No live phone forwarding or chat tests.
- No prospect/customer contact.
- No CRM/Supabase/Paperclip writes.
- No production site edits.
- No deploys, DNS/domain changes, billing, or Stripe actions.

Recommended next 3 actions:
1. Hold Experiments while board-clearing lanes take priority.
2. If spare bandwidth exists, tighten the existing graduation checklist and CRM v2 widget-state notes for AI Receptionist and Elfsight-style add-ons.
3. If spare bandwidth still exists, add dry-run-only candidate notes; do not touch live Elfsight, Retell, Twilio, Resend, Worker, widget, billing, CRM, Paperclip, or prospect-facing paths.

Cross-lane impacts:
- GTMDot Platform should only be involved once the experiment needs CRM/channel-state representation or productized field contracts.
- Outreach should ignore this lane unless Jesse explicitly approves a live offer, live channel, or customer-facing pilot.
- Pre-Build/Post-Build can supply candidate sites for offline dry-run prompt QA, but no production edits or staging moves should be driven by this lane during away-mode.

Notify:
Main Codex coordinator / quarterback. Loop in GTMDot Platform only if the coordinator wants a graduation checklist tied to CRM/product state.
