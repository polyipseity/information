---
aliases:
  - adiabatic index
  - adiabatic indexes
  - adiabatic indices
  - heat capacity ratio
  - heat capacity ratios
tags:
  - flashcard/active/general/heat_capacity_ratio
  - language/in/English
---

# heat capacity ratio

> __heat capacity ratio__
>
> {@{$$\gamma = \frac{C_p}{C_V} = \frac{\bar{C}_p}{\bar{C}_V} = \frac{c_p}{c_V}$$}@}
>
> - where
>   - {@{$C$ is the [heat capacity](heat%20capcaity.md), $\bar{C}$ is the [molar heat capacity](molar%20heat%20capacity.md), and $c$ is the [specific heat capacity](specific%20heat%20capacity.md); the subscript $p$ and $V$ means [constant pressure](isobaric%20process.md) and [constant volume](isochoric%20process.md) respectively}@} <!--SR:!2024-11-29,268,330!2026-01-14,477,270-->

<!-- markdownlint MD028 -->

> [!tip] tips
>
> - $Q / W$ ::@:: Since the extra [heat capacity](heat%20capacity.md) of [isobaric processes](isobaric%20process.md) comes from [work](work%20(physics).md), therefore $Q / W = \gamma / (\gamma - 1)$ for [isobaric processes](isobaric%20process.md). For a generalization, see [polytropic process § relation between polytropic index and energy transfer ratio](polytropic%20process.md#relation%20between%20polytropic%20index%20and%20energy%20transfer%20ratio). <!--SR:!2025-03-01,292,290!2025-01-02,215,333-->

## ideal gas relations

[Mayer's relation](Mayer's%20relation.md) {@{provides a convenient way to deduce $C_V$ from the more easily found and commonly tabulated $C_p$}@}. <!--SR:!2025-11-09,483,310-->

### relation with degrees of freedom

> __relation between heat capacity ratio and degrees of freedom for an ideal gas__
>
> {@{$$\gamma = 1 + \frac2f \quad \text{or} \quad f = \frac2{\gamma - 1}$$}@}
>
> - where
>   - {@{$\gamma$ is the heat capacity ratio and $f$ is the thermally accessible [degrees of freedom](degrees%20of%20freedom%20(physics%20and%20chemistry).md)}@}
> - conditions: {@{[ideal gas](ideal%20gas.md)}@} <!--SR:!2025-04-22,247,230!2025-03-12,300,290!2025-11-24,494,310-->

#### derivation

Consider an [ideal gas](ideal%20gas.md). For [constant volume](isochoric%20process.md) condition, {@{no [work](work%20(physics).md) is done on the surroundings. Therefore, all supplied [heat](heat.md) increases the [internal energy](internal%20energy.md): $\Delta U = Q$}@}. Compare that with [constant pressure](constant%20pressure.md) condition, {@{where the [volume](volume.md) increases, so [work](work%20(physics).md) is done on the surroundings. Therefore, some supplied [heat](heat.md) goes to [work](work%20(physics).md) instead of [internal energy](internal%20energy.md): $\Delta U = Q - W$}@}. We can derive this ratio: <!--SR:!2026-02-06,547,310!2027-02-16,861,310-->

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
