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

A __reactivity series__ is {{a progression of series of [metals](metal.md) arranged by their [reactivity](reactivity%20(chemistry).md)}}. <!--SR:!2023-05-13,29,270-->

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
> | {{[platinum](platinum.md)}} | {{Pt<sup>4+</sup>}} | {{may react with some strong [oxidizing agents](oxidizing%20agent.md)}} | {{heat or physical extraction}} | <!--SR:!2023-06-28,65,310!2023-06-13,54,310!2023-06-24,63,310!2023-07-01,68,310!2023-07-02,69,310!2023-05-21,34,270!2023-07-01,68,310!2023-06-30,67,310!2023-06-15,56,310!2023-06-12,53,310!2023-06-16,56,310!2023-06-16,56,310!2023-07-03,70,310!2023-06-13,54,310!2023-06-10,51,310!2023-07-04,71,310!2023-06-11,52,310!2023-06-27,65,310!2023-06-22,61,310!2023-06-03,42,290!2023-07-05,72,310!2023-06-15,56,310!2023-05-30,40,290!2023-06-30,68,310!2023-05-30,43,290!2023-06-17,57,310!2023-06-01,40,290!2023-06-28,66,310!2023-06-15,56,310!2023-07-04,71,310!2023-05-12,25,270!2023-06-26,64,310!2023-06-30,68,310!2023-06-23,62,310!2023-05-02,17,250!2023-05-22,34,270!2023-05-31,44,290!2023-05-31,41,290!2023-05-16,21,210!2023-06-14,55,310!2023-06-25,64,310!2023-06-24,63,310!2023-05-01,3,210!2023-06-01,33,250!2023-07-02,69,310!2023-05-30,40,290!2023-05-10,23,250!2023-05-15,28,270!2023-06-23,62,310!2023-06-01,42,290!2023-05-02,6,210!2023-04-30,6,230!2023-06-23,62,310!2023-06-11,49,290!2023-05-24,36,270!2023-06-07,45,290!2023-06-04,47,290!2023-06-18,58,310!2023-05-20,33,270!2023-05-26,27,270!2023-06-28,66,310!2023-06-10,48,290!2023-06-08,46,290!2023-05-04,20,290!2023-06-14,55,310!2023-06-29,66,310!2023-05-31,41,290!2023-06-05,45,290!2023-06-25,64,310!2023-07-02,69,310!2023-06-16,53,290!2023-06-05,44,290!2023-06-26,64,310!2023-06-15,56,310!2023-06-07,46,290!2023-07-01,68,310!2023-06-19,59,310!2023-07-06,73,310!2023-05-22,34,270!2023-06-02,41,290!2023-06-19,59,310!2023-06-12,50,290!2023-07-06,73,310!2023-06-02,42,290!2023-06-27,65,310!2023-05-22,33,270!2023-06-18,58,310!2023-06-06,45,290!2023-07-03,70,310!2023-05-16,32,270!2023-07-04,71,310!2023-06-20,60,310!2023-06-29,67,310!2023-05-03,10,270!2023-05-15,28,270!2023-06-30,68,310!2023-06-17,57,310!2023-06-03,42,290!2023-06-19,59,310!2023-07-03,70,310!2023-06-16,56,310!2023-06-02,42,290!2023-06-22,61,310!2023-06-11,52,310!2023-06-21,60,310!2023-06-04,43,290!2023-06-17,57,310!2023-06-27,65,310!2023-06-24,63,310!2023-05-28,41,290!2023-06-15,56,310!2023-06-20,60,310!2023-06-16,56,310!2023-06-05,37,290!2023-06-26,64,310!2023-07-05,72,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="299018"--><!-- The following content is generated at 2023-03-22T00:41:25.863762+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[caesium](caesium.md) <!--SR:!2023-06-15,56,310!2023-06-20,60,310-->
2. [caesium](caesium.md)→:::←[rubidium](rubidium.md) <!--SR:!2023-06-08,41,250!2023-05-29,33,250-->
3. [rubidium](rubidium.md)→:::←[potassium](potassium.md) <!--SR:!2023-05-06,22,250!2023-06-11,44,250-->
4. [potassium](potassium.md)→:::←[sodium](sodium.md) <!--SR:!2023-05-02,19,250!2023-06-28,66,310-->
5. [sodium](sodium.md)→:::←[lithium](lithium.md) <!--SR:!2023-05-11,26,270!2023-05-08,25,270-->
6. [lithium](lithium.md)→:::←[barium](barium.md) <!--SR:!2023-05-08,10,230!2023-05-21,33,270-->
7. [barium](barium.md)→:::←[strontium](strontium.md) <!--SR:!2023-05-05,20,250!2023-05-31,38,250-->
8. [strontium](strontium.md)→:::←[calcium](calcium.md) <!--SR:!2023-05-08,10,230!2023-05-02,4,250-->
9. [calcium](calcium.md)→:::←[magnesium](magnesium.md) <!--SR:!2023-05-02,19,250!2023-05-20,35,290-->
10. [magnesium](magnesium.md)→:::←[beryllium](beryllium.md) <!--SR:!2023-05-31,44,290!2023-05-19,32,270-->
11. [beryllium](beryllium.md)→:::←[aluminium](aluminium.md) <!--SR:!2023-05-16,29,270!2023-05-15,27,250-->
12. [aluminium](aluminium.md)→:::←[titanium](titanium.md) <!--SR:!2023-05-10,11,230!2023-05-06,24,270-->
13. [titanium](titanium.md)→:::←[manganese](manganese.md) <!--SR:!2023-05-05,21,250!2023-05-25,36,270-->
14. [manganese](manganese.md)→:::←[zinc](zinc.md) <!--SR:!2023-05-08,23,250!2023-06-13,45,250-->
15. [zinc](zinc.md)→:::←[chromium](chromium.md) <!--SR:!2023-06-04,37,230!2023-05-13,19,250-->
16. [chromium](chromium.md)→:::←[iron](iron.md) <!--SR:!2023-06-01,45,290!2023-05-03,18,230-->
17. [iron](iron.md)→:::←[cadmium](cadmium.md) <!--SR:!2023-05-29,42,290!2023-05-18,31,270-->
18. [cadmium](cadmium.md)→:::←[cobalt](cobalt.md) <!--SR:!2023-05-05,21,250!2023-05-06,10,190-->
19. [cobalt](cobalt.md)→:::←[nickel](nickel.md) <!--SR:!2023-05-02,19,250!2023-05-04,19,250-->
20. [nickel](nickel.md)→:::←[tin](tin.md) <!--SR:!2023-05-03,20,250!2023-05-07,23,250-->
21. [tin](tin.md)→:::←[lead](lead.md) <!--SR:!2023-05-07,23,250!2023-05-21,28,230-->
22. [lead](lead.md)→:::←[antimony](antimony.md) <!--SR:!2023-05-06,22,250!2023-06-06,39,250-->
23. [antimony](antimony.md)→:::←[bismuth](bismuth.md) <!--SR:!2023-06-09,42,250!2023-06-26,58,270-->
24. [bismuth](bismuth.md)→:::←[copper](copper.md) <!--SR:!2023-05-04,20,250!2023-04-30,17,250-->
25. [copper](copper.md)→:::←[tungsten](tungsten.md) <!--SR:!2023-05-12,27,270!2023-06-10,43,250-->
26. [tungsten](tungsten.md)→:::←[mercury](mercury%20(element).md) <!--SR:!2023-05-09,26,270!2023-05-20,32,270-->
27. [mercury](mercury%20(element).md)→:::←[silver](silver.md) <!--SR:!2023-06-21,60,310!2023-06-30,67,310-->
28. [silver](silver.md)→:::←[gold](gold.md) <!--SR:!2023-06-05,48,290!2023-06-29,67,310-->
29. [gold](gold.md)→:::←[platinum](platinum.md) <!--SR:!2023-06-29,67,310!2023-06-18,58,310-->
30. [platinum](platinum.md)→:::←_(end)_ <!--SR:!2023-06-17,57,310!2023-06-25,64,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## reactions

### reactions between water and acids

More reactive [metals](metal.md) react with {{cold [water](water.md) to form the metal [hydroxide](hydroxide.md) and [hydrogen](hydrogen.md)}}. <!--SR:!2023-05-23,35,270-->

Moderately reactive metals react with {{[steam](steam.md) or [acids](acid.md) to form respectively the metal [oxide](oxide.md) or [salt](salt%20(chemistry).md), along with [hydrogen](hydrogen.md)}}. <!--SR:!2023-05-03,20,250-->
