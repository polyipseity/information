#flashcards/chemistry/atmosphere_of_Earth #academic/chemistry

# atmosphere of Earth

## composition

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
data: gen.TextCode = gen.common.seq_to_code((
	R'N<sub>2</sub>{text:\: 78.084%}',
	R'O<sub>2</sub>{text:\: 20.946%}',
	R'Ar{text:\: 0.9340%}',
	R'CO<sub>2</sub>{text:\: 0.0417% (2022-04-xx)}',
	'{text:_others_}{mem:_others_}{mem lnk:_others_}',),
	index=1,
	prefix='{mem lnk:_(begin)_}',
	suffix='{mem lnk:_(end)_}',)
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
		text=gen.common.memorize_linked_seq(data,
			tag='mem lnk',
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

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a34f1d"--><!-- The following content is generated at 2022-11-05T00:25:01.489869+08:00. Any edits will be overridden! -->

> 1. N<sub>2</sub>: 78.084%
> 2. O<sub>2</sub>: 20.946%
> 3. Ar: 0.9340%
> 4. CO<sub>2</sub>: 0.0417% (2022-04-xx)
> 5. _others_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="123480"--><!-- The following content is generated at 2022-11-05T00:25:01.497870+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←N<sub>2</sub>
2. N<sub>2</sub>→:::←O<sub>2</sub>
3. O<sub>2</sub>→:::←Ar
4. Ar→:::←CO<sub>2</sub>
5. CO<sub>2</sub>→:::←_others_
6. _others_→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1ad236"--><!-- The following content is generated at 2022-11-05T00:25:01.505868+08:00. Any edits will be overridden! -->

1. N<sub>2</sub>::78.084%
2. O<sub>2</sub>::20.946%
3. Ar::0.9340%
4. CO<sub>2</sub>::0.0417% (2022-04-xx)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
