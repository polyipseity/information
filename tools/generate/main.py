import\
    json as _json,\
    logging as _logging,\
    sys as _sys,\
    typing as _typing
from .. import globals as _globals
from .. import utils as _utils
from . import parser as _parser
from . import types as _types_0
from . import writer as _writer


def main(argv: _typing.Sequence[str]) -> None:
    input: ParseArgvDict = parse_argv(argv)
    writers: _writer.Writers = _writer.Writers()
    path: _utils.Path | int
    for path in input['paths']:
        try:
            file: _typing.TextIO = open(
                path, mode='rt', **_globals.open_default_options)
        except OSError:
            _logging.exception(f'Cannot open file: {path}')
            continue
        except ValueError:
            _logging.exception(f'Encoding error opening file: {path}')
            continue
        with file:
            try:
                data_chunks: _typing.Sequence[_types_0.ParsedData] = _parser.parse_file(
                    file)
            except _json.decoder.JSONDecodeError:
                _logging.exception(f'Invalid JSON data in file: {file.name}')
                continue
            except ValueError:
                _logging.exception(f'Invalid file: {file.name}')
                continue
            data: _types_0.ParsedData
            for data in data_chunks:
                writers.add_from(data)
    writer: _writer.Writer
    for writer in writers:
        try:
            writer.write()
        except:
            _logging.exception(f'Error while writing: {writer}')


class ParseArgvDict(_typing.TypedDict):
    paths: _typing.Sequence[_utils.Path | int]


def parse_argv(argv: _typing.Sequence[str]) -> ParseArgvDict:
    paths: _typing.Sequence[_utils.Path | int] = tuple(argv[1:])
    if not paths:
        paths = (_sys.stdin.fileno(),)
    return {'paths': paths}
