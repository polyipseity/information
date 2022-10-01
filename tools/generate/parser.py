import\
    collections as _collections,\
    json as _json,\
    os as _os,\
    pathlib as _pathlib,\
    sys as _sys
from .. import globals as _globals, utils as _utils
import collections.abc as _
del _


def parse_file(file):
    func = parse_file
    if file.fileno() == _sys.stdin.fileno():
        return (_json.load(file, object_hook=func.object_hooker(file)),)
    name, ext = _os.path.splitext(file.name)
    if ext == '.json':
        return (_json.load(file, object_hook=func.object_hooker(file)),)
    if ext == '.md':
        chunks = []
        text = file.read()
        start = text.find(func.md_start)
        while start != -1:
            end = text.find(func.md_end, start + len(func.md_start))
            if end == -1:
                raise ValueError(f'Unenclosed JSON data block at char {start}')
            chunk = _json.loads(
                text[start + len(func.md_start):end], object_hook=func.object_hooker(file))
            if not isinstance(chunk, _collections.abc.Iterable):
                chunk = (chunk,)
            chunks.append(chunk)
            start = text.find(func.md_start, end + len(func.md_end))
        return tuple(chunks)
    raise ValueError(f'Unrecognized file type: {name}{ext}')


parse_file.md_start = f'%%<!--{_globals.uuid},generate,data-->\n```json'
parse_file.md_end = '```\n%%'


def _(file):
    def _0(obj):
        loc = obj.get('location', dict())
        if 'file' in loc:
            loc['file'] = _pathlib.Path(file.name) / loc['file']
        obj['location'] = _utils.FileTextLocation(**loc)
        return obj
    return _0


parse_file.object_hooker = _
del _
