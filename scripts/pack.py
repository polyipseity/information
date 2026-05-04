"""Create a PageRank-ordered zip bundle of knowledge-base notes.

Walks the Markdown link graph, computes PageRank to rank files by
importance, and writes a zip archive containing the top *N* files
together with metadata about omitted notes and link closure.
"""

from argparse import ONE_OR_MORE, ZERO_OR_MORE, ArgumentParser, Namespace
from collections.abc import (
    AsyncIterator,
    Callable,
    Collection,
    Mapping,
    MutableSet,
    Sequence,
    Set,
)
from dataclasses import asdict, dataclass, is_dataclass, replace
from datetime import datetime, timezone
from functools import reduce, wraps
from itertools import chain, count
from json import JSONEncoder, dumps
from logging import INFO, basicConfig, info
from os import PathLike, cpu_count, fspath
from pathlib import PurePath
from re import compile
from sys import argv
from typing import Any, NamedTuple, final, override
from urllib.parse import unquote
from zipfile import ZIP_DEFLATED, ZipFile

from anyio import CapacityLimiter, Path
from asyncer import SoonValue, asyncify, create_task_group, runnify
from asyncstdlib import chain as a_chain
from asyncstdlib import tuple as a_tuple
from bs4 import BeautifulSoup
from markdown import markdown
from numpy import array, float64, full, zeros
from numpy.linalg import matrix_power
from numpy.typing import NDArray

"""Exported names from this module (none: standalone script, not importable as a library)."""
__all__ = ()

# structural concurrency will be used instead of gather helper

"Maximum number of concurrent file-processing workers."
_CONCURRENCY = cpu_count() or 2
"Immutable empty frozenset used as a placeholder for pages with no outbound links."
_EMPTY_SET = frozenset[Any]()
"Path to this script file."
_FILE_PATH = PurePath(__file__)
"Format string for the metadata JSON filename written into the zip archive."
_METADATA_FILENAME_FORMAT = "metadata{}.json"
"Version string for the pack script."
_VERSION = "∞"


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
    """Parsed command-line arguments for the pack script."""

    output: Path
    root: Path | None
    count: int
    damping_factor: float
    page_rank_iterations: int
    exclude_extensions: Collection[str]
    files: Collection[Path]

    def __post_init__(self) -> None:
        """Coerce mutable sequences to tuples to satisfy the frozen dataclass contract."""
        object.__setattr__(self, "files", tuple(self.files))
        object.__setattr__(self, "exclude_extensions", tuple(self.exclude_extensions))


