---
aliases:
  - bonding in solids
  - bondings in solids
tags:
  - academic/chemistry
  - flashcards/academic/Bb/bonding_in_solids
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# bonding in solids

## basic kinds

### molecular solid

A __molecular solid__, also called __simple molecular structure__, {{consists of discrete [molecules](molecule.md) held together by [intermolecular force](intermolecular%20force.md)}}. If the molecules are [highly organized](crystal%20structure.md), {{it is also called a __molecular crystal__}}. <!--SR:!2023-06-12,44,230!2023-06-15,61,310-->

#### properties

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.util import NULL_LOCATION
e = __env__
return await memorize_table(
	(e.cwf_sect('9d9d'), NULL_LOCATION,),
	('property', 'description',),
	(
		('[electrical conductivity](electrical%20conductivity.md)', 'low',),
		('[melting point](melting%20point.md) and [boiling point](boiling%20point.md)', 'low',),
		('[strength](strength%20of%20materials.md)', 'low',),
	),
	lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9d9d"--><!-- The following content is generated at 2023-03-21T09:18:33.032052+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{low}} |
> | {{[melting point](melting%20point.md) and [boiling point](boiling%20point.md)}} | {{low}} |
> | {{[strength](strength%20of%20materials.md)}} | {{low}} | <!--SR:!2023-10-19,141,290!2023-06-29,73,310!2023-06-26,70,310!2023-06-27,71,310!2023-06-07,42,250!2023-06-16,62,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### network covalent solid

A __network covalent solid__, also called __giant covalent structure__, {{consists of [atoms](atom.md) held together by a network of [covalent bonds](covalent%20bond.md)}}. <!--SR:!2023-06-26,56,250-->

#### properties

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.util import NULL_LOCATION
e = __env__
return await memorize_table(
	(e.cwf_sect('357d'), NULL_LOCATION,),
	('property', 'description',),
	(
		('[brittleness](brittleness.md)', 'high',),
		('[electrical conductivity](electrical%20conductivity.md)', 'low ([graphite](graphite.md): high)',),
		('[melting point](melting%20point.md) and [boiling point](boiling%20point.md)', 'high',),
		('[strength](strength%20of%20materials.md)', 'high ([graphite](graphite.md): low)',),
	),
	lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="357d"--><!-- The following content is generated at 2023-03-21T09:21:26.394192+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[brittleness](brittleness.md)}} | {{high}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{low ([graphite](graphite.md): high)}} |
> | {{[melting point](melting%20point.md) and [boiling point](boiling%20point.md)}} | {{high}} |
> | {{[strength](strength%20of%20materials.md)}} | {{high ([graphite](graphite.md): low)}} | <!--SR:!2023-07-01,59,250!2023-06-12,59,310!2023-10-08,141,290!2023-12-10,194,310!2023-09-06,111,290!2023-06-23,67,310!2023-09-06,113,290!2023-06-28,55,230-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### ionic solid

A __ionic sold__, also called __giant ionic structure__, {{consists of [atoms](atom.md) held together by [ionic bonds](ionic%20bond.md)}}. <!--SR:!2023-06-15,23,250-->

#### properties

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.util import NULL_LOCATION
e = __env__
return await memorize_table(
	(e.cwf_sect('5460'), NULL_LOCATION,),
	('property', 'description',),
	(
		('[brittleness](brittleness.md)', 'high',),
		('[electrical conductivity](electrical%20conductivity.md)', 'high when [liquid](liquid.md) or [aqueous](aqueous%20solution.md), otherwise low',),
		('[melting point](melting%20point.md) and [boiling point](boiling%20point.md)', 'high',),
		('[strength](strength%20of%20materials.md)', 'high',),
	),
	lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5460"--><!-- The following content is generated at 2023-03-21T09:26:02.675571+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[brittleness](brittleness.md)}} | {{high}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{high when [liquid](liquid.md) or [aqueous](aqueous%20solution.md), otherwise low}} |
> | {{[melting point](melting%20point.md) and [boiling point](boiling%20point.md)}} | {{high}} |
> | {{[strength](strength%20of%20materials.md)}} | {{high}} | <!--SR:!2023-07-08,53,250!2024-02-04,243,330!2023-11-29,187,310!2023-09-23,118,290!2023-10-01,128,290!2023-06-17,63,310!2023-06-10,15,210!2023-12-09,193,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### metallic solid

A __metallic solid__, also called __giant metallic structure__, {{consists of [metal](metal.md) [ions](ion.md) held together by [metallic bonds](metallic%20bond.md)}}. <!--SR:!2023-09-05,110,270-->

#### properties

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.util import NULL_LOCATION
e = __env__
return await memorize_table(
	(e.cwf_sect('435d'), NULL_LOCATION,),
	('property', 'description',),
	(
		('[ductility](ductility.md)', 'high',),
		('[electrical conductivity](electrical%20conductivity.md)', 'high',),
		('[malleability](malleability.md)', 'high',),
		('[melting point](melting%20point.md) and [boiling point](boiling%20point.md)', 'high',),
		('[thermal conductivity](thermal%20conductivity.md)', 'high',),
	),
	lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="435d"--><!-- The following content is generated at 2023-03-21T09:18:33.074937+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[ductility](ductility.md)}} | {{high}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{high}} |
> | {{[malleability](malleability.md)}} | {{high}} |
> | {{[melting point](melting%20point.md) and [boiling point](boiling%20point.md)}} | {{high}} |
> | {{[thermal conductivity](thermal%20conductivity.md)}} | {{high}} | <!--SR:!2023-06-20,56,270!2023-06-09,56,310!2023-12-17,199,310!2023-06-24,68,310!2023-10-02,137,290!2023-06-25,69,310!2023-11-27,181,310!2023-06-13,60,310!2023-07-19,48,250!2023-06-28,72,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
