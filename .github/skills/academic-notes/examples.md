# Examples and snippets (academic notes)

**CRITICAL:** before using any examples, agents must read every file in this directory (`.github/skills/academic-notes/`) and every line of those files. Do not treat this file as a complete summary; it supplements the detailed instructions elsewhere.

This file collects concise, long-line examples that the **academic-notes** agent uses for training and guidance.  Each section pairs a Markdown snippet with minimal commentary.  Lines are deliberately not wrapped; examples may be extremely long to ensure the agent sees realistic real‑world patterns.

## Minimal frontmatter

```markdown
---
aliases:
  - COMP 3031
  - Principles of Programming Languages
tags:
  - flashcard/active/special/academia/<INSTITUTION>/COMP_3031
  - function/index
  - language/in/English
---
```

## Weekly lecture outline

Basic skeleton used by most course notes.  Agents should always add flashcard glosses immediately after creating a new header, even if it is a minor subtopic.

```markdown
## week 3 lecture

- datetime: 2025-09-16T12:00:00+08:00/2025-09-16T13:20:00+08:00, PT1H20M
- topic: polymorphism; type bound; variance
- COMP 3031
  - COMP 3031 / polymorphism ::@:: Parametric polymorphism, subtyping polymorphism
```

**Tag tip:** use underscores for course codes in flashcard activation tags (`COMP_3031`) and canonical institution short names in frontmatter (e.g. `HKUST`).

## Detailed lecture entry (slide-level detail)

Shows the richest permitted structure, including numbered lists, explicit indentation, acronyms, rhetorical questions, and a reminder about linking deep proofs to `general/` instead of copying them.

```markdown
## week 7 lecture

- datetime: 2025-10-07T12:00:00+08:00/2025-10-07T13:20:00+08:00, PT1H20M
- topic: type inference; Hindley–Milner
- COMP 3031
  - HM / algorithm sketch ::@:: Unify constraints from expression syntax tree, solve by substitution
  - HM / type variable rules ::@:: Fresh variable introduced for each binder; generalized at let-bound identifiers
  - HM / example explanation ::@:: Step through constraint generation from syntax tree nodes
  - HM / worked example (detailed):
    1. Given expression: let f = \x -> (x, x) in f 3
    2. Assign type variables: x: a, result tuple components a, a
    3. Constraint from (x, x): both positions share type a
    4. f: a -> (a, a); application f 3 enforces a = Int by unification
    5. Generalize: f : forall a. a -> (a, a); instantiate at Int for f 3
    6. Result: (3, 3) :: (Int, Int)
  - HM / pitfalls ::@:: Forgetting to generalize at let leads to value restriction bugs. **Emphasis**: Instructor stressed 'generalization at let-bindings' (important for polymorphism in ML-like languages).
  <!-- Note: keep long proofs or formal material in `general/` when they are encyclopedic; link from course notes instead of copying. Save long proofs or formal definitions in `../../../../general/Hindley–Milner.md` and link from here. -->
  - COMP 3031 / related literature ::@:: Reynolds, J. (1974): "Polymorphism"<br/> Cardelli, L. (1985): "Typeful Programming" <br/> Pierce, B. (2002): _Types and Programming Languages_  
    (list items separated by dashes with a space before each `<br/>`)
  <!-- indentation example: bullet directly under course header with no extra indent -->
  - COMP 3031 / extra note ::@:: This line is indented exactly two spaces relative to the previous level, illustrating the correct outline indentation without extra blank levels.
```

## Logistic paragraph example

Mixes structural outline with prose and cloze flashcards.  The long paragraph below demonstrates multiple simultaneous clozes in narrative form; agents should model generation of similar content.

