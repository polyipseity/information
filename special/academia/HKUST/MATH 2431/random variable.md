---
aliases:
  - random variable
  - random variables
  - real random variable
  - real random variables
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/random_variable
  - language/in/English
---

# random variable

A random variable is the device that lets us keep only the aspect of an experiment that matters for a question. Instead of working directly with the full sample space, one applies a measurable function to outcomes and studies the induced probability law on a usually much simpler state space. This is how one passes, for example, from the $36$ equally likely outcomes of two dice to the $11$ possible values of their sum.

---

Flashcards for this section are as follows:

- overview ::@:: A random variable is a measurable function that extracts the quantity of interest from an experiment and thereby transfers probability from the original sample space to a simpler state space.

## sum of two dice

Consider two fair dice. The natural probability space is $\Omega=\{1,2,3,4,5,6\}^2$, $\mathcal{F}=\mathcal{P}(\Omega)$, and $P=\mathrm{U}(\Omega)$, so every outcome $\omega=(\omega_1,\omega_2)$ has probability $1/36$. If we are interested only in the sum of the two dice, we define $S(\omega)=\omega_1+\omega_2$.

Then $S$ takes values in $\{2,3,\ldots,12\}$. For instance, $P[S=3]=P[\{\omega\in\Omega:S(\omega)=3\}]=P[\{(1,2),(2,1)\}]=\frac{2}{36}=\frac{1}{18}$.

The point is that the event “the sum equals $3$ ” is described as a preimage under $S$. More generally, for any Borel set $B\subseteq\mathbb{R}$, one has $\{S\in B\}=\{\omega\in\Omega:S(\omega)\in B\}=S^{-1}(B)$.

This is exactly the pattern behind the general definition: a random variable is a function whose preimages of measurable sets are events.

---

Flashcards for this section are as follows:

- two-dice sum model ::@:: In the two-dice example, the full sample space is $\Omega=\{1,2,3,4,5,6\}^2$ with $36$ equally likely outcomes, while the sum is captured by the function $S(\omega)=\omega_1+\omega_2$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- probability that the sum is $3$ ::@:: In the two-dice model, $P[S=3]=P[\{(1,2),(2,1)\}]=2/36=1/18$.
- why the sum example motivates the definition ::@:: The event “the random variable lies in a Borel set $B$ ” is the preimage $S^{-1}(B)$, so the quantity of interest is usable in probability only when those preimages are events. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## measurable functions and random variables

Let $(\Omega,\mathcal{F})$ and $(E,\mathcal{E})$ be measurable spaces, meaning that $\mathcal{F}$ is a sigma-algebra on the outcome space $\Omega$ and $\mathcal{E}$ is a sigma-algebra on the value space $E$. A function $f\colon\Omega\to E$ is called measurable from $(\Omega,\mathcal{F})$ to $(E,\mathcal{E})$ if $f^{-1}(B)\in\mathcal{F}$ for every measurable set $B\in\mathcal{E}$.

The notation is worth unpacking because this is standard probability language. The letter $B$ here refers to a measurable subset of the target or value space $E$, not to a subset of $\Omega$. The statement that $f$ is $(\mathcal{F},\mathcal{E})$-measurable means exactly that whenever one picks an admissible target event $B\in\mathcal{E}$, the set of outcomes that land in $B$, namely $f^{-1}(B)=\{\omega\in\Omega:f(\omega)\in B\}$, belongs to the source sigma-algebra $\mathcal{F}$.

If $(\Omega,\mathcal{F},P)$ is a probability space, then a measurable function $X\colon\Omega\to E$ from $(\Omega,\mathcal{F})$ to $(E,\mathcal{E})$ is called an $E$-valued random variable. The definition depends only on the sigma-algebra $\mathcal{F}$, not on the particular probability measure $P$. This matters conceptually: measurability says which questions about $X$ can be expressed as events, whereas the measure $P$ only assigns numerical probabilities once those events are already available.

