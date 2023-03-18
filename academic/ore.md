#academic/chemistry #academic/geology #academic/mineralogy #flashcards/academic/ore

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# ore

An __ore__ is {{a [rock](rock%20(geology).md) or [sediment](sediment.md) containing valuable [minerals](mineral.md) [concentrated](concentration.md) above background levels.}}

## extraction

See [extractive metallurgy](extractive%20metallurgy.md).

## important ores

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_table(
	(e.cwf_section('283749'), e.cwf_section('0398da')),
	('name', 'formula(s)', 'description',),
	(
		('[bauxite](bauxite.md)', 'Al(OH)<sub>3</sub>, AlOOH', 'Dried to Al<sub>3</sub>O<sub>3</sub> to produce [aluminium](aluminium.md).',),
		('[chalcopyrite](chalcopyrite.md), copper pyrite', 'CuFeS<sub>2</sub>', '',),
		('[galena](galena.md)', 'PbS', '',),
		('[hematite](hematite.md)', 'Fe<sub>2</sub>O<sub>3</sub>', '',),
	),
	lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="283749"--><!-- The following content is generated at 2023-03-17T10:53:05.633054+08:00. Any edits will be overridden! -->

> name | formula(s) | description
> -|-|-
> {{[bauxite](bauxite.md)}} | {{Al(OH)<sub>3</sub>, AlOOH}} | {{Dried to Al<sub>3</sub>O<sub>3</sub> to produce [aluminium](aluminium.md).}}
> {{[chalcopyrite](chalcopyrite.md), copper pyrite}} | {{CuFeS<sub>2</sub>}} |
> {{[galena](galena.md)}} | {{PbS}} |
> {{[hematite](hematite.md)}} | {{Fe<sub>2</sub>O<sub>3</sub>}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="0398da"--><!-- The following content is generated at 2023-03-17T10:53:05.644025+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[bauxite](bauxite.md)
2. [bauxite](bauxite.md)→:::←[chalcopyrite](chalcopyrite.md), copper pyrite
3. [chalcopyrite](chalcopyrite.md), copper pyrite→:::←[galena](galena.md)
4. [galena](galena.md)→:::←[hematite](hematite.md)
5. [hematite](hematite.md)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
