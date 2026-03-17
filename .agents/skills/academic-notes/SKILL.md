---
name: academic-notes
description: Content conventions, examples, and tooling for course notes under special/academia.
---

# Academic notes — consolidated skill

This document explains how to author, validate, and maintain academic course notes stored under `special/academia/<INSTITUTION>`. Agents and human authors **must read every line of this file** before editing course material, since the rules below are exhaustive and are enforced by the validator script. Flashcards are generated automatically by the build system; do **not** run `init generate` yourself.

## Key principles

1. **Content first**: capture every slide bullet, formula, definition, wor/ked example and instructor comment as prose or hierarchical bullets. Err on the side of completeness; extra detail helps recall and tooling filters out noise. When in doubt include more rather than less.
2. **Automatic flashcards**: add flashcard markup (`{@{ }@}`, `::@::`, `:@:`) whenever you add new factual material. Update cards whenever you expand or revise a section, and treat prose and flashcards as one unit of maintenance: if you add, remove, split, merge, or rename topic-note content, revise the corresponding flashcards in the same edit rather than leaving them behind. Generators run in CI; agents must never invoke them.
   - Treat every flashcard as a standalone artifact. A reviewer may encounter it without the surrounding paragraph or neighbouring cards, so repeat any local hypotheses, notation, or conditions that are necessary for the statement to be correct (for example $f\colon\Omega\to[0,\infty)$, $P[B]>0$, “without replacement”, or which random variable is being counted).
3. **Structured metadata**: every file starts with a `---` YAML block. Use ISO‑8601 datetimes, maintain `children:` lists in indexes, add activation tags (`flashcard/active/special/academia/...`), and keep semester headings chronological. The validator enforces these rules and will report any violations as errors.
   - The validator’s output now includes the exact line (and column when available) where a problem was detected, along with a short preview of the offending line, making it much easier to locate and fix issues quickly. The preview highlights the precise column range using carets (`^`), and long lines are truncated with ellipses so the marker remains in view. The length of the snippet is automatically limited to fit within your terminal width (accounting for the leading `preview:` indentation).
4. **Session ordering**: lectures/labs/tutorials ordered by the `datetime:` interval; all exams go after regular sessions. Duplicate week numbers around holidays require manual renumbering plus a no-class entry; use `status: public holiday: <name>` when the holiday is known, or `status: no class` for breaks. Omit `topic:` on no-class days. Entries with `status: unscheduled` must omit `topic:`.
5. **Continuous improvement**: record new rules, bugs, or user preferences in `continuous_improvement.md` and update this document accordingly. Feedback drives evolution of the skill; see the **Continuous improvement** section below for the full workflow.
6. **Math formatting**: never place math in fenced code blocks. Use LaTeX inline (`$…$`) or display (`$$…$$`) notation for all formulas; this applies equally to examples in topic notes and session outlines. **Exception — accounting courses:** do **not** use LaTeX in accounting notes; use plain text, plain numbers, and plain symbols (e.g. ×, −, ÷) for formulas and amounts.
   - **Dollar delimiters only.**  Do not use `\[`, `\]`, `\(` or `\)`; all LaTeX must be wrapped in `$…$` or `$$…$$`.
   - **One line only.**  Whether inline or display math, the source between the delimiters must not contain a newline.  In particular, display formulas must use `$$` but stay on a single markdown line.
   - **Never standalone.**  A line consisting solely of a math expression is forbidden; the formula must be embedded in surrounding prose or list text.  This keeps diff noise down and matches the flashcard generator’s expectations.
   - **Spacing around delimiters.**  When an equation appears after other text, leave a normal space before the opening dollar sign; likewise put a space after the closing dollar if more text follows.  **Exception:** no space is required if the character immediately following the closing dollar is punctuation (e.g. `.,;:!?)]}`) or the end of line.  Leading or trailing whitespace is allowed at the beginning or end of a paragraph, but adjacent alphanumeric characters without a space will trigger the validator.
7. **Header style**: section headers in topic notes should be all lowercase (capitalize only proper nouns or the first word of a sentence) to keep anchors predictable and maintain consistency.
8. **Markdown emphasis**: use underscore for italic and bold in course notes: `_italic_` and `__bold__` (not `*`/`**`). This keeps formatting consistent and avoids asterisk collisions with list or math. Do **not** put LaTeX inside emphasis; it may not render correctly—keep math outside `_..._` and `__...__` (e.g. _phrase_ on $math$, not _phrase $math$_).
9. **Immediate validation**: run `uv run .agents/skills/academic-notes/check.py` after every editing tool invocation or manual change. The agent tends to produce malformed Markdown, and fixing issues promptly prevents a flood of errors later.
10. **Honors courses**: when a course is marked as an honors version (for example, aliases or the course name include “Honors” such as “Honors Probability”), treat its notes as mathematically rigorous references: think carefully and thoroughly about the underlying theory before editing, include clear arguments or derivations (or proof sketches) for important results instead of bare statements, split long reasoning into a few logically separate paragraphs rather than one over-dense block, and favour more detailed, conceptually rich flashcards over minimal ones. For structural results like the law of total probability and Bayes' theorem, explicitly spell out hypotheses (for example what it means for $(B_j)$ to be a partition of $\Omega$) and include short derivation sketches both in the prose and in a small cluster of cards that distinguish the statement from the key proof idea.

