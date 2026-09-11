#!/usr/bin/env python
"""Regenerate convert_wiki snapshot auxiliary data from the live Wikimedia APIs.

Each ``<name>.aux.json`` fixture captures, at snapshot time, the external data
that ``run_pipeline`` would otherwise fetch over the network:

- ``redirect_cache``: resolved redirects for every link title in the input HTML.
- ``api_responses``: the raw batched API responses that produced ``redirect_cache``.
- ``image_metadata``: Commons ``ImageDescription`` values for media embeds.
- ``name_map_overrides``: per-snapshot filename overrides (never regenerated).

By default only ``redirect_cache`` and ``api_responses`` are regenerated, so
snapshots whose hand-curated ``image_metadata`` is intentional (synthetic
fixtures) keep their descriptions.  Pass ``--image-metadata`` to also refetch
descriptions from Commons.

Existing per-file formatting is preserved: top-level key order (with
``api_responses`` first), two-space indentation, ASCII escaping, and the
trailing newline.
"""

from __future__ import annotations

import json
import sys
from argparse import ArgumentParser
from collections.abc import Sequence
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from aiohttp import ClientSession, TCPConnector  # noqa: E402
from anyio import Path as AsyncPath  # noqa: E402
from asyncer import runnify  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
from yarl import URL  # noqa: E402

from scripts.convert_wiki import api as _api  # noqa: E402
from scripts.convert_wiki import config as _cfg  # noqa: E402
from scripts.convert_wiki.types import _ApiResponse, _RedirectInfo  # noqa: E402

_SNAPSHOT_DIRECTORY = _REPO_ROOT / "tests" / "scripts" / "convert_wiki" / "snapshots"
"""Directory holding ``<name>.aux.json`` fixtures."""

_KEY_ORDER_HEAD = "api_responses"
"""Top-level aux key that is always written first."""


def _uses_ascii_escapes(raw: str) -> bool:
    """Return whether *raw* JSON escapes non-ASCII characters."""
    return not any(ord(character) > 127 for character in raw)


def _key_order(existing: Sequence[str]) -> list[str]:
    """Return the aux key order, always leading with ``api_responses``."""
    return [_KEY_ORDER_HEAD, *(key for key in existing if key != _KEY_ORDER_HEAD)]


async def _regenerate_snapshot(
    session: ClientSession,
    aux_path: Path,
    *,
    refetch_image_metadata: bool,
    recorded: list[_ApiResponse],
) -> str:
    """Regenerate one aux fixture and return a human-readable summary."""
    raw = await AsyncPath(aux_path).read_text(encoding="UTF-8")
    existing: dict[str, Any] = json.loads(raw)

    input_path = aux_path.with_name(f"{aux_path.name[: -len('.aux.json')]}.input.html")
    soup = BeautifulSoup(
        await AsyncPath(input_path).read_text(encoding="UTF-8"), "html.parser"
    )

    titles = _api._collect_link_titles(soup)
    del recorded[:]
    cache: dict[str, _RedirectInfo] = {}
    tmp_path = aux_path.with_name(f"{aux_path.name}.redirect_cache.tmp")
    await _api._resolve_redirects(session, titles, cache, cache_path=tmp_path)
    if await AsyncPath(tmp_path).exists():
        await AsyncPath(tmp_path).unlink()
    raw_responses = list(recorded)

    image_metadata = existing.get("image_metadata", {})
    if refetch_image_metadata:
        image_metadata = await _api._resolve_image_metadata(
            session, _api._collect_image_filenames(soup)
        )

    data: dict[str, Any] = {
        "redirect_cache": {
            title: {
                "to": info.to,
                "tofragment": info.tofragment,
                "cached_at": info.cached_at,
            }
            for title, info in cache.items()
        },
        "api_responses": raw_responses,
        "image_metadata": image_metadata,
        "name_map_overrides": existing.get("name_map_overrides", {}),
    }
    ordered = {key: data[key] for key in _key_order(list(existing))}
    await AsyncPath(aux_path).write_text(
        json.dumps(ordered, ensure_ascii=_uses_ascii_escapes(raw), indent=2) + "\n",
        encoding="UTF-8",
    )

    redirects = sum(
        1 for title, info in cache.items() if info.to != title or info.tofragment
    )
    return (
        f"titles={len(titles)} redirects={redirects} "
        f"batches={len(raw_responses)} images={len(image_metadata)}"
    )


async def main(argv: Sequence[str] | None = None) -> None:
    """Regenerate snapshot auxiliary data from the live APIs."""
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "snapshots",
        nargs="*",
        help="Snapshot names to regenerate (default: all).",
    )
    parser.add_argument(
        "--image-metadata",
        action="store_true",
        help="Also refetch image descriptions from Wikimedia Commons.",
    )
    args = parser.parse_args(argv)

    recorded: list[_ApiResponse] = []
    original_request = _api._api_request

    async def recording_request(
        session: ClientSession,
        params: dict[str, str | int],
        host: URL = _cfg._WIKI_HOST_URL,
    ) -> _ApiResponse:
        """Record raw API responses, then delegate to the real request."""
        result = await original_request(session, params, host)
        recorded.append(result)
        return result

    names = args.snapshots or sorted(
        path.name[: -len(".aux.json")]
        for path in _SNAPSHOT_DIRECTORY.glob("*.aux.json")
    )

    async with ClientSession(
        connector=TCPConnector(limit_per_host=_cfg._MAX_CONCURRENT_REQUESTS_PER_HOST),
        headers={"Accept-Encoding": "gzip", "User-Agent": _cfg.USER_AGENT},
    ) as session:
        for name in names:
            aux_path = _SNAPSHOT_DIRECTORY / f"{name}.aux.json"
            if not await AsyncPath(aux_path).exists():
                raise SystemExit(f"unknown snapshot: {name}")
            # ``_resolve_redirects`` resolves ``_api_request`` from this
            # module's globals at call time, so patching the attribute keeps
            # the production parser as the single source of truth for how
            # recorded batches are interpreted.
            setattr(_api, "_api_request", recording_request)
            try:
                summary = await _regenerate_snapshot(
                    session,
                    aux_path,
                    refetch_image_metadata=args.image_metadata,
                    recorded=recorded,
                )
            finally:
                setattr(_api, "_api_request", original_request)
            print(f"{name}: {summary}")


def __main__() -> None:
    """Run the auxiliary-data regeneration CLI."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
