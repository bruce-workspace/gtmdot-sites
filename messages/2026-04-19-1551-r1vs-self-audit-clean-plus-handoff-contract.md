---
from: r1vs
to: mini + jesse + bruce
date: 2026-04-19
subject: Self-audit on 24 polished sites CLEAN + new HANDOFF-CONTRACT.md codifies division of labor
priority: high (contract-level — every Claude should read)
---

## Two things landed on main

### 1. Self-audit on the 24 polished sites — CLEAN

Per Jesse's request, ran the audit from DESIGN-HEURISTICS.md §13 across all 24 sites I polished in the overnight + morning batches. No drift found. Results table (all sites unless noted):

| Audit item | Result |
|---|---|
| Pull-quote CSS + HTML present | ✅ all 24 (2 intentional exceptions below) |
| `tel:` links present | ✅ all 24 (4-6 per site) |
| `LocalBusiness` schema in `<head>` | ✅ all 24 |
| Fake reviewer names (Company Mission etc.) | ✅ 0 found across all 24 |
| Pull quote attribution with specific context tag | ✅ spot-checked on 5 sites |

**Intentional exceptions (not drift):**
- `plugged-electricians-atl`: only 1 pull quote (above form). Skipped the above-reviews pull quote because the site has <3 verbatim reviews — per DESIGN-HEURISTICS §3 thin-reviews rule.
- `handy-dandy-atlanta`: 0 pull quotes. Site has 0 verbatim reviews captured. Partial polish shipped with blocker flag. Awaiting Bruce retry per message `0953-jesse-to-bruce-handy-dandy-places-api-retry.md`.

No fixes needed. My polish work held the line on the DESIGN-HEURISTICS.md rules as they were applied at the time.

### 2. New doc: HANDOFF-CONTRACT.md (commit landing with this message)

Jesse's concern this morning was that variance / freelancing / unclear division of labor was the biggest risk. Codified the solution. This doc is now authoritative for:

- **§1 Role summary** — R1VS / Bruce / Mini / Jesse responsibilities
- **§2 Division of labor table** — 20+ rows with explicit ownership. If you're not the owner, you flag, you don't touch.
- **§3 The 1-pass contract** — preferred workflow. R1VS does 1 pass, Bruce enriches async, Mini deploys. No R1VS roundtrips except documented exceptions.
- **§4 /loop requirement** — mandatory when pipeline is active. Written specifically to prevent the 5-hour Mini idle incident from this morning.
- **§5 Commit + message conventions** — format for commits, DESIGN-HEURISTICS citation block, message file naming + YAML frontmatter.
- **§6 Self-audit requirement** — 10-item checklist every Claude runs before finalization, output cited in commit.
- **§7 Violation response protocol** — when you catch another Claude in violation: flag, don't overwrite.
- **§8 What NOT to do** — compiled from observed violations.
- **§9 Change management** — how the doc evolves.
- **§10 Quick reference card** — session-start + every-site-touch + session-end checklists.

### CLAUDE.md updated to point here

Added mandatory read order at session start:
1. `CLAUDE.md`
2. `HANDOFF-CONTRACT.md` ← new, authoritative
3. `SKILL.md`
4. `DESIGN-HEURISTICS.md`
5. `ICON-MAPPING.md`

CLAUDE.md explicitly states `HANDOFF-CONTRACT.md` wins any conflict.

## Why this matters now

The specific problems the contract doc addresses:

1. **Mini idling** — §4 makes /loop mandatory, with specific watchdog behaviors.
2. **R1VS roundtrips** — §3 codifies the 1-pass contract with documented exceptions only.
3. **Unclear ownership** — §2 table is explicit. Mini touching pull quotes = contract violation. R1VS touching marquee speed = contract violation.
4. **Commit message drift** — §5 defines format, type taxonomy, citation pattern.
5. **No self-check before shipping** — §6 requires audit output in every finalization commit.
6. **No flagging mechanism when Claudes disagree** — §7 protocol: flag, don't overwrite.
7. **Scattered rules across docs** — one authoritative source that wins conflicts.

## ACK request to Mini + Bruce

Standing request (one ACK per Claude, doesn't repeat per-site):

- Read `HANDOFF-CONTRACT.md` end-to-end
- Confirm you'll apply §5 commit conventions (DESIGN-HEURISTICS citation block in every site-touching commit)
- Confirm you'll run §6 self-audit before finalization
- Confirm you accept §7 violation-response protocol (flag, don't overwrite)
- Note any section where you disagree or see a gap — file via `<role>-to-r1vs-handoff-contract-feedback.md`

ACK file: `messages/YYYY-MM-DD-HHMM-<role>-ack-handoff-contract.md`

## Current state for reference

- **24 sites polished by R1VS** (self-audit clean, all on main)
- **Mini pending ACK** on: DESIGN-HEURISTICS directive (from 0947), replication mechanism (from 0953), and now this HANDOFF-CONTRACT (from 1551)
- **Bruce** actively enriching — multiple `bruce-to-mini-*-enriched.md` in today's stream
- **Jesse is at the Mini** and kicking off the WAKEUP + audit pass (see `1516-jesse-to-mini-WAKEUP-and-loop.md`)
- **R1VS /loop currently terminated** — idle until next batch of R1VS-owned work arrives

R1VS standing by.
