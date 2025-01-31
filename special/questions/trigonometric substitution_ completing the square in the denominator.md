---
aliases:
  - 'trigonometric substitution: completing the square in the denominator'
tags:
  - date/2024/07/01
  - flashcard/active/special/questions/trigonometric_substitution__completing_the_square_in_the_denominator
  - language/in/English
  - question/mathematics/calculus/integral
---

# trigonometric substitution: completing the square in the denominator

- time:2024-07-01T16:09:56.318+08:00

Evaluate $$\int \! \frac x {\sqrt{-148 - 6x^2 + 60x} } \,\mathrm{d}x$$.

## strategy

- inspecting "$$\int \! \frac x {\sqrt{-148 - 6x^2 + 60x} } \,\mathrm{d}x$$" :@: Extract the factor $\frac 1 {\sqrt 2}$ from the integrand. Complete the square for the square root to get $\sqrt{-\left(\sqrt 3 x - 5\sqrt 3 \right)^2 + 1}$. Substitute $\sqrt 3 x - 5\sqrt 3 = \sin \theta \quad \theta \in \left[ -\frac \pi 2, \frac \pi 2 \right]$. <!--SR:!2025-04-09,68,230-->

## solution

$$\begin{aligned}
x & := \frac {\sin \theta} {\sqrt 3} + 5 \quad \theta \in \left[ -\frac \pi 2, \frac \pi 2 \right] \\
\\
& \phantom = \int \! \frac x {\sqrt{-148 - 6x^2 + 60x} } \,\mathrm{d}x \\
& = \frac 1 {\sqrt 2} \int \! \frac x {\sqrt{-74 - 3x^2 + 30x} } \,\mathrm{d}x \\
& = \frac 1 {\sqrt 2} \int \! \frac x {\sqrt{-\left(\sqrt 3 x - 5\sqrt 3 \right)^2 + 1} } \,\mathrm{d}x \\
& = \frac 1 {\sqrt 2} \int \! \frac {\frac {\sin \theta} {\sqrt 3} + 5} {\sqrt{-\sin^2 \theta + 1} } \frac {\cos \theta} {\sqrt 3} \,\mathrm{d}\theta \\
& = \frac 1 {\sqrt 6} \int \! \left( \frac {\sin \theta} {\sqrt 3} + 5 \right) \frac {\cos \theta} {\lvert \cos \theta \rvert} \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\cos \theta) \frac 1 {\sqrt 6} \int \! \left( \frac {\sin \theta} {\sqrt 3} + 5 \right) \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\cos \theta) \left(-\frac {\cos \theta} {3\sqrt 2} + \frac {5\sqrt 6} 6 \theta \right) + C \\
& = \left(-\frac {\cos \theta} {3\sqrt 2} + \frac {5\sqrt 6} 6 \theta \right) + C && \cos \theta \ge 0 \quad \forall \theta \in \left[ -\frac \pi 2, \frac \pi 2 \right] \\
& = -\frac {\sqrt{1 - 3(x - 5)^2} } {3\sqrt 2} + \frac {5\sqrt 6} 6 \arcsin\left( \sqrt 3(x - 5) \right) + C
\end{aligned}$$
