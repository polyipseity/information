---
aliases:
  - structural system
  - structural systems
tags:
  - flashcard/active/general/eng/structural_system
  - language/in/English
---

# structural system

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## high-rise buildings

Buildings can be {@{categorized by height}@}: {@{single-storey, multi-storey with height less than 24 m, high-rise with height more than 24 m but less than 100 m, tall, and supertall}@}. <!--SR:!2026-08-02,617,335!2025-12-13,384,295-->

The structural system of a building only {@{consists of members designed to carry loads}@}, and all others are {@{non-structural}@}. <!--SR:!2026-03-26,496,310!2025-04-17,259,335-->

The structural system of a high-rise building should support {@{vertical loads such as gravity and foundation settlement, and also lateral loads such as earthquake, wind}@}. The latter, {@{lateral loads, are especially important for tall buildings}@}. Otherwise, tall buildings may {@{slide (horizontal translation) or overturn (rotation about the base)}@}. Generally the higher up, {@{the larger the load}@}. <!--SR:!2025-05-19,259,290!2026-05-23,543,315!2027-03-24,798,335!2025-03-04,204,310-->

Hence, foundation-wise, low-rise buildings are {@{supported by shallow foundations (footings)}@}, while high-rise buildings are {@{supported by deep foundations (pipes), which may even reach the bedrock}@}. <!--SR:!2025-02-07,195,315!2026-04-25,520,315-->

The structural system affects {@{the load distribution}@}. For example, a {@{structural steel undergoing overturning due to wind}@} would experience {@{tension at the wind-facing side and compression on the other side}@}. A {@{reinforced concrete (concrete with steel bars)}@} would experience the same thing, but {@{steel bars bear most of the tension while concrete bears most of the compression and the heavy vertical loading}@}. <!--SR:!2025-02-05,188,315!2026-06-10,553,315!2025-06-07,297,335!2026-05-27,547,315!2025-05-10,230,275-->

We can {@{quantify}@} overturning. The {@{lateral stiffness}@} of a building is defined as {@{the force divided by the horizontal displacement at the building top, and has a unit of kN/mm}@}, somewhat similar to {@{[elastic modulus](elastic%20modulus.md)}@}. The aim is to {@{increase the lateral stiffness, which involves making the building stiff and strong}@}. <!--SR:!2025-04-19,259,335!2025-04-18,258,335!2026-03-01,439,295!2027-03-06,782,335!2025-05-17,282,335-->

### classification

For high-rise buildings, the structural system can be broadly categorized into {@{exterior and interior structures}@}. <!--SR:!2025-06-03,295,335-->

#### interior structures

```Python
# pytextgen generate data
items = R"""
[braced frame](braced%20frame.md)
[hinged frame](hinged%20frame.md)
[outrigger](#outrigger)
[rigid frame](rigid%20frame.md)
[shear-walled frame](#sheared-walled%20frame): [rigid frame](rigid%20frame.md) + [shear wall](shear%20wall.md)
""".strip().splitlines()
return await memorize_seq(
  __env__.cwf_sects("ed23", "ab92"),
  items,
)
```

The following interior structures are possible.

<!--pytextgen generate section="ed23"--><!-- The following content is generated at 2024-05-14T21:11:05.334113+08:00. Any edits will be overridden! -->

