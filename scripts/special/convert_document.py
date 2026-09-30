#!/usr/bin/env python
"""Extract text, page images, and embedded images from documents (PDF, DOCX, PPTX).

Three extractions always run: text for flashcards/search/Markdown, rendered page
images for reading visual content with vision, and the document's own embedded
images for the rare graphic that has to be kept as a file. Outputs are persisted
in a .extracted/ folder near the source document with a manifest for cache
validation.
"""

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
from docx.parts.image import ImagePart
from pptx import Presentation
from pptx.shapes.picture import Picture

"""Exported names from this module (none: standalone script, not importable as a library)."""
__all__ = ()

"""Smallest embedded image kept, in pixels.

Anything thinner than this in either direction is decoration — a rule, bullet,
border, or icon — rather than content. The manifest records how many were
dropped, so the filter never hides a graphic silently.
"""
MIN_IMAGE_SIDE = 32


@dataclass(frozen=True)
class EmbeddedImages:
    """Embedded images written for one document, plus how many were filtered out."""

    paths: tuple[Path, ...]
    skipped: int


@dataclass(frozen=True)
class DocumentResult:
    """Result of document extraction."""

    text: str
    pages: tuple[Path, ...]
    embedded_images: tuple[Path, ...]
    embedded_images_skipped: int
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


def extract_pages_pdf(path: Path, output_dir: Path) -> tuple[Path, ...]:
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
    return tuple(image_paths)


def extract_images_pdf(path: Path, output_dir: Path) -> EmbeddedImages:
    """Write the PDF's own embedded raster images, named for the page holding them.

    These are the images as they exist inside the document, not the 150 DPI page
    renders: a figure is kept at its true resolution instead of being re-photographed
    along with the slide around it.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(path)
    written: list[Path] = []
    skipped = 0
    for i, page in enumerate(doc.pages()):
        for n, info in enumerate(page.get_images(full=True), start=1):
            width, height = info[2], info[3]
            if min(width, height) < MIN_IMAGE_SIDE:
                skipped += 1
                continue
            image = doc.extract_image(info[0])
            out = output_dir / f"page_{i + 1:03d}_img_{n}.{image['ext']}"
            out.write_bytes(image["image"])
            written.append(out)
    doc.close()
    return EmbeddedImages(paths=tuple(written), skipped=skipped)


def extract_text_docx(path: Path) -> str:
    """Extract text from a DOCX file."""
    doc = Document(str(path))
    parts: list[str] = []
    for para in doc.paragraphs:
        if para.text.strip():
            parts.append(para.text.strip())
    return "\n\n".join(parts)


def extract_images_docx(path: Path, output_dir: Path) -> EmbeddedImages:
    """Write the DOCX package's own embedded images, in part-name order.

    A DOCX has no page notion, so images are numbered by their position in the
    package rather than by any location in the rendered document.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    doc = Document(str(path))
    parts = sorted(
        (part for part in doc.part.package.parts if isinstance(part, ImagePart)),
        key=lambda part: str(part.partname),
    )
    written: list[Path] = []
    skipped = 0
    for n, part in enumerate(parts, start=1):
        if min(part.image.px_width, part.image.px_height) < MIN_IMAGE_SIDE:
            skipped += 1
            continue
        out = output_dir / f"image_{n:03d}{Path(part.filename).suffix}"
        out.write_bytes(part.blob)
        written.append(out)
    return EmbeddedImages(paths=tuple(written), skipped=skipped)


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


def extract_pages_pptx(path: Path, output_dir: Path) -> tuple[Path, ...]:
    """Render each PPTX slide as a PNG via LibreOffice conversion.

    Returns empty tuple if LibreOffice is not available.
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
        return ()

    pdf_name = path.stem + ".pdf"
    pdf_path = output_dir / pdf_name
    if pdf_path.exists():
        images = extract_pages_pdf(pdf_path, output_dir)
        pdf_path.unlink()
        return images
    return ()


def extract_images_pptx(path: Path, output_dir: Path) -> EmbeddedImages:
    """Write the PPTX's own embedded pictures, named for the slide holding them."""
    output_dir.mkdir(parents=True, exist_ok=True)
    prs = Presentation(str(path))
    written: list[Path] = []
    skipped = 0
    for i, slide in enumerate(prs.slides, start=1):
        n = 0
        for shape in slide.shapes:
            if not isinstance(shape, Picture):
                continue
            n += 1
            image = shape.image
            width, height = image.size
            if min(width, height) < MIN_IMAGE_SIDE:
                skipped += 1
                continue
            out = output_dir / f"slide_{i:03d}_img_{n}.{image.ext}"
            out.write_bytes(image.blob)
            written.append(out)
    return EmbeddedImages(paths=tuple(written), skipped=skipped)


