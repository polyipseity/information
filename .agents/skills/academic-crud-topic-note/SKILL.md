---
name: academic-crud-topic-note
description: Create, read, update, and delete standalone topic notes (<topic>.md) for concepts, theorems, and lecture content under special/academia/<INSTITUTION>/<COURSE>/.
---

# Academic CRUD: Topic notes

Create, read, update, and delete standalone topic notes. These are concept-focused pages, like compact encyclopedia entries, with explanatory prose and section-local flashcards.

## Target

`special/academia/<INSTITUTION>/<COURSE>/<topic>.md`

## Topic note naming

The filename stem and the H1 title are the __same string__, and both are the canonical Wikipedia article title for the concept, written in __sentence case__ — capitalize only the first word plus genuine proper nouns, eponyms, and acronyms.

Naming is a mandatory step, not a stylistic afterthought. It runs before scaffolding, because renaming a note afterwards also means fixing every link to it in the course `index.md`.

### When to use

- Creating __any__ topic note — always, to fix the filename and the H1 title. Not only for Wikipedia-sourced notes.
- Creating a `transcludes/` entry for full Wikipedia content (see `academic-crud-transcludes`).
- Verifying the canonical title or spelling of a concept before adding aliases.

### Naming rules

- Sentence case, not title case: `operating system`, not `Operating System`.
- Prefer the Wikipedia form and number: `operating system`, not `Operating Systems` or `operating systems`.
- Keep the casing of proper nouns, eponyms, acronyms, and product names: `Boolean algebra`, `Kirchhoff's circuit laws`, `Lisp`, `Scala 3`, `H-bridge`.
- Hyphenation follows Wikipedia: `pulse-width modulation`.
- When Wikipedia has no article for the concept, invent a sentence-case descriptive title and record it as an alias.
- Aliases: the canonical title first, then synonyms and abbreviations.
- The path-derived flashcard tag mirrors the filename: spaces and quote characters become `_` and every other character stays literal, parentheses included. `cache (computing).md` in `COMP 3511` needs the tag `flashcard/active/special/academia/HKUST/COMP_3511/cache_(computing)` — never normalize or strip the parentheses.

| Correct | Wrong |
| --- | --- |
| `operating system` | `Operating System` |
| `introduction to operating systems` | `Introduction and OS Structures` |
| `pulse-width modulation` | `Pulse Width Modulation` |
| `Kirchhoff's circuit laws` | `Kirchhoffs Circuit Laws` |

Filenames on disk contain literal spaces (`operating system.md`); links encode those spaces as `%20` and keep every other character literal: `- [cache (computing)](cache%20(computing).md)`.

__Why this needs its own step:__ the `header_style` lint rule starts at heading level 2, so an H1 title is never checked, and no lint rule inspects filenames. A title-case name passes validation silently and can only be caught here.

### Discovering the canonical title

```bash
# Search for articles matching a query (default: 3 results)
uv run python .agents/skills/academic-crud-topic-note/find_wikipedia.py "Fourier transform"

# Limit results
uv run python .agents/skills/academic-crud-topic-note/find_wikipedia.py --limit 3 "Bayes theorem"
```

`find_wikipedia.py` searches Wikipedia and returns canonical titles, URLs, and short descriptions. It finds the exact article title (avoiding redirects and disambiguation pages), gives the canonical spelling of a technical term, and surfaces related articles you may not have considered.

Use the returned canonical title verbatim as both the filename stem (`<topic>.md`) and the H1 title (`# <topic>`).

### Mapping output to frontmatter

The canonical title is the primary alias, followed by synonyms and abbreviations:

```yaml
aliases:
  - Fourier transform
  - Fourier analysis
  - DFT
```

## Grouping: concepts, not source layout

File and section boundaries come from the concepts, never from the shape of the ingested material. A deck, a chapter, a page range, and a lecture are delivery formats, not concepts: they determine what content exists, never how it is grouped or named.

### Files are concepts

