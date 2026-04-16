---
aliases:
  - Riemann integral
  - Riemann integrals
  - Riemann integration
  - improper Riemann integral
  - improper Riemann integrals
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/Riemann_integration
  - language/in/English
---

# Riemann integration

In this course the point is not to rebuild real analysis from scratch, but to keep clear exactly which integration facts are being used when probability densities, cumulative distribution functions, and improper integrals over tails appear.

---

Flashcards for this section are as follows:

- overview ::@:: In this course, Riemann integration is the one-dimensional integration framework used to justify probability densities, interval probabilities, and improper integrals over tails or near singular endpoints.

<!-- check: ignore-next-line[header_style]: proper noun -->
## Riemann sums and integrability

Fix a bounded interval $[a,b]$. Let $B([a,b])$ denote the bounded real-valued functions on $[a,b]$. A partition of $[a,b]$ is a finite ordered tuple $Z_n=(x_0,x_1,\ldots,x_n)$ with $a=x_0<x_1<\cdots<x_n=b$. Its norm is $|Z_n|=\max_{1\le j\le n}(x_j-x_{j-1})$, which measures the mesh size of the partition.

If $f\in B([a,b])$ and $I_j=[x_{j-1},x_j]$, the lower Riemann sum is $$S_-(Z_n,f)=\sum_{j=1}^n (x_j-x_{j-1})\inf_{z\in I_j}f(z),$$ while the upper Riemann sum is $$S_+(Z_n,f)=\sum_{j=1}^n (x_j-x_{j-1})\sup_{z\in I_j}f(z).$$ Because $f$ is bounded, the infima and suprema are finite and both sums are well defined.

The lower Riemann integral is the supremum of all lower sums and the upper Riemann integral is the infimum of all upper sums. A bounded function is _Riemann-integrable_ when these two values agree. The common value is written $\int_a^b f(x)\,dx$. So integrability means that sufficiently fine lower and upper step-function approximations squeeze the same area.

This language is exactly what lies behind the density viewpoint in probability. When one says that probabilities of small intervals are approximated by evaluating a density on fine subintervals and summing, one is really invoking the convergence of these lower and upper sum approximations.

---

Flashcards for this section are as follows:

- partition of $[a,b]$ ::@:: A partition of $[a,b]$ is a finite ordered tuple $Z_n=(x_0,\ldots,x_n)$ with $a=x_0<x_1<\cdots<x_n=b$.
- norm of a partition $Z_n$ ::@:: The norm of a partition $Z_n$ is $|Z_n|=\max_{1\le j\le n}(x_j-x_{j-1})$; it measures the largest subinterval length.
- lower Riemann sum for $f$ on intervals $I_j=[x_{j-1},x_j]$ ::@:: The lower Riemann sum is $S_-(Z_n,f)=\sum_{j=1}^n (x_j-x_{j-1})\inf_{z\in I_j}f(z)$.
- upper Riemann sum for $f$ on intervals $I_j=[x_{j-1},x_j]$ ::@:: The upper Riemann sum is $S_+(Z_n,f)=\sum_{j=1}^n (x_j-x_{j-1})\sup_{z\in I_j}f(z)$.
- Riemann-integrability on $[a,b]$ ::@:: A bounded function on $[a,b]$ is Riemann-integrable when the supremum of all lower sums equals the infimum of all upper sums; the common value is $\int_a^b f(x)\,dx$.
- why Riemann sums justify interval probabilities of width $\Delta x$ ::@:: The density heuristic "probability on a small interval is approximately density times width" becomes rigorous by passing from fine interval sums to the Riemann integral.

## continuous functions are Riemann-integrable

Every continuous function $f\colon[a,b]\to\mathbb{R}$ is Riemann-integrable on $[a,b]$. The proof idea is compactness plus uniform continuity, but it is worth seeing exactly where each ingredient enters.

