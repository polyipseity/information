"""Tests for scripts/special/get_hkust_undergraduate_courses.py.

Covers: Subject dataclass, module constants, fetch_subjects (HTML parsing),
fetch_subject_courses (HTML parsing from mock response), open_dest (file vs
stdout), main() (mocked HTTP and I/O).
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import FrozenInstanceError
from io import StringIO
from os import fspath
from pathlib import Path
from sys import stdout

import pytest
from aiohttp import ClientSession

from scripts.special import get_hkust_undergraduate_courses as _mod

# ---------------------------------------------------------------------------
# TestSubject
# ---------------------------------------------------------------------------


class TestSubject:
    """Tests for the Subject frozen dataclass."""

    def test_attributes(self) -> None:
        """Should store code, name, and credit."""
        s = _mod.Subject(code="COMP", name="Computer Science", credit="3")
        assert s.code == "COMP"
        assert s.name == "Computer Science"
        assert s.credit == "3"

    def test_frozen(self) -> None:
        """Should raise FrozenInstanceError when modifying attributes."""
        s = _mod.Subject(code="MATH", name="Mathematics", credit="4")
        with pytest.raises(FrozenInstanceError):
            s.code = "PHYS"  # type: ignore[misc]

    def test_hashable(self) -> None:
        """Should be usable as a dict key."""
        s = _mod.Subject(code="COMP", name="CS", credit="3")
        d = {s: "value"}
        assert d[s] == "value"

    def test_equality(self) -> None:
        """Two Subjects with same fields should be equal."""
        s1 = _mod.Subject(code="COMP", name="CS", credit="3")
        s2 = _mod.Subject(code="COMP", name="CS", credit="3")
        assert s1 == s2

    def test_inequality(self) -> None:
        """Two Subjects with different fields should not be equal."""
        s1 = _mod.Subject(code="COMP", name="CS", credit="3")
        s2 = _mod.Subject(code="MATH", name="Math", credit="4")
        assert s1 != s2

    def test_repr(self) -> None:
        """repr should include all fields."""
        s = _mod.Subject(code="COMP", name="CS", credit="3")
        r = repr(s)
        assert "Subject(" in r
        assert "code=" in r

    def test_kw_only(self) -> None:
        """Should require keyword arguments."""
        with pytest.raises(TypeError):
            _mod.Subject("COMP", "CS", "3")  # type: ignore[call-arg]


# ---------------------------------------------------------------------------
# TestConstants
# ---------------------------------------------------------------------------


class TestConstants:
    """Tests for module-level constants."""

    def test_csv_dialect(self) -> None:
        """_CSV_DIALECT should be 'excel'."""
        assert _mod._CSV_DIALECT == "excel"

    def test_csv_line_terminator(self) -> None:
        """_CSV_LINE_TERMINATOR should be '\\n'."""
        assert _mod._CSV_LINE_TERMINATOR == "\n"

    def test_max_concurrent_requests(self) -> None:
        """_MAX_CONCURRENT_REQUESTS_PER_HOST should be 2."""
        assert _mod._MAX_CONCURRENT_REQUESTS_PER_HOST == 2

    def test_undergraduate_courses_url(self) -> None:
        """_UNDERGRADUATE_COURSES_URL should be the correct URL."""
        assert str(_mod._UNDERGRADUATE_COURSES_URL) == (
            "https://prog-crs.hkust.edu.hk/ugcourse"
        )


# ---------------------------------------------------------------------------
# Helpers: fake aiohttp session / response
# ---------------------------------------------------------------------------


class _FakeResponse:
    """Simulates an aiohttp.ClientResponse with a .text() coroutine."""

    def __init__(self, text: str) -> None:
        self._text = text

    async def text(self) -> str:
        """Return the preset HTML text."""
        return self._text

    async def __aenter__(self) -> _FakeResponse:
        """Support async with."""
        return self

    async def __aexit__(self, *args: object) -> None:
        """Support async with."""


class _FakeClientSession:
    """Fake aiohttp.ClientSession with a configurable .get method.

    The get function must be synchronous (not async) and return a response
    object directly, because the source does ``async with session.get(u) as r``
    which calls __aenter__ on the return value of session.get(), not on an
    awaited coroutine.

    This class supports ``async with`` so it can be used as
    ``ClientSession(...) as session`` in the source code.
    """

    def __init__(self, get_fn: Callable[..., object]) -> None:
        self.get = get_fn

    async def __aenter__(self) -> _FakeClientSession:
        return self

    async def __aexit__(self, *args: object) -> None:
        return None


def _fake_session(get_fn: Callable[..., object]) -> ClientSession:
    """Build a fake aiohttp.ClientSession with a configurable .get method."""
    return _FakeClientSession(get_fn)  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# TestFetchSubjects
# ---------------------------------------------------------------------------


class TestFetchSubjects:
    """Tests for the fetch_subjects function."""

    _SUBJECTS_HTML = """\
