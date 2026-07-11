"""Tests for scripts/retract.py."""

from __future__ import annotations

import os
from argparse import ArgumentParser
from pathlib import Path, PurePath

import pytest

from scripts import retract as _mod


class TestConstants:
    """Tests for module-level constants."""

    def test_file_path_type(self) -> None:
        """_FILE_PATH should be a PurePath."""
        assert isinstance(_mod._FILE_PATH, PurePath)

    def test_version_string(self) -> None:
        """_VERSION should be a string."""
        assert isinstance(_mod._VERSION, str)

    def test_null_sha(self) -> None:
        """_NULL_SHA should be the 40-char zero SHA."""
        assert _mod._NULL_SHA == "0000000000000000000000000000000000000000"

    def test_pgp_signature_header(self) -> None:
        """_PGP_SIGNATURE_HEADER should be a string."""
        assert isinstance(_mod._PGP_SIGNATURE_HEADER, str)
        assert "PGP" in _mod._PGP_SIGNATURE_HEADER

    def test_public_git_dir_type(self) -> None:
        """_PUBLIC_GIT_DIRECTORY should be a PurePath."""
        assert isinstance(_mod._PUBLIC_GIT_DIRECTORY, PurePath)

    def test_semaphore_type(self) -> None:
        """_SUBPROCESS_SEMAPHORE should be a Semaphore."""
        from anyio import Semaphore

        assert isinstance(_mod._SUBPROCESS_SEMAPHORE, Semaphore)


class TestWhich2:
    """Tests for the _which2 async function."""

    @pytest.mark.anyio
    async def test_found(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should return path when command is found."""
        monkeypatch.setattr("scripts.retract._sync_which", lambda cmd: "/usr/bin/git")
        result = await _mod._which2("git")  # noqa: SLF001
        assert result == "/usr/bin/git"

    @pytest.mark.anyio
    async def test_not_found(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should raise FileNotFoundError when command is not found."""
        monkeypatch.setattr("scripts.retract._sync_which", lambda cmd: None)
        with pytest.raises(FileNotFoundError, match="nonexistent"):
            await _mod._which2("nonexistent")  # noqa: SLF001


class MockProcessResult:
    """Mock result from anyio.run_process."""

    def __init__(
        self,
        stdout: bytes = b"",
        stderr: bytes = b"",
        returncode: int = 0,
    ) -> None:
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode


class TestExec:
    """Tests for the _exec async function."""

    @pytest.mark.anyio
    async def test_success(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should return (stdout, stderr) on subprocess success."""
        async def mock_run_process(*args: object, **kwargs: object) -> MockProcessResult:
            return MockProcessResult(stdout=b"out\n", stderr=b"", returncode=0)

        monkeypatch.setattr("scripts.retract.run_process", mock_run_process)
        stdout, stderr = await _mod._exec("git", "status")  # noqa: SLF001
        assert stdout == "out\n"
        assert stderr == ""

    @pytest.mark.anyio
    async def test_failure(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should raise ChildProcessError on non-zero return code."""
        async def mock_run_process(*args: object, **kwargs: object) -> MockProcessResult:
            return MockProcessResult(stdout=b"", stderr=b"fatal", returncode=1)

        monkeypatch.setattr("scripts.retract.run_process", mock_run_process)
        with pytest.raises(ChildProcessError):
            await _mod._exec("git", "status")  # noqa: SLF001

    @pytest.mark.anyio
    async def test_passes_input(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should pass input bytes through to run_process."""
        captured: dict[str, object] = {}

        async def mock_run_process(*args: object, **kwargs: object) -> MockProcessResult:
            captured.update(kwargs)
            return MockProcessResult(stdout=b"", stderr=b"", returncode=0)

        monkeypatch.setattr("scripts.retract.run_process", mock_run_process)
        await _mod._exec("git", "log", input=b"test\n")  # noqa: SLF001
        assert captured.get("input") == b"test\n"

    @pytest.mark.anyio
    async def test_empty_input_passes_none(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should pass input=None when no input is given."""
        captured: dict[str, object] = {}

        async def mock_run_process(*args: object, **kwargs: object) -> MockProcessResult:
            captured.update(kwargs)
            return MockProcessResult(stdout=b"", stderr=b"", returncode=0)

        monkeypatch.setattr("scripts.retract.run_process", mock_run_process)
        await _mod._exec("git", "status")  # noqa: SLF001
        assert captured.get("input") is None


class TestArguments:
    """Tests for the Arguments dataclass."""

    def test_create(self) -> None:
        """Should create instance with valid arguments."""
        p = Path("test.txt")
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=p,
            refs=(),
        )
        assert args.allow_trailing_whitespaces_in_paths is False
        assert args.paths_file is p
        assert args.refs == ()

    def test_frozen(self) -> None:
        """Should be immutable (frozen dataclass)."""
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=Path("test.txt"),
            refs=(),
        )
        with pytest.raises(AttributeError):
            args.allow_trailing_whitespaces_in_paths = True  # type: ignore[misc]

    def test_allow_trailing_whitespaces_true(self) -> None:
        """Should store True for allow_trailing_whitespaces_in_paths."""
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=True,
            paths_file=Path("test.txt"),
            refs=(),
        )
        assert args.allow_trailing_whitespaces_in_paths is True

    def test_refs_coerced_to_tuple(self) -> None:
        """__post_init__ should coerce refs Sequence to tuple."""
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=Path("test.txt"),
            refs=["branch1", "branch2"],
        )
        assert args.refs == ("branch1", "branch2")
        assert isinstance(args.refs, tuple)


