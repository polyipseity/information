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
---

# derivative test

## single variable

### first derivative test

The _first derivative test_ can {{determine [extrema](maximum%20and%20minimum.md) and whether a [function](function%20(mathematics).md) is increasing or decreasing at a point}}. <!--SR:!2023-12-17,16,299-->

> __first derivative test__
>
> 1. {{Let $f:I\to\mathbb{R}$ be a [real-valued function](real-valued%20function.md). $I$ is an [interval](interval%20(mathematics).md) containing $c$. $f$ is [right/left-continuous](continuous%20function.md) at $c$, i.e. $\lim_{x\to{}c^\pm}f(x)=f(c)$, and [differentiable](differentiable%20function.md) on the immediate right/left of $c$, i.e. for some $\delta>0$, $f'(c\pm\epsilon)$ exists for all $\epsilon\in(0,\delta)$. (Choose either right (`+`) or left (`-`).)}}
> 2. {{If there exists $\epsilon>0$ such that:<ul><li>(left (`-`)) $f'(x)<0$ ($f'(x)\le0$) for all $x\in(c-\epsilon,c)$, then $f$ has a [strict (respectively, weak) local minimum](maximum%20and%20minimum.md) at $c$ from the left.</li><li>(left (`-`)) $f'(x)>0$ ($f'(x)\ge0$) for all $x\in(c-\epsilon,c)$, then $f$ has a [strict (respectively, weak) local maximum](maximum%20and%20minimum.md) at $c$ from the left.</li><li>(right (`+`)) $f'(x)<0$ ($f'(x)\le0$) for all $x\in(c,c+\epsilon)$, then $f$ has a [strict (respectively, weak) local maximum](maximum%20and%20minimum.md) at $c$ from the right.</li><li>(right (`+`)) $f'(x)>0$ ($f'(x)\ge0$) for all $x\in(c,c+\epsilon)$, then $f$ has a [strict (respectively, weak) local minimum](maximum%20and%20minimum.md) at $c$ from the right.</li></ul>}}
> 3. {{Combine the above conclusions from both sides.}} <!--SR:!2023-12-28,19,259!2023-12-11,10,279!2023-12-16,15,299-->

The _one-sided first derivative test_ is {{a variant of the first derivative test that covers a different set of functions. Neither of the two tests are stronger than the other}}. <!--SR:!2023-12-18,17,299-->