<div class="subject">
  <span class="subject-code">ACCT</span>
  <a href="/ugcourse/ACCT">Accounting</a>
</div>
<div class="subject">
  <span class="subject-code">COMP</span>
  <a href="/ugcourse/COMP">Computer Science</a>
</div>
"""

    @pytest.mark.anyio
    async def test_returns_sorted_subjects(self) -> None:
        """Should parse subject blocks and return sorted mapping."""
        session = _fake_session(lambda url, **kw: _FakeResponse(self._SUBJECTS_HTML))
        result = await _mod.fetch_subjects(session=session)
        assert list(result.keys()) == ["ACCT", "COMP"]

    @pytest.mark.anyio
    async def test_href_joined_with_base(self) -> None:
        """Should join relative href with the base URL."""
        session = _fake_session(lambda url, **kw: _FakeResponse(self._SUBJECTS_HTML))
        result = await _mod.fetch_subjects(session=session)
        assert str(result["ACCT"]) == (
            "https://prog-crs.hkust.edu.hk/ugcourse/ACCT"
        )
        assert str(result["COMP"]) == (
            "https://prog-crs.hkust.edu.hk/ugcourse/COMP"
        )

    @pytest.mark.anyio
    async def test_missing_subject_code_raises(self) -> None:
        """Should raise ValueError when .subject-code element is missing."""
        html = '<div class="subject"><a href="/x">X</a></div>'
        session = _fake_session(lambda url, **kw: _FakeResponse(html))
        with pytest.raises(ValueError):
            await _mod.fetch_subjects(session=session)

    @pytest.mark.anyio
    async def test_empty_href(self) -> None:
        """Should handle empty href gracefully (join with base URL)."""
        html = '<div class="subject"><span class="subject-code">X</span><a href="">X</a></div>'
        session = _fake_session(lambda url, **kw: _FakeResponse(html))
        result = await _mod.fetch_subjects(session=session)
        # Empty href joins with the base URL, yielding the base URL itself
        assert str(result["X"]) == "https://prog-crs.hkust.edu.hk/ugcourse"

    @pytest.mark.anyio
    async def test_empty_subject_list(self) -> None:
        """Should return empty dict when there are no .subject elements."""
        session = _fake_session(lambda url, **kw: _FakeResponse("<html></html>"))
        result = await _mod.fetch_subjects(session=session)
        assert result == {}

    @pytest.mark.anyio
    async def test_anchor_without_href_raises(self) -> None:
        """Should raise ValueError when anchor tag has no href attribute."""
        html = '<div class="subject"><span class="subject-code">X</span><a>no href</a></div>'
        session = _fake_session(lambda url, **kw: _FakeResponse(html))
        with pytest.raises(ValueError):
            await _mod.fetch_subjects(session=session)


# ---------------------------------------------------------------------------
# TestFetchSubjectCourses
# ---------------------------------------------------------------------------


class TestFetchSubjectCourses:
    """Tests for the fetch_subject_courses function."""

    _COURSES_HTML = """\
<div class="crse-header">
  <span class="crse-code">COMP2011</span>
  <span class="crse-title">Data Structures</span>
  <span class="crse-unit">4 Credit(s)</span>
</div>
<div class="crse-header">
  <span class="crse-code">COMP2012</span>
  <span class="crse-title">OO Programming</span>
  <span class="crse-unit">3 Credit(s)</span>
