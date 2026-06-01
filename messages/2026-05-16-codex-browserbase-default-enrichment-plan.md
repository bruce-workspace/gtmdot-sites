---
from: codex
to: jesse
date: 2026-05-16T02:04:32Z
subject: Browserbase default enrichment plan and first backlog batch
priority: high
---

# Browserbase Default Enrichment Plan

Jesse direction: Browserbase should become the default browser/scraping layer for GTMDot enrichment. Bruce remains useful for enrichment judgment, photo/review synthesis, and gpt-image-2 asset generation, but Browserbase should replace Scrapfly as the primary browser execution layer where practical.

This is not a source-of-truth change by itself. Browserbase should produce evidence packets. CRM writes, outreach sends, deploys, and prospect-contact actions still require the normal gates.

## Current Setup Finding

I checked the obvious local env files.

- `/Users/bruce/.openclaw/.env` contains old Scrapfly variables.
- I did not find `BROWSERBASE_API_KEY` or `BROWSERBASE_PROJECT_ID` in the obvious env files.
- No Browserbase-backed GTMDot enrichment script was found in the obvious script inventory.

Action needed before Browserbase execution:

- Add or confirm `BROWSERBASE_API_KEY`.
- Add or confirm `BROWSERBASE_PROJECT_ID`, if the Browserbase API flow requires it.
- Keep Scrapfly only as temporary fallback until Browserbase has passed at least one real GTMDot enrichment run.

## Browserbase Role

Use Browserbase for public-source collection:

- official website contact/about/service pages
- Google Business Profile public facts where accessible
- Yelp
- Facebook public pages/photos
- BBB
- Yahoo Local
- Nextdoor where publicly accessible
- Thumbtack where publicly accessible
- Angi where publicly accessible
- Secretary of State / business registration lookups where applicable

Do not use Browserbase to bypass logins, payment walls, captchas, or explicit access controls.

## Required Output Per Prospect

For each enrichment run, produce a packet before any CRM write:

- `browserbase-evidence.json`
- `browserbase-enrichment.md`
- `photos-raw/<source>-NN.ext` for collected public photos, where allowed
- source URLs
- timestamps
- screenshots or screenshot paths where practical
- extracted email/phone/address candidates
- review snippets with exact source labels
- confidence level for each candidate field
- known unknowns and blocked sources

Suggested path:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/sites/<slug>/`

If the site is not present under `gtmdot-sites/sites/<slug>`, write a coordination packet under:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/`

until the canonical site/source folder is created or reconciled.

## First Enrichment Batch

Prioritize prospects that are near approval or stuck in needs_enrichment and have weak/no hero imagery, weak/no service imagery, missing email, missing screenshot, or thin source evidence.

### Batch A: Browserbase enrichment first

1. `premier-tv-mounting-atl`
   - Stage: `needs_enrichment`
   - Missing email.
   - No CRM hero source.
   - No CRM screenshot.
   - Existing website present.
   - Current `gtmdot-sites` dispatcher reports no R1VS artifacts, so use Browserbase/manual packet rather than relying on the old dispatcher.

2. `trushyne-mobile-detailing`
   - Stage: `needs_enrichment`
   - Missing email.
   - Open tasks: 3.
   - No CRM hero source.
   - No CRM screenshot.
   - Current dispatcher reports no R1VS artifacts.

3. `plumbingpro-north-atlanta`
   - Stage: `needs_enrichment`
   - Missing email.
   - Open tasks: 2.
   - Has site hero source but still needs source/contact confidence work.
   - Current dispatcher reports no R1VS artifacts.

4. `sumptuous-mobile-detailing`
   - Stage: `needs_enrichment`
   - Has email and reviews, but dry-run finds 0 canonical photos.
   - Good candidate for public photo/service image collection.

5. `thermys-mobile-tire-and-brakes`
   - Stage: `needs_approval`
   - Missing email.
   - Open tasks: 2.
   - Dry-run finds 0 canonical photos.
   - Needs postcard/site hero readiness review before approval.

### Batch B: gpt-image-2 / hero remediation first

These are less about Browserbase scraping and more about replacing stale or wrong-generation hero assets:

1. `forest-park-collision`
   - `heroImageSource` indicates MiniMax and needs gpt-image-2 regeneration per Jesse mandate.

2. `plugged-electricians-atl`
   - `heroImageSource` indicates MiniMax and needs gpt-image-2 regeneration per Jesse mandate.

3. `raiden-electrical`
   - `heroImageSource` indicates MiniMax.
   - Also has broken/incorrect preview path history and should not be treated as clean until live URL/path is verified.

### Batch C: approval queue with likely asset gaps

These may be further along than the stage suggests, but should get a lightweight Browserbase/source check plus postcard-preview check before Jesse spends time reviewing:

1. `cityboys`
2. `dream-steam`
3. `handy-dandy-atlanta`
4. `tuckers-home-services`
5. `intire-mobile-tire-shop`
6. `smartwire-solutions`

## Existing Dispatcher Limitation

`gtmdot-sites/scripts/enrichment-dispatcher.py --dry-run` currently looks only under:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/sites/<slug>`

That means many older or deploy-target-only prospects return:

`no-r1vs-artifacts-yet`

even when the CRM has a preview URL and the deploy target may exist elsewhere.

Do not treat that skip reason as proof that no enrichment is needed. It only means the dispatcher could not find the expected canonical R1VS source folder.

## Recommended Next Build Step

Create a Browserbase enrichment runner that can operate from CRM slug + public URLs, not only canonical site folders.

Minimum command shape:

`browserbase-enrich-prospect --slug <slug> --crm-read-only --sources website,gbp,yelp,facebook,bbb,nextdoor,thumbtack,angi,sos --write-packet`

Minimum safety defaults:

- read-only public browsing
- no CRM writes
- no deploys
- no outreach
- no paid third-party calls beyond Browserbase itself
- no login/captcha bypass
- write evidence packet only

## Operating Decision

For GTMDot going forward:

- Browserbase = default scraping/browser execution layer.
- Bruce = enrichment judgment, asset intelligence, gpt-image-2 image generation, and synthesis.
- Codex = orchestration, evidence packet validation, board clearing, post-build/outreach preflight.
- R1VS = site scaffolding and structure.

