---
aliases:
  - structural load
tags:
  - flashcard/active/general/eng/structural_load
  - language/in/English
---

# structural load

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## loads on architectural and civil engineering structures

```Python
# pytextgen generate data
from asyncio import gather
from pytextgen.util import Result

items = R"""
[dead load](#dead%20load)
[environmental load](#environmental%20load)
[live load](#live%20load)
[load combinations](#load%20combinations)
[other loads](#other%20loads)
""".strip().splitlines()
return (
  Result(
    location=__env__.cwf_sect("28ba"),
    text=str(len(items) - 1),
  ),
  *await memorize_seq(
    __env__.cwf_sects("98ba", "cc19"),
    items,
  ),
)
```

Loads can be specified in {@{three ways}@}: {@{point load (load at a point) in kN, line load (load over a line) in kN/m, and distributed load (load over an area) in kN/m<sup>2</sup>}@}. <!--SR:!2027-10-24,976,350!2029-02-10,1357,360-->

Loads on civil engineering can be separated into {@{<!--pytextgen generate section="28ba"--><!-- The following content is generated at 2024-05-14T01:02:39.496907+08:00. Any edits will be overridden! -->4<!--/pytextgen-->}@} main categories. <!--SR:!2027-07-16,879,330-->

<!--pytextgen generate section="98ba"--><!-- The following content is generated at 2024-05-14T21:09:52.059240+08:00. Any edits will be overridden! -->

