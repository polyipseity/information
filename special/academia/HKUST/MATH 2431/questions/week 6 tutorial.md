---
aliases:
    - HKUST MATH 2431 week 6 tutorial
    - HKUST MATH2431 week 6 tutorial
    - MATH 2431 week 6 tutorial
    - MATH2431 week 6 tutorial
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/week_6_tutorial
    - language/in/English
---

# week 6 tutorial

- HKUST MATH 2431

The questions on this page summarize the _official tutorial materials_ for week 6. Because they come from course materials rather than repository-authored review prompts, each question is kept as a markdown quote block and the clozes live inside that quoted Q&A block.

- topics: exponential waiting-time memorylessness; PDF validity checks; median criterion via CDF; Dynkin systems; pi-lambda theorem; densities and cumulative distribution functions.

> Radioactive-source model: emissions follow a Poisson process with rate $3$ per minute. If no emission has occurred in the first minute, what is the probability that one must wait more than 10 additional minutes for the first emission?
>
> Solution: Let $T$ be the {@{first-arrival time}@}. Then $\{T>t\}$ means {@{no emission occurs in the time interval $[0,t]$}@}. If $N_t$ denotes the number of emissions by time $t$, this event is exactly {@{the zero-count event $\{N_t=0\}$}@}. Since a rate-3 Poisson process satisfies $N_t\sim\mathrm{Pois}(3t)$, we get {@{the survival formula $P(T>t)=P(N_t=0)=e^{-3t}$}@}. The question asks for the probability of waiting {@{more than 10 additional minutes after already waiting 1 minute with no emission}@}, so the required probability is {@{the conditional tail probability $P(T>11\mid T>1)$}@}. By the {@{memoryless property of the exponential waiting time}@}, this equals {@{the fresh-tail probability $P(T>10)=e^{-30}$}@}. <!--SR:!2026-05-17,16,307!2026-05-16,15,307!2026-05-15,14,290!2026-05-16,15,307!2026-05-18,17,307!2026-05-17,16,307!2026-05-18,17,301!2026-05-16,15,307-->

<!-- markdownlint MD028 -->

> Determine for each candidate whether it can be a probability density function, and find $c$ when possible:
>
> - (a) $f(x)=c(2x-x^3)$ for $0<x<2$.
> - (b) $f(x)=cx e^{-x^2}$ for $x>0$.
> - (c) $f(x)=ce^{-x}$ for $x>0$.
>
> Solution:
>
> - A PDF must be {@{nonnegative}@} and have {@{total integral 1}@}.
> - (a) Since $2x-x^3=x(2-x^2)$ changes sign on $(0,2)$ and becomes negative when $x>\sqrt2$, no choice of $c$ makes the function nonnegative everywhere; thus it is {@{not a PDF}@}.
> - (b) Here {@{normalization reduces to evaluating $\int_0^\infty x e^{-x^2}dx$, and since that integral equals $1/2$ we must choose $c=2$}@}.
> - (c) Here {@{the unscaled density already integrates to $1$ on $(0,\infty)$ because $\int_0^\infty e^{-x}dx=1$, so the correct normalizing constant is $c=1$}@}. <!--SR:!2026-05-18,17,307!2026-05-15,14,290!2026-05-17,16,301!2026-05-18,17,307!2026-05-17,16,301-->

<!-- markdownlint MD028 -->

> Let $X$ be a continuous random variable with CDF $F$. Show that $m$ is a median of $X$ iff $\lim_{x\uparrow m}F(x)\le 1/2$ and $F(m)\ge 1/2$.
>
> Solution: By definition, {@{a median is a point $m$ such that $P(X\le m)\ge 1/2$ and $P(X\ge m)\ge 1/2$}@}. The first condition is {@{exactly $F(m)\ge1/2$}@}. Also {@{the second condition becomes $P(X\ge m)=1-P(X<m)=1-F(m^-)\ge1/2$, equivalently $F(m^-)\le1/2$}@}. Therefore the criterion is {@{the two-sided CDF condition $F(m^-)\le1/2\le F(m)$}@}; for continuous $X$, this reduces to {@{the simpler equation $F(m)=1/2$}@}. <!--SR:!2026-05-16,15,307!2026-05-16,15,307!2026-05-17,16,301!2026-05-17,16,307!2026-05-15,14,290-->

<!-- markdownlint MD028 -->

