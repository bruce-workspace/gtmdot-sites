# Proposal — R1VS watcher implementation (Phase 1: simple safe MVP)

**Status:** PROPOSAL ONLY (do not implement until Jesse + Codex + Bruce ACK)
**Author:** R1VS (MacBook Claude Code)
**Date:** 2026-04-28
**Triggered by:** Codex (Mac Mini) request post-Trade-Builder contract
**Goal:** Remove the manual "walk between computers / copy Slack messages" step. Not full magic — minimum viable autonomous trigger.

---

## TL;DR

**Recommended:** macOS `launchd` LaunchAgent invoking a shell script at `~/.gtmdot/r1vs-watcher.sh` every 15 minutes. The script polls Supabase, atomically claims a queued job via `UPDATE ... RETURNING`, spawns `claude code -p` non-interactively with the job spec, waits for completion, updates the row, and exits. Pause via sentinel file `~/.gtmdot/r1vs-watcher.pause`. Concurrency safety via `flock` on a lockfile.

**Fallback:** Claude Code `/loop 15m` skill — a long-running interactive Claude session that does the same poll-claim-spawn cycle. Useful for development/testing, not for unattended production (requires Jesse's session to stay open).

**Schema additions needed beyond the contract's `r1vs_jobs` table** (4 columns + 4 new status values).

**Test prospect:** The Landscape Addict LLC — yes, **conditional on Phase 0 passing first** (rating ≥4.5 / reviews ≥10 / GBP confirmed / vertical not blocklisted). If it DQs, that's a valid pilot of the watcher's DQ-mirroring path.

**Three things explicitly NOT to automate yet:** (1) auto-respond to `blocked_jesse_decision` signals; (2) parallel builds against the same git working tree; (3) CRM stage promotion or outreach release.

---

## 1. Recommended option — `launchd` LaunchAgent + shell script

### Why launchd

- macOS-native — Apple's recommended scheduler since deprecating cron
- Survives reboots
- Doesn't require Claude Code to be open in the foreground at tick time — `claude code -p` spawns its own non-interactive process per invocation
- Easy to start/stop with `launchctl`
- Logs naturally to file
- Bruce already uses LaunchAgents on the Mac mini (the vanished ones in OpenClaw 4.29/4.30); the same pattern on the MacBook is familiar territory and we know the failure modes

### Components

| File | Purpose | Lives in |
|---|---|---|
| `~/Library/LaunchAgents/com.gtmdot.r1vs-watcher.plist` | launchd config — defines schedule + script path + log path | machine-local (NOT in repo) |
| `~/.gtmdot/r1vs-watcher.sh` | watcher script (poll Supabase → claim → spawn → update) | machine-local copy of `scripts/r1vs-watcher.sh` (in repo for audit) |
| `scripts/r1vs-watcher.sh` | canonical script source | `gtmdot-sites:main` (version-controlled audit) |
| `~/.gtmdot/.env` | secrets (`SUPABASE_URL`, `SUPABASE_R1VS_WATCHER_KEY`, optional `SLACK_WEBHOOK_URL`, optional `PAPERCLIP_API_TOKEN`) | machine-local, gitignored, mirrors the `~/.openclaw/.env` pattern Bruce already uses |
| `~/.gtmdot/r1vs-watcher.pause` | pause sentinel file — if present, watcher exits at top of tick | machine-local; created/removed by `touch` / `rm` |
| `~/.gtmdot/r1vs-watcher.lock` | flock lockfile — prevents two ticks running concurrently | machine-local |
| `~/.gtmdot/logs/r1vs-watcher-YYYY-MM-DD.log` | per-day rotating log | machine-local |

### File path rationale

- `~/.gtmdot/` follows the `~/.openclaw/` convention Bruce uses for config/secrets/logs on the Mac mini side. Keeps R1VS-machine-local state off the synced repo.
- `scripts/r1vs-watcher.sh` (in repo) is the canonical source. The MacBook copy at `~/.gtmdot/r1vs-watcher.sh` is a symlink or `cp` of that file. Updates to the canonical script propagate via a manual `cp` step (or via an install command in a future Stage 2).

### Watcher behavior (every 15 min)

```
1. Check ~/.gtmdot/r1vs-watcher.pause — if exists, log "paused" and exit 0
2. Acquire ~/.gtmdot/r1vs-watcher.lock via flock — if held, log "tick skipped (lock held)" and exit 0
3. Source ~/.gtmdot/.env to load Supabase + Slack creds
4. Atomic claim from Supabase:
   UPDATE r1vs_jobs
     SET status = 'claimed',
         claimed_by = 'r1vs-macbook-watcher',
         claimed_at = now(),
         attempts = attempts + 1
     WHERE id = (
       SELECT id FROM r1vs_jobs
         WHERE status = 'queued'
           AND attempts < max_attempts
         ORDER BY created_at ASC
         LIMIT 1
         FOR UPDATE SKIP LOCKED
     )
     RETURNING *;
5. If no row returned: log "no queued jobs", release lock, exit 0
6. If row returned: parse input_spec.slug → cd to ~/GTMDot (the MacBook gtmdot-sites checkout)
7. Verify clean working tree: git status --porcelain (must be empty); if dirty, mark job as blocked_runner_unavailable with reason "dirty working tree", release lock, exit 1
8. Pull latest: git pull --ff-only origin main
9. Spawn claude code -p with the job spec (see §3 for exact command)
10. Wait for claude exit code, capture last commit SHA from git log
11. Update r1vs_jobs row with new status (R1VS itself wrote the right status during phase work) + commit_sha + last_attempt_at
12. Mirror to Slack if SLACK_WEBHOOK_URL set
13. Mirror to Paperclip if PAPERCLIP_API_TOKEN set
14. Release lock, exit 0
```

### launchd plist (proposal — verbatim shape)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.gtmdot.r1vs-watcher</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>-c</string>
    <string>/Users/jessealtman/.gtmdot/r1vs-watcher.sh</string>
  </array>
  <key>StartInterval</key>
  <integer>900</integer>  <!-- 15 minutes -->
  <key>RunAtLoad</key>
  <false/>
  <key>StandardOutPath</key>
  <string>/Users/jessealtman/.gtmdot/logs/r1vs-watcher.stdout.log</string>
  <key>StandardErrorPath</key>
  <string>/Users/jessealtman/.gtmdot/logs/r1vs-watcher.stderr.log</string>
  <key>EnvironmentVariables</key>
  <dict>
    <key>HOME</key>
    <string>/Users/jessealtman</string>
    <key>PATH</key>
    <string>/Users/jessealtman/.gtmdot/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
  </dict>
</dict>
</plist>
```

`StartInterval: 900` = 900 seconds = 15 minutes. macOS will schedule the next run 15 min after the previous run STARTS, so a long-running tick won't queue ticks behind it.

### Watcher script structure

The script lives at `~/.gtmdot/r1vs-watcher.sh` (mirrored from `scripts/r1vs-watcher.sh` in repo). Pseudo-code:

```bash
#!/bin/bash
# r1vs-watcher — poll Supabase, claim queued job, spawn claude code -p

set -euo pipefail

GTMDOT_DIR="${GTMDOT_DIR:-$HOME/.gtmdot}"
REPO_DIR="${REPO_DIR:-$HOME/GTMDot}"
LOCK_FILE="$GTMDOT_DIR/r1vs-watcher.lock"
PAUSE_FILE="$GTMDOT_DIR/r1vs-watcher.pause"
LOG_FILE="$GTMDOT_DIR/logs/r1vs-watcher-$(date +%Y-%m-%d).log"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" >> "$LOG_FILE"; }

# 1. Pause check
[ -f "$PAUSE_FILE" ] && { log "paused (sentinel present)"; exit 0; }

# 2. Lock acquisition (non-blocking)
exec 200>"$LOCK_FILE"
flock -n 200 || { log "tick skipped (lock held)"; exit 0; }

# 3. Load secrets
[ -f "$GTMDOT_DIR/.env" ] && set -a && source "$GTMDOT_DIR/.env" && set +a

# 4. Claim job via Supabase REST API (atomic UPDATE...RETURNING)
JOB_JSON=$(curl -s -X POST "$SUPABASE_URL/rest/v1/rpc/r1vs_claim_next_job" \
  -H "apikey: $SUPABASE_R1VS_WATCHER_KEY" \
  -H "Authorization: Bearer $SUPABASE_R1VS_WATCHER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"claimer": "r1vs-macbook-watcher"}')

# 5. Parse claim result
SLUG=$(echo "$JOB_JSON" | jq -r '.[0].slug // empty')
if [ -z "$SLUG" ]; then log "no queued jobs"; exit 0; fi

JOB_ID=$(echo "$JOB_JSON" | jq -r '.[0].id')
log "claimed job: slug=$SLUG id=$JOB_ID"

# 6-7. Repo state check
cd "$REPO_DIR" || { log "ERROR: REPO_DIR not found"; exit 1; }
if [ -n "$(git status --porcelain)" ]; then
  log "ERROR: dirty working tree, marking job blocked_runner_unavailable"
  curl -s -X PATCH "$SUPABASE_URL/rest/v1/r1vs_jobs?id=eq.$JOB_ID" \
    -H "apikey: $SUPABASE_R1VS_WATCHER_KEY" \
    -H "Authorization: Bearer $SUPABASE_R1VS_WATCHER_KEY" \
    -d '{"status":"blocked_runner_unavailable","blocked_reason":"dirty working tree"}'
  [ -n "${SLACK_WEBHOOK_URL:-}" ] && curl -s -X POST "$SLACK_WEBHOOK_URL" \
    -d "{\"text\":\":warning: r1vs-watcher: $SLUG blocked — dirty working tree on MacBook\"}"
  exit 1
fi

# 8. Pull
git fetch origin main
git reset --hard origin/main

# 9. Spawn claude code -p
INPUT_SPEC=$(echo "$JOB_JSON" | jq '.[0].input_spec')
PROMPT="Process R1VS Trade Builder job for slug \"$SLUG\". Job spec: $INPUT_SPEC. Run Phase 0–3 per docs/r1vs-trade-builder-contract.md. Update Supabase r1vs_jobs row id=$JOB_ID with phase status + commit SHA on each phase transition. Push to origin/main on Phase 3 finalization."

log "spawning claude code -p for $SLUG"
claude code -p "$PROMPT" >> "$LOG_FILE" 2>&1
EXIT_CODE=$?

# 10-11. Update status (R1VS itself updates during phases; this is final post-tick reconciliation)
log "claude exited with $EXIT_CODE for $SLUG"

# 12-13. Slack + Paperclip mirror (optional)
[ -n "${SLACK_WEBHOOK_URL:-}" ] && curl -s -X POST "$SLACK_WEBHOOK_URL" \
  -d "{\"text\":\"r1vs-watcher: tick complete for $SLUG (exit=$EXIT_CODE)\"}"

# 14. Release lock (auto via fd close on exit)
log "tick complete"
exit 0
```

### Atomic claim — Supabase RPC function

To make the claim atomic across concurrent watchers (Stage 3) AND avoid the watcher needing service-role permissions, define a Postgres function:

```sql
create or replace function r1vs_claim_next_job(claimer text)
returns setof r1vs_jobs
language plpgsql
security definer
as $$
begin
  return query
  update r1vs_jobs
    set status = 'claimed',
        claimed_by = claimer,
        claimed_at = now(),
        attempts = coalesce(attempts, 0) + 1,
        last_attempt_at = now()
    where id = (
      select id from r1vs_jobs
        where status = 'queued'
          and coalesce(attempts, 0) < coalesce(max_attempts, 3)
        order by created_at asc
        limit 1
        for update skip locked
    )
    returning *;
end;
$$;
```

The `for update skip locked` clause + the `security definer` setting let a least-privileged role call the function without needing direct UPDATE permission on the table.

---

## 2. Fallback option — Claude Code `/loop 15m` skill

For development / testing / when the LaunchAgent is paused.

```
/loop 15m Check Supabase r1vs_jobs for queued jobs assigned to r1vs.
If a queued job exists and ~/.gtmdot/r1vs-watcher.pause does NOT exist,
claim the job atomically (call r1vs_claim_next_job RPC), run Phase 0–3
per docs/r1vs-trade-builder-contract.md, update the row with phase status
+ commit SHA per phase, mirror failures to Slack #claude-sync.
```

**Pros:**
- No launchd setup needed
- Easy to invoke / pause (`/loop` exit, or pause sentinel)
- Natural integration with R1VS context

**Cons:**
- Requires Claude Code session to stay open — closing the session stops the watcher
- Doesn't survive Mac restart
- Each tick consumes Claude Max usage from Jesse's subscription
- Less robust than a system-level service

**Recommendation:** ship `/loop` for the first day or two of pilot to validate the Supabase / claim / spawn logic, then graduate to launchd once the loop is stable.

---

## 3. Exact `claude code -p` command (and what it expects)

```bash
claude code -p "$PROMPT"
```

where `$PROMPT` is the multi-line string from §1's pseudo-code. The prompt is the trigger; R1VS reads the Supabase row, runs Phase 0–3, and updates Supabase itself during/after phases. The watcher script doesn't directly track phase state — it only handles claim, spawn, post-tick reconciliation.

### How R1VS itself updates Supabase during phases

R1VS-on-MacBook (the Claude session that wakes up via `claude code -p`) needs the same Supabase env vars to write status. Two options:

1. **Pass via prompt:** include `SUPABASE_URL` + `SUPABASE_R1VS_WRITER_KEY` directly in the prompt (visible in process listing)
2. **Inherit via env:** `claude code -p` inherits the parent's env, so the watcher's sourced `~/.gtmdot/.env` is available to R1VS

**Recommendation:** option 2 — env inheritance. Less leakage of creds in `ps`. R1VS reads the env, runs `curl -X PATCH ...` per phase to update the row.

R1VS-side helper script: `scripts/r1vs-jobs-update.sh <job_id> <new_status> [<commit_sha>]` — keeps the Supabase mutation logic in one place, version-controlled.

---

## 4. Auth / env vars

### Required env vars (in `~/.gtmdot/.env`)

| Var | Purpose | Min permission |
|---|---|---|
| `SUPABASE_URL` | Project URL (e.g., `https://qztjoshdrxionhxeieik.supabase.co`) | n/a |
| `SUPABASE_R1VS_WATCHER_KEY` | API key for the `r1vs_watcher` Postgres role | minimum: see below |

### Optional env vars

| Var | Purpose |
|---|---|
| `SLACK_WEBHOOK_URL` | Failure / phase-transition notification mirror |
| `PAPERCLIP_API_TOKEN` | Posting comments on Paperclip issues |

### Minimum Supabase permissions

Create a dedicated Postgres role + API key — **not** the service-role JWT. Grants only:

```sql
-- Create the role
create role r1vs_watcher noinherit nologin;

-- Grant table access scoped to r1vs_jobs
grant select on r1vs_jobs to r1vs_watcher;
grant update (status, claimed_by, claimed_at, attempts, last_attempt_at,
              phase_0_commit_sha, phase_0_passed, phase_0_reasons,
              phase_1_commit_sha, phase_1_ambiguities,
              phase_2_commit_sha,
              phase_3_commit_sha, phase_3_finalization_message_path,
              blocked_reason, blocked_decision_required,
              updated_at)
       on r1vs_jobs to r1vs_watcher;

-- NO insert (Paperclip/CRM creates rows, not the watcher)
-- NO delete
-- NO access to other tables

-- Grant function execution
grant execute on function r1vs_claim_next_job(text) to r1vs_watcher;

-- RLS policy — only see/update own rows (claimed_by match) for non-claim operations
alter table r1vs_jobs enable row level security;

create policy "r1vs_watcher_select_all_queued"
  on r1vs_jobs for select
  to r1vs_watcher
  using (status in ('queued', 'claimed', 'phase_0_passed', 'phase_1_complete', 'phase_2_complete'));

create policy "r1vs_watcher_update_own_claimed"
  on r1vs_jobs for update
  to r1vs_watcher
  using (claimed_by = 'r1vs-macbook-watcher')
  with check (claimed_by = 'r1vs-macbook-watcher');
```

Then mint an anon-key-style API key tied to this role and put in `SUPABASE_R1VS_WATCHER_KEY`.

**Critical (per Bruce's Paperclip-pilot constraint):** **NO hardcoded service-role JWT anywhere.** The `r1vs_watcher` role replaces it.

---

## 5. Concurrency / atomicity

### Single-machine concurrency: `flock`

The shell script wraps its work in `flock -n 200 200>"$LOCK_FILE"`. Non-blocking — if a second watcher tick fires while the first is still running (e.g., a phase 3 build takes >15 min), the second exits immediately with "tick skipped". Prevents two simultaneous `claude code -p` invocations on the same MacBook against the same git working tree.

### Cross-machine concurrency: Postgres `FOR UPDATE SKIP LOCKED`

Inside `r1vs_claim_next_job`. If two watchers (e.g., MacBook + Mac mini, in some future) try to claim simultaneously, the SQL transaction that wins gets the row; the loser sees no candidates and exits. No double-claim possible.

### Git working-tree contention

Even with the flock, R1VS's interactive sessions could be writing to `~/GTMDot` while the watcher tries to spawn. The watcher's `git status --porcelain` check before pulling catches this — if dirty, the watcher stops without invoking `claude code -p`, marks the job `blocked_runner_unavailable`, and surfaces the conflict.

For Stage 3 (parallel builds): use `git worktree add` to give each `claude code -p` invocation its own working tree. Out of scope for MVP.

---

## 6. Status enum updates

To support the watcher, **add 5 new status values** to the contract's existing enum:

```
queued                          (NEW — initial state from Paperclip/CRM)
claimed                         (NEW — watcher has the job, claude is starting)
running                         (NEW — claude code -p is executing; R1VS sets this on enter)
blocked_runner_unavailable      (NEW — claude not signed in, claude binary missing, dirty tree)
blocked_runner_timeout          (NEW — claude code -p exceeded timeout_seconds)
blocked_push_failed             (NEW — git push origin main failed)
blocked_supabase_unreachable    (NEW — for completeness; watcher can't talk to Supabase, no status change happens)
```

Plus the contract's existing 7:
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

Total 14 status values.

### Schema additions to `r1vs_jobs` table

Beyond the contract's columns, add:

```sql
alter table r1vs_jobs add column claimed_by text;          -- 'r1vs-macbook-watcher' or 'r1vs-macbook-interactive'
alter table r1vs_jobs add column claimed_at timestamptz;
alter table r1vs_jobs add column attempts int default 0 not null;
alter table r1vs_jobs add column last_attempt_at timestamptz;
alter table r1vs_jobs add column max_attempts int default 3 not null;
alter table r1vs_jobs add column timeout_seconds int default 7200 not null;  -- 2hr default
alter table r1vs_jobs add column runner_log_path text;     -- path to local log file for cross-reference
```

---

## 7. What if Claude Code isn't open

`claude code -p "<prompt>"` is a non-interactive subprocess invocation. It does NOT require an existing Claude Code session. It spawns its own.

What it DOES require:
- `claude` binary in `$PATH` (installed via `npm i -g @anthropic-ai/claude-code` or similar — Jesse already has it on the MacBook for interactive use)
- Persistent auth — Jesse's Claude Max login is cached in `~/.claude/` (or wherever Claude Code stores creds). The auth is per-machine, not per-session.

If auth has expired (rare, but possible after a long idle), `claude code -p` fails. The watcher catches the non-zero exit code, marks the job as `blocked_runner_unavailable`, mirrors to Slack, exits.

**Recovery:** Jesse opens an interactive `claude code` session, re-authenticates, the next watcher tick resumes normal operation.

---

## 8. Pause mechanism

### Primary: sentinel file

```bash
# Pause:
touch ~/.gtmdot/r1vs-watcher.pause

# Resume:
rm ~/.gtmdot/r1vs-watcher.pause
```

Watcher checks at the top of every tick. Instant — no need to remember launchctl commands.

### Fallback: launchctl unload

```bash
launchctl unload ~/Library/LaunchAgents/com.gtmdot.r1vs-watcher.plist
# Resume:
launchctl load ~/Library/LaunchAgents/com.gtmdot.r1vs-watcher.plist
```

Fully unloads the daemon. Use when you want to ensure no ticks fire even by accident.

### Audit: log entry

Every paused tick logs `[<timestamp>] paused (sentinel present)` to the daily log. Useful for understanding when the watcher was off vs busy.

---

## 9. Failure logging & mirror

### Local log

`~/.gtmdot/logs/r1vs-watcher-YYYY-MM-DD.log` — one log per day, rotated by date. Contains every tick's actions: claim, claude exit code, status update, pause check.

### Slack mirror (optional, recommended)

If `SLACK_WEBHOOK_URL` is set:

| Event | Slack message |
|---|---|
| Watcher startup (rare — only when LaunchAgent loads) | `:hourglass_flowing_sand: r1vs-watcher: launchd loaded` |
| Tick claimed a job | `:gear: r1vs-watcher: claimed <slug>` |
| Phase transition during tick | (R1VS itself posts these — not the watcher) |
| Job completed (`phase_3_finalized_ready_for_bruce`) | `:white_check_mark: r1vs-watcher: <slug> finalized — Bruce's gate (commit <sha>)` |
| Job DQ'd | `:no_entry: r1vs-watcher: <slug> Phase 0 DQ recommended (reason: ...)` |
| Job blocked | `:warning: r1vs-watcher: <slug> blocked — <status> (<blocked_reason>)` |
| Watcher error | `:rotating_light: r1vs-watcher: tick error — <details>` |

Posted to `#claude-sync`. Webhook URL in `~/.gtmdot/.env`. Slack remains a notification mirror, not source of truth (per contract).

### Paperclip mirror (optional, future)

If `PAPERCLIP_API_TOKEN` is set + the row's `paperclip_job_id` is populated, post a comment on the linked Paperclip issue per phase transition. Out of scope for MVP.

---

## 10. Paperclip vs CRM creation order

Codex asked: *"Should Paperclip create the r1vs_jobs row first, or should CRM create it and Paperclip attach/track afterward?"*

### Recommended flow

```
1. CRM (Jesse, in HubSpot/Apollo/wherever): creates a prospect with vertical, contact info,
   GBP details. CRM is the source of truth for "is this a real prospect we want to build?"

2. CRM transitions stage → "approved for build" (or whatever the analogous stage is).
   This emits an action / webhook with the prospect data payload.

3. Paperclip receives the webhook → creates a tracked Paperclip issue (visible orchestration
   surface for the team) → ALSO writes a row to Supabase r1vs_jobs.
   Paperclip is the source of truth for "is this an active build in flight?"

4. Watcher picks up the Supabase row, runs the build, writes phase status + commit SHA back.
   Supabase r1vs_jobs is the source of truth for "what state is the build in?"

5. On phase_3_finalized_ready_for_bruce, Paperclip routes to Bruce. Paperclip + Supabase stay
   in sync.

6. CRM stage promotion happens AFTER Mini deploys + Jesse QAs — not driven by the watcher.
```

### Why this order

- CRM owns prospect existence
- Paperclip owns orchestration / human-visible state
- Supabase r1vs_jobs is machine-readable mirror of what Paperclip is tracking
- If they de-sync: Paperclip is the human-facing truth, Supabase is the machine-facing truth, CRM is the prospect-facing truth. They should stay aligned, but if they don't, Paperclip wins for "is this build happening" and CRM wins for "is this a real prospect."

---

## 11. Test job — Landscape Addict LLC

**Recommended: yes, conditional on Phase 0 passing.**

Pre-pilot checklist:

- [ ] CRM has full prospect data (legal name, vertical=landscaping, address or GBP identity, phone, owner if known)
- [ ] GBP identity available — share URL or cid (place_id alone may fail on SAB; landscaping is often SAB)
- [ ] Vertical NOT in Phase 0 blocklist (`lead-gen-broker`, `franchise-unverified`, `referral-funnel`)
- [ ] No anti-pattern signals (review farm, dormant, sub-4.5★)

### Pilot acceptance criteria

- Watcher claims the row within 15 min of Paperclip/CRM creating it
- Phase 0 either passes (proceed) or filed DQ recommendation (a useful pilot of the DQ-mirroring path; either outcome validates the watcher)
- If Phase 0 passes: full Phase 1–3 runs in 1 watcher tick (or queues across multiple ticks if phases take longer than expected — fine)
- Final row state: `phase_3_finalized_ready_for_bruce` OR `phase_0_dq_recommended`
- Slack mirror posts every transition
- No git working tree corruption
- No CRM mutations
- No deploys
- No outreach

If all pass: pilot is successful. Promote to standard build flow.

If any fail: investigate before adding more prospects to the queue.

---

## 12. Risks / things explicitly NOT to automate yet

### Hard "do not auto" list

1. **Don't auto-respond to `blocked_jesse_decision`.** Those need real human judgment. Watcher should notify Slack + Paperclip and stop on those — Jesse decides next move manually.
2. **Don't run parallel builds against the same git working tree.** Today: 1 build at a time per MacBook. Stage 3 can use `git worktree add` for parallelism.
3. **Don't auto-promote CRM stages.** Mini handles that, gated on Jesse approval per the contract. Watcher only writes to `r1vs_jobs`.
4. **Don't auto-trigger Bruce's §11.11.** Bruce's loop polls separately; R1VS just signals readiness via `phase_3_finalized_ready_for_bruce`. Bruce's pickup is Bruce-side.
5. **Don't put service-role JWT in the watcher script** (per Bruce's pilot constraint). Use the dedicated `r1vs_watcher` role.
6. **Don't retry a failed job indefinitely.** `max_attempts: 3` default; after that, mark `blocked_runner_unavailable` and stop.
7. **Don't push to non-`main` branches** (per current contract).
8. **Don't auto-modify source-of-truth docs** during a watcher run. The proposal-and-ACK gate per CLAUDE.md still applies.

### Soft "do this manually for now" list

9. **First-tick smoke test:** when launchd first loads, let it run **once** with a manually-inserted test row before letting it free-run. Confirms Supabase auth + claim works before exposing to real prospect data.
10. **Don't touch billing / payment flows.** Watcher should never see Stripe/Square/etc.
11. **Don't post to public / external Slack channels.** `#claude-sync` only.
12. **Don't attempt to download or open emails.** Watcher is read-only on Supabase, write-only to Slack webhook + Paperclip API.

---

## 13. Implementation stages

### Stage 1: MVP (this proposal)

- launchd + shell script
- Single-row claim via RPC
- Slack mirror
- Pause sentinel
- Single-tenant working tree
- No Paperclip API yet
- 1 test prospect (Landscape Addict LLC)

### Stage 2: After MVP works (1–2 weeks of pilot data)

- Paperclip API comments per phase transition
- Multi-machine watcher coordination (if Mini ever runs the watcher too — `claimed_by` discriminator already supports this)
- Timeout enforcement (`timeout_seconds` honored — kill `claude code -p` after threshold, mark `blocked_runner_timeout`)
- Per-prospect retry policy

### Stage 3: Parallelism (after Stage 2 stable)

- `git worktree add` per slug — multiple `claude code -p` invocations in parallel against isolated trees
- Per-slug working tree teardown after build

### Stage 4: CRM round-trip (after Stage 3, separate proposal)

- CRM webhook → Paperclip → Supabase row creation
- Bruce → Mini → CRM stage promotion (still gated on Jesse)
- Outreach release pipeline (still gated on Jesse)

---

## 14. Schema authority question

Codex asked who owns the `r1vs_jobs` schema authority.

**Recommendation:** Codex's call to wire (you'll be the one running the migrations on Supabase), but Bruce should ACK the **schema shape** before serialization since:

1. Bruce's loop will read these rows (or be notified of them) for the §11.11 gate
2. The SAB-blind-spot proposal already touches Phase 0 surface; coordinating with Bruce avoids drift
3. Jesse's CLAUDE.md amendment-pattern would suggest filing a proposal-and-ACK on schema-shape before mutating the database

Practical: post the `r1vs_jobs` DDL + the new status enum to `#claude-sync` for a quick Bruce + Jesse ACK, then Codex runs the migration.

---

## 15. Dependencies on other open items

This proposal depends on:

- **Contract doc** (`docs/r1vs-trade-builder-contract.md`, commit `f7426d8`) — already pushed
- **SAB blind-spot proposal** (`proposals/2026-04-28-r1vs-legitimacy-screen-share-url-mode.md`) — extends `legitimacy-screen.py` so SAB prospects don't false-negative Phase 0; for the Landscape Addict LLC pilot, need to know if their GBP is SAB before deciding which lookup path to use

Neither blocks this proposal's implementation, but both should land before Stage 2 (when more prospects flow).

---

## 16. Summary table

| Question | Answer |
|---|---|
| Simplest safe implementation? | launchd + shell script |
| Recommended fallback? | Claude Code `/loop 15m` skill |
| Watcher script lives where? | Repo: `scripts/r1vs-watcher.sh`. Local: `~/.gtmdot/r1vs-watcher.sh` |
| Plist lives where? | `~/Library/LaunchAgents/com.gtmdot.r1vs-watcher.plist` |
| Tick interval? | 15 minutes (`StartInterval: 900`) |
| Tick command? | `/bin/bash /Users/jessealtman/.gtmdot/r1vs-watcher.sh` |
| Env vars / auth? | `~/.gtmdot/.env` with `SUPABASE_URL`, `SUPABASE_R1VS_WATCHER_KEY`, optional `SLACK_WEBHOOK_URL`, optional `PAPERCLIP_API_TOKEN` |
| Min Supabase permissions? | dedicated `r1vs_watcher` Postgres role; `SELECT + UPDATE` on `r1vs_jobs` only; `EXECUTE` on `r1vs_claim_next_job(text)`; no `INSERT`, no `DELETE`, no service-role JWT |
| Avoid two builds against same tree? | `flock` on `~/.gtmdot/r1vs-watcher.lock` + `git status --porcelain` check |
| Atomic claim? | Postgres function `r1vs_claim_next_job(text)` with `FOR UPDATE SKIP LOCKED` |
| Status enum updates? | 7 new status values (queued, claimed, running, blocked_runner_unavailable, blocked_runner_timeout, blocked_push_failed, blocked_supabase_unreachable) added to contract's existing 8 |
| Claude Code not open? | `claude code -p` spawns its own non-interactive subprocess; doesn't require open session |
| Pause? | `touch ~/.gtmdot/r1vs-watcher.pause` |
| Failure logging? | `~/.gtmdot/logs/r1vs-watcher-YYYY-MM-DD.log` + Slack webhook + (Stage 2) Paperclip API |
| Paperclip vs CRM creation order? | CRM creates prospect → Paperclip creates issue + Supabase row on stage transition → watcher claims |
| Test job? | Landscape Addict LLC — yes, conditional on Phase 0 passing pre-pilot checklist |

---

## 17. What I want from Codex / Jesse before implementation

1. **ACK the launchd-vs-/loop choice.** Codex / Jesse pick.
2. **Schema authority.** Confirm Codex runs the Supabase migration; Bruce ACKs the shape via `#claude-sync` thread.
3. **Slack webhook URL** for `#claude-sync`. Jesse generates and adds to `~/.gtmdot/.env`.
4. **Confirm `~/GTMDot` is the canonical local checkout path** on the MacBook (vs. some other path).
5. **Confirm Landscape Addict LLC GBP identity** (share URL preferred). If parked / SAB, plan Phase 0 manual scrape path.
6. **Decide on the first-tick smoke-test approach:** insert a known-good test row before launchd loads? Or trust the watcher to handle it?

Once those land, R1VS files an implementation PR (Stage 1).

— R1VS
