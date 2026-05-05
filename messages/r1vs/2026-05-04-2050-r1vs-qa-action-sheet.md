# QA action sheet — 51 prospects, all deployed, awaiting Jesse review

**Generated:** 2026-05-04 (post-dinner sitrep)  
**Source:** R1VS spot-check of `<slug>.pages.dev` for all 51 prospects in `rebuild-queue.json`. *51/51 returned HTTP 200.* Every site is live.  
**Use:** Open this on mobile. Each row gives you the live URL + claim code + 1-line context. Batch-review by vertical for efficiency.  
**Per-site review checklist:** (1) hero loads, (2) reviews look real and named, (3) claim bar shows correct claim code, (4) contact form has upload, (5) mobile responsive on a 30-second scroll. Mark `qa_approved` if green; file feedback if not.

---

## TL;DR — by stage

- **ready_for_review**: 35
- **outreach_sent**: 11
- **outreach_staged**: 4
- **qa_approved**: 1

**The path to outreach for the 32 `ready_for_review` is short**: Jesse opens URL on mobile → 30-second look → `qa_approved` or feedback. ~16 minutes total at 30s each.

---

## Decision-required FIRST (3 prospects with R1VS DQ flags)

These need a Jesse yes/no before they advance in either direction:

| Slug | Trade | URL | Why flagged |
|---|---|---|---|
| `posh-paws-atlanta` | Pet Grooming | https://posh-paws-atlanta.pages.dev/ | Pet grooming may be off-vertical for trade-site builder (intake commit `c051f29`) |
| `sandy-springs-plumbing-share` | Plumbing | (intake-branch only — share variant) | Data quality issue (intake commit `887f449`) — recommend DQ or correct rebuild-queue |
| `cleveland-electric` | Electrician | (not in rebuild-queue list — check intake `4f42b19`) | Market mismatch flag |

Note: `cleveland-electric` and `sandy-springs-plumbing-share` are NOT in the rebuild-queue's 51 prospects — flagged in intake-branch commits, may have been DQ'd already. `posh-paws-atlanta` IS in the queue at `ready_for_review`.

---

## Batch-review pass by vertical

### Plumbing (7)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_sent | Sandy Springs Plumbing | https://sandy-springs-plumbing.pages.dev/ | `SSPL4817` | Jack |  |
| ready_for_review | Bravo Plumbing Solutions | https://bravo-plumbing-solutions.pages.dev/ | `BPST1027` | Forrell Hillery | Ellenwood |
| ready_for_review | PlumbingPro North Atlanta | https://plumbingpro-north-atlanta.pages.dev/ | `PNAR1671` | — | Chamblee |
| ready_for_review | Rooter Pro Plumbing & Drain | https://rooter-pro-plumbing-drain.pages.dev/ | `RPPD9298` | Megan Dammann | Marietta |
| ready_for_review | Sandy Springs Plumber, Sewer & S | https://sandy-springs-plumber-sewer-septic.pages.dev/ | `SSPS4071` | — | Sandy Springs |
| ready_for_review | Sandy Springs Plumbing Share | https://sandy-springs-plumbing-share.pages.dev/ | `SSPS4553` | — | Atlanta |
| ready_for_review | Tuxedo Mechanical & Plumbing | https://tuxedo-mechanical-plumbing.pages.dev/ | `TXDO3912` | Wayne M. Huckabee | Chamblee |

### mobile_tire (4)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_sent | InTire Mobile Tire Shop | https://intire-mobile-tire-shop.pages.dev/ | `INTR-AJ01` | Adrian Johnson | Decatur |
| outreach_sent | Tire & Ride Mobile | https://tire-and-ride-mobile.pages.dev/ | `TNRD-ATL1` | — | Atlanta |
| ready_for_review | 24 hrs Mobile Tire Services | https://24-hrs-mobile-tire-services.pages.dev/ | `HMTS3276` | — | Atlanta |
| ready_for_review | Zion Mobile Tire Services 247 | https://zion-mobile-tire-services.pages.dev/ | `ZION-5524` | — | Austell |

