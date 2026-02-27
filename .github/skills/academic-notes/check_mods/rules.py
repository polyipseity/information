"""Validation rules for course notes.

This module contains a large collection of functions that enforce various
structural and content conventions for ``special/academia`` Markdown files.
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
from string import punctuation

from .models import ValidationContext, ValidationMessage
from .registry import RuleRegistry
from .utils import FRONT_RE, has_flash_tag, locate, locate_range

__all__ = ("RULE_REGISTRY",)

# single registry used by this module; external code may import and merge it
RULE_REGISTRY = RuleRegistry()

# metadata checks ------------------------------------------------------------


@RULE_REGISTRY.register(id="metadata_aliases_present")
def metadata_aliases_present(ctx: ValidationContext) -> list[ValidationMessage]:
    """Rule: file must include an 'aliases:' field in YAML frontmatter.

    Returns a list containing an error message if the tag is missing.
    """
    errors: list[ValidationMessage] = []
    if "aliases:" not in ctx.front:
        errors.append(ValidationMessage("no 'aliases:' in frontmatter"))
    return errors


@RULE_REGISTRY.register(id="metadata_tags_present")
def metadata_tags_present(ctx: ValidationContext) -> list[ValidationMessage]:
    """Rule: YAML frontmatter must contain a 'tags:' entry.

    Produces an error message if the tags field is absent.
    """
    errors: list[ValidationMessage] = []
    if "tags:" not in ctx.front:
        errors.append(ValidationMessage("no 'tags:' in frontmatter"))
    return errors


@RULE_REGISTRY.register(id="metadata_flash_tag")
def metadata_flash_tag(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure that the tags list includes a flashcard activation tag.

    Only checks when a tags section is present; emits an error if no flash tag
    is found.
    """
    errors: list[ValidationMessage] = []
    if "tags:" in ctx.front and not has_flash_tag(ctx.front):
        errors.append(ValidationMessage("missing flashcard activation tag in 'tags:'"))
    return errors


@RULE_REGISTRY.register(id="aliases_sorted")
def aliases_sorted(ctx: ValidationContext) -> list[ValidationMessage]:
    """Check that the aliases list in frontmatter is sorted alphabetically.

    Comparison is case-insensitive; an error is returned if ordering differs.
    """
    errors: list[ValidationMessage] = []
    aliases = ctx.data.aliases
    if aliases != sorted(aliases, key=str.lower):
        errors.append(ValidationMessage("'aliases' list is not alphabetically sorted"))
    return errors


@RULE_REGISTRY.register(id="tag_language")
def tag_language(ctx: ValidationContext) -> list[ValidationMessage]:
    """Require a language tag of 'language/in/English' in the tags list.

    This ensures all notes are explicitly marked as English-language content.
    """
    errors: list[ValidationMessage] = []
    tags: list[str] = ctx.data.tags or []
    if "language/in/English" not in tags:
        errors.append(ValidationMessage("missing 'language/in/English' tag"))
    return errors


