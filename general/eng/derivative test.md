---
aliases:
  - concavity test
  - concavity tests
  - derivative test
  - derivative tests
  - first derivative test
  - first derivative tests
  - first-derivative test
  - first-derivative tests
  - general derivative test
  - general derivative tests
  - higher order derivative test
  - higher order derivative tests
  - higher-order derivative test
  - higher-order derivative tests
  - one sided first derivative test
  - one sided first derivative tests
  - one sided higher order derivative test
  - one sided higher order derivative tests
  - one sided second derivative test
  - one sided second derivative tests
  - one-sided first-derivative test
  - one-sided first-derivative tests
  - one-sided higher-order derivative test
  - one-sided higher-order derivative tests
  - one-sided second-derivative test
  - one-sided second-derivative tests
  - second derivative test
  - second derivative tests
  - second-derivative test
  - second-derivative tests
  - two sided first derivative test
  - two sided first derivative tests
  - two sided higher order derivative test
  - two sided higher order derivative tests
  - two sided second derivative test
  - two sided second derivative tests
  - two-sided first-derivative test
  - two-sided first-derivative tests
  - two-sided higher-order derivative test
  - two-sided higher-order derivative tests
  - two-sided second-derivative test
  - two-sided second-derivative tests
tags:
  - flashcard/active/general/eng/derivative_test
  - language/in/English
---

# derivative test

## single variable

### first derivative test

The _first derivative test_ can {@{determine [extrema](maximum%20and%20minimum.md) and whether a [function](function%20(mathematics).md) is increasing or decreasing at a point}@}. <!--SR:!2028-06-28,1310,359-->

> __first derivative test__
>
> 1. {@{Let $f:I\to\mathbb{R}$ be a [real-valued function](real-valued%20function.md). $I$ is an [interval](interval%20(mathematics).md) containing $c$. $f$ is [right/left-continuous](continuous%20function.md) at $c$, i.e. $\lim_{x\to{}c^\pm}f(x)=f(c)$, and [differentiable](differentiable%20function.md) on the immediate right/left of $c$, i.e. for some $\delta>0$, $f'(c\pm\epsilon)$ exists for all $\epsilon\in(0,\delta)$. (Choose either right (`+`) or left (`-`).)}@} (annotation: {@{One-sided continuity is required so that $f(c)$ cannot be an arbitrary value. Differentiability nearby (one-sided) is required by the conditions.}@})
> 2. {@{If there exists $\epsilon>0$ such that:<ul><li>(left (`-`)) $f'(x) \le 0$ ($f'(x) < 0$) for all $x\in(c-\epsilon,c)$, then $f$ has a [(strict) local minimum](maximum%20and%20minimum.md) at $c$ from the left.</li><li>(left (`-`)) $f'(x) \ge 0$ ($f'(x) > 0$) for all $x\in(c-\epsilon,c)$, then $f$ has a [(strict) local maximum](maximum%20and%20minimum.md) at $c$ from the left.</li><li>(right (`+`)) $f'(x) \le 0$ ($f'(x) < 0$) for all $x\in(c,c+\epsilon)$, then $f$ has a [(strict) local maximum](maximum%20and%20minimum.md) at $c$ from the right.</li><li>(right (`+`)) $f'(x) \ge 0$ ($f'(x) > 0$) for all $x\in(c,c+\epsilon)$, then $f$ has a [(strict) local minimum](maximum%20and%20minimum.md) at $c$ from the right.</li></ul>}@} (annotation: {@{Think of a graph and its first derivative.}@})
> 3. {@{If needed, combine the above conclusions from both sides. <p> Strictness of [extremum](maximum%20and%20minimum.md) at $c$ is preserved if and only if both sides are [strict local maxima](maximum%20and%20minimum.md) or both sides are [strict local minima](maximum%20and%20minimum.md).}@} <!--SR:!2027-08-09,831,259!2026-08-26,644,279!2026-05-20,627,319!2026-04-16,424,375!2025-11-04,291,355-->

The _one-sided first derivative test_ is {@{a variant of the first derivative test that covers a different set of functions. Neither of the two tests are stronger than the other}@}. <!--SR:!2028-01-25,1100,339-->

