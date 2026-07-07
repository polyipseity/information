---
aliases:
    - HKUST MATH 2431 midterm examination
    - HKUST MATH2431 midterm examination
    - MATH 2431 midterm examination
    - MATH2431 midterm examination
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/midterm_examination
    - language/in/English
---

# midterm examination

- HKUST MATH 2431

This page summarizes the written questions from the official midterm examination materials in paraphrased study-note form.

## multiple choice (questions 1–5)

> How many probability measures exist on $\Omega=\{0,1\}$ with $\sigma$-algebra $\mathcal P(\{0,1\})$?
>
> Solution: For each {@{$p\in[0,1]$}@}, {@{$\mathrm{Ber}(p)$}@} gives a different measure, so there are {@{uncountably many}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> If $P[C\mid D]>P[C]$ with $P[C],P[D]>0$, which of the following must hold?
>
> - (A) $P[D\mid C]>P[D]$.
> - (B) $P[C]=P[D]$.
> - (C) $P[C\mid D]=P[D\mid C]$.
> - (D) $P[C]>P[D]$.
> - (E) $P[D\mid C]<P[D]$.
>
> Solution: (A) is true. {@{$P[C\mid D]>P[C]\iff P[C\cap D]>P[C]P[D] \iff P[D\mid C]>P[D]$}@}.
>
> - (B) is false. Take {@{$\Omega=\{1,2,3,4\}$, $P=U(\{1,2,3,4\})$}@}, {@{$C=\{1\}$, $D=\{1,2\}$}@}; then {@{$P[C\mid D]=1/2>1/4=P[C]$ but $P[D]=1/2\neq1/4=P[C]$}@}.
> - (C) is false — same example gives {@{$P[C\mid D]=1/2\neq1=P[D\mid C]$}@}.
> - (D) is false — same example gives {@{$P[C]=1/4<1/2=P[D]$}@}.
> - (E) is false — {@{opposite of (A)}@}.

<!-- markdownlint MD028 -->

> Two groups of $4$ people each sit on opposite sides of a rectangular table. How many seating arrangements are possible?
>
> Solution: {@{$4!$ per side}@}, times {@{$2$ for which side each group takes}@}, giving {@{$2\cdot(4!)^2$}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> For a set $\Omega$ with $|\Omega|=n$, how many ways are there to choose a collection $E\subseteq\mathcal P(\Omega)$?
>
> Solution: This counts {@{$\mathcal P(\mathcal P(\Omega))$}@}, so {@{$2^{2^n}$}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Let $F(x)=0$ for $x<0$, $F(0)=1/2$, $F(x)=1$ for $x>0$. Is $F$ a cumulative distribution function?
>
> Solution: {@{No}@}, because {@{$F$ is not right-continuous at $0$}@}: {@{$F(0)=1/2$ but $\lim_{x\downarrow0}F(x)=1$}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

## true/false (questions 6–10)

> For a discrete probability space $(\Omega,\mathcal P(\Omega),P)$ and an event $B\in\mathcal P(\Omega)$, the set function $Q[A]=P[A\cap B]$ defines a probability measure on $(B,\mathcal P(B))$.
>
> Solution: {@{False}@}. Take {@{$\Omega=\{0,1\}$, $P=\mathrm{Ber}(1/2)$, $B=\{0\}$}@}; then {@{$Q[B]=1/2\neq1$, so normalization fails}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> For independent events $A,B$, $P[A\cup B]=P[A]+P[B]P[A^c]$.
>
> Solution: {@{True}@}. {@{$P[A\cup B]=P[A]+P[B]-P[A\cap B]=P[A]+P[B]-P[A]P[B]$}@} <br/> {@{${}=P[A]+P[B](1-P[A])=P[A]+P[B]P[A^c]$}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> If $P[(a,a+1]]=Q[(a,a+1]]$ for all $a\in\mathbb R$, then $P=Q$.
>
> Solution: {@{True}@}. For any $x$, {@{$F_P(x)=\sum_{n=1}^\infty P[(x-n,x-n+1]]=\sum_{n=1}^\infty Q[(x-n,x-n+1]]=F_Q(x)$}@}, so {@{the CDFs agree}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> For a finite $\Omega$, if $|\delta(\mathcal E)|=|\sigma(\mathcal E)|$, then $\delta(\mathcal E)$ is a $\sigma$-algebra.
>
> Solution: {@{True}@}. Since {@{$\delta(\mathcal E)\subseteq\sigma(\mathcal E)$}@} and both are {@{finite with equal cardinality}@}, {@{$\delta(\mathcal E)=\sigma(\mathcal E)$}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> The pointwise limit of a sequence of CDFs is always a CDF.
>
> Solution: {@{False}@}. {@{$F_n(x)=\mathbf 1_{[1/n,\infty)}(x)\to\mathbf 1_{(0,\infty)}(x)$}@}, which is {@{not right-continuous at $0$}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

## long-form (questions 11–12)

> - (a) Let $(\Omega,\mathcal F,P)$ be a probability space and $\mathcal E\subseteq\mathcal F$. Define what it means for $\mathcal E$ to be $\cap$-stable.
> - (b) Define $\sigma(\mathcal E)$, the $\sigma$-algebra generated by $\mathcal E$.
> - (c) State Dynkin's $\pi$-$\lambda$ theorem.
> - (d) Let $(\Omega,\mathcal F,P)$ be a probability space and $\mathcal E_1,\mathcal E_2\subseteq\mathcal F$ be $\cap$-stable. Suppose $P[A\cap B]=P[A]P[B]$ for all $A\in\mathcal E_1$, $B\in\mathcal E_2$. Show this holds for all $A\in\sigma(\mathcal E_1)$, $B\in\sigma(\mathcal E_2)$.
> - (e) Let $\mathcal D\subseteq\mathcal P(\Omega)$ be a Dynkin system that is also closed under finite unions. Show $\mathcal D$ is a $\sigma$-algebra.
>
> Solution:
>
> - (a) {@{$\mathcal E$ is $\cap$-stable}@} if {@{for all $A,B\in\mathcal E$, $A\cap B\in\mathcal E$}@}.
> - (b) {@{$\sigma(\mathcal E)=\bigcap\{\mathcal G\subseteq\mathcal P(\Omega):\mathcal E\subseteq\mathcal G,\ \mathcal G\text{ is a }\sigma\text{-algebra}\}$}@}.
> - (c) If {@{$\mathcal E\subseteq\mathcal P(\Omega)$ is $\cap$-stable and $\mathcal D\subseteq\mathcal P(\Omega)$ is a Dynkin system with $\mathcal E\subseteq\mathcal D$}@}, then {@{$\sigma(\mathcal E)\subseteq\mathcal D$}@}.
> - (d) Fix {@{$A\in\mathcal E_1$}@} and define {@{$\mathcal D_A=\{B\in\mathcal F:P[A\cap B]=P[A]P[B]\}$}@}. Show $\mathcal D_A$ is {@{a Dynkin system containing $\mathcal E_2$}@}. By {@{Dynkin's $\pi$-$\lambda$ theorem}@}, {@{$\sigma(\mathcal E_2)\subseteq\mathcal D_A$}@}. Then {@{fix $B\in\sigma(\mathcal E_2)$ and repeat}@}.
> - (e) $\mathcal D$ is {@{already closed under complements}@}. For {@{$A,B\in\mathcal D$}@}, {@{$A\cap B=(A^c\cup B^c)^c\in\mathcal D$ using finite unions}@}, so $\mathcal D$ is {@{$\cap$-stable, hence a $\sigma$-algebra}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> - (a) Let $f(x)=c$ for $x\in\bigcup_{n=1}^\infty[n,n+2^{-n})$ and $f(x)=0$ elsewhere. Determine $c$ so that $f$ is a probability density.
> - (b) Show that a $2026$-periodic continuous nonnegative function $g\colon\mathbb R\to\mathbb R$ cannot be a probability density.
> - (c) Let $p$ be a probability mass function on a countably infinite $\Omega$. Can $q(\omega)=2\sqrt{p(\omega)}$ be a probability mass function?
> - (d) The Rayleigh distribution $\mathrm{Ra}(\theta)$ has density $h(x)=\frac{x}{\theta^2}e^{-x^2/(2\theta^2)}\mathbf 1_{[0,\infty)}(x)$. Find its median $m$.
>
> Solution:
>
> - (a) {@{Normalization}@} requires {@{$1=c\sum_{n=1}^\infty2^{-n}$}@}. Since {@{$\sum_{n=1}^\infty2^{-n}=1$}@}, we have {@{$c=1$}@}.
> - (b) If {@{$g$ is not identically $0$}@}, {@{continuity}@} gives {@{a positive integral over one period}@}, and {@{periodicity}@} makes {@{$\int_{-\infty}^\infty g(x)\,dx=\infty$}@}. If {@{$g$ is identically $0$}@}, then it {@{cannot satisfy normalization}@}.
> - (c) {@{No}@}. {@{For $x\in[0,1]$, $\sqrt x\ge x$}@}, so {@{$\sum_\omega q(\omega)\ge2\sum_\omega p(\omega)=2$}@}.
> - (d) {@{$F(x)=\int_0^x\frac{t}{\theta^2}e^{-t^2/(2\theta^2)}\,dt$}@}. Substituting {@{$u=t^2/(2\theta^2)$}@}, {@{$du=t/\theta^2\,dt$}@}, we get {@{$F(x)=1-e^{-x^2/(2\theta^2)}$ on $[0,\infty)$}@}. Setting {@{$F(m)=1/2$}@} gives {@{$m=\theta\sqrt{2\log2}$}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->
