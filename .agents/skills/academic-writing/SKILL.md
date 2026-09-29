---
name: academic-writing
description: Rewrite a note's written content so the information arrives in the order a reader needs it. Covers prose, flashcards, lists, tables, and reference lines. Load it after any edit to a note's prose or cards, and before academic-lint.
---

# Academic writing pass

Start with a paragraph that reads badly. This one comes from a note on trial design.

Before:

> Blinding hides the information that would let anyone taking part tilt the result. When the participants stay in the dark as well, the study is double-blind. It answers two expectations random assignment does not: what a participant thinks is expected of them, and what an experimenter expects to see. Both are ordinary, and nobody admits to either, so a new treatment trial hands half the participants a pill that looks like the real one but contains nothing.

After:

> A trial of a new drug gives half the participants a pill that looks real and contains nothing. Blinding hides that from them, so they cannot act on what they have taken. It also hides it from the experimenter, who would otherwise guess which participants got the real pill. That guess is not cheating. An experimenter who hopes a treatment works reads the confident patient as a success and the hesitant one as a failure. Random assignment removes that problem by deciding who gets what at random. It cannot stop a participant from guessing which pill they took. Hiding the treatment from both is what makes a study double-blind.

Nothing was shortened. No sentence was over 30 words, and every one was already active. The paragraph was still hard to read, and the reason was the order. It opened with the term __blinding__, which a reader meeting this note for the first time cannot picture. It used an "It" that had never been given an antecedent, and it named the two problems only after relying on them. The fake pill, the most vivid thing in the paragraph, sat in the last clause of the last sentence. And it asked the reader to hold an abstraction for four sentences before showing them anything.

So the pass is not a tidy-up. __You rewrite the text and you put it in a different order.__ Editing a clause inside a badly ordered paragraph leaves a badly ordered paragraph, and it costs the reader exactly as much as it did before. When only part of a sentence is wrong, rewrite the whole paragraph around it rather than patching the clause.

Everything below follows from that example.

## What the pass covers, and when

Run it after any edit to a note's prose or cards, and before `academic-lint`. A corrected fact, a renamed heading, a rewritten card, a sentence added to a lab write-up: each takes it. So does a section you have just rearranged, since moving paragraphs usually breaks the order of the cards beside them.

Leave alone quoted source text, the body of a Wikipedia transclude, a verbatim question from a paper, heading text, and anything inside a pytextgen fence. Session entries link to `#section%20anchors`, so a heading is never a rewrite target. A table cell holding a word or two is doing its job; the pass checks the order of the rows rather than rewriting the cells.

## How to rewrite

Label every paragraph with the job it does, choosing from this fixed vocabulary: gives an example, defines a term, lists things, draws a consequence, adds background, repeats an earlier point. Decide the new order from the labels, and only then write a sentence. On that basis, merge two paragraphs doing the same job, split any paragraph doing three, move every example ahead of the rule it illustrates, move every term after the point that needs it, and cut a paragraph that only repeats an earlier one.

Do not turn this into a checklist. A lettered list of rules makes an editing agent work down the lines and report success while changing nothing a reader would notice. Expect to move a paragraph rather than to satisfy an item.

The rewrite is a rewrite, not a touch-up. Sentence length, filler words, and abstract wording have already been swept out of this material, and each sweep left notes that were correct and still hard to read. What fixed them was moving things.

## The same questions, asked of everything else

A reader walks a list, scans a table, drills a card block, and hunts a name in a reference list. Each is a sequence, and the order inside it costs the reader what a bad paragraph order costs. A single cell, and a single reference line, hold no sequence of their own. The order lives one level up, in the list of cells and the list of entries.

Can a reader predict the order of a list? Steps run in causal order. Definitions run in the order the prose introduces them. A list of examples puts the clearest first. A list whose order you cannot predict is a set the reader has to hold all at once, which is what a list was supposed to prevent.

Do a table's rows follow the order the prose discusses them in? When a table reorders its own rows against the surrounding text, the reader builds a second index in their head to match a row back to a paragraph. That is the cost the table was supposed to remove. When the table is the only place the list exists, put first whatever a reader compares first.

Does a card block open on its foundational claim? Matching the prose is the floor, not the ceiling. A block that starts on an incidental detail and saves the claim the section exists to make drills the wrong thing first.

