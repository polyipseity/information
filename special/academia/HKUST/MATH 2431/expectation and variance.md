---
aliases:
  - expectation
  - expectation and variance
  - variance
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/expectation_and_variance
  - language/in/English
---

# expectation and variance

Expectation extracts the average size of a random quantity from its law, while variance, covariance, and the standard deviation quantify how widely a random quantity fluctuates.

In the second half of the course these notions become structural tools: they feed directly into Markov-type bounds, covariance computations, and the law of large numbers.

---

Flashcards for this section are as follows:

<!-- check: ignore-line[two_sided_calc_warning]: conceptual --> - overview ::@:: Expectation is the average determined by the law of a random variable (the $L^1$ integral under $P$), while variance measures the average squared deviation from the mean (the $L^2$ distance to $E[X]$).

## alternative definition via discretization

<!-- Added from PDF: Lemma 6.3, Def 6.4, pages 49--51 -->
One may also define expectation without direct recourse to densities or sums by first treating simple (finite-range) variables, then extending via discretization. For a nonnegative random variable $X$, set $$X_n = 2^{-n} \lfloor 2^n X \rfloor.$$ Each $X_n$ is simple (it takes only dyadic rational values), so its expectation $E[X_n]$ is defined as a finite sum. Moreover $X_n \uparrow X$ pointwise, and one defines $E[X] = \lim_{n\to\infty} E[X_n]$, which exists as an extended real number (possibly $\infty$). For general (possibly signed) $X$, split $X = X^+ - X^-$ with $X^+ = \max\{X,0\}$, $X^- = \max\{-X,0\}$; the expectation is defined when at least one of $E[X^+]$, $E[X^-]$ is finite, and is finite when both are finite.

The tail-sum and density formulas are consequences of this discretization (or of the layer-cake representation), so all approaches are equivalent.

---

Flashcards for this section are as follows:

- alternative definition via discretization / purpose ::@:: Instead of defining expectation separately for discrete sums and continuous integrals, one first defines it for simple variables, then extends via dyadic discretization $X_n = 2^{-n}\lfloor 2^n X\rfloor$. This gives a unified definition that works for any random variable. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- dyadic discretization / construction for $X\ge0$ ::@:: $X_n = 2^{-n}\lfloor 2^n X\rfloor$. At each $\omega$, $X_n(\omega)$ rounds $X(\omega)$ down to the nearest dyadic rational $k/2^n$ ($k\in\mathbb N_0$), so $X_n$ is simple (finite range). As $n\to\infty$, $X_n\uparrow X$ pointwise. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- expectation via discretization / definition for $X\ge0$ ::@:: $E[X] = \lim_{n\to\infty} E[X_n]$ where $X_n=2^{-n}\lfloor 2^n X\rfloor$. The limit exists in $[0,\infty]$ (monotone convergence of the simple-function expectations). <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- expectation via discretization / extension to signed $X$ ::@:: Split $X = X^+ - X^-$ where $X^+=\max\{X,0\}$, $X^-=\max\{-X,0\}$. Define $E[X] = E[X^+] - E[X^-]$ provided at least one of $E[X^+]$, $E[X^-]$ is finite (avoids $\infty-\infty$). $E[X]$ is finite iff both $E[X^+]$ and $E[X^-]$ are finite. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- expectation definitions / equivalence ::@:: The tail-sum formula, density integrals, and PMF sums are all consequences of the discretization definition (or the layer-cake representation), so they are consistent: any of these approaches yields the same value of $E[X]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->

## expectation of discrete random variables

If $X$ is discrete with probability mass function $p_X$, then $E[X]=\sum_x x\,p_X(x)$, provided the series converges absolutely. More generally, if $X\ge 0$ is $\mathbb N$-valued, then $E[X]=\sum_{n=1}^{\infty} P[X\ge n]$. This tail-sum formula is often easier to use than the definition.

__Proof.__ Write each integer $k\ge 1$ as $k=\sum_{n=1}^k 1$. Then $E[X]=\sum_{k=1}^{\infty} kP[X=k]=\sum_{k=1}^{\infty}\sum_{n=1}^k P[X=k]$. Since all terms are nonnegative, Tonelli's theorem allows us to reverse the sums and obtain $E[X]=\sum_{n=1}^{\infty}\sum_{k=n}^{\infty}P[X=k]=\sum_{n=1}^{\infty}P[X\ge n]$.

Expectation depends only on the law of $X$. Thus if $X$ and $Y$ satisfy $X\stackrel d=Y$ and either expectation exists, then $E[X]=E[Y]$. The proof is immediate from the formula above, since the mass function is determined by the law.

---

Flashcards for this section are as follows:

- expectation of a discrete random variable: If $X$ has PMF $p_X$, what is $E[X]$? ::@:: $E[X]=\sum_x x\,p_X(x)$ provided $\sum_x |x|\,p_X(x)<\infty$ (absolute convergence guarantees the sum is independent of ordering). <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- tail-sum formula for a nonnegative integer-valued variable: If $X\ge 0$ is $\mathbb N$-valued, what is $E[X]$? ::@:: $E[X]=\sum_{n=1}^{\infty}P[X\ge n]$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- tail-sum proof technique: How do you prove $E[X]=\sum_{n\ge1}P[X\ge n]$ for $\mathbb N$-valued $X$? ::@:: Write each integer $k$ as $\sum_{n=1}^k 1$, so $E[X]=\sum_{k\ge1}\sum_{n=1}^k P[X=k]$; swap sums (Tonelli, nonnegative) to get $\sum_{n\ge1}\sum_{k\ge n}P[X=k]=\sum_{n\ge1}P[X\ge n]$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- expectation depends only on law: If $X\stackrel d=Y$ and either expectation exists, why is $E[X]=E[Y]$? ::@:: Because expectation depends only on $P_X$ (via PMF, density, or the general discretization definition); $X\stackrel d=Y$ means $P_X=P_Y$, hence their expectations coincide. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->

