---
aliases:
    - HKUST MATH 2431 problem set 11
    - HKUST MATH2431 problem set 11
    - MATH 2431 problem set 11
    - MATH2431 problem set 11
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/problem_set_11
    - language/in/English
---

# problem set 11

- HKUST MATH 2431

The questions on this page summarize the _official problem-set materials_ for problem set 11.

- topics: convergence in probability; weak law of large numbers; Borel-Cantelli lemmas; convergence in distribution.

> 1.a. Convergence in probability. Let $X_n,Y_n$ be real random variables and let $X,Y$ be real limits. If $X_n\to X$ in probability and $Y_n\to Y$ in probability, show that $X_n+Y_n\to X+Y$ in probability.
>
> ---
>
> - solution: {@{The sum converges in probability, $X_n+Y_n\to X+Y$}@}
> - explanation: {@{The difference $(X_n+Y_n)-(X+Y)=(X_n-X)+(Y_n-Y)$}@} splits the sum. By {@{the triangle inequality}@}, {@{$|X_n-X|\le\varepsilon/2$ and $|Y_n-Y|\le\varepsilon/2$ together imply $|X_n+Y_n-(X+Y)|\le\varepsilon$}@}, so {@{the inclusion $$\{|X_n+Y_n-(X+Y)|>\varepsilon\}\subseteq\{|X_n-X|>\varepsilon/2\}\cup\{|Y_n-Y|>\varepsilon/2\}.$$}@} Hence {@{the bound $$P(|X_n+Y_n-(X+Y)|>\varepsilon)\le P(|X_n-X|>\varepsilon/2)+P(|Y_n-Y|>\varepsilon/2)\to0$$ holds as $n\to\infty$}@}, where each term {@{converges to $0$ by the definition of $X_n\to X$ and $Y_n\to Y$ in probability}@}. Thus {@{the sum $X_n+Y_n\to X+Y$ in probability}@}.

<!-- markdownlint MD028 -->

> 1.b. Convergence in probability. Let $X_n,Y_n$ be real random variables and let $X,Y$ be real limits. Let $a_n\to a$ in $\mathbb R$ and suppose $X_n\to x$ in probability for some constant $x$. Show that $a_nX_n\to ax$ in probability.
>
> ---
>
> - solution: {@{The product converges in probability, $a_nX_n\to ax$}@}
> - explanation: Write {@{the difference $a_nX_n-ax=a_n(X_n-x)+x(a_n-a)$}@}. Since {@{the sequence $a_n\to a$ is bounded}@}, {@{the bound $|a_n|\le M$ holds for all $n$ and some $M>0$}@}. For {@{any $\varepsilon>0$, the probability splits}@} as {@{the bound $$P(|a_nX_n-ax|>\varepsilon)\le P(|a_n||X_n-x|>\varepsilon/2)+P(|x||a_n-a|>\varepsilon/2).$$}@} The first term is {@{bounded by $P(|X_n-x|>\varepsilon/(2M))$}@}, which {@{converges to $0$ since $X_n\to x$ in probability}@}. For {@{the second term}@}, {@{$|x||a_n-a|\to0$ deterministically}@}, so for {@{all sufficiently large $n$ the bound $|x||a_n-a|<\varepsilon/2$ holds}@}, making that {@{probability $0$}@}. Hence {@{the probability $P(|a_nX_n-ax|>\varepsilon)\to0$, so $a_nX_n\to ax$ in probability}@}. <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2027-07-16T00:00:00.000Z,287,287.44288338,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 2.a. Weak law of large numbers. Let $X_1,X_2,\dots$ be iid with $X_1\sim E(1/2)$. Show that $$\frac1n\sum_{i=1}^n e^{-X_i/2}\to \frac12$$ in probability.
>
> ---
>
> - solution: {@{The average converges in probability to $1/2$}@}
> - explanation: {@{The variables $Y_i=e^{-X_i/2}$}@} are {@{iid, being measurable functions of iid $X_i$}@}. {@{The weak law applies provided $E[|Y_1|]<\infty$}@}, which holds since {@{$Y_1\ge0$ and bounded above by $1$}@}. Thus {@{the average $\frac1n\sum Y_i\to E[Y_1]$ converges in probability}@}. The mean is {@{the value $$E[e^{-X_1/2}]=\int_0^\infty e^{-x/2}\cdot\frac12 e^{-x/2}\,dx=\frac12\int_0^\infty e^{-x}\,dx=\frac12.$$}@} Hence {@{the average $\frac1n\sum_{i=1}^n e^{-X_i/2}\to\frac12$ in probability}@}.

