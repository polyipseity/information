# -*- coding: UTF-8 -*-
import aioshutil as _aioshutil
import anyio as _anyio
import asyncstdlib as _asyncstdlib
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
import sys as _sys
from tools.pytextgen import (
    globals as _pytextgen_globals,
    main as _pytextgen_main,
    util as _pytextgen_util,
)
import types as _types
import typing as _typing

_LOCAL_APP_DIRS = _appdirs.AppDirs(
    appname="9a27fc39-496b-4b4c-87a7-03b9e88fc6bc",
    appauthor="polyipseity",
    version=None,
    roaming=False,
    multipath=False,
)
_ROOT_DIR_EXCLUDES: _typing.AbstractSet[str] = frozenset(
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
        filename = _inspect.getframeinfo(frame).filename
        folder = _anyio.Path(filename).parent

        local_data_folder = _anyio.Path(_LOCAL_APP_DIRS.user_data_dir)
        if not args.cached and await local_data_folder.exists():
            await _aioshutil.rmtree(local_data_folder, ignore_errors=False)
        await local_data_folder.mkdir(parents=True, exist_ok=True)

        cache_data_path = local_data_folder / "cache.json"
        if not await cache_data_path.exists():
            await cache_data_path.write_text(
                "", encoding="UTF-8", errors="strict", newline=None
            )
        async with await _anyio.open_file(
            cache_data_path,
            mode="r+t",
            **_pytextgen_globals.OPEN_OPTIONS,
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

            async def gen_inputs():
                cache: _typing.MutableMapping[str, tuple[int, str]] = data.setdefault(
                    "cache", {}
                )

                def on_error(err: OSError) -> None:
                    try:
                        raise err
                    except OSError:
                        _logging.exception("Exception while walking folders")

                async def maybe_yield(path: str):
                    def finalizer():
                        async def impl():
                            async with await _anyio.open_file(
                                path,
                                mode="r+t",
                                **{
                                    **_pytextgen_globals.OPEN_OPTIONS,
                                    "newline": "",
                                },
                            ) as file:
                                text = await file.read()
                                async with _asyncio.TaskGroup() as group:
                                    group.create_task(file.seek(0))
                                    text = text.replace(_os.linesep, "\n")
                                await file.write(text)
                                await file.truncate()
                            cache[path] = (
                                (
                                    await _pytextgen_util.asyncify(_os.lstat)(path)
                                ).st_mtime_ns,
                                text,
                            )

                        del cache[path]
                        return impl

                    if diff_args:
                        return finalizer()
                    try:
                        c_mtime, c_text = cache[path]
                    except KeyError:
                        return finalizer()
                    if (
                        await _pytextgen_util.asyncify(_os.lstat)(path)
                    ).st_mtime_ns != c_mtime:
                        async with await _anyio.open_file(
                            path,
                            mode="rt",
                            **{
                                **_pytextgen_globals.OPEN_OPTIONS,
                                "newline": "",
                            },
                        ) as io:
                            text = await io.read()
                        if text != c_text:
                            return finalizer()

                for root, dirs, files in _os.walk(
                    folder, topdown=True, onerror=on_error, followlinks=False
                ):
                    if await folder.samefile(root):
                        for exclude in _ROOT_DIR_EXCLUDES:
                            try:
                                dirs.remove(exclude)
                            except ValueError:
                                pass
                    for file in files:
                        if file.endswith(".md"):
                            path = _os.path.join(root, file)
                            finalize = await maybe_yield(path)
                            if finalize is not None:
                                finalizers.append(finalize)
                                yield path

            inputs = await _asyncstdlib.tuple(gen_inputs())
            print(f"Using {len(inputs)} input(s)")
            success: bool = True
            if inputs:
                try:
                    entry: _argparse.Namespace = _pytextgen_main.parser().parse_args(
                        tuple(
                            _itertools.chain(
                                args.arguments,
                                ("--",),
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
        description="input wrapper for tools",
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
