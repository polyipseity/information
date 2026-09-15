"""Shared fixtures for convert_wiki tests."""

import pytest


@pytest.fixture(autouse=True)
def _patch_reload_names_map(monkeypatch: pytest.MonkeyPatch) -> None:
    """Mock _reload_names_map to a no-op across all reprocess tests.

    Every apply_reprocess_plan call invokes _reload_names_map, which reads
    the 491KB real JSONC file from disk (~0.5s per call). Tests pass
    base_map explicitly, so the reload is wasted. This fixture eliminates
    ~4.5s of redundant I/O across the reprocess test suite.
    """
    monkeypatch.setattr(
        "scripts.convert_wiki.name_map_io._reload_names_map",
        lambda: None,
    )
