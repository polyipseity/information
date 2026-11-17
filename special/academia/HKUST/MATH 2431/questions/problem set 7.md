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

> 1.a. Expectation of transformed random variables. Start with 1 dollar, toss a coin with head probability $p$ for $n$ rounds, and double the amount after each head. If $X$ is the final amount, compute $E[X]$ and $\operatorname{Var}(X)$.
>
> ---
>
> - solution: {@{$E[X]=(1+p)^n$ and $\operatorname{Var}(X)=(1+3p)^n-(1+p)^{2n}$}@}
> - explanation: Let {@{$Y\sim \operatorname{Bin}(n,p)$ count the heads}@}, so {@{the final amount is $X=2^Y$}@}. Using {@{the binomial moment generating function}@}, {@{the first moment is $E[X]=E[2^Y]=\psi_Y(\log2)=(1-p+pe^{\log2})^n = (1+p)^n$}@} and {@{the second moment is $E[X^2]=E[4^Y]=\psi_Y(\log4)=(1-p+4p)^n = (1+3p)^n$}@}, hence {@{the variance is $\operatorname{Var}(X)=E[X^2]-(E[X])^2=(1+3p)^n-(1+p)^{2n}$}@}.

<!-- markdownlint MD028 -->

> 1.b. Expectation of transformed random variables. Pick a point uniformly on the upper semicircle and let $A$ be the area of the triangle with vertices $(0,0)$, $(1,0)$, and that point. Compute $E[A]$ and $\operatorname{Var}(A)$.
>
> ---
>
> - solution: {@{The mean is $E[A]=1/\pi$ and the variance is $\operatorname{Var}(A)=1/8-1/\pi^2$}@}
> - explanation: Parametrize {@{the point as $(\cos\Phi,\sin\Phi)$ with $\Phi\sim U([0,\pi])$}@}. The area of the triangle is {@{the value $A=\frac12|\det((1,0),(\cos\Phi,\sin\Phi))| = \frac12\sin\Phi$}@}. Then {@{the mean is $E[A]=\frac12\int_0^\pi\sin\Phi\cdot\frac1\pi\,d\Phi = 1/\pi$}@} and {@{the second moment is $E[A^2]=\frac14\int_0^\pi\sin^2\Phi\cdot\frac1\pi\,d\Phi = 1/8$}@}, hence {@{the variance is $\operatorname{Var}(A)=E[A^2]-(E[A])^2=1/8-1/\pi^2$}@}. <!--SR:!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 2.a. Markov and Chebyshev inequalities. A coin with $P(\text{heads})=1/3$ is tossed $200$ times. Bound the probability of getting at least $120$ heads using Markov, then improve it using Chebyshev.
>
> ---
>
> - solution: {@{Markov gives $P(X\ge 120)\le 5/9$ and Chebyshev gives $P(X\ge 120)\le 1/64$}@}
> - explanation: With {@{$X\sim \operatorname{Bin}(200,1/3)$ counting the heads}@}, {@{the mean is $E[X]=200/3$ and the variance is $\operatorname{Var}(X)=200\cdot\frac13\cdot\frac23=400/9$}@}. <br/>
>     Markov gives {@{the bound $P(X\ge 120)\le\dfrac{E[X]}{120}=\dfrac{200/3}{120} = 5/9$}@}. <br/>
>     Chebyshev starts from {@{the event $X\ge120\iff X-200/3\ge160/3$}@}, so {@{the bound is $$P(X\ge120)\le P(|X-200/3|\ge160/3)\le\frac{\operatorname{Var}(X)}{(160/3)^2}=\frac{400/9}{25600/9}=1/64.$$}@}

<!-- markdownlint MD028 -->