First, continuity on the compact interval $[a,b]$ implies boundedness, so the lower and upper sums are defined at all. Next, take the equal-mesh partition $x_j=a+\frac{b-a}{n}j$ and write $I_j=[x_{j-1},x_j]$. On each subinterval define the oscillation by $\omega_j(f):=\sup_{x\in I_j}f(x)-\inf_{x\in I_j}f(x)$. Then $S_+(Z_n,f)-S_-(Z_n,f)=\sum_{j=1}^n (x_j-x_{j-1})\omega_j(f)$. For the equal partition, every subinterval has length $\frac{b-a}{n}$, so $0\le S_+(Z_n,f)-S_-(Z_n,f)\le (b-a)\max_{1\le j\le n}\omega_j(f)$.

Now compactness matters again: a continuous function on a compact interval is uniformly continuous. Therefore for every $\varepsilon>0$ there exists $\delta>0$ such that $|x-y|<\delta$ implies $|f(x)-f(y)|<\varepsilon$. Once $|Z_n|<\delta$, every interval $I_j$ has diameter below $\delta$, hence every oscillation satisfies $\omega_j(f)<\varepsilon$. Substituting into the previous estimate gives $0\le S_+(Z_n,f)-S_-(Z_n,f)<\varepsilon(b-a)$.

Finally, the lower integral is at most every upper sum and the upper integral is at least every lower sum, so $0\le \overline{\int_a^b} f-\underline{\int_a^b} f\le S_+(Z_n,f)-S_-(Z_n,f)<\varepsilon(b-a)$ for all sufficiently fine equal-mesh partitions. Since $\varepsilon>0$ is arbitrary, the upper and lower integrals must coincide. So continuity is a sufficient condition for Riemann integrability.

For MATH 2431 this is the bridge that justifies routine integral manipulations for smooth densities such as uniform, exponential, and Gaussian densities on bounded intervals before one passes to improper tails.

---

Flashcards for this section are as follows:

- continuous functions on a compact interval $[a,b]$ ::@:: Every continuous function on a compact interval $[a,b]$ is Riemann-integrable.
- why continuity on $[a,b]$ implies boundedness ::@:: A continuous function on the compact interval $[a,b]$ is bounded, so its lower and upper Riemann sums are well defined.
- oscillation on a subinterval $I_j=[x_{j-1},x_j]$ ::@:: In the proof, one measures variation on each subinterval by $\omega_j(f)=\sup_{x\in I_j}f(x)-\inf_{x\in I_j}f(x)$.
- proof idea for continuous functions on equal-mesh partitions ::@:: On a compact interval, continuity implies uniform continuity, so once the mesh is small, every oscillation $\omega_j(f)$ is small; since $S_+(Z_n,f)-S_-(Z_n,f)=\sum_j (x_j-x_{j-1})\omega_j(f)$, the gap between upper and lower sums becomes arbitrarily small. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why uniform continuity is the key extra input ::@:: Ordinary continuity controls $f$ near one point at a time, but uniform continuity gives one single mesh size that works on every subinterval at once, which is exactly what the Riemann-sum estimate needs. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why $S_+(Z_n,f)-S_-(Z_n,f)\to0$ forces equal integrals ::@:: If the gap $S_+(Z_n,f)-S_-(Z_n,f)$ can be made arbitrarily small, then the upper integral minus the lower integral is squeezed between $0$ and that same small quantity, so the two integrals must be equal.

## fundamental theorem of calculus

The appendix records both directions of the fundamental theorem of calculus, but the second direction needs a careful hypothesis in the Riemann setting.

For the first direction, if $f\colon[a,b]\to\mathbb{R}$ is continuous and $F(x)=\int_a^x f(t)\,dt$, then $F$ is uniformly continuous on $[a,b]$, differentiable on $(a,b)$, and satisfies $F'(x)=f(x)$ for every $x\in(a,b)$. So integrating first and then differentiating recovers the original continuous integrand. The standard theorem statement usually records _uniform continuity_ rather than the stronger Lipschitz property, because uniform continuity is the more natural minimal conclusion. But in this specific setting one can say more: since $f$ is continuous on the compact interval $[a,b]$, it is bounded, say by $|f(t)|\le M$. Then for $x,y\in[a,b]$ one has $|F(x)-F(y)|=\left|\int_x^y f(t)\,dt\right|\le M|x-y|$, so $F$ is actually Lipschitz, and hence automatically uniformly continuous. Thus replacing "uniformly continuous" by "Lipschitz" would be correct here, but it would be unnecessarily strong and less standard as the headline theorem statement.

