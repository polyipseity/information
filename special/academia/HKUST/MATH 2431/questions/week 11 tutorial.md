---
aliases:
    - HKUST MATH 2431 week 11 tutorial
    - HKUST MATH2431 week 11 tutorial
    - MATH 2431 week 11 tutorial
    - MATH2431 week 11 tutorial
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/week_11_tutorial
    - language/in/English
---

# week 11 tutorial

- HKUST MATH 2431

The questions on this page summarize the _official tutorial materials_ for week 11, combining T1B tutorial session problems with supplementary examples from solution notes. The tutorial focused on expectation bounds and the multivariable integration techniques used repeatedly in later joint-distribution calculations.

- topics: generalized Markov inequality; Chebyshev bounds; probability via multiple integrals; Markov/Chebyshev application; non-decreasing Markov; moment existence

> Let $g$ be a nonnegative function and let $X$ be a random variable. Show that for every $c>0$, $$P(g(X)\ge c)\le \frac{E[g(X)]}{c}.$$
>
> Solution: Since {@{$g(X)\ge 0$}@}, we may estimate {@{$$E[g(X)]\ge E[\mathbf 1_{\{g(X)\ge c\}}g(X)]\ge c\,E[\mathbf 1_{\{g(X)\ge c\}}]=cP(g(X)\ge c).$$}@} Rearranging gives {@{the generalized Markov inequality}@}.

<!-- markdownlint MD028 -->

> A factory's weekly production has mean $500$. What can be said about $P(X\ge 1000)$? If the variance is also $100$, what lower bound can be given for the probability that production lies between $400$ and $600$?
>
> Solution: Markov gives {@{$P(X\ge 1000)\le E[X]/1000=1/2$}@}. If $\operatorname{Var}(X)=100$, then Chebyshev yields {@{$$P(|X-500|\ge 100)\le \frac{100}{100^2}=\frac{1}{100},$$}@} so {@{$P(400\le X\le 600)\ge 99/100$}@}. The mean controls only {@{a one-sided tail, while the variance yields concentration around the center}@}.

<!-- markdownlint MD028 -->

> Summarize the integration strategy used for later joint-density and problem-set questions.
>
> Solution: The core workflow is three steps: {@{(1) translate the probability statement into a planar region, (2) draw the region to understand its geometry, (3) integrate the joint density over that region}@}.
>
> Concretely:
>
> - {@{__Rectangles__ $R=[a,b]\times[c,d]$}@}: {@{iterated integrals with constant limits, $$P((X,Y)\in R)=\int_a^b\int_c^d f(x,y)\,dy\,dx.$$}@}
> - {@{__Variable-bound regions__ (e.g., $0\le y\le x\le 1$)}@}: {@{the inner limits become functions, $$P(0\le Y\le X\le 1)=\int_0^1\int_0^x f(x,y)\,dy\,dx.$$}@}
> - {@{__Integration order__}@}: sketching {@{the region reveals whether $dx\,dy$ or $dy\,dx$ is simpler}@} — swap when {@{one order requires case-splitting and the other does not}@}.
>
> In short: {@{identify the region first, then integrate over the region}@}.

---

<!-- Source: Solution of Tutorial Notes 8 (Supplementary Examples) -->

> A biased coin has probability $0.2$ of heads, independently of other flips. The coin is flipped $20$ times. Use (a) Markov's inequality and (b) Chebyshev's inequality to bound the probability it lands heads at least $16$ times.
>
> Solution: Let {@{$X\sim\operatorname{Bin}(20,0.2)$}@}. Write {@{$X=\sum_{i=1}^{20}I_i$ with $I_i\overset{\text{i.i.d.}}{\sim}\operatorname{Ber}(0.2)$}@}. Then {@{$E[X]=20(0.2)=4$ and $\operatorname{Var}(X)=20(0.2)(0.8)=3.2$}@}.
>
> - (a) Markov gives {@{$$P(X\ge 16)\le\frac{E[X]}{16}=\frac{4}{16}=0.25.$$}@}
> - (b) Chebyshev gives {@{$$P(X\ge 16)=P(X-4\ge 12)\le P(|X-4|\ge 12)\le\frac{3.2}{12^2}\approx 0.0222.$$}@}
>
> The Chebyshev bound is {@{much tighter ($0.022$ vs $0.25$) because it uses the variance}@}.

<!-- markdownlint MD028 -->

> Let $X$ be a random variable and $g:\mathbb R\to[0,\infty)$ be measurable and non-decreasing, with $E[g(X)]$ finite. Show that for every $t\in\mathbb R$ with $g(t)>0$, $$P(X\ge t)\le\frac{E[g(X)]}{g(t)}.$$
>
> Solution: Since $g$ is {@{non-decreasing, $\{X\ge t\}\subseteq\{g(X)\ge g(t)\}$}@}. Applying {@{the generalized Markov inequality to $g(X)$}@} gives {@{$$P(X\ge t)\le P(g(X)\ge g(t))\le\frac{E[g(X)]}{g(t)}.$$}@} This is {@{Markov's inequality with a non-decreasing transform}@}, extending {@{the standard version beyond the identity function}@}.

<!-- markdownlint MD028 -->

> Let $X$ be a random variable and $k\in\mathbb N$. If $E[X^k]$ exists, show that $E[X^r]$ exists for any positive integer $r<k$.
>
> Solution: Write {@{$|X|^r=|X|^r\mathbf 1_{\{|X|\le 1\}}+|X|^r\mathbf 1_{\{|X|>1\}}$}@}. The first term is {@{bounded by $1$. For the second, note that $r<k$, so $|X|^r\le |X|^k$ when $|X|>1$}@}. Hence {@{$$E[|X|^r]\le 1+E[|X|^k]<\infty.$$}@}
>
> Alternatively, use {@{the layer-cake (tail-integral) representation}@}. For any {@{non-negative $Y$, the tail integral identity}@} is {@{$E[Y]=\int_0^\infty P(Y>t)\,dt$}@}. Applying it to {@{$Y=|X|^r$ and substituting $t=s^r$ (so $dt=r s^{r-1}ds$)}@} gives {@{$$E[|X|^r]=\int_0^\infty P(|X|^r>t)\,dt=\int_0^\infty r s^{r-1}P(|X|>s)\,ds.$$}@} Rename $s$ back to $t$. Split {@{the integral at $t=1$}@}. For $t\le1$, the integrand is {@{bounded by $r t^{r-1}$, whose $dt$ integral is finite}@}. For $t>1$, since {@{$r<k$, we have $t^{r-1}\le t^{k-1}$}@}, hence {@{$$\int_1^\infty r t^{r-1}P(|X|>t)\,dt\le\frac{r}{k}\int_1^\infty k t^{k-1}P(|X|>t)\,dt\le\frac{r}{k}E[|X|^k]<\infty.$$}@} Both parts are {@{finite, so $E[|X|^r]<\infty$}@}. The key idea is that {@{higher moments dominate lower moments on tails}@}.
