---
aliases:
  - cumulative distribution function
  - cumulative distribution functions
  - distribution function
  - distribution functions
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/cumulative_distribution_function
  - language/in/English
---

# cumulative distribution function

The cumulative distribution function is the most robust way to describe a probability law on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$. Unlike a probability density function, which only describes the absolutely continuous part of a law, the cumulative distribution function works uniformly for discrete, continuous, mixed, and even pathological singular continuous distributions.

---

Flashcards for this section are as follows:

- cumulative distribution function / overview ::@:: A cumulative distribution function describes probability laws on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ in a way that works for discrete, continuous, mixed, and singular continuous distributions. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## definition and density relation

For a probability measure $P$ on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$, the _cumulative distribution function_ is defined by $F_P(x)=P[(-\infty,x]]$. This records how much probability has accumulated by the time one reaches the point $x$. The definition makes sense for every probability law on the real line, not only for laws that admit densities.

If $P$ is characterized by a density $f$, then $F_P(x)=\int_{-\infty}^{x} f(t)\,dt$. So in the absolutely continuous case the cumulative distribution function is obtained by integrating the density from the far left up to $x$. Conversely, whenever $f$ is continuous at $x$, the fundamental theorem of calculus gives $f(x)=F_P'(x)$.

This is why cumulative distribution functions unify the discrete and continuous viewpoints. A discrete law produces a step function with jumps at atoms, while a density-based continuous law produces a continuous accumulation curve. More general laws may combine both features.

---

Flashcards for this section are as follows:

- cumulative distribution function / definition from a probability measure ::@:: For a probability measure $P$ on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$, the cumulative distribution function is $F_P(x)=P[(-\infty,x]]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- interpretation ::@:: The cumulative distribution function $F_P(x)$ measures how much probability has accumulated up to the point $x$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- cdf from density ::@:: If $P$ is characterized by a density $f$, then $F_P(x)=\int_{-\infty}^{x} f(t)\,dt$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- density from cdf ::@:: If $P$ has density $f$ and $f$ is continuous at $x$, then $f(x)=F_P'(x)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why cdfs unify probability laws ::@:: A cumulative distribution function works for discrete laws, density-based continuous laws, mixed laws, and more pathological laws, so it is more general than a density.

## standard normal notation

For the standard normal distribution $\mathrm{N}(0,1)$, the density is traditionally denoted by $\varphi(x)=\dfrac{1}{\sqrt{2\pi}}e^{-x^2/2}$, and the corresponding cumulative distribution function is denoted by $\Phi(x)=\int_{-\infty}^{x} \varphi(t)\,dt$. The special notation is useful because the Gaussian density has no elementary antiderivative, so its cumulative distribution function occurs so often that it receives its own symbol.

---

Flashcards for this section are as follows:

- standard normal density ::@:: For the standard normal distribution $\mathrm{N}(0,1)$, the density is $\varphi(x)=\dfrac{1}{\sqrt{2\pi}}e^{-x^2/2}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- standard normal cumulative distribution function ::@:: For the standard normal law, the cumulative distribution function is $\Phi(x)=\int_{-\infty}^{x} \varphi(t)\,dt$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why $\Phi$ gets special notation ::@:: The Gaussian density has no elementary antiderivative, so its cumulative distribution function is denoted separately by $\Phi$.

## general properties

Every cumulative distribution function $F$ satisfies four universal properties:

- $0 \le F(x) \le 1$ for all $x$,
- $F$ is nondecreasing,
- $F$ is right-continuous,
- $\lim_{x\to-\infty}F(x)=0$ and $\lim_{x\to\infty}F(x)=1$.

Each property has a short proof from the half-line definition.

For the range property, $(-\infty,x]$ is an event, so probability theory immediately gives $0 \le P[(-\infty,x]] \le 1$. Hence $0 \le F(x) \le 1$.

For monotonicity, if $x \le y$, then $(-\infty,x] \subseteq (-\infty,y]$. Since probability is monotone under inclusion, this implies $F(x)=P[(-\infty,x]] \le P[(-\infty,y]] = F(y)$.

For right-continuity, fix $x$ and let $x_n \downarrow x$ with $x_n>x$. Then the sets $(-\infty,x_n]$ form a decreasing sequence whose intersection is exactly $(-\infty,x]$. By continuity of probability from above, $F(x_n)=P[(-\infty,x_n]] \downarrow P\big[\bigcap_{n=1}^{\infty}(-\infty,x_n]\big] = P[(-\infty,x]] = F(x)$. So $\lim_{n\to\infty}F(x_n)=F(x)$, which is precisely right-continuity.

For the limits at infinity, if $x_n\to -\infty$, then $(-\infty,x_n] \downarrow \varnothing$, so continuity from above gives $F(x_n) \downarrow P[\varnothing]=0$. Likewise, if $x_n\to\infty$, then $(-\infty,x_n] \uparrow \mathbb{R}$, so continuity from below gives $F(x_n) \uparrow P[\mathbb{R}]=1$.

Another important fact is that jumps of $F$ detect atoms. If we define $F(x-):=\lim_{y\uparrow x}F(y)$, then $F(x)-F(x-)=P[\{x\}]$. So a jump in the cumulative distribution function is exactly the probability mass sitting at the point $x$.

To prove this jump formula, take any sequence $y_n \uparrow x$ with $y_n<x$. Then the sets $(-\infty,y_n]$ increase to $(-\infty,x)$, so by continuity from below, $F(x-)=\lim_{n\to\infty}F(y_n)=P[(-\infty,x))$. Now split the half-line at the endpoint: $(-\infty,x] = (-\infty,x) \cup \{x\}$, and the two sets on the right are disjoint. Therefore $F(x)=P[(-\infty,x]] = P[(-\infty,x)) + P[\{x\}] = F(x-) + P[\{x\}]$, which rearranges to $F(x)-F(x-)=P[\{x\}]$.

---

Flashcards for this section are as follows:

- cumulative distribution function / value range ::@:: Every cumulative distribution function satisfies $0 \le F(x) \le 1$ for all $x$, because $F(x)=P[(-\infty,x]]$ and every probability lies between $0$ and $1$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- cumulative distribution function / monotonicity ::@:: Every cumulative distribution function is nondecreasing: if $x \le y$, then $(-\infty,x] \subseteq (-\infty,y]$, so monotonicity of probability gives $F(x) \le F(y)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- cumulative distribution function / right continuity ::@:: Every cumulative distribution function is right-continuous: if $x_n \downarrow x$, then $(-\infty,x_n] \downarrow (-\infty,x]$, so continuity of probability from above gives $F(x_n) \downarrow F(x)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- cumulative distribution function / limits at infinity ::@:: Every cumulative distribution function satisfies $\lim_{x\to-\infty}F(x)=0$ and $\lim_{x\to\infty}F(x)=1$, because the half-lines $(-\infty,x]$ decrease to $\varnothing$ on the left and increase to $\mathbb{R}$ on the right. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- cumulative distribution function / jump formula for atoms ::@:: If $F(x-)=\lim_{y\uparrow x}F(y)$, then $F(x-)=P[(-\infty,x))$ by continuity from below, and since $(-\infty,x]=(-\infty,x)\cup\{x\}$ is a disjoint union, one gets $F(x)-F(x-)=P[\{x\}]$; jumps of the cumulative distribution function are exactly atoms. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## equality of distributions

