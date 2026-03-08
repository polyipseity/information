# Continuous improvement — academic-notes skill

This note exists solely to teach agents how to keep the `academic-notes` skill
sharp.  The operational guidance lives in the **Continuous improvement** section
of `SKILL.md`; read that first.  Use this file only when you need a quick
check‑list or process reminder while performing updates.

## Workflow for agents

1. **Gather examples** – whenever you encounter a pattern, bug, author
    question, or user feedback related to `special/academia`, save a snippet or
    run the validator in `--content` mode.  Log each incident in
    `.agents/skills/academic-notes/reports/feedback_log.md` with a date and a
    one‑sentence description.  Include privacy concerns, formatting quirks, or
    template ideas.
2. **Document the change** – decide where the information belongs:
    * new idiom, normalization or regex → add to `patterns.md`
    * short sample or explanation → add to `examples.md`
    * repeated author behaviour or gotcha → note it in `checklist.md`
    Always write prose directed at the human reader; the validator will learn
    later if needed.
3. **Teach the validator** – if the issue is structural or recurring, add a
    rule to `check.py` and cover it with a unit test under
    `.agents/skills/academic-notes/tests/` so future runs catch it automatically.
4. **Verify impact** – run the validator on the affected files (or the whole
    tree) and regenerate `issue_frequencies.md` so you can watch counts drop
    after your fix lands.  This step is how you measure progress.
5. **Submit a focused PR** – bundle only the documentation, tests, and any
    normalization patches required to address the issue.  Keep diffs
    reviewable; avoid broad regex respells unless you have explicit
    owner approval.  In the PR description list which content files will be
    affected when the change is deployed.

### Best practices for agents

* Prefer advisory `--content` warnings when unsure; they are nonblocking and
   educate authors without causing failures.
* Always update the skill docs instead of editing this file.  This file is
   a lightweight reminder, not the authoritative reference.
* Record process notes or unusual decisions in the feedback log or a GitHub
   issue rather than cluttering the docs.

### Illustration of the process

* Notice several courses missing flashcard tags during a browse of
   `special/academia`.
* Add a new pattern and checklist item for mandatory flashcard tags; write a
   small test that flags absent tags.
* After merging, run the validator and regenerate `issue_frequencies.md` to
   confirm the count has dropped to zero.

### Historical context (provenance only)

This section is for archive; agents do not normally read it.

