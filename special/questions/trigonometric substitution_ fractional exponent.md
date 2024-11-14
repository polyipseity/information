---
aliases:
  - 'trigonometric substitution: fractional exponent'
tags:
  - date/2024/07/01
  - flashcard/active/special/questions/trigonometric_substitution__fractional_exponent
  - language/in/English
  - question/mathematics/calculus/integral
---

# trigonometric substitution: fractional exponent

- datetime: 2024-07-01T16:09:36.245+08:00

Evaluate $$\int \! \left( 5x^2 - 5 \right)^{\frac 3 2} \, \mathrm{d}x$$.

## strategy

- inspecting "$$\int \! \left( 5x^2 - 5 \right)^{\frac 3 2} \, \mathrm{d}x$$" :@: Consider that $\lvert x \rvert \ge 1$ (otherwise $*^{\frac 3 2}$ is undefined) and $\sec^2 \theta - 1 = \tan^2 \theta$. Substitute $x = \sec \theta \quad \theta \in \left[0, \frac \pi 2 \right) \cup \left(-\frac \pi 2, \pi \right]$. <!--SR:!2024-11-24,12,190-->
- logarithm simplification tricks :@: First, $\ln(a(x + y)) + C = \ln a + \ln(x + y) + C$, of which $\ln a$ can be absorbed into $C$ to become $\ln(x + y) + C$. Second, $\ln \left\lvert a + \sqrt{a^2 \pm 1} \right\rvert = -\ln \left\lvert a - \sqrt{a^2 \pm 1} \right\rvert$. <!--SR:!2025-08-10,287,290-->

## solution

$$\begin{aligned}
x & := \sec \theta \quad \theta \in \left[0, \frac \pi 2 \right) \cup \left(-\frac \pi 2, \pi \right] \\
\\
& \phantom = \int \! \left( 5x^2 - 5 \right)^{\frac 3 2} \,\mathrm{d}x \\
& = 5\sqrt 5 \int \! \left( \sec^2 \theta - 1 \right)^{\frac 3 2} \tan \theta \sec \theta \,\mathrm{d}\theta \\
& = 5\sqrt 5 \int \! \left\lvert \tan^3 \theta \right\rvert \tan \theta \sec \theta \,\mathrm{d}\theta \\
& = 5\sqrt 5 \int \! \left\lvert \tan^4 \theta \sec \theta \right\rvert \,\mathrm{d}\theta && \tan \theta \sec \theta \ge 0 \quad \forall \theta \in [0, \pi] \\
& = \operatorname{sgn}(\sec \theta) \cdot 5\sqrt 5 \int \! \left( \sec^2 \theta - 1 \right)^2 \sec \theta \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\sec \theta) \cdot 5\sqrt 5 \int \! \left( \sec^5 \theta - 2 \sec^3 \theta + \sec \theta \right) \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\sec \theta) \cdot 5\sqrt 5 \left(\int \! \sec^5 \theta \,\mathrm{d}\theta - 2 \int \! \sec^3 \theta \,\mathrm{d}\theta + \int \! \sec \theta \,\mathrm{d}\theta \right) \\
& = \operatorname{sgn}(\sec \theta) \cdot 5\sqrt 5 \left(\frac {\sec^3 \theta \tan \theta} 4 - \frac 5 4 \int \! \sec^3 \theta \,\mathrm{d}\theta + \int \! \sec \theta \,\mathrm{d}\theta \right) \\
& = \operatorname{sgn}(\sec \theta) \cdot 5\sqrt 5 \left(\frac {\sec^3 \theta \tan \theta} 4 - \frac 5 4 \frac {\sec \theta \tan \theta} 2 + \frac 3 8 \int \! \sec \theta \,\mathrm{d}\theta \right) \\
& = \operatorname{sgn}(\sec \theta) \cdot 5\sqrt 5 \left(\frac {\sec^3 \theta \tan \theta} 4 - \frac {5 \sec \theta \tan \theta} 8 + \frac {3 \ln \lvert \tan \theta + \sec \theta \rvert} 8 \right) + C \\
& = \operatorname{sgn}(x) \cdot 5\sqrt 5 \left(\frac {x^3 \sqrt{x^2 - 1} \operatorname{sgn}(x)} 4 - \frac {5 x \sqrt{x^2 - 1} \operatorname{sgn}(x)} 8 + \frac {3 \ln \left\lvert \sqrt{x^2 - 1} \operatorname{sgn}(x) + x \right\rvert} 8 \right) + C \\
& = 5\sqrt 5 \left(\frac {x^3 \sqrt{x^2 - 1} } 4 - \frac {5 x \sqrt{x^2 - 1} } 8 + \frac {3 \operatorname{sgn}(x) \ln \left\lvert \sqrt{x^2 - 1} \operatorname{sgn}(x) + x \right\rvert} 8 \right) + C \\
& = \begin{cases} 5\sqrt 5 \left(\frac {x^3 \sqrt{x^2 - 1} } 4 - \frac {5 x \sqrt{x^2 - 1} } 8 + \frac {3 \ln \left\lvert \sqrt{x^2 - 1} + x \right\rvert} 8 \right) + C, & x \ge 1 \\ 5\sqrt 5 \left(\frac {x^3 \sqrt{x^2 - 1} } 4 - \frac {5 x \sqrt{x^2 - 1} } 8 - \frac {3 \ln \left\lvert -\sqrt{x^2 - 1} + x \right\rvert} 8 \right) + C, & x \le -1 \end{cases} \\
& = \begin{cases} 5\sqrt 5 \left(\frac {x^3 \sqrt{x^2 - 1} } 4 - \frac {5 x \sqrt{x^2 - 1} } 8 + \frac {3 \ln \left\lvert \sqrt{x^2 - 1} + x \right\rvert} 8 \right) + C, & x \ge 1 \\ 5\sqrt 5 \left(\frac {x^3 \sqrt{x^2 - 1} } 4 - \frac {5 x \sqrt{x^2 - 1} } 8 + \frac {3 \ln \left\lvert \frac 1 {-\sqrt{x^2 - 1} + x} \right\rvert} 8 \right) + C, & x \le -1 \end{cases} \\
& = \frac {5 \sqrt 5 x^3 \sqrt{x^2 - 1} } 4 - \frac {25 \sqrt 5 x \sqrt{x^2 - 1} } 8 + \frac {15 \sqrt 5 \ln \left\lvert \sqrt{x^2 - 1} + x \right\rvert} 8 + C && \frac 1 {-\sqrt{x^2 - 1} + x} = \sqrt{x^2 - 1} + x
\end{aligned}$$
