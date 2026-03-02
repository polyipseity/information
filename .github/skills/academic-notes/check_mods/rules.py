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

from .models import Severity, ValidationContext, ValidationMessage
from .registry import RuleRegistry
from .utils import FRONT_RE, has_flash_tag, locate, locate_range

__all__ = ("RULE_REGISTRY",)

# single registry used by this module; external code may import and merge it
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
            rel = "/".join(part.replace(" ", "_") for part in rel.split("/"))
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
def index_heading_rule(ctx: ValidationContext) -> list[ValidationMessage]:
    """Check that an index.md contains a top-level '# index' heading.

    Only applicable to files named 'index.md'.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() == "index.md":
        if "# index" not in ctx.text:
            errors.append(
                ValidationMessage(
                    "index_heading_rule", "index.md missing '# index' heading"
                )
            )
    return errors


@RULE_REGISTRY.register()
def index_children_rule(ctx: ValidationContext) -> list[ValidationMessage]:
    """Ensure index.md includes a 'children' section or heading.

    Looks for either '## children' or a literal 'children:' string.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() == "index.md":
        if "## children" not in ctx.text and "children:" not in ctx.text:
            errors.append(
                ValidationMessage(
                    "index_children_rule", "index.md missing 'children' section"
                )
            )
    return errors


@RULE_REGISTRY.register()
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
            errors.append(
                ValidationMessage(
                    "index_semester_order_rule", msg, line=line_no, col=col_no
                )
            )
            break
    return errors


# session-related -----------------------------------------------------------


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

    This rule applies only when the session is not marked 'unscheduled'.  It
    mirrors the second half of the previous ``session_topic_presence`` rule but
    now lives in its own registration so that each violation has a distinct
    rule identifier.
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
            # skip unscheduled sessions here
            if "status:" in section and re.search(
                r"status:\s*unscheduled", section, re.IGNORECASE
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
                "Stand‑alone example sections are discouraged – move the material under the appropriate conceptual header, "
                "or, if you truly need a separate examples block, add a justification using a suppression comment.",
                line=line,
                col=col,
                col_end=col_end,
            )
        )
    return errors


@RULE_REGISTRY.register()
def header_style_rule(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when non-index headers start with an uppercase letter.

    This stylistic rule scans all headers of level 2 or deeper and emits a
    warning for headers whose first non-space character is uppercase or
    non-alphanumeric.  Proper nouns (person names, brands, etc.) are
    legitimate exceptions; callers can suppress the warning using a
    check directive (for example
    ``<!-- check: ignore-line[header_style_rule]: proper name -->``) if the
    capitalization is intentional.
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
            # this rule is stylistic; most headers should be lowercase
            # but proper nouns (people, brands, etc.) may legitimately
            # start with a capital letter.  emit as a warning so callers
            # can suppress it if the capitalization is intentional.
            errors.append(
                ValidationMessage(
                    rule_id="header_style_rule",
                    msg=(
                        "header normally start lowercase; suppressions are allowed only **for proper nouns**.  Do **not** ignore this rule for ordinary section titles."
                    ),
                    severity=Severity.WARNING,
                    line=line,
                    col=col,
                    col_end=col_end,
                )
            )
    return errors


@RULE_REGISTRY.register()
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
                    rule_id="header_flashcard_presence",
                    msg=f"header {hdr!r} has no flashcard markers in its section",
                    line=line,
                    col=col,
                    col_end=col_end,
                )
            )
    return errors


@RULE_REGISTRY.register()
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
                        rule_id="header_flashcard_separator",
                        msg=f"flashcards under header {hdr!r} should be preceded by a '---' separator",
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
                            "on the left so the card is answerable. For example:\n"
                            R"before: - Ohm's law example ::@:: If $I = 2\,\text{A}, R = 5\,\Omega$, then by Ohm's law $V = IR = 10\,\text{V}$.\n"
                            R"after:  - Ohm's law example: Given $I = 2\,\text{A}$ and $R = 5\,\Omega$, calculate the voltage $V$ using Ohm's law. ::@:: If $I = 2\,\text{A}, R = 5\,\Omega$, then by Ohm's law $V = IR = 10\,\text{V}$. "
                            "Long prompts (even full derivations) are fine – the rule warns only "
                            "about missing context, not verbosity. To suppress for a purely "
                            "conceptual card use `<!-- check: ignore-line[two_sided_calc_warning]: conceptual -->`."
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
    necessary numerical data; urge the author to include or duplicate that
    data in the prompt.  **For calculation cards the left prompt may be
    arbitrarily long; write out the full equation or value list – the warning
    is about missing answerable context, not about keeping the prompt short.**
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
                            "Include or duplicate the needed values in the left prompt. For example:\n"
                            R"before: - Ohm's law example :@: If $I = 2\,\text{A}, R = 5\,\Omega$, then by Ohm's law $V = IR = 10\,\text{V}$.\n"
                            R"after:  - Ohm's law example: Given $I = 2\,\text{A}$ and $R = 5\,\Omega$, calculate the voltage $V$ using Ohm's law. :@: If $I = 2\,\text{A}, R = 5\,\Omega$, then by Ohm's law $V = IR = 10\,\text{V}$. "
                            "Long equations are allowed; this check simply ensures answerable context. "
                            "For conceptual-only cards suppress with `<!-- check: ignore-line[one_sided_calc_warning]: conceptual -->`."
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

    1. A number followed (optionally with intervening whitespace) by a
       electrical unit such as ``V``, ``A``, ``\u03a9``, ``Hz``, ``W`` etc.
    2. A simple variable assignment like ``I2=0.04`` where a letter and
       digit are followed by an equals sign (the right-hand side may itself
       include units).

    If either pattern is found on a dollar-free line a warning is emitted
    advising the author to wrap the expression in ``$...$``.  The check is
    deliberately conservative to avoid flagging mundane prose such as dates or
    lecture numbers; it only runs on lines that include one of the above
    constructs.  Suppressions are supported via the usual ``<!-- check: ... -->``
    directives when the numeric content is intentionally not typeset as math.
    """
    errors: list[ValidationMessage] = []
    # precompile regexes for performance
    unit_re = re.compile(r"\b\d+(?:\.\d+)?\s*(?:V|A|Ω|Ohm|Hz|W|mW|kΩ|mV|kV|mA|kA|C)\b")
    var_eq_re = re.compile(r"\b[IiRrVv]\d+\s*=")
    for idx, line in enumerate(ctx.text.splitlines(), start=1):
        if "$" in line:
            # line already contains math; skip
            continue
        if unit_re.search(line) or var_eq_re.search(line):
            # warn at the first matching substring
            m = unit_re.search(line) or var_eq_re.search(line)
            assert m is not None
            col = m.start() + 1
            col_end = m.end() + 1
            errors.append(
                ValidationMessage(
                    rule_id="numeric_text_not_latex",
                    msg=(
                        "numeric expression detected outside math delimiters; "
                        "wrap quantities such as 5 V or I2=0.04 A in `$…$` "
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
    """
    errors: list[ValidationMessage] = []
    # match a single-dollar expression but not $$
    for m in re.finditer(r"(?<!\$)\$.*?\$(?!\$)", ctx.text, re.DOTALL):
        if "\n" in m.group(0):
            length = len(m.group(0))
            line, col, col_end = locate_range(ctx.text, m.start(), length)
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
    """
    errors: list[ValidationMessage] = []
    text = ctx.text
    for m in re.finditer(r"\$\$?.*?\$\$?", text, re.DOTALL):
        start_idx = m.start()
        if start_idx > 0:
            prev_char = text[start_idx - 1]
            # opening parenthesis is acceptable (common in e.g. "($x$"),
            # so we treat it as a non-error even though there is no space.
            if prev_char not in " \n(" and not prev_char.isspace():
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


# split the original check into two specific rules; retain a wrapper
# for backward compatibility.


@RULE_REGISTRY.register()
def no_soft_wrap_paragraph(ctx: ValidationContext) -> list[ValidationMessage]:
    """Flag unescaped single newlines within paragraphs.

    Paragraphs should not be soft-wrapped.  List items are ignored here.
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
                    rule_id="week_monotonic_rule",
                    msg="week numbers do not progress monotonically (unexpected reset)",
                    line=line,
                    col=col,
                    col_end=col_end,
                )
            )
            break
        prev_week = num
    return errors
