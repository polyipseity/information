"""Tests for scripts/pack.py.

Covers: Arguments dataclass, modified_page_rank_stochastic_mat (PageRank matrix
construction), parser(), and main() (integration with real temp files + limited
mocking).

Note: ProcessMarkdownFileResult and MetadataJSONEncoder are local to main() and
cannot be imported at module level — they are tested indirectly via main().
"""

from __future__ import annotations

from collections.abc import Mapping, Set
from dataclasses import FrozenInstanceError
from pathlib import Path
from zipfile import ZipFile

import numpy as np
import pytest

from scripts import pack as _mod

# ---------------------------------------------------------------------------
# TestArguments
# ---------------------------------------------------------------------------


class TestArguments:
    """Tests for the Arguments frozen dataclass."""

    def test_attributes(self) -> None:
        """Should store all attributes."""
        args = _mod.Arguments(
            output=_mod.Path("out.zip"),
            root=_mod.Path("/root"),
            count=10,
            damping_factor=0.5,
            page_rank_iterations=100,
            exclude_extensions=[".pdf", ".png"],
            files=[_mod.Path("a.md"), _mod.Path("b.md")],
        )
        assert args.output == _mod.Path("out.zip")
        assert args.root == _mod.Path("/root")
        assert args.count == 10
        assert args.damping_factor == 0.5
        assert args.page_rank_iterations == 100

    def test_post_init_coerces_files_to_tuple(self) -> None:
        """files should be coerced to a tuple in __post_init__."""
        args = _mod.Arguments(
            output=_mod.Path("out.zip"),
            root=None,
            count=5,
            damping_factor=0.5,
            page_rank_iterations=10,
            exclude_extensions=[],
            files=[_mod.Path("a.md"), _mod.Path("b.md")],
        )
        assert isinstance(args.files, tuple)
        assert args.files == (_mod.Path("a.md"), _mod.Path("b.md"))

    def test_post_init_coerces_exclude_extensions(self) -> None:
        """exclude_extensions should be coerced to a tuple."""
        args = _mod.Arguments(
            output=_mod.Path("out.zip"),
            root=None,
            count=5,
            damping_factor=0.5,
            page_rank_iterations=10,
            exclude_extensions=[".pdf"],
            files=[_mod.Path("a.md")],
        )
        assert isinstance(args.exclude_extensions, tuple)
        assert args.exclude_extensions == (".pdf",)

    def test_frozen(self) -> None:
        """Should raise FrozenInstanceError when modifying."""
        args = _mod.Arguments(
            output=_mod.Path("o"),
            root=None,
            count=1,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(),
        )
        with pytest.raises(FrozenInstanceError):
            args.count = 99  # type: ignore[misc]

    def test_repr(self) -> None:
        """repr should include fields."""
        args = _mod.Arguments(
            output=_mod.Path("o"),
            root=None,
            count=1,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(),
        )
        r = repr(args)
        assert "Arguments(" in r
        assert "output=" in r

    def test_eq(self) -> None:
        """Equality should work."""
        kw = dict(
            output=_mod.Path("o"),
            root=None,
            count=1,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(),
        )
        assert _mod.Arguments(**kw) == _mod.Arguments(**kw)

    def test_root_none_allowed(self) -> None:
        """root may be None."""
        args = _mod.Arguments(
            output=_mod.Path("o"),
            root=None,
            count=1,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(),
        )
        assert args.root is None


# ---------------------------------------------------------------------------
# TestModifiedPageRankStochasticMat
# ---------------------------------------------------------------------------