For the second direction, one must be more careful. It is **not** true that every derivative on $[a,b]$ is automatically Riemann-integrable. A differentiable function may have an unbounded derivative or a derivative with too many discontinuities. So the correct Riemann-version statement is: if $g\colon[a,b]\to\mathbb{R}$ is differentiable and $g'$ is Riemann-integrable on $[a,b]$, then $\int_a^b g'(x)\,dx=g(b)-g(a)$. A common sufficient hypothesis is that $g\in C^1([a,b])$, or more generally that $g'$ is bounded with only sufficiently sparse discontinuities.

A standard warning example is $$g(x)=\begin{cases}x^2\sin(1/x^2),&x\neq0,\\0,&x=0.\end{cases}$$ Then $g$ is differentiable on $[-1,1]$, but for $x\neq0$ one has $g'(x)=2x\sin(1/x^2)-2x^{-1}\cos(1/x^2)$, which is unbounded near $0$. Hence $g'$ is not Riemann-integrable on $[-1,1]$. So in the Riemann theory, differentiability of $g$ alone is not enough to conclude that $g'$ is integrable.

There are two complementary intuitions here. In the first direction, $F(x)=\int_a^x f(t)\,dt$ is an _accumulated area_ function. Its derivative at $x$ should therefore be the local rate at which area is being accumulated, namely the current height $f(x)$. In the second direction, the derivative $g'$ records instantaneous change, so integrating $g'$ over an interval should recover the total net change of $g$ across that interval.

In probability this theorem explains why one recovers a density from a differentiable cumulative distribution function and why antiderivatives are the natural way to evaluate interval probabilities for standard continuous laws.

---

Flashcards for this section are as follows:

- fundamental theorem of calculus / if $F(x)=\int_a^x f(t)\,dt$ with continuous $f$ ::@:: Then $F$ is uniformly continuous on $[a,b]$, differentiable on $(a,b)$, and satisfies $F'(x)=f(x)$.
- fundamental theorem of calculus / why $F$ is uniformly continuous ::@:: If $|f(t)|\le M$ on $[a,b]$, then $|F(x)-F(y)|=\left|\int_x^y f(t)\,dt\right|\le M|x-y|$, so $F$ is Lipschitz and therefore uniformly continuous.
- fundamental theorem of calculus / can one replace "uniformly continuous" by "Lipschitz" in part I, given $|F(x)-F(y)|\le \sup_{t\in[a,b]}|f(t)|\,|x-y|$? ::@:: In this setting yes, because that estimate shows $F$ is Lipschitz. But the standard theorem statement uses the weaker conclusion "uniformly continuous", which is the more natural minimal claim; saying "Lipschitz" as the headline would be correct but unnecessarily strong.
- fundamental theorem of calculus / correct Riemann-theory hypothesis for part II: if $g$ is differentiable on $[a,b]$ and $g'$ is Riemann-integrable on $[a,b]$ ::@:: Then $\int_a^b g'(x)\,dx=g(b)-g(a)$.
- fundamental theorem of calculus / why differentiability of $g$ alone is not enough ::@:: A differentiable function can have a derivative that is not Riemann-integrable, for example because the derivative is unbounded or too badly behaved; so FTC II in the Riemann setting needs the extra hypothesis that $g'$ itself is Riemann-integrable.
- fundamental theorem of calculus / warning example with $g(x)=x^2\sin(1/x^2)$ for $x\neq0$, $g(0)=0$ ::@:: This $g$ is differentiable on $[-1,1]$, but $g'(x)=2x\sin(1/x^2)-2x^{-1}\cos(1/x^2)$ for $x\neq0$, which is unbounded near $0$; hence $g'$ is not Riemann-integrable. So differentiability of $g$ does not by itself imply the hypothesis needed for FTC II.
- fundamental theorem of calculus / intuition for $F(x)=\int_a^x f(t)\,dt$ ::@:: The function $F$ measures accumulated area from $a$ to $x$, so its derivative should be the local rate of accumulation; that rate is exactly the current height $f(x)$.
- fundamental theorem of calculus / intuition for $\int_a^b g'(x)\,dx=g(b)-g(a)$ once $g'$ is integrable ::@:: The derivative $g'$ is instantaneous change, so integrating it over $[a,b]$ adds up all infinitesimal changes and recovers the total net change $g(b)-g(a)$.
- why $F(x)=\int_{-\infty}^x f(t)\,dt$ leads to $F'(x)=f(x)$ ::@:: If a cumulative distribution function has the form $F(x)=\int_{-\infty}^x f(t)\,dt$ with a continuous density $f$, then the fundamental theorem gives $F'(x)=f(x)$ at points of continuity of the density.

