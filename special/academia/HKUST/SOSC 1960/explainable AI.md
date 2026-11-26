---
aliases:
  - XAI
  - explainable AI
tags:
  - flashcard/active/special/academia/HKUST/SOSC_1960/explainable_AI
  - language/in/English
---

# explainable AI

Explainable artificial intelligence (XAI) concerns what a model's answer means to the person who reads it. Its methods recover the reasons behind a prediction and present them to someone other than the model's author.

---

Flashcards for this section are as follows:

- what explainable artificial intelligence (XAI) concerns ::@:: What a machine-learning model's answer means to the person who reads it.
- what the field of explainable artificial intelligence (XAI) supplies ::@:: Methods for recovering the reasons behind a prediction and presenting them to someone who is not the model's author.
- who an explanation of a model is written for ::@:: A reader who is not the model's author.
- whose reading an explanation is measured against ::@:: The person who reads it.

## field and problem

### definition

XAI is [artificial intelligence](artificial%20intelligence.md) whose decisions or predictions a human can understand. In a second sense it names the processes and methods that let users understand and trust what a machine-learning algorithm produces. A deep model's answer arrives without the reasoning that produced it.

---

Flashcards for this section are as follows:

- the property that makes artificial intelligence explainable, in the first sense ::@:: Its decisions or predictions are ones a human can understand.
- what explainable artificial intelligence (XAI) is in the second sense ::@:: The set of processes and methods that allows users to comprehend and trust what a machine-learning algorithm produces.
- what separates the two senses of explainable artificial intelligence (XAI) ::@:: The first names a property of the system, the second a set of processes and methods.
- what a deep model's answer arrives without ::@:: The reasoning that produced it.

### generations

Work on XAI falls into three generations (Miller et al., 2019): expert systems, then knowledge-based tutors, then deep-learning systems. A deep-learning system's decision process stays obscure to its users and developers.

---

Flashcards for this section are as follows:

- the three generations of explainable artificial intelligence (XAI) research ::@:: Expert systems, knowledge-based tutors, and deep-learning systems (Miller et al., 2019).
- the first generation of explainable artificial intelligence (XAI) research ::@:: Expert systems.
- the second generation of explainable artificial intelligence (XAI) research ::@:: Knowledge-based tutors.
- what produced the third generation of explainable artificial intelligence (XAI) research ::@:: The advance of deep learning methods.
- what a deep-learning system obscures, and to whom ::@:: Its decision-making processes, to users and developers.

### opaque pipeline

Researchers design the high-level architecture: which blocks the pipeline holds, and how they connect. What goes into a learned block and what comes out are readable, but the workings inside are not, so following the blocks end to end does not say how the input became the answer. A developer cannot debug or improve the model, an end user cannot understand or trust it, and a regulator cannot judge its safety and failure modes.

---

Flashcards for this section are as follows:

- what researchers decide when they design a model's high-level architecture ::@:: Which blocks the pipeline holds and how they connect.
- what stays unreadable inside a learned block ::@:: Its internal workings.
- what a readable block boundary tells a reader ::@:: What goes in and what comes out, not how the block turns one into the other.
- what an unreadable learned block stops a developer from doing ::@:: Debugging and improving the model.
- what an unreadable learned block stops an end user from doing ::@:: Understanding and trusting the model.
- what an unreadable learned block stops a regulator from judging ::@:: The model's safety issues and failure modes.

<!-- check: ignore-next-line[header_deep_nesting]: the questions ask what the unreadable pipeline demands of an explanation -->
#### four questions

How can the internal workings of the model be explained? How should an explanation address a developer rather than an end user? How can it stay maximally informative at a low cognitive load? How does an explanation induce understanding and trust?

---

Flashcards for this section are as follows:

- the four questions of explainable artificial intelligence (XAI) research ::@:: How to explain the internal workings, how to address a developer rather than an end user, how to stay maximally informative at a low cognitive load, and how to induce understanding and trust.
- the two audiences an explanation of a model must serve ::@:: The developer and the end user.
- how informative an explanation must be, and at what cognitive load ::@:: Maximally informative, at a low cognitive load.
- what an explanation aims to induce beyond comprehension ::@:: Understanding and trust.

## explanation and its reader

### saliency maps

A saliency map, also called a visual explanation or attribution map, is a heat map over the input that shows which regions mattered most to a prediction. Gradient-based methods highlight the regions that most affect the output.

The map is computed on a grid coarser than the image and scaled up, so its edges stay soft. Colour carries how much a region moved the score, warm at the most and cool at the least. A classifier answering "lion" with 94 percent confidence comes with a map that lights up the animal's face.

![A photograph of a man, then the convolutional layers that read it, the convolutional feature maps they produce, the fully connected layers, the class score they return, and the same face under two heat maps: one from a class activation map, one from gradient-weighted class activation mapping](attachments/CAM%20and%20Grad-CAM%20example.png)

