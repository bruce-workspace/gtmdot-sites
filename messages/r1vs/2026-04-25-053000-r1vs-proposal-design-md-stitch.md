---
from: r1vs (MacBook Claude Code)
to: jesse, mini (Master Site Builder)
date: 2026-04-25
subject: PROPOSAL — DESIGN.md as a sidecar artifact per site (Stitch-compatible, additive only)
priority: normal — no rush, blocks nothing
refs:
 - Jesse's direction 2026-04-25 (ack on direction, dive into research first)
 - Stitch DESIGN.md spec: https://github.com/google-labs-code/design.md
 - Stitch skill ecosystem: https://github.com/google-labs-code/stitch-skills
 - Google announcement: https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/
---

## TL;DR

Add a per-site `design.md` artifact (Stitch's open-source format) that
captures the visual identity in a single Apache-licensed, AI-readable file.
**Nothing existing changes** — `business-data.json`, `_base.css`, the
multi-page scaffold, `fill-scaffold.py` all stay. `design.md` is a sidecar
that makes our designs portable to Stitch + Cursor + Copilot + any other
agent that reads the spec.

Lowest-friction path: generate `design.md` from data we already have (`gbp_snapshot.json` + `business-data.json` + the `VERTICAL_ACCENT_COLOR` we already pick). One new script, one new file per site, no other changes.

## What DESIGN.md is

Open-source spec from Google Labs (released March 2026, Apache 2.0,
already at alpha). Single file, two parts:

1. **YAML front matter** — machine-readable tokens (colors, typography, spacing, components)
2. **Markdown body** — human-readable rationale (why this color, when to use which type ramp, do's and don'ts)

Canonical sections (in this order): Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts.

Token types: hex colors, dimensions (px/em/rem), token references like `{colors.primary}`, typography objects (fontFamily/fontSize/weight/lineHeight). Components support `hover`/`active`/`pressed` variants.

There's an `@google/design.md` CLI for `lint`, `diff`, `export` (to Tailwind or W3C tokens), and `spec`.

## Why it fits GTMDot — three concrete wins

1. **Portability across agents.** Right now our design lives in `_base.css` (machine-readable) + scattered comments + my judgment. A new agent walking into a `sites/<slug>/` folder has no single place to read "what does this brand look like and why." DESIGN.md fixes that.

2. **AI-checkable design consistency.** With the front-matter tokens, an agent can verify that a `button.primary.backgroundColor` actually equals `{colors.brand}` and not some drift. That's structurally similar to the icon-intent.json check in `pre-push-gate.sh` — but for design tokens.

3. **Stitch as an optional design canvas later.** If/when you want a designer (or you, or me) to iterate visually in Stitch, we already have the design.md ready to import — Stitch reads it and respects it. No conversion step.

## What I'm proposing — three pieces

### Piece 1: NEW per-site artifact `sites/<slug>/design.md`

Stored alongside `business-data.json` and `gbp_snapshot.json`. Always
written when `fill-scaffold.py` runs. Generated from data we already have.

Sample shape for an electrical vertical site:

```markdown
---
version: alpha
name: Plugged Electricians ATL
description: Atlanta licensed electrician — repair, panel, EV chargers
colors:
  brand: "#0B60D6"
  brand-soft: "#E5EFFA"
  ink: "#1A1A1A"
  ink-soft: "#555555"
  paper: "#FFFFFF"
  paper-soft: "#F7F7F5"
  rule: "#E5E5E0"
  accent-emergency: "#D4351C"
typography:
  display:
    fontFamily: "Inter"
    fontWeight: 700
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Inter"
    fontWeight: 400
    lineHeight: 1.55
rounded:
  sm: 6px
  md: 10px
  lg: 16px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
components:
  cta-button:
    backgroundColor: "{colors.brand}"
    textColor: "{colors.paper}"
    rounded: "{rounded.md}"
    padding: "14px 24px"
  service-card:
    backgroundColor: "{colors.paper-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.rule}"
---

# Plugged Electricians ATL — Design system

## Overview
Atlanta licensed electrician serving Buckhead, Decatur, Sandy Springs.
Visual tone: **trustworthy, fast, modern**. Emergency-capable but not
loud — we don't want to look like a 2003 Yellow Pages ad.

## Colors
- **brand (#0B60D6):** primary actions, CTAs, link text. Cool, technical
  blue — fits "electrical" without using yellow caution-tape clichés.
- **accent-emergency (#D4351C):** reserved for the 24/7 emergency call
  button only. Never use elsewhere.
- ...

## Typography
Inter for both display and body. Display weights 700, body 400. Tight
letter-spacing on display headers (-0.02em) for editorial feel.

## Components
### cta-button
The single most visible element on every page. Uses `{colors.brand}` background
with `{colors.paper}` text. Hover state: 1px translateY, no color change.

### service-card
Used on services.html and homepage teaser grid. Subtle bordered card with
`{colors.paper-soft}` background. Icon at top-left, name + teaser below.

## Do's and Don'ts
- DO use `accent-emergency` for the 24/7 callout only.
- DO NOT use shadows on cards — borders only (consistent with our
  "modern not loud" tone).
- DO NOT introduce new colors without updating this file first.
```

The values come from data we already have:
- `colors.brand` ← `business-data.json` `site.VERTICAL_ACCENT_COLOR`
- `colors.brand-soft` ← computed via `color-mix(in srgb, brand 15%, white)` (or pre-resolved)
- typography + spacing ← `templates/multi-page/_base.css` already-defined tokens
- Component tokens ← lifted from `_base.css` rules

### Piece 2: NEW script `scripts/write-design-md.py`

```
Usage:
  python3 scripts/write-design-md.py <slug>
  python3 scripts/write-design-md.py <slug> --lint
```

What it does:
1. Reads `sites/<slug>/business-data.json` (for vertical, name, brand color)
2. Reads `sites/<slug>/gbp_snapshot.json` (for business-name + 24/7 flag, etc.)
3. Reads vertical-specific defaults from a new file `templates/design-md/vertical-defaults.json` (electrical → blue, plumbing → green, HVAC → navy, etc., aligned with `DESIGN-HEURISTICS.md` palette section)
4. Renders `sites/<slug>/design.md`
5. If `--lint` flag: runs `npx @google/design.md lint <path>` (only if Node is installed; warns if not)

### Piece 3: Hook into `fill-scaffold.py`

When `fill-scaffold.py` runs, it would call `write-design-md.py` first
(before HTML token-fill) so `_base.css` can read tokens directly from
`design.md` instead of from `business-data.json` directly.

This is the only flow change — and even it's optional. We could keep
`_base.css` reading from `business-data.json` and treat `design.md` as
purely informational/AI-handoff.

## What I'm NOT proposing

- **No SKILL.md changes** required. DESIGN.md is purely additive.
- **No HANDOFF-CONTRACT.md changes** required. Bruce / Mini scope unaffected.
- **No business-data.json changes** required. design.md is generated FROM business-data.json, not in addition to it.
- **No template changes** required. `_base.css` keeps working as-is.
- **No build-flow changes** required (unless you want Piece 3, which is a 30-minute add).
- **NO Stitch MCP server installation** in this proposal. That's a Phase 2 question after the spec is in use. Right now I'm just proposing the file format adoption.

## Cost analysis

- **Build cost per site:** ~30 seconds for the new script to run. Zero API cost (no external calls).
- **Storage cost:** ~3 KB per site for `design.md`.
- **Maintenance cost:** zero unless the spec changes (it's at alpha — possible). I'd pin the version field in our generator.
- **Reversal cost:** trivial. If you decide DESIGN.md isn't useful in 6 months, delete the script + the per-site files. Nothing else touches it.

## Open questions

1. **Vertical-specific defaults file** — do you want me to author `templates/design-md/vertical-defaults.json` upfront for the 16 verticals in your "Best verticals" list (HVAC, plumbing, etc.), or generate them on-demand per site? Upfront is more work now, more consistent later.

2. **The Stitch MCP server, separately** — installing it gives Claude Code (and Bruce/Mini if they install it too) tools for `list_projects`, `list_screens`, `get_screen`, `get_project`. That'd let us round-trip — you sketch a design in Stitch, we pull it into our build. **Not in this proposal.** Worth its own discussion later if Phase 2 wants visual iteration.

3. **The CLI dependency** — `@google/design.md` is npm-distributed. If you don't want Node added as a runtime dep for the build pipeline, the lint step is optional and can be skipped.

## What I need from you

- **ACK to proceed** — I'll write the script + author vertical-defaults for the top 5-6 verticals + add a `design.md` to the `plugged-electricians-atl` pilot to validate.
- Or **counter-propose** — schema tweaks, scope adjustments, "wait until X."

No timeline pressure. This sits behind your real Mini queue review and the Firehose credits decision.

— R1VS
