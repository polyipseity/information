---
aliases:
  - ODE
  - ordinary differential equation
tags:
  - flashcards/general/ordinary_differential_equation
  - languages/in/English
---

# ordinary differential equation

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```

%%

## definitions

An [explicit](implicit%20function.md) ordinary differential equation of order _n_ has the form:

> {{__explicit ordinary differential equation of order _n___}}
>
> {{$F\left(x,y(x),y'(x),\ldots,y^{(n-1)}(x)\right)=y^{(n)}(x)$}}
>
> given
>
> - $x$, an [independent variable](dependent%20and%20independent%29variables.md)
> - $y(x)$, a [function](function%20(mathematics).md) of $x$
> - $y^{(d)}(x)$, [derivatives](derivative%20.md) of $y(x)$
> - $F$, a [formula](formula.md) <!--SR:!2024-07-25,207,310!2024-12-02,330,344-->

An [implicit](implicit%20function.md) ordinary differential equation of order _n_ has the form:

> {{__implicit ordinary differential equation of order _n___}}
>
> {{$F\left(x,y(x),y'(x),\ldots,y^{(n-1)}(x), y^{(n)}(x)\right)=0$}}
>
> given
>
> - $x$, an [independent variable](dependent%20and%20independent%29variables.md)
> - $y(x)$, a [function](function%20(mathematics).md) of $x$
> - $y^{(d)}(x)$, [derivatives](derivative%20.md) of $y(x)$
> - $F$, a [formula](formula.md) <!--SR:!2024-06-22,181,310!2024-12-07,334,344-->

### classifications

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_seq(
  e.cwf_sects('0d9f', 'ff12'),
  (
    '[autonomous](#^autonomous)',
    '[homogeneous](#^homogeneous)',
    '[linear](#^linear)',
    '[nonhomogeneous](#^nonhomogeneous)/inhomogeneous',
    '[nonlinear](#^nonlinear)',
  ),
)
```

%%

Ordinary differential equations are furthered classified:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="0d9f"--><!-- The following content is generated at 2023-09-26T08:47:40.039221+08:00. Any edits will be overridden! -->