Two branches leave the chain that runs the photograph to its class score, and each turns the feature maps into one heat map over the photograph. The upper branch pools each feature map to a single number, weights the maps by one weight each, and sums them, which gives the class activation map. The lower branch backpropagates from the class score to the maps and averages the gradient of each map. It then weights the maps by those averages, sums them, and rectifies the sum, which gives gradient-weighted class activation mapping.

Both maps put their warm region in the same place, across the chest and below the face, with the rest of the frame cool. The class activation map needs a network that pools each map to one number before the score, while gradient-weighted class activation mapping needs only a score the maps can be differentiated from.

---

Flashcards for this section are as follows:

- what a saliency map is ::@:: A heat map over the input showing which regions matter most to a model's prediction.
- the other names for a saliency map ::@:: Visual explanation and attribution map.
- what a gradient-based method highlights ::@:: The input regions that most affect the output.
- what the saliency map shows for a classifier that answers "lion" with 94 percent confidence ::@:: The animal's face.
- what the colour of a heat map carries ::@:: How much a region moved the score, from warm at the most to cool at the least.
- the grid a saliency map is computed on ::@:: One coarser than the input image, then scaled up, so its edges stay soft.
- the two heat maps the saliency figure sets side by side ::@:: One from a class activation map, which weights and sums the maps, and one from gradient-weighted class activation mapping, which averages each map's gradients, weights the maps by them and rectifies the sum.
- where the two heat maps of the saliency figure put their warm region ::@:: Across the chest and below the face, with the rest of the frame cool.
- what each of the two methods in the saliency figure asks of the network ::@:: The class activation map needs a network that pools each feature map to one number before the score; gradient-weighted class activation mapping needs only a score that can be differentiated down to the maps.

### explaining a prediction

Machine-learning models predict a person's aesthetic preference for an image. XAI methods expose the factors that preference rests on. Aesthetic preference for images is complex (Soydaner & Wagemans, 2024).

---

Flashcards for this section are as follows:

- what a machine-learning model of aesthetic preference predicts ::@:: A person's aesthetic preference for an image.
- what explainable artificial intelligence (XAI) methods expose behind an aesthetic preference ::@:: The factors the preference rests on.
- what explainable artificial intelligence (XAI) methods showed about aesthetic preference for an image ::@:: That it is complex, since the factors behind it are many (Soydaner & Wagemans, 2024).

### cognitive metrics

XAI scores an explanation by its effect on a person, not by its fidelity to the model. User understanding and trust are then cognitive metrics (Hoffman et al., 2018; Hsiao et al., 2021), measured by testing the people who read the explanation. An explanation that reproduces the model's reasons exactly and still leaves its reader unclear scores well on fidelity and badly on understanding.

---

Flashcards for this section are as follows:

- what an explanation is evaluated by ::@:: Its effect on a person, not its fidelity to the model.
- the two cognitive metrics for an explanation ::@:: User understanding and trust (Hoffman et al., 2018; Hsiao et al., 2021).
- how a cognitive metric is measured ::@:: By testing the people who read the explanation.
- what an explanation can do while still failing on understanding ::@:: Reproduce the model's reasons exactly and leave its reader unclear.
- the two things an explanation is judged between ::@:: How faithfully it reproduces the model's reasons, and what effect it has on a person.

<!-- check: ignore-next-line[header_deep_nesting]: two fields that measure an explanation by its effect on people -->
#### machine behaviour and stakeholder needs

Artificial Cognition (Taylor & Taylor, 2021) studies machine behaviour with cognitive psychology's experimental methods, built to expose the mechanisms behind human behaviour. In human-computer interaction, human-centred explainable artificial intelligence (HC-XAI) studies the needs of the people affected. It evaluates an explanation through user studies and user experience (Ehsen et al., 2024).

---

Flashcards for this section are as follows:

- what Artificial Cognition studies, and by what method ::@:: Machine behaviour, by the experimental methods cognitive psychology uses to expose the mechanisms behind human behaviour (Taylor & Taylor, 2021).
- what those experimental methods were originally designed to expose ::@:: The mechanisms behind human behaviour.
- what human-centred explainable artificial intelligence (HC-XAI) studies ::@:: The needs of the people a model affects.
- how human-centred explainable artificial intelligence (HC-XAI) evaluates an explanation ::@:: Through user studies and user experience (Ehsen et al., 2024).
- the field of study that contains human-centred explainable artificial intelligence (HC-XAI) ::@:: Human-computer interaction.

### human strategies

People explaining an image classification use one of two strategies, distinguished by where their eye gaze travels (Qi et al., 2026). The explorative strategy sweeps the gaze widely across the image and goes with more visual explanations, which suit beginners. The focused strategy gathers the gaze on few regions and goes with more conceptual explanations, which are diagnostic.

