---
aliases:
  - polytropic index
  - polytropic indexes
  - polytropic indices
  - polytropic process
  - polytropic processes
tags:
  - flashcard/active/general/polytropic_process
  - language/in/English
---

# polytropic process

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

> __polytropic process__
>
> {{$$pV^n = C$$}}
>
> - where
>   - {{$p$ is the [pressure](pressure.md), $V$ is the [volume](volume.md), $n$ is the __polytropic index__, and $C$ is a [constant](constant%20(mathematics).md)}}

## relation between polytropic index and energy transfer ratio

> __relation between polytropic index and energy transfer ratio__
>
> {{$$pV^{(1 - \gamma)K + \gamma} = C$$}}
>
> - where
>   - {{$p$ is the [pressure](pressure.md), $V$ is the [volume](volume.md), and $C$ is a [constant](constant%20(mathematics).md)}}
>   - {{$\gamma$ is the [heat capacity ratio](heat%20capacity%20ratio.md) and $K = \frac{\delta Q}{\delta W}$ is the energy transfer ratio}}
>   - {{thus the __polytropic index__ is $n = (1 - \gamma)K + \gamma$}}
> - conditions: {{[ideal gas](ideal%20gas.md)}}

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
T^{\frac1{\gamma - 1}} & = V^{K - 1}C \\
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
  ("_n_ = 0", "$p = C$; equivalent to [isobaric process](isobaric%20process.md)",),
  ("0 < _n_ < 1", "under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases",),
  ("_n_ = 1", "$pV = C$; under [ideal gas law](ideal%20gas%20law.md), equivalent to [isothermic process](isothermic%20process.md)",),
  ("1 < _n_ < _γ_", "under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) decreases",),
  ("_n_ = _γ_", "under [ideal gas law](ideal%20gas%20law.md), equivalent to [isentropic process](isentropic%20process.md)",),
  ("_γ_ < _n_ < +∞", "under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the same direction",),
  ("_n_ = +∞", "$V = C$; equivalent to [isochoric process](isochoric%20process.md)",),
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

<!--pytextgen generate section="029f"--><!-- The following content is generated at 2023-12-15T10:02:45.991107+08:00. Any edits will be overridden! -->

> | polytropic index | effects |
> |-|-|
> | _n_ < 0 | under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases enough to increase [pressure](pressure.md) too |
> | _n_ = 0 | $p = C$; equivalent to [isobaric process](isobaric%20process.md) |
> | 0 < _n_ < 1 | under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases |
> | _n_ = 1 | $pV = C$; under [ideal gas law](ideal%20gas%20law.md), equivalent to [isothermic process](isothermic%20process.md) |
> | 1 < _n_ < _γ_ | under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) decreases |
> | _n_ = _γ_ | under [ideal gas law](ideal%20gas%20law.md), equivalent to [isentropic process](isentropic%20process.md) |
> | _γ_ < _n_ < +∞ | under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the same direction |
> | _n_ = +∞ | $V = C$; equivalent to [isochoric process](isochoric%20process.md) |

<!--/pytextgen-->

<!--pytextgen generate section="577a"--><!-- The following content is generated at 2024-01-04T20:17:52.495477+08:00. Any edits will be overridden! -->

- _(begin)_→:::←_n_ < 0
- _n_ < 0→:::←_n_ = 0
- _n_ = 0→:::←0 < _n_ < 1
- 0 < _n_ < 1→:::←_n_ = 1
- _n_ = 1→:::←1 < _n_ < _γ_
- 1 < _n_ < _γ_→:::←_n_ = _γ_
- _n_ = _γ_→:::←_γ_ < _n_ < +∞
- _γ_ < _n_ < +∞→:::←_n_ = +∞
- _n_ = +∞→:::←_(end)_

<!--/pytextgen-->

<!--pytextgen generate section="5599"--><!-- The following content is generated at 2024-01-04T20:17:52.438922+08:00. Any edits will be overridden! -->

- _n_ < 0::under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases enough to increase [pressure](pressure.md) too
- _n_ = 0::$p = C$; equivalent to [isobaric process](isobaric%20process.md)
- 0 < _n_ < 1::under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases
- _n_ = 1::$pV = C$; under [ideal gas law](ideal%20gas%20law.md), equivalent to [isothermic process](isothermic%20process.md)
- 1 < _n_ < _γ_::under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) decreases
- _n_ = _γ_::under [ideal gas law](ideal%20gas%20law.md), equivalent to [isentropic process](isentropic%20process.md)
- _γ_ < _n_ < +∞::under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the same direction
- _n_ = +∞::$V = C$; equivalent to [isochoric process](isochoric%20process.md)

<!--/pytextgen-->

<!--pytextgen generate section="0033"--><!-- The following content is generated at 2024-01-04T20:17:52.404405+08:00. Any edits will be overridden! -->

- under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases enough to increase [pressure](pressure.md) too::_n_ < 0
- $p = C$; equivalent to [isobaric process](isobaric%20process.md)::_n_ = 0
- under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases::0 < _n_ < 1
- $pV = C$; under [ideal gas law](ideal%20gas%20law.md), equivalent to [isothermic process](isothermic%20process.md)::_n_ = 1
- under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) decreases::1 < _n_ < _γ_
- under [ideal gas law](ideal%20gas%20law.md), equivalent to [isentropic process](isentropic%20process.md)::_n_ = _γ_
- under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the same direction::_γ_ < _n_ < +∞
- $V = C$; equivalent to [isochoric process](isochoric%20process.md)::_n_ = +∞

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/polytropic_process) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
