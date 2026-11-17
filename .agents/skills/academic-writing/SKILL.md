---
name: academic-writing
description: Run this on prose that is not acceptable yet, whatever the defect is, a packed sentence, a hidden point, the wrong order, or padding. It names each part's job, splits the sentences doing several, moves the parts into the order a reader needs, cuts what earns nothing, and ends at the humanizer pattern list. Covers prose and cards. Load it after any edit to a note's prose or cards, and before academic-lint.
---

# Academic writing pass

This pass moves material until a reader can follow it, then ends at the [humanizer](~/.agents/skills/humanizer/SKILL.md) list, which is the bar for the surface. Run this, then humanizer, then `academic-lint`.

Two ways to get it wrong. Running only humanizer is one: it rewrites the smallest span that fixes a pattern, so a sentence doing three jobs stays packed. Running only this pass is the other, and it is the commoner of the two. What this pass breaks is surface damage. One packed sentence split into five comes out repetitive. A cut paragraph leaves its survivors pointing at a "this" with nothing antecedent. Whoever breaks it finishes it.

## Style authority

Register, heading grammar, and section order follow Wikipedia's [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style). Where this pass and the humanizer list disagree, Wikipedia decides what a section is called and how a fact is stated, and the humanizer list decides only whether a sentence reads as machine-written.