## Authoring workflow

This section covers the full lifecycle of course note content, from initial creation through final checks before committing. Start here whenever you need to add or revise material.

1. Start with `course-template.md`. Fill aliases (singular, plural, concatenated), tags (include underscore course code), course name, credits, and a brief description. Sort aliases alphabetically.
2. Add a `logistics` section with `scheme:` weights and a nested `sections:` list. For lectures (and similarly tutorials/labs), use a single key for the _chosen_ section (e.g. `lecture: L1`); under that key list all section identifiers and their details (e.g. L1, L2, L3 each with venue and weekly time pattern). Do not repeat separate `lecture: L2`, `lecture: L3` keys—one block per stream type with every section’s details nested under the chosen section key.
3. Maintain a `children:` list with lectures, labs, assignments, topics, questions, attachments; keep entries in teaching order and update it whenever you add a new page.
4. Use the session structure from the examples below. Add `datetime:` entries with ISO intervals (date only if time unknown). Place prose summaries after the bullet outline separated by `---`. Draft explanatory prose before adding cloze markup; don’t flashcard‑ify first and then write prose.
5. Capture content‑first details in prose paragraphs, not bullets; convert slide fragments into full sentences. When a lecture introduces a component type (e.g. integrated circuit) via a specific instance (e.g. LM7805), include explicit treatment of the general concept—definition, role, and how to use it (e.g. datasheet)—with flashcards; do not skip to the instance without defining the parent concept.
6. Audit the whole file whenever you add or change any section: check for missing/malformed flashcards, separators, numeric values, tags, and indentation.
7. If the file is a topic note referenced from a course index, audit the relevant `index.md` entries in the same pass: update section links, anchors, and link text whenever you add, remove, split, merge, or rename headings.
8. Run the validator and fix any errors it reports; do this immediately after each edit tool call or manual change. Errors (and warnings) must be resolved before committing.

### Adding new lecture content (ingestion)

When ingesting content from a new lecture (e.g. transcript or slides), **before creating new topic notes or new sections**, decide how the new material relates to existing notes:

1. **Duplicate**: If the new content substantially duplicates an existing topic or section, **do not add a new note**. Add a **section link** from the session in the index to the relevant existing section (e.g. `[§ section name](existing-note.md#anchor)`). No new file and no duplicate prose.
2. **Enhancement**: If the new content extends, clarifies, or deepens existing material, **enhance the existing note**: add or revise prose in the relevant section, and add or update flashcards there. Then add **section links** from the session to those sections. Do not create a separate “part 2” note for the same topic.
3. **New**: Create a **new topic note** (and new journal-entry sections if applicable) only when there is **no or little overlap** with existing notes—i.e. the lecture introduces a distinct concept that does not already have a suitable home.

This keeps the knowledge base single-source: one place per concept, with the index and § links directing learners to the right section. When in doubt, prefer enhancing an existing note and adding section links over creating another note that overlaps.

### Pre‑commit checklist

Before committing any new or changed course note, run through these items.  This checklist complements the authoring steps above and ensures metadata, chronology, and flashcards are all in place.

