from asyncio.subprocess import DEVNULL, PIPE
from collections import defaultdict
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
from typing import Any, Callable, MutableSet, final

_FILE_PATH = PurePath(__file__)
_MESSAGE_PROPERTY_KEY = b"Private-commit"
_PRIVATE_GIT_DIRECTORY = _FILE_PATH / "../../private/.git"
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
        await proc.wait()
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

    pri_git_dir, pub_git_dir, git_exe, paths = await gather(
        Path(_PRIVATE_GIT_DIRECTORY).resolve(strict=True),
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
$ git merge --allow-unrelated-histories --gpg-sign {quote(f'refs/remotes/{remote_name}/{branch_name}')}
Resolve merge conflict if any.
Cleanup the temporary remote:
$ git remote remove {quote(remote_name)}"""
    )


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
