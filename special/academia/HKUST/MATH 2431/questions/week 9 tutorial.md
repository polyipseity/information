---
aliases:
    - HKUST MATH 2431 week 9 tutorial
    - HKUST MATH2431 week 9 tutorial
    - MATH 2431 week 9 tutorial
    - MATH2431 week 9 tutorial
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/week_9_tutorial
    - language/in/English
---

# week 9 tutorial

- HKUST MATH 2431

The questions on this page combine the T1B tutorial session problems with supplementary examples from the solution notes, all paraphrased in compact course-note form.

- topics: expectation and laws; zero expectation for nonnegative variables; equality almost surely from $L^1$ distance; inclusion-exclusion via indicators; tail sum formula; expected search cost; order statistics expectation.

> Show that the expectation of a random variable depends only on its law.
>
> Solution: {@{The expectation $E[X]=\int_\Omega X\,dP$}@} is {@{the Lebesgue integral of $X$ with respect to the underlying probability $P$}@}. By {@{the change-of-variables formula for pushforward measures}@}, {@{$$\int_\Omega X\,dP = \int_{\mathbb{R}} x\,dP_X(x),$$}@} where {@{$P_X=P\circ X^{-1}$ is the law of $X$ (the distribution on $\mathbb{R}$)}@}. {@{The right-hand side}@} depends {@{only on $P_X$, not on the original sample space $\Omega$}@}. This is the sense in which {@{the expectation depends only on the distribution $P_X$}@}.
>
> Concretely, approximate {@{$X$ from below by a sequence of simple functions $X_n=\sum_{k=1}^{K_n} x_{n,k}\,\mathbf 1_{A_{n,k}}$}@} where $x_{n,k}$ are {@{the values the simple function takes}@} (e.g., dyadic rationals {@{$k/2^n$ on the partition $B_{n,k}=[k/2^n,(k+1)/2^n)$ of $\mathbb{R}$}@}) and {@{$A_{n,k}=X^{-1}(B_{n,k})$}@}. Then {@{$$E[X_n]=\sum_k x_{n,k}P(A_{n,k})=\sum_k x_{n,k}P_X(B_{n,k})$$}@} depends {@{only on $P_X$, not on the specific representation of $X$ on $\Omega$}@}. {@{The monotone convergence theorem}@} gives {@{$E[X]=\lim_{n\to\infty}E[X_n]$ whenever the expectation exists}@}, so {@{$E[X]$ is determined by the law alone}@}.

<!-- markdownlint MD028 -->

