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
- **NO claim bar / popup / cookie banner in R1VS builds.** Mac Mini injects the shared template at `gtmdot/sites/_shared/claim-ui.html` post-build. Any R1VS-built claim UI will be suppressed by the injector's `display: none !important` block for legacy selectors (`#claimBar`, `#claim-bar`, `#exitPopup`, `#exit-popup`, `#cookieBanner`, etc.).
- **NO `<!-- CLAIM_BAR_ANCHOR -->` comment needed.** Mini's injector finds `</body>` and inserts before it automatically.

---

## System facts (confirmed by Mini, Apr 2026)

Do not trust documentation older than this table. These are the authoritative values.

### Supabase
- **Project ID:** `qztjoshdrxionhxeieik`
- **`supabase/schema.sql` in brucecom-v3 is STALE** — do not read it. Migrations are authoritative.
- R1VS never writes to Supabase directly. It POSTs to the intake API (`crm.cloakanddagger.co/api/site-intake`) per `R1VS-REBUILD-BRIEF.md`.

### Pipeline stages (`public.prospects.stage`)
Linear flow, in order:
```
research → site_built → ready_for_review → qa_approved → outreach_staged → outreach_sent → converted → dead
```
Also valid edge state: `stuck` (added 2026-04-04)

**Killed stages** (migrated away 2026-04-12, DO NOT use):
`claude_reviewed`, `design_review`, `in_window`, `follow_up`, `disqualified`

### Intake API state (`public.site_intake.state`)
Separate lifecycle from `prospects.stage`:
```
received → reviewing → accepted → revision_needed → rejected → built → deployed
```

### Claim bar / shared UI template
- **Path (Mini side):** `gtmdot/sites/_shared/claim-ui.html`
- **Current SHA:** `e59f489` ("feat(brief-7): retrofit claim bar + popup across 36 non-live sites")
- **CSS namespace:** `.gtmdot-claim-*` (won't collide with R1VS-built site CSS)
- **Template variables:** `{{CLAIM_CODE}}`, `{{BUSINESS_NAME}}`, `{{PRICE_FIRST_MONTH}}` (default `$49`), `{{PRICE_ONGOING}}` (default `$149`), `{{CHECKOUT_URL}}` (default `https://gtmdot.com/checkout?code={{CLAIM_CODE}}`), `{{HOW_IT_WORKS_URL}}` (default `https://gtmdot.com/how-it-works`)

### Secrets
- **`INTAKE_BEARER_TOKEN`** — required by R1VS to POST to the intake API. Set in Mini's `brucecom-v3/.env.local` (server-side verification). R1VS needs its own copy, canonically at `~/.openclaw/.env` on the MacBook. **NOT required for retrofit passes** on existing intake branches — only for new site builds.
- **API keys** (`GOOGLE_MAPS_API_KEY`, `FIRECRAWL_API_KEY`, `RECRAFT_API_KEY`, `POPLAR_API_KEY`) — canonical location is `~/.openclaw/.env` on both machines. R1VS mostly does not need these directly (Bruce owns the waterfall), but they're there for ad-hoc research.

### Bruce status
- Bruce is **not always active.** When R1VS writes a finalization message, Bruce may not process it until the next time he's explicitly started. Don't treat enrichment as automatic.
- "Blocked" enrichment on grandfathered sites (already deployed) is fine — Mini bypassed the Bruce gate for those at deploy time.

### Outreach hold
- When an **outreach hard hold** is active (e.g. Brief 15 pending), all email/postcard sends are frozen. Retrofitting and deploying are still fine — only send actions are gated.

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
