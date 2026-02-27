import json

import find_wikipedia
import pytest
from pydantic import BaseModel

__all__ = ()


@pytest.fixture(autouse=True)
def no_network(monkeypatch: pytest.MonkeyPatch) -> None:
    """Prevent real network calls by default during tests."""  #

    def fake_request(url: str) -> dict[str, object]:
        raise RuntimeError("network should not be invoked")

    monkeypatch.setattr(find_wikipedia, "_make_request", fake_request)


def test_make_filenames_basic():
    # simple title -> percent-encoded name
    result = find_wikipedia.make_filenames("Hello World")
    assert result["filename"] == "Hello%20World.md"
    assert "%20" in result["friendly_filename"]
    # friendly name preserves hyphen
    result2 = find_wikipedia.make_filenames("foo-bar")
    assert result2["friendly_filename"].startswith("foo-bar")


def test_search_parsing(monkeypatch: pytest.MonkeyPatch):
    # provide a canned response to the underlying API helper
    fake = {"query": {"search": [{"title": "T1", "snippet": "<b>hi</b>"}]}}

    def fake_req(
        url: str, model: type[BaseModel] | None = None
    ) -> BaseModel | dict[str, object]:
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
    def stub_extract(t: str) -> str:
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
    # stub both search and extract to avoid network
    def stub_search(term: str, limit: int) -> list[find_wikipedia.SearchHit]:
        return [find_wikipedia.SearchHit(title="Foo")]

    monkeypatch.setattr(
        find_wikipedia,
        "search",
        stub_search,
    )

    def stub_extract(t: str) -> str:
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
    def empty_search(term: str, limit: int) -> list[find_wikipedia.SearchHit]:
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
