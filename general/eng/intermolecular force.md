---
aliases:
  - intermolecular force
  - intermolecular forces
tags:
  - flashcard/active/general/eng/intermolecular_force
  - language/in/English
---

# intermolecular force

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

__Intermolecular forces__ are {@{attractive or replusive [forces](force.md) between [molecules](molecule.md)}@}. They are {@{relatively weak}@} compared to [intramolecular forces](intramolecular%20force.md).

Attractive forces include {@{[van der Waals forces](van%20der%20Waals%20force.md), [hydrogen bond](hydrogen%20bond.md), and [ion](ion.md)–(induced) dipole forces}@}.

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
> | {@{[London dispersion force](London%20dispersion%20force.md)}@} | {@{0.01–63 kJ/mol}@} |

<!--/pytextgen-->

<!--pytextgen generate section="ff83"--><!-- The following content is generated at 2024-03-07T00:12:03.503454+08:00. Any edits will be overridden! -->

- _(strongest)_→::@::←[covalent bond](covalent%20bond.md)
- [covalent bond](covalent%20bond.md)→::@::←[hydrogen bond](hydrogen%20bond.md)
- [hydrogen bond](hydrogen%20bond.md)→::@::←[London dispersion force](London%20dispersion%20force.md)
- [London dispersion force](London%20dispersion%20force.md)→::@::←_(weakest)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/intermolecular_force) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
