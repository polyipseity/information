"""Tests for scripts/convert_wiki/config.py.

These tests cover the module-level constants and configuration helpers.
"""

import json
import os
from os import PathLike
from pathlib import Path as PathlibPath

from anyio import Path

from scripts.convert_wiki import config as _mod

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestConstants:
    """Tests for module-level constants."""

    def test_name_map_loaded(self, tmp_path: PathLike[str]) -> None:
        """_load_names_map should return a non-empty dict from JSONC only."""
        small_map = {"Test key": "test value"}
        map_path = PathlibPath(os.fspath(tmp_path)) / "small.name_map.jsonc"
        map_path.write_text(json.dumps(small_map), encoding="UTF-8")
        result = _mod._load_names_map(map_path)  # noqa: SLF001
        assert isinstance(result, dict)
        assert result == small_map

    def test_load_names_map_from_custom_path(self, tmp_path: PathLike[str]) -> None:
        """_load_names_map should load only from the given JSONC path."""
        custom_map = {"Foo": "foo", "Bar baz": "bar baz"}
        map_path = PathlibPath(os.fspath(tmp_path)) / "custom.name_map.jsonc"
        map_path.write_text(
            json.dumps(custom_map, ensure_ascii=False, indent=2) + "\n",
            encoding="UTF-8",
        )
        result = _mod._load_names_map(map_path)  # noqa: SLF001
        assert result == custom_map

    def test_names_map_exists(self) -> None:
        """_NAMES_MAP should be a dict loaded from the JSONC name map."""
        assert isinstance(_mod._NAMES_MAP, dict)  # noqa: SLF001


class TestWithCwd:
    """Tests for the _with_cwd context manager."""

    def test_changes_and_restores_cwd(self, tmp_path: PathLike[str]) -> None:
        """Should temporarily change the working directory and restore it."""
        # We pass mock chdir/getcwd since we can't actually chdir without
        # affecting other tests.

        last_paths: list[str] = []

        def tracking_chdir(path: str) -> None:
            """Track chdir paths in order."""
            last_paths.append(path)

        with _mod._with_cwd(  # noqa: SLF001
            Path("/tmp"), chdir=tracking_chdir
        ):
            pass
        # Two calls: set to /tmp, then restore to original cwd.
        assert len(last_paths) == 2
        assert os.fspath(last_paths[0]) == os.fspath(Path("/tmp"))

    def test_restores_cwd_on_exception(self) -> None:
        """Should restore the original cwd even when the body raises."""
        original_cwd = os.getcwd()
        # _with_cwd catches the exception and restores cwd
        cwds: list[str] = []

        def tracking_getcwd() -> str:
            """Return tracked cwd or original."""
            if cwds:
                return cwds[-1]
            return original_cwd

        def tracking_chdir(path: str) -> None:
            """Track chdir by appending to cwds list."""
            cwds.append(path)

        try:
            with _mod._with_cwd(  # noqa: SLF001
                Path("/tmp"), chdir=tracking_chdir, getcwd=tracking_getcwd
            ):
                raise ValueError("test exception")
        except ValueError:
            pass

        # cwd should be restored
        assert cwds[-1] == original_cwd
