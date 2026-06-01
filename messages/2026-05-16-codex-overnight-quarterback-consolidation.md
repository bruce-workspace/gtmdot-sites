---
from: codex
to: jesse, gtmdot-platform, pre-build-coordination, post-build-operations, outreach-operations, bruce, r1vs
date: 2026-05-16T04:33:14Z
subject: Overnight GTMDot quarterback consolidation
priority: high
---

# Overnight GTMDot Quarterback Consolidation

## Scope

This pass stayed inside Jesse's overnight approval:

- Read-only CRM/API/file audits.
- Local GTMDot, CRM, and Paperclip inspection.
- Local coordination artifacts and lane status files.
- Browserbase read-only enrichment evidence only.

No CRM writes, deploys, Poplar sends, Resend sends, prospect/customer contact, DNS/domain/hosting/billing changes, Stripe actions, git pushes, destructive cleanup, production site edits, or paid outreach actions were performed.

## Control-plane state

Paperclip remains the intended orchestration/control plane, but the local Paperclip API is currently unavailable at `127.0.0.1:3199`.

The local Paperclip package and old `gtmdot-sandbox` server log were found under:

- `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/.npm/_npx/43414d9b790239bb/node_modules/paperclipai`
- `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox/logs/server.log`

The log proves the previous sandbox used:

- instance: `gtmdot-sandbox`
- API: `127.0.0.1:3199`
- embedded Postgres data dir: `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox/db`

However, the current instance folder only contains logs. The expected `config.json`, `db/`, `data/`, and `secrets/` folders are missing. A careful restart attempt with the existing home/instance/port failed because the CLI found no config and refused non-interactive startup.

Conclusion: do not create a fresh Paperclip board by onboarding. Treat Paperclip as blocked until the old instance data/config is recovered or Jesse explicitly approves rebuilding the sandbox from file artifacts.

## Active fallback ledger

Until Paperclip is recovered, the active safe control plane is:

- `gtmdot-sites/messages/status/*.md` for lane status.
- `gtmdot-sites/messages/*.md` for durable coordination packets.
- `paperclip-sandbox/artifacts/*.md` for issue-tree/gate artifacts that can later be rehydrated into Paperclip.

