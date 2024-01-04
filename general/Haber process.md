---
aliases:
  - Haber process
  - Haber–Bosch process
tags:
  - flashcards/general/Haber_process
  - languages/in/English
---

# Haber process

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```

%%

The __Haber process__ or __Haber–Bosch process__ is {{the main industrial process for [ammonia production](ammonia%20production.md)}}. <!--SR:!2024-02-29,213,310-->

The primary reaction is:

> primary reaction
>
> - {{$\ce{N2(g) + 3H2(g) <=>[\text{finely divided iron}][\text{400–450 °C, 200 atm}] 2NH3(g)}\qquad\Delta{}H=-91.8\ \text{kJ mol}^{-1}$}} <!--SR:!2024-02-15,48,190-->

## process

### nitrogen production

[Nitrogen](nitrogen.md) is obtained by {{[air separation](air%20separation.md) of [atmospheric air](atmosphere%20of%20Earth.md)}}. <!--SR:!2024-02-12,200,310-->

### hydrogen production

[Hydrogen](hydrogen.md) is obtained {{from the [electrolysis](electrolysis.md) of [brine](brine.md) and as a [by-product](by-product.md) of [cracking](cracking%20(chemistry).md) of [petroleum](petroleum.md), but the major source is [methane](methane.md)}}. <!--SR:!2024-03-09,195,250-->

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
context = '[natural gas](natural%20gas.md) to [hydrogen](hydrogen.md)'
return await memorize_seq(
  e.cwf_sects('d85a', '4956',),
  (
    R'[steam–methane reforming](steam%20reforming.md) to produce [syngas](syngas.md): $\ce{CH4(g) + H2O(g) <=>[NiO][\text{700–1000 °C, 10–20 atm}] 3H2(g) + CO(g)}\qquad\Delta{}H=+206\ \text{kJ mol}^{-1}$',
    R'[water–gas shift reaction](water–gas%20shift%20reaction.md): $\ce{CO(g) + H2O(g) <=> CO2(g) + H2(g)}\qquad\Delta{}H=-41\ \text{kJ mol}^{-1}$',
  ),
  pretext=context, posttext=context,
)
```

%%

Starting with a [natural gas](natural%20gas.md) feedstock:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d85a"--><!-- The following content is generated at 2023-05-02T11:22:28.877358+08:00. Any edits will be overridden! -->

> 1. [steam–methane reforming](steam%20reforming.md) to produce [syngas](syngas.md): $\ce{CH4(g) + H2O(g) <=>[NiO][\text{700–1000 °C, 10–20 atm}] 3H2(g) + CO(g)}\qquad\Delta{}H=+206\ \text{kJ mol}^{-1}$
> 2. [water–gas shift reaction](water–gas%20shift%20reaction.md): $\ce{CO(g) + H2O(g) <=> CO2(g) + H2(g)}\qquad\Delta{}H=-41\ \text{kJ mol}^{-1}$

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="4956"--><!-- The following content is generated at 2023-05-02T11:22:28.899300+08:00. Any edits will be overridden! -->

1. _([natural gas](natural%20gas.md) to [hydrogen](hydrogen.md))_→:::←[steam–methane reforming](steam%20reforming.md) to produce [syngas](syngas.md): $\ce{CH4(g) + H2O(g) <=>[NiO][\text{700–1000 °C, 10–20 atm}] 3H2(g) + CO(g)}\qquad\Delta{}H=+206\ \text{kJ mol}^{-1}$ <!--SR:!2024-01-12,10,130!2024-02-07,153,310-->
2. [steam–methane reforming](steam%20reforming.md) to produce [syngas](syngas.md): $\ce{CH4(g) + H2O(g) <=>[NiO][\text{700–1000 °C, 10–20 atm}] 3H2(g) + CO(g)}\qquad\Delta{}H=+206\ \text{kJ mol}^{-1}$→:::←[water–gas shift reaction](water–gas%20shift%20reaction.md): $\ce{CO(g) + H2O(g) <=> CO2(g) + H2(g)}\qquad\Delta{}H=-41\ \text{kJ mol}^{-1}$ <!--SR:!2024-03-19,146,230!2024-02-23,182,250-->
3. [water–gas shift reaction](water–gas%20shift%20reaction.md): $\ce{CO(g) + H2O(g) <=> CO2(g) + H2(g)}\qquad\Delta{}H=-41\ \text{kJ mol}^{-1}$→:::←_([natural gas](natural%20gas.md) to [hydrogen](hydrogen.md))_ <!--SR:!2024-07-08,336,330!2024-07-03,217,210-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## industrial production

### large-scale implementation

