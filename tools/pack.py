from itertools import chain, count
from json import JSONEncoder, dumps
from os import PathLike, cpu_count
from pathlib import PurePath
from types import EllipsisType
from urllib.parse import unquote
from zipfile import ZIP_DEFLATED, ZipFile
from anyio import Path
from argparse import ONE_OR_MORE, ArgumentParser, Namespace
from asyncio import (
    BoundedSemaphore,
    Queue,
    QueueEmpty,
    TaskGroup,
    create_task,
    gather,
    run,
)
from dataclasses import asdict, dataclass, is_dataclass, replace
from functools import reduce, wraps
from logging import INFO, basicConfig, info
from lxml.html import fromstring  # type: ignore
from markdown import markdown
from matplotlib.pylab import matrix_power
from numpy import array, float64, full, zeros
from numpy.typing import NDArray
from re import compile
from sys import argv
from typing import (
    AbstractSet,
    Any,
    AnyStr,
    AsyncIterable,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Mapping,
    MutableSet,
    NamedTuple,
    Sequence,
    TypeVar,
    final,
    override,
)

_T = TypeVar("_T")
_U = TypeVar("_U")

_CONCURRENCY = cpu_count() or 2
_EMPTY_SET = frozenset[Any]()
_FILE_PATH = PurePath(__file__)
_METADATA_FILENAME_FORMAT = "metadata{}.json"
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
    output: Path
    root: Path | None
    files: Sequence[Path]
    count: int
    damping_factor: float
    page_rank_iterations: int


