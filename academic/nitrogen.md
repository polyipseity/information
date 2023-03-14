#academic/chemistry #flashcards/academic/nitrogen

# nitrogen

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
	('food packaging', 'To prevent [food spoilage](food%20spoilage.md).',),
	('making [ammonia](ammonia.md)', '',),
	('[refrigerant](refrigerant.md)', '',),
)
return Results(
	Result(
		location=e.cwf_section('293850'),
		text=gen.cloze_text(
			TextCode.compile(gen.rows_to_table(
				data,
				names=('name', 'description',),
				values=lambda datum: (TextCode.escape(f'{cl}{field}{cr}') if field else '' for field in datum),
			)),
			states=await read.read_flashcard_states(e.cwf_section('293850')),
		),
	),
	Result(
		location=e.cwf_section('232ba1'),
		text=gen.memorize_linked_seq(
			gen.seq_to_code(
				map(lambda datum: TextCode.escape(datum[0]), data),
				prefix=f'{{{Tag.MEMORIZE}:_(begin)_}}',
				suffix=f'{{{Tag.MEMORIZE}:_(end)_}}',
			),
			hinted=False,
			states=await read.read_flashcard_states(e.cwf_section('232ba1')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="293850"--><!-- The following content is generated at 2023-03-14T22:44:07.536441+08:00. Any edits will be overridden! -->

> name | description
> -|-
> {{food packaging}} | {{To prevent [food spoilage](food%20spoilage.md).}}
> {{making [ammonia](ammonia.md)}} |
> {{[refrigerant](refrigerant.md)}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="232ba1"--><!-- The following content is generated at 2023-03-14T22:44:07.551779+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←food packaging
2. food packaging→:::←making [ammonia](ammonia.md)
3. making [ammonia](ammonia.md)→:::←[refrigerant](refrigerant.md)
4. [refrigerant](refrigerant.md)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
