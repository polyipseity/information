---
aliases:
  - Maxwell distribution
  - Maxwell distributions
  - Maxwellian distribution
  - Maxwellian distributions
  - Maxwell-Boltzmann distribution
  - Maxwell-Boltzmann distributions
  - Maxwell–Boltzmann distribution
  - Maxwell–Boltzmann distributions
tags:
  - flashcard/active/general/eng/Maxwell-Boltzmann_distribution
  - language/in/English
---

# Maxwell–Boltzmann distribution

## distribution function

> __Maxwell–Boltzmann distribution in [three-dimensional space](three-dimensional%20space.md)__
>
> - conditions: {@{requires [kinetic theory of gases](kinetic%20theory%20of%20gases.md), which applies to [ideal gases](ideal%20gas.md) and approximates [real gases](real%20gas.md)}@}
>
> {@{$$\begin{aligned} f(\vec{v}) \,\mathrm{d}^3\vec{v} & = \left(\frac{m}{2\pi k T}\right)^\frac32 \exp\left( -\frac{m\lvert\vec{v}\rvert^2}{2kT} \right) \,\mathrm{d}^3\vec{v} \\ f(v) \,\mathrm{d}v & = 4\pi v^2 \left(\frac{m}{2\pi k T}\right)^\frac32 \exp\left(-\frac{mv^2}{2kT}\right) \,\mathrm{d}v \end{aligned}$$}@}
>
> where
>
> - [function](function%20(mathematics).md) properties
>   - {@{$f(\vec{v})$}@} is {@{a [probability density function](probability%20density%20function.md)}@}, showing {@{the fraction of [particles](particle.md) within an infinitesimal element of the three-dimensional velocity space $\mathrm{d}^3\vec{v}$}@} centered on {@{a velocity vector $\vec{v}$}@}, {@{properly normalized}@} such that {@{$\int f(\vec{v}) \,\mathrm{d}^3\vec{v}$ over all velocity vectors is unity}@}
>   - {@{$f(v)$}@} is {@{another [probability density function](probability%20density%20function.md)}@}, showing {@{the density of [particles](particle.md) with velocity $v$}@}, {@{properly normalized}@} such that {@{$\int_0^\infty f(v) \,\mathrm{d}v$ is unity}@}
> - system properties: $m$ is {@{the [particle](particle.md) [mass](mass.md)}@} and $T$ is {@{the [thermodynamic temperature](thermodynamic%20temperature.md)}@}
> - {@{$k_\text{B} = 1.380\,649 \times 10^{−23} \mathrm{\ J \cdot K^{−1} }$}@} is {@{the [Boltzmann constant](Boltzmann%20constant.md)}@} <!--SR:!2026-04-19,94,138!2027-09-23,990,298!2027-12-04,1033,298!2026-10-08,717,318!2031-04-14,1877,298!2026-06-17,143,303!2026-11-19,285,343!2026-10-04,231,323!2026-12-02,295,343!2027-01-16,330,343!2026-09-29,227,323!2026-11-27,292,343!2026-11-29,293,343!2026-12-31,319,343!2026-08-14,191,323!2026-11-20,286,342!2026-12-03,296,343-->

## typical speeds

- average speed $\langle v \rangle$ ::@:: $\langle v \rangle = \frac2{\sqrt\pi}v_p = \sqrt{\frac{8kT}{\pi{}m} } = \sqrt{\frac{8RT}{\pi{}M} } \left( \text{evaluate } \int_0^\infty v f(v) \,\mathrm{d}v \right)$ <!--SR:!2027-06-03,473,230!2026-06-21,157,250-->
- most probable speed $v_p$ ::@:: $v_p = \sqrt{\frac{2kT}m} = \sqrt{\frac{2RT}M} \left( \text{solve for } v \text{ in } \frac{\mathrm{d}f(v)}{\mathrm{d}v} = 0 \right)$ <!--SR:!2028-04-06,1041,290!2028-03-11,988,270-->
- root-mean-square speed $v_\mathrm{rms}$ ::@:: $v_\mathrm{rms} = \sqrt{\frac32}v_p=\sqrt{\frac{3kT}m} = \sqrt{\frac{3RT}M} \left( \text{evaluate } \sqrt{\int_0^\infty v^2 f(v) \,\mathrm{d}v} \right)$ <!--SR:!2026-05-03,600,310!2028-02-16,936,270-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Maxwell–Boltzmann_distribution) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
