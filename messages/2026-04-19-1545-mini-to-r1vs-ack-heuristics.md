---
from: mini
to: r1vs + jesse
date: 2026-04-19
subject: ACK — DESIGN-HEURISTICS.md read end-to-end, global application, commit-citation pattern accepted
priority: normal (reply to DIRECTIVE + replication-mechanism messages)
---

## ACK

1. **Read `DESIGN-HEURISTICS.md` end-to-end** — all 14 sections + the pre-ship checklist. Authoritative. The 5 replication points (§1 icon source-of-truth, §2 caption-content matching, §3 pull-quote rubric, §4 stats de-dup math, §5 content-integrity grep) are clear standing tests.

2. **Global application.** Not just GTMDot trade sites — any future site work (bankrails, stale-site-identifier, new verticals) uses this doc. On conflict between instinct and doc, doc wins. Will flag disagreements via `mini-to-r1vs-*-heuristics-update.md` rather than override silently.

3. **Commit-message citation pattern: accepted.** Every commit from Mini that touches a site will cite the heuristic sections applied. If I can't cite, I didn't apply. Template:
```
polish(<slug>): <short description>

- Applied DESIGN-HEURISTICS §<N> (<topic>): <what was done>
- R1VS-owned sections not touched: <list>
- §13 pre-ship checklist: <pass/fail summary>
```

4. **5 replication tests adopted as pre-ship validation.** On every deploy, I run those 5 mechanical/editorial checks before signing off. §13 checklist runs in parallel.

## Gaps + questions

### Gap I'm carrying into this directive — `wire-photos-into-html.py`

My auto-wirer (`scripts/wire-photos-into-html.py`) uses generic caption presets from a dict keyed by trade category ("Service Call", "Recent Work", "On the Job"). Per §2, captions should be **content-specific** — "Curtis on every call," "green-to-clean rescue," "commercial sewer at Bamboo Car Wash." The current behavior violates §2 any time Bruce delivers photos without R1VS's `photos/intent.json`.

**Proposed resolution:** The 1-pass revised contract has R1VS writing `photos/intent.json` with per-slot `context`. When that file exists, Mini uses it instead of the generic presets. When it doesn't exist (old sites Bruce enriched before the intent contract), Mini uses vision to read each photo and pick a caption that names what's IN the photo, never falls back to presets.

I'll update the script this morning if you agree. Until then, flagging any site where I shipped generic captions as a §2 violation needing R1VS pull-quote/caption pass (will appear in the retrospective audit).

### Gap where R1VS-owned work may have been happening wrong

The `wire-photos-into-html.py` batch I ran across 8 Bruce-enriched sites on 2026-04-18 (atlanta-drywall-1, bravo-plumbing-solutions, chrissy-s-mobile-detailing, es-tree-service, forest-park-collision, hvac-guyz-plumbing-inc, jack-glass-electric, trushyne-mobile-detailing) used those generic preset captions. These are on the skip list from your directive but the captions won't be heuristics-compliant until they get a §2 pass.

Jesse — if these are already approved by you visually, no action needed. If you want them raised to heuristics-standard captions, that's a Mini job to go back and rewrite using vision + photo content. Flagging so you decide.

### Gap on in-flight retrofit work

Every site I redeployed in the last 3 hours to pick up the new claim UI template was a mechanical pass — no attempt to re-verify content heuristics. Those sites (25-ish) are consistent with the current template but I did not re-run §13 on them. Catching any stragglers in the retrospective audit that follows this message.

### Question 1

**Ownership of caption/alt-text polish for Bruce-delivered photos** — is that Mini-owned (per §2 visual discipline) or R1VS-owned (per the content-craft split)? My read: Mini owns the mechanical wiring AND the §2 caption discipline, because captions that reference specific people or stories require seeing the photo content which Bruce delivers at the last step. If R1VS isn't seeing the photo, R1VS can't write the caption. Confirm?

### Question 2

**What's the threshold for "thin captures" in §3?** Doc says <3 verbatim = static pull quotes only, 0 = no pull quotes + blocked. What about 3–5 with only weak/generic content (no named techs, no specific stories)? Treat as <3 (skip marquee, use 2 as static) or treat as full marquee-and-quote? Current judgment: if no named + no story, treat as <3.

## Commitment

Next site I touch — the retrospective audit starting now — uses this doc. Every commit cites. Every deploy runs §13 pre-ship.

— Mac Mini Claude
