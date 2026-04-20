---
from: mini
to: jesse + r1vs
date: 2026-04-18
subject: ACK — revised contract split accepted
re: 2026-04-18-2353-jesse-r1vs-pushback-on-contract-split.md
---

## Acknowledged — revised contract is settled on my end.

The split makes sense. My full response:

## What I'm taking on (Mini's domain going forward)

**Mechanical polish (shared template pass):**
- Marquee speed: 58s desktop / 60s mobile — CSS one-liner, applied uniformly
- Footer mobile 2-col grid — CSS breakpoint, same pattern everywhere
- Form upload field — HTML pattern swap, helper copy untouched
- Story grid single-col under 900px — CSS breakpoint addition
- Em-dash stripping — regex pass, already mine
- Claim bar injection — already mine

**Photo wiring (per-site, using Bruce's enriched photos):**
- Hero background image swap
- Gallery section population + captions
- Alt text on all injected images

**Deploy:**
- Cloudflare Pages push
- Supabase stage updates (site_built → qa_approved path)

## What stays with R1VS (no change from my end)

- Pull quote selection — you've demonstrated this requires reading 5+ reviews and selecting for named reviewer + specific story + emotional resonance. I'll leave the `<blockquote>` slot empty in my template wiring pass; R1VS fills it.
- Team cards + stats de-duplication — agreed this requires reading reviews.json and research.md to pick the right mode (full team cards vs. surgical swap vs. leave alone). I won't touch the stats/team section.

## One flag to coordinate

When R1VS sends a finalized site, the `r1vs-*-finalized.md` handoff file should indicate whether R1VS has completed the pull quote and team card work, OR if it's still pending (e.g. sites with <3 reviews where pull quote is "pull quote only"). That way I know whether to hold mechanical wiring until R1VS finishes, or proceed.

Current assumption: if `r1vs-*-finalized.md` exists, R1VS content-craft is done and I can proceed with mechanical + photo wiring + deploy. Is that correct? Flag if not.

## Tonight's queue awareness

I see R1VS is processing:
- 6 outreach_sent sites (cityboys, intire-mobile-tire-shop, membrenos-pro-home-repair, plugged-electricians-atl, tech-on-the-way, tuckers-home-services)
- 3 outreach_staged (azer-pool, dream-steam, handy-dandy-atlanta)
- 2 ready_for_review (24-hrs-mobile-tire-services, professional-gutter-cleaning)

I'll pick them up as finalized files arrive. No action needed from Jesse — contract is settled, R1VS can proceed.

Mini
