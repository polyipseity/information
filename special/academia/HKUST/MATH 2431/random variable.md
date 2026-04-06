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

The point is that the event "the sum equals $3$ " is described as a preimage under $S$. More generally, for any Borel set $B\subseteq\mathbb{R}$, one has $\{S\in B\}=\{\omega\in\Omega:S(\omega)\in B\}=S^{-1}(B)$.

This is exactly the pattern behind the general definition: a random variable is a function whose preimages of measurable sets are events.

---

Flashcards for this section are as follows:

- two-dice sum model ::@:: In the two-dice example, the full sample space is $\Omega=\{1,2,3,4,5,6\}^2$ with $36$ equally likely outcomes, while the sum is captured by the function $S(\omega)=\omega_1+\omega_2$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- probability that the sum is $3$ ::@:: In the two-dice model, $P[S=3]=P[\{(1,2),(2,1)\}]=2/36=1/18$.
- why the sum example motivates the definition ::@:: The event "the random variable lies in a Borel set $B$ " is the preimage $S^{-1}(B)$, so the quantity of interest is usable in probability only when those preimages are events. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## measurable functions and random variables

Let $(\Omega,\mathcal{F})$ and $(E,\mathcal{E})$ be measurable spaces, meaning that $\mathcal{F}$ is a sigma-algebra on the outcome space $\Omega$ and $\mathcal{E}$ is a sigma-algebra on the value space $E$. A function $f\colon\Omega\to E$ is called measurable from $(\Omega,\mathcal{F})$ to $(E,\mathcal{E})$ if $f^{-1}(B)\in\mathcal{F}$ for every measurable set $B\in\mathcal{E}$.

The notation is worth unpacking because this is standard probability language. The letter $B$ here refers to a measurable subset of the target or value space $E$, not to a subset of $\Omega$. The statement that $f$ is $(\mathcal{F},\mathcal{E})$-measurable means exactly that whenever one picks an admissible target event $B\in\mathcal{E}$, the set of outcomes that land in $B$, namely $f^{-1}(B)=\{\omega\in\Omega:f(\omega)\in B\}$, belongs to the source sigma-algebra $\mathcal{F}$.

If $(\Omega,\mathcal{F},P)$ is a probability space, then a measurable function $X\colon\Omega\to E$ from $(\Omega,\mathcal{F})$ to $(E,\mathcal{E})$ is called an $E$-valued random variable. The definition depends only on the sigma-algebra $\mathcal{F}$, not on the particular probability measure $P$. This matters conceptually: measurability says which questions about $X$ can be expressed as events, whereas the measure $P$ only assigns numerical probabilities once those events are already available.

Another useful viewpoint is that one may replace the large target space $E$ by the smaller image $\Omega_X=\{X(\omega):\omega\in\Omega\}$. This set is called the _image_ or _range_ of the random variable; it is the set of values that can actually be observed.

Measurability is also stable under composition. If $f\colon(\Omega,\mathcal{F})\to(G,\mathcal{G})$ and $g\colon(G,\mathcal{G})\to(H,\mathcal{H})$ are measurable, then $g\circ f$ is measurable because for every $A\in\mathcal{H}$ one has $(g\circ f)^{-1}(A)=f^{-1}(g^{-1}(A))\in\mathcal{F}$. In particular, if $X$ is a real random variable and $h\colon\mathbb{R}\to\mathbb{R}$ is Borel-measurable—hence in particular if $h$ is continuous—then $h(X)$ is again a random variable. Constant maps are always measurable, and indicator functions are the simplest nontrivial examples: for an event $A\in\mathcal{F}$, the map $\mathbf{1}_A$ is measurable because the preimages of $\{1\}$ and $\{0\}$ are exactly $A$ and $A^c$.

