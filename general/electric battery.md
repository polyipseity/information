---
aliases:
  - battery
  - battiers
  - electric batteries
  - electric battery
  - electrical batteries
  - electrical battery
tags:
  - flashcards/general/electric_battery
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# electric battery

A __battery__ is {{a source of [electricity](electricity.md) composed of one or multiple [electrochemical cells](electrochemical%20cell.md)}}. When discharging, the positive terminal is {{the [cathode](cathode.md) and the negative terminal is the [anode](anode.md)}}. <!--SR:!2023-10-24,76,230!2024-05-17,320,330-->

[Primary batteries](primary%20battery.md) are {{discharged once only and then [discarded](disposable%20product.md)}}. [Secondary batteries](rechargeable%20battery.md) can be {{discharged and recharged multiple times before being discarded}}. <!--SR:!2024-01-10,213,310!2023-12-10,187,310-->

## types

### comparison

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather
from itertools import chain
headers = 'chemistry', '[anode](anode.md) (-)', '[cathode](cathode.md) (+)', '[electrolyte](electrolyte.md)', 'nominal/max [voltage](voltage.md)', 'properties', 'elaboration',
e = __env__
return chain.from_iterable(await gather(
	memorize_table(
		e.cwf_sects('d923', 'aa92'),
		headers,
		(
			('[alkaline](alkaline%20battery.md)', '[Zn](zinc.md)', '[MnO<sub>2</sub>](manganese%20dioxide.md)', '[KOH](potassium%20hydroxide.md)', '1.15/1.5 V', html_ul('high discharge rate', 'longer [shelf life](shelf%20life.md)', 'low [internal resistance](internal%20resistance.md)', 'slightly more expensive',), 'Usually cylindrical. Suitable for high-drain or continuous-use devices.',),
			('[silver oxide](silver%20oxide%20battery.md)', '[Zn](zinc.md)', '[Ag<sub>2</sub>O](silver%20oxide.md)', '[KOH](potassium%20hydroxide.md)', '1.5/1.6 V', html_ul('expensive', 'lightweight', 'small', 'wide operating temperature range',), 'Usually [button-shaped](button%20cell.md). Suitable for small continuous-use devices.'),
			('[zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride', '[Zn](zinc.md)', '[C](carbon.md) ([graphite](graphite.md)) with [MnO<sub>2</sub>](manganese%20dioxide.md)', '[NH<sub>4</sub>Cl](ammonium%20chloride.md)/[ZnCl<sub>2</sub>](zinc%20chloride.md)', '1.2/1.5 V', html_ul('cheap', 'low performance in high-drain or continuous-use devices', 'short [shelf life](shelf%20life.md)',), 'Usually cylindrical. Suitable for low-drain or intermittent-use devices.',),
		),
		lambda datum: map(cloze, datum),
	),
	memorize_table(
		e.cwf_sects('4214', '6661'),
		headers,
		(
			('[NiMH](nickel–metal%20hydride%20battery.md)', '[H](hydrogen.md)-absorbing [alloy](alloy.md)', '[Ni(OH)<sub>2</sub>](nickel(II)%20hydroxide.md)', '[KOH](potassium%20hydroxide.md)', '/1.2 V', html_ul('expensive', 'high discharge rate', 'high energy density', 'low [internal resistance](internal%20resistance.md)', 'rechargeable up to 500 (180–2000) times'), 'Usually cylindrical. Suitable for high-drain devices.',),
			('[lead–acid](lead–acid%20battery.md)', '[Pb](lead.md)', '[PbO<sub>2</sub>](lead%20dioxide.md)', '[H<sub>2</sub>SO<sub>4</sub>](sulfuric%20acid.md)', '/2.1 V (6 cells: 12 V)', html_ul('cheap [electricity](electricity.md)', 'expensive', 'heavy', 'high [current](electric%20current.md)', 'high discharge rate', '[lead](lead.md) [toxicity](toxicity.md)', 'rechargeable 500 (<350) times',), 'Usually box-shaped. Suitable for [car batteries](automotive%20battery.md) or [uninterruptible power supplies](uninterruptible%20power%20supply.md).',),
			('[lithium-ion](lithium-ion%20battery.md)', '[C](carbon.md) ([graphite](graphite.md) [intercalated](intercalation.md) with [Li](lithium.md))', '[Li](lithium.md) metal [oxide](oxide.md)', '[Li](lithium.md) [salt](salt%20(chemistry).md) in [organic compound](organic%20compound.md) [solvent](solvent.md)', '/3.7 V', html_ul('aging', 'very expensive', 'high discharge rate', 'high energy density', 'lightweight', 'protection circuitry needed for safety', 'rechargeable up to 1200 (400–1200) times', 'susceptibe to [thermal runaway](thermal%20runaway.md) and [explosion](explosion.md)'), 'Usually cylindrical or prismatic. Suitable for portable devices.',),
		),
		lambda datum: map(cloze, datum),
	),
))
```
%%

#### primary batteries

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d923"--><!-- The following content is generated at 2023-03-30T18:11:29.694080+08:00. Any edits will be overridden! -->

> | chemistry | [anode](anode.md) (-) | [cathode](cathode.md) (+) | [electrolyte](electrolyte.md) | nominal/max [voltage](voltage.md) | properties | elaboration |
> |-|-|-|-|-|-|-|
> | {{[alkaline](alkaline%20battery.md)}} | {{[Zn](zinc.md)}} | {{[MnO<sub>2</sub>](manganese%20dioxide.md)}} | {{[KOH](potassium%20hydroxide.md)}} | {{1.15/1.5 V}} | {{<ul><li>high discharge rate</li><li>longer [shelf life](shelf%20life.md)</li><li>low [internal resistance](internal%20resistance.md)</li><li>slightly more expensive</li></ul>}} | {{Usually cylindrical. Suitable for high-drain or continuous-use devices.}} |
> | {{[silver oxide](silver%20oxide%20battery.md)}} | {{[Zn](zinc.md)}} | {{[Ag<sub>2</sub>O](silver%20oxide.md)}} | {{[KOH](potassium%20hydroxide.md)}} | {{1.5/1.6 V}} | {{<ul><li>expensive</li><li>lightweight</li><li>small</li><li>wide operating temperature range</li></ul>}} | {{Usually [button-shaped](button%20cell.md). Suitable for small continuous-use devices.}} |
> | {{[zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride}} | {{[Zn](zinc.md)}} | {{[C](carbon.md) ([graphite](graphite.md)) with [MnO<sub>2</sub>](manganese%20dioxide.md)}} | {{[NH<sub>4</sub>Cl](ammonium%20chloride.md)/[ZnCl<sub>2</sub>](zinc%20chloride.md)}} | {{1.2/1.5 V}} | {{<ul><li>cheap</li><li>low performance in high-drain or continuous-use devices</li><li>short [shelf life](shelf%20life.md)</li></ul>}} | {{Usually cylindrical. Suitable for low-drain or intermittent-use devices.}} | <!--SR:!2023-08-27,111,290!2023-08-24,96,270!2023-12-16,193,310!2023-12-03,185,310!2023-09-29,115,250!2023-08-30,72,190!2024-03-18,272,330!2024-01-18,221,310!2024-06-23,321,290!2023-12-12,189,310!2023-11-19,175,310!2024-04-17,247,270!2023-12-19,154,250!2024-04-22,251,270!2024-04-14,294,330!2024-04-27,305,330!2023-11-10,138,250!2024-08-07,356,290!2023-09-22,95,270!2024-02-10,194,250!2024-04-09,289,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="aa92"--><!-- The following content is generated at 2023-03-30T18:11:29.706415+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[alkaline](alkaline%20battery.md) <!--SR:!2024-04-19,297,330!2024-06-15,344,330-->
2. [alkaline](alkaline%20battery.md)→:::←[silver oxide](silver%20oxide%20battery.md) <!--SR:!2023-12-01,185,310!2023-12-20,197,310-->
3. [silver oxide](silver%20oxide%20battery.md)→:::←[zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride <!--SR:!2023-11-20,176,310!2023-12-17,193,310-->
4. [zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride→:::←_(end)_ <!--SR:!2024-04-18,298,330!2023-12-11,188,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### secondary batteries

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="4214"--><!-- The following content is generated at 2023-03-30T09:32:54.722674+08:00. Any edits will be overridden! -->

> | chemistry | [anode](anode.md) (-) | [cathode](cathode.md) (+) | [electrolyte](electrolyte.md) | nominal/max [voltage](voltage.md) | properties | elaboration |
> |-|-|-|-|-|-|-|
> | {{[NiMH](nickel–metal%20hydride%20battery.md)}} | {{[H](hydrogen.md)-absorbing [alloy](alloy.md)}} | {{[Ni(OH)<sub>2</sub>](nickel(II)%20hydroxide.md)}} | {{[KOH](potassium%20hydroxide.md)}} | {{/1.2 V}} | {{<ul><li>expensive</li><li>high discharge rate</li><li>high energy density</li><li>low [internal resistance](internal%20resistance.md)</li><li>rechargeable up to 500 (180–2000) times</li></ul>}} | {{Usually cylindrical. Suitable for high-drain devices.}} |
> | {{[lead–acid](lead–acid%20battery.md)}} | {{[Pb](lead.md)}} | {{[PbO<sub>2</sub>](lead%20dioxide.md)}} | {{[H<sub>2</sub>SO<sub>4</sub>](sulfuric%20acid.md)}} | {{/2.1 V (6 cells: 12 V)}} | {{<ul><li>cheap [electricity](electricity.md)</li><li>expensive</li><li>heavy</li><li>high [current](electric%20current.md)</li><li>high discharge rate</li><li>[lead](lead.md) [toxicity](toxicity.md)</li><li>rechargeable 500 (&lt;350) times</li></ul>}} | {{Usually box-shaped. Suitable for [car batteries](automotive%20battery.md) or [uninterruptible power supplies](uninterruptible%20power%20supply.md).}} |
> | {{[lithium-ion](lithium-ion%20battery.md)}} | {{[C](carbon.md) ([graphite](graphite.md) [intercalated](intercalation.md) with [Li](lithium.md))}} | {{[Li](lithium.md) metal [oxide](oxide.md)}} | {{[Li](lithium.md) [salt](salt%20(chemistry).md) in [organic compound](organic%20compound.md) [solvent](solvent.md)}} | {{/3.7 V}} | {{<ul><li>aging</li><li>very expensive</li><li>high discharge rate</li><li>high energy density</li><li>lightweight</li><li>protection circuitry needed for safety</li><li>rechargeable up to 1200 (400–1200) times</li><li>susceptibe to [thermal runaway](thermal%20runaway.md) and [explosion](explosion.md)</li></ul>}} | {{Usually cylindrical or prismatic. Suitable for portable devices.}} | <!--SR:!2023-12-13,190,310!2023-08-30,59,230!2023-11-11,139,250!2024-01-25,207,270!2023-09-11,20,170!2023-10-26,73,190!2024-01-04,150,250!2024-05-19,322,330!2024-04-15,295,330!2023-09-08,105,270!2024-04-08,251,270!2024-03-17,271,330!2023-12-10,109,210!2024-03-05,224,290!2024-04-17,297,330!2024-04-18,248,270!2023-09-23,67,230!2024-01-18,175,250!2023-11-19,94,230!2023-09-22,39,210!2024-02-01,234,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="6661"--><!-- The following content is generated at 2023-03-30T09:25:01.110324+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[NiMH](nickel–metal%20hydride%20battery.md) <!--SR:!2024-05-21,324,330!2024-03-11,266,330-->
2. [NiMH](nickel–metal%20hydride%20battery.md)→:::←[lead–acid](lead–acid%20battery.md) <!--SR:!2023-10-19,149,290!2024-05-18,321,330-->
3. [lead–acid](lead–acid%20battery.md)→:::←[lithium-ion](lithium-ion%20battery.md) <!--SR:!2024-03-16,270,330!2024-04-16,296,330-->
4. [lithium-ion](lithium-ion%20battery.md)→:::←_(end)_ <!--SR:!2024-05-20,323,330!2024-03-10,265,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## hazards

Many batteries contain {{[toxic](toxicity.md) materials such as [cadmium](cadmium.md), [lead](lead.md), and [mercury](mercury.md)}}, so {{proper disposal is needed to prevent contamination of the environment}}. {{[Recycling batteries](battery%20recycling.md) and using [secondary batteries](rechargeable%20battery.md)}} can reduce waste as well. <!--SR:!2023-10-11,96,230!2023-11-12,154,290!2024-03-07,262,330-->