Another useful viewpoint is that one may replace the large target space $E$ by the smaller image $\Omega_X=\{X(\omega):\omega\in\Omega\}$.

If $\Omega_X$ is countable, then one usually calls $X$ a discrete random variable. The motivation is that once only countably many values can occur, the whole law of $X$ is determined by the point probabilities $P[X=x]$ for $x\in\Omega_X$. So one no longer needs the full target sigma-algebra on a large space such as $\mathbb{R}$; one can compress the problem to a countable state space where the law is just a probability mass function on the actually attained values.

This is why the countable-image viewpoint is useful rather than merely formal. In the original experiment, many different outcomes $\omega$ may lead to the same observed value $X(\omega)$. Passing to $\Omega_X$ merges all those outcomes into a single state labeled by that value. Probabilistically, nothing is lost if the question concerns only $X$, because all such questions can be answered from the probabilities attached to the states in $\Omega_X$.

---

Flashcards for this section are as follows:

- measurable function ::@:: A function $f\colon(\Omega,\mathcal{F})\to(E,\mathcal{E})$ is measurable if for every measurable set $B\in\mathcal{E}$ in the target space, the preimage $f^{-1}(B)=\{\omega\in\Omega:f(\omega)\in B\}$ belongs to $\mathcal{F}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- random variable on a measurable space ::@:: If $(\Omega,\mathcal{F},P)$ is a probability space and $(E,\mathcal{E})$ is a measurable space, then a measurable map $X\colon\Omega\to E$ from $(\Omega,\mathcal{F})$ to $(E,\mathcal{E})$ is an $E$-valued random variable. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why measurability is the right requirement ::@:: Measurability guarantees that every event of the form $\{X\in B\}=X^{-1}(B)$, where $B$ is a measurable set in the value space, belongs to $\mathcal{F}$, so its probability is well defined. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- dependence on $\mathcal{F}$ not on $P$ ::@:: Whether $X$ is a random variable depends only on the sigma-algebra $\mathcal{F}$, because measurability asks only whether preimages of measurable sets belong to $\mathcal{F}$; the probability measure $P$ comes in only after that.
- image-space viewpoint ::@:: The image $\Omega_X=\{X(\omega):\omega\in\Omega\}$ is the set of values actually attained by $X$; if it is countable, then $X$ is called a discrete random variable, because the law is then determined by the point probabilities on those countably many attained values. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## real random variables

A real random variable is simply a measurable map $X\colon(\Omega,\mathcal{F})\to(\mathbb{R},\mathcal{B}(\mathbb{R}))$.

The Borel sigma-algebra is used because probabilities on the real line are defined on Borel sets. In practice one often checks measurability through the half-line criterion: $X$ is real-valued and measurable if and only if $\{X\le a\}\in\mathcal{F}$ for every $a\in\mathbb{R}$.

This criterion is natural because the sets $(-\infty,a]$ form a pi-system generating $\mathcal{B}(\mathbb{R})$. If one defines $\mathcal{M}:=\{A\in\mathcal{B}(\mathbb{R}):X^{-1}(A)\in\mathcal{F}\}$, then $\mathcal{M}$ is a sigma-algebra on $\mathbb{R}$. So once all left half-lines belong to $\mathcal{M}$, the generator argument behind Dynkin's pi-lambda theorem shows that $\mathcal{M}$ must contain the whole Borel sigma-algebra. In other words, checking preimages of the generating half-lines already forces the preimages of all Borel sets to be events.

If $\Omega$ is countable and $\mathcal{F}=\mathcal{P}(\Omega)$, then every function $X\colon\Omega\to\mathbb{R}$ is automatically a random variable. Indeed, for any Borel set $A\subseteq\mathbb{R}$, the preimage $X^{-1}(A)$ is simply some subset of $\Omega$, and every subset of $\Omega$ lies in the full power set. This explains why measurability is invisible in elementary discrete examples and becomes important only once the event sigma-algebra is smaller than the whole power set.