- YAML frontmatter present and delimited by `---` at the top of the file.
- `aliases` include canonical course code(s) and human-readable names; tags include `flashcard/active/special/academia/<institution>/<course code>/<page>` and where appropriate `function/index` and `language/in/English`. `<page>` mirrors the relative path to the course folder with underscores and should not be percent‑encoded. Validators flag missing or malformed tags; report missing tags in review rather than bulk-editing existing files.
- Do **not** create, modify or edit files under `general/` – only work inside the course folder.
- Index files: `# index` header and a `## children` list or `children:` YAML key with child pages in teaching order (folders first). After the course list (e.g. `- name:`, `- credits:`) insert a horizontal rule `---` before the course description paragraph. Use ISO datetimes for week entries and ensure they have `datetime` and, unless the session is a no-class day or `status: unscheduled`, `topic`.
- Check that lecture/lab/tutorial entries are chronological and exams are placed last. **Run the validator only on the specific course directory you are editing rather than the entire institution tree** (e.g. `uv run .agents/skills/academic-notes/check.py special/academia/HKUST/ELEC\ 1100`); running it on `special/academia/HKUST/` will produce too many unrelated errors. Fix any errors returned.
- Ensure every Markdown section in a topic note contains flashcard entries (a rubric introduced by “Flashcards for this section are as follows:” preceded by `---`, with two-sided or one-sided cards; topic notes other than journal entries do not use inline clozes). The validator flags missing cards. Index and questions pages (e.g. `questions.md`) are not topic notes and do not need that rubric.
- Add assignments, questions, attachments under appropriate subfolders and list them under `children`.
- Link to canonical `general/` pages instead of copying long definitions; percent-encode spaces in paths. When a concept deserves its own course note, follow the topic‑specific notes workflow below.
- Filenames are friendly and human‑readable; use spaces and percent‑encode them in links.
- Run `bun run format`, `bun run check` (with `--no-globs` and explicit paths), and `bun run test` locally before committing.
- Use `assignments/`, `questions/`, and `attachments/` subfolders for respective content.
- Do **not** include instructor or TA names or email addresses in course notes; refer readers to the official syllabus or LMS (e.g. Canvas) for contact. Office hours (day, time, format such as "or via Zoom") may be included in logistics.
- Include venue lines immediately after `datetime:`; apply the HKUST room interpretation rule if appropriate (numeric rooms → “Room ####, Academic Building”).
- Add at least one worked example or solution sketch for important techniques and sample exam‑style problems linked to `questions/solutions.md`.
- Record lab/tutorial section identifiers near the top of the note so tooling can filter irrelevant streams.

### Session and index rules

- **Course index structure**: After the course list line(s) (institution, `name:`, `credits:`), add a horizontal separator `---` before the course description. The description and “The content is in teaching order.” follow the separator.
- **Logistics sections**: Under `sections:`, use one key per stream type for the _chosen_ section only (e.g. `lecture: L1`). Under that key list every section’s identifier and details: e.g. `L1: <venue>; <times>`, `L2: <venue>; <times>`, `L3: <venue>; <times>`. All sections are documented under the single chosen-section key; do not add separate `lecture: L2`, `lecture: L3` siblings.
- **Session heading format (strict)**: Only `## week N type [number]` is allowed (_type_ = `lecture`, `lab`, or `tutorial` only (status has no bearing on heading); number optional when one per week). Examples: `## week N lecture` and `## week N lecture 2` (use a space in “lecture 2”); same pattern for `lab`/`tutorial`. Number resets each week. Use the same heading as the scheduled slot (e.g. `## week 3 lecture`) and put no class or holiday only in metadata (`status: public holiday: …` or `status: no class`). `## week 3 no class`, `## week 3 (Lunar New Year)`, or `## week 3` with no type are invalid. If a week is repeated due to holidays, shift subsequent weeks upward and add a no-class entry (see below).
- Session metadata: `datetime:` ISO_START/ISO_END[, DURATION]; `topic:` short text for normal sessions. Omit `topic:` for no-class days (holidays, breaks). Use `status: public holiday: <name>` when the public holiday is known (e.g. `status: public holiday: Lunar New Year`, `status: public holiday: Labor Day`); use `status: no class` for other non-teaching days (e.g. midterm break). Entries with `status: unscheduled` must omit `topic:`.
- Optional `venue:` on every session when known.
- **Index session flashcards**: Session-level flashcard bullets in the index (e.g. “COURSE / Ch 12 introduction ::@:: …”) are optional. Omit them when they only describe scope or content coverage rather than testable knowledge; topic notes and questions pages remain the place for substantive flashcards. If in doubt, prefer no index session card over a scope-only one.
- Bullet items nested under a session hold course‑specific notes and cross‑links. Each top‑level bullet must sit on its own source line; use `<br/>` or `<p>` for internal breaks. Numeric examples should include units inside `$…$` math delimiters.
- When embedding a diagram or schematic image in prose, place the image markup (e.g. `<p> ![...](attachments/...svg)`) on the same line as the end of the preceding paragraph, not on a new line.
- Outline items correspond to flashcard glosses; avoid extra indentation levels. Convert generic headings into specific QA entries or remove them.
- After the outline, add a prose paragraph preceded by `---` only when it **adds value** (e.g. next-lecture pointer, grading or schedule reminders). Do not duplicate the same content as the index bullets and topic notes; keep session prose short or omit it if the outline and topic links already capture the content.
- Omit a **lecture summary** flashcard in the index unless it refers to **major grading components** (exams, project milestones); the outline and topic-note links already summarise the lecture.
- Semester headings in institution indexes must be chronologically ordered; validator warns otherwise.

Once the session outline rules are understood, the next section describes how flashcards themselves are formatted and how to tag them correctly.

## Flashcards and markup

The spaced‑repetition system is central to the entire repository; flashcards are automatically generated from your markup. These rules apply both within session outlines and inside longer topic notes, so master them early.

- Use three patterns only:
  - **Cloze deletions**: `{@{hidden text}@}` anywhere in a paragraph.
  - **Two‑sided QA**: single source line `term ::@:: definition` (produces two cards). Use `<br/>` or `<p>` for visible breaks; do not insert newlines.
  - **One‑sided QA**: single source line `term :@: answer` (one card).
- **Topic notes (except journal entries):** For course topic-specific notes (e.g. current liability, provisions, circuit laws), **do not use cloze** (`{@{ }@}`) in the prose. Use **two-sided** (::@::) cards only, or **one-sided** (:@:) very rarely. Add more QA flashcards to cover definitions, steps, and examples. Cloze is required only in **journal entries** for example amounts and scenario text (see § Journal entries note).
- Add a gloss by appending `::@::` after a linked term. The text after `::@::` becomes the card content; keep it concise, normally one or two sentences. Long derivations do not make good cards. When you lift sentences from prose or examples, also copy any adjacent diagrams or images into the question — cards with visual context are easier to learn and the validator will warn if an image appears in the source but not in the flashcard. It is fine to use LaTeX on **either side** of a card (left or right) as long as the usual math rules above are respected (no standalone math lines, dollar delimiters only, no newlines inside). In particular, do **not** paraphrase away equations or symbolic expressions just to avoid LaTeX on the left-hand side; if the natural prompt is mathematical, keep the mathematics there. However, for **multi-step derivations, approximations, or proof-outline flashcards**, prefer a descriptive left-hand label such as `Poisson approximation / factor limits` or `hypergeometric approximation / derivation strategy` rather than dumping the full target formula on the left; keep the formulas and step details on the right-hand side.
- Flashcards must be understandable in isolation. Do not rely on the preceding card, heading, or paragraph to supply a hypothesis; if the result needs conditions such as nonnegativity, independence, positivity of a probability, or a particular sampling scheme, restate them in the card itself.
- For notes that include schematic symbols or circuit diagrams, add **diagram‑recall flashcards** whose prompt embeds the image (e.g. `schematic symbol: resistor <p> ![resistor](attachments/symbol_resistor.svg) ::@:: …`). The answer should name the component and briefly state what the symbol represents; keep any math/symbols on the left as needed for validator rules.
- Prefer **single-focus cards**. If a card’s right-hand side explains multiple distinct ideas (e.g. definition + steps + conditions), split it into multiple smaller cards, each testing one concept. This improves recall and avoids “all-or-nothing” cards. For multi-step procedures (e.g. ON/OFF assumption methods, saturation checks, multi-step circuit analyses), prefer one card per 1–2 steps rather than a single “all steps at once” card, as long as each resulting card’s left-hand prompt still contains all givens needed to answer it.
- Prefix every gloss with the complete hierarchical path only when the surrounding page does **not** already supply enough context. In **topic-specific notes**, the flashcard viewer already shows the filename and the note itself already shows the title, so omit redundant filename/title text from top-level prompts: write `definition`, `probability space`, or `why sigma-additivity holds`, not `probability measure`, `probability measure / definition`, or `sample space / definition`. Use an explicit course-code prefix (`COURSE / topic / item`) only when you are writing **index/session-level cards** or other mixed-context pages where multiple courses or topics might otherwise collide. Do not rely on indentation for context; only the literal text is used by the flashcard viewer.
- For **nested flashcards in any academic-notes file** (not just course indexes), indent by exactly two spaces per level and make every nested QA prompt start with its full **in-file** parent path. For example, in `discrete distributions.md` write `- Poisson approximation` then `- Poisson approximation / statement ::@:: ...` on the next indentation level, rather than repeating `discrete distributions / ...`.
- For **approximation, derivation, or proof-outline clusters**, a descriptive step-name prompt on the left is still preferred, but the right-hand side should usually show the important mathematical expressions as well (for example the exact factorization being used, the key limit terms, or the target PMF) so the strategy is explicit rather than purely verbal.
- When grouping related cards, give the parent a full path label (e.g. `ELEC 1100 / class expectations`) and nest children beneath it.
- Calculation cards must be self‑contained: put all given values on the left and outline computation steps on the right. When applicable, include any relevant diagrams, circuit sketches, or images in the left‑hand prompt; the validator’s calculation warnings now remind you to copy such visuals if the answer side contains math but the prompt lacks data.
- Do **not** “shorten” calculation cards by removing givens from the left-hand side. If a worked example feels too long, split it into smaller cards only if each resulting card still includes all necessary givens to be solvable from the prompt.
- **Circuit and KVL examples**: When describing a circuit for a calculation (e.g. KVL, voltage divider), state the topology explicitly: component connections (what connects to what), source polarities (which terminal is +/−), assumed current direction or loop traversal, and node names. This makes the example answerable without a diagram.
- **Circuit prose clarity**: In topic notes, describe circuit topologies precisely. For divider-like or regulator circuits, specify the signal path (e.g. $V_{\text{in}} \rightarrow R_S \rightarrow \text{node} \rightarrow R_L \rightarrow \text{GND}$), component orientations (e.g. Zener cathode at node, anode at ground), and which elements shunt or limit current.
- **Circuit notation and topology terms**: When a lecture uses shorthand like $V_{CC}$, $V_{CE}$, $V_{BE}$, or terms like “low-side switch”, add a brief definition the first time they appear in that page (and optionally a flashcard). Example: $V_{CC}$ is the supply rail feeding the collector/load network; $V_{CE}=V_C-V_E$; “low-side” means the switch is between the load and ground. For transistor-as-inverter or similar logic-level topics, state how levels are determined (e.g. $V_C$ vs $V_E$) and keep math readable (avoid overly dense derivations); the same derivation need not appear in both the index and the topic note.
- Units must always be inside `$…$` or `$$…$$` (e.g. `$5\text{ V}$`); units outside math trigger validator errors.
- Every markdown section in a topic-specific note, no matter the header level, must have at least one flashcard entry. Use a horizontal rule `---` immediately before the first flashcard block; missing separators or cards trigger validator errors. Index files and questions pages (e.g. `questions.md`) are exempt: index files need only session‑level cards; questions pages are not topic notes and do not need the "Flashcards for this section are as follows:" pattern in each section.
- Do not merge cards across sections; each heading gets its own block directly beneath the prose. The validator flags missing separators or cards.
- Keep gloss text single‑lined; use `<br/>` for right‑hand breaks, never sublists. For glosses that contain bullet‑like numbered items, write them inline as `(1) … <br/> (1.1) … <br/> (1.2) … <br/> (2) …` rather than using an actual list, so you can express nested proof or intuition steps without breaking the one-line rule. If you instead use nested flashcard bullets, indent them by exactly two spaces per level and include the full parent path in each nested QA prompt. Bibliographic references on the right‑hand side should be dash‑separated with a space before each `<br/>`.
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

These examples illustrate proper indentation and the two-sided QA list format. Topic notes (except journal entries) use only QA cards, not cloze.

## Topic-specific notes

When a lecture topic deserves its own dedicated page — either because it is broad, gets revisited, or should be linkable from multiple sessions — create a new Markdown file inside the course directory. **Flashcards in topic notes** (other than `journal entries.md`): use only two-sided (::@::) or, very rarely, one-sided (:@:) cards; do **not** add cloze deletions in the prose. Add more QA flashcards as needed instead of clozes. **Create the file empty first** (use a normal, unescaped filename with spaces; links will be percent-encoded later) and then add content in separate edit operations. When subsequently editing a topic note, each commit should target exactly one markdown section or add exactly one new section so that diffs remain precise and reviewable.

These **topic notes** are written in a neutral, encyclopaedic style rather than as a bulleted outline. Think of them as miniature Wikipedia articles: use smooth prose, organise the text with headings, and split material into logical sections. Use **subsections** (### under ##) where it improves hierarchy (e.g. “switches and current path” and “hazards” under “four-switch topology”; “saturation and transistor types” and “base voltage pattern” under “building an H-bridge”). Each ### gets its own prose and flashcard block; the same rule applies if you introduce even deeper headings (####, etc.). If a ### is very short (one paragraph and one or two flashcards), consider merging it into an adjacent related ### to avoid an overly fragmented outline.

When a course uses a **specific circuit layout** (e.g. H-bridge with top row both PNP, bottom row both NPN, and left/right legs each having one PNP and one NPN), describe that layout explicitly in the topic note; course materials may differ from generic textbook arrangements, so avoid assuming a “generic” topology without checking the slides or handout.

When choosing section names and groupings in topic notes, **do not blindly copy the headings or section partitions from the source course materials** (slides, PDFs, Canvas pages). Instead, design headings that succinctly express the underlying concept and its role (e.g. “conditional probability: definition and multiplication rule”, “independence via cards and coins”) and regroup related material when a different hierarchy makes the theory clearer; the course slides are an input, not a layout you must reproduce verbatim. In particular, avoid bundling two distinct named objects into one section heading when they deserve separate treatment (for example, separate “discrete uniform distribution” and “Bernoulli distribution” rather than a combined heading), and prefer the canonical law name itself as the heading when extra interpretation can live in the prose (for example, “binomial distribution” rather than “binomial distribution and Bernoulli-trial model”).

Each section must be followed immediately by a horizontal rule and a list of flashcards, exactly as described earlier in this document.  The validator will reject any heading that lacks a card block, so it’s easiest to add the "Flashcards for this section are as follows:" rubric as you compose the paragraphs. This requirement applies to topic-specific notes only; index and questions pages (e.g. `questions.md`) are exempt.

### Filenames, titles, and links

- Use **all lowercase** for topic note filenames (e.g. `voltage regulator.md`), except proper nouns that must remain capitalised (e.g. `Kirchhoff's circuit laws.md`). When the topic matches a general/Wikipedia article, prefer the full canonical name for both filename and H1 title (e.g. `brushed DC electric motor.md` and `# brushed DC electric motor`). The top‑level heading in the note should match the filename (lowercase except for proper nouns and any acronyms the course keeps capitalised).
- When creating the file, do **not** percent-escape the name; percent-encoding is only applied when writing links elsewhere.
- Add appropriate `aliases:` and `tags:` in the frontmatter, including the usual `flashcard/active/special/academia/...` tag for the course page. **Aliases should list only the general topic term and its synonyms** — do not include specific instances (e.g. LM7805 is an instance of a voltage regulator, not an alias for the general term). **Include both singular and plural forms** where applicable (e.g. brushed motor / brushed motors, brushed DC electric motor / brushed DC electric motors); keep the list sorted alphabetically (case‑sensitive).
- Cross‑link to the corresponding `general/` article using a relative path with `%20` encoding for spaces.  To discover canonical titles, run `uv run .agents/skills/academic-notes/find_wikipedia.py "<query>"` and pick the top hit.  **Do not** create or modify files under `general/` yourself.  Use **lowercase for the first word** in both the link display text and the path (e.g. `[brushed DC electric motor](.../general/brushed%20DC%20electric%20motor.md)` not “Brushed”); this keeps display and path convention consistent.

### Images and circuit diagrams

- Place diagram/schematic image markup on the same line as the preceding paragraph (see Session and index rules). Reference SVGs or other assets under a course-level `attachments/` (or similar) folder so links are stable.
- Some courses keep a script (e.g. `attachments/generate_circuit_diagrams.py`) that generates SVG diagrams with :mod:`schemdraw` or similar; outputs go into that folder and are referenced from topic notes. The script’s docstrings should describe each diagram’s topology and drawing style (e.g. ground‑up vs central‑component‑first, use of ``.at()`` and ``.reverse()``) for future maintainers. For **H-bridge schematics**: build from the motor first (one horizontal line left-to-right); use the motor’s start/end nodes for the left and right rails (e.g. up: PNP–Vcc, down: NPN–GND on each side). Use ``BjtPnp(circle=True).up()`` and ``BjtNpn(circle=True).down()`` for high-side and low-side switches; document this topology in the docstring.
- **Equivalent circuits with a main rail and a branch** (e.g. BJT diode + dependent current source): draw the main rail first (e.g. collector–emitter or emitter–collector with the dependent source), call ``.push()`` to save the node where the branch will attach (typically the emitter node), finish the rail (line and terminal), then ``.pop()`` to restore that node and draw the branch (e.g. diode and base terminal). Use ``.reverse()`` on the diode when needed so polarity matches the junction (e.g. NPN B–E: anode at B, cathode at E → ``.reverse()`` when drawing from emitter toward base).
- For ICs with power pins (e.g. **74HC14**): **VCC** can connect to any valid supply voltage for the IC; the course may use a specific value (e.g. $5\text{ V}$). **GND** connects to ground. Do not state that the IC “must be connected to $5\text{ V}$” unless the course explicitly fixes that value; instead write “VCC to the positive supply (in our course, $5\text{ V}$); GND to ground.”

### Course index and outline updates

After creating a topic note, append its link to the course `children:` list (after any folders) and add a reference in the relevant weekly session entry. In addition, **every named section and subsection within the topic note should be linked from the course index page**, not just to the file itself: link every `##`, every `###`, and any `####` (or deeper) so readers can jump to any heading. Use anchor-style links (`Topic%20Name#section-heading`) so that readers can jump directly to the appropriate subsection. Make sure the **link text exactly matches the section heading** – display names which differ (e.g. dropping “Kirchhoff's” from a heading) are not allowed and must be corrected. When you later revisit the topic in another lecture, append new material to the existing file instead of making a duplicate. _Proper nouns such as Kirchhoff must be capitalised in both filenames and headings._

**Indexing sections and subsections:** In the course index **children** section, list each topic note as a single link (e.g. `- [sample space](sample%20space.md)`); do not nest § links under topic notes in children. In **lecture, tutorial, and lab session entries**, list each topic note covered as a parent link (e.g. `- [sample space](sample%20space.md)`), then underneath one indented line per section: `- topic name / [§ section name](file#anchor)`. For **index-only content** (e.g. session-level flashcards not in topic notes), keep the course code as parent and nest those bullets under it (e.g. `- MATH 2431` then `- MATH 2431 / topic ::@:: ...`). Within topic notes themselves you may and should use deeper headings (e.g. `###` under `##`) where it improves hierarchy; every such subsection must still follow the “section prose → --- → Flashcards for this section…” pattern with its own local flashcard block.

**Section links index in session entries:** For each lecture, tutorial, or lab session that references topic notes, list each topic note as a **parent link** (e.g. `- [sample space](sample%20space.md)`), then under it one indented line per section covered: `- topic name / [§ section name](file#anchor)`. For content that lives only in the index (e.g. session-level flashcards), use the course code as parent and nest under it (`- MATH 2431` then `- MATH 2431 / …`). For anchors: percent-encode spaces, or use **hyphenated anchors** for headings with commas or special characters to avoid validator false positives. When you merge or remove ### subsections in a topic note, update the § links in the session entries to match.

Whenever you edit a topic note, treat the note and the course index as a synchronized pair: update the prose, update the flashcards that test that prose, and then update every affected `index.md` link or anchor before finishing the task.

For lab-heavy courses that maintain assignment-style lab notes under `labs/lab N/index.md`, each timed lab session in the main course index (for example “week 4 lab 1”) should both (a) include the usual § links into the relevant topic notes (electronic component, lab equipment, diode, voltage regulator, H-bridge, etc.) and (b) add a bullet linking to the corresponding lab assignment note (`labs/lab N/index.md`). This keeps the timeline as the single navigation hub for both conceptual material and the Canvas-style lab pages without duplicating lab-manual procedures into the index.

### Journal entries note (accounting courses)

For **accounting courses**, include a topic note named **`journal entries.md`** that collects every type of journal entry encountered in the course. One journal entry type per section (`##`). Each example must sit in a **single markdown blockquote**: (1) a brief _scenario_ (before the journal entry), (2) the **journal entry in a markdown table** with columns for account, Dr, and Cr, and (3) optionally _explanation_ or _calculation_ (after the table). Use **markdown tables** for the entry (not LaTeX); in accounting notes do not use LaTeX anywhere—use plain numbers and symbols. Right-align the Dr and Cr columns with separator `|--|--:|--:|`. **Table header:** the first column header (the cell above the account names) must contain a **very brief description** of the journal entry (e.g. "Receive cash; record note", "Settle claim; reduce liability"); wrap that description and **each account name** in the first column in clozes (`{@{…}@}`) so that flashcards cover the description and every account fully. For **readability**, use **`&nbsp;`** (non-breaking space) as the three-digit thousands separator in amounts (e.g. 50&nbsp;000, 1&nbsp;200), not a comma. **Cloze delimiter:** the closing `}@}` must come **before** any trailing punctuation—place punctuation after the delimiter (e.g. `{@{text}@}.` not `{@{text.}@}`). Add two-sided cards (::@::) for concepts and how to create the entry. **Cloze requirements for examples:** (a) mask **all** debit and credit amounts in the table with `{@{ amount }@}`; (b) add one or more cloze cards in the scenario text so that **almost** the entire scenario is covered, but **leave a few hint words uncovered** at the beginning or at the end (do not cover an entire sentence with a single cloze). For longer statements, use **two or three** clozes with hint words between or at the ends. (c) Cover **calculation** and **explanation** lines with clozes as well, again leaving a few hint words at the start or end. For calculations: **cover both sides of an equality separately** (e.g. `{@{50&nbsp;000 × 0.08 × 2/12}@} = {@{833.33}@}`), and **cover the text (non-equation) portion** too, with hint words uncovered (e.g. “Crediting” at start, “maturity amount.” at end). After adding new entry types, add the new sections to the course index `children:` and to the relevant week’s session outline with § links. **Warranty settlement:** when describing or showing warranty claim entries, use the credit account "Cash, Inventory, or Accrued Payroll" (depending on how the repair is satisfied), not just "Cash". **Service-type warranty:** in examples, show the service period as starting after the assurance-type warranty has expired (e.g. years 2–4); the general principle is that revenue is recognized as the entity satisfies the performance obligation over the service period. The validator exempts only **table rows** from the soft-wrap rule (after stripping any number of blockquote markers, e.g. `>`, `>>`, `> >`); blockquote prose is still subject to the rule (see `no_soft_wrap_paragraph` in the rules).

### Micro‑workflow example

**Math and formatting rules:** never use fenced code blocks for maths; always write expressions inline or in display math (`$...$` or `$$...$$`) using LaTeX syntax. Topic notes do not require a separate summary section. Section headers should use all lowercase words except where grammatical capitalization is needed (proper nouns, the first word of a sentence).

Create the note, update the index, and add the outline link as shown below:

```markdown
# Kirchhoff's circuit laws

Kirchhoff's circuit laws are the two foundational relations engineers use to analyse arbitrary resistor networks when simple series/parallel reduction fails.  The current law (KCL) applies at nodes, the voltage law (KVL) applies around closed loops.  Both follow directly from conservation principles and are named after Gustav Kirchhoff (1824–1887).

---

Flashcards for this section are as follows:

- Kirchhoff's circuit laws definition ::@:: Two fundamental relations for analysing circuits: KCL (node current rule) and KVL (loop voltage rule).
- Kirchhoff's current law ::@:: At any junction, the sum of currents entering equals the sum leaving.
- Kirchhoff's voltage law ::@:: Around any loop, the algebraic sum of voltage rises and drops is zero.
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
# POSIX shells (bash/zsh/fish); escape the space in the course folder
uv run .agents/skills/academic-notes/check.py special/academia/<institution>/ELEC\ 1100

# Windows PowerShell or cmd; quote the path that contains a space
uv run .agents/skills/academic-notes/check.py "special/academia/<institution>/ELEC 1100"

# Example (this course, ELEC 1100):
uv run .agents/skills/academic-notes/check.py "special/academia/HKUST/ELEC 1100"
```

The validator is strict and does not have an advisory mode. Common errors include missing tags, absent `datetime:` values, out‑of-order semesters, sections without cards, duplicate week numbers, and exams placed too early. Fix errors before committing. Before committing, run `bun run format`, `bun run check`, and `bun run test` with explicit paths to your changed files so the commands execute quickly.

The repository contains helper scripts (`check.py`, `find_wikipedia.py`) and templates (`course-template.md`) that you should inspect when writing new notes. Keep these tools up to date and report any bugs or feature requests in `continuous_improvement.md` or the Continuous improvement section below.

## Continuous improvement

The skill evolves with real course content. Record every new pattern, validator failure, or user preference in `continuous_improvement.md` (with date and a one-sentence description); consider whether the rule or clarification should be added to this document. Maintainers should review the log periodically. When the log gets too long, fold learnings into the skill docs (this file, `course-template.md`, or academic-notes instructions), then remove the incorporated entries from the log so it stays a short, current list; git history preserves provenance.

### Workflow for agents

1. **Gather examples** — When you encounter a pattern, bug, author question, or user feedback related to `special/academia`, save a snippet or run the validator in `--content` mode. Log each incident in `continuous_improvement.md` with a date and a one-sentence description. Include privacy concerns, formatting quirks, or template ideas.
2. **Document the change** — Decide where the information belongs: new idiom, normalization or regex → add to this document (e.g. Session and index rules, Topic-specific notes) or a dedicated doc if the skill later adds one (e.g. patterns.md). Short samples or explanations → add to this document’s examples or a dedicated examples doc. Repeated author behaviour or gotcha → note it in the Pre‑commit checklist or a checklist doc. Always write prose directed at the human reader; the validator can be extended later if needed.
3. **Teach the validator** — If the issue is structural or recurring, add a rule to `check_mods/rules.py` and cover it with a unit test under `tests_a7392be/check_mods/` so future runs catch it automatically.
4. **Verify impact** — Run the validator on the affected files (or the whole tree). If the skill maintains an issue-frequency report, regenerate it so you can watch counts drop after your fix lands.
5. **Submit a focused PR** — Bundle only the documentation, tests, and any normalization patches required to address the issue. Keep diffs reviewable; avoid broad regex respells unless you have explicit owner approval. In the PR description list which content files will be affected when the change is deployed.

**Best practices:** Prefer advisory `--content` warnings when unsure; they are nonblocking and educate authors without causing failures. Always update the skill docs (this file and related skill files) as the authoritative reference; use the feedback log for incidents and process notes. Record unusual decisions in the feedback log or a GitHub issue rather than cluttering the main docs.

**Example:** You notice several courses missing flashcard tags during a browse of `special/academia`. Add a new pattern and checklist item for mandatory flashcard tags; write a small test that flags absent tags. After merging, run the validator (and any issue-frequency report) to confirm the count has dropped.

### Provenance and folding the log

New feedback and incidents go in `continuous_improvement.md` (date + short description). When the log is long, fold learnings into this file, `course-template.md`, or academic-notes instructions and remove those entries from the log; git history keeps provenance.

### Extending the validator

If you encounter a structural issue the existing checks do not catch, you can add a new rule to the validator instead of simply suppressing the warning. The validator code lives under `.agents/skills/academic-notes/check_mods`.

1. **Edit `rules.py`.**  Add a new function accepting a
   :class:`ValidationContext` and returning a list of
   :class:`ValidationMessage`.  Decorate it with ``@RULE_REGISTRY.register()``
   so it is automatically discovered.  Keep the rule pure (no side effects) and
   return an empty list when the file passes the check.  Use existing rules as
   templates; the docstring should clearly describe what the rule validates.
   Example:

   ```python
   @RULE_REGISTRY.register()
   def no_foo_heading(ctx: ValidationContext) -> list[ValidationMessage]:
       """Disallow headings containing the word “foo”.

       This is useful when we know the term is meaningless in course notes.
       """
       errors: list[ValidationMessage] = []
       if re.search(r"^#+.*\bfoo\b", ctx.text, re.I):
           errors.append(ValidationMessage("no_foo_heading", "heading contains foo"))
       return errors
   ```

   The rule identifier is derived from the function name (underscores only),
   and the test suite enforces this invariant; see ``tests_a7392be/check_mods``
   for examples.

2. **Add unit tests.**  Every rule gets a corresponding test in
   `tests_a7392be/check_mods/test_rules.py`.  Construct a minimal
   ``ValidationContext`` that triggers the rule and assert the correct
   message is returned.  Also add a case demonstrating the rule passes.
   This ensures future refactors don’t accidentally disable your check.

3. **Run the validator.**  Exercise the new rule with real notes to
   verify the behaviour and adjust error messages as needed.  Commit both the
   rule and its tests together so CI can catch regressions.

4. **Document the change.**  Optionally update this SKILL.md section or
   `continuous_improvement.md` with a brief rationale.  New rules are a
   permanent part of the course‑notes grammar, so explain why the check is
   needed and what to do when it fires.

   The previous example of adding the ‘section_example_heading’ rule (which
   flags headings containing the word “example”) came from exactly this
   workflow: after noticing repeated blocks of “numerical examples” the rule
   was added, tests written, and the SKILL updated with guidance like this.
