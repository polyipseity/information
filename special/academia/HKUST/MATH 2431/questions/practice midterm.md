---
aliases:
    - HKUST MATH 2431 practice midterm
    - HKUST MATH2431 practice midterm
    - MATH 2431 practice midterm
    - MATH2431 practice midterm
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/practice_midterm
    - language/in/English
---

# practice midterm

- HKUST MATH 2431

The question blocks on this page summarize the _official practice problems for the midterm exam_. The accompanying official midterm-guidelines sheet says that the midterm covers Sessions 1-11 (Weeks 1-6; Chapters 1 - Section 5.2 in the notes; problem sets 1-5), except the proof of Theorem 4.17 (Dynkin's pi-lambda theorem), Formula (4.61) (the pseudoinverse definition), Remark 4.20 (iii) on singular continuous distributions, Definition 5.5 and Example 5.6 on equality in law, and Problem 2 on Problem Set 5.

- topics: convex combinations of probability measures; transformations of cumulative distribution functions; measurable bijections; transformation of continuous random variables.

> Let $(\Omega,\mathcal{F})$ be a measurable space.
>
> - (a) Let $P_1$ and $P_2$ be probability measures on $(\Omega,\mathcal{F})$. Show that, for $\lambda\in[0,1]$, the set function $Q_\lambda[A]=\lambda P_1[A]+(1-\lambda)P_2[A]$ is a probability measure on $(\Omega,\mathcal{F})$.
> - (b) Now let $\lambda<0$. Give an explicit example of $(\Omega,\mathcal{F})$ and two probability measures $P_1\neq P_2$ such that the same formula still defines a probability measure, or prove that this is impossible.
> - (c) Suppose $F_1$ and $F_2$ are cumulative distribution functions. Decide whether $G_1=\tfrac12(F_1+F_2)$ and $G_2=\sqrt{F_1F_2}$ are cumulative distribution functions.
> - (d) Assume now that $F_1(x)>0$ for all $x\in\mathbb{R}$. Decide, with proof or examples, whether $G_3=F_2/F_1$ is always a cumulative distribution function, never a cumulative distribution function, or sometimes but not always a cumulative distribution function.
>
> Solution:
>
> - (a) For $\lambda\in[0,1]$, the coefficients are {@{nonnegative and sum to $1$}@}. Hence {@{$Q_\lambda[A]\ge0$ for every $A\in\mathcal{F}$}@}, {@{normalization gives $Q_\lambda[\Omega]=\lambda P_1[\Omega]+(1-\lambda)P_2[\Omega]=1$}@}, and for pairwise disjoint $(A_j)$, {@{countable additivity is preserved because $Q_\lambda[\bigcup_jA_j]=\lambda\sum_jP_1[A_j]+(1-\lambda)\sum_jP_2[A_j]=\sum_jQ_\lambda[A_j]$}@}. Therefore {@{$Q_\lambda$ is a probability measure}@}.
> - (b) It is {@{sometimes still possible when $\lambda<0$}@}. Take {@{$\Omega=\{0,1\}$, $\mathcal{F}=\mathcal{P}(\Omega)$, and $P_2(\{0\})=P_2(\{1\})=1/2$}@}, and choose any $\varepsilon$ such that {@{$0<\varepsilon\le1/(2|\lambda|)$, so the negative coefficient cannot make a singleton mass fall below $0$}@}. Define {@{$P_1(\{0\})=1/2+\varepsilon$ and $P_1(\{1\})=1/2-\varepsilon$}@}. Then {@{$Q_\lambda(\{0\})=1/2+\lambda\varepsilon$ and $Q_\lambda(\{1\})=1/2-\lambda\varepsilon$}@}, and since $|\lambda|\varepsilon$ satisfies {@{$|\lambda|\varepsilon\le1/2$, both values $1/2\pm\lambda\varepsilon$ lie in $[0,1]$ and are valid probabilities}@}. Thus $Q_\lambda$ is again {@{a probability measure even though $\lambda<0$ and $P_1\neq P_2$}@}.
> - (c) Both are CDFs because each construction preserves {@{monotonicity, right continuity, and the endpoint limits $0$ at $-\infty$ and $1$ at $+\infty$}@}. For {@{$G_1=\tfrac12(F_1+F_2)$}@}, taking {@{an average of two nondecreasing right-continuous functions with limits $0$ and $1$ at $\pm\infty$ preserves all CDF axioms}@}. For {@{$G_2=\sqrt{F_1F_2}$}@}, $F_1F_2$ is {@{nondecreasing because both factors are nondecreasing in $[0,1]$}@}, and multiplication plus $x\mapsto\sqrt{x}$ preserve {@{right continuity and endpoint limits}@}. Hence {@{$G_1$ and $G_2$ are cumulative distribution functions}@}.
> - (d) The correct choice is: {@{$F_2/F_1$ can be a CDF for some valid pairs $(F_1,F_2)$, but fails the CDF axioms for other pairs}@}. For a positive example, let {@{$F_1=\Phi$ be the standard normal CDF and set $F_2=\Phi^2$}@}; then {@{$u\mapsto u^2$ is increasing on $[0,1]$, so $F_2$ is a CDF and $G_3=F_2/F_1=\Phi$ is also a CDF}@}. For a negative example, take {@{$F_2=F_1$}@}; then {@{$G_3\equiv1$, which is not a CDF because its limit at $-\infty$ is $1$ instead of $0$}@}. So {@{$F_2/F_1$ can be a CDF in some cases, but it need not be one}@}. <!--SR:!2026-05-15,17,302!2026-05-19,17,302!2026-05-15,17,302!2026-05-19,17,302!2026-05-16,14,290!2026-05-16,14,290!2026-05-19,17,302!2026-05-15,17,302!2026-05-19,17,302!2026-05-17,15,290!2026-05-19,17,302!2026-05-14,16,290!2026-05-15,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-17,15,290!2026-05-15,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-16,14,290!2026-05-19,17,302!2026-05-15,17,302-->

<!-- markdownlint MD028 -->

> Let $Y\colon(\Omega,\mathcal{F},P)\to(\mathbb{R},\mathcal{B}(\mathbb{R}))$ be a continuously distributed random variable.
>
> - (a) Let $g\colon\mathbb{R}\to\mathbb{R}$ be a bijective $\mathcal{B}(\mathbb{R})$-$\mathcal{B}(\mathbb{R})$ measurable map. Can $g(Y)$ be a discrete random variable? Give a concrete example or prove why this is impossible.
> - (b) For the rest of the problem, assume $Y$ has density $f_Y(y)=\dfrac{3}{(1+y)^4}\mathbf{1}_{(0,\infty)}(y)$. Calculate the cumulative distribution function and probability density function of $Z=(1+Y)^{-1}$.
> - (c) Let $U=3Y$ if $Y\le1$ and $U=Y/3$ if $Y>1$. Calculate $P[U\ge1]$.
>
> Solution:
>
> - (a) No. If {@{$g(Y)$ were discrete}@}, then there would exist {@{a point $k\in\mathbb{R}$ with $P(g(Y)=k)>0$}@}. But since $g$ is {@{bijective, the event $\{g(Y)=k\}$ is exactly $\{Y=g^{-1}(k)\}$}@}, and a continuously distributed {@{random variable assigns probability $0$ to every singleton}@}. Hence {@{$P(g(Y)=k)=P(Y=g^{-1}(k))=0$}@}, a contradiction. So $g(Y)$ {@{cannot be discrete when $g$ is a measurable bijection and $Y$ is continuously distributed}@}.
> - (b) First integrate the density of $Y$: {@{$F_Y(y)=0$ for $y\le0$, while for $y>0$ one has $F_Y(y)=\int_0^y\frac{3}{(1+t)^4}\,dt=1-\frac{1}{(1+y)^3}$}@}. Since {@{$Z=(1+Y)^{-1}$ and $Y>0$ imply $0<Z\le1$}@}, the CDF of $Z$ is {@{$F_Z(z)=0$ for $z\le0$ and $F_Z(z)=1$ for $z\ge1$}@}. For $0<z<1$, {@{the monotone transformation gives $Z\le z\iff Y\ge z^{-1}-1$, hence $F_Z(z)=P(Y\ge z^{-1}-1)=1-F_Y(z^{-1}-1)=z^3$}@}. Therefore {@{$F_Z(z)=z^3$ on $(0,1)$}@}, and differentiating yields {@{the density $f_Z(z)=3z^2\mathbf{1}_{(0,1)}(z)$}@}.
> - (c) The event {@{$\{U\ge1\}$ splits according to the two branches of the definition of $U$}@}. On the $Y\le1$ branch, {@{$U=3Y$ so $U\ge1\iff Y\ge1/3$}@}; on the $Y>1$ branch, {@{$U=Y/3$ so $U\ge1\iff Y\ge3$}@}. So {@{$\{U\ge1\}=\{1/3\le Y\le1\}\cup\{Y\ge3\}$}@}. Using $F_Y$, {@{$F_Y(y)=1-(1+y)^{-3}$ for $y>0$ (and $0$ for $y\le0$)}@}, so {@{$P(1/3\le Y\le1)=\frac{19}{64}$ and $P(Y\ge3)=\frac{1}{64}$}@}. Hence {@{$P(U\ge1)=\frac{19}{64}+\frac{1}{64}=\frac{5}{16}$}@}. <!--SR:!2026-05-18,16,290!2026-05-19,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-18,16,290!2026-05-19,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-19,17,302!2026-05-15,17,302!2026-05-19,17,302!2026-05-17,15,290!2026-05-19,17,302!2026-05-17,15,290-->