## expectation of continuous random variables

If $X$ has density $f_X$, then $E[X]=\int_{-\infty}^{\infty} x f_X(x)\,dx$, again under absolute integrability. For nonnegative real-valued random variables the continuous tail formula is $E[X]=\int_0^{\infty} P[X>t]\,dt=\int_0^{\infty}(1-F_X(t))\,dt$.

__Proof.__ Since $X(\omega)=\int_0^{\infty}\mathbf 1_{\{X(\omega)>t\}}\,dt$ for every nonnegative value $X(\omega)$, Tonelli gives $E[X]=E\left[\int_0^{\infty}\mathbf 1_{\{X>t\}}\,dt\right]=\int_0^{\infty}E[\mathbf 1_{\{X>t\}}]dt=\int_0^{\infty}P[X>t]dt$. For the exponential law $X\sim E(\lambda)$, this yields immediately $E[X]=\int_0^{\infty}e^{-\lambda t}\,dt=1/\lambda$.

---

Flashcards for this section are as follows:

- expectation from a density: If $X$ has density $f_X$, how do you compute $E[X]$? ::@:: $E[X]=\int_{-\infty}^{\infty}x f_X(x)\,dx$ whenever $\int_{-\infty}^{\infty}|x|f_X(x)dx<\infty$ (absolute integrability guarantees a well-defined finite value). <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- tail-integral formula for a nonnegative variable: If $X\ge 0$, what is $E[X]$ in terms of tails? ::@:: $E[X]=\int_0^{\infty}P[X>t]dt=\int_0^{\infty}(1-F_X(t))dt$; this holds for any $X\ge0$ regardless of whether $X$ is discrete, continuous, or mixed. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- tail-integral proof technique: How do you prove $E[X]=\int_0^\infty P[X>t]dt$ for $X\ge0$? ::@:: Write $X(\omega)=\int_0^\infty\mathbf 1_{\{X(\omega)>t\}}dt$ (layer-cake representation); take expectation and swap order via Tonelli (nonnegative integrand). <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- exponential expectation from tail integral: For $X\sim E(\lambda)$, what does the tail-integral formula give? ::@:: $E[X]=\int_0^\infty e^{-\lambda t}dt=1/\lambda$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->

## expectation of transformed random variables

If $g$ is measurable and $g(X)$ is integrable, then expectation may be computed directly from the law of $X$: in the discrete case $E[g(X)]=\sum_x g(x)p_X(x)$, and in the continuous case $E[g(X)]=\int_{-\infty}^{\infty} g(x)f_X(x)\,dx$. This is the law of the unconscious statistician. Its proof is simply that the law of $g(X)$ is the pushforward of the law of $X$, so one may integrate over the value space instead of the sample space.

Two standard special cases are worth isolating.

- If $A\in\mathcal F$, then $E[\mathbf 1_A]=P[A]$.
- If $g(x)=x^n$, then $E[g(X)]$ is the moment of order $n$.

As an example, if $X\sim \mathrm{Pois}(\lambda)$, then $E[e^{tX}]=\sum_{k=0}^{\infty} e^{tk}e^{-\lambda}\frac{\lambda^k}{k!}=\exp(\lambda(e^t-1))$, which is the moment generating function of the Poisson law.

<!-- Added from PDF: Example 6.6(ix), page 55 -->
__Example (nonexistent expectation: Cauchy).__ Let $X$ have the standard Cauchy density $$f_X(x) = \frac{1}{\pi}\cdot\frac{1}{1+x^2}, \qquad x \in \mathbb R.$$ Then $$E[|X|] = \frac{2}{\pi}\int_0^\infty \frac{x}{1+x^2}\,dx = \frac{2}{\pi}\left[ \frac{1}{2}\ln(1+x^2)\right]_0^\infty = \infty,$$ so the absolute expectation is infinite and $E[X]$ is defined _not to exist_ under the Lebesgue integral definition. (The improper Riemann integral $\lim_{a\to\infty}\int_{-a}^{a} x f_X(x)\,dx$ converges to $0$ by symmetry, but this Cauchy principal value does not satisfy the requirement $\int |x| f_X(x)\,dx < \infty$.)

The failure can also be seen from the tail-sum formula: for $t>0$, $$P(X > t) = \frac{1}{\pi}\int_t^\infty \frac{dx}{1+x^2} = \frac{1}{\pi}\bigl(\tfrac{\pi}{2} - \arctan t\bigr) \sim \frac{1}{\pi t} \quad \text{as } t\to\infty,$$ so $\int_0^\infty P(X > t)\,dt$ diverges logarithmically.

---

Flashcards for this section are as follows:

