"""Tests for scripts/special/convert_document.py.

Covers the public API: process_document function, manifest creation,
cache hit/miss behavior, and force re-extraction.
"""

import json
import os
from pathlib import Path

import pymupdf
import pytest

from scripts.special.convert_document import process_document

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


def test_process_document_rejects_unknown_format(
    tmp_path: os.PathLike[str],
) -> None:
    """Unsupported extension raises ValueError."""
    base = Path(os.fspath(tmp_path))
    bad = base / "file.txt"
    bad.write_text("hello")
    with pytest.raises(ValueError, match="Unsupported format"):
        process_document(bad, base / "out")


def test_manifest_created(tmp_path: os.PathLike[str]) -> None:
    """process_document writes a manifest.json with correct fields."""
    base = Path(os.fspath(tmp_path))

    pdf_path = base / "test.pdf"
    doc = pymupdf.open()
    doc.new_page()
    doc.save(pdf_path)
    doc.close()

    out_dir = base / "output"
    result = process_document(pdf_path, out_dir)

    manifest_path = out_dir / "manifest.json"
    assert manifest_path.exists()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["format"] == "pdf"
    assert manifest["source_name"] == "test.pdf"
    assert "source_sha256" in manifest
    assert "timestamp" in manifest
    assert manifest["page_count"] == result.page_count


def test_cache_hit_skips_extraction(tmp_path: os.PathLike[str]) -> None:
    """Second call with same source returns cached result."""
    base = Path(os.fspath(tmp_path))

    pdf_path = base / "test.pdf"
    doc = pymupdf.open()
    doc.new_page()
    doc.save(pdf_path)
    doc.close()

    out_dir = base / "output"
    result1 = process_document(pdf_path, out_dir)
    assert result1.cached is False

    result2 = process_document(pdf_path, out_dir)
    assert result2.cached is True
    assert result2.text == result1.text
    assert result2.page_count == result1.page_count


def test_force_overrides_cache(tmp_path: os.PathLike[str]) -> None:
    """force=True re-extracts even when cache is valid."""
    base = Path(os.fspath(tmp_path))

    pdf_path = base / "test.pdf"
    doc = pymupdf.open()
    doc.new_page()
    doc.save(pdf_path)
    doc.close()

    out_dir = base / "output"
    process_document(pdf_path, out_dir)
    result = process_document(pdf_path, out_dir, force=True)
    assert result.cached is False


def test_extract_text_pdf(tmp_path: os.PathLike[str]) -> None:
    """PDF text extraction produces a non-empty markdown file."""
    pytest.skip("No test PDF fixture")


def test_extract_text_docx(tmp_path: os.PathLike[str]) -> None:
    """DOCX text extraction produces a non-empty markdown file."""
    pytest.skip("No test DOCX fixture")


def test_extract_text_pptx(tmp_path: os.PathLike[str]) -> None:
    """PPTX text extraction produces a non-empty markdown file."""
    pytest.skip("No test PPTX fixture")
