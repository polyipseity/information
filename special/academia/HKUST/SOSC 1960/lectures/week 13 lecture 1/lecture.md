---
aliases:
  - HKUST SOSC 1960 week 13 lecture 1 lecture
  - SOSC 1960 week 13 lecture 1 lecture
tags:
  - flashcard/active/special/academia/HKUST/SOSC_1960/lectures/week_13_lecture_1/lecture
  - language/in/English
---

# lecture

- HKUST SOSC 1960 week 13 lecture 1
- parent: [week 13 lecture 1](index.md)

Four question sets: the shared history of AI and psychology, rule-based models and their limits, explainable AI and the human explanation, and AI as a research tool.

---

Flashcards for this section are as follows:

- the four question sets on AI and psychology ::@:: The shared history of artificial intelligence (AI) and psychology, rule-based models and their limits, explainable AI (XAI) and the human explanation, and AI as a research tool.

## AI and psychology

> __Prompt.__ 1.1. Why is it important to learn about AI and psychology? Give one way psychology benefits from AI and one way AI benefits from psychology.

<!-- markdownlint MD028 -->

> __Prompt.__ 1.2. What is behaviorism, and how does it contrast with the Cognitive Revolution? (Slide 5)

<!-- markdownlint MD028 -->

> __Prompt.__ 1.3. What new approaches did the Cognitive Revolution introduce for studying the human mind? (Slide 6)

<!-- markdownlint MD028 -->

> __Prompt.__ 1.4. Why was 1956 an important year for both psychology and AI? (Slides 6-7)

<!-- markdownlint MD028 -->

> __Prompt.__ 1.5. Which disciplines make up cognitive science? Give examples to illustrate the interdisciplinary nature of cognitive science. (Slides 8-9)

Artificial intelligence (AI) now runs search, recommendations, chatbots, hiring and healthcare, so its effect on how people think and behave falls inside what psychology studies. Both fields ask one question about intelligence, psychology in people and AI in machines, and each can test the other's answer.

Psychology gains a computational model to test theories of perception, memory and language, and a tool for data volumes no researcher reads by hand. Language models find patterns in text, speech and social media that a person would miss, such as early signs of depression in how someone writes.

AI gains from psychology in return. [Reinforcement learning](reinforcement%20learning.md) came from conditioning, attention mechanisms from the study of attention, and curriculum learning from how a person masters material in stages.

