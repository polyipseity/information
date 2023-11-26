---
aliases:
  - laboratory apparatus
  - laboratory equipment
  - laboratory equipments
  - laboratory instrument
  - laboratory instruments
tags:
  - flashcards/general/laboratory_equipment
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# laboratory equipment

## examples

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain
from pytextgen.gen import markdown_sanitizer as _md_san
e = __env__
rinse_water = 'Rinse the equipment with deionized [water](water.md) before use.'
rinse_water_soln = 'Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered.'
table = (
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
)
table = tuple((*entry[:1], entry[1].format(_md_san(entry[0])), *entry[2:]) for entry in table)
return _chain.from_iterable(await _gather(
  memorize_table(
    e.cwf_sects('fadd2e', 'b81237'),
    ('name & image', 'description',),
    table,
    lambda datum: (f'{datum[0]}<br/>{datum[1]}', *datum[2:]),
  ),
  memorize_map(
    e.cwf_sects(None, 'dd23', 'f002'),
    items_to_map(*(entry[:2] for entry in table)),
  ),
  memorize_map(
    e.cwf_sects(None, '3934', None),
    items_to_map(*((entry[0], entry[2]) for entry in table if entry[2])),
  ),
))
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="fadd2e"--><!-- The following content is generated at 2023-11-26T19:12:56.438295+08:00. Any edits will be overridden! -->

