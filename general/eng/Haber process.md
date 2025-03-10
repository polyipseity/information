---
aliases:
  - Haber process
  - Haber–Bosch process
tags:
  - flashcard/active/general/eng/Haber_process
  - language/in/English
---

# Haber process

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

The __Haber process__ or __Haber–Bosch process__ is {@{the main industrial process for [ammonia production](ammonia%20production.md)}@}.

The primary reaction is:

> primary reaction
>
> - {@{$\ce{N2(g) + 3H2(g) <=>[\text{finely divided iron}][\text{400–450 °C, 200 atm}] 2NH3(g)}\qquad\Delta{}H=-91.8\ \text{kJ mol}^{-1}$}@}

## process

### nitrogen production

[Nitrogen](nitrogen.md) is obtained by {@{[air separation](air%20separation.md) of [atmospheric air](atmosphere%20of%20Earth.md)}@}.

### hydrogen production

[Hydrogen](hydrogen.md) is obtained {@{from the [electrolysis](electrolysis.md) of [brine](brine.md) and as a [by-product](by-product.md) of [cracking](cracking%20(chemistry).md) of [petroleum](petroleum.md), but the major source is [methane](methane.md)}@}.

```Python
# pytextgen generate data
context = "[natural gas](natural%20gas.md) to [hydrogen](hydrogen.md)"
return await memorize_seq(
  __env__.cwf_sects("d85a", "4956"),
  (
    R"[steam–methane reforming](steam%20reforming.md) to produce [syngas](syngas.md): $\ce{CH4(g) + H2O(g) <=>[NiO][\text{700–1000 °C, 10–20 atm}] 3H2(g) + CO(g)}\qquad\Delta{}H=+206\ \text{kJ mol}^{-1}$",
    R"[water–gas shift reaction](water–gas%20shift%20reaction.md): $\ce{CO(g) + H2O(g) <=> CO2(g) + H2(g)}\qquad\Delta{}H=-41\ \text{kJ mol}^{-1}$",
  ),
  pretext=context,
  posttext=context,
)
```

Starting with a [natural gas](natural%20gas.md) feedstock:

<!--pytextgen generate section="d85a"--><!-- The following content is generated at 2023-05-02T11:22:28.877358+08:00. Any edits will be overridden! -->

> 1. [steam–methane reforming](steam%20reforming.md) to produce [syngas](syngas.md): $\ce{CH4(g) + H2O(g) <=>[NiO][\text{700–1000 °C, 10–20 atm}] 3H2(g) + CO(g)}\qquad\Delta{}H=+206\ \text{kJ mol}^{-1}$
> 2. [water–gas shift reaction](water–gas%20shift%20reaction.md): $\ce{CO(g) + H2O(g) <=> CO2(g) + H2(g)}\qquad\Delta{}H=-41\ \text{kJ mol}^{-1}$

<!--/pytextgen-->

<!--pytextgen generate section="4956"--><!-- The following content is generated at 2024-01-04T20:17:51.755623+08:00. Any edits will be overridden! -->

- _([natural gas](natural%20gas.md) to [hydrogen](hydrogen.md))_→::@::←[steam–methane reforming](steam%20reforming.md) to produce [syngas](syngas.md): $\ce{CH4(g) + H2O(g) <=>[NiO][\text{700–1000 °C, 10–20 atm}] 3H2(g) + CO(g)}\qquad\Delta{}H=+206\ \text{kJ mol}^{-1}$
- [steam–methane reforming](steam%20reforming.md) to produce [syngas](syngas.md): $\ce{CH4(g) + H2O(g) <=>[NiO][\text{700–1000 °C, 10–20 atm}] 3H2(g) + CO(g)}\qquad\Delta{}H=+206\ \text{kJ mol}^{-1}$→::@::←[water–gas shift reaction](water–gas%20shift%20reaction.md): $\ce{CO(g) + H2O(g) <=> CO2(g) + H2(g)}\qquad\Delta{}H=-41\ \text{kJ mol}^{-1}$
- [water–gas shift reaction](water–gas%20shift%20reaction.md): $\ce{CO(g) + H2O(g) <=> CO2(g) + H2(g)}\qquad\Delta{}H=-41\ \text{kJ mol}^{-1}$→::@::←_([natural gas](natural%20gas.md) to [hydrogen](hydrogen.md))_

