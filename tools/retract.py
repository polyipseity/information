from asyncio.subprocess import DEVNULL, PIPE
from collections import defaultdict
from itertools import chain
from os import cpu_count
from pathlib import PurePath
from shlex import quote
from tempfile import NamedTemporaryFile, TemporaryDirectory
from aioshutil import which
from anyio import AsyncFile, Path
from argparse import ZERO_OR_MORE, ArgumentParser, Namespace
from asyncio import BoundedSemaphore, create_subprocess_exec, gather, run
from dataclasses import dataclass
from functools import wraps
from logging import INFO, basicConfig, error, info
from sys import argv
from typing import Any, Callable, MutableSet, Sequence, final

_FILE_PATH = PurePath(__file__)
_NULL_SHA = "0000000000000000000000000000000000000000"
_PGP_SIGNATURE_HEADER = "-----BEGIN PGP SIGNATURE-----"
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
    refs: Sequence[str]

    def __post_init__(self) -> None:
        object.__setattr__(self, "refs", tuple(self.refs))


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

    # `delete` is `False` so that tags can be updated
    with TemporaryDirectory(delete=False) as tmp_repo:
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
        old_commits_with_files_added = set(old_commits_with_files_added.splitlines())

        async def get_path(commit: str):
            return (
                await _exec(
                    git_exe,
                    "-C",
                    tmp_repo,
                    "rev-list",
                    "--ancestry-path",
                    f"{commit}..HEAD",
                )
            )[0].splitlines()

        for commit in tuple(old_commits_with_files_added):
            if commit in old_commits_with_files_added:
                old_commits_with_files_added.difference_update(await get_path(commit))
        info(f"Commit tails to rewrite: {old_commits_with_files_added}")

        initial_commits, _ = await _exec(
            git_exe, "-C", tmp_repo, "rev-list", "--max-parents=0", "--all"
        )
        initial_commits = frozenset(initial_commits.splitlines())

        unmapped_tags, _ = await _exec(
            git_exe,
            "-C",
            tmp_repo,
            "for-each-ref",
            "--format=%(refname) %(object)",
            "refs/tags",
        )
        unmapped_tags = {
            key.removeprefix("refs/tags/"): val
            for line in unmapped_tags.splitlines()
            for key, val in (line.split(" ", 1),)
        }

        with NamedTemporaryFile("xt", delete_on_close=False) as tmp_path_file:
            async with AsyncFile(tmp_path_file) as tmp_path_file_open:
                await tmp_path_file_open.write(
                    "\n".join(f"literal:{path}" for path in paths)
                )
            # Please ensure there are no unstaged and uncommitted changes, otherwise `filter-repo` will miss many commits.
            await _exec(
                git_exe,
                "-C",
                tmp_repo,
                "filter-repo",
                "--invert-paths",
                f"--paths-from-file={tmp_path_file.name}",
                *(
                    f"--refs=--ancestry-path={commit}~"  # put before other paths or `filter-repo` will not work
                    for commit in old_commits_with_files_added - initial_commits
                ),
                *(
                    f"--refs=--ancestry-path={commit}"  # put before other paths or `filter-repo` will not work
                    for commit in old_commits_with_files_added & initial_commits
                ),
                "--refs=HEAD",
                *(f"--refs={ref}" for ref in args.refs),
                *(
                    f"--refs={commit}~..{ref}"
                    for ref in ("HEAD", *args.refs)
                    for commit in old_commits_with_files_added - initial_commits
                ),
            )
        commit_map_text = await (tmp_repo / ".git/filter-repo/commit-map").read_text()
        commit_map = dict(
            line.split(" ", 1)
            for line in commit_map_text.splitlines()[1:]
            if _NULL_SHA not in line
        )
        await (tmp_repo / ".git/filter-repo/new-commits").write_text(
            "\n".join(
                line2
                for line in commit_map_text.splitlines()[1:]
                for line2 in (line[line.index(" ") + 1 :],)
                if line2 != _NULL_SHA
            )
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
            'grep -q "${GIT_COMMIT}" ../../.git/filter-repo/new-commits && (echo -n "${GIT_COMMIT} " >> ../../.git/filter-branch/commit-map; git commit-tree --gpg-sign "$@" | tee -a ../../.git/filter-branch/commit-map) || echo "${GIT_COMMIT}"',
            "--setup",
            "mkdir ../../.git/filter-branch",
            "--tag-name-filter",
            "cat",
            "--",
            "HEAD",
            *(commit_map[ref] for ref in args.refs if ref in commit_map),
        )

        commit_map_text2 = await (
            tmp_repo / ".git/filter-branch/commit-map"
        ).read_text()
        commit_map2 = dict(line.split(" ", 1) for line in commit_map_text2.splitlines())

        def map_old_commit(old_commit: str):
            return commit_map2.get(commit_map.get(old_commit, ""), "")

        for tag, old_commit in tuple(unmapped_tags.items()):
            if not (new_commit := map_old_commit(old_commit)):
                if old_commit not in commit_map:
                    del unmapped_tags[tag]
                continue
            tag_msg = (
                await _exec(
                    git_exe,
                    "-C",
                    tmp_repo,
                    "for-each-ref",
                    f"refs/tags/{tag}",
                    "--format=%(contents)",
                )
            )[0]
            try:
                signature_idx = tag_msg.index(_PGP_SIGNATURE_HEADER)
            except ValueError:
                pass
            else:
                tag_msg = tag_msg[:signature_idx]
            tag_msg = tag_msg.strip()
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
                new_commit,
                input=tag_msg.encode(),
            )
            del unmapped_tags[tag]

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

        tmp_repo = await tmp_repo.resolve(strict=True)
    info(
        f"""Commit maps:
1. {tmp_repo / ".git/filter-repo/commit-map"}
2. {tmp_repo / ".git/filter-branch/commit-map"}
Check the following unmapped tags:
{'\n'.join(' '.join(item) for item in unmapped_tags.items()) or '(none)'}
Replace all commits in this repository with commits from the temporary remote:
$ git reset --hard {quote(f'refs/remotes/{remote_name}/{branch_name}')}
$ git fetch --force --tags {quote(remote_name)}
Cleanup the temporary remote:
$ git remote remove {quote(remote_name)}
$ rm -fr {tmp_repo}"""
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
    parser.add_argument(
        "--ref",
        action="store",
        nargs=ZERO_OR_MORE,
        type=str,
        default=(),
        help="additional refs",
        dest="refs",
    )

    @wraps(main)
    async def invoke(args: Namespace):
        await main(
            Arguments(
                allow_trailing_whitespaces_in_paths=args.allow_trailing_whitespaces_in_paths,
                paths_file=args.paths_file,
                refs=args.refs,
            )
        )

    parser.set_defaults(invoke=invoke)
    return parser


if __name__ == "__main__":
    __name__ = _FILE_PATH.stem
    basicConfig(level=INFO)
    entry = parser().parse_args(argv[1:])
    run(entry.invoke(entry))
