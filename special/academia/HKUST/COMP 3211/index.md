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
  - objectives ::@:: appreciate AI problem solving; learn fundamental AI algorithm; understand AI challenges and goals <!--SR:!2025-03-03,16,290!2025-03-01,14,290-->
  - course intended learning outcomes (CILOs) ::@:: appreciate cutting edge AI research; identify AI fundamental concepts and techniques; understand and apply state space search techniques <!--SR:!2025-03-02,15,290!2025-02-25,10,270-->
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
- topic: introduction
- [artificial intelligence](../../../../general/artificial%20intelligence.md) (AI) ::@:: John McCarthy, one of the founders of AI — "It is the science and engineering of making intelligent machines, especially intelligent computer programs. It is related to the similar task of using computers to understand human intelligence, but AI does not have to confine itself to methods that are biologically observable." <!--SR:!2025-02-25,11,270!2025-02-25,10,270-->
  - artificial intelligence (AI) / intuition ::@:: What is it? A calculator? An operating system? A text editor? ChatGPT or DeepSeek? <!--SR:!2025-03-01,14,290!2025-03-01,14,290-->
  - artificial intelligence (AI) / motivations ::@:: forefront of computer applications; make machines do things so far that can be done by humans; in the long-term, make machines that can act, sense, and think intelligently <!--SR:!2025-03-01,14,290!2025-03-02,15,290-->
  - artificial intelligence (AI) / algorithms, techniques ::@:: heuristic search algorithms, knowledge representation languages, machine learning algorithms and reasoners, etc. <!--SR:!2025-02-25,10,270!2025-02-25,10,270-->
  - artificial intelligence (AI) / impacts ::@:: engineering, science; everyday life; humanity in general <!--SR:!2025-02-25,10,270!2025-03-03,16,290-->
  - artificial intelligence (AI) / in computer science (CS) ::@:: science and engineering of making intelligent computer programs, the frontier of computer applications; new ways to solve problems with a computer <!--SR:!2025-02-25,10,270!2025-02-25,10,270-->
  - artificial intelligence (AI) / origins ::@:: Ada Lovelace (1815–1852), Alan Turing (1912–1954) <!--SR:!2025-03-13,19,250!2025-02-25,10,270-->
    - artificial intelligence (AI) / origins / Ada Lovelace (1815–1852) ::@:: Considered as the first computer programmer. Her Note G describes an algorithm for Babbage's analytical engine to compute Bernoulli numbers. She described the analytical engine as able to do what we tell it to perform, but cannot anticipate things that we do not tell it to perform. <!--SR:!2025-02-25,11,270!2025-03-01,14,290-->
    - artificial intelligence (AI) / origins / Alan Turing (1912–1954) ::@:: Computing machinery and intelligence. _Mind_, 59:433-460, 1950. — "I propose to consider the question, 'Can machines think?' This should begin with definitions of the meaning of the terms 'machine' and 'think.'" <!--SR:!2025-02-23,9,250!2025-02-22,8,250-->
      - Turing test ::@:: A test to empirically determine whether a computer has achieved intelligence. A human questioner questions two respondents, one human, the other a computer function, whose identities are unknown to the human questioner. Using a specified format and context, the questioner interrogates the two respondents within a specific subject area. After a preset length of time or number of questions, the questioner is then asked to decide which respondent is human and which is a computer. <!--SR:!2025-03-01,14,290!2025-03-01,14,290-->
  - artificial intelligence (AI) / history
    - artificial intelligence (AI) / history / 1956 ::@:: John McCarthy coined the term "__artificial intelligence__" as the topic of the Dartmouth Conference, the first conference devoted to the subject. The conference was proposed by John McCarthy, Marvin Minsky, Nathaniel Rochester, and Claude Shannon: "2 month, 10 man study of artificial intelligence". <!--SR:!2025-02-23,9,250!2025-02-23,9,250-->
    - artificial intelligence (AI) / history / Marvel (1992) ::@:: a real-time expert system that monitors the massive stream of data from the Voyager spacecraft, handling routine tasks, and alerting the analysts to more serious problems at Jet Propulsion Laboratory (JPL) <!--SR:!2025-03-13,19,250!2025-02-25,10,270-->
    - artificial intelligence (AI) / history / Pegasus (1994) ::@:: a speech understanding program that handles airline ticket reservations <!--SR:!2025-02-25,10,270!2025-02-25,10,270-->
    - artificial intelligence (AI) / history / Gulf War ::@:: An AI planning and scheduling system employed by US military. A DARPA report said the saving from this AI system had paid back the US Government all its investment on AI during the past 20 years. <!--SR:!2025-03-01,14,290!2025-03-02,15,290-->
    - artificial intelligence (AI) / history / older AIs & misc ::@:: Deep Blue (1997), IBM Watson (2011), AlphaFold (2020) <!--SR:!2025-02-22,8,250!2025-02-25,10,270-->
    - artificial intelligence (AI) / history / playing Go ::@:: AlphaGo (2016), AlphaGo Zero (2017) <!--SR:!2025-02-25,11,270!2025-03-01,14,290-->
    - artificial intelligence (AI) / history / GPT ::@:: GPT-3 (2020), ChatGPT (2022), GPT4 (2023), GPT4o (2024) <!--SR:!2025-02-25,11,270!2025-02-25,10,270-->
    - artificial intelligence (AI) / history / chatbots ::@:: ELIZA (1963, Weizenbaum; a computer psychotherapist) <br/> BlenderBot 3 (2022, Meta; letdown) <br/> AI Test Kitchen (2022, Google; announced only) <br/> ChatGPT (2022, OpenAI; breakthrough) <!--SR:!2025-02-25,10,270!2025-02-25,10,270-->
  - artificial intelligence (AI) / brittleness ::@:: Current AI systems are still brittle. Examples include hallucinations, object recognition, sensitivity to disturbance, etc. <!--SR:!2025-02-25,10,270!2025-02-25,10,270-->
