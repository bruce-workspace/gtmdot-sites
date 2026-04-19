# Sandy Springs Plumbing Share — Research

## ⚠️ DATA QUALITY FLAG — recommend Jesse review for disqualification or rebuild-queue correction

## Basic Info (as-provided in rebuild-queue.json)
- **Name:** Sandy Springs Plumbing Share
- **Owner:** null
- **Industry:** Plumbing
- **City/State:** Atlanta, GA (note: city mismatch with name — name says "Sandy Springs" but city says "Atlanta")
- **Phone:** null
- **Email:** null
- **GBP URL:** null
- **Website:** Not surfaced
- **Claim code:** SSPS4553 (preserved)

## Why this is flagged

**The slug ends in `-share`, and every contact field is null.** This pattern strongly suggests:

1. **The slug was generated from an orphaned GBP share URL fragment** that never got resolved to a real business name + contact info. The word "Share" is not a plausible business-name suffix (no GA plumbing business uses "Share" in its name per web search).
2. **The city/state mismatch** (name "Sandy Springs" but city "Atlanta") suggests sloppy or auto-generated metadata, not a real owner-validated listing.
3. **Potential duplicate** of the already-processed `sandy-springs-plumber-sewer-septic` (claim code SSPS4071, also Sandy Springs, also Plumbing, GBP URL available) — "Sandy Springs Plumbing Share" may have been the GBP share URL used to scrape that business, with the slug accidentally retained as a separate entry.

## Web search attempts
- **Google search** for "Sandy Springs Plumbing Share" Atlanta Georgia: anti-scrape returned, no organic business by that exact name
- **DuckDuckGo search**: no business by that name
- **BBB**: no listing under this name (earlier lookup)
- **No website, no phone, no GBP URL** in rebuild-queue to retry against

## Classification per HANDOFF-CONTRACT

**Data quality issue — similar to posh-paws-atlanta flag.** Does NOT fit the empty-shell 2-pass variant cleanly because there's no Bruce-actionable handle (no GBP URL, no name, no phone). Recommend Jesse:

1. **Check rebuild-queue.json source** — was this a scrape of a GBP share URL that lost context? If so, correct the entry with the real business name + contact info.
2. **OR disqualify the slug** if no real business can be identified — consistent with `sandy-springs-plumber-sewer-septic` likely being the intended business (same claim-code prefix SSPS).
3. **OR confirm it's a separate business** and add the missing owner-provided contact info.

## Recommendation

**Disqualify unless rebuild-queue.json source can resolve it to a real business.** The all-null signature + "share" slug suffix + duplicate-ish claim-code prefix with sandy-springs-plumber-sewer-septic all point toward stale/orphaned data rather than a genuine prospect.

## Content-craft status (pass-1 deliverable)
- ✅ RESEARCH.md — this document (data-quality flag)
- ✅ reviews.json — `captured: 0` + disqualification flag
- ✅ photos/intent.json — skeleton plumbing vertical, do-not-waterfall flag
- ❌ index.html — DO NOT build until Jesse resolves data-quality flag

## Outreach angles
**N/A — disqualification pending.** No real business identified to outreach to.

---

*Research compiled 2026-04-19. Flagged for Jesse per HANDOFF-CONTRACT §3 data-quality pattern established with posh-paws-atlanta.*