## algebraic properties of the Riemann integral

The appendix also recalls the standard properties used repeatedly in probability calculations.

If $f\in R([a,b])$ and $f\ge0$, then $\int_a^b f(x)\,dx\ge0$. If $f,g\in R([a,b])$ and $\alpha,\beta\in\mathbb{R}$, then $\alpha f+\beta g$ is again Riemann-integrable, and linearity gives $\int_a^b (\alpha f(x)+\beta g(x))\,dx=\alpha\int_a^b f(x)\,dx+\beta\int_a^b g(x)\,dx$. So $R([a,b])$ is a linear subspace of the bounded functions $B([a,b])$.

Moreover, if $f$ and $g$ are Riemann-integrable, then so are $|f|$ and $fg$, and one has the estimate $\left|\int_a^b f(x)\,dx\right|\le\int_a^b |f(x)|\,dx$. This is the integral analogue of the triangle inequality: the signed area cannot exceed the total area obtained after removing cancellations.

The closure statements do have limits. Division is _not_ automatically preserved. A clean counterexample on $[-1,1]$ is obtained by taking $f(x)\equiv1$ and $g(x)=x$ for $x\neq0$, with $g(0)=1$. The function $g$ differs from the continuous map $x\mapsto x$ at only one point, so $g$ is Riemann-integrable; it is also nowhere zero. But $f(x)/g(x)=1/x$ for $x\neq0$, with value $1$ at $0$, which is unbounded near $0$ and therefore not Riemann-integrable on $[-1,1]$. So closure under quotients requires extra hypotheses, typically that the denominator stay bounded away from $0$.

These facts are what make density calculations behave like ordinary algebra. Positivity guarantees that integrals of nonnegative densities really are probabilities; linearity lets one split expectations and compare candidate densities term by term; and the absolute-value inequality provides a simple control estimate when one needs bounds.

---

Flashcards for this section are as follows:

- positivity of $\int_a^b f(x)\,dx$ when $f\ge0$ ::@:: If $f\in R([a,b])$ and $f\ge0$, then $\int_a^b f(x)\,dx\ge0$.
- linear subspace property of $R([a,b])$ ::@:: If $f,g\in R([a,b])$ and $\alpha,\beta\in\mathbb{R}$, then $\alpha f+\beta g\in R([a,b])$; in particular, $R([a,b])$ is a linear subspace of $B([a,b])$.
- linearity of $\int_a^b (\alpha f+\beta g)$ once $\alpha f+\beta g\in R([a,b])$ ::@:: One has $\int_a^b (\alpha f(x)+\beta g(x))\,dx=\alpha\int_a^b f(x)\,dx+\beta\int_a^b g(x)\,dx$.
- closure of $R([a,b])$ under $|f|$ and $fg$ ::@:: If $f,g\in R([a,b])$, then $|f|$ and $fg$ are also Riemann-integrable.
- absolute-value estimate and triangle inequality for $\int_a^b f(x)\,dx$ ::@:: For $f\in R([a,b])$, one has $\left|\int_a^b f(x)\,dx\right|\le\int_a^b |f(x)|\,dx$; this is the integral form of the triangle inequality because cancellation in the signed integral can only reduce total size.
- quotient counterexample with $f(x)\equiv1$ and $g(x)=x$ for $x\neq0$, $g(0)=1$ ::@:: Both $f$ and $g$ are Riemann-integrable and $g$ never vanishes, but $f/g$ equals $1/x$ for $x\neq0$ and is unbounded near $0$, so it is not Riemann-integrable on $[-1,1]$. Thus Riemann-integrable functions are not closed under arbitrary division.
- intuition for the algebraic properties ::@:: Positivity prevents negative probability mass, linearity says integrals respect superposition, and the absolute-value estimate says cancellations can only make a signed integral smaller in magnitude than the total unsigned mass.

