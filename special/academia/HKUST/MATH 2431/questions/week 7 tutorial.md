---
aliases:
    - HKUST MATH 2431 week 7 tutorial
    - HKUST MATH2431 week 7 tutorial
    - MATH 2431 week 7 tutorial
    - MATH2431 week 7 tutorial
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/week_7_tutorial
    - language/in/English
---

# week 7 tutorial

- HKUST MATH 2431

The questions on this page summarize the _official tutorial materials_ for week 7. Because they come from course materials rather than repository-authored review prompts, each question is kept as a markdown quote block and the clozes live inside that quoted Q&A block.

- topics: measurable functions; random variables; laws of random variables; measurable transformations.

> Prove the half-line criterion: $X\colon\Omega\to\mathbb{R}$ is a random variable iff $\{X\le x\}\in\mathcal{F}$ for every $x\in\mathbb{R}$, and extend the statement to any generating family $\mathcal{E}$ with $\sigma(\mathcal{E})=\mathcal{B}(\mathbb{R})$.
>
> Solution: We prove the two directions separately. Forward direction: if $X$ is already a random variable, then by definition $X^{-1}(B)\in\mathcal F$ for every Borel set $B$. In particular, since $(-\infty,x]$ is Borel, we have $\{X\le x\}=X^{-1}(( -\infty,x])\in\mathcal F$. Reverse direction: assume that $\{X\le x\}\in\mathcal F$ for every $x\in\mathbb R$. Define {@{the class $\mathcal G:=\{A\subseteq\mathbb R:X^{-1}(A)\in\mathcal F\}$}@}. Then {@{this class $\mathcal G$ is a sigma-algebra on $\mathbb R$ because preimages preserve complements and countable unions}@}. By assumption {@{every left half-line belongs to $\mathcal G$}@}, and since left half-lines {@{generate $\mathcal B(\mathbb R)$}@}, we obtain {@{the inclusion $\mathcal B(\mathbb R)\subseteq\mathcal G$}@}. Therefore $X^{-1}(B)\in\mathcal F$ for every Borel set $B$, so {@{$X$ is a random variable}@}. More generally, if $\mathcal E$ satisfies {@{$\sigma(\mathcal E)=\mathcal B(\mathbb R)$}@} and $X^{-1}(E)\in\mathcal F$ for every $E\in\mathcal E$, then the same argument shows that it is enough to check preimages of {@{any generating family of the Borel sigma-algebra}@}. <!--SR:!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270-->

<!-- markdownlint MD028 -->

> Verify that the law $P_X[A]=P[X\in A]$ of an $(S,\mathcal{S})$-valued random variable is a probability measure on $(S,\mathcal{S})$.
>
> Solution: Check the measure axioms directly: {@{non-negativity is inherited from $P$}@}, normalization is {@{the identity $P_X(S)=P(X\in S)=P(\Omega)=1$}@}, and for {@{pairwise disjoint sets}@} $(A_i)\subseteq\mathcal S$ we have {@{the preimages $X^{-1}(A_i)$ pairwise disjoint in $\mathcal F$}@}, so {@{countable additivity becomes $P_X(\bigcup_iA_i)=P(\bigcup_iX^{-1}(A_i))=\sum_iP(X^{-1}(A_i))=\sum_iP_X(A_i)$}@}. Therefore {@{$P_X$ is a probability measure}@}. <!--SR:!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270-->

<!-- markdownlint MD028 -->

> If $f\colon(\Omega,\mathcal{F})\to(G,\mathcal{G})$ and $g\colon(G,\mathcal{G})\to(H,\mathcal{H})$ are measurable, prove that $g\circ f$ is measurable.
>
> Solution: For arbitrary $A\in\mathcal H$, measurability of $g$ gives {@{the first preimage condition $g^{-1}(A)\in\mathcal G$}@}, and then measurability of $f$ gives {@{the second preimage condition $f^{-1}(g^{-1}(A))\in\mathcal F$}@}. Using {@{the identity $(g\circ f)^{-1}(A)=f^{-1}(g^{-1}(A))$}@}, every measurable target set has measurable preimage under $g\circ f$, so {@{$g\circ f$ is measurable}@}. This is exactly why measurability is {@{closed under composition}@}. <!--SR:!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270-->

<!-- markdownlint MD028 -->

> Light-intensity model: if $\theta\sim\mathrm{U}(( -\pi/2,\pi/2))$ and $X=a\tan\theta$, show that $X$ has density $\dfrac{a}{\pi(a^2+x^2)}$.
>
> Solution: Since $x=a\tan\theta$ is {@{strictly increasing on $( -\pi/2,\pi/2)$}@}, the {@{CDF method}@} gives {@{the formula $F_X(x)=P(X\le x)=P(\theta\le\arctan(x/a))=(\arctan(x/a)+\pi/2)/\pi$}@}, and hence {@{the density $f_X(x)=\frac{a}{\pi(a^2+x^2)}$}@}. Equivalently, one can use the {@{inverse-derivative formula}@} with inverse {@{the inverse map $\theta(x)=\arctan(x/a)$ and derivative $\left|d\theta/dx\right|=a/(a^2+x^2)$}@}. <!--SR:!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270-->

<!-- markdownlint MD028 -->

> Let $\Omega=\{1,2,3,4,5,6\}$, $\mathcal{F}=\{\varnothing,\Omega,\{1,2\},\{3,4,5,6\}\}$, and $P(\{1,2\})=p$. Define $X(\omega)=1$ for $\omega=1,2$ and $X(\omega)=-1$ otherwise; define $Y(\omega)=1$ for $\omega=1,2,3$ and $Y(\omega)=0$ otherwise. Decide whether $X$ and $Y$ are random variables, and find the distribution function when it exists.
>
> Solution: For $X$, the relevant preimages are $X^{-1}(\{1\})=\{1,2\}$ and $X^{-1}(\{-1\})=\{3,4,5,6\}$, both in $\mathcal F$, so {@{$X$ is measurable}@}. Its law is therefore given by $P(X=1)=p$ and $P(X=-1)=1-p$, which yields {@{the cumulative distribution function $F_X(x)=0$ for $x<-1$, $F_X(x)=1-p$ for $-1\le x<1$, and $F_X(x)=1$ for $x\ge1$}@}. For $Y$, the preimage $Y^{-1}(\{1\})=\{1,2,3\}$ is not in $\mathcal F$, so {@{$Y$ is not measurable}@}. <!--SR:!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270-->

<!-- markdownlint MD028 -->

> If $(X_j)_{j\ge 1}$ is a sequence of random variables, show that $\inf_j X_j$ and $\sup_j X_j$ are random variables.
>
> Solution: By the {@{half-line criterion}@}, it is enough to show that events of the form $\{Y\le x\}$ are measurable. For $Y=\sup_jX_j$, the event $\{\sup_jX_j\le x\}$ means {@{every $X_j\le x$}@}, so {@{the event identity is $\{\sup_jX_j\le x\}=\bigcap_{j\ge1}\{X_j\le x\}$}@}. For $Y=\inf_jX_j$, the event $\{\inf_jX_j\le x\}$ means {@{at least one $X_j\le x$}@}, so {@{the event identity is $\{\inf_jX_j\le x\}=\bigcup_{j\ge1}\{X_j\le x\}$}@}. Since each $\{X_j\le x\}$ lies in $\mathcal F$ and sigma-algebras are closed under countable intersections and unions, {@{$\inf_j X_j$ and $\sup_j X_j$ are random variables}@}. <!--SR:!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270!2026-04-12,4,270-->