> 1. [dead load](#dead%20load)
> 2. [environmental load](#environmental%20load)
> 3. [live load](#live%20load)
> 4. [load combinations](#load%20combinations)
> 5. [other loads](#other%20loads)

<!--/pytextgen-->

<!--pytextgen generate section="cc19"--><!-- The following content is generated at 2024-05-14T21:09:52.082807+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[dead load](#dead%20load) <!--SR:!2027-12-25,1018,348!2029-11-23,1581,360-->
- [dead load](#dead%20load)→::@::←[environmental load](#environmental%20load) <!--SR:!2026-06-30,531,310!2031-04-23,1923,330-->
- [environmental load](#environmental%20load)→::@::←[live load](#live%20load) <!--SR:!2027-08-30,845,290!2026-02-01,374,308-->
- [live load](#live%20load)→::@::←[load combinations](#load%20combinations) <!--SR:!2026-09-14,602,320!2027-05-29,848,330-->
- [load combinations](#load%20combinations)→::@::←[other loads](#other%20loads) <!--SR:!2029-12-12,1481,310!2027-09-06,915,340-->
- [other loads](#other%20loads)→::@::←_(end)_ <!--SR:!2029-10-15,1551,360!2028-02-03,1043,340-->

<!--/pytextgen-->

### dead load

The dead load includes {@{loads that are relatively constant over time}@}. This includes {@{self-weights of structural members, such as beams, columns, floor slabs, roofs, and walls}@} and {@{weights of permanent fixtures such as carpets, tiles, walls, and windows}@}. Usually calculated by {@{density of material multiplied by component size}@}. <!--SR:!2029-11-12,1573,360!2026-01-31,466,310!2027-08-20,839,290!2028-09-11,1038,290-->

Generally, dead load (and live load) internally {@{deflects beams and floors}@}. As a whole, it causes {@{the foundation to settle, which may be uniform or tilt (e.g. [Leaning Tower of Pisa](Leaning%20Tower%20of%20Pisa.md))}@}. More seriously, {@{dishing or sagging may happen to the foundation}@}. If not managed well, it can lead to {@{partial or total collapse of structural elements or the roof}@}. <!--SR:!2028-03-11,1069,350!2028-04-03,1085,350!2027-12-10,1010,350!2027-12-06,1010,350-->

### live load

The live load includes {@{loads that are temporary or moving}@}. This includes {@{moving things, such as moving vehicles, people, and storage}@}; {@{non-permanent fixtures such as ceiling lights, furniture, and pipe ducts}@}. The load can vary in {@{location and magnitude}@}. In building codes such as {@{_Minimum Design Load for Buildings and Other Structures_, ASCE 7-05}@}, the live load is {@{tabulated and usually assumed uniform on building floors}@}. <!--SR:!2027-05-14,833,330!2026-10-11,676,340!2029-04-17,1185,290!2026-05-31,566,330!2029-01-31,1209,290!2026-09-20,659,340-->

Generally, live load has {@{similar effects to dead load}@}. <!--SR:!2028-02-24,1069,350-->

### environmental loads

```Python
# pytextgen generate data
items = R"""
[hydrostatic load](#hydrostatic%20load)
[lateral load](#lateral%20load)
[seismic load](#seismic%20load)
[thermal load](#thermal%20load)
[wind load](#wind%20load)
""".strip().splitlines()
return await memorize_seq(
  __env__.cwf_sects("ed23", "ab92"),
  items,
)
```

<!--pytextgen generate section="ed23"--><!-- The following content is generated at 2024-05-14T21:09:52.132885+08:00. Any edits will be overridden! -->

> 1. [hydrostatic load](#hydrostatic%20load)
> 2. [lateral load](#lateral%20load)
> 3. [seismic load](#seismic%20load)
> 4. [thermal load](#thermal%20load)
> 5. [wind load](#wind%20load)

<!--/pytextgen-->

<!--pytextgen generate section="ab92"--><!-- The following content is generated at 2024-05-14T21:09:52.106487+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[hydrostatic load](#hydrostatic%20load) <!--SR:!2026-05-23,515,310!2029-11-30,1587,360-->
- [hydrostatic load](#hydrostatic%20load)→::@::←[lateral load](#lateral%20load) <!--SR:!2028-08-02,1116,308!2030-02-17,1548,320-->
- [lateral load](#lateral%20load)→::@::←[seismic load](#seismic%20load) <!--SR:!2028-02-10,989,308!2026-02-12,429,300-->
- [seismic load](#seismic%20load)→::@::←[thermal load](#thermal%20load) <!--SR:!2028-02-25,938,280!2028-03-14,970,280-->
- [thermal load](#thermal%20load)→::@::←[wind load](#wind%20load) <!--SR:!2027-09-30,889,320!2029-02-18,1223,290-->
- [wind load](#wind%20load)→::@::←_(end)_ <!--SR:!2029-10-13,1550,360!2027-12-02,990,348-->

<!--/pytextgen-->

#### hydrostatic load

Hydrostatic load refers to load caused by {@{[water](water.md)}@}. The load can be caused by {@{pure water itself, or water in a material such as soil}@}. <!--SR:!2028-05-10,1132,350!2027-05-18,786,330-->

For example, when there is {@{water buildup in the soil}@}, there is {@{increased hydrostatic pressure on retaining walls}@}. For pure water, examples include a {@{[dam](dam.md), where deeper waters exert more horizontal hydrostatic pressure on the dam}@}. <!--SR:!2028-07-19,1185,350!2027-12-15,1005,340!2028-07-28,1195,350-->

#### lateral load

Lateral load may be caused by {@{bulk materials, [groundwater](groundwater.md), or [soil](soil.md)}@}. <!--SR:!2027-08-07,897,330-->

For example, there is lateral soil load on {@{retaining walls of a slope because the soil of a slope on the retained side tends to slip down, pushing the walls towards the excavated side}@}. This lateral soil load can cause {@{lateral deflection, toppling of the retaining structure, or even a landslide}@}. <!--SR:!2026-04-09,465,300!2026-10-01,645,320-->

To protect against soil loads, {@{retaining structures are built and weep holes may be installed}@}. Alternatively, {@{slopes on natural terrain can become man-made slopes, such as cut slopes, fill slopes, or retaining walls}@}. <!--SR:!2027-12-02,924,300!2026-07-07,581,320-->

#### seismic load

Seismic load are {@{caused by [earthquakes](earthquake.md)}@}. It can induce {@{both horizontal and vertical load on structures}@}. <!--SR:!2026-04-30,524,310!2026-12-20,729,340-->

The consequences are {@{partial or complete collapse of structural elements or entire buildings}@}. <!--SR:!2027-10-16,939,330-->

#### thermal load

Thermal load refers to load {@{caused by [temperature](temperature.md) changes leading to [thermal expansion](thermal%20expansion.md) (contraction) of structural and non-structural members}@}. <!--SR:!2026-04-18,480,308-->

For example, {@{a beam in between two fixed support creates thermal load under heating as the beam expands}@}. A solution would be {@{making the beam a simply supported beam instead, with one side a pinned support and the other side a roller support}@}. Then when thermal expansion occurs, {@{the beam can expand in the direction of the roller support, relieving the thermal load}@}. <!--SR:!2026-12-12,698,328!2027-09-15,916,330!2029-02-16,1362,360-->

#### wind load

[Wind](wind.md) is {@{movement of air}@}. When wind moves past a building, {@{wind changes in velocity}@}. Then, {@{the pressure of air changes}@}. Positive pressure outside {@{causes inward forces while negative causes outward (uplift for roof) forces}@}. This is wind load. It also depends on {@{building shape, wind direction, and wind speed}@}. <!--SR:!2028-01-09,1024,340!2027-03-28,798,330!2026-05-07,533,320!2027-11-20,985,340!2030-11-30,1834,340-->

Wind load causes {@{lateral deflection, which may further lead to toppling of the structure, such as collapse of bridges}@}. Less serious consequences include {@{damage to individual structural elements such as roofs, walls, and windows; and causes excessive building vibrations}@}. <!--SR:!2026-11-28,644,320!2026-04-30,481,300-->

### other loads

### load combinations

{@{Load (amplifying) factors}@} are used in {@{design equations to increase the design loads}@}, to {@{account for uncertainties involved when estimating loads}@}. An example is {@{_U_ = 1.2 _D_ + 1.6 _L_, where _D_ is the dead load and _L_ is the live load}@}. <!--SR:!2028-10-11,1253,350!2028-03-24,1096,350!2026-07-15,560,320!2027-09-12,936,340-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/structural_load) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
