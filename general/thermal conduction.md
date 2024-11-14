---
aliases:
  - conduction
  - thermal conduction
tags:
  - flashcard/active/general/thermal_conduction
  - language/in/English
---

# thermal conduction

## Fourier's law

### differential form

> __Fourier's law, differential form__
>
> {@{$$\vec\phi_\text{q} = -k \cdot \nabla T$$}@}
>
> - where
>   - {@{$\vec\phi_\text{q}$ is the [heat flux](heat%20flux.md), in W⋅m<sup>-2</sup>}@}
>   - {@{$k$ is the [thermal conductivity](thermal%20conductivity%20and%20resistivity.md), in W⋅m<sup>-1</sup>⋅K<sup>-1</sup>}@}
>   - {@{$\nabla T$ is the [temperature gradient](temperature%20gradient.md), in K⋅m<sup>-1</sup>}@}

For simple applications, Fourier's law is used in its one-dimensional form:

> __Fourier's law, differential form, {@{one-dimensional}@}__
>
> {@{$$\phi_\text{q,x} = -k \frac{\partial T}{\partial x}$$}@}
>
> - where
>   - {@{$\phi_\text{q,x}$ is the [heat flux](heat%20flux.md) along the $x$-direction, in W⋅m<sup>-2</sup>}@}
>   - {@{$k$ is the [thermal conductivity](thermal%20conductivity%20and%20resistivity.md), in W⋅m<sup>-1</sup>⋅K<sup>-1</sup>}@}
>   - {@{$\frac{\partial T}{\partial x}$ is the [temperature gradient](temperature%20gradient.md) along the $x$-direction, in K⋅m<sup>-1</sup>}@}

### integral form

> __Fourier's law, integral form__
>
> {@{$$\frac{\partial Q}{\partial t} = - \oiint_\mathbf{S}\! k \cdot \nabla T \cdot \mathrm{d}\mathbf{S} $$}@}
>
> - where
>   - {@{$\frac{\partial Q}{\partial t}$ is the [heat](heat.md) transferred per unit [time](time.md), in W}@}
>   - {@{$k$ is the [thermal conductivity](thermal%20conductivity%20and%20resistivity.md), in W⋅m<sup>-1</sup>⋅K<sup>-1</sup>}@}
>   - {@{$\nabla T$ is the [temperature gradient](temperature%20gradient.md), in K⋅m<sup>-1</sup>}@}
>   - {@{$\mathrm{d}\mathbf{S}$ is a [vector area](vector%20area.md) element, in m<sup>2</sup>}@}

For simple applications where the material is [homogeneous](homogeneity%20and%20heterogeneity.md) between two endpoints at constant [temperature](temperature.md), the above can be [integrated](integral.md) to give:

> __Fourier's law, integral form, {@{homogeneous material between two endpoints at constant temperature}@}__
>
> {@{$$\frac{Q}{\Delta t} = -k\frac{\Delta T}{\Delta x}A$$}@}
>
> - where
>   - {@{$\frac{Q}{\Delta t}$ is the [heat](heat.md) transferred per unit [time](time.md), in W}@}
>   - {@{$k$ is the [thermal conductivity](thermal%20conductivity%20and%20resistivity.md), in W⋅m<sup>-1</sup>⋅K<sup>-1</sup>}@}
>   - {@{$\frac{\Delta T}{\Delta x}$ is the [temperature](temperature.md) change per unit distance along the $x$-direction which is perpendicular to the surface, in K⋅m<sup>-1</sup>}@}
>   - {@{$A$ is the cross-sectional [surface area](surface20area.md), in m<sup>2</sup>}@}

## references

This text incorporates [content](https://en.wikipedia.org/wiki/thermal_conduction) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
