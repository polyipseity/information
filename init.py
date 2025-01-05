from aioshutil import rmtree as _rmtr, sync_to_async
from anyio import Path as _Path
from appdirs import AppDirs as _AppDirs  # type: ignore
from argparse import (
    ArgumentParser as _ArgParser,
    Namespace as _NS,
    ONE_OR_MORE as _ONE_OR_MORE,
)
from asyncio import Task, TaskGroup, create_task, gather as _gather, run as _run
from collections import defaultdict as _defdict
from dataclasses import dataclass as _dc
from functools import wraps as _wraps
from inspect import currentframe as _curframe, getframeinfo as _frameinfo
from itertools import chain as _chain, starmap as _smap, zip_longest as _zip_l
from json import dumps as _dumps, loads as _loads
from json.decoder import JSONDecodeError as _JSONDecErr
from logging import (
    INFO as _INFO,
    basicConfig as _basicConfig,
    exception as _exc,
    info as _info,
)
from operator import ne as _ne
from os import linesep as _linesep, lstat as _lstat, walk as _walk
from sys import argv as _argv, exit as _exit, modules as _mods
from typing import (
    Any as _Any,
    Awaitable as _Await,
    Callable as _Call,
    Collection as _Collect,
    MutableMapping as _MMap,
    Sequence as _Seq,
    final as _fin,
)

try:
    import tools.pytextgen as _mod

    _mods[_mod.__name__.removeprefix("tools.")] = _mod
except ImportError:
    pass
from pytextgen import OPEN_TEXT_OPTIONS as _OPEN_TXT_OPTS  # type: ignore
from pytextgen.main import parser as _pytextgen_parser  # type: ignore

_EXCLUDES = (
    ".git",
    ".obsidian",
    "tools",
)
_UUID = "9a27fc39-496b-4b4c-87a7-03b9e88fc6bc"
_NAME = _UUID
_LOCAL_APP_DIRS = _AppDirs(
    appname=_NAME,
    appauthor="polyipseity",
    version=None,
    roaming=False,
    multipath=False,
)
_lstat_a = sync_to_async(_lstat)


@_fin
@_dc(
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
    arguments: _Seq[str]

    def __post_init__(self):
        object.__setattr__(self, "arguments", tuple(self.arguments))


async def main(args: Arguments):
    try:
        frame = _curframe()
        if frame is None:
            raise ValueError(frame)
        folder = _Path(_frameinfo(frame).filename).parent

        excludes: _Seq[_Path] = await _gather(
            *(_Path(path).resolve(strict=True) for path in _EXCLUDES)
        )

        cache_folder = _Path(
            _LOCAL_APP_DIRS.user_cache_dir,  # type: ignore
        ) / str((await _lstat_a(folder)).st_ino)
        if not args.cached and await cache_folder.exists():
            await _rmtr(cache_folder, ignore_errors=False)
        await cache_folder.mkdir(parents=True, exist_ok=True)

        cache_data_path = cache_folder / "cache.json"
        if not await cache_data_path.exists():
            await cache_data_path.write_text(
                "", encoding="UTF-8", errors="strict", newline=None
            )
        async with await cache_data_path.open(
            mode="r+t",
            **_OPEN_TXT_OPTS,
        ) as cache_data:
            try:
                data: _MMap[str, _Any] = _loads(await cache_data.read())
            except _JSONDecErr:
                data = {}
                _info("Cache data will be regenerated because it is empty or corrupted")
            data = _defdict(dict, data)
            finalizers = list[_Call[[], _Await[None]]]()

            try:
                old_args: _Collect[str] = data["args"]
            except KeyError:
                old_args = ()
            diff_args = any(
                _smap(_ne, _zip_l(args.arguments, old_args, fillvalue=object()))
            )
            data["args"] = args.arguments

            async def gen_inputs():
                cache: _MMap[str, tuple[int, str]] = data["cache"]

                def on_error(err: OSError):
                    try:
                        raise err
                    except OSError:
                        _exc("Exception while walking folders")

                async def maybe_yield(path: _Path):
                    path_s = str(path)

                    def finalizer():
                        async def impl():
                            open_opts = _OPEN_TXT_OPTS.copy()
                            open_opts.update({"newline": ""})
                            async with await path.open(mode="r+t", **open_opts) as file:
                                read = await file.read()
                                seek = create_task(file.seek(0))
                                try:
                                    if (text := read.replace(_linesep, "\n")) != read:
                                        await seek
                                        await file.write(text)
                                        await file.truncate()
                                finally:
                                    seek.cancel()
                            cache[path_s] = (
                                (await _lstat_a(path)).st_mtime_ns,
                                text,
                            )

                        try:
                            del cache[path_s]
                        except KeyError:
                            pass
                        return impl

                    if diff_args:
                        return finalizer()
                    try:
                        c_mtime, c_text = cache[path_s]
                    except KeyError:
                        return finalizer()
                    if (await _lstat_a(path)).st_mtime_ns != c_mtime:
                        open_opts = _OPEN_TXT_OPTS.copy()
                        open_opts.update({"newline": ""})
                        async with await path.open(mode="rt", **open_opts) as io:
                            text = await io.read()
                        if text != c_text:
                            return finalizer()

                async def potential_files():
                    for root, dirs, files in _walk(
                        folder, topdown=True, onerror=on_error, followlinks=False
                    ):
                        if any(await _gather(*(ex.samefile(root) for ex in excludes))):
                            dirs.clear()
                            files.clear()
                        for file in files:
                            yield _Path(root, file)

                results = list[_Path]()

                async def process_file(file: _Path):
                    if await file.is_symlink():
                        return
                    path = await file.resolve(strict=True)
                    if path.suffix != ".md" or any(
                        await _gather(*(ex.samefile(path) for ex in excludes))
                    ):
                        return
                    finalize = await maybe_yield(path)
                    if finalize is not None:
                        finalizers.append(finalize)
                        results.append(path)

                async with TaskGroup() as tg:
                    tasks = list[Task[object]]()
                    async for file in potential_files():
                        tasks.append(tg.create_task(process_file(file)))
                return results

            inputs = await gen_inputs()
            _info(f"Using {len(inputs)} input(s)")
            try:
                entry = _pytextgen_parser().parse_args(
                    tuple(_chain(args.arguments, ("--",), inputs))
                )
                await entry.invoke(entry)
                success = True
            except SystemExit as ex:
                success = ex.code == 0

            if success:
                await _gather(
                    cache_data.seek(0), *(finalizer() for finalizer in finalizers)
                )
                await cache_data.write(
                    _dumps(data, ensure_ascii=False, sort_keys=True, indent=2)
                )
                await cache_data.truncate()
    except Exception:
        _exc("Uncaught exception")
    finally:
        _info("Press <enter> to exit")
        try:
            input()
        except EOFError:
            pass
    _exit(0)


def parser(parent: _Call[..., _ArgParser] | None = None):
    prog = _argv[0]

    parser = (_ArgParser if parent is None else parent)(
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
        nargs=_ONE_OR_MORE,
        help="sequence of argument(s) to pass through",
    )

    @_wraps(main)
    async def invoke(args: _NS):
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
    _basicConfig(level=_INFO)
    entry = parser().parse_args(_argv[1:])
    _run(entry.invoke(entry))
