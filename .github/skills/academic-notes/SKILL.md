---
name: academic-notes
description: Content conventions, examples, and tooling for course notes under special/academia.
---

# Academic notes — consolidated skill

This document explains how to author, validate, and maintain academic course notes stored under `special/academia/<INSTITUTION>`. Agents and human authors **must read every line of this file** before editing course material, since the rules below are exhaustive and are enforced by the validator script. Flashcards are generated automatically by the build system; do **not** run `init generate` yourself.

## Key principles

1. **Content first**: capture every slide bullet, formula, definition, wor/ked example and instructor comment as prose or hierarchical bullets. Err on the side of completeness; extra detail helps recall and tooling filters out noise. When in doubt include more rather than less.
2. **Automatic flashcards**: add flashcard markup (`{@{ }@}`, `::@::`, `:@:`) whenever you add new factual material. Update cards whenever you expand or revise a section. Generators run in CI; agents must never invoke them.
3. **Structured metadata**: every file starts with a `---` YAML block. Use ISO‑8601 datetimes, maintain `children:` lists in indexes, add activation tags (`flashcard/active/special/academia/...`), and keep semester headings chronological. The validator enforces these rules and will report any violations as errors.  
   - The validator’s output now includes the exact line (and column when available) where a problem was detected, along with a short preview of the offending line, making it much easier to locate and fix issues quickly. The preview highlights the precise column range using carets (`^`), and long lines are truncated with ellipses so the marker remains in view. The length of the snippet is automatically limited to fit within your terminal width (accounting for the leading `preview:` indentation).
4. **Session ordering**: lectures/labs/tutorials ordered by the `datetime:` interval; all exams go after regular sessions. Duplicate week numbers around holidays require manual renumbering plus an entry with `status: public holiday`. Entries with `status: unscheduled` must omit `topic:`.
5. **Continuous improvement**: record new rules, bugs, or user preferences in `continuous_improvement.md` and update this file accordingly. Feedback drives evolution of the skill.
6. **Math formatting**: never place math in fenced code blocks. Use LaTeX inline (`$…$`) or display (`$$…$$`) notation for all formulas; this applies equally to examples in topic notes and session outlines.
   - **Dollar delimiters only.**  Do not use `\[`, `\]`, `\(` or `\)`; all LaTeX must be wrapped in `$…$` or `$$…$$`.
   - **One line only.**  Whether inline or display math, the source between the delimiters must not contain a newline.  In particular, display formulas must use `$$` but stay on a single markdown line.
   - **Never standalone.**  A line consisting solely of a math expression is forbidden; the formula must be embedded in surrounding prose or list text.  This keeps diff noise down and matches the flashcard generator’s expectations.
   - **Spacing around delimiters.**  When an equation appears after other text, leave a normal space before the opening dollar sign; likewise put a space after the closing dollar if more text follows.  **Exception:** no space is required if the character immediately following the closing dollar is punctuation (e.g. `.,;:!?)]}`) or the end of line.  Leading or trailing whitespace is allowed at the beginning or end of a paragraph, but adjacent alphanumeric characters without a space will trigger the validator.
7. **Header style**: section headers in topic notes should be all lowercase (capitalize only proper nouns or the first word of a sentence) to keep anchors predictable and maintain consistency.

## Authoring workflow

This section covers the full lifecycle of course note content, from initial creation through final checks before committing. Start here whenever you need to add or revise material.

1. Start with `course-template.md`. Fill aliases (singular, plural, concatenated), tags (include underscore course code), course name, credits, and a brief description. Sort aliases alphabetically.
2. Add a `logistics` section with `scheme:` weights and a nested `sections:` list grouped by lectures/tutorials/labs. Include identifiers, venues, and weekly time patterns.
3. Maintain a `children:` list with lectures, labs, assignments, topics, questions, attachments; keep entries in teaching order and update it whenever you add a new page.
4. Use the session structure from the examples below. Add `datetime:` entries with ISO intervals (date only if time unknown). Place prose summaries after the bullet outline separated by `---`. Draft explanatory prose before adding cloze markup; don’t flashcard‑ify first and then write prose.
5. Capture content‑first details in prose paragraphs, not bullets; convert slide fragments into full sentences.
6. Audit the whole file whenever you add or change any section: check for missing/malformed flashcards, separators, numeric values, tags, and indentation.
7. Run the validator and fix any errors it reports. Errors must be resolved before committing.