## improper Riemann integrals

Probability densities are often defined on unbounded intervals or have endpoint singularities, so one needs improper integrals.

Improper Riemann integrals of the _first kind_ arise when the interval is unbounded. If $f\colon[a,\infty)\to\mathbb{R}$ is Riemann-integrable on every compact interval $[a,c]$, then one says that $f$ is Riemann-integrable over $[a,\infty)$ when the limit $\int_a^{\infty} f(x)\,dx:=\lim_{c\to\infty}\int_a^c f(x)\,dx$ exists and is finite. The analogous definition applies to $(-\infty,a]$. For functions on the whole line one uses the two-sided limit $\int_{-\infty}^{\infty} f(x)\,dx:=\lim_{s\to\infty}\lim_{r\to\infty}\int_{-r}^s f(x)\,dx$, provided the resulting finite limit exists.

Improper Riemann integrals of the _second kind_ arise when the interval is bounded but the integrand may blow up near an endpoint. If $f\colon(a,b]\to\mathbb{R}$ is Riemann-integrable on every $[c,b]$ with $a<c<b$, then $\int_a^b f(x)\,dx:=\lim_{\varepsilon\downarrow0}\int_{a+\varepsilon}^b f(x)\,dx$ whenever the limit exists and is finite. The same idea works for singularities at the right endpoint.

In this course the distinction between first kind and second kind is mostly bookkeeping rather than deep theory: in both cases one replaces a problematic domain by ordinary Riemann integrals over safe compact intervals and then asks whether the limiting value exists and is finite. The probabilistic issue is simply whether the candidate density accumulates finite total mass.

These definitions are exactly what justify statements such as $\int_{-\infty}^{\infty}\varphi(x)\,dx=1$ for the standard normal density or $\int_0^{\infty}\lambda e^{-\lambda x}\,dx=1$ for the exponential density.

---

Flashcards for this section are as follows:

- improper integral of the first kind on $[a,\infty)$ ::@:: If $f$ is Riemann-integrable on every $[a,c]$, then $\int_a^{\infty} f(x)\,dx$ is defined as $\lim_{c\to\infty}\int_a^c f(x)\,dx$ when this finite limit exists.
- improper integral of the first kind on $\mathbb{R}$ ::@:: One defines $\int_{-\infty}^{\infty} f(x)\,dx$ by a two-sided limiting process because the difficulty is the unbounded domain, not a singularity inside a bounded interval.
- improper integral of the second kind for $\int_a^b f(x)\,dx$ near endpoint $a$ ::@:: If $f$ is Riemann-integrable away from an endpoint singularity at $a$, then $\int_a^b f(x)\,dx$ is defined by $\lim_{\varepsilon\downarrow0}\int_{a+\varepsilon}^b f(x)\,dx$ when the finite limit exists.
- first kind versus second kind ::@:: First kind means the trouble comes from an infinite interval, while second kind means the interval is bounded but the integrand may blow up near an endpoint; in this course the distinction is mainly bookkeeping because both are handled by truncation and a finite-limit test.
- why improper integrals normalize densities on unbounded supports or near singularities ::@:: Unbounded supports and endpoint singularities in densities require improper integrals; exponential and Gaussian normalization are standard examples.

## shrinking intervals near a point

A small but important technical fact used in probability is the following. Suppose $f\colon\mathbb{R}\to[0,\infty)$ is piecewise continuous and Riemann-integrable in the relevant improper sense. Then for every $a\in\mathbb{R}$ one has $\lim_{\delta\downarrow0}\int_a^{a+\delta} f(x)\,dx=0$.

