---
aliases:
  - crude oil
  - crude oils
  - oil
  - oils
  - petroleum
tags:
  - flashcard/active/general/petroleum
  - language/in/English
---

# petroleum

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

## composition

Petroleum is {@{a [heterogeneous mixture](mixture.md#heterogeneous%20mixture) of many [hydrocarbons](hydrocarbon.md)}@}. Larger hydrocarbons have {@{higher [boiling points](boiling%20point.md), darker colors, more [viscous](viscosity.md), less [volatile](volatility%20(chemistry).md), less [flammable](flammability.md), and burn less completely}@}.

## uses

Petroleum is {@{separated by [fractional distillation](fractional%20distillation.md) in [fractionating columns](fractionating%20column.md)}@}. Fractions that {@{have lower [boiling points](boiling%20point.md) are collected at the top}@}. It is used for {@{making [fuels](#fuels) and derivatives}@}.

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

- _(begin)_→::@::←[liqueified petroleum gas](liqueified%20petroleum%20gas.md)
- [liqueified petroleum gas](liqueified%20petroleum%20gas.md)→::@::←[butane](butane.md)
- [butane](butane.md)→::@::←[gasoline/petrol](gasoline.md)
- [gasoline/petrol](gasoline.md)→::@::←[naphtha](naphtha.md)
- [naphtha](naphtha.md)→::@::←[jet fuel](jet%20fuel.md)
- [jet fuel](jet%20fuel.md)→::@::←[kerosene](kerosene.md)
- [kerosene](kerosene.md)→::@::←[fuel oil](fuel%20oil.md)
- [fuel oil](fuel%20oil.md)→::@::←[diesel fuel](diesel%20fuel.md)
- [diesel fuel](diesel%20fuel.md)→::@::←[paraffin wax](paraffin%20wax.md)
- [paraffin wax](paraffin%20wax.md)→::@::←[bitumen](bitumen.md)
- [bitumen](bitumen.md)→::@::←_(end)_

<!--/pytextgen-->

#### fraction–boiling point range

<!--pytextgen generate section="3984"--><!-- The following content is generated at 2024-01-04T20:17:52.568538+08:00. Any edits will be overridden! -->

- [liqueified petroleum gas](liqueified%20petroleum%20gas.md):@:-40 to -1 °C
- [butane](butane.md):@:-12 to -1 °C
- [gasoline/petrol](gasoline.md):@:-1 to 110 °C
- [naphtha](naphtha.md):@:30 to 200 °C
- [jet fuel](jet%20fuel.md):@:150 to 205 °C
- [kerosene](kerosene.md):@:205 to 260 °C
- [fuel oil](fuel%20oil.md):@:205 to 290 °C
- [diesel fuel](diesel%20fuel.md):@:260 to 315 °C
- [paraffin wax](paraffin%20wax.md):@:370 °C or above
- [bitumen](bitumen.md):@:500 °C or above

<!--/pytextgen-->

<!--pytextgen generate section="e8ff"--><!-- The following content is generated at 2024-01-04T20:17:52.452954+08:00. Any edits will be overridden! -->

- -40 to -1 °C:@:[liqueified petroleum gas](liqueified%20petroleum%20gas.md)
- -12 to -1 °C:@:[butane](butane.md)
- -1 to 110 °C:@:[gasoline/petrol](gasoline.md)
- 30 to 200 °C:@:[naphtha](naphtha.md)
- 150 to 205 °C:@:[jet fuel](jet%20fuel.md)
- 205 to 260 °C:@:[kerosene](kerosene.md)
- 205 to 290 °C:@:[fuel oil](fuel%20oil.md)
- 260 to 315 °C:@:[diesel fuel](diesel%20fuel.md)
- 370 °C or above:@:[paraffin wax](paraffin%20wax.md)
- 500 °C or above:@:[bitumen](bitumen.md)

<!--/pytextgen-->

#### fraction–use(s)

<!--pytextgen generate section="495a"--><!-- The following content is generated at 2024-01-04T20:17:52.496485+08:00. Any edits will be overridden! -->

- [liqueified petroleum gas](liqueified%20petroleum%20gas.md):@:[chemical synthesis](chemical%20synthesis.md), [fuel](fuel.md)
- [gasoline/petrol](gasoline.md):@:fuel for [motor vehicles](motor%20vehicle.md)
- [naphtha](naphtha.md):@:production of [plastics](plastic.md) and [town gas](coal%20gas.md)
- [jet fuel](jet%20fuel.md):@:fuel for [aeroplanes](airplane.md)
- [kerosene](kerosene.md):@:fuel for domestic use
- [fuel oil](fuel%20oil.md):@:fuel for [power plants](power%20station.md) and [ships](ship.md)
- [diesel fuel](diesel%20fuel.md):@:fuel for [buses](bus.md) and [trucks](truck.md)
- [paraffin wax](paraffin%20wax.md):@:[candles](candle.md), [lubrication](lubrication.md)
- [bitumen](bitumen.md):@:[road construction](road%20construction.md)

<!--/pytextgen-->

## industry

- see: [petroleum industry](petroleum%20industry.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/petroleum) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