"""Supported source extensions mapped to their kind and extractor functions.

Each value is ``(kind, text extractor, page extractor, image extractor)``; the
page extractor is ``None`` for formats without rendered page images.
"""
EXTENSION_MAP = {
    ".pdf": ("pdf", extract_text_pdf, extract_pages_pdf, extract_images_pdf),
    ".docx": ("docx", extract_text_docx, None, extract_images_docx),
    ".pptx": ("pptx", extract_text_pptx, extract_pages_pptx, extract_images_pptx),
}


def is_extracted_valid(output_dir: Path, source_path: Path) -> bool:
    """Check if existing extraction is still valid for the source.

    Every output the current extractor writes must be present, and the manifest
    hash must match the source. `images/` is created even when a document holds
    no embedded image, so its absence marks an extraction written by an older
    layout and forces a re-extract instead of silently returning a partial cache.
    """
    manifest_path = output_dir / "manifest.json"
    if not manifest_path.exists():
        return False
    if not (output_dir / "text.md").exists():
        return False
    if not (output_dir / "images").is_dir():
        return False
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False
    return manifest.get("source_sha256") == _sha256(source_path)


def _cached_files(output_dir: Path, subdir: str) -> tuple[Path, ...]:
    """Return the sorted files of a cached `.extracted/` subdirectory, if it exists."""
    directory = output_dir / subdir
    if not directory.is_dir():
        return ()
    return tuple(sorted(directory.glob("*")))


def process_document(
    path: Path,
    output_dir: Path,
    *,
    force: bool = False,
) -> DocumentResult:
    """Process a document file and extract text, page images, and embedded images.

    If output_dir already contains a valid extraction (matching manifest),
    returns the cached result without re-extracting. Pass force=True to
    override.
    """
    suffix = path.suffix.lower()
    if suffix not in EXTENSION_MAP:
        raise ValueError(f"Unsupported format: {suffix}")

    # Check cache
    if not force and is_extracted_valid(output_dir, path):
        manifest = json.loads(
            (output_dir / "manifest.json").read_text(encoding="utf-8")
        )
        return DocumentResult(
            text=(output_dir / "text.md").read_text(encoding="utf-8"),
            pages=_cached_files(output_dir, "pages"),
            embedded_images=_cached_files(output_dir, "images"),
            embedded_images_skipped=manifest["image_skipped_count"],
            format=manifest["format"],
            page_count=manifest["page_count"],
            cached=True,
        )

    fmt, text_fn, pages_fn, images_fn = EXTENSION_MAP[suffix]
    text = text_fn(path)
    output_dir.mkdir(parents=True, exist_ok=True)

    pages: tuple[Path, ...] = ()
    if pages_fn is not None:
        pages = pages_fn(path, output_dir / "pages")

    images = images_fn(path, output_dir / "images")

    (output_dir / "text.md").write_text(text, encoding="utf-8")

    manifest = {
        "source_name": path.name,
        "source_sha256": _sha256(path),
        "format": fmt,
        "page_count": len(pages),
        "image_count": len(images.paths),
        "image_skipped_count": images.skipped,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )

    return DocumentResult(
        text=text,
        pages=pages,
        embedded_images=images.paths,
        embedded_images_skipped=images.skipped,
        format=fmt,
        page_count=len(pages),
        cached=False,
    )


def main(argv: Sequence[str] | None = None) -> None:
    """CLI entry point: convert_document.py [--force] <input> <output_dir>"""
    parser = argparse.ArgumentParser(
        description="Extract text, page images, and embedded images from documents",
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
    print(f"  Pages: {result.page_count} rendered")
    print(
        f"  Embedded images: {len(result.embedded_images)} written,"
        f" {result.embedded_images_skipped} filtered as decoration"
    )


def __main__() -> None:
    """Entry point for running the script directly."""
    main()


if __name__ == "__main__":
    __main__()
