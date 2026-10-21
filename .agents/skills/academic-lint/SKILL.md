---
name: academic-lint
description: 'Validate academic course notes after edits. Wraps main.py validator with two modes: whole-course or specific-files.'
---

# Academic Lint

Wraps the `main.py` validator and defines when and how to run it.

## When to run

Run it after every edit to academic notes under `special/academia/`, and before committing.

Validation is the __last__ step of an edit. The humanizer pass runs first (see "Humanizer pass" in `academic-ingest`): rewriting a card can strand a suppression with nothing to suppress, or create a warning that now needs one.

## Invocation modes

### Specific files (preferred when known)

When you know which files were edited, lint those files only:

```bash
uv run python .agents/skills/academic-lint/main.py <file1> <file2> ...
```

### Whole-course (default)

When the whole course folder changed (scaffolding a new course, batch updates), lint the entire course:

```bash
uv run python .agents/skills/academic-lint/main.py "special/academia/<INSTITUTION>/<COURSE>/"
```

With no paths, the run covers both trees: `special/academia` and `private/special/academia`.

### Private files

A file under `private/special/academia` validates as if it sat at its mirrored public path: flashcard tags derive from the path after `special/academia/`, so a private page carries its public twin's tag, and a children link written in colocated form resolves against the mirrored tree (see "Public and private trees" in `academic-ingest`). A target missing from both trees still warns.

## Exit codes

- `0`: no issues
- `1`: warnings only, advisory, fix when practical
- `2`: errors found, must fix before commit

## Blind spots

A clean run is a shape check, not a content check, and a value that is internally consistent but wrong still passes. `session_datetime_order` compares the `datetime:` values as written, so it cannot tell a session carrying another section's weekday, time, or venue; no rule compares a session against the section recorded in `## logistics`, or an ordinal against the sessions around it in its week. A `status: no class` session holding a wrong slot is as invisible to the linter as a correct one. Verifying those is the author's job, against the source, per "Session ordering" and "Validation" in `academic-crud-course-index`.

In a whole-course run the warnings can come from untouched files. Re-run on the edited file to tell a pre-existing warning from an introduced one, and report the pre-existing ones instead of fixing them.

## Options

- `--json`: machine-readable output
- `--max-per-rule N`: limit per-rule output (default 5, 0 for unlimited)

## Change audit

Every run reads the uncommitted diff against `HEAD`, read-only and scoped to the paths being linted. It prints `change audit: N file(s) vs HEAD, M warning(s)`, and outside a git work tree it says so and carries on. No flag turns it off.

| Rule | Fires when |
| --- | --- |
| `change_append_bias` | a topic note gains 300 bytes or more, at three bytes added per byte deleted |
| `change_flat_section_growth` | a note that already had six `##` sections gains another, with no `###` added |
| `change_note_without_index` | a topic note changed and its course `index.md` gained no link to it |

These warnings cannot be suppressed; a directive naming one is reported as `suppression-not-permitted`. They observe a window rather than a state, so __they clear when the files are committed__, and committing is the user's act. An agent that believes the addition is genuine new material ignores the warning and says so in its report. Deleting content to silence one is never the fix.

## Structure rules

Sections nest. A note's _width_ is the largest number of sibling sections that open no subsection of their own, and `flatness = width / 7`.

| Rule | Severity | Fires when |
| --- | --- | --- |
| `header_hierarchy_flat` | error | width above 9 |
| `header_hierarchy_thin` | warning | width 7 to 9 |
| `header_hierarchy_shallow` | warning | no `###` at all, 120+ lines, width 5 or 6 |
| `header_generic_article` | error | a section name opens on `the`, `a`, `an`, or a demonstrative |
| `header_question_form` | warning | a section name is a question |
| `header_sentence_like` | warning | a section name ends in `.`, runs past nine words, or carries a finite verb |

A section name is a term: `time constant`, not `the time constant`; `hysteresis`, not `the state it keeps`. Renaming a heading breaks every `§` anchor pointing at it, so re-link the course `index.md` in the same edit, or `link_anchor_slug` reports the miss.

## Readability rules

Seven standard metrics score each topic note against a single density limit:

| Metric | Fails above |
| --- | --- |
| Flesch reading ease | below 35, because the scale runs backwards |
| Flesch-Kincaid grade | 13 |
| Gunning fog | 13.5 |
| SMOG | 13 |
| Coleman-Liau | 14.5 |
| automated readability index | 13.5 |
| Dale-Chall | 8.8 |

Only one direction counts. Text denser than the limit is the defect; plain prose under every limit is the target, so nothing fires for writing simply. A note with one or two metrics past the limit gets `readability_warning`, three or more get `readability_error`.

Prose and cards are measured apart, because they are read differently. The prose score leaves out frontmatter, headings, maths, code, the `Flashcards for this section are as follows:` separator and everything under it, and the `## references` list. The card score measures that block alone, and reports `card_readability_warning` or `card_readability_error` from the same limits. Prose needs 120 words and 8 sentences to score, cards need 60 words and 4 sentences, and a note that is mostly non-English is skipped.

A word the course already uses as a heading or alias is jargon and never counts as difficult, which is Fog's own definition, not an exemption.

The seven metrics measure the shape of the text, not whether it teaches anything. Padding a sentence or shredding one into fragments moves a score and is a worse defect than the one reported. The fix for a failing metric is structural: merge or split sections, break up the longest sentences, cut clauses that carry no fact. A failing card means it asks two things at once or pads an answer that should be one term.

## Suppression

A suppression is an HTML comment: `<!-- check: ignore-line[rule_id]: why -->` on the line it exempts, or `<!-- check: ignore-next-line[rule_id]: why -->` on the line above. A heading takes the second form, because a comment on the heading line becomes part of the heading text. Content rules accept a rationale after a colon; the three change rules refuse one, because the diff is the evidence and the file cannot hide the warning about itself.

## Sibling tools

Files in this directory:

| Tool | Purpose |
| --- | --- |
| `main.py` | Entry point for the validator CLI |
| `main_mods/` | Validation rules, models, and registry |
| `tests_a7392be/` | Validator test suite |

## References

- All `academic-crud-*` skills run this after edits
