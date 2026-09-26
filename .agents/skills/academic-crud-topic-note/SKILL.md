---
name: academic-crud-topic-note
description: Create, read, update, and delete standalone topic notes (<topic>.md) for concepts, theorems, and lecture content under special/academia/<INSTITUTION>/<COURSE>/.
---

# Academic CRUD: Topic notes

Topic notes are concept-focused pages, like compact encyclopedia entries, with explanatory prose and section-local flashcards.

## Target

`special/academia/<INSTITUTION>/<COURSE>/<topic>.md`

## Topic note naming

The filename stem and the H1 title are the __same string__, written in __sentence case__ (capitalize only the first word plus genuine proper nouns, eponyms, and acronyms), and both are the canonical Wikipedia article title for the concept.

Naming runs before scaffolding, because renaming a note afterwards also means fixing every link to it in the course `index.md`. It applies when:

- Creating __any__ topic note, not only Wikipedia-sourced ones.
- Creating a `transcludes/` entry for full Wikipedia content (see `academic-crud-transcludes`).
- Verifying the canonical title or spelling of a concept before adding aliases.

__Why it needs its own step:__ the `header_style` lint rule starts at heading level 2, so it never checks an H1 title, and no rule inspects filenames. A title-case name passes validation silently and can only be caught here.

### Naming rules

- Sentence case, not title case: `operating system`, not `Operating System`.
- Prefer the Wikipedia form and number: `operating system`, not `Operating Systems` or `operating systems`.
- Keep the casing of proper nouns, eponyms, acronyms, and product names: `Boolean algebra`, `Kirchhoff's circuit laws`, `Lisp`, `Scala 3`, `H-bridge`.
- Hyphenation follows Wikipedia: `pulse-width modulation`.
- When Wikipedia has no article for the concept, invent a sentence-case descriptive title and record it as an alias.
- Aliases: the canonical title first, then synonyms and abbreviations.
- The path-derived flashcard tag mirrors the filename: spaces and quote characters become `_`, and every other character stays literal, parentheses included. `cache (computing).md` in `COMP 3511` needs the tag `flashcard/active/special/academia/HKUST/COMP_3511/cache_(computing)`; never normalize or strip the parentheses.

| Correct | Wrong |
| --- | --- |
| `operating system` | `Operating System` |
| `introduction to operating systems` | `Introduction and OS Structures` |
| `pulse-width modulation` | `Pulse Width Modulation` |
| `Kirchhoff's circuit laws` | `Kirchhoffs Circuit Laws` |

Filenames on disk contain literal spaces (`operating system.md`); links encode those spaces as `%20` and keep every other character literal: `- [cache (computing)](cache%20(computing).md)`.

### Discovering the canonical title

```bash
# Search for articles matching a query (default: 3 results)
uv run python .agents/skills/academic-crud-topic-note/find_wikipedia.py "Fourier transform"

# Limit results
uv run python .agents/skills/academic-crud-topic-note/find_wikipedia.py --limit 3 "Bayes theorem"
```

`find_wikipedia.py` searches Wikipedia and returns canonical titles, URLs, and short descriptions. It finds the exact article title (avoiding redirects and disambiguation pages), gives the canonical spelling of a technical term, and surfaces related articles. Use the returned canonical title verbatim as both the filename stem (`<topic>.md`) and the H1 title (`# <topic>`).

### Mapping output to frontmatter

The canonical title is the primary alias, followed by synonyms and abbreviations:

```yaml
aliases:
  - Fourier transform
  - Fourier analysis
  - DFT
```

Aliases exist for search, not for linking. Notes link to each other by relative path, so a duplicate alias across notes is normal and never a defect.

## Grouping: concepts, not source layout

File and section boundaries come from the concepts, never from the shape of the ingested material. A deck, a chapter, a page range, and a lecture are delivery formats, not concepts: they determine what content exists, never how it is grouped or named.

### Files are concepts