If $\Omega_X$ is countable, then one usually calls $X$ a discrete random variable. The motivation is that once only countably many values can occur, the whole law of $X$ is determined by the point probabilities $P[X=x]$ for $x\in\Omega_X$. So one no longer needs the full target sigma-algebra on a large space such as $\mathbb{R}$; one can compress the problem to a countable state space where the law is just a probability mass function on the actually attained values.

This is why the countable-image viewpoint is useful rather than merely formal. In the original experiment, many different outcomes $\omega$ may lead to the same observed value $X(\omega)$. Passing to $\Omega_X$ merges all those outcomes into a single state labeled by that value. Probabilistically, nothing is lost if the question concerns only $X$, because all such questions can be answered from the probabilities attached to the states in $\Omega_X$.

---

Flashcards for this section are as follows:

- measurable function ::@:: A function $f\colon(\Omega,\mathcal{F})\to(E,\mathcal{E})$ is measurable if for every measurable set $B\in\mathcal{E}$ in the target space, the preimage $f^{-1}(B)=\{\omega\in\Omega:f(\omega)\in B\}$ belongs to $\mathcal{F}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- random variable on a measurable space ::@:: If $(\Omega,\mathcal{F},P)$ is a probability space and $(E,\mathcal{E})$ is a measurable space, then a measurable map $X\colon\Omega\to E$ from $(\Omega,\mathcal{F})$ to $(E,\mathcal{E})$ is an $E$-valued random variable. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why measurability is the right requirement ::@:: Measurability guarantees that every event of the form $\{X\in B\}=X^{-1}(B)$, where $B$ is a measurable set in the value space, belongs to $\mathcal{F}$, so its probability is well defined. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- dependence on $\mathcal{F}$ not on $P$ ::@:: Whether $X$ is a random variable depends only on the sigma-algebra $\mathcal{F}$, because measurability asks only whether preimages of measurable sets belong to $\mathcal{F}$; the probability measure $P$ comes in only after that.
- composition of measurable maps ::@:: If $f\colon(\Omega,\mathcal{F})\to(G,\mathcal{G})$ and $g\colon(G,\mathcal{G})\to(H,\mathcal{H})$ are measurable, then $g\circ f$ is measurable because for every $A\in\mathcal{H}$, first $g^{-1}(A)\in\mathcal{G}$ and then $f^{-1}(g^{-1}(A))\in\mathcal{F}$, while $(g\circ f)^{-1}(A)=f^{-1}(g^{-1}(A))$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- image or range of a random variable ::@:: The image (or range) of $X$ is $\Omega_X=\{X(\omega):\omega\in\Omega\}$, the set of values that can actually occur. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- continuous function of a random variable ::@:: If $X$ is a real random variable and $h\colon\mathbb{R}\to\mathbb{R}$ is continuous, then $h(X)$ is again a random variable because continuity implies Borel measurability: for each Borel $B$, $(h\circ X)^{-1}(B)=X^{-1}(h^{-1}(B))$ and $h^{-1}(B)$ is Borel. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- indicator random variable ::@:: For an event $A\in\mathcal{F}$, the indicator $\mathbf{1}_A$ is measurable and takes only values $0,1$: $\mathbf{1}_A^{-1}(\{1\})=A$, $\mathbf{1}_A^{-1}(\{0\})=A^c$, and equivalently each half-line event $\{\mathbf{1}_A\le x\}$ is one of $\varnothing$, $A^c$, or $\Omega$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- image-space viewpoint ::@:: The image $\Omega_X=\{X(\omega):\omega\in\Omega\}$ is the set of values actually attained by $X$; if it is countable, then $X$ is called a discrete random variable, because the law is then determined by the point probabilities on those countably many attained values. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## real random variables

A real random variable is simply a measurable map $X\colon(\Omega,\mathcal{F})\to(\mathbb{R},\mathcal{B}(\mathbb{R}))$.

The Borel sigma-algebra is used because probabilities on the real line are defined on Borel sets. In practice one often checks measurability through the half-line criterion: $X$ is real-valued and measurable if and only if $\{X\le a\}\in\mathcal{F}$ for every $a\in\mathbb{R}$.

