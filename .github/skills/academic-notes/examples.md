# Examples and snippets (academic notes)

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

## Weekly lecture example

```markdown
## week 3 lecture

- datetime: 2025-09-16T12:00:00+08:00/2025-09-16T13:20:00+08:00, PT1H20M
- topic: polymorphism; type bound; variance
- COMP 3031
  - COMP 3031 / polymorphism ::@:: Parametric polymorphism, subtyping polymorphism
```

Notes: prefer using `COMP_3031` (underscore) in course-scoped flashcard activation tags; frontmatter tags should use the canonical institution short name (e.g., `HKUST`).

## Detailed lecture example (content-focused)

The following snippet shows the kind of rich, slide-level detail we aim for
– the lecture has been transcribed almost verbatim, with every bullet and
example preserved and elaborated.

Additional conventions illustrated below show how to record rhetorical
questions and handle acronyms.

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
  - HM / pitfalls ::@:: Forgetting to generalize at let leads to value restriction bugs
  - !emphasis: Instructor stressed 'generalization at let-bindings' (important for polymorphism in ML-like languages)

  Note: keep long proofs or formal material in `general/` when they are encyclopedic; link from course notes instead of copying.

> Note: Save long proofs or formal definitions in `../../../../general/Hindley–Milner.md` and link from here.

```markdown
## outline with logistics paragraph

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

## example of questions & acronyms

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

Use the helper script to find a recommended article title:

```bash
python .github/skills/academic-notes/find_wikipedia.py "Hindley Milner"
```

The script prints JSON lines with suggested `title` and `url`. Pick the top candidate (e.g., `Hindley–Milner`) and link to `../../../../general/Hindley–Milner.md` from course notes. Do NOT create or edit files under `general/`.

## Assignments layout

```text
special/academia/<INSTITUTION>/<COURSE>/assignments/
  index.md
  homework 1/
    index.md
    submission.yml
    attachments/
```

Tip: keep `assignments/` directories small and include a `submission.yml` template for graders; student-submitted files (if containing PII) belong in `private/`.

## Inline gloss & takeaway examples (what we actually see in notes)

## sections metadata and weekly pattern example

```markdown
## logistics
- sections:
  - lecture: L1; CYT‑LTL; MondayT16:00:00/MondayT16:50:00, FridayT11:30:00/Fri
dayT12:20:00
  - tutorial: T2; NCKU‑103; TuesdayT14:00:00/TuesdayT15:20:00
  - lab: LA3; LAB‑1; WednesdayT09:00:00/WednesdayT11:00:00
```

The `sections:` list bundles the stream code, venue, and weekly
weekday/time pattern in one semicolon‑separated line.  Agents should use
this format when prompting for section information.

## unscheduled session example

```markdown
### week 5 lecture
- datetime: 2025-10-21
- status: unscheduled
```

Since the session is cancelled or a holiday, no `topic:` field is included.
The validator will warn if `topic:` is present along with `status:
unscheduled`.

## duplicate week number (holiday) example

```markdown
### week 9 lecture
- datetime: 2025-11-11T10:00:00+08:00/2025-11-11T11:20:00+08:00
- topic: regular lecture

### week 9 lecture 2
- datetime: 2025-11-18T10:00:00+08:00/2025-11-18T11:20:00+08:00
- status: public holiday
```

When a timetable repeats a week label during a break, shift subsequent
weeks upward and insert an explicit holiday entry.  The validator also
checks for duplicate numbers.

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

Institution indices should list semesters chronologically.  The validator
warns if headings appear out of order:

```markdown
### 2024 fall
- COMP 3031 (taken)

### 2024 spring
- COMP 2012 (taken)
```

(The above would trigger a warning because 2024 spring precedes 2024 fall.)

```markdown
### 2023 fall
### 2024 spring
### 2024 fall
```

is the correct sequencing.

The validator warns if an exam section precedes any regular session.

```markdown
- topic ::@:: Type inference and Hindley–Milner
- takeaway ::@:: Principal type inference reduces annotation burden; watch for let-polymorphism corner cases
- COMP 3031 / Hindley–Milner ::@:: Unify constraints from expression syntax tree and solve by substitution

Keep glossary one-liners concise; these are the primary source of flashcards via `::@::` markup.
```

## Taxonomy / chain notation (observed)

```markdown
- _(begin)_→::@::←blue ocean strategy: Break the value–cost tradeoff. For example, London cab services (red) and Uber (blue).
- blue ocean strategy: Break the value–cost tradeoff.→::@::←business model canvas
- business model canvas→::@::←competitor analysis
- ...
- value proposition canvas→::@::←_(end)_
```

## Takeaway shorthand (normalization suggestion)

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

## Flashcard activation tag (example frontmatter)

```markdown
---
tags:
  - flashcard/active/special/academia/<INSTITUTION>/COMP_3031
  - function/index
---
```

These examples are institution-agnostic; replace `<INSTITUTION>` with the canonical short name you use (e.g., `HKUST`, `MIT`, `STANFORD`). Use underscores for course codes inside the tag (e.g., `COMP_3031`).
