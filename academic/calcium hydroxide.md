---
aliases:
  - Ca(OH)2
  - calcium hydroxide
  - limewater
  - slaked lime
tags:
  - academic/chemistry
  - flashcards/academic/Cc/calcium_hydroxide
---

# calcium hydroxide

__Calcium hydroxide__, also known as {{slaked lime}} in its solid state and {{limewater}} in its liquid state, is an [ionic compound](ionic%20compound.md). Its [chemical formula](chemical%20formula.md) is {{Ca(OH)<sub>2</sub>}}. It looks like a {{white solid}} in its solid form. <!--SR:!2023-06-05,132,230!2024-02-05,285,230!2023-06-19,301,270!2023-12-16,391,259-->

## preparation

Treating {{calcium [salts](salt%20(chemistry).md) with a strong [base](base%20(chemistry).md) [precipitates](precipitate.md) out white calcium hydroxide}}. Weak bases {{result in no observation because there are insufficient [hydroxide ions](hydroxide.md) to saturate the [solution](solution%20(chemistry).md)}}: <!--SR:!2023-06-07,55,300!2023-07-10,68,260-->

> treating with [bases](base%20(chemistry).md)
> - {{Ca<sup>2+</sup>(aq) + 2OH<sup>-</sup>(aq) → Ca(OH)<sub>2</sub>(s)}} <!--SR:!2023-10-28,161,300-->

## reactions

### tests

Calcium hydroxide can be used to test for {{[carbon dioxide](carbon%20dioxide.md)}}. <!--SR:!2023-06-09,149,278-->

### preparation
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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d7182f"--><!-- The following content is generated at 2023-04-09T17:42:57.291224+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←Dissolve carbonate hydroxide in deionized [water](water.md). <!--SR:!2023-10-03,348,250!2026-12-09,1345,358-->
2. Dissolve carbonate hydroxide in deionized [water](water.md).→:::←Filter the solution to obtain the [filtrate](filtrate.md). <!--SR:!2023-12-19,375,230!2023-11-05,365,261-->
3. Filter the solution to obtain the [filtrate](filtrate.md).→:::←_(end)_ <!--SR:!2026-01-24,1062,339!2023-10-10,240,259-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