- A note is a concept with a canonical title and a body that stands on its own, never a source unit.
- Never name or bound a file after its source: no `lecture 3`, `chapter 1`, `part 2`, `slides 20-37`, `introduction`, `definitions`, `misc`, `other topics`, or `summary`.
- __Merge test__: one note when the parts share a single canonical title, when neither can be explained without the other, or when they are one concept seen from two angles (a mechanism and its motivation or failure modes).
- __Split test__: separate notes when they answer different canonical-title questions, when their prerequisites differ, or when their sections would not cohere under one concept. Independent linkability supports the decision but never decides it.
- __When the tests conflict, the canonical-title test decides.__ One canonical title means one note; that another note might link to a section does not by itself justify a file, or every section would become one.
- Regrouping moves boundaries but never drops facts: every source fact lands in exactly one note, with its flashcards.
- The file set has no order. Teaching order lives only in the course `index.md`: the `## overview` topic-to-file mapping and the session entries.
- New material about an existing concept routes to Update (see Create below). A source never produces a file named after itself, and a five-concept source produces five notes, not one lecture summary.

### Sections are sub-concepts

- A `##` heading names a sub-concept of the note's own concept, in sentence case, never a source unit, slide title, page number, or source-structural label.
- Rename every source heading to the sub-concept it carries: `Why Does Caching Work? - Locality` → `locality of reference`, `a bit history` → `history and adoption`.
- A section must not restate the note's own concept: `## caching` inside `cache (computing)` or `## hierarchy of storage` inside `memory hierarchy` repeats the H1. Give the section a genuine sub-aspect the title does not already claim, or drop the heading and keep the material as the note's unheaded intro prose with its flashcard block.
- Section boundaries may cross source boundaries in both directions: merge material that answers one question, split material that answers several.
- Lecture apparatus is never a section: objectives, outline, recap or summary, announcements, references, and question lists belong to the course `index.md`.
- The sections must partition the concept: each answers one question, along parallel axes, with no leftover other section.
- Order sections by the concept's own logic (definition, then mechanism, then variants, limits, and examples). Coinciding with the source's order is fine; the source's order is never the justification.

### Prose and cards are organized by the note

The principle reaches inside a section. Paragraph order, the grouping of list items, and the slicing of cards belong to the note, not the material: a source's sequence and the boundaries it draws are inputs, never a structure to reproduce.

- Regroup a flat list by whatever property separates its members, and move a fact to the paragraph where it belongs, even when the source presented it elsewhere.
- Slice enumerated answers at a boundary the note names on the prompt side, not necessarily one the material shows (see "Enumeration cards" in `create-flashcards`).
- Reorganizing only moves boundaries: every fact stays in the note, and no statement may claim a grouping the material contradicts.

### Nesting is always decided

Decide nesting explicitly while planning the note. Do not inherit the source's depth. Nesting is the default and flat is the outcome that needs a reason: a heading is what makes a sub-concept linkable, card-bearing, and skippable on a second reading.

- __Nest__ (`###`) as soon as a section carries two or more nameable sub-concepts: classification members, per-case breakdowns (modes, models, layers), separate derivations or worked examples, or sub-topics a reader would link to on their own. Prefer the split even when each sub-concept is short.
- __Tiebreaker: count what the sub-concept owns, not how long it is.__ One card plus a sentence of its own prose earns a `###`, and so does a named member of a classification. Keep it inside the parent only when it owns neither: a clause inside another sub-concept's sentence, an example told within it, or a card with no prose of its own to head. Three one-card variants that each explain themselves are three headings, not one flat list.
- __Stay flat__ when the section carries no sub-concepts at all, when nothing inside it earns a heading under the tiebreaker, or when everything that does is a parallel one-sentence row of a single mapping, enumeration, or table. Those rows are card slices, not headings. A lone `###` is fine while the parent keeps substance of its own beside it, and folds back when it is the parent's whole content. "The material presented them together" is never the reason.
- __Depth__: `###` freely. A `###` that carries its own two or more sub-concepts (the members of its classification, the cases of its rule, the steps of its derivation) nests to `####` rather than flattening or splitting, justified inline with `<!-- check: ignore-line[header_deep_nesting]: <reason> -->`. Splitting the note is for material that answers a different canonical-title question, not for material that is merely one level deeper.
- `#####` and deeper are unsanctioned: they mean the file boundary is wrong, so split the note instead.
- Every `###` and deeper carries its own `---` separator and its own `Flashcards for this section are as follows:` block, recursively. The validator requires a card block under every heading a non-index note carries, the other half of the tiebreaker.

