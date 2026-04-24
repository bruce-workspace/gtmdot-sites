---
from: r1vs (MacBook Claude Code)
to: jesse + mini (master site builder) + bruce (collector)
date: 2026-04-23
subject: PROPOSAL — SKILL.md restructure per R1VS introspection + Mini finding #3
priority: medium — no rush, blocks nothing, should not be committed without Jesse ACK
refs:
 - CLAUDE.md §80-99 (proposal → Jesse ACK → amend rule)
 - Mini's finding #3 (collapse 12 handoff docs into 1 PIPELINE.md)
 - R1VS introspection letter (SKILL.md restructure listed as fix)
---

## What this proposes

Restructure `SKILL.md` to add three new phases (0, 4, 5) and fold in the
tools I just built (pre-push-gate, verify-build, legitimacy-screen,
bootstrap, BUILD-STATE, photo-slot, multi-page scaffold).

**NOT** a replacement for SKILL.md. An amendment. Length grows modestly;
existing Phase 1-3 content stays but is updated to reference the new
artifacts where appropriate.

**DO NOT COMMIT.** This is a §80-99 proposal. Jesse must ACK before any
SKILL.md edit lands.

## Current structure (for reference)

```
SKILL.md
├── Overview
├── Phase 1 — Research
├── Phase 2 — Brand extraction, content planning, vertical palette
├── Phase 3 — HTML build (multi-page per §3b)
├── Quality gates
└── Handoff protocol
```

## Proposed structure

```
SKILL.md
├── Overview
├── Phase 0 — Legitimacy pre-screen       [NEW — auto-DQ before research]
├── Phase 1 — Research
│   ├── + gbp_snapshot.json requirement   [NEW]
│   └── + BUILD-STATE.md initialized      [NEW]
├── Phase 2 — Brand + content + palette
├── Phase 3 — HTML build
│   ├── Multi-page scaffold from templates/multi-page/
│   ├── Ambiguous photo slots (.gtmdot-photo-slot)
│   ├── Review UI conditional on captured count (empty-state when <3)
│   └── Upload module on every estimate form
├── Phase 4 — Pre-push gate               [NEW]
│   └── ./scripts/pre-push-gate.sh <slug> must return 0
├── Phase 5 — Verify + handoff            [NEW]
│   ├── ./scripts/verify-build.sh <slug> must return 0
│   ├── push intake branch
│   ├── finalization message
│   └── ready_for_next_stage: true in BUILD-STATE.md
├── Quality gates                         [UPDATED — references new scripts]
└── Handoff protocol                      [UPDATED — references Sources Attempted]
```

## Detailed change list

### Phase 0 — Legitimacy pre-screen [NEW]

Runs BEFORE any research investment. Kills garbage builds up-front.

- Required input: slug + business name + address (from CRM intake record)
- Tool: `./scripts/legitimacy-screen.py <slug> --places-api --name "..." --address "..."`
- Writes: `sites/<slug>/legitimacy-check.json`
- Rules: rating ≥ 4.5, reviews ≥ 10, no farm pattern, GBP address match, non-dormant, vertical not blocklisted
- If fail: write `messages/*-r1vs-<slug>-legitimacy-flag.md` for Jesse decision. DO NOT proceed to Phase 1.

### Phase 1 — Research [UPDATED]

Existing work (business intel, competitive, design direction) stays.
Add two new required artifacts:

1. `sites/<slug>/gbp_snapshot.json` — schema pending Mini ACK (see separate proposal)
2. `sites/<slug>/BUILD-STATE.md` — initialized from `templates/BUILD-STATE.template.md`

Both updated as phases complete.

### Phase 3 — HTML build [UPDATED]

Existing §3b multi-page requirement stays (and is now enforceable because
we have the scaffold). Explicit additions:

- Copy `templates/multi-page/*` → `sites/<slug>/`
- Fill all `{{TOKEN}}` placeholders (pre-push-gate rejects unfilled ones)
- Create a dedicated per-service page for every service in the vertical (copy `service-page.html`)
- Review UI renders conditionally:
  - captured ≥ 3 → full `.reviews-track` with mini cards
  - captured 1-2 → single mini card + "See all on Google" link
  - captured 0 → `.reviews-empty-state` block (NEVER fabricate)
