---
aliases:
    - HKUST MATH 2431 problem set 6
    - HKUST MATH2431 problem set 6
    - MATH 2431 problem set 6
    - MATH2431 problem set 6
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/problem_set_6
    - language/in/English
---

# problem set 6

- HKUST MATH 2431

The questions on this page summarize the _official problem-set materials_ for problem set 6. The official materials are paraphrased into study-note form while preserving the underlying questions and core solution ideas.

- topics: moments; gamma distribution; tail-sum identities; hazard rates; expectation tricks.

> 1.a. Expectation, variance, and higher moments. Let $X$ have density $f(x)=\dfrac{c}{(1+x)^5}\mathbf 1_{(0,\infty)}(x)$. Find $c$, the CDF, $E[X]$, $\operatorname{Var}(X)$, and the largest integer $n$ for which $E[X^n]$ exists.
>
> ---
>
> - solution: {@{$c=4$, $F_X(x)=1-(1+x)^{-4}$ on $x\ge0$, $E[X]=1/3$, $\operatorname{Var}(X)=2/9$, and the largest integer with $E[X^n]$ finite is $n=3$}@}
> - explanation: Integrating {@{the normalization $\int_0^\infty\frac{c}{(1+x)^5}\,dx=\frac{c}{4}=1$}@} gives {@{the constant $c=4$}@}. <br/>
>     The CDF is {@{the value $F_X(x)=0$ for $x<0$}@} and {@{then $F_X(x)=1-(1+x)^{-4}$ for $x\ge0$}@}. <br/>
>     {@{The mean $E[X]=\int_0^\infty 4x(1+x)^{-5}\,dx$}@} follows by rewriting {@{$4x(1+x)^{-5}=4[(1+x)^{-4}-(1+x)^{-5}]$ and integrating}@}, which gives {@{the value $E[X]=1/3$}@}. <br/>
>     {@{The second moment $E[X^2]=\int_0^\infty 4x^2(1+x)^{-5}\,dx$}@} yields under {@{the substitution $t=\frac{x}{1+x}$}@} (so {@{$x=\frac{t}{1-t}$ and $dx=\frac{dt}{(1-t)^2}$}@}), which simplifies {@{the integrand to $t^2(1-t)$, giving $\int_0^\infty x^2(1+x)^{-5}\,dx=\int_0^1 t^2(1-t)\,dt$}@}. <br/>
>     {@{The Beta function}@} is {@{the identity $B(a,b)=\int_0^1 t^{a-1}(1-t)^{b-1}\,dt=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$}@}; here {@{the identity $t^2(1-t)=t^{3-1}(1-t)^{2-1}$}@} holds, so the integral equals {@{the value $B(3,2)=\frac{\Gamma(3)\Gamma(2)}{\Gamma(5)}=\frac{2!\cdot1!}{4!}=\frac1{12}$}@}. <br/>
>     Hence {@{the value $E[X^2]=4\cdot\frac1{12}=1/3$}@}, and thus {@{the variance $\operatorname{Var}(X)=E[X^2]-(E[X])^2=2/9$}@}. <br/>
>     Finally {@{the moment $E[X^n]$ exists}@} iff {@{the integral $\int_0^\infty \frac{x^n}{(1+x)^5}\,dx$ converges at $\infty$, i.e. $n<4$}@}, so {@{the largest integer is $n=3$}@}.

<!-- markdownlint MD028 -->

