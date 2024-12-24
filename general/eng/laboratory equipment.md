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

- _(begin)_→::@::←[Bunsen burner](Bunsen%20burner.md)
- [Bunsen burner](Bunsen%20burner.md)→::@::←[Liebig condenser](Liebig%20condenser.md)
- [Liebig condenser](Liebig%20condenser.md)→::@::←[beaker](beaker.md)
- [beaker](beaker.md)→::@::←[burette](burette.md)
- [burette](burette.md)→::@::←[burette clamp](burette%20clamp.md)
- [burette clamp](burette%20clamp.md)→::@::←[clamp](clamp.md)
- [clamp](clamp.md)→::@::←[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)
- [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)→::@::←[crucible](crucible.md)
- [crucible](crucible.md)→::@::←[crucible tongs](crucible%20tongs.md)
- [crucible tongs](crucible%20tongs.md)→::@::←[desiccator](desiccator.md)
- [desiccator](desiccator.md)→::@::←[(eye) dropper/Pasteur pipette](eye%20dropper.md)
- [(eye) dropper/Pasteur pipette](eye%20dropper.md)→::@::←dropping bottle
- dropping bottle→::@::←[electronic balance](weighing%20scale.md)
- [electronic balance](weighing%20scale.md)→::@::←[evaporating dish](evaporating%20dish.md)
- [evaporating dish](evaporating%20dish.md)→::@::←[filter funnel](filter%20funnel.md)
- [filter funnel](filter%20funnel.md)→::@::←[flat-bottom(ed) flask](flat-bottom%20flask.md)
- [flat-bottom(ed) flask](flat-bottom%20flask.md)→::@::←[gas jar/pneumatic trough](pneumatic%20trough.md)
- [gas jar/pneumatic trough](pneumatic%20trough.md)→::@::←[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)
- [glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)→::@::←[graduated pipette](graduated%20pipette.md)
- [graduated pipette](graduated%20pipette.md)→::@::←[heat-resistant mat/heatproof mat](heatproof%20mat.md)
- [heat-resistant mat/heatproof mat](heatproof%20mat.md)→::@::←[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)
- [measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)→::@::←[mortar and pestle](mortar%20and%20pestle.md)
- [mortar and pestle](mortar%20and%20pestle.md)→::@::←[pipeclay triangle](pipeclay%20triangle.md)
- [pipeclay triangle](pipeclay%20triangle.md)→::@::←[reagent bottle](reagent%20bottle.md)
- [reagent bottle](reagent%20bottle.md)→::@::←[round-bottom(ed) flask](round-bottom%20flask.md)
- [round-bottom(ed) flask](round-bottom%20flask.md)→::@::←[rubber bulb](rubber%20bulb.md)
- [rubber bulb](rubber%20bulb.md)→::@::←[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)
- [rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)→::@::←[safety spectacles/safety glasses/goggles](goggles.md)
- [safety spectacles/safety glasses/goggles](goggles.md)→::@::←[spatula](spatula.md)
- [spatula](spatula.md)→::@::←[stand/retort stand/ring stand/support stand](retort%20stand.md)
- [stand/retort stand/ring stand/support stand](retort%20stand.md)→::@::←[test tube](test%20tube.md), boiling tube
- [test tube](test%20tube.md), boiling tube→::@::←[test tube brush](test%20tube%20brush.md)
- [test tube brush](test%20tube%20brush.md)→::@::←[test tube holder](test%20tube%20holder.md)
- [test tube holder](test%20tube%20holder.md)→::@::←[test tube rack](test%20tube%20rack.md)
- [test tube rack](test%20tube%20rack.md)→::@::←[thermometer](thermometer.md)
- [thermometer](thermometer.md)→::@::←[tripod](tripod.md)
- [tripod](tripod.md)→::@::←[volumetric flask](volumetric%20flask.md)
- [volumetric flask](volumetric%20flask.md)→::@::←[volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)
- [volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)→::@::←[wash bottle](wash%20bottle.md)
- [wash bottle](wash%20bottle.md)→::@::←[watch glass](watch%20glass.md)
- [watch glass](watch%20glass.md)→::@::←[weighing bottle](weighing%20bottle.md)
- [weighing bottle](weighing%20bottle.md)→::@::←[wire gauze](wire%20gauze.md)
- [wire gauze](wire%20gauze.md)→::@::←_(end)_

<!--/pytextgen-->

### name–image

<!--pytextgen generate section="dd23"--><!-- The following content is generated at 2024-01-04T20:17:52.234332+08:00. Any edits will be overridden! -->

