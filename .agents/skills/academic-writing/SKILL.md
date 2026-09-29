---
name: academic-writing
description: Rewrite a note's written content so a reader can build the meaning as they go. Fixes order and packing at the scale of the clause, the sentence, and the paragraph, in prose, flashcards, lists, tables, and reference lines. Load it after any edit to a note's prose or cards, and before academic-lint.
---

# Academic writing pass

## What goes wrong

A paragraph hands the reader a conclusion before the ground it stands on. A sentence hands the reader three facts at once and expects them to sort themselves out. Both ask the reader to hold something they cannot yet make sense of. The cause is the same in each: too many things doing too much work in too small a space.

The work happens at three scales. A pass that fixes only the largest one will shorten the note and leave it just as hard to read.

| Scale | One unit is | The unit is broken when |
| --- | --- | --- |
| Clause | a modifying phrase inside a sentence | the explanation arrives before the thing it explains |
| Sentence | one statement | it does two of the jobs below |
| Paragraph | one block of prose | it does three of the jobs, or two blocks do the same one |

The jobs are: gives an example, defines a term, lists things, draws a consequence, adds background, repeats an earlier point.

## Example: order

From a note on trial design.

Before:

> Blinding hides the information that would let anyone taking part tilt the result. When the participants stay in the dark as well, the study is double-blind. It answers two expectations random assignment does not: what a participant thinks is expected of them, and what an experimenter expects to see. Both are ordinary, and nobody admits to either, so a new treatment trial hands half the participants a pill that looks like the real one but contains nothing.

After:

> A trial of a new drug gives half the participants a pill that looks real and contains nothing. Blinding hides that from them, so they cannot act on what they have taken. It also hides it from the experimenter, who would otherwise guess which participants got the real pill. That guess is not cheating. An experimenter who hopes a treatment works reads the confident patient as a success and the hesitant one as a failure. Random assignment removes that problem by deciding who gets what at random. It cannot stop a participant from guessing which pill they took. Hiding the treatment from both is what makes a study double-blind.

No sentence was shortened. The paragraph was still hard to read, and the order was why:

- It opened with __blinding__, a term a reader meeting the note for the first time cannot picture.
- It used an "It" with no antecedent.
- It relied on two problems before naming either of them.
- It put the fake pill, the most vivid thing there, in the last clause of the last sentence.

## Example: packing

From this very skill, in an earlier draft.

Before:

> Then merge two paragraphs doing the same job, split any paragraph doing three, move every example ahead of the rule it illustrates, move every term after the point that needs it, and cut a paragraph that only repeats an earlier one.

After:

> Two paragraphs doing the same job become one. A paragraph doing three becomes three. Each example moves ahead of the rule it illustrates. Each term moves after the point that needs it. A paragraph that only repeats an earlier one is cut.

One sentence doing five, and every part carrying the same job. Five parts sharing one job belong in five sentences, not in a chain of clauses joined by "and".

No word changed meaning. The reader now gets one instruction per breath.

## When to run it, and what to leave alone

Run it after any edit to a note's prose or cards, and before `academic-lint`. A corrected fact, a renamed heading, a rewritten card, a sentence added to a lab write-up: each takes it. So does a section you have just rearranged, since moving paragraphs usually breaks the order of the cards beside them.

Leave alone quoted source text, the body of a Wikipedia transclude, a verbatim question from a paper, heading text, and anything inside a pytextgen fence. Session entries link to `#section%20anchors`, so a heading is never a rewrite target.

## The pass

Do not turn this into a checklist. A lettered list of rules makes an editing agent work down the lines and report success while changing nothing a reader would notice. Expect to move a paragraph and take a sentence apart, not to satisfy an item.

Work at the smallest scale first, and work outward. A clause fixed inside a sentence is lost the moment that sentence is moved, so settle each unit before you touch the one above it.

Take a sentence apart before you rewrite it. Name each part's job, then write one sentence per job, in the order those labels imply. Choose the words last, once the jobs are separate. Reaching for a better word to describe a sentence that is doing three jobs polishes the packing instead of undoing it. The note comes out shorter and no clearer.

Do the same outward, and decide the new order from the labels before you write a word of it. Merge two paragraphs doing the same job, and split a paragraph doing three. Move each example ahead of the rule it illustrates, and each term after the point that needs it. Cut a paragraph that only repeats an earlier one.

A sentence doing one job usually lands under 25 words. An over-long one is usually doing more than a single job, so count words only to find the sentence worth taking apart. When the words are already plain and the job count is wrong, cutting words changed nothing.

## Lists, tables, cards, and reference lines

