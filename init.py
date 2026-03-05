from argparse import ONE_OR_MORE, ArgumentParser, Namespace
from collections import defaultdict
from collections.abc import (
    Awaitable,
    Callable,
    Collection,
    Iterable,
    MutableMapping,
    Sequence,
)
from dataclasses import dataclass
from functools import wraps
from inspect import currentframe, getframeinfo
from itertools import chain, starmap, zip_longest
from json import dumps, loads
from json.decoder import JSONDecodeError
from logging import INFO, basicConfig, exception, info
from operator import ne
from os import PathLike, fspath, linesep, lstat, walk
from sys import argv, exit
from typing import Any, final

from aioshutil import rmtree
from anyio import Path
from appdirs import AppDirs  # type: ignore
from asyncer import SoonValue, asyncify, create_task_group, runnify
from pytextgen.main import parser as pytextgen_parser
from pytextgen.meta import OPEN_TEXT_OPTIONS

__all__ = ("Arguments", "main", "parser")

_EXCLUDES = (
    ".git",
    ".obsidian",
    "node_modules",
    "tools",
)
_UUID = "9a27fc39-496b-4b4c-87a7-03b9e88fc6bc"
_NAME = _UUID
_LOCAL_APP_DIRS = AppDirs(
    appname=_NAME,
    appauthor="polyipseity",
    version=None,
    roaming=False,
    multipath=False,
)
_lstat_a = asyncify(lstat)


@final
@dataclass(
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
    arguments: Sequence[str]

    def __post_init__(self):
        object.__setattr__(self, "arguments", tuple(self.arguments))


async def _in_paths(path: str | PathLike[str], paths: Iterable[Path]) -> bool:
    """Return True if any ``ex`` is the same filesystem object as
    ``path``. Runs checks concurrently for speed.  ``path`` may
    be a str wrapper or Path-like object.
    """
    if not paths:
        return False
    svs: list[SoonValue[bool]] = []
    async with create_task_group() as tg:
        for ex in paths:
            svs.append(tg.soonify(ex.samefile)(path))
    return any(sv.value for sv in svs)


async def main(args: Arguments):
    try:
        frame = currentframe()
        if frame is None:
            raise ValueError(frame)
        folder = Path(getframeinfo(frame).filename).parent

        # resolve excluded paths concurrently using a task group
        excludes_svs: list[SoonValue[Path]] = []
        async with create_task_group() as tg:
            for path in _EXCLUDES:
                excludes_svs.append(tg.soonify(Path(path).resolve)(strict=True))
        # note: results order may differ from _EXCLUDES but order is irrelevant
        excludes = [sv.value for sv in excludes_svs]

        cache_folder = Path(
            _LOCAL_APP_DIRS.user_cache_dir,  # type: ignore
        ) / str((await _lstat_a(folder)).st_ino)
        if not args.cached and await cache_folder.exists():
            await rmtree(cache_folder, ignore_errors=False)
        await cache_folder.mkdir(parents=True, exist_ok=True)

        cache_data_path = cache_folder / "cache.json"
        if not await cache_data_path.exists():
            await cache_data_path.write_text(
                "", encoding="UTF-8", errors="strict", newline=None
            )
        async with await cache_data_path.open(
            mode="r+t",
            **OPEN_TEXT_OPTIONS,
        ) as cache_data:
            try:
                data: MutableMapping[str, Any] = loads(await cache_data.read())
            except JSONDecodeError:
                data = {}
                info("Cache data will be regenerated because it is empty or corrupted")
            data = defaultdict(dict, data)
            finalizers = list[Callable[[], Awaitable[None]]]()

            try:
                old_args: Collection[str] = data["args"]
            except KeyError:
                old_args = ()
            diff_args = any(
                starmap(ne, zip_longest(args.arguments, old_args, fillvalue=object()))
            )
            data["args"] = args.arguments

            async def gen_inputs():
                cache: MutableMapping[str, tuple[int, str]] = data["cache"]

                def on_error(err: OSError):
                    try:
                        raise err
                    except OSError:
                        exception("Exception while walking folders")

                async def maybe_yield(path: Path):
                    path_s = str(path)

                    def finalizer():
                        async def impl():
                            open_opts = OPEN_TEXT_OPTIONS.copy()
                            open_opts.update({"newline": ""})
                            async with await path.open(mode="r+t", **open_opts) as file:
                                read = await file.read()
                                # the original version spawned a background task to seek before
                                # writing.  that micro-optimization is unnecessary with
                                # AnyIO; just await the seek when needed.
                                if (text := read.replace(linesep, "\n")) != read:
                                    await file.seek(0)
                                    await file.write(text)
                                    await file.truncate()
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
                        open_opts = OPEN_TEXT_OPTIONS.copy()
                        open_opts.update({"newline": ""})
                        async with await path.open(mode="rt", **open_opts) as io:
                            text = await io.read()
                        if text != c_text:
                            return finalizer()

                async def potential_files():
                    for root, dirs, files in walk(
                        folder, topdown=True, onerror=on_error, followlinks=False
                    ):
                        # skip roots matching any exclude path
                        if await _in_paths(root, excludes):
                            dirs.clear()
                            files.clear()
                        for file in files:
                            yield Path(root, file)

                results = list[Path]()

                async def process_file(file: Path) -> Path | None:
                    # return the path when it should be included, otherwise None
                    if await file.is_symlink():
                        return None
                    path = await file.resolve(strict=True)
                    if path.suffix != ".md":
                        return None
                    # test exclusion in parallel; once one matches we can bail
                    if await _in_paths(path, excludes):
                        return None
                    finalize = await maybe_yield(path)
                    if finalize is not None:
                        finalizers.append(finalize)
                        return path
                    return None

                # concurrently walk and process files using SoonValue objects
                soon_values: list[SoonValue[Path | None]] = []

                async with create_task_group() as tg:
                    async for file in potential_files():
                        soon_values.append(tg.soonify(process_file)(file))

                # gather completed paths, filtering out Nones
                results = [p for p in (sv.value for sv in soon_values) if p is not None]
                return results

            inputs = await gen_inputs()
            info(f"Using {len(inputs)} input(s)")
            try:
                entry = pytextgen_parser().parse_args(
                    tuple(chain(args.arguments, ("--",), map(fspath, inputs)))
                )
                await entry.invoke(entry)
                success = True
            except SystemExit as ex:
                success = ex.code == 0

            if success:
                async with create_task_group() as tg:
                    tg.start_soon(cache_data.seek, 0)
                    for finalizer in finalizers:
                        tg.start_soon(finalizer)
                await cache_data.write(
                    dumps(data, ensure_ascii=False, sort_keys=True, indent=2)
                )
                await cache_data.truncate()
    except Exception:
        exception("Uncaught exception")
    finally:
        info("Press <enter> to exit")
        try:
            input()
        except EOFError:
            pass
    exit(0)


def parser(parent: Callable[..., ArgumentParser] | None = None):
    prog = argv[0]

    parser = (ArgumentParser if parent is None else parent)(
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
        nargs=ONE_OR_MORE,
        help="sequence of argument(s) to pass through",
    )

    @wraps(main)
    async def invoke(args: Namespace):
        await main(
            Arguments(
                prog=prog,
                cached=args.cached,
                arguments=args.arguments,
            )
        )

    parser.set_defaults(invoke=invoke)
    return parser


def __main__() -> None:
    """Entry point for running the script directly."""
    basicConfig(level=INFO)
    entry = parser().parse_args(argv[1:])
    runnify(entry.invoke, backend_options={"use_uvloop": True})(entry)


if __name__ == "__main__":
    __main__()