> 1.b. Expectation, variance, and higher moments. Let $X\sim \Gamma(\alpha,\lambda)$ in the course parameterization (density $\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}$). Verify normalization and compute $E[X]$ and $\operatorname{Var}(X)$.
>
> ---
>
> - solution: {@{The density integrates to $1$, and the moments are $E[X]=\alpha/\lambda$ and $\operatorname{Var}(X)=\alpha/\lambda^2$}@}
> - explanation: {@{Normalization}@} follows from {@{the identity $\int_0^\infty x^{\alpha-1}e^{-\lambda x}\,dx = \frac{\Gamma(\alpha)}{\lambda^\alpha}$}@}, which makes {@{the density integrate to $1$}@}. <br/>
>     Then {@{the mean is $E[X]=\frac{\lambda^\alpha}{\Gamma(\alpha)}\int_0^\infty x^\alpha e^{-\lambda x}\,dx=\frac{\Gamma(\alpha+1)}{\Gamma(\alpha)\lambda}=\alpha/\lambda$}@}, and similarly {@{the second moment is $E[X^2]=\frac{\Gamma(\alpha+2)}{\Gamma(\alpha)\lambda^2}=\frac{(\alpha+1)\alpha}{\lambda^2}$}@}, so {@{the variance is $\operatorname{Var}(X)=E[X^2]-(E[X])^2=\alpha/\lambda^2$}@}. <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 2.a. Properties of the expectation. For an $\mathbb N$-valued random variable $X$, show that $E[X]=\sum_{n=1}^\infty P(X\ge n)$, and use this for $X\sim \operatorname{Geo}(p)$.
>
> ---
>
> - solution: {@{The identity $E[X]=\sum_{n=1}^\infty P(X\ge n)$ holds, and for $X\sim\operatorname{Geo}(p)$ it gives $E[X]=1/p$}@}
> - explanation: Write {@{the indicator identity $X=\sum_{n=1}^\infty\mathbf 1_{\{X\ge n\}}$}@}, then {@{take expectation and interchange sum and expectation}@} (by {@{Tonelli, since the summands are nonnegative}@}) to get {@{the expectation $E[X]=\sum_{n\ge 1}P(X\ge n)$}@}. <br/>
>     For $\operatorname{Geo}(p)$, {@{the tail $P(X\ge n)=\sum_{k=n}^\infty (1-p)^{k-1}p = (1-p)^{n-1}$}@}, so {@{the mean is $E[X]=\sum_{n=1}^\infty (1-p)^{n-1} = \sum_{k=0}^\infty (1-p)^k = \frac{1}{1-(1-p)} = 1/p$}@}.

<!-- markdownlint MD028 -->

> 2.b. Properties of the expectation. For a nonnegative real random variable $X$, show that $E[X]=\int_0^\infty (1-F_X(x))\,dx$, and use this for $X\sim \operatorname{Exp}(\lambda)$.
>
> ---
>
> - solution: {@{The identity $E[X]=\int_0^\infty (1-F_X(x))\,dx$ holds, and for $X\sim\operatorname{Exp}(\lambda)$ it gives $E[X]=1/\lambda$}@}
> - explanation: Write {@{the indicator identity $X=\int_0^\infty \mathbf 1_{\{X> x\}}\,dx$, true for nonnegative $X$}@}, then {@{take expectation and swap integral and expectation by Tonelli}@} to get {@{the identity $E[X]=\int_0^\infty P(X>x)\,dx = \int_0^\infty (1-F_X(x))\,dx$}@}. <br/>
>     For $\operatorname{Exp}(\lambda)$ the CDF is {@{the value $F_X(x)=1-e^{-\lambda x}$}@}, so {@{$1-F_X(x)=e^{-\lambda x}$ and the integral $\int_0^\infty e^{-\lambda x}\,dx = 1/\lambda$}@}. <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 3.a. Hazard rate. We model the lifetime of a device by a continuously distributed random variable $T\ge0$ with CDF $F(t)$ and PDF $f(t)$ (continuous for all $t\ge0$). The hazard rate is defined as $$\lambda(t)=\lim_{h\searrow0}\frac{P[t\le T\le t+h\mid T\ge t]}{h},\qquad t\ge0$$ (this is also relevant for life-insurance purposes). Express $\lambda(t)$ in terms of $f(t)$ and $F(t)$.
>
> ---
>
> - solution: {@{The hazard rate is $\lambda(t)=f(t)/(1-F(t))$}@}
> - explanation: From {@{the definition of the hazard rate through the conditional probability}@}, {@{the ratio rewrites as $\lambda(t)=\lim_{h\searrow0}\frac{P[t\le T\le t+h\mid T\ge t]}{h} =\lim_{h\searrow0}\frac{P[t\le T\le t+h]}{h\,P(T\ge t)}$}@}, and {@{the chain continues as $\frac1{1-F(t)}\lim_{h\searrow0}\frac{F(t+h)-F(t)}{h} =\frac{f(t)}{1-F(t)}$}@}, which leaves {@{the formula $\lambda(t)=f(t)/(1-F(t))$}@}.

