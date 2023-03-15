#functional/code

# `utility.py`

## utilities

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from pytextgen.util import export_seq
import zlib as _zlib
def fast_hash(string: str):
	return _zlib.adler32(string.encode("UTF-8"))

return export_seq(fast_hash,)
```

## HTML

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
import html as _html
from pytextgen.util import export_seq
import typing as _typing

def html_list(type: _typing.Literal['ol', 'ul'], iter: _typing.Iterable[str], *, escape = True):
	return f"<{type}><li>{'</li><li>'.join(map(_html.escape, iter) if escape else iter)}</li></{type}>"

def html_ol(iter: _typing.Iterable[str], **kwargs):
	return html_list('ol', iter, **kwargs)

def html_ul(iter: _typing.Iterable[str], **kwargs):
	return html_list('ul', iter, **kwargs)

return export_seq(html_list, html_ol, html_ul,)
```

## hard

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from pytextgen import config as _pytextgen_config, gen as _pytextgen_gen
from pytextgen.util import export_seq
def hard(string: str):
	cl, cr = map(_pytextgen_gen.TextCode.escape, _pytextgen_config.CONFIG.cloze_token)
	return f"{{text:{cl}}}{string}{{text:{cr}}}"

return export_seq(hard,)
```

## notes

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from pytextgen import gen as _pytextgen_gen, read as _pytextgen_read, util as _pytextgen_util
from pytextgen.util import export_seq
import typing as _typing
@_typing.final
class Notes:
	__slots__: _typing.ClassVar = ("__data",)

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
		return _pytextgen_gen.TextCode.escape(f"<sup>[{len(self.__data)}](#{id})</sup>")

	async def text(self, location: _pytextgen_util.Location):
		return _pytextgen_gen.memorize_two_sided(
			_pytextgen_gen.two_columns_to_code(self.data,
				left=lambda n: _pytextgen_gen.TextCode.escape(n[0]),
				right=lambda n: _pytextgen_gen.TextCode.escape(n[1]),
			),
			reversible=True,
			states=await _pytextgen_read.read_flashcard_states(location),
		)

return export_seq(Notes,)
```
