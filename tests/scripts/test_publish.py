"""Tests for scripts/publish.py."""

from argparse import ArgumentParser
from os import PathLike, fspath
from pathlib import PurePath
from typing import Any, cast

import pytest
from anyio import Path, Semaphore

from scripts import publish as _mod

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestConstants:
    """Tests for module-level constants."""

    def test_file_path_type(self) -> None:
        """_FILE_PATH should be a PurePath."""
        assert isinstance(_mod._FILE_PATH, PurePath)

    def test_version_string(self) -> None:
        """_VERSION should be a string."""
        assert isinstance(_mod._VERSION, str)

    def test_private_git_dir_type(self) -> None:
        """_PRIVATE_GIT_DIRECTORY should be a PurePath."""
        assert isinstance(_mod._PRIVATE_GIT_DIRECTORY, PurePath)

    def test_public_git_dir_type(self) -> None:
        """_PUBLIC_GIT_DIRECTORY should be a PurePath."""
        assert isinstance(_mod._PUBLIC_GIT_DIRECTORY, PurePath)

    def test_semaphore_type(self) -> None:
        """_SUBPROCESS_SEMAPHORE should be a Semaphore."""
        assert isinstance(_mod._SUBPROCESS_SEMAPHORE, Semaphore)

    def test_message_property_key_type(self) -> None:
        """_MESSAGE_PROPERTY_KEY should be bytes."""
        assert isinstance(_mod._MESSAGE_PROPERTY_KEY, bytes)


class TestWhich2:
    """Tests for the _which2 async function."""

    @pytest.mark.anyio
    async def test_found(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should return path when command is found."""
        monkeypatch.setattr("scripts.publish._sync_which", lambda cmd: "/usr/bin/git")
        result = await _mod._which2("git")  # noqa: SLF001
        assert result == "/usr/bin/git"

    @pytest.mark.anyio
    async def test_not_found(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should raise FileNotFoundError when command is not found."""
        monkeypatch.setattr("scripts.publish._sync_which", lambda cmd: None)
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
        """Store process output and return code."""
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode


class TestExec:
    """Tests for the _exec async function."""

    @pytest.mark.anyio
    async def test_success(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should return (stdout, stderr) on subprocess success."""
        async def mock_run_process(*args: object, **kwargs: object) -> MockProcessResult:
            """Return successful process result."""
            return MockProcessResult(stdout=b"out\n", stderr=b"", returncode=0)

        monkeypatch.setattr("scripts.publish.run_process", mock_run_process)
        stdout, stderr = await _mod._exec("git", "status")  # noqa: SLF001
        assert stdout == "out\n"
        assert stderr == ""

    @pytest.mark.anyio
    async def test_failure(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should raise ChildProcessError on non-zero return code."""
        async def mock_run_process(*args: object, **kwargs: object) -> MockProcessResult:
            """Return failed process result."""
            return MockProcessResult(stdout=b"", stderr=b"fatal", returncode=1)

        monkeypatch.setattr("scripts.publish.run_process", mock_run_process)
        with pytest.raises(ChildProcessError):
            await _mod._exec("git", "status")  # noqa: SLF001

    @pytest.mark.anyio
    async def test_passes_input(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should pass input bytes through to run_process."""
        captured: dict[str, object] = {}

        async def mock_run_process(*args: object, **kwargs: object) -> MockProcessResult:
            """Capture kwargs and return empty process result."""
            captured.update(kwargs)
            return MockProcessResult(stdout=b"", stderr=b"", returncode=0)

        monkeypatch.setattr("scripts.publish.run_process", mock_run_process)
        await _mod._exec("git", "log", input=b"test\n")  # noqa: SLF001
        assert captured.get("input") == b"test\n"

    @pytest.mark.anyio
    async def test_empty_input_passes_none(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should pass input=None when no input is given."""
        captured: dict[str, object] = {}

        async def mock_run_process(*args: object, **kwargs: object) -> MockProcessResult:
            """Capture kwargs and return empty process result."""
            captured.update(kwargs)
            return MockProcessResult(stdout=b"", stderr=b"", returncode=0)

        monkeypatch.setattr("scripts.publish.run_process", mock_run_process)
        await _mod._exec("git", "status")  # noqa: SLF001
        assert captured.get("input") is None


class TestArguments:
    """Tests for the Arguments dataclass."""

    def test_create(self) -> None:
        """Should create instance with valid arguments."""
        p = _mod.Path("test.txt")
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=p,
        )
        assert args.allow_trailing_whitespaces_in_paths is False
        assert args.paths_file is p

    def test_frozen(self) -> None:
        """Should be immutable (frozen dataclass)."""
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=_mod.Path("test.txt"),
        )
        with pytest.raises(AttributeError):
            cast(Any, args).allow_trailing_whitespaces_in_paths = True

    def test_allow_trailing_whitespaces_true(self) -> None:
        """Should store True for allow_trailing_whitespaces_in_paths."""
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=True,
            paths_file=_mod.Path("test.txt"),
        )
        assert args.allow_trailing_whitespaces_in_paths is True


