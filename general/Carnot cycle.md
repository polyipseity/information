---
aliases:
  - Carnot cycle
  - Carnot cycles
tags:
  - flashcards/general/Carnot_cycle
  - languages/in/English
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# Carnot cycle

The Carnot cycle provides {{the upper limit of [efficiency](thermal%20efficiency.md) of any [heat engine](heat%20engine.md) in converting [heat](heat.md) into [work](work%20(physics).md) by [Carnot's theorem](Carnot's%20theorem%20(thermodynamics).md)}}. <!--SR:!2024-02-19,50,310-->

## stages

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_seq(
  e.cwf_sects("bb11", "2944",),
  (
    R"__[reversible](reversible%20process%20(thermodynamics).md) [isothermal](isothermal%20process.md) expansion__: $Q_\mathrm{H}$ is transferred from the hot reservoir to the gas, performing the same amount of [work](work%20(physics).md); [temperature](temperature.md) is $T_\mathrm{H}$ and remains constant; [entropy](entropy.md) increases by $\Delta S = Q_\mathrm{H} / T_\mathrm{H}$",
    R"__[isentropic](isentropic%20process.md) expansion__: [temperature](temperature.md) decreases from $T_\mathrm{H}$ to $T_\mathrm{C}$, performing [work](work%20(physics).md); [entropy](entropy.md) remains constant",
    R"__[reversible](reversible%20process%20(thermodynamics).md) [isothermal](isothermal%20process.md) compression__: $Q_\mathrm{C}$ is transferred from the gas to the cold reservoir, receiving the same amount of [work](work%20(physics).md); [temperature](temperature.md) is $T_\mathrm{C}$ and remains constant; [entropy](entropy.md) decreases by $\Delta S = Q_\mathrm{C} / T_\mathrm{C}$",
    R"__[isentropic](isentropic%20process.md) compression__: [temperature](temperature.md) increases from $T_\mathrm{C}$ to $T_\mathrm{H}$, receiving [work](work%20(physics).md); [entropy](entropy.md) remains constant",
  ),
  pretext="starts at top left in the [PV diagram](pressure–volume%20diagram.md)",
  posttext="ends at top left in the [PV diagram](pressure–volume%20diagram.md)",
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="bb11"--><!-- The following content is generated at 2023-12-14T18:09:39.353040+08:00. Any edits will be overridden! -->

> 1. __[reversible](reversible%20process%20(thermodynamics).md) [isothermal](isothermal%20process.md) expansion__: $Q_\mathrm{H}$ is transferred from the hot reservoir to the gas, performing the same amount of [work](work%20(physics).md); [temperature](temperature.md) is $T_\mathrm{H}$ and remains constant; [entropy](entropy.md) increases by $\Delta S = Q_\mathrm{H} / T_\mathrm{H}$
> 2. __[isentropic](isentropic%20process.md) expansion__: [temperature](temperature.md) decreases from $T_\mathrm{H}$ to $T_\mathrm{C}$, performing [work](work%20(physics).md); [entropy](entropy.md) remains constant
> 3. __[reversible](reversible%20process%20(thermodynamics).md) [isothermal](isothermal%20process.md) compression__: $Q_\mathrm{C}$ is transferred from the gas to the cold reservoir, receiving the same amount of [work](work%20(physics).md); [temperature](temperature.md) is $T_\mathrm{C}$ and remains constant; [entropy](entropy.md) decreases by $\Delta S = Q_\mathrm{C} / T_\mathrm{C}$
> 4. __[isentropic](isentropic%20process.md) compression__: [temperature](temperature.md) increases from $T_\mathrm{C}$ to $T_\mathrm{H}$, receiving [work](work%20(physics).md); [entropy](entropy.md) remains constant

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2944"--><!-- The following content is generated at 2023-12-31T18:27:53.481443+08:00. Any edits will be overridden! -->

1. _(starts at top left in the [PV diagram](pressure–volume%20diagram.md))_→:::←__[reversible](reversible%20process%20(thermodynamics).md) [isothermal](isothermal%20process.md) expansion__: $Q_\mathrm{H}$ is transferred from the hot reservoir to the gas, performing the same amount of [work](work%20(physics).md); [temperature](temperature.md) is $T_\mathrm{H}$ and remains constant; [entropy](entropy.md) increases by $\Delta S = Q_\mathrm{H} / T_\mathrm{H}$ <!--SR:!2024-02-07,40,290!2024-02-20,51,310-->
2. __[reversible](reversible%20process%20(thermodynamics).md) [isothermal](isothermal%20process.md) expansion__: $Q_\mathrm{H}$ is transferred from the hot reservoir to the gas, performing the same amount of [work](work%20(physics).md); [temperature](temperature.md) is $T_\mathrm{H}$ and remains constant; [entropy](entropy.md) increases by $\Delta S = Q_\mathrm{H} / T_\mathrm{H}$→:::←__[isentropic](isentropic%20process.md) expansion__: [temperature](temperature.md) decreases from $T_\mathrm{H}$ to $T_\mathrm{C}$, performing [work](work%20(physics).md); [entropy](entropy.md) remains constant <!--SR:!2024-03-04,62,310!2024-02-11,44,290-->
3. __[isentropic](isentropic%20process.md) expansion__: [temperature](temperature.md) decreases from $T_\mathrm{H}$ to $T_\mathrm{C}$, performing [work](work%20(physics).md); [entropy](entropy.md) remains constant→:::←__[reversible](reversible%20process%20(thermodynamics).md) [isothermal](isothermal%20process.md) compression__: $Q_\mathrm{C}$ is transferred from the gas to the cold reservoir, receiving the same amount of [work](work%20(physics).md); [temperature](temperature.md) is $T_\mathrm{C}$ and remains constant; [entropy](entropy.md) decreases by $\Delta S = Q_\mathrm{C} / T_\mathrm{C}$ <!--SR:!2024-01-20,27,270!2024-01-17,24,270-->
4. __[reversible](reversible%20process%20(thermodynamics).md) [isothermal](isothermal%20process.md) compression__: $Q_\mathrm{C}$ is transferred from the gas to the cold reservoir, receiving the same amount of [work](work%20(physics).md); [temperature](temperature.md) is $T_\mathrm{C}$ and remains constant; [entropy](entropy.md) decreases by $\Delta S = Q_\mathrm{C} / T_\mathrm{C}$→:::←__[isentropic](isentropic%20process.md) compression__: [temperature](temperature.md) increases from $T_\mathrm{C}$ to $T_\mathrm{H}$, receiving [work](work%20(physics).md); [entropy](entropy.md) remains constant <!--SR:!2024-03-03,61,310!2024-01-28,24,270-->
5. __[isentropic](isentropic%20process.md) compression__: [temperature](temperature.md) increases from $T_\mathrm{C}$ to $T_\mathrm{H}$, receiving [work](work%20(physics).md); [entropy](entropy.md) remains constant→:::←_(ends at top left in the [PV diagram](pressure–volume%20diagram.md))_ <!--SR:!2024-02-28,57,310!2024-02-06,39,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

> [!tip] tip
>
> - [intuition](intuition.md):
>     1. {{Let's imagine you have two infinite heat reservoirs, one of higher [temperature](temperature.md) $T_\mathrm{H}$ and one of lower [temperature](temperature.md) $T_\mathrm{C}$. Your goal is to create a heat engine that maximizes efficiency, i.e. max work per heat accepted}}.
>     2. {{Intuitively, heat moves from higher [temperature](temperature.md) to lower [temperature](temperature.md) and not in reverse, so the max amount of work we can extract is the energy difference between the two [temperatures](temperatures.md)}}.
>     3. {{Another requirement is that we want to run the heat engine indefinitely, so we need the heat engine to return to its starting state}}.
>     4. {{Starting from a gas of [temperature](temperature.md) $T_\mathrm{H}$ and [volume](volume.md) $V_0$, we start accepting heat from the hot reservoir, called $Q_\mathrm{H}$. To maximize work done, all accepted heat performs work and does not heat up the gas. The [temperature](temperature.md) remains $T_\mathrm{H}$, but the [volume](volume.md) increases. Remember $\delta W = \delta Q_\mathrm{H}$.}}
>     5. {{Then we need to change the gas temperature from $T_\mathrm{H}$ to $T_\mathrm{C}$, as a cooler gas consumes less work to be compressed. To maximize work, all the lost internal energy are converted to work. Remember $\delta W = \mathrm{d}U$.}}
>     6. {{Now we need to start compressing the gas back to its starting state. That means we need to decrease the [volume](volume.md) and increase the [temperature](temperature.md). Compressing the gas at $T_\mathrm{C}$ takes less work, so we will use work to compress the gas while keeping its [temperature](temperature.md) at $T_\mathrm{C}$. That requires dissipating the work into the cold reservoir to avoid the temperature increase, which we call $Q_\mathrm{C}$. Remember $\delta W = -\delta Q_\mathrm{C}$.}}
>     7. {{We also need to increase the [temperature](temperature.md) to $T_\mathrm{H}$ to return the gas to its starting state. To do so, instead of compressing the gas to $V_0$ while keeping the [temperature](temperature.md) at $T_\mathrm{C}$, we will use the work that would have been dissipated as $Q_\mathrm{C}$ to increase the [internal energy](internal%20energy.md) of the gas, and thus [temperature](temperature.md). Remember $\delta W = -\mathrm{d}U$.}}
>     8. {{Obviously, step 5 and step 7 cancels out as the [internal energy](internal%20energy.md) of the gas returns to its original state: $\delta W = \mathrm{d}U - \mathrm{d}U = 0$. That means the only work produced comes from step 4 and 6, which is the difference between $Q_\mathrm{H}$ and $Q_\mathrm{C}$: $\delta W = \delta Q_\mathrm{H} - \delta Q_\mathrm{C}$.}}
>     9. {{To understand entropy, consider the [heat](heat.md) ratio $Q_\mathrm{H} / Q_\mathrm{C}$. As $Q_\mathrm{H}$ increases, more [volume](volume.md) is displaced, so more $Q_\mathrm{C}$ is needed to restore the [volume](volume.md). Heuristically, that means the ratio is only affected by the [temperature](temperature.md) ratio $T_\mathrm{H}/T_\mathrm{C}$ but not the [volume](volume.md). So we can think of [temperature](temperature.md) as characterizing the amount of [heat](heat.md) converted to [work](work%20(physics).md) per [volume](volume.md). Then the inverse [temperature](temperature.md) $1/T$ characterizes the amount of [volume](volume.md) displaced per [heat](heat.md) converted to [work](work%20(physics).md), or in other words, how easy it is to displace [volume](volume.md). Compare it with $\mathrm{d}S = \frac{\delta Q_\text{in} }T$.}} <!--SR:!2024-03-12,68,310!2024-01-21,26,270!2024-02-16,48,290!2024-02-11,40,290!2024-03-06,63,310!2024-01-12,19,250!2024-02-14,43,290!2024-03-05,62,310!2024-01-19,24,250-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Carnot_cycle) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
