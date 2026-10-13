"""Tests for scripts.convert_wiki.record_snapshot_aux.

The recorder talks to the live Wikipedia and Commons APIs, so these tests point
the module at a temporary fixture directory and stub ``aiohttp.ClientSession.get``.
The real ``_resolve_redirects``, ``_resolve_image_metadata``, URL building, and
the recording session wrapper all run against canned response bodies.
"""

import json
import os
from os import PathLike
from pathlib import Path as PathlibPath

import aiohttp
import pytest
from aiohttp.typedefs import StrOrURL
from anyio import Path
from yarl import URL

from scripts.convert_wiki import config as config_module
from scripts.convert_wiki import record_snapshot_aux as mod

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()

"""Uploaded filename the fixture image resolves to."""
_FILENAME = "Fourier spectrum.svg"

"""Minimal article body: one link and one archiveable image."""
_INPUT_HTML = f"""<meta charset="utf-8" />
<div id="mw-content-text">
  <p>See <a href="/wiki/Fourier_transform" title="Fourier transform">Fourier transform</a>.</p>
  <img src="//upload.wikimedia.org/wikipedia/commons/1/1a/{_FILENAME.replace(" ", "_")}" alt="" />
</div>
"""

"""Starting point for the aux file, with every recorded field empty."""
_SKELETON_AUX: dict[str, object] = {
    "api_titles": [],
    "api_responses": [],
    "redirect_cache": {},
    "image_metadata": {},
    "name_map_overrides": {"Fourier transform": "fourier transform"},
}

"""Production name map, which the fixture directory normally symlinks to."""
_NAME_MAP = (
    PathlibPath(__file__).resolve(strict=True).parents[3]
    / "scripts"
    / "assets"
    / "convert_wiki.name_map.jsonc"
)


class _FakeResponse:
    """Minimal stand-in for an aiohttp response body."""

    method = "GET"
    status = 200
    closed = False

    def __init__(self, body: dict[str, object]) -> None:
        """Store the canned JSON body."""
        self._body = body

    async def json(self) -> dict[str, object]:
        """Return the canned body."""
        return self._body

    def raise_for_status(self) -> None:
        """Report no HTTP error."""

    def close(self) -> None:
        """Report the response as closed."""
        self.closed = True


def _body_for(url: URL) -> dict[str, object]:
    """Return the MediaWiki body a request for *url* would receive."""
    titles = url.query.get("titles", "")
    if url.query.get("iiprop"):
        return {
            "batchcomplete": True,
            "query": {
                "pages": [
                    {
                        "ns": 6,
                        "title": title,
                        "imageinfo": [
                            {
                                "extmetadata": {
                                    "ImageDescription": {"value": "A plotted spectrum."}
                                }
                            }
                        ],
                    }
                    for title in titles.split("|")
                ]
            },
        }
    return {"batchcomplete": True, "query": {"redirects": []}}


@pytest.fixture
def _fixture_dir(monkeypatch: pytest.MonkeyPatch, tmp_path: PathLike[str]) -> Path:
    """Point the recorder at a temp directory holding one minimal fixture."""
    root = PathlibPath(os.fspath(tmp_path))
    (root / "article.input.html").write_text(_INPUT_HTML, encoding="UTF-8")
    (root / "article.aux.json").write_text(json.dumps(_SKELETON_AUX), encoding="UTF-8")
    (root / "name_map.jsonc").symlink_to(_NAME_MAP)
    monkeypatch.setattr(mod, "_SNAPSHOT_DIR", root)
    return Path(tmp_path)


class _SilentResponse:
    """Response context that yields an empty MediaWiki body."""

    async def __aenter__(self) -> _FakeResponse:
        """Enter the response context."""
        return _FakeResponse({})

    async def __aexit__(self, *exc: object) -> None:
        """Leave the response context."""


class _SilentSession:
    """Stand-in for the recording session that captures no queried titles."""

    def get(self, url: object) -> _SilentResponse:
        """Answer a request without recording anything."""
        del url
        return _SilentResponse()


@pytest.fixture
def _requests(monkeypatch: pytest.MonkeyPatch) -> list[URL]:
    """Serve canned Wikipedia and Commons bodies, recording every request URL."""

    async def fake_request(
        self: aiohttp.ClientSession, method: str, url: StrOrURL, **kwargs: object
    ) -> _FakeResponse:
        """Answer one API request from a canned body.

        ``RetryClient`` calls ``ClientSession.request``, so patching it covers
        both the recording session and the plain Commons session.
        """
        del self, method, kwargs
        requested = URL(url)
        requests.append(requested)
        return _FakeResponse(_body_for(requested))

    requests: list[URL] = []
    monkeypatch.setattr(aiohttp.ClientSession, "request", fake_request)
    return requests


@pytest.mark.anyio
async def test_record_collects_titles_and_image_metadata(
    _fixture_dir: Path, _requests: list[URL]
) -> None:
    """A recorded fixture carries the queried titles and the Commons descriptions."""
    recorded = await mod._record("article")

    assert set(recorded["redirect_cache"]) == {"Fourier transform"}
    assert recorded["api_titles"] == ["Fourier transform"]
    assert recorded["image_metadata"] == {f"File:{_FILENAME}": "A plotted spectrum."}


@pytest.mark.anyio
async def test_record_preserves_name_map_overrides(
    _fixture_dir: Path, _requests: list[URL]
) -> None:
    """Hand-written name map overrides survive a re-record."""
    recorded = await mod._record("article")

    assert recorded["name_map_overrides"] == {"Fourier transform": "fourier transform"}


@pytest.mark.anyio
async def test_record_keeps_commons_bodies_out_of_api_responses(
    _fixture_dir: Path, _requests: list[URL]
) -> None:
    """Only the redirect batches are recorded, so the batch count invariant holds."""
    recorded = await mod._record("article")
    commons_host = str(config_module._COMMONS_HOST_URL.host)  # noqa: SLF001

    wiki_calls = [url for url in _requests if url.host != commons_host]
    assert len(recorded["api_responses"]) == len(wiki_calls)
    assert recorded["api_responses"] == [
        {"batchcomplete": True, "query": {"redirects": []}}
    ]


@pytest.mark.anyio
async def test_expected_uses_recorded_image_metadata(_fixture_dir: Path) -> None:
    """Regenerating ``expected.md`` uses the recorded descriptions as alt text."""
    aux = {
        **_SKELETON_AUX,
        "redirect_cache": {
            "Fourier transform": {"to": "Fourier transform", "tofragment": ""}
        },
        "image_metadata": {f"File:{_FILENAME}": "A plotted spectrum."},
    }
    await (_fixture_dir / "article.aux.json").write_text(
        json.dumps(aux), encoding="UTF-8"
    )

    size = await mod._write_expected("article")

    output = await (_fixture_dir / "article.expected.md").read_text(encoding="UTF-8")
    assert size == len(output)
    assert "![A plotted spectrum.]" in output


@pytest.mark.anyio
async def test_recorded_titles_must_cover_the_input(
    _fixture_dir: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A query that misses a collected title is refused, not written."""
    monkeypatch.setattr(mod._RecordingSession, "get", _SilentSession().get)  # noqa: SLF001

    with pytest.raises(RuntimeError, match="refusing to write a partial fixture"):
        await mod._record("article")
