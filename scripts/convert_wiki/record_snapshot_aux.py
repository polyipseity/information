"""Record or regenerate ``convert_wiki`` snapshot fixtures.

Two subcommands:

``record <name>``
    Query the live Wikipedia API for every link title of
    ``snapshots/<name>.input.html`` with a *cold* redirect cache, then write
    ``api_titles``, ``api_responses``, and ``redirect_cache`` into the snapshot
    aux fixture.  ``image_metadata`` and ``name_map_overrides`` are preserved.

``expected <name>``
    Regenerate ``snapshots/<name>.expected.md`` from the aux fixture without
    network access.

Run ``record``, then Prettier (which may reorder JSON keys), then ``expected``:
the expected output must be generated from the final on-disk aux data.

Usage::

    uv run -m scripts.convert_wiki.record_snapshot_aux record "<name>"
    uv run -m scripts.convert_wiki.record_snapshot_aux expected "<name>"
"""

from __future__ import annotations

import argparse
import json
import tempfile
from collections.abc import MutableMapping, Sequence
from contextlib import AbstractAsyncContextManager
from pathlib import Path
from types import TracebackType
from typing import TYPE_CHECKING, NotRequired, Self, TypedDict, cast

import json5
from aiohttp import ClientResponse, ClientSession, TCPConnector
from aiohttp_retry import RetryClient
from asyncer import runnify
from bs4 import BeautifulSoup

from scripts.convert_wiki import api as _api
from scripts.convert_wiki import config as _cfg
from scripts.convert_wiki.pipeline import run_pipeline
from scripts.convert_wiki.types import _RedirectInfo

if TYPE_CHECKING:
    from aiohttp_retry.types import ClientType
    from yarl import URL

"""Absolute path to the snapshot fixtures directory."""
_SNAPSHOT_DIR = (
    Path(__file__).resolve(strict=True).parents[2]
    / "tests"
    / "scripts"
    / "convert_wiki"
    / "snapshots"
)


class _RedirectEntry(TypedDict):
    """Serialized ``_RedirectInfo`` stored in a fixture's ``redirect_cache``."""

    to: str
    tofragment: str


class _AuxFixture(TypedDict):
    """Shape of a snapshot ``.aux.json`` fixture."""

    api_titles: NotRequired[list[str]]
    api_responses: list[dict[str, object]]
    redirect_cache: dict[str, _RedirectEntry]
    image_metadata: dict[str, str]
    name_map_overrides: dict[str, str]


class _RecordingResponse:
    """Capture the JSON body of a wrapped ``ClientResponse`` context manager."""

    def __init__(
        self,
        context: AbstractAsyncContextManager[ClientResponse],
        sink: list[dict[str, object]],
    ) -> None:
        """Store the wrapped context manager and the capture list."""
        self._context = context
        self._sink = sink
        self._response: ClientResponse | None = None

    @property
    def status(self) -> int:
        """Return the HTTP status of the entered response."""
        if self._response is None:
            msg = "HTTP status read before entering the response context"
            raise RuntimeError(msg)
        return self._response.status

    async def __aenter__(self) -> Self:
        """Enter the wrapped context manager."""
        self._response = await self._context.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool | None:
        """Leave the wrapped context manager."""
        return await self._context.__aexit__(exc_type, exc, tb)

    async def json(self) -> object:
        """Return the decoded body, capturing it on the way through."""
        if self._response is None:
            msg = "JSON body read before entering the response context"
            raise RuntimeError(msg)
        data = await self._response.json()
        # aiohttp's ``json()`` is untyped (returns ``Any``); the body is the
        # MediaWiki API response whose shape ``_resolve_redirects`` parses.
        self._sink.append(cast("dict[str, object]", data))
        return data


class _RecordingSession:
    """Wrap a client session, capturing redirect queries and their bodies."""

    def __init__(self, session: ClientType) -> None:
        """Store the wrapped session."""
        self._session = session
        self.title_chunks: list[str] = []
        self.responses: list[dict[str, object]] = []

    def get(self, url: URL) -> _RecordingResponse:
        """Capture the requested titles and wrap the response context."""
        self.title_chunks.extend(str(value) for value in url.query.getall("titles"))
        return _RecordingResponse(self._session.get(url), self.responses)


def _aux_path(name: str) -> Path:
    """Return the aux fixture path for snapshot *name*."""
    return _SNAPSHOT_DIR / f"{name}.aux.json"