- law of the unconscious statistician, discrete version: If $X$ has PMF $p_X$ and $g(X)$ is integrable, how do you compute $E[g(X)]$? ::@:: $E[g(X)]=\sum_x g(x)p_X(x)$. Integrate $g$ against the law of $X$ directly, without finding the distribution of $g(X)$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- law of the unconscious statistician, continuous version: If $X$ has density $f_X$ and $g(X)$ is integrable, how do you compute $E[g(X)]$? ::@:: $E[g(X)]=\int_{-\infty}^{\infty} g(x)f_X(x)\,dx$. Again, no need to derive the density of $g(X)$; the original law of $X$ suffices. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- indicator expectation: For an event $A$, what is $E[\mathbf 1_A]$? ::@:: $E[\mathbf 1_A]=P[A]$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- moment definition: For $k\in\mathbb N$, what is the (raw) moment of order $k$ of $X$? ::@:: $E[X^k]$, provided $E[|X|^k]<\infty$. The first moment ($k=1$) is the mean; the second ($k=2$) feeds into $\operatorname{Var}(X)=E[X^2]-(E[X])^2$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Poisson moment generating function: If $X\sim\mathrm{Pois}(\lambda)$, what is $E[e^{tX}]$, i.e. the MGF $M_X(t)$? ::@:: $E[e^{tX}]=\sum_{k=0}^\infty e^{tk}e^{-\lambda}\lambda^k/k!=\exp(\lambda(e^t-1))$, valid for all $t\in\mathbb R$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- expectation may not exist / Cauchy counterexample ::@:: The standard Cauchy distribution has $E[|X|]=\infty$, so $E[X]$ does not exist under the Lebesgue definition (even though the principal-value Riemann integral $\lim_{a\to\infty}\int_{-a}^{a}x f_X(x)dx=0$ by symmetry). Absolute integrability $\int_{-\infty}^{\infty}|x|f_X(x)dx<\infty$ is required for existence. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->

## linearity of expectation

The key algebraic fact is that expectation is linear: $E[aX+bY+c]=aE[X]+bE[Y]+c$ whenever the expectations exist.

__Proof.__ In the discrete case this follows by distributing the sum over the probability weights; in the continuous case it follows by linearity of the integral. No independence assumption is needed.

This is why indicator decompositions are powerful. If $X=\sum_{j=1}^n \mathbf 1_{A_j}$ counts how many events occur, then $E[X]=\sum_{j=1}^n P[A_j]$.

This argument proves, for instance, that the expected number of fixed points in a uniform random permutation is $1$.

Let $\pi$ be a uniform random permutation of $\{1,\dots,n\}$, so each of the $n!$ orderings is equally likely. For each position $i$, define the indicator $I_i=\mathbf 1_{\{\pi(i)=i\}}$. The total number of fixed points is $X=\sum_{i=1}^n I_i$, and by linearity $E[X]=\sum_{i=1}^n E[I_i]=\sum_{i=1}^n P[\pi(i)=i]$.

Since $\pi$ is uniform, position $i$ is equally likely to contain any of the $n$ elements; hence $P[\pi(i)=i]=1/n$ for every $i$, and $E[X]=n\cdot1/n=1$.

The intuition is symmetry: every position has the same chance $1/n$ of being fixed, and linearity lets us add the $n$ identical contributions without worrying about the complicated dependencies among the indicators. Note that the distribution of $X$ is not concentrated around $1$ — for large $n$, the probability of no fixed points tends to $1/e\approx0.368$ — but linearity alone suffices to obtain the exact expectation.

<!-- Added from PDF: Example 6.1, page 49 -->
__Example (die game).__ A fair die is rolled. If the outcome is $i$, the player receives a payout of $x \cdot i$ dollars; the cost to play is $c$ dollars. The net gain is $G = x D - c$, where $D$ is the face value of the die. The expected gain is $$E[G] = x \cdot \frac{1+2+3+4+5+6}{6} - c = x \cdot \frac{21}{6} - c = 3.5 x - c.$$ The game is _fair_ when $E[G] = 0$, i.e. $3.5 x = c$. For instance, $x = 2$ and $c = 7$ yields a fair game. The problem illustrates how linearity of expectation reduces a random-payout computation to a simple weighted sum.

---

Flashcards for this section are as follows:

- linearity of expectation: If the expectations exist, what is $E[aX+bY+c]$? ::@:: $E[aX+bY+c]=aE[X]+bE[Y]+c$. Linearity works for any finite linear combination; no independence is required. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- linearity needs no independence: What hypothesis is _not_ needed for $E[X+Y]=E[X]+E[Y]$? ::@:: No independence assumption is needed. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- indicator decomposition: If $X=\sum_{j=1}^n\mathbf 1_{A_j}$ counts events, what is $E[X]$? ::@:: $E[X]=\sum_{j=1}^n P[A_j]$ by linearity of expectation. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- fixed points in random permutation: In a uniform random permutation of $\{1,\dots,n\}$, what is the expected number of fixed points, and what is the derivation? ::@:: 1. Let $I_i=\mathbf 1_{\{\pi(i)=i\}}$; then $X=\sum_{i=1}^n I_i$ and $E[X]=\sum_{i=1}^n P[\pi(i)=i]=n\cdot1/n=1$ by linearity. Each position is equally likely to contain any element, so $P[\pi(i)=i]=1/n$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- die game / expected gain and fair condition ::@:: Roll a fair die, payout $x$ times face value $D$, cost $c$. Net gain $G=xD-c$, expected gain $E[G]=3.5x-c$. The game is fair when $c=3.5x$ ($E[G]=0$). This illustrates linearity: $E[G]=xE[D]-c$ with $E[D]=3.5$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->

## variance and standard deviation

For a square-integrable random variable, $\operatorname{Var}(X)=E[(X-E[X])^2]$ and $\operatorname{sd}(X)=\sqrt{\operatorname{Var}(X)}$. Expanding the square gives the computational identity $\operatorname{Var}(X)=E[X^2]-(E[X])^2$.

__Proof.__ One has $E[(X-E[X])^2]=E[X^2]-2E[X]E[X]+(E[X])^2=E[X^2]-(E[X])^2$.

