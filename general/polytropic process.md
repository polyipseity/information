---
aliases:
  - polytropic index
  - polytropic indexes
  - polytropic indices
  - polytropic process
  - polytropic processes
tags:
  - flashcards/general/polytropic_process
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
>     - {{$p$ is the [pressure](pressure.md), $V$ is the [volume](volume.md), $n$ is the __polytropic index__, and $C$ is a [constant](constant%20(mathematics).md)}}

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

1. _(begin)_→:::←_n_ < 0
2. _n_ < 0→:::←_n_ = 0
3. _n_ = 0→:::←0 < _n_ < 1
4. 0 < _n_ < 1→:::←_n_ = 1
5. _n_ = 1→:::←1 < _n_ < _γ_
6. 1 < _n_ < _γ_→:::←_n_ = _γ_
7. _n_ = _γ_→:::←_γ_ < _n_ < +∞
8. _γ_ < _n_ < +∞→:::←_n_ = +∞
9. _n_ = +∞→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5599"--><!-- The following content is generated at 2023-12-15T10:02:45.970998+08:00. Any edits will be overridden! -->

1. _n_ < 0::under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases enough to increase [pressure](pressure.md) too
2. _n_ = 0::$p = C$; equivalent to [isobaric process](isobaric%20process.md)
3. 0 < _n_ < 1::under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases
4. _n_ = 1::$pV = C$; under [ideal gas law](ideal%20gas%20law.md), equivalent to [isothermic process](isothermic%20process.md)
5. 1 < _n_ < _γ_::under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) decreases
6. _n_ = _γ_::under [ideal gas law](ideal%20gas%20law.md), equivalent to [isentropic process](isentropic%20process.md)
7. _γ_ < _n_ < +∞::under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the same direction
8. _n_ = +∞::$V = C$; equivalent to [isochoric process](isochoric%20process.md)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="0033"--><!-- The following content is generated at 2023-12-15T10:02:46.001804+08:00. Any edits will be overridden! -->

1. under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases enough to increase [pressure](pressure.md) too::_n_ < 0
2. $p = C$; equivalent to [isobaric process](isobaric%20process.md)::_n_ = 0
3. under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) increases::0 < _n_ < 1
4. $pV = C$; under [ideal gas law](ideal%20gas%20law.md), equivalent to [isothermic process](isothermic%20process.md)::_n_ = 1
5. under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the opposite direction; when [volume](volume.md) increases, [temperature](temperature.md) decreases::1 < _n_ < _γ_
6. under [ideal gas law](ideal%20gas%20law.md), equivalent to [isentropic process](isentropic%20process.md)::_n_ = _γ_
7. under [ideal gas law](ideal%20gas%20law.md), [heat](heat.md) and [work](work%20(physics).md) flow in the same direction::_γ_ < _n_ < +∞
8. $V = C$; equivalent to [isochoric process](isochoric%20process.md)::_n_ = +∞

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
