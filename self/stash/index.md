---
aliases: []
tags:
  - function/index
  - language/in/English
---

# self/stash — Stashed utility scripts

A small collection of ad-hoc Python utilities kept here as a personal "stash". These files are user-managed; see `.agents/instructions/submodule-self.instructions.md` for repository guidance.

## Contents

- `md_table_to_rows.py` — Parse a Markdown table and produce a compact, per-row Markdown representation suitable for flashcard or note generation. Usage:

  ```bash
  # Read from clipboard and copy output back to clipboard (requires pyperclip for clipboard automation)
  python md_table_to_per_row_markdown.py --clipboard --copy

  # Read from a file and write to stdout
  python md_table_to_per_row_markdown.py -i path/to/table.md

  # Read from stdin and print output
  cat table.md | python md_table_to_per_row_markdown.py
  ```

- `clean_canvas_html.py` — Clean and normalize HTML copied from Canvas LMS for Markdown conversion.
- `d2l_mcq_to_md.py` — Convert exported D2L/Brightspace multiple-choice questions into Markdown.
- `download_attachments.py` — Download linked attachment files from HTML/Markdown documents.
- `find_missing_flashcards.py` — Inspect notes and flashcard metadata to locate missing cards.
- `median_filter_ignore_transparency.py` — Image‑processing helper: median filter that ignores transparent pixels.
- `rematch_flashcard_states.py` — Recompute or rematch flashcard review states after metadata changes.
- `tiling_puzzle_solver.py` — Puzzle solver used for experimenting with tiling algorithms (small utility script).

> Note: These scripts are intentionally informal and may rely on local utilities (e.g., `pyperclip`) or ad-hoc inputs. Edit or remove them only when you explicitly want to change your local stash.