<!-- markdownlint MD028 -->

> 2.b. Weak law of large numbers. Let $X_1,X_2,\dots$ be iid with density $f(x)=\frac16$ on $[0,2)$ and $f(x)=\frac13$ on $[2,4]$. Determine the constant $a$ such that $$\frac1n\sum_{k=1}^n \sqrt{X_k}\to a$$ in probability.
>
> ---
>
> - solution: {@{The constant is $a=\frac{2}{9}(8-\sqrt2)$}@}
> - explanation: Since {@{the variables $\sqrt{X_1},\dots,\sqrt{X_n}$ are iid with $E[\sqrt{X_1}]<\infty$ (bounded support)}@}, {@{the weak law gives $\frac1n\sum\sqrt{X_k}\to E[\sqrt{X_1}]$ in probability}@}. The constant is {@{the value $$a=E[\sqrt{X_1}]=\int_0^2\sqrt{x}\cdot\frac16\,dx+\int_2^4\sqrt{x}\cdot\frac13\,dx.$$}@} Using {@{the antiderivative $\int\sqrt x\,dx=\frac23 x^{3/2}$}@}, each piece evaluates as {@{the pair $$\begin{aligned} \frac16\int_0^2\sqrt x\,dx&=\frac16\cdot\frac23\bigl[x^{3/2}\bigr]_0^2=\frac19\cdot2^{3/2}=\frac{2\sqrt2}{9} \,, \\ \frac13\int_2^4\sqrt x\,dx&=\frac13\cdot\frac23\bigl[x^{3/2}\bigr]_2^4=\frac29(4^{3/2}-2^{3/2})=\frac29(8-2\sqrt2)=\frac{16-4\sqrt2}{9} \,, \end{aligned}$$}@}. Summing gives {@{the value $a=\frac{2\sqrt{2}+16-4\sqrt{2}}{9}={\frac{2}{9}(8-\sqrt{2})}$}@}, hence {@{the average $\frac1n\sum_{k=1}^n\sqrt{X_k}\to\frac{2}{9}(8-\sqrt2)$ in probability}@}. <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2027-07-16T00:00:00.000Z,287,287.44288338,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 3.a. Applications of the Borel-Cantelli lemmas. Let $(X_n)$ be iid exponential with parameter $\lambda$. Show that $$\limsup_{n\to\infty}\frac{X_n}{\log n}=\frac1\lambda \quad\text{a.s.}, \qquad \liminf_{n\to\infty}\frac{X_n}{\log n}=0 \quad\text{a.s.}$$
>
> ---
>
> - solution: {@{Both limits hold almost surely: $\limsup_{n\to\infty}\frac{X_n}{\log n}=\frac1\lambda$ and $\liminf_{n\to\infty}\frac{X_n}{\log n}=0$}@}
> - explanation: For $E(\lambda)$, {@{the tail is $P(X_n>t)=e^{-\lambda t}$ for $t>0$}@}. <br/>
>     __Upper bound.__ Fix {@{$\varepsilon>0$ and set $u_n=(1+\varepsilon)\frac{\log n}{\lambda}$}@}. Then {@{the pair $P(X_n>u_n)=e^{-\lambda u_n}=n^{-(1+\varepsilon)}$ and $\sum_{n=1}^\infty n^{-(1+\varepsilon)}<\infty$}@}. By {@{the first Borel-Cantelli lemma}@}, {@{the event $X_n>u_n$ occurs for only finitely many $n$ a.s.}@}, hence {@{the bound $\limsup_{n\to\infty}\frac{X_n}{\log n}\le\frac{1+\varepsilon}{\lambda}$ holds a.s.}@}, and since $\varepsilon>0$ is arbitrary, {@{the bound $\limsup_{n\to\infty}\frac{X_n}{\log n}\le\frac1\lambda$ holds a.s.}@}. <br/>
>     __Lower bound.__ Fix {@{$\varepsilon>0$ and set $\ell_n=(1-\varepsilon)\frac{\log n}{\lambda}$}@}. Then {@{the pair $P(X_n>\ell_n)=n^{-(1-\varepsilon)}$ and $\sum_{n=1}^\infty n^{-(1-\varepsilon)}=\infty$, a divergent $p$-series}@}. By {@{the second Borel-Cantelli lemma, which additionally requires independence}@}, {@{the event $X_n>\ell_n$ occurs for infinitely many $n$ a.s.}@}, so {@{the bound $\limsup_{n\to\infty}\frac{X_n}{\log n}\ge\frac{1-\varepsilon}{\lambda}$ holds a.s.}@}. Letting {@{the parameter $\varepsilon\downarrow0$}@} gives {@{the bound $\limsup_{n\to\infty}\frac{X_n}{\log n}\ge\frac1\lambda$ a.s.}@}. Combining both bounds gives {@{the common value $\limsup_{n\to\infty}\frac{X_n}{\log n}=1/\lambda$ a.s.}@}. <br/>
>     __Lower tail (liminf).__ Clearly {@{the bound $\frac{X_n}{\log n}\ge0$ holds a.s.}@}, so {@{the bound $\liminf\ge0$ holds a.s.}@}. For the reverse, fix {@{$\varepsilon>0$ and compute $$P\bigl(X_n<\varepsilon\log n\bigr)=1-e^{-\lambda\varepsilon\log n}=1-n^{-\lambda\varepsilon}.$$}@} For {@{any $\varepsilon>0$, the value $n^{-\lambda\varepsilon}\to0$}@}, so {@{the probability $P(X_n<\varepsilon\log n)\to1$ and $\sum_{n=1}^\infty P(X_n<\varepsilon\log n)=\infty$, since the terms do not vanish}@}. {@{The events $\{X_n<\varepsilon\log n\}$ are independent}@}, so by {@{the second Borel-Cantelli lemma they occur infinitely often a.s.}@}. Hence {@{the bound $\liminf_{n\to\infty}\frac{X_n}{\log n}\le\varepsilon$ holds a.s.}@}, and since {@{the parameter $\varepsilon>0$ is arbitrary}@}, {@{the value $\liminf_{n\to\infty}\frac{X_n}{\log n}=0$ holds a.s.}@}.