<!-- markdownlint MD028 -->

> 3.b. Hazard rate. We model the lifetime of a device by a continuously distributed random variable $T\ge0$ with CDF $F(t)$ and PDF $f(t)$ (continuous for all $t\ge0$). The hazard rate is defined as $$\lambda(t)=\lim_{h\searrow0}\frac{P[t\le T\le t+h\mid T\ge t]}{h},\qquad t\ge0$$ (this is also relevant for life-insurance purposes). Suppose $T\sim\operatorname{Exp}(\alpha)$ with $\alpha>0$ and compute $\lambda(t)$.
>
> ---
>
> - solution: {@{The hazard rate is the constant $\lambda(t)=\alpha$}@}
> - explanation: For the exponential law, {@{the density is $f(t)=\alpha e^{-\alpha t}$ and the survival function is $1-F(t)=e^{-\alpha t}$}@}, so {@{the ratio is $\lambda(t)=\frac{f(t)}{1-F(t)}=\frac{\alpha e^{-\alpha t}}{e^{-\alpha t}}=\alpha$}@}, i.e. the hazard rate is {@{the constant rate $\alpha$}@}; this encodes {@{memorylessness}@}.

<!-- markdownlint MD028 -->

> 3.c. Hazard rate. We model the lifetime of a device by a continuously distributed random variable $T\ge0$ with CDF $F(t)$ and PDF $f(t)$ (continuous for all $t\ge0$). The hazard rate is defined as $$\lambda(t)=\lim_{h\searrow0}\frac{P[t\le T\le t+h\mid T\ge t]}{h},\qquad t\ge0$$ (this is also relevant for life-insurance purposes). Verify that $F(t)=1-\exp\!\big(-\int_0^t\lambda(s)\,ds\big)$ when $t\ge0$.
>
> ---
>
> - solution: {@{The survival formula holds, $F(t)=1-\exp\left(-\int_0^t\lambda(s)\,ds\right)$ for $t\ge0$}@}
> - explanation: From {@{the identity $\lambda(t)=\frac{f(t)}{1-F(t)} = -\frac{d}{dt}\log(1-F(t))$}@}, integrating over $\int_0^t$ gives {@{the identity $-\int_0^t\lambda(s)\,ds = \log(1-F(t))-\log(1-F(0))$}@}. <br/>
>     With {@{the value $F(0)=0$}@}, {@{the logarithm is $\log(1-F(t))=-\int_0^t\lambda(s)\,ds$}@}, and exponentiating gives {@{the claim $F(t)=1-\exp\left(-\int_0^t \lambda(s)\,ds\right)$}@}.

<!-- markdownlint MD028 -->

