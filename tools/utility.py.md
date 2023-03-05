#functional/code

# `utility.py`

## notes

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
from pytextgen import gen as _pytextgen_gen, read as _pytextgen_read, util as _pytextgen_util
import typing as _typing
import zlib as _zlib
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
			id = _zlib.adler32(f"{text}{note}".encode("UTF-8"))
		self.__data.append((text, f"{note} ^{id}"))
		return _pytextgen_gen.TextCode.escape(f"<sup>[{len(self.__data)}](#^{id})</sup>")

	async def text(self, location: _pytextgen_util.Location):
		return _pytextgen_gen.memorize_two_sided(
			_pytextgen_gen.two_columns_to_code(self.data,
				left=lambda n: _pytextgen_gen.TextCode.escape(n[0]),
				right=lambda n: _pytextgen_gen.TextCode.escape(n[1]),
			),
			reversible=True,
			states=await _pytextgen_read.read_flashcard_states(location),
		)
```
