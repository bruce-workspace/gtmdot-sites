# R1VS handoff packet — The Landscape Addict LLC

**To:** Codex (Mac mini) and downstream Bruce/Mini
**From:** R1VS
**Date:** 2026-05-03
**Status:** Intake-prep artifact only. No deploys, no CRM writes, no outreach, no production changes. Read-only first unless Jesse approves changes.

---

## 1. Prospect identity

| Field | Value |
|---|---|
| Business name | The Landscape Addict LLC |
| Slug | `landscape-addict` |
| Vertical | landscaping (lawn / gutters / sod / hedge trimming) |
| CRM stage (last known to R1VS) | `research` |
| Entity type | LLC (per BBB) |
| Owner name | **Mr. Kore Bridges** (BBB Principal Contact + Yelp business owner blurb signed "Kore B." + Yelp customer review naming "Kore came out and helped...") |
| Years in business | 10 (per BBB) |
| Business start date | 2016-04-15 (per BBB) |

**Note on prior owner-name confusion:** earlier in the parent session, "Natalie White" appeared as an owner candidate. Resolved via direct website fetch — Natalie White is a customer-testimonial author quoted on `thelandscapeaddict.com`, NOT the owner. **Kore Bridges is the actual owner.** Three independent sources confirm.

## 2. Local source path

| Item | Path / status |
|---|---|
| Site directory | `sites/landscape-addict/` — DOES NOT EXIST. Net-new prospect. |
| Intake branch | `intake/landscape-addict` — DOES NOT EXIST. Net-new. |
| Pre-build intel (this artifact) | `messages/r1vs/2026-05-03-1531-r1vs-landscape-addict-handoff-packet.md` (this file) |
| Raw scraped sources | `/tmp/landscape-addict-yelp.md` (Yelp) and `/tmp/landscape-bbb.md` (BBB) — captured during prior session side-project work; not committed |
| "Local context files" referenced by Jesse | NOT YET LOCATED on R1VS-MacBook side. Jesse mentioned Landscape Addict has local context files; they likely live in a Paperclip artifact or Mac-mini-side directory. **Codex action requested:** locate + commit them to `sites/landscape-addict/` so R1VS Phase 1 can use them. |

## 3. Pages currently built

**None.** No HTML, no `RESEARCH.md`, no `BRAND.md`, no `business-data.json`, no `icon-intent.json`, no `legitimacy-check.json`. Nothing in `sites/landscape-addict/`. Phase 0 has not been run.

## 4. Screenshots available

**None on R1VS-MacBook side.** No KP scrape, no live-site screenshot. Yelp page has 4 photo thumbnails (URLs in §6).

## 5. Research / source links

| Source | URL | Status |
|---|---|---|
| Yelp | https://www.yelp.com/biz/the-landscape-addict-atlanta | Live, scraped to `/tmp/landscape-addict-yelp.md` |
| Yelp business ID | `I65E7e1NeEH3RDroso6IfA` | — |
| BBB | https://www.bbb.org/us/ga/atlanta/profile/landscape-contractors/the-landscape-addict-llc-0443-28139944 | Live, scraped to `/tmp/landscape-bbb.md` |
| BBB business ID | `0443-28139944` | — |
| Owner website | https://www.thelandscapeaddict.com/ | Live (confirmed via prior session WebFetch) |
| Facebook | https://www.facebook.com/landscapeaddictatl/ | Linked from BBB; not yet scraped (auth-walled per prior session) |
| LinkedIn | https://linkedin.com/company/the-landscape-addict | Linked from BBB; not scraped |
| Google Business Profile | Not yet identified by share_url / kgmid / cid | **Missing — Phase 0 blocker** |

## 6. Contact info found

| Field | Value | Source |
|---|---|---|
| Phone | (678) 369-3489 | Yelp + BBB (matches) |
| Address | 17 Park Ave SE, Atlanta, GA 30315-4061 | BBB |
| Service area | Atlanta, GA (per BBB "Serving the following areas") | BBB — pure SAB pattern likely |
| Hours | By Appt. Only (all 7 days) | BBB |
| Email | Available via BBB form (not direct) | BBB |
| Website | https://www.thelandscapeaddict.com/ | Yelp + BBB |

## 7. Photos / reviews already collected

### Photos
- 4 photos on Yelp listing (with caption metadata — useful):
  - "Fescue Sod Installation in Buckhead": `https://s3-media0.fl.yelpcdn.com/bphoto/aAUx5DRomPOm0fpngMpXuQ/l.jpg`
  - "Patio paver and sod Installation in Grant Park": `https://s3-media0.fl.yelpcdn.com/bphoto/3nV6vwp7ZKIDBSZ19Nm-pQ/l.jpg`
  - "Jungle Clearing in Decatur": `https://s3-media0.fl.yelpcdn.com/bphoto/LKiH-JkAD8XvsC1cnii0vQ/l.jpg`
  - "Fresh mulching in East Atlanta": `https://s3-media0.fl.yelpcdn.com/bphoto/BKai6b5GvHchEkEno68sWw/l.jpg`
