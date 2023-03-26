---
aliases: ['titration', 'titrimetric analysis', 'titrimetry', 'volumetric analysis',]
---

#academic/chemistry #flashcards/academic/Tt/titration

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# titration

__Titration__ is {{[quantitative](quantitative%20research.md) [chemical method](analytical%20chemistry.md) to determine the [concentration](concentration.md) of an [analyte](analyte.md)}}.

## types

### acid–base titration

- See: [acid–base titration](acid–base%20titration.md)

Acid–base titrations {{depend on [neutralization](neutralization%20(chemistry).md) between an [acid](acid.md) and a [base](base%20(chemistry).md)}}. It is measured {{using a [pH indicator](pH%20indicator.md)}}. The equivalence point is {{when complete neutralization occurs}}. The end point is {{when the [pH indicator](pH%20indicator.md) changes color sharply}}. For this reason, {{the pH indicator is chosen such that the equivalence point falls in its range of color change}}. For more accuracy, {{a [pH meter](pH%20meter.md) can be used}}.

If a [strong acid](acid%20strength.md) and a [strong base](base%20strength.md) are used, {{the [titration curve](#titration%20curve) is regular and many pH indicators are appropriate}}. If one is strong while the other is weak, {{the equivalence point shifts to the stronger side}}. If both are weak, {{the titration curve is very irregular and a [pH meter](pH%20meter.md) is often used instead of a [pH indicator](pH%20indicator.md)}}.

## measurement

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_table(
	(e.cwf_section('d981'), e.cwf_section('248f'),),
	('name', 'description',),
	(
		('indicator', 'Using a [substance](chemical%20substance.md) that changes color to a [chemical change](chemical%20change.md) to monitor the reaction. [pH indicators](pH%20indicator.md) are used in [acid–base titration](#acid–base%20titration).',),
		('[pH meter](pH%20meter.md)', 'The [pH](pH.md) is measured throughout the reaction. A sudden pH change happens at the end point.',),
		('[thermometric titration](thermometric%20titration.md)', 'The [temperature](temperature.md) change is measured and then plotted to find the end point.',),
	),
)
```
%%

Methods to determine the end point include:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d981"--><!-- The following content is generated at 2023-03-23T18:13:41.619815+08:00. Any edits will be overridden! -->

> | name | description |
> |-|-|
> | indicator | Using a [substance](chemical%20substance.md) that changes color to a [chemical change](chemical%20change.md) to monitor the reaction. [pH indicators](pH%20indicator.md) are used in [acid–base titration](#acid–base%20titration). |
> | [pH meter](pH%20meter.md) | The [pH](pH.md) is measured throughout the reaction. A sudden pH change happens at the end point. |
> | [thermometric titration](thermometric%20titration.md) | The [temperature](temperature.md) change is measured and then plotted to find the end point. |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="248f"--><!-- The following content is generated at 2023-03-23T18:13:41.634856+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←indicator
2. indicator→:::←[pH meter](pH%20meter.md)
3. [pH meter](pH%20meter.md)→:::←[thermometric titration](thermometric%20titration.md)
4. [thermometric titration](thermometric%20titration.md)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### equivalence and end point

The _equivalence point_ is {{the theoretical completion of titration}}. The _end point_ is {{the actual measured change}}.

### back titration

In back titration, {{a known excess reagent is added to the [solution](solution%20(chemistry).md), and the excess is titrated instead of the original solution}}.
