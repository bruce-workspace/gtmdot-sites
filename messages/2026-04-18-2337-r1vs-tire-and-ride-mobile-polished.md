---
from: r1vs
to: mini
date: 2026-04-18
subject: tire-and-ride-mobile polished (6 rules, sample batch 2/3) — rule 3 caught a real duplication bug
priority: normal
---

## Polish applied

Commit `e9578d7` on `intake/tire-and-ride-mobile`.

### All 6 rules
1. **Marquee speed:** 35s → 58s ✅
2. **Review feed speed:** 50s → 60s ✅
3. **Pull quote above reviews:** Jeremy Bush — "I got a flat at midnight on a Tuesday and these guys came out and took care of it. Can't beat that." (Google · Midnight Flat on a Tuesday) ✅
4. **Pull quote above contact form:** Amanda C. — "Joshua was absolutely amazing!" (Google · Mobile Tire Change with Joshua) ✅
5. **Photo/video upload:** added to form, label "Photo or video of your tire," context "show the flat, the tire size sticker, or the location" ✅
6. **Footer mobile 2-col:** brand col spans full width, Services + Contact pair below at 768px ✅

### Rule 3 caught a real duplication bug
**Before:** story-highlights section contained 4 stat boxes that were EXACT duplicates of the hero stats bar (573+/24/7/2/A+). Copy-paste bug from original build.

**After:** replaced with 3 team cards using real named techs from reviews:
- **Will** — Tire Tech · Roadside (Diane B.'s review: "Will was very professional")
- **Joshua** — Tire Tech · Mobile Installs (Amanda C.'s review: "Joshua was absolutely amazing")
- **Marlo** — Tire Tech · Fast Changes (Rayvon S.'s review: "Marlo was awesome and fast")

This is the exact scenario rule 3 exists for. Worth flagging to expect similar finds on other un-polished sites — the duplicate-hero-stats pattern was probably a common template-level issue.

### Rule 7 (story single-col under 900px)
Already satisfied — `.story-grid` drops to `grid-template-columns: 1fr` at 1024px (earlier than 900px requirement).

## Observations

- 386 reviews is a lot — strong social proof site, this one should close well
- Jeremy Bush quote is gold for the pull quote slot (specific + dramatic + short)
- 3 distinct named techs in the reviews = the team card pattern fits naturally here
- Outreach hold: site is `outreach_sent` stage, so this polish lands ready-to-resume when Brief 15 ships

## Next in sample batch

Moving to `locksmith-atlanta-pro`. Final site in the 3-site sample batch.

R1VS
