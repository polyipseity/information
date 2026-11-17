---
aliases:
    - HKUST MATH 2431 problem set 5
    - HKUST MATH2431 problem set 5
    - MATH 2431 problem set 5
    - MATH2431 problem set 5
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/problem_set_5
    - language/in/English
---

# problem set 5

- HKUST MATH 2431

The questions on this page summarize the _official problem-set materials_ for problem set 5. The official materials are paraphrased into study-note form while preserving the underlying questions and core solution ideas.

- topics: symmetric sigma-algebras; transformed densities; cumulative distribution functions; medians.

> 1.a. Symmetric sigma-algebra on two dice. Let $\Omega=\{1,\dots,6\}^2$, let $\mathcal F=\mathcal P(\Omega)$, and let $\mathcal F_{\mathrm{sym}}=\{A\subseteq\Omega:(\omega_1,\omega_2)\in A\iff (\omega_2,\omega_1)\in A\}$. When is $\mathcal F_{\mathrm{sym}}$ a natural modeling choice?
>
> ---
>
> - solution: {@{It is natural when the two coordinates are observationally indistinguishable}@}
> - explanation: {@{This sigma-algebra is natural when the two coordinates are observationally indistinguishable.}@}

<!-- markdownlint MD028 -->

> 1.b. Symmetric sigma-algebra on two dice. Let $\Omega=\{1,\dots,6\}^2$, let $\mathcal F=\mathcal P(\Omega)$, and let $\mathcal F_{\mathrm{sym}}=\{A\subseteq\Omega:(\omega_1,\omega_2)\in A\iff (\omega_2,\omega_1)\in A\}$. Show that it is a sigma-algebra.
>
> ---
>
> - solution: {@{The symmetric family $\mathcal F_{\mathrm{sym}}$ is a sigma-algebra}@}
> - explanation: It contains {@{the whole space $\Omega$}@}, and {@{the symmetry property is preserved}@} under {@{the operations of complements and countable unions}@}, so {@{the family $\mathcal F_{\mathrm{sym}}$ is a sigma-algebra}@}.

<!-- markdownlint MD028 -->

> 1.c. Symmetric sigma-algebra on two dice. Let $\Omega=\{1,\dots,6\}^2$, let $\mathcal F=\mathcal P(\Omega)$, and let $\mathcal F_{\mathrm{sym}}=\{A\subseteq\Omega:(\omega_1,\omega_2)\in A\iff (\omega_2,\omega_1)\in A\}$. Show that "one die shows $3$" belongs to $\mathcal F_{\mathrm{sym}}$ but "the blue die shows $3$" does not.
>
> ---
>
> - solution: {@{"One die shows $3$" is symmetric, while "the blue die shows $3$" is not}@}
> - explanation: {@{"One die shows $3$" is invariant under swapping the two coordinates, while "the blue die shows $3$" is not.}@}

<!-- markdownlint MD028 -->

> 1.d. Symmetric sigma-algebra on two dice. Let $\Omega=\{1,\dots,6\}^2$, let $\mathcal F=\mathcal P(\Omega)$, and let $\mathcal F_{\mathrm{sym}}=\{A\subseteq\Omega:(\omega_1,\omega_2)\in A\iff (\omega_2,\omega_1)\in A\}$. Decide whether $X(\omega_1,\omega_2)=\omega_1$ and $S(\omega_1,\omega_2)=\omega_1+\omega_2$ are random variables on $(\Omega,\mathcal F_{\mathrm{sym}})$.
>
> ---
>
> - solution: {@{The coordinate map $X$ is not a random variable, while the sum map $S$ is}@}
> - explanation: {@{The coordinate map $X$ is not measurable}@}, because {@{events like $\{X\le 1\}$ break the symmetry}@}, whereas {@{the sum map $S$ is measurable}@}, because {@{the condition $\omega_1+\omega_2\le a$ is symmetric}@}. <!--SR:!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 2.a. Bubble radius and transformed densities. Suppose first that $R\sim U([1,10])$ and $V=\frac{4\pi}{3}R^3$. Find the density of $V$.
>
> ---
>
> - solution: {@{The density is $f_V(v)=\frac{1}{9}\left(\frac{3}{4\pi}\right)^{1/3}v^{-2/3}$ on $\left[\frac{4\pi}{3},\frac{4000\pi}{3}\right]$ and $0$ outside}@}
> - explanation: Since {@{the map $v=\frac{4\pi}{3}r^3$ is increasing}@}, {@{the change-of-variables formula}@} gives {@{$f_V(v)=f_R(r(v))\,|dr/dv|$ with $r(v)=(3v/(4\pi))^{1/3}$}@}. <br/>
>     Then {@{the derivative is $dr/dv=\frac13(3/(4\pi))^{1/3}v^{-2/3}$}@}, and {@{$R\sim U([1,10])$ implies the constant density $f_R(r)=\frac19$}@}. <br/>
>     Hence {@{the density is $f_V(v)=\frac{1}{9}\left(\frac{3}{4\pi}\right)^{1/3}v^{-2/3}$ on $\left[\frac{4\pi}{3},\frac{4000\pi}{3}\right]$ and $0$ outside}@}.

