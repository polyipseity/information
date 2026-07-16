#!/usr/bin/env python
"""Scaffold a new Wikipedia-sourced note with frontmatter, then create the file and a symlink.

Prompts for the language (ISO 639‑1/2 code, default eng) and article name,
builds YAML frontmatter and a skeleton note body, then atomically creates:
- general/<lang>/<name>.md (the note file)
- general/<name>.md → <lang>/<name>.md (relative symlink)
"""

from contextlib import suppress
from os import rename, symlink
from pathlib import Path
from re import sub
from unicodedata import normalize

import pycountry
from asyncer import runnify

"""Exported names from this module (none: standalone script, not importable as a library)."""
__all__ = ()

"""Absolute path to the repository root directory."""
_REPO_ROOT = Path(__file__).resolve().parent.parent


def _resolve_lang(code: str) -> tuple[str, str, str]:
    """Validate an ISO language code and return (directory_code, human_name, wikipedia_lang).

    Accepts ISO 639‑1 (2‑letter), ISO 639‑2 (3‑letter), and ISO 639‑3
    (3‑letter) codes.

    - ``directory_code``: longest available code via fallback chain
      ``alpha_3`` → ``alpha_2`` (used for filesystem directory).
    - ``wikipedia_lang``: shortest available code via fallback chain
      ``alpha_2`` → ``alpha_3`` (used for Wikipedia subdomain).
    """
    code = code.strip().lower()
    lang = pycountry.languages.get(alpha_2=code) or pycountry.languages.get(
        alpha_3=code
    )
    if lang is None:
        msg = f"unknown language code: {code!r}"
        raise LookupError(msg)
    dir_code = lang.alpha_3 or lang.alpha_2
    wikipedia_lang = lang.alpha_2 or lang.alpha_3
    return dir_code, lang.name, wikipedia_lang


async def main() -> None:
    """Prompt for language and article name, then create the note and symlink."""
    # --- Language ---
    raw = input("Language? (ISO code, default: eng) ").strip()
    lang_code = normalize("NFC", raw) if raw else "eng"
    dir_code, lang_name, wikipedia_lang = _resolve_lang(lang_code)

    lang_dir = _REPO_ROOT / "general" / dir_code
    if not lang_dir.is_dir():
        msg = f"language directory does not exist: {lang_dir}"
        raise FileNotFoundError(msg)

    # --- Name ---
    name = normalize("NFC", input("Name? ")).strip()
    if not name:
        msg = "name cannot be empty"
        raise ValueError(msg)

    tag_replacements = {"–": "-", "—": "-"}
    tag_name = sub(
        r"[^A-Za-z0-9À-ÿ_-]",
        lambda match: tag_replacements.get(match.group(0), "_"),
        name,
    )
    if not tag_name or tag_name.isnumeric():
        tag_name += "_"

    wikipedia_name = name.replace(" ", "_")
    title = sub(r" \([^()]+\)$", "", name)
    output = f"""---
aliases:
  - {title}
tags:
  - flashcard/active/general/{dir_code}/{tag_name}
  - language/in/{lang_name}
---

# {title}

## references

This text incorporates [content](https://{wikipedia_lang}.wikipedia.org/wiki/{wikipedia_name}) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
"""

    # --- File paths ---
    note_path = lang_dir / f"{name}.md"
    link_path = _REPO_ROOT / "general" / f"{name}.md"
    link_target = f"{dir_code}/{name}.md"

    # Pre-check: neither path must exist (file or symlink)
    if note_path.exists() or note_path.is_symlink():
        msg = f"note already exists: {note_path}"
        raise FileExistsError(msg)
    if link_path.exists() or link_path.is_symlink():
        msg = f"symlink target already exists: {link_path}"
        raise FileExistsError(msg)

    # --- Atomic write: temp files + atomic rename ---
    tmp_note = note_path.with_suffix(".md.tmp")
    tmp_link = link_path.with_suffix(".md.link.tmp")

    success = False
    try:
        tmp_note.write_text(output, encoding="utf-8")
        symlink(link_target, tmp_link)
        rename(tmp_note, note_path)
        rename(tmp_link, link_path)
        success = True
    finally:
        if not success:
            for p in (tmp_note, tmp_link, note_path, link_path):
                with suppress(OSError):
                    p.unlink()

    print(f"Created: {note_path}")
    print(f"Symlink: {link_path} -> {link_target}")


def __main__():
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