For probability measures $P$ and $Q$ on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$, saying that the two distributions are equal means exactly that they are the same measure on the whole Borel sigma-algebra: $P[A]=Q[A]$ for every Borel set $A$.

For laws on the real line, this is equivalent to equality of cumulative distribution functions. One direction is immediate: if $P=Q$, then $F_P(x)=P[(-\infty,x]]=Q[(-\infty,x]]=F_Q(x)$ for every $x$. Conversely, if $F_P(x)=F_Q(x)$ for every $x$, then $P$ and $Q$ agree on all left half-lines $(-\infty,x]$. Since those half-lines form a pi-system generating $\mathcal{B}(\mathbb{R})$, the uniqueness argument from Dynkin's pi-lambda theorem gives $P=Q$ on all Borel sets.

This is the natural way to say the correspondence: on the real line, specifying a probability measure on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ is equivalent to specifying its cumulative distribution function. The forward map sends $P$ to $F_P(x)=P[(-\infty,x]]$. This already determines the probabilities of half-open intervals because

$P((a,b])=P(( -\infty,b]) - P(( -\infty,a]) = F_P(b)-F_P(a)$.

So if two probability measures have the same CDF, then they agree on every interval $(a,b]$. Since such intervals generate $\mathcal{B}(\mathbb{R})$, the two measures must agree on all Borel sets. This explains injectivity of the map $P\mapsto F_P$.

Conversely, if $F$ is any CDF, the Lebesgue-Stieltjes theorem produces a probability measure $\mu_F$ with $\mu_F(( -\infty,x])=F(x)$ for every $x$. Then automatically $\mu_F((a,b])=F(b)-F(a)$, so the CDF determines the probabilities of the basic generating intervals and hence the whole measure. Therefore the space of probability measures on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ is in bijection with the space of CDFs.

This is the correct meaning of statements such as "two real random variables have the same law": it means their laws are equal, or equivalently, in the real-valued case, their cumulative distribution functions are equal at every point. It does _not_ mean that $X$ and $Y$ are pointwise equal as functions, nor that they must even be defined on the same sample space. A very simple counterexample is the fair-coin space $\Omega=\{H,T\}$ with $X(H)=1$, $X(T)=0$, $Y(H)=0$, and $Y(T)=1$. Both random variables are Bernoulli $(1/2)$, so they have the same distribution, but they are never equal pointwise.

Several intuitive shortcuts are wrong. Checking only point masses is not enough: two continuous distributions may satisfy $P[\{x\}]=Q[\{x\}]=0$ for every $x$ and still be completely different, because interval probabilities can differ. For instance, the uniform law on $(0,1)$ and the law with density $2x$ on $(0,1)$ both assign probability $0$ to every singleton, but they disagree on $\big(0,\tfrac12\big]$: the first gives probability $1/2$, while the second gives probability $\int_0^{1/2}2x\,dx=1/4$.

Likewise, matching only a few summary statistics such as mean and variance does not determine the whole law. For example, let $X$ take the values $-1$ and $1$ with probability $1/2$ each, and let $Y$ take the values $-\sqrt2,0,\sqrt2$ with probabilities $1/4,1/2,1/4$. Then both have mean $0$ and variance $1$, but $P[X=0]=0$ whereas $P[Y=0]=1/2$, so their distributions are different.

Even sharing the same support does not determine the law: support tells you where mass may lie, not how much mass is assigned to different Borel sets inside that support. The same pair of laws just used above—the uniform law on $(0,1)$ and the law with density $2x$ on $(0,1)$ — already shows this. They have the same support $[0,1]$, but they still disagree on intervals such as $\big(0,\tfrac12\big]$.

There is one important refinement. If both distributions are known in advance to be absolutely continuous with densities $f$ and $g$, then equality of distributions is equivalent to $f=g$ almost everywhere. The words _almost everywhere_ are essential: changing a density at a single point, or on any Lebesgue-null set, does not change any interval integral and therefore does not change the cumulative distribution function or the underlying law.

So equal cumulative distribution functions do not force equal densities _everywhere_. They force equality only almost everywhere, provided densities exist at all. For example, if $f$ is a density and one defines $g(x)=f(x)$ for $x\neq 0$ but changes the single value $g(0)$ arbitrarily, then $f$ and $g$ define the same distribution and the same cumulative distribution function, even though they are not pointwise equal as functions. A concrete instance is $f(x)=\mathbf{1}_{(0,1)}(x)$ and $g(x)=\mathbf{1}_{(0,1)}(x)+100\mathbf{1}_{\{1/2\}}(x)$: the two functions differ at one point, but their interval integrals are identical, so they define the same law. In other words, "equal distribution" is a statement about the resulting measure, not about literal pointwise equality of one chosen density representative.

But this is only a special-case criterion; it is not the general definition, because many laws—such as mixed or singular continuous laws—do not admit densities at all.

---

Flashcards for this section are as follows:

- equality of two distributions on $\mathbb{R}$ ::@:: Two distributions $P$ and $Q$ on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ are equal exactly when $P[A]=Q[A]$ for every Borel set $A$; equality means equality of measures, not just matching a few numerical features.
- equality of distributions via cumulative distribution functions ::@:: For probability measures on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$, one has $P=Q$ if and only if $F_P(x)=F_Q(x)$ for every $x$, because the left half-lines $(-\infty,x]$ form a generating pi-system. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- probability measures on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ versus CDFs ::@:: On the real line, specifying a probability measure is equivalent to specifying its cumulative distribution function.
- interval probabilities from a CDF ::@:: If $F_P(x)=P(( -\infty,x])$, then for every $a<b$ one has $P((a,b])=F_P(b)-F_P(a)$; so a CDF already determines the probabilities of the basic half-open intervals. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- derivation of the probability measure-CDF correspondence ::@:: Forward direction: from $P$, define $F_P(x)=P(( -\infty,x])$, then recover interval probabilities by $P((a,b])=F_P(b)-F_P(a)$. Since half-open intervals generate $\mathcal{B}(\mathbb{R})$, the measure is determined by its CDF. Reverse direction: from a CDF $F$, the Lebesgue-Stieltjes theorem gives a unique probability measure $\mu_F$ with $\mu_F(( -\infty,x])=F(x)$, hence also $\mu_F((a,b])=F(b)-F(a)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- same distribution for real random variables ::@:: Real random variables $X$ and $Y$ have the same distribution exactly when their laws satisfy $P_X=P_Y$, equivalently $F_X=F_Y$ pointwise; this does not require $X$ and $Y$ to be pointwise equal or to live on the same sample space. A simple counterexample is a fair coin with $X(H)=1$, $X(T)=0$, $Y(H)=0$, and $Y(T)=1$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- same point masses or same support do not imply same distribution ::@:: Counterexample: the uniform law on $(0,1)$ and the law with density $2x$ on $(0,1)$ both assign probability $0$ to every singleton and have the same support $[0,1]$, but on $\big(0,\tfrac12\big]$ they give probabilities $1/2$ and $1/4$, so the distributions are different. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- same mean and variance do not imply same distribution ::@:: Counterexample: if $X=\pm1$ with probability $1/2$ each, while $Y\in\{-\sqrt2,0,\sqrt2\}$ with probabilities $1/4,1/2,1/4$, then both have mean $0$ and variance $1$, but $P[X=0]=0\neq 1/2=P[Y=0]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- equal distributions imply equal densities only almost everywhere ::@:: If two laws are already known to admit densities, then equality of distributions forces those densities to agree only almost everywhere, not necessarily everywhere; for example $f(x)=\mathbf{1}_{(0,1)}(x)$ and $g(x)=\mathbf{1}_{(0,1)}(x)+100\mathbf{1}_{\{1/2\}}(x)$ define the same law even though they are not pointwise equal. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## mixed and pathological distributions