```markdown
### week 1 lecture 1
- datetime: 2026-02-02T16:00:00+08:00/2026-02-02T16:50:00+08:00, PT50M
- topic: course introduction
- ELEC 1100
  - ELEC 1100 / course overview
    - ELEC 1100 / course overview / description ::@:: Designed to provide fundamental knowledge in electrical engineering, basic electronic components and robot design
    - ELEC 1100 / course overview / outcomes ::@:: Analyze and design simple analog circuits; implement control strategies; build/debug systems using hierarchical design; manage projects; execute full project lifecycle
  - ELEC 1100 / pedagogy
    - ELEC 1100 / pedagogy / methodology ::@:: Reverse engineering approach: start with engineering, then physics, then mathematics; emphasizes learning by doing
    - ELEC 1100 / pedagogy / traditional limitations ::@:: Traditional education teaches knowledge that may become obsolete and does not focus on application
  - ELEC 1100 / expectations ::@:: Attend lectures, tutorials and labs on time; participate actively; ask questions; enjoy the experience
  - ELEC 1100 / what is a robot?
    - ELEC 1100 / what is a robot? / history ::@:: Word “robot” first used in 1921 by Czech playwright Karel Capek; “robotic” appeared in Issac Asimov’s 1942 story
    - ELEC 1100 / what is a robot? / definitions ::@:: Robot Institute of America definition: a reprogrammable, multifunctional manipulator designed to move material, parts, tools, or specialised devices through various programmed motions for the performance of a variety of tasks; Webster definition: “an automatic device that performs functions normally ascribed to humans or a machine in the form of a human.”
    - ELEC 1100 / what is a robot? / features ::@:: - artificially created and programmable <br/>  - can sense its environment and manipulate or interact with things in it <br/>  - has some ability to make choices based on the environment, often using automatic control or a preprogrammed sequence <br/>  - moves without direct human interaction <br/>  - discussion questions: are animals robots? is a motorcycle a robot? 
    - ELEC 1100 / what is a robot? / examples ::@:: - First real robot Unimate deployed in 1961 at a GM car plant, developed by Joseph F. Engelberger and George C. Devol<br/>  - Modern robots: Boston Dynamics dancing robots; Roomba vacuum cleaner; Aqua 2 underwater robot from McGill University; DJI Air 2S drone

---

During the first lecture the instructor went over {@{the course logistics}@}.  You should regularly check {@{the Canvas home page and syllabus}@} for {@{the complete schedule and any exam announcements}@}; {@{next week the tutorials}@} start on 2026-02-09, 2026-02-12, and 2026-02-13 and {@{the first lab sessions}@} begin on 2026-02-13, so be prepared for Lab #1.  The teaching team consists of the {@{course instructor supported by an instructional assistant and a technical officer}@}.  Grading is weighted as follows: {@{six labs totalling 29%, eight pop‑up quizzes worth up to 3%, a closed‑book lab exam 20%, a closed‑book written exam 25%, a project demo 20%, and a short project report 3%}@}.  {@{Late work}@} is not accepted; if you {@{miss a submission for a legitimate reason}@} you must {@{contact the IA within one week and provide documentation}@} to arrange a make‑up.  Finally, all students are expected to observe {@{the HKUST academic honour code}@} – {@{violations such as plagiarism}@} may result in {@{failing the course}@}.
```

## Energy and power example

Straightforward concept list followed by extracted flashcards.  Agents can use this pattern to verify that they identify cards correctly.

```markdown
- Energy is electrical or mechanical work capacity; analogies (food for humans, batteries for robots) help make the idea concrete.
- Electrical energy delivered to charge $q$ through a potential difference $V$ is given by $E = qV$.
- Power is the rate of energy transfer: $P = E/\Delta t = IV$, and for resistive components $P = I^{2}R = V^{2}/R$.
- Batteries and DC supplies provide constant voltages; AC sources oscillate (50 Hz in Hong Kong, 60 Hz elsewhere).
- Example calculation ::@:: A $200\,\Omega$ resistor with $5\text{ V}$ across it dissipates $P = V^{2}/R = 0.125\text{ W}$.

---

Flashcards for this section are as follows:

- energy definition ::@:: Energy is the ability to do work and may be electrical, mechanical, thermal, or chemical.
- human/robot analogy ::@:: People get energy from food while robots obtain it from batteries or power supplies.
- energy formula ::@:: Electrical energy for charge $q$ across voltage $V$ is $E = qV$.
- power definition ::@:: Power is energy per time $P = E/\Delta t = IV$ and in resistors $P = I^{2}R = V^{2}/R$.
- AC vs DC ::@:: DC has constant polarity; AC alternates at typical mains frequencies (50 Hz or 60 Hz).
- calculation example ::@:: A $200\,\Omega$ resistor with $5\text{ V}$ across it dissipates $P = V^{2}/R = 0.125\text{ W}$.
```

## Questions & acronyms example

Shows how multi-line bullet lists and discussion questions appear.  The script snippet below demonstrates the helper for Wikipedia title lookup.