* 2026-03-06 (ELEC 1100 voltage regulator session): Consolidated authoring learnings into SKILL.md: (1) topic note filenames use all lowercase except proper nouns (e.g. `voltage regulator.md`); (2) aliases list only the general term and synonyms, not specific instances (e.g. LM7805 is not an alias for voltage regulator); (3) circuit/KVL examples must describe component connections, polarities, and loop traversal; (4) circuit prose should specify signal path and component orientations (e.g. Zener cathode/anode); (5) when introducing a component via an instance (e.g. LM7805), include explicit treatment of the general concept (IC definition, datasheet role) with flashcards.
* 2026-03-06 (ELEC 1100 transistor session): Added guidance to (1) define common circuit shorthand and topology jargon at first use (e.g. $V_{CC}$ supply rail, $V_{CE}=V_C-V_E$, “low-side switch”), and (2) prefer single-focus conceptual flashcards by splitting multi-concept cards, while keeping calculation cards self-contained (do not delete givens from the left-hand prompt).
* 2026-03-06 (ELEC 1100 diode/transistor flashcard refinement): Clarified that multi-step procedures (e.g. diode ON/OFF assumption method, BJT saturation checks, low-side switch behaviour) should normally be broken into several smaller cards covering 1–2 steps each, provided each resulting card’s prompt on the left remains fully self-contained.
* 2026-03-06 (circuit diagrams and images): (1) Image placement: put diagram/schematic markup (e.g. `<p> ![...](path)`) on the same line as the preceding paragraph, not on a new line. (2) Diagram‑recall flashcards: add dedicated cards that embed the image in the prompt so learners can recall what each symbol or circuit diagram represents; keep left-hand side self-contained for validator. (3) Circuit diagram generators: course-level scripts (e.g. `attachments/generate_circuit_diagrams.py`) produce SVGs into `attachments/`; docstrings should describe topology and drawing style (ground‑up vs central component, `.at()`, `.reverse()`).
* 2026-03-07 (BJT equivalent diagrams, schemdraw): For equivalent circuits that have a main rail (e.g. C–E or E–C with dependent current source) and a branch (e.g. base–emitter diode), draw the rail first, then use `.push()` at the node where the branch attaches (e.g. emitter node), complete the rail, then `.pop()` and draw the branch (diode + base). Use `.reverse()` on the diode when polarity requires it (e.g. NPN B–E: anode B, cathode E when drawing from E toward B). SKILL.md “Images and circuit diagrams” updated with this pattern; generator docstrings in ELEC 1100 were updated to match the implementation.
* 2026-03-06 (section links index, H-bridge generator): (1) **Section links index**: Each session that references a topic note must list § links to every top-level section (`##`) of that note under the topic parent; list § links first, then session glosses. SKILL.md “Course index and outline updates” updated. (2) **H-bridge schematic (schemdraw)**: Build from the motor first: one horizontal `Line` left-to-right; use `motor.start` for the left rail (up: PNP–Vcc, down: NPN–GND) and `motor.end` for the right rail (same). Use `BjtPnp(circle=True).up()` and `BjtNpn(circle=True).down()` for high-side and low-side switches; docstrings should describe topology and `circle=True`.
* 2026-03-06 (H-bridge, session prose, topic hierarchy): (1) **Course-specific circuit layout**: Describe the course’s actual topology in topic notes (e.g. H-bridge with top row both PNP, bottom row both NPN; left/right legs each one PNP and one NPN); do not assume a generic “one PNP and one NPN per diagonal” without the top/bottom description. (2) **Topic note hierarchy**: Use ### subsections under ## for clearer structure; each ### gets its own prose and flashcard block. (3) **Session prose**: Prose after the outline (`---`) only when it adds value (next lecture, grading); do not duplicate index bullets and topic notes. (4) **Lecture summary cards**: Omit in the index unless they cover major grading components. (5) **74HC14 / IC power**: VCC can be any valid supply voltage (course may use 5 V); GND to ground; do not state “must be 5 V” unless the course fixes it. (6) **Transistor as inverter**: Logic levels from $V_C$ vs $V_E$; keep math readable (less dense); same content need not appear in both index prose and topic note.
* 2026-03-07 (brushed DC electric motor, topic note conventions): (1) **Topic filename and title**: Prefer the full canonical term for the topic note filename and H1 title when it matches the general/Wikipedia article (e.g. `brushed DC electric motor.md` and `# brushed DC electric motor` rather than a shortened form like `brushed dc motor`). (2) **Aliases singular and plural**: Include both singular and plural forms in `aliases:` where applicable (e.g. brushed motor / brushed motors, brushed DC electric motor / brushed DC electric motors); sort alphabetically (case-sensitive). (3) **General link display and path**: When linking to a `general/` article, use lowercase for the first word in both the link display text and the path (e.g. `[brushed DC electric motor](../../../../general/brushed%20DC%20electric%20motor.md)` not “Brushed”); this keeps display and filename convention consistent. (4) **Hierarchy**: Topic notes should use ### subsections under ## where it improves structure; each ### gets its own prose and flashcard block (already in SKILL.md; reinforced by user preference for “slightly more hierarchical” notes).
* 2026-03-07 (consolidation and index): (1) **Merging short ### subsections**: When a ### has only one short paragraph and one or two flashcards, consider merging it into an adjacent related ### (e.g. “current path at brushes and inside motor” merged into “commutation and the commutator and brushes”); move the prose and flashcards into the target subsection and remove the standalone ###. (2) **Index § links**: The session outline lists one § link per **##** (top-level) section only, not per ###; merging or removing ### subsections does not add or remove § links. (3) **Updating § glosses**: After consolidating topic-note structure, update the session § glosses in the index so the one-line summaries still accurately describe each ## section’s content.
* 2026-03-08 (index subsections, consolidation, anchors): (1) **Index sections and subsections**: The course index should index not only top-level sections (`##`) but also subsections (`###`) and any deeper (`####`). Under each topic note, list § links for every `##` and nest § links for each `###` (and `####`) under the corresponding `##`. (2) **Dedicated topic outline block**: The index may include a dedicated block per topic (e.g. “H-bridge (sections and subsections)”) with a nested list of § links for all `##` and `###` (and `####`), so readers can jump to any section or subsection from the index. (3) **Topic note consolidation**: When a topic note has too many small subsections, consolidate slightly by merging redundant or overlapping `###` (e.g. two subsections covering the same concept) into one; keep subsection titles lowercase per header style (e.g. “direction (DIR) signal and inverter solution” not “DIR signal and inverter solution”). (4) **Anchor format in index links**: For headings that contain commas or special characters, use hyphenated anchors (e.g. `#saturation-transistor-types-and-layout`, `#connecting-l293-74hc14-and-lm7805`) in index links to avoid validator false positives from `numeric_text_not_latex` on percent-encoded sequences (e.g. `%2C`).
* 2026-03-08 (ACCT 3020 course index and logistics): (1) **Course index separator**: Insert a horizontal rule `---` after the course list (name, credits) and before the course description. (2) **Logistics sections format**: Use a single key for the chosen section (e.g. `lecture: L1`); under it list all section identifiers and their details (L1, L2, L3 with venue and times). Do not create separate `lecture: L2`, `lecture: L3` keys. (3) **Session headings**: Use “lecture 2” with a space; do not put holiday or status in the section name (e.g. `## week 3` not `## week 3 (Lunar New Year)`). (4) **No-class days**: Omit `topic:` for days without classes. Use `status: public holiday: <name>` when the holiday is known (e.g. Lunar New Year, Labor Day); use `status: no class` for other non-teaching days (e.g. midterm break). (5) **Index session flashcards**: Omit session-level flashcard bullets in the index when they only describe scope/coverage; keep substantive cards in topic notes and questions. (6) **Markdown emphasis**: Use underscore for italic and bold (`_italic_`, `__bold__`) in course notes. SKILL.md, academic-notes.instructions.md, editing-conventions.instructions.md, and course-template.md updated accordingly.

* 2026-02-25 (latest consolidation): most prior notes were moved into
   `SKILL.md`, `patterns.md`, `examples.md`, `checklist.md`, `issue_frequencies.md`
   and validator tests.  This file now simply points agents at those sources
   and records why they exist.  A course template note and explicit rules were
   added at that time requiring every Markdown section to include a flashcard
   block and for authors/agents to update flashcards when editing sections.

* 2026-02-25 (energy/power & units): editing `electronic component.md`
   surfaced a new subsection heavy with units and formulas.  Documentation
   was updated to emphasise analogies, full sentences, and calculation-style
   flashcards.  A validator rule was added warning when physical units appear
   outside `$...$` math delimiters; `issue_frequencies.md` reflects that new
   warning.

Agents should not hard-wrap any lines in this document; long single lines are
preserved intentionally so automated tools and diffs remain clean.
