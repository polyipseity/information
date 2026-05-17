---
aliases:
  - adiabatic index
  - adiabatic indexes
  - adiabatic indices
  - heat capacity ratio
  - heat capacity ratios
tags:
  - flashcard/active/general/eng/heat_capacity_ratio
  - language/in/English
---

# heat capacity ratio

> __heat capacity ratio__
>
> {@{$$\gamma = \frac{C_p}{C_V} = \frac{\bar{C}_p}{\bar{C}_V} = \frac{c_p}{c_V}$$}@}
>
> where
>
> - {@{$C$}@} is {@{the [heat capacity](heat%20capcaity.md)}@}
> - {@{$\bar{C}$}@} is {@{the [molar heat capacity](molar%20heat%20capacity.md)}@}
> - {@{$c$}@} is {@{the [specific heat capacity](specific%20heat%20capacity.md)}@}
> - {@{the subscript $p$ and $V$}@} means {@{[constant pressure](isobaric%20process.md) and [constant volume](isochoric%20process.md) respectively}@} <!--SR:!2028-04-01,1219,350!2030-12-21,1799,290!2026-10-11,250,346!2027-02-17,362,366!2027-03-08,376,366!2027-04-01,394,366!2027-03-31,393,366!2027-04-03,396,366!2027-04-04,397,366-->

<!-- markdownlint MD028 -->

> [!tip] tips
>
> - $Q / W$ ::@:: Since the extra [heat capacity](heat%20capacity.md) of [isobaric processes](isobaric%20process.md) comes from [work](work%20(physics).md), therefore $Q / W = \gamma / (\gamma - 1)$ for [isobaric processes](isobaric%20process.md). For a generalization, see [polytropic process § relation between polytropic index and energy transfer ratio](polytropic%20process.md#relation%20between%20polytropic%20index%20and%20energy%20transfer%20ratio). <!--SR:!2027-06-19,840,290!2026-12-18,715,333-->

## ideal gas relations

{@{[Mayer's relation](Mayer's%20relation.md)}@} provides {@{a convenient way to deduce $C_V$}@} from {@{the more easily found and commonly tabulated $C_p$}@}. <!--SR:!2029-12-12,1494,310!2027-01-22,353,360!2027-02-05,365,360-->

### relation with degrees of freedom

> __relation between heat capacity ratio and degrees of freedom for an ideal gas__
>
> - conditions: {@{[ideal gas](ideal%20gas.md)}@}
>
> {@{$$\gamma = 1 + \frac2f \quad \text{or} \quad f = \frac2{\gamma - 1}$$}@}
>
> where
>
> - {@{$\gamma$}@} is {@{the heat capacity ratio}@}
> - {@{$f$}@} is {@{the thermally accessible [degrees of freedom](degrees%20of%20freedom%20(physics%20and%20chemistry).md)}@} <!--SR:!2027-07-02,801,250!2027-02-16,558,290!2031-09-13,2119,330!2027-03-12,380,366!2027-04-05,398,366!2027-04-02,395,366-->

#### derivation

Consider {@{an [ideal gas](ideal%20gas.md)}@}. For {@{[constant volume](isochoric%20process.md) condition}@}, {@{no [work](work%20(physics).md) is done on the surroundings}@}. Therefore, {@{all supplied [heat](heat.md)}@} increases {@{the [internal energy](internal%20energy.md): $\Delta U = Q$}@}. Compare that with {@{[constant pressure](constant%20pressure.md) condition, where the [volume](volume.md) increases}@}, so {@{[work](work%20(physics).md) is done on the surroundings}@}. Therefore, {@{some supplied [heat](heat.md)}@} goes to {@{[work](work%20(physics).md) instead of [internal energy](internal%20energy.md)}@}: {@{$$\Delta U = Q - W \,.$$}@} We can derive {@{this ratio}@}: <!--SR:!2030-10-01,1698,310!2027-02-16,861,310!2026-06-20,95,371!fsrs,2027-11-20T03:28:54.300Z,523,522.5183221,1,2,8,0,0,2026-06-15T03:28:54.300Z!fsrs,2027-11-10T10:12:22.784Z,514,514.43261153,1,2,7,0,0,2026-06-14T10:12:22.784Z!fsrs,2027-10-01T10:01:27.136Z,483,482.53730635,1,2,7,0,0,2026-06-05T10:01:27.136Z!fsrs,2027-10-07T00:56:32.187Z,488,487.56217659,1,2,7,0,0,2026-06-06T00:56:32.187Z!fsrs,2027-11-14T10:12:23.589Z,518,517.7137874,1,2,7,0,0,2026-06-14T10:12:23.589Z!fsrs,2027-10-14T01:37:44.394Z,493,492.57902295,1,2,7,0,0,2026-06-08T01:37:44.394Z!fsrs,2027-12-01T00:00:00.000Z,532,532.43883878,1,2,8,0,0,2026-06-17T00:00:00.000Z!fsrs,2027-12-07T00:00:00.000Z,537,537.38840954,1,2,8,0,0,2026-06-18T00:00:00.000Z-->

> __derivation of relation between heat capacity ratio and degrees of freedom for an ideal gas__
>
> $$\begin{aligned}
> \mathrm{d}V & = \left(\frac{\partial V}{\partial p}\right)_T \,\mathrm{d}p + \left(\frac{\partial V}{\partial T}\right)_p \,\mathrm{d}T && (V(p, T)) \\
> & = \left(\frac{\partial V}{\partial T}\right)_p \,\mathrm{d}T && (\text{isobaric process}) \\
> \mathrm{d}W & = p \,\mathrm{d}V \\
> & = p \left(\frac{\partial V}{\partial T}\right)_p \,\mathrm{d}T \\
> & = p \frac{nR}{p} \,\mathrm{d}T \\
> & = nR \,\mathrm{d}T \\
> W &= nR \\
> C_V & = \frac{f}2nR && (\text{equipartition theorem}) \\
> C_p & = \frac{f}2nR + nR && (\text{equipartition theorem}) \\
> & = \frac{f + 2}2nR \\
> \frac{C_p}{C_V} & = \frac{f + 2}f = 1 + \frac2f
> \end{aligned}$$

## adiabatic process

- see: [adiabatic process](adiabatic%20process.md), [polytropic process](polytropic%20process.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/heat_capacity_ratio) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
