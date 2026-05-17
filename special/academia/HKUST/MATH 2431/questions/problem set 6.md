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

> Expectation, variance, and higher moments.
>
> - (a) Let $X$ have density $f(x)=\dfrac{c}{(1+x)^5}\mathbf 1_{(0,\infty)}(x)$. Find $c$, the CDF, $E[X]$, $\operatorname{Var}(X)$, and the largest integer $n$ for which $E[X^n]$ exists.
> - (b) Let $X\sim \Gamma(\alpha,\lambda)$ in the course parameterization (density $\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}$). Verify normalization and compute $E[X]$ and $\operatorname{Var}(X)$.
>
> Solution:
>
> - (a) Integrating {@{$\int_0^\infty\frac{c}{(1+x)^5}\,dx=\frac{c}{4}=1$}@} gives {@{$c=4$}@}. <p> The CDF is {@{$F_X(x)=0$ for $x<0$}@} and {@{$F_X(x)=1-(1+x)^{-4}$ for $x\ge0$}@}. <p> {@{$E[X]=\int_0^\infty 4x(1+x)^{-5}\,dx$}@}; rewriting {@{$4x(1+x)^{-5}=4[(1+x)^{-4}-(1+x)^{-5}]$ and integrating}@} gives {@{$E[X]=1/3$}@}. <p> {@{$E[X^2]=\int_0^\infty 4x^2(1+x)^{-5}\,dx$}@}; {@{the substitution $t=\frac{x}{1+x}$}@} (so {@{$x=\frac{t}{1-t}$, $dx=\frac{dt}{(1-t)^2}$}@}) simplifies {@{the integrand to $t^2(1-t)$, giving $\int_0^\infty x^2(1+x)^{-5}\,dx=\int_0^1 t^2(1-t)\,dt$}@}. {@{The Beta function}@} is {@{$B(a,b)=\int_0^1 t^{a-1}(1-t)^{b-1}\,dt=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$}@}; here {@{$t^2(1-t)=t^{3-1}(1-t)^{2-1}$}@}, so the integral equals {@{$B(3,2)=\frac{\Gamma(3)\Gamma(2)}{\Gamma(5)}=\frac{2!\cdot1!}{4!}=\frac1{12}$}@}. Hence {@{$E[X^2]=4\cdot\frac1{12}=1/3$}@}; hence {@{$\operatorname{Var}(X)=E[X^2]-(E[X])^2=2/9$}@}. <p> {@{$E[X^n]$ exists}@} iff {@{$\int_0^\infty \frac{x^n}{(1+x)^5}\,dx$ converges at $\infty$, i.e. $n<4$}@}, so {@{the largest integer is $n=3$}@}.
> - (b) {@{Normalization}@} follows from {@{$\int_0^\infty x^{\alpha-1}e^{-\lambda x}\,dx = \frac{\Gamma(\alpha)}{\lambda^\alpha}$}@}. Then {@{$E[X]=\frac{\lambda^\alpha}{\Gamma(\alpha)}\int_0^\infty x^\alpha e^{-\lambda x}\,dx=\frac{\Gamma(\alpha+1)}{\Gamma(\alpha)\lambda}=\alpha/\lambda$}@}; similarly {@{$E[X^2]=\frac{\Gamma(\alpha+2)}{\Gamma(\alpha)\lambda^2}=\frac{(\alpha+1)\alpha}{\lambda^2}$}@}, so {@{$\operatorname{Var}(X)=\alpha/\lambda^2$}@}. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Properties of the expectation.
>
> - (a) For an $\mathbb N$-valued random variable $X$, show that $E[X]=\sum_{n=1}^\infty P(X\ge n)$, and use this for $X\sim \operatorname{Geo}(p)$.
> - (b) For a nonnegative real random variable, show that $E[X]=\int_0^\infty (1-F_X(x))\,dx$, and use this for $X\sim \operatorname{Exp}(\lambda)$.
>
> Solution:
>
> - (a) Write {@{$X=\sum_{n=1}^\infty\mathbf 1_{\{X\ge n\}}$}@}, take {@{expectation, and interchange sum and expectation}@} (by {@{Tonelli, since summands are nonnegative}@}) to get {@{$E[X]=\sum_{n\ge 1}P(X\ge n)$}@}. <p> For $\operatorname{Geo}(p)$, {@{$P(X\ge n)=\sum_{k=n}^\infty (1-p)^{k-1}p = (1-p)^{n-1}$}@}, so {@{$E[X]=\sum_{n=1}^\infty (1-p)^{n-1} = \sum_{k=0}^\infty (1-p)^k = \frac{1}{1-(1-p)} = 1/p$}@}.
> - (b) Write {@{$X=\int_0^\infty \mathbf 1_{\{X> x\}}\,dx$ (true for nonnegative $X$)}@}, take {@{expectation, and swap integral and expectation (Tonelli)}@} to get {@{$E[X]=\int_0^\infty P(X>x)\,dx = \int_0^\infty (1-F_X(x))\,dx$}@}. <p> For $\operatorname{Exp}(\lambda)$, {@{$F_X(x)=1-e^{-\lambda x}$}@}, so {@{$1-F_X(x)=e^{-\lambda x}$ and $\int_0^\infty e^{-\lambda x}\,dx = 1/\lambda$}@}. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Hazard rate.
>
> We model the lifetime of a device by a continuously distributed random variable $T\ge0$ with CDF $F(t)$ and PDF $f(t)$ (continuous for all $t\ge0$). The hazard rate is defined as $$\lambda(t)=\lim_{h\searrow0}\frac{P[t\le T\le t+h\mid T\ge t]}{h},\qquad t\ge0$$ (this is also relevant for life-insurance purposes).
>
> - (a) Express $\lambda(t)$ in terms of $f(t)$ and $F(t)$.
> - (b) Suppose $T\sim\operatorname{Exp}(\alpha)$ with $\alpha>0$ and compute $\lambda(t)$.
> - (c) Verify that $F(t)=1-\exp\!\big(-\int_0^t\lambda(s)\,ds\big)$ when $t\ge0$.
> - (d) Compute $F(t)$ and $f(t)$ for $t\ge0$ when $\lambda(t)=\alpha t^\gamma$ ($\alpha,\gamma>0$) (Weibull distribution).
> - (e) Show that $E[T]=\int_0^\infty\exp\!\big(-\int_0^t\lambda(s)\,ds\big)\,dt$.
>
> Solution:
>
> - (a) From the definition, {@{$\lambda(t)=\lim_{h\searrow0}\frac{P[t\le T\le t+h\mid T\ge t]}{h} =\lim_{h\searrow0}\frac{P[t\le T\le t+h]}{h\,P(T\ge t)} =\frac1{1-F(t)}\lim_{h\searrow0}\frac{F(t+h)-F(t)}{h} =\frac{f(t)}{1-F(t)}$}@}, so {@{$\lambda(t)=f(t)/(1-F(t))$}@}.
> - (b) For the exponential law, {@{$f(t)=\lambda e^{-\lambda t}$ and $1-F(t)=e^{-\lambda t}$}@}, so {@{$\lambda(t)=\frac{f(t)}{1-F(t)}=\frac{\lambda e^{-\lambda t}}{e^{-\lambda t}}=\lambda$}@}, i.e. the hazard rate is {@{the constant $\lambda$}@}; this encodes {@{memorylessness}@}.
> - (c) From {@{$\lambda(t)=\frac{f(t)}{1-F(t)} = -\frac{d}{dt}\log(1-F(t))$}@}, integrate $\int_0^t$: {@{$-\int_0^t\lambda(s)\,ds = \log(1-F(t))-\log(1-F(0))$}@}; {@{$F(0)=0$}@}, so {@{$\log(1-F(t))=-\int_0^t\lambda(s)\,ds$}@}, and exponentiating gives {@{$F(t)=1-\exp\left(-\int_0^t \lambda(s)\,ds\right)$}@}.
> - (d) Substituting {@{$\lambda(t)=\alpha t^\gamma$ into (c)}@} gives {@{$\int_0^t \alpha s^\gamma\,ds = \frac{\alpha}{\gamma+1}t^{\gamma+1}$}@}, so {@{$F(t)=1-\exp\left(-\frac{\alpha}{\gamma+1}t^{\gamma+1}\right)$ (a Weibull-type law)}@}. Differentiating gives {@{$f(t)=F'(t)=\alpha t^\gamma\exp\left(-\frac{\alpha}{\gamma+1}t^{\gamma+1}\right)$}@}.
> - (e) The survival function is {@{$1-F(t)=\exp\left(-\int_0^t\lambda(s)\,ds\right)$}@} from (c); plugging into {@{$E[T]=\int_0^\infty (1-F(t))\,dt$ (from Problem 2(b))}@} gives {@{$E[T]=\int_0^\infty \exp\left(-\int_0^t\lambda(s)\,ds\right)dt$}@}. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,46,46.47643997,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> More expectation tricks.
>
> - (a) For a uniform random permutation of $\{1,\dots,n\}$, let $X$ be the number of fixed points. Find $E[X]$.
> - (b) A company counts a day as a holiday if at least one worker has a birthday on that day. For which workforce size is the expected number of worker-days maximized?
>
> Solution:
>
> - (a) Let $A_i$ be {@{the event that $i$ is fixed}@}; there are {@{$(n-1)!$ permutations fixing $i$ out of $n!$ total}@}, so {@{$P(A_i)=(n-1)!/n! = 1/n$}@}. Since {@{$X=\sum_{i=1}^n\mathbf 1_{A_i}$}@}, {@{linearity gives $E[X]=n\cdot\frac1n=1$}@}.
> - (b) Let $S$ be {@{the number of birthday-free days}@}. For {@{a fixed day}@}, the probability {@{no one has a birthday is $(364/365)^n$}@}, so by {@{linearity $E[S]=365(364/365)^n$}@}. Expected working days = $E[S]$, so {@{expected worker-days = $n\cdot E[S]$}@}. Let {@{$a_n=365n(364/365)^n$}@}; then {@{$\frac{a_{n+1}}{a_n}=\frac{n+1}{n}\cdot\frac{364}{365}$}@}, so $a_n$ {@{increases while $\frac{n+1}{n}>\frac{365}{364}$, i.e. $n<364$, and decreases afterward}@}, giving the maximum at {@{$n=364$ or $n=365$ (they are equal)}@}. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->