> __one-sided first derivative test__
>
> 1. {{Let $f:I\to\mathbb{R}$ be a [real-valued function](real-valued%20function.md). $I$ is an [interval](interval%20(mathematics).md) containing $c$. $f$ is [right/left-differentiable](differentiable%20function.md) at $c$, i.e. $f'_\pm(c)$ exists. (Choose either right (`+`) or left (`-`).)}}
> 2. {{then:<ul><li>If $f'_-(c)<0$, then $f$ has a [strict local minimum](maximum%20and%20minimum.md) at $c$ from the left.</li><li>If $f'_-(c)>0$, then $f$ has a [strict local maximum](maximum%20and%20minimum.md) at $c$ from the left.</li><li>If $f'_+(c)<0$, then $f$ has a [strict local maximum](maximum%20and%20minimum.md) at $c$ from the right.</li><li>If $f'_+(c)>0$, then $f$ has a [strict local minimum](maximum%20and%20minimum.md) at $c$ from the right.</li><li>Otherwise, the test is inconclusive.</li></ul>}} <!--SR:!2023-12-10,6,239!2023-12-12,11,279-->

#### examples

- $f(x):=\begin{cases}e^{-\frac1{x^2} }&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$: {{[Strict local minimum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
- $f(x):=-x^{2n+1}\text{ for }n\in\mathbb{N}^+,c=0$: {{Weakly decreasing by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
- $f(x):=x^{2n+1}\text{ for }n\in\mathbb{N}^+,c=0$: {{Weakly increasing by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
- $f(x):=x^\frac{2n+1}2,n\in\mathbb{N}_0,c=0$: {{[Right-sided strict local minimum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
- $f(x):=-x^{2n}\text{ for }n\in\mathbb{N}^+,c=0$: {{[Strict local maximum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
- $f(x):=\begin{cases}\lvert{x}\rvert\left(2+\sin{\frac1x}\right)&\text{if }\ne0\\0&\text{if }x=0\end{cases},c=0$: {{Inconclusive by the two-sided test because no suitable $\epsilon$ exist and inconclusive by the one-sided test because the one-sided [derivaties](derivative.md) do not exist. Actual is [strict local minimum](maximum%20and%20minimum.md).}}
- $f(x):=x^{2n}\text{ for }n\in\mathbb{N}^+,c=0$: {{[Strict local minimum](maximum%20and%20minimum.md) by the two-sided and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
- $f(x):=\lvert{x}\rvert,c=0$: {{[Strict local minimum](maximum%20and%20minimum.md) by the two-sided or one-sided test.}}
- $f(x):=x^\frac13,c=0$: {{Strictly increasing by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) do not exist.}}
- $f(x):=\begin{cases}x^2\sin{\frac1x}&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$: {{Inconclusive by the two-sided test because no suitable $\epsilon$ exist and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are both 0. Actual is neither [local extremum](maximum%20and%20minimum.md) nor [inflection point](inflection%20point.md).}}
- $f(x):=x^\frac{2n+3}3,n\in\mathbb{N}^+,c=0$: {{Weakly increasing by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}}
- $f(x):=\begin{cases}\lvert{x}\rvert\left(2+x\sin{\frac1x}\right)&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$: {{Inconclusive by the two-sided test because no suitable $\epsilon$ exist and [strict local minimum](maximum%20and%20minimum.md) by the one-sided test.}}
- $f(x):=x^\frac{2n}3,n\in\mathbb{N}^+,c=0$: {{[Strict local minimum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0 or do not exist.}}
- $f(x):=\frac16\lvert{x}\rvert{}x^2,c=0$: {{[Strict local minimum](maximum%20and%20minimum.md) by the two-sided test and inconclusive by the one-sided test because the one-sided [derivatives](derivative.md) are 0.}} <!--SR:!2023-12-11,10,279!2023-12-14,13,279!2023-12-15,14,292!2023-12-25,17,259!2023-12-17,16,299!2023-12-14,13,279!2023-12-15,14,294!2023-12-16,15,299!2023-12-10,9,274!2023-12-19,18,299!2023-12-15,14,299!2023-12-11,10,274!2023-12-16,15,294!2023-12-15,14,299-->

### concavity test

The [second derivative](second%20derivative.md) of a [function](function%20(mathematics).md) can {{determine whether the [function](function%20(mathematics).md) is [concave up](convex%20function.md) or [concave down](concave%20function.md)}}. A [twice-differentiable function](differentiable%20function.md) is {{[weakly concave up](convex%20function.md) if $f''(x)\ge0$, [strictly concave up](convex%20function.md) if $f''(x)>0$, [weakly concave down](concave%20function.md) if $f''(x)\le0$, and [strictly concave down](concave%20function.md) if $f''(x)<0$}}. <!--SR:!2023-12-15,14,294!2023-12-16,15,299-->

### second derivative test

The _second derivative test_ is {{a special case of $n=2$ in the [higher-order derivative test](#higher-order%20derivative%20test)}}. The same applies for the _one-sided second derivative test_. <!--SR:!2023-12-17,16,299-->

### higher-order derivative test

The _higher-order derivative test_ or _general derivative test_ can {{determine [extrema](maximum%20and%20minimum.md), and [inflection points](inflection%20point.md) for sufficiently [differentiable functions](differentiable%20function.md)}}. <!--SR:!2023-12-16,15,299-->

> __higher-order derivative test__
>
> 1. {{Let $f:I\to\mathbb{R}$ be a [real-valued](real-valued%20function.md) [$n$-times differentiable function](differentiable%20function.md) where $n\in\mathbb{N}^+\setminus\set{1}$. $I$ is an [interval](interval%20(mathematics).md) $\in\mathbb{R}$ containing $c$.}}
> 2. {{If $f'(c)=\cdots=f^{(n-1)}(c)=0$ and $f^{(n)}(c)\ne0$,}}
> 3. {{then:<ul><li>If $n$ is even and $f^{(n)}(c)<0$, $c$ is a [strict local maximum](maximum%20and%20minimum.md) of $f$.</li><li>If $n$ is even and $f^{(n)}(c)>0$, $c$ is a [strict local minimum](maximum%20and%20minimum.md) of $f$.</li><li>If $n$ is odd and $f^{(n)}(c)<0$, $c$ is a [weakly decreasing falling inflection point](inflection%20point.md) and not a [local extremum](maximum%20and%20minimum.md) of $f$.</li><li>If $n$ is odd and $f^{(n)}(c)>0$, $c$ is a [weakly increasing rising inflection point](inflection%20point.md) and not a [local extremum](maximum%20and%20minimum.md) of $f$.</li></ul>}} <!--SR:!2023-12-17,16,299!2023-12-18,17,299!2023-12-16,15,299-->

The _one-sided higher-order derivative test_ is {{stronger than the two-sided higher-order derivative test, as the two-sided version can be derived from the one-sided one by combining conclusions}}. <!--SR:!2023-12-18,17,299-->

> __one-sided higher-order derivative test__
>
> 1. {{Let $f:I\to\mathbb{R}$ be a [real-valued function](real-valued%20function.md). $I$ is an [interval](interval%20(mathematics).md) containing $c$. $f$ is [right/left-continuous](continuous%20function.md) at $c$, i.e. $\lim_{x\to{}c^\pm}f(x)=f(c)$. $f$ is [$n-1$-times differentiable](differentiable%20function.md) on the immediate right/left of $c$ where $n\in\mathbb{N}^+\setminus\set{1}$, i.e. for some $\delta>0$, $f^{(n-1)}(c\pm\epsilon)$ exists for all $\epsilon\in(0,\delta)$. $f$ is also $n$-times right/left-differentiable at $c$, i.e. $f^{(n)}_\pm(c)$ exists. (Choose either right (`+`) or left (`-`).)}}
> 2. {{If $f'_\pm(c)=\cdots=f^{(n-1)}_\pm(c)=0$ and $f^{(n)}_\pm(c)\ne0$, (Choose either right (`+`) or left (`-`).)}}
> 3. {{then:<ul><li>If $n$ is even and $f^{(n)}_-(c)<0$, $c$ is a [strict local maximum](maximum%20and%20minimum.md) of $f$ from the left. $f$ is [weakly concave](concave%20function.md) to the immediate left of $c$.</li><li>If $n$ is even and $f^{(n)}_-(c)>0$, $c$ is a [strict local minimum](maximum%20and%20minimum.md) of $f$ from the left. $f$ is [weakly convex](convex%20function.md) to the immediate left of $c$.</li><li>If $n$ is odd and $f^{(n)}_-(c)<0$, $c$ is a [strict local minimum](maximum%20and%20minimum.md) of $f$ from the left. $f$ is [weakly convex](convex%20function.md) to the immediate left of $c$.</li><li>If $n$ is odd and $f^{(n)}_-(c)>0$, $c$ is a [strict local maximum](maximum%20and%20minimum.md) of $f$ from the left. $f$ is [weakly concave](concave%20function.md) to the immediate left of $c$.</li><li>If $f^{(n)}_+(c)<0$, $c$ is a [strict local maximum](maximum%20and%20minimum.md) of $f$ from the right. $f$ is [weakly concave](concave%20function.md) to the immediate right of $c$.</li><li>If $f^{(n)}_+(c)>0$, $c$ is a [strict local minimum](maximum%20and%20minimum.md) of $f$ from the right. $f$ is [weakly convex](convex%20function.md) to the immediate right of $c$.</li></ul>}} <!--SR:!2023-12-29,20,259!2023-12-18,17,299!2023-12-23,16,259-->

> [!tip]
>
> - [intuition](intuition.md): {{Notice that for a [continuous](continuous%20function.md) $n$-th derivative that is 0 at $c$, i.e. $f^{(n)}(c)=0$, the [sign](sign%20(mathematics).md) of the two-sided or one-sided $n+1$-th derivative at $c$ $f^{(n+1)}_\pm(c)$ determines whether $f^{(n)}$ is larger or smaller than 0 to the immediate left or right of $c$. Repeat this until the [first derivative](derivative.md) $f'$ is reached to prove [extrema](maximum%20and%20minimum.md) and the [second derivative](second%20derivative.md) $f''$ is reached to prove convexities.}} <!--SR:!2023-12-11,10,279-->

#### examples

- $f(x):=-x^{2n}\text{ for }n\in\mathbb{N}^+,c=0$: {{[Strict local maximum](maximum%20and%20minimum.md).}}
- $f(x):=x^{2n}\text{ for }n\in\mathbb{N}^+,c=0$: {{[Strict local minimum](maximum%20and%20minimum.md).}}
- $f(x):=x^\frac{2n}3,n\in\mathbb{N}^+,c=0$: {{Inconclusive because no $d\in\mathbb{N}^+$ such that $f^{(d)}(0)$ exists and $f^{(d)}(0)\ne0$. Actual is [strict local minimum](maximum%20and%20minimum.md).}}
- $f(x):=x\lvert{x}\rvert,c=0$: {{Inconclusive by the two-sided test and [weakly increasing rising inflection point](maximum%20and%20minimum.md) by the one-sided test.}}
- $f(x):=x^{2n+1}\text{ for }n\in\mathbb{N}^+,c=0$: {{[Weakly increasing rising inflection point](inflection%20point.md) and not [local extremum](maximum%20and%20minimum.md).}}
- $f(x):=\begin{cases}e^{-\frac1{x^2} }&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$: {{Inconclusive because $\forall{n\in\mathbb{N}^+}\,f^{(n)}(0)=0$. Actual is [strict local minimum](maximum%20and%20minimum.md).}}
- $f(x):=x^\frac{2n+1}2,n\in\mathbb{N}_0,c=0$: {{Inconclusive because no $d\in\mathbb{N}^+$ such that $f^{(d)}(0)$ exists and $f^{(d)}(0)\ne0$. Actual is [right-sided strict local minimum](maximum%20and%20minimum.md).}}
- $f(x):=-x^{2n+1}\text{ for }n\in\mathbb{N}^+,c=0$: {{[Weakly decreasing falling inflection point](inflection%20point.md) and not [local extremum](maximum%20and%20minimum.md).}}
- $f(x):=x^\frac13,c=0$: {{Inconclusive because $f^{(n)}(0)$ for all $n\in\mathbb{N}^+$ does not exist $(f^{(n)}(0)=\pm\infty)$. Actual is [vertically increasing inflection point](inflection%20point.md).}}
- $f(x):=x^\frac{2n+3}3,n\in\mathbb{N}^+,c=0$: {{Inconclusive because no $d\in\mathbb{N}^+$ such that $f^{(d)}(0)$ exists and $f^{(d)}(0)\ne0$. Actual is [stationary rising inflection point](inflection%20point.md).}}
- $f(x):=\frac16\lvert{x}\rvert{}x^2,c=0$: {{Inconclusive by the two-sided test and [strict local minimum](maximum%20and%20minimum.md) by the one-sided test.}}
- $f(x):=\begin{cases}x^2\sin{\frac1x}&\text{if }x\ne0\\0&\text{if }x=0\end{cases},c=0$: {{Inconclusive because the two-sided [second derivative](second%20derivative.md) $f''(0)$ and one-sided [second derivatives](second%20derivative.md) $f''_\pm(0)$ do not exist. Actual is neither [local extremum](maximum%20and%20minimum.md) nor [inflection point](inflection%20point.md).}} <!--SR:!2023-12-13,12,274!2023-12-15,14,290!2023-12-24,16,254!2023-12-10,9,279!2023-12-11,10,272!2023-12-15,14,299!2023-12-13,12,279!2023-12-16,15,299!2023-12-13,12,272!2023-12-11,10,279!2023-12-10,9,274!2023-12-16,15,299-->