class TestModifiedPageRankStochasticMat:
    """Tests for the modified_page_rank_stochastic_mat function."""

    @staticmethod
    def _p(*parts: str) -> Path:
        return Path(*parts)

    def test_two_node_graph(self) -> None:
        """A->B should produce a 2x2 stochastic matrix."""
        a = self._p("a.md")
        b = self._p("b.md")
        initial: Set[Path] = {a, b}
        links: Mapping[Path, Set[Path]] = {a: {b}, b: set()}
        ordered, mat = _mod.modified_page_rank_stochastic_mat(
            initial, links, damping=0.5
        )
        assert len(ordered) == 2
        assert mat.shape == (2, 2)
        np.testing.assert_allclose(mat.sum(axis=0), np.ones(2))

    def test_three_node_chain(self) -> None:
        """A->B, B->C should produce a 3x3 matrix."""
        a = self._p("a.md")
        b = self._p("b.md")
        c = self._p("c.md")
        initial: Set[Path] = {a, b, c}
        links: Mapping[Path, Set[Path]] = {a: {b}, b: {c}, c: set()}
        ordered, mat = _mod.modified_page_rank_stochastic_mat(
            initial, links, damping=0.8
        )
        assert len(ordered) == 3
        assert mat.shape == (3, 3)
        np.testing.assert_allclose(mat.sum(axis=0), np.ones(3))

    def test_single_node(self) -> None:
        """Single node with no links should produce a 1x1 matrix of all ones."""
        a = self._p("a.md")
        initial: Set[Path] = {a}
        links: Mapping[Path, Set[Path]] = {a: set()}
        _, mat = _mod.modified_page_rank_stochastic_mat(
            initial, links, damping=0.5
        )
        # damping * uniform(1) + (1-damping) * uniform(1) = [[1]]
        np.testing.assert_allclose(mat, np.ones((1, 1)))

    def test_damping_zero(self) -> None:
        """With damping=0, all probability teleports to initial nodes uniformly."""
        a = self._p("a.md")
        b = self._p("b.md")
        c = self._p("c.md")
        initial: Set[Path] = {a, b}
        links: Mapping[Path, Set[Path]] = {a: {c}, b: set(), c: {b}}
        ordered, mat = _mod.modified_page_rank_stochastic_mat(
            initial, links, damping=0.0
        )
        np.testing.assert_allclose(mat.sum(axis=0), np.ones(mat.shape[1]))
        idx_a = ordered.index(a)
        idx_b = ordered.index(b)
        # Only initial nodes get probability mass in each column
        for col in range(mat.shape[1]):
            assert np.isclose(mat[idx_a, col] + mat[idx_b, col], 1.0)

    def test_damping_one(self) -> None:
        """With damping=1, no teleportation; pure link-following."""
        a = self._p("a.md")
        b = self._p("b.md")
        initial: Set[Path] = {a, b}
        links: Mapping[Path, Set[Path]] = {a: {b}, b: set()}
        ordered, mat = _mod.modified_page_rank_stochastic_mat(
            initial, links, damping=1.0
        )
        np.testing.assert_allclose(mat.sum(axis=0), np.ones(2))
        idx_a = ordered.index(a)
        idx_b = ordered.index(b)
        assert np.isclose(mat[idx_b, idx_a], 1.0)  # a->b
        assert np.isclose(mat[idx_a, idx_b], 0.5)  # b->uniform
        assert np.isclose(mat[idx_b, idx_b], 0.5)

    def test_disconnected_graph(self) -> None:
        """Disconnected nodes: all columns are uniform."""
        a = self._p("a.md")
        b = self._p("b.md")
        initial: Set[Path] = {a, b}
        links: Mapping[Path, Set[Path]] = {}
        _, mat = _mod.modified_page_rank_stochastic_mat(
            initial, links, damping=0.5
        )
        np.testing.assert_allclose(mat, np.full((2, 2), 0.5))

    def test_all_nodes_initial(self) -> None:
        """All nodes in initial set: teleportation uniform over all."""
        a = self._p("a.md")
        b = self._p("b.md")
        c = self._p("c.md")
        initial: Set[Path] = {a, b, c}
        links: Mapping[Path, Set[Path]] = {a: {b}, b: {c}, c: {a}}
        ordered, mat = _mod.modified_page_rank_stochastic_mat(
            initial, links, damping=0.5
        )
        np.testing.assert_allclose(mat.sum(axis=0), np.ones(3))
        idx_a, idx_b, idx_c = ordered.index(a), ordered.index(b), ordered.index(c)
        # Column a: 0.5 * link(a->b) + 0.5 * uniform
        assert np.isclose(mat[idx_b, idx_a], 0.5 * 1.0 + 0.5 * 1 / 3)
        assert np.isclose(mat[idx_a, idx_a], 0.5 * 1 / 3)

    def test_returns_ordered_paths(self) -> None:
        """Ordered paths should contain all nodes."""
        a = self._p("z.md")
        b = self._p("a.md")
        initial: Set[Path] = {a, b}
        links: Mapping[Path, Set[Path]] = {a: {b}}
        ordered, _ = _mod.modified_page_rank_stochastic_mat(
            initial, links, damping=0.5
        )
        assert set(ordered) == {a, b}

    def test_matrix_type(self) -> None:
        """Should return NDArray[float64]."""
        a = self._p("a.md")
        initial: Set[Path] = {a}
        _, mat = _mod.modified_page_rank_stochastic_mat(
            initial, {}, damping=0.5
        )
        assert mat.dtype == np.float64


