---
aliases:
  - Bacon fuel cell
  - alkaline fuel cell
  - alkaline fuel cells
tags:
  - flashcard/active/general/alkaline_fuel_cell
  - language/in/English
---

# alkaline fuel cell

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

The __alkaline fuel cell__ (__AFC__) is {@{a [fuel cell](fuel%20cell.md) that consumes [hydrogen](hydrogen.md) and pure [oxygen](oxygen.md) to produce [water](water.md), [electricity](electricity.md), and [heat](heat.md)}@}. It has an efficiency of {@{70%}@}.

## chemistry

Energy is produced through {@{a [redox reaction](redox%20reaction.md) between [hydrogen](hydrogen.md) and [oxygen](oxygen.md) in hot concentrated [alkaline](alkali.md) [electrolyte](electrolyte.md) such as [potassium hydroxide](potassium%20hydroxide.md) with a temperature in between ambient temperature and 90 °C}@}:

> - [anode](anode.md) ::@:: H<sub>2</sub>(g) + 2OH<sup>-</sup>(aq) → 2H<sub>2</sub>O(l) + 2e<sup>-</sup>
> - [cathode](cathode.md) ::@:: O<sub>2</sub>(g) + 2H<sub>2</sub>O(l) + 4e<sup>-</sup> → 4OH<sup>-</sup>(aq)
> - overall ::@:: 2H<sub>2</sub>(g) + O<sub>2</sub>(g) → 2H<sub>2</sub>O(l)

Electrodes {@{are porous to allow hydrogen, oxygen, and [water](water.md) to flow in and out. They are made of [nickel](nickel.md) or [platinum](platinum.md) to catalyze the redox reaction}@}.

Pure oxygen is needed {@{to avoid poisoning the fuel cell by converting potassium hydroxide into [potassium carbonate](potassium%20carbonate.md)}@}.

## advantages and disadvantages

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects('d929', 'afb9'),
  (
    '+: efficiency as high as 70%',
    '+: operate continuously, producing a stable supply of [electricity](electricity.md)',
    '+: products, which consist of [water](water.md), are clean',
    '-: expensive',
    '-: storage of [hydrogen](hydrogen.md) and [oxygen](oxygen.md) gas is difficult',
  ),
)
```

<!--pytextgen generate section="d929"--><!-- The following content is generated at 2023-04-01T12:33:20.447271+08:00. Any edits will be overridden! -->

> 1. +: efficiency as high as 70%
> 2. +: operate continuously, producing a stable supply of [electricity](electricity.md)
> 3. +: products, which consist of [water](water.md), are clean
> 4. -: expensive
> 5. -: storage of [hydrogen](hydrogen.md) and [oxygen](oxygen.md) gas is difficult

<!--/pytextgen-->

<!--pytextgen generate section="afb9"--><!-- The following content is generated at 2024-01-04T20:17:51.172248+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←+: efficiency as high as 70%
- +: efficiency as high as 70%→::@::←+: operate continuously, producing a stable supply of [electricity](electricity.md)
- +: operate continuously, producing a stable supply of [electricity](electricity.md)→::@::←+: products, which consist of [water](water.md), are clean
- +: products, which consist of [water](water.md), are clean→::@::←-: expensive
- -: expensive→::@::←-: storage of [hydrogen](hydrogen.md) and [oxygen](oxygen.md) gas is difficult
- -: storage of [hydrogen](hydrogen.md) and [oxygen](oxygen.md) gas is difficult→::@::←_(end)_

<!--/pytextgen-->

## uses

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects('2939', '2901'),
  (
    'auxiliary heat and water source',
    'backup power source',
    '[electricity](electricity.md) generation for [electric vehicles](electric%20vehicle.md)',
    'remote power source',
  ),
)
```

<!--pytextgen generate section="2939"--><!-- The following content is generated at 2023-03-31T22:39:40.309569+08:00. Any edits will be overridden! -->

> 1. auxiliary heat and water source
> 2. backup power source
> 3. [electricity](electricity.md) generation for [electric vehicles](electric%20vehicle.md)
> 4. remote power source

<!--/pytextgen-->

<!--pytextgen generate section="2901"--><!-- The following content is generated at 2024-01-04T20:17:51.276821+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←auxiliary heat and water source
- auxiliary heat and water source→::@::←backup power source
- backup power source→::@::←[electricity](electricity.md) generation for [electric vehicles](electric%20vehicle.md)
- [electricity](electricity.md) generation for [electric vehicles](electric%20vehicle.md)→::@::←remote power source
- remote power source→::@::←_(end)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/alkaline_fuel_cell) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