| Wikipedia page | What it decides here |
| --- | --- |
| [MOS:HEADINGS](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Section_headings) | sentence case, a noun phrase, no question, no terminal punctuation, no repetition of the note title |
| [MOS:LEAD](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lead_section) | the opening says what the concept is before any mechanism |
| [MOS:PARAGRAPHS](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Paragraphs) | one idea per paragraph, and no one-sentence section |
| [MOS:PROSE](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Prose) | a list only where a list is the right form |
| [WP:PEACOCK](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Words_to_watch#Puffery) and [MOS:WTW](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Words_to_watch) | no promotional adjective, no word doing the work of a fact |
| [WP:NPOV](https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view) | no editorialising, and no narrating where the material came from |
| [MOS:NUM](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Dates_and_numbers) | units, ranges, and significant figures |
| [MOS:LINK](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Linking) | the first mention carries the link |
| [MOS:CONCISENESS](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Writing_clearly) | every sentence earns its place; cut before you add |

A note states. It does not instruct, persuade, or tell the reader what a source asked.

## When to run it, and what to leave alone

Run it after any edit to a note's prose or cards, and before `academic-lint`. A corrected fact, a rewritten card, a sentence added to a lab write-up: each takes it. A heading renamed elsewhere takes the pass on the prose that referred to it, not on the heading, which is frozen here. A section you have just rearranged takes the pass too. Moving paragraphs usually breaks the order of the cards beside them.

Leave alone quoted source text, the body of a Wikipedia transclude, a verbatim question from a paper, and anything inside a pytextgen fence. Session entries link to `#section%20anchors`, so a heading is never a rewrite target here, and moving one means repointing every anchor that reaches it.

## What goes wrong

A paragraph hands the reader a conclusion before the ground it stands on. A sentence hands the reader three facts at once and expects them to sort themselves out. Both ask the reader to hold something they cannot yet make sense of. The cause is the same in each: too many things doing too much work in too small a space.

| Scale | One unit is | The unit is broken when |
| --- | --- | --- |
| Note | the whole run of sections | it carries a section nothing needs, or lacks the one a reader needs first |
| Section | one run of headings under one name | its name is a sentence or a phrase that points, or it sits after the section that needs it |
| Paragraph | one block of prose | it does three of the jobs below, or two blocks do the same one |
| Sentence | one statement | it does two of the jobs below |
| Clause | a modifying phrase inside a sentence | the explanation arrives before the thing it explains |

The jobs are: gives an example, defines a term, lists things, draws a consequence, adds background, repeats an earlier point.

## Concision

Less is more, and the unit it applies to is the sentence, not the fact. Three deletions come before any rewording:

- a sentence that repeats its neighbour, which includes the one that announces what the next sentence will say;
- a section that restates the lead, or a paragraph that restates its own first sentence;
- an adjective, adverb, or aside that carries no measurement and no relation.

Report words removed against words added. Removal should win, and a pass that ends with more words than it started with has to name the fact it added. Padding earns no place, and neither does a sentence kept only because deleting it would leave the paragraph short.

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

## The pass

Do not turn this into a checklist. A lettered list of rules makes an editing agent work down the lines and report success. Nothing a reader would notice has changed. Expect to move a section, take a sentence apart, and delete a paragraph, not to satisfy an item.

__Cut before you rewrite.__ A paragraph that only repeats an earlier one is not badly written, it is unnecessary, and no rewriting makes it earn its place. Deletion is a move in this pass, and it is usually the one that helps most. Reach for it first, and expect the pass to end with less text than it started with.

__Place before you polish.__ Decide the skeleton first: which sections the note needs, in what order, and which paragraphs belong in each. A section sitting after the section that needs it is not a prose problem, and rewriting its sentences will not move it. Splitting one section in two is often the honest answer. Two notes arguing the same point are better merged than both kept. When the skeleton is settled, settle the clause and the sentence inside its final home. A clause polished inside a paragraph that is about to move two sections down is work thrown away.

__Name the section.__ A section name is a term, not a description of the paragraph under it: `time constant`, not `the time constant`; `hysteresis`, not `the state it keeps`. A name carrying a finite verb is a sentence wearing a heading, and a leading article is the same defect half-finished. Renaming is the levelling pass's job, not this one, because the session entries point at the old anchor; report the name that needs changing and let the levelling pass do it.

__Then take a sentence apart.__ Name each part's job, then write one sentence per job, in the order those labels imply. Choose the words last, once the jobs are separate. Reaching for a better word to describe a sentence that is doing three jobs polishes the packing instead of undoing it. The note comes out shorter and no clearer.

__End on a full stop.__ A connective is not a shorter full stop. It is a claim that the two halves cannot stand alone, and most of the time they can. Write the two halves as two sentences. Keep "so" only where the result really is a result, and "but" only where the opposition changes what the reader should conclude. A sentence doing one job usually lands under 25 words.

__Then hand over.__ Once the order and the packing are right, run the [humanizer](~/.agents/skills/humanizer/SKILL.md) skill over what you changed. It holds the list. This pass holds the structure. Both run.

## When the defect is architectural

A reported readability defect is not repaired by rewording clauses. The lint measures sentence length, vocabulary, and section width at once, so a note that fails three metrics has too much packed into too few sections, and the answer is a different shape: merge two sections doing the same job, split one carrying three, move a paragraph to the section that needs it, delete the section that restates the lead.

A rewrite at that scale reports what it moved. A pass that comes back with polished sentences and the same section tree has not done the work, whatever the score now says.

## Reading level

The target is a university reader, on the secondary side of that line: not graduate density, and not primary-school fragments either. `.agents/skills/academic-lint/SKILL.md` holds the seven metrics and their bands. Two things matter here.

A short sentence and a plain word are not defects, and the lint's lower bound exists only to catch prose written down to a child. Do not lengthen a sentence or reach for a harder word to lift a score.

Clearing a metric by padding, or by shredding one sentence into four fragments, is a worse defect than the one reported. Fix the shape, then read the score.

## Running humanizer

The [humanizer](~/.agents/skills/humanizer/SKILL.md) list is the bar. Read it in full, and do not work from a summary of it or from memory of it. Half the patterns on it are ones a reader notices without being able to name them, which is why a remembered list is worse than none at all.

Its instruction to "rewrite the smallest spans needed to fix them" is __superseded here__, for packing, for order, and for concision. In a sentence doing three jobs the smallest span is often the clause that was already fine, and a span that only repeats its neighbour has to go rather than improve.

## Before reporting done

Read every sentence you changed against that list and quote each pattern still standing. An em dash, a participle opener, a bolded fragment, a synonym that only exists because the first one was used: name each and fix it, or say why it stays.

A pass that cannot quote a surviving pattern has not checked. Neither "it reads well now" nor a before-and-after word count answers the question, because both grade the edit rather than the sentences.

## Lists, tables, cards, and reference lines

A reader walks a list, scans a table, drills a card block, and hunts a name in a reference list. Each is a sequence. Getting the order wrong inside one costs the reader what getting it wrong between paragraphs costs. A single cell and a single reference line hold no sequence of their own; the order lives one level up.

No structure here has one right order. Ask which order the reader is being served, then check that the note actually uses it.

### Lists

Can a reader predict the order? Steps run in causal order. Definitions run in the order the prose introduces them. A list of examples puts the clearest first. An order the reader cannot predict is a set they have to hold all at once, and preventing that is what a list is for. Never stack a list inside a list.

A list item that runs to a paragraph has stopped being a list, and the reader loses the scan that made it worth having. Split it across several items, one claim each, or lift it out to stand as a paragraph beside the list. Do not shorten a genuine claim to fit the shape.

### Tables

Do the rows follow the order the prose discusses them in? A table that reorders its rows against the surrounding text makes the reader build a second index in their head, which is the cost the table was meant to remove. When the table is the only place the list exists, put first whatever a reader compares first.

A cell holding a sentence breaks the alignment that made the table readable. Cut it back to the term or short phrase the cell is there for. If a row genuinely needs the reasoning, put it in a note under the table, and let that note take the order rules like any other paragraph.

### Cards

Cards carry most of the content in this repository, and nothing enforces their length. A card answer has to be recalled in seconds, and a long one is worse than a long paragraph. A reader can re-read a paragraph; a card gives one attempt.

Does the block open on its foundational claim? Matching the prose is the floor, not the ceiling. A block that starts on an incidental detail and saves the claim the section exists to make drills the wrong thing first.

Take a card apart the way you take any sentence apart. A prompt that gives its own answer away is broken rather than long, and trimming will not repair it. A prompt that runs long is a paragraph in disguise, sitting where the reader expected a question. A card doing two claims is two cards, and two cards asking the same thing are one card. Never add a card to reach coverage: a note is allowed to state a fact once in prose and stop there, and where a table row already states a fact, neither prose nor a card restates it.

A short clear phrase beats a full sentence, and do not bolt a verb onto a noun-phrase fragment to make it grammatical. Never cut a given or a piece of notation from a prompt; that breaks a calculation card rather than shortening it. Never shorten a full form to its acronym, or a person's name to a surname: the card viewer shows one line at a time, so the expansion belongs on the line that uses the short form (see "Full forms on every card" in `create-flashcards`).

### Reference lines

A reference line is a citation, not prose. Keep it to author, year, title, and a source, and do not summarise what the source says there: that summary is the note's own claim, and it belongs in the body where the order rules can place it.

Can a reader find a name? Alphabetical is the default, and grouping by the argument the sources serve works when the note discusses them in sequence. The order the sources happened to be read in serves nobody.

## Reference: words and shape

This is a lookup table. The example above is the method.

Use the plainest word that is still accurate, and keep a technical term when the subject genuinely needs it.

| Roundabout | Plain |
| --- | --- |
| withhold | hide |
| tilt the result | change it |
| stay in the dark | not be told |
| expectation | what someone expects |
| demonstrate, indicate | show |
| facilitate | help |
| attempt | try |
| sufficient | enough |
| prior to | before |
| in order to | to |
| a number of | several |
| constitutes | is |
| exhibits, modifies | shows, changes |
| utilise | use |
| subsequent | later |

These usually go: "which is why", "therefore", "thus", "hence", "moreover", "furthermore", "at the same time", "in addition", "as a result", "it is worth noting", "in other words", "that said". "So" and "but" are the two worth keeping, and only where the relation is real.

## What the pass must not do

Accuracy beats style in every conflict. Leave a factual claim, a number, a measurement, a term, and a citation exactly as written. If something is factually wrong, report it rather than quietly fixing it.

Do not pad, and do not delete a real fact to reach a shorter note. Do not collapse a full form into its acronym in prose after first use either, and never in a card. Do not narrate a source: "the deck", "the slides", "the lecture" and "the course" never take a sentence as their subject.

Never edit part of a sentence. Replace the whole paragraph, because a partial edit is what produces a result that reports success and changes nothing a reader would notice.

After rewriting, recheck every `two_sided_calc_warning` suppression. Cutting a prompt can strand one, and `academic-lint` errors on a stranded suppression.

## Delegation

The author never certifies its own prose. An author reading its own sentence has already decided what it says, so the pass runs in a fresh-context child whenever the text's author is still in the room.

The brief gives the file path, both skill paths, and the contract at `.agents/instructions/academic-notes.instructions.md`, and nothing else: no before-state, no diff, no list of what to fix. One child per file, at most two at once.

The brief says five things. It is a rewrite, not a touch-up. Cut before you reword, and deletion is the default verdict. Name the five scales, because a child told only about paragraphs will do paragraphs. Never edit part of a sentence. Never rename a heading, because session entries link to the old anchor; the levelling pass owns renames.

The brief also names the banned reading: the child does not consult git history to see what the note used to say, because a writer who reads it restores old wording instead of rewriting. The change audit's read-only git and the parent's commit are separate mechanisms and stay available.

The parent accepts the result only after comparing, against the pre-pass copy, the card count, each card line's `$...$` set, the heading text, the suppression list, and the whole diff. A report that names no moved section, no deleted paragraph and no split sentence is a report of no work, because the default is to cut. In one run four of ten children reported a finished rewrite and left their file untouched.

Before/after numbers are reconstructed from the child's own initial read. Do not pass counts in the brief, and do not accept a delta the child never measured.
