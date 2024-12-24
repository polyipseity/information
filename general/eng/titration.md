---
aliases:
  - titration
  - titrimetric analysis
  - titrimetry
  - volumetric analysis
tags:
  - flashcard/active/general/eng/titration
  - language/in/English
---

# titration

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

__Titration__ is {@{[quantitative](quantitative%20research.md) [chemical method](analytical%20chemistry.md) to determine the [concentration](concentration.md) of an [analyte](analyte.md)}@}. <!--SR:!2027-07-13,1014,270-->

## types

### acid–base titration

- see: [acid–base titration](acid–base%20titration.md)

Acid–base titrations {@{depend on [neutralization](neutralization%20(chemistry).md) between an [acid](acid.md) and a [base](base%20(chemistry).md)}@}. It is measured {@{using a [pH indicator](pH%20indicator.md)}@}. The equivalence point is {@{when complete neutralization occurs}@}. The end point is {@{when the [pH indicator](pH%20indicator.md) changes color sharply}@}. For this reason, {@{the pH indicator is chosen such that the equivalence point falls in its range of color change}@}. For more accuracy, {@{a [pH meter](pH%20meter.md) can be used}@}. <!--SR:!2027-03-25,936,290!2026-05-14,866,330!2027-01-13,991,330!2025-08-31,616,310!2026-03-11,685,270!2026-11-12,1007,330-->

If a [strong acid](acid%20strength.md) and a [strong base](base%20strength.md) are used, {@{the [titration curve](#titration%20curve) is regular and many pH indicators are appropriate}@}. If one is strong while the other is weak, {@{the equivalence point shifts to the stronger side}@}. If both are weak, {@{the titration curve is very irregular and a [pH meter](pH%20meter.md) is often used instead of a [pH indicator](pH%20indicator.md)}@}. <!--SR:!2025-02-26,523,310!2026-07-17,917,330!2027-02-23,1103,350-->

## measurement

```Python
# pytextgen generate data
return await memorize_table(
  __env__.cwf_sects('d981', '248f'),
  ('name', 'description',),
  (
    ('indicator', 'Using a [substance](chemical%20substance.md) that changes color to a [chemical change](chemical%20change.md) to monitor the reaction. [pH indicators](pH%20indicator.md) are used in [acid–base titration](#acid–base%20titration).',),
    ('[pH meter](pH%20meter.md)', 'The [pH](pH.md) is measured throughout the reaction. A sudden pH change happens at the end point.',),
    ('[thermometric titration](thermometric%20titration.md)', 'The [temperature](temperature.md) change is measured and then plotted to find the end point.',),
  ),
)
```

Methods to determine the end point include:

<!--pytextgen generate section="d981"--><!-- The following content is generated at 2023-03-23T18:13:41.619815+08:00. Any edits will be overridden! -->

> | name | description |
> |-|-|
> | indicator | Using a [substance](chemical%20substance.md) that changes color to a [chemical change](chemical%20change.md) to monitor the reaction. [pH indicators](pH%20indicator.md) are used in [acid–base titration](#acid–base%20titration). |
> | [pH meter](pH%20meter.md) | The [pH](pH.md) is measured throughout the reaction. A sudden pH change happens at the end point. |
> | [thermometric titration](thermometric%20titration.md) | The [temperature](temperature.md) change is measured and then plotted to find the end point. |

<!--/pytextgen-->

<!--pytextgen generate section="248f"--><!-- The following content is generated at 2024-01-04T20:17:52.903712+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←indicator <!--SR:!2026-05-04,857,330!2026-11-10,946,330-->
- indicator→::@::←[pH meter](pH%20meter.md) <!--SR:!2027-05-13,1078,330!2025-06-17,551,310-->
- [pH meter](pH%20meter.md)→::@::←[thermometric titration](thermometric%20titration.md) <!--SR:!2027-08-11,1060,290!2025-09-07,619,310-->
- [thermometric titration](thermometric%20titration.md)→::@::←_(end)_ <!--SR:!2027-12-08,1328,350!2025-04-20,444,250-->

<!--/pytextgen-->

### equivalence and end point

The _equivalence point_ is {@{the theoretical completion of titration}@}. The _end point_ is {@{the actual measured change}@}. <!--SR:!2026-01-09,758,330!2026-11-18,1011,330-->

### back titration

In back titration, {@{a known excess reagent is added to the [solution](solution%20(chemistry).md), and the excess is titrated instead of the original solution}@}. <!--SR:!2025-11-15,607,270-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/titration) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
