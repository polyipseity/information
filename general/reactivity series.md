---
aliases:
  - activity series
  - reactivity series
tags:
  - flashcard/general/reactivity_series
  - language/in/English
---

# reactivity series

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```

%%

A __reactivity series__ is {{a progression of series of [metals](metal.md) arranged by their [reactivity](reactivity%20(chemistry).md)}}. <!--SR:!2024-03-23,232,270-->

## data

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain

r_water = "reacts with cold [water](water.md)"
r_mg = "reacts very slowly with cold [water](water.md), rapidly with boiling water, and very vigorously with [acids](acid.md)"
r_steam = "reacts with [steam](steam.md) and [acids](acid.md)"
r_ti = "reacts with concentrated [mineral acids](mineral%20acid.md)"
r_acid = "reacts with [acids](acid.md), poorly with [steam](steam.md)"
r_cu = "reacts slowly with [air](air.md)"
r_ox = "may react with some strong [oxidizing agents](oxidizing%20agent.md)"
e_ele = "[electrolysis](electrolysis.md)"
e_ti = "[pyrometallurgical](pyrometallurgy.md) extraction using [magnesium](magnesium.md)"
e_smelt = "[smelting](smelting.md) with [coke](coke%20(fuel).md)"
e_cr = "[aluminothermic reaction](aluminothermic%20reaction.md)"
e_phy = "heat or physical extraction"

headers = ("[metal](metal.md)", "[ion](ion.md)", "[reactivity](reactivity%20(chemistry).md)", "[extraction](extractive%20metallurgy.md)")
table = (
  ("[caesium](caesium.md)", "Cs<sup>+</sup>", r_water, e_ele,),
  ("[rubidium](rubidium.md)", "Rb<sup>+</sup>", r_water, e_ele,),
  ("[potassium](potassium.md)", "K<sup>+</sup>", r_water, e_ele,),
  ("[sodium](sodium.md)", "Na<sup>+</sup>", r_water, e_ele,),
  ("[lithium](lithium.md)", "Li<sup>+</sup>", r_water, e_ele,),
  ("[barium](barium.md)", "Ba<sup>2+</sup>", r_water, e_ele,),
  ("[strontium](strontium.md)", "Sr<sup>2+</sup>", r_water, e_ele,),
  ("[calcium](calcium.md)", "Ca<sup>2+</sup>", r_water, e_ele,),
  ("[magnesium](magnesium.md)", "Mg<sup>2+</sup>", r_mg, e_ele,),
  ("[beryllium](beryllium.md)", "Be<sup>2+</sup>", r_steam, e_ele,),
  ("[aluminium](aluminium.md)", "Al<sup>3+</sup>", r_steam, e_ele,),
  ("[titanium](titanium.md)", "Ti<sup>4+</sup>", r_ti, e_ti,),
  ("[manganese](manganese.md)", "Mn<sup>2+</sup>", r_acid, e_smelt,),
  ("[zinc](zinc.md)", "Zn<sup>2+</sup>", r_acid, e_smelt,),
  ("[chromium](chromium.md)", "Cr<sup>3+</sup>", r_acid, e_cr,),
  ("[iron](iron.md)", "Fe<sup>2+</sup>", r_acid, e_smelt,),
  ("[cadmium](cadmium.md)", "Cd<sup>2+</sup>", r_acid, e_smelt,),
  ("[cobalt](cobalt.md)", "Co<sup>2+</sup>", r_acid, e_smelt,),
  ("[nickel](nickel.md)", "Ni<sup>2+</sup>", r_acid, e_smelt,),
  ("[tin](tin.md)", "Sn<sup>2+</sup>", r_acid, e_smelt,),
  ("[lead](lead.md)", "Pb<sup>2+</sup>", r_acid, e_smelt,),
  ("[antimony](antimony.md)", "Sb<sup>3+</sup>", r_ox, e_phy,),
  ("[bismuth](bismuth.md)", "Bi<sup>3+</sup>", r_ox, e_phy,),
  ("[copper](copper.md)", "Cu<sup>2+</sup>", r_cu, e_phy,),
  ("[tungsten](tungsten.md)", "W<sup>3+</sup>", r_ox, e_phy,),
  ("[mercury](mercury%20(element).md)", "Hg<sup>2+</sup>", r_ox, e_phy,),
  ("[silver](silver.md)", "Ag<sup>+</sup>", r_ox, e_phy,),
  ("[gold](gold.md)", "Au<sup>3+</sup>", r_ox, e_phy,),
  ("[platinum](platinum.md)", "Pt<sup>4+</sup>", r_ox, e_phy,),
)

return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects("a2994d", "299018"), headers, table,
    pretext="most reactive", posttext="least reactive",
  ),
  memorize_map(
    __env__.cwf_sects(None, "1e32", "8912",),
    items_to_map(*((entry[0], entry[1],) for entry in table if entry[1])),
  ),
  memorize_map(
    __env__.cwf_sects(None, "22ba", "671a",),
    items_to_map(*((entry[0], entry[2],) for entry in table if entry[2])),
  ),
  memorize_map(
    __env__.cwf_sects(None, "ba24", "ee23",),
    items_to_map(*((entry[0], entry[3],) for entry in table if entry[3])),
  ),
))
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a2994d"--><!-- The following content is generated at 2024-02-17T20:43:15.082424+08:00. Any edits will be overridden! -->

> | [metal](metal.md) | [ion](ion.md) | [reactivity](reactivity%20(chemistry).md) | [extraction](extractive%20metallurgy.md) |
> |-|-|-|-|
> | [caesium](caesium.md) | Cs<sup>+</sup> | reacts with cold [water](water.md) | [electrolysis](electrolysis.md) |
> | [rubidium](rubidium.md) | Rb<sup>+</sup> | reacts with cold [water](water.md) | [electrolysis](electrolysis.md) |
> | [potassium](potassium.md) | K<sup>+</sup> | reacts with cold [water](water.md) | [electrolysis](electrolysis.md) |
> | [sodium](sodium.md) | Na<sup>+</sup> | reacts with cold [water](water.md) | [electrolysis](electrolysis.md) |
> | [lithium](lithium.md) | Li<sup>+</sup> | reacts with cold [water](water.md) | [electrolysis](electrolysis.md) |
> | [barium](barium.md) | Ba<sup>2+</sup> | reacts with cold [water](water.md) | [electrolysis](electrolysis.md) |
> | [strontium](strontium.md) | Sr<sup>2+</sup> | reacts with cold [water](water.md) | [electrolysis](electrolysis.md) |
> | [calcium](calcium.md) | Ca<sup>2+</sup> | reacts with cold [water](water.md) | [electrolysis](electrolysis.md) |
> | [magnesium](magnesium.md) | Mg<sup>2+</sup> | reacts very slowly with cold [water](water.md), rapidly with boiling water, and very vigorously with [acids](acid.md) | [electrolysis](electrolysis.md) |
> | [beryllium](beryllium.md) | Be<sup>2+</sup> | reacts with [steam](steam.md) and [acids](acid.md) | [electrolysis](electrolysis.md) |
> | [aluminium](aluminium.md) | Al<sup>3+</sup> | reacts with [steam](steam.md) and [acids](acid.md) | [electrolysis](electrolysis.md) |
> | [titanium](titanium.md) | Ti<sup>4+</sup> | reacts with concentrated [mineral acids](mineral%20acid.md) | [pyrometallurgical](pyrometallurgy.md) extraction using [magnesium](magnesium.md) |
> | [manganese](manganese.md) | Mn<sup>2+</sup> | reacts with [acids](acid.md), poorly with [steam](steam.md) | [smelting](smelting.md) with [coke](coke%20(fuel).md) |
> | [zinc](zinc.md) | Zn<sup>2+</sup> | reacts with [acids](acid.md), poorly with [steam](steam.md) | [smelting](smelting.md) with [coke](coke%20(fuel).md) |
> | [chromium](chromium.md) | Cr<sup>3+</sup> | reacts with [acids](acid.md), poorly with [steam](steam.md) | [aluminothermic reaction](aluminothermic%20reaction.md) |
> | [iron](iron.md) | Fe<sup>2+</sup> | reacts with [acids](acid.md), poorly with [steam](steam.md) | [smelting](smelting.md) with [coke](coke%20(fuel).md) |
> | [cadmium](cadmium.md) | Cd<sup>2+</sup> | reacts with [acids](acid.md), poorly with [steam](steam.md) | [smelting](smelting.md) with [coke](coke%20(fuel).md) |
> | [cobalt](cobalt.md) | Co<sup>2+</sup> | reacts with [acids](acid.md), poorly with [steam](steam.md) | [smelting](smelting.md) with [coke](coke%20(fuel).md) |
> | [nickel](nickel.md) | Ni<sup>2+</sup> | reacts with [acids](acid.md), poorly with [steam](steam.md) | [smelting](smelting.md) with [coke](coke%20(fuel).md) |
> | [tin](tin.md) | Sn<sup>2+</sup> | reacts with [acids](acid.md), poorly with [steam](steam.md) | [smelting](smelting.md) with [coke](coke%20(fuel).md) |
> | [lead](lead.md) | Pb<sup>2+</sup> | reacts with [acids](acid.md), poorly with [steam](steam.md) | [smelting](smelting.md) with [coke](coke%20(fuel).md) |
> | [antimony](antimony.md) | Sb<sup>3+</sup> | may react with some strong [oxidizing agents](oxidizing%20agent.md) | heat or physical extraction |
> | [bismuth](bismuth.md) | Bi<sup>3+</sup> | may react with some strong [oxidizing agents](oxidizing%20agent.md) | heat or physical extraction |
> | [copper](copper.md) | Cu<sup>2+</sup> | reacts slowly with [air](air.md) | heat or physical extraction |
> | [tungsten](tungsten.md) | W<sup>3+</sup> | may react with some strong [oxidizing agents](oxidizing%20agent.md) | heat or physical extraction |
> | [mercury](mercury%20(element).md) | Hg<sup>2+</sup> | may react with some strong [oxidizing agents](oxidizing%20agent.md) | heat or physical extraction |
> | [silver](silver.md) | Ag<sup>+</sup> | may react with some strong [oxidizing agents](oxidizing%20agent.md) | heat or physical extraction |
> | [gold](gold.md) | Au<sup>3+</sup> | may react with some strong [oxidizing agents](oxidizing%20agent.md) | heat or physical extraction |
> | [platinum](platinum.md) | Pt<sup>4+</sup> | may react with some strong [oxidizing agents](oxidizing%20agent.md) | heat or physical extraction |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="299018"--><!-- The following content is generated at 2024-02-18T15:03:20.984589+08:00. Any edits will be overridden! -->

- _(most reactive)_→:::←[caesium](caesium.md) <!--SR:!2024-03-03,258,330!2024-03-06,260,330-->
- [caesium](caesium.md)→:::←[rubidium](rubidium.md) <!--SR:!2024-10-25,391,270!2025-02-13,397,250-->
- [rubidium](rubidium.md)→:::←[potassium](potassium.md) <!--SR:!2025-01-07,392,250!2024-07-12,286,250-->
- [potassium](potassium.md)→:::←[sodium](sodium.md) <!--SR:!2024-05-06,293,290!2025-11-14,655,310-->
- [sodium](sodium.md)→:::←[lithium](lithium.md) <!--SR:!2024-05-12,84,250!2024-05-25,285,290-->
- [lithium](lithium.md)→:::←[barium](barium.md) <!--SR:!2024-10-24,314,230!2024-06-18,139,230-->
- [barium](barium.md)→:::←[strontium](strontium.md) <!--SR:!2025-06-09,520,270!2024-06-03,167,250-->
- [strontium](strontium.md)→:::←[calcium](calcium.md) <!--SR:!2025-01-09,360,230!2024-10-15,347,270-->
- [calcium](calcium.md)→:::←[magnesium](magnesium.md) <!--SR:!2025-01-25,377,270!2024-04-07,153,270-->
- [magnesium](magnesium.md)→:::←[beryllium](beryllium.md) <!--SR:!2024-03-01,91,290!2024-07-23,341,290-->
- [beryllium](beryllium.md)→:::←[aluminium](aluminium.md) <!--SR:!2024-03-10,56,230!2024-05-01,92,230-->
- [aluminium](aluminium.md)→:::←[titanium](titanium.md) <!--SR:!2024-03-23,222,250!2024-04-30,95,250-->
- [titanium](titanium.md)→:::←[manganese](manganese.md) <!--SR:!2024-12-07,372,250!2024-06-29,294,270-->
- [manganese](manganese.md)→:::←[zinc](zinc.md) <!--SR:!2024-03-13,22,150!2024-03-13,61,210-->
- [zinc](zinc.md)→:::←[chromium](chromium.md) <!--SR:!2024-04-13,217,230!2024-04-18,167,230-->
- [chromium](chromium.md)→:::←[iron](iron.md) <!--SR:!2024-06-15,280,290!2024-04-15,68,190-->
- [iron](iron.md)→:::←[cadmium](cadmium.md) <!--SR:!2024-10-08,368,290!2024-04-07,237,270-->
- [cadmium](cadmium.md)→:::←[cobalt](cobalt.md) <!--SR:!2024-03-09,35,210!2024-03-13,37,150-->
- [cobalt](cobalt.md)→:::←[nickel](nickel.md) <!--SR:!2024-10-03,332,250!2024-06-10,151,230-->
- [nickel](nickel.md)→:::←[tin](tin.md) <!--SR:!2024-11-01,352,250!2024-04-03,49,190-->
- [tin](tin.md)→:::←[lead](lead.md) <!--SR:!2025-02-24,419,250!2025-07-07,539,250-->
- [lead](lead.md)→:::←[antimony](antimony.md) <!--SR:!2024-03-23,38,210!2024-06-15,267,250-->
- [antimony](antimony.md)→:::←[bismuth](bismuth.md) <!--SR:!2024-12-31,415,270!2025-11-08,643,290-->
- [bismuth](bismuth.md)→:::←[copper](copper.md) <!--SR:!2024-05-03,96,250!2025-01-25,397,250-->
- [copper](copper.md)→:::←[tungsten](tungsten.md) <!--SR:!2024-03-08,220,270!2025-02-02,436,270-->
- [tungsten](tungsten.md)→:::←[mercury](mercury%20(element).md) <!--SR:!2024-08-30,262,250!2024-03-16,168,230-->
- [mercury](mercury%20(element).md)→:::←[silver](silver.md) <!--SR:!2024-03-17,266,330!2024-04-24,297,330-->
- [silver](silver.md)→:::←[gold](gold.md) <!--SR:!2026-06-26,904,330!2024-05-09,312,330-->
- [gold](gold.md)→:::←[platinum](platinum.md) <!--SR:!2024-04-28,301,330!2027-04-17,1146,350-->
- [platinum](platinum.md)→:::←_(least reactive)_ <!--SR:!2027-03-09,1114,350!2024-03-21,270,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### metal–ion

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1e32"--><!-- The following content is generated at 2024-02-17T20:43:14.994069+08:00. Any edits will be overridden! -->

- [caesium](caesium.md)::Cs<sup>+</sup> <!--SR:!2026-12-21,1055,350-->
- [rubidium](rubidium.md)::Rb<sup>+</sup> <!--SR:!2024-11-27,411,290-->
- [potassium](potassium.md)::K<sup>+</sup> <!--SR:!2027-01-16,1077,350-->
- [sodium](sodium.md)::Na<sup>+</sup> <!--SR:!2027-02-19,1104,350-->
- [lithium](lithium.md)::Li<sup>+</sup> <!--SR:!2024-04-03,281,330-->
- [barium](barium.md)::Ba<sup>2+</sup> <!--SR:!2024-03-09,264,330-->
- [strontium](strontium.md)::Sr<sup>2+</sup> <!--SR:!2027-04-10,1140,350-->
- [calcium](calcium.md)::Ca<sup>2+</sup> <!--SR:!2024-05-19,317,330-->
- [magnesium](magnesium.md)::Mg<sup>2+</sup> <!--SR:!2024-04-03,283,330-->
- [beryllium](beryllium.md)::Be<sup>2+</sup> <!--SR:!2025-04-06,511,310-->
- [aluminium](aluminium.md)::Al<sup>3+</sup> <!--SR:!2024-03-22,271,330-->
- [titanium](titanium.md)::Ti<sup>4+</sup> <!--SR:!2025-03-21,498,310-->
- [manganese](manganese.md)::Mn<sup>2+</sup> <!--SR:!2025-05-26,548,310-->
- [zinc](zinc.md)::Zn<sup>2+</sup> <!--SR:!2026-04-22,848,330-->
- [chromium](chromium.md)::Cr<sup>3+</sup> <!--SR:!2027-03-20,1123,350-->
- [iron](iron.md)::Fe<sup>2+</sup> <!--SR:!2026-04-29,853,330-->
- [cadmium](cadmium.md)::Cd<sup>2+</sup> <!--SR:!2024-05-05,308,330-->
- [cobalt](cobalt.md)::Co<sup>2+</sup> <!--SR:!2024-05-07,310,330-->
- [nickel](nickel.md)::Ni<sup>2+</sup> <!--SR:!2024-03-07,262,330-->
- [tin](tin.md)::Sn<sup>2+</sup> <!--SR:!2024-05-18,316,330-->
- [lead](lead.md)::Pb<sup>2+</sup> <!--SR:!2026-05-15,866,330-->
- [antimony](antimony.md)::Sb<sup>3+</sup> <!--SR:!2024-05-07,72,210-->
- [bismuth](bismuth.md)::Bi<sup>3+</sup> <!--SR:!2024-07-30,351,290-->
- [copper](copper.md)::Cu<sup>2+</sup> <!--SR:!2025-04-11,504,310-->
- [tungsten](tungsten.md)::W<sup>3+</sup> <!--SR:!2025-07-09,575,310-->
- [mercury](mercury%20(element).md)::Hg<sup>2+</sup> <!--SR:!2024-04-20,54,250-->
- [silver](silver.md)::Ag<sup>+</sup> <!--SR:!2025-07-03,572,310-->
- [gold](gold.md)::Au<sup>3+</sup> <!--SR:!2025-04-23,526,310-->
- [platinum](platinum.md)::Pt<sup>4+</sup> <!--SR:!2025-03-27,498,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="8912"--><!-- The following content is generated at 2024-02-17T20:43:15.136674+08:00. Any edits will be overridden! -->

- Cs<sup>+</sup>::[caesium](caesium.md) <!--SR:!2024-03-10,17,325-->
- Rb<sup>+</sup>::[rubidium](rubidium.md) <!--SR:!2024-03-09,16,325-->
- K<sup>+</sup>::[potassium](potassium.md) <!--SR:!2024-03-09,16,327-->
- Na<sup>+</sup>::[sodium](sodium.md) <!--SR:!2024-03-12,19,325-->
- Li<sup>+</sup>::[lithium](lithium.md) <!--SR:!2024-03-09,16,327-->
- Ba<sup>2+</sup>::[barium](barium.md) <!--SR:!2024-03-08,15,327-->
- Sr<sup>2+</sup>::[strontium](strontium.md) <!--SR:!2024-03-08,15,325-->
- Ca<sup>2+</sup>::[calcium](calcium.md) <!--SR:!2024-03-11,18,325-->
- Mg<sup>2+</sup>::[magnesium](magnesium.md) <!--SR:!2024-03-09,16,325-->
- Be<sup>2+</sup>::[beryllium](beryllium.md) <!--SR:!2024-03-08,15,327-->
- Al<sup>3+</sup>::[aluminium](aluminium.md) <!--SR:!2024-03-08,15,325-->
- Ti<sup>4+</sup>::[titanium](titanium.md) <!--SR:!2024-03-11,18,325-->
- Mn<sup>2+</sup>::[manganese](manganese.md) <!--SR:!2024-03-12,19,325-->
- Zn<sup>2+</sup>::[zinc](zinc.md) <!--SR:!2024-03-08,15,325-->
- Cr<sup>3+</sup>::[chromium](chromium.md) <!--SR:!2024-03-11,18,327-->
- Fe<sup>2+</sup>::[iron](iron.md) <!--SR:!2024-03-10,17,325-->
- Cd<sup>2+</sup>::[cadmium](cadmium.md) <!--SR:!2024-03-10,17,325-->
- Co<sup>2+</sup>::[cobalt](cobalt.md) <!--SR:!2024-03-12,19,325-->
- Ni<sup>2+</sup>::[nickel](nickel.md) <!--SR:!2024-03-10,17,325-->
- Sn<sup>2+</sup>::[tin](tin.md) <!--SR:!2024-03-08,15,327-->
- Pb<sup>2+</sup>::[lead](lead.md) <!--SR:!2024-03-11,18,325-->
- Sb<sup>3+</sup>::[antimony](antimony.md) <!--SR:!2024-03-12,19,325-->
- Bi<sup>3+</sup>::[bismuth](bismuth.md) <!--SR:!2024-03-12,19,325-->
- Cu<sup>2+</sup>::[copper](copper.md) <!--SR:!2024-03-10,17,327-->
- W<sup>3+</sup>::[tungsten](tungsten.md) <!--SR:!2024-03-09,16,325-->
- Hg<sup>2+</sup>::[mercury](mercury%20(element).md) <!--SR:!2024-03-11,18,325-->
- Ag<sup>+</sup>::[silver](silver.md) <!--SR:!2024-03-10,17,327-->
- Au<sup>3+</sup>::[gold](gold.md) <!--SR:!2024-03-11,18,327-->
- Pt<sup>4+</sup>::[platinum](platinum.md) <!--SR:!2024-03-12,19,325-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### metal–reactivity

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="22ba"--><!-- The following content is generated at 2024-02-17T20:43:15.064424+08:00. Any edits will be overridden! -->

- [caesium](caesium.md)::reacts with cold [water](water.md) <!--SR:!2024-04-02,282,330-->
- [rubidium](rubidium.md)::reacts with cold [water](water.md) <!--SR:!2024-05-03,306,330-->
- [potassium](potassium.md)::reacts with cold [water](water.md) <!--SR:!2027-03-25,1127,350-->
- [sodium](sodium.md)::reacts with cold [water](water.md) <!--SR:!2026-03-14,773,330-->
- [lithium](lithium.md)::reacts with cold [water](water.md) <!--SR:!2026-04-15,831,330-->
- [barium](barium.md)::reacts with cold [water](water.md) <!--SR:!2025-03-15,495,310-->
- [strontium](strontium.md)::reacts with cold [water](water.md) <!--SR:!2025-03-20,497,310-->
- [calcium](calcium.md)::reacts with cold [water](water.md) <!--SR:!2025-08-04,539,270-->
- [magnesium](magnesium.md)::reacts very slowly with cold [water](water.md), rapidly with boiling water, and very vigorously with [acids](acid.md) <!--SR:!2024-03-29,44,170-->
- [beryllium](beryllium.md)::reacts with [steam](steam.md) and [acids](acid.md) <!--SR:!2024-03-16,57,170-->
- [aluminium](aluminium.md)::reacts with [steam](steam.md) and [acids](acid.md) <!--SR:!2024-03-11,27,130-->
- [titanium](titanium.md)::reacts with concentrated [mineral acids](mineral%20acid.md) <!--SR:!2025-02-22,417,250-->
- [manganese](manganese.md)::reacts with [acids](acid.md), poorly with [steam](steam.md) <!--SR:!2024-03-08,11,130-->
- [zinc](zinc.md)::reacts with [acids](acid.md), poorly with [steam](steam.md) <!--SR:!2024-06-30,295,270-->
- [chromium](chromium.md)::reacts with [acids](acid.md), poorly with [steam](steam.md) <!--SR:!2024-04-30,252,270-->
- [iron](iron.md)::reacts with [acids](acid.md), poorly with [steam](steam.md) <!--SR:!2024-12-06,399,290-->
- [cadmium](cadmium.md)::reacts with [acids](acid.md), poorly with [steam](steam.md) <!--SR:!2025-04-01,507,310-->
- [cobalt](cobalt.md)::reacts with [acids](acid.md), poorly with [steam](steam.md) <!--SR:!2025-03-22,477,290-->
- [nickel](nickel.md)::reacts with [acids](acid.md), poorly with [steam](steam.md) <!--SR:!2025-06-25,566,310-->
- [tin](tin.md)::reacts with [acids](acid.md), poorly with [steam](steam.md) <!--SR:!2024-08-20,361,290-->
- [lead](lead.md)::reacts with [acids](acid.md), poorly with [steam](steam.md) <!--SR:!2026-10-19,973,330-->
- [antimony](antimony.md)::may react with some strong [oxidizing agents](oxidizing%20agent.md) <!--SR:!2024-03-17,90,290-->
- [bismuth](bismuth.md)::may react with some strong [oxidizing agents](oxidizing%20agent.md) <!--SR:!2024-06-08,112,290-->
- [copper](copper.md)::reacts slowly with [air](air.md) <!--SR:!2026-04-18,783,290-->
- [tungsten](tungsten.md)::may react with some strong [oxidizing agents](oxidizing%20agent.md) <!--SR:!2026-05-29,824,330-->
- [mercury](mercury%20(element).md)::may react with some strong [oxidizing agents](oxidizing%20agent.md) <!--SR:!2024-03-19,268,330-->
- [silver](silver.md)::may react with some strong [oxidizing agents](oxidizing%20agent.md) <!--SR:!2027-03-31,1132,350-->
- [gold](gold.md)::may react with some strong [oxidizing agents](oxidizing%20agent.md) <!--SR:!2024-03-04,259,330-->
- [platinum](platinum.md)::may react with some strong [oxidizing agents](oxidizing%20agent.md) <!--SR:!2024-04-02,280,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="671a"--><!-- The following content is generated at 2024-02-17T20:43:15.023699+08:00. Any edits will be overridden! -->

- reacts with cold [water](water.md)::[caesium](caesium.md), [rubidium](rubidium.md), [potassium](potassium.md), [sodium](sodium.md), [lithium](lithium.md), [barium](barium.md), [strontium](strontium.md), [calcium](calcium.md) <!--SR:!2024-03-05,6,225-->
- reacts very slowly with cold [water](water.md), rapidly with boiling water, and very vigorously with [acids](acid.md)::[magnesium](magnesium.md) <!--SR:!2024-03-09,16,325-->
- reacts with [steam](steam.md) and [acids](acid.md)::[beryllium](beryllium.md), [aluminium](aluminium.md) <!--SR:!2024-03-01,8,267-->
- reacts with concentrated [mineral acids](mineral%20acid.md)::[titanium](titanium.md) <!--SR:!2024-03-03,11,305-->
- reacts with [acids](acid.md), poorly with [steam](steam.md)::[manganese](manganese.md), [zinc](zinc.md), [chromium](chromium.md), [iron](iron.md), [cadmium](cadmium.md), [cobalt](cobalt.md), [nickel](nickel.md), [tin](tin.md), [lead](lead.md) <!--SR:!2024-03-09,9,245-->
- may react with some strong [oxidizing agents](oxidizing%20agent.md)::[antimony](antimony.md), [bismuth](bismuth.md), [tungsten](tungsten.md), [mercury](mercury%20(element).md), [silver](silver.md), [gold](gold.md), [platinum](platinum.md) <!--SR:!2024-03-24,24,285-->
- reacts slowly with [air](air.md)::[copper](copper.md) <!--SR:!2024-03-09,16,325-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### metal–extraction

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ba24"--><!-- The following content is generated at 2024-02-17T20:43:15.115428+08:00. Any edits will be overridden! -->

- [caesium](caesium.md)::[electrolysis](electrolysis.md) <!--SR:!2024-04-21,294,330-->
- [rubidium](rubidium.md)::[electrolysis](electrolysis.md) <!--SR:!2024-04-22,295,330-->
- [potassium](potassium.md)::[electrolysis](electrolysis.md) <!--SR:!2026-04-28,801,330-->
- [sodium](sodium.md)::[electrolysis](electrolysis.md) <!--SR:!2024-05-31,329,330-->
- [lithium](lithium.md)::[electrolysis](electrolysis.md) <!--SR:!2026-01-26,782,330-->
- [barium](barium.md)::[electrolysis](electrolysis.md) <!--SR:!2024-05-08,311,330-->
- [strontium](strontium.md)::[electrolysis](electrolysis.md) <!--SR:!2024-04-29,302,330-->
- [calcium](calcium.md)::[electrolysis](electrolysis.md) <!--SR:!2024-03-31,278,330-->
- [magnesium](magnesium.md)::[electrolysis](electrolysis.md) <!--SR:!2024-05-11,258,270-->
- [beryllium](beryllium.md)::[electrolysis](electrolysis.md) <!--SR:!2024-03-06,261,330-->
- [aluminium](aluminium.md)::[electrolysis](electrolysis.md) <!--SR:!2024-10-07,250,230-->
- [titanium](titanium.md)::[pyrometallurgical](pyrometallurgy.md) extraction using [magnesium](magnesium.md) <!--SR:!2024-03-10,28,150-->
- [manganese](manganese.md)::[smelting](smelting.md) with [coke](coke%20(fuel).md) <!--SR:!2024-03-07,41,190-->
- [zinc](zinc.md)::[smelting](smelting.md) with [coke](coke%20(fuel).md) <!--SR:!2024-11-16,379,290-->
- [chromium](chromium.md)::[aluminothermic reaction](aluminothermic%20reaction.md) <!--SR:!2024-03-02,207,270-->
- [iron](iron.md)::[smelting](smelting.md) with [coke](coke%20(fuel).md) <!--SR:!2024-04-01,251,310-->
- [cadmium](cadmium.md)::[smelting](smelting.md) with [coke](coke%20(fuel).md) <!--SR:!2025-08-22,610,310-->
- [cobalt](cobalt.md)::[smelting](smelting.md) with [coke](coke%20(fuel).md) <!--SR:!2025-07-07,573,310-->
- [nickel](nickel.md)::[smelting](smelting.md) with [coke](coke%20(fuel).md) <!--SR:!2024-04-23,296,330-->
- [tin](tin.md)::[smelting](smelting.md) with [coke](coke%20(fuel).md) <!--SR:!2024-03-06,89,290-->
- [lead](lead.md)::[smelting](smelting.md) with [coke](coke%20(fuel).md) <!--SR:!2024-03-26,97,290-->
- [antimony](antimony.md)::heat or physical extraction <!--SR:!2025-06-20,562,310-->
- [bismuth](bismuth.md)::heat or physical extraction <!--SR:!2025-07-22,576,310-->
- [copper](copper.md)::heat or physical extraction <!--SR:!2025-11-24,662,310-->
- [tungsten](tungsten.md)::heat or physical extraction <!--SR:!2024-05-20,318,330-->
- [mercury](mercury%20(element).md)::heat or physical extraction <!--SR:!2026-03-04,765,330-->
- [silver](silver.md)::heat or physical extraction <!--SR:!2024-04-14,292,330-->
- [gold](gold.md)::heat or physical extraction <!--SR:!2027-04-23,1150,350-->
- [platinum](platinum.md)::heat or physical extraction <!--SR:!2024-05-30,328,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ee23"--><!-- The following content is generated at 2024-02-17T20:43:15.045911+08:00. Any edits will be overridden! -->

- [electrolysis](electrolysis.md)::[caesium](caesium.md), [rubidium](rubidium.md), [potassium](potassium.md), [sodium](sodium.md), [lithium](lithium.md), [barium](barium.md), [strontium](strontium.md), [calcium](calcium.md), [magnesium](magnesium.md), [beryllium](beryllium.md), [aluminium](aluminium.md) <!--SR:!2024-03-03,6,245-->
- [pyrometallurgical](pyrometallurgy.md) extraction using [magnesium](magnesium.md)::[titanium](titanium.md) <!--SR:!2024-03-01,9,287-->
- [smelting](smelting.md) with [coke](coke%20(fuel).md)::[manganese](manganese.md), [zinc](zinc.md), [iron](iron.md), [cadmium](cadmium.md), [cobalt](cobalt.md), [nickel](nickel.md), [tin](tin.md), [lead](lead.md) <!--SR:!2024-03-03,4,205-->
- [aluminothermic reaction](aluminothermic%20reaction.md)::[chromium](chromium.md) <!--SR:!2024-03-04,4,267-->
- heat or physical extraction::[antimony](antimony.md), [bismuth](bismuth.md), [copper](copper.md), [tungsten](tungsten.md), [mercury](mercury%20(element).md), [silver](silver.md), [gold](gold.md), [platinum](platinum.md) <!--SR:!2024-03-02,10,285-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## reactions

### reactions between water and acids

More reactive [metals](metal.md) react with {{cold [water](water.md) to form the metal [hydroxide](hydroxide.md) and [hydrogen](hydrogen.md)}}. <!--SR:!2024-08-31,368,290-->

Moderately reactive metals react with {{[steam](steam.md) or [acids](acid.md) to form respectively the metal [oxide](oxide.md) or [salt](salt%20(chemistry).md), along with [hydrogen](hydrogen.md)}}. <!--SR:!2024-06-06,271,250-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/reactivity_series) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
