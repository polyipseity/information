---
name: academic-notes
description: Content conventions, examples, and tooling for course notes under special/academia.
---

# Academic notes — consolidated skill

This document explains how to author, validate, and maintain academic course notes stored under `special/academia/<INSTITUTION>`. Agents and human authors **must read every line of this file** before editing course material, since the rules below are exhaustive and are enforced by the validator script. Flashcards are generated automatically by the build system; do **not** run `init generate` yourself.

## Key principles

1. **Content first**: capture every slide bullet, formula, definition, wor/ked example and instructor comment as prose or hierarchical bullets. Err on the side of completeness; extra detail helps recall and tooling filters out noise. When in doubt include more rather than less.
2. **Automatic flashcards**: add flashcard markup (`{@{ }@}`, `::@::`, `:@:`) whenever you add new factual material. Update cards whenever you expand or revise a section. Generators run in CI; agents must never invoke them.
3. **Structured metadata**: every file starts with a `---` YAML block. Use ISO‑8601 datetimes, maintain `children:` lists in indexes, add activation tags (`flashcard/active/special/academia/...`), and keep semester headings chronological. The validator warns on most mistakes.
4. **Session ordering**: lectures/labs/tutorials ordered by the `datetime:` interval; all exams go after regular sessions. Duplicate week numbers around holidays require manual renumbering plus an entry with `status: public holiday`. Entries with `status: unscheduled` must omit `topic:`.
5. **Continuous improvement**: record new rules, bugs, or user preferences in `continuous_improvement.md` and update this file accordingly. Feedback drives evolution of the skill.

## Pre‑commit checklist

Before committing any new or changed course note, run through these items:

- YAML frontmatter present and delimited by `---` at the top of the file.
- `aliases` include canonical course code(s) and human-readable names; tags include `flashcard/active/special/academia/<INSTITUTION>/<PAGE>` and where appropriate `function/index` and `language/in/English`.
- Do **not** create, modify or edit files under `general/` – only work inside the course folder.
- Index files: `# index` header and a `## children` list or `children:` YAML key with child pages in teaching order (folders first). Use ISO datetimes for week entries and ensure they have `datetime` and, unless `status: unscheduled`, `topic`.
- Check that lecture/lab/tutorial entries are chronological and exams are placed last. Run `python .github/skills/academic-notes/validate_academic.py --content special/academia/<INSTITUTION>` for automated checks; address warnings.
- Ensure every Markdown section in a topic note contains flashcard entries (inline clozes or a rubric introduced by “Flashcards for this section are as follows:” preceded by `---`). The validator flags missing cards.
- Add assignments, questions, attachments under appropriate subfolders and list them under `children`.
- Link to canonical `general/` pages instead of copying long definitions; percent-encode spaces in paths. When a concept deserves its own course note, follow the topic‑specific notes workflow below.
- Filenames are friendly and human‑readable; use spaces and percent‑encode them in links.
- Run `pnpm run format`, `pnpm run check` (with `--no-globs` and explicit paths), and `pnpm run test` locally before committing.

Recommended but not required:

- Use `assignments/`, `questions/`, and `attachments/` subfolders for respective content.
- Include venue lines immediately after `datetime:`; apply the HKUST room interpretation rule if appropriate (numeric rooms → “Room ####, Academic Building”).
- Add at least one worked example or solution sketch for important techniques and sample exam‑style problems linked to `questions/solutions.md`.
- Record lab/tutorial section identifiers near the top of the note so tooling can filter irrelevant streams.

## Authoring workflow

1. Start with `course-template.md`. Fill aliases (singular, plural, concatenated), tags (include underscore course code), course name, credits, and brief description. Sort aliases alphabetically.
2. Add a `logistics` section with `scheme:` weights and a nested `sections:` list grouped by lectures/tutorials/labs. Include identifiers, venues, and weekly time patterns.
3. Maintain a `children:` list with lectures, labs, assignments, topics, questions, attachments; keep entries in teaching order and update it whenever you add a new page.
4. Use the session structure from the examples below. Add `datetime:` entries with ISO intervals (date only if time unknown). Place prose summaries after the bullet outline separated by `---`. Draft explanatory prose before adding cloze markup; don’t flashcard‑ify first and then write prose.
5. Capture content‑first details in prose paragraphs, not bullets; convert slide fragments into full sentences.
6. Audit the whole file whenever you add or change any section: check for missing/malformed flashcards, separators, numeric values, tags, and indentation.
7. Run the validator and address warnings. Fix issues before committing.

### Session and index rules

- Heading styles: `## week N lecture`/`lab`/`tutorial`; number resets each week after filtering irrelevant streams. If a week is repeated due to holidays, shift subsequent weeks upward and insert an entry with `status: public holiday`.
- Session metadata: `datetime:` ISO_START/ISO_END[, DURATION]; `topic:` short text (omit if `status: unscheduled`); optional `status:` and `venue:`.
- Bullet items nested under a session hold course‑specific notes and cross‑links. Each top‑level bullet must sit on its own source line; use `<br/>` or `<p>` for internal breaks. Numeric examples should include units inside `$…$` math delimiters.
- Outline items correspond to flashcard glosses; avoid extra indentation levels. Convert generic headings into specific cloze entries or remove them.
- After the outline, add a prose paragraph preceded by `---` for administrative comments (schedule links, grading breakdowns, reminders). Use cloze markup within that paragraph for cards.
- Semester headings in institution indexes must be chronologically ordered; validator warns otherwise.

## Flashcards and markup

- Use three patterns only:
  - **Cloze deletions**: `{@{hidden text}@}` anywhere in a paragraph.
  - **Two‑sided QA**: single source line `term ::@:: definition` (produces two cards). Use `<br/>` or `<p>` for visible breaks; do not insert newlines.
  - **One‑sided QA**: single source line `term :@: answer` (one card).
- Add a gloss by appending `::@::` after a linked term. The text after `::@::` becomes the card content; keep it concise, normally one or two sentences. Long derivations do not make good cards.
- Prefix every gloss with the complete hierarchical path (`COURSE / topic / item`). Do not rely on indentation for context; only the literal text is used by the flashcard generator.
- When grouping related cards, give the parent a full path label (e.g. `ELEC 1100 / class expectations`) and nest children beneath it.
- Calculation cards must be self‑contained: put all given values on the left and outline computation steps on the right.
- Units must always be inside `$…$` or `$$…$$` (e.g. `$5\\text{ V}$`); units outside math trigger validator warnings.
- Every markdown section in a topic note, no matter the header level, must have at least one flashcard entry. Use a horizontal rule `---` immediately before the first flashcard block; missing separators or cards trigger validator warnings. Index files are exempt and need only session‑level cards.
- Do not merge cards across sections; each heading gets its own block directly beneath the prose. The validator flags missing separators or cards.
- Keep gloss text single‑lined; use `<br/>` for right‑hand breaks, never sublists. Bibliographic references on the right‑hand side should be dash‑separated with a space before each `<br/>`.
- When you see `takeaway ::@:: …` consider converting it to a `takeaway:` metadata field.
- Avoid acronyms. Spell out the first occurrence and add a card if needed.
- Do not write next‑lecture remarks inside sessions unless they describe a major grading event (exam or project milestone).

**Example snippets** (long lines deliberately unwrapped):

```markdown
## week 3 lecture

- datetime: 2025-09-16T12:00:00+08:00/2025-09-16T13:20:00+08:00, PT1H20M
- topic: polymorphism; type bound; variance
- COMP 3031
  - COMP 3031 / polymorphism ::@:: Parametric polymorphism, subtyping polymorphism
```

```markdown
## week 7 lecture

- datetime: 2025-10-07T12:00:00+08:00/2025-10-07T13:20:00+08:00, PT1H20M
- topic: type inference; Hindley–Milner
- COMP 3031
  - HM / algorithm sketch ::@:: Unify constraints from expression syntax tree, solve by substitution
  - HM / type variable rules ::@:: Fresh variable introduced for each binder; generalized at let-bound identifiers
  - HM / worked example (detailed):
    1. Given expression: let f = \\x -> (x, x) in f 3
    2. Assign type variables: x: a, result tuple components a, a
    3. Constraint from (x, x): both positions share type a
    4. f: a -> (a, a); application f 3 enforces a = Int by unification
    5. Generalize: f : forall a. a -> (a, a); instantiate at Int for f 3
    6. Result: (3, 3) :: (Int, Int)
  - HM / pitfalls ::@:: Forgetting to generalize at let leads to value restriction bugs. **Emphasis**: Instructor stressed 'generalization at let-bindings' (important for polymorphism in ML-like languages).
```

```markdown
---

Flashcards for this section are as follows:

- energy definition ::@:: Energy is the ability to do work and may be electrical, mechanical, thermal, or chemical.
- human/robot analogy ::@:: People get energy from food while robots obtain it from batteries or power supplies.
```

These examples illustrate proper indentation, cloze usage, and the two-sided QA list format.

## Flashcard tags

Always add `flashcard/active/special/academia/<institution>/<page>` to frontmatter. `<page>` mirrors the course code with underscores and should not be percent‑encoded. Validators flag missing or malformed tags; report missing tags in review rather than bulk-editing existing files.

## Topic-specific notes

When a lecture topic merits its own note (because it is broad, reused, or should link from multiple sessions) create a new file under the course directory. Topic-specific notes are intended to be **Wikipedia-style articles**: write in neutral voice with natural flowing paragraphs rather than slide-outline bullet lists. Break content into coherent sections, using headers to organise the prose and **ensure each section includes its own flashcard block** as described above. Use a Wikipedia article title for the filename (capitalize proper nouns, lowercase the first letter otherwise). The heading inside the note matches the filename in sentence case. Add aliases and tags appropriate to the topic and include a cross-link to the corresponding `general/` article (percent‑encode spaces). Update the course `children:` list by appending the file after folders and add a markdown section link in the weekly outline. When later lectures revisit the topic, append to the existing note rather than creating a duplicate.

Use `python .github/skills/academic-notes/find_wikipedia.py "<query>"` to search for canonical titles; choose the top candidate and link to `../../../../general/<title>.md`. Do not create or edit files under `general/` yourself.

**Example (excerpt from an existing topic note):**

```markdown
# electronic component

Electronic components are the building blocks of electronic circuits; they affect how currents flow and voltages appear, and range from passive elements such as resistors and capacitors to active semiconductor devices like diodes and transistors. In ELEC 1100 the scope is expanded to include the underlying electrical concepts required to understand component behaviour, together with the power sources and delivery systems (batteries, supplies) that energise a robot’s electronic subsystems.

---

Flashcards for this section are as follows:

- electronic component definition ::@:: Electronic components are the building blocks used in electronic circuits that influence the behaviour of currents and voltages.
- passive vs active examples ::@:: Passive elements like resistors and capacitors contrast with active semiconductor devices such as diodes and transistors.
- course context ::@:: In ELEC 1100, electronic components also include basic electrical concepts needed to understand how components operate.
- active device examples ::@:: Active semiconductor devices include diodes and transistors, distinguishing them from passive elements.
- power/energy context ::@:: In ELEC 1100, electronic components also encompass power sources and delivery systems such as batteries and supplies that provide energy.
```

The above excerpt demonstrates natural prose, clear sectioning, and the flashcard block that immediately follows the introductory paragraph. Every subsequent header (e.g. `## electrical fundamentals`, `### atoms and charge`) likewise contains its own `---` followed by a card list, so no matter how deep the hierarchy the validator will find and generate cards correctly.

## Validator and tooling

Run:

```shell
python .github/skills/academic-notes/validate_academic.py special/academia/<path>
```

Use `--content` for advisory warnings during drafting. Common warnings include missing tags, absent `datetime:` values, out‑of-order semesters, sections without cards, duplicate week numbers, and exams placed too early. Address issues where practical. Before committing, run `pnpm run format`, `pnpm run check`, and `pnpm run test` with explicit paths to your changed files so the commands execute quickly.

The repository contains helper scripts (`validate_academic.py`, `find_wikipedia.py`) and templates (`course-template.md`) that you should inspect when writing new notes. Keep these tools up to date and report any bugs or feature requests in `continuous_improvement.md`.

## Continuous improvement

Record every new pattern, validator failure, or user preference in `continuous_improvement.md` and consider whether the rule should be added to this document. Short reports can be placed under `.github/skills/academic-notes/reports/`. The skill evolves with real course content, and maintainers should review the log periodically.
