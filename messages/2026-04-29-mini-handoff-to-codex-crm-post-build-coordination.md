---
from: mini-claude
to: mini-codex (chatgpt-5.5)
cc: bruce, r1vs, jesse, paperclip
date: 2026-04-29
subject: Handoff — CRM post-build coordination role + 10 learnings
priority: high
---

# Mini handoff: CRM post-build coordination

This is the durable brief for whoever picks up the Mini-side coordination
role after Anthropic cut OpenClaw OAuth. R1VS continues building sites
on the MacBook; you (Codex / GPT-5.5 on the Mini) inherit everything
downstream of site approval through outreach release, with Paperclip
owning the board and gates.

## Read-order at session start

1. `gtmdot-sites/PIPELINE.md` — single source of truth for who/what/when
2. `gtmdot-sites/HANDOFF-CONTRACT.md` — §11 Bruce-as-Collector + §11.11 Asset Intelligence
3. `gtmdot-sites/SKILL.md` — per-site build phases (R1VS-owned, Mini reads)
4. `gtmdot-sites/DESIGN-HEURISTICS.md` — content + editorial judgment, §13 self-audit
5. `gtmdot-sites/ICON-MAPPING.md` — service icon source of truth
6. `brucecom-v3/CLAUDE.md` — CRM codebase context
7. This file (handoff brief)

## Identity / role

**Mini = the CRM post-build coordinator.** You sit between R1VS's site
build (intake → preview deploy) and Jesse's outreach approval. Your scope:

| Phase | Owner | Mini's job |
|---|---|---|
| Research → BRAND.md + RESEARCH.md | R1VS | Read-only |
| Site build (intake branch) | R1VS | Read-only |
| §11 Bruce collect-request → bruce-collected.md | Mini → Bruce | Write the request, consume the result |
| §11.11 asset-intel | Bruce | Default-accept Bruce's recs per §11.11.3, override only on specific issue |
| Photo wiring → integration copy `photos/` | Mini | YOU |
| Mechanical polish (claim bar, popup, marquee, footer, em-dashes) | Mini | YOU |
| Cloudflare Pages deploy | Mini | YOU (use direct wrangler when CI broken, see "Deploy" below) |
| Supabase stage transitions | Mini | YOU — but never advance to outreach without Jesse approval |
| QA + fix loop | Mini | YOU |
| Outreach-readiness gate | Mini | YOU — `scripts/outreach-readiness-gate.sh <crm-slug>` |
| Final outreach approval (Poplar/Resend trigger, billing, public release) | Jesse | Surface; never auto-trigger |

## Current state (as of 2026-04-29)

**SmartWire Solutions pilot — outreach-ready pending Jesse approval:**
- Live preview: https://smart-wire-solutions.pages.dev/
- HEAD: commit `819fa94` on `gtmdot-sites/main`
- CRM prospect id: `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`
- CRM slug: `smartwire-solutions` (one word — note the slug mismatch
  with directory `smart-wire-solutions`; both work but the CRM slug is
  what the postcard modal uses for asset URLs)
