---
aliases:
  - structural load
tags:
  - flashcard/general/structural_load
  - language/in/English
---

# structural load

%%

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

%%

## loads on architectural and civil engineering structures

%%

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

%%

Loads can be specified in {{3}} ways: {{point load (load at a point) in kN, line load (load over a line) in kN/m, and distributed load (load over an area) in kN/m<sup>2</sup>}}. <!--SR:!2024-06-01,13,290!2024-06-03,15,300-->

Loads on civil engineering can be separated into {{<!--pytextgen generate section="28ba"--><!-- The following content is generated at 2024-05-14T01:02:39.496907+08:00. Any edits will be overridden! -->4<!--/pytextgen-->}} main categories. <!--SR:!2024-06-05,17,290-->

<!--pytextgen generate section="98ba"--><!-- The following content is generated at 2024-05-14T21:09:52.059240+08:00. Any edits will be overridden! -->

> 1. [dead load](#dead%20load)
> 2. [environmental load](#environmental%20load)
> 3. [live load](#live%20load)
> 4. [load combinations](#load%20combinations)
> 5. [other loads](#other%20loads)

<!--/pytextgen-->

<!--pytextgen generate section="cc19"--><!-- The following content is generated at 2024-05-14T21:09:52.082807+08:00. Any edits will be overridden! -->

- _(begin)_→:::←[dead load](#dead%20load) <!--SR:!2024-06-07,18,308!2024-06-06,18,300-->
- [dead load](#dead%20load)→:::←[environmental load](#environmental%20load) <!--SR:!2024-06-02,14,290!2024-05-30,10,270-->
- [environmental load](#environmental%20load)→:::←[live load](#live%20load) <!--SR:!2024-06-02,13,270!2024-06-05,17,308-->
- [live load](#live%20load)→:::←[load combinations](#load%20combinations) <!--SR:!2024-06-03,15,300!2024-05-31,12,270-->
- [load combinations](#load%20combinations)→:::←[other loads](#other%20loads) <!--SR:!2024-06-02,14,290!2024-06-04,16,300-->
- [other loads](#other%20loads)→:::←_(end)_ <!--SR:!2024-06-06,18,300!2024-06-06,18,300-->

<!--/pytextgen-->

### dead load

The dead load includes {{loads that are relatively constant over time}}. This includes {{self-weights of structural members, such as beams, columns, floor slabs, roofs, and walls}} and {{weights of permanent fixtures such as carpets, tiles, walls, and windows}}. Usually calculated by {{density of material multiplied by component size}}. <!--SR:!2024-06-06,18,300!2024-06-01,12,270!2024-05-30,11,270!2024-06-02,14,290-->

Generally, dead load (and live load) internally {{deflects beams and floors}}. As a whole, it causes {{the foundation to settle, which may be uniform or tilt (e.g. [Leaning Tower of Pisa](Leaning%20Tower%20of%20Pisa.md))}}. More seriously, {{dishing or sagging may happen to the foundation}}. If not managed well, it can need to {{partial or total collapse of structural elements or the roof}}. <!--SR:!2024-06-04,16,310!2024-06-05,17,310!2024-06-01,13,290!2024-05-31,12,290-->

### live load

The live load includes {{loads that are temporary or moving}}. This includes {{moving things, such as moving vehicles, people, and storage}}; {{non-permanent fixtures such as ceiling lights, furniture, and pipe ducts}}. The load can vary in {{location and magnitude}}. In building codes such as {{_Minimum Design Load for Buildings and Other Structures_, ASCE 7-05}}, the live load is {{tabulated and usually assumed uniform on building floors}}. <!--SR:!2024-06-03,15,290!2024-05-28,9,280!2024-05-31,12,270!2024-05-29,9,270!2024-06-10,17,270!2024-05-28,9,280-->

Generally, live load has {{similar effects to dead load}}. <!--SR:!2024-06-05,17,310-->

### environmental loads

%%

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

%%

<!--pytextgen generate section="ed23"--><!-- The following content is generated at 2024-05-14T21:09:52.132885+08:00. Any edits will be overridden! -->

> 1. [hydrostatic load](#hydrostatic%20load)
> 2. [lateral load](#lateral%20load)
> 3. [seismic load](#seismic%20load)
> 4. [thermal load](#thermal%20load)
> 5. [wind load](#wind%20load)

<!--/pytextgen-->

<!--pytextgen generate section="ab92"--><!-- The following content is generated at 2024-05-14T21:09:52.106487+08:00. Any edits will be overridden! -->

- _(begin)_→:::←[hydrostatic load](#hydrostatic%20load) <!--SR:!2024-06-02,14,290!2024-06-06,18,300-->
- [hydrostatic load](#hydrostatic%20load)→:::←[lateral load](#lateral%20load) <!--SR:!2024-05-30,11,288!2024-05-31,11,280-->
- [lateral load](#lateral%20load)→:::←[seismic load](#seismic%20load) <!--SR:!2024-05-29,10,288!2024-06-01,12,280-->
- [seismic load](#seismic%20load)→:::←[thermal load](#thermal%20load) <!--SR:!2024-05-28,9,280!2024-05-25,6,260-->
- [thermal load](#thermal%20load)→:::←[wind load](#wind%20load) <!--SR:!2024-05-29,10,280!2024-05-25,5,250-->
- [wind load](#wind%20load)→:::←_(end)_ <!--SR:!2024-06-05,17,300!2024-06-04,16,308-->

<!--/pytextgen-->

#### hydrostatic load

Hydrostatic load refers to load caused by {{[water](water.md)}}. The load can be caused by {{pure water itself, or water in a material such as soil}}. <!--SR:!2024-06-02,14,290!2024-06-01,13,290-->

For example, when there is {{water buildup in the soil}}, there is {{increased hydrostatic pressure on retaining walls}}. For pure water, examples include a {{[dam](dam.md), where deeper waters exert more horizontal hydrostatic pressure on the dam}}. <!--SR:!2024-06-03,15,290!2024-06-05,17,300!2024-06-02,14,290-->

#### lateral load

Lateral load may be caused by {{bulk materials, [groundwater](groundwater.md), or [soil](soil.md)}}. <!--SR:!2024-06-05,17,290-->

For example, there is lateral soil load on {{retaining walls of a slope because the soil of a slope on the retained side tends to slip down, pushing the walls towards the excavated side}}. This lateral soil load can cause {{lateral deflection, toppling of the retaining structure, or even a landslide}}. <!--SR:!2024-06-06,18,300!2024-06-01,13,280-->

To protect against soil loads, {{retaining structures are built and weep holes may be installed}}. Alternatively, {{slopes on natural terrain can become man-made slopes, such as cut slopes, fill slopes, or retaining walls}}. <!--SR:!2024-05-30,11,280!2024-05-30,11,280-->

#### seismic load

Seismic load are {{caused by [earthquakes](earthquake.md)}}. It can induce {{both horizontal and vertical load on structures}}. <!--SR:!2024-05-31,12,270!2024-05-30,11,280-->

The consequences are {{partial or complete collapse of structural elements or entire buildings}}. <!--SR:!2024-06-06,17,290-->

#### thermal load

Thermal load refers to load {{caused by [temperature](temperature.md) changes leading to [thermal expansion](thermal%20expansion.md) (contraction) of structural and non-structural members}}. <!--SR:!2024-05-31,12,288-->

For example, {{a beam in between two fixed support creates thermal load under heating as the beam expands}}. A solution would be {{making the beam a simply supported beam instead, with one side a pinned support and the other side a roller support}}. Then when thermal expansion occurs, {{the beam can expand in the direction of the roller support, relieving the thermal load}}. <!--SR:!2024-06-07,18,308!2024-06-05,17,290!2024-06-03,15,300-->

#### wind load

[Wind](wind.md) is {{movement of air}}. When wind moves past a building, {{wind changes in velocity}}. Then, {{the pressure of air changes}}. Positive pressure outside {{causes inward forces while negative causes outward (uplift for roof) forces}}. This is wind load. It also depends on {{building shape, wind direction, and wind speed}}. <!--SR:!2024-06-06,18,300!2024-05-31,12,270!2024-06-02,14,300!2024-06-06,18,300!2024-05-29,10,280-->

Wind load causes {{lateral deflection, which may further lead to toppling of the structure, such as collapse of bridges}}. Less serious consequences include {{damage to individual structural elements such as roofs, walls, and windows; and causes excessive building vibrations}}. <!--SR:!2024-06-04,16,300!2024-06-05,17,300-->

### other loads

### load combinations

{{Load (amplifying) factors}} are used in {{design equations to increase the design loads}}, to {{account for uncertainties involved when estimating loads}}. An example is {{_U_ = 1.2 _D_ + 1.6 _L_, where _D_ is the dead load and _L_ is the live load}}. <!--SR:!2024-06-03,15,290!2024-06-02,14,290!2024-05-30,11,280!2024-06-01,13,280-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/structural_load) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
