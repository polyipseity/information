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
