---
aliases:
  - integration by substitution
tags:
  - flashcard/special/integration_by_substitution
  - language/in/English
---

# integration by substitution

## pitfalls

### _u_ not satisfying conditions

The substituting $u$ {{should be [differentiable](../general/differentiable%20function.md) and $u'$ should be [integrable](../general/integral.md)}}. An example is {{substituting $u = \frac 1 x$ into $\int_{-1}^1 \! \mathrm{d}x$}}: <!--SR:!2024-05-11,17,290!2024-05-03,9,270-->

$$\begin{aligned}
& \phantom{=} \int_{-1}^1 \! \mathrm{d}x \\
(\text{error}) & = -\int_{-1}^1 \! x^2 \,\mathrm{d}u && \left( \mathrm{d}u = -\frac 1 {x^2} \,\mathrm{d}x \right) \\
& = \int_1^{-1} \frac 1 {u^2} \,\mathrm{d}u \\
& = \left[ \frac 1 u \right]_1^{-1} \\
& = -1 - 1 \\
& = -2
\end{aligned}$$

But the integral value is obviously 2, not -2. This is because {{$u$ is not even defined at $x = 0$}}. <!--SR:!2024-05-10,16,290-->

### integrand is non-rewritable

The integrand {{must be rewritable in terms of $u$ within the bounds of integration}}. An example is {{substituting $u = x^2$ into $\int_{-1}^1 \! \mathrm{d}x$}}: <!--SR:!2024-05-09,15,290!2024-05-06,13,270-->

$$\begin{aligned}
& \phantom{=} \int_{-1}^1 \! \mathrm{d}x \\
& = \frac 1 2 \int_1^1 \! \frac 1 x \,\mathrm{d}u && \left( \mathrm{d}u = 2x \,\mathrm{d}x \right) \\
(\text{error}) & = \frac 1 2 \int_1^1 \! \frac 1 {\sqrt u} \,\mathrm{d}u \\
& = \left[\sqrt u \right]_1^1 \\
& = 0
\end{aligned}$$

But the integral value is obviously 2, not 0. This is because {{$\frac 1 x \ne \frac 1 {\sqrt u}$ when $x$ is negative, and the bounds of integration $[-1, 1]$ contain negative $x$}}. Furthermore, {{this substitution would have worked if the bounds of integration were $[0, 1]$ instead of $[-1, 1]$, as $x$ is never negative in this case}}. Alternatively, {{splitting the integral into two integrals on $[-1, 0]$ and $[0, 1]$ resp., then using $\frac 1 x = -\frac 1 {\sqrt u}$ instead of $\frac 1 x = \frac 1 {\sqrt u}$ for the integral with negative bounds of integration, would also have worked}}. <!--SR:!2024-05-09,15,290!2024-05-06,12,270!2024-05-01,8,250-->
