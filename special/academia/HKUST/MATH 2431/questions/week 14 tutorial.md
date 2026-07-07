---
aliases:
    - HKUST MATH 2431 week 14 tutorial
    - HKUST MATH2431 week 14 tutorial
    - MATH 2431 week 14 tutorial
    - MATH2431 week 14 tutorial
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/week_14_tutorial
    - language/in/English
---

# week 14 tutorial

- HKUST MATH 2431

The questions on this page combine T1A and T1B tutorial session problems with supplementary examples from solution notes. The tutorial introduced conditional expectation through concrete posterior and recursion calculations.

- topics: conditional expectation; Bayes reversal; waiting time for runs of heads; conditional variance; MGF independence verification; Poisson-Exponential mixture.

> A factory produces $n$ robots. Each robot is faulty with probability $\phi$, and each fault is detected independently with probability $\delta$. Let $X$ be the number of faulty robots and $Y$ the number detected as faulty. Find $E[X\mid Y]$.
>
> Solution: The model is {@{$X\sim\operatorname{Bin}(n,\phi)$, $Y\mid X\sim\operatorname{Bin}(X,\delta)$}@}; unconditionally {@{$Y\sim\operatorname{Bin}(n,\phi\delta)$ by Bernoulli thinning}@}.
>
> Write {@{$X=\sum_{i=1}^n X_i$ where $X_i\sim\operatorname{Ber}(\phi)$}@}, and {@{$Y=\sum_{i=1}^n Y_i$ where $Y_i$ is $X_i$ times an independent $\operatorname{Ber}(\delta)$ indicator}@}. For a single robot, {@{$$E[X_i\mid Y_i]=\frac{\phi(1-\delta)}{1-\phi\delta}+\Bigl(1-\frac{\phi(1-\delta)}{1-\phi\delta}\Bigr)Y_i,$$}@} since {@{$P(Y_i=0)=1-\phi\delta$, $P(X_i=1,Y_i=0)=\phi(1-\delta)$}@}. When {@{$Y_i=0$ the expected fault count is the posterior $\frac{\phi(1-\delta)}{1-\phi\delta}$}@}; when {@{$Y_i=1$ it is $1$ (detected implies faulty)}@}. By {@{linearity of conditional expectation, $E[X\mid Y]=\sum_{i=1}^n E[X_i\mid Y]$}@}, and {@{$E[X_i\mid Y]=E[X_i\mid Y_i]$ because $Y_i$ is a function of $Y$}@}. {@{Summing over $i$}@}, {@{$$E[X\mid Y]=\sum_{i=1}^n\Bigl[\frac{\phi(1-\delta)}{1-\phi\delta}+\Bigl(1-\frac{\phi(1-\delta)}{1-\phi\delta}\Bigr)Y_i\Bigr] =\frac{n\phi(1-\delta)+(1-\phi)Y}{1-\phi\delta}.$$}@} Therefore {@{$$E[X\mid Y]=\frac{n\phi(1-\delta)+(1-\phi)Y}{1-\phi\delta} \,.$$}@} <!--SR:!fsrs,2026-07-11T20:07:03.219Z,8,8.2956,1,2,1,0,0,2026-07-03T20:07:03.219Z!fsrs,2026-07-11T19:30:26.879Z,8,8.2956,1,2,1,0,0,2026-07-03T19:30:26.879Z!fsrs,2026-07-11T20:03:06.078Z,8,8.2956,1,2,1,0,0,2026-07-03T20:03:06.078Z!fsrs,2026-07-11T20:02:11.768Z,8,8.2956,1,2,1,0,0,2026-07-03T20:02:11.768Z!fsrs,2026-07-11T20:06:38.821Z,8,8.2956,1,2,1,0,0,2026-07-03T20:06:38.821Z!fsrs,2026-07-11T20:07:00.077Z,8,8.2956,1,2,1,0,0,2026-07-03T20:07:00.077Z!fsrs,2026-07-11T20:04:25.551Z,8,8.2956,1,2,1,0,0,2026-07-03T20:04:25.551Z!fsrs,2026-07-11T20:02:32.624Z,8,8.2956,1,2,1,0,0,2026-07-03T20:02:32.624Z!fsrs,2026-07-11T20:06:59.061Z,8,8.2956,1,2,1,0,0,2026-07-03T20:06:59.061Z!fsrs,2026-07-11T20:07:26.920Z,8,8.2956,1,2,1,0,0,2026-07-03T20:07:26.920Z!fsrs,2026-07-11T20:06:40.289Z,8,8.2956,1,2,1,0,0,2026-07-03T20:06:40.289Z!fsrs,2026-07-11T19:32:49.895Z,8,8.2956,1,2,1,0,0,2026-07-03T19:32:49.895Z!fsrs,2026-07-11T20:02:46.420Z,8,8.2956,1,2,1,0,0,2026-07-03T20:02:46.420Z-->

<!-- markdownlint MD028 -->

