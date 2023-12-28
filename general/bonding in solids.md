---
aliases:
  - bonding in solids
  - bondings in solids
tags:
  - flashcards/general/bonding_in_solids
  - languages/in/English
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

A __molecular solid__, also called __simple molecular structure__, {{consists of discrete [molecules](molecule.md) held together by [intermolecular force](intermolecular%20force.md)}}. If the molecules are [highly organized](crystal%20structure.md), {{it is also called a __molecular crystal__}}.

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
    ('[boiling point](boiling%20point.md)', 'typically low',),
    ('[brittleness](brittleness.md)', 'typically [anisotropic](anisotropy.md)',),
    ('[electrical conductivity](electrical%20conductivity.md)', 'typically low',),
    ('[melting point](melting%20point.md)', 'typically low',),
    ('[strength](strength%20of%20materials.md)', 'typically low',),
  ),
  lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9d9d"--><!-- The following content is generated at 2023-12-25T08:13:56.305002+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[boiling point](boiling%20point.md)}} | {{typically low}} |
> | {{[brittleness](brittleness.md)}} | {{typically [anisotropic](anisotropy.md)}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{typically low}} |
> | {{[melting point](melting%20point.md)}} | {{typically low}} |
> | {{[strength](strength%20of%20materials.md)}} | {{typically low}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### network covalent solid

A __network covalent solid__, also called __giant covalent structure__, {{consists of [atoms](atom.md) held together by a network of [covalent bonds](covalent%20bond.md)}}.

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
    ('[boiling point](boiling%20point.md)', 'typically high',),
    ('[brittleness](brittleness.md)', 'typically high',),
    ('[electrical conductivity](electrical%20conductivity.md)', 'typically low ([graphite](graphite.md): high)',),
    ('[melting point](melting%20point.md)', 'typically high',),
    ('[strength](strength%20of%20materials.md)', 'typically high ([graphite](graphite.md): low)',),
  ),
  lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="357d"--><!-- The following content is generated at 2023-12-25T08:00:46.096288+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[boiling point](boiling%20point.md)}} | {{typically high}} |
> | {{[brittleness](brittleness.md)}} | {{typically high}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{typically low ([graphite](graphite.md): high)}} |
> | {{[melting point](melting%20point.md)}} | {{typically high}} |
> | {{[strength](strength%20of%20materials.md)}} | {{typically high ([graphite](graphite.md): low)}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### ionic solid

A __ionic sold__, also called __giant ionic structure__, {{consists of [atoms](atom.md) held together by [ionic bonds](ionic%20bond.md)}}.

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
    ('[boiling point](boiling%20point.md)', 'typically moderately high',),
    ('[brittleness](brittleness.md)', 'typically extremely high',),
    ('[electrical conductivity](electrical%20conductivity.md)', 'typically high when [liquid](liquid.md) or [aqueous](aqueous%20solution.md), otherwise typically low',),
    ('[melting point](melting%20point.md)', 'typically moderately high',),
    ('[strength](strength%20of%20materials.md)', 'typically intermediate',),
  ),
  lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5460"--><!-- The following content is generated at 2023-12-25T08:13:56.331587+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[boiling point](boiling%20point.md)}} | {{typically moderately high}} |
> | {{[brittleness](brittleness.md)}} | {{typically extremely high}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{typically high when [liquid](liquid.md) or [aqueous](aqueous%20solution.md), otherwise typically low}} |
> | {{[melting point](melting%20point.md)}} | {{typically moderately high}} |
> | {{[strength](strength%20of%20materials.md)}} | {{typically intermediate}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### metallic solid

A __metallic solid__, also called __giant metallic structure__, {{consists of [metal](metal.md) [ions](ion.md) held together by [metallic bonds](metallic%20bond.md)}}.

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
    ('[boiling point](boiling%20point.md)', 'typically high ([mercury](mercury.md): low)',),
    ('[brittleness](brittleness.md)', 'typically low',),
    ('[ductility](ductility.md)', 'typically high',),
    ('[electrical conductivity](electrical%20conductivity.md)', 'typically high',),
    ('[malleability](malleability.md)', 'typically high',),
    ('[melting point](melting%20point.md)', 'typically high ([mercury](mercury.md): low)',),
    ('[strength](strength%20of%20materials.md)', 'typically low when pure',),
    ('[thermal conductivity](thermal%20conductivity.md)', 'typically high',),
  ),
  lambda datum: map(cloze, datum),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="435d"--><!-- The following content is generated at 2023-12-25T08:18:39.407540+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[boiling point](boiling%20point.md)}} | {{typically high ([mercury](mercury.md): low)}} |
> | {{[brittleness](brittleness.md)}} | {{typically low}} |
> | {{[ductility](ductility.md)}} | {{typically high}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{typically high}} |
> | {{[malleability](malleability.md)}} | {{typically high}} |
> | {{[melting point](melting%20point.md)}} | {{typically high ([mercury](mercury.md): low)}} |
> | {{[strength](strength%20of%20materials.md)}} | {{typically low when pure}} |
> | {{[thermal conductivity](thermal%20conductivity.md)}} | {{typically high}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/bonding_in_solids) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
