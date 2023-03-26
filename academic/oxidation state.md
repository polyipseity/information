---
aliases: ['oxidation number',]
---

#academic/chemistry #flashcards/academic/Oo/oxidation_state

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

1. _(begin)_→:::←element in a free form: 0 <!--SR:!2023-05-14,133,290!2024-03-22,395,330-->
2. element in a free form: 0→:::←ionic compound or ion: _charge_ <!--SR:!2023-10-20,218,250!2023-06-12,154,290-->
3. ionic compound or ion: _charge_→:::←fluorine: -1 <!--SR:!2023-04-23,106,250!2024-03-26,372,290-->
4. fluorine: -1→:::←(if not bonded to a lighter halogen, oxygen, or nitrogen) chlorine, bromine: -1 <!--SR:!2023-09-02,174,230!2023-10-01,208,250-->
5. (if not bonded to a lighter halogen, oxygen, or nitrogen) chlorine, bromine: -1→:::←group I metal: +1 <!--SR:!2023-06-15,149,270!2023-04-23,97,230-->
6. group I metal: +1→:::←group II metal: +2 <!--SR:!2023-12-31,322,310!2023-07-31,205,310-->
7. group II metal: +2→:::←metallic hydride: -1 <!--SR:!2023-10-02,216,270!2023-04-04,103,270-->
8. metallic hydride: -1→:::←hydrogen: +1 <!--SR:!2023-06-21,160,290!2023-05-12,141,290-->
9. hydrogen: +1→:::←(if not bonded to oxygen or flourine) oxygen: -2 <!--SR:!2023-10-06,211,250!2023-12-29,293,270-->
10. (if not bonded to oxygen or flourine) oxygen: -2→:::←_(end)_ <!--SR:!2024-03-23,396,330!2023-04-05,40,230-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
