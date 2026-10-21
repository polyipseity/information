---
description: "Use when delegating a writing pass on one academic note to a fresh-context child. Holds the brief verbatim."
name: "Academic writing pass"
applyTo: "**"
alwaysApply: false
---

# Academic writing pass

The parent hands this brief to a child that has no history. Fill the three placeholders and send nothing else: no diagnosis, no before-state, no diff. A child that has read the parent's reasoning certifies it instead of reading the file.

```text
File: <absolute path>
Skills: <absolute path>/.agents/skills/academic-writing/SKILL.md and
        <absolute path>/.agents/skills/humanizer/SKILL.md
Contract: <absolute path>/.agents/instructions/academic-notes.instructions.md

Read the two skills and the file. Then rewrite its prose and cards.

Rules
- Cut before you add. Delete a sentence that repeats its neighbour, a section
  that restates the lead, and an adjective that carries no measurement. Report
  words removed against words added; removal must win.
- Keep every card line's mathematics identical. Do not change the number of
  `::@::` or `:@:` lines, the headings, the frontmatter, the `---` separators,
  image lines, or `<!-- check: ... -->` comments.
- No display math (`$$`), no em dash or en dash in prose, no `*` emphasis, no
  trailing whitespace, no run of three or more blank lines.
- Edit with short oldText/newText pairs, at most ten per call, one call per
  message. Never rewrite the whole file in one go.
- Do not rename a heading. Structure is the parent's call.

Report, five lines at most: words added, words removed, sections reordered or
merged, paragraphs deleted, and anything you could not do.
```

## Parent's gate

Before accepting the result, compare against the pre-pass copy: card count, each card line's `$...$` set, heading text, the suppression list, and the whole diff. A report that names no deletion means no pass happened, because the default is to cut.