- Stage: `needs_enrichment` (auto-moved by deploy script earlier;
  Jesse hasn't reverted)
- Claim code: `SMAR1182` registered in `gtmdot.com/codes.json` (Bruce did this)
- Email: NOT on file → postcard-only outreach path; needs Jesse explicit approval
- Outreach-readiness gate: 7/7 technical PASS; 5 Jesse-approval gates pending
- All 4 Google verbatim reviews extracted (Cam Martin, Robbie Burr, Like The Bull Co, Robert W)
- Hero: OpenAI gpt-image-2 generated (Bruce, due to Google image-gen budget cap)
- Gallery: 4 Alignable owner-controlled service photos (smart switches, ceiling fan, recessed lighting, modern outlets)
- Postcard assets all staged at `gtmdot-postcards.pages.dev`

## Hard rules — never do without Jesse explicit approval

These are ratified by Jesse 2026-04-28 and 2026-04-29:

1. ❌ No CRM stage move past `qa_approved`
2. ❌ No Poplar postcard send
3. ❌ No Resend email send
4. ❌ No billing / charge / subscription start
5. ❌ No public outreach release (LinkedIn, social, etc.)
6. ❌ No site-builder script (deprecated per PIPELINE.md §3)
7. ❌ No hardcoded Supabase service-role JWT in scripts (env var only)
8. ❌ No production repo / CRM source / DNS edits without telling Jesse first

The outreach-readiness gate explicitly lists these as `⌛ jesse-approval-gates`.

## Coordination protocol

### Message-file convention

All cross-instance coordination goes through `gtmdot-sites/messages/`:

```
messages/YYYY-MM-DD-HHMM-<from>-<subject>.md
```

`<from>` values: `mini`, `bruce`, `r1vs`, `bruce-to-mini`, `mini-to-r1vs`,
`r1vs-jesse-to-mini`, `jesse-to-mini`. Each file has YAML frontmatter
(`from`, `to`, `date`, `subject`, `priority`) and is a self-contained
ack-or-flag artifact.

### Branch / commit hygiene (multi-instance hazard)

**THIS IS THE #1 GOTCHA.** When other instances (Bruce daemon, spawned
tasks) work in the same repo concurrently, you may auto-end up on a
feature branch from their work. ALWAYS:

```bash
git branch --show-current
git status --short
```

before committing. If you committed to a feature branch by accident,
cherry-pick onto main:

```bash
git stash push -m "wt" -- <unrelated-paths>   # stash anything not yours
git checkout main && git pull origin main
git cherry-pick <wrong-branch-sha>
git push origin main
git stash pop
```

I burned this twice in this session.

### Deploy

Cloudflare Pages auto-deploy is configured via `.github/workflows/deploy.yml`
on push to main. **It's been broken since 2026-04-23** with a chain of
issues — most recently `node:sqlite` import unresolvable in Workers
runtime. There's a spawned task to lazify module-level client init
(see "Open items"); until that lands, deploys must go through:

```bash
cd /Users/bruce/.openclaw/workspace/brucecom-v3   # for the CRM itself
npx opennextjs-cloudflare build && npx opennextjs-cloudflare deploy

# OR for prospect sites:
cd /Users/bruce/.openclaw/workspace/gtmdot-sites
npx wrangler pages deploy sites/<slug> --project-name <slug> --branch main --commit-dirty=true
```

**Critical:** do NOT use `gtmdot/scripts/deploy-site.sh`. It auto-moves
the prospect to `site_built` and registers claim codes, both of which
violate the "no CRM stage change without approval" rule for the pilot.
Direct wrangler is the safer path during QA.

### The outreach-readiness gate (you own this)

`gtmdot-sites/scripts/outreach-readiness-gate.sh <crm-slug>` is the
canonical implementation. Returns exit 0 on technical pass, exit 1 on
fail, exit 2 on lookup error. Always run before signaling
outreach-readiness. The 8 checks:

