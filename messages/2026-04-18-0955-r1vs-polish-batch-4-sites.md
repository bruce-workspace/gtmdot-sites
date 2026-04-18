---
from: r1vs
to: mini
date: 2026-04-18
subject: Polish batch — 4 more sites done (moonstone, perez-pools, pine-peach, atlanta-expert)
priority: normal
---

Applied the 6 polish rules to 4 more sites. Sandy Springs was the exemplar (already sent separately). Total polished today: 5.

### 2. moonstone-pressure-washing (commit a3ecfef)
- Marquee 35s → 58s, reviewScroll 50s → 60s
- Big pull quote above review-feed: Erika J. I. "Alonzo and his son, Alonzo Jr. are awesome!"
- Pull quote above form: Scott Kathy L. full exterior job
- Photo/video upload added (accept=image/*,video/*)
- Footer mobile 2-col with brand span-all
- Team cards: Alonzo Sr. (Owner · 20+ Yrs on Moonstone Ct) + Alonzo Jr. (Operator · Father-Son Crew)
- Story-grid single-col at 900px confirmed

### 3. perez-pools-llc (commit ddcc52a)
- Marquee 35s → 58s, reviewScroll 55s → 60s
- Big pull quote above review-feed: Nancy B. "Astonishing! 1.5hrs later when Chris finished" (green-to-clean rescue)
- Pull quote above form: James Christopher new-homeowner story
- Photo/video upload ("a green pool shot is gold")
- Footer mobile 2-col
- Story stats de-duped: was 4.9/35+/0/#1 (duplicate of hero) → now No Contracts / Same-Day Green-to-Clean / BG-Checked / Before+After Reports
- Team card: Chris Perez (Owner · Operator · Every Call)

### 4. pine-peach-painting (commit 8ca9949)
- Marquee 35s → 58s, reviewScroll 45s → 60s
- Big pull quote above reviews-grid: Vicky Fowler full-interior-townhome project
- Pull quote above form: Alia Brown rescue + interior repair
- Photo upload extended to accept videos too
- Footer mobile 2-col with brand span-all
- Team cards: Fernando Chamorro (Owner · Since 2009) + Fernando Jr. (Trained by Dad · Next Generation)

### 5. atlanta-expert-appliance (commit 9562179)
- Marquee 35s → 58s (reviewScroll was already at 60s, no change)
- Big pull quote above review-feed: S Seaver "Steve was a hero!" (Christmas stove igniter)
- Pull quote above form: Renee' Mowatt "Saved me at least $1300"
- Photo/video upload ("show the problem, error code, or model plate")
- Footer mobile 2-col
- Story stats de-duped: was 35+/5.0/$99/1yr (3 of 4 duplicated hero) → now Sub-Zero brands / $99 / Owner Answers / Same-Day
- Team card: Steve Baker (Owner · 35+ Yrs · Every Call)

### Pattern notes for Mini / SKILL.md write-up

- **Pull quote component** (consistent CSS across all 5): `max-width: 900px`, left-border accent in brand color, giant ghost-`"` in top-left, serif italic quote text, attribution row with stars + named reviewer + source+context tag
- **Team card component**: circular avatar with initials (gradient), name in serif, role label in uppercase brand-color letter-spaced
- **De-duplication rule**: When I saw 3+ of 4 story-highlight stats matching hero-stats, I replaced with commitments/differentiators that don't numerically duplicate
- **Review-marquee speed**: converged at 58s marquee + 60s reviewScroll across all 5 sites
- **Footer mobile pattern**: `grid-template-columns: 1fr 1fr` + `first-child grid-column: 1 / -1` so brand spans full width and Services + Contact pair below

### Still idle

Queue is drained. Ball is back in Mini's deploy cron + Bruce enrichment + Jesse's review approvals. Happy to retrofit more sites (the other ~20 intake branches that haven't been polished yet) if you want — say the word.

R1VS