A probability measure on $\mathbb{R}$ need not be purely discrete or purely continuous in the density sense. A simple mixed example is $P=\frac{1}{2}\delta_0+\frac{1}{2}\mathrm{U}(0,1)$, meaning that with probability $1/2$ the value is exactly $0$, while with probability $1/2$ it is drawn uniformly from $(0,1)$. Its cumulative distribution function has a jump of size $1/2$ at $0$ and then increases continuously on $(0,1)$, so one sees both an atomic part and an absolutely continuous part in the same law.

For honors-level perspective, there is an even more general phenomenon. A probability measure on $\mathbb{R}$ can have an atomic part, an absolutely continuous part, and a singular continuous part. The singular continuous part is the pathological one from the elementary viewpoint: it has no atoms, yet it is not given by integrating a density against Lebesgue measure.

The classical example is the Cantor distribution. One way to describe it is to start with independent Bernoulli digits $\xi_1,\xi_2,\ldots$ taking values $0$ and $2$ with probability $1/2$ each, and then form the random ternary expansion $X=\sum_{n=1}^{\infty} \frac{\xi_n}{3^n}$. Because only the digits $0$ and $2$ appear, $X$ always lies in the Cantor set. The distribution function of $X$ is continuous and nondecreasing, but it increases only on the Cantor set, which has Lebesgue measure $0$. So the law has no jumps, hence no point masses, but also no density in the usual sense. This shows that continuity of the cumulative distribution function does _not_ by itself imply the existence of a density.

It helps to view the construction stage by stage. After one ternary digit, $X$ has been placed in either the left third $[0,1/3]$ or the right third $[2/3,1]$, each with probability $1/2$. After two digits, one has chosen one of the four surviving intervals of length $3^{-2}$, each with probability $1/4$. In general, the partial sum $X_n=\sum_{k=1}^{n}\frac{\xi_k}{3^k}$ determines which one of the $2^n$ retained stage $n$ Cantor intervals contains $X$, and each such interval has probability $2^{-n}$. So the random variable is built by repeatedly choosing left or right and zooming into a nested sequence of surviving intervals.

This stage-by-stage picture explains both the absence of atoms and the singularity. A single point of the Cantor set corresponds to one infinite left/right choice pattern. The probability of matching its first $n$ choices is $2^{-n}$, which tends to $0$, so no single point can carry positive mass. On the other hand, after stage $n$ the entire probability mass still lies inside the union of the $2^n$ retained intervals, whose total length is $(2/3)^n\to0$. Thus the mass is concentrated on sets of arbitrarily small total length, which is exactly the opposite of what an ordinary density would do.

So the right intuition is not merely "continuous but strange." The Cantor distribution spreads mass across smaller and smaller Cantor intervals without ever piling up at a point, yet it keeps all the mass trapped inside a set of Lebesgue measure $0$. That is why its cumulative distribution function is continuous, but the law is still singular.

Thus the cumulative distribution function reveals the real classification: discrete laws appear through jumps, density-based continuous laws through absolutely continuous growth, mixed laws through both behaviors at once, and pathological singular continuous laws through continuous growth without a density.

---

Flashcards for this section are as follows:

- mixed distribution ::@:: A mixed distribution has both an atomic part and an absolutely continuous part, so it is neither purely discrete nor purely continuous in the density sense.
- simple mixed example ::@:: The law $P=\frac{1}{2}\delta_0+\frac{1}{2}\mathrm{U}(0,1)$ is mixed: it puts probability $1/2$ at the single point $0$ and spreads the remaining probability continuously over $(0,1)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- cdf of $P=\frac{1}{2}\delta_0+\frac{1}{2}\mathrm{U}(0,1)$ ::@:: The cumulative distribution function has a jump where the atom at $0$ sits and then varies continuously where the uniform density part contributes.
- singular continuous distribution ::@:: A singular continuous distribution has no atoms and no density with respect to Lebesgue measure, yet its cumulative distribution function is still continuous and nondecreasing.
- Cantor distribution construction ::@:: The Cantor distribution can be constructed by taking independent digits $\xi_n\in\{0,2\}$ with probability $1/2$ each and setting $X=\sum_{n=1}^{\infty}\xi_n/3^n$; because only ternary digits $0$ and $2$ appear, $X$ always lies in the Cantor set. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- stage $n$ intuition for the Cantor distribution ::@:: After $n$ ternary digits, the partial sum $X_n=\sum_{k=1}^{n}\xi_k/3^k$ determines one of the $2^n$ surviving Cantor intervals of length $3^{-n}$, each chosen with probability $2^{-n}$; the full random variable comes from a nested left/right choice at every stage.
- Cantor distribution ::@:: The Cantor distribution is the classical singular continuous example: its cumulative distribution function is continuous, but the probability is concentrated on the Cantor set, which has Lebesgue measure $0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- intuition for the Cantor distribution ::@:: The Cantor distribution repeatedly splits probability between the left and right thirds while removing the middle third, so mass is spread continuously over the Cantor set without creating atoms and without producing a density on intervals.
- why the Cantor distribution has no atoms ::@:: A single Cantor point corresponds to one infinite sequence of left/right choices; the probability of matching its first $n$ digits is $2^{-n}$, so the probability of the full infinite path is $0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the Cantor distribution is singular ::@:: After stage $n$, all mass lies in the $2^n$ retained intervals, whose total length is $(2/3)^n\to0$; so the law is concentrated on sets of arbitrarily small total length and cannot come from an ordinary density. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why a continuous cumulative distribution function need not come from a density ::@:: A continuous cumulative distribution function can fail to have a density because singular continuous laws, such as the Cantor distribution, have no jumps but are still not absolutely continuous with respect to Lebesgue measure.
- cdf behavior for discrete continuous mixed and pathological laws ::@:: Discrete laws produce jumps, density-based continuous laws have no jumps and admit densities, mixed laws have both jump and continuous pieces, and singular continuous pathological laws have no jumps but still no density.

