---
aliases:
  - group
  - groups
---

#academic/chemistry #academic/physics #flashcards/academic/Gg/group__periodic_table_

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# group

A __group__ is {{a column of [chemical elements](chemical%20element.md) in the [periodic table](periodic%20table.md)}}. The elements have {{similar [chemical](chemical%20property.md) or [physical](physical%20property.md) characteristics in their outermost [electron shells](electron%20shell.md)}}. <!--SR:!2023-06-11,54,310!2023-05-19,35,270-->

## list

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from itertools import chain
e = __env__
return await memorize_table(
	e.cwf_sects('8462', '92de'),
	('name (IUPAC/old IUPAC/old CAS)', 'IUPAC recommended trivial name',),
	(
		('[group 1](#^group-1)/IA/IA', '[hydrogen](hydrogen.md) and [alkali metals](alkali%20metal.md)', '^group-1',),
		('[group 2](alkaline%20earth%20metal.md)/IIA/IIA', '[alkaline earth metals](alkaline%20earth%20metal.md)', None,),
		('[group 17](halogen.md)/VIIB/VIIA', '[halogens](halogen.md)', None,),
		('[group 18](noble%20gas.md)/0/VIIIA', '[noble gases](noble%20gas.md)', None,),
	),
	lambda datum: chain(map(cloze, datum[:-2]), (f'{cloze(datum[-2])}{f" {datum[-1]}" if datum[-1] else ""}',),),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="8462"--><!-- The following content is generated at 2023-03-20T16:20:30.859423+08:00. Any edits will be overridden! -->

> | name (IUPAC/old IUPAC/old CAS) | IUPAC recommended trivial name |
> |-|-|
> | {{[group 1](#^group-1)/IA/IA}} | {{[hydrogen](hydrogen.md) and [alkali metals](alkali%20metal.md)}} ^group-1 |
> | {{[group 2](alkaline%20earth%20metal.md)/IIA/IIA}} | {{[alkaline earth metals](alkaline%20earth%20metal.md)}} |
> | {{[group 17](halogen.md)/VIIB/VIIA}} | {{[halogens](halogen.md)}} |
> | {{[group 18](noble%20gas.md)/0/VIIIA}} | {{[noble gases](noble%20gas.md)}} | <!--SR:!2023-06-23,64,310!2023-06-21,62,310!2023-06-22,63,310!2023-06-20,61,310!2023-06-12,55,310!2023-06-24,64,310!2023-06-29,68,310!2023-06-14,56,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="92de"--><!-- The following content is generated at 2023-03-20T10:25:32.449331+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[group 1](#^group-1)/IA/IA <!--SR:!2023-06-30,69,310!2023-07-03,72,310-->
2. [group 1](#^group-1)/IA/IA→:::←[group 2](alkaline%20earth%20metal.md)/IIA/IIA <!--SR:!2023-06-10,53,310!2023-06-25,65,310-->
3. [group 2](alkaline%20earth%20metal.md)/IIA/IIA→:::←[group 17](halogen.md)/VIIB/VIIA <!--SR:!2023-05-20,33,270!2023-06-18,60,310-->
4. [group 17](halogen.md)/VIIB/VIIA→:::←[group 18](noble%20gas.md)/0/VIIIA <!--SR:!2023-06-17,59,310!2023-06-27,67,310-->
5. [group 18](noble%20gas.md)/0/VIIIA→:::←_(end)_ <!--SR:!2023-07-04,73,310!2023-06-26,66,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
