from asyncio.subprocess import DEVNULL, PIPE
from collections import defaultdict
from itertools import chain
from os import cpu_count
from pathlib import PurePath
from shlex import quote
from tempfile import NamedTemporaryFile, TemporaryDirectory
from aioshutil import which
from anyio import AsyncFile, Path
from argparse import ArgumentParser, Namespace
from asyncio import BoundedSemaphore, create_subprocess_exec, gather, run
from dataclasses import dataclass
from functools import wraps
from logging import INFO, basicConfig, error, info
from sys import argv
from typing import Any, Callable, Iterable, MutableSet, final

_FILE_PATH = PurePath(__file__)
_PUBLIC_GIT_DIRECTORY = _FILE_PATH / "../../.git"
_SUBPROCESS_SEMAPHORE = BoundedSemaphore(cpu_count() or 4)
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
    allow_trailing_whitespaces_in_paths: bool
    paths_file: Path


@wraps(which)
async def _which2(cmd: str) -> str:
    ret = await which(cmd)
    if ret is None:
        raise FileNotFoundError(cmd)
    return ret


@wraps(create_subprocess_exec)
async def _exec(
    *args: Any, input: bytes | bytearray | memoryview | None = None, **kwargs: Any
) -> tuple[str, str]:
    async with _SUBPROCESS_SEMAPHORE:
        proc = await create_subprocess_exec(
            *args,
            stdin=DEVNULL if input is None else PIPE,
            stdout=PIPE,
            stderr=PIPE,
            **kwargs,
        )
        stdout, stderr = await proc.communicate(input=input)
    stdout, stderr = (
        stdout.decode(errors="backslashreplace"),
        stderr.decode(errors="backslashreplace"),
    )
    if stdout:
        info(stdout)
    if stderr:
        error(stderr)
    if proc.returncode:
        raise ChildProcessError(proc.returncode, stderr)
    return stdout, stderr


