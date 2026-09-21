"""Tests for scripts/retract.py and scripts/publish.py.

Merged from test_retract.py and test_publish.py. Only the high-value
integration tests (TestMain) are retained; trivial constant/boilerplate
tests were removed.
"""

from os import PathLike, fspath
from pathlib import PurePath

import pytest
from anyio import Path

from scripts import publish as _publish_mod
from scripts import retract as _retract_mod

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestRetractMain:
    """Tests for retract.main() async function."""

    @pytest.mark.anyio
    async def test_success(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: PathLike[str],
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Should run the full retract pipeline without errors (empty data flow)."""
        tmp = Path(tmp_path)
        await (tmp / "public" / ".git").mkdir(parents=True)
        monkeypatch.setattr(
            "scripts.retract._PUBLIC_GIT_DIRECTORY",
            PurePath(fspath(tmp / "public" / ".git")),
        )

        paths_file = tmp / "paths.txt"
        await paths_file.write_text("secret.txt\n")
        args = _retract_mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=_retract_mod.Path(fspath(paths_file)),
            refs=(),
        )

        async def mock_which2(cmd: str) -> str:
            """Mock _which2 returning /usr/bin/git."""
            return "/usr/bin/git"

        monkeypatch.setattr("scripts.retract._which2", mock_which2)

        fake_tmp = tmp / "fakerepo"
        await fake_tmp.mkdir(parents=True, exist_ok=True)
        await (fake_tmp / ".git" / "filter-repo" / "analysis").mkdir(
            parents=True, exist_ok=True
        )
        await (
            fake_tmp / ".git" / "filter-repo" / "analysis" / "renames.txt"
        ).write_text("")
        await (fake_tmp / ".git" / "filter-repo" / "commit-map").write_text("")
        await (fake_tmp / ".git" / "filter-branch").mkdir(parents=True, exist_ok=True)
        await (fake_tmp / ".git" / "filter-branch" / "commit-map").write_text("")

        class FakeTemporaryDirectory:
            """Fake TemporaryDirectory that points to a fixed path."""

            def __init__(self, **kw: object) -> None:
                """Store the fake tmp directory path."""
                self.name = fspath(fake_tmp)

            def __enter__(self) -> str:
                """Return the fake directory path."""
                return self.name

            def __exit__(self, *args: object) -> None:
                """No-op cleanup."""
                pass

        monkeypatch.setattr(
            "scripts.retract.TemporaryDirectory", FakeTemporaryDirectory
        )

        exec_results: list[tuple[str, str]] = [
            ("", ""),  # 0: git clone
            ("", ""),  # 1: filter-repo --analyze
            ("", ""),  # 2: git log --diff-filter=A (empty result)
            ("", ""),  # 3: rev-list --max-parents=0 --all
            ("", ""),  # 4: for-each-ref refs/tags
            ("", ""),  # 5: filter-repo --invert-paths
            ("main\n", ""),  # 6: branch --show-current
            ("", ""),  # 7: filter-branch
            ("", ""),  # 8: remote add
            ("", ""),  # 9: remote update
        ]
        exec_index = [0]

        async def mock_exec(*a: object, **kw: object) -> tuple[str, str]:
            """Mock _exec returning predetermined results by call index."""
            idx = exec_index[0]
            exec_index[0] += 1
            if idx >= len(exec_results):
                msg = f"Unexpected _exec call #{idx}: args={a}"
                raise RuntimeError(msg)
            return exec_results[idx]

        monkeypatch.setattr("scripts.retract._exec", mock_exec)
        monkeypatch.setattr("scripts.retract.info", print)

        await _retract_mod.main(args)

        captured = capsys.readouterr()
        assert "Commit maps" in captured.out
        assert "filter-repo/commit-map" in captured.out
        assert "filter-branch/commit-map" in captured.out
        assert "git reset --hard" in captured.out

    @pytest.mark.anyio
    async def test_trailing_whitespace_error(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: PathLike[str],
    ) -> None:
        """Should raise ValueError when paths have trailing whitespace."""
        tmp = Path(tmp_path)
        await (tmp / "public" / ".git").mkdir(parents=True)
        monkeypatch.setattr(
            "scripts.retract._PUBLIC_GIT_DIRECTORY",
            PurePath(fspath(tmp / "public" / ".git")),
        )

        paths_file = tmp / "paths.txt"
        await paths_file.write_text("secret.txt \n")
        args = _retract_mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=_retract_mod.Path(fspath(paths_file)),
            refs=(),
        )

        async def mock_which2(cmd: str) -> str:
            """Mock _which2 returning /usr/bin/git."""
            return "/usr/bin/git"

        monkeypatch.setattr("scripts.retract._which2", mock_which2)

        with pytest.raises(ValueError, match="Found trailing whitespaces in paths"):
            await _retract_mod.main(args)

    @pytest.mark.anyio
    async def test_with_refs(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: PathLike[str],
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Should handle additional --ref refs without error."""
        tmp = Path(tmp_path)
        await (tmp / "public" / ".git").mkdir(parents=True)
        monkeypatch.setattr(
            "scripts.retract._PUBLIC_GIT_DIRECTORY",
            PurePath(fspath(tmp / "public" / ".git")),
        )

        paths_file = tmp / "paths.txt"
        await paths_file.write_text("secret.txt\n")
        args = _retract_mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=_retract_mod.Path(fspath(paths_file)),
            refs=("other-branch",),
        )

        async def mock_which2(cmd: str) -> str:
            """Mock _which2 returning /usr/bin/git."""
            return "/usr/bin/git"

        monkeypatch.setattr("scripts.retract._which2", mock_which2)

        fake_tmp = tmp / "fakerepo2"
        await fake_tmp.mkdir(parents=True, exist_ok=True)
        await (fake_tmp / ".git" / "filter-repo" / "analysis").mkdir(
            parents=True, exist_ok=True
        )
        await (
            fake_tmp / ".git" / "filter-repo" / "analysis" / "renames.txt"
        ).write_text("")
        await (fake_tmp / ".git" / "filter-repo" / "commit-map").write_text("")
        await (fake_tmp / ".git" / "filter-branch").mkdir(parents=True, exist_ok=True)
        await (fake_tmp / ".git" / "filter-branch" / "commit-map").write_text("")

        class FakeTemporaryDirectory2:
            """Fake TemporaryDirectory that points to a fixed path."""

            def __init__(self, **kw: object) -> None:
                """Store the fake tmp directory path."""
                self.name = fspath(fake_tmp)

            def __enter__(self) -> str:
                """Return the fake directory path."""
                return self.name

            def __exit__(self, *args: object) -> None:
                """No-op cleanup."""
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
            """Mock _exec returning predetermined results by call index."""
            idx = exec_index[0]
            exec_index[0] += 1
            if idx >= len(exec_results):
                msg = f"Unexpected _exec call #{idx}: args={a}"
                raise RuntimeError(msg)
            return exec_results[idx]

        monkeypatch.setattr("scripts.retract._exec", mock_exec)
        monkeypatch.setattr("scripts.retract.info", print)

        await _retract_mod.main(args)
        captured = capsys.readouterr()
        assert "Commit maps" in captured.out


