---
aliases:
  - log derivative
  - logarithmic derivative
tags:
  - flashcard/general/logarithmic_derivative
  - language/in/English
---

# logarithmic derivative

The __logarithmic derivative__ of a [function](function%20(mathematics).md) is defined by {{$\frac {f'} f$ when $f \ne 0$}}. Intuitively, this is the {{infinitesimal [relative change](relative%20change.md) in $f$}}. <!--SR:!2024-12-07,239,330!2025-01-04,261,330-->

When $f$ is {{$f: \mathbb{R} \to \mathbb{R}_{\ne 0}$, then the logarithmic derivative equals the derivative of $\ln \lvert f \rvert$, and hence its name}}. This follows directly from {{the [chain rule](chain%20rule.md): $(\ln \lvert f \rvert)' = \frac 1 {\lvert f \rvert} \cdot \operatorname{sgn}(f) \cdot f' = \frac {f'} f$}}. <!--SR:!2024-10-08,176,310!2025-02-21,299,330-->

## basic properties

{{Many properties of the real [logarithm](logarithm.md)}} applies to the logarithmic derivative whenever $f \ne 0$. This can be easily seen from {{[linearity of differentiation](linearity%20of%20differentiation.md)}}. See [list of logarithmic identities](list%20of%20logarithmic%20identities.md). <!--SR:!2025-02-27,304,330!2024-11-26,231,330-->

### select properties

- functional [power rule](power%20rule.md) ::: $$\frac {(x^y)'} {x^y} = y \frac {x'} x + y' \ln x \qquad x > 0$$ <!--SR:!2024-05-15,61,230!2024-09-27,170,310-->
- [power rule](power%20rule.md) ::: $$\frac {(u^k)'} {u^k} = k \frac {u'} u \qquad u > 0, k = \mathrm{const} $$ <!--SR:!2024-09-05,154,310!2024-12-28,256,330-->
- [product rule](product%20rule.md) ::: $$\frac {(\prod _{i = 1} ^n x_i)'} {\prod _{i = 1} ^n x_i} = \sum _{i = 1} ^n \frac {x_i'} {x_i}$$ <!--SR:!2024-12-19,248,330!2024-10-25,205,330-->
- [quotient rule](quotient%20rule.md) ::: $$\frac {(u / v)'} {u / v} = \frac {u'} u - \frac {v'} v$$ <!--SR:!2024-12-10,224,310!2025-01-09,265,330-->
- [reciprocal rule](reciprocal%20rule.md) ::: $$\frac {(1 / f)'} {1 / f} = -\frac {f'} f$$ <!--SR:!2024-09-18,163,310!2024-10-16,184,310-->

> [!example] examples
>
> Define $\operatorname{Logder}(f)$ to be the logarithmic derivative of $f$.
>
> - $f := (7xy)^5, \operatorname{Logder}(f) = ?$ :: $\operatorname{Logder}(f) = 5 \frac {x'} x + 5 \frac {y'} y$ <!--SR:!2024-10-29,209,330-->
> - $f := -2.692u, \operatorname{Logder}(f) = ?$ :: $\operatorname{Logder} = \frac {u'} u$ <!--SR:!2024-09-14,159,310-->
> - $f := -\frac {(78.38uvw)^{8.39}} {(59.2xy)^{9682} z^{-386}}, \operatorname{Logder}(f) = ?$ :: $\operatorname{Logder}(f) = 8.39 \frac {u'} u + 8.39 \frac {v'} v + 8.39 \frac {w'} w - 9682 \frac {x'} x - 9682 \frac {y'} y + 386 \frac {z'} z$ <!--SR:!2024-07-03,106,290-->
> - $f := 4 x^{2y}, \operatorname{Logder}(f) = ?$ :: $\operatorname{Logder}(f) = 2y \frac {x'} x + 2y y' \ln 4x \qquad x > 0$ <!--SR:!2024-11-05,183,270-->
> - $f := e^{x^{-2}} (x - 3)^2 \left(z^2 + 1\right)^{42} (y - 5)^{x^2}, \operatorname{Logder}(f) = ?$ :: $\operatorname{Logder}(f) = -2 x^{-3} x' + 2 \frac {x'} {x - 3} + 42 \frac {2zz'} {z^2 + 1} + x^2 \frac {y'} {y - 5} + 2xx' \ln (y - 5) \qquad y > 5$ <!--SR:!2024-08-08,115,250-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/logarithmic_derivative) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
