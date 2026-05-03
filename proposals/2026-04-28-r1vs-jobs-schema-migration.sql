-- =====================================================================
-- Migration: r1vs_jobs queue + watcher infrastructure (Stage 1 MVP)
-- =====================================================================
--
-- Status: ACK'd FOR STAGE 1 ONLY by Codex + R1VS on 2026-04-28.
--         Bruce ACK unavailable due to OpenClaw 4.29/4.30 instability —
--         Bruce responded "standing by" to direct ACK/BLOCK request,
--         did not complete schema review.
--
--         Stage 1 does not modify Bruce runtime, does not auto-trigger
--         Bruce, does not write to Paperclip API, does not promote CRM
--         stages, does not deploy, does not release outreach. The
--         `phase_3_finalized_ready_for_bruce` status is a visible signal
--         only — Bruce/Mini continue using the existing manual/observed
--         handoff (messages/r1vs/<date>-r1vs-<slug>-finalized.md) for
--         Stage 1.
--
--         BRUCE ACK MUST BE REVISITED BEFORE STAGE 2/3, where Bruce/
--         Paperclip integration becomes active. Stage 2/3 cannot ship
--         without Bruce thumbing the schema shape. If Bruce wants
--         status names changed at that point, ALTER TABLE is cheap
--         while there are no Bruce-side dependents.
--
-- Author: R1VS (MacBook Claude Code)
-- Date:   2026-04-28
-- Refs:
--   docs/r1vs-trade-builder-contract.md (commit f7426d8) — table shape (§11)
--   proposals/2026-04-28-r1vs-watcher-implementation.md (commit d523c87) — watcher additions (§4–§6)
--
-- Codex on the Mac Mini runs this after the Stage 1-only ACK is recorded
-- in the #claude-sync watcher proposal thread (parent ts 1777769892.336259).
--
-- Idempotent: uses `if not exists` everywhere reasonable. Safe to re-run
-- if a partial migration occurred. NOTE: column adds are NOT idempotent in
-- vanilla Postgres — the script uses `do $$ ... $$` blocks to gate them.
--
-- Scope: Stage 1 MVP only.
--   - r1vs_jobs table
--   - r1vs_watcher role + grants + RLS
--   - r1vs_claim_next_job() RPC function
--   - NO Paperclip API integration tables
--   - NO CRM-side webhook handler tables
--   - NO trigger functions for status auto-mutation
-- =====================================================================


-- =====================================================================
-- 1. Table: r1vs_jobs
-- =====================================================================
-- Combines the contract's §11 columns + the watcher proposal's §6
-- additions into a single CREATE TABLE statement.
-- =====================================================================

create table if not exists public.r1vs_jobs (
  -- Identity
  id                              uuid primary key default gen_random_uuid(),
  paperclip_job_id                text,
  slug                            text not null unique,

  -- Input spec (the JSON shape from contract §10)
  input_spec                      jsonb not null,

  -- Status enum — 15 values total (contract's 8 + watcher's 7)
  --
  --   queued                          initial state from Paperclip/CRM
  --   claimed                         watcher has the job
  --   running                         claude code -p executing (R1VS sets on enter)
  --   phase_0_passed                  Phase 0 legitimacy-check passed
  --   phase_0_dq_recommended          Phase 0 failed; DQ message filed
  --   phase_1_complete                RESEARCH.md + BRAND.md committed
  --   phase_2_complete                business-data.json + icon-intent.json committed
  --   phase_3_finalized_ready_for_bruce  All gates 7/7 + finalization message filed
  --   blocked_jesse_decision          R1VS hit a gate requiring human decision
  --   blocked_source_material         Phase 1 cannot meet quality bar from public sources
  --   blocked_build_quality           Gates fail and R1VS can't self-resolve
  --   blocked_runner_unavailable      dirty tree / claude not signed in / binary missing
  --   blocked_runner_timeout          exceeded timeout_seconds
  --   blocked_push_failed             git push origin main failed
  --   blocked_supabase_unreachable    watcher can't talk to Supabase
  status                          text not null default 'queued',

  -- Phase artifacts
  phase_0_commit_sha              text,
  phase_0_passed                  boolean,
  phase_0_reasons                 jsonb,
  phase_1_commit_sha              text,
  phase_1_ambiguities             jsonb,
  phase_2_commit_sha              text,
  phase_3_commit_sha              text,
  phase_3_finalization_message_path text,

  -- Blocked context
  blocked_reason                  text,
  blocked_decision_required       jsonb,

  -- Watcher control plane (proposal §6)
  claimed_by                      text,
  claimed_at                      timestamptz,
  attempts                        int not null default 0,
  last_attempt_at                 timestamptz,
  max_attempts                    int not null default 3,
  timeout_seconds                 int not null default 7200,  -- 2 hr default
  runner_log_path                 text,

  -- Timestamps
  created_at                      timestamptz not null default now(),
  updated_at                      timestamptz not null default now(),

  -- Status enum guard (prevents typos at write time)
  constraint r1vs_jobs_status_valid check (status in (
    'queued',
    'claimed',
    'running',
    'phase_0_passed',
    'phase_0_dq_recommended',
    'phase_1_complete',
    'phase_2_complete',
    'phase_3_finalized_ready_for_bruce',
    'blocked_jesse_decision',
    'blocked_source_material',
    'blocked_build_quality',
    'blocked_runner_unavailable',
    'blocked_runner_timeout',
    'blocked_push_failed',
    'blocked_supabase_unreachable'
  ))
);

