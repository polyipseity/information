---
aliases:
  - central limit theorem
  - convergence and limit theorems
  - convergence of random variables
  - laws of large numbers
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/convergence_and_limit_theorems
  - language/in/English
---

# convergence and limit theorems

The final part of the course studies how sequences of random variables behave asymptotically. Different modes of convergence capture different strengths of control, and the main theorems explain why repeated randomness becomes stable on large scales.

---

Flashcards for this section are as follows:

- overview ::@:: Limit theorems describe the asymptotic behavior of sequences of random variables and explain why averages and normalized sums become predictable.

## convergence in probability

One says that $X_n\to X$ in probability if for every $\varepsilon>0$, one has $P(|X_n-X|>\varepsilon)\to 0$.

This is the natural notion for statements such as "the sample mean is close to the true mean with high probability for large $n$."

Convergence in probability is stable under continuous transformations and algebraic operations. If $X_n\to X$ and $Y_n\to Y$ in probability, then

- $X_n+Y_n\xrightarrow{p}X+Y$, $X_n-Y_n\xrightarrow{p}X-Y$, $X_nY_n\xrightarrow{p}XY$, and $X_n/Y_n\xrightarrow{p}X/Y$ (provided $P(Y=0)=0$);
- for any $c\in\mathbb R$, $cX_n\xrightarrow{p}cX$;
- $(X_n,Y_n)\xrightarrow{p}(X,Y)$ without requiring independence;
- $|X_n|\xrightarrow{p}|X|$, $\max(X_n,Y_n)\xrightarrow{p}\max(X,Y)$, $\min(X_n,Y_n)\xrightarrow{p}\min(X,Y)$.

The key contrast with convergence in distribution is that no constant limit is needed here—convergence in probability preserves all operations even when both limits are non-degenerate random variables, unlike Slutsky's theorem.

---

Flashcards for this section are as follows:

- convergence in probability / definition ::@:: $X_n\to X$ in probability means $P(|X_n-X|>\varepsilon)\to0$ for every $\varepsilon>0$. The defect set $A_n^X(\varepsilon)=\{\omega:|X_n(\omega)-X(\omega)|>\varepsilon\}$ captures where the approximation fails. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- continuous mapping for convergence in probability ::@:: If $g$ is continuous and $X_n\xrightarrow{p}X$, then $g(X_n)\xrightarrow{p}g(X)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- algebra of convergence in probability ::@:: If $X_n\to X$, $Y_n\to Y$ in probability, then $X_n\pm Y_n$, $X_nY_n$, $X_n/Y_n$ (when $P(Y=0)=0$), $(X_n,Y_n)$, and $\max/\min/|\cdot|$ all converge accordingly. No constant limit is needed, unlike Slutsky's theorem for convergence in distribution. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## convergence in p-th mean

One says that $Z_n\to Z$ in $p$-th mean (for $p\ge1$) if $E[|Z_n|^p]<\infty$ and $E[|Z|^p]<\infty$, and $E[|Z_n-Z|^p]\to0$.

This is convergence in the $L^p$ vector-space norm $\|Z_n-Z\|_p=(E[|Z_n-Z|^p])^{1/p}$. Larger $p$ penalizes tail and outlier deviations more heavily.

__$p$-th mean $\Rightarrow$ convergence in probability.__ By Markov's inequality, $$P(|Z_n-Z|>\varepsilon)=P(|Z_n-Z|^p>\varepsilon^p)\le\frac{E[|Z_n-Z|^p]}{\varepsilon^p}\to0.$$

The weak law of large numbers below is actually proved first in $L^2$ (mean-square convergence), and the convergence-in-probability conclusion follows from the case $p=2$.

By Lyapunov's inequality (a consequence of Jensen), $\|X\|_q\le\|X\|_p$ for $1\le q\le p$, so $L^p$ convergence implies $L^q$ convergence. $L^p$ convergence does __not__ imply almost-sure convergence (the typewriter sequence is a counterexample), but every $L^p$-convergent sequence has an almost-surely convergent subsequence. If $X_n\to X$ in $L^p$, then $E[|X_n|^p]\to E[|X|^p]$.

---

Flashcards for this section are as follows:

- convergence in $p$-th mean / definition ::@:: For $p\ge1$, $E[|Z_n|^p],E[|Z|^p]<\infty$ and $E[|Z_n-Z|^p]\to0$.
- $p$-th mean implies convergence in probability ::@:: $P(|Z_n-Z|>\varepsilon)\le E[|Z_n-Z|^p]/\varepsilon^p\to0$ by Markov's inequality.
- Lyapunov inequality / monotonicity ::@:: For $1\le q\le p$, $\|X\|_q\le\|X\|_p$ by Jensen, so $L^p$ convergence implies $L^q$ convergence. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- $L^p$ convergence: implications for almost-sure convergence ::@:: $L^p$ convergence does __not__ imply almost-sure convergence (counterexample: typewriter sequence). However: (1) every $L^p$-convergent sequence has an almost-surely convergent subsequence; (2) $X_n\xrightarrow{L^p} X$ implies $E[|X_n|^p]\to E[|X|^p]$.

## convergence in distribution

One says that $X_n\xrightarrow{d} X$ in distribution if $F_{X_n}(x)\to F_X(x)$ at every continuity point $x$ of $F_X$.

This is weaker than convergence in probability: it describes only the asymptotic law, not a coupling on the same sample space. The standard implication is that $X_n\to X$ in probability implies $X_n\xrightarrow{d} X$.

Convergence in distribution cares about the asymptotic __shape__ of the law, not pointwise behavior. Portmanteau's theorem collects several equivalent characterizations:

- $E[f(X_n)]\to E[f(X)]$ for all bounded continuous $f$ — integration smooths fluctuations.
- $\limsup_{n\to\infty} P(X_n\in F)\le P(X\in F)$ for every closed set $F$.
- $\liminf_{n\to\infty} P(X_n\in G)\ge P(X\in G)$ for every open set $G$.
- $P(X_n\in B)\to P(X\in B)$ for every continuity set $B$ (i.e., $P(X\in\partial B)=0$).

The closed-set formulation is especially useful for tightness arguments: if mass escapes to infinity in the limit (a closed set is lost), the limit law cannot assign that mass. Convergence must be required at __continuity points__ of $F_X$ to avoid point-mass slipping past a discontinuity (e.g. $X_n=1/n$ vs $X=0$ fails at $x=0$ but holds elsewhere).

__Vanishing perturbation.__ If $Y_n\xrightarrow{d} X$ and $X_n-Y_n\to0$ in probability, then $X_n\xrightarrow{d} X$. Proof: $F_{X_n}(x)\le F_{Y_n}(x+\varepsilon)+P(|X_n-Y_n|\ge\varepsilon)$; $\limsup/\liminf$ sandwich gives $F_{X_n}(x)\to F_X(x)$.

__Proof that $X_n\to X$ in probability $\Rightarrow$ $X_n\xrightarrow{d} X$.__ Split $\{X_n\le x\}$ into cases where $|X_n-X|\le\varepsilon$ and $>\varepsilon$, giving $F_{X_n}(x)\le F_X(x+\varepsilon)+P(|X_n-X|>\varepsilon)$. Symmetrically $F_X(x-\varepsilon)\le F_{X_n}(x)+P(|X_n-X|>\varepsilon)$. Let $n\to\infty$ then $\varepsilon\downarrow0$; at continuity points of $F_X$ the bounds squeeze to $F_X(x)$.

__Smoothing effect.__ The CDF is an integral/sum of the PDF/PMF, acting as a low-pass filter. Convergence in distribution is strictly weaker than density convergence:

- __Oscillating PDF:__ $f_n(x)=1+\sin(2\pi n x)$ on $[0,1]$: $F_n(x)\to x$ uniformly, so $X_n\xrightarrow{d}\operatorname{Uniform}(0,1)$ despite $f_n\not\to 1$.
- __Discrete-to-continuous:__ $X_n$ uniform on $\{k/n\}_{k=0}^n$: $F_{X_n}(x)\to x$, so $X_n\xrightarrow{d}\operatorname{Uniform}(0,1)$ despite discrete support.

__Lévy's continuity theorem.__ $X_n\xrightarrow{d} X$ iff their characteristic functions $\phi_n(t)=E[e^{itX_n}]$ converge pointwise to $\phi(t)=E[e^{itX}]$ for all $t\in\mathbb R$.

_Proof sketch (forward direction)._ If $X_n\xrightarrow{d} X$, the function $x\mapsto e^{itx}$ is bounded and continuous for each fixed $t$, so by Portmanteau $E[e^{itX_n}]\to E[e^{itX}]$. This direction is immediate.

_Proof sketch (reverse direction)._ Assume $\phi_n(t)\to\phi(t)$ pointwise and $\phi$ is continuous at $0$. Clearly $\phi(0)=\lim_n\phi_n(0)=1$.

__Tail inequality for CFs.__ By Fubini's theorem, $$\frac1\delta\int_{-\delta}^\delta(1-\phi_n(t))\,dt = E\!\left[\,\frac1\delta\int_{-\delta}^\delta(1-e^{itX_n})\,dt\right] = E\!\left[2-\frac{2\sin(\delta X_n)}{\delta X_n}\right].$$ The function $h(y)=2-2\sin y/y$ satisfies $h(y)\ge1$ for $|y|\ge2$ (since $|\sin y|\le1$ gives $h(y)\ge2-2/|y|\ge1$) and $h(y)\ge0$ elsewhere. Consequently $$P(|X_n|>2/\delta)\le E\!\left[2-\frac{2\sin(\delta X_n)}{\delta X_n}\right] = \frac1\delta\int_{-\delta}^\delta(1-\phi_n(t))\,dt.$$

__Tightness via dominated convergence.__ Continuity of $\phi$ at $0$ gives: for any $\varepsilon>0$, choose $\delta>0$ such that $|1-\phi(t)|<\varepsilon$ for $|t|<\delta$. Then $$\frac1\delta\int_{-\delta}^\delta(1-\phi(t))\,dt \le \frac1\delta\int_{-\delta}^\delta|1-\phi(t)|\,dt < \frac1\delta\cdot2\delta\cdot\varepsilon = 2\varepsilon,$$ where the first inequality holds because the integral is real (the imaginary part cancels by symmetry $\phi(-t)=\overline{\phi(t)}$). For each $n$, $|1-\phi_n(t)|\le2$ (because $|\phi_n(t)|\le1$) and $1-\phi_n(t)\to1-\phi(t)$ pointwise. On $[-\delta,\delta]$, the dominated convergence theorem therefore applies: $$\lim_{n\to\infty}\frac1\delta\int_{-\delta}^\delta(1-\phi_n(t))\,dt = \frac1\delta\int_{-\delta}^\delta(1-\phi(t))\,dt < 2\varepsilon.$$ Combining with the tail inequality gives $\limsup_n P(|X_n|>2/\delta)<2\varepsilon$. Since $\varepsilon$ is arbitrary, $\{X_n\}$ is tight.

__Subsequence convergence and identification.__ By Prokhorov's theorem, tightness implies relative compactness: every subsequence of $\{X_n\}$ contains a further subsequence $\{X_{n_k}\}$ converging in distribution to some $Q$. The forward direction of Lévy's theorem identifies the CF of $Q$ as $\phi_Q(t)=\lim_k\phi_{n_k}(t)=\phi(t)$. Characteristic functions uniquely determine the law, so every subsequential limit must be the same distribution $P$ (the distribution whose CF is $\phi$). Hence $X_n\xrightarrow{d} P$.

---

Flashcards for this section are as follows:

- convergence in distribution / definition ::@:: $X_n\xrightarrow{d} X$ means $F_{X_n}(x)\to F_X(x)$ at every continuity point of $F_X$. Equivalently (Portmanteau): $E[f(X_n)]\to E[f(X)]$ for bounded continuous $f$, or $\limsup P(X_n\in F)\le P(X\in F)$ for closed $F$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- vanishing perturbation ::@:: If $Y_n\xrightarrow{d} X$ and $X_n-Y_n\to0$ in probability, then $X_n\xrightarrow{d} X$. Proof: sandwich $F_{X_n}(x)$ via $F_{Y_n}(x\pm\varepsilon)$ and $P(|X_n-Y_n|\ge\varepsilon)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- smoothing effect of CDF integration ::@:: The CDF integrates the PDF/PMF, acting as a low-pass filter. Convergence in distribution is strictly weaker: $f_n(x)=1+\sin(2\pi n x)$ oscillates but $F_n\to x$ uniformly, and discrete uniforms on $\{k/n\}$ converge to $\operatorname{Uniform}(0,1)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- proof that convergence in probability implies convergence in distribution ::@:: Sandwich: $F_{X_n}(x)\le F_X(x+\varepsilon)+P(|X_n-X|>\varepsilon)$ and $F_X(x-\varepsilon)\le F_{X_n}(x)+P(|X_n-X|>\varepsilon)$; let $n\to\infty$ then $\varepsilon\downarrow0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Portmanteau theorem: four equivalent formulations ::@:: (1) $E[f(X_n)]\to E[f(X)]$ for bounded continuous $f$; (2) $\limsup P(X_n\in F)\le P(X\in F)$ for closed $F$; (3) $\liminf P(X_n\in G)\ge P(X\in G)$ for open $G$; (4) $P(X_n\in B)\to P(X\in B)$ for continuity sets $B$. (2) and (3) are dual via complement. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Lévy's continuity theorem, forward direction ::@:: If $X_n\xrightarrow{d} X$, then $\phi_n(t)\to\phi(t)$ pointwise for all $t\in\mathbb R$. Proof: $e^{itx}$ is bounded and continuous, so Portmanteau gives $\phi_n(t)\to\phi(t)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Lévy's continuity theorem, reverse direction / outline ::@:: If $\phi_n(t)\to\phi(t)$ pointwise for all $t\in\mathbb R$ and $\phi$ is continuous at $0$, then $X_n\xrightarrow{d} X$. The proof proceeds in two phases: first show $\{X_n\}$ is tight (mass does not escape to infinity), then identify every subsequential limit as the same distribution $P$ (the law whose CF is $\phi$). Tightness is proved via a tail bound for CFs combined with dominated convergence; identification uses Prokhorov's theorem, the forward direction, and uniqueness of characteristic functions. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Lévy reverse: tail inequality for CFs ::@:: By Fubini's theorem and Euler's formula, $\frac1\delta\int_{-\delta}^\delta(1-\phi_n(t))\,dt = E[\,\frac1\delta\int_{-\delta}^\delta(1-e^{itX_n})\,dt\,] = E[2-2\sin(\delta X_n)/(\delta X_n)]$. Define $h(y)=2-2\sin y/y$. For $|y|\ge2$, $|\sin y|\le1$ implies $h(y)\ge2-2/|y|\ge1$; $h(y)\ge0$ everywhere. Hence $P(|X_n|>2/\delta)\le E[h(\delta X_n)] = \frac1\delta\int_{-\delta}^\delta(1-\phi_n(t))\,dt$. This bound connects the tail probability of $X_n$ to an average of the CF $\phi_n$ near $0$ — if $\phi_n\approx1$ near $0$, the right side is small and $X_n$ is unlikely to be large. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Lévy reverse: tightness via DCT ::@:: Fix $\varepsilon>0$. Since $\phi$ is continuous at $0$ with $\phi(0)=1$, there exists $\delta>0$ such that $|1-\phi(t)|<\varepsilon$ for $|t|<\delta$. Then $\frac1\delta\int_{-\delta}^\delta(1-\phi(t))\,dt \le \frac1\delta\int_{-\delta}^\delta|1-\phi(t)|\,dt < 2\varepsilon$ (the integral is real because the imaginary part cancels by $\phi(-t)=\overline{\phi(t)}$). For each $n$, $|1-\phi_n(t)|\le2$ (since $|\phi_n|\le1$) and $1-\phi_n(t)\to1-\phi(t)$ pointwise. DCT on $[-\delta,\delta]$ (dominated by the constant $2$) gives $\lim_n\frac1\delta\int_{-\delta}^\delta(1-\phi_n(t))\,dt = \frac1\delta\int_{-\delta}^\delta(1-\phi(t))\,dt < 2\varepsilon$. Combining with the tail inequality, $\limsup_n P(|X_n|>2/\delta) < 2\varepsilon$. Since $\varepsilon$ is arbitrary, $\{X_n\}$ is tight. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Lévy reverse: identification of the limit ::@:: By Prokhorov's theorem, tightness implies relative compactness: every subsequence of $\{X_n\}$ contains a further subsequence $\{X_{n_k}\}$ converging in distribution to some $Q$. The forward direction of Lévy's theorem identifies the CF of $Q$: $\phi_Q(t)=\lim_k\phi_{n_k}(t)=\phi(t)$. Characteristic functions uniquely determine the law, so every subsequential limit must be the same distribution $P$ (the distribution whose CF is $\phi$). Hence the whole sequence converges in distribution to $P$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## relations between convergence modes

The different modes of convergence form a hierarchy. Some modes imply others, and the chain of implications captures how strong a given convergence guarantee is. The relationships taught in this course are:

- Almost-sure convergence implies convergence in probability.
- $p$-th mean convergence (for any $p\ge1$) implies convergence in probability.
- Convergence in probability implies convergence in distribution.

These implications can be summarized as: $$X_n\xrightarrow{\text{a.s.}}X\;\Rightarrow\; X_n\xrightarrow{P}X\;\Rightarrow\; X_n\xrightarrow{d} X,$$

and $X_n\xrightarrow{(p)}X\;\Rightarrow\;X_n\xrightarrow{P}X$, with no other implications in general. Counterexamples exist for each missing implication: the typewriter sequence converges in probability (and in $L^p$) but not almost surely, and oscillating densities converge in distribution but not in probability.

__The typewriter sequence.__ Take $([0,1],\mathcal B,\lambda)$ as the probability space, where $\lambda$ is the Lebesgue measure. Write each $n\ge1$ uniquely as $n=2^k+m$ with $k\ge0$ and $0\le m<2^k$ (so $k=\lfloor\log_2 n\rfloor$), and define $$X_n(\omega)=1_{[m/2^k,\;(m+1)/2^k]}(\omega).$$ The indicator sweeps across $[0,1]$ in dyadic blocks: $X_1=1$ on the whole interval, $X_2,X_3$ each cover half, $X_4$–$X_7$ cover quarters, and so on. For any $\omega\in[0,1]$ and each resolution level $k$, there is exactly one $n$ in $\{2^k,\dots,2^{k+1}-1\}$ whose interval contains $\omega$; consequently $X_n(\omega)=1$ for infinitely many $n$ (once per level), and $\limsup_{n\to\infty}X_n=1$ almost surely. Since $P(|X_n-0|>\varepsilon)=2^{-k}\to0$ for any $\varepsilon\in(0,1)$, we have $X_n\to0$ in probability (and in $L^p$ for every $p\ge1$). Yet $X_n$ does not converge to $0$ almost surely — the sequence oscillates between $0$ and $1$ at every $\omega$ infinitely often.

A useful partial converse connects weak convergence with vanishing perturbations: if $X_n\xrightarrow{d} X$ and $Y_n\to0$ in probability, then $X_nY_n\to0$ in probability. This result is closely related to Slutsky's theorem and supports many of the applications later in this chapter.

---

Flashcards for this section are as follows:

- hierarchy of convergence modes / summary ::@:: Almost-sure $\Rightarrow$ in probability $\Rightarrow$ in distribution; $p \ge 1$-th mean $\Rightarrow$ in probability. No other implications hold in general. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- convergence in probability implies weak convergence: If $X_n\to X$ in probability, what can you conclude about $X_n\xrightarrow{d} X$? ::@:: One has $X_n\xrightarrow{d} X$.
- vanishing product: $X_n\xrightarrow{d} X$ and $Y_n\to_P0$ imply $X_nY_n\to_P0$ ::@:: If $X_n\xrightarrow{d} X$ and $Y_n\to0$ in probability, then $X_nY_n\to0$ in probability.
- typewriter sequence / intuition ::@:: Write $n=2^k+m$ ($0\le m<2^k$). The indicator $1_{[m/2^k,(m+1)/2^k]}$ sweeps across $[0,1]$ in dyadic blocks of width $2^{-k}$. As $n$ increases the blocks get narrower, scanning the whole interval like a typewriter. Each point $\omega$ is covered exactly once per level $k$, so $X_n(\omega)=1$ infinitely often ($\limsup X_n=1$ a.s.), yet the probability mass of each block shrinks to 0.
- typewriter sequence / counterexample ::@:: On $([0,1],\lambda)$ (Lebesgue measure), define $X_n=1_{[m/2^k,(m+1)/2^k]}$ where $n=2^k+m$ ($0\le m<2^k$). Then $X_n\to0$ in probability and in $L^p$, but $\limsup X_n=1$ a.s., so $X_n\not\to0$ almost surely. Shows convergence in probability (and $L^p$) does __not__ imply almost sure convergence. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## almost sure convergence

One says that $(Z_n)_{n\in\mathbb N}$ converges $P$-almost surely to $Z$, written $Z_n\xrightarrow{\text{a.s.}} Z$, if $P\bigl(\{\omega\in\Omega:\lim_{n\to\infty}Z_n(\omega)=Z(\omega)\}\bigr)=1$. More compactly, $P(\lim_{n\to\infty} Z_n = Z) = 1$.

__Measurability of the convergence set.__ We must first check that $\{\omega\in\Omega:\lim_{n\to\infty}Z_n(\omega)=Z(\omega)\}\in\mathcal F$. Recall that $\limsup_{n\to\infty} Y_n$ and $\liminf_{n\to\infty} Y_n$ are measurable when each $Y_n$ is measurable: $\sup_{n\ge m} Y_n$ is measurable for each $m$, and $\inf_{m\ge 1}\sup_{n\ge m} Y_n$ preserves measurability. Now $\{\lim Z_n = Z\} = \{\limsup_{n\to\infty} |Z_n-Z| = 0\} = \bigcap_{k=1}^\infty \{\limsup_{n\to\infty} |Z_n-Z| < 1/k\}$. Because $\limsup |Z_n-Z|$ is measurable, each set $\{\limsup |Z_n-Z| < 1/k\}\in\mathcal F$, and the countable intersection stays in $\mathcal F$.

__Proposition.__ Almost sure convergence implies convergence in probability.

__Proof.__ Assume $Z_n\xrightarrow{\text{a.s.}} Z$. For any $\varepsilon>0$, $P(|Z_n-Z|>\varepsilon) \le P(\bigcup_{k=n}^\infty \{|Z_k-Z|>\varepsilon\})$. By continuity from above, the right-hand side converges to $P(\bigcap_{n=1}^\infty \bigcup_{k=n}^\infty \{|Z_k-Z|>\varepsilon\}) = P(\{|Z_k-Z|>\varepsilon\}\text{ infinitely often (i.o.)})$. This set is contained in $\{\lim Z_n \neq Z\}$, whose probability is $0$ under almost sure convergence. Hence $P(|Z_n-Z|>\varepsilon)\to 0$.

---

Flashcards for this section are as follows:

- almost sure convergence / definition ::@:: $Z_n$ converges $P$-almost surely to $Z$ if $P(\{\omega\in\Omega:\lim_{n\to\infty}Z_n(\omega)=Z(\omega)\})=1$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- convergence set is measurable ::@:: The set $\{\omega\in\Omega:\lim_{n\to\infty}Z_n(\omega)=Z(\omega)\}$ belongs to $\mathcal F$ because $\limsup_{n\to\infty}|Z_n-Z|$ is measurable, and $\{\lim Z_n=Z\} = \bigcap_{k=1}^\infty \{\limsup_{n\to\infty}|Z_n-Z| < 1/k\}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- almost sure convergence implies convergence in probability: proof sketch ::@:: $P(|Z_n-Z|>\varepsilon) \le P(\bigcup_{k=n}^\infty \{|Z_k-Z|>\varepsilon\}) \to P(\{|Z_k-Z|>\varepsilon\}\text{ infinitely often (i.o.)}) \le P(\lim Z_n \neq Z)=0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- $\limsup$ of random variables is measurable ::@:: For each $m$, $\sup_{n\ge m}Y_n$ is measurable because $\{\sup_{n\ge m}Y_n\le t\}=\bigcap_{n\ge m}\{Y_n\le t\}$, and $\limsup Y_n = \inf_{m\ge 1}\sup_{n\ge m}Y_n$, so it remains measurable.
- convergence set as intersection of $\limsup$ conditions ::@:: $\{\lim Z_n = Z\} = \{\limsup_{n\to\infty}|Z_n-Z| = 0\} = \bigcap_{k=1}^\infty \{\limsup|Z_n-Z| < 1/k\}$, proving the convergence set is in $\mathcal F$.
- continuity from above in the a.s. $\Rightarrow$ in prob proof ::@:: $B_n = \bigcup_{k=n}^\infty\{|Z_k-Z|>\varepsilon\}$ forms a decreasing sequence; by continuity from above $P(B_n)\to P(\bigcap_n B_n)=P(\{|Z_k-Z|>\varepsilon\}\text{ infinitely often (i.o.)})$.
- i.o. set containment in convergence-failure set ::@:: $\{|Z_k-Z|>\varepsilon\}\text{ infinitely often (i.o.)} \subseteq \{\lim Z_n \neq Z\}$, because if $|Z_k-Z|>\varepsilon$ for infinitely many $k$, the limit cannot be $Z$. Thus $P(\{|Z_k-Z|>\varepsilon\}\text{ infinitely often (i.o.)})\le P(\lim Z_n\neq Z)=0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## continuous mapping theorem

If $Z_n\to Z$ in probability (resp. almost surely) and $g:\mathbb R\to\mathbb R$ is measurable with $P(Z\in D_g)=0$ where $D_g$ is the discontinuity set of $g$, then $g(Z_n)\to g(Z)$ in probability (resp. almost surely).

__Almost-sure case: pathwise determinism.__ On a set of probability $1$, $Z_n$ and $Z$ behave as ordinary deterministic sequences, so pointwise continuity of $g$ carries the convergence through. Formally, take $\tilde\Omega\in\mathcal F$ with $P(\tilde\Omega)=1$ on which $Z_n(\omega)\to Z(\omega)$. Then $\{Z\in D_g\}^c\cap\tilde\Omega$ still has probability $1$, and $g(Z_n(\omega))\to g(Z(\omega))$ by continuity.

__Probability case: three-way trap decomposition.__ The inequality decomposes the error into three distinct risks:

- __Distance trap__ $P(|Z_n-Z|\ge\delta)$: probability that $Z_n$ is far from $Z$, eliminated by sending $n\to\infty$ first.
- __High-sensitivity trap__ $P(Z\in B_\delta)$: probability that $Z$ lands in a region where a small perturbation can cause a large jump in $g$, eliminated by sending $\delta\downarrow0$ after $n\to\infty$.
- __Discontinuity trap__ $P(Z\in D_g)$: probability that $Z$ hits a discontinuity of $g$, assumed zero.