async def main(args: Arguments) -> None:
    """Resolve inputs, build the Markdown link graph, rank files with PageRank, and write the zip."""
    if not args.files:
        raise ValueError("No files to pack")
    if 0 > args.damping_factor or args.damping_factor > 1:
        raise ValueError(
            f"Damping factor should be between 0 and 1: {args.damping_factor}"
        )

    async def resolve_root():
        """Resolve the root directory, or return None if no root was supplied."""
        return await args.root.resolve(strict=True) if args.root else None

    async def resolve_file(file: Path) -> AsyncIterator[Path]:
        """Yield resolved paths: expand directories recursively, yield files as-is."""
        file = await file.resolve(strict=True)
        if await file.is_dir():
            async for child in file.glob("**/*"):
                if await child.is_file():
                    yield child
            return
        yield file

    # resolve output, root, and file list concurrently
    sv_output: SoonValue[Path] | None = None
    sv_root: SoonValue[Path | None] | None = None
    sv_files: SoonValue[tuple[Path, ...]] | None = None
    async with create_task_group() as tg:
        sv_output = tg.soonify(lambda: args.output.resolve())()
        sv_root = tg.soonify(resolve_root)()
        sv_files = tg.soonify(
            lambda: a_tuple(a_chain[Path].from_iterable(map(resolve_file, args.files)))
        )()
    assert sv_output is not None and sv_root is not None and sv_files is not None
    output, root, files = sv_output.value, sv_root.value, sv_files.value
    exclude_extensions = frozenset(args.exclude_extensions)
    args = replace(
        args,
        output=output,
        root=root,
        exclude_extensions=exclude_extensions,
        files=files,
    )

    if root is not None and not all(root in file.parents for file in files):
        raise ValueError("The specified root does not contain all files to pack")

    class ProcessMarkdownFileResult(NamedTuple):
        """Result of processing a single Markdown file: its resolved path plus sets of existing and missing link targets."""

        path: Path
        existing: MutableSet[Path]
        missing: MutableSet[Path]

    scheme_regex = compile(r"^[^:]+:")

    async def process_file(file: Path):
        """Parse links from a Markdown file and return paths of reachable and missing link targets."""
        if file.suffix in exclude_extensions:
            return None
        if file.suffix != ".md":
            return ProcessMarkdownFileResult(file, set(), set())
        text = await file.read_text()
        # markdown is synchronous and can be CPU-bound; run it in a worker thread
        html = await asyncify(markdown)(text, output_format="html")
        link_paths = list[Path]()
        for a_tag in BeautifulSoup(html, "html.parser").find_all("a"):
            if not (href := a_tag.get("href")):
                continue
            if not (link_path := str(href).split("#", 2)[0]):
                continue
            link_path = unquote(link_path)
            if scheme_regex.match(link_path):
                continue
            link_paths.append(file.parent / link_path)

        async def process_path(path: Path):
            """Resolve a link path and yield (resolved_path, exists) pairs, expanding directories."""
            resolved = await path.resolve()
            if await resolved.exists():
                if await resolved.is_dir():
                    async for child in resolved.glob("**/*"):
                        if await child.is_file():
                            yield child, True
                    return
                yield resolved, True
                return
            yield resolved, False

        def reduce_ret(
            ret: ProcessMarkdownFileResult, path_and_existence: tuple[Path, bool]
        ):
            """Accumulate a resolved path into the existing or missing set of the result."""
            (ret.existing if path_and_existence[1] else ret.missing).add(
                path_and_existence[0]
            )
            return ret

        link_paths = await a_tuple(
            a_chain[tuple[Path, bool]].from_iterable(map(process_path, link_paths))
        )
        return reduce(
            reduce_ret, link_paths, ProcessMarkdownFileResult(file, set(), set())
        )

    existing_map: dict[Path, Set[Path]] = {}
    missing_paths = set[Path]()

    # Instead of iterating in discrete batches we spawn a single task
    # group and allow workers to enqueue additional paths dynamically.
    # A global CapacityLimiter bounds concurrent ``process_file`` calls.
    async with create_task_group() as tg:
        limiter = CapacityLimiter(_CONCURRENCY)

        async def worker(path: Path) -> None:
            """Process one file, record its links, and schedule newly discovered files for processing."""
            async with limiter:
                ret = await process_file(path)
            if ret is None:
                return
            path2, existing, missing = ret

            new_existing = set(existing) - existing_map.keys()
            existing_map.update({p: _EMPTY_SET for p in new_existing})
            # schedule newly discovered files for processing
            for p in new_existing:
                tg.start_soon(worker, p)

            missing_paths.update(missing)
            existing_map[path2] = existing

        # seed initial work
        for item in files:
            tg.start_soon(worker, item)

    common_parents = set(files[0].parents)
    for path in existing_map:
        common_parents.intersection_update(path.parents)
    if root is None:
        common_parents = tuple(common_parents)
        try:
            root = common_parents[0]
        except IndexError:
            raise ValueError("Cannot automatically detect root")
        for common_parent in common_parents[1:]:
            if root in common_parent.parents:
                root = common_parent
        args = replace(args, root=root)
    elif root not in common_parents:
        existing_paths_not_in_root = tuple(
            root not in path.parents for path in existing_map
        )
        raise ValueError(
            f"The specified root does not contain all files to pack: {existing_paths_not_in_root}"
        )

    ordered_paths, stochastic_mat = modified_page_rank_stochastic_mat(
        frozenset(files), existing_map, damping=args.damping_factor
    )
    ordered_paths_size = len(ordered_paths)
    page_ranks = full((ordered_paths_size, 1), 1 / ordered_paths_size, dtype=float64)
    page_ranks = matrix_power(stochastic_mat, args.page_rank_iterations) @ page_ranks
    page_ranks = page_ranks.reshape(-1)
    page_rank_map = {path: page_ranks[idx] for idx, path in enumerate(ordered_paths)}

    def try_make_relative(path: Path):
        """Return a root-relative POSIX string for path, or an absolute string if path is outside root."""
        try:
            return path.relative_to(root).__fspath__()
        except ValueError:
            return path.__fspath__()

    # produce a list of (relative_path, rank) pairs without mutating
    # ``existing_paths`` which is still used as a dict above
    ranked = sorted(
        (
            (try_make_relative(path), float(page_rank_map[path]))
            for path in existing_map
        ),
        key=lambda item: item[1],
        reverse=True,
    )
    filtered_paths = ()
    if args.count >= 0:
        ranked, filtered_paths = (
            ranked[: args.count],
            ranked[args.count :],
        )
    existing_paths, filtered_paths = dict(ranked), dict(filtered_paths)
    # produce a sorted list version for metadata; keep original set intact
    missing_paths_sorted = sorted(map(try_make_relative, missing_paths))

    filter_threshold = max(filtered_paths.values(), default=0)

    info(f"existing paths: {existing_paths}")
    # info(f"filtered paths: {filtered_paths}")
    # info(f"missing paths: {missing_paths}")
    info(f"filter threshold: {filter_threshold}")
    info(f"root: {root}")

    metadata_filename = _METADATA_FILENAME_FORMAT.format("")
    if metadata_filename in existing_paths:
        for discriminator in count():
            if (
                metadata_filename := _METADATA_FILENAME_FORMAT.format(discriminator)
            ) not in existing_paths:
                break

    class MetadataJSONEncoder(JSONEncoder):
        """JSON encoder that serialises PathLike objects and dataclasses."""

        @override
        def default(self, o: object) -> object:
            """Serialise PathLike objects to strings and dataclasses to dicts."""
            if isinstance(o, PathLike):
                return fspath(o)
            if is_dataclass(o) and not isinstance(o, type):
                return asdict(o)
            return super().default(o)

    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as output_zip:
        output_zip.writestr(
            metadata_filename,
            dumps(
                {
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "arguments": args,
                    "filter_threshold": filter_threshold,
                    "existing_paths": existing_paths,
                    "filtered_paths": filtered_paths,
                    "missing_paths": missing_paths_sorted,
                },
                ensure_ascii=False,
                indent=4,
                sort_keys=False,
                cls=MetadataJSONEncoder,
            ),
        )
        for path in existing_paths:
            output_zip.write(root / path, path)

    info(f"Output: {output}")