> Show that Dynkin's pi-lambda theorem is equivalent to the statement that if $\mathcal{E}$ is a pi-system then $\sigma(\mathcal{E})=\delta(\mathcal{E})$.
>
> Solution: Apply Dynkin's theorem to a pi-system $\mathcal E$ and its Dynkin closure $\delta(\mathcal E)$. This gives {@{the inclusion $\sigma(\mathcal E)\subseteq\delta(\mathcal E)$}@}, while the reverse inclusion is automatic because {@{every sigma-algebra is a Dynkin system}@}. Hence {@{we obtain the equality $\sigma(\mathcal E)=\delta(\mathcal E)$}@}. Conversely, if this equality holds for every pi-system, then {@{any Dynkin system containing $\mathcal E$ must also contain $\delta(\mathcal E)=\sigma(\mathcal E)$, which is exactly Dynkin's pi-lambda theorem}@}. <!--SR:!2026-05-16,15,301!2026-05-17,16,307!2026-05-18,17,307!2026-05-18,17,307-->

<!-- markdownlint MD028 -->

> Suppose the waiting time for bank service is $\mathrm{Exp}(1/5)$ minutes. A customer leaves if the wait exceeds 10 minutes and visits the bank 5 times in a week. What is the PMF of the number of times the customer leaves unserved?
>
> Solution: With $X\sim\mathrm{Exp}(1/5)$, the {@{one-visit leave probability is $q=P(X>10)=e^{-2}$}@}. Over {@{5 independent visits}@}, the number $L$ of unserved departures follows {@{the binomial law $\mathrm{Bin}(5,e^{-2})$}@}, so the pmf is {@{the formula $P(L=k)=\binom5k e^{-2k}(1-e^{-2})^{5-k}$ for $k=0,1,2,3,4,5$}@}. <!--SR:!2026-05-17,16,307!2026-05-16,15,307!2026-05-18,17,307!2026-05-18,17,301-->

<!-- markdownlint MD028 -->

> Let $f(x)=cx^2\mathbf{1}_{[0,1]}(x)$. Find $c$, the CDF, and $P([0.1,0.5))$.
>
> Solution: Normalize first via $1=\int_{-\infty}^{\infty}f(x)dx=\int_0^1cx^2dx=c/3$, so {@{$c=3$}@}. Then the CDF is {@{$F(x)=0$ for $x<0$, $F(x)=x^3$ for $0\le x\le1$, and $F(x)=1$ for $x>1$}@}, hence {@{$P([0.1,0.5))=F(0.5)-F(0.1)=0.124$}@}. Since this law has a density, it is {@{continuous}@}, so {@{endpoint inclusion/exclusion does not change interval probabilities}@}. <!--SR:!2026-05-18,17,307!2026-05-17,16,307!2026-05-15,14,290!2026-05-18,17,307!2026-05-15,14,290-->

<!-- markdownlint MD028 -->

> Let $F(x)=\sum_{i=1}^{\infty}2^{-i}\mathbf{1}_{[1/i,\infty)}(x)$. Show that $F$ is a cumulative distribution function and compute $P([1/10,\infty))$ for its associated measure.
>
> Solution: The definition already shows what is happening: whenever $x$ reaches the point {@{$1/i$}@}, the function $F$ {@{jumps upward by size $2^{-i}$}@}. So {@{$F$ is the cumulative function of a discrete law that puts mass $2^{-i}$ at the point $1/i$}@}. Each term $2^{-i}\mathbf{1}_{[1/i,\infty)}(x)$ is {@{nondecreasing and right-continuous}@}, so their sum is nondecreasing; right continuity follows because {@{the coefficients $2^{-i}$ are summable}@}. Also $F(x)=0$ for $x<0$, and as $x\to\infty$ every indicator turns on, so {@{$F(x)\to\sum_{i=1}^{\infty}2^{-i}=1$}@}. Therefore {@{$F$ is a CDF}@}. For the associated measure, the interval $[1/10,\infty)$ contains exactly the atoms $1,1/2,\dots,1/10$, so {@{$P([1/10,\infty))=\sum_{i=1}^{10}2^{-i}=1-2^{-10}$}@}. <!--SR:!2026-05-16,15,307!2026-05-17,16,307!2026-05-15,14,290!2026-05-16,15,307!2026-05-18,17,307!2026-05-15,14,290!2026-05-15,14,290!2026-05-15,14,290-->

<!-- markdownlint MD028 -->

> Explain the extra tutorial remark that once a function $F$ satisfies the CDF axioms, the Lebesgue-Stieltjes theorem produces a corresponding probability measure.
>
> Solution: The {@{Lebesgue-Stieltjes correspondence}@} says that {@{any function with the CDF axioms}@} determines {@{a unique probability measure $\mu_F$}@} on $(\mathbb R,\mathcal B(\mathbb R))$ via {@{$\mu_F(( -\infty,x])=F(x)$ for all $x$}@}, so {@{specifying $F$ is equivalent to specifying the full law}@}. <!--SR:!2026-05-16,15,307!2026-05-17,16,301!2026-05-17,16,307!2026-05-15,14,290!2026-05-16,15,307-->
