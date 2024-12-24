---
aliases:
  - group
  - group (periodic table)
  - groups
tags:
  - flashcard/active/general/eng/group__periodic_table_
  - language/in/English
---

# group (periodic table)

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

A __group__ is {@{a column of [chemical elements](chemical%20element.md) in the [periodic table](periodic%20table.md)}@}. The elements have {@{similar [chemical](chemical%20property.md) or [physical](physical%20property.md) characteristics in their outermost [electron shells](electron%20shell.md)}@}. <!--SR:!2027-01-04,1068,350!2028-11-26,1534,310-->

## list

```Python
# pytextgen generate data
from itertools import chain
return await memorize_table(
  __env__.cwf_sects('8462', '92de'),
  ('name (IUPAC/old IUPAC/old CAS)', 'IUPAC recommended trivial name',),
  (
    ('[group 1](#^group-1)/IA/IA', '[hydrogen](hydrogen.md) and [alkali metals](alkali%20metal.md)', '<a id="^group-1"></a>^group-1',),
    ('[group 2](alkaline%20earth%20metal.md)/IIA/IIA', '[alkaline earth metals](alkaline%20earth%20metal.md)', None,),
    ('[group 17](halogen.md)/VIIB/VIIA', '[halogens](halogen.md)', None,),
    ('[group 18](noble%20gas.md)/0/VIIIA', '[noble gases](noble%20gas.md)', None,),
  ),
  lambda datum: chain(map(cloze, datum[:-2]), (f'{cloze(datum[-2])}{f" {datum[-1]}" if datum[-1] else ""}',),),
)
```

<!--pytextgen generate section="8462"--><!-- The following content is generated at 2023-09-26T08:44:21.496687+08:00. Any edits will be overridden! -->

> | name (IUPAC/old IUPAC/old CAS) | IUPAC recommended trivial name |
> |-|-|
> | {@{[group 1](#^group-1)/IA/IA}@} | {@{[hydrogen](hydrogen.md) and [alkali metals](alkali%20metal.md)}@} <a id="^group-1"></a>^group-1 |
> | {@{[group 2](alkaline%20earth%20metal.md)/IIA/IIA}@} | {@{[alkaline earth metals](alkaline%20earth%20metal.md)}@} |
> | {@{[group 17](halogen.md)/VIIB/VIIA}@} | {@{[halogens](halogen.md)}@} |
> | {@{[group 18](noble%20gas.md)/0/VIIIA}@} | {@{[noble gases](noble%20gas.md)}@} | <!--SR:!2026-12-07,966,330!2026-06-02,870,330!2026-12-10,969,330!2026-09-05,900,330!2025-10-16,501,330!2026-10-14,926,330!2027-02-09,1011,330!2027-06-17,1196,350-->

<!--/pytextgen-->

<!--pytextgen generate section="92de"--><!-- The following content is generated at 2024-01-04T20:17:51.853130+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[group 1](#^group-1)/IA/IA <!--SR:!2027-01-22,998,330!2028-09-15,1555,350-->
- [group 1](#^group-1)/IA/IA→::@::←[group 2](alkaline%20earth%20metal.md)/IIA/IIA <!--SR:!2026-03-12,771,330!2027-10-05,1280,350-->
- [group 2](alkaline%20earth%20metal.md)/IIA/IIA→::@::←[group 17](halogen.md)/VIIB/VIIA <!--SR:!2026-03-08,679,270!2026-07-10,857,330-->
- [group 17](halogen.md)/VIIB/VIIA→::@::←[group 18](noble%20gas.md)/0/VIIIA <!--SR:!2025-08-26,604,310!2027-01-06,989,330-->
- [group 18](noble%20gas.md)/0/VIIIA→::@::←_(end)_ <!--SR:!2028-09-10,1551,350!2027-01-03,986,330-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/group_(periodic_table)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