@RULE_REGISTRY.register(id="tag_index_function")
def tag_index_function(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure that index.md files include the 'function/index' tag.

    Only applies when the filename is literally 'index.md'.
    """
    errors: list[ValidationMessage] = []
    tags: list[str] = ctx.data.tags or []
    if ctx.path.name.lower() == "index.md" and "function/index" not in tags:
        errors.append(ValidationMessage("index page missing 'function/index' tag"))
    return errors


@RULE_REGISTRY.register(id="tag_path_flash")
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
            rel = "/".join(part.replace(" ", "_") for part in rel.split("/"))
            found = any(rel in t for t in tags)
            if not found:
                errors.append(
                    ValidationMessage(
                        "tags do not include flash tag matching file path"
                    )
                )
    return errors


# index structure -----------------------------------------------------------


@RULE_REGISTRY.register(id="index_heading_rule")
def index_heading_rule(ctx: ValidationContext) -> list[ValidationMessage]:
    """Check that an index.md contains a top-level '# index' heading.

    Only applicable to files named 'index.md'.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() == "index.md":
        if "# index" not in ctx.text:
            errors.append(ValidationMessage("index.md missing '# index' heading"))
    return errors


@RULE_REGISTRY.register(id="index_children_rule")
def index_children_rule(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure index.md includes a 'children' section or heading.

    Looks for either '## children' or a literal 'children:' string.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() == "index.md":
        if "## children" not in ctx.text and "children:" not in ctx.text:
            errors.append(ValidationMessage("index missing 'children' section"))
    return errors


@RULE_REGISTRY.register(id="index_semester_order_rule")
def index_semester_order_rule(ctx: ValidationContext) -> list[ValidationMessage]:
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
            errors.append(ValidationMessage(msg, line_no, col_no))
            break
    return errors


# session-related -----------------------------------------------------------


@RULE_REGISTRY.register(id="session_duplicate_heading")
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
                    f"duplicate session heading {hdr!r} (week {week} {typ})",
                    line,
                    col,
                    col_end,
                )
            )
        seen_pairs[pair] = idx
    return errors


@RULE_REGISTRY.register(id="session_datetime_order")
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
                        f"session {hdr!r} has datetime {dt} not after previous session",
                        line,
                        col,
                        col_end,
                    )
                )
            last_datetime = dt
    return errors


@RULE_REGISTRY.register(id="session_topic_presence")
def session_topic_presence(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure sessions with datetimes also have a topic (unless unscheduled).

    - If status is 'unscheduled' and topic exists, that's flagged as an error.
    - Otherwise, missing topic when a datetime is present is an error.
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
                            f"session {hdr!r} has status unscheduled but also a topic",
                            line,
                            col,
                            col_end,
                        )
                    )
            else:
                if "topic:" not in section:
                    line, col, col_end = locate_range(ctx.text, idx, len(hdr))
                    errors.append(
                        ValidationMessage(
                            f"session {hdr!r} has a datetime but no topic field",
                            line,
                            col,
                            col_end,
                        )
                    )
    return errors


@RULE_REGISTRY.register(id="session_venue_presence")
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
                    f"session {hdr!r} has a datetime but no venue",
                    line,
                    col,
                    col_end,
                )
            )
    return errors


@RULE_REGISTRY.register(id="session_next_lecture_remark")
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
                    f"session {hdr!r} contains a 'next lecture/next week' remark; remove unless major grading event",
                    line,
                    col,
                    col_end,
                )
            )
    return errors


@RULE_REGISTRY.register(id="session_exam_order")
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
                        "exam section appears before some lecture/lab/tutorial entries — exams should be placed after other sessions",
                        line,
                        col,
                    )
                )
                break
    return errors


# header and flashcard style --------------------------------------------------


@RULE_REGISTRY.register(id="header_style_rule")
def header_style_rule(ctx: ValidationContext) -> list[ValidationMessage]:
    """Enforce that non-index headers start with a lowercase letter.

    Scans all headers of level 2 or deeper and flags those whose first
    non-space character is uppercase or non-alphanumeric.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() == "index.md":
        return errors
    for h in re.finditer(r"^(#{2,})\s+(.+)$", ctx.text, re.MULTILINE):
        hdr_text = h.group(2)
        if hdr_text and not hdr_text[0].islower() and not hdr_text[0].isdigit():
            start = h.start()
            hdr_text = h.group(0)
            line, col, col_end = locate_range(ctx.text, start, len(hdr_text))
            errors.append(
                ValidationMessage(
                    f"header {hdr_text.strip()!r} should start with lowercase",
                    line,
                    col,
                    col_end,
                )
            )
    return errors


@RULE_REGISTRY.register(id="header_flashcard_presence")
def header_flashcard_presence(ctx: ValidationContext) -> list[ValidationMessage]:
    """Require that each non-index header contains flashcard markers.

    Searches the text between the header and the next header at the same or
    higher level; if no flashcard syntax is found, an error is returned.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() == "index.md":
        return errors
    for h in re.finditer(r"^(#{2,})\s+(.+)$", ctx.text, re.MULTILINE):
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
                    f"header {hdr!r} has no flashcard markers in its section",
                    line,
                    col,
                    col_end,
                )
            )
    return errors


