---
aliases:
  - COMP 3211
  - COMP 3211 index
  - COMP3211
  - COMP3211 index
  - Fundamentals of Artificial Intelligence
  - Fundamentals of Artificial Intelligence index
  - HKUST COMP 3211
  - HKUST COMP 3211 index
  - HKUST COMP3211
  - HKUST COMP3211 index
tags:
  - flashcard/active/special/academia/HKUST/COMP_3211/index
  - function/index
  - language/in/English
---

# index

- HKUST COMP 3211
- name: Fundamentals of Artificial Intelligence

The content is in teaching order.

- grading
  - scheme
    - assignment ×3: 15%
    - midterm exam: 35%
      - datetime: 2025-03-26T19:30:00+08:00/2025-03-26T21:30:00+08:00, PT2H
    - final exam: 50%
- logistics
  - objectives ::@:: appreciate AI problem solving; learn fundamental AI algorithm; understand AI challenges and goals <!--SR:!2025-04-20,46,290!2025-04-28,58,310-->
  - course intended learning outcomes (CILOs) ::@:: appreciate cutting edge AI research; identify AI fundamental concepts and techniques; understand and apply state space search techniques <!--SR:!2025-05-07,63,310!2025-03-24,27,270-->
  - syllabus
    - simple intelligent agents: machine evolution, machine learning, rule-based systems
    - search: adversarial, heuristic, uniformed
    - learning
    - knowledge planning, knowledge reasoning, knowledge representation
    - auction, game theory, multi-agent systems
    - uncertainty

## children

- [assignments](assignments/)
<!-- - [questions](questions.md) -->

## week 1 tutorial

- datetime: 2025-02-04T12:30:00+08:00/2025-02-04T13:20:00+08:00
- status: unscheduled, no tutorial

## week 1 lecture

- datetime: 2025-02-05T13:30:00+08:00/2025-02-04T14:50:00+08:00
- topic: introduction, reactive agents
- [artificial intelligence](../../../../general/artificial%20intelligence.md) (AI) ::@:: John McCarthy, one of the founders of AI — "It is the science and engineering of making intelligent machines, especially intelligent computer programs. It is related to the similar task of using computers to understand human intelligence, but AI does not have to confine itself to methods that are biologically observable." <!--SR:!2025-03-27,30,270!2025-03-23,26,270-->
  - artificial intelligence (AI) / intuition ::@:: What is it? A calculator? An operating system? A text editor? ChatGPT or DeepSeek? <!--SR:!2025-04-26,56,310!2025-04-26,56,310-->
  - artificial intelligence (AI) / motivations ::@:: forefront of computer applications; make machines do things so far that can be done by humans; in the long-term, make machines that can act, sense, and think intelligently <!--SR:!2025-04-26,56,310!2025-05-06,62,310-->
  - artificial intelligence (AI) / algorithms, techniques ::@:: heuristic search algorithms, knowledge representation languages, machine learning algorithms and reasoners, etc. <!--SR:!2025-04-05,39,290!2025-04-05,39,290-->
  - artificial intelligence (AI) / impacts ::@:: engineering, science; everyday life; humanity in general <!--SR:!2025-04-05,39,290!2025-05-09,65,310-->
  - artificial intelligence (AI) / in computer science (CS) ::@:: science and engineering of making intelligent computer programs, the frontier of computer applications; new ways to solve problems with a computer <!--SR:!2025-03-25,28,270!2025-03-25,28,270-->
  - artificial intelligence (AI) / origins ::@:: Ada Lovelace (1815–1852), Alan Turing (1912–1954) <!--SR:!2025-03-13,19,250!2025-03-25,28,270-->
    - artificial intelligence (AI) / origins / Ada Lovelace (1815–1852) ::@:: Considered as the first computer programmer. Her Note G describes an algorithm for Babbage's analytical engine to compute Bernoulli numbers. She described the analytical engine as able to do what we tell it to perform, but cannot anticipate things that we do not tell it to perform. <!--SR:!2025-03-26,29,270!2025-04-27,57,310-->
    - artificial intelligence (AI) / origins / Alan Turing (1912–1954) ::@:: Computing machinery and intelligence. _Mind_, 59:433-460, 1950. — "I propose to consider the question, 'Can machines think?' This should begin with definitions of the meaning of the terms 'machine' and 'think.'" <!--SR:!2025-03-19,24,250!2025-03-15,21,250-->
      - Turing test ::@:: A test to empirically determine whether a computer has achieved intelligence. A human questioner questions two respondents, one human, the other a computer function, whose identities are unknown to the human questioner. Using a specified format and context, the questioner interrogates the two respondents within a specific subject area. After a preset length of time or number of questions, the questioner is then asked to decide which respondent is human and which is a computer. <!--SR:!2025-04-12,42,290!2025-04-28,58,310-->
  - artificial intelligence (AI) / history
    - artificial intelligence (AI) / history / 1956 ::@:: John McCarthy coined the term "__artificial intelligence__" as the topic of the Dartmouth Conference, the first conference devoted to the subject. The conference was proposed by John McCarthy, Marvin Minsky, Nathaniel Rochester, and Claude Shannon: "2 month, 10 man study of artificial intelligence". <!--SR:!2025-03-18,23,250!2025-03-17,22,250-->
    - artificial intelligence (AI) / history / Marvel (1992) ::@:: a real-time expert system that monitors the massive stream of data from the Voyager spacecraft, handling routine tasks, and alerting the analysts to more serious problems at Jet Propulsion Laboratory (JPL) <!--SR:!2025-03-13,19,250!2025-03-24,27,270-->
    - artificial intelligence (AI) / history / Pegasus (1994) ::@:: a speech understanding program that handles airline ticket reservations <!--SR:!2025-03-23,26,270!2025-04-05,39,290-->
    - artificial intelligence (AI) / history / Gulf War ::@:: An AI planning and scheduling system employed by US military. A DARPA report said the saving from this AI system had paid back the US Government all its investment on AI during the past 20 years. <!--SR:!2025-04-11,41,290!2025-05-06,62,310-->
    - artificial intelligence (AI) / history / older AIs & misc ::@:: Deep Blue (1997), IBM Watson (2011), AlphaFold (2020) <!--SR:!2025-03-14,20,250!2025-03-23,26,270-->
    - artificial intelligence (AI) / history / playing Go ::@:: AlphaGo (2016), AlphaGo Zero (2017) <!--SR:!2025-03-26,29,270!2025-04-13,43,290-->
    - artificial intelligence (AI) / history / GPT ::@:: GPT-3 (2020), ChatGPT (2022), GPT4 (2023), GPT4o (2024) <!--SR:!2025-03-28,31,270!2025-03-19,14,250-->
    - artificial intelligence (AI) / history / chatbots ::@:: ELIZA (1963, Weizenbaum; a computer psychotherapist) <br/> BlenderBot 3 (2022, Meta; letdown) <br/> AI Test Kitchen (2022, Google; announced only) <br/> ChatGPT (2022, OpenAI; breakthrough) <!--SR:!2025-03-24,27,270!2025-04-05,39,290-->
  - artificial intelligence (AI) / brittleness ::@:: Current AI systems are still brittle. Examples include hallucinations, object recognition, sensitivity to disturbance, etc. <!--SR:!2025-03-25,28,270!2025-03-24,27,270-->