class TestParser:
    """Tests for the parser() function."""

    def test_returns_argument_parser(self) -> None:
        """Should return an ArgumentParser instance."""
        p = _mod.parser()
        assert isinstance(p, ArgumentParser)

    def test_prog_contains_publish(self) -> None:
        """Should have 'publish' in the description."""
        p = _mod.parser()
        assert "publish" in p.description

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
        tmp_path: PathLike[str],
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Should run the full publish pipeline without errors."""
        tmp = Path(tmp_path)
        # Setup: create git dirs that resolve(strict=True) will find
        await (tmp / "private" / ".git").mkdir(parents=True)
        await (tmp / "public" / ".git").mkdir(parents=True)
        monkeypatch.setattr(
            "scripts.publish._PRIVATE_GIT_DIRECTORY",
            PurePath(fspath(tmp / "private" / ".git")),
        )
        monkeypatch.setattr(
            "scripts.publish._PUBLIC_GIT_DIRECTORY",
            PurePath(fspath(tmp / "public" / ".git")),
        )

        # Setup: paths file
        paths_file = tmp / "paths.txt"
        await paths_file.write_text("file1\nfile2\n")
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=_mod.Path(fspath(paths_file)),
        )

        # Mock _which2 (async, for soonify)
        async def mock_which2(cmd: str) -> str:
            """Return a fake git path."""
            return "/usr/bin/git"

        monkeypatch.setattr("scripts.publish._which2", mock_which2)

        # Mock _exec with ordered results for the 7 subprocess calls
        exec_results: list[tuple[str, str]] = [
            ("", ""),          # 0: git clone
            ("", ""),          # 1: filter-repo --analyze
            ("", ""),          # 2: filter-repo --commit-callback
            ("main\n", ""),    # 3: branch --show-current
            ("", ""),          # 4: rebase
            ("", ""),          # 5: remote add
            ("", ""),          # 6: remote update
        ]
        exec_index = [0]

        async def mock_exec(*a: object, **kw: object) -> tuple[str, str]:
            """Return next pre-defined exec result."""
            idx = exec_index[0]
            exec_index[0] += 1
            if idx >= len(exec_results):
                msg = f"Unexpected _exec call #{idx}: args={a}"
                raise RuntimeError(msg)
            return exec_results[idx]

        monkeypatch.setattr("scripts.publish._exec", mock_exec)

        # Mock TemporaryDirectory to use a controlled path under tmp_path
        fake_tmp = tmp / "fakerepo"
        await fake_tmp.mkdir(parents=True, exist_ok=True)
        await (fake_tmp / ".git" / "filter-repo" / "analysis").mkdir(
            parents=True, exist_ok=True
        )
        await (fake_tmp / ".git" / "filter-repo" / "analysis" / "renames.txt").write_text("")

        class FakeTemporaryDirectory:
            """Fake temp dir pointing at a controlled path."""

            def __init__(self, **kw: object) -> None:
                """Store the controlled path."""
                self.name = fspath(fake_tmp)

            def __enter__(self) -> str:
                """Return the controlled path."""
                return self.name

            def __exit__(self, *args: object) -> None:
                """No-op cleanup."""
                pass

        monkeypatch.setattr(
            "scripts.publish.TemporaryDirectory", FakeTemporaryDirectory
        )

        # Route logging output to stdout so capsys captures it
        monkeypatch.setattr("scripts.publish.info", print)

        # Act
        await _mod.main(args)

        # Assert: final output mentions merge instructions
        captured = capsys.readouterr()
        assert "Merge commits" in captured.out

    @pytest.mark.anyio
    async def test_trailing_whitespace_error(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: PathLike[str],
    ) -> None:
        """Should raise ValueError when paths have trailing whitespace."""
        tmp = Path(tmp_path)
        await (tmp / "private" / ".git").mkdir(parents=True)
        await (tmp / "public" / ".git").mkdir(parents=True)
        monkeypatch.setattr(
            "scripts.publish._PRIVATE_GIT_DIRECTORY",
            PurePath(fspath(tmp / "private" / ".git")),
        )
        monkeypatch.setattr(
            "scripts.publish._PUBLIC_GIT_DIRECTORY",
            PurePath(fspath(tmp / "public" / ".git")),
        )

        # Paths file with trailing whitespace
        paths_file = tmp / "paths.txt"
        await paths_file.write_text("file1 \n")
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=_mod.Path(fspath(paths_file)),
        )

        async def mock_which2(cmd: str) -> str:
            """Return a fake git path."""
            return "/usr/bin/git"

        monkeypatch.setattr("scripts.publish._which2", mock_which2)

        with pytest.raises(ValueError, match="Found trailing whitespaces in paths"):
            await _mod.main(args)

    @pytest.mark.anyio
    async def test_allow_trailing_whitespace_ok(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: PathLike[str],
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Should allow trailing whitespace when the flag is set."""
        tmp = Path(tmp_path)
        await (tmp / "private" / ".git").mkdir(parents=True)
        await (tmp / "public" / ".git").mkdir(parents=True)
        monkeypatch.setattr(
            "scripts.publish._PRIVATE_GIT_DIRECTORY",
            PurePath(fspath(tmp / "private" / ".git")),
        )
        monkeypatch.setattr(
            "scripts.publish._PUBLIC_GIT_DIRECTORY",
            PurePath(fspath(tmp / "public" / ".git")),
        )

        paths_file = tmp / "paths.txt"
        await paths_file.write_text("file1 \n")
        args = _mod.Arguments(
            allow_trailing_whitespaces_in_paths=True,
            paths_file=_mod.Path(fspath(paths_file)),
        )

        async def mock_which2(cmd: str) -> str:
            """Return a fake git path."""
            return "/usr/bin/git"

        monkeypatch.setattr("scripts.publish._which2", mock_which2)

        # Mock _exec for the pipeline
        exec_results: list[tuple[str, str]] = [
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
            """Return next pre-defined exec result."""
            idx = exec_index[0]
            exec_index[0] += 1
            if idx >= len(exec_results):
                msg = f"Unexpected _exec call #{idx}: args={a}"
                raise RuntimeError(msg)
            return exec_results[idx]

        monkeypatch.setattr("scripts.publish._exec", mock_exec)

        fake_tmp = tmp / "fakerepo2"
        await fake_tmp.mkdir(parents=True, exist_ok=True)
        await (fake_tmp / ".git" / "filter-repo" / "analysis").mkdir(
            parents=True, exist_ok=True
        )
        await (fake_tmp / ".git" / "filter-repo" / "analysis" / "renames.txt").write_text("")

        class FakeTemporaryDirectory2:
            """Fake temp dir pointing at a controlled path."""

            def __init__(self, **kw: object) -> None:
                """Store the controlled path."""
                self.name = fspath(fake_tmp)

            def __enter__(self) -> str:
                """Return the controlled path."""
                return self.name

            def __exit__(self, *args: object) -> None:
                """No-op cleanup."""
                pass

        monkeypatch.setattr(
            "scripts.publish.TemporaryDirectory", FakeTemporaryDirectory2
        )

        # Route logging output to stdout so capsys captures it
        monkeypatch.setattr("scripts.publish.info", print)

        await _mod.main(args)
        captured = capsys.readouterr()
        assert "Merge commits" in captured.out
