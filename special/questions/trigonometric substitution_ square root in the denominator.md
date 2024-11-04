---
aliases:
  - 'trigonometric substitution: square root in the denominator'
tags:
  - date/2024/07/01
  - flashcard/active/special/questions/trigonometric_substitution__square_root_in_the_denominator
  - language/in/English
  - question/mathematics/calculus/integral
---

# trigonometric substitution: square root in the denominator

- datetime: 2024-07-01T16:09:49.707+08:00

Evaluate $$\int \! \frac {x^2} {\sqrt{3x^2 + 8} } \,\mathrm{d}x$$.

## strategy

- inspecting "$$\int \! \frac {x^2} {\sqrt{3x^2 + 8} } \,\mathrm{d}x$$" :: Consider that $x \in \mathbb{R}$ (valid for all reals) and $\tan^2 \theta + 1 = \sec^2 \theta$. Substitute $x = \sqrt{\frac 8 3} \tan \theta \quad \theta \in \left( -\frac \pi 2, \frac \pi 2 \right)$. <!--SR:!2025-06-06,218,270-->
- logarithm simplification tricks :: First, $\ln(a(x + y)) + C = \ln a + \ln(x + y) + C$, of which $\ln a$ can be absorbed into $C$ to become $\ln(x + y) + C$. Second, $\ln \left\lvert a + \sqrt{a^2 \pm 1} \right\rvert = -\ln \left\lvert a - \sqrt{a^2 \pm 1} \right\rvert$. <!--SR:!2025-01-05,124,290-->

## solution

$$\begin{aligned}
& \phantom = \int \! \frac {x^2} {\sqrt{3x^2 + 8} } \,\mathrm{d}x \\
& = \int \! \frac {\frac 8 3 \tan^2 \theta} {\sqrt 8 \sqrt{\tan^2 \theta + 1} } \sqrt{\frac 8 3} \sec^2 \theta \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\tan \theta) \frac 8 {3 \sqrt 3} \int \! \tan^2 \theta \sec \theta \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\tan \theta) \frac 8 {3 \sqrt 3} \int \! \tan^2 \theta \sec \theta \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\tan \theta) \frac 8 {3 \sqrt 3} \int \! \left( \sec^2 \theta - 1 \right) \sec \theta \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\tan \theta) \frac 8 {3 \sqrt 3} \int \! \left( \sec^3 \theta - \sec \theta \right) \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\tan \theta) \frac 8 {3 \sqrt 3} \left( \int \! \sec^3 \theta \,\mathrm{d}\theta - \int \! \sec \theta \,\mathrm{d}\theta \right) \\
& = \operatorname{sgn}(\tan \theta) \frac 8 {3 \sqrt 3} \left( \frac {\sec \theta \tan \theta} 2 - \frac 1 2 \int \! \sec \theta \,\mathrm{d}\theta \right) \\
& = \operatorname{sgn}(\tan \theta) \frac 8 {3 \sqrt 3} \left( \frac {\sec \theta \tan \theta} 2 - \frac {\ln \lvert \tan \theta + \sec \theta \rvert} 2 \right) + C \\
& = \operatorname{sgn}(x) \frac 8 {3 \sqrt 3} \left( \frac {\operatorname{sgn}(x) \sqrt{\frac 3 8 x^2 + 1} \sqrt{\frac 3 8} x} 2 - \frac {\ln \left\lvert \sqrt{\frac 3 8} x + \operatorname{sgn}(x) \sqrt{\frac 3 8 x^2 + 1} \right\rvert} 2 \right) + C \\
& = \frac 8 {3 \sqrt 3} \left( \frac {\sqrt{\frac 3 8 x^2 + 1} \sqrt{\frac 3 8} x} 2 - \frac {\ln \left\lvert \sqrt{\frac 3 8} x + \sqrt{\frac 3 8 x^2 + 1} \right\rvert} 2 \right) + C && \ln \left\lvert \sqrt{\frac 3 8} x + \sqrt{\frac 3 8 x^2 + 1} \right\rvert = -\ln \left\lvert \sqrt{\frac 3 8} x - \sqrt{\frac 3 8 x^2 + 1} \right\rvert \\
& = \frac {4 \sqrt{\frac 3 8 x^2 + 1} \sqrt{\frac 3 8} x} {3 \sqrt 3} - \frac {4 \ln \left\lvert \sqrt{\frac 3 8} x + \sqrt{\frac 3 8 x^2 + 1} \right\rvert} {3 \sqrt 3} + C \\
& = \frac {x \sqrt{3 x^2 + 8} } 6 - \frac {4 \ln \left\lvert \sqrt 3 x + \sqrt{3x^2 + 8} \right\rvert} {3 \sqrt 3} + C \\
\end{aligned}$$
