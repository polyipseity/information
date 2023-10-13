---
aliases:
  - titration
  - titrimetric analysis
  - titrimetry
  - volumetric analysis
tags:
  - flashcards/general/titration
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# titration

__Titration__ is {{[quantitative](quantitative%20research.md) [chemical method](analytical%20chemistry.md) to determine the [concentration](concentration.md) of an [analyte](analyte.md)}}. <!--SR:!2024-10-02,376,270-->

## types

### acid–base titration

- See: [acid–base titration](acid–base%20titration.md)

Acid–base titrations {{depend on [neutralization](neutralization%20(chemistry).md) between an [acid](acid.md) and a [base](base%20(chemistry).md)}}. It is measured {{using a [pH indicator](pH%20indicator.md)}}. The equivalence point is {{when complete neutralization occurs}}. The end point is {{when the [pH indicator](pH%20indicator.md) changes color sharply}}. For this reason, {{the pH indicator is chosen such that the equivalence point falls in its range of color change}}. For more accuracy, {{a [pH meter](pH%20meter.md) can be used}}. <!--SR:!2024-08-31,323,290!2023-12-30,202,310!2024-04-27,300,330!2023-12-23,199,310!2024-04-25,254,270!2024-02-09,235,310-->

If a [strong acid](acid%20strength.md) and a [strong base](base%20strength.md) are used, {{the [titration curve](#titration%20curve) is regular and many pH indicators are appropriate}}. If one is strong while the other is weak, {{the equivalence point shifts to the stronger side}}. If both are weak, {{the titration curve is very irregular and a [pH meter](pH%20meter.md) is often used instead of a [pH indicator](pH%20indicator.md)}}. <!--SR:!2025-02-26,523,310!2024-01-12,214,310!2024-02-16,242,330-->

## measurement

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_table(
  e.cwf_sects('d981', '248f'),
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

1. _(begin)_→:::←indicator <!--SR:!2023-12-29,200,310!2024-04-07,287,330-->
2. indicator→:::←[pH meter](pH%20meter.md) <!--SR:!2024-05-30,328,330!2023-12-14,178,310-->
3. [pH meter](pH%20meter.md)→:::←[thermometric titration](thermometric%20titration.md) <!--SR:!2024-09-15,366,290!2023-12-28,200,310-->
4. [thermometric titration](thermometric%20titration.md)→:::←_(end)_ <!--SR:!2024-04-19,292,330!2024-02-01,178,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### equivalence and end point

The _equivalence point_ is {{the theoretical completion of titration}}. The _end point_ is {{the actual measured change}}. <!--SR:!2023-12-13,177,310!2024-02-10,236,310-->

### back titration

In back titration, {{a known excess reagent is added to the [solution](solution%20(chemistry).md), and the excess is titrated instead of the original solution}}. <!--SR:!2024-03-16,225,270-->