This criterion is natural because the sets $(-\infty,a]$ form a pi-system generating $\mathcal{B}(\mathbb{R})$. If one defines $\mathcal{M}:=\{A\in\mathcal{B}(\mathbb{R}):X^{-1}(A)\in\mathcal{F}\}$, then $\mathcal{M}$ is a sigma-algebra on $\mathbb{R}$. So once all left half-lines belong to $\mathcal{M}$, the generator argument behind Dynkin's pi-lambda theorem shows that $\mathcal{M}$ must contain the whole Borel sigma-algebra. In other words, checking preimages of the generating half-lines already forces the preimages of all Borel sets to be events.

If $\Omega$ is countable and $\mathcal{F}=\mathcal{P}(\Omega)$, then every function $X\colon\Omega\to\mathbb{R}$ is automatically a random variable. Indeed, for any Borel set $A\subseteq\mathbb{R}$, the preimage $X^{-1}(A)$ is simply some subset of $\Omega$, and every subset of $\Omega$ lies in the full power set. This explains why measurability is invisible in elementary discrete examples and becomes important only once the event sigma-algebra is smaller than the whole power set.

This also helps expose a common misconception: not every function into $\mathbb{R}$ is automatically a random variable. A very simple counterexample is $\Omega=\mathbb{R}$ with the trivial sigma-algebra $\mathcal{F}=\{\varnothing,\mathbb{R}\}$ and $X(\omega)=\omega$. Then $\{X\le 0\}=(-\infty,0]$, which is not in $\mathcal{F}$, so $X$ is not measurable.

Another common misconception is that a discrete random variable must come from a countable sample space. Not so: one can take the uncountable sample space $\Omega=[0,1]$ with its Borel sigma-algebra and define $X(\omega)=\mathbf{1}_{[1/2,1]}(\omega)$. Then $X$ takes only the two values $0$ and $1$, so it is a discrete random variable even though the underlying sample space is uncountable.

The tutorial also emphasized that measurability is stable under countable pointwise extrema. If $(X_j)_{j\ge 1}$ is a sequence of real random variables, then both $\sup_j X_j$ and $\inf_j X_j$ are real random variables. Indeed, for every $x\in\mathbb{R}$,

- $\{\sup_j X_j\le x\}=\bigcap_{j=1}^{\infty}\{X_j\le x\}$,
- $\{\inf_j X_j\le x\}=\bigcup_{j=1}^{\infty}\{X_j\le x\}$,

and sigma-algebras are closed under countable intersections and unions. So once the individual random variables are measurable, the pointwise supremum and infimum remain measurable as well.

Two important subclasses are worth stating formally. A real random variable $X$ is called _discrete_ if its image $\Omega_X$ is countable. It is called _continuous_, in the sense used in these notes, if its law admits a density with respect to Lebesgue measure.

---

Flashcards for this section are as follows:

- real random variable ::@:: A real random variable is a measurable map $X\colon(\Omega,\mathcal{F})\to(\mathbb{R},\mathcal{B}(\mathbb{R}))$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- half-line criterion ::@:: A real-valued function $X$ is a random variable iff $\{X\le a\}\in\mathcal{F}$ for every $a\in\mathbb{R}$, because the left half-lines $(-\infty,a]$ form a generating pi-system for $\mathcal{B}(\mathbb{R})$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the half-line criterion works ::@:: If $\mathcal{M}=\{A\in\mathcal{B}(\mathbb{R}):X^{-1}(A)\in\mathcal{F}\}$, then $\mathcal{M}$ is a sigma-algebra containing every left half-line. Since those half-lines form a generating pi-system, the Dynkin pi-lambda generator idea forces $\mathcal{M}=\mathcal{B}(\mathbb{R})$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- every function is measurable on a countable full-power-set space ::@:: If $\Omega$ is countable and $\mathcal{F}=\mathcal{P}(\Omega)$, then every function $X\colon\Omega\to\mathbb{R}$ is a random variable, because every preimage $X^{-1}(A)$ is just a subset of $\Omega$ and therefore belongs to $\mathcal{F}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- not every function into $\mathbb{R}$ is automatically measurable ::@:: Counterexample: take $\Omega=\mathbb{R}$, $\mathcal{F}=\{\varnothing,\mathbb{R}\}$, and $X(\omega)=\omega$. Then $\{X\le 0\}=(-\infty,0]$, which is not an event in $\mathcal{F}$, so $X$ is not a random variable.
- discrete random variable does not require countable sample space ::@:: Counterexample: on the uncountable sample space $\Omega=[0,1]$, the function $X(\omega)=\mathbf{1}_{[1/2,1]}(\omega)$ takes only the two values $0$ and $1$, so $X$ is discrete even though $\Omega$ is uncountable. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- supremum of random variables ::@:: For $Y=\sup_jX_j$, the half-line criterion says check $\{Y\le x\}$; this means every coordinate is at most $x$, so $\{\sup_j X_j\le x\}=\bigcap_{j=1}^{\infty}\{X_j\le x\}$, measurable by countable-intersection closure. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- infimum of random variables ::@:: For $Y=\inf_jX_j$, the half-line criterion says check $\{Y\le x\}$; this means at least one coordinate is at most $x$, so $\{\inf_j X_j\le x\}=\bigcup_{j=1}^{\infty}\{X_j\le x\}$, measurable by countable-union closure. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- discrete random variable ::@:: A real random variable is discrete if its image $\Omega_X$ is countable, so only countably many values can actually occur. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- continuous random variable ::@:: In these notes, a real random variable is called continuous if its law admits a density with respect to Lebesgue measure.

## law and cumulative distribution

If $X\colon(\Omega,\mathcal{F},P)\to(S,\mathcal{S})$ is an $S$-valued random variable, its _law_ under $P$ is the probability measure $P_X$ on $(S,\mathcal{S})$ defined by $P_X[B]=P[X^{-1}(B)]$ for $B\in\mathcal{S}$.

This is the measure-theoretic way of saying that $X$ transports the original probability measure from the outcome space to the value space. Instead of asking for probabilities of underlying outcomes, one asks for probabilities of observable values.

When $X$ is real-valued, $P_X$ is a probability measure on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$. Its cumulative distribution function is denoted by $F_X(x):=P[X\le x]=P_X[(-\infty,x]]$.

So the cumulative distribution function of a random variable is simply the cumulative distribution function of its law. This is the precise link between the new chapter on random variables and the previous chapter on cumulative distribution functions.

This also clarifies what it means for two real random variables to have the same distribution. The correct statement is $P_X=P_Y$ as probability measures on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$, or equivalently $F_X(x)=F_Y(x)$ for every $x\in\mathbb{R}$. The equivalence between equality of laws and equality of cumulative distribution functions is another direct application of Dynkin's pi-lambda theorem: equality of the cumulative distribution functions means agreement on the generating pi-system of left half-lines, and the theorem upgrades that to agreement on all Borel sets.

