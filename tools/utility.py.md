---
aliases:
  - utility.py
  - utility.py.md
tags:
  - function/code
  - language/in/English
---

# `utility.py`

## utilities

```Python
# pytextgen generate module
from pytextgen.compat.util import export_seq
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
# pytextgen generate module
from html import escape as h_esc
from pytextgen.compat.util import export_seq
from typing import Iterable, Literal

def colored_block(color: str) -> str:
  return f'<span style="background-color:{color};border:1px solid black;color:white;display:inline-block;height:1.25em;line-height:1.25;margin:1px 0;min-width:1.25em;text-align:center;">&nbsp;</span>'

def html_list0(type: Literal['ol', 'ul'], iter: Iterable[str], *, escape = True):
  return f"<{type}><li>{'</li><li>'.join(map(h_esc, iter) if escape else iter)}</li></{type}>"

def html_list(type: Literal['ol', 'ul'], *args, **kwargs):
  return html_list0(type, args, **kwargs)

def html_ol0(iter: Iterable[str], **kwargs):
  return html_list0('ol', iter, **kwargs)

def html_ol(*args, **kwargs):
  return html_ol0(args, **kwargs)

def html_ul0(iter: Iterable[str], **kwargs):
  return html_list0('ul', iter, **kwargs)

def html_ul(*args, **kwargs):
  return html_ul0(args, **kwargs)

return export_seq(
  colored_block,
  html_list0,
  html_list,
  html_ol0,
  html_ol,
  html_ul0,
  html_ul,
)
```

## hard

```Python
# pytextgen generate module
from pytextgen.compat.config import CONFIG
from pytextgen.compat.gen import Tag, TextCode
from pytextgen.compat.util import export_seq

def hard(string: str):
  cl, cr = map(TextCode.escape, CONFIG.cloze_token)
  return f"{{{Tag.TEXT}:{cl}}}{string}{{{Tag.TEXT}:{cr}}}"

return export_seq(hard,)
```

## memorization

```Python
# pytextgen generate module
from asyncio import gather
from collections import defaultdict
from itertools import starmap
from pytextgen.compat.config import CONFIG
from pytextgen.compat.gen import Tag, TextCode, cloze_text, memorize_linked_seq, memorize_two_sided, quote_text, rows_to_table, seq_to_code, two_columns_to_code
from pytextgen.compat.read import read_flashcard_states
from pytextgen.compat.util import Location, Result, export_seq, identity
from typing import Any, Callable, Iterable, Mapping, Sequence, TypeVar

T = TypeVar('T')

def _prefix_or_pretext(prefix: None | str, pretext: str):
  if prefix is None:
    return f'{{{Tag.MEMORIZE}:_({TextCode.escape(pretext or "begin")})_}}'
  if pretext:
    raise ValueError(pretext)
  return prefix

def _suffix_or_posttext(suffix: None | str, posttext: str):
  if suffix is None:
    return f'{{{Tag.MEMORIZE}:_({TextCode.escape(posttext or "end")})_}}'
  if posttext:
    raise ValueError(posttext)
  return suffix

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
  escape: bool = True,
  pretext: str = '',
  posttext: str = '',
  prefix: None | str = None,
  suffix: None | str = None,
) -> tuple[Result, Result]:
  prefix, suffix = _prefix_or_pretext(prefix, pretext), _suffix_or_posttext(suffix, posttext)
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
  escape = True,
  pretext: str = '',
  posttext: str = '',
  prefix: None | str = None,
  suffix: None | str = None,
  use_compiled_len: bool = False,
  use_visible_len: bool = False,
) -> tuple[Result, Result]:
  prefix, suffix = _prefix_or_pretext(prefix, pretext), _suffix_or_posttext(suffix, posttext)
  states = read_states(locations)
  escaper = TextCode.escape if escape else identity
  states = await states
  return (
    Result(
      location=locations[0],
      text=cloze_text(
        TextCode.compile(escaper(rows_to_table(
          data,
          names=headers,
          values=lambda data: transformer(data),
          escape=escape,
          use_compiled_len=use_compiled_len,
          use_visible_len=use_visible_len,
        ))),
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
# pytextgen generate module
from pytextgen.compat.gen import TextCode, memorize_two_sided, two_columns_to_code
from pytextgen.compat.read import read_flashcard_states
from pytextgen.compat.util import Location, export_seq
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
    self.__data.append((text, f'{note} <a id="{id}"></a>{id}'))
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
# pytextgen generate module
from enum import StrEnum, unique
from pytextgen.compat.util import export_seq
from typing import ClassVar, final

@final
@unique
class Tags(StrEnum):
  __slots__: ClassVar = ()

  MEMORIZE_LINKED: ClassVar = 'mem lnk'

return export_seq(Tags,)
```
