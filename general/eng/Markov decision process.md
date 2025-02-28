---
aliases:
  - Markov decision process
  - Markov decision processes
tags:
  - flashcard/active/general/eng/Markov_decision_process
  - language/in/English
---

# Markov decision process

__Markov decision process__ \(__MDP__\), also called {@{a [stochastic dynamic program](stochastic%20dynamic%20programming.md) or stochastic control problem}@}, is {@{a model for [sequential decision making](sequential%20decision%20making.md) when [outcomes](outcome%20(probability).md) are uncertain}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-03-07,70,329!2025-03-06,69,329-->

Originating from {@{[operations research](operations%20research.md) in the 1950s}@},<sup>[\[2\]](#^ref-2)</sup><sup>[\[3\]](#^ref-3)</sup> MDPs have since {@{gained recognition in a variety of fields}@}, including {@{[ecology](ecology.md), [economics](economics.md), [healthcare](health%20care.md), [telecommunications](telecommunications.md) and [reinforcement learning](reinforcement%20learning.md)}@}.<sup>[\[4\]](#^ref-4)</sup> {@{Reinforcement learning}@} utilizes {@{the MDP framework to model the interaction between a learning agent and its environment}@}. In this framework, {@{the interaction is characterized by states, actions, and rewards}@}. The MDP framework is designed to {@{provide a simplified representation of key elements of [artificial intelligence](artificial%20intelligence.md) challenges}@}. These elements encompass {@{the understanding of [cause and effect](causality.md), the management of uncertainty and nondeterminism, and the pursuit of explicit goals}@}.<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2025-08-02,164,309!2025-03-03,67,329!2025-10-07,229,329!2025-03-11,73,329!2025-03-13,75,329!2025-09-23,217,329!2025-08-31,201,329!2025-09-12,210,329-->

The name comes from {@{its connection to [Markov chains](Markov%20chain.md)}@}, a concept developed by {@{the Russian mathematician [Andrey Markov](Andrey%20Markov.md)}@}. {@{The "Markov" in "Markov decision process"}@} refers to {@{the underlying structure of [state transitions](transition%20system.md) that still follow the [Markov property](Markov%20property.md)}@}. The process is called {@{a "decision process"}@} because {@{it involves making decisions that influence these state transitions}@}, extending the concept of a Markov chain into {@{the realm of decision-making under uncertainty}@}. <!--SR:!2025-03-11,73,329!2025-03-03,67,329!2025-03-12,74,329!2025-03-12,74,329!2025-03-14,76,329!2025-03-02,66,329!2025-03-13,75,329-->

## definition

> {@{![Example of a simple MDP with three states \(green circles\) and two actions \(orange circles\), with two rewards \(orange arrows\)](../../archives/Wikimedia%20Commons/Markov%20Decision%20Process.svg)}@}
>
> Example of {@{a simple MDP with three states \(green circles\) and two actions \(orange circles\), with two rewards \(orange arrows\)}@} <!--SR:!2025-03-09,71,329!2025-03-14,76,329-->

A Markov decision process is {@{a 4-[tuple](tuple.md) $(S,A,P_{a},R_{a})$}@}, where: <!--SR:!2025-03-14,76,329-->

- $S$ is ::@:: a [set](set%20(mathematics).md) of states called the _state space_. The state space may be discrete or continuous, like the [set of real numbers](real%20number.md). <!--SR:!2025-12-06,281,332!2025-08-25,184,312-->
- $A$ is ::@:: a set of actions called the _action space_ \(alternatively, $A_{s}$ is the set of actions available from state $s$\). As for state, this set may be discrete or continuous. <!--SR:!2025-03-04,67,312!2025-07-25,170,312-->
- $P_{a}(s,s')$ is, on an intuitive level, {@{the probability that action $a$ in state $s$ at time $t$ will lead to state $s'$ at time $t+1$}@}. In general, this probability transition is defined to {@{satisfy $\Pr(s_{t+1}\in S'\mid s_{t}=s,a_{t}=a)=\int _{S'}P_{a}(s,s')ds',$ for every $S'\subseteq S$ measurable}@}. In case {@{the state space is discrete}@}, the integral is {@{intended with respect to the counting measure}@}, so that {@{the latter simplifies as $P_{a}(s,s')=\Pr(s_{t+1}=s'\mid s_{t}=s,a_{t}=a)$}@}; In case {@{$S\subseteq \mathbb {R} ^{d}$}@}, the integral is {@{usually intended with respect to the [Lebesgue measure](Lebesgue%20measure.md)}@}.
- $R_{a}(s,s')$ is ::@:: the immediate reward \(or expected immediate reward\) received after transitioning from state $s$ to state $s'$, due to action $a$. <!--SR:!2025-11-04,255,332!2025-11-08,259,332-->

A policy function $\pi$ is ::@:: a \(potentially probabilistic\) mapping from state space \($S$\) to action space \($A$\). <!--SR:!2025-11-05,256,332!2025-11-09,260,332-->

### optimization objective

{@{The goal in a Markov decision process}@} is to {@{find a good "policy" for the decision maker}@}: a function $\pi$ that {@{specifies the action $\pi (s)$ that the decision maker will choose when in state $s$}@}. Once {@{a Markov decision process is combined with a policy in this way}@}, this {@{fixes the action for each state}@} and the resulting combination {@{behaves like a [Markov chain](Markov%20chain.md) \(since the action chosen in state $s$ is completely determined by $\pi (s)$\)}@}. <!--SR:!2025-03-05,68,329!2025-12-19,294,349!2025-03-02,66,329!2025-03-10,72,329!2025-03-03,67,329!2025-03-11,73,329-->

The objective is to {@{choose a policy $\pi$ that will maximize some cumulative function of the random rewards}@}, typically {@{the expected discounted sum over a potentially infinite horizon}@}: <p> {@{$E\left[\sum _{t=0}^{\infty }{\gamma ^{t}R_{a_{t} }(s_{t},s_{t+1})}\right]$}@} \(where we choose {@{$a_{t}=\pi (s_{t})$, i.e. actions given by the policy}@}\). And the expectation is {@{taken over $s_{t+1}\sim P_{a_{t} }(s_{t},s_{t+1})$}@} <p> where {@{$\ \gamma \ {}$ is the discount factor satisfying $0\leq \ \gamma \ \leq \ 1$,}@} which is usually {@{close to $1$ \(for example, $\gamma =1/(1+r)$ for some discount rate $r$\)}@}. {@{A lower discount factor}@} motivates {@{the decision maker to favor taking actions early, rather than postpone them indefinitely}@}. <!--SR:!2025-03-06,69,329!2025-03-13,75,329!2025-03-13,75,329!2025-03-10,72,329!2025-09-19,215,329!2025-03-14,76,329!2025-03-10,72,329!2025-03-01,65,329!2025-03-11,73,329-->

{@{Another possible, but strictly related, objective that is commonly used}@} is {@{the $H$-step return}@}. This time, instead of {@{using a discount factor $\ \gamma \ {}$}@}, the agent is {@{interested only in the first $H$ steps of the process, with each reward having the same weight}@}. <p> {@{$E\left[\sum _{t=0}^{H-1}{R_{a_{t} }(s_{t},s_{t+1})}\right]$}@} \(where we choose {@{$a_{t}=\pi (s_{t})$, i.e. actions given by the policy}@}\). And the expectation is {@{taken over $s_{t+1}\sim P_{a_{t} }(s_{t},s_{t+1})$}@} <p> where {@{$\ H\ {}$ is the time horizon}@}. Compared to {@{the previous objective}@}, the latter one is {@{more used in [Learning Theory](learning%20theory.md)}@}. <!--SR:!2025-03-10,72,329!2025-03-14,76,329!2025-03-06,69,329!2025-03-09,71,329!2025-08-03,165,309!2025-03-09,71,329!2025-03-11,73,329!2025-03-12,74,329!2025-03-07,70,329!2025-03-13,75,329-->

A policy that maximizes the function above is called an _optimal policy_ and is usually denoted $\pi ^{*}$. A particular MDP may have multiple distinct optimal policies. Because of the Markov property, it can be shown that the optimal policy is a function of the current state, as assumed above.

### simulator models

In many cases, it is difficult to represent the transition probability distributions, $P_{a}(s,s')$, explicitly. In such cases, a simulator can be used to model the MDP implicitly by providing samples from the transition distributions. One common form of implicit MDP model is an episodic environment simulator that can be started from an initial state and yields a subsequent state and reward every time it receives an action input. In this manner, trajectories of states, actions, and rewards, often called _episodes_ may be produced.

Another form of simulator is a _generative model_, a single step simulator that can generate samples of the next state and reward given any state and action.<sup>[\[5\]](#^ref-5)</sup> \(Note that this is a different meaning from the term [generative model](generative%20model.md) in the context of statistical classification.\) In [algorithms](algorithm.md) that are expressed using [pseudocode](pseudocode.md), $G$ is often used to represent a generative model. For example, the expression $s',r\gets G(s,a)$ might denote the action of sampling from the generative model where $s$ and $a$ are the current state and action, and $s'$ and $r$ are the new state and reward. Compared to an episodic simulator, a generative model has the advantage that it can yield data from any state, not only those encountered in a trajectory.

These model classes form a hierarchy of information content: an explicit model trivially yields a generative model through sampling from the distributions, and repeated application of a generative model yields an episodic simulator. In the opposite direction, it is only possible to learn approximate models through [regression](regression%20analysis.md). The type of model available for a particular MDP plays a significant role in determining which solution algorithms are appropriate. For example, the [dynamic programming](dynamic%20programming.md) algorithms described in the next section require an explicit model, and [Monte Carlo tree search](Monte%20Carlo%20tree%20search.md) requires a generative model \(or an episodic simulator that can be copied at any state\), whereas most [reinforcement learning](#reinforcement%20learning) algorithms require only an episodic simulator.

## example

> {@{![Pole Balancing example \(rendering of the environment from the [Open AI gym benchmark](Open%20AI%20gym%20benchmark.md)\)](../../archives/Wikimedia%20Commons/Cartpole.gif)}@}
>
> {@{Pole Balancing example \(rendering of the environment from the [Open AI gym benchmark](Open%20AI%20gym%20benchmark.md)\)}@} <!--SR:!2025-03-11,73,329!2025-03-14,76,329-->

An example of MDP is {@{the Pole-Balancing model}@}, which comes from {@{classic control theory}@}. <!--SR:!2025-03-12,74,329!2025-03-14,76,329-->

In this example, we have

- $S$ is ::@:: the set of ordered tuples $(\theta ,{\dot {\theta } },x,{\dot {x} })\subset \mathbb {R} ^{4}$ given by pole angle, angular velocity, position of the cart and its speed. <!--SR:!2025-11-04,255,332!2025-11-06,257,332-->
- $A$ is ::@:: $\{-1,1\}$, corresponding to applying a force on the left \(right\) on the cart. <!--SR:!2025-12-07,282,332!2025-11-10,261,332-->
- $P_{a}(s,s')$ is ::@:: the transition of the system, which in this case is going to be deterministic and driven by the laws of mechanics. <!--SR:!2025-11-10,261,332!2025-03-04,67,312-->
- $R_{a}(s,s')$ is ::@:: $1$ if the pole is up after the transition, zero otherwise. Therefore, this function only depend on $s'$ in this specific case. <!--SR:!2025-08-06,179,312!2025-11-02,253,330-->

## algorithms

{@{Solutions for MDPs with finite state and action spaces}@} may be found through {@{a variety of methods such as [dynamic programming](dynamic%20programming.md)}@}. The algorithms in this section apply to {@{MDPs with finite state and action spaces and explicitly given transition probabilities and reward functions}@}, but {@{the basic concepts may be extended to handle other problem classes}@}, for example {@{using [function approximation](function%20approximation.md)}@}. <!--SR:!2025-03-08,70,329!2025-03-14,76,329!2025-03-12,74,329!2025-03-10,72,329!2025-03-10,72,329-->

{@{The standard family of algorithms to calculate optimal policies for finite state and action MDPs}@} requires {@{storage for two arrays indexed by state: _value_ $V$, which contains real values, and _policy_ $\pi$, which contains actions}@}. At {@{the end of the algorithm}@}, $\pi$ will {@{contain the solution and $V(s)$ will contain the discounted sum of the rewards to be earned \(on average\) by following that solution from state $s$}@}. <!--SR:!2025-10-05,227,329!2025-03-14,76,329!2025-03-08,71,329!2025-03-08,71,329-->

The algorithm has {@{two steps, \(1\) a value update and \(2\) a policy update}@}, which are {@{repeated in some order for all the states until no further changes take place}@}. Both {@{recursively update a new estimation of the optimal policy}@} and {@{state value using an older estimation of those values}@}. <!--SR:!2025-03-03,67,329!2025-03-01,65,329!2025-03-11,73,329!2025-12-21,296,349-->

- value update ::@:: $$V(s):=\sum _{s'}P_{\pi (s)}(s,s')\left(R_{\pi (s)}(s,s')+\gamma V(s')\right)$$ <!--SR:!2025-03-15,62,252!2025-04-08,78,272-->
- policy update ::@:: $$\pi (s):=\operatorname {argmax} _{a}\left\{\sum _{s'}P_{a}(s,s')\left(R_{a}(s,s')+\gamma V(s')\right)\right\}$$ <!--SR:!2025-06-07,103,250!2025-05-27,114,292-->

Their order depends on {@{the variant of the algorithm}@}; one can {@{also do them for all states at once or state by state, and more often to some states than others}@}. As long as {@{no state is permanently excluded from either of the steps}@}, {@{the algorithm will eventually arrive at the correct solution}@}.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2025-03-12,74,329!2025-10-09,231,329!2025-03-07,70,329!2025-03-02,66,329-->

### notable variants

#### value iteration

In {@{value iteration \([Bellman 1958](#CITEREFBellman1958)\), which is also called [backward induction](backward%20induction.md)}@}, {@{the $\pi$ function is not used}@}; instead, {@{the value of $\pi (s)$ is calculated within $V(s)$ whenever it is needed}@}. Substituting {@{the calculation of $\pi (s)$ into the calculation of $V(s)$}@} gives the combined step<!-- <sup>\[_[further explanation needed](https://en.wikipedia.org/wiki/Wikipedia:Please%20clarify)_\]</sup> -->: {@{$$V_{i+1}(s):=\max _{a}\left\{\sum _{s'}P_{a}(s,s')\left(R_{a}(s,s')+\gamma V_{i}(s')\right)\right\},$$}@} where {@{$i$ is the iteration number}@}. Value iteration starts at {@{$i=0$ and $V_{0}$ as a guess of the [value function](value%20function.md)}@}. It then {@{iterates, repeatedly computing $V_{i+1}$ for all states $s$}@}, until {@{$V$ converges with the left-hand side equal to the right-hand side}@} \(which is {@{the "[Bellman equation](Bellman%20equation.md)" for this problem}@}<!-- <sup>\[_[clarification needed](https://en.wikipedia.org/wiki/Wikipedia:Please%20clarify)_\]</sup> -->\). {@{[Lloyd Shapley](Lloyd%20Shapley.md)'s 1953 paper}@} on {@{[stochastic games](stochastic%20game.md)}@} included {@{as a special case the value iteration method for MDPs,<sup>[\[7\]](#^ref-7)</sup> but this was recognized only later on}@}.<sup>[\[8\]](#^ref-8)</sup> <!--SR:!2025-03-02,66,329!2025-03-06,69,329!2025-03-13,75,329!2025-03-05,68,329!2025-05-06,99,289!2025-03-10,72,329!2025-03-09,71,329!2025-03-13,75,329!2025-03-14,76,329!2025-03-02,66,329!2025-04-24,92,289!2025-09-16,212,329!2025-03-13,75,329-->

#### policy iteration

In {@{policy iteration \([Howard 1960](#CITEREFHoward1960)\)}@}, {@{step one (value update) is performed once, and then step two (policy update) is performed once, then both are repeated until policy converges}@}. Then {@{step one is again performed once and so on}@}. \(Policy iteration was {@{invented by Howard to optimize [Sears](Sears.md) catalogue mailing}@}, which {@{he had been optimizing using value iteration}@}.<sup>[\[9\]](#^ref-9)</sup>\) <!--SR:!2025-10-12,232,329!2025-03-05,68,329!2025-03-08,71,329!2025-10-06,228,329!2025-03-03,67,329-->

Instead of {@{repeating step two to convergence}@}, it may be {@{formulated and solved as a set of linear equations}@}. These equations are merely obtained by {@{making $s=s'$ in the step two equation}@}.<!-- <sup>\[_[clarification needed](https://en.wikipedia.org/wiki/Wikipedia:Please%20clarify)_\]</sup> --> Thus, {@{repeating step two to convergence}@} can be {@{interpreted as solving the linear equations by [relaxation](relaxation%20(iterative%20method).md)}@}. <!--SR:!2025-03-13,75,329!2025-03-01,65,329!2025-03-12,74,329!2025-03-11,73,329!2025-03-14,76,329-->

This variant has the advantage that {@{there is a definite stopping condition}@}: when {@{the array $\pi$ does not change in the course of applying step 1 to all states}@}, {@{the algorithm is completed}@}. <!--SR:!2025-03-12,74,329!2025-03-11,73,329!2025-03-09,71,329-->

Policy iteration is usually {@{slower than value iteration for a large number of possible states}@}. <!--SR:!2025-03-11,73,329-->

#### modified policy iteration

In {@{modified policy iteration \([van Nunen 1976](#CITEREFvan%20Nunen1976); [Puterman & Shin 1978](#CITEREFPutermanShin1978)\)}@}, {@{step one is performed once, and then step two is repeated several times}@}.<sup>[\[10\]](#^ref-10)</sup><sup>[\[11\]](#^ref-11)</sup> Then {@{step one is again performed once and so on}@}. <!--SR:!2025-09-24,218,329!2025-03-14,76,329!2025-03-07,70,329-->

#### prioritized sweeping

In this variant, the steps are {@{preferentially applied to states which are in some way important}@} – whether based on {@{the algorithm \(there were large changes in $V$ or $\pi$ around those states recently\)}@} or based on {@{use \(those states are near the starting state, or otherwise of interest to the person or program using the algorithm\)}@}. <!--SR:!2025-03-11,73,329!2025-03-09,71,329!2025-03-13,75,329-->

### computational complexity

{@{Algorithms for finding optimal policies with [time complexity](time%20complexity.md) polynomial in the size of the problem representation}@} {@{exist for finite MDPs}@}. Thus, {@{[decision problems](decision%20problem.md) based on MDPs}@} are {@{in computational [complexity class](complexity%20class.md) [P](p%20(complexity).md)}@}.<sup>[\[12\]](#^ref-12)</sup> However, due to {@{the [curse of dimensionality](curse%20of%20dimensionality.md)}@}, {@{the size of the problem representation}@} is {@{often exponential in the number of state and action variables}@}, limiting {@{exact solution techniques to problems that have a compact representation}@}. In practice, {@{online planning techniques such as [Monte Carlo tree search](Monte%20Carlo%20tree%20search.md)}@} can {@{find useful solutions in larger problems}@}, and, in {@{theory}@}, it is possible to {@{construct online planning algorithms that can find an arbitrarily near-optimal policy with no computational complexity dependence on the size of the state space}@}.<sup>[\[13\]](#^ref-13)</sup> <!--SR:!2025-03-08,71,329!2025-03-13,75,329!2025-03-09,71,329!2025-03-12,74,329!2025-03-14,76,329!2025-03-07,70,329!2025-03-02,66,329!2025-03-14,76,329!2025-03-14,76,329!2025-03-05,68,329!2025-03-11,73,329!2025-04-25,92,289-->

## extensions and generalizations

A Markov decision process is {@{a [stochastic game](stochastic%20game.md) with only one player}@}. <!--SR:!2025-03-13,75,329-->

### partial observability

- Main article: [Partially observable Markov decision process](Partially%20observable%20Markov%20decision%20process.md)

The solution above assumes that {@{the state $s$ is known when action is to be taken}@}; otherwise {@{$\pi (s)$ cannot be calculated}@}. When {@{this assumption is not true}@}, the problem is called {@{a partially observable Markov decision process or POMDP}@}. <!--SR:!2025-03-12,74,329!2025-03-10,72,329!2025-03-12,74,329!2025-03-11,73,329-->

### constrained Markov decision processes

{@{Constrained Markov decision processes \(CMDPS\)}@} are {@{extensions to Markov decision process \(MDPs\)}@}. There are {@{three fundamental differences}@} between MDPs and CMDPs.<sup>[\[14\]](#^ref-14)</sup> <!--SR:!2025-03-09,71,329!2025-03-07,70,329!2025-09-11,209,329-->

- There are multiple ::@:: costs incurred after applying an action instead of one. <!--SR:!2025-11-05,256,332!2025-08-24,183,312-->
- CMDPs are solved ::@:: with [linear programs](linear%20programming.md) only, and [dynamic programming](dynamic%20programming.md) does not work. <!--SR:!2025-08-30,198,312!2025-03-05,68,312-->
- The final policy ::@:: depends on the starting state. <!--SR:!2025-11-07,258,332!2025-11-06,257,332-->

{@{The method of Lagrange multipliers}@} applies to CMDPs. {@{Many Lagrangian-based algorithms}@} have been developed. (annotation: An example is {@{the natural policy gradient primal-dual method}@}.) <!--SR:!2025-09-17,213,329!2025-03-09,71,329!2025-07-15,151,309-->

- Natural policy gradient primal-dual method.<sup>[\[15\]](#^ref-15)</sup>

There are {@{a number of applications}@} for CMDPs. It has recently been used in {@{[motion planning](motion%20planning.md) scenarios in robotics}@}.<sup>[\[16\]](#^ref-16)</sup> <!--SR:!2025-03-12,74,329!2025-03-01,65,329-->

### continuous-time Markov decision process

In {@{discrete-time Markov Decision Processes}@}, decisions are {@{made at discrete time intervals}@}. However, for {@{__continuous-time Markov decision processes__}@}, decisions can be {@{made at any time the decision maker chooses}@}. In comparison to {@{discrete-time Markov decision processes}@}, continuous-time Markov decision processes can {@{better model the decision-making process for a system that has [continuous dynamics](discrete%20time%20and%20continuous%20time.md)}@}, i.e., {@{the system dynamics is defined by [ordinary differential equations](ordinary%20differential%20equation.md) \(ODEs\)}@}. These kind of applications raise in {@{[queueing systems](queueing%20theory.md), epidemic processes, and [population processes](population%20process.md)}@}. <!--SR:!2025-03-13,75,329!2025-09-06,205,329!2025-03-10,72,329!2025-10-10,230,329!2025-03-10,72,329!2025-12-22,297,349!2025-03-02,66,329!2025-03-13,75,329-->

Like the discrete-time Markov decision processes, in continuous-time Markov decision processes {@{the agent aims at finding the optimal _policy_ which could maximize the expected cumulated reward}@}. The only difference with the standard case stays in the fact that, {@{due to the continuous nature of the time variable, the sum is replaced by an integral}@}: {@{$$\max \operatorname {E} _{\pi }\left[\left.\int _{0}^{\infty }\gamma ^{t}r(s(t),\pi (s(t)))\,dt\;\right|s_{0}\right]$$}@} where {@{$0\leq \gamma <1.$}@} <!--SR:!2025-03-02,66,329!2025-03-01,65,329!2025-05-03,98,289!2025-03-14,76,329-->

#### discrete space: linear programming formulation

If {@{the state space and action space are finite}@}, we could use {@{linear programming to find the optimal policy}@}, which was {@{one of the earliest approaches applied}@}. Here we only consider {@{the ergodic model}@}, which means {@{our continuous-time MDP becomes an [ergodic](ergodicity.md) continuous-time Markov chain under a stationary [policy](policy.md)}@}. Under this assumption, although {@{the decision maker can make a decision at any time in the current state}@}, there is {@{no benefit in taking multiple actions}@}. It is better to {@{take an action only at the time when system is transitioning from the current state to another state}@}. Under {@{some conditions}@},<sup>[\[17\]](#^ref-17)</sup> if {@{our optimal value function $V^{*}$ is independent of state $i$}@}, we will have the following inequality: $$g\geq R(i,a)+\sum _{j\in S}q(j\mid i,a)h(j)\quad \forall i\in S{\text{ and } }a\in A(i)$$ (TODO: What is this inequality?) If {@{there exists a function $h$}@}, then {@{${\bar {V} }^{*}$ will be the smallest $g$ satisfying the above equation}@}. In order to find ${\bar {V} }^{*}$, we could {@{use the following linear programming model}@}: <!--SR:!2025-03-06,69,329!2025-12-20,295,349!2025-03-09,71,329!2025-03-08,71,329!2025-03-11,73,329!2025-03-13,75,329!2025-03-12,74,329!2025-09-18,214,329!2025-03-07,70,329!2025-03-12,74,329!2025-03-07,70,329!2025-03-13,75,329!2025-03-11,73,329-->

- Primal linear program\(P-LP\) <br/> $${\begin{aligned}{\text{Minimize} }\quad &g\\{\text{s.t} }\quad &g-\sum _{j\in S}q(j\mid i,a)h(j)\geq R(i,a)\,\,\forall i\in S,\,a\in A(i)\end{aligned} }$$
- Dual linear program\(D-LP\) <br/> $${\begin{aligned}{\text{Maximize} }&\sum _{i\in S}\sum _{a\in A(i)}R(i,a)y(i,a)\\{\text{s.t.} }&\sum _{i\in S}\sum _{a\in A(i)}q(j\mid i,a)y(i,a)=0\quad \forall j\in S,\\&\sum _{i\in S}\sum _{a\in A(i)}y(i,a)=1,\\&y(i,a)\geq 0\qquad \forall a\in A(i){\text{ and } }\forall i\in S\end{aligned} }$$

$y(i,a)$ is {@{a feasible solution to the D-LP}@} if {@{$y(i,a)$ is nonnative and satisfied the constraints in the D-LP problem}@}. {@{A feasible solution $y^{*}(i,a)$ to the D-LP is said to be an optimal solution}@} if {@{$${\begin{aligned}\sum _{i\in S}\sum _{a\in A(i)}R(i,a)y^{*}(i,a)\geq \sum _{i\in S}\sum _{a\in A(i)}R(i,a)y(i,a)\end{aligned} }$$ for all feasible solution $y(i,a)$ to the D-LP}@}. Once {@{we have found the optimal solution $y^{*}(i,a)$}@}, we can {@{use it to establish the optimal policies}@}. <!--SR:!2025-03-12,74,329!2025-07-15,155,309!2025-03-14,76,329!2025-05-05,98,289!2025-08-29,200,329!2025-03-05,68,329-->

#### continuous space: Hamilton–Jacobi–Bellman equation

In continuous-time MDP, if {@{the state space and action space are continuous}@}, {@{the optimal criterion could be found by solving [Hamilton–Jacobi–Bellman \(HJB\) partial differential equation](Hamilton–Jacobi–Bellman%20equation.md)}@}. In order to {@{discuss the HJB equation}@}, we need to reformulate our problem {@{$${\begin{aligned}V(s(0),0)={}&\max _{a(t)=\pi (s(t))}\int _{0}^{T}r(s(t),a(t))\,dt+D[s(T)]\\{\text{s.t.} }\quad &{\frac {ds(t)}{dt} }=f[s(t),a(t), t]\end{aligned} }$$}@} (annotation: The optimal value is {@{the maximum reward we can get in the process (the integral) plus the final reward}@}, such that {@{the process evolution, $s(t)$, is a valid evolution (the constraint)}@}.) $D(\cdot )$ is {@{the terminal reward function}@}, $s(t)$ is {@{the system state vector}@}, $a(t)$ is {@{the system control vector we try to find}@}. $f(\cdot )$ shows {@{how the state vector changes over time}@}. The Hamilton–Jacobi–Bellman equation is as follows: {@{$$0=\max _{a}(r(s,a, t)+{\frac {\partial V(s, t)}{\partial s} }f(s,a, t))$$}@} We could {@{solve the equation to find the optimal control $a(t)$}@}, which could {@{give us the optimal [value function](value%20function.md) $V^{*}$}@}. <!--SR:!2025-03-09,71,329!2025-03-11,73,329!2025-03-09,71,329!2025-04-26,93,289!2025-03-09,71,329!2025-03-11,73,329!2025-03-09,71,329!2025-03-14,76,329!2025-03-13,75,329!2025-09-20,216,329!2025-03-24,70,269!2025-09-17,213,329!2025-03-01,65,329-->

## reinforcement learning

- Main article: [Reinforcement learning](reinforcement%20learning.md)

{@{[Reinforcement learning](reinforcement%20learning.md)}@} is {@{an interdisciplinary area of [machine learning](machine%20learning.md) and [optimal control](optimal%20control.md)}@} that has, {@{as main objective, finding an approximately optimal policy for MDPs where transition probabilities and rewards are unknown}@}.<sup>[\[18\]](#^ref-18)</sup> <!--SR:!2025-03-12,74,329!2025-03-10,72,329!2025-03-14,76,329-->

Reinforcement learning can {@{solve Markov-Decision processes without explicit specification of the transition probabilities}@} which are instead {@{needed to perform policy iteration}@}. In this setting, {@{transition probabilities and rewards must be learned from experience}@}, i.e. by {@{letting an agent interact with the MDP for a given number of steps}@}. Both on {@{a theoretical and on a practical level}@}, effort is put in {@{maximizing the sample efficiency, i.e. minimimizing the number of samples needed to learn a policy}@} whose {@{performance is $\varepsilon$-close to the optimal one}@} \(due to {@{the stochastic nature of the process}@}, {@{learning the optimal policy with a finite number of samples}@} is, in general, impossible\). <!--SR:!2025-03-01,65,329!2025-03-10,72,329!2025-03-12,74,329!2025-03-12,74,329!2025-03-11,73,329!2025-03-14,76,329!2025-03-10,72,329!2025-03-14,76,329!2025-03-13,75,329-->

### reinforcement learning for discrete MDPs

For {@{the purpose of this section}@}, it is useful to {@{define a further function}@}, which corresponds to {@{taking the action $a$ and then continuing optimally \(or according to whatever policy one currently has\)}@}: {@{$$\ Q(s,a)=\sum _{s'}P_{a}(s,s')(R_{a}(s,s')+\gamma V(s')).\ {}$$}@} While {@{this function is also unknown}@}, {@{experience during learning is based on $(s,a)$ pairs}@} \(together with {@{the outcome $s'$; that is, "I was in state $s$ and I tried doing $a$ and $s'$ happened"}@}\). Thus, {@{one has an array $Q$ and uses experience to update it directly}@}. This is known as {@{[Q-learning](Q-learning.md)}@}. <!--SR:!2025-03-03,67,329!2025-06-15,139,309!2025-03-10,72,329!2025-03-14,76,329!2025-03-12,74,329!2025-03-10,72,329!2025-03-03,67,329!2025-12-18,293,349!2025-03-13,75,329-->

## other scopes

### learning automata

- Main article: [Learning automata](learning%20automaton.md)

Another application of MDP process in {@{[machine learning](machine%20learning.md) theory}@} is called {@{learning automata}@}. This is also {@{one type of reinforcement learning if the environment is stochastic}@}. {@{The first detail __learning automata__ paper}@} is surveyed by {@{[Narendra](Kumpati%20S.%20Narendra.md) and Thathachar \(1974\)}@}, which were originally {@{described explicitly as [finite state automata](finite-state%20machine.md)}@}.<sup>[\[19\]](#^ref-19)</sup> Similar to {@{reinforcement learning}@}, a learning automata algorithm also has {@{the advantage of solving the problem when probability or rewards are unknown}@}. {@{The difference between learning automata and Q-learning}@} is that {@{the former technique omits the memory of Q-values, but updates the action probability directly to find the learning result}@}. Learning automata is {@{a learning scheme with a rigorous proof of convergence}@}.<sup>[\[20\]](#^ref-20)</sup> <!--SR:!2025-03-14,76,329!2025-03-03,67,329!2025-03-14,76,329!2025-03-05,68,329!2025-08-01,163,309!2025-03-08,71,329!2025-10-10,230,329!2025-03-10,72,329!2025-03-03,67,329!2025-03-14,76,329!2025-03-09,71,329-->

In {@{learning automata theory}@}, a {@{__stochastic automaton__}@} consists of: <!--SR:!2025-03-14,76,329!2025-03-08,70,329-->

- a set _x_ ::@:: of possible inputs, <!--SR:!2025-12-06,281,332!2025-11-09,260,332-->
- a set Φ = { Φ<sub>1</sub>, ..., Φ<sub>_s_</sub> } ::@:: of possible internal states, <!--SR:!2025-11-07,258,332!2025-03-03,66,312-->
- a set α = { α<sub>1</sub>, ..., α<sub>_r_</sub> } ::@:: of possible outputs, or actions, with _r_ ≤ _s_, <!--SR:!2025-07-03,140,292!2025-12-07,282,332-->
- an initial state probability vector ::@:: _p_\(0\) = ≪ _p_<sub>1</sub>\(0\), ..., _p<sub>s</sub>_\(0\) ≫, (annotation: This randomly selects the current state.) <!--SR:!2025-12-06,281,332!2025-08-24,183,312-->
- a [computable function](computable%20function.md) _A_ which ::@:: after each time step _t_ generates _p_\(_t_ + 1\) from _p_\(_t_\), the current input, and the current state, and (annotation: This makes the automata "learn" from an input.) <!--SR:!2025-04-03,76,272!2025-06-04,120,292-->
- a function _G_: Φ → α which ::@:: generates the output at each time step. (annotation: Note that the function only depends on the current state, not the current input.) <!--SR:!2025-08-23,182,312!2025-09-01,199,312-->

{@{The states of such an automaton}@} correspond to {@{the states of a "discrete-state discrete-parameter [Markov process](Markov%20chain.md)"}@}.<sup>[\[21\]](#^ref-21)</sup> At {@{each time step _t_ = 0,1,2,3,...}@}, the automaton {@{reads an input from its environment}@}, {@{updates P\(_t_\) to P\(_t_ + 1\) by _A_}@}, {@{randomly chooses a successor state according to the probabilities P\(_t_ + 1\)}@} and {@{outputs the corresponding action}@}. The automaton's environment, in turn, {@{reads the action and sends the next input to the automaton}@}.<sup>[\[20\]](#^ref-20)</sup> <!--SR:!2025-03-12,74,329!2025-08-10,169,309!2025-03-08,70,329!2025-03-09,71,329!2025-03-13,75,329!2025-03-10,72,329!2025-03-10,72,329!2025-03-13,75,329-->

### category theoretic interpretation

Other than {@{the rewards}@}, a Markov decision process $(S,A,P)$ can be {@{understood in terms of [Category theory](category%20theory.md)}@}. Namely, let {@{${\mathcal {A} }$ denote the [free monoid](free%20monoid.md) with generating set _A_}@}. Let {@{__Dist__ denote the [Kleisli category](Kleisli%20category.md) of the [Giry monad](http://ncatlab.org/nlab/show/Giry+monad)}@}. Then {@{a functor ${\mathcal {A} }\to \mathbf {Dist}$}@} encodes {@{both the set _S_ of states and the probability function _P_}@}. (annotation: Thus, {@{$(\mathcal A, F: \mathcal A \to \mathbf{Dist})$ may be used to represent $(S, A, P)$}@} instead.) (TODO: What is this abstract nonsense?) <!--SR:!2025-03-12,74,329!2025-03-08,71,329!2025-03-09,71,329!2025-03-01,45,269!2025-07-24,158,309!2025-03-10,72,329!2025-07-10,148,309-->

In this way, Markov decision processes could be {@{generalized from monoids \(categories with one object\) to arbitrary categories}@}. One can call {@{the result $({\mathcal {C} },F:{\mathcal {C} }\to \mathbf {Dist} )$}@} {@{a _context-dependent Markov decision process_}@}, because {@{moving from one object to another in ${\mathcal {C} }$}@} changes {@{the set of available actions and the set of possible states}@}.<!-- <sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> --> <!--SR:!2025-03-11,73,329!2025-03-11,73,329!2025-03-13,75,329!2025-09-03,203,329!2025-03-12,74,329-->

## alternative notations

{@{The terminology and notation for MDPs}@} are {@{not entirely settled}@}. There are {@{two main streams}@} — one focuses on {@{maximization problems from contexts like economics}@}, using the terms {@{action, reward, value, and calling the discount factor _β_ or _γ_}@}, while the other focuses on {@{minimization problems from engineering and navigation}@}<!-- <sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> -->, using the terms {@{control, cost, cost-to-go, and calling the discount factor _α_}@}. In addition, {@{the notation for the transition probability}@} varies. <!--SR:!2025-03-06,69,329!2025-03-02,66,329!2025-03-10,72,329!2025-10-11,231,329!2025-03-11,73,329!2025-03-03,67,329!2025-03-11,73,329!2025-03-13,75,329-->

| in this article                            | alternative                               | comment                          |
| ------------------------------------------ | ----------------------------------------- | -------------------------------- |
| {@{action _a_}@}                           | {@{control _u_}@}                         |                                  |
| {@{reward _R_}@}                           | {@{cost _g_}@}                            | _g_ is {@{the negative of _R_}@} |
| {@{value _V_}@}                            | {@{cost-to-go _J_}@}                      | _J_ is {@{the negative of _V_}@} |
| {@{policy _π_}@}                           | {@{policy _μ_}@}                          |                                  |
| {@{discounting factor _γ_}@}               | {@{discounting factor _α_}@}              |                                  |
| {@{transition probability $P_{a}(s,s')$}@} | {@{transition probability $p_{ss'}(a)$}@} |                                  | <!--SR:!2025-03-11,73,329!2025-03-11,73,329!2025-03-10,72,329!2025-03-13,75,329!2025-03-13,75,329!2025-03-09,71,329!2025-03-08,71,329!2025-03-01,65,329!2025-03-12,74,329!2025-03-12,74,329!2025-03-03,67,329!2025-03-10,72,329!2025-03-14,76,329!2025-03-01,65,329-->

In addition, {@{transition probability}@} is {@{sometimes written $\Pr(s,a,s')$, $\Pr(s'\mid s,a)$ or, rarely, $p_{s's}(a).$}@} <!--SR:!2025-03-10,72,329!2025-03-14,76,329-->

## see also

- [Probabilistic automata](probabilistic%20automaton.md)
- [Odds algorithm](odds%20algorithm.md)
- [Quantum finite automata](quantum%20finite%20automaton.md)
- [Partially observable Markov decision process](partially%20observable%20Markov%20decision%20process.md)
- [Dynamic programming](dynamic%20programming.md)
- [Bellman equation](Bellman%20equation.md) for ::@:: applications to economics. <!--SR:!2025-11-08,259,332!2025-11-06,257,332-->
- [Hamilton–Jacobi–Bellman equation](Hamilton–Jacobi–Bellman%20equation.md)
- [Optimal control](optimal%20control.md)
- [Recursive economics](recursive%20economics.md)
- [Mabinogion sheep problem](Mabinogion%20sheep%20problem.md)
- [Stochastic games](stochastic%20game.md)
- [Q-learning](Q-learning.md)
- [Markov chain](Markov%20chain.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Markov_decision_process) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFPuterman1994"></a> Puterman, Martin L. \(1994\). _Markov decision processes: discrete stochastic dynamic programming_. Wiley series in probability and mathematical statistics. Applied probability and statistics section. New York: Wiley. [ISBN](ISBN.md) [978-0-471-61977-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-471-61977-2). <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFSchneiderWagner1957"></a> Schneider, S.; Wagner, D. H. \(1957-02-26\). ["Error detection in redundant systems"](https://dl.acm.org/doi/10.1145/1455567.1455587). _Papers presented at the February 26-28, 1957, western joint computer conference: Techniques for reliability on - IRE-AIEE-ACM '57 \(Western\)_. New York, NY, USA: Association for Computing Machinery. pp. 115–121. [doi](digital%20object%20identifier.md):[10.1145/1455567.1455587](https://doi.org/10.1145%2F1455567.1455587). [ISBN](ISBN.md) [978-1-4503-7861-1](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4503-7861-1). <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFBellman1958"></a> Bellman, Richard \(1958-09-01\). ["Dynamic programming and stochastic control processes"](https://linkinghub.elsevier.com/retrieve/pii/S0019995858800030). _Information and Control_. __1__ \(3\): 228–239. [doi](digital%20object%20identifier.md):[10.1016/S0019-9958\(58\)80003-0](https://doi.org/10.1016%2FS0019-9958%2858%2980003-0). [ISSN](ISSN.md) [0019-9958](https://search.worldcat.org/issn/0019-9958). <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFSuttonBarto2018"></a> Sutton, Richard S.; Barto, Andrew G. \(2018\). _Reinforcement learning: an introduction_. Adaptive computation and machine learning series \(2nd ed.\). Cambridge, Massachusetts: The MIT Press. [ISBN](ISBN.md) [978-0-262-03924-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-262-03924-6). <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFKearnsMansourNg2002"></a> Kearns, Michael; Mansour, Yishay; Ng, Andrew \(2002\). ["A Sparse Sampling Algorithm for Near-Optimal Planning in Large Markov Decision Processes"](https://doi.org/10.1023%2FA%3A1017932429737). _Machine Learning_. __49__ \(193–208\): 193–208. [doi](digital%20object%20identifier.md):[10.1023/A:1017932429737](https://doi.org/10.1023%2FA%3A1017932429737). <a id="^ref-5"></a>^ref-5
6. _Reinforcement Learning: Theory and Python Implementation_. Beijing: China Machine Press. 2019. p. 44. [ISBN](ISBN.md) [9787111631774](https://en.wikipedia.org/wiki/Special:BookSources/9787111631774). <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFShapley1953"></a> [Shapley, Lloyd](Lloyd%20Shapley.md) \(1953\). ["Stochastic Games"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1063912). _Proceedings of the National Academy of Sciences of the United States of America_. __39__ \(10\): 1095–1100. [Bibcode](bibcode.md):[1953PNAS...39.1095S](https://ui.adsabs.harvard.edu/abs/1953PNAS...39.1095S). [doi](digital%20object%20identifier.md):[10.1073/pnas.39.10.1095](https://doi.org/10.1073%2Fpnas.39.10.1095). [PMC](PubMed%20Central.md#PMCID) [1063912](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1063912). [PMID](PubMed.md#PubMed%20identifier) [16589380](https://pubmed.ncbi.nlm.nih.gov/16589380). <a id="^ref-7"></a>^ref-7
8. <a id="CITEREFKallenberg2002"></a> Kallenberg, Lodewijk \(2002\). "Finite state and action MDPs". In [Feinberg, Eugene A.](Eugene%20A.%20Feinberg.md); Shwartz, Adam \(eds.\). _Handbook of Markov decision processes: methods and applications_. Springer. [ISBN](ISBN.md) [978-0-7923-7459-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-7923-7459-6). <a id="^ref-8"></a>^ref-8
9. Howard 2002, ["Comments on the Origin and Application of Markov Decision Processes"](https://pubsonline.informs.org/doi/10.1287/opre.50.1.100.17788) <a id="^ref-9"></a>^ref-9
10. <a id="CITEREFPutermanShin1978"></a> Puterman, M. L.; Shin, M. C. \(1978\). "Modified Policy Iteration Algorithms for Discounted Markov Decision Problems". _Management Science_. __24__ \(11\): 1127–1137. [doi](digital%20object%20identifier.md):[10.1287/mnsc.24.11.1127](https://doi.org/10.1287%2Fmnsc.24.11.1127). <a id="^ref-10"></a>^ref-10
11. <a id="CITEREFvan Nunen1976"></a> van Nunen, J.A. E. E \(1976\). "A set of successive approximation methods for discounted Markovian decision problems". _Zeitschrift für Operations Research_. __20__ \(5\): 203–208. [doi](digital%20object%20identifier.md):[10.1007/bf01920264](https://doi.org/10.1007%2Fbf01920264). [S2CID](Semantic%20Scholar.md#S2CID) [5167748](https://api.semanticscholar.org/CorpusID:5167748). <a id="^ref-11"></a>^ref-11
12. <a id="CITEREFPapadimitriouTsitsiklis1987"></a> [Papadimitriou, Christos](Christos%20Papadimitriou.md); [Tsitsiklis, John](John%20Tsitsiklis.md) \(1987\). ["The Complexity of Markov Decision Processes"](https://pubsonline.informs.org/doi/abs/10.1287/moor.12.3.441). _[Mathematics of Operations Research](Mathematics%20of%20Operations%20Research.md)_. __12__ \(3\): 441–450. [doi](digital%20object%20identifier.md):[10.1287/moor.12.3.441](https://doi.org/10.1287%2Fmoor.12.3.441). [hdl](Handle%20System.md):[1721.1/2893](https://hdl.handle.net/1721.1%2F2893). Retrieved November 2, 2023. <a id="^ref-12"></a>^ref-12
13. <a id="CITEREFKearnsMansourNg2002"></a> Kearns, Michael; Mansour, Yishay; Ng, Andrew \(November 2002\). ["A Sparse Sampling Algorithm for Near-Optimal Planning in Large Markov Decision Processes"](https://doi.org/10.1023%2FA%3A1017932429737). _Machine Learning_. __49__ \(2/3\): 193–208. [doi](digital%20object%20identifier.md):[10.1023/A:1017932429737](https://doi.org/10.1023%2FA%3A1017932429737). <a id="^ref-13"></a>^ref-13
14. <a id="CITEREFAltman1999"></a> Altman, Eitan \(1999\). _Constrained Markov decision processes_. Vol. 7. CRC Press. <a id="^ref-14"></a>^ref-14
15. <a id="CITEREFDingZhangJovanovicBasar2020"></a> Ding, Dongsheng; Zhang, Kaiqing; Jovanovic, Mihailo; Basar, Tamer \(2020\). _Natural policy gradient primal-dual method for constrained Markov decision processes_. Advances in Neural Information Processing Systems. <a id="^ref-15"></a>^ref-15
16. <a id="CITEREFFeyzabadiCarpin2014"></a> Feyzabadi, S.; Carpin, S. \(18–22 Aug 2014\). ["Risk-aware path planning using hierarchical constrained Markov Decision Processes"](https://www.researchgate.net/publication/270105954). _Automation Science and Engineering \(CASE\)_. IEEE International Conference. pp. 297, 303. <a id="^ref-16"></a>^ref-16
17. [_Continuous-Time Markov Decision Processes_](https://link.springer.com/book/10.1007/978-3-642-02547-1). Stochastic Modelling and Applied Probability. Vol. 62. 2009. [doi](digital%20object%20identifier.md):[10.1007/978-3-642-02547-1](https://doi.org/10.1007%2F978-3-642-02547-1). [ISBN](ISBN.md) [978-3-642-02546-4](https://en.wikipedia.org/wiki/Special:BookSources/978-3-642-02546-4). <a id="^ref-17"></a>^ref-17
18. <a id="CITEREFShoham, Y.Powers, R.Grenager, T.2003"></a> Shoham, Y.; Powers, R.; Grenager, T. \(2003\). ["Multi-agent reinforcement learning: a critical survey"](http://jmvidal.cse.sc.edu/library/shoham03a.pdf) \(PDF\). _Technical Report, Stanford University_: 1–13. Retrieved 2018-12-12. <a id="^ref-18"></a>^ref-18
19. <a id="CITEREFNarendraThathachar1974"></a> [Narendra, K. S.](Kumpati%20S.%20Narendra.md); Thathachar, M. A. L. \(1974\). "Learning Automata – A Survey". _IEEE Transactions on Systems, Man, and Cybernetics_. SMC-4 \(4\): 323–334. [CiteSeerX](CiteSeerX.md) [10.1.1.295.2280](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.295.2280). [doi](digital%20object%20identifier.md):[10.1109/TSMC.1974.5408453](https://doi.org/10.1109%2FTSMC.1974.5408453). [ISSN](ISSN.md) [0018-9472](https://search.worldcat.org/issn/0018-9472). <a id="^ref-19"></a>^ref-19
20. <a id="CITEREFNarendraThathachar1989"></a> [Narendra, Kumpati S.](Kumpati%20S.%20Narendra.md); Thathachar, Mandayam A. L. \(1989\). [_Learning automata: An introduction_](https://archive.org/details/learningautomata00nare). Prentice Hall. [ISBN](ISBN.md) [9780134855585](https://en.wikipedia.org/wiki/Special:BookSources/9780134855585). <a id="^ref-20"></a>^ref-20
21. [Narendra & Thathachar 1974](#CITEREFNarendraThathachar1974), p.325 left. <a id="^ref-21"></a>^ref-21

## further reading

- <a id="CITEREFBellman.2003"></a> Bellman., R. E. \(2003\) \[1957\]. _Dynamic Programming_ \(Dover paperback ed.\). Princeton, NJ: Princeton University Press. [ISBN](ISBN.md) [978-0-486-42809-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-42809-3).
- <a id="CITEREFBertsekas1995"></a> Bertsekas, D. \(1995\). _Dynamic Programming and Optimal Control_. Vol. 2. MA: Athena.
- <a id="CITEREFDerman1970"></a> Derman, C. \(1970\). _Finite state Markovian decision processes_. Academic Press.
- <a id="CITEREFFeinbergShwartz2002"></a> Feinberg, E.A.; Shwartz, A., eds. \(2002\). [_Handbook of Markov Decision Processes_](https://books.google.com/books?id=TpwKCAAAQBAJ). Boston, MA: Kluwer. [ISBN](ISBN.md) [9781461508052](https://en.wikipedia.org/wiki/Special:BookSources/9781461508052).
- <a id="CITEREFGuoHernández-Lerma2009"></a> Guo, X.; Hernández-Lerma, O. \(2009\). [_Continuous-Time Markov Decision Processes_](https://www.springer.com/mathematics/applications/book/978-3-642-02546-4). Stochastic Modelling and Applied Probability. Springer. [ISBN](ISBN.md) [9783642025464](https://en.wikipedia.org/wiki/Special:BookSources/9783642025464).
- <a id="CITEREFMeyn2007"></a> Meyn, S. P. \(2007\). [_Control Techniques for Complex Networks_](https://web.archive.org/web/20100619011046/https://netfiles.uiuc.edu/meyn/www/spm_files/CTCN/CTCN.html). Cambridge University Press. [ISBN](ISBN.md) [978-0-521-88441-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-88441-9). Archived from [the original](https://netfiles.uiuc.edu/meyn/www/spm_files/CTCN/CTCN.html) on 19 June 2010. Appendix contains abridged ["Meyn & Tweedie"](https://web.archive.org/web/20121218173202/https://netfiles.uiuc.edu/meyn/www/spm_files/book.html). Archived from [the original](https://netfiles.uiuc.edu/meyn/www/spm_files/book.html) on 18 December 2012.
- <a id="CITEREFPuterman.1994"></a> Puterman., M. L. \(1994\). _Markov Decision Processes_. Wiley.
- <a id="CITEREFRoss1983"></a> Ross, S. M. \(1983\). [_Introduction to stochastic dynamic programming_](http://www.deeplearningitalia.com/wp-content/uploads/2018/03/Introduction-to-Stochastic-Dynamic-Programming-Ross.pdf) \(PDF\). Academic press.
- <a id="CITEREFSuttonBarto2017"></a> Sutton, R. S.; Barto, A. G. \(2017\). [_Reinforcement Learning: An Introduction_](http://incompleteideas.net/sutton/book/the-book-2nd.html). Cambridge, MA: The MIT Press.
- <a id="CITEREFTijms.2003"></a> Tijms., H.C. \(2003\). [_A First Course in Stochastic Models_](https://books.google.com/books?id=WibF8iVHaiMC). Wiley. [ISBN](ISBN.md) [9780470864289](https://en.wikipedia.org/wiki/Special:BookSources/9780470864289).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Optimal decisions](https://en.wikipedia.org/wiki/Category:Optimal%20decisions)
> - [Dynamic programming](https://en.wikipedia.org/wiki/Category:Dynamic%20programming)
> - [Markov processes](https://en.wikipedia.org/wiki/Category:Markov%20processes)
> - [Stochastic control](https://en.wikipedia.org/wiki/Category:Stochastic%20control)
