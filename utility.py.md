#functional/code

# `utility.py`

## utilities

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from pytextgen.util import export_seq
from zlib import adler32

def fast_hash(string: str):
	return adler32(string.encode("UTF-8"))

return export_seq(fast_hash,)
```

## HTML

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from html import escape as h_esc
from pytextgen.util import export_seq
from typing import Iterable, Literal

def html_list(type: Literal['ol', 'ul'], iter: Iterable[str], *, escape = True):
	return f"<{type}><li>{'</li><li>'.join(map(h_esc, iter) if escape else iter)}</li></{type}>"

def html_ol(iter: Iterable[str], **kwargs):
	return html_list('ol', iter, **kwargs)

def html_ul(iter: Iterable[str], **kwargs):
	return html_list('ul', iter, **kwargs)

return export_seq(html_list, html_ol, html_ul,)
```

## hard

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from pytextgen.config import CONFIG
from pytextgen.gen import TextCode
from pytextgen.util import export_seq

def hard(string: str):
	cl, cr = map(TextCode.escape, CONFIG.cloze_token)
	return f"{{text:{cl}}}{string}{{text:{cr}}}"

return export_seq(hard,)
```

## memorization

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from pytextgen.config import CONFIG
from pytextgen.gen import Tag, TextCode, cloze_text, memorize_linked_seq, quote_text, rows_to_table, seq_to_code
from pytextgen.read import read_flashcard_states
from pytextgen.util import Location, Result, export_seq, identity
from typing import Any, Callable, Iterable, Sequence, TypeVar

T = TypeVar('T')

def cloze(string: str, escape = False):
	cl, cr = CONFIG.cloze_token
	return (TextCode.escape if escape else identity)(f'{cl}{string}{cr}') if string else ''

async def memorize_steps(
	locations: tuple[Location, Location],
	seq: Iterable[str],
	*,
	prefix = f'{{{Tag.MEMORIZE}:_(begin)_}}',
	suffix = f'{{{Tag.MEMORIZE}:_(end)_}}',
	escape = True,
	**kwargs
) -> tuple[Result, Result]:
	code = seq_to_code(
		seq,
		prefix=prefix,
		suffix=suffix,
		escape=escape,
		**kwargs,
	)
	return (
		Result(
			location=locations[0],
			text=cloze_text(
				code,
				states=await read_flashcard_states(locations[0]),
			),
		),
		Result(
			location=locations[1],
			text=memorize_linked_seq(
				code,
				hinted=False,
				states=await read_flashcard_states(locations[1]),
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
	escaper = TextCode.escape if escape else identity
	return (
		Result(
			location=locations[0],
			text=cloze_text(
				TextCode.compile(rows_to_table(
					data,
					names=map(escaper, headers),
					values=lambda data: map(escaper, transformer(data)),
				)),
				states=await read_flashcard_states(locations[0]),
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
				states=await read_flashcard_states(locations[1]),
			),
		),
	)

return export_seq(cloze, memorize_steps, memorize_table,)
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