<!-- markdownlint MD028 -->

> 2.b. Bubble radius and transformed densities. Suppose instead that $R\sim \ell N(\mu,\sigma^2)$. Find the density of $R$.
>
> ---
>
> - solution: {@{The density is $f_R(x)=\frac{1}{x\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(\log x-\mu)^2}{2\sigma^2}\right)\mathbf 1_{(0,\infty)}(x)$}@}
> - explanation: By definition {@{the variable is $R=e^Y$ with $Y\sim N(\mu,\sigma^2)$}@}. <br/>
>     Using {@{the change-of-variables formula}@} with {@{the map $Y=g(R)=\log R$, whose derivative is $g'(r)=1/r$}@} gives {@{the identity $f_R(r)=f_Y(g(r))\,|g'(r)|=\frac1r f_Y(\log r)$}@}. <br/>
>     Substituting {@{the normal density $f_Y(y)=\frac1{\sqrt{2\pi\sigma^2}}e^{-(y-\mu)^2/(2\sigma^2)}$}@} then gives {@{the density $f_R(x)=\frac{1}{x\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(\log x-\mu)^2}{2\sigma^2}\right)\mathbf 1_{(0,\infty)}(x)$}@}.

<!-- markdownlint MD028 -->

> 2.c. Bubble radius and transformed densities. Suppose $R\sim \ell N(\mu,\sigma^2)$. Show that the bubble volume $V=\frac{4\pi}{3}R^3$ and surface area $A=4\pi R^2$ are also lognormal, and identify their parameters.
>
> ---
>
> - solution: {@{Both $V$ and $A$ are lognormal, with $\log V\sim N\left(\log\frac{4\pi}{3}+3\mu,9\sigma^2\right)$ and $\log A\sim N\left(\log(4\pi)+2\mu,4\sigma^2\right)$}@}
> - explanation: By {@{the defining property of the lognormal}@}, {@{$R\sim\ell N(\mu,\sigma^2)$ means $\log R\sim N(\mu,\sigma^2)$}@}. <br/>
>     With {@{the logarithm $Y=\log R$}@}, taking logarithms gives {@{the identity $\log V = \log\frac{4\pi}{3} + 3\log R = \log\frac{4\pi}{3} + 3Y$}@}, {@{a linear transformation}@} of $Y$, so {@{the law is $\log V\sim N(\log\frac{4\pi}{3}+3\mu,\;9\sigma^2)$}@}. <br/> <!--SR:!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2028-04-02T00:00:00.000Z,525,524.82711532,1,2,4,0,0,2026-10-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-05-25T00:00:00.000Z,242,242.43601181,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z-->
>     Similarly {@{the area gives $\log A = \log(4\pi) + 2Y\sim N(\log(4\pi)+2\mu,\;4\sigma^2)$}@}. <br/>
>     By {@{the same defining property, that a normal logarithm makes the variable lognormal}@}, $V$ and $A$ are {@{lognormal with these parameters}@}.

<!-- markdownlint MD028 -->

> 3.a. Piecewise cumulative distribution functions and named examples. Let $X$ be a real random variable with CDF
>
> $$F_X(x)=\begin{cases} \frac14 e^{x+2}+c, & x<-2,\\[2pt] \frac12+\frac x8, & -2\le x<0,\\[2pt] \frac{2+x}{3+x}, & 0\le x<5,\\[2pt] (\lambda-1)e^x+1, & x\ge5. \end{cases}$$
>
> Determine the constants $c,\lambda$ from the CDF axioms.
>
> ---
>
> - solution: {@{The constants are $c=0$ and $\lambda=1$}@}
> - explanation: {@{The limit $\lim_{x\to-\infty}F_X(x)=0$}@} forces {@{the first piece to vanish}@}, so {@{the constant is $c=0$}@}. <br/>
>     {@{The limit $\lim_{x\to\infty}F_X(x)=1$}@} forces {@{the coefficient $(\lambda-1)$ to be $0$}@}, so {@{the constant is $\lambda=1$}@}.

