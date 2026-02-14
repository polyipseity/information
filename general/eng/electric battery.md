---
aliases:
  - battery
  - battiers
  - electric batteries
  - electric battery
  - electrical batteries
  - electrical battery
tags:
  - flashcard/active/general/eng/electric_battery
  - language/in/English
---

# electric battery

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

A __battery__ is {@{a source of [electricity](electricity.md) composed of one or multiple [electrochemical cells](electrochemical%20cell.md)}@}. When discharging, the positive terminal is {@{the [cathode](cathode.md) and the negative terminal is the [anode](anode.md)}@}.

[Primary batteries](primary%20battery.md) are {@{discharged once only and then [discarded](disposable%20product.md)}@}. [Secondary batteries](rechargeable%20battery.md) can be {@{discharged and recharged multiple times before being discarded}@}.

## types

### comparison

```Python
# pytextgen generate data
from asyncio import gather
from itertools import chain
headers = 'chemistry', '[anode](anode.md) (-)', '[cathode](cathode.md) (+)', '[electrolyte](electrolyte.md)', 'nominal and max [voltage](voltage.md)', 'properties', 'elaboration',
primary_batteries = (
  ('[alkaline](alkaline%20battery.md)', '[Zn](zinc.md)', '[MnO<sub>2</sub>](manganese%20dioxide.md)', '[KOH](potassium%20hydroxide.md)', '1.15 V, 1.5 V', ", ".join(('high discharge rate', 'longer [shelf life](shelf%20life.md)', 'low [internal resistance](internal%20resistance.md)', 'slightly more expensive',)), 'Usually cylindrical. Suitable for high-drain or continuous-use devices.',),
  ('[silver oxide](silver%20oxide%20battery.md)', '[Zn](zinc.md)', '[Ag<sub>2</sub>O](silver%20oxide.md)', '[KOH](potassium%20hydroxide.md)', '1.5 V, 1.6 V', ", ".join(('expensive', 'lightweight', 'small', 'wide operating temperature range',)), 'Usually [button-shaped](button%20cell.md). Suitable for small continuous-use devices.',),
  ('[zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride', '[Zn](zinc.md)', '[C](carbon.md) ([graphite](graphite.md)) with [MnO<sub>2</sub>](manganese%20dioxide.md)', '[NH<sub>4</sub>Cl](ammonium%20chloride.md)/[ZnCl<sub>2</sub>](zinc%20chloride.md)', '1.2 V, 1.5 V', ", ".join(('cheap', 'low performance in high-drain or continuous-use devices', 'short [shelf life](shelf%20life.md)',)), 'Usually cylindrical. Suitable for low-drain or intermittent-use devices.',),
)
secondary_batteries = (
  ('[NiMH](nickel–metal%20hydride%20battery.md)', '[H](hydrogen.md)-absorbing [alloy](alloy.md)', '[Ni(OH)<sub>2</sub>](nickel(II)%20hydroxide.md)', '[KOH](potassium%20hydroxide.md)', '(unavailable), 1.2 V', ", ".join(('expensive', 'high discharge rate', 'high energy density', 'low [internal resistance](internal%20resistance.md)', 'rechargeable up to 180–2000 times',)), 'Usually cylindrical. Suitable for high-drain devices.',),
  ('[lead–acid](lead–acid%20battery.md)', '[Pb](lead.md)', '[PbO<sub>2</sub>](lead%20dioxide.md)', '[H<sub>2</sub>SO<sub>4</sub>](sulfuric%20acid.md)', '(unavailable), 2.1 V; 6 cells: 12 V', ", ".join(('cheap [electricity](electricity.md)', 'expensive', 'heavy', 'high [current](electric%20current.md)', 'high discharge rate', '[lead](lead.md) [toxicity](toxicity.md)', 'rechargeable <350 times',)), 'Usually box-shaped. Suitable for [car batteries](automotive%20battery.md) or [uninterruptible power supplies](uninterruptible%20power%20supply.md).',),
  ('[lithium-ion](lithium-ion%20battery.md)', '[C](carbon.md) ([graphite](graphite.md) [intercalated](intercalation.md) with [Li](lithium.md))', '[Li](lithium.md) metal [oxide](oxide.md)', '[Li](lithium.md) [salt](salt%20(chemistry).md) in [organic compound](organic%20compound.md) [solvent](solvent.md)', '(unavailable), 3.7 V', ", ".join(('aging', 'very expensive', 'high discharge rate', 'high energy density', 'lightweight', 'protection circuitry needed for safety', 'rechargeable up to 400–1200 times', 'susceptibe to [thermal runaway](thermal%20runaway.md) and [explosion](explosion.md)',)), 'Usually cylindrical or prismatic. Suitable for portable devices.',),
)
return chain.from_iterable(await gather(
  memorize_table(
    __env__.cwf_sects('d923', 'aa92',),
    headers, primary_batteries,
  ),
  memorize_map(
    __env__.cwf_sects(None, '98ab', None,),
    items_to_map(*((row[0], row[1]) for row in primary_batteries)),
  ),
  memorize_map(
    __env__.cwf_sects(None, '27ee', None,),
    items_to_map(*((row[0], row[2]) for row in primary_batteries)),
  ),
  memorize_map(
    __env__.cwf_sects(None, '9583', None,),
    items_to_map(*((row[0], row[3]) for row in primary_batteries)),
  ),
  memorize_map(
    __env__.cwf_sects(None, '8104', None,),
    items_to_map(*((row[0], row[4]) for row in primary_batteries)),
  ),
  memorize_map(
    __env__.cwf_sects(None, 'bba9', '209f',),
    items_to_map(*((row[0], row[5]) for row in primary_batteries)),
  ),
  memorize_map(
    __env__.cwf_sects(None, '983e', None,),
    items_to_map(*((row[0], row[6]) for row in primary_batteries)),
  ),
  memorize_table(
    __env__.cwf_sects('4214', '6661',),
    headers, secondary_batteries,
  ),
  memorize_map(
    __env__.cwf_sects(None, '7801', None,),
    items_to_map(*((row[0], row[1]) for row in secondary_batteries)),
  ),
  memorize_map(
    __env__.cwf_sects(None, '38ab', None,),
    items_to_map(*((row[0], row[2]) for row in secondary_batteries)),
  ),
  memorize_map(
    __env__.cwf_sects(None, '863b', None,),
    items_to_map(*((row[0], row[3]) for row in secondary_batteries)),
  ),
  memorize_map(
    __env__.cwf_sects(None, '018e', None,),
    items_to_map(*((row[0], row[4]) for row in secondary_batteries)),
  ),
  memorize_map(
    __env__.cwf_sects(None, '46ff', '99ab',),
    items_to_map(*((row[0], row[5]) for row in secondary_batteries)),
  ),
  memorize_map(
    __env__.cwf_sects(None, '8c52', None,),
    items_to_map(*((row[0], row[6]) for row in secondary_batteries)),
  ),
))
```

