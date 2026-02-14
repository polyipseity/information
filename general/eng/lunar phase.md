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
# import ../../tools/utility.py.md
```

A __lunar phase__ or __Moon phase__ is {@{the apparent shape of the [Moon](Moon.md)'s directly sunlit portion as viewed from [Earth](Earth.md)}@}. In common usage, the four major phases are {@{the [new moon](new%20moon.md), the first quarter, the [full moon](full%20moon.md) and the last quarter}@}; the four minor phases are {@{waxing crescent, waxing gibbous, waning gibbous, and waning crescent}@}. A [lunar month](lunar%20month.md) is thus {@{the time between successive recurrences of the same phase}@}. The duration is {@{not perfectly constant due to [eccentricity](orbital%20eccentricity.md) of the Moon's orbit}@}, but {@{averages out to about 29.5 days}@}, which is also {@{the [synodic orbital period](orbital%20period.md#synodic%20period) of the Moon}@}.

The appearance of the [Moon](Moon.md) (its phase) depends on {@{the relative orbital positions of the Moon, [Earth](Earth.md), and the [Sun](Sun.md)}@}. It gradually {@{changes over a [lunar month](lunar%20month.md) as the Moon orbits around Earth and Earth orbits around the Sun}@}. Half of the Moon is {@{always sunlit (the side facing the Sun), but as the visible side (the side facing the Earth) shifts relative to the sunlit side, so the portion of visible side that is sunlit changes}@}, varying from {@{0% at [new moon](new%20moon.md) to nearly 100% at [full moon](full%20moon.md)}@}. The rotation of Earth {@{has only little effect on the phase}@} because {@{the [lunar distance](lunar%20distance.md) is about 30 times the diameter of Earth, so the perspective of observers on Earth changes only very slightly}@}. This partially contributes to {@{[lunar libration](libration.md) slightly}@}.

As different [Moon](Moon.md) phases represent {@{different relative orbital positions of the Moon relative to [Earth](Earth.md)}@}, this also means the corresponding {@{moonrise and moonset are at different times of the day}@}. In particular, the Moon rises and sets {@{about 50 minutes later each day}@}.

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

<!--pytextgen generate section="2f02"--><!-- The following content is generated at 2026-01-25T23:32:18.892491+08:00. Any edits will be overridden! -->

> | moon phase                      | visibility                                                                                                 | average moonrise time | culmination time (highest point) | average moonset time |
> | ------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------- | -------------------------------- | -------------------- |
> | [new moon](new%20moon.md)       | invisible due to being too closed to the [Sun](Sun.md) except during a [solar eclipse](solar%20eclipse.md) | 06:00                 | 12:00                            | 18:00                |
> | waxing [crescent](crescent.md)  | late morning to post-dusk                                                                                  | 09:00                 | 15:00                            | 21:00                |
> | first quarter                   | afternoon to early night                                                                                   | 12:00                 | 18:00                            | 00:00                |
> | waxing gibbous                  | late afternoon to most of night                                                                            | 15:00                 | 21:00                            | 03:00                |
> | [full moon](full%20moon.md)     | all night (sunset to sunrise)                                                                              | 18:00                 | 00:00                            | 06:00                |
> | waning gibbous                  | most of night to early morning                                                                             | 21:00                 | 03:00                            | 09:00                |
> | last quarter                    | late night to morning                                                                                      | 00:00                 | 06:00                            | 12:00                |
> | waning [crescent](cresceent.md) | pre-dawn to early afternoon                                                                                | 03:00                 | 09:00                            | 15:00                |

<!--/pytextgen-->

<!--pytextgen generate section="652a"--><!-- The following content is generated at 2024-07-04T10:16:44.272591+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[new moon](new%20moon.md)
- [new moon](new%20moon.md)→::@::←waxing [crescent](crescent.md)
- waxing [crescent](crescent.md)→::@::←first quarter
- first quarter→::@::←waxing gibbous
- waxing gibbous→::@::←[full moon](full%20moon.md)
- [full moon](full%20moon.md)→::@::←waning gibbous
- waning gibbous→::@::←last quarter
- last quarter→::@::←waning [crescent](cresceent.md)
- waning [crescent](cresceent.md)→::@::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="3b1a"--><!-- The following content is generated at 2024-07-04T10:16:44.255004+08:00. Any edits will be overridden! -->

- [new moon](new%20moon.md):@:invisible due to being too closed to the [Sun](Sun.md) except during a [solar eclipse](solar%20eclipse.md)
- waxing [crescent](crescent.md):@:late morning to post-dusk
- first quarter:@:afternoon to early night
- waxing gibbous:@:late afternoon to most of night
- [full moon](full%20moon.md):@:all night (sunset to sunrise)
- waning gibbous:@:most of night to early morning
- last quarter:@:late night to morning
- waning [crescent](cresceent.md):@:pre-dawn to early afternoon

<!--/pytextgen-->

<!--pytextgen generate section="d8fa"--><!-- The following content is generated at 2024-07-04T10:16:44.237111+08:00. Any edits will be overridden! -->

- invisible due to being too closed to the [Sun](Sun.md) except during a [solar eclipse](solar%20eclipse.md):@:[new moon](new%20moon.md)
- late morning to post-dusk:@:waxing [crescent](crescent.md)
- afternoon to early night:@:first quarter
- late afternoon to most of night:@:waxing gibbous
- all night (sunset to sunrise):@:[full moon](full%20moon.md)
- most of night to early morning:@:waning gibbous
- late night to morning:@:last quarter
- pre-dawn to early afternoon:@:waning [crescent](cresceent.md)

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/lunar_phase) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
