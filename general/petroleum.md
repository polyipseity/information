---
aliases:
  - crude oil
  - crude oils
  - oil
  - oils
  - petroleum
tags:
  - flashcards/general/petroleum
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# petroleum

## composition

Petroleum is {{a [heterogeneous mixture](mixture.md#heterogeneous%20mixture) of many [hydrocarbons](hydrocarbon.md)}}. Larger hydrocarbons have {{higher [boiling points](boiling%20point.md), darker colors, more [viscous](viscosity.md), less [volatile](volatility%20(chemistry).md), less [flammable](flammability.md), and burn less completely}}.

## uses

Petroleum is {{separated by [fractional distillation](fractional%20distillation.md) in [fractionating columns](fractionating%20column.md)}}. Fractions that {{have lower [boiling points](boiling%20point.md) are collected at the top}}. It is used for {{making [fuels](#fuels) and derivatives}}.

### fuels

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain

e = __env__
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
    e.cwf_sects('2039', 'd5f1',),
    headers, table,
  ),
  memorize_map(
    e.cwf_sects(None, '3984', 'e8ff',),
    items_to_map(*(row[:2] for row in table)),
  ),
  memorize_map(
    e.cwf_sects(None, '495a', None,),
    items_to_map(*((row[0], row[2]) for row in table if row[2])),
  ),
))
```
%%

[Fuels](fuel.md) by ascending [boiling point](boiling%20point.md) include:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2039"--><!-- The following content is generated at 2023-12-04T08:18:54.256450+08:00. Any edits will be overridden! -->

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

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d5f1"--><!-- The following content is generated at 2023-03-24T01:37:04.143883+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[liqueified petroleum gas](liqueified%20petroleum%20gas.md)
2. [liqueified petroleum gas](liqueified%20petroleum%20gas.md)→:::←[butane](butane.md)
3. [butane](butane.md)→:::←[gasoline/petrol](gasoline.md)
4. [gasoline/petrol](gasoline.md)→:::←[naphtha](naphtha.md)
5. [naphtha](naphtha.md)→:::←[jet fuel](jet%20fuel.md)
6. [jet fuel](jet%20fuel.md)→:::←[kerosene](kerosene.md)
7. [kerosene](kerosene.md)→:::←[fuel oil](fuel%20oil.md)
8. [fuel oil](fuel%20oil.md)→:::←[diesel fuel](diesel%20fuel.md)
9. [diesel fuel](diesel%20fuel.md)→:::←[paraffin wax](paraffin%20wax.md)
10. [paraffin wax](paraffin%20wax.md)→:::←[bitumen](bitumen.md)
11. [bitumen](bitumen.md)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### fraction–boiling point range

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3984"--><!-- The following content is generated at 2023-12-04T08:18:54.328065+08:00. Any edits will be overridden! -->

1. [liqueified petroleum gas](liqueified%20petroleum%20gas.md)::-40 to -1 °C
2. [butane](butane.md)::-12 to -1 °C
3. [gasoline/petrol](gasoline.md)::-1 to 110 °C
4. [naphtha](naphtha.md)::30 to 200 °C
5. [jet fuel](jet%20fuel.md)::150 to 205 °C
6. [kerosene](kerosene.md)::205 to 260 °C
7. [fuel oil](fuel%20oil.md)::205 to 290 °C
8. [diesel fuel](diesel%20fuel.md)::260 to 315 °C
9. [paraffin wax](paraffin%20wax.md)::370 °C or above
10. [bitumen](bitumen.md)::500 °C or above

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="e8ff"--><!-- The following content is generated at 2023-12-04T08:18:54.227804+08:00. Any edits will be overridden! -->

1. -40 to -1 °C::[liqueified petroleum gas](liqueified%20petroleum%20gas.md)
2. -12 to -1 °C::[butane](butane.md)
3. -1 to 110 °C::[gasoline/petrol](gasoline.md)
4. 30 to 200 °C::[naphtha](naphtha.md)
5. 150 to 205 °C::[jet fuel](jet%20fuel.md)
6. 205 to 260 °C::[kerosene](kerosene.md)
7. 205 to 290 °C::[fuel oil](fuel%20oil.md)
8. 260 to 315 °C::[diesel fuel](diesel%20fuel.md)
9. 370 °C or above::[paraffin wax](paraffin%20wax.md)
10. 500 °C or above::[bitumen](bitumen.md)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### fraction–use(s)

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="495a"--><!-- The following content is generated at 2023-12-04T08:18:54.205129+08:00. Any edits will be overridden! -->

1. [liqueified petroleum gas](liqueified%20petroleum%20gas.md)::[chemical synthesis](chemical%20synthesis.md), [fuel](fuel.md)
2. [gasoline/petrol](gasoline.md)::fuel for [motor vehicles](motor%20vehicle.md)
3. [naphtha](naphtha.md)::production of [plastics](plastic.md) and [town gas](coal%20gas.md)
4. [jet fuel](jet%20fuel.md)::fuel for [aeroplanes](airplane.md)
5. [kerosene](kerosene.md)::fuel for domestic use
6. [fuel oil](fuel%20oil.md)::fuel for [power plants](power%20station.md) and [ships](ship.md)
7. [diesel fuel](diesel%20fuel.md)::fuel for [buses](bus.md) and [trucks](truck.md)
8. [paraffin wax](paraffin%20wax.md)::[candles](candle.md), [lubrication](lubrication.md)
9. [bitumen](bitumen.md)::[road construction](road%20construction.md)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## industry

- see: [petroleum industry](petroleum%20industry.md)