```markdown
- datetime: 2026-02-02T16:00:00+08:00/2026-02-02T16:50:00+08:00, PT50M
- topic: robot definition
- ELEC 1100
  - ELEC 1100 / what is a robot? / features
    - artificially created and programmable
    - can sense its environment and manipulate or interact with things in it
    - has some ability to make choices based on the environment, often using automatic control or a preprogrammed sequence
    - moves without direct human interaction
    - discussion question:: Are animals robots? Is a motorcycle a robot?
  - ELEC 1100 / robot definitions ::@:: Robot Institute of America (RIA) definition: a reprogrammable, multifunctional manipulator …
```

```bash
python .github/skills/academic-notes/find_wikipedia.py "Hindley Milner"
```

The script prints JSON lines with suggested `title` and `url`. Pick the top candidate (e.g., `Hindley–Milner`) and link to `../../../../general/Hindley–Milner.md` from course notes. Do **not** create or edit files under `general/`.

## Topic-specific note workflow

When a lecture topic deserves its own note, keep the index clean and provide linkable content in a separate file.  The example below is condensed but steps are explicit.

1. Search folder and run helper script.
2. Create new file with sentence-cased heading, aliases, tags, and a cross-link to the corresponding `general/` article.
3. Update `index.md` by appending the file after folders and add a `see also` link in the weekly outline.  Use the pattern illustrated in the earlier code block; link the file once and subsequently refer by section-only anchors.

File header example:

```markdown
---
aliases:
  - ELEC 1100 electronic component
  - ELEC 1100 electronic components
  - ELEC1100 electronic component
  - ELEC1100 electronic components
  - HKUST ELEC 1100 electronic component
  - HKUST ELEC 1100 electronic components
  - HKUST ELEC1100 electronic component
  - HKUST ELEC1100 electronic components
  - electronic component
  - electronic components
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/electronic_component
  - language/in/English
---
# electronic component

- HKUST ELEC 1100

---

- see: [general/electronic component](../../../../general/eng/electronic%20component.md)
```

## Assignments directory layout

```text
special/academia/<INSTITUTION>/<COURSE>/assignments/
  index.md
  homework 1/
    index.md
    submission.yml
    attachments/
```

Keep assignment directories small and avoid storing student PII; use `private/` for submissions.

## Hierarchical administrative snippet

```markdown
### week 1 lecture 1
- datetime: 2026-02-02T16:00:00+08:00/2026-02-02T16:50:00+08:00, PT50M
- topic: course introduction
- ELEC 1100
  - ELEC 1100 / what is a robot?
    - ELEC 1100 / what is a robot? / examples ::@::
        - First real robot Unimate (1961) created by Engelberger & Devol
        - Categories: aerospace, consumer, industrial, humanoid, etc.
  - ELEC 1100 / design principles
    - ELEC 1100 / design principles / hierarchical decomposition ::@::
        Divide-and-conquer into subsystems; e.g., Mars rover project uses control, comms, mechanical, signal teams.
```

This snippet illustrates multiple levels of nesting and combining related points under a single parent node.

## cloze-rich general paragraph example

```markdown
During the first lecture the instructor went over {@{the course logistics}@}.  You should regularly check {@{the Canvas home page and syllabus}@} for {@{the complete schedule and any exam announcements}@} and monitor your HKUST email account for updates; {@{next week the tutorials}@} start on 2026‑02‑09, 2026‑02‑12, and 2026‑02‑13 and {@{the first lab sessions}@} begin on 2026‑02‑13, so be prepared for Lab #1.  The teaching team consists of the {@{course instructor supported by an instructional assistant and a technical officer}@}.  Grading is weighted as follows: {@{six labs totalling 29%, eight pop‑up quizzes worth up to 3%, a closed‑book lab exam 20%, a closed‑book written exam 25%, a project demo 20%, and a short project report 3%}@}.  {@{Late work}@} is not accepted; if you {@{miss a submission for a legitimate reason}@} you must {@{contact the IA within one week and provide documentation}@} to arrange a make‑up.  Finally, all students are expected to observe {@{the HKUST academic honour code}@} – {@{violations such as plagiarism}@} may result in {@{failing the course}@}.  The next lecture will cover {@{basic components and charge/current/voltage/resistor}@}.
```

## pedagogy paragraph example

```markdown
The instructor emphasised {@{a **reverse‑engineering learning approach**}@} “tell {@{me and I forget}@}; teach {@{me and I remember}@}; involve {@{me and I learn}@}”, contrasting {@{traditional math‑first pedagogy}@}.  He emphasised {@{**not a LEGO robot programming class**}@} – students start {@{from the most basic components}@} and build {@{an autonomous robot step by step}@}, learning to manage {@{power supplies, drive motors}@}, read {@{sensor outputs and implement logic/decision‑making}@} as they construct a working system.
```

