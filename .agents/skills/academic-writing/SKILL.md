---
name: academic-writing
description: Pass over all written content in an academic note, prose and flashcards alike, so the information arrives in the order a reader needs it. Covers prose, cards, lists, tables, and reference lines. Load this after any edit to a note's prose or cards, before academic-lint.
---

# Academic writing pass

## When this pass runs

Run this pass after any edit to note prose or flashcards, and before `academic-lint`. It is not a fresh-ingestion step. A corrected fact, a renamed heading, a rewritten card, a sentence added to a lab write-up: each one takes it. Sweeping the text that changed is what counts. Running the pass as you edit and batching several edits to the end of a run are both fine. Skipping it is not.

The pass is out of scope for quoted source text, the body of a Wikipedia transclude, a verbatim question from a paper, heading text, table rows, and anything inside a pytextgen fence. Session entries link to `#section%20anchors`, so a heading is never a rewrite target and renaming one costs no prose work here.

## Diagnose the order before rewriting anything

Go through the note and label every paragraph with the job it does, choosing from this fixed vocabulary: gives an example, defines a term, lists things, draws a consequence, adds background, repeats an earlier point.

The diagnostic covers prose and the order of cards, because both are sequences a reader walks through in turn. It reaches a list, a table, and a reference list the same way: the reader is moving through their items in an order, and a bad order costs them the same way a bad paragraph order does.

A single table cell, and a single reference line, hold no sequence of their own. There is nothing to arrange inside one, and pretending otherwise is a way of doing nothing while reporting a pass. The order lives one level up, in the list of cells and the list of entries.

Only then decide the new order, and only then write a sentence. Merge two paragraphs that do the same job. Split any paragraph doing three jobs. Move every example earlier than the rule it illustrates. Move every term later than the point that needs it. Delete a paragraph that only repeats an earlier one.

__This planning is the actual work.__ A pass that starts editing on sight reproduces the paragraph it was given. Three separate passes over one course each fixed something real (sentence length, filler words, abstract wording) and each left notes that were correct and still hard to read. The pass that fixed order is the one that worked.

## The order principles, as questions to ask

Do not read these as a checklist. A lettered list turns an editing agent into a ticker, and a ticker reports success while changing nothing a reader would notice. Apply them with judgement, and expect to move a paragraph rather than to satisfy a line.

Could a reader picture this? Open a section with the example, the situation, or the thing that actually happens, and name the technical term later, where the reader now wants the name. __Concrete before abstract__ is the test: if the first sentence is a word the reader cannot yet picture, the example is somewhere behind it.

Does the paragraph's first word have an antecedent? Never open with a term the reader has no context for, and never write "It answers..." when nothing named an "it". A dangling pronoun is the most common symptom of a paragraph that was assembled in the wrong order.

Where is the point? Put it first instead of building to it and delivering it in a trailing clause. A reader who stops after the first sentence should hold the thing that matters.

Is there a before and an after? Say what happens, then say what it leads to. If the consequence comes first and the mechanism second, the reader has to hold the conclusion while waiting for the reason.

Which of these two paragraphs would a reader want twice? Two paragraphs doing the same job are one paragraph, so merge them. A paragraph that defines a term, then lists things, then draws a consequence is doing three jobs, so split it. __One paragraph, one job__ cuts both ways.

## The same questions, asked of the other structures

A reader walks a list, scans a table, and hunts a name in a reference list. Each of those is a sequence too, and the order inside it is just as capable of costing the reader as a bad paragraph order.

Can a reader predict the order? A list of steps runs in causal order, a list of definitions in the order the prose introduces them, a list of examples with the clearest one first. A list whose order you cannot predict is a set the reader has to hold in their head all at once, which is what a list was supposed to prevent.

Do a table's rows follow the order the prose discusses them in? When the table reorders its own rows against the surrounding text, the reader builds a second index in their head to match a row back to the paragraph. That is the cost the table was supposed to remove. When the table is genuinely the only place the list exists, order it so the table can be scanned: what a reader compares first goes first.

Does a card block start with its foundational claim? Rebuilding card order to match the prose is the floor, not the ceiling. A block that opens with an incidental detail and saves the claim the section exists to make trains the wrong thing first.

Are reference entries in an order a reader can find a name in? Alphabetical is the default, and grouped by the argument the sources serve is a real alternative when the note discusses them in sequence. What a reference list must not be is the order the sources happened to be read in, because nothing in that order is for the reader.

None of these has one right answer, and a pass that asserts a single correct order for tables is inventing a rule the note never asked for. Ask which order the reader is being served, then check that the note actually uses it.

## A worked example

Before:

> Blinding hides the information that would let anyone taking part tilt the result. When the participants stay in the dark as well, the study is double-blind. It answers two expectations random assignment does not: what a participant thinks is expected of them, and what an experimenter expects to see. Both are ordinary, and nobody admits to either, so a new treatment trial hands half the participants a pill that looks like the real one but contains nothing.

The order is wrong in four ways, and none of them is a grammar mistake. It opens with the term "Blinding", which the reader cannot yet picture. "It answers" uses an "It" that was never given an antecedent, and it names the two problems only after relying on them. The concrete example, the fake pill, arrives last, buried in a "so" clause, when it is the most vivid thing in the paragraph. And "tilt the result", "stay in the dark" and "expectations" are roundabout words standing in for simple ones.