A reader walks a list, scans a table, drills a card block, and hunts a name in a reference list. Each is a sequence, and the order inside it costs what a bad paragraph order costs. A single cell and a single reference line hold no sequence of their own. The order lives one level up, in the list of cells and the list of entries.

None of this has one right answer. Ask which order the reader is being served, then check that the note actually uses it. A pass that asserts one correct row order for tables is inventing a rule the note never asked for.

### Lists

Can a reader predict the order? Steps run in causal order. Definitions run in the order the prose introduces them. A list of examples puts the clearest first. An order the reader cannot predict is a set they have to hold all at once, which is what a list was supposed to prevent.

A list item that runs to a paragraph has stopped being a list, and the reader loses the scan that made it worth having. Split it across several items, one claim each, or lift it out to stand as a paragraph beside the list. Do not shorten a genuine claim to fit the shape; a list holding half a fact is worse than prose.

### Tables

Do the rows follow the order the prose discusses them in? A table that reorders its rows against the surrounding text makes the reader build a second index in their head to match a row back to a paragraph. That is the cost the table was meant to remove. When the table is the only place the list exists, put first whatever a reader compares first.

A cell holding a sentence breaks the alignment that made the table readable. Cut it back to the term or short phrase the cell is there for. If a row genuinely needs the reasoning, put it in a note under the table, and let that note take the order rules like any other paragraph.

### Cards

Cards carry most of the content in this repository, and nothing enforces their length, so this is where a pass finds the most to fix. A card answer has to be recalled in seconds, and a long one is worse than a long paragraph: a reader can re-read a paragraph, a card gives one attempt.

Does the block open on its foundational claim? Matching the prose is the floor, not the ceiling. A block that starts on an incidental detail and saves the claim the section exists to make drills the wrong thing first.

Take a card apart the way you take any sentence apart. A prompt that gives its own answer away is broken rather than long, and trimming will not repair it. A prompt that runs long is a paragraph in disguise, sitting where the reader expected a question. A card doing two claims is two cards, and two cards asking the same thing are one card. Never add a card to reach coverage, because a claim with no card is not a claim the note makes. Where a table row already states a fact, neither prose nor a card restates it.

A short clear phrase beats a full sentence. Do not bolt a verb onto a noun-phrase fragment to make it grammatical, since that inflates the answer without adding meaning. Never cut a given or a piece of notation from a prompt. That breaks a calculation card rather than shortening it, and the card ends up unanswerable rather than merely long.

### Reference lines

A reference line is a citation, not prose, and prose is what makes it long. Keep it to author, year, title, and a source, and do not summarise what the source says there. That summary is the note's own claim, and it belongs in the body where the order rules can place it.

Can a reader find a name? Alphabetical is the default, and grouping by the argument the sources serve works when the note discusses them in sequence. The order the sources happened to be read in serves nobody.

## Reference: words and shape

This is a lookup table. The two examples above are the method.

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

A semicolon means the sentence was doing two jobs. Three or more "and"s means it was doing three. Never stack a list inside a list.

## What the pass must not do

Accuracy beats style in every conflict. Leave a factual claim, a number, a measurement, a term, and a citation exactly as written. If something is factually wrong, report it rather than quietly fixing it.

Do not pad, and do not delete a real fact to hit a length target. Do not narrate a source: "the deck", "the slides", "the lecture" and "the course" never take a sentence as their subject.

After rewriting, recheck every `two_sided_calc_warning` suppression. Cutting a prompt can strand one, and `academic-lint` errors on a stranded suppression.

## Relation to the humanizer skill

The `humanizer` skill at `~/.agents/skills/humanizer/SKILL.md` is still loaded, and it still owns the surface AI-writing patterns it documents. Its instruction to "rewrite the smallest spans needed to fix them" is __superseded here__, for packing as well as for order. In a sentence doing three jobs, the smallest span is often the clause that was already fine.

Order first, then packing, then surface patterns. An agent working on academic notes runs this skill, then humanizer, then `academic-lint`.

## Delegation

When this pass goes to a subagent, the brief names this skill and gives its path, and makes the child read the file before editing. It also makes the child report which paragraphs moved, which sentences were taken apart, and which were deleted: a child reporting nothing measurable has most likely done nothing.

Say in the brief that the job is a rewrite and not a touch-up, because a child left to infer that will produce the tidy-up. Name the three scales in the brief, because a child told only about paragraphs will do paragraphs. Ban partial-sentence edits explicitly, and name the banned git commands explicitly, as "not `status`, not `show`, not `diff`, not `rev-parse`". A general ban on git has been ignored, so the named list is the part that has to be written down.

Before/after numbers must be reconstructed from the child's own initial read. Do not pass counts in the brief, and do not accept a delta the child never measured.