More precisely, for $\varepsilon>0$ define $B_\delta=\{x\notin D_g:\exists y,\,|x-y|<\delta,\,|g(x)-g(y)|>\varepsilon\}$. Then $P(Z\in B_\delta)\to0$ as $\delta\downarrow0$. The bound $$\begin{aligned}P(|g(Z_n)-g(Z)|>\varepsilon)&\le P(|Z_n-Z|\ge\delta)+P(Z\in B_\delta)+P(Z\in D_g)\end{aligned}$$ lets $n\to\infty$ first (eliminating the distance trap), then $\delta\downarrow0$ (eliminating the sensitivity trap).

__Example.__ For i.i.d. $X_i\sim\operatorname{Exp}(\lambda)$, SLLN gives $\overline X_n\to1/\lambda$ a.s., so $1/\overline X_n\to\lambda$ a.s. by continuous mapping.

---

Flashcards for this section are as follows:

- continuous mapping theorem (a.s. and probability versions) ::@:: Let $D_g$ be the discontinuity set of $g$. If $Z_n\to Z$ in probability (resp. a.s.) and $g$ is measurable with $P(Z\in D_g)=0$, then $g(Z_n)\to g(Z)$ in probability (resp. a.s.). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- continuous mapping theorem: a.s. case proof ::@:: Let $D_g$ be $g$'s discontinuity set. Restrict to the probability-1 set where $Z_n(\omega)\to Z(\omega)$ and $Z(\omega)\notin D_g$; on this set $g$ is continuous at $Z(\omega)$, so $g(Z_n(\omega))\to g(Z(\omega))$ pointwise. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- continuous mapping theorem: probability case proof sketch ::@:: $P(|g(Z_n)-g(Z)|>\varepsilon)\le P(|Z_n-Z|\ge\delta)+P(Z\in B_\delta)+P(Z\in D_g)$, where $D_g$ is $g$'s discontinuity set and $B_\delta=\{x\notin D_g:\exists y,\,|x-y|<\delta,\,|g(x)-g(y)|>\varepsilon\}$ (points where a $\delta$-perturbation of $x$ can change $g$ by $>\varepsilon$). Let $n\to\infty$ (distance term $\to0$), then $\delta\downarrow0$ (sensitivity term $\to0$ because $P(Z\in B_\delta)\to0$ at continuity points). The discontinuity term is zero by $P(Z\in D_g)=0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## weak law of large numbers

Let $X_1,X_2,\dots$ be iid with mean $\mu$ and finite variance $\sigma^2$, and define

$\overline X_n=\frac1n\sum_{j=1}^n X_j$.

Then

$\overline X_n\to \mu$ in probability.

__Proof.__ Independence gives

$\operatorname{Var}(\overline X_n)=\frac{1}{n^2}\sum_{j=1}^n \operatorname{Var}(X_j)=\frac{\sigma^2}{n}$.

Chebyshev's inequality then yields $P(|\overline X_n-\mu|>\varepsilon)\le \frac{\sigma^2}{n\varepsilon^2}\to 0$.

This is the cleanest form of the weak law and is often called Chebyshev's law of large numbers.

__Remarks (assumptions).__

(i) The theorem only requires $\operatorname{Var}(\overline X_n)\to0$. This holds, for example, if the $X_j$ are pairwise uncorrelated with uniformly bounded variance, but $\operatorname{Var}(\overline X_n)\to0$ can also arise under other dependence structures where covariances decay sufficiently fast — pairwise uncorrelated is only one sufficient condition.

(ii) The finite-variance assumption can be relaxed: if $E[|X_1|]<\infty$ (but $\operatorname{Var}(X_1)=\infty$), a more refined truncation argument still yields $\overline X_n\to\mu$ in probability. "Truncation" here means cutting off the extreme values — e.g. defining $X_j^{(n)}=X_j\mathbf1_{|X_j|\le b_n}$ for a growing threshold $b_n$, applying Chebyshev to the bounded (hence finite-variance) truncated variables, and then showing the error from the discarded tails is negligible as $n\to\infty$ because $E[|X_1|]<\infty$ ensures the tails are light enough. However, if $E[|X_1|]=\infty$ the WLLN can fail (the sample mean may not converge to any finite constant).

__Hierarchy of WLLN versions.__ The WLLN admits a chain of progressively weaker conditions:

- __Chebyshev (finite variance):__ $X_j$ iid with $\operatorname{Var}(X_1)<\infty$ → $\overline X_n\to\mu$ in probability.
- __Khinchin (finite mean):__ $X_j$ iid with $E[|X_1|]<\infty$ (no variance needed) → $\overline X_n\to\mu$ in probability.
- __Feller (tail condition):__ $X_j$ iid with $xP(|X_1|>x)\to0$ → $\overline X_n-a_n\to0$ in probability for $a_n=E[X_1\mathbf1_{|X_1|\le n}]$.

Each step weakens the assumption, and Feller's condition is the weakest possible: the Cauchy counterexample shows that if it fails, no centering sequence can salvage the WLLN.

---

Flashcards for this section are as follows:

- sample mean in the weak law: If $X_1,X_2,\dots$ are iid, how is $\overline X_n$ defined? ::@:: $\overline X_n=\frac1n\sum_{j=1}^n X_j$.
- weak law of large numbers: If $X_1,X_2,\dots$ are iid with mean $\mu$ and finite variance, what happens to $\overline X_n$? ::@:: $\overline X_n\to \mu$ in probability.
- variance of the sample mean: Under the weak-law hypotheses, what is $\operatorname{Var}(\overline X_n)$? ::@:: $\operatorname{Var}(\overline X_n)=\sigma^2/n$.
- WLLN: relaxation to pairwise uncorrelated ::@:: The theorem only needs $\operatorname{Var}(\overline X_n)\to0$, which holds if the $X_j$ are pairwise uncorrelated with uniformly bounded variance (independence is not required). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- WLLN: relaxation to infinite variance ::@:: If $E[|X_1|]<\infty$ but $\operatorname{Var}(X_1)=\infty$, truncation (cutting off extreme values at a growing threshold $b_n$ to make the variables bounded, then applying Chebyshev and showing the tails' contribution vanishes) still yields $\overline X_n\to\mu$ in probability. If $E[|X_1|]=\infty$, the WLLN can fail. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Chebyshev WLLN proof ::@:: By independence $\operatorname{Var}(\overline X_n)=\sigma^2/n$, so Chebyshev gives $P(|\overline X_n-\mu|>\varepsilon)\le\sigma^2/(n\varepsilon^2)\to0$. This is the simplest proof of a WLLN.
- hierarchy of WLLN versions ::@:: Chebyshev (finite variance) → Khinchin (finite mean) → Feller ($xP(|X_1|>x)\to0$, with centering). Each step weakens the required assumption, and Feller's condition is the weakest — if it fails, no WLLN with any centering holds. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- WLLN assumption remark (i): essential condition ::@:: The theorem only needs $\operatorname{Var}(\overline X_n)\to0$. This holds, for example, if the $X_j$ are pairwise uncorrelated with uniformly bounded variance, but $\operatorname{Var}(\overline X_n)\to0$ can also hold under other forms of sufficiently weak dependence — pairwise uncorrelated is only one sufficient condition, not the only case. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- WLLN assumption remark (ii): infinite variance ::@:: If $E[|X_1|]<\infty$ but $\operatorname{Var}(X_1)=\infty$, a truncation argument (capping extreme values at a growing threshold $b_n$, applying Chebyshev to the bounded truncated variables, showing the tails' contribution is negligible) still yields $\overline X_n\to\mu$ in probability. If $E[|X_1|]=\infty$, the WLLN can fail. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

<!-- check: ignore-next-line[header_style]: proper noun -->
### Khinchin's weak law

If $X_1,X_2,\dots$ are iid with finite mean $\mu$ (no variance assumption), then $\overline X_n\to\mu$ in probability.

__Proof using characteristic functions.__ Let $\varphi_X(t)=E[e^{itX_1}]$. Since $E[|X_1|]<\infty$, the characteristic function expands near $0$ as $\varphi_X(t)=1+i\mu t+o(t)$. For the characteristic function expansion, the sample mean gives $$\varphi_{\overline X_n}(t)=\bigl(\varphi_X(t/n)\bigr)^n=\Bigl(1+\frac{i\mu t}{n}+o\Bigl(\frac1n\Bigr)\Bigr)^n\to e^{i\mu t},$$ which is the characteristic function of the degenerate law $\delta_\mu$. By Lévy's continuity theorem, $\overline X_n\xrightarrow{d}\delta_\mu$, i.e. $\overline X_n\to\mu$ in probability (since convergence in distribution to a constant implies convergence in probability).

This proof is more powerful than Chebyshev's: it only requires $E[|X_1|]<\infty$, not finite variance.

---

Flashcards for this section are as follows:

- Khinchin's WLLN: assumptions and conclusion ::@:: For iid $X_j$ with $E[|X_1|]<\infty$ (no variance needed), $\overline X_n\to\mu$ in probability. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Khinchin's WLLN: proof via characteristic functions ::@:: $\varphi_{\overline X_n}(t)=(\varphi_X(t/n))^n$ expands to $(1+i\mu t/n+o(1/n))^n\to e^{i\mu t}$, identifying the limit as $\delta_\mu$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Khinchin's WLLN: why the characteristic-function expansion works ::@:: $E[|X_1|]<\infty$ ensures $\varphi_X(t)$ is differentiable at $t=0$ with $\varphi_X'(0)=i\mu$, giving $\varphi_X(t)=1+i\mu t+o(t)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- convergence in distribution to a constant implies convergence in probability ::@:: If $Z_n\xrightarrow{d}\delta_c$, then $P(|Z_n-c|>\varepsilon)\to0$ for every $\varepsilon>0$, which means $Z_n\to c$ in probability. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Khinchin vs Chebyshev WLLN ::@:: Chebyshev requires finite variance; Khinchin only requires finite mean (via CF expansion instead of Chebyshev inequality). Both give $\overline X_n\to\mu$ in probability, but Khinchin's proof is more powerful. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

<!-- check: ignore-next-line[header_style]: proper noun -->
### Feller's necessary and sufficient condition

A necessary and sufficient condition for a weak law to hold (with suitable centering constants $a_n$) is Feller's condition: $$\lim_{x\to\infty} x\,P(|X_1|>x)=0.$$ When this holds, one can take $a_n=E[X_1\mathbb I_{|X_1|\le n}]$ and obtain $\overline X_n-a_n\to0$ in probability.

__Remarks.__ (i) The condition is strictly weaker than finite expectation: it controls only the tail decay rate, requiring $P(|X_1|>x)$ to decay faster than $1/x$. (ii) When $E[X_1]=\mu$ is finite, $a_n\to\mu$ and the classical WLLN is recovered. (iii) The condition is necessary: if $\overline X_n-a_n\to0$ in probability for some $a_n$, then $xP(|X_1|>x)\to0$ as $x\to\infty$. Thus the weak law demands essentially nothing more than slow-enough tail mass.

---

Flashcards for this section are as follows:

- Feller's necessary and sufficient condition for the WLLN ::@:: $\lim_{x\to\infty}xP(|X_1|>x)=0$; centering constants $a_n=E[X_1\mathbb I_{|X_1|\le n}]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Feller's condition: intuitive meaning ::@:: $xP(|X_1|>x)\to0$ means $P(|X_1|>x)$ decays faster than $1/x$. It is strictly weaker than finite expectation. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- centering constant in Feller's WLLN ::@:: $a_n=E[X_1\mathbb I_{|X_1|\le n}]$ corrects for the truncated mean; when $E[X_1]=\mu$ is finite, $a_n\to\mu$ and the classical WLLN is recovered. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Feller's condition: necessity direction ::@:: If $\overline X_n-a_n\to0$ in probability for some $a_n$, then $xP(|X_1|>x)\to0$ must hold. So Feller's condition is not just sufficient but also necessary for a WLLN with centering. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

<!-- check: ignore-next-line[header_style]: proper noun -->
### Cauchy counterexample

Let $X_1,X_2,\dots$ be iid Cauchy $(0,1)$ with density $f(x)=1/(\pi(1+x^2))$. Then $P(|X_1|>x)\sim 1/(\pi x)$, so $xP(|X_1|>x)\to 1/\pi\neq0$, violating Feller's condition. The sample mean is again Cauchy $(0,1)$ — stable under averaging — so $\overline X_n$ has the same distribution as $X_1$ and does not concentrate. There is no finite limit $\mu$ or centering $a_n$ such that $\overline X_n-a_n\to0$ in probability.

This shows that the WLLN is not universal: heavy-tailed distributions can defeat averaging.

---

Flashcards for this section are as follows:

- Cauchy counterexample to the WLLN ::@:: For iid Cauchy variables, $\overline X_n\sim\text{Cauchy}(0,1)$ — no concentration, tails too heavy ($xP(|X_1|>x)\to 1/\pi$), violating Feller's condition. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Cauchy: stability under averaging ::@:: The characteristic function of Cauchy(0,1) is $\varphi(t)=e^{-|t|}$; then $\varphi_{\overline X_n}(t)=(\varphi(t/n))^n=e^{-|t|}$, so $\overline X_n$ has the same Cauchy(0,1) distribution for every $n$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Cauchy: tail-decay rate ::@:: Density $f(x)=1/(\pi(1+x^2))$ gives $P(|X_1|>x)\sim 1/(\pi x)$, so $xP(|X_1|>x)\to 1/\pi$, violating Feller's condition. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Cauchy: no centering helps ::@:: Because $\overline X_n$ has the same Cauchy(0,1) distribution for every $n$, no centering sequence $a_n$ can make $\overline X_n-a_n\to0$ in probability — the distribution does not concentrate at all. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