def _load_aux(name: str) -> _AuxFixture:
    """Load the aux fixture for snapshot *name*."""
    loaded = json.loads(_aux_path(name).read_text(encoding="UTF-8"))
    # The aux fixture is a checked-in artifact of this recorder and is
    # validated by the snapshot and replay tests; narrowing every nested field
    # would duplicate that validation.
    return cast("_AuxFixture", loaded)


async def _record(name: str) -> _AuxFixture:
    """Query the live API and return the refreshed aux data for *name*."""
    aux = _load_aux(name)
    html = BeautifulSoup(
        (_SNAPSHOT_DIR / f"{name}.input.html").read_text(encoding="UTF-8"),
        "html.parser",
    )
    titles = _api._collect_link_titles(html)
    cache: MutableMapping[str, _RedirectInfo] = {}

    async with ClientSession(
        connector=TCPConnector(limit_per_host=_cfg._MAX_CONCURRENT_REQUESTS_PER_HOST),
        headers={
            "Accept-Encoding": "gzip",
            "User-Agent": _cfg.USER_AGENT,
        },
        trust_env=True,
    ) as raw_session:
        session = RetryClient(
            client_session=raw_session,
            retry_options=_cfg._WikimediaRetry(
                attempts=3,
                start_timeout=1.0,
                max_timeout=30.0,
                statuses={429},
            ),
            raise_for_status=False,
        )
        recorder = _RecordingSession(session)
        try:
            with tempfile.TemporaryDirectory() as tmp:
                await _api._resolve_redirects(
                    cast("ClientType", recorder),
                    titles,
                    cache,
                    cache_path=Path(tmp) / "redirect_cache.json",
                )
        finally:
            await session.close()

    api_titles = [
        title for chunk in recorder.title_chunks for title in chunk.split("|") if title
    ]
    if set(api_titles) != set(titles):
        msg = (
            f"{name}: recorded {len(set(api_titles))} queried titles but collected "
            f"{len(titles)}; refusing to write a partial fixture"
        )
        raise RuntimeError(msg)

    return {
        "api_titles": api_titles,
        "api_responses": recorder.responses,
        "redirect_cache": {
            title: {"to": info.to, "tofragment": info.tofragment}
            for title, info in cache.items()
        },
        "image_metadata": aux["image_metadata"],
        "name_map_overrides": aux["name_map_overrides"],
    }


async def _write_expected(name: str) -> int:
    """Regenerate ``<name>.expected.md`` from the aux fixture; return its size."""
    aux = _load_aux(name)
    html = BeautifulSoup(
        (_SNAPSHOT_DIR / f"{name}.input.html").read_text(encoding="UTF-8"),
        "html.parser",
    )
    redirect_map = {
        title: _RedirectInfo(to=entry["to"], tofragment=entry.get("tofragment", ""))
        for title, entry in aux["redirect_cache"].items()
    }
    with (_SNAPSHOT_DIR / "name_map.jsonc").open(encoding="UTF-8") as names_map_file:
        shared_names_map: dict[str, str] = json5.load(names_map_file)
    names_map = shared_names_map | aux["name_map_overrides"]

    with tempfile.TemporaryDirectory() as tmp:
        wiki_dir = Path(tmp) / "general"
        lang_dir = wiki_dir / "eng"
        lang_dir.mkdir(parents=True)
        output, _ = await run_pipeline(
            html,
            redirect_map=redirect_map,
            image_metadata=aux["image_metadata"],
            names_map=names_map,
            wiki_dir=wiki_dir,
            wiki_lang_dir=lang_dir,
            refs=True,
            page_name=name[0].upper() + name[1:] if name else name,
        )

    (_SNAPSHOT_DIR / f"{name}.expected.md").write_text(output, encoding="UTF-8")
    return len(output)


def main(argv: Sequence[str] | None = None) -> None:
    """Run the requested subcommand."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("record", "expected"))
    parser.add_argument("name", help="Snapshot name, e.g. 'Fourier transform'")
    args = parser.parse_args(argv)

    if args.command == "record":
        data = runnify(_record)(args.name)
        _aux_path(args.name).write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="UTF-8"
        )
        print(
            f"{args.name}: {len(data['api_titles'])} titles, "
            f"{len(data['api_responses'])} batches, "
            f"{len(data['redirect_cache'])} cache entries"
        )
        return

    size = runnify(_write_expected)(args.name)
    print(f"{args.name}: expected.md written ({size} chars)")


def __main__() -> None:
    """Run the CLI entry point."""
    main()


if __name__ == "__main__":
    __main__()