> {{![process flow diagram of the Haber process](../archives/Wikimedia%20Commons/Haber-Bosch-En.svg)}}
>
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#ecbae7" title="#ECBAE7">&#xFEFF;</span></span> primary reformer
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#4d94e1" title="#4D94E1">&#xFEFF;</span></span> air feed
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#f2c500" title="#F2C500">&#xFEFF;</span></span> secondary reformer
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#cadaeb" title="#CADAEB">&#xFEFF;</span></span> CO conversion
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#cadaeb" title="#CADAEB">&#xFEFF;</span></span> washing tower
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#f2c500" title="#F2C500">&#xFEFF;</span></span> ammonia reactor
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#4d94e1" title="#4D94E1">&#xFEFF;</span></span> heat exchanger
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#fffc51" title="#FFFC51">&#xFEFF;</span></span> ammonia condenser <!--SR:!2024-01-10,159,250-->

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
context = 'large scale implementation of the Haber process'
return await memorize_seq(
  e.cwf_sects('ff91', '485b',),
  (
    'Purify and dry [syngas](syngas.md) in purifiers and driers.',
    'Mix [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) in the ratio of 1:3 by volume.',
    'The gas mixture is compressed using [axial compressors](axial%20compressor.md). The heat from compression is used to preheat raw gases using [heat exchangers](heat%20exchanger.md).',
    'The gas mixture is preheated in [heat exchangers](heat%20exchanger.md).',
    'The gas mixture enters catalytic chambers for reaction.',
    'The product mixture containing [ammonia](ammonia.md), unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) is cooled to 450 °C in [heat exchangers](heat%20exchanger.md) using fresh reactants, [water](water.md), or other process streams.',
    'The [ammonia](ammonia.md) liquefies under pressure in a [condenser](condenser.md), is separated by a pressure separator, and collected. Unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) are compressed and recycled by a circulating gas [compressor](compressor.md).',
  ),
  pretext=context, posttext=context,
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ff91"--><!-- The following content is generated at 2023-05-02T10:02:01.861492+08:00. Any edits will be overridden! -->

> 1. Purify and dry [syngas](syngas.md) in purifiers and driers.
> 2. Mix [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) in the ratio of 1:3 by volume.
> 3. The gas mixture is compressed using [axial compressors](axial%20compressor.md). The heat from compression is used to preheat raw gases using [heat exchangers](heat%20exchanger.md).
> 4. The gas mixture is preheated in [heat exchangers](heat%20exchanger.md).
> 5. The gas mixture enters catalytic chambers for reaction.
> 6. The product mixture containing [ammonia](ammonia.md), unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) is cooled to 450 °C in [heat exchangers](heat%20exchanger.md) using fresh reactants, [water](water.md), or other process streams.
> 7. The [ammonia](ammonia.md) liquefies under pressure in a [condenser](condenser.md), is separated by a pressure separator, and collected. Unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) are compressed and recycled by a circulating gas [compressor](compressor.md).

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="485b"--><!-- The following content is generated at 2023-05-02T10:02:01.876428+08:00. Any edits will be overridden! -->

1. _(large scale implementation of the Haber process)_→:::←Purify and dry [syngas](syngas.md) in purifiers and driers. <!--SR:!2024-03-01,214,310!2024-05-11,288,330-->
2. Purify and dry [syngas](syngas.md) in purifiers and driers.→:::←Mix [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) in the ratio of 1:3 by volume. <!--SR:!2024-02-05,195,310!2024-03-20,229,310-->
3. Mix [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) in the ratio of 1:3 by volume.→:::←The gas mixture is compressed using [axial compressors](axial%20compressor.md). The heat from compression is used to preheat raw gases using [heat exchangers](heat%20exchanger.md). <!--SR:!2024-04-18,201,230!2024-03-06,77,270-->
4. The gas mixture is compressed using [axial compressors](axial%20compressor.md). The heat from compression is used to preheat raw gases using [heat exchangers](heat%20exchanger.md).→:::←The gas mixture is preheated in [heat exchangers](heat%20exchanger.md). <!--SR:!2025-01-31,434,290!2024-01-11,48,210-->
5. The gas mixture is preheated in [heat exchangers](heat%20exchanger.md).→:::←The gas mixture enters catalytic chambers for reaction. <!--SR:!2024-03-03,216,310!2025-03-20,454,290-->
6. The gas mixture enters catalytic chambers for reaction.→:::←The product mixture containing [ammonia](ammonia.md), unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) is cooled to 450 °C in [heat exchangers](heat%20exchanger.md) using fresh reactants, [water](water.md), or other process streams. <!--SR:!2024-01-20,52,210!2024-03-21,230,310-->
7. The product mixture containing [ammonia](ammonia.md), unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) is cooled to 450 °C in [heat exchangers](heat%20exchanger.md) using fresh reactants, [water](water.md), or other process streams.→:::←The [ammonia](ammonia.md) liquefies under pressure in a [condenser](condenser.md), is separated by a pressure separator, and collected. Unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) are compressed and recycled by a circulating gas [compressor](compressor.md). <!--SR:!2024-03-08,194,250!2024-02-25,184,250-->
8. The [ammonia](ammonia.md) liquefies under pressure in a [condenser](condenser.md), is separated by a pressure separator, and collected. Unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) are compressed and recycled by a circulating gas [compressor](compressor.md).→:::←_(large scale implementation of the Haber process)_ <!--SR:!2024-03-02,215,310!2024-06-13,195,230-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Haber_process) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
