# R1VS Trade Builder → Paperclip Handoff Contract (v1)

**Audience:** Codex (Mac Mini), Bruce (OpenClaw), Mini (Master Site Builder), Jesse, Paperclip orchestrator
**Date:** 2026-04-28
**Author:** R1VS (MacBook Claude Code)
**Status:** Contract export — describes what R1VS does **today**, not aspirational behavior. Gaps are called out explicitly.
**Triggered by:** Codex handoff request post-OpenClaw 4.29/4.30 incident

---

This contract describes the R1VS Trade Builder's input/output/signal surface so Paperclip + Supabase can orchestrate Phase 0–3 builds without Jesse hand-walking messages between machines. It is descriptive, not prescriptive — where R1VS is missing a capability (queue-watching, autonomous trigger), it says so.

---

## 1. Inputs R1VS needs to start a build

### Required

A build cannot start without these:

| Field | Notes |
|---|---|
| `slug` | kebab-case, becomes `sites/<slug>/` folder name |
| `business_name` | display name; `business_name_legal` if it differs |
| `vertical` | `electrical` / `collision` / `plumbing` / `hvac` / `painting` / etc. |
| `gbp_identity` | exactly **one** of: GBP `share_url` (preferred), `kgmid`, `cid` (hex or decimal), or `place_id`. **`place_id` alone fails on service-area-business listings (ftid=0x0)**; `share_url` or `cid` are the SAB-safe inputs. SAB blind-spot proposal at `proposals/2026-04-28-r1vs-legitimacy-screen-share-url-mode.md`. |
| `phone` | E.164 + display format. If multiple phone numbers exist (KP vs business-promoted), supply `phone_canonical` in `constraints[]`. |
| `service_area_or_city` | Atlanta / metro region / specific neighborhoods |

### Recommended

R1VS researches if missing, but quality is higher when supplied:

- `owner_name` — improves review-attribution sanity
- `address` — lets Places API search by proximity if name search fails
- `year_founded` — explicit year beats inferred lineage
- `claim_code` — pre-created code, otherwise Mini injects fresh at deploy time
- `paperclip_job_id` — for cross-referencing in artifacts

### Constraints (override defaults)

The `constraints[]` array carries explicit per-prospect overrides Phase 2 honors verbatim:

- `phone_canonical: <e164>` — when multiple phones exist, this is the one that goes on the public site
- `address_treatment: storefront | service_area_admin` — default `service_area_admin` if SAB-detected; `storefront` only when verified physical location with customer-facing presence
- `tenure_lead: <year> | "20+ years"` — when LLC date differs from brand lineage (e.g., SmartWire's 2004 lineage vs 2020 LLC date)
- `services_whitelist: [<slugs>]` / `services_blocklist: [<slugs>]` — hard caps on which services appear; R1VS won't invent EV chargers, generators, panel upgrades unless whitelisted
- `accent_color_override: <hex>` — overrides per-vertical default; useful when two prospects in the same vertical need to look different (e.g., SmartWire `#1e40af` vs Plugged ATL `#0B60D6`)
- `exclude_domains_in_copy: [<domains>]` — e.g., parked domains
- `forbidden_phrases: [<phrases>]` — e.g., `"BBB Accredited"` when prospect is not BBB-accredited
- `hero_intent: aspirational | documentary | either` — passed through to Bruce's collect-request later
- `generated_images_allowed: yes | no | atmosphere-only` — passed through to Bruce

### Optional (R1VS uses scaffold defaults)

- `design_direction` — default: editorial dark mode + per-vertical accent (per `.impeccable.md` brand fingerprint)
- `page_structure` — default: 4 services × multi-page scaffold (`index`, `services`, `about`, `contact`, + 4 per-service pages)
- `image_requirements` — default: hero placeholder for Bruce; gallery slots open with `data-resolved="false"`

---

## 2. R1VS outputs (per phase)

| Phase | Artifact | Path | Required? |
|---|---|---|---|
| 0 — legitimacy | `legitimacy-check.json` (`passed: true/false` + reasons + snapshot data) | `sites/<slug>/legitimacy-check.json` | Always |
| 0 — audit trail | `gbp-data-from-kp.json` (manual KP scrape input — used when Places API ZERO_RESULTS forces fallback to chrome-devtools render) + `phase-0-evidence-google-kp.png` | `sites/<slug>/` | Conditional (only when manual scrape needed) |
| 1 — research | `RESEARCH.md` (10-section structured facts + sources, ends with §9 ambiguities/blockers) | `sites/<slug>/RESEARCH.md` | Always |
| 1 — voice | `BRAND.md` (3-word voice cluster, signature phrases verbatim with attribution, copy patterns to use/avoid, Phase 2 hero/trust/about/photo direction) | `sites/<slug>/BRAND.md` | Always |
| 2 — config | `business-data.json` (40 site keys + 4 services with full per-page content) | `sites/<slug>/business-data.json` | Always |
| 2 — icons | `icon-intent.json` (vertical, service_cards, actions) | `sites/<slug>/icon-intent.json` | Always |
| 3 — render | `index.html`, `services.html`, `about.html`, `contact.html`, 4× `<service-slug>-<city>.html`, filled `_base.css` | `sites/<slug>/*.html`, `_base.css` | Always |
| 3 — reviews stub | `reviews.json` (Path C `captured: 0` if Bruce hasn't run §11.11 yet) | `sites/<slug>/reviews.json` | Always |
| 3 — finalization | `<date>-r1vs-<slug>-finalized.md` | `messages/r1vs/` | Always (when Phase 3 succeeds) |

**Standard build = 9 HTML files + 1 CSS + 4 JSON + 2 markdown + finalization message.**

### What's in §9 of RESEARCH.md (Phase 1 ambiguities)

Severity-ranked, owner-assigned table:

| # | Item | Severity | Owner |
|---|---|---|---|
| ... | (one row per ambiguity surfaced during research) | High / Medium / Low | Bruce / Jesse / R1VS-Phase-2 |

Today's example (SmartWire): 8 items including license verification (Bruce), service confirmation (Bruce), verbatim Google reviews (Bruce — high), service-area neighborhood list (Jesse one-touch), hero generation (Bruce), tenure-lead copy guidance (R1VS Phase 2).

### What's NOT in R1VS output today

- **No screenshots** beyond the Phase 0 KP-evidence shot. Mini owns post-deploy live screenshots.
- **No Slack posts** by R1VS. Mini posts to `#claude-sync` after deploy.
- **No CRM mutations.** R1VS never writes to Supabase / HubSpot / etc.
- **No collect-request.md.** Bruce owns when/whether to engage §11.11 collection. R1VS surfaces what Bruce should pull in the finalization message but doesn't trigger it.

---

## 3. Where R1VS writes

- **Repo:** `bruce-workspace/gtmdot-sites`. Branch: `main`.
- **Push gate:** `internal source control only` — verified by R1VS before each session:
  - `.github/workflows/` does not exist (no GitHub Actions auto-deploy)
  - `gh api repos/bruce-workspace/gtmdot-sites/hooks` returns `[]` (no GitHub webhooks)
  - No top-level `wrangler.toml`, `_redirects`, `_headers`, `netlify.toml`, `vercel.json`
  - Cloudflare Pages deploys are manually invoked by Mini via `wrangler` from a separate Mac-mini-side staging directory (`gtmdot/sites/<slug>/`); a push to `gtmdot-sites/main` does not auto-deploy
- **Folders R1VS writes to:**
  - `sites/<slug>/` — per-prospect artifacts
  - `messages/r1vs/` — R1VS-authored coordination messages
  - `messages/` — DQ recommendations, blockers (root, not r1vs/ subfolder)
  - `proposals/` — proposed source-of-truth doc changes (awaiting Jesse ACK)
  - `docs/` — contract / process docs (this file lives here)

### Pre-push gate

`scripts/pre-push-gate.sh <slug>` — 7 checks:

1. fabrication-grep (known hallucination strings)
2. stock-image-grep (external stock hosts)
3. claim-bar-grep (R1VS must not inject claim bar / popup / cookie banner)
4. review-count-audit (`reviews.json captured` matches rendered review UI slots)
5. icon-intent-diff (`icon-intent.json` matches actual lucide icons in HTML)
6. proposal-gate (source-of-truth doc changes require visible Jesse ACK message)
7. generated-image-rules (§11.11.5 guardrails 1, 2, 3)

`scripts/verify-build.sh <slug>` — 7 checks:

1. asset resolution (every src/href resolves)
2. reviews.json vs review UI count parity
3. claim code presence (warn-only; Mini injects at deploy time)
4. stock image hosts (none)
5. fabrication patterns (none)
6. hero image existence (referenced hero must exist or be held for Mini)
7. generated-image proportion ≤30% per §11.11.5 guardrail 5

**R1VS does not push if either gate fails.** Both must report 7/7.

---

## 4. Signal definitions

| Signal | Trigger | Artifact |
|---|---|---|
| `phase_0_passed` | Phase 0 legitimacy-check passes all 6 rules | `legitimacy-check.json { passed: true }` committed |
| `phase_0_dq_recommended` | Phase 0 fails any rule (rating <4.5, reviews <10, farm pattern, no GBP match, dormancy >24mo, vertical blocklisted) | `legitimacy-check.json { passed: false, reasons: [...] }` + `messages/<date>-r1vs-<slug>-dq-recommended.md` |
| `phase_1_complete` | RESEARCH.md + BRAND.md committed, ambiguities surfaced in §9 | files at `sites/<slug>/`; finalization message NOT yet filed |
| `phase_2_complete` | business-data.json + icon-intent.json committed | files at `sites/<slug>/` |
| `phase_3_finalized_ready_for_bruce` | All 9 HTML rendered + both gates 7/7 + finalization message filed | `messages/r1vs/<date>-r1vs-<slug>-finalized.md` exists; **this is the ready-for-Bruce signal** |
| `blocked_jesse_decision` | R1VS hits a gate that requires human decision (DQ recommendation, ambiguous business name, conflicting constraint, contract amendment proposed) | `messages/<date>-r1vs-<slug>-blocked-jesse.md` with explicit decision tree |
| `blocked_source_material` | Phase 1 cannot meet quality bar from public sources alone (e.g., parked website + no GBP + no FB) | `messages/<date>-r1vs-<slug>-blocked-source.md` listing what's missing + what input would unblock |
| `blocked_build_quality` | Gates fail and R1VS can't self-resolve | `messages/<date>-r1vs-<slug>-blocked-build.md` with gate output + diagnosis |

### How signals are surfaced today

- **Filename + git commit subject** are the canonical signals
- Paperclip can subscribe via GitHub webhooks on push (filename pattern `messages/r1vs/*-finalized.md`, `messages/*-dq-recommended.md`, `messages/*-blocked-*.md`)
- OR R1VS upserts a row in a Supabase `r1vs_jobs` table on every phase transition with `phase_status`, `commit_sha`, `gate_result`, `next_action`

### How signals SHOULD be surfaced (proposed)

- R1VS upserts a Supabase row per phase transition (one row per slug, updated through phases)
- Paperclip subscribes to the Supabase row's status changes
- Slack post is a backup notification, not source of truth

---

## 5. §11.11 multi-page standard (current production)

### Required pages

- `index.html` — hero + trust strip + marquee + services teaser + reviews bar (Path A/B/C dynamic) + gallery + estimate band + CTA + footer
- `services.html` — eyebrow + h1 + lede + 4-up service grid + estimate band + CTA + footer
- `about.html` — eyebrow + h1 + 2-col intro + service area pills + owner section + story callout + estimate band + CTA + footer
- `contact.html` — eyebrow + h1 + lede + form with upload + aside (phone/email/hours/area) + footer
- N × `<service-slug>-<city>.html` — one per service in business-data.json; minimum 4 to fill the homepage service-grid

### Materially distinct = required

- Each per-service page has its own `h1`, `meta_description`, `body_paragraphs[4]`, `steps[4]`, `faqs[3]`, `photo_context`, `cta_subhead`
- No copy duplicated across service pages (pre-push-gate fabrication-grep catches template filler)
- No external stock images (pre-push-gate stock-image-grep)

### Source-backed copy expectations

- Every factual claim in RESEARCH.md cites a source URL (LinkedIn, BBB, Alignable, KP, Yelp, etc.)
- BRAND.md voice/phrases attribute to the source (owner copy vs. customer testimonial — never blur)
- business-data.json values trace back to RESEARCH.md or `constraints[]` — no inventions
- "Inferred" claims (e.g., "typical residential electrician offerings") explicitly marked in RESEARCH.md and kept conservative in business-data.json

### Placeholders for Bruce enrichment

- `<figure class="gtmdot-photo-slot" data-resolved="false" data-context="...">` on every photo (hero + 6 gallery + 1 about + 3 per service page = 22 slots for a standard 4-service build)
- `reviews.json { captured: 0, total_reviews: N, overall_rating: M }` if Bruce hasn't pulled yet → `render-reviews-bar.py` applies Path C (empty-state with GBP link)
- `icon-intent.json { hero: null }` if R1VS isn't generating the hero (Bruce does it via `hero_intent`)
- Claim bar **deliberately absent** — Mini injects from `gtmdot/sites/_shared/claim-ui.html` at deploy time

### What counts as "not actually multi-page"

- Single `index.html` with no service pages
- No JSON-LD per page
- No unique `<title>` / `meta` per service
- Generic copy not source-backed
- No per-service FAQs
- Mini's process-main-site.sh / process-intake.sh enforces this at deploy

---

## 6. Bruce's responsibilities (after R1VS finalization)

Per HANDOFF-CONTRACT.md §11.11 Asset Intelligence Layer:

- **Photo scrape** (GBP, Yelp, Facebook, Instagram, owner site if live) → `photos-raw/<source>-NN.jpg`
- **Review scrape** (verbatim text + dates + reviewer names + source) → `reviews-raw.json` → merged to `reviews.json`
  - For SAB GBPs (ftid=0x0): use cid on Place Details endpoint, **NOT** `findplacefromtext`
- **Hero generation** per `hero_intent` from collect-request → `photos-generated/hero-NN.png`
- **Photo-quality labels** (`role`, `confidence`, `caption-overlay-risk`, `object-context-OK`) → `bruce-asset-intel.{md,json}` per §11.11.6 + §11.11.7
- **Object/context verification** (does this look like an electrical shop / paint booth / etc.?)
- **Icon flag routing** (if a service-card icon doesn't match the actual service, flag back to R1VS via `messages/<date>-bruce-icon-flag-<slug>.md`)
- **Source reconciliation** (cross-check phone, address, year-founded across surfaces)
- **License verification** (e.g., GA SOS Construction Industry Licensing Board for trades)
- **Owner photo for ABOUT_PHOTO slot** — real headshot only, **never generated** (§11.11.1 forbids generating images that impersonate the actual owner)

Bruce surfaces all of this back via `bruce-asset-intel.{md,json}` + the corresponding photo files. R1VS's finalization message lists what Bruce should pull, in priority order.

---

## 7. Mini / Codex / Post-Build responsibilities

After Bruce's §11.11 deliverables land:

- **Photo integration:** copy `photos-raw/` + `photos-generated/` → `gtmdot/sites/<slug>/photos/` per Bruce's labels
- **`data-resolved` flip:** `false` → `true` on every photo slot post-integration
- **`<figcaption>` + alt-text injection** per Bruce's intel
- **`data-source="generated"`** on hero `<img>` per §11.11.5 guardrail 6
- **Claim bar / popup / cookie banner** injection from `gtmdot/sites/_shared/claim-ui.html` with **fresh** claim code
- **Claim code registration** with checkout system
- **Cloudflare Pages deploy** via `wrangler`
- **`verify-build.sh <slug> --live <url>`** post-deploy
- **Accessibility check** (WCAG AA contrast, keyboard nav, prefers-reduced-motion)
- **Mobile QA** (viewport breakpoints, touch targets, hamburger nav)
- **Impeccable / polish pass** (visual inspection; craft refinements if needed)
- **Final live QA** + Slack-ping Jesse for review
- **Supabase stage promotion** **gated on Jesse approval per stage** (research → site_built → ready_for_review → qa_approved → outreach_staged → outreach_sent)
- **Outreach release** (Poplar postcard + email sequence) **gated on final Jesse approval**
- **CRM contact records / attribution**

---

## 8. R1VS NEVER does

These are absolute prohibitions:

- CRM writes (Supabase, HubSpot, Apollo, etc.)
- Cloudflare Pages deploys / `wrangler` invocations
- Outreach sends (Poplar postcards, email sequences, Slack-to-prospect)
- Live email sends
- Claim-code generation or registration with checkout
- Modifying `ICON-MAPPING.md` / `HANDOFF-CONTRACT.md` / `CLAUDE.md` / `SKILL.md` / `DESIGN-HEURISTICS.md` without Jesse ACK (proposal-and-ACK gate per CLAUDE.md)
- Image generation (Bruce / §11.11.1 — R1VS only writes placeholders with `data-resolved="false"`)
- Mac mini state mutation (LaunchAgents, processes, secrets, payment flows)
- Pushing to branches other than `main` (intake/<slug> branches retired per current contract)
- Rotating secrets / credentials
- Claiming source truth without evidence — every Phase 1 fact must cite a source URL
- Hardcoded Supabase service-role JWT (per Bruce's Paperclip-pilot constraint — env vars only)

---

## 9. Queue-watching capability

### Today: NO autonomous queue watching

R1VS is **interactive-only**:

- Jesse opens a Claude Code session
- `bootstrap.sh` reads `messages/r1vs/` on session start (manual)
- R1VS works through the queue
- Session ends when Jesse closes it

The Mac Mini's `intake-pipeline-watcher` LaunchAgent (which would have triggered on `r1vs-finalized.md` files) **vanished in the OpenClaw 4.29/4.30 incident**. The `enrichment-dispatcher` LaunchAgent survived but watches Bruce-side photo/review thinness, not R1VS triggers.

### Aspirational: orchestrator plan filed, blocked on Bruce ACK

`messages/r1vs/2026-04-26-230000-r1vs-to-bruce-orchestrator-plan-for-review.md` proposes:

- A `next_action` enum-driven orchestrator running on Mac Mini in a separate clone
- Spawns R1VS via `claude code -p "<prompt>"` non-interactive on `needs_r1vs_build` actions
- Q4 (auto-spawn vs Slack-ping fallback) was **resolved** to (a) auto-spawn per the model-stack addendum
- Plan blocked on Bruce's responses to questions 1, 2, 3, 5, 6

### For Paperclip integration TODAY

Paperclip can:

1. Write a job spec to a Supabase `r1vs_jobs` table → emit a webhook
2. Mac Mini-side hook spawns `claude code -p` on R1VS-on-MacBook with the slug + input shape
3. R1VS picks up the job, runs Phase 0–3, writes phase artifacts to git + status to the `r1vs_jobs` row
4. On `phase_3_finalized_ready_for_bruce`, Paperclip routes to Bruce (collect-request creation, §11.11 trigger)
5. Bruce → Mini → Jesse QA → CRM stage promotion → outreach release; each step gated on the next signal

R1VS itself doesn't poll. The Mac Mini side is what triggers R1VS.

---

## 10. Artifact format preferences

### Input to R1VS (preferred)

JSON job spec on a Supabase row OR a Paperclip issue body. Example shape:

```json
{
  "paperclip_job_id": "PC-1234",
  "slug": "smart-wire-solutions",
  "business_name": "SmartWire Solutions LLC",
  "business_name_short": "SmartWire Solutions",
  "vertical": "electrical",
  "gbp_identity": {
    "type": "share_url",
    "value": "https://share.google/odJwB0uvcD08lbYxb",
    "kgmid": "/g/11j61b1qy5",
    "cid_hex": "0x41524a050c3d29f4"
  },
  "phone": {
    "e164": "+14043829847",
    "display": "(404) 382-9847"
  },
  "address_hint": "Midtown Atlanta",
  "owner_name": "Terry Henry",
  "year_founded_hint": null,
  "constraints": {
    "phone_canonical": "+14043829847",
    "address_treatment": "service_area_admin",
    "tenure_lead": "2004",
    "services_whitelist": [
      "electrical-repair",
      "ceiling-fan-installation",
      "recessed-lighting",
      "electrical-troubleshooting"
    ],
    "exclude_domains_in_copy": ["smartwire365.com"],
    "forbidden_phrases": ["BBB Accredited"],
    "hero_intent": "aspirational",
    "generated_images_allowed": "yes"
  },
  "design_direction": "default",
  "page_structure": "default"
}
```

### Output from R1VS

- **Artifacts:** files in git (`bruce-workspace/gtmdot-sites:main`)
- **Status updates:** Supabase `r1vs_jobs` row updates per phase transition (status enum below)
- **Audit:** full git history of `sites/<slug>/`
- **Optional:** Paperclip comment via API on each phase transition

### Status enum

```
phase_0_passed
phase_0_dq_recommended
phase_1_complete
phase_2_complete
phase_3_finalized_ready_for_bruce
blocked_jesse_decision
blocked_source_material
blocked_build_quality
```

### Slack

Backup-only notification surface, not source of truth.

---

## 11. Proposed Supabase `r1vs_jobs` table shape

```sql
create table r1vs_jobs (
  id uuid primary key default gen_random_uuid(),
  paperclip_job_id text,
  slug text not null unique,
  input_spec jsonb not null,            -- the JSON shape from §10
  status text not null,                 -- enum from §10
  phase_0_commit_sha text,
  phase_0_passed boolean,
  phase_0_reasons jsonb,
  phase_1_commit_sha text,
  phase_1_ambiguities jsonb,            -- §9 of RESEARCH.md, structured
  phase_2_commit_sha text,
  phase_3_commit_sha text,
  phase_3_finalization_message_path text,
  blocked_reason text,
  blocked_decision_required jsonb,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);
```

R1VS upserts on every phase transition. Paperclip subscribes via Supabase Realtime.

---

## 12. TL;DR for Codex's wiring task

1. Paperclip creates a job → writes JSON spec to `r1vs_jobs` table row keyed by `slug`
2. Mac Mini-side hook OR cron polls the table → on new row, spawns `claude code -p` invocation on R1VS-on-MacBook (via SSH or direct Claude SDK if wired)
3. R1VS reads the row, runs Phase 0–3, writes artifacts to `gtmdot-sites/main`, updates the row with phase status + commit SHA
4. On `phase_3_finalized_ready_for_bruce`, Paperclip routes to Bruce (collect-request creation, §11.11 trigger)
5. Bruce → Mini → Jesse QA → CRM stage promotion → outreach release; each step gated on the next signal

R1VS is the **deterministic phase-runner**. Paperclip + Supabase are the **orchestration ledger**. Bruce + Mini are the **enrichment + deploy + QA tier**. Jesse is **the only one who promotes CRM stages or releases outreach**.

---

## 13. Open questions for Codex

1. **Trigger mechanism on Mac Mini:** SSH-spawn `claude code -p` from Mini → MacBook? Or webhook → MacBook-side daemon? Or Paperclip issues a Mac Mini job that does the SSH itself?
2. **Supabase schema authority:** does the `r1vs_jobs` table shape above need Bruce's ACK, or is this Codex's call to wire?
3. **Paperclip → Supabase write order:** Paperclip writes the job row first, then notifies R1VS? Or R1VS pulls from Paperclip API directly?
4. **Slack backup channel:** keep `#claude-sync` as a notification mirror? Or retire entirely once Paperclip is the ledger?
5. **Failure recovery:** if R1VS crashes mid-phase, does Paperclip re-spawn with same `slug`? R1VS phases are idempotent — safe to re-run.
6. **Multi-prospect concurrency:** can R1VS-on-MacBook run two builds in parallel (separate `claude code -p` invocations)? Today they'd compete for the same git working tree.

---

— R1VS
