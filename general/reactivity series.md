---
aliases:
  - activity series
  - reactivity series
tags:
  - flashcards/general/reactivity_series
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# reactivity series

A __reactivity series__ is {{a progression of series of [metals](metal.md) arranged by their [reactivity](reactivity%20(chemistry).md)}}. <!--SR:!2024-03-23,232,270-->

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
> | {{[platinum](platinum.md)}} | {{Pt<sup>4+</sup>}} | {{may react with some strong [oxidizing agents](oxidizing%20agent.md)}} | {{heat or physical extraction}} | <!--SR:!2024-04-25,298,330!2024-01-31,232,330!2024-04-02,282,330!2024-04-21,294,330!2024-04-30,303,330!2023-10-12,142,290!2024-05-03,306,330!2024-04-22,295,330!2024-03-05,260,330!2024-02-04,237,330!2024-02-22,248,330!2024-02-17,243,330!2024-06-01,330,330!2024-02-11,243,330!2024-01-31,234,330!2024-05-31,329,330!2024-01-30,233,330!2024-04-03,281,330!2024-01-05,194,310!2023-12-06,182,310!2024-06-02,331,330!2024-03-09,264,330!2023-11-06,160,310!2024-05-08,311,330!2023-11-23,177,310!2024-02-25,251,330!2023-11-09,161,310!2024-04-29,302,330!2024-02-29,255,330!2024-05-19,317,330!2024-02-12,200,270!2024-03-31,278,330!2024-05-01,304,330!2024-04-03,283,330!2023-10-08,23,190!2024-05-11,258,270!2023-12-01,184,310!2023-11-12,165,310!2023-09-26,57,190!2024-03-06,261,330!2024-03-16,265,330!2024-03-22,271,330!2023-12-25,101,170!2023-10-14,48,230!2024-05-06,309,330!2023-11-07,161,310!2024-01-01,167,250!2023-11-06,84,210!2024-04-04,284,330!2023-11-25,177,310!2023-09-20,26,130!2023-09-16,18,210!2024-03-18,267,330!2023-12-26,198,310!2024-06-30,295,270!2023-10-16,131,290!2024-01-05,212,310!2024-02-21,247,330!2024-04-30,252,270!2024-03-02,207,270!2024-05-02,305,330!2023-12-27,199,310!2023-10-27,138,290!2024-04-01,251,310!2024-03-08,263,330!2024-05-05,308,330!2023-11-11,164,310!2023-12-21,197,310!2024-03-20,269,330!2024-05-07,310,330!2023-11-30,164,290!2023-12-11,187,310!2024-03-30,277,330!2024-03-07,262,330!2023-12-07,183,310!2024-04-23,296,330!2024-02-27,253,330!2024-05-18,316,330!2024-08-20,361,290!2023-12-08,184,310!2024-02-15,241,330!2023-12-31,202,310!2024-02-19,227,310!2023-12-20,196,310!2024-04-01,279,330!2023-10-11,49,250!2023-12-18,182,310!2023-12-06,182,310!2024-06-03,332,330!2024-07-30,351,290!2024-02-17,225,310!2023-12-23,186,310!2024-05-04,307,330!2023-11-21,163,310!2024-02-25,208,270!2024-02-01,214,310!2024-02-20,246,330!2023-12-10,186,310!2024-02-24,250,330!2024-05-20,318,330!2024-02-16,242,330!2023-10-07,97,290!2024-03-19,268,330!2024-01-29,232,330!2024-03-24,273,330!2023-12-09,185,310!2024-02-23,249,330!2024-04-14,292,330!2024-03-23,272,330!2023-11-14,170,310!2024-03-04,259,330!2024-02-28,253,330!2024-02-28,254,330!2023-11-15,161,310!2024-04-02,280,330!2024-05-30,328,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="299018"--><!-- The following content is generated at 2023-03-22T00:41:25.863762+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[caesium](caesium.md) <!--SR:!2024-03-03,258,330!2024-03-06,260,330-->
2. [caesium](caesium.md)→:::←[rubidium](rubidium.md) <!--SR:!2023-09-27,108,250!2024-01-13,159,250-->
3. [rubidium](rubidium.md)→:::←[potassium](potassium.md) <!--SR:!2023-12-11,157,250!2023-09-30,111,250-->
4. [potassium](potassium.md)→:::←[sodium](sodium.md) <!--SR:!2024-05-06,293,290!2024-01-29,211,310-->
5. [sodium](sodium.md)→:::←[lithium](lithium.md) <!--SR:!2024-02-18,162,270!2024-05-25,285,290-->
6. [lithium](lithium.md)→:::←[barium](barium.md) <!--SR:!2023-12-15,137,230!2023-10-17,51,250-->
7. [barium](barium.md)→:::←[strontium](strontium.md) <!--SR:!2024-01-06,193,270!2023-10-13,135,270-->
8. [strontium](strontium.md)→:::←[calcium](calcium.md) <!--SR:!2024-01-15,157,230!2023-10-26,129,270-->
9. [calcium](calcium.md)→:::←[magnesium](magnesium.md) <!--SR:!2024-01-14,140,270!2023-11-05,57,270-->
10. [magnesium](magnesium.md)→:::←[beryllium](beryllium.md) <!--SR:!2023-11-30,183,310!2024-07-23,341,290-->
11. [beryllium](beryllium.md)→:::←[aluminium](aluminium.md) <!--SR:!2023-09-21,45,250!2024-01-30,186,250-->
12. [aluminium](aluminium.md)→:::←[titanium](titanium.md) <!--SR:!2024-03-23,222,250!2024-01-26,192,270-->
13. [titanium](titanium.md)→:::←[manganese](manganese.md) <!--SR:!2023-11-28,149,250!2024-06-29,294,270-->
14. [manganese](manganese.md)→:::←[zinc](zinc.md) <!--SR:!2023-09-25,10,190!2023-10-08,117,250-->
15. [zinc](zinc.md)→:::←[chromium](chromium.md) <!--SR:!2024-04-13,217,230!2023-10-19,73,230-->
16. [chromium](chromium.md)→:::←[iron](iron.md) <!--SR:!2024-06-15,280,290!2023-09-18,62,210-->
17. [iron](iron.md)→:::←[cadmium](cadmium.md) <!--SR:!2023-10-02,125,290!2024-04-07,237,270-->
18. [cadmium](cadmium.md)→:::←[cobalt](cobalt.md) <!--SR:!2023-11-22,143,250!2023-09-26,17,130-->
19. [cobalt](cobalt.md)→:::←[nickel](nickel.md) <!--SR:!2023-11-05,133,250!2023-11-06,134,250-->
20. [nickel](nickel.md)→:::←[tin](tin.md) <!--SR:!2023-11-15,141,250!2023-09-27,12,190-->
21. [tin](tin.md)→:::←[lead](lead.md) <!--SR:!2024-01-02,168,250!2024-01-15,166,230-->
22. [lead](lead.md)→:::←[antimony](antimony.md) <!--SR:!2023-11-29,150,250!2023-09-18,103,250-->
23. [antimony](antimony.md)→:::←[bismuth](bismuth.md) <!--SR:!2023-11-12,154,270!2024-02-04,222,290-->
24. [bismuth](bismuth.md)→:::←[copper](copper.md) <!--SR:!2024-01-28,194,270!2023-12-25,159,250-->
25. [copper](copper.md)→:::←[tungsten](tungsten.md) <!--SR:!2024-03-08,220,270!2023-11-19,161,270-->
26. [tungsten](tungsten.md)→:::←[mercury](mercury%20(element).md) <!--SR:!2023-12-12,105,250!2023-09-25,69,230-->
27. [mercury](mercury%20(element).md)→:::←[silver](silver.md) <!--SR:!2024-03-17,266,330!2024-04-24,297,330-->
28. [silver](silver.md)→:::←[gold](gold.md) <!--SR:!2024-01-04,211,310!2024-05-09,312,330-->
29. [gold](gold.md)→:::←[platinum](platinum.md) <!--SR:!2024-04-28,301,330!2024-02-26,252,330-->
30. [platinum](platinum.md)→:::←_(end)_ <!--SR:!2024-02-19,245,330!2024-03-21,270,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## reactions

### reactions between water and acids

More reactive [metals](metal.md) react with {{cold [water](water.md) to form the metal [hydroxide](hydroxide.md) and [hydrogen](hydrogen.md)}}. <!--SR:!2024-08-31,368,290-->

Moderately reactive metals react with {{[steam](steam.md) or [acids](acid.md) to form respectively the metal [oxide](oxide.md) or [salt](salt%20(chemistry).md), along with [hydrogen](hydrogen.md)}}. <!--SR:!2024-06-06,271,250-->