### Section levelling pass

Nesting is planned before the note is written and reviewed after it. The pass runs over every section the ingestion created or touched, and it is the only place a heading may change: the humanizer pass treats heading text as frozen, because session entries link to its anchor.

- __Promote.__ Give a sub-concept its own `###` when it earned one under the tiebreaker, including a second nameable sub-concept sitting inside a section that also carries another.
- __Fold.__ Drop a section that restates the note's own H1, a lone `###` that is its parent's whole content, and a section the note's concept does not contain. Material whose owning concept lives in another note is moved to that note.
- __Re-level.__ Move a heading up or down rather than leaving it at the level the source showed; depth follows the concept's own structure, never the source's.
- __Re-home the prose with the heading.__ A heading that moves takes its prose and its card block; a heading that folds merges them into the parent's. The validator requires a card block under every heading, so no block is left without one or split across two.
- __Refresh the links.__ Renaming, moving, or removing a heading invalidates every session-entry and appendix anchor that pointed at it. Fix them in the same task (see "Session outline content: sections, not files" in `academic-crud-course-index`).

The pass moves boundaries and headings; it never drops a fact or a card. Report the card count before and after, because the count feeds the `Flashcards-now` commit trailer.

## CRUD operations

### Create

1. __Determine the canonical title:__ run `find_wikipedia.py` and take the canonical article title verbatim as the filename stem and the H1 title (see "Topic note naming" above). Do this first, because renaming later means fixing links in the course `index.md` too.
2. __Classify the incoming content:__ a duplicate of an existing note routes to Update rather than Create, an enhancement of an existing note also routes to Update, and only a new concept creates a new note.
3. __Extract the content structure:__
   - Key concepts, definitions, formulas, derivations
   - Examples, counterexamples, worked problems
   - Teaching caveats, distinctions, classifications
   - Mathematical spine: formula + derivation + intuition + worked example
   - The drawings the concept is defined by (a symbol, a convention, a construction), attached as SVGs and embedded per `academic-crud-attachments`
   - The file boundary: one concept, per the merge and split tests in "Grouping: concepts, not source layout"
   - The sections and their nesting (`###` for each sub-concept that owns a card and a sentence of its own, `####` where a `###` carries sub-concepts of its own, see "Nesting is always decided"), never mirroring the source's headings or depth
4. __Scaffold the note file:__

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

5. __Generate flashcards:__
   - Use `::@::` (two-sided QA), not cloze `{@{ }@}`. Accounting journal-entry worked examples may use cloze.
   - Every `##`, `###`, and deeper heading gets its own `---` separator and its own flashcard block, never one block shared by a parent and its sub-sections.
   - Group related cards with inline bold labels (e.g., `**superposition.**`).
   - Cards must be self-contained (restate givens, hypotheses, notation) and never name their source; write the example, not `the lecture's example`.
   - The overview card comes first in each section.
   - Preserve the derivation or proof spine in cards.
   - Split packed cards into focused units, and split an enumeration of six or more items into sibling cards sliced at a boundary the items show (era, date range, divergence versus curl), each naming its slice on the prompt side (see "Enumeration cards" in `create-flashcards`).
   - Calculation cards must name every quantity they combine on the prompt side (e.g. `$\text{hit ratio}$`, `$\text{hit time}$`) so the card is answerable in isolation. Rewrite a two-sided card this way before reaching for a suppression (`two_sided_calc_warning`).
   - The lint suppression `<!-- check: ignore-line[two_sided_calc_warning]: conceptual -->` applies to math cards only when the card is genuinely conceptual rather than computational.
   - Use `<p>` for paragraph breaks in single-line source, and `__` for bold, never `<b>`/`</b>`.
