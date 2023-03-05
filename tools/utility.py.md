#functional/code

# `utility.py`

## notes

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
import pytextgen.gen as _pytextgen_gen
import typing as _typing
import zlib as _zlib
@_typing.final
class Notes:
	__slots__: _typing.ClassVar = ('__data',)

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
```