<!-- markdownlint MD028 -->

> 3.b. Piecewise cumulative distribution functions and named examples. Let $X$ be a real random variable with CDF
>
> $$F_X(x)=\begin{cases} \frac14 e^{x+2}+c, & x<-2,\\[2pt] \frac12+\frac x8, & -2\le x<0,\\[2pt] \frac{2+x}{3+x}, & 0\le x<5,\\[2pt] (\lambda-1)e^x+1, & x\ge5. \end{cases}$$
>
> Compute $P(0\le X<5)$ and $P(-2<X\le5)$.
>
> ---
>
> - solution: {@{The two probabilities are $P(0\le X<5)=\frac38$ and $P(-2<X\le5)=\frac34$}@}
> - explanation: For {@{the event $0\le X<5$}@} the left limits are needed: {@{$F_X(5-)=\frac78$ and $F_X(0-)=\frac12$}@}, hence {@{the first probability is $P(0\le X<5)=\frac38$}@}. <br/>
>     For {@{the event $-2<X\le5$}@}: {@{$F_X(5)=1$ and $F_X(-2)=\frac14$}@}, hence {@{the second probability is $P(-2<X\le5)=\frac34$}@}.

<!-- markdownlint MD028 -->

> 3.c. Piecewise cumulative distribution functions and named examples. Calculate the CDF of $X\sim\operatorname{Bin}(4,\tfrac14)$ and draw a sketch.
>
> ---
>
> - solution: {@{The CDF is $F_X(x)=0$ for $x<0$, $0.316$ for $x\in[0,1)$, $0.738$ for $x\in[1,2)$, $0.949$ for $x\in[2,3)$, $0.996$ for $x\in[3,4)$, and $1$ for $x\ge4$}@}
> - explanation: {@{For the binomial law $X\sim\operatorname{Bin}(4,\tfrac14)$, the CDF is $F_X(x)=\sum_{0\le k\le\min\{4,x\}}\binom4k\Big(\frac14\Big)^k\Big(\frac34\Big)^{4-k}$, which evaluates to the staircase $$F_X(x)=\begin{cases} 0, & x<0,\\ 0.316, & x\in[0,1),\\ 0.738, & x\in[1,2),\\ 0.949, & x\in[2,3),\\ 0.996, & x\in[3,4),\\ 1, & x\ge4. \end{cases}$$}@}

<!-- markdownlint MD028 -->

> 3.d. Piecewise cumulative distribution functions and named examples. Calculate the CDF of $Y\sim\operatorname{Cau}(1,2)$ and draw a sketch, where $\operatorname{Cau}(\mu,a)$ is the Cauchy distribution with density $f_Y(y)=\frac{a}{\pi(a^2+(y-\mu)^2)}$, $y\in\mathbb R$.
>
> ---
>
> - solution: {@{The CDF is $F_Y(y)=\dfrac1\pi\left(\arctan\dfrac{y-1}{2}+\dfrac\pi2\right)$}@}
> - explanation: {@{The CDF comes from integrating the density in four steps, $$\begin{aligned} F_Y(y)&=\int_{-\infty}^y\frac{2}{\pi(4+(t-1)^2)}\,dt\\ &=\frac1{2\pi}\int_{-\infty}^y\frac{1}{1+\big(\frac{t-1}{2}\big)^2}\,dt\\ &=\frac1\pi\Big[\arctan\Big(\frac{t-1}{2}\Big)\Big]_{-\infty}^y\\ &=\frac1\pi\Big(\arctan\frac{y-1}{2}+\frac\pi2\Big). \end{aligned}$$}@} <!--SR:!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-05-25T00:00:00.000Z,242,242.43601181,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z!fsrs,2027-10-27T00:00:00.000Z,397,396.77501923,1,2,3,0,0,2026-09-25T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 4.a. Medians of distribution functions. Show that the median condition $\lim_{y\uparrow m}F(y)\le \tfrac12\le F(m)$ is equivalent to $P([m,\infty))\ge\frac12$ and $P((-\infty,m])\ge\frac12$, where $P$ is the probability measure associated with $F$.
>
> ---
>
> - solution: {@{The median condition is equivalent to both $P((-\infty,m])\ge\frac12$ and $P([m,\infty))\ge\frac12$}@}
> - explanation: By {@{the definition of the CDF}@}, {@{the left mass is $P((-\infty,m])=F(m)$}@}, so {@{that mass satisfies $P((-\infty,m])\ge\frac12\iff F(m)\ge\frac12$}@}. <br/>
>     For {@{the right-side mass}@}, write {@{the identity $P([m,\infty))=1-P((-\infty,m))$}@}. <br/>
>     Since {@{$P((-\infty,m))=\lim_{y\uparrow m}F(y)$, the left limit of the CDF}@}, we get {@{the chain $P([m,\infty))\ge\frac12\iff 1-\lim_{y\uparrow m}F(y)\ge\frac12\iff \lim_{y\uparrow m}F(y)\le\frac12$}@}. <br/>
>     Hence {@{the median condition}@} is equivalent to {@{both $P((-\infty,m])\ge\frac12$ and $P([m,\infty))\ge\frac12$}@}.