- Owner avatar (Kore B.): `https://s3-media0.fl.yelpcdn.com/buphoto/oVebI2mUi6IKA7vX_TDpEg/90s.jpg`
- None saved locally.
- **Note:** Yelp captions explicitly tag Atlanta neighborhoods (Buckhead / Grant Park / Decatur / East Atlanta) — these are gold for service-area copy and per-photo `figcaption`s.

### Reviews
- **Verbatim reviews captured: 1** (full text, attributable):

> Amy C. (Atlanta, GA) — Apr 13, 2022 — First to Review:
> *"Kore came out and helped with some really overgrown hedges (trimming) and cleaning our gutters. He did a fantastic job and was super responsive. He did all the work for a great price. Will definitely have him help us again for any lawn needs we may have in the future!"*

- This review names the owner ("Kore"), describes specific services performed (hedge trimming + gutter cleaning), uses praise terms (fantastic, super responsive, great price), and mentions repeat-customer intent. Strong material for a Path B pull-quote per `DESIGN-HEURISTICS.md`.
- `reviews.json` does not exist for this site.

### Other Yelp / BBB signals
- Yelp Services Offered (verified): Lawn care
- Yelp categories: Lawn Services, Gutter Services
- BBB categories (extensive): Landscape Contractors, Lawn Maintenance, Gutters, Landscape Maintenance, Gutter Cleaning, Lawn Care, Landscape Design, Sod, Lawn Installation, Landscape Lighting, Lawn and Garden, Mulch, Commercial Landscape Contractors, Pine Straw, Seeding, Gardening, Brush Controls, Hedge Trimming, Gutter Contractors
- BBB rating: A+ (NOT BBB Accredited — `forbidden_phrases: ["BBB Accredited"]` constraint candidate)
- Owner blurb (Kore B., business owner, on Yelp): <q>I am passionate about customer service and landscaping</q> — single short clause, usable verbatim for an "About" section.

## 8. Known gaps

1. **GBP identity not resolved.** No share_url / kgmid / cid / place_id. Phase 0 blocker.
2. **Pure SAB pattern.** "By Appt. Only" + "Serving the following areas: Atlanta, GA" + private residential address (17 Park Ave SE) → likely service-area-business with no public storefront. SAB blind-spot risk for Places API findplacefromtext. Plan for chrome-devtools KP scrape fallback.
3. **Address treatment.** 17 Park Ave SE may be Kore Bridges's home address (residential block). Should NOT be displayed on the public site as a storefront. `address_treatment: "service_area_admin"` recommended (mention service area in service-area copy, do not publish street address).
4. **Only 1 verbatim review.** Yelp listing shows 1 recommended review (Amy C., 2022). Possible additional reviews on Google (not captured), Facebook, BBB. Below DESIGN-HEURISTICS Path A threshold (≥3 verbatim).
5. **Website content not yet captured.** R1VS hasn't WebFetch'd `thelandscapeaddict.com` in this session (was done in prior session per parent context). Bruce should pull current website copy for source-cited research.
6. **Facebook page not scraped.** `landscapeaddictatl` likely has substantial photo/post history; auth-walled in prior session attempts.
7. **Google review count + rating unknown.** Cannot confirm Google's ground truth without GBP identity.
8. **CRM row contents unknown to R1VS.** Codex/Mini side may have additional facts (lead source, prior outreach, claim code if assigned).
9. **Jesse-mentioned "local context files" not located.** May contain richer content / photos / prior research.

## 9. What Bruce scraping/enrichment would ideally add

Once Bruce auth is repaired and the main-DM lane is reset:

1. **GBP identification & legitimacy resolution** — Places API findplacefromtext on `"The Landscape Addict Atlanta"` (likely fails on SAB) → fallback to manual KP scrape via chrome-devtools, populate `gbp-data-from-kp.json`.
2. **Verbatim review pull** — Places API Place Details (top 5 Google reviews), Yelp full review-body scrape via Firecrawl, BBB customer reviews if any.
3. **Photo waterfall** — Places API photos (Google), Yelp photos (4 URLs already captured above with neighborhood captions), website photos via Firecrawl, Facebook photos if accessible.
4. **Owner photo** — Yelp owner avatar exists; Bruce should pull a higher-res version if available. Per §11.11, owner photo must be REAL (never generated).
5. **Hero generation** — gpt-image-2 hero per §11.11 (Atlanta yard / hedge / sod aesthetic, residential intown vibe matching Buckhead/Grant Park/Decatur photos).
6. **Website content scrape** — Firecrawl `thelandscapeaddict.com` for current service copy, testimonials, about-page (resolve "Natalie White" testimonial author for verbatim-quote sourcing).
7. **Facebook scrape** — `facebook.com/landscapeaddictatl/` for additional reviews + photos + Kore's posts.

