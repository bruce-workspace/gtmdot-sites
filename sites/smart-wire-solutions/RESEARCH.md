# RESEARCH.md — SmartWire Solutions LLC

**Phase:** 1 — Research
**Slug:** `smart-wire-solutions`
**Date:** 2026-04-28
**Authored by:** R1VS (MacBook Claude Code)
**Status:** Phase 1 complete; HOLDING for Phase 2 approval per Paperclip-pilot gate

---

## 1. Identity & contact (canonical)

| Field | Value | Source |
|---|---|---|
| Legal name | **SmartWire Solutions LLC** | BBB profile |
| Common / display name | **SmartWire Solutions** | Google KP, Facebook, Instagram, Yelp |
| Predecessor name | Wiring Solutions of Georgia (2004) | Alignable profile |
| Vertical | Electrical contractor (residential-focused) | BBB, Google KP, Alignable, Instagram bio |
| Address | **730 Peachtree St NE, Ste 570, Atlanta, GA 30308-1244** | BBB (primary), Yelp listing snippet, Google KP cross-ref |
| Service-area-business posture | YES — GBP cid `0x0:0x...` ftid is `0x0` (no verified storefront geocode) | Phase 0 v2 manual KP scrape |
| Primary phone | **(404) 382-9847** | BBB (primary), Yelp, Facebook, business's own copy, Jesse's handoff |
| Secondary phone | (404) 635-6301 | Google KP only — likely owner direct line |
| Hours | Open 24 hours | Google KP |
| Website | https://smartwire365.com — **PARKED** (JS-redirects to `/lander`, registrar parking page) | curl probe 2026-04-28 |

**Phone canonical recommendation:** Use **(404) 382-9847** for the site's primary contact CTA, "Call Us" button, JSON-LD `telephone` field, and footer. The BBB-registered, Yelp-listed, Facebook-listed, owner-promoted number is the canonical one. Google KP's (404) 635-6301 is likely a direct cell for Terry Henry; do not feature it on the public site.

## 2. Business entity history

| Event | Date / Year | Source |
|---|---|---|
| Predecessor "Wiring Solutions of Georgia" founded | 2004 | Alignable: *"Established in 2004 under the name Wiring Solutions of Georgia we have been faithfully serving Metro Atlanta for over 15 years now."* |
| SmartWire Solutions LLC (current entity) started | **3/11/2020** | BBB: *"Business Started: 3/11/2020"* |
| BBB file opened | 5/15/2020 | BBB |
| Years operating (lineage / brand) | 22 years (since 2004) | KP description: *"providing quality electrical services to the Metro Area for over 20yrs"* |
| Years operating (legal entity) | 6 years (since 2020) | BBB: *"Years in Business: 6"* |

**Tenure-claim guidance for Phase 2:** Lead with the **lineage tenure** ("Atlanta electricians since 2004" / "20+ years serving Metro Atlanta"). The 2020 LLC date is a corporate-restructure milestone, not a service-history start date. Do not say "since 2020" — that undersells two decades of work.

## 3. Officers / leadership

| Person | Role | Background | Source |
|---|---|---|---|
| **Terry Henry** | President / Owner-operator / Master Electrician | 30+ years electrical experience; trained in U.S. Air Force; former instructor for Independent Electrical Contractors Association (IEC) Atlanta; LinkedIn lists 170+ followers | BBB, Alignable, LinkedIn (terry-henry-b761bb25), Google KP description |
| **Maria Henry** | Vice President | Listed as VP on BBB; secondary contact per Jesse's handoff | BBB |

