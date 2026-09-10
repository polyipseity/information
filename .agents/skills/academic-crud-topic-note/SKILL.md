---
name: academic-crud-topic-note
description: Create, read, update, and delete standalone topic notes (<topic>.md) for concepts, theorems, and lecture content under special/academia/<INSTITUTION>/<COURSE>/.
---

# Academic CRUD: Topic notes

Create, read, update, and delete standalone topic notes. These are concept-focused pages, like compact encyclopedia entries, with explanatory prose and section-local flashcards.

## Target

`special/academia/<INSTITUTION>/<COURSE>/<topic>.md`

## CRUD operations

### Create

1. __Classify incoming content:__
   - Duplicate of existing note → do not create; route to Update
   - Enhancement of existing note → route to Update
   - New concept → create new note

2. __Extract content structure:__
   - Key concepts, definitions, formulas, derivations
   - Examples, counterexamples, worked problems
   - Teaching caveats, distinctions, classifications
   - Mathematical spine: formula + derivation + intuition + worked example

3. __Scaffold note file:__

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
```

1. __Flashcard generation:__
   - Use `::@::` (two-sided QA) format — NOT cloze `{@{ }@}`
   - Exception: accounting journal-entry worked examples may use cloze
   - Each section AND subsection gets its own flashcard block
   - Group related cards with inline bold labels (e.g., `**superposition.**`)
   - Cards must be self-contained (restate givens, hypotheses, notation)
   - Overview card as first card in each section
   - Preserve derivation/proof spine in cards
   - Split packed cards into focused units
   - Lint suppression: `<!-- check: ignore-line[two_sided_calc_warning]: conceptual -->` on math cards
   - `<p>` for paragraph breaks in single-line source
   - No `<b>`/`</b>` — use `__` for bold

2. __Update course index:__
   - Read the course `index.md` (`special/academia/<INSTITUTION>/<COURSE>/index.md`)
   - Add the topic note to `## children` in alphabetical position among topic notes (after `assignments/`, `questions/`, `AGENTS`, and other non-topic entries)
   - Determine which session heading the topic belongs to (e.g., `## week 3 lecture`). Use the session mapping rules below. If the session is unclear from the input, __ask the user__ which session(s) the topic should be linked under.
   - Under the matched session heading, add a link to the topic note with section anchors for each `##` section:

     ```markdown
     - [topic name](topic%20name.md)
         - topic name / [§ section heading](topic%20name.md#section%20heading)
     ```

   - If the topic spans multiple sessions, add links under each relevant session

3. __Validate:__ run `academic-lint` on the created file.

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

Use `(none)` for absent metadata — for example, when a topic has no cross-references or a section has no formula. See [special.instructions.md](../../instructions/special.instructions.md#missing-data).

## Style conventions

- Lowercase headings except proper nouns (use `<!-- check: ignore-next-line[header_style]: proper noun -->`)
- `_italic_` and `__bold__` (not `*`/`**`)
- KaTeX `$...$` (inline) and `$$...$$` (block) intact, on one source line
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

Omit the indented section links if the topic has no `##` sections (single-section notes).

## Wikipedia title discovery with `find_wikipedia.py`

When creating topic notes from Wikipedia content, use `find_wikipedia.py` to discover canonical article titles. This ensures consistent naming and proper linking.

### What it does

`find_wikipedia.py` searches Wikipedia for articles matching a query and returns canonical titles, URLs, and short descriptions. It helps you:

- Find the exact Wikipedia article title (avoiding redirects and disambiguation pages)
- Discover related articles you may not have considered
- Get the canonical spelling of technical terms

### When to use

- Creating a topic note that summarizes a Wikipedia article
- Creating a `transcludes/` entry for full Wikipedia content (see `academic-crud-transcludes`)
- Verifying the canonical title of a concept before creating aliases

### How to use

```bash
# Search for articles matching a query (default: 5 results)
uv run .agents/skills/academic-crud-topic-note/find_wikipedia.py "Fourier transform"

# Limit results
uv run .agents/skills/academic-crud-topic-note/find_wikipedia.py --limit 3 "Bayes theorem"
```

### Mapping output to frontmatter

The canonical title from `find_wikipedia.py` should appear in your topic note's `aliases` list:

```yaml
aliases:
  - Fourier transform
  - Fourier analysis
  - DFT
```

Use the canonical title as the primary alias. Add synonyms and abbreviations as secondary aliases.

## References

- `create-flashcards` flashcard markup patterns
- `academic-lint` validation
- `academic-crud-transcludes` full Wikipedia article inclusion
- `academic-crud-topic-note/find_wikipedia.py` canonical title discovery script
