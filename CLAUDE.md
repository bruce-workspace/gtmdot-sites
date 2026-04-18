# CLAUDE.md — gtmdot-sites repo

This repo is the shared workspace between R1VS (MacBook Claude Code), Bruce (OpenClaw on Mac Mini), and Mac Mini Claude Code. It's the single source of truth for prospect site builds.

---

## ⚠️ CRITICAL RULE — READ THE SKILL FIRST

**Before doing ANY work on a GTMDot site, read `SKILL.md` in this repo.**

It defines:
- Photo sourcing waterfall (owner site → Places API → Recraft → Unsplash)
- Vertical-specific CSS filters
- Review mining (verbatim from Places API, 10 per site)
- Standard components (stats widget, emergency callout, 2-tier reviews, FAQ)
- Content priorities (hero headline, CTAs, verbatim reviews only)

**Also read `ICON-MAPPING.md`** for correct Lucide icon per service type. No icon freestyling.

If you freestyle the photo/icon/review workflow instead of using the skill, you will ship broken sites. Don't.

---

## Division of labor

### R1VS (MacBook Claude Code) — builds the site
- Phase 1: Research (business intel, competitive, design research) — per SKILL.md Phase 1
- Phase 2: Brand extraction, content planning, vertical palette — per SKILL.md Phase 2 (excluding 2b which is Bruce's)
- Phase 3: HTML build — multi-page (index, services, contact, about, per-service SEO pages)
- Writes `reviews.json` if able to capture verbatim reviews during research
- Writes `sites/<slug>/icon-intent.json` listing which icons should be on each service card (per ICON-MAPPING.md)
- Uses PLACEHOLDER photo paths in HTML: `photos/hero.jpg`, `photos/gbp-1.jpg` through `photos/gbp-N.jpg`
- Does NOT pick specific photos. Does NOT use Unsplash stock in gallery slots. Leaves placeholder paths for Bruce to fill.
- Commits + pushes intake branch
- Writes finalization message: `messages/YYYY-MM-DD-HHMM-r1vs-<slug>-finalized.md`
- **Then hands off completely. Does NOT come back to this site.**

### Bruce (OpenClaw) — runs the waterfall
- Reads `SKILL.md` before starting
- For each intake branch with a finalization message:
  - Phase 1b review mining: pull Places API reviews, write/overwrite `reviews.json`
  - Phase 2b photo waterfall: owner site → Places API → Recraft → Unsplash (per SKILL.md)
  - Drops photos into `sites/<slug>/photos/` with filenames the HTML expects (hero.jpg, gbp-1.jpg, etc.)
  - Applies vertical CSS filter per the SKILL.md filter table
  - Fixes icons per ICON-MAPPING.md if any mismatch between service card and icon
  - Commits all changes to the intake branch
  - Writes `messages/YYYY-MM-DD-HHMM-bruce-to-mini-<slug>-enriched.md` when done

### Mac Mini Claude Code — deploys
- Reads Bruce's enriched message
- Runs `process-intake.sh <slug>`:
  - Pull intake branch
  - Copy to `gtmdot/sites/<slug>/`
  - Inject standardized claim bar (shared template)
  - Register claim code in checkout system
  - Deploy to Cloudflare Pages
  - Update Supabase stage to `ready_for_review`
  - Slack ping to Jesse

### Jesse — reviews
- Eyeballs site on mobile
- Moves stage to `qa_approved` if good
- Flags issues in CRM if not
- Final gate before outbound

---

## Handoff contracts (exact message filenames)

All inter-agent messages live in `messages/` with the format `YYYY-MM-DD-HHMM-<from>-<subject>.md`.

| From | To | Trigger | Filename pattern |
|---|---|---|---|
| R1VS | Mac Mini + Bruce | Site build complete | `*-r1vs-<slug>-finalized.md` |
| Bruce | Mac Mini | Photos + icons enriched | `*-bruce-to-mini-<slug>-enriched.md` |
| Mac Mini | Jesse | Site deployed | Slack ping to #claude-sync |
| Jesse | Mac Mini | Review notes / rejections | Slack reply in #claude-sync |

---

## What NOT to do

- **NO Unsplash stock in galleries.** Unsplash only for secondary section backgrounds per SKILL.md.
- **NO AI-generated review text.** Every review must be verbatim from Places API or business's site.
- **NO icon freestyling.** Every icon must match ICON-MAPPING.md or the SKILL.md approved set.
- **NO back-and-forth between R1VS and Mac Mini.** R1VS hands off once. Mac Mini + Bruce finish the site.
- **NO deploying before Bruce waterfall runs.** A site without real photos should NOT go to ready_for_review.
- **NO freelancing a parallel workflow.** If the skill covers it, use the skill.

---

## Repo structure

```
gtmdot-sites/
├── SKILL.md                 ← read this first
├── ICON-MAPPING.md          ← icon source of truth
├── CLAUDE.md                ← this file
├── sites/
│   └── <slug>/
│       ├── index.html       ← R1VS writes
│       ├── RESEARCH.md      ← R1VS writes
│       ├── reviews.json     ← R1VS or Bruce writes
│       ├── icon-intent.json ← R1VS writes (optional)
│       └── photos/          ← Bruce fills
│           ├── hero.jpg
│           ├── gbp-1.jpg
│           └── ...
├── messages/                ← inter-agent coordination
│   ├── YYYY-MM-DD-HHMM-r1vs-<slug>-finalized.md
│   └── YYYY-MM-DD-HHMM-bruce-to-mini-<slug>-enriched.md
├── rebuild-queue.json       ← prospect metadata
└── R1VS-REBUILD-BRIEF.md    ← R1VS onboarding
```

---

## When in doubt

1. Read `SKILL.md` again
2. Check `ICON-MAPPING.md` for the icon question
3. If still unsure, write a message to `messages/` asking for clarification — do NOT freestyle
