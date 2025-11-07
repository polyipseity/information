---
aliases:
  - crude oil
  - crude oils
  - oil
  - oils
  - petroleum
tags:
  - flashcard/active/general/eng/petroleum
  - language/in/English
---

# petroleum

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## composition

Petroleum is {@{a [heterogeneous mixture](mixture.md#heterogeneous%20mixture) of many [hydrocarbons](hydrocarbon.md)}@}. Larger hydrocarbons have {@{higher [boiling points](boiling%20point.md), darker colors, more [viscous](viscosity.md), less [volatile](volatility%20(chemistry).md), less [flammable](flammability.md), and burn less completely}@}. <!--SR:!2033-10-02,2887,334!2026-08-01,801,254-->

## uses

Petroleum is {@{separated by [fractional distillation](fractional%20distillation.md) in [fractionating columns](fractionating%20column.md)}@}. Fractions that {@{have lower [boiling points](boiling%20point.md) are collected at the top}@}. It is used for {@{making [fuels](#fuels) and derivatives}@}. <!--SR:!2025-12-23,583,254!2032-02-19,2300,294!2027-07-24,1019,294-->

### fuels

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

- _(begin)_→::@::←[liqueified petroleum gas](liqueified%20petroleum%20gas.md) <!--SR:!2026-09-26,912,330!2028-06-08,1481,354-->
- [liqueified petroleum gas](liqueified%20petroleum%20gas.md)→::@::←[butane](butane.md) <!--SR:!2026-10-09,928,334!2026-10-02,924,334-->
- [butane](butane.md)→::@::←[gasoline/petrol](gasoline.md) <!--SR:!2028-02-13,1205,294!2025-12-26,470,314-->
- [gasoline/petrol](gasoline.md)→::@::←[naphtha](naphtha.md) <!--SR:!2026-01-03,643,274!2026-02-09,228,170-->
- [naphtha](naphtha.md)→::@::←[jet fuel](jet%20fuel.md) <!--SR:!2026-04-28,184,170!2027-10-23,876,234-->
- [jet fuel](jet%20fuel.md)→::@::←[kerosene](kerosene.md) <!--SR:!2028-05-10,1202,274!2027-04-11,728,194-->
- [kerosene](kerosene.md)→::@::←[fuel oil](fuel%20oil.md) <!--SR:!2026-01-12,384,214!2025-12-02,85,130-->
- [fuel oil](fuel%20oil.md)→::@::←[diesel fuel](diesel%20fuel.md) <!--SR:!2028-03-11,1228,294!2026-06-08,573,254-->
- [diesel fuel](diesel%20fuel.md)→::@::←[paraffin wax](paraffin%20wax.md) <!--SR:!2026-09-03,959,334!2025-12-22,234,194-->
- [paraffin wax](paraffin%20wax.md)→::@::←[bitumen](bitumen.md) <!--SR:!2027-03-30,656,294!2029-12-17,1686,314-->
- [bitumen](bitumen.md)→::@::←_(end)_ <!--SR:!2027-05-09,1164,350!2026-12-25,984,334-->

<!--/pytextgen-->

#### fraction–boiling point range

<!--pytextgen generate section="3984"--><!-- The following content is generated at 2024-01-04T20:17:52.568538+08:00. Any edits will be overridden! -->

- [liqueified petroleum gas](liqueified%20petroleum%20gas.md):@:-40 to -1 °C <!--SR:!2026-05-07,462,270-->
- [butane](butane.md):@:-12 to -1 °C <!--SR:!2027-01-08,963,314-->
- [gasoline/petrol](gasoline.md):@:-1 to 110 °C <!--SR:!2027-01-19,543,190-->
- [naphtha](naphtha.md):@:30 to 200 °C <!--SR:!2026-10-02,387,190-->
- [jet fuel](jet%20fuel.md):@:150 to 205 °C <!--SR:!2026-03-22,208,170-->
- [kerosene](kerosene.md):@:205 to 260 °C <!--SR:!2026-12-18,424,170-->
- [fuel oil](fuel%20oil.md):@:205 to 290 °C <!--SR:!2026-01-27,134,150-->
- [diesel fuel](diesel%20fuel.md):@:260 to 315 °C <!--SR:!2025-12-07,156,150-->
- [paraffin wax](paraffin%20wax.md):@:370 °C or above <!--SR:!2026-08-24,416,194-->
- [bitumen](bitumen.md):@:500 °C or above <!--SR:!2026-09-06,608,294-->

<!--/pytextgen-->

<!--pytextgen generate section="e8ff"--><!-- The following content is generated at 2024-01-04T20:17:52.452954+08:00. Any edits will be overridden! -->

- -40 to -1 °C:@:[liqueified petroleum gas](liqueified%20petroleum%20gas.md) <!--SR:!2029-10-24,1643,310-->
- -12 to -1 °C:@:[butane](butane.md) <!--SR:!2026-09-20,914,334-->
- -1 to 110 °C:@:[gasoline/petrol](gasoline.md) <!--SR:!2027-10-29,947,294-->
- 30 to 200 °C:@:[naphtha](naphtha.md) <!--SR:!2025-12-14,632,274-->
- 150 to 205 °C:@:[jet fuel](jet%20fuel.md) <!--SR:!2026-07-22,499,274-->
- 205 to 260 °C:@:[kerosene](kerosene.md) <!--SR:!2028-04-26,1191,274-->
- 205 to 290 °C:@:[fuel oil](fuel%20oil.md) <!--SR:!2027-02-20,922,274-->
- 260 to 315 °C:@:[diesel fuel](diesel%20fuel.md) <!--SR:!2027-12-24,766,274-->
- 370 °C or above:@:[paraffin wax](paraffin%20wax.md) <!--SR:!2025-12-07,690,314-->
- 500 °C or above:@:[bitumen](bitumen.md) <!--SR:!2028-06-03,1476,354-->

<!--/pytextgen-->

#### fraction–use(s)

<!--pytextgen generate section="495a"--><!-- The following content is generated at 2024-01-04T20:17:52.496485+08:00. Any edits will be overridden! -->

- [liqueified petroleum gas](liqueified%20petroleum%20gas.md):@:[chemical synthesis](chemical%20synthesis.md), [fuel](fuel.md) <!--SR:!2027-07-02,862,254-->
- [gasoline/petrol](gasoline.md):@:fuel for [motor vehicles](motor%20vehicle.md) <!--SR:!2027-12-30,1211,314-->
- [naphtha](naphtha.md):@:production of [plastics](plastic.md) and [town gas](coal%20gas.md) <!--SR:!2025-11-24,533,234-->
- [jet fuel](jet%20fuel.md):@:fuel for [aeroplanes](airplane.md) <!--SR:!2027-04-11,999,294-->
- [kerosene](kerosene.md):@:fuel for domestic use <!--SR:!2032-12-10,2600,314-->
- [fuel oil](fuel%20oil.md):@:fuel for [power plants](power%20station.md) and [ships](ship.md) <!--SR:!2032-04-19,2344,294-->
- [diesel fuel](diesel%20fuel.md):@:fuel for [buses](bus.md) and [trucks](truck.md) <!--SR:!2027-12-04,896,254-->
- [paraffin wax](paraffin%20wax.md):@:[candles](candle.md), [lubrication](lubrication.md) <!--SR:!2029-08-26,1643,314-->
- [bitumen](bitumen.md):@:[road construction](road%20construction.md) <!--SR:!2028-09-16,1559,354-->

<!--/pytextgen-->

## industry

- see: [petroleum industry](petroleum%20industry.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/petroleum) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
