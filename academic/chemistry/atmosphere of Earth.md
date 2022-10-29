#flashcards/chemistry/atmosphere_of_Earth #academic/chemistry

# atmosphere of Earth

## composition

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
data: gen.TextCode = gen.common.seq_to_code((
	r'N<sub>2</sub>{text:\: 78.084%}',
	r'O<sub>2</sub>{text:\: 20.946%}',
	r'Ar{text:\: 0.9340%}',
	r'CO<sub>2</sub>{text:\: 0.0417% (2022-04-xx)}',
	'{text:_others_}{mem:_others_}',), index=1)
data_affixed: gen.TextCode = gen.affix_code(data,
	prefix='{mem:_(begin)_}', suffix='{mem:_(end)_}',)
sem: gen.TextCode = gen.TextCode.compile(
	'''78.084%{}20.946%{}0.9340%{}0.0417% (2022-04-xx)'''
)
__env__.result = gen.Results(
	gen.Result(
		location=__env__.cwf_section('a34f1d'),
		text=gen.common.quote_text(data),
	),
	gen.Result(
		location=__env__.cwf_section('123480'),
		text=gen.common.memorize_linked_seq(data_affixed,
			hinted=False,
			states=read.read_flashcard_states(__env__.cwf_section('123480')),
		),
	),
	gen.Result(
		location=__env__.cwf_section('1ad236'),
		text=gen.common.semantics_seq_map(data, sem,
			states=read.read_flashcard_states(__env__.cwf_section('1ad236')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a34f1d"--><!-- The following content is generated at 2022-10-30T00:35:00.498209+08:00. Any edits will be overridden! -->

> 1. N<sub>2</sub>: 78.084%
> 2. O<sub>2</sub>: 20.946%
> 3. Ar: 0.9340%
> 4. CO<sub>2</sub>: 0.0417% (2022-04-xx)
> 5. _others_
<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="123480"--><!-- The following content is generated at 2022-10-30T00:35:00.506207+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←N<sub>2</sub> <!--SR:!2023-01-30,248,270!2024-08-30,680,327-->
2. N<sub>2</sub>→:::←O<sub>2</sub> <!--SR:!2023-03-26,281,270!2024-03-05,497,267-->
3. O<sub>2</sub>→:::←Ar <!--SR:!2022-11-10,196,270!2023-09-01,375,267-->
4. Ar→:::←CO<sub>2</sub> <!--SR:!2023-05-15,328,290!2023-03-28,283,270-->
5. CO<sub>2</sub>→:::←_others_ <!--SR:!2023-06-14,348,290!2023-08-24,367,267-->
6. _others_→:::←_(end)_ <!--SR:!2024-10-15,785,345!2024-08-16,725,326-->
<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1ad236"--><!-- The following content is generated at 2022-10-30T00:35:00.514206+08:00. Any edits will be overridden! -->

1. N<sub>2</sub>::78.084% <!--SR:!2023-10-25,370,230-->
2. O<sub>2</sub>::20.946% <!--SR:!2022-10-30,10,210-->
3. Ar::0.9340% <!--SR:!2022-11-06,68,210-->
4. CO<sub>2</sub>::0.0417% (2022-04-xx) <!--SR:!2023-01-04,76,207-->
<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