---

Flashcards for this section are as follows:

- the two strategies people use to explain an image classification ::@:: The explorative strategy and the focused strategy (Qi et al., 2026).
- what distinguishes the two strategies people use to explain an image classification ::@:: Where their eye gaze travels.
- what the explorative strategy does with the gaze ::@:: Sweeps it widely across the image.
- what the explorative strategy goes with, and whom it suits ::@:: More visual explanations, which are effective for beginners.
- what the focused strategy does with the gaze ::@:: Gathers it on few regions of the image.
- what the focused strategy goes with, and what it does better ::@:: More conceptual explanations, which are diagnostic.

<!-- check: ignore-next-line[header_deep_nesting]: the comparison is measured against the strategies it follows -->
#### saliency maps and human explanation

Saliency maps imitate the explorative strategy: a marked region says where the evidence sits, not why it decides the class. Methods that highlight the features informing observable causality, those whose visible presence causes the class, match human explanations better, and are potentially more accessible to their users. Knowing how people explain shows how to make an explanation accessible to a reader.

---

Flashcards for this section are as follows:

- which human strategy current saliency maps match ::@:: The explorative strategy, because a marked region says where the evidence sits and not why it decides the class.
- what an explainable artificial intelligence (XAI) method must highlight to match human explanations better ::@:: The features informing observable causality, whose visible presence causes the class.
- what such a method is for the people who read it ::@:: Potentially more accessible.
- what knowing how people explain shows ::@:: How to make an explanation accessible to a reader.

### interaction and trust

Explanations of human-AI interaction cover what happens when a strong system errs. XAI can ease the negative user experience and keep user trust after a machine error, even in a system that outperforms most humans (Xu & Wang, 2024).

---

Flashcards for this section are as follows:

- what explanations of human-AI interaction cover ::@:: What happens when a strong system errs.
- what explainable artificial intelligence (XAI) can ease after a machine error ::@:: The negative user experience.
- what explainable artificial intelligence (XAI) can keep after a machine error ::@:: User trust.
- the kind of system in which explainable artificial intelligence (XAI) keeps trust after an error ::@:: One that outperforms most humans (Xu & Wang, 2024).

<!-- check: ignore-next-line[header_deep_nesting]: a machine verdict is the case where the system's output meets a human decision -->
#### machine verdict and human decision

Knowing a machine's face-identification verdict moves human decisions toward confirming a match when the verdict is binary, given as same person or different people. Human accuracy does not change. A verdict given as a similarity score biases the decision less (Mueller et al., 2024).

---

Flashcards for this section are as follows:

- what a machine's face-identification verdict does to a human decision ::@:: Moves it toward confirming a match (Mueller et al., 2024).
- the form of machine verdict that biases a human decision toward confirming a match ::@:: A binary verdict, given as same person or different people.
- the form of machine verdict that biases a human decision less ::@:: A similarity score.
- what a machine's face-identification verdict does to human accuracy ::@:: Nothing changes.

<!-- check: ignore-next-line[header_deep_nesting]: acceptability is what a user makes of the system's use, the other side of the trust described here -->
#### judgments of AI use

People judge their own use of artificial intelligence differently from other people's (Purcell et al., 2024), and open use differently from secret use. These judgments concern acceptability, and rest on normative psychology theories of what a person expects of themselves and of others.

---

Flashcards for this section are as follows:

- what people's beliefs about artificial intelligence use concern ::@:: Which uses of artificial intelligence are acceptable (Purcell et al., 2024).
- whether people judge open use of artificial intelligence as they judge secret use ::@:: No: they judge the two differently.
- whether people judge their own use of artificial intelligence as they judge other people's ::@:: No: they judge the two differently (Purcell et al., 2024).
- the kind of theory judgments of artificial intelligence use rest on ::@:: Normative psychology theories.

## references

- O'Toole, A. J., & Ludvig, E. A. (2026). [The use of AI in psychology: A historical perspective](https://doi.org/10.1111/bjop.70061). _British Journal of Psychology_, _117_(2).
    - Source of the material on interaction and trust, and of the observable-causality match in human strategies.
    - Open access under a Creative Commons license; the publisher footer does not name the variant.
- Qi, R., Zheng, Y., Yang, Y., Cao, C. C., & Hsiao, J. H. (2026). [Explanation strategies in humans vs. current explainable AI: Insights from image classification](https://doi.org/10.1111/bjop.12714). _British Journal of Psychology_, _177_(2), 479-502.
    - Source of the material on human explanation strategies and of their comparison with current saliency maps.
- Miller et al. (2019), the review of the explainable AI literature the material cites.
    - Source of the three generations of explainable artificial intelligence research.
- \[missing\].
    - Source of the two definitions, the three generations, the four questions, the lion example, and the cognitive metrics, Artificial Cognition and Ehsen et al. (2024) references.
