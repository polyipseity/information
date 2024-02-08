---
aliases:
  - conversion of scales of temperature
  - conversions of scales of temperature
tags:
  - flashcards/general/conversion_of_scales_of_temperature
  - languages/in/English
---

# conversion of scales of temperature

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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="33dd"--><!-- The following content is generated at 2024-01-04T20:17:51.562998+08:00. Any edits will be overridden! -->

- [Kelvin](Kelvin.md)::from: x °C ≘ (x + 273.15) K, to: x K ≘ (x − 273.15) °C <!--SR:!2024-02-23,51,310-->
- [Fahrenheit](Fahrenheit.md)::from: x °C ≘ (x × 9/5 + 32) °F, to: x °F ≘ (x − 32) × 5/9 °C <!--SR:!2024-05-02,97,290-->
- [Rankine](Rankine%20scale.md)::from: x °C ≘ (x + 273.15) × 9/5 °R, to: x °R ≘ (x − 491.67) × 5/9 °C <!--SR:!2024-02-15,32,210-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="76bc"--><!-- The following content is generated at 2024-01-04T20:17:51.591589+08:00. Any edits will be overridden! -->

- from: x °C ≘ (x + 273.15) K, to: x K ≘ (x − 273.15) °C::[Kelvin](Kelvin.md) <!--SR:!2024-03-09,64,310-->
- from: x °C ≘ (x × 9/5 + 32) °F, to: x °F ≘ (x − 32) × 5/9 °C::[Fahrenheit](Fahrenheit.md) <!--SR:!2024-02-27,54,310-->
- from: x °C ≘ (x + 273.15) × 9/5 °R, to: x °R ≘ (x − 491.67) × 5/9 °C::[Rankine](Rankine%20scale.md) <!--SR:!2024-03-08,62,310-->

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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="50fb"--><!-- The following content is generated at 2024-01-04T20:17:51.639096+08:00. Any edits will be overridden! -->

- [Celsius](Celsius.md)::from: x K ≘ (x − 273.15) °C, to: x °C ≘ (x + 273.15) K <!--SR:!2024-03-05,59,310-->
- [Fahrenheit](Fahrenheit.md)::from: x K ≘ (x × 9/5 − 459.67) °F, to: x °F ≘ (x + 459.67) × 5/9 K <!--SR:!2024-04-18,70,230-->
- [Rankine](Rankine%20scale.md)::from: x K ≘ x × 9/5 °R, to: x °R ≘ x × 5/9 K <!--SR:!2024-07-02,148,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1234"--><!-- The following content is generated at 2024-01-04T20:17:51.611097+08:00. Any edits will be overridden! -->

- from: x K ≘ (x − 273.15) °C, to: x °C ≘ (x + 273.15) K::[Celsius](Celsius.md) <!--SR:!2024-03-10,63,310-->
- from: x K ≘ (x × 9/5 − 459.67) °F, to: x °F ≘ (x + 459.67) × 5/9 K::[Fahrenheit](Fahrenheit.md) <!--SR:!2024-03-09,63,310-->
- from: x K ≘ x × 9/5 °R, to: x °R ≘ x × 5/9 K::[Rankine](Rankine%20scale.md) <!--SR:!2024-03-15,67,310-->

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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="aad2"--><!-- The following content is generated at 2024-01-04T20:17:51.727638+08:00. Any edits will be overridden! -->

- [Celsius](Celsius.md)::from: x °F ≘ (x − 32) × 5/9 °C, to: x °C ≘ (x × 9/5 + 32) °F <!--SR:!2024-02-20,49,290-->
- [Kelvin](Kelvin.md)::from: x °F ≘ (x + 459.67) × 5/9 K, to: x K ≘ (x × 9/5 − 459.67) °F <!--SR:!2024-02-22,41,250-->
- [Rankine](Rankine%20scale.md)::from: x °F ≘ (x + 459.67) °R, to: x °R ≘ (x − 459.67) °F <!--SR:!2024-02-09,38,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3496"--><!-- The following content is generated at 2024-01-04T20:17:51.695626+08:00. Any edits will be overridden! -->

- from: x °F ≘ (x − 32) × 5/9 °C, to: x °C ≘ (x × 9/5 + 32) °F::[Celsius](Celsius.md) <!--SR:!2024-03-14,67,310-->
- from: x °F ≘ (x + 459.67) × 5/9 K, to: x K ≘ (x × 9/5 − 459.67) °F::[Kelvin](Kelvin.md) <!--SR:!2024-03-07,62,310-->
- from: x °F ≘ (x + 459.67) °R, to: x °R ≘ (x − 459.67) °F::[Rankine](Rankine%20scale.md) <!--SR:!2024-02-15,44,290-->

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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ef82"--><!-- The following content is generated at 2024-01-04T20:17:51.757639+08:00. Any edits will be overridden! -->

- [Celsius](Celsius.md)::from: x °R ≘ (x − 491.67) × 5/9 °C, to: x °C ≘ (x + 273.15) × 9/5 °R <!--SR:!2024-03-23,52,230-->
- [Kelvin](Kelvin.md)::from: x °R ≘ x × 5/9 K, to: x K ≘ x × 9/5 °R <!--SR:!2024-02-27,53,310-->
- [Fahrenheit](Fahrenheit.md)::from: x °R ≘ (x − 459.67) °F, to: x °F ≘ (x + 459.67) °R <!--SR:!2024-03-11,34,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="35a1"--><!-- The following content is generated at 2024-01-04T20:17:51.833127+08:00. Any edits will be overridden! -->

- from: x °R ≘ (x − 491.67) × 5/9 °C, to: x °C ≘ (x + 273.15) × 9/5 °R::[Celsius](Celsius.md) <!--SR:!2024-03-07,61,310-->
- from: x °R ≘ x × 5/9 K, to: x K ≘ x × 9/5 °R::[Kelvin](Kelvin.md) <!--SR:!2024-03-06,61,310-->
- from: x °R ≘ (x − 459.67) °F, to: x °F ≘ (x + 459.67) °R::[Fahrenheit](Fahrenheit.md) <!--SR:!2024-02-24,51,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/conversion_of_scales_of_temperature) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
