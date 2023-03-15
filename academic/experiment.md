#flashcards/academic/experiment #academic/biology #academic/chemistry #academic/physics

# experiment

## steps

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read, util
data = gen.seq_to_code(
	(
		"Observe",
		"Record",
		"Analyze",
		"Conclude",
	),
	index=1,
	prefix='{mem:_(begin)_}',
	suffix='{mem:_(end)_}',
)
return (
	util.Result(
		location=__env__.cwf_section("d9203e"),
		text=gen.quote_text(data),
	),
	util.Result(
		location=__env__.cwf_section("b923ed"),
		text=gen.memorize_linked_seq(
			data,
			hinted=False,
			states=await read.read_flashcard_states(__env__.cwf_section("b923ed")),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d9203e"--><!-- The following content is generated at 2023-03-12T14:16:16.592826+08:00. Any edits will be overridden! -->

> 1. Observe
> 2. Record
> 3. Analyze
> 4. Conclude

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b923ed"--><!-- The following content is generated at 2023-03-12T14:16:16.582373+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←Observe
2. Observe→:::←Record
3. Record→:::←Analyze
4. Analyze→:::←Conclude
5. Conclude→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
