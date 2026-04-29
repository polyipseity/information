"""Mirror filtered commit history from the private repository to the public one.

Uses ``git filter-repo`` to rewrite history, stripping commits marked with
the ``Private-commit`` property, then splices the cleaned branch into the
public ``.git`` so it can be pushed.
"""

from argparse import ArgumentParser, Namespace
from collections import defaultdict
from collections.abc import Callable, MutableSet
from dataclasses import dataclass
from functools import wraps
from logging import INFO, basicConfig, error, info
from os import cpu_count
from pathlib import PurePath
from shlex import quote
from shutil import which as _sync_which
from subprocess import DEVNULL, PIPE
from sys import argv
from tempfile import NamedTemporaryFile, TemporaryDirectory
from typing import Any, final

from anyio import AsyncFile, Path, Semaphore, run_process
from asyncer import SoonValue, asyncify, create_task_group, runnify

"""Exported names from this module (none: standalone script, not importable as a library)."""
__all__ = ()

"Path to this script file."
_FILE_PATH = PurePath(__file__)
"Git commit message property key used to mark public-mirror commits."
_MESSAGE_PROPERTY_KEY = b"Private-commit"
"Path to the private repository's .git directory relative to this script."
_PRIVATE_GIT_DIRECTORY = _FILE_PATH / "../../private/.git"
"Path to the public repository's .git directory relative to this script."
_PUBLIC_GIT_DIRECTORY = _FILE_PATH / "../../.git"
"Semaphore that limits the number of concurrently running subprocesses."
_SUBPROCESS_SEMAPHORE = Semaphore(cpu_count() or 4)
"Version string for the publish script."
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
    """Parsed command-line arguments for the publish script."""

    allow_trailing_whitespaces_in_paths: bool
    paths_file: Path


@wraps(_sync_which)
async def _which2(cmd: str) -> str:
    """Async wrapper around shutil.which that raises FileNotFoundError if the command is not found."""
    ret = await asyncify(_sync_which)(cmd)
    assert not isinstance(ret, bytes)
    if ret is None:
        raise FileNotFoundError(cmd)
    return ret


@wraps(run_process)
async def _exec(
    *args: Any, input: bytes | bytearray | memoryview | None = None, **kwargs: Any
) -> tuple[str, str]:
    """Run a subprocess under the concurrency semaphore, logging stdout/stderr and raising on non-zero exit."""
    async with _SUBPROCESS_SEMAPHORE:
        proc = await run_process(
            *args,
            input=None if input is None else bytes(input),
            stdin=DEVNULL if input is None else PIPE,
            stdout=PIPE,
            stderr=PIPE,
            **kwargs,
        )
    stdout, stderr = (
        proc.stdout.decode(errors="backslashreplace"),
        proc.stderr.decode(errors="backslashreplace"),
    )
    if stdout:
        info(stdout)
    if stderr:
        error(stderr)
    if proc.returncode:
        raise ChildProcessError(proc.returncode, stderr)
    return stdout, stderr


async def main(args: Arguments) -> None:
    """Clone the private repo, filter its history, rebase with signatures, and splice into the public repo."""

    async def read_paths():
        """Read and return the set of literal path patterns from the paths file, stripping comments."""
        ret = set(
            line.replace("\\", "/")
            for line in (await args.paths_file.read_text()).splitlines()
            if not line.startswith("#")
        )
        ret.discard("")
        return ret

    sv_pri: SoonValue[Path] | None = None
    sv_pub: SoonValue[Path] | None = None
    sv_git: SoonValue[str] | None = None
    sv_paths: SoonValue[set[str]] | None = None
    async with create_task_group() as tg:
        sv_pri = tg.soonify(Path(_PRIVATE_GIT_DIRECTORY).resolve)(strict=True)
        sv_pub = tg.soonify(Path(_PUBLIC_GIT_DIRECTORY).resolve)(strict=True)
        sv_git = tg.soonify(_which2)("git")
        sv_paths = tg.soonify(read_paths)()
    assert (
        sv_pri is not None
        and sv_pub is not None
        and sv_git is not None
        and sv_paths is not None
    )
    pri_git_dir = sv_pri.value
    pub_git_dir = sv_pub.value
    git_exe = sv_git.value
    paths = sv_paths.value

    info(f"Paths: {paths}")
    if not args.allow_trailing_whitespaces_in_paths and any(
        path.rstrip() != path for path in paths
    ):
        raise ValueError("Found trailing whitespaces in paths")

    with TemporaryDirectory() as tmp_repo:
        tmp_repo = Path(tmp_repo)
        info(f"Repository: {tmp_repo}")

        await _exec(git_exe, "clone", "--no-local", pri_git_dir, tmp_repo)
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
                line = line[:-3]
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
                "--commit-callback",
                Rf"""
{_MESSAGE_PROPERTY_KEY=}
commit.message = commit.message.rstrip()
msg_lines = commit.message.splitlines()
msg_lines_rev = msg_lines[::-1]
try:
    last_para_rev_idx = msg_lines_rev.index(b"")
except ValueError:
    last_para_rev_idx = 0
prop_regex = re.compile(rb"^[a-zA-Z0-9_-]*: ")
if all(prop_regex.match(para) is None for para in msg_lines[-last_para_rev_idx:]):
    commit.message += b"\n"
commit.message += b"\n" + _MESSAGE_PROPERTY_KEY + b": " + commit.original_id
""",
                "--paths-from-file",
                tmp_path_file.name,
            )

        branch_name = (
            await _exec(git_exe, "-C", tmp_repo, "branch", "--show-current")
        )[0].strip()
        remote_name = tmp_repo.name.replace(" ", "_")
        await _exec(
            git_exe,
            "-C",
            tmp_repo,
            "rebase",
            "--exec",
            f"{quote(git_exe)} commit --amend --gpg-sign --no-edit --no-verify",
            "--rebase-merges",
            "--root",
        )

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
        f"""Merge commits from the temporary remote:
$ git merge --allow-unrelated-histories --gpg-sign {quote(f"refs/remotes/{remote_name}/{branch_name}")}
Resolve merge conflict if any.
Cleanup the temporary remote:
$ git remote remove {quote(remote_name)}"""
    )


def parser(parent: Callable[..., ArgumentParser] | None = None):
    """Build and return the argument parser for the publish script."""
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
        """Construct an Arguments instance from parsed namespace and call main."""
        await main(
            Arguments(
                allow_trailing_whitespaces_in_paths=args.allow_trailing_whitespaces_in_paths,
                paths_file=args.paths_file,
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


def __main__() -> None:
    """Entry point for running the script directly."""
    runnify(main0, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
