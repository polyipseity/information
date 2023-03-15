#academic/biology #academic/chemistry #academic/physics #flashcards/academic/laboratory_equipment

# laboratory equipment

## examples

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read
from pytextgen.config import CONFIG
from pytextgen.gen import Tag, TextCode
from pytextgen.util import Result
cl, cr = CONFIG.cloze_token
data = (
	('[Bunsen burner](Bunsen%20burner.md)', '![{}](../attachments/Bunsen%20burner.jpg)', '',),
	('[beaker](beaker.md)', '![{}](../attachments/Glassware-%20Beaker.jpg)', '',),
	('[burette clamp](burette%20clamp.md)', '![{}](../attachments/Burette%20with%20Clamp(3).jpg)', '',),
	('[clamp](clamp.md)', '![{}](../attachments/Utility%20clamp1.jpg)', '',),
	('[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)', '![{}](../attachments/250%20mL%20Erlenmeyer%20flask.jpg)', '',),
	('[crucible](crucible.md)', '![{}](../attachments/Czochralski%20method%20used%20crucible%201.jpg)', '',),
	('[crucible tongs](crucible%20tongs.md)', '![{}](../attachments/Crucible%20tong.jpg)', '',),
	('[desiccator](desiccator.md)', '![{}](../attachments/Desiccator.jpg)', '',),
	('[(eye) dropper/Pasteur pipette](eye%20dropper.md)', '![{}](../attachments/Transfer%20pipette.jpg)', '',),
	('dropping bottle', '![{}](../attachments/Dropper%20with%20vial.jpg)', 'literally bottle with dropper',),
	('[electronic balance](weighing%20scale.md)', '![{}](../attachments/Weighing%20balance,%20MNIT.jpg)', '',),
	('[evaporating dish](evaporating%20dish.md)', '![{}](../attachments/Abdampfschalen%20verschiedene%20Groessen.jpg)', '',),
	('[filter funnel](filter%20funnel.md)', '![{}](../attachments/High-Speed%20Filter%20Funnel-2.jpg)', '',),
	('[flat-bottom(ed) flask](flat-bottom%20flask.md)', '![{}](../attachments/TGI%20250.jpg)', '',),
	('[gas jar/pneumatic trough](pneumatic%20trough.md)', '![{}](../attachments/Gas-Pak%20jar.jpg)', '',),
	('[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)', '![{}](../attachments/Stirring%20rod.jpg)', '',),
	('[heat-resistant mat/heatproof mat](heatproof%20mat.md)', '![{}](../attachments/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg)', '',),
	('[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)', '![{}](../attachments/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg)', '',),
	('[mortar and pestle](mortar%20and%20pestle.md)', '![{}](../attachments/White-Mortar-and-Pestle.jpg)', '',),
	('[pipeclay triangle](pipeclay%20triangle.md)', '![{}](../attachments/Pipeclay%20triangle.jpg)', '',),
	('[reagent bottle](reagent%20bottle.md)', '![{}](../attachments/Dark%20bottle%20with%20ground%20glass%20plug.jpg)', '',),
	('[round-bottom(ed) flask](round-bottom%20flask.md)', '![{}](../attachments/Verrerie-p1030896.jpg)', '',),
	('[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)', '![{}](../attachments/Rubber%20stopper%20holes.jpg)', '',),
	('[safety spectacles/safety glasses/goggles](goggles.md)', '![{}](../attachments/Safety%20Goggles.jpg)', '',),
	('[spatula](spatula.md)', '![{}](../attachments/Laboratory%20Spatula.JPG)', '',),
	('[stand/retort stand/ring stand/support stand](retort%20stand.md)', '![{}](../attachments/Retort%20stand.jpg)', '',),
	('[test tube](test%20tube.md), boiling tube', '![{}](../attachments/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg)', 'boiling tube: scaled-up to avoid [bumping](bumping%20(chemistry).md)',),
	('[test tube brush](test%20tube%20brush.md)', '![{}](../attachments/Test%20tube%20brushes.jpg)', '',),
	('[test tube holder](test%20tube%20holder.md)', '![{}](../attachments/Test%20Tube%20Holder2%202015.JPG)', '',),
	('[test tube rack](test%20tube%20rack.md)', '![{}](../attachments/Metal%20tube%20rack-laboratory%202.jpg)', '',),
	('[thermometer](thermometer.md)', '![{}](../attachments/Mercury%20Thermometer.jpg)', '',),
	('[tripod](tripod.md)', '![{}](../attachments/Laboratory%20tripod.jpg)', '',),
	('[wash bottle](wash%20bottle.md)', '![{}](../attachments/Lab%20wash-bottles%20water%20EtOH.jpg)', '',),
	('[watch glass](watch%20glass.md)', '![{}](../attachments/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg)', '',),
	('[weighing bottle](weighing%20bottle.md)', '![{}](../attachments/Weighing%20bottles.jpg)', '',),
	('[wire gauze](wire%20gauze.md)', '![{}](../attachments/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg)', '',),
)
return (
	Result(
		location=__env__.cwf_section('fadd2e'),
		text=gen.cloze_text(
			TextCode.compile(gen.rows_to_table(
				data,
				names=('name & image', 'description',),
				values=lambda datum: (
					TextCode.escape(f'{cl}{datum[0]}{cr}<br/>{cl}{datum[1].format(datum[0],)}{cr}'),
					TextCode.escape(f'{cl}{datum[2]}{cr}' if datum[2] else ''),
				),
			)),
			states=await read.read_flashcard_states(__env__.cwf_section('fadd2e')),
		),
	),
	Result(
		location=__env__.cwf_section('b81237'),
		text=gen.memorize_linked_seq(
			gen.seq_to_code(
				map(lambda datum: TextCode.escape(datum[0]), data),
				prefix=f'{{{Tag.MEMORIZE}:_(start)_}}',
				suffix=f'{{{Tag.MEMORIZE}:_(end)_}}',
			),
			hinted=False,
			states=await read.read_flashcard_states(__env__.cwf_section('b81237')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="fadd2e"--><!-- The following content is generated at 2023-03-14T16:16:39.221670+08:00. Any edits will be overridden! -->

> name & image | description
> -|-
> {{[Bunsen burner](Bunsen%20burner.md)}}<br/>{{![[Bunsen burner](Bunsen%20burner.md)](../attachments/Bunsen%20burner.jpg)}} |
> {{[beaker](beaker.md)}}<br/>{{![[beaker](beaker.md)](../attachments/Glassware-%20Beaker.jpg)}} |
> {{[burette clamp](burette%20clamp.md)}}<br/>{{![[burette clamp](burette%20clamp.md)](../attachments/Burette%20with%20Clamp(3).jpg)}} |
> {{[clamp](clamp.md)}}<br/>{{![[clamp](clamp.md)](../attachments/Utility%20clamp1.jpg)}} |
> {{[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)}}<br/>{{![[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)](../attachments/250%20mL%20Erlenmeyer%20flask.jpg)}} |
> {{[crucible](crucible.md)}}<br/>{{![[crucible](crucible.md)](../attachments/Czochralski%20method%20used%20crucible%201.jpg)}} |
> {{[crucible tongs](crucible%20tongs.md)}}<br/>{{![[crucible tongs](crucible%20tongs.md)](../attachments/Crucible%20tong.jpg)}} |
> {{[desiccator](desiccator.md)}}<br/>{{![[desiccator](desiccator.md)](../attachments/Desiccator.jpg)}} |
> {{[(eye) dropper/Pasteur pipette](eye%20dropper.md)}}<br/>{{![[(eye) dropper/Pasteur pipette](eye%20dropper.md)](../attachments/Transfer%20pipette.jpg)}} |
> {{dropping bottle}}<br/>{{![dropping bottle](../attachments/Dropper%20with%20vial.jpg)}} | {{literally bottle with dropper}}
> {{[electronic balance](weighing%20scale.md)}}<br/>{{![[electronic balance](weighing%20scale.md)](../attachments/Weighing%20balance,%20MNIT.jpg)}} |
> {{[evaporating dish](evaporating%20dish.md)}}<br/>{{![[evaporating dish](evaporating%20dish.md)](../attachments/Abdampfschalen%20verschiedene%20Groessen.jpg)}} |
> {{[filter funnel](filter%20funnel.md)}}<br/>{{![[filter funnel](filter%20funnel.md)](../attachments/High-Speed%20Filter%20Funnel-2.jpg)}} |
> {{[flat-bottom(ed) flask](flat-bottom%20flask.md)}}<br/>{{![[flat-bottom(ed) flask](flat-bottom%20flask.md)](../attachments/TGI%20250.jpg)}} |
> {{[gas jar/pneumatic trough](pneumatic%20trough.md)}}<br/>{{![[gas jar/pneumatic trough](pneumatic%20trough.md)](../attachments/Gas-Pak%20jar.jpg)}} |
> {{[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)}}<br/>{{![[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)](../attachments/Stirring%20rod.jpg)}} |
> {{[heat-resistant mat/heatproof mat](heatproof%20mat.md)}}<br/>{{![[heat-resistant mat/heatproof mat](heatproof%20mat.md)](../attachments/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg)}} |
> {{[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)}}<br/>{{![[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)](../attachments/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg)}} |
> {{[mortar and pestle](mortar%20and%20pestle.md)}}<br/>{{![[mortar and pestle](mortar%20and%20pestle.md)](../attachments/White-Mortar-and-Pestle.jpg)}} |
> {{[pipeclay triangle](pipeclay%20triangle.md)}}<br/>{{![[pipeclay triangle](pipeclay%20triangle.md)](../attachments/Pipeclay%20triangle.jpg)}} |
> {{[reagent bottle](reagent%20bottle.md)}}<br/>{{![[reagent bottle](reagent%20bottle.md)](../attachments/Dark%20bottle%20with%20ground%20glass%20plug.jpg)}} |
> {{[round-bottom(ed) flask](round-bottom%20flask.md)}}<br/>{{![[round-bottom(ed) flask](round-bottom%20flask.md)](../attachments/Verrerie-p1030896.jpg)}} |
> {{[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)}}<br/>{{![[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)](../attachments/Rubber%20stopper%20holes.jpg)}} |
> {{[safety spectacles/safety glasses/goggles](goggles.md)}}<br/>{{![[safety spectacles/safety glasses/goggles](goggles.md)](../attachments/Safety%20Goggles.jpg)}} |
> {{[spatula](spatula.md)}}<br/>{{![[spatula](spatula.md)](../attachments/Laboratory%20Spatula.JPG)}} |
> {{[stand/retort stand/ring stand/support stand](retort%20stand.md)}}<br/>{{![[stand/retort stand/ring stand/support stand](retort%20stand.md)](../attachments/Retort%20stand.jpg)}} |
> {{[test tube](test%20tube.md), boiling tube}}<br/>{{![[test tube](test%20tube.md), boiling tube](../attachments/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg)}} | {{boiling tube: scaled-up to avoid [bumping](bumping%20(chemistry).md)}}
> {{[test tube brush](test%20tube%20brush.md)}}<br/>{{![[test tube brush](test%20tube%20brush.md)](../attachments/Test%20tube%20brushes.jpg)}} |
> {{[test tube holder](test%20tube%20holder.md)}}<br/>{{![[test tube holder](test%20tube%20holder.md)](../attachments/Test%20Tube%20Holder2%202015.JPG)}} |
> {{[test tube rack](test%20tube%20rack.md)}}<br/>{{![[test tube rack](test%20tube%20rack.md)](../attachments/Metal%20tube%20rack-laboratory%202.jpg)}} |
> {{[thermometer](thermometer.md)}}<br/>{{![[thermometer](thermometer.md)](../attachments/Mercury%20Thermometer.jpg)}} |
> {{[tripod](tripod.md)}}<br/>{{![[tripod](tripod.md)](../attachments/Laboratory%20tripod.jpg)}} |
> {{[wash bottle](wash%20bottle.md)}}<br/>{{![[wash bottle](wash%20bottle.md)](../attachments/Lab%20wash-bottles%20water%20EtOH.jpg)}} |
> {{[watch glass](watch%20glass.md)}}<br/>{{![[watch glass](watch%20glass.md)](../attachments/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg)}} |
> {{[weighing bottle](weighing%20bottle.md)}}<br/>{{![[weighing bottle](weighing%20bottle.md)](../attachments/Weighing%20bottles.jpg)}} |
> {{[wire gauze](wire%20gauze.md)}}<br/>{{![[wire gauze](wire%20gauze.md)](../attachments/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg)}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b81237"--><!-- The following content is generated at 2023-03-14T16:16:39.208323+08:00. Any edits will be overridden! -->

1. _(start)_→:::←[Bunsen burner](Bunsen%20burner.md)
2. [Bunsen burner](Bunsen%20burner.md)→:::←[beaker](beaker.md)
3. [beaker](beaker.md)→:::←[burette clamp](burette%20clamp.md)
4. [burette clamp](burette%20clamp.md)→:::←[clamp](clamp.md)
5. [clamp](clamp.md)→:::←[conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)
6. [conical flask/Erlenmeyer flask/titration flask](Erlenmeyer%20flask.md)→:::←[crucible](crucible.md)
7. [crucible](crucible.md)→:::←[crucible tongs](crucible%20tongs.md)
8. [crucible tongs](crucible%20tongs.md)→:::←[desiccator](desiccator.md)
9. [desiccator](desiccator.md)→:::←[(eye) dropper/Pasteur pipette](eye%20dropper.md)
10. [(eye) dropper/Pasteur pipette](eye%20dropper.md)→:::←dropping bottle
11. dropping bottle→:::←[electronic balance](weighing%20scale.md)
12. [electronic balance](weighing%20scale.md)→:::←[evaporating dish](evaporating%20dish.md)
13. [evaporating dish](evaporating%20dish.md)→:::←[filter funnel](filter%20funnel.md)
14. [filter funnel](filter%20funnel.md)→:::←[flat-bottom(ed) flask](flat-bottom%20flask.md)
15. [flat-bottom(ed) flask](flat-bottom%20flask.md)→:::←[gas jar/pneumatic trough](pneumatic%20trough.md)
16. [gas jar/pneumatic trough](pneumatic%20trough.md)→:::←[glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)
17. [glass stirring rod/glass rod/stir(ring) rod](glass%20rod.md)→:::←[heat-resistant mat/heatproof mat](heatproof%20mat.md)
18. [heat-resistant mat/heatproof mat](heatproof%20mat.md)→:::←[measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)
19. [measuring cylinder/graduated cylinder/mixing cylinder](graduated%20cylinder.md)→:::←[mortar and pestle](mortar%20and%20pestle.md)
20. [mortar and pestle](mortar%20and%20pestle.md)→:::←[pipeclay triangle](pipeclay%20triangle.md)
21. [pipeclay triangle](pipeclay%20triangle.md)→:::←[reagent bottle](reagent%20bottle.md)
22. [reagent bottle](reagent%20bottle.md)→:::←[round-bottom(ed) flask](round-bottom%20flask.md)
23. [round-bottom(ed) flask](round-bottom%20flask.md)→:::←[rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)
24. [rubber stopper/rubber bung/rubber cork](rubber%20stopper.md)→:::←[safety spectacles/safety glasses/goggles](goggles.md)
25. [safety spectacles/safety glasses/goggles](goggles.md)→:::←[spatula](spatula.md)
26. [spatula](spatula.md)→:::←[stand/retort stand/ring stand/support stand](retort%20stand.md)
27. [stand/retort stand/ring stand/support stand](retort%20stand.md)→:::←[test tube](test%20tube.md), boiling tube
28. [test tube](test%20tube.md), boiling tube→:::←[test tube brush](test%20tube%20brush.md)
29. [test tube brush](test%20tube%20brush.md)→:::←[test tube holder](test%20tube%20holder.md)
30. [test tube holder](test%20tube%20holder.md)→:::←[test tube rack](test%20tube%20rack.md)
31. [test tube rack](test%20tube%20rack.md)→:::←[thermometer](thermometer.md)
32. [thermometer](thermometer.md)→:::←[tripod](tripod.md)
33. [tripod](tripod.md)→:::←[wash bottle](wash%20bottle.md)
34. [wash bottle](wash%20bottle.md)→:::←[watch glass](watch%20glass.md)
35. [watch glass](watch%20glass.md)→:::←[weighing bottle](weighing%20bottle.md)
36. [weighing bottle](weighing%20bottle.md)→:::←[wire gauze](wire%20gauze.md)
37. [wire gauze](wire%20gauze.md)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