- The unit of a note is a concept with a canonical title and a body that stands on its own — never a source unit.
- Never name or bound a file after its source: no `lecture 3`, `chapter 1`, `part 2`, `slides 20-37`, `introduction`, `definitions`, `misc`, `other topics`, or `summary`.
- __Merge test__ — one note when the parts share a single canonical title, when neither can be explained without the other, or when they are one concept seen from two angles (a mechanism and its motivation or failure modes).
- __Split test__ — separate notes when they answer different canonical-title questions, when their prerequisites differ, or when their sections would not cohere under a single concept. Independent linkability is supporting evidence, never the deciding test.
- __When the tests conflict, the canonical-title test decides.__ One canonical title means one note: that another note might link to a section does not by itself justify a file, or every section would become one.
- Regrouping moves boundaries; it never drops facts. Every source fact lands in exactly one note, with its flashcards.
- The file set has no order. Teaching order lives only in the course `index.md` — the `## overview` topic-to-file mapping and the session entries.
- New material about an existing concept routes to Update (see Create below). A source never produces a file named after itself, and a five-concept source produces five notes, not one lecture summary.

### Sections are sub-concepts

- A `##` heading names a sub-concept of the note's own concept, in sentence case — never a source unit, slide title, page number, or source-structural label.
- Rename every source heading to the sub-concept it carries: `Why Does Caching Work? - Locality` → `locality of reference`, `a bit history` → `history and adoption`.
- A section must not restate the note's own concept: `## caching` inside `cache (computing)` and `## hierarchy of storage` inside `memory hierarchy` repeat the H1. Give the section a genuine sub-aspect the title does not already claim, or drop the heading and keep the material as the note's unheaded intro prose with its flashcard block.
- Section boundaries may cross source boundaries in both directions: merge material that answers one question, split material that answers several.
- Lecture apparatus is never a section: objectives, outline, recap or summary, announcements, references, and question lists belong to the course `index.md`, not to a concept note.
- The sections must partition the concept — each answers one question, along parallel axes, with no leftover other section.
- Order sections by the concept's own logic: definition, then mechanism, then variants, limits, and examples. Coinciding with the source's order is fine; the source's order is never the justification.

### Nesting is always decided

Decide nesting explicitly while planning the note. Do not inherit the source's depth, and do not default to flat.

- __Nest__ (`###`) when a section carries two or more independently meaningful sub-concepts: a classification whose variants each own a block, per-case breakdowns (modes, models, layers), separate derivations or worked examples, or sub-topics a reader would link to on their own.
- __Do not nest__ when the sub-topics read better as prose or a short list, when it would produce exactly one `###` (fold it back), or when the only reason is the source's layout.
- __Tiebreaker__: count flashcards per variant. A variant earns its own block when it carries two or more flashcards, or more than a sentence or two of explanation. A variant captured by a single card stays flat however many variants the section has, because the section's single block already covers them: three one-card variants are still flat.
- __Depth__: `###` freely. `####` when it names a distinct sub-sub-concept of a `###` and splitting the note instead would fragment one concept, justified inline with `<!-- check: ignore-line[header_deep_nesting]: <reason> -->`. `#####` and deeper are unsanctioned — they mean the file boundary is wrong, so split the note instead.
- Every `###` and deeper carries its own `---` separator and its own `Flashcards for this section are as follows:` block, recursively.
- Flat is a valid outcome for a concept with no sub-concepts — as a decision, never as a default.

## CRUD operations

### Create

1. __Determine the canonical title:__ run `find_wikipedia.py` and take the canonical article title verbatim as the filename stem and the H1 title — see "Topic note naming" above. Do this first; renaming later means fixing links in the course `index.md` too.

2. __Classify incoming content:__
   - Duplicate of existing note → do not create; route to Update
   - Enhancement of existing note → route to Update
   - New concept → create new note

3. __Extract content structure:__
   - Key concepts, definitions, formulas, derivations
   - Examples, counterexamples, worked problems
   - Teaching caveats, distinctions, classifications
   - Mathematical spine: formula + derivation + intuition + worked example
   - Decide the file boundary: one concept, per the merge and split tests in "Grouping: concepts, not source layout"
   - Decide the sections and their nesting — never mirror the source's headings or depth

4. __Scaffold note file:__

