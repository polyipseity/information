#!/usr/bin/env python
# /// script
# dependencies = [
#     "pymupdf>=1.25.0",
#     "python-docx>=1.1.0",
#     "python-pptx>=1.0.0",
#     "pillow>=12.0.0",
# ]
# requires-python = ">=3.13.0"
# /// script
"""Extract text and page images from document-like formats (PDF, DOCX, PPTX).

Dual extraction always runs: text for flashcards/search/Markdown, page images
for visual content (diagrams, formulas, handwritten notes). Outputs are
persisted in a .extracted/ folder near the source document with a manifest
for cache validation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

import pymupdf
from docx import Document
from pptx import Presentation


@dataclass(frozen=True)
class DocumentResult:
    text: str
    images: list[Path]
    format: str
    page_count: int
    cached: bool


def _sha256(path: Path) -> str:
    """Compute SHA-256 hex digest of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_text_pdf(path: Path) -> str:
    """Extract text from a PDF, page by page."""
    doc = pymupdf.open(path)
    parts: list[str] = []
    for i, page in enumerate(doc.pages()):
        text = page.get_text()
        if text.strip():
            parts.append(f"## Page {i + 1}\n\n{text.strip()}")
    doc.close()
    return "\n\n".join(parts)


def extract_pages_pdf(path: Path, output_dir: Path) -> list[Path]:
    """Render each PDF page as a PNG image at 150 DPI."""
    output_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(path)
    image_paths: list[Path] = []
    for i, page in enumerate(doc.pages()):
        pix = page.get_pixmap(dpi=150)
        out = output_dir / f"page_{i + 1:03d}.png"
        pix.save(out)
        image_paths.append(out)
    doc.close()
    return image_paths


def extract_text_docx(path: Path) -> str:
    """Extract text from a DOCX file."""
    doc = Document(str(path))
    parts: list[str] = []
    for para in doc.paragraphs:
        if para.text.strip():
            parts.append(para.text.strip())
    return "\n\n".join(parts)


def extract_text_pptx(path: Path) -> str:
    """Extract text from a PPTX file, slide by slide."""
    prs = Presentation(str(path))
    parts: list[str] = []
    for i, slide in enumerate(prs.slides):
        slide_text: list[str] = []
        for shape in slide.shapes:
            if hasattr(shape, "text") and shape.text.strip():
                slide_text.append(shape.text.strip())
        if slide_text:
            parts.append(f"## Slide {i + 1}\n\n" + "\n\n".join(slide_text))
    return "\n\n".join(parts)


def extract_pages_pptx(path: Path, output_dir: Path) -> list[Path]:
    """Render each PPTX slide as a PNG via LibreOffice conversion.

    Returns empty list if LibreOffice is not available.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            [
                "libreoffice",
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                str(output_dir),
                str(path),
            ],
            check=True,
            capture_output=True,
            timeout=60,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return []

    pdf_name = path.stem + ".pdf"
    pdf_path = output_dir / pdf_name
    if pdf_path.exists():
        images = extract_pages_pdf(pdf_path, output_dir)
        pdf_path.unlink()
        return images
    return []


EXTENSION_MAP = {
    ".pdf": ("pdf", extract_text_pdf, extract_pages_pdf),
    ".docx": ("docx", extract_text_docx, None),
    ".pptx": ("pptx", extract_text_pptx, extract_pages_pptx),
}


def is_extracted_valid(output_dir: Path, source_path: Path) -> bool:
    """Check if existing extraction is still valid for the source."""
    manifest_path = output_dir / "manifest.json"
    if not manifest_path.exists():
        return False
    if not (output_dir / "text.md").exists():
        return False
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False
    return manifest.get("source_sha256") == _sha256(source_path)


def process_document(
    path: Path,
    output_dir: Path,
    *,
    force: bool = False,
) -> DocumentResult:
    """Process a document file and extract text + page images.

    If output_dir already contains a valid extraction (matching manifest),
    returns the cached result without re-extracting. Pass force=True to
    override.

    Returns dict with keys:
      - "text": extracted markdown text
      - "images": list of page image Paths (may be empty)
      - "format": detected format string ("pdf", "docx", "pptx")
      - "page_count": number of pages/slides rendered as images
      - "cached": True if reused existing extraction
    """
    suffix = path.suffix.lower()
    if suffix not in EXTENSION_MAP:
        raise ValueError(f"Unsupported format: {suffix}")

    # Check cache
    if not force and is_extracted_valid(output_dir, path):
        text = (output_dir / "text.md").read_text(encoding="utf-8")
        pages_dir = output_dir / "pages"
        images = sorted(pages_dir.glob("page_*.png")) if pages_dir.exists() else []
        manifest = json.loads(
            (output_dir / "manifest.json").read_text(encoding="utf-8")
        )
        return DocumentResult(
            text=text,
            images=images,
            format=manifest["format"],
            page_count=manifest["page_count"],
            cached=True,
        )

    fmt, text_fn, pages_fn = EXTENSION_MAP[suffix]
    text = text_fn(path)

    images: list[Path] = []
    if pages_fn is not None:
        pages_dir = output_dir / "pages"
        images = pages_fn(path, pages_dir)

    # Write text
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "text.md").write_text(text, encoding="utf-8")

    # Write manifest
    manifest = {
        "source_name": path.name,
        "source_sha256": _sha256(path),
        "format": fmt,
        "page_count": len(images),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )

    return DocumentResult(
        text=text,
        images=images,
        format=fmt,
        page_count=len(images),
        cached=False,
    )


def main(argv: Sequence[str] | None = None) -> None:
    """CLI entry point: convert_document.py [--force] <input> <output_dir>"""

    parser = argparse.ArgumentParser(
        description="Extract text and page images from documents",
    )
    parser.add_argument("input", type=Path, help="Input document path")
    parser.add_argument("output_dir", type=Path, help="Output directory")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-extract even if cached output exists",
    )
    args = parser.parse_args(argv)

    if not args.input.exists():
        print(f"Error: {args.input} not found", file=sys.stderr)
        exit(1)

    result = process_document(args.input, args.output_dir, force=args.force)

    status = "cached" if result.cached else "extracted"
    text_path = args.output_dir / "text.md"
    print(f"[{status}] Format: {result.format}")
    print(f"  Text: {text_path} ({len(result.text)} chars)")
    print(f"  Images: {result.page_count} pages")


def __main__() -> None:
    main()


if __name__ == "__main__":
    __main__()
