---
aliases:
  - Ca(OH)2
  - calcium hydroxide
  - limewater
  - slaked lime
tags:
  - flashcards/general/calcium_hydroxide
  - languages/in/English
---

# calcium hydroxide

__Calcium hydroxide__, also known as {{slaked lime}} in its solid state and {{limewater}} in its liquid state, is an [ionic compound](ionic%20compound.md). Its [chemical formula](chemical%20formula.md) is {{Ca(OH)<sub>2</sub>}}. It looks like a {{white solid}} in its solid form. <!--SR:!2024-04-06,305,230!2024-02-05,285,230!2026-07-28,1135,290!2026-09-23,1012,259-->

## preparation

Treating {{calcium [salts](salt%20(chemistry).md) with a strong [base](base%20(chemistry).md) [precipitates](precipitate.md) out white calcium hydroxide}}. Weak bases {{result in no observation because there are insufficient [hydroxide ions](hydroxide.md) to saturate the [solution](solution%20(chemistry).md)}}: <!--SR:!2026-01-24,732,320!2025-12-15,691,280-->

> treating with [bases](base%20(chemistry).md)
>
> - {{Ca<sup>2+</sup>(aq) + 2OH<sup>-</sup>(aq) → Ca(OH)<sub>2</sub>(s)}} <!--SR:!2025-08-28,669,320-->

## reactions

### tests

Calcium hydroxide can be used to test for {{[carbon dioxide](carbon%20dioxide.md)}}. <!--SR:!2025-01-15,584,298-->

## preparation steps

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

Calcium hydroxide can be prepared in the following way:
<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="12ff7a"--><!-- The following content is generated at 2023-04-09T17:42:57.250097+08:00. Any edits will be overridden! -->

> 1. Dissolve carbonate hydroxide in deionized [water](water.md).
> 2. Filter the solution to obtain the [filtrate](filtrate.md).

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d7182f"--><!-- The following content is generated at 2024-01-04T20:17:51.479474+08:00. Any edits will be overridden! -->

- _(begin)_→:::←Dissolve carbonate hydroxide in deionized [water](water.md). <!--SR:!2026-02-26,874,250!2026-12-09,1345,358-->
- Dissolve carbonate hydroxide in deionized [water](water.md).→:::←Filter the solution to obtain the [filtrate](filtrate.md). <!--SR:!2024-06-23,187,210!2026-06-15,952,261-->
- Filter the solution to obtain the [filtrate](filtrate.md).→:::←_(end)_ <!--SR:!2026-01-24,1062,339!2026-02-28,869,279-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/calcium_hydroxide) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
