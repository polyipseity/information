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
		return gen.affix_lines(
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
		text=gen.common.text(methyl_orange.table),
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
		text=gen.common.text(litmus.table),
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
		text=gen.common.text(phenolphthalein.table),
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

1. _(acidic)_→:::←1~3.1 <!--SR:!2023-01-03,44,261!2023-02-04,74,301-->
2. 1~3.1→:::←3.1~4.4 <!--SR:!2023-03-02,85,261!2023-02-15,79,281-->
3. 3.1~4.4→:::←4.4~14 <!--SR:!2023-01-15,56,281!2023-02-17,73,241-->
4. 4.4~14→:::←_(basic)_ <!--SR:!2023-02-06,75,301!2023-01-03,41,241-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1389d0"--><!-- The following content is generated at 2022-11-05T00:25:01.100868+08:00. Any edits will be overridden! -->

1. 1~3.1:::<span style="color: red;">red</span> <!--SR:!2023-04-11,232,250!2023-07-05,258,230-->
2. 3.1~4.4:::<span style="color: orange;">orange</span> <!--SR:!2023-10-09,345,250!2023-07-15,268,230-->
3. 4.4~14:::<span style="color: yellow;">yellow</span> <!--SR:!2023-01-07,79,230!2023-01-24,96,210-->

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

1. _(acidic)_→:::←1~5 <!--SR:!2023-01-04,44,261!2023-02-14,82,301-->
2. 1~5→:::←5~8 <!--SR:!2022-12-27,40,261!2022-12-28,43,281-->
3. 5~8→:::←8~14 <!--SR:!2023-02-16,80,281!2022-12-29,37,241-->
4. 8~14→:::←_(basic)_ <!--SR:!2023-02-03,73,301!2023-01-15,54,261-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="29f820"--><!-- The following content is generated at 2022-11-05T00:25:01.078869+08:00. Any edits will be overridden! -->

1. 1~5:::<span style="color: red;">red</span> <!--SR:!2023-06-13,282,270!2023-09-16,325,250-->
2. 5~8:::<span style="color: purple; background-color: white;">purple</span> <!--SR:!2023-03-31,221,250!2023-07-03,256,230-->
3. 8~14:::<span style="color: blue; background-color: white;">blue</span> <!--SR:!2023-05-12,263,270!2022-12-22,3,150-->

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

1. _(acidic)_→:::←1~8.3 <!--SR:!2022-12-28,36,241!2023-02-10,78,301-->
2. 1~8.3→:::←8.3~10 <!--SR:!2023-01-18,56,261!2023-01-26,63,281-->
3. 8.3~10→:::←10~14 <!--SR:!2023-02-03,70,281!2023-01-02,40,241-->
4. 10~14→:::←_(basic)_ <!--SR:!2023-02-13,81,301!2023-01-19,57,261-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="0245d8"--><!-- The following content is generated at 2022-11-05T00:25:01.058870+08:00. Any edits will be overridden! -->

1. 1~8.3:::colorless <!--SR:!2023-01-03,51,210!2023-01-12,28,210-->
2. 8.3~10:::<span style="color: lightPink;">very pale pink</span> <!--SR:!2023-11-01,362,250!2022-12-26,17,210-->
3. 10~14:::<span style="color: pink;">pink</span> <!--SR:!2023-04-08,118,230!2024-02-15,455,250-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