6. __Figures and diagrams:__
   - When the source carries figures the prose depends on (slide diagrams, schematics, plots), extract the document per "Document extraction (mandatory)" in `academic-ingest`.
   - Read a figure from `.extracted/images/`, not the 150 DPI page render in `.extracted/pages/`; the render is downscaled and hides the labels. Crop and upscale when the figure is still unclear.
   - Default to text: transcribe a figure's labels, values, and steps into the prose, or into a Markdown table when the figure is tabular. Describe it for the point it makes in the section rather than listing what the picture contains.
   - Attach a graphic only when the picture itself is the material, and never attach a page render. Copy the embedded image into `attachments/` under a descriptive name (`attachments/lob_depth_diagram.png`, not `attachments/pages/.../page_007.png`).
   - Reference each attached graphic from the section that uses it: `![<alt text>](attachments/zener_circuit_q1.jpg)`. Alt text is plain language describing what the figure shows, never LaTeX.
   - Follow "Page image handling" in `academic-ingest` for what may and may not be asserted about an image. Leave `.extracted/` alone; it is a cache, not an attachment source.
7. __Section levelling pass:__ re-review the written sections against "Nesting is always decided" and re-level them, then fix the anchors the review invalidated (see "Section levelling pass" above).
8. __Update the course index:__
   - Read `special/academia/<INSTITUTION>/<COURSE>/index.md`.
   - Add the topic note to `## children` in its sorted position: folders first, then files, Python string order within each group (see "Children format" in `academic-crud-index`).
   - Determine which session heading the topic belongs to (e.g., `## week 3 lecture 1`, or `### 2026 fall week 3 tutorial 1` in a recurrent course) using the session mapping rules below, and __ask the user__ when it is unclear.
   - Under the matched session heading, add a link to the topic note with section anchors for each `##` section this session's material created or expanded; a file link alone is never enough:

     ```markdown
     - [topic name](topic%20name.md)
         - [§ section heading](topic%20name.md#section%20heading)
     ```

   - If the topic spans several sessions, add links under each, listing only the sections that session's material covered.
9. __Humanizer pass:__ sweep the prose and flashcards separately before validating: H1 intro and section prose first, then card prompts and answers (see "Humanizer pass" in `academic-ingest`).
10. __Validate:__ run `academic-lint` on the created file.

### Read

List topic notes for a course; search by keyword; show structure and flashcard count.

### Update

1. __Reconcile the material against the note.__ Compare what the session carried (a lecture deck, a lab manual, a tutorial handout, a problem set) against the concepts the note already owns, then extend it, prune what the material supersedes, or record the concept as already covered (see "Topic-note reconciliation (mandatory)" in `academic-ingest`). Watch for overlap as you go: a new distinction, example, or counterexample belongs inside the section that owns the idea, and a new card beats an overstuffed old one.
2. Level the sections this update touched (see "Section levelling pass").
3. Run the humanizer pass over the prose and the cards that changed (see "Humanizer pass" in `academic-ingest`).
4. Refresh the course `index.md`: a renamed topic changes `## children`, and added, removed, or renamed sections change the session topic links. Re-verify the session mapping when the topic's scope has moved.
5. Validate after changes.

### Delete

Remove the note file, drop it from the course `index.md` `## children`, strip its topic links out of every session heading that carried it, and fix the cross-references in the notes that linked to it. Then validate.

## Missing data

