---
aliases:
  - entropies
  - entropy
tags:
  - flashcards/general/entropy
---

# entropy

## definitions and descriptions

There are two main ways to describe entropy: {{the macroscopic description from [classical thermodynamics](thermodynamics.md#classical%20thermodynamics) and the microscopic description from [statistical mechanics](statistical%20mechanics.md). The former one defines entropy based on macroscopic measurable variables like [pressure](pressure.md), [temperature](temperature.md), total [mass](mass.md), and [volume](volume.md), while the latter defines entropy based on statistics of motions of microscopic constituents in a [system](thermodynamic%20system.md)}}. Both definitions are {{consistent with each other}}. <!--SR:!2023-12-17,3,250!2023-12-18,4,270-->

> [!tip]
>
> - physical analogy: {{There is no easy physical analogy for entropy. The best analogy one can make is that entropy is a [state variable](state%20variable.md) of a [thermodynamic equilibrium](thermodynamic%20equilibrium.md), similar to [internal energy](internal%20energy.md), [pressure](pressure.md), [temperature](temperature.md), [volume](volume.md), etc.}}
> - understand entropy in [classical thermodynamics](classical%20thermodynamics.md) using the [Carnot cycle](Carnot%20cycle.md):
>     1. {{Let's imagine you have two infinite heat reservoirs, one of higher [temperature](temperature.md) $T_\mathrm{H}$ and one of lower [temperature](temperature.md) $T_\mathrm{C}$. Your goal is to create a heat engine that maximizes efficiency, i.e. max work per heat accepted}}.
>     2. {{Intuitively, heat moves from higher [temperature](temperature.md) to lower [temperature](temperature.md) and not in reverse, so the max amount of work we can extract is the energy difference between the two [temperatures](temperatures.md)}}.
>     3. {{Another requirement is that we want to run the heat engine indefinitely, so we need the heat engine to return to its starting state}}.
>     4. {{Starting from a gas of [temperature](temperature.md) $T_\mathrm{H}$ and [volume](volume.md) $V_0$, we start accepting heat from the hot reservoir, called $Q_\mathrm{H}$. To maximize work done, all accepted heat performs work and does not heat up the gas. The [temperature](temperature.md) remains $T_\mathrm{H}$, but the [volume](volume.md) increases. Remember $\delta W = \delta Q_\mathrm{H}$.}}
>     5. {{Then we need to change the gas temperature from $T_\mathrm{H}$ to $T_\mathrm{C}$, as a cooler gas consumes less work to be compressed. To maximize work, all the lost internal energy are converted to work. Remember $\delta W = \mathrm{d}U$.}}
>     6. {{Now we need to start compressing the gas back to its starting state. That means we need to decrease the [volume](volume.md) and increase the [temperature](temperature.md). Compressing the gas at $T_\mathrm{C}$ takes less work, so we will use work to compress the gas while keeping its [temperature](temperature.md) at $T_\mathrm{C}$. That requires dissipating the work into the cold reservoir to avoid the temperature increase, which we call $Q_\mathrm{C}$. Remember $\delta W = -\delta Q_\mathrm{C}$.}}
>     7. {{We also need to increase the [temperature](temperature.md) to $T_\mathrm{H}$ to return the gas to its starting state. To do so, instead of compressing the gas to $V_0$ while keeping the [temperature](temperature.md) at $T_\mathrm{C}$, we will use the work that would have been dissipated as $Q_\mathrm{C}$ to increase the [internal energy](internal%20energy.md) of the gas, and thus [temperature](temperature.md). Remember $\delta W = -\mathrm{d}U$.}}
>     8. {{Obviously, step 5 and step 7 cancels out as the [internal energy](internal%20energy.md) of the gas returns to its original state: $\delta W = \mathrm{d}U - \mathrm{d}U = 0$. That means the only work produced comes from step 4 and 6, which is the difference between $Q_\mathrm{H}$ and $Q_\mathrm{C}$: $\delta W = \delta Q_\mathrm{H} - \delta Q_\mathrm{C}$.}}
>     9. {{To understand entropy, consider the [heat](heat.md) ratio $Q_\mathrm{H} / Q_\mathrm{C}$. As $Q_\mathrm{H}$ increases, more [volume](volume.md) is displaced, so more $Q_\mathrm{C}$ is needed to restore the [volume](volume.md). Heuristically, that means the ratio is only affected by the [temperature](temperature.md) ratio $T_\mathrm{H}/T_\mathrm{C}$ but not the [volume](volume.md). So we can think of [temperature](temperature.md) as characterizing the amount of [heat](heat.md) converted to [work](work%20(physics).md) per [volume](volume.md). Then the inverse [temperature](temperature.md) $1/T$ characterizes the amount of [volume](volume.md) displaced per [heat](heat.md) converted to [work](work%20(physics).md), or in other words, how easy it is to displace [volume](volume.md). Compare it with $\mathrm{d}S = \frac{\delta Q_\text{in} }T$.}} <!--SR:!2023-12-18,4,270!2023-12-18,4,270!2023-12-17,3,250!2023-12-17,3,250!2023-12-18,4,270!2023-12-18,4,270!2023-12-17,3,250!2023-12-18,4,270!2023-12-18,4,270!2023-12-17,3,250-->

### classical thermodynamics

> __entropy change__
>
> {{$$\mathrm{d}S = \frac{\delta Q_\text{in} }T$$}}
>
> - where
>     - {{$\mathrm{d}S$ is the infinitesimal entropy change due to the infinitesimal received [heat](heat.md) $\delta Q_\text{in}$ ([inexact differential](inexact%20differential.md)) at instantaneous [temperature](temperature.md) $T$}} <!--SR:!2023-12-17,3,250!2023-12-17,3,250-->
