---
aliases:
  - conduction
  - thermal conduction
tags:
  - flashcard/active/general/eng/thermal_conduction
  - language/in/English
---

# thermal conduction

## Fourier's law

### differential form

> __Fourier's law, differential form__
>
> {@{$$\vec\phi_\text{q} = -k \cdot \nabla T$$}@}
>
> where
>
> - {@{$\vec\phi_\text{q}$}@} is {@{the [heat flux](heat%20flux.md), in W⋅m<sup>-2</sup>}@}
> - {@{$k$}@} is {@{the [thermal conductivity](thermal%20conductivity%20and%20resistivity.md), in W⋅m<sup>-1</sup>⋅K<sup>-1</sup>}@}
> - {@{$\nabla T$}@} is {@{the [temperature gradient](temperature%20gradient.md), in K⋅m<sup>-1</sup>}@} <!--SR:!2029-11-29,1541,290!2027-03-13,863,310!2027-07-28,1023,350!2027-02-22,833,330!2026-03-12,92,361!2027-05-19,438,381!2027-05-25,443,381-->

For simple applications, Fourier's law is used in its one-dimensional form:

> __Fourier's law, differential form, {@{one-dimensional}@}__
>
> {@{$$\phi_\text{q,x} = -k \frac{\partial T}{\partial x}$$}@}
>
> where
>
> - {@{$\phi_\text{q,x}$}@} is {@{the [heat flux](heat%20flux.md) along the $x$-direction, in W⋅m<sup>-2</sup>}@}
> - {@{$k$}@} is {@{the [thermal conductivity](thermal%20conductivity%20and%20resistivity.md), in W⋅m<sup>-1</sup>⋅K<sup>-1</sup>}@}
> - {@{$\frac{\partial T}{\partial x}$}@} is {@{the [temperature gradient](temperature%20gradient.md) along the $x$-direction, in K⋅m<sup>-1</sup>}@} <!--SR:!2028-05-11,1249,350!2029-09-08,1420,310!2026-09-04,696,290!2027-09-11,1059,350!2026-10-07,734,330!2026-03-10,90,361!2026-03-10,90,361!2026-03-09,89,361-->

### integral form

> __Fourier's law, integral form__
>
> {@{$$\frac{\partial Q}{\partial t} = -k \oiint_\mathbf{S}\! \nabla T \cdot \mathrm{d}\mathbf{S}$$}@}
>
> where
>
> - {@{$\frac{\partial Q}{\partial t}$}@} is {@{the [heat](heat.md) transferred per unit [time](time.md), in W}@}
> - {@{$k$}@} is {@{the [thermal conductivity](thermal%20conductivity%20and%20resistivity.md), in W⋅m<sup>-1</sup>⋅K<sup>-1</sup>}@}
> - {@{$\nabla T$}@} is {@{the [temperature gradient](temperature%20gradient.md), in K⋅m<sup>-1</sup>}@}
> - {@{$\mathrm{d}\mathbf{S}$}@} is {@{a [vector area](vector%20area.md) element, in m<sup>2</sup>}@} <!--SR:!2026-07-04,554,250!2028-07-24,1307,350!2027-08-03,986,310!2031-09-18,2123,330!2026-10-01,728,330!2026-03-11,91,361!2027-05-19,438,381!2027-05-15,435,381!2026-12-10,305,361-->

For simple applications where the material is [homogeneous](homogeneity%20and%20heterogeneity.md) between two endpoints at constant [temperature](temperature.md), the above can be [integrated](integral.md) to give:

> __Fourier's law, integral form, {@{homogeneous material between two endpoints at constant temperature}@}__
>
> {@{$$\frac{Q}{\Delta t} = -k\frac{\Delta T}{\Delta x}A$$}@}
>
> where
>
> - {@{$\frac{Q}{\Delta t}$}@} is {@{the [heat](heat.md) transferred per unit [time](time.md), in W}@}
> - {@{$k$}@} is {@{the [thermal conductivity](thermal%20conductivity%20and%20resistivity.md), in W⋅m<sup>-1</sup>⋅K<sup>-1</sup>}@}
> - {@{$\frac{\Delta T}{\Delta x}$}@} is {@{the [temperature](temperature.md) change per unit distance along the $x$-direction which is perpendicular to the surface, in K⋅m<sup>-1</sup>}@}
> - {@{$A$}@} is {@{the cross-sectional [surface area](surface20area.md), in m<sup>2</sup>}@} <!--SR:!2027-08-25,967,330!2027-06-27,846,290!2027-03-12,780,290!2028-03-18,1206,350!2030-12-15,1939,330!2027-11-18,1112,350!2027-05-20,438,381!2026-03-09,89,361!2026-03-12,92,361!2026-03-11,91,361-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/thermal_conduction) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