> 2.b. Markov and Chebyshev inequalities. Give an example where Chebyshev's inequality is attained with equality.
>
> ---
>
> - solution: {@{Chebyshev is attained with equality when $X$ is uniform on $\{-1,0,1\}$ and $a=1$, where $E[X]=0$, $\operatorname{Var}(X)=2/3$ and $P(|X|\ge1)=2/3$}@}
> - explanation: {@{Chebyshev attains equality when $X$ takes only $\mu$ and $\mu\pm a$ with $P(|X-\mu|\ge a)=\operatorname{Var}(X)/a^2$; for example, $X$ uniform on $\{-1,0,1\}$ with $a=1$ has $E[X]=0$, $\operatorname{Var}(X)=2/3$ and $P(|X|\ge1)=2/3=\frac{\operatorname{Var}(X)}{1^2}$.}@} <!--SR:!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 3.a. Chernoff bounds. Show that for $t>0$, $P(X\ge a)\le e^{-ta}\psi_X(t)$, and for $t<0$, $P(X\le a)\le e^{-ta}\psi_X(t)$.
>
> ---
>
> - solution: {@{For $t>0$, $P(X\ge a)\le e^{-ta}\psi_X(t)$; for $t<0$, $P(X\le a)\le e^{-ta}\psi_X(t)$}@}
> - explanation: {@{For $t>0$, Markov's inequality applied to $e^{tX}$ gives $$P(X\ge a)=P(e^{tX}\ge e^{ta})\le e^{-ta}E[e^{tX}] = e^{-ta}\psi_X(t) \,,$$ and for $t<0$ the lower-tail analogue gives $P(X\le a)\le e^{-ta}\psi_X(t)$.}@}

<!-- markdownlint MD028 -->

> 3.b. Chernoff bounds. Compute the moment generating function of $N(0,1)$.
>
> ---
>
> - solution: {@{$\psi_X(t)=e^{t^2/2}$}@}
> - explanation: {@{The moment generating function is $$\psi_X(t)=\frac1{\sqrt{2\pi}}\int_{-\infty}^\infty e^{tx-x^2/2}\,dx=e^{t^2/2}\cdot\frac1{\sqrt{2\pi}}\int_{-\infty}^\infty e^{-(x-t)^2/2}\,dx = e^{t^2/2} \,.$$}@}

<!-- markdownlint MD028 -->

> 3.c. Chernoff bounds. Deduce Gaussian tail bounds.
>
> ---
>
> - solution: {@{For $a>0$, the upper tail obeys $P(X\ge a)\le e^{-a^2/2}$}@}
> - explanation: Combining {@{the bound with $t>0$ and the normal moment generating function $e^{t^2/2}$}@} gives {@{$P(X\ge a)\le e^{-ta+t^2/2}$ for every $t>0$}@}. Minimize {@{the exponent $f(t)=-ta+t^2/2$}@}: {@{the derivative $f'(t)=-a+t=0$ gives $t=a$}@}, so {@{the tail bound is $P(X\ge a)\le e^{-a^2/2}$ for $a>0$}@}. <!--SR:!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 4.a. Joint distributions. Decide whether each of the two candidate functions below can be a joint CDF, and when valid, find the marginal CDFs.
>
> $$\begin{aligned} \text{i.}\quad &F(x,y)= \begin{cases} 1-e^{-x-y}, & x,y\ge0,\\ 0, & \text{otherwise}, \end{cases}\\[4pt] \text{ii.}\quad &F(x,y)= \begin{cases} 1-e^{-x}-xe^{-y}, & 0\le x\le y,\\ 1-e^{-y}-ye^{-y}, & 0\le y\le x,\\ 0, & \text{otherwise}. \end{cases} \end{aligned}$$
>
> ---
>
> - solution: {@{Candidate (i) is not a joint CDF, while candidate (ii) is valid with marginals $F_X(x)=1-e^{-x}$ and $F_Y(y)=1-e^{-y}-ye^{-y}$}@}
> - explanation: __Candidate (i):__ {@{The mixed partial derivative}@} is {@{the value $$\frac{\partial^2F}{\partial x\partial y}=-e^{-x-y}<0\quad(x,y>0),$$}@} so {@{the increment over a rectangle can be negative}@}, and thus it is {@{not a valid joint CDF}@}. <br/>
>     __Candidate (ii):__ It is easy to check that {@{the limits at infinities are correct and that it is _jointly_ right-continuous}@}. <br/>
>     Differentiating {@{the first case ($0\le x\le y$)}@} gives {@{the pair $$\frac{\partial F}{\partial x}=e^{-x}-e^{-y},\qquad f(x,y)=\frac{\partial^2F}{\partial x\partial y}=e^{-y}\ge0.$$}@} On {@{the other range $0\le y\le x$}@}, $F$ {@{does not depend on $x$, so $f=0$}@}. <br/>
>     Hence {@{the density is $f(x,y)=e^{-y}\mathbf1_{0\le x\le y}$}@}, which {@{integrates to $1$ — valid}@}. The marginal CDFs are {@{$F_X(x)=\lim_{y\to\infty}F(x,y)=1-e^{-x}$ for $x\ge0$}@} and {@{$F_Y(y)=\lim_{x\to\infty}F(x,y)=1-e^{-y}-ye^{-y}$ for $y\ge0$}@}.

<!-- markdownlint MD028 -->

> 4.b. Joint distributions. Let $$p_{X,Y}(j,k)=C\,2^{-k}\mathbf1_{\{1\le j<k\}}.$$ Find $C$ and the marginals.
>
> ---
>
> - solution: {@{The constant is $C=1$, and the marginals are $p_X(j)=2^{-j}$ for $j\ge1$ and $p_Y(k)=(k-1)2^{-k}$ for $k\ge2$}@}
> - explanation: The support is {@{the set $\{1\le j<k\}$}@}. {@{Swapping the order of summation}@} gives {@{the value $\sum_{j=1}^\infty\sum_{k=j+1}^\infty C2^{-k}=C\sum_{j=1}^\infty2^{-j}=C\cdot1=1$}@}, so {@{the constant is $C=1$}@}. The marginals are {@{$p_X(j)=\sum_{k=j+1}^\infty2^{-k}=2^{-j}$ for $j\ge1$}@} and {@{$p_Y(k)=\sum_{j=1}^{k-1}2^{-k}=(k-1)2^{-k}$ for $k\ge2$}@}. <!--SR:!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z-->
