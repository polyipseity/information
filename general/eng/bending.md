---
aliases:
  - bending
  - mechanical bending
tags:
  - flashcard/active/general/eng/bending
  - language/in/English
---

# bending

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## quasi-static bending of beams

```Python
# pytextgen generate data
from asyncio import gather
from pytextgen.util import Result

items = R"""
[compressive stress](compression%20(physics).md): the side being shortened by the bending
[shear stress](shear%20stress.md): mostly parallel and some complementary perpendicular to the load direction
[tensile stress](tension%20(physics).md): the side being lengthened by the bending
""".strip().splitlines()
return (
  Result(
    location=__env__.cwf_sect("298b"),
    text=str(len(items)),
  ),
  *await memorize_seq(
    __env__.cwf_sects("98ba", "cc19"),
    items,
  ),
)
```

There are {@{<!--pytextgen generate section="298b"--><!-- The following content is generated at 2024-05-14T01:07:43.943498+08:00. Any edits will be overridden! -->3<!--/pytextgen--> forms of internal stresses}@} caused by lateral loads ([force](force.md) on the side): <!--SR:!2028-07-18,1184,350-->

<!--pytextgen generate section="98ba"--><!-- The following content is generated at 2024-05-14T01:07:43.913119+08:00. Any edits will be overridden! -->

> 1. [compressive stress](compression%20(physics).md): the side being shortened by the bending
> 2. [shear stress](shear%20stress.md): mostly parallel and some complementary perpendicular to the load direction
> 3. [tensile stress](tension%20(physics).md): the side being lengthened by the bending

<!--/pytextgen-->

<!--pytextgen generate section="cc19"--><!-- The following content is generated at 2024-05-14T01:07:43.929852+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[compressive stress](compression%20(physics).md): the side being shortened by the bending <!--SR:!2027-02-08,714,330!2025-05-23,286,330-->
- [compressive stress](compression%20(physics).md): the side being shortened by the bending→::@::←[shear stress](shear%20stress.md): mostly parallel and some complementary perpendicular to the load direction <!--SR:!2025-12-02,377,290!2026-12-02,649,310-->
- [shear stress](shear%20stress.md): mostly parallel and some complementary perpendicular to the load direction→::@::←[tensile stress](tension%20(physics).md): the side being lengthened by the bending <!--SR:!2026-11-10,623,310!2025-06-18,253,270-->
- [tensile stress](tension%20(physics).md): the side being lengthened by the bending→::@::←_(end)_ <!--SR:!2028-06-22,1165,350!2027-10-26,947,330-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/bending) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
