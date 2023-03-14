#academic/chemistry #academic/physics #flashcards/academic/physical_property

# physical property

A __physical property__ is {{a [property](property.md) measurable without [chemical reactions](chemical%20reaction.md)}}. It is contrasted with {{[chemical property](chemical%20property.md)}}

## examples

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
	('[boiling point](boiling%20point.md)', '',),
	('[color](color.md)', '',),
	('[density](density.md)', '',),
	('[ductility](ductility.md)', '',),
	('[electrical conductivity](electrical%20conductivity.md)',),
	('[hardness](hardness.md)', '',),
	('[malleability](malleability.md)', '',),
	('[melting point](melting%20point.md)', '',),
	('[odor](odor.md)', '',),
	('[physical state](physical%20state.md)', '',),
	('[solubility](solubility.md)', 'Varies with [solvent](solvent.md).',),
	('[taste](taste.md)', '',),
	('[thermal conductivity](thermal%20conductivity.md)', '',),
)
return Results(
	Result(
		location=e.cwf_section('1238ff'),
		text=gen.cloze_text(
			TextCode.compile(gen.rows_to_table(
				data,
				names=('name', 'description',),
				values=lambda datum: (TextCode.escape(f'{cl}{field}{cr}') if field else '' for field in datum),
			)),
			states=await read.read_flashcard_states(e.cwf_section('1238ff')),
		),
	),
	Result(
		location=e.cwf_section('bad29e'),
		text=gen.memorize_linked_seq(
			gen.seq_to_code(
				map(lambda datum: TextCode.escape(datum[0]), data),
				prefix=f'{{{Tag.MEMORIZE}:_(begin)_}}',
				suffix=f'{{{Tag.MEMORIZE}:_(end)_}}',
			),
			hinted=False,
			states=await read.read_flashcard_states(e.cwf_section('bad29e')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1238ff"--><!-- The following content is generated at 2023-03-14T20:27:23.376512+08:00. Any edits will be overridden! -->

> name | description
> -|-
> {{[boiling point](boiling%20point.md)}} |
> {{[color](color.md)}} |
> {{[density](density.md)}} |
> {{[ductility](ductility.md)}} |
> {{[electrical conductivity](electrical%20conductivity.md)}}
> {{[hardness](hardness.md)}} |
> {{[malleability](malleability.md)}} |
> {{[melting point](melting%20point.md)}} |
> {{[odor](odor.md)}} |
> {{[physical state](physical%20state.md)}} |
> {{[solubility](solubility.md)}} | {{Varies with [solvent](solvent.md).}}
> {{[taste](taste.md)}} |
> {{[thermal conductivity](thermal%20conductivity.md)}} |

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="bad29e"--><!-- The following content is generated at 2023-03-14T20:27:23.388951+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[boiling point](boiling%20point.md)
2. [boiling point](boiling%20point.md)→:::←[color](color.md)
3. [color](color.md)→:::←[density](density.md)
4. [density](density.md)→:::←[ductility](ductility.md)
5. [ductility](ductility.md)→:::←[electrical conductivity](electrical%20conductivity.md)
6. [electrical conductivity](electrical%20conductivity.md)→:::←[hardness](hardness.md)
7. [hardness](hardness.md)→:::←[malleability](malleability.md)
8. [malleability](malleability.md)→:::←[melting point](melting%20point.md)
9. [melting point](melting%20point.md)→:::←[odor](odor.md)
10. [odor](odor.md)→:::←[physical state](physical%20state.md)
11. [physical state](physical%20state.md)→:::←[solubility](solubility.md)
12. [solubility](solubility.md)→:::←[taste](taste.md)
13. [taste](taste.md)→:::←[thermal conductivity](thermal%20conductivity.md)
14. [thermal conductivity](thermal%20conductivity.md)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