This also helps expose a common misconception: not every function into $\mathbb{R}$ is automatically a random variable. A very simple counterexample is $\Omega=\mathbb{R}$ with the trivial sigma-algebra $\mathcal{F}=\{\varnothing,\mathbb{R}\}$ and $X(\omega)=\omega$. Then $\{X\le 0\}=(-\infty,0]$, which is not in $\mathcal{F}$, so $X$ is not measurable.

Another common misconception is that a discrete random variable must come from a countable sample space. Not so: one can take the uncountable sample space $\Omega=[0,1]$ with its Borel sigma-algebra and define $X(\omega)=\mathbf{1}_{[1/2,1]}(\omega)$. Then $X$ takes only the two values $0$ and $1$, so it is a discrete random variable even though the underlying sample space is uncountable.

---

Flashcards for this section are as follows:

- real random variable ::@:: A real random variable is a measurable map $X\colon(\Omega,\mathcal{F})\to(\mathbb{R},\mathcal{B}(\mathbb{R}))$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- half-line criterion ::@:: A real-valued function $X$ is a random variable iff $\{X\le a\}\in\mathcal{F}$ for every $a\in\mathbb{R}$, because the left half-lines $(-\infty,a]$ form a generating pi-system for $\mathcal{B}(\mathbb{R})$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the half-line criterion works ::@:: If $\mathcal{M}=\{A\in\mathcal{B}(\mathbb{R}):X^{-1}(A)\in\mathcal{F}\}$, then $\mathcal{M}$ is a sigma-algebra containing every left half-line. Since those half-lines form a generating pi-system, the Dynkin pi-lambda generator idea forces $\mathcal{M}=\mathcal{B}(\mathbb{R})$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- every function is measurable on a countable full-power-set space ::@:: If $\Omega$ is countable and $\mathcal{F}=\mathcal{P}(\Omega)$, then every function $X\colon\Omega\to\mathbb{R}$ is a random variable, because every preimage $X^{-1}(A)$ is just a subset of $\Omega$ and therefore belongs to $\mathcal{F}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- not every function into $\mathbb{R}$ is automatically measurable ::@:: Counterexample: take $\Omega=\mathbb{R}$, $\mathcal{F}=\{\varnothing,\mathbb{R}\}$, and $X(\omega)=\omega$. Then $\{X\le 0\}=(-\infty,0]$, which is not an event in $\mathcal{F}$, so $X$ is not a random variable.
- discrete random variable does not require countable sample space ::@:: Counterexample: on the uncountable sample space $\Omega=[0,1]$, the function $X(\omega)=\mathbf{1}_{[1/2,1]}(\omega)$ takes only the two values $0$ and $1$, so $X$ is discrete even though $\Omega$ is uncountable. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## law and cumulative distribution

If $X\colon(\Omega,\mathcal{F},P)\to(S,\mathcal{S})$ is an $S$-valued random variable, its _law_ under $P$ is the probability measure $P_X$ on $(S,\mathcal{S})$ defined by $P_X[B]=P[X^{-1}(B)]$ for $B\in\mathcal{S}$.

This is the measure-theoretic way of saying that $X$ transports the original probability measure from the outcome space to the value space. Instead of asking for probabilities of underlying outcomes, one asks for probabilities of observable values.

When $X$ is real-valued, $P_X$ is a probability measure on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$. Its cumulative distribution function is denoted by $F_X(x):=P[X\le x]=P_X[(-\infty,x]]$.

So the cumulative distribution function of a random variable is simply the cumulative distribution function of its law. This is the precise link between the new chapter on random variables and the previous chapter on cumulative distribution functions.

This also clarifies what it means for two real random variables to have the same distribution. The correct statement is $P_X=P_Y$ as probability measures on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$, or equivalently $F_X(x)=F_Y(x)$ for every $x\in\mathbb{R}$. The equivalence between equality of laws and equality of cumulative distribution functions is another direct application of Dynkin's pi-lambda theorem: equality of the cumulative distribution functions means agreement on the generating pi-system of left half-lines, and the theorem upgrades that to agreement on all Borel sets. This does not require $X(\omega)=Y(\omega)$ pointwise, and it does not even require $X$ and $Y$ to be defined on the same probability space.

