---
from: jesse (physically at the Mini as of 15:16 EDT)
to: mini claude (reading this ON the Mac Mini right now)
date: 2026-04-19
subject: WAKEUP — read new docs + ACK + start a /loop so this doesn't happen again
priority: URGENT — unblock pipeline
---

# What happened

R1VS pushed 3 critical docs/messages between 09:47 and 09:53 this morning. Your cron pulled them. But your Claude Code session has been idle — cron ≠ active Claude. It's now 15:16, roughly 5.5 hours later, and there's been no ACK from you.

I'm sitting at the Mini right now. Paste this message into your Claude Code session and process it.

# Three immediate asks

### 1. Pull latest main

```bash
cd /path/to/gtmdot-sites   # wherever the repo is on the Mini
git checkout main
git pull origin main
```

### 2. Read these three files, in order

- **`DESIGN-HEURISTICS.md`** (repo root) — newly added. Mandatory reference for every site decision. Global scope, not just trade sites.
- **`messages/2026-04-19-0947-r1vs-jesse-DIRECTIVE-design-heuristics-mandatory.md`** — the standing directive. States the heuristics doc is authoritative and gives you the pre-read order for every session.
- **`messages/2026-04-19-0953-r1vs-jesse-to-mini-replication-mechanism.md`** — the specific 5 tests you need to apply on every site work + the commit-message citation pattern.

### 3. Write an ACK to the repo

Create a file at `messages/YYYY-MM-DD-HHMM-mini-to-r1vs-ack-heuristics.md` that confirms:

- You read `DESIGN-HEURISTICS.md` end-to-end
- You'll apply the commit-message citation pattern going forward (cite which `DESIGN-HEURISTICS.md` sections each commit applies)
- You accept the 5 replication-point tests as standing pre-ship validation:
  1. Icon selection test (§1) — cite the `ICON-MAPPING.md` entry for every service card icon
  2. Photo wiring test (§2) — write caption **before** picking the photo
  3. Pull-quote gap test (§3) — if R1VS hasn't polished a site's pull quotes, DO NOT fill with generic; leave blank and flag back to R1VS
  4. Stats de-dup test (§4) — count hero-vs-story stat matches before deploying
  5. Content integrity grep (§5) — scan review-feed for placeholder-as-reviewer patterns ("Company Mission" etc.)
- Any questions or gaps you see in the doc
- Commit + push this ACK to main

# Fourth ask — prevent this from happening again

Once you've ACKed, start a `/loop` on your end so you automatically poll for new R1VS + Jesse messages. Paste this into your Claude Code session after the ACK:

```
/loop Watch messages/ for new r1vs-*.md or jesse-*.md files every cycle. When new messages land, read them, take the requested action, and write a response message back to messages/. Between messages, process any pending Bruce enrichment (bruce-to-mini-*-enriched.md) by wiring photos into HTML per DESIGN-HEURISTICS.md §2 (caption-content matching), applying mechanical polish per the revised contract d004e79 (marquee 58s, review feed 60s, footer mobile 2-col, form upload field, story breakpoint 900px, em-dash cleanup), and deploying to Cloudflare Pages. Cite which DESIGN-HEURISTICS.md sections your commit applies. Read DESIGN-HEURISTICS.md + CLAUDE.md + SKILL.md + ICON-MAPPING.md at the start of each site. Stop and write a summary if Jesse explicitly says to stop, or if you hit a blocker that needs R1VS or Bruce.
```

Self-paced (no interval) — you decide your own cadence. Default fallback delay: 1200s (20 min) to match your existing cron.

# Status snapshot (from R1VS's side)

- 24 sites polished by R1VS overnight + this morning (3 sample + 11 /loop + 3 urgent rebuilds + 7 grandfathered)
- All 3 urgent rebuild branches ready for redeploy — moonstone / perez-pools / appliance-gals (claim codes preserved)
- Revised 1-pass contract proposed (R1VS does research + HTML + content-craft + photo-intent in a single pass; Mini wires + polishes + deploys; Bruce only when needed) — details in the DIRECTIVE message
- handy-dandy-atlanta retry requested from Bruce (still 0 verbatim reviews)
- Bruce has been actively enriching — multiple `bruce-to-mini-*-enriched.md` messages landed today

# Why this matters

Jesse's direct quote from minutes ago: *"It's been hours. There is no reason the Mini has not picked it up."*

The fix isn't more messages — the fix is you running a `/loop` so future R1VS pushes don't sit unread. The cron pulls; the loop acts. Both are needed.

Once you've ACKed + started the loop, the pipeline runs itself.

— Jesse + R1VS
