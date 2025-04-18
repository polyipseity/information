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
  - objectives ::@:: appreciate AI problem solving; learn fundamental AI algorithm; understand AI challenges and goals
  - course intended learning outcomes (CILOs) ::@:: appreciate cutting edge AI research; identify AI fundamental concepts and techniques; understand and apply state space search techniques
  - syllabus
    - simple intelligent agents: machine evolution, machine learning, rule-based systems
    - search: adversarial, heuristic, uniformed
    - learning
    - knowledge planning, knowledge reasoning, knowledge representation
    - auction, game theory, multi-agent systems
    - uncertainty

## children

- [assignments](assignments/index.md)
<!-- - [questions](questions.md) -->

## week 1 tutorial

- datetime: 2025-02-04T12:30:00+08:00/2025-02-04T13:20:00+08:00
- status: unscheduled, no tutorial

## week 1 lecture

- datetime: 2025-02-05T13:30:00+08:00/2025-02-04T14:50:00+08:00
- topic: introduction, reactive agents
- [artificial intelligence](../../../../general/artificial%20intelligence.md) (AI) ::@:: John McCarthy, one of the founders of AI — "It is the science and engineering of making intelligent machines, especially intelligent computer programs. It is related to the similar task of using computers to understand human intelligence, but AI does not have to confine itself to methods that are biologically observable."
  - artificial intelligence (AI) / intuition ::@:: What is it? A calculator? An operating system? A text editor? ChatGPT or DeepSeek?
  - artificial intelligence (AI) / motivations ::@:: forefront of computer applications; make machines do things so far that can be done by humans; in the long-term, make machines that can act, sense, and think intelligently
  - artificial intelligence (AI) / algorithms, techniques ::@:: heuristic search algorithms, knowledge representation languages, machine learning algorithms and reasoners, etc.
  - artificial intelligence (AI) / impacts ::@:: engineering, science; everyday life; humanity in general
  - artificial intelligence (AI) / in computer science (CS) ::@:: science and engineering of making intelligent computer programs, the frontier of computer applications; new ways to solve problems with a computer
  - artificial intelligence (AI) / origins ::@:: Ada Lovelace (1815–1852), Alan Turing (1912–1954)
    - artificial intelligence (AI) / origins / Ada Lovelace (1815–1852) ::@:: Considered as the first computer programmer. Her Note G describes an algorithm for Babbage's analytical engine to compute Bernoulli numbers. She described the analytical engine as able to do what we tell it to perform, but cannot anticipate things that we do not tell it to perform.
    - artificial intelligence (AI) / origins / Alan Turing (1912–1954) ::@:: Computing machinery and intelligence. _Mind_, 59:433-460, 1950. — "I propose to consider the question, 'Can machines think?' This should begin with definitions of the meaning of the terms 'machine' and 'think.'"
      - Turing test ::@:: A test to empirically determine whether a computer has achieved intelligence. A human questioner questions two respondents, one human, the other a computer function, whose identities are unknown to the human questioner. Using a specified format and context, the questioner interrogates the two respondents within a specific subject area. After a preset length of time or number of questions, the questioner is then asked to decide which respondent is human and which is a computer.
  - artificial intelligence (AI) / history
    - artificial intelligence (AI) / history / 1956 ::@:: John McCarthy coined the term "__artificial intelligence__" as the topic of the Dartmouth Conference, the first conference devoted to the subject. The conference was proposed by John McCarthy, Marvin Minsky, Nathaniel Rochester, and Claude Shannon: "2 month, 10 man study of artificial intelligence".
    - artificial intelligence (AI) / history / Marvel (1992) ::@:: a real-time expert system that monitors the massive stream of data from the Voyager spacecraft, handling routine tasks, and alerting the analysts to more serious problems at Jet Propulsion Laboratory (JPL)
    - artificial intelligence (AI) / history / Pegasus (1994) ::@:: a speech understanding program that handles airline ticket reservations
    - artificial intelligence (AI) / history / Gulf War ::@:: An AI planning and scheduling system employed by US military. A DARPA report said the saving from this AI system had paid back the US Government all its investment on AI during the past 20 years.
    - artificial intelligence (AI) / history / older AIs & misc ::@:: Deep Blue (1997), IBM Watson (2011), AlphaFold (2020)
    - artificial intelligence (AI) / history / playing Go ::@:: AlphaGo (2016), AlphaGo Zero (2017)
    - artificial intelligence (AI) / history / GPT ::@:: GPT-3 (2020), ChatGPT (2022), GPT4 (2023), GPT4o (2024)
    - artificial intelligence (AI) / history / chatbots ::@:: ELIZA (1963, Weizenbaum; a computer psychotherapist) <br/> BlenderBot 3 (2022, Meta; letdown) <br/> AI Test Kitchen (2022, Google; announced only) <br/> ChatGPT (2022, OpenAI; breakthrough)
  - artificial intelligence (AI) / brittleness ::@:: Current AI systems are still brittle. Examples include hallucinations, object recognition, sensitivity to disturbance, etc.
- [hallucination](../../../../general/hallucination%20(artificial%20intelligence).md) ::@:: A response generated by AI that contains false or misleading information presented as fact, e.g. false negatives, false positives, incorrect predictions. It is associated with unjustified responses or beliefs rather than perceptual experiences.
  - hallucination / causes ::@:: These errors can be caused by a variety of factors, including data biases, incorrect model assumptions, insufficient training data, etc.
  - hallucination / examples ::@:: DALL-E 2 or Midjourney unable to create the image you want because the AI does not understand your desired context.
