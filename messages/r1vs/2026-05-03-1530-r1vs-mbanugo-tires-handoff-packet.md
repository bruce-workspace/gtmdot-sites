# R1VS handoff packet — Mbanugo Tires

**To:** Codex (Mac mini) and downstream Bruce/Mini
**From:** R1VS
**Date:** 2026-05-03
**Status:** Intake-prep artifact only. No deploys, no CRM writes, no outreach, no production changes. Read-only first unless Jesse approves changes.

---

## 1. Prospect identity

| Field | Value |
|---|---|
| Business name | Mbanugo Tires |
| Slug | `mbanugo-tires` |
| Vertical | tires (auto / tire dealer) |
| CRM stage (last known to R1VS) | `research` |
| Entity type | Unverified — Yelp says "claimed" by business |
| Owner name | Unknown to R1VS |

## 2. Local source path

| Item | Path / status |
|---|---|
| Site directory | `sites/mbanugo-tires/` — DOES NOT EXIST. Net-new prospect. |
| Intake branch | `intake/mbanugo-tires` — DOES NOT EXIST. Net-new. |
| Pre-build intel (this artifact) | `messages/r1vs/2026-05-03-1530-r1vs-mbanugo-tires-handoff-packet.md` (this file) |
| Raw scraped source | `/tmp/mbanugo-yelp.md` (Yelp scrape, captured during prior session side-project work; not committed) |

## 3. Pages currently built

**None.** No HTML, no `RESEARCH.md`, no `BRAND.md`, no `business-data.json`, no `icon-intent.json`, no `legitimacy-check.json`. Nothing in `sites/mbanugo-tires/`. Phase 0 has not been run.

## 4. Screenshots available

**None on R1VS-MacBook side.** No KP scrape, no live-site screenshot. Yelp page has 7 photo thumbnails (URLs in §6).

## 5. Research / source links

| Source | URL | Status |
|---|---|---|
| Yelp | https://www.yelp.com/biz/mbanugo-tires-atlanta-3 | Live, scraped to `/tmp/mbanugo-yelp.md` |
| Yelp business ID | `rmfFqNO7ZpcBDGomASk0_g` | — |
| Owner website | `mbanugotires.com` (referenced indirectly; not confirmed live) | **Cert expired (`net::ERR_CERT_DATE_INVALID`)** during prior session — likely effectively dead |
| Google Business Profile | Not yet identified by share_url / kgmid / cid | **Missing — Phase 0 blocker** |
| BBB | Not searched | — |
| Facebook | Not searched | — |

## 6. Contact info found

| Field | Value | Source |
|---|---|---|
| Phone | (678) 613-0489 | Yelp |
| Address | 921 White St SW, Atlanta, GA 30310 | Yelp (West End neighborhood) |
| Service area | "Serving Atlanta Area" | Yelp (suggests partial SAB pattern: physical address + delivery) |
| Hours | Mon–Sat 9:00 AM – 9:00 PM; Sun closed | Yelp |
| Email | Not captured | — |
| Website | `mbanugotires.com` (cert-expired per prior session) | — |

## 7. Photos / reviews already collected

### Photos
- 7 photos visible on Yelp listing (tire-mounting, shop interior). URLs:
  - `https://s3-media0.fl.yelpcdn.com/bphoto/lAMaWVK3sFcQHeHF91RzSQ/l.jpg` (Tires mounted)
  - `https://s3-media0.fl.yelpcdn.com/bphoto/iiDc1Tgbc5FTSC1oE91CMA/l.jpg`
  - `https://s3-media0.fl.yelpcdn.com/bphoto/th__1XA5rf2KFH4Gic-Y0A/l.jpg` (Tires)
  - `https://s3-media0.fl.yelpcdn.com/bphoto/ubfoZc0Nk_ZGirAkbyfXoA/l.jpg`
  - `https://s3-media0.fl.yelpcdn.com/bphoto/tfdgCPL67J82X4wUjYgAqw/l.jpg`
  - `https://s3-media0.fl.yelpcdn.com/bphoto/BtkMuCNToMMdOi5WkhCOhw/l.jpg`
  - `https://s3-media0.fl.yelpcdn.com/bphoto/1V_cfk1_w9uTTviEV9wX6A/l.jpg`
- None saved locally.

### Reviews
- **Verbatim reviews captured: 0.**
- Yelp listing shows 5.0 rating with 1 recommended review + 4 not-currently-recommended. Recommended review text was NOT in the captured Yelp markup (Yelp gates review bodies behind interaction triggers).
- `reviews.json` does not exist for this site.

### Other Yelp signals
- Services Offered (Yelp-verified): Auto wheel and tire repair, Tire installation, Tire rotation, Tire balancing, Tire repair
- Categories: Tires
- Amenities: Accepts cash, Accepts credit cards, **Black-owned** (potential brand signal — verify with Jesse before using in copy), Wi-Fi
- About-business excerpt (truncated): <q>Mbanugo Tires is the one-stop destination for all your tire needs in Atlanta, GA</q>

## 8. Known gaps

