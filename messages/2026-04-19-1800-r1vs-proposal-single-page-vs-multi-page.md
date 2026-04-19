---
from: r1vs
to: jesse
date: 2026-04-19T18:00:00-04:00
subject: Proposal — single-page (shipped pattern) vs multi-page (SKILL.md §3b) for Phase B HTML backfill
priority: HIGH — blocks HTML backfill loop
type: proposal (per CLAUDE.md §80-99)
topic: build-pattern-clarification
---

# Blocker for HTML backfill — need to confirm which pattern governs

## The contradiction

**SKILL.md §3b** (line 276-284) explicitly requires multi-page:

> Build a complete multi-page site, not a one-pager. Minimum pages:
> - `index.html` — homepage
> - `services.html` — detailed service page
> - `contact.html` — contact form + info
> - `about.html` — full founder/owner story
>
> Plus per-service SEO pages: `/refrigerator-repair-atlanta.html`, `/washer-dryer-repair-atlanta.html`, etc.

**Every shipped live site on main is single-page:**

| Site | Files |
|---|---|
| `sites/bobs-hvac/` | `index.html` only |
| `sites/cleveland-electric/` | `index.html` only |
| `sites/jack-glass-electric/` | `index.html` only |
| `sites/pine-peach-painting/` | `index.html` only |

I also grep'd the `origin/intake/bobs-hvac` branch (one of the recent R1VS-polished sites Mini redeployed today per `65ecc1c`) — still single-page. Same for `doctor-concrete-atl` and `rooter-pro-plumbing-drain`.

## Why this matters

- **Single-page × 15 backfill sites** = 15 index.html files, ~240 lines each, ~3600 total lines. Consistent with what's live.
- **Multi-page × 15 backfill sites** = 60+ HTML files (minimum 4 pages × 15, plus per-service SEO pages could push to 100+). Massive write volume, and they'd look nothing like any site that's ever shipped. The inline CSS would need to be extracted to a shared file or duplicated, the nav would need real cross-page links, and there's no proof the deploy pipeline handles multi-page routing correctly.

Getting this wrong is 60+ orphaned HTML files to rewrite. Exactly the failure mode the propose-and-wait rule is meant to prevent.

## My recommendation (hold for your ACK)

**Build single-page, matching the shipped bobs-hvac / cleveland-electric / jack-glass-electric pattern.**

Reasoning:
1. **Shipped reality is the strongest signal.** SKILL.md §3b looks like early-spec aspirational planning; the pattern that has actually made it through Mini's QA and deploy is single-page.
2. **Template parity matters for Mini's DESIGN-HEURISTICS pass.** Mini's audit grep patterns (per `65ecc1c` / `2026-04-19-1420-mini-to-r1vs-3-polished-redeployed`) were built against single-page structure. Multi-page would force audit-script changes too.
3. **Single-page fits the current claim-bar injection** (per CLAUDE.md: Mini injects the shared claim template at `_shared/claim-ui.html` before `</body>`). Injector assumes one `</body>` per site.
4. **Lower blast radius.** If this turns out to be wrong, unwinding 15 single-page files is small vs 60+ multi-page files.

## What I need from you

One of:

- **"Go single-page"** → I proceed with bobs-hvac-style single-page template for all 15 sites.
- **"Go multi-page"** → I follow SKILL.md §3b literally, build 4+ pages per site, and we accept the larger blast radius.
- **"Amend SKILL.md first"** → propose-and-wait on a SKILL.md §3b amendment that reconciles the spec with shipped reality, then do the backfill after the doc change lands.

Loop is halted pending your call. Not re-arming until you respond.

---

*R1VS doing propose-and-wait correctly this time per CLAUDE.md §80-99. Exact same failure mode (SKILL.md says X, reality shipped Y, I pick one and freelance) is what the new rule is meant to prevent.*
