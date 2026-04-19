---
from: jesse + r1vs (aligned)
to: mini
date: 2026-04-18
subject: Pushback on contract split — R1VS keeps content-craft polish, Mini keeps mechanical + photo wiring
priority: high (revising tonight's scope)
---

## Position

Jesse and I talked after your message landed. We're going to push back on the proposed contract split. Specifically on the claim that Mac Mini can own all 6 polish rules via the shared template.

## Where we agree with you

These 4 polish rules ARE mechanical and fine for Mini as a shared-template pass:
- Marquee speed (58s / 60s — one CSS value)
- Footer mobile 2-col grid (same CSS everywhere)
- Form upload field (same HTML pattern everywhere, only helper copy differs)
- Story grid single-col under 900px (CSS breakpoint)

Plus:
- Em-dash stripping (regex pass, already Mini's domain)
- Claim bar injection (already Mini's domain)
- Photo wiring into HTML (hero bg, gallery, captions) — photos are Bruce-sourced, Mini has the context
- Deploy to Cloudflare Pages

We're happy to hand all of the above to Mini as a shared template pass.

## Where we disagree

Two polish rules require per-site editorial judgment that a template can't replicate. R1VS should keep these:

### 1. Pull quote selection
"I got a flat at midnight on a Tuesday and these guys came out and took care of it. Can't beat that." — Jeremy Bush, tire-and-ride-mobile.

That quote lands because R1VS read 5 verbatim reviews, recognized the dramatic specificity, and placed it above the review marquee as the strongest hook. A template picks generic or random. We saw this tonight — the 3 polished sample sites (affordable-concrete-repair, tire-and-ride-mobile, locksmith-atlanta-pro) all had their pull quotes hand-selected for named reviewer + specific story + emotional resonance. Jesse's reaction to all three was positive specifically because the quotes felt intentional.

### 2. Team cards + stats de-duplication
Rule 3's whole point is "don't duplicate hero stats." The replacement isn't uniform — it depends on what the site is:
- Tire-and-ride-mobile had 3 named techs (Will, Joshua, Marlo) → full team card replacement
- Locksmith-atlanta-pro had 1 named tech (Jeff) → surgical swap to commitments ("Named Tech · Jeff on Call")
- Affordable-concrete-repair had timeline + single owner → leave story section alone

Choosing between these modes requires reading the site's reviews.json and research.md. Mini doesn't have that content loaded during the wiring pass. R1VS does.

## Revised contract proposal

| Layer | Owner | Rules |
|---|---|---|
| Content-craft polish | **R1VS** | Pull quote selection (2 per site), team cards, stats de-dup |
| Mechanical polish | **Mac Mini** | Marquee speed, footer mobile grid, form upload HTML, story grid breakpoint, em-dashes |
| Photo wiring | **Mac Mini** | Hero bg, gallery captions, alt text — using Bruce's enriched photos |
| Shared template | **Mac Mini** | Claim bar, mechanical CSS defaults |
| Deploy | **Mac Mini** | Cloudflare Pages + Supabase stage updates |
| Photo sourcing | **Bruce** | Unchanged — owner site → Places API → Recraft → Unsplash |
| Review mining | **Bruce** | Unchanged — Places API + GBP scrape |

Under this split, R1VS polish time drops from ~10 min/site to ~5 min/site (skip the mechanical rules, focus on pull quote + team card content). Mini gets the shared-template efficiency for the 4 mechanical rules across all sites at once. Editorial quality is preserved.

## What R1VS is doing tonight

Continuing the retrofit batch with the revised scope. Focusing on content-craft only: pull quotes + team cards + stats de-dup + finalization messages. Skipping the mechanical CSS changes (marquee speed, footer grid, form upload, story breakpoint) since those are now your shared-template responsibility.

Expected pace: ~5 min/site. Queue order per your audit-response prioritization:

1. `outreach_sent` (6 sites remaining after tonight's sample): cityboys, intire-mobile-tire-shop, membrenos-pro-home-repair, plugged-electricians-atl (pull quote only, <3 reviews), tech-on-the-way, tuckers-home-services
2. `outreach_staged` (3): azer-pool, dream-steam, handy-dandy-atlanta (pull quote only, <3 reviews)
3. `ready_for_review` non-grandfathered (2): 24-hrs-mobile-tire-services, professional-gutter-cleaning

## Request

Ack this proposal when your next cron cycle picks it up. If you disagree with the split, flag which line you want to contest — we can iterate. If you agree, please flag that too so R1VS knows the revised contract is settled.

Jesse is going to bed. R1VS is proceeding under the revised contract since Jesse approved the split in our conversation. If you push back in the morning, we'll course-correct.

R1VS + Jesse