> A coin shows heads with probability $p\in(0,1)$. Let $X_n$ be the number of tosses needed to obtain a run of $n$ consecutive heads. Show that $$E[X_n]=\sum_{k=1}^n p^{-k}.$$
>
> Solution: {@{$E[X_1]=1/p$}@} (geometric). For $n\ge 2$, first {@{get $n-1$ consecutive heads}@}. After {@{that streak, toss once}@}: {@{heads ($p$) succeeds; tails ($1-p$) restarts to needing $n$ fresh}@}. Hence {@{$$E[X_n] = E[X_{n-1}] + 1 + (1-p)E[X_n],$$}@} so {@{$pE[X_n] = E[X_{n-1}] + 1$}@}. {@{Unwinding from $E[X_1]=1/p$}@} gives {@{$$E[X_n] = \frac{1}{p}E[X_{n-1}] + \frac{1}{p} = \sum_{k=1}^n \frac{1}{p^k}.$$}@} <!--SR:!fsrs,2026-07-11T20:01:28.751Z,8,8.2956,1,2,1,0,0,2026-07-03T20:01:28.751Z!fsrs,2026-07-11T20:04:26.732Z,8,8.2956,1,2,1,0,0,2026-07-03T20:04:26.732Z!fsrs,2026-07-11T20:02:30.460Z,8,8.2956,1,2,1,0,0,2026-07-03T20:02:30.460Z!fsrs,2026-07-11T20:07:01.121Z,8,8.2956,1,2,1,0,0,2026-07-03T20:07:01.121Z!fsrs,2026-07-11T20:07:24.568Z,8,8.2956,1,2,1,0,0,2026-07-03T20:07:24.568Z!fsrs,2026-07-11T20:07:04.501Z,8,8.2956,1,2,1,0,0,2026-07-03T20:07:04.501Z!fsrs,2026-07-11T20:07:05.336Z,8,8.2956,1,2,1,0,0,2026-07-03T20:07:05.336Z!fsrs,2026-07-11T20:04:30.551Z,8,8.2956,1,2,1,0,0,2026-07-03T20:04:30.551Z-->

---

<!-- Source: Solution of Tutorial Notes 11 (Supplementary Examples) -->

> Let $(X,Y)$ have joint density $$f(x,y)=\frac{e^{-x/y}e^{-y}}{y},\qquad x>0,\,y>0.$$ Find $E[X^2\mid Y]$.
>
> Solution: First find {@{the marginal of $Y$}@}: {@{$$f_Y(y)=\int_0^\infty\frac{e^{-x/y}e^{-y}}{y}\,dx=e^{-y}\int_0^\infty\frac{e^{-x/y}}{y}\,dx=e^{-y}\cdot 1=e^{-y},$$}@} where {@{the inner integral is $1$ because $\frac{1}{y}e^{-x/y}$ is an exponential density with rate $1/y$}@}. So {@{$Y\sim\operatorname{Exp}(1)$}@}.
>
> {@{The conditional density}@} is {@{$$f_{X\mid Y}(x\mid y)=\frac{f(x,y)}{f_Y(y)}=\frac{e^{-x/y}}{y},$$}@} so {@{$X\mid Y\sim\operatorname{Exp}(1/Y)$}@}. Hence {@{$\operatorname{E}[X\mid Y]=Y$ and $\operatorname{Var}(X\mid Y)=Y^2$}@}, and therefore {@{$\operatorname{E}[X^2\mid Y]=\operatorname{Var}(X\mid Y)+(\operatorname{E}[X\mid Y])^2=Y^2+Y^2=2Y^2$}@}. <!--SR:!fsrs,2026-07-11T20:03:54.737Z,8,8.2956,1,2,1,0,0,2026-07-03T20:03:54.737Z!fsrs,2026-07-11T19:37:47.905Z,8,8.2956,1,2,1,0,0,2026-07-03T19:37:47.905Z!fsrs,2026-07-11T19:37:55.180Z,8,8.2956,1,2,1,0,0,2026-07-03T19:37:55.180Z!fsrs,2026-07-11T19:31:01.413Z,8,8.2956,1,2,1,0,0,2026-07-03T19:31:01.413Z!fsrs,2026-07-11T20:01:26.955Z,8,8.2956,1,2,1,0,0,2026-07-03T20:01:26.955Z!fsrs,2026-07-11T20:07:28.348Z,8,8.2956,1,2,1,0,0,2026-07-03T20:07:28.348Z!fsrs,2026-07-11T20:02:08.278Z,8,8.2956,1,2,1,0,0,2026-07-03T20:02:08.278Z!fsrs,2026-07-11T19:30:24.310Z,8,8.2956,1,2,1,0,0,2026-07-03T19:30:24.310Z!fsrs,2026-07-11T19:28:34.352Z,8,8.2956,1,2,1,0,0,2026-07-03T19:28:34.352Z-->

<!-- markdownlint MD028 -->

