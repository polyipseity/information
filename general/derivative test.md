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
  - flashcards/general/derivative_test
  - languages/in/English
---

# derivative test

## single variable

### first derivative test

The _first derivative test_ can {{determine [extrema](maximum%20and%20minimum.md) and whether a [function](function%20(mathematics).md) is increasing or decreasing at a point}}. <!--SR:!2024-02-19,64,319-->

> __first derivative test__
>
> 1. {{Let $f:I\to\mathbb{R}$ be a [real-valued function](real-valued%20function.md). $I$ is an [interval](interval%20(mathematics).md) containing $c$. $f$ is [right/left-continuous](continuous%20function.md) at $c$, i.e. $\lim_{x\to{}c^\pm}f(x)=f(c)$, and [differentiable](differentiable%20function.md) on the immediate right/left of $c$, i.e. for some $\delta>0$, $f'(c\pm\epsilon)$ exists for all $\epsilon\in(0,\delta)$. (Choose either right (`+`) or left (`-`).)}}
> 2. {{If there exists $\epsilon>0$ such that:<ul><li>(left (`-`)) $f'(x) \le 0$ ($f'(x) < 0$) for all $x\in(c-\epsilon,c)$, then $f$ has a [(strict) local minimum](maximum%20and%20minimum.md) at $c$ from the left.</li><li>(left (`-`)) $f'(x) \ge 0$ ($f'(x) > 0$) for all $x\in(c-\epsilon,c)$, then $f$ has a [(strict) local maximum](maximum%20and%20minimum.md) at $c$ from the left.</li><li>(right (`+`)) $f'(x) \le 0$ ($f'(x) < 0$) for all $x\in(c,c+\epsilon)$, then $f$ has a [(strict) local maximum](maximum%20and%20minimum.md) at $c$ from the right.</li><li>(right (`+`)) $f'(x) \ge 0$ ($f'(x) > 0$) for all $x\in(c,c+\epsilon)$, then $f$ has a [(strict) local minimum](maximum%20and%20minimum.md) at $c$ from the right.</li></ul>}}
> 3. {{If needed, combine the above conclusions from both sides. Strictness of [extremum](maximum%20and%20minimum.md) at $c$ is preserved if and only if both sides are [strict local maxima](maximum%20and%20minimum.md) or both sides are [strict local minima](maximum%20and%20minimum.md).}} <!--SR:!2024-02-14,48,259!2024-04-03,83,279!2024-02-16,62,319-->

The _one-sided first derivative test_ is {{a variant of the first derivative test that covers a different set of functions. Neither of the two tests are stronger than the other}}. <!--SR:!2024-03-01,74,319-->

