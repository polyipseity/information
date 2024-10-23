---
aliases:
  - thermal expansion
tags:
  - flashcard/active/general/thermal_expansion
  - language/in/English
---

# thermal expansion

## expansion in solids

### linear expansion

> __coefficient of linear thermal expansion__
>
> {{$$\begin{aligned} \alpha_L & = \frac1L \frac{\mathrm{d}L}{\mathrm{d}T} \\ \frac{\mathrm{d}L}L & = \alpha_L \,\mathrm{d}T \end{aligned}$$}}
>
> - where
>   - {{$\alpha_L$ is the __coefficient of linear thermal expansion__, $L$ is the [length](length.md), and $\frac{\mathrm{d}L}{\mathrm{d}T}$ is the change of [length](length.md) $\mathrm{d}L$ per unit change in [temperature](temperature.md) $\mathrm{d}T$}} <!--SR:!2024-11-22,225,290!2026-01-07,513,310-->

### area expansion

> __coefficient of area thermal expansion__
>
> {{$$\begin{aligned} \alpha_A & = \frac1A \frac{\mathrm{d}A}{\mathrm{d}T} \\ \frac{\mathrm{d}A}A & = \alpha_A \,\mathrm{d}T \end{aligned}$$}}
>
> - where
>   - {{$\alpha_A$ is the __coefficient of area thermal expansion__, $A$ is the [area](area.md), and $\frac{\mathrm{d}A}{\mathrm{d}T}$ is the change of [area](area.md) $\mathrm{d}A$ per unit change in [temperature](temperature.md) $\mathrm{d}T$}} <!--SR:!2026-07-27,714,330!2025-08-12,421,310-->

### volume expansion

> __coefficient of volume thermal expansion__
>
> {{$$\begin{aligned} \alpha_V & = \frac1V \frac{\mathrm{d}V}{\mathrm{d}T} \\ \frac{\mathrm{d}V}V & = \alpha_V \,\mathrm{d}T \end{aligned}$$}}
>
> - where
>   - {{$\alpha_V$ is the __coefficient of volume thermal expansion__, $V$ is the [volume](volume.md), and $\frac{\mathrm{d}V}{\mathrm{d}T}$ is the change of [volume](volume.md) $\mathrm{d}V$ per unit change in [temperature](temperature.md) $\mathrm{d}T$}} <!--SR:!2027-10-19,1091,350!2026-11-28,770,330-->

#### isotropic materials

> __relations between coefficients of thermal expansion for isotropic materials__
>
> {{$$\begin{aligned} \alpha_A & = 2\alpha_L \\ \alpha_V & = 3\alpha_L = \frac32 \alpha_A \end{aligned}$$}}
>
> - where
>   - {{$\alpha$ is the coefficient of thermal expansion, with the subscripts $L$, $A$, and $V$ denoting respectively [length](length.md), [area](area.md), and [volume](volume.md)}}
> - conditions: {{isotropic materials}} <!--SR:!2027-09-26,1072,350!2027-07-28,1023,350!2025-02-23,286,290-->

We can derive the above equations for a $n$-dimensional coefficient:

$$\begin{aligned}
\alpha_L & = \frac1L \frac{\mathrm{d}L}{\mathrm{d}T} \\
M_n & = L^n \\
\mathrm{d}M_n & = nL^{n - 1} \mathrm{d}L \\
\alpha_{M_n} & = \frac1{M_n} \frac{\mathrm{d}M_n}{\mathrm{d}T} \\
& = \frac1{L^n} nL^{n - 1} \frac{\mathrm{d}L}{\mathrm{d}T} \\
& = n \frac1L \frac{\mathrm{d}L}{\mathrm{d}T} \\
& = n \alpha_L
\end{aligned}$$

## references

This text incorporates [content](https://en.wikipedia.org/wiki/thermal_expansion) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