> 1. [autonomous](#^autonomous)
> 2. [homogeneous](#^homogeneous)
> 3. [linear](#^linear)
> 4. [nonhomogeneous](#^nonhomogeneous)/inhomogeneous
> 5. [nonlinear](#^nonlinear)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ff12"--><!-- The following content is generated at 2024-01-04T20:17:52.323867+08:00. Any edits will be overridden! -->

- _(begin)_→:::←[autonomous](#^autonomous) <!--SR:!2024-05-30,173,310!2024-09-20,268,330-->
- [autonomous](#^autonomous)→:::←[homogeneous](#^homogeneous) <!--SR:!2024-05-25,170,310!2024-10-21,293,330-->
- [homogeneous](#^homogeneous)→:::←[linear](#^linear) <!--SR:!2024-09-21,269,330!2024-05-13,160,310-->
- [linear](#^linear)→:::←[nonhomogeneous](#^nonhomogeneous)/inhomogeneous <!--SR:!2024-07-17,225,330!2024-07-30,210,310-->
- [nonhomogeneous](#^nonhomogeneous)/inhomogeneous→:::←[nonlinear](#^nonlinear) <!--SR:!2024-09-16,265,330!2024-09-04,255,330-->
- [nonlinear](#^nonlinear)→:::←_(end)_ <!--SR:!2024-05-26,170,310!2024-05-17,163,310-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

> [__autonomous__](autonomous%20system%20(mathematics).md) <a id="^autonomous"></a>^autonomous
>
> {{An ODE where $F$ does not depend on the [independent variable](dependent%20and%20independent%29variables.md) $x$ explicitly.}} <!--SR:!2024-06-10,173,310-->

<!-- markdownlint MD028 -->

> [__homogeneous__](homogeneous%20differential%20equation.md) <a id="^homogeneous"></a>^homogeneous
>
> {{An [linear](#^linear) ODE where there are no constant terms ($r(x)=0$).}} <!--SR:!2024-07-14,211,310-->

<!-- markdownlint MD028 -->

> [__linear__](linear%20differential%20equation.md) <a id="^linear"></a>^linear
>
> {{An ODE where $F$ can be written as a [linear combination](linear%20combination.md) of the derivatives of $y$ with the [coefficients](coefficient.md) being [constants](constant%20(mathematics).md) or [continuous functions](continuous%20function.md) of $x$. The constant term $r(x)$ is also called the _source term_.}} <!--SR:!2024-04-06,127,290-->

<!-- markdownlint MD028 -->

> [__nonhomogeneous__](homogeneous%20differential%20equation.md) <a id="^nonhomogeneous"></a>^nonhomogeneous
>
> {{An [linear](#^linear) ODE that is not [homogeneous](#^homogeneous).}} <!--SR:!2024-08-26,248,330-->

<!-- markdownlint MD028 -->

> [__nonlinear__](nonlinear%20system.md#nonlinear%20differential%20equations) <a id="^nonlinear"></a>^nonlinear
>
> {{An ODE that is not [linear](#^linear).}} <!--SR:!2024-07-24,231,330-->

### exact solutions

#### first-order equations

> {{__first-order, separable in $x$ and $y$__}}
>
> - form: {{$F_1(x)G_1(y)\,\mathrm{d}x+F_2(x)G_2(y)\,\mathrm{d}y=0$, where $F_1, F_2, G_1, G_2$ are [integrable](integrability.md) [functions](function%20(mathematics).md)}}
> - solution: {{divide by $F_2(x)G_1(y)$ to [separate the variables](separation%20of%20variables.md), then integrate}}
> - steps: $\begin{aligned}
F_1(x)G_1(y)\,\mathrm{d}x+F_2(x)G_2(y)\,\mathrm{d}y&=0\\
\frac{F_1(x)}{F_2(x)}\,\mathrm{d}x+\frac{G_2(y)}{G_1(y)}\,\mathrm{d}y&=0\\
\int\!\frac{F_1(x)}{F_2(x)}\,\mathrm{d}x+\int\!\frac{G_2(y)}{G_1(y)}\,\mathrm{d}y&=C
\end{aligned}$
> - example: $\begin{aligned}
xe^y\frac{\mathrm{d}y}{\mathrm{d}x}&=y\sin{x}\\
xe^y\frac{\mathrm{d}y}{\mathrm{d}x}-y\sin{x}&=0\\
xe^y\,\mathrm{d}y-y\sin{x}\,\mathrm{d}x&=0\\
\frac{e^y}y\,\mathrm{d}y-\frac{\sin{x} }x\,\mathrm{d}x&=0\\
\int\!\frac{e^y}y\,\mathrm{d}y-\int\!\frac{\sin{x} }x\,\mathrm{d}x&=C\\
\operatorname{Ei}(y)-\operatorname{Si}(x)&=C\\
\operatorname{Ei}(y)&=\operatorname{Si}(x)+C\\
y&=\operatorname{Ei}^{-1}(\operatorname{Si}(x)+C)
\end{aligned}$ <!--SR:!2024-02-03,92,320!2024-03-05,123,340!2024-02-29,118,340-->

<!-- markdownlint MD028 -->

> {{__first-order, [homogeneous](#^homogeneous)__}}
>
> - form: {{$\frac{\mathrm{d}y}{\mathrm{d}x}=F\left(\frac{y}x\right)$, where $F$ is an [integrable](integrability.md) [function](function%20(mathematics).md)}}
> - solution: {{substitute $y\overset{\mathrm{def} }=ux$, then [separate the variables](separation%20of%20variables.md)}}
> - steps: $\begin{aligned}
\frac{\mathrm{d}y}{\mathrm{d}x}&=F\left(\frac{y}x\right)\\
\frac{\mathrm{d}u}{\mathrm{d}x}x+u&=F(u) && (y\overset{\mathrm{def} }=ux)\\
\frac{\mathrm{d}u}{\mathrm{d}x}x&=F(u)-u\\
\frac{\mathrm{d}u}{F(u)-u}&=\frac{\mathrm{d}x}x\\
\frac{\mathrm{d}u}{F(u)-u}-\frac{\mathrm{d}x}x&=0\\
\int\!\frac{\mathrm{d}u}{F(u)-u}-\int\!\frac{\mathrm{d}x}x&=C\\
\int\!\frac{\mathrm{d}u}{F(u)-u}-\ln{x}&=C\\
\ln{x}+C&=\int\!\frac{\mathrm{d}u}{F(u)-u}
\end{aligned}$
> - example: $\begin{aligned}
\frac{\mathrm{d}y}{\mathrm{d}x}&=\frac{y^2\left(e^{\frac{x}y}-1+\frac{x}y\right)}{x^2}\\
\frac{\mathrm{d}u}{\mathrm{d}x}x+u&=u^2e^\frac1u-u^2+u && (y\overset{\mathrm{def} }=ux)\\
\frac{\mathrm{d}u}{\mathrm{d}x}x&=u^2e^\frac1u-u^2\\
\frac{\mathrm{d}u}{u^2e^\frac1u-u^2}&=\frac{\mathrm{d}x}x\\
\frac{\mathrm{d}u}{u^2e^\frac1u-u^2}-\frac{\mathrm{d}x}x&=0\\
\int\!\frac{\mathrm{d}u}{u^2e^\frac1u-u^2}-\int\!\frac{\mathrm{d}x}x&=C\\
\int\!\frac{\mathrm{d}u}{u^2\left(e^\frac1u-1\right)}-\ln{x}&=C\\
-\int\!\frac{\mathrm{d}v}{e^v-1}-\ln{x}&=C && \left(v\overset{\mathrm{def} }=\frac1u\right)\\
-\int\!\frac{\mathrm{d}w}{w^2-w}-\ln{x}&=C && \left(w\overset{\mathrm{def} }=e^v\right)\\
\int\!\frac{\mathrm{d}\!\left(\frac1w\right)}{1-\frac1w}-\ln{x}&=C\\
-\ln\left(\frac1w-1\right)-\ln{x}&=C\\
x\left(\frac1w-1\right)&=C\\
\frac1w&=1+\frac{C}x\\
e^\frac{x}y&=\frac1{\frac{C}x+1}\\
\frac{x}y&=-\ln\left(\frac{C}x+1\right)\\
y&=-\frac{x}{\ln\left(\frac{C}x+1\right)}
\end{aligned}$ <!--SR:!2024-03-04,122,340!2024-02-28,117,340!2024-10-16,265,320-->

#### second-order equation

> {{__second-order, [autonomous](#^autonomous)__}}
>
> - form: {{$\frac{\mathrm{d}^2y}{\mathrm{d}x^2}=F(y)$, where $F$ is an [integrable](integrability.md) [function](function%20(mathematics).md)}}
> - solution: {{multiply by $2\frac{\mathrm{d}y}{\mathrm{d}x}$, then substitute $2\frac{\mathrm{d}y}{\mathrm{d}x}\frac{\mathrm{d}^2y}{\mathrm{d}x^2}=\frac{\mathrm{d} }{\mathrm{d}x}\!\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2$, then integrate twice}}
> - steps: $\begin{aligned}
\frac{\mathrm{d}^2y}{\mathrm{d}x^2}&=F(y)\\
2\frac{\mathrm{d}y}{\mathrm{d}x}\frac{\mathrm{d}^2y}{\mathrm{d}x^2}&=2\frac{\mathrm{d}y}{\mathrm{d}x}F(y)\\
\frac{\mathrm{d} }{\mathrm{d}x}\!\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2&=2\frac{\mathrm{d}y}{\mathrm{d}x}F(y)\\
\mathrm{d}\!\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2&=2F(y)\,\mathrm{d}y\\
\int\!\mathrm{d}\!\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2&=\int\!2F(y)\,\mathrm{d}y\\
\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2&=2\int\!F(y)\,\mathrm{d}y+C_1\\
\frac{\mathrm{d}y}{\mathrm{d}x}&=\pm\sqrt{2\int\!F(y)\,\mathrm{d}y+C_1}\\
\int\!\mathrm{d}x&=\int\!\frac{\mathrm{d}y}{\pm\sqrt{2\int\!F(y)\,\mathrm{d}y+C_1} }\\
x&=\pm\int\!\frac{\mathrm{d}y}{\sqrt{2\int\!F(y)\,\mathrm{d}y+C_1} }+C_2
\end{aligned}$
> - example: $\begin{aligned}
\frac{\mathrm{d}^2x}{\mathrm{d}t^2}&=-\frac{k}mx\\
2\frac{\mathrm{d}x}{\mathrm{d}t}\frac{\mathrm{d}^2x}{\mathrm{d}t^2}&=-2\frac{\mathrm{d}x}{\mathrm{d}t}\frac{k}mx\\
\frac{\mathrm{d} }{\mathrm{d}t}\!\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2&=-2\frac{\mathrm{d}x}{\mathrm{d}t}\frac{k}mx\\
\int\!\mathrm{d}\!\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2&=-\frac{2k}m\int\!x\,\mathrm{d}x\\
\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2&=-\frac{kx^2}m+C_1\\
\frac{\mathrm{d}x}{\mathrm{d}t}&=\pm\sqrt{-\frac{kx^2}m+C_1}\\
\int\!\mathrm{d}t&=\pm\int\!\frac{\mathrm{d}x}{\sqrt{-\frac{kx^2}m+C_1} }\\
t&=\pm\sqrt{\frac{mC_1}k}\int\!\frac{\cos\theta\,\mathrm{d}\theta}{\sqrt{-C_1\sin^2\theta+C_1} } && \left(x\overset{\mathrm{def} }=\sqrt{\frac{mC_1}k}\sin\theta,\theta\in\left[-\frac\pi2,\frac\pi2\right]\right)\\
&=\pm\sqrt{\frac{m}k}\int\!\mathrm{d}\theta\\
&=\pm\sqrt{\frac{m}k}\theta+C_2\\
&=\pm\sqrt{\frac{m}k}\arcsin\frac{x}{\sqrt{\frac{mC_1}k} }+C_2\\
&=\pm\sqrt{\frac{m}k}\arcsin{}C_1x+C_2\\
\arcsin{}C_1x&=\pm\frac{t-C_2}{\sqrt{\frac{m}k} }\\
&=\pm\sqrt{\frac{k}m}t+C_2\\
C_1x&=\pm\sin\left(\sqrt{\frac{k}m}t+C_2\right)\\
&=C_1\sin\left(\sqrt{\frac{k}m}t+C_2\right)\\
&=C_1\left(C_{2\in[-1,1]}\sin\sqrt{\frac{k}m}t+C_{3\in[-1,1]}\cos\sqrt{\frac{k}m}t\right)\\
&=C_1\sin\sqrt{\frac{k}m}t+C_2\cos\sqrt{\frac{k}m}t
\end{aligned}$ <!--SR:!2024-10-27,273,320!2024-08-12,222,320!2024-08-13,223,320-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/ordinary_differential_equation) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
