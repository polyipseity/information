---
aliases:
  - Ca(OH)2
  - calcium hydroxide
  - limewater
  - slaked lime
tags:
  - flashcard/active/general/eng/calcium_hydroxide
  - language/in/English
---

# calcium hydroxide

__Calcium hydroxide__, also known as {@{slaked lime}@} in its solid state and {@{limewater}@} in its liquid state, is an [ionic compound](ionic%20compound.md). Its [chemical formula](chemical%20formula.md) is {@{Ca(OH)<sub>2</sub>}@}. It looks like a {@{white solid}@} in its solid form. <!--SR:!2028-02-28,951,230!2026-08-18,925,250!2026-07-28,1135,290!2026-09-23,1012,259-->

## preparation

Treating {@{calcium [salts](salt%20(chemistry).md) with a strong [base](base%20(chemistry).md) [precipitates](precipitate.md) out white calcium hydroxide}@}. {@{Weak bases result in no observation}@} because there are {@{insufficient [hydroxide ions](hydroxide.md) to saturate the [solution](solution%20(chemistry).md)}@}: <!--SR:!2026-01-24,732,320!2031-04-02,1934,280!2025-12-25,4,292-->

> treating with [bases](base%20(chemistry).md)
>
> - {@{Ca<sup>2+</sup>(aq) + 2OH<sup>-</sup>(aq) → Ca(OH)<sub>2</sub>(s)}@} <!--SR:!2033-10-06,2961,340-->

## reactions

### tests

Calcium hydroxide can be used to test for {@{[carbon dioxide](carbon%20dioxide.md)}@}. <!--SR:!2031-08-26,2414,318-->

## preparation steps

```Python
# pytextgen generate data
from pytextgen import gen, read, util
data: gen.TextCode = gen.seq_to_code((
  'Dissolve carbonate hydroxide in deionized [water](water.md).',
  'Filter the solution to obtain the [filtrate](filtrate.md).',
  ),
  index=1,
  prefix=f'{{{gen.Tag.MEMORIZE}:_(begin)_}}',
  suffix=f'{{{gen.Tag.MEMORIZE}:_(end)_}}',)
return (
  util.Result(
    location=__env__.cwf_sect('12ff7a'),
    text=gen.quote_text(data),
  ),
  util.Result(
    location=__env__.cwf_sect('d7182f'),
    text=gen.memorize_linked_seq(data,
      hinted=False,
      states=await read.read_flashcard_states(__env__.cwf_sect('d7182f')),
    ),
  ),
)
```

Calcium hydroxide can be prepared in the following way:
<!--pytextgen generate section="12ff7a"--><!-- The following content is generated at 2023-04-09T17:42:57.250097+08:00. Any edits will be overridden! -->

> 1. Dissolve carbonate hydroxide in deionized [water](water.md).
> 2. Filter the solution to obtain the [filtrate](filtrate.md).

<!--/pytextgen-->

<!--pytextgen generate section="d7182f"--><!-- The following content is generated at 2024-01-04T20:17:51.479474+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←Dissolve carbonate hydroxide in deionized [water](water.md). <!--SR:!2026-02-26,874,250!2026-12-09,1345,358-->
- Dissolve carbonate hydroxide in deionized [water](water.md).→::@::←Filter the solution to obtain the [filtrate](filtrate.md). <!--SR:!2027-10-21,823,210!2026-06-15,952,261-->
- Filter the solution to obtain the [filtrate](filtrate.md).→::@::←_(end)_ <!--SR:!2026-01-24,1062,339!2026-02-28,869,279-->

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/calcium_hydroxide) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
