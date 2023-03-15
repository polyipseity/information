#academic/geology #academic/geophysics #flashcards/academic/internal_structure_of_Earth

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# internal structure of Earth

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read
from pytextgen.config import CONFIG
from pytextgen.gen import Tag, TextCode
from pytextgen.util import Result
e = __env__
cl, cr = CONFIG.cloze_token
data = (
	('[atmosphere](atmosphere%20of%20Earth.md)', html_ul(('~80 km thick', 'gas',),),),
	('[crust](crust.md)', html_ul(('~5–70 km thick', 'solid [rock](rock.md)',),),),
	('[mantle](mantle.md)', html_ul(('~2900 km thick', 'solid, dense rock',),),),
	('[outer core](outer%20core.md)', html_ul(('very dense liquid rock', 'high [temperature](temperature.md)',),),),
	('[inner core](inner%20core.md)', html_ul(('very dense solid rock', 'very high temperature and [pressure](pressure.md)',),),),
)
return (
	Result(
		location=e.cwf_section('2182ff'),
		text=gen.cloze_text(
			TextCode.compile(gen.rows_to_table(
				data,
				names=('name', 'description',),
				values=lambda data: (TextCode.escape(f'{cl}{datum}{cr}') for datum in data),
			)),
			states=await read.read_flashcard_states(e.cwf_section('2182ff')),
		),
	),
	Result(
		location=e.cwf_section('239e8f'),
		text=gen.memorize_linked_seq(
			gen.seq_to_code(
				map(lambda datum: TextCode.escape(datum[0]), data),
				prefix=f'{{{Tag.MEMORIZE}:_(exterior)_}}',
				suffix=f'{{{Tag.MEMORIZE}:_(interior)_}}',
			),
			hinted=False,
			states=await read.read_flashcard_states(e.cwf_section('239e8f')),
		),
	),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2182ff"--><!-- The following content is generated at 2023-03-14T20:25:01.586205+08:00. Any edits will be overridden! -->

> name | description
> -|-
> {{[atmosphere](atmosphere%20of%20Earth.md)}} | {{<ul><li>~80 km thick</li><li>gas</li></ul>}}
> {{[crust](crust.md)}} | {{<ul><li>~5–70 km thick</li><li>solid [rock](rock.md)</li></ul>}}
> {{[mantle](mantle.md)}} | {{<ul><li>~2900 km thick</li><li>solid, dense rock</li></ul>}}
> {{[outer core](outer%20core.md)}} | {{<ul><li>very dense liquid rock</li><li>high [temperature](temperature.md)</li></ul>}}
> {{[inner core](inner%20core.md)}} | {{<ul><li>very dense solid rock</li><li>very high temperature and [pressure](pressure.md)</li></ul>}}

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="239e8f"--><!-- The following content is generated at 2023-03-14T20:25:01.566163+08:00. Any edits will be overridden! -->

1. _(exterior)_→:::←[atmosphere](atmosphere%20of%20Earth.md)
2. [atmosphere](atmosphere%20of%20Earth.md)→:::←[crust](crust.md)
3. [crust](crust.md)→:::←[mantle](mantle.md)
4. [mantle](mantle.md)→:::←[outer core](outer%20core.md)
5. [outer core](outer%20core.md)→:::←[inner core](inner%20core.md)
6. [inner core](inner%20core.md)→:::←_(interior)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->
