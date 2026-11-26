---
aliases:
  - AI
  - artificial intelligence
tags:
  - flashcard/active/special/academia/HKUST/SOSC_1960/artificial_intelligence
  - language/in/English
---

# artificial intelligence

Artificial intelligence (AI) is the field that builds machines to do what counts as intelligent: recognising a face, answering a question, playing chess. The name dates from a 1956 summer workshop. The field and psychology have borrowed from each other, and the exchange has quickened over the past decade.

---

Flashcards for this section are as follows:

- what artificial intelligence builds ::@:: Machines that do what counts as intelligent: recognising a face, answering a question, playing chess.
- the year the name artificial intelligence was first used ::@:: 1956, at a summer workshop.
- what psychology has taken from artificial intelligence ::@:: Theoretical models of psychological phenomena, shaped by artificial intelligence's successes and failures.
- what artificial intelligence has taken from psychology ::@:: Subject matter for its models: perception, memory, learning and language.
- how the pace of the exchange between psychology and artificial intelligence has changed ::@:: It has quickened over the past decade.

## Turing's question

Alan Turing's 1950 paper, _Computing Machinery and Intelligence_, asked whether machines can think. The 1956 summer workshop gathered John McCarthy, Marvin Minsky, Nathaniel Rochester, Claude Shannon, Herbert Simon and Allen Newell.

The workshop set four questions. How can a computer be programmed to use a language? How can a set of hypothetical neurons be arranged to form concepts? Can machines form abstractions from sensory and other data? Can machines, beyond a rule-based algorithm, think creatively and intuitively?

A second meeting in September 1956 added Noam Chomsky from linguistics, John Swets from signal detection theory and George Miller from cognitive psychology. Miller dates the birth of cognitive science to that month. The group aimed to explain how the mind works in computational terms.

---

Flashcards for this section are as follows:

- what Alan Turing asked in his 1950 paper ::@:: Whether machines can think.
- the six researchers gathered at the 1956 summer workshop ::@:: John McCarthy, Marvin Minsky, Nathaniel Rochester, Claude Shannon, Herbert Simon and Allen Newell.
- the workshop question about a computer and a language ::@:: How a computer can be programmed to use a language.
- the workshop question about neurons and concepts ::@:: How a set of hypothetical neurons can be arranged to form concepts.
- the workshop question about abstraction from data ::@:: Whether machines can form abstractions from sensory and other data.
- the workshop question about creativity beyond rules ::@:: Whether machines, beyond a rule-based algorithm, can think creatively and intuitively.
- the scholars who joined the September 1956 meeting from other fields ::@:: Noam Chomsky from linguistics, John Swets from signal detection theory and George Miller from cognitive psychology.
- what George Miller dates to the September 1956 meeting ::@:: The birth of cognitive science.

## approaches

### rule-based approach

Early work modelled cognition as information processing: an algorithm that manipulates symbols to reach a goal. Newell, Shaw and Simon held that human problem solving is the execution of such an algorithm. Newell and Simon's theorem prover of 1956 proved complex theorems and improved on the human proofs. From the 1980s into the 2000s the approach produced many models of human reasoning for problem-solving systems (Anderson et al., 1997; Laird, 2019; Rubinstein et al., 2001). The models moved away from the behaviourist mind as a black box and opened the mechanisms of thought, reasoning and problem solving to study.

A rule-based program reasons over a described state of the world, such as the block world of the [frame problem](frame%20problem.md). An action changes a few facts and leaves the rest alone, but the description never says the untouched facts survive, so the program lists them as unchanged after every action. That list covers every fact that could bear on the step and grows faster than the reasoning it supports, so the approach is intractable. Perception and language widen the list without limit. Rule-based artificial intelligence stalled.

---

Flashcards for this section are as follows:

- how early artificial intelligence modelled cognition ::@:: As information processing: an algorithm that manipulates symbols to reach a goal.
- the three researchers who set out the information processing view of problem solving ::@:: Allen Newell, J. C. Shaw and Herbert Simon.
- what Newell and Simon's 1956 theorem prover did ::@:: Proved complex theorems and improved on the human proofs.
- the models of human reasoning the rule-based approach produced from the 1980s into the 2000s ::@:: Many models for problem-solving systems (Anderson et al., 1997; Laird, 2019; Rubinstein et al., 2001).
- what the problem-solving models of the 1980s to 2000s opened to study, where a behaviourist left the mind a black box ::@:: The mechanisms of thought, reasoning and problem solving.
- the two conditions the rule-based approach needed of a task ::@:: An information-encapsulated system with limited inputs, and a determinate task a tractable algorithm could compute.
- why the frame problem stops a rule-based approach being tractable ::@:: Every action needs a list of everything it leaves unchanged, which covers every fact that could bear on a step.

<!-- check: ignore-next-line[header_deep_nesting]: the state-space formulation is a sub-case of the rule-based approach -->
#### state space search

Problem solving became a search over a space of states, each move a step from one state to the next. The three-disk Tower of Hanoi has 27 states, one for each arrangement of the disks, and its solution is a path through them.

![The 27 states of the three-disk Tower of Hanoi, each labelled by which disks sit on which peg, with the starting arrangement and the goal arrangement marked in blue and joined by a path through the graph](attachments/Tower%20of%20Hanoi%203-disk%20graph%20-%20longest%20path.svg)

---

Flashcards for this section are as follows:

- what a problem-solving task became in the rule-based approach ::@:: A search over a space of states, with each move a step from one state to another.
- what one state of a search space stands for ::@:: One arrangement of the problem's objects, such as one placement of the disks on the pegs.
- the number of states in the three-disk Tower of Hanoi ::@:: 27, one for each arrangement of the three disks.
- what a solution is in a search over states ::@:: A path through the states, one move per step.

### neural network approach

An [artificial neural network](artificial%20neural%20network.md) approximates a population of neurons. Its history runs alongside the rule-based one from 1943, when Warren McCulloch and Walter Pitts showed that a single unit can compute logical functions.

---

Flashcards for this section are as follows:

- what an artificial neural network approximates ::@:: A population of neurons, in the respects that matter for the task it is given.
- the year the adaptive network history began, alongside the rule-based one ::@:: 1943.
- what Warren McCulloch and Walter Pitts showed in 1943 ::@:: That a single simple unit can compute logical functions.
- how the rule-based history and the network history relate ::@:: They ran side by side from 1943, and neither replaced the other.

## winters

The early promise ran aground on perception, language and movement, which did not behave like a puzzle. Two AI winters followed, each after a failure on a skill a child manages: language, visual recognition and motor coordination.

Hans Moravec set out the difficulty in 1988: adult-level performance on an intelligence test or at checkers is easy to produce, while the perception and mobility of a one-year-old are difficult or impossible. Steven Pinker's summary is that the hard problems turned out easy and the easy ones hard.

A winter never reset the field: each cycle kept what it learned from its successes and failures.

---

Flashcards for this section are as follows:

- what the early promise of artificial intelligence ran aground on ::@:: Perception, language and movement, none of which behaved like a puzzle.
- what followed the early promise of artificial intelligence (AI) ::@:: Two AI winters.
- what Hans Moravec called comparatively easy for a computer in 1988 ::@:: Adult-level performance on an intelligence test or at checkers.
- what Hans Moravec called difficult or impossible for a computer in 1988 ::@:: The skills of a one-year-old at perception and mobility.
- Steven Pinker's summary of the hard and easy problems ::@:: What looked hard turned out easy, and what looked easy turned out hard.
- what an artificial intelligence winter left behind ::@:: Each cycle kept what it learned from its successes and failures.

### chess

Chess was the exception: Alan Turing wrote an algorithm for playing chess in 1953, Deep Thought reached Grand Master level in the late 1980s, and Deep Blue beat Garry Kasparov in the 1990s. The method was brute-force search of a decision tree, and nobody doubted that the result was intelligent.

Once a computer and an internet connection were common, a player could study recorded games and practise against an engine at home, where a club and a coach had once set the pace. A neural engine gives up material for an attack, so its games show a player how to weigh that trade. Playing one trains the anticipation of a reply, which is what the engine's strength rests on.

Bilalić et al. (2024) found that the play of the best human players improved at two points in the engine's history: the late 1990s, with personal computers and the internet, and the late 2010s, with engines built on deep neural networks.