<!-- check: ignore-next-line[header_style]: proper noun -->
## Lebesgue-Stieltjes measures

The converse to the basic cumulative-distribution-function properties is just as important as the forward direction: every function $F\colon\mathbb{R}\to\mathbb{R}$ that is nondecreasing, right-continuous, satisfies $\lim_{x\to-\infty}F(x)=0$, and $\lim_{x\to\infty}F(x)=1$ is the cumulative distribution function of a unique probability measure on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$. This measure is often called the _Lebesgue-Stieltjes measure_ associated with $F$.

Existence is often proved by a generalized inverse-transform construction, while uniqueness comes from the half-line generator argument. So the theorem says that the four basic CDF properties are not just necessary conditions; they are exactly the conditions needed to describe a probability law on the real line.

Uniqueness comes from the pi-lambda machinery. The left half-lines $\mathcal{E}=\{(-\infty,b]:b\in\mathbb{R}\}$ form a pi-system and generate $\mathcal{B}(\mathbb{R})$. If two probability measures have the same cumulative distribution function $F$, then they agree on every set in $\mathcal{E}$, because each such set has probability $F(b)$. Agreement on this generating pi-system therefore implies agreement on all Borel sets.

This theorem explains why cumulative distribution functions are such a powerful language: giving the function $F$ is already enough to specify a unique probability law on the whole Borel sigma-algebra. In other words, the reverse map $F\mapsto\mu_F$ is well defined and surjective onto the whole space of probability measures on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$, while the half-line generator argument gives injectivity of the forward map $P\mapsto F_P$.

---

Flashcards for this section are as follows:

- Lebesgue-Stieltjes theorem ::@:: Every nondecreasing, right-continuous function $F\colon\mathbb{R}\to\mathbb{R}$ with $\lim_{x\to-\infty}F(x)=0$ and $\lim_{x\to\infty}F(x)=1$ is the cumulative distribution function of a unique probability measure on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$. This is the surjectivity half of the probability measure-CDF bijection. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- uniqueness from half-lines ::@:: Uniqueness holds because the left half-lines $(-\infty,b]$ form a pi-system generating $\mathcal{B}(\mathbb{R})$; if two measures have the same cumulative distribution function, then they agree on every such half-line, so by the pi-lambda theorem they agree on all Borel sets. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- inverse-transform intuition ::@:: The Lebesgue-Stieltjes construction is the inverse-transform idea in measure form: begin with a uniform random input and use a generalized inverse of the target cumulative distribution function to produce the desired law.

### concrete proof of existence and uniqueness

One concrete proof of existence starts from the generalized inverse $F^{-1}(u)=\sup\{y\in\mathbb{R}:F(y)<u\}$ for $u\in(0,1)$, and from a uniform random input $U\sim\mathrm{U}(0,1)$. Define $X=F^{-1}(U)$ and let $P$ be the law of $X$.

The key computation is to identify the event $\{F^{-1}(U)\le x\}$. Fix $u\in(0,1)$ and write $A_u:=\{y\in\mathbb{R}:F(y)<u\}$ and $s:=\sup A_u=F^{-1}(u)$. The previous subsection proved that $\{x\in\mathbb{R}:F(x)\ge u\}=[s,\infty)$. Therefore, for every real $x$, one has $F^{-1}(u)\le x \Longleftrightarrow s\le x \Longleftrightarrow x\in[s,\infty) \Longleftrightarrow F(x)\ge u$, that is, $F^{-1}(u)\le x \Longleftrightarrow u\le F(x)$.

So the set of uniform levels that land at or before $x$ is exactly $\{u\in(0,1):F^{-1}(u)\le x\}=(0,F(x)]\cap(0,1)$.

Therefore $P[(-\infty,x]]=P[F^{-1}(U)\le x]=P[U\le F(x)]=F(x)$, because $U$ is uniform on $(0,1)$. This proves existence: the random variable $X=F^{-1}(U)$ has cumulative distribution function exactly equal to $F$.

The intuition is simple once one pictures the graph of $F$. A uniform input $u\in(0,1)$ chooses a horizontal probability level. The generalized inverse $F^{-1}(u)$ then asks for the first point where the graph of $F$ has already climbed to that level. So the event $F^{-1}(u)\le x$ means that the chosen level has been reached by the time one arrives at $x$. That is why it should match the condition $u\le F(x)$.

Uniqueness is then separate and simple. If $P$ and $Q$ are two probability measures on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ with the same cumulative distribution function $F$, then they agree on every left half-line $(-\infty,b]$. Since those half-lines form a pi-system generating $\mathcal{B}(\mathbb{R})$, the uniqueness result from the pi-lambda theorem implies $P=Q$ on all Borel sets.

So the proof naturally splits into two ideas: existence comes from explicitly building a random variable from uniform input, and uniqueness comes from the fact that cumulative distribution functions already determine the probabilities of a generating family.

This is also the right place to notice how the concrete proof leads into the abstract proof. In the concrete proof one starts with a uniform random variable $U$, forms $X=F^{-1}(U)$, and studies the law of $X$. The abstract proof packages the same idea in measure-theoretic notation: instead of talking about the random variable $X$ directly, it says that the distribution of $X$ is obtained by transporting uniform measure through the map $T(u)=F^{-1}(u)$. So the abstract proof is not a different construction; it is the same construction written at the level of measures rather than sample points.

This is also the right place to notice two practical remarks. First, the proof is constructive: once one can simulate a uniform random variable on $(0,1)$, the formula $X=F^{-1}(U)$ gives a direct simulation method for the law with cumulative distribution function $F$. Second, this shows that the real-line case is conceptually reduced to the existence of the uniform distribution. In the discrete setting, a law is described directly by its probability mass function; here the only genuinely external input is the existence of $\mathrm{U}(0,1)$, equivalently the existence of Lebesgue measure on $\mathbb{R}$. Also, because continuous laws assign probability $0$ to singletons, $\mathrm{U}(0,1)$ and $\mathrm{U}([0,1])$ are essentially the same for this construction: the endpoints make no probabilistic difference.

---

Flashcards for this section are as follows:

- concrete existence proof for Lebesgue-Stieltjes theorem ::@:: Purpose: explicitly build a random variable whose cumulative distribution function is the prescribed function $F$. The construction is to start with $U\sim\mathrm{U}(0,1)$, define $X=F^{-1}(U)$, and then prove that this $X$ satisfies $P[X\le x]=F(x)$ for every $x$; uniqueness is handled separately by the half-line generator argument. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- intuition for the concrete existence proof ::@:: A uniform input $u\in(0,1)$ chooses a horizontal probability level, and the generalized inverse returns the first point where the graph of $F$ has climbed to that level. So $F^{-1}(u)\le x$ should mean exactly that the chosen level has already been reached by time $x$, which is the condition $u\le F(x)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- key event identity in the concrete existence proof ::@:: Fix $x\in\mathbb{R}$. The left-hand side $\{u\in(0,1):F^{-1}(u)\le x\}$ asks which uniform input levels are sent by the generalized inverse to points at or before $x$. The right-hand side $(0,F(x)]\cap(0,1)$ asks which levels have already been reached by the cumulative distribution function by time $x$. The identity says these are the same set: $\{u\in(0,1):F^{-1}(u)\le x\}=(0,F(x)]\cap(0,1)$, equivalently $F^{-1}(u)\le x \iff u\le F(x)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why $F^{-1}(u)\le x$ implies $u\le F(x)$ ::@:: Let $s:=F^{-1}(u)$. From the pseudoinverse argument, the set of points where the cumulative distribution function has already reached level $u$ is $\{z\in\mathbb{R}:F(z)\ge u\}=[s,\infty)$. If $F^{-1}(u)\le x$, then $s\le x$. Therefore $x\in[s,\infty)=\{z:F(z)\ge u\}$, so $F(x)\ge u$, i.e. $u\le F(x)$.
- why $u\le F(x)$ implies $F^{-1}(u)\le x$ ::@:: Let $s:=F^{-1}(u)$. Again $\{z\in\mathbb{R}:F(z)\ge u\}=[s,\infty)$. If $u\le F(x)$, then $x\in\{z:F(z)\ge u\}=[s,\infty)$. Hence $s\le x$. Since $s=F^{-1}(u)$, this gives $F^{-1}(u)\le x$.
- why the concrete construction gives the target cumulative distribution function ::@:: Let $X=F^{-1}(U)$. The key event identity says $\{X\le x\}=\{F^{-1}(U)\le x\}=\{U\le F(x)\}$. Therefore $P[X\le x]=P[U\le F(x)]=F(x)$ because $U$ is uniform on $(0,1)$. So the cumulative distribution function of the constructed random variable $X$ is exactly $F$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- uniqueness in the concrete proof ::@:: If two probability measures have the same cumulative distribution function, then they agree on every left half-line $(-\infty,b]$; since those half-lines generate $\mathcal{B}(\mathbb{R})$, the pi-lambda uniqueness argument forces the measures to be equal on all Borel sets. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- concrete proof and abstract proof relation ::@:: The abstract proof repackages the same construction as the concrete proof: the concrete version starts with $U$ and forms $X=F^{-1}(U)$, while the abstract version says that the law of $X$ is the measure obtained by transporting uniform measure through the map $u\mapsto F^{-1}(u)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- concrete proof / next step intuition ::@:: After constructing $X=F^{-1}(U)$, the next step is to identify the event $\{X\le x\}$ in a form involving only the uniform variable $U$; once that event is rewritten as $\{U\le F(x)\}$, taking probabilities becomes immediate because the law of $U$ is already known. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- constructive simulation viewpoint ::@:: The proof is constructive: if one can simulate $U\sim\mathrm{U}(0,1)$, then setting $X=F^{-1}(U)$ gives a way to simulate the distribution with cumulative distribution function $F$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the real-line construction reduces to the uniform law ::@:: On $(\mathbb{R},\mathcal{B}(\mathbb{R}))$, once $\mathrm{U}(0,1)$ exists, every real-valued probability law can be constructed from it via the generalized inverse; the uniform law is the single external input from which the concrete existence proof builds the target distribution. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why $\mathrm{U}(0,1)$ and $\mathrm{U}([0,1])$ are essentially the same here ::@:: Continuous distributions give probability $0$ to single points, so the endpoints $0$ and $1$ do not affect the inverse-transform construction; using $(0,1)$ or $[0,1]$ makes no essential probabilistic difference.

### pseudoinverse

The guiding idea comes from the classical inverse-transform method. Here $X$ denotes a real random variable whose cumulative distribution function is the target function $F$. If $F$ were strictly increasing and continuous, then one would expect $U=F(X)$ to be uniformly distributed on $(0,1)$, and conversely one could try to recover a random variable with cumulative distribution function $F$ by solving $X=F^{-1}(U)$ for a uniform random variable $U$. So the whole construction comes from trying to solve the level equation $u=F(x)$ for $x$.

The difficulty is that a general cumulative distribution function need not be strictly increasing or even continuous. It can have flat parts, where many $x$ share the same function value, and jump parts, where whole intervals of $u$-values should collapse onto a single atom. So the ordinary inverse usually does not exist.

The pseudoinverse repairs this by choosing the first point where the graph has already reached the level $u$. Intuitively, one may think of $F^{-1}(u)=\inf\{x\in\mathbb{R}:F(x)\ge u\}$, which, for nondecreasing right-continuous $F$, is equivalent to the course formula $F^{-1}(u)=\sup\{y\in\mathbb{R}:F(y)<u\}$. This definition behaves correctly in all cases: on a strictly increasing part it agrees with the usual inverse, on a flat part it jumps to the left endpoint of the plateau, and at an atom it sends the whole vertical jump interval of $u$-values to the same point.

The equivalence of the two formulas is worth spelling out carefully in steps. Let $A_u:=\{y\in\mathbb{R}:F(y)<u\}$, let $B_u:=\{x\in\mathbb{R}:F(x)\ge u\}$, and write $s:=\sup A_u$. The goal is to prove that $B_u=[s,\infty)$, because then automatically $\inf B_u=s=\sup A_u$. The next steps are therefore to understand what happens to points left of $s$, right of $s$, and exactly at $s$.

Step (1): if $x<s$, then $x\notin B_u$. Since $s$ is the supremum of $A_u$, there exists some $y\in A_u$ with $x<y\le s$. Because $F$ is nondecreasing, $F(x)\le F(y)<u$, so $F(x)<u$, hence $x\notin B_u$.

Step (2): if $x>s$, then $x\in B_u$. If not, then $F(x)<u$, so $x\in A_u$. But that contradicts $x>s=\sup A_u$. Therefore every point strictly to the right of $s$ lies in $B_u$.

Step (3): the boundary point $s$ itself also lies in $B_u$. Indeed, if $F(s)<u$, then right-continuity at $s$ gives some $\delta>0$ such that $F(s+\delta)<u$. Then $s+\delta\in A_u$, contradicting the definition of $s$ as the supremum of $A_u$. So $F(s)\ge u$, hence $s\in B_u$.

Step (4): combine the three steps. Step (1) says no point left of $s$ is in $B_u$, while Steps (2) and (3) say every point at or to the right of $s$ is in $B_u$. Therefore $B_u=[s,\infty)$.

Now the two formulas agree: $\sup\{y:F(y)<u\}=s=\inf\{x:F(x)\ge u\}$.

That is exactly the behavior one wants. A jump of size $P[\{x\}]$ in the cumulative distribution function means there should be an interval of uniform input values whose entire mass is sent to the atom $x$. A flat part means no probability mass lies there, so no uniform input values should be assigned to interior points of that flat region.

---

Flashcards for this section are as follows:

- pseudoinverse intuition ::@:: The pseudoinverse comes from trying to solve the inverse-transform equation $u=F(x)$: if $F$ were strictly increasing and continuous, one would generate $X$ from a uniform $U$ by setting $X=F^{-1}(U)$, so the generalized inverse is designed to preserve this idea when ordinary inverses fail. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what $X$ means in the inverse-transform heuristic ::@:: In the heuristic identity $U=F(X)$, the symbol $X$ denotes a real random variable whose cumulative distribution function is the target function $F$; the point is to recover such an $X$ from a uniform random variable $U$.
- why the ordinary inverse usually fails for a cumulative distribution function ::@:: A general cumulative distribution function can have flat parts and jumps, so it need not be one-to-one or continuous; an ordinary inverse may therefore not exist.
- pseudoinverse as first hitting point of a level ::@:: The generalized inverse chooses the first point where the cumulative distribution function has reached the level $u$, so it can still solve the inverse-transform problem even when the graph has plateaus or jumps. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- inf-definition of the pseudoinverse ::@:: A natural generalized-inverse definition is $F^{-1}(u)=\inf\{x\in\mathbb{R}:F(x)\ge u\}$, meaning the leftmost point where the graph has already reached level $u$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- course definition of the pseudoinverse ::@:: The course writes the generalized inverse as $F^{-1}(u)=\sup\{y\in\mathbb{R}:F(y)<u\}$, meaning the last point whose cumulative value is still strictly below $u$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- pseudoinverse / next step intuition ::@:: To compare the two formulas, one should not manipulate the sup and inf directly. Instead, define the threshold sets $A_u$ and $B_u$, introduce $s=\sup A_u$, and then check what happens left of $s$, right of $s$, and at the boundary point $s$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- pseudoinverse equivalence
  - pseudoinverse equivalence / setup ::@:: To compare the two formulas, fix $u\in(0,1)$ and define $A_u=\{y:F(y)<u\}$, $B_u=\{x:F(x)\ge u\}$, and $s=\sup A_u$; the goal is to prove $B_u=[s,\infty)$, because then $\inf B_u=s=\sup A_u$. The next steps are to check points left of $s$, right of $s$, and finally the boundary point $s$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - pseudoinverse equivalence / left of $s$ ::@:: If $x<s$, then some $y\in A_u$ satisfies $x<y\le s$; monotonicity gives $F(x)\le F(y)<u$, so $x\notin B_u$. Thus no point left of $s$ belongs to $\{x:F(x)\ge u\}$.
  - pseudoinverse equivalence / right of $s$ ::@:: If $x>s$ and $x\notin B_u$, then $F(x)<u$, so $x\in A_u$, contradicting $x>s=\sup A_u$. Hence every point right of $s$ belongs to $\{x:F(x)\ge u\}$.
  - pseudoinverse equivalence / boundary point ::@:: If $F(s)<u$, right-continuity gives some $\delta>0$ with $F(s+\delta)<u$, so $s+\delta\in A_u$, contradicting $s=\sup A_u$. Therefore $F(s)\ge u$, so the boundary point $s$ also lies in $B_u$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - pseudoinverse equivalence / conclusion ::@:: The previous steps show $B_u=[s,\infty)$ with $s=\sup A_u$, so $\sup\{y:F(y)<u\}=s=\inf\{x:F(x)\ge u\}$. Intuitively, both formulas pick the same threshold point where the graph stops being below level $u$ and starts being at least level $u$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what a jump means for the pseudoinverse ::@:: If $F$ has a jump at $x$, then the whole interval of uniform levels covered by that jump is sent by the pseudoinverse to the single point $x$; this is how the construction creates atoms. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what a flat part means for the pseudoinverse ::@:: If $F$ is flat on an interval, then no uniform levels are assigned to interior points of that interval, reflecting the fact that the distribution puts no mass there. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### abstract pushforward proof

The clean abstract viewpoint is to define a map $T:(0,1)\to\mathbb{R}$ by $T(u)=F^{-1}(u)$ and then form a new measure on $\mathbb{R}$ from uniform measure on $(0,1)$ by the rule $(T_{\ast}\mu)(A):=\mu(T^{-1}(A))$. In this notation the symbol $T_{\ast}$ means transport the measure through the map $T$.

Let $\lambda_{(0,1)}$ denote Lebesgue measure restricted to $(0,1)$. Because the interval $(0,1)$ has length $1$, this is already a probability measure. Probabilistically, $\lambda_{(0,1)}$ is exactly the law of a random variable $U\sim\mathrm{U}(0,1)$.

Next, if $A\subseteq\mathbb{R}$, the _preimage_ of $A$ under $T$ is defined by $T^{-1}(A):=\{u\in(0,1):T(u)\in A\}$.

So $T^{-1}(A)$ is the set of input values $u$ whose image under $T$ lands inside $A$.

Now define a measure $P$ on $\mathbb{R}$ by $P:=T_{\ast}\lambda_{(0,1)}$. This means the following, with the operator written out in full: for every Borel set $A\subseteq\mathbb{R}$, one defines $P[A]=(T_{\ast}\lambda_{(0,1)})(A):=\lambda_{(0,1)}(T^{-1}(A))$. In words: look at all points $u\in(0,1)$ that are sent into $A$ by $T$, and then take the uniform measure of that set of inputs. This is just the measure-theoretic way to say that if $U\sim\mathrm{U}(0,1)$, then the law of $T(U)$ is the transported measure denoted by $T_{\ast}\lambda_{(0,1)}$.

This definition is legitimate for two separate reasons.

First, $T$ is measurable. Indeed, $T=F^{-1}$ is nondecreasing, and every monotone real-valued function is Borel measurable. Therefore, whenever $A$ is a Borel set in $\mathbb{R}$, its preimage $T^{-1}(A)$ is a Borel subset of $(0,1)$. So the quantity $\lambda_{(0,1)}(T^{-1}(A))$ is actually defined for every Borel set $A$.

Second, the assignment $A\mapsto \lambda_{(0,1)}(T^{-1}(A))$ really is a probability measure, not just a formal expression. One has $T^{-1}(\varnothing)=\varnothing$ and $T^{-1}(\mathbb{R})=(0,1)$, so the empty set gets mass $0$ and the whole space gets mass $1$. Also, preimages preserve unions: $T^{-1}(\bigcup_{n=1}^{\infty}A_n)=\bigcup_{n=1}^{\infty}T^{-1}(A_n)$. If the sets $A_n$ are pairwise disjoint, then the sets $T^{-1}(A_n)$ are also pairwise disjoint, because one input value $u$ cannot be sent simultaneously into two disjoint target sets. Therefore $$P\Big[\bigcup_{n=1}^{\infty}A_n\Big]=\lambda_{(0,1)}\Big(T^{-1}\Big(\bigcup_{n=1}^{\infty}A_n\Big)\Big)=\lambda_{(0,1)}\Big(\bigcup_{n=1}^{\infty}T^{-1}(A_n)\Big)=\sum_{n=1}^{\infty}\lambda_{(0,1)}(T^{-1}(A_n))=\sum_{n=1}^{\infty}P[A_n].$$

So the pushforward formula is legitimate because measurability makes every preimage measurable, and the basic set-theoretic behavior of preimages transfers countable additivity from $\lambda_{(0,1)}$ to the new measure $P$.