-- Index for the most common watcher query: oldest-first claimable
create index if not exists r1vs_jobs_claimable_idx
  on public.r1vs_jobs (created_at asc)
  where status = 'queued';

-- Index for paperclip cross-reference
create index if not exists r1vs_jobs_paperclip_idx
  on public.r1vs_jobs (paperclip_job_id)
  where paperclip_job_id is not null;

-- Trigger: maintain updated_at on every UPDATE
create or replace function public.r1vs_jobs_set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists r1vs_jobs_updated_at on public.r1vs_jobs;
create trigger r1vs_jobs_updated_at
  before update on public.r1vs_jobs
  for each row
  execute function public.r1vs_jobs_set_updated_at();


-- =====================================================================
-- 2. Role: r1vs_watcher
-- =====================================================================
-- Dedicated least-privilege role for the MacBook watcher. Replaces any
-- service-role JWT usage per Bruce's pilot constraint.
--
-- The watcher role:
--   - SELECT on r1vs_jobs (to see what's queued / what state)
--   - UPDATE on a tightly-scoped column list of r1vs_jobs (no row creation,
--     no row deletion, no schema mutation)
--   - EXECUTE on the r1vs_claim_next_job() RPC (the only path to atomic
--     claim of a queued job; the function itself runs as security definer)
--   - RLS-restricted UPDATE: can only mutate rows where claimed_by matches
--     the watcher's own claim identity ('r1vs-macbook-watcher')
-- =====================================================================

do $$
begin
  if not exists (select 1 from pg_roles where rolname = 'r1vs_watcher') then
    create role r1vs_watcher noinherit nologin;
  end if;
end
$$;

-- SELECT — broad view across all states the watcher needs to reason about
grant select on public.r1vs_jobs to r1vs_watcher;

-- UPDATE — column-scoped (no schema-mutation columns, no PK, no created_at)
grant update (
  status,
  claimed_by,
  claimed_at,
  attempts,
  last_attempt_at,
  phase_0_commit_sha,
  phase_0_passed,
  phase_0_reasons,
  phase_1_commit_sha,
  phase_1_ambiguities,
  phase_2_commit_sha,
  phase_3_commit_sha,
  phase_3_finalization_message_path,
  blocked_reason,
  blocked_decision_required,
  runner_log_path,
  updated_at
) on public.r1vs_jobs to r1vs_watcher;

-- DELIBERATELY OMITTED:
--   - INSERT (Paperclip/CRM creates rows; watcher never inserts)
--   - DELETE (no row deletion path)
--   - REFERENCES / TRIGGER / TRUNCATE
--   - access to other tables in the schema


-- =====================================================================
-- 3. Row-level security: r1vs_watcher can only mutate its own claims
-- =====================================================================

alter table public.r1vs_jobs enable row level security;

-- SELECT: watcher sees all rows (needed to find queued candidates)
drop policy if exists r1vs_watcher_select_all on public.r1vs_jobs;
create policy r1vs_watcher_select_all
  on public.r1vs_jobs
  for select
  to r1vs_watcher
  using (true);

-- UPDATE: only rows already claimed by this watcher identity
-- (the RPC bypasses this via security definer to perform the initial claim;
-- subsequent phase-status updates from R1VS go through this policy)
drop policy if exists r1vs_watcher_update_own on public.r1vs_jobs;
create policy r1vs_watcher_update_own
  on public.r1vs_jobs
  for update
  to r1vs_watcher
  using (claimed_by = current_setting('app.r1vs_claimer', true))
  with check (claimed_by = current_setting('app.r1vs_claimer', true));

-- The watcher script will set the GUC at session start:
--   set app.r1vs_claimer = 'r1vs-macbook-watcher';
-- This makes the policy machine-aware (Mac mini watcher would set a
-- different value and only see/mutate its own claims).


-- =====================================================================
-- 4. RPC: r1vs_claim_next_job(claimer)
-- =====================================================================
-- Atomic single-row claim. FOR UPDATE SKIP LOCKED prevents double-claim
-- across concurrent watchers (cross-machine). Runs as security definer
-- so the watcher role doesn't need direct UPDATE permission for the
-- INITIAL claim (subsequent mutations go through RLS).
--
-- Returns the claimed row (including input_spec) so the watcher script
-- can pass it to claude code -p without a follow-up SELECT.
--
-- Idempotent retry policy: the function increments attempts on every
-- claim. If a row exceeds max_attempts, it falls out of the candidate
-- pool until a manual reset.
-- =====================================================================

create or replace function public.r1vs_claim_next_job(claimer text)
returns setof public.r1vs_jobs
language plpgsql
security definer
set search_path = public
as $$
begin
  return query
  update public.r1vs_jobs
    set status         = 'claimed',
        claimed_by     = claimer,
        claimed_at     = now(),
        attempts       = coalesce(attempts, 0) + 1,
        last_attempt_at = now()
    where id = (
      select id from public.r1vs_jobs
        where status = 'queued'
          and coalesce(attempts, 0) < coalesce(max_attempts, 3)
        order by created_at asc
        limit 1
        for update skip locked
    )
    returning *;
end;
$$;

revoke all on function public.r1vs_claim_next_job(text) from public;
grant execute on function public.r1vs_claim_next_job(text) to r1vs_watcher;


-- =====================================================================
-- 5. (Optional) Smoke-test row
-- =====================================================================
-- Per Codex's first-tick approach: insert a manually-known-good test row
-- BEFORE enabling the watcher for real prospects.
--
-- This row uses a sentinel slug ('smoke-test-r1vs-watcher') that R1VS will
-- recognize and short-circuit through Phase 0 — no actual prospect data,
-- no real GBP lookup, just a round-trip exercise of:
--   1. Watcher sees the row (status=queued)
--   2. Watcher claims it via RPC (status=claimed)
--   3. Watcher spawns claude code -p
--   4. R1VS recognizes the smoke-test slug and writes phase_0_passed
--   5. Slack mirror confirms the round trip
--   6. Smoke-test row stays in the table for future re-runs
--
-- COMMENTED OUT until Codex is ready to insert. Run separately when the
-- watcher is enabled for the first time.
-- =====================================================================

-- insert into public.r1vs_jobs (slug, input_spec, status)
-- values (
--   'smoke-test-r1vs-watcher',
--   '{
--     "paperclip_job_id": "SMOKE-TEST",
--     "slug": "smoke-test-r1vs-watcher",
--     "_smoke_test": true,
--     "_note": "Recognized by R1VS as a watcher-loop validation row. R1VS will write phase_0_passed and stop."
--   }'::jsonb,
--   'queued'
-- )
-- on conflict (slug) do update set
--   status = 'queued',
--   attempts = 0,
--   claimed_by = null,
--   claimed_at = null,
--   blocked_reason = null,
--   updated_at = now();


-- =====================================================================
-- 6. Verification queries (run these post-migration as sanity checks)
-- =====================================================================

-- Confirm table + columns + constraint
-- select column_name, data_type, is_nullable
--   from information_schema.columns
--   where table_schema = 'public' and table_name = 'r1vs_jobs'
--   order by ordinal_position;

-- Confirm role + grants
-- select grantee, privilege_type, column_name
--   from information_schema.column_privileges
--   where table_name = 'r1vs_jobs' and grantee = 'r1vs_watcher'
--   order by privilege_type, column_name;

-- Confirm RLS enabled
-- select relname, relrowsecurity, relforcerowsecurity
--   from pg_class where relname = 'r1vs_jobs';

-- Confirm RPC exists + accessible
-- select proname, prosecdef from pg_proc where proname = 'r1vs_claim_next_job';

-- Round-trip test (only after smoke-test row is inserted):
-- set app.r1vs_claimer = 'r1vs-macbook-watcher';
-- select * from r1vs_claim_next_job('r1vs-macbook-watcher');
-- (should return the smoke-test row with status='claimed', attempts=1)


-- =====================================================================
-- End migration
-- =====================================================================
