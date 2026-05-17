---
aliases:
    - HKUST MATH 2431 week 8 tutorial
    - HKUST MATH2431 week 8 tutorial
    - MATH 2431 week 8 tutorial
    - MATH2431 week 8 tutorial
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/week_8_tutorial
    - language/in/English
---

# week 8 tutorial

- HKUST MATH 2431

The questions on this page combine the _T1B tutorial session_ problems with supplementary examples from the solution notes. As in the earlier tutorial pages, each official-style prompt is kept as a markdown quote block and the solutions are faithful paraphrased study notes rather than verbatim transcription.

- topics: transformation of random variables; inverse-transform sampling; invariance of the Cauchy law; discrete iid min/max/equality; power-transform density.

> Let $X$ be a continuous random variable and let $Y=g(X)$ where $g$ is strictly monotone. Derive the density of $Y$ from the density of $X$.
>
> Solution: Rewrite {@{the event $\{g(X)\le y\}$ by using the inverse map}@}. If {@{$g$ is increasing}@}, then {@{$F_Y(y)=P(X\le g^{-1}(y))=F_X(g^{-1}(y))$}@}. If {@{$g$ is decreasing, the inequality reverses}@}, but differentiating still {@{leads to the same absolute-value rule}@}. Therefore the transformed density is {@{$f_Y(y)=f_X(g^{-1}(y))\left|\dfrac{d}{dy}g^{-1}(y)\right|$ on the range of $g$}@}. <!--SR:!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Suppose $X\sim U([-1,1])$ and $Y=\arcsin(X)$. Find the density of $Y$.
>
> Solution: {@{The map $\arcsin$}@} is {@{increasing from $[-1,1]$ onto $[-\pi/2,\pi/2]$}@}. Hence {@{$$F_Y(y)=P(\arcsin(X)\le y)=P(X\le \sin y)=\frac{1+\sin y}{2}, \qquad -\frac{\pi}{2}\le y\le \frac{\pi}{2}.$$}@} {@{Differentiating}@} gives {@{$f_Y(y)=\frac12\cos y$ on $[-\pi/2,\pi/2]$, and $f_Y(y)=0$ outside that interval}@}. <!--SR:!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Let $U\sim U((0,1))$ and let $F$ be a cumulative distribution function with pseudoinverse $F^{-1}(u)=\sup\{z\in\mathbb R:F(z)<u\}$. Show that $X=F^{-1}(U)$ has CDF $F$.
>
> Solution: The key equivalence is {@{$F^{-1}(u)\le x \iff u\le F(x)$}@}.
>
> _Proof of the equivalence:_ ($\Rightarrow$) If $F^{-1}(u)\le x$ then {@{$\sup\{z:F(z)<u\}\le x$, so every $z>x$ satisfies $F(z)\ge u$}@}; {@{right-continuity of $F$}@} gives {@{$F(x)=\lim_{z\downarrow x}F(z)\ge u$, i.e. $u\le F(x)$}@}. ($\Leftarrow$) If $u\le F(x)$, then for {@{any $z>x$, $F(z)\ge F(x)\ge u$}@}, hence {@{no $z>x$ has $F(z)<u$ and thus $\sup\{z:F(z)<u\}\le x$, i.e. $F^{-1}(u)\le x$}@}.
>
> Therefore {@{$$P(X\le x)=P(F^{-1}(U)\le x)=P(U\le F(x))=F(x),$$}@} because $U$ is {@{uniform on $(0,1)$}@}. So $F^{-1}(U)$ realizes {@{the target law; this is the inverse-transform construction}@}. <!--SR:!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Let $X$ have the Cauchy density $f(x)=\dfrac{1}{\pi(1+x^2)}$ and define $Y=X^{-1}$. Show that $Y$ is again Cauchy.
>
> Solution: {@{The map $x\mapsto 1/x$}@} has {@{inverse itself and Jacobian factor $1/y^2$}@}. Hence {@{$$f_Y(y)=f_X(1/y)\left|\frac{d}{dy}(1/y)\right|=\frac{1}{\pi(1+y^{-2})}\cdot \frac{1}{y^2}=\frac{1}{\pi(1+y^2)}.$$}@} Thus $Y$ has {@{the same Cauchy density as $X$; the Cauchy law is stable under reciprocation}@}. <!--SR:!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z-->

---

<!-- Source: Solution of Tutorial Notes 6 (Supplementary Examples) -->

> Let $X$ and $Y$ be iid discrete random variables taking values in the positive integers with PMF $f(x)=2^{-x}$ for $x=1,2,\dots$. Find (a) $P(\min\{X,Y\}\ge x)$, (b) $P(Y=X)$, (c) $P(X>Y)$.
>
> Solution:
>
> - (a) {@{$\{\min\{X,Y\}\ge x\}=\{X\ge x\}\cap\{Y\ge x\}$}@}, so by {@{independence $$P(\min\{X,Y\}\ge x)=P(X\ge x)^2.$$}@} Since {@{$P(X\ge x)=\sum_{k=x}^\infty 2^{-k}=2^{1-x}$}@}, we get {@{$P(\min\{X,Y\}\ge x)=2^{2-2x}$}@}.
> - (b) By {@{the iid property}@}, {@{$$P(Y=X)=\sum_{n=1}^\infty P(X=n)^2=\sum_{n=1}^\infty 4^{-n}=\frac{1}{3} \,.$$}@}
> - (c) By {@{symmetry, $P(X>Y)=P(X<Y)$. Since $P(X>Y)+P(X<Y)+P(X=Y)=1$}@}, we obtain {@{$P(X>Y)=\frac{1}{2}(1-P(Y=X))=\frac{1}{3}$}@}. <!--SR:!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Let $X$ be continuous with density $f_X$ and define $Y=X^n$ for positive integers $n$. Find the density $f_Y$. Note the formula differs in between even $n$ and odd $n$ because $x\mapsto x^n$ is not one-to-one on $\mathbb R$.
>
> Solution: {@{The map $g(x)=x^n$}@} has {@{inverse $g^{-1}(y)=y^{1/n}$ and derivative $\frac{d}{dy}g^{-1}(y)=\frac{1}{n}y^{1/n-1}$}@}.
>
> For odd $n$, $g$ is {@{strictly increasing on $\mathbb R$}@}, so {@{$$f_Y(y)=f_X(y^{1/n})\cdot\frac{1}{n}|y|^{1/n-1},\qquad y\in\mathbb R.$$}@}
>
> For even $n$, $g$ is {@{not one-to-one: $x$ and $-x$ map to the same $y$}@}. Hence {@{$Y\ge 0$ almost surely and two preimages contribute}@}: {@{$$F_Y(y)=P(-y^{1/n}\le X\le y^{1/n})=F_X(y^{1/n})-F_X(-y^{1/n}),\qquad y\ge 0.$$}@} Differentiating, {@{$$f_Y(y)=\frac{1}{n}y^{1/n-1}\bigl(f_X(y^{1/n})+f_X(-y^{1/n})\bigr),\qquad y\ge 0.$$}@} So the even case involves {@{a sum of two branches while the odd case uses a single branch}@}. <!--SR:!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z!fsrs,2026-09-25T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-07-21T00:00:00.000Z-->
