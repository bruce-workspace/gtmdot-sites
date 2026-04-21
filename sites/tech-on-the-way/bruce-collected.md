---
slug: tech-on-the-way
collected_by: bruce
collected_at: 2026-04-21T13:25:00Z
---

# Bruce Collected — Tech On The Way, LLC

## Summary

- **Photos collected:** 15 (budget cap hit — owner website)
- **Reviews collected:** 10 (Yelp, page 1 of ~3 — budget not hit, but Yelp pagination requires JS interaction beyond Firecrawl's single-pass)
- **Google Places:** not found — business does not appear in Google Places API (service-area business with no storefront; may be listed under alternate name or not indexed)

---

## Source Outcomes

### 1. Owner Website (techonthewaymobile.com) — ✅ SUCCESS
- **Tool:** Firecrawl crawl (v1/crawl + v1/scrape)
- **Photos found:** 15 (from homepage + blog post page `/welcome/f/the-benefits-of-mobile-truck-repair-services`)
- **Saved as:** `photos-raw/owner-01.jpg` through `photos-raw/owner-15.jpg`
- **Notable finds:**
  - `owner-01.jpg` — hero image (`mc.jpg`) — likely branded truck or Celena at job site
  - `owner-02.jpg` through `owner-04.jpg` — section photos from homepage (Photo 10, Photo 8, Photo 17)
  - `owner-05.jpg` through `owner-14.jpg` — dated job site photos (20220222, 20220223, 20220302, 20220306, 20220217, 20220524, 20210904, 20220112, 20210811, 20220302)
  - `owner-15.jpg` — high-res version of Photo 8 (`rs=w:1280`)
- **Budget cap hit at 15 photos — Yelp photos not downloaded**

### 2. Yelp (_cVwB1vPMdGkfemQYSGGKA) — ✅ PARTIAL
- **Tool:** Firecrawl (v1/scrape with JS rendering)
- **Photos found:** 20 Yelp photos (URLs captured, not downloaded — photo budget already at cap)
- **Reviews captured:** 10 of 23
- **Failure reason for remaining 13 reviews:** Yelp only loads first 10 in a single-pass scrape; pagination requires JS click interaction (not available without Scrapfly or browser automation)
- **Reviews saved to:** `reviews-raw.json`

#### Yelp photo URLs (not downloaded — photo budget cap):
```
https://s3-media0.fl.yelpcdn.com/bphoto/Wh-e81HA-IdcUYplgjEn8g/l.jpg  (Tech On The Way Mobile)
https://s3-media0.fl.yelpcdn.com/bphoto/7I7o27MLYlHugbytVHObSw/l.jpg
https://s3-media0.fl.yelpcdn.com/bphoto/zZWvzeviGitTSnnOt2ux8w/l.jpg
https://s3-media0.fl.yelpcdn.com/bphoto/EtMipZxsBSGN3Y3OnMA4JQ/l.jpg  (Electrical Diagnostics)
https://s3-media0.fl.yelpcdn.com/bphoto/6cJ1BbGfgkl0_aqwgd5ZDA/l.jpg  (Mobile Mechanic, Mobile Repair Service)
https://s3-media0.fl.yelpcdn.com/bphoto/b_kcS7U5rFPW-e7qREtaCQ/l.jpg  (Belt Tensioner)
https://s3-media0.fl.yelpcdn.com/bphoto/SJRkzcXx37LFJfgt8cEehw/l.jpg  (Coolant Leak)
https://s3-media0.fl.yelpcdn.com/bphoto/Uv1LY9_FwbRBwjjzycML3A/l.jpg  (Air Leak)
https://s3-media0.fl.yelpcdn.com/bphoto/_qsoTPRxnGoHHCHbJEZlpA/l.jpg  (Ignition Coils)
https://s3-media0.fl.yelpcdn.com/bphoto/xQ4AhyWJ544LjPTXP2YnNQ/l.jpg  (Mobile Service Unit)
https://s3-media0.fl.yelpcdn.com/bphoto/8VKbCjToSS0YWRKU3_il5Q/l.jpg  (Catalytic Converter)
https://s3-media0.fl.yelpcdn.com/bphoto/NyMhR7muomK8HX1o8_C28Q/l.jpg  (Battery)
https://s3-media0.fl.yelpcdn.com/bphoto/g-JRI7JkR1r39z5V090rrg/l.jpg  (Starter)
https://s3-media0.fl.yelpcdn.com/bphoto/MQABQwKkyv6s3hwKz-Rbmw/l.jpg  (Liftgate Hydraulic Pump)
https://s3-media0.fl.yelpcdn.com/bphoto/XiIcKAAbokzM7wONN2nnEA/l.jpg  (Trailer Door)
https://s3-media0.fl.yelpcdn.com/bphoto/2gHS_Jc0k7_ZIA0RpcyMTA/l.jpg  (Light Repair)
https://s3-media0.fl.yelpcdn.com/bphoto/07xTmcuAue7TjhzTCHouLQ/l.jpg  (Roll Up Door Rollers)
https://s3-media0.fl.yelpcdn.com/bphoto/f8_NMiMDq01wmCWyuKIM1A/l.jpg  (Exhaust Stack)
https://s3-media0.fl.yelpcdn.com/bphoto/PrwZ13m_xSYE-86J-FNWeg/l.jpg  (Parking Brake)
https://s3-media0.fl.yelpcdn.com/bphoto/dO-Gz4Lea1dhRt2jWDcAUA/l.jpg  (Fuel Filter)
```

### 3. Google Places API — ❌ NOT FOUND
- **Failure reason:** `not-found`
- **Attempted queries:** multiple variations of business name + location, phone number, website URL
- **Notes:** Tech On The Way is a service-area business (no storefront). It may appear on Google Maps under a different listing name, or may not be indexed in the Places API. Rating of 4.6 / 97 reviews mentioned in collect-request — those reviews remain uncaptured.

### 4. Instagram (@techonthewaymobile) — ❌ BLOCKED
- **Failure reason:** `login-wall` (no Scrapfly key available; direct curl blocked by JS challenge)
- **Tool attempted:** direct curl (Scrapfly not configured on this machine)

### 5. Facebook (facebook.com/TechOnTheWayMobile) — ❌ BLOCKED
- **Failure reason:** `login-wall` (no Scrapfly key available; Facebook requires login for content)
- **Tool attempted:** direct curl

---

## Notes for Mini

- **Yelp photo URLs are captured above** — if Mini wants to wire in Yelp photos, the full-res `/l.jpg` URLs are ready. Notable ones for intent matching: Electrical Diagnostics, Belt Tensioner, Air Leak, Coolant Leak (diesel work evidence), Mobile Service Unit (branded truck), Exhaust Stack, Catalytic Converter.
- **Google reviews (97) are uncaptured** — the business likely uses a different listing or is not indexed via standard API. A manual Google Maps search may find the GBP page.
- **Yelp reviews:** 10 of 23 captured. Reviews show a mixed picture — strong positive reviews from Terese H., Lelia's E., Talia R., Calista F. alongside some negative experiences (communication/timing issues). The highlighted reviews in RESEARCH.md are the positive ones.
- **No SCRAPFLY_API_KEY found** in environment — Instagram and Facebook unavailable without it.