From this perspective, the proof becomes a generator argument. We do not try to compute $P[A]$ for every Borel set $A$ at once. Instead we first compute it on the generating half-lines $(-\infty,x]$.

For such a half-line, it helps to unpack the preimage step by step rather than jump straight to the answer. By definition of preimage, $$T^{-1}(( -\infty,x])=\{u\in(0,1):T(u)\in(-\infty,x]\}=\{u\in(0,1):T(u)\le x\}.$$

Since $T(u)=F^{-1}(u)$, this becomes $$T^{-1}(( -\infty,x])=\{u\in(0,1):F^{-1}(u)\le x\}.$$

Now the concrete pseudoinverse argument supplies the key order relation $F^{-1}(u)\le x \Longleftrightarrow u\le F(x)$. So the previous set can be rewritten as $$T^{-1}(( -\infty,x])=\{u\in(0,1):u\le F(x)\}=(0,F(x)]\cap(0,1).$$

This identity is the heart of the proof. The left-hand side asks which uniform input levels are sent by $T$ into the target half-line $(-\infty,x]$. The right-hand side answers: exactly those levels that lie below the cumulative height already reached by time $x$. So the abstract proof reduces the half-line probability on the real line to the length of an initial interval inside $(0,1)$, where the reference measure is completely transparent.

Applying $\lambda_{(0,1)}$ gives $P(( -\infty,x])=\lambda_{(0,1)}((0,F(x)]\cap(0,1))=F(x)$, because the uniform measure of $(0,t]\cap(0,1)$ is exactly $t$ for $0\le t\le1$, and every cumulative distribution function satisfies $0\le F(x)\le1$.

So the measure $P$, namely the transported measure defined by $P[A]=\lambda_{(0,1)}(T^{-1}(A))$, has cumulative distribution function $F$. That proves existence again, now in a more structural language.

The advantage of this viewpoint is conceptual clarity. The reference probability space is the simple interval $(0,1)$ with uniform measure, the map $T=F^{-1}$ transports that mass to the real line, and the verification is reduced to one generating family of sets. Uniqueness is then the familiar second generator step on the target side: if two probability measures have the same cumulative distribution function, then they agree on all half-lines $(-\infty,x]$, and since those half-lines generate $\mathcal{B}(\mathbb{R})$, the pi-lambda argument shows the measures are equal everywhere.

---

Flashcards for this section are as follows:

- abstract pushforward proof
  - abstract pushforward proof / overview ::@:: The Lebesgue-Stieltjes construction can be written abstractly as follows: define $T(u)=F^{-1}(u)$, then define a new measure $P$ by $P[A]=(T_{\ast}\lambda_{(0,1)})(A):=\lambda_{(0,1)}(T^{-1}(A))$. In words, $T_{\ast}$ means transport the uniform measure on $(0,1)$ through the map $T$ and measure a target set $A$ by the size of all inputs that land in it. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - abstract pushforward proof / meaning of $T_{\ast}$ ::@:: The symbol $T_{\ast}$ means push the measure forward through $T$: given a measure $\mu$ on the domain, the new measure $T_{\ast}\mu$ on the target is defined by $(T_{\ast}\mu)(A)=\mu(T^{-1}(A))$.
  - abstract pushforward proof / meaning of $\lambda_{(0,1)}$ ::@:: $\lambda_{(0,1)}$ is Lebesgue measure restricted to $(0,1)$; because $(0,1)$ has length $1$, it is already a probability measure, namely the law of $U\sim\mathrm{U}(0,1)$.
  - abstract pushforward proof / meaning of preimage ::@:: For a set $A\subseteq\mathbb{R}$, the preimage $T^{-1}(A)=\{u\in(0,1):T(u)\in A\}$ is the set of uniform inputs whose images under $T$ land in $A$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - abstract pushforward proof / legitimacy
    - abstract pushforward proof / legitimacy / measurability of $T$ ::@:: The map $T(u)=F^{-1}(u)$ is nondecreasing, so it is Borel measurable. Therefore, if $A$ is a Borel set in $\mathbb{R}$, then the preimage $T^{-1}(A)$ is a Borel subset of $(0,1)$ and $\lambda_{(0,1)}(T^{-1}(A))$ is well defined.
    - abstract pushforward proof / legitimacy / why the formula defines a measure ::@:: The assignment $P[A]=\lambda_{(0,1)}(T^{-1}(A))$ is a measure because preimages preserve the empty set, the whole space, and countable unions; moreover, disjoint target sets have disjoint preimages, so countable additivity of $\lambda_{(0,1)}$ transfers directly to $P$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
    - abstract pushforward proof / legitimacy / why it is a probability measure ::@:: Since $T^{-1}(\mathbb{R})=(0,1)$, one gets $P[\mathbb{R}]=\lambda_{(0,1)}((0,1))=1$. So the pushforward is not merely a measure but a probability measure. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - abstract pushforward proof / next step intuition ::@:: Once $P[A]=(T_{\ast}\lambda_{(0,1)})(A):=\lambda_{(0,1)}(T^{-1}(A))$ is defined, the next step is not to study all Borel sets at once. Instead, compute the preimage of the generating half-line $(-\infty,x]$, because once that is understood, the cumulative distribution function follows immediately. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - abstract pushforward proof / meaning of $P=T_{\ast}\lambda_{(0,1)}$ ::@:: The notation $P=T_{\ast}\lambda_{(0,1)}$ means that for every Borel set $A$, one defines $P[A]=(T_{\ast}\lambda_{(0,1)})(A):=\lambda_{(0,1)}(T^{-1}(A))$; the probability assigned to $A$ is the uniform mass of all inputs sent into $A$ by $T$.
  - abstract pushforward proof / key identity
    - abstract pushforward proof / key identity / first rewrite ::@:: For the generating half-line $(-\infty,x]$, the preimage definition gives $T^{-1}(( -\infty,x])=\{u\in(0,1):T(u)\le x\}$. The next step is then to substitute the specific map $T(u)=F^{-1}(u)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
    - abstract pushforward proof / key identity / insert the pseudoinverse ::@:: Substituting $T(u)=F^{-1}(u)$ gives $T^{-1}(( -\infty,x])=\{u\in(0,1):F^{-1}(u)\le x\}$. This is the exact point where the abstract proof imports the concrete generalized-inverse identity. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
    - abstract pushforward proof / key identity / order comparison ::@:: The concrete pseudoinverse argument proves $F^{-1}(u)\le x$ if and only if $u\le F(x)$, so the previous set becomes $\{u\in(0,1):u\le F(x)\}$. The abstract proof works because it converts a target-space inequality into a simple input-space inequality. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
    - abstract pushforward proof / key identity / interval form and interpretation ::@:: Since $u$ already ranges over $(0,1)$, the set $\{u\in(0,1):u\le F(x)\}$ is exactly $(0,F(x)]\cap(0,1)$. Intuitively, the inputs sent into $(-\infty,x]$ are precisely the uniform levels already reached by the cumulative distribution function at $x$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
    - abstract pushforward proof / key identity / measure computation ::@:: Therefore $P(( -\infty,x])=\lambda_{(0,1)}(T^{-1}(( -\infty,x]))=\lambda_{(0,1)}((0,F(x)]\cap(0,1))=F(x)$. So the pushforward measure has cumulative distribution function exactly equal to $F$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - abstract pushforward proof / why half-lines are enough ::@:: The half-lines $(-\infty,x]$ generate $\mathcal{B}(\mathbb{R})$, so once the pushforward measure has the correct values on them, its cumulative distribution function is identified; uniqueness then extends equality from that generator to all Borel sets. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - abstract pushforward proof / interpretation ::@:: The abstract proof separates the construction into three transparent ingredients: a reference measure $\lambda_{(0,1)}$, a transport rule $(T_{\ast}\mu)(A)=\mu(T^{-1}(A))$, and a generator check on half-lines. Intuitively, it is the same inverse-transform idea as the concrete proof, but rewritten at the level of measures instead of sample points. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## absolutely continuous and singular continuous distributions