- [model collapse](../../../../general/model%20collapse.md) ::@:: It is a phenomenon where machine learning models gradually degrade due to errors coming from uncurated training on the outputs of another model, including prior versions of itself. Such outputs are known as synthetic data. <p> A study in 2024 shows this. For example, after successive generations, nonsense text are generated. Biases in the dataset get amplified, e.g. forgetting obscure dog breeds exist due to under-representation in the initial dataset.
- [intelligent agent](../../../../general/intelligent%20agent.md) ::@:: It is an entity that perceives its environment, takes actions autonomously to achieve goals, and may improve its performance through machine learning or by acquiring knowledge.
  - intelligent agent / features ::@:: can perceive, can perform actions, has an objective/goal
  - intelligent agent / learning objectives \(this course\) ::@:: stimulus-response agent (stateless), then add states
  - intelligent agent / control ::@:: e.g. designed vs. evolved/learned, genetic algorithms, neural networks, rules
  - intelligent agent / stimulus-response agent ::@:: Stateless machines that reacts to _immediate_ stimulus from the environment.
    - intelligent agent / stimulus-response agent / example ::@:: actions: up/down/left/right (cannot go into walls) <br/> environment: an enclosed 2D grid with walls <br/> objective: follow the boundary of the first obstacle met <br/> perceptions: 8 sensors for 8 adjacent cells, each testing if the corresponding cell is occupied <br/> policy: an algorithm to control the robot

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
  - perceptron / alias ::@:: threshold logical unit (TLU)
  - perceptron / supervised learning ::@:: It requires a training dataset. Each data in the dataset consists of _n_ _inputs_ as a _n_-dimensional vector and a _label_ (e.g. desired output). <p> Then, the task is computing a function that computes a "good" label from arbitrary _n_ inputs. This usually means agreeing with the training dataset's labels as much as possible (accuracy metric). <p> Here, we consider using a threshold linear unit (TLU; a.k.a perceptron) to learn the function.
  - perceptron / computation ::@:: Given a data vector $\mathbf x$; and weights $\mathbf w$, the bias $\theta$, and the activation function $f$ of a perceptron, the result is computed by: $$y = f(\mathbf x \cdot \mathbf w + \theta) \,.$$ <p> Given $n$ row data vectors vertically stacked as a matrix $\mathbf X$, the $n$ results as a column vector is computed by: $$\mathbf y = f\left(\mathbf X \mathbf w + \mathbf 1 \theta \right) \,.$$
    - perceptron / computation / activation function ::@:: $$f(u) = \begin{cases} 1 & \text{if }u \ge \theta \\ 0 & \text{if }u < \theta \end{cases}$$ <p> Usually, the threshold _θ_ is chosen to be 0. This is because we can always add to a perceptron, an new input that is always 1, and its weight set to the negation of the original threshold. Such a weight is known as the _bias_.
  - perceptron / Boolean functions ::@:: A function whose inputs are Booleans (0: false, 1: true) and the output is also a Boolean (0: false, 1: true). <p> _Linearly separable_ functions can be _learnt_ by a perceptron. But not all such functions are linearly separable, e.g. $x_1 \overline {x_2} + \overline {x_1} x_2$ (($x_1$ AND NOT $x_2$) OR (NOT $x_1$ AND $x_2$)) \(or better known as $x_1 \oplus x_2$ \($x_1$ XOR $x_2$\)\).
  - [perceptron § steps](../../../../general/perceptron.md#steps)
    - [perceptron § steps](../../../../general/perceptron.md#steps) / initialization ::@:: Initialize the weights arbitrarily. Weights may be initialized to 0 or small random values.
    - [perceptron § steps](../../../../general/perceptron.md#steps) / training ::@:: For each sample $j$ in the training dataset, perform the following steps over the input $\mathbf{x}_j$ and the desired output $d_j$:
      - [perceptron § steps](../../../../general/perceptron.md#steps) / training / forward ::@:: Calculate the actual output: $$y_j(t) = f(\mathbf{w}(t) \cdot \mathbf{x}_j) = f(w_0(t) x_{j, 0} + w_1(t) x_{j, 1} + \cdots + w_n(t) x_{j, n})$$. <p> The dot product can be interpreted as a weighted sum. Using linear algebra, this is: $$y_j(t) = f\left(\mathbf w(t)^\intercal \mathbf x_j \right)$$
      - [perceptron § steps](../../../../general/perceptron.md#steps) / training / backward ::@:: Update the weights: $$w_i(t + 1) = w_i(t) + r (d_j - y_j(t)) x_{j, i}$$ for all features $0 \le i \le n$. $r$ is the [learning rate](learning%20rate.md). <p> Since $x_{j, 0} = 1$ always, $w_0$ is effectively the bias $b$. Thus the above algorithm already includes updating the bias: $$b(t + 1) = b(t) + r(d_j - y_j(t)) \,.$$ <p> Using linear algebra, this is: $$\mathbf w(t + 1) = \mathbf w(t) + r (d_j - y_j(t)) \mathbf x_j$$
    - [perceptron § steps](../../../../general/perceptron.md#steps) / termination ::@:: For [offline training](offline%20training.md), the second step may be repeated until the batch or iteration error $\frac 1 s \sum_{j = 1}^s \lvert d_j - y_j(t) \rvert$ is less than a user-defined threshold $\gamma$, or a predetermined number of batches or iterations have been completed. $s$ is the batch or iteration (not to be confused with epoch) size. <p> If the training set is linearly separable, the above (i.e. termination) will eventually happen. The number of steps depends on the dataset ordering, initial weights, learning rate.
  - perceptron / biological neuron ::@:: inputs: dendrites; node/computation unit: cell nucleus; outputs: axons; weights: synapses <p> TLUs are is a very simple model of biological neuron.
  - perceptron / output ::@:: \(__this course__: A perceptron can only output 0 or 1 \(after activation function\).\)
- [linear separability](../../../../general/linear%20separability.md)
  - linear separability / determination ::@:: It is co-NP-complete to decide whether a Boolean function given in disjunctive or conjunctive normal form is linearly separable. <p> For manual determination, it is usually impossible. The most common situation in which you can manually determine it is by finding a XOR operation in the Boolean function. \(This is tested in assignment 1 and likely in examinations.\)
- [activation function](../../../../general/activation%20function.md) ::@:: In the context of an artificial neural network, it is a function that calculates the output of the node based on its individual inputs and their weights. Nontrivial problems can be solved using only a few nodes if the above is nonlinear.
  - activation function / examples ::@:: ReLU (rectified linear unit), logistic (sigmoid), hyperbolic tangent (tanh)
- [ReLU](../../../../general/rectifier%20(neural%20networks).md) ::@:: $$f(x) = \max(0, x)$$
  - ReLU / properties ::@:: continuous, linear, piecewise, differentiable almost everywhere
- [sigmoid](../../../../general/logistic%20function.md) ::@:: $$f(x) = \frac 1 {1 + e^{-x} }$$
- [hyperbolic tangent](../../../../general/hyperbolic%20functions.md) ::@:: $$f(x) = \frac {e^{x} - e^{-x} } {e^x + e^{-x} } = \frac {e^{2x} - 1} {e^{2x} + 1}$$
- [identity (activation)](../../../../general/identity%20function.md) (linear) ::@:: $$f(x) = x$$
  - identity (activation) / use ::@:: For output layers, target values used to train a model with such an activation function in the output layer are typically scaled before modeling using normalization or standardization transforms. Useful for _regression problems_.
- [neural network](../../../../general/neural%20network%20(machine%20learning).md) ::@:: __(Artificial) neural network__ (__(A)NN__) is one of the most powerful artificial intelligence and machine learning algorithms. It can approximate any [function](../../../../general/function%20(mathematics).md) from a certain [function space](../../../../general/function%20space.md), i.e. an _universal approximator_, by the [universal approximation theorem](../../../../general/universal%20approximation%20theorem.md). <p> As the name suggests, it draws inspiration from neurons in our brain and the way they are connected.
  - neural network / basic structure ::@:: A directed graph whose nodes are neurons. Those with no incoming edges are inputs/sources. Those wih no outgoing edges are output/targets. The remaining are internal nodes and represent _hidden_ features.
  - neural network / training overview ::@:: We initialize the weights of directed edges in the graph. Then while a condition to keep updating the weights is satisfied (e.g. accuracy target, number of updates), "improve" the weights. When the condition is no longer met, training has completed. <p> Two popular ways to "improve" the weights are gradient descent and _stochastic_ gradient descent (they are different things!).
- intelligent agent
  - intelligent agent / basic stateless architecture ::@:: sensory input → perceptual processing → feature vector → action function (specified by the designer) → action
  - intelligent agent / perception ::@:: Represented using a set of $x_i$. Note that there can be illegal combinations of values for the set $x_i$.
  - intelligent agent / action function ::@:: It consists of several statement in the form: If the set of $x_i$ has this combination of values, then perform a certain action.
- [Boolean algebra](../../../../general/Boolean%20algebra.md)
  - Boolean algebra / overview ::@:: $a$ AND $b$: $ab$ or $a \cdot b$; $a$ OR $b$: $a + b$; NOT $a$: $\overline a$ <p> AND and OR are associative and commutative.
- [production system](../../../../general/production%20system%20(computer%20science).md) ::@:: Essentially a giant if-else if-...-else program. <p> It is a _sequence_ (so it is ordered) in the form of: $c \to a$, where $c$ is a Boolean function and $a$ is an action. Find the first statement where $c$ evaluates to 1. Its action $a$ is the action the agent will take. <p> Commonly, we add a fallback case: $1 \to a$, where $1$ is the constant Boolean function always returning true.

## week 2 lecture 2

- datetime: 2025-02-14T13:30:00+08:00/2025-02-14T14:50:00+08:00
- topic: reactive agents
- [genetic programming](../../../../general/genetic%20programming.md) (GP) ::@:: An evolutionary algorithm, an artificial intelligence technique mimicking natural evolution, which operates on a population of programs.
  - genetic programming / motivation ::@:: Human evolves to become what we are now (unless you are not human). Maybe we can adapt evolution for machine learning? Evolution has two key components: reproduction and selection (survival of the fittest).
  - genetic programming / overview ::@:: Decide on how to represent _legal_ programs. Define a fitness function. Select some programs as generation 0. Produce the next generation until you have a "good enough" program. <p> 3 common methods to produce next generations: copy, crossover, and mutate.
  - genetic programming / program representation ::@:: Typically represented as tree structures. <p> We can consider statements in a program as functions. For example, AND(a, b) stands for a AND b and IF(a, b, c) stands for if a is true, then b, otherwise c. Then a program is a composition of many functions. <p> With this function composition in mind, we convert it into a tree recursively: A constant value or a input value is represented by a leaf. A function application/call is represented by having the function itself as a node and its arguments as its children nodes.
  - genetic programming / initialization ::@:: _full_, _grow_, _ramped half-and-half_, etc.
    - genetic programming / initialization / _grow_ ::@:: It creates the individuals sequentially. Every GP tree is created starting from the root, creating functional nodes with children as well as terminal nodes up to a certain depth.
    - genetic programming / initialization / _full_ ::@:: It is similar to _Grow_. The difference is that all branches in a tree are of same predetermined depth.
    - genetic programming / initialization / _ramped half-and-half_ ::@:: It creates a populations consisting of $md-1$ parts and a maximum depth of $md$ for its trees. The first part has a maximum depth of 2, second of 3 and so on up to the $md-1$-th part with maximum depth $md$. Half of every part is created by _Grow_, while the other part is created by _Full_.
  - genetic programming / selection ::@:: You need a fitness function to do so.
    - genetic programming / selection / example ::@:: We run the program for a certain number of steps and count the number of steps with an adjacent wall. We clamp its value between 0 and 32. We do 10 runs at random starting positions and sum the values (clamped between 0 and 320).
  - genetic programming / reproduction ::@:: Common methods for producing a new generation: copy, crossover, mutate.
    - genetic programming / reproduction / copy ::@:: Copy some programs from the previous generation. They are called the _parents_. A _tournament selection_ is used: randomly select some programs and choose the best one to copy. Other methods are possible. <p> A typical percentage of the new generation copied is 10%.
    - genetic programming / reproduction / crossover ::@:: From the copied _parents_, select 2 programs. A randomly chosen subtree of one parent is used to replace (including the subtree root node) a randomly selected subtree of another parent. <p> A typical percentage of the new generation crossover-ed is 90%.
    - genetic programming / reproduction / mutate ::@:: From the copied _parents_, select 1 program. Replace a randomly selected subtree by a new randomly generated subtree. <p> A typical percentage of the new generation mutated is 1% \(i.e. rarely occurs\).
  - genetic programming / performance ::@:: It depends on the initial generation size, copy/crossover/mutate rates, and tournament selection parameters. <p> The wall-following example in the slides generates a perfect tree after 10 generations.

## week 3 tutorial

- datetime: 2025-02-18T12:30:00+08:00/2025-02-18T13:20:00+08:00
- topic: TLU basics
- [object detection](../../../../general/object%20detection.md)
  - object detection / transplanted objects ::@:: elephant in the room: Transplanting such an object onto an image, it itself is often not detected or assumes wrong identities. It also has non-local effects, causing other previously correctly detected objects to go missing.
- [computer vision](../../../../general/computer%20vision.md)
  - computer vision / image recognition
    - computer vision / image recognition / fooling them ::@:: Current systems are easily fooled by: adding human-undetectable noise, adding small obstructions to an image, random patterns, geometric transformation of an object in the image, etc.
- [natural language processing](../../../../general/natural%20language%20processing.md) (NLP)
  - natural language processing / hallucinations ::@:: They are prone to creating content that do not match real-world facts (factuality hallucination) or user inputs (faithfulness hallucination, e.g. the year of an event being replaced by the year of another event). <p> Vision language models (VLMs) are also prone to this.
- [artificial intelligence](../../../../general/artificial%20intelligence.md) (AI)
  - artificial intelligence / recent trend ::@:: Its performance has been improving! For example, see the performance of works from different years on an object detection benchmark (COCO).
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
- [feature engineering](../../../../general/feature%20engineering.md) ::@:: It is a preprocessing step in supervised machine learning and statistical modeling which transforms raw data into a more effective set of inputs. <p> Input variables may be created, modified, or selected (filtered/filtered out).
  - feature engineering / example: perceptron ::@:: A perceptron can only classify linearly separable data. <p> Given a non-linearly separable data, sometimes we may be able to derive a new input from the original inputs (e.g. _z_ = _x_<sup>2</sup> + _y_<sup>2</sup>) such that the data based on the new input is linearly separable.
- [Anaconda](../../../../general/Anaconda%20(Python%20distribution).md) ::@:: It is an open source data science and artificial intelligence distribution platform for Python and R programming languages.
  - Anaconda / download ::@:: <https://anaconda.com/download>
  - Anaconda / installation
  - Anaconda / usage

## week 3 lecture

- datetime: 2025-02-19T13:30:00+08:00/2025-02-19T14:50:00+08:00
- topic: reactive agents, search
- [finite state machine](../../../../general/finite%20state%20machine.md)
  - finite state machine / motivation for agents ::@:: The above agents we have introduced are stateless: they only respond to the current stimuli. They may not be powerful enough. <p> State machines can additionally remembered their previous actions, features, and its internal states (kinda like mental states). Then its action function additionally accepts the previous actions, features, and internal states.
  - finite state machine / agent architecture ::@:: same as statelessness: sensory input → perceptual processing → feature vector → action function (specified by the designer) → action <br/> added for statefulness: feature vector, action → memory (stores previous features and actions) → perceptual processing
  - finite state machine / production system ::@:: They can be represented by production system like stateless machines. The only difference is that the Boolean function also accepts machine states as input, not just input features.
- [search problem](../../../../general/search%20problem.md) ::@:: It is a type of computational problem represented by a binary relation. Intuitively, the problem consists in finding structure "y" in object "x".
  - search problem / examples ::@:: missionaries and cannibals problem, 8/15 puzzle
- [missionaries and cannibals problem](../../../../general/missionaries%20and%20cannibals%20problem.md) ::@:: Three missionaries and three cannibals must cross a river using a boat which can carry at most two people, under the constraint that, for both banks, if there are missionaries present on the bank, they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries). The boat cannot cross the river by itself with no people on board.
  - missionaries and cannibals problem / variations ::@:: These variations do not affect the solution: <br/> One of the cannibals has only one arm and cannot row. <br/> The missionaries and cannibals become three married couples, with the constraint that no woman can be in the presence of another man unless her husband is also present.
  - missionaries and cannibals problem / solving ::@:: The current state is represented by a simple vector ⟨m, c, b⟩. The vector's elements represent the number of missionaries, cannibals, and whether the boat is on the wrong (original) side, respectively. <p> Then we can think of the possible actions, also as vectors ⟨m, c, 1⟩ (b = 1 will be apparent in the next sentence). The boating rowing to the correct side subtracts an action vector while rowing to the wrong side adds an action vector. <p> Now we can _search_: Construct the state tree, perhaps using DFS. Start with an initial node with the initial state vector. Each valid action vector generates a child node, and we prune away nodes that violate the constraints. Repeat until the desired node is found (⟨0, 0, 0⟩), and the path from the initial node to the desired node is the solution.
- [15 puzzle](../../../../general/15%20puzzle.md) (8 puzzle) ::@:: It has 15 square tiles numbered 1 to 15 in a frame that is 4 tile positions high and 4 tile positions wide, with one unoccupied position. Tiles in the same row or column of the open position can be moved by sliding them horizontally or vertically, respectively. The goal of the puzzle is to place the tiles in numerical order (from left to right, top to bottom).
  - 15 puzzle / 8 puzzle (in the slides) ::@:: states: any arrangement of numbers 1 to 8 in the 3-by-3 board <br/> initial state: any given state <br/> goal: any other state; in the slides, a blank in the middle, with numbers ordered clockwise starting from the top-left corner <br/> actions: move the blank left, up, right, or down <br/> (path) cost: number of actions (length of the path)
- search problem
  - search problem / elements ::@:: set of states, start state, goal state (goal test), successor function (deterministic actins); if cost needs to be considered \(__this course__: considered\), a path cost function

## week 3 lecture 2

- datetime: 2025-02-21T13:30:00+08:00/2025-02-21T14:50:00+08:00
- topic: search
- search problem
  - search problem / problem-solving agent ::@:: These agents solve search problems, and are often _goal-directed_. <p> They find the best or "good enough" solution by _systematically_ considering different paths (sequences of actions) that may lead to the goal state. The paths are in a _representation space_, and this is where the agents search in. <p> After _finding a solution_, the agents _executes_ it.
  - search problem / [search algorithm](../../../../general/search%20algorithm.md) (search method) ::@:: Searching a solution can be thought of lazily expanding a search tree. The root is the initial state. A leaf node is expanded by applying all possible actions to the corresponding state. If a state that is a goal state is found, return it. Otherwise, if there are no more leaf nodes to expand, we could not a find a solution and return failure. <p> Choosing a leaf node to expand defines the _search strategy_, which is what we are studying here.
- [search algorithm](../../../../general/search%20algorithm.md) (search method) ::@:: an algorithm designed to solve a search problem
  - search algorithm / types ::@:: game tree, heuristic/informed, local, uninformed/blind, etc.
  - search algorithm / uninformed, blind ::@:: breadth-first search (BFS), depth-first search (DFS, backtracking search), iterative deepening search (IDS, IDDFS), etc.
  - search algorithm / explicit graph ::@:: A graph that is not too large (or infinite) to store explicitly. Often, repetitions can be identified and avoided. <p> We can measure its number of vertices $\lvert V \rvert$ and number of edges $\lvert E \rvert$. Note that $O(\lvert E \rvert)$ varies in between $O(1)$ and $O\left(\lvert V \rvert^2 \right)$, depending on how sparse the input graph is.
  - search algorithm / implicit graph ::@:: A graph that is too large (or infinite) to store explicitly. <p> We can measure its branching factor $b$ (average out-degree).
- [breadth-first search](../../../../general/breadth-first%20search.md) (BFS) ::@:: It is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level. Extra memory, usually a queue, is needed to keep track of the child nodes that were encountered but not yet explored.
  - breadth-first search / completeness ::@:: If there is a solution, BFS will find it eventually, given unlimited time and space. \(__this course__: yes\)
  - breadth-first search / optimality ::@:: Yes. If there are multiple solutions, BFS will find a solution with a shortest path from the root. \(__this course__: yes\)
  - breadth-first search / worst-case time complexity ::@:: Explicit graph (without repetition): $O(\lvert V \rvert + \lvert E \rvert)$. Implicit graph (possibly with repetition): $O\left(b^d \right)$, where $b$ is the branching factor (average out-degree) and $d$ is the number of edges to reach the solution. \(__this course__: use the implicit one\) <p> It is impractical for most real world problems, and there are algorithms with better time complexity.
    - breadth-first search / worst-case time complexity / intuition ::@:: For explicit graph, each vertex and edge needs to be explored in the worst case, hence $O(\lvert V \rvert + \lvert E \rvert)$. <p> For implicit graph, if $d$ is the number of edges to reach the solution, the nodes that take not greater than $d$ edges are visited in the worst case, hence $O\left(b^d\right)$ to visit them.
  - breadth-first search / worst-case space complexity ::@:: Explicit graph (without repetition): $O(\lvert V \rvert)$. Implicit graph (possibly with repetition): $O\left(b^d \right)$, where $b$ is the branching factor (average out-degree) and $d$ is the number of edges to reach the solution. \(__this course__: use the implicit one\) <p> It is impractical for most real world problems, and there are algorithms with better space complexity.
    - breadth-first search / worst-case space complexity / intuition ::@:: For explicit graph, each vertex needs to be stored in the visited set in the worst case, hence $O(\lvert V \rvert)$. <p> For implicit graph, if $d$ is the number of edges to reach the solution, the nodes that take not greater than $d$ edges are visited in the worst case, hence $O\left(b^d\right)$ to store them.
- search algorithm
  - search algorithm / importance ::@:: It determines the order of states expanded in the search state. Different algorithms lead to different search trees, and have different time and space complexities.
  - search algorithm / properties ::@:: completeness, optimality, space complexity, time complexity
  - search algorithm / completeness ::@:: Is the algorithm guaranteed to find a solution if it exists?
  - search algorithm / time complexity ::@:: How long does the algorithm take to find a solution? Note that it is frequently denoted using big O notation.
  - search algorithm / space complexity ::@:: How much memory does the algorithm use? Note that it is frequently denoted using big O notation.
  - search algorithm / optimality ::@:: Does the algorithm find an "_optimal_" solution if there are multiple solutions?
- [depth-first search](../../../../general/depth-first%20search.md) (DFS, backtracking search) ::@:: It is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking. Extra memory, usually a stack, is needed to keep track of the nodes discovered so far along a specified branch which helps in backtracking of the graph.
  - depth-first search / depth bound ::@:: A variation uses the _depth bound_, denoted $m$. It means the maximum depth (in terms of edges, inclusive) that DFS will search. Any deeper states are left un-generated (thus unexplored).
  - depth-first search / completeness ::@:: If there is a solution, DFS will find it eventually, given unlimited time and space. If _depth bound_ is used, we also require $m \ge d$, where $d$ is the number of edges to reach the solution. \(__this course__: yes, if $m \ge d$\)
  - depth-first search / optimality ::@:: If there are multiple solutions, DFS will find a solution that comes first in lexicographic DFS ordering. \(__this course__: no\)
  - depth-first search / worst-case time complexity ::@:: Explicit graph (without repetition): $O(\lvert V \rvert + \lvert E \rvert)$. Implicit graph (possibly with repetition): $O\left(b^m \right)$, where $b$ is the branching factor (average out-degree) and $m$ is the depth bound (number of edges). \(__this course__: use the implicit one\) <p> It is impractical for most real world problems, and there are algorithms with better time complexity.
    - depth-first search / worst-case time complexity / intuition ::@:: For explicit graph, each vertex and edge needs to be explored in the worst case, hence $O(\lvert V \rvert + \lvert E \rvert)$. <p> For implicit graph, if $m$ is the depth bound \(number of edges\), the each vertex not greater than $m$ edges away needs to be explored in the worst case, hence $O\left(b^m\right)$ to visit them.
  - depth-first search / worst-case space complexity ::@:: Explicit graph (without repetition): $O(\lvert V \rvert)$. Implicit graph (possibly with repetition): $O(m)$ or $O(bm)$, where $b$ is the branching factor \(average out-degree\) and $m$ is the depth bound (number of edges). \(__this course__: use $O(bm)$\) <p> It is impractical for most real world problems, and there are algorithms with better space complexity.
    - depth-first search / worst-case space complexity / intuition ::@:: For explicit graph, each vertex needs to be stored in the visited set in the worst case, hence $O(\lvert V \rvert)$. <p> For implicit graph, if $m$ is the depth bound, the longest path has $m$ edges, hence $O(m)$ to store them. However, if your implementation \(which we assume above\) stores all generated but unvisited children along the path in the queue instead of generating them dynamically, then we need to multiply by $b$, hence $O(bm)$. \(__this course__: use $O(bm)$\)
- [iterative deepening search](../../../../general/iterative%20deepening%20depth-first%20search.md) (IDS, IDDFS) ::@:: A state space/graph search strategy in which a depth-limited version of depth-first search is run repeatedly with increasing depth limits until the goal is found.
  - iterative deepening search / motivation ::@:: What if we want the completeness, optimality of BFS while having the space complexity of DFS? (For time complexity, BFS and DFS are similar.)
  - iterative deepening search / description ::@:: Perform DFS with a depth bound repeatedly. The depth bound starts from 0, and increase by 1 each time DFS finishes, until a goal state is found.
  - iterative deepening search / completeness ::@:: If there is a solution, IDDFS will find it eventually, given unlimited time and space. \(__this course__: yes\)
  - iterative deepening search / optimality ::@:: Yes. If there are multiple solutions, IDDFS will find a solution with a shortest path from the root. This is because the cumulative order in which nodes are first visited is effectively the same as in BFS. \(__this course__: yes\)
  - iterative deepening search / worst-case time complexity ::@:: Implicit graph (possibly with repetition): $O\left(b^d \right)$, where $b$ is the branching factor (average out-degree) and $d$ is the number of edges to reach the solution.
    - iterative deepening search / worst-case time complexity / intuition ::@:: For implicit graph, if $d$ is the number of edges to reach the solution, the each vertex not greater than $d$ edges away needs to be explored in the worst case, hence $O\left(b^d\right)$ to visit them.
  - iterative deepening search / worst-case space complexity ::@:: Implicit graph (possibly with repetition): $O(d)$ or $O(bd)$, where $b$ is the branching factor \(average out-degree\) and $d$ is the number of edges to reach the solution. \(__this course__: use $O(bd)$\)
    - iterative deepening search / worst-case space complexity / intuition ::@:: For implicit graph, if $d$ is the number of edges to reach the solution, the longest path has $d$ edges, hence $O(d)$ to store them. However, if your implementation \(which we assume above\) stores all generated but unvisited children along the path in the queue instead of generating them dynamically, then we need to multiply by $b$, hence $O(bd)$. \(__this course__: use $O(bd)$\)
- search algorithm
  - search algorithm / implicit graph
    - search algorithm / implicit graph / repetition ::@:: As mentioned above, implicit graphs may repeat states. There are several ways to deal with this, in increasing effectiveness and overhead: do not return to the state we have just come from, which requires tracking the last state; do not create cycles, which requires tracking the current path; do not generate any state that has been generated, which requires tracking the set of generated states. <p> \(Note that for A\*, unless the heuristic is also consistent, you can at most deduplicate _visited_ instead of _generated_ states, otherwise the path may not be optimal.\)
  - search algorithm / heuristic (informed) ::@:: The search uses a _heuristic function_, which given the current path and search tree, maps states to real numbers. The leaf with the smallest heuristic function value is expanded first.
    - search algorithm / heuristic / heuristic function ::@:: Given the current path and search tree, it usually measures how far the inputted state and path is from a goal state.
      - search algorithm / heuristic / heuristic function / examples ::@:: 8 puzzle: number of tiles out of place, current path length + number of tiles out of place, etc.

## week 4 tutorial

- datetime: 2025-02-25T12:30:00+08:00/2025-02-25T13:20:00+08:00
- topic: simple agents
- intelligent agent
  - intelligent agent / aspects ::@:: memory, action, optimization, etc.
    - intelligent agent / aspects / memory ::@:: without: stimulus-response agent, with: state machine
    - intelligent agent / aspects / action ::@:: neural network, rule-based
    - intelligent agent / aspects / optimization ::@:: genetic programming, gradient descent
- production system
  - production system / capabilities ::@:: goal representation, memory (e.g. How many past readings?), sensors, stopping guarantee; multi-agents?
- genetic programming
  - genetic programming / motivation
  - genetic programming / overview
  - genetic programming / initialization
  - genetic programming / selection
  - genetic programming / reproduction
  - genetic programming / optimization ::@:: It can be considered as a zeroth-order optimization method (evolution). That is, the fitness/loss function is used directly, and its derivatives are not used.
    - genetic programming / optimization / gradient descent, Newton's method ::@:: They are respectively one of the first-order and second-order optimization methods. <p> The first uses first derivatives (gradient). The second uses both first and second derivatives (Hessian matrix). <p> Usually, the higher the order of the derivatives used, the more efficient and also computationally expensive the method is. <p> The first is commonly used in deep learning and machine learning. The second is good for convex problems.

## week 4 lecture

- datetime: 2025-02-26T13:30:00+08:00/2025-02-26T14:50:00+08:00
- topic: search
- [A\* search algorithm](../../../../general/A*%20search%20algorithm.md) ::@:: It is a graph traversal and pathfinding algorithm that is used in many fields of computer science due to its completeness, optimality, and optimal efficiency. Given a weighted graph, a source node and a goal node, the algorithm finds the shortest path (with respect to the given weights) from source to goal.
  - A\* search algorithm / idea ::@:: We want to find the shortest path from $a$ to $b$. We have $g(n)$ which is just the path cost function. We also have $h(n)$ which is an _estimate_ of the path cost from $n$ to $b$. We always expand the node with the lowest $g(n) + h(n)$ until we find the goal. <p> Under some condition on $h(n)$, which is that it never overestimates the path cost from $n$ to $b$ (_admissible_), A\* must return a least-cost path. Example: On a map, $h(n)$ can be the straight line distance (such a function is further _consistent_).
  - A\* search algorithm / algorithm ::@:: Start with a list (min-heap or priority queue is better) of nodes to be (re-)expanded, which will be called the _open set_. Add the starting node to it. <p> Repeat this paragraph until the _open set_ is empty. Select and remove the first node _n_ from the _open set_. If _n_ is the goal, output _n_. Otherwise, expand _n_ and add its children (i.e. exclude the parent) to the _open set_. Sort the _open set_ in increasing $g(n) + h(n)$ values, tie-breaking with the deepest node first (i.e. LIFO). Repeat starting from this paragraph. <p> If we have reached here (no _n_ has been outputted but the _open set_ is empty), output _failure_.
    - A\* search algorithm / algorithm / deduplication ::@:: Note that when expanding _n_, we exclude the expanded node \(but not the generated nodes, i.e. a node can be generated multiple times before being expanded\). This is a kind of deduplication. It assumes that there are no paths of negative costs, so going back to the parent must not decrease the path cost. <p> More advanced deduplication is possible: Also track the _currently known_ cost of the cheapest path from start to $n$ (this is actually just $g(n)$ but lazily computed and updated), called $g'(n)$. For each children $n'$ of $n$, check if $g(n) + w(n \to n') < g'(n)$, and only add $n'$ to the _open set_ if yes \(if $n'$ is already in the set, replace it with this new lower cost\). <p> If $h(n)$ is not only _admissible_, but also _consistent_, then using the above more advanced deduplication, each node is visited at most once.
  - A\* search algorithm / vs. Dijkstra's algorithm ::@:: When $h(n) = 0$ is a constant zero function, this is just Dijkstra's algorithm. A\* achieves better performance by using heuristics to guide its search.
- [admissible heuristic](../../../../general/admissible%20heuristic.md) ::@:: A heuristic function is said to be __admissible__ if it never overestimates the cost of reaching the goal, i.e. the cost it estimates to reach the goal is not higher than the lowest possible cost from the current point in the path. In other words, it should act as a lower bound. <p> Intuitively, as one walks along _any_ path from the start to the goal, $g(n) + h(n)$ is always not greater than the actual cost to the goal.
- [consistent heuristic](../../../../general/consistent%20heuristic.md) ::@:: A heuristic function is said to be __consistent__, or __monotone__, if its estimate is always less than or equal to the estimated distance from any neighbouring vertex to the goal, plus the cost of reaching that neighbour. <p> Intuitively, as one walks along _any_ path from the start to the goal, $g(n) + h(n)$ is non-decreasing.
  - consistent heuristic / example ::@:: A simple example is $h(n) = 0$. A more practical example is on a map, $h(n)$ is the straight line distance.
  - consistent heuristic / from admissible heuristic ::@:: If the number of operators is finite (thus finite branching factor), and the cost of each operator is greater than a positive real $\varepsilon$, then an admissible heuristic can be made into a consistent heuristic.
- A\* search algorithm
  - A\* search algorithm / behavior ::@:: Assuming $h(n)$ is _admissible_. Let $f*$ be the path cost to the optimal solution. Then the algorithm will explore all nodes with $f(n) < f*$, some of the non-solution nodes with $f(n) = f*$, and none of the nodes with $f(n) > f*$. <p> Assuming $h(n)$ is further _consistent_ (implies being _admissible_). Then the nodes are visited in increasing $f(n) = g(n) + h(n)$ up until $f*$ (inclusive). Some of the non-solution nodes with $f(n) = f$ may be visited. Further, it is _optimally efficient_ in that no other algorithms expand a subset of the nodes expanded by this algorithm (Dechter and Pearl, 1985).
  - A\* search algorithm / completeness ::@:: If there is a solution, yes, for finite graphs with nonnegative edges, and infinite graphs with finite branching factors and edge costs larger than a positive real $\varepsilon$. If there are no solutions, the former is guaranteed to terminate while the latter is not. <p> Proof is by realizing that there are a finite number of nodes to expand (nodes with $f(n) < f*$) before expanding nodes with $f*$.
  - A\* search algorithm / optimality ::@:: Given the heuristic function is _admissible_, yes. <p> Proof is by assuming a non-optimal path is outputted and deriving a contradiction: <p> __S__<sub>__true__</sub> \< __T__<sub>__true__</sub>: __S__ is an optimal path and __T__ is a non-optimal path. <br/> __T__<sub>__eval__</sub> ≤ __S__<sub>__eval__</sub>: __T__ was picked instead of __S__ before terminating. <br/> __T__<sub>__eval__</sub> ≤ __T__<sub>__true__</sub>, __S__<sub>__eval__</sub> ≤ __S__<sub>__true__</sub>: The heuristic is admissible.
  - A\* search algorithm / worst-case space complexity ::@:: $O(|V|)=O(b^{d})$, where _d_ is the depth of the solution \(the length of the shortest path\) and _b_ is the [branching factor](../../../../general/branching%20factor.md) \(the maximum number of successors for a state\), as it stores all generated nodes in memory.
    - A\* search algorithm / worst-case space complexity / intuition ::@:: Its space complexity is roughly the same as that of all other graph search algorithms, as it keeps all generated nodes in memory.
  - A\* search algorithm / worst-case time complexity ::@:: $O(|E|\log |V|)=O(b^{d})$
    - A\* search algorithm / worst-case time complexity / intuition ::@:: For explicit graph, it is hard to explain why it is $O(\lvert E \rvert \log \lvert V \rvert)$. <p> For implicit graph, if $d$ is the number of edges to reach the solution, the nodes that take not greater than $d$ edges are visited in the worst case, hence $O\left(b^d\right)$ to store them.
  - A\* search algorithm / heuristic function ::@:: _Admissible_ heuristic functions that give higher values (i.e. more accurate) tend to (but not _always_) make the search more efficient. <p> (The slides say if an admissible heuristic function $h$ dominates over another $h'$ ($h(n) \ge h'(n)$ for all $n$), then it is _always_ better to use it. This should not be correct... the _always_ should be replaced by _probably_.)
  - A\* search algorithm / variants ::@:: iterative deepening A\* (IDA\*), memory-bounded A\*, simplified memory bounded A\* (SMA\*)
- [iterative deepening A\*](../../../../general/iterative%20deepending%20A*.md) ::@:: It works as follows: at each iteration, perform a [depth-first search](../../../../general/depth-first%20search.md), cutting off a branch when its total cost $f(n)=g(n)+h(n)$ exceeds a given _threshold_. This threshold starts at the estimate of the cost at the initial state, and increases for each iteration of the algorithm. At each iteration, the threshold used for the next iteration is the minimum cost of all values that exceeded the current threshold.
- [SMA\*](../../../../general/SMA*.md) ::@:: Literally just A\* but nodes with the highest f-cost ($f(n) = g(n) + h(n)$) are pruned from the queue when there isn't any space left. Because those nodes are deleted, simple memory bounded A\* has to remember the f-cost of the best forgotten child of the parent node. When it seems that all explored paths are worse than such a forgotten path, the path is regenerated.

## week 4 lecture 2

- datetime: 2025-02-28T13:30:00+08:00/2025-02-28T14:50:00+08:00
- topic: search, constraint satisfaction problem \(CSP\)
- admissible heuristic
  - admissible heuristic / construction ::@:: It can be derived from a relaxed version of the problem (dropping conditions, but remember to check if the resulting heuristic is _admissible_), or by information from pattern databases that store exact solutions to subproblems of the problem, or by using inductive learning methods.
    - admissible heuristic / construction / examples ::@:: ABSOLVER (Prieditis, 1993) is a computer program that automatically generates heuristics based on relaxing problems and other techniques.
- [constraint satisfaction problem](../../../../general/constraint%20satisfaction%20problem.md) (CSP) ::@:: They are mathematical questions defined as a set of objects whose state must satisfy a number of constraints or limitations. CSPs represent the entities in a problem as a homogeneous collection of finite constraints over variables, which is solved by constraint satisfaction methods.
  - constraint satisfaction problem / definition ::@:: It is defined as a triple $\langle X,D,C\rangle$, where <p> - $X=\{X_{1},\ldots ,X_{n}\}$ is a set of variables, <br/> - $D=\{D_{1},\ldots ,D_{n}\}$ is a set of their respective domains of values, and <br/> - $C=\{C_{1},\ldots ,C_{m}\}$ is a set of constraints. <p> Each variable $X_{i}$ can take on the values in the nonempty domain $D_{i}$. Every constraint $C_{j}\in C$ is in turn a pair $\langle t_{j},R_{j}\rangle$, where $t_{j}\subseteq \{1,2,\ldots ,n\}$ is a set of $k$ indices and $R_{j}$ is a $k$-ary [relation](../../../../general/relation%20(mathematics).md) on the corresponding product of domains $\times _{i\in t_{j} }D_{i}$ where the product is taken with indices in ascending order. (Simply put, each $C_j$ relates a set of $k$ variables together.)
    - constraint satisfaction problem / definition / evaluation ::@:: It is a function from a subset of variables to a particular set of values in the corresponding subset of domains. (Simply put, the function assigns values to some of the variables.) An evaluation $v$ satisfies a constraint $\langle t_{j},R_{j}\rangle$ if the values assigned to the variables $t_{j}$ satisfy the relation $R_{j}$.
    - constraint satisfaction problem / definition / solution ::@:: An evaluation is _consistent_ if it does not violate any of the constraints. An evaluation is _complete_ if it includes all variables. An evaluation is a _solution_ if it is consistent and complete; such an evaluation is said to _solve_ the constraint satisfaction problem.
  - constraint satisfaction problem / examples ::@:: eight queens puzzle, logic puzzles, map coloring problem, maximum cut problem, type inference, etc.
- [eight queens puzzle](../../../../general/eight%20queens%20puzzle.md) ::@:: It is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. There are 92 solutions.
  - eight queens puzzle / generalization ::@:: _n_ queens on a _n_-by-_n_ chessboard
  - eight queens puzzle / CSP ::@:: The set of variables can be the row position of the queen in each column. The set of domains is from 1 to 8. Note that this already encodes the constraint that no two queens share the same column. <p> There are two more constraint sets to encode: No two queens share the same row. No two queens share the same diagonal.
- constraint satisfaction problem
  - constraint satisfaction problem / constructive methods ::@:: Use search algorithms, e.g. depth-first search, to find a solution. To encode a CSP as a search problem: <p> Any partial assignment is a state. The initial state is the empty assignment. The actions are assign a value to a new variable. The goal is a solution assignment. A path cost function is not used (the path cost is always 0). <p> The problem with this approach is that, without _pruning_, the search space (the number of states, including constraint-violating ones) explodes exponentially.
- [local consistency](../../../../general/local%20consistency.md) ::@:: They are properties of constraint satisfaction problems related to the consistency of subsets of variables or constraints. They can be used to reduce the search space and make the problem easier to solve.
  - local consistency / constraint propagation ::@:: Every local consistency condition can be enforced by a transformation that changes the problem without changing its solutions (but solutions can be hidden away). <p> It works by reducing domains of variables, strengthening constraints, or creating new constraints. This leads to a reduction of the search space, making the problem easier to solve by some algorithms.
    - local consistency / constraint propagation / methods ::@:: Boolean satisfiability problem (SAT), constraint graph, etc.
- [constraint graph](../../../../general/constraint%20graph.md) ::@:: They are used to represent relations among constraints in a constraint satisfaction problem.
  - constraint graph / hypergraph ::@:: It is a hypergraph in which the vertices correspond to the variables, and the hyperedges correspond to the constraints. A set of vertices forms a hyperedge if the corresponding variables are those occurring in some constraint.
  - constraint graph / graph ::@:: The hypergraph can be converted into a _bipartite_ graph if each hyperedge is replaced by a new vertex with edges to all vertices previously connected by the hyperedge.
  - constraint graph / consistency propagation ::@:: Assign a value to a variable first. Then remove constraint-violating elements in vertices (representing other variables) adjacent to the variables. If you have removed any element in a vertex, run the above thing again for that vertex's adjacent vertices. This is done recursively (in BFS or DFS order) until no new elements have been removed. <p> Repeat the above until a solution has been found yet or could not be found. Note that failing to find a solution _does not_ imply a solution does not exist.
    - constraint graph / consistency propagation / properties ::@:: This procedure does not create new solutions but may remove some solutions. It is possible for this procedure to remove all solutions even if solutions exist (and _backtracking_ is needed to solve this).
  - constraint graph / note ::@:: \(__this course__: Our constraint graph only contains constraints involving exactly two variables as edges. Constraints involving more variables are not shown on the constraint graph, but still needs to be reasoned.\)
- [Boolean satisfiability problem](../../../../general/Boolean%20satisfiability%20problem.md) \(SAT\) ::@:: It asks whether there exists an interpretation that satisfies a given Boolean formula. In other words, it asks whether the formula's variables can be consistently replaced by the values TRUE or FALSE to make the formula evaluate to TRUE. If this is the case, the formula is called satisfiable, else unsatisfiable.
  - Boolean satisfiability problem / conjunctive normal form \(CNF\) ::@:: A _literal_ is either a variable \(in which case it is called a _positive literal_\) or the negation of a variable \(called a _negative literal_\). A _clause_ is a disjunction \(OR\) of literals \(or a single literal\). A clause is called a _[Horn clause](../../../../general/Horn%20clause.md)_ if it contains at most one positive literal. A formula is in _[conjunctive normal form](../../../../general/conjunctive%20normal%20form.md)_ \(CNF\) if it is a conjunction \(AND\) of clauses \(or a single clause\).
  - Boolean satisfiability problem / status ::@:: It is the first _NP-complete_ problem discovered by Cook. It is also one of the most intensely studied NP-complete problems as it has a huge literature and many applications.
  - Boolean satisfiability problem / 3-satisfiability \(3SAT\) ::@:: Each _clause_ has no more than 3 _literals_. In terms of computational complexity, it is equivalent to SAT \(NP-complete\).
    - Boolean satisfiability problem / 3-satisfiability / reduction ::@:: To reduce the unrestricted SAT problem to 3-SAT, transform each clause _l_<sub>1</sub> ∨ ⋯ ∨ _l_<sub>_n_</sub> to a conjunction of _n_ - 2 clauses <p> \(_l_<sub>1</sub> ∨ _l_<sub>2</sub> ∨ _x_<sub>2</sub>\) ∧ <br/> \(¬<!-- markdown separator -->_x_<sub>2</sub> ∨ _l_<sub>3</sub> ∨ _x_<sub>3</sub>\) ∧ <br/> \(¬<!-- markdown separator -->_x_<sub>3</sub> ∨ _l_<sub>4</sub> ∨ _x_<sub>4</sub>\) ∧ ⋯ ∧ <br/> \(¬<!-- markdown separator -->_x_<sub>_n_<!-- markdown separator -->−3</sub> ∨ _l_<sub>_n_<!-- markdown separator -->−2</sub> ∨ _x_<sub>_n_<!-- markdown separator -->−2</sub>\) ∧ <br/> \(¬<!-- markdown separator -->_x_<sub>_n_<!-- markdown separator -->−2</sub> ∨ _l_<sub>_n_<!-- markdown separator -->−1</sub> ∨ _l_<sub>_n_</sub>\) <p> where _x_<sub>2</sub>, ⋯ , <!-- markdown separator -->_x_<sub>_n_<!-- markdown separator -->−2</sub> are [fresh variables](../../../../general/fresh%20variable.md) not occurring elsewhere. Although the two formulas are not [logically equivalent](../../../../general/logically%20equivalent.md), they are [equisatisfiable](../../../../general/equisatisfiable.md).
- [SAT solver](../../../../general/SAT%20solver.md) ::@:: It is a computer program which aims to solve the Boolean satisfiability problem (SAT).
  - SAT solver / soundness ::@:: The program returns yes _only if_ the input is satisfiable. We want _\(this\)_ property.
    - [soundness](../../../../general/soundness.md)
  - SAT solver / completeness ::@:: The program returns yes _if and only if_ the input is satisfiable. We want _\(this\)_ property, but we may give up this for performance.
    - [completeness](../../../../general/completeness%20(logic).md)
- [DPLL algorithm](../../../../general/DPLL%20algorithm.md) ::@:: It is a _complete_, backtracking-based search algorithm for deciding the satisfiability of propositional logic formulae in conjunctive normal form, i.e. for solving the CNF-SAT problem. <p> It is a _constructive_ method.
  - DPLL algorithm / full name ::@:: Davis–Putnam–Logemann–Loveland algorithm
  - DPLL algorithm / algorithm ::@:: <pre>__function__ _DPLL_\(Φ\)<br/>    // unit propagation:<br/>    __while__ there is a unit clause {_l_} in Φ __do__<br/>        Φ ← _unit-propagate_\(_l_, Φ\);<br/>    // pure literal elimination:<br/>    __while__ there is a literal _l_ that occurs pure in Φ __do__<br/>        Φ ← _pure-literal-assign_\(_l_, Φ\);<br/>    // stopping conditions:<br/>    __if__ Φ is empty __then__<br/>        __return__ true;<br/>    __if__ Φ contains an empty clause __then__<br/>        __return__ false;<br/>    // DPLL procedure:<br/>    _l_ ← _choose-literal_\(Φ\);<br/>    __return__ _DPLL_\(Φ __∧__ {l}\) __or__ _DPLL_\(Φ __∧__ {¬l}\);</pre>
    - DPLL algorithm / algorithm / pruning ::@:: In this pseudocode, `unit-propagate(l, Φ)` and `pure-literal-assign(l, Φ)` are functions that return the result of applying unit propagation and the pure literal rule, respectively, to the literal `l` and the formula `Φ`. In other words, they replace every occurrence of `l` with "true" and every occurrence of `not l` with "false" in the formula `Φ`, and simplify the resulting formula. <p> For `pure-literal-assign(l, Φ)`, `l` appears only _purely positively_. That is, if `m` appears only _purely negatively_, then `l` should be `not m`.
      - DPLL algorithm / algorithm / pruning / detail ::@:: Provided a literal `l` to assign "true", clauses with `l` are removed from the CNF, because they have been satisfied. Clauses with `not l` have `not l` removed from itself \(but the clause itself is not removed, even if it will become empty afterwards\). Then the resulting CNF formula is processed further as outlined above.
    - DPLL algorithm / algorithm / note ::@:: The __`or`__ in the __`return`__ statement is a [short-circuiting operator](../../../../general/short-circuiting%20operator.md). `Φ ∧ {l}` denotes the simplified result of substituting "true" for `l` in `Φ`.
    - DPLL algorithm / algorithm / lecture slides ::@:: \(__this course__: In the lecture slides, the checking steps are in a different order: check empty, check has empty clause, then check for a pure literal, then check for a unit clause, then finally select a variable. If a check passes, either yes, no, or the algorithm is recursively called after replacing a literal with "true", so no `while` appears in the lecture slides. <p> The intermediate steps and CNFs are different. While the algorithm returns the same result \(satisfiability\) as the original, the instructors may prefer us to show the steps in the above order instead.\)
  - DPLL algorithm / completeness ::@:: It is complete \(_constructive_ method\). <p> Notice that the algorithm without the pure literal rule is _almost_ simply trying all 2<sup>_n_</sup> possible inputs for the _n_ variables \(the unit propagation rule eliminates unit clauses in the _initial_ CNF formula, hence "almost"\). This is _backtracking_. Then, the pure literal rule is simply a _sound_ rule to _prune_ more of the search space.

## week 5 tutorial

- datetime: 2025-03-04T12:30:00+08:00/2025-03-04T13:20:00+08:00
- topic: search
- intelligent agents
  - intelligent agents / search problem ::@:: Simple agents \(production system, state machine\) cannot do search problem by itself alone. Solving a search problem requires planning ahead \(e.g. evaluating states that have not been reached yet\). <p> After an agent computes a solution to a search problem, we can simply input the solution into another simple agent to "solve" it by executing the solution \(the simple agent does not even need computation and sensing\).
- search problem
  - search problem / notations ::@:: common notations: set of states $\mathcal S$, initial state $I \in \mathcal S$, set of goal states $\mathcal G \subseteq \mathcal S$ \(goal state $G \in \mathcal G \subseteq \mathcal S$\), set of actions $\mathcal A$, successor function $T: \mathcal S \times \mathcal A \to \mathcal S$, cost function $c: \mathcal S \times \mathcal A \to \mathbb R$, solution: a sequence of actions from $I$ to some $G \in \mathcal G$
- search algorithm
  - search algorithm / terminology ::@:: expansion, frontier/fringe, search tree, strategy, state space graph
  - search algorithm / breadth-first search \(BFS\) ::@:: The strategy is expanding shallowest nodes first. It can be implemented using a FIFO queue. <p> It can be reduced from _uniform cost search_ by setting the cumulative cost function to the number of edges to reach the node.
  - search algorithm / uniform cost search \(UCS\) ::@:: The strategy is expanding nodes with the lowest cumulative cost first. It can be implemented using a priority queue that puts nodes with lower cumulative cost earlier in the queue. <p> It generalizes _breadth-first search_ by allowing the edges to have weights, which specifies the cost of taking the edge in a solution. <p> An example is Dijkstra's algorithm.
  - search algorithm / greedy search ::@:: The strategy is expanding nodes with the lowest _estimated_ cost to a goal state first. It can be implemented using a priority queue that puts nodes with lower estimated cost earlier in the queue. <p> It differs from BFS and UCS in that it uses the _estimated_ cost to a goal state rather than the cumulative cost from the initial state.
  - search algorithm / A\* search algorithm ::@:: The strategy is expanding nodes with the lowest _sum_ of cumulative cost and _estimated_ cost to a goal state first. It can be implemented using a priority queue \(tie-breaking with the deepest node, i.e. LIFO\). <p> It can be seen as a hybrid of _uniform cost search_ \(cumulative cost\) and _greedy search_ \(estimated cost to a goal state\).

## week 5 lecture

- datetime: 2025-03-05T13:30:00+08:00/2025-03-05T14:50:00+08:00
- topic: constraint satisfaction problem \(CSP\)
- DPLL algorithm
  - DPLL algorithm / state of the art ::@:: The main improvement has been Conflict-Driven Clause Learning (CDCL), which is similar to DPLL but after reaching a conflict "learns" the root causes (assignments to variables) of the conflict, and uses this information to perform non-chronological backtracking (aka backjumping) in order to avoid reaching the same conflict again.
- [conflict-driven clause learning](../../../../general/conflict-driven%20clause%20learning.md) \(CDCL\) ::@:: It is an algorithm for solving the Boolean satisfiability problem (SAT).
  - conflict-driven clause learning / difference from DPLL ::@:: The main difference between CDCL and DPLL is that CDCL's backjumping is non-chronological. Another difference is that when a conflict occurs, a new clause is learnt to avoid it again.
  - conflict-driven clause learning / algorithm ::@:: 1. Select a variable and assign True or False. This is called decision state. Remember the assignment. <br/> 2. Apply Boolean constraint propagation (unit propagation). <br/> 3. Build the [implication graph](../../../../general/implication%20graph.md). <br/> 4. If there is any conflict <br/> &emsp; 1. Find the cut in the implication graph that led to the conflict <br/> &emsp; 2. Derive a new clause which is the negation of the assignments that led to the conflict <br/> &emsp; 3. Non-chronologically backtrack ("back jump") to the appropriate decision level, where the first-assigned variable involved in the conflict was assigned <br/> 5. Otherwise continue from step 1 until all variable values are assigned.
- GSAT, [WalkSAT](../../../../general/WalkSAT.md) ::@:: They are local search algorithms to solve Boolean satisfiability problems. <p> They are _heuristic repair_ methods.
  - GSAT, WalkSAT / overview ::@:: They start by assigning a random value to each variable in the formula. If the assignment satisfies all clauses, the algorithm terminates, returning the assignment. Otherwise, a variable is flipped and the above is then repeated until all the clauses are satisfied. WalkSAT and GSAT differ in the methods used to select which variable to flip. <p> Both algorithms may restart with a new random assignment if no solution has been found for too long, as a way of getting out of local minima of numbers of unsatisfied clauses.
    - GSAT, WalkSAT / overview / GSAT ::@:: It makes the change which minimizes the number of unsatisfied clauses in the new assignment, or with some probability picks a variable at random. <p> It can be seen as a _min-conflicts algorithm_. <p> \(__this course__: minimize the number of unsatisfied clauses\)
  - GSAT, WalkSAT / algorithm
    - GSAT, WalkSAT / algorithm / GSAT ::@:: Given a CNF formula Φ, max restarts _mr_, and max climbs _mc_, it returns either a SAT solution or fails. <p> 1. Repeat this block for at most _mr_ times. <br/> &emsp; 1. Randomly generate an assignment. <br/> &emsp; 2. Repeat this block for at most _mc_ times. <br/> &emsp;&emsp; 1. If the assignment satisfies Φ, return the assignment. <br/> &emsp;&emsp; 2. Generate successors of the assignment by flipping exactly one variable. _n_ variables should generate _n_ successors. <br/> &emsp;&emsp; 3. Select the assignment that minimizes the number of unsatisfied clauses. <br/> 2. Return failure.
  - GSAT, WalkSAT / completeness ::@:: It is sound but incomplete \(_heuristic repair_ method\).
- [heuristic](../../../../general/heuristic%20(computer%20science).md) ::@:: It is a technique designed for problem solving more quickly when classic methods are too slow for finding an exact or approximate solution, or when classic methods fail to find any exact solution in a search space.
  - heuristic / repair ::@:: It starts with a proposed solution that probably does not satisfy all constraints. Then it repairs the solution until it does.
- [min-conflicts algorithm](../../../../general/min-conflicts%20algorithm.md) ::@:: It is a search algorithm or heuristic method to solve constraint satisfaction problems. \(__this course__: It is by Gu.\) <p> It can be seen as a _hill climbing_ algorithm, where the "hill" to be climbed is the number of satisfied constraints.
- [unsupervised learning](../../../../general/unsupervised%20learning.md) ::@:: It is a framework in machine learning where, in contrast to supervised learning, algorithms learn patterns exclusively from unlabeled data.
  - unsupervised learning / contrast ::@:: reinforcement learning \(even though it also does not require labeled data\), supervised learning
  - unsupervised learning / examples ::@:: Brown/IBM clustering, image clustering
- [reinforcement learning](../../../../general/reinforcement%20learning.md) \(RL\) ::@:: It is an interdisciplinary area of machine learning and optimal control concerned with how an intelligent agent should take actions in a dynamic environment in order to maximize a reward signal. It is one of the three basic machine learning paradigms, alongside supervised learning and unsupervised learning.
- [Brown clustering](../../../../general/Brown%20clustering.md)
  - Brown clustering / natural language processing ::@:: In natural language processing \(NLP\), it is a form of hierarchical clustering of words based on the contexts in which they occur, proposed in 1992.

## week 5 lecture 2

- datetime: 2025-03-07T13:30:00+08:00/2025-03-07T14:50:00+08:00
- topic: constraint satisfaction problem \(CSP\), game tree search
- [_k_-means clustering](../../../../general/k-means%20clustering.md) ::@:: It is a method of vector quantization, originally from signal processing, that aims to partition _n_ observations into _k_ clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster.
  - _k_-means clustering / characteristics ::@:: does not require data to be labeled, hyperparameter _k_, parametric (centroid locations), unsupervised
  - _k_-means clustering / algorithm ::@:: Choose _k_ initial centroids. They are usually data points in the training dataset. <p> Find distances (using a distance function) of training data to the centroids. Assign each data point to the closest centroid (a tie-breaking method may be required). Re-compute the centroids using the centroid memberships (_k_-means use the mean, _k_-medians use the median, _k_-modes use the mode, _k_-medoids use an actual training point). If a _stopping criterion_ is not met, repeat the above steps again.
  - _k_-means clustering / CSP ::@:: The variables are cluster assignments of each data point \(_n_ data points\) and cluster centroid positions \(_k_ clusters\), for a total of _n_ + _k_ variables. Cluster assignments have a domain of {1, ..., _n_}. Cluster centroid positions have a domain of the feature space. The constraint is minimizing the sum of squared distances to assigned cluster centroids. <p> The resulting algorithm is essentially the same as the usual one described above, but using CSP terminology, as described below. <p> Initialize the cluster centroid positions. Repeat the following two statements until termination condition has been met: Compute the best cluster assignments. Then compute the best centroid positions.
- [hill climbing](../../../../general/hill%20climbing.md) ::@:: It is a mathematical optimization technique which belongs to the family of local search. <p> It is an iterative algorithm that starts with an arbitrary solution to a problem, then attempts to find a better solution by making an incremental change to the solution. If the change produces a better solution, another incremental change is made to the new solution, and so on until no further improvements can be found.
  - hill climbing / search problem ::@:: A search problem can be converted into a function maximization problem by designing such a function that is maximum for a solution state. <p> For example, designing very large scale integration \(VLSL\) circuits requires finding a layout satisfying \(many\) constraints.
  - hill climbing / differences ::@:: Major differences include that it does not maintain a search tree. It also does not backtrack.
  - hill climbing / algorithm ::@:: Set the current state to the initial state. Then, literally just keep choosing the _highest_ valued successor for the current state until all successors have lower values. Then return the current state.
  - hill climbing / problems ::@:: A major problem is that it does not necessarily find the _global_ maximum. It may find a _local_ maximum instead. _Simulated annealing_ is one way of mitigating this. <p> \(There are other major problems unmentioned here.\)
- [simulated annealing](../../../../general/simulated%20annealing.md) \(SA\) ::@:: It is a probabilistic technique for _approximating_ the global optimum of a given function. Specifically, it is a metaheuristic to approximate global optimization in a large search space for an optimization problem. For large numbers of local optima, SA can find the global optimum.
  - simulated annealing / hill climbing ::@:: Instead of choosing the best successor, a random successor is chosen. If has a higher \(or equal\) value, the move is executed. Otherwise, the move is executed with a probability that decreases as the algorithm progresses. If not executed, randomly pick another successor and repeat the above. The probability is computed from a function called the _annealing schedule_.
  - simulated annealing / naming ::@:: It comes from annealing in metallurgy, a technique involving heating and controlled cooling of a material to alter its physical properties.
- [game](../../../../game.md) ::@:: They are the _oldest, most well-studied domain_ in artificial intelligence.
  - game / motivation ::@:: They are fun. <br/> Easy to represent, rules are clear. <br/> Possible combination of move can be big, e.g., there are about 10<sup>154</sup> possible moves in chess. <br/> Like the "real world" in that decisions have to be made and time is important. <br/> Easy to determine when a program is doing well.
  - game / uncertainty ::@:: One is we do not know what the opponents do in advance. The other is we have practical time limits. To stay within the limit limits, the decision we make may be suboptimal.
  - game / characteristics ::@:: (non-)deterministic, perfect information/imperfect information, (non-)zero-sum
    - [perfect information](../../../../general/perfect%20information.md) ::@:: In [game theory](../../../../general/game%20theory.md), a [sequential game](../../../../general/sequential%20game.md) has _\(this\)_ property if each player, when making any decision, is perfectly informed of all the events that have previously occurred, including the "initialization event" of the [game](../../../../general/game.md) \(e.g. the starting hands of each player in a card game\).
    - [zero-sum game](../../../../general/zero-sum%20game.md) ::@:: It is a mathematical representation in game theory and economic theory of a situation that involves two competing entities, where the result is an advantage for one side and an equivalent loss for the other. In other words, _player one's gain is equivalent to player two's loss_, with the result that the net improvement in benefit of the game is zero.
    - deterministic game ::@:: It is a game that does not involve random choices.
    - game / characteristics / tic-tac-toe ::@:: deterministic, perfect information, zero-sum
- [tic-tac-toe](../../../../general/tic-tac-toe.md) ::@:: It is a [paper-and-pencil game](../../../../general/paper-and-pencil%20game.md) for two players who take turns marking the spaces in a three-by-three grid with _X_ or _O_. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. It is a [solved game](../../../../general/solved%20game.md), with a forced draw assuming [best play](../../../../general/best%20response.md) from both players.
- game
  - game / search problem ::@:: Many games can be formulated as a search problem. States are the game states. Initial state is the initial game state \(duh\). Actions are legal moves in the game. Goal states are terminal game states. Path cost function is the utility/payoff function \(which evaluates the goal states\), and we actually want to maximize it instead of minimizing it.
- [minimax](../../../../general/minimax.md) ::@:: It is a _recursive algorithm_ which is used to _choose an optimal move_ for a player assuming that _the other player is also playing optimally_. <p> The two players are called _maximizer_ (denoted as MAX) and _minimizer_ (denoted as MIN), and define a scoring method from the standpoint of the MAX player. The maximizer (the _AI_) tries to maximize its score while the minimizer (the _human_) tries to minimize the score of AI.
  - minimax / names ::@:: It is called "minimax" because it helps in _minimizing_ the _loss_ the other players can force us to receive. It may also be called "maxmini" if we want to _maximize_ the _gain_ that others players try to minimize.
  - minimax / steps ::@:: Construct the game tree. The initial node containing the current state is a MAX node if we are the controlling player, and MIN otherwise. The nodes alternate between MAX and MIN in increasing tree depth. MAX nodes are assigned ∞ while MIN nodes are assigned +∞. Evaluate and assign to each terminal state using a utility function (e.g. win (for me, not the controlling player given the terminal state) = <!-- +1/ -->+∞, lose = <!-- −1/ -->−∞, draw = 0). The setup is complete. <p> Using depth-first traversal, explore as far as possible, and when backtracking, update the utility of non-terminal nodes according to the MAX or MIN between the value of the current node (the node we have just backtracked to) and the just-explored child (the node we have just backtracked from). <p> Finally, make the decision either using the MAX (this is the usual case) or the MIN (evaluating the optimal decision for other players) rule.
  - minimax / deterministic ::@:: It requires determinism, otherwise we cannot make choices deterministically. <p> (Actually, strictly speaking, if we are not forced to make random choices but others are, we can still use minimax. Even if we are, we can use expected values, i.e. expectiminimax. But ignore this for exams...)
    - [expectiminimax](../../../../general/expectiminimax.md)
  - minimax / perfect information ::@:: It requires perfect information, otherwise we cannot construct the game tree. <p> If a game has probabilistic elements but the results and probabilities are still known, they are still regarded as games of perfect information (but not deterministic). <p> (Of course there are extensions of minimax to imperfect games, but ignore this for exams...)
  - minimax / zero-sum game ::@:: The original version requires zero-sum. In two-player zero-sum games, others minimizing my payoff is the same as maximizing others' own payoff. In a non-zero-sum game, this is not necessarily the case. <p> More information: "Maximin" is a term commonly used for non-zero-sum games to describe the strategy which maximizes one's own minimum payoff. In non-zero-sum games, this is _not generally the same_ as minimizing the opponent's maximum gain, nor the same as the Nash equilibrium strategy. <p> (There are extensions to more complex games, but ignore this for exams...)
  - minimax / number of states ::@:: If the game is deterministic, has perfect information, and is zero-sum, then we can apply minimax to it _theoretically_. But in _practice_, games with too many states are also not suitable (even with alpha–beta pruning). <p> A way to handle this to evaluate on the _partial_ game tree, as described below.
  - minimax / visual execution ::@:: Setup the tree as above. <p> Explore the state tree in in depth-first traversal. In DFS, backtracking is needed. Whenever a backtracking occurs, update the utility of non-terminal nodes according to the MAX or MIN between the value of the current node (the node we have just backtracked to) and the just-explored child (the node we have just backtracked from). Repeat until the entire tree is explored. <p> Finally, make the decision either using the MAX (this is the usual case) or the MIN (evaluating the optimal decision for other players) rule.
  - minimax / non-optimal play ::@:: The definition of optimal play for MAX assumes MIN plays optimally, i.e., maximizes the worst-case outcome for MAX. If _MIN does not play optimally_, MAX, if _playing optimally_, will do the same or even better, i.e. has a equal or higher payoff than that given by the minimax algorithm.
  - minimax / partial ::@:: As mentioned above, games with too many states are impractical to evaluate using the original minimax algorithm. A variant that sacrifice perfect decision \(i.e. _imperfect decision_\) for performance is presented below. <p> The game tree is now _partial_. One way to make a _partial_ tree is to limit by depth bound \(number of edges\). Also, the utility/payoff function is extended to a _heuristic evaluation function_. The function agrees with the original utility/payoff function for terminal game states, and additionally _approximates_ the utility/payoff for non-terminal game states. Its computation should also be _efficient_. Otherwise, everything remains the same.
    - minimax / partial / heuristic ::@:: A common way to construct such a function is using a _weighted linear function_, with features in a game state as inputs. Another way is to _learn_ such a function automatically from past experience using other techniques. <p> For example, the heuristic for tic-tac-toe for non-terminal game states can be the number of available winning positions \(columns, diagonals, rows\) for MAX subtracted by that for MIN.

## week 6 tutorial

- datetime: 2025-03-11T12:30:00+08:00/2025-03-11T13:20:00+08:00
- topic: constraint satisfaction problem \(CSP\)
- constraint satisfaction problem \(CSP\)
  - constraint satisfaction problem / definition
    - constraint satisfaction problem / definition / evaluation
    - constraint satisfaction problem / definition / solution
- [Sudoku](../../../../general/Sudoku.md) ::@:: It is a logic-based, combinatorial number-placement puzzle. In classic Sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contains all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.
- constraint satisfaction problem
  - constraint satisfaction problem / constructive methods
- local consistency
  - local consistency / constraint propagation
    - local consistency / constraint propagation / methods
  - local consistency / forms ::@:: arc consistency, hyper-arc consistency, path consistency
  - local consistency / arc consistency ::@:: A variable of a constraint satisfaction problem is arc consistent with another one if each of its admissible values are consistent with some admissible value of the second variable. Formally, a variable $x_{i}$ is arc consistent with another variable $x_{j}$ if, for every value $a$ in the domain of $x_{i}$ there exists a value $b$ in the domain of $x_{j}$ such that $(a,b)$ satisfies the binary constraint between $x_{i}$ and $x_{j}$. A problem is arc consistent if every variable is arc consistent with every other one.
    - local consistency / arc consistency / example ::@:: For example, consider the constraint $x<y$ where the variables range over the domain 1 to 3. Because $x$ can never be 3, there is no arc from 3 to a value in $y$ so it is safe to remove. Likewise, $y$ can never be 1, so there is no arc, therefore it can be removed.
  - local consistency / path consistency ::@:: Path consistency is a property similar to arc consistency, but considers pairs of variables instead of only one. A pair of variables is path-consistent with a third variable if each consistent evaluation of the pair can be extended to the other variable in such a way that all _binary_ constraints are satisfied. Formally, $x_{i}$ and $x_{j}$ are path consistent with $x_{k}$ if, for every pair of values $(a,b)$ that satisfies the binary constraint between $x_{i}$ and $x_{j}$, there exists a value $c$ in the domain of $x_{k}$ such that $(a,c)$ and $(b,c)$ satisfy the constraint between $x_{i}$ and $x_{k}$ and between $x_{j}$ and $x_{k}$, respectively.
- Boolean satisfiability problem
  - Boolean satisfiability problem / conjunctive normal form \(CNF\)
  - Boolean satisfiability problem / search problem ::@:: A CNF formula is given. The states are partial \(including empty and full\) assignments of variables. The initial state is the empty assignment. The goal state is an assignment that satisfies the CNF formula. The actions are assigning a Boolean to an unassigned variable. The path cost is 1 per action. <p> Setting the path cost to 1 per action means we try to find a solution that has the least number of assigned variables. The remaining unassigned variables can be assigned arbitrarily.

## week 6 lecture

- datetime: 2025-03-12T13:30:00+08:00/2025-03-12T14:50:00+08:00
- topic: game tree search
- [game tree](../../../../general/game%20tree.md) ::@:: It is a graph representing all possible game states within a sequential game that has perfect information.
  - game tree / simplification ::@:: Manually drawing a game tree is a laborious process, and is only plausible for \(very\) small games. <p> A trick is to make use of the game state symmetry to reduce the number of states drawn. Remember to note that you have omitted symmetric game states.
  - game tree / partial ::@:: As mentioned above, games with too many states are impractical to have its whole game tree generated. <p> There are several ways to deal with this. Two simple ways are DFS with depth bound or iterative deepening search \(IDDFS\). A more advanced way is _quiescence search_. <p> Typically, the utility/payoff function is extended to a _heuristic evaluation function_. The function agrees with the original utility/payoff function for terminal game states, and additionally _approximates_ the utility/payoff for non-terminal game states. Its computation should also be _efficient_. Otherwise, everything remains the same.
- [quiescence search](../../../../general/quiescence%20search.md) ::@:: It is an algorithm typically used to extend search at unstable nodes in minimax game trees in game-playing computer programs. It is an extension of the evaluation function to defer evaluation until the position is stable enough to be evaluated statically, that is, without considering the history of the position or future moves from the position. It mitigates the effect of the horizon problem.
  - quiescence search / detail ::@:: Essentially, it is DFS, but the expansion termination is decided by some criterion to distinguish _quiet_ \(_quiescence_\) positions from _volatile_ positions instead of by depth bound. <p> _Quiet_  \(_quiescence_\) positions are positions that are _unlikely_ to have large variations in the future \(unexpanded states\).
- [alpha–beta pruning](../../../../general/alpha–beta%20pruning.md) ::@:: It is a _search algorithm_ that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. It stops evaluating a move when at least one possibility has been found that proves the move to be _worse than a previously examined move_. Such moves need not be evaluated further. When applied to a standard minimax tree, it returns _the same move as minimax_ would, but prunes away branches that _cannot possibly influence_ the final decision.
  - alpha–beta pruning / idea ::@:: The algorithm maintains two values, alpha and beta, which respectively represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of. Initially, alpha is negative infinity and beta is positive infinity, i.e. both players start with their worst possible score. Whenever the maximum score that the minimizing player (i.e. the "beta" player) is assured of becomes less than the minimum score that the maximizing player (i.e., the "alpha" player) is assured of (i.e. beta < alpha), the maximizing player need not consider further descendants of this node, as they will never be reached in the actual play. <p> To summarize, it prevents ourselves from exploring branches of the game tree that are _not worth exploring_, because they will have _no effect on the final outcome_.
    - alpha–beta pruning / idea / example ::@:: To illustrate this with a real-life example, suppose somebody is playing chess, and it is their turn. Move "A" will improve the player's position (_alpha_ = score of Move "A"). The player continues to look for moves to make sure a better one hasn't been missed (exploring a new branch for the _player_). Move "B" is also a good move, but the player then realizes that it will allow the opponent to force checkmate in two moves. Thus, other outcomes from playing move B no longer need to be considered since the opponent can force a win. The maximum score that the opponent could force after move "B" is negative infinity: a loss for the player (_beta_ = score of the move for the _opponent_ checkmating). This is less than the minimum position that was previously found (_alpha_ > _beta_); move "A" does not result in a forced loss in two moves.
  - alpha–beta pruning / alpha ::@:: It represents the _minimum_ score that the _maximizing_ player is assured of. Initially, it is negative infinity (worst possible score). <p> For visual execution on a tree, given a search path from the root to the currently being visited vertex in DFS, it is the _maximum_ score among the _maximizing_ player vertices in the path, assuming the scores are _updated dynamically_ while doing DFS \(that is, nodes that have at least one children fully explored have scores, which may or may not be the final score\).
  - alpha–beta pruning / beta ::@:: It represents the _maximum_ score that the _minimizing_ player is assured of. Initially, it is positive infinity (worst possible score). <p> For visual execution on a tree, given a search path from the root to the currently being visited vertex in DFS, it is the _minimum_ score among the _minimizing_ player vertices in the path, assuming the scores are _updated dynamically_ while doing DFS \(that is, nodes that have at least one children fully explored have scores, which may or may not be the final score\).
  - alpha–beta pruning / visual execution ::@:: If you use the above visual interpretations of _alpha_ and _beta_, it will become easier. Then the algorithm works the same way as in minimax, except that every time before you decide to explore a new unexplored branch, evaluate if _alpha_ ≥ _beta_. If no, continue. Otherwise, do not explore said branch and backtrack from the current vertex now, as the remaining branches need no more exploration.
  - alpha–beta pruning / recursive execution ::@:: Assume there is a minimax function that recurses on children. Add parameters _alpha_ and _beta_ to it. <p> For the root, _alpha_ and _beta_ are their worst possible scores. Otherwise, _alpha_ and _beta_ are copied from the parent. <p> First, return the score if the current vertex is to be evaluated. If not returned, for each child, run the minimax function recursively. When it returns, update _alpha_ to be the larger value between _alpha_ and the return value if the current vertex is _maximizing_, otherwise update _beta_ to be the smaller value between _beta_ and the return value (as the current vertex is _minimizing_). Note that these updates do not update the _alpha_ or _beta_ of the parent vertex. Then check if _alpha_ ≥ _beta_. If so, return from the function now \(return value is _beta_ if _maximizing_, _alpha_ if _minimizing_\) without recursing on the remaining children (this prunes the remaining branches).
  - alpha–beta pruning / search order ::@:: Note that the branches prune away can be different depending on the search order. It is also possible that no branches are pruned away at all. <p> Assuming all nodes have the same branching factor, all leaf nodes are evaluated at the same fixed depth, and the leaf nodes have randomly distributed scores, an optimal search order reduces the branching factor from $b$ to $\sqrt b$ \(Knuth and Moore, 1975\).
  - alpha–beta pruning / advantages ::@:: It _reduces the number of explored nodes_. When one chance or _option is found at the minimum_, it _stops assessing a move_. So it helps to _improve the search procedure_ in an effective way.
  - alpha–beta pruning / disadvantages ::@:: It prunes _a large part_ of search space, but still needs to search all the way to _terminal states_. And this may not prune enough states such that the moves can be _made in a reasonable amount of time_.
  - alpha–beta pruning / extensions ::@:: We could set a _depth limit_, and then use a _heuristic evaluation function_, which estimates desirability or utility of position that _correlates_ with the actual chance of winning. But then the algorithm is _no longer guaranteed_ to find a winning strategy _if one exists_.
- [Monte Carlo method](../../../../general/Monte%20Carlo%20method.md) ::@:: a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results
- [Monte Carlo tree search](../../../../general/Monte%20Carlo%20tree%20search.md) \(MCTS\) ::@:: It is a heuristic search algorithm for some kinds of decision processes, most notably those employed in software that plays board games. In that context MCTS is used to solve the game tree.
  - Monte Carlo tree search / steps ::@:: selection → expansion → simulation → backpropagation
    - Monte Carlo tree search / steps / selection ::@:: Start from root _R_ and select successive child nodes until a leaf node _L_ is reached. The root is the current game state and a leaf is any node that has a potential child from which no simulation \(playout\) has yet been initiated. <!-- The section below says more about a way of biasing choice of child nodes that lets the game tree expand towards the most promising moves, which is the essence of Monte Carlo tree search. -->
    - Monte Carlo tree search / steps / expansion ::@:: Unless _L_ ends the game decisively \(e.g. win/loss/draw\) for either player, create one \(or more\) child nodes and choose node _C_ from one of them. Child nodes are any valid moves from the game position defined by _L_.
    - Monte Carlo tree search / steps / simulation ::@:: Complete one random playout from node _C_. This step is sometimes also called playout or rollout. A playout may be as simple as choosing [uniform random](../../../../general/discrete%20uniform%20distribution.md) moves until the game is decided \(for example in chess, the game is won, lost, or drawn\).
    - Monte Carlo tree search / steps / backpropagation ::@:: Use the result of the playout to update information in the nodes on the path from _C_ to _R_.
    - Monte Carlo tree search / steps / lecture slides ::@:: The steps given in the lecture slides are different. The above steps assumes you are evaluating a game tree starting from the current node, in order to decide the next move. The steps in the lecture slides assuming you are in a leaf node of the game tree, and then you evaluate its children to decide the next move. So in particular, the _selection_ step is missing. <p> \(The _selection_ step is skipped.\) Expand the current node \(corresponds to _expansion_\). For each child, play a large number of random games to the finish and compute the average payoffs \(values\) \(corresponds to simulation\). Play the child move that has the largest average value \(this does not directly correspond to anything above).
  - Monte Carlo tree search / average payoff ::@:: It is the expected value of a game, calculated from the simulations. <p> For example, in a zero-sum game, it is the number of wins divided by the number of simulations.
  - Monte Carlo tree search / idea ::@:: It analyzes the most promising moves in the leaf nodes of a game tree. A promising move could be a leaf node with the highest value evaluated by a _heuristic function_. <p> The simplest simulation \(playout\) is by _randomly_ playing the game until its end for a fixed number of times, starting from the leaf node child, and record the scores \(e.g. number of wins\). Choose the child with the highest score, and break ties randomly. This is applicable for games with a _finite_ number of moves and length.
  - Monte Carlo tree search / improvements ::@:: For the method itself, we could use upper confidence bound \(UCB\) instead of average payoff to calculate the score a child. <p> For combining with other methods, we could use minimax with alpha–beta pruning up to a depth, and then Monte Carlo tree search is used to _selectively_ search promising nodes, or as a _heuristic function_. We could also make use of domain knowledge \(knowledge about the game that does not apply in general\) to combine it with other learning techniques.

## week 6 lecture 2

- datetime: 2025-03-14T13:30:00+08:00/2025-03-14T14:50:00+08:00
- topic: game tree search, Markov decision process \(MDP\)
- Monte Carlo tree search
  - Monte Carlo tree search / upper confidence bound \(UCB\) ::@:: The formula is $${\frac {w_{i} }{n_{i} } }+c{\sqrt {\frac {\ln N_{i} }{n_{i} } } } \,.$$ In this formula: <p> - _w_<sub>_i_</sub> stands for the number of wins for the node considered after the _i_-th move <br/> - _n_<sub>_i_</sub> stands for the number of simulations for the node considered after the _i_-th move <br/> - _N_<sub>_i_</sub> stands for the total number of simulations after the _i_-th move run by the parent node of the one considered <br/> - _c_ is the exploration parameter—theoretically equal to √2; in practice usually chosen empirically <p> \(__this course__: In the lecture slides, $\frac {w_i} {n_i}$ is replaced by $\mu_i$, which is the _average payoff_. $N_i$ is the number of simulations run under the parent node.\)
    - Monte Carlo tree search / upper confidence bound / interpretation ::@:: The first component of the formula above corresponds to exploitation; it is high for moves with high average win ratio. The second component corresponds to exploration; it is high for moves with few simulations.
  - Monte Carlo tree search / examples ::@:: checker: Chinook \(Schaeffer _et al._\) became the world champion in 1994. <br/> chess: Deep Blue \(Benjamin, Tan, _et al._\) defeated the world champion Gary Kasparov on 1997-05-11. <br/> Go: AlphaGo \(Silver _et al._\) defeated a top-level player in 2016.
- [Markov decision process](../../../../general/Markov%20decision%20process.md) \(MDP\) ::@:: It is a model for sequential decision making when outcomes are uncertain.
  - Markov decision process / motivation ::@:: The above algorithms consider deterministic actions. What if the actions are nondeterministic, i.e. involving chances? This nondeterminism comes from, e.g. one-shot decisions \(cannot undo\) that have random outcomes, resource constraints \(e.g. money, time, etc.\), uncertainty about the environment \(you could not always _predict_ the exact state after you have performed an action\), etc.
- search problem
  - search problem / elements
- Markov decision process
  - Markov decision process / vs. search problem ::@:: Recall the elements of a search problem. A MDP differs from it in that the actions \(successor function\) are nondeterministic, and becomes a _probability distribution function_ of reaching a certain state given a starting state. The path cost function becomes a _reward function_ \(becomes higher is better instead of lower\). Additionally, a discount factor $\gamma$ between 0 and 1 \(inclusive\) is added.
  - Markov decision process / transition probability ::@:: $T(s, a, s')$ gives the probability of reaching the ending state $s'$ given the action $a$ is performed when in the starting state $s$. <p> A possible successor $s'$ of a state $s$ has $T(s, a, s') > 0$. For a fixed starting state $s$ and action $a$, it is a _probability distribution function_ over the ending states, so we have $\sum_{s'} T(s, a, s') = 1$ for all $s, a$.
  - Markov decision process / reward function ::@:: $\operatorname{reward}(s, a, s')$ gives the reward for reaching the ending state $s'$ by taking the action $a$ when in the starting state $s$.
  - Markov decision process / policy function ::@:: It is a \(potentially probabilistic\) mapping from state space \($S$\) to action space \($A$\). \(__this course__: Ignore the potentially probabilistic nature, and thus it is $\pi: S \to A$.\) <p> It maps the current state to an action, which is the action that we will then take.
  - Markov decision process / run ::@:: A way to express a run of a MDP is: $$\text{state, action, reward, state, action, reward, state, ..., state} \,.$$ <p> For a typical MDP, there are many possible runs, usually infinite.
  - Markov decision process / optimization objective ::@:: The reward of a run is easily calculated. The formula is simply the expression in the expected value operator below. Note that the first reward obtained is not discounted, i.e. multiplied by $\gamma^0 = 1$. <p> But there are many possible runs for a typical MDP. The objective is to choose a policy $\pi$ that will maximize some cumulative function of the random rewards, typically the expected discounted sum over a potentially infinite horizon <p> &emsp; $E\left[\sum _{t=0}^{\infty }{\gamma ^{t}R_{a_{t} }(s_{t},s_{t+1})}\right]$ \(where we choose $a_{t}=\pi (s_{t})$, i.e. actions given by the policy\). And the expectation is taken over $s_{t+1}\sim P_{a_{t} }(s_{t},s_{t+1})$ <p> where $\ \gamma \ {}$ is the discount factor satisfying $0\leq \ \gamma \ \leq \ 1$.
  - Markov decision process / discount factor ::@:: $\ \gamma \ {}$ a discount factor satisfying $0\leq \ \gamma \ \leq \ 1$, which is usually close to $1$ \(for example, $\gamma =1/(1+r)$ for some discount rate $r$\). A lower discount factor motivates the decision maker to favor taking actions early, rather than postpone them indefinitely.

## week 7 tutorial

- datetime: 2025-03-18T12:30:00+08:00/2025-03-18T13:20:00+08:00
- topic: minimax, alpha–beta pruning
- minimax
- game
  - game / uncertainty
  - game / characteristics
    - perfect information
    - zero-sum game
    - deterministic game
- minimax
  - minimax / visual execution
  - minimax / recursive execution
- alpha–beta pruning
  - alpha–beta pruning / idea
  - alpha–beta pruning / alpha
  - alpha–beta pruning / beta
  - alpha–beta pruning / visual execution
  - alpha–beta pruning / recursive execution
  - alpha–beta pruning / search order

## week 7 lecture

- datetime: 2025-03-19T13:30:00+08:00/2025-03-19T14:50:00+08:00
- topic: Markov decision process \(MDP\)
- Markov decision process
  - Markov decision process / value function ::@:: Given a policy, the value function gives the expected utility starting from a certain state. It can be defined using recursion \(notice $V_\pi$ appears in its own definition\): $$V_\pi(s) = \begin{cases} 0 & \text{if }s\text{ is an ending state} \\ \sum_{s'} T(s, \pi(s), s') (R(s, \pi(s), s') + \gamma V_\pi(s') ) & \text{otherwise} \end{cases} \,,$$ where $\sum_{s'}$ sums over all states. <p> Intuitively, after a state transition due to an action, the future expected utility only depends on the current state, but not past state. So recursion can be used.
    - Markov decision process / value function / Q-value ::@:: \(__this course__: For some reason, it mentions Q-value not in the context of Q-learning, but in the context of evaluating the value function...\) <p> Q-value is the expected utility of doing $a$ in $s$, and then following the policy $\pi$: $$Q_\pi(s, a) = \sum_{s'} T(s, a, s') (R(s, a, s') + \gamma V_\pi(s') ) \,.$$ So the value function can be rewritten as: $$V_\pi(s) = \begin{cases} 0 & \text{if }s\text{ is an ending state} \\ Q_\pi(s, \pi(a)) & \text{otherwise} \,. \end{cases}$$ <p> Using this, for very simple MDPs, we can get a closed solution for the value function.
    - Markov decision process / value function / iteration ::@:: What if a closed solution for the value function does not exist or is difficult to find? <p> The idea is we initialize the value function to all 0s. Then we use the recursive definition to get a new value function in terms of the old value function. Repeat this until max iteration or some termination condition, e.g. the new value function does not differ too much from the old value function. <p> Formally, each iteration involves: $$V_\pi^{t + 1}(s) = \sum_{s'} T(s, \pi(s), s') (R(s, \pi(s), s') + \gamma V_\pi^t(s')) \,,$$ where the superscript denote the value function at iteration $t$. The starting values are $$V_\pi^0(s) = 0 \,.$$
    - Markov decision process / value function / optimal ::@:: Given a starting state, an _optimal_ policy is one that _maximizes_ the value function evaluated at the starting state. The value function is said to be an _optimal_ value function. <p> Two popular methods to find the optimal value function are policy iteration and value iteration.
      - Markov decision process / value function / optimal / note ::@:: \(__this course__: __Important__. The lecture slides uses that an optimal policy is one that maximizes the value function _for all_ starting states. But this is not exactly correct: A MDP can have multiple distinct optimal policies, and is a function of the starting state. Indeed, an optimal policy as defined in the lecture slides may not even exist. <p> For optimal value function, the definition is the same: Given a starting state, an optimal value function is one has the maximum value evaluated at the starting state.\)
  - Markov decision process / policy iteration ::@:: The idea is we start with a random policy. Then we improve the policy \(_policy improvement_\) until max iteration or some termination condition, e.g. the policy stops changing. <p> We initialize the policy function randomly. We initialize the value function to all 0s. Then while the policy function has changed in the last iteration \(for the first iteration, this is considered true\), iterate: update the value function, then update the policy function using Q-values _calculated_ from the value function.
    - Markov decision process / policy iteration / policy improvement ::@:: Given we have a \(not necessarily optimal\) policy $\pi$ and a \(not necessarily optimal\) value function $V_\pi(s)$, we can improve the policy. <p> Calculate the Q-value for each combination of state and action. Then for each state, choose the action that has the highest Q-value. This is the new policy function. Mathematically, this is $$\pi_{\text{new} }(s) = \operatorname{argmax}_{a \in \operatorname{actions}(s)} Q(s, a) \,.$$
    - Markov decision process / policy iteration / monotonicity ::@:: The sequence of value functions obtained is monotonically increasing. The sequence of action functions is monotonically improving \(i.e. it cannot regress\).

## week 7 lecture 2

- datetime: 2025-03-21T13:30:00+08:00/2025-03-21T14:50:00+08:00
- topic: Markov decision process \(MDP\), reinforcement learning
- Markov decision process
  - Markov decision process / value iteration ::@:: \(Bellman 1957\) In policy iteration, we update the value function and policy function alternatively. What if we combine these together into one step? This is value iteration. <p> We initialize the value function to all 0s. Repeat this until max iteration or some termination condition, e.g. the new value function does not differ too much from the old value function: update the value function as follows: $$V_{\text{opt} }^{t + 1}(s) = \max_{a \in \operatorname{action}(s)} \sum_{s'} T(s, a, s') (R(s, a, s') + \gamma V_{\text{opt} }^t(s') ) \,.$$ That is, it is similar to finding the value function for a fixed policy using iteration, but this time the action used is not from a fixed policy, but instead maximizes the value function.
    - Markov decision process / value iteration / policy extraction ::@:: Finally, the policy function can be extracted \(_policy extraction_) from the almost optimal value function, which is simply finding the action that maximizes the expected utility for each state. <p> Note that an almost optimal value function can yield the same policy function as an optimal value function \(given the actions are discrete\).
  - Markov decision process / convergence ::@:: If either the MDP is acyclic \(directed acyclic graph\) or the discount factor is less than 1, then both policy iteration and value iteration converges to an optimal solution. <p> The intuition is that if the MDP is acyclic, each run is finite. For if the discount factor is less than 1, it is harder to explain, but consider that a geometric sum converges if the factor is less than 1. <p> \(__this course__: Proof is not required here.\)
  - Markov decision process / policy iteration
    - Markov decision process / policy iteration / vs. value iteration ::@:: Policy iteration has the advantage that there is a definite stopping condition: when the array $\pi$ does not change in the course of applying step 1 to all states, the algorithm is completed. <p> Policy iteration is usually slower than value iteration for a large number of possible states. \(__this course__: __Important__. Policy iteration is faster?!?\)
      - Markov decision process / policy iteration / vs. value iteration / note ::@:: \(__this course__: <p> initialization: random policy vs. 0 <br/> update: policy \(explicit\) vs. value \(implicit\) <br/> phases: 2 \(evaluate, improve\) vs. 1 <br/> convergence: both converges to an optimal solution <br/> \# iterations: less vs. more <br/> speed: faster vs. slower\)
- reinforcement learning
  - reinforcement learning / motivation ::@:: In MDPs, the environment or the model is fully specified, only that action outcomes are random. That is, we know the actions, reward functions, states, and transition probabilities. <p> But it is possible that not all of the above information is available, or too difficult to represent. <p> Reinforcement learning is about learning using reward signals.
  - reinforcement learning / considerations ::@:: Assume we know the states and actions available in a state. We want to learn a policy that maximizes the rewards.
  - reinforcement learning / framework ::@:: The agent is in a state. The agent acts. The agent observes the updated state and the rewards. The agent updates itself \(its parameters\) to better maximize the rewards.
  - reinforcement learning / tradeoff ::@:: Reinforcement learning is about balancing _exploration_ and _exploitation_. Unless we have a perfect model of the world, both needs to be done. <p> Exploration tries to improve the agent itself to get better long-term benefits, at the cost of getting less rewards in the near future. Exploitation tries to get the most rewards, preferably in the near future, but this may lead to the agent missing out on actions that gives more rewards in the long-term.
  - reinforcement learning / ε-greedy ::@:: $0<\varepsilon <1$ is a parameter controlling the amount of exploration vs. exploitation. With probability $1-\varepsilon$, exploitation is chosen, and the agent chooses the action that it believes has the best long-term effect \(ties between actions are broken uniformly at random\). Alternatively, with probability $\varepsilon$, exploration is chosen, and the action is chosen uniformly at random. $\varepsilon$ is usually a fixed parameter but can be adjusted either according to a schedule \(making the agent explore progressively less\), or adaptively based on heuristics. <p> mnemonics: $\varepsilon$ is the probability of exploration because $\varepsilon$ usually stands for a small number and the probability of exploration should be small.
    - reinforcement learning / ε-greedy / Q-value ::@:: In terms of Q-value, this can be expressed as: $$\pi(s) = \begin{cases} \operatorname{argmax}_{a \in \operatorname{action}(s)} \hat Q(s, a) & \text{with probability }1 - \varepsilon \\ \text{random }a \in \operatorname{action}(s) & \text{with probability }\varepsilon \,, \end{cases}$$ where $\hat Q(s, a)$ is the current _estimated_ Q-value.

## week 8 tutorial

- datetime: 2025-03-25T12:30:00+08:00/2025-03-25T13:20:00+08:00, PT50M
- topic: midterm Q&A

## week 8 lecture

- datetime: 2025-03-26T13:30:00+08:00/2025-03-26T14:50:00+08:00, PT1H20M
- topic: reinforcement learning
- reinforcement learning
  - reinforcement learning / key algorithms ::@:: Monte Carlo, Q-learning, Q-values, deep Q-learning, policy gradient, temporal difference, etc.
    - reinforcement learning / key algorithms / representation ::@:: approximation: efficiently approximate the observed values by functions, e.g. deep Q-learning, policy gradient <br/> tabular representation: store the observed values in tables, e.g. Monte Carlo, Q-values, temporal difference, Q-learning
  - reinforcement learning / Monte Carlo ::@:: Given a sample run $D = (s_1, a_1, r_1, s_2, a_2, r_2, \ldots)$, estimate the sample transition probabilities and reward functions. In particular, we have $$\begin{aligned} \hat T(s, a, s') & = \frac {\#(s, a, s') \in D} {\sum_{s''} \#(s, a, s'') \in D} \\ R(s, a, s') & = \operatorname E\set{r : (s, a, r, s') \in D} \\ R(s, a) & = \operatorname E\set{r: (s, a, r) \in D} \,, \end{aligned}$$ which you should be able to infer yourself.
  - reinforcement learning / Q-values ::@:: Given a sample run $D = (s_1, a_1, r_1, s_2, a_2, r_2, \ldots)$, estimate the Q-values $Q_\pi(s, a)$ for each combination of state $s$ and action $a$. <p> We can derive the utility at state $s_t$, where $t$ is time: $$u_t = r_t + \gamma r_{t + 1} + \gamma^2 r_{t + 2} + \cdots \,,$$ where $\gamma$ is the discount factor. Then, the Q-value $Q_\pi(s, a)$ is estimated as $$Q_\pi(s, a) = \operatorname E\set{u_t : (s_t, a_t) = (s, a)} \,,$$ that is, the average utility at time $t$ where the state is $s$ and you take action $a$.
  - reinforcement learning / temporal difference ::@:: It refers to a class of model-free reinforcement learning methods which learn by bootstrapping from the current estimate of the value function. These methods sample from the environment, like Monte Carlo methods, and perform updates based on current estimates, like dynamic programming methods. <p> This method is in contrast to Monte Carlo methods. <p> examples: Q-learning
  - reinforcement learning / Q-learning ::@:: Initialize Q-values $\hat Q(s, a)$ for each combination of state $s$ and $a$ to zero. <p> An agent at state $s$ performs an action $a$, recevies reward $r$, and reaches state $s'$, i.e. $(s, a, r, s')$. The original new value of Q-value is thus: $$\hat Q'(s, a) = r + \gamma \hat V(s') \,,$$ where $\hat V(s') = \max_a \hat Q(s', a)$ is the highest possible Q-value for state $s'$. <p> The method of _temporal difference_ additionally requires a _learning rate_ $\mu \in [0, 1]$ to control how much the new value replaces the old value: $$\hat Q_{\text{new} }(s, a) = (1 - \mu) \hat Q(s, a) + \mu \hat Q'(s, a) = (1 - \mu) \hat Q(s, a) + \mu(r + \gamma \hat V(s')) \,.$$
  - reinforcement learning / deep Q-learning ::@:: When there are many states, Q-learning may not be efficient enough at estimating the real Q-values. A deep neural network is used to represent the Q-values as a Q-function. <p> The DeepMind system used a deep convolutional neural network, with layers of tiled convolutional filters to mimic the effects of receptive fields. \(<https://arxiv.org/pdf/1312.5602.pdf>\)
  - reinfrocement learning / policy gradient ::@:: [Gradient](../../../../general/gradient.md)-based methods \(_policy gradient methods_\) start with a mapping from a finite-dimensional \(parameter\) space to the space of policies: given the parameter vector $\theta$, let $\pi _{\theta }$ denote the policy associated to $\theta$. Defining the performance function by $\rho (\theta )=\rho ^{\pi _{\theta } }$ under mild conditions this function will be differentiable as a function of the parameter vector $\theta$. If the gradient of $\rho$ was known, one could use [gradient ascent](../../../../general/gradient%20descent.md).
    - reinforcement learning / policy gradient / approximation ::@:: Since an analytic expression for the gradient is not available, only a noisy estimate is available. Such an estimate can be constructed in many ways, giving rise to algorithms such as Williams's REINFORCE method \(which is known as the likelihood ratio method in the [simulation-based optimization](../../../../general/simulation-based%20optimization.md) literature\).

## midterm examination

- datetime: 2025-03-26T19:30:00+08:00/2025-03-26T21:30:00+08:00, PT2H
- venue: Lecture Theater B
- format
  - calculator: yes
  - cheatsheet: no
  - referencing: closed book, closed notes
  - provided: select lecture slides
  - questions: long questions ×8
- grades: 98/100 → 98/100
  - statistics
    - timestamps: 2025-04-07T15:40+08:00 → 2025-04-10T22+08:00
    - mean: 69.58 \(provided: 69.56\) → 69.79
    - standard deviation: ? \(provided: 22.158\) → ?
    - low: 0
    - lower quartile: 60.5 → 60.88
    - median: 76 → 76
    - upper quartile: 84 → 84.25
    - high: 99 → 99
    - distribution: ? → ?
    - data: ? → ?
- report
  - breadth-first search, depth-first search, A\* search \(0\) ::@:: Take note of how states are deduplicated. In the exam, BFS and DFS deduplicates _generated_ states, while A\* search deduplicates _visited_/_expanded_ states \(wording: "ancestors"\). <p> It turns out it is very easy to get this wrong if you try to run the algorithm by hand... For BFS and DFS, it is easy to get the depth wrong, since the depth is based on _generation_ instead of _expansion_. For A\* search, it is troublesome in general, since the same state may be generated multiple times with different _g_ and thus _f_ values, so these generated states are considered distinct.
  - depth-first search \(–1\) ::@:: Apparently, when expanding a node, the lecture slides generate a single unvisited child instead of generating all children at a time.
  - DPLL algorithm \(–1\) ::@:: Yeah, you need to follow the exact checking order on the lecture slides...
- check
  - datetime: 2025-04-10T19:00:00+08:00/2025-04-10T20:30:00+08:00, PT1H30M
  - venue: Room 4621, Academic Building
  - report: \(none\)

> __<big>Midterm Information and Past Midterm Exam Papers</big>__
>
> <big>Midterm Information</big>
>
> COMP3211 midterm exam will be held __on March 26 \(Wed\), from 7:30pm to 9:30pm, in LTB__. The special arrangement exam venue for those with time conflicts will be informed via email in a few days.
>
> - The midterm coverage is from the beginning to Page 30 \(including\) of _Lecture 6: MDP and Reinforcement Learning_, everything in the lecture notes and the first two assignments.
> - The exam is closed-book. No cheat sheet is allowed.
> - Calculators are allowed.
> - Written programming/coding won't be tested in the exam.
>
> <big>Midterm Q&A Sessions</big>
>
> The tutorials on March 21 \(Fri\) and March 25 \(Tue\) will be midterm Q&A sessions. No new materials will be conducted. You can feel free to go to the Q&A sessions if you have any question regarding the course contents.
>
> <big>Past Midterm Exam Papers</big>
>
> 23-midterm.pdf, 20-midterm.pdf

## week 8 lecture 2

- datetime: 2025-03-28T13:30:00+08:00/2025-03-28T14:50:00+08:00, PT1H20M
- topic: game theory
- [multi-agent system](../../../../general/multi-agent%20system.md) \(MAS\) ::@:: It is a computerized system composed of multiple interacting intelligent agents.
  - multi-agent system / issues ::@:: communication, cooperation, reaction \(facing adversity\), etc.
  - multi-agent system / examples ::@:: chess, contract bridge, market mechanism, most sport games, resource allocation, tic-tac-toe
- [game theory](../../../../general/game%20theory.md) ::@:: It is the study of [mathematical models](../../../../general/mathematical%20model.md) of strategic interactions. <p> It studies players (decision makers), strategies (players' complete plan of actions), and payoffs (outcomes, which can be rewards or punishments). Usually there are two players, but any number of players can be analyzed.
  - game theory / normal form ::@:: They are the simplest games studied in game theory and also most fundamental ones. \(To be defined later...\)
- [preference](../../../../general/preference%20(economics).md) ::@:: It refers to an order by which an agent, while in search of an "optimal choice", ranks alternatives based on their respective utility.
  - preference / properties ::@:: completeness, continuity, decomposability, monotonicity, substituability, transitivity
    - preference / properties / completeness ::@:: Every pair of two bundles is comparable by ≽. Either _A_ ≽ _B_, _B_ ≽ _A_, or both.
    - preference / properties / transitivty ::@:: _A_ ≽ _B_ and _B_ ≽ _C_ implies _A_ ≽ _C_.
    - preference / properties / substituability ::@:: In a bundle _A_, there may be multiple \(repeated\) elements. The desirability of an element is not affected by the presence or absence of other elements.
    - preference / properties / decomposability ::@:: The set of bundles _O_ can be decomposed into two sets _O_<sub>1</sub> and _O_<sub>2</sub>. The most preferred option of _O_ is either that in _O_<sub>1</sub> or _O_<sub>2</sub>.  
    - preference / properties / monotonicity ::@:: Comparing two bundles, if an element occurs in a bundle _A_ more times than the other bundle _B_, and no less for other elements, then _A_ ≽ _B_.
    - preference / properties / continuity ::@:: If _A_ ≽ _B_, and _C_ is sufficiently close to _A_, then _C_ ≽ _B_.
  - preference / utility function ::@:: \(von Neumann and Morgenstern, 1944\) If a preference relation ≽ satisfies 6 properties:  completeness, continuity, decomposability, monotonicity, substituability, transitivity, then: <p> We can map the bundles to a real number in \[0, 1\]. This function can be considered a _utility function_. It respects that if _A_ ≽ _B_, then _u_(_A_) ≥ _u_(_B_). Further, the utility of a lottery of bundles is simply the weighted sum of the bundle utilities, weighted by their probabilities.
- [normal-form game](../../../../general/normal-form%20game.md) ::@:: It is a description of a _game_. Unlike [extensive form](../../../../general/extensive-form%20game.md), normal-form representations are not [graphical](../../../../general/graph%20(discrete%20mathematics).md) _per se_, but rather represent the game by way of a [matrix](../../../../general/matrix%20(mathematics).md).
  - normal-form game / formal definition ::@:: The game has _n_ players. Each player has their own set of actions _A_<sub>_i_</sub>. Each player also has their own utility function _u_<sub>_i_</sub>, which maps from the Cartesian product of all sets of actions to a real number. <p> This is because the utility for a player also depends on the actions of other players.
  - normal-form game / matrix ::@:: For _n_ players, we can represent the _n_ utilities for _n_ players in a _n_-dimensional matrix. Each dimension corresponds to the set of actions for a player.
- [prisoners' dilemma](../../../../general/prisoners'%20dilemma.md) ::@:: It is a [game theory](../../../../general/game%20theory.md) thought experiment involving two [rational agents](../../../../general/rational%20agent.md), each of whom can either cooperate for mutual benefit or betray their partner \("defect"\) for individual gain. The dilemma arises from the fact that while defecting is rational for each agent, cooperation yields a higher payoff for each.
- [coordination game](../../../../general/coordination%20game.md) ::@:: It is a type of simultaneous game found in game theory. It describes the situation where a player will earn a higher payoff when they select the same course of action as another player. The game is not one of pure conflict, which results in multiple pure strategy Nash equilibria in which players choose matching strategies.
- [matching pennies](../../../../general/matching%20pennies.md) ::@:: __Matching pennies__ is a [non-cooperative game](../../../../general/non-cooperative%20game%20theory.md) studied in [game theory](../../../../general/game%20theory.md). It is played between two players, Even and Odd. Each player has a [penny](../../../../general/penny.md) and must secretly turn the penny to heads or tails. The players then reveal their choices simultaneously. If the pennies match \(both heads or both tails\), then Even wins and keeps both pennies. If the pennies do not match \(one heads and one tails\), then Odd wins and keeps both pennies.
- [Nash equilibrium](../../../../general/Nash%20equilibrium.md) ::@:: In [game theory](../../../../general/game%20theory.md), it is the most commonly-used [solution concept](../../../../general/solution%20concept.md) for [non-cooperative games](../../../../general/non-cooperative%20game%20theory.md). It is a situation where no player could gain by changing their own strategy \(holding all other players' strategies fixed\). <p> If each player has chosen a [strategy](../../../../general/strategy%20(game%20theory).md) – an action plan based on what has happened so far in the game – and no one can increase one's own expected payoff by changing one's strategy while the other players keep theirs unchanged, then the current set of strategy choices constitutes _\(this\)_. <p> Note that the strategy may be pure (one could also considered pure as a degenerate form of mixed) or mixed.
  - Nash equilibrium / number ::@:: There may be one, multiple, or no _pure_ Nash equilibria. <p> Under some conditions, a _possibly mixed_ Nash equilibrium must exist.
- prisoners' dilemma
  - prisoners' dilemma / Nash equilibrium ::@:: Both prisoners confessing \(which is worse than both prisoners denying for both prisoners\) is the unique Nash equilibrium.
- coordination game
  - coordination game / Nash equilibrium ::@:: Both players doing the same thing, for which there are two profiles, are the two Nash equilibra.

## week 9 tutorial

- datetime: 2025-04-01T12:30:00+08:00/2025-04-01T13:20:00+08:00, PT50M
- status: unscheduled, midterm break

## week 9 lecture

- datetime: 2025-04-02T13:30:00+08:00/2025-04-02T14:50:00+08:00, PT1H20M
- status: unscheduled, midterm break

## week 9 lecture 2

- datetime: 2025-04-04T13:30:00+08:00/2025-04-04T14:50:00+08:00, PT1H20M
- status: unscheduled, midterm break

## final examination

## aftermath

### total