Can a reader find a name in the reference list? Alphabetical is the default, and grouping by the argument the sources serve is a real alternative when the note discusses them in sequence. The order the sources happened to be read in serves nobody.

None of these has one right answer, and a pass that asserts a single correct order for tables is inventing a rule the note never asked for. Ask which order the reader is being served, then check that the note actually uses it.

## Flashcards

Cards carry most of the content in this repository, and nothing enforces their length, so this is where a pass finds the most. A card answer has to be recalled in seconds, and a long one is worse than a long paragraph: a reader can re-read a paragraph, a card gives one attempt.

A prompt that gives its own answer away is broken rather than long. The recall it was built for never happens, and trimming will not repair it. A prompt that runs long is a paragraph in disguise, sitting where the reader expected a question. A card carrying two claims is two cards. Two cards asking the same thing are one card, since the second adds nothing to recall. Never add a card to reach coverage: a claim with no card is not a claim the note makes. Where a table row already states a fact, neither prose nor a card restates it.

A short clear phrase beats a full sentence. Do not bolt a verb onto a noun-phrase fragment to make it grammatical, because that inflates the answer without adding meaning. Never cut a given or a piece of notation from a prompt. That breaks a calculation card rather than shortening it, and the card ends up unanswerable rather than merely long.

## Lists, tables, and reference lines

A list item that runs to a paragraph has stopped being a list, and the reader loses the scan that made it worth having. Split it across several items, one claim each, or lift it out and let it stand as a paragraph beside the list. Do not shorten a genuine claim to fit the shape; a list holding half a fact is worse than prose.

A cell holding a sentence breaks the alignment that made the table readable. Cut it back to the term or the short phrase the cell is there for. If a row genuinely needs the reasoning, put it in a note under the table rather than widening the cell, and let the note follow the order rules as any other paragraph.

A reference line is a citation, not prose, and prose is what makes it long. Keep it to author, year, title, and a source. Do not summarise what the source says there. That summary is the note's own claim, and it belongs in the body where the order rules can place it.

## Reference: words and shape

This section is a lookup, not the method. The example at the top is the method.

Use the plainest word that is still accurate, and keep a technical term when the subject genuinely needs it.

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

Cut most of these: "so", "which is why", "therefore", "thus", "hence", "moreover", "furthermore", "at the same time", "in addition", "as a result", "it is worth noting", "in other words", "that said". The default is two short sentences instead of one joined by a connective. Keep a connective when the relation is real and a full stop would not carry it.

Aim for 12 to 20 words, with a ceiling of 30. One idea per sentence, active voice, the doer named. A semicolon means split it. Three or more "and"s means split it. Never stack a list inside a list.

## What the pass must not do

Accuracy beats style in every conflict. Leave a factual claim, a number, a measurement, a term, and a citation exactly as written. If something is factually wrong, report it rather than quietly fixing it.

Do not pad, and do not delete a real fact to hit a length target. Do not narrate a source: "the deck", "the slides", "the lecture" and "the course" never take a sentence as their subject.

After rewriting, recheck every `two_sided_calc_warning` suppression. Cutting a prompt can strand one, and `academic-lint` errors on a stranded suppression.

## Relation to the humanizer skill

The `humanizer` skill at `~/.agents/skills/humanizer/SKILL.md` is still loaded, and it still owns the surface AI-writing patterns it documents. Its instruction to "rewrite the smallest spans needed to fix them" is __superseded for reordering__, because in a misordered paragraph the smallest span is often the clause that was already fine.

Order first, then surface patterns. An agent working on academic notes runs this skill, then humanizer, then `academic-lint`.

## Delegation

When this pass goes to a subagent, the brief names this skill and gives its path, and makes the child read the file before editing. It also makes the child report which paragraphs moved, merged, split, or were deleted: a child reporting nothing measurable has most likely done nothing.

Say in the brief that the job is a rewrite and not a touch-up, because a child left to infer that will produce the tidy-up. Ban partial-sentence edits explicitly, and name the banned git commands explicitly, as "not `status`, not `show`, not `diff`, not `rev-parse`". A general ban on git has been ignored, so the named list is the part that has to be written down.

Before/after numbers must be reconstructed from the child's own initial read. Do not pass counts in the brief, and do not accept a delta the child never measured.