Adding such narrative samples helps the model generalize to prose clozes of conceptual points.

## Inline gloss & takeaway examples (what we actually see in notes)

## sections metadata and weekly pattern example

```markdown
## logistics
- sections:
  - lecture: L1
    - L1: CYT‑LTL; MondayT16:00:00/MondayT16:50:00, FridayT11:30:00/FridayT12:20:00
  - tutorials: T2
    - T2: NCKU‑103; TuesdayT14:00:00/TuesdayT15:20:00
  - labs: LA3
    - LA3: LAB‑1; WednesdayT09:00:00/WednesdayT11:00:00
```

The `sections:` list bundles each **section identifier** with its venue and a comma‑separated sequence of weekly day/time patterns.  The outer entries are labeled by session type (`lecture`, `tutorials`, `labs`), and the same identifier appears both at the outer level and as the key of the inner list. Agents and authors should treat the day/time segment as potentially unbounded — include as many comma‑separated pairs as needed for multiple slots during the week.  This nested structure replaces the older flat semicolon format and keeps all metadata self‑contained.

## unscheduled session example

```markdown
### week 5 lecture
- datetime: 2025-10-21
- status: unscheduled
```

Since the session is cancelled or a holiday, no `topic:` field is included. The validator will warn if `topic:` is present along with `status: unscheduled`.

## duplicate week number (holiday) example

```markdown
### week 9 lecture
- datetime: 2025-11-11T10:00:00+08:00/2025-11-11T11:20:00+08:00
- topic: regular lecture

### week 9 lecture 2
- datetime: 2025-11-18T10:00:00+08:00/2025-11-18T11:20:00+08:00
- status: public holiday
```

When a timetable repeats a week label during a break, shift subsequent weeks upward and insert an explicit holiday entry.  The validator also checks for duplicate numbers.

## exam ordering illustration

```markdown
## week 5 lecture
- datetime: 2025-10-14T12:00:00+08:00/2025-10-14T13:20:00+08:00
- topic: combinatorics

## midterm examination
- datetime: 2025-10-28T12:00:00+08:00/2025-10-28T14:00:00+08:00

## week 6 lecture
- datetime: 2025-11-04T12:00:00+08:00/2025-11-04T13:20:00+08:00
```

## semester heading order example

Institution indices should list semesters chronologically.  Ordering errors trigger validator warnings.

```markdown
### 2024 fall
- COMP 3031 (taken)

### 2024 spring
- COMP 2012 (taken)
```

Invalid: spring before fall. Correct order:

```markdown
### 2023 fall
### 2024 spring
### 2024 fall
```

The validator also warns if an exam section precedes regular sessions.

```markdown
- topic ::@:: Type inference and Hindley–Milner
- takeaway ::@:: Principal type inference reduces annotation burden; watch for let-polymorphism corner cases
- COMP 3031 / Hindley–Milner ::@:: Unify constraints from expression syntax tree and solve by substitution

Keep glossary one-liners concise; these are the primary source of flashcards via `::@::` markup.
```

## Taxonomy / chain notation

```markdown
- _(begin)_→::@::←blue ocean strategy: Break the value–cost tradeoff. For example, London cab services (red) and Uber (blue).
- blue ocean strategy: Break the value–cost tradeoff.→::@::←business model canvas
- business model canvas→::@::←competitor analysis
- ...
- value proposition canvas→::@::←_(end)_
```

## Takeaway shorthand normalization suggestion

```markdown
- general case analysis question takeaways ::@:: Identify key questions. Choose the question that is most precise and involves least work.

-->

- takeaway: Identify key questions; pick the most precise one that minimizes extra work.
```

## Datetime with duration example

```markdown
- datetime: 2024-02-06T18:00:00+08:00/2024-02-06T20:00:00+08:00
- datetime: 2024-11-09T09:30:00+08:00/2024-11-09T12:30:00+08:00, PT3H
```

## Flashcard activation tag example

```markdown
---
tags:
  - flashcard/active/special/academia/<INSTITUTION>/COMP_3031
  - function/index
---
```

Replace `<INSTITUTION>` with your canonical short name (e.g., `HKUST`, `MIT`, `STANFORD`). Use underscores in course codes.