### Gutter Cleaning (3)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_sent | Professional Gutter Cleaning | https://professional-gutter-cleaning.pages.dev/ | `PXPX3229` | Esau Gonzalez | Atlanta |
| ready_for_review | Pro Gutter Cleaning | https://pro-gutter-cleaning.pages.dev/ | `PROG4046` | Matt (last name unconf | Carrollton |
| ready_for_review | THE SMART COMPANY LLC | https://the-smart-company-llc.pages.dev/ | `SMRT5293` | Jose Figueroa + Yenire | Buford |

### Appliance Repair (2)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_sent | Atlanta Expert Appliance | https://atlanta-expert-appliance.pages.dev/ | `DQTI9023` | Steve Baker | Decatur |
| qa_approved | The Appliance Gals | https://the-appliance-gals.pages.dev/ | `RUVO7205` | Sharonda/Eunice | Atlanta |

### Auto Repair (2)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Atl Mobile Mechanics | https://atl-mobile-mechanics.pages.dev/ | `SVYG3351` | Joseph | Douglasville |
| ready_for_review | ATL Mobile Mechanics | https://douglasville-mobile-mechanics.pages.dev/ | `IPJN5652` | Joseph | Douglasville |

### Drywall (2)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Atlanta Drywall | https://atlanta-drywall-1.pages.dev/ | `FHWL8920` | Wilber Tejada Garcia | Norcross |
| ready_for_review | Done Right Drywall | https://done-right-drywall.pages.dev/ | `MTJL8654` | David Neel | Atlanta |

### Electrician (2)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Harrison & Sons Electrical Servi | https://harrison-sons-electrical.pages.dev/ | `HARR2423` | — | Atlanta |
| ready_for_review | Plugged Electricians ATL LLC | https://plugged-electricians-atl.pages.dev/ | `PLUG3677` | Sherea Jones | Atlanta |

### HVAC (2)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_staged | Bob's Heating & Air | https://bobs-hvac.pages.dev/ | `BOBS3341` | Bob | Roswell |
| ready_for_review | HVAC Guyz & Plumbing Inc | https://hvac-guyz-plumbing-inc.pages.dev/ | `HGPI3337` | Rohan Sloley | Atlanta |

### Handyman (2)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_staged | Handy Dandy Atlanta | https://handy-dandy-atlanta.pages.dev/ | `HBSR0716` | Ruslan | Barnesville |
| ready_for_review | Atlanta Pro Repairs | https://atlanta-pro-repairs.pages.dev/ | `UTJH5186` | W. Davis | Atlanta |

### Pool Service (2)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_sent | Perez Pools LLC | https://perez-pools-llc.pages.dev/ | `TYGG3598` | Chris Perez | Atlanta |
| outreach_staged | Azer Pool | https://azer-pool.pages.dev/ | `AZER9901` | Mr. Azer | Buford |

### Pressure Washing (2)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Golden Choice Pro Wash | https://golden-choice-prowash.pages.dev/ | `BUUH5104` | Sheridan | Sandy Springs |
| ready_for_review | Moonstone Pressure Washing | https://moonstone-pressure-washing.pages.dev/ | `MOON4729` | Alonzo Cabrera Sr. | Lithia Springs |

### concrete (2)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_sent | Affordable Concrete & Repair | https://affordable-concrete-repair.pages.dev/ | `CONCRETE352` | Maurice Dykes | Hawthorne |
| ready_for_review | Doctor Concrete ATL LLC | https://doctor-concrete-atl.pages.dev/ | `DCAL8179` | Hugo Tamayo | Marietta |

### mobile_mechanic (2)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_sent | Tech On The Way | https://tech-on-the-way.pages.dev/ | `KBHA2199` | Celena | Mableton |
| ready_for_review | Thermys Mobile Tire and Brakes L | https://thermys-mobile-tire-and-brakes.pages.dev/ | `THMY-QW01` | Quartisha Williams | Atlanta |

### Car Washing & Detailing (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Trushyne Mobile Detailing | https://trushyne-mobile-detailing.pages.dev/ | `TMDH6713` | Demetric R. Johnson | Atlanta |

### Carpet Cleaning (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_staged | Dream Steam | https://dream-steam.pages.dev/ | `ILIM2208` | Reuben | Atlanta |

### Collision Repair (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Forest Park Collision | https://forest-park-collision.pages.dev/ | `FPCJ7255` | — | Atlanta |

### Fencing (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Thompson's Fence | https://thompsons-fence.pages.dev/ | `YYEJ4549` | Thompson | Atlanta |