@RULE_REGISTRY.register(id="header_flashcard_separator")
def header_flashcard_separator(ctx: ValidationContext) -> list[ValidationMessage]:
    """Enforce a '---' separator before flashcard markers under headers.

    When flashcards appear in a section, there should be a horizontal rule
    separating them from preceding text.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() == "index.md":
        return errors
    for h in re.finditer(r"^(#{2,})\s+(.+)$", ctx.text, re.MULTILINE):
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
                        f"flashcards under header {hdr!r} should be preceded by a '---' separator",
                        line,
                        col,
                        col_end,
                    )
                )
    return errors


# math and unit rules --------------------------------------------------------


@RULE_REGISTRY.register(id="unit_outside_math")
def unit_outside_math(ctx: ValidationContext) -> list[ValidationMessage]:
    """Detect numeric units appearing outside of LaTeX math delimiters.

    Splits the document into math and non-math segments, then searches the
    non-math portions for common electrical/physical units. The first match
    generates an error advising to wrap the unit in ``$...$``.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text

    def split_math_segments(s: str) -> list[str]:
        """Split text into alternating non-math and math segments.

        Returns a list where every odd index is a math-delimited string and
        every even index is the intervening non-math text.  Used by the
        ``unit_outside_math`` rule to ignore math regions during scanning.
        """
        return re.split(r"(\$\$?.*?\$\$?)", s, flags=re.DOTALL)

    offset = 0
    for segment in split_math_segments(text)[::2]:
        m = re.search(r"\b\d+(?:\.\d+)?\s*(?:V|A|Ω|W|mW|kΩ|C|Hz)\b", segment)
        if m:
            abs_idx = offset + m.start()
            length = m.end() - m.start()
            line, col, col_end = locate_range(text, abs_idx, length)
            errors.append(
                ValidationMessage(
                    "found a unit (e.g. V, A, Ω, W, mW, kΩ, C, Hz) outside math delimiters; enclose units in $...$",
                    line,
                    col,
                    col_end,
                )
            )
            break
        offset += len(segment)
    return errors


# additional rules ---------------------------------------------------------


@RULE_REGISTRY.register(id="math_in_code_fence")
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
                    "math expression found inside a code fence; use inline or display math instead",
                    line,
                    col,
                )
            )
            break
    return errors


@RULE_REGISTRY.register(id="latex_disallowed_delimiters")
def latex_disallowed_delimiters(ctx: ValidationContext) -> list[ValidationMessage]:
    r"""Disallow alternative LaTeX delimiters \[ \] or \( \) in favour of $.

    Search the text for the deprecated delimiters and flag their locations.
    """
    errors: list[ValidationMessage] = []
    m = re.search(r"\\\[|\\\]|\\\\(|\\\\)", ctx.text)
    if m:
        length = len(m.group(0))
        line, col, col_end = locate_range(ctx.text, m.start(), length)
        errors.append(
            ValidationMessage(
                "use dollar delimiters ($ or $$) instead of \\[ \\] or \\( \\)",
                line,
                col,
                col_end,
            )
        )
    return errors


@RULE_REGISTRY.register(id="latex_single_line")
def latex_single_line(ctx: ValidationContext) -> list[ValidationMessage]:
    """Enforce that LaTeX expressions do not span multiple lines.

    Finds each dollar-delimited segment and emits an error if it contains a
    newline character.
    """
    errors: list[ValidationMessage] = []
    for m in re.finditer(r"\$\$?.*?\$\$?", ctx.text, re.DOTALL):
        if "\n" in m.group(0):
            length = len(m.group(0))
            line, col, col_end = locate_range(ctx.text, m.start(), length)
            errors.append(
                ValidationMessage(
                    "LaTeX expression spans multiple lines; keep it on one line",
                    line,
                    col,
                    col_end,
                )
            )
    return errors