### Pre‑commit checklist

Before committing any new or changed course note, run through these items.  This checklist complements the authoring steps above and ensures metadata, chronology, and flashcards are all in place.

- YAML frontmatter present and delimited by `---` at the top of the file.
- `aliases` include canonical course code(s) and human-readable names; tags include `flashcard/active/special/academia/<institution>/<course code>/<page>` and where appropriate `function/index` and `language/in/English`. `<page>` mirrors the relative path to the course folder with underscores and should not be percent‑encoded. Validators flag missing or malformed tags; report missing tags in review rather than bulk-editing existing files.
- Do **not** create, modify or edit files under `general/` – only work inside the course folder.
- Index files: `# index` header and a `## children` list or `children:` YAML key with child pages in teaching order (folders first). Use ISO datetimes for week entries and ensure they have `datetime` and, unless `status: unscheduled`, `topic`.
- Check that lecture/lab/tutorial entries are chronological and exams are placed last. **Run the validator only on the specific course directory you are editing rather than the entire institution tree** (e.g. `python .github/skills/academic-notes/check.py special/academia/HKUST/ELEC\ 1100`); running it on `special/academia/HKUST/` will produce too many unrelated errors. Fix any errors returned.
- Ensure every Markdown section in a topic note contains flashcard entries (inline clozes or a rubric introduced by “Flashcards for this section are as follows:” preceded by `---`). The validator flags missing cards.
- Add assignments, questions, attachments under appropriate subfolders and list them under `children`.
- Link to canonical `general/` pages instead of copying long definitions; percent-encode spaces in paths. When a concept deserves its own course note, follow the topic‑specific notes workflow below.
- Filenames are friendly and human‑readable; use spaces and percent‑encode them in links.
- Run `pnpm run format`, `pnpm run check` (with `--no-globs` and explicit paths), and `pnpm run test` locally before committing.
- Use `assignments/`, `questions/`, and `attachments/` subfolders for respective content.
- Include venue lines immediately after `datetime:`; apply the HKUST room interpretation rule if appropriate (numeric rooms → “Room ####, Academic Building”).
- Add at least one worked example or solution sketch for important techniques and sample exam‑style problems linked to `questions/solutions.md`.
- Record lab/tutorial section identifiers near the top of the note so tooling can filter irrelevant streams.

### Session and index rules

- Heading styles: `## week N lecture`/`lab`/`tutorial`; number resets each week after filtering irrelevant streams. If a week is repeated due to holidays, shift subsequent weeks upward and insert an entry with `status: public holiday`.
- Session metadata: `datetime:` ISO_START/ISO_END[, DURATION]; `topic:` short text (omit if `status: unscheduled`); optional `status:` and `venue:`.
- Bullet items nested under a session hold course‑specific notes and cross‑links. Each top‑level bullet must sit on its own source line; use `<br/>` or `<p>` for internal breaks. Numeric examples should include units inside `$…$` math delimiters.
- Outline items correspond to flashcard glosses; avoid extra indentation levels. Convert generic headings into specific cloze entries or remove them.
- After the outline, add a prose paragraph preceded by `---` for administrative comments (schedule links, grading breakdowns, reminders). Use cloze markup within that paragraph for cards.
- Semester headings in institution indexes must be chronologically ordered; validator warns otherwise.

Once the session outline rules are understood, the next section describes how flashcards themselves are formatted and how to tag them correctly.

## Flashcards and markup

The spaced‑repetition system is central to the entire repository; flashcards are automatically generated from your markup. These rules apply both within session outlines and inside longer topic notes, so master them early.

- Use three patterns only:
  - **Cloze deletions**: `{@{hidden text}@}` anywhere in a paragraph.
  - **Two‑sided QA**: single source line `term ::@:: definition` (produces two cards). Use `<br/>` or `<p>` for visible breaks; do not insert newlines.
  - **One‑sided QA**: single source line `term :@: answer` (one card).
- Add a gloss by appending `::@::` after a linked term. The text after `::@::` becomes the card content; keep it concise, normally one or two sentences. Long derivations do not make good cards.
- Prefix every gloss with the complete hierarchical path (typically `topic / item`; for course-specific content, use `COURSE / topic / item`). Do not rely on indentation for context; only the literal text is used by the flashcard viewer.
- When grouping related cards, give the parent a full path label (e.g. `ELEC 1100 / class expectations`) and nest children beneath it.
- Calculation cards must be self‑contained: put all given values on the left and outline computation steps on the right.
- Units must always be inside `$…$` or `$$…$$` (e.g. `$5\text{ V}$`); units outside math trigger validator errors.
- Every markdown section in a topic-specific note, no matter the header level, must have at least one flashcard entry. Use a horizontal rule `---` immediately before the first flashcard block; missing separators or cards trigger validator errors. Index files are exempt and need only session‑level cards.
- Do not merge cards across sections; each heading gets its own block directly beneath the prose. The validator flags missing separators or cards.
- Keep gloss text single‑lined; use `<br/>` for right‑hand breaks, never sublists. Bibliographic references on the right‑hand side should be dash‑separated with a space before each `<br/>`.
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
- Hindley–Milner
  - Hindley–Milner / algorithm sketch ::@:: Unify constraints from expression syntax tree, solve by substitution
  - Hindley–Milner / type variable rules ::@:: Fresh variable introduced for each binder; generalized at let-bound identifiers
  - Hindley–Milner / worked example (detailed): <p> 1. Given expression: let f = \\x -> (x, x) in f 3 <br/> 2. Assign type variables: x: a, result tuple components a, a <br/> 3. Constraint from (x, x): both positions share type a <br/> 4. f: a -> (a, a); application f 3 enforces a = Int by unification <br/> 5. Generalize: f : forall a. a -> (a, a); instantiate at Int for f 3 <br/> 6. Result: (3, 3) :: (Int, Int)
  - Hindley–Milner / pitfalls ::@:: Forgetting to generalize at let leads to value restriction bugs. **Emphasis**: Instructor stressed 'generalization at let-bindings' (important for polymorphism in ML-like languages).
```

```markdown
---

Flashcards for this section are as follows:

- example power calculation: Given a $200\,\Omega$ resistor with $5\text{ V}$ across it, what power is dissipated? ::@:: Use $P=V^{2}/R$ to get $0.125\text{ W}$.
- parallel circuit current: Two $2\,\Omega$ resistors are in parallel with $10\,\text{V}$ applied; find the total current. ::@:: First compute $R_{\text{eq}}=(1/2+1/2)^{-1}=1\,\Omega$ then $I=V/R_{\text{eq}}=10\,\text{A}$.
- 10 V series‑plus‑parallel network: A $10\text{ V}$ source drives a $2\,\Omega$ resistor in series with a parallel combination of a single $2\,\Omega$ branch and another branch composed of two $2\,\Omega$ resistors in series; what is the total current? ::@:: Equivalent resistance $10/3\,\Omega$ gives $I=3\text{ A}$.
- series/parallel power: A $5\text{ V}$ source drives two equal resistors $R_S=R_L=2.4\text{ k}\Omega$ in series; calculate the power dissipated by $R_L$. ::@:: The answer is about $2.6\text{ mW}$ (use $I=1.04\text{ mA}$, then $I^{2}R$, or halve the total power).
```

These examples illustrate proper indentation, cloze usage, and the two-sided QA list format.

## Topic-specific notes

When a lecture topic deserves its own dedicated page — either because it is broad, gets revisited, or should be linkable from multiple sessions — create a new Markdown file inside the course directory. **Create the file empty first** (use a normal, unescaped filename with spaces; links will be percent-encoded later) and then add content in separate edit operations. When subsequently editing a topic note, each commit should target exactly one markdown section or add exactly one new section so that diffs remain precise and reviewable.

These **topic notes** are written in a neutral, encyclopaedic style rather than as a bulleted outline. Think of them as miniature Wikipedia articles: use smooth prose, organise the text with headings, and split material into logical sections.

Each section must be followed immediately by a horizontal rule and a list of flashcards, exactly as described earlier in this document.  The validator will reject any heading that lacks a card block, so it’s easiest to add the "Flashcards for this section are as follows:" rubric as you compose the paragraphs.

### Filenames, titles, and links

- Use a Wikipedia‑style title for the filename: capitalise proper nouns and lowercase the first letter of ordinary words.  The top‑level heading in the note should match the filename in all lowercase (except for proper nouns).
- When creating the file, do **not** percent-escape the name; percent-encoding is only applied when writing links elsewhere.
- Add appropriate `aliases:` and `tags:` in the frontmatter, including the usual `flashcard/active/special/academia/...` tag for the course page.
- Cross‑link to the corresponding `general/` article using a relative path with `%20` encoding for spaces.  To discover canonical titles, run `python .github/skills/academic-notes/find_wikipedia.py "<query>"` and pick the top hit.  **Do not** create or modify files under `general/` yourself.

### Course index and outline updates

After creating a topic note, append its link to the course `children:` list (after any folders) and add a reference in the relevant weekly session entry. When you later revisit the topic in another lecture, append new material to the existing file instead of making a duplicate. *Proper nouns such as Kirchhoff must be capitalised in both filenames and headings.*

### Micro‑workflow example

**Math and formatting rules:** never use fenced code blocks for maths; always write expressions inline or in display math (`$...$` or `$$...$$`) using LaTeX syntax. Topic notes do not require a separate summary section. Section headers should use all lowercase words except where grammatical capitalization is needed (proper nouns, the first word of a sentence).

Create the note, update the index, and add the outline link as shown below:

```markdown
# Kirchhoff's circuit laws

...prose section as shown in the section "Sample note excerpt" later...

---

Flashcards for this section are as follows:

...flashcard section following guidelines in the "Flashcards and markup" section...
```

```markdown
## children

- [electronic component](electronic%20component.md)
- [Kirchhoff's circuit laws](Kirchhoff%27s%20circuit%20laws.md)
```

```markdown
### week 2 lecture 2

- datetime: 2026-02-13T11:30:00+08:00/2026-02-13T12:20:00+08:00, PT50M
- venue: CYT-LTL
- topic: KCL & KVL
- ELEC 1100
  - ELEC 1100 / [Kirchhoff's circuit laws](Kirchhoff%27s%20circuit%20laws.md) ::@:: Two fundamental relations (KCL and KVL)
    - [§ current law](Kirchhoff%27s%20circuit%20laws.md#Kirchhoff's%20current%20law%20(KCL)) ::@:: Sum of currents entering a node equals sum leaving it
    - [§ voltage law](Kirchhoff%27s%20circuit%20laws.md#Kirchhoff's%20voltage%20law%20(KVL)) ::@:: Sum of voltage drops around a closed loop equals zero
```

These snippets illustrate the full cycle: author the topic note, add it to `children:`, and reference specific sections by anchor in the weekly outline. When adding or modifying sections, keep edits focused to a single section as noted above. Adjust the headings and anchors as needed when the note grows.

With a topic note written and flashcards inserted, you should run the validator and other tooling described in the next section to catch any structural problems before you commit.

### Sample note excerpt

To show how prose, structure and cards coexist, here is an excerpt from an existing topic note:

```markdown
## resistor networks

Resistors in series add: $R_{\text{eq}} = R_1 + R_2 + \cdots$; the same current flows through each. A voltage divider is a pair of series resistors; the voltage at the junction N relative to ground is $V\cdot\frac{R_L}{R_S + R_L}$ assuming ideal wire (zero resistance) and ground reference.

Resistors in parallel combine as $1/R_{\text{eq}} = 1/R_1 + 1/R_2 + \cdots$; the total resistance is always smaller than the smallest branch. Conductance $G = 1/R$ is useful, unit siemens (S).

For a network with mixed series/parallel elements the total resistance may be computed stepwise (e.g. $30\,\Omega + (40\,\Omega\parallel 60\,\Omega) = 54\,\Omega$).

Short circuit occurs when a low-resistance path bypasses a component (R→0); current through the short tends to infinity and components may be damaged. In an ideal short the branch current is infinite and the other branch zero.

Resistors dissipate electrical power as heat, which is why excessive current can make a resistor get hot or even burn.  The video linked in the slides demonstrates a resistor glowing when driven beyond its power rating.

---

Flashcards for this section are as follows:

- series resistors formula ::@:: Resistors in series simply add: $R_{\text{eq}} = R_1 + R_2 + \cdots$ (same current through each).
- voltage divider ::@:: A voltage divider is two series resistors; assuming an ideal wire and ground, setup the circuit as V → RS → N → RL → GND → (V), then the voltage at node N is $V\cdot\frac{R_L}{R_S + R_L}$.
- series divider assumptions ::@:: The voltage-divider formula assumes an ideal wire (zero resistance) and that the reference node is ground (0 V).
- parallel resistors formula ::@:: Resistors in parallel satisfy $1/R_{\text{eq}} = 1/R_1 + 1/R_2 + \cdots$; conductance $G = 1 / R$ with unit siemens.
- conductance units ::@:: Conductance $G=1/R$ is measured in siemens (S); older units mho or ℧ are equivalent.
- network calculation example: A $5\,\textrm{V}$ source drives $30\,\Omega$ in series with parallel $40\,\Omega$ and $60\,\Omega$ branches; what are $R_{\text{eq}}$ and total current? ::@:: $R_{\parallel}=24\,\Omega$, $R_{\text{eq}}=54\,\Omega$, $I=5/54\approx0.093\,\textrm{A}$.
- short circuit danger ::@:: A short circuit is a near-zero-resistance path (close to zero, like through a metal wire) causing very high current and has the potential to damage components.

### numerical examples

- Example power dissipated by a $200\,\Omega$ resistor with $5\text{ V}$ across it: $P = V^{2}/R = 0.125\text{ W}$.
- Network example: a $10\text{ V}$ source drives a $2\,\Omega$ resistor in series with a parallel combination of a single $2\,\Omega$ branch and another branch composed of two $2\,\Omega$ resistors in series; the equivalent resistance is $R=\tfrac{10}{3}\,\Omega$ and the total current is $I=3\text{ A}$ (slide example).
- Challenging series/parallel example: a source of $5\text{ V}$ drives two equal resistors $R_S=R_L=2.4\text{ k}\Omega$; total $R=4.8\text{ k}\Omega$ giving $I=1.04\text{ mA}$, so $P_{R_L}=I^{2}R_L\approx2.6\text{ mW}$ (same result whether computed via current or halving total power).

---

Flashcards for this section are as follows:

- example power calculation: Given a $200\,\Omega$ resistor with $5\text{ V}$ across it, what power is dissipated? ::@:: Use $P=V^{2}/R$ to get $0.125\text{ W}$.
- parallel circuit current: Two $2\,\Omega$ resistors are in parallel with $10\,\text{V}$ applied; find the total current. ::@:: First compute $R_{\text{eq}}=(1/2+1/2)^{-1}=1\,\Omega$ then $I=V/R_{\text{eq}}=10\,\text{A}$.
- 10 V series‑plus‑parallel network: A $10\text{ V}$ source drives a $2\,\Omega$ resistor in series with a parallel combination of a single $2\,\Omega$ branch and another branch composed of two $2\,\Omega$ resistors in series; what is the total current? ::@:: Equivalent resistance $10/3\,\Omega$ gives $I=3\text{ A}$.
- series/parallel power: A $5\text{ V}$ source drives two equal resistors $R_S=R_L=2.4\text{ k}\Omega$ in series; calculate the power dissipated by $R_L$. ::@:: The answer is about $2.6\text{ mW}$ (use $I=1.04\text{ mA}$, then $I^{2}R$, or halve the total power).
```

The excerpt demonstrates natural prose, clear headings, and a card block immediately after the introductory paragraph. Every subsequent header (e.g. `## resistor networks`, `### numerical examples`) likewise contains its own `---` followed by cards, allowing the validator to locate them regardless of the depth of nesting.

## Validator and tooling

Before pushing your edits, validate them using the provided tooling. The validator script checks metadata, chronology, flashcards, and other conventions; consider it the programme’s grammar checker.

Run:

```shell
python .github/skills/academic-notes/check.py special/academia/<institution>/<course folder>  # e.g. special/academia/HKUST/ELEC\ 1100; do not point at the whole institution
```

The validator is strict and does not have an advisory mode. Common errors include missing tags, absent `datetime:` values, out‑of-order semesters, sections without cards, duplicate week numbers, and exams placed too early. Fix errors before committing. Before committing, run `pnpm run format`, `pnpm run check`, and `pnpm run test` with explicit paths to your changed files so the commands execute quickly.

The repository contains helper scripts (`check.py`, `find_wikipedia.py`) and templates (`course-template.md`) that you should inspect when writing new notes. Keep these tools up to date and report any bugs or feature requests in `continuous_improvement.md`.

## Continuous improvement

Record every new pattern, validator failure, or user preference in `continuous_improvement.md` and consider whether the rule should be added to this document. Short reports can be placed under `.github/skills/academic-notes/reports/`. The skill evolves with real course content, and maintainers should review the log periodically.