<!-- check: ignore-next-line[header_style]: proper noun -->
### WLLN vs SLLN comparison

| Aspect                        | WLLN                                                                         | SLLN                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Convergence mode              | In probability                                                               | Almost surely                                                                                             |
| Typical assumptions           | $E[\vert X_1\vert]<\infty$ (Khinchin) or $xP(\vert X_1\vert>x)\to0$ (Feller) | $E[\vert X_1\vert]<\infty$ (Kolmogorov)                                                                   |
| Necessary condition           | $xP(\vert X_1\vert>x)\to0$ (Feller)                                          | $E[\vert X_1\vert]<\infty$                                                                                |
| Speed (under finite variance) | $O_P(1/\sqrt n)$                                                             | No universal $n^{-\alpha}$ a.s. rate; Hartman–Wintner LIL gives $O\bigl(\sqrt{(\log\log n)/n}\bigr)$ a.s. |

The WLLN holds under strictly weaker conditions than the SLLN (cf. Feller's condition vs finite expectation). The SLLN gives a stronger conclusion but demands more of the tails.

The two $O$ notations in the speed row: $O_P(1/\sqrt n)$ means $\sqrt n(\overline X_n-\mu)$ is bounded in probability (tight), the typical CLT rate; $O\bigl(\sqrt{(\log\log n)/n}\bigr)$ a.s. means the almost-sure fluctuation is bounded by $\sqrt{(\log\log n)/n}$ up to a constant, following from the Hartman–Wintner law of the iterated logarithm.

---

Flashcards for this section are as follows:

- WLLN vs SLLN comparison ::@:: WLLN requires only $xP(|X_1|>x)\to0$ (Feller) for convergence in probability; SLLN needs $E[|X_1|]<\infty$ for almost sure convergence. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- WLLN vs SLLN: rate of convergence ::@:: Under finite variance, WLLN gives $O_P(1/\sqrt n)$ (tightness: $\sqrt n(\overline X_n-\mu)$ is bounded in probability, the CLT rate). The SLLN has no universal $n^{-\alpha}$ a.s. rate; the Hartman–Wintner LIL gives $O\bigl(\sqrt{(\log\log n)/n}\bigr)$ a.s. (sharp a.s. bound: fluctuations grow like $\sqrt{(\log\log n)/n}$ up to a constant). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- WLLN and SLLN: conditions compared ::@:: The WLLN holds under $xP(|X_1|>x)\to0$ (Feller), which is strictly weaker than the SLLN's requirement $E[|X_1|]<\infty$ (Kolmogorov). The stronger SLLN conclusion (a.s. vs in probability) demands stronger tail control. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## strong law of large numbers

__Kolmogorov's strong law of large numbers.__ Let $X_1,X_2,\dots$ be i.i.d. with $E[|X_1|]<\infty$ (hence the mean $\mu=E[X_1]$ exists). Then the sample mean converges almost surely to the true mean:

$\overline X_n\to \mu$ almost surely.

The condition $E[|X_1|]<\infty$ is necessary as well as sufficient for the SLLN in the i.i.d. case — if $E[|X_1|]=\infty$, the sample mean diverges almost surely. For independent but not identically distributed variables, a variant with finite second moments and a variance-summability condition also gives an SLLN (see the subsection below).

The route taken in the course passes through the Borel-Cantelli lemmas and a truncation argument.

<!-- check: ignore-next-line[header_style]: Borel-Cantelli is a proper noun (eponymous) -->
### Borel-Cantelli lemmas

The Borel-Cantelli lemmas are the fundamental tools for converting probability estimates into almost-sure statements. They answer a basic question: given a sequence of events $A_n$, when can we be sure that infinitely many of them happen (or don't)?

__Intuition for the two lemmas.__ BC1 says that if the total probability mass $\sum P(A_n)$ is finite, there simply isn't enough "room" for infinitely many events to occur — like a finite budget that can only cover finitely many purchases. BC2 says the opposite: if the total mass is infinite and the events are independent (no "coordination" to avoid each other), then infinitely many must occur almost surely — like having unlimited budget guarantees you'll buy infinitely many items, provided each purchase decision is made independently.

The set $\{A_n\text{ i.o.}\}$ is $\bigcap_{m=1}^\infty\bigcup_{n=m}^\infty A_n$, the $\limsup$ of the events — the collection of outcomes that belong to $A_n$ for arbitrarily large $n$. It is a kind of "supremum over tails": as $m$ grows, the tail union $\bigcup_{n=m}^\infty A_n$ shrinks, and their intersection catches what persists in all tails.

__First Borel-Cantelli lemma.__ If $\sum_n P(A_n)<\infty$, then $P(\bigcap_{m=1}^\infty\bigcup_{n=m}^\infty A_n)=P(A_n \text{ i.o.})=0$.

__Intuition for the proof.__ The i.o. set is the limit of decreasing tail unions; by continuity from above its probability is the limit of $P(\bigcup_{n=m}^\infty A_n)$ as $m\to\infty$. The union bound controls each tail union by the remaining tail sum $\sum_{n=m}^\infty P(A_n)$, which tends to $0$ because the full sum converges.

__Proof.__ Since

$\{A_n \text{ i.o.}\}=\bigcap_{m=1}^{\infty}\bigcup_{n\ge m}A_n=\limsup_{n\to\infty}A_n$ (the set-theoretic limsup, a supremum over tails in the sense that it is the limit of the decreasing sequence of tail unions $\bigcup_{n\ge m}A_n$ as $m\to\infty$), the union bound shows $P\left(\bigcup_{n\ge m}A_n\right)\le \sum_{n\ge m}P(A_n)\to 0$, and continuity from above finishes the proof.

__Second Borel-Cantelli lemma.__ If the $A_n$ are independent and $\sum_n P(A_n)=\infty$, then $P(\bigcap_{m=1}^\infty\bigcup_{n=m}^\infty A_n)=P(A_n \text{ i.o.})=1$.

__Intuition for the proof.__ We show that the complement — "$A_n$ occurs only finitely often" — has probability zero. That complement is $\bigcup_{m=1}^\infty\bigcap_{n=m}^\infty A_n^c$ (eventually all complements happen). By independence, $P(A_n^c\text{ eventually})=P(\bigcap_{n=m}^\infty A_n^c)$ for some $m$ is a product $\prod_{n=m}^\infty(1-P(A_n))$. The bound $1-x\le e^{-x}$ turns the product into $\exp(-\sum_{n=m}^\infty P(A_n))$, which is $0$ because the tail sum diverges. So the probability that all $A_n$ eventually stop happening is zero — hence infinitely many $A_n$ happen.

__Proof.__ Since $A_n$ are independent, so are their complements $A_n^c$. Then

$$P\!\left(\bigcap_{n=m}^\infty A_n^c\right)=\prod_{n=m}^\infty(1-P(A_n)).$$

Using $1-x\le e^{-x}$ for all $x\in\mathbb R$,

$$\prod_{n=m}^\infty(1-P(A_n))\le\exp\!\Bigl(-\sum_{n=m}^\infty P(A_n)\Bigr)=0,$$

because the tail sum diverges. Hence $P(\bigcup_{n=m}^\infty A_n)=1$ for every $m$. By continuity from above on the decreasing sequence $\{\bigcup_{n=m}^\infty A_n\}_{m=1}^\infty$, we obtain

$$P\!\left(\bigcap_{m=1}^\infty\bigcup_{n=m}^\infty A_n\right)=\lim_{m\to\infty}P\!\left(\bigcup_{n=m}^\infty A_n\right)=1.$$

Thus $A_n$ occurs infinitely often with probability $1$.

This turns divergent sums of independent probabilities into almost-sure infinitely-often events.

---

Flashcards for this subsection are as follows:

- first Borel-Cantelli lemma ::@:: If $\sum_n P(A_n)<\infty$, what is $P(A_n \text{ i.o.})$? $P(\bigcap_{m=1}^\infty\bigcup_{n=m}^\infty A_n)=P(A_n \text{ i.o.})=0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- BC1 / intuition ::@:: Finite total probability mass ⇒ not enough "room" for infinitely many events to occur. Like a finite budget that can only cover finitely many purchases. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- BC1 proof / intuition ::@:: The i.o. set is the limit of decreasing tail unions $\bigcup_{n=m}^\infty A_n$. By continuity from above, $P(\text{i.o.})=\lim_{m\to\infty}P(\bigcup_{n=m}^\infty A_n)$. The union bound controls each tail union by the remaining tail sum $\sum_{n=m}^\infty P(A_n)$, which →0 because the full sum converges. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- first Borel-Cantelli lemma / proof ::@:: $\{A_n\text{ i.o.}\}=\bigcap_{m=1}^\infty\bigcup_{n\ge m}A_n$; union bound gives $P(\bigcup_{n\ge m}A_n)\le\sum_{n\ge m}P(A_n)\to0$; continuity from above yields $P(\{A_n\text{ i.o.}\})=0$.
- second Borel-Cantelli lemma ::@:: If the events $A_n$ are independent and $\sum_n P(A_n)=\infty$, what is $P(A_n \text{ i.o.})$? $P(\bigcap_{m=1}^\infty\bigcup_{n=m}^\infty A_n)=P(A_n \text{ i.o.})=1$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- BC2 / intuition ::@:: Infinite total probability mass + independence ⇒ infinitely many events must occur almost surely. Independence prevents "coordination" to avoid each other — like having unlimited budget guarantees infinitely many purchases if each decision is independent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- BC2 proof / intuition ::@:: Prove complement (eventually all $A_n^c$) has probability 0. Independence makes $P(A_n^c\text{ eventually})$ a product $\prod(1-P(A_n))$; the bound $1-x\le e^{-x}$ turns it into $\exp(-\sum P(A_n))=0$ when the tail sum diverges. So eventually-all-complements is impossible → i.o. must happen. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- second Borel-Cantelli lemma / proof ::@:: For independent $A_n$, $P(\bigcap_{n=m}^\infty A_n^c)=\prod_{n=m}^\infty(1-P(A_n))\le\exp(-\sum_{n=m}^\infty P(A_n))=0$, so $P(\bigcup_{n=m}^\infty A_n)=1$ for all $m$; continuity from above on the decreasing tail unions gives $P(\bigcap_{m=1}^\infty\bigcup_{n=m}^\infty A_n)=1$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### strong-law proof

__Strong-law proof (subsequence method).__ Under the SLLN condition $E[|X_1|]<\infty$, we first reduce to bounded variables via truncation:

- __Truncate.__ Define $Y_j=X_j\mathbf1_{|X_j|\le j}$, cutting off values exceeding the index $j$.
- __Tail error is negligible.__ $\sum_{j=1}^\infty P(X_j\neq Y_j)=\sum_{j=1}^\infty P(|X_1|>j)\le E[|X_1|]<\infty$, so the first Borel-Cantelli lemma gives $P(X_j\neq Y_j\text{ i.o.})=0$. On the probability-1 set where $X_j=Y_j$ eventually, the two averages differ by only finitely many terms, whose contribution $\to0$ as $n\to\infty$; hence $\overline X_n$ and $\frac1n\sum_{j=1}^n Y_j$ share the same almost-sure limit.
- __Centering correction.__ $E[Y_j]\to\mu$ by dominated convergence ($|Y_j|\le|X_1|$ with $E[|X_1|]<\infty$), so replacing $Y_j$ by $Y_j-E[Y_j]$ does not affect the limit.

Having removed the tail problem via $E[|X_1|]<\infty$, the truncated variables are bounded and the proof below (which assumes $|X_j|\le C$) applies to them. The proof therefore assumes $|X_j|\le C$ and proceeds in two steps.

_Step 1 — convergence on a subsequence._ Take $n_k=k^2$ as the subsequence. By Chebyshev's inequality, $$P(|\overline X_{n_k}-\mu|>\varepsilon)\le\frac{\operatorname{Var}(\overline X_{n_k})}{\varepsilon^2}=\frac{\sigma^2}{k^2\varepsilon^2},$$ which is summable over $k$. The first Borel-Cantelli lemma gives $P(|\overline X_{n_k}-\mu|>\varepsilon\text{ i.o.})=0$, so $\overline X_{n_k}\to\mu$ almost surely along the squares.

_Step 2 — gap filling._ For $n$ between $k^2$ and $(k+1)^2$, control how far $\overline X_n$ can stray from $\overline X_{k^2}$. For bounded variables ($|X_j|\le C$), split the sample mean: $$\overline X_n-\overline X_{k^2}=\frac{1}{n}\sum_{j=1}^n X_j-\frac{1}{k^2}\sum_{j=1}^{k^2}X_j=\Bigl(\frac1n-\frac1{k^2}\Bigr)\sum_{j=1}^{k^2}X_j+\frac1n\sum_{j=k^2+1}^n X_j.$$ Using $|X_j|\le C$, $$|\overline X_n-\overline X_{k^2}|\le\Bigl(\frac1{k^2}-\frac1n\Bigr)k^2C+\frac{n-k^2}{n}C=\frac{n-k^2}{n}C+\frac{n-k^2}{n}C=2\frac{n-k^2}{n}C.$$ Since $k^2\le n\le(k+1)^2=k^2+2k+1$, we have $n-k^2\le2k+1$ and $n\ge k^2$, so $$2\frac{n-k^2}{n}C\le2\frac{2k+1}{k^2}C=\frac{4C}{k}+O\!\left(\frac1{k^2}\right).$$ Thus $\max_{k^2\le n\le(k+1)^2}|\overline X_n-\overline X_{k^2}|\to0$ as $k\to\infty$. Combined with the subsequence convergence, this forces $\overline X_n\to\mu$ almost surely for all $n$.

__Lemma (subsequence criterion for a.s. convergence).__ $Z_n\to Z$ almost surely if and only if every subsequence contains a further sub-subsequence converging almost surely to $Z$.

---

Flashcards for this section are as follows:

- Kolmogorov's SLLN: conditions and conclusion ::@:: For i.i.d. $X_j$ with $E[|X_1|]<\infty$, $\overline X_n\to E[X_1]$ almost surely. The condition $E[|X_1|]<\infty$ is necessary as well as sufficient for the SLLN. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- SLLN: truncation purpose and steps ::@:: Under $E[|X_1|]<\infty$, truncate $X_j$ at $j$ ($Y_j=X_j\mathbf1_{|X_j|\le j}$). Borel-Cantelli shows the discarded tails contribute zero a.s. ($\sum P(|X_1|>j)\le E[|X_1|]<\infty$). Dominated convergence gives $E[Y_j]\to\mu$. The truncated variables are bounded, so the bounded-variable proof applies. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- SLLN: truncation tail estimate ::@:: $\sum_{j=1}^\infty P(|X_1|>j)\le E[|X_1|]<\infty$, so by Borel-Cantelli $P(X_j\neq Y_j\text{ i.o.})=0$. Where $X_j=Y_j$ eventually, the two averages differ by only finitely many terms (contribution $\to0$ as $n\to\infty$), so their a.s. limits coincide. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- SLLN: why the subsequence $n_k=k^2$ works ::@:: Along $k^2$, Chebyshev gives $P(|\overline X_{k^2}-\mu|>\varepsilon)\le\sigma^2/(k^2\varepsilon^2)$, summable, so Borel-Cantelli yields almost sure convergence.
- SLLN: gap-filling idea ::@:: Extend a.s. convergence from squares $n_k=k^2$ to all $n$ by controlling $|\overline X_n-\overline X_{k^2}|$. Split the sample-mean difference: $\overline X_n-\overline X_{k^2}=(\frac1n-\frac1{k^2})\sum_{j=1}^{k^2}X_j+\frac1n\sum_{j=k^2+1}^n X_j$ — the first term corrects the averaging factor on the common part, the second adds the fresh terms. Bound each piece using $|X_j|\le C$. For the first term, $\frac1n<\frac1{k^2}$ makes $(\frac1n-\frac1{k^2})$ negative, so $|(\frac1n-\frac1{k^2})\sum_{j=1}^{k^2}X_j|\le(\frac1{k^2}-\frac1n)k^2C=\frac{n-k^2}{n}C$. The second term is at most $\frac{n-k^2}{n}C$. Hence $|\overline X_n-\overline X_{k^2}|\le2\frac{n-k^2}{n}C$. For $n\in[k^2,(k+1)^2]$, the gap satisfies $n-k^2\le2k+1$, so $2\frac{n-k^2}{n}C\le2\frac{2k+1}{k^2}C=\frac{4C}{k}+O(1/k^2)\to0$. Thus the gap closes uniformly within each block, and $\overline X_{k^2}\to\mu$ a.s. forces $\overline X_n\to\mu$ a.s. for all $n$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- subsequence criterion for a.s. convergence ::@:: $Z_n\to Z$ a.s. iff every subsequence contains a further sub-subsequence converging a.s. to $Z$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- SLLN: non-iid variant exists ::@:: For independent (not necessarily i.i.d.) $X_j$ with $E[X_j^2]<\infty$ and $\sum_{k=1}^\infty\frac1{k^2}\operatorname{Var}[X_k]<\infty$, $\overline X_n-E[\overline X_n]\xrightarrow{\text{a.s.}}0$. The identical-distribution assumption is not essential — only moment control is. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

<!-- check: ignore-next-line[header_style]: proper noun -->
### Kolmogorov's SLLN (non-identically distributed)

If the $X_j$ are independent but no longer identically distributed, Kolmogorov's strong law can still be stated under a second-moment condition. Let $X_1,X_2,\dots$ be independent with $E[X_j^2]<\infty$ for all $j$ and

$$\sum_{k=1}^\infty\frac{1}{k^2}\operatorname{Var}[X_k]<\infty.$$

Then the centered sample mean converges almost surely to $0$:

$$\overline X_n-E[\overline X_n]\xrightarrow{\text{a.s.}}0.$$

__Relation to the i.i.d. case.__ When the $X_j$ are i.i.d. with finite variance, $\operatorname{Var}[X_k]=\sigma^2$ and $\sum_{k=1}^\infty\sigma^2/k^2<\infty$, so the i.i.d. SLLN is recovered. The non-i.i.d. version relaxes the identical-distribution requirement at the cost of requiring finite second moments, whereas the i.i.d. version only needs $E[|X_1|]<\infty$ (first moment).

__Proof sketch (different from the i.i.d. case).__ The i.i.d. proof used the subsequence method ($n_k=k^2$) with Chebyshev and gap-filling, relying on the common variance $\sigma^2$ to make the Chebyshev probabilities summable. In the non-iid setting with potentially different variances, a different strategy is needed because the common $\sigma^2$ is not available and the gap-filling step would require a uniform bound that may not exist.

Instead, the non-iid proof proceeds via weighted sums and Kronecker's lemma:

1. __Center.__ Let $Y_j=X_j-E[X_j]$ so $E[Y_j]=0$.
2. __Weighted sums.__ Consider $T_n=\sum_{j=1}^n Y_j/j$. Then $\operatorname{Var}[T_n]=\sum_{j=1}^n\operatorname{Var}[X_j]/j^2$, which converges as $n\to\infty$ by the hypothesis.
3. __Almost-sure convergence of $T_n$.__ For independent centered variables, $\sum\operatorname{Var}[Y_j/j]<\infty$ implies that $T_n$ converges almost surely (by Kolmogorov's three-series theorem or martingale convergence).
4. __Kronecker's lemma.__ If $\sum_{j=1}^\infty Y_j/j$ converges, then $\frac1n\sum_{j=1}^n Y_j\to0$ a.s. — the weights $1/j$ are replaced by equal weights $1/n$.
5. __Conclusion.__ $\overline X_n-E[\overline X_n]=\frac1n\sum_{j=1}^n Y_j\xrightarrow{\text{a.s.}}0$.

The i.i.d. subsequence proof is more constructive and avoids variance entirely (using truncation + $E[|X_1|]<\infty$). The non-iid proof uses the variance-summability condition to guarantee convergence of the weighted series, then transfers the result back to the sample mean via Kronecker's lemma.

---

Flashcards for this subsection are as follows:

- Kolmogorov's SLLN (non-iid): statement ::@:: For independent $X_j$ with $E[X_j^2]<\infty$ and $\sum_{k=1}^\infty\frac1{k^2}\operatorname{Var}[X_k]<\infty$, $\overline X_n-E[\overline X_n]\xrightarrow{\text{a.s.}}0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Kolmogorov's SLLN (non-iid): relation to i.i.d. case ::@:: For i.i.d. $X_j$ with finite variance, $\sum\sigma^2/k^2<\infty$ holds trivially — the non-iid version contains the i.i.d. finite-variance case. The trade-off: the non-iid version needs second moments but drops the identical-distribution assumption. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Kolmogorov's SLLN (non-iid): proof structure ::@:: Center $Y_j=X_j-E[X_j]$; define weighted sum $T_n=\sum Y_j/j$; convergent variance $\sum\operatorname{Var}[X_j]/j^2<\infty$ gives a.s. convergence of $T_n$; Kronecker's lemma transfers back: $\frac1n\sum Y_j\to0$ a.s. No subsequence method needed. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Kronecker's lemma ::@:: If $\sum_{j=1}^\infty a_j$ converges, then $\frac1n\sum_{j=1}^n j a_j\to0$. Equivalently, if $\sum_{j=1}^\infty x_j/j$ converges, then $\frac1n\sum_{j=1}^n x_j\to0$. Used to convert weighted-sum convergence into sample-mean convergence. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Kolmogorov's SLLN (non-iid): why the proof differs from i.i.d. ::@:: The i.i.d. proof uses subsequence $n_k=k^2$, Chebyshev with common $\sigma^2$, and gap-filling. The non-iid proof cannot rely on a common variance, so it switches to weighted sums $Y_j/j$ and Kronecker's lemma, leveraging the variance-summability condition to force a.s. convergence. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Kolmogorov's SLLN (non-iid): variance summability $\to$ a.s. convergence ::@:: $\operatorname{Var}[T_n]=\sum_{j=1}^n\operatorname{Var}[X_j]/j^2$ converges by hypothesis, so $T_n$ is $L^2$-Cauchy for independent centered variables; $L^2$ convergence for independent increments gives an $L^2$-bounded martingale, which converges a.s. by the martingale convergence theorem. (Equivalently, Kolmogorov's three-series theorem: the variance condition alone suffices because the variables are centered.) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Kolmogorov's SLLN (non-iid): Kronecker's lemma application ::@:: $T_n=\sum_{j=1}^n Y_j/j$ converges a.s., so set $x_j=Y_j$ in $\sum x_j/j$ convergent $\implies\frac1n\sum x_j\to0$ to get $\frac1n\sum_{j=1}^n Y_j\xrightarrow{\text{a.s.}}0$, i.e. $\overline X_n-E[\overline X_n]\xrightarrow{\text{a.s.}}0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## law of the iterated logarithm

__Law of the iterated logarithm (Hartman–Wintner).__ For iid $X_j$ with mean $\mu$ and finite variance $\sigma^2$, $$\limsup_{n\to\infty}\frac{\overline X_n-\mu}{\sigma\sqrt{2(\log\log n)/n}}=1\quad\text{a.s.}$$ The $\liminf$ is $-1$ a.s., so the normalized sample mean oscillates between $\pm1$ infinitely often. While the CLT describes $\sqrt{n}$-scale fluctuations in distribution, the LIL gives the a.s. fluctuation envelope: extreme deviations grow like $\sqrt{2n\log\log n}$, only slightly larger than $\sqrt{n}$. The extra factor $\sqrt{\log\log n}$ grows so slowly ($\sqrt{\log\log 10^{100}}\approx 2.7$) that for practical sample sizes the LIL and CLT scales are nearly indistinguishable.

---

Flashcards for this section are as follows:

- LIL / statement ::@:: For iid $X_j$ with mean $\mu$ and finite variance $\sigma^2$, $\limsup_{n\to\infty}\frac{\overline X_n-\mu}{\sigma\sqrt{2(\log\log n)/n}}=1$ a.s. and $\liminf$ is $-1$, so the normalized sample mean oscillates between $\pm1$ infinitely often. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- LIL / intuition ::@:: The LIL gives the tight a.s. fluctuation envelope: for any $\varepsilon>0$, $|\overline X_n-\mu| < (1+\varepsilon)\sigma\sqrt{2(\log\log n)/n}$ eventually, and $|\overline X_n-\mu| > (1-\varepsilon)\sigma\sqrt{2(\log\log n)/n}$ occurs infinitely often. The scale $\sqrt{2n\log\log n}$ is only slightly larger than the CLT's $\sqrt n$; the extra factor $\sqrt{\log\log n}$ grows so slowly that for typical sample sizes the two scales are nearly the same size. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## central limit theorem

Let $X_1,X_2,\dots$ be iid with mean $\mu$ and variance $\sigma^2>0$. Then

$\frac{\sum_{j=1}^n X_j-n\mu}{\sigma\sqrt n}\xrightarrow{d} N(0,1)$.

Equivalently,

$\sqrt n\,\frac{\overline X_n-\mu}{\sigma}\xrightarrow{d} N(0,1)$.

So the law of large numbers gives the deterministic limit, while the central limit theorem gives the first random correction around that limit.

---

Flashcards for this section are as follows:

- central limit theorem for sums: If $X_1,X_2,\dots$ are iid with mean $\mu$ and variance $\sigma^2>0$, what is the limiting law of $\frac{\sum_{j=1}^n X_j-n\mu}{\sigma\sqrt n}$? ::@:: The normalized sum converges in distribution to $N(0,1)$.
- central limit theorem for the sample mean: Under the CLT hypotheses, what is the limiting law of $\sqrt n\,\frac{\overline X_n-\mu}{\sigma}$? ::@:: The normalized sample mean converges in distribution to $N(0,1)$.

<!-- check: ignore-next-line[header_style]: MGF is an acronym -->
### MGF convergence and convergence in distribution

If the MGFs of a sequence of random variables converge pointwise to the MGF of a limit in a neighborhood of $0$, convergence in distribution follows. This is the engine behind the CLT proof when MGFs exist.

__Theorem (MGF convergence ⇒ convergence in distribution).__ Let $Z_n,Z$ be random variables whose MGFs $\psi_n(t)=E[e^{tZ_n}]$ and $\psi(t)=E[e^{tZ}]$ all exist for $|t|<\delta$ (some $\delta>0$). If $\psi_n(t)\to\psi(t)$ for every $t\in(-\delta,\delta)$, then $Z_n\xrightarrow{d}Z$.

_Proof._ The argument proceeds in three stages.

1. __Real convergence: pointwise → uniform on compacta.__ MGFs are convex on the real interval where they exist. A pointwise-convergent sequence of convex functions on $(-\delta,\delta)$ converges uniformly on every compact subinterval — in particular on $[-\delta/2,\delta/2]$.
2. __Analytic continuation to characteristic functions.__ Each MGF extends to an analytic function on the complex strip $S=\{z\in\mathbb C:|\Re(z)|<\delta\}$ via $\psi_n(z)=E[e^{zZ_n}]$. On $S$ we have $|\psi_n(z)|\le\psi_n(\Re(z))$; together with the uniform real convergence this gives uniform boundedness on compact subsets of $S$. __Vitali's convergence theorem__ for analytic functions then yields $\psi_n(z)\to\psi(z)$ uniformly on compact subsets of $S$. Restricting to the imaginary axis $z=it$ ($t\in\mathbb R$) gives pointwise convergence of characteristic functions: $$\phi_n(t)=\psi_n(it)\to\psi(it)=\phi(t)\quad\text{for all }t\in\mathbb R.$$

3. __Lévy's continuity theorem__ asserts that pointwise convergence of CFs to a limit continuous at $0$ implies convergence in distribution. Hence $Z_n\xrightarrow{d}Z$.

__MGF of $N(0,1)$.__ For $Z\sim N(0,1)$, $$\psi_Z(t)=E[e^{tZ}]=\int_{-\infty}^\infty\frac{1}{\sqrt{2\pi}}e^{tz}e^{-z^2/2}\,dz=e^{t^2/2}\int_{-\infty}^\infty\frac{1}{\sqrt{2\pi}}e^{-(z-t)^2/2}\,dz=e^{t^2/2}.$$

__Reverse direction ($\Leftarrow$) does not come for free.__ Convergence in distribution alone does not guarantee MGF convergence, even when every $Z_n$ and $Z$ has a finite MGF in a neighborhood of $0$. For example, let $Z_n=n$ with probability $1/n$ and $0$ otherwise. Then $Z_n\xrightarrow{d}0$ and each MGF $\psi_n(t)=(1-1/n)+(1/n)e^{tn}$ exists for all real $t$, but $\psi_n(t)\to\infty$ for $t>0$ while $\psi_0(t)=1$. The obstacle is that $e^{tZ_n}$ is unbounded, so the portmanteau theorem does not apply. To obtain $\psi_n(t)\to\psi(t)$ from $Z_n\xrightarrow{d}Z$ one needs uniform integrability of $\{e^{tZ_n}\}$. The argument proceeds as follows:

1. For a truncation level $M>0$, define $g_M(z)=e^{tz}\land M$ (i.e. $e^{tz}$ capped at $M$). This function is bounded and continuous.
2. By the triangle inequality, $$|E[e^{tZ_n}]-E[e^{tZ}]|\le|E[g_M(Z_n)]-E[g_M(Z)]|+E[e^{tZ_n}\mathbf{1}_{e^{tZ_n}>M}]+E[e^{tZ}\mathbf{1}_{e^{tZ}>M}].$$
3. For each fixed $M$, $g_M$ is bounded continuous, so portmanteau gives $E[g_M(Z_n)]\to E[g_M(Z)]$ as $n\to\infty$; the first term vanishes in the limit.
4. Uniform integrability of $\{e^{tZ_n}\}$ makes the tail expectations arbitrarily small uniformly in $n$ for sufficiently large $M$. The same holds for the single variable $Z$ by fatou or by noting that $\{e^{tZ}\}$ alone is UI.
5. Taking $n\to\infty$ then $M\to\infty$ yields $\psi_n(t)\to\psi(t)$.

In the CLT setting only the forward direction is used.

---

Flashcards for this section are as follows:

- MGF convergence theorem (forward direction) ::@:: If $\psi_n(t)=E[e^{tZ_n}]$ and $\psi(t)=E[e^{tZ}]$ exist on $(-\delta,\delta)$ and $\psi_n(t)\to\psi(t)$ pointwise there, then $Z_n\xrightarrow{d}Z$. Three stages: (i) convexity upgrades pointwise to uniform convergence on compacta; (ii) Vitali's theorem extends convergence from the real interval to the complex strip $|\Re(z)|<\delta$; (iii) restricting to $z=it$ gives CF convergence $\phi_n(t)\to\phi(t)$, so Lévy's continuity theorem applies. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- MGF convergence: convexity → uniform on compacta ::@:: MGFs are convex on the real interval where they exist. A sequence of convex functions converging pointwise on an interval converges uniformly on every compact subinterval. This uniform control is what lets the complex-analytic step go through.
- MGF convergence: why convergence extends to CFs ::@:: Each $\psi_n(z)=E[e^{zZ_n}]$ extends analytically to the strip $|\Re(z)|<\delta$. Uniform convergence on real compacta implies uniform boundedness there, which propagates to complex compacta via analyticity. Vitali's theorem then forces $\psi_n(z)\to\psi(z)$ on the whole strip; taking $z=it$ yields $\phi_n(t)\to\phi(t)$, and Lévy's continuity theorem gives $Z_n\xrightarrow{d}Z$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- MGF vs characteristic function ::@:: Characteristic functions $\phi(t)=E[e^{itX}]$ always exist (bounded modulus 1) and are the gold standard; MGFs $\psi(t)=E[e^{tX}]$ may be infinite for some $t>0$, restricting their use to light-tailed distributions. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- MGF of $N(0,1)$ ::@:: $\psi_Z(t)=e^{t^2/2}$.
- counterexample: reverse direction of MGF lemma fails even with MGFs ::@:: For $Z_n=n$ w.p. $1/n$, $0$ otherwise, $Z_n\xrightarrow{d}0$; each $\psi_{Z_n}(t)=(1-1/n)+(1/n)e^{tn}$ exists on all $\mathbb R$ yet $\psi_n(t)\to\infty$ for $t>0$ (while $\psi_0(t)=1$). MGF existence alone does not salvage the reverse direction — UI of $\{e^{tZ_n}\}$ is needed. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why UI is sufficient for the reverse MGF lemma ::@:: Step 1: truncate $e^{tz}$ at $M$, defining $g_M(z)=e^{tz}\land M$ (bounded continuous). Step 2: triangle inequality $|E[e^{tZ_n}]-E[e^{tZ}]|\le|E[g_M(Z_n)]-E[g_M(Z)]|+E[e^{tZ_n}\mathbf{1}_{e^{tZ_n}>M}]+E[e^{tZ}\mathbf{1}_{e^{tZ}>M}]$. Step 3: for fixed $M$, portmanteau $\Rightarrow\ E[g_M(Z_n)]\to E[g_M(Z)]$; first term $\to0$. Step 4: UI of $\{e^{tZ_n}\}$ makes the two tail expectations $<\varepsilon$ uniformly in $n$ for large $M$. Step 5: let $n\to\infty$ then $M\to\infty$ to get $\psi_n(t)\to\psi(t)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### proof sketch for the CLT

The course's proof uses moment-generating functions. Let

$Y_j=\frac{X_j-\mu}{\sigma}$ and $S_n=\frac{Y_1+\cdots+Y_n}{\sqrt n}$.

Then $E[Y_j]=0$ and $E[Y_j^2]=1$. Write $L(u)=\log\psi_{Y_1}(u)$. Since $\psi_{Y_1}(0)=1$, $\psi_{Y_1}'(0)=E[Y_1]=0$, and $\psi_{Y_1}''(0)=E[Y_1^2]=1$, one has $L(0)=0$, $L'(0)=0$, $L''(0)=1$. Because $\psi_{S_n}(t)=(\psi_{Y_1}(t/\sqrt n))^n$, a second-order Taylor expansion of $\log\psi_{S_n}(t)$ gives $\displaystyle\log\psi_{S_n}(t)=nL\!\left(\frac t{\sqrt n}\right)=n\!\left(\frac{t^2}{2n}+o\!\left(\frac1n\right)\right)=\frac{t^2}{2}+o(1)\to\frac{t^2}{2}$.

Thus $\psi_{S_n}(t)\to e^{t^2/2}$, the MGF of $N(0,1)$. By the continuity lemma for MGFs, $S_n\xrightarrow{d}N(0,1)$.

__With characteristic functions.__ An alternative proof uses characteristic functions $\varphi(t)=E[e^{itX}]$ instead of MGFs, avoiding the requirement that MGFs exist. Expanding $\varphi_{Y_1}(t)=1-t^2/2+o(t^2)$ near $0$ and raising to the $n$-th power yields $\varphi_{S_n}(t)=(1-t^2/(2n)+o(1/n))^n\to e^{-t^2/2}$, the CF of $N(0,1)$. Lévy's continuity theorem then gives $S_n\xrightarrow{d}N(0,1)$.

__Rate of convergence (Berry–Esseen).__ The CLT guarantees approximation quality improves as $n$ grows, but does not say how fast. The __Berry–Esseen theorem__ fills this gap: if $E[|X_1-\mu|^3]<\infty$, then for all $n$ and all $x$,

$\bigl|P(S_n\le x)-\Phi(x)\bigr|\le\frac{C\,\rho}{\sigma^3\sqrt n},\qquad\rho=E[|X_1-\mu|^3]$,

where $C$ is a universal constant. The best known bounds are $0.40973\le C<0.4748$ (the optimal $C$ is not known); $C\approx0.5$ is a common textbook approximation. This gives a concrete $O(1/\sqrt n)$ error bound, justifying the rule of thumb that CLT approximations are decent for moderate $n$ (say $n\ge30$).

---

Flashcards for this section are as follows:

- normalized variables in the CLT proof: How are $Y_j$ and $S_n$ defined? ::@:: $Y_j=\frac{X_j-\mu}{\sigma}$ and $S_n=\frac{Y_1+\cdots+Y_n}{\sqrt n}$.
- CLT proof via MGFs: log Taylor expansion ::@:: Let $L(u)=\log\psi_{Y_1}(u)$. $L(0)=0$, $L'(0)=0$, $L''(0)=1$; expanding $L(t/\sqrt n)$ yields $\log\psi_{S_n}(t)=nL(t/\sqrt n)\to t^2/2$, so $\psi_{S_n}(t)\to e^{t^2/2}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- CLT proof: the $(1+a_n/n)^n$ limit ::@:: $\varphi_{S_n}(t)=(1-t^2/(2n)+o(1/n))^n\to e^{-t^2/2}$ via $(1+a_n/n)^n\to e^a$ whenever $a_n\to a$.
- why the second-order expansion is valid ::@:: Finite variance ensures $\varphi_{Y_1}(t)$ is twice differentiable at $0$; $\varphi_{Y_1}'(0)=iE[Y_1]=0$ and $\varphi_{Y_1}''(0)=-E[Y_1^2]=-1$, so Taylor's theorem gives $\varphi_{Y_1}(t)=1-t^2/2+o(t^2)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Berry–Esseen theorem: rate of convergence in the CLT ::@:: If $E[|X_1-\mu|^3]<\infty$, then $|P(S_n\le x)-\Phi(x)|\le C\rho/(\sigma^3\sqrt n)$ where $\rho=E[|X_1-\mu|^3]$ and $0.40973\le C<0.4748$ — an $O(1/\sqrt n)$ bound. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- CLT proof via MGFs ::@:: When MGFs exist, $\psi_{Y_1}(t)=1+t^2/2+o(t^2)$, so $\psi_{S_n}(t)=(1+t^2/(2n)+o(1/n))^n\to e^{t^2/2}$, the MGF of $N(0,1)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### proof structure summary

Both approaches follow the same template:

1. Center and scale: $Y_j=(X_j-\mu)/\sigma$.
2. Show $E[Y_1]=0$, $E[Y_1^2]=1$.
3. Expand the transform (characteristic function or MGF) near $0$: $\varphi_{Y_1}(t)=1-t^2/2+o(t^2)$.
4. Use independence to raise to the $n$-th power: $\varphi_{S_n}(t)=(1-t^2/(2n)+o(1/n))^n\to e^{-t^2/2}$.
5. Identify $e^{-t^2/2}$ as the transform of $N(0,1)$, conclude by uniqueness.

---

Flashcards for this section are as follows:

- CLT proof structure template ::@:: Center/scale $\to$ expand transform near 0 $\to$ raise to $n$ via independence $\to$ identify limit as $N(0,1)$ transform. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

<!-- check: ignore-next-line[section_example_heading]: die-roll CLT as numerical illustration of limit theorems -->
### examples

Roll a fair die $n=100$ times. The sum $S_{100}=\sum_{i=1}^{100}X_i$ has mean $100\cdot3.5=350$ and variance $100\cdot(35/12)\approx291.67$. By the CLT, $$P(S_{100}>400)=P\!\left(\frac{S_{100}-350}{\sqrt{291.67}}>\frac{50}{\sqrt{291.67}}\approx2.928\right)\approx P(Z>2.928)\approx0.0017.$$

__Empirical variance.__ Let $X_1,\dots,X_n$ be i.i.d. with $E[X_1]=\mu$, $\operatorname{Var}(X_1)=\sigma^2$, and $E[X_1^4]<\infty$. Define the sample variance $S_n^2=\frac1n\sum_{i=1}^nX_i^2-\overline X_n^2$. Then $$\sqrt n\,(S_n^2-\sigma^2)\xrightarrow{d} N(0,\alpha),\qquad\alpha=E[(X_1-\mu)^4]-\sigma^4.$$

_Proof sketch._ Write $Y_i=(X_i-\mu)^2$ so that $E[Y_1]=\sigma^2$ and $\operatorname{Var}(Y_1)=\alpha$. The CLT gives $\sqrt n(\overline Y_n-\sigma^2)\xrightarrow{d} N(0,\alpha)$. Now $S_n^2-\sigma^2=(\overline Y_n-\sigma^2)+(\mu^2-\overline X_n^2)$. Since $\overline X_n\to\mu$ a.s., $\mu^2-\overline X_n^2\to0$ in probability. By Slutsky's theorem (or the vanishing-perturbation proposition), the limit distribution of $\sqrt n(S_n^2-\sigma^2)$ is the same as that of $\sqrt n(\overline Y_n-\sigma^2)$.

---

Flashcards for this section are as follows:

- die-roll sum CLT example: $P(S_{100}>400)$ (sum of 100 dice) approximation ::@:: $S_{100}$ has mean $350$, variance $100\cdot35/12\approx291.67$; CLT gives $P(Z>50/\sqrt{291.67})\approx0.0017$.
- empirical variance: asymptotic distribution ::@:: $\sqrt n(S_n^2-\sigma^2)\xrightarrow{d} N(0,E[(X_1-\mu)^4]-\sigma^4)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- empirical variance: proof idea ::@:: Write $S_n^2-\sigma^2=(\overline Y_n-\sigma^2)+(\mu^2-\overline X_n^2)$ where $Y_i=(X_i-\mu)^2$; CLT handles the first term, SLLN+Slutsky eliminates the second. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

<!-- check: ignore-next-line[header_style]: Slutsky is a proper noun (eponymous) -->
## Slutsky's theorem and vanishing perturbation

These results let one "clean up" a weak-convergence limit by discarding asymptotically negligible perturbations. They formalize the idea that if two sequences are asymptotically indistinguishable — their difference vanishes in probability — they must share the same limiting distribution, and that constants in the limit can absorb many operations cleanly.

### vanishing-perturbation proposition

_Intuition._ If two paths through a forest get arbitrarily close to each other, they must be heading to the same destination. Similarly, if $X_n$ converges weakly and $Y_n$ gets arbitrarily close to it (the difference vanishes in probability), then $Y_n$ inherits the same limit — the "perturbation" between them fades away.

If $X_n\xrightarrow{d} X$ and $X_n-Y_n\to0$ in probability, then $Y_n\xrightarrow{d} X$.

_Proof sketch._ Let $Z_n=Y_n-X_n\to0$ in probability. For a continuity point $x$ of $F_X$, $$\begin{aligned}F_{Y_n}(x)&=P(Y_n\le x)=P(X_n+Z_n\le x) \\ &\le P(X_n\le x+\varepsilon)+P(|Z_n|\ge\varepsilon)\quad\Rightarrow\quad\limsup_{n\to\infty}F_{Y_n}(x)\le F_X(x+\varepsilon), \end{aligned}$$ and a matching lower bound gives $\liminf_{n\to\infty}F_{Y_n}(x)\ge F_X(x-\varepsilon)$. Sending $\varepsilon\downarrow0$ yields $F_{Y_n}(x)\to F_X(x)$.

---

Flashcards for this subsection are as follows:

- intuition: vanishing-perturbation proposition ::@:: If two sequences are asymptotically indistinguishable (difference $\to0$ in probability), they share the same weak limit — like two converging paths must lead to the same destination. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- vanishing-perturbation proposition ::@:: If $X_n\xrightarrow{d}X$ and $X_n-Y_n\to0$ in probability, then $Y_n\xrightarrow{d}X$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- proof: sandwich argument ::@:: Bound $F_{Y_n}(x)\le F_{X_n}(x+\varepsilon)+P(|X_n-Y_n|\ge\varepsilon)$ and $F_{Y_n}(x)\ge F_{X_n}(x-\varepsilon)-P(|X_n-Y_n|\ge\varepsilon)$; take $\limsup/\liminf$, then $\varepsilon\downarrow0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why "vanishing perturbation" ::@:: The difference $X_n-Y_n$ is a perturbation that vanishes in probability; it is too small to affect the limiting distribution. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

<!-- check: ignore-next-line[header_style]: Slutsky is a proper noun (eponymous) -->
### Slutsky's theorem

_Intuition._ When one operand converges to a constant, joint limiting behavior simplifies dramatically — the constant passes through addition, multiplication, and division as if it were deterministic. This is why we can normalize a sample mean by an estimated standard deviation and still obtain a standard normal limit.

If $X_n\xrightarrow{d} X$ and $Y_n\to c$ in probability (with $c$ a constant), then $$X_n+Y_n\xrightarrow{d} X+c,\qquad X_nY_n\xrightarrow{d} cX,$$ and for $c\neq0$, $$\frac{X_n}{Y_n}\xrightarrow{d}\frac{X}{c}.$$

_Proof._ For the sum, $(X_n+Y_n)-(X_n+c)=Y_n-c\to0$ in probability, so the vanishing-perturbation proposition applies. For the product, first note $cX_n\xrightarrow{d}cX$ by the continuous mapping theorem. Then use the auxiliary result that $X_n\xrightarrow{d}X$ and $Y_n\to0$ in probability imply $X_nY_n\to0$ in probability. Hence $X_nY_n-cX_n=X_n(Y_n-c)\to0$ in probability, and the vanishing-perturbation proposition gives $X_nY_n\xrightarrow{d}cX$. The quotient follows similarly.

---

Flashcards for this subsection are as follows:

- intuition: Slutsky's theorem ::@:: When one sequence converges to a constant, the constant passes cleanly through addition, multiplication, and division — the stochastic and deterministic parts separate in the limit.
- Slutsky's theorem: sum ::@:: If $X_n\xrightarrow{d}X$ and $Y_n\xrightarrow{p}c$, then $X_n+Y_n\xrightarrow{d}X+c$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Slutsky's theorem: product ::@:: If $X_n\xrightarrow{d}X$ and $Y_n\xrightarrow{p}c$, then $X_nY_n\xrightarrow{d}cX$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Slutsky's theorem: quotient ::@:: If $X_n\xrightarrow{d}X$ and $Y_n\xrightarrow{p}c\neq0$, then $X_n/Y_n\xrightarrow{d}X/c$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- proof: Slutsky's theorem ::@:: Sum: vanishing-perturbation on $(X_n+Y_n)-(X_n+c)$. Product: CMT gives $cX_n\xrightarrow{d}cX$; vanishing product on $X_n(Y_n-c)$; vanishing-perturbation again. Quotient: analogous. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why a constant limit is needed ::@:: Slutsky requires $Y_n\xrightarrow{p}c$ (constant). If $Y_n\xrightarrow{d}Y$ with random $Y$, the joint distribution of $(X_n,Y_n)$ is uncontrolled, so algebraic operations don't pass through cleanly. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### vanishing product

_Intuition._ Weakly convergent sequences are tight — the probability of extreme values is uniformly bounded. When this is multiplied by a term that shrinks to zero in probability, the product also shrinks: large values of $X_n$ can't occur often enough to offset the vanishing $Y_n$.

If $X_n\xrightarrow{d}X$ and $Y_n\to0$ in probability, then $X_nY_n\to0$ in probability.

_Proof._ For any $\varepsilon,k>0$, $$P(|X_nY_n|\ge\varepsilon)\le P(|X_n|>k)+P\!\left(|Y_n|\ge\frac{\varepsilon}{k}\right).$$ Taking $n\to\infty$ then $k\to\infty$ gives $\limsup_{n\to\infty}P(|X_nY_n|\ge\varepsilon)\le P(|X|>k)\to0$.

---

Flashcards for this subsection are as follows:

- intuition: vanishing product ::@:: $X_n$ is tight (large values have small probability) while $Y_n\to_p0$; the product shrinks because $X_n$ can't blow up often enough to offset the vanishing $Y_n$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- vanishing product ::@:: If $X_n\xrightarrow{d}X$ and $Y_n\to0$ in probability, then $X_nY_n\to0$ in probability. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- proof: vanishing product ::@:: $P(|X_nY_n|\ge\varepsilon)\le P(|X_n|>k)+P(|Y_n|\ge\varepsilon/k)$; $n\to\infty$ then $k\to\infty$ sends both terms to $0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- role of tightness ::@:: Without tightness of $\{X_n\}$, $Y_n\to_p0$ alone could fail — $X_n$ might take unboundedly large values that offset a small $Y_n$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

<!-- check: ignore-next-line[section_example_heading]: worked example integrated within Slutsky section -->
### example: empirical variance

_Intuition._ The empirical variance uses the estimated mean $\overline X_n$, introducing an extra source of error. Remarkably, this error is of smaller order — it vanishes in probability — so the asymptotic distribution of $\sqrt n(\hat\sigma_n^2-\sigma^2)$ is the same as if the true mean were known.

Let $X_1,X_2,\dots$ be i.i.d. with mean $\mu$, variance $\sigma^2$, and finite fourth moment $\mu_4^{(c)}=E[(X_1-\mu)^4]$.

__Step 1: a convenient infeasible estimator.__ If the true mean $\mu$ were known, we could use $\frac1n\sum_{i=1}^n(X_i-\mu)^2$. Define $Y_i=(X_i-\mu)^2$; then $E[Y_1]=\sigma^2$ and $\operatorname{Var}(Y_1)=\mu_4^{(c)}-\sigma^4$. The CLT gives $$\sqrt n\!\left(\frac1n\sum_{i=1}^n Y_i-\sigma^2\right)\xrightarrow{d}N\!\left(0,\mu_4^{(c)}-\sigma^4\right).$$

__Step 2: relate the empirical variance to the infeasible estimator.__ Expand $\hat\sigma_n^2$ around $\mu$: $$\begin{aligned}\hat\sigma_n^2&=\frac1n\sum_{i=1}^n(X_i-\overline X_n)^2=\frac1n\sum_{i=1}^n\bigl[(X_i-\mu)-(\overline X_n-\mu)\bigr]^2\\[2pt]&=\frac1n\sum_{i=1}^n(X_i-\mu)^2-\frac{2(\overline X_n-\mu)}n\sum_{i=1}^n(X_i-\mu)+(\overline X_n-\mu)^2.\end{aligned}$$ The middle term simplifies because $\frac1n\sum_{i=1}^n(X_i-\mu)=\overline X_n-\mu$, yielding $$\hat\sigma_n^2 = \frac1n\sum_{i=1}^n Y_i \;\-\; (\overline X_n-\mu)^2.$$

Thus $\hat\sigma_n^2$ is exactly the infeasible estimator minus a squared-error correction that shrinks as $\overline X_n$ approaches $\mu$.

__Step 3: scale the difference.__ Multiply the relation by $\sqrt n$: $$\sqrt n(\hat\sigma_n^2-\sigma^2)=\sqrt n\!\left(\frac1n\sum_{i=1}^n Y_i-\sigma^2\right)-\sqrt n(\overline X_n-\mu)\cdot(\overline X_n-\mu).$$ The first term converges weakly to $N(0,\mu_4^{(c)}-\sigma^4)$ by Step~1. For the second term, note that

- $\overline X_n-\mu\to0$ in probability (WLLN);
- $\sqrt n(\overline X_n-\mu)\xrightarrow{d}N(0,\sigma^2)$ (CLT), hence it is tight.

By the vanishing-product result, the product $\sqrt n(\overline X_n-\mu)\cdot(\overline X_n-\mu)$ converges in probability to $0$.

__Step 4: apply the vanishing-perturbation proposition.__ Since $\sqrt n(\hat\sigma_n^2-\sigma^2)$ and $\sqrt n(\frac1n\sum Y_i-\sigma^2)$ differ by something that vanishes in probability, the vanishing-perturbation proposition forces them to share the same weak limit: $$\sqrt n(\hat\sigma_n^2-\sigma^2)\xrightarrow{d}N\!\left(0,\mu_4^{(c)}-\sigma^4\right).$$

---

Flashcards for this subsection are as follows:

- intuition for the empirical-variance derivation: why can we ignore the correction $(\overline X_n-\mu)^2$ in the limit? ::@:: Replacing the true mean $\mu$ by the sample mean $\overline X_n$ creates a correction $(\overline X_n-\mu)^2$ that vanishes in probability; Slutsky lets us ignore it in the limit.
- finite fourth moment: why is $E[X_1^4]<\infty$ required for the asymptotic distribution of $\hat\sigma_n^2$? ::@:: The CLT for $\frac1n\sum(X_i-\mu)^2$ requires $\operatorname{Var}((X_i-\mu)^2)=\mu_4^{(c)}-\sigma^4$ to be finite, where $\mu_4^{(c)}=E[(X_1-\mu)^4]$ is the fourth central moment and $\sigma^2=\operatorname{Var}(X_1)$; this holds iff the fourth moment is finite.
- expansion of $\hat\sigma_n^2$ around the true mean $\mu$: what formula relates $\hat\sigma_n^2$ to the infeasible estimator $\frac1n\sum Y_i$? ::@:: $\hat\sigma_n^2 = \frac1n\sum Y_i - (\overline X_n-\mu)^2$ where $\hat\sigma_n^2$ is the empirical variance, $\overline X_n$ is the sample mean, $\mu$ is the true mean, and $Y_i=(X_i-\mu)^2$. Expanding $(X_i-\overline X_n)^2$ and simplifying shows the squared-mean correction appears because centering at $\overline X_n$ rather than $\mu$ subtracts exactly $(\overline X_n-\mu)^2$.
- vanishing of the squared-mean correction term: why does $\sqrt n(\overline X_n-\mu)^2$ converge in probability to 0? ::@:: $\sqrt n(\overline X_n-\mu)(\overline X_n-\mu)\to_p0$: the sample-mean deviation $\overline X_n-\mu$ (where $\mu$ is the true mean) vanishes in probability (WLLN) while $\sqrt n(\overline X_n-\mu)$ is tight (CLT), so the vanishing-product result applies.
- how the vanishing-perturbation proposition applies to the empirical-variance derivation: why does the correction not affect the limiting distribution? ::@:: The difference $\sqrt n(\hat\sigma_n^2-\sigma^2)-\sqrt n(\frac1n\sum Y_i-\sigma^2)$ vanishes in probability, where $\hat\sigma_n^2$ is the empirical variance, $\sigma^2$ is the true variance, and $Y_i=(X_i-\mu)^2$; so the vanishing-perturbation proposition equates their weak limits. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- asymptotic distribution of the empirical variance: what is the weak limit of $\sqrt n(\hat\sigma_n^2-\sigma^2)$? ::@:: $\sqrt n(\hat\sigma_n^2-\sigma^2)\xrightarrow{d}N(0,\mu_4^{(c)}-\sigma^4)$, where $\hat\sigma_n^2$ is the empirical variance, $\sigma^2$ is the true variance, and $\mu_4^{(c)}=E[(X_1-\mu)^4]$ is the fourth central moment.<p>Brief derivation: $\operatorname{Var}((X_i-\mu)^2)=E[((X_i-\mu)^2)^2]-E[(X_i-\mu)^2]^2=\mu_4^{(c)}-\sigma^4$, so CLT on $Y_i=(X_i-\mu)^2$ gives the limit for $\frac1n\sum Y_i$; the squared-mean correction $(\overline X_n-\mu)^2$ vanishes by the vanishing-product result, and the vanishing-perturbation proposition transfers the limit to $\hat\sigma_n^2$.

#### zero asymptotic variance

The asymptotic variance $\mu_4^{(c)}-\sigma^4$ can be zero even when $\sigma^2>0$. The condition $\mu_4^{(c)}=\sigma^4$ is equivalent to $\operatorname{Var}((X_1-\mu)^2)=0$, i.e., the squared deviation $(X_1-\mu)^2$ is almost surely equal to its expectation $\sigma^2$. This happens in two regimes:

1. __Degenerate case__ ($\sigma^2=0$): $X_1$ is almost surely constant. Then there is no variance to estimate at all — the problem is trivial.

2. __Symmetric two-point case__ ($\sigma^2>0$): $X_1$ takes exactly the two values $\mu\pm\sigma$, each with probability $1/2$. Then every squared deviation satisfies $(X_i-\mu)^2=\sigma^2$ deterministically, so the infeasible estimator $\frac1n\sum_{i=1}^n(X_i-\mu)^2$ equals $\sigma^2$ exactly for every $n$ — it has no sampling variability whatsoever. The correction $(\overline X_n-\mu)^2$ still converges to $0$ in probability, so $\hat\sigma_n^2$ inherits this exactness asymptotically.

In both regimes the leading CLT term vanishes, so $\hat\sigma_n^2$ converges to $\sigma^2$ faster than $1/\sqrt n$ — specifically, $\hat\sigma_n^2-\sigma^2=o_p(n^{-1/2})$. The usual $\sqrt n$ scaling overestimates the convergence rate.

---

Flashcards for this subsection are as follows:

- zero asymptotic variance: what does $\mu_4^{(c)}=\sigma^4$ imply about $(X_1-\mu)^2$? ::@:: $\operatorname{Var}((X_1-\mu)^2)=0$, so $(X_1-\mu)^2$ is almost surely equal to $\sigma^2$; the squared deviation has no randomness.
- zero asymptotic variance: degenerate case ($\sigma^2=0$) ::@:: $X_1$ is almost surely constant; there is no variance to estimate and the asymptotic variance is trivially zero ($\mu_4^{(c)}=0=\sigma^4$).
- zero asymptotic variance: symmetric two-point case ::@:: $X_1$ takes values $\mu\pm\sigma$ each with probability $1/2$; then every $(X_i-\mu)^2=\sigma^2$ deterministically, so $\mu_4^{(c)}=\sigma^4$ and the asymptotic variance is zero even though $\sigma^2>0$. (A rescaled symmetric Bernoulli.) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- zero asymptotic variance: convergence rate when $\mu_4^{(c)}=\sigma^4$ ::@:: The leading CLT term vanishes, so $\hat\sigma_n^2-\sigma^2=o_p(n^{-1/2})$ — convergence is faster than $1/\sqrt n$. The usual $\sqrt n$ scaling overestimates the rate.

## normal approximations and continuity correction

The CLT is used to approximate distributions of large sums by a normal law. For lattice variables one often improves the approximation by a continuity correction, replacing an event such as $S_n\le k$ by the normal event $S_n\le k+1/2$ before standardizing.

This correction is especially relevant when approximating binomial probabilities by normal probabilities. For $S_n\sim\operatorname{Binomial}(n,p)$, the CLT gives $$P(a\le S_n\le b)\approx\Phi\!\left(\frac{b+\frac12-np}{\sqrt{np(1-p)}}\right)-\Phi\!\left(\frac{a-\frac12-np}{\sqrt{np(1-p)}}\right),$$ where the $\pm\frac12$ is the continuity correction.

__Rule of thumb.__ The normal approximation to the binomial is reliable when $np\ge5$ and $n(1-p)\ge5$. When $np$ is small, the Poisson approximation is more accurate.

__Inverse problem: required sample size.__ Given a desired margin of error $\delta>0$ and confidence level $1-\alpha$, one can solve for $n$ such that $P(|\hat p-p|<\delta)\ge 1-\alpha$, where $\hat p=S_n/n$ with $S_n\sim\operatorname{Binomial}(n,p)$ (the sample proportion). The CLT gives $\hat p\approx N(p,p(1-p)/n)$, so standardizing yields $Z:=\frac{\hat p-p}{\sqrt{p(1-p)/n}}\approx N(0,1)$ and

$$P(|\hat p-p|<\delta)=P\!\left(|Z|<\frac{\delta}{\sqrt{p(1-p)/n}}\right).$$

For $N(0,1)$, $P(|Z|<z_{\alpha/2})=1-\alpha$, so requiring this probability to be at least $1-\alpha$ implies $\frac{\delta}{\sqrt{p(1-p)/n}}\ge z_{\alpha/2}$. Squaring and rearranging:

$$\delta\ge z_{\alpha/2}\sqrt{\frac{p(1-p)}{n}}\quad\Longrightarrow\quad n\ge\frac{z_{\alpha/2}^2\,p(1-p)}{\delta^2}.$$

Since $p$ is unknown, the worst-case $p=1/2$ (maximizing $p(1-p)=1/4$) gives the conservative bound $n\ge z_{\alpha/2}^2/(4\delta^2)$. For $\alpha=0.05$ ($z_{0.025}\approx1.96$) and $\delta=0.05$, this yields $n\ge385$.

---

Flashcards for this section are as follows:

- continuity correction for $S_n\le k$ ::@:: For lattice variables, one often improves a normal approximation by replacing an event such as $S_n\le k$ with $S_n\le k+1/2$ before standardizing.
- continuity correction for binomial probabilities ::@:: $P(a\le S_n\le b)\approx\Phi((b+1/2-np)/\sqrt{np(1-p)})-\Phi((a-1/2-np)/\sqrt{np(1-p)})$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why continuity correction works ::@:: Binomial increments are integer-valued; approximating a discrete $P(S_n\le k)$ by a continuous normal $P(S_n\le k)$ underestimates coverage by $0.5$ on average. Adding $1/2$ before standardizing centers the bar at $k$ correctly. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- binomial CLT example (sum of 100 dice): $P(40\le S_{100}\le 60)$ with $p=0.5$ ::@:: Mean $50$, variance $25$, continuity-corrected: $\Phi((60.5-50)/5)-\Phi((39.5-50)/5)=\Phi(2.1)-\Phi(-2.1)\approx0.964$.
- normal approximation to binomial: rule of thumb ::@:: Reliable when $np\ge5$ and $n(1-p)\ge5$; otherwise Poisson approximation is more accurate. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- required $n$ for $P(|\hat p-p|<\delta)\ge 1-\alpha$ with $\hat p=S_n/n\sim\operatorname{Binomial}(n,p)$ ::@:: CLT $\Rightarrow\hat p\approx N(p,p(1-p)/n)$, so $Z:=(\hat p-p)/\sqrt{p(1-p)/n}\approx N(0,1)$. Then $P(|\hat p-p|<\delta)=P(|Z|<\delta/\sqrt{p(1-p)/n})\ge 1-\alpha$ requires $\delta/\sqrt{p(1-p)/n}\ge z_{\alpha/2}$. Square $\Rightarrow n\ge z_{\alpha/2}^2\,p(1-p)/\delta^2$. Worst-case $p=1/2$ gives $n\ge z_{\alpha/2}^2/(4\delta^2)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## applications and intuition

The weak law explains why empirical averages stabilize. If $X_1,X_2,\dots$ represent repeated measurements, then the sample mean becomes a reliable approximation of $E[X_1]$ for large $n$.

Typical examples include Monte Carlo integration, empirical frequencies of coin tosses, and averages of transformed observations such as

$\frac1n\sum_{j=1}^n e^{-X_j/2}$.

As long as the transformed variables are iid with finite variance, the same argument applies.

---

Flashcards for this section are as follows:

- why the weak law matters for large $n$ ::@:: It explains why empirical averages stabilize and become reliable approximations to the true mean for large $n$.
- transformed-observation average $\frac1n\sum_{j=1}^n e^{-X_j/2}$ in the weak law: What kind of average is still covered when the transformed variables are iid with finite variance? ::@:: An average such as $\frac1n\sum_{j=1}^n e^{-X_j/2}$ is still covered.

<!-- check: ignore-next-line[header_style]: proper noun -->
### Monte Carlo integration

A direct application of the strong law (or weak law) is Monte Carlo estimation. For a piecewise continuous function $h:[0,1]\to\mathbb R$ with $\int_0^1 h^2(x)\,dx<\infty$, one can approximate the integral $I=\int_0^1 h(x)\,dx$ by $$\widehat I_n=\frac1n\sum_{i=1}^n h(U_i),$$ where $U_1,\dots,U_n$ are i.i.d. $\operatorname{Uniform}(0,1)$. The SLLN gives $\widehat I_n\to I$ almost surely.

By choosing a different sampling distribution, other integrals can be handled. For example, for $X_1,\dots,X_n\sim N(0,1)$ i.i.d., one can approximate $$\int_{-\infty}^\infty e^{-x^2/2}h(x)\,dx\approx\frac{\sqrt{2\pi}}{n}\sum_{i=1}^n h(X_i),$$ provided $\int_{-\infty}^\infty h^2(x)e^{-x^2/2}\,dx<\infty$.

---

Flashcards for this subsection are as follows:

- Monte Carlo integration: basic idea ::@:: Approximate $I=\int_0^1 h(x)\,dx$ by $\frac1n\sum_{i=1}^n h(U_i)$ with $U_i\sim\operatorname{Uniform}(0,1)$ i.i.d. By the SLLN the estimate converges to $I$ almost surely. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Monte Carlo integration for normal distributions ::@:: With $X_i\sim N(0,1)$ i.i.d., $\frac{\sqrt{2\pi}}{n}\sum_{i=1}^n h(X_i)\to\int_{-\infty}^\infty e^{-x^2/2}h(x)\,dx$ a.s. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### application to random walks

For the simple symmetric random walk on $\mathbb Z$, the position after $n$ steps is

$X_n=\xi_1+\cdots+\xi_n$,

where the $\xi_j$ are iid with mean $0$ and variance $1$. The weak and strong laws imply

$\frac{X_n}{n}\to 0$,

in probability and almost surely, while the central limit theorem gives

$\frac{X_n}{\sqrt n}\xrightarrow{d} N(0,1)$.

Thus the walk has vanishing average velocity but Gaussian fluctuations on the diffusive scale $\sqrt n$.

The LLN squashes the walk to a point (linear $n$ scale), while the CLT reveals the $\sqrt n$ diffusive dynamics — both are necessary: the LLN gives the deterministic limit, and the CLT gives the scale of fluctuations. The $\sqrt n$ scale follows from uncorrelated increments: $\operatorname{Var}(X_n)=n$, so the standard deviation grows as $\sqrt n$. This quadratic space-time relation ($x^2\sim t$) underpins physical diffusion; the continuous limit of the walk yields Brownian motion via Donsker's invariance principle (functional CLT). Moreover, local mass at the origin scales as $1/\sqrt n$; since $\sum 1/\sqrt n$ diverges, Pólya's theorem guarantees the walk is recurrent — it returns infinitely often with probability 1. Despite zero average velocity, fluctuations are unbounded, so a gambler with finite capital faces almost sure ruin.

---

Flashcards for this section are as follows:

- simple symmetric random walk position: How is $X_n$ written in terms of the increments $\xi_j$? ::@:: $X_n=\xi_1+\cdots+\xi_n$.
- law of large numbers for the random walk: What happens to $X_n/n$? ::@:: It converges to $0$ in probability and almost surely.
- central limit theorem for the random walk: What happens to $X_n/\sqrt n$? ::@:: It converges in distribution to $N(0,1)$.
- scaling disconnect between LLN and CLT ::@:: LLN scales by $n$, squashing to a point; CLT scales by $\sqrt n$, revealing diffusive dynamics. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- origin of the $\sqrt n$ scale ::@:: Uncorrelated increments give $\operatorname{Var}(X_n)=n$, so the RMS distance grows as $\sqrt n$ — the generic diffusive scale.
- random walk to Brownian motion ::@:: The $x^2\sim t$ scaling leads to Brownian motion via Donsker's invariance principle (functional CLT), formalizing the microscopic basis of the heat equation. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- recurrence and Pólya's theorem ::@:: Local mass at origin $\sim 1/\sqrt n$; $\sum 1/\sqrt n$ diverges, so the walk returns infinitely often with probability 1. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- unbounded fluctuations despite mean zero ::@:: Average velocity 0 but $\sqrt n$ fluctuations are unbounded — a gambler with finite capital faces almost sure ruin. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
