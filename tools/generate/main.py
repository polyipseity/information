import\
    json as _json,\
    logging as _logging,\
    sys as _sys,\
    types as _types
from .. import globals as _globals
from . import parser as _parser, writer as _writer


def main(argv):
    input = parse_argv(argv)
    writers = _writer.Writers()
    for path in input['paths']:
        try:
            file = open(path, mode='rt', **_globals.open_default_options)
        except OSError:
            _logging.exception(f'Cannot open file: {path}')
            continue
        except ValueError:
            _logging.exception(f'Encoding error opening file: {path}')
            continue
        with file:
            try:
                data_chunks = _parser.parse_file(file)
            except _json.decoder.JSONDecodeError:
                _logging.exception(f'Invalid JSON data in file: {file.name}')
                continue
            except ValueError:
                _logging.exception(f'Invalid file: {file.name}')
                continue
            for data in data_chunks:
                writers.add_from(data)
    for writer in writers:
        try:
            writer.write()
        except:
            _logging.exception(f'Error while writing: {writer}')


def parse_argv(argv):
    paths = tuple(argv[1:])
    if not paths:
        paths = (_sys.stdin.fileno(),)
    return _types.MappingProxyType({'paths': paths})
