---
from: mini
to: jesse
date: 2026-04-20
subject: Overnight session summary — contract ratified, 3 sites redeployed, loop armed
priority: normal
---

# Tonight's work (summary for your morning coffee)

## Contract ratified + committed

- **New §11 "Bruce as Collector"** committed to `HANDOFF-CONTRACT.md` (commit `2a6b935`)
- Old §11 archived to `HANDOFF-CONTRACT-ARCHIVE.md` for audit trail
- **Rule1 notification** sent via `messages/2026-04-20-1919-mini-to-r1vs-contract-amended-bruce-as-collector.md` (commit `6d23ba4`). Rule1 will see it on next session start. Key ask: add a `## Sources Attempted` table to every dossier going forward.
- **New Bruce cron prompt** drafted and saved to `/tmp/bruce-cron-new-prompt.txt` — you'll need to paste into `~/.openclaw/cron/jobs.json` → `photo-brief-processor.payload.message` in the morning to switch Bruce to the new Collector-only behavior.

## Three sites redeployed under new contract

### 1. Moonstone Pressure Washing ✅
- **URL:** https://moonstone-pressure-washing.pages.dev
- **Claim:** `MOON4729`
- **Commit:** `c803d8c`
- **Changes:** Navy-blue cottage hero (from your GBP browse), 6 gallery slots with matching captions including real roof + exterior work shot (fills roof-service gap), 5 fresh reviews merged. Full breakdown in `messages/2026-04-20-1938-mini-to-jesse-moonstone-pressure-washing-deployed.md`.

### 2. Membrenos Pro Home Repair ✅
- **URL:** https://membrenos-pro-home-repair.pages.dev
- **Claim:** `MEMB2247`
- **Commit:** `7b624e8`
- **Changes:** Stock scattered-tools hero → real modern bathroom remodel. Gallery rewired with 6 real job photos including **fence repair** (new from Places API, fills the "handyman one call fixes everything" gap that had no fence photo before). 3 fresh reviews merged (total 8 verbatim).

### 3. Plugged Electricians ATL ✅ (with collect-request staged)
- **URL:** https://plugged-electricians-atl.pages.dev
- **Claim:** `PLUG3677`
- **Commit:** `2604909`
- **Changes:** Staged-kitchen catalog hero → real breaker panel with hand-written labels (authentic but visually plain). Gallery rewired with 5 real photos: Service Panel, New Construction, Ceiling Fan, Smart Controller, Panel Labeling.
- **Collect-request staged:** `sites/plugged-electricians-atl/collect-request.md` asks Bruce to hit Instagram (@plugged_electricians), Facebook, Yelp, Thumbtack, Nextdoor for a real photo of owner Sherea Jones ("The Female Electrician"). None of those sources are reachable from my current session — this is exactly what Bruce's Scrapfly access is for.

## What you need to do in the morning

1. **Eyeball the 3 live sites on mobile** — Moonstone, Membrenos, Plugged Electricians
2. **Apply the new Bruce cron prompt** — copy `/tmp/bruce-cron-new-prompt.txt` into `~/.openclaw/cron/jobs.json`. Once applied, Bruce will start scanning for `collect-request.md` files and executing scrapes. Plugged's collect-request is ready to be picked up.
3. **Greenlight or reject specific sites for Jesse Review stage progression** — they're all at `ready_for_review` now, which is where you eyeball. I don't progress them past that.

## What the /loop will do overnight

Armed for 25-min cycles. Each cycle:
- Pull main, check for new messages or Bruce output
- Pick the next unprocessed site from the ~47 remaining
- Audit existing photos + fetch Places API photos + Places reviews
- If the site can be fixed from this session (Places-reachable photos good enough) → rewire captions, swap hero if a better real photo exists, commit + deploy
- If the site needs Yelp/Nextdoor/Facebook/Instagram content → stage `collect-request.md` for Bruce and move on
- Slack ping per site deployed
- Leave a cycle-log message in `messages/` so you can see what got done

**Realistic overnight output: 6–10 sites fully redeployed + 10–15 collect-request.md files staged for Bruce.** I won't touch outreach triggers or stage transitions past `ready_for_review`.

## Constraints I'm keeping

- No touching `HANDOFF-CONTRACT.md` or other source-of-truth docs
- No stage transitions past `ready_for_review`
- No email or postcard triggers
- No Bruce cron config edits (you apply when you wake up)
- If I hit a blocker I'll stop the loop and leave a status message in `messages/` rather than silently spin

## Files staged for your morning review

- **New cron prompt:** `/tmp/bruce-cron-new-prompt.txt`
- **Moonstone proposal + comparison** (historical reference): `/tmp/moonstone-final-staging/`
- **Plugged collect-request** (already in repo): `sites/plugged-electricians-atl/collect-request.md`

Get some sleep. See you in the morning with more progress on main.

— Mini