1. claim code resolves on `gtmdot.com/codes.json` + `/checkout?code=X` returns 200
2. desktop screenshot at `gtmdot-postcards.pages.dev/screenshots/<slug>-desktop.jpg` (image/* content-type)
3. mobile screenshot same pattern
4. hero image at `gtmdot-postcards.pages.dev/<slug>-hero.jpg`
5. postcard mockup ready (transitive)
6. email present OR explicitly missing (postcard-only acceptable, needs Jesse approval)
7. email-sequence draft #1 renders if email present
8. Jesse-approval gates listed (CRM stage move, Poplar, Resend, billing, public release) — never auto-pass

## Canonical files / scripts you'll use most

| Path | Purpose |
|---|---|
| `gtmdot-sites/scripts/outreach-readiness-gate.sh` | YOUR gate (Mini-owned) |
| `gtmdot-sites/scripts/pre-push-gate.sh` | R1VS pre-push checks (Mini reads, sometimes overrides — see "Stale gate overrides") |
| `gtmdot-sites/scripts/verify-build.sh` | R1VS post-build verification |
| `gtmdot-sites/scripts/consume-asset-intel.py` | Read Bruce's `bruce-asset-intel.json`, route findings |
| `gtmdot-sites/scripts/render-reviews-bar.py` | Conditional Path A/B/C review-bar render |
| `gtmdot-sites/scripts/enrichment-dispatcher.py` | Write `collect-request.md` for Bruce |
| `gtmdot-sites/scripts/state-snapshot.sh` | Update PIPELINE.md §4 snapshot |
| `gtmdot-sites/templates/multi-page/index.html` | Template for new prospect sites |
| `brucecom-v3/src/lib/poplar.ts` | Postcard send (Poplar API client) |
| `brucecom-v3/src/lib/resend.ts` | Email send (Resend API client) |
| `brucecom-v3/src/components/prospect/PostcardPreviewModal.tsx` | CRM postcard preview |

## What changed in this session (handoff context)

In rough order, this session touched:

### CRM intake form expansion (brucecom-v3)
- Added 7 new fields to the prospect intake: payments URL, Facebook,
  Yelp, Nextdoor, Thumbtack, Angi URLs, existing-site-status (3-button
  enum: no_site / outdated / has_site)
- Fixed misleading "Failed to execute 'json' on 'Response'..." error
  that masked Postgres unique-violation on duplicate slugs. The route
  now wraps `createProspect` in try/catch, maps Postgres `23505` to a
  409 with a friendly message, and the modal reads response as text
  first then tries JSON.
- DB migration applied: `payments_url`, `facebook_url`, `yelp_url`,
  `nextdoor_url`, `thumbtack_url`, `angi_url`, `existing_site_status`
  (with CHECK constraint).
- Shipped via PR #6 → main → manual `npx opennextjs-cloudflare deploy`.

### Auto-deploy CI repair attempts (brucecom-v3 GitHub Actions)
- Added 6 GitHub repo secrets via Chrome (Jesse + I together):
  `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`,
  `SUPABASE_SERVICE_KEY`, `RESEND_API_KEY`, `CLOUDFLARE_API_TOKEN`,
  `CLOUDFLARE_ACCOUNT_ID`. Wired them into the `Build OpenNext bundle`
  step.
- Build now passes the env-var stage but **wrangler deploy fails on
  `node:sqlite` resolution** — some dependency tree imports Node's
  built-in SQLite which isn't supported in Workers. Spawned task open.
- Until that lands, manual deploy is required.

### SmartWire pilot end-to-end
- Bruce did §11.11 asset-intel pass: hero PNG, Alignable photos,
  reviews placeholder. Hit Google image-gen budget cap; OpenAI fallback.
- I extracted 4 verbatim Google reviews via Chrome MCP navigation
  (Bruce was policy-blocked). Updated `reviews.json`.
- Integrated hero (with `data-source="generated"`), gallery, reviews PATH A.
- Generated claim code SMAR1182 (Bruce later registered it on gtmdot.com).
- Cloudflare deploy via direct wrangler (skipping deploy-site.sh's
  auto-stage-move).
- Multi-pass QA fixes (Jesse mobile review):
  - 130 internal nav hrefs `.html` → clean URLs (eliminates 308 redirect)
  - Upload-module file-chip JS handler (with `</body>`-in-comment gotcha)
  - Mobile h1 sizing (clamp 36→28 floor + tighter line-height)
  - Service-card overflow-wrap fix
  - Reviews carousel: marquee animation → flex-wrap grid
  - Gallery: removed 2 rough photos (damaged outlets, dirty panel),
    fixed gbp-1 context mismatch
  - data-resolved="false" → "true" on 13 service-page slots (alt-text leak)
  - Nav-dropdown hover bridge via `.nav-dropdown::before`
  - 88 em-dashes stripped from authored copy across 8 pages

### Process / governance
- Established outreach-readiness gate (Mini-owned, Jesse 2026-04-29 ratified)
- Documented two stale-rule overrides (pre-push-gate Check #3, verify-build Check #1)
  with spawned follow-up tasks to make them stage-aware / Cloudflare-aware
- The verify-build clean-URL fix shipped during this session as `4024f38`
- The pre-push-gate stage-aware fix is on a branch but not merged to main yet
- Wrote pipeline-task-snapshot doc to Bruce on 2026-04-28 with cadence/IO
  for the 11 missing scheduled tasks (Paperclip will orchestrate them)

## Top 10 learnings + things I battled against

### 1. Cloudflare Pages SPA fallback masks missing assets
HEAD requests return **200 with `content-type: text/html`** for files
that don't exist (it serves the SPA index instead). Status code alone
is a false positive. Always check content-type. The
outreach-readiness-gate's `check_image_url` function does this; copy
that pattern anywhere you check asset existence.

### 2. CSS `attr()` with `data-` attributes silently leaks debug content
The rule `.gtmdot-photo-slot[data-resolved="false"]::before { content:
"📷 " attr(data-slot-id) " — " attr(data-context); }` was a R1VS-side
debug aid. When Mini forgets to flip `data-resolved` to `"true"`, the
internal context tags ("panel-work-OK | outlet-repair-OK | ...") render
to the user as if they were real captions. Production-blocking. Always
audit for unresolved photo slots before deploy.

### 3. CSS hover dropdowns need an unconditional bridge element
Menus positioned `top: calc(100% + 14px)` are visually offset from the
trigger, creating a gap where neither element is hovered. The menu
itself can't bridge — it has `visibility: hidden` until parent hover.
Bridge has to be an `::before` on the **always-rendered parent**, not
the menu. Caught only on MacBook (worked on M1 — likely cursor
acceleration / mouse-poll difference).

### 4. Module-level client init breaks Next.js page-data collection
`const x = new SomeClient(process.env.X);` at the top of a lib file
fires during build's page-data walk, and crashes if `X` isn't set.
Slack does this right (lazy: token read inside the function). Resend
and Supabase did it wrong (module-level). Build environments don't
have your `.env.local`, so every missing var → build fail. The proper
fix is lazy `getX()` accessors. Spawned task pending.

### 5. `text.replace(needle, X, 1)` matches the FIRST needle, including inside comments
Injecting `</body>`-adjacent code with `text.replace('</body>', ..., 1)`
matched the `</body>` inside an HTML comment ("Injected by ... just
before </body>.") instead of the real closing tag. Result: my injected
script ended up commented out and silently never ran. Use `rfind` for
last-occurrence, or use a regex anchored to "real" tag (e.g. preceded
by `>` or whitespace at end of file).

### 6. Slug mismatches — directory slug vs CRM slug
SmartWire is `smart-wire-solutions` on disk (R1VS chose the spaces-as-hyphens
form) but `smartwire-solutions` in CRM (deduped on intake). Cloudflare
serves both forms because of how Pages routes — but only one of them is
the real file. Other tooling (postcard modal, codes.json registry) uses
the CRM slug. **Always disambiguate which slug you mean** in any URL/path.
Recommend converging to CRM slug as canonical.

### 7. Multi-instance branch confusion is the #1 process hazard
Other instances (Bruce daemon, spawned-task agents) commit to feature
branches in the same repo. When you `git add` and `git commit`, you may
silently land on their branch. I made this mistake **twice** in this
session — both times had to cherry-pick onto main and stash unrelated
working-tree changes. Always `git branch --show-current` before
committing. Always `git status --short` to see if WT has unrelated
modifications you'd accidentally bundle.

### 8. CSS marquee animations require duplicated content (2N cards)
`.reviews-marquee` had `animation: review-scroll 52s linear infinite`
expecting `transform: translateX(-50%)` to seamlessly loop because the
track held 2× the visible cards (forward + duplicate). With only N
cards (no duplicate), the animation just translates everything off-screen
revealing nothing. The home `.marquee` (rotating taglines) does this
correctly with explicit `<!-- duplicated for seamless loop -->` block.
**Either duplicate or use a non-animated layout.** I switched reviews
to flex-wrap grid because animation on user-readable content (vs.
decorative tagline) is anti-accessibility.

### 9. Stale gates erode trust in the gate
`pre-push-gate.sh` Check #3 forbids claim UI in any push, but Mini's
mid-pipeline commits LEGITIMATELY contain claim UI by design. Override
mountain: every Mini push needs a documented override message. The fix
is making the gate stage-aware (read `STAGE.txt` per site). Spawned
task already shipped on a branch but not merged. **Lesson:** when a
gate fires false positives every run, it gets ignored — fix the rule,
don't normalize the override.

### 10. JSON-LD content shows up in Google rich results — strip noise too
Em-dash strip pass initially missed JSON-LD blocks because they're
inside `<script type="application/ld+json">` — same tag as JS, so my
regex excluded them. But `description` and `acceptedAnswer.text` in
JSON-LD render in Google search snippets and AI-assistant answers.
Authored copy rules apply there too. **Treat JSON-LD as visible content
for editorial/style purposes**, not as code.

### Bonus 11: The browser HEAD request is asymmetric vs GET
Some endpoints respond differently to HEAD vs GET. Cloudflare Pages
sometimes returns no `content-length` or different cache behavior on
HEAD. When in doubt, use a `curl -sS ... | wc -c` actual GET to confirm
file existence + size, not just HEAD.

## Open items / spawned tasks

(Run `mcp__ccd_session__spawn_task` chips check, but for context:)

1. **Lazify module-level client init in `brucecom-v3/src/lib/`** — fixes
   the auto-deploy CI permanently. Pattern: `let _x = null; const getX =
   () => _x ??= new Client(env);` Resend is confirmed offender; Stripe,
   Apollo, Google Places need audit too.
2. **Make `pre-push-gate.sh` Check #3 stage-aware** — branch
   `fix/pre-push-gate-stage-aware-claim-check` shipped, just not merged
   to main yet.
3. **`node:sqlite` resolution failure in Workers** — separate issue
   from #1; a dependency tree imports Node's built-in SQLite which
   isn't supported in Workers. Need to track the import chain and
   either remove the dep or configure compat flags.
4. **Reconcile site directory slug vs CRM slug for SmartWire** — pick
   one (recommend CRM `smartwire-solutions`) and align both.
5. **Cache-bust the postcard preview screenshots** — `PostcardPreviewModal.tsx`
   has cache-bust on hero (`?v=${heroBust}`) but not desktop/mobile
   screenshots. Browser-cached 404s can survive after assets are staged.
6. **Email outreach for SmartWire** — find Terry Henry's email or
   commit to postcard-only path with Jesse approval.
7. **The 11 missing scheduled-task LaunchAgents** — Bruce-Codex via
   Paperclip will orchestrate from the recovered SKILL.md files; see
   `messages/2026-04-28-1049-mini-to-bruce-pipeline-task-snapshot.md`
   for the full cadence/IO map.

## Where to start your first session

```bash
cd /Users/bruce/.openclaw/workspace/gtmdot-sites
git fetch origin && git pull origin main
git status --short              # confirm clean WT before any commit
ls messages/ | tail -10          # any new directives?
./scripts/outreach-readiness-gate.sh smartwire-solutions   # baseline
```

Then read the latest 3-5 message files in `messages/` for any new
directive from Jesse / Bruce / R1VS.

— Mini-Claude (final handoff before OAuth cutover)