Since the left-hand side is the expectation of a nonnegative variable, variance is always nonnegative, and it vanishes exactly when $X=E[X]$ almost surely.

Affine changes behave in the expected way: $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$. The constant shift disappears because variance measures spread around the center rather than location.

Important examples are:

- $X\sim\mathrm{Ber}(p)$: $E[X]=p$, $\operatorname{Var}(X)=p(1-p)$;
- $X\sim\mathrm{Bin}(n,p)$: $E[X]=np$, $\operatorname{Var}(X)=np(1-p)$;
- $X\sim\mathrm{Pois}(\lambda)$: $E[X]=\lambda$, $\operatorname{Var}(X)=\lambda$;
- $X\sim N(\mu,\sigma^2)$: $E[X]=\mu$, $\operatorname{Var}(X)=\sigma^2$;
- $X\sim\mathrm{Geo}(p)$: $E[X]=1/p$, $\operatorname{Var}(X)=(1-p)/p^2$;
- $X\sim\mathrm{Exp}(\lambda)$: $E[X]=1/\lambda$, $\operatorname{Var}(X)=1/\lambda^2$;
- $X\sim U(a,b)$: $E[X]=(a+b)/2$, $\operatorname{Var}(X)=(b-a)^2/12$.

<!-- Added from PDF: Corollary 7.30, page 67 -->
__Bienaymé formula.__ For square-integrable random variables $X_1,\dots,X_n$, $$\operatorname{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \operatorname{Var}(X_i) + \sum_{i \neq j} \operatorname{Cov}(X_i, X_j),$$ where the double sum runs over all ordered pairs with $i \neq j$.

When the variables are independent, all covariance terms vanish and the formula reduces to $\operatorname{Var}(\sum_{i=1}^n X_i) = \sum_{i=1}^n \operatorname{Var}(X_i)$. The $n=2$ case gives the familiar identity $\operatorname{Var}(X+Y) = \operatorname{Var}X + \operatorname{Var}Y + 2\operatorname{Cov}(X,Y)$.

---

Flashcards for this section are as follows:

- variance and standard deviation: For a square-integrable random variable $X$, what are $\operatorname{Var}(X)$ and $\operatorname{sd}(X)$? ::@:: $\operatorname{Var}(X)=E[(X-E[X])^2]$ and $\operatorname{sd}(X)=\sqrt{\operatorname{Var}(X)}$; both depend only on the law of $X$ and $\operatorname{sd}$ has the same units as $X$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- computational variance identity: How do you rewrite $\operatorname{Var}(X)$ using $E[X^2]$ and $E[X]$? ::@:: $\operatorname{Var}(X)=E[X^2]-(E[X])^2$, obtained by expanding $(X-E[X])^2$ and using linearity of expectation. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- affine change of variance: What is $\operatorname{Var}(aX+b)$? ::@:: $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$; additive constants cancel because variance measures spread around the mean. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- variance identity proof: Derive $\operatorname{Var}(X)=E[X^2]-(E[X])^2$. ::@:: Expand: $E[(X-E[X])^2]=E[X^2-2XE[X]+E[X]^2]=E[X^2]-2E[X]^2+E[X]^2=E[X^2]-(E[X])^2$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- variance nonnegativity: Why is $\operatorname{Var}(X)\ge0$, and when does equality hold? ::@:: $\operatorname{Var}(X)=E[(X-E[X])^2]\ge0$ because it is an expectation of a nonnegative random variable. Equality iff $(X-E[X])^2=0$ a.s., i.e., $X=E[X]$ a.s. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Bernoulli variance: If $X\sim\mathrm{Ber}(p)$, what are $E[X]$ and $\operatorname{Var}(X)$? ::@:: $E[X]=p$, $\operatorname{Var}(X)=p(1-p)$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- binomial variance: If $X\sim\mathrm{Bin}(n,p)$, what are $E[X]$ and $\operatorname{Var}(X)$? ::@:: $E[X]=np$, $\operatorname{Var}(X)=np(1-p)$ (sum of $n$ independent Bernoulli variables; by Bienaymé, variances add when covariance vanishes). <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Poisson variance: If $X\sim\mathrm{Pois}(\lambda)$, what are $E[X]$ and $\operatorname{Var}(X)$? ::@:: $E[X]=\lambda$, $\operatorname{Var}(X)=\lambda$ (the Poisson is equidispersed). <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- normal variance: If $X\sim N(\mu,\sigma^2)$, what are $E[X]$ and $\operatorname{Var}(X)$? ::@:: $E[X]=\mu$, $\operatorname{Var}(X)=\sigma^2$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- geometric variance: If $X\sim\mathrm{Geo}(p)$, what are $E[X]$ and $\operatorname{Var}(X)$? ::@:: $E[X]=1/p$, $\operatorname{Var}(X)=(1-p)/p^2$; derived from $E[X^2]=(2-p)/p^2$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- exponential variance: If $X\sim\mathrm{Exp}(\lambda)$, what are $E[X]$ and $\operatorname{Var}(X)$? ::@:: $E[X]=1/\lambda$, $\operatorname{Var}(X)=1/\lambda^2$; derived from $E[X^2]=2/\lambda^2$ and the tail integral for $E[X]$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- uniform variance: If $X\sim U(a,b)$, what are $E[X]$ and $\operatorname{Var}(X)$? ::@:: $E[X]=(a+b)/2$, $\operatorname{Var}(X)=(b-a)^2/12$; derived from $E[X^2]=(a^2+ab+b^2)/3$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Bienaymé formula / variance of a sum ::@:: $\operatorname{Var}(\sum_{i=1}^n X_i)=\sum_i\operatorname{Var}(X_i)+\sum_{i\neq j}\operatorname{Cov}(X_i,X_j)$. For independent variables, covariance terms vanish: $\operatorname{Var}(\sum X_i)=\sum\operatorname{Var}(X_i)$. The $n=2$ case: $\operatorname{Var}(X+Y)=\operatorname{Var}X+\operatorname{Var}Y+2\operatorname{Cov}(X,Y)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->

## covariance and correlation

For square-integrable $X$ and $Y$, define $\operatorname{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])] = E[XY]-E[X]E[Y]$. Covariance is symmetric and bilinear: $\operatorname{Cov}(aX+b,cY+d)=ac\,\operatorname{Cov}(X,Y)$.

