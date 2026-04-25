from argparse import ONE_OR_MORE, ArgumentParser, Namespace
from collections import defaultdict
from collections.abc import (AsyncIterator, Awaitable, Callable, Collection,
                             Iterable, MutableMapping, Sequence)
from dataclasses import dataclass
from functools import wraps
from inspect import currentframe, getframeinfo
from itertools import chain, starmap, zip_longest
from json import dumps, loads
from json.decoder import JSONDecodeError
from logging import INFO, basicConfig, exception, info
from operator import ne
from os import fspath, linesep, lstat
from pathlib import PurePath
from shutil import rmtree as _sync_rmtree
from sys import argv, exit, stdin
from typing import Any, final

from anyio import Path
from appdirs import AppDirs
from asyncer import SoonValue, asyncify, create_task_group, runnify
from pytextgen.main import parser as pytextgen_parser
from pytextgen.meta import OPEN_TEXT_OPTIONS

__all__ = ("Arguments", "main", "parser")

# Gitignore-style spec: one pattern per line; order matters (last match wins).
# Negated interpretation: pattern = include; !pattern = exclude. Default (no match) = excluded.
_GLOB_SPEC = """
general/**/*.md
private/general/**/*.md
private/special/**/*.md
special/**/*.md
"""


def _iter_ignore_patterns(spec: str) -> Iterable[tuple[str, bool]]:
    """Parse a gitignore-style, multi-line spec (negated: pattern = include, ! = exclude).

    Yields (pattern, is_ignore) in order. is_ignore=True => exclude; False => include.
    """
    for raw in spec.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        is_ignore = line.startswith("!")
        pattern = line[1:].strip() if line.startswith("!") else line
        if not pattern:
            continue
        yield pattern, is_ignore


def _path_matches_pattern(rel: PurePath, pattern: str) -> bool:
    """Return True if rel (relative to root) matches the pattern.

    Patterns with * or ? use pathlib match(); otherwise: single-segment patterns
    match that name at any depth; multi-segment patterns match as a path prefix.
    """
    if "*" in pattern or "?" in pattern:
        return rel.match(pattern)
    parts = rel.parts
    pat_parts = tuple(p for p in pattern.split("/") if p)
    if not pat_parts:
        return False
    if len(pat_parts) == 1:
        return pat_parts[0] in parts
    if len(pat_parts) <= len(parts):
        return parts[: len(pat_parts)] == pat_parts
    return False


def _is_ignored_by_spec(rel: PurePath, patterns: Sequence[tuple[str, bool]]) -> bool:
    """Return True if rel should be ignored (excluded). Last match wins; default (no match) = excluded."""
    ignored = True
    for pattern, is_ignore in patterns:
        if _path_matches_pattern(rel, pattern):
            ignored = is_ignore
    return ignored


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
_rmtree = asyncify(_sync_rmtree)


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


async def main(args: Arguments):
    try:
        frame = currentframe()
        if frame is None:
            raise ValueError(frame)
        folder = Path(getframeinfo(frame).filename).parent

        # parse gitignore-style spec (last match wins); list of (pattern, is_ignore)
        ignore_patterns: list[tuple[str, bool]] = list(
            _iter_ignore_patterns(_GLOB_SPEC)
        )

        cache_folder = Path(
            _LOCAL_APP_DIRS.user_cache_dir,
        ) / str((await _lstat_a(folder)).st_ino)
        if not args.cached and await cache_folder.exists():
            await _rmtree(cache_folder, ignore_errors=False)
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

                async def candidate_md_files() -> AsyncIterator[Path]:
                    """Yield .md paths under folder that pass the glob spec (not ignored)."""
                    async for path in folder.rglob("*.md"):
                        if await path.is_symlink():
                            continue
                        try:
                            resolved = await path.resolve(strict=True)
                            rel = PurePath(resolved).relative_to(folder)
                        except (ValueError, OSError):
                            continue
                        if _is_ignored_by_spec(rel, ignore_patterns):
                            continue
                        yield path

                results = list[Path]()

                async def process_file(file: Path) -> Path | None:
                    # return the path when it should be included, otherwise None
                    if await file.is_symlink():
                        return None
                    path = await file.resolve(strict=True)
                    if path.suffix != ".md":
                        return None
                    try:
                        rel = PurePath(path).relative_to(folder)
                    except ValueError:
                        return None  # path outside folder, skip
                    if _is_ignored_by_spec(rel, ignore_patterns):
                        return None
                    finalize = await maybe_yield(path)
                    if finalize is not None:
                        finalizers.append(finalize)
                        return path
                    return None

                # generate candidates from spec-filtered rglob, then process concurrently
                soon_values: list[SoonValue[Path | None]] = []
                async with create_task_group() as tg:
                    async for file in candidate_md_files():
                        soon_values.append(tg.soonify(process_file)(file))

                # gather completed paths, filtering out Nones
                results = [p for p in (sv.value for sv in soon_values) if p is not None]
                return results

            inputs = await gen_inputs()
            info(f"Using {len(inputs)} input(s)")
            try:
                entry = pytextgen_parser().parse_args(
                    tuple(chain(args.arguments, ("--",), (fspath(input) for input in inputs)))
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
        # Only wait for Enter when not in an interactive terminal (e.g. double-click
        # launcher), so CLI runs (generate -C, CI) exit immediately.
        if stdin.isatty():
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
        description="input wrapper for scripts",
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


async def main0():
    """Entry point for running the script directly. Parses CLI arguments and invokes main()."""
    basicConfig(level=INFO)
    entry = parser().parse_args(argv[1:])
    await entry.invoke(entry)


def __main__() -> None:
    """Entry point for running the script directly."""
    runnify(main0, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