> 3.d. Hazard rate. We model the lifetime of a device by a continuously distributed random variable $T\ge0$ with CDF $F(t)$ and PDF $f(t)$ (continuous for all $t\ge0$). The hazard rate is defined as $$\lambda(t)=\lim_{h\searrow0}\frac{P[t\le T\le t+h\mid T\ge t]}{h},\qquad t\ge0$$ (this is also relevant for life-insurance purposes). Compute $F(t)$ and $f(t)$ for $t\ge0$ when $\lambda(t)=\alpha t^\gamma$ ($\alpha,\gamma>0$) (Weibull distribution).
>
> ---
>
> - solution: {@{The law is $F(t)=1-\exp\left(-\frac{\alpha}{\gamma+1}t^{\gamma+1}\right)$ with density $f(t)=\alpha t^\gamma\exp\left(-\frac{\alpha}{\gamma+1}t^{\gamma+1}\right)$}@}
> - explanation: Substituting {@{the rate $\lambda(t)=\alpha t^\gamma$ into $F(t)=1-\exp\left(-\int_0^t\lambda(s)\,ds\right)$}@} gives {@{the integral $\int_0^t \alpha s^\gamma\,ds = \frac{\alpha}{\gamma+1}t^{\gamma+1}$}@}, so {@{the CDF is $F(t)=1-\exp\left(-\frac{\alpha}{\gamma+1}t^{\gamma+1}\right)$, a Weibull-type law}@}. <br/>
>     Differentiating gives {@{the density $f(t)=F'(t)=\alpha t^\gamma\exp\left(-\frac{\alpha}{\gamma+1}t^{\gamma+1}\right)$}@}.

<!-- markdownlint MD028 -->

> 3.e. Hazard rate. We model the lifetime of a device by a continuously distributed random variable $T\ge0$ with CDF $F(t)$ and PDF $f(t)$ (continuous for all $t\ge0$). The hazard rate is defined as $$\lambda(t)=\lim_{h\searrow0}\frac{P[t\le T\le t+h\mid T\ge t]}{h},\qquad t\ge0$$ (this is also relevant for life-insurance purposes). Show that $E[T]=\int_0^\infty\exp\!\big(-\int_0^t\lambda(s)\,ds\big)\,dt$.
>
> ---
>
> - solution: {@{The expectation is $E[T]=\int_0^\infty\exp\left(-\int_0^t\lambda(s)\,ds\right)dt$}@}
> - explanation: {@{The survival function of the law}@} is {@{the value $1-F(t)=\exp\left(-\int_0^t\lambda(s)\,ds\right)$}@}, and plugging that expression into {@{the tail-sum identity for nonnegative variables, $E[T]=\int_0^\infty (1-F(t))\,dt$}@} gives {@{the claim $E[T]=\int_0^\infty \exp\left(-\int_0^t\lambda(s)\,ds\right)dt$}@}. <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> 4.a. More expectation tricks. For a uniform random permutation of $\{1,\dots,n\}$, let $X$ be the number of fixed points. Find $E[X]$.
>
> ---
>
> - solution: {@{The expected number of fixed points is $E[X]=1$}@}
> - explanation: Let {@{$A_i$ be the event that $i$ is fixed}@}; there are {@{$(n-1)!$ permutations fixing $i$ out of $n!$ total}@}, so {@{the probability is $P(A_i)=(n-1)!/n! = 1/n$}@}. <br/>
>     Since {@{the count is $X=\sum_{i=1}^n\mathbf 1_{A_i}$}@}, {@{linearity gives $E[X]=n\cdot\frac1n=1$}@}.

<!-- markdownlint MD028 -->

> 4.b. More expectation tricks. A company counts a day as a holiday if at least one worker has a birthday on that day. For which workforce size is the expected number of worker-days maximized?
>
> ---
>
> - solution: {@{The expected worker-days are maximized at the workforce size $n=364$ or $n=365$}@}
> - explanation: Let {@{$S$ be the number of birthday-free days}@}. <br/>
>     For {@{a fixed day}@}, the probability {@{no one has a birthday is $(364/365)^n$}@}, so by {@{linearity of expectation $E[S]=365(364/365)^n$}@}. <br/>
>     {@{The expected working days equal $E[S]$}@}, so {@{the expected worker-days are $n\cdot E[S]$}@}. <br/>
>     With {@{the sequence $a_n=365n(364/365)^n$}@}, {@{the ratio is $\frac{a_{n+1}}{a_n}=\frac{n+1}{n}\cdot\frac{364}{365}$}@}, so $a_n$ {@{increases while $\frac{n+1}{n}>\frac{365}{364}$, i.e. $n<364$, and decreases afterward}@}, giving {@{the maximum at $n=364$ or $n=365$ (they are equal)}@}. <!--SR:!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2027-07-16T00:00:00.000Z,287,287.44288338,1,2,3,0,0,2026-10-02T00:00:00.000Z!fsrs,2028-01-14T00:00:00.000Z,469,468.69043243,1,2,3,0,0,2026-10-02T00:00:00.000Z-->