class TestPublishMain:
    """Tests for publish.main() async function."""

    @pytest.mark.anyio
    async def test_success(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: PathLike[str],
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Should run the full publish pipeline without errors."""
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
        await paths_file.write_text("file1\nfile2\n")
        args = _publish_mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=_publish_mod.Path(fspath(paths_file)),
        )

        async def mock_which2(cmd: str) -> str:
            """Mock _which2 returning /usr/bin/git."""
            return "/usr/bin/git"

        monkeypatch.setattr("scripts.publish._which2", mock_which2)

        exec_results: list[tuple[str, str]] = [
            ("", ""),  # 0: git clone
            ("", ""),  # 1: filter-repo --analyze
            ("", ""),  # 2: filter-repo --commit-callback
            ("main\n", ""),  # 3: branch --show-current
            ("", ""),  # 4: rebase
            ("", ""),  # 5: remote add
            ("", ""),  # 6: remote update
        ]
        exec_index = [0]

        async def mock_exec(*a: object, **kw: object) -> tuple[str, str]:
            """Mock _exec returning predetermined results by call index."""
            idx = exec_index[0]
            exec_index[0] += 1
            if idx >= len(exec_results):
                msg = f"Unexpected _exec call #{idx}: args={a}"
                raise RuntimeError(msg)
            return exec_results[idx]

        monkeypatch.setattr("scripts.publish._exec", mock_exec)

        fake_tmp = tmp / "fakerepo"
        await fake_tmp.mkdir(parents=True, exist_ok=True)
        await (fake_tmp / ".git" / "filter-repo" / "analysis").mkdir(
            parents=True, exist_ok=True
        )
        await (
            fake_tmp / ".git" / "filter-repo" / "analysis" / "renames.txt"
        ).write_text("")

        class FakeTemporaryDirectory:
            """Fake TemporaryDirectory that points to a fixed path."""

            def __init__(self, **kw: object) -> None:
                """Store the fake tmp directory path."""
                self.name = fspath(fake_tmp)

            def __enter__(self) -> str:
                """Return the fake directory path."""
                return self.name

            def __exit__(self, *args: object) -> None:
                """No-op cleanup."""
                pass

        monkeypatch.setattr(
            "scripts.publish.TemporaryDirectory", FakeTemporaryDirectory
        )

        monkeypatch.setattr("scripts.publish.info", print)

        await _publish_mod.main(args)

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

        paths_file = tmp / "paths.txt"
        await paths_file.write_text("file1 \n")
        args = _publish_mod.Arguments(
            allow_trailing_whitespaces_in_paths=False,
            paths_file=_publish_mod.Path(fspath(paths_file)),
        )

        async def mock_which2(cmd: str) -> str:
            """Mock _which2 returning /usr/bin/git."""
            return "/usr/bin/git"

        monkeypatch.setattr("scripts.publish._which2", mock_which2)

        with pytest.raises(ValueError, match="Found trailing whitespaces in paths"):
            await _publish_mod.main(args)

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
        args = _publish_mod.Arguments(
            allow_trailing_whitespaces_in_paths=True,
            paths_file=_publish_mod.Path(fspath(paths_file)),
        )

        async def mock_which2(cmd: str) -> str:
            """Mock _which2 returning /usr/bin/git."""
            return "/usr/bin/git"

        monkeypatch.setattr("scripts.publish._which2", mock_which2)

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
            """Mock _exec returning predetermined results by call index."""
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
        await (
            fake_tmp / ".git" / "filter-repo" / "analysis" / "renames.txt"
        ).write_text("")

        class FakeTemporaryDirectory2:
            """Fake TemporaryDirectory that points to a fixed path."""

            def __init__(self, **kw: object) -> None:
                """Store the fake tmp directory path."""
                self.name = fspath(fake_tmp)

            def __enter__(self) -> str:
                """Return the fake directory path."""
                return self.name

            def __exit__(self, *args: object) -> None:
                """No-op cleanup."""
                pass

        monkeypatch.setattr(
            "scripts.publish.TemporaryDirectory", FakeTemporaryDirectory2
        )

        monkeypatch.setattr("scripts.publish.info", print)

        await _publish_mod.main(args)
        captured = capsys.readouterr()
        assert "Merge commits" in captured.out