If $X$ and $Y$ are independent, then $E[XY]=E[X]E[Y]$, so $\operatorname{Cov}(X,Y)=0$. The converse fails in general; zero covariance only kills the first nontrivial mixed centered moment.

If $\operatorname{Var}(X),\operatorname{Var}(Y)>0$, the correlation coefficient is $\rho(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}}$.

By the Cauchy-Schwarz inequality one always has $|\rho(X,Y)|\le 1$. Equality holds precisely when the centered variables are linearly dependent almost surely.

As a concrete example, if $X\sim U([0,a])$, then $\operatorname{Cov}(X,X^2)=E[X^3]-E[X]E[X^2]=a^3/12$, and a short computation gives $\rho(X,X^2)=\sqrt{15}/4$.

---

Flashcards for this section are as follows:

- covariance definition: For square-integrable $X$ and $Y$, how is $\operatorname{Cov}(X,Y)$ defined? ::@:: $\operatorname{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])]=E[XY]-E[X]E[Y]$; the second form follows by expanding the product and using linearity. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- covariance under affine changes: What is $\operatorname{Cov}(aX+b,cY+d)$? ::@:: $\operatorname{Cov}(aX+b,cY+d)=ac\,\operatorname{Cov}(X,Y)$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- independence and covariance: If $X$ and $Y$ are independent, what can you conclude about $\operatorname{Cov}(X,Y)$? ::@:: $\operatorname{Cov}(X,Y)=0$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- correlation coefficient: If $\operatorname{Var}(X),\operatorname{Var}(Y)>0$, what is $\rho(X,Y)$? ::@:: $\rho(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}}$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- covariance symmetry: What property of $\operatorname{Cov}(X,Y)$ follows directly from its definition? ::@:: Symmetry: $\operatorname{Cov}(X,Y)=\operatorname{Cov}(Y,X)$, because $(X-E[X])(Y-E[Y])$ is symmetric. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- zero covariance vs independence: Does $\operatorname{Cov}(X,Y)=0$ imply $X$ and $Y$ are independent? ::@:: No; zero covariance only removes the first nontrivial mixed centered moment. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- correlation magnitude bound: What is the range of $\rho(X,Y)$, and why? ::@:: $-1\le\rho(X,Y)\le1$, by Cauchy-Schwarz: $|\operatorname{Cov}(X,Y)|\le\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- correlation equality condition: When does $|\rho(X,Y)|=1$ hold? ::@:: When the centered variables are linearly dependent a.s.: $Y-E[Y]=c(X-E[X])$ for some $c\in\mathbb R\setminus\{0\}$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- covariance example $U([0,a])$: Derive $\operatorname{Cov}(X,X^2)$ and $\rho(X,X^2)$ for $X\sim U([0,a])$. ::@:: $\operatorname{Cov}=E[X^3]-E[X]E[X^2]=a^3/4-(a/2)(a^2/3)=a^3/12$; $\rho=(a^3/12)/\sqrt{(a^2/12)(4a^4/45)}=\sqrt{15}/4$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->

## inequalities

The first universal tail estimate is Markov's inequality.

__Theorem (Markov).__ If $Y\ge 0$ and $c>0$, then $P[Y\ge c]\le E[Y]/c$.

__Proof.__ Since $Y\ge c\mathbf 1_{\{Y\ge c\}}$, taking expectation yields $E[Y]\ge cP[Y\ge c]$.

__Intuition.__ Markov is the foundational engine — every tail bound in this section derives from it. Because it only requires nonnegativity and the first moment, it is the crudest bound but also the most widely applicable.

A direct consequence is Chebyshev's inequality.

__Theorem (Chebyshev).__ For $a>0$, $P(|X-E[X]|\ge a)\le \operatorname{Var}(X)/a^2$.

__Proof.__ Apply Markov to the nonnegative variable $(X-E[X])^2$ with threshold $a^2$.

__Intuition.__ Chebyshev trades variance for a symmetric two-sided tail bound. The bound $1/k^2$ on the $k\sigma$ tail is universal — it holds for any distribution with finite variance — but course Remark 6.16 notes it is often extremely crude compared to the true tail (e.g., for a normal distribution Chebyshev gives $P(|Z|\ge 5)\le 1/25$, while the true probability is about $6\times10^{-7}$).

Applying Markov to $e^{tX}$ instead yields Chernoff-type bounds, which later combine naturally with generating functions.

A one-sided refinement of Chebyshev is Cantelli's inequality.

__Theorem (Cantelli).__ For $a>0$, $P(X-E[X]\ge a)\le \dfrac{\operatorname{Var}(X)}{\operatorname{Var}(X)+a^2}$.