A simple counterexample keeps everything on one probability space. Let $\Omega=\{H,T\}$ with $P[H]=P[T]=1/2$, and define $X(H)=1$, $X(T)=0$, while $Y(H)=0$, $Y(T)=1$. Then both $X$ and $Y$ have the Bernoulli $(1/2)$ law, so they have the same distribution, but they are never equal pointwise: $X(\omega)=1-Y(\omega)$ for every $\omega$.

If the image $\Omega_X$ is countable, then one may also view $P_X$ as a probability measure on $(\Omega_X,\mathcal{P}(\Omega_X))$. This is often the most efficient viewpoint in discrete problems: instead of tracking the whole underlying experiment, one keeps only the countably many values the observable can actually take and the masses assigned to them.

The motivation is exactly the same as in the dice-sum example. The original sample space for two dice has $36$ points, but the sum random variable has only $11$ possible values. Once the question is about the sum rather than the detailed ordered pair, the probability problem becomes a problem on that smaller image space. The countable-image law is the general version of this compression principle.

Standard notation writes $X\sim P_X$, and one often abbreviates this further by naming the law, for example $X\sim\mathrm{Bin}(n,p)$ or $X\sim\mathrm{N}(\mu,\sigma^2)$. If the law $P_X$ admits a density, then one calls $X$ a continuous random variable; if the image is countable, one calls it a discrete random variable. In either case, the law is what matters probabilistically.

---

Flashcards for this section are as follows:

- law of a random variable ::@:: If $X\colon(\Omega,\mathcal{F},P)\to(S,\mathcal{S})$ is measurable, its law is the probability measure $P_X$ on $(S,\mathcal{S})$ defined by $P_X[B]=P[X^{-1}(B)]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- law as transported probability ::@:: The law $P_X$ is the probability measure obtained by transporting the original measure $P$ from the outcome space to the value space through the map $X$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- cumulative distribution function of a real random variable ::@:: For a real random variable $X$, the cumulative distribution function is $F_X(x)=P[X\le x]=P_X[(-\infty,x]]$; it is the cumulative distribution function of the law of $X$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- same distribution of real random variables ::@:: Real random variables $X$ and $Y$ have the same distribution exactly when their laws are equal, $P_X=P_Y$, equivalently when their cumulative distribution functions satisfy $F_X(x)=F_Y(x)$ for every $x$; the equivalence uses agreement on the generating pi-system of half-lines and Dynkin's pi-lambda theorem. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- same distribution does not mean pointwise equality ::@:: Counterexample: on $\Omega=\{H,T\}$ with fair-coin measure, let $X(H)=1$, $X(T)=0$, $Y(H)=0$, and $Y(T)=1$. Then both have the Bernoulli $(1/2)$ law, so they have the same distribution, but $X(\omega)\neq Y(\omega)$ for every outcome $\omega$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the law reduces complexity ::@:: The law forgets the detailed underlying outcomes and keeps only the probabilities of the values of $X$, which is why random variables reduce a complicated experiment to a simpler value-space model. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- countable-image law ::@:: If the image $\Omega_X$ is countable, then one may regard $P_X$ as a probability measure on $(\Omega_X,\mathcal{P}(\Omega_X))$; the point is that the law is then completely described by the masses $P_X[\{x\}]=P[X=x]$ on the countably many values that can actually occur. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- notation $X\sim P_X$ ::@:: The notation $X\sim P_X$ means that the law of $X$ is the probability measure $P_X$; in practice one often abbreviates further by naming the distribution, such as $X\sim\mathrm{Bin}(n,p)$.
- discrete versus continuous random variable ::@:: A random variable is called discrete when its image is countable and continuous when its law admits a density; in both cases the probabilistic content is carried by the law.
