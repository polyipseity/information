import argparse as _argparse
import contextlib as _contextlib
import logging as _logging
import os as _os
import pathlib as _pathlib
import sys as _sys
import typing as _typing

from .. import globals as _globals
from .. import version as _version
from . import read as _read
from . import write as _write


def main(argv: _typing.Sequence[str]) -> None:
    args: Arguments = parse_argv(argv)
    writers: _typing.MutableSequence[_write.Writer] = []
    input: _pathlib.PurePath
    for input in args.inputs:
        try:
            file: _typing.TextIO = open(
                input, mode='rt', **_globals.open_options)
        except OSError:
            _logging.exception(f'Cannot open file: {input}')
            continue
        except ValueError:
            _logging.exception(f'Encoding error opening file: {input}')
            continue
        with file:
            try:
                ext: str
                _, ext = _os.path.splitext(input)
                reader: _read.Reader = _read.Reader.registry[ext](
                    path=input,
                    timestamp=args.timestamp,
                )
                reader.read(file.read())
                writers.extend(reader.pipe())
            except BaseException:
                _logging.exception(f'Exception reading file: {input}')
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
class Arguments(_typing.NamedTuple):
    inputs: _typing.Sequence[_pathlib.PurePath]
    timestamp: bool


def parse_argv(argv: _typing.Sequence[str]) -> Arguments | _typing.NoReturn:
    prog0: str | None = _sys.modules[__name__].__package__
    prog: str = prog0 if prog0 else __name__
    del prog0

    parser: _argparse.ArgumentParser = _argparse.ArgumentParser(
        prog=f'python -m {prog}',
        description='generate text from input',
        add_help=True,
        allow_abbrev=True,
        exit_on_error=False,
    )
    parser.add_argument('-v', '--version',
                        action='version',
                        version=f'{prog} v{_version.version}',
                        help='print version and exit',
                        )
    parser.add_argument('-t', '--timestamp',
                        action='store_true',
                        default=True,
                        help='update or write timestamp (default)',
                        dest='timestamp',
                        )
    parser.add_argument('-T', '--no-timestamp',
                        action='store_false',
                        default=False,
                        help='do not update or write timestamp',
                        dest='timestamp',
                        )
    parser.add_argument('inputs',
                        action='store',
                        nargs=_argparse.ONE_OR_MORE,
                        type=_pathlib.PurePath,
                        help='sequence of input(s) to read',
                        )
    input: _argparse.Namespace = parser.parse_args(argv[1:])
    return Arguments(
        inputs=tuple(input.inputs),
        timestamp=input.timestamp,
    )
