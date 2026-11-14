---
aliases:
    - HKUST MATH 2431 practice midterm examination
    - HKUST MATH2431 practice midterm examination
    - MATH 2431 practice midterm examination
    - MATH2431 practice midterm examination
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/practice_midterm_examination
    - language/in/English
---

# practice midterm examination

- HKUST MATH 2431

The question blocks on this page summarize the _official practice problems for the midterm exam_. The accompanying official midterm-guidelines sheet says that the midterm covers Sessions 1-11 (Weeks 1-6; Chapters 1 - Section 5.2 in the notes; problem sets 1-5), except the proof of Theorem 4.17 (Dynkin's pi-lambda theorem), Formula (4.61) (the pseudoinverse definition), Remark 4.20 (iii) on singular continuous distributions, Definition 5.5 and Example 5.6 on equality in law, and Problem 2 on Problem Set 5.

- topics: convex combinations of probability measures; transformations of cumulative distribution functions; measurable bijections; transformation of continuous random variables.

> 1.a. Let $(\Omega,\mathcal{F})$ be a measurable space, and let $P_1$ and $P_2$ be probability measures on it. Show that, for $\lambda\in[0,1]$, the set function $Q_\lambda[A]=\lambda P_1[A]+(1-\lambda)P_2[A]$ is a probability measure on $(\Omega,\mathcal{F})$.
>
> ---
>
> - solution: {@{$Q_\lambda$ is a probability measure}@}
> - explanation: For $\lambda\in[0,1]$ the coefficients are {@{nonnegative and sum to $1$}@}. <br/>
>     Nonnegativity gives {@{$Q_\lambda[A]\ge0$ for every $A\in\mathcal{F}$}@}, and {@{normalization gives $Q_\lambda[\Omega]=\lambda P_1[\Omega]+(1-\lambda)P_2[\Omega]=1$}@}. <br/>
>     For pairwise disjoint $(A_j)$ {@{countable additivity carries over, since $Q_\lambda[\bigcup_jA_j]=\lambda\sum_jP_1[A_j]+(1-\lambda)\sum_jP_2[A_j]=\sum_jQ_\lambda[A_j]$}@}.

<!-- markdownlint MD028 -->

> 1.b. On the same measurable space, with two probability measures $P_1\neq P_2$, now let $\lambda<0$. Give an explicit example of $(\Omega,\mathcal{F})$ and of such a pair for which the same formula still defines a probability measure, or prove that this is impossible.
>
> ---
>
> - solution: {@{An example exists, so the formula can still define a probability measure}@}
> - explanation: Take {@{$\Omega=\{0,1\}$, $\mathcal{F}=\mathcal{P}(\Omega)$, and $P_2(\{0\})=P_2(\{1\})=1/2$}@}, and pick any $\varepsilon$ with {@{$0<\varepsilon\le1/(2|\lambda|)$, so the negative coefficient cannot push a singleton mass below $0$}@}. <br/>
>     Define {@{$P_1(\{0\})=1/2+\varepsilon$ and $P_1(\{1\})=1/2-\varepsilon$}@}. <br/>
>     Then {@{$Q_\lambda(\{0\})=1/2+\lambda\varepsilon$ and $Q_\lambda(\{1\})=1/2-\lambda\varepsilon$}@}, and {@{$|\lambda|\varepsilon\le1/2$ keeps both values inside $[0,1]$}@}.

<!-- markdownlint MD028 -->

> 1.c. Suppose $F_1$ and $F_2$ are cumulative distribution functions. Decide whether $G_1=\tfrac12(F_1+F_2)$ and $G_2=\sqrt{F_1F_2}$ are cumulative distribution functions.
>
> ---
>
> - solution: {@{Both $G_1$ and $G_2$ are cumulative distribution functions}@}
> - explanation: Each construction preserves {@{monotonicity, right continuity, and the endpoint limits $0$ at $-\infty$ and $1$ at $+\infty$}@}. <br/>
>     For $G_1$ this is {@{an average of two nondecreasing right-continuous functions, which keeps the three CDF properties}@}. <br/>
>     For $G_2$, the product $F_1F_2$ is {@{nondecreasing because both factors are nondecreasing and lie in $[0,1]$}@}, and {@{multiplying by a nondecreasing factor together with $x\mapsto\sqrt{x}$ keeps right continuity and the endpoint limits}@}.

<!-- markdownlint MD028 -->

> 1.d. Assume now that $F_1(x)>0$ for all $x\in\mathbb{R}$. Decide, with proof or examples, whether $G_3=F_2/F_1$ is always a cumulative distribution function, never a cumulative distribution function, or sometimes but not always a cumulative distribution function.
>
> ---
>
> - solution: {@{Sometimes, but not always}@}
> - explanation: For a positive example take {@{$F_1=\Phi$, the standard normal CDF, and $F_2=\Phi^2$}@}; then {@{$u\mapsto u^2$ is increasing on $[0,1]$, so $F_2$ is a CDF and $G_3=F_2/F_1=\Phi$ is one too}@}. <br/>
>     For a negative example {@{take $F_2=F_1$}@}; then {@{$G_3\equiv1$, which fails because its limit at $-\infty$ is $1$ instead of $0$}@}.

<!-- markdownlint MD028 -->

> 2.a. Let $Y\colon(\Omega,\mathcal{F},P)\to(\mathbb{R},\mathcal{B}(\mathbb{R}))$ be a continuously distributed random variable, and let $g\colon\mathbb{R}\to\mathbb{R}$ be a bijective $\mathcal{B}(\mathbb{R})$-$\mathcal{B}(\mathbb{R})$ measurable map. Can $g(Y)$ be a discrete random variable? Give a concrete example or prove why this is impossible.
>
> ---
>
> - solution: {@{No, $g(Y)$ cannot be discrete}@}
> - explanation: If $g(Y)$ were {@{discrete}@}, some point $k$ {@{would carry positive probability $P(g(Y)=k)>0$}@}. <br/>
>     Bijectivity makes that event {@{exactly $\{Y=g^{-1}(k)\}$}@}, and continuous $Y$ {@{assigns probability $0$ to every singleton}@}. <br/>
>     {@{So $P(g(Y)=k)=P(Y=g^{-1}(k))=0$}@}, which is {@{a contradiction}@}.

<!-- markdownlint MD028 -->

> 2.b. Let $Y$ have density $f_Y(y)=\dfrac{3}{(1+y)^4}\mathbf{1}_{(0,\infty)}(y)$. Calculate the cumulative distribution function and probability density function of $Z=(1+Y)^{-1}$.
>
> ---
>
> - solution: {@{$F_Z(z)=z^3$ on $(0,1)$ and $f_Z(z)=3z^2\mathbf{1}_{(0,1)}(z)$}@}
> - explanation: Integrating the density of $Y$ {@{gives $F_Y(y)=0$ for $y\le0$ and $F_Y(y)=\int_0^y\frac{3}{(1+t)^4}\,dt=1-\frac{1}{(1+y)^3}$ for $y>0$}@}. <br/>
>     Since {@{$Z=(1+Y)^{-1}$ with $Y>0$ gives $0<Z\le1$}@}, the CDF {@{satisfies $F_Z(z)=0$ for $z\le0$ and $F_Z(z)=1$ for $z\ge1$}@}. <br/>
>     For $0<z<1$ {@{the monotone transformation gives $Z\le z\iff Y\ge z^{-1}-1$, so $F_Z(z)=1-F_Y(z^{-1}-1)=z^3$}@}. <br/>
>     Differentiating {@{gives $f_Z(z)=3z^2$ on $(0,1)$}@}.

<!-- markdownlint MD028 -->

> 2.c. Let $Y$ have density $f_Y(y)=\dfrac{3}{(1+y)^4}\mathbf{1}_{(0,\infty)}(y)$, and let $U=3Y$ if $Y\le1$ and $U=Y/3$ if $Y>1$. Calculate $P[U\ge1]$.
>
> ---
>
> - solution: {@{$P[U\ge1]=\frac{5}{16}$}@}
> - explanation: The event splits along {@{the two branches of the definition of $U$}@}: on $Y\le1$, {@{$U=3Y$ so $U\ge1\iff Y\ge1/3$}@}, and on $Y>1$, {@{$U=Y/3$ so $U\ge1\iff Y\ge3$}@}. <br/>
>     {@{Hence $\{U\ge1\}=\{1/3\le Y\le1\}\cup\{Y\ge3\}$}@}, and with {@{$F_Y(y)=1-(1+y)^{-3}$ for $y>0$}@} this gives {@{$P(1/3\le Y\le1)=\frac{19}{64}$ and $P(Y\ge3)=\frac{1}{64}$}@}.
