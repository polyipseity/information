#functional/code

# `utility.py`

## utilities

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from pytextgen.util import export_seq
from types import MappingProxyType
from typing import Iterable, Mapping, TypeVar
from zlib import adler32

T = TypeVar('T')
U = TypeVar('U')

def fast_hash(string: str):
	return adler32(string.encode("UTF-8"))

def items_to_map(*items: tuple[T, U]) -> Mapping[T, U]:
	return MappingProxyType({key: val for key, val in items})

return export_seq(fast_hash, items_to_map,)
```

## HTML

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from html import escape as h_esc
from pytextgen.util import export_seq
from typing import Iterable, Literal

def html_list(type: Literal['ol', 'ul'], iter: Iterable[str], *, escape = True):
	return f"<{type}><li>{'</li><li>'.join(map(h_esc, iter) if escape else iter)}</li></{type}>"

def html_list2(type: Literal['ol', 'ul'], *args, **kwargs):
	return html_list(type, args, **kwargs)

def html_ol(iter: Iterable[str], **kwargs):
	return html_list('ol', iter, **kwargs)

def html_ol2(*args, **kwargs):
	return html_ol(args, **kwargs)

def html_ul(iter: Iterable[str], **kwargs):
	return html_list('ul', iter, **kwargs)

def html_ul2(*args, **kwargs):
	return html_ul(args, **kwargs)

return export_seq(
	html_list,
	html_list2,
	html_ol,
	html_ol2,
	html_ul,
	html_ul2,
)
```

## hard

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from pytextgen.config import CONFIG
from pytextgen.gen import Tag, TextCode
from pytextgen.util import export_seq

def hard(string: str):
	cl, cr = map(TextCode.escape, CONFIG.cloze_token)
	return f"{{{Tag.TEXT}:{cl}}}{string}{{{Tag.TEXT}:{cr}}}"

return export_seq(hard,)
```

## memorization

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from asyncio import gather
from collections import defaultdict
from itertools import starmap
from pytextgen.config import CONFIG
from pytextgen.gen import Tag, TextCode, cloze_text, memorize_linked_seq, memorize_two_sided, quote_text, rows_to_table, seq_to_code, two_columns_to_code
from pytextgen.read import read_flashcard_states
from pytextgen.util import Location, Result, export_seq, identity
from typing import Any, Callable, Iterable, Mapping, Sequence, TypeVar

T = TypeVar('T')

def cloze(string: str, escape = False):
	cl, cr = CONFIG.cloze_token
	return (TextCode.escape if escape else identity)(f'{cl}{string}{cr}') if string else ''

async def memorize_map(
	locations: tuple[Location, Location, Location],
	data: Mapping[str, str | Iterable[str]],
	*,
	delimiter = ': ',
	joiner = ', ',
	escape = True,
) -> tuple[Result, Result]:
	states = read_states(locations)
	forward = {}
	backward = defaultdict(list)
	for key, vals in data.items():
		if isinstance(vals, str):
			vals = (vals,)
		forward[key] = tuple(vals)
		for val in vals:
			backward[val].append(key)

	def mem(index: int, map_: Mapping[str, Iterable[str]]):
		escaper = TextCode.escape if escape else identity
		return Result(
			location=locations[index],
			text=memorize_two_sided(
				two_columns_to_code(
					map_.items(),
					left=lambda data: escaper(data[0]),
					right=lambda data: joiner.join(map(escaper, data[1])),
				),
				empty=True,
				reversible=False,
				states=states[index],
			),
		)

	def quote():
		return Result(
			location=locations[0],
			text=cloze_text(
				seq_to_code(
					(delimiter.join((key, joiner.join(val),)) for key, val in forward.items()),
					escape=escape,
				),
				states=states[0],
			),
		)

	states = await states
	return (
		quote(),
		mem(1, forward),
		mem(2, backward),
	)

async def memorize_seq(
	locations: tuple[Location, Location],
	seq: Iterable[str],
	*,
	prefix = f'{{{Tag.MEMORIZE}:_(begin)_}}',
	suffix = f'{{{Tag.MEMORIZE}:_(end)_}}',
	escape = True,
) -> tuple[Result, Result]:
	states = read_states(locations)
	code = seq_to_code(
		seq,
		prefix=prefix,
		suffix=suffix,
		escape=escape,
	)
	states = await states
	return (
		Result(
			location=locations[0],
			text=cloze_text(
				code,
				states=states[0],
			),
		),
		Result(
			location=locations[1],
			text=memorize_linked_seq(
				code,
				hinted=False,
				states=states[1],
			),
		),
	)

async def memorize_table(
	locations: tuple[Location, Location],
	headers: Iterable[str],
	data: Iterable[T],
	transformer: Callable[[T], Iterable[Any]] = lambda data: data if isinstance(data, Iterable) else (data,),
	*,
	prefix = f'{{{Tag.MEMORIZE}:_(begin)_}}',
	suffix = f'{{{Tag.MEMORIZE}:_(end)_}}',
	escape = True,
) -> tuple[Result, Result]:
	states = read_states(locations)
	escaper = TextCode.escape if escape else identity
	states = await states
	return (
		Result(
			location=locations[0],
			text=cloze_text(
				TextCode.compile(rows_to_table(
					data,
					names=map(escaper, headers),
					values=lambda data: map(escaper, transformer(data)),
				)),
				states=states[0],
			),
		),
		Result(
			location=locations[1],
			text=memorize_linked_seq(
				seq_to_code(
					map(lambda datum: escaper(datum[0]), data),
					prefix=prefix,
					suffix=suffix,
				),
				hinted=False,
				states=states[1],
			),
		),
	)

async def read_states(locations: Iterable[Location]):
	return await gather(*map(read_flashcard_states, locations))

return export_seq(
	cloze, 
	memorize_map,
	memorize_seq,
	memorize_table,
	read_states,
)
```

## notes

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from pytextgen.gen import TextCode, memorize_two_sided, two_columns_to_code
from pytextgen.read import read_flashcard_states
from pytextgen.util import Location, export_seq
from typing import ClassVar, final

@final
class Notes:
	__slots__: ClassVar = ("__data",)

	def __init__(self):
		self.__data = []

	@property
	def data(self):
		return tuple(self.__data)

	def embed(self, text: str, note: str, id: str | None = None):
		if id is None:
			id = f"{fast_hash(f'{text}{note}'):x}"
		id = f"^note-{id}"
		self.__data.append((text, f"{note} {id}"))
		return TextCode.escape(f"<sup>[{len(self.__data)}](#{id})</sup>")

	async def text(self, location: Location):
		return memorize_two_sided(
			two_columns_to_code(self.data,
				left=lambda n: TextCode.escape(n[0]),
				right=lambda n: TextCode.escape(n[1]),
			),
			reversible=True,
			states=await read_flashcard_states(location),
		)

return export_seq(Notes,)
```

## tags

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from enum import StrEnum, unique
from pytextgen.util import export_seq
from typing import ClassVar, final

@final
@unique
class Tags(StrEnum):
	__slots__: ClassVar = ()

	MEMORIZE_LINKED: ClassVar = 'mem lnk'

return export_seq(Tags,)
```