<!--/pytextgen-->

## industrial production

### large-scale implementation

> {@{![process flow diagram of the Haber process](../../archives/Wikimedia%20Commons/Haber-Bosch-En.svg)}@}
>
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#ecbae7" title="#ECBAE7">&#xFEFF;</span></span> primary reformer
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#4d94e1" title="#4D94E1">&#xFEFF;</span></span> air feed
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#f2c500" title="#F2C500">&#xFEFF;</span></span> secondary reformer
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#cadaeb" title="#CADAEB">&#xFEFF;</span></span> CO conversion
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#cadaeb" title="#CADAEB">&#xFEFF;</span></span> washing tower
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#f2c500" title="#F2C500">&#xFEFF;</span></span> ammonia reactor
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#4d94e1" title="#4D94E1">&#xFEFF;</span></span> heat exchanger
> - <span style="border:thin solid black"><span style="border-left:1.2em solid;border-left-color:#fffc51" title="#FFFC51">&#xFEFF;</span></span> ammonia condenser

```Python
# pytextgen generate data
context = 'large scale implementation of the Haber process'
return await memorize_seq(
  __env__.cwf_sects('ff91', '485b',),
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

<!--pytextgen generate section="ff91"--><!-- The following content is generated at 2023-05-02T10:02:01.861492+08:00. Any edits will be overridden! -->

> 1. Purify and dry [syngas](syngas.md) in purifiers and driers.
> 2. Mix [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) in the ratio of 1:3 by volume.
> 3. The gas mixture is compressed using [axial compressors](axial%20compressor.md). The heat from compression is used to preheat raw gases using [heat exchangers](heat%20exchanger.md).
> 4. The gas mixture is preheated in [heat exchangers](heat%20exchanger.md).
> 5. The gas mixture enters catalytic chambers for reaction.
> 6. The product mixture containing [ammonia](ammonia.md), unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) is cooled to 450 °C in [heat exchangers](heat%20exchanger.md) using fresh reactants, [water](water.md), or other process streams.
> 7. The [ammonia](ammonia.md) liquefies under pressure in a [condenser](condenser.md), is separated by a pressure separator, and collected. Unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) are compressed and recycled by a circulating gas [compressor](compressor.md).

<!--/pytextgen-->

<!--pytextgen generate section="485b"--><!-- The following content is generated at 2024-01-04T20:17:51.833127+08:00. Any edits will be overridden! -->

- _(large scale implementation of the Haber process)_→::@::←Purify and dry [syngas](syngas.md) in purifiers and driers.
- Purify and dry [syngas](syngas.md) in purifiers and driers.→::@::←Mix [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) in the ratio of 1:3 by volume.
- Mix [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) in the ratio of 1:3 by volume.→::@::←The gas mixture is compressed using [axial compressors](axial%20compressor.md). The heat from compression is used to preheat raw gases using [heat exchangers](heat%20exchanger.md).
- The gas mixture is compressed using [axial compressors](axial%20compressor.md). The heat from compression is used to preheat raw gases using [heat exchangers](heat%20exchanger.md).→::@::←The gas mixture is preheated in [heat exchangers](heat%20exchanger.md).
- The gas mixture is preheated in [heat exchangers](heat%20exchanger.md).→::@::←The gas mixture enters catalytic chambers for reaction.
- The gas mixture enters catalytic chambers for reaction.→::@::←The product mixture containing [ammonia](ammonia.md), unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) is cooled to 450 °C in [heat exchangers](heat%20exchanger.md) using fresh reactants, [water](water.md), or other process streams.
- The product mixture containing [ammonia](ammonia.md), unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) is cooled to 450 °C in [heat exchangers](heat%20exchanger.md) using fresh reactants, [water](water.md), or other process streams.→::@::←The [ammonia](ammonia.md) liquefies under pressure in a [condenser](condenser.md), is separated by a pressure separator, and collected. Unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) are compressed and recycled by a circulating gas [compressor](compressor.md).
- The [ammonia](ammonia.md) liquefies under pressure in a [condenser](condenser.md), is separated by a pressure separator, and collected. Unreacted [nitrogen](nitrogen.md) and [hydrogen](hydrogen.md) are compressed and recycled by a circulating gas [compressor](compressor.md).→::@::←_(large scale implementation of the Haber process)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Haber_process) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
