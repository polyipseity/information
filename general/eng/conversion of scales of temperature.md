---
aliases:
  - conversion of scales of temperature
  - conversions of scales of temperature
tags:
  - flashcard/active/general/eng/conversion_of_scales_of_temperature
  - language/in/English
---

# conversion of scales of temperature

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
from asyncio import gather as _gather
from itertools import chain as _chain
from pytextgen.util import Location as _Loc, NULL_LOCATION as _NULL_LOC

headers = ("[temperature scale](temperature%20scale.md)", "from {}", "to {}",)
t_celsius = "[Celsius](Celsius.md)"
t_fahrenheit = "[Fahrenheit](Fahrenheit.md)"
t_kelvin = "[Kelvin](Kelvin.md)"
t_rankine = "[Rankine](Rankine%20scale.md)"

async def conversion_table(
  temperature: str,
  locations: tuple[_Loc, _Loc, _Loc],
  *table: tuple[str, str, str],
):
  this_headers = tuple(header.format(temperature) for header in headers)
  return _chain.from_iterable(await _gather(
    memorize_table(
      (locations[0], _NULL_LOC,),
      this_headers, table,
    ),
    memorize_map(
      (_NULL_LOC, *locations[1:3],),
      items_to_map(*((row[0], ", ".join(f"{this_headers[ii]}: {row[ii]}" for ii in range(1, 3)),) for row in table)),
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

## Celsius scale

- see: [Celsius](Celsius.md)

```Python
# pytextgen generate data
return await conversion_table(
  t_celsius,
  __env__.cwf_sects("5ffa", "33dd", "76bc",),
  (t_kelvin, "x °C ≘ (x + 273.15) K", "x K ≘ (x − 273.15) °C",),
  (t_fahrenheit, "x °C ≘ (x × 9/5 + 32) °F", "x °F ≘ (x − 32) × 5/9 °C",),
  (t_rankine, "x °C ≘ (x + 273.15) × 9/5 °R", "x °R ≘ (x − 491.67) × 5/9 °C",),
)
```

<!--pytextgen generate section="5ffa"--><!-- The following content is generated at 2024-03-07T00:32:24.791478+08:00. Any edits will be overridden! -->

> | [temperature scale](temperature%20scale.md) | from [Celsius](Celsius.md) | to [Celsius](Celsius.md) |
> |-|-|-|
> | [Kelvin](Kelvin.md) | x °C ≘ (x + 273.15) K | x K ≘ (x − 273.15) °C |
> | [Fahrenheit](Fahrenheit.md) | x °C ≘ (x × 9/5 + 32) °F | x °F ≘ (x − 32) × 5/9 °C |
> | [Rankine](Rankine%20scale.md) | x °C ≘ (x + 273.15) × 9/5 °R | x °R ≘ (x − 491.67) × 5/9 °C |

<!--/pytextgen-->

<!--pytextgen generate section="33dd"--><!-- The following content is generated at 2024-03-07T00:30:25.300831+08:00. Any edits will be overridden! -->

- [Kelvin](Kelvin.md):@:from [Celsius](Celsius.md): x °C ≘ (x + 273.15) K, to [Celsius](Celsius.md): x K ≘ (x − 273.15) °C <!--SR:!2027-06-16,991,350-->
- [Fahrenheit](Fahrenheit.md):@:from [Celsius](Celsius.md): x °C ≘ (x × 9/5 + 32) °F, to [Celsius](Celsius.md): x °F ≘ (x − 32) × 5/9 °C <!--SR:!2027-04-28,811,290-->
- [Rankine](Rankine%20scale.md):@:from [Celsius](Celsius.md): x °C ≘ (x + 273.15) × 9/5 °R, to [Celsius](Celsius.md): x °R ≘ (x − 491.67) × 5/9 °C <!--SR:!2026-04-05,221,150-->

<!--/pytextgen-->

<!--pytextgen generate section="76bc"--><!-- The following content is generated at 2024-03-07T00:30:25.322423+08:00. Any edits will be overridden! -->

- from [Celsius](Celsius.md): x °C ≘ (x + 273.15) K, to [Celsius](Celsius.md): x K ≘ (x − 273.15) °C:@:[Kelvin](Kelvin.md) <!--SR:!2028-05-08,1247,350-->
- from [Celsius](Celsius.md): x °C ≘ (x × 9/5 + 32) °F, to [Celsius](Celsius.md): x °F ≘ (x − 32) × 5/9 °C:@:[Fahrenheit](Fahrenheit.md) <!--SR:!2027-07-22,1017,350-->
- from [Celsius](Celsius.md): x °C ≘ (x + 273.15) × 9/5 °R, to [Celsius](Celsius.md): x °R ≘ (x − 491.67) × 5/9 °C:@:[Rankine](Rankine%20scale.md) <!--SR:!2027-04-22,876,330-->

<!--/pytextgen-->

## Kelvin scale

- see: [Kelvin](Kelvin.md)

```Python
# pytextgen generate data
return await conversion_table(
  t_kelvin,
  __env__.cwf_sects("955a", "50fb", "1234",),
  (t_celsius, "x K ≘ (x − 273.15) °C", "x °C ≘ (x + 273.15) K",),
  (t_fahrenheit, "x K ≘ (x × 9/5 − 459.67) °F", "x °F ≘ (x + 459.67) × 5/9 K",),
  (t_rankine, "x K ≘ x × 9/5 °R", "x °R ≘ x × 5/9 K",),
)
```

<!--pytextgen generate section="955a"--><!-- The following content is generated at 2024-03-07T00:32:24.829185+08:00. Any edits will be overridden! -->

> | [temperature scale](temperature%20scale.md) | from [Kelvin](Kelvin.md) | to [Kelvin](Kelvin.md) |
> |-|-|-|
> | [Celsius](Celsius.md) | x K ≘ (x − 273.15) °C | x °C ≘ (x + 273.15) K |
> | [Fahrenheit](Fahrenheit.md) | x K ≘ (x × 9/5 − 459.67) °F | x °F ≘ (x + 459.67) × 5/9 K |
> | [Rankine](Rankine%20scale.md) | x K ≘ x × 9/5 °R | x °R ≘ x × 5/9 K |

<!--/pytextgen-->

<!--pytextgen generate section="50fb"--><!-- The following content is generated at 2024-03-07T00:30:25.375033+08:00. Any edits will be overridden! -->

- [Celsius](Celsius.md):@:from [Kelvin](Kelvin.md): x K ≘ (x − 273.15) °C, to [Kelvin](Kelvin.md): x °C ≘ (x + 273.15) K <!--SR:!2028-01-01,1145,350-->
- [Fahrenheit](Fahrenheit.md):@:from [Kelvin](Kelvin.md): x K ≘ (x × 9/5 − 459.67) °F, to [Kelvin](Kelvin.md): x °F ≘ (x + 459.67) × 5/9 K <!--SR:!2028-01-26,851,230-->
- [Rankine](Rankine%20scale.md):@:from [Kelvin](Kelvin.md): x K ≘ x × 9/5 °R, to [Kelvin](Kelvin.md): x °R ≘ x × 5/9 K <!--SR:!2031-02-16,1963,330-->

<!--/pytextgen-->

<!--pytextgen generate section="1234"--><!-- The following content is generated at 2024-03-07T00:30:25.360089+08:00. Any edits will be overridden! -->

- from [Kelvin](Kelvin.md): x K ≘ (x − 273.15) °C, to [Kelvin](Kelvin.md): x °C ≘ (x + 273.15) K:@:[Celsius](Celsius.md) <!--SR:!2028-04-23,1233,350-->
- from [Kelvin](Kelvin.md): x K ≘ (x × 9/5 − 459.67) °F, to [Kelvin](Kelvin.md): x °F ≘ (x + 459.67) × 5/9 K:@:[Fahrenheit](Fahrenheit.md) <!--SR:!2027-05-11,888,330-->
- from [Kelvin](Kelvin.md): x K ≘ x × 9/5 °R, to [Kelvin](Kelvin.md): x °R ≘ x × 5/9 K:@:[Rankine](Rankine%20scale.md) <!--SR:!2027-08-01,948,330-->

<!--/pytextgen-->

## Fahrenheit scale

- see: [Fahrenheit](Fahrenheit.md)

```Python
# pytextgen generate data
return await conversion_table(
  t_fahrenheit,
  __env__.cwf_sects("46ab", "aad2", "3496",),
  (t_celsius, "x °F ≘ (x − 32) × 5/9 °C", "x °C ≘ (x × 9/5 + 32) °F",),
  (t_kelvin, "x °F ≘ (x + 459.67) × 5/9 K", "x K ≘ (x × 9/5 − 459.67) °F",),
  (t_rankine, "x °F ≘ (x + 459.67) °R", "x °R ≘ (x − 459.67) °F",),
)
```

<!--pytextgen generate section="46ab"--><!-- The following content is generated at 2024-03-07T00:32:24.850721+08:00. Any edits will be overridden! -->

> | [temperature scale](temperature%20scale.md) | from [Fahrenheit](Fahrenheit.md) | to [Fahrenheit](Fahrenheit.md) |
> |-|-|-|
> | [Celsius](Celsius.md) | x °F ≘ (x − 32) × 5/9 °C | x °C ≘ (x × 9/5 + 32) °F |
> | [Kelvin](Kelvin.md) | x °F ≘ (x + 459.67) × 5/9 K | x K ≘ (x × 9/5 − 459.67) °F |
> | [Rankine](Rankine%20scale.md) | x °F ≘ (x + 459.67) °R | x °R ≘ (x − 459.67) °F |

<!--/pytextgen-->

<!--pytextgen generate section="aad2"--><!-- The following content is generated at 2024-03-07T00:30:25.407033+08:00. Any edits will be overridden! -->

- [Celsius](Celsius.md):@:from [Fahrenheit](Fahrenheit.md): x °F ≘ (x − 32) × 5/9 °C, to [Fahrenheit](Fahrenheit.md): x °C ≘ (x × 9/5 + 32) °F <!--SR:!2027-01-07,853,330-->
- [Kelvin](Kelvin.md):@:from [Fahrenheit](Fahrenheit.md): x °F ≘ (x + 459.67) × 5/9 K, to [Fahrenheit](Fahrenheit.md): x K ≘ (x × 9/5 − 459.67) °F <!--SR:!2026-11-13,639,250-->
- [Rankine](Rankine%20scale.md):@:from [Fahrenheit](Fahrenheit.md): x °F ≘ (x + 459.67) °R, to [Fahrenheit](Fahrenheit.md): x °R ≘ (x − 459.67) °F <!--SR:!2025-11-01,476,310-->

<!--/pytextgen-->

<!--pytextgen generate section="3496"--><!-- The following content is generated at 2024-03-07T00:30:25.444393+08:00. Any edits will be overridden! -->

- from [Fahrenheit](Fahrenheit.md): x °F ≘ (x − 32) × 5/9 °C, to [Fahrenheit](Fahrenheit.md): x °C ≘ (x × 9/5 + 32) °F:@:[Celsius](Celsius.md) <!--SR:!2027-07-30,948,330-->
- from [Fahrenheit](Fahrenheit.md): x °F ≘ (x + 459.67) × 5/9 K, to [Fahrenheit](Fahrenheit.md): x K ≘ (x × 9/5 − 459.67) °F:@:[Kelvin](Kelvin.md) <!--SR:!2027-04-21,876,330-->
- from [Fahrenheit](Fahrenheit.md): x °F ≘ (x + 459.67) °R, to [Fahrenheit](Fahrenheit.md): x °R ≘ (x − 459.67) °F:@:[Rankine](Rankine%20scale.md) <!--SR:!2026-02-08,545,310-->

<!--/pytextgen-->

## Rankine scale

- see: [Rankine scale](Rankine%20scale.md)

```Python
# pytextgen generate data
return await conversion_table(
  t_rankine,
  __env__.cwf_sects("b0a9", "ef82", "35a1",),
  (t_celsius, "x °R ≘ (x − 491.67) × 5/9 °C", "x °C ≘ (x + 273.15) × 9/5 °R",),
  (t_kelvin, "x °R ≘ x × 5/9 K", "x K ≘ x × 9/5 °R",),
  (t_fahrenheit, "x °R ≘ (x − 459.67) °F", "x °F ≘ (x + 459.67) °R",),
)
```

<!--pytextgen generate section="b0a9"--><!-- The following content is generated at 2024-03-07T00:32:24.869938+08:00. Any edits will be overridden! -->

> | [temperature scale](temperature%20scale.md) | from [Rankine](Rankine%20scale.md) | to [Rankine](Rankine%20scale.md) |
> |-|-|-|
> | [Celsius](Celsius.md) | x °R ≘ (x − 491.67) × 5/9 °C | x °C ≘ (x + 273.15) × 9/5 °R |
> | [Kelvin](Kelvin.md) | x °R ≘ x × 5/9 K | x K ≘ x × 9/5 °R |
> | [Fahrenheit](Fahrenheit.md) | x °R ≘ (x − 459.67) °F | x °F ≘ (x + 459.67) °R |

<!--/pytextgen-->

<!--pytextgen generate section="ef82"--><!-- The following content is generated at 2024-03-07T00:30:25.492261+08:00. Any edits will be overridden! -->

- [Celsius](Celsius.md):@:from [Rankine](Rankine%20scale.md): x °R ≘ (x − 491.67) × 5/9 °C, to [Rankine](Rankine%20scale.md): x °C ≘ (x + 273.15) × 9/5 °R <!--SR:!2027-01-14,633,230-->
- [Kelvin](Kelvin.md):@:from [Rankine](Rankine%20scale.md): x °R ≘ x × 5/9 K, to [Rankine](Rankine%20scale.md): x K ≘ x × 9/5 °R <!--SR:!2027-08-20,1039,350-->
- [Fahrenheit](Fahrenheit.md):@:from [Rankine](Rankine%20scale.md): x °R ≘ (x − 459.67) °F, to [Rankine](Rankine%20scale.md): x °F ≘ (x + 459.67) °R <!--SR:!2026-12-30,731,270-->

<!--/pytextgen-->

<!--pytextgen generate section="35a1"--><!-- The following content is generated at 2024-03-07T00:30:25.461925+08:00. Any edits will be overridden! -->

- from [Rankine](Rankine%20scale.md): x °R ≘ (x − 491.67) × 5/9 °C, to [Rankine](Rankine%20scale.md): x °C ≘ (x + 273.15) × 9/5 °R:@:[Celsius](Celsius.md) <!--SR:!2028-03-02,1195,350-->
- from [Rankine](Rankine%20scale.md): x °R ≘ x × 5/9 K, to [Rankine](Rankine%20scale.md): x K ≘ x × 9/5 °R:@:[Kelvin](Kelvin.md) <!--SR:!2028-02-18,1183,350-->
- from [Rankine](Rankine%20scale.md): x °R ≘ (x − 459.67) °F, to [Rankine](Rankine%20scale.md): x °F ≘ (x + 459.67) °R:@:[Fahrenheit](Fahrenheit.md) <!--SR:!2027-06-18,991,350-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/conversion_of_scales_of_temperature) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
