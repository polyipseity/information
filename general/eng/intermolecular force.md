---
aliases:
  - intermolecular force
  - intermolecular forces
tags:
  - flashcard/active/general/intermolecular_force
  - language/in/English
---

# intermolecular force

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

__Intermolecular forces__ are {@{attractive or replusive [forces](force.md) between [molecules](molecule.md)}@}. They are {@{relatively weak}@} compared to [intramolecular forces](intramolecular%20force.md). <!--SR:!2025-08-18,640,310!2026-05-29,878,330-->

Attractive forces include {@{[van der Waals forces](van%20der%20Waals%20force.md), [hydrogen bond](hydrogen%20bond.md), and [ion](ion.md)–(induced) dipole forces}@}. <!--SR:!2026-11-15,797,250-->

## relative strength

```Python
# pytextgen generate data
return await memorize_table(
  __env__.cwf_sects('294a', 'ff83'),
  ('type', 'dissociation energy',),
  (
    ('[covalent bond](covalent%20bond.md)', '130–1100 kJ/mol',),
    ('[hydrogen bond](hydrogen%20bond.md)', '4–50 kJ/mol',),
    ('[London dispersion force](London%20dispersion%20force.md)', '0.01–63 kJ/mol',),
  ),
  lambda datum: map(cloze, datum),
  pretext="strongest", posttext="weakest",
)
```

<!--pytextgen generate section="294a"--><!-- The following content is generated at 2023-03-26T19:44:39.015343+08:00. Any edits will be overridden! -->

> | type | dissociation energy |
> |-|-|
> | {@{[covalent bond](covalent%20bond.md)}@} | {@{130–1100 kJ/mol}@} |
> | {@{[hydrogen bond](hydrogen%20bond.md)}@} | {@{4–50 kJ/mol}@} |
> | {@{[London dispersion force](London%20dispersion%20force.md)}@} | {@{0.01–63 kJ/mol}@} | <!--SR:!2025-12-16,693,310!2025-05-08,193,170!2027-03-06,1031,330!2026-08-20,624,210!2026-11-13,949,330!2028-05-12,1237,290-->

<!--/pytextgen-->

<!--pytextgen generate section="ff83"--><!-- The following content is generated at 2024-03-07T00:12:03.503454+08:00. Any edits will be overridden! -->

- _(strongest)_→::@::←[covalent bond](covalent%20bond.md) <!--SR:!2027-06-22,1198,350!2027-03-03,1114,350-->
- [covalent bond](covalent%20bond.md)→::@::←[hydrogen bond](hydrogen%20bond.md) <!--SR:!2026-11-10,946,330!2028-04-05,1425,350-->
- [hydrogen bond](hydrogen%20bond.md)→::@::←[London dispersion force](London%20dispersion%20force.md) <!--SR:!2027-07-15,1218,350!2026-08-13,883,330-->
- [London dispersion force](London%20dispersion%20force.md)→::@::←_(weakest)_ <!--SR:!2028-08-06,1523,350!2027-04-06,1137,350-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/intermolecular_force) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
