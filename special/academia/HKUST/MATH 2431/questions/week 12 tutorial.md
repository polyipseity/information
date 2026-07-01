---
aliases:
    - HKUST MATH 2431 week 12 tutorial
    - HKUST MATH2431 week 12 tutorial
    - MATH 2431 week 12 tutorial
    - MATH2431 week 12 tutorial
tags:
    - flashcard/active/special/academia/HKUST/MATH_2431/questions/week_12_tutorial
    - language/in/English
---

# week 12 tutorial

- HKUST MATH 2431

The questions on this page combine T1B tutorial session problems with supplementary examples from solution notes. The quoted problems focus on joint laws, marginalization, and geometric probability.

- topics: joint versus marginal laws; marginal densities; Buffon's needle; packet collisions; convolution of uniforms.

> Give two random vectors with the same marginal distributions but different joint distributions.
>
> Solution: {@{A $2\times2$ probability table}@} already suffices for a concrete example. Let {@{$X,Y\in\{0,1\}$}@} and consider two joint mass functions: {@{$$P_1(X=0,Y=0)=\tfrac12,\quad P_1(X=0,Y=1)=0,\quad P_1(X=1,Y=0)=0,\quad P_1(X=1,Y=1)=\tfrac12,$$}@} so that {@{$X=Y$ with probability $1$ (perfect positive dependence)}@}. The marginals are {@{$P_1(X=0)=P_1(Y=0)=\tfrac12$ and $P_1(X=1)=P_1(Y=1)=\tfrac12$}@}. Now consider: {@{$$P_2(X=0,Y=0)=\tfrac14,\quad P_2(X=0,Y=1)=\tfrac14,\quad P_2(X=1,Y=0)=\tfrac14,\quad P_2(X=1,Y=1)=\tfrac14,$$}@} so that {@{$X$ and $Y$ are independent (each of the four joint outcomes is equally likely)}@}. The marginals are {@{again $\tfrac12$ each, hence identical to those of $P_1$}@}, yet {@{$P_1\neq P_2$}@}. This shows that {@{marginals alone do not determine the joint distribution}@}.

<!-- markdownlint MD028 -->

> Consider the joint density $$f_{X,Y}(x,y)=\lambda^2 e^{-\lambda y}\mathbf 1_{\{0\le x\le y\}}, \qquad \lambda>0.$$ Find the marginal densities.
>
> Solution: The support is {@{$\{(x,y):0\le x\le y\}$}@}. For the marginal of $X$, fix {@{$x\ge0$ and integrate out $y$}@}: {@{$$f_X(x)=\int_{-\infty}^\infty f_{X,Y}(x,y)\,dy=\int_x^\infty \lambda^2 e^{-\lambda y}\,dy = \lambda e^{-\lambda x},\qquad x\ge0,$$}@} so {@{$X\sim\operatorname{Exp}(\lambda)$}@}. For the marginal of $Y$, fix {@{$y\ge0$ and integrate out $x$}@}: {@{$$f_Y(y)=\int_{-\infty}^\infty f_{X,Y}(x,y)\,dx=\int_0^y \lambda^2 e^{-\lambda y}\,dx = \lambda^2 y e^{-\lambda y},\qquad y\ge0,$$}@} which is {@{$\operatorname{Gamma}(2,\lambda)$}@}. Hence {@{$X$ is exponential and $Y$ has a Gamma-type density}@}.

<!-- markdownlint MD028 -->

