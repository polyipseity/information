#flashcards/academic/laboratory_glassware #academic/biology #academic/chemistry #academic/physics

# laboratory equipment

## examples

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read
from pytextgen.config import CONFIG
from pytextgen.gen import Tag, TextCode
from pytextgen.util import Result, Results
cl, cr = CONFIG.cloze_token
data = (
	('Bunsen burner', '![{}](../attachments/Bunsen%20burner.jpg)', '',),
	('beaker', '![{}](../attachments/Glassware-%20Beaker.jpg)', '',),
	('burette clamp', '![{}](../attachments/Burette%20with%20Clamp(3).jpg)', '',),
	('clamp', '![{}](../attachments/Utility%20clamp1.jpg)', '',),
	('conical flask/Erlenmeyer flask/titration flask', '![{}](../attachments/250%20mL%20Erlenmeyer%20flask.jpg)', '',),
	('crucible', '![{}](../attachments/Czochralski%20method%20used%20crucible%201.jpg)', '',),
	('crucible tongs', '![{}](../attachments/Crucible%20tong.jpg)', '',),
	('desiccator', '![{}](../attachments/Desiccator.jpg)', '',),
	('(eye) dropper/Pasteur pipette', '![{}](../attachments/Transfer%20pipette.jpg)', '',),
	('dropping bottle', '![{}](../attachments/Dropper%20with%20vial.jpg)', 'literally bottle with dropper',),
	('electronic balance', '![{}](../attachments/Weighing%20balance,%20MNIT.jpg)', '',),
	('evaporating dish', '![{}](../attachments/Abdampfschalen%20verschiedene%20Groessen.jpg)', '',),
	('filter funnel', '![{}](../attachments/High-Speed%20Filter%20Funnel-2.jpg)', '',),
	('flat-bottom(ed) flask', '![{}](../attachments/TGI%20250.jpg)', '',),
	('gas jar/pneumatic trough', '![{}](../attachments/Gas-Pak%20jar.jpg)', '',),
	('glass stirring rod/glass rod/stir(ring) rod', '![{}](../attachments/Stirring%20rod.jpg)', '',),
	('heat-resistant mat/heatproof mat', '![{}](../attachments/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg)', '',),
	('measuring cylinder/graduated cylinder/mixing cylinder', '![{}](../attachments/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg)', '',),
	('mortar and pestle', '![{}](../attachments/White-Mortar-and-Pestle.jpg)', '',),
	('pipeclay triangle', '![{}](../attachments/Pipeclay%20triangle.jpg)', '',),
	('reagent bottle', '![{}](../attachments/Dark%20bottle%20with%20ground%20glass%20plug.jpg)', '',),
	('round-bottom(ed) flask', '![{}](../attachments/Verrerie-p1030896.jpg)', '',),
	('rubber stopper/rubber bung/rubber cork', '![{}](../attachments/Rubber%20stopper%20holes.jpg)', '',),
	('safety spectacles/safety glasses/goggles', '![{}](../attachments/Safety%20Goggles.jpg)', '',),
	('spatula', '![{}](../attachments/Laboratory%20Spatula.JPG)', '',),
	('stand/retort stand/ring stand/support stand', '![{}](../attachments/Retort%20stand.jpg)', '',),
	('test tube, boiling tube', '![{}](../attachments/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg)', 'boiling tube: scaled-up to avoid [bumping](bumping%20(chemistry).md)',),
	('test tube brush', '![{}](../attachments/Test%20tube%20brushes.jpg)', '',),
	('test tube holder', '![{}](../attachments/Test%20Tube%20Holder2%202015.JPG)', '',),
	('test tube rack', '![{}](../attachments/Metal%20tube%20rack-laboratory%202.jpg)', '',),
	('thermometer', '![{}](../attachments/Mercury%20Thermometer.jpg)', '',),
	('tripod', '![{}](../attachments/Laboratory%20tripod.jpg)', '',),
	('wash bottle', '![{}](../attachments/Lab%20wash-bottles%20water%20EtOH.jpg)', '',),
	('watch glass', '![{}](../attachments/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg)', '',),
	('weighing bottle', '![{}](../attachments/Weighing%20bottles.jpg)', '',),
	('wire gauze', '![{}](../attachments/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg)', '',),
)
return Results(
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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="fadd2e"--><!-- The following content is generated at 2023-03-14T15:55:38.342389+08:00. Any edits will be overridden! -->

> name & image | description
> -|-
> {{Bunsen burner}}<br/>{{![Bunsen burner](../attachments/Bunsen%20burner.jpg)}} |
> {{beaker}}<br/>{{![beaker](../attachments/Glassware-%20Beaker.jpg)}} |
> {{burette clamp}}<br/>{{![burette clamp](../attachments/Burette%20with%20Clamp(3).jpg)}} |
> {{clamp}}<br/>{{![clamp](../attachments/Utility%20clamp1.jpg)}} |
> {{conical flask/Erlenmeyer flask/titration flask}}<br/>{{![conical flask/Erlenmeyer flask/titration flask](../attachments/250%20mL%20Erlenmeyer%20flask.jpg)}} |
> {{crucible}}<br/>{{![crucible](../attachments/Czochralski%20method%20used%20crucible%201.jpg)}} |
> {{crucible tongs}}<br/>{{![crucible tongs](../attachments/Crucible%20tong.jpg)}} |
> {{desiccator}}<br/>{{![desiccator](../attachments/Desiccator.jpg)}} |
> {{(eye) dropper/Pasteur pipette}}<br/>{{![(eye) dropper/Pasteur pipette](../attachments/Transfer%20pipette.jpg)}} |
> {{dropping bottle}}<br/>{{![dropping bottle](../attachments/Dropper%20with%20vial.jpg)}} | {{literally bottle with dropper}}
> {{electronic balance}}<br/>{{![electronic balance](../attachments/Weighing%20balance,%20MNIT.jpg)}} |
> {{evaporating dish}}<br/>{{![evaporating dish](../attachments/Abdampfschalen%20verschiedene%20Groessen.jpg)}} |
> {{filter funnel}}<br/>{{![filter funnel](../attachments/High-Speed%20Filter%20Funnel-2.jpg)}} |
> {{flat-bottom(ed) flask}}<br/>{{![flat-bottom(ed) flask](../attachments/TGI%20250.jpg)}} |
> {{gas jar/pneumatic trough}}<br/>{{![gas jar/pneumatic trough](../attachments/Gas-Pak%20jar.jpg)}} |
> {{glass stirring rod/glass rod/stir(ring) rod}}<br/>{{![glass stirring rod/glass rod/stir(ring) rod](../attachments/Stirring%20rod.jpg)}} |
> {{heat-resistant mat/heatproof mat}}<br/>{{![heat-resistant mat/heatproof mat](../attachments/A%20laboratory%20heat%20spreader%20made%20of%20asbestos,%20over%20Teclu%20burner.jpg)}} |
> {{measuring cylinder/graduated cylinder/mixing cylinder}}<br/>{{![measuring cylinder/graduated cylinder/mixing cylinder](../attachments/Different%20types%20of%20graduated%20cylinder-%2010ml,%2025ml,%2050ml%20and%20100%20ml%20graduated%20cylinder.jpg)}} |
> {{mortar and pestle}}<br/>{{![mortar and pestle](../attachments/White-Mortar-and-Pestle.jpg)}} |
> {{pipeclay triangle}}<br/>{{![pipeclay triangle](../attachments/Pipeclay%20triangle.jpg)}} |
> {{reagent bottle}}<br/>{{![reagent bottle](../attachments/Dark%20bottle%20with%20ground%20glass%20plug.jpg)}} |
> {{round-bottom(ed) flask}}<br/>{{![round-bottom(ed) flask](../attachments/Verrerie-p1030896.jpg)}} |
> {{rubber stopper/rubber bung/rubber cork}}<br/>{{![rubber stopper/rubber bung/rubber cork](../attachments/Rubber%20stopper%20holes.jpg)}} |
> {{safety spectacles/safety glasses/goggles}}<br/>{{![safety spectacles/safety glasses/goggles](../attachments/Safety%20Goggles.jpg)}} |
> {{spatula}}<br/>{{![spatula](../attachments/Laboratory%20Spatula.JPG)}} |
> {{stand/retort stand/ring stand/support stand}}<br/>{{![stand/retort stand/ring stand/support stand](../attachments/Retort%20stand.jpg)}} |
> {{test tube, boiling tube}}<br/>{{![test tube, boiling tube](../attachments/Two%20small%20test%20tubes%20held%20in%20spring%20clamps.jpg)}} | {{boiling tube: scaled-up to avoid [bumping](bumping%20(chemistry).md)}}
> {{test tube brush}}<br/>{{![test tube brush](../attachments/Test%20tube%20brushes.jpg)}} |
> {{test tube holder}}<br/>{{![test tube holder](../attachments/Test%20Tube%20Holder2%202015.JPG)}} |
> {{test tube rack}}<br/>{{![test tube rack](../attachments/Metal%20tube%20rack-laboratory%202.jpg)}} |
> {{thermometer}}<br/>{{![thermometer](../attachments/Mercury%20Thermometer.jpg)}} |
> {{tripod}}<br/>{{![tripod](../attachments/Laboratory%20tripod.jpg)}} |
> {{wash bottle}}<br/>{{![wash bottle](../attachments/Lab%20wash-bottles%20water%20EtOH.jpg)}} |
> {{watch glass}}<br/>{{![watch glass](../attachments/Laboratory%20Watch%20glasses%20of%20different%20sizes%202.jpg)}} |
> {{weighing bottle}}<br/>{{![weighing bottle](../attachments/Weighing%20bottles.jpg)}} |
> {{wire gauze}}<br/>{{![wire gauze](../attachments/12.5cm%20by%2012.5cm%20Wire%20Gauze.jpg)}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b81237"--><!-- The following content is generated at 2023-03-14T15:55:38.328849+08:00. Any edits will be overridden! -->

1. _(start)_→:::←Bunsen burner
2. Bunsen burner→:::←beaker
3. beaker→:::←burette clamp
4. burette clamp→:::←clamp
5. clamp→:::←conical flask/Erlenmeyer flask/titration flask
6. conical flask/Erlenmeyer flask/titration flask→:::←crucible
7. crucible→:::←crucible tongs
8. crucible tongs→:::←desiccator
9. desiccator→:::←(eye) dropper/Pasteur pipette
10. (eye) dropper/Pasteur pipette→:::←dropping bottle
11. dropping bottle→:::←electronic balance
12. electronic balance→:::←evaporating dish
13. evaporating dish→:::←filter funnel
14. filter funnel→:::←flat-bottom(ed) flask
15. flat-bottom(ed) flask→:::←gas jar/pneumatic trough
16. gas jar/pneumatic trough→:::←glass stirring rod/glass rod/stir(ring) rod
17. glass stirring rod/glass rod/stir(ring) rod→:::←heat-resistant mat/heatproof mat
18. heat-resistant mat/heatproof mat→:::←measuring cylinder/graduated cylinder/mixing cylinder
19. measuring cylinder/graduated cylinder/mixing cylinder→:::←mortar and pestle
20. mortar and pestle→:::←pipeclay triangle
21. pipeclay triangle→:::←reagent bottle
22. reagent bottle→:::←round-bottom(ed) flask
23. round-bottom(ed) flask→:::←rubber stopper/rubber bung/rubber cork
24. rubber stopper/rubber bung/rubber cork→:::←safety spectacles/safety glasses/goggles
25. safety spectacles/safety glasses/goggles→:::←spatula
26. spatula→:::←stand/retort stand/ring stand/support stand
27. stand/retort stand/ring stand/support stand→:::←test tube, boiling tube
28. test tube, boiling tube→:::←test tube brush
29. test tube brush→:::←test tube holder
30. test tube holder→:::←test tube rack
31. test tube rack→:::←thermometer
32. thermometer→:::←tripod
33. tripod→:::←wash bottle
34. wash bottle→:::←watch glass
35. watch glass→:::←weighing bottle
36. weighing bottle→:::←wire gauze
37. wire gauze→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
