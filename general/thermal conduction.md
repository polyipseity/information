---
aliases:
  - conduction
  - thermal conduction
tags:
  - flashcard/general/thermal_conduction
  - language/in/English
---

# thermal conduction

## Fourier's law

### differential form

> __Fourier's law, differential form__
>
> {{$$\vec\phi_\text{q} = -k \cdot \nabla T$$}}
>
> - where
>   - {{$\vec\phi_\text{q}$ is the [heat flux](heat%20flux.md), in W⋅m<sup>-2</sup>}}
>   - {{$k$ is the [thermal conductivity](thermal%20conductivity%20and%20resistivity.md), in W⋅m<sup>-1</sup>⋅K<sup>-1</sup>}}
>   - {{$\nabla T$ is the [temperature gradient](temperature%20gradient.md), in K⋅m<sup>-1</sup>}} <!--SR:!2024-07-28,152,270!2024-03-29,74,290!2024-10-07,225,330!2024-11-11,252,330-->

For simple applications, Fourier's law is used in its one-dimensional form:

> __Fourier's law, differential form, {{one-dimensional}}__
>
> {{$$\phi_\text{q,x} = -k \frac{\partial T}{\partial x}$$}}
>
> - where
>   - {{$\phi_\text{q,x}$ is the [heat flux](heat%20flux.md) along the $x$-direction, in W⋅m<sup>-2</sup>}}
>   - {{$k$ is the [thermal conductivity](thermal%20conductivity%20and%20resistivity.md), in W⋅m<sup>-1</sup>⋅K<sup>-1</sup>}}
>   - {{$\frac{\partial T}{\partial x}$ is the [temperature gradient](temperature%20gradient.md) along the $x$-direction, in K⋅m<sup>-1</sup>}} <!--SR:!2024-12-09,274,330!2024-07-17,148,310!2024-04-04,69,270!2024-10-17,233,330!2024-10-03,222,330-->

### integral form

> __Fourier's law, integral form__
>
> {{$$\frac{\partial Q}{\partial t} = - \oiint_\mathbf{S}\! k \cdot \nabla T \cdot \mathrm{d}\mathbf{S} $$}}
>
> - where
>   - {{$\frac{\partial Q}{\partial t}$ is the [heat](heat.md) transferred per unit [time](time.md), in W}}
>   - {{$k$ is the [thermal conductivity](thermal%20conductivity%20and%20resistivity.md), in W⋅m<sup>-1</sup>⋅K<sup>-1</sup>}}
>   - {{$\nabla T$ is the [temperature gradient](temperature%20gradient.md), in K⋅m<sup>-1</sup>}}
>   - {{$\mathrm{d}\mathbf{S}$ is a [vector area](vector%20area.md) element, in m<sup>2</sup>}} <!--SR:!2024-05-17,89,250!2024-12-25,286,330!2024-11-20,244,290!2024-07-17,160,310!2024-10-03,221,330-->

For simple applications where the material is [homogeneous](homogeneity%20and%20heterogeneity.md) between two endpoints at constant [temperature](temperature.md), the above can be [integrated](integral.md) to give:

> __Fourier's law, integral form, {{homogeneous material between two endpoints at constant temperature}}__
>
> {{$$\frac{Q}{\Delta t} = -k\frac{\Delta T}{\Delta x}A$$}}
>
> - where
>   - {{$\frac{Q}{\Delta t}$ is the [heat](heat.md) transferred per unit [time](time.md), in W}}
>   - {{$k$ is the [thermal conductivity](thermal%20conductivity%20and%20resistivity.md), in W⋅m<sup>-1</sup>⋅K<sup>-1</sup>}}
>   - {{$\frac{\Delta T}{\Delta x}$ is the [temperature](temperature.md) change per unit distance along the $x$-direction which is perpendicular to the surface, in K⋅m<sup>-1</sup>}}
>   - {{$A$ is the cross-sectional [surface area](surface20area.md), in m<sup>2</sup>}} <!--SR:!2024-12-31,291,330!2024-05-14,101,290!2024-04-26,93,290!2024-11-28,265,330!2024-05-29,112,290!2024-11-01,244,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/thermal_conduction) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
