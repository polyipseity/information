---
aliases:
  - Markov chain
  - discrete-time Markov chain
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/Markov_chains
  - language/in/English
---

# Markov chain

A Markov chain is a model for a system that evolves in discrete time steps where the probability of each future step depends only on the current state, not on how the chain arrived there. This "memoryless" property, called the Markov property, is what makes the model tractable for a huge range of applications, from queueing theory and statistical physics to finance and reinforcement learning.

The classic illustration is a random walk on a graph. Imagine a particle that at each time step moves from the current vertex to a neighbouring vertex chosen at random. The next position depends only on where the particle is now—the past trajectory is irrelevant once the current location is known. The Markov chain formalizes this idea for a finite set of possible states.

For simplicity, only finite state spaces $E=\{1,\dots,N\}$ are considered in this chapter. The state space $E$ is the set of all possible configurations the system can occupy, and the chain moves among these states according to fixed probabilities that depend only on the current state.

---

Flashcards for this section are as follows:

- Markov chain / overview ::@:: A discrete-time stochastic process $(X_n)_{n\ge0}$ on a finite state space $E=\{1,\dots,N\}$ where the probability of each future step depends only on the current state (Markov property). The classic illustration is a random walk on a graph — the next position depends only on the current vertex. Applications: queueing theory, statistical physics, finance, reinforcement learning. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Markov chain / the Markov property as conditional independence ::@:: For all $n\ge0$ and $x_0,\dots,x_{n+1}\in E$, $P[X_{n+1}=x_{n+1}\mid X_0=x_0,\dots,X_n=x_n]=P[X_{n+1}=x_{n+1}\mid X_n=x_n]$. Conditionally on the present $X_n$, the future $X_{n+1}$ is independent of the past $X_0,\dots,X_{n-1}$. This "memoryless" property makes Markov chains tractable. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## transition matrices and the Markov property

The dynamics of a Markov chain are encoded in its transition matrix $\Pi$. An $N\times N$ matrix $\Pi$ is called a matrix of transition probabilities if for every $x\in E$, the row $\Pi(x,\cdot)$ is a probability mass function—meaning all entries are non-negative and sum to $1$. The entry $\Pi(x,y)$ is the probability that the chain moves from $x$ to $y$ in a single step.

**Transition matrix.** An $N\times N$ matrix $\Pi$ is a matrix of transition probabilities if for every $x\in E$, the row $\Pi(x,\cdot)$ is a probability mass function. The entry $\Pi(x,y)$ is the probability that the chain moves from $x$ to $y$ in one step.

**Example.** For $E=\{1,2,3\}$,
$$
\Pi_1=\begin{pmatrix}
0.1&0.2&0.7\\
0.3&0.3&0.4\\
0&0.5&0.5
\end{pmatrix}
$$
is a valid transition matrix (rows sum to $1$, all entries non‑negative).

Not every matrix qualifies as a transition matrix. Two counterexamples illustrate the requirements:

<!-- Added from PDF: Example 13.8 -->
$$
\Pi_2=\begin{pmatrix}
0.5&0.5&0\\
0&0.5&0.5\\
0.5&0&0
\end{pmatrix}
$$
$\Pi_2$ is **invalid** because the rows must each sum to $1$. Row 3 sums to $0.5\neq1$, so $\Pi_2$ does not represent a valid set of one‑step transition probabilities — from state 3 the probabilities of where the chain goes next would not sum to $1$.

<!-- Added from PDF: Example 13.8 -->
$$
\Pi_3=\begin{pmatrix}
0.5&-0.5&1\\
0&0.5&0.5\\
0.5&0&0.5
\end{pmatrix}
$$
$\Pi_3$ is **invalid** because it contains a negative entry ($-0.5$ at position $(1,2)$). Transition probabilities must be non‑negative — they are probabilities, so values below zero are not allowed. Although every row of $\Pi_3$ sums to $1$, the negative entry makes it an invalid stochastic matrix.

The Markov property formalizes the "memoryless" intuition as a precise conditional-probability condition. It says that the conditional distribution of the next state $X_{n+1}$ depends on the entire history $X_0,\dots,X_n$ only through the present state $X_n$; the transition matrix $\Pi$ supplies the one-step probabilities. Given any initial distribution $\mu$ on $E$ and any transition matrix $\Pi$, a Markov chain with those dynamics exists.

**Markov property.** For all $n\ge0$ and $x_0,\dots,x_{n+1}\in E$,
$$
P[X_{n+1}=x_{n+1}\mid X_0=x_0,\dots,X_n=x_n]=\Pi(x_n,x_{n+1}).
$$

---

Flashcards for this section are as follows:

- Markov chain / overview ::@:: A discrete-time stochastic process $(X_n)_{n\ge0}$ on finite state space $E=\{1,\dots,N\}$ where the next state depends only on the current state (Markov property). The dynamics are encoded by a transition matrix $\Pi$ (each row is a pmf), and the full law is specified by the pair $(\mu,\Pi)$ where $\mu$ is the initial distribution. Classic example: random walk on a graph — at each step move to a neighbour uniformly at random; the next position depends only on the current vertex. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Markov chain: definition ::@:: $(X_n)_{n\ge0}$ on $E$ with $P[X_{n+1}=x_{n+1}\mid X_0=x_0,\dots,X_n=x_n]=\Pi(x_n,x_{n+1})$, where $\Pi$ is a transition matrix. The Markov property says that conditionally on $X_n$, the future $X_{n+1}$ is independent of the past $X_0,\dots,X_{n-1}$. Any initial distribution $\mu$ and transition matrix $\Pi$ define a unique Markov chain (Kolmogorov extension). <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- transition matrix ::@:: $\Pi$ is an $N\times N$ matrix where each row $\Pi(x,\cdot)$ is a probability mass function (non-negative entries summing to $1$). The entry $\Pi(x,y)=P[X_{n+1}=y\mid X_n=x]$ is the one-step transition probability from $x$ to $y$, independent of $n$ (time homogeneity). Example: $\Pi_1$ with rows $(0.1,0.2,0.7),(0.3,0.3,0.4),(0,0.5,0.5)$ is valid because each row sums to $1$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- transition matrix / row-stochastic property ::@:: For each $x\in E$, $\sum_{y\in E}\Pi(x,y)=1$ and $\Pi(x,y)\ge0$, so every row of $\Pi$ is a probability mass function. This ensures that from any state $x$, the probabilities of all possible next states sum to $1$. It also implies that $\Pi$ has spectral radius $1$ and that $\mathbf 1$ (the all-ones vector) is a right eigenvector with eigenvalue $1$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- transition matrix / invalid: row sum $\neq1$ ::@:: $\Pi_2$ with rows $(0.5,0.5,0),(0,0.5,0.5),(0.5,0,0)$ is invalid because row 3 sums to $0.5\neq1$. Every row of a transition matrix must sum to $1$ — it must be a probability mass function, otherwise the one-step probabilities from some state would not be a valid distribution. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- transition matrix / invalid: negative entry ::@:: $\Pi_3$ with entry $-0.5$ at position $(1,2)$ is invalid because transition probabilities must be non-negative. Although every row sums to $1$, a negative value is not allowed — probabilities cannot be below zero. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Markov property intuition ::@:: The next step depends only on the current position, not on how the chain arrived there. Formally: for every $n$ and every history $x_0,\dots,x_{n+1}$, $P[X_{n+1}=x_{n+1}\mid X_0=x_0,\dots,X_n=x_n]=P[X_{n+1}=x_{n+1}\mid X_n=x_n]=\Pi(x_n,x_{n+1})$. This is the "memoryless" property that makes Markov chains tractable. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## joint law and n-step transitions

