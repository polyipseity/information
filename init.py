# -*- coding: UTF-8 -*-
import aiofiles as _aiofiles
import appdirs as _appdirs
import argparse as _argparse
import asyncio as _asyncio
import dataclasses as _dataclasses
import functools as _functools
import inspect as _inspect
import itertools as _itertools
import json as _json
import logging as _logging
import operator as _operator
import os as _os
import pathlib as _pathlib
import shutil as _shutil
import sys as _sys
import types as _types
import typing as _typing


@_typing.final
class _OpenOptions(_typing.TypedDict):
    encoding: str
    errors: _typing.Literal[
        "strict",
        "ignore",
        "replace",
        "surrogateescape",
        "xmlcharrefreplace",
        "backslashreplace",
        "namereplace",
    ]
    newline: None | _typing.Literal["", "\n", "\r", "\r\n"]


open_options: _OpenOptions = _OpenOptions(
    encoding="UTF-8",
    errors="strict",
    newline=None,
)
_local_app_dirs: _appdirs.AppDirs = _appdirs.AppDirs(
    appname="9a27fc39-496b-4b4c-87a7-03b9e88fc6bc",
    appauthor="polyipseity",
    version=None,
    roaming=False,
    multipath=False,
)
_root_dir_excludes: _typing.AbstractSet[str] = frozenset(
    {
        ".git",
        ".obsidian",
        "templates",
        "tools",
    }
)


@_typing.final
@_dataclasses.dataclass(
    init=True,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=False,
    frozen=True,
    match_args=True,
    kw_only=True,
    slots=True,
)
class Arguments:
    prog: str
    cached: bool
    arguments: _typing.Sequence[str]

    def __post_init__(self) -> None:
        object.__setattr__(self, "arguments", tuple(self.arguments))


async def main(args: Arguments) -> _typing.NoReturn:
    try:
        frame: _types.FrameType | None = _inspect.currentframe()
        if frame is None:
            raise ValueError(frame)
        filename: str = _inspect.getframeinfo(frame).filename
        folder: _pathlib.Path = _pathlib.Path(filename).parent.resolve(strict=True)

        local_data_folder: _pathlib.Path = _pathlib.Path(_local_app_dirs.user_data_dir)
        if not args.cached and local_data_folder.exists():
            _shutil.rmtree(local_data_folder, ignore_errors=False)
        local_data_folder.mkdir(parents=True, exist_ok=True)
        local_data_folder = local_data_folder.resolve(strict=True)

        cache_data_path: _pathlib.Path = local_data_folder / "cache.json"
        if not cache_data_path.exists():
            cache_data_path.write_text(
                "", encoding="UTF-8", errors="strict", newline=None
            )
        async with _aiofiles.open(
            cache_data_path, mode="r+t", **open_options
        ) as cache_data:
            try:
                data: _typing.MutableMapping[str, _typing.Any] = _json.loads(
                    await cache_data.read()
                )
            except _json.decoder.JSONDecodeError:
                data = {}
                print("Cache data will be regenerated because it is empty or corrupted")
            finalizers: _typing.MutableSequence[
                _typing.Callable[[], _typing.Awaitable[None]]
            ] = []

            try:
                old_args: _typing.Collection[str] = data["args"]
            except KeyError:
                old_args = ()
            diff_args: bool = any(
                _itertools.starmap(
                    _operator.ne,
                    _itertools.zip_longest(
                        args.arguments, old_args, fillvalue=object()
                    ),
                )
            )
            data["args"] = args.arguments

            def gen_inputs() -> _typing.Iterator[str]:
                mod_times: _typing.MutableMapping[str, int] = data.setdefault(
                    "mod_times", {}
                )

                def on_error(err: OSError) -> None:
                    try:
                        raise err
                    except OSError:
                        _logging.exception("Exception while walking folders")

                root: str
                dirs: _typing.MutableSequence[str]
                files: _typing.Sequence[str]
                for root, dirs, files in _os.walk(
                    folder, topdown=True, onerror=on_error, followlinks=False
                ):
                    if _pathlib.Path(root).resolve(strict=True) == folder:
                        exclude: str
                        for exclude in _root_dir_excludes:
                            try:
                                dirs.remove(exclude)
                            except ValueError:
                                pass
                    file: str
                    for file in files:
                        if file.endswith(".md"):
                            path: str = _os.path.join(root, file)
                            try:
                                if (
                                    diff_args
                                    or mod_times[path] != _os.lstat(path).st_mtime_ns
                                ):
                                    yield path
                            except KeyError:
                                yield path

                            async def finalize(
                                *,
                                __mod_times: _typing.MutableMapping[
                                    str, int
                                ] = mod_times,
                                __path: str = path,
                            ):
                                async with _aiofiles.open(
                                    __path,
                                    mode="r+t",
                                    **{**open_options, "newline": ""},
                                ) as file:
                                    text = await file.read()
                                    seek = file.seek(0)
                                    text = text.replace(_os.linesep, "\n")
                                    await seek
                                    await file.write(text)
                                    await file.truncate()
                                __mod_times[__path] = _os.lstat(__path).st_mtime_ns

                            finalizers.append(finalize)
                mod_times.clear()

            inputs: _typing.Sequence[str] = tuple(gen_inputs())
            print(f"Using {len(inputs)} input(s)")
            success: bool = True
            if inputs:
                try:
                    import tools.pytextgen.main as main

                    entry: _argparse.Namespace = main.parser().parse_args(
                        tuple(
                            _itertools.chain(
                                args.arguments,
                                inputs,
                            )
                        )
                    )
                    await entry.invoke(entry)
                except SystemExit as ex:
                    success = ex.code == 0

            if success:
                await _asyncio.gather(
                    cache_data.seek(0), *(finalizer() for finalizer in finalizers)
                )
                await cache_data.write(
                    _json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2)
                )
                await cache_data.truncate()
    except Exception:
        _logging.exception("Uncaught exception")
    finally:
        print("Press <enter> to exit")
        try:
            input()
        except EOFError:
            pass
    _sys.exit(0)


def parser(
    parent: _typing.Callable[..., _argparse.ArgumentParser] | None = None,
) -> _argparse.ArgumentParser:
    frame: _types.FrameType | None = _inspect.currentframe()
    if frame is None:
        raise ValueError(frame)
    prog: str = _sys.argv[0]

    parser: _argparse.ArgumentParser = (
        _argparse.ArgumentParser if parent is None else parent
    )(
        prog=prog,
        description="input wrapper for tools for notes",
        add_help=True,
        allow_abbrev=False,
        exit_on_error=False,
    )
    c_group = parser.add_mutually_exclusive_group()
    c_group.add_argument(
        "-c",
        "--cached",
        action="store_true",
        default=True,
        help="use cache (default)",
        dest="cached",
    )
    c_group.add_argument(
        "-C",
        "--no-cached",
        action="store_false",
        default=False,
        help="do not use cache",
        dest="cached",
    )
    parser.add_argument(
        "arguments",
        action="store",
        nargs=_argparse.ONE_OR_MORE,
        help="sequence of argument(s) to pass through",
    )

    @_functools.wraps(main)
    async def invoke(args: _argparse.Namespace) -> _typing.NoReturn:
        await main(
            Arguments(
                prog=prog,
                cached=args.cached,
                arguments=args.arguments,
            )
        )

    parser.set_defaults(invoke=invoke)
    return parser


if __name__ == "__main__":
    entry: _argparse.Namespace = parser().parse_args(_sys.argv[1:])
    _asyncio.run(entry.invoke(entry))
