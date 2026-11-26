---
aliases:
  - frame problem
tags:
  - flashcard/active/special/academia/HKUST/SOSC_1960/frame_problem
  - language/in/English
---

# frame problem

The frame problem is the difficulty of writing down all the change that does not happen. Saying what an action changes does not entail that anything else stays as it was.

---

Flashcards for this section are as follows:

- what an action's effects fail to entail ::@:: That everything the action does not affect stays as it was.
- what the frame problem is ::@:: The difficulty of writing down, axiom by axiom, all the change that does not happen.
- what governs the cost of a first-order description ::@:: The number of conditions the description leaves alone.

## frame axioms

A state description in first-order logic is one axiom per fact that holds. An action's axioms give only its effects, so nothing in them stops a block from moving on its own. Each condition an action leaves alone needs a frame axiom, stating that it is unchanged while the action runs. John McCarthy and Patrick J. Hayes posed the problem in 1969, over Hayes's block world of stacking rules.

---

Flashcards for this section are as follows:

- what an axiom set entails about a block that nothing moves ::@:: Nothing about its staying put. The axioms state only what each action changes.
- what a first-order description of a robot's world consists of ::@:: One axiom for each fact that holds.
- where the frame problem arises for a robot ::@:: In representing the state of the robot's environment in first-order logic.
- what a frame axiom states ::@:: That every condition an action does not affect is unchanged while that action runs.
- how many frame axioms the frame problem calls for ::@:: One for every pair of an action and a condition the action does not affect.
- who posed the frame problem, and when ::@:: John McCarthy and Patrick J. Hayes, in a 1969 article.
- the example the frame problem is stated over ::@:: A block world of stacking rules.

## limits of the rule-based approach

### growth of the axiom set

A rule-based system works inside an information-encapsulated world: a limited range of inputs, and a determinate task. Every fact that could bear on a step is listed as unchanged, so the axiom set grows faster than the reasoning it supports. Real perception and language widened the inputs until rule-based [artificial intelligence](artificial%20intelligence.md) stalled.

---

Flashcards for this section are as follows:

- the two conditions a rule-based system works within ::@:: An information-encapsulated world with a limited range of inputs, and a determinate task.
- what an information-encapsulated system limits ::@:: The range of inputs it works with.
- what a rule-based system's task must be ::@:: Determinate, and small enough for a computationally tractable algorithm.
- what widening the range of potentially relevant information does to the frame problem ::@:: Makes it more intractable.
- why rule-based artificial intelligence stalled on real perception and language ::@:: The range of information bearing on a step widened past what the list could carry.

### Dennett's robots

A robot must fetch a spare battery from a room holding a ticking bomb. R1 pulls its wagon out on a valid plan, leaves the bomb on the wagon, and the bomb goes off. R1D1 was built to deduce what its actions change first. Without a relevance rule, it deduces room temperature and wall colour too. The bomb goes off while it reasons.

R2D1 adds a relevance filter and a junk box for irrelevant deductions. Deciding whether a deduction belongs in the junk box is itself a deduction, so the sorting never ends and the bomb goes off again. A filter written as a rule cannot decide relevance, so the robots lack framing, not speed.

---

Flashcards for this section are as follows:

- what R1 does with the wagon in the room holding the spare battery and the ticking bomb ::@:: Pulls it out on a valid plan, leaves the bomb on it, and the bomb goes off.
- what R1D1 was built to deduce before it acts ::@:: What its actions change.
- what R1D1 deduces that is irrelevant ::@:: Room temperature and wall colour.
- what R1D1's deduction of the effects of its actions costs it ::@:: The bomb goes off while it reasons.
- what R2D1 adds that R1D1 lacks ::@:: A relevance filter and a junk box for irrelevant deductions.
- why R2D1's junk box never settles what belongs in it ::@:: Deciding whether a deduction belongs in the junk box is itself a deduction.
- what R1, R1D1 and R2D1 lack ::@:: Framing, not speed.

## beyond the machine

In logic an action is specified by its changes. The frame is everything else, assumed to stay as it was. In philosophy the problem moved from logic to belief. After an action, which beliefs must be revised, and how are the rest left alone? Without frame axioms, an argument may conclude changes that nothing made.

---

Flashcards for this section are as follows:

- how the frame problem was generalised in philosophy ::@:: From logic to belief, as the question of which beliefs an action revises.
- the two questions the philosophical frame problem asks after an action ::@:: Which beliefs must be revised, and how the rest are left alone.
- how the logical context specifies an action ::@:: By what it changes, with everything else assumed to remain unchanged.
- what the frame of an action consists of ::@:: Everything the action leaves unchanged.
- what an argument may conclude without frame axioms ::@:: Changes that nothing made.

## references

- Wikipedia contributors. (n.d.). _Frame problem_. Wikipedia, The Free Encyclopedia. Retrieved November 18, 2026, from <https://en.wikipedia.org/wiki/Frame_problem>
    - Source of the first-order logic statement of the problem, the 1969 article by John McCarthy and Patrick J. Hayes, the block world described by Patrick J. Hayes, and the generalisation of the problem to belief.
- McCarthy, J., & Hayes, P. J. (1969). Some philosophical problems from the standpoint of artificial intelligence. _Machine Intelligence_, _4_, 463-502.
    - The article the entry above credits with defining the frame problem.
- \[missing\].
    - Source of the information-encapsulated world with a limited range of inputs and the determinate task, of the claim that the problem grows more intractable as the range of potentially relevant information widens, and of the attribution to José Luis Bermúdez (Cambridge University Press, 2010).
- \[missing\]. (\[missing\]). [The Frame Problem in AI](https://www.youtube.com/watch?v=EVAKG6Y2uIg) [Video]. YouTube.
    - Source of the battery-and-bomb thought experiment, of the robots R1, R1D1 and R2D1, of their relevance filter and junk box, and of the argument that what a relevance filter written as a rule cannot supply is framing rather than speed.
    - The thought experiment originates in Daniel Dennett, _Cognitive Wheels: The Frame Problem in AI_ (1984).