__Proof.__ Let $Y=X-E[X]$ (so $E[Y]=0$) and fix any $t\ge0$. Then $P(Y\ge a)=P(Y+t\ge a+t)\le P((Y+t)^2\ge(a+t)^2)\le E[(Y+t)^2]/(a+t)^2$, where the last step is Markov applied to $(Y+t)^2\ge0$. Expanding the numerator gives $E[(Y+t)^2]=\operatorname{Var}(X)+t^2$ (since $E[Y]=0$). Hence $P(Y\ge a)\le(\operatorname{Var}(X)+t^2)/(a+t)^2$ for every $t\ge0$.

Minimising the right side over $t\ge0$ (set derivative to zero) gives $t=\operatorname{Var}(X)/a$, and substituting back yields the stated bound $\operatorname{Var}(X)/(\operatorname{Var}(X)+a^2)$.

__Intuition.__ Chebyshev bounds the two-sided tail $P(|Y|\ge a)$; if the distribution is asymmetric the upper tail may deserve a tighter estimate. Cantelli introduces a free parameter $t\ge0$ that shifts the variable, optimising the Markov step and improving the denominator from $a^2$ to $\operatorname{Var}+a^2$. The bound is tight: equality holds for two-point distributions supported on $\{-\sigma^2/a,\,a\}$, where $\sigma^2=\operatorname{Var}(X)$ and $P(X=a)=\sigma^2/(\sigma^2+a^2)$, $P(X=-\sigma^2/a)=a^2/(\sigma^2+a^2)$. (Then $E[X]=0$, $\operatorname{Var}(X)=\sigma^2$, and $P(X\ge a)=\sigma^2/(\sigma^2+a^2)$, matching the Cantelli bound.)

Convexity produces a second family of structural inequalities.

__Theorem (Jensen).__ If $\varphi$ is convex and $X$ is integrable, then $\varphi(E[X])\le E[\varphi(X)]$.

__Proof.__ Every convex function admits a supporting line at each interior point: for $m=E[X]$ there exists $\alpha$ such that $\varphi(x)\ge\varphi(m)+\alpha(x-m)$ for all $x$. Substitute $x=X$ and take expectations.

__Intuition.__ The line through $(m,\varphi(m))$ stays below the graph of $\varphi$; replacing the random input $X$ by its mean $m$ can only decrease the average value of $\varphi$. For concave $\varphi$ the inequality reverses, as with $\log$ in Jensen's inequality for entropy.

__Theorem (Hölder).__ If $p,q>1$ satisfy $1/p+1/q=1$, then $E[|XY|]\le(E[|X|^p])^{1/p}(E[|Y|^q])^{1/q}$.

__Intuition.__ The idea is to normalize $X$ and $Y$ by their $L^p$ and $L^q$ norms so that the scaled variables have unit $p$-th and $q$-th moments: $E[|a|^p]=E[|b|^q]=1$. Then Young's inequality $ab\le a^p/p+b^q/q$ becomes, after taking expectation, $E[ab]\le1/p+1/q=1$, which directly gives the Hölder bound. The normalization is the key trick that aligns the probabilistic expectations with the unit condition in Young's inequality.

__Proof.__ Young's inequality $ab\le a^p/p+b^q/q$ for $a,b\ge0$ is the key. Set $a=|X|/\|X\|_p$ and $b=|Y|/\|Y\|_q$ where $\|X\|_p=(E[|X|^p])^{1/p}$. Then $|XY|/(\|X\|_p\|Y\|_q)\le |X|^p/(p\|X\|_p^p)+|Y|^q/(q\|Y\|_q^q)$. Take expectations; the right side becomes $1/p+1/q=1$, giving $E[|XY|]\le\|X\|_p\|Y\|_q$.

The special case $p=q=2$ is the Cauchy-Schwarz inequality: $|E[XY]|\le\sqrt{E[X^2]E[Y^2]}$.

__Alternative proof (Cauchy-Schwarz).__ Consider $0\le E[(X-\lambda Y)^2]=E[X^2]-2\lambda E[XY]+\lambda^2E[Y^2]$ as a quadratic in $\lambda$. The discriminant must be nonpositive: $(2E[XY])^2-4E[X^2]E[Y^2]\le0$, hence $|E[XY]|\le\sqrt{E[X^2]E[Y^2]}$.

__Intuition for Hölder/CS.__ These inequalities control product moments via $L^p$ and $L^2$ norms. They are the probabilistic analogue of $|\langle u,v\rangle|\le\|u\|\|v\|$ in inner product spaces. Hölder is needed because $E[X]$ and $E[Y]$ finite alone does __not__ guarantee $E[XY]$ finite (e.g. $X=Y$ with $P[X=n]=1/(c_3n^3)$, $c_3=\sum n^{-3}$, satisfies $E[X]<\infty$ but $E[X^2]=\infty$).

---

Flashcards for this section are as follows:

- Markov inequality: If $Y\ge 0$ and $c>0$, what bound does Markov give for $P[Y\ge c]$? ::@:: $P[Y\ge c]\le E[Y]/c$; follows from $Y\ge c\mathbf 1_{\{Y\ge c\}}$ pointwise and taking expectations. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Chebyshev inequality: For $a>0$, how do you bound $P(|X-E[X]|\ge a)$? ::@:: $P(|X-E[X]|\ge a)\le \operatorname{Var}(X)/a^2$, obtained by applying Markov to $(X-E[X])^2$ (nonnegative). <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Cantelli inequality: For $a>0$, how do you bound the one-sided tail $P(X-E[X]\ge a)$? ::@:: $P(X-E[X]\ge a)\le \operatorname{Var}(X)/(\operatorname{Var}(X)+a^2)$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Jensen inequality: If $\varphi$ is convex and $X$ is integrable, what inequality holds? ::@:: $\varphi(E[X])\le E[\varphi(X)]$; the reverse inequality holds when $\varphi$ is concave. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Hölder inequality: If $1/p+1/q=1$ with $p,q>1$, what bound holds for $E[|XY|]$? ::@:: $E[|XY|]\le (E[|X|^p])^{1/p}(E[|Y|^q])^{1/q}$; the $p=q=2$ case is Cauchy-Schwarz. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Cauchy-Schwarz inequality: What is the $p=q=2$ case of Hölder's inequality? ::@:: $|E[XY]|\le \sqrt{E[X^2]E[Y^2]}$, equivalently $|\langle X,Y\rangle|\le\|X\|_2\|Y\|_2$ in the $L^2$ inner product. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Markov inequality proof: Prove $P[Y\ge c]\le E[Y]/c$ for $Y\ge0$, $c>0$. ::@:: $Y\ge c\mathbf 1_{\{Y\ge c\}}$ pointwise; take expectations: $E[Y]\ge cP[Y\ge c]$, then divide by $c>0$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Chebyshev from Markov: Derive $P(|X-E[X]|\ge a)\le\operatorname{Var}(X)/a^2$ from Markov's inequality. ::@:: Apply Markov to the nonnegative variable $Y=(X-E[X])^2$ with $c=a^2$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Cantelli derivation: Derive $P(X-E[X]\ge a)\le\operatorname{Var}(X)/(\operatorname{Var}(X)+a^2)$. ::@:: Let $Y=X-E[X]$. For $t\ge0$, apply Markov to $(Y+t)^2$: $P(Y\ge a)\le\frac{\operatorname{Var}+t^2}{(a+t)^2}$. Minimise over $t\ge0$ to get $t=\operatorname{Var}/a$; substitute back. <!--SR:!fsrs,2026-07-13T00:10:00.000Z,0,2.3065,2.11810397,1,1,0,1,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Cantelli intuition: Why is Cantelli a refinement of Chebyshev, and when is it tight? ::@:: Cantelli optimises Chebyshev for the one-sided tail by introducing a shift parameter $t$, giving $\operatorname{Var}/(\operatorname{Var}+a^2)$ vs Chebyshev's $\operatorname{Var}/a^2$. Tight for two-point distributions supported on $\{-\sigma^2/a,a\}$ with $P(X=a)=\sigma^2/(\sigma^2+a^2)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Jensen inequality proof technique: How does the supporting-line argument prove $\varphi(E[X])\le E[\varphi(X)]$? ::@:: At $m=E[X]$, convex $\varphi$ satisfies $\varphi(x)\ge\varphi(m)+\alpha(x-m)$ for some $\alpha$. Substitute $X$ and take expectations. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Hölder inequality proof: How does Young's inequality prove $E[|XY|]\le\|X\|_p\|Y\|_q$ (where $\|X\|_p=(E[|X|^p])^{1/p}$, $1/p+1/q=1$)? ::@:: Young: $ab\le a^p/p+b^q/q$ for $a,b\ge0$. Normalise so $E[a^p]=E[b^q]=1$: $a=|X|/\|X\|_p$, $b=|Y|/\|Y\|_q$. Young gives $\frac{|XY|}{\|X\|_p\|Y\|_q}\le\frac{|X|^p}{p\|X\|_p^p}+\frac{|Y|^q}{q\|Y\|_q^q}$. Take expectations: $\frac{E[|XY|]}{\|X\|_p\|Y\|_q}\le\frac{E[|X|^p]}{p\|X\|_p^p}+\frac{E[|Y|^q]}{q\|Y\|_q^q}=\frac{\|X\|_p^p}{p\|X\|_p^p}+\frac{\|Y\|_q^q}{q\|Y\|_q^q}=1/p+1/q=1$. Hence $E[|XY|]\le\|X\|_p\|Y\|_q$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Cauchy-Schwarz discriminant proof: How does the quadratic discriminant argument prove $|E[XY]|\le\sqrt{E[X^2]E[Y^2]}$? ::@:: Consider $0\le E[(X-\lambda Y)^2]=E[X^2]-2\lambda E[XY]+\lambda^2E[Y^2]$. The discriminant $(2E[XY])^2-4E[X^2]E[Y^2]$ must be $\le0$, giving the bound. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->

---

### relations between the inequalities

The six inequalities above are not isolated facts. They form a natural hierarchy.

- __Markov is the engine.__ Every tail bound — Chebyshev, Cantelli, Chernoff — begins by applying Markov to a transformed variable $(X-E[X])^2$, $(Y+t)^2$, or $e^{tX}$. The trade-off is moment information versus tail sharpness.

- __Chebyshev specialises Markov to variance.__ Squaring converts second-moment information into a two-sided tail bound. The bound is symmetric: upper and lower tails get the same estimate.

- __Cantelli refines Chebyshev for one-sided tails.__ An optimisation parameter $t$ improves $\operatorname{Var}/a^2$ to $\operatorname{Var}/(\operatorname{Var}+a^2)$. The improvement is largest when $\operatorname{Var}\ll a^2$.

- __Chernoff refines Markov through the MGF.__ Exponentiation turns Markov into $P[X\ge a]\le e^{-ta}M_X(t)$. Optimising over $t>0$ gives exponentially decaying bounds — far sharper than Chebyshev — at the cost of requiring the moment generating function.

- __Jensen is orthogonal.__ Tail bounds control large-deviation probabilities; Jensen controls how convex functions interact with expectation. They answer different questions and are used in different settings.