- [hallucination](../../../../general/hallucination%20(artificial%20intelligence).md) ::@:: A response generated by AI that contains false or misleading information presented as fact, e.g. false negatives, false positives, incorrect predictions. It is associated with unjustified responses or beliefs rather than perceptual experiences. <!--SR:!2025-02-25,10,270!2025-02-25,10,270-->
  - hallucination / causes ::@:: These errors can be caused by a variety of factors, including data biases, incorrect model assumptions, insufficient training data, etc. <!--SR:!2025-03-01,14,290!2025-03-01,14,290-->
  - hallucination / examples ::@:: DALL-E 2 or Midjourney unable to create the image you want because the AI does not understand your desired context. <!--SR:!2025-02-25,10,270!2025-02-25,10,270-->
- [model collapse](../../../../general/model%20collapse.md) ::@:: It is a phenomenon where machine learning models gradually degrade due to errors coming from uncurated training on the outputs of another model, including prior versions of itself. Such outputs are known as synthetic data. <p> A study in 2024 shows this. For example, after successive generations, nonsense text are forgotten. Biases in the dataset get amplified, e.g. forgetting obscure dog breeds exist due to under-representation in the initial dataset. <!--SR:!2025-02-25,10,270!2025-03-01,14,290-->

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
- [intelligent agent](../../../../general/intelligent%20agent.md) ::@:: It is an entity that perceives its environment, takes actions autonomously to achieve goals, and may improve its performance through machine learning or by acquiring knowledge. <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
  - intelligent agent / features ::@:: can perceive, can perform actions, has an objective/goal <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
  - intelligent agent / learning objectives (in this course) ::@:: stimulus-response agent (stateless), then add states <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
  - intelligent agent / control ::@:: e.g. designed vs. evolved/learned, genetic algorithms, neural networks, rules <!--SR:!2025-02-25,4,293!2025-02-24,4,303-->
  - intelligent agent / stimulus-response agent ::@:: Stateless machines that reacts to _immediate_ stimulus from the environment. <!--SR:!2025-02-25,4,293!2025-02-24,4,303-->
    - intelligent agent / stimulus-response agent / example ::@:: actions: up/down/left/right (cannot go into walls) <br/> environment: an enclosed 2D grid with walls <br/> objective: follow the boundary of the first obstacle met <br/> perceptions: 8 sensors for 8 adjacent cells, each testing if the corresponding cell is occupied <br/> policy: an algorithm to control the robot <!--SR:!2025-02-25,4,293!2025-02-24,4,303-->
