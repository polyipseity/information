---
aliases:
  - Leibniz integral rule
tags:
  - flashcard/active/general/eng/Leibniz_integral_rule
  - language/in/English
---

# Leibniz integral rule

In [calculus](calculus.md), the __Leibniz integral rule__ is {@{a rule that allows evaluation of [differentiating](derivative.md) an [integral](integral.md) in the form of $$\int_{a(x)}^{b(x)} \! f(x, t) \, \mathrm{d}t$$}@}.

> __Leibniz integral rule__
>
> 1. {@{Let $f(x, t)$ be a [function](function%20(mathematics).md) such that both $f(x, t)$ and its [partial derivative](partial%20derivative.md) with respect to $x$, $f_x(x, t)$, are jointly [continuous](continuous%20function.md) in $x$ and $t$ over the $xt$-plane (not just continuous in both $x$ and $t$ separately), including $x_0 \le x \le x_1$ and $a(x) \le t \le b(x)$ (swapping the inequalities if $b(x) > a(x)$).}@}
> 2. {@{Let $a(x)$ and $b(x)$ be [continuously differentiable functions](differentiable%20function.md) on $x_0 \le x \le x_1$.}@}
> 3. {@{Then, $$\forall x \in [x_0, x_1] \qquad \frac{\mathrm{d} }{\mathrm{d}x} \int_{a(x)}^{b(x)} \! f(x, t) \, \mathrm{d}t = f(x, b(x)) b'(x) - f(x, a(x)) a'(x) + \int_{a(x)}^{b(x)} \! f_x(x, t) \, \mathrm{d}x$$.}@}

<!-- markdownlint MD028 -->

> [!tip] tips
>
> - [intuition](intuition.md) ::@:: $f(x, b(x)) b'(x)$ represents the change caused by moving the right endpoint, $-f(x, a(x)) a'(x)$ represents the change caused by moving the left endpoint, and $\int_{a(x)}^{b(x)} \! f_x(x, t) \, \mathrm{d}x$ represents the change of the [integral](integral.md) caused by changing $x$.

## examples

### example 1: fixed limits

Consider the function {@{$$\varphi (\alpha )=\int _{0}^{1}{\frac {\alpha }{x^{2}+\alpha ^{2} } }\,dx.$$}@}

{@{The function under the integral sign}@} is {@{not continuous at the point $(x,\alpha )=(0,0)$}@}, and {@{the function $\varphi (\alpha )$ has a discontinuity at $\alpha =0$}@} because {@{$\varphi (\alpha )$ approaches $\pm \pi /2$ as $\alpha \to 0^{\pm }$}@}. \(annotation: Simply {@{integrate the above formula normally to see this}@}.\)

If we {@{differentiate $\varphi (\alpha )$ with respect to $\alpha$ under the integral sign}@}, we get {@{$${\frac {d}{d\alpha } }\varphi (\alpha )=\int _{0}^{1}{\frac {\partial }{\partial \alpha } }\left({\frac {\alpha }{x^{2}+\alpha ^{2} } }\right)\,dx=\int _{0}^{1}{\frac {x^{2}-\alpha ^{2} }{(x^{2}+\alpha ^{2})^{2} } }dx=\left.-{\frac {x}{x^{2}+\alpha ^{2} } }\right|_{0}^{1}=-{\frac {1}{1+\alpha ^{2} } },$$}@} \(annotation: Use the {@{quotient rule \(in reverse\) for one of the equality}@}.\) for {@{$\alpha \neq 0$}@}. This may be {@{integrated \(with respect to $\alpha$\)}@} to find {@{$$\varphi (\alpha )={\begin{cases}0,&\alpha =0,\\-\arctan({\alpha })+{\frac {\pi }{2} },&\alpha \neq 0.\end{cases} }$$}@} \(annotation: {@{The constants after integration}@} are obtained by {@{considering $\varphi(\alpha)$ approaches $\pm \pi / 2$ as $\alpha \to 0^\pm$}@}.\)