## 10. Can the site proceed to Codex/Mini QA without Bruce?

**Closer to feasible than Mbanugo** — but still has blockers:

| Phase | Status without Bruce |
|---|---|
| Phase 0 (legitimacy) | **BLOCKED** without GBP identity. Could run with manual KP scrape (R1VS chrome-devtools fallback) → likely passes (10 years, A+ BBB, owner name confirmed). |
| Phase 1 (research) | **Feasible** with current Yelp + BBB intel + a fresh website fetch. Strong source backing already. |
| Phase 2 (brand + content) | **Feasible** with the captured Amy C. review + Kore's owner blurb + Yelp neighborhood photo captions. |
| Phase 3 (HTML build) | **Feasible** with Path C reviews stub (only 1 captured) and placeholder photo slots. Multi-page §11.11 standard achievable. |
| Hero image | **BLOCKED** until Bruce gpt-image-2 auth is repaired. Could ship with a placeholder + `data-resolved="false"` for Bruce later, but visually rough. |
| Photo gallery | **DEGRADED** — could use Yelp photo URLs as references for a Bruce-light pilot, but R1VS does not own photo download/license-clear pipeline. Better to wait for Bruce. |

**Verdict:** Landscape Addict is the better Bruce-light pilot candidate of the two prospects. R1VS could produce a Phase 1 + Phase 2 + Phase 3 (HTML skeleton with placeholder photo slots and Path C reviews stub) artifact set TODAY, leaving Bruce to fill photos + hero + additional reviews when back online. This is the "R1VS as Bruce fallback" runbook capability noted in the long Slack thread.

**Caveat:** Codex/Jesse must explicitly approve before R1VS runs the Bruce-light Phase 0–3. R1VS will not start without that ACK.

## 11. Recommendation for Codex

- **First-build candidate ranking (vs. Mbanugo Tires):** *Higher priority.* Owner name confirmed, BBB-A+ rating, 10-year tenure, real verbatim review, neighborhood-tagged photos, live website. Lower research burden, more usable material.
- **Pre-Phase-0 actions needed:**
  1. Codex pulls CRM row contents (to surface lead source, claim code if assigned, prior outreach state)
  2. Codex locates Jesse's "local context files" for this prospect and commits to `sites/landscape-addict/`
  3. Resolve GBP identity (share_url / kgmid / cid) — likely SAB, plan KP-scrape fallback
  4. Decide: wait-for-Bruce vs. R1VS Bruce-light pilot
- **If Bruce-light pilot approved:** R1VS can produce Phase 0–3 artifacts in a single iteration, with `data-resolved="false"` photo slots and Path C reviews stub for Bruce to fill later.

## 12. Constraints to consider for `input_spec.constraints`

```
forbidden_phrases: ["BBB Accredited"]   # NOT BBB-accredited (BBB rating A+ but not accredited)
address_treatment: "service_area_admin"   # 17 Park Ave SE is likely residential; do not publish street address
services_whitelist: [
  "lawn-maintenance", "lawn-care", "sod-installation",
  "hedge-trimming", "gutter-cleaning", "mulching",
  "landscape-design", "patio-paver-installation"
]
service_area_phrases: ["Atlanta", "Buckhead", "Grant Park", "Decatur", "East Atlanta"]
tenure_lead: "2016"   # 10 years per BBB
hero_intent: "intown-atlanta-residential-landscaping-trusted-owner-operator"
generated_images_allowed: "yes"   # subject to Bruce gpt-image-2 auth being repaired
owner_name: "Kore Bridges"
owner_first_name_for_copy: "Kore"   # appears in Amy C. review verbatim
exclude_domains_in_copy: []   # owner website is healthy; no exclusions needed
```

These are R1VS recommendations only — final values are Codex/Jesse's call.

## 13. Guardrails (per Codex's handoff request)

- Read-only first unless Jesse approves changes
- No outreach
- No CRM writes from this packet
- No deploys
- No production changes (this branch is `intake-prep/codex-handoff-2026-05-03`, not `main`)
- Bruce auto-routing stays paused until main-DM lane is reset
- If a Bruce-light Phase 0–3 pilot is approved, R1VS will write a separate finalization message at completion and explicitly tag what's pending Bruce vs. complete

— R1VS