- [Bunsen burner](Bunsen%20burner.md):@:![Bunsen burner](../../archives/Wikimedia%20Commons/Bunsen%20burner.jpg)
- [Liebig condenser](Liebig%20condenser.md):@:![Liebig condenser](../../archives/Wikimedia%20Commons/LiebigCondenser.jpg)
- [beaker](beaker.md):@:![beaker](../../archives/Wikimedia%20Commons/Glassware-%20Beaker.jpg)
- [burette](burette.md):@:![burette](../../archives/Wikimedia%20Commons/Burette.svg)
- [burette clamp](burette%20clamp.md):@:![burette clamp](../../archives/Wikimedia%20Commons/Burette%20with%20Clamp(3).jpg)
- [clamp](clamp.md):@:![clamp](../../archives/Wikimedia%20Commons/Utility%20clamp1.jpg)
- [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md):@:![conical flask/Erlenmeyer flask/titration flask](../../archives/Wikimedia%20Commons/250%20mL%20Erlenmeyer%20flask.jpg)
- [crucible](crucible.md):@:![crucible](../../archives/Wikimedia%20Commons/Czochralski%20method%20used%20crucible%201.jpg)
- [crucible tongs](crucible%20tongs.md):@:![crucible tongs](../../archives/Wikimedia%20Commons/Crucible%20tong.jpg)
- [desiccator](desiccator.md):@:![desiccator](../../archives/Wikimedia%20Commons/Desiccator.jpg)
- [(eye) dropper/Pasteur pipette](eye%20dropper.md):@:![(eye) dropper/Pasteur pipette](../../archives/Wikimedia%20Commons/Transfer%20pipette.jpg)
- dropping bottle:@:![dropping bottle](../../archives/Wikimedia%20Commons/Dropper%20with%20vial.jpg)
- [electronic balance](weighing%20scale.md):@:![electronic balance](../../archives/Wikimedia%20Commons/Weighing%20balance,%20MNIT.jpg)
- [evaporating dish](evaporating%20dish.md):@:![evaporating dish](../../archives/Wikimedia%20Commons/Abdampfschalen%20verschiedene%20Groessen.jpg)
- [filter funnel](filter%20funnel.md):@:![filter funnel](../../archives/Wikimedia%20Commons/High-Speed%20Filter%20Funnel-2.jpg)
- [flat-bottom(ed) flask](flat-bottom%20flask.md):@:![flat-bottom(ed) flask](../../archives/Wikimedia%20Commons/TGI%20250.jpg)
- [gas jar/pneumatic trough](pneumatic%20trough.md):@:![gas jar/pneumatic trough](../../archives/Wikimedia%20Commons/Gas-Pak%20jar.jpg)
- [glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md):@:![glass stirring rod/glass rod/stir(ring) rod](../../archives/Wikimedia%20Commons/Stirring%20rod.jpg)
- [graduated pipette](graduated%20pipette.md):@:![graduated pipette](../../archives/Wikimedia%20Commons/Mohr%20and%20Sero.jpg)
- [heat-resistant mat/heatproof mat](heatproof%20mat.md):@:![heat-resistant mat/heatproof mat](../../archives/Wikimedia%20Commons/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg)
- [measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md):@:![measuring cylinder/graduated cylinder/mixing cylinder](../../archives/Wikimedia%20Commons/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg)
- [mortar and pestle](mortar%20and%20pestle.md):@:![mortar and pestle](../../archives/Wikimedia%20Commons/White-Mortar-and-Pestle.jpg)
- [pipeclay triangle](pipeclay%20triangle.md):@:![pipeclay triangle](../../archives/Wikimedia%20Commons/Pipeclay%20triangle.jpg)
- [reagent bottle](reagent%20bottle.md):@:![reagent bottle](../../archives/Wikimedia%20Commons/Dark%20bottle%20with%20ground%20glass%20plug.jpg)
- [round-bottom(ed) flask](round-bottom%20flask.md):@:![round-bottom(ed) flask](../../archives/Wikimedia%20Commons/Verrerie-p1030896.jpg)
- [rubber bulb](rubber%20bulb.md):@:![rubber bulb](../../archives/Wikimedia%20Commons/Rubber%20bulb%205.jpg)
- [rubber stopper/rubber bung/rubber cork](rubber%20stopper.md):@:![rubber stopper/rubber bung/rubber cork](../../archives/Wikimedia%20Commons/Rubber%20stopper%20holes.jpg)
- [safety spectacles/safety glasses/goggles](goggles.md):@:![safety spectacles/safety glasses/goggles](../../archives/Wikimedia%20Commons/Safety%20Goggles.jpg)
- [spatula](spatula.md):@:![spatula](../../archives/Wikimedia%20Commons/Laboratory%20Spatula.JPG)
- [stand/retort stand/ring stand/support stand](retort%20stand.md):@:![stand/retort stand/ring stand/support stand](../../archives/Wikimedia%20Commons/Retort%20stand.jpg)
- [test tube](test%20tube.md), boiling tube:@:![test tube, boiling tube](../../archives/Wikimedia%20Commons/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg)
- [test tube brush](test%20tube%20brush.md):@:![test tube brush](../../archives/Wikimedia%20Commons/Test%20tube%20brushes.jpg)
- [test tube holder](test%20tube%20holder.md):@:![test tube holder](../../archives/Wikimedia%20Commons/Test%20Tube%20Holder2%202015.JPG)
- [test tube rack](test%20tube%20rack.md):@:![test tube rack](../../archives/Wikimedia%20Commons/Metal%20tube%20rack-laboratory%202.jpg)
- [thermometer](thermometer.md):@:![thermometer](../../archives/Wikimedia%20Commons/Mercury%20Thermometer.jpg)
- [tripod](tripod.md):@:![tripod](../../archives/Wikimedia%20Commons/Laboratory%20tripod.jpg)
- [volumetric flask](volumetric%20flask.md):@:![volumetric flask](../../archives/Wikimedia%20Commons/10mL%20Messkolben%20mit%20Schliff%20A.jpg)
- [volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md):@:![volumetric pipette/bulb pipette/belly pipette](../../archives/Wikimedia%20Commons/Vollpipetten.jpg)
- [wash bottle](wash%20bottle.md):@:![wash bottle](../../archives/Wikimedia%20Commons/Lab%20wash-bottles%20water%20EtOH.jpg)
- [watch glass](watch%20glass.md):@:![watch glass](../../archives/Wikimedia%20Commons/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg)
- [weighing bottle](weighing%20bottle.md):@:![weighing bottle](../../archives/Wikimedia%20Commons/Weighing%20bottles.jpg)
- [wire gauze](wire%20gauze.md):@:![wire gauze](../../archives/Wikimedia%20Commons/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg)

