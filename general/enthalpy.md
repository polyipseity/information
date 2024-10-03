---
aliases:
  - enthalpies
  - enthalpy
tags:
  - flashcard/active/general/enthalpy
  - language/in/English
---

# enthalpy

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

In [chemistry](chemistry.md), the enthalpy of reaction is {{the heat change of reaction under constant [pressure](pressure.md) and [temperature](temperature.md)}}. <!--SR:!2025-12-16,628,270-->

For [endothermic processes](endothermic%20process.md), {{heat is absorbed while for [exothermic processes](exothermic%20process.md), heat is released}}. <!--SR:!2025-04-18,560,310-->

## definition

> __enthalpy of a [thermodynamic system](thermodynamic%20system.md)__
>
> {{$$H = U + pV$$}}
>
> - where
>   - [state variables](state%20variable.md): {{$H$ is the enthalpy, $U$ is the [internal energy](internal%20energy.md), $p$ is the [pressure](pressure.md), and $V$ is the [volume](volume.md)}} <!--SR:!2024-10-26,86,314!2025-06-04,427,374-->

## applications

### enthalpy changes

#### standard conditions

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects('d92a', '9911'),
  (
    '[concentration](concentration.md) (if in a [solution](solution%20(chemistry).md)): 1 mol dm<sup>-3</sup>',
    '[physical states](physical%20state.md): [standard states](standard%20state.md)',
    '[pressure](pressure.md): 1 [atm](atmosphere%20(unit).md)',
    '[temperature](temperature.md): 25 °C/298.15 K',
  ),
)
```

Enthalpy changes are measured under the following {{standard conditions}}: <!--SR:!2028-08-12,1527,350-->

<!--pytextgen generate section="d92a"--><!-- The following content is generated at 2023-04-01T23:56:04.117433+08:00. Any edits will be overridden! -->

> 1. [concentration](concentration.md) (if in a [solution](solution%20(chemistry).md)): 1 mol dm<sup>-3</sup>
> 2. [physical states](physical%20state.md): [standard states](standard%20state.md)
> 3. [pressure](pressure.md): 1 [atm](atmosphere%20(unit).md)
> 4. [temperature](temperature.md): 25 °C/298.15 K

<!--/pytextgen-->

<!--pytextgen generate section="9911"--><!-- The following content is generated at 2024-01-04T20:17:51.631097+08:00. Any edits will be overridden! -->

- _(begin)_→:::←[concentration](concentration.md) (if in a [solution](solution%20(chemistry).md)): 1 mol dm<sup>-3</sup> <!--SR:!2024-10-13,229,278!2028-11-01,1600,358-->
- [concentration](concentration.md) (if in a [solution](solution%20(chemistry).md)): 1 mol dm<sup>-3</sup>→:::←[physical states](physical%20state.md): [standard states](standard%20state.md) <!--SR:!2027-06-24,1111,330!2024-11-19,166,310-->
- [physical states](physical%20state.md): [standard states](standard%20state.md)→:::←[pressure](pressure.md): 1 [atm](atmosphere%20(unit).md) <!--SR:!2026-03-14,746,318!2025-02-12,467,298-->
- [pressure](pressure.md): 1 [atm](atmosphere%20(unit).md)→:::←[temperature](temperature.md): 25 °C/298.15 K <!--SR:!2025-10-10,676,310!2024-11-06,315,290-->
- [temperature](temperature.md): 25 °C/298.15 K→:::←_(end)_ <!--SR:!2027-08-25,1165,338!2026-04-23,567,258-->

<!--/pytextgen-->

#### chemical properties

```Python
# pytextgen generate data
return await memorize_map(
  __env__.cwf_sects('1294', 'abba', '9687'),
  {
    '[enthalpy of combustion](standard%20enthalpy%20of%20combustion.md)': 'enthalpy change of complete [combustion](combustion.md) of a [mole](mole%20(unit).md) of a [substance](chemical%20substance.md)',
    '[enthalpy of formation](standard%20enthalpy%20of%20formation.md)': 'enthalpy change of formation of a [mole](mole%20(unit).md) of a [compound](chemical%20compound.md) from its constituent [elements](chemical%20element.md) in their reference states',
    '[enthalpy of neutralization](standard%20enthalpy%20of%20neutralization.md)': 'enthalpy change of [neutralization](neutralization%20(chemistry).md) with the formation of a [mole](mole%20(unit).md) of [water](water.md)',
  },
)
```

For [chemical properties](chemical%20property.md):

<!--pytextgen generate section="1294"--><!-- The following content is generated at 2023-04-02T00:13:11.400053+08:00. Any edits will be overridden! -->

> 1. [enthalpy of combustion](standard%20enthalpy%20of%20combustion.md): enthalpy change of complete [combustion](combustion.md) of a [mole](mole%20(unit).md) of a [substance](chemical%20substance.md)
> 2. [enthalpy of formation](standard%20enthalpy%20of%20formation.md): enthalpy change of formation of a [mole](mole%20(unit).md) of a [compound](chemical%20compound.md) from its constituent [elements](chemical%20element.md) in their reference states
> 3. [enthalpy of neutralization](standard%20enthalpy%20of%20neutralization.md): enthalpy change of [neutralization](neutralization%20(chemistry).md) with the formation of a [mole](mole%20(unit).md) of [water](water.md)

<!--/pytextgen-->

<!--pytextgen generate section="abba"--><!-- The following content is generated at 2024-01-04T20:17:51.719624+08:00. Any edits will be overridden! -->

- [enthalpy of combustion](standard%20enthalpy%20of%20combustion.md)::enthalpy change of complete [combustion](combustion.md) of a [mole](mole%20(unit).md) of a [substance](chemical%20substance.md) <!--SR:!2025-08-03,628,310-->
- [enthalpy of formation](standard%20enthalpy%20of%20formation.md)::enthalpy change of formation of a [mole](mole%20(unit).md) of a [compound](chemical%20compound.md) from its constituent [elements](chemical%20element.md) in their reference states <!--SR:!2025-03-26,480,290-->
- [enthalpy of neutralization](standard%20enthalpy%20of%20neutralization.md)::enthalpy change of [neutralization](neutralization%20(chemistry).md) with the formation of a [mole](mole%20(unit).md) of [water](water.md) <!--SR:!2026-01-19,724,318-->

<!--/pytextgen-->

<!--pytextgen generate section="9687"--><!-- The following content is generated at 2024-01-04T20:17:51.682615+08:00. Any edits will be overridden! -->

- enthalpy change of complete [combustion](combustion.md) of a [mole](mole%20(unit).md) of a [substance](chemical%20substance.md)::[enthalpy of combustion](standard%20enthalpy%20of%20combustion.md) <!--SR:!2028-10-28,1597,358-->
- enthalpy change of formation of a [mole](mole%20(unit).md) of a [compound](chemical%20compound.md) from its constituent [elements](chemical%20element.md) in their reference states::[enthalpy of formation](standard%20enthalpy%20of%20formation.md) <!--SR:!2028-11-12,1609,358-->
- enthalpy change of [neutralization](neutralization%20(chemistry).md) with the formation of a [mole](mole%20(unit).md) of [water](water.md)::[enthalpy of neutralization](standard%20enthalpy%20of%20neutralization.md) <!--SR:!2028-10-21,1591,358-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/enthalpy) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
