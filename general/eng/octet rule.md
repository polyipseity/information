---
aliases:
  - octet rule
tags:
  - flashcard/active/general/eng/octet_rule
  - language/in/English
---

# octet rule

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

The __octet rule__ is {@{a [chemical](chemistry.md) [rule of thumb](rule%20of%20thumb.md) that states [main-group elements](main-group%20element.md) tend to [bond](chemical%20bond.md) in a way such that each [atom](atom.md) has eight [electrons](electron.md) in its [valence shell](valence%20shell.md)}@}. Other similar rules are {@{the [duplet rule](#^duplet-rule) for [hydrogen](hydrogen.md), [helium](helium.md), and [lithium](lithium.md)}@}; and {@{the [18-electron rule](18-electron%20rule.md) for [transition metals](transition%20metal.md)}@}. <!--SR:!2025-08-04,507,270!2026-11-22,828,290!2026-08-03,376,370-->

## exceptions

{@{[Electron deficit](electron%20deficiency.md) molecules like [boron trifluoride](boron%20trifluoride.md) (BF<sub>3</sub>)}@} {@{do not obey the octet rule}@}. <!--SR:!2026-09-24,632,270!2026-07-30,373,370-->

[Main-group elements](main-group%20element.md) {@{in third [period](period%20(periodic%20table).md) or later can form [hypervalent molecules](hypervalent%20molecule.md)}@} such as {@{[phosphorous pentachloride](phosphorous%20pentachloride.md) (PCl<sub>5</sub>) and [sulfur hexafluoride](sulfur%20hexafluoride.md) (SF<sub>6</sub>)}@}. <!--SR:!2027-11-12,948,250!2025-12-05,178,330-->

## other rules

```Python
# pytextgen generate data
from itertools import chain
return await memorize_table(
  __env__.cwf_sects('309d', '284d'),
  ('name', 'description',),
  (
    ('__duplet rule__', '2 electrons in valence shell', '<a id="^duplet-rule"></a>^duplet-rule'),
    ('__[18-electron rule](18-electron%20rule.md)__', '18 electrons in valence shell', None,),
  ),
  lambda datum: chain(map(cloze, datum[:-2]), (f'{cloze(datum[-2])}{f" {datum[-1]}" if datum[-1] else ""}',),),
)
```

<!--pytextgen generate section="309d"--><!-- The following content is generated at 2023-09-26T08:43:44.011903+08:00. Any edits will be overridden! -->

> | name | description |
> |-|-|
> | {@{__duplet rule__}@} | {@{2 electrons in valence shell}@} <a id="^duplet-rule"></a>^duplet-rule |
> | {@{__[18-electron rule](18-electron%20rule.md)__}@} | {@{18 electrons in valence shell}@} | <!--SR:!2025-08-30,617,330!2032-07-01,2566,350!2032-09-16,2623,350!2025-08-24,612,330-->

<!--/pytextgen-->

<!--pytextgen generate section="284d"--><!-- The following content is generated at 2024-01-04T20:17:52.390426+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←__duplet rule__ <!--SR:!2025-09-09,625,330!2032-09-04,2618,350-->
- __duplet rule__→::@::←__[18-electron rule](18-electron%20rule.md)__ <!--SR:!2032-11-27,2684,350!2032-08-18,2604,350-->
- __[18-electron rule](18-electron%20rule.md)__→::@::←_(end)_ <!--SR:!2025-09-04,620,330!2032-06-06,2547,350-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/octet_rule) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
