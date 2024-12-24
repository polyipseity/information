---
aliases:
  - bending
  - mechanical bending
tags:
  - flashcard/active/general/bending
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

There are {@{<!--pytextgen generate section="298b"--><!-- The following content is generated at 2024-05-14T01:07:43.943498+08:00. Any edits will be overridden! -->3<!--/pytextgen--> forms of internal stresses}@} caused by lateral loads ([force](force.md) on the side):

<!--pytextgen generate section="98ba"--><!-- The following content is generated at 2024-05-14T01:07:43.913119+08:00. Any edits will be overridden! -->

> 1. [compressive stress](compression%20(physics).md): the side being shortened by the bending
> 2. [shear stress](shear%20stress.md): mostly parallel and some complementary perpendicular to the load direction
> 3. [tensile stress](tension%20(physics).md): the side being lengthened by the bending

<!--/pytextgen-->

<!--pytextgen generate section="cc19"--><!-- The following content is generated at 2024-05-14T01:07:43.929852+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[compressive stress](compression%20(physics).md): the side being shortened by the bending
- [compressive stress](compression%20(physics).md): the side being shortened by the bending→::@::←[shear stress](shear%20stress.md): mostly parallel and some complementary perpendicular to the load direction
- [shear stress](shear%20stress.md): mostly parallel and some complementary perpendicular to the load direction→::@::←[tensile stress](tension%20(physics).md): the side being lengthened by the bending
- [tensile stress](tension%20(physics).md): the side being lengthened by the bending→::@::←_(end)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/bending) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
