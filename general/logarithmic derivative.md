---
aliases:
  - log derivative
  - logarithmic derivative
tags:
  - flashcards/general/logarithmic_derivative
  - languages/in/English
---

# logarithmic derivative

The __logarithmic derivative__ of a [function](function%20(mathematics).md) is defined by {{$\frac {f'} f$ when $f \ne 0$}}. Intuitively, this is the {{infinitesimal [relative change](relative%20change.md) in $f$}}. <!--SR:!2024-04-12,56,310!2024-04-18,61,310-->

When $f$ is {{$f: \mathbb{R} \to \mathbb{R}_{\ne 0}$, then the logarithmic derivative equals the derivative of $\ln \lvert f \rvert$, and hence its name}}. This follows directly from {{the [chain rule](chain%20rule.md): $(\ln \lvert f \rvert)' = \frac 1 {\lvert f \rvert} \cdot \operatorname{sgn}(f) \cdot f' = \frac {f'} f$}}. <!--SR:!2024-04-13,57,310!2024-02-18,17,290-->

## basic properties

{{Many properties of the real [logarithm](logarithm.md)}} applies to the logarithmic derivative whenever $f \ne 0$. This can be easily seen from {{[linearity of differentiation](linearity%20of%20differentiation.md)}}. See [list of logarithmic identities](list%20of%20logarithmic%20identities.md). <!--SR:!2024-02-18,17,290!2024-04-09,54,310-->

### select properties

- functional [power rule](power%20rule.md) ::: $$\frac {(x^y)'} {x^y} = y \frac {x'} x + y' \ln x \qquad x > 0$$ <!--SR:!2024-03-15,27,230!2024-04-10,55,310-->
- [power rule](power%20rule.md) ::: $$\frac {(u^k)'} {u^k} = k \frac {u'} u \qquad u > 0, k = \mathrm{const} $$ <!--SR:!2024-04-04,50,310!2024-04-16,60,310-->
- [product rule](product%20rule.md) ::: $$\frac {(\prod _{i = 1} ^n x_i)'} {\prod _{i = 1} ^n x_i} = \sum _{i = 1} ^n \frac {x_i'} {x_i}$$ <!--SR:!2024-04-14,58,310!2024-04-02,48,310-->
- [quotient rule](quotient%20rule.md) ::: $$\frac {(u / v)'} {u / v} = \frac {u'} u - \frac {v'} v$$ <!--SR:!2024-02-18,17,290!2024-04-19,62,310-->
- [reciprocal rule](reciprocal%20rule.md) ::: $$\frac {(1 / f)'} {1 / f} = -\frac {f'} f$$ <!--SR:!2024-04-08,53,310!2024-04-15,60,310-->

> [!example] examples
>
> Define $\operatorname{Logder}(f)$ to be the logarithmic derivative of $f$.
>
> - $f := (7xy)^5, \operatorname{Logder}(f) = ?$ :: $\operatorname{Logder}(f) = 5 \frac {x'} x + 5 \frac {y'} y$ <!--SR:!2024-04-03,49,310-->
> - $f := -2.692u, \operatorname{Logder}(f) = ?$ :: $\operatorname{Logder} = \frac {u'} u$ <!--SR:!2024-04-06,52,310-->
> - $f := -\frac {(78.38uvw)^{8.39}} {(59.2xy)^{9682} z^{-386}}, \operatorname{Logder}(f) = ?$ :: $\operatorname{Logder}(f) = 8.39 \frac {u'} u + 8.39 \frac {v'} v + 8.39 \frac {w'} w - 9682 \frac {x'} x - 9682 \frac {y'} y + 386 \frac {z'} z$ <!--SR:!2024-03-19,37,290-->
> - $f := 4 x^{2y}, \operatorname{Logder}(f) = ?$ :: $\operatorname{Logder}(f) = 2y \frac {x'} x + 2y y' \ln x \qquad x > 0$ <!--SR:!2024-02-27,19,250-->
> - $f := e^{x^{-2}} (x - 3)^2 \left(z^2 + 1\right)^{42} (y - 5)^{x^2}, \operatorname{Logder}(f) = ?$ :: $\operatorname{Logder}(f) = -2 x^{-3} x' + 2 \frac {x'} {x - 3} + 42 \frac {2zz'} {z^2 + 1} + x^2 \frac {y'} {y - 5} + 2xx' \ln (y - 5) \qquad y > 5$ <!--SR:!2024-02-26,19,250-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/logarithmic_derivative) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