- __Hölder/CS control product moments__, not tail probabilities. They are the $L^p$ analogues of the geometric bound $|\langle u,v\rangle|\le\|u\|\|v\|$, used to decouple dependent variables in moment estimates.

---

Flashcards for this section are as follows:

- Markov as engine: Why is Markov called the engine of tail bounds? ::@:: Every tail bound — Chebyshev, Cantelli, Chernoff — begins by applying Markov to a transformed variable $(X-E[X])^2$, $(Y+t)^2$, or $e^{tX}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Chebyshev vs Markov: How does Chebyshev specialise Markov? ::@:: Chebyshev applies Markov to $(X-E[X])^2$, converting second-moment information into a two-sided symmetric tail bound $P(|X-E[X]|\ge a)\le\operatorname{Var}(X)/a^2$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Cantelli vs Chebyshev: How does Cantelli improve Chebyshev for one-sided tails? ::@:: Cantelli introduces an optimisation parameter $t$, improving $\operatorname{Var}/a^2$ to $\operatorname{Var}/(\operatorname{Var}+a^2)$; the improvement is largest when $\operatorname{Var}\ll a^2$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Chernoff vs Markov: How does Chernoff refine Markov to get sharper bounds? ::@:: Chernoff applies Markov to $e^{tX}$: $P[X\ge a]\le e^{-ta}M_X(t)$, then optimises over $t>0$ for exponentially decaying bounds at the cost of requiring the MGF. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Jensen vs tail bounds: How do Jensen and tail bounds differ? ::@:: Tail bounds control large-deviation probabilities; Jensen controls how convex/concave functions interact with expectation — they answer different questions. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Hölder/CS purpose: What do Hölder/CS inequalities control? ::@:: Product moments via $L^p$ and $L^2$ norms — the $L^p$ analogues of $|\langle u,v\rangle|\le\|u\|\|v\|$ in inner product spaces, used to decouple dependent variables. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->

### moment comparison

A useful consequence of the inequalities above is that $L^p$ norms increase with $p$: for $0<r<s$, one has $\|X\|_r\le\|X\|_s$, i.e. $(E[|X|^r])^{1/r}\le(E[|X|^s])^{1/s}$. This can be proved in two ways.

__Proof via Hölder.__ Apply Hölder's inequality to $|X|^r\cdot1$ with $p=s/r>1$ and $q=p/(p-1)=s/(s-r)$ (so $1/p+1/q=r/s+(s-r)/s=1$). Then $$E[|X|^r]\le(E[(|X|^r)^{s/r}])^{r/s}(E[1^{s/(s-r)}])^{(s-r)/s}=(E[|X|^s])^{r/s}.$$ Taking $r$-th roots gives $(E[|X|^r])^{1/r}\le(E[|X|^s])^{1/s}$.

__Proof via Jensen.__ Since $s/r>1$, the function $\varphi(x)=|x|^{s/r}$ is convex on $\mathbb R$. By Jensen's inequality, $$\varphi(E[|X|^r])\le E[\varphi(|X|^r)],\quad\text{i.e.}\quad(E[|X|^r])^{s/r}\le E[|X|^s].$$ Raising both sides to $1/s$ gives $(E[|X|^r])^{1/r}\le(E[|X|^s])^{1/s}$.

---

Flashcards for this section are as follows:

- Markov is the engine: How do Chebyshev, Cantelli, and Chernoff relate to Markov? ::@:: Each applies Markov to a transformed variable: $(X-E[X])^2$ for Chebyshev, $(Y+t)^2$ for Cantelli, $e^{tX}$ for Chernoff. Markov is the single source of all these tail bounds. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Chebyshev vs Cantelli: How do Chebyshev and Cantelli differ? ::@:: Chebyshev gives $P(|Y|\ge a)\le\operatorname{Var}/a^2$ (two-sided, symmetric). Cantelli improves the one-sided bound to $\operatorname{Var}/(\operatorname{Var}+a^2)$ via an optimisation parameter $t$, always tighter for the same tail. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Jensen vs tail bounds: How is Jensen different from Markov-type inequalities? ::@:: Tail bounds (Markov, Chebyshev, Cantelli, Chernoff) control probabilities of large deviations. Jensen controls how convex functions interact with expectations. They are orthogonal tools for different tasks. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- moment comparison via Hölder: How does Hölder's inequality show $(E[|X|^r])^{1/r}\le(E[|X|^s])^{1/s}$ for $0<r<s$? ::@:: Apply Hölder to $|X|^r\cdot1$ with $p=s/r$, $q=s/(s-r)$: $E[|X|^r]\le(E[|X|^s])^{r/s}$; take $r$-th roots. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- moment comparison via Jensen: How does Jensen's inequality show $(E[|X|^r])^{1/r}\le(E[|X|^s])^{1/s}$ for $0<r<s$? ::@:: $\varphi(x)=|x|^{s/r}$ is convex, so by Jensen $(E[|X|^r])^{s/r}\le E[|X|^s]$; raise to $1/s$. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
- Chernoff-type bounds: Derive $P[X\ge a]\le e^{-ta}E[e^{tX}]$ for $t>0$ from Markov's inequality, and how is it optimised? ::@:: Apply Markov to $Y=e^{tX}$ (nonnegative for $t>0$): $P[e^{tX}\ge e^{ta}]\le e^{-ta}E[e^{tX}]$, which gives $P[X\ge a]\le e^{-ta}M_X(t)$. Optimising over $t>0$ gives the sharpest bound, connecting to moment generating functions. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
