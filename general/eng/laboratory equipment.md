---
aliases:
  - laboratory apparatus
  - laboratory equipment
  - laboratory equipments
  - laboratory instrument
  - laboratory instruments
tags:
  - flashcard/active/general/eng/laboratory_equipment
  - language/in/English
---

# laboratory equipment

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## examples

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
from pytextgen.gen import markdown_sanitizer as _md_san
rinse_water = 'Rinse the equipment with deionized [water](water.md) before use.'
rinse_water_soln = 'Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered.'
table = (
  ('[Bunsen burner](Bunsen%20burner.md)', '![{}](../../archives/Wikimedia%20Commons/Bunsen%20burner.jpg)', '',),
  ('[Liebig condenser](Liebig%20condenser.md)', '![{}](../../archives/Wikimedia%20Commons/LiebigCondenser.jpg)', '',),
  ('[beaker](beaker.md)', '![{}](../../archives/Wikimedia%20Commons/Glassware-%20Beaker.jpg)', '',),
  ('[burette](burette.md)', '![{}](../../archives/Wikimedia%20Commons/Burette.svg)', rinse_water_soln,),
  ('[burette clamp](burette%20clamp.md)', '![{}](../../archives/Wikimedia%20Commons/Burette%20with%20Clamp(3).jpg)', '',),
  ('[clamp](clamp.md)', '![{}](../../archives/Wikimedia%20Commons/Utility%20clamp1.jpg)', '',),
  ('[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)', '![{}](../../archives/Wikimedia%20Commons/250%20mL%20Erlenmeyer%20flask.jpg)', rinse_water,),
  ('[crucible](crucible.md)', '![{}](../../archives/Wikimedia%20Commons/Czochralski%20method%20used%20crucible%201.jpg)', '',),
  ('[crucible tongs](crucible%20tongs.md)', '![{}](../../archives/Wikimedia%20Commons/Crucible%20tong.jpg)', '',),
  ('[desiccator](desiccator.md)', '![{}](../../archives/Wikimedia%20Commons/Desiccator.jpg)', '',),
  ('[(eye) dropper/Pasteur pipette](eye%20dropper.md)', '![{}](../../archives/Wikimedia%20Commons/Transfer%20pipette.jpg)', '',),
  ('dropping bottle', '![{}](../../archives/Wikimedia%20Commons/Dropper%20with%20vial.jpg)', 'literally bottle with dropper',),
  ('[electronic balance](weighing%20scale.md)', '![{}](../../archives/Wikimedia%20Commons/Weighing%20balance,%20MNIT.jpg)', '',),
  ('[evaporating dish](evaporating%20dish.md)', '![{}](../../archives/Wikimedia%20Commons/Abdampfschalen%20verschiedene%20Groessen.jpg)', '',),
  ('[filter funnel](filter%20funnel.md)', '![{}](../../archives/Wikimedia%20Commons/High-Speed%20Filter%20Funnel-2.jpg)', '',),
  ('[flat-bottom(ed) flask](flat-bottom%20flask.md)', '![{}](../../archives/Wikimedia%20Commons/TGI%20250.jpg)', '',),
  ('[gas jar/pneumatic trough](pneumatic%20trough.md)', '![{}](../../archives/Wikimedia%20Commons/Gas-Pak%20jar.jpg)', '',),
  ('[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)', '![{}](../../archives/Wikimedia%20Commons/Stirring%20rod.jpg)', '',),
  ('[graduated pipette](graduated%20pipette.md)', '![{}](../../archives/Wikimedia%20Commons/Mohr%20and%20Sero.jpg)', rinse_water_soln,),
  ('[heat-resistant mat/heatproof mat](heatproof%20mat.md)', '![{}](../../archives/Wikimedia%20Commons/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg)', '',),
  ('[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)', '![{}](../../archives/Wikimedia%20Commons/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg)', '',),
  ('[mortar and pestle](mortar%20and%20pestle.md)', '![{}](../../archives/Wikimedia%20Commons/White-Mortar-and-Pestle.jpg)', '',),
  ('[pipeclay triangle](pipeclay%20triangle.md)', '![{}](../../archives/Wikimedia%20Commons/Pipeclay%20triangle.jpg)', '',),
  ('[reagent bottle](reagent%20bottle.md)', '![{}](../../archives/Wikimedia%20Commons/Dark%20bottle%20with%20ground%20glass%20plug.jpg)', '',),
  ('[round-bottom(ed) flask](round-bottom%20flask.md)', '![{}](../../archives/Wikimedia%20Commons/Verrerie-p1030896.jpg)', '',),
  ('[rubber bulb](rubber%20bulb.md)', '![{}](../../archives/Wikimedia%20Commons/Rubber%20bulb%205.jpg)', '',),
  ('[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)', '![{}](../../archives/Wikimedia%20Commons/Rubber%20stopper%20holes.jpg)', '',),
  ('[safety spectacles/safety glasses/goggles](goggles.md)', '![{}](../../archives/Wikimedia%20Commons/Safety%20Goggles.jpg)', '',),
  ('[spatula](spatula.md)', '![{}](../../archives/Wikimedia%20Commons/Laboratory%20Spatula.JPG)', '',),
  ('[stand/retort stand/ring stand/support stand](retort%20stand.md)', '![{}](../../archives/Wikimedia%20Commons/Retort%20stand.jpg)', '',),
  ('[test tube](test%20tube.md), boiling tube', '![{}](../../archives/Wikimedia%20Commons/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg)', 'boiling tube: scaled-up to avoid [bumping](bumping%20(chemistry).md)',),
  ('[test tube brush](test%20tube%20brush.md)', '![{}](../../archives/Wikimedia%20Commons/Test%20tube%20brushes.jpg)', '',),
  ('[test tube holder](test%20tube%20holder.md)', '![{}](../../archives/Wikimedia%20Commons/Test%20Tube%20Holder2%202015.JPG)', '',),
  ('[test tube rack](test%20tube%20rack.md)', '![{}](../../archives/Wikimedia%20Commons/Metal%20tube%20rack-laboratory%202.jpg)', '',),
  ('[thermometer](thermometer.md)', '![{}](../../archives/Wikimedia%20Commons/Mercury%20Thermometer.jpg)', '',),
  ('[tripod](tripod.md)', '![{}](../../archives/Wikimedia%20Commons/Laboratory%20tripod.jpg)', '',),
  ('[volumetric flask](volumetric%20flask.md)', '![{}](../../archives/Wikimedia%20Commons/10mL%20Messkolben%20mit%20Schliff%20A.jpg)', rinse_water,),
  ('[volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)', '![{}](../../archives/Wikimedia%20Commons/Vollpipetten.jpg)', rinse_water_soln,),
  ('[wash bottle](wash%20bottle.md)', '![{}](../../archives/Wikimedia%20Commons/Lab%20wash-bottles%20water%20EtOH.jpg)', '',),
  ('[watch glass](watch%20glass.md)', '![{}](../../archives/Wikimedia%20Commons/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg)', '',),
  ('[weighing bottle](weighing%20bottle.md)', '![{}](../../archives/Wikimedia%20Commons/Weighing%20bottles.jpg)', '',),
  ('[wire gauze](wire%20gauze.md)', '![{}](../../archives/Wikimedia%20Commons/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg)', '',),
)
table = tuple((*entry[:1], entry[1].format(_md_san(entry[0])), *entry[2:]) for entry in table)
return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects('fadd2e', 'b81237'),
    ('name & image', 'description',),
    table,
    lambda datum: (f'{datum[0]}<br/>{datum[1]}', *datum[2:]),
  ),
  memorize_map(
    __env__.cwf_sects(None, 'dd23', 'f002'),
    items_to_map(*(entry[:2] for entry in table)),
  ),
  memorize_map(
    __env__.cwf_sects(None, '3934', None),
    items_to_map(*((entry[0], entry[2]) for entry in table if entry[2])),
  ),
))
```

<!--pytextgen generate section="fadd2e"--><!-- The following content is generated at 2023-11-26T19:12:56.438295+08:00. Any edits will be overridden! -->

> | name & image | description |
> |-|-|
> | [Bunsen burner](Bunsen%20burner.md)<br/>![Bunsen burner](../../archives/Wikimedia%20Commons/Bunsen%20burner.jpg) |  |
> | [Liebig condenser](Liebig%20condenser.md)<br/>![Liebig condenser](../../archives/Wikimedia%20Commons/LiebigCondenser.jpg) |  |
> | [beaker](beaker.md)<br/>![beaker](../../archives/Wikimedia%20Commons/Glassware-%20Beaker.jpg) |  |
> | [burette](burette.md)<br/>![burette](../../archives/Wikimedia%20Commons/Burette.svg) | Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered. |
> | [burette clamp](burette%20clamp.md)<br/>![burette clamp](../../archives/Wikimedia%20Commons/Burette%20with%20Clamp(3).jpg) |  |
> | [clamp](clamp.md)<br/>![clamp](../../archives/Wikimedia%20Commons/Utility%20clamp1.jpg) |  |
> | [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)<br/>![conical flask/Erlenmeyer flask/titration flask](../../archives/Wikimedia%20Commons/250%20mL%20Erlenmeyer%20flask.jpg) | Rinse the equipment with deionized [water](water.md) before use. |
> | [crucible](crucible.md)<br/>![crucible](../../archives/Wikimedia%20Commons/Czochralski%20method%20used%20crucible%201.jpg) |  |
> | [crucible tongs](crucible%20tongs.md)<br/>![crucible tongs](../../archives/Wikimedia%20Commons/Crucible%20tong.jpg) |  |
> | [desiccator](desiccator.md)<br/>![desiccator](../../archives/Wikimedia%20Commons/Desiccator.jpg) |  |
> | [(eye) dropper/Pasteur pipette](eye%20dropper.md)<br/>![(eye) dropper/Pasteur pipette](../../archives/Wikimedia%20Commons/Transfer%20pipette.jpg) |  |
> | dropping bottle<br/>![dropping bottle](../../archives/Wikimedia%20Commons/Dropper%20with%20vial.jpg) | literally bottle with dropper |
> | [electronic balance](weighing%20scale.md)<br/>![electronic balance](../../archives/Wikimedia%20Commons/Weighing%20balance,%20MNIT.jpg) |  |
> | [evaporating dish](evaporating%20dish.md)<br/>![evaporating dish](../../archives/Wikimedia%20Commons/Abdampfschalen%20verschiedene%20Groessen.jpg) |  |
> | [filter funnel](filter%20funnel.md)<br/>![filter funnel](../../archives/Wikimedia%20Commons/High-Speed%20Filter%20Funnel-2.jpg) |  |
> | [flat-bottom(ed) flask](flat-bottom%20flask.md)<br/>![flat-bottom(ed) flask](../../archives/Wikimedia%20Commons/TGI%20250.jpg) |  |
> | [gas jar/pneumatic trough](pneumatic%20trough.md)<br/>![gas jar/pneumatic trough](../../archives/Wikimedia%20Commons/Gas-Pak%20jar.jpg) |  |
> | [glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)<br/>![glass stirring rod/glass rod/stir(ring) rod](../../archives/Wikimedia%20Commons/Stirring%20rod.jpg) |  |
> | [graduated pipette](graduated%20pipette.md)<br/>![graduated pipette](../../archives/Wikimedia%20Commons/Mohr%20and%20Sero.jpg) | Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered. |
> | [heat-resistant mat/heatproof mat](heatproof%20mat.md)<br/>![heat-resistant mat/heatproof mat](../../archives/Wikimedia%20Commons/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg) |  |
> | [measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)<br/>![measuring cylinder/graduated cylinder/mixing cylinder](../../archives/Wikimedia%20Commons/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg) |  |
> | [mortar and pestle](mortar%20and%20pestle.md)<br/>![mortar and pestle](../../archives/Wikimedia%20Commons/White-Mortar-and-Pestle.jpg) |  |
> | [pipeclay triangle](pipeclay%20triangle.md)<br/>![pipeclay triangle](../../archives/Wikimedia%20Commons/Pipeclay%20triangle.jpg) |  |
> | [reagent bottle](reagent%20bottle.md)<br/>![reagent bottle](../../archives/Wikimedia%20Commons/Dark%20bottle%20with%20ground%20glass%20plug.jpg) |  |
> | [round-bottom(ed) flask](round-bottom%20flask.md)<br/>![round-bottom(ed) flask](../../archives/Wikimedia%20Commons/Verrerie-p1030896.jpg) |  |
> | [rubber bulb](rubber%20bulb.md)<br/>![rubber bulb](../../archives/Wikimedia%20Commons/Rubber%20bulb%205.jpg) |  |
> | [rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)<br/>![rubber stopper/rubber bung/rubber cork](../../archives/Wikimedia%20Commons/Rubber%20stopper%20holes.jpg) |  |
> | [safety spectacles/safety glasses/goggles](goggles.md)<br/>![safety spectacles/safety glasses/goggles](../../archives/Wikimedia%20Commons/Safety%20Goggles.jpg) |  |
> | [spatula](spatula.md)<br/>![spatula](../../archives/Wikimedia%20Commons/Laboratory%20Spatula.JPG) |  |
> | [stand/retort stand/ring stand/support stand](retort%20stand.md)<br/>![stand/retort stand/ring stand/support stand](../../archives/Wikimedia%20Commons/Retort%20stand.jpg) |  |
> | [test tube](test%20tube.md), boiling tube<br/>![test tube, boiling tube](../../archives/Wikimedia%20Commons/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg) | boiling tube: scaled-up to avoid [bumping](bumping%20(chemistry).md) |
> | [test tube brush](test%20tube%20brush.md)<br/>![test tube brush](../../archives/Wikimedia%20Commons/Test%20tube%20brushes.jpg) |  |
> | [test tube holder](test%20tube%20holder.md)<br/>![test tube holder](../../archives/Wikimedia%20Commons/Test%20Tube%20Holder2%202015.JPG) |  |
> | [test tube rack](test%20tube%20rack.md)<br/>![test tube rack](../../archives/Wikimedia%20Commons/Metal%20tube%20rack-laboratory%202.jpg) |  |
> | [thermometer](thermometer.md)<br/>![thermometer](../../archives/Wikimedia%20Commons/Mercury%20Thermometer.jpg) |  |
> | [tripod](tripod.md)<br/>![tripod](../../archives/Wikimedia%20Commons/Laboratory%20tripod.jpg) |  |
> | [volumetric flask](volumetric%20flask.md)<br/>![volumetric flask](../../archives/Wikimedia%20Commons/10mL%20Messkolben%20mit%20Schliff%20A.jpg) | Rinse the equipment with deionized [water](water.md) before use. |
> | [volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)<br/>![volumetric pipette/bulb pipette/belly pipette](../../archives/Wikimedia%20Commons/Vollpipetten.jpg) | Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered. |
> | [wash bottle](wash%20bottle.md)<br/>![wash bottle](../../archives/Wikimedia%20Commons/Lab%20wash-bottles%20water%20EtOH.jpg) |  |
> | [watch glass](watch%20glass.md)<br/>![watch glass](../../archives/Wikimedia%20Commons/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg) |  |
> | [weighing bottle](weighing%20bottle.md)<br/>![weighing bottle](../../archives/Wikimedia%20Commons/Weighing%20bottles.jpg) |  |
> | [wire gauze](wire%20gauze.md)<br/>![wire gauze](../../archives/Wikimedia%20Commons/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg) |  |

<!--/pytextgen-->

<!--pytextgen generate section="b81237"--><!-- The following content is generated at 2024-01-04T20:17:52.174780+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[Bunsen burner](Bunsen%20burner.md) <!--SR:!2028-03-07,1151,310!2027-10-17,1291,350-->
- [Bunsen burner](Bunsen%20burner.md)→::@::←[Liebig condenser](Liebig%20condenser.md) <!--SR:!2026-11-25,959,330!2027-12-18,1340,350-->
- [Liebig condenser](Liebig%20condenser.md)→::@::←[beaker](beaker.md) <!--SR:!2032-06-08,2553,330!2028-01-26,1368,350-->
- [beaker](beaker.md)→::@::←[burette](burette.md) <!--SR:!2026-01-24,421,230!2026-11-03,942,330-->
- [burette](burette.md)→::@::←[burette clamp](burette%20clamp.md) <!--SR:!2025-11-30,444,310!2027-05-07,1162,350-->
- [burette clamp](burette%20clamp.md)→::@::←[clamp](clamp.md) <!--SR:!2026-01-15,470,310!2026-03-27,501,310-->
- [clamp](clamp.md)→::@::←[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md) <!--SR:!2026-02-06,623,250!2026-08-15,412,210-->
- [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)→::@::←[crucible](crucible.md) <!--SR:!2026-03-24,348,150!2026-08-16,782,270-->
- [crucible](crucible.md)→::@::←[crucible tongs](crucible%20tongs.md) <!--SR:!2026-09-07,902,330!2027-08-07,1237,350-->
- [crucible tongs](crucible%20tongs.md)→::@::←[desiccator](desiccator.md) <!--SR:!2025-10-07,631,310!2026-06-29,517,190-->
- [desiccator](desiccator.md)→::@::←[(eye) dropper/Pasteur pipette](eye%20dropper.md) <!--SR:!2026-05-14,480,270!2026-12-20,580,270-->
- [(eye) dropper/Pasteur pipette](eye%20dropper.md)→::@::←dropping bottle <!--SR:!2031-02-14,1969,310!2026-11-04,940,330-->
- dropping bottle→::@::←[electronic balance](weighing%20scale.md) <!--SR:!2027-08-29,1055,290!2026-08-17,355,170-->
- [electronic balance](weighing%20scale.md)→::@::←[evaporating dish](evaporating%20dish.md) <!--SR:!2026-12-20,757,230!2026-08-25,636,270-->
- [evaporating dish](evaporating%20dish.md)→::@::←[filter funnel](filter%20funnel.md) <!--SR:!2029-03-01,1245,250!2026-08-23,787,270-->
- [filter funnel](filter%20funnel.md)→::@::←[flat-bottom(ed) flask](flat-bottom%20flask.md) <!--SR:!2025-11-16,257,190!2030-06-21,1801,310-->
- [flat-bottom(ed) flask](flat-bottom%20flask.md)→::@::←[gas jar/pneumatic trough](pneumatic%20trough.md) <!--SR:!2026-09-04,640,250!2026-05-02,286,170-->
- [gas jar/pneumatic trough](pneumatic%20trough.md)→::@::←[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md) <!--SR:!2027-11-03,837,210!2027-10-26,1106,290-->
- [glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)→::@::←[graduated pipette](graduated%20pipette.md) <!--SR:!2026-02-04,402,230!2027-02-01,570,170-->
- [graduated pipette](graduated%20pipette.md)→::@::←[heat-resistant mat/heatproof mat](heatproof%20mat.md) <!--SR:!2028-08-10,1179,250!2026-06-27,339,190-->
- [heat-resistant mat/heatproof mat](heatproof%20mat.md)→::@::←[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md) <!--SR:!2027-07-04,1046,290!2027-04-04,679,250-->
- [measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)→::@::←[mortar and pestle](mortar%20and%20pestle.md) <!--SR:!2025-11-25,193,170!2026-07-27,697,250-->
- [mortar and pestle](mortar%20and%20pestle.md)→::@::←[pipeclay triangle](pipeclay%20triangle.md) <!--SR:!2028-08-26,1158,250!2026-08-20,785,270-->
- [pipeclay triangle](pipeclay%20triangle.md)→::@::←[reagent bottle](reagent%20bottle.md) <!--SR:!2026-02-19,671,270!2025-11-12,177,150-->
- [reagent bottle](reagent%20bottle.md)→::@::←[round-bottom(ed) flask](round-bottom%20flask.md) <!--SR:!2028-03-09,1155,270!2026-04-14,423,250-->
- [round-bottom(ed) flask](round-bottom%20flask.md)→::@::←[rubber bulb](rubber%20bulb.md) <!--SR:!2026-07-09,473,190!2025-10-13,309,190-->
- [rubber bulb](rubber%20bulb.md)→::@::←[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md) <!--SR:!2031-06-03,2103,290!2027-07-08,1049,290-->
- [rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)→::@::←[safety spectacles/safety glasses/goggles](goggles.md) <!--SR:!2026-06-13,252,150!2028-04-30,1044,230-->
- [safety spectacles/safety glasses/goggles](goggles.md)→::@::←[spatula](spatula.md) <!--SR:!2026-06-23,750,270!2027-06-17,1037,290-->
- [spatula](spatula.md)→::@::←[stand/retort stand/ring stand/support stand](retort%20stand.md) <!--SR:!2026-01-20,583,230!2027-07-23,807,270-->
- [stand/retort stand/ring stand/support stand](retort%20stand.md)→::@::←[test tube](test%20tube.md), boiling tube <!--SR:!2026-06-20,358,190!2025-11-10,199,190-->
- [test tube](test%20tube.md), boiling tube→::@::←[test tube brush](test%20tube%20brush.md) <!--SR:!2028-07-27,1514,350!2028-08-13,1528,350-->
- [test tube brush](test%20tube%20brush.md)→::@::←[test tube holder](test%20tube%20holder.md) <!--SR:!2026-02-24,631,270!2025-11-25,442,310-->
- [test tube holder](test%20tube%20holder.md)→::@::←[test tube rack](test%20tube%20rack.md) <!--SR:!2027-06-05,1029,290!2029-09-27,1724,310-->
- [test tube rack](test%20tube%20rack.md)→::@::←[thermometer](thermometer.md) <!--SR:!2026-06-29,289,170!2027-12-30,864,230-->
- [thermometer](thermometer.md)→::@::←[tripod](tripod.md) <!--SR:!2029-01-10,1335,290!2027-06-03,1008,290-->
- [tripod](tripod.md)→::@::←[volumetric flask](volumetric%20flask.md) <!--SR:!2025-12-07,160,150!2029-08-06,1584,310-->
- [volumetric flask](volumetric%20flask.md)→::@::←[volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md) <!--SR:!2027-07-11,651,230!2028-11-11,1208,270-->
- [volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)→::@::←[wash bottle](wash%20bottle.md) <!--SR:!2027-07-31,1052,290!2027-11-28,1085,270-->
- [wash bottle](wash%20bottle.md)→::@::←[watch glass](watch%20glass.md) <!--SR:!2026-03-12,682,270!2027-10-13,956,270-->
- [watch glass](watch%20glass.md)→::@::←[weighing bottle](weighing%20bottle.md) <!--SR:!2025-10-23,638,310!2025-10-14,588,270-->
- [weighing bottle](weighing%20bottle.md)→::@::←[wire gauze](wire%20gauze.md) <!--SR:!2028-08-17,1304,290!2031-03-15,2174,330-->
- [wire gauze](wire%20gauze.md)→::@::←_(end)_ <!--SR:!2026-12-29,980,330!2026-09-08,897,330-->

<!--/pytextgen-->

### name–image

<!--pytextgen generate section="dd23"--><!-- The following content is generated at 2024-01-04T20:17:52.234332+08:00. Any edits will be overridden! -->

- [Bunsen burner](Bunsen%20burner.md):@:![Bunsen burner](../../archives/Wikimedia%20Commons/Bunsen%20burner.jpg) <!--SR:!2027-05-10,1164,350-->
- [Liebig condenser](Liebig%20condenser.md):@:![Liebig condenser](../../archives/Wikimedia%20Commons/LiebigCondenser.jpg) <!--SR:!2026-06-14,891,330-->
- [beaker](beaker.md):@:![beaker](../../archives/Wikimedia%20Commons/Glassware-%20Beaker.jpg) <!--SR:!2026-09-27,913,330-->
- [burette](burette.md):@:![burette](../../archives/Wikimedia%20Commons/Burette.svg) <!--SR:!2026-01-13,771,330-->
- [burette clamp](burette%20clamp.md):@:![burette clamp](../../archives/Wikimedia%20Commons/Burette%20with%20Clamp(3).jpg) <!--SR:!2028-05-25,1238,290-->
- [clamp](clamp.md):@:![clamp](../../archives/Wikimedia%20Commons/Utility%20clamp1.jpg) <!--SR:!2028-04-24,1441,350-->
- [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md):@:![conical flask/Erlenmeyer flask/titration flask](../../archives/Wikimedia%20Commons/250%20mL%20Erlenmeyer%20flask.jpg) <!--SR:!2027-01-21,1082,350-->
- [crucible](crucible.md):@:![crucible](../../archives/Wikimedia%20Commons/Czochralski%20method%20used%20crucible%201.jpg) <!--SR:!2027-01-10,1073,350-->
- [crucible tongs](crucible%20tongs.md):@:![crucible tongs](../../archives/Wikimedia%20Commons/Crucible%20tong.jpg) <!--SR:!2028-02-04,1376,350-->
- [desiccator](desiccator.md):@:![desiccator](../../archives/Wikimedia%20Commons/Desiccator.jpg) <!--SR:!2027-04-17,1146,350-->
- [(eye) dropper/Pasteur pipette](eye%20dropper.md):@:![(eye) dropper/Pasteur pipette](../../archives/Wikimedia%20Commons/Transfer%20pipette.jpg) <!--SR:!2027-08-01,1228,350-->
- dropping bottle:@:![dropping bottle](../../archives/Wikimedia%20Commons/Dropper%20with%20vial.jpg) <!--SR:!2028-07-11,1501,350-->
- [electronic balance](weighing%20scale.md):@:![electronic balance](../../archives/Wikimedia%20Commons/Weighing%20balance,%20MNIT.jpg) <!--SR:!2026-08-24,887,330-->
- [evaporating dish](evaporating%20dish.md):@:![evaporating dish](../../archives/Wikimedia%20Commons/Abdampfschalen%20verschiedene%20Groessen.jpg) <!--SR:!2027-12-14,1337,350-->
- [filter funnel](filter%20funnel.md):@:![filter funnel](../../archives/Wikimedia%20Commons/High-Speed%20Filter%20Funnel-2.jpg) <!--SR:!2028-05-15,1455,350-->
- [flat-bottom(ed) flask](flat-bottom%20flask.md):@:![flat-bottom(ed) flask](../../archives/Wikimedia%20Commons/TGI%20250.jpg) <!--SR:!2028-07-22,1510,350-->
- [gas jar/pneumatic trough](pneumatic%20trough.md):@:![gas jar/pneumatic trough](../../archives/Wikimedia%20Commons/Gas-Pak%20jar.jpg) <!--SR:!2029-05-02,1652,310-->
- [glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md):@:![glass stirring rod/glass rod/stir(ring) rod](../../archives/Wikimedia%20Commons/Stirring%20rod.jpg) <!--SR:!2028-04-29,1445,350-->
- [graduated pipette](graduated%20pipette.md):@:![graduated pipette](../../archives/Wikimedia%20Commons/Mohr%20and%20Sero.jpg) <!--SR:!2031-08-15,2282,330-->
- [heat-resistant mat/heatproof mat](heatproof%20mat.md):@:![heat-resistant mat/heatproof mat](../../archives/Wikimedia%20Commons/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg) <!--SR:!2027-06-15,1194,350-->
- [measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md):@:![measuring cylinder/graduated cylinder/mixing cylinder](../../archives/Wikimedia%20Commons/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg) <!--SR:!2027-05-21,1173,350-->
- [mortar and pestle](mortar%20and%20pestle.md):@:![mortar and pestle](../../archives/Wikimedia%20Commons/White-Mortar-and-Pestle.jpg) <!--SR:!2027-04-06,1137,350-->
- [pipeclay triangle](pipeclay%20triangle.md):@:![pipeclay triangle](../../archives/Wikimedia%20Commons/Pipeclay%20triangle.jpg) <!--SR:!2026-02-24,805,330-->
- [reagent bottle](reagent%20bottle.md):@:![reagent bottle](../../archives/Wikimedia%20Commons/Dark%20bottle%20with%20ground%20glass%20plug.jpg) <!--SR:!2027-06-03,1185,350-->
- [round-bottom(ed) flask](round-bottom%20flask.md):@:![round-bottom(ed) flask](../../archives/Wikimedia%20Commons/Verrerie-p1030896.jpg) <!--SR:!2027-10-01,1278,350-->
- [rubber bulb](rubber%20bulb.md):@:![rubber bulb](../../archives/Wikimedia%20Commons/Rubber%20bulb%205.jpg) <!--SR:!2026-11-21,1032,350-->
- [rubber stopper/rubber bung/rubber cork](rubber%20stopper.md):@:![rubber stopper/rubber bung/rubber cork](../../archives/Wikimedia%20Commons/Rubber%20stopper%20holes.jpg) <!--SR:!2027-08-22,1245,350-->
- [safety spectacles/safety glasses/goggles](goggles.md):@:![safety spectacles/safety glasses/goggles](../../archives/Wikimedia%20Commons/Safety%20Goggles.jpg) <!--SR:!2027-01-15,1077,350-->
- [spatula](spatula.md):@:![spatula](../../archives/Wikimedia%20Commons/Laboratory%20Spatula.JPG) <!--SR:!2027-01-05,1068,350-->
- [stand/retort stand/ring stand/support stand](retort%20stand.md):@:![stand/retort stand/ring stand/support stand](../../archives/Wikimedia%20Commons/Retort%20stand.jpg) <!--SR:!2027-12-04,1328,350-->
- [test tube](test%20tube.md), boiling tube:@:![test tube, boiling tube](../../archives/Wikimedia%20Commons/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg) <!--SR:!2026-03-06,814,330-->
- [test tube brush](test%20tube%20brush.md):@:![test tube brush](../../archives/Wikimedia%20Commons/Test%20tube%20brushes.jpg) <!--SR:!2027-05-04,1159,350-->
- [test tube holder](test%20tube%20holder.md):@:![test tube holder](../../archives/Wikimedia%20Commons/Test%20Tube%20Holder2%202015.JPG) <!--SR:!2027-09-25,1273,350-->
- [test tube rack](test%20tube%20rack.md):@:![test tube rack](../../archives/Wikimedia%20Commons/Metal%20tube%20rack-laboratory%202.jpg) <!--SR:!2027-10-12,1287,350-->
- [thermometer](thermometer.md):@:![thermometer](../../archives/Wikimedia%20Commons/Mercury%20Thermometer.jpg) <!--SR:!2027-05-19,1172,350-->
- [tripod](tripod.md):@:![tripod](../../archives/Wikimedia%20Commons/Laboratory%20tripod.jpg) <!--SR:!2028-01-02,1353,350-->
- [volumetric flask](volumetric%20flask.md):@:![volumetric flask](../../archives/Wikimedia%20Commons/10mL%20Messkolben%20mit%20Schliff%20A.jpg) <!--SR:!2028-08-21,1535,350-->
- [volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md):@:![volumetric pipette/bulb pipette/belly pipette](../../archives/Wikimedia%20Commons/Vollpipetten.jpg) <!--SR:!2027-05-02,1158,350-->
- [wash bottle](wash%20bottle.md):@:![wash bottle](../../archives/Wikimedia%20Commons/Lab%20wash-bottles%20water%20EtOH.jpg) <!--SR:!2027-12-23,1340,350-->
- [watch glass](watch%20glass.md):@:![watch glass](../../archives/Wikimedia%20Commons/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg) <!--SR:!2026-02-15,788,330-->
- [weighing bottle](weighing%20bottle.md):@:![weighing bottle](../../archives/Wikimedia%20Commons/Weighing%20bottles.jpg) <!--SR:!2026-06-06,883,330-->
- [wire gauze](wire%20gauze.md):@:![wire gauze](../../archives/Wikimedia%20Commons/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg) <!--SR:!2027-05-14,1168,350-->

<!--/pytextgen-->

<!--pytextgen generate section="f002"--><!-- The following content is generated at 2024-01-04T20:17:52.211338+08:00. Any edits will be overridden! -->

- ![Bunsen burner](../../archives/Wikimedia%20Commons/Bunsen%20burner.jpg):@:[Bunsen burner](Bunsen%20burner.md) <!--SR:!2028-05-09,1454,350-->
- ![Liebig condenser](../../archives/Wikimedia%20Commons/LiebigCondenser.jpg):@:[Liebig condenser](Liebig%20condenser.md) <!--SR:!2027-06-06,1187,350-->
- ![beaker](../../archives/Wikimedia%20Commons/Glassware-%20Beaker.jpg):@:[beaker](beaker.md) <!--SR:!2027-04-11,1141,350-->
- ![burette](../../archives/Wikimedia%20Commons/Burette.svg):@:[burette](burette.md) <!--SR:!2029-11-10,1840,330-->
- ![burette clamp](../../archives/Wikimedia%20Commons/Burette%20with%20Clamp(3).jpg):@:[burette clamp](burette%20clamp.md) <!--SR:!2027-02-20,1105,350-->
- ![clamp](../../archives/Wikimedia%20Commons/Utility%20clamp1.jpg):@:[clamp](clamp.md) <!--SR:!2027-05-15,1168,350-->
- ![conical flask/Erlenmeyer flask/titration flask](../../archives/Wikimedia%20Commons/250%20mL%20Erlenmeyer%20flask.jpg):@:[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md) <!--SR:!2032-03-06,2442,330-->
- ![crucible](../../archives/Wikimedia%20Commons/Czochralski%20method%20used%20crucible%201.jpg):@:[crucible](crucible.md) <!--SR:!2027-05-29,1091,330-->
- ![crucible tongs](../../archives/Wikimedia%20Commons/Crucible%20tong.jpg):@:[crucible tongs](crucible%20tongs.md) <!--SR:!2027-04-21,1149,350-->
- ![desiccator](../../archives/Wikimedia%20Commons/Desiccator.jpg):@:[desiccator](desiccator.md) <!--SR:!2026-08-01,930,330-->
- ![(eye) dropper/Pasteur pipette](../../archives/Wikimedia%20Commons/Transfer%20pipette.jpg):@:[(eye) dropper/Pasteur pipette](eye%20dropper.md) <!--SR:!2027-10-07,1282,350-->
- ![dropping bottle](../../archives/Wikimedia%20Commons/Dropper%20with%20vial.jpg):@:dropping bottle <!--SR:!2027-08-04,1230,350-->
- ![electronic balance](../../archives/Wikimedia%20Commons/Weighing%20balance,%20MNIT.jpg):@:[electronic balance](weighing%20scale.md) <!--SR:!2027-06-09,1189,350-->
- ![evaporating dish](../../archives/Wikimedia%20Commons/Abdampfschalen%20verschiedene%20Groessen.jpg):@:[evaporating dish](evaporating%20dish.md) <!--SR:!2027-05-28,1180,350-->
- ![filter funnel](../../archives/Wikimedia%20Commons/High-Speed%20Filter%20Funnel-2.jpg):@:[filter funnel](filter%20funnel.md) <!--SR:!2027-01-23,998,330-->
- ![flat-bottom(ed) flask](../../archives/Wikimedia%20Commons/TGI%20250.jpg):@:[flat-bottom(ed) flask](flat-bottom%20flask.md) <!--SR:!2026-04-12,794,330-->
- ![gas jar/pneumatic trough](../../archives/Wikimedia%20Commons/Gas-Pak%20jar.jpg):@:[gas jar/pneumatic trough](pneumatic%20trough.md) <!--SR:!2026-01-23,784,330-->
- ![glass stirring rod/glass rod/stir(ring) rod](../../archives/Wikimedia%20Commons/Stirring%20rod.jpg):@:[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md) <!--SR:!2031-06-30,2295,330-->
- ![graduated pipette](../../archives/Wikimedia%20Commons/Mohr%20and%20Sero.jpg):@:[graduated pipette](graduated%20pipette.md) <!--SR:!2029-03-22,1501,330-->
- ![heat-resistant mat/heatproof mat](../../archives/Wikimedia%20Commons/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg):@:[heat-resistant mat/heatproof mat](heatproof%20mat.md) <!--SR:!2025-12-08,737,330-->
- ![measuring cylinder/graduated cylinder/mixing cylinder](../../archives/Wikimedia%20Commons/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg):@:[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md) <!--SR:!2025-11-14,728,330-->
- ![mortar and pestle](../../archives/Wikimedia%20Commons/White-Mortar-and-Pestle.jpg):@:[mortar and pestle](mortar%20and%20pestle.md) <!--SR:!2027-06-22,1199,350-->
- ![pipeclay triangle](../../archives/Wikimedia%20Commons/Pipeclay%20triangle.jpg):@:[pipeclay triangle](pipeclay%20triangle.md) <!--SR:!2027-01-28,1002,330-->
- ![reagent bottle](../../archives/Wikimedia%20Commons/Dark%20bottle%20with%20ground%20glass%20plug.jpg):@:[reagent bottle](reagent%20bottle.md) <!--SR:!2027-02-13,1100,350-->
- ![round-bottom(ed) flask](../../archives/Wikimedia%20Commons/Verrerie-p1030896.jpg):@:[round-bottom(ed) flask](round-bottom%20flask.md) <!--SR:!2027-11-13,1313,350-->
- ![rubber bulb](../../archives/Wikimedia%20Commons/Rubber%20bulb%205.jpg):@:[rubber bulb](rubber%20bulb.md) <!--SR:!2026-02-08,797,330-->
- ![rubber stopper/rubber bung/rubber cork](../../archives/Wikimedia%20Commons/Rubber%20stopper%20holes.jpg):@:[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md) <!--SR:!2027-02-03,1091,350-->
- ![safety spectacles/safety glasses/goggles](../../archives/Wikimedia%20Commons/Safety%20Goggles.jpg):@:[safety spectacles/safety glasses/goggles](goggles.md) <!--SR:!2027-08-11,1241,350-->
- ![spatula](../../archives/Wikimedia%20Commons/Laboratory%20Spatula.JPG):@:[spatula](spatula.md) <!--SR:!2028-08-01,1518,350-->
- ![stand/retort stand/ring stand/support stand](../../archives/Wikimedia%20Commons/Retort%20stand.jpg):@:[stand/retort stand/ring stand/support stand](retort%20stand.md) <!--SR:!2026-06-09,887,330-->
- ![test tube, boiling tube](../../archives/Wikimedia%20Commons/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg):@:[test tube](test%20tube.md), boiling tube <!--SR:!2028-08-07,1523,350-->
- ![test tube brush](../../archives/Wikimedia%20Commons/Test%20tube%20brushes.jpg):@:[test tube brush](test%20tube%20brush.md) <!--SR:!2027-03-12,1117,350-->
- ![test tube holder](../../archives/Wikimedia%20Commons/Test%20Tube%20Holder2%202015.JPG):@:[test tube holder](test%20tube%20holder.md) <!--SR:!2026-11-18,954,330-->
- ![test tube rack](../../archives/Wikimedia%20Commons/Metal%20tube%20rack-laboratory%202.jpg):@:[test tube rack](test%20tube%20rack.md) <!--SR:!2028-01-08,1353,350-->
- ![thermometer](../../archives/Wikimedia%20Commons/Mercury%20Thermometer.jpg):@:[thermometer](thermometer.md) <!--SR:!2028-02-20,1389,350-->
- ![tripod](../../archives/Wikimedia%20Commons/Laboratory%20tripod.jpg):@:[tripod](tripod.md) <!--SR:!2027-02-09,1096,350-->
- ![volumetric flask](../../archives/Wikimedia%20Commons/10mL%20Messkolben%20mit%20Schliff%20A.jpg):@:[volumetric flask](volumetric%20flask.md) <!--SR:!2026-06-04,883,330-->
- ![volumetric pipette/bulb pipette/belly pipette](../../archives/Wikimedia%20Commons/Vollpipetten.jpg):@:[volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md) <!--SR:!2028-01-29,1192,290-->
- ![wash bottle](../../archives/Wikimedia%20Commons/Lab%20wash-bottles%20water%20EtOH.jpg):@:[wash bottle](wash%20bottle.md) <!--SR:!2027-04-27,1154,350-->
- ![watch glass](../../archives/Wikimedia%20Commons/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg):@:[watch glass](watch%20glass.md) <!--SR:!2026-11-16,952,330-->
- ![weighing bottle](../../archives/Wikimedia%20Commons/Weighing%20bottles.jpg):@:[weighing bottle](weighing%20bottle.md) <!--SR:!2027-09-04,1255,350-->
- ![wire gauze](../../archives/Wikimedia%20Commons/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg):@:[wire gauze](wire%20gauze.md) <!--SR:!2027-08-18,1241,350-->

<!--/pytextgen-->

### name–description

<!--pytextgen generate section="3934"--><!-- The following content is generated at 2024-01-04T20:17:52.258336+08:00. Any edits will be overridden! -->

- [burette](burette.md):@:Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered. <!--SR:!2029-06-09,1655,310-->
- [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md):@:Rinse the equipment with deionized [water](water.md) before use. <!--SR:!2026-12-31,981,330-->
- dropping bottle:@:literally bottle with dropper <!--SR:!2027-06-30,1162,330-->
- [graduated pipette](graduated%20pipette.md):@:Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered. <!--SR:!2027-08-06,955,250-->
- [test tube](test%20tube.md), boiling tube:@:boiling tube: scaled-up to avoid [bumping](bumping%20(chemistry).md) <!--SR:!2027-12-10,1334,350-->
- [volumetric flask](volumetric%20flask.md):@:Rinse the equipment with deionized [water](water.md) before use. <!--SR:!2030-07-07,2021,330-->
- [volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md):@:Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered. <!--SR:!2028-11-16,1430,310-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/laboratory_equipment) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