1. **GBP identity not resolved.** No share_url / kgmid / cid / place_id captured. Phase 0 legitimacy check cannot run without one. SAB-blind-spot risk if listing is service-area-only.
2. **Owner name unknown.** Not on Yelp public profile. BBB / Secretary-of-State / Facebook may surface it.
3. **Owner website effectively dead** (cert-expired). Cannot use as primary research source. Should be excluded from outbound copy (`exclude_domains_in_copy`).
4. **Zero verbatim reviews captured.** Public listing claims 5.0 with 1 recommended + 4 not-currently-recommended, but body text is gated. Bruce or a paid Places API call would be needed to pull review bodies.
5. **No Google KP screenshot or business profile data.** Cannot confirm photo count / rating / review count from Google's ground truth.
6. **No Facebook search done.** Likely a treasure trove for photo + review intel per prior thread context.
7. **CRM row contents unknown to R1VS-MacBook.** R1VS doesn't have Supabase read access wired. Codex/Mini side may have additional facts already in `prospects` row.
8. **Service-area pattern unclear.** Has physical address (921 White St SW) AND "Serving Atlanta Area" — could be a brick-and-mortar with mobile add-on, or could be SAB-presented-as-storefront. Affects address_treatment constraint.

## 9. What Bruce scraping/enrichment would ideally add

Once Bruce auth is repaired and the main-DM lane is reset:

1. **GBP identification & legitimacy resolution** — Places API findplacefromtext on `"Mbanugo Tires Atlanta"` to get place_id; if SAB blind-spot triggers, manually scrape Knowledge Panel from a Google search and write `gbp-data-from-kp.json` per §11.11.
2. **Verbatim review pull** — Places API Place Details `reviews[]` (top 5 max from Google) + Yelp review-body scrape (Firecrawl, since DataDome blocks WebFetch + chrome-devtools).
3. **Photo waterfall** — Places API photos[] (Google), Yelp photos[] (already URL-captured above), Facebook photos if accessible. Goal: 10+ candidate photos for hero + gallery selection.
4. **BBB profile** — search BBB for `mbanugo tires atlanta` to surface business-management contact name + tenure.
5. **Facebook page** — locate `facebook.com/mbanugotires*` or similar; pull additional photos + owner posts.
6. **Hero generation** — once auth is repaired, gpt-image-2 hero per §11.11 (tire-shop atmosphere, black-owned positioning if Jesse approves).
7. **Owner identity** — name resolution from any of the above sources.

## 10. Can the site proceed to Codex/Mini QA without Bruce?

**No, not at acceptable §11.11 quality.** Specific blockers:

- Phase 0 legitimacy check requires a resolved GBP identity. Without Bruce or chrome-devtools manual KP scrape, R1VS can't populate `legitimacy-check.json`.
- §11.11 multi-page build requires real photos in `photos/` slots. Yelp's 7 photos are URLs — Bruce's photo waterfall is the canonical path to download + license-clear them.
- Verbatim reviews `reviews.json` should have ≥3 captures for Path A/B routing per `DESIGN-HEURISTICS.md`. Current capture: 0. Path C empty-state stub is possible but suboptimal for a reviews-light prospect.
- Hero image needs gpt-image-2 generation — Bruce-side capability post-auth-repair.

**However:** R1VS *could* run a degraded Phase 0–1–2 with what's currently captured + a manual KP scrape (chrome-devtools fallback per §11.11 SAB blind-spot pattern), producing a Phase-2-complete artifact set with placeholder photo slots. That's a "Bruce-light pilot" pattern noted in the long Slack thread (R1VS as fallback for Bruce's photo + review steps). Codex/Jesse decision whether to take that path or wait for Bruce.

## 11. Recommendation for Codex

- **First-build candidate ranking (vs. Landscape Addict):** *Lower priority.* GBP identity unresolved, owner name unknown, zero verbatim reviews, owner website dead. More gaps to close before Phase 0.
- **Pre-Phase-0 actions needed:**
  1. Codex pulls CRM row (or commits to `sites/mbanugo-tires/intake-spec.yaml`)
  2. Resolve GBP identity (share_url / kgmid / cid)
  3. Confirm SAB-or-storefront pattern for `address_treatment`
  4. Decide whether to wait for Bruce or run R1VS Bruce-light pilot
- **Do not** auto-promote to `phase_0_passed` from this artifact. Use as the input for whichever party (Codex, Bruce-when-back, or Jesse) populates the proper job spec.

## 12. Constraints to consider for `input_spec.constraints`

When this prospect eventually becomes a build job:

```
forbidden_phrases: ["BBB Accredited"]   # not yet confirmed BBB-accredited; default-ban claim
exclude_domains_in_copy: ["mbanugotires.com"]   # cert-expired, do not link
address_treatment: "tbd"   # decide after SAB-vs-storefront resolution
services_whitelist: ["tire-installation", "tire-repair", "tire-rotation", "tire-balancing", "wheel-and-tire-repair"]
hero_intent: "trustworthy-neighborhood-tire-shop"
generated_images_allowed: "yes"
```

These are R1VS recommendations only — final values are Codex/Jesse's call.

## 13. Guardrails (per Codex's handoff request)

- Read-only first unless Jesse approves changes
- No outreach
- No CRM writes from this packet
- No deploys
- No production changes (this branch is `intake-prep/codex-handoff-2026-05-03`, not `main`)
- Bruce auto-routing stays paused until main-DM lane is reset

— R1VS