def modified_page_rank_stochastic_mat(
    initial: Set[Path],
    links: Mapping[Path, Set[Path]],
    *,
    damping: float,
) -> tuple[Sequence[Path], NDArray[float64]]:
    """Build a modified PageRank stochastic matrix that teleports to seed files with probability (1-damping)."""
    ordered_paths = tuple(
        frozenset(chain(initial, links, chain.from_iterable(links.values())))
    )
    path_indices = {path: idx for idx, path in enumerate(ordered_paths)}
    size = len(path_indices)

    def make_link_array(links: Set[Path]):
        """Return a column probability vector for the given outbound link set, or a uniform vector if empty."""
        if links:
            ret = zeros((size,), dtype=float64)
            ret[list(path_indices[link] for link in links)] = 1 / len(links)
            return ret
        return full((size,), 1 / size, dtype=float64)

    stochastic_mat = array(
        tuple(make_link_array(links.get(path, set[Path]())) for path in ordered_paths),
        dtype=float64,
    ).transpose()
    stochastic_mat *= damping
    stochastic_mat[list(path_indices[path] for path in initial), :] += (
        1 - damping
    ) / len(initial)

    return ordered_paths, stochastic_mat


def parser(parent: Callable[..., ArgumentParser] | None = None):
    """Build and return the argument parser for the pack script."""
    prog = __package__ or __name__

    parser = (ArgumentParser if parent is None else parent)(
        prog=f"python -m {prog}",
        description="publish private files",
        add_help=True,
        allow_abbrev=False,
        exit_on_error=False,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{prog} v{_VERSION}",
        help="print version and exit",
    )
    parser.add_argument(
        "-o",
        "--output",
        action="store",
        required=False,
        default=Path(f"{_FILE_PATH.name}.zip"),
        type=Path,
        help=f"output filepath; default `{_FILE_PATH.name}.zip`",
    )
    parser.add_argument(
        "-r",
        "--root",
        action="store",
        required=False,
        type=Path,
        help="root; default is automatically determined",
    )
    parser.add_argument(
        "-n",
        "--count",
        action="store",
        required=False,
        default=25,
        type=int,
        help="maximum number of files to pack; default 25, negative means all files",
    )
    parser.add_argument(
        "-d",
        "--damping-factor",
        action="store",
        required=False,
        default=0.5,
        type=float,
        help="PageRank damping factor; default 0.5",
    )
    parser.add_argument(
        "--page-rank-iterations",
        action="store",
        required=False,
        default=100,
        type=int,
        help="number of PageRank iterations; default 100",
    )
    parser.add_argument(
        "-e",
        "--exclude-extension",
        action="store",
        nargs=ZERO_OR_MORE,
        type=str,
        help="extensions to exclude, with a leading dot if nonempty",
    )
    parser.add_argument(
        "files",
        action="store",
        nargs=ONE_OR_MORE,
        type=Path,
        help="files to pack",
    )

    @wraps(main)
    async def invoke(args: Namespace):
        """Construct an Arguments instance from parsed namespace and call main."""
        await main(
            Arguments(
                output=args.output,
                root=args.root,
                count=args.count,
                damping_factor=args.damping_factor,
                page_rank_iterations=args.page_rank_iterations,
                exclude_extensions=args.exclude_extension,
                files=args.files,
            )
        )

    parser.set_defaults(invoke=invoke)
    return parser


async def main0():
    """Entry point for running the script directly. Parses CLI arguments and invokes main()."""
    global __name__
    __name__ = _FILE_PATH.stem
    basicConfig(level=INFO)
    entry = parser().parse_args(argv[1:])
    await entry.invoke(entry)


def __main__():
    """Entry point for running the script directly."""
    runnify(main0, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