async def main(args: Arguments) -> None:
    async def read_paths():
        ret = set(
            line.replace("\\", "/")
            for line in (await args.paths_file.read_text()).splitlines()
            if not line.startswith("#")
        )
        ret.discard("")
        return ret

    pub_git_dir, git_exe, paths = await gather(
        Path(_PUBLIC_GIT_DIRECTORY).resolve(strict=True),
        _which2("git"),
        read_paths(),
    )

    info(f"Paths: {paths}")
    if not args.allow_trailing_whitespaces_in_paths and any(
        path.rstrip() != path for path in paths
    ):
        raise ValueError("Found trailing whitespaces in paths")

    with TemporaryDirectory() as tmp_repo:
        tmp_repo = Path(tmp_repo)
        info(f"Repository: {tmp_repo}")

        await _exec(git_exe, "clone", "--no-local", pub_git_dir, tmp_repo)
        await _exec(git_exe, "-C", tmp_repo, "filter-repo", "--analyze")

        renames_backward = defaultdict[str, MutableSet[str]](set)
        current_equivalence_group = set[str]()
        for line in (
            await (tmp_repo / ".git/filter-repo/analysis/renames.txt").read_text()
        ).splitlines():  # The arrow is stupidly misleading, it represents equivalence classes, not maps
            if line.endswith(" ->"):
                for name in current_equivalence_group:
                    renames_backward[name] = current_equivalence_group
                current_equivalence_group = set[str]()
            else:
                assert line.startswith("    ")
                line = line[4:]
            current_equivalence_group.add(line)
        for name in current_equivalence_group:
            renames_backward[name] = current_equivalence_group

        paths_len = 0
        while paths_len != len(paths):
            paths_len = len(paths)
            for path in tuple(paths):
                paths.update(renames_backward[path])
        info(f"Paths with renames: {paths}")

        old_commits_with_files_added, _ = await _exec(
            git_exe,
            "-C",
            tmp_repo,
            "log",
            "--diff-filter=A",
            "--pretty=format:%H",
            "--reverse",
            "--stdin",
            input="\n".join(chain(("--",), paths)).encode(),
        )
        old_commits_with_files_added = set(
            commit.strip()
            for commit in old_commits_with_files_added.strip().splitlines()
        )

        async def get_path(commit: str):
            return (
                line.strip()
                for line in (
                    await _exec(
                        git_exe,
                        "-C",
                        tmp_repo,
                        "rev-list",
                        "--ancestry-path",
                        f"{commit}..HEAD",
                    )
                )[0]
                .strip()
                .splitlines()
            )

        for commit in tuple(old_commits_with_files_added):
            if commit in old_commits_with_files_added:
                old_commits_with_files_added.difference_update(await get_path(commit))
        info(f"Commit tails to rewrite: {old_commits_with_files_added}")

        unmapped_tags, _ = await _exec(
            git_exe,
            "-C",
            tmp_repo,
            "for-each-ref",
            "--format=%(refname) %(object)",
            "refs/tags",
        )

        with NamedTemporaryFile("xt", delete_on_close=False) as tmp_path_file:
            async with AsyncFile(tmp_path_file) as tmp_path_file_open:
                await tmp_path_file_open.write(
                    "\n".join(f"literal:{path}" for path in paths)
                )
            await _exec(
                git_exe,
                "-C",
                tmp_repo,
                "filter-repo",
                "--invert-paths",
                f"--paths-from-file={tmp_path_file.name}",
                "--refs=--ancestry-path",
                *(f"--refs={commit}~..HEAD" for commit in old_commits_with_files_added),
            )

        branch_name = (
            await _exec(git_exe, "-C", tmp_repo, "branch", "--show-current")
        )[0].strip()
        remote_name: str = tmp_repo.name.replace(" ", "_")
        await _exec(
            git_exe,
            "-C",
            tmp_repo,
            "filter-branch",
            "--commit-filter",
            'git commit-tree --gpg-sign "$@"',
            "--tag-name-filter",
            "cat",
            "--",
            "--ancestry-path",
            "HEAD",
            *(f"^{commit}~" for commit in old_commits_with_files_added),
        )

        # Not working yet
        """
        for tag in (
            (await _exec(git_exe, "-C", tmp_repo, "tag"))[0].strip().splitlines()
        ):
            await _exec(
                git_exe,
                "-C",
                tmp_repo,
                "tag",
                "--file",
                "-",
                "--force",
                "--sign",
                tag,
                f"{tag}^{{}}",
                input=(
                    await _exec(
                        git_exe,
                        "-C",
                        tmp_repo,
                        "for-each-ref",
                        f"refs/tags/{tag}",
                        "--format=%(contents)",
                    )
                )[0]
                .strip()
                .encode(),
            )
        """

        await _exec(
            git_exe,
            "--git-dir",
            pub_git_dir,
            "remote",
            "add",
            remote_name,
            tmp_repo,
        )
        await _exec(git_exe, "--git-dir", pub_git_dir, "remote", "update", remote_name)

    info(
        f"""Replace all commits in this repository with commits from the temporary remote:
$ git reset --hard {quote(f'refs/remotes/{remote_name}/{branch_name}')}
Remap the following tags manually:
{unmapped_tags.strip()}
Cleanup the temporary remote:
$ git remote remove {quote(remote_name)}"""
    )


def parser(parent: Callable[..., ArgumentParser] | None = None):
    prog = __package__ or __name__

    parser = (ArgumentParser if parent is None else parent)(
        prog=f"python -m {prog}",
        description="retract public files",
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
        "--allow-trailing-whitespaces-in-paths",
        action="store_true",
        default=False,
        help="allow trailing whitespaces in paths",
    )
    parser.add_argument(
        "-p",
        "--paths-file",
        action="store",
        required=True,
        type=Path,
        help="paths file",
    )

    @wraps(main)
    async def invoke(args: Namespace):
        await main(
            Arguments(
                allow_trailing_whitespaces_in_paths=args.allow_trailing_whitespaces_in_paths,
                paths_file=args.paths_file,
            )
        )

    parser.set_defaults(invoke=invoke)
    return parser


if __name__ == "__main__":
    __name__ = _FILE_PATH.stem
    basicConfig(level=INFO)
    entry = parser().parse_args(argv[1:])
    run(entry.invoke(entry))