**Notable past project history (Terry Henry's career — not necessarily SmartWire LLC):**
- Georgia Tech
- VA Hospital Atlanta
- Dobbins Air Force Base
- Coca-Cola Distribution Centers (Metro Atlanta)

⚠️ **Phase 2 caution:** These projects skew commercial/institutional, but SmartWire's current marketing is **residential-first**. Don't lead the site with these; use them as a "Master Electrician Terry has worked on projects across Atlanta" credibility line, not as a "we serve commercial accounts" pitch. The hero / services / about copy should target homeowners.

## 4. Trust signals

| Surface | Signal | Notes |
|---|---|---|
| Google Business Profile | 5.0 ★ across **17 reviews**; KP description present; Open 24 hours | Knowledge Panel rendered; verbatim review text NOT yet captured (Bruce §11.11 deliverable) |
| Facebook page | 480+ followers; **5/5 from 6 votes** (per KP cross-ref); page name "SmartWire Solutions Home Electrical Services" | facebook.com/SmartWire365 |
| Instagram | 230+ followers; bio: "South Fulton Electrician" | instagram.com/smartwire365 |
| YouTube | Channel `@smartwiresolutions6624`; content suggests outdoor-lighting topics per Instagram caption snippet | Channel exists; content depth NOT verified |
| LinkedIn (owner) | 170+ followers; Terry Henry, "Owner - SmartWire Solutions LLC" | linkedin.com/in/terry-henry-b761bb25 |
| Yelp | Listed as "SMARTWIRE SOLUTIONS - Updated April 2026"; address + phone confirmed via search snippet; full reviews NOT extractable (DataDome captcha blocks both WebFetch and headless browser) | yelp.com/biz/smartwire-solutions-atlanta |
| Alignable | 2 verbatim recommendations | alignable.com/midtown-atlanta-atlanta-ga/smartwire-solutions-llc |
| BBB | Profile present; **NOT BBB Accredited**; **Not Rated** ("BBB does not have sufficient information"); no complaints visible | bbb.org/.../smartwire-solutions-llc-0443-28141526 |

**License posture:** No license number visible on the BBB profile. BBB references *"Secretary of State - Professional Licensing Boards, 237 Coliseum Dr, Macon GA 31217, (478) 207-2440, www.sos.ga.gov"* as the verifying authority. **Verification of an active GA electrical license is not done in Phase 1; flagging as a Phase 2 / Bruce sanity check.** Terry Henry self-identifies as "Master Electrician" across all surfaces, which under GA law requires a class IV license issued by the Construction Industry Licensing Board.

## 5. Service area & posture

- **Registered address:** 730 Peachtree St NE Ste 570, Atlanta GA 30308 (Midtown — dense commercial corridor)
- **Marketing reach (KP description):** "Metro Area"
- **Self-described focus (Instagram bio):** "South Fulton Electrician"
- **Self-described customer base (Alignable):** "Atlanta Homeowners"
- **Operating posture:** Service-area-business GBP without verified storefront geocode (cid ftid = `0x0`). The 730 Peachtree address is the registered business address per BBB but may be a small office, virtual mail-drop, or coworking suite — the actual work happens at customers' homes.

**Service area for Phase 2 site copy:**
> "Serving Atlanta homeowners — Midtown, Buckhead, Inman Park, Virginia-Highland, Decatur, Sandy Springs, Brookhaven, and South Fulton (College Park, East Point, Fairburn, Union City)."

⚠️ The above neighborhood list is **a reasonable Atlanta-residential-electrician spread synthesized from the data** (Midtown + South Fulton are explicit; the rest are intown-Atlanta neighborhoods within reasonable radius). Bruce's §11.11 collection should confirm by pulling SmartWire's own service-area copy if findable, or flag for Jesse to confirm before Phase 2 ships the list.

## 6. Services offered

### Confirmed (Alignable lists as primary services)
1. **Electrical Repairs** — general residential repair work
2. **Ceiling Fan Installation**
3. **Recessed Lighting Installation**

### Mentioned across other surfaces (less confident — needs Bruce verification)
4. **Custom lighting** (per WebSearch synthesis from search snippets)
5. **Smart home technology** (per WebSearch synthesis; consistent with the "personal entertainment paradise" Facebook copy)
6. **Appliance repair** (per WebSearch synthesis — UNUSUAL for an electrician; may be a misattribution by the search-result snippet; flag for Bruce to confirm or remove)

### Inferred but NOT explicitly confirmed (typical residential-electrician offerings)
- Service panel upgrades
- EV charger installation
- Generator install
- Outdoor / landscape lighting (consistent with Instagram caption: "ready to take of your outdoor lighting needs")
- Whole-home rewiring (consistent with LinkedIn testimonial: "rewiring houses to trouble shooting small electrical problems")

**Phase 2 services-page recommendation (4 service cards, the multi-page scaffold convention):**
1. **Electrical Repair** (icon: `zap`) — general repair / troubleshooting / "fix problems other electricians can't"
2. **Ceiling Fans & Lighting** (icon: `lightbulb`) — ceiling fan install + recessed lighting + custom lighting
3. **Panel Upgrades** (icon: `battery-charging`) — IF confirmed; otherwise substitute Smart Home (icon: `home`)
4. **Outdoor & Smart Home** (icon: `house-plug` or `lamp-floor`) — outdoor lighting, smart-home integration, EV charging

The exact 4 to feature is a Phase 2 decision; Bruce's collection should pull SmartWire's full service list from any live source (FB posts, IG bio links, YouTube descriptions) to confirm before Phase 2 commits.

## 7. Verbatim testimonials & review fragments captured

### Alignable (2 recommendations)
1. **Dr. Troye Washington-Clanton (HOPE):** *"Experienced and knowledgeable, prompt and hard working. Terry Henry @ SmartWire Solutions LLC can fix your electrical problem when all other can't!"*
2. **Casey Brown (Tuckers Home Solutions):** *"Great friebflj service"* — typo, exclude or flag for revision

### LinkedIn (verbatim, attribution unknown — pulled via WebSearch)
3. *"Terry has great work ethics, integrity, and gives great customer service. I have known him for 10+ years, and he is the only electrician I would hire, or recommend."*
4. *"Over the last ten years I have hired Terry for any and all electrical needs. He has done everything from rewiring houses to trouble shooting small electrical problems. I have found him to be fast accurate and very fair with his pricing."*

### Google reviews (5.0 / 17)
- **NOT yet captured verbatim.** KP doesn't expose individual review dates or full text without scrolling/expansion that the captcha-protected surfaces won't permit reliably.
- **Phase 2 / Bruce blocker:** Bruce's §11.11 collection should pull verbatim Google reviews via Places API Place Details endpoint — note that this GBP is a service-area-business with `ftid=0x0` so `findplacefromtext` fails; Bruce will need to use the kgmid `/g/11j61b1qy5` or the cid `0x41524a050c3d29f4` as the lookup key. This is the SAB blind spot also flagged in `proposals/2026-04-28-r1vs-legitimacy-screen-share-url-mode.md`.

### Facebook (5/5 from 6 votes per KP cross-ref)
- Verbatim text NOT captured — Facebook page is JS-rendered and WebFetch returned truncated content. Bruce's collection should target this surface.

## 8. Cross-source phone / address consistency check

| Source | Phone | Address |
|---|---|---|
| BBB | (404) 382-9847 | 730 Peachtree St NE STE 570, Atlanta GA 30308-1244 |
| Yelp listing snippet | (404) 382-9847 | 730 Peachtree St NE, Atlanta GA 30308 |
| Google KP | (404) 635-6301 | (no street; SAB ftid=0x0) |
| Facebook description | (404) 382-9847 (per KP cross-ref) | not in extracted snippet |
| Jesse's handoff | (404) 382-9847 | unknown |
| Instagram bio | not extracted | "South Fulton Electrician" framing |

**Verdict:** Address fully consistent across BBB + Yelp. Phone fully consistent across BBB + Yelp + Facebook + Jesse + business's own copy on Facebook. Google KP's secondary phone is a benign discrepancy.

## 9. Phase 1 ambiguities / blockers for Phase 2

These are issues Phase 2 / Bruce / Jesse should resolve before the multi-page scaffold ships:

| # | Item | Severity | Recommended owner |
|---|---|---|---|
| 1 | License number / verification (GA SOS Construction Industry Licensing Board) | Medium — Master Electrician credential is a brand pillar; should be verifiable | Bruce (lookup during §11.11) or Jesse (one-touch CRM check) |
| 2 | 730 Peachtree St NE Ste 570 — real operating office, virtual mail-drop, or coworking suite? | Low — not site-displayed for SAB; affects no copy | Optional — Bruce can do a quick OSINT pass |
| 3 | Confirm / refute "appliance repair" as a service line | Medium — unusual for an electrician; if real, distinguishing differentiator; if misattribution, dropping it cleans the services page | Bruce (verify on FB/IG/YouTube) |
| 4 | Confirm panel upgrades, EV chargers, generators as service lines | Medium — these are typical residential electrician offerings; if Bruce can find reference to them in any SmartWire-controlled copy, treat as confirmed | Bruce (§11.11 collection) |
| 5 | Verbatim Google reviews (5.0 / 17) | High — site reviews-bar can't render Path A without ≥3 verbatim reviews; Path B (1-2) or Path C (0) renders empty if Bruce can't pull them | Bruce (§11.11 — primary deliverable; SAB workaround uses kgmid `/g/11j61b1qy5` or cid `0x41524a050c3d29f4`) |
| 6 | Service-area neighborhood list | Low — Phase 2 can populate from the synthesized list above with a Jesse review pass | Jesse (one-touch CRM confirmation) |
| 7 | Hero photo direction | Medium — `hero_intent: aspirational` recommended given parked website + no scraped photos in `photos-raw/`; Bruce should generate per §11.11.1 | Bruce (§11.11 — generated hero) |
| 8 | Reconcile "20+ years" tenure claim with 2020 LLC date in Phase 2 copy | Low — guidance in §2 above; lead with 2004 lineage | R1VS Phase 2 |

## 10. Sources

- [Terry Henry - Owner - SmartWire Solutions LLC | LinkedIn](https://www.linkedin.com/in/terry-henry-b761bb25/) — owner profile + verbatim testimonials
- [SmartWire Solutions LLC - Midtown Atlanta Atlanta, GA - Alignable](https://www.alignable.com/midtown-atlanta-atlanta-ga/smartwire-solutions-llc) — founding history, services, brand voice tagline
- [SmartWire Solutions LLC | BBB Business Profile | Better Business Bureau](https://www.bbb.org/us/ga/atlanta/profile/electrical-contractors/smartwire-solutions-llc-0443-28141526) — legal entity, address, officers, primary phone, BBB rating posture
- [SmartWire Solutions Home Electrical Services | Facebook](https://www.facebook.com/SmartWire365/) — page name, follower count via KP cross-ref
- [SmartWire Solutions | South Fulton Electrician (@smartwire365) • Instagram](https://www.instagram.com/smartwire365/) — bio framing, follower count
- [SmartWire Solutions - 730 Peachtree St NE - Yelp](https://www.yelp.com/biz/smartwire-solutions-atlanta) — address cross-ref via search snippet (full page captcha-blocked)
- [SmartWire Solutions: Metro Atlanta's Favorite Electricians](https://smartwire365.com/) — **PARKED domain** (curl-confirmed)
- [Google share URL → Knowledge Panel](https://share.google/odJwB0uvcD08lbYxb) — kgmid `/g/11j61b1qy5`, rating 5.0/17, hours, primary KP source for Phase 0 v2 verification

— R1VS Phase 1
