---
aliases:
  - polytropic index
  - polytropic indexes
  - polytropic indices
  - polytropic process
  - polytropic processes
tags:
  - flashcard/active/general/eng/polytropic_process
  - language/in/English
---

# polytropic process

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

> __polytropic process__
>
> {@{$$pV^n = C$$}@}
>
> - where
>   - {@{$p$ is the [pressure](pressure.md), $V$ is the [volume](volume.md), $n$ is the __polytropic index__, and $C$ is a [constant](constant%20(mathematics).md)}@} <!--SR:!2028-01-29,1169,350!2027-10-20,1091,350-->

## relation between polytropic index and energy transfer ratio

> __relation between polytropic index and energy transfer ratio__
>
> {@{$$pV^{(1 - \gamma)K + \gamma} = C$$}@}
>
> - where
>   - {@{$p$ is the [pressure](pressure.md), $V$ is the [volume](volume.md), and $C$ is a [constant](constant%20(mathematics).md)}@}
>   - {@{$\gamma$ is the [heat capacity ratio](heat%20capacity%20ratio.md) and $K = \frac{\delta Q}{\delta W}$ is the energy transfer ratio}@}
>   - {@{thus the __polytropic index__ is $n = (1 - \gamma)K + \gamma$}@}
> - conditions: {@{[ideal gas](ideal%20gas.md)}@} <!--SR:!2025-12-09,221,210!2026-01-30,532,310!2025-09-27,162,270!2025-07-04,414,310!2025-05-20,94,329-->

The relation between polytropic index and energy transfer ratio can be derived as follows:

$$\begin{aligned}
K & = \frac{\delta Q}{\delta W} \\
U & = \frac{f}2nRT = \frac{nRT}{\gamma - 1} \\
\mathrm{d}U & = \frac{nR}{\gamma - 1} \,\mathrm{d}T \\
\mathrm{d}U & = \delta Q - \delta W \\
& = K \,\delta W - \delta W \\
& = (K - 1)\, \delta W \\
\frac{nR}{\gamma - 1} \,\mathrm{d}T & = (K - 1) \,\delta W \\
& = (K - 1)p \,\mathrm{d}V \\
& = \frac{(K - 1)nRT}V \,\mathrm{d}V \\
\frac{1}{T(\gamma - 1)} \,\mathrm{d}T & = \frac{K - 1}V \,\mathrm{d}V \\
\frac{\ln T}{\gamma - 1} & = (K - 1)\ln V + C \\
T^{\frac1{\gamma - 1} } & = V^{K - 1}C \\
T & = V^{(K - 1)(\gamma - 1)}C \\
\frac{pV}{nR} & = V^{(K - 1)(\gamma - 1)}C \\
pV^{1 + (K - 1)(1 - \gamma)} & = C \\
pV^{1 + K - K\gamma - 1 + \gamma} & = C \\
pV^{(1 - \gamma)K + \gamma} &= C
\end{aligned}$$

## relationship to ideal process

### variation of polytropic index _n_

```Python
# pytextgen generate data
from asyncio import gather as _gather
from itertools import chain as _chain
headers = ("polytropic index", "effects",)
table = (
  ("_n_ < 0", "under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases enough to increase [pressure](pressure.md) too",),
  ("_n_ = 0", "$p = C$, equivalent to [isobaric process](isobaric%20process.md); under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in opposite direction",),
  ("0 < _n_ < 1", "under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases",),
  ("_n_ = 1", "$pV = C$; under [ideal gas law](ideal%20gas%20law.md), equivalent to [isothermic process](isothermic%20process.md), and [heat](heat.md) and [work](work%20(physics).md) flow in opposite direction",),
  ("1 < _n_ < _γ_", "under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) decreases",),
  ("_n_ = _γ_", "under [ideal gas law](ideal%20gas%20law.md), equivalent to [isentropic process](isentropic%20process.md), and there is no [heat](heat.md) flow",),
  ("_γ_ < _n_ < +∞", "under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the same direction",),
  ("_n_ = +∞", "$V = C$, equivalent to [isochoric process](isochoric%20process.md); there is no [work](work%20(physics).md)",),
)
return _chain.from_iterable(await _gather(
  memorize_table(
    __env__.cwf_sects("029f", "577a",),
    headers, table,
  ),
  memorize_map(
    __env__.cwf_sects(None, "5599", "0033",),
    items_to_map(*(row[:2] for row in table)),
  ),
))
```

<!--pytextgen generate section="029f"--><!-- The following content is generated at 2024-09-13T23:15:48.061046+08:00. Any edits will be overridden! -->

