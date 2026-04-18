# GTMDot Icon Mapping Reference
**Icon Library:** [Lucide React](https://lucide.dev/icons/)
**Last updated:** 2026-04-02
**Purpose:** Definitive icon reference for GTMDot local business site builder. Every service on every site gets a semantically correct, non-duplicated icon. Attach to every copy brief before writing.

---

> **How to read this doc:** Icon names are exact Lucide identifiers. In React: `import { Wrench } from 'lucide-react'` (PascalCase). In the Notes column, ⚠️ means there's a common mix-up to watch for.

---

## Mobile Tire & Automotive

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Tire installation | `circle-dot` | Closest to a tire cross-section in Lucide. Never use `wrench` here — that's for mechanical repair. |
| Flat tire repair | `wrench` | Tool-on-vehicle work. Only acceptable `wrench` use in this vertical. |
| Curb rash repair | `paintbrush-2` | Surface restoration / cosmetic finish work. |
| Wheel balancing | `gauge` | Measurement + calibration connotation. |
| Roadside assistance | `triangle-alert` | Universal roadside hazard signal. |
| Fuel delivery | `fuel` | The gas pump icon. Exact match. |
| Battery jump / replacement | `battery-charging` | Distinguished from dead battery (`battery-low`). |
| Brake service | `disc` | Disc shape maps to a brake rotor. ⚠️ Don't use `wrench` — too generic. |
| Engine diagnostic | `stethoscope` | Diagnostic listening. Cleaner than `activity` for this use. |
| Tire rotation | `rotate-cw` | Rotational motion. Different from balancing. |
| Windshield repair (mobile) | `scan-line` | Scanning/inspecting a crack. |

---

## Pool Service

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Pool cleaning | `waves` | Water surface movement. Primary pool icon. |
| Chemical balance / water testing | `flask-conical` | Lab flask = chemistry/testing. Don't use `droplet`. |
| Equipment repair | `wrench` | Standard mechanical repair. |
| Pool heater installation | `flame` | Heat source. ⚠️ Don't use `thermometer` — that's for measuring, not generating heat. |
| Pump repair | `zap` | Electric motor connotation. Differentiates from generic wrench repair. |
| Leak detection | `droplet` | Single drip = leak. Distinguished from `waves` (surface) and `droplets` (spray). |
| Pool opening (spring) | `sun` | Seasonal opening. |
| Pool closing (winterizing) | `snowflake` | Seasonal closing. |
| Filter cleaning / replacement | `filter` | Exact match. |
| Algae treatment | `flask-conical` | Same as chemical balance — if you need to differentiate, use `bug-off` (algae as organism). |
| Safety inspection | `shield-check` | Compliance / safety review. |

---

## HVAC

| Service | Lucide Icon Name | Notes |
|---|---|---|
| New system installation | `package` | New unit arriving / being installed. ⚠️ Not `wrench` — that's repair. |
| AC / furnace repair | `wrench` | |
| Seasonal tune-up / maintenance | `settings` | Calibration and adjustment. |
| Emergency service | `zap` | Urgent power/system failure. ⚠️ Don't use `triangle-alert` — reserve that for roadside automotive. |
| Filter replacement | `filter` | Exact match. |
| Duct cleaning | `wind` | Airflow through ducts. |
| Thermostat installation / programming | `thermometer` | Temperature control. |
| Air quality testing | `activity` | Monitoring / reading data. |
| Air vent / register service | `air-vent` | Exact match for vent grilles. |
| Ventilation / exhaust fan | `fan` | Mechanical air movement. |
| Mini-split installation | `layers` | Multi-zone layered system. |
| Smart thermostat (Nest/Ecobee) | `wifi` | Connected/smart device. |

---

## Locksmith

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Emergency lockout (residential) | `door-open` | Door standing open after unlock. |
| Rekey service | `key` | Primary locksmith icon. Reserve for rekey specifically. |
| Deadbolt installation | `lock` | Physical bolt/padlock. |
| Car lockout | `car` | Vehicle context, not a door or key. |
| Safe opening / repair | `shield` | Vault protection. ⚠️ Don't use `archive` — that reads as file storage. |
| Commercial lock installation | `building-2` | Business/commercial context. |
| 24/7 emergency availability | `clock` | Always-on time signal. |
| Master key system | `key-round` | Distinguished from standard `key`. |
| Access control / keypad | `scan` | Electronic access scanning. |
| Lock repair | `wrench` | Mechanical fix. |

---

## Appliance Repair

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Washer repair | `washing-machine` | Exact Lucide icon. |
| Dryer repair | `wind` | Airflow / heat drying. ⚠️ Don't use `washing-machine` for dryers — they're separate icons in Lucide. |
| Refrigerator repair | `refrigerator` | Exact Lucide icon. |
| Oven / stove repair | `flame` | Heat source / cooking fire. |
| Dishwasher repair | `droplets` | Water spray cycle. Differentiated from `washing-machine`. |
| Microwave repair | `microwave` | Exact Lucide icon. |
| Freezer repair | `snowflake` | Cold storage. |
| Ice maker repair | `snowflake` | Same as freezer if needed, or `droplet` for water line issues. |
| Range hood / vent repair | `fan` | Air extraction. |
| Garbage disposal repair | `trash-2` | Waste processing. |

---

## Gutter Service

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Gutter cleaning | `trash-2` | Debris removal focus. ⚠️ Not `brush` — that implies painting. |
| Gutter repair | `wrench` | |
| Gutter installation | `hammer` | New construction / install. |
| Gutter guard installation | `shield` | Protection against debris ingress. |
| Downspout service | `arrow-down-to-line` | Water directed downward. |
| Gutter inspection | `search` | Looking for problems. |
| Christmas light installation | `lightbulb` | Lights, not electrical infrastructure. |
| Soffit & fascia repair | `layers` | Board layers behind gutter. |

---

## Pressure Washing

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Driveway / concrete cleaning | `droplets` | High-pressure water spray. Primary icon for this vertical. |
| House washing (exterior) | `home` | Whole-structure wash. |
| Deck / patio cleaning | `grid-3x3` | Deck boards / surface grid. |
| Roof soft wash | `cloud-rain` | Water falling on roof from above. |
| Fleet / truck washing | `truck` | Vehicle fleet. |
| Commercial property washing | `building-2` | Business structure. |
| Graffiti removal | `eraser` | Removing marks. Exact semantic match. |
| Fence washing | `fence` | |
| Dumpster pad cleaning | `trash-2` | Waste area context. |

---

## Handyman

| Service | Lucide Icon Name | Notes |
|---|---|---|
| General repair | `hammer` | Hands-on fix-it work. Primary handyman icon. |
| Drywall repair / patching | `square` | Wall panel / flat surface. |
| Interior painting | `paintbrush` | |
| Furniture assembly | `package` | Box-to-assembled item. ⚠️ Don't use `hammer` — that's structural repair. |
| TV mounting | `monitor` | Screen on wall. ⚠️ Use `monitor` not `tv` to avoid conflict with home theater vertical. |
| Door installation / repair | `door-open` | |
| Window repair / caulking | `maximize` | Window frame. |
| Caulking / weatherstripping | `pen-line` | Applying a bead/line. |
| Shelf / cabinet installation | `layout-dashboard` | Built-in organization. |
| Tile repair | `grid-2x2` | Grid of tiles. |
| Deck repair | `hammer` | Use same as general repair with descriptive label. |

---

## Landscaping

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Lawn mowing | `scissors` | Cutting. Primary landscaping icon. |
| Edging | `ruler` | Straight-line precision work. |
| Mulch installation | `layers` | Layered ground cover. |
| Tree / shrub trimming | `tree-pine` | Vegetation shaping. ⚠️ Don't use `scissors` for trimming — that's reserved for mowing. |
| Leaf removal | `leaf` | Falling leaf. Exact semantic match. |
| Irrigation / sprinkler service | `droplets` | Water delivery system. |
| Sod installation | `grid-3x3` | Sod panels laid in grid pattern. |
| Landscape design | `pencil-ruler` | Planning / design work. |
| Fertilization / treatment | `flask-conical` | Chemical application. |
| Aeration | `circle-dot` | Core aeration = holes in ground. |
| Stump removal | `axe` | Cutting / removal. Lucide has `axe`. |
| Snow removal (seasonal) | `snowflake` | Cold weather service. |

---

## Roofing

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Roof repair | `wrench` | Targeted fix. |
| Full roof installation | `hammer` | New construction. |
| Roof inspection | `search` | Looking for damage. |
| Gutter work (roofing context) | `arrow-down-to-line` | Same as gutter vertical — water flow. |
| Flashing installation / repair | `shield` | Waterproof barrier / protection layer. |
| Emergency tarping | `triangle-alert` | Urgent / storm damage response. |
| Commercial roofing | `building-2` | |
| Skylight installation | `sun` | Light-through-roof source. |
| Ventilation / ridge vent | `wind` | Airflow through roof. |
| Flat / TPO roofing | `layers` | Membrane layers. |
| Chimney flashing | `flame` | Chimney = fire source. |

---

## Painting

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Interior painting | `paintbrush` | Primary painting icon. |
| Exterior painting | `home` | Whole exterior / structure. ⚠️ Not `paintbrush` again — reserve that for interior. |
| Cabinet painting / refinishing | `paintbrush-2` | Detailed finish work. Distinguishes from broad interior painting. |
| Deck / fence staining | `fence` | Structure being stained. |
| Commercial painting | `building-2` | |
| Wallpaper removal | `layers` | Peeling layers off wall. |
| Color consultation | `palette` | Exact semantic match for color selection. |
| Trim / baseboards | `ruler` | Precise linear work. |
| Epoxy floor coating | `layers` | Multi-coat floor finish. |
| Pressure wash prep | `droplets` | Surface prep before painting. |

---

## Electrical

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Panel upgrade / replacement | `cpu` | Circuit board / control panel. More precise than `zap`. |
| Outlet / switch installation | `plug` | Physical outlet. |
| Lighting installation | `lightbulb` | Primary lighting icon. |
| EV charger installation | `plug-zap` | Exact match — Lucide has `plug-zap` for EV charging. |
| Generator installation | `zap` | Power generation. |
| Ceiling fan installation | `fan` | |
| Rewiring / home rewire | `cable` | Wiring / cabling. Lucide has `cable`. |
| Electrical inspection | `search` | Looking for issues. |
| Outdoor / landscape lighting | `lamp` | Fixture-specific. |
| Smart home / automation | `wifi` | Connected system. |
| Surge protector / whole-home | `shield-check` | Protection from power events. |
| Smoke / CO detector | `alarm-smoke` | Lucide has `alarm-smoke`. ⚠️ Not `bell`. |

---

## Plumbing

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Drain cleaning | `arrow-down-circle` | Water flowing down and through. |
| Leak detection / repair | `droplet` | Single drip = leak. Core plumbing icon. |
| Water heater installation / repair | `flame` | Heat source. ⚠️ Not `thermometer` — that measures temp, not generates heat. |
| Toilet repair / replacement | `wrench` | No toilet icon in Lucide; wrench is correct here. |
| Faucet / fixture installation | `settings` | Adjusting / fitting. |
| Pipe repair / replacement | `minus` | Horizontal pipe. Limited Lucide options here. Add label copy to compensate. |
| Sewer line service | `arrow-down-to-line` | Deep/down directional. |
| Emergency plumbing | `triangle-alert` | Urgent failure / flooding risk. |
| Water filtration / softener | `filter` | |
| Gas line service | `flame` | Gas = combustion source. |
| Backflow prevention | `arrow-left-right` | Flow reversal control. |
| Sump pump service | `arrow-down-to-line` | Pumping down and out. Use with clear label. |

---

## Fence

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Fence installation | `fence` | Exact Lucide icon. Primary fence icon. |
| Fence repair | `wrench` | |
| Fence staining / painting | `paintbrush` | |
| Gate installation | `door-open` | Gate = movable entry point. |
| Commercial fencing | `building-2` | |
| Privacy fence | `eye-off` | Blocking line of sight. Exact semantic match. |
| Chain link fence | `link-2` | Linked chain pattern. |
| Wood fence | `tree-pine` | Material origin (lumber/timber). |
| Vinyl fence | `layers` | Layered/manufactured panel material. |
| Post installation / repair | `minus` | Vertical structural post (when used with clear label). |

---

## TV Mounting & Home Theater

| Service | Lucide Icon Name | Notes |
|---|---|---|
| TV mounting | `tv` | Primary icon for this vertical. |
| Soundbar installation | `speaker` | |
| Projector installation | `projector` | Lucide has `projector`. |
| Cable management / concealment | `cable` | Lucide has `cable`. ⚠️ This is also used in Electrical — context differentiates. |
| Smart home integration | `wifi` | Connected ecosystem. |
| Surround sound / receiver | `radio` | Multi-channel audio system. |
| Home theater design | `layout-dashboard` | Room layout / system design. |
| Streaming device setup | `play-circle` | Media playback. |
| In-ceiling / in-wall speakers | `volume-2` | |
| Gaming setup | `gamepad-2` | Lucide has `gamepad-2`. |

---

## Pest Control

| Service | Lucide Icon Name | Notes |
|---|---|---|
| General pest treatment | `bug` | Primary pest icon. Use broadly. |
| Rodent control | `footprints` | Tracking / trapping rodents. Lucide has `footprints`. ⚠️ Don't use `mouse` — that's a computer mouse icon. |
| Termite treatment | `bug-off` | Elimination context. Differentiated from `bug`. |
| Bed bug treatment | `bed` | Lucide has `bed`. Direct semantic match. |
| Wasp / bee removal | `triangle-alert` | Sting danger / hazard. |
| Mosquito treatment | `zap` | Quick-kill spray. |
| Pest inspection | `search` | Looking for evidence. |
| Preventative / quarterly service | `shield-check` | Ongoing protection plan. |
| Ant treatment | `bug` | Same as general pest with specific label copy. |
| Wildlife / exclusion | `home` | Keeping animals out of structure. |

---

## Cleaning Services

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Standard house cleaning | `sparkles` | Clean / shine connotation. Primary cleaning icon. |
| Deep clean | `zap` | Intensive, thorough. |
| Move-in / move-out clean | `package` | Moving boxes / transition. |
| Commercial cleaning | `building-2` | |
| Window cleaning | `maximize` | Window frame / glass pane. |
| Carpet cleaning | `layers` | Carpet pile / fiber layers. |
| Post-construction cleaning | `hard-hat` | Construction aftermath. |
| Upholstery cleaning | `sofa` | Lucide has `sofa`. |
| Pressure wash (exterior cleaning) | `droplets` | ⚠️ Only use here if you're NOT running a dedicated pressure washing section. |
| Organizing / declutter | `layout-grid` | Ordered arrangement. |
| Disinfection / sanitizing | `shield-check` | Health protection. |
| Laundry service | `washing-machine` | |

---

## Auto Body & Collision

| Service | Lucide Icon Name | Notes |
|---|---|---|
| Dent repair | `car` | Vehicle with implied damage. Primary auto body icon. |
| Paintless dent repair (PDR) | `magnet` | Magnetic pulling technique. Exact process match. |
| Bumper repair / replacement | `shield` | Bumper = front protection element. |
| Scratch repair | `pen-line` | Linear surface mark. |
| Full paint / refinish | `paintbrush` | |
| Glass / windshield repair | `scan-line` | Scanning a crack / chip in glass. |
| Frame straightening | `ruler` | Precision alignment. |
| Insurance estimate / claim | `file-text` | Documentation / paperwork. |
| Detailing (as add-on) | `sparkles` | Polish and shine. |
| Rust repair | `triangle-alert` | Damage warning / structural concern. |

---

## Icons Bruce Should NEVER Use for Multiple Services

These are the most common icon reuse mistakes. Each section below names an icon, shows where it's correct, and flags the wrong uses.

---

### `wrench`
**Correct:** Flat tire repair, AC/furnace repair, roof repair, lock repair, toilet repair, fence repair, gutter repair
**Wrong uses (stop doing this):**
- ❌ Tire *installation* — use `circle-dot`
- ❌ Brake service — use `disc`
- ❌ Engine diagnostic — use `stethoscope`
- ❌ HVAC *installation* — use `package`
- ❌ Pool equipment repair when you already used `wrench` for HVAC repair on the same page — differentiate with icon + color or label-only blocks

**Rule:** `wrench` = repair/fix. Installation = `hammer`. Diagnostic = `stethoscope`. New unit = `package`.

---

### `home`
**Correct:** Exterior house washing (pressure wash), exterior house painting, pest exclusion (keeping animals out of structure)
**Wrong uses:**
- ❌ Any interior service — interior painting is `paintbrush`, not `home`
- ❌ General handyman — use `hammer`
- ❌ Smart home / thermostat — use `wifi` or `thermometer`
- ❌ House cleaning — use `sparkles`

**Rule:** `home` = the building's exterior shell. Anything happening *inside* or *to a system* gets a specific icon.

---

### `zap`
**Correct:** HVAC emergency service, generator install, mosquito treatment, deep clean (intensive)
**Wrong uses:**
- ❌ All electrical work — use `cpu`, `plug`, `lightbulb`, `plug-zap`, `cable` depending on service
- ❌ Roadside emergency — use `triangle-alert`
- ❌ Pump repair — `zap` is acceptable there but if you're already using it for HVAC emergency on the same page, differentiate

**Rule:** `zap` = urgency or energy. Don't let it become the default for "electricity."

---

### `shield`
**Correct:** Gutter guard install, flashing (roofing), safe service (locksmith), bumper repair, whole-home surge protection
**Wrong uses:**
- ❌ Any generic "protection" marketing — too vague
- ❌ Privacy fence — use `eye-off`
- ❌ Pest preventative — use `shield-check` (the checkmark variant is for completed/ongoing protection)

**Rule:** `shield` = physical barrier. `shield-check` = ongoing verified protection. Never use bare `shield` for abstract security concepts.

---

### `settings` (gear icon)
**Correct:** HVAC tune-up/maintenance, faucet/fixture fitting
**Wrong uses:**
- ❌ Any new installation — use `hammer` or `package`
- ❌ Smart home — use `wifi`
- ❌ Engine diagnostic — use `stethoscope`
- ❌ Thermostat programming — use `thermometer`

**Rule:** `settings` = calibrating something that already exists. Not a catch-all for "technical stuff."

---

### `triangle-alert`
**Correct:** Roadside assistance, roofing emergency tarping, emergency plumbing, wasp/bee removal, rust repair
**Wrong uses:**
- ❌ HVAC emergency — use `zap` for that
- ❌ Pest inspection — use `search`
- ❌ Any non-emergency service dressed up to sound urgent in copy

**Rule:** `triangle-alert` = actual hazard or structural emergency. One per page max — if every service has a warning triangle, none of them feel urgent.

---

### `layers`
**Correct:** Mini-split zoning (HVAC), mulch install, wallpaper removal, flat/TPO roofing, carpet cleaning, vinyl fence, drywall repair
**Wrong uses:**
- ❌ Carpet and drywall on the same page — pick one usage, not both
- ❌ "Comprehensive" or "full-service" as a generic icon — always tie it to a specific layered material

**Rule:** `layers` = stacked physical material. If you're not thinking about something that literally has layers, pick a different icon.

---

### `building-2`
**Correct:** Commercial context — commercial plumbing, commercial painting, commercial pest, commercial fencing, commercial HVAC, etc.
**Wrong uses:**
- ❌ Do NOT use this for residential services just because they're large jobs
- ❌ Do NOT repeat it for every commercial service on the same page without variation (pair with a service-specific icon instead)

**Rule:** One `building-2` per trade page max, for a clearly labeled "commercial" service tier.

---

### `paintbrush`
**Correct:** Interior painting, cabinet painting (use `paintbrush-2` to differentiate), scratch repair, handyman interior painting
**Wrong uses:**
- ❌ Exterior painting — use `home`
- ❌ Curb rash repair — use `paintbrush-2`
- ❌ Deck staining — use `fence` (the structure being stained is more specific)

**Rule:** `paintbrush` = fine interior/detail work. Exterior or structural surfaces → use the surface icon.

---

### `droplets`
**Correct:** Pressure washing (primary), dishwasher, irrigation
**Wrong uses:**
- ❌ Leak detection — use `droplet` (singular)
- ❌ Pool cleaning — use `waves`
- ❌ Water heater — use `flame`
- ❌ Don't use on plumbing AND pressure washing on the same site without differentiating via color or section

**Rule:** `droplets` = spray/volume of water. `droplet` = single drip/leak.

---

## Quick-Reference Cheat Sheet

| Icon | Best single use | Do NOT use for |
|---|---|---|
| `circle-dot` | Tire (auto) | Aeration (landscaping) if tires are on same page |
| `disc` | Brake rotor | CDs, anything media-related |
| `stethoscope` | Engine diagnostic | Medical services |
| `fuel` | Fuel delivery | Gas line plumbing (use `flame`) |
| `flask-conical` | Pool chemicals, fertilization | Pest control (use `bug`) |
| `eye-off` | Privacy fence | Data privacy, nothing else |
| `magnet` | Paintless dent repair | Nothing else on local biz sites |
| `eraser` | Graffiti removal | Nothing else |
| `plug-zap` | EV charger only | General electrical (use `plug` or `zap`) |
| `bed` | Bed bug treatment | Nothing else |
| `footprints` | Rodent tracking | Nothing else |
| `sofa` | Upholstery cleaning | Nothing else |
| `palette` | Color consultation | Nothing else |
| `gamepad-2` | Gaming setup | Nothing else on local biz sites |

---

*This document is a living reference. When a new trade vertical is added to GTMDot, add a section here before writing copy.*