class TestParser:
    """Tests for the parser() function."""

    def test_returns_argument_parser(self) -> None:
        """Should return an ArgumentParser instance."""
        p = _mod.parser()
        assert isinstance(p, ArgumentParser)

    def test_prog_contains_retract(self) -> None:
        """Should have 'retract' in the description."""
        p = _mod.parser()
        assert "retract" in p.description

    def test_has_version_action(self) -> None:
        """Should define a --version action."""
        p = _mod.parser()
        actions = {a.dest: a for a in p._actions}
        assert "version" in actions

    def test_paths_file_required(self) -> None:
        """Should define --paths-file as required."""
        p = _mod.parser()
        actions = {a.dest: a for a in p._actions}
        assert actions["paths_file"].required is True

    def test_allow_trailing_whitespaces_action(self) -> None:
        """Should define --allow-trailing-whitespaces-in-paths."""
        p = _mod.parser()
        actions = {a.dest: a for a in p._actions}
        assert "allow_trailing_whitespaces_in_paths" in actions
        assert actions["allow_trailing_whitespaces_in_paths"].default is False

    def test_has_ref_action(self) -> None:
        """Should define a --ref action."""
        p = _mod.parser()
        actions = {a.dest: a for a in p._actions}
        assert "refs" in actions

    def test_default_invoke(self) -> None:
        """Parser should set an 'invoke' default."""
        p = _mod.parser()
        assert callable(p.get_default("invoke"))