After:

> A trial of a new drug gives half the participants a pill that looks real and contains nothing. Blinding hides that from them, so they cannot act on what they have taken. It also hides it from the experimenter, who would otherwise guess which participants got the real pill. That guess is not cheating. An experimenter who hopes a treatment works reads the confident patient as a success and the hesitant one as a failure. Random assignment removes that problem by deciding who gets what at random. It cannot stop a participant from guessing which pill they took. Hiding the treatment from both is what makes a study double-blind.

What changed is the order, not the vocabulary. The pill comes first, so the reader has something concrete to hold for the rest. Each of the two problems now has its own subject, so no "It" dangles. The experimenter's problem is explained with a concrete scene, and the claim that it is not cheating is made before the mechanism that fixes it. The term "double-blind" arrives last, at the point where the reader finally has everything it means. __Copy the method, not the words.__

## Word choice

Use this as a guideline, not a lookup table. Keep a technical term when the subject genuinely needs it, and drop it when a plain word does the job.

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

## Connectives

Cut most of these: "so", "which is why", "therefore", "thus", "hence", "moreover", "furthermore", "at the same time", "in addition", "as a result", "it is worth noting", "in other words", "that said".

The default is two short sentences instead of one joined by a connective. A connective earns its place only when the relation is real and a full stop would not carry it, so keep "so" when the second sentence is genuinely a consequence and drop it when the two sentences merely sit next to each other.

## Sentence shape

Aim for 12 to 20 words, with a ceiling of 30. One idea per sentence, and prefer active voice with the doer named. A semicolon is a failure signal: split it. Three or more "and"s in a sentence means split it. Never stack a list inside a list.

The rule that matters most here: __never make an edit that changes only part of a sentence, replace the whole paragraph.__ A partial edit is exactly what produces a cosmetic result that reports success and changes nothing a reader would notice. When only a clause is wrong, rewrite the paragraph around it rather than patching the clause.

## Flashcards

Cards carry most of the content in this repository, and nothing enforces their length, so this is where a writing pass has the most to find. A card answer has to be recalled in seconds, and a long one is worse than a long paragraph, because a reader can re-read a paragraph but a card gives one attempt.

A prompt that gives its own answer away is broken rather than long: the recall it was built for never happens, and no amount of trimming repairs it. A prompt that runs long is a paragraph in disguise, sitting where the reader expected a question. A card that carries two claims is two cards, and two cards that ask the same thing are one card, since the second adds nothing to recall.

Order follows the prose. When a section is reordered, rebuild the card order with it, so that a card asked second is not the one that carries the section's opening claim. Never add a card in order to reach coverage: a claim with no card is not a claim the note makes. Where a table row already states a fact, neither prose nor a card restates it.

A short clear phrase beats a full sentence, so do not bolt a verb onto a noun-phrase fragment just to make it grammatical, because that inflates the answer without adding meaning. What must never be cut is a given or a piece of notation: removing one from a prompt breaks a calculation card rather than shortening it, and the card is then unanswerable rather than merely long.

## Lists

A list item that runs to a paragraph is a list that has stopped being a list, and the reader loses the scan that made it worth having. Either split the item across several items, one claim each, or lift the whole thing out of the list and let it stand as a paragraph beside it. Do not shorten a genuine claim to fit the shape; a list that only holds half a fact is worse than prose.

## Tables

A cell holding a sentence is a paragraph wearing a table's clothes, and it also breaks the alignment that made the table readable. Cut it back to the term or the short phrase the cell is there to hold. If a row genuinely needs the reasoning, give it a note underneath the table instead of widening the cell, and let the note follow the same order rules as any other paragraph.

## References

A reference line is a citation, not prose, and prose is what makes it long. Keep it to author, year, title, and a source. Do not write a summary of what the source says in the reference line, because that is the note's claim and it belongs in the body, where the order diagnostic can place it.

## What the pass must not do

Accuracy beats style in every conflict. Do not change a factual claim, a number, a measurement, a term, or a citation. If something is factually wrong, leave it and report it instead of quietly fixing it.

Do not pad, and do not delete a real fact to hit a length target. Do not narrate a source: "the deck", "the slides", "the lecture" and "the course" never take a sentence as their subject.

After rewriting, recheck every `two_sided_calc_warning` suppression. Cutting a prompt can strand one, and `academic-lint` errors on a stranded suppression.

## Relation to the humanizer skill

The `humanizer` skill at `~/.agents/skills/humanizer/SKILL.md` is still loaded, and it still owns the surface AI-writing patterns it documents. Its instruction to "rewrite the smallest spans needed to fix them" is __superseded for reordering__, and that instruction is precisely what produces a cosmetic result.

Order first, then surface patterns. An agent working on academic notes runs this skill, then humanizer, then `academic-lint`.

## Delegation

When this pass is handed to a subagent, the brief must name this skill and give its path, and must require the child to read the file before editing. It must require the child to report which paragraphs moved, merged, split, or were deleted, since a child that reports nothing measurable has most likely done nothing.

State the ban on partial-sentence edits explicitly, and name the banned git commands explicitly, as "not `status`, not `show`, not `diff`, not `rev-parse`". A general ban on git has been ignored, so the named list is the part that has to be written down.

Before/after numbers must be reconstructed from the child's own initial read. Do not pass counts in the brief, and do not let the child report a delta it never measured.