We also clarify an important distinction: a continuous cumulative distribution function need not come from a density. What characterizes density-based laws is not mere continuity of the cumulative distribution function, but _absolute continuity_.

Let $X$ be a real random variable, let $P_X$ be its law on $(\mathbb{R},\mathcal{B}(\mathbb{R}))$, and let $F_X$ be its cumulative distribution function. Then the following four conditions are equivalent.

First condition: there exists a nonnegative measurable function $f$ on $\mathbb{R}$ such that for every Borel set $A\subseteq\mathbb{R}$, one has $$P[X\in A]=\int_A f(x)\,dx,$$ where the integral is the Lebesgue integral. This is the most direct density formulation: probabilities of all Borel sets are obtained by integrating one nonnegative measurable function.

Second condition: the cumulative distribution function $F_X$ is absolutely continuous. Concretely, this means that for every $\varepsilon>0$ there exists $\delta>0$ such that whenever $(a_k,b_k)$ are pairwise disjoint intervals with total length $\sum_k (b_k-a_k)<\delta$, one has $\sum_k |F_X(b_k)-F_X(a_k)|<\varepsilon$. This is the function-theoretic formulation.

Third condition: for every Borel set $A\subseteq\mathbb{R}$ with Lebesgue measure $\lambda(A)=0$, one has $P[X\in A]=0$. This is the measure-theoretic statement that the law of $X$ is absolutely continuous with respect to Lebesgue measure.

Fourth condition: for every $\varepsilon>0$ there exists $\delta>0$ such that whenever $A\subseteq\mathbb{R}$ is a Borel set with $\lambda(A)<\delta$, one has $P[X\in A]<\varepsilon$. This is the epsilon-delta form of absolute continuity for the measure induced by $X$.

So the right four-way equivalence is: density on all Borel sets, absolute continuity of the cumulative distribution function, vanishing probability on Lebesgue-null Borel sets, and the epsilon-delta small-set criterion for Borel sets.

These are not four unrelated facts. Condition (1) says that the law has a density. Condition (2) says the same thing at the level of the cumulative distribution function. Condition (3) says the law ignores every Lebesgue-null set. Condition (4) strengthens that intuition by saying that sets of sufficiently small Lebesgue measure must carry arbitrarily small probability.

So an absolutely continuous cumulative distribution function is precisely the same thing as a distribution that admits a density in the full measure-theoretic sense. This is the correct converse to the density-based viewpoint from continuous distributions.

By contrast, a _singular continuous distribution_ has a cumulative distribution function that is continuous but not absolutely continuous. Such a law has no atoms, because continuity rules out jumps, but it is still singular with respect to Lebesgue measure, so it cannot be written as $\int_{-\infty}^x f(t)\,dt$ for a density $f$. The Cantor distribution is the classical example: its cumulative distribution function is continuous and nondecreasing, but it increases only on a set of Lebesgue measure $0$.

This gives the clean trichotomy on the real line. Jumps correspond to atoms, absolutely continuous growth corresponds to density-based mass, and continuous but singular growth corresponds to singular continuous mass. The cumulative distribution function is the object that makes all three behaviors visible in a unified way.

---

Flashcards for this section are as follows:

- absolutely continuous cumulative distribution function
  - absolutely continuous cumulative distribution function / overview ::@:: For a real random variable $X$, the following are equivalent: (1) there is a nonnegative measurable density $f$ with $P[X\in A]=\int_A f(x)\,dx$ for every Borel set $A$, (2) the cumulative distribution function $F_X$ is absolutely continuous, (3) every Lebesgue-null Borel set has probability $0$, and (4) sets of sufficiently small Lebesgue measure have arbitrarily small probability. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - absolutely continuous cumulative distribution function / density on Borel sets ::@:: One equivalent condition is that there exists a nonnegative measurable function $f$ on $\mathbb{R}$ such that for every Borel set $A$, one has $P[X\in A]=\int_A f(x)\,dx$, where the integral is Lebesgue. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - absolutely continuous cumulative distribution function / cdf formulation ::@:: An equivalent condition is that the cumulative distribution function $F_X$ is absolutely continuous, meaning that for every $\varepsilon>0$ there exists $\delta>0$ such that pairwise disjoint intervals with total length less than $\delta$ produce total variation in $F_X$ less than $\varepsilon$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - absolutely continuous cumulative distribution function / null-set formulation ::@:: An equivalent condition is that if $A$ is a Borel set with Lebesgue measure $0$, then $P[X\in A]=0$. This says the law of $X$ is absolutely continuous with respect to Lebesgue measure. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - absolutely continuous cumulative distribution function / epsilon-delta small-set formulation ::@:: An equivalent condition is that for every $\varepsilon>0$ there exists $\delta>0$ such that every Borel set $A$ with Lebesgue measure less than $\delta$ satisfies $P[X\in A]<\varepsilon$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
  - absolutely continuous cumulative distribution function / why these are the same idea ::@:: These four conditions all say that the law of $X$ is spread in the same way as Lebesgue measure: it is described by a density, its cumulative distribution function is absolutely continuous, it vanishes on null sets, and it gives very small probability to sets of very small Lebesgue measure. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- continuity versus absolute continuity ::@:: Mere continuity of a cumulative distribution function does not imply the existence of a density; the correct condition is absolute continuity.
- singular continuous distribution ::@:: A singular continuous distribution has a cumulative distribution function that is continuous but not absolutely continuous; it has no atoms, yet it is not described by a density with respect to Lebesgue measure.
- why the Cantor distribution is singular continuous ::@:: The Cantor distribution is singular continuous because its cumulative distribution function has no jumps, so there are no atoms, but the probability mass is concentrated on the Cantor set, which has Lebesgue measure $0$, so no density exists. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- trichotomy seen from the cumulative distribution function ::@:: On the real line, jumps in the cumulative distribution function correspond to atoms, absolutely continuous growth corresponds to density-based mass, and continuous but singular growth corresponds to singular continuous mass.