#### primary batteries

<!--pytextgen generate section="d923"--><!-- The following content is generated at 2026-01-25T23:32:18.344196+08:00. Any edits will be overridden! -->

> | chemistry                                             | [anode](anode.md) (-) | [cathode](cathode.md) (+)                                                               | [electrolyte](electrolyte.md)                                                     | nominal and max [voltage](voltage.md) | properties                                                                                                                              | elaboration                                                                           |
> | ----------------------------------------------------- | --------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
> | [alkaline](alkaline%20battery.md)                     | [Zn](zinc.md)         | [MnO<sub>2</sub>](manganese%20dioxide.md)                                               | [KOH](potassium%20hydroxide.md)                                                   | 1.15 V, 1.5 V                         | high discharge rate, longer [shelf life](shelf%20life.md), low [internal resistance](internal%20resistance.md), slightly more expensive | Usually cylindrical. Suitable for high-drain or continuous-use devices.               |
> | [silver oxide](silver%20oxide%20battery.md)           | [Zn](zinc.md)         | [Ag<sub>2</sub>O](silver%20oxide.md)                                                    | [KOH](potassium%20hydroxide.md)                                                   | 1.5 V, 1.6 V                          | expensive, lightweight, small, wide operating temperature range                                                                         | Usually [button-shaped](button%20cell.md). Suitable for small continuous-use devices. |
> | [zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride | [Zn](zinc.md)         | [C](carbon.md) ([graphite](graphite.md)) with [MnO<sub>2</sub>](manganese%20dioxide.md) | [NH<sub>4</sub>Cl](ammonium%20chloride.md)/[ZnCl<sub>2</sub>](zinc%20chloride.md) | 1.2 V, 1.5 V                          | cheap, low performance in high-drain or continuous-use devices, short [shelf life](shelf%20life.md)                                     | Usually cylindrical. Suitable for low-drain or intermittent-use devices.              |

<!--/pytextgen-->

<!--pytextgen generate section="aa92"--><!-- The following content is generated at 2024-01-04T20:17:51.686624+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[alkaline](alkaline%20battery.md)
- [alkaline](alkaline%20battery.md)→::@::←[silver oxide](silver%20oxide%20battery.md)
- [silver oxide](silver%20oxide%20battery.md)→::@::←[zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride
- [zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride→::@::←_(end)_

<!--/pytextgen-->

##### chemistry–anode (primary batteries)

<!--pytextgen generate section="98ab"--><!-- The following content is generated at 2024-03-06T23:33:30.624136+08:00. Any edits will be overridden! -->

- [alkaline](alkaline%20battery.md):@:[Zn](zinc.md)
- [silver oxide](silver%20oxide%20battery.md):@:[Zn](zinc.md)
- [zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride:@:[Zn](zinc.md)

<!--/pytextgen-->

##### chemistry–cathode (primary batteries)

<!--pytextgen generate section="27ee"--><!-- The following content is generated at 2024-03-06T23:33:30.705237+08:00. Any edits will be overridden! -->

- [alkaline](alkaline%20battery.md):@:[MnO<sub>2</sub>](manganese%20dioxide.md)
- [silver oxide](silver%20oxide%20battery.md):@:[Ag<sub>2</sub>O](silver%20oxide.md)
- [zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride:@:[C](carbon.md) ([graphite](graphite.md)) with [MnO<sub>2</sub>](manganese%20dioxide.md)

<!--/pytextgen-->

##### chemistry–electrolyte (primary batteries)

<!--pytextgen generate section="9583"--><!-- The following content is generated at 2024-03-06T23:33:30.525732+08:00. Any edits will be overridden! -->

- [alkaline](alkaline%20battery.md):@:[KOH](potassium%20hydroxide.md)
- [silver oxide](silver%20oxide%20battery.md):@:[KOH](potassium%20hydroxide.md)
- [zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride:@:[NH<sub>4</sub>Cl](ammonium%20chloride.md)/[ZnCl<sub>2</sub>](zinc%20chloride.md)

<!--/pytextgen-->

##### chemistry–nominal and max voltage (primary batteries)

<!--pytextgen generate section="8104"--><!-- The following content is generated at 2024-03-08T13:15:49.071658+08:00. Any edits will be overridden! -->

- [alkaline](alkaline%20battery.md):@:1.15 V, 1.5 V
- [silver oxide](silver%20oxide%20battery.md):@:1.5 V, 1.6 V
- [zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride:@:1.2 V, 1.5 V

<!--/pytextgen-->

##### chemistry–properties (primary batteries)

<!--pytextgen generate section="bba9"--><!-- The following content is generated at 2024-03-06T23:36:40.572889+08:00. Any edits will be overridden! -->

- [alkaline](alkaline%20battery.md):@:high discharge rate, longer [shelf life](shelf%20life.md), low [internal resistance](internal%20resistance.md), slightly more expensive
- [silver oxide](silver%20oxide%20battery.md):@:expensive, lightweight, small, wide operating temperature range
- [zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride:@:cheap, low performance in high-drain or continuous-use devices, short [shelf life](shelf%20life.md)

<!--/pytextgen-->

<!--pytextgen generate section="209f"--><!-- The following content is generated at 2024-03-06T23:36:40.557902+08:00. Any edits will be overridden! -->

- high discharge rate, longer [shelf life](shelf%20life.md), low [internal resistance](internal%20resistance.md), slightly more expensive:@:[alkaline](alkaline%20battery.md)
- expensive, lightweight, small, wide operating temperature range:@:[silver oxide](silver%20oxide%20battery.md)
- cheap, low performance in high-drain or continuous-use devices, short [shelf life](shelf%20life.md):@:[zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride

<!--/pytextgen-->

##### chemistry–elaboration (primary batteries)

<!--pytextgen generate section="983e"--><!-- The following content is generated at 2024-03-06T23:33:30.602829+08:00. Any edits will be overridden! -->

- [alkaline](alkaline%20battery.md):@:Usually cylindrical. Suitable for high-drain or continuous-use devices.
- [silver oxide](silver%20oxide%20battery.md):@:Usually [button-shaped](button%20cell.md). Suitable for small continuous-use devices.
- [zinc–carbon](zinc–carbon%20battery.md)/zinc–chloride:@:Usually cylindrical. Suitable for low-drain or intermittent-use devices.

<!--/pytextgen-->

#### secondary batteries

<!--pytextgen generate section="4214"--><!-- The following content is generated at 2026-01-25T23:32:18.402040+08:00. Any edits will be overridden! -->

> | chemistry                                   | [anode](anode.md) (-)                                                                           | [cathode](cathode.md) (+)                       | [electrolyte](electrolyte.md)                                                                                     | nominal and max [voltage](voltage.md) | properties                                                                                                                                                                                                                                   | elaboration                                                                                                                                         |
> | ------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
> | [NiMH](nickel–metal%20hydride%20battery.md) | [H](hydrogen.md)-absorbing [alloy](alloy.md)                                                    | [Ni(OH)<sub>2</sub>](nickel(II)%20hydroxide.md) | [KOH](potassium%20hydroxide.md)                                                                                   | (unavailable), 1.2 V                  | expensive, high discharge rate, high energy density, low [internal resistance](internal%20resistance.md), rechargeable up to 180–2000 times                                                                                                  | Usually cylindrical. Suitable for high-drain devices.                                                                                               |
> | [lead–acid](lead–acid%20battery.md)         | [Pb](lead.md)                                                                                   | [PbO<sub>2</sub>](lead%20dioxide.md)            | [H<sub>2</sub>SO<sub>4</sub>](sulfuric%20acid.md)                                                                 | (unavailable), 2.1 V; 6 cells: 12 V   | cheap [electricity](electricity.md), expensive, heavy, high [current](electric%20current.md), high discharge rate, [lead](lead.md) [toxicity](toxicity.md), rechargeable <350 times                                                          | Usually box-shaped. Suitable for [car batteries](automotive%20battery.md) or [uninterruptible power supplies](uninterruptible%20power%20supply.md). |
> | [lithium-ion](lithium-ion%20battery.md)     | [C](carbon.md) ([graphite](graphite.md) [intercalated](intercalation.md) with [Li](lithium.md)) | [Li](lithium.md) metal [oxide](oxide.md)        | [Li](lithium.md) [salt](salt%20(chemistry).md) in [organic compound](organic%20compound.md) [solvent](solvent.md) | (unavailable), 3.7 V                  | aging, very expensive, high discharge rate, high energy density, lightweight, protection circuitry needed for safety, rechargeable up to 400–1200 times, susceptibe to [thermal runaway](thermal%20runaway.md) and [explosion](explosion.md) | Usually cylindrical or prismatic. Suitable for portable devices.                                                                                    |

<!--/pytextgen-->

<!--pytextgen generate section="6661"--><!-- The following content is generated at 2024-01-04T20:17:51.711635+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[NiMH](nickel–metal%20hydride%20battery.md)
- [NiMH](nickel–metal%20hydride%20battery.md)→::@::←[lead–acid](lead–acid%20battery.md)
- [lead–acid](lead–acid%20battery.md)→::@::←[lithium-ion](lithium-ion%20battery.md)
- [lithium-ion](lithium-ion%20battery.md)→::@::←_(end)_

<!--/pytextgen-->

##### chemistry–anode (secondary batteries)

<!--pytextgen generate section="7801"--><!-- The following content is generated at 2024-03-06T23:33:30.574761+08:00. Any edits will be overridden! -->

- [NiMH](nickel–metal%20hydride%20battery.md):@:[H](hydrogen.md)-absorbing [alloy](alloy.md)
- [lead–acid](lead–acid%20battery.md):@:[Pb](lead.md)
- [lithium-ion](lithium-ion%20battery.md):@:[C](carbon.md) ([graphite](graphite.md) [intercalated](intercalation.md) with [Li](lithium.md))

<!--/pytextgen-->

##### chemistry–cathode (secondary batteries)

<!--pytextgen generate section="38ab"--><!-- The following content is generated at 2024-03-06T23:33:30.754640+08:00. Any edits will be overridden! -->

- [NiMH](nickel–metal%20hydride%20battery.md):@:[Ni(OH)<sub>2</sub>](nickel(II)%20hydroxide.md)
- [lead–acid](lead–acid%20battery.md):@:[PbO<sub>2</sub>](lead%20dioxide.md)
- [lithium-ion](lithium-ion%20battery.md):@:[Li](lithium.md) metal [oxide](oxide.md)

<!--/pytextgen-->

##### chemistry–electrolyte (secondary batteries)

<!--pytextgen generate section="863b"--><!-- The following content is generated at 2024-03-06T23:33:30.773973+08:00. Any edits will be overridden! -->

- [NiMH](nickel–metal%20hydride%20battery.md):@:[KOH](potassium%20hydroxide.md)
- [lead–acid](lead–acid%20battery.md):@:[H<sub>2</sub>SO<sub>4</sub>](sulfuric%20acid.md)
- [lithium-ion](lithium-ion%20battery.md):@:[Li](lithium.md) [salt](salt%20(chemistry).md) in [organic compound](organic%20compound.md) [solvent](solvent.md)

<!--/pytextgen-->

##### chemistry–nominal and max voltage (secondary batteries)

<!--pytextgen generate section="018e"--><!-- The following content is generated at 2024-03-08T13:15:49.087660+08:00. Any edits will be overridden! -->

- [NiMH](nickel–metal%20hydride%20battery.md):@:(unavailable), 1.2 V
- [lead–acid](lead–acid%20battery.md):@:(unavailable), 2.1 V; 6 cells: 12 V
- [lithium-ion](lithium-ion%20battery.md):@:(unavailable), 3.7 V

<!--/pytextgen-->

##### chemistry–properties (secondary batteries)

<!--pytextgen generate section="46ff"--><!-- The following content is generated at 2024-03-06T23:36:40.541906+08:00. Any edits will be overridden! -->

- [NiMH](nickel–metal%20hydride%20battery.md):@:expensive, high discharge rate, high energy density, low [internal resistance](internal%20resistance.md), rechargeable up to 180–2000 times
- [lead–acid](lead–acid%20battery.md):@:cheap [electricity](electricity.md), expensive, heavy, high [current](electric%20current.md), high discharge rate, [lead](lead.md) [toxicity](toxicity.md), rechargeable <350 times
- [lithium-ion](lithium-ion%20battery.md):@:aging, very expensive, high discharge rate, high energy density, lightweight, protection circuitry needed for safety, rechargeable up to 400–1200 times, susceptibe to [thermal runaway](thermal%20runaway.md) and [explosion](explosion.md)

<!--/pytextgen-->

<!--pytextgen generate section="99ab"--><!-- The following content is generated at 2024-03-06T23:36:40.619769+08:00. Any edits will be overridden! -->

- expensive, high discharge rate, high energy density, low [internal resistance](internal%20resistance.md), rechargeable up to 180–2000 times:@:[NiMH](nickel–metal%20hydride%20battery.md)
- cheap [electricity](electricity.md), expensive, heavy, high [current](electric%20current.md), high discharge rate, [lead](lead.md) [toxicity](toxicity.md), rechargeable <350 times:@:[lead–acid](lead–acid%20battery.md)
- aging, very expensive, high discharge rate, high energy density, lightweight, protection circuitry needed for safety, rechargeable up to 400–1200 times, susceptibe to [thermal runaway](thermal%20runaway.md) and [explosion](explosion.md):@:[lithium-ion](lithium-ion%20battery.md)

<!--/pytextgen-->

##### chemistry–elaboration (secondary batteries)

<!--pytextgen generate section="8c52"--><!-- The following content is generated at 2024-03-06T23:33:30.718238+08:00. Any edits will be overridden! -->

- [NiMH](nickel–metal%20hydride%20battery.md):@:Usually cylindrical. Suitable for high-drain devices.
- [lead–acid](lead–acid%20battery.md):@:Usually box-shaped. Suitable for [car batteries](automotive%20battery.md) or [uninterruptible power supplies](uninterruptible%20power%20supply.md).
- [lithium-ion](lithium-ion%20battery.md):@:Usually cylindrical or prismatic. Suitable for portable devices.

<!--/pytextgen-->

## hazards

Many batteries contain {@{[toxic](toxicity.md) materials such as [cadmium](cadmium.md), [lead](lead.md), and [mercury](mercury.md)}@}, so {@{proper disposal is needed to prevent contamination of the environment}@}. {@{[Recycling batteries](battery%20recycling.md) and using [secondary batteries](rechargeable%20battery.md)}@} can reduce waste as well.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/electric_battery) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
