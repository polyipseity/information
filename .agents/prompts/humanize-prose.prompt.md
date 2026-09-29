---
description: "Use when a note's sentences read acceptably but the information arrives in the wrong order. Rewrites one file for readability, prose and flashcards together."
name: "Humanize note prose"
applyTo: "**"
alwaysApply: false
---

# Note prose order pass

Rewrite one academic note for readability, prose and flashcards together, and change nothing else in the repository.

## 0. Read the humanizer skill first

__Before you edit anything__, load the `humanizer` skill and read it in full:

- Path: `~/.agents/skills/humanizer/SKILL.md`

Do not work from a summary of it, and do not from memory of these rules.

## 1. Target file

`<path/to/note.md>`

Edit this file and no other file in the repository.

## 2. What the defect is

Sentence-level editing has already been done on this note. The sentences are grammatical, the words are plain, and it still reads wrong, because the defect is the __order__ the information arrives in.

Rewording sentences is therefore not the job. A paragraph reworded in the wrong order stays in the wrong order. What you are fixing is which paragraph comes first, which term arrives before the thing that gives it meaning, and which example is doing the work.

## 3. Diagnose the order before rewriting anything

Go through the note and label every paragraph with the job it does, choosing from this fixed vocabulary:

- gives an example
- defines a term
- lists things
- draws a consequence
- adds background
- repeats an earlier point

Only then decide the new order. Only then write a sentence. A pass that starts editing on sight reproduces the paragraph it was given.

Then: merge two paragraphs that do the same job, split any paragraph doing three jobs, move every example earlier than the rule it illustrates, move every term later than the point that needs it, and delete a paragraph that only repeats an earlier one.

## 4. Ask these questions, do not tick these boxes

A lettered list turns an editing agent into a ticker, and a ticker reports success while changing nothing a reader would notice. Apply these with judgement, and expect to move a paragraph rather than to satisfy a line.

Could a reader picture this? Is the first sentence a word the reader cannot yet picture, with the example stranded behind it?

Does the paragraph's first word have an antecedent? A dangling "It answers…" is the most common symptom of a paragraph assembled in the wrong order.

Where is the point? Would a reader who stopped after the first sentence be holding the thing that matters?

Is there a before and an after, in that order? Does the conclusion arrive before the mechanism the reader needs to hold it?

Which two paragraphs would a reader want only once? One paragraph, one job, cuts both ways: merge same-job paragraphs, split a paragraph doing three.

## 5. Word choice

Use this as a guideline, not a lookup table. Keep a technical term the subject genuinely needs, and drop it when a plain word does the job.

| Roundabout | Plain |
| --- | --- |
| withhold | hide |
| tilt the result | change it |
| stay in the dark | not be told |
| expectation | what someone expects |
| inert | contains nothing |
| demonstrate | show |
| indicate | show |
| facilitate | help |
| attempt | try |
| sufficient | enough |
| prior to | before |
| in order to | to |
| a number of | several |
| constitutes | is |
| exhibits | shows |
| modifies | changes |
| utilise | use |
| subsequent | later |
| approximate | rough |

## 6. Connectives to cut

Cut most of these: "so", "which is why", "therefore", "thus", "hence", "moreover", "furthermore", "at the same time", "in addition", "as a result", "it is worth noting", "in other words", "that said".

The default is two short sentences instead of one joined by a connective. A connective earns its place only when the relation is real and a full stop would not carry it.

## 7. Sentence shape

Aim for 12 to 20 words, with a ceiling of 30. One idea per sentence, and prefer active voice with the doer named. A semicolon is a failure signal: split it. Three or more "and"s in a sentence means split it. Never stack a list inside a list.

## 8. Flashcards

Build the cards to match the new prose and the new order. A card must be answerable on its own, with no context from the note. One claim per card, and a card holding two claims is two cards. Merge two cards that ask the same thing. A short clear phrase beats a full sentence, so do not bolt a verb onto a noun-phrase fragment just to make it grammatical.

Cut a prompt that repeats its answer, an answer that repeats its prompt, and a trailing justification clause. Keep the hint words that make a cloze answerable. Never cut a given or a piece of notation out of a prompt: that breaks a calculation card instead of shortening it.

## 9. Constraints

- Edit only the target file. No other file in the repository changes, and no new file is created.
- __Never run git.__ Not `status`, not `show`, not `diff`, not `rev-parse`, not `rev-list`, not `add`, not `log`, not anything. The ban is absolute; there is no read-only exception.
- Do not rename, add, remove, or reorder any heading. Session entries in the course `index.md` link to `#section%20anchors`, so heading text and heading order are frozen.
- Do not touch the frontmatter: no tag, alias, `status:`, or metadata change.
- Do not change any factual claim, number, measurement, term, or citation. If something is factually wrong, leave it as it is and report it in the report below.
- Do not break or retarget any link, and keep image alt text accurate to what the image shows.
- __Never make an edit that changes only part of a sentence.__ Replace the whole paragraph. A partial edit is exactly what produces a cosmetic result that reports success and changes nothing a reader would notice.
- A quantitative length target is guidance only. Deleting a real fact to hit one is a failure, and padding to hit one is a failure too.
- Do not pad, and do not narrate a source: "the deck", "the slides", "the lecture" and "the course" never take a sentence as their subject.

## 10. Report

Report all of the following:

- the new order you chose, and why that order
- which paragraphs moved, and where they went
- which paragraphs were merged, split, or deleted, and which job labels were involved
- the before and after word counts, reconstructed from your own initial read of the file, plus the card count before and after
- anything factually wrong you found and deliberately left alone
- any `two_sided_calc_warning` suppression you found stranded by a cut prompt, since `academic-lint` errors on one