```markdown
---
aliases:
  - <canonical term>
  - <synonym 1>
tags:
  - flashcard/active/special/academia/<INSTITUTION>/<COURSE>/<topic_name>
  - language/in/English
---

# <topic name>

<Motivating prose — 1-3 paragraphs explaining why the concept matters and how it fits the course narrative>

---

Flashcards for this section are as follows:

- overview ::@:: <single-sentence definition>
- <concept> / <specific aspect> ::@:: <self-contained answer>
- ...

## <section heading>

<Explanatory prose — definition, motivation, theorem, derivation, intuition, worked example>

---

Flashcards for this section are as follows:

- <concept> / <specific aspect> ::@:: <self-contained answer>
- ...

### <sub-concept heading>

<Nested explanatory prose — only where the nesting criteria apply>

---

Flashcards for this section are as follows:

- <concept> / <sub-concept aspect> ::@:: <self-contained answer>
- ...
```

1. __Flashcard generation:__
   - Use `::@::` (two-sided QA) format — NOT cloze `{@{ }@}`
   - Exception: accounting journal-entry worked examples may use cloze
   - Every `##`, `###`, and deeper heading gets its own `---` separator and its own flashcard block — never one block shared by a parent and its sub-sections
   - Group related cards with inline bold labels (e.g., `**superposition.**`)
   - Cards must be self-contained (restate givens, hypotheses, notation)
   - Overview card as first card in each section
   - Preserve derivation/proof spine in cards
   - Split packed cards into focused units
   - Calculation cards must name every quantity they combine on the prompt side (e.g. `$\text{hit ratio}$`, `$\text{hit time}$`), so the card is answerable in isolation. Rewrite a two-sided card this way before reaching for a suppression (`two_sided_calc_warning`)
   - Lint suppression: `<!-- check: ignore-line[two_sided_calc_warning]: conceptual -->` on math cards, only when the card is genuinely conceptual rather than computational
   - `<p>` for paragraph breaks in single-line source
   - No `<b>`/`</b>` — use `__` for bold

2. __Figures and diagrams:__
   - When the source carries figures the prose depends on (slide diagrams, schematics, plots), extract page images per "Document extraction (mandatory)" in `academic-ingest`.
   - Copy only the pages that matter into `attachments/pages/<stem>/`; do not copy the whole deck.
   - Reference each from the section that uses it: `![<alt text>](attachments/pages/<stem>/page_007.png)`.
   - Alt text is plain language describing what the figure shows — never LaTeX.
   - Leave `.extracted/` alone; it is a cache, not an attachment source.

3. __Update course index:__
   - Read the course `index.md` (`special/academia/<INSTITUTION>/<COURSE>/index.md`)
   - Add the topic note to `## children` in its sorted position: folders first, then files, Python string order within each group — see "Children format" in `academic-crud-index`
   - Determine which session heading the topic belongs to (e.g., `## week 3 lecture`). Use the session mapping rules below. If the session is unclear from the input, __ask the user__ which session(s) the topic should be linked under.
   - Under the matched session heading, add a link to the topic note with section anchors for each `##` section that this session's material created or expanded. A file link alone is never enough:

     ```markdown
     - [topic name](topic%20name.md)
         - topic name / [§ section heading](topic%20name.md#section%20heading)
     ```

   - If the topic spans multiple sessions, add links under each relevant session, listing under each only the sections that session's material covered

4. __Humanizer pass:__ sweep the prose and the flashcards separately before validating — the H1 intro and each section's prose first, then every card prompt and answer. See "Humanizer pass" in `academic-ingest`.

5. __Validate:__ run `academic-lint` on the created file.

### Read

List topic notes for a course; search by keyword; show structure and flashcard count.

### Update

Merge new material into existing note:

1. Detect overlap with existing content
2. Enhance prose: add new distinctions, examples, counterexamples
3. Add/modify flashcards — do not overstuff existing cards; add new ones instead
4. Refresh course `index.md`:
   - Update `## children` if the topic was renamed
   - Update session topic links if sections were added, removed, or renamed
   - Re-verify the session mapping if the topic's scope changed
5. Validate after changes

### Delete

1. Remove the topic note file
2. Remove from course `index.md` `## children`
3. Remove topic links from all session headings under which it appeared
4. Update cross-references in other notes that linked to this topic
5. Validate after changes

## Missing data