> In Buffon's needle problem, parallel lines are distance $a$ apart and a needle of length $\ell<a$ is dropped uniformly at random. What is the probability that the needle hits a line?
>
> Solution: {@{The needle's position}@} is determined by {@{the distance $X$ of its midpoint to the nearest line and its orientation angle $\Theta$}@}. By {@{the uniformity assumption}@}, {@{$X\sim U([0,a/2])$ and $\Theta\sim U([0,\pi])$ independently}@}, so their joint density is {@{constant on the rectangle $[0,a/2]\times[0,\pi]$}@}: {@{$$f_{X,\Theta}(x,\theta)=\frac{2}{\pi a},\qquad 0\le x\le\frac a2,\;0\le\theta\le\pi.$$}@} The needle hits a line iff its {@{vertical projection reaches the line, i.e. $\frac{\ell}{2}\sin\Theta\ge X$}@}. Integrating over this admissible region, {@{$$\begin{aligned} P(\text{hit}) &=\iint_{\frac\ell2\sin\theta\ge x} f_{X,\Theta}(x,\theta)\,dx\,d\theta =\frac{2}{\pi a}\int_0^\pi\int_0^{\frac\ell2\sin\theta}dx\,d\theta\\ &=\frac{2}{\pi a}\int_0^\pi \frac\ell2\sin\theta\,d\theta =\frac{\ell}{\pi a}\int_0^\pi \sin\theta\,d\theta =\frac{2\ell}{\pi a} \,. \end{aligned}$$}@} Thus {@{$P(\text{hit})=\dfrac{2\ell}{\pi a}$}@}.

<!-- markdownlint MD028 -->

> Two packet arrival times $T_1,T_2$ are independent and uniform on $[0,T]$. If packets collide whenever they arrive within time $\tau$ of each other, find the collision probability.
>
> Solution: Since $T_1,T_2$ are {@{iid $U([0,T])$}@}, the pair $(T_1,T_2)$ is {@{uniformly distributed over the square $[0,T]^2$}@}. A collision occurs when {@{$|T_1-T_2|\le\tau$, which corresponds to the diagonal strip $\{(t_1,t_2):|t_1-t_2|\le\tau\}$}@}. {@{The complement of this strip}@} in the square consists of {@{two right triangles at opposite corners, each with side length $T-\tau$}@}. Hence {@{$$P(\text{collision})=1-\frac{2\cdot\frac12(T-\tau)^2}{T^2}=1-\frac{(T-\tau)^2}{T^2}=1-\left(1-\frac\tau T\right)^2.$$}@} Equivalently, {@{$P(\text{collision})=\dfrac{2T\tau-\tau^2}{T^2}$}@}.

---

<!-- Source: Solution of Tutorial Notes 9 (Supplementary Examples) -->

> Let $X$ and $Y$ be independent random variables uniformly distributed on $[0,1]$. Find the PDF of $W=X+Y$.
>
> Solution: Since {@{$X$ and $Y$ are independent}@}, the density of their sum is {@{the convolution $f_W(w)=\int_{-\infty}^\infty f_X(w-y)f_Y(y)\,dy$}@}. The integrand is {@{nonzero only when $0\le w-y\le1$ and $0\le y\le1$}@}, which together give {@{$w-1\le y\le w$}@}. Split $w$ into two ranges:
>
> - {@{$0\le w\le1$: $0\le y\le w$}@}, giving {@{$f_W(w)=\int_0^w 1\,dy=w$}@}.
> - {@{$1<w\le2$: $w-1\le y\le 1$}@}, giving {@{$f_W(w)=\int_{w-1}^1 1\,dy=2-w$}@}.
>
> Hence {@{$$f_W(w)=\begin{cases} w, & 0\le w\le 1,\\ 2-w, & 1<w\le 2,\\ 0, & \text{otherwise}, \end{cases}$$}@} which is {@{the triangular distribution on $[0,2]$}@}.

<!-- markdownlint MD028 -->

> __Self exercise:__ Let $X,Y,Z$ be jointly independent and uniformly distributed on $[0,1]$. Find the PDF of $A=X+Y+Z$.
>
> Solution: Let {@{$W=X+Y$ (triangular on $[0,2]$)}@}. By {@{independence, $f_A(a)=\int_{-\infty}^\infty f_W(a-z)f_Z(z)\,dz$ where $f_Z(z)=\mathbf 1_{\{0\le z\le1\}}$}@}. The limits come from {@{$0\le z\le1$ and the support $0\le a-z\le2$}@}, giving {@{$\max(0,a-2)\le z\le\min(1,a)$}@}. Split $a$ into three ranges:
>
> - {@{$0\le a\le1$: $0\le z\le a$}@}, so {@{$a-z\in[0,1]$ and $f_W(a-z)=a-z$}@}, giving {@{$f_A(a)=\int_0^a (a-z)\,dz = \dfrac{a^2}{2}$}@}.
> - {@{$1<a\le2$: $z\in[a-1,a]$}@}. On $[a-1,1]$, {@{$a-z\in[0,1]$, giving $f_W(a-z)=a-z$}@}; on $[1,a]$, {@{$a-z\in[1,2]$, giving $f_W(a-z)=2-(a-z)$}@}. Hence {@{$$\begin{aligned} f_A(a)&=\int_{a-1}^1 (a-z)\,dz+\int_1^a (2-(a-z))\,dz \\ & =\Bigl[-\frac{(a-z)^2}{2}\Bigr]_{z=a-1}^{1}+\Bigl[2z-\frac{(a-z)^2}{2}\Bigr]_{z=1}^{a} \\ &= -a^2+3a-\frac32 \,. \end{aligned}$$}@}
> - {@{$2<a\le3$: $z\in[a-2,1]$}@}, so {@{$a-z\in[1,2]$ and $f_W(a-z)=2-(a-z)$}@}. Hence {@{$$f_A(a)=\int_{a-2}^1 (2-(a-z))\,dz =\int_{a-2}^1 (2-a+z)\,dz =\frac{(3-a)^2}{2}.$$}@}
>
> The result is {@{a piecewise quadratic density symmetric about $1.5$}@}; the three pieces {@{agree at $a=1,2$, confirming continuity}@}.