Use `\[missing\]` for absent values, such as a topic with no cross-references or a section with no formula (see [special.instructions.md](../../instructions/special.instructions.md#missing-data)).

## Style conventions

- Lowercase headings except proper nouns (use `<!-- check: ignore-next-line[header_style]: proper noun -->`).
- A `##` heading must not repeat the note's own H1 title (MD024). Merge that section's prose and flashcards into the unheaded intro under the H1 instead of renaming the heading.
- `_italic_` and `__bold__`, not `*`/`**`.
- Keep KaTeX `$...$` (inline) and `$$...$$` (block) intact on one source line. A `$$...$$` block must share its line with the surrounding prose, never stand alone (`latex_not_standalone`).
- Ordinals: `$k$-th`, not `$k$th` (LaTeX renders without the hyphen literally).
- Distribution names: `\operatorname{Bin}`, `\operatorname{Exp}`, `\operatorname{Poi}`, etc.
- Indicator functions: `\mathbf 1_A(x)` or `\mathbb 1_A(x)`.
- Multi-letter operators: `\operatorname{Var}`, `\operatorname{Cov}`, `\operatorname{E}`, `\operatorname{MSE}`.
- Left and right limits: `\lim_{y\uparrow m}`, `\lim_{y\downarrow m}`.
- "Distributed as": `\sim` (e.g., `$X\sim N(0,1)$`).
- Binomial coefficients: `\binom{n}{k}`.
- No source numbering (theorem, definition, or chapter numbers); use topic names.
- Never narrate the source: no `the deck`, `the slides`, `the lecture`, or `the course` as a subject, and no reporting what a source shows, asks, or stresses. State the fact, example, or question itself (see "Scope guardrails" in `academic-ingest`, rule __Write the content, not the material__).
- `## references` lists its sources as list items, never as prose paragraphs. Licence, attribution, and any other source detail are nested bullets under the entry they qualify.

    ```markdown
    ## references

    - Walker, M. (2020). [How sleep affects your emotions](https://www.youtube.com/watch?v=6F8wFkScnME) [Video]. TED.
        - Source of the material on emotional reactivity under sleep loss.
        - Part of the _Sleeping with Science_ series.
    ```

## Subject-specific guidance

### Technical/mathematical notes

- Default bundle: formula + derivation + intuition + worked example.
- Compare commonly confused concepts explicitly (e.g., message vs signal, energy vs power).
- Name analogies to classical mathematics (discrete Dirichlet problem, maximum principle).
- Add proof sketches for non-obvious statements.

### Honors/proof-heavy courses

- State hypotheses explicitly.
- Prefer short derivation or proof sketches over bare theorem statements.
- Include concrete examples and counterexamples.
- List equivalent formulations explicitly.

### Machine-learning notes

- Derive formulas; separate estimation from decision.
- Make assumptions explicit (IID, priors, thresholds, intercept conventions).
- Distinguish the true distribution $P$ from the model distribution $Q$.
- Distinguish L2 regularization from weight decay.
- Explain why the empirical loss carries the $1/N$ factor.
- Pair the forward layer equation with composition and backward views.

### Physics/electronics/lab notes

- Define jargon near first use ($V_{CC}$, $V_{CE}$, "low-side switch").
- Give circuit topology, polarity, and loop direction in cards.
- Embed the drawing itself for each symbol and convention (`attachments/`, see `academic-crud-attachments`), then card it both ways: recognition (drawing shown) and recall (drawing asked for), per `create-flashcards`.
- For signal processing, explain the chain stage by stage.

### Accounting notes

- Put journal-entry examples inside topic sections, not a separate collector.
- Each scenario in a blockquote: scenario → Dr/Cr table → explanation.
- Cloze in quoted scenarios, tables, and calculations.
- Table: right-aligned Dr/Cr columns, `&nbsp;` thousands separator.
- Warranty examples allow settlement credits (Cash, Inventory, Accrued Payroll).

## Session mapping

When updating the course `index.md`, link topic notes under the session heading that course already uses: `## week N <type> <N>`, or `### <YYYY term> week N <type> <number>` in a recurrent course.

### Determining the correct session

1. __Input metadata__: the PDF filename, Canvas assignment title, or user-provided context often names the session ("lecture 5", "tutorial 3").
2. __Topic content__: match the topic's subject matter to the session's `topic:` line in the index.
3. __User input__: when the topic could plausibly belong to several sessions, or to none, ask:

   ```text
   This topic could belong to:
   1. week 3 lecture 1 (topic: logistic regression; cross entropy)
   2. week 4 lecture 1 (topic: softmax; performance metrics)
   Which session should it link under? [1/2/both]
   ```

### Link format

Add the link under the session heading, after the existing content:

```markdown
- [topic name](topic%20name.md)
    - [§ section heading 1](topic%20name.md#section%20heading%201)
    - [§ section heading 2](topic%20name.md#section%20heading%202)
```

List every section that session's material created or expanded, not the whole note; a file link alone is never enough. The anchor format and the `link_anchor_slug` rule that checks it are in "Session outline content: sections, not files" in `academic-crud-course-index`.

Omit the indented section links when the topic has no `##` sections.

## References

- `create-flashcards` flashcard markup patterns
- `humanizer` for the AI-writing patterns it removes
- `academic-lint` validation
- `academic-crud-transcludes` full Wikipedia article inclusion
- `academic-crud-topic-note/find_wikipedia.py` canonical title discovery script
