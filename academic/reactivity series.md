---
aliases:
  - activity series
  - reactivity series
---

#academic/chemistry #flashcards/academic/Rr/reactivity_series

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# reactivity series

A __reactivity series__ is {{a progression of series of [metals](metal.md) arranged by their [reactivity](reactivity%20(chemistry).md)}}. <!--SR:!2023-04-14,8,250-->

## data

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
r_water = 'reacts with cold [water](water.md)'
r_mg = 'reacts very slowly with cold [water](water.md), rapidly with boiling water, and very vigorously with [acids](acid.md)'
r_steam = 'reacts with [steam](steam.md) and [acids](acid.md)'
r_ti = 'reacts with concentrated [mineral acids](mineral%20acid.md)'
r_acid = 'reacts with [acids](acid.md), poorly with [steam](steam.md)'
r_cu = 'reacts slowly with [air](air.md)'
r_ox = 'may react with some strong [oxidizing agents](oxidizing%20agent.md)'
e_ele = '[electrolysis](electrolysis.md)'
e_ti = '[pyrometallurgical](pyrometallurgy.md) extraction using [magnesium](magnesium.md)'
e_smelt = '[smelting](smelting.md) with [coke](coke%20(fuel).md)'
e_cr = '[aluminothermic reaction](aluminothermic%20reaction.md)'
e_phy = 'heat or physical extraction'
return await memorize_table(
	e.cwf_sects('a2994d', '299018'),
	('[metal](metal.md)', '[ion](ion.md)', '[reactivity](reactivity%20(chemistry).md)', '[extraction](extractive%20metallurgy.md)'),
	(
		('[caesium](caesium.md)', 'Cs<sup>+</sup>', r_water, e_ele,),
		('[rubidium](rubidium.md)', 'Rb<sup>+</sup>', r_water, e_ele,),
		('[potassium](potassium.md)', 'K<sup>+</sup>', r_water, e_ele,),
		('[sodium](sodium.md)', 'Na<sup>+</sup>', r_water, e_ele,),
		('[lithium](lithium.md)', 'Li<sup>+</sup>', r_water, e_ele,),
		('[barium](barium.md)', 'Ba<sup>2+</sup>', r_water, e_ele,),
		('[strontium](strontium.md)', 'Sr<sup>2+</sup>', r_water, e_ele,),
		('[calcium](calcium.md)', 'Ca<sup>2+</sup>', r_water, e_ele,),
		('[magnesium](magnesium.md)', 'Mg<sup>2+</sup>', r_mg, e_ele,),
		('[beryllium](beryllium.md)', 'Be<sup>2+</sup>', r_steam, e_ele,),
		('[aluminium](aluminium.md)', 'Al<sup>3+</sup>', r_steam, e_ele,),
		('[titanium](titanium.md)', 'Ti<sup>4+</sup>', r_ti, e_ti,),
		('[manganese](manganese.md)', 'Mn<sup>2+</sup>', r_acid, e_smelt,),
		('[zinc](zinc.md)', 'Zn<sup>2+</sup>', r_acid, e_smelt,),
		('[chromium](chromium.md)', 'Cr<sup>3+</sup>', r_acid, e_cr,),
		('[iron](iron.md)', 'Fe<sup>2+</sup>', r_acid, e_smelt,),
		('[cadmium](cadmium.md)', 'Cd<sup>2+</sup>', r_acid, e_smelt,),
		('[cobalt](cobalt.md)', 'Co<sup>2+</sup>', r_acid, e_smelt,),
		('[nickel](nickel.md)', 'Ni<sup>2+</sup>', r_acid, e_smelt,),
		('[tin](tin.md)', 'Sn<sup>2+</sup>', r_acid, e_smelt,),
		('[lead](lead.md)', 'Pb<sup>2+</sup>', r_acid, e_smelt,),
		('[antimony](antimony.md)', 'Sb<sup>3+</sup>', r_ox, e_phy,),
		('[bismuth](bismuth.md)', 'Bi<sup>3+</sup>', r_ox, e_phy,),
		('[copper](copper.md)', 'Cu<sup>2+</sup>', r_cu, e_phy,),
		('[tungsten](tungsten.md)', 'W<sup>3+</sup>', r_ox, e_phy,),
		('[mercury](mercury%20(element).md)', 'Hg<sup>2+</sup>', r_ox, e_phy,),
		('[silver](silver.md)', 'Ag<sup>+</sup>', r_ox, e_phy,),
		('[gold](gold.md)', 'Au<sup>3+</sup>', r_ox, e_phy,),
		('[platinum](platinum.md)', 'Pt<sup>4+</sup>', r_ox, e_phy,),
	),
	lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a2994d"--><!-- The following content is generated at 2023-04-04T11:36:38.494541+08:00. Any edits will be overridden! -->

> | [metal](metal.md) | [ion](ion.md) | [reactivity](reactivity%20(chemistry).md) | [extraction](extractive%20metallurgy.md) |
> |-|-|-|-|
> | {{[caesium](caesium.md)}} | {{Cs<sup>+</sup>}} | {{reacts with cold [water](water.md)}} | {{[electrolysis](electrolysis.md)}} |
> | {{[rubidium](rubidium.md)}} | {{Rb<sup>+</sup>}} | {{reacts with cold [water](water.md)}} | {{[electrolysis](electrolysis.md)}} |
> | {{[potassium](potassium.md)}} | {{K<sup>+</sup>}} | {{reacts with cold [water](water.md)}} | {{[electrolysis](electrolysis.md)}} |
> | {{[sodium](sodium.md)}} | {{Na<sup>+</sup>}} | {{reacts with cold [water](water.md)}} | {{[electrolysis](electrolysis.md)}} |
> | {{[lithium](lithium.md)}} | {{Li<sup>+</sup>}} | {{reacts with cold [water](water.md)}} | {{[electrolysis](electrolysis.md)}} |
> | {{[barium](barium.md)}} | {{Ba<sup>2+</sup>}} | {{reacts with cold [water](water.md)}} | {{[electrolysis](electrolysis.md)}} |
> | {{[strontium](strontium.md)}} | {{Sr<sup>2+</sup>}} | {{reacts with cold [water](water.md)}} | {{[electrolysis](electrolysis.md)}} |
> | {{[calcium](calcium.md)}} | {{Ca<sup>2+</sup>}} | {{reacts with cold [water](water.md)}} | {{[electrolysis](electrolysis.md)}} |
> | {{[magnesium](magnesium.md)}} | {{Mg<sup>2+</sup>}} | {{reacts very slowly with cold [water](water.md), rapidly with boiling water, and very vigorously with [acids](acid.md)}} | {{[electrolysis](electrolysis.md)}} |
> | {{[beryllium](beryllium.md)}} | {{Be<sup>2+</sup>}} | {{reacts with [steam](steam.md) and [acids](acid.md)}} | {{[electrolysis](electrolysis.md)}} |
> | {{[aluminium](aluminium.md)}} | {{Al<sup>3+</sup>}} | {{reacts with [steam](steam.md) and [acids](acid.md)}} | {{[electrolysis](electrolysis.md)}} |
> | {{[titanium](titanium.md)}} | {{Ti<sup>4+</sup>}} | {{reacts with concentrated [mineral acids](mineral%20acid.md)}} | {{[pyrometallurgical](pyrometallurgy.md) extraction using [magnesium](magnesium.md)}} |
> | {{[manganese](manganese.md)}} | {{Mn<sup>2+</sup>}} | {{reacts with [acids](acid.md), poorly with [steam](steam.md)}} | {{[smelting](smelting.md) with [coke](coke%20(fuel).md)}} |
> | {{[zinc](zinc.md)}} | {{Zn<sup>2+</sup>}} | {{reacts with [acids](acid.md), poorly with [steam](steam.md)}} | {{[smelting](smelting.md) with [coke](coke%20(fuel).md)}} |
> | {{[chromium](chromium.md)}} | {{Cr<sup>3+</sup>}} | {{reacts with [acids](acid.md), poorly with [steam](steam.md)}} | {{[aluminothermic reaction](aluminothermic%20reaction.md)}} |
> | {{[iron](iron.md)}} | {{Fe<sup>2+</sup>}} | {{reacts with [acids](acid.md), poorly with [steam](steam.md)}} | {{[smelting](smelting.md) with [coke](coke%20(fuel).md)}} |
> | {{[cadmium](cadmium.md)}} | {{Cd<sup>2+</sup>}} | {{reacts with [acids](acid.md), poorly with [steam](steam.md)}} | {{[smelting](smelting.md) with [coke](coke%20(fuel).md)}} |
> | {{[cobalt](cobalt.md)}} | {{Co<sup>2+</sup>}} | {{reacts with [acids](acid.md), poorly with [steam](steam.md)}} | {{[smelting](smelting.md) with [coke](coke%20(fuel).md)}} |
> | {{[nickel](nickel.md)}} | {{Ni<sup>2+</sup>}} | {{reacts with [acids](acid.md), poorly with [steam](steam.md)}} | {{[smelting](smelting.md) with [coke](coke%20(fuel).md)}} |
> | {{[tin](tin.md)}} | {{Sn<sup>2+</sup>}} | {{reacts with [acids](acid.md), poorly with [steam](steam.md)}} | {{[smelting](smelting.md) with [coke](coke%20(fuel).md)}} |
> | {{[lead](lead.md)}} | {{Pb<sup>2+</sup>}} | {{reacts with [acids](acid.md), poorly with [steam](steam.md)}} | {{[smelting](smelting.md) with [coke](coke%20(fuel).md)}} |
> | {{[antimony](antimony.md)}} | {{Sb<sup>3+</sup>}} | {{may react with some strong [oxidizing agents](oxidizing%20agent.md)}} | {{heat or physical extraction}} |
> | {{[bismuth](bismuth.md)}} | {{Bi<sup>3+</sup>}} | {{may react with some strong [oxidizing agents](oxidizing%20agent.md)}} | {{heat or physical extraction}} |
> | {{[copper](copper.md)}} | {{Cu<sup>2+</sup>}} | {{reacts slowly with [air](air.md)}} | {{heat or physical extraction}} |
> | {{[tungsten](tungsten.md)}} | {{W<sup>3+</sup>}} | {{may react with some strong [oxidizing agents](oxidizing%20agent.md)}} | {{heat or physical extraction}} |
> | {{[mercury](mercury%20(element).md)}} | {{Hg<sup>2+</sup>}} | {{may react with some strong [oxidizing agents](oxidizing%20agent.md)}} | {{heat or physical extraction}} |
> | {{[silver](silver.md)}} | {{Ag<sup>+</sup>}} | {{may react with some strong [oxidizing agents](oxidizing%20agent.md)}} | {{heat or physical extraction}} |
> | {{[gold](gold.md)}} | {{Au<sup>3+</sup>}} | {{may react with some strong [oxidizing agents](oxidizing%20agent.md)}} | {{heat or physical extraction}} |
> | {{[platinum](platinum.md)}} | {{Pt<sup>4+</sup>}} | {{may react with some strong [oxidizing agents](oxidizing%20agent.md)}} | {{heat or physical extraction}} | <!--SR:!2023-04-24,17,290!2023-04-20,13,290!2023-04-22,15,290!2023-04-24,17,290!2023-04-24,17,290!2023-04-17,11,270!2023-04-24,17,290!2023-04-24,17,290!2023-04-20,13,290!2023-04-20,13,290!2023-04-21,14,290!2023-04-21,14,290!2023-04-24,17,290!2023-04-20,13,290!2023-04-20,13,290!2023-04-24,17,290!2023-04-20,13,290!2023-04-23,16,290!2023-04-22,15,290!2023-04-22,15,290!2023-04-24,17,290!2023-04-20,13,290!2023-04-20,13,290!2023-04-23,16,290!2023-04-16,10,270!2023-04-21,14,290!2023-04-22,15,290!2023-04-23,16,290!2023-04-20,13,290!2023-04-24,17,290!2023-04-09,2,250!2023-04-23,16,290!2023-04-23,16,290!2023-04-22,15,290!2023-04-09,2,230!2023-04-18,12,270!2023-04-16,10,270!2023-04-20,13,290!2023-04-09,1,210!2023-04-20,13,290!2023-04-22,15,290!2023-04-22,15,290!2023-04-15,9,270!2023-04-14,6,250!2023-04-24,17,290!2023-04-20,13,290!2023-04-16,8,250!2023-04-16,9,270!2023-04-22,15,290!2023-04-20,13,290!2023-04-14,6,250!2023-04-21,14,290!2023-04-22,15,290!2023-04-23,16,290!2023-04-18,12,270!2023-04-23,16,290!2023-04-18,12,270!2023-04-21,14,290!2023-04-17,11,270!2023-04-20,13,290!2023-04-23,16,290!2023-04-23,16,290!2023-04-23,16,290!2023-04-09,2,250!2023-04-20,13,290!2023-04-24,17,290!2023-04-20,13,290!2023-04-21,14,290!2023-04-22,15,290!2023-04-24,17,290!2023-04-24,17,290!2023-04-22,15,290!2023-04-23,16,290!2023-04-20,13,290!2023-04-22,15,290!2023-04-24,17,290!2023-04-21,14,290!2023-04-24,17,290!2023-04-18,11,270!2023-04-22,15,290!2023-04-21,14,290!2023-04-23,16,290!2023-04-24,17,290!2023-04-21,14,290!2023-04-23,16,290!2023-04-19,12,270!2023-04-21,14,290!2023-04-22,15,290!2023-04-24,17,290!2023-04-14,8,250!2023-04-24,17,290!2023-04-21,14,290!2023-04-23,16,290!2023-04-23,16,290!2023-04-16,9,270!2023-04-23,16,290!2023-04-21,14,290!2023-04-22,15,290!2023-04-21,14,290!2023-04-24,17,290!2023-04-21,14,290!2023-04-21,14,290!2023-04-22,15,290!2023-04-20,13,290!2023-04-22,15,290!2023-04-22,15,290!2023-04-21,14,290!2023-04-23,16,290!2023-04-22,15,290!2023-04-16,9,270!2023-04-20,13,290!2023-04-21,14,290!2023-04-21,14,290!2023-04-20,13,290!2023-04-23,16,290!2023-04-24,17,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="299018"--><!-- The following content is generated at 2023-03-22T00:41:25.863762+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[caesium](caesium.md) <!--SR:!2023-04-20,13,290!2023-04-21,14,290-->
2. [caesium](caesium.md)→:::←[rubidium](rubidium.md) <!--SR:!2023-04-12,4,230!2023-04-12,4,230-->
3. [rubidium](rubidium.md)→:::←[potassium](potassium.md) <!--SR:!2023-04-14,8,250!2023-04-12,6,250-->
4. [potassium](potassium.md)→:::←[sodium](sodium.md) <!--SR:!2023-04-13,7,250!2023-04-23,16,290-->
5. [sodium](sodium.md)→:::←[lithium](lithium.md) <!--SR:!2023-04-15,9,270!2023-04-13,7,250-->
6. [lithium](lithium.md)→:::←[barium](barium.md) <!--SR:!2023-04-13,5,250!2023-04-18,11,270-->
7. [barium](barium.md)→:::←[strontium](strontium.md) <!--SR:!2023-04-15,7,250!2023-04-12,4,230-->
8. [strontium](strontium.md)→:::←[calcium](calcium.md) <!--SR:!2023-04-12,6,250!2023-04-12,6,250-->
9. [calcium](calcium.md)→:::←[magnesium](magnesium.md) <!--SR:!2023-04-13,7,250!2023-04-15,9,270-->
10. [magnesium](magnesium.md)→:::←[beryllium](beryllium.md) <!--SR:!2023-04-16,10,270!2023-04-17,11,270-->
11. [beryllium](beryllium.md)→:::←[aluminium](aluminium.md) <!--SR:!2023-04-17,10,270!2023-04-18,10,250-->
12. [aluminium](aluminium.md)→:::←[titanium](titanium.md) <!--SR:!2023-04-12,6,250!2023-04-12,6,250-->
13. [titanium](titanium.md)→:::←[manganese](manganese.md) <!--SR:!2023-04-14,8,250!2023-04-19,12,270-->
14. [manganese](manganese.md)→:::←[zinc](zinc.md) <!--SR:!2023-04-15,8,250!2023-04-12,6,250-->
15. [zinc](zinc.md)→:::←[chromium](chromium.md) <!--SR:!2023-04-13,5,230!2023-04-17,11,270-->
16. [chromium](chromium.md)→:::←[iron](iron.md) <!--SR:!2023-04-16,10,270!2023-04-15,7,230-->
17. [iron](iron.md)→:::←[cadmium](cadmium.md) <!--SR:!2023-04-17,10,270!2023-04-17,11,270-->
18. [cadmium](cadmium.md)→:::←[cobalt](cobalt.md) <!--SR:!2023-04-14,8,250!2023-04-13,7,250-->
19. [cobalt](cobalt.md)→:::←[nickel](nickel.md) <!--SR:!2023-04-13,7,250!2023-04-15,7,250-->
20. [nickel](nickel.md)→:::←[tin](tin.md) <!--SR:!2023-04-13,7,250!2023-04-14,8,250-->
21. [tin](tin.md)→:::←[lead](lead.md) <!--SR:!2023-04-14,8,250!2023-04-12,4,230-->
22. [lead](lead.md)→:::←[antimony](antimony.md) <!--SR:!2023-04-14,8,250!2023-04-13,5,250-->
23. [antimony](antimony.md)→:::←[bismuth](bismuth.md) <!--SR:!2023-04-12,6,250!2023-04-12,6,250-->
24. [bismuth](bismuth.md)→:::←[copper](copper.md) <!--SR:!2023-04-14,7,250!2023-04-13,6,250-->
25. [copper](copper.md)→:::←[tungsten](tungsten.md) <!--SR:!2023-04-15,9,270!2023-04-12,6,250-->
26. [tungsten](tungsten.md)→:::←[mercury](mercury%20(element).md) <!--SR:!2023-04-13,7,250!2023-04-18,11,270-->
27. [mercury](mercury%20(element).md)→:::←[silver](silver.md) <!--SR:!2023-04-22,15,290!2023-04-24,17,290-->
28. [silver](silver.md)→:::←[gold](gold.md) <!--SR:!2023-04-18,12,270!2023-04-23,16,290-->
29. [gold](gold.md)→:::←[platinum](platinum.md) <!--SR:!2023-04-23,16,290!2023-04-21,14,290-->
30. [platinum](platinum.md)→:::←_(end)_ <!--SR:!2023-04-21,14,290!2023-04-22,15,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## reactions

### reactions between water and acids

More reactive [metals](metal.md) react with {{cold [water](water.md) to form the metal [hydroxide](hydroxide.md) and [hydrogen](hydrogen.md)}}. <!--SR:!2023-04-18,12,270-->

Moderately reactive metals react with {{[steam](steam.md) or [acids](acid.md) to form respectively the metal [oxide](oxide.md) or [salt](salt%20(chemistry).md), along with [hydrogen](hydrogen.md)}}. <!--SR:!2023-04-13,7,250-->
