"""Validation rules for course notes.

This module contains a large collection of functions that enforce various
structural and content conventions for ``special/academia`` Markdown files.
Each rule is a self‑contained test that inspects the file text or parsed
frontmatter and returns zero or more ``ValidationMessage`` objects.  New
rules can be added by creating a function and registering it with the
``RULE_REGISTRY`` decorator; see the ``Extending the validator`` section of
`.agents/skills/academic-notes/SKILL.md` for a step‑by‑step workflow.

Rather than relying on a global registry the module provides its own
:class:`RuleRegistry` instance below; rules are registered with
``RULE_REGISTRY`` via a decorator.  The rules are pure functions returning a
list of ``ValidationMessage`` instances when violations are detected.

Each function is registered with the local ``RULE_REGISTRY`` instance using
its decorator.  The functions are pure: they accept a
:class:`ValidationContext` and return a sequence of
:class:`ValidationMessage` objects.
"""

import re
import unicodedata
from string import punctuation
from urllib.parse import unquote

from anyio import Path

from .models import Severity, ValidationContext, ValidationMessage
from .registry import RuleRegistry
from .utils import FRONT_RE, has_flash_tag, locate, locate_range

"""Public symbols exported by this module."""
__all__ = ("RULE_REGISTRY",)

# single registry used by this module; external code may import and merge it
"""Registry of all validation rules in this module; decorator-based registration."""
RULE_REGISTRY = RuleRegistry()

# metadata checks ------------------------------------------------------------


@RULE_REGISTRY.register()
def metadata_aliases_present(ctx: ValidationContext) -> list[ValidationMessage]:
    """Rule: file must include an 'aliases:' field in YAML frontmatter.

    Returns a list containing an error message if the tag is missing.
    """
    errors: list[ValidationMessage] = []
    if "aliases:" not in ctx.front:
        errors.append(
            ValidationMessage(
                "metadata_aliases_present", "no 'aliases:' in frontmatter"
            )
        )
    return errors


@RULE_REGISTRY.register()
def metadata_tags_present(ctx: ValidationContext) -> list[ValidationMessage]:
    """Rule: YAML frontmatter must contain a 'tags:' entry.

    Produces an error message if the tags field is absent.
    """
    errors: list[ValidationMessage] = []
    if "tags:" not in ctx.front:
        errors.append(
            ValidationMessage("metadata_tags_present", "no 'tags:' in frontmatter")
        )
    return errors