async def main(args: Arguments) -> None:
    if not args.files:
        raise ValueError("No files to pack")
    if 0 > args.damping_factor or args.damping_factor > 1:
        raise ValueError(
            f"Damping factor should be between 0 and 1: {args.damping_factor}"
        )

    async def resolve_root():
        return await args.root.resolve(strict=True) if args.root else None

    output, root, files = await gather(
        args.output.resolve(),
        resolve_root(),
        gather(*(file.resolve(strict=True) for file in args.files)),
    )
    args = replace(args, output=output, root=root, files=files)

    if root is not None and not all(root in file.parents for file in files):
        raise ValueError("The specified root does not contain all files to pack")

    class ProcessMarkdownFileResult(NamedTuple):
        path: Path
        existing: MutableSet[Path]
        missing: MutableSet[Path]

    scheme_regex = compile(r"^[^:]+:")

    async def process_markdown_file(file: Path) -> ProcessMarkdownFileResult:
        text = await file.read_text()
        xhtml = markdown(text, output_format="xhtml")
        link_paths = list[Path]()
        for link in fromstring(xhtml).xpath("//a"):
            if not (href := link.get("href")):
                continue
            if not (link_path := href.split("#", 2)[0]):
                continue
            link_path = unquote(link_path)
            if scheme_regex.match(link_path):
                continue
            link_paths.append(file.parent / link_path)

        async def process_path(path: Path):
            resolved = await path.resolve()
            return resolved, await resolved.exists()

        def reduce_ret(
            ret: ProcessMarkdownFileResult, path_and_existence: tuple[Path, bool]
        ):
            (ret.existing if path_and_existence[1] else ret.missing).add(
                path_and_existence[0]
            )
            return ret

        link_paths = await gather(*map(process_path, link_paths))
        return reduce(
            reduce_ret, link_paths, ProcessMarkdownFileResult(file, set(), set())
        )

    existing_paths = dict[Path, AbstractSet[Path]]()
    missing_paths = set[Path]()
    queue = files.copy()

    async def queue_iter():
        while queue:
            yield queue.pop()

    while queue:
        async for path, existing, missing in a_eager_map(
            process_markdown_file, queue_iter(), concurrency=_CONCURRENCY
        ):
            new_existing = set(existing)
            new_existing.difference_update(existing_paths)
            existing_paths.update({path: _EMPTY_SET for path in new_existing})
            queue.extend(new_existing)

            missing_paths.update(missing)
            existing_paths[path] = existing

    common_parents = set(files[0].parents)
    for path in existing_paths:
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
            root not in path.parents for path in existing_paths
        )
        raise ValueError(
            f"The specified root does not contain all files to pack: {existing_paths_not_in_root}"
        )

    ordered_paths, stochastic_mat = modified_page_rank_stochastic_mat(
        frozenset(files), existing_paths, damping=args.damping_factor
    )
    ordered_paths_size = len(ordered_paths)
    page_ranks = full((ordered_paths_size, 1), 1 / ordered_paths_size, dtype=float64)
    page_ranks = matrix_power(stochastic_mat, args.page_rank_iterations) @ page_ranks
    page_ranks = page_ranks.reshape(-1)
    page_rank_map = {path: page_ranks[idx] for idx, path in enumerate(ordered_paths)}

    def try_make_relative(path: Path):
        try:
            return path.relative_to(root).__fspath__()
        except ValueError:
            return path.__fspath__()

    existing_paths = sorted(
        (
            (try_make_relative(path), float(page_rank_map[path]))
            for path in existing_paths
        ),
        key=lambda item: item[1],
        reverse=True,
    )
    filtered_paths = ()
    if args.count >= 0:
        existing_paths, filtered_paths = (
            existing_paths[: args.count],
            existing_paths[args.count :],
        )
    existing_paths, filtered_paths = dict(existing_paths), dict(filtered_paths)
    missing_paths = sorted(map(try_make_relative, missing_paths))

    filter_threshold = min(existing_paths.values())

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
        @override
        def default(self, o: object):
            if isinstance(o, PathLike):
                o2: PathLike[AnyStr] = o  # type: ignore
                return o2.__fspath__()
            if is_dataclass(o):
                return asdict(o)  # type: ignore
            return super().default(o)

    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as output_zip:
        output_zip.writestr(
            metadata_filename,
            dumps(
                {
                    "arguments": args,
                    "filter_threshold": filter_threshold,
                    "existing_paths": existing_paths,
                    "filtered_paths": filtered_paths,
                    "missing_paths": missing_paths,
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
    initial: AbstractSet[Path],
    links: Mapping[Path, AbstractSet[Path]],
    *,
    damping: float,
) -> tuple[Sequence[Path], NDArray[float64]]:
    ordered_paths = tuple(
        frozenset(chain(initial, links, chain.from_iterable(links.values())))
    )
    path_indices = {path: idx for idx, path in enumerate(ordered_paths)}
    size = len(path_indices)

    def make_link_array(links: AbstractSet[Path]):
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
        "files",
        action="store",
        nargs=ONE_OR_MORE,
        type=Path,
        help="files to pack",
    )

    @wraps(main)
    async def invoke(args: Namespace):
        await main(
            Arguments(
                output=args.output,
                root=args.root,
                files=args.files,
                count=args.count,
                damping_factor=args.damping_factor,
                page_rank_iterations=args.page_rank_iterations,
            )
        )

    parser.set_defaults(invoke=invoke)
    return parser


# copied utilities


async def a_eager_map(
    func: Callable[[_T], Awaitable[_U]],
    iterable: AsyncIterable[_T],
    *,
    concurrency: int = 1,
    max_size: int = 0,
) -> AsyncIterator[_U]:
    """
    Async map that eagerly evaluates. `func` is run in the same thread.

    Exceptions are propagated in an exception group when the items with
    exceptions are accessed.
    The group of exceptions may include exceptions that occur during eager
    submission of tasks.
    """
    queue = Queue[Awaitable[_U] | EllipsisType](max_size)

    async def submit():
        try:
            concurrency_limiter = BoundedSemaphore(concurrency)

            async def execute(item: _T):
                async with concurrency_limiter:
                    return await func(item)

            async for item in iterable:
                async with concurrency_limiter:
                    task = create_task(execute(item))
                    try:
                        await queue.put(task)
                    except BaseException:
                        task.cancel()
                        raise
        finally:
            await queue.put(...)

    try:
        async with TaskGroup() as tg:
            submit_task = tg.create_task(submit())
            async for item in a_iter_queue(queue):
                if item is ...:
                    break
                yield await item
        submit_task.result()
    except BaseExceptionGroup as exc:  # type: ignore
        # do not wrap `GeneratorExit` in an exception group
        gen_exits = exc.subgroup(GeneratorExit)  # type: ignore
        if gen_exits is not None:
            raise gen_exits.exceptions[0]
        raise
    finally:
        # stop and cleanup unconsumed awaitables
        await gather(
            *(awaitable for awaitable in iter_queue(queue) if awaitable is not ...),
            return_exceptions=True,
        )


async def a_iter_queue(queue: Queue[_T]) -> AsyncIterator[_T]:
    """
    Iterate through a `Queue` without needing to call `task_done`.
    """
    while True:
        ret = await queue.get()
        try:
            yield ret
        finally:
            queue.task_done()


def iter_queue(queue: Queue[_T]) -> Iterator[_T]:
    """
    Iterate all items available now in `Queue`.
    """
    while True:
        try:
            ret = queue.get_nowait()
        except QueueEmpty:
            break
        try:
            yield ret
        finally:
            queue.task_done()


if __name__ == "__main__":
    __name__ = _FILE_PATH.stem
    basicConfig(level=INFO)
    entry = parser().parse_args(argv[1:])
    run(entry.invoke(entry))
