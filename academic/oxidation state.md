---
aliases: ['oxidation number',]
---

#academic/chemistry #flashcards/academic/oxidation_state

# oxidation state

## simple approach

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read, util
data: gen.TextCode = gen.seq_to_code((
		R'element in a free form\: 0',
		R'ionic compound or ion\: _charge_',
		R'fluorine\: -1',
		R'(if not bonded to a lighter halogen, oxygen, or nitrogen) chlorine, bromine\: -1',
		R'group I metal\: +1',
		R'group II metal\: +2',
		R'metallic hydride\: -1',
		R'hydrogen\: +1',
		R'(if not bonded to oxygen or flourine) oxygen\: -2',
	),
	index=1,
	prefix=f'{{{gen.Tag.MEMORIZE}:_(begin)_}}',
	suffix=f'{{{gen.Tag.MEMORIZE}:_(end)_}}',)
return (
	util.Result(
		location=__env__.cwf_section('2d99fe'),
		text=gen.quote_text(data),
	),
	util.Result(
		location=__env__.cwf_section('341d9e'),
		text=gen.memorize_linked_seq(data,
			hinted=False,
			states=await read.read_flashcard_states(__env__.cwf_section('341d9e')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2d99fe"--><!-- The following content is generated at 2022-11-05T00:25:01.101869+08:00. Any edits will be overridden! -->

> 1. element in a free form: 0
> 2. ionic compound or ion: _charge_
> 3. fluorine: -1
> 4. (if not bonded to a lighter halogen, oxygen, or nitrogen) chlorine, bromine: -1
> 5. group I metal: +1
> 6. group II metal: +2
> 7. metallic hydride: -1
> 8. hydrogen: +1
> 9. (if not bonded to oxygen or flourine) oxygen: -2

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="341d9e"--><!-- The following content is generated at 2022-11-05T00:25:01.108868+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←element in a free form: 0
2. element in a free form: 0→:::←ionic compound or ion: _charge_
3. ionic compound or ion: _charge_→:::←fluorine: -1
4. fluorine: -1→:::←(if not bonded to a lighter halogen, oxygen, or nitrogen) chlorine, bromine: -1
5. (if not bonded to a lighter halogen, oxygen, or nitrogen) chlorine, bromine: -1→:::←group I metal: +1
6. group I metal: +1→:::←group II metal: +2
7. group II metal: +2→:::←metallic hydride: -1
8. metallic hydride: -1→:::←hydrogen: +1
9. hydrogen: +1→:::←(if not bonded to oxygen or flourine) oxygen: -2
10. (if not bonded to oxygen or flourine) oxygen: -2→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
