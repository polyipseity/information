---
aliases:
  - integration by substitution
tags:
  - flashcard/active/special/integration_by_substitution
  - language/in/English
---

# integration by substitution

## pitfalls

### _u_ not satisfying conditions

The substituting $u$ {@{should be [differentiable](../general/differentiable%20function.md) and $u'$ should be [integrable](../general/integral.md)}@}. An example is {@{substituting $u = \frac 1 x$ into $\int_{-1}^1 \! \mathrm{d}x$}@}: <!--SR:!2026-08-08,615,310!2030-03-19,1617,330-->

$$\begin{aligned}
& \phantom{=} \int_{-1}^1 \! \mathrm{d}x \\
(\text{error}) & = -\int_{-1}^1 \! x^2 \,\mathrm{d}u && \left( \mathrm{d}u = -\frac 1 {x^2} \,\mathrm{d}x \right) \\
& = \int_1^{-1} \frac 1 {u^2} \,\mathrm{d}u \\
& = \left[ \frac 1 u \right]_1^{-1} \\
& = -1 - 1 \\
& = -2
\end{aligned}$$

But the integral value is obviously 2, not -2. This is because {@{$u$ is not even defined at $x = 0$}@}. <!--SR:!2026-04-21,532,310-->

### integrand is non-rewritable

The integrand {@{must be rewritable in terms of $u$ within the bounds of integration}@}. An example is {@{substituting $u = x^2$ into $\int_{-1}^1 \! x^2 \,\mathrm{d}x$}@}: <!--SR:!2026-12-20,740,330!2026-12-26,618,270-->

$$\begin{aligned}
& \phantom{=} \int_{-1}^1 \! x^2 \,\mathrm{d}x \\
& = \frac 1 2 \int_1^1 \! x \,\mathrm{d}u && \left( \mathrm{d}u = 2x \,\mathrm{d}x \right) \\
(\text{error}) & = \frac 1 2 \int_1^1 \! \sqrt u \,\mathrm{d}u \\
& = \left[\frac 2 3 u^{\frac 3 2} \right]_1^1 \\
& = 0
\end{aligned}$$

But the integral value is obviously $\frac 2 3$, not 0. This is because {@{$x \ne \sqrt u$ when $x$ is negative, and the bounds of integration $[-1, 1]$ contain negative $x$}@}. Furthermore, {@{this substitution would have worked if the bounds of integration were $[0, 1]$ instead of $[-1, 1]$, as $x$ is never negative in this case}@}. Alternatively, {@{splitting the integral into two integrals on $[-1, 0]$ and $[0, 1]$ resp., then using $x = -\sqrt u$ instead of $x = \sqrt u$ for the integral with negative bounds of integration, would also have worked}@}. <!--SR:!2029-08-21,1416,310!2026-03-05,501,310!2026-05-28,489,270-->
