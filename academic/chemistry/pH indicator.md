#flashcards/chemistry/pH_indicator #academic/chemistry

# pH indicator

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
import typing
@typing.final
class pHRanges(typing.NamedTuple):
	data: typing.Mapping[str, str]

	@property
	def table(self: typing.Self) -> str:
		return gen.common.quotette(
			gen.common.rows_to_table(self.data.items(),
				names=('pH', 'color',),
				values=util.identity,),
			prefix='> ',
		)

	@property
	def mem_ranges(self: typing.Self) -> gen.TextCode:
		return gen.common.seq_to_code(self.data.keys(),
			index=1,
			prefix='{mem:_(acidic)_}',
			suffix='{mem:_(basic)_}',
			escape=True,)

	@property
	def mem_map(self: typing.Self) -> gen.TextCode:
		return gen.common.two_columns_to_code(self.data.items(),
			left=lambda item: gen.TextCode.escape(item[0]),
			right=lambda item: gen.TextCode.escape(item[1]),)
methyl_orange: pHRanges = pHRanges({
	'1~3.1': '<span style="color: red;">red</span>',
	'3.1~4.4': '<span style="color: orange;">orange</span>',
	'4.4~14': '<span style="color: yellow;">yellow</span>',
})
litmus: pHRanges = pHRanges({
	'1~5': '<span style="color: red;">red</span>',
	'5~8': '<span style="color: purple; background-color: white;">purple</span>',
	'8~14': '<span style="color: blue; background-color: white;">blue</span>',
})
phenolphthalein: pHRanges = pHRanges({
	'1~8.3': 'colorless',
	'8.3~10': '<span style="color: lightPink;">very pale pink</span>',
	'10~14': '<span style="color: pink;">pink</span>',
})

__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('a9208f'),
		text=methyl_orange.table,
	),
	gen.Result(
		location=__env__.cwf_section('d82740'),
		text=gen.common.memorize_linked_seq(methyl_orange.mem_ranges,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('d82740')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('1389d0'),
		text=gen.common.memorize_two_sided(methyl_orange.mem_map,
			states=read.read_flashcard_states(__env__.cwf_section('1389d0')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('2acde1'),
		text=litmus.table,
	),
	gen.Result(
		location=__env__.cwf_section('f25a99'),
		text=gen.common.memorize_linked_seq(litmus.mem_ranges,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('f25a99')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('29f820'),
		text=gen.common.memorize_two_sided(litmus.mem_map,
			states=read.read_flashcard_states(__env__.cwf_section('29f820')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('5c8883'),
		text=phenolphthalein.table,
	),
	gen.Result(
		location=__env__.cwf_section('155d9a'),
		text=gen.common.memorize_linked_seq(phenolphthalein.mem_ranges,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('155d9a')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('0245d8'),
		text=gen.common.memorize_two_sided(phenolphthalein.mem_map,
			states=read.read_flashcard_states(__env__.cwf_section('0245d8')),
		),
	),
)
```
%%

## methyl orange

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a9208f"--><!-- The following content is generated at 2022-11-05T00:25:01.086869+08:00. Any edits will be overridden! -->

> pH | color
> -|-
> 1~3.1 | <span style="color: red;">red</span>
> 3.1~4.4 | <span style="color: orange;">orange</span>
> 4.4~14 | <span style="color: yellow;">yellow</span>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d82740"--><!-- The following content is generated at 2022-11-09T19:01:32.632530+08:00. Any edits will be overridden! -->

1. _(acidic)_→:::←1~3.1 <!--SR:!2023-05-08,121,261!2023-12-10,309,321-->
2. 1~3.1→:::←3.1~4.4 <!--SR:!2023-03-02,85,261!2023-12-27,314,301-->
3. 3.1~4.4→:::←4.4~14 <!--SR:!2023-06-22,158,281!2023-02-17,73,241-->
4. 4.4~14→:::←_(basic)_ <!--SR:!2023-12-15,312,321!2023-04-24,107,241-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1389d0"--><!-- The following content is generated at 2022-11-05T00:25:01.100868+08:00. Any edits will be overridden! -->

1. 1~3.1:::<span style="color: red;">red</span> <!--SR:!2023-04-11,232,250!2023-07-05,258,230-->
2. 3.1~4.4:::<span style="color: orange;">orange</span> <!--SR:!2023-10-09,345,250!2023-07-15,268,230-->
3. 4.4~14:::<span style="color: yellow;">yellow</span> <!--SR:!2023-07-04,178,230!2023-03-13,48,190-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## litmus

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2acde1"--><!-- The following content is generated at 2022-11-05T00:25:01.064868+08:00. Any edits will be overridden! -->

> pH | color
> -|-
> 1~5 | <span style="color: red;">red</span>
> 5~8 | <span style="color: purple; background-color: white;">purple</span>
> 8~14 | <span style="color: blue; background-color: white;">blue</span>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f25a99"--><!-- The following content is generated at 2022-11-09T19:11:57.168670+08:00. Any edits will be overridden! -->

1. _(acidic)_→:::←1~5 <!--SR:!2023-05-07,120,261!2024-02-02,351,321-->
2. 1~5→:::←5~8 <!--SR:!2023-04-11,105,261!2023-06-18,171,301-->
3. 5~8→:::←8~14 <!--SR:!2023-12-26,313,301!2023-05-02,124,261-->
4. 8~14→:::←_(basic)_ <!--SR:!2023-09-13,221,301!2023-06-05,141,261-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="29f820"--><!-- The following content is generated at 2022-11-05T00:25:01.078869+08:00. Any edits will be overridden! -->

1. 1~5:::<span style="color: red;">red</span> <!--SR:!2023-06-13,282,270!2023-09-16,325,250-->
2. 5~8:::<span style="color: purple; background-color: white;">purple</span> <!--SR:!2023-03-31,221,250!2023-07-03,256,230-->
3. 8~14:::<span style="color: blue; background-color: white;">blue</span> <!--SR:!2023-05-12,263,270!2023-04-07,59,190-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## phenolphthalein

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5c8883"--><!-- The following content is generated at 2022-11-05T00:25:01.044870+08:00. Any edits will be overridden! -->

> pH | color
> -|-
> 1~8.3 | colorless
> 8.3~10 | <span style="color: lightPink;">very pale pink</span>
> 10~14 | <span style="color: pink;">pink</span>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="155d9a"--><!-- The following content is generated at 2022-11-09T19:11:57.181670+08:00. Any edits will be overridden! -->

1. _(acidic)_→:::←1~8.3 <!--SR:!2023-03-30,91,241!2024-01-12,334,321-->
2. 1~8.3→:::←8.3~10 <!--SR:!2023-06-16,149,261!2023-07-22,177,281-->
3. 8.3~10→:::←10~14 <!--SR:!2023-11-08,277,301!2023-04-09,97,241-->
4. 10~14→:::←_(basic)_ <!--SR:!2024-02-01,350,321!2023-06-18,149,261-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="0245d8"--><!-- The following content is generated at 2022-11-05T00:25:01.058870+08:00. Any edits will be overridden! -->

1. 1~8.3:::colorless <!--SR:!2023-04-30,113,210!2023-03-10,57,210-->
2. 8.3~10:::<span style="color: lightPink;">very pale pink</span> <!--SR:!2023-11-01,362,250!2023-04-20,77,210-->
3. 10~14:::<span style="color: pink;">pink</span> <!--SR:!2023-04-08,118,230!2024-02-15,455,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