---

Flashcards for this section are as follows:

- the year Alan Turing wrote an algorithm for playing chess ::@:: 1953.
- the level Deep Thought reached in the late 1980s ::@:: Grand Master.
- how Deep Blue beat Garry Kasparov in the 1990s ::@:: By brute-force search of a decision tree.
- what brute-force search did not put in doubt ::@:: The intelligence of the machine's behaviour.
- what let a chess player study and practise at home instead of at a club ::@:: A computer and an internet connection, with a chess engine to play against.
- what a neural engine that gives up material for an attack teaches a player ::@:: How to weigh a sacrificed piece against the chances it buys.
- what practising against a chess engine trains ::@:: Anticipating the opponent's reply.
- the two points at which the play of the best human chess players improved ::@:: The late 1990s, with personal computers and the internet, and the late 2010s, with deep-neural-network engines.

## present

The recent advance came from hardware and data, not theory. The computational power of machines has risen exponentially, and the graphics processing unit (GPU), built for video gaming, supplies the arithmetic that training a network with millions of parameters demands. The internet supplies the images, text and speech those networks learn from. Earlier systems depended on hand-crafted features; a deep network learns its own from the data.

Results followed at a human level or close to it: object recognition, face recognition, the game of Go and [large language models](large%20language%20model.md). The Contrastive Language-Image Pre-training (CLIP) model learnt to pair an image with its caption and to retrieve one from the other.

Every result stays inside its task: a machine maps inputs to outputs along the instructions it was given, so a task it was not designed for is out of reach.

Those results opened a comparison not available before: whether a network that matches human performance is a true [computational model](computational%20model.md) of human behaviour. The answer stays open. George Box's line frames it: all models are wrong but some are useful (Box, 1979), and the wrongness is worth studying.

Psychologists' chance to shape how artificial intelligence is understood and built keeps growing, because good human oversight of its decisions depends on that work. Progress will likely slow again, as after earlier booms, and the two fields will settle into cooperative research when it does.

---

Flashcards for this section are as follows:

- what drove the recent advances in artificial intelligence ::@:: Hardware and data, not new theory.
- how the computational power of machines has grown ::@:: Exponentially.
- what the graphics processing unit (GPU) was built for ::@:: Video gaming; its arithmetic serves training a network with millions of parameters.
- what the internet supplied for training large networks ::@:: Images, text and speech.
- what the deep-learning era put in place of hand-crafted features ::@:: Features the network learns from the data itself.
- the four human-level or human-like results in perception, play and language ::@:: Object recognition, face recognition, the game of Go and large language models.
- what the Contrastive Language-Image Pre-training (CLIP) model learns ::@:: To pair an image with its caption, and to retrieve one from the other.
- the comparison the human-level results opened ::@:: Whether a network that matches human performance on a task is a true computational model of human behaviour.
- whether the question of a network as a true computational model of human behaviour is settled ::@:: No, the answer stays open.
- why a machine's skill stays inside its own task ::@:: It maps inputs to outputs along the instructions it was given, so a task it was not designed for is out of reach.
- George Box's 1979 line on models ::@:: All models are wrong, but some are useful.
- what good human oversight of artificial intelligence decisions depends on ::@:: Psychologists' work on how an artificial intelligence system is understood and built.
- what the pace of artificial intelligence progress is expected to do ::@:: Slow again, as it did after earlier booms, letting the two fields settle into sustained cooperative research.

### use in psychology

Artificial intelligence enters psychological research in three roles: an object of study, a test of theory, and a research tool.

As an object of study it raises questions about a person, not the machine: how a model reaches a decision, how people interact with it, and how living alongside it changes human skill. An explanation of a model's output is studied because a person must act on it, and a person's mental model of a machine shapes the decisions they take on that output. That model is hard to study partly because a machine cannot always explain itself. Interaction with a machine also opens a window on the mental models people form of other intelligent systems.

As a test of theory, generated stimuli and simulated models stand in for participants, so a theory about one trait becomes an experiment. This role rests on control. A [generative adversarial network](generative%20adversarial%20network.md) varies one trait while holding identity fixed, which no photograph of a real person does, and a [computational model](computational%20model.md) lets a researcher change one parameter where a participant gives one indivisible performance.

