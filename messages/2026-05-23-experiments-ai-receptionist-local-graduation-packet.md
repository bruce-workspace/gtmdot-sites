# Experiments - AI Receptionist Local Graduation Packet

Updated: 2026-05-23T12:47:01-04:00
Owner: Codex Experiments lane
Mode: local-only coordination artifact
Source lane: `/Users/bruce/.openclaw/workspace/gtmdot/.claude/worktrees/goofy-newton-1d9241/gtmdot/ai-receptionist/`

## Purpose

Prepare the AI receptionist experiment for a future Jesse decision without touching production systems. This packet is intentionally local-only: it documents graduation criteria, candidate fit, and prompt QA notes from dry-run checks.

## Current State

The AI receptionist prototype exists as a local Retell voice/chat experiment with:

- Cloudflare Worker webhook scaffold for Retell events.
- Twilio SMS and Resend email notification code paths.
- Empty customer registry.
- Placeholder Cloudflare KV id.
- Retell provisioning script with dry-run and commit modes.
- Chat widget snippet template.
- Intake and carrier-forwarding onboarding docs.
- Fixture KB/intake files for `bobs-hvac` and `thompsons-fence`.

No live Retell, Twilio, Resend, Stripe, Cloudflare deploy, phone forwarding, chat widget, CRM, Paperclip, outreach, or customer-contact action has been performed by this lane.

## Graduation Criteria

Before this experiment can move from local R&D to a live pilot, the coordinator should require all of the following:

- Jesse explicitly approves a live pilot prospect and channels: voice, chat, or both.
- Jesse explicitly approves vendor resource creation: Retell LLM, voice agent, chat agent, and any phone number purchase.
- A test-only customer registry entry exists with owner phone/email values controlled by GTMDot, not a real prospect owner.
- Cloudflare KV namespace, Worker secrets, and Worker deploy are approved as a separate infrastructure action.
- Retell webhook signature format is verified against a live signed event before routing any real lead notification.
- Retell `post_call_analysis_data` shape is verified against a live Retell response.
- Twilio and Resend notification tests are performed only to GTMDot-controlled destinations.
- Chat widget embed is tested on a local or non-production page before any prospect site.
- Prompt QA passes for service area, pricing, after-hours policy, callback promises, and reviewer/phone-number wording.
- Pricing/offer language is approved before the feature appears in GTMDot marketing, checkout, outreach, or CRM.
- Cross-lane routing is documented: Platform owns product/CRM representation, Outreach owns customer-facing channel use, Post-Build owns site embed readiness, Experiments owns R&D notes only.

## Candidate-Fit Matrix

| Candidate | Local evidence | Fit | Current risk | Safe next local-only step |
| --- | --- | --- | --- | --- |
| `bobs-hvac` | Extractor returns business name, phone, city, service area, rating, 4 services, 4 FAQs. Provisioning dry-run renders complete voice/chat request bodies. | Strongest seed for offline QA because HVAC has missed-call urgency and complete extracted structure. | FAQs include `1-2 hours`, `$49 diagnostic fee`, and "upfront repair quote" language that conflicts with never-quote and callback guardrails. | Create a spoken-tone FAQ cleanup note, then re-run dry-run against cleaned local fixture only. |
| `thompsons-fence` | Fixture intake exists and provisioning dry-run renders voice/chat request bodies. | Useful second seed because fencing exercises estimate-heavy and material-choice guardrails. | Dry-run flags missing `kb.service_area`; FAQs include reviewer names, a phone number, "free estimate", "straightforward price", and "honest pricing" language that should not be spoken by the AI before intake confirmation. | Add a local QA note requiring service-area capture and FAQ rewrite before any live pilot. |
| Other current near-revenue prospects | Not checked in this run. | Candidate fit should be evaluated only after board-clearing packets are handled. | Experiments must not pull Post-Build/Outreach prospects into production pilot decisions during away-mode. | If spare bandwidth exists, run extractor plus dry-run only, then record prompt conflicts without changing production files. |

## Dry-Run Prompt QA Notes

`bobs-hvac`:

- Dry-run command completed locally with no Retell API calls.
- Prompt rendered for both voice and chat.
- Service area is present: Atlanta, Roswell, Alpharetta, Sandy Springs, Dunwoody, Marietta.
- QA issue: emergency FAQ promises response timing while intake says after-hours leads return first thing in the morning unless emergency.
- QA issue: diagnostic FAQ includes an exact dollar amount and fee credit language while intake says never quote exact dollar prices.
- QA issue: service copy references "upfront pricing" and warranty wording; these need an owner-approved voice-safe version before pilot.

`thompsons-fence`:

- Dry-run command completed locally with no Retell API calls.
- Prompt rendered for both voice and chat.
- Missing-field warning fired for `kb.service_area`.
- QA issue: FAQ answers mention individual reviewers by name; voice/chat agent should avoid reading reviewer names as proof.
- QA issue: FAQ answers tell callers to call a phone number even though the AI is already handling the interaction.
- QA issue: free estimate and straightforward price wording can undermine the never-quote rule.

## Exact Approval Needed From Jesse

No approval is needed for further local-only dry-run QA notes.

Approval is required before any of these actions:

- Run `provision_agent.py --commit`.
- Create live Retell resources or buy/route a Retell phone number.
- Create Cloudflare KV, set Worker secrets, or deploy the Worker.
- Send Twilio SMS or Resend email, even to internal numbers, unless the destination and purpose are explicitly approved.
- Add a chat widget to any prospect or production site.
- Contact a prospect/customer or ask them to configure carrier forwarding.
- Add pricing/checkout/Stripe/billing support.
- Present AI Receptionist as a live revenue offer.

## Safe Next Action

Keep the experiment isolated and use it only for local readiness work. The next useful local-only action is to create a small prompt-QA checklist that can be applied to each candidate KB before any live pilot approval packet is drafted.

## No-Action Statement

No CRM/Supabase writes, Paperclip mutations, deploys, Poplar/Resend/SMS sends, Retell/Twilio/Resend resource creation, phone forwarding, chat embeds, prospect/customer contact, git pushes, DNS/domain/hosting/billing changes, Stripe actions, or production-impacting edits were performed.
