---
aliases:
  - DOF
  - degree of freedom
  - degrees of freedom
  - degrees of freedom (physics and chemistry)
tags:
  - flashcards/general/degrees_of_freedom__physics_and_chemistry_
  - languages/in/English
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# degrees of freedom (physics and chemistry)

## thermodynamic degrees of freedom for gases

### table

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
# import ../../tools/utility.py.md
from asyncio import gather as _gather
from itertools import chain as _chain

e = __env__
header = ("type", "[monoatomic](monoatomic%20gas.md)", "[linear molecules](linear%20molecular%20geometry.md)", "[non-linear molecules](molecular%20geometry.md)",)
table = (
  ("[translation](translation%20(geometry).md) ($x, y, z$)", "3", "3", "3",),
  ("[rotation](rotation.md) ($x, y, z$, < 100 [K](Kelvin.md))", "0", "2", "3",),
  ("[vibration](vibration.md) (10<sup>3</sup>~10<sup>4</sup> [K](Kelvin.md))", "0", "$2(3N - 5)$", "$2(3N - 6)$",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    e.cwf_sects("dee2", None,),
    header, table,
  ),
  memorize_map(
    e.cwf_sects(None, "2bba", "baa2",),
    items_to_map(*((row[0], ", ".join(f"{header[ii]}: {row[ii]}" for ii in range(1, 4)),) for row in table)),
  ),
))
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="dee2"--><!-- The following content is generated at 2023-12-17T18:44:27.093167+08:00. Any edits will be overridden! -->

> | type | [monoatomic](monoatomic%20gas.md) | [linear molecules](linear%20molecular%20geometry.md) | [non-linear molecules](molecular%20geometry.md) |
> |-|-|-|-|
> | [translation](translation%20(geometry).md) ($x, y, z$) | 3 | 3 | 3 |
> | [rotation](rotation.md) ($x, y, z$, < 100 [K](Kelvin.md)) | 0 | 2 | 3 |
> | [vibration](vibration.md) (10<sup>3</sup>~10<sup>4</sup> [K](Kelvin.md)) | 0 | $2(3N - 5)$ | $2(3N - 6)$ |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2bba"--><!-- The following content is generated at 2023-12-17T18:44:27.039680+08:00. Any edits will be overridden! -->

1. [translation](translation%20(geometry).md) ($x, y, z$)::[monoatomic](monoatomic%20gas.md): 3, [linear molecules](linear%20molecular%20geometry.md): 3, [non-linear molecules](molecular%20geometry.md): 3 <!--SR:!2023-12-21,4,270-->
2. [rotation](rotation.md) ($x, y, z$, < 100 [K](Kelvin.md))::[monoatomic](monoatomic%20gas.md): 0, [linear molecules](linear%20molecular%20geometry.md): 2, [non-linear molecules](molecular%20geometry.md): 3 <!--SR:!2023-12-21,4,270-->
3. [vibration](vibration.md) (10<sup>3</sup>~10<sup>4</sup> [K](Kelvin.md))::[monoatomic](monoatomic%20gas.md): 0, [linear molecules](linear%20molecular%20geometry.md): $2(3N - 5)$, [non-linear molecules](molecular%20geometry.md): $2(3N - 6)$ <!--SR:!2023-12-20,3,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="baa2"--><!-- The following content is generated at 2023-12-17T18:44:27.009934+08:00. Any edits will be overridden! -->

1. [monoatomic](monoatomic%20gas.md): 3, [linear molecules](linear%20molecular%20geometry.md): 3, [non-linear molecules](molecular%20geometry.md): 3::[translation](translation%20(geometry).md) ($x, y, z$) <!--SR:!2023-12-21,4,270-->
2. [monoatomic](monoatomic%20gas.md): 0, [linear molecules](linear%20molecular%20geometry.md): 2, [non-linear molecules](molecular%20geometry.md): 3::[rotation](rotation.md) ($x, y, z$, < 100 [K](Kelvin.md)) <!--SR:!2023-12-21,4,270-->
3. [monoatomic](monoatomic%20gas.md): 0, [linear molecules](linear%20molecular%20geometry.md): $2(3N - 5)$, [non-linear molecules](molecular%20geometry.md): $2(3N - 6)$::[vibration](vibration.md) (10<sup>3</sup>~10<sup>4</sup> [K](Kelvin.md)) <!--SR:!2023-12-20,3,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
