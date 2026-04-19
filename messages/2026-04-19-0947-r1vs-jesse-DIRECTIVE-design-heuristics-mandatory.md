---
from: r1vs + jesse (jointly)
to: mini claude (and any future Claude on the pipeline — present and future sessions)
date: 2026-04-19
subject: MANDATORY — Use DESIGN-HEURISTICS.md on every site decision. Global. Not optional.
priority: URGENT / STANDING DIRECTIVE
---

# Directive

Jesse is issuing this directly. A new file landed at the repo root: `DESIGN-HEURISTICS.md` (commit `9e0f0a8`).

**Read it. Use it. On every site decision. Every time.**

This is not a suggestion. It's not a "maybe try." It's the working reference for how GTMDot sites are built to a quality bar. R1VS applied these patterns across 24 sites in the last 12 hours (3 sample + 11 overnight loop + 3 urgent rebuilds + 7 grandfathered polish) and Jesse confirmed the output quality is unmatched by what he was previously getting from the pipeline.

## The scope is global — not just trade sites

This document applies to:
- GTMDot trade-business sites (the current 51-site rebuild queue)
- Any future non-trade site work (stale-site-identifier candidates, new verticals, client sites, anything)
- Retrofits, polish passes, and rebuilds — not just greenfield builds
- Every Claude session on this pipeline, present and future

When you're tempted to freestyle an icon, pick a generic pull quote, or duplicate hero stats in the story section — **stop and read the heuristic.** If there's a conflict between what you'd instinctively do and what the doc says, the doc wins. Jesse has made that call explicitly.

## What to do on every session startup

Before touching any site-building task, read (in this order):

1. `CLAUDE.md` (contract, division of labor)
2. `SKILL.md` (workflow phases, polish rules)
3. `ICON-MAPPING.md` (icon source of truth)
4. **`DESIGN-HEURISTICS.md` (this newly-added doc) — REQUIRED**
5. Site-specific `RESEARCH.md` + `reviews.json` for whatever site you're working on

If the session's prior Claude read DESIGN-HEURISTICS.md and you're continuing that session, re-read the relevant section before each individual site decision anyway.

## Specific things the heuristics doc fixes (that were failing before)

Jesse flagged these as blockers on the other machine (Mini Claude) that R1VS was getting right:

1. **Contextual icon selection** — Mini was picking generic icons instead of matching the service type to `ICON-MAPPING.md`. Fix: §1 of DESIGN-HEURISTICS.md spells out the rule + examples.
2. **Photo wiring context** — Mini was placing photos without reading the reviews to know what the photo should show. Fix: §2 includes caption-content matching and a `photos/intent.json` spec for the revised 1-pass contract.
3. **Pull quote selection** — Mini was picking generic quotes instead of the specific-story-with-named-tech ones. Fix: §3 has the selection rubric + examples.
4. **Stats de-dup** — sites were shipping with story-highlights that copy-pasted hero stats. Fix: §4 has four resolution modes keyed to what the site already has.
5. **Content integrity** — fake review content (e.g. "Company Mission" signed as a reviewer) was landing in review cards. Fix: §5 hard rule.

## Why this is happening now

We're revising the contract from `d004e79` to eliminate unnecessary R1VS passes. Under the new model:

- **R1VS** does research + HTML + content-craft + writes `photos/intent.json` in a single first pass
- **Bruce** only runs when R1VS can't source photos or heavy scrapes (Places API + Firecrawl)
- **Mini Claude** wires photos per R1VS's intent, applies mechanical polish, deploys — **and now also inherits the design-craft responsibility** for any decisions R1VS didn't explicitly resolve

For Mini to do that last step well, Mini must operate with the same editorial discipline R1VS has been applying. `DESIGN-HEURISTICS.md` is the mechanism. That's why it's mandatory.

## If you disagree with any rule in DESIGN-HEURISTICS.md

Flag it in a `mini-to-r1vs-*.md` message with specific reasoning. Do not override silently. R1VS + Jesse will discuss and either update the doc or clarify the rule. Until that happens, the doc is authoritative.

## Acknowledgment

When you (Mini Claude, or any future Claude) pick up this directive, please ACK in a reply message stating:
- You've read `DESIGN-HEURISTICS.md`
- You're applying it globally (not just to trade sites)
- Any section where you have questions or see gaps

No site polish, photo wire, or deploy should happen after you read this message without first reading the heuristics doc.

## One more thing

This doc will evolve. When new patterns emerge from real builds, update it. Commit message format: `docs(heuristics): add/update rule for [topic]`. Every rule should come from observed practice, not speculation.

---

Jesse + R1VS
