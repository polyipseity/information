---
aliases:
  - structural load
tags:
  - flashcard/general/structural_load
  - language/in/English
---

# structural load

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
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

Loads can be specified in {{3}} ways: {{point load (load at a point) in kN, line load (load over a line) in kN/m, and distributed load (load over an area) in kN/m<sup>2</sup>}}. <!--SR:!2024-07-21,50,310!2024-08-08,66,320-->

Loads on civil engineering can be separated into {{<!--pytextgen generate section="28ba"--><!-- The following content is generated at 2024-05-14T01:02:39.496907+08:00. Any edits will be overridden! -->4<!--/pytextgen-->}} main categories. <!--SR:!2024-07-25,50,290-->

<!--pytextgen generate section="98ba"--><!-- The following content is generated at 2024-05-14T21:09:52.059240+08:00. Any edits will be overridden! -->

> 1. [dead load](#dead%20load)
> 2. [environmental load](#environmental%20load)
> 3. [live load](#live%20load)
> 4. [load combinations](#load%20combinations)
> 5. [other loads](#other%20loads)

<!--/pytextgen-->

<!--pytextgen generate section="cc19"--><!-- The following content is generated at 2024-05-14T21:09:52.082807+08:00. Any edits will be overridden! -->

- _(begin)_→:::←[dead load](#dead%20load) <!--SR:!2024-07-30,53,308!2024-08-22,77,320-->
- [dead load](#dead%20load)→:::←[environmental load](#environmental%20load) <!--SR:!2024-07-28,56,310!2024-07-06,37,290-->
- [environmental load](#environmental%20load)→:::←[live load](#live%20load) <!--SR:!2024-07-03,31,270!2024-08-16,72,328-->
- [live load](#live%20load)→:::←[load combinations](#load%20combinations) <!--SR:!2024-07-18,45,300!2024-07-19,49,290-->
- [load combinations](#load%20combinations)→:::←[other loads](#other%20loads) <!--SR:!2024-07-16,44,290!2024-08-08,65,320-->
- [other loads](#other%20loads)→:::←_(end)_ <!--SR:!2024-08-20,75,320!2024-08-02,57,300-->

<!--/pytextgen-->

### dead load

The dead load includes {{loads that are relatively constant over time}}. This includes {{self-weights of structural members, such as beams, columns, floor slabs, roofs, and walls}} and {{weights of permanent fixtures such as carpets, tiles, walls, and windows}}. Usually calculated by {{density of material multiplied by component size}}. <!--SR:!2024-08-21,76,320!2024-10-22,112,290!2024-09-21,83,270!2024-07-14,42,290-->

Generally, dead load (and live load) internally {{deflects beams and floors}}. As a whole, it causes {{the foundation to settle, which may be uniform or tilt (e.g. [Leaning Tower of Pisa](Leaning%20Tower%20of%20Pisa.md))}}. More seriously, {{dishing or sagging may happen to the foundation}}. If not managed well, it can need to {{partial or total collapse of structural elements or the roof}}. <!--SR:!2024-08-13,70,330!2024-08-17,73,330!2024-07-23,52,310!2024-07-22,52,310-->

### live load

The live load includes {{loads that are temporary or moving}}. This includes {{moving things, such as moving vehicles, people, and storage}}; {{non-permanent fixtures such as ceiling lights, furniture, and pipe ducts}}. The load can vary in {{location and magnitude}}. In building codes such as {{_Minimum Design Load for Buildings and Other Structures_, ASCE 7-05}}, the live load is {{tabulated and usually assumed uniform on building floors}}. <!--SR:!2024-07-21,48,290!2024-07-04,37,300!2024-07-18,48,290!2024-11-11,132,310!2024-07-25,45,270!2024-07-03,36,300-->

Generally, live load has {{similar effects to dead load}}. <!--SR:!2024-07-30,55,310-->

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

- _(begin)_→:::←[hydrostatic load](#hydrostatic%20load) <!--SR:!2024-07-13,41,290!2024-08-22,77,320-->
- [hydrostatic load](#hydrostatic%20load)→:::←[lateral load](#lateral%20load) <!--SR:!2024-07-03,34,288!2024-07-12,42,300-->
- [lateral load](#lateral%20load)→:::←[seismic load](#seismic%20load) <!--SR:!2024-09-21,85,288!2024-07-19,48,300-->
- [seismic load](#seismic%20load)→:::←[thermal load](#thermal%20load) <!--SR:!2024-07-05,14,260!2024-07-17,38,260-->
- [thermal load](#thermal%20load)→:::←[wind load](#wind%20load) <!--SR:!2024-07-06,38,300!2024-07-26,45,270-->
- [wind load](#wind%20load)→:::←_(end)_ <!--SR:!2024-08-19,75,320!2024-08-10,67,328-->

<!--/pytextgen-->

#### hydrostatic load

Hydrostatic load refers to load caused by {{[water](water.md)}}. The load can be caused by {{pure water itself, or water in a material such as soil}}. <!--SR:!2024-07-30,58,310!2024-07-25,54,310-->

For example, when there is {{water buildup in the soil}}, there is {{increased hydrostatic pressure on retaining walls}}. For pure water, examples include a {{[dam](dam.md), where deeper waters exert more horizontal hydrostatic pressure on the dam}}. <!--SR:!2024-08-03,61,310!2024-07-30,55,300!2024-07-31,59,310-->

#### lateral load

Lateral load may be caused by {{bulk materials, [groundwater](groundwater.md), or [soil](soil.md)}}. <!--SR:!2024-07-27,52,290-->

For example, there is lateral soil load on {{retaining walls of a slope because the soil of a slope on the retained side tends to slip down, pushing the walls towards the excavated side}}. This lateral soil load can cause {{lateral deflection, toppling of the retaining structure, or even a landslide}}. <!--SR:!2024-07-28,52,300!2024-07-23,52,300-->

To protect against soil loads, {{retaining structures are built and weep holes may be installed}}. Alternatively, {{slopes on natural terrain can become man-made slopes, such as cut slopes, fill slopes, or retaining walls}}. <!--SR:!2024-09-22,85,280!2024-07-16,47,300-->

#### seismic load

Seismic load are {{caused by [earthquakes](earthquake.md)}}. It can induce {{both horizontal and vertical load on structures}}. <!--SR:!2024-07-15,45,290!2024-07-09,40,300-->

The consequences are {{partial or complete collapse of structural elements or entire buildings}}. <!--SR:!2024-08-14,69,310-->

#### thermal load

Thermal load refers to load {{caused by [temperature](temperature.md) changes leading to [thermal expansion](thermal%20expansion.md) (contraction) of structural and non-structural members}}. <!--SR:!2024-07-21,51,308-->

For example, {{a beam in between two fixed support creates thermal load under heating as the beam expands}}. A solution would be {{making the beam a simply supported beam instead, with one side a pinned support and the other side a roller support}}. Then when thermal expansion occurs, {{the beam can expand in the direction of the roller support, relieving the thermal load}}. <!--SR:!2024-07-31,54,308!2024-08-12,68,310!2024-08-08,66,320-->

#### wind load

[Wind](wind.md) is {{movement of air}}. When wind moves past a building, {{wind changes in velocity}}. Then, {{the pressure of air changes}}. Positive pressure outside {{causes inward forces while negative causes outward (uplift for roof) forces}}. This is wind load. It also depends on {{building shape, wind direction, and wind speed}}. <!--SR:!2024-07-31,55,300!2024-07-16,46,290!2024-07-15,43,300!2024-07-30,54,300!2024-10-03,100,300-->

Wind load causes {{lateral deflection, which may further lead to toppling of the structure, such as collapse of bridges}}. Less serious consequences include {{damage to individual structural elements such as roofs, walls, and windows; and causes excessive building vibrations}}. <!--SR:!2024-08-06,63,320!2024-07-28,53,300-->

### other loads

### load combinations

{{Load (amplifying) factors}} are used in {{design equations to increase the design loads}}, to {{account for uncertainties involved when estimating loads}}. An example is {{_U_ = 1.2 _D_ + 1.6 _L_, where _D_ is the dead load and _L_ is the live load}}. <!--SR:!2024-08-06,64,310!2024-07-26,54,310!2024-07-11,42,300!2024-07-22,51,300-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/structural_load) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