</div>
"""

    @pytest.mark.anyio
    async def test_yields_subjects(self) -> None:
        """Should yield Subject objects from .crse-header blocks."""
        session = _fake_session(
            lambda url, **kw: _FakeResponse(self._COURSES_HTML)
        )
        subjects = [
            s
            async for s in _mod.fetch_subject_courses(
                _mod._UNDERGRADUATE_COURSES_URL, session=session
            )
        ]
        assert len(subjects) == 2
        assert subjects[0] == _mod.Subject(
            code="COMP2011", name="Data Structures", credit="4"
        )
        assert subjects[1] == _mod.Subject(
            code="COMP2012", name="OO Programming", credit="3"
        )

    @pytest.mark.anyio
    async def test_empty_course_list(self) -> None:
        """Should yield nothing when there are no .crse-header elements."""
        session = _fake_session(
            lambda url, **kw: _FakeResponse("<html></html>")
        )
        subjects = [
            s
            async for s in _mod.fetch_subject_courses(
                _mod._UNDERGRADUATE_COURSES_URL, session=session
            )
        ]
        assert subjects == []

    @pytest.mark.anyio
    async def test_missing_code_raises(self) -> None:
        """Should raise ValueError when .crse-code is missing."""
        html = '<div class="crse-header"><span class="crse-title">T</span><span class="crse-unit">3 Credit(s)</span></div>'
        session = _fake_session(lambda url, **kw: _FakeResponse(html))
        with pytest.raises(ValueError):
            async for _ in _mod.fetch_subject_courses(
                _mod._UNDERGRADUATE_COURSES_URL, session=session
            ):
                pass

    @pytest.mark.anyio
    async def test_missing_title_raises(self) -> None:
        """Should raise ValueError when .crse-title is missing."""
        html = '<div class="crse-header"><span class="crse-code">C1</span><span class="crse-unit">3 Credit(s)</span></div>'
        session = _fake_session(lambda url, **kw: _FakeResponse(html))
        with pytest.raises(ValueError):
            async for _ in _mod.fetch_subject_courses(
                _mod._UNDERGRADUATE_COURSES_URL, session=session
            ):
                pass

    @pytest.mark.anyio
    async def test_missing_unit_raises(self) -> None:
        """Should raise ValueError when .crse-unit is missing."""
        html = '<div class="crse-header"><span class="crse-code">C1</span><span class="crse-title">T</span></div>'
        session = _fake_session(lambda url, **kw: _FakeResponse(html))
        with pytest.raises(ValueError):
            async for _ in _mod.fetch_subject_courses(
                _mod._UNDERGRADUATE_COURSES_URL, session=session
            ):
                pass

    @pytest.mark.anyio
    async def test_credit_parsing(self) -> None:
        """Should parse credit as text before the first space."""
        html = '<div class="crse-header"><span class="crse-code">C1</span><span class="crse-title">T</span><span class="crse-unit">4.0 Credit(s)</span></div>'
        session = _fake_session(lambda url, **kw: _FakeResponse(html))
        subjects = [
            s
            async for s in _mod.fetch_subject_courses(
                _mod._UNDERGRADUATE_COURSES_URL, session=session
            )
        ]
        assert subjects[0].credit == "4.0"

    @pytest.mark.anyio
    async def test_empty_code_raises(self) -> None:
        """Should raise ValueError when .crse-code string is empty."""
        html = '<div class="crse-header"><span class="crse-code"></span><span class="crse-title">T</span><span class="crse-unit">3 Credit(s)</span></div>'
        session = _fake_session(lambda url, **kw: _FakeResponse(html))
        with pytest.raises(ValueError):
            async for _ in _mod.fetch_subject_courses(
                _mod._UNDERGRADUATE_COURSES_URL, session=session
            ):
                pass


# ---------------------------------------------------------------------------
# TestOpenDest
# ---------------------------------------------------------------------------


class TestOpenDest:
    """Tests for the open_dest async context manager."""

    @pytest.mark.anyio
    async def test_to_file_creates_if_not_exists(self, tmp_path: Path) -> None:
        """Should create the file if it doesn't exist."""
        dest = tmp_path / "output.csv"
        assert not dest.exists()
        async with _mod.open_dest(fspath(dest)) as fh:
            assert dest.exists()
            assert isinstance(fh, _mod.AsyncFile)

    @pytest.mark.anyio
    async def test_to_file_writable(self, tmp_path: Path) -> None:
        """Should allow writing to the file."""
        dest = tmp_path / "output.csv"
        async with _mod.open_dest(fspath(dest)) as fh:
            await fh.write("hello")
        assert dest.read_text(encoding="UTF-8") == "hello"

    @pytest.mark.anyio
    async def test_to_file_opens_existing(self, tmp_path: Path) -> None:
        """Should open an existing file for r/w."""
        dest = tmp_path / "existing.csv"
        dest.write_text("old content", encoding="UTF-8")
        async with _mod.open_dest(fspath(dest)) as fh:
            content = await fh.read()
            assert "old content" in content
            await fh.write(" + new")
        assert "old content" in dest.read_text(encoding="UTF-8")

    @pytest.mark.anyio
    async def test_to_stdout(self) -> None:
        """Should yield AsyncFile wrapping stdout when path is empty."""
        async with _mod.open_dest("") as fh:
            assert fh.wrapped is stdout

    @pytest.mark.anyio
    async def test_none_path_yields_stdout(self) -> None:
        """Should yield stdout when path is empty (falsy)."""
        async with _mod.open_dest("") as fh:
            assert fh.wrapped is stdout

    @pytest.mark.anyio
    async def test_to_file_with_anyio_path(self, tmp_path: Path) -> None:
        """Should accept an anyio.Path object."""
        dest = _mod.Path(fspath(tmp_path / "anyio_output.csv"))
        async with _mod.open_dest(dest) as fh:
            await fh.write("anyio path")
        assert (tmp_path / "anyio_output.csv").read_text(encoding="UTF-8") == (
            "anyio path"
        )