### General Services (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_sent | City Boys R Us | https://cityboys.pages.dev/ | `CITY6612` | Curtis | Atlanta |

### Home Repair (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Membreno's Pro Home Repair | https://membrenos-pro-home-repair.pages.dev/ | `MEMB2247` | Hector Membreno | Lawrenceville |

### Home Services (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_sent | Tucker's Home Services | https://tuckers-home-services.pages.dev/ | `SHBJ5366` | Shaun Tucker | Woodstock |

### Landscaping (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Morales Landscape & Construction | https://morales-landscape-construction.pages.dev/ | `SPLN0347` | Jose Morales | Norcross |

### Locksmith (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| outreach_sent | Locksmith Atlanta Pro | https://locksmith-atlanta-pro.pages.dev/ | `EEVK3309` | Jeff | Atlanta |

### Mobile Car Wash & Detailing (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Chrissy’s Mobile Detailing | https://chrissy-s-mobile-detailing.pages.dev/ | `CMDW5642` | Chrissy | Atlanta |

### Mobile Services (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Roberts Mobile Services | https://roberts-mobile-services.pages.dev/ | `ROBE1849` | Robert Stinton | Atlanta |

### Pet Grooming (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Posh Paws Atlanta | https://posh-paws-atlanta.pages.dev/ | `POSH3847` | — |  |

### Remodeler (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | TGP Home Services | https://tgp-home-services.pages.dev/ | `TGPH8214` | — | Chamblee |

### Roswell Pro Plumber (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Roswell PRO plumber | https://roswell-pro-plumber.pages.dev/ | `RSWPL847` | — | Atlanta |

### TV Mounting (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Premier TV Mounting | https://premier-tv-mounting-atl.pages.dev/ | `JSMA4043` | Marcus | Atlanta |

### Tire Shop (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Piedmont Tires (New/Used) | https://piedmont-tires.pages.dev/ | `PIED-7488` | — | Chamblee |

### Waxing and Ceramic Coating (1)

| Stage | Business | Live URL | Claim code | Owner | City |
|---|---|---|---|---|---|
| ready_for_review | Sumptuous Mobile Detailing | https://sumptuous-mobile-detailing.pages.dev/ | `SMDT6777` | Darren | Suwanee |

---

## What to look for during 30-second mobile review

Per-site quick checklist:

1. **Hero image loads** (no broken `data-resolved="false"` placeholder text bleeding through)
2. **Reviews are real and named** (no `Anonymous Customer` or invented names; the marquee or static quotes show actual reviewer names from Yelp/Google/Nextdoor)
3. **Claim bar shows the correct claim code** — bottom of viewport, format `Claim this site for $49 →` followed by `[Claim it now]` button linking to `/checkout?code=<CODE>`. Cross-reference against the table above to confirm code matches.
4. **Contact form is present** — homepage or contact page, with a phone number prominently displayed and (for many sites) a file upload field
5. **Mobile responsive** — scroll the whole page, look for layout breaks, overlapping text, hero photo cropped weirdly, marquee that scrolls fine
6. **No obvious typos, placeholder text, or `{{merge_token}}` strings**

If green on all 6 → `qa_approved`. If something's off → file specific feedback in #claude-sync naming the slug + the issue.

---

## Honest gaps

- This sheet doesn't tell you *whether outreach has gotten any responses* on the 14 `outreach_sent` prospects — that's CRM-side ground truth Codex would surface.
- This sheet doesn't tell you *whether the outreach hold is currently active* per CLAUDE.md's outreach-hold-language gate.
- Forest Park Collision is at `ready_for_review` per the queue but is the deployed pilot — likely already at `qa_approved` if you've reviewed it before. Verify against current CRM state.
- `plugged-electricians-atl` shows `outreach_sent` (tier 1) AND `ready_for_review` (rebuild-queue's `current_stage`). Stage drift — Codex should reconcile.
- `atl-mobile-mechanics` and `douglasville-mobile-mechanics` show identical owners (Joseph) and same CRM `ready_for_review` stage in the rebuild-queue. Mini's earlier #claude-sync message indicated `douglasville-mobile-mechanics` was dead-staged as a duplicate. Stale data; Codex should drop it from the queue.
