#flashcards/chemistry/pH_indicator #academic/chemistry

# pH indicator

## methyl orange

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
data: gen.TextCode = gen.TextCode.compile(
	r'''{mem:_(begin)_}{text:pH | color
-|-
}1~3.1{text: | <span style="color\: red;">red</span>
}3.1~4.4{text: | <span style="color\: orange;">orange</span>
}4.4~14{text: | <span style="color\: yellow;">yellow</span>}{mem:_(end)_}'''
)
sem: gen.TextCode = gen.TextCode.compile(
	r'''<span style="color\: red;">red</span>{}<span style="color\: orange;">orange</span>{}<span style="color\: yellow;">yellow</span>'''
)
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('a9208f'),
		text=gen.common.quote_text(data),
	),
	gen.Result(
		location=__env__.cwf_section('d82740'),
		text=gen.common.memorize_linked_seq(data,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('d82740')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('1389d0'),
		text=gen.common.semantics_seq_map(data, sem,
			reversible=True,
			states=read.read_flashcard_states(__env__.cwf_section('1389d0')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a9208f"--><!-- The following content is generated at 2022-11-05T00:25:01.086869+08:00. Any edits will be overridden! -->

> pH | color
> -|-
> 1~3.1 | <span style="color: red;">red</span>
> 3.1~4.4 | <span style="color: orange;">orange</span>
> 4.4~14 | <span style="color: yellow;">yellow</span>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d82740"--><!-- The following content is generated at 2022-11-05T00:25:01.093869+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←1~3.1 <!--SR:!2022-11-20,16,261!2022-11-22,18,281-->
2. 1~3.1→:::←3.1~4.4 <!--SR:!2022-11-13,9,221!2022-11-07,6,241-->
3. 3.1~4.4→:::←4.4~14 <!--SR:!2022-11-05,4,241!2022-11-13,9,221-->
4. 4.4~14→:::←_(end)_ <!--SR:!2022-11-23,19,281!2022-11-07,6,241-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1389d0"--><!-- The following content is generated at 2022-11-05T00:25:01.100868+08:00. Any edits will be overridden! -->

1. 1~3.1:::<span style="color: red;">red</span> <!--SR:!2023-04-11,232,250!2023-07-05,258,230-->
2. 3.1~4.4:::<span style="color: orange;">orange</span> <!--SR:!2023-10-09,345,250!2023-07-15,268,230-->
3. 4.4~14:::<span style="color: yellow;">yellow</span> <!--SR:!2023-01-07,79,230!2023-01-24,96,210-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## litmus

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
data: gen.TextCode = gen.TextCode.compile(
	r'''{mem:_(begin)_}{text:pH | color
-|-
}1~5{text: | <span style="color\: red;">red</span>
}5~8{text: | <span style="color\: purple; background-color\: white;">purple</span>
}8~14{text: | <span style="color\: blue; background-color\: white;">blue</span>}{mem:_(end)_}'''
)
sem: gen.TextCode = gen.TextCode.compile(
	r'''<span style="color\: red;">red</span>{}<span style="color\: purple; background-color\: white;">purple</span>{}<span style="color\: blue; background-color\: white;">blue</span>'''
)
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('2acde1'),
		text=gen.common.quote_text(data),
	),
	gen.Result(
		location=__env__.cwf_section('f25a99'),
		text=gen.common.memorize_linked_seq(data,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('f25a99')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('29f820'),
		text=gen.common.semantics_seq_map(data, sem,
			reversible=True,
			states=read.read_flashcard_states(__env__.cwf_section('29f820')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2acde1"--><!-- The following content is generated at 2022-11-05T00:25:01.064868+08:00. Any edits will be overridden! -->

> pH | color
> -|-
> 1~5 | <span style="color: red;">red</span>
> 5~8 | <span style="color: purple; background-color: white;">purple</span>
> 8~14 | <span style="color: blue; background-color: white;">blue</span>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f25a99"--><!-- The following content is generated at 2022-11-05T00:25:01.071868+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←1~5 <!--SR:!2022-11-05,4,241!2022-11-24,20,281-->
2. 1~5→:::←5~8 <!--SR:!2022-11-06,5,241!2022-11-15,11,261-->
3. 5~8→:::←8~14 <!--SR:!2022-11-07,6,241!2022-11-07,6,241-->
4. 8~14→:::←_(end)_ <!--SR:!2022-11-22,18,281!2022-11-07,6,241-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="29f820"--><!-- The following content is generated at 2022-11-05T00:25:01.078869+08:00. Any edits will be overridden! -->

1. 1~5:::<span style="color: red;">red</span> <!--SR:!2023-06-13,282,270!2023-09-16,325,250-->
2. 5~8:::<span style="color: purple; background-color: white;">purple</span> <!--SR:!2023-03-31,221,250!2023-07-03,256,230-->
3. 8~14:::<span style="color: blue; background-color: white;">blue</span> <!--SR:!2023-05-12,263,270!2022-11-08,4,210-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## phenolphthalein

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
data: gen.TextCode = gen.TextCode.compile(
	r'''{mem:_(begin)_}{text:pH | color
-|-
}1~8.3{text: | colorless
}8.3~10{text: | <span style="color\: lightPink;">very pale pink</span>
}10~14{text: | <span style="color\: pink;">pink</span>}{mem:_(end)_}'''
)
sem: gen.TextCode = gen.TextCode.compile(
	r'''colorless{}<span style="color\: lightPink;">very pale pink</span>{}<span style="color\: pink;">pink</span>'''
)
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('5c8883'),
		text=gen.common.quote_text(data),
	),
	gen.Result(
		location=__env__.cwf_section('155d9a'),
		text=gen.common.memorize_linked_seq(data,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('155d9a')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('0245d8'),
		text=gen.common.semantics_seq_map(data, sem,
			reversible=True,
			states=read.read_flashcard_states(__env__.cwf_section('0245d8')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5c8883"--><!-- The following content is generated at 2022-11-05T00:25:01.044870+08:00. Any edits will be overridden! -->

> pH | color
> -|-
> 1~8.3 | colorless
> 8.3~10 | <span style="color: lightPink;">very pale pink</span>
> 10~14 | <span style="color: pink;">pink</span>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="155d9a"--><!-- The following content is generated at 2022-11-05T00:25:01.050869+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←1~8.3 <!--SR:!2022-11-07,6,241!2022-11-24,20,281-->
2. 1~8.3→:::←8.3~10 <!--SR:!2022-11-07,6,241!2022-11-06,5,241-->
3. 8.3~10→:::←10~14 <!--SR:!2022-11-07,6,241!2022-11-07,6,241-->
4. 10~14→:::←_(end)_ <!--SR:!2022-11-24,20,281!2022-11-07,6,241-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="0245d8"--><!-- The following content is generated at 2022-11-05T00:25:01.058870+08:00. Any edits will be overridden! -->

1. 1~8.3:::colorless <!--SR:!2022-11-10,21,210!2022-12-15,56,230-->
2. 8.3~10:::<span style="color: lightPink;">very pale pink</span> <!--SR:!2023-11-01,362,250!2022-11-08,14,230-->
3. 10~14:::<span style="color: pink;">pink</span> <!--SR:!2022-12-10,51,230!2022-11-17,139,230-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
