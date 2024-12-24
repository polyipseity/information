---
aliases:
  - activity series
  - reactivity series
tags:
  - flashcard/active/general/reactivity_series
  - language/in/English
---

# reactivity series

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

A __reactivity series__ is {@{a progression of series of [metals](metal.md) arranged by their [reactivity](reactivity%20(chemistry).md)}@}.

## data

```Python
# pytextgen generate data
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

<!--pytextgen generate section="a2994d"--><!-- The following content is generated at 2024-02-17T20:43:15.082424+08:00. Any edits will be overridden! -->

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

<!--/pytextgen-->

<!--pytextgen generate section="299018"--><!-- The following content is generated at 2024-02-18T15:03:20.984589+08:00. Any edits will be overridden! -->

- _(most reactive)_→::@::←[caesium](caesium.md)
- [caesium](caesium.md)→::@::←[rubidium](rubidium.md)
- [rubidium](rubidium.md)→::@::←[potassium](potassium.md)
- [potassium](potassium.md)→::@::←[sodium](sodium.md)
- [sodium](sodium.md)→::@::←[lithium](lithium.md)
- [lithium](lithium.md)→::@::←[barium](barium.md)
- [barium](barium.md)→::@::←[strontium](strontium.md)
- [strontium](strontium.md)→::@::←[calcium](calcium.md)
- [calcium](calcium.md)→::@::←[magnesium](magnesium.md)
- [magnesium](magnesium.md)→::@::←[beryllium](beryllium.md)
- [beryllium](beryllium.md)→::@::←[aluminium](aluminium.md)
- [aluminium](aluminium.md)→::@::←[titanium](titanium.md)
- [titanium](titanium.md)→::@::←[manganese](manganese.md)
- [manganese](manganese.md)→::@::←[zinc](zinc.md)
- [zinc](zinc.md)→::@::←[chromium](chromium.md)
- [chromium](chromium.md)→::@::←[iron](iron.md)
- [iron](iron.md)→::@::←[cadmium](cadmium.md)
- [cadmium](cadmium.md)→::@::←[cobalt](cobalt.md)
- [cobalt](cobalt.md)→::@::←[nickel](nickel.md)
- [nickel](nickel.md)→::@::←[tin](tin.md)
- [tin](tin.md)→::@::←[lead](lead.md)
- [lead](lead.md)→::@::←[antimony](antimony.md)
- [antimony](antimony.md)→::@::←[bismuth](bismuth.md)
- [bismuth](bismuth.md)→::@::←[copper](copper.md)
- [copper](copper.md)→::@::←[tungsten](tungsten.md)
- [tungsten](tungsten.md)→::@::←[mercury](mercury%20(element).md)
- [mercury](mercury%20(element).md)→::@::←[silver](silver.md)
- [silver](silver.md)→::@::←[gold](gold.md)
- [gold](gold.md)→::@::←[platinum](platinum.md)
- [platinum](platinum.md)→::@::←_(least reactive)_

<!--/pytextgen-->

### metal–ion

<!--pytextgen generate section="1e32"--><!-- The following content is generated at 2024-02-17T20:43:14.994069+08:00. Any edits will be overridden! -->

- [caesium](caesium.md):@:Cs<sup>+</sup>
- [rubidium](rubidium.md):@:Rb<sup>+</sup>
- [potassium](potassium.md):@:K<sup>+</sup>
- [sodium](sodium.md):@:Na<sup>+</sup>
- [lithium](lithium.md):@:Li<sup>+</sup>
- [barium](barium.md):@:Ba<sup>2+</sup>
- [strontium](strontium.md):@:Sr<sup>2+</sup>
- [calcium](calcium.md):@:Ca<sup>2+</sup>
- [magnesium](magnesium.md):@:Mg<sup>2+</sup>
- [beryllium](beryllium.md):@:Be<sup>2+</sup>
- [aluminium](aluminium.md):@:Al<sup>3+</sup>
- [titanium](titanium.md):@:Ti<sup>4+</sup>
- [manganese](manganese.md):@:Mn<sup>2+</sup>
- [zinc](zinc.md):@:Zn<sup>2+</sup>
- [chromium](chromium.md):@:Cr<sup>3+</sup>
- [iron](iron.md):@:Fe<sup>2+</sup>
- [cadmium](cadmium.md):@:Cd<sup>2+</sup>
- [cobalt](cobalt.md):@:Co<sup>2+</sup>
- [nickel](nickel.md):@:Ni<sup>2+</sup>
- [tin](tin.md):@:Sn<sup>2+</sup>
- [lead](lead.md):@:Pb<sup>2+</sup>
- [antimony](antimony.md):@:Sb<sup>3+</sup>
- [bismuth](bismuth.md):@:Bi<sup>3+</sup>
- [copper](copper.md):@:Cu<sup>2+</sup>
- [tungsten](tungsten.md):@:W<sup>3+</sup>
- [mercury](mercury%20(element).md):@:Hg<sup>2+</sup>
- [silver](silver.md):@:Ag<sup>+</sup>
- [gold](gold.md):@:Au<sup>3+</sup>
- [platinum](platinum.md):@:Pt<sup>4+</sup>

<!--/pytextgen-->

<!--pytextgen generate section="8912"--><!-- The following content is generated at 2024-02-17T20:43:15.136674+08:00. Any edits will be overridden! -->

- Cs<sup>+</sup>:@:[caesium](caesium.md)
- Rb<sup>+</sup>:@:[rubidium](rubidium.md)
- K<sup>+</sup>:@:[potassium](potassium.md)
- Na<sup>+</sup>:@:[sodium](sodium.md)
- Li<sup>+</sup>:@:[lithium](lithium.md)
- Ba<sup>2+</sup>:@:[barium](barium.md)
- Sr<sup>2+</sup>:@:[strontium](strontium.md)
- Ca<sup>2+</sup>:@:[calcium](calcium.md)
- Mg<sup>2+</sup>:@:[magnesium](magnesium.md)
- Be<sup>2+</sup>:@:[beryllium](beryllium.md)
- Al<sup>3+</sup>:@:[aluminium](aluminium.md)
- Ti<sup>4+</sup>:@:[titanium](titanium.md)
- Mn<sup>2+</sup>:@:[manganese](manganese.md)
- Zn<sup>2+</sup>:@:[zinc](zinc.md)
- Cr<sup>3+</sup>:@:[chromium](chromium.md)
- Fe<sup>2+</sup>:@:[iron](iron.md)
- Cd<sup>2+</sup>:@:[cadmium](cadmium.md)
- Co<sup>2+</sup>:@:[cobalt](cobalt.md)
- Ni<sup>2+</sup>:@:[nickel](nickel.md)
- Sn<sup>2+</sup>:@:[tin](tin.md)
- Pb<sup>2+</sup>:@:[lead](lead.md)
- Sb<sup>3+</sup>:@:[antimony](antimony.md)
- Bi<sup>3+</sup>:@:[bismuth](bismuth.md)
- Cu<sup>2+</sup>:@:[copper](copper.md)
- W<sup>3+</sup>:@:[tungsten](tungsten.md)
- Hg<sup>2+</sup>:@:[mercury](mercury%20(element).md)
- Ag<sup>+</sup>:@:[silver](silver.md)
- Au<sup>3+</sup>:@:[gold](gold.md)
- Pt<sup>4+</sup>:@:[platinum](platinum.md)

<!--/pytextgen-->

### metal–reactivity

<!--pytextgen generate section="22ba"--><!-- The following content is generated at 2024-02-17T20:43:15.064424+08:00. Any edits will be overridden! -->

- [caesium](caesium.md):@:reacts with cold [water](water.md)
- [rubidium](rubidium.md):@:reacts with cold [water](water.md)
- [potassium](potassium.md):@:reacts with cold [water](water.md)
- [sodium](sodium.md):@:reacts with cold [water](water.md)
- [lithium](lithium.md):@:reacts with cold [water](water.md)
- [barium](barium.md):@:reacts with cold [water](water.md)
- [strontium](strontium.md):@:reacts with cold [water](water.md)
- [calcium](calcium.md):@:reacts with cold [water](water.md)
- [magnesium](magnesium.md):@:reacts very slowly with cold [water](water.md), rapidly with boiling water, and very vigorously with [acids](acid.md)
- [beryllium](beryllium.md):@:reacts with [steam](steam.md) and [acids](acid.md)
- [aluminium](aluminium.md):@:reacts with [steam](steam.md) and [acids](acid.md)
- [titanium](titanium.md):@:reacts with concentrated [mineral acids](mineral%20acid.md)
- [manganese](manganese.md):@:reacts with [acids](acid.md), poorly with [steam](steam.md)
- [zinc](zinc.md):@:reacts with [acids](acid.md), poorly with [steam](steam.md)
- [chromium](chromium.md):@:reacts with [acids](acid.md), poorly with [steam](steam.md)
- [iron](iron.md):@:reacts with [acids](acid.md), poorly with [steam](steam.md)
- [cadmium](cadmium.md):@:reacts with [acids](acid.md), poorly with [steam](steam.md)
- [cobalt](cobalt.md):@:reacts with [acids](acid.md), poorly with [steam](steam.md)
- [nickel](nickel.md):@:reacts with [acids](acid.md), poorly with [steam](steam.md)
- [tin](tin.md):@:reacts with [acids](acid.md), poorly with [steam](steam.md)
- [lead](lead.md):@:reacts with [acids](acid.md), poorly with [steam](steam.md)
- [antimony](antimony.md):@:may react with some strong [oxidizing agents](oxidizing%20agent.md)
- [bismuth](bismuth.md):@:may react with some strong [oxidizing agents](oxidizing%20agent.md)
- [copper](copper.md):@:reacts slowly with [air](air.md)
- [tungsten](tungsten.md):@:may react with some strong [oxidizing agents](oxidizing%20agent.md)
- [mercury](mercury%20(element).md):@:may react with some strong [oxidizing agents](oxidizing%20agent.md)
- [silver](silver.md):@:may react with some strong [oxidizing agents](oxidizing%20agent.md)
- [gold](gold.md):@:may react with some strong [oxidizing agents](oxidizing%20agent.md)
- [platinum](platinum.md):@:may react with some strong [oxidizing agents](oxidizing%20agent.md)

<!--/pytextgen-->

<!--pytextgen generate section="671a"--><!-- The following content is generated at 2024-02-17T20:43:15.023699+08:00. Any edits will be overridden! -->

- reacts with cold [water](water.md):@:[caesium](caesium.md), [rubidium](rubidium.md), [potassium](potassium.md), [sodium](sodium.md), [lithium](lithium.md), [barium](barium.md), [strontium](strontium.md), [calcium](calcium.md)
- reacts very slowly with cold [water](water.md), rapidly with boiling water, and very vigorously with [acids](acid.md):@:[magnesium](magnesium.md)
- reacts with [steam](steam.md) and [acids](acid.md):@:[beryllium](beryllium.md), [aluminium](aluminium.md)
- reacts with concentrated [mineral acids](mineral%20acid.md):@:[titanium](titanium.md)
- reacts with [acids](acid.md), poorly with [steam](steam.md):@:[manganese](manganese.md), [zinc](zinc.md), [chromium](chromium.md), [iron](iron.md), [cadmium](cadmium.md), [cobalt](cobalt.md), [nickel](nickel.md), [tin](tin.md), [lead](lead.md)
- may react with some strong [oxidizing agents](oxidizing%20agent.md):@:[antimony](antimony.md), [bismuth](bismuth.md), [tungsten](tungsten.md), [mercury](mercury%20(element).md), [silver](silver.md), [gold](gold.md), [platinum](platinum.md)
- reacts slowly with [air](air.md):@:[copper](copper.md)

<!--/pytextgen-->

### metal–extraction

<!--pytextgen generate section="ba24"--><!-- The following content is generated at 2024-02-17T20:43:15.115428+08:00. Any edits will be overridden! -->

- [caesium](caesium.md):@:[electrolysis](electrolysis.md)
- [rubidium](rubidium.md):@:[electrolysis](electrolysis.md)
- [potassium](potassium.md):@:[electrolysis](electrolysis.md)
- [sodium](sodium.md):@:[electrolysis](electrolysis.md)
- [lithium](lithium.md):@:[electrolysis](electrolysis.md)
- [barium](barium.md):@:[electrolysis](electrolysis.md)
- [strontium](strontium.md):@:[electrolysis](electrolysis.md)
- [calcium](calcium.md):@:[electrolysis](electrolysis.md)
- [magnesium](magnesium.md):@:[electrolysis](electrolysis.md)
- [beryllium](beryllium.md):@:[electrolysis](electrolysis.md)
- [aluminium](aluminium.md):@:[electrolysis](electrolysis.md)
- [titanium](titanium.md):@:[pyrometallurgical](pyrometallurgy.md) extraction using [magnesium](magnesium.md)
- [manganese](manganese.md):@:[smelting](smelting.md) with [coke](coke%20(fuel).md)
- [zinc](zinc.md):@:[smelting](smelting.md) with [coke](coke%20(fuel).md)
- [chromium](chromium.md):@:[aluminothermic reaction](aluminothermic%20reaction.md)
- [iron](iron.md):@:[smelting](smelting.md) with [coke](coke%20(fuel).md)
- [cadmium](cadmium.md):@:[smelting](smelting.md) with [coke](coke%20(fuel).md)
- [cobalt](cobalt.md):@:[smelting](smelting.md) with [coke](coke%20(fuel).md)
- [nickel](nickel.md):@:[smelting](smelting.md) with [coke](coke%20(fuel).md)
- [tin](tin.md):@:[smelting](smelting.md) with [coke](coke%20(fuel).md)
- [lead](lead.md):@:[smelting](smelting.md) with [coke](coke%20(fuel).md)
- [antimony](antimony.md):@:heat or physical extraction
- [bismuth](bismuth.md):@:heat or physical extraction
- [copper](copper.md):@:heat or physical extraction
- [tungsten](tungsten.md):@:heat or physical extraction
- [mercury](mercury%20(element).md):@:heat or physical extraction
- [silver](silver.md):@:heat or physical extraction
- [gold](gold.md):@:heat or physical extraction
- [platinum](platinum.md):@:heat or physical extraction

<!--/pytextgen-->

<!--pytextgen generate section="ee23"--><!-- The following content is generated at 2024-02-17T20:43:15.045911+08:00. Any edits will be overridden! -->

- [electrolysis](electrolysis.md):@:[caesium](caesium.md), [rubidium](rubidium.md), [potassium](potassium.md), [sodium](sodium.md), [lithium](lithium.md), [barium](barium.md), [strontium](strontium.md), [calcium](calcium.md), [magnesium](magnesium.md), [beryllium](beryllium.md), [aluminium](aluminium.md)
- [pyrometallurgical](pyrometallurgy.md) extraction using [magnesium](magnesium.md):@:[titanium](titanium.md)
- [smelting](smelting.md) with [coke](coke%20(fuel).md):@:[manganese](manganese.md), [zinc](zinc.md), [iron](iron.md), [cadmium](cadmium.md), [cobalt](cobalt.md), [nickel](nickel.md), [tin](tin.md), [lead](lead.md)
- [aluminothermic reaction](aluminothermic%20reaction.md):@:[chromium](chromium.md)
- heat or physical extraction:@:[antimony](antimony.md), [bismuth](bismuth.md), [copper](copper.md), [tungsten](tungsten.md), [mercury](mercury%20(element).md), [silver](silver.md), [gold](gold.md), [platinum](platinum.md)

<!--/pytextgen-->

## reactions

### reactions between water and acids

More reactive [metals](metal.md) react with {@{cold [water](water.md) to form the metal [hydroxide](hydroxide.md) and [hydrogen](hydrogen.md)}@}.

Moderately reactive metals react with {@{[steam](steam.md) or [acids](acid.md) to form respectively the metal [oxide](oxide.md) or [salt](salt%20(chemistry).md), along with [hydrogen](hydrogen.md)}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/reactivity_series) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
