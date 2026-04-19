---
from: mini claude (scheduled pipeline watcher, 15:32 EDT)
to: r1vs + jesse
date: 2026-04-19
subject: ACK — DESIGN-HEURISTICS.md read, directive accepted, 5 replication tests adopted
---

# Acknowledgment

I read `DESIGN-HEURISTICS.md` end-to-end (all 14 sections + pre-amble). This message is the formal ACK requested in both `0947-DIRECTIVE` and `0953-replication-mechanism`.

---

## What I'm confirming

### 1. DESIGN-HEURISTICS.md read in full

All sections:
- **Pre-amble:** Core discipline (read reviews.json + RESEARCH.md + hero stats bar before touching HTML)
- **§1:** Icon selection — Lucide only, ICON-MAPPING.md is authoritative, 48–52px containers, never freestyle
- **§2:** Photo wiring — owner action > stock, gallery = real jobs, Unsplash only for section backgrounds, vertical CSS filter always applied, caption-content matching, `photos/intent.json` spec
- **§3:** Pull quote selection — named tech > specific story > emotional hook, verbatim always, source-tag tells micro-story, thin-review fallback rules
- **§4:** Stats de-dup — four modes (A: team cards / B: callouts in stat slots / C: timeline already there / D: commitment callouts). De-dup math by count.
- **§5:** Content integrity — 100% verbatim reviews, no invented names, no AI-gen review content, verifiable stats
- **§6:** Voice rules — no em dashes in authored copy, named people > generic titles, specific CTAs, active voice
- **§7:** Hero section — subhead states specific differentiator, named owner when possible, verifiable badge, CTA primary = action + secondary = phone
- **§8:** Service cards — lead with symptoms, then capability, then scope. Owner-specific jargon preferred.
- **§9:** FAQ — verbatim from source or skip entirely. No fake questions.
- **§10:** Mobile-first — nav dark always, H1 max 2 lines at 390px, grids stack at 768px, footer 2-col mobile, form upload field on every quote form
- **§11:** Brand colors — extract from logo, one display + one body font, Cormorant Garamond for pull quotes, H1 gradient on line 2 only
- **§12:** What NOT to build — no claim bar, no marquee speed tuning, no footer-mobile CSS, no form-upload HTML, no story-grid breakpoint CSS (all Mini-owned via injector)
- **§13:** Pre-ship 10-item checklist (verbatim reviews, icon mapping, stats de-dup, two pull quotes, attribution context, named owner, verbatim FAQ, no em dashes, tel: links, LocalBusiness schema)
- **§14:** Editorial test — "Would the owner look at this and say someone built this for ME specifically?"

### 2. Commit-message citation pattern — adopted

All future commits from this pipeline will cite which DESIGN-HEURISTICS.md sections apply. Format:

```
polish(slug): photo wire + mechanical pass

- DESIGN-HEURISTICS §2: caption-content matching — hero shows [person], caption references them by name
- DESIGN-HEURISTICS §1: verified all service card icons match ICON-MAPPING.md
- DESIGN-HEURISTICS §10: footer mobile 2-col, H1 clamped to 2 lines at 390px
- DESIGN-HEURISTICS §5: content integrity grep — no placeholder reviewer names found
- DESIGN-HEURISTICS §13: pre-ship checklist — all 10 items verified
- R1VS-owned (not touched): §3 pull quotes, §4 team cards
```

### 3. Five replication-point tests — accepted as standing pre-ship validation

1. **Icon selection test (§1):** For each service card, name the Lucide icon and cite the ICON-MAPPING.md entry. No freestyled icons.
2. **Photo wiring test (§2):** Write the caption BEFORE picking the photo. Caption describes what it must show; then find a Bruce-delivered photo matching that description.
3. **Pull-quote gap test (§3):** If R1VS hasn't polished pull quotes, leave the section empty and flag back to R1VS. No generic fill.
4. **Stats de-dup test (§4):** Before deploy, compare hero-stats (4 values) vs story-highlights (4 values). Count matches. Apply mode A/B/C/D from §4 by count.
5. **Content integrity grep (§5):** Scan review-feed for reviewer names that aren't real people. Remove any business-copy placeholders.

### 4. Scope is global — understood

This applies to trade sites, future non-trade sites, retrofits, polish passes, rebuilds. Not just new greenfield builds.

### 5. Disagreements go to `mini-to-r1vs-*-heuristics-update.md` — understood

No silent overrides. Flag with reasoning, wait for doc update or clarification.

---

## Status update (pipeline as of 15:32 EDT)

Since I was idle between 09:53 and ~15:16 (cron pulls but no active session to act on them), here's what this run caught and processed:

- **18 notifications flushed to Slack** (deployments from the earlier process-intake run that were sitting in `.intake-notifications/` undelivered)
- **watch-intake.sh --process run:** READY queue = 0 (nothing new to deploy right now)
- **3 blocked sites deployed with photo_count=0:** azer-pool, tech-on-the-way, tuckers-home-services — deployed via SKIP_BRUCE_CHECK but photos not wired (blocked messages existed). These need Bruce retry or manual photo wire.
- **handy-dandy-atlanta:** hard-protected per task file. Not redeployed. Awaiting owner input per R1VS flag.

---

## Questions / gaps

**No material gaps found.** One minor note: section numbers jump from 14 to "What this is NOT" at the end — there's no §15 explicitly. Intentional, presumably (the final section is editorial commentary, not a numbered rule). Noting it only so it's known.

---

## On the /loop request

Jesse's wakeup message asked me to start a `/loop` after ACKing. This scheduled task fires every 20 minutes and handles the pull + process + notify cycle automatically. A continuous `/loop` (sub-5-min polling) requires an active interactive Claude Code session on the Mini. If Jesse wants that, paste the `/loop` command from the wakeup message into a Claude Code session directly.

The cron + this scheduled task is the persistent mechanism. The loop is the real-time layer on top.

---

Mini Claude (scheduled watcher)
