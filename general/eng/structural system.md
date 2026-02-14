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
# import ../../tools/utility.py.md
```

## high-rise buildings

Buildings can be {@{categorized by height}@}: {@{single-storey, multi-storey with height less than 24 m}@}, {@{high-rise with height more than 24 m but less than 100 m}@}, {@{tall, and supertall}@}.

The structural system of a building only {@{consists of members designed to carry loads}@}, and all others are {@{non-structural}@}.

The structural system of a high-rise building should support {@{vertical loads such as gravity and foundation settlement, and also lateral loads such as earthquake, wind}@}. The latter, {@{lateral loads, are especially important for tall buildings}@}. Otherwise, tall buildings may {@{slide (horizontal translation) or overturn (rotation about the base)}@}. Generally the higher up, {@{the larger the load}@}.

Hence, foundation-wise, low-rise buildings are {@{supported by shallow foundations (footings)}@}, while high-rise buildings are {@{supported by deep foundations (pipes), which may even reach the bedrock}@}.

The structural system affects {@{the load distribution}@}. For example, a {@{structural steel undergoing overturning due to wind}@} would experience {@{tension at the wind-facing side and compression on the other side}@}. A {@{reinforced concrete (concrete with steel bars)}@} would experience the same thing, but {@{steel bars bear most of the tension while concrete bears most of the compression and the heavy vertical loading}@}.

We can {@{quantify}@} overturning. The {@{lateral stiffness}@} of a building is defined as {@{the force divided by the horizontal displacement at the building top, and has a unit of kN/mm}@}, somewhat similar to {@{[elastic modulus](elastic%20modulus.md)}@}. The aim is to {@{increase the lateral stiffness, which involves making the building stiff and strong}@}.

### classification

For high-rise buildings, the structural system can be broadly categorized into {@{exterior and interior structures}@}.

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

- _(begin)_→::@::←[braced frame](braced%20frame.md)
- [braced frame](braced%20frame.md)→::@::←[hinged frame](hinged%20frame.md)
- [hinged frame](hinged%20frame.md)→::@::←[outrigger](#outrigger)
- [outrigger](#outrigger)→::@::←[rigid frame](rigid%20frame.md)
- [rigid frame](rigid%20frame.md)→::@::←[shear-walled frame](#sheared-walled%20frame): [rigid frame](rigid%20frame.md) + [shear wall](shear%20wall.md)
- [shear-walled frame](#sheared-walled%20frame): [rigid frame](rigid%20frame.md) + [shear wall](shear%20wall.md)→::@::←_(end)_

<!--/pytextgen-->

##### outrigger

- see [outrigger](outrigger.md)

Intuitively, if a high-rise building is {@{a skier}@}, then {@{the building core is the human body, the outriggers are the arms, and the building exterior are the ski poles}@}.

Outriggers can {@{reduce the overturning moment in the core by transferring some moment to columns outside the core}@}.

For example, outriggers are used in {@{the [International Commerce Center](International%20Commerce%20Center.md)}@}. The building has {@{4 outriggers in 4 separate floors}@}. In each outrigger, {@{8 outriggers connect the core to the mega columns of the exterior structure, forming a hash (#) shape}@}.

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

- _(begin)_→::@::←[buttress](buttress.md)
- [buttress](buttress.md)→::@::←[diagrid](diagrid.md)
- [diagrid](diagrid.md)→::@::←[exoskeleton](exoskeleton.md)
- [exoskeleton](exoskeleton.md)→::@::←[space truss](space%20frame.md)
- [space truss](space%20frame.md)→::@::←[superframe](superframe.md)
- [superframe](superframe.md)→::@::←[tube](tube%20(structure).md)
- [tube](tube%20(structure).md)→::@::←_(end)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/structural_system) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
