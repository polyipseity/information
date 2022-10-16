import contextlib as _contextlib
import logging as _logging
import os as _os
import pathlib as _pathlib
import typing as _typing

from .. import globals as _globals
from . import read as _read
from . import write as _write


def main(argv: _typing.Sequence[str]) -> None:
    input: ParseArgvDict = parse_argv(argv)
    writers: _typing.MutableSequence[_write.Writer] = []
    path: _pathlib.PurePath
    for path in input.paths:
        try:
            file: _typing.TextIO = open(
                path, mode='rt', **_globals.open_options)
        except OSError:
            _logging.exception(f'Cannot open file: {path}')
            continue
        except ValueError:
            _logging.exception(f'Encoding error opening file: {path}')
            continue
        with file:
            try:
                ext: str
                _, ext = _os.path.splitext(path)
                reader: _read.Reader = _read.Reader.registry[ext](
                    path=path)
                reader.read(file.read())
                writers.extend(reader.pipe())
            except BaseException:
                _logging.exception(f'Exception reading file: {path}')
                continue

    writer_stack: _contextlib.ExitStack = _contextlib.ExitStack().__enter__()
    try:
        writer: _write.Writer
        for writer in writers:
            try:
                writer_stack.enter_context(writer.write())
            except:
                _logging.exception(f'Error while validation: {writer}')
                continue
    finally:
        try:
            writer_stack.close()
        except:
            _logging.exception(f'Error while writing')


@_typing.final
class ParseArgvDict(_typing.NamedTuple):
    paths: _typing.Sequence[_pathlib.PurePath]


def parse_argv(argv: _typing.Sequence[str]) -> ParseArgvDict:
    return ParseArgvDict(paths=tuple(_pathlib.PurePath(path) for path in argv[1:]))