### example 2: variable limits

An example with {@{variable limits}@}: \(annotation: Evaluate {@{$$\frac {d}{dx}\int _{\sin x}^{\cos x}\cosh t^{2}\,dt$$}@}.\) {@{$${\begin{aligned}{\frac {d}{dx} }\int _{\sin x}^{\cos x}\cosh t^{2}\,dt&=\cosh \left(\cos ^{2}x\right){\frac {d}{dx} }(\cos x)-\cosh \left(\sin ^{2}x\right){\frac {d}{dx} }(\sin x)+\int _{\sin x}^{\cos x}{\frac {\partial }{\partial x} }(\cosh t^{2})\,dt\\[6pt]&=\cosh(\cos ^{2}x)(-\sin x)-\cosh(\sin ^{2}x)(\cos x)+0\\[6pt]&=-\cosh(\cos ^{2}x)\sin x-\cosh(\sin ^{2}x)\cos x.\end{aligned} }$$}@}

## applications

### evaluating definite integrals

The formula {@{$${\frac {d}{dx} }\left(\int _{a(x)}^{b(x)}f(x,t)\,dt\right)=f{\big (}x,b(x){\big )}\cdot {\frac {d}{dx} }b(x)-f{\big (}x,a(x){\big )}\cdot {\frac {d}{dx} }a(x)+\int _{a(x)}^{b(x)}{\frac {\partial }{\partial x} }f(x,t)\,dt$$}@} can be {@{of use when evaluating certain definite integrals}@}. When {@{used in this context}@}, {@{the Leibniz integral rule for differentiating under the integral sign}@} is also known as {@{__Feynman's trick__ for integration}@}.

#### example 3

Consider {@{$$\varphi (\alpha )=\int _{0}^{\pi }\ln \left(1-2\alpha \cos(x)+\alpha ^{2}\right)\,dx,\qquad |\alpha |\neq 1.$$}@} Now, {@{$${\begin{aligned}{\frac {d}{d\alpha } }\varphi (\alpha )&=\int _{0}^{\pi }{\frac {-2\cos(x)+2\alpha }{1-2\alpha \cos(x)+\alpha ^{2} } }dx\\[6pt]&={\frac {1}{\alpha } }\int _{0}^{\pi }\left(1-{\frac {1-\alpha ^{2} }{1-2\alpha \cos(x)+\alpha ^{2} } }\right)dx\\[6pt]&=\left.{\frac {\pi }{\alpha } }-{\frac {2}{\alpha } }\left\{\arctan \left({\frac {1+\alpha }{1-\alpha } }\tan \left({\frac {x}{2} }\right)\right)\right\}\right|_{0}^{\pi }.\end{aligned} }$$}@} \(annotation: For {@{the last equality}@}, use {@{the tangent half-angle substitution}@}.\) As {@{$x$ varies from $0$ to $\pi$}@}, we have {@{$${\begin{cases}{\frac {1+\alpha }{1-\alpha } }\tan \left({\frac {x}{2} }\right)\geq 0,&|\alpha |<1,\\{\frac {1+\alpha }{1-\alpha } }\tan \left({\frac {x}{2} }\right)\leq 0,&|\alpha |>1.\end{cases} }$$}@} Hence, {@{$$\left.\arctan \left({\frac {1+\alpha }{1-\alpha } }\tan \left({\frac {x}{2} }\right)\right)\right|_{0}^{\pi }={\begin{cases}{\frac {\pi }{2} },&|\alpha |<1,\\-{\frac {\pi }{2} },&|\alpha |>1.\end{cases} }$$}@} Therefore, {@{$${\frac {d}{d\alpha } }\varphi (\alpha )={\begin{cases}0,&|\alpha |<1,\\{\frac {2\pi }{\alpha } },&|\alpha |>1.\end{cases} }$$}@} {@{Integrating both sides with respect to $\alpha$}@}, we get: {@{$$\varphi (\alpha )={\begin{cases}C_{1},&|\alpha |<1,\\2\pi \ln |\alpha |+C_{2},&|\alpha |>1.\end{cases} }$$}@}

{@{$C_{1}=0$}@} follows from {@{evaluating $\varphi (0)$}@}: {@{$$\varphi (0)=\int _{0}^{\pi }\ln(1)\,dx=\int _{0}^{\pi }0\,dx=0.$$}@} To {@{determine $C_{2}$ in the same manner}@}, we should need to {@{substitute in a value of $\alpha$ greater than 1 in $\varphi (\alpha )$}@}. This is {@{somewhat inconvenient}@}. Instead, we {@{substitute $\alpha ={\frac {1}{\beta } }$, where $|\beta |<1$}@}. Then, {@{$${\begin{aligned}\varphi (\alpha )&=\int _{0}^{\pi }\left(\ln \left(1-2\beta \cos(x)+\beta ^{2}\right)-2\ln |\beta |\right)dx\\[6pt]&=\int _{0}^{\pi }\ln \left(1-2\beta \cos(x)+\beta ^{2}\right)\,dx-\int _{0}^{\pi }2\ln |\beta |dx\\[6pt]&=0-2\pi \ln |\beta |\\[6pt]&=2\pi \ln |\alpha |.\end{aligned} }$$}@} Therefore, {@{$C_{2}=0$}@} {@{The definition of $\varphi (\alpha )$}@} is now complete: {@{$$\varphi (\alpha )={\begin{cases}0,&|\alpha |<1,\\2\pi \ln |\alpha |,&|\alpha |>1.\end{cases} }$$}@}

{@{The foregoing discussion}@}, of course, {@{does not apply when $\alpha =\pm 1$}@}, since {@{the conditions for differentiability are not met}@}.

#### example 4

{@{$$I=\int _{0}^{\pi /2}{\frac {1}{\left(a\cos ^{2}x+b\sin ^{2}x\right)^{2} } }\,dx,\qquad a,b>0.$$}@} First we calculate: {@{$${\begin{aligned}J&=\int _{0}^{\pi /2}{\frac {1}{a\cos ^{2}x+b\sin ^{2}x} }dx\\[6pt]&=\int _{0}^{\pi /2}{\frac {\frac {1}{\cos ^{2}x} }{a+b{\frac {\sin ^{2}x}{\cos ^{2}x} } } }dx\\[6pt]&=\int _{0}^{\pi /2}{\frac {\sec ^{2}x}{a+b\tan ^{2}x} }dx\\[6pt]&={\frac {1}{b} }\int _{0}^{\pi /2}{\frac {1}{\left({\sqrt {\frac {a}{b} } }\right)^{2}+\tan ^{2}x} }\,d(\tan x)\\[6pt]&=\left.{\frac {1}{\sqrt {ab} } }\arctan \left({\sqrt {\frac {b}{a} } }\tan x\right)\right|_{0}^{\pi /2}\\[6pt]&={\frac {\pi }{2{\sqrt {ab} } } }.\end{aligned} }$$}@} {@{The limits of integration}@} being {@{independent of $a$}@}, we have: {@{$${\frac {\partial J}{\partial a} }=-\int _{0}^{\pi /2}{\frac {\cos ^{2}x}{\left(a\cos ^{2}x+b\sin ^{2}x\right)^{2} } }\,dx$$}@} On the other hand: {@{$${\frac {\partial J}{\partial a} }={\frac {\partial }{\partial a} }\left({\frac {\pi }{2{\sqrt {ab} } } }\right)=-{\frac {\pi }{4{\sqrt {a^{3}b} } } }.$$}@} {@{Equating these two relations}@} then yields {@{$$\int _{0}^{\pi /2}{\frac {\cos ^{2}x}{\left(a\cos ^{2}x+b\sin ^{2}x\right)^{2} } }\,dx={\frac {\pi }{4{\sqrt {a^{3}b} } } }.$$}@} In {@{a similar fashion}@}, {@{pursuing ${\frac {\partial J}{\partial b} }$}@} yields {@{$$\int _{0}^{\pi /2}{\frac {\sin ^{2}x}{\left(a\cos ^{2}x+b\sin ^{2}x\right)^{2} } }\,dx={\frac {\pi }{4{\sqrt {ab^{3} } } } }.$$}@} {@{Adding the two results}@} then produces {@{$$I=\int _{0}^{\pi /2}{\frac {1}{\left(a\cos ^{2}x+b\sin ^{2}x\right)^{2} } }\,dx={\frac {\pi }{4{\sqrt {ab} } } }\left({\frac {1}{a} }+{\frac {1}{b} }\right),$$}@} which {@{computes $I$ as desired}@}.

This derivation may {@{be generalized}@}. Note that if we define {@{$$I_{n}=\int _{0}^{\pi /2}{\frac {1}{\left(a\cos ^{2}x+b\sin ^{2}x\right)^{n} } }\,dx,$$}@} it can easily be shown that {@{$$(1-n)I_{n}={\frac {\partial I_{n-1} }{\partial a} }+{\frac {\partial I_{n-1} }{\partial b} }$$}@} {@{Given $I_{1}$}@}, {@{this integral reduction formula}@} can be used to {@{compute all of the values of $I_{n}$ for $n>1$}@}. {@{Integrals like $I$ and $J$}@} may also be {@{handled using the [Weierstrass substitution](Weierstrass%20substitution.md)}@}.

#### example 5

Here, we consider {@{the integral $$I(\alpha )=\int _{0}^{\pi /2}{\frac {\ln(1+\cos \alpha \cos x)}{\cos x} }\,dx,\qquad 0<\alpha <\pi .$$}@} {@{Differentiating under the integral with respect to $\alpha$}@}, we have {@{$${\begin{aligned}{\frac {d}{d\alpha } }I(\alpha )&=\int _{0}^{\pi /2}{\frac {\partial }{\partial \alpha } }\left({\frac {\ln(1+\cos \alpha \cos x)}{\cos x} }\right)\,dx\\[6pt]&=-\int _{0}^{\pi /2}{\frac {\sin \alpha }{1+\cos \alpha \cos x} }\,dx\\&=-\int _{0}^{\pi /2}{\frac {\sin \alpha }{\left(\cos ^{2}{\frac {x}{2} }+\sin ^{2}{\frac {x}{2} }\right)+\cos \alpha \left(\cos ^{2}{\frac {x}{2} }-\sin ^{2}{\frac {x}{2} }\right)} }\,dx\\[6pt]&=-{\frac {\sin \alpha }{1-\cos \alpha } }\int _{0}^{\pi /2}{\frac {1}{\cos ^{2}{\frac {x}{2} } } }{\frac {1}{ {\frac {1+\cos \alpha }{1-\cos \alpha } }+\tan ^{2}{\frac {x}{2} } } }\,dx\\[6pt]&=-{\frac {2\sin \alpha }{1-\cos \alpha } }\int _{0}^{\pi /2}{\frac { {\frac {1}{2} }\sec ^{2}{\frac {x}{2} } }{ {\frac {2\cos ^{2}{\frac {\alpha }{2} } }{2\sin ^{2}{\frac {\alpha }{2} } } }+\tan ^{2}{\frac {x}{2} } } }\,dx\\[6pt]&=-{\frac {2\left(2\sin {\frac {\alpha }{2} }\cos {\frac {\alpha }{2} }\right)}{2\sin ^{2}{\frac {\alpha }{2} } } }\int _{0}^{\pi /2}{\frac {1}{\cot ^{2}{\frac {\alpha }{2} }+\tan ^{2}{\frac {x}{2} } } }\,d\left(\tan {\frac {x}{2} }\right)\\[6pt]&=-2\cot {\frac {\alpha }{2} }\int _{0}^{\pi /2}{\frac {1}{\cot ^{2}{\frac {\alpha }{2} }+\tan ^{2}{\frac {x}{2} } } }\,d\left(\tan {\frac {x}{2} }\right)\\[6pt]&=-2\arctan \left(\tan {\frac {\alpha }{2} }\tan {\frac {x}{2} }\right){\bigg |}_{0}^{\pi /2}\\[6pt]&=-\alpha .\end{aligned} }$$}@} \(annotation: Alternatively, use {@{tangent half-angle substitution}@}.\) Therefore: {@{$$I(\alpha )=C-{\frac {\alpha ^{2} }{2} }.$$}@} But {@{$I{\left({\frac {\pi }{2} }\right)}=0$ by definition}@} so {@{$C={\frac {\pi ^{2} }{8} }$}@} and {@{$$I(\alpha )={\frac {\pi ^{2} }{8} }-{\frac {\alpha ^{2} }{2} }.$$}@}

#### example 6

Here, we consider {@{the integral $$\int _{0}^{2\pi }e^{\cos \theta }\cos(\sin \theta )\,d\theta .$$}@} We {@{introduce a new variable _φ_ and rewrite the integral}@} as {@{$$f(\varphi )=\int _{0}^{2\pi }e^{\varphi \cos \theta }\cos(\varphi \sin \theta )\,d\theta .$$}@} When {@{_φ_ = 1 this equals the original integral}@}. However, this more general integral may be {@{differentiated with respect to $\varphi$}@}: {@{$${\frac {df}{d\varphi } }=\int _{0}^{2\pi }{\frac {\partial }{\partial \varphi } }\left[e^{\varphi \cos \theta }\cos(\varphi \sin \theta )\right]d\theta =\int _{0}^{2\pi }e^{\varphi \cos \theta }\left[\cos \theta \cos(\varphi \sin \theta )-\sin \theta \sin(\varphi \sin \theta )\right]d\theta .$$}@} Now, {@{fix _φ_}@}, and consider {@{the vector field on $\mathbb {R} ^{2}$}@} defined by {@{$\mathbf {F} (x,y)=(F_{1}(x,y),F_{2}(x,y)):=(e^{\varphi x}\sin(\varphi y),e^{\varphi x}\cos(\varphi y))$}@}. Further, choose {@{the [positive oriented](curve%20orientation.md) parameterization of the [unit circle](unit%20circle.md) $S^{1}$}@} given by {@{$\mathbf {r} \colon [0,2\pi )\to \mathbb {R} ^{2}$, $\mathbf {r} (\theta ):=(\cos \theta ,\sin \theta )$}@}, so that {@{$\mathbf {r} '(t)=(-\sin \theta ,\cos \theta )$}@}. Then {@{the final integral above}@} is precisely {@{$${\begin{aligned}&\int _{0}^{2\pi }e^{\varphi \cos \theta }\left[\cos \theta \cos(\varphi \sin \theta )-\sin \theta \sin(\varphi \sin \theta )\right]d\theta \\[6pt]={}&\int _{0}^{2\pi }{\begin{bmatrix}e^{\varphi \cos \theta }\sin(\varphi \sin \theta )\\e^{\varphi \cos \theta }\cos(\varphi \sin \theta )\end{bmatrix} }\cdot {\begin{bmatrix}-\sin \theta \\{\hphantom {-} }\cos \theta \end{bmatrix} }\,d\theta \\[6pt]={}&\int _{0}^{2\pi }\mathbf {F} (\mathbf {r} (\theta ))\cdot \mathbf {r} '(\theta )\,d\theta \\[6pt]={}&\oint _{S^{1} }\mathbf {F} (\mathbf {r} )\cdot d\mathbf {r} =\oint _{S^{1} }F_{1}\,dx+F_{2}\,dy,\end{aligned} }$$}@} {@{the line integral}@} of {@{$\mathbf {F}$ over $S^{1}$}@}. By {@{[Green's Theorem](Green's%20theorem.md)}@}, this equals {@{the double integral $$\iint _{D}{\frac {\partial F_{2} }{\partial x} }-{\frac {\partial F_{1} }{\partial y} }\,dA,$$}@} where {@{$D$ is the closed [unit disc](unit%20disk.md)}@}. Its integrand is {@{identically 0}@}, so {@{$df/d\varphi$ is likewise identically zero}@}. This implies that {@{_f_\(_φ_\) is constant}@}. {@{The constant may be determined}@} by {@{evaluating $f$ at $\varphi =0$}@}: {@{$$f(0)=\int _{0}^{2\pi }1\,d\theta =2\pi .$$}@} Therefore, {@{the original integral also equals $2\pi$}@}.

#### other problems to solve

There are {@{innumerable other integrals}@} that can be {@{solved using the technique of differentiation under the integral sign}@}. For example, in {@{each of the following cases}@}, {@{the original integral}@} may be {@{replaced by a similar integral having a new parameter $\alpha$}@}: $${\begin{aligned}\int _{0}^{\infty }{\frac {\sin x}{x} }\,dx&\to \int _{0}^{\infty }e^{-\alpha x}{\frac {\sin x}{x} }dx,\\[6pt]\int _{0}^{\pi /2}{\frac {x}{\tan x} }\,dx&\to \int _{0}^{\pi /2}{\frac {\tan ^{-1}(\alpha \tan x)}{\tan x} }dx,\\[6pt]\int _{0}^{\infty }{\frac {\ln(1+x^{2})}{1+x^{2} } }\,dx&\to \int _{0}^{\infty }{\frac {\ln(1+\alpha ^{2}x^{2})}{1+x^{2} } }dx\\[6pt]\int _{0}^{1}{\frac {x-1}{\ln x} }\,dx&\to \int _{0}^{1}{\frac {x^{\alpha }-1}{\ln x} }dx.\end{aligned} }$$

> __flashcards__
>
> - \(annotation: Dirichlet integral\) $\int _{0}^{\infty }{\frac {\sin x}{x} }\,dx$ ::@:: $\int _{0}^{\infty }e^{-\alpha x}{\frac {\sin x}{x} }dx$ \(annotation: Also requires proving the formula remains valid when $\alpha = 0$.\)
> - $\int _{0}^{\pi /2}{\frac {x}{\tan x} }\,dx$ ::@:: $\int _{0}^{\pi /2}{\frac {\tan ^{-1}(\alpha \tan x)}{\tan x} }dx$
> - $\int _{0}^{\infty }{\frac {\ln(1+x^{2})}{1+x^{2} } }\,dx$ ::@:: $\int _{0}^{\infty }{\frac {\ln(1+\alpha ^{2}x^{2})}{1+x^{2} } }dx$
> - $\int _{0}^{1}{\frac {x-1}{\ln x} }\,dx$ ::@:: $\int _{0}^{1}{\frac {x^{\alpha }-1}{\ln x} }dx$

{@{The first integral, the [Dirichlet integral](Dirichlet%20integral.md)}@}, is {@{absolutely convergent for positive _α_}@} but {@{only conditionally convergent when $\alpha =0$}@}. Therefore, {@{differentiation under the integral sign}@} is {@{easy to justify when $\alpha >0$}@}, but {@{proving that the resulting formula remains valid when $\alpha =0$}@} requires {@{some careful work}@}. \(annotation: One method is {@{using the dominated convergence theorem}@}.\)

### infinite series

{@{The measure-theoretic version}@} of {@{differentiation under the integral sign}@} also {@{applies to summation \(finite or infinite\)}@} by {@{interpreting summation as [counting measure](counting%20measure.md)}@}. {@{An example of an application}@} is the fact that {@{[power series](power%20series.md) are differentiable in their radius of convergence}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup>

### Euler-Lagrange equations

{@{The Leibniz integral rule}@} is {@{used in the derivation of the [Euler-Lagrange equation](Euler-Lagrange%20equation.md)}@} in {@{[variational calculus](variational%20calculus.md)}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Leibniz_integral_rule) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