Once the initial distribution $\mu$ and the transition matrix $\Pi$ are fixed, the joint distribution of any finite segment of the chain is determined by multiplying the initial probability with the successive one-step transition probabilities.

**Joint law.** For a Markov chain with initial distribution $\mu$ and transition matrix $\Pi$,
$$
P[X_0=x_0,\dots,X_n=x_n]=\mu(x_0)\,\Pi(x_0,x_1)\cdots\Pi(x_{n-1},x_n).
$$

The chain is therefore completely specified by $(\mu,\Pi)$, and every probability statement about the chain can in principle be derived from this joint law.

It is also useful to know the probabilities of moving from one state to another in more than one step. The $n$-step transition probabilities are defined by $\Pi^{(n)}(x,y)=P[X_{n+m}=y\mid X_m=x]$. These turn out to be the entries of the $n$-fold matrix product of $\Pi$ with itself.

**$n$-step transitions.** For $n$-step transition probabilities $\Pi^{(n)}(x,y)=P[X_{n+m}=y\mid X_m=x]$:

1. $\Pi^{(n)}=\Pi^n$ (the $n$-fold matrix product).
2. **Chapman–Kolmogorov equation:** $\Pi^{(n)}(x,y)=\sum_{z\in E}\Pi^{(r)}(x,z)\,\Pi^{(n-r)}(z,y)$ for $0<r<n$.
3. $P[X_n=y]=\sum_{z\in E}\mu(z)\,\Pi^n(z,y)$.

The Chapman–Kolmogorov equation expresses the fact that to go from $x$ to $y$ in $n$ steps, the chain must pass through some intermediate state $z$ after $r$ steps, and these intermediate possibilities are summed over. The proposition's third part says that the marginal distribution of $X_n$ is obtained by multiplying the initial distribution (as a row vector) by $\Pi^n$.

---

Flashcards for this section are as follows:

- Markov chain joint law ::@:: $P[X_0=x_0,\dots,X_n=x_n]=\mu(x_0)\Pi(x_0,x_1)\cdots\Pi(x_{n-1},x_n)$. Derivation: by repeatedly applying the Markov property, the joint probability factors into the initial probability $\mu(x_0)$ times the successive one-step transition probabilities. This formula completely specifies the law of the chain from $(\mu,\Pi)$. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- $n$-step transition probability ::@:: $\Pi^{(n)}(x,y)=P[X_{n+m}=y\mid X_m=x]=\Pi^n(x,y)$ (the $n$-fold matrix product). Proof: by induction using $\Pi^{(n+1)}(x,y)=\sum_z\Pi^{(n)}(x,z)\Pi(z,y)$, which is exactly matrix multiplication. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- Chapman–Kolmogorov equation ::@:: $\Pi^{(n)}(x,y)=\sum_{z\in E}\Pi^{(r)}(x,z)\,\Pi^{(n-r)}(z,y)$ for $0<r<n$. Intuition: to go from $x$ to $y$ in $n$ steps, the chain must pass through some intermediate state $z$ after $r$ steps; sum over all possible $z$. This is a direct consequence of $\Pi^n=\Pi^r\Pi^{n-r}$ and the Markov property. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- law of $X_n$ ::@:: $P[X_n=y]=\sum_{z\in E}\mu(z)\,\Pi^n(z,y)$; in vector form $\mu_n=\mu\Pi^n$ where $\mu$ is treated as a row vector. This follows from the joint law by marginalising over $X_0,\dots,X_{n-1}$. It shows that the distribution at time $n$ is obtained by multiplying the initial distribution by the $n$-step transition matrix. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->

## stationary distributions

A probability mass function $\pi$ on $E$ that is preserved by the dynamics of the chain is called a stationary distribution. If the chain is started from $\pi$, then at every future time the distribution remains $\pi$. The defining equation is a linear system: $\pi$ must satisfy $\pi=\pi\Pi$ as row vectors.

**Stationary distribution.** A probability mass function $\pi$ on $E$ is a stationary distribution for $\Pi$ if $\pi=\pi\Pi$ (as row vectors), i.e.
$$
\pi(x)=\sum_{z\in E}\pi(z)\,\Pi(z,x),\qquad\forall x\in E.
$$

In linear-algebra terms, $\pi$ is a left eigenvector of $\Pi$ for eigenvalue $1$, with positive entries summing to $1$. The equation $\pi=\pi\Pi$ says that if the chain has distribution $\pi$ at time $n$, then after one more step it still has distribution $\pi$.

The natural question is whether such a $\pi$ exists and, if so, whether it is unique. The answer depends on whether the chain can eventually reach any state from any other state — a property called irreducibility.

**Existence and uniqueness of stationary distribution.** If $\Pi^n(x,y)>0$ for all $x,y\in E$ for some $n$ (the chain is irreducible), then there exists a unique stationary distribution.

---

Flashcards for this section are as follows:

- stationary distribution ::@:: A probability mass function $\pi$ on $E$ satisfying $\pi=\pi\Pi$ (row-vector equation). In coordinates: $\pi(x)=\sum_{z\in E}\pi(z)\Pi(z,x)$ for every $x\in E$. $\pi$ is a left eigenvector of $\Pi$ for eigenvalue $1$, normalised so that $\sum_x\pi(x)=1$. Interpretation: if $X_n\sim\pi$, then $X_{n+1}\sim\pi$ — the distribution is invariant under the dynamics. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- stationary distribution / balance equation ::@:: $\pi(x)=\sum_{z\in E}\pi(z)\Pi(z,x)$ for every $x\in E$. In vector form: $\pi=\pi\Pi$. This says the probability flowing into state $x$ from all possible previous states $z$ equals the probability of being at $x$; if the chain has distribution $\pi$ at time $n$, it maintains $\pi$ after one more step. The system is linear in $\pi$, so finding $\pi$ reduces to solving an $(N\times N)$ linear system with the normalisation constraint $\sum_x\pi(x)=1$. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- irreducibility / definition ::@:: $\Pi^n(x,y)>0$ for all $x,y\in E$ for some $n$ (possibly depending on $(x,y)$). Intuition: every state can eventually reach every other state with positive probability — the chain cannot be decomposed into disjoint subsets that never communicate. A chain is irreducible iff it has a single communicating class. In a finite chain, irreducibility implies recurrence (every state is recurrent). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- irreducibility / role in stationary distribution ::@:: Irreducibility guarantees (together with aperiodicity) the existence of a unique stationary distribution and convergence to it from any initial condition. For finite state spaces, irreducibility alone suffices for existence and uniqueness (Perron-Frobenius theorem gives a unique positive left eigenvector for eigenvalue $1$). Without irreducibility there may be zero, one, or many stationary distributions. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- existence and uniqueness of stationary distribution ::@:: If $\Pi^n(x,y)>0$ for all $x,y$ (the chain is irreducible), then there exists a unique stationary distribution $\pi$. Proof sketch (finite case): by the Perron-Frobenius theorem, an irreducible non-negative matrix has a unique positive left eigenvector for eigenvalue $1$; normalising gives $\pi$. Without irreducibility there may be zero, one, or multiple stationary distributions (e.g., a chain with two absorbing states has infinitely many stationary distributions, one for each mixture of the two absorbing states). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## state classification

