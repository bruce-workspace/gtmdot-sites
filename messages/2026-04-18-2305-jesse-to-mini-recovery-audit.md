---
from: jesse (not r1vs — r1vs session is dead, see context below)
to: mini
date: 2026-04-18
subject: Recovery audit — what's outstanding that only lived in the (now-dead) R1VS chats?
priority: high (blocking fresh R1VS session startup)
---

## Situation

Three R1VS Claude Desktop chats are poisoned and unrecoverable — all hit the "image exceeds 2000px dimension limit for many-image requests" error. Every retry fails. The chats are effectively killed.

Before spinning up a fresh R1VS session to work through the remaining ~20 un-polished intake branches, I want to make sure nothing important-but-undocumented was only living in those dead chats.

I did an audit on the R1VS side and confirmed the following IS codified in the repo:

- ✅ Division of labor + handoff filename contracts → `CLAUDE.md`
- ✅ Intake API payload spec + error codes → `R1VS-REBUILD-BRIEF.md`
- ✅ Git `messages/` bus + 10-min cron → `proposals/2026-04-17-real-time-comms-problem-brief-v2.md`
- ✅ Phase 1/2/3 build rules + 6 polish rules + pull-quote/team-card specs → `SKILL.md` (just updated, commit `0c7e1b3`, needs push to main)
- ✅ Icon source of truth → `ICON-MAPPING.md`
- ✅ Rebuild queue (51 prospects) → `rebuild-queue.json`

## What I need from you

Please audit your side and confirm, deny, or fill in each of these. Write back to `messages/` as `YYYY-MM-DD-HHMM-mini-to-jesse-recovery-audit-response.md`.

### 1. Protocol refinements not yet in CLAUDE.md or SKILL.md

Are there any decisions we made in the dead R1VS chats (visible to you through my relays or through your cron-pulled messages) that aren't written into CLAUDE.md, SKILL.md, or the `messages/` history yet? Especially anything about:

- Handoff sequencing tweaks
- New fields required in finalization messages
- Any rule changes after the 0955 polish-batch message

### 2. Supabase schema snapshot

What tables does the CRM use that R1VS needs to know about, beyond the `site_intake` table already documented? At minimum:

- Table name
- Key columns (especially state fields, foreign keys)
- State machine values for `current_stage` (I see `received`, `reviewing`, `accepted`, `built`, `deployed`, `ready_for_review`, `qa_approved` scattered across docs — is that the complete list, and in what order?)

A schema dump or pointer to a migration file is fine.

### 3. Claim bar shared template

Current version of the claim bar template you inject post-build:

- Path to the template on your side
- Variables it expects (I see `{{claim_code}}`, `{{checkout_url}}`, `{{preview_name}}` referenced)
- Latest version number / commit SHA so R1VS can ensure nothing in its builds conflicts

### 4. Current pipeline state

Quick status table of the ~20 remaining intake branches that haven't been polished yet. For each:

- Slug
- `current_stage`
- Whether Bruce has delivered photos (enriched) yet
- Whether there are known blockers (e.g. sites with <2 verbatim reviews that can't get full polish rules applied)

This helps R1VS prioritize the retrofit order intelligently instead of just going alphabetical.

### 5. Bruce status

Anything open on Bruce's side that R1VS should know about before starting?

- Any sites with `blocked` enrichment status that need R1VS to do something differently
- Any changes to the photo waterfall rules since the 1710 correction message
- Is Bruce actively running right now, or do I need to wake him?

### 6. Environment variables + secrets

Confirm these exist in a real env file (not just in chat history):

- `INTAKE_BEARER_TOKEN` — used by R1VS to POST to `crm.cloakanddagger.co/api/site-intake`
- `GOOGLE_MAPS_API_KEY`, `FIRECRAWL_API_KEY`, `RECRAFT_API_KEY`, `POPLAR_API_KEY`

Where should R1VS read them from on the MacBook side? (I assume `~/.openclaw/.env` per SKILL.md but that's the Mini path.)

### 7. Anything I'm not thinking of

If you have visibility into decisions, policy changes, or build rules that R1VS referenced in the dead chats but didn't commit — list them here. Better to surface now than have the fresh R1VS session discover a gap mid-build.

## Timing

Not urgent on the minute scale — I won't start the fresh R1VS session until I have your response. Please respond when your next cron cycle catches this (or sooner if you want to kick it off manually). A few hours is fine.

## One administrative note

The SKILL.md commit `0c7e1b3` with the 6 polish rules codified from the batch pass is on the `claude/silly-mclean-e07792` worktree branch, not main. Before R1VS starts retrofitting, I'll cherry-pick it to main (or you can, whichever is easier). Flag if you want me to push it a specific way.

Thanks.

Jesse
