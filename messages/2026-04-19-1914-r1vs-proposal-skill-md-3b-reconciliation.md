---
from: r1vs
to: jesse
date: 2026-04-19T19:14:00-04:00
subject: Proposal — reconcile SKILL.md §3b multi-page spec with shipped single-page reality (+ pipeline dependency)
type: proposal (per CLAUDE.md §80-99)
topic: skill-md-3b-reconciliation
priority: normal — doc-only, not blocking
---

# Proposal — SKILL.md §3b: multi-page spec → single-page reality

## The gap

SKILL.md §3b (lines 276-306) reads:

> Build a complete multi-page site, not a one-pager. Minimum pages:
> - `index.html` — homepage
> - `services.html` — detailed service page
> - `contact.html` — contact form + info
> - `about.html` — full founder/owner story
>
> Plus per-service SEO pages: `/refrigerator-repair-atlanta.html`, etc.

**Every shipped live site contradicts this.** Single-page is the actual operating reality.

## Why reconciliation is needed, not just "aspiration" reclassification

Earlier today I proposed treating multi-page as aspirational while shipping single-page. Jesse confirmed single-page is the right call, and then Mini noted something I hadn't fully weighed: **Mini's entire deploy-side pipeline assumes single-page.** Specifically:

- `process-intake.sh` — copies intake branch content expecting single `index.html`
- `pre-deploy-gate.sh` — validates claim-bar presence, title tag, popup etc. against one file
- `heuristics-audit.py` — greps patterns (pull-quote classes, blockquote selectors) across one file
- `wire-photos-into-html.py` — maps Bruce-dropped photos into one HTML

**Multi-page isn't just "not what we ship" — it would break deployment automation.** That makes SKILL.md §3b not merely out of date but actively misleading: if a future R1VS session (or a new Claude instance) reads §3b literally and produces 4+ HTML files per site, Mini's pipeline fails silently or trips audit patterns that don't know about the extra files. That's the exact propose-and-wait failure mode CLAUDE.md §80-99 is designed to prevent.

## The recommendation

Amend SKILL.md §3b to:

1. **State single-page as the spec** — `index.html` contains the full rich-sectioned build (hero, stats, marquee, services grid, reviews section with 2-tier pull-quote + feed, story/timeline, area pills, FAQ, contact form, footer). Nav uses `#anchor` fragments.
2. **Cite the shipped reference sites** as the structural pattern (`sites/bobs-hvac`, `sites/cleveland-electric`, `sites/jack-glass-electric`, `sites/pine-peach-painting`).
3. **Cite the pipeline dependency** — deployment automation assumes single-page. Multi-page would require coordinated changes to `process-intake.sh`, `pre-deploy-gate.sh`, `heuristics-audit.py`, and `wire-photos-into-html.py` first.
4. **Preserve the multi-page aspiration as a "future expansion" note** — the per-service SEO pages (`/refrigerator-repair-atlanta.html` etc.) are still a valid ambition, just not something any session should ship unilaterally. If/when the pipeline is extended to handle multi-page, §3b gets re-amended.
5. **Cross-reference `R1VS-REBUILD-BRIEF.md`** — that brief already specifies `index.html` as the single file, and its scope (rebuild work) should win for scope conflicts per Jesse's earlier call.

## Proposed §3b replacement text (draft for your review)

```
### Phase 3: Build

**3a. Paper artboard** — unchanged, final polish only.

**3b. HTML preview site — single-page rich-sectioned build**

Build a single `index.html` with all standard sections inline:
- Hero (badge, accent headline, sub, actions, optional hero-quote)
- Stats widget (4 tiles)
- Marquee (scrolling credentials)
- Services grid (6-8 cards with Lucide icons per ICON-MAPPING.md)
- Reviews section — 2-tier (pull-quote + review-feed) per DESIGN-HEURISTICS §3
- Story / timeline / owner section
- Area pills
- FAQ (if scrape-source content exists)
- Contact form with service-type dropdown
- Footer (brand + services + contact)

Nav uses `#anchor` fragments for intra-page scroll. Mobile nav keeps full section list under hamburger.

Reference structural pattern: `sites/bobs-hvac`, `sites/cleveland-electric`, `sites/jack-glass-electric`, `sites/pine-peach-painting` (all shipped single-page).

**Why single-page:** deployment automation (`process-intake.sh`, `pre-deploy-gate.sh`, `heuristics-audit.py`, `wire-photos-into-html.py`) assumes one `index.html` per site. Multi-page would require coordinated pipeline changes — see `R1VS-REBUILD-BRIEF.md` for scope authority.

**Future expansion (not yet implemented):** Per-service SEO pages (e.g. `/kitchen-remodel-atlanta.html`, `/water-heater-install-roswell.html`) are a valid ambition for SEO ranking but require pipeline extensions first. Do not ship multi-page until Jesse and Mini coordinate the pipeline work.

**3c. Deploy** — unchanged.
```

## What I am NOT doing

- **Not amending SKILL.md in this iteration.** Per CLAUDE.md §80-99, source-of-truth docs require Jesse approval before commit. The file stays as-is until you ACK.
- **Not batching this with the finalization.** Two messages, each self-contained. You can ACK one without the other.
- **Not assuming this is urgent.** The 15 sites I just finalized don't depend on this. The Phase B handoff works today. This is about not leaving a landmine for the next session that reads SKILL.md literally.

## What I need from you

One of:
- **"Amend per proposed text"** → I commit the SKILL.md update with a reference to this approval in the commit body.
- **"Amend but edit the draft text"** → give me the diff you want, I commit that.
- **"Defer"** → leave SKILL.md as-is, add a one-line warning comment at top of §3b noting "see current shipped pattern" and revisit later.
- **"Reject"** → multi-page is the goal; let it stay as aspiration. I'll note that in a follow-up so next session doesn't trip over this again.

No loop armed after this. Finalization + proposal both on main.

---

*R1VS doing propose-and-wait correctly per CLAUDE.md §80-99. The 2-pass-variant unwind cost one revert + one Mini notification + 15 HTML backfills. This proposal is paying the tax in advance instead of paying it in remediation.*