> | name & image | description |
> |-|-|
> | [Bunsen burner](Bunsen%20burner.md)<br/>![Bunsen burner](../archives/Wikimedia%20Commons/Bunsen%20burner.jpg) |  |
> | [Liebig condenser](Liebig%20condenser.md)<br/>![Liebig condenser](../archives/Wikimedia%20Commons/LiebigCondenser.jpg) |  |
> | [beaker](beaker.md)<br/>![beaker](../archives/Wikimedia%20Commons/Glassware-%20Beaker.jpg) |  |
> | [burette](burette.md)<br/>![burette](../archives/Wikimedia%20Commons/Burette.svg) | Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered. |
> | [burette clamp](burette%20clamp.md)<br/>![burette clamp](../archives/Wikimedia%20Commons/Burette%20with%20Clamp(3).jpg) |  |
> | [clamp](clamp.md)<br/>![clamp](../archives/Wikimedia%20Commons/Utility%20clamp1.jpg) |  |
> | [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)<br/>![conical flask/Erlenmeyer flask/titration flask](../archives/Wikimedia%20Commons/250%20mL%20Erlenmeyer%20flask.jpg) | Rinse the equipment with deionized [water](water.md) before use. |
> | [crucible](crucible.md)<br/>![crucible](../archives/Wikimedia%20Commons/Czochralski%20method%20used%20crucible%201.jpg) |  |
> | [crucible tongs](crucible%20tongs.md)<br/>![crucible tongs](../archives/Wikimedia%20Commons/Crucible%20tong.jpg) |  |
> | [desiccator](desiccator.md)<br/>![desiccator](../archives/Wikimedia%20Commons/Desiccator.jpg) |  |
> | [(eye) dropper/Pasteur pipette](eye%20dropper.md)<br/>![(eye) dropper/Pasteur pipette](../archives/Wikimedia%20Commons/Transfer%20pipette.jpg) |  |
> | dropping bottle<br/>![dropping bottle](../archives/Wikimedia%20Commons/Dropper%20with%20vial.jpg) | literally bottle with dropper |
> | [electronic balance](weighing%20scale.md)<br/>![electronic balance](../archives/Wikimedia%20Commons/Weighing%20balance,%20MNIT.jpg) |  |
> | [evaporating dish](evaporating%20dish.md)<br/>![evaporating dish](../archives/Wikimedia%20Commons/Abdampfschalen%20verschiedene%20Groessen.jpg) |  |
> | [filter funnel](filter%20funnel.md)<br/>![filter funnel](../archives/Wikimedia%20Commons/High-Speed%20Filter%20Funnel-2.jpg) |  |
> | [flat-bottom(ed) flask](flat-bottom%20flask.md)<br/>![flat-bottom(ed) flask](../archives/Wikimedia%20Commons/TGI%20250.jpg) |  |
> | [gas jar/pneumatic trough](pneumatic%20trough.md)<br/>![gas jar/pneumatic trough](../archives/Wikimedia%20Commons/Gas-Pak%20jar.jpg) |  |
> | [glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)<br/>![glass stirring rod/glass rod/stir(ring) rod](../archives/Wikimedia%20Commons/Stirring%20rod.jpg) |  |
> | [graduated pipette](graduated%20pipette.md)<br/>![graduated pipette](../archives/Wikimedia%20Commons/Mohr%20and%20Sero.jpg) | Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered. |
> | [heat-resistant mat/heatproof mat](heatproof%20mat.md)<br/>![heat-resistant mat/heatproof mat](../archives/Wikimedia%20Commons/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg) |  |
> | [measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)<br/>![measuring cylinder/graduated cylinder/mixing cylinder](../archives/Wikimedia%20Commons/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg) |  |
> | [mortar and pestle](mortar%20and%20pestle.md)<br/>![mortar and pestle](../archives/Wikimedia%20Commons/White-Mortar-and-Pestle.jpg) |  |
> | [pipeclay triangle](pipeclay%20triangle.md)<br/>![pipeclay triangle](../archives/Wikimedia%20Commons/Pipeclay%20triangle.jpg) |  |
> | [reagent bottle](reagent%20bottle.md)<br/>![reagent bottle](../archives/Wikimedia%20Commons/Dark%20bottle%20with%20ground%20glass%20plug.jpg) |  |
> | [round-bottom(ed) flask](round-bottom%20flask.md)<br/>![round-bottom(ed) flask](../archives/Wikimedia%20Commons/Verrerie-p1030896.jpg) |  |
> | [rubber bulb](rubber%20bulb.md)<br/>![rubber bulb](../archives/Wikimedia%20Commons/Rubber%20bulb%205.jpg) |  |
> | [rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)<br/>![rubber stopper/rubber bung/rubber cork](../archives/Wikimedia%20Commons/Rubber%20stopper%20holes.jpg) |  |
> | [safety spectacles/safety glasses/goggles](goggles.md)<br/>![safety spectacles/safety glasses/goggles](../archives/Wikimedia%20Commons/Safety%20Goggles.jpg) |  |
> | [spatula](spatula.md)<br/>![spatula](../archives/Wikimedia%20Commons/Laboratory%20Spatula.JPG) |  |
> | [stand/retort stand/ring stand/support stand](retort%20stand.md)<br/>![stand/retort stand/ring stand/support stand](../archives/Wikimedia%20Commons/Retort%20stand.jpg) |  |
> | [test tube](test%20tube.md), boiling tube<br/>![test tube, boiling tube](../archives/Wikimedia%20Commons/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg) | boiling tube: scaled-up to avoid [bumping](bumping%20(chemistry).md) |
> | [test tube brush](test%20tube%20brush.md)<br/>![test tube brush](../archives/Wikimedia%20Commons/Test%20tube%20brushes.jpg) |  |
> | [test tube holder](test%20tube%20holder.md)<br/>![test tube holder](../archives/Wikimedia%20Commons/Test%20Tube%20Holder2%202015.JPG) |  |
> | [test tube rack](test%20tube%20rack.md)<br/>![test tube rack](../archives/Wikimedia%20Commons/Metal%20tube%20rack-laboratory%202.jpg) |  |
> | [thermometer](thermometer.md)<br/>![thermometer](../archives/Wikimedia%20Commons/Mercury%20Thermometer.jpg) |  |
> | [tripod](tripod.md)<br/>![tripod](../archives/Wikimedia%20Commons/Laboratory%20tripod.jpg) |  |
> | [volumetric flask](volumetric%20flask.md)<br/>![volumetric flask](../archives/Wikimedia%20Commons/10mL%20Messkolben%20mit%20Schliff%20A.jpg) | Rinse the equipment with deionized [water](water.md) before use. |
> | [volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)<br/>![volumetric pipette/bulb pipette/belly pipette](../archives/Wikimedia%20Commons/Vollpipetten.jpg) | Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered. |
> | [wash bottle](wash%20bottle.md)<br/>![wash bottle](../archives/Wikimedia%20Commons/Lab%20wash-bottles%20water%20EtOH.jpg) |  |
> | [watch glass](watch%20glass.md)<br/>![watch glass](../archives/Wikimedia%20Commons/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg) |  |
> | [weighing bottle](weighing%20bottle.md)<br/>![weighing bottle](../archives/Wikimedia%20Commons/Weighing%20bottles.jpg) |  |
> | [wire gauze](wire%20gauze.md)<br/>![wire gauze](../archives/Wikimedia%20Commons/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg) |  |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b81237"--><!-- The following content is generated at 2023-03-23T16:01:43.594725+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[Bunsen burner](Bunsen%20burner.md) <!--SR:!2023-12-22,199,310!2024-04-04,284,330-->
2. [Bunsen burner](Bunsen%20burner.md)→:::←[Liebig condenser](Liebig%20condenser.md) <!--SR:!2024-04-10,290,330!2024-04-17,295,330-->
3. [Liebig condenser](Liebig%20condenser.md)→:::←[beaker](beaker.md) <!--SR:!2025-06-11,595,310!2024-04-28,301,330-->
4. [beaker](beaker.md)→:::←[burette](burette.md) <!--SR:!2024-01-21,134,250!2024-04-05,285,330-->
5. [burette](burette.md)→:::←[burette clamp](burette%20clamp.md) <!--SR:!2024-04-21,294,330!2024-03-01,256,330-->
6. [burette clamp](burette%20clamp.md)→:::←[clamp](clamp.md) <!--SR:!2024-05-03,306,330!2024-05-31,329,330-->
7. [clamp](clamp.md)→:::←[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md) <!--SR:!2024-05-24,192,230!2023-11-30,18,170-->
8. [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)→:::←[crucible](crucible.md) <!--SR:!2023-12-13,68,150!2024-06-25,290,270-->
9. [crucible](crucible.md)→:::←[crucible tongs](crucible%20tongs.md) <!--SR:!2024-03-19,274,330!2024-03-17,272,330-->
10. [crucible tongs](crucible%20tongs.md)→:::←[desiccator](desiccator.md) <!--SR:!2024-01-15,204,310!2023-12-14,75,190-->
11. [desiccator](desiccator.md)→:::←[(eye) dropper/Pasteur pipette](eye%20dropper.md) <!--SR:!2024-07-24,351,290!2024-01-26,208,310-->
12. [(eye) dropper/Pasteur pipette](eye%20dropper.md)→:::←dropping bottle <!--SR:!2023-12-29,205,310!2024-04-06,286,330-->
13. dropping bottle→:::←[electronic balance](weighing%20scale.md) <!--SR:!2024-10-04,364,290!2024-01-01,53,170-->
14. [electronic balance](weighing%20scale.md)→:::←[evaporating dish](evaporating%20dish.md) <!--SR:!2023-12-29,144,230!2023-12-10,46,250-->
15. [evaporating dish](evaporating%20dish.md)→:::←[filter funnel](filter%20funnel.md) <!--SR:!2023-12-18,66,250!2024-06-27,292,270-->
16. [filter funnel](filter%20funnel.md)→:::←[flat-bottom(ed) flask](flat-bottom%20flask.md) <!--SR:!2023-12-05,127,230!2023-12-10,187,310-->
17. [flat-bottom(ed) flask](flat-bottom%20flask.md)→:::←[gas jar/pneumatic trough](pneumatic%20trough.md) <!--SR:!2024-01-03,159,250!2023-12-04,9,150-->
18. [gas jar/pneumatic trough](pneumatic%20trough.md)→:::←[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md) <!--SR:!2023-11-28,24,190!2024-10-15,381,290-->
19. [glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)→:::←[graduated pipette](graduated%20pipette.md) <!--SR:!2023-12-07,118,250!2024-01-24,74,150-->
20. [graduated pipette](graduated%20pipette.md)→:::←[heat-resistant mat/heatproof mat](heatproof%20mat.md) <!--SR:!2024-02-02,189,250!2024-02-08,85,210-->
21. [heat-resistant mat/heatproof mat](heatproof%20mat.md)→:::←[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md) <!--SR:!2024-08-22,361,290!2024-05-08,215,270-->
22. [measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)→:::←[mortar and pestle](mortar%20and%20pestle.md) <!--SR:!2023-12-12,67,150!2024-08-29,279,250-->
23. [mortar and pestle](mortar%20and%20pestle.md)→:::←[pipeclay triangle](pipeclay%20triangle.md) <!--SR:!2024-01-31,68,230!2024-06-26,291,270-->
24. [pipeclay triangle](pipeclay%20triangle.md)→:::←[reagent bottle](reagent%20bottle.md) <!--SR:!2024-04-19,249,270!2023-12-14,31,170-->
25. [reagent bottle](reagent%20bottle.md)→:::←[round-bottom(ed) flask](round-bottom%20flask.md) <!--SR:!2024-02-15,132,250!2024-04-09,155,270-->
26. [round-bottom(ed) flask](round-bottom%20flask.md)→:::←[rubber bulb](rubber%20bulb.md) <!--SR:!2023-12-01,32,170!2024-04-04,174,210-->
27. [rubber bulb](rubber%20bulb.md)→:::←[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md) <!--SR:!2024-02-19,207,270!2024-08-23,362,290-->
28. [rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)→:::←[safety spectacles/safety glasses/goggles](goggles.md) <!--SR:!2023-12-10,23,170!2024-03-25,198,230-->
29. [safety spectacles/safety glasses/goggles](goggles.md)→:::←[spatula](spatula.md) <!--SR:!2024-06-03,278,270!2024-08-14,358,290-->
30. [spatula](spatula.md)→:::←[stand/retort stand/ring stand/support stand](retort%20stand.md) <!--SR:!2024-06-16,254,230!2024-03-22,224,290-->
31. [stand/retort stand/ring stand/support stand](retort%20stand.md)→:::←[test tube](test%20tube.md), boiling tube <!--SR:!2024-01-30,122,250!2024-01-30,166,230-->
32. [test tube](test%20tube.md), boiling tube→:::←[test tube brush](test%20tube%20brush.md) <!--SR:!2024-06-04,333,330!2024-06-07,336,330-->
33. [test tube brush](test%20tube%20brush.md)→:::←[test tube holder](test%20tube%20holder.md) <!--SR:!2024-06-03,234,270!2024-04-18,296,330-->
34. [test tube holder](test%20tube%20holder.md)→:::←[test tube rack](test%20tube%20rack.md) <!--SR:!2024-08-09,355,290!2025-01-07,428,290-->
35. [test tube rack](test%20tube%20rack.md)→:::←[thermometer](thermometer.md) <!--SR:!2024-01-06,172,250!2024-01-14,127,250-->
36. [thermometer](thermometer.md)→:::←[tripod](tripod.md) <!--SR:!2024-02-06,203,270!2024-08-29,348,290-->
37. [tripod](tripod.md)→:::←[volumetric flask](volumetric%20flask.md) <!--SR:!2023-12-31,37,190!2025-04-05,511,310-->
38. [volumetric flask](volumetric%20flask.md)→:::←[volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md) <!--SR:!2024-03-07,219,270!2024-05-01,166,270-->
39. [volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)→:::←[wash bottle](wash%20bottle.md) <!--SR:!2024-09-12,363,290!2024-12-08,401,270-->
40. [wash bottle](wash%20bottle.md)→:::←[watch glass](watch%20glass.md) <!--SR:!2024-04-29,253,270!2023-12-15,63,270-->
41. [watch glass](watch%20glass.md)→:::←[weighing bottle](weighing%20bottle.md) <!--SR:!2024-01-24,206,310!2024-03-05,218,270-->
42. [weighing bottle](weighing%20bottle.md)→:::←[wire gauze](wire%20gauze.md) <!--SR:!2025-01-21,449,290!2025-03-31,507,310-->
43. [wire gauze](wire%20gauze.md)→:::←_(end)_ <!--SR:!2024-04-23,296,330!2024-03-23,272,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### name–image

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="dd23"--><!-- The following content is generated at 2023-11-26T19:26:50.536419+08:00. Any edits will be overridden! -->