> __one-sided first derivative test__
>
> 1. {@{Let $f:I\to\mathbb{R}$ be a [real-valued function](real-valued%20function.md). $I$ is an [interval](interval%20(mathematics).md) containing $c$. $f$ is [right/left-differentiable](differentiable%20function.md) at $c$, i.e. $f'_\pm(c)$ exists. (Choose either right (`+`) or left (`-`).)}@} (annotation: {@{One-sided differentiability is required by the conditions. It automatically implies one-sided continuity.}@})
> 2. {@{then:<ul><li>If $f'_-(c)<0$, then $f$ has a [strict local minimum](maximum%20and%20minimum.md) at $c$ from the left.</li><li>If $f'_-(c)>0$, then $f$ has a [strict local maximum](maximum%20and%20minimum.md) at $c$ from the left.</li><li>If $f'_+(c)<0$, then $f$ has a [strict local maximum](maximum%20and%20minimum.md) at $c$ from the right.</li><li>If $f'_+(c)>0$, then $f$ has a [strict local minimum](maximum%20and%20minimum.md) at $c$ from the right.</li><li>Otherwise, the test is inconclusive.</li></ul>}@} (annotation: {@{Think of a graph and its first derivative.}@})
> 3. {@{If needed, combine the above conclusions from both sides. <p> Strictness of [extremum](maximum%20and%20minimum.md) at $c$ is preserved if and only if both sides are [strict local maxima](maximum%20and%20minimum.md) or both sides are [strict local minima](maximum%20and%20minimum.md).}@} <!--SR:!2025-10-29,403,239!2026-08-22,641,279!2026-01-03,493,329!2026-04-22,429,375!2025-12-17,306,355-->

<!-- markdownlint MD028 -->

> [!example] examples
>
> - $f(x):=\begin{cases}e^{-\frac1{x^2} }&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$ :@: [Strict local minimum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0. <!--SR:!2029-11-07,1502,319-->
> - $f(x):=-x^{2n+1}\text{ for }n\in\mathbb{N}^+,c=0$ :@: Decreasing (actually, weakly decreasing) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0. <!--SR:!2027-12-08,829,259-->
> - $f(x):=x^{2n+1}\text{ for }n\in\mathbb{N}^+,c=0$ :@: Increasing (actually, weakly increasing) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0. <!--SR:!2027-12-29,981,292-->
> - $f(x):=x^\frac{2n+1}2,n\in\mathbb{N}_0,c=0$ :@: [Right-sided strict local minimum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0 or do not exist. <!--SR:!2027-03-12,736,259-->
> - $f(x):=-x^{2n}\text{ for }n\in\mathbb{N}^+,c=0$ :@: [Strict local maximum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0. <!--SR:!2030-03-23,1696,319-->
> - $f(x):=\begin{cases}\lvert{x}\rvert\left(2+\sin{\frac1x}\right)&\text{if }\ne0\\0&\text{if }x=0\end{cases},c=0$ :@: Inconclusive by the two-sided test because no suitable $\epsilon$ exist and inconclusive by the one-sided test because the one-sided [derivaties](derivative.md) do not exist. Actual is [strict local minimum](maximum%20and%20minimum.md). <!--SR:!2026-05-05,221,279-->
> - $f(x):=x^{2n}\text{ for }n\in\mathbb{N}^+,c=0$ :@: [Strict local minimum](maximum%20and%20minimum.md) by the two-sided and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0. <!--SR:!2026-02-24,574,314-->
> - $f(x):=\lvert{x}\rvert,c=0$ :@: [Strict local minimum](maximum%20and%20minimum.md) by the two-sided or one-sided test. <!--SR:!2030-07-12,1779,319-->
> - $f(x):=x^\frac13,c=0$ :@: Increasing (actually, strictly increasing) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) do not exist. <!--SR:!2027-08-12,847,274-->
> - $f(x):=\begin{cases}x^2\sin{\frac1x}&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$ :@: Inconclusive by the two-sided test because no suitable $\epsilon$ exist and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are both 0. Actual is neither [local extremum](maximum%20and%20minimum.md) nor [inflection point](inflection%20point.md). <!--SR:!2027-01-09,791,319-->
> - $f(x):=x^\frac{2n+3}3,n\in\mathbb{N}^+,c=0$ :@: Increasing (actually, weakly increasing) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0. <!--SR:!2028-10-13,1189,299-->
> - $f(x):=\begin{cases}\lvert{x}\rvert\left(2+x\sin{\frac1x}\right)&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$ :@: Inconclusive by the two-sided test because no suitable $\epsilon$ exist and [strict local minimum](maximum%20and%20minimum.md) by the one-sided test. <!--SR:!2025-12-20,436,254-->
> - $f(x):=x^\frac{2n}3,n\in\mathbb{N}^+,c=0$ :@: [Strict local minimum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0 or do not exist. <!--SR:!2028-06-22,1103,294-->
> - $f(x):=\frac16\lvert{x}\rvert{}x^2,c=0$ :@: [Strict local minimum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0. <!--SR:!2029-07-13,1511,319-->

### concavity test

The [second derivative](second%20derivative.md) of a [function](function%20(mathematics).md) can {@{determine whether the [function](function%20(mathematics).md) is [concave up](convex%20function.md) or [concave down](concave%20function.md)}@}. A [twice-differentiable function](differentiable%20function.md) is {@{[concave up](convex%20function.md) if $f''(x)\ge0$, [_strictly_ concave up](convex%20function.md) if $f''(x)>0$, [concave down](concave%20function.md) if $f''(x)\le0$, and [_strictly_ concave down](concave%20function.md) if $f''(x)<0$}@}. <!--SR:!2027-10-02,1094,354!2026-07-09,663,319-->

### second derivative test

The _second derivative test_ is {@{a special case of $n=2$ in the [higher-order derivative test](#higher-order%20derivative%20test)}@}. The same applies for the _one-sided second derivative test_. <!--SR:!2028-06-04,1291,359-->

### higher-order derivative test

The _higher-order derivative test_ or _general derivative test_ can {@{determine [extrema](maximum%20and%20minimum.md), and [inflection points](inflection%20point.md) for sufficiently [differentiable functions](differentiable%20function.md)}@}. <!--SR:!2028-08-03,1339,359-->

> __higher-order derivative test__
>
> 1. {@{Let $f:I\to\mathbb{R}$ be a [real-valued](real-valued%20function.md) [$n$-times differentiable function](differentiable%20function.md) where $n\in\mathbb{N}_{\ge 2}$. $I$ is an [interval](interval%20(mathematics).md) $\in\mathbb{R}$ containing $c$.}@} (annotation: {@{$n$-times differentiability is required by the conditions. $n$-times differentiability automatically implies $n$-times continuity.}@})
> 2. {@{If $f'(c)=\cdots=f^{(n-1)}(c)=0$ and $f^{(n)}(c)\ne0$,}@}
> 3. {@{then:<ul><li>If $n$ is even and $f^{(n)}(c)<0$, $c$ is a [strict local maximum](maximum%20and%20minimum.md) of $f$. $f$ is weakly (strictly if $n = 2$) [concave](concave%20function.md) around $c$.</li><li>If $n$ is even and $f^{(n)}(c)>0$, $c$ is a [strict local minimum](maximum%20and%20minimum.md) of $f$. $f$ is weakly (strictly if $n = 2$) [convex](convex%20function.md) around $c$.</li><li>If $n$ is odd and $f^{(n)}(c)<0$, $c$ is a [stationary falling inflection point](inflection%20point.md) and not a [local extremum](maximum%20and%20minimum.md) of $f$.</li><li>If $n$ is odd and $f^{(n)}(c)>0$, $c$ is a [stationary rising inflection point](inflection%20point.md) and not a [local extremum](maximum%20and%20minimum.md) of $f$.</li></ul>}@}  (annotation: {@{One can memorize most of the above by considering the graph of a function $n = 1$ for odd $n$ and $n = 2$ for even $n$.}@}) <!--SR:!2030-05-12,1733,319!2028-01-08,1088,339!2030-03-22,1696,319!2025-09-29,222,295!2026-01-05,321,355-->

The _one-sided higher-order derivative test_ is {@{stronger than the two-sided higher-order derivative test, as the two-sided version can be derived from the one-sided one by combining conclusions}@}. <!--SR:!2027-11-29,1059,339-->

> __one-sided higher-order derivative test__
>
> 1. {@{Let $f:I\to\mathbb{R}$ be a [real-valued function](real-valued%20function.md). $I$ is an [interval](interval%20(mathematics).md) containing $c$. $f$ is [$n-1$-times differentiable](differentiable%20function.md) on the immediate right/left of $c$ where $n\in\mathbb{N}_{\ge 2}$, i.e. for some $\delta>0$, $f^{(n-1)}(c\pm\epsilon)$ exists for all $\epsilon\in(0,\delta)$. $f$ is also $n$-times right/left-differentiable at $c$, i.e. $f^{(n)}_\pm(c)$ exists. (Choose either right (`+`) or left (`-`).)}@} (annotation: {@{One-sided $n$-times differentiability is required by the conditions. One-sided $n$-times differentiability and $n - 1$-times differentiability nearby (one-sided) together automatically implies one-sided $n$-times continuity.}@})
> 2. {@{If $f'_\pm(c)=\cdots=f^{(n-1)}_\pm(c)=0$ and $f^{(n)}_\pm(c)\ne0$, (Choose either right (`+`) or left (`-`).)}@}
> 3. {@{then:<ul><li>If $n$ is even and $f^{(n)}_-(c)<0$, $c$ is a [strict local maximum](maximum%20and%20minimum.md) of $f$ from the left. $f$ is [strictly concave](concave%20function.md) to the immediate left of $c$.</li><li>If $n$ is even and $f^{(n)}_-(c)>0$, $c$ is a [strict local minimum](maximum%20and%20minimum.md) of $f$ from the left. $f$ is [strictly convex](convex%20function.md) to the immediate left of $c$.</li><li>If $n$ is odd and $f^{(n)}_-(c)<0$, $c$ is a [strict local minimum](maximum%20and%20minimum.md) of $f$ from the left. $f$ is [strictly convex](convex%20function.md) to the immediate left of $c$.</li><li>If $n$ is odd and $f^{(n)}_-(c)>0$, $c$ is a [strict local maximum](maximum%20and%20minimum.md) of $f$ from the left. $f$ is [strictly concave](concave%20function.md) to the immediate left of $c$.</li><li>If $f^{(n)}_+(c)<0$, $c$ is a [strict local maximum](maximum%20and%20minimum.md) of $f$ from the right. $f$ is [strictly concave](concave%20function.md) to the immediate right of $c$.</li><li>If $f^{(n)}_+(c)>0$, $c$ is a [strict local minimum](maximum%20and%20minimum.md) of $f$ from the right. $f$ is [strictly convex](convex%20function.md) to the immediate right of $c$.</li></ul>}@} (annotation: {@{One can memorize most of the above by considering the graph of a function when $n = 1$ for odd $n$ and $n = 2$ for even $n$.}@})
> 4. {@{If needed, combine the above conclusions from both sides. <p> Strictness of [extremum](maximum%20and%20minimum.md) at $c$ is preserved if and only if both sides are [strict local maxima](maximum%20and%20minimum.md) or both sides are [strict local minima](maximum%20and%20minimum.md). <p> When both sides have the same concavity, concavity at $c$ is always weak, except when $f''_+(c) < 0, f''_-(c) < 0$ or $f''_+(c) > 0, f''_-(c) > 0$, in which case it is strict. <p> Any [inflection point](inflection%20point.md) at $c$ is always stationary and not a local [extremum](maximum%20and%20minimumm.md).}@} <!--SR:!2027-10-24,875,259!2027-10-17,1027,339!2026-01-15,424,259!2028-09-10,1143,309!2027-02-22,636,335!2026-07-30,438,315-->

<!-- markdownlint MD028 -->

> [!tip] tips
>
> - [intuition](intuition.md) ::@:: Notice that for a [continuous](continuous%20function.md) $n$-th derivative that is 0 at $c$, i.e. $f^{(n)}(c)=0$, the [sign](sign%20(mathematics).md) of the two-sided or one-sided $n+1$-th derivative at $c$ $f^{(n+1)}_\pm(c)$ determines whether $f^{(n)}$ is larger or smaller than 0 to the immediate left or right of $c$. Repeat this until the [first derivative](derivative.md) $f'$ is reached to prove [extrema](maximum%20and%20minimum.md) and the [second derivative](second%20derivative.md) $f''$ is reached to prove convexities. <!--SR:!2027-09-11,927,299!2026-11-18,693,335-->

<!-- markdownlint MD028 -->

> [!example] examples
>
> - $f(x):=-x^{2n}\text{ for }n\in\mathbb{N}^+,c=0$ :@: [Strict local maximum](maximum%20and%20minimum.md) and weakly (strictly when $n = 1$) [concave](convex%20function.md). <!--SR:!2028-10-14,1181,294-->
> - $f(x):=x^{2n}\text{ for }n\in\mathbb{N}^+,c=0$ :@: [Strict local minimum](maximum%20and%20minimum.md) and weakly (strictly when $n = 1$) [convex](convex%20function.md). <!--SR:!2026-05-10,464,270-->
> - $f(x):=x^\frac{2n}3,n\in\mathbb{N}^+ \setminus \set{n \in \mathbb N^+ : 3 \mid n},c=0$ :@: Inconclusive because no $d\in\mathbb{N}^+$ such that $f^{(d)}(0)$ exists and $f^{(d)}(0)\ne0$. Actual is [strict local minimum](maximum%20and%20minimum.md). <!--SR:!2028-10-16,1135,274-->
> - $f(x):=x\lvert{x}\rvert,c=0$ :@: Inconclusive by the two-sided test and [stationary rising inflection point](maximum%20and%20minimum.md) and not local [extremum](maximum%20and%20minimumm.md) by the one-sided test. <!--SR:!2026-04-18,557,279-->
> - $f(x):=x^{2n+1}\text{ for }n\in\mathbb{N}^+,c=0$ :@: [Stationary rising inflection point](inflection%20point.md) and not local [extremum](maximum%20and%20minimumm.md). <!--SR:!2026-06-25,597,272-->
> - $f(x):=\begin{cases}e^{-\frac1{x^2} }&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$ :@: Inconclusive because $\forall{n\in\mathbb{N}^+}\,f^{(n)}(0)=0$. Actual is [strict local minimum](maximum%20and%20minimum.md). <!--SR:!2028-05-05,1269,359-->
> - $f(x):=x^\frac{2n+1}2,n\in\mathbb{N}_0,c=0$ :@: Inconclusive because no $d\in\mathbb{N}^+$ such that $f^{(d)}(0)$ exists and $f^{(d)}(0)\ne0$. Actual is [right-sided strict local minimum](maximum%20and%20minimum.md). <!--SR:!2027-04-18,799,279-->
> - $f(x):=-x^{2n+1}\text{ for }n\in\mathbb{N}^+,c=0$ :@: [stationary falling inflection point](inflection%20point.md) and not [local extremum](maximum%20and%20minimum.md). <!--SR:!2030-05-11,1733,319-->
> - $f(x):=x^\frac13,c=0$ :@: Inconclusive because $f^{(n)}(0)$ for all $n\in\mathbb{N}^+$ does not exist $(f^{(n)}(0)=\pm\infty)$. Actual is [vertically rising inflection point](inflection%20point.md). <!--SR:!2026-01-01,563,312-->
> - $f(x):=x^\frac{2n+3}3,n\in\mathbb{N}^+ \setminus \set{n \in \mathbb N^+ : 3 \mid n},c=0$ :@: Inconclusive because no $d\in\mathbb{N}^+$ such that $f^{(d)}(0)$ exists and $f^{(d)}(0)\ne0$. Actual is [stationary rising inflection point](inflection%20point.md). <!--SR:!2025-12-07,294,259-->
> - $f(x):=\frac16\lvert{x}\rvert{}x^2,c=0$ :@: Inconclusive by the two-sided test and [strict local minimum](maximum%20and%20minimum.md) by the one-sided test. <!--SR:!2027-10-20,879,274-->
> - $f(x):=\begin{cases}x^2\sin{\frac1x}&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$ :@: Inconclusive because the two-sided [second derivative](second%20derivative.md) $f''(0)$ and one-sided [second derivatives](second%20derivative.md) $f''_\pm(0)$ do not exist. Actual is neither [local extremum](maximum%20and%20minimum.md) nor [inflection point](inflection%20point.md). <!--SR:!2026-08-26,536,279-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/derivative_test) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
