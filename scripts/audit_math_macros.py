#!/usr/bin/env python
"""Audit the math macros used by the Markdown notes and report the ones Obsidian lacks."""

from argparse import ArgumentParser
from collections.abc import Sequence
from pathlib import Path
from re import DOTALL
from re import compile as re_compile

"""Exported names from this module (none: standalone script, not importable as a library)."""
__all__ = ()

"""Macros that Obsidian 1.15.0 (MathJax 4.1.3) does not define, mapped to the definition to add to its MathJax preamble."""
POLYFILLS: dict[str, str] = {
    "Eta": r"\mathrm{H}",
    "argmax": r"\mathop{\mathrm{arg\,max}}",
    "argmin": r"\mathop{\mathrm{arg\,min}}",
    "Z": r"\mathbb{Z}",
    "degree": r"{}^\circ",
    "texteuro": r"\text{€}",
}

"""Misspelled macros, mapped to the macro that the note means."""
TYPO_FIXES: dict[str, str] = {"sqdeert": "sqrt"}

"""Root directories audited when no paths are given on the command line."""
DEFAULT_PATHS: tuple[str, ...] = ("general", "special", "self")

"""Maximum number of example paths printed for each cataloged macro."""
EXAMPLE_LIMIT = 3

"""Math delimiters as (opener, closer, may span lines), longest opener first so that ``$$`` wins over ``$``."""
_MATH_DELIMITERS: tuple[tuple[str, str, bool], ...] = (
    ("$$", "$$", True),
    ("\\[", "\\]", True),
    ("$", "$", False),
    ("\\(", "\\)", False),
)

"""Backslash pairs that stand for a literal character and never open math."""
_ESCAPED_CHARACTERS: tuple[str, ...] = ("\\\\", "\\$")

"""Regex matching a YAML frontmatter block at the very start of a note."""
_FRONTMATTER_REGEX = re_compile(
    r"\A---[ \t]*\r?\n(?:.*?\r?\n)?---[ \t]*(?:\r?\n|\Z)", DOTALL
)

"""Regex matching the fence of a fenced code block, which may be indented by up to three spaces."""
_FENCE_REGEX = re_compile(r"[ \t]{0,3}(?P<fence>`{3,}|~{3,})")


def _strip_frontmatter(text: str) -> str:
    """Drop a leading YAML frontmatter block, which holds metadata rather than prose."""
    return _FRONTMATTER_REGEX.sub("", text, count=1)


def _is_fence_close(line: str, fence: str) -> bool:
    """Return whether line closes a fenced code block opened by fence."""
    stripped = line.strip()
    return len(stripped) >= len(fence) and stripped == fence[0] * len(stripped)


def _strip_blockquote(line: str) -> str:
    """Return the line without the blockquote markers of an excerpt."""
    rest = line.lstrip()
    while rest.startswith(">"):
        rest = rest[1:].lstrip()
    return rest


def _strip_fenced_code(text: str) -> str:
    """Blank out fenced code blocks so that their dollars and backslashes stay out of the audit.

    The line breaks are kept because inline math may not span a line.
    """
    lines: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        blank = line[len(line.rstrip("\r\n")) :]
        content = _strip_blockquote(line)
        if fence is None:
            match = _FENCE_REGEX.match(content)
            if match is None:
                lines.append(line)
            else:
                fence = match.group("fence")
                lines.append(blank)
            continue
        if _is_fence_close(content, fence):
            fence = None
        lines.append(blank)
    return "".join(lines)


def _find_backtick_run(text: str, start: int, length: int) -> int | None:
    """Return the start index of the next backtick run of exactly length, or None."""
    index = start
    while index < len(text):
        if text[index] != "`":
            index += 1
            continue
        end = index
        while end < len(text) and text[end] == "`":
            end += 1
        if end - index == length:
            return index
        index = end
    return None


def _strip_inline_code(text: str) -> str:
    """Replace inline code spans with a space so that their backslashes stay out of the audit.

    An unmatched backtick run is left alone because it is prose rather than code.
    """
    parts: list[str] = []
    index = 0
    while index < len(text):
        if text[index] != "`":
            next_tick = text.find("`", index)
            end = len(text) if next_tick == -1 else next_tick
            parts.append(text[index:end])
            index = end
            continue
        run_end = index
        while run_end < len(text) and text[run_end] == "`":
            run_end += 1
        length = run_end - index
        close = _find_backtick_run(text, run_end, length)
        if close is None:
            parts.append(text[index:run_end])
            index = run_end
            continue
        parts.append(" ")
        index = close + length
    return "".join(parts)


