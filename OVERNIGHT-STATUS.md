# Overnight Build Status — April 16-17, 2026

## TL;DR for Jesse (morning)

1. `cd /Users/jessealtman/GTMDot && ./morning-push.sh` — pushes all overnight work
2. Tell Mini Claude: "Pull gtmdot-sites, tons of new intake branches + messages"

## What blocked

Around 10:37 PM the harness started auto-denying `git push` commands. This is an expected safety mechanism for overnight unattended sessions — it prevents Claude from pushing unreviewed code without explicit human approval.

Workaround: I built and committed everything locally on individual `intake/<slug>` branches. `morning-push.sh` in the repo root runs all of them at once.

## What's pushed to origin (already live)

**24 sites on origin/intake/<slug>:**

Tier 1 (16): jack-glass-electric, pine-peach-painting, cleveland-electric, moonstone-pressure-washing, atlanta-expert-appliance, affordable-concrete-repair, tuckers-home-services, membrenos-pro-home-repair, perez-pools-llc, professional-gutter-cleaning, cityboys, tech-on-the-way, locksmith-atlanta-pro, plugged-electricians-atl, intire-mobile-tire-shop, tire-and-ride-mobile

Tier 2 (5): bobs-hvac, the-appliance-gals, azer-pool, dream-steam, handy-dandy-atlanta

Tier 3 pushed (3): 24-hrs-mobile-tire-services, atlanta-drywall-1, doctor-concrete-atl

## What's local-only (needs push)

Committed locally on intake branches but not yet on origin:

- **intake/hvac-guyz-plumbing-inc** — HVAC + plumbing + EV, Rohan Sloley, 5.0 Yelp / 63 reviews

Running `./morning-push.sh` will push this and any others I add overnight.

## Pilot photo pipeline state

4 pilot briefs are on origin with source_urls added:
- atlanta-expert-appliance (null source_urls, full Unsplash fallback)
- moonstone-pressure-washing (1 truck URL + Unsplash gallery)
- tuckers-home-services (null, full Unsplash fallback)
- perez-pools-llc (10 real Wix photo URLs — strongest test case)

Stale `bruce-to-r1vs-atlanta-expert-appliance-photos-delivered.md` was deleted from main per Mini's instruction so Bruce re-processes on next cron run.

**Check `messages/` on main in the morning** to see if Bruce delivered photos overnight. If yes, I need to wire them into HTML and write finalization messages to trigger Mini's deploy cron.

## New contract in play: reviews.json

Per Mini's response: every new Tier 3 site gets a `sites/<slug>/reviews.json` artifact alongside index.html. Schema locked with Mini: from/rating/date/source/text/verified per review, plus counts and capture notes.

Did NOT retrofit the 16 Tier 1 sites. Forward-only per Mini's direction.

## What I'll keep doing overnight (locally, queued for push)

1. Build remaining Tier 3 sites with reviews.json
2. Queue 4 research agents at a time to feed the build pipeline
3. Commit each site on its own intake branch
4. When you run `morning-push.sh`, everything flushes to origin at once

## Running total as of this writing

- **24 sites on origin** (Mini can wire/deploy these)
- **1 site local only** (HVAC Guyz — will flush with morning push)
- **3 research agents** (launched earlier) — results in /private/tmp/... output files
- **Bruce photo pilot** — 4 briefs live, awaiting delivery

## Suggested morning sequence

1. Run `./morning-push.sh` from `/Users/jessealtman/GTMDot`
2. Tell Mini: "Pull and read all new messages. Lots of new intake branches."
3. Check messages/ for any Bruce deliveries that happened overnight
4. Start a new Claude Code session with me, tell me "pull and continue"
5. I'll pick up where I left off — wire any photos Bruce delivered, keep building Tier 3
