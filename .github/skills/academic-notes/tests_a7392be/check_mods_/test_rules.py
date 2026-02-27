"""Lightweight rule tests for the academic-notes validator.

Each function constructs a minimal ValidationContext and exercises a rule
function, verifying expected messages or lack thereof.
"""

import re

from anyio import Path
from check_mods.models import Frontmatter, ValidationContext
from check_mods.rules import RULE_REGISTRY, metadata_aliases_present
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
