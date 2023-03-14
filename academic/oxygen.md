#academic/chemistry #flashcards/academic/oxygen

# oxygen

## uses

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read
from pytextgen.config import CONFIG
from pytextgen.gen import Tag, TextCode
from pytextgen.util import Result, Results
e = __env__
cl, cr = CONFIG.cloze_token
data = (
	('breathing', '',),
	('burning of fuels', '',),
	('medical use', '',),
)
return Results(
	Result(
		location=e.cwf_section('923dac'),
		text=gen.cloze_text(
			TextCode.compile(gen.rows_to_table(
				data,
				names=('name', 'description',),
				values=lambda datum: (TextCode.escape(f'{cl}{field}{cr}') if field else '' for field in datum),
			)),
			states=await read.read_flashcard_states(e.cwf_section('923dac')),
		),
	),
	Result(
		location=e.cwf_section('aaee9e'),
		text=gen.memorize_linked_seq(
			gen.seq_to_code(
				map(lambda datum: TextCode.escape(datum[0]), data),
				prefix=f'{{{Tag.MEMORIZE}:_(begin)_}}',
				suffix=f'{{{Tag.MEMORIZE}:_(end)_}}',
			),
			hinted=False,
			states=await read.read_flashcard_states(e.cwf_section('aaee9e')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="923dac"--><!-- The following content is generated at 2023-03-14T22:39:01.193958+08:00. Any edits will be overridden! -->

> name | description
> -|-
> {{breathing}} |
> {{burning of fuels}} |
> {{medical use}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="aaee9e"--><!-- The following content is generated at 2023-03-14T22:39:01.204551+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←breathing
2. breathing→:::←burning of fuels
3. burning of fuels→:::←medical use
4. medical use→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## tests

### glowing splint

See [glowing splint test](splint%20(laboratory%20equipment).md#glowing%20splint%20test).