> | polytropic index | effects |
> |-|-|
> | _n_ < 0 | under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases enough to increase [pressure](pressure.md) too |
> | _n_ = 0 | $p = C$, equivalent to [isobaric process](isobaric%20process.md); under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in opposite direction |
> | 0 < _n_ < 1 | under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases |
> | _n_ = 1 | $pV = C$; under [ideal gas law](ideal%20gas%20law.md), equivalent to [isothermic process](isothermic%20process.md), and [heat](heat.md) and [work](work%20(physics).md) flow in opposite direction |
> | 1 < _n_ < _γ_ | under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) decreases |
> | _n_ = _γ_ | under [ideal gas law](ideal%20gas%20law.md), equivalent to [isentropic process](isentropic%20process.md), and there is no [heat](heat.md) flow |
> | _γ_ < _n_ < +∞ | under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the same direction |
> | _n_ = +∞ | $V = C$, equivalent to [isochoric process](isochoric%20process.md); there is no [work](work%20(physics).md) |

<!--/pytextgen-->

<!--pytextgen generate section="577a"--><!-- The following content is generated at 2024-01-04T20:17:52.495477+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←_n_ < 0 <!--SR:!2026-11-20,814,330!2027-07-10,931,330-->
- _n_ < 0→::@::←_n_ = 0 <!--SR:!2027-07-09,1009,350!2026-01-18,582,330-->
- _n_ = 0→::@::←0 < _n_ < 1 <!--SR:!2028-03-12,1203,350!2028-10-03,1360,350-->
- 0 < _n_ < 1→::@::←_n_ = 1 <!--SR:!2027-12-03,1125,350!2026-03-09,569,310-->
- _n_ = 1→::@::←1 < _n_ < _γ_ <!--SR:!2028-01-23,1164,350!2027-06-15,991,350-->
- 1 < _n_ < _γ_→::@::←_n_ = _γ_ <!--SR:!2027-09-05,1055,350!2027-09-18,1065,350-->
- _n_ = _γ_→::@::←_γ_ < _n_ < +∞ <!--SR:!2027-08-31,970,330!2027-10-25,1095,350-->
- _γ_ < _n_ < +∞→::@::←_n_ = +∞ <!--SR:!2027-12-08,1128,350!2028-02-23,1189,350-->
- _n_ = +∞→::@::←_(end)_ <!--SR:!2028-02-16,1183,350!2027-07-08,1009,350-->

<!--/pytextgen-->

<!--pytextgen generate section="5599"--><!-- The following content is generated at 2024-09-13T23:15:48.088970+08:00. Any edits will be overridden! -->

- _n_ < 0:@:under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases enough to increase [pressure](pressure.md) too <!--SR:!2027-04-21,862,290-->
- _n_ = 0:@:$p = C$, equivalent to [isobaric process](isobaric%20process.md); under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in opposite direction <!--SR:!2027-08-01,1027,350-->
- 0 < _n_ < 1:@:under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases <!--SR:!2026-11-01,605,250-->
- _n_ = 1:@:$pV = C$; under [ideal gas law](ideal%20gas%20law.md), equivalent to [isothermic process](isothermic%20process.md), and [heat](heat.md) and [work](work%20(physics).md) flow in opposite direction <!--SR:!2027-05-14,892,330-->
- 1 < _n_ < _γ_:@:under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) decreases <!--SR:!2025-07-06,213,250-->
- _n_ = _γ_:@:under [ideal gas law](ideal%20gas%20law.md), equivalent to [isentropic process](isentropic%20process.md), and there is no [heat](heat.md) flow <!--SR:!2027-11-17,1112,350-->
- _γ_ < _n_ < +∞:@:under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the same direction <!--SR:!2026-05-24,622,310-->
- _n_ = +∞:@:$V = C$, equivalent to [isochoric process](isochoric%20process.md); there is no [work](work%20(physics).md) <!--SR:!2027-11-16,1112,350-->

<!--/pytextgen-->

<!--pytextgen generate section="0033"--><!-- The following content is generated at 2024-09-13T23:15:48.105926+08:00. Any edits will be overridden! -->

- under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases enough to increase [pressure](pressure.md) too:@:_n_ < 0 <!--SR:!2027-03-29,858,330-->
- $p = C$, equivalent to [isobaric process](isobaric%20process.md); under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in opposite direction:@:_n_ = 0 <!--SR:!2027-09-18,1065,350-->
- under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases:@:0 < _n_ < 1 <!--SR:!2027-06-18,916,330-->
- $pV = C$; under [ideal gas law](ideal%20gas%20law.md), equivalent to [isothermic process](isothermic%20process.md), and [heat](heat.md) and [work](work%20(physics).md) flow in opposite direction:@:_n_ = 1 <!--SR:!2028-04-16,1230,350-->
- under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) decreases:@:1 < _n_ < _γ_ <!--SR:!2026-04-02,582,310-->
- under [ideal gas law](ideal%20gas%20law.md), equivalent to [isentropic process](isentropic%20process.md), and there is no [heat](heat.md) flow:@:_n_ = _γ_ <!--SR:!2028-09-09,1344,350-->
- under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the same direction:@:_γ_ < _n_ < +∞ <!--SR:!2026-10-30,664,270-->
- $V = C$, equivalent to [isochoric process](isochoric%20process.md); there is no [work](work%20(physics).md):@:_n_ = +∞ <!--SR:!2027-07-31,1026,350-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/polytropic_process) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
