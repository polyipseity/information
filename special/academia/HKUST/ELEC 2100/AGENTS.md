---
aliases:
  - ELEC 2100 AGENTS
  - HKUST ELEC 2100 AGENTS
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/AGENTS
  - language/in/English
---

# ELEC 2100 agent instructions

- Keep this course scaffold logistics-heavy until lecture PDFs, tutorial sheets, or worked solutions are actually ingested; do not invent transform derivations or topic notes from vague source-unit titles alone.
- Keep `index.md` pages lean: the course root should give the overview, folder indexes should summarize navigation, and leaf indexes should usually hold only minimal logistics.
- The chosen sections are L1 for lecture, T2 for tutorial, and LA3 for lab; default schedule metadata should follow those sections unless a page is intentionally summarizing all official sections in parallel.
- When tutorial routing is kept in the course root instead of separate child pages, represent it as chronological `## week N tutorial` sessions using the chosen T2 stream; do not collapse tutorial coverage into one bulk tutorial-summary section.
- When the course root keeps week-by-week chronology, include `## week N lab` sections for every teaching week using the chosen LA3 timeslot, even when the content is only `status: no class` or a public-holiday marker.
- For Canvas-derived assignment-style leaf indexes in this course (including `labs/lab X/index.md` and similar deliverable pages), keep the visible Canvas page wording verbatim. Preserve color with `<span style>`, use Markdown for bold, italics, links, paragraphing, and line breaks, and structure the page as: index metadata (with no extra `---` after the parent line), `## children`, `## description`, `## attachments`, `## submission`, and `## solution`. Inside `## description`, do not keep the Canvas title as a heading; add it as the first list item in the exact form `- title: <Canvas title header verbatim>`, then continue with the other Canvas properties. Omit generic `## logistics` and `## overview` sections, include an explicit attachments list pointing to the local `attachments/` files, and leave `submission` / `solution` empty until the user provides content.
- In `lab.md` and `prelab.md` pages, let `index.md` own the logistics, Canvas wording, and attachments. Use the companion pages for new knowledge points, worked cases, implementation pitfalls, and interpretation habits that are specific to the tasks. Do not re-teach theory that already has a durable topic note; link to the topic-specific note for that theory, and keep flashcards only for page-specific knowledge or worked cases rather than for duplicated course concepts.
- In `lab.md` and `prelab.md` pages, keep the prose and flashcards about pure knowledge only. Do not add workflow checklists, student expectations, assessment framing, or other logistics-like prose there.
- In `lab.md` and `prelab.md` pages, also avoid meta-summary sections and meta-level flashcards about what the page covers. Write them like normal knowledge notes, and refer to durable topic notes with ordinary sentences when needed.
- When the lab source includes MATLAB work, keep short MATLAB code idioms in `lab.md` and `prelab.md` as part of the knowledge content: function choices, indexing patterns, plotting commands, and signal/audio/image handling details that make the lab mathematically concrete. Prefer concise snippets over full script dumps.
- For MATLAB-heavy flashcards in this course, include enough code context in the prompt to make the card answerable on its own, such as the relevant snippet, the role of a variable, or the meaning of a particular indexing pattern.
- When a MATLAB flashcard still feels too generic, include the local given as well: the specific waveform, filter, index expression, or before/after workflow that the prompt is referring to.
- When the user asks for more context, put that extra context mainly on the left-hand side of the flashcard prompt rather than only in the answer.
- Do not add staff names, email addresses, or phone numbers to the public notes; office-hour times and rooms are acceptable.
- When scaffolding course logistics from partial LMS material, create minimal pages for foreseeable assignment, tutorial, and lab items evidenced by the provided materials. Prefer flat leaf files such as `tutorial 1.md` when an item is not expected to gain children or attachment-local assets, and reserve per-item folders with `index.md` for cases that really need their own subtree. Keep any agent-only guidance here in the course-root `AGENTS.md`, not in child note pages.
- When official lecture materials are added, prefer durable topic notes for convolution, Fourier analysis, sampling theorem, Laplace transform, and differential/difference-equation system models, then route the course index to those notes with section links.
- Keep `unified Fourier representations.md` treated as extra enrichment content rather than official course coverage: it may be linked only once from the `## children` section of the course root `index.md`, and it must not be linked from week-by-week lecture sections or used to rewrite official lecture scope.
- Avoid chapter-number references in prose and flashcards when a lecture week or topic-note link can be used instead; this course stores topic notes, not chapter pages.
- For technical ELEC 2100 notes, prefer formula + derivation/proof skeleton + intuition + worked example over formula-only summaries.
- Preserve the Spring 2026 timetable snapshot: lectures meet on Tuesday and Thursday, tutorials on Wednesday/Thursday, and labs on Thursday/Friday as recorded in the Canvas timetable.