@RULE_REGISTRY.register(id="latex_not_standalone")
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
                    "LaTeX equation should not occupy an entire line; embed it in prose",
                    line_no,
                    col_no,
                    col_end,
                )
            )
    return errors


@RULE_REGISTRY.register(id="latex_spacing_before")
def latex_spacing_before(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when there is no space before an opening dollar math delimiter.

    This rule scans each LaTeX segment and checks the character immediately
    preceding the start; if it is not whitespace, an error is produced.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text
    for m in re.finditer(r"\$\$?.*?\$\$?", text, re.DOTALL):
        start_idx = m.start()
        if start_idx > 0:
            prev_char = text[start_idx - 1]
            if prev_char not in " \n" and not prev_char.isspace():
                line, col, col_end = locate_range(ctx.text, start_idx, 1)
                errors.append(
                    ValidationMessage(
                        "no space before opening dollar sign; add a space when text comes before math",
                        line,
                        col,
                        col_end,
                    )
                )
    return errors


@RULE_REGISTRY.register(id="latex_spacing_after")
def latex_spacing_after(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when there is no space after a closing dollar math delimiter.

    Similar to :func:`latex_spacing_before`, but checks the character immediately
    following each math expression.
    """
    errors: list[ValidationMessage] = []
    text = ctx.text
    for m in re.finditer(r"\$\$?.*?\$\$?", text, re.DOTALL):
        end_idx = m.end()
        if end_idx < len(text):
            next_char = text[end_idx]
            if (
                next_char not in " \n"
                and not next_char.isspace()
                and next_char not in punctuation
            ):
                line, col, col_end = locate_range(ctx.text, end_idx, 1)
                errors.append(
                    ValidationMessage(
                        "no space after closing dollar sign; add a space when text follows math",
                        line,
                        col,
                        col_end,
                    )
                )
    return errors


@RULE_REGISTRY.register(id="link_unencoded_space")
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
                "link target contains unencoded space; use %20 encoding",
                line,
                col,
                col_end,
            )
        )
    return errors


@RULE_REGISTRY.register(id="nested_list_path")
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
                    "nested list item does not include full path (e.g. 'ELEC 1100 / ...')",
                    line_no,
                    col_no,
                )
            )
            break
        offset += len(line)
    return errors


@RULE_REGISTRY.register(id="qa_missing_separator")
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
                        "QA-style flashcard list detected without preceding separator phrase",
                        line_no,
                        col_no,
                        col_end,
                    )
                )
            break
    return errors


@RULE_REGISTRY.register(id="qa_multiple_separators")
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
                    "line contains multiple flashcard separators (::@:: or :@:); use only one per card",
                    line_no,
                    col_no,
                    col_end,
                )
            )
            break
    return errors


@RULE_REGISTRY.register(id="br_space_rule")
def br_space_rule(ctx: ValidationContext) -> list[ValidationMessage]:
    """Require a space before ``<br/>`` tags.

    This rule flags occurrences of ``<br/>`` immediately following non-blank
    characters, reminding editors to add a space for readability.
    """
    errors: list[ValidationMessage] = []
    for m in re.finditer(r"[^ \t]<br/>", ctx.text):
        line, col = locate(ctx.text, m.start())
        col_end = col + len("<br/>") - 1
        errors.append(
            ValidationMessage(
                "'<br/>' found without a preceding space; add a space before '<br/>'",
                line,
                col,
                col_end,
            )
        )
        break
    return errors


@RULE_REGISTRY.register(id="week_monotonic_rule")
def week_monotonic_rule(ctx: ValidationContext) -> list[ValidationMessage]:
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
                    "week numbers do not progress monotonically (unexpected reset)",
                    line,
                    col,
                    col_end,
                )
            )
            break
        prev_week = num
    return errors
