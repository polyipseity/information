---
aliases:
  - conversion of scales of temperature
  - conversions of scales of temperature
tags:
  - flashcards/general/conversion_of_scales_of_temperature
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
from asyncio import gather as _gather
from itertools import chain as _chain
from pytextgen.util import Location as _Loc, NULL_LOCATION as _NULL_LOC

header = ("[temperature scale](temperature%20scale.md)", "from", "to",)
t_celsius = "[Celsius](Celsius.md)"
t_fahrenheit = "[Fahrenheit](Fahrenheit.md)"
t_kelvin = "[Kelvin](Kelvin.md)"
t_rankine = "[Rankine](Rankine%20scale.md)"

async def conversion_table(
  locations: tuple[_Loc, _Loc, _Loc],
  *table: tuple[str, str, str],
):
  return _chain.from_iterable(await _gather(
    memorize_table(
      (locations[0], _NULL_LOC,),
      header, table,
    ),
    memorize_map(
      (_NULL_LOC, *locations[1:3],),
      items_to_map(*((row[0], ", ".join(f"{header[ii]}: {row[ii]}" for ii in range(1, 3)),) for row in table)),
    ),
  ))

return {
  conversion_table.__name__: conversion_table,
  "t_celsius": t_celsius,
  "t_fahrenheit": t_fahrenheit,
  "t_kelvin": t_kelvin,
  "t_rankine": t_rankine,
}
```
%%

# conversion of scales of temperature

## Celsius scale

- see: [Celsius](Celsius.md)

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await conversion_table(
  e.cwf_sects("5ffa", "33dd", "76bc",),
  (t_kelvin, "x °C ≘ (x + 273.15) K", "x K ≘ (x − 273.15) °C",),
  (t_fahrenheit, "x °C ≘ (x × 9/5 + 32) °F", "x °F ≘ (x − 32) × 5/9 °C",),
  (t_rankine, "x °C ≘ (x + 273.15) × 9/5 °R", "x °R ≘ (x − 491.67) × 5/9 °C",),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5ffa"--><!-- The following content is generated at 2023-12-17T17:08:50.524420+08:00. Any edits will be overridden! -->

> | [temperature scale](temperature%20scale.md) | from | to |
> |-|-|-|
> | [Kelvin](Kelvin.md) | x °C ≘ (x + 273.15) K | x K ≘ (x − 273.15) °C |
> | [Fahrenheit](Fahrenheit.md) | x °C ≘ (x × 9/5 + 32) °F | x °F ≘ (x − 32) × 5/9 °C |
> | [Rankine](Rankine%20scale.md) | x °C ≘ (x + 273.15) × 9/5 °R | x °R ≘ (x − 491.67) × 5/9 °C |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="33dd"--><!-- The following content is generated at 2023-12-17T17:08:50.586837+08:00. Any edits will be overridden! -->

1. [Kelvin](Kelvin.md)::from: x °C ≘ (x + 273.15) K, to: x K ≘ (x − 273.15) °C
2. [Fahrenheit](Fahrenheit.md)::from: x °C ≘ (x × 9/5 + 32) °F, to: x °F ≘ (x − 32) × 5/9 °C
3. [Rankine](Rankine%20scale.md)::from: x °C ≘ (x + 273.15) × 9/5 °R, to: x °R ≘ (x − 491.67) × 5/9 °C

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="76bc"--><!-- The following content is generated at 2023-12-17T17:08:50.461280+08:00. Any edits will be overridden! -->

1. from: x °C ≘ (x + 273.15) K, to: x K ≘ (x − 273.15) °C::[Kelvin](Kelvin.md)
2. from: x °C ≘ (x × 9/5 + 32) °F, to: x °F ≘ (x − 32) × 5/9 °C::[Fahrenheit](Fahrenheit.md)
3. from: x °C ≘ (x + 273.15) × 9/5 °R, to: x °R ≘ (x − 491.67) × 5/9 °C::[Rankine](Rankine%20scale.md)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## Kelvin scale

- see: [Kelvin](Kelvin.md)

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await conversion_table(
  e.cwf_sects("955a", "50fb", "1234",),
  (t_celsius, "x K ≘ (x − 273.15) °C", "x °C ≘ (x + 273.15) K",),
  (t_fahrenheit, "x K ≘ (x × 9/5 − 459.67) °F", "x °F ≘ (x + 459.67) × 5/9 K",),
  (t_rankine, "x K ≘ x × 9/5 °R", "x °R ≘ x × 5/9 K",),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="955a"--><!-- The following content is generated at 2023-12-17T17:08:50.664363+08:00. Any edits will be overridden! -->

> | [temperature scale](temperature%20scale.md) | from | to |
> |-|-|-|
> | [Celsius](Celsius.md) | x K ≘ (x − 273.15) °C | x °C ≘ (x + 273.15) K |
> | [Fahrenheit](Fahrenheit.md) | x K ≘ (x × 9/5 − 459.67) °F | x °F ≘ (x + 459.67) × 5/9 K |
> | [Rankine](Rankine%20scale.md) | x K ≘ x × 9/5 °R | x °R ≘ x × 5/9 K |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="50fb"--><!-- The following content is generated at 2023-12-17T17:08:50.611405+08:00. Any edits will be overridden! -->

1. [Celsius](Celsius.md)::from: x K ≘ (x − 273.15) °C, to: x °C ≘ (x + 273.15) K
2. [Fahrenheit](Fahrenheit.md)::from: x K ≘ (x × 9/5 − 459.67) °F, to: x °F ≘ (x + 459.67) × 5/9 K
3. [Rankine](Rankine%20scale.md)::from: x K ≘ x × 9/5 °R, to: x °R ≘ x × 5/9 K

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1234"--><!-- The following content is generated at 2023-12-17T17:08:50.642031+08:00. Any edits will be overridden! -->

1. from: x K ≘ (x − 273.15) °C, to: x °C ≘ (x + 273.15) K::[Celsius](Celsius.md)
2. from: x K ≘ (x × 9/5 − 459.67) °F, to: x °F ≘ (x + 459.67) × 5/9 K::[Fahrenheit](Fahrenheit.md)
3. from: x K ≘ x × 9/5 °R, to: x °R ≘ x × 5/9 K::[Rankine](Rankine%20scale.md)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## Fahrenheit scale

- see: [Fahrenheit](Fahrenheit.md)

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await conversion_table(
  e.cwf_sects("46ab", "aad2", "3496",),
  (t_celsius, "x °F ≘ (x − 32) × 5/9 °C", "x °C ≘ (x × 9/5 + 32) °F",),
  (t_kelvin, "x °F ≘ (x + 459.67) × 5/9 K", "x K ≘ (x × 9/5 − 459.67) °F",),
  (t_rankine, "x °F ≘ (x + 459.67) °R", "x °R ≘ (x − 459.67) °F",),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="46ab"--><!-- The following content is generated at 2023-12-17T17:08:50.710874+08:00. Any edits will be overridden! -->

> | [temperature scale](temperature%20scale.md) | from | to |
> |-|-|-|
> | [Celsius](Celsius.md) | x °F ≘ (x − 32) × 5/9 °C | x °C ≘ (x × 9/5 + 32) °F |
> | [Kelvin](Kelvin.md) | x °F ≘ (x + 459.67) × 5/9 K | x K ≘ (x × 9/5 − 459.67) °F |
> | [Rankine](Rankine%20scale.md) | x °F ≘ (x + 459.67) °R | x °R ≘ (x − 459.67) °F |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="aad2"--><!-- The following content is generated at 2023-12-17T17:08:50.683509+08:00. Any edits will be overridden! -->

1. [Celsius](Celsius.md)::from: x °F ≘ (x − 32) × 5/9 °C, to: x °C ≘ (x × 9/5 + 32) °F
2. [Kelvin](Kelvin.md)::from: x °F ≘ (x + 459.67) × 5/9 K, to: x K ≘ (x × 9/5 − 459.67) °F
3. [Rankine](Rankine%20scale.md)::from: x °F ≘ (x + 459.67) °R, to: x °R ≘ (x − 459.67) °F

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3496"--><!-- The following content is generated at 2023-12-17T17:08:50.733168+08:00. Any edits will be overridden! -->

1. from: x °F ≘ (x − 32) × 5/9 °C, to: x °C ≘ (x × 9/5 + 32) °F::[Celsius](Celsius.md)
2. from: x °F ≘ (x + 459.67) × 5/9 K, to: x K ≘ (x × 9/5 − 459.67) °F::[Kelvin](Kelvin.md)
3. from: x °F ≘ (x + 459.67) °R, to: x °R ≘ (x − 459.67) °F::[Rankine](Rankine%20scale.md)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## Rankine scale

- see: [Rankine scale](Rankine%20scale.md)

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await conversion_table(
  e.cwf_sects("b0a9", "ef82", "35a1",),
  (t_celsius, "x °R ≘ (x − 491.67) × 5/9 °C", "x °C ≘ (x + 273.15) × 9/5 °R",),
  (t_kelvin, "x °R ≘ x × 5/9 K", "x K ≘ x × 9/5 °R",),
  (t_fahrenheit, "x °R ≘ (x − 459.67) °F", "x °F ≘ (x + 459.67) °R",),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b0a9"--><!-- The following content is generated at 2023-12-17T17:08:50.748638+08:00. Any edits will be overridden! -->

> | [temperature scale](temperature%20scale.md) | from | to |
> |-|-|-|
> | [Celsius](Celsius.md) | x °R ≘ (x − 491.67) × 5/9 °C | x °C ≘ (x + 273.15) × 9/5 °R |
> | [Kelvin](Kelvin.md) | x °R ≘ x × 5/9 K | x K ≘ x × 9/5 °R |
> | [Fahrenheit](Fahrenheit.md) | x °R ≘ (x − 459.67) °F | x °F ≘ (x + 459.67) °R |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ef82"--><!-- The following content is generated at 2023-12-17T17:08:50.765666+08:00. Any edits will be overridden! -->

1. [Celsius](Celsius.md)::from: x °R ≘ (x − 491.67) × 5/9 °C, to: x °C ≘ (x + 273.15) × 9/5 °R
2. [Kelvin](Kelvin.md)::from: x °R ≘ x × 5/9 K, to: x K ≘ x × 9/5 °R
3. [Fahrenheit](Fahrenheit.md)::from: x °R ≘ (x − 459.67) °F, to: x °F ≘ (x + 459.67) °R

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="35a1"--><!-- The following content is generated at 2023-12-17T17:08:50.779184+08:00. Any edits will be overridden! -->

1. from: x °R ≘ (x − 491.67) × 5/9 °C, to: x °C ≘ (x + 273.15) × 9/5 °R::[Celsius](Celsius.md)
2. from: x °R ≘ x × 5/9 K, to: x K ≘ x × 9/5 °R::[Kelvin](Kelvin.md)
3. from: x °R ≘ (x − 459.67) °F, to: x °F ≘ (x + 459.67) °R::[Fahrenheit](Fahrenheit.md)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->