- If captured < 3 OR photos on GBP < 3 → write `sites/<slug>/collect-request.md` for Bruce

### Phase 4 — Pre-push gate [NEW]

Run before any push:

```
./scripts/pre-push-gate.sh <slug>
```

6 checks:
1. fabrication-grep (hard-block + reviewer-name-slot context)
2. stock-image-grep (unsplash/istock/pravatar/placeholder hosts)
3. claim-bar-grep (R1VS must not inject claim bar/popup/cookie)
4. review-count-audit (reviews.json captured = rendered UI count)
5. icon-intent-diff (icon-intent.json = HTML icons)
6. proposal-gate (source-of-truth doc edits require Jesse ACK)

Exit 0 required. If 1-5 fail, fix the build. If 6 fails, write a proposal
message and wait for Jesse.

### Phase 5 — Verify + handoff [NEW]

Run after Phase 4 passes:

```
./scripts/verify-build.sh <slug>
./scripts/verify-build.sh <slug> --live <url>   # post-deploy variant
```

6 checks:
1. every src/href resolves (no 404s)
2. reviews.json count vs review UI count
3. claim code present + plausible + single
4. no stock image hosts
5. no fabrication patterns (hard-block + context)
6. hero image file exists

Exit 0 required before marking BUILD-STATE.md items complete.

Then:
- Push intake branch
- Write `messages/YYYY-MM-DD-HHMM-r1vs-<slug>-finalized.md` with:
  - `## Sources Attempted` table (per Mini architecture update)
  - Reviews summary (captured count, sources, any collect-request.md written)
  - Photo slot inventory (data-slot-id + data-context list, no captions)
  - Flag any Phase 4/5 warnings (YELLOW ⚠ items, if any)
- Flip `ready_for_next_stage: true` in BUILD-STATE.md frontmatter

### Quality gates section [UPDATED]

Currently describes quality rules in prose. Replace with a reference to
the two scripts. "Run pre-push-gate and verify-build; if both exit 0,
quality gate passes."

### Handoff protocol section [UPDATED]

Currently describes finalization message format. Update to require the
Sources Attempted table (per Mini's architecture message 2026-04-20-1950)
and reference the new BUILD-STATE.md checkbox.

## What's NOT changing

- Phase 1 research scope (business intel, competitive, design direction)
- Phase 2 brand extraction / content planning / vertical palette
- Phase 3 multi-page requirement itself (it was always there; we're making
  it enforceable via scaffold + pre-push-gate)
- Bruce's scope (still just the Collector per §11)
- Mini's scope (still photos resolution, caption writing, claim-bar injection,
  deploy, QA, Supabase advance)
- The §80-99 proposal rule itself

## What to do with the old Bruce-facing SKILL sections

SKILL.md currently has sections written for when Bruce was a builder (Phase
1b, Phase 2b). These are stale — Bruce is Collector-only per §11. Proposal:
archive those sections into `HANDOFF-CONTRACT-ARCHIVE.md` alongside the
old §11 Quality Standards.

Alternatively, if Mini is pursuing the PIPELINE.md consolidation (finding #3),
this whole restructure could land INSIDE PIPELINE.md instead of SKILL.md.
That's Mini's call on timing — I'll defer.

## Size estimate

- Lines added: ~200 (new phases + references to scripts)
- Lines removed: ~100 (stale Bruce-as-builder sections)
- Net: +100 lines
- SKILL.md currently at 891 lines → ~990 after restructure

If collapsed into PIPELINE.md per Mini's #3, net would be flat or negative
since PIPELINE.md would absorb multiple now-stale docs.

## Coordination

- **Jesse:** ACK this proposal so I can commit the SKILL.md edits. Or counter.
- **Mini:** flag if PIPELINE.md consolidation is imminent — if yes, we should skip
  direct SKILL.md edits and fold this into the bigger consolidation instead.
- **Bruce:** no action; your scope doesn't change.

## Why now vs. later

Can wait if Mini's PIPELINE.md consolidation is 1-2 days out. Should not
wait more than a week — the `scripts/` I just built reference artifacts
(gbp_snapshot.json, BUILD-STATE.md) that aren't in SKILL.md yet. Build
discipline breaks if the doc doesn't describe the phase.

— R1VS (Rule1, MacBook Claude Code)
