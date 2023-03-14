#flashcards/academic/atmosphere_of_Earth #academic/chemistry

# atmosphere of Earth

## composition

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read, util
data: gen.TextCode = gen.seq_to_code((
	R'[N<sub>2</sub>](nitrogen.md){text:\: 78.084%}',
	R'[O<sub>2</sub>](oxygen.md){text:\: 20.946%}',
	R'[Ar](argon.md){text:\: 0.9340%}',
	R'[CO<sub>2</sub>](carbon%20dioxide.md){text:\: 0.0417% (2022-04-xx)}',
	'{text:_others_}{mem:_others_}{mem lnk:_others_}',),
	index=1,
	prefix='{mem lnk:_(begin)_}',
	suffix='{mem lnk:_(end)_}',)
sem: gen.TextCode = gen.TextCode.compile(
	'''78.084%{}20.946%{}0.9340%{}0.0417% (2022-04-xx)'''
)
return util.Results(
	util.Result(
		location=__env__.cwf_section('a34f1d'),
		text=gen.quote_text(data),
	),
	util.Result(
		location=__env__.cwf_section('123480'),
		text=gen.memorize_linked_seq(data,
			tag='mem lnk',
			hinted=False,
			states=await read.read_flashcard_states(__env__.cwf_section('123480')),
		),
	),
	util.Result(
		location=__env__.cwf_section('1ad236'),
		text=gen.semantics_seq_map(data, sem,
			states=await read.read_flashcard_states(__env__.cwf_section('1ad236')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a34f1d"--><!-- The following content is generated at 2023-03-14T22:09:57.723829+08:00. Any edits will be overridden! -->

> 1. [N<sub>2</sub>](nitrogen.md): 78.084%
> 2. [O<sub>2</sub>](oxygen.md): 20.946%
> 3. [Ar](argon.md): 0.9340%
> 4. [CO<sub>2</sub>](carbon%20dioxide.md): 0.0417% (2022-04-xx)
> 5. _others_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="123480"--><!-- The following content is generated at 2023-03-14T22:09:57.737978+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[N<sub>2</sub>](nitrogen.md) <!--SR:!2024-11-30,670,270!2024-08-30,680,327-->
2. [N<sub>2</sub>](nitrogen.md)→:::←[O<sub>2</sub>](oxygen.md) <!--SR:!2023-03-26,281,270!2024-03-05,497,267-->
3. [O<sub>2</sub>](oxygen.md)→:::←[Ar](argon.md) <!--SR:!2024-04-29,533,270!2023-09-01,375,267-->
4. [Ar](argon.md)→:::←[CO<sub>2</sub>](carbon%20dioxide.md) <!--SR:!2023-05-15,328,290!2023-03-28,283,270-->
5. [CO<sub>2</sub>](carbon%20dioxide.md)→:::←_others_ <!--SR:!2023-06-14,348,290!2023-08-24,367,267-->
6. _others_→:::←_(end)_ <!--SR:!2024-10-15,785,345!2024-08-16,725,326-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1ad236"--><!-- The following content is generated at 2023-03-14T22:09:57.767517+08:00. Any edits will be overridden! -->

1. [N<sub>2</sub>](nitrogen.md)::78.084% <!--SR:!2023-10-25,370,230-->
2. [O<sub>2</sub>](oxygen.md)::20.946% <!--SR:!2023-03-22,50,190-->
3. [Ar](argon.md)::0.9340% <!--SR:!2023-03-28,142,210-->
4. [CO<sub>2</sub>](carbon%20dioxide.md)::0.0417% (2022-04-xx) <!--SR:!2023-03-17,24,167-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