The most useful current lane files are:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/codex-pre-build-coordination-status.md`

## CRM board snapshot

Read-only CRM snapshot from production API:

| Stage | Count |
| --- | ---: |
| research | 2 |
| site_built | 0 |
| needs_enrichment | 9 |
| needs_decision | 3 |
| needs_approval | 11 |
| qa_approved | 7 |
| outreach_staged | 2 |
| outreach_sent | 13 |
| dead | 20 |

Total prospects in API response: 67.

## Outreach channel-state finding

`outreach_sent` is too coarse to operate safely.

Current `outreach_sent` has 13 prospects, but the real channel states are mixed:

- 13 have postcard status `submitted`.
- 0 have confirmed `in_production`, `mailed`, `delivered`, `returned`, or `suppressed`.
- 10 email sent events are recorded.
- 9 delivered events are recorded.
- 1 hard bounce is recorded.
- 0 replies are confirmed tracked.

Examples:

- `atlanta-drywall-1`, `atl-mobile-mechanics`, `done-right-drywall`, and `roberts-mobile-services` are postcard-only because no email is present, yet CRM still labels next action as `Send Email 1`.
- `affordable-concrete-repair` has an email but no email send is recorded.
- `tech-on-the-way` and `perez-pools-llc` have sequence 2 sent/delivered and are scheduled for sequence 3.
- `membrenos-pro-home-repair`, `moonstone-pressure-washing`, `atlanta-pro-repairs`, `morales-landscape-construction`, `locksmith-atlanta-pro`, and `golden-choice-prowash` are paused by open flags.
- `morales-landscape-construction` has a hard bounce and should not continue email follow-up without suppression/pause cleanup.

Conclusion: the CRM needs derived channel-state visibility at minimum: postcard state, email state, reply state, suppression/bounce state, and next-email due state. A single `outreach_sent` stage should not mean "all outreach channels completed."

## QA/backlog clearing snapshot

The next revenue-facing board clearing lanes are:

- `outreach_staged`: `the-appliance-gals`, `harrison-sons-electrical`
- `qa_approved`: `cityboys`, `sandy-springs-plumbing`, `dream-steam`, `handy-dandy-atlanta`, `tuckers-home-services`, `intire-mobile-tire-shop`, `smartwire-solutions`
- `needs_approval`: `thermys-mobile-tire-and-brakes`, `24-hrs-mobile-tire-services`, `piedmont-tires`, `forest-park-collision`, `bravo-plumbing-solutions`, `chrissy-s-mobile-detailing`, `rooter-pro-plumbing-drain`, `tuxedo-mechanical-plumbing`, `pine-peach-painting`, `raiden-electrical`, `browning-electrical-services`
- `needs_enrichment`: `premier-tv-mounting-atl`, `azer-pool`, `professional-gutter-cleaning`, `plugged-electricians-atl`, `trushyne-mobile-detailing`, `sumptuous-mobile-detailing`, `plumbingpro-north-atlanta`, `hvac-guyz-plumbing-inc`, `jack-glass-electric`

Priority logic:

1. Fix outreach channel-state visibility first, because otherwise sends and follow-ups are difficult to trust.
2. Audit `outreach_staged` and `qa_approved` prospects next, because these are closest to revenue.
3. Use Browserbase/Bruce enrichment on `needs_enrichment` prospects where missing hero/reviews/photos/email are the blockers.
4. Keep pre-build focused on Mbanugo/Landscape only after board-clearing lanes have a stable path.

## Browserbase/Scrapfly position

Browserbase is working and should be the default public enrichment browser layer.

Confirmed:

- `BROWSERBASE_API_KEY` and `BROWSERBASE_PROJECT_ID` are present in `/Users/bruce/.openclaw/.env` without exposing values.
- Browserbase API connectivity returned HTTP 200.
- Browserbase successfully loaded Thumbtack for the Premier TV Mounting/Premier TV Installs candidate and extracted useful evidence.

Limits observed:

- `premiertvmountingatl.com` failed through Browserbase with an upstream/tunnel/browser error. This is a blocked source, not proof that no evidence exists.
- No direct email was found in the first Browserbase pass.
- Identity reconciliation is required because CRM says `Premier TV Mounting ATL`, while Thumbtack evidence says `Premier TV Installs`.

Scrapfly should stay active for the next two weeks as fallback/comparison only. Use it when Browserbase fails on a specific public source, not as the default.

## Paperclip recovery recommendation

Do not onboard a fresh Paperclip instance overnight.

Recommended next steps:

1. Search for an old `gtmdot-sandbox` `config.json`, `db/`, `data/backups/`, or SQL backup outside the current visible instance folder.
2. If the old embedded Postgres backup cannot be found, create a Paperclip recovery issue from file artifacts only.
3. Rehydrate the current board from `paperclip-sandbox/artifacts/` and `gtmdot-sites/messages/status/` only after Jesse explicitly approves a local Paperclip rebuild.
4. Once Paperclip is live again, make every lane write both:
   - Paperclip issue/gate state
   - `messages/status/*-latest.md` as a durable fallback ledger

## Morning recommendations

### First

Run an Outreach Operations pass that produces a channel-state table for all 13 `outreach_sent` prospects:

- postcard submitted/in production/mailed/delivered/returned/suppressed
- email absent/not sent/sent/delivered/bounced/paused
- reply watcher active/inactive/unknown
- next email due date
- whether stale flags are blocking automation

Do not send anything or update CRM until this table is reviewed.

### Second

Audit the two `outreach_staged` prospects:

- `the-appliance-gals`
- `harrison-sons-electrical`

Goal: determine whether they are truly ready to launch outreach or whether stale flags/postcard/email/claim UI gaps are hiding.

### Third

Audit the seven `qa_approved` prospects for staging readiness:

- `cityboys`
- `sandy-springs-plumbing`
- `dream-steam`
- `handy-dandy-atlanta`
- `tuckers-home-services`
- `intire-mobile-tire-shop`
- `smartwire-solutions`

Goal: produce pass/fail blockers for postcard renderings, claim UI, mobile screenshot, email sequence, and stale flags.

### Fourth

Continue the Browserbase/Bruce enrichment lane on the highest-leverage `needs_enrichment` prospects:

- `premier-tv-mounting-atl`
- `trushyne-mobile-detailing`
- `sumptuous-mobile-detailing`
- `plugged-electricians-atl`
- `plumbingpro-north-atlanta`

### Fifth

Treat HeroUI Pro CRM v2 as GTMDot Platform work, not Outreach or Experimental. Build it as a safe lab dashboard route first, using the channel-state findings above as the design brief.