States can be classified by their long-run behaviour. Two fundamental properties are whether the chain eventually returns to a state (recurrence) and whether the set of states reachable from it forms a closed subset (communicating classes).

---

Flashcards for this section are as follows:

- state classification / overview ::@:: States are classified by their long-run behaviour into categories such as recurrent vs transient and by their communication structure (communicating classes). Two fundamental properties are whether the chain eventually returns to a state (recurrence) and whether the set of states reachable from it forms a closed subset. This classification determines the chain's qualitative behaviour: which states are visited infinitely often, where the chain can get trapped, and whether a unique stationary distribution exists. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- state classification / key properties ::@:: The two fundamental classification properties are (1) recurrence/transience — whether the chain returns to a state infinitely often — and (2) whether the state's communicating class is closed — whether the chain can ever escape that equivalence class. Together they determine which states are visited infinitely often, which are eventually abandoned, and where the chain can get trapped. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- state classification / why it matters ::@:: Classification reveals the chain's long-run structure: recurrent states are visited infinitely often, transient states are eventually abandoned, closed classes trap the chain, and absorbing states are single-state traps. Finding communicating classes lets us decompose the state space into irreducible building blocks, each with its own stationary distribution. This is the first step in analysing any Markov chain. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### communicating classes

Two states $x,y\in E$ **communicate**, written $x\leftrightarrow y$, if there exist $m,n\ge0$ such that $\Pi^m(x,y)>0$ and $\Pi^n(y,x)>0$. Communication is an equivalence relation (reflexive, symmetric, transitive), so it partitions the state space into disjoint **communicating classes**. A chain is **irreducible** if all states belong to the same communicating class.

The transition matrix restricted to a communicating class is itself a valid transition matrix (after possibly discarding rows and columns for states outside the class). States that belong to different classes cannot influence each other's dynamics.

To find the communicating classes, view $\Pi$ as the adjacency matrix of a directed graph on $E$ where an edge $x\to y$ exists if $\Pi(x,y)>0$. The communicating classes are the **strongly connected components** of this graph — maximal subsets where each pair is mutually reachable. Algorithms such as Kosaraju's or Tarjan's can identify them in $O(N^2)$ time for a finite chain.

---

Flashcards for this section are as follows:

- communication / definition ::@:: $x\leftrightarrow y$ if $\Pi^m(x,y)>0$ and $\Pi^n(y,x)>0$ for some $m,n\ge0$. Communication means each state can reach the other with positive probability — they are in the same directed strongly connected component of the transition graph. This is a symmetric relation: $x$ can reach $y$ and $y$ can reach $x$, possibly in different numbers of steps. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- communicating class / partition and identification ::@:: Communication is an equivalence relation (reflexive, symmetric, transitive), so it partitions $E$ into disjoint communicating classes. States in different classes cannot influence each other; the dynamics is confined within each class. To find classes: view $\Pi$ as a directed graph, then the classes are the strongly connected components (identifiable by Kosaraju's or Tarjan's algorithm in $O(N^2)$ time). <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- irreducible chain / definition ::@:: A chain is irreducible if it has a single communicating class — every state can reach every other state with positive probability. Equivalently, for all $x,y\in E$ there exists $n\ge0$ such that $\Pi^n(x,y)>0$. Irreducibility is the strongest connectivity form; it prevents decomposition into independent sub-chains and guarantees a unique stationary distribution in finite chains. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->

### closed classes

A communicating class $C\subseteq E$ is **closed** if no state inside $C$ can transition to a state outside $C$ — i.e., $\sum_{y\in C}\Pi(x,y)=1$ for every $x\in C$. A closed class is a trap: once the chain enters it, it almost surely never leaves. A closed class consisting of a single state is an **absorbing state** ( $\Pi(x,x)=1$ ). Classes that are not closed are **transient** — the chain can leave them and never return.

Closed classes play a key role in the long-run behaviour: each closed class supports its own stationary distribution (obtained by restricting $\Pi$ to the class and solving the global balance equations), and the chain eventually settles into one of these closed classes. In a finite chain, the closed classes are exactly the recurrent states; the transient states lie in non-closed classes. The chain may have multiple closed classes, each with a distinct stationary distribution, giving multiple possible limiting regimes depending on which closed class is entered.

To identify closed classes, check whether every state in the class has all its outgoing transitions staying within the class. If any state has $\Pi(x,y)>0$ for $y\notin C$, then $C$ is not closed.

---

Flashcards for this section are as follows:

- closed class / definition ::@:: A communicating class $C$ with $\sum_{y\in C}\Pi(x,y)=1$ for all $x\in C$ — once entered, the chain almost surely never leaves. A singleton closed class is an absorbing state ($\Pi(x,x)=1$). To check: verify that every state in $C$ has zero probability of transitioning to a state outside $C$. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- transient class / definition ::@:: A communicating class is transient (not closed) if some state can transition outside the class with positive probability: $\sum_{y\in C}\Pi(x,y)<1$ for at least one $x\in C$. The chain can leave a transient class permanently and never returns — states in such classes are visited only finitely many times. In a finite chain, all states in a non-closed class are transient. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- closed class / stationary-distribution role ::@:: Each closed class supports its own stationary distribution (restrict $\Pi$ to the class and solve $\pi=\pi\Pi$). The chain eventually settles into one of the closed classes it enters. If there are multiple closed classes, there are multiple stationary distributions; the limiting behaviour depends on which is entered. In finite chains, closed classes are exactly the recurrent states. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->

### recurrence and transience

A state $x$ is **recurrent** if the chain returns to $x$ infinitely often with probability $1$, when started from $x$. It is **transient** if the chain returns to $x$ only finitely many times with probability $1$. Equivalently, define the return probability $f_{xx}=P[X_n=x\text{ for some }n\ge1\mid X_0=x]$. Then:

- $x$ is recurrent iff $f_{xx}=1$.
- $x$ is transient iff $f_{xx}<1$.

For a finite-state chain, a state is recurrent iff it belongs to a closed communicating class; every state in a non-closed class is transient. This gives a simple classification procedure: find the communicating classes, identify which are closed, and the closed-class states are recurrent while the rest are transient.

