---
aliases:
  - bonding in solids
  - bondings in solids
tags:
  - flashcard/active/general/eng/bonding_in_solids
  - language/in/English
---

# bonding in solids

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## basic kinds

### molecular solid

A __molecular solid__, also called __simple molecular structure__, {@{consists of discrete [molecules](molecule.md) held together by [intermolecular force](intermolecular%20force.md)}@}. If the molecules are [highly organized](crystal%20structure.md), {@{it is also called a __molecular crystal__}@}. <!--SR:!2026-09-17,828,250!2026-10-08,926,330-->

#### properties of molecular solid

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

<!--pytextgen generate section="9d9d"--><!-- The following content is generated at 2026-01-25T23:32:18.088336+08:00. Any edits will be overridden! -->

> | property                                                      | description                                  |
> | ------------------------------------------------------------- | -------------------------------------------- |
> | {@{[boiling point](boiling%20point.md)}@}                     | {@{typically low}@}                          |
> | {@{[brittleness](brittleness.md)}@}                           | {@{typically [anisotropic](anisotropy.md)}@} |
> | {@{[electrical conductivity](electrical%20conductivity.md)}@} | {@{typically low}@}                          |
> | {@{[melting point](melting%20point.md)}@}                     | {@{typically low}@}                          |
> | {@{[strength](strength%20of%20materials.md)}@}                | {@{typically low}@}                          | <!--SR:!2029-06-13,1648,310!2028-09-10,1555,350!2027-04-03,1055,330!2026-02-17,488,310!2029-10-09,1605,290!2027-09-02,1259,350!2028-10-20,1373,373!2030-08-14,2003,393!2026-05-28,623,341!2028-12-04,1415,382-->

<!--/pytextgen-->

### network covalent solid

A __network covalent solid__, also called __giant covalent structure__, {@{consists of [atoms](atom.md) held together by a network of [covalent bonds](covalent%20bond.md)}@}. <!--SR:!2026-02-18,764,290-->

#### properties of network covalent solid

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

<!--pytextgen generate section="357d"--><!-- The following content is generated at 2026-01-25T23:32:18.096610+08:00. Any edits will be overridden! -->

> | property                                                      | description                                         |
> | ------------------------------------------------------------- | --------------------------------------------------- |
> | {@{[boiling point](boiling%20point.md)}@}                     | {@{typically high}@}                                |
> | {@{[brittleness](brittleness.md)}@}                           | {@{typically high}@}                                |
> | {@{[electrical conductivity](electrical%20conductivity.md)}@} | {@{typically low ([graphite](graphite.md): high)}@} |
> | {@{[melting point](melting%20point.md)}@}                     | {@{typically high}@}                                |
> | {@{[strength](strength%20of%20materials.md)}@}                | {@{typically high ([graphite](graphite.md): low)}@} | <!--SR:!2031-07-05,2145,290!2027-04-15,1150,350!2026-06-05,708,290!2032-08-20,2574,330!2030-04-06,1949,330!2026-12-31,986,330!2027-04-08,973,290!2029-04-25,1547,270!2033-09-02,2763,353!2026-07-16,775,353-->

<!--/pytextgen-->

### ionic solid

A __ionic sold__, also called __giant ionic structure__, {@{consists of [atoms](atom.md) held together by [ionic bonds](ionic%20bond.md)}@}. <!--SR:!2032-09-23,2427,290-->

#### properties of ionic solid

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

<!--pytextgen generate section="5460"--><!-- The following content is generated at 2026-01-25T23:32:18.108731+08:00. Any edits will be overridden! -->

> | property                                                      | description                                                                                                |
> | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
> | {@{[boiling point](boiling%20point.md)}@}                     | {@{typically moderately high}@}                                                                            |
> | {@{[brittleness](brittleness.md)}@}                           | {@{typically extremely high}@}                                                                             |
> | {@{[electrical conductivity](electrical%20conductivity.md)}@} | {@{typically high when [liquid](liquid.md) or [aqueous](aqueous%20solution.md), otherwise typically low}@} |
> | {@{[melting point](melting%20point.md)}@}                     | {@{typically moderately high}@}                                                                            |
> | {@{[strength](strength%20of%20materials.md)}@}                | {@{typically intermediate}@}                                                                               | <!--SR:!2031-11-22,2236,290!2029-11-02,1603,330!2026-02-09,801,330!2027-05-22,994,290!2027-04-28,729,290!2026-09-17,910,330!2027-09-03,980,250!2026-03-15,827,330!2027-04-08,934,353!2027-12-30,1216,373-->

<!--/pytextgen-->

### metallic solid

A __metallic solid__, also called __giant metallic structure__, {@{consists of [metal](metal.md) [ions](ion.md) held together by [metallic bonds](metallic%20bond.md)}@}. <!--SR:!2029-06-30,1701,310-->

#### properties of metallic solid

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

<!--pytextgen generate section="435d"--><!-- The following content is generated at 2026-01-25T23:32:18.117082+08:00. Any edits will be overridden! -->

> | property                                                      | description                                       |
> | ------------------------------------------------------------- | ------------------------------------------------- |
> | {@{[boiling point](boiling%20point.md)}@}                     | {@{typically high ([mercury](mercury.md): low)}@} |
> | {@{[brittleness](brittleness.md)}@}                           | {@{typically low}@}                               |
> | {@{[ductility](ductility.md)}@}                               | {@{typically high}@}                              |
> | {@{[electrical conductivity](electrical%20conductivity.md)}@} | {@{typically high}@}                              |
> | {@{[malleability](malleability.md)}@}                         | {@{typically high}@}                              |
> | {@{[melting point](melting%20point.md)}@}                     | {@{typically high ([mercury](mercury.md): low)}@} |
> | {@{[strength](strength%20of%20materials.md)}@}                | {@{typically low when pure}@}                     |
> | {@{[thermal conductivity](thermal%20conductivity.md)}@}       | {@{typically high}@}                              | <!--SR:!2028-02-23,1093,290!2027-05-01,1164,350!2028-03-12,1160,310!2027-01-09,992,330!2026-10-20,595,230!2027-01-04,989,330!2028-03-23,1122,310!2027-07-03,1214,350!2028-04-20,1173,270!2028-09-05,1551,350!2026-02-25,578,293!2029-03-16,1481,373!2029-08-31,1628,382!2027-03-14,791,322!2031-08-11,2138,361!2031-02-14,2094,402-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/bonding_in_solids) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
