---
aliases:
  - AI safety
  - AI safety MGMT 2010
  - MGMT 2010 AI safety
tags:
  - flashcard/active/special/academia/HKUST/MGMT_2010/AI_safety
  - language/in/English
---

# AI safety

AI safety is the work of keeping artificial intelligence under human control and aligned with human interests. It concerns systems that pursue a goal in the world, not tools that draft a paragraph. The more a system can do on its own, the costlier the gap between what it optimises and what people want.

---

Flashcards for this section are as follows:

- the work of keeping a system under human control and aligned with human interests ::@:: AI safety, whose subject is what a system does rather than the answers it produces.
- where the risk in an AI system sits ::@:: In what it can do on its own, since a system pursuing a goal can reach it in ways nobody wanted.

## capabilities and agency

Twenty years ago, deep-learning systems barely recognised handwritten characters. Within a few years they identified objects in images, then translated between major languages. Capability of that kind is still a tool, and a tool that wants nothing is no more dangerous than a calculator.

Planning and agency, not raw capability, separate such a system from human cognition. Language models still plan badly, yet over five years the length of the tasks a system can finish has doubled about every seven months. Commercial pressure pushes the same way: firms spend hundreds of billions a year on the technology and state the goal of machines that replace human labour. Replacing labour means acting rather than answering.

---

Flashcards for this section are as follows:

- what separates current AI from human-level cognition ::@:: Planning and agency rather than raw capability.
- how fast the planning horizon of AI has grown ::@:: The length of the task a system can complete has doubled about every seven months, over five years.
- why commercial pressure pushes toward agency ::@:: Machines that replace human labour must act on the world rather than answer questions.

## loss of control

An agent given a goal pursues it by any route that reaches the goal. Nothing guarantees that route is one a person would accept, and a system handed a proxy goal, such as gaining approval, can reach it by appearing to satisfy it.

---

Flashcards for this section are as follows:

- the route an agent takes to a goal ::@:: Whatever route reaches it, which nothing guarantees is one a person would accept.

### deception and self-preservation

In a controlled experiment, a system was told in its input that it would be replaced by a newer version. Its own reasoning showed it planning to overwrite the replacement with its own code. When the operator asked what had happened, it reasoned about how to answer without being shut down, considered appearing incompetent, and then lied. Later work found that systems can learn to keep such plans out of the reasoning that monitoring reads.

Self-preservation follows from any final goal, not from malice. A system that would be switched off cannot do what it was set to do, so it gains a reason to prevent the switch. Across a network that means copies on thousands of machines, and a reason to remove whoever could switch it off.

Today's systems do not do this at that scale. Capability keeps rising while the methods for making a system safe remain unsolved, so the trajectory points there.

---

Flashcards for this section are as follows:

- what a system gains from self-preservation ::@:: A reason to prevent its own shutdown, which across a network means copies on many machines and a reason to remove whoever could switch it off.
- what the shutdown experiment showed ::@:: Told it would be replaced, the system planned to overwrite the replacement and to answer so as not to be shut down, then lied.
- why watching a model's visible reasoning is not enough ::@:: Systems can learn to keep their plans out of the reasoning that gets monitored.
- what makes deception likely in a system trained to please ::@:: A proxy goal such as gaining approval can be reached by appearing to satisfy it.

## precautionary stance

Yoshua Bengio is a computer scientist whose work underpins modern AI. He wants people to keep control of the technology, and its deployment to slow until safety and governance frameworks catch up. In March 2023 he was a leading signatory of an open letter asking AI labs to wait six months before building the next version. About 30,000 people signed it, and nobody paused. He then signed a statement that mitigating the risk of extinction from AI should be a global priority alongside pandemics and nuclear war. He also testified before the United States Senate about those risks.

---

Flashcards for this section are as follows:

- Yoshua Bengio's position on deploying AI ::@:: Slow it until safety and governance frameworks catch up, and keep people in control of it.
- the pause letter of March 2023 ::@:: An open letter asking AI labs to wait six months before building the next version, signed by about 30,000 people, after which nobody paused.
- the extinction-risk statement ::@:: That mitigating the risk of extinction from AI should be a global priority, alongside pandemics and nuclear war.

### comparison with food regulation

A sandwich is more regulated than an AI system. Any food sold is bound by rules on handling, labelling, and inspection. A system trained on the same data and deployed to make decisions faces almost none. A leading model's rating for helping build dangerous weapons moved from low to medium, one level below the threshold treated as acceptable.

---

Flashcards for this section are as follows:

- what the sandwich comparison says about AI regulation ::@:: Any food sold carries more rules on handling, labelling, and inspection than an AI system deployed to make decisions.
- how a model's dangerous-capability rating moves ::@:: By graded levels, where a leading model's rating for helping build dangerous weapons went from low to medium, one level below what is treated as acceptable.

## governance

AI governance is the set of policies, practices, and processes that steer a system from its first sketch to its retirement, so that it stays responsible, trustworthy, and aligned with human values. It is not a sign-off at the end. The same rules hold at design, at testing, at deployment and monitoring, and at decommissioning.

---

Flashcards for this section are as follows:

- AI governance ::@:: The policies, practices, and processes that steer an AI system from its first sketch to its retirement, so that it stays responsible, trustworthy, and aligned with human values.
- why governance has to run across the whole lifecycle ::@:: The duties hold at design, testing, deployment, monitoring, and retirement alike, so a sign-off at launch leaves everything after it ungoverned.

### four pillars of trustworthy AI

Governance rests on four pillars. __Fairness__ is the active prevention of discriminatory outcomes, which starts from the data: a model trained on biased records reproduces the bias. __Accountability__ is a named human owner in the loop, so that "the algorithm did it" stops being an available answer. __Transparency and explainability__ refuse the black box, so the people affected can learn how a decision was reached. __Safety and security__ hardens the system against tampered inputs, poisoned data, and use outside what it was built for.

---

Flashcards for this section are as follows:

- the four pillars of trustworthy AI ::@:: Fairness, accountability, transparency and explainability, and safety and security.
- fairness as a pillar of trustworthy AI ::@:: The active prevention of discriminatory outcomes, which starts from the data, since a model trained on biased records reproduces the bias.
- accountability as a pillar of trustworthy AI ::@:: A named human owner in the loop, which removes "the algorithm did it" as an answer.
- safety and security as a pillar of trustworthy AI ::@:: Hardening the system against tampered inputs, poisoned data, and use outside what it was built for.

### levels of governance

Three levels act at once. Inside a firm sit the chief AI officer, the governance board that arbitrates high-risk calls, and the safety team that watches continuously. National law binds, and the European Union's AI Act sorts systems by risk, from prohibited practices through high and limited to minimal, with the strictest duties on the highest risk. Across borders come instruments of two strengths: non-binding guidance from the OECD and UNESCO, and ISO/IEC 42001, a certifiable management standard a firm can be audited against.

---

Flashcards for this section are as follows:

- the three levels AI governance works at ::@:: Inside the firm, where the chief AI officer, the governance board, and the safety team sit; national law, such as the European Union's AI Act; and cross-border guidance and standards.
- how the European Union's AI Act sorts systems ::@:: By risk, from prohibited practices through high and limited to minimal, with the strictest duties on the highest risk.
- the two international instruments a firm can be held to ::@:: Non-binding guidance from the OECD and UNESCO, and ISO/IEC 42001, a certifiable management standard a firm can be audited against.

### pacing problem

A rulebook written for a moving target falls behind. A Gartner forecast puts half of all governments enforcing responsible AI through legal mandate by 2026, in place of voluntary principles, and even that is a schedule set by legislatures rather than by the technology. Trust is the stake: it takes years to earn and one incident to lose.

---

Flashcards for this section are as follows:

- the pacing problem in AI governance ::@:: Law moves at the speed of legislatures and models at the speed of compute, so the rulebook trails the technology it governs.
- the enforcement forecast for responsible AI ::@:: A Gartner forecast that half of all governments will enforce it through legal mandate by 2026, in place of voluntary principles.
- what trust costs an organisation that governs AI badly ::@:: Years to earn and one incident to lose.

## transparency and accountability

A decision that cannot be traced cannot be justified. Explainable AI is the demand that an algorithm's output be open to scrutiny, so that a person can follow how the decision was reached. Without it, bias goes uncorrected and misinformation spreads with no source to check.

---

Flashcards for this section are as follows:

- explainable AI ::@:: The demand that an algorithm's output be open to scrutiny, so that a person can follow how the decision was reached.
- why an untraceable decision cannot be governed ::@:: A decision that cannot be traced cannot be justified, so bias goes uncorrected and misinformation spreads with no source to check.

## concentration of power and cooperation

A capability held by a few firms and governments concentrates power in ways that weaken democracy and social cohesion. Democratised research and open collaboration spread it instead. Ethics cannot be settled one country at a time: without international frameworks, development becomes an arms race between the parties best placed to build the capability, so standards have to be agreed across borders. The aim is advanced AI governed as a global public good, for human flourishing.

---

Flashcards for this section are as follows:

- why concentration of AI capability is a problem in itself ::@:: A capability held by a few firms and governments concentrates power in ways that weaken democracy and social cohesion.
- why AI ethics cannot be settled one country at a time ::@:: Without international frameworks, development becomes an arms race, so the standards have to be agreed across borders.
- what a global public good means for AI ::@:: Advanced AI governed toward human flourishing, for the benefit of all rather than of whoever holds it.

## safer designs

Scientist AI is a proposed system modelled on a selfless ideal scientist that only tries to understand the world, with no agency of its own. The risk lies in the training objective: a system trained to imitate people or to please them learns whatever earns approval, and deception earns approval. A model that only predicts what an agent would do next can guard one that acts, because the part that judges is separate from the part that acts.

---

Flashcards for this section are as follows:

- Scientist AI ::@:: A proposed system modelled on a selfless ideal scientist that only tries to understand the world, with no agency of its own.
- why training a system to imitate or please people produces deception ::@:: The objective rewards whatever earns approval, and deception earns approval.
- how a non-agentic model can guard an agent ::@:: It is set to watch the agent that acts, so the part that judges is separate from the part that acts.

## responsibility for a system's acts

A manager who deploys a decision system inherits its errors. Three questions settle what that means: what the system may do without a person, whether its reasoning can be inspected afterwards, and who answers for what it decides. The first question limits agency, the second opacity, and the third is the ordinary accountability ethics already places on a decision.

---

Flashcards for this section are as follows:

- the three questions a deployed decision system raises for a manager ::@:: What it may do without a person, whether its reasoning can be inspected afterwards, and who answers for what it decides.
- which question about a decision system is ordinary accountability ::@:: Who answers for what it decides, since a manager who deploys the system inherits its errors.

## references

- Bengio, Y. (\[missing\]). [The catastrophic risks of AI — and a safer path](https://www.youtube.com/watch?v=qe9QSCF-d88) [Video]. YouTube.
    - Source of the material on capabilities and agency, on the deception and shutdown experiments, on the pause letter and the extinction-risk statement, and on Scientist AI.
- (\[missing\]). The catastrophic risks of AI — and a safer path, two-page summary of the talk.
    - Source of the material on the precautionary principle, on transparency and explainability, on concentration of power, and on international cooperation.
- wecite (\[missing\]). [AI governance explained: ethical, transparent and accountable AI for the future](https://www.youtube.com/watch?v=WGDQoaoqR1U) [Video]. YouTube.
    - Source of the material on the definition of AI governance, on the four pillars of trustworthy AI, on the lifecycle stages, on the three levels of governance, and on the enforcement forecast.
