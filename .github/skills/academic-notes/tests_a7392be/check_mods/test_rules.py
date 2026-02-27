"""Lightweight rule tests for the academic-notes validator.

Each function constructs a minimal ValidationContext and exercises a rule
function, verifying expected messages or lack thereof.
"""

import re

from anyio import Path
from check_mods.models import Frontmatter, ValidationContext
from check_mods.rules import (
    RULE_REGISTRY,
    aliases_sorted,
    index_children_rule,
    index_heading_rule,
    index_semester_order_rule,
    metadata_aliases_present,
    metadata_flash_tag,
    metadata_tags_present,
    session_datetime_order,
    session_duplicate_heading,
    tag_language,
)
from check_mods.utils import FRONT_RE, parse_frontmatter
from pydantic_yaml import parse_yaml_raw_as

# explicit imports reduce namespace clutter and make references clear


__all__ = ()


def make_ctx(text: str, path: Path = Path("/tmp/course/index.md")) -> ValidationContext:
    """Helper constructing a ValidationContext from raw markdown text."""
    front = parse_frontmatter(text) or ""
    if front:
        try:
            data = parse_yaml_raw_as(Frontmatter, front)
        except Exception:  # pragma: no cover
            data = Frontmatter()
    else:
        data = Frontmatter()

    body = text
    m = FRONT_RE.match(text)
    if m:
        body = text[m.end() :]
    session_headers = []
    for m2 in re.finditer(
        r"^##\s+week\s+(\d+)(?:\s+(\w+))?", text, re.IGNORECASE | re.MULTILINE
    ):
        week = m2.group(1)
        typ = (m2.group(2) or "").lower()
        session_headers.append((week, typ, m2.group(0), m2.start()))
    return ValidationContext(
        path=path,
        text=text,
        front=front,
        data=data,
        body=body,
        session_headers=session_headers,
    )


def test_metadata_aliases_present():
    """The aliases present rule should fire when frontmatter lacks aliases."""
    txt = "---\ntags: []\n---\n"
    ctx = make_ctx(txt)
    msgs = metadata_aliases_present(ctx)
    assert msgs and msgs[0].msg.startswith("no 'aliases:'")
    # also verify the rule is registered in the module registry
    ids = [rid for rid, _ in RULE_REGISTRY.items()]
    assert "metadata_aliases_present" in ids
    txt = "---\naliases:[a]\ntags:[]\n---\n"
    ctx = make_ctx(txt)
    assert not metadata_aliases_present(ctx)


def test_metadata_tags_present_and_flash():
    """Rules should detect missing tags and missing flash activation."""

    txt = "---\naliases: [a]\n---\n"
    ctx = make_ctx(txt)
    msgs = metadata_tags_present(ctx)
    # flash rule should not fire when tags are entirely absent
    assert any("no 'tags:'" in m.msg for m in msgs)

    txt = "---\ntags: []\n---\n"
    ctx = make_ctx(txt)
    msgs = metadata_flash_tag(ctx)
    assert msgs and msgs[0].msg.startswith("missing flashcard")


def test_aliases_sorted_and_tag_language():
    """Aliases order and language tag rules fire appropriately."""

    txt = "---\naliases: [b, a]\ntags: [language/in/English]\n---\n"
    ctx = make_ctx(txt)
    assert aliases_sorted(ctx)
    assert not tag_language(ctx)
    # wrong language
    txt = "---\naliases: [a]\ntags: []\n---\n"
    ctx = make_ctx(txt)
    assert tag_language(ctx)


def test_index_rules():
    """Index-specific rules should only apply to index.md and detect problems."""

    txt = "# some page\n"
    ctx = make_ctx(txt, path=Path("/tmp/index.md"))
    assert index_heading_rule(ctx)
    assert index_children_rule(ctx)

    txt = "# index\n## children\n### 2023 fall\n### 2022 spring\n"
    ctx = make_ctx(txt, path=Path("/tmp/index.md"))
    msgs = index_semester_order_rule(ctx)
    assert msgs and "chronological" in msgs[0].msg


def test_session_rules():
    """Session-related rules around duplicates and datetime ordering."""

    txt = "## week 1 lecture\n## week 1 lecture\n"
    ctx = make_ctx(txt)
    msgs = session_duplicate_heading(ctx)
    assert msgs and "duplicate session heading" in msgs[0].msg

    txt = (
        "## week 1 lecture\n- datetime: 2023-01-02T10:00\n"
        "## week 2 lecture\n- datetime: 2023-01-01T09:00\n"
    )
    ctx = make_ctx(txt)
    msgs = session_datetime_order(ctx)
    assert msgs and "not after previous" in msgs[0].msg
