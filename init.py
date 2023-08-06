# -*- coding: UTF-8 -*-
import aioshutil as _aioshutil
import anyio as _anyio
import asyncstdlib as _asyncstdlib
import appdirs as _appdirs  # type: ignore
import argparse as _argparse
import asyncio as _asyncio
import collections as _collections
import dataclasses as _dataclasses
import functools as _functools
from importlib import abc as _importlib_abc, util as _importlib_util
import inspect as _inspect
import itertools as _itertools
import json as _json
from logging import INFO as _INFO, basicConfig as _basicConfig, getLogger as _getLogger
import operator as _operator
import os as _os
import pathlib as _pathlib
import sys as _sys
import types as _types
import typing as _typing


@_typing.final
class ToolsPathEntryFinder(_importlib_abc.PathEntryFinder):
    __slots__: _typing.ClassVar = ("__path",)
    PREFIX: _typing.ClassVar = "tools"

    def __init__(self, path: _pathlib.Path):
        self.__path = path

    def find_spec(self, fullname: str, target: _types.ModuleType | None = None):
        name = fullname.removeprefix(f"{self.PREFIX}.")
        override = _importlib_util.find_spec(name)
        if override is not None:
            return override
        try:
            path = (self.__path / name / "__init__.py").resolve(strict=True)
        except FileNotFoundError:
            return None
        return _importlib_util.spec_from_file_location(
            name, path, submodule_search_locations=[]
        )

    @classmethod
    def hook(cls, path: str):
        path0 = _pathlib.Path(path)
        if path0.samefile(cls.PREFIX):
            return cls(path0)
        raise ImportError


_sys.path_hooks.insert(0, ToolsPathEntryFinder.hook)
from tools.pytextgen import (
    OPEN_TEXT_OPTIONS as _OPEN_TXT_OPTS,
    main as _pytextgen_main,
    util as _pytextgen_util,
)

_UUID = "9a27fc39-496b-4b4c-87a7-03b9e88fc6bc"
_NAME = _UUID
_LOCAL_APP_DIRS = _appdirs.AppDirs(
    appname=_NAME,
    appauthor="polyipseity",
    version=None,
    roaming=False,
    multipath=False,
)
_basicConfig(level=_INFO)
_LOGGER = _getLogger(_NAME)
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

        cache_folder = _anyio.Path(
            _LOCAL_APP_DIRS.user_cache_dir,  # type: ignore
        ) / str((await _pytextgen_util.asyncify(_os.lstat)(folder)).st_ino)
        if not args.cached and await cache_folder.exists():
            await _aioshutil.rmtree(cache_folder, ignore_errors=False)
        await cache_folder.mkdir(parents=True, exist_ok=True)

        cache_data_path = cache_folder / "cache.json"
        if not await cache_data_path.exists():
            await cache_data_path.write_text(
                "", encoding="UTF-8", errors="strict", newline=None
            )
        async with await _anyio.open_file(
            cache_data_path,
            mode="r+t",
            **_OPEN_TXT_OPTS,
        ) as cache_data:
            try:
                data: _typing.MutableMapping[str, _typing.Any] = _json.loads(
                    await cache_data.read()
                )
            except _json.decoder.JSONDecodeError:
                data = {}
                _LOGGER.info(
                    "Cache data will be regenerated because it is empty or corrupted"
                )
            data = _collections.defaultdict(dict, data)
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
                cache: _typing.MutableMapping[str, tuple[int, str]] = data["cache"]

                def on_error(err: OSError) -> None:
                    try:
                        raise err
                    except OSError:
                        _LOGGER.exception("Exception while walking folders")

                async def maybe_yield(path: str):
                    def finalizer():
                        async def impl():
                            open_opts = _OPEN_TXT_OPTS.copy()
                            open_opts.update({"newline": ""})
                            async with await _anyio.open_file(
                                path,
                                mode="r+t",
                                **open_opts,
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

                        try:
                            del cache[path]
                        except KeyError:
                            pass
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
                        open_opts = _OPEN_TXT_OPTS.copy()
                        open_opts.update({"newline": ""})
                        async with await _anyio.open_file(
                            path,
                            mode="rt",
                            **open_opts,
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
            _LOGGER.info(f"Using {len(inputs)} input(s)")
            try:
                entry = _pytextgen_main.parser().parse_args(
                    tuple(
                        _itertools.chain(
                            args.arguments,
                            ("--",),
                            inputs,
                        )
                    )
                )
                await entry.invoke(entry)
                success = True
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
        _LOGGER.exception("Uncaught exception")
    finally:
        _LOGGER.info("Press <enter> to exit")
        try:
            input()
        except EOFError:
            pass
    _sys.exit(0)


def parser(
    parent: _typing.Callable[..., _argparse.ArgumentParser] | None = None,
) -> _argparse.ArgumentParser:
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
    entry = parser().parse_args(_sys.argv[1:])
    _asyncio.run(entry.invoke(entry))