- [hallucination](../../../../general/hallucination%20(artificial%20intelligence).md) ::@:: A response generated by AI that contains false or misleading information presented as fact, e.g. false negatives, false positives, incorrect predictions. It is associated with unjustified responses or beliefs rather than perceptual experiences. <!--SR:!2025-03-25,28,270!2025-03-24,27,270-->
  - hallucination / causes ::@:: These errors can be caused by a variety of factors, including data biases, incorrect model assumptions, insufficient training data, etc. <!--SR:!2025-04-11,41,290!2025-04-28,58,310-->
  - hallucination / examples ::@:: DALL-E 2 or Midjourney unable to create the image you want because the AI does not understand your desired context. <!--SR:!2025-03-23,26,270!2025-04-05,39,290-->
- [model collapse](../../../../general/model%20collapse.md) ::@:: It is a phenomenon where machine learning models gradually degrade due to errors coming from uncurated training on the outputs of another model, including prior versions of itself. Such outputs are known as synthetic data. <p> A study in 2024 shows this. For example, after successive generations, nonsense text are generated. Biases in the dataset get amplified, e.g. forgetting obscure dog breeds exist due to under-representation in the initial dataset. <!--SR:!2025-03-23,26,270!2025-04-27,57,310-->
- [intelligent agent](../../../../general/intelligent%20agent.md) ::@:: It is an entity that perceives its environment, takes actions autonomously to achieve goals, and may improve its performance through machine learning or by acquiring knowledge. <!--SR:!2025-03-16,17,329!2025-03-16,17,329-->
  - intelligent agent / features ::@:: can perceive, can perform actions, has an objective/goal <!--SR:!2025-03-16,17,329!2025-03-16,17,329-->
  - intelligent agent / learning objectives (in this course) ::@:: stimulus-response agent (stateless), then add states <!--SR:!2025-03-17,18,329!2025-03-16,17,329-->
  - intelligent agent / control ::@:: e.g. designed vs. evolved/learned, genetic algorithms, neural networks, rules <!--SR:!2025-03-16,17,329!2025-03-15,16,329-->
  - intelligent agent / stimulus-response agent ::@:: Stateless machines that reacts to _immediate_ stimulus from the environment. <!--SR:!2025-03-17,18,329!2025-03-17,18,329-->
    - intelligent agent / stimulus-response agent / example ::@:: actions: up/down/left/right (cannot go into walls) <br/> environment: an enclosed 2D grid with walls <br/> objective: follow the boundary of the first obstacle met <br/> perceptions: 8 sensors for 8 adjacent cells, each testing if the corresponding cell is occupied <br/> policy: an algorithm to control the robot <!--SR:!2025-03-17,18,329!2025-03-16,17,329-->

## week 1 lecture 2

- datetime: 2025-02-07T13:30:00+08:00/2025-02-07T14:50:00+08:00
- status: canceled

> Dear All,
>
> The lectures tomorrow (both L1 and L2) will be canceled due to my sickness.
>
> Because of the canceled lectures tomorrow, the tutorial starting date changes accordingly: T2 will start on Feb 18. But T1 still starts on Feb 14 (next Friday). You may check the tutorial arrangements at the tutorial page.
>
> Sorry for any possible inconvenience that may cause. See you next week!
>
> Best regards,
> \[redacted\]

## week 2 tutorial

- datetime: 2025-02-11T12:30:00+08:00/2025-02-11T13:20:00+08:00
- status: canceled

## week 2 lecture