Use `\[missing\]` for absent values — for example, when a topic has no cross-references or a section has no formula. See [special.instructions.md](../../instructions/special.instructions.md#missing-data).

## Style conventions

- Lowercase headings except proper nouns (use `<!-- check: ignore-next-line[header_style]: proper noun -->`)
- A `##` heading must not repeat the note's own H1 title (MD024). Merge that section's prose and flashcards into the unheaded intro under the H1 instead of renaming the heading.
- `_italic_` and `__bold__` (not `*`/`**`)
- KaTeX `$...$` (inline) and `$$...$$` (block) intact, on one source line. A `$$...$$` block must share that line with the surrounding prose — never leave a display equation alone on its own line (`latex_not_standalone`)
- Ordinals: `$k$-th` not `$k$th` (LaTeX renders without hyphen literally)
- Distribution names: `\operatorname{Bin}`, `\operatorname{Exp}`, `\operatorname{Poi}`, etc.
- Indicator functions: `\mathbf 1_A(x)` or `\mathbb 1_A(x)`
- Multi-letter operators: `\operatorname{Var}`, `\operatorname{Cov}`, `\operatorname{E}`, `\operatorname{MSE}`
- Left/right limits: `\lim_{y\uparrow m}`, `\lim_{y\downarrow m}`
- "Distributed as": `\sim` (e.g., `$X\sim N(0,1)$`)
- Binomial coefficients: `\binom{n}{k}`
- No source numbering (theorem numbers, definition numbers, chapter numbers). Use topic names
- No "in this lecture" or "the tutorial sheet shows". Use topic-level references

## Subject-specific guidance

### Technical/mathematical notes

- Formula + derivation + intuition + worked example as default bundle
- Explicit comparisons of commonly confused concepts (e.g., message vs signal, energy vs power)
- Named analogies to classical mathematics (discrete Dirichlet problem, maximum principle)
- Proof sketches for non-obvious statements

### Honors/proof-heavy courses

- State hypotheses explicitly
- Short derivation/proof sketches over bare theorem statements
- Concrete examples and counterexamples
- Equivalent formulations listed explicitly

### Machine-learning notes

- Derive formulas; separate estimation from decision
- Make assumptions explicit (IID, priors, thresholds, intercept conventions)
- Distinguish true distribution $P$ from model distribution $Q$
- Distinguish L2 regularization from weight decay
- Explain why empirical loss carries $1/N$ factor
- Pair forward layer equation with composition and backward views

### Physics/electronics/lab notes

- Define jargon near first use ($V_{CC}$, $V_{CE}$, "low-side switch")
- Circuit topology, polarity, loop direction in cards
- Diagram-recall flashcards for key symbols
- Signal-processing: stage-by-stage chain explanation

### Accounting notes

- Journal-entry examples in topic sections (not separate collector)
- Each scenario in blockquote: scenario → Dr/Cr table → explanation
- Cloze in quoted scenarios, tables, calculations
- Table: right-aligned Dr/Cr columns, `&nbsp;` thousands separator
- Warranty examples allow settlement credits (Cash, Inventory, Accrued Payroll)

## Session mapping

When updating the course `index.md`, link topic notes under the correct session heading. Session headings follow the format `## week N lecture`, `## week N tutorial`, or `## week N lab`.

### Determining the correct session

1. __Input metadata__ — PDF filename, Canvas assignment title, or user-provided context often names the session (e.g., "lecture 5", "tutorial 3")
2. __Topic content__ — match the topic's subject matter to the session's `topic:` line in the index
3. __User input__ — when the topic could plausibly belong to multiple sessions or no session is obvious, ask the user:

   ```text
   This topic could belong to:
   1. week 3 lecture (topic: logistic regression; cross entropy)
   2. week 4 lecture (topic: softmax; performance metrics)
   Which session should it link under? [1/2/both]
   ```

### Link format

Under the session heading, after the existing content, add:

```markdown
- [topic name](topic%20name.md)
    - topic name / [§ section heading 1](topic%20name.md#section%20heading%201)
    - topic name / [§ section heading 2](topic%20name.md#section%20heading%202)
```

List every section that session's material created or expanded, not the whole note; a file link alone is never enough. Anchors are the heading lowercased with `%20` for spaces and colons removed (`## Main memory` → `#main%20memory`), never dash-slugs.

Omit the indented section links if the topic has no `##` sections (single-section notes).

## References

- `create-flashcards` flashcard markup patterns
- `humanizer` verbosity pass over new prose and flashcards (see "Humanizer pass" in `academic-ingest`)
- `academic-lint` validation
- `academic-crud-transcludes` full Wikipedia article inclusion
- `academic-crud-topic-note/find_wikipedia.py` canonical title discovery script