> __one-sided first derivative test__
>
> 1. {{Let $f:I\to\mathbb{R}$ be a [real-valued function](real-valued%20function.md). $I$ is an [interval](interval%20(mathematics).md) containing $c$. $f$ is [right/left-differentiable](differentiable%20function.md) at $c$, i.e. $f'_\pm(c)$ exists. (Choose either right (`+`) or left (`-`).)}}
> 2. {{then:<ul><li>If $f'_-(c)<0$, then $f$ has a [strict local minimum](maximum%20and%20minimum.md) at $c$ from the left.</li><li>If $f'_-(c)>0$, then $f$ has a [strict local maximum](maximum%20and%20minimum.md) at $c$ from the left.</li><li>If $f'_+(c)<0$, then $f$ has a [strict local maximum](maximum%20and%20minimum.md) at $c$ from the right.</li><li>If $f'_+(c)>0$, then $f$ has a [strict local minimum](maximum%20and%20minimum.md) at $c$ from the right.</li><li>Otherwise, the test is inconclusive.</li></ul>}}
> 3. {{If needed, combine the above conclusions from both sides. Strictness of [extremum](maximum%20and%20minimum.md) at $c$ is preserved if and only if both sides are [strict local maxima](maximum%20and%20minimum.md) or both sides are [strict local minima](maximum%20and%20minimum.md).}} <!--SR:!2024-04-04,71,239!2024-04-02,82,279!2024-02-12,11,309-->

<!-- markdownlint MD028 -->

> [!example] examples
>
> - $f(x):=\begin{cases}e^{-\frac1{x^2} }&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$: {{[Strict local minimum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
> - $f(x):=-x^{2n+1}\text{ for }n\in\mathbb{N}^+,c=0$: {{Decreasing (actually, weakly decreasing) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
> - $f(x):=x^{2n+1}\text{ for }n\in\mathbb{N}^+,c=0$: {{Increasing (actually, weakly increasing) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
> - $f(x):=x^\frac{2n+1}2,n\in\mathbb{N}_0,c=0$: {{[Right-sided strict local minimum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
> - $f(x):=-x^{2n}\text{ for }n\in\mathbb{N}^+,c=0$: {{[Strict local maximum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
> - $f(x):=\begin{cases}\lvert{x}\rvert\left(2+\sin{\frac1x}\right)&\text{if }\ne0\\0&\text{if }x=0\end{cases},c=0$: {{Inconclusive by the two-sided test because no suitable $\epsilon$ exist and inconclusive by the one-sided test because the one-sided [derivaties](derivative.md) do not exist. Actual is [strict local minimum](maximum%20and%20minimum.md).}}
> - $f(x):=x^{2n}\text{ for }n\in\mathbb{N}^+,c=0$: {{[Strict local minimum](maximum%20and%20minimum.md) by the two-sided and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
> - $f(x):=\lvert{x}\rvert,c=0$: {{[Strict local minimum](maximum%20and%20minimum.md) by the two-sided or one-sided test.}}
> - $f(x):=x^\frac13,c=0$: {{Increasing (actually, strictly increasing) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) do not exist.}}
> - $f(x):=\begin{cases}x^2\sin{\frac1x}&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$: {{Inconclusive by the two-sided test because no suitable $\epsilon$ exist and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are both 0. Actual is neither [local extremum](maximum%20and%20minimum.md) nor [inflection point](inflection%20point.md).}}
> - $f(x):=x^\frac{2n+3}3,n\in\mathbb{N}^+,c=0$: {{Increasing (actually, weakly increasing) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
> - $f(x):=\begin{cases}\lvert{x}\rvert\left(2+x\sin{\frac1x}\right)&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$: {{Inconclusive by the two-sided test because no suitable $\epsilon$ exist and [strict local minimum](maximum%20and%20minimum.md) by the one-sided test.}}
> - $f(x):=x^\frac{2n}3,n\in\mathbb{N}^+,c=0$: {{[Strict local minimum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0 or do not exist.}}
> - $f(x):=\frac16\lvert{x}\rvert{}x^2,c=0$: {{[Strict local minimum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}} <!--SR:!2024-06-13,148,319!2024-04-24,97,279!2024-05-19,116,292!2024-02-06,43,259!2024-06-17,137,299!2024-07-03,151,299!2024-07-30,183,314!2024-06-24,143,299!2024-02-20,32,254!2024-03-06,78,319!2024-06-09,133,299!2024-02-12,27,254!2024-06-05,128,294!2024-05-24,122,299-->

### concavity test

The [second derivative](second%20derivative.md) of a [function](function%20(mathematics).md) can {{determine whether the [function](function%20(mathematics).md) is [concave up](convex%20function.md) or [concave down](concave%20function.md)}}. A [twice-differentiable function](differentiable%20function.md) is {{[concave up](convex%20function.md) if $f''(x)\ge0$, [_strictly_ concave up](convex%20function.md) if $f''(x)>0$, [concave down](concave%20function.md) if $f''(x)\le0$, and [_strictly_ concave down](concave%20function.md) if $f''(x)<0$}}. <!--SR:!2024-02-08,55,314!2024-02-19,65,319-->

### second derivative test

The _second derivative test_ is {{a special case of $n=2$ in the [higher-order derivative test](#higher-order%20derivative%20test)}}. The same applies for the _one-sided second derivative test_. <!--SR:!2024-02-18,63,319-->

### higher-order derivative test

The _higher-order derivative test_ or _general derivative test_ can {{determine [extrema](maximum%20and%20minimum.md), and [inflection points](inflection%20point.md) for sufficiently [differentiable functions](differentiable%20function.md)}}. <!--SR:!2024-02-19,65,319-->

> __higher-order derivative test__
>
> 1. {{Let $f:I\to\mathbb{R}$ be a [real-valued](real-valued%20function.md) [$n$-times differentiable function](differentiable%20function.md) where $n\in\mathbb{N}_{\ge 2}$. $I$ is an [interval](interval%20(mathematics).md) $\in\mathbb{R}$ containing $c$.}}
> 2. {{If $f'(c)=\cdots=f^{(n-1)}(c)=0$ and $f^{(n)}(c)\ne0$,}}
> 3. {{then:<ul><li>If $n$ is even and $f^{(n)}(c)<0$, $c$ is a [strict local maximum](maximum%20and%20minimum.md) of $f$. $f$ is weakly (strictly if $n = 2$) [concave](concave%20function.md) around $c$.</li><li>If $n$ is even and $f^{(n)}(c)>0$, $c$ is a [strict local minimum](maximum%20and%20minimum.md) of $f$. $f$ is weakly (strictly if $n = 2$) [convex](convex%20function.md) around $c$.</li><li>If $n$ is odd and $f^{(n)}(c)<0$, $c$ is a [stationary falling inflection point](inflection%20point.md) and not a [local extremum](maximum%20and%20minimum.md) of $f$.</li><li>If $n$ is odd and $f^{(n)}(c)>0$, $c$ is a [stationary rising inflection point](inflection%20point.md) and not a [local extremum](maximum%20and%20minimum.md) of $f$.</li></ul>}} <!--SR:!2024-06-21,140,299!2024-02-29,73,319!2024-06-16,137,299-->

The _one-sided higher-order derivative test_ is {{stronger than the two-sided higher-order derivative test, as the two-sided version can be derived from the one-sided one by combining conclusions}}. <!--SR:!2024-02-27,71,319-->

> __one-sided higher-order derivative test__
>
> 1. {{Let $f:I\to\mathbb{R}$ be a [real-valued function](real-valued%20function.md). $I$ is an [interval](interval%20(mathematics).md) containing $c$. $f$ is [$n-1$-times differentiable](differentiable%20function.md) on the immediate right/left of $c$ where $n\in\mathbb{N}_{\ge 2}$, i.e. for some $\delta>0$, $f^{(n-1)}(c\pm\epsilon)$ exists for all $\epsilon\in(0,\delta)$. $f$ is also $n$-times right/left-differentiable at $c$, i.e. $f^{(n)}_\pm(c)$ exists. (Choose either right (`+`) or left (`-`).)}}
> 2. {{If $f'_\pm(c)=\cdots=f^{(n-1)}_\pm(c)=0$ and $f^{(n)}_\pm(c)\ne0$, (Choose either right (`+`) or left (`-`).)}}
> 3. {{then:<ul><li>If $n$ is even and $f^{(n)}_-(c)<0$, $c$ is a [strict local maximum](maximum%20and%20minimum.md) of $f$ from the left. $f$ is [strictly concave](concave%20function.md) to the immediate left of $c$.</li><li>If $n$ is even and $f^{(n)}_-(c)>0$, $c$ is a [strict local minimum](maximum%20and%20minimum.md) of $f$ from the left. $f$ is [strictly convex](convex%20function.md) to the immediate left of $c$.</li><li>If $n$ is odd and $f^{(n)}_-(c)<0$, $c$ is a [strict local minimum](maximum%20and%20minimum.md) of $f$ from the left. $f$ is [strictly convex](convex%20function.md) to the immediate left of $c$.</li><li>If $n$ is odd and $f^{(n)}_-(c)>0$, $c$ is a [strict local maximum](maximum%20and%20minimum.md) of $f$ from the left. $f$ is [strictly concave](concave%20function.md) to the immediate left of $c$.</li><li>If $f^{(n)}_+(c)<0$, $c$ is a [strict local maximum](maximum%20and%20minimum.md) of $f$ from the right. $f$ is [strictly concave](concave%20function.md) to the immediate right of $c$.</li><li>If $f^{(n)}_+(c)>0$, $c$ is a [strict local minimum](maximum%20and%20minimum.md) of $f$ from the right. $f$ is [strictly convex](convex%20function.md) to the immediate right of $c$.</li></ul>}}
> 4. {{If needed, combine the above conclusions from both sides. When both sides have the same concavity, concavity around $c$ is always weak, except when $f''_+(c) < 0, f''_-(c) < 0$ or $f''_+(c) > 0, f''_-(c) > 0$, in which case it is strict. Any [inflection point](inflection%20point.md) at $c$ is always stationary and not a local [extremum](maximum%20and%20minimumm.md).}} <!--SR:!2024-02-18,51,259!2024-02-25,69,319!2024-05-22,108,259!2024-02-10,10,289-->

<!-- markdownlint MD028 -->

> [!tip] tip
>
> - [intuition](intuition.md): {{Notice that for a [continuous](continuous%20function.md) $n$-th derivative that is 0 at $c$, i.e. $f^{(n)}(c)=0$, the [sign](sign%20(mathematics).md) of the two-sided or one-sided $n+1$-th derivative at $c$ $f^{(n+1)}_\pm(c)$ determines whether $f^{(n)}$ is larger or smaller than 0 to the immediate left or right of $c$. Repeat this until the [first derivative](derivative.md) $f'$ is reached to prove [extrema](maximum%20and%20minimum.md) and the [second derivative](second%20derivative.md) $f''$ is reached to prove convexities.}} <!--SR:!2024-04-21,104,299-->

<!-- markdownlint MD028 -->

> [!example] examples
>
> - $f(x):=-x^{2n}\text{ for }n\in\mathbb{N}^+,c=0$: {{[Strict local maximum](maximum%20and%20minimum.md) and weakly (strictly when $n = 1$) [concave](convex%20function.md).}}
> - $f(x):=x^{2n}\text{ for }n\in\mathbb{N}^+,c=0$: {{[Strict local minimum](maximum%20and%20minimum.md) and weakly (strictly when $n = 1$) [convex](convex%20function.md).}}
> - $f(x):=x^\frac{2n}3,n\in\mathbb{N}^+,c=0$: {{Inconclusive because no $d\in\mathbb{N}^+$ such that $f^{(d)}(0)$ exists and $f^{(d)}(0)\ne0$. Actual is [strict local minimum](maximum%20and%20minimum.md).}}
> - $f(x):=x\lvert{x}\rvert,c=0$: {{Inconclusive by the two-sided test and [stationary rising inflection point](maximum%20and%20minimum.md) and not local [extremum](maximum%20and%20minimumm.md) by the one-sided test.}}
> - $f(x):=x^{2n+1}\text{ for }n\in\mathbb{N}^+,c=0$: {{[Stationary rising inflection point](inflection%20point.md) and not local [extremum](maximum%20and%20minimumm.md).}}
> - $f(x):=\begin{cases}e^{-\frac1{x^2} }&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$: {{Inconclusive because $\forall{n\in\mathbb{N}^+}\,f^{(n)}(0)=0$. Actual is [strict local minimum](maximum%20and%20minimum.md).}}
> - $f(x):=x^\frac{2n+1}2,n\in\mathbb{N}_0,c=0$: {{Inconclusive because no $d\in\mathbb{N}^+$ such that $f^{(d)}(0)$ exists and $f^{(d)}(0)\ne0$. Actual is [right-sided strict local minimum](maximum%20and%20minimum.md).}}
> - $f(x):=-x^{2n+1}\text{ for }n\in\mathbb{N}^+,c=0$: {{[stationary falling inflection point](inflection%20point.md) and not [local extremum](maximum%20and%20minimum.md).}}
> - $f(x):=x^\frac13,c=0$: {{Inconclusive because $f^{(n)}(0)$ for all $n\in\mathbb{N}^+$ does not exist $(f^{(n)}(0)=\pm\infty)$. Actual is [vertically rising inflection point](inflection%20point.md).}}
> - $f(x):=x^\frac{2n+3}3,n\in\mathbb{N}^+,c=0$: {{Inconclusive because no $d\in\mathbb{N}^+$ such that $f^{(d)}(0)$ exists and $f^{(d)}(0)\ne0$. Actual is [stationary rising inflection point](inflection%20point.md).}}
> - $f(x):=\frac16\lvert{x}\rvert{}x^2,c=0$: {{Inconclusive by the two-sided test and [strict local minimum](maximum%20and%20minimum.md) by the one-sided test.}}
> - $f(x):=\begin{cases}x^2\sin{\frac1x}&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$: {{Inconclusive because the two-sided [second derivative](second%20derivative.md) $f''(0)$ and one-sided [second derivatives](second%20derivative.md) $f''_\pm(0)$ do not exist. Actual is neither [local extremum](maximum%20and%20minimum.md) nor [inflection point](inflection%20point.md).}} <!--SR:!2024-06-14,137,294!2024-06-07,130,290!2024-02-18,56,274!2024-03-19,72,279!2024-03-31,80,272!2024-02-15,62,319!2024-04-30,102,279!2024-06-20,140,299!2024-06-17,139,292!2024-03-28,77,279!2024-03-13,43,274!2024-06-19,139,299-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/derivative_test) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