> 1. [braced frame](braced%20frame.md)
> 2. [hinged frame](hinged%20frame.md)
> 3. [outrigger](#outrigger)
> 4. [rigid frame](rigid%20frame.md)
> 5. [shear-walled frame](#sheared-walled%20frame): [rigid frame](rigid%20frame.md) + [shear wall](shear%20wall.md)

<!--/pytextgen-->

<!--pytextgen generate section="ab92"--><!-- The following content is generated at 2024-05-14T21:11:05.318372+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[braced frame](braced%20frame.md) <!--SR:!2025-03-13,161,270!2027-02-04,749,335-->
- [braced frame](braced%20frame.md)→::@::←[hinged frame](hinged%20frame.md) <!--SR:!2025-10-02,259,235!2025-01-22,106,235-->
- [hinged frame](hinged%20frame.md)→::@::←[outrigger](#outrigger) <!--SR:!2025-02-23,68,150!2025-01-21,45,175-->
- [outrigger](#outrigger)→::@::←[rigid frame](rigid%20frame.md) <!--SR:!2025-05-25,238,275!2025-05-20,138,195-->
- [rigid frame](rigid%20frame.md)→::@::←[shear-walled frame](#sheared-walled%20frame): [rigid frame](rigid%20frame.md) + [shear wall](shear%20wall.md) <!--SR:!2025-11-02,328,255!2025-08-02,273,255-->
- [shear-walled frame](#sheared-walled%20frame): [rigid frame](rigid%20frame.md) + [shear wall](shear%20wall.md)→::@::←_(end)_ <!--SR:!2025-01-27,181,315!2025-03-17,170,255-->

<!--/pytextgen-->

##### outrigger

- see [outrigger](outrigger.md)

Intuitively, if a high-rise building is {@{a skier}@}, then {@{the building core is the human body, the outriggers are the arms, and the building exterior are the ski poles}@}. <!--SR:!2025-01-29,191,315!2025-04-25,265,335-->

Outriggers can {@{reduce the overturning moment in the core by transferring some moment to columns outside the core}@}. <!--SR:!2025-07-03,297,295-->

For example, outriggers are used in {@{the [International Commerce Center](International%20Commerce%20Center.md)}@}. The building has {@{4 outriggers in 4 separate floors}@}. In each outrigger, {@{8 outriggers connect the core to the mega columns of the exterior structure, forming a hash (#) shape}@}. <!--SR:!2025-03-15,213,310!2026-02-18,431,295!2025-02-11,199,315-->

#### exterior structures

The following exterior structures are possible.

```Python
# pytextgen generate data
items = R"""
[buttress](buttress.md)
[diagrid](diagrid.md)
[exoskeleton](exoskeleton.md)
[space truss](space%20frame.md)
[superframe](superframe.md)
[tube](tube%20(structure).md)
""".strip().splitlines()
return await memorize_seq(
  __env__.cwf_sects("ffe2", "7123"),
  items,
)
```

<!--pytextgen generate section="ffe2"--><!-- The following content is generated at 2024-05-14T21:11:05.355104+08:00. Any edits will be overridden! -->

> 1. [buttress](buttress.md)
> 2. [diagrid](diagrid.md)
> 3. [exoskeleton](exoskeleton.md)
> 4. [space truss](space%20frame.md)
> 5. [superframe](superframe.md)
> 6. [tube](tube%20(structure).md)

<!--/pytextgen-->

<!--pytextgen generate section="7123"--><!-- The following content is generated at 2024-05-14T21:11:05.350734+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[buttress](buttress.md) <!--SR:!2027-03-13,786,335!2025-03-18,216,315-->
- [buttress](buttress.md)→::@::←[diagrid](diagrid.md) <!--SR:!2025-07-03,224,235!2026-03-05,417,315-->
- [diagrid](diagrid.md)→::@::←[exoskeleton](exoskeleton.md) <!--SR:!2025-04-14,215,275!2025-07-19,242,295-->
- [exoskeleton](exoskeleton.md)→::@::←[space truss](space%20frame.md) <!--SR:!2025-12-30,361,255!2025-04-12,159,235-->
- [space truss](space%20frame.md)→::@::←[superframe](superframe.md) <!--SR:!2026-02-12,422,295!2025-05-07,216,275-->
- [superframe](superframe.md)→::@::←[tube](tube%20(structure).md) <!--SR:!2025-02-14,148,275!2025-01-19,84,195-->
- [tube](tube%20(structure).md)→::@::←_(end)_ <!--SR:!2025-03-24,220,315!2025-03-17,215,315-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/structural_system) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
