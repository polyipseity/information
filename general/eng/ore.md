---
tags:
  - flashcard/active/general/ore
  - language/in/English
---

# ore

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

An __ore__ is {@{a [rock](rock%20(geology).md) or [sediment](sediment.md) containing valuable [minerals](mineral.md) [concentrated](concentration.md) above background levels.}@}

## extraction

See [extractive metallurgy](extractive%20metallurgy.md).

## important ores

```Python
# pytextgen generate data
return await memorize_table(
  __env__.cwf_sects('283749', '0398da'),
  ('name', 'formula',),
  (
    ('[bauxite](bauxite.md)', 'Al(OH)<sub>3</sub>, AlOOH',),
    ('[chalcopyrite](chalcopyrite.md), copper pyrite', 'CuFeS<sub>2</sub>',),
    ('[cinnabar](cinnabar.md), cinnabarite', 'HgS',),
    ('[galena](galena.md)', 'PbS',),
    ('[hematite](hematite.md)', 'Fe<sub>2</sub>O<sub>3</sub>',),
  ),
  lambda datum: map(cloze, datum),
)
```

<!--pytextgen generate section="283749"--><!-- The following content is generated at 2023-03-22T00:41:25.734579+08:00. Any edits will be overridden! -->

> | name | formula |
> |-|-|
> | {@{[bauxite](bauxite.md)}@} | {@{Al(OH)<sub>3</sub>, AlOOH}@} |
> | {@{[chalcopyrite](chalcopyrite.md), copper pyrite}@} | {@{CuFeS<sub>2</sub>}@} |
> | {@{[cinnabar](cinnabar.md), cinnabarite}@} | {@{HgS}@} |
> | {@{[galena](galena.md)}@} | {@{PbS}@} |
> | {@{[hematite](hematite.md)}@} | {@{Fe<sub>2</sub>O<sub>3</sub>}@} |

<!--/pytextgen-->

<!--pytextgen generate section="0398da"--><!-- The following content is generated at 2024-01-04T20:17:52.269345+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[bauxite](bauxite.md)
- [bauxite](bauxite.md)→::@::←[chalcopyrite](chalcopyrite.md), copper pyrite
- [chalcopyrite](chalcopyrite.md), copper pyrite→::@::←[cinnabar](cinnabar.md), cinnabarite
- [cinnabar](cinnabar.md), cinnabarite→::@::←[galena](galena.md)
- [galena](galena.md)→::@::←[hematite](hematite.md)
- [hematite](hematite.md)→::@::←_(end)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/ore) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
