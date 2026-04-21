---
from: mini
to: r1vs
date: 2026-04-20
subject: HANDOFF-CONTRACT §11 replaced — Bruce is now Collector only; Rule1 needs new Sources Attempted section in dossiers
priority: high — please adopt on next session start
---

## What changed

`HANDOFF-CONTRACT.md` §11 was replaced tonight (commit `2a6b935` on main). The old "Quality Standards" §11 is archived to `HANDOFF-CONTRACT-ARCHIVE.md`. Rule1 needs to read the new §11 on your next session start and adjust behavior accordingly.

**TL;DR of the change:** Bruce is no longer a partial-builder. Bruce is now a specialized scraper only (Yelp / Nextdoor / anti-bot sources). Mini (this session) absorbs everything that used to be Bruce's "enrichment phase" — HTML integration, caption writing, CSS filter application, claim bar, deploy, Supabase, Slack, email prep, postcard prep.

## Why this matters for Rule1

**One new responsibility for Rule1:** every dossier now requires a `## Sources Attempted` section documenting which sources Rule1 already scraped and what each returned. This prevents Bruce from re-scraping sources Rule1 already hit — it was the biggest source of wasted work under the old contract.

### Required format

Add this section to `RESEARCH.md` (or wherever the dossier lives) on every site:

```markdown
## Sources Attempted

| Source | Status | Photos Pulled | Reviews Pulled | Notes |
|---|---|---|---|---|
| Owner website | success | 4 | 0 | moonstonepressurewashing.com |
| Google Business Profile (Places API) | success | 7 | 10 | |
| Facebook | success | 3 | 0 | private posts not accessible |
| Instagram | failed | 0 | 0 | login wall |
| Yelp | not-attempted | — | — | requires persistent browser |
| Nextdoor | not-attempted | — | — | requires persistent browser |
| Thumbtack | not-attempted | — | — | requires persistent browser |
| BBB | success | 0 | 2 | profile scraped |
```

**Status values:** `success`, `failed`, `partial`, `not-attempted`.

**Rule:** If a source is listed as `success`, Bruce will not re-scrape it. If `failed` or `not-attempted`, Mini decides whether to request Bruce to try.

## What else changed (Rule1 impact)

### Things Rule1 no longer has to worry about

- **The `<!-- REVIEWS_LOADING -->` marker convention.** The old §11.3 required it; new §11 doesn't gate on it. Rule1 can still use a clean loading placeholder if captured < 3, but it's not a mandatory pre-publish block anymore — Mini handles integration outcome directly.
- **Upload module requirement inside Rule1's HTML.** Still a good idea for consistency, but it's no longer a hard bounce-back rule from Mini's pre-deploy gate.
- **Strict `feat(<slug>):` commit format for Bruce handoff.** Removed. Bruce now triggers only via `collect-request.md` files from Mini, not by scanning your commit messages.

### Things Rule1 still owns (unchanged)

- Research + `RESEARCH.md` authorship (plus the new Sources Attempted table)
- `reviews.json` initial capture via WebSearch / WebFetch / Places API / Brave / Firecrawl / Scrapfly — everything Rule1 already does
- `index.html` skeleton + copy + content-craft polish
- Pull quote selection (§3)
- Team cards + stats de-dup
- Icon selection per ICON-MAPPING.md
- `photos/intent.json` if you use placeholder photo paths

### Session consolidation note

Companion directive from Jesse 2026-04-20: the "submission and site build process" session on the Mini is being merged INTO the master site builder session (Mini, this session). The former submission session becomes post-approved handler, taking over at `qa_approved` stage for outreach triggers, email sequences, postcard send, CRM work. **No impact on Rule1's side** — you still hand off to Mini, Mini still stops at `ready_for_review` for Jesse's eyeball.

## Quick reference — new invocation flow

When Rule1 finishes a site under the new contract:

1. Rule1 writes `RESEARCH.md` (with Sources Attempted table), `reviews.json`, `index.html`, `photos/intent.json`, creates intake branch, commits + pushes.
2. Rule1 writes `messages/YYYY-MM-DD-HHMM-r1vs-<slug>-finalized.md` same as before.
3. **That's it for Rule1.** No expectation of further coordination with Bruce.

What happens next (for your awareness, not action):

4. Mini reads Rule1's dossier including Sources Attempted.
5. If Mini sees gaps (Yelp/Nextdoor/etc. not-attempted AND the site needs more photos), Mini writes `sites/<slug>/collect-request.md`.
6. Bruce's cron scans for `collect-request.md` files, executes scrape, writes raw files + `bruce-collected.md`.
7. Mini integrates Bruce's output + Rule1's partial, applies design heuristics §2, deploys.

## Full contract text

See `HANDOFF-CONTRACT.md` §11 (new) on main for the complete new rules including budget caps (§11.7), state ownership matrix (§11.8), invocation lifecycle (§11.9), and retirement conditions (§11.10).

## Questions / pushback

If you disagree with any part of the new contract, write a response message (`r1vs-to-mini-*-contract-feedback.md`) and flag it to Jesse. Per CLAUDE.md §80-99, further amendments require Jesse approval before commit.

No action needed tonight — just adopt on your next session start.

— Mini (master site builder)
