---
aliases:
    - HKUST MATH 2431 problem set 7
    - HKUST MATH2431 problem set 7
    - MATH 2431 problem set 7
    - MATH2431 problem set 7
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/problem_set_7
    - language/in/English
---
# problem set 7

- HKUST MATH 2431

The questions on this page summarize the _official problem-set materials_ for problem set 7.

- topics: transformed expectations; Markov and Chebyshev inequalities; Chernoff bounds; joint distributions.

> Expectation of transformed random variables.
>
> - (a) Start with 1 dollar, toss a coin with head probability $p$ for $n$ rounds, and double the amount after each head. If $X$ is the final amount, compute $E[X]$ and $\operatorname{Var}(X)$.
> - (b) Pick a point uniformly on the upper semicircle and let $A$ be the area of the triangle with vertices $(0,0)$, $(1,0)$, and that point. Compute $E[A]$ and $\operatorname{Var}(A)$.
>
> Solution:
>
> - (a) Let {@{$Y\sim \operatorname{Bin}(n,p)$ count the heads}@}, so {@{$X=2^Y$}@}. Using {@{the binomial MGF}@}: {@{$E[X]=E[2^Y]=\psi_Y(\log2)=(1-p+pe^{\log2})^n = (1+p)^n$}@}; {@{$E[X^2]=E[4^Y]=\psi_Y(\log4)=(1-p+4p)^n = (1+3p)^n$}@}; hence {@{$\operatorname{Var}(X)=E[X^2]-(E[X])^2=(1+3p)^n-(1+p)^{2n}$}@}.
> - (b) Parametrize the point as {@{$(\cos\Phi,\sin\Phi)$ with $\Phi\sim U([0,\pi])$}@}. The area is {@{$A=\frac12|\det((1,0),(\cos\Phi,\sin\Phi))| = \frac12\sin\Phi$}@}. Then {@{$E[A]=\frac12\int_0^\pi\sin\Phi\cdot\frac1\pi\,d\Phi = 1/\pi$}@}; {@{$E[A^2]=\frac14\int_0^\pi\sin^2\Phi\cdot\frac1\pi\,d\Phi = 1/8$}@}; hence {@{$\operatorname{Var}(A)=E[A^2]-(E[A])^2=1/8-1/\pi^2$}@}. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Markov and Chebyshev inequalities.
>
> - (a) A coin with $P(\text{heads})=1/3$ is tossed $200$ times. Bound the probability of getting at least $120$ heads using Markov, then improve it using Chebyshev.
> - (b) Give an example where Chebyshev's inequality is attained with equality.
>
> Solution:
>
> - (a) {@{$X\sim \operatorname{Bin}(200,1/3)$}@}, so {@{$E[X]=200/3$ and $\operatorname{Var}(X)=200\cdot\frac13\cdot\frac23=400/9$}@}. <p> Markov: {@{$P(X\ge 120)\le\dfrac{E[X]}{120}=\dfrac{200/3}{120} = 5/9$}@}. <br/> Chebyshev: {@{$X\ge120\iff X-200/3\ge160/3$}@}, so {@{$$P(X\ge120)\le P(|X-200/3|\ge160/3)\le\frac{\operatorname{Var}(X)}{(160/3)^2}=\frac{400/9}{25600/9}=1/64.$$}@}
> - (b) Chebyshev attains equality when {@{$X$ takes only $\mu$ and $\mu\pm a$ with $P(|X-\mu|\ge a)=\operatorname{Var}(X)/a^2$}@}. For example, take $X$ {@{uniform on $\{-1,0,1\}$ with $a=1$}@}: {@{$$E[X]=0,\quad\operatorname{Var}(X)=2/3,\quad P(|X|\ge1)=2/3=\frac{\operatorname{Var}(X)}{1^2}.$$}@} <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Chernoff bounds.
>
> - (a) Show that for $t>0$, $P(X\ge a)\le e^{-ta}\psi_X(t)$, and for $t<0$, $P(X\le a)\le e^{-ta}\psi_X(t)$.
> - (b) Compute the moment generating function of $N(0,1)$.
> - (c) Deduce Gaussian tail bounds.
>
> Solution:
>
> - (a) For $t>0$, apply {@{Markov to $e^{tX}$}@}: {@{$$P(X\ge a)=P(e^{tX}\ge e^{ta})\le e^{-ta}E[e^{tX}] = e^{-ta}\psi_X(t) \,.$$}@} For $t<0$, {@{the lower-tail analogue gives $P(X\le a)\le e^{-ta}\psi_X(t)$}@}.
> - (b) For $X\sim N(0,1)$: {@{$$\psi_X(t)=\frac1{\sqrt{2\pi}}\int_{-\infty}^\infty e^{tx-x^2/2}\,dx=e^{t^2/2}\cdot\frac1{\sqrt{2\pi}}\int_{-\infty}^\infty e^{-(x-t)^2/2}\,dx = e^{t^2/2} \,.$$}@}
> - (c) From (a) and (b): {@{$P(X\ge a)\le e^{-ta+t^2/2}$ for $t>0$}@}. Minimize {@{$f(t)=-ta+t^2/2$: $f'(t)=-a+t=0\Rightarrow t=a$}@}, giving {@{$$P(X\ge a)\le e^{-a^2/2}$$ for $a>0$}@}. <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Joint distributions.
>
> - (a) Decide whether each of the two candidate functions below can be a joint CDF, and when valid, find the marginal CDFs.
>
> $$\begin{aligned} \text{i.}\quad &F(x,y)= \begin{cases} 1-e^{-x-y}, & x,y\ge0,\\ 0, & \text{otherwise}, \end{cases}\\[4pt] \text{ii.}\quad &F(x,y)= \begin{cases} 1-e^{-x}-xe^{-y}, & 0\le x\le y,\\ 1-e^{-y}-ye^{-y}, & 0\le y\le x,\\ 0, & \text{otherwise}. \end{cases} \end{aligned}$$
>
> - (b) Let $$p_{X,Y}(j,k)=C\,2^{-k}\mathbf1_{\{1\le j<k\}}.$$ Find $C$ and the marginals.
>
> Solution:
>
> - (a) __Candidate (i):__ {@{The mixed partial derivative}@} is {@{$$\frac{\partial^2F}{\partial x\partial y}=-e^{-x-y}<0\quad(x,y>0),$$}@} so {@{the increment over a rectangle can be negative}@}. Thus it is {@{not a valid joint CDF}@}. <p> __Candidate (ii):__ It is easy to check that {@{the limits at infinities are correct and that it is _jointly_ right-continuous}@}. <p> Differentiating {@{the first case ($0\le x\le y$)}@}: {@{$$\frac{\partial F}{\partial x}=e^{-x}-e^{-y},\qquad f(x,y)=\frac{\partial^2F}{\partial x\partial y}=e^{-y}\ge0.$$}@} On {@{$0\le y\le x$}@}, $F$ {@{does not depend on $x$, so $f=0$}@}. Hence {@{$f(x,y)=e^{-y}\mathbf1_{0\le x\le y}$}@}, which {@{integrates to $1$ — valid}@}. Marginal CDFs: {@{$$F_X(x)=\lim_{y\to\infty}F(x,y)=1-e^{-x}\;(x\ge0),$$}@} {@{$$F_Y(y)=\lim_{x\to\infty}F(x,y)=1-e^{-y}-ye^{-y}\;(y\ge0).$$}@}
> - (b) The support is {@{$\{1\le j<k\}$}@}. {@{Swap sum order}@}: {@{$\sum_{j=1}^\infty\sum_{k=j+1}^\infty C2^{-k}=C\sum_{j=1}^\infty2^{-j}=C\cdot1=1$}@}, so {@{$C=1$}@}. Marginals: {@{$$p_X(j)=\sum_{k=j+1}^\infty2^{-k}=2^{-j}\;(j\ge1),$$}@} {@{$$p_Y(k)=\sum_{j=1}^{k-1}2^{-k}=(k-1)2^{-k}\;(k\ge2).$$}@} <!--SR:!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-07-21T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-13T00:00:00.000Z-->
