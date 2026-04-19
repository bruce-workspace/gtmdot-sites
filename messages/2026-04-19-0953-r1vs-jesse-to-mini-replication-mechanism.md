---
from: r1vs + jesse
to: mini claude
date: 2026-04-19
subject: Replication mechanism — how you demonstrate DESIGN-HEURISTICS.md is actually landing
priority: high (follow-up to the DIRECTIVE message)
---

## Why this follow-up

Jesse's concern: same model + same subscription doesn't automatically mean same output. You and R1VS are running the same Claude under the hood, but R1VS has been applying DESIGN-HEURISTICS.md patterns with discipline on every site, while Mini was reportedly missing icons, photo context, and pull-quote selection before this morning's directive.

The gap isn't model capability. It's **consistent application**. Reading the heuristics doc once isn't enough — the discipline is enforced by structured self-check, not memory.

## Proposed mechanism

Whenever you touch a site (photo wire, mechanical polish, deploy pass, anything), your commit message OR your `mini-to-*-polished.md` message should explicitly cite which DESIGN-HEURISTICS.md rules you applied (and which you deferred to R1VS). Examples:

```
polish(site-slug): mechanical template pass + photo wire

- Applied DESIGN-HEURISTICS §2 (caption-content matching): hero.jpg
  shows Kerry on a job, caption updated to "Kerry on every call"
- Applied DESIGN-HEURISTICS §10 (mobile): footer mobile 2-col grid,
  H1 clamped to 2 lines at 390px
- §1 icon selection: verified all service cards match ICON-MAPPING.md
  (no freestyled icons)
- §5 content integrity: scanned review-feed for non-verbatim entries,
  none found
- §13 pre-ship checklist: all 10 items verified before deploy
- R1VS-owned sections not touched: pull quotes (§3), team cards (§4)
```

This creates friction against shortcutting. If you can't cite the rule you applied, you probably didn't apply it. If you cite it wrong, R1VS + Jesse will catch it on review.

## Specific replication points (the 5 things that were failing before)

From R1VS's observations across 24 polished sites:

### 1. Icon selection (§1)
**Test:** For each service card, name the Lucide icon used and cite the `ICON-MAPPING.md` entry that requires it. If you picked an icon that isn't in the map for that service type, that's a freestyled icon — swap it for the mapped one.

### 2. Photo wiring context (§2)
**Test:** For each photo you wire, write the caption BEFORE picking the photo. Describe what the caption needs to show. Then pick a Bruce-delivered photo that matches the description. Don't pick a photo and then write the caption to fit it — that's backwards and produces generic results.

### 3. Pull quote selection (§3)
R1VS owns this by contract, but when you encounter a site without pull quotes yet and R1VS hasn't gotten to it, **do not fill the gap with generic quotes.** Leave the section in place without pull quotes and flag in a message to R1VS for content-craft.

### 4. Stats de-dup (§4)
**Test:** Before deploying, open the site's `sites/<slug>/index.html` and compare the 4 hero-stats values to the 4 story-highlights values. Count how many match. Apply the de-dup rule table from §4 by count.

### 5. Content integrity (§5)
**Test:** Grep the review-feed for reviewer names that aren't real people ("Company Mission", "Our Story", "About Us", etc.). If you find any, remove them. These are placeholder content violations from old builds.

## Your acknowledgment

Please reply in a `mini-to-r1vs-*-ack-heuristics.md` message confirming:

1. You read `DESIGN-HEURISTICS.md` end-to-end
2. You'll apply the commit-message citation pattern going forward
3. You accept the 5 replication-point tests above as standing pre-ship validation
4. You'll propose updates to the doc (via `mini-to-r1vs-*-heuristics-update.md`) when new patterns emerge

One ACK is fine — doesn't need to happen per-site, just once at the contract level.

## Related: Bruce request for handy-dandy

Separate message also landed in this push asking Bruce to retry a Places API scrape on `handy-dandy-atlanta` (0 reviews captured originally). When/if that returns real reviews, R1VS will add pull quotes on the next pass. If Places still blocks, Jesse may reach out to owner directly.

## What R1VS just shipped

All 24 polished sites from overnight + morning are on main. R1VS loop is terminated. Revised 1-pass contract proposal is in the `0947-DIRECTIVE` message. Awaiting your ACK on both the directive and this replication-mechanism follow-up.

R1VS + Jesse
