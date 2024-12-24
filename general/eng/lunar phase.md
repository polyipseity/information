---
aliases:
  - Moon phase
  - Moon phases
  - lunar phase
  - lunar phases
  - moon phase
  - moon phases
tags:
  - flashcard/active/general/eng/lunar_phase
  - language/in/English
---

# lunar phase

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

A __lunar phase__ or __Moon phase__ is {@{the apparent shape of the [Moon](Moon.md)'s directly sunlit portion as viewed from [Earth](Earth.md)}@}. In common usage, the four major phases are {@{the [new moon](new%20moon.md), the first quarter, the [full moon](full%20moon.md) and the last quarter}@}; the four minor phases are {@{waxing crescent, waxing gibbous, waning gibbous, and waning crescent}@}. A [lunar month](lunar%20month.md) is thus {@{the time between successive recurrences of the same phase}@}. The duration is {@{not perfectly constant due to [eccentricity](orbital%20eccentricity.md) of the Moon's orbit, but averages out to about 29.5 days, which is also the [synodic orbital period](orbital%20period.md#synodic%20period) of the Moon}@}. <!--SR:!2025-03-24,184,310!2025-03-25,192,310!2025-03-05,180,310!2025-05-18,222,310!2025-08-10,256,270-->

The appearance of the [Moon](Moon.md) (its phase) depends on {@{the relative orbital positions of the Moon, [Earth](Earth.md), and the [Sun](Sun.md)}@}. It gradually {@{changes over a [lunar month](lunar%20month.md) as the Moon orbits around Earth and Earth orbits around the Sun}@}. Half of the Moon is {@{always sunlit (the side facing the Sun), but as the visible side (the side facing the Earth) shifts relative to the sunlit side, so the portion of visible side that is sunlit changes}@}, varying from {@{0% at [new moon](new%20moon.md) to nearly 100% at [full moon](full%20moon.md)}@}. The rotation of Earth {@{has only little effect on the phase}@} because {@{the [lunar distance](lunar%20distance.md) is about 30 times the diameter of Earth, so the perspective of observers on Earth changes only very slightly}@}. This partially contributes to {@{[lunar libration](libration.md) slightly}@}. <!--SR:!2025-02-12,156,310!2025-02-20,174,310!2025-05-31,252,330!2025-04-27,225,330!2025-02-08,147,290!2025-03-29,196,310!2025-07-10,281,330-->

As different [Moon](Moon.md) phases represent {@{different relative orbital positions of the Moon relative to [Earth](Earth.md)}@}, this also means the corresponding {@{moonrise and moonset are at different times of the day}@}. In particular, the Moon rises and sets {@{about 50 minutes later each day}@}. <!--SR:!2025-05-17,244,330!2025-07-10,282,330!2025-07-08,264,305-->

## principal and intermediate phases of the Moon

```Python
# pytextgen generate data
from asyncio import gather
from itertools import chain
headers = R"moon phase", R"visibility", R"average moonrise time", R"culmination time (highest point)", R"average moonset time"
map_indices = headers.index(R"moon phase"), headers.index(R"visibility")
table = (
  (R"[new moon](new%20moon.md)", R"invisible due to being too closed to the [Sun](Sun.md) except during a [solar eclipse](solar%20eclipse.md)", R"06:00", R"12:00", R"18:00"),
  (R"waxing [crescent](crescent.md)", R"late morning to post-dusk", R"09:00", R"15:00", R"21:00"),
  (R"first quarter", R"afternoon to early night", R"12:00", R"18:00", R"00:00"),
  (R"waxing gibbous", R"late afternoon to most of night", R"15:00", R"21:00", R"03:00"),
  (R"[full moon](full%20moon.md)", R"all night (sunset to sunrise)", R"18:00", R"00:00", R"06:00"),
  (R"waning gibbous", R"most of night to early morning", R"21:00", R"03:00", R"09:00"),
  (R"last quarter", R"late night to morning", R"00:00", R"06:00", R"12:00"),
  (R"waning [crescent](cresceent.md)", R"pre-dawn to early afternoon", R"03:00", R"09:00", R"15:00"),
)
return chain.from_iterable(await gather(
  memorize_table(
    __env__.cwf_sects("2f02", "652a"),
    headers,
    table,
  ),
  memorize_map(
    __env__.cwf_sects(None, "3b1a", "d8fa"),
    {item[map_indices[0]]: item[map_indices[1]] for item in table},
  )
))
```

<!--pytextgen generate section="2f02"--><!-- The following content is generated at 2024-07-04T10:16:44.291574+08:00. Any edits will be overridden! -->

> | moon phase | visibility | average moonrise time | culmination time (highest point) | average moonset time |
> |-|-|-|-|-|
> | [new moon](new%20moon.md) | invisible due to being too closed to the [Sun](Sun.md) except during a [solar eclipse](solar%20eclipse.md) | 06:00 | 12:00 | 18:00 |
> | waxing [crescent](crescent.md) | late morning to post-dusk | 09:00 | 15:00 | 21:00 |
> | first quarter | afternoon to early night | 12:00 | 18:00 | 00:00 |
> | waxing gibbous | late afternoon to most of night | 15:00 | 21:00 | 03:00 |
> | [full moon](full%20moon.md) | all night (sunset to sunrise) | 18:00 | 00:00 | 06:00 |
> | waning gibbous | most of night to early morning | 21:00 | 03:00 | 09:00 |
> | last quarter | late night to morning | 00:00 | 06:00 | 12:00 |
> | waning [crescent](cresceent.md) | pre-dawn to early afternoon | 03:00 | 09:00 | 15:00 |

<!--/pytextgen-->

<!--pytextgen generate section="652a"--><!-- The following content is generated at 2024-07-04T10:16:44.272591+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[new moon](new%20moon.md) <!--SR:!2025-04-28,226,330!2025-04-15,217,330-->
- [new moon](new%20moon.md)→::@::←waxing [crescent](crescent.md) <!--SR:!2025-05-04,232,330!2025-07-01,274,330-->
- waxing [crescent](crescent.md)→::@::←first quarter <!--SR:!2025-01-29,95,290!2025-07-30,295,330-->
- first quarter→::@::←waxing gibbous <!--SR:!2025-01-26,152,310!2025-01-30,94,290-->
- waxing gibbous→::@::←[full moon](full%20moon.md) <!--SR:!2025-06-23,273,330!2025-04-16,218,330-->
- [full moon](full%20moon.md)→::@::←waning gibbous <!--SR:!2025-03-03,170,310!2025-07-21,291,330-->
- waning gibbous→::@::←last quarter <!--SR:!2025-04-24,224,330!2025-08-14,310,330-->
- last quarter→::@::←waning [crescent](cresceent.md) <!--SR:!2025-02-08,150,290!2025-06-23,268,330-->
- waning [crescent](cresceent.md)→::@::←_(end)_ <!--SR:!2025-04-11,214,330!2025-03-04,170,310-->

<!--/pytextgen-->

<!--pytextgen generate section="3b1a"--><!-- The following content is generated at 2024-07-04T10:16:44.255004+08:00. Any edits will be overridden! -->

- [new moon](new%20moon.md):@:invisible due to being too closed to the [Sun](Sun.md) except during a [solar eclipse](solar%20eclipse.md) <!--SR:!2025-05-05,233,330-->
- waxing [crescent](crescent.md):@:late morning to post-dusk <!--SR:!2025-12-07,351,290-->
- first quarter:@:afternoon to early night <!--SR:!2025-08-03,299,330-->
- waxing gibbous:@:late afternoon to most of night <!--SR:!2025-06-03,212,270-->
- [full moon](full%20moon.md):@:all night (sunset to sunrise) <!--SR:!2025-02-22,172,310-->
- waning gibbous:@:most of night to early morning <!--SR:!2025-01-01,131,290-->
- last quarter:@:late night to morning <!--SR:!2025-03-16,188,310-->
- waning [crescent](cresceent.md):@:pre-dawn to early afternoon <!--SR:!2024-12-23,102,250-->

<!--/pytextgen-->

<!--pytextgen generate section="d8fa"--><!-- The following content is generated at 2024-07-04T10:16:44.237111+08:00. Any edits will be overridden! -->

- invisible due to being too closed to the [Sun](Sun.md) except during a [solar eclipse](solar%20eclipse.md):@:[new moon](new%20moon.md) <!--SR:!2025-06-12,259,330-->
- late morning to post-dusk:@:waxing [crescent](crescent.md) <!--SR:!2025-05-21,203,270-->
- afternoon to early night:@:first quarter <!--SR:!2025-03-09,145,270-->
- late afternoon to most of night:@:waxing gibbous <!--SR:!2025-08-01,235,250-->
- all night (sunset to sunrise):@:[full moon](full%20moon.md) <!--SR:!2025-03-08,173,310-->
- most of night to early morning:@:waning gibbous <!--SR:!2025-02-22,168,310-->
- late night to morning:@:last quarter <!--SR:!2025-03-20,192,310-->
- pre-dawn to early afternoon:@:waning [crescent](cresceent.md) <!--SR:!2025-03-23,166,270-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/lunar_phase) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