class TestMain:
    """Tests for the main() async function."""

    @pytest.mark.anyio
    async def test_success(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Should run the full retract pipeline without errors (empty data flow)."""
        # Setup: create public git dir
        (tmp_path / "public" / ".git").mkdir(parents=True)
        monkeypatch.setattr(
            "scripts.retract._PUBLIC_GIT_DIRECTORY",
            PurePath(os.fspath(tmp_path / "public" / ".git")),
        )

        # Setup: paths file
        paths_file = tmp_path / "paths.txt"
        paths_file.write_text("secret.txt\n")
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=_mod.Path(os.fspath(paths_file)),
            refs=(),
        )

        # Mock _which2
        async def mock_which2(cmd: str) -> str:
            return "/usr/bin/git"

        monkeypatch.setattr("scripts.retract._which2", mock_which2)

        # Mock TemporaryDirectory(delete=False) with a controlled path
        fake_tmp = tmp_path / "fakerepo"
        fake_tmp.mkdir(parents=True, exist_ok=True)
        # Create directory structure needed during main()
        (fake_tmp / ".git" / "filter-repo" / "analysis").mkdir(
            parents=True, exist_ok=True
        )
        (fake_tmp / ".git" / "filter-repo" / "analysis" / "renames.txt").write_text("")
        (fake_tmp / ".git" / "filter-repo" / "commit-map").write_text("")
        (fake_tmp / ".git" / "filter-branch").mkdir(parents=True, exist_ok=True)
        (fake_tmp / ".git" / "filter-branch" / "commit-map").write_text("")

        class FakeTemporaryDirectory:
            def __init__(self, **kw: object) -> None:
                self.name = os.fspath(fake_tmp)

            def __enter__(self) -> str:
                return self.name

            def __exit__(self, *args: object) -> None:
                pass

        monkeypatch.setattr(
            "scripts.retract.TemporaryDirectory", FakeTemporaryDirectory
        )

        # Mock _exec: 10 calls for the empty-data-flow path through main()
        exec_results: list[tuple[str, str]] = [
            ("", ""),          # 0: git clone
            ("", ""),          # 1: filter-repo --analyze
            ("", ""),          # 2: git log --diff-filter=A (empty result)
            ("", ""),          # 3: rev-list --max-parents=0 --all
            ("", ""),          # 4: for-each-ref refs/tags
            ("", ""),          # 5: filter-repo --invert-paths
            ("main\n", ""),    # 6: branch --show-current
            ("", ""),          # 7: filter-branch
            ("", ""),          # 8: remote add
            ("", ""),          # 9: remote update
        ]
        exec_index = [0]

        async def mock_exec(*a: object, **kw: object) -> tuple[str, str]:
            idx = exec_index[0]
            exec_index[0] += 1
            if idx >= len(exec_results):
                msg = f"Unexpected _exec call #{idx}: args={a}"
                raise RuntimeError(msg)
            return exec_results[idx]

        monkeypatch.setattr("scripts.retract._exec", mock_exec)

        # Route logging output to stdout so capsys captures it
        monkeypatch.setattr("scripts.retract.info", print)

        # Act
        await _mod.main(args)

        # Assert: final output contains commit maps and cleanup instructions
        captured = capsys.readouterr()
        assert "Commit maps" in captured.out
        assert "filter-repo/commit-map" in captured.out
        assert "filter-branch/commit-map" in captured.out
        assert "git reset --hard" in captured.out

    @pytest.mark.anyio
    async def test_trailing_whitespace_error(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
    ) -> None:
        """Should raise ValueError when paths have trailing whitespace."""
        (tmp_path / "public" / ".git").mkdir(parents=True)
        monkeypatch.setattr(
            "scripts.retract._PUBLIC_GIT_DIRECTORY",
            PurePath(os.fspath(tmp_path / "public" / ".git")),
        )

        paths_file = tmp_path / "paths.txt"
        paths_file.write_text("secret.txt \n")  # trailing space
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=_mod.Path(os.fspath(paths_file)),
            refs=(),
        )

        async def mock_which2(cmd: str) -> str:
            return "/usr/bin/git"

        monkeypatch.setattr("scripts.retract._which2", mock_which2)

        with pytest.raises(ValueError, match="Found trailing whitespaces in paths"):
            await _mod.main(args)

    @pytest.mark.anyio
    async def test_with_refs(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Should handle additional --ref refs without error."""
        (tmp_path / "public" / ".git").mkdir(parents=True)
        monkeypatch.setattr(
            "scripts.retract._PUBLIC_GIT_DIRECTORY",
            PurePath(os.fspath(tmp_path / "public" / ".git")),
        )

        paths_file = tmp_path / "paths.txt"
        paths_file.write_text("secret.txt\n")
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=_mod.Path(os.fspath(paths_file)),
            refs=("other-branch",),
        )

        async def mock_which2(cmd: str) -> str:
            return "/usr/bin/git"

        monkeypatch.setattr("scripts.retract._which2", mock_which2)

        fake_tmp = tmp_path / "fakerepo2"
        fake_tmp.mkdir(parents=True, exist_ok=True)
        (fake_tmp / ".git" / "filter-repo" / "analysis").mkdir(
            parents=True, exist_ok=True
        )
        (fake_tmp / ".git" / "filter-repo" / "analysis" / "renames.txt").write_text("")
        (fake_tmp / ".git" / "filter-repo" / "commit-map").write_text("")
        (fake_tmp / ".git" / "filter-branch").mkdir(parents=True, exist_ok=True)
        (fake_tmp / ".git" / "filter-branch" / "commit-map").write_text("")

        class FakeTemporaryDirectory2:
            def __init__(self, **kw: object) -> None:
                self.name = os.fspath(fake_tmp)

            def __enter__(self) -> str:
                return self.name

            def __exit__(self, *args: object) -> None:
                pass

        monkeypatch.setattr(
            "scripts.retract.TemporaryDirectory", FakeTemporaryDirectory2
        )

        exec_results: list[tuple[str, str]] = [
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("", ""),
            ("main\n", ""),
            ("", ""),
            ("", ""),
            ("", ""),
        ]
        exec_index = [0]

        async def mock_exec(*a: object, **kw: object) -> tuple[str, str]:
            idx = exec_index[0]
            exec_index[0] += 1
            if idx >= len(exec_results):
                msg = f"Unexpected _exec call #{idx}: args={a}"
                raise RuntimeError(msg)
            return exec_results[idx]

        monkeypatch.setattr("scripts.retract._exec", mock_exec)

        # Route logging output to stdout so capsys captures it
        monkeypatch.setattr("scripts.retract.info", print)

        await _mod.main(args)
        captured = capsys.readouterr()
        assert "Commit maps" in captured.out