- datetime: 2025-02-12T13:30:00+08:00/2025-02-12T14:50:00+08:00
- topic: reactive agents
- [perceptron](../../../../general/perceptron.md)
  - perceptron / alias ::@:: threshold logical unit (TLU) <!--SR:!2025-03-13,17,323!2025-03-14,18,323-->
  - perceptron / supervised learning ::@:: It requires a training dataset. Each data in the dataset consists of _n_ _inputs_ as a _n_-dimensional vector and a _label_ (e.g. desired output). <p> Then, the task is computing a function that computes a "good" label from arbitrary _n_ inputs. This usually means agreeing with the training dataset's labels as much as possible (accuracy metric). <p> Here, we consider using a threshold linear unit (TLU; a.k.a perceptron) to learn the function. <!--SR:!2025-04-09,35,303!2025-03-12,15,313-->
  - perceptron / computation ::@:: Given a data vector $\mathbf x$; and weights $\mathbf w$, the bias $\theta$, and the activation function $f$ of a perceptron, the result is computed by: $$y = f(\mathbf x \cdot \mathbf w + \theta) \,.$$ <p> Given $n$ row data vectors vertically stacked as a matrix $\mathbf X$, the $n$ results as a column vector is computed by: $$\mathbf y = f\left(\mathbf X \mathbf w + \mathbf 1 \theta \right) \,.$$ <!--SR:!2025-03-13,17,323!2025-03-08,12,303-->
    - perceptron / computation / activation function ::@:: $$f(u) = \begin{cases} 1 & \text{if }u \ge \theta \\ 0 & \text{if }u < \theta \end{cases}$$ <p> Usually, the threshold _θ_ is chosen to be 0. This is because we can always add to a perceptron, an new input that is always 1, and its weight set to the negation of the original threshold. Such a weight is known as the _bias_. <!--SR:!2025-03-14,18,323!2025-03-13,17,323-->
  - perceptron / Boolean functions ::@:: A function whose inputs are Booleans (0: false, 1: true) and the output is also a Boolean (0: false, 1: true). <p> _Linearly separable_ functions can be _learnt_ by a perceptron. But not all such functions are linearly separable, e.g. $x_1 \overline {x_2} + \overline {x_1} x_2$ (($x_1$ AND NOT $x_2$) OR (NOT $x_1$ AND $x_2$)). <!--SR:!2025-03-12,15,313!2025-03-13,16,313-->
  - [perceptron § steps](../../../../general/perceptron.md#steps)
    - [perceptron § steps](../../../../general/perceptron.md#steps) / initialization ::@:: Initialize the weights arbitrarily. Weights may be initialized to 0 or small random values. <!--SR:!2025-03-13,16,313!2025-03-12,15,313-->
    - [perceptron § steps](../../../../general/perceptron.md#steps) / training ::@:: For each sample $j$ in the training dataset, perform the following steps over the input $\mathbf{x}_j$ and the desired output $d_j$: <!--SR:!2025-03-13,16,313!2025-03-13,17,323-->
      - [perceptron § steps](../../../../general/perceptron.md#steps) / training / forward ::@:: Calculate the actual output: $$y_j(t) = f(\mathbf{w}(t) \cdot \mathbf{x}_j) = f(w_0(t) x_{j, 0} + w_1(t) x_{j, 1} + \cdots + w_n(t) x_{j, n})$$. <p> The dot product can be interpreted as a weighted sum. Using linear algebra, this is: $$y_j(t) = f\left(\mathbf w(t)^\intercal \mathbf x_j \right)$$ <!--SR:!2025-03-08,11,293!2025-03-08,11,293-->
      - [perceptron § steps](../../../../general/perceptron.md#steps) / training / backward ::@:: Update the weights: $$w_i(t + 1) = w_i(t) + r (d_j - y_j(t)) x_{j, i}$$ for all features $0 \le i \le n$. $r$ is the [learning rate](learning%20rate.md). <p> Since $x_{j, 0} = 1$ always, $w_0$ is effectively the bias $b$. Thus the above algorithm already includes updating the bias: $$b(t + 1) = b(t) + r(d_j - y_j(t)) \,.$$ <p> Using linear algebra, this is: $$\mathbf w(t + 1) = \mathbf w(t) + r (d_j - y_j(t)) \mathbf x_j$$ <!--SR:!2025-03-08,11,293!2025-04-09,35,303-->
    - [perceptron § steps](../../../../general/perceptron.md#steps) / termination ::@:: For [offline training](offline%20training.md), the second step may be repeated until the batch or iteration error $\frac 1 s \sum_{j = 1}^s \lvert d_j - y_j(t) \rvert$ is less than a user-defined threshold $\gamma$, or a predetermined number of batches or iterations have been completed. $s$ is the batch or iteration (not to be confused with epoch) size. <p> If the training set is linearly separable, the above (i.e. termination) will eventually happen. The number of steps depends on the dataset ordering, initial weights, learning rate. <!--SR:!2025-03-08,11,293!2025-03-08,11,293-->
  - perceptron / biological neuron ::@:: inputs: dendrites; node/computation unit: cell nucleus; outputs: axons; weights: synapses <p> TLUs are is a very simple model of biological neuron. <!--SR:!2025-03-12,15,313!2025-03-12,16,323-->
  - perceptron / output ::@:: In this course, a perceptron can only output 0 or 1 (after activation function). <!--SR:!2025-03-22,17,343!2025-03-24,19,343-->
- [activation function](../../../../general/activation%20function.md) ::@:: In the context of an artificial neural network, it is a function that calculates the output of the node based on its individual inputs and their weights. Nontrivial problems can be solved using only a few nodes if the above is nonlinear. <!--SR:!2025-03-12,16,323!2025-03-12,16,323-->
  - activation function / examples ::@:: ReLU (rectified linear unit), logistic (sigmoid), hyperbolic tangent (tanh) <!--SR:!2025-03-13,16,313!2025-03-14,17,313-->
- [ReLU](../../../../general/rectifier%20(neural%20networks).md) ::@:: $$f(x) = \max(0, x)$$ <!--SR:!2025-03-13,17,323!2025-03-12,15,313-->
  - ReLU / properties ::@:: continuous, linear, piecewise, differentiable almost everywhere <!--SR:!2025-03-14,17,313!2025-03-13,17,323-->
- [sigmoid](../../../../general/logistic%20function.md) ::@:: $$f(x) = \frac 1 {1 + e^{-x} }$$ <!--SR:!2025-03-14,18,323!2025-03-14,18,323-->
- [hyperbolic tangent](../../../../general/hyperbolic%20functions.md) ::@:: $$f(x) = \frac {e^{x} - e^{-x} } {e^x + e^{-x} } = \frac {e^{2x} - 1} {e^{2x} + 1}$$ <!--SR:!2025-03-14,18,323!2025-03-07,11,303-->
- [identity (activation)](../../../../general/identity%20function.md) (linear) ::@:: $$f(x) = x$$ <!--SR:!2025-03-12,16,323!2025-03-13,16,313-->
  - identity (activation) / use ::@:: For output layers, target values used to train a model with such an activation function in the output layer are typically scaled before modeling using normalization or standardization transforms. Useful for _regression problems_. <!--SR:!2025-03-07,11,303!2025-03-07,11,303-->
- [neural network](../../../../general/neural%20network%20(machine%20learning).md) ::@:: __(Artificial) neural network__ (__(A)NN__) is one of the most powerful artificial intelligence and machine learning algorithms. It can approximate any [function](../../../../general/function%20(mathematics).md) from a certain [function space](../../../../general/function%20space.md), i.e. an _universal approximator_, by the [universal approximation theorem](../../../../general/universal%20approximation%20theorem.md). <p> As the name suggests, it draws inspiration from neurons in our brain and the way they are connected. <!--SR:!2025-03-12,15,313!2025-03-08,11,293-->
  - neural network / basic structure ::@:: A directed graph whose nodes are neurons. Those with no incoming edges are inputs/sources. Those wih no outgoing edges are output/targets. The remaining are internal nodes and represent _hidden_ features. <!--SR:!2025-03-12,16,323!2025-03-13,17,323-->
  - neural network / training overview ::@:: We initialize the weights of directed edges in the graph. Then while a condition to keep updating the weights is satisfied (e.g. accuracy target, number of updates), "improve" the weights. When the condition is no longer met, training has completed. <p> Two popular ways to "improve" the weights are gradient descent and _stochastic_ gradient descent (they are different things!). <!--SR:!2025-03-14,18,323!2025-03-14,18,323-->
- intelligent agent
  - intelligent agent / basic stateless architecture ::@:: sensory input → perceptual processing → feature vector → action function (specified by the designer) → action <!--SR:!2025-03-14,18,323!2025-03-08,11,293-->
  - intelligent agent / perception ::@:: Represented using a set of $x_i$. Note that there can be illegal combinations of values for the set $x_i$. <!--SR:!2025-03-14,18,323!2025-03-13,17,323-->
  - intelligent agent / action function ::@:: It consists of several statement in the form: If the set of $x_i$ has this combination of values, then perform a certain action. <!--SR:!2025-03-08,11,293!2025-03-12,15,313-->
- [Boolean algebra](../../../../general/Boolean%20algebra.md)
  - Boolean algebra / overview ::@:: $a$ AND $b$: $ab$ or $a \cdot b$; $a$ OR $b$: $a + b$; NOT $a$: $\overline a$ <p> AND and OR are associative and commutative. <!--SR:!2025-03-14,17,313!2025-03-08,11,293-->
- [production system](../../../../general/production%20system%20(computer%20science).md) ::@:: Essentially a giant if-else if-...-else program. <p> It is a _sequence_ (so it is ordered) in the form of: $c \to a$, where $c$ is a Boolean function and $a$ is an action. Find the first statement where $c$ evaluates to 1. Its action $a$ is the action the agent will take. <p> Commonly, we add a fallback case: $1 \to a$, where $1$ is the constant Boolean function always returning true. <!--SR:!2025-03-08,11,293!2025-03-14,17,313-->

## week 2 lecture 2

- datetime: 2025-02-14T13:30:00+08:00/2025-02-14T14:50:00+08:00
- topic: reactive agents
- [genetic programming](../../../../general/genetic%20programming.md) (GP) ::@:: An evolutionary algorithm, an artificial intelligence technique mimicking natural evolution, which operates on a population of programs. <!--SR:!2025-03-08,11,293!2025-03-14,18,323-->
  - genetic programming / motivation ::@:: Human evolves to become what we are now (unless you are not human). Maybe we can adapt evolution for machine learning? Evolution has two key components: reproduction and selection (survival of the fittest). <!--SR:!2025-03-08,11,293!2025-03-14,17,313-->
  - genetic programming / overview ::@:: Decide on how to represent _legal_ programs. Define a fitness function. Select some programs as generation 0. Produce the next generation until you have a "good enough" program. <p> 3 common methods to produce next generations: copy, crossover, and mutate. <!--SR:!2025-03-13,17,323!2025-03-12,16,323-->
  - genetic programming / program representation ::@:: Typically represented as tree structures. <p> We can consider statements in a program as functions. For example, AND(a, b) stands for a AND b and IF(a, b, c) stands for if a is true, then b, otherwise c. Then a program is a composition of many functions. <p> With this function composition in mind, we convert it into a tree recursively: A constant value or a input value is represented by a leaf. A function application/call is represented by having the function itself as a node and its arguments as its children nodes. <!--SR:!2025-03-08,11,293!2025-04-09,35,293-->
  - genetic programming / initialization ::@:: _full_, _grow_, _ramped half-and-half_, etc. <!--SR:!2025-03-12,16,323!2025-03-14,17,313-->
    - genetic programming / initialization / _grow_ ::@:: It creates the individuals sequentially. Every GP tree is created starting from the root, creating functional nodes with children as well as terminal nodes up to a certain depth. <!--SR:!2025-03-08,11,293!2025-03-08,11,293-->
    - genetic programming / initialization / _full_ ::@:: It is similar to _Grow_. The difference is that all branches in a tree are of same predetermined depth. <!--SR:!2025-03-13,16,313!2025-03-13,17,323-->
    - genetic programming / initialization / _ramped half-and-half_ ::@:: It creates a populations consisting of $md-1$ parts and a maximum depth of $md$ for its trees. The first part has a maximum depth of 2, second of 3 and so on up to the $md-1$-th part with maximum depth $md$. Half of every part is created by _Grow_, while the other part is created by _Full_. <!--SR:!2025-03-29,24,273!2025-03-08,11,293-->
  - genetic programming / selection ::@:: You need a fitness function to do so. <!--SR:!2025-03-12,16,323!2025-03-08,11,293-->
    - genetic programming / selection / example ::@:: We run the program for a certain number of steps and count the number of steps with an adjacent wall. We clamp its value between 0 and 32. We do 10 runs at random starting positions and sum the values (clamped between 0 and 320). <!--SR:!2025-03-14,17,313!2025-03-13,17,323-->
  - genetic programming / reproduction ::@:: Common methods for producing a new generation: copy, crossover, mutate. <!--SR:!2025-03-13,17,323!2025-03-07,11,303-->
    - genetic programming / reproduction / copy ::@:: Copy some programs from the previous generation. They are called the _parents_. A _tournament selection_ is used: randomly select some programs and choose the best one to copy. Other methods are possible. <p> A typical percentage of the new generation copied is 10%. <!--SR:!2025-03-08,11,293!2025-03-12,16,323-->
    - genetic programming / reproduction / crossover ::@:: From the copied _parents_, select 2 programs. A randomly chosen subtree of one parent is used to replace (including the subtree root node) a randomly selected subtree of another parent. <p> A typical percentage of the new generation crossover-ed is 90%. <!--SR:!2025-03-13,16,313!2025-03-13,16,313-->
    - genetic programming / reproduction / mutate ::@:: From the copied _parents_, select 1 program. Replace a randomly selected subtree by a new randomly generated subtree. <p> A typical percentage of the new generation mutated is 1% (rarely used). <!--SR:!2025-03-08,12,303!2025-03-14,17,313-->
  - genetic programming / performance ::@:: It depends on the initial generation size, copy/crossover/mutate rates, and tournament selection parameters. <p> The wall-following example in the slides generates a perfect tree after 10 generations. <!--SR:!2025-03-14,18,323!2025-03-14,18,323-->

## week 3 tutorial

- datetime: 2025-02-18T12:30:00+08:00/2025-02-18T13:20:00+08:00
- topic: TLU basics
- [object detection](../../../../general/object%20detection.md)
  - object detection / transplanted objects ::@:: elephant in the room: Transplanting such an object onto an image, it itself is often not detected or assumes wrong identities. It also has non-local effects, causing other previously correctly detected objects to go missing. <!--SR:!2025-03-16,17,329!2025-03-16,17,329-->
- [computer vision](../../../../general/computer%20vision.md)
  - computer vision / image recognition
    - computer vision / image recognition / fooling them ::@:: Current systems are easily fooled by: adding human-undetectable noise, adding small obstructions to an image, random patterns, geometric transformation of an object in the image, etc. <!--SR:!2025-03-17,18,329!2025-03-16,17,329-->
- [natural language processing](../../../../general/natural%20language%20processing.md) (NLP)
  - natural language processing / hallucinations ::@:: They are prone to creating content that do not match real-world facts (factuality hallucination) or user inputs (faithfulness hallucination, e.g. the year of an event being replaced by the year of another event). <p> Vision language models (VLMs) are also prone to this. <!--SR:!2025-03-16,17,329!2025-03-16,17,329-->
- [artificial intelligence](../../../../general/artificial%20intelligence.md) (AI)
  - artificial intelligence / recent trend ::@:: Its performance has been improving! For example, see the performance of works from different years on an object detection benchmark (COCO). <!--SR:!2025-03-16,17,329!2025-03-17,18,329-->
- [perceptron](../../../../general/perceptron.md)
  - perceptron / alias
  - perceptron / supervised learning
  - perceptron / computation
    - perceptron / computation / activation function
  - [perceptron § steps](../../../../general/perceptron.md#steps)
    - [perceptron § steps](../../../../general/perceptron.md#steps) / initialization
    - [perceptron § steps](../../../../general/perceptron.md#steps) / training
      - [perceptron § steps](../../../../general/perceptron.md#steps) / training / forward
      - [perceptron § steps](../../../../general/perceptron.md#steps) / training / backward
    - [perceptron § steps](../../../../general/perceptron.md#steps) / termination
- [feature engineering](../../../../general/feature%20engineering.md) ::@:: It is a preprocessing step in supervised machine learning and statistical modeling which transforms raw data into a more effective set of inputs. <p> Input variables may be created, modified, or selected (filtered/filtered out). <!--SR:!2025-03-17,18,329!2025-03-16,17,329-->
  - feature engineering / example: perceptron ::@:: A perceptron can only classify linearly separable data. <p> Given a non-linearly separable data, sometimes we may be able to derive a new input from the original inputs (e.g. _z_ = _x_<sup>2</sup> + _y_<sup>2</sup>) such that the data based on the new input is linearly separable. <!--SR:!2025-03-16,17,329!2025-03-16,17,329-->
- [Anaconda](../../../../general/Anaconda%20(Python%20distribution).md) ::@:: It is an open source data science and artificial intelligence distribution platform for Python and R programming languages. <!--SR:!2025-03-16,17,329!2025-03-16,17,329-->
  - Anaconda / download ::@:: <https://anaconda.com/download> <!--SR:!2025-03-16,17,329!2025-03-16,17,329-->
  - Anaconda / installation
  - Anaconda / usage

## week 3 lecture

- datetime: 2025-02-19T13:30:00+08:00/2025-02-19T14:50:00+08:00
- topic: reactive agents, search
- [finite state machine](../../../../general/finite%20state%20machine.md)
  - finite state machine / motivation for agents ::@:: The above agents we have introduced are stateless: they only respond to the current stimuli. They may not be powerful enough. <p> State machines can additionally remembered their previous actions, features, and its internal states (kinda like mental states). Then its action function additionally accepts the previous actions, features, and internal states. <!--SR:!2025-03-14,18,323!2025-03-08,11,293-->
  - finite state machine / agent architecture ::@:: same as statelessness: sensory input → perceptual processing → feature vector → action function (specified by the designer) → action <br/> added for statefulness: feature vector, action → memory (stores previous features and actions) → perceptual processing <!--SR:!2025-03-07,11,303!2025-04-10,36,303-->
  - finite state machine / production system ::@:: They can be represented by production system like stateless machines. The only difference is that the Boolean function also accepts machine states as input, not just input features. <!--SR:!2025-03-14,17,313!2025-03-08,11,293-->
- [search problem](../../../../general/search%20problem.md) ::@:: <!--SR:!2025-03-07,2,283!2025-03-24,19,343-->
  - search problem / examples ::@:: missionaries and cannibals problem, 8/15 puzzle <!--SR:!2025-03-23,18,343!2025-03-22,17,343-->
- [missionaries and cannibals problem](../../../../general/missionaries%20and%20cannibals%20problem.md) ::@:: Three missionaries and three cannibals must cross a river using a boat which can carry at most two people, under the constraint that, for both banks, if there are missionaries present on the bank, they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries). The boat cannot cross the river by itself with no people on board. <!--SR:!2025-03-22,17,343!2025-03-19,14,323-->
  - missionaries and cannibals problem / variations ::@:: These variations does not affect the solution: <br/> One of the cannibals has only one arm and cannot row. <br/> The missionaries and cannibals become three married couples, with the constraint that no woman can be in the presence of another man unless her husband is also present. <!--SR:!2025-03-24,19,343!2025-03-24,19,343-->
  - missionaries and cannibals problem / solving ::@:: The current state is represented by a simple vector ⟨m, c, b⟩. The vector's elements represent the number of missionaries, cannibals, and whether the boat is on the wrong (original) side, respectively. <p> Then we can think of the possible actions, also as vectors ⟨m, c, 1⟩ (b = 1 will be apparent in the next sentence). The boating rowing to the correct side subtracts an action vector while rowing to the wrong side adds an action vector. <p> Now we can _search_: Construct the state tree, perhaps using DFS. Start with an initial node with the initial state vector. Each valid action vector generates a child node, and we prune away nodes that violate the constraints. Repeat until the desired node is found (⟨0, 0, 0⟩), and the path from the initial node to the desired node is the solution. <!--SR:!2025-03-19,14,323!2025-03-24,19,343-->
- [15 puzzle](../../../../general/15%20puzzle.md) (8 puzzle) ::@:: It has 15 square tiles numbered 1 to 15 in a frame that is 4 tile positions high and 4 tile positions wide, with one unoccupied position. Tiles in the same row or column of the open position can be moved by sliding them horizontally or vertically, respectively. The goal of the puzzle is to place the tiles in numerical order (from left to right, top to bottom). <!--SR:!2025-03-19,14,323!2025-03-24,19,343-->
  - 15 puzzle / 8 puzzle (in the slides) ::@:: states: any arrangement of numbers 1 to 8 in the 3-by-3 board <br/> initial state: any given state <br/> goal: any other state; in the slides, a blank in the middle, with numbers ordered clockwise starting from the top-left corner <br/> actions: move the blank left, up, right, or down <br/> (path) cost: number of actions (length of the path) <!--SR:!2025-03-22,17,343!2025-03-22,17,343-->
- search problem
  - search problem / elements ::@:: set of states, start state, goal state (goal test), successor function (deterministic actins); if cost needs to be considered (considered in this course), a path cost function <!--SR:!2025-03-22,17,343!2025-03-22,17,343-->

## week 3 lecture 2

- datetime: 2025-02-21T13:30:00+08:00/2025-02-21T14:50:00+08:00
- topic: search
- search problem
  - search problem / problem-solving agent ::@:: These agents solve search problems, and are often _goal-directed_. <p> They find the best or "good enough" solution by _systematically_ considering different paths (sequences of actions) that may lead to the goal state. The different path are in a _representation space_, and this is where our agents search in. <p> After _finding a solution_, the agent _executes_ it. <!--SR:!2025-03-19,14,323!2025-03-19,14,323-->
  - search problem / [search algorithm](../../../../general/search%20algorithm.md) (search method) ::@:: Searching a solution can be thought of lazily expanding a search tree. The root is the initial state. A leaf node is expanded by applying all possible actions to the corresponding state. If a state that is a goal state is found, return it. Otherwise, if there are no more leaf nodes to expand, we could not a find a solution and return failure. <p> Choosing a leaf node to expand defines the _search strategy_, which is what we are studying here. <!--SR:!2025-03-22,17,343!2025-03-22,17,343-->
- [search algorithm](../../../../general/search%20algorithm.md) (search method) ::@:: an algorithm designed to solve a search problem <!--SR:!2025-03-22,17,343!2025-03-23,18,343-->
  - search algorithm / types ::@:: game tree, heuristic/informed, local, uninformed/blind, etc. <!--SR:!2025-03-23,18,343!2025-03-22,17,343-->
  - search algorithm / uninformed, blind ::@:: breadth-first search (BFS), depth-first search (DFS, backtracking search), iterative deepening search, etc. <!--SR:!2025-03-22,17,343!2025-03-23,18,343-->
  - search algorithm / explicit graph ::@:: A graph that is not too large (or infinite) to store explicitly. Often, repetitions can be identified and avoided. <p> We can measure its number of vertices $\lvert V \rvert$ and number of edges $\lvert E \rvert$. Note that $O(\lvert E \rvert)$ varies in between $O(1)$ and $O\left(\lvert V \rvert^2)$, depending on how sparse the input graph is. <!--SR:!2025-03-22,17,343!2025-03-22,17,343-->
  - search algorithm / implicit graph ::@:: A graph that is too large (or infinite) to store explicitly. <p> We can measure its branching factor $b$ (average out-degree). <!--SR:!2025-03-22,17,343!2025-03-24,19,343-->
- [breadth-first search](../../../../general/breadth-first%20search.md) (BFS) ::@:: It is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level. Extra memory, usually a queue, is needed to keep track of the child nodes that were encountered but not yet explored. <!--SR:!2025-03-24,19,343!2025-03-24,19,343-->
  - breadth-first search / completeness ::@:: If there is a solution, BFS will find it eventually, given unlimited time and space. (For this course: Yes.) <!--SR:!2025-03-22,17,343!2025-03-23,18,343-->
  - breadth-first search / optimality ::@:: Yes. If there are multiple solutions, BFS will find a solution with a shortest path from the root. (For this course: Yes.) <!--SR:!2025-03-24,19,343!2025-03-22,17,343-->
  - breadth-first search / time complexity ::@:: Explicit graph (without repetition): $O(\lvert V \rvert + \lvert E \rvert)$. Implicit graph (possibly with repetition): $O\left(b^{d + 1} \right)$, where $b$ is the branching factor (average out-degree) and $d$ is the number of edges to reach the solution. (For this course, use the implicit one, and remove the $+ 1$.) <p> It is impractical for most real world problems, and there are algorithms with better time complexity. <!--SR:!2025-03-19,14,323!2025-03-22,17,343-->
  - breadth-first search / space complexity ::@:: Explicit graph (without repetition): $O(\lvert V \rvert)$. Implicit graph (possibly with repetition): $O\left(b^{d + 1} \right)$, where $b$ is the branching factor (average out-degree) and $d$ is the number of edges to reach the solution. (For this course, use the implicit one, and remove the $+ 1$.) <p> It is impractical for most real world problems, and there are algorithms with better space complexity. <!--SR:!2025-03-19,14,323!2025-03-24,19,343-->
- search algorithm
  - search algorithm / importance ::@:: It determines the order of states expanded in the search state. Different algorithms lead to different search trees, and have different time and space complexities. <!--SR:!2025-03-23,18,343!2025-03-22,17,343-->
  - search algorithm / properties ::@:: completeness, optimality, space complexity, time complexity <!--SR:!2025-03-23,18,343!2025-03-24,19,343-->
  - search algorithm / completeness ::@:: Is the algorithm guaranteed to find a solution if it exists. <!--SR:!2025-03-23,18,343!2025-03-22,17,343-->
  - search algorithm / time complexity ::@:: How long does the algorithm take to find a solution? Note that it is frequently denoted using big O notation. <!--SR:!2025-03-22,17,343!2025-03-22,17,343-->
  - search algorithm / space complexity ::@:: How much memory does the algorithm use? Note that it is frequently denoted using big O notation. <!--SR:!2025-03-23,18,343!2025-03-24,19,343-->
  - search algorithm / optimality ::@:: Does the algorithm find an "_optimal_" solution if there are multiple solutions? <!--SR:!2025-03-23,18,343!2025-03-22,17,343-->
- [depth-first search](../../../../general/depth-first%20search.md) (DFS, backtracking search) ::@:: It is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking. Extra memory, usually a stack, is needed to keep track of the nodes discovered so far along a specified branch which helps in backtracking of the graph. <!--SR:!2025-03-19,14,323!2025-03-19,14,323-->
  - depth-first search / depth bound ::@:: A variation uses the _depth bound_, denoted $m$. It means the maximum depth (in terms of edges, inclusive) that DFS will search. Any deeper states are left un-generated (thus unexplored). <!--SR:!2025-03-22,17,343!2025-03-23,18,343-->
  - depth-first search / completeness ::@:: If there is a solution, DFS will find it eventually, given unlimited time and space. If _depth bound_ is used, we also require $m \ge d$, where $d$ is the number of edges to reach the solution. (For this course: Yes, if $m \ge d$.) <!--SR:!2025-03-23,18,343!2025-03-23,18,343-->
  - depth-first search / optimality ::@:: If there are multiple solutions, DFS will find a solution that comes first in lexicographic DFS ordering. (For this course: No.) <!--SR:!2025-03-19,14,323!2025-03-23,18,343-->
  - breadth-first search / time complexity ::@:: Explicit graph (without repetition): $O(\lvert V \rvert + \lvert E \rvert)$. Implicit graph (possibly with repetition): $O\left(b^{m + 1} \right)$, where $b$ is the branching factor (average out-degree) and $m$ is the depth bound (number of edges). (For this course, use the implicit one, and remove the $+ 1$.) <p> It is impractical for most real world problems, and there are algorithms with better time complexity. <!--SR:!2025-03-19,14,323!2025-03-19,14,323-->
  - breadth-first search / space complexity ::@:: Explicit graph (without repetition): $O(\lvert V \rvert)$. Implicit graph (possibly with repetition): $O(bm)$, where $b$ is the branching factor (average out-degree) and $m$ is the depth bound (number of edges). (For this course, use the implicit one.) <p> It is impractical for most real world problems, and there are algorithms with better space complexity. <!--SR:!2025-03-22,17,343!2025-03-07,2,303-->
- [iterative deepening search](../../../../general/iterative%20deepening%20depth-first%20search.md) (IDS, IDDFS) ::@:: A state space/graph search strategy in which a depth-limited version of depth-first search is run repeatedly with increasing depth limits until the goal is found. <!--SR:!2025-03-23,18,343!2025-03-24,19,343-->
  - iterative deepening search / motivation ::@:: What if we want the completeness, optimality of BFS while having the space complexity of DFS? (For time complexity, BFS and DFS are similar.) <!--SR:!2025-03-24,19,343!2025-03-23,18,343-->
  - iterative deepening search / description ::@:: Perform DFS with a depth bound repeatedly. The depth bound starts from 0, and increase by 1 each time DFS finishes, until a goal state is found. <!--SR:!2025-03-23,18,343!2025-03-24,19,343-->
  - iterative deepening search / completeness ::@:: If there is a solution, IDDFS will find it eventually, given unlimited time and space. (For this course: Yes.) <!--SR:!2025-03-24,19,343!2025-03-22,17,343-->
  - iterative deepening search / optimality ::@:: Yes. If there are multiple solutions, IDDFS will find a solution with a shortest path from the root. This is because the cumulative order in which nodes are first visited is effectively the same as in BFS. (For this course: Yes.) <!--SR:!2025-03-22,17,343!2025-03-23,18,343-->
  - iterative deepening search / time complexity ::@:: Implicit graph (possibly with repetition): $O\left(b^{d + 1} \right)$, where $b$ is the branching factor (average out-degree) and $d$ is the number of edges to reach the solution. (For this course, remove the $+ 1$.) <!--SR:!2025-03-19,14,323!2025-03-24,19,343-->
  - iterative deepening search / space complexity ::@:: Implicit graph (possibly with repetition): $O(d)$, where $d$ is the number of edges to reach the solution. <!--SR:!2025-03-24,19,343!2025-03-19,14,323-->
- search algorithm
  - search algorithm / implicit graph
    - search algorithm / implicit graph / repetition ::@:: As mentioned above, implicit graphs may repeat states. There are several ways to deal with this, in increasing effectiveness and overhead: do not return to the state we have just come from, which requires tracking the last state; do not create cycles, which requires tracking the current path; do not generate any state that has been generated, which requires tracking the set of generated states. <!--SR:!2025-03-24,19,343!2025-03-19,14,323-->
  - search algorithm / heuristic (informed) ::@:: The search uses a _heuristic function_, which given the current path and search tree, maps states to real numbers. The leaf with the smallest heuristic function value is expanded first. <!--SR:!2025-03-23,18,343!2025-03-22,17,343-->
    - search algorithm / heuristic / heuristic function ::@:: Given the current path and search tree, it usually measures how far the inputted state and path is from a goal state. <!--SR:!2025-03-23,18,343!2025-03-22,17,343-->
      - search algorithm / heuristic / heuristic function / examples ::@:: 8 puzzle: number of tiles out of place, current path length + number of tiles out of place, etc. <!--SR:!2025-03-22,17,343!2025-03-23,18,343-->

## assignments

## midterm examination

## final examination

## aftermath

### total