The main point for the random-variable chapter is therefore structural: "same distribution" means equality of laws on the value space, not pointwise equality on the original outcome space. A fuller discussion of that distinction, including concrete counterexamples and warnings about false heuristics, appears in [cumulative distribution function](cumulative%20distribution%20function.md#equality%20of%20distributions).

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

## equality in distribution

The notation $X \stackrel{d}{=} Y$ means that $X$ and $Y$ have the same law. For real random variables this is equivalent to $F_X(x)=F_Y(x)$ for every $x\in\mathbb{R}$. The key point is that equality in distribution is a statement about the transported probability measures on the value space, not about pointwise agreement on the original outcome space.

The distinction matters immediately in simple examples. On the probability space for two fair dice, define $X(\omega_1,\omega_2)=\omega_1$ and $Y(\omega_1,\omega_2)=\omega_2$. Both random variables are uniformly distributed on $\{1,2,3,4,5,6\}$, so $X \stackrel{d}{=} Y$, yet they are not the same function because for example $X(1,2)=1$ while $Y(1,2)=2$.

Symmetry of a density gives another useful source of distributional identities. If a continuous random variable $X$ has an even density, meaning $f_X(x)=f_X(-x)$ for every $x\in\mathbb{R}$, then $X \stackrel{d}{=} -X$. The reason is that the symmetry lets one rewrite $P[-X\le x]$ into the same tail integral that defines $P[X\le x]$. In particular, every centered normal random variable satisfies $X \stackrel{d}{=} -X$.

These examples are reminders that random variables are often compared algebraically through their laws rather than through outcome-by-outcome equality. That point becomes even more useful once one starts transforming random variables.

---

Flashcards for this section are as follows:

- equality in distribution ::@:: The notation $X \stackrel{d}{=} Y$ means that the laws are equal, $P_X=P_Y$; for real random variables this is equivalent to $F_X(x)=F_Y(x)$ for every $x\in\mathbb{R}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- equality in distribution is not pointwise equality ::@:: The statement $X \stackrel{d}{=} Y$ compares the transported probability measures on the value space; it does _not_ mean that $X(\omega)=Y(\omega)$ for each outcome $\omega$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- first die and second die example: On the two-dice space, let $X(\omega_1,\omega_2)=\omega_1$ and $Y(\omega_1,\omega_2)=\omega_2$. Why can $X \stackrel{d}{=} Y$ hold even though $X\neq Y$? ::@:: Both random variables are uniform on $\{1,\ldots,6\}$, so they have the same law, but they are not equal as functions because, for example, $X(1,2)=1\neq 2=Y(1,2)$.
- even-density symmetry: If a continuous random variable $X$ has density satisfying $f_X(x)=f_X(-x)$ for all $x$, what is the relation between $X$ and $-X$ in distribution? ::@:: Then $X \stackrel{d}{=} -X$; in particular, if $X\sim\mathrm{N}(0,\sigma^2)$, then $-X\sim\mathrm{N}(0,\sigma^2)$ as well.

## transformation of random variables

Suppose $X$ is a continuous random variable and we define a new observable by applying a deterministic function $g$, so $Y=g(X)$. Abstractly, this means that we are not changing the underlying randomness and then sampling again; we are only relabelling the already-existing outcomes through a new measurement rule.

The law of $Y$ is therefore the pushforward of the law of $X$ under $g$. If we write the law of $X$ as $P_X$, then the law of $Y$ is written $P_Y=g_{\\ast}P_X$, and this means explicitly that $(g_{\\ast}P_X)(A)=P_X(g^{-1}(A))$ for every measurable target set $A$. In words, pushforward means that probability mass is transported from the old value space to the new one by the map $g$. If several different $x$-values are sent to the same output value or to the same output region, their probabilities are pooled together there. Thus the pushforward viewpoint answers the question "after we observe the old random quantity through the lens $g$, what probability distribution do we see on the output side?"

The corresponding computational move is the pullback. If one wants the probability that $Y$ lands in some set $A$ in the output space, one does not usually calculate directly on the $y$-side. Instead one pulls the set $A$ back through the map and asks which original $x$-values would have produced an outcome in $A$. The pulled-back set is $g^{-1}(A)=\{x\in\mathbb{R}:g(x)\in A\}$. This gives the identity $P[Y\in A]=P[g(X)\in A]=P[X\in g^{-1}(A)]$. So pushforward is the forward transport of probability measures, while pullback is the backward translation of events or sets to a space where the probability is already known.

That pair of ideas is the right mental picture to memorize. Pushforward tells us what the new law _is_; pullback tells us how to _compute_ it. For a monotone map, the pullback of an interval in the $y$-space is again an interval in the $x$-space, which is why cumulative distributions and densities can be computed cleanly. For a non-injective map, the pullback of one target interval may split into several source pieces, and each such piece contributes probability mass to the same output region.

The linear case already shows the pattern. If $Y=aX+b$ with $a\neq 0$, then for $a>0$ one has $F_Y(y)=P[aX+b\le y]=P[X\le (y-b)/a]=F_X\!\left(\frac{y-b}{a}\right)$. Differentiating gives $f_Y(y)=\frac{1}{a}f_X\!\left(\frac{y-b}{a}\right)$. The same argument with the inequality reversed when $a<0$ leads to the uniform formula $f_Y(y)=\frac{1}{|a|}f_X\!\left(\frac{y-b}{a}\right)$. In particular, if $X\sim\mathrm{N}(\mu,\sigma^2)$, then $aX+b\sim\mathrm{N}(a\mu+b,a^2\sigma^2)$.

More generally, if $g\colon\mathbb{R}\to\mathbb{R}$ is differentiable and strictly monotone, then $g$ has an inverse on its range and the density transforms by the change-of-variables rule $f_Y(y)=f_X\!\left(g^{-1}(y)\right)\left|\frac{d}{dy}g^{-1}(y)\right|$ for points $y$ in the range of $g$ corresponding to values where $f_X$ is positive, and $f_Y(y)=0$ elsewhere.

There is an intuitive reason for the factor $\left|\frac{d}{dy}g^{-1}(y)\right|$. Density is probability per unit length on the target axis. If a tiny interval around $y$ comes from a much longer interval around $x=g^{-1}(y)$, then the same probability mass is being spread over a shorter $y$-interval, so the density on the $y$-side becomes larger. If the map stretches intervals, the density becomes smaller. Thus the derivative of the inverse measures local compression or expansion: compression raises density, expansion lowers it. The absolute value appears because orientation may reverse under a decreasing map, but density itself must stay nonnegative.

If one wants a slightly more geometric way to remember the same rule, one may think of the density not merely as a function but as a weighted length element $f_X(x)|dx|$. Probability conservation under the change of variable $y=g(x)$ then says that the same infinitesimal mass can be written on either side as $f_X(x)|dx|=f_Y(y)|dy|$. Rewriting this in terms of $y$ and $x=g^{-1}(y)$ gives $f_Y(y)=f_X(g^{-1}(y))\left|\frac{d}{dy}g^{-1}(y)\right|$. In this light, the Jacobian factor is the one-dimensional version of the volume-scaling factor familiar from differential geometry and multivariable calculus.

The example $Y=e^X$ with $X\sim\mathrm{U}([0,1])$ is a clean illustration. Step 1: identify the transformation $g(x)=e^x$, which is strictly increasing on $\mathbb{R}$. Step 2: compute the inverse $g^{-1}(y)=\log y$, valid on the range $[1,e]$. Step 3: differentiate the inverse to get $\frac{d}{dy}g^{-1}(y)=1/y$. Step 4: insert this into the monotone-map formula together with $f_X(x)=1$ on $[0,1]$. The result is $f_Y(y)=1/y$ on $[1,e]$ and $0$ outside. Intuitively, the exponential map stretches intervals more and more as $x$ grows, so the density on the $y$-side decays like $1/y$.

The example $Y=X^2$ with $X\sim\mathrm{N}(0,1)$ shows what changes when the map is not injective. Step 1: note that $g(x)=x^2$ is not monotone on all of $\mathbb{R}$, so there is no single global inverse. Step 2: for a fixed $y>0$, the preimages are $\sqrt{y}$ and $-\sqrt{y}$. Step 3: compute the local derivative factor from one branch, namely $\frac{d}{dy}\sqrt{y}=1/(2\sqrt{y})$. Step 4: add the contributions from both branches. Because the standard normal density is symmetric, the two contributions are equal, so the total density is $2\cdot \frac{1}{\sqrt{2\pi}}e^{-y/2}\cdot \frac{1}{2\sqrt{y}}=\frac{1}{\sqrt{2\pi}}y^{-1/2}e^{-y/2}$ on $[0,\infty)$. This is the $\chi^2$ distribution with one degree of freedom.

Another instructive tutorial example produces the Cauchy distribution geometrically. Suppose a light source sits at distance $a>0$ from a straight line, emits rays with angle $\theta\sim\mathrm{U}((-\pi/2,\pi/2))$, and let $X=a\tan\theta$ be the point where the ray meets the line. Then the map $g(\theta)=a\tan\theta$ is strictly increasing with inverse $g^{-1}(x)=\arctan(x/a)$. Since $f_\theta(t)=1/\pi$ on $(-\pi/2,\pi/2)$ and $\frac{d}{dx}\arctan(x/a)=\frac{a}{a^2+x^2}$, the density of $X$ is $f_X(x)=\dfrac{a}{\pi(a^2+x^2)}$ for $x\in\mathbb{R}$. This is the centered Cauchy distribution with scale parameter $a$. The heavy tails come from the tangent map blowing up near $\pm\pi/2$: angles close to grazing incidence correspond to very large displacements along the line.

The main lesson is therefore abstract as well as computational: a transformation changes the observable, hence the value space and the law, by gathering probability from all source points that map to the same target value. For monotone maps there is one source point per target value, so one inverse branch and one Jacobian factor appear. For non-injective maps one must sum over all relevant branches.

---

Flashcards for this section are as follows:

- transformation of a random variable, abstractly ::@:: If $Y=g(X)$, then the randomness is not regenerated; rather, the original outcomes are relabelled by a new measurement rule $g$, and the law of $Y$ is obtained by pushing the law of $X$ forward through $g$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- pushforward viewpoint for $Y=g(X)$ ::@:: If the law of $X$ is $P_X$, then the law of $Y=g(X)$ is $P_Y=g_{\ast}P_X$, meaning $(g_{\ast}P_X)(A)=P_X(g^{-1}(A))$ for every measurable target set $A$; this pools together the probabilities of all source values that map into $A$.
- pullback viewpoint for $Y=g(X)$ ::@:: To compute probabilities for $Y=g(X)$, pull the target event back to the original space: for any set $A$, its pullback is $g^{-1}(A)=\{x:g(x)\in A\}$. The point is that the original law of $X$ is already known on the source side, so one can compute $P[Y\in A]$ by evaluating $P[X\in g^{-1}(A)]$ instead.
- pushforward versus pullback ::@:: Pushforward and pullback are the two complementary directions of the same picture. Pushforward moves the probability law forward from the $x$-space to the $y$-space, often written $P_Y=g_{\ast}P_X$, while pullback moves a target set $A$ backward to the source set $g^{-1}(A)$ where the original law is already known. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- monotone-map intuition for densities ::@:: Under a differentiable monotone map, the factor $\left|\frac{d}{dy}g^{-1}(y)\right|$ measures how much a tiny interval near $y$ expands or contracts when pulled back to the $x$-side. If the pullback interval is long, the same probability mass is spread over a shorter target interval and the density rises; if the pullback interval is short, the density falls. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- geometric memory aid for density transformation ::@:: A one-dimensional density may be remembered as a weighted length element $f_X(x)|dx|$. Probability conservation under the coordinate change $y=g(x)$ says that the same infinitesimal mass is written as $f_X(x)|dx|=f_Y(y)|dy|$, and rewriting this identity as $f_Y(y)=f_X(x)\left|\frac{dx}{dy}\right|=f_X(g^{-1}(y))\left|\frac{d}{dy}g^{-1}(y)\right|$ gives the Jacobian rule for $f_Y$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Jacobian factor, geometrically ::@:: The factor $\left|\frac{d}{dy}g^{-1}(y)\right|$ is the one-dimensional volume-scaling factor: it records how lengths change under the coordinate transformation. This is the same geometric role played by Jacobian determinants in higher dimensions, but here the "volume" is just length. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- density of $Y=aX+b$: If $Y=aX+b$ with $a\neq 0$ and $X$ has density $f_X$, what is $f_Y$? ::@:: $f_Y(y)=\frac{1}{|a|}f_X\!\left(\frac{y-b}{a}\right)$.
- normal law under $Y=aX+b$: If $X\sim\mathrm{N}(\mu,\sigma^2)$ and $Y=aX+b$, what distribution does $Y$ have? ::@:: $Y\sim\mathrm{N}(a\mu+b,a^2\sigma^2)$.
- density of $Y=g(X)$ under a monotone map: If $X$ has density $f_X$, $Y=g(X)$, and $g$ is differentiable and strictly monotone, what is the density of $Y$? ::@:: $f_Y(y)=f_X\!\left(g^{-1}(y)\right)\left|\frac{d}{dy}g^{-1}(y)\right|$ on the range of $g$, and $0$ elsewhere.
- why the absolute value appears in the transformation rule ::@:: The derivative of $g^{-1}$ may be negative when $g$ is decreasing, but a density must stay nonnegative, so the change-of-variables factor is $\left|\frac{d}{dy}g^{-1}(y)\right|$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- exponential example / steps: If $X\sim\mathrm{U}([0,1])$ and $Y=e^X$, what are the main steps to compute $f_Y$? ::@:: (1) Note that $g(x)=e^x$ is strictly increasing. <br/> (2) Compute the inverse $g^{-1}(y)=\log y$ on $[1,e]$. <br/> (3) Differentiate to get $\frac{d}{dy}g^{-1}(y)=1/y$. <br/> (4) Since $f_X=1$ on $[0,1]$, conclude $f_Y(y)=1/y$ for $y\in[1,e]$ and $0$ otherwise.
- exponential example / intuition: If $X\sim\mathrm{U}([0,1])$ and $Y=e^X$, why does the density of $Y$ behave like $1/y$? ::@:: The exponential map stretches intervals more strongly at larger $x$, so equal amounts of probability mass are spread over longer $y$-intervals there; hence the density decreases like $1/y$.
- square-normal example / steps: If $X\sim\mathrm{N}(0,1)$ and $Y=X^2$, what are the main steps to compute $f_Y$? ::@:: (1) Observe that $x\mapsto x^2$ is not one-to-one on $\mathbb{R}$. <br/> (2) For each $y>0$, identify the two preimages $\sqrt{y}$ and $-\sqrt{y}$. <br/> (3) Use the derivative factor $\frac{d}{dy}\sqrt{y}=1/(2\sqrt{y})$. <br/> (4) Add the equal contributions from the two symmetric branches to get $f_Y(y)=\frac{1}{\sqrt{2\pi}}y^{-1/2}e^{-y/2}$ on $[0,\infty)$.
- square of a standard normal random variable: If $X\sim\mathrm{N}(0,1)$ and $Y=X^2$, what is the density of $Y$? ::@:: $f_Y(y)=\frac{1}{\sqrt{2\pi}}y^{-1/2}e^{-y/2}\mathbf{1}_{[0,\infty)}(y)$; this is the $\chi^2$ distribution with one degree of freedom.
- light-source transformation ::@:: If $\theta\sim\mathrm{U}((-\pi/2,\pi/2))$ and $X=a\tan\theta$ with $a>0$, then $X$ has density $f_X(x)=\dfrac{a}{\pi(a^2+x^2)}$ on $\mathbb{R}$; this is the centered Cauchy distribution with scale parameter $a$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the light-source model gives heavy tails ::@:: In the light-source example, angles near $\pm\pi/2$ correspond to rays that travel almost parallel to the line, so tiny angular changes produce very large horizontal displacements; this is why the resulting Cauchy density has heavy tails. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- non-injective transformation idea ::@:: When the transformation $g$ is not one-to-one, the density of $Y=g(X)$ is obtained by summing the contributions from all preimage branches that yield the same value of $y$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