@RULE_REGISTRY.register()
def metadata_flash_tag(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure that the tags list includes a flashcard activation tag.

    Only checks when a tags section is present; emits an error if no flash tag
    is found.
    """
    errors: list[ValidationMessage] = []
    if "tags:" in ctx.front and not has_flash_tag(ctx.front):
        errors.append(
            ValidationMessage(
                "metadata_flash_tag", "missing flashcard activation tag in 'tags:'"
            )
        )
    return errors


@RULE_REGISTRY.register()
def aliases_sorted(ctx: ValidationContext) -> list[ValidationMessage]:
    """Check that the aliases list in frontmatter is sorted alphabetically.

    Comparison is case-sensitive; an error is returned if ordering differs.
    """
    errors: list[ValidationMessage] = []
    aliases = ctx.data.aliases
    if aliases != sorted(aliases):
        errors.append(
            ValidationMessage(
                "aliases_sorted", "'aliases' list is not alphabetically sorted"
            )
        )
    return errors


@RULE_REGISTRY.register()
def tag_language(ctx: ValidationContext) -> list[ValidationMessage]:
    """Require a language tag of 'language/in/English' in the tags list.

    This ensures all notes are explicitly marked as English-language content.
    """
    errors: list[ValidationMessage] = []
    tags: list[str] = ctx.data.tags or []
    if "language/in/English" not in tags:
        errors.append(
            ValidationMessage("tag_language", "missing 'language/in/English' tag")
        )
    return errors


@RULE_REGISTRY.register()
def tag_index_function(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure that index.md files include the 'function/index' tag.

    Only applies when the filename is literally 'index.md'.
    """
    errors: list[ValidationMessage] = []
    tags: list[str] = ctx.data.tags or []
    if ctx.path.name.lower() == "index.md" and "function/index" not in tags:
        errors.append(
            ValidationMessage(
                "tag_index_function", "index page missing 'function/index' tag"
            )
        )
    return errors


@RULE_REGISTRY.register()
def tag_path_flash(ctx: ValidationContext) -> list[ValidationMessage]:
    """Verify that the tags include a flashcard tag matching the file path.

    Constructs a path-derived string and checks whether any tag contains it.
    Errors if no such tag is present.  Only runs when some tags exist.
    """
    errors: list[ValidationMessage] = []
    tags: list[str] = ctx.data.tags or []
    if tags:
        pstr = str(ctx.path.as_posix())
        marker = "special/academia/"
        if marker in pstr:
            rel = pstr.split(marker, 1)[1]
            rel = rel.replace(".md", "")

            # convert spaces, single quotes, and double quotes to underscores
            def _clean(part: str) -> str:
                """Normalize a path segment: spaces/quotes to underscores, collapse/trim."""
                s = re.sub(r"[ \"']+", "_", part)
                s = re.sub(r"_+", "_", s)
                return s.strip("_")

            rel = "/".join(_clean(part) for part in rel.split("/"))
            found = any(rel in t for t in tags)
            if not found:
                errors.append(
                    ValidationMessage(
                        "tag_path_flash",
                        f"tags do not include flash tag matching file path '{rel}'",
                    )
                )
    return errors


# index structure -----------------------------------------------------------


@RULE_REGISTRY.register()
def index_heading(ctx: ValidationContext) -> list[ValidationMessage]:
    """Check that an index.md contains a top-level '# index' heading.

    Only applicable to files named 'index.md'.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() == "index.md":
        if "# index" not in ctx.text:
            errors.append(
                ValidationMessage("index_heading", "index.md missing '# index' heading")
            )
    return errors


def _extract_named_h2_section(text: str, heading: str) -> list[tuple[int, str]]:
    """Return the lines contained within a named `## <heading>` section.

    The section begins after a matching level-2 heading and ends at the next
    header of the same or higher level (i.e. a line starting with `#`).

    Returns a list of (line_number, line_text) tuples.
    """

    lines = text.splitlines()
    start_line = None
    for idx, line in enumerate(lines):
        if re.match(rf"^##\s+{re.escape(heading)}\s*$", line, re.IGNORECASE):
            start_line = idx + 1
            break
    if start_line is None:
        return []

    section: list[tuple[int, str]] = []
    for idx in range(start_line, len(lines)):
        if re.match(r"^#{1,2}\s+", lines[idx]):
            break
        section.append((idx + 1, lines[idx]))
    return section


def _extract_children_section(text: str) -> list[tuple[int, str]]:
    """Return the lines contained within the `## children` section."""

    return _extract_named_h2_section(text, "children")


async def _path_exists(href: str, base: Path) -> bool:
    """Check if a linked file/directory exists on disk.

    Decodes percent-encoded components and checks for directory or file
    existence. Returns False for external URLs or invalid paths.
    """
    # Decode percent-encoded components (e.g. %20 → space)
    unquoted = unquote(href)
    # Remove any fragment/query portion
    unquoted = re.split(r"[#?]", unquoted, 1)[0]
    if not unquoted:
        return False

    # Skip external URLs
    if re.match(r"^[a-zA-Z]+://", unquoted):
        return True  # Consider external URLs as "existing" (not our responsibility)

    # anyio Path methods are async; use them directly.
    candidate = await (base / unquoted).resolve()
    return await candidate.is_dir() or await candidate.is_file()


async def _is_folder_without_index_md(href: str, base: Path) -> bool:
    """Check if href links to index.md in a folder that exists but lacks index.md.

    Returns True if:
    - href ends with /index.md or is index.md
    - The parent folder exists
    - The index.md file does not exist

    This detects the case where a children link may need the index.md file created
    or should be changed to link to the folder instead.
    """
    # Decode percent-encoded components
    unquoted = unquote(href)
    unquoted = re.split(r"[#?]", unquoted, 1)[0]
    if not unquoted:
        return False

    # Check if this is a link to index.md
    if not (unquoted.endswith("/index.md") or unquoted.endswith("index.md")):
        return False

    # Get the parent directory (remove index.md from the path)
    if unquoted.endswith("/index.md"):
        parent_path = unquoted[:-9]  # Remove "/index.md" (9 characters)
    else:
        parent_path = unquoted[:-8]  # Remove "index.md" (8 characters)

    # Ensure parent path is not empty
    if not parent_path or parent_path == "/":
        return False

    # Check if parent folder exists but index.md doesn't
    candidate_parent = await (base / parent_path).resolve()
    return (
        await candidate_parent.is_dir()
        and not await (candidate_parent / "index.md").is_file()
    )


@RULE_REGISTRY.register()
def index_children(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure index.md includes a 'children' section or heading.

    Looks for either '## children' or a literal 'children:' string.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() == "index.md":
        if "## children" not in ctx.text and "children:" not in ctx.text:
            errors.append(
                ValidationMessage(
                    "index_children", "index.md missing 'children' section"
                )
            )
    return errors


@RULE_REGISTRY.register()
async def index_children_agents_link(ctx: ValidationContext) -> list[ValidationMessage]:
    """Require a precise AGENTS link in index children when AGENTS.md exists.

    If ``AGENTS.md`` exists in the same folder as ``index.md``, the
    ``## children`` section must contain exactly one entry
    ``- [AGENTS](AGENTS.md)``.
    """

    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() != "index.md":
        return errors

    agents_path = ctx.path.parent / "AGENTS.md"
    if not await agents_path.is_file():
        return errors

    section = _extract_children_section(ctx.text)
    if not section:
        return errors

    heading_match = re.search(
        r"^##\s+children\s*$", ctx.text, re.IGNORECASE | re.MULTILINE
    )
    heading_line = None
    if heading_match:
        heading_line, _ = locate(ctx.text, heading_match.start())

    entries: list[tuple[int, str, str]] = []
    for line_no, line in section:
        stripped = line.strip()
        if not stripped or stripped.startswith("<!--"):
            continue
        m = re.match(r"^[-*]\s*\[([^\]]+)\]\(([^\)]+)\)\s*$", stripped)
        if not m:
            continue
        display = m.group(1).strip()
        href = m.group(2).strip()
        href_clean = re.split(r"[#?]", href, 1)[0]
        if href_clean.casefold() == "agents.md":
            entries.append((line_no, display, href_clean))

    if not entries:
        errors.append(
            ValidationMessage(
                "index_children_agents_link",
                "AGENTS.md exists but children section is missing '- [AGENTS](AGENTS.md)'",
                line=heading_line,
                col=1 if heading_line is not None else None,
            )
        )
        return errors

    if len(entries) > 1:
        line_no = entries[1][0]
        errors.append(
            ValidationMessage(
                "index_children_agents_link",
                "children section contains multiple AGENTS links; keep exactly one '- [AGENTS](AGENTS.md)' entry",
                line=line_no,
                col=1,
            )
        )

    line_no, display, href_clean = entries[0]
    if display != "AGENTS" or href_clean != "AGENTS.md":
        errors.append(
            ValidationMessage(
                "index_children_agents_link",
                "AGENTS link must be exactly '- [AGENTS](AGENTS.md)'",
                line=line_no,
                col=1,
            )
        )
    return errors


@RULE_REGISTRY.register()
def index_non_suppression_html_comments(
    ctx: ValidationContext,
) -> list[ValidationMessage]:
    """Disallow non-suppression HTML comments in index.md.

    Course-local agent guidance should live in ``AGENTS.md``. The only HTML
    comments allowed in ``index.md`` are validator suppression directives such
    as ``<!-- check: ignore-line[...] -->``.
    """

    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() != "index.md":
        return errors

    for m in re.finditer(r"<!--(.*?)-->", ctx.text, re.DOTALL):
        body = m.group(1).strip()
        if re.match(r"^check:\s*ignore-(line|next-line|file)\[", body, re.IGNORECASE):
            continue
        line_no, col_no, col_end = locate_range(ctx.text, m.start(), len(m.group(0)))
        errors.append(
            ValidationMessage(
                "index_non_suppression_html_comments",
                "non-suppression HTML comments are not allowed in index.md; move agent instructions/context to AGENTS.md",
                line=line_no,
                col=col_no,
                col_end=col_end,
            )
        )
    return errors


@RULE_REGISTRY.register()
def index_canvas_metadata_iso_datetime(
    ctx: ValidationContext,
) -> list[ValidationMessage]:
    """Require ISO datetime and duration values in Canvas-derived leaf indexes.

    Applies to assignment-style leaf ``index.md`` pages under ``assignments`` or
    ``labs``. The rule inspects metadata bullets in ``## description`` and
    ``## logistics`` and requires ISO 8601 values for due timestamps,
    availability endpoints or ranges, and durations.
    """

    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() != "index.md":
        return errors

    path_str = ctx.path.as_posix().casefold()
    if not re.search(r"/(assignments|labs)/[^/]+/index\.md$", path_str):
        return errors

    iso_datetime = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}"
    iso_duration = (
        r"P(?!$)(?:\d+Y)?(?:\d+M)?(?:\d+W)?(?:\d+D)?(?:T(?:\d+H)?(?:\d+M)?(?:\d+S)?)?"
    )
    iso_range = rf"{iso_datetime}/{iso_datetime}(?:,\s*{iso_duration})?"

    def _push(line_no: int, line: str, msg: str) -> None:
        errors.append(
            ValidationMessage(
                "index_canvas_metadata_iso_datetime",
                msg,
                line=line_no,
                col=1,
                col_end=len(line) if line else 1,
            )
        )

    sections = _extract_named_h2_section(
        ctx.text, "description"
    ) + _extract_named_h2_section(ctx.text, "logistics")
    for line_no, line in sections:
        stripped = line.strip()
        m = re.match(r"^-\s*([^:]+):\s*(.+)$", stripped)
        if not m:
            continue
        key = m.group(1).strip().casefold()
        value = m.group(2).strip()

        if key == "due":
            if value.casefold() == "tbd":
                continue
            if not re.fullmatch(iso_datetime, value):
                _push(
                    line_no,
                    stripped,
                    "Canvas-derived due metadata must use one ISO datetime with timezone",
                )
        elif key in {"available until", "locked at", "start", "end"}:
            if not re.fullmatch(iso_datetime, value):
                _push(
                    line_no,
                    stripped,
                    f"Canvas-derived '{key}' metadata must use one ISO datetime with timezone",
                )
        elif key == "available":
            if not (
                re.fullmatch(rf"until\s+{iso_datetime}", value)
                or re.fullmatch(iso_range, value)
            ):
                _push(
                    line_no,
                    stripped,
                    "Canvas-derived availability metadata must use 'until <ISO datetime>' or '<ISO start>/<ISO end>, <ISO duration>'",
                )
        elif "duration" in key and not re.fullmatch(iso_duration, value):
            _push(
                line_no,
                stripped,
                "Canvas-derived duration metadata must use ISO duration syntax",
            )

    return errors


@RULE_REGISTRY.register()
def index_children_format(ctx: ValidationContext) -> list[ValidationMessage]:
    """Validate the format of the `## children` list in an index.md file.

    The children section must be an unordered list of Markdown links (no
    nested bulleted lists). This rule enforces a strict bullet format and
    rejects any item that is not a single Markdown link.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() != "index.md":
        return errors

    section = _extract_children_section(ctx.text)
    if not section:
        return errors

    for line_no, line in section:
        stripped = line.strip()
        if not stripped or stripped.startswith("<!--"):
            continue
        # Disallow nested list entries (indentation implies nesting)
        indent = len(line) - len(line.lstrip(" \t"))
        if indent > 0:
            errors.append(
                ValidationMessage(
                    "index_children_format",
                    "children list items must be top-level bullets (no nested sub-lists)",
                    line=line_no,
                    col=1,
                )
            )
            continue
        # Must be a simple markdown link list item (- [text](href))
        if not re.match(r"^[-*]\s*\[[^\]]+\]\([^\)]+\)\s*$", stripped):
            errors.append(
                ValidationMessage(
                    "index_children_format",
                    "children list must consist of top-level bullet points each containing a single Markdown link",
                    line=line_no,
                    col=1,
                )
            )
    return errors


@RULE_REGISTRY.register()
async def index_children_order(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure the `## children` list is ordered folders first, then files.

    Within each group (folders vs files), entries must be sorted using Python
    string ordering. Missing files/directories are skipped and handled by
    the dedicated index_children_missing.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() != "index.md":
        return errors

    section = _extract_children_section(ctx.text)
    if not section:
        return errors

    entries: list[tuple[bool, str, int]] = []
    base_dir = ctx.path.parent
    for line_no, line in section:
        stripped = line.strip()
        if not stripped or stripped.startswith("<!--"):
            continue
        m = re.match(r"^[-*]\s*\[([^\]]+)\]\(([^\)]+)\)\s*$", stripped)
        if not m:
            # ignore formatting errors; those are handled by other rules
            continue
        href = m.group(2).strip()
        # Skip entries where the path doesn't exist
        if not await _path_exists(href, base_dir):
            continue
        # Default to file unless the path actually resolves to a folder (or an index.md)
        is_folder = await _is_folder_link(href, base_dir, allow_index_as_folder=True)
        entries.append((is_folder, href, line_no))

    # Ensure all folders come before any files
    seen_file = False
    for is_folder, href, line_no in entries:
        if seen_file and is_folder:
            errors.append(
                ValidationMessage(
                    "index_children_order",
                    "folder entries in children section must come before file entries",
                    line=line_no,
                    col=1,
                )
            )
            # Only report once for the first violation
            break
        if not is_folder:
            seen_file = True

    # Check alphabetical ordering within each subgroup (folders and files)
    for group_name, group_entries in (
        ("folder", [e for e in entries if e[0]]),
        (
            "file",
            [e for e in entries if not e[0]],
        ),
    ):
        keys = [href for _, href, _ in group_entries]
        sorted_keys = sorted(keys)
        if keys != sorted_keys and keys:
            # Find the first out-of-order entry
            for (is_folder, href, line_no), expected in zip(group_entries, sorted_keys):
                if href != expected:
                    errors.append(
                        ValidationMessage(
                            "index_children_order",
                            f"{group_name.capitalize()} entries in children section must be in Python alphabetical order; expected '{expected}'",
                            line=line_no,
                            col=1,
                        )
                    )
                    break
            break
    return errors


async def _is_folder_link(
    href: str, base: Path, *, allow_index_as_folder: bool = True
) -> bool:
    """Return True if *href* refers to a folder (or folder index) on disk.

    A link is treated as a folder link if it points to an existing directory.
    If *allow_index_as_folder* is True, a link that resolves to an existing
    ``index.md`` file is also treated as a folder (useful for sorting in
    children sections).  Otherwise, ``index.md`` is treated as a regular file.
    """

    # Decode percent-encoded components (e.g. %20 → space)
    unquoted = unquote(href)
    # Remove any fragment/query portion
    unquoted = re.split(r"[#?]", unquoted, 1)[0]
    if not unquoted:
        return False

    # Skip obvious external URLs
    if re.match(r"^[a-zA-Z]+://", unquoted):
        return False

    # If the link explicitly has a trailing slash, treat as folder
    if unquoted.endswith("/"):
        return True

    # anyio Path methods are async; use them directly.
    candidate = await (base / unquoted).resolve()
    if await candidate.is_dir():
        return True
    if (
        allow_index_as_folder
        and await candidate.is_file()
        and candidate.name == "index.md"
    ):
        return True
    return False


@RULE_REGISTRY.register()
async def index_children_missing(
    ctx: ValidationContext,
) -> list[ValidationMessage]:
    """Check for missing files/directories in the `## children` list.

    Identifies links in the children section that do not exist on disk and
    suggests either removing the link (if not wanted) or creating the file/
    directory (if wanted). Excludes folders without index.md (handled by
    index_children_missing_index).
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() != "index.md":
        return errors

    section = _extract_children_section(ctx.text)
    if not section:
        return errors

    base_dir = ctx.path.parent
    for line_no, line in section:
        stripped = line.strip()
        if not stripped or stripped.startswith("<!--"):
            continue
        m = re.match(r"^[-*]\s*\[([^\]]+)\]\(([^\)]+)\)\s*$", stripped)
        if not m:
            # ignore formatting errors; those are handled by other rules
            continue
        href = m.group(2).strip()
        # Skip this if it's a folder-without-index case (handled by another rule)
        if await _is_folder_without_index_md(href, base_dir):
            continue
        # Check if the path exists
        if not await _path_exists(href, base_dir):
            errors.append(
                ValidationMessage(
                    "index_children_missing",
                    f"linked file/directory not found: '{href}'; either remove the link if not wanted or create the file/directory if desired",
                    line=line_no,
                    col=1,
                    severity=Severity.WARNING,
                )
            )
    return errors


@RULE_REGISTRY.register()
async def index_children_missing_index(
    ctx: ValidationContext,
) -> list[ValidationMessage]:
    """Check for links to index.md in folders that lack index.md.

    Detects when a children link points to index.md in a folder that exists
    but does not contain an index.md file. Suggests either creating the
    index.md file or changing the link to point to the folder instead.
    Note: attachments/ typically should not have index.md.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() != "index.md":
        return errors

    section = _extract_children_section(ctx.text)
    if not section:
        return errors

    base_dir = ctx.path.parent
    for line_no, line in section:
        stripped = line.strip()
        if not stripped or stripped.startswith("<!--"):
            continue
        m = re.match(r"^[-*]\s*\[([^\]]+)\]\(([^\)]+)\)\s*$", stripped)
        if not m:
            continue
        href = m.group(2).strip()
        # Check if this is a folder-without-index case
        if await _is_folder_without_index_md(href, base_dir):
            errors.append(
                ValidationMessage(
                    "index_children_missing_index",
                    f"folder '{href}' exists but lacks index.md; either create index.md "
                    "or change the link to the folder without /index.md "
                    "(note: attachments/ folders typically should not have index.md)",
                    line=line_no,
                    col=1,
                    severity=Severity.WARNING,
                )
            )
    return errors


@RULE_REGISTRY.register()
async def folder_link_trailing_slash(
    ctx: ValidationContext,
) -> list[ValidationMessage]:
    """Ensure markdown links to folders end with a trailing slash.

    This applies to any file, not just index.md, and helps keep links
    consistent between folder-style references and file-style references.
    """
    errors: list[ValidationMessage] = []
    base_dir = ctx.path.parent

    for m in re.finditer(r"\[([^\]]+)\]\(([^\)]+)\)", ctx.text):
        display = m.group(1).strip()
        href = m.group(2).strip()
        if not href or href.startswith("#"):
            continue
        if re.match(r"^[a-zA-Z]+://", href):
            continue
        if await _is_folder_link(href, base_dir, allow_index_as_folder=False):
            if not href.endswith("/"):
                line_no, col, col_end = locate_range(ctx.text, m.start(2), len(href))
                errors.append(
                    ValidationMessage(
                        "folder_link_trailing_slash",
                        "links to folders must end with a trailing slash",
                        line=line_no,
                        col=col,
                        col_end=col_end,
                    )
                )
            elif not display.endswith("/"):
                line_no, col, col_end = locate_range(ctx.text, m.start(1), len(display))
                errors.append(
                    ValidationMessage(
                        "folder_link_trailing_slash",
                        "folder link display text should end with a trailing slash",
                        line=line_no,
                        col=col,
                        col_end=col_end,
                    )
                )
    return errors


@RULE_REGISTRY.register()
def index_semester_order(ctx: ValidationContext) -> list[ValidationMessage]:
    """Verify chronological ordering of semester headings in index.md.

    Parses '### YYYY term' headings and ensures each is later than the
    previous.  Emits an error on the first out-of-order heading.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() != "index.md":
        return errors
    semesters: list[tuple[int, int, str]] = []
    term_map = {"winter": 1, "spring": 2, "summer": 3, "fall": 4}
    for line in ctx.text.splitlines():
        m = re.match(r"###\s+(\d{4})\s+([A-Za-z]+)", line)
        if m:
            year = int(m.group(1))
            term = m.group(2).lower()
            order = term_map.get(term)
            if order:
                semesters.append((year, order, line))
    for i in range(1, len(semesters)):
        if semesters[i][:2] < semesters[i - 1][:2]:
            msg = f"semester headings are not in chronological order ({semesters[i][2]} comes before {semesters[i - 1][2]})"
            lines = ctx.text.splitlines()
            try:
                line_no = lines.index(semesters[i][2]) + 1
            except ValueError:
                line_no = None
            col_no = 1 if line_no is not None else None
            errors.append(
                ValidationMessage("index_semester_order", msg, line=line_no, col=col_no)
            )
            break
    return errors


# session-related -----------------------------------------------------------

"""Compile a regex pattern for validating session headings of the form
'## week N type [number]'.

Allowed types are lecture, lab, or tutorial, optionally followed by a
number (e.g. 'lecture 2'). The pattern is case-insensitive and ignores
leading/trailing whitespace. Status information (e.g. 'status: no class')
should not appear in the heading and is not relevant to validation; it
belongs in the metadata section of the session entry."""
_SESSION_HEADING_VALID = re.compile(
    r"^##\s+week\s+\d+\s+((?:lecture|lab|tutorial)(?:\s+\d+)?)\s*$",
    re.IGNORECASE,
)


@RULE_REGISTRY.register()
def session_heading_format(ctx: ValidationContext) -> list[ValidationMessage]:
    """Require session headings to use only week N type [number].

    Allowed: ## week 1 lecture, ## week 1 lecture 2, ## week 2 lab 1. Type = lecture|lab|tutorial only.
    Invalid: ## week 3 no class, ## week 3 (Lunar New Year), ## week 3 (no type). Status belongs in metadata only.
    """
    errors: list[ValidationMessage] = []
    for m in re.finditer(
        r"^##\s+week\s+\d+\s*.+$", ctx.text, re.IGNORECASE | re.MULTILINE
    ):
        line = m.group(0).rstrip()
        if not _SESSION_HEADING_VALID.match(line):
            line_no, col, col_end = locate_range(ctx.text, m.start(), len(line))
            errors.append(
                ValidationMessage(
                    "session_heading_format",
                    "invalid session heading; use week N type [number] "
                    "(e.g. week 1 lecture, week 1 lecture 2); status has no bearing on heading",
                    line=line_no,
                    col=col,
                    col_end=col_end,
                )
            )
    # Also flag ## week N with no type at all (nothing after the number)
    for m in re.finditer(
        r"^##\s+week\s+(\d+)\s*$", ctx.text, re.IGNORECASE | re.MULTILINE
    ):
        line = m.group(0)
        line_no, col, col_end = locate_range(ctx.text, m.start(), len(line))
        errors.append(
            ValidationMessage(
                "session_heading_format",
                "session heading must include type (e.g. lecture, lecture 2)",
                line=line_no,
                col=col,
                col_end=col_end,
            )
        )
    return errors


@RULE_REGISTRY.register()
def session_duplicate_heading(ctx: ValidationContext) -> list[ValidationMessage]:
    """Detect duplicate week/type session headings within a file.

    If the same (week, type) pair appears more than once, emit an error
    pointing at the repeated header.
    """
    errors: list[ValidationMessage] = []
    seen_pairs: dict[tuple[str, str], int] = {}
    for week, typ, hdr, idx in ctx.session_headers:
        pair = (week, typ)
        if pair in seen_pairs:
            line, col, col_end = locate_range(ctx.text, idx, len(hdr))
            errors.append(
                ValidationMessage(
                    "session_duplicate_heading",
                    f"duplicate session heading {hdr!r} (week {week} {typ})",
                    line=line,
                    col=col,
                    col_end=col_end,
                )
            )
        seen_pairs[pair] = idx
    return errors


@RULE_REGISTRY.register()
def session_datetime_order(ctx: ValidationContext) -> list[ValidationMessage]:
    """Check that session datetimes are strictly increasing.

    Iterates through session headers in file order, parsing any ``datetime:``
    field and ensuring it is later than the previous session's datetime.
    """
    errors: list[ValidationMessage] = []
    last_datetime = None
    text = ctx.text
    for _week, _typ, hdr, idx in ctx.session_headers:
        end = len(text)
        m2 = re.search(r"^##\s+", text[idx + len(hdr) :], re.MULTILINE)
        if m2:
            end = idx + len(hdr) + m2.start()
        section = text[idx:end]
        mdt = re.search(r"^\s*-\s*datetime:\s*(\S+)", section, re.MULTILINE)
        if mdt:
            dt = mdt.group(1)
            if last_datetime and dt < last_datetime:
                line, col, col_end = locate_range(ctx.text, idx, len(hdr))
                errors.append(
                    ValidationMessage(
                        "session_datetime_order",
                        f"session {hdr!r} has datetime {dt} not after previous session",
                        line=line,
                        col=col,
                        col_end=col_end,
                    )
                )
            last_datetime = dt
    return errors


# session topic rules -------------------------------------------------------


@RULE_REGISTRY.register()
def session_missing_topic(ctx: ValidationContext) -> list[ValidationMessage]:
    """Flag sessions that have a datetime but are missing a topic.

    This rule applies only when the session is not marked 'unscheduled' and
    not a no-class day (status: no class, or status: public holiday / public
    holiday: <name>).  No-class days omit topic per skill conventions.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text
    for _week, _typ, hdr, idx in ctx.session_headers:
        end = len(text)
        m2 = re.search(r"^##\s+", text[idx + len(hdr) :], re.MULTILINE)
        if m2:
            end = idx + len(hdr) + m2.start()
        section = text[idx:end]
        if re.search(r"^\s*-\s*datetime:", section, re.MULTILINE):
            # skip unscheduled sessions
            if "status:" in section and re.search(
                r"status:\s*unscheduled", section, re.IGNORECASE
            ):
                continue
            # skip no-class days (topic omitted per skill)
            if "status:" in section and (
                re.search(r"status:\s*no\s+class", section, re.IGNORECASE)
                or re.search(r"status:\s*public\s+holiday", section, re.IGNORECASE)
            ):
                continue
            if "topic:" not in section:
                line, col, col_end = locate_range(ctx.text, idx, len(hdr))
                errors.append(
                    ValidationMessage(
                        "session_missing_topic",
                        f"session {hdr!r} has a datetime but no topic field",
                        line=line,
                        col=col,
                        col_end=col_end,
                    )
                )
    return errors


@RULE_REGISTRY.register()
def session_unscheduled_with_topic(ctx: ValidationContext) -> list[ValidationMessage]:
    """Detect sessions marked unscheduled that nevertheless declare a topic.

    Before the refactor this was handled inside ``session_topic_presence``
    alongside the missing-topic check.  Splitting it makes the validator's
    output and any automated commit messages far easier to interpret.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text
    for _week, _typ, hdr, idx in ctx.session_headers:
        end = len(text)
        m2 = re.search(r"^##\s+", text[idx + len(hdr) :], re.MULTILINE)
        if m2:
            end = idx + len(hdr) + m2.start()
        section = text[idx:end]
        if re.search(r"^\s*-\s*datetime:", section, re.MULTILINE):
            if "status:" in section and re.search(
                r"status:\s*unscheduled", section, re.IGNORECASE
            ):
                if "topic:" in section:
                    line, col, col_end = locate_range(ctx.text, idx, len(hdr))
                    errors.append(
                        ValidationMessage(
                            "session_unscheduled_with_topic",
                            f"session {hdr!r} has status unscheduled but also a topic",
                            line=line,
                            col=col,
                            col_end=col_end,
                        )
                    )
    return errors


@RULE_REGISTRY.register()
def session_venue_presence(ctx: ValidationContext) -> list[ValidationMessage]:
    """Flag sessions with a datetime but missing a venue field.

    Applies to any session entry; location absence is considered an error.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text
    for _week, _typ, hdr, idx in ctx.session_headers:
        end = len(text)
        m2 = re.search(r"^##\s+", text[idx + len(hdr) :], re.MULTILINE)
        if m2:
            end = idx + len(hdr) + m2.start()
        section = text[idx:end]
        if (
            re.search(r"^\s*-\s*datetime:", section, re.MULTILINE)
            and "venue:" not in section
        ):
            line, col, col_end = locate_range(ctx.text, idx, len(hdr))
            errors.append(
                ValidationMessage(
                    "session_venue_presence",
                    f"session {hdr!r} has a datetime but no venue",
                    line=line,
                    col=col,
                    col_end=col_end,
                )
            )
    return errors


@RULE_REGISTRY.register()
def session_next_lecture_remark(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when a session entry mentions 'next lecture/week/class'.

    Such remarks are discouraged except for major grading events.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text
    for _week, _typ, hdr, idx in ctx.session_headers:
        end = len(text)
        m2 = re.search(r"^##\s+", text[idx + len(hdr) :], re.MULTILINE)
        if m2:
            end = idx + len(hdr) + m2.start()
        section = text[idx:end]
        if re.search(r"next\s+(lecture|week|class)", section, re.IGNORECASE):
            line, col, col_end = locate_range(ctx.text, idx, len(hdr))
            errors.append(
                ValidationMessage(
                    "session_next_lecture_remark",
                    f"session {hdr!r} contains a 'next lecture/next week' remark; remove unless major grading event",
                    line=line,
                    col=col,
                    col_end=col_end,
                )
            )
    return errors


@RULE_REGISTRY.register()
def session_exam_order(ctx: ValidationContext) -> list[ValidationMessage]:
    """Enforce that midterm/final sections come after other sessions.

    Scans for the first exam heading and flags any later session entries that
    occur before it in the file order.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text
    exam_idx = None
    for m in re.finditer(
        r"^##\s+(midterm|final)\b", text, re.IGNORECASE | re.MULTILINE
    ):
        exam_idx = m.start()
        break
    if exam_idx is not None:
        for _, _, _hdr, idx in ctx.session_headers:
            if idx > exam_idx:
                line, col = locate(ctx.text, idx)
                errors.append(
                    ValidationMessage(
                        rule_id="session_exam_order",
                        msg="exam section appears before some lecture/lab/tutorial entries — exams should be placed after other sessions",
                        line=line,
                        col=col,
                    )
                )
                break
    return errors


# header and flashcard style --------------------------------------------------


# This rule was originally added in response to a validator failure when
# a user created a 'numerical examples' section in ELEC 1100.  The
# accompanying SKILL.md documentation now points back to this clause as a
# worked example of how to extend the validator.
@RULE_REGISTRY.register()
def section_example_heading(ctx: ValidationContext) -> list[ValidationMessage]:
    """Error when any section heading contains the word "example".

    Course notes should **never** include stand‑alone "Example" or "Examples" sections.
    Instead the illustrative material belongs beneath the relevant conceptual
    heading (e.g. put circuit calculations under "KCL" rather than in an
    isolated "Examples" block).  If a file contains a header whose text
    includes the word *example* (case‑insensitive) the validator emits an
    error pointing at that heading and instructs the author to remove the
    entire section and integrate the examples appropriately.

    This rule is intentionally broad: it does **not** attempt to distinguish
    between a benign use of the word (e.g. "For example, consider…") and a
    problematic section title.  Authors who need to cite a real-world
    situation may either rewrite the heading or suppress the rule with the
    usual ``<!-- check: ignore-line[...] -->`` directive, but the default
    posture is to treat such sections as mistakes.
    """
    errors: list[ValidationMessage] = []
    # match any markdown header of level 1 or deeper containing 'example'
    # match 'example' or 'examples' in headers
    # match 'example' or 'examples' in headers but ignore hyphenated forms
    for m in re.finditer(
        r"^(#{1,})\s*(.*\bexamples?\b(?!-).*)$", ctx.text, re.IGNORECASE | re.MULTILINE
    ):
        hdr = m.group(0)
        start = m.start()
        line, col, col_end = locate_range(ctx.text, start, len(hdr))
        errors.append(
            ValidationMessage(
                "section_example_heading",
                "section heading contains the word 'example' (e.g. an isolated Examples subsection). "
                "Stand‑alone example sections are discouraged – integrate the illustrative material into the relevant conceptual "
                "paragraphs rather than copying the course layout verbatim.  Do *not* suppress two_sided_calc_warning or one_sided_calc_warning when the word "
                "example appears; the presence of examples signals numeric context that the calculator rules should enforce. "
                "If you genuinely require a separate examples block, add a clear justification using a suppression comment.",
                line=line,
                col=col,
                col_end=col_end,
            )
        )
    return errors


@RULE_REGISTRY.register()
def header_style(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when non-index headers start with an uppercase letter.

    This stylistic rule scans all headers of level 2 or deeper and emits a
    warning for headers whose first non-space character is an uppercase
    **Latin** letter (A–Z) or non-alphanumeric ASCII character.

    Non-Latin scripts (CJK, Cyrillic, Arabic, Greek, etc.) do not have
    uppercase/lowercase distinction and are exempted from this rule.

    Proper nouns in Latin scripts (person names, brands, acronyms) are
    legitimate exceptions; callers can suppress the warning using a check
    directive (for example
    ``<!-- check: ignore-line[header_style]: proper name -->``) if the
    capitalization is intentional.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() == "index.md":
        return errors
    for h in re.finditer(r"^(#{2,})\s+(.+)$", ctx.text, re.MULTILINE):
        hdr_text = h.group(2)
        if hdr_text:
            first_char = hdr_text[0]
            # Skip rule for non-cased letters (CJK, Cyrillic, Arabic, etc.)
            # Unicode category 'Lu' = uppercase letter, 'Ll' = lowercase letter
            # For non-cased scripts (e.g. CJK 'Lo' = other letter), skip the check
            char_category = unicodedata.category(first_char)

            # Only apply the rule to cased letters (uppercase/lowercase distinction)
            # Skip if it's a digit, or a non-cased letter (CJK, etc.)
            if char_category in ("Lu", "Ll"):
                # For cased letters, warn if uppercase
                if first_char.isupper():
                    start = h.start()
                    hdr_text_full = h.group(0)
                    line, col, col_end = locate_range(
                        ctx.text, start, len(hdr_text_full)
                    )
                    errors.append(
                        ValidationMessage(
                            rule_id="header_style",
                            msg="header normally start lowercase; suppressions are allowed only **for proper nouns** (person names, brands, acronyms).  Do **not** ignore this rule for ordinary section titles.",
                            severity=Severity.WARNING,
                            line=line,
                            col=col,
                            col_end=col_end,
                        )
                    )
    return errors


@RULE_REGISTRY.register()
def agents_title(ctx: ValidationContext) -> list[ValidationMessage]:
    """Require AGENTS.md to begin with '# <course code> agent instructions'."""

    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() != "agents.md":
        return errors

    expected = f"{ctx.path.parent.name} agent instructions"
    expected_header = f"# {expected}"
    body_start = len(ctx.text) - len(ctx.body)
    offset = body_start
    for line in ctx.body.splitlines(keepends=True):
        stripped = line.strip()
        if not stripped:
            offset += len(line)
            continue
        if stripped != expected_header:
            line_no, col_no, col_end = locate_range(
                ctx.text, offset, len(line.rstrip("\n"))
            )
            errors.append(
                ValidationMessage(
                    "agents_title",
                    f"AGENTS.md title must be exactly '{expected_header}'",
                    line=line_no,
                    col=col_no,
                    col_end=col_end,
                )
            )
        return errors

    errors.append(
        ValidationMessage(
            "agents_title",
            f"AGENTS.md is empty; add title '{expected_header}'",
        )
    )
    return errors


@RULE_REGISTRY.register()
def agents_no_flashcard_markup(ctx: ValidationContext) -> list[ValidationMessage]:
    """Disallow flashcard syntax in AGENTS.md files."""

    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() != "agents.md":
        return errors

    m = re.search(r"\{@\{|::@::|(?<!:):@:(?!:)", ctx.text)
    if m:
        line_no, col_no, col_end = locate_range(ctx.text, m.start(), len(m.group(0)))
        errors.append(
            ValidationMessage(
                "agents_no_flashcard_markup",
                "AGENTS.md must not contain flashcard markup ({@{ }@}, :@:, ::@::)",
                line=line_no,
                col=col_no,
                col_end=col_end,
            )
        )
    return errors


@RULE_REGISTRY.register()
def header_flashcard_presence(ctx: ValidationContext) -> list[ValidationMessage]:
    """Require that each non-index, non-questions header contains flashcard markers.

    Index and questions pages are not topic notes; they are exempt. Searches the
    text between the header and the next header at the same or higher level; if
    no flashcard syntax is found, an error is returned.

    This rule applies to headers at any level (e.g. #, ##, ###, etc.).
    """
    errors: list[ValidationMessage] = []
    name = ctx.path.name.lower()
    parent_parts = [part.casefold() for part in ctx.path.parts[:-1]]
    if (
        name == "index.md"
        or name == "questions.md"
        or name == "agents.md"
        or "questions" in parent_parts
    ):
        return errors
    for h in re.finditer(r"^(#{1,})\s+(.+)$", ctx.text, re.MULTILINE):
        lvl = len(h.group(1))
        start = h.end()
        pattern = r"^(#{1,%d})\s+" % lvl
        m = re.search(pattern, ctx.text[start:], re.MULTILINE)
        end = start + (m.start() if m else len(ctx.text) - start)
        section = ctx.text[start:end]
        if not re.search(r"::@::|:@:|Flashcards for", section):
            hdr = h.group(0).strip()
            start = h.start()
            line, col, col_end = locate_range(ctx.text, start, len(h.group(0)))
            errors.append(
                ValidationMessage(
                    rule_id="header_flashcard_presence",
                    msg=(
                        f"header {hdr!r} has no flashcard markers in its section; "
                        "convert key sentences into cards and include any relevant "
                        "diagrams or images from the paragraph above."
                    ),
                    line=line,
                    col=col,
                    col_end=col_end,
                )
            )
    return errors


@RULE_REGISTRY.register()
def header_flashcard_separator(ctx: ValidationContext) -> list[ValidationMessage]:
    """Enforce a '---' separator before flashcard markers under headers.

    Index and questions pages are exempt. When flashcards appear in a section,
    there should be a horizontal rule separating them from preceding text.

    This rule applies to headers at any level (e.g. #, ##, ###, etc.).
    """
    errors: list[ValidationMessage] = []
    name = ctx.path.name.lower()
    parent_parts = [part.casefold() for part in ctx.path.parts[:-1]]
    if (
        name == "index.md"
        or name == "questions.md"
        or name == "agents.md"
        or "questions" in parent_parts
    ):
        return errors
    for h in re.finditer(r"^(#{1,})\s+(.+)$", ctx.text, re.MULTILINE):
        lvl = len(h.group(1))
        start = h.end()
        pattern = r"^(#{1,%d})\s+" % lvl
        m = re.search(pattern, ctx.text[start:], re.MULTILINE)
        end = start + (m.start() if m else len(ctx.text) - start)
        section = ctx.text[start:end]
        m2 = re.search(r"(::@::|:@:|Flashcards for)", section)
        if m2:
            prefix = section[: m2.start()]
            if "---" not in prefix:
                hdr = h.group(0).strip()
                start = h.start()
                line, col, col_end = locate_range(ctx.text, start, len(h.group(0)))
                errors.append(
                    ValidationMessage(
                        rule_id="header_flashcard_separator",
                        msg=f"flashcards under header {hdr!r} should be preceded by a '---' separator",
                        line=line,
                        col=col,
                        col_end=col_end,
                    )
                )
    return errors


@RULE_REGISTRY.register()
def header_flashcard_sections_duplicate(
    ctx: ValidationContext,
) -> list[ValidationMessage]:
    """Disallow duplicate flashcard sections within a single header block.

    A header block should contain at most one flashcard section marker line:
    ``Flashcards for this section are as follows:``. If duplicates are found,
    authors should merge the sections and deduplicate overlapping cards.
    """
    errors: list[ValidationMessage] = []
    name = ctx.path.name.lower()
    parent_parts = [part.casefold() for part in ctx.path.parts[:-1]]
    if (
        name == "index.md"
        or name == "questions.md"
        or name == "agents.md"
        or "questions" in parent_parts
    ):
        return errors

    marker_re = re.compile(
        r"^\s*Flashcards for this section are as follows:\s*$",
        re.IGNORECASE | re.MULTILINE,
    )

    for h in re.finditer(r"^(#{1,})\s+(.+)$", ctx.text, re.MULTILINE):
        start = h.end()
        # For this rule, use the immediate next header (any level) so nested
        # subsections are validated independently.
        m = re.search(r"^#{1,6}\s+", ctx.text[start:], re.MULTILINE)
        end = start + (m.start() if m else len(ctx.text) - start)
        section = ctx.text[start:end]
        occurrences = list(marker_re.finditer(section))
        if len(occurrences) >= 2:
            dup = occurrences[1]
            abs_start = start + dup.start()
            line, col, col_end = locate_range(ctx.text, abs_start, len(dup.group(0)))
            hdr = h.group(0).strip()
            errors.append(
                ValidationMessage(
                    rule_id="header_flashcard_sections_duplicate",
                    msg=(
                        f"header {hdr!r} contains multiple flashcard section blocks; "
                        "merge duplicate flashcard sections into one '---' + "
                        "'Flashcards for this section are as follows:' block and "
                        "deduplicate cards when the flashcards overlap significantly, "
                        "instead of deleting an entire duplicate section"
                    ),
                    line=line,
                    col=col,
                    col_end=col_end,
                )
            )

    return errors


# flashcard calculation sanity -------------------------------------------------


@RULE_REGISTRY.register()
def two_sided_calc_warning(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when a two-sided card has LaTeX only on the right side.

    Many two-sided cards containing formulas or numerical results on the
    right-hand side require supporting data on the left so that the question
    is answerable (e.g. numbers, variable values, circuit parameters).  Agents
    often forget to duplicate that data before ``::@::`` and end up with
    prompts like ``term ::@:: $a+b=c$`` which are impossible to recall.  This
    rule scans lines with a single ``::@::`` separator; if the right portion
    contains any inline/block LaTeX but the left portion does not, a warning
    is emitted urging the author to add or copy the necessary data into the
    left side.  **Note:** for calculation-style cards the left-hand prompt may
    be arbitrarily long; including full equations or derivations is perfectly
    acceptable and encouraged.  The warning should not be interpreted as a
    hint to shorten the prompt – it flags missing information, not verbosity.
    Suppress the warning only when the card is purely conceptual and involves
    no calculation.
    """
    errors: list[ValidationMessage] = []
    for idx, line in enumerate(ctx.text.splitlines(), start=1):
        if "::@::" in line:
            # skip malformed cases with multiple separators
            if line.count("::@::") != 1:
                continue
            left, right = line.split("::@::", 1)

            # simple LaTeX detection: dollar signs or \( \[ delimiters
            def has_latex(s: str) -> bool:
                """Return True if *s* contains LaTeX-style delimiters or dollar signs."""
                return bool(re.search(r"\$|\\\(|\\\[", s))

            # warn when the answer side contains math but the prompt side has
            # no LaTeX.  Suppressions for purely conceptual cards are still
            # supported.
            if has_latex(right) and not has_latex(left):
                col = line.find("::@::") + 1
                col_end = len(line) + 1
                errors.append(
                    ValidationMessage(
                        rule_id="two_sided_calc_warning",
                        msg=(
                            "Right-hand side contains numeric or symbolic data but the left prompt "
                            "(before `::@::`) has none. Copy or repeat the necessary values/parameters "
                            "on the left so the card is answerable, and include any related "
                            "diagrams or images if needed for clarity, and include any related diagrams or "
                            "images from the original paragraph if they help provide context. These warnings "
                            "target example-style calculation cards, which should never be suppressed; if the word 'example' appears anywhere in the line, the check must fire. For example:\n"
                            R"before: - Ohm's law example ::@:: If $I = 2\,\text{A}, R = 5\,\Omega$, then by Ohm's law $V = IR = 10\,\text{V}$.\n"
                            R"after:  - Ohm's law example: Given $I = 2\,\text{A}$ and $R = 5\,\Omega$, calculate the voltage $V$ using Ohm's law. ::@:: If $I = 2\,\text{A}, R = 5\,\Omega$, then by Ohm's law $V = IR = 10\,\text{V}$. "
                            "Long prompts (even full derivations) are fine – the rule warns only "
                            "about missing context, not verbosity. To suppress for a purely "
                            "conceptual card use `<!-- check: ignore-line[two_sided_calc_warning]: conceptual -->` (do not apply to example cards)."
                        ),
                        severity=Severity.WARNING,
                        line=idx,
                        col=col,
                        col_end=col_end,
                    )
                )
    return errors


@RULE_REGISTRY.register()
def one_sided_calc_warning(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when a one-sided card has LaTeX on the answer side only.

    Similar to :func:`two_sided_calc_warning`, but handles ``:@:`` cards which
    only have a prompt on the left and an answer on the right.  If the right
    side contains math while the left side has none, the card likely omits
    necessary numerical data or associated diagrams; urge the author to include
    or duplicate that data (or relevant image) in the prompt.  **For
    calculation cards the left prompt may be arbitrarily long; write out the
    full equation or value list – the warning is about missing answerable
    context, not about keeping the prompt short.**
    Suppress only for purely conceptual flashcards.
    """
    errors: list[ValidationMessage] = []
    for idx, line in enumerate(ctx.text.splitlines(), start=1):
        if ":@:" in line:
            # ignore any line that also contains a two-sided separator
            if "::@::" in line:
                continue
            # earlier versions skipped lines with multiple ":@:" separators,
            # but tests rely on parsing the first occurrence. drop the guard and
            # split at the first separator instead.
            # (two-sided separators are already handled above.)
            left, right = line.split(":@:", 1)

            def has_latex(s: str) -> bool:
                """Return True if *s* contains LaTeX-style delimiters or dollar signs."""
                return bool(re.search(r"\$|\\\(|\\\[", s))

            if has_latex(right) and not has_latex(left):
                col = line.find(":@:") + 1
                col_end = len(line) + 1
                errors.append(
                    ValidationMessage(
                        rule_id="one_sided_calc_warning",
                        msg=(
                            "Right-hand side has numeric or symbolic data but the prompt before `:@:` is blank. "
                            "Include or duplicate the needed values in the left prompt. These warnings target example cards and must not be suppressed. For example:\n"
                            R"before: - Ohm's law example :@: If $I = 2\,\text{A}, R = 5\,\Omega$, then by Ohm's law $V = IR = 10\,\text{V}$.\n"
                            R"after:  - Ohm's law example: Given $I = 2\,\text{A}$ and $R = 5\,\Omega$, calculate the voltage $V$ using Ohm's law. :@: If $I = 2\,\text{A}, R = 5\,\Omega$, then by Ohm's law $V = IR = 10\,\text{V}$. "
                            "Long equations are allowed; this check simply ensures answerable context. "
                            "For conceptual-only cards suppress with `<!-- check: ignore-line[one_sided_calc_warning]: conceptual -->` (not for example cards)."
                        ),
                        severity=Severity.WARNING,
                        line=idx,
                        col=col,
                        col_end=col_end,
                    )
                )
    return errors


# math and unit rules --------------------------------------------------------


@RULE_REGISTRY.register()
def unit_outside_math(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when units appear immediately after math without delimiters.

    After a dollar‑delimited math expression that ends in a number, a
    measurement unit such as ``V`` or ``Hz`` should itself be wrapped in
    ``$…$``.  This rule scans for such patterns and reports the first
    occurrence it finds.  It is conservative: it only triggers when the math
    expression ends in a digit, reducing false positives (e.g. the letter
    ``A`` used as an article).
    """
    errors: list[ValidationMessage] = []
    text = ctx.text

    # walk through every math-delimited span and inspect following text
    math_re = re.compile(r"(\$\$?.*?\$\$?)", re.DOTALL)
    unit_pat = re.compile(r"^(?:V|A|Ω|W|mW|kΩ|C|Hz)\b")

    for mblock in math_re.finditer(text):
        # only flag units when the math expression ends in a numeric value;
        # otherwise the following 'A' is more likely an English article.
        inner = mblock.group(1)
        # strip delimiters ($ or $$) and trailing whitespace
        inner_content = inner.strip("$ ").rstrip()
        if not re.search(r"\d$", inner_content):
            continue

        end_idx = mblock.end()
        idx = end_idx
        # skip whitespace
        while idx < len(text) and text[idx].isspace():
            idx += 1
        # optional numeric prefix
        num = re.match(r"\d+(?:\.\d+)?", text[idx:])
        if num:
            idx += num.end()
            while idx < len(text) and text[idx].isspace():
                idx += 1
        mu = unit_pat.match(text[idx:])
        if mu:
            start_pos = idx + mu.start()
            length = mu.end() - mu.start()
            line, col, col_end = locate_range(text, start_pos, length)
            errors.append(
                ValidationMessage(
                    rule_id="unit_outside_math",
                    msg="found a unit (e.g. V, A, Ω, W, mW, kΩ, C, Hz) outside math delimiters; enclose units in $...$",
                    line=line,
                    col=col,
                    col_end=col_end,
                )
            )
            break
    return errors


# additional rules ---------------------------------------------------------


@RULE_REGISTRY.register()
def numeric_text_not_latex(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when numeric expressions appear as plain text instead of math.

    Course notes frequently include examples such as ``5 V``, ``50\u03a9+75\u03a9``
    or ``I2=0.04 A`` that are meant to be read as mathematical quantities.
    These should normally be wrapped in dollar delimiters so that LaTeX
    rendering, spacing and unit formatting work correctly.  Authors sometimes
    forget and type the values as ordinary prose; this rule scans each line
    that does **not** contain any dollar sign and looks for two common
    patterns:

    1. A number followed by a unit such as ``V``, ``A``, ``\u03a9``, ``Hz``,
       ``W`` etc.  The rule is intentionally conservative for a bare trailing
       ``C``: it requires whitespace before ``C`` so room codes such as
       ``4225C`` are not mistaken for charges or temperatures.
    2. A simple variable assignment like ``I2=0.04`` where a letter and
       digit are followed by an equals sign (the right-hand side may itself
       include units).

    Lines inside fenced code blocks are ignored entirely. Markdown link
    targets, inline code, and HTML comments are also masked before matching so
    percent-encoded anchors such as ``%2C`` do not produce false positives.
    """
    errors: list[ValidationMessage] = []

    unit_re = re.compile(
        r"""
        \b
        \d+(?:\.\d+)?
        (?:
            \s+(?:V|A|Ω|Ohm|Hz|W|mW|kΩ|mV|kV|mA|kA|C)
            |
            (?:V|A|Ω|Ohm|Hz|W|mW|kΩ|mV|kV|mA|kA)
        )
        \b
        """,
        re.VERBOSE,
    )
    var_eq_re = re.compile(r"\b[IiRrVv]\d+\s*=\s*\d")

    def _mask_match(match: re.Match[str]) -> str:
        """Replace a matched span with spaces to preserve column positions."""

        return " " * len(match.group(0))

    def _mask_link_target(match: re.Match[str]) -> str:
        """Mask only the target portion of a Markdown link, not its label."""

        full = match.group(0)
        target = match.group(1)
        return full.replace(target, " " * len(target), 1)

    in_fence = False
    for idx, line in enumerate(ctx.text.splitlines(keepends=True), start=1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        stripped = line.rstrip("\n")
        if "$" in stripped:
            continue

        masked = re.sub(r"<!--.*?-->", _mask_match, stripped)
        masked = re.sub(r"`[^`]*`", _mask_match, masked)
        masked = re.sub(r"\[[^\]]*\]\(([^)]+)\)", _mask_link_target, masked)

        if unit_re.search(masked) or var_eq_re.search(masked):
            m = unit_re.search(masked) or var_eq_re.search(masked)
            assert m is not None
            col = m.start() + 1
            col_end = m.end() + 1
            errors.append(
                ValidationMessage(
                    rule_id="numeric_text_not_latex",
                    msg=(
                        "numeric expression detected outside math delimiters; "
                        "wrap quantities such as 5\u202fV or I2=0.04\u202fA in `$…$` "
                        "so they render correctly and obey spacing rules"
                    ),
                    severity=Severity.WARNING,
                    line=idx,
                    col=col,
                    col_end=col_end,
                )
            )
    return errors


# additional rules ---------------------------------------------------------


@RULE_REGISTRY.register()
def math_in_code_fence(ctx: ValidationContext) -> list[ValidationMessage]:
    """Flag LaTeX-style math found inside fenced code blocks.

    Authors should not include dollar signs within code fences; this rule
    warns on the first occurrence.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text
    for mblock in re.finditer(r"```.*?```", text, re.DOTALL):
        block = mblock.group(0)
        if "$" in block:
            rel = block.find("$")
            abs_idx = mblock.start() + rel
            line, col = locate(text, abs_idx)
            errors.append(
                ValidationMessage(
                    rule_id="math_in_code_fence",
                    msg="math expression found inside a code fence; use inline or display math instead",
                    line=line,
                    col=col,
                )
            )
            break
    return errors


@RULE_REGISTRY.register()
def latex_disallowed_delimiters(ctx: ValidationContext) -> list[ValidationMessage]:
    r"""Disallow alternative LaTeX delimiters \[ \] or \( \) in favour of $.

    Search the text for the deprecated delimiters and flag their locations.
    """
    errors: list[ValidationMessage] = []
    # match the four deprecated delimiter sequences: \[, \], \(, or \)
    # the previous implementation also accidentally matched any ``\\`` which
    # is common in TeX macros (\Omega, line breaks, etc.) and produced
    # spurious warnings.  Restricting the pattern to the exact four sequences
    # resolves those false positives.
    m = re.search(r"\\\[|\\\]|\\\(|\\\)", ctx.text)
    if m:
        length = len(m.group(0))
        line, col, col_end = locate_range(ctx.text, m.start(), length)
        errors.append(
            ValidationMessage(
                rule_id="latex_disallowed_delimiters",
                msg="use dollar delimiters ($ or $$) instead of \\[ \\] or \\( \\)",
                line=line,
                col=col,
                col_end=col_end,
            )
        )
    return errors


@RULE_REGISTRY.register()
def latex_single_line(ctx: ValidationContext) -> list[ValidationMessage]:
    """Enforce that *inline* LaTeX expressions do not span multiple lines.

    The previous implementation also checked display math (``$$...$$``) which
    should instead be handled by a dedicated rule.  Here we match only single
    dollar delimiters and warn if the contents contain a literal newline
    character.  Block math is addressed by :func:`latex_block_no_newline`.

    Fenced code blocks are ignored entirely since their contents are not
    rendered as math.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text

    def in_code_fence(idx: int) -> bool:
        """Return True if byte offset *idx* is inside a fenced code block."""
        return text[:idx].count("```") % 2 == 1

    # match a single-dollar expression but not $$
    for m in re.finditer(r"(?<!\$)\$.*?\$(?!\$)", text, re.DOTALL):
        if in_code_fence(m.start()):
            continue
        if "\n" in m.group(0):
            length = len(m.group(0))
            line, col, col_end = locate_range(text, m.start(), length)
            errors.append(
                ValidationMessage(
                    rule_id="latex_single_line",
                    msg="inline LaTeX spans multiple lines; keep it on one line",
                    line=line,
                    col=col,
                    col_end=col_end,
                )
            )
    return errors


# new rules for LaTeX handling ------------------------------------------------


@RULE_REGISTRY.register()
def latex_environment_not_wrapped(ctx: ValidationContext) -> list[ValidationMessage]:
    """Detect LaTeX environments that are not enclosed in math delimiters.

    Authors often copy-paste multi-line equations using ``\\begin{align*}``
    (or other environments) directly into notes.  These blocks will not be
    processed as math unless wrapped in display delimiters like ``$$ ... $$``.
    This rule looks for a ``\\begin{...}``/``\\end{...}`` pair that spans
    multiple lines and emits a warning unless the ``\\begin`` line already
    contains a dollar sign (which usually indicates it is already wrapped).
    """
    errors: list[ValidationMessage] = []
    text = ctx.text
    # locate each \begin{env} and ensure a matching \end{env} later
    for m in re.finditer(r"^\\begin\{([^}]+)\}", text, re.MULTILINE):
        env = m.group(1)
        end_re = re.compile(r"^\\end\{" + re.escape(env) + r"\}", re.MULTILINE)
        m2 = end_re.search(text, m.end())
        if not m2:
            continue
        # if the begin line already contains a dollar sign it is probably
        # wrapped in $$ or inline math; skip in that case
        line_start = text.rfind("\n", 0, m.start()) + 1
        begin_line = text[line_start : text.find("\n", line_start)]
        if "$" in begin_line:
            continue
        # otherwise emit a warning pointing at the \begin keyword
        length = len(m.group(0))
        line, col, col_end = locate_range(text, m.start(), length)
        errors.append(
            ValidationMessage(
                rule_id="latex_environment_not_wrapped",
                msg="LaTeX environment found outside math delimiters; wrap in $$",
                line=line,
                col=col,
                col_end=col_end,
            )
        )
    return errors


@RULE_REGISTRY.register()
def latex_block_no_newline(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure block (``$$``) LaTeX expressions contain no literal newlines.

    Authors should not break the source across physical lines; use ``\\`` or
    ``\newline`` if an internal line break is required.  This rule is similar
    to :func:`latex_single_line` but applies only to ``$$`` delimited sections
    and provides a more specific message.
    """
    errors: list[ValidationMessage] = []
    for m in re.finditer(r"\$\$(.*?)\$\$", ctx.text, re.DOTALL):
        inner = m.group(1)
        if "\n" in inner:
            length = m.end() - m.start()
            line, col, col_end = locate_range(ctx.text, m.start(), length)
            errors.append(
                ValidationMessage(
                    rule_id="latex_block_no_newline",
                    msg="block LaTeX should not contain literal newline; use '\\\\' or '\\newline' instead",
                    line=line,
                    col=col,
                    col_end=col_end,
                )
            )
    return errors


@RULE_REGISTRY.register()
def latex_not_standalone(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when a LaTeX equation is the only content on its line.

    Authors are encouraged to embed equations within prose rather than
    leaving them as standalone lines.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text
    for m in re.finditer(r"\$\$?.*?\$\$?", text, re.DOTALL):
        start_idx = m.start()
        end_idx = m.end()
        line_start = text.rfind("\n", 0, start_idx) + 1
        line_end = text.find("\n", end_idx)
        if line_end == -1:
            line_end = len(text)
        line = text[line_start:line_end].strip()
        if line == m.group(0):
            length = end_idx - start_idx
            line_no, col_no, col_end = locate_range(ctx.text, start_idx, length)
            errors.append(
                ValidationMessage(
                    rule_id="latex_not_standalone",
                    msg="LaTeX equation should not occupy an entire line; embed it in prose",
                    line=line_no,
                    col=col_no,
                    col_end=col_end,
                )
            )
    return errors


@RULE_REGISTRY.register()
def latex_spacing_before(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when there is no space before an opening dollar math delimiter.

    This rule scans each LaTeX segment and checks the character immediately
    preceding the start; if it is not whitespace, an error is produced.

    Ignore any math that appears inside fenced code blocks.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text

    def in_code_fence(idx: int) -> bool:
        """Return True if byte offset *idx* is inside a fenced code block."""
        return text[:idx].count("```") % 2 == 1

    for m in re.finditer(r"\$\$?.*?\$\$?", text, re.DOTALL):
        if in_code_fence(m.start()):
            continue
        start_idx = m.start()
        if start_idx > 0:
            prev_char = text[start_idx - 1]
            # opening parenthesis or opening brace is acceptable
            # (common in e.g. "($x$" or "{@{ $x$"), so we treat it
            # as a non-error even though there is no space.
            if (
                prev_char not in " \n"
                and not prev_char.isspace()
                and prev_char not in punctuation
            ):
                line, col, col_end = locate_range(ctx.text, start_idx, 1)
                errors.append(
                    ValidationMessage(
                        rule_id="latex_spacing_before",
                        msg="no space before opening dollar sign; add a space when text comes before math",
                        line=line,
                        col=col,
                        col_end=col_end,
                    )
                )
    return errors


@RULE_REGISTRY.register()
def latex_spacing_after(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when there is no space after a closing dollar math delimiter.

    Similar to :func:`latex_spacing_before`, but checks the character immediately
    following each math expression.

    We skip any match that lies inside a fenced code block.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text

    def in_code_fence(idx: int) -> bool:
        """Return True if byte offset *idx* is inside a fenced code block."""
        return text[:idx].count("```") % 2 == 1

    for m in re.finditer(r"\$\$?.*?\$\$?", text, re.DOTALL):
        if in_code_fence(m.start()):
            continue
        end_idx = m.end()
        if end_idx < len(text):
            next_char = text[end_idx]
            if (
                next_char not in " \n"
                and not next_char.isspace()
                and next_char not in punctuation
                and next_char != "}"
            ):
                line, col, col_end = locate_range(ctx.text, end_idx, 1)
                errors.append(
                    ValidationMessage(
                        rule_id="latex_spacing_after",
                        msg="no space after closing dollar sign; add a space when text follows math",
                        line=line,
                        col=col,
                        col_end=col_end,
                    )
                )
    return errors


@RULE_REGISTRY.register()
def link_unencoded_space(ctx: ValidationContext) -> list[ValidationMessage]:
    """Detect markdown links whose target contains a raw space character.

    Authors should use ``%20`` encoding in link URLs; this rule reports
    the first offending link it finds.
    """
    errors: list[ValidationMessage] = []
    m = re.search(r"\[[^\]]+\]\([^\) ]+ [^\)]+\)", ctx.text)
    if m:
        length = len(m.group(0))
        line, col, col_end = locate_range(ctx.text, m.start(), length)
        errors.append(
            ValidationMessage(
                rule_id="link_unencoded_space",
                msg="link target contains unencoded space; use %20 encoding",
                line=line,
                col=col,
                col_end=col_end,
            )
        )
    return errors


# new rule to prohibit lecture summary sections ---------------------------------------------


@RULE_REGISTRY.register()
def no_lecture_summary(ctx: ValidationContext) -> list[ValidationMessage]:
    """Error if a "lecture summary" section or list item appears.

    Occasionally course notes imported or edited manually include a
    "lecture summary" heading or bullet.  These summaries duplicate the
    actual session content and are not allowed; authors should merge any
    high-level comments back into the regular lecture entry.  The rule
    scans for any level-2-or-deeper header whose text begins with
    ``lecture summary`` (case-insensitive) or a bullet list item whose
    text starts the same way.  An error is emitted pointing at the
    offending line so it can be removed.

    Summary‑sentence flashcards (cards whose gloss begins with the word
    "summary") are also discouraged; they provide little learning value
    and should be rephrased as ordinary content or deleted.  The test
    suite ensures the rule catches both forms.
    """
    errors: list[ValidationMessage] = []
    # match "## lecture summary" or deeper, or "- lecture summary" list
    pattern = re.compile(
        r"^(?:#{2,}\s*lecture summary|-\s*lecture summary)",
        re.IGNORECASE | re.MULTILINE,
    )
    for m in pattern.finditer(ctx.text):
        line, col, col_end = locate_range(ctx.text, m.start(), len(m.group(0)))
        errors.append(
            ValidationMessage(
                "no_lecture_summary",
                "lecture summary sections are not allowed; remove or merge into main notes",
                line=line,
                col=col,
                col_end=col_end,
            )
        )
    # also detect summary-sentence flashcards
    for m in re.finditer(
        r"^-\s*summary sentence\b", ctx.text, re.IGNORECASE | re.MULTILINE
    ):
        line, col, col_end = locate_range(ctx.text, m.start(), len(m.group(0)))
        errors.append(
            ValidationMessage(
                "no_lecture_summary",
                "summary-sentence flashcards are not allowed; rephrase or remove",
                line=line,
                col=col,
                col_end=col_end,
            )
        )
    return errors


# control character detection ------------------------------------------------


@RULE_REGISTRY.register()
def no_control_characters(ctx: ValidationContext) -> list[ValidationMessage]:
    """Error if the file contains invisible control characters.

    Control characters (U+0000–U+001F and U+007F) except for newline (\n),
    carriage return (\r) and tab (\t) are almost always introduced by copy-
    paste mistakes or encoding glitches.  They cause problems in Markdown and
    the flashcard generator, so we treat their presence as an error and point
    at the first offending character.
    """
    errors: list[ValidationMessage] = []
    # allow common whitespace control characters (LF, CR, TAB)
    # everything else in the C0 and DEL range is disallowed
    m = re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", ctx.text)
    if m:
        code = ord(m.group(0))
        hexcode = f"U+{code:04X}"
        line, col, col_end = locate_range(ctx.text, m.start(), 1)
        errors.append(
            ValidationMessage(
                rule_id="no_control_characters",
                msg=f"control character {hexcode} detected; remove or replace it",
                line=line,
                col=col,
                col_end=col_end,
            )
        )
    return errors


@RULE_REGISTRY.register()
def no_smart_double_quotes(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ban smart double quotes; require normal ASCII double quotes."""
    errors: list[ValidationMessage] = []
    for m in re.finditer(r"[\u201C\u201D]", ctx.text):
        line, col, col_end = locate_range(ctx.text, m.start(), 1)
        errors.append(
            ValidationMessage(
                rule_id="no_smart_double_quotes",
                msg='smart double quotes are not allowed; use normal ASCII double quotes (").',
                line=line,
                col=col,
                col_end=col_end,
            )
        )
    return errors


@RULE_REGISTRY.register()
def no_smart_single_quotes(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ban smart single quotes/apostrophes; require normal ASCII single quote."""
    errors: list[ValidationMessage] = []
    for m in re.finditer(r"[\u2018\u2019]", ctx.text):
        line, col, col_end = locate_range(ctx.text, m.start(), 1)
        errors.append(
            ValidationMessage(
                rule_id="no_smart_single_quotes",
                msg="smart single quotes are not allowed; use normal ASCII single quote (').",
                line=line,
                col=col,
                col_end=col_end,
            )
        )
    return errors


@RULE_REGISTRY.register()
def nested_list_path(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure nested list items include the full course path.

    When a lecture list is nested under its parent course, each item should
    include the course name (e.g. ``- ELEC 1100 / topic``).  This rule scans
    the body of the note and emits a warning for the first violation.
    """
    errors: list[ValidationMessage] = []
    body = ctx.body
    course = None
    offset = 0
    for line in body.splitlines(keepends=True):
        m2 = re.match(r"^\s*-\s+(.+?)\s*$", line)
        if m2:
            course = m2.group(1)
            break
        offset += len(line)
    seen_course = False
    offset = 0
    for line in body.splitlines(keepends=True):
        if not seen_course and course and line.strip().startswith(f"- {course}"):
            seen_course = True
            offset += len(line)
            continue
        if not seen_course:
            offset += len(line)
            continue
        if line.lstrip().startswith("## "):
            break
        if re.match(r"^ {2,}- ", line) and "/" not in line:
            line_no, col_no = locate(ctx.body, offset)
            errors.append(
                ValidationMessage(
                    rule_id="nested_list_path",
                    msg="nested list item does not include full path (e.g. 'ELEC 1100 / ...')",
                    line=line_no,
                    col=col_no,
                )
            )
            break
        offset += len(line)
    return errors


@RULE_REGISTRY.register()
def qa_hierarchical_path(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure nested QA glosses include the full hierarchical parent path.

    In any academic-notes file, each nested flashcard gloss (lines containing
    ``::@::`` or ``:@:``) should prefix its left-hand label with the complete
    parent path rather than relying on list indentation for context. For
    example:

    - ELEC 1100
      - ELEC 1100 / lab 1 preparation / breadboard and equipment
        - ELEC 1100 / lab 1 preparation / breadboard and equipment / lab equipment overview ::@: ...

    This rule walks the body list structure, tracking non-QA bullets as parent
    paths.  When it encounters an indented QA line, it locates the nearest
    less-indented parent and requires the QA's left-hand label to start with
    ``<parent> /``.  Only the first violation is reported.
    """
    errors: list[ValidationMessage] = []
    body = ctx.body
    lines = body.splitlines(keepends=True)
    # stack holds (indent_width, label_text) for non-QA bullets
    stack: list[tuple[int, str]] = []
    offset = 0

    for line in lines:
        m = re.match(r"^(?P<indent>\s*)-\s+(?P<rest>.+)$", line)
        if not m:
            offset += len(line)
            continue

        indent = len(m.group("indent"))
        rest = m.group("rest").rstrip()
        is_qa = "::@::" in rest or ":@:" in rest

        if is_qa:
            # determine left-hand gloss label
            sep_idx = rest.find("::@::")
            if sep_idx == -1:
                sep_idx = rest.find(":@:")
            if sep_idx == -1:
                offset += len(line)
                continue
            label_left = rest[:sep_idx].rstrip()
            # skip section-link style cards (e.g. '[§ section](...)') which use
            # a different, anchor-based hierarchy rather than course-path
            # prefixes.  The hierarchical-path requirement only applies to
            # course-path glosses like 'ELEC 1100 / topic / ...'.
            if label_left.lstrip().startswith("[§"):
                offset += len(line)
                continue
            # ignore cards that do not use path-style labels at all
            if "/" not in label_left:
                offset += len(line)
                continue

            # find nearest less-indented parent bullet
            parent_label: str | None = None
            for p_indent, p_label in reversed(stack):
                if p_indent < indent:
                    parent_label = p_label.strip()
                    break

            if parent_label and "/" in parent_label:
                expected_prefix = f"{parent_label} /"
                if not label_left.startswith(expected_prefix):
                    line_no, col_no = locate(ctx.body, offset)
                    errors.append(
                        ValidationMessage(
                            rule_id="qa_hierarchical_path",
                            msg=(
                                "nested QA gloss does not start with its parent path; "
                                f"expected prefix '{expected_prefix}' but found '{label_left}'"
                            ),
                            line=line_no,
                            col=col_no,
                        )
                    )
                    break
        else:
            # plain bullet defines or updates the current parent stack
            label = rest
            # only treat plain course-path bullets (no markdown links) as
            # hierarchical parents; other bullets (e.g. section links or
            # descriptive labels) should not affect the path stack
            while stack and stack[-1][0] >= indent:
                stack.pop()
            if "/" in label and "[" not in label:
                stack.append((indent, label))

        offset += len(line)

    return errors


@RULE_REGISTRY.register()
def qa_nested_indentation(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure nested flashcard bullets use consistent two-space indentation.

    Nested flashcard structures in academic notes should indent by exactly two
    spaces per level. This applies to both grouping bullets and nested QA
    bullets, so a child bullet should be indented exactly two spaces more than
    its nearest less-indented parent.
    """

    errors: list[ValidationMessage] = []
    lines = ctx.body.splitlines(keepends=True)
    offset = 0
    in_flashcards = False
    indent_stack: list[int] = []

    for line in lines:
        stripped = line.strip()

        if stripped == "Flashcards for this section are as follows:":
            in_flashcards = True
            indent_stack = []
            offset += len(line)
            continue

        if in_flashcards and line.lstrip().startswith("##"):
            in_flashcards = False
            indent_stack = []

        if not in_flashcards:
            offset += len(line)
            continue

        m = re.match(r"^(?P<indent>\s*)-\s+(?P<rest>.+)$", line)
        if not m:
            offset += len(line)
            continue

        indent = len(m.group("indent"))

        if indent % 2 != 0:
            line_no, col_no = locate(ctx.body, offset)
            errors.append(
                ValidationMessage(
                    rule_id="qa_nested_indentation",
                    msg="flashcard bullets must use multiples of two spaces for indentation",
                    line=line_no,
                    col=col_no,
                )
            )
            break

        while indent_stack and indent_stack[-1] >= indent:
            indent_stack.pop()

        if indent > 0:
            parent_indent = indent_stack[-1] if indent_stack else None
            if parent_indent is None or indent != parent_indent + 2:
                line_no, col_no = locate(ctx.body, offset)
                errors.append(
                    ValidationMessage(
                        rule_id="qa_nested_indentation",
                        msg="nested flashcard bullets must be indented exactly two spaces deeper than their parent",
                        line=line_no,
                        col=col_no,
                    )
                )
                break

        indent_stack.append(indent)
        offset += len(line)

    return errors


@RULE_REGISTRY.register()
def topic_note_redundant_filename_prefix(
    ctx: ValidationContext,
) -> list[ValidationMessage]:
    """Disallow repeating the topic-note filename or title in prompts.

    In topic-specific notes, the flashcard viewer already shows the filename,
    and the page itself already shows the title, so prompts such as
    ``probability measure / definition``, ``# probability measure`` echoed as
    ``probability measure``, or ``discrete distributions / Poisson approximation
    / statement`` are redundant. Top-level prompts should use only local labels
    (for example ``definition``), while nested prompts should use only the
    in-file parent path (for example ``Poisson approximation / statement``).
    """

    errors: list[ValidationMessage] = []
    name = ctx.path.name.lower()
    parent_parts = [part.casefold() for part in ctx.path.parts[:-1]]
    if name in {"index.md", "questions.md"} or "questions" in parent_parts:
        return errors

    stem = ctx.path.stem
    title_match = re.search(r"^#\s+(.+)$", ctx.text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""
    stem_lower = stem.casefold()
    title_lower = title.casefold()
    body_start = len(ctx.text) - len(ctx.body)
    lines = ctx.body.splitlines(keepends=True)
    offset = 0
    in_flashcards = False

    for line in lines:
        stripped = line.strip()

        if stripped == "Flashcards for this section are as follows:":
            in_flashcards = True
            offset += len(line)
            continue

        if in_flashcards and line.lstrip().startswith("#"):
            in_flashcards = False

        if not in_flashcards:
            offset += len(line)
            continue

        m = re.match(r"^(?P<indent>\s*)-\s+(?P<rest>.+)$", line)
        if not m:
            offset += len(line)
            continue

        rest = m.group("rest").rstrip()
        label = rest
        sep_idx = rest.find("::@::")
        if sep_idx == -1:
            sep_idx = rest.find(":@:")
        if sep_idx != -1:
            label = rest[:sep_idx].rstrip()

        label_lower = label.casefold()

        stem_redundant = label_lower == stem_lower or label_lower.startswith(
            f"{stem_lower} /"
        )
        title_redundant = bool(title_lower) and (
            label_lower == title_lower or label_lower.startswith(f"{title_lower} /")
        )

        if stem_redundant or title_redundant:
            repeated = title if title_redundant and title else stem
            line_no, col_no = locate(ctx.text, body_start + offset)
            errors.append(
                ValidationMessage(
                    rule_id="topic_note_redundant_filename_prefix",
                    msg=(
                        f"flashcard prompt redundantly repeats the topic-note filename or title '{repeated}'; "
                        "omit it because the flashcard viewer already shows the file name and the note already shows its title"
                    ),
                    line=line_no,
                    col=col_no,
                )
            )
            break

        offset += len(line)

    return errors


@RULE_REGISTRY.register()
def qa_missing_separator(ctx: ValidationContext) -> list[ValidationMessage]:
    """Check for QA-style flashcard lists without a preceding separator phrase.

    Lines beginning with ``- ...::@::`` or ``- ...:@:`` should be
    preceded by ``Flashcards for`` or a ``---`` separator.  If not, an
    error is returned.
    """
    errors: list[ValidationMessage] = []
    lines = ctx.text.splitlines()
    fm = FRONT_RE.match(ctx.text)
    if fm:
        fm_lines = fm.group(0).splitlines()
        lines = lines[len(fm_lines) :]
    offset = ctx.text.find("\n") + 1 if fm else 0
    for i, line in enumerate(lines):
        if re.match(r"^[ \t]{0,1}-\s+([^/]*?)::@::", line) or re.match(
            r"^[ \t]{0,1}-\s+([^/]*?):@:", line
        ):
            line_start = ctx.text.find(line, offset)
            j = i - 1
            prev = None
            while j >= 0:
                if lines[j].strip():
                    prev = lines[j].strip()
                    break
                j -= 1
            prev_line = prev or ""
            lower_prev = prev_line.lower()
            if not (
                lower_prev.startswith("flashcards for") or prev_line.startswith("---")
            ):
                line_no, col_no = locate(
                    ctx.text, line_start if line_start != -1 else 0
                )
                span = len(line)
                _, _, col_end = locate_range(
                    ctx.text, line_start if line_start != -1 else 0, span
                )
                errors.append(
                    ValidationMessage(
                        rule_id="qa_missing_separator",
                        msg="QA-style flashcard list detected without preceding separator phrase",
                        line=line_no,
                        col=col_no,
                        col_end=col_end,
                    )
                )
            break
    return errors


@RULE_REGISTRY.register()
def qa_multiple_separators(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when a single line contains more than one flashcard separator.

    Only one ``::@::`` or ``:@:`` is permitted per line; multiple separators
    often indicate a formatting mistake.
    """
    errors: list[ValidationMessage] = []
    lines = ctx.text.splitlines()
    fm = FRONT_RE.match(ctx.text)
    if fm:
        lines = lines[len(fm.group(0).splitlines()) :]
    offset = ctx.text.find("\n") + 1 if fm else 0
    for line in lines:
        if line.count("::@::") > 1 or line.count(":@:") > 1:
            line_start = ctx.text.find(line, offset)
            line_no, col_no = locate(ctx.text, line_start if line_start != -1 else 0)
            span = len(line)
            _, _, col_end = locate_range(
                ctx.text, line_start if line_start != -1 else 0, span
            )
            errors.append(
                ValidationMessage(
                    rule_id="qa_multiple_separators",
                    msg="line contains multiple flashcard separators (::@:: or :@:); use only one per card",
                    line=line_no,
                    col=col_no,
                    col_end=col_end,
                )
            )
            break
    return errors


def _scan_cloze_tokens(
    text: str,
) -> tuple[
    list[tuple[str, int]],
    list[tuple[int, int]],
    list[int],
    list[int],
    list[int],
]:
    """Scan cloze tokens and return token stream with structural diagnostics.

    Returns:
      - tokens: list of ("open"|"close", absolute_index)
      - spans: matched cloze spans as (open_index, close_index)
      - unmatched_open: opening token indices left unclosed
      - unmatched_close: closing token indices without opening
      - nested_open: opening token indices encountered while already inside a cloze
    """
    tokens: list[tuple[str, int]] = []
    spans: list[tuple[int, int]] = []
    stack: list[int] = []
    unmatched_close: list[int] = []
    nested_open: list[int] = []

    i = 0
    n = len(text)
    while i < n:
        if text.startswith("{@{", i):
            if stack:
                nested_open.append(i)
            stack.append(i)
            tokens.append(("open", i))
            i += 3
            continue
        if text.startswith("}@}", i):
            tokens.append(("close", i))
            if stack:
                spans.append((stack.pop(), i))
            else:
                unmatched_close.append(i)
            i += 3
            continue
        i += 1

    unmatched_open = stack.copy()
    return tokens, spans, unmatched_open, unmatched_close, nested_open


@RULE_REGISTRY.register()
def cloze_open_close_matching(ctx: ValidationContext) -> list[ValidationMessage]:
    """Check that cloze openings '{@{' and closings '}@}' match in order/count."""
    errors: list[ValidationMessage] = []
    _, _, unmatched_open, unmatched_close, _ = _scan_cloze_tokens(ctx.text)

    for idx in unmatched_open:
        line_no, col_no = locate(ctx.text, idx)
        _, _, col_end = locate_range(ctx.text, idx, 3)
        errors.append(
            ValidationMessage(
                rule_id="cloze_open_close_matching",
                msg="unmatched cloze opening '{@{' (missing matching '}@}').",
                line=line_no,
                col=col_no,
                col_end=col_end,
            )
        )

    for idx in unmatched_close:
        line_no, col_no = locate(ctx.text, idx)
        _, _, col_end = locate_range(ctx.text, idx, 3)
        errors.append(
            ValidationMessage(
                rule_id="cloze_open_close_matching",
                msg="unmatched cloze closing '}@}' (no preceding '{@{').",
                line=line_no,
                col=col_no,
                col_end=col_end,
            )
        )

    return errors


@RULE_REGISTRY.register()
def cloze_wrong_closing_token(ctx: ValidationContext) -> list[ValidationMessage]:
    """Check for wrong cloze close token '}}' where '}@}' is required."""
    errors: list[ValidationMessage] = []
    text = ctx.text

    depth = 0
    i = 0
    n = len(text)
    while i < n:
        if text.startswith("{@{", i):
            depth += 1
            i += 3
            continue
        if text.startswith("}@}", i):
            depth = max(depth - 1, 0)
            i += 3
            continue

        if depth > 0 and text.startswith("}}", i):
            next_char = text[i + 2] if i + 2 < n else ""
            # Only flag when it looks like a cloze terminator typo, not generic
            # LaTeX brace nesting inside the cloze body.
            if next_char == "" or next_char.isspace() or next_char in ".,;:!?)]":
                line_no, col_no = locate(text, i)
                _, _, col_end = locate_range(text, i, 2)
                errors.append(
                    ValidationMessage(
                        rule_id="cloze_wrong_closing_token",
                        msg="wrong cloze closing token '}}' found; use '}@}' instead.",
                        line=line_no,
                        col=col_no,
                        col_end=col_end,
                    )
                )
            i += 2
            continue
        i += 1

    return errors


@RULE_REGISTRY.register()
def cloze_single_line(ctx: ValidationContext) -> list[ValidationMessage]:
    """Check cloze text does not span newline in markdown source."""
    errors: list[ValidationMessage] = []
    _, spans, _, _, _ = _scan_cloze_tokens(ctx.text)

    for start, end in spans:
        inner = ctx.text[start + 3 : end]
        if "\n" in inner:
            line_no, col_no = locate(ctx.text, start)
            _, _, col_end = locate_range(ctx.text, start, (end + 3) - start)
            errors.append(
                ValidationMessage(
                    rule_id="cloze_single_line",
                    msg="cloze content must be on one source line; multiline clozes are not recognized.",
                    line=line_no,
                    col=col_no,
                    col_end=col_end,
                )
            )

    return errors


@RULE_REGISTRY.register()
def cloze_no_nested(ctx: ValidationContext) -> list[ValidationMessage]:
    """Check nested clozes are not used."""
    errors: list[ValidationMessage] = []
    _, _, _, _, nested_open = _scan_cloze_tokens(ctx.text)

    for idx in nested_open:
        line_no, col_no = locate(ctx.text, idx)
        _, _, col_end = locate_range(ctx.text, idx, 3)
        errors.append(
            ValidationMessage(
                rule_id="cloze_no_nested",
                msg="nested cloze detected; fix other cloze matching problems first, since this can be caused by mismatched cloze delimiters.",
                line=line_no,
                col=col_no,
                col_end=col_end,
            )
        )

    return errors


# split the original check into two specific rules; retain a wrapper
# for backward compatibility.


@RULE_REGISTRY.register()
def no_consecutive_source_newlines(ctx: ValidationContext) -> list[ValidationMessage]:
    """Flag consecutive source newlines in markdown text.

    This rule enforces that markdown source should not contain runs of
    three or more consecutive newline tokens. It checks *actual*
    newline characters and does not treat HTML line breaks such as ``<br/>``
    as newlines.

    Trailing whitespace is stripped from each source line before evaluating
    blank-line runs so lines like ``"   \n"`` behave like empty lines.

    To cover quoted content, lines that consist only of blockquote markers
    (``>``, ``>>``, ``> >`` etc.) are treated as blank for this rule.
    Mixed line endings (``\n``, ``\r\n``, and ``\r``) are handled explicitly.
    """

    errors: list[ValidationMessage] = []
    text = ctx.text

    line_start = 0
    newline_run = 0
    in_violation_run = False

    for raw_line in text.splitlines(keepends=True):
        if raw_line.endswith("\r\n"):
            line_content = raw_line[:-2]
            line_ending = "\r\n"
        elif raw_line.endswith("\n") or raw_line.endswith("\r"):
            line_content = raw_line[:-1]
            line_ending = raw_line[-1]
        else:
            line_content = raw_line
            line_ending = ""

        line_content = line_content.rstrip()
        stripped_quote = re.sub(r"^\s*(?:>\s*)+", "", line_content)
        is_effectively_blank = stripped_quote.strip() == ""

        if line_ending:
            if is_effectively_blank:
                newline_run += 1
            else:
                newline_run = 1
        else:
            newline_run = 0

        if newline_run >= 3:
            if not in_violation_run:
                line_no, col_no, col_end = locate_range(text, line_start, 1)
                errors.append(
                    ValidationMessage(
                        rule_id="no_consecutive_source_newlines",
                        msg=(
                            "three or more consecutive source newlines detected; "
                            "remove extra blank source lines (including quote-only blank lines) "
                            "and use <br/> if a visual line break is required"
                        ),
                        line=line_no,
                        col=col_no,
                        col_end=col_end,
                    )
                )
                in_violation_run = True
        else:
            in_violation_run = False

        line_start += len(raw_line)

    return errors


@RULE_REGISTRY.register()
def no_soft_wrap_paragraph(ctx: ValidationContext) -> list[ValidationMessage]:
    """Flag unescaped single newlines within paragraphs.

    Paragraphs should not be soft-wrapped.  List items are ignored here.
    Only **table rows** are exempt: after stripping any number of blockquote
    markers (e.g. ``>``, ``>>``, ``> > ``), if the line starts with ``|`` it is
    treated as a table row and skipped.  Blockquote content remains subject to
    the soft-wrap rule (e.g. ``> line one\\n> line two`` is still flagged).
    """
    errors: list[ValidationMessage] = []
    text = ctx.text
    fm = FRONT_RE.match(text)
    body_start = fm.end() if fm else 0
    body = text[body_start:]

    def in_code_fence(idx: int) -> bool:
        """Return True if *idx* is within a fenced code block in *body*."""
        return body[:idx].count("```") % 2 == 1

    for m in re.finditer(r"\n(?!\n)", body):
        idx = m.start()
        if in_code_fence(idx):
            continue
        line_start = body.rfind("\n", 0, idx) + 1
        line = body[line_start:idx]
        if not line.strip():
            continue
        nxt_end = body.find("\n", idx + 1)
        next_line = body[idx + 1 : nxt_end if nxt_end != -1 else None]

        if line.endswith("\\") or line.endswith("  "):
            continue
        if any(tag in line.rstrip() for tag in ("<br/>", "<p>", "</p>")):
            continue
        if re.match(r"^\s*(#{1,6}|[-*+]\s|\d+\.\s)", next_line):
            continue
        if not next_line.strip():
            continue
        if line.strip().startswith("<!--"):
            continue
        if re.match(r"^\s*([-*+]|\d+\.)\s", line):
            continue

        # table rows only: strip multi-level blockquote prefix then check for |
        def after_quote(s: str) -> str:
            """Return *s* with any number of leading blockquote markers (e.g. >, >>, > >) removed."""
            return re.sub(r"^\s*(?:>\s*)+", "", s.strip())

        content = after_quote(line)
        next_content = after_quote(next_line)
        if not content or not next_content:
            continue  # line or next is only blockquote markers (treated as blank)
        if content.startswith("|") or next_content.startswith("|"):
            continue
        if re.match(r"^\s*(?:[-*+]\s|\d+\.\s)", content):
            continue
        if re.match(r"^\s*(?:[-*+]\s|\d+\.\s)", next_content):
            continue
        abs_idx = body_start + line_start
        line_no, col, col_end = locate_range(text, abs_idx, len(line))
        errors.append(
            ValidationMessage(
                rule_id="no_soft_wrap_paragraph",
                msg=(
                    "soft-wrapped paragraph detected — this is unacceptable; "
                    "remove the stray newline or insert a blank line/explicit break"
                ),
                line=line_no,
                col=col,
                col_end=col_end,
            )
        )
    return errors


@RULE_REGISTRY.register()
def no_soft_wrap_list(ctx: ValidationContext) -> list[ValidationMessage]:
    """Flag soft wraps inside list items."""
    errors: list[ValidationMessage] = []
    text = ctx.text
    fm = FRONT_RE.match(text)
    body_start = fm.end() if fm else 0
    body = text[body_start:]

    def in_code_fence(idx: int) -> bool:
        """Return True if *idx* is within a fenced code block in *body*."""
        return body[:idx].count("```") % 2 == 1

    for m in re.finditer(r"\n(?!\n)", body):
        idx = m.start()
        if in_code_fence(idx):
            continue
        line_start = body.rfind("\n", 0, idx) + 1
        line = body[line_start:idx]
        if not line.strip():
            continue
        nxt_end = body.find("\n", idx + 1)
        next_line = body[idx + 1 : nxt_end if nxt_end != -1 else None]

        if line.endswith("\\") or line.endswith("  "):
            continue
        if any(tag in line.rstrip() for tag in ("<br/>", "<p>", "</p>")):
            continue
        if re.match(r"^\s*(#{1,6}|[-*+]\s|\d+\.\s)", next_line):
            continue
        if not next_line.strip():
            continue
        if line.strip().startswith("<!--"):
            continue
        if re.match(r"^\s*([-*+]|\d+\.)\s", line):
            if re.match(r"^\s*([-*+]|\d+\.)\s", next_line):
                continue
            abs_idx = body_start + line_start
            line_no, col, col_end = locate_range(text, abs_idx, len(line))
            errors.append(
                ValidationMessage(
                    rule_id="no_soft_wrap_list",
                    msg="soft-wrapped list item detected; collapse it or use <br/>/<p> (sloppy formatting not permitted)",
                    line=line_no,
                    col=col,
                    col_end=col_end,
                )
            )
    return errors


@RULE_REGISTRY.register()
def week_monotonic(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure week numbers progress monotonically (with allowed reset to 1).

    Useful for detecting accidental misnumbering of session headings in notes.
    """
    errors: list[ValidationMessage] = []
    prev_week = None
    for week, _, hdr, idx in ctx.session_headers:
        num = int(week)
        if prev_week is not None and num < prev_week and num != 1:
            line, col, col_end = locate_range(ctx.text, idx, len(hdr))
            errors.append(
                ValidationMessage(
                    rule_id="week_monotonic",
                    msg="week numbers do not progress monotonically (unexpected reset)",
                    line=line,
                    col=col,
                    col_end=col_end,
                )
            )
            break
        prev_week = num
    return errors
