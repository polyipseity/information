---
aliases:
  - octet rule
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# octet rule

The __octet rule__ is {{a [chemical](chemistry.md) [rule of thumb](rule%20of%20thumb.md) that states [main-group elements](main-group%20element.md) tend to [bond](chemical%20bond.md) in a way such that each [atom](atom.md) has eight [electrons](electron.md) in its [valence shell](valence%20shell.md)}}. Other similar rules are {{the [duplet rule](#^duplet-rule) for [hydrogen](hydrogen.md), [helium](helium.md), and [lithium](lithium.md); and the [18-electron rule](18-electron%20rule.md) for [transition metals](transition%20metal.md)}}.

## exceptions

{{[Electron deficit](electron%20deficiency.md) molecules like [boron trifluoride](boron%20trifluoride.md) (BF<sub>3</sub>)}} do not obey the octet rule.

[Main-group elements](main-group%20element.md) {{in third [period](period%20(periodic%20table).md) or later can form [hypervalent molecules](hypervalent%20molecule.md) such as [phosphorous pentachloride](phosphorous%20pentachloride.md) (PCl<sub>5</sub>) and [sulfur hexafluoride](sulfur%20hexafluoride.md) (SF<sub>6</sub>)}}.

## other rules

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from itertools import chain
e = __env__
return await memorize_table(
	(e.cwf_sect('309d'), e.cwf_sect('284d'),),
	('name', 'description',),
	(
		('__duplet rule__', '2 electrons in valence shell', '^duplet-rule'),
		('__[18-electron rule](18-electron%20rule.md)__', '18 electrons in valence shell', None,),
	),
	lambda datum: chain(map(cloze, datum[:-2]), (f'{cloze(datum[-2])}{f" {datum[-1]}" if datum[-1] else ""}',),),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="309d"--><!-- The following content is generated at 2023-03-20T16:20:31.070686+08:00. Any edits will be overridden! -->

> | name | description |
> |-|-|
> | {{__duplet rule__}} | {{2 electrons in valence shell}} ^duplet-rule |
> | {{__[18-electron rule](18-electron%20rule.md)__}} | {{18 electrons in valence shell}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="284d"--><!-- The following content is generated at 2023-03-20T12:51:18.460734+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←__duplet rule__
2. __duplet rule__→:::←__[18-electron rule](18-electron%20rule.md)__
3. __[18-electron rule](18-electron%20rule.md)__→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
