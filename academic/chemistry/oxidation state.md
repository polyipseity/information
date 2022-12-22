---
aliases: ['oxidation number',]
---

#flashcards/chemistry/oxidation_state #academic/chemistry

# oxidation state

## simple approach

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
data: gen.TextCode = gen.common.seq_to_code((
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
	prefix='{mem:_(begin)_}',
	suffix='{mem:_(end)_}',)
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('2d99fe'),
		text=gen.common.quote_text(data),
	),
	gen.Result(
		location=__env__.cwf_section('341d9e'),
		text=gen.common.memorize_linked_seq(data,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('341d9e')),
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

1. _(begin)_→:::←element in a free form: 0 <!--SR:!2023-01-01,46,290!2023-02-18,85,310-->
2. element in a free form: 0→:::←ionic compound or ion: _charge_ <!--SR:!2023-03-16,86,250!2023-01-09,53,290-->
3. ionic compound or ion: _charge_→:::←fluorine: -1 <!--SR:!2023-01-07,31,230!2023-03-20,98,270-->
4. fluorine: -1→:::←(if not bonded to a lighter halogen, oxygen, or nitrogen) chlorine, bromine: -1 <!--SR:!2022-12-30,30,230!2023-03-07,80,250-->
5. (if not bonded to a lighter halogen, oxygen, or nitrogen) chlorine, bromine: -1→:::←group I metal: +1 <!--SR:!2023-01-17,55,270!2023-01-16,41,230-->
6. group I metal: +1→:::←group II metal: +2 <!--SR:!2023-02-09,77,290!2023-01-07,51,290-->
7. group II metal: +2→:::←metallic hydride: -1 <!--SR:!2023-02-28,78,270!2023-04-04,103,270-->
8. metallic hydride: -1→:::←hydrogen: +1 <!--SR:!2023-01-12,55,290!2023-05-12,141,290-->
9. hydrogen: +1→:::←(if not bonded to oxygen or flourine) oxygen: -2 <!--SR:!2023-03-09,81,250!2023-03-11,84,250-->
10. (if not bonded to oxygen or flourine) oxygen: -2→:::←_(end)_ <!--SR:!2023-02-17,84,310!2023-02-24,74,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
