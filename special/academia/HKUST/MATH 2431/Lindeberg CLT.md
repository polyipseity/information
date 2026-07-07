---
aliases:
  - Lindeberg CLT
  - Lindeberg replacement method
  - Lindeberg's central limit theorem
  - Lindeberg's condition
  - Lindeberg-Feller CLT
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/Lindeberg_CLT
  - language/in/English
---
# Lindeberg CLT

The Lindeberg central limit theorem generalises the classical CLT from i.i.d. sequences to triangular arrays of independent random variables under a weak uniformity condition. It is the definitive CLT for independent (but not necessarily identically distributed) summands.

Let $\{X_{n,i}:i=1,\dots,k_n,\,n\ge1\}$ be a triangular array of random variables, independent within each row, with $E[X_{n,i}]=\mu_{n,i}$ and $\operatorname{Var}[X_{n,i}]=\sigma_{n,i}^2<\infty$. Set $$S_n=\sum_{i=1}^{k_n}X_{n,i},\qquad s_n^2=\operatorname{Var}[S_n]=\sum_{i=1}^{k_n}\sigma_{n,i}^2.$$

Intuitively, when each term contributes negligibly to the total, its individual distribution washes out — only its mean and variance survive. The Lindeberg condition, defined below, makes this "negligibility" precise.

Lindeberg's replacement method is a direct probabilistic approach to proving the CLT that avoids characteristic functions. It proves $E[g((S_n-E[S_n])/s_n)]\to E[g(Z)]$ for smooth test functions $g$ (twice differentiable with $g''$ bounded and uniformly continuous), then extends to indicator functions by smooth approximation. The method replaces each standardised variable $Z_{n,i}=(X_{n,i}-\mu_{n,i})/s_n$ with independent normals $W_{n,i}\sim N(0,\sigma_{n,i}^2/s_n^2)$ one at a time (telescoping sum) so that $\sum_iW_{n,i}\sim N(0,1)$, and uses Taylor expansions to show each replacement changes $g(\sum_iZ_{n,i})$ by a negligible amount. The two stages are: (1) smooth $g$ convergence via replacement, (2) extension from smooth to indicator functions.

---

Flashcards for this section are as follows:

- Lindeberg-Feller CLT / triangular array definition ($\{X_{n,i}\}$, $S_n$, $s_n^2$) and row-wise independence <p> __Notation:__ $S_n=\sum_{i=1}^{k_n}X_{n,i}$ (row sum), $s_n^2=\operatorname{Var}[S_n]=\sum_{i=1}^{k_n}\sigma_{n,i}^2$ (row variance). ::@:: Triangular array $\{X_{n,i}:1\le i\le k_n,\,n\ge1\}$, independent within each row. <p> No identical-distribution assumption — only independence and finite variances. Both $k_n$ and the distributions may change with $n$. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg-Feller CLT / convergence to normality ::@:: Under the Lindeberg (or Lindeberg–Feller) condition, $(S_n-E[S_n])/s_n\xrightarrow{d}N(0,1)$. <p> The result requires only Lindeberg's condition plus finite variances — no identical distribution, no higher moment assumptions, and no bound on $k_n$ beyond what $s_n^2$ implicitly controls. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg replacement method / core procedure (replace $Z_{n,i}$ with $W_{n,i}$, Taylor expand, vanish remainder) ::@:: The method replaces each $Z_{n,i}=(X_{n,i}-\mu_{n,i})/s_n$ with $W_{n,i}\sim N(0,\sigma_{n,i}^2/s_n^2)$ one at a time (telescoping sum), Taylor-expands $g$ to second order, and shows the remainder vanishes via the Lindeberg condition. <p> __Key idea:__ Smooth functions are locally quadratic. Matching $E[Z_{n,i}]=E[W_{n,i}]=0$ and $\operatorname{Var}[Z_{n,i}]=\operatorname{Var}[W_{n,i}]$ cancels the leading terms; the remainder is $o(1/k_n)$ per swap, so $k_n$ swaps vanish in the limit. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg replacement method / two stages of proof (smooth $g$ convergence then indicator extension) ::@:: __Stage 1 (smooth $g$):__ Show $\lim_{n\to\infty}|E[g(Z_n)]-E[g(Z)]|=0$ for $g\in C^2$ with $g''$ bounded and uniformly continuous, using telescoping replacement and Lindeberg's condition. <p> __Stage 2 (extension to indicators):__ Approximate $\mathbf{1}_{(-\infty,x]}$ by smooth sandwich functions $g_1\le\mathbf{1}_{(-\infty,x]}\le g_2$ to transfer convergence from smooth $g$ to CDFs, yielding convergence in distribution. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg replacement method / why it works (locally quadratic, moment matching, tail control) ::@:: Smooth functions are locally quadratic; matching first two moments cancels leading Taylor terms; Lindeberg condition eliminates the remainder. <p> __Intuition:__ Each swap error $=o(1/k_n)$, so $k_n$ swaps $\to0$. The Lindeberg condition ensures uniform tail control: no single $Z_{n,i}$ is "too large" too often. <p> __Key ingredients:__ (1) smooth $g$ expands to second order, (2) independence cancels first-order terms, (3) matching variances cancels second-order, (4) Lindeberg condition makes remainder vanish. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

## Lindeberg's condition <!-- check: ignore-line[header_style]: proper noun → Lindeberg is a proper noun -->

Define the standardised variables $Z_{n,i}=(X_{n,i}-\mu_{n,i})/s_n$. The __Lindeberg condition__ requires that for every $\varepsilon>0$, $$\lim_{n\to\infty}\frac{1}{s_n^2}\sum_{i=1}^{k_n}E\!\left[(X_{n,i}-\mu_{n,i})^2\, \mathbf{1}_{\{|X_{n,i}-\mu_{n,i}|>\varepsilon s_n\}}\right]=0,$$

or equivalently, $$\lim_{n\to\infty}\sum_{i=1}^{k_n}E\!\left[Z_{n,i}^2\,\mathbf{1}_{\{|Z_{n,i}|>\varepsilon\}}\right]=0,$$

where $\mathbf{1}_{\{\cdot\}}$ is the indicator function. In words: for any fixed $\varepsilon>0$, the total contribution of the __tails__ (the parts of each $X_{n,i}$ more than $\varepsilon s_n$ from its mean) to the overall variance $s_n^2$ becomes negligible as $n\to\infty$. No single variable contributes a disproportionate share of the total variance, and the tail mass beyond $\varepsilon s_n$ vanishes uniformly across all $i$. The threshold $\varepsilon s_n$ is scale-invariant: a variable counts as "large" only relative to the total standard deviation, not in absolute terms.

---

Flashcards for this section are as follows:

- Lindeberg condition / formal definition (two equivalent forms with $X_{n,i}$ and $Z_{n,i}$) ::@:: For every $\varepsilon>0$: $\lim_{n\to\infty}\frac1{s_n^2}\sum_{i=1}^{k_n}E[(X_{n,i}-\mu_{n,i})^2\mathbf{1}_{\{|X_{n,i}-\mu_{n,i}|>\varepsilon s_n\}}]=0$. <p> __Equivalent form (standardised):__ $\lim_{n\to\infty}\sum_{i=1}^{k_n}E[Z_{n,i}^2\mathbf{1}_{\{|Z_{n,i}|>\varepsilon\}}]=0$ where $Z_{n,i}=(X_{n,i}-\mu_{n,i})/s_n$. <p> __Interpretation:__ The tail variance beyond $\varepsilon s_n$ contributes negligibly to the total variance as $n\to\infty$. The threshold $\varepsilon s_n$ is scale-invariant — a variable counts as "large" only relative to the total standard deviation. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg condition / intuition (uniform asymptotic negligibility and role in the proof) ::@:: The condition ensures that the summands $X_{n,i}$ are _uniformly asymptotically negligible_: no single term dominates the sum, and the probability mass in the extreme tails contributes negligibly to the total variance. <p> __Why it's weak:__ It only requires finite variance, unlike moment bounds beyond the second. It is strictly weaker than identical distribution — distributions can have different shapes as long as the tail variance washes out. <p> __Role in the proof:__ The Lindeberg condition replaces the dominated convergence theorem (DCT) argument used in the i.i.d. case. For triangular arrays, there is no single variable to apply DCT to — Lindeberg's condition is exactly the right uniform tail-control assumption. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

## statement

__Theorem (Lindeberg CLT).__ Let $\{X_{n,i}\}$ be a triangular array of independent random variables satisfying

1. $E[X_{n,i}]=\mu_{n,i}$, $\operatorname{Var}[X_{n,i}]=\sigma_{n,i}^2<\infty$;
2. Lindeberg's condition above.

Set $$S_n=\sum_{i=1}^{k_n}X_{n,i},\qquad s_n^2=\operatorname{Var}[S_n]=\sum_{i=1}^{k_n}\sigma_{n,i}^2.$$

Then $$\frac{S_n-E[S_n]}{s_n}\xrightarrow{d} N(0,1),\qquad n\to\infty.$$

A proof via the Lindeberg replacement method is given in the next section. The theorem requires only Lindeberg's condition plus finite variances — no identical distribution, no higher moment assumptions, and no bound on $k_n$ beyond what $s_n^2$ implicitly controls.

---

Flashcards for this section are as follows:

- theorem statement (hypotheses $\implies$ $(S_n-E[S_n])/s_n\xrightarrow{d}N(0,1)$) <p> __Notation:__ $S_n=\sum_{i=1}^{k_n}X_{n,i}$, $s_n^2=\operatorname{Var}[S_n]=\sum_{i=1}^{k_n}\sigma_{n,i}^2$. ::@:: Let $\{X_{n,i}\}$ be independent within each row, $E[X_{n,i}]=\mu_{n,i}$, $\operatorname{Var}[X_{n,i}]=\sigma_{n,i}^2<\infty$. If Lindeberg's condition holds, then $(S_n-E[S_n])/s_n\xrightarrow{d}N(0,1)$. <p> The theorem requires only Lindeberg's condition plus finite variances — no identical distribution, no higher moment assumptions, and no bound on $k_n$ beyond what $s_n^2$ implicitly controls. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

## proof of the Lindeberg CLT

The proof proceeds in four steps: (1) a smooth test function lemma, (2) a telescoping replacement decomposition, (3) Taylor expansion of each replacement step, and (4) extension from smooth to indicator functions.

### smooth test functions for triangular arrays

The core of the proof is a lemma about smooth functions. Let $Z_{n,i}=(X_{n,i}-\mu_{n,i})/s_n$ be the standardised summands (so $E[Z_{n,i}]=0$, $\sum_i\operatorname{Var}[Z_{n,i}]=1$), and let $W_{n,i}\sim N(0,\sigma_{n,i}^2/s_n^2)$ be independent normals independent of the $X$ array, so that $\sum_{i=1}^{k_n}W_{n,i}\sim N(0,1)$. Define $Z_n=\sum_iZ_{n,i}$ (so $Z_n=(S_n-E[S_n])/s_n$) and let $Z\sim N(0,1)$. For any $g:\mathbb{R}\to\mathbb{R}$ twice differentiable with $g''$ uniformly continuous and bounded, $$\lim_{n\to\infty}\bigl|E[g(Z_n)]-E[g(Z)]\bigr|=0.$$

The idea is to compare $Z_n$ to a sum whose distribution is exactly normal. The replacement method constructs an explicit path from $Z_n$ to normality: a chain of $k_n$ intermediate sums that differ from the previous by exactly one variable. At each link, only the local behaviour of $g$ — over the tiny range of a single $Z_{n,i}$ — determines whether the swap changes the expectation. Since $\sum_iW_{n,i}\sim N(0,1)$, the target $E[g(Z)]$ equals $E[g(\sum_iW_{n,i})]$. The difference between $E[g(Z_n)]$ and $E[g(\sum_iW_{n,i})]$ is written as a telescoping sum over $k_n$ replacement steps, and each step is controlled by Taylor expansion whose remainder vanishes in the limit via the Lindeberg condition.

---

Flashcards for this section are as follows:

- Lindeberg smooth test function lemma / statement ($g\in C^2$, $g''$ bounded+uniformly continuous) <p> __Notation:__ $Z_{n,i}=(X_{n,i}-\mu_{n,i})/s_n$ (standardised summands, $E[Z_{n,i}]=0$, $\sum_i\operatorname{Var}[Z_{n,i}]=1$), $Z_n=\sum_{i=1}^{k_n}Z_{n,i}=(S_n-E[S_n])/s_n$, $Z\sim N(0,1)$. ::@:: For $g\in C^2$ with $g''$ bounded and uniformly continuous: $\lim_{n\to\infty}|E[g(Z_n)]-E[g(Z)]|=0$. <p> This lemma is the core of Lindeberg's method — it shows expectations of smooth functions converge to Gaussian expectations, which is then extended to indicator functions to prove convergence in distribution. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg smooth test function lemma / proof outline (four substeps) <p> __Notation:__ $Z_n=\sum_iZ_{n,i}$ (standardised row sum), $Z\sim N(0,1)$, $U_{n,i}=\sum_{j<i}W_{n,j}+\sum_{j>i}Z_{n,j}$ (leave-pair-out, independent of $Z_{n,i},W_{n,i}$), $V_{n,i}=g(U_{n,i}+Z_{n,i})-g(U_{n,i}+W_{n,i})$, $R_{n,i}$ = Taylor remainder. ::@:: <p> __Step 1 — Decompose:__ Introduce $W_{n,i}\sim N(0,\sigma_{n,i}^2/s_n^2)$ with $\sum_iW_{n,i}\sim N(0,1)$. The telescoping sum $\sum_iE[V_{n,i}] = E[g(Z_n)]-E[g(\sum_iW_{n,i})]$, and because $\sum_iW_{n,i}\sim Z$, this equals $E[g(Z_n)]-E[g(Z)]$. <p> __Step 2 — Taylor expand:__ Each $V_{n,i}=g(U_{n,i}+Z_{n,i})-g(U_{n,i}+W_{n,i})$ expanded to second order around $U_{n,i}$, giving linear, quadratic, and remainder terms. <p> __Step 3 — Cancel leading terms:__ First-order vanishes ($E[Z_{n,i}]=E[W_{n,i}]=0$ + independence of $U_{n,i}$). Second-order vanishes ($\operatorname{Var}[Z_{n,i}]=\operatorname{Var}[W_{n,i}]$ + independence). Only $E[R_{n,i}]$ survives. <p> __Step 4 — Control remainder:__ $\sum_iE[|R_{n,i}|]\to0$ via uniform continuity of $g''$ (bulk) + Lindeberg condition (tails). Hence $\lim_{n\to\infty}|E[g(Z_n)]-E[g(Z)]|=0$. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

#### i.i.d. case

<!-- Added from PDF: Lemma A.18 -->

The smooth test function lemma above is formulated for the general triangular-array setting. A simpler i.i.d.-only version — sometimes called the "replacement lemma" — makes the idea more transparent. For i.i.d. $X_1,\dots,X_n$ with $E[X_1]=0$ and $\operatorname{Var}[X_1]=\sigma^2<\infty$, let $Y_1,\dots,Y_n$ be i.i.d. $N(0,\sigma^2)$ independent of the $X$'s. For any bounded $C^3$ function $f$ with bounded derivatives, $$|E[f(Z + Y_i) - f(Z + X_i)]| \to 0,$$

where $Z$ is the sum of the remaining $n-1$ terms. A second-order Taylor expansion shows the error per replacement is $O(1/n)$; summing over $n$ replacements gives convergence to zero. The triangular-array proof above subsumes this as a special case while additionally handling non-identical distributions via the Lindeberg condition.

---

Flashcards for this section are as follows:

- i.i.d. replacement lemma / statement ::@:: For i.i.d. $X_1,\dots,X_n$ with $E[X_1]=0$, $\operatorname{Var}[X_1]=\sigma^2<\infty$, let $Y_1,\dots,Y_n$ be i.i.d. $N(0,\sigma^2)$ independent of the $X$'s. For any bounded $C^3$ function $f$ with bounded derivatives, $|E[f(Z+Y_i)-f(Z+X_i)]|\to0$, where $Z$ is the sum of the remaining $n-1$ terms. This is the i.i.d.-only "replacement lemma" — a simpler special case of the smooth test function lemma for triangular arrays. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- i.i.d. replacement lemma / error analysis ::@:: By second-order Taylor expansion of $f$ around $Z$, matching first two moments cancels the leading terms. The per-replacement error is $O(1/n)$; summing $n$ such errors yields total $\to0$, establishing the lemma. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- i.i.d. replacement lemma / relation to triangular-array version ::@:: The i.i.d. case is a special case of the smooth test function lemma. In the triangular-array proof, the Lindeberg condition replaces the DCT argument needed for i.i.d. summands, allowing non-identical distributions while subsuming the i.i.d. result. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

### step-by-step replacement

Write the difference $g(Z_n)-g(\sum_iW_{n,i})$ as a telescoping sum of $k_n$ terms, one for each variable that gets replaced: $$g(Z_n)-g\!\left({\textstyle\sum_i}W_{n,i}\right)=\sum_{i=1}^{k_n}V_{n,i},$$

where the $i$-th term is $$V_{n,i}=g\!\left(U_{n,i}+Z_{n,i}\right)-g\!\left(U_{n,i}+W_{n,i}\right),\qquad U_{n,i}=\sum_{j=1}^{i-1}W_{n,j}+\sum_{j=i+1}^{k_n}Z_{n,j}.$$

The variable $U_{n,i}$ collects all contributions from variables that are not being replaced at step $i$. Because $U_{n,i}$ is a function of all $Z_{n,j}$ and $W_{n,j}$ for $j\neq i$, it is independent of $Z_{n,i}$ and $W_{n,i}$. The telescoping structure turns one global convergence question into $k_n$ local comparisons, each isolating a single variable swap. At step $i$, only the distribution of $Z_{n,i}$ versus $W_{n,i}$ matters — everything else is frozen in $U_{n,i}$.

---

Flashcards for this section are as follows:

- Lindeberg telescoping sum / why $U_{n,i}$ is independent of $Z_{n,i},W_{n,i}$ <p> __Notation:__ $Z_{n,i}=(X_{n,i}-\mu_{n,i})/s_n$ (std'd summands), $W_{n,i}\sim N(0,\sigma_{n,i}^2/s_n^2)$ (matched normals), $U_{n,i}$ (leave-pair-out sum). ::@:: $U_{n,i}=\sum_{j=1}^{i-1}W_{n,j}+\sum_{j=i+1}^{k_n}Z_{n,j}$ collects all variables except those being replaced at step $i$ (the $i$-th pair). Since all $X_{n,i}$ (hence $Z_{n,i}$) and $W_{n,i}$ are independent across $i$, $U_{n,i}$ is independent of both $Z_{n,i}$ and $W_{n,i}$. <p> __Why this matters:__ The first-order Taylor term $E[(Z_{n,i}-W_{n,i})g'(U_{n,i})]$ factors as $E[Z_{n,i}-W_{n,i}]\,E[g'(U_{n,i})]$ by independence. Since $E[Z_{n,i}]=E[W_{n,i}]=0$, this term vanishes. Without independence, such factoring would be impossible and the proof would collapse. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg telescoping sum / decomposition $V_{n,i}$ and $U_{n,i}$ <p> __Notation:__ $Z_{n,i}$ (std'd summands), $W_{n,i}$ (matched normals), $U_{n,i}$ (leave-pair-out sum), $V_{n,i}=g(U_{n,i}+Z_{n,i})-g(U_{n,i}+W_{n,i})$ (per-replacement diff). ::@:: $g(Z_n)-g(\sum_iW_{n,i})=\sum_{i=1}^{k_n}V_{n,i}$ where $V_{n,i}=g(U_{n,i}+Z_{n,i})-g(U_{n,i}+W_{n,i})$ and $U_{n,i}=\sum_{j=1}^{i-1}W_{n,j}+\sum_{j=i+1}^{k_n}Z_{n,j}$. <p>$U_{n,i}$ is the "leave-pair-out" sum: all variables except the $i$-th pair $(Z_{n,i},W_{n,i})$. Each term $V_{n,i}$ compares the effect of $Z_{n,i}$ vs $W_{n,i}$ when added to the same base $U_{n,i}$. This turns one global convergence question into $k_n$ local comparisons. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg telescoping sum / error analysis (per-replacement vs cumulative) <p> __Notation:__ $V_{n,i}=g(U_{n,i}+Z_{n,i})-g(U_{n,i}+W_{n,i})$ (per-replacement diff), $R_{n,i}$ (Taylor remainder), $Z_{n,i}$ (std'd summands), $W_{n,i}$ (matched normals). ::@:: Taylor-expanding each $V_{n,i}$ to second order gives $k_n$ remainder terms $R_{n,i}$ whose expected sum vanishes as $n\to\infty$ via the Lindeberg condition. <p> __Typical magnitude:__ each $Z_{n,i}=O_p(1/\sqrt{k_n})$, so per-replacement error $|V_{n,i}|\approx O_p(1/k_n)$. Summing $k_n$ such errors: $\sum_i|E[V_{n,i}]|=\sum_i|E[R_{n,i}]|=o(1)$. The cumulative error stays controlled because each individual error is $o(1/k_n)$ in expectation. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

### Taylor expansion <!-- check: ignore-line[header_style]: proper noun → Taylor is a proper noun (Brook Taylor) -->

The Lindeberg proof uses a second-order Taylor expansion of the test function $g$ to compare each replacement pair $(Z_{n,i},W_{n,i})$. The key idea is to expand $g(U_{n,i}+h)$ for $h=Z_{n,i}$ and $h=W_{n,i}$, subtract, and bound the remainder.

__Taylor's theorem with Lagrange remainder (order $k=2$).__ For a twice-differentiable function $g$, $$g(a+h)=g(a)+g'(a)h+\frac12 g''(\xi)h^2,$$

where $\xi$ lies between $a$ and $a+h$. The remainder $\frac12 g''(\xi)h^2$ depends on $g''$ at an unknown intermediate point. Its size is controlled either by smoothness (when $h$ is small, $g''$ varies little) or by the rarity of large $h$ (the Lindeberg condition makes large $|Z_{n,i}|$ improbable).

__Step 1 — Expand $g(U_{n,i}+h)$ in centred form.__ Set $U=U_{n,i}$. For an increment $h$ (either $Z_{n,i}$ or $W_{n,i}$), write the Lagrange remainder in centred form by adding and subtracting $\frac12 g''(U)h^2$: $$g(U+h)=g(U)+g'(U)h+\frac12 g''(U)h^2+\frac12[g''(\xi)-g''(U)]h^2.$$

The centred form extracts the $\frac12 g''(U)h^2$ term into the explicit second-order part, leaving only the difference $g''(\xi)-g''(U)$ in the remainder. This separation is essential: the $g''(U)$ part will later cancel between $Z_{n,i}$ and $W_{n,i}$ (since $E[Z_{n,i}^2]=E[W_{n,i}^2]$), while $g''(\xi)-g''(U)$ is controlled by the modulus of continuity of $g''$ (Step 3).

__Step 2 — Apply both expansions and form $V_{n,i}$.__ Expand $g(U+Z_{n,i})$ and $g(U+W_{n,i})$ separately using Step 1: $$\begin{aligned} g(U+Z_{n,i})&=g(U)+g'(U)Z_{n,i}+\tfrac12 g''(U)Z_{n,i}^2+\tfrac12[g''(\xi_Z)-g''(U)]Z_{n,i}^2,\\[2pt] g(U+W_{n,i})&=g(U)+g'(U)W_{n,i}+\tfrac12 g''(U)W_{n,i}^2+\tfrac12[g''(\xi_W)-g''(U)]W_{n,i}^2. \end{aligned}$$

Subtract to form $V_{n,i}=g(U+Z_{n,i})-g(U+W_{n,i})$. The $g(U)$ term cancels, giving $$V_{n,i}=(Z_{n,i}-W_{n,i})\,g'(U)+\frac12(Z_{n,i}^2-W_{n,i}^2)\,g''(U)+R_{n,i},$$

where $R_{n,i}=R_{n,i}^{(Z)}-R_{n,i}^{(W)}$ collects the centred remainders: $$R_{n,i}^{(Z)}=\tfrac12[g''(\xi_Z)-g''(U)]Z_{n,i}^2,\qquad R_{n,i}^{(W)}=\tfrac12[g''(\xi_W)-g''(U)]W_{n,i}^2.$$

__Step 3 — Bound each centred remainder via the modulus of continuity.__ Since $g''$ is uniformly continuous, define $$\delta(h)=\sup_{|x-y|\le h}|g''(x)-g''(y)|.$$

Then $\delta(h)\to0$ as $h\downarrow0$, $\delta$ is non-decreasing, and $\delta(h)\le2\sup|g''|$ for all $h$. Because $\xi$ lies between $U$ and $U+h$, we have $|\xi-U|\le|h|$, hence $|g''(\xi)-g''(U)|\le\delta(|h|)$. Therefore $$|R_{n,i}^{(Z)}|\le\tfrac12 Z_{n,i}^2\,\delta(|Z_{n,i}|),\qquad |R_{n,i}^{(W)}|\le\tfrac12 W_{n,i}^2\,\delta(|W_{n,i}|).$$

__Step 4 — Combine both parts via the triangle inequality.__ $$|R_{n,i}| =|R_{n,i}^{(Z)}-R_{n,i}^{(W)}| \le|R_{n,i}^{(Z)}|+|R_{n,i}^{(W)}| \le\frac12 Z_{n,i}^2\,\delta(|Z_{n,i}|)+\frac12 W_{n,i}^2\,\delta(|W_{n,i}|).$$

This is the __Lindeberg remainder bound__. It splits naturally into two independent parts: the $Z_{n,i}$ term will be controlled by the Lindeberg condition, and the $W_{n,i}$ term by Gaussian tail bounds. The bound exploits a duality — when the increment is small, $g''$ varies little ($\delta$ is tiny); when it is large, the squared increment is penalised by a small tail probability.

---

Flashcards for this section are as follows:

- Taylor's theorem with Lagrange remainder / truncation at order $k$ ::@:: For $f$ $k$-times differentiable: $f(a+h)=\sum_{j=0}^{k-1}\frac{f^{(j)}(a)}{j!}h^j+\frac{f^{(k)}(\xi)}{k!}h^k$, where $\xi$ is between $a$ and $a+h$. <p> Larger $k$ gives smaller remainder (if derivatives bounded) but requires more smoothness. The remainder is controlled by the $k$-th derivative at an unknown point. <p> __In CLT proofs ($k=2$):__ Remainder $=\frac12 g''(\xi)h^2$. Uniform continuity of $g''$ controls it for small $h$; Lindeberg condition handles large $h$ via tail bounds. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Taylor expansion in Lindeberg's method / expanding $V_{n,i}$ via centred form <p> __Notation:__ $U=U_{n,i}$ (leave-pair-out sum), $Z=Z_{n,i},\;W=W_{n,i}$ (increments). ::@:: __Step 1 — Centre the Lagrange remainder:__ $\frac12 g''(\xi)h^2 = \frac12 g''(U)h^2 + \frac12[g''(\xi)-g''(U)]h^2$. The $\frac12 g''(U)h^2$ part joins the explicit second-order term. <p> __Step 2 — Expand $g(U+Z)$ and $g(U+W)$:__ $g(U+Z)=g(U)+g'(U)Z+\frac12 g''(U)Z^2+\frac12[g''(\xi_Z)-g''(U)]Z^2$, and analogously for $W$. <p> __Step 3 — Subtract to form $V_{n,i}$:__ $V_{n,i}=(Z-W)g'(U)+\frac12(Z^2-W^2)g''(U)+R_{n,i}$ where $R_{n,i}^{(Z)}=\frac12[g''(\xi_Z)-g''(U)]Z^2$ and $R_{n,i}^{(W)}=\frac12[g''(\xi_W)-g''(U)]W^2$. <p> __Why centred form helps:__ The $g''(U)$ terms cancel in expectation ($E[Z^2]=E[W^2]$), leaving only $R_{n,i}$. Without centring, the two remainders $\frac12 g''(\xi_Z)Z^2-\frac12 g''(\xi_W)W^2$ would not simplify because $\xi_Z\neq\xi_W$. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg remainder bound / statement ::@:: $|R_{n,i}|\le\frac12 Z_{n,i}^2\delta(|Z_{n,i}|)+\frac12 W_{n,i}^2\delta(|W_{n,i}|)$. <p> The bound decouples into two parts: $Z_{n,i}$ term (controlled by Lindeberg condition) and $W_{n,i}$ term (controlled by Gaussian tail bounds). Each is $(\text{squared increment})\times(\text{smoothness penalty})/2$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg remainder bound / derivation and properties ::@:: __Step 1 — Apply centred expansion:__ $g(U+h)=g(U)+g'(U)h+\frac12 g''(U)h^2+\frac12[g''(\xi)-g''(U)]h^2$, with $|g''(\xi)-g''(U)|\le\delta(|h|)$. <p> __Step 2 — Properties of $\delta$:__ non-decreasing, $\delta(h)\to0$ as $h\to0$ (uniform continuity of $g''$), $\delta(h)\le2\sup|g''|$ for all $h$. <p> __Step 3 — Write $R_{n,i}^{(Z)}$ and $R_{n,i}^{(W)}$:__ $R_{n,i}^{(Z)}=\frac12[g''(\xi_Z)-g''(U)]Z_{n,i}^2$, $R_{n,i}^{(W)}=\frac12[g''(\xi_W)-g''(U)]W_{n,i}^2$. Bound each: $|R_{n,i}^{(Z)}|\le\frac12 Z_{n,i}^2\delta(|Z_{n,i}|)$, $|R_{n,i}^{(W)}|\le\frac12 W_{n,i}^2\delta(|W_{n,i}|)$. <p> __Step 4 — Triangle inequality:__ $|R_{n,i}|=|R_{n,i}^{(Z)}-R_{n,i}^{(W)}|\le\frac12 Z_{n,i}^2\delta(|Z_{n,i}|)+\frac12 W_{n,i}^2\delta(|W_{n,i}|)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

### vanishing expectation via Lindeberg's condition

__Step 1 — Cancel the leading terms via moment matching.__

Take expectations of $V_{n,i}=g(U_{n,i}+Z_{n,i})-g(U_{n,i}+W_{n,i})$ using the expansion from the Taylor expansion section: $$E[V_{n,i}] = E[(Z_{n,i}-W_{n,i})\,g'(U_{n,i})] + \frac12 E[(Z_{n,i}^2-W_{n,i}^2)\,g''(U_{n,i})] + E[R_{n,i}].$$

Since $U_{n,i}$ is independent of $Z_{n,i}$ and $W_{n,i}$, both expectations factor: $$\begin{aligned} E[(Z_{n,i}-W_{n,i})\,g'(U_{n,i})] &= E[Z_{n,i}-W_{n,i}]\,E[g'(U_{n,i})],\\[2pt] E[(Z_{n,i}^2-W_{n,i}^2)\,g''(U_{n,i})] &= E[Z_{n,i}^2-W_{n,i}^2]\,E[g''(U_{n,i})]. \end{aligned}$$

Matching first moments: $E[Z_{n,i}] = E[W_{n,i}] = 0$, so the first term vanishes. Matching second moments: $\operatorname{Var}[Z_{n,i}] = \operatorname{Var}[W_{n,i}]$ implies $E[Z_{n,i}^2] = E[W_{n,i}^2]$, so the second term vanishes. Hence $$E[V_{n,i}] = E[R_{n,i}],$$

where $R_{n,i} = R_{n,i}^{(Z)} - R_{n,i}^{(W)}$ is the combined centred remainder from the Taylor expansion. Only the remainder survives in expectation — both explicit terms are killed by moment matching and independence.

__Step 2 — Bound the $Z$ remainder via a two-regime split.__

From the Lindeberg remainder bound, $|R_{n,i}^{(Z)}| \le \frac12 Z_{n,i}^2\,\delta(|Z_{n,i}|)$. Split the expectation into a bulk region ($|Z_{n,i}| \le \varepsilon$) and a tail region ($|Z_{n,i}| > \varepsilon$): $$\begin{aligned} E[Z_{n,i}^2\,\delta(|Z_{n,i}|)] &= E[Z_{n,i}^2\,\delta(|Z_{n,i}|)\,\mathbf{1}_{\{|Z_{n,i}|\le\varepsilon\}}] + E[Z_{n,i}^2\,\delta(|Z_{n,i}|)\,\mathbf{1}_{\{|Z_{n,i}|>\varepsilon\}}] \\[2pt] &\le \delta(\varepsilon)\,E[Z_{n,i}^2] + C\,E[Z_{n,i}^2\,\mathbf{1}_{\{|Z_{n,i}|>\varepsilon\}}], \end{aligned}$$

where $C = 2\sup|g''|$ bounds $\delta$ globally ($\delta(h) \le 2\sup|g''|$ for all $h$). The bulk bound uses $\delta(|Z_{n,i}|) \le \delta(\varepsilon)$ because $\delta$ is non-decreasing and $|Z_{n,i}| \le \varepsilon$. The tail bound uses $\delta(|Z_{n,i}|) \le C$.

Summing over $i = 1,\dots,k_n$ and using $\sum_i E[Z_{n,i}^2] = \sum_i \sigma_{n,i}^2/s_n^2 = 1$: $$\sum_{i=1}^{k_n} E[Z_{n,i}^2\,\delta(|Z_{n,i}|)] \le \delta(\varepsilon) + C\sum_{i=1}^{k_n} E[Z_{n,i}^2\,\mathbf{1}_{\{|Z_{n,i}|>\varepsilon\}}]. \tag{1}$$

__Step 3 — Bound the $W$ remainder via the Feller condition and Gaussian tails.__

Similarly, $|R_{n,i}^{(W)}| \le \frac12 W_{n,i}^2\,\delta(|W_{n,i}|)$. The same two-regime split gives $$\sum_{i=1}^{k_n} E[W_{n,i}^2\,\delta(|W_{n,i}|)] \le \delta(\varepsilon) + C\sum_{i=1}^{k_n} E[W_{n,i}^2\,\mathbf{1}_{\{|W_{n,i}|>\varepsilon\}}]. \tag{2}$$

The tail term for $W_{n,i}\sim N(0,\sigma_{n,i}^2/s_n^2)$ is controlled by the Feller condition $\max_i \sigma_{n,i}/s_n \to 0$, which follows from Lindeberg's condition (if some $\sigma_{n,i}/s_n$ stayed bounded away from $0$, that term would contribute enough second-moment mass to violate the Lindeberg tail-sum bound). Write $W_{n,i} = (\sigma_{n,i}/s_n)\,\eta_{n,i}$ with $\eta_{n,i}\sim N(0,1)$ i.i.d.: $$\begin{aligned} E[W_{n,i}^2\,\mathbf{1}_{\{|W_{n,i}|>\varepsilon\}}] &= \frac{\sigma_{n,i}^2}{s_n^2}\,E\!\bigl[\eta_{n,i}^2\,\mathbf{1}_{\{|\eta_{n,i}| > \varepsilon s_n/\sigma_{n,i}\}}\bigr] \\[2pt] &\le \frac{\sigma_{n,i}^2}{s_n^2}\,E\!\bigl[\eta^2\,\mathbf{1}_{\{|\eta| > \varepsilon s_n/\sigma_{n,i}\}}\bigr], \end{aligned}$$

where $\eta\sim N(0,1)$. Since $\max_i \sigma_{n,i}/s_n \to 0$, for any $M>0$, once $n$ is large enough that $\max_i \sigma_{n,i}/s_n \le 1/M$, we have $\varepsilon s_n/\sigma_{n,i} \ge \varepsilon M$ for all $i$, hence $$E\!\bigl[\eta^2\,\mathbf{1}_{\{|\eta| > \varepsilon s_n/\sigma_{n,i}\}}\bigr] \le E[\eta^2\,\mathbf{1}_{\{|\eta| > \varepsilon M\}}].$$

Summing over $i$ and using $\sum_i \sigma_{n,i}^2/s_n^2 = 1$: $$\sum_{i=1}^{k_n} E[W_{n,i}^2\,\mathbf{1}_{\{|W_{n,i}|>\varepsilon\}}] \le E[\eta^2\,\mathbf{1}_{\{|\eta| > \varepsilon M\}}].$$

The RHS is independent of $n$. Sending $M\to\infty$ (which is forced by $n\to\infty$ because $\max_i \sigma_{n,i}/s_n \to 0$), $E[\eta^2\,\mathbf{1}_{\{|\eta| > \varepsilon M\}}] \to 0$ by DCT (since $E[\eta^2]<\infty$). Thus $$\lim_{n\to\infty} \sum_{i=1}^{k_n} E[W_{n,i}^2\,\mathbf{1}_{\{|W_{n,i}|>\varepsilon\}}] = 0 \quad\text{for each }\varepsilon>0. \tag{3}$$

__Step 4 — Combine the bounds and take limits.__

From (1)–(3) and the triangle inequality $|R_{n,i}| \le |R_{n,i}^{(Z)}| + |R_{n,i}^{(W)}|$: $$\begin{aligned} \sum_{i=1}^{k_n} E[|R_{n,i}|] &\le \frac12\Bigl(\sum_i E[Z_{n,i}^2\delta(|Z_{n,i}|)] + \sum_i E[W_{n,i}^2\delta(|W_{n,i}|)]\Bigr) \\[2pt] &\le \delta(\varepsilon) + \frac{C}{2}\Bigl(\underbrace{\sum_i E[Z_{n,i}^2\mathbf{1}_{\{|Z_{n,i}|>\varepsilon\}}]}_{(\text{A})} + \underbrace{\sum_i E[W_{n,i}^2\mathbf{1}_{\{|W_{n,i}|>\varepsilon\}}]}_{(\text{B})}\Bigr). \end{aligned}$$

Take $n\to\infty$ first. Lindeberg's condition gives $(\text{A})\to0$, and (3) gives $(\text{B})\to0$, so for each $\varepsilon>0$: $$\limsup_{n\to\infty} \sum_{i=1}^{k_n} E[|R_{n,i}|] \le \delta(\varepsilon).$$

Now send $\varepsilon\downarrow0$. Uniform continuity of $g''$ implies $\lim_{\varepsilon\downarrow0} \delta(\varepsilon) = 0$, hence $$\lim_{n\to\infty} \sum_{i=1}^{k_n} E[|R_{n,i}|] = 0.$$

__Step 5 — Conclude the smooth test function lemma.__

Since $E[V_{n,i}] = E[R_{n,i}]$ (Step 1) and $g(Z_n) - g(\sum_i W_{n,i}) = \sum_{i=1}^{k_n} V_{n,i}$ (telescoping sum), $$\begin{aligned} |E[g(Z_n)] - E[g(Z)]| &= \Bigl|\,E\!\Bigl[g\Bigl(\sum_i Z_{n,i}\Bigr) - g\Bigl(\sum_i W_{n,i}\Bigr)\Bigr]\,\Bigr| \\[2pt] &= \Bigl|\,\sum_{i=1}^{k_n} E[V_{n,i}]\,\Bigr| \\[2pt] &= \Bigl|\,\sum_{i=1}^{k_n} E[R_{n,i}]\,\Bigr| \\[2pt] &\le \sum_{i=1}^{k_n} E[|R_{n,i}|] \;\longrightarrow\; 0 \quad\text{as } n\to\infty. \end{aligned}$$

Therefore $\lim_{n\to\infty} |E[g(Z_n)] - E[g(Z)]| = 0$, completing the smooth test function lemma.

__Why the Lindeberg condition is needed here.__ In the i.i.d. case, $Z_{n,i} = X_i/\sqrt{n}$ and the tail bound $E[X_1^2\mathbf{1}_{\{|X_1| > \varepsilon\sqrt{n}\}}] \to 0$ follows from $E[X_1^2] < \infty$ by the dominated convergence theorem (DCT). For triangular arrays, there is no single random variable to apply DCT to — the Lindeberg condition is exactly the right uniform tail-control assumption that replaces the DCT argument.

---

Flashcards for this section are as follows:

- Lindeberg vanishing expectation / Step 1 — leading terms cancel via $E[Z]=0$, $E[Z^2]=E[W^2]$, independence ::@:: __Set-up:__ $V_{n,i}=(Z_{n,i}-W_{n,i})g'(U_{n,i})+\frac12(Z_{n,i}^2-W_{n,i}^2)g''(U_{n,i})+R_{n,i}$. <p> __Take $E$:__ $E[V]=E[(Z-W)g'(U)]+\frac12 E[(Z^2-W^2)g''(U)]+E[R]$. <p> __Factor by independence:__ $U_{n,i}\perp(Z_{n,i},W_{n,i})$, so $E[(Z-W)g'(U)]=E[Z-W]E[g'(U)]$, $E[(Z^2-W^2)g''(U)]=E[Z^2-W^2]E[g''(U)]$. <p> __First term $=0$:__ $E[Z]=E[W]=0\implies E[Z-W]=0$. <p> __Second term $=0$:__ $\operatorname{Var}[Z]=\operatorname{Var}[W]\implies E[Z^2]=E[W^2]\implies E[Z^2-W^2]=0$. <p> __Conclusion:__ $E[V_{n,i}]=E[R_{n,i}]$ — only remainder survives in expectation. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg two-regime bound / Step 2 — controlling $\sum_iE[Z_{n,i}^2\delta(|Z_{n,i}|)]$ via truncation ::@:: __Target:__ Bound $\sum_iE[Z_{n,i}^2\delta(|Z_{n,i}|)]$. $C=2\sup|g''|$ is a global bound on $\delta$. <p> __Split $|Z|\le\varepsilon$ (bulk) vs $>\varepsilon$ (tails):__ $E[Z^2\delta(|Z|)]=E[Z^2\delta(|Z|)\mathbf{1}_{\{|Z|\le\varepsilon\}}]+E[Z^2\delta(|Z|)\mathbf{1}_{\{|Z|>\varepsilon\}}]$. <p> __Bulk:__ $\delta(|Z|)\le\delta(\varepsilon)$ ($\delta$ non-decreasing). $\le\delta(\varepsilon)E[Z^2]$. <p> __Tails:__ $\delta(|Z|)\le C$. $\le C\,E[Z^2\mathbf{1}_{\{|Z|>\varepsilon\}}]$. <p> __Sum over $i$:__ $\sum_iE[Z_{n,i}^2\delta(|Z_{n,i}|)]\le\delta(\varepsilon)+C\sum_iE[Z_{n,i}^2\mathbf{1}_{\{|Z_{n,i}|>\varepsilon\}}]$. <p> The bulk term $=O(\delta(\varepsilon))$ uniformly in $n$ (because $\sum_iE[Z_{n,i}^2]=1$); the tail term $\to0$ as $n\to\infty$ by Lindeberg. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg $W$ remainder bound / Step 3 — Gaussian tails and Feller condition ($\max_i\sigma_{n,i}/s_n\to0$) ::@:: __Set-up:__ $|R_{n,i}^{(W)}|\le\frac12 W_{n,i}^2\delta(|W_{n,i}|)$, $W_{n,i}\sim N(0,\sigma_{n,i}^2/s_n^2)$. Two-regime split gives $\sum_iE[W^2\delta(|W|)]\le\delta(\varepsilon)+C\sum_iE[W^2\mathbf{1}_{\{|W|>\varepsilon\}}]$. <p> __Rewrite tail term:__ $W_{n,i}=(\sigma_{n,i}/s_n)\eta_{n,i}$, $\eta_{n,i}\sim N(0,1)$. Then $E[W_{n,i}^2\mathbf{1}_{\{|W_{n,i}|>\varepsilon\}}]=(\sigma_{n,i}^2/s_n^2)E[\eta^2\mathbf{1}_{\{|\eta|>\varepsilon s_n/\sigma_{n,i}\}}]$. <p> __Feller condition:__ Lindeberg $\implies\max_i\sigma_{n,i}/s_n\to0$ (if $\sigma_{n,i}/s_n\ge c>0$, then $E[Z_{n,i}^2\mathbf{1}_{\{|Z_{n,i}|>c/2\}}]\ge(\sigma_{n,i}/s_n)^2-(c/2)^2\ge3c^2/4>0$ (tail $E\ge\mathrm{variance}-\mathrm{threshold}^2$ since $Z^2\mathbf{1}_{\{|Z|\le a\}}\le a^2$), violating Lindeberg). For any $M>0$, large $n$ gives $\max_i\sigma_{n,i}/s_n\le1/M$, so $\varepsilon s_n/\sigma_{n,i}\ge\varepsilon M$ uniformly in $i$. <p> __Bound:__ $\sum_iE[W_{n,i}^2\mathbf{1}_{\{|W_{n,i}|>\varepsilon\}}]\le\sum_i(\sigma_{n,i}^2/s_n^2)E[\eta^2\mathbf{1}_{\{|\eta|>\varepsilon M\}}]=E[\eta^2\mathbf{1}_{\{|\eta|>\varepsilon M\}}]\to0$ as $M\to\infty$ (dominated convergence theorem, $E[\eta^2]<\infty$). <p> __Conclusion:__ For each $\varepsilon>0$, $\sum_iE[W_{n,i}^2\mathbf{1}_{\{|W_{n,i}|>\varepsilon\}}]\to0$ as $n\to\infty$. <!--SR:!fsrs,2026-07-03T00:06:00.000Z,0,1.2931,5.11217071,1,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg vanishing expectation / Steps 4-5 — double limit and smooth lemma conclusion ::@:: __Step 4 — Combine:__ $|R_{n,i}|\le|R_{n,i}^{(Z)}|+|R_{n,i}^{(W)}|$. Then $\sum_iE[|R_{n,i}|]\le\frac12(\sum_iE[Z^2\delta(|Z|)]+\sum_iE[W^2\delta(|W|)])\le\delta(\varepsilon)+\frac{C}{2}(\text{A}+\text{B})$ where $\text{A}=\sum_iE[Z^2\mathbf{1}_{\{|Z|>\varepsilon\}}]$, $\text{B}=\sum_iE[W^2\mathbf{1}_{\{|W|>\varepsilon\}}]$. <p> __First limit $n\to\infty$:__ Lindeberg $\implies\text{A}\to0$; Gaussian tail $\implies\text{B}\to0$. So $\limsup_{n\to\infty}\sum_iE[|R_{n,i}|]\le\delta(\varepsilon)$. <p> __Second limit $\varepsilon\downarrow0$:__ Uniform continuity $\implies\delta(\varepsilon)\to0$. Hence $\lim_{n\to\infty}\sum_iE[|R_{n,i}|]=0$. <p> __Step 5 — Conclude:__ $E[V_{n,i}]=E[R_{n,i}]$, $\sum_iV_{n,i}=g(Z_n)-g(\sum_i W_{n,i})$, and $\sum_i W_{n,i}\sim N(0,1)=:Z$. So $|E[g(Z_n)]-E[g(Z)]|\le\sum_iE[|R_{n,i}|]\to0$ — the smooth test function lemma. <p> __Lindeberg's role:__ Replaces the dominated convergence theorem (DCT) tail bound used in the i.i.d. case. No single variable to apply DCT to in a triangular array. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

### extension to indicator functions

The smooth test function lemma is not directly about convergence in distribution — that requires convergence of the CDF at every continuity point. To bridge the gap, approximate indicators by smooth functions.

Fix $x\in\mathbb{R}$ and $\varepsilon>0$. Choose two smooth functions $g_1,g_2$ (in $C^2$ with $g''$ bounded and uniformly continuous, so the smooth lemma applies) such that $$g_1(t)\le 1_{(-\infty,x]}(t)\le g_2(t)\quad\text{for all }t,\qquad \int_{-\infty}^\infty(g_2(t)-g_1(t))\,dt\le\varepsilon.$$

Geometrically, smooth the jump at $x$ over $[x-\varepsilon,x+\varepsilon]$; $g_2-g_1$ is supported there, has height at most $1$, and its integral is at most $2\varepsilon$ (the constant is absorbed by the arbitrary $\varepsilon$ at the end).

From the sandwich property, for every $n$, $$E[g_1(Z_n)]\le F_{Z_n}(x)\le E[g_2(Z_n)],\qquad E[g_1(Z)]\le\Phi(x)\le E[g_2(Z)],$$

where $F_{Z_n}$ is the CDF of $Z_n$ and $\Phi$ that of $Z\sim N(0,1)$. Combining the two sandwich chains via the triangle inequality gives $$|F_{Z_n}(x)-\Phi(x)| \le \max_{k=1,2}|E[g_k(Z_n)]-E[g_k(Z)]| + E[g_2(Z)-g_1(Z)].$$

(From $F_{Z_n}\le E[g_2(Z_n)]$ and $E[g_1(Z)]\le\Phi(x)$, we have $F_{Z_n}-\Phi\le E[g_2(Z_n)]-E[g_1(Z)] = (E[g_2(Z_n)]-E[g_2(Z)]) + E[g_2(Z)-g_1(Z)]$; the lower bound is analogous, leading to the expression above.)

The smooth lemma applies to $g_1,g_2$, so $\lim_{n\to\infty}E[g_k(Z_n)]=E[g_k(Z)]$ for $k=1,2$, and the first term vanishes as $n\to\infty$. Hence $$\limsup_{n\to\infty}|F_{Z_n}(x)-\Phi(x)|\le E[g_2(Z)-g_1(Z)].$$

Now bound the remaining expectation using the standard Gaussian density $\phi(t)=e^{-t^2/2}/\sqrt{2\pi}$: $$E[g_2(Z)-g_1(Z)] = \int_{-\infty}^\infty (g_2(t)-g_1(t))\,\phi(t)\,dt \le \phi(0)\int_{-\infty}^\infty (g_2(t)-g_1(t))\,dt \le \phi(0)\,\varepsilon,$$

since $\phi(t)\le\phi(0)=1/\sqrt{2\pi}$ (the Gaussian density attains its maximum at zero) and $\int(g_2-g_1)\le\varepsilon$ by construction.

Therefore, for every $x\in\mathbb{R}$ and $\varepsilon>0$, $$\limsup_{n\to\infty}|F_{Z_n}(x)-\Phi(x)|\le\phi(0)\varepsilon.$$

Since $\varepsilon>0$ is arbitrary, the limsup is zero, giving $F_{Z_n}(x)\to\Phi(x)$ for every $x$ — convergence in distribution.

---

Flashcards for this section are as follows:

- Extending smooth lemma to indicators / smooth sandwich by $g_1,g_2$ ::@:: __Step 1 — Construct:__ Fix $x$, $\varepsilon>0$. Choose $g_1,g_2\in C^2$ (with $g''$ bounded+uniformly continuous) s.t. $g_1\le 1_{(-\infty,x]}\le g_2$ and $\int(g_2-g_1)\le\varepsilon$. Smooth the jump at $x$ over $[x-\varepsilon,x+\varepsilon]$; $g_2-g_1$ supported there, height $\le1$, integral $\le2\varepsilon$. <p> __Step 2 — Sandwich CDFs:__ $E[g_1(Z_n)]\le F_{Z_n}(x)\le E[g_2(Z_n)]$ and $E[g_1(Z)]\le\Phi(x)\le E[g_2(Z)]$. Both CDFs are pinned by the same pair of smooth functions. <p> __Step 3 — Smooth lemma:__ $\lim_{n\to\infty}E[g_{1,2}(Z_n)]=E[g_{1,2}(Z)]$ by the smooth test function lemma. So the sandwich endpoints converge to their Gaussian counterparts. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Extending smooth lemma to indicators / bounding $|F_{Z_n}(x)-\Phi(x)|$ via $\phi(0)$ ::@:: __Step 1 — Combine sandwiches:__ $|F_{Z_n}(x)-\Phi(x)|\le\max_k|E[g_k(Z_n)]-E[g_k(Z)]|+E[g_2(Z)-g_1(Z)]$ (by $F_{Z_n}\le E[g_2(Z_n)]$, $\Phi\ge E[g_1(Z)]$, triangle inequality). <p> __Step 2 — Smooth lemma:__ $\max_k|E[g_k(Z_n)]-E[g_k(Z)]|\to0$, so $\limsup_{n\to\infty}|F_{Z_n}(x)-\Phi(x)|\le E[g_2(Z)-g_1(Z)]$. <p> __Step 3 — Density bound:__ $E[g_2-g_1]=\int(g_2-g_1)\phi(t)dt\le\phi(0)\int(g_2-g_1)\le\phi(0)\varepsilon$ because $\phi(t)\le\phi(0)=1/\sqrt{2\pi}$. <p> __Step 4 — Arbitrary $\varepsilon$:__ $\varepsilon>0$ arbitrary $\implies\limsup=0$, so $F_{Z_n}(x)\to\Phi(x)$ for every $x$ — convergence in distribution. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Extending smooth lemma to indicators / full inequality chain (construction → convergence) ::@:: (1) Construct $g_1,g_2$: $g_1\le 1_{(-\infty,x]}\le g_2$, $\int(g_2-g_1)\le\varepsilon$. (2) Sandwich both CDFs: $E[g_1(Z_n)]\le F_{Z_n}(x)\le E[g_2(Z_n)]$, same for $\Phi$. (3) Triangle: $|F_{Z_n}-\Phi|\le\max_k|E[g_k(Z_n)]-E[g_k(Z)]|+E[g_2-g_1]$. (4) Smooth lemma $\to0$ for first term. (5) Density bound $E[g_2-g_1]\le\phi(0)\varepsilon$. (6) $\varepsilon\downarrow0\implies\limsup=0$, so $F_{Z_n}(x)\to\Phi(x)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

## Lindeberg–Feller CLT <!-- check: ignore-line[header_style]: proper noun → Lindeberg–Feller is a compound proper noun -->

The Lindeberg–Feller theorem sharpens the result by also addressing necessity: under a mild regularity condition (the Feller condition), Lindeberg's condition is not only sufficient but also necessary for convergence to normality.

__Theorem (Lindeberg–Feller CLT).__ Let $\{X_{n,i}\}$ be a triangular array of independent random variables with $E[X_{n,i}]=0$ (w.l.o.g., by centering) and $\operatorname{Var}[X_{n,i}]=\sigma_{n,i}^2<\infty$. Define $s_n^2=\sum_i\sigma_{n,i}^2$. If $$\text{(Feller)}\qquad \lim_{n\to\infty}\max_{1\le i\le k_n}\frac{\sigma_{n,i}}{s_n}=0,$$

then the following are equivalent:

- $(S_n)/s_n\xrightarrow{d} N(0,1)$;
- Lindeberg's condition holds.

The Feller condition $\max_i\sigma_{n,i}/s_n\to0$ says that no single term contributes asymptotically to the total variance — each individual variance is $o(s_n^2)$. This is a natural regularity condition: if one term dominated the variance, the sum would be essentially that term, which cannot be normal unless that term itself is approximately normal. The Feller condition rules out this degenerate scenario and forces the CLT to arise from the collective contribution of many small terms.

_Proof of necessity (sketch)._ Under the Feller condition, if $S_n/s_n\xrightarrow{d}N(0,1)$ but Lindeberg fails, then there exists $\varepsilon>0$ and a subsequence along which $\sum_iE[Z_{n,i}^2\mathbf{1}_{\{|Z_{n,i}|>\varepsilon\}}]\not\to0$. The Feller condition forces the individual terms to be uniformly small, so non-vanishing of this sum implies many summands carry mass in the $\varepsilon$-tails. A coupling argument then shows the limiting distribution of $S_n/s_n$ would have a larger variance than 1 — contradicting $N(0,1)$. Formalising this uses a truncation argument and the replacement method in reverse.

---

Flashcards for this section are as follows:

- Lindeberg-Feller theorem / equivalence result ($S_n/s_n\xrightarrow{d}N(0,1)$ $\iff$ Lindeberg, under Feller) ::@:: For independent zero-mean $X_{n,i}$ with variances $\sigma_{n,i}^2$, $s_n^2=\sum\sigma_{n,i}^2$. If the Feller condition $\max_i\sigma_{n,i}/s_n\to0$ holds, then $(S_n)/s_n\xrightarrow{d}N(0,1)$ __iff__ Lindeberg's condition holds. <p> This is the sharpest CLT for independent summands: under mild regularity (no single term dominates), Lindeberg's condition is both sufficient and necessary. <p> __Feller condition:__ $\lim_{n\to\infty}\max_{i}\sigma_{n,i}/s_n=0$ ensures no single variance dominates — otherwise the sum could be essentially one term. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Feller condition / $\max_i\sigma_{n,i}/s_n\to0$ and why it's needed ::@:: $\lim_{n\to\infty}\max_{1\le i\le k_n}\sigma_{n,i}/s_n=0$. <p> __Purpose:__ Ensures the sum is built from a large number of individually negligible terms — no single variable contributes an asymptotically positive fraction of the total variance. <p> __Without it:__ Convergence could occur for pathological arrangements where Lindeberg's condition fails because one dominant term happens to be approximately normal. The Feller condition rules out this degenerate scenario and forces the CLT to arise from the collective contribution of many small terms. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg-Feller necessity / why Lindeberg must hold for $N(0,1)$ convergence (proof idea) ::@:: Under the Feller condition, if $S_n/s_n\xrightarrow{d}N(0,1)$ then Lindeberg's condition must hold. <p> __Proof idea (reverse replacement):__ If Lindeberg fails, non-vanishing tail variance would force the limiting distribution to have variance exceeding 1, contradicting $N(0,1)$. A coupling argument shows the limiting distribution would have variance $>1$ because the tail mass contributes extra variance that the normal replacement cannot absorb. <p> __Key insight:__ The replacement method is reversible. If some tail mass does not vanish, the smoothing argument produces a limiting variance $>1$, contradicting the $N(0,1)$ target. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

## relation to Lyapunov's condition

Lyapunov's condition is a stronger, easier-to-verify condition that implies Lindeberg's. It requires that for some $\delta>0$, $$\lim_{n\to\infty}\frac{1}{s_n^{2+\delta}}\sum_{i=1}^{k_n} E\!\left[|X_{n,i}-\mu_{n,i}|^{2+\delta}\right]=0.$$

On $\{|X_{n,i}-\mu_{n,i}|>\varepsilon s_n\}$, $|X_{n,i}-\mu_{n,i}|^\delta>(\varepsilon s_n)^\delta$, so $|X_{n,i}-\mu_{n,i}|^{-\delta}<(\varepsilon s_n)^{-\delta}$.

Rewriting $(X_{n,i}-\mu_{n,i})^2=|X_{n,i}-\mu_{n,i}|^{2+\delta}|X_{n,i}-\mu_{n,i}|^{-\delta}$ gives the pointwise bound $$(X_{n,i}-\mu_{n,i})^2\mathbf{1}_{\{|X_{n,i}-\mu_{n,i}|>\varepsilon s_n\}} \le |X_{n,i}-\mu_{n,i}|^{2+\delta}\,(\varepsilon s_n)^{-\delta}.$$

Taking expectations, $$E\!\bigl[(X_{n,i}-\mu_{n,i})^2\mathbf{1}_{\{|X_{n,i}-\mu_{n,i}|>\varepsilon s_n\}}\bigr] \le (\varepsilon s_n)^{-\delta}\, E\!\bigl[|X_{n,i}-\mu_{n,i}|^{2+\delta}\bigr].$$

Summing over $i$ and dividing by $s_n^2$, $$\frac{1}{s_n^2}\sum_{i=1}^{k_n}E\!\bigl[(X_{n,i}-\mu_{n,i})^2\mathbf{1}_{\{|X_{n,i}-\mu_{n,i}|>\varepsilon s_n\}}\bigr] \le\frac{1}{\varepsilon^\delta}\cdot\frac{1}{s_n^{2+\delta}}\sum_{i=1}^{k_n}E\!\bigl[|X_{n,i}-\mu_{n,i}|^{2+\delta}\bigr]\to0,$$

where the limit follows from Lyapunov's condition. Conversely, Lindeberg does __not__ imply Lyapunov; there exist sequences satisfying Lindeberg but having infinite $(2+\delta)$-moments (heavy-tailed distributions with finite variance).

---

Flashcards for this section are as follows:

- Lyapunov condition / definition ($(2+\delta)$-moments) and implication ($\implies$ Lindeberg) ::@:: $\lim_{n\to\infty}\frac1{s_n^{2+\delta}}\sum_iE[|X_{n,i}-\mu_{n,i}|^{2+\delta}]=0$ for some $\delta>0$. <p> __Lyapunov $\implies$ Lindeberg:__ On $\{|X-\mu|>\varepsilon s_n\}$, $(X-\mu)^2=|X-\mu|^{2+\delta}|X-\mu|^{-\delta}$, and $|X-\mu|^\delta>(\varepsilon s_n)^\delta\implies|X-\mu|^{-\delta}<(\varepsilon s_n)^{-\delta}$, so $(X-\mu)^2\mathbf{1}_{\{\dots\}}\le|X-\mu|^{2+\delta}(\varepsilon s_n)^{-\delta}$; take $E$: $\le(\varepsilon s_n)^{-\delta}E[|X-\mu|^{2+\delta}]$. Sum over $i$: $\sum_iE[(X)^2\mathbf{1}_{\{\dots\}}]\le(\varepsilon s_n)^{-\delta}\sum_iE[|X|^{2+\delta}]$. Divide by $s_n^2$: $\frac1{s_n^2}\sum_iE[(X)^2\mathbf{1}_{\{\dots\}}]\le\frac1{\varepsilon^\delta s_n^{2+\delta}}\sum_iE[|X|^{2+\delta}]\to0$ by Lyapunov. <p> The Lyapunov condition is stronger but easier to verify than Lindeberg because absolute moments often have closed forms. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lyapunov vs Lindeberg / Lindeberg strictly weaker, but Lyapunov easier to verify ::@:: Lindeberg is strictly weaker than Lyapunov: distributions with finite variance but no higher moments satisfy Lindeberg but not Lyapunov. <p> __Trade-off:__ Lyapunov is easier to verify in practice because absolute moments often have closed forms. Lindeberg is the more fundamental condition — it is both necessary (under Feller) and sufficient for the CLT, whereas Lyapunov is only sufficient. <p> Lyapunov's condition also gives convergence rate information: higher $\delta$ yields faster tail bounds in some contexts. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

## classical CLT as a corollary

The classical CLT for i.i.d. sequences follows immediately from the Lindeberg CLT. Let $Y_1,Y_2,\dots$ be i.i.d. with $E[Y_1]=\mu$, $\operatorname{Var}[Y_1]=\sigma^2<\infty$. Set $X_{n,i}=Y_i$ for $i=1,\dots,n$, so $S_n=\sum_{i=1}^nY_i$, $s_n^2=n\sigma^2$, $k_n=n$. For any $\varepsilon>0$, $$\frac{1}{s_n^2}\sum_{i=1}^nE\!\bigl[(Y_i-\mu)^2\mathbf{1}_{\{|Y_i-\mu|>\varepsilon s_n\}}\bigr] =\frac{E\!\bigl[(Y_1-\mu)^2\mathbf{1}_{\{|Y_1-\mu|>\varepsilon\sigma\sqrt n\}}\bigr]}{\sigma^2}\longrightarrow0$$

by the dominated convergence theorem (DCT): as $n\to\infty$, $\varepsilon\sigma\sqrt n\to\infty$, so $\mathbf{1}_{\{|Y_1-\mu|>\varepsilon\sigma\sqrt n\}}\to0$ pointwise. The integrand is bounded by $(Y_1-\mu)^2$, which has finite expectation ($\sigma^2<\infty$). Hence DCT applies. Thus Lindeberg's condition holds, and the Lindeberg CLT gives $$\frac{S_n-n\mu}{\sigma\sqrt n}\xrightarrow{d}N(0,1).$$

---

Flashcards for this section are as follows:

- classical i.i.d. CLT as a corollary of Lindeberg (by dominated convergence theorem) ::@:: For i.i.d. $Y_i$ with $E[Y_1]=\mu$, $\operatorname{Var}[Y_1]=\sigma^2<\infty$, set $X_{n,i}=Y_i$, $S_n=\sum_{i=1}^nY_i$, $s_n^2=n\sigma^2$. <p> __Verification:__ Lindeberg becomes $E[(Y_1-\mu)^2\mathbf{1}_{\{|Y_1-\mu|>\varepsilon\sigma\sqrt n\}}]/\sigma^2$. As $n\to\infty$, $\varepsilon\sigma\sqrt n\to\infty$, so $\mathbf{1}_{\{\dots\}}\to0$ pointwise. The integrand is bounded by $(Y_1-\mu)^2\in L^1$ ($\sigma^2<\infty$). Hence DCT $\to0$ — Lindeberg holds. <p> __Conclusion:__ The Lindeberg CLT implies the classical CLT: $(S_n-n\mu)/(\sigma\sqrt n)\xrightarrow{d}N(0,1)$. No additional proof beyond checking Lindeberg — it is a special case. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- classical CLT / DCT verification chain (pointwise limit + dominating function) ::@:: __Why DCT applies:__ $\varepsilon\sigma\sqrt n\to\infty$, so $\mathbf{1}_{\{|Y_1-\mu|>\varepsilon\sigma\sqrt n\}}\to0$ pointwise (the threshold diverges). <p> __Dominating function:__ $(Y_1-\mu)^2\mathbf{1}_{\{\dots\}}\le(Y_1-\mu)^2$, and $E[(Y_1-\mu)^2]=\sigma^2<\infty$ guarantees integrability. <p> __Result:__ By DCT, the Lindeberg numerator $\to0$, so Lindeberg holds and the classical CLT follows. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

## worked example: Bernoulli triangular array <!-- check: ignore-line[section_example_heading]: genuine worked example needed for exposition -->

To see the Lindeberg-Feller CLT in action, consider a triangular array where the $i$-th variable in row $n$ is Bernoulli with success probability $p_{n,i}$. Let $X_{n,i}\sim\operatorname{Bernoulli}(p_{n,i})$, independent across $i$, with $\mu_{n,i}=p_{n,i}$ and $\sigma_{n,i}^2=p_{n,i}(1-p_{n,i})$. Set $s_n^2=\sum_{i=1}^{k_n}p_{n,i}(1-p_{n,i})$.

Choose a concrete pattern: for each $n$, take $k_n=n$ and let $p_{n,i}=1/2$ for all $i$ — the classical symmetric Bernoulli. Then each $\sigma_{n,i}^2=1/4$, so $s_n^2=n/4$. Lindeberg's condition holds because the variables are bounded ($|X_{n,i}-1/2|\le1/2$), and for $\varepsilon>0$ and large $n$, $\varepsilon s_n=\varepsilon\sqrt n/2$ exceeds $1/2$, making the indicators zero. The Lindeberg-Feller CLT then gives $\frac1{\sqrt n}\sum_{i=1}^n(2X_{n,i}-1)\xrightarrow{d}N(0,1)$, which matches the classical CLT for Bernoulli $(1/2)$.

For a more interesting pattern where $p_{n,i}$ depends on $n$: take $p_{n,i}=a_i/\sqrt{n}$ where $a_i\in(0,1)$ are fixed (e.g., $a_i=1/4$ for odd $i$, $a_i=3/4$ for even $i$). Then $p_{n,i}\to0$ as $n\to\infty$ (sparse), $\sigma_{n,i}^2\approx a_i/\sqrt{n}$ for large $n$, and $s_n^2\approx\frac1{\sqrt{n}}\sum_i a_i\to\infty$ for $k_n=n$. Since $|X_{n,i}-\mu_{n,i}|\le1$ and $\varepsilon s_n\to\infty$ for every $\varepsilon>0$, the indicators vanish for large $n$. Lindeberg's condition therefore holds, and the sum converges to normality — a result that cannot be obtained from the classical i.i.d. CLT because the summands are not identically distributed. This models rare-event counts (e.g., number of insurance claims per period) where the total rate grows without bound.

---

Flashcards for this section are as follows:

- Bernoulli example / constant $p=1/2$ (bounded $\implies$ Lindeberg holds) ::@:: For $X_{n,i}\sim\operatorname{Bernoulli}(1/2)$ independent across $i$, $\mu_{n,i}=1/2$, $\sigma_{n,i}^2=1/4$, $s_n^2=n/4$. <p> __Why Lindeberg holds:__ Variables are bounded ($|X_{n,i}-1/2|\le1/2$). For fixed $\varepsilon>0$ and large $n$, $\varepsilon s_n=\varepsilon\sqrt n/2$ exceeds $1/2$, making the tail indicators zero. <p> __Result:__ $\frac1{\sqrt n}\sum_i(2X_{n,i}-1)\xrightarrow{d}N(0,1)$, matching the classical Bernoulli CLT. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Bernoulli example / sparse $p_{n,i}=a_i/\sqrt n$ (non-identically distributed, rare events) ::@:: For $p_{n,i}=a_i/\sqrt{n}$ with fixed $a_i\in(0,1)$, $s_n^2\approx\frac1{\sqrt{n}}\sum_i a_i\to\infty$. <p> __Why Lindeberg holds:__ $|X_{n,i}-p_{n,i}|\le1$ and $\varepsilon s_n\to\infty$, so tail indicators vanish for large $n$. <p> __Key point:__ The summands are not identically distributed — the classical i.i.d. CLT does not apply. This models rare-event counts with growing total rate (each $p_{n,i}\to0$ but total expected count grows). <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- sparse Bernoulli example / why Lindeberg-Feller applies (non-identically distributed, rare events) ::@:: For $p_{n,i}=a_i/\sqrt{n}$ with fixed $a_i\in(0,1)$, the summands are not identically distributed and the classical i.i.d. CLT does not apply. <p> __Why Lindeberg-Feller works:__ $s_n^2\to\infty$, so $\varepsilon s_n\to\infty$ for every $\varepsilon>0$. Since $|X_{n,i}-p_{n,i}|\le1$, the tail indicators vanish for large $n$, satisfying Lindeberg's condition. <p> __Significance:__ Models rare-event settings with growing total rate (e.g., insurance claims per period), where the normal approximation is valid despite each $p_{n,i}\to0$. The Feller condition also holds: $\max_i\sigma_{n,i}/s_n\to0$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

## remarks on the method

### comparison with the characteristic function approach

The classical proof of the CLT uses characteristic functions (Fourier transforms). For i.i.d. variables with variance $\sigma^2$, the characteristic function of the normalised sum is $(\varphi(t/\sqrt n))^n$, where $\varphi$ is the characteristic function of $X_1$. Expanding $\varphi$ around $0$ gives $\varphi(t)=1-\sigma^2t^2/2+o(t^2)$, so $(\varphi(t/\sqrt n))^n\to e^{-t^2/2}$, the characteristic function of $N(0,1)$. Lévy's continuity theorem then gives convergence in distribution.

Lindeberg's method differs in two important ways:

- __Directness:__ It works with expectations of test functions directly, bypassing Fourier inversion. This makes it more elementary — no complex analysis or Fourier theory is needed.
- __Generalisability:__ The same telescoping-replacement idea extends to settings where characteristic functions are unavailable or unwieldy. The Lindeberg-Feller CLT for triangular arrays is a prime example — the CF approach requires handling products of $k_n$ different characteristic functions, which is messy without the Lindeberg condition. The "replacement" philosophy also underlies Stein's method for quantifying rates of convergence.

For triangular arrays, the replacement method is especially natural: instead of analysing a product of $k_n$ different CFs, one replaces each variable one at a time, and the Lindeberg condition directly controls the cumulative Taylor error.

---

Flashcards for this section are as follows:

- classical CLT CF proof / $\varphi(t/\sqrt n)^n$ expansion + Lévy continuity ::@:: CF of normalised sum is $(\varphi(t/\sqrt n))^n$. Expand $\varphi(t)=1-\sigma^2t^2/2+o(t^2)$, so $(\varphi(t/\sqrt n))^n\to e^{-\sigma^2t^2/2}$, the CF of $N(0,\sigma^2)$. <p> __Lévy continuity:__ Pointwise CF convergence $\implies$ convergence in distribution. <p> __Limitation for arrays:__ Product of $k_n$ different CFs — messy without Lindeberg's condition. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- Lindeberg replacement vs CF proof / directness and generalisability ::@:: __Lindeberg's method:__ Works directly with expectations of test functions via telescoping replacement. More elementary — no Fourier/complex analysis needed. Natural for triangular arrays: replace one variable at a time. <p> __CF proof:__ Requires expanding products of $k_n$ different characteristic functions — unwieldy. <p> __Stein's method:__ Builds on the same "replace and control error" philosophy to give convergence rates, which the basic Lindeberg approach does not. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

### why matching the first two moments is sufficient

A natural question is why matching only the first two moments of $Z_{n,i}$ and $W_{n,i}$ makes the proof work — why doesn't the third moment matter? The Taylor expansion of $g$ up to second order leaves a remainder that depends on $g''$ and the squared increments $Z_{n,i}^2,W_{n,i}^2$. The linear term vanishes because $E[Z_{n,i}]=E[W_{n,i}]=0$; the quadratic term vanishes because $\operatorname{Var}[Z_{n,i}]=\operatorname{Var}[W_{n,i}]$. The remaining error involves only second powers and the modulus of continuity of $g''$.

If one needed to match third moments, the Taylor expansion would need to go to third order, requiring $g'''$ bounded and uniform continuity of $g'''$, and the remainder would involve $Z_{n,i}^3$ terms that vanish only if $E[Z_{n,i}^3]=E[W_{n,i}^3]=0$. For symmetric distributions this is automatic, but the CLT holds for all distributions with finite variance, not just symmetric ones. The fact that second-order truncation suffices is a deep insight: because each individual $Z_{n,i}$ is small (of order $O_p(1/\sqrt{k_n})$ in typical cases), the second-order Taylor error decays fast enough that $k_n$ such errors sum to $o(1)$. Higher moments only affect the convergence rate, not the existence of the limit.

---

Flashcards for this section are as follows:

- why second-moment matching works / cancellation via $E[Z]=0$ + $\operatorname{Var}[Z]=\operatorname{Var}[W]$ ::@:: Taylor to second order: first-order term vanishes because $E[Z_{n,i}]=E[W_{n,i}]=0$. Second-order term vanishes because $\operatorname{Var}[Z_{n,i}]=\operatorname{Var}[W_{n,i}]$. <p> __Remainder control:__ Only second powers $Z_{n,i}^2,W_{n,i}^2$ plus the modulus of continuity of $g''$ remain. Each term is $o(1/k_n)$ by Lindeberg + uniform continuity of $g''$. Summing $k_n$ terms $\to o(1)$. <p> __Key:__ Only $E[Z]=0$ and $\operatorname{Var}[Z]=\operatorname{Var}[W]$ matter — higher moments cancel indirectly through the Lindeberg bound on second powers. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
- why third moments not needed / second-order truncation suffices ::@:: __Third-moment matching would require:__ $g'''$ bounded and uniformly continuous, and $E[Z_{n,i}^3]=E[W_{n,i}^3]$ — not guaranteed for non-symmetric distributions. <p> __Why second order is enough:__ Each $Z_{n,i}$ is $O_p(1/\sqrt{k_n})$ in typical cases, so the second-order Taylor error decays fast enough. The sum of $k_n$ such errors $\to0$. <p> __Impact:__ Third moments affect the convergence rate but not the existence of the CLT limit. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