If $f$ is continuous at $a$, the proof is direct. By continuity there exists $\delta_0>0$ such that $|f(x)-f(a)|<1$ whenever $|x-a|<\delta_0$. Hence for $0<\delta<\delta_0$, one has $0\le\int_a^{a+\delta} f(x)\,dx\le\int_a^{a+\delta} |f(a)|\,dx+\int_a^{a+\delta}|f(x)-f(a)|\,dx<(|f(a)|+1)\delta$. Letting $\delta\downarrow0$ forces the integral to go to $0$.

If $f$ is not continuous at $a$ but is piecewise continuous and nonnegative, one argues indirectly from the existence of the improper integral. Choose $b>a$ such that $f$ is continuous on $(a,b]$. Because the improper integral $\lim_{n\to\infty}\int_{a+1/n}^b f(x)\,dx$ exists, the sequence of truncated integrals is Cauchy. Therefore for every $\eta>0$ there exists $N\in\mathbb{N}$ such that for all $n\ge N$, one has $\left|\int_{a+1/n}^b f(x)\,dx-\int_{a+1/N}^b f(x)\,dx\right|<\eta$. Since $f\ge0$, the left-hand side is exactly $\int_{a+1/n}^{a+1/N} f(x)\,dx<\eta$.

Now fix any $0<\delta<1/N$. For all large $n$ with $1/n<\delta$, nonnegativity gives $0\le\int_{a+1/n}^{a+\delta} f(x)\,dx\le\int_{a+1/n}^{a+1/N} f(x)\,dx<\eta$. Passing to the limit $n\to\infty$ yields $0\le\int_a^{a+\delta} f(x)\,dx\le\eta$. The small detail is that the last inequality weakens from $<\eta$ to $\le\eta$ exactly at this limit step: strict inequalities need not survive taking limits (for example $1-1/n<1$ for all $n$ but $1-1/n\to1$), whereas non-strict inequalities do. Since $\eta>0$ was arbitrary, this proves again that $\int_a^{a+\delta} f(x)\,dx\to0$ as $\delta\downarrow0$.

This is the rigorous reason that even an integrable singularity does not create positive probability at a single point. The density may become large near the point, but the total area over a shrinking interval still goes to zero.

---

Flashcards for this section are as follows:

- shrinking interval integral $\int_a^{a+\delta} f(x)\,dx$ ::@:: If $f\colon\mathbb{R}\to[0,\infty)$ is piecewise continuous and improperly Riemann-integrable, then $\lim_{\delta\downarrow0}\int_a^{a+\delta} f(x)\,dx=0$ for every $a\in\mathbb{R}$.
- proof when $f$ is continuous at $a$ / estimate ::@:: If $|f(x)-f(a)|<1$ near $a$, then $0\le\int_a^{a+\delta} f(x)\,dx\le\int_a^{a+\delta}|f(a)|\,dx+\int_a^{a+\delta}|f(x)-f(a)|\,dx<(|f(a)|+1)\delta$, so the integral tends to $0$ as $\delta\downarrow0$.
- proof when $f$ is not continuous at $a$ / Cauchy step ::@:: If the improper integral $\int_a^b f(x)\,dx$ exists, then the truncated integrals $\int_{a+1/n}^b f(x)\,dx$ form a Cauchy sequence, so for every $\eta>0$ there is $N$ with $\int_{a+1/n}^{a+1/N} f(x)\,dx<\eta$ for all $n\ge N$.
- proof when $f$ is not continuous at $a$ / squeezing step ::@:: After fixing $0<\delta<1/N$ and choosing $n$ with $1/n<\delta$, nonnegativity gives $0\le\int_{a+1/n}^{a+\delta} f(x)\,dx\le\int_{a+1/n}^{a+1/N} f(x)\,dx<\eta$. Letting $n\to\infty$ gives $0\le\int_a^{a+\delta} f(x)\,dx\le\eta$; the rightmost inequality becomes non-strict exactly here, because strict inequalities need not survive limits, while non-strict ones do. So the limit is $0$.
- why integrability still gives point probability $0$ ::@:: Even if a density blows up near a point, integrability forces the probability of a shrinking interval around that point to go to $0$, so a single point cannot carry positive mass in a continuous density model.
