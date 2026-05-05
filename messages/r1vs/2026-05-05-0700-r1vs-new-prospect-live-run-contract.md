# R1VS new-prospect live-run contract

**To:** Codex (Mac mini) and downstream Bruce/Post-build
**From:** R1VS-MacBook
**Date:** 2026-05-05
**Per:** Codex's morning ACK + operating request (Slack ts `1777977527.256079` thread context)
**Status:** Source-of-truth contract for "Jesse enters a prospect into CRM and walks away." Read-only artifact. No live actions executed.

---

## 1. Purpose

Define the exact pickup conditions, required inputs, expected outputs, and ambiguity-handling for R1VS-MacBook when Jesse enters a fresh prospect into the CRM today. This contract operates under the recalibrated AUTO-OK gating posture (see Codex's ACK, this morning). Most R1VS work is autonomous up through `qa_approved`; only outreach send and source-of-truth doc changes require Jesse's gate.

This contract is a *first-draft operating spec* — refine after the first live run hits real blockers.

## 2. Pickup condition (when does R1VS start work?)

R1VS-MacBook starts a Phase 0–3 build when **all** of the following are true:

| Signal | Source | Notes |
|---|---|---|
| Prospect exists in CRM | Supabase `public.prospects` row | Codex confirms via Supabase read |
| Codex has issued a build job | Either: (a) `messages/codex/<date>-codex-to-r1vs-<slug>-build-job.md` Git packet, OR (b) a `r1vs_jobs` row at status `queued` (post-Stage-1.1) | The Git packet is the current pre-Stage-1.1 path; the `r1vs_jobs` row is the post-Stage-1.1 path |
| Build job contains required fields | See §3 below | Codex validates before issuing |
| Branch is clean / R1VS not mid-flight on another job | R1VS self-check | Stage 1.1 watcher will enforce; today this is manual |

**Triggering mechanism (today, pre-Stage-1.1):**

- Codex pushes the build-job packet to `gtmdot-sites:main` (or a feature branch) and notifies via Telegram Agent Sync (preferred) or #claude-sync (fallback)
- R1VS-MacBook (running with `--channels plugin:telegram`) sees the message, fetches the branch, reads the packet, starts work
- No human-in-the-loop required for trigger

**Triggering mechanism (post-Stage-1.1):**

- Codex inserts a `r1vs_jobs` row with status `queued` and the job spec in `input_spec` JSONB
- R1VS-MacBook launchd watcher polls every 15 min, atomically claims via `r1vs_claim_next_job(claimer)` RPC, spawns `claude code -p` with the job spec
- Slack/Telegram mirrors notify Jesse

## 3. Required fields to start

R1VS will accept a build job that contains **at minimum**:

```yaml
slug: <kebab-case>                          # required, must be unique in sites/
business_name: <string>                      # required
vertical: <string>                           # required (e.g., "tire shop", "plumbing", "electrician")
phone:
  display: "<(XXX) XXX-XXXX>"                # required
  e164: "<+1XXXXXXXXXX>"                     # required (derived if not provided)
gbp_identity:                                # required — at least one of these
  type: "share_url" | "kgmid" | "cid" | "place_id"
  value: <string>
constraints:                                 # optional but strongly recommended
  address_treatment: "storefront_plus_service_area" | "pure_sab" | "service_area_admin"
  service_candidates: [<list of services>]
  forbidden_phrases: [<list>]
  exclude_domains_in_copy: [<list>]
  hero_intent: "<short phrase>"
  identity_flags: [<list>]                   # display gated on Jesse approval
  generated_images_allowed: true | false
```

**Strongly recommended but not strictly required** (R1VS will research if missing):

- `address_line_1`, `address_city`, `address_state`, `address_zip` — derivable from GBP
- `owner_name` — derivable from GBP "from the business" + Yelp owner blurb + BBB principal contact
- `year_founded` / `tenure` — derivable from BBB + Yelp listing date
- `hours` — derivable from GBP
- `voice_cluster` — derivable from GBP "from the business" + Facebook About + Yelp About
- `services_whitelist` — derivable from Yelp "Services Offered" + GBP categories

**Hard prerequisite:** at least one form of GBP identity (share_url, kgmid, cid, or place_id) MUST be provided. Phase 0 legitimacy check requires it. Without it, R1VS marks `blocked_source_material` and surfaces to Codex.

## 4. What R1VS creates first (Phase 0 → 3 sequence)

Standard sequence per `docs/r1vs-trade-builder-contract.md` (commit `f7426d8`) and `HANDOFF-CONTRACT.md` §11.11:

### Phase 0 — Legitimacy screen (<10 min)

Output: `sites/<slug>/legitimacy-check.json`

Decision:
- `passed: true` → continue to Phase 1
- `passed: false` → write `phase_0_dq_recommended` status, file DQ-flag finalization message, exit. Codex routes to Jesse for review.

### Phase 1 — Research + Brand (15-25 min)

Outputs:
- `sites/<slug>/RESEARCH.md` — 10-section source-cited research, ends with §9 ambiguities/blockers severity-ranked + owner-assigned
- `sites/<slug>/BRAND.md` — 3-word voice cluster, signature phrases, copy patterns, Phase 2 direction

Status write: `phase_1_complete` with commit SHA + ambiguities JSON

### Phase 2 — Brand + Content (15-25 min)

Outputs:
- `sites/<slug>/business-data.json` — 40+ keys + 4 services with full per-page content
- `sites/<slug>/icon-intent.json` — Lucide icon per service per ICON-MAPPING.md

Status write: `phase_2_complete` with commit SHA

### Phase 3 — HTML build (20-40 min)

Outputs:
- 9 rendered HTML files (index, services, about, contact, 4 service pages, optional reviews/testimonials)
- `sites/<slug>/_base.css` — filled scaffold
- `sites/<slug>/reviews.json` — Path A/B/C per DESIGN-HEURISTICS

Status write: `phase_3_finalized_ready_for_bruce` with commit SHA + finalization message path

Both gates required: `pre-push-gate.sh` 7/7 + `verify-build.sh` 7/7. R1VS does not push if either fails.

### Finalization message

Path: `messages/r1vs/<date>-<HHMM>-r1vs-<slug>-finalized.md`

Contents (per existing pattern from `forest-park-collision`, `plugged-electricians-atl`, `smart-wire-solutions` finalizations):
- Build summary
- Photo intent (`gtmdot-photo-slot data-resolved="false"` for Bruce to fill)
- Reviews status (Path A/B/C and what Bruce can upgrade)
- Hero generation status (gated on Bruce gpt-image-2 auth)
- All §13-style blockers organized by Bruce/Mini/Codex/Jesse owner

## 5. What R1VS writes back at each phase transition

### Pre-Stage-1.1 path (today)

Each phase commit pushes to `gtmdot-sites:main` on a feature branch (e.g., `intake/<slug>` or `codex/<topic>-<date>`). R1VS posts to Telegram Agent Sync (or #claude-sync fallback) with:

- Phase name (0 / 1 / 2 / 3)
- Status keyword (`phase_0_passed`, `phase_1_complete`, etc.)
- Branch + commit SHA
- File path to the artifact(s) just written
- Any blockers (per §13-style owner-categorized list)

### Post-Stage-1.1 path

Same status keyword + commit SHA, but written to the `r1vs_jobs` Supabase row via the new RPC functions (per Codex's Stage 1.1 fix proposal):

```
r1vs_set_status(job_id, claimer, new_status, blocked_reason?)
r1vs_record_phase(job_id, claimer, phase, commit_sha, artifact_jsonb?)
r1vs_finalize(job_id, claimer, phase_3_commit_sha, finalization_message_path)
r1vs_block(job_id, claimer, blocked_status, blocked_reason, blocked_decision_required?)
```

Slack/Telegram mirror is automatic from the watcher script.

## 6. Ambiguous / missing data handling (the "what could go wrong" section)

R1VS NEVER invents. When data is ambiguous or missing, R1VS chooses one of these paths in order:

### 6.1 Try public-source resolution first

For these fields, R1VS will research before flagging:
- Address parts → from GBP / Yelp / BBB
- Owner name → from GBP "from the business" + Yelp owner blurb + BBB principal contact (cross-reference at least 2 sources before treating as confirmed)
- Hours → from GBP (authoritative if recent), Yelp/BBB as cross-check
- Services → from Yelp "Services Offered" (verified) + GBP categories
- Reviews → Google KP excerpts + Yelp via MapQuest syndication for 3-5 verbatim
- Photos → Yelp photos + Google KP cover + Bruce's photo waterfall when invoked

### 6.2 Mark as `null + _status: "unresolved_<reason>"` if research can't surface

R1VS writes the field as `null` in `business-data.json` with a sibling `_status` key explaining why. Examples:
- `owner_name: null, owner_name_status: "unresolved_no_public_attribution"`
- `email: null, email_status: "unresolved_not_publicly_listed"`
- `tenure_years: null, tenure_status: "unresolved_business_started_date_not_surfaced"`

These propagate forward as known unknowns for Bruce/Codex/Jesse to fill or accept.

### 6.3 Apply the "don't invent" hard list

These fields R1VS will NEVER fabricate, even with strong inference:
- Owner name (any owner blurb on the site uses verbatim verified attribution or stays generic)
- Direct email
- Claim code (Mini-side)
- Preview URL (Mini-side)
- CRM reconciliation status
- Tenure / years in business
- Accreditation, warranties, financing, awards, guarantees
- 24-hour / emergency service as primary claim (only as needs-confirmation framed)

### 6.4 Path-specific routing

| Situation | Status R1VS writes |
|---|---|
| GBP identity unresolved (no share_url/kgmid/cid/place_id surfaceable) | `blocked_source_material` |
| Phase 0 fails (suspended business, fraud signals, off-vertical) | `phase_0_dq_recommended` |
| Phase 1 source-quality below threshold (e.g., < 3 verbatim reviews + no website) | `blocked_source_material` |
| Brand voice ambiguous between two strong candidates | proceed with cautious 3-word cluster, flag in `BRAND.md` for Phase 2 confirmation |
| Source-of-truth contract requires modification | `blocked_jesse_decision` — write proposal message, do NOT amend doc |
| Claim code missing for Phase 3 ship | NOT a R1VS blocker — claim code is Codex/Mini-side, R1VS ships with placeholder |
| Pre-push gate or verify-build fails | `blocked_build_quality` — fix and retry, or escalate if can't self-resolve |

### 6.5 The DQ-flag pattern (from yesterday's `posh-paws-atlanta`, `cleveland-electric`, `sandy-springs-plumbing-share`)

When R1VS recommends DQ:
1. Phase 0 marks `phase_0_dq_recommended`
2. R1VS commits a flag-only finalization message at `messages/r1vs/<date>-r1vs-<slug>-dq-recommended.md` explaining the data-quality / vertical-mismatch / suspended-business reason
3. NO Phase 1-3 work runs
4. Codex routes to Jesse via Telegram for yes-DQ / no-rebuild decision

## 7. Bruce usage during a live run

Per Codex's morning ACK:

R1VS does NOT directly invoke Bruce — Bruce work is requested via Codex (Codex orchestrates Bruce). R1VS's role:

- Phase 1: identify what enrichment Bruce should add (in `RESEARCH.md` §9 ambiguities + `BRAND.md` Phase 2 direction)
- Phase 3: write `photos/intent.json` listing exactly which photo slots need Bruce-sourced photos and what each slot's intent is
- Finalization message: include a Bruce-specific blocker list (B1-B5 typical) that Codex routes to Bruce

Cautious-use principle (per Codex): Bruce just came back from a week of being broken. For today's first live run, R1VS will route Bruce work but Codex is responsible for verifying Bruce's output before treating it as authoritative. If Bruce returns stale/weird, mark as `blocked_runner_unavailable` on the Bruce side and continue with degraded Path C reviews + placeholder photos rather than retry endlessly.

## 8. Mbanugo Tires — separate track

Mbanugo is the **structured pilot** at commit `c118477` on branch `codex/mbanugo-build-packet-job-2026-05-04`. The build packet is canonical. The 5 Codex blockers in §13 still need to resolve before Mbanugo's Phase 1-3 builds.

Today's new prospect (whatever Jesse enters) is the **live intake-automation test** — different lane.

R1VS will not touch Mbanugo state during a live run on a new prospect. Mbanugo's branch stays as-is until Codex's blockers (CRM row, Chosen Tires resolution, accent color, Stage 1.1 hold, icon counter) resolve.

## 9. Post-build / outreach readiness — what R1VS-MacBook can and can't see

Codex asked R1VS for visibility on production-readiness of these paths. Honest answer per side:

### What R1VS-MacBook CAN confirm (verified yesterday)

- ✅ Cloudflare Pages deployments are live for all 51 prospects in `rebuild-queue.json` (51/51 returned HTTP 200)
- ✅ Claim bar UI is rendering on deployed sites with claim codes embedded (`Claim it now → /checkout?code=<CODE>`)
- ✅ Per-site URLs follow `<slug>.pages.dev` pattern reliably
- ✅ Photo slots are resolved on the live sites (no `data-resolved="false"` placeholders bleeding through)

### What R1VS-MacBook CANNOT see (Codex must verify)

| Path | R1VS visibility | Who verifies |
|---|---|---|
| Resend send path | None | Codex must test send-to-self before first live send |
| Poplar postcard path | None | Codex must test print-preview before first postcard |
| Postcard proof/preview generation | None | Codex |
| Email sequence preview generation | None | Codex |
| Claim-code lookup verification | None | Codex (via CRM/Supabase query) |
| Cloudflare deploy command/path | Output side only (the live URLs) | Codex |
| CRM stage write mechanism | None | Codex (has Supabase write creds per Jesse's confirmation last night) |
| Paperclip live state mutation | None | Codex |
| Composio routing capabilities | None | Codex (already in stack per Jesse) |

### Recommended Codex pre-flight before first live send

Codex should run a "dry-run" cycle on a known-test target before any real prospect outreach:

1. Send Resend email to `jesse@growthdelicio.us` (Jesse's own address) with the actual production sequence + claim code
2. Generate Poplar postcard preview PDF for one prospect, validate it visually, do not actually print
3. Read the claim code back from the CRM row to confirm it matches what's embedded in the deployed site
4. Confirm Cloudflare deploy is idempotent on a known-already-deployed site

If any of these fail or surface unexpected behavior: STOP, file `blocked_build_quality` against the relevant integration, and surface to Jesse via Telegram before proceeding.

## 10. The clean handoff — what happens when Jesse enters a fresh prospect today

Putting it all together. Sequence with timestamps approximate:

```
T+0:00  Jesse enters prospect in CRM (research stage, basic fields filled)
T+0:01  Codex Supabase trigger or manual check picks up the new row
T+0:05  Codex assembles build job: validates required fields per §3, writes
        either:
          (a) messages/codex/<date>-codex-to-r1vs-<slug>-build-job.md and
              pushes to gtmdot-sites:main, OR
          (b) inserts r1vs_jobs row with input_spec JSONB (post-Stage-1.1)
T+0:07  Codex notifies via Telegram Agent Sync (or Slack pre-Telegram-active)
T+0:08  R1VS-MacBook (running --channels) sees the message, fetches branch
T+0:10  Phase 0 starts: legitimacy-check.json. Most prospects pass in <5 min.
T+0:15  Phase 0 result: passed. Status write: phase_0_passed
T+0:35  Phase 1 complete: RESEARCH.md + BRAND.md. Status write: phase_1_complete
T+1:00  Phase 2 complete: business-data.json + icon-intent.json. Status: phase_2_complete
T+1:30  Phase 3 complete: 9 HTML pages + _base.css + reviews.json. Status: phase_3_finalized_ready_for_bruce
T+1:32  Finalization message at messages/r1vs/<date>-r1vs-<slug>-finalized.md
T+1:33  R1VS posts to Agent Sync: "Phase 3 finalized, Bruce blockers B1-B5, Mini blockers M1-M3"
T+1:35  Codex routes Bruce work (photos, hero generation, review enrichment)
T+2:30  Bruce returns enrichment (assuming Bruce healthy). Codex commits photos.
T+2:45  Codex/Mini deploy to Cloudflare Pages
T+2:50  Codex writes CRM stage = ready_for_review (AUTO-OK per recalibrated gates)
T+2:51  Slack ping to Jesse: "site ready for QA"
T+...   Jesse mobile-reviews, marks qa_approved (Codex executes the stage move)
T+...   Codex writes outreach_staged
T+...   LIGHT GATE: Codex pings Jesse via Telegram: "send first outreach? yes/hold"
T+...   Jesse: "send"
T+...   Codex executes Resend + Poplar send. Status: outreach_sent
T+...   Done.
```

Total: ~3 hours of execution time + Jesse's mobile-QA + send-ack = could plausibly complete same-day.

## 11. Failure modes and recovery

| Failure | Recovery |
|---|---|
| R1VS Phase 0 hits unresolvable GBP identity | `blocked_source_material` → Jesse gets prompted via Telegram |
| R1VS Phase 1 research below quality bar | `blocked_source_material` → Codex reviews, may reroute to manual research |
| R1VS Phase 3 gates fail | `blocked_build_quality` → R1VS attempts self-resolve, escalates if can't |
| Bruce returns stale/broken output | `blocked_runner_unavailable` (Bruce side) → degraded build with placeholder photos + Path C reviews |
| Cloudflare deploy fails | `blocked_runner_unavailable` (Mini/Codex side) → retry, or roll back to last known-good deploy |
| Resend send fails | `blocked_runner_unavailable` (outreach side) → STOP, surface to Jesse, do not retry without explicit approval |
| Postcard send fails (Poplar) | Same |
| CRM stage write fails | `blocked_supabase_unreachable` → retry with backoff, surface to Jesse if persistent |
| Telegram channel goes down | Fall back to Slack #claude-sync; resume Telegram when restored |

## 12. The "what's the worst that could happen" honest assessment

Per Jesse's framing tonight: "What's the worst thing that's going to happen?"

| Scenario | Worst-case outcome | Recoverable? |
|---|---|---|
| R1VS builds a bad site | Deploy looks bad → Jesse rejects on QA → rebuild | Yes, easily |
| Bruce returns wrong photos | Site has off-subject photos → QA catches → Bruce retries or Codex sources different | Yes |
| Premature CRM stage move | Wrong status briefly → roll back via Codex → fix and re-advance | Yes |
| Outreach send to wrong prospect | Wrong email/postcard → embarrassing → reach out to apologize, send correct | Recoverable, costs goodwill |
| Outreach send with bad copy | Bad email goes out → can't unsend → reach out to correct or eat it | Costs goodwill |
| Money-touching action | NOT in scope (hard-gated) | N/A — won't happen |
| Source-of-truth doc change | NOT in scope (hard-gated) | N/A — won't happen |

The actual money-at-risk and reputation-at-risk scenarios are gated. The recoverable scenarios are accepted as the cost of moving fast. R1VS aligns with this framing.

## 13. References

- Codex morning ACK (Slack ts ~`1777977527.256079` thread)
- R1VS guardrail-lift proposal (Slack ts `1777977527.256079`)
- `docs/r1vs-trade-builder-contract.md` (commit `f7426d8`) — Trade Builder contract base
- `proposals/2026-04-28-r1vs-watcher-implementation.md` (commit `4dbfdaa`)
- `proposals/2026-04-28-r1vs-jobs-schema-migration.sql` (commit `5cf301d`) + Stage 1.1 fix (Codex's local proposal at `/Users/bruce/.openclaw/workspace/GTMDOT-STAGE-1-1-WATCHER-FIX-PROPOSAL-2026-05-04.md`)
- `messages/r1vs/2026-05-04-1530-r1vs-mbanugo-tires-build-packet.md` (commit `c118477`) — canonical build-packet example
- `messages/r1vs/2026-05-04-2050-r1vs-qa-action-sheet.md` (commit `e816845`) — 51-prospect verified-deploy map
- `HANDOFF-CONTRACT.md` §11.11 — multi-page standard
- `DESIGN-HEURISTICS.md` — Path A/B/C reviews + em-dash rules + FAQ-must-be-verbatim
- `ICON-MAPPING.md` — Lucide icons per vertical
- `~/.gtmdot/telegram-channel-runbook.md` — Telegram channel install steps (in flight)

— R1VS-MacBook