<!--/pytextgen-->

<!--pytextgen generate section="f002"--><!-- The following content is generated at 2024-01-04T20:17:52.211338+08:00. Any edits will be overridden! -->

- ![Bunsen burner](../../archives/Wikimedia%20Commons/Bunsen%20burner.jpg):@:[Bunsen burner](Bunsen%20burner.md)
- ![Liebig condenser](../../archives/Wikimedia%20Commons/LiebigCondenser.jpg):@:[Liebig condenser](Liebig%20condenser.md)
- ![beaker](../../archives/Wikimedia%20Commons/Glassware-%20Beaker.jpg):@:[beaker](beaker.md)
- ![burette](../../archives/Wikimedia%20Commons/Burette.svg):@:[burette](burette.md)
- ![burette clamp](../../archives/Wikimedia%20Commons/Burette%20with%20Clamp(3).jpg):@:[burette clamp](burette%20clamp.md)
- ![clamp](../../archives/Wikimedia%20Commons/Utility%20clamp1.jpg):@:[clamp](clamp.md)
- ![conical flask/Erlenmeyer flask/titration flask](../../archives/Wikimedia%20Commons/250%20mL%20Erlenmeyer%20flask.jpg):@:[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)
- ![crucible](../../archives/Wikimedia%20Commons/Czochralski%20method%20used%20crucible%201.jpg):@:[crucible](crucible.md)
- ![crucible tongs](../../archives/Wikimedia%20Commons/Crucible%20tong.jpg):@:[crucible tongs](crucible%20tongs.md)
- ![desiccator](../../archives/Wikimedia%20Commons/Desiccator.jpg):@:[desiccator](desiccator.md)
- ![(eye) dropper/Pasteur pipette](../../archives/Wikimedia%20Commons/Transfer%20pipette.jpg):@:[(eye) dropper/Pasteur pipette](eye%20dropper.md)
- ![dropping bottle](../../archives/Wikimedia%20Commons/Dropper%20with%20vial.jpg):@:dropping bottle
- ![electronic balance](../../archives/Wikimedia%20Commons/Weighing%20balance,%20MNIT.jpg):@:[electronic balance](weighing%20scale.md)
- ![evaporating dish](../../archives/Wikimedia%20Commons/Abdampfschalen%20verschiedene%20Groessen.jpg):@:[evaporating dish](evaporating%20dish.md)
- ![filter funnel](../../archives/Wikimedia%20Commons/High-Speed%20Filter%20Funnel-2.jpg):@:[filter funnel](filter%20funnel.md)
- ![flat-bottom(ed) flask](../../archives/Wikimedia%20Commons/TGI%20250.jpg):@:[flat-bottom(ed) flask](flat-bottom%20flask.md)
- ![gas jar/pneumatic trough](../../archives/Wikimedia%20Commons/Gas-Pak%20jar.jpg):@:[gas jar/pneumatic trough](pneumatic%20trough.md)
- ![glass stirring rod/glass rod/stir(ring) rod](../../archives/Wikimedia%20Commons/Stirring%20rod.jpg):@:[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)
- ![graduated pipette](../../archives/Wikimedia%20Commons/Mohr%20and%20Sero.jpg):@:[graduated pipette](graduated%20pipette.md)
- ![heat-resistant mat/heatproof mat](../../archives/Wikimedia%20Commons/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg):@:[heat-resistant mat/heatproof mat](heatproof%20mat.md)
- ![measuring cylinder/graduated cylinder/mixing cylinder](../../archives/Wikimedia%20Commons/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg):@:[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)
- ![mortar and pestle](../../archives/Wikimedia%20Commons/White-Mortar-and-Pestle.jpg):@:[mortar and pestle](mortar%20and%20pestle.md)
- ![pipeclay triangle](../../archives/Wikimedia%20Commons/Pipeclay%20triangle.jpg):@:[pipeclay triangle](pipeclay%20triangle.md)
- ![reagent bottle](../../archives/Wikimedia%20Commons/Dark%20bottle%20with%20ground%20glass%20plug.jpg):@:[reagent bottle](reagent%20bottle.md)
- ![round-bottom(ed) flask](../../archives/Wikimedia%20Commons/Verrerie-p1030896.jpg):@:[round-bottom(ed) flask](round-bottom%20flask.md)
- ![rubber bulb](../../archives/Wikimedia%20Commons/Rubber%20bulb%205.jpg):@:[rubber bulb](rubber%20bulb.md)
- ![rubber stopper/rubber bung/rubber cork](../../archives/Wikimedia%20Commons/Rubber%20stopper%20holes.jpg):@:[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)
- ![safety spectacles/safety glasses/goggles](../../archives/Wikimedia%20Commons/Safety%20Goggles.jpg):@:[safety spectacles/safety glasses/goggles](goggles.md)
- ![spatula](../../archives/Wikimedia%20Commons/Laboratory%20Spatula.JPG):@:[spatula](spatula.md)
- ![stand/retort stand/ring stand/support stand](../../archives/Wikimedia%20Commons/Retort%20stand.jpg):@:[stand/retort stand/ring stand/support stand](retort%20stand.md)
- ![test tube, boiling tube](../../archives/Wikimedia%20Commons/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg):@:[test tube](test%20tube.md), boiling tube
- ![test tube brush](../../archives/Wikimedia%20Commons/Test%20tube%20brushes.jpg):@:[test tube brush](test%20tube%20brush.md)
- ![test tube holder](../../archives/Wikimedia%20Commons/Test%20Tube%20Holder2%202015.JPG):@:[test tube holder](test%20tube%20holder.md)
- ![test tube rack](../../archives/Wikimedia%20Commons/Metal%20tube%20rack-laboratory%202.jpg):@:[test tube rack](test%20tube%20rack.md)
- ![thermometer](../../archives/Wikimedia%20Commons/Mercury%20Thermometer.jpg):@:[thermometer](thermometer.md)
- ![tripod](../../archives/Wikimedia%20Commons/Laboratory%20tripod.jpg):@:[tripod](tripod.md)
- ![volumetric flask](../../archives/Wikimedia%20Commons/10mL%20Messkolben%20mit%20Schliff%20A.jpg):@:[volumetric flask](volumetric%20flask.md)
- ![volumetric pipette/bulb pipette/belly pipette](../../archives/Wikimedia%20Commons/Vollpipetten.jpg):@:[volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md)
- ![wash bottle](../../archives/Wikimedia%20Commons/Lab%20wash-bottles%20water%20EtOH.jpg):@:[wash bottle](wash%20bottle.md)
- ![watch glass](../../archives/Wikimedia%20Commons/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg):@:[watch glass](watch%20glass.md)
- ![weighing bottle](../../archives/Wikimedia%20Commons/Weighing%20bottles.jpg):@:[weighing bottle](weighing%20bottle.md)
- ![wire gauze](../../archives/Wikimedia%20Commons/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg):@:[wire gauze](wire%20gauze.md)

<!--/pytextgen-->

### name–description

<!--pytextgen generate section="3934"--><!-- The following content is generated at 2024-01-04T20:17:52.258336+08:00. Any edits will be overridden! -->

- [burette](burette.md):@:Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered.
- [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md):@:Rinse the equipment with deionized [water](water.md) before use.
- dropping bottle:@:literally bottle with dropper
- [graduated pipette](graduated%20pipette.md):@:Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered.
- [test tube](test%20tube.md), boiling tube:@:boiling tube: scaled-up to avoid [bumping](bumping%20(chemistry).md)
- [volumetric flask](volumetric%20flask.md):@:Rinse the equipment with deionized [water](water.md) before use.
- [volumetric pipette/bulb pipette/belly pipette](volumetric%20pipette.md):@:Rinse the equipment with deionized [water](water.md) and then the [solution](solution.md) to be delivered.

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/laboratory_equipment) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
