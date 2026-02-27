"""Unit tests for :mod:`academic-notes.find_wikipedia`.

This module lives in the skill directory and exercises the network
mocking logic used by the real CLI.  The tests here ensure we avoid
external HTTP calls by default and that the main entrypoint produces
expected output in its various modes.
"""

import json

import find_wikipedia
import pytest
from pydantic import BaseModel

__all__ = ()


@pytest.fixture(autouse=True)
def no_network(monkeypatch: pytest.MonkeyPatch) -> None:
    """Ensure that network requests are stubbed out in every test."""

    def fake_request(url: str) -> dict[str, object]:
        """Stub that raises if any code tries to perform an HTTP call."""
        raise RuntimeError("network should not be invoked")

    monkeypatch.setattr(find_wikipedia, "_make_request", fake_request)


def test_make_filenames_basic():
    """make_filenames should percent-encode titles appropriately."""
    # simple title -> percent-encoded name
    result = find_wikipedia.make_filenames("Hello World")
    assert result["filename"] == "Hello%20World.md"
    assert "%20" in result["friendly_filename"]
    # friendly name preserves hyphen
    result2 = find_wikipedia.make_filenames("foo-bar")
    assert result2["friendly_filename"].startswith("foo-bar")


def test_search_parsing(monkeypatch: pytest.MonkeyPatch):
    """The search() wrapper should parse JSON into SearchHit objects."""
    # provide a canned response to the underlying API helper
    fake = {"query": {"search": [{"title": "T1", "snippet": "<b>hi</b>"}]}}

    def fake_req(
        url: str, model: type[BaseModel] | None = None
    ) -> BaseModel | dict[str, object]:
        """Stubbed _make_request that optionally validates using pydantic."""
        # if a pydantic model is supplied, validate our fake data so the
        # calling code gets an instance rather than a raw dict
        if model is not None:
            return model.model_validate(fake)
        return fake

    monkeypatch.setattr(find_wikipedia, "_make_request", fake_req)
    hits = find_wikipedia.search("anything", limit=1)
    assert len(hits) == 1
    assert hits[0].title == "T1"
    assert hits[0].snippet == "<b>hi</b>"


def test_format_result_with_extract(monkeypatch: pytest.MonkeyPatch):
    """format_result should include truncated extract and full extract."""

    def stub_extract(t: str) -> str:
        """Return a fixed introductory paragraph for testing."""
        return "an introductory paragraph"

    monkeypatch.setattr(find_wikipedia, "_get_extract", stub_extract)
    res = find_wikipedia.format_result("Some Title")
    assert res.title == "Some Title"
    assert "Some_Title" in str(res.url)
    assert res.extract.startswith("an introductory")
    # extract_full should equal the full text
    assert res.extract_full == "an introductory paragraph"
    # the returned object is a pydantic model and can be serialized
    d = res.model_dump()
    assert d["title"] == "Some Title"


def test_cli_human_and_json(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    """CLI should produce human output and JSON variants correctly."""

    # stub both search and extract to avoid network
    def stub_search(term: str, limit: int) -> list[find_wikipedia.SearchHit]:
        """Return a single hit for any query."""
        return [find_wikipedia.SearchHit(title="Foo")]

    monkeypatch.setattr(
        find_wikipedia,
        "search",
        stub_search,
    )

    def stub_extract(t: str) -> str:
        """Short extract used by format_result."""
        return "brief"

    monkeypatch.setattr(find_wikipedia, "_get_extract", stub_extract)

    # human readable
    rc = find_wikipedia.main(["--human", "foo"])
    assert rc == 0
    captured = capsys.readouterr()
    assert "Foo" in captured.out

    # pretty json
    rc = find_wikipedia.main(["--pretty", "foo"])
    assert rc == 0
    captured = capsys.readouterr()
    # JSON object with query key
    parsed = json.loads(captured.out)
    assert parsed["query"] == "foo"

    # default json-lines
    rc = find_wikipedia.main(["foo"])
    assert rc == 0
    captured = capsys.readouterr()
    # one line per result; must be valid json
    lines = [line for line in captured.out.splitlines() if line.strip()]
    assert len(lines) == 1
    obj = json.loads(lines[0])
    assert obj["title"] == "Foo"


def test_no_results_print(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
):
    """CLI should handle zero-search-results gracefully."""

    def empty_search(term: str, limit: int) -> list[find_wikipedia.SearchHit]:
        """Stub returning an empty hit list."""
        return []

    monkeypatch.setattr(find_wikipedia, "search", empty_search)
    # human mode prints friendly message
    rc = find_wikipedia.main(["--human", "zzz"])
    assert rc == 0
    assert "No Wikipedia results" in capsys.readouterr().out

    # json mode prints empty results
    rc = find_wikipedia.main(["zzz"])
    assert rc == 0
    output = capsys.readouterr().out
    assert '"results": []' in output
