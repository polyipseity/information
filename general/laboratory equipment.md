---
aliases:
  - laboratory apparatus
  - laboratory equipment
  - laboratory equipments
  - laboratory instrument
  - laboratory instruments
tags:
  - academic/biology
  - academic/chemistry
  - academic/physics
  - flashcards/academic/Ll/laboratory_equipment
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# laboratory equipment

## examples

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.gen import markdown_sanitizer
e = __env__
rinse_water = 'Rinse the equipment with deionized [water](water.md) before use.'
rinse_water_soln = 'Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delievered.'
return await memorize_table(
	e.cwf_sects('fadd2e', 'b81237'),
	('name & image', 'description',),
	(
		('[Bunsen burner](Bunsen%20burner.md)', '![{}](../archives/Wikimedia%20Commons/Bunsen%20burner.jpg)', '',),
		('[Liebig condenser](Liebig%20condenser.md)', '![{}](../archives/Wikimedia%20Commons/LiebigCondenser.jpg)', '',),
		('[beaker](beaker.md)', '![{}](../archives/Wikimedia%20Commons/Glassware-%20Beaker.jpg)', '',),
		('[burette](burette.md)', '![{}](../archives/Wikimedia%20Commons/Burette.svg)', rinse_water_soln,),
		('[burette clamp](burette%20clamp.md)', '![{}](../archives/Wikimedia%20Commons/Burette%20with%20Clamp(3).jpg)', '',),
		('[clamp](clamp.md)', '![{}](../archives/Wikimedia%20Commons/Utility%20clamp1.jpg)', '',),
		('[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)', '![{}](../archives/Wikimedia%20Commons/250%20mL%20Erlenmeyer%20flask.jpg)', rinse_water,),
		('[crucible](crucible.md)', '![{}](../archives/Wikimedia%20Commons/Czochralski%20method%20used%20crucible%201.jpg)', '',),
		('[crucible tongs](crucible%20tongs.md)', '![{}](../archives/Wikimedia%20Commons/Crucible%20tong.jpg)', '',),
		('[desiccator](desiccator.md)', '![{}](../archives/Wikimedia%20Commons/Desiccator.jpg)', '',),
		('[(eye) dropper/Pasteur pipette](eye%20dropper.md)', '![{}](../archives/Wikimedia%20Commons/Transfer%20pipette.jpg)', '',),
		('dropping bottle', '![{}](../archives/Wikimedia%20Commons/Dropper%20with%20vial.jpg)', 'literally bottle with dropper',),
		('[electronic balance](weighing%20scale.md)', '![{}](../archives/Wikimedia%20Commons/Weighing%20balance,%20MNIT.jpg)', '',),
		('[evaporating dish](evaporating%20dish.md)', '![{}](../archives/Wikimedia%20Commons/Abdampfschalen%20verschiedene%20Groessen.jpg)', '',),
		('[filter funnel](filter%20funnel.md)', '![{}](../archives/Wikimedia%20Commons/High-Speed%20Filter%20Funnel-2.jpg)', '',),
		('[flat-bottom(ed) flask](flat-bottom%20flask.md)', '![{}](../archives/Wikimedia%20Commons/TGI%20250.jpg)', '',),
		('[gas jar/pneumatic trough](pneumatic%20trough.md)', '![{}](../archives/Wikimedia%20Commons/Gas-Pak%20jar.jpg)', '',),
		('[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)', '![{}](../archives/Wikimedia%20Commons/Stirring%20rod.jpg)', '',),
		('[graduated pipette](graduated%20pipette.md)', '![{}](../archives/Wikimedia%20Commons/Mohr%20and%20Sero.jpg)', rinse_water_soln,),
		('[heat-resistant mat/heatproof mat](heatproof%20mat.md)', '![{}](../archives/Wikimedia%20Commons/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg)', '',),
		('[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)', '![{}](../archives/Wikimedia%20Commons/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg)', '',),
		('[mortar and pestle](mortar%20and%20pestle.md)', '![{}](../archives/Wikimedia%20Commons/White-Mortar-and-Pestle.jpg)', '',),
		('[pipeclay triangle](pipeclay%20triangle.md)', '![{}](../archives/Wikimedia%20Commons/Pipeclay%20triangle.jpg)', '',),
		('[reagent bottle](reagent%20bottle.md)', '![{}](../archives/Wikimedia%20Commons/Dark%20bottle%20with%20ground%20glass%20plug.jpg)', '',),
		('[round-bottom(ed) flask](round-bottom%20flask.md)', '![{}](../archives/Wikimedia%20Commons/Verrerie-p1030896.jpg)', '',),
		('[rubber bulb](rubber%20bulb.md)', '![{}](../archives/Wikimedia%20Commons/Rubber%20bulb%205.jpg)', '',),
		('[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)', '![{}](../archives/Wikimedia%20Commons/Rubber%20stopper%20holes.jpg)', '',),
		('[safety spectacles/safety glasses/goggles](goggles.md)', '![{}](../archives/Wikimedia%20Commons/Safety%20Goggles.jpg)', '',),
		('[spatula](spatula.md)', '![{}](../archives/Wikimedia%20Commons/Laboratory%20Spatula.JPG)', '',),
		('[stand/retort stand/ring stand/support stand](retort%20stand.md)', '![{}](../archives/Wikimedia%20Commons/Retort%20stand.jpg)', '',),
		('[test tube](test%20tube.md), boiling tube', '![{}](../archives/Wikimedia%20Commons/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg)', 'boiling tube: scaled-up to avoid [bumping](bumping%20(chemistry).md)',),
		('[test tube brush](test%20tube%20brush.md)', '![{}](../archives/Wikimedia%20Commons/Test%20tube%20brushes.jpg)', '',),
		('[test tube holder](test%20tube%20holder.md)', '![{}](../archives/Wikimedia%20Commons/Test%20Tube%20Holder2%202015.JPG)', '',),
		('[test tube rack](test%20tube%20rack.md)', '![{}](../archives/Wikimedia%20Commons/Metal%20tube%20rack-laboratory%202.jpg)', '',),
		('[thermometer](thermometer.md)', '![{}](../archives/Wikimedia%20Commons/Mercury%20Thermometer.jpg)', '',),
		('[tripod](tripod.md)', '![{}](../archives/Wikimedia%20Commons/Laboratory%20tripod.jpg)', '',),
		('[volumetric flask](volumetric%20flask.md)', '![{}](../archives/Wikimedia%20Commons/10mL%20Messkolben%20mit%20Schliff%20A.jpg)', rinse_water,),
		('[volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)', '![{}](../archives/Wikimedia%20Commons/Vollpipetten.jpg)', rinse_water_soln,),
		('[wash bottle](wash%20bottle.md)', '![{}](../archives/Wikimedia%20Commons/Lab%20wash-bottles%20water%20EtOH.jpg)', '',),
		('[watch glass](watch%20glass.md)', '![{}](../archives/Wikimedia%20Commons/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg)', '',),
		('[weighing bottle](weighing%20bottle.md)', '![{}](../archives/Wikimedia%20Commons/Weighing%20bottles.jpg)', '',),
		('[wire gauze](wire%20gauze.md)', '![{}](../archives/Wikimedia%20Commons/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg)', '',),
	),
	lambda datum: (
		f'{cloze(datum[0])}<br/>{cloze(datum[1].format(markdown_sanitizer(datum[0])))}',
		cloze(datum[2]),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="fadd2e"--><!-- The following content is generated at 2023-04-09T17:42:57.282099+08:00. Any edits will be overridden! -->

> | name & image | description |
> |-|-|
> | {{[Bunsen burner](Bunsen%20burner.md)}}<br/>{{![Bunsen burner](../archives/Wikimedia%20Commons/Bunsen%20burner.jpg)}} |  |
> | {{[Liebig condenser](Liebig%20condenser.md)}}<br/>{{![Liebig condenser](../archives/Wikimedia%20Commons/LiebigCondenser.jpg)}} |  |
> | {{[beaker](beaker.md)}}<br/>{{![beaker](../archives/Wikimedia%20Commons/Glassware-%20Beaker.jpg)}} |  |
> | {{[burette](burette.md)}}<br/>{{![burette](../archives/Wikimedia%20Commons/Burette.svg)}} | {{Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delievered.}} |
> | {{[burette clamp](burette%20clamp.md)}}<br/>{{![burette clamp](../archives/Wikimedia%20Commons/Burette%20with%20Clamp(3).jpg)}} |  |
> | {{[clamp](clamp.md)}}<br/>{{![clamp](../archives/Wikimedia%20Commons/Utility%20clamp1.jpg)}} |  |
> | {{[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)}}<br/>{{![conical flask/Erlenmeyer flask/titration flask](../archives/Wikimedia%20Commons/250%20mL%20Erlenmeyer%20flask.jpg)}} | {{Rinse the equipment with deionized [water](water.md) before use.}} |
> | {{[crucible](crucible.md)}}<br/>{{![crucible](../archives/Wikimedia%20Commons/Czochralski%20method%20used%20crucible%201.jpg)}} |  |
> | {{[crucible tongs](crucible%20tongs.md)}}<br/>{{![crucible tongs](../archives/Wikimedia%20Commons/Crucible%20tong.jpg)}} |  |
> | {{[desiccator](desiccator.md)}}<br/>{{![desiccator](../archives/Wikimedia%20Commons/Desiccator.jpg)}} |  |
> | {{[(eye) dropper/Pasteur pipette](eye%20dropper.md)}}<br/>{{![(eye) dropper/Pasteur pipette](../archives/Wikimedia%20Commons/Transfer%20pipette.jpg)}} |  |
> | {{dropping bottle}}<br/>{{![dropping bottle](../archives/Wikimedia%20Commons/Dropper%20with%20vial.jpg)}} | {{literally bottle with dropper}} |
> | {{[electronic balance](weighing%20scale.md)}}<br/>{{![electronic balance](../archives/Wikimedia%20Commons/Weighing%20balance,%20MNIT.jpg)}} |  |
> | {{[evaporating dish](evaporating%20dish.md)}}<br/>{{![evaporating dish](../archives/Wikimedia%20Commons/Abdampfschalen%20verschiedene%20Groessen.jpg)}} |  |
> | {{[filter funnel](filter%20funnel.md)}}<br/>{{![filter funnel](../archives/Wikimedia%20Commons/High-Speed%20Filter%20Funnel-2.jpg)}} |  |
> | {{[flat-bottom(ed) flask](flat-bottom%20flask.md)}}<br/>{{![flat-bottom(ed) flask](../archives/Wikimedia%20Commons/TGI%20250.jpg)}} |  |
> | {{[gas jar/pneumatic trough](pneumatic%20trough.md)}}<br/>{{![gas jar/pneumatic trough](../archives/Wikimedia%20Commons/Gas-Pak%20jar.jpg)}} |  |
> | {{[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)}}<br/>{{![glass stirring rod/glass rod/stir(ring) rod](../archives/Wikimedia%20Commons/Stirring%20rod.jpg)}} |  |
> | {{[graduated pipette](graduated%20pipette.md)}}<br/>{{![graduated pipette](../archives/Wikimedia%20Commons/Mohr%20and%20Sero.jpg)}} | {{Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delievered.}} |
> | {{[heat-resistant mat/heatproof mat](heatproof%20mat.md)}}<br/>{{![heat-resistant mat/heatproof mat](../archives/Wikimedia%20Commons/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg)}} |  |
> | {{[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)}}<br/>{{![measuring cylinder/graduated cylinder/mixing cylinder](../archives/Wikimedia%20Commons/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg)}} |  |
> | {{[mortar and pestle](mortar%20and%20pestle.md)}}<br/>{{![mortar and pestle](../archives/Wikimedia%20Commons/White-Mortar-and-Pestle.jpg)}} |  |
> | {{[pipeclay triangle](pipeclay%20triangle.md)}}<br/>{{![pipeclay triangle](../archives/Wikimedia%20Commons/Pipeclay%20triangle.jpg)}} |  |
> | {{[reagent bottle](reagent%20bottle.md)}}<br/>{{![reagent bottle](../archives/Wikimedia%20Commons/Dark%20bottle%20with%20ground%20glass%20plug.jpg)}} |  |
> | {{[round-bottom(ed) flask](round-bottom%20flask.md)}}<br/>{{![round-bottom(ed) flask](../archives/Wikimedia%20Commons/Verrerie-p1030896.jpg)}} |  |
> | {{[rubber bulb](rubber%20bulb.md)}}<br/>{{![rubber bulb](../archives/Wikimedia%20Commons/Rubber%20bulb%205.jpg)}} |  |
> | {{[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)}}<br/>{{![rubber stopper/rubber bung/rubber cork](../archives/Wikimedia%20Commons/Rubber%20stopper%20holes.jpg)}} |  |
> | {{[safety spectacles/safety glasses/goggles](goggles.md)}}<br/>{{![safety spectacles/safety glasses/goggles](../archives/Wikimedia%20Commons/Safety%20Goggles.jpg)}} |  |
> | {{[spatula](spatula.md)}}<br/>{{![spatula](../archives/Wikimedia%20Commons/Laboratory%20Spatula.JPG)}} |  |
> | {{[stand/retort stand/ring stand/support stand](retort%20stand.md)}}<br/>{{![stand/retort stand/ring stand/support stand](../archives/Wikimedia%20Commons/Retort%20stand.jpg)}} |  |
> | {{[test tube](test%20tube.md), boiling tube}}<br/>{{![test tube, boiling tube](../archives/Wikimedia%20Commons/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg)}} | {{boiling tube: scaled-up to avoid [bumping](bumping%20(chemistry).md)}} |
> | {{[test tube brush](test%20tube%20brush.md)}}<br/>{{![test tube brush](../archives/Wikimedia%20Commons/Test%20tube%20brushes.jpg)}} |  |
> | {{[test tube holder](test%20tube%20holder.md)}}<br/>{{![test tube holder](../archives/Wikimedia%20Commons/Test%20Tube%20Holder2%202015.JPG)}} |  |
> | {{[test tube rack](test%20tube%20rack.md)}}<br/>{{![test tube rack](../archives/Wikimedia%20Commons/Metal%20tube%20rack-laboratory%202.jpg)}} |  |
> | {{[thermometer](thermometer.md)}}<br/>{{![thermometer](../archives/Wikimedia%20Commons/Mercury%20Thermometer.jpg)}} |  |
> | {{[tripod](tripod.md)}}<br/>{{![tripod](../archives/Wikimedia%20Commons/Laboratory%20tripod.jpg)}} |  |
> | {{[volumetric flask](volumetric%20flask.md)}}<br/>{{![volumetric flask](../archives/Wikimedia%20Commons/10mL%20Messkolben%20mit%20Schliff%20A.jpg)}} | {{Rinse the equipment with deionized [water](water.md) before use.}} |
> | {{[volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)}}<br/>{{![volumetric pipette/bulb pipette/belly pipette](../archives/Wikimedia%20Commons/Vollpipetten.jpg)}} | {{Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delievered.}} |
> | {{[wash bottle](wash%20bottle.md)}}<br/>{{![wash bottle](../archives/Wikimedia%20Commons/Lab%20wash-bottles%20water%20EtOH.jpg)}} |  |
> | {{[watch glass](watch%20glass.md)}}<br/>{{![watch glass](../archives/Wikimedia%20Commons/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg)}} |  |
> | {{[weighing bottle](weighing%20bottle.md)}}<br/>{{![weighing bottle](../archives/Wikimedia%20Commons/Weighing%20bottles.jpg)}} |  |
> | {{[wire gauze](wire%20gauze.md)}}<br/>{{![wire gauze](../archives/Wikimedia%20Commons/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg)}} |  |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b81237"--><!-- The following content is generated at 2023-03-23T16:01:43.594725+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[Bunsen burner](Bunsen%20burner.md)
2. [Bunsen burner](Bunsen%20burner.md)→:::←[Liebig condenser](Liebig%20condenser.md)
3. [Liebig condenser](Liebig%20condenser.md)→:::←[beaker](beaker.md)
4. [beaker](beaker.md)→:::←[burette](burette.md)
5. [burette](burette.md)→:::←[burette clamp](burette%20clamp.md)
6. [burette clamp](burette%20clamp.md)→:::←[clamp](clamp.md)
7. [clamp](clamp.md)→:::←[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)
8. [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)→:::←[crucible](crucible.md)
9. [crucible](crucible.md)→:::←[crucible tongs](crucible%20tongs.md)
10. [crucible tongs](crucible%20tongs.md)→:::←[desiccator](desiccator.md)
11. [desiccator](desiccator.md)→:::←[(eye) dropper/Pasteur pipette](eye%20dropper.md)
12. [(eye) dropper/Pasteur pipette](eye%20dropper.md)→:::←dropping bottle
13. dropping bottle→:::←[electronic balance](weighing%20scale.md)
14. [electronic balance](weighing%20scale.md)→:::←[evaporating dish](evaporating%20dish.md)
15. [evaporating dish](evaporating%20dish.md)→:::←[filter funnel](filter%20funnel.md)
16. [filter funnel](filter%20funnel.md)→:::←[flat-bottom(ed) flask](flat-bottom%20flask.md)
17. [flat-bottom(ed) flask](flat-bottom%20flask.md)→:::←[gas jar/pneumatic trough](pneumatic%20trough.md)
18. [gas jar/pneumatic trough](pneumatic%20trough.md)→:::←[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)
19. [glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)→:::←[graduated pipette](graduated%20pipette.md)
20. [graduated pipette](graduated%20pipette.md)→:::←[heat-resistant mat/heatproof mat](heatproof%20mat.md)
21. [heat-resistant mat/heatproof mat](heatproof%20mat.md)→:::←[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)
22. [measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)→:::←[mortar and pestle](mortar%20and%20pestle.md)
23. [mortar and pestle](mortar%20and%20pestle.md)→:::←[pipeclay triangle](pipeclay%20triangle.md)
24. [pipeclay triangle](pipeclay%20triangle.md)→:::←[reagent bottle](reagent%20bottle.md)
25. [reagent bottle](reagent%20bottle.md)→:::←[round-bottom(ed) flask](round-bottom%20flask.md)
26. [round-bottom(ed) flask](round-bottom%20flask.md)→:::←[rubber bulb](rubber%20bulb.md)
27. [rubber bulb](rubber%20bulb.md)→:::←[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)
28. [rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)→:::←[safety spectacles/safety glasses/goggles](goggles.md)
29. [safety spectacles/safety glasses/goggles](goggles.md)→:::←[spatula](spatula.md)
30. [spatula](spatula.md)→:::←[stand/retort stand/ring stand/support stand](retort%20stand.md)
31. [stand/retort stand/ring stand/support stand](retort%20stand.md)→:::←[test tube](test%20tube.md), boiling tube
32. [test tube](test%20tube.md), boiling tube→:::←[test tube brush](test%20tube%20brush.md)
33. [test tube brush](test%20tube%20brush.md)→:::←[test tube holder](test%20tube%20holder.md)
34. [test tube holder](test%20tube%20holder.md)→:::←[test tube rack](test%20tube%20rack.md)
35. [test tube rack](test%20tube%20rack.md)→:::←[thermometer](thermometer.md)
36. [thermometer](thermometer.md)→:::←[tripod](tripod.md)
37. [tripod](tripod.md)→:::←[volumetric flask](volumetric%20flask.md)
38. [volumetric flask](volumetric%20flask.md)→:::←[volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)
39. [volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)→:::←[wash bottle](wash%20bottle.md)
40. [wash bottle](wash%20bottle.md)→:::←[watch glass](watch%20glass.md)
41. [watch glass](watch%20glass.md)→:::←[weighing bottle](weighing%20bottle.md)
42. [weighing bottle](weighing%20bottle.md)→:::←[wire gauze](wire%20gauze.md)
43. [wire gauze](wire%20gauze.md)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->