"""Data types used by the academic-notes validator.

This module defines the pydantic-based ``Frontmatter`` model, helper
classes such as ``StrList``, and container/dataclass types used during the
validation process.  It also provides simple enums and utilities for
reporting validation results.
"""

from collections.abc import Iterable
from dataclasses import dataclass
from enum import StrEnum
from os import fspath
from typing import cast

from anyio import Path
from pydantic import BaseModel, ConfigDict, Field, GetCoreSchemaHandler, ValidationInfo
from pydantic_core import core_schema

__all__ = (
    "StrList",
    "Frontmatter",
    "ValidationContext",
    "Severity",
    "ValidationMessage",
    "PreviewEntry",
    "ValidationResult",
)


class StrList(list[str]):
    """A list of strings that happily accepts almost anything.

    The validator will coerce ``None`` to an empty list.  If the input is an
    iterable (list/tuple/etc.) its items are stringified; any scalar value is
    converted to a single-element list.  This makes the model robust against
    YAML loader types such as ``YamlStr`` or other pydantic-yaml wrappers.

    This class implements a pydantic v2 core schema instead of the deprecated
    ``__get_validators__`` hook.  The schema simply delegates to the built-in
    ``list`` schema with a string validator, and then applies custom post-
    processing via ``validate`` to implement the lenient coercion rules.
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: object, handler: GetCoreSchemaHandler
    ):
        """Pydantic v2 hook to supply a custom core schema for ``StrList``.

        Constructs a base list-of-string schema and then wraps it with a
        post-validator (defined below) that implements the lenient coercions
        described in the class docstring.

        ``source`` and ``handler`` are part of the protocol but ignored.
        """
        # ``source`` and ``handler`` are required by the protocol but unused
        # here; the schema produced below is independent of them.

        # base schema: a list of *anything*; we'll convert elements to
        # strings in the post-validator.  using ``any_schema`` allows values
        # like ``[1, 2]`` or ``[null]`` to pass through rather than being
        # rejected by ``str_schema()`` prematurely.
        list_schema = core_schema.list_schema(core_schema.any_schema())
        # allow ``None`` values so that ``StrList`` fields default to an empty
        # list when the YAML/JSON explicitly contains ``null``.  ``union_schema``
        # ensures the ``_post_validator`` is still called, giving us a single
        # entry point for our coercions.
        # union accepts None, a list, or any other value (scalar/string)
        union_schema = core_schema.union_schema(
            [
                core_schema.none_schema(),
                list_schema,
                core_schema.any_schema(),
            ]
        )

        # wrap with a custom plain validator for our coercion rules
        def _post_validator(v: object, info: ValidationInfo[object]) -> StrList:
            """Plain validator implementing lenient coercion rules.

            - ``None`` becomes an empty ``StrList``.
            - Iterable inputs have their items stringified.
            - Scalar values are converted to single-element lists.
            This mirrors the behaviour of the ``validate`` method described in
            the class docstring above.
            """
            if v is None:
                return StrList()
            if isinstance(v, (list, tuple, set)):
                v = cast(
                    Iterable[object], v
                )  # mypy does not know the type of v here, but we just checked it
                return StrList(str(item) for item in v)
            try:
                return StrList([str(v)])
            except Exception:
                return StrList()

        # new API uses with_info_after_validator_function rather than the older
        # general_* helpers which have been deprecated.  ``info`` argument is
        # passed through automatically.
        return core_schema.with_info_after_validator_function(
            schema=union_schema,
            function=_post_validator,
        )


class Frontmatter(BaseModel):
    """Structured representation of YAML frontmatter used by rules.

    Simple model with two list fields.  Any extra keys in the YAML are
    ignored thanks to ``model_config``; they are not preserved since the
    validator never uses them.
    """

    aliases: StrList = Field(default_factory=StrList)
    tags: StrList = Field(default_factory=StrList)

    model_config = ConfigDict(extra="ignore")


@dataclass
class ValidationContext:
    """Execution context passed to each validation rule.

    Attributes correspond to parsed file state:
    ``path`` is the file path; ``text`` is the full file contents; ``front``
    is the raw YAML frontmatter string; ``data`` holds the parsed
    ``Frontmatter`` model; ``body`` contains the text after frontmatter; and
    ``session_headers`` is a list of tuples describing any ``## week N``
    headings found (used by session-related rules).
    """

    path: Path
    text: str
    front: str
    data: Frontmatter
    body: str
    session_headers: list[tuple[str, str, str, int]]


class Severity(StrEnum):
    """Severity levels for validation messages.

    Each value also carries a default Rich color string used when
    displaying the severity/rule-id prefix.  The colors are chosen to match
    the usual conventions (red for errors, yellow for warnings).
    """

    ERROR = "error"
    WARNING = "warning"

    @property
    def color(self) -> str:
        """Return a Rich style string associated with this severity."""
        if self is Severity.ERROR:
            return "bold red"
        if self is Severity.WARNING:
            return "bold yellow"
        # fallback
        return "bold cyan"


@dataclass
class ValidationMessage:
    """Structured message with location, severity, and originating rule ID.

    ``rule_id`` is **required**: every message must know which rule produced it.

    :param rule_id: ID of the rule that produced this message.
    :param msg: Human-readable error/warning text.
    :param severity: message severity; use :class:`Severity`.
    :param line: 1-based line number where the issue occurs, if known.
    :param col: 1-based column where the issue begins, if known.
    :param col_end: 1-based column immediately after the issue span.
    """

    rule_id: str
    msg: str
    severity: Severity = Severity.ERROR
    line: int | None = None
    col: int | None = None
    col_end: int | None = None


@dataclass
class PreviewEntry:
    """Preview information for a specific validation message.

    Instances are produced by :func:`aggregate` and serialized in JSON output.

    ``path`` is the file path; ``excerpt`` is a short snippet of text from the
    file; ``caret`` is an optional caret line pointing at a column range; and
    ``line``/``col`` indicate the location of the issue if known.
    """

    path: Path
    excerpt: str
    msg: str
    severity: Severity
    caret: str | None = None
    line: int | None = None
    col: int | None = None

    def to_dict(self) -> dict[str, object]:
        """Serialize the preview entry to a dictionary for JSON output.

        The returned dict includes the path, excerpt, and optionally caret,
        line, and column information if available.
        """
        d: dict[str, object] = {
            "path": fspath(self.path),
            "excerpt": self.excerpt,
            "msg": self.msg,
            "severity": self.severity,
        }
        if self.caret is not None:
            d["caret"] = self.caret
        if self.line is not None:
            d["line"] = self.line
        if self.col is not None:
            d["col"] = self.col
        return d


class ValidationResult:
    """Container for all validation messages discovered during a run.

    Every issue—whether an error or a warning—is stored in the
    :attr:`messages` list along with its severity.  Helper methods
    :meth:`errors` and :meth:`warnings` provide convenient filtered views.
    """

    def __init__(self) -> None:
        """Initialize an empty validation result container.

        The :attr:`messages` list will hold ``(Path, ValidationMessage)`` tuples.
        """
        # messages are stored as tuples of (Path, ValidationMessage)
        self.messages: list[tuple[Path, ValidationMessage]] = []

    def errors(self) -> list[tuple[Path, ValidationMessage]]:
        """Return only the messages that are errors (not warnings)."""
        return [(p, m) for p, m in self.messages if m.severity is Severity.ERROR]

    def warnings(self) -> list[tuple[Path, ValidationMessage]]:
        """Return only the messages that are warnings."""
        return [(p, m) for p, m in self.messages if m.severity is Severity.WARNING]

    def add(self, path: Path, msg: ValidationMessage) -> None:
        """Record a validation message for the given file path.

        The caller **must** supply a :class:`ValidationMessage` instance.  This
        simplifies the API by requiring a :class:`ValidationMessage`
        instance.  The message's ``severity`` attribute is used verbatim; the
        method does **not** modify it.

        :param path: path of the file where the issue was found
        :param msg: a prepared ``ValidationMessage`` with appropriate severity
        """
        self.messages.append((path, msg))