> Let $X\ge 0$ almost surely and suppose $E[X]=0$. Show that $P(X=0)=1$.
>
> Solution: For each {@{$n\ge 1$, let $A_n=\{X\ge 1/n\}$}@}. Since {@{$X\ge \frac1n\mathbf 1_{A_n}$ pointwise}@}, we have {@{$$0=E[X]\ge E\left[\frac1n\mathbf 1_{A_n}\right]=\frac1nP(A_n).$$}@} {@{The sandwich $0\le\frac1nP(A_n)\le 0$}@} forces {@{$P(A_n)=0$ for all $n$}@}. Because {@{$A_n\uparrow\{X>0\}$, continuity from below}@} gives {@{$P(X>0)=\lim_{n\to\infty}P(A_n)=0$, so $P(X=0)=1$}@}. (This is essentially {@{Markov's inequality $P(X\ge\varepsilon)\le E[X]/\varepsilon$ applied with $\varepsilon=1/n$}@}.)

<!-- markdownlint MD028 -->

> Decide whether the following are true for integrable random variables $X,Y$: (a) if $E[X]=E[Y]$, then $X=Y$ almost surely; (b) if $E[|X-Y|]=0$, then $X=Y$ almost surely.
>
> Solution:
>
> - (a) {@{__False.__}@} Equal expectations {@{alone do not force equality of random variables}@}. For a concrete counterexample, let {@{$X\equiv 0$ and let $Y$ be a Rademacher variable taking values $\pm1$ with equal probability $1/2$}@}. Then {@{$E[X]=E[Y]=0$, yet $P(X=Y)=0$ (they differ almost surely)}@}.
> - (b) {@{__True.__}@} The variable $|X-Y|$ is {@{nonnegative almost surely and has expectation $0$}@}. By {@{the previous result (a nonnegative random variable with zero expectation vanishes almost surely)}@}, we obtain {@{$|X-Y|=0$ almost surely, which forces $X=Y$ almost surely}@}.

<!-- markdownlint MD028 -->

> Give an expectation-based proof of the inclusion-exclusion formula by starting from the identity $\mathbf1_{\cup_{j=1}^n A_j}=1-\prod_{j=1}^n(1-\mathbf1_{A_j})$.
>
> Solution: Expand {@{the product explicitly}@}: {@{$$\prod_{j=1}^n(1-\mathbf 1_{A_j}) = \sum_{k=0}^n (-1)^k \sum_{1\le i_1<\dots<i_k\le n} \mathbf 1_{A_{i_1}\cap\cdots\cap A_{i_k}},$$}@} where {@{the $k=0$ term is $1$ (the empty product)}@}. {@{Substituting into $\mathbf 1_{\cup A_j}=1-\prod(1-\mathbf 1_{A_j})$}@} gives {@{$$\mathbf 1_{\bigcup_{j=1}^n A_j} = \sum_{k=1}^n (-1)^{k+1} \sum_{1\le i_1<\dots<i_k\le n} \mathbf 1_{A_{i_1}\cap\cdots\cap A_{i_k}}.$$}@} Take {@{expectations term by term and use $E[\mathbf 1_B]=P(B)$}@} to obtain {@{the usual alternating inclusion-exclusion formula $$P\left(\bigcup_{j=1}^n A_j\right)=\sum_i P(A_i)-\sum_{i<j}P(A_i\cap A_j)+\cdots+(-1)^{n+1}P\left(\bigcap_{j=1}^n A_j\right).$$}@}

---

<!-- Source: Solution of Tutorial Notes 7 (Supplementary Examples) -->

> Show the tail sum formula for the discrete case: let $X$ take values in $\mathbb N_0$, then $$E[X]=\sum_{k=1}^\infty P(X\ge k).$$
>
> Solution: Note {@{the pointwise identity $X=\sum_{k=1}^\infty \mathbf 1_{\{X\ge k\}}$}@}: for each {@{$\omega$, a nonnegative integer $X(\omega)$}@} contributes {@{$1$ for every $k\le X(\omega)$, so the sum counts $1$ exactly $X(\omega)$ times}@}. Since {@{all terms are nonnegative, Tonelli's theorem}@} justifies {@{swapping expectation and summation}@}: {@{$$E[X]=\sum_{k=1}^\infty E[\mathbf 1_{\{X\ge k\}}]=\sum_{k=1}^\infty P(X\ge k).$$}@} This is {@{the layer-cake representation (or tail-sum formula)}@} for the expectation of {@{a nonnegative integer-valued random variable}@}.

<!-- markdownlint MD028 -->
> One of the numbers 1 through 10 is randomly chosen. You try to guess it by asking yes/no questions.
>
> - (a) Your _i_-th question is "Is it _i_?" (linear search). Find the expected number of questions.
> - (b) With each question, you eliminate roughly half the remaining numbers (binary search). Find the expected number of questions.
>
> Solution:
>
> - For (a), {@{the number $X$ of questions}@} is {@{uniformly distributed on $\{1,\dots,10\}$}@}, so {@{$$E[X]=\frac{1+2+\cdots+10}{10}=5.5.$$}@}
> - For (b), {@{an optimal binary-search strategy}@} {@{halves the remaining set each time}@}. Since 10 lies {@{between $2^3=8$ and $2^4=16$}@}, the depth {@{ranges from 3 to 4 questions (worst-case $4$)}@}. Concretely, {@{6 of the 10 numbers are reached in 3 questions and the remaining 4 require 4 questions}@}, giving {@{$$E[X]=3\cdot\frac{6}{10}+4\cdot\frac{4}{10}=3.4.$$}@} Thus {@{binary search (3.4) beats linear search (5.5)}@} in expectation.

<!-- markdownlint MD028 -->
> Suppose $4$ fair dice are rolled. Find (a) the expected minimum $L$ and (b) the expected maximum $U$ of the $4$ rolls.
>
> Solution: For a single fair die, {@{$P(X\ge k)=\frac{7-k}{6}$ for $k=1,\dots,6$}@}.
>
> For the maximum $U=\max\{X_1,\dots,X_4\}$, {@{the event $U\le k$}@} means {@{all four dice show at most $k$, so $P(U\le k)=(k/6)^4$}@}. {@{The tail-sum formula}@} then gives {@{$$E[U]=\sum_{k=1}^6 P(U\ge k)=\sum_{k=1}^6\bigl(1-P(U\le k-1)\bigr)=\sum_{k=1}^6\left(1-\left(\frac{k-1}{6}\right)^4\right).$$}@}
>
> For the minimum $L$, {@{the event $L\ge k$}@} means {@{all dice show at least $k$, so $P(L\ge k)=\bigl(\frac{7-k}{6}\bigr)^4$}@}. {@{The tail-sum formula}@} directly yields {@{$$E[L]=\sum_{k=1}^6 P(L\ge k)=\sum_{k=1}^6\left(\frac{7-k}{6}\right)^4.$$}@} Computing these sums gives {@{$E[U]\approx 5.24$ and $E[L]\approx 1.76$}@}.