1. [Bunsen burner](Bunsen%20burner.md)::![Bunsen burner](../archives/Wikimedia%20Commons/Bunsen%20burner.jpg) <!--SR:2024-03-02,256,330-->
2. [Liebig condenser](Liebig%20condenser.md)::![Liebig condenser](../archives/Wikimedia%20Commons/LiebigCondenser.jpg) <!--SR:2024-01-05,208,310-->
3. [beaker](beaker.md)::![beaker](../archives/Wikimedia%20Commons/Glassware-%20Beaker.jpg) <!--SR:2024-03-28,277,330-->
4. [burette](burette.md)::![burette](../archives/Wikimedia%20Commons/Burette.svg) <!--SR:2023-12-03,180,310-->
5. [burette clamp](burette%20clamp.md)::![burette clamp](../archives/Wikimedia%20Commons/Burette%20with%20Clamp(3).jpg) <!--SR:2025-01-03,427,290-->
6. [clamp](clamp.md)::![clamp](../archives/Wikimedia%20Commons/Utility%20clamp1.jpg) <!--SR:2024-05-14,317,330-->
7. [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)::![conical flask/Erlenmeyer flask/titration flask](../archives/Wikimedia%20Commons/250%20mL%20Erlenmeyer%20flask.jpg) <!--SR:2024-02-04,238,330-->
8. [crucible](crucible.md)::![crucible](../archives/Wikimedia%20Commons/Czochralski%20method%20used%20crucible%201.jpg) <!--SR:2024-02-02,236,330-->
9. [crucible tongs](crucible%20tongs.md)::![crucible tongs](../archives/Wikimedia%20Commons/Crucible%20tong.jpg) <!--SR:2024-04-29,302,330-->
10. [desiccator](desiccator.md)::![desiccator](../archives/Wikimedia%20Commons/Desiccator.jpg) <!--SR:2024-02-26,252,330-->
11. [(eye) dropper/Pasteur pipette](eye%20dropper.md)::![(eye) dropper/Pasteur pipette](../archives/Wikimedia%20Commons/Transfer%20pipette.jpg) <!--SR:2024-03-21,270,330-->
12. dropping bottle::![dropping bottle](../archives/Wikimedia%20Commons/Dropper%20with%20vial.jpg) <!--SR:2024-06-01,330,330-->
13. [electronic balance](weighing%20scale.md)::![electronic balance](../archives/Wikimedia%20Commons/Weighing%20balance,%20MNIT.jpg) <!--SR:2024-03-20,269,330-->
14. [evaporating dish](evaporating%20dish.md)::![evaporating dish](../archives/Wikimedia%20Commons/Abdampfschalen%20verschiedene%20Groessen.jpg) <!--SR:2024-04-16,294,330-->
15. [filter funnel](filter%20funnel.md)::![filter funnel](../archives/Wikimedia%20Commons/High-Speed%20Filter%20Funnel-2.jpg) <!--SR:2024-05-17,320,330-->
16. [flat-bottom(ed) flask](flat-bottom%20flask.md)::![flat-bottom(ed) flask](../archives/Wikimedia%20Commons/TGI%20250.jpg) <!--SR:2024-06-03,332,330-->
17. [gas jar/pneumatic trough](pneumatic%20trough.md)::![gas jar/pneumatic trough](../archives/Wikimedia%20Commons/Gas-Pak%20jar.jpg) <!--SR:2024-10-23,410,290-->
18. [glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)::![glass stirring rod/glass rod/stir(ring) rod](../archives/Wikimedia%20Commons/Stirring%20rod.jpg) <!--SR:2024-05-15,318,330-->
19. [graduated pipette](graduated%20pipette.md)::![graduated pipette](../archives/Wikimedia%20Commons/Mohr%20and%20Sero.jpg) <!--SR:2025-05-09,532,310-->
20. [heat-resistant mat/heatproof mat](heatproof%20mat.md)::![heat-resistant mat/heatproof mat](../archives/Wikimedia%20Commons/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg) <!--SR:2024-03-08,263,330-->
21. [measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)::![measuring cylinder/graduated cylinder/mixing cylinder](../archives/Wikimedia%20Commons/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg) <!--SR:2024-03-04,258,330-->
22. [mortar and pestle](mortar%20and%20pestle.md)::![mortar and pestle](../archives/Wikimedia%20Commons/White-Mortar-and-Pestle.jpg) <!--SR:2024-02-24,250,330-->
23. [pipeclay triangle](pipeclay%20triangle.md)::![pipeclay triangle](../archives/Wikimedia%20Commons/Pipeclay%20triangle.jpg) <!--SR:2023-12-11,188,310-->
24. [reagent bottle](reagent%20bottle.md)::![reagent bottle](../archives/Wikimedia%20Commons/Dark%20bottle%20with%20ground%20glass%20plug.jpg) <!--SR:2024-03-05,260,330-->
25. [round-bottom(ed) flask](round-bottom%20flask.md)::![round-bottom(ed) flask](../archives/Wikimedia%20Commons/Verrerie-p1030896.jpg) <!--SR:2024-04-01,281,330-->
26. [rubber bulb](rubber%20bulb.md)::![rubber bulb](../archives/Wikimedia%20Commons/Rubber%20bulb%205.jpg) <!--SR:2024-01-24,227,330-->
27. [rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)::![rubber stopper/rubber bung/rubber cork](../archives/Wikimedia%20Commons/Rubber%20stopper%20holes.jpg) <!--SR:2024-03-25,274,330-->
28. [safety spectacles/safety glasses/goggles](goggles.md)::![safety spectacles/safety glasses/goggles](../archives/Wikimedia%20Commons/Safety%20Goggles.jpg) <!--SR:2024-02-03,237,330-->
29. [spatula](spatula.md)::![spatula](../archives/Wikimedia%20Commons/Laboratory%20Spatula.JPG) <!--SR:2024-02-02,235,330-->
30. [stand/retort stand/ring stand/support stand](retort%20stand.md)::![stand/retort stand/ring stand/support stand](../archives/Wikimedia%20Commons/Retort%20stand.jpg) <!--SR:2024-04-14,292,330-->
31. [test tube](test%20tube.md), boiling tube::![test tube, boiling tube](../archives/Wikimedia%20Commons/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg) <!--SR:2023-12-13,190,310-->
32. [test tube brush](test%20tube%20brush.md)::![test tube brush](../archives/Wikimedia%20Commons/Test%20tube%20brushes.jpg) <!--SR:2024-03-01,255,330-->
33. [test tube holder](test%20tube%20holder.md)::![test tube holder](../archives/Wikimedia%20Commons/Test%20Tube%20Holder2%202015.JPG) <!--SR:2024-03-31,280,330-->
34. [test tube rack](test%20tube%20rack.md)::![test tube rack](../archives/Wikimedia%20Commons/Metal%20tube%20rack-laboratory%202.jpg) <!--SR:2024-04-03,283,330-->
35. [thermometer](thermometer.md)::![thermometer](../archives/Wikimedia%20Commons/Mercury%20Thermometer.jpg) <!--SR:2024-03-03,258,330-->
36. [tripod](tripod.md)::![tripod](../archives/Wikimedia%20Commons/Laboratory%20tripod.jpg) <!--SR:2024-04-19,297,330-->
37. [volumetric flask](volumetric%20flask.md)::![volumetric flask](../archives/Wikimedia%20Commons/10mL%20Messkolben%20mit%20Schliff%20A.jpg) <!--SR:2024-06-08,337,330-->
38. [volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)::![volumetric pipette/bulb pipette/belly pipette](../archives/Wikimedia%20Commons/Vollpipetten.jpg) <!--SR:2024-02-29,255,330-->
39. [wash bottle](wash%20bottle.md)::![wash bottle](../archives/Wikimedia%20Commons/Lab%20wash-bottles%20water%20EtOH.jpg) <!--SR:2024-04-22,295,330-->
40. [watch glass](watch%20glass.md)::![watch glass](../archives/Wikimedia%20Commons/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg) <!--SR:2023-12-20,184,310-->
41. [weighing bottle](weighing%20bottle.md)::![weighing bottle](../archives/Wikimedia%20Commons/Weighing%20bottles.jpg) <!--SR:2024-01-05,206,310-->
42. [wire gauze](wire%20gauze.md)::![wire gauze](../archives/Wikimedia%20Commons/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg) <!--SR:2024-03-02,257,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f002"--><!-- The following content is generated at 2023-11-26T19:26:50.455849+08:00. Any edits will be overridden! -->

