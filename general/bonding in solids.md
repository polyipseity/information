---
aliases:
  - bonding in solids
  - bondings in solids
tags:
  - flashcard/general/bonding_in_solids
  - language/in/English
---

# bonding in solids

%%

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

%%

## basic kinds

### molecular solid

A __molecular solid__, also called __simple molecular structure__, {{consists of discrete [molecules](molecule.md) held together by [intermolecular force](intermolecular%20force.md)}}. If the molecules are [highly organized](crystal%20structure.md), {{it is also called a __molecular crystal__}}. <!--SR:!2024-06-11,255,230!2026-10-08,926,330-->

#### properties of molecular solid

%%

```Python
# pytextgen generate data
from pytextgen.util import NULL_LOCATION
return await memorize_table(
  (__env__.cwf_sect('9d9d'), NULL_LOCATION,),
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

<!--pytextgen generate section="9d9d"--><!-- The following content is generated at 2023-12-25T08:13:56.305002+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[boiling point](boiling%20point.md)}} | {{typically low}} |
> | {{[brittleness](brittleness.md)}} | {{typically [anisotropic](anisotropy.md)}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{typically low}} |
> | {{[melting point](melting%20point.md)}} | {{typically low}} |
> | {{[strength](strength%20of%20materials.md)}} | {{typically low}} | <!--SR:!2024-12-08,410,290!2024-06-08,342,330!2027-04-03,1055,330!2024-10-17,159,310!2025-05-09,553,290!2027-09-02,1259,350!2025-01-16,368,373!2025-02-18,392,373!2024-09-12,183,341!2025-01-18,285,362-->

<!--/pytextgen-->

### network covalent solid

A __network covalent solid__, also called __giant covalent structure__, {{consists of [atoms](atom.md) held together by a network of [covalent bonds](covalent%20bond.md)}}. <!--SR:!2026-02-18,764,290-->

#### properties of network covalent solid

%%

```Python
# pytextgen generate data
from pytextgen.util import NULL_LOCATION
return await memorize_table(
  (__env__.cwf_sect('357d'), NULL_LOCATION,),
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

<!--pytextgen generate section="357d"--><!-- The following content is generated at 2023-12-25T08:00:46.096288+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[boiling point](boiling%20point.md)}} | {{typically high}} |
> | {{[brittleness](brittleness.md)}} | {{typically high}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{typically low ([graphite](graphite.md): high)}} |
> | {{[melting point](melting%20point.md)}} | {{typically high}} |
> | {{[strength](strength%20of%20materials.md)}} | {{typically high ([graphite](graphite.md): low)}} | <!--SR:!2025-08-20,569,270!2027-04-15,1150,350!2024-06-27,188,270!2025-08-03,600,310!2024-12-04,454,310!2026-12-31,986,330!2024-08-08,336,290!2025-01-29,441,250!2024-06-16,181,333!2024-06-01,169,333-->

<!--/pytextgen-->

### ionic solid

A __ionic sold__, also called __giant ionic structure__, {{consists of [atoms](atom.md) held together by [ionic bonds](ionic%20bond.md)}}. <!--SR:!2026-01-24,644,270-->

#### properties of ionic solid

%%

```Python
# pytextgen generate data
from pytextgen.util import NULL_LOCATION
return await memorize_table(
  (__env__.cwf_sect('5460'), NULL_LOCATION,),
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

<!--pytextgen generate section="5460"--><!-- The following content is generated at 2023-12-25T08:13:56.331587+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[boiling point](boiling%20point.md)}} | {{typically moderately high}} |
> | {{[brittleness](brittleness.md)}} | {{typically extremely high}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{typically high when [liquid](liquid.md) or [aqueous](aqueous%20solution.md), otherwise typically low}} |
> | {{[melting point](melting%20point.md)}} | {{typically moderately high}} |
> | {{[strength](strength%20of%20materials.md)}} | {{typically intermediate}} | <!--SR:!2025-10-08,593,270!2024-06-04,121,310!2026-02-09,801,330!2024-08-31,343,290!2024-10-18,378,290!2026-09-17,910,330!2024-12-27,392,250!2026-03-15,827,330!2024-09-16,265,353!2024-08-31,251,353-->

<!--/pytextgen-->

### metallic solid

A __metallic solid__, also called __giant metallic structure__, {{consists of [metal](metal.md) [ions](ion.md) held together by [metallic bonds](metallic%20bond.md)}}. <!--SR:!2024-11-02,422,290-->

#### properties of metallic solid

%%

```Python
# pytextgen generate data
from pytextgen.util import NULL_LOCATION
return await memorize_table(
  (__env__.cwf_sect('435d'), NULL_LOCATION,),
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

<!--pytextgen generate section="435d"--><!-- The following content is generated at 2023-12-25T08:18:39.407540+08:00. Any edits will be overridden! -->

> | property | description |
> |-|-|
> | {{[boiling point](boiling%20point.md)}} | {{typically high ([mercury](mercury.md): low)}} |
> | {{[brittleness](brittleness.md)}} | {{typically low}} |
> | {{[ductility](ductility.md)}} | {{typically high}} |
> | {{[electrical conductivity](electrical%20conductivity.md)}} | {{typically high}} |
> | {{[malleability](malleability.md)}} | {{typically high}} |
> | {{[melting point](melting%20point.md)}} | {{typically high ([mercury](mercury.md): low)}} |
> | {{[strength](strength%20of%20materials.md)}} | {{typically low when pure}} |
> | {{[thermal conductivity](thermal%20conductivity.md)}} | {{typically high}} | <!--SR:!2025-02-25,290,270!2027-05-01,1164,350!2025-01-07,288,290!2027-01-09,992,330!2024-08-17,94,210!2027-01-04,989,330!2025-02-25,362,310!2027-07-03,1214,350!2025-02-02,436,270!2024-06-07,341,330!2024-07-25,152,273!2025-02-24,397,373!2025-03-17,328,362!2025-01-12,246,322!2024-07-04,134,341!2025-05-21,401,382-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/bonding_in_solids) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