def _find_closer(
    text: str, start: int, closer: str, may_span_lines: bool
) -> int | None:
    """Return the index of the closing delimiter at or after start, or None.

    A backslash consumes the character after it, so an escaped delimiter never closes math.
    """
    index = start
    while index < len(text):
        if text.startswith(closer, index):
            return index
        if not may_span_lines and text[index] == "\n":
            return None
        index += 2 if text[index] == "\\" else 1
    return None


def _math_segments(text: str) -> list[str]:
    """Return the contents of every math segment of a note, in document order.

    Frontmatter, fenced code blocks, and inline code are dropped first so that
    their dollars and backslashes cannot reach the macro scanner. ``$$`` and
    ``\\[...\\]`` may span lines; ``$`` and ``\\(...\\)`` must close on the line
    that opens them. An escaped ``\\$`` never opens or closes math.
    """
    text = _strip_inline_code(_strip_fenced_code(_strip_frontmatter(text)))
    segments: list[str] = []
    index = 0
    while index < len(text):
        if any(text.startswith(escape, index) for escape in _ESCAPED_CHARACTERS):
            index += 2
            continue
        for opener, closer, may_span_lines in _MATH_DELIMITERS:
            if not text.startswith(opener, index):
                continue
            start = index + len(opener)
            end = _find_closer(text, start, closer, may_span_lines)
            if end is not None:
                segments.append(text[start:end])
                index = end + len(closer)
                break
        else:
            index += 1
    return segments


def _is_ascii_letter(character: str) -> bool:
    """Return whether character is a letter of the ASCII alphabet."""
    return character.isascii() and character.isalpha()


def _macro_names(segment: str) -> set[str]:
    """Return the names of the macros used in a math segment.

    ``\\\\`` is TeX's line break, not a macro, so it is skipped as a whole.
    Otherwise the first letter of the next line would be read as a macro name.
    """
    names: set[str] = set()
    index = 0
    while index < len(segment):
        if segment[index] != "\\":
            index += 1
            continue
        index += 1
        if segment.startswith("\\", index):
            index += 1
            continue
        start = index
        while index < len(segment) and _is_ascii_letter(segment[index]):
            index += 1
        if index > start:
            names.add(segment[start:index])
    return names


def _collect_files(roots: Sequence[Path]) -> list[Path]:
    """Return the readable Markdown files under roots, without duplicates.

    Paths are resolved for identity so that the alias links of the notes are
    audited once and dangling ones are dropped; the first path seen is kept so
    that the report shows paths as they were named.
    """
    files: dict[Path, Path] = {}
    for root in roots:
        candidates = sorted(root.rglob("*.md")) if root.is_dir() else [root]
        for candidate in candidates:
            try:
                real_path = candidate.resolve(strict=True)
            except OSError:
                continue
            if real_path.is_file():
                files.setdefault(real_path, candidate)
    return list(files.values())


def _audit(paths: Sequence[Path]) -> dict[str, set[Path]]:
    """Return the files that use each macro, keyed by macro name."""
    usage: dict[str, set[Path]] = {}
    for path in paths:
        for segment in _math_segments(path.read_text(encoding="utf-8")):
            for name in _macro_names(segment):
                usage.setdefault(name, set()).add(path)
    return usage


def _print_catalog(
    usage: dict[str, set[Path]], catalog: dict[str, str], label: str
) -> None:
    """Print each cataloged macro with its definition, its file count, and a few example paths."""
    for name, definition in catalog.items():
        paths = sorted(usage.get(name, set()))
        print(f"  \\{name}: {label} {definition}; {len(paths)} file(s)")
        for path in paths[:EXAMPLE_LIMIT]:
            print(f"    {path}")


def main(argv: Sequence[str] | None = None) -> None:
    """Print the polyfill and typo report for the given paths, which default to the note roots."""
    parser = ArgumentParser(description="Audit the math macros used by the notes.")
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[],
        metavar="PATH",
        help="files or directories to audit; defaults to general, special, and self",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="also list every macro used in math, with its file count",
    )
    arguments = parser.parse_args(argv)

    roots = arguments.paths or [Path(path) for path in DEFAULT_PATHS]
    files = _collect_files(roots)
    usage = _audit(files)

    print(f"Audited {len(files)} file(s); found {len(usage)} distinct math macros.")
    print()
    print(
        "Polyfills (missing from Obsidian; definitions to add to the MathJax preamble):"
    )
    _print_catalog(usage, POLYFILLS, "defined as")
    print()
    print("Typo fixes (misspelled macros; fix the note):")
    _print_catalog(usage, TYPO_FIXES, "should be")
    if arguments.all:
        print()
        print("All macros used in math:")
        entries = sorted(usage.items(), key=lambda entry: (-len(entry[1]), entry[0]))
        for name, paths in entries:
            print(f"  \\{name}: {len(paths)} file(s)")


def __main__() -> None:
    """Entry point for running the script directly."""
    main()


if __name__ == "__main__":
    __main__()