> Let $X_1,X_2,X_3$ be i.i.d. $\operatorname{Unif}(0,1)$ and $S=X_1+X_2+X_3$. Using MGFs, verify that $X_1$ and $S-3X_1$ are not independent.
>
> Solution: The MGF of $X_1$ is {@{$M_{X_1}(t)=\frac{e^t-1}{t}$}@}. The MGF of $S-3X_1=X_2+X_3-2X_1$ is {@{$$M_{S-3X_1}(t)=M_{X_2}(t)M_{X_3}(t)M_{-2X_1}(t)=\left(\frac{e^t-1}{t}\right)^2\frac{e^{-2t}-1}{-2t}.$$}@}
>
> The joint MGF of $(X_1,S-3X_1)$ is {@{$$M_{(X_1,\,S-3X_1)}(t_1,t_2)=E[e^{t_1X_1+t_2(X_2+X_3-2X_1)}]=E[e^{(t_1-2t_2)X_1}]E[e^{t_2X_2}]E[e^{t_2X_3}]=\frac{e^{t_1-2t_2}-1}{t_1-2t_2}\left(\frac{e^{t_2}-1}{t_2}\right)^2.$$}@} Since this {@{does not factor as $M_{X_1}(t_1)M_{S-3X_1}(t_2)$}@}, they are {@{not independent}@}. <!--SR:!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Let $N\sim\operatorname{Poisson}(\lambda)$ where $\lambda\sim\operatorname{Exp}(\mu)$. Find the marginal distribution of $N$.
>
> Solution: $N$ is {@{a Poisson rate mixture}@}: {@{$N\mid\lambda\sim\operatorname{Poisson}(\lambda)$ and $\lambda\sim\operatorname{Exp}(\mu)$}@}. {@{The joint density/mass}@} is {@{$f(n,\lambda)=\frac{e^{-\lambda}\lambda^n}{n!}\cdot\mu e^{-\mu\lambda}$ for $n\ge0$, $\lambda>0$}@}. {@{Marginalize by integrating out $\lambda$}@}: {@{$$P(N=n)=\int_0^\infty\frac{e^{-\lambda}\lambda^n}{n!}\,\mu e^{-\mu\lambda}\,d\lambda=\frac{\mu}{n!}\int_0^\infty\lambda^n e^{-(1+\mu)\lambda}\,d\lambda.$$}@}
>
> Recall {@{the gamma function $\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}\,dt$, so $\Gamma(n+1)=n!$}@}. Substitute {@{$t=(1+\mu)\lambda$ ($dt=(1+\mu)\,d\lambda$)}@}: {@{$$\int_0^\infty\lambda^n e^{-(1+\mu)\lambda}\,d\lambda = \frac{1}{(1+\mu)^{n+1}}\int_0^\infty t^n e^{-t}\,dt = \frac{\Gamma(n+1)}{(1+\mu)^{n+1}} = \frac{n!}{(1+\mu)^{n+1}}.$$}@} Hence {@{$$P(N=n)=\frac{\mu}{n!}\cdot\frac{n!}{(1+\mu)^{n+1}}=\frac{\mu}{(1+\mu)^{n+1}}=\frac{\mu}{1+\mu}\left(\frac{1}{1+\mu}\right)^n,$$}@} which is {@{a geometric distribution with success probability $\frac{\mu}{1+\mu}$}@} (shifted to {@{start at $0$, counting failures before the first success}@}). <!--SR:!fsrs,2026-07-11T20:07:02.097Z,8,8.2956,1,2,1,0,0,2026-07-03T20:07:02.097Z!fsrs,2026-07-11T19:37:56.907Z,8,8.2956,1,2,1,0,0,2026-07-03T19:37:56.907Z!fsrs,2026-07-11T19:37:51.853Z,8,8.2956,1,2,1,0,0,2026-07-03T19:37:51.853Z!fsrs,2026-07-11T19:38:48.824Z,8,8.2956,1,2,1,0,0,2026-07-03T19:38:48.824Z!fsrs,2026-07-11T20:02:09.260Z,8,8.2956,1,2,1,0,0,2026-07-03T20:02:09.260Z!fsrs,2026-07-11T20:05:04.725Z,8,8.2956,1,2,1,0,0,2026-07-03T20:05:04.725Z!fsrs,2026-07-11T20:04:54.594Z,8,8.2956,1,2,1,0,0,2026-07-03T20:04:54.594Z!fsrs,2026-07-11T20:04:48.651Z,8,8.2956,1,2,1,0,0,2026-07-03T20:04:48.651Z!fsrs,2026-07-11T20:07:30.118Z,8,8.2956,1,2,1,0,0,2026-07-03T20:07:30.118Z!fsrs,2026-07-11T20:03:53.734Z,8,8.2956,1,2,1,0,0,2026-07-03T20:03:53.734Z!fsrs,2026-07-11T20:04:55.724Z,8,8.2956,1,2,1,0,0,2026-07-03T20:04:55.724Z!fsrs,2026-07-11T20:05:06.028Z,8,8.2956,1,2,1,0,0,2026-07-03T20:05:06.028Z-->