<!-- markdownlint MD028 -->

> 3.b. Applications of the Borel-Cantelli lemmas. Consider independent random variables with $P(X_1=0)=1$ and, for $n\ge 2$, $$P(X_n=n)=P(X_n=-n)=\frac{1}{2n\log n}, \qquad P(X_n=0)=1-\frac{1}{n\log n}.$$ Show that $\frac1n\sum_{i=1}^n X_i\to 0$ in probability but not almost surely.
>
> ---
>
> - solution: {@{The average $\frac1n\sum_{i=1}^n X_i\to0$ in probability but not almost surely}@}
> - explanation: __Convergence in probability.__ First {@{the mean $E[X_n]=0$ holds for all $n$}@} by symmetry. For $m\ge2$, {@{the variance is $\operatorname{Var}(X_m)=E[X_m^2]=m^2\cdot\frac{1}{m\log m}=\frac{m}{\log m}$, with $\operatorname{Var}(X_1)=0$}@}. By {@{Chebyshev's inequality}@}, {@{the bound $$P\!\left(\Bigl|\frac1n\sum_{i=1}^n X_i\Bigr|>\varepsilon\right)\le\frac{1}{n^2\varepsilon^2}\sum_{m=2}^n\frac{m}{\log m}$$ holds}@}. Splitting {@{the sum at $\lfloor\sqrt n\rfloor$}@} gives, for {@{$m\le\sqrt n$ the bound $\log m\ge\log2$ and for $m>\sqrt n$ the bound $\log m\ge\frac12\log n$}@}, {@{the bound $$\sum_{m=2}^n\frac{m}{\log m}\le\sum_{m=2}^{\lfloor\sqrt n\rfloor}\frac{m}{\log2}+\frac{2}{\log n}\sum_{m=\lfloor\sqrt n\rfloor+1}^n m\le\frac{n}{\log2}+\frac{2}{\log n}\cdot\frac{n^2}{2}=\frac{n}{\log2}+\frac{n^2}{\log n}.$$}@} Therefore {@{$$P\!\left(\Bigl|\frac1n\sum_{i=1}^n X_i\Bigr|>\varepsilon\right)\le\frac{1}{n^2\varepsilon^2}\!\left(\frac{n}{\log2}+\frac{n^2}{\log n}\right)=\frac{1}{n\varepsilon^2\log2}+\frac{1}{\varepsilon^2\log n}\to0$$ as $n\to\infty$}@}, hence {@{the average $\frac1n\sum_{i=1}^n X_i\to0$ in probability}@}. <br/>
>     __Non-convergence almost surely.__ Let {@{the event $A_n=\{|X_n|\ge n\}$}@}. Then {@{the probability $P(A_n)=\frac{1}{n\log n}$ for $n\ge2$, with $\sum_{n=2}^\infty\frac{1}{n\log n}=\infty$ by the integral test}@}. The $A_n$ are {@{independent, so the second Borel-Cantelli lemma applies}@}, giving {@{$P(A_n\text{ i.o.})=1$, i.e. $|X_n|\ge n$ for infinitely many $n$ a.s.}@}. Hence {@{the ratio $X_n/n\not\to0$ a.s.}@}. <br/>
>     Now suppose, {@{for contradiction, that $S_n/n:=\frac1n\sum_{i=1}^n X_i$ converges a.s. to some $c\in\mathbb R$}@}. Then {@{$S_{n-1}/(n-1)\to c$ a.s. as well (a subsequence of a convergent sequence) and $(n-1)/n\to1$}@}, so {@{the identity $$\frac{X_n}{n}=\frac{S_n}{n}-\frac{n-1}{n}\cdot\frac{S_{n-1}}{n-1}\longrightarrow c-1\cdot c=0 \quad\text{a.s.}$$}@} But {@{the divergence $X_n/n\not\to0$ a.s. contradicts that}@}. Therefore {@{the average $\frac1n\sum_{i=1}^n X_i$ does not converge a.s., in particular not to $0$}@}. <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2027-07-16T00:00:00.000Z,287,287.44288338,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2027-07-16T00:00:00.000Z,287,287.44288338,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2027-06-23T00:00:00.000Z,297,296.59855496,1,2,3,0,0,2026-08-30T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 4\. Convergence in distribution. Consider sequences of random variables with densities $$f_{X_n}(x)=\lambda\left(1-\frac{\lambda x}{n}\right)^{n-1}\mathbf 1_{[0,n/\lambda)}(x), \qquad f_{Y_n}(x)=\frac{n+1}{n}x^{1/n}\mathbf 1_{[0,1]}(x).$$ Determine the limit distributions.
>
> ---
>
> - solution: {@{The limits are $X_n\xrightarrow{d}E(\lambda)$ and $Y_n\xrightarrow{d}U([0,1])$}@}
> - explanation: The limit is read off {@{the CDFs, computed explicitly and then taken to $n\to\infty$}@}, and {@{using the densities directly is wrong}@}. <br/>
>     __For $X_n$:__ for $x<0$, {@{the value $F_{X_n}(x)=0$}@}. For {@{the range $0\le x<n/\lambda$}@}, integrating with {@{the antiderivative $\frac{d}{dt}[-(1-\lambda t/n)^n]=\lambda(1-\lambda t/n)^{n-1}$}@} gives {@{the value $$F_{X_n}(x)=\int_0^x\lambda\Bigl(1-\frac{\lambda t}{n}\Bigr)^{n-1}\!dt=\Bigl[-\Bigl(1-\frac{\lambda t}{n}\Bigr)^n\Bigr]_{t=0}^{t=x}=1-\Bigl(1-\frac{\lambda x}{n}\Bigr)^n.$$}@} For {@{$x\ge n/\lambda$, the value $F_{X_n}(x)=1$}@}. As {@{$n\to\infty$, the power $(1-\lambda x/n)^n\to e^{-\lambda x}$}@}, so {@{the limit $$F_{X_n}(x)\to\bigl(1-e^{-\lambda x}\bigr)\mathbf 1_{[0,\infty)}(x),$$}@} which is {@{the CDF of an $E(\lambda)$ distribution}@}, hence {@{the limit law $X_n\xrightarrow{d}E(\lambda)$}@}. <br/>
>     __For $Y_n$:__ for $x<0$, {@{the value $F_{Y_n}(x)=0$}@}. For {@{the range $0\le x<1$}@}, {@{the CDF is $$F_{Y_n}(x)=\int_0^x\frac{n+1}{n}t^{1/n}\,dt=\Bigl[t^{(n+1)/n}\Bigr]_{t=0}^{t=x}=x^{(n+1)/n}.$$}@} For {@{$x\ge1$, the value $F_{Y_n}(x)=1$}@}. Writing {@{the identity $x^{(n+1)/n}=x\cdot x^{1/n}$}@} and using {@{the limit $x^{1/n}\to1$ for $x>0$}@} gives {@{the limit $$F_{Y_n}(x)\to\begin{cases}0,&x<0,\\ x,&0\le x<1,\\ 1,&x\ge1,\end{cases}$$}@} which is {@{the CDF of a $U([0,1])$ distribution}@}, hence {@{the limit law $Y_n\xrightarrow{d}U([0,1])$}@}. <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2027-07-16T00:00:00.000Z,287,287.44288338,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->
