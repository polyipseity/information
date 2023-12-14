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

Petroleum is {{a [heterogeneous mixture](mixture.md#heterogeneous%20mixture) of many [hydrocarbons](hydrocarbon.md)}}. Larger hydrocarbons have {{higher [boiling points](boiling%20point.md), darker colors, more [viscous](viscosity.md), less [volatile](volatility%20(chemistry).md), less [flammable](flammability.md), and burn less completely}}. <!--SR:!2024-01-10,212,314!2024-05-22,243,234-->

## uses

Petroleum is {{separated by [fractional distillation](fractional%20distillation.md) in [fractionating columns](fractionating%20column.md)}}. Fractions that {{have lower [boiling points](boiling%20point.md) are collected at the top}}. It is used for {{making [fuels](#fuels) and derivatives}}. <!--SR:!2024-05-19,177,234!2024-03-09,220,274!2024-10-06,347,294-->

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

1. _(begin)_→:::←[liqueified petroleum gas](liqueified%20petroleum%20gas.md) <!--SR:!2024-03-27,276,330!2024-05-19,322,334-->
2. [liqueified petroleum gas](liqueified%20petroleum%20gas.md)→:::←[butane](butane.md) <!--SR:!2024-03-23,278,334!2024-03-22,277,334-->
3. [butane](butane.md)→:::←[gasoline/petrol](gasoline.md) <!--SR:!2024-10-26,413,294!2024-04-13,291,334-->
4. [gasoline/petrol](gasoline.md)→:::←[naphtha](naphtha.md) <!--SR:!2024-03-29,235,274!2023-12-16,3,134-->
5. [naphtha](naphtha.md)→:::←[jet fuel](jet%20fuel.md) <!--SR:!2024-01-18,37,130!2023-12-27,63,234-->
6. [jet fuel](jet%20fuel.md)→:::←[kerosene](kerosene.md) <!--SR:!2025-01-24,437,274!2024-04-03,194,194-->
7. [kerosene](kerosene.md)→:::←[fuel oil](fuel%20oil.md) <!--SR:!2024-02-24,77,234!2023-12-19,50,194-->
8. [fuel oil](fuel%20oil.md)→:::←[diesel fuel](diesel%20fuel.md) <!--SR:!2024-10-30,417,294!2024-01-03,180,274-->
9. [diesel fuel](diesel%20fuel.md)→:::←[paraffin wax](paraffin%20wax.md) <!--SR:!2024-01-18,221,314!2023-12-16,15,214-->
10. [paraffin wax](paraffin%20wax.md)→:::←[bitumen](bitumen.md) <!--SR:!2024-10-28,432,314!2025-05-06,539,314-->
11. [bitumen](bitumen.md)→:::←_(end)_ <!--SR:!2024-03-01,256,330!2024-04-15,295,334-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### fraction–boiling point range

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3984"--><!-- The following content is generated at 2023-12-04T08:18:54.328065+08:00. Any edits will be overridden! -->

1. [liqueified petroleum gas](liqueified%20petroleum%20gas.md)::-40 to -1 °C <!--SR:!2024-08-12,338,290-->
2. [butane](butane.md)::-12 to -1 °C <!--SR:!2024-05-20,307,314-->
3. [gasoline/petrol](gasoline.md)::-1 to 110 °C <!--SR:!2024-01-08,30,230-->
4. [naphtha](naphtha.md)::30 to 200 °C <!--SR:!2024-01-18,164,230-->
5. [jet fuel](jet%20fuel.md)::150 to 205 °C <!--SR:!2023-12-19,6,130-->
6. [kerosene](kerosene.md)::205 to 260 °C <!--SR:!2023-12-15,1,130-->
7. [fuel oil](fuel%20oil.md)::205 to 290 °C <!--SR:!2024-01-23,130,190-->
8. [diesel fuel](diesel%20fuel.md)::260 to 315 °C <!--SR:!2023-12-25,13,130-->
9. [paraffin wax](paraffin%20wax.md)::370 °C or above <!--SR:!2024-03-13,110,214-->
10. [bitumen](bitumen.md)::500 °C or above <!--SR:!2024-01-02,209,314-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="e8ff"--><!-- The following content is generated at 2023-12-04T08:18:54.227804+08:00. Any edits will be overridden! -->

1. -40 to -1 °C::[liqueified petroleum gas](liqueified%20petroleum%20gas.md) <!--SR:!2025-04-25,529,310-->
2. -12 to -1 °C::[butane](butane.md) <!--SR:!2024-03-20,274,334-->
3. -1 to 110 °C::[gasoline/petrol](gasoline.md) <!--SR:!2024-01-19,222,314-->
4. 30 to 200 °C::[naphtha](naphtha.md) <!--SR:!2024-03-22,231,274-->
5. 150 to 205 °C::[jet fuel](jet%20fuel.md) <!--SR:!2024-09-09,365,294-->
6. 205 to 260 °C::[kerosene](kerosene.md) <!--SR:!2025-01-21,435,274-->
7. 205 to 290 °C::[fuel oil](fuel%20oil.md) <!--SR:!2024-08-11,337,274-->
8. 260 to 315 °C::[diesel fuel](diesel%20fuel.md) <!--SR:!2024-02-13,157,274-->
9. 370 °C or above::[paraffin wax](paraffin%20wax.md) <!--SR:!2024-01-17,220,314-->
10. 500 °C or above::[bitumen](bitumen.md) <!--SR:!2024-05-18,321,334-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### fraction–use(s)

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="495a"--><!-- The following content is generated at 2023-12-04T08:18:54.205129+08:00. Any edits will be overridden! -->

1. [liqueified petroleum gas](liqueified%20petroleum%20gas.md)::[chemical synthesis](chemical%20synthesis.md), [fuel](fuel.md) <!--SR:!2024-03-16,134,254-->
2. [gasoline/petrol](gasoline.md)::fuel for [motor vehicles](motor%20vehicle.md) <!--SR:!2024-09-05,386,314-->
3. [naphtha](naphtha.md)::production of [plastics](plastic.md) and [town gas](coal%20gas.md) <!--SR:!2024-06-09,228,234-->
4. [jet fuel](jet%20fuel.md)::fuel for [aeroplanes](airplane.md) <!--SR:!2024-07-16,340,294-->
5. [kerosene](kerosene.md)::fuel for domestic use <!--SR:!2024-01-30,217,294-->
6. [fuel oil](fuel%20oil.md)::fuel for [power plants](power%20station.md) and [ships](ship.md) <!--SR:!2024-03-15,224,274-->
7. [diesel fuel](diesel%20fuel.md)::fuel for [buses](bus.md) and [trucks](truck.md) <!--SR:!2024-01-03,192,274-->
8. [paraffin wax](paraffin%20wax.md)::[candles](candle.md), [lubrication](lubrication.md) <!--SR:!2025-02-25,522,314-->
9. [bitumen](bitumen.md)::[road construction](road%20construction.md) <!--SR:!2024-06-10,339,334-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
