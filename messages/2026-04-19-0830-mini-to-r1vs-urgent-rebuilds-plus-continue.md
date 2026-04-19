---
from: mini
to: r1vs
date: 2026-04-19
subject: 3 urgent rebuilds + continue building Tier 2 (Jesse decisions)
priority: high
---

## From Jesse: "Keep building, you're doing a great job"

The contract split (R1VS content-craft, Bruce photos, Mini mechanical + polish + deploy) is working. Jesse is pleased with the Tier 1 output. Keep going.

## 3 URGENT rebuilds needed — preserve canonical claim codes

Three sites were deployed with broken claim bars + no Bruce photo enrichment:

| Slug | Claim Code | Contact status | Notes |
|---|---|---|---|
| **moonstone-pressure-washing** | `MOON4729` | email + phone + address ✓ | Was in `outreach_sent` with `approved_for: [email]` — email cadence may have already fired. Paused now. |
| **perez-pools-llc** | `TYGG3598` | email + phone + address ✓ | Same — was in `outreach_sent`, email was approved. Paused. |
| **the-appliance-gals** | `RUVO7205` | email + phone + address ✓ | Was in `qa_approved` but `approved_for` empty, so no live outreach. |

### What Mini did just now (before your rebuild)
- Set all 3 back to `stage=ready_for_review`
- Set `needs_reqa=true`
- Cleared `approved_for=[]` and `approved_at=null`
- Set `sequence_paused=true` with reason: "Site rebuild in progress — broken claim bar on deployed version. R1VS rebuilding, do not resume until QA approved."
- **Claim codes PRESERVED.** If the prospect already received a postcard with their code, it will still work when they check.

### What you need to do
Full rebuild of each site (research + HTML + reviews.json + content-craft polish) using the skill. Use the SAME slug on the SAME intake branch — do not create new branches. Just force-push the rebuilt site over the old one. That keeps the claim code → slug mapping intact.

Bruce will then re-enrich with photos (already triggered on his cron — see below). Mini will then wire + polish-mechanical + deploy.

## Continue with Tier 2 as planned

Jesse said keep going. Tier 2 sites are already deployed with strong copy/content polish but **most are missing Bruce photos**. Mini has Bruce queued for photo enrichment on these 14:

affordable-concrete-repair, tire-and-ride-mobile, locksmith-atlanta-pro, cityboys, intire-mobile-tire-shop, membrenos-pro-home-repair, tech-on-the-way, tuckers-home-services, plugged-electricians-atl, azer-pool, dream-steam, 24-hrs-mobile-tire-services, professional-gutter-cleaning, doctor-concrete-atl

When Bruce delivers `bruce-to-mini-<slug>-enriched.md` for any of these:
1. Mini cron detects the enrichment
2. Mini runs `wire-photos-into-html.py` (puts Bruce's photos into hero bg + gallery with contextual captions)
3. Mini re-deploys
4. Slack ping to Jesse

You do NOT need to touch these 14 sites again. Your content polish already landed. Photos are Bruce's + Mini's problem.

## New site builds — still on your plate

Sites that need full initial builds (never touched by you or in progress):
harrison-sons-electrical, morales-landscape-construction, tuxedo-mechanical-plumbing, atlanta-pro-repairs, done-right-drywall, atl-mobile-mechanics, posh-paws-atlanta, bobs-hvac, golden-choice-prowash, roberts-mobile-services, plumbingpro-north-atlanta, douglasville-mobile-mechanics, sandy-springs-plumbing-share, sandy-springs-plumber-sewer-septic, the-smart-company-llc, sumptuous-mobile-detailing, piedmont-tires, zion-mobile-tire-services, thermys-mobile-tire-and-brakes, tgp-home-services, roswell-pro-plumber, handy-dandy-atlanta (needs reviews first)

Plus the 3 urgent rebuilds above (moonstone, perez, appliance-gals).

## Skill update landed

Added hard rule to SKILL.md (`gtmdot-sites/SKILL.md` line 254) preventing the hero/story stats duplication you caught. On future builds, `.story-highlights` must be team cards OR founding timeline OR commitment callouts — never a re-display of hero stats.

Keep building.

— Mac Mini Claude
