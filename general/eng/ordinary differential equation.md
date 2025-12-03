---
aliases:
  - ODE
  - ordinary differential equation
tags:
  - flashcard/active/general/eng/ordinary_differential_equation
  - language/in/English
---

# ordinary differential equation

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## definitions

{@{An _[explicit](implicit%20function.md) ordinary differential equation of order n_}@} has the form: {@{$$F\left(x,y(x),y'(x),\ldots,y^{(n-1)}(x)\right)=y^{(n)}(x) \,,$$}@} where $x$ is {@{an [independent variable](dependent%20and%20independent%29variables.md)}@}, $y(x)$ is {@{a [function](function%20(mathematics).md) of $x$}@}, $y^{(d)}(x)$ are {@{$d$-th [derivatives](derivative%20.md) of $y(x)$}@}, and $F$ is {@{a [formula](formula.md)}@}.

{@{An _[implicit](implicit%20function.md) ordinary differential equation of order n_}@} has the form: {@{$$F\left(x,y(x),y'(x),\ldots,y^{(n-1)}(x), y^{(n)}(x)\right)=0$$}@}, using the same notations as above.

### classifications

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects('0d9f', 'ff12'),
  (
    '[autonomous](#^autonomous)',
    '[homogeneous](#^homogeneous)',
    '[linear](#^linear)',
    '[nonhomogeneous](#^nonhomogeneous)/inhomogeneous',
    '[nonlinear](#^nonlinear)',
  ),
)
```

Ordinary differential equations are furthered classified:

<!--pytextgen generate section="0d9f"--><!-- The following content is generated at 2023-09-26T08:47:40.039221+08:00. Any edits will be overridden! -->

> 1. [autonomous](#^autonomous)
> 2. [homogeneous](#^homogeneous)
> 3. [linear](#^linear)
> 4. [nonhomogeneous](#^nonhomogeneous)/inhomogeneous
> 5. [nonlinear](#^nonlinear)

<!--/pytextgen-->

<!--pytextgen generate section="ff12"--><!-- The following content is generated at 2024-01-04T20:17:52.323867+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[autonomous](#^autonomous)
- [autonomous](#^autonomous)→::@::←[homogeneous](#^homogeneous)
- [homogeneous](#^homogeneous)→::@::←[linear](#^linear)
- [linear](#^linear)→::@::←[nonhomogeneous](#^nonhomogeneous)/inhomogeneous
- [nonhomogeneous](#^nonhomogeneous)/inhomogeneous→::@::←[nonlinear](#^nonlinear)
- [nonlinear](#^nonlinear)→::@::←_(end)_

<!--/pytextgen-->

> [__autonomous__](autonomous%20system%20(mathematics).md) <a id="^autonomous"></a>^autonomous
>
> {@{An ODE}@} where $F$ {@{does not depend on the [independent variable](dependent%20and%20independent%29variables.md) $x$ explicitly}@}.

<!-- markdownlint MD028 -->

> [__homogeneous__](homogeneous%20differential%20equation.md) <a id="^homogeneous"></a>^homogeneous
>
> {@{An [linear](#^linear) ODE}@} where {@{there are no constant terms ($r(x)=0$)}@}.

<!-- markdownlint MD028 -->

> [__linear__](linear%20differential%20equation.md) <a id="^linear"></a>^linear
>
> {@{An ODE where $F$}@} can be written as {@{a [linear combination](linear%20combination.md) of the derivatives of $y$}@} with {@{the [coefficients](coefficient.md) being [constants](constant%20(mathematics).md) or [continuous functions](continuous%20function.md) of $x$}@}. {@{The constant term $r(x)$}@} is also called {@{the _source term_}@}.

<!-- markdownlint MD028 -->

> [__nonhomogeneous__](homogeneous%20differential%20equation.md) <a id="^nonhomogeneous"></a>^nonhomogeneous
>
> {@{An [linear](#^linear) ODE}@} that is {@{not [homogeneous](#^homogeneous)}@}.

<!-- markdownlint MD028 -->

> [__nonlinear__](nonlinear%20system.md#nonlinear%20differential%20equations) <a id="^nonlinear"></a>^nonlinear
>
> {@{An ODE}@} that is {@{not [linear](#^linear)}@}.

### exact solutions

#### separable equations

##### first-order, separable in _x_ and _y_

- form :@: $F_1(x) G_1(y) \,\mathrm{d}x + F_2(x) G_2(y) \,\mathrm{d}y = 0$, where $F_1, F_2, G_1, G_2$ are [integrable](integral.md) [functions](function%20(mathematics).md).
- solution :@: Divide by $F_2(x) G_1(y)$ to [separate the variables](separation%20of%20variables.md), then integrate.

The general solution is:

$$\begin{aligned}
F_1(x)G_1(y)\,\mathrm{d}x+F_2(x)G_2(y)\,\mathrm{d}y&=0\\
\frac{F_1(x)}{F_2(x)}\,\mathrm{d}x+\frac{G_2(y)}{G_1(y)}\,\mathrm{d}y&=0\\
\int\!\frac{F_1(x)}{F_2(x)}\,\mathrm{d}x+\int\!\frac{G_2(y)}{G_1(y)}\,\mathrm{d}y&=C
\end{aligned}$$

> [!example] example
>
> $$\begin{aligned}
> xe^y\frac{\mathrm{d}y}{\mathrm{d}x}&=y\sin{x}\\
> xe^y\frac{\mathrm{d}y}{\mathrm{d}x}-y\sin{x}&=0\\
> xe^y\,\mathrm{d}y-y\sin{x}\,\mathrm{d}x&=0\\
> \frac{e^y}y\,\mathrm{d}y-\frac{\sin{x} }x\,\mathrm{d}x&=0\\
> \int\!\frac{e^y}y\,\mathrm{d}y-\int\!\frac{\sin{x} }x\,\mathrm{d}x&=C\\
> \operatorname{Ei}(y)-\operatorname{Si}(x)&=C\\
> \operatorname{Ei}(y)&=\operatorname{Si}(x)+C\\
> y&=\operatorname{Ei}^{-1}(\operatorname{Si}(x)+C)
> \end{aligned}$$

#### general first-order equations

##### first-order, homogeneous

- form :@: $\frac{\mathrm{d}y}{\mathrm{d}x}=F\left(\frac{y}x\right)$, where $F$ is an [integrable](integraable.md) [function](function%20(mathematics).md).
- solution :@: Substitute $y\overset{\mathrm{def} }=ux$, then [separate the variables](separation%20of%20variables.md), then integrate.

The general solution is:

$$\begin{aligned}
\frac{\mathrm{d}y}{\mathrm{d}x}&=F\left(\frac{y}x\right)\\
\frac{\mathrm{d}u}{\mathrm{d}x}x+u&=F(u) && (y\overset{\mathrm{def} }=ux)\\
\frac{\mathrm{d}u}{\mathrm{d}x}x&=F(u)-u\\
\frac{\mathrm{d}u}{F(u)-u}&=\frac{\mathrm{d}x}x\\
\frac{\mathrm{d}u}{F(u)-u}-\frac{\mathrm{d}x}x&=0\\
\int\!\frac{\mathrm{d}u}{F(u)-u}-\int\!\frac{\mathrm{d}x}x&=C\\
\int\!\frac{\mathrm{d}u}{F(u)-u}-\ln{x}&=C\\
\ln{x}+C&=\int\!\frac{\mathrm{d}u}{F(u)-u}
\end{aligned}$$

> [!example] example
>
> $$\begin{aligned}
> \frac{\mathrm{d}y}{\mathrm{d}x}&=\frac{y^2\left(e^{\frac{x}y}-1+\frac{x}y\right)}{x^2}\\
> \frac{\mathrm{d}u}{\mathrm{d}x}x+u&=u^2e^\frac1u-u^2+u && (y\overset{\mathrm{def} }=ux)\\
> \frac{\mathrm{d}u}{\mathrm{d}x}x&=u^2e^\frac1u-u^2\\
> \frac{\mathrm{d}u}{u^2e^\frac1u-u^2}&=\frac{\mathrm{d}x}x\\
> \frac{\mathrm{d}u}{u^2e^\frac1u-u^2}-\frac{\mathrm{d}x}x&=0\\
> \int\!\frac{\mathrm{d}u}{u^2e^\frac1u-u^2}-\int\!\frac{\mathrm{d}x}x&=C\\
> \int\!\frac{\mathrm{d}u}{u^2\left(e^\frac1u-1\right)}-\ln{x}&=C\\
> -\int\!\frac{\mathrm{d}v}{e^v-1}-\ln{x}&=C && \left(v\overset{\mathrm{def} }=\frac1u\right)\\
> -\int\!\frac{\mathrm{d}w}{w^2-w}-\ln{x}&=C && \left(w\overset{\mathrm{def} }=e^v\right)\\
> \int\!\frac{\mathrm{d}\!\left(\frac1w\right)}{1-\frac1w}-\ln{x}&=C\\
> -\ln\left(\frac1w-1\right)-\ln{x}&=C\\
> x\left(\frac1w-1\right)&=C\\
> \frac1w&=1+\frac{C}x\\
> e^\frac{x}y&=\frac1{\frac{C}x+1}\\
> \frac{x}y&=-\ln\left(\frac{C}x+1\right)\\
> y&=-\frac{x}{\ln\left(\frac{C}x+1\right)}
> \end{aligned}$$

#### general second-order equation

##### second-order, autonomous

- form :@: $\frac{\mathrm{d}^2y}{\mathrm{d}x^2}=F(y)$, where $F$ is an [integrable](integral.md) [function](function%20(mathematics).md).
- solution :@: Multiply by $2\frac{\mathrm{d}y}{\mathrm{d}x}$, then substitute $2\frac{\mathrm{d}y}{\mathrm{d}x}\frac{\mathrm{d}^2y}{\mathrm{d}x^2}=\frac{\mathrm{d} }{\mathrm{d}x}\!\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2$, then integrate twice.

The general solution is:

$$\begin{aligned}
\frac{\mathrm{d}^2y}{\mathrm{d}x^2}&=F(y)\\
2\frac{\mathrm{d}y}{\mathrm{d}x}\frac{\mathrm{d}^2y}{\mathrm{d}x^2}&=2\frac{\mathrm{d}y}{\mathrm{d}x}F(y)\\
\frac{\mathrm{d} }{\mathrm{d}x}\!\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2&=2\frac{\mathrm{d}y}{\mathrm{d}x}F(y)\\
\mathrm{d}\!\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2&=2F(y)\,\mathrm{d}y\\
\int\!\mathrm{d}\!\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2&=\int\!2F(y)\,\mathrm{d}y\\
\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2&=2\int\!F(y)\,\mathrm{d}y+C_1\\
\frac{\mathrm{d}y}{\mathrm{d}x}&=\pm\sqrt{2\int\!F(y)\,\mathrm{d}y+C_1}\\
\int\!\mathrm{d}x&=\int\!\frac{\mathrm{d}y}{\pm\sqrt{2\int\!F(y)\,\mathrm{d}y+C_1} }\\
x&=\pm\int\!\frac{\mathrm{d}y}{\sqrt{2\int\!F(y)\,\mathrm{d}y+C_1} }+C_2
\end{aligned}$$

> [!example] example
>
> $$\begin{aligned}
> \frac{\mathrm{d}^2x}{\mathrm{d}t^2}&=-\frac{k}mx\\
> 2\frac{\mathrm{d}x}{\mathrm{d}t}\frac{\mathrm{d}^2x}{\mathrm{d}t^2}&=-2\frac{\mathrm{d}x}{\mathrm{d}t}\frac{k}mx\\
> \frac{\mathrm{d} }{\mathrm{d}t}\!\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2&=-2\frac{\mathrm{d}x}{\mathrm{d}t}\frac{k}mx\\
> \int\!\mathrm{d}\!\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2&=-\frac{2k}m\int\!x\,\mathrm{d}x\\
> \left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2&=-\frac{kx^2}m+C_1\\
> \frac{\mathrm{d}x}{\mathrm{d}t}&=\pm\sqrt{-\frac{kx^2}m+C_1}\\
> \int\!\mathrm{d}t&=\pm\int\!\frac{\mathrm{d}x}{\sqrt{-\frac{kx^2}m+C_1} }\\
> t&=\pm\sqrt{\frac{mC_1}k}\int\!\frac{\cos\theta\,\mathrm{d}\theta}{\sqrt{-C_1\sin^2\theta+C_1} } && \left(x\overset{\mathrm{def} }=\sqrt{\frac{mC_1}k}\sin\theta,\theta\in\left[-\frac\pi2,\frac\pi2\right]\right)\\
> &=\pm\sqrt{\frac{m}k}\int\!\mathrm{d}\theta\\
> &=\pm\sqrt{\frac{m}k}\theta+C_2\\
> &=\pm\sqrt{\frac{m}k}\arcsin\frac{x}{\sqrt{\frac{mC_1}k} }+C_2\\
> &=\pm\sqrt{\frac{m}k}\arcsin{}C_1x+C_2\\
> \arcsin{}C_1x&=\pm\frac{t-C_2}{\sqrt{\frac{m}k} }\\
> &=\pm\sqrt{\frac{k}m}t+C_2\\
> C_1x&=\pm\sin\left(\sqrt{\frac{k}m}t+C_2\right)\\
> &=C_1\sin\left(\sqrt{\frac{k}m}t+C_2\right)\\
> &=C_1\left(C_{2\in[-1,1]}\sin\sqrt{\frac{k}m}t+C_{3\in[-1,1]}\cos\sqrt{\frac{k}m}t\right)\\
> &=C_1\sin\sqrt{\frac{k}m}t+C_2\cos\sqrt{\frac{k}m}t
> \end{aligned}$$

## references

This text incorporates [content](https://en.wikipedia.org/wiki/ordinary_differential_equation) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