# ---------------------------------------------------------------------------
# TestParser
# ---------------------------------------------------------------------------


class TestParser:
    """Tests for the parser() function."""

    def test_returns_argument_parser(self) -> None:
        """Should return an ArgumentParser."""
        from argparse import ArgumentParser

        p = _mod.parser()
        assert isinstance(p, ArgumentParser)

    def test_default_output(self) -> None:
        """Default output should be set."""
        p = _mod.parser()
        defaults = p.parse_args(["/dev/null"])
        assert defaults.output is not None

    def test_default_count(self) -> None:
        """Default count should be 25."""
        p = _mod.parser()
        defaults = p.parse_args(["/dev/null"])
        assert defaults.count == 25

    def test_default_damping_factor(self) -> None:
        """Default damping factor should be 0.5."""
        p = _mod.parser()
        defaults = p.parse_args(["/dev/null"])
        assert defaults.damping_factor == 0.5

    def test_default_page_rank_iterations(self) -> None:
        """Default page rank iterations should be 100."""
        p = _mod.parser()
        defaults = p.parse_args(["/dev/null"])
        assert defaults.page_rank_iterations == 100

    def test_custom_output(self) -> None:
        """Custom -o flag should be stored."""
        p = _mod.parser()
        args = p.parse_args(["-o", "custom.zip", "file.md"])
        assert str(args.output) == "custom.zip"

    def test_custom_count(self) -> None:
        """Custom -n flag should be stored."""
        p = _mod.parser()
        args = p.parse_args(["-n", "50", "file.md"])
        assert args.count == 50

    def test_custom_damping(self) -> None:
        """Custom -d flag should be stored."""
        p = _mod.parser()
        args = p.parse_args(["-d", "0.85", "file.md"])
        assert args.damping_factor == 0.85

    def test_custom_root(self) -> None:
        """Custom -r flag should be stored."""
        p = _mod.parser()
        args = p.parse_args(["-r", "/some/root", "file.md"])
        assert str(args.root) == "/some/root"

    def test_files_collected(self) -> None:
        """Positional files argument should be collected."""
        p = _mod.parser()
        args = p.parse_args(["a.md", "b.md", "c.md"])
        assert [str(f) for f in args.files] == ["a.md", "b.md", "c.md"]

    def test_exclude_extensions(self) -> None:
        """Custom -e flag with ZERO_OR_MORE — use -- to stop option parsing."""
        p = _mod.parser()
        args = p.parse_args(["-e", ".pdf", ".png", "--", "file.md"])
        assert args.exclude_extension == [".pdf", ".png"]

    def test_invoke_is_callable(self) -> None:
        """Parsed namespace should have an 'invoke' callable."""
        p = _mod.parser()
        defaults = p.parse_args(["/dev/null"])
        assert callable(defaults.invoke)

    def test_parser_with_parent(self) -> None:
        """Should accept a parent parser factory."""
        from argparse import ArgumentParser as AP

        parent = lambda **kw: AP(**kw)
        p = _mod.parser(parent=parent)
        import argparse

        assert isinstance(p, argparse.ArgumentParser)

    def test_negative_count_allowed(self) -> None:
        """Negative count should be parsed (means 'all files')."""
        p = _mod.parser()
        args = p.parse_args(["-n", "-1", "file.md"])
        assert args.count == -1


# ---------------------------------------------------------------------------
# TestMain
# ---------------------------------------------------------------------------


