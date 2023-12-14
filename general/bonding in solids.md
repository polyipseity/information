---
aliases:
  - bonding in solids
  - bondings in solids
tags:
  - flashcards/general/bonding_in_solids
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# bonding in solids

## basic kinds

### molecular solid

A __molecular solid__, also called __simple molecular structure__, {{consists of discrete [molecules](molecule.md) held together by [intermolecular force](intermolecular%20force.md)}}. If the molecules are [highly organized](crystal%20structure.md), {{it is also called a __molecular crystal__}}. <!--SR:!2024-06-11,255,230!2024-03-26,281,330-->

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
    ('[boiling point](boiling%20point.md)', 'low',),
    ('[electrical conductivity](electrical%20conductivity.md)', 'low',),
    ('[melting point](melting%20point.md)', 'low',),
    ('[strength](strength%20of%20materials.md)', 'low',),
  ),
  lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9d9d"--><!-- The following content is generated at 2023-10-07T07:46:37.390561+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[boiling point](boiling%20point.md)}} | {{low}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{low}} |
> | {{[melting point](melting%20point.md)}} | {{low}} |
> | {{[strength](strength%20of%20materials.md)}} | {{low}} | <!--SR:!2024-12-08,410,290!2024-06-08,342,330!2024-05-12,320,330!2024-05-11,319,330!2025-05-09,553,290!2024-03-22,277,330!2024-01-14,76,353!2024-01-23,81,353-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### network covalent solid

A __network covalent solid__, also called __giant covalent structure__, {{consists of [atoms](atom.md) held together by a network of [covalent bonds](covalent%20bond.md)}}. <!--SR:!2024-01-16,203,270-->

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
    ('[boiling point](boiling%20point.md)', 'high',),
    ('[brittleness](brittleness.md)', 'high',),
    ('[electrical conductivity](electrical%20conductivity.md)', 'low ([graphite](graphite.md): high)',),
    ('[melting point](melting%20point.md)', 'high',),
    ('[strength](strength%20of%20materials.md)', 'high ([graphite](graphite.md): low)',),
  ),
  lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="357d"--><!-- The following content is generated at 2023-10-07T07:46:37.415026+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[boiling point](boiling%20point.md)}} | {{high}} |
> | {{[brittleness](brittleness.md)}} | {{high}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{low ([graphite](graphite.md): high)}} |
> | {{[melting point](melting%20point.md)}} | {{high}} |
> | {{[strength](strength%20of%20materials.md)}} | {{high ([graphite](graphite.md): low)}} | <!--SR:!2024-01-29,211,270!2024-02-20,253,330!2023-12-22,70,270!2025-08-03,600,310!2024-12-04,454,310!2024-04-19,299,330!2024-08-08,336,290!2025-01-29,441,250!2023-12-18,54,333!2023-12-15,51,333-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### ionic solid

A __ionic sold__, also called __giant ionic structure__, {{consists of [atoms](atom.md) held together by [ionic bonds](ionic%20bond.md)}}. <!--SR:!2024-04-20,239,270-->

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
    ('[boiling point](boiling%20point.md)', 'high',),
    ('[brittleness](brittleness.md)', 'high',),
    ('[electrical conductivity](electrical%20conductivity.md)', 'high when [liquid](liquid.md) or [aqueous](aqueous%20solution.md), otherwise low',),
    ('[melting point](melting%20point.md)', 'high',),
    ('[strength](strength%20of%20materials.md)', 'high',),
  ),
  lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5460"--><!-- The following content is generated at 2023-10-07T07:46:37.443929+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[boiling point](boiling%20point.md)}} | {{high}} |
> | {{[brittleness](brittleness.md)}} | {{high}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{high when [liquid](liquid.md) or [aqueous](aqueous%20solution.md), otherwise low}} |
> | {{[melting point](melting%20point.md)}} | {{high}} |
> | {{[strength](strength%20of%20materials.md)}} | {{high}} | <!--SR:!2024-02-23,220,270!2024-02-04,243,330!2026-02-09,801,330!2024-08-31,343,290!2024-10-18,378,290!2024-03-21,276,330!2024-12-27,392,250!2026-03-15,827,330!2023-12-26,58,333!2023-12-23,55,333-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### metallic solid

A __metallic solid__, also called __giant metallic structure__, {{consists of [metal](metal.md) [ions](ion.md) held together by [metallic bonds](metallic%20bond.md)}}. <!--SR:!2024-11-02,422,290-->

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
    ('[boiling point](boiling%20point.md)', 'high',),
    ('[ductility](ductility.md)', 'high',),
    ('[electrical conductivity](electrical%20conductivity.md)', 'high',),
    ('[malleability](malleability.md)', 'high',),
    ('[melting point](melting%20point.md)', 'high',),
    ('[thermal conductivity](thermal%20conductivity.md)', 'high',),
  ),
  lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="435d"--><!-- The following content is generated at 2023-10-07T07:46:37.464150+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[boiling point](boiling%20point.md)}} | {{high}} |
> | {{[ductility](ductility.md)}} | {{high}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{high}} |
> | {{[malleability](malleability.md)}} | {{high}} |
> | {{[melting point](melting%20point.md)}} | {{high}} |
> | {{[thermal conductivity](thermal%20conductivity.md)}} | {{high}} | <!--SR:!2024-01-24,218,290!2024-02-22,256,330!2023-12-17,199,310!2024-04-21,301,330!2024-01-14,31,250!2024-04-20,300,330!2024-02-29,90,290!2024-03-06,267,330!2025-02-02,436,270!2024-06-07,341,330!2023-12-15,11,253!2024-01-24,82,353-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
