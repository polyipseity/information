---
aliases:
  - DOF
  - degree of freedom
  - degrees of freedom
  - degrees of freedom (physics and chemistry)
tags:
  - flashcard/active/general/eng/degrees_of_freedom__physics_and_chemistry_
  - language/in/English
---

# degrees of freedom (physics and chemistry)

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## thermodynamic degrees of freedom for gases

### table

```Python
# pytextgen generate data
# import ../../../tools/utility.py.md
from asyncio import gather as _gather
from itertools import chain as _chain
headers = ("type", "[monoatomic](monoatomic%20gas.md)", "[linear molecules](linear%20molecular%20geometry.md)", "[non-linear molecules](molecular%20geometry.md)",)
table = (
  ("[translation](translation%20(geometry).md) ($x, y, z$)", "3", "3", "3",),
  ("[rotation](rotation.md) ($x, y, z$, < 100 [K](Kelvin.md))", "0", "2", "3",),
  ("[vibration](vibration.md) (10<sup>3</sup>~10<sup>4</sup> [K](Kelvin.md))", "0", "$2(3N - 5)$", "$2(3N - 6)$",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects("dee2", None,),
    headers, table,
  ),
  memorize_map(
    __env__.cwf_sects(None, "2bba", "baa2",),
    items_to_map(*((row[0], ", ".join(f"{headers[ii]}: {row[ii]}" for ii in range(1, 4)),) for row in table)),
  ),
))
```

<!--pytextgen generate section="dee2"--><!-- The following content is generated at 2023-12-17T18:44:27.093167+08:00. Any edits will be overridden! -->

> | type | [monoatomic](monoatomic%20gas.md) | [linear molecules](linear%20molecular%20geometry.md) | [non-linear molecules](molecular%20geometry.md) |
> |-|-|-|-|
> | [translation](translation%20(geometry).md) ($x, y, z$) | 3 | 3 | 3 |
> | [rotation](rotation.md) ($x, y, z$, < 100 [K](Kelvin.md)) | 0 | 2 | 3 |
> | [vibration](vibration.md) (10<sup>3</sup>~10<sup>4</sup> [K](Kelvin.md)) | 0 | $2(3N - 5)$ | $2(3N - 6)$ |

<!--/pytextgen-->

<!--pytextgen generate section="2bba"--><!-- The following content is generated at 2024-01-04T20:17:51.551995+08:00. Any edits will be overridden! -->

- [translation](translation%20(geometry).md) ($x, y, z$):@:[monoatomic](monoatomic%20gas.md): 3, [linear molecules](linear%20molecular%20geometry.md): 3, [non-linear molecules](molecular%20geometry.md): 3 <!--SR:!2027-08-21,964,330-->
- [rotation](rotation.md) ($x, y, z$, < 100 [K](Kelvin.md)):@:[monoatomic](monoatomic%20gas.md): 0, [linear molecules](linear%20molecular%20geometry.md): 2, [non-linear molecules](molecular%20geometry.md): 3 <!--SR:!2027-05-24,973,350-->
- [vibration](vibration.md) (10<sup>3</sup>~10<sup>4</sup> [K](Kelvin.md)):@:[monoatomic](monoatomic%20gas.md): 0, [linear molecules](linear%20molecular%20geometry.md): $2(3N - 5)$, [non-linear molecules](molecular%20geometry.md): $2(3N - 6)$ <!--SR:!2026-07-01,622,290-->

<!--/pytextgen-->

<!--pytextgen generate section="baa2"--><!-- The following content is generated at 2024-01-04T20:17:51.576010+08:00. Any edits will be overridden! -->

- [monoatomic](monoatomic%20gas.md): 3, [linear molecules](linear%20molecular%20geometry.md): 3, [non-linear molecules](molecular%20geometry.md): 3:@:[translation](translation%20(geometry).md) ($x, y, z$) <!--SR:!2027-08-03,1027,350-->
- [monoatomic](monoatomic%20gas.md): 0, [linear molecules](linear%20molecular%20geometry.md): 2, [non-linear molecules](molecular%20geometry.md): 3:@:[rotation](rotation.md) ($x, y, z$, < 100 [K](Kelvin.md)) <!--SR:!2027-02-14,878,330-->
- [monoatomic](monoatomic%20gas.md): 0, [linear molecules](linear%20molecular%20geometry.md): $2(3N - 5)$, [non-linear molecules](molecular%20geometry.md): $2(3N - 6)$:@:[vibration](vibration.md) (10<sup>3</sup>~10<sup>4</sup> [K](Kelvin.md)) <!--SR:!2025-01-31,277,290-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/degrees_of_freedom_(physics_and_chemistry)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