class TestMain:
    """Tests for the main(args) function.

    Uses real files in tmp_path for robust path resolution, plus minimal
    mocking of ZipFile to capture output in memory.
    """

    @pytest.mark.anyio
    async def test_no_files_raises(self) -> None:
        """Should raise ValueError when files is empty."""
        args = _mod.Arguments(
            output=_mod.Path("out.zip"),
            root=None,
            count=10,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(),
        )
        with pytest.raises(ValueError, match="No files to pack"):
            await _mod.main(args)

    @pytest.mark.anyio
    async def test_negative_damping_raises(self) -> None:
        """Should raise ValueError when damping < 0."""
        args = _mod.Arguments(
            output=_mod.Path("out.zip"),
            root=None,
            count=10,
            damping_factor=-0.1,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(_mod.Path("a.md"),),
        )
        with pytest.raises(
            ValueError, match="Damping factor should be between 0 and 1"
        ):
            await _mod.main(args)

    @pytest.mark.anyio
    async def test_damping_above_one_raises(self) -> None:
        """Should raise ValueError when damping > 1."""
        args = _mod.Arguments(
            output=_mod.Path("out.zip"),
            root=None,
            count=10,
            damping_factor=1.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(_mod.Path("a.md"),),
        )
        with pytest.raises(
            ValueError, match="Damping factor should be between 0 and 1"
        ):
            await _mod.main(args)

    @pytest.mark.anyio
    async def test_root_not_contain_files_raises(
        self, tmp_path: Path
    ) -> None:
        """Should raise ValueError when root does not contain all files."""
        output = tmp_path / "out.zip"
        root = tmp_path / "root"
        root.mkdir()
        file_outside = tmp_path / "outside" / "a.md"
        file_outside.parent.mkdir()
        file_outside.write_text("content")

        args = _mod.Arguments(
            output=_mod.Path(output),
            root=_mod.Path(root),
            count=10,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(_mod.Path(file_outside),),
        )

        with pytest.raises(
            ValueError, match="The specified root does not contain"
        ):
            await _mod.main(args)

    @pytest.mark.anyio
    async def test_simple_markdown_file(self, tmp_path: Path) -> None:
        """Should pack a single markdown file with no links."""
        root = tmp_path / "root"
        root.mkdir()
        (root / "doc.md").write_text("Just text.")
        output = tmp_path / "out.zip"

        args = _mod.Arguments(
            output=_mod.Path(output),
            root=_mod.Path(root),
            count=10,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(_mod.Path(root / "doc.md"),),
        )

        await _mod.main(args)

        assert output.exists()
        assert output.stat().st_size > 0

        with ZipFile(output) as zf:
            names = zf.namelist()
            assert "doc.md" in names
            assert any(n.startswith("metadata") for n in names)

    @pytest.mark.anyio
    async def test_two_files_with_link(self, tmp_path: Path) -> None:
        """Should handle a file linking to another in the same dir."""
        root = tmp_path / "root"
        root.mkdir()
        (root / "a.md").write_text("[b](b.md)")
        (root / "b.md").write_text("Target.")
        output = tmp_path / "out.zip"

        args = _mod.Arguments(
            output=_mod.Path(output),
            root=_mod.Path(root),
            count=10,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(_mod.Path(root / "a.md"),),
        )

        await _mod.main(args)

        with ZipFile(output) as zf:
            names = zf.namelist()
            assert "a.md" in names
            assert "b.md" in names  # discovered via link

    @pytest.mark.anyio
    async def test_directory_input_expanded(
        self, tmp_path: Path
    ) -> None:
        """When a file argument is a directory, it should be expanded recursively."""
        root = tmp_path / "root"
        root.mkdir()
        sub = root / "sub"
        sub.mkdir()
        (root / "a.md").write_text("")
        (sub / "b.md").write_text("")
        output = tmp_path / "out.zip"

        args = _mod.Arguments(
            output=_mod.Path(output),
            root=_mod.Path(root),
            count=10,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(_mod.Path(root),),
        )

        await _mod.main(args)

        with ZipFile(output) as zf:
            names = zf.namelist()
            assert "a.md" in names
            assert "sub/b.md" in names

    @pytest.mark.anyio
    async def test_exclude_extension_skips(
        self, tmp_path: Path
    ) -> None:
        """Files with excluded extensions should not appear in output."""
        root = tmp_path / "root"
        root.mkdir()
        (root / "doc.md").write_text("")
        (root / "ignore.pdf").write_text("")
        (root / "doc.txt").write_text("")
        output = tmp_path / "out.zip"

        args = _mod.Arguments(
            output=_mod.Path(output),
            root=_mod.Path(root),
            count=10,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(".pdf",),
            files=(_mod.Path(root / "doc.md"), _mod.Path(root / "ignore.pdf")),
        )

        await _mod.main(args)

        with ZipFile(output) as zf:
            names = zf.namelist()
            assert "doc.md" in names
            # .pdf is excluded; .txt is not in files
            assert not any("ignore.pdf" in n for n in names)
            assert not any("doc.txt" in n for n in names)

    @pytest.mark.anyio
    async def test_negative_count_keeps_all(self, tmp_path: Path) -> None:
        """Negative count should keep all files (no filtering)."""
        root = tmp_path / "root"
        root.mkdir()
        (root / "a.md").write_text("")
        (root / "b.md").write_text("")
        output = tmp_path / "out.zip"

        args = _mod.Arguments(
            output=_mod.Path(output),
            root=_mod.Path(root),
            count=-1,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(_mod.Path(root / "a.md"), _mod.Path(root / "b.md")),
        )

        await _mod.main(args)

        with ZipFile(output) as zf:
            names = zf.namelist()
            assert "a.md" in names
            assert "b.md" in names

    @pytest.mark.anyio
    async def test_missing_link_target_recorded(self, tmp_path: Path) -> None:
        """Links to non-existent files should be recorded in metadata as missing."""
        root = tmp_path / "root"
        root.mkdir()
        (root / "doc.md").write_text("[missing](nonexistent.md)")
        output = tmp_path / "out.zip"

        args = _mod.Arguments(
            output=_mod.Path(output),
            root=_mod.Path(root),
            count=10,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(_mod.Path(root / "doc.md"),),
        )

        await _mod.main(args)

        import json

        with ZipFile(output) as zf:
            metadata_name = [n for n in zf.namelist() if n.startswith("metadata")][0]
            meta = json.loads(zf.read(metadata_name))
            assert "missing_paths" in meta
            assert any("nonexistent" in p for p in meta["missing_paths"])

    @pytest.mark.anyio
    async def test_metadata_contains_arguments(self, tmp_path: Path) -> None:
        """Metadata JSON should include the serialised Arguments."""
        root = tmp_path / "root"
        root.mkdir()
        (root / "doc.md").write_text("content")
        output = tmp_path / "out.zip"

        args = _mod.Arguments(
            output=_mod.Path(output),
            root=_mod.Path(root),
            count=10,
            damping_factor=0.5,
            page_rank_iterations=1,
            exclude_extensions=(),
            files=(_mod.Path(root / "doc.md"),),
        )

        await _mod.main(args)

        import json

        with ZipFile(output) as zf:
            metadata_name = [n for n in zf.namelist() if n.startswith("metadata")][0]
            meta = json.loads(zf.read(metadata_name))
            assert "arguments" in meta
            assert "damping_factor" in meta["arguments"]
            assert meta["arguments"]["damping_factor"] == 0.5
            assert meta["arguments"]["count"] == 10
            assert "root" in meta["arguments"]
            assert "output" in meta["arguments"]


# ---------------------------------------------------------------------------
# TestMain0
# ---------------------------------------------------------------------------


class TestMain0:
    """Minimal tests for the main0() entry point."""

    @pytest.mark.anyio
    async def test_invokes_main(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should parse argv and invoke main()."""
        monkeypatch.setattr(
            _mod.__name__ + ".argv",
            ["pack.py", "/dev/null", "--exclude-extension", ".zip"],
        )
        called = False

        async def fake_main(args: object) -> None:
            nonlocal called
            called = True

        monkeypatch.setattr(_mod.__name__ + ".main", fake_main)

        await _mod.main0()
        assert called