# ---------------------------------------------------------------------------
# TestMain
# ---------------------------------------------------------------------------


def _fake_session_factory(
    subjects_html: str,
    courses_by_subject: Mapping[str, str],
) -> Callable[..., object]:
    """Return a fake session.get that returns appropriate HTML per URL.

    The returned function is synchronous — it returns a _FakeResponse
    directly (not a coroutine), matching how aiohttp.ClientSession.get
    works in ``async with session.get(url) as resp:``.
    """

    def fake_get(url: object, **kwargs: object) -> _FakeResponse:
        url_str = str(url)
        if url_str == str(_mod._UNDERGRADUATE_COURSES_URL):
            return _FakeResponse(subjects_html)
        for prefix, courses_html in courses_by_subject.items():
            if prefix in url_str:
                return _FakeResponse(courses_html)
        return _FakeResponse("")

    return fake_get


class TestMain:
    """Tests for the main() orchestrator."""

    @pytest.mark.anyio
    async def test_empty_destination_stdout(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Should process courses and write CSV to stdout."""
        subjects_html = """\
<div class="subject">
  <span class="subject-code">COMP</span>
  <a href="/ugcourse/COMP">Computer Science</a>
</div>"""
        courses_html = """\
<div class="crse-header">
  <span class="crse-code">COMP2011</span>
  <span class="crse-title">Data Structures</span>
  <span class="crse-unit">4 Credit(s)</span>
</div>"""

        monkeypatch.setattr("builtins.input", lambda prompt="": "")
        fake_get = _fake_session_factory(subjects_html, {"COMP": courses_html})
        monkeypatch.setattr(
            _mod.__name__ + ".ClientSession",
            lambda **kwargs: _fake_session(fake_get),
        )

        out = StringIO()
        monkeypatch.setattr(_mod.__name__ + ".stdout", out)

        await _mod.main()

        output = out.getvalue()
        assert "COMP2011" in output
        assert "Data Structures" in output
        assert "4" in output

    @pytest.mark.anyio
    async def test_existing_courses_merged(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        """Should merge existing courses from file with freshly fetched ones."""
        dest = tmp_path / "courses.csv"
        dest.write_text(
            "code,name,credit\nEXIST1,Existing Course,3\n", encoding="UTF-8"
        )

        subjects_html = """\
<div class="subject">
  <span class="subject-code">COMP</span>
  <a href="/ugcourse/COMP">CS</a>
</div>"""
        courses_html = """\
<div class="crse-header">
  <span class="crse-code">COMP2011</span>
  <span class="crse-title">Data Structures</span>
  <span class="crse-unit">4 Credit(s)</span>
</div>"""

        monkeypatch.setattr("builtins.input", lambda prompt="": fspath(dest))
        fake_get = _fake_session_factory(subjects_html, {"COMP": courses_html})
        monkeypatch.setattr(
            _mod.__name__ + ".ClientSession",
            lambda **kwargs: _fake_session(fake_get),
        )

        await _mod.main()

        content = dest.read_text(encoding="UTF-8")
        assert "EXIST1" in content
        assert "COMP2011" in content
        assert "Existing Course" in content
        assert "Data Structures" in content

    @pytest.mark.anyio
    async def test_multiple_subjects(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        """Should handle multiple subject areas."""
        dest = tmp_path / "multi.csv"

        subjects_html = """\
<div class="subject">
  <span class="subject-code">COMP</span>
  <a href="/ugcourse/COMP">CS</a>
</div>
<div class="subject">
  <span class="subject-code">MATH</span>
  <a href="/ugcourse/MATH">Math</a>
</div>"""
        comp_html = """\
<div class="crse-header">
  <span class="crse-code">COMP2011</span>
  <span class="crse-title">Data Structures</span>
  <span class="crse-unit">4 Credit(s)</span>
</div>"""
        math_html = """\
<div class="crse-header">
  <span class="crse-code">MATH1011</span>
  <span class="crse-title">Calculus</span>
  <span class="crse-unit">3 Credit(s)</span>
</div>"""

        monkeypatch.setattr("builtins.input", lambda prompt="": fspath(dest))
        fake_get = _fake_session_factory(
            subjects_html, {"COMP": comp_html, "MATH": math_html}
        )
        monkeypatch.setattr(
            _mod.__name__ + ".ClientSession",
            lambda **kwargs: _fake_session(fake_get),
        )

        await _mod.main()

        content = dest.read_text(encoding="UTF-8")
        assert "COMP2011" in content
        assert "MATH1011" in content
        # Should be sorted alphabetically by course code
        comp_pos = content.index("COMP2011")
        math_pos = content.index("MATH1011")
        assert comp_pos < math_pos

    @pytest.mark.anyio
    async def test_existing_course_overwritten(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        """Same course code should be overwritten by new data."""
        dest = tmp_path / "overwrite.csv"
        dest.write_text(
            "code,name,credit\nCOMP2011,Old Name,2\n", encoding="UTF-8"
        )

        subjects_html = """\
<div class="subject">
  <span class="subject-code">COMP</span>
  <a href="/ugcourse/COMP">CS</a>
</div>"""
        courses_html = """\
<div class="crse-header">
  <span class="crse-code">COMP2011</span>
  <span class="crse-title">Data Structures</span>
  <span class="crse-unit">4 Credit(s)</span>
</div>"""

        monkeypatch.setattr("builtins.input", lambda prompt="": fspath(dest))
        fake_get = _fake_session_factory(subjects_html, {"COMP": courses_html})
        monkeypatch.setattr(
            _mod.__name__ + ".ClientSession",
            lambda **kwargs: _fake_session(fake_get),
        )

        await _mod.main()

        content = dest.read_text(encoding="UTF-8")
        assert "Data Structures" in content
        assert "4" in content
        assert "Old Name" not in content

    @pytest.mark.anyio
    async def test_csv_format(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        """Should produce valid CSV with header."""
        dest = tmp_path / "fmt.csv"

        subjects_html = """\
<div class="subject">
  <span class="subject-code">COMP</span>
  <a href="/ugcourse/COMP">CS</a>
</div>"""
        courses_html = """\
<div class="crse-header">
  <span class="crse-code">COMP2011</span>
  <span class="crse-title">Data Structures</span>
  <span class="crse-unit">4 Credit(s)</span>
</div>"""

        monkeypatch.setattr("builtins.input", lambda prompt="": fspath(dest))
        fake_get = _fake_session_factory(subjects_html, {"COMP": courses_html})
        monkeypatch.setattr(
            _mod.__name__ + ".ClientSession",
            lambda **kwargs: _fake_session(fake_get),
        )

        await _mod.main()

        lines = dest.read_text(encoding="UTF-8").strip().split("\n")
        assert lines[0] == "code,name,credit"
        assert len(lines) == 2

    @pytest.mark.anyio
    async def test_no_subjects_found(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        """Should produce header-only CSV when no subjects are found."""
        dest = tmp_path / "empty.csv"

        monkeypatch.setattr("builtins.input", lambda prompt="": fspath(dest))
        fake_get = _fake_session_factory("<html></html>", {})
        monkeypatch.setattr(
            _mod.__name__ + ".ClientSession",
            lambda **kwargs: _fake_session(fake_get),
        )

        await _mod.main()

        content = dest.read_text(encoding="UTF-8").strip()
        assert content == "code,name,credit"
