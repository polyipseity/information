---
aliases:
  - enthalpies
  - enthalpy
tags:
  - flashcards/general/enthalpy
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# enthalpy

In [chemistry](chemistry.md), the enthalpy of reaction is {{the heat change of reaction under constant [pressure](pressure.md) and [temperature](temperature.md)}}. <!--SR:!2024-03-27,233,270-->

For [endothermic processes](endothermic%20process.md), {{heat is absorbed while for [exothermic processes](exothermic%20process.md), heat is released}}. <!--SR:!2025-04-18,560,310-->

## applications

### enthalpy changes

#### standard conditions

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_seq(
  e.cwf_sects('d92a', '9911'),
  (
    '[concentration](concentration.md) (if in a [solution](solution%20(chemistry).md)): 1 mol dm<sup>-3</sup>',
    '[physical states](physical%20state.md): [standard states](standard%20state.md)',
    '[pressure](pressure.md): 1 [atm](atmosphere%20(unit).md)',
    '[temperature](temperature.md): 25 °C/298.15 K',
  ),
)
```
%%

Enthalpy changes are measured under the following {{standard conditions}}: <!--SR:!2024-06-07,336,330-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d92a"--><!-- The following content is generated at 2023-04-01T23:56:04.117433+08:00. Any edits will be overridden! -->

> 1. [concentration](concentration.md) (if in a [solution](solution%20(chemistry).md)): 1 mol dm<sup>-3</sup>
> 2. [physical states](physical%20state.md): [standard states](standard%20state.md)
> 3. [pressure](pressure.md): 1 [atm](atmosphere%20(unit).md)
> 4. [temperature](temperature.md): 25 °C/298.15 K

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9911"--><!-- The following content is generated at 2023-04-01T23:56:04.104463+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[concentration](concentration.md) (if in a [solution](solution%20(chemistry).md)): 1 mol dm<sup>-3</sup> <!--SR:!2023-12-05,169,298!2024-06-15,344,338-->
2. [concentration](concentration.md) (if in a [solution](solution%20(chemistry).md)): 1 mol dm<sup>-3</sup>→:::←[physical states](physical%20state.md): [standard states](standard%20state.md) <!--SR:!2024-06-08,337,330!2024-06-06,335,330-->
3. [physical states](physical%20state.md): [standard states](standard%20state.md)→:::←[pressure](pressure.md): 1 [atm](atmosphere%20(unit).md) <!--SR:!2024-02-27,235,318!2025-02-12,467,298-->
4. [pressure](pressure.md): 1 [atm](atmosphere%20(unit).md)→:::←[temperature](temperature.md): 25 °C/298.15 K <!--SR:!2023-12-04,168,290!2023-12-27,109,290-->
5. [temperature](temperature.md): 25 °C/298.15 K→:::←_(end)_ <!--SR:!2024-06-16,345,338!2023-11-20,58,258-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### chemical properties

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_map(
  e.cwf_sects('1294', 'abba', '9687'),
  {
    '[enthalpy of combustion](standard%20enthalpy%20of%20combustion.md)': 'enthalpy change of complete [combustion](combustion.md) of a [mole](mole%20(unit).md) of a [substance](chemical%20substance.md)',
    '[enthalpy of formation](standard%20enthalpy%20of%20formation.md)': 'enthalpy change of formation of a [mole](mole%20(unit).md) of a [compound](chemical%20compound.md) from its constituent [elements](chemical%20element.md) in their reference states',
    '[enthalpy of neutralization](standard%20enthalpy%20of%20neutralization.md)': 'enthalpy change of [neutralization](neutralization%20(chemistry).md) with the formation of a [mole](mole%20(unit).md) of [water](water.md)',
  },
)
```
%%

For [chemical properties](chemical%20property.md):

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1294"--><!-- The following content is generated at 2023-04-02T00:13:11.400053+08:00. Any edits will be overridden! -->

> 1. [enthalpy of combustion](standard%20enthalpy%20of%20combustion.md): enthalpy change of complete [combustion](combustion.md) of a [mole](mole%20(unit).md) of a [substance](chemical%20substance.md)
> 2. [enthalpy of formation](standard%20enthalpy%20of%20formation.md): enthalpy change of formation of a [mole](mole%20(unit).md) of a [compound](chemical%20compound.md) from its constituent [elements](chemical%20element.md) in their reference states
> 3. [enthalpy of neutralization](standard%20enthalpy%20of%20neutralization.md): enthalpy change of [neutralization](neutralization%20(chemistry).md) with the formation of a [mole](mole%20(unit).md) of [water](water.md)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="abba"--><!-- The following content is generated at 2023-04-02T00:13:11.432967+08:00. Any edits will be overridden! -->

1. [enthalpy of combustion](standard%20enthalpy%20of%20combustion.md)::enthalpy change of complete [combustion](combustion.md) of a [mole](mole%20(unit).md) of a [substance](chemical%20substance.md) <!--SR:!2025-08-03,628,310-->
2. [enthalpy of formation](standard%20enthalpy%20of%20formation.md)::enthalpy change of formation of a [mole](mole%20(unit).md) of a [compound](chemical%20compound.md) from its constituent [elements](chemical%20element.md) in their reference states <!--SR:!2023-12-02,166,290-->
3. [enthalpy of neutralization](standard%20enthalpy%20of%20neutralization.md)::enthalpy change of [neutralization](neutralization%20(chemistry).md) with the formation of a [mole](mole%20(unit).md) of [water](water.md) <!--SR:!2024-01-26,228,318-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9687"--><!-- The following content is generated at 2023-04-02T00:13:11.416008+08:00. Any edits will be overridden! -->

1. enthalpy change of complete [combustion](combustion.md) of a [mole](mole%20(unit).md) of a [substance](chemical%20substance.md)::[enthalpy of combustion](standard%20enthalpy%20of%20combustion.md) <!--SR:!2024-06-14,343,338-->
2. enthalpy change of formation of a [mole](mole%20(unit).md) of a [compound](chemical%20compound.md) from its constituent [elements](chemical%20element.md) in their reference states::[enthalpy of formation](standard%20enthalpy%20of%20formation.md) <!--SR:!2024-06-17,346,338-->
3. enthalpy change of [neutralization](neutralization%20(chemistry).md) with the formation of a [mole](mole%20(unit).md) of [water](water.md)::[enthalpy of neutralization](standard%20enthalpy%20of%20neutralization.md) <!--SR:!2024-06-13,342,338-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

#### physical properties

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_map(
  e.cwf_sects('bb12', '2440', '69ff'),
  {
  },
)
```
%%

For [physical properties](physical%20property.md):

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="bb12"--><!-- The following content is generated at 2023-04-02T00:06:47.143099+08:00. Any edits will be overridden! -->

>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2440"--><!-- The following content is generated at 2023-04-02T00:06:47.124597+08:00. Any edits will be overridden! -->



<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="69ff"--><!-- The following content is generated at 2023-04-02T00:06:47.106642+08:00. Any edits will be overridden! -->



<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