- [perceptron](../../../../general/perceptron.md)
  - perceptron / alias ::@:: threshold logical unit (TLU) <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
  - perceptron / supervised learning ::@:: It requires a training dataset. Each data in the dataset consists of _n_ _inputs_ as a _n_-dimensional vector and a _label_ (e.g. desired output). <p> Then, the task is computing a function that computes a "good" label from arbitrary _n_ inputs. This usually means agreeing with the training dataset's labels as much as possible (accuracy metric). <p> Here, we consider using a threshold linear unit (TLU; a.k.a perceptron) to learn the function. <!--SR:!2025-02-23,3,283!2025-02-25,4,293-->
  - [perceptron](../../../../general/perceptron.md) / computation ::@:: Given a data vector $\mathbf x$; and weights $\mathbf w$, the bias $\theta$, and the activation function $f$ of a perceptron, the result is computed by: $$y = f(\mathbf x \cdot \mathbf w + \theta) \,.$$ <p> Given $n$ row data vectors vertically stacked as a matrix $\mathbf X$, the $n$ results as a column vector is computed by: $$\mathbf y = f\left(\mathbf X \mathbf w + \mathbf 1 \theta \right) \,.$$ <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
    - perceptron / computation / activation function ::@:: $$f(u) = \begin{cases} 1 & \text{if }u \ge \theta \\ 0 & \text{if }u < \theta \end{cases}$$ <p> Usually, the threshold _θ_ is chosen to be 0. This is because we can always add to a perceptron, an new input that is always 1, and its weight set to the negation of the original threshold. <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
  - perceptron / Boolean functions ::@:: A function whose inputs are Booleans (0: false, 1: true) and the output is also a Boolean (0: false, 1: true). <p> _Linearly separable_ functions can be _learnt_ by a perceptron. But not all such functions are linearly separable, e.g. $x_1 \overline {x_2} + \overline {x_1} x_2$ (($x_1$ AND NOT $x_2$) OR (NOT $x_1$ AND $x_2$)). <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
  - [perceptron § steps](../../../../general/perceptron.md#steps)
    - [perceptron § steps](../../../../general/perceptron.md#steps) / initialization ::@:: Initialize the weights arbitrarily. Weights may be initialized to 0 or small random values. <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
    - [perceptron § steps](../../../../general/perceptron.md#steps) / training ::@:: For each sample $j$ in the training dataset, perform the following steps over the input $\mathbf{x}_j$ and the desired output $d_j$: <!--SR:!2025-02-25,4,293!2025-02-24,4,303-->
      - [perceptron § steps](../../../../general/perceptron.md#steps) / training / forward ::@:: Calculate the actual output: $$y_j(t) = f(\mathbf{w}(t) \cdot \mathbf{x}_j) = f(w_0(t) x_{j, 0} + w_1(t) x_{j, 1} + \cdots + w_n(t) x_{j, n})$$. <p> The dot product can be interpreted as a weighted sum. Using linear algebra, this is: $$y_j(t) = f\left(\mathbf w(t)^\intercal \mathbf x_j \right)$$ <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
      - [perceptron § steps](../../../../general/perceptron.md#steps) / training / backward ::@:: Update the weights: $$w_i(t + 1) = w_i(t) + r (d_j - y_j(t)) x_{j, i}$$ for all features $0 \le i \le n$. $r$ is the [learning rate](learning%20rate.md). <p> Since $x_{j, 0} = 1$ always, $w_0$ is effectively the bias $b$. Thus the above algorithm already includes updating the bias: $$b(t + 1) = b(t) + r(d_j - y_j(t)) \,.$$ <p> Using linear algebra, this is: $$\mathbf w(t + 1) = \mathbf w(t) + r (d_j - y_j(t)) \mathbf x_j$$ <!--SR:!2025-02-25,4,293!2025-02-23,3,283-->
    - [perceptron § steps](../../../../general/perceptron.md#steps) / termination ::@:: For [offline training](offline%20training.md), the second step may be repeated until the batch or iteration error $\frac 1 s \sum_{j = 1}^s \lvert d_j - y_j(t) \rvert$ is less than a user-defined threshold $\gamma$, or a predetermined number of batches or iterations have been completed. $s$ is the batch or iteration (not to be confused with epoch) size. <p> If the training set is linearly separable, the above (i.e. termination) will eventually happen. The number of steps depends on the dataset ordering, initial weights, learning rate. <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
  - perceptron / biological neuron ::@:: inputs: dendrites; node/computation unit: cell nucleus; outputs: axons; weights: synapses <p> TLUs are is a very simple model of biological neuron <!--SR:!2025-02-25,4,293!2025-02-24,4,303-->
- [activation function](../../../../general/activation%20function.md) ::@:: In the context of an artificial neural network, it is a function that calculates the output of the node based on its individual inputs and their weights. Nontrivial problems can be solved using only a few nodes if the above is nonlinear. <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
  - activation function / examples ::@:: ReLU (rectified linear unit), logistic (sigmoid), hyperbolic tangent (tanh) <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
- [ReLU](../../../../general/rectifier%20(neural%20networks).md) ::@:: $$f(x) = \max(0, x)$$ <!--SR:!2025-02-24,4,303!2025-02-25,4,293-->
  - ReLU / properties ::@:: continuous, linear, piecewise, differentiable almost everywhere <!--SR:!2025-02-25,4,293!2025-02-24,4,303-->
- [sigmoid](../../../../general/logistic%20function.md) ::@:: $$f(x) = \frac 1 {1 + e^{-x} }$$ <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
- [hyperbolic tangent](../../../../general/hyperbolic%20functions.md) ::@:: $$f(x) = \frac {e^{x} - e^{-x} } {e^x + e^{-x} } = \frac {e^{2x} - 1} {e^{2x} + 1}$$ <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
- [identity (activation)](../../../../general/identity%20function.md) (linear) ::@:: $$f(x) = x$$ <!--SR:!2025-02-24,4,303!2025-02-25,4,293-->
  - identity (activation) / use ::@:: For output layers, target values used to train a model with such an activation function in the output layer are typically scaled before modeling using normalization or standardization transforms. Useful for _regression problems_. <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
- [neural network](../../../../general/neural%20network%20(machine%20learning).md) ::@:: __(Artificial) neural network__ (__(A)NN__) is one of the most powerful artificial intelligence and machine learning algorithms. It can approximate any [function](../../../../general/function%20(mathematics).md) from a certain [function space](../../../../general/function%20space.md), i.e. an _universal approximator_, by the [universal approximation theorem](../../../../general/universal%20approximation%20theorem.md). <p> As the name suggests, it draws inspiration from neurons in our brain and the way they are connected. <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
  - neural network / basic structure ::@:: A directed graph whose nodes are neurons. Those with no incoming edges are inputs/sources. Those wih no outgoing edges are output/targets. The remaining are internal nodes and represent _hidden_ features. <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
  - neural network / training overview ::@:: We initialize the weights of directed edges in the graph. Then while a condition to keep updating the weights is satisfied (e.g. accuracy target, number of updates), "improve" the weights. When the condition is no longer met, training has completed. <p> Two popular ways to "improve" the weights are gradient descent and _stochastic_ gradient descent (they are different things!). <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
- intelligent agent
  - intelligent agent / basic stateless architecture ::@:: sensory input → perceptual processing → feature vector → action function (specified by the designer) → action <!--SR:!2025-02-24,4,303!2025-02-25,4,293-->
  - intelligent agent / perception ::@:: Represented using a set of $x_i$. Note that there can be illegal combinations of values for the set f $x_i$. <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
  - intelligent agent / action function ::@:: It consists of several statement in the form: If the set of $x_i$ has this combination of values, then perform a certain action. <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
- [Boolean algebra](../../../../general/Boolean%20algebra.md)
  - Boolean algebra / overview ::@:: $a$ AND $b$: $ab$ or $a \cdot b$; $a$ OR $b$: $a + b$; NOT $a$: $\overline a$ <p> AND and OR are associative and commutative. <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
- [production system](../../../../general/production%20system%20(computer%20science).md) ::@:: Essentially a giant if-else if-...-else program. <p> It is a _sequence_ (so it is ordered) in the form of: $c \to a$, where $c$ is a Boolean function and $a$ is an action. Find the first statement where $c$ evaluates to 1. Its action $a$ is the action the agent will take. <p> Commonly, we add a fallback case: $1 \to a$, where $1$ is the constant Boolean function always returning true. <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
- [genetic programming](../../../../general/genetic%20programming.md) (GP) ::@:: An evolutionary algorithm, an artificial intelligence technique mimicking natural evolution, which operates on a population of programs. <!--SR:!2025-02-25,4,293!2025-02-24,4,303-->
  - genetic programming / motivation ::@:: Human evolves to become what we are now (unless you are not human). Maybe we can adapt evolution for machine learning? Evolution has two key components: reproduction and selection (survival of the fittest). <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
  - genetic programming / overview ::@:: Decide on how to represent _legal_ programs. Define a fitness function. Select some programs as generation 0. Produce the next generation until you have a "good enough" program. <p> 3 common methods to produce next generations: copy, crossover, and mutate. <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
  - genetic programming / program representation ::@:: Typically represented as tree structures. <p> We can consider statements in a program as functions. For example, AND(a, b) stands for a AND b and IF(a, b, c) stands for if a is true, then b, otherwise c. Then a program is a composition of many functions. <p> With this function composition in mind, we convert it into a tree recursively: A constant value or a input value is represented by a leaf. A function application/call is represented by having the function itself as a node and its arguments as its children nodes. <!--SR:!2025-02-25,4,293!2025-02-24,3,273-->
  - genetic programming / initialization ::@:: full, grow, ramped half-and-half, etc. <!--SR:!2025-02-24,4,303!2025-02-25,4,293-->
    - genetic programming / initialization / grow ::@:: It creates the individuals sequentially. Every GP tree is created starting from the root, creating functional nodes with children as well as terminal nodes up to a certain depth. <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
    - genetic programming / initialization / full ::@:: It is similar to _Grow_. The difference is that all branches in a tree are of same predetermined depth. <!--SR:!2025-02-25,4,293!2025-02-24,4,303-->
    - genetic programming / initialization / ramped half-and-half ::@:: It creates a populations consisting of $md-1$ parts and a maximum depth of $md$ for its trees. The first part has a maximum depth of 2, second of 3 and so on up to the $md-1$-th part with maximum depth $md$. Half of every part is created by _Grow_, while the other part is created by _Full_. <!--SR:!2025-02-24,3,273!2025-02-25,4,293-->
  - genetic programming / selection ::@:: You need a fitness function to do so. <!--SR:!2025-02-24,4,303!2025-02-25,4,293-->
    - genetic programming / selection / example ::@:: We run the program for a certain number of steps and count the number of steps with an adjacent wall. We clamp its value between 0 and 32. We do 10 runs at random starting positions and sum the values (clamped between 0 and 320). <!--SR:!2025-02-25,4,293!2025-02-24,4,303-->
  - genetic programming / reproduction ::@:: Common methods for producing a new generation: copy, crossover, mutate. <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
    - genetic programming / reproduction / copy ::@:: Copy some programs from the previous generation. They are called the _parents_. A _tournament selection_ is used: randomly select some programs and choose the best one to copy. Other methods are possible. <p> A typical percentage of the new generation copied is 10%. <!--SR:!2025-02-25,4,293!2025-02-24,4,303-->
    - genetic programming / reproduction / crossover ::@:: From the copied _parents_, select 2 programs. A randomly chosen subtree of one parent is used to replace (including the subtree root node) a randomly selected subtree of another parent. <p> A typical percentage of the new generation crossover-ed is 90%. <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->
    - genetic programming / reproduction / mutate ::@:: From the copied _parents_, select 1 program. Replace a randomly selected subtree by a new randomly generated subtree. <p> A typical percentage of the new generation mutated is 1% (rarely used). <!--SR:!2025-02-24,4,303!2025-02-25,4,293-->
  - genetic programming / performance ::@:: It depends on the initial generation size, copy/crossover/mutate rates, and tournament selection parameters. <p> The wall-following example in the slides generates a perfect tree after 10 generations. <!--SR:!2025-02-24,4,303!2025-02-24,4,303-->
- [finite state machine](../../../../general/finite%20state%20machine.md)
  - finite state machine / motivation for agents ::@:: The above agents we have introduced are stateless: they only respond to the current stimuli. They may not be powerful enough. <p> State machines can additionally remembered their previous actions, features, and its internal states (kinda like mental states). Then its action function additionally accepts the previous actions, features, and internal states. <!--SR:!2025-02-24,4,303!2025-02-25,4,293-->
  - finite state machine / agent architecture ::@:: same as statelessness: sensory input → perceptual processing → feature vector → action function (specified by the designer) → action <br/> added for statefulness: feature vector, action → memory (stores previous features and actions) → perceptual processing <!--SR:!2025-02-24,4,303!2025-02-23,3,283-->
  - finite state machine / production system ::@:: They can be represented by production system like stateless machines. The only difference is that the Boolean function also accepts machine states as input, not just input features. <!--SR:!2025-02-25,4,293!2025-02-25,4,293-->

## assignments

## midterm examination

## final examination

## aftermath

### total