As a research tool, natural language processing and [large language models](large%20language%20model.md) analyse text, write study material and approximate a participant distribution. This role rests on scale. A language model finds structure in text, speech and social media that a laboratory sample is too small to show. A network trained on human responses supplies a distribution to compare against people's.

A 1990 to 2021 review of language processing applications in counselling and psychotherapy sets out their trends, advances, challenges and limitations (Laricheva et al., 2024). Text-based automatic personality recognition infers a person's personality from a sample of their text, and five corpora test where it fails, from hand-crafted linguistic features to data-driven transformers (Bhandarkar et al., 2024). Generated content stands in for a stimulus too: Generative Pre-trained Transformer 4 (GPT-4) manipulations of face and text in donation-based crowdfunding show that emotional valence in either channel moves the decision whether to give, while only words move how much (Guo et al., 2025).

The strongest systems are commercial and change quickly, so an experiment built on one is hard to reproduce. A model that matches human performance still makes errors, and whether a person would make the same errors is open. New models arrive faster than researchers can settle which part of a model a conclusion about a human process depends on.

---

Flashcards for this section are as follows:

- the three roles artificial intelligence (AI) plays in psychological research ::@:: An object of study, a test of theory, and a research tool.
- what an artificial intelligence (AI) model raises as an object of study ::@:: Questions about a person rather than about the machine: how a model reaches a decision, how people interact with it, and how living alongside it changes human skill.
- what makes artificial intelligence (AI) a test of theory ::@:: Generated stimuli and simulated models stand in for participants, so a theory about one trait becomes an experiment.
- what makes artificial intelligence (AI) a research tool ::@:: Natural language processing and large language models analyse text, write study material and approximate a participant distribution.
- what the second role of artificial intelligence (AI) in research rests on ::@:: Control, since a generative model varies one trait while holding the rest fixed and a computational model changes a single parameter.
- what the third role of artificial intelligence (AI) in research rests on ::@:: Scale, since a language model finds structure a laboratory sample is too small to show and a trained network supplies a distribution to compare against people's.
- why an explanation of a machine's output matters ::@:: A person must decide what to do with the output, so the explanation serves the person, not the model.
- why a person's mental model of a machine is hard to study ::@:: It shapes the decisions they take on the machine's output, and a machine cannot always explain its own decisions.
- what interaction with a machine opens a window on ::@:: The mental models a person forms of other intelligent systems.
- why an experiment built on a strong commercial artificial intelligence system is hard to reproduce ::@:: The system changes quickly, and access to it is time-limited.
- what is open about the errors a model that matches human performance makes ::@:: Whether a person would make the same errors.
- what a fast succession of new models makes hard to settle ::@:: Which part of a model a conclusion about a human process depends on.
- what a review of natural language processing in counselling and psychotherapy, covering 1990 to 2021, sets out ::@:: The applications' trends, advances, challenges and limitations (Laricheva et al., 2024).
- what text-based automatic personality recognition infers, and from what ::@:: A person's personality, from a sample of their text (Bhandarkar et al., 2024).
- what five text corpora test about automatic personality recognition, and across what range of methods ::@:: Where it fails, across hand-crafted linguistic features to data-driven transformers (Bhandarkar et al., 2024).
- in donation-based crowdfunding, how face and text manipulations of Generative Pre-trained Transformer 4 (GPT-4) differ in their effect on giving ::@:: Emotional valence in either channel moves whether a person gives, but only words move how much they give (Guo et al., 2025).

## references

- O'Toole, A. J., & Ludvig, E. A. (2026). [The use of AI in psychology: A historical perspective](https://doi.org/10.1111/bjop.70061). _British Journal of Psychology_, _117_(2).
    - Source of the material on Turing's question, the rule-based approach, the network approach, the two winters and what each left behind, chess and the present data-driven advance, and the three roles of artificial intelligence in psychological research with their limits.
    - Open access under a Creative Commons license; the publisher footer does not name the variant.
- \[missing\].
    - Source of the 27 states of the three-disk Tower of Hanoi problem space, which the cited editorial does not describe.
