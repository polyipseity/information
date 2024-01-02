---
aliases:
  - polytropic index
  - polytropic indexes
  - polytropic indices
  - polytropic process
  - polytropic processes
tags:
  - flashcards/general/polytropic_process
  - languages/in/English
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# polytropic process

> __polytropic process__
>
> {{$$pV^n = C$$}}
>
> - where
>     - {{$p$ is the [pressure](pressure.md), $V$ is the [volume](volume.md), $n$ is the __polytropic index__, and $C$ is a [constant](constant%20(mathematics).md)}} <!--SR:!2024-01-05,16,290!2024-01-03,14,290-->

## relation between polytropic index and energy transfer ratio

> __relation between polytropic index and energy transfer ratio__
>
> {{$$pV^{(1 - \gamma)K + \gamma} = C$$}}
>
> - where
>     - {{$p$ is the [pressure](pressure.md), $V$ is the [volume](volume.md), and $C$ is a [constant](constant%20(mathematics).md)}}
>     - {{$\gamma$ is the [heat capacity ratio](heat%20capacity%20ratio.md) and $K = \frac{\delta Q}{\delta W}$ is the energy transfer ratio, so the __polytropic index__ $n = (1 - \gamma)K + \gamma$}}
> - conditions: {{[ideal gas](ideal%20gas.md)}} <!--SR:!2024-01-04,6,250!2024-02-26,55,310!2024-02-07,39,290!2024-02-03,36,290-->

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

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from asyncio import gather as _gather
from itertools import chain as _chain

e = __env__
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
    e.cwf_sects("029f", "577a",),
    headers, table,
  ),
  memorize_map(
    e.cwf_sects(None, "5599", "0033",),
    items_to_map(*(row[:2] for row in table)),
  ),
))
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="029f"--><!-- The following content is generated at 2023-12-15T10:02:45.991107+08:00. Any edits will be overridden! -->

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

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="577a"--><!-- The following content is generated at 2023-12-15T09:34:37.162579+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←_n_ < 0 <!--SR:!2024-02-17,48,290!2024-01-06,17,290-->
2. _n_ < 0→:::←_n_ = 0 <!--SR:!2024-01-03,14,290!2024-01-31,34,290-->
3. _n_ = 0→:::←0 < _n_ < 1 <!--SR:!2024-01-05,16,290!2024-01-06,17,290-->
4. 0 < _n_ < 1→:::←_n_ = 1 <!--SR:!2024-01-03,14,290!2024-02-15,46,290-->
5. _n_ = 1→:::←1 < _n_ < _γ_ <!--SR:!2024-01-04,15,290!2024-02-22,51,310-->
6. 1 < _n_ < _γ_→:::←_n_ = _γ_ <!--SR:!2024-01-03,14,290!2024-02-26,55,310-->
7. _n_ = _γ_→:::←_γ_ < _n_ < +∞ <!--SR:!2024-01-06,17,290!2024-01-04,15,290-->
8. _γ_ < _n_ < +∞→:::←_n_ = +∞ <!--SR:!2024-01-04,15,290!2024-01-04,15,290-->
9. _n_ = +∞→:::←_(end)_ <!--SR:!2024-01-05,16,290!2024-02-23,52,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5599"--><!-- The following content is generated at 2023-12-15T10:02:45.970998+08:00. Any edits will be overridden! -->

1. _n_ < 0::under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases enough to increase [pressure](pressure.md) too <!--SR:!2024-01-31,32,270-->
2. _n_ = 0::$p = C$; equivalent to [isobaric process](isobaric%20process.md) <!--SR:!2024-02-24,53,310-->
3. 0 < _n_ < 1::under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases <!--SR:!2024-02-03,32,270-->
4. _n_ = 1::$pV = C$; under [ideal gas law](ideal%20gas%20law.md), equivalent to [isothermic process](isothermic%20process.md) <!--SR:!2024-01-05,16,290-->
5. 1 < _n_ < _γ_::under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) decreases <!--SR:!2024-01-21,23,270-->
6. _n_ = _γ_::under [ideal gas law](ideal%20gas%20law.md), equivalent to [isentropic process](isentropic%20process.md) <!--SR:!2024-01-04,15,290-->
7. _γ_ < _n_ < +∞::under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the same direction <!--SR:!2024-02-21,50,290-->
8. _n_ = +∞::$V = C$; equivalent to [isochoric process](isochoric%20process.md) <!--SR:!2024-01-03,14,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="0033"--><!-- The following content is generated at 2023-12-15T10:02:46.001804+08:00. Any edits will be overridden! -->

1. under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases enough to increase [pressure](pressure.md) too::_n_ < 0 <!--SR:!2024-01-05,16,290-->
2. $p = C$; equivalent to [isobaric process](isobaric%20process.md)::_n_ = 0 <!--SR:!2024-01-03,14,290-->
3. under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases::0 < _n_ < 1 <!--SR:!2024-01-06,17,290-->
4. $pV = C$; under [ideal gas law](ideal%20gas%20law.md), equivalent to [isothermic process](isothermic%20process.md)::_n_ = 1 <!--SR:!2024-01-05,16,290-->
5. under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) decreases::1 < _n_ < _γ_ <!--SR:!2024-01-06,17,290-->
6. under [ideal gas law](ideal%20gas%20law.md), equivalent to [isentropic process](isentropic%20process.md)::_n_ = _γ_ <!--SR:!2024-01-06,17,290-->
7. under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the same direction::_γ_ < _n_ < +∞ <!--SR:!2024-02-03,34,270-->
8. $V = C$; equivalent to [isochoric process](isochoric%20process.md)::_n_ = +∞ <!--SR:!2024-01-03,14,290-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/polytropic_process) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
