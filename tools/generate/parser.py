import\
    json as _json,\
    os as _os,\
    pathlib as _pathlib,\
    sys as _sys,\
    typing as _typing
from .. import globals as _globals, utils as _utils
from . import types as _types_0
import collections.abc as _
del _

_md_start: str = f'%%<!--{_globals.uuid},generate,data-->\n```json'
_md_end: str = '```\n%%'


def _object_hooker(file: _typing.IO[_typing.Any]) -> _typing.Callable[[_typing.Dict[str, _typing.Any]], _typing.Any]:
    def _0(obj: _typing.Dict[str, _typing.Any]) -> _typing.Any:
        try:
            loc: _typing.Dict[str, _typing.Any] = obj['location']
            try:
                loc['file'] = _pathlib.Path(file.name) / loc['file']
            except KeyError:
                pass
            obj['location'] = _utils.FileTextLocation(**loc)
        except KeyError:
            obj['location'] = _utils.FileTextLocation()
        return obj
    return _0


def parse_file(file: _typing.TextIO) -> _typing.Sequence[_types_0.ParsedData | _typing.Sequence[_types_0.ParsedData]]:
    if file.fileno() == _sys.stdin.fileno():
        return (_json.load(file, object_hook=_object_hooker(file)),)
    name: str
    ext: str
    name, ext = _os.path.splitext(file.name)
    if ext == '.json':
        return (_json.load(file, object_hook=_object_hooker(file)),)
    if ext == '.md':
        chunks: _typing.MutableSequence[_types_0.ParsedData |
                                        _typing.Sequence[_types_0.ParsedData]] = []
        text: str = file.read()
        start: int = text.find(_md_start)
        while start != -1:
            end: int = text.find(_md_end, start + len(_md_start))
            if end == -1:
                raise ValueError(f'Unenclosed JSON data block at char {start}')
            chunk: _types_0.ParsedData = _json.loads(
                text[start + len(_md_start):end], object_hook=_object_hooker(file))
            chunks.append(chunk)
            start = text.find(_md_start, end + len(_md_end))
        return tuple(chunks)
    raise ValueError(f'Unrecognized file type: {name}{ext}')
