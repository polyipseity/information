#academic/chemistry #flashcards/academic/splint__laboratory_equipment_

# splint

## uses

### glowing splint test

It is a test for an [oxidizing](oxidization.md) gas.

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.gen import memorize_linked_seq, quote_text, seq_to_code
from pytextgen.read import read_flashcard_states
from pytextgen.util import Result, Results
e = __env__
data = seq_to_code(
	(
		'Light a wooden splint.',
		'Blow out the flame.',
		'Introduce the [ember](ember.md) into the gas sample trapped in a container.',
		'Positive: The ember flares and reignites.',
	),
	prefix='{mem:_(begin)_}',
	suffix='{mem:_(suffix)_}',
)
return Results(
	Result(
		location=e.cwf_section('28a383'),
		text=quote_text(data),
	),
	Result(
		location=e.cwf_section('23ba9d'),
		text=memorize_linked_seq(
			data,
			hinted=False,
			states=await read_flashcard_states(e.cwf_section('23ba9d')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="28a383"--><!-- The following content is generated at 2023-03-14T22:56:07.078677+08:00. Any edits will be overridden! -->

> 1. Light a wooden splint.
> 2. Blow out the flame.
> 3. Introduce the [ember](ember.md) into the gas sample trapped in a container.
> 4. Positive: The ember flares and reignites.

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="23ba9d"--><!-- The following content is generated at 2023-03-14T22:56:07.064724+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←Light a wooden splint.
2. Light a wooden splint.→:::←Blow out the flame.
3. Blow out the flame.→:::←Introduce the [ember](ember.md) into the gas sample trapped in a container.
4. Introduce the [ember](ember.md) into the gas sample trapped in a container.→:::←Positive: The ember flares and reignites.
5. Positive: The ember flares and reignites.→:::←_(suffix)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