**Proof sketch: series criterion.** The expected number of visits to $x$ starting from $x$ is $\sum_{n=0}^\infty\Pi^n(x,x)$. If $f_{xx}=1$, the chain returns infinitely often with probability $1$, so the expected number is infinite. If $f_{xx}<1$, the number of returns after the starting visit is geometric with success probability $f_{xx}$, giving $\mathbb{E}[\#\text{visits}]=1+f_{xx}+f_{xx}^2+\cdots=1/(1-f_{xx})<\infty$. Hence $\sum_n\Pi^n(x,x)=\infty$ iff $x$ is recurrent, and $<\infty$ iff $x$ is transient.

**Proof sketch: finite closed-class criterion.** If a communicating class $C$ is closed, the chain almost surely never leaves $C$, so the restriction of $\Pi$ to $C$ is itself a finite Markov chain. At least one state in a finite chain must be recurrent (otherwise every state would be visited only finitely often, which is impossible in a finite space), and recurrence is a class property — if one state in a communicating class is recurrent, all are. Conversely, if a class is not closed, there is positive probability of leaving it and never returning, making every state in it transient.

**Positive recurrence and null recurrence.** Define the expected return time $m_x=E[\min\{n\ge1:X_n=x\}\mid X_0=x]$. A recurrent state $x$ is:

- **positive recurrent** if $m_x<\infty$.
- **null recurrent** if $m_x=\infty$.

In finite chains, every recurrent state is positive recurrent: the expected return time is finite because the state space is finite and the chain is confined to a closed class. Null recurrence only occurs in infinite state spaces.

The distinction matters for the stationary distribution. If one exists, $\pi(x)=1/m_x$ for a positive recurrent state, while $\pi(x)=0$ for a null recurrent state — null recurrent states are visited so rarely that they contribute no mass. For irreducible chains, the type of recurrence is a class property: either all states are positive recurrent, all are null recurrent, or all are transient.

**Example.** Consider $E=\{1,2,3,4\}$ with
$$
\Pi=\begin{pmatrix}
0.5&0.5&0&0\\
0.2&0.8&0&0\\
0.1&0&0.6&0.3\\
0&0&0.4&0.6
\end{pmatrix}.
$$
The communicating classes are $\{1,2\}$ (closed, hence recurrent) and $\{3,4\}$ (also closed, recurrent). If state $3$ had a transition to state $1$, then $\{3,4\}$ would not be closed and those states would be transient — the chain could leave $\{3,4\}$ for $\{1,2\}$ but never return.

---

Flashcards for this section are as follows:

- recurrent vs transient / return-probability criterion ::@:: $x$ is recurrent if $P[\text{return to }x\mid X_0=x]=1$; transient if this probability is $<1$. Equivalently, $f_{xx}=1$ for recurrence, $f_{xx}<1$ for transience, where $f_{xx}=P[X_n=x\text{ for some }n\ge1\mid X_0=x]$. A recurrent state returns infinitely often w.p.~1; a transient state returns only finitely many times. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- recurrence / series criterion ::@:: $\sum_{n=0}^\infty\Pi^n(x,x)=\infty$ iff $x$ is recurrent, $<\infty$ iff $x$ is transient. Proof sketch: the number of returns is geometric with success probability $f_{xx}$; its expectation is $1/(1-f_{xx})$ when $f_{xx}<1$ and $\infty$ when $f_{xx}=1$, and this expectation equals $\sum_n\Pi^n(x,x)$. Hence the series diverges exactly when the state is recurrent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- recurrence / finite-chain closed-class criterion ::@:: In a finite chain, $x$ is recurrent iff its communicating class is closed. Proof sketch: if the class is closed, the restriction is a finite chain, so at least one state is recurrent; recurrence transfers within a class. If the class is not closed, there is positive probability of leaving and never returning, making every state transient. This gives a simple algorithm: find the communicating classes; the closed ones are the recurrent states. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- positive recurrence vs null recurrence ::@:: Let $m_x=E[\min\{n\ge1:X_n=x\}\mid X_0=x]$ be the expected return time. A recurrent state $x$ is positive recurrent if $m_x<\infty$ and null recurrent if $m_x=\infty$. Null recurrence only occurs in infinite state spaces; in finite chains all recurrent states are positive recurrent. For irreducible chains, recurrence type is a class property — all states share the same type. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- positive/null recurrence / stationary-distribution implication ::@:: If a stationary distribution exists, $\pi(x)=1/m_x$ for a positive recurrent state $x$, while $\pi(x)=0$ for a null recurrent state. Null recurrent states are visited so rarely in the long run that they contribute no mass to $\pi$, even though they are visited infinitely often. This is why infinite state spaces can have chains with $\pi(x)=0$ for all $x$ despite being recurrent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### absorbing states and absorbing chains

A state $a$ is **absorbing** if $\Pi(a,a)=1$. Once the chain reaches $a$, it stays there forever. An **absorbing Markov chain** has at least one absorbing state and can reach an absorbing state from every transient state (possibly in multiple steps).

Absorbing chains model many applied problems: gambler's ruin, population extinction, and absorption of a diffusing particle by a boundary.

**Fundamental matrix.** Partition the states into transient states $T$ and absorbing states $A$. The transition matrix has block form:
$$
\Pi = \begin{pmatrix} Q & R \\ 0 & I \end{pmatrix}
$$
where $Q$ ($|T|\times|T|$) gives transitions among transient states, $R$ ($|T|\times|A|$) gives one-step probabilities from transient to absorbing states, and the lower-right block $I$ ($|A|\times|A|$) reflects that absorbing states stay put.

The **fundamental matrix** $N=(I-Q)^{-1}$ captures the expected behaviour before absorption. The entry $N(x,y)$ is the expected number of visits to transient state $y$ starting from transient state $x$, and the expected time to absorption from $x$ is $\sum_{y}N(x,y)$.

**Proof sketch: why $N=(I-Q)^{-1}$.** Count the visits step by step. At step $0$, starting at a transient state, we have the identity matrix $I$ (the starting visit counts as one). From a transient state $x$, the chain moves to another transient state $y$ with probability $Q(x,y)$, and from $y$ the expected remaining visits are $N(y,\cdot)$. Hence $N = I + QN$. Solving $(I-Q)N = I$ gives $N = (I-Q)^{-1}$. The series expansion $N = I + Q + Q^2 + \cdots$ makes the interpretation clear: $Q^k(x,y)$ is the probability of being at transient $y$ after exactly $k$ steps, and summing over all $k$ gives total expected visits.

**Absorption probabilities.** Let $B$ be the $|T|\times|A|$ matrix with $B(x,a)=P[\text{chain is eventually absorbed at }a\mid X_0=x]$. Conditioning on the first step:
$$
B(x,a) = R(x,a) + \sum_{z\in T} Q(x,z)\,B(z,a),
$$
or in matrix form $B = R + QB$. Solving: $B = (I-Q)^{-1}R = NR$. Since the chain is absorbing (absorption occurs with probability 1 from every transient state), each row of $B$ sums to $1$: $\sum_{a\in A}B(x,a)=1$ for every transient $x$.

---

Flashcards for this section are as follows:

- absorbing state ::@:: A state $a$ with $\Pi(a,a)=1$. Once the chain reaches $a$, it stays forever. In an absorbing Markov chain, there is at least one absorbing state and every transient state can reach some absorbing state (possibly in multiple steps). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- absorbing chain / block decomposition ::@:: Partition states into transient $T$ and absorbing $A$. Then $\Pi=\begin{pmatrix}Q&R\\0&I\end{pmatrix}$ where $Q$ governs transitions among transient states, $R$ gives one-step probabilities from transient to absorbing, and $I$ on the absorbing states reflects that they stay put. This block form shows the chain eventually leaves $T$ and settles in $A$. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- fundamental matrix / derivation ::@:: $N=(I-Q)^{-1}$ where $Q$ is the transient submatrix. Derivation: $N=I+QN$ — the starting visit counts as $I$, then from a transient $x$ we move to transient $y$ with probability $Q(x,y)$ and expect $N(y,\cdot)$ remaining visits. Solving $(I-Q)N=I$ gives $N=(I-Q)^{-1}$. Series expansion: $N=I+Q+Q^2+\cdots$, where $Q^k(x,y)$ is the probability of being at transient $y$ after exactly $k$ steps. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- fundamental matrix / expected time to absorption ::@:: From transient state $x$, the expected time (number of steps) before absorption is $\sum_{y\in T}N(x,y)$, i.e., the row sum of $N$ for $x$. This is the total expected number of visits to all transient states before hitting an absorbing state. The chain eventually leaves the transient set with probability $1$ in an absorbing chain (the fundamental matrix is finite). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- absorption probability matrix ::@:: $B(x,a)=P[\text{absorbed at }a\mid X_0=x]$ for $x\in T,a\in A$. First-step decomposition: $B=R+QB$ (absorb in one step via $R$, or move to another transient $z$ then eventually absorb). Solving: $B=(I-Q)^{-1}R=NR$. Each row of $B$ sums to $1$ because absorption occurs with probability 1 from every transient state in an absorbing chain. Example: gambler's ruin — $B(x,0)$ and $B(x,N)$ are ruin and victory probabilities from fortune $x$. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->

## periodicity and convergence to stationarity

Periodicity controls whether the chain can converge to stationarity in the usual sense. A periodic chain oscillates and never settles into a single distribution, though its Cesàro averages still converge. The convergence theorem (Markov chain ergodic theorem) requires aperiodicity alongside irreducibility to guarantee that the chain's distribution converges from any starting point.

---

Flashcards for this section are as follows:

- periodicity / definition ::@:: The period of a state $x$ is $d(x)=\gcd\{n\ge1:\Pi^n(x,x)>0\}$. Intuitively, it is the greatest common divisor of all return-cycle lengths from $x$. A state with $d(x)=1$ is aperiodic; with $d(x)>1$ it is periodic. Example: a random walk on a bipartite graph has period $2$ because returns to the starting vertex require an even number of steps. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- periodicity / class property ::@:: Periodicity is a class property: if $x\leftrightarrow y$ then $d(x)=d(y)$. This means periodicity can be analysed at the communicating class level rather than for individual states. A chain is called aperiodic if every state has period $1$, which is equivalent to all communicating classes being aperiodic. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why periodicity matters for convergence ::@:: An irreducible aperiodic chain converges to its stationary distribution from any initial distribution (Convergence Theorem). A periodic chain cannot converge in the usual sense because its distribution oscillates (e.g., even steps vs odd steps), though the Cesàro average still converges to $\pi$. Hence aperiodicity is a necessary condition for the raw $n$-step distribution to converge. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### period

The **period** of a state $x$ is $d(x)=\gcd\{n\ge1:\Pi^n(x,x)>0\}$. If $d(x)=1$, the state is **aperiodic**; if $d(x)>1$, it is **periodic** with period $d(x)$. Intuitively, the period is the greatest common divisor of the lengths of all cycles from $x$ back to itself.

Period is a class property: if $x\leftrightarrow y$, then $d(x)=d(y)$. Hence periodicity is defined for each communicating class, not just individual states. A chain is called aperiodic if every state has period $1$.

**Example.** A random walk on a bipartite graph where each edge connects a black vertex to a white vertex has period $2$: starting from a black vertex, the walk can only be back on a black vertex after an even number of steps. The transition matrix for such a walk has the form $\Pi=\begin{pmatrix}0&A\\B&0\end{pmatrix}$, and $\Pi^2$ is block-diagonal.

---

Flashcards for this section are as follows:

- period of a state ::@:: $d(x)=\gcd\{n\ge1:\Pi^n(x,x)>0\}$. If $d(x)=1$, the state is aperiodic; if $d(x)>1$, it is periodic. Example: a random walk on a bipartite graph has period $2$ because returns to the starting vertex require an even number of steps. Period is a class property: communicating states share the same period. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- period / class property ::@:: If $x\leftrightarrow y$ then $d(x)=d(y)$. Proof: there exist $m,n$ with $\Pi^m(x,y)>0$ and $\Pi^n(y,x)>0$, so $\Pi^{m+n}(x,x)>0$ and $d(x)\mid m+n$. For any $k$ with $\Pi^k(y,y)>0$, $\Pi^{m+k+n}(x,x)>0$ so $d(x)\mid m+k+n$. Thus $d(x)\mid k$, i.e., $d(x)$ divides every return cycle length from $y$, so $d(x)\le d(y)$. Symmetry gives equality. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->

### convergence theorem

The **Convergence Theorem for Markov chains** (also called the Markov chain ergodic theorem for the finite case) states: if $\Pi$ is irreducible and aperiodic with stationary distribution $\pi$, then for every initial distribution $\mu$,
$$
\lim_{n\to\infty}\|\mu\Pi^n-\pi\|_{\text{TV}}=0,
$$
where $\|\cdot\|_{\text{TV}}$ is the **total variation distance**. For two probability distributions $\mu,\nu$ on $E$,
$$
\|\mu-\nu\|_{\text{TV}} = \frac12\sum_{x\in E}|\mu(x)-\nu(x)| = \max_{A\subseteq E}|\mu(A)-\nu(A)|.
$$
The total variation distance is the maximum difference in probability assigned to any event $A\subseteq E$, equivalently half the $L^1$ distance between the probability mass functions. It is a metric on the space of probability distributions, with values in $[0,1]$; $\|\mu-\nu\|_{\text{TV}}=0$ iff $\mu=\nu$, and $=1$ iff $\mu$ and $\nu$ have disjoint supports.

The convergence rate is geometric in the second-largest eigenvalue of $\Pi$: $\|\mu\Pi^n-\pi\|_{\text{TV}}\le C\rho^n$ for some $C>0$ and $\rho<1$, where $\rho$ is the absolute value of the second-largest eigenvalue of $\Pi$ (when the eigenvalues are real, as for reversible chains).

The intuition for the role of aperiodicity: a periodic chain (e.g., period $2$) can oscillate between two subsets of states forever, never settling into a single distribution. The distribution on even steps differs from the distribution on odd steps, though both converge to $\pi$ when averaged. The aperiodicity condition ensures that these oscillations are damped out, so the distribution itself converges, not just the Cesàro average.

**Periodic case.** If $\Pi$ is irreducible with period $d>1$, the chain does not converge to $\pi$ in the usual TV sense because the $n$-step distribution depends on $n$ modulo $d$ — it oscillates among $d$ different distributions. Instead, the **Cesàro averages** converge:
$$
\lim_{n\to\infty}\frac1n\sum_{k=1}^n\mu\Pi^k=\pi.
$$

The structural reason is that an irreducible periodic chain admits a **cyclic decomposition** of the state space: $E = C_0 \cup C_1 \cup \cdots \cup C_{d-1}$ where $\Pi$ moves from $C_i$ to $C_{i+1\bmod d}$ with probability $1$ (so $x\in C_i$ implies $\sum_{y\in C_{i+1}}\Pi(x,y)=1$). These $C_i$ are called **cyclic classes**. After $d$ steps the chain returns to the same cyclic class, so the $d$-step chain $\Pi^d$ restricted to each $C_i$ is irreducible and aperiodic on $C_i$. Consequently $\mu\Pi^{nd}$ converges to $\pi$ when restricted to the appropriate cyclic class — the distribution on steps congruent to $i$ modulo $d$ converges to $\pi$ on $C_i$ and is zero elsewhere. Averaging over all $d$ cosets recovers the full stationary distribution $\pi$.

**Example.** The two-state chain $\Pi=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ has period $2$, with cyclic classes $C_0=\{1\}$, $C_1=\{2\}$. The $2$-step chain $\Pi^2=I$ (identity) is aperiodic. From any initial $\mu$, $\mu\Pi^n$ alternates: $\mu$ for even $n$, $\mu\Pi$ for odd $n$. Neither converges individually, but $\frac1n\sum_{k=1}^n\mu\Pi^k\to(\frac12,\frac12)=\pi$.

---

Flashcards for this section are as follows:

- convergence theorem / statement (irreducible aperiodic) ::@:: If $\Pi$ is irreducible and aperiodic with stationary distribution $\pi$, then $\lim_{n\to\infty}\|\mu\Pi^n-\pi\|_{\text{TV}}=0$ for every initial distribution $\mu$. Convergence is geometric: $\|\mu\Pi^n-\pi\|_{\text{TV}}\le C\rho^n$ where $\rho<1$ is the absolute second-largest eigenvalue of $\Pi$ (assuming reversibility). The theorem guarantees that Markov chain Monte Carlo works — after enough steps the distribution is close to stationary. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- total variation distance / definition ::@:: $\|\mu-\nu\|_{\text{TV}} = \frac12\sum_{x\in E}|\mu(x)-\nu(x)| = \max_{A\subseteq E}|\mu(A)-\nu(A)|$. It is the maximum difference in probability assigned to any event, equivalently half the $L^1$ distance between probability mass functions. Values range from $0$ (identical distributions) to $1$ (disjoint supports). It is a metric on probability distributions over $E$. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- why aperiodicity is needed for convergence ::@:: A periodic chain (say period $2$) oscillates: the distribution on even and odd steps differ and may never individually equal $\pi$. Example: the two-state chain $\Pi=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ has period $2$; $\mu\Pi^n$ alternates with parity. The Cesàro average converges, but the raw distribution does not. Aperiodicity breaks this oscillation so the raw distribution converges. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- periodic case / Cesàro convergence ::@:: If $\Pi$ is irreducible with period $d>1$, $\lim_{n\to\infty}\frac1n\sum_{k=1}^n\mu\Pi^k=\pi$ even though $\mu\Pi^n$ does not converge. The raw $n$-step distribution depends on $n$ modulo $d$ and oscillates among $d$ distributions, but time-averaging smears the phases and recovers $\pi$. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- periodic case / cyclic decomposition ::@:: An irreducible period-$d$ chain partitions $E$ into $d$ cyclic classes $C_0,\dots,C_{d-1}$ where $\Pi$ moves $C_i\to C_{i+1\bmod d}$ w.p.~$1$. The $d$-step chain $\Pi^d$ restricted to each $C_i$ is aperiodic, so $\mu\Pi^{nd}$ converges to $\pi$ on each coset. Example: period-$2$ chain has $C_0,C_1$; $\Pi^2$ is aperiodic on each class. This decomposition explains why Cesàro averaging works. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->

## reversible chains and detailed balance

A Markov chain is **reversible** with respect to a distribution $\pi$ if
$$
\pi(x)\,\Pi(x,y)=\pi(y)\,\Pi(y,x),\qquad\forall x,y\in E.
$$
This condition is called **detailed balance**. If a chain satisfies detailed balance with respect to $\pi$, then $\pi$ is a stationary distribution — summing both sides over $x$ gives $\pi(y)=\sum_x\pi(x)\Pi(x,y)$.

Detailed balance is a stronger condition than stationarity. It says that in stationarity, the probability flux from $x$ to $y$ is the same as the flux from $y$ to $x$. Intuitively, the chain "looks the same" running forwards and backwards in time — the process is time-reversible.

Many important chains are reversible: random walks on undirected graphs (where $\Pi(x,y)=1/\deg(x)$ and $\pi(x)\propto\deg(x)$), the Metropolis–Hastings algorithm, and the Gibbs sampler. The reversibility property is central to the analysis of Markov chain Monte Carlo methods because it guarantees that the chain has real eigenvalues, making spectral analysis tractable.

**Example (random walk on a graph).** Let $G=(V,E)$ be an undirected graph with degree $\deg(x)$ for vertex $x$. The simple random walk has $\Pi(x,y)=1/\deg(x)$ if $(x,y)\in E$, and $0$ otherwise. The stationary distribution is $\pi(x)=\deg(x)/(2|E|)$. Detailed balance holds because $\pi(x)\Pi(x,y)=\deg(x)/(2|E|)\cdot1/\deg(x)=1/(2|E|)$ is symmetric in $x$ and $y$.

---

Flashcards for this section are as follows:

- detailed balance ::@:: $\pi(x)\Pi(x,y)=\pi(y)\Pi(y,x)$ for all $x,y\in E$. Summing over $x$ gives $\pi(y)=\sum_x\pi(x)\Pi(x,y)$, i.e., $\pi$ is stationary. Detailed balance says the probability flux from $x$ to $y$ equals the flux from $y$ to $x$ in stationarity — the chain is time-reversible. Many practical chains satisfy it (random walks on undirected graphs, Metropolis-Hastings). <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- detailed balance vs stationarity ::@:: Detailed balance is stronger than stationarity. Stationarity only requires global flux balance: $\sum_x\pi(x)\Pi(x,y)=\pi(y)$ (total flow into $y$ equals $\pi(y)$). Detailed balance requires pairwise flux balance between every pair of states. Example: a 3-state cyclic chain with $\Pi(1,2)=\Pi(2,3)=\Pi(3,1)=1$ has uniform stationary distribution but does not satisfy detailed balance (because $\pi(1)\Pi(1,2)=1/3\neq0=\pi(2)\Pi(2,1)$). <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- simple random walk on an undirected graph ::@:: $\Pi(x,y)=1/\deg(x)$ for neighbours, $0$ otherwise. Stationary distribution: $\pi(x)=\deg(x)/(2|E|)$. Detailed balance holds because $\pi(x)\Pi(x,y)=1/(2|E|)$ is symmetric. Intuition: the walk spends proportionally more time at high-degree vertices because there are more ways to arrive and stay. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->

## hitting probabilities

For a subset $A\subseteq E$, the **hitting time** is $H_A=\inf\{n\ge0:X_n\in A\}$. The **hitting probability** $h_A(x)=P[H_A<\infty\mid X_0=x]$ is the probability that the chain ever reaches $A$ starting from $x$.

Hitting probabilities satisfy a system of linear equations derived from the Markov property via **first-step decomposition**: condition on the first step $X_1$. For $x\notin A$,
$$
h_A(x)=\sum_{y\in E}\Pi(x,y)\,h_A(y),
$$
with boundary conditions $h_A(x)=1$ for $x\in A$ and $h_A(x)=0$ for $x$ in a closed class disjoint from $A$ (absorption elsewhere). This system is a **discrete Dirichlet problem**: the operator $L=I-\Pi$ acts as a discrete Laplacian, and $Lh=0$ on $A^c$ with $h$ prescribed on $A$ mirrors the classical PDE $-\Delta u=0$ with Dirichlet boundary conditions. The hitting probability is the unique bounded harmonic function satisfying the boundary values; the PDE analogy implies a maximum principle (the maximum of $h_A$ is attained on the boundary $A$) and enables comparison arguments. The system has as many unknowns as states outside $A$ and can be solved by standard linear algebra.

The hitting probability $h_A$ is the **minimal non-negative solution** to the harmonic equation — any other non-negative solution $h'$ with the same boundary values satisfies $h'(x)\ge h_A(x)$ for all $x$. Together with the Dirichlet-problem structure (which guarantees uniqueness of bounded solutions when absorption into $A$ occurs with probability 1), this characterisation gives a practical **guess-and-verify method**: if we can find any function $f$ satisfying $f(x)=\sum_y\Pi(x,y)f(y)$ for $x\notin A$, $f|_A=1$, and $f=0$ on closed classes disjoint from $A$, then $f$ must equal $h_A$. No path-sum computation or further verification about the chain's structure is needed — simply checking that $f$ satisfies the equation and boundary values suffices. This is especially useful for structured state spaces such as birth-death chains, where a natural candidate can be proposed and verified by substitution.

---

Flashcards for this section are as follows:

- hitting probability / harmonic equation ::@:: $h_A(x)=P[H_A<\infty\mid X_0=x]$, the probability of ever reaching $A$ from $x$. For $x\notin A$: $h_A(x)=\sum_y\Pi(x,y)h_A(y)$ (first-step decomposition). Boundary conditions: $h_A(x)=1$ for $x\in A$, $h_A(x)=0$ for $x$ in closed classes disjoint from $A$. This linear system uniquely determines $h_A$ (Dirichlet problem for the Markov chain). <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- hitting probability / minimal non-negative solution ::@:: $h_A$ is the minimal non-negative solution ($h'\ge h_A$ for any other non-negative solution $h'$). When absorption into $A$ occurs with probability 1, the harmonic equation on $A^c$ with $h|_A=1$ has a unique bounded solution, so any candidate satisfying the recurrence and boundary values must equal $h_A$ — a guess-and-verify method useful for birth-death chains and other structured state spaces. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- hitting probability / Dirichlet problem ::@:: $Lh=0$ on $A^c$ with $h|_A=1$, where $L=I-\Pi$ is the discrete Laplacian. This mirrors $-\Delta u=0$ with Dirichlet boundary conditions in PDE theory. Implication: the maximum principle holds (the hitting probability attains its maximum on the boundary $A$), comparison arguments apply, and the solution is unique when absorption into $A$ occurs with probability 1. The name comes from the classical Dirichlet problem in potential theory. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->

### Gambler's ruin — hitting probabilities

**Example (gambler's ruin — hitting probabilities).** A gambler starts with $k$ dollars and bets $1$ per round, winning with probability $p$ and losing with $q=1-p$. The game stops when the gambler reaches $0$ (ruin) or $N$ (target). The hitting probability $h(k)=P[\text{reach }N\text{ before }0\mid X_0=k]$ satisfies the first-step decomposition
$$
h(k)=p\,h(k+1)+q\,h(k-1),\qquad h(0)=0,\;h(N)=1.
$$
Solving gives closed-form formulas:

- If $p\neq q$ (biased game): $\displaystyle h(k)=\frac{1-(q/p)^k}{1-(q/p)^N}$.
- If $p=q=1/2$ (fair game): $\displaystyle h(k)=\frac{k}{N}$.

**Solution method.** The recurrence rearranges to $p\,h(k+1)-h(k)+q\,h(k-1)=0$. Trying $h(k)=\lambda^k$ gives the characteristic equation $p\lambda^2-\lambda+q=0$ with roots
$$
\lambda=\frac{1\pm\sqrt{1-4pq}}{2p}.
$$
Since $q=1-p$, the discriminant $1-4pq=1-4p(1-p)=(1-2p)^2$, so the roots simplify to $\lambda=1$ and $\lambda=q/p$ (distinct for $p\neq q$, repeated at $\lambda=1$ for $p=q$). The general solution is
$$
h(k)=
\begin{cases}
A+B\,(q/p)^k, & p\neq q,\\[4pt]
A+Bk, & p=q.
\end{cases}
$$
Applying $h(0)=0$, $h(N)=1$ determines $A$ and $B$, yielding the formulas above. This method generalises to any birth-death chain with constant coefficients.

**Interpretation.** For a fair game, the winning probability is simply $k/N$, the fraction of the target fortune already held. For a biased game with $p<q$ (odds against you), $q/p>1$ and as $N\to\infty$, $h(k)\to0$ — eventual ruin is almost certain. Even a small disadvantage makes long-run survival have probability approaching 0 against an infinitely rich opponent.

---

Flashcards for this section are as follows:

- gambler's ruin / hitting probabilities ::@:: On $\{0,\dots,N\}$ with $\Pi(i,i+1)=p$, $\Pi(i,i-1)=q$, absorbing at $0,N$. $h(k)=P[\text{reach }N\mid X_0=k]$ satisfies $h(k)=p\,h(k+1)+q\,h(k-1)$, $h(0)=0$, $h(N)=1$. Solution: $h(k)=\frac{1-(q/p)^k}{1-(q/p)^N}$ ($p\neq q$) or $k/N$ ($p=q$). This illustrates the linear-equation method for hitting probabilities and the gambler's ruin difference equation. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- gambler's ruin / hitting probabilities solution method ::@:: Solve $h(k)=p\,h(k+1)+q\,h(k-1)$ with $h(0)=0$, $h(N)=1$. This is a linear homogeneous second-order difference equation. Characteristic equation: $p\lambda^2-\lambda+q=0$, roots $1$ and $q/p$. General solution: $h(k)=A+B(q/p)^k$ ($p\neq q$) or $h(k)=A+Bk$ ($p=q$). Apply $h(0)=0$, $h(N)=1$ to find $A,B$. Generalises to any birth-death chain with constant coefficients. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- gambler's ruin / hitting probabilities limiting behavior ::@:: For $p<q$ (odds against the gambler), $h(k)\to0$ as $N\to\infty$ — eventual ruin is almost certain against an infinitely rich opponent. For a fair game ($p=q$), $h(k)=k/N$ is simply the fraction of target already held. This is why casinos profit: even a small disadvantage makes long-run survival have probability approaching 0. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->

## expected hitting times

**Expected hitting times** $g_A(x)=E[H_A\mid X_0=x]$ satisfy a similar first-step decomposition. For $x\notin A$,
$$
g_A(x)=1+\sum_{y\in E}\Pi(x,y)\,g_A(y),
$$
with $g_A(x)=0$ for $x\in A$. The "$+1$" accounts for the step just taken. This system always has a unique solution when the chain is irreducible and $A$ is non-empty. In matrix form, $g_A = \mathbf 1_{A^c} + \Pi g_A$, where $\mathbf 1_{A^c}$ is the indicator vector of the complement of $A$. This is a **discrete Poisson equation**: $Lg_A = \mathbf 1_{A^c}$ with $g_A|_A=0$, where the same discrete Laplacian $L=I-\Pi$ now has a non-zero source term — the discrete analogue of $-\Delta u = f$ with Dirichlet boundary conditions. The $+1$ on $A^c$ is the source term, representing the unit step cost incurred each time the chain moves while still outside $A$. The solution is unique because $I-Q$ (the restriction of $L$ to $A^c$) is invertible.

---

Flashcards for this section are as follows:

- expected hitting time / first-step decomposition ::@:: $g_A(x)=E[H_A\mid X_0=x]$. For $x\notin A$: $g_A(x)=1+\sum_y\Pi(x,y)g_A(y)$, with $g_A(x)=0$ for $x\in A$. The "$+1$" accounts for the current step. In matrix form: $g_A = \mathbf 1_{A^c} + \Pi g_A$ (Poisson equation). For irreducible finite chains and non-empty $A$, the system has a unique solution. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- expected hitting time / Poisson equation ::@:: $Lg_A = \mathbf 1_{A^c}$ with $g_A|_A=0$, where $L=I-\Pi$ is the discrete Laplacian. This mirrors $-\Delta u = f$ with Dirichlet boundary conditions. The source term $\mathbf 1_{A^c}$ (constant $1$ on $A^c$) represents the unit step cost incurred each time the chain moves while still outside $A$. The solution is unique because $I-Q$ (the restriction of $L$ to $A^c$) is invertible; finiteness follows from the absorbing structure. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->

### Gambler's ruin — expected duration

**Example (gambler's ruin — expected duration).** Let $g(k)=E[H_{\{0,N\}}\mid X_0=k]$ be the expected number of rounds until absorption. First-step decomposition gives
$$
g(k)=1+p\,g(k+1)+q\,g(k-1),\qquad g(0)=g(N)=0.
$$
The "$+1$" counts the current step. Solving gives:

- If $p=q=1/2$ (fair game): $\displaystyle g(k)=k(N-k)$.
- If $p\neq q$ (biased game): $\displaystyle g(k)=\frac{k}{q-p}-\frac{N}{q-p}\cdot\frac{1-(q/p)^k}{1-(q/p)^N}$.

**Solution method.** The equation is a non-homogeneous second-order difference equation. The homogeneous part $p\,g_h(k+1)-g_h(k)+q\,g_h(k-1)=0$ is identical to the hitting-probability equation, so $g_h(k)=A+B\,(q/p)^k$ ($p\neq q$) or $g_h(k)=A+Bk$ ($p=q$). For a particular solution, use undetermined coefficients:

- $p\neq q$: try $g_p(k)=Ck$. Substituting into $g(k)=1+p\,g(k+1)+q\,g(k-1)$ gives $Ck=1+pC(k+1)+qC(k-1)$, which simplifies to $Ck=1+Ck+C(p-q)$, so $C=1/(q-p)$.
- $p=q$: try $g_p(k)=Ck^2$. Substituting gives $Ck^2=1+\frac{1}{2}C(k+1)^2+\frac{1}{2}C(k-1)^2$, which simplifies to $Ck^2=1+Ck^2+C$, so $C=-1$.
Then $g=g_h+g_p$; applying $g(0)=g(N)=0$ determines $A$ and $B$, yielding the formulas above.

**Interpretation.** For a fair game, $g(k)=k(N-k)$ grows like $O(N^2)$ for $k\approx N/2$ — games can last very long. For a biased game, as $N\to\infty$,
$$
g(k)\to\frac{k}{q-p},
$$
a finite bound independent of $N$. Even against an enormously rich opponent, a disadvantaged gambler loses quickly on average. As $p\to q$, the bound diverges, consistent with the fair-game $O(N^2)$ scaling.

---

Flashcards for this section are as follows:

- gambler's ruin / expected duration ::@:: $g(k)=E[H_{\{0,N\}}\mid X_0=k]$ satisfies $g(k)=1+p\,g(k+1)+q\,g(k-1)$, $g(0)=g(N)=0$. Solution: $g(k)=k(N-k)$ ($p=q$) or $g(k)=\frac{k}{q-p}-\frac{N}{q-p}\cdot\frac{1-(q/p)^k}{1-(q/p)^N}$ ($p\neq q$). Insight: a fair game's expected duration is $O(N^2)$, while a biased game's is bounded as $N\to\infty$ — bias makes the game end quickly on average regardless of stakes. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- gambler's ruin / expected duration solution method ::@:: Solve $g(k)=1+p\,g(k+1)+q\,g(k-1)$ with $g(0)=g(N)=0$, a non-homogeneous difference equation. Homogeneous solution: same as hitting probability. Particular solution (undetermined coefficients): try $Ck$ for $p\neq q$ (gives $C=1/(q-p)$), try $Ck^2$ for $p=q$ (gives $C=-1$). Then $g=g_h+g_p$; apply boundary conditions. Standard method for linear difference equations with constant coefficients. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
- gambler's ruin / expected duration limiting behavior ::@:: For a fair game ($p=q$), $g(k)=k(N-k)$ grows like $O(N^2)$ as $N\to\infty$ — games can last extremely long. For a biased game ($p\neq q$), $g(k)\to k/(q-p)$ as $N\to\infty$, a finite bound — the disadvantaged gambler loses quickly on average regardless of the opponent's wealth. As $p\to q$, the bound diverges, consistent with the fair-game $O(N^2)$ scaling. <!-- check: ignore-line[no_soft_wrap_list]: flashcard must be single-line -->
