---
aliases: ['battiers', 'battery', 'electric batteries', 'electric battery', 'electrical batteries', 'electrical battery']
---

#academic/chemistry #flashcards/academic/Ee/electric_battery

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# electric battery

A __battery__ is {{a source of [electricity](electricity.md) composed of one or multiple [electrochemical cells](electrochemical%20cell.md)}}. When discharging, the positive terminal is {{the [cathode](cathode.md) and the negative terminal is the [anode](anode.md)}}. <!--SR:!2023-04-03,3,250!2023-04-04,4,270-->

[Primary batteries](primary%20battery.md) are {{discharged once only and then [discarded](disposable%20product.md)}}. [Secondary batteries](rechargeable%20battery.md) can be {{discharged and recharged multiple times before being discarded}}. <!--SR:!2023-04-04,4,270!2023-04-04,4,270-->

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
		(e.cwf_section('d923'), e.cwf_section('aa92'),),
		headers,
		(
			('[alkaline](alkaline%20battery.md)', '[Zn](zinc.md)', '[MnO<sub>2</sub>](manganese%20dioxide.md)', '[KOH](potassium%20hydroxide.md)', '1.15/1.5 V', html_ul2('high discharge rate', 'longer [shelf life](shelf%20life.md)', 'low [internal resistance](internal%20resistance.md)', 'slightly more expensive',), 'Usually cylindrical. Suitable for high-drain or continuous-use devices.',),
			('[silver oxide](silver%20oxide%20battery.md)', '[Zn](zinc.md)', '[Ag<sub>2</sub>O](silver%20oxide.md)', '[KOH](potassium%20hydroxide.md)', '1.5/1.6 V', html_ul2('expensive', 'lightweight', 'small', 'wide operating temperature range',), 'Usually [button-shaped](button%20cell.md). Suitable for small continuous-use devices.'),
			('[zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride', '[Zn](zinc.md)', '[C](carbon.md) ([graphite](graphite.md)) with [MnO<sub>2</sub>](manganese%20dioxide.md)', '[NH<sub>4</sub>Cl](ammonium%20chloride.md)/[ZnCl<sub>2</sub>](zinc%20chloride.md)', '1.2/1.5 V', html_ul2('cheap', 'low performance in high-drain or continuous-use devices', 'short [shelf life](shelf%20life.md)',), 'Usually cylindrical. Suitable for low-drain or intermittent-use devices.',),
		),
		lambda datum: map(cloze, datum),
	),
	memorize_table(
		(e.cwf_section('4214'), e.cwf_section('6661'),),
		headers,
		(
			('[NiMH](nickel–metal%20hydride%20battery.md)', '[H](hydrogen.md)-absorbing [alloy](alloy.md)', '[Ni(OH)<sub>2</sub>](nickel(II)%20hydroxide.md)', '[KOH](potassium%20hydroxide.md)', '/1.2 V', html_ul2('expensive', 'high discharge rate', 'high energy density', 'low [internal resistance](internal%20resistance.md)', 'rechargeable up to 500 (180–2000) times'), 'Usually cylindrical. Suitable for high-drain devices.',),
			('[lead–acid](lead–acid%20battery.md)', '[Pb](lead.md)', '[PbO<sub>2</sub>](lead%20dioxide.md)', '[H<sub>2</sub>SO<sub>4</sub>](sulfuric%20acid.md)', '/2.1 V (6 cells: 12 V)', html_ul2('cheap [electricity](electricity.md)', 'expensive', 'heavy', 'high [current](electric%20current.md)', 'high discharge rate', '[lead](lead.md) [toxicity](toxicity.md)', 'rechargeable 500 (<350) times',), 'Usually box-shaped. Suitable for [car batteries](automotive%20battery.md) or [uninterruptible power supplies](uninterruptible%20power%20supply.md).',),
			('[lithium-ion](lithium-ion%20battery.md)', '[C](carbon.md) ([graphite](graphite.md) [intercalated](intercalation.md) with [Li](lithium.md))', '[Li](lithium.md) metal [oxide](oxide.md)', '[Li](lithium.md) [salt](salt%20(chemistry).md) in [organic compound](organic%20compound.md) [solvent](solvent.md)', '/3.7 V', html_ul2('aging', 'very expensive', 'high discharge rate', 'high energy density', 'lightweight', 'protection circuitry needed for safety', 'rechargeable up to 1200 (400–1200) times', 'susceptibe to [thermal runaway](thermal%20runaway.md) and [explosion](explosion.md)'), 'Usually cylindrical or prismatic. Suitable for portable devices.',),
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
> | {{[zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride}} | {{[Zn](zinc.md)}} | {{[C](carbon.md) ([graphite](graphite.md)) with [MnO<sub>2</sub>](manganese%20dioxide.md)}} | {{[NH<sub>4</sub>Cl](ammonium%20chloride.md)/[ZnCl<sub>2</sub>](zinc%20chloride.md)}} | {{1.2/1.5 V}} | {{<ul><li>cheap</li><li>low performance in high-drain or continuous-use devices</li><li>short [shelf life](shelf%20life.md)</li></ul>}} | {{Usually cylindrical. Suitable for low-drain or intermittent-use devices.}} | <!--SR:!2023-04-01,1,230!2023-04-03,3,250!2023-04-04,4,270!2023-04-04,4,270!2023-04-03,3,250!2023-04-01,1,230!2023-04-04,4,270!2023-04-03,3,250!2023-04-01,1,230!2023-04-04,4,270!2023-04-03,3,250!2023-04-03,3,250!2023-04-01,1,230!2023-04-04,4,270!2023-04-04,4,270!2023-04-04,4,270!2023-04-03,3,250!2023-04-03,3,250!2023-04-01,1,230!2023-04-01,1,230!2023-04-04,4,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="aa92"--><!-- The following content is generated at 2023-03-30T18:11:29.706415+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[alkaline](alkaline%20battery.md) <!--SR:!2023-04-04,4,270!2023-04-04,4,270-->
2. [alkaline](alkaline%20battery.md)→:::←[silver oxide](silver%20oxide%20battery.md) <!--SR:!2023-04-03,3,250!2023-04-04,4,270-->
3. [silver oxide](silver%20oxide%20battery.md)→:::←[zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride <!--SR:!2023-04-03,3,250!2023-04-04,4,270-->
4. [zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride→:::←_(end)_ <!--SR:!2023-04-04,4,270!2023-04-04,4,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### secondary batteries

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="4214"--><!-- The following content is generated at 2023-03-30T09:32:54.722674+08:00. Any edits will be overridden! -->

> | chemistry | [anode](anode.md) (-) | [cathode](cathode.md) (+) | [electrolyte](electrolyte.md) | nominal/max [voltage](voltage.md) | properties | elaboration |
> |-|-|-|-|-|-|-|
> | {{[NiMH](nickel–metal%20hydride%20battery.md)}} | {{[H](hydrogen.md)-absorbing [alloy](alloy.md)}} | {{[Ni(OH)<sub>2</sub>](nickel(II)%20hydroxide.md)}} | {{[KOH](potassium%20hydroxide.md)}} | {{/1.2 V}} | {{<ul><li>expensive</li><li>high discharge rate</li><li>high energy density</li><li>low [internal resistance](internal%20resistance.md)</li><li>rechargeable up to 500 (180–2000) times</li></ul>}} | {{Usually cylindrical. Suitable for high-drain devices.}} |
> | {{[lead–acid](lead–acid%20battery.md)}} | {{[Pb](lead.md)}} | {{[PbO<sub>2</sub>](lead%20dioxide.md)}} | {{[H<sub>2</sub>SO<sub>4</sub>](sulfuric%20acid.md)}} | {{/2.1 V (6 cells: 12 V)}} | {{<ul><li>cheap [electricity](electricity.md)</li><li>expensive</li><li>heavy</li><li>high [current](electric%20current.md)</li><li>high discharge rate</li><li>[lead](lead.md) [toxicity](toxicity.md)</li><li>rechargeable 500 (&lt;350) times</li></ul>}} | {{Usually box-shaped. Suitable for [car batteries](automotive%20battery.md) or [uninterruptible power supplies](uninterruptible%20power%20supply.md).}} |
> | {{[lithium-ion](lithium-ion%20battery.md)}} | {{[C](carbon.md) ([graphite](graphite.md) [intercalated](intercalation.md) with [Li](lithium.md))}} | {{[Li](lithium.md) metal [oxide](oxide.md)}} | {{[Li](lithium.md) [salt](salt%20(chemistry).md) in [organic compound](organic%20compound.md) [solvent](solvent.md)}} | {{/3.7 V}} | {{<ul><li>aging</li><li>very expensive</li><li>high discharge rate</li><li>high energy density</li><li>lightweight</li><li>protection circuitry needed for safety</li><li>rechargeable up to 1200 (400–1200) times</li><li>susceptibe to [thermal runaway](thermal%20runaway.md) and [explosion](explosion.md)</li></ul>}} | {{Usually cylindrical or prismatic. Suitable for portable devices.}} | <!--SR:!2023-04-04,4,270!2023-04-03,3,250!2023-04-03,3,250!2023-04-03,3,250!2023-04-03,3,250!2023-04-03,3,250!2023-04-03,3,250!2023-04-04,4,270!2023-04-04,4,270!2023-04-01,1,230!2023-04-03,3,250!2023-04-04,4,270!2023-04-03,3,250!2023-04-01,1,230!2023-04-04,4,270!2023-04-01,1,230!2023-04-03,3,250!2023-04-03,3,250!2023-04-01,1,230!2023-04-01,1,230!2023-04-03,3,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="6661"--><!-- The following content is generated at 2023-03-30T09:25:01.110324+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[NiMH](nickel–metal%20hydride%20battery.md) <!--SR:!2023-04-04,4,270!2023-04-04,4,270-->
2. [NiMH](nickel–metal%20hydride%20battery.md)→:::←[lead–acid](lead–acid%20battery.md) <!--SR:!2023-04-03,3,250!2023-04-04,4,270-->
3. [lead–acid](lead–acid%20battery.md)→:::←[lithium-ion](lithium-ion%20battery.md) <!--SR:!2023-04-04,4,270!2023-04-04,4,270-->
4. [lithium-ion](lithium-ion%20battery.md)→:::←_(end)_ <!--SR:!2023-04-04,4,270!2023-04-04,4,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## hazards

Many batteries contain {{[toxic](toxicity.md) materials such as [cadmium](cadmium.md), [lead](lead.md), and [mercury](mercury.md)}}, so {{proper disposal is needed to prevent contamination of the environment}}. {{[Recycling batteries](battery%20recycling.md) and using [secondary batteries](rechargeable%20battery.md)}} can reduce waste as well. <!--SR:!2023-04-03,3,250!2023-04-04,4,270!2023-04-04,4,270-->
