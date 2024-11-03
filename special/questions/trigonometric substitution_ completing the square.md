---
aliases:
  - 'trigonometric substitution: completing the square'
tags:
  - date/2024/07/01
  - flashcard/active/special/questions/trigonometric_substitution__completing_the_square
  - language/in/English
  - question/mathematics/calculus/integral
---

# trigonometric substitution: completing the square

- datetime: 2024-07-01T16:09:53.702+08:00

Evaluate $$\int \! x \sqrt{4x^2 - 40x + 92} \,\mathrm{d}x$$.

## strategy

- inspecting "$$\int \! x \sqrt{4x^2 - 40x + 92} \,\mathrm{d}x$$" :: Extract the factor $2$ from inside the square root. Complete the square to get $\sqrt{(x - 5)^2 - 2}$. Substitute $x - 5 = \sqrt 2 \sec \theta \quad \theta \in \left[0, \frac \pi 2\right) \cup \left(\frac \pi 2, \pi \right]$.
- logarithm simplification tricks :: First, $\ln(a(x + y)) + C = \ln a + \ln(x + y) + C$, of which $\ln a$ can be absorbed into $C$ to become $\ln(x + y) + C$. Second, $\ln \left\lvert a + \sqrt{a^2 \pm 1} \right\rvert = -\ln \left\lvert a - \sqrt{a^2 \pm 1} \right\rvert$.

## solution

$$\begin{aligned}
x & := \sqrt 2 \sec \theta + 5 \quad \theta \in \left[0, \frac \pi 2\right) \cup \left(\frac \pi 2, \pi \right] \\
\\
& \phantom = \int \! x \sqrt{4x^2 - 40x + 92} \,\mathrm{d}x \\
& = 2 \int \! x \sqrt{x^2 - 10x + 23} \,\mathrm{d}x \\
& = 2 \int \! x \sqrt{(x - 5)^2 - 2} \,\mathrm{d}x \\
& = 2 \int \left(\sqrt 2 \sec \theta + 5 \right) \sqrt{2 \sec^2 \theta - 2} \sqrt 2 \tan \theta \sec \theta \,\mathrm{d}\theta \\
& = 4 \int \left(\sqrt 2 \sec \theta + 5 \right) \lvert \tan \theta \rvert \tan \theta \sec \theta \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\tan \theta) \cdot 4 \int \left(\sqrt 2 \sec \theta + 5 \right) \tan^2 \theta \sec \theta \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\tan \theta) \cdot 4 \int \left( \sqrt 2 \tan^2 \theta \sec^2 \theta + 5 \tan^2 \theta \sec \theta \right) \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\tan \theta) \cdot 4 \int \left( \sqrt 2 \tan^2 \theta \sec^2 \theta + 5 \sec^3 \theta - 5 \sec \theta \right) \,\mathrm{d}\theta \\
& = \operatorname{sgn}(\tan \theta) \cdot 4 \left(\frac {\sqrt 2} 3 \tan^3 \theta + 5 \int \! \sec^3 \theta \,\mathrm{d}\theta - 5 \int \! \sec \theta \,\mathrm{d}\theta \right) \\
& = \operatorname{sgn}(\tan \theta) \cdot 4 \left(\frac {\sqrt 2} 3 \tan^3 \theta + \frac {5 \sec \theta \tan \theta} 2 - \frac 5 2 \int \! \sec \theta \,\mathrm{d}\theta \right) \\
& = \operatorname{sgn}(\tan \theta) \cdot 4 \left(\frac {\sqrt 2} 3 \tan^3 \theta + \frac {5 \sec \theta \tan \theta} 2 - \frac {5 \ln \lvert \sec \theta + \tan \theta \rvert} 2 \right) + C \\
& = \operatorname{sgn}\left(\operatorname{sgn}(x - 5) \sqrt{ \left(\frac {x - 5} {\sqrt 2} \right)^2 - 1} \right) \cdot 4 \left(\frac {\sqrt 2} 3 \operatorname{sgn}(x - 5) \left( \left(\frac {x - 5} {\sqrt 2} \right)^2 - 1 \right)^{\frac 3 2} \right. \\
& \phantom = + \left. \frac {5 \frac {x - 5} {\sqrt 2} \operatorname{sgn}(x - 5) \sqrt{ \left(\frac {x - 5} {\sqrt 2} \right)^2 - 1} } 2 \right. \\
& \phantom = \left. - \frac {5 \ln \left\lvert \frac {x - 5} {\sqrt 2} + \operatorname{sgn}(x - 5) \sqrt{ \left(\frac {x - 5} {\sqrt 2} \right)^2 - 1} \right\rvert} 2 \right) + C \\
& = 4 \left(\frac {\sqrt 2} 3 \left( \left(\frac {x - 5} {\sqrt 2} \right)^2 - 1 \right)^{\frac 3 2} \right. \\
& \phantom = + \left. \frac {5 \frac {x - 5} {\sqrt 2} \sqrt{ \left(\frac {x - 5} {\sqrt 2} \right)^2 - 1} } 2 \right. \\
& \phantom = \left. - \frac {5 \ln \left\lvert \frac {x - 5} {\sqrt 2} + \sqrt{ \left(\frac {x - 5} {\sqrt 2} \right)^2 - 1} \right\rvert} 2 \right) + C  && \ln \left\lvert \frac {x - 5} {\sqrt 2} + \sqrt{ \left(\frac {x - 5} {\sqrt 2} \right)^2 - 1} \right\rvert = -\ln \left\lvert \frac {x - 5} {\sqrt 2} - \sqrt{ \left(\frac {x - 5} {\sqrt 2} \right)^2 - 1} \right\rvert \\
& = \frac {4\sqrt 2} 3 \left( \frac {x^2 - 10x + 23} 2 \right)^{\frac 3 2} + 10 \frac {x - 5} {\sqrt 2} \sqrt{ \frac {x^2 - 10x + 23} 2} \\
& \phantom = - 10 \ln \left\lvert \frac {x - 5} {\sqrt 2} + \sqrt{ \frac {x^2 - 10x + 23} 2} \right\rvert + C \\
& = \frac 2 3 \left(x^2 - 10x + 23 \right)^{\frac 3 2} + 5 (x - 5) \sqrt{x^2 - 10x + 23} \\
& \phantom = - 10 \ln \left\lvert x - 5 + \sqrt{x^2 - 10x + 23} \right\rvert + C \\
\end{aligned}$$