1. ![Bunsen burner](../archives/Wikimedia%20Commons/Bunsen%20burner.jpg)::[Bunsen burner](Bunsen%20burner.md) <!--SR:2024-05-16,319,330-->
2. ![Liebig condenser](../archives/Wikimedia%20Commons/LiebigCondenser.jpg)::[Liebig condenser](Liebig%20condenser.md) <!--SR:2024-03-06,261,330-->
3. ![beaker](../archives/Wikimedia%20Commons/Glassware-%20Beaker.jpg)::[beaker](beaker.md) <!--SR:2024-02-25,251,330-->
4. ![burette](../archives/Wikimedia%20Commons/Burette.svg)::[burette](burette.md) <!--SR:2024-10-27,429,310-->
5. ![burette clamp](../archives/Wikimedia%20Commons/Burette%20with%20Clamp(3).jpg)::[burette clamp](burette%20clamp.md) <!--SR:2024-02-10,243,330-->
6. ![clamp](../archives/Wikimedia%20Commons/Utility%20clamp1.jpg)::[clamp](clamp.md) <!--SR:2024-03-03,257,330-->
7. ![conical flask/Erlenmeyer flask/titration flask](../archives/Wikimedia%20Commons/250%20mL%20Erlenmeyer%20flask.jpg)::[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md) <!--SR:2023-12-08,184,310-->
8. ![crucible](../archives/Wikimedia%20Commons/Czochralski%20method%20used%20crucible%201.jpg)::[crucible](crucible.md) <!--SR:2024-06-02,331,330-->
9. ![crucible tongs](../archives/Wikimedia%20Commons/Crucible%20tong.jpg)::[crucible tongs](crucible%20tongs.md) <!--SR:2024-02-27,253,330-->
10. ![desiccator](../archives/Wikimedia%20Commons/Desiccator.jpg)::[desiccator](desiccator.md) <!--SR:2024-01-14,217,310-->
11. ![(eye) dropper/Pasteur pipette](../archives/Wikimedia%20Commons/Transfer%20pipette.jpg)::[(eye) dropper/Pasteur pipette](eye%20dropper.md) <!--SR:2024-04-02,282,330-->
12. ![dropping bottle](../archives/Wikimedia%20Commons/Dropper%20with%20vial.jpg)::dropping bottle <!--SR:2024-03-22,271,330-->
13. ![electronic balance](../archives/Wikimedia%20Commons/Weighing%20balance,%20MNIT.jpg)::[electronic balance](weighing%20scale.md) <!--SR:2024-03-07,262,330-->
14. ![evaporating dish](../archives/Wikimedia%20Commons/Abdampfschalen%20verschiedene%20Groessen.jpg)::[evaporating dish](evaporating%20dish.md) <!--SR:2024-03-04,259,330-->
15. ![filter funnel](../archives/Wikimedia%20Commons/High-Speed%20Filter%20Funnel-2.jpg)::[filter funnel](filter%20funnel.md) <!--SR:2024-04-30,303,330-->
16. ![flat-bottom(ed) flask](../archives/Wikimedia%20Commons/TGI%20250.jpg)::[flat-bottom(ed) flask](flat-bottom%20flask.md) <!--SR:2024-02-08,241,330-->
17. ![gas jar/pneumatic trough](../archives/Wikimedia%20Commons/Gas-Pak%20jar.jpg)::[gas jar/pneumatic trough](pneumatic%20trough.md) <!--SR:2023-11-30,183,310-->
18. ![glass stirring rod/glass rod/stir(ring) rod](../archives/Wikimedia%20Commons/Stirring%20rod.jpg)::[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md) <!--SR:2025-03-18,535,310-->
19. ![graduated pipette](../archives/Wikimedia%20Commons/Mohr%20and%20Sero.jpg)::[graduated pipette](graduated%20pipette.md) <!--SR:2023-11-30,171,310-->
20. ![heat-resistant mat/heatproof mat](../archives/Wikimedia%20Commons/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg)::[heat-resistant mat/heatproof mat](heatproof%20mat.md) <!--SR:2023-12-02,172,310-->
21. ![measuring cylinder/graduated cylinder/mixing cylinder](../archives/Wikimedia%20Commons/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg)::[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md) <!--SR:2025-11-14,728,330-->
22. ![mortar and pestle](../archives/Wikimedia%20Commons/White-Mortar-and-Pestle.jpg)::[mortar and pestle](mortar%20and%20pestle.md) <!--SR:2024-03-09,264,330-->
23. ![pipeclay triangle](../archives/Wikimedia%20Commons/Pipeclay%20triangle.jpg)::[pipeclay triangle](pipeclay%20triangle.md) <!--SR:2024-05-01,304,330-->
24. ![reagent bottle](../archives/Wikimedia%20Commons/Dark%20bottle%20with%20ground%20glass%20plug.jpg)::[reagent bottle](reagent%20bottle.md) <!--SR:2024-02-09,242,330-->
25. ![round-bottom(ed) flask](../archives/Wikimedia%20Commons/Verrerie-p1030896.jpg)::[round-bottom(ed) flask](round-bottom%20flask.md) <!--SR:2024-04-09,289,330-->
26. ![rubber bulb](../archives/Wikimedia%20Commons/Rubber%20bulb%205.jpg)::[rubber bulb](rubber%20bulb.md) <!--SR:2023-12-04,186,310-->
27. ![rubber stopper/rubber bung/rubber cork](../archives/Wikimedia%20Commons/Rubber%20stopper%20holes.jpg)::[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md) <!--SR:2024-02-08,240,330-->
28. ![safety spectacles/safety glasses/goggles](../archives/Wikimedia%20Commons/Safety%20Goggles.jpg)::[safety spectacles/safety glasses/goggles](goggles.md) <!--SR:2024-03-18,273,330-->
29. ![spatula](../archives/Wikimedia%20Commons/Laboratory%20Spatula.JPG)::[spatula](spatula.md) <!--SR:2024-06-05,334,330-->
30. ![stand/retort stand/ring stand/support stand](../archives/Wikimedia%20Commons/Retort%20stand.jpg)::[stand/retort stand/ring stand/support stand](retort%20stand.md) <!--SR:2024-01-04,207,310-->
31. ![test tube, boiling tube](../archives/Wikimedia%20Commons/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg)::[test tube](test%20tube.md), boiling tube <!--SR:2024-06-06,335,330-->
32. ![test tube brush](../archives/Wikimedia%20Commons/Test%20tube%20brushes.jpg)::[test tube brush](test%20tube%20brush.md) <!--SR:2024-02-19,245,330-->
33. ![test tube holder](../archives/Wikimedia%20Commons/Test%20Tube%20Holder2%202015.JPG)::[test tube holder](test%20tube%20holder.md) <!--SR:2024-04-08,288,330-->
34. ![test tube rack](../archives/Wikimedia%20Commons/Metal%20tube%20rack-laboratory%202.jpg)::[test tube rack](test%20tube%20rack.md) <!--SR:2024-04-25,298,330-->
35. ![thermometer](../archives/Wikimedia%20Commons/Mercury%20Thermometer.jpg)::[thermometer](thermometer.md) <!--SR:2024-05-02,305,330-->
36. ![tripod](../archives/Wikimedia%20Commons/Laboratory%20tripod.jpg)::[tripod](tripod.md) <!--SR:2024-02-09,241,330-->
37. ![volumetric flask](../archives/Wikimedia%20Commons/10mL%20Messkolben%20mit%20Schliff%20A.jpg)::[volumetric flask](volumetric%20flask.md) <!--SR:2024-01-03,206,310-->
38. ![volumetric pipette/bulb pipette/belly pipette](../archives/Wikimedia%20Commons/Vollpipetten.jpg)::[volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md) <!--SR:2024-10-24,411,290-->
39. ![wash bottle](../archives/Wikimedia%20Commons/Lab%20wash-bottles%20water%20EtOH.jpg)::[wash bottle](wash%20bottle.md) <!--SR:2024-02-28,254,330-->
40. ![watch glass](../archives/Wikimedia%20Commons/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg)::[watch glass](watch%20glass.md) <!--SR:2024-04-07,287,330-->
41. ![weighing bottle](../archives/Wikimedia%20Commons/Weighing%20bottles.jpg)::[weighing bottle](weighing%20bottle.md) <!--SR:2024-03-27,276,330-->
42. ![wire gauze](../archives/Wikimedia%20Commons/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg)::[wire gauze](wire%20gauze.md) <!--SR:2024-03-24,273,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### name–description

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3934"--><!-- The following content is generated at 2023-11-26T19:11:13.226275+08:00. Any edits will be overridden! -->

1. [burette](burette.md)::Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered. <!--SR:2024-11-27,411,290-->
2. [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)::Rinse the equipment with deionized [water](water.md) before use. <!--SR:2024-04-24,297,330-->
3. dropping bottle::literally bottle with dropper <!--SR:2024-04-24,271,310-->
4. [graduated pipette](graduated%20pipette.md)::Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered. <!--SR:2023-12-07,153,250-->
5. [test tube](test%20tube.md), boiling tube::boiling tube: scaled-up to avoid [bumping](bumping%20(chemistry).md) <!--SR:2024-04-15,293,330-->
6. [volumetric flask](volumetric%20flask.md)::Rinse the equipment with deionized [water](water.md) before use. <!--SR:2024-12-24,471,310-->
7. [volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)::Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered. <!--SR:2024-12-15,463,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