[Behaviourism](../../psychology.md#behaviorism) measures observable behaviour and sets internal states aside, so the mind becomes a black box. Classical conditioning and instrumental conditioning explained learning as the effect of the environment on what a person or animal does.

The cognitive revolution of the 1950s returned internal representations and information processing to the centre. A behaviourist asks how a reward changed the behaviour. A cognitive psychologist asks how the mind represented the situation and produced the action. The computer supplied the model for the second.

Three approaches carried the shift. Internal representations explain how the mind stores and processes information. Computer models specify the mechanism that produces behaviour, which a description from outside cannot. Objective methods study the activity itself through reaction times, error patterns and imaging of the working brain.

Both fields took shape in 1956. The Dartmouth summer workshop made artificial intelligence a discipline, with John McCarthy coining the term for the proposal and Newell and Simon bringing a working theorem prover. In psychology, Miller's _The Magical Number Seven, Plus or Minus Two_ made the limits of memory measurable, and Noam Chomsky argued for a rule-governed mental grammar. A symposium that September joined the two fields, and George Miller dates cognitive science to it.

[Cognitive science](cognitive%20science.md) draws on six disciplines: psychology, neuroscience, linguistics, philosophy, anthropology and artificial intelligence. The Sloan Foundation set the name in 1976, its 1978 report defined the field, and the Cognitive Science Society formed in 1979.

One question pulls several disciplines at once. Language needs linguistics for the grammar a speaker masters, psychology for how an infant segments speech sounds, and neuroscience for the imaging that locates the process. Philosophy tests what the others assume.

---

Flashcards for this section are as follows:

- why artificial intelligence (AI) falls inside what psychology studies ::@:: It runs search, recommendations, chatbots, hiring and healthcare, so its effect on how people think and behave is part of psychology's subject matter.
- the one question both artificial intelligence (AI) and psychology ask ::@:: What intelligence is, asked of machines and of people.
- the two things psychology gains from artificial intelligence (AI) ::@:: A computational model to test theories of perception, memory and language, and a tool for data volumes no researcher reads by hand.
- the three artificial intelligence (AI) methods that came from psychology ::@:: Reinforcement learning from conditioning, attention mechanisms from the study of attention, and curriculum learning from staged learning.
- what behaviourism measures, and what it sets aside ::@:: Observable behaviour; internal states, which makes the mind a black box.
- how a behaviourist and a cognitive psychologist differ on the same reward ::@:: The behaviourist asks how the reward changed the behaviour. The cognitive psychologist asks how the mind represented the situation and produced the action.
- the three approaches the cognitive revolution introduced ::@:: Internal representations of information, computer models that specify the mechanism producing behaviour, and objective methods such as reaction times and brain imaging.
- the 1956 event that made artificial intelligence (AI) a discipline ::@:: The Dartmouth summer workshop, where John McCarthy coined the name.
- the 1956 psychology paper that made the limits of memory measurable ::@:: George Miller's _The Magical Number Seven, Plus or Minus Two_.
- the six disciplines of cognitive science ::@:: Psychology, neuroscience, linguistics, philosophy, anthropology and artificial intelligence.
- the year the Sloan Foundation set the name cognitive science, and the year the Cognitive Science Society formed ::@:: 1976 for the name, and 1979 for the Society.
- the three disciplines one question about language draws together ::@:: Linguistics for the grammar a speaker masters, psychology for how an infant segments speech sounds, and neuroscience for imaging the process.

## rule-based models and their limits

> __Prompt.__ 2.1. How did early rule-based AI model cognition as information processing, and what are some potential problems? (Slides 11-13)

<!-- markdownlint MD028 -->

> __Prompt.__ 2.2. What is the frame problem, and why does a greater range of relevant information make it harder to solve? (Slide 13)

<!-- markdownlint MD028 -->

> __Prompt.__ 2.3. How do neural network (connectionist) models differ from rule-based approaches in modelling human learning? (Slide 14)

<!-- markdownlint MD028 -->

> __Prompt.__ 2.4. What factors drove recent advances in AI and psychology? (Slide 15)

<!-- markdownlint MD028 -->

> __Prompt.__ 2.5. In what ways is AI being incorporated into psychological research in recent years? (Slide 16)

The [rule-based approach](../../artificial%20intelligence.md#rule-based%20approach) treated thinking as symbol manipulation: an algorithm applied explicit if-then rules to symbols until a goal state appeared. A puzzle then became a search over states, and the three-disk Tower of Hanoi has 27 of them.

Four problems stopped it. The [frame problem](frame%20problem.md) asks what an action leaves unchanged, and nothing in the description says. Real cognition is messier than a puzzle and needs a flexibility that fixed rules do not give, so the skills of a one-year-old proved the hard ones. A rule-based system also needs its inputs and its task boundaries fixed in advance, and it fails outside that envelope.

An action changes a few facts and leaves the rest alone, so the program must list every unchanged fact for every action. Each fact that could bear on the step adds an axiom, and the axioms grow faster than the reasoning they support. More relevant information makes the problem harder, because more of it must be checked for what it does not change, and the count turns intractable before the task does.

A rule-based model explains learning as acquiring explicit rules and applying them. A [neural network](artificial%20neural%20network.md) model distributes knowledge across weighted connections and learns by adjusting the weights from examples. A child who has seen many dogs strengthens the pattern that recognises the next one, and no stated rule for the concept exists.

Two factors drove the recent advance. Computing power rose exponentially, with graphics processing units supplying the parallel arithmetic that training a network of millions of parameters needs. The internet supplied the data those networks learn from. Both fed generative AI and natural language processing, which reached research practice as speech transcription, thematic analysis of text, and models of visual and linguistic processing.

AI enters [psychological research](artificial%20intelligence.md) three ways. It is an object of study, where research asks how a model reaches a decision, how people interact with it, and how living with it changes human skill. It is a way to test theory, where generated stimuli and simulated models stand in for participants. It is a research tool, where natural language processing and [large language models](large%20language%20model.md) analyse text, write study material and approximate a participant distribution.

---

Flashcards for this section are as follows:

- how the rule-based approach treated thinking, and what it applied ::@:: As symbol manipulation; an algorithm applied explicit if-then rules to symbols until a goal state appeared.
- the number of states in the three-disk Tower of Hanoi, and what one state stands for ::@:: 27, one for each arrangement of the three disks.
- the four problems that stopped the rule-based approach ::@:: The frame problem, the messiness of real cognition, inputs and task boundaries fixed in advance, and failure outside that envelope.
- why a wider range of relevant information makes the frame problem harder ::@:: Every fact that could bear on a step adds an axiom stating what the action leaves unchanged, and the axioms grow faster than the reasoning they support.
- how a rule-based model and a neural network model explain learning differently ::@:: A rule-based model explains it as acquiring explicit rules and applying them, a neural network model as adjusting the weights on connections.
- the two factors that drove the recent advance in artificial intelligence (AI) ::@:: An exponential rise in computing power, chiefly graphics processing units, and the data the internet supplied.
- what the graphics processing unit (GPU) supplies for training a large network ::@:: The parallel arithmetic that a network of millions of parameters demands.
- the three ways artificial intelligence (AI) enters psychological research ::@:: As an object of study, as a way to test theory, and as a research tool.
- what artificial intelligence (AI) studies as an object of study ::@:: How a model reaches a decision, how people interact with it, and how living with it changes human skill.
- what natural language processing and large language models do as a research tool ::@:: Analyse text, write study material, and approximate a participant distribution.

## explainable AI and the human explanation

> __Prompt.__ 3.1. What is Explainable AI (XAI), and how have XAI systems changed across three generations according to Miller et al. (2019)? (Slide 17)

<!-- markdownlint MD028 -->

> __Prompt.__ 3.2. Why are the internal workings of learned AI models hard to interpret, and why does this matter? (Slide 18)

<!-- markdownlint MD028 -->

> __Prompt.__ 3.3. How can human cognition be integrated into XAI research? (Slide 19)

<!-- markdownlint MD028 -->

> __Prompt.__ 3.4. What are the major findings of Qi et al. (2026) on how humans explain image classification decisions? (Slide 21)

<!-- markdownlint MD028 -->

> __Prompt.__ 3.5. Do current XAI methods use explanation strategies similar to humans', based on Qi et al. (2026)? (Slides 21-22)

[Explainable artificial intelligence](explainable%20AI.md) (XAI) is any method that gives a person an understandable reason for a model's decision, prediction or behaviour: which information it used, or which assumption it made.

Miller et al. (2019) divide its history into three generations. The first used expert systems whose if-then rules a person could read directly. The second moved from exposing code to supporting the user's reasoning and diagnosing gaps in their understanding. The third explains deep models that learn complex patterns without explicit rules, so the mechanism stays opaque to user and developer.

A deep model's high-level architecture, its encoders, decoders and prediction heads, can be designed. Its internal representation is learned from data across billions of parameters, and those computations need not resemble human cognition at all.

Opacity limits four things. Debugging suffers because a failure cannot be traced. Trust suffers because a user cannot judge when to rely on the output. Fairness suffers because a model can learn to underrepresent a group. Theory testing suffers because a model that matches behaviour for the wrong reason still fails as a model of mind.

Human cognition enters XAI research by three routes. Cognitive metrics measure how real users respond: whether they understand an explanation and whether they trust the decision. That puts human understanding inside the evaluation, beside technical correctness. Artificial cognition applies the experimental methods of cognitive psychology to the model itself. Human-centred XAI studies the needs of the different people affected, since a developer wants technical detail where an ordinary user wants a clear reason. It tests an explanation through user studies.

Qi et al. (2026) tracked eye movements while people decided what an image showed and then explained the decision. Two attention strategies appeared. Explorative attention spreads across several regions of the image and goes with visual explanations, which a beginner finds easier. Focused attention settles on the features that decide the class and goes with conceptual explanations, which are more diagnostic. Both relationships were significant.

Current methods match one of the two strategies. Saliency maps follow the explorative strategy. Among them, a method highlighting observable causality comes nearer to how a person explains than one reading internal features, and a method such as Grad-CAM reads internal features.

---

Flashcards for this section are as follows:

- what explainable artificial intelligence (XAI) gives a person ::@:: An understandable reason for a model's decision, prediction or behaviour: which information it used, or which assumption it made.
- the three generations of explainable artificial intelligence (XAI) according to Miller et al. (2019) ::@:: Expert systems with readable if-then rules, systems that support the user's reasoning and diagnose gaps in their understanding, then deep models that learn complex patterns without explicit rules.
- what makes a deep model's internal workings ambiguous to read ::@:: Its internal representation is learned from data, the model carries billions of parameters, and its computations need not resemble human cognition.
- the four things the opacity of a deep model limits ::@:: Debugging, because a failure cannot be traced; trust, because a user cannot judge when to rely on the output; fairness, because a model can learn to underrepresent a group; and theory testing, because matching behaviour for the wrong reason still fails as a model of mind.
- the three routes by which human cognition enters explainable artificial intelligence (XAI) research ::@:: Cognitive metrics, artificial cognition, and human-centred XAI.
- what cognitive metrics measure, and where they put human understanding ::@:: How real users respond, whether they understand an explanation and whether they trust the decision; inside the evaluation, beside technical correctness.
- how human-centred explainable artificial intelligence (XAI) differs from the other two routes ::@:: It studies the needs of the different people affected and tests an explanation through user studies.
- what Qi et al. (2026) tracked, and what it revealed ::@:: Eye movements while people decided what an image showed and then explained the decision; two attention strategies appeared.
- the two attention strategies Qi et al. (2026) found, and the explanation each goes with ::@:: Explorative attention, spread across several regions of the image, goes with visual explanations that a beginner finds easier; focused attention, on the features that decide the class, goes with conceptual explanations that are more diagnostic.
- which human attention strategy saliency maps match, and which they miss ::@:: They follow explorative attention more closely, and miss focused attention.
- why a method reading internal features explains less like a person ::@:: A person explaining a decision follows observable causality, not a model's internal features.

## AI as a research tool

> __Prompt.__ 4.1. Why are explanations about AI's operations important during human-AI interaction? (Slide 23)

<!-- markdownlint MD028 -->

> __Prompt.__ 4.2. How has AI affected human chess-playing skills? (Slide 23)

<!-- markdownlint MD028 -->

> __Prompt.__ 4.3. How did Sobieszek et al. (2024) test whether "dominance" and "trustworthiness" are independent dimensions for first impressions in humans, and what did they find? (Slide 24)

<!-- markdownlint MD028 -->

> __Prompt.__ 4.4. How can AI help test psychological theories? (Slides 24-25)

<!-- markdownlint MD028 -->

> __Prompt.__ 4.5. What did Jones et al. (2024) find on first-impression descriptions, and how can NLP refine models of social cognition? (Slide 26)

An explanation gives a user something to check after a mistake: what led to the output, and so what to do next. It also eases the frustration of an error nobody can account for, since the user can see why it happened and how to recover. Trust survives an explained failure better than an unexplained one. That matters where a model decides about a person, as with a rejected application or a missed diagnosis. An explanation also supports accountability, because misuse and bias are hard to contest without a stated reason.

[Chess](../../artificial%20intelligence.md#chess) shows what an engine does to the people who use it. Once a computer and an internet connection were common, a player could study recorded games and practise against an engine at home, and a club and a coach no longer set the limit.

A neural engine such as AlphaZero gives up material to build an attack, so its games show a player how to weigh a sacrificed pawn against the chances it buys. Practising against an engine trains a player to anticipate the reply, the skill the engine's own strength rests on.

Oosterhof and Todorov (2008) proposed that a first impression of a face runs on two independent dimensions, trustworthiness and dominance. A face can gain dominance while its trustworthiness rating holds.

Sobieszek, Siemiątkowski and Imbir (2024) tested that. A [generative adversarial network](generative%20adversarial%20network.md) produced faces varying along one dimension while holding identity and other features fixed, and participants rated every face on both. Changing one dimension changed the rating of the other, so the two are not independent and the brain links them when it forms an impression.

A generated face isolates a single trait, because a photograph of a real face varies in many ways at once. That turns a theory about the trait into an experiment. A model can also stand in for participants: a network trained on human responses gives a response distribution to compare with people's, and a language model can supply a preliminary sample. Analysis at that scale finds structure a laboratory sample is too small to show.

Jones, Shiramizu and Jones (2024) applied topic modelling, a natural language processing technique, to free-text descriptions of [first impressions](first%20impression.md) rather than to ratings on traits the researcher chose. The descriptions fell into two topics, one of positive emotional valence and warmth, one of negative emotional valence and potential threat. Valence and dominance explained about 44 percent of the variance in those topics. A rating design misses most of what a person spontaneously writes, so free text corrects a model that ratings alone would have fixed too early.

---

Flashcards for this section are as follows:

- what an explanation gives a user after a mistake ::@:: Something to check: what led to the output, so the user can decide what to do next.
- why an explained failure keeps more trust than an unexplained one ::@:: The user can account for the error and judge what to do next, which matters where a model decides about a person.
- how wider access to a computer changed chess practice ::@:: A player could study recorded games and practise against an engine at home, which a club and a coach had once limited.
- what an AlphaZero game shows a chess player ::@:: How to weigh a sacrificed pawn against the attacking chances it buys.
- what practising against a chess engine trains ::@:: Anticipating the opponent's reply, the skill the engine's own strength rests on.
- the two dimensions Oosterhof and Todorov (2008) said a first impression of a face runs on, and how they relate ::@:: Trustworthiness and dominance, which they held to be independent.
- how Sobieszek, Siemiątkowski and Imbir (2024) built face stimuli varying one trait ::@:: A generative adversarial network (GAN) produced faces that varied along one dimension while holding identity and other features fixed.
- what Sobieszek, Siemiątkowski and Imbir (2024) found about the two face dimensions ::@:: Changing one dimension changed the rating of the other, so the two are not independent.
- what a generative model supplies that a photograph cannot ::@:: A controlled stimulus that isolates a single trait, which turns a theory about that trait into an experiment.
- how a model can stand in for participants ::@:: A network trained on human responses gives a response distribution to compare with people's, and a language model can supply a preliminary sample.
- what topic modelling of free-text first impressions found ::@:: Two topics, one of positive emotional valence and warmth, one of negative emotional valence and potential threat.
- how much of the variance in those topics valence and dominance explained ::@:: About 44 percent, so a trait-rating design misses most of what a person spontaneously writes.
