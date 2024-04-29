---
aliases:
  - crude oil
  - crude oils
  - oil
  - oils
  - petroleum
tags:
  - flashcard/general/petroleum
  - language/in/English
---

# petroleum

%%

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

%%

## composition

Petroleum is {{a [heterogeneous mixture](mixture.md#heterogeneous%20mixture) of many [hydrocarbons](hydrocarbon.md)}}. Larger hydrocarbons have {{higher [boiling points](boiling%20point.md), darker colors, more [viscous](viscosity.md), less [volatile](volatility%20(chemistry).md), less [flammable](flammability.md), and burn less completely}}. <!--SR:!2025-11-06,665,314!2024-05-22,243,234-->

## uses

Petroleum is {{separated by [fractional distillation](fractional%20distillation.md) in [fractionating columns](fractionating%20column.md)}}. Fractions that {{have lower [boiling points](boiling%20point.md) are collected at the top}}. It is used for {{making [fuels](#fuels) and derivatives}}. <!--SR:!2024-05-19,177,234!2025-11-02,602,274!2024-10-06,347,294-->

### fuels

%%

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = ('[fraction](fraction%20(chemistry).md)', '[boiling point](boiling%20point.md) range', 'use(s)',)
table = (
  ('[liqueified petroleum gas](liqueified%20petroleum%20gas.md)', '-40 to -1 °C', '[chemical synthesis](chemical%20synthesis.md), [fuel](fuel.md)',),
  ('[butane](butane.md)', '-12 to -1 °C', '',),
  ('[gasoline/petrol](gasoline.md)', '-1 to 110 °C', 'fuel for [motor vehicles](motor%20vehicle.md)',),
  ('[naphtha](naphtha.md)', '30 to 200 °C', 'production of [plastics](plastic.md) and [town gas](coal%20gas.md)',),
  ('[jet fuel](jet%20fuel.md)', '150 to 205 °C', 'fuel for [aeroplanes](airplane.md)',),
  ('[kerosene](kerosene.md)', '205 to 260 °C', 'fuel for domestic use',),
  ('[fuel oil](fuel%20oil.md)', '205 to 290 °C', 'fuel for [power plants](power%20station.md) and [ships](ship.md)',),
  ('[diesel fuel](diesel%20fuel.md)', '260 to 315 °C', 'fuel for [buses](bus.md) and [trucks](truck.md)',),
  ('[paraffin wax](paraffin%20wax.md)', '370 °C or above', '[candles](candle.md), [lubrication](lubrication.md)',),
  ('[bitumen](bitumen.md)', '500 °C or above', '[road construction](road%20construction.md)',),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects('2039', 'd5f1',),
    headers, table,
  ),
  memorize_map(
    __env__.cwf_sects(None, '3984', 'e8ff',),
    items_to_map(*(row[:2] for row in table)),
  ),
  memorize_map(
    __env__.cwf_sects(None, '495a', None,),
    items_to_map(*((row[0], row[2]) for row in table if row[2])),
  ),
))
```

%%

[Fuels](fuel.md) by ascending [boiling point](boiling%20point.md) include:

<!--pytextgen generate section="2039"--><!-- The following content is generated at 2023-12-04T08:18:54.256450+08:00. Any edits will be overridden! -->

> | [fraction](fraction%20(chemistry).md) | [boiling point](boiling%20point.md) range | use(s) |
> |-|-|-|
> | [liqueified petroleum gas](liqueified%20petroleum%20gas.md) | -40 to -1 °C | [chemical synthesis](chemical%20synthesis.md), [fuel](fuel.md) |
> | [butane](butane.md) | -12 to -1 °C |  |
> | [gasoline/petrol](gasoline.md) | -1 to 110 °C | fuel for [motor vehicles](motor%20vehicle.md) |
> | [naphtha](naphtha.md) | 30 to 200 °C | production of [plastics](plastic.md) and [town gas](coal%20gas.md) |
> | [jet fuel](jet%20fuel.md) | 150 to 205 °C | fuel for [aeroplanes](airplane.md) |
> | [kerosene](kerosene.md) | 205 to 260 °C | fuel for domestic use |
> | [fuel oil](fuel%20oil.md) | 205 to 290 °C | fuel for [power plants](power%20station.md) and [ships](ship.md) |
> | [diesel fuel](diesel%20fuel.md) | 260 to 315 °C | fuel for [buses](bus.md) and [trucks](truck.md) |
> | [paraffin wax](paraffin%20wax.md) | 370 °C or above | [candles](candle.md), [lubrication](lubrication.md) |
> | [bitumen](bitumen.md) | 500 °C or above | [road construction](road%20construction.md) |

<!--/pytextgen-->

<!--pytextgen generate section="d5f1"--><!-- The following content is generated at 2024-01-04T20:17:52.536836+08:00. Any edits will be overridden! -->

- _(begin)_→:::←[liqueified petroleum gas](liqueified%20petroleum%20gas.md) <!--SR:!2026-09-26,912,330!2024-05-19,322,334-->
- [liqueified petroleum gas](liqueified%20petroleum%20gas.md)→:::←[butane](butane.md) <!--SR:!2026-10-09,928,334!2026-10-02,924,334-->
- [butane](butane.md)→:::←[gasoline/petrol](gasoline.md) <!--SR:!2024-10-26,413,294!2024-09-12,150,314-->
- [gasoline/petrol](gasoline.md)→:::←[naphtha](naphtha.md) <!--SR:!2026-01-03,643,274!2024-05-05,31,150-->
- [naphtha](naphtha.md)→:::←[jet fuel](jet%20fuel.md) <!--SR:!2024-05-06,33,130!2024-08-12,134,214-->
- [jet fuel](jet%20fuel.md)→:::←[kerosene](kerosene.md) <!--SR:!2025-01-24,437,274!2025-04-13,375,194-->
- [kerosene](kerosene.md)→:::←[fuel oil](fuel%20oil.md) <!--SR:!2024-06-27,84,214!2024-04-30,3,130-->
- [fuel oil](fuel%20oil.md)→:::←[diesel fuel](diesel%20fuel.md) <!--SR:!2024-10-30,417,294!2024-11-12,225,254-->
- [diesel fuel](diesel%20fuel.md)→:::←[paraffin wax](paraffin%20wax.md) <!--SR:!2026-09-03,959,334!2024-05-13,42,174-->
- [paraffin wax](paraffin%20wax.md)→:::←[bitumen](bitumen.md) <!--SR:!2024-10-28,432,314!2025-05-06,539,314-->
- [bitumen](bitumen.md)→:::←_(end)_ <!--SR:!2027-05-09,1164,350!2026-12-25,984,334-->

<!--/pytextgen-->

#### fraction–boiling point range

<!--pytextgen generate section="3984"--><!-- The following content is generated at 2024-01-04T20:17:52.568538+08:00. Any edits will be overridden! -->

- [liqueified petroleum gas](liqueified%20petroleum%20gas.md)::-40 to -1 °C <!--SR:!2024-08-12,338,290-->
- [butane](butane.md)::-12 to -1 °C <!--SR:!2024-05-20,307,314-->
- [gasoline/petrol](gasoline.md)::-1 to 110 °C <!--SR:!2024-05-24,46,170-->
- [naphtha](naphtha.md)::30 to 200 °C <!--SR:!2024-05-20,42,190-->
- [jet fuel](jet%20fuel.md)::150 to 205 °C <!--SR:!2024-04-30,3,130-->
- [kerosene](kerosene.md)::205 to 260 °C <!--SR:!2024-05-09,12,130-->
- [fuel oil](fuel%20oil.md)::205 to 290 °C <!--SR:!2024-05-14,15,130-->
- [diesel fuel](diesel%20fuel.md)::260 to 315 °C <!--SR:!2024-05-11,24,130-->
- [paraffin wax](paraffin%20wax.md)::370 °C or above <!--SR:!2024-05-06,54,194-->
- [bitumen](bitumen.md)::500 °C or above <!--SR:!2024-06-15,54,274-->

<!--/pytextgen-->

<!--pytextgen generate section="e8ff"--><!-- The following content is generated at 2024-01-04T20:17:52.452954+08:00. Any edits will be overridden! -->

- -40 to -1 °C::[liqueified petroleum gas](liqueified%20petroleum%20gas.md) <!--SR:!2025-04-25,529,310-->
- -12 to -1 °C::[butane](butane.md) <!--SR:!2026-09-20,914,334-->
- -1 to 110 °C::[gasoline/petrol](gasoline.md) <!--SR:!2024-05-08,110,294-->
- 30 to 200 °C::[naphtha](naphtha.md) <!--SR:!2025-12-14,632,274-->
- 150 to 205 °C::[jet fuel](jet%20fuel.md) <!--SR:!2024-09-09,365,294-->
- 205 to 260 °C::[kerosene](kerosene.md) <!--SR:!2025-01-21,435,274-->
- 205 to 290 °C::[fuel oil](fuel%20oil.md) <!--SR:!2024-08-11,337,274-->
- 260 to 315 °C::[diesel fuel](diesel%20fuel.md) <!--SR:!2025-04-17,429,274-->
- 370 °C or above::[paraffin wax](paraffin%20wax.md) <!--SR:!2025-12-07,690,314-->
- 500 °C or above::[bitumen](bitumen.md) <!--SR:!2024-05-18,321,334-->

<!--/pytextgen-->

#### fraction–use(s)

<!--pytextgen generate section="495a"--><!-- The following content is generated at 2024-01-04T20:17:52.496485+08:00. Any edits will be overridden! -->

- [liqueified petroleum gas](liqueified%20petroleum%20gas.md)::[chemical synthesis](chemical%20synthesis.md), [fuel](fuel.md) <!--SR:!2025-02-20,339,254-->
- [gasoline/petrol](gasoline.md)::fuel for [motor vehicles](motor%20vehicle.md) <!--SR:!2024-09-05,386,314-->
- [naphtha](naphtha.md)::production of [plastics](plastic.md) and [town gas](coal%20gas.md) <!--SR:!2024-06-09,228,234-->
- [jet fuel](jet%20fuel.md)::fuel for [aeroplanes](airplane.md) <!--SR:!2024-07-16,340,294-->
- [kerosene](kerosene.md)::fuel for domestic use <!--SR:!2025-10-28,637,294-->
- [fuel oil](fuel%20oil.md)::fuel for [power plants](power%20station.md) and [ships](ship.md) <!--SR:!2025-11-18,613,274-->
- [diesel fuel](diesel%20fuel.md)::fuel for [buses](bus.md) and [trucks](truck.md) <!--SR:!2024-05-29,51,234-->
- [paraffin wax](paraffin%20wax.md)::[candles](candle.md), [lubrication](lubrication.md) <!--SR:!2025-02-25,522,314-->
- [bitumen](bitumen.md)::[road construction](road%20construction.md) <!--SR:!2024-06-10,339,334-->

<!--/pytextgen-->

## industry

- see: [petroleum industry](petroleum%20industry.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/petroleum) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
