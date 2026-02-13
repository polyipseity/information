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

A __molecular solid__, also called __simple molecular structure__, {@{consists of discrete [molecules](molecule.md) held together by [intermolecular force](intermolecular%20force.md)}@}. If the molecules are [highly organized](crystal%20structure.md), {@{it is also called a __molecular crystal__}@}.

#### properties of molecular solid

```Python
# pytextgen generate data
from pytextgen.compat.util import NULL_LOCATION
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
> | {@{[strength](strength%20of%20materials.md)}@}                | {@{typically low}@}                          |

<!--/pytextgen-->

### network covalent solid

A __network covalent solid__, also called __giant covalent structure__, {@{consists of [atoms](atom.md) held together by a network of [covalent bonds](covalent%20bond.md)}@}.

#### properties of network covalent solid

```Python
# pytextgen generate data
from pytextgen.compat.util import NULL_LOCATION
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
> | {@{[strength](strength%20of%20materials.md)}@}                | {@{typically high ([graphite](graphite.md): low)}@} |

<!--/pytextgen-->

### ionic solid

A __ionic sold__, also called __giant ionic structure__, {@{consists of [atoms](atom.md) held together by [ionic bonds](ionic%20bond.md)}@}.

#### properties of ionic solid

```Python
# pytextgen generate data
from pytextgen.compat.util import NULL_LOCATION
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
> | {@{[strength](strength%20of%20materials.md)}@}                | {@{typically intermediate}@}                                                                               |

<!--/pytextgen-->

### metallic solid

A __metallic solid__, also called __giant metallic structure__, {@{consists of [metal](metal.md) [ions](ion.md) held together by [metallic bonds](metallic%20bond.md)}@}.

#### properties of metallic solid

```Python
# pytextgen generate data
from pytextgen.compat.util import NULL_LOCATION
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
> | {@{[thermal conductivity](thermal%20conductivity.md)}@}       | {@{typically high}@}                              |

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/bonding_in_solids) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