<!-- markdownlint MD028 -->

> 4.b. Medians of distribution functions. Show that every distribution function has at least one median.
>
> ---
>
> - solution: {@{Every distribution function has at least one median}@}
> - explanation: Let {@{the set $A=\{x\in\mathbb R:F(x)<\frac12\}$ and its supremum $\alpha=\sup A$}@}. <br/>
>     Since {@{$\lim_{x\to-\infty}F(x)=0<\frac12$, the set $A$ is nonempty}@}, and since {@{the right limit $\lim_{x\to\infty}F(x)=1>\frac12$}@}, $A$ is {@{bounded above, so $\alpha\in\mathbb R$ exists}@}. <br/>
>     First, show {@{the left limit $\lim_{y\uparrow\alpha}F(y)\le\frac12$}@}: pick {@{a sequence $\alpha_n\in A$ with $\alpha_n\uparrow\alpha$}@}. <br/>
>     Because $F$ is {@{non-decreasing, $F(\alpha_n)<\frac12$ for all $n$}@}, {@{the limit satisfies $\lim_{y\uparrow\alpha}F(y)=\lim_{n\to\infty}F(\alpha_n)\le\frac12$}@}. <br/>
>     Second, show {@{the value satisfies $F(\alpha)\ge\frac12$}@}: suppose {@{not, so that $F(\alpha)<\frac12$}@}. <br/>
>     {@{Right-continuity of $F$ and completeness of the reals}@} then give {@{some $\varepsilon>0$ such that $F(x)<\frac12$ for all $x\in(\alpha,\alpha+\varepsilon)$}@}. <br/>
>     Those {@{$x$ belong to $A$, contradicting $\alpha=\sup A$}@}, hence {@{the value $F(\alpha)\ge\frac12$}@}. <br/>
>     Thus $\alpha$ satisfies {@{the median condition and is a median}@}.

<!-- markdownlint MD028 -->

> 4.c. Medians of distribution functions. Show that the set of medians of $F$ is a closed interval of $\mathbb R$.
>
> ---
>
> - solution: {@{The medians form the closed interval $[\alpha,\beta]$}@}
> - explanation: Let {@{the value be $\beta=\sup\{x\in\mathbb R:F(x)\le\frac12\}$}@}, {@{the last point where the CDF is still $\le\frac12$}@}. <br/>
>     {@{_Medians are contained in $[\alpha,\beta]$<!-- LaTeX separator -->_}@}: if {@{$m$ is a median}@}, then {@{the value satisfies $F(m)\ge\frac12$}@}, so {@{$m\notin A$ and therefore $m\ge\sup A=\alpha$}@}. <br/>
>     If {@{a point satisfies $m>\beta$}@}, choose {@{$\varepsilon=(m-\beta)/2>0$; then $F(\beta+\varepsilon)>\frac12$}@} (since {@{the inequality $\beta+\varepsilon>\beta$ holds}@}), and by {@{monotonicity $\lim_{y\uparrow m}F(y)\ge F(\beta+\varepsilon)>\frac12$}@}, contradicting {@{the median condition, so $m\le\beta$}@}. <br/>
>     {@{_Every $m\in[\alpha,\beta]$ is a median_}@}: if {@{the median $m$ lies in $[\alpha,\beta]$}@}, then {@{$m\ge\alpha$ implies $F(m)\ge\frac12$}@} (otherwise {@{$m\in A$ would contradict $\alpha=\sup A$}@}). <br/>
>     For {@{each point $y<m\le\beta$}@}, {@{$F(y)\le\frac12$, so $\lim_{y\uparrow m}F(y)\le\frac12$}@}. <br/>
>     Thus $m$ {@{satisfies the condition $(\star)$}@}. <br/>
>     Therefore {@{the full set of medians is $[\alpha,\beta]$}@}.
