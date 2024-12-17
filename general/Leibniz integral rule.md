---
aliases:
  - Leibniz integral rule
tags:
  - flashcard/active/general/Leibniz_integral_rule
  - language/in/English
---

# Leibniz integral rule

In [calculus](calculus.md), the __Leibniz integral rule__ is {@{a rule that allows evaluation of [differentiating](derivative.md) an [integral](integral.md) in the form of $$\int_{a(x)}^{b(x)} \! f(x, t) \, \mathrm{d}t$$}@}. <!--SR:!2027-08-24,1050,350-->

> __Leibniz integral rule__
>
> 1. {@{Let $f(x, t)$ be a [function](function%20(mathematics).md) such that both $f(x, t)$ and its [partial derivative](partial%20derivative.md) with respect to $x$, $f_x(x, t)$, are jointly [continuous](continuous%20function.md) in $x$ and $t$ over the $xt$-plane (not just continuous in both $x$ and $t$ separately), including $x_0 \le x \le x_1$ and $a(x) \le t \le b(x)$ (swapping the inequalities if $b(x) > a(x)$).}@}
> 2. {@{Let $a(x)$ and $b(x)$ be [continuously differentiable functions](differentiable%20function.md) on $x_0 \le x \le x_1$.}@}
> 3. {@{Then, $$\forall x \in [x_0, x_1] \qquad \frac{\mathrm{d} }{\mathrm{d}x} \int_{a(x)}^{b(x)} \! f(x, t) \, \mathrm{d}t = f(x, b(x)) b'(x) - f(x, a(x)) a'(x) + \int_{a(x)}^{b(x)} \! f_x(x, t) \, \mathrm{d}x$$.}@} <!--SR:!2025-09-20,370,241!2026-02-21,556,321!2026-08-01,612,281-->

<!-- markdownlint MD028 -->

> [!tip] tips
>
> - [intuition](intuition.md) ::@:: $f(x, b(x)) b'(x)$ represents the change caused by moving the right endpoint, $-f(x, a(x)) a'(x)$ represents the change caused by moving the left endpoint, and $\int_{a(x)}^{b(x)} \! f_x(x, t) \, \mathrm{d}x$ represents the change of the [integral](integral.md) caused by changing $x$. <!--SR:!2025-07-17,408,310!2025-01-03,227,344-->

## examples

### example 1: fixed limits

Consider the [function](function%20(mathematics).md):

$$f(a) = \int_0^1\! \frac{a}{a^2 + x^2} \,\mathrm{d}x$$

Note that the [integrand](integral.md) is not [continuous](continuous%20function.md) (undefined, so neither continuous nor discontinuous) at the point $(x, a) = (0, 0)$. Accordingly, we need to consider whether $f(a)$ is continuous when $a = 0$. It turns out it is discontinuous because $\lim_{a \to 0^\pm} f(a) = \pm\frac\pi2$. Keep this in mind.

[Differentiate](derivative.md) $f(a)$ with respect to $a$ under the [integral](integral.md) sign to obtain:

$$\begin{aligned}
\frac{\mathrm{d} }{\mathrm{d}a} f(a) & = \int_0^1\! \frac{\partial}{\partial a} \frac{a}{a^2 + x^2} \,\mathrm{d}x \\
& = \int_0^1\! \frac{a^2 + x^2 - 2a^2}{\left(a^2 + x^2\right)^2} \,\mathrm{d}x \\
& = \int_0^1\! \frac{x^2 - a^2}{\left(x^2 + a^2\right)^2} \,\mathrm{d}x \\
& = -\int_0^1\! \frac{-x^2 + a^2}{\left(x^2 + a^2\right)^2} \,\mathrm{d}x \\
& = -\int_0^1\! \frac{\left(x^2 + a^2\right) - 2x^2}{\left(x^2 + a^2\right)^2} \,\mathrm{d}x \\
& = -\left[\frac{x}{x^2 + a^2}\right]_0^1 \\
& = -\frac{1}{x^2 + 1} && (a \ne 0) \\
\end{aligned}$$

The above is true for all [reals](real%20number.md) except for $a = 0$. To find $f(a)$, we need to [integrate](integral.md) the above [derivative](derivative.md) separately on the [intervals](interval%20(mathematics).md) $(-\inf, 0)$ and $(0, \inf)$ and consider $f(0)$ separately:

$$\begin{aligned}
f(0) & = \int_0^1\! \frac{0}{0 + x^2} \,\mathrm{d}x \\
& = \lim_{b \to 0^+} \int_b^1\! 0 \,\mathrm{d}x \\
& = 0 \\
f(a) & = -\int\! \frac{1}{x^2 + 1} \,\mathrm{d}x \\
& = \begin{cases}-\arctan x + C_1, & a < 0 \\
0, & a = 0 \\
-\arctan x + C_2, & a > 0
\end{cases} && (\text{discontinuous when }a = 0, f(0) = 0) \\
-\arctan 1 + C_1 & = f(1) \\
& = \int_0^1\! \frac{1}{1 + x^2} \,\mathrm{d}x \\
& = [\arctan x]_0^1 \\
& = \arctan 1 \\
C_1 & = 2 \arctan 1 \\
& = \frac\pi 2 \\
-\arctan (-1) + C_2 & = f(-1) \\
\arctan 1 + C_2 & = -\int_0^1\! \frac{1}{1 + x^2} \,\mathrm{d}x \\
& = -[\arctan x]_0^1 \\
& = -\arctan 1 \\
C_2 & = -2 \arctan 1 \\
& = -\frac\pi 2 \\
f(a) & = \begin{cases}-\arctan x - \frac\pi2, & a < 0 \\
0, & a = 0 \\
-\arctan x + \frac\pi2, & a > 0 \end{cases} \\
& = \begin{cases}0, & a = 0 \\
-\arctan x + \frac\pi2\operatorname{sgn}(a), & a \ne 0 \end{cases}
\end{aligned}$$

Direct integration also works with similar difficulty, though [continuity](continuous%20function.md) still needs to be considered like before:

$$\begin{aligned}
f(a) & = \int_0^1\! \frac{a}{a^2 + x^2} \,\mathrm{d}x \\
& = \int_{x = 0}^{x = 1}\! \frac{a^2}{a^2 + x^2} \,\mathrm{d}\frac{x}a \\
& = \int_{x = 0}^{x = 1}\! \frac{1}{1 + \left(\frac{x}a\right)^2} \,\mathrm{d}\frac{x}a \\
& = \left[ \arctan \frac{x}a \right]_0^1 \\
& = \arctan \frac{1}a \\
& = -\arctan a + \frac\pi2 \operatorname{sgn}(a) && (a \ne 0) \\
f(0) & = \int_0^1\! \frac{0}{0 + x^2} \,\mathrm{d}x \\
& = \lim_{b \to 0^+} \int_b^1\! 0 \,\mathrm{d}x \\
& = 0 \\
f(a) & = \begin{cases} 0, & a = 0 \\
-\arctan a + \frac\pi2 \operatorname{sgn}(a), & a \ne 0 \end{cases}
\end{aligned}$$

> [!tip] tips
>
> - takeaway ::@:: No matter whether direct [integration](integral.md) or the Leibniz integral rule is used, [continuity](continuous%20function.md) of the integrand and the integral needs to be considered. <!--SR:!2026-08-21,670,324!2025-02-28,272,344-->

### example 2: variable limits

Consider the [function](function%20(mathematics).md):

$$f(a) = \int_0^a\! \frac{a - x}{\sqrt{a^2 - x^2} } \,\mathrm{d}x$$

Note that the integrand is not [continuous](continuous%20function.md) (undefined, so neither continuous nor discontinuous) along the lines $x = \pm a$. It is [Lebesgue integrable](Lebesgue%20integration.md) and thus equals the [improper Riemann integral](Riemann%20integral.md): $$f(a) = \lim_{b \to a^-} \int_0^b\! \frac{a - x}{\sqrt{a^2 - x^2} } \,\mathrm{d}x$$

Note that a [limit](limit%20of%20a%20function.md) is being [differentiated](derivative.md). We can prove that differentiating the limit is the same as taking the limit of the derivative, assuming conditions on $f(x, a)$ required by the Leibniz integral rule:

$$\begin{aligned}
\frac{\mathrm{d} }{\mathrm{d}a} \lim_{b \to a^{-} } \int_0^b\! f(x, a) \,\mathrm{d}x & = \lim_{h \to 0} \frac1h \left( {\lim_{b \to (a + h)^-} \int_0^b\! f(x, a + h) \,\mathrm{d}x - \lim_{b \to a^-} \int_0^b\! f(x, a) \,\mathrm{d}x} \right) && (\text{by definition}) \\
& = \lim_{h \to 0} \frac1h \left( {\lim_{b \to (a + h)^-} \lim_{c \to a^{-} } \left( \int_0^b\! f(x, a + h) \,\mathrm{d}x - \int_0^c\! f(x, a + h) \,\mathrm{d}x + \int_0^c\! f(x, a + h) \,\mathrm{d}x \right) - \lim_{b \to a^-} \int_0^b\! f(x, a) \,\mathrm{d}x} \right) \\
& = \lim_{h \to 0} \frac1h \left( \lim_{b \to (a+h)^-} \int_0^b\! f(x, a + h) \,\mathrm{d}x - \lim_{c \to a^-} \int_0^c\! f(x, a + h) \,\mathrm{d}x + \lim_{c \to a^-} \int_0^c\! f(x, a + h) \,\mathrm{d}x - \lim_{b \to a^-} \int_0^b f(x, a) \,\mathrm{d}x \right) && (\text{requires the newly expanded limits to exist}) \\
& = \lim_{h \to 0} \frac1h \left( \lim_{b \to a^-} \left( \int_0^{b + h}\! f(x, a + h) \,\mathrm{d}x - \int_0^b\! f(x, a + h) \,\mathrm{d}x \right) + \lim_{b \to a^-} \left( \int_0^b\! (f(x, a + h) - f(x, a)) \,\mathrm{d}x \right) \right) \\
& = \lim_{h \to 0} \frac1h \lim_{b \to a^-} \left( \int_0^{b + h}\! f(x, a + h) \,\mathrm{d}x - \int_0^b\! f(x, a + h) \,\mathrm{d}x \right) + \lim_{h \to 0} \frac1h \lim_{b \to a^-} \left( \int_0^b\! (f(x, a + h) - f(x, a)) \,\mathrm{d}x \right) && (\text{requires the newly expanded limits to exist}) \\
& = \lim_{b \to a^-} \lim_{h \to 0} \frac1h \left( \int_0^{b + h}\! f(x, a + h) \,\mathrm{d}x - \int_0^b\! f(x, a + h) \,\mathrm{d}x \right) + \lim_{b \to a^-} \lim_{h \to 0} \left( \int_0^b\! \frac1h (f(x, a + h) - f(x, a)) \,\mathrm{d}x \right) && (\text{requires the expressions in the limits to be continuous over the }bh\text{-plane}) \\
& = \lim_{b \to a^-} \frac{\partial}{\partial b} \int_0^b\! f(x, a) \,\mathrm{d}x + \lim_{b \to a^-} \int_0^b\! \frac{\partial}{\partial a} f(x, a) \,\mathrm{d}x && (\text{requires }f(x, a)\text{ to be continuous over }a) \\
& = \lim_{b \to a^-} f(b, a) + \lim_{b \to a^-} \int_0^b\! \frac{\partial}{\partial a} f(x, a) \,\mathrm{d}x
\end{aligned}$$

Now [differentiate](derivative.md) $f(a)$ with respect to $a$ using the Leibniz integral rule:

$$\begin{aligned}
\frac{\mathrm{d} }{\mathrm{d}a}f(a) & = \frac{\mathrm{d} }{\mathrm{d}a} \lim_{b \to a^-} \int_0^b \frac{a - x}{\sqrt{a^2 - x^2} } \,\mathrm{d}x \\
& = \lim_{b \to a^-} \frac{a - b}{\sqrt{a^2 - b^2} } + \lim_{b \to a^-} \int_0^b\! \frac{\sqrt{a^2 - x^2} - \frac{(a-x)(2a)}{2\sqrt{a^2 - x^2} } }{a^2 - x^2} \,\mathrm{d}x \\
& = \lim_{b \to a^-} \frac{-1}{\frac{-2b}{2\sqrt{a^2 - b^2} } } + \lim_{b \to a^-} \int_0^b\! \frac{(a + x)(a - x) - a(a - x)}{(a + x) (a - x) \sqrt{a^2 - x^2} } \,\mathrm{d}x \\
& = \lim_{b \to a^-} \frac{\sqrt{a^2 - b^2} }{b} + \lim_{b \to a^-} \int_0^b\! \frac{x}{(a + x)\sqrt{a^2 - x^2} } \,\mathrm{d}x \\
& = 0 + \lim_{b \to a^-} \int_0^b\! \frac{a + x - a}{(a + x) \sqrt{a^2 - x^2} } \,\mathrm{d}x \\ \\
& = \lim_{b \to a^-} \left(\int_0^b\! \frac1{\sqrt{a^2 - x^2} } \,\mathrm{d}x - a \int_0^b\! \frac{1}{(a + x)\sqrt{a^2 - x^2} } \,\mathrm{d}x \right) \\
& = \lim_{b \to a^-} \left(\left[\arcsin \frac{x}{\lvert a \rvert} \right]_0^b - a \int_{x = 0}^{x = b}\! \frac{a \cos \theta}{(a + a \sin \theta) \sqrt{a^2 - a^2 \sin^2 \theta} } \,\mathrm{d}\theta \right) && \left(x = a \sin \theta, \theta \in \left[ -\frac\pi2, \frac\pi2 \right]\right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} - \int_{x = 0}^{x = b}\! \frac{1}{1 + \sin \theta} \,\mathrm{d}\theta \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} - \int_{x = 0}^{x = b}\! \frac{1}{1 + \left(\sin \frac\theta2 + \cos \frac\theta2 \right)^2 - 1} \,\mathrm{d}\theta \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} - \int_{x = 0}^{x = b}\! \frac{\sec^2 \frac\theta2}{\left(\tan \frac\theta2 + 1\right)^2} \,\mathrm{d}\theta \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} - 2 \int_{x = 0}^{x = b}\! \frac{1}{\left(\tan \frac\theta2 + 1 \right)^2} \,\mathrm{d}\!\left(\tan \frac\theta2 + 1 \right) \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + 2 \left[ \frac{1}{\tan \frac\theta2 + 1} \right]_{x = 0}^{x = b} \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + 2 \left[ \frac{1}{\tan \frac\theta2 + 1} \right]_{x = 0}^{x = b} \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + 2 \left[ \frac{1}{\frac{1 - \cos\theta}{\sin \theta} + 1} \right]_{x = 0}^{x = b} \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + 2 \left[ \frac{1}{\frac{1 - \frac{\sqrt{a^2 - x^2} }{a} }{\frac{x}{a} } + 1} \right]_0^b \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + 2 \left[ \frac{1}{\frac{a - \sqrt{a^2 - x^2} }{x} + 1} \right]_0^b \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + 2 \left[ \frac{x}{a + x - \sqrt{a^2 - x^2} } \right]_0^b \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + 2 \left[ \frac{x\left(a + x + \sqrt{a^2 - x^2}\right)}{\left(a + x - \sqrt{a^2 - x^2}\right)\left(a + x + \sqrt{a^2 - x^2}\right)} \right]_0^b \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + 2 \left[ \frac{x\left(a + x + \sqrt{a^2 - x^2}\right)}{(a + x)^2 - \left(a^2 - x^2\right)} \right]_0^b \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + 2 \left[ \frac{ax + x^2 + x\sqrt{a^2 - x^2} }{2ax + 2x^2} \right]_0^b \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + \left[ \frac{ax + x^2 + x\sqrt{a^2 - x^2} }{ax + x^2} \right]_0^b \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + \left[ \frac{x\sqrt{a^2 - x^2} }{ax + x^2} \right]_0^b \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + \left[ \frac{\sqrt{a^2 - x^2} }{a + x} \right]_0^b \right) \\
& = \lim_{b \to a^-} \left(\arcsin \frac{b}{\lvert a \rvert} + \frac{\sqrt{a^2 - b^2} }{a + b} - \frac{\lvert a \rvert}{a} \right) \\
& = \frac\pi2 \operatorname{sgn}(a) + 0 - \operatorname{sgn}(a) \\
& = \left(\frac\pi2 - 1\right)\operatorname{sgn}(a) \\
\end{aligned}$$

This can be integrated with respect to $a$ to yield $f(a)$:

$$\begin{aligned}
f(a) & = \int\! \left(\frac\pi2 - 1\right)\operatorname{sgn}(a) \,\mathrm{d}a \\
& = \left(\frac\pi2 - 1\right)\lvert a \rvert + C \\
& = \left(\frac\pi2 - 1\right)\lvert a \rvert && (f(0) = 0)
\end{aligned}$$

However, for this example, it is much less troublesome to find $f(a)$ directly:

$$\begin{aligned}
f(a) & = \int_0^a\! \frac{a - x}{\sqrt{a^2 - x^2} } \,\mathrm{d}x \\
& = a \int_0^a\! \frac{1}{\sqrt{a^2 - x^2} } \,\mathrm{d}x - \int_0^a\! \frac{x}{\sqrt{a^2 - x^2} } \,\mathrm{d}x \\
& = a \int_0^a\! \frac{1}{\sqrt{a^2 - x^2} } \,\mathrm{d}x + \int_{x = 0}^{x = a}\! \,\mathrm{d}\sqrt{a^2 - x^2} \\
& = a \int_0^a\! \frac{1}{\sqrt{a^2 - x^2} } \,\mathrm{d}x + \int_{x = 0}^{x = a}\! \,\mathrm{d}\sqrt{a^2 - x^2} \\
& = a \left[ \arcsin \frac{x}{\lvert a \rvert} \right]_0^a + \left[\sqrt{a^2 - x^2}\right]_0^a \\
& = a \arcsin \frac{a}{\lvert a \rvert} - \lvert a \rvert \\
& = \frac\pi2 \lvert a \rvert - \lvert a \rvert \\
& = \left(\frac\pi2 - 1\right) \lvert a \rvert
\end{aligned}$$

> [!tip] tips
>
> - takeaway ::@:: Usually, it is easier to [integrate](integral.md) directly rather than through the Leibniz integral rule. <!--SR:!2025-03-10,267,308!2024-12-30,223,344-->

## applications

### evaluating definite integrals

#### example 3: natural logarithm

Consider:

$$f(a) = \int_0^\pi\! \ln\left(1 - 2a \cos x + a^2\right) \,\mathrm{d}x$$

Observe that $f(a)$ is a [even function](even%20and%20odd%20functions.md), i.e. $f(a) = f(-a)$. Also, note that when $\lvert a \rvert = 1$, the [integrand](integral.md) is not [continuous](continuous) (undefined, so neither continuous nor discontinuous) at one of the integral's endpoint. We can see this by checking $1 - 2a + a^2 > 0$ when $\cos x = 1$ and $1 + 2a + a^2 > 0$ when $\cos x = -1$:

$$\begin{aligned}
1 - 2a + a^2 > 0 & \text{ and } 1 + 2a + a^2 > 0 \\
(a - 1)^2 > 0 & \text{ and } (a + 1)^2 > 0 \\
a \ne 1 & \text{ and } a \ne -1 \\
\lvert a \rvert \ne 1
\end{aligned}$$

As the Leibniz integral rule cannot be applied when $\lvert a \rvert = 1$, differentiate $f(a)$ with respect to $a$ using the rule, assuming $\lvert a \rvert \ne 1$:

$$\begin{aligned}
\frac{\mathrm{d} }{\mathrm{d}a} f(a) & = \frac{\mathrm{d} }{\mathrm{d}a} \int_0^\pi\! \ln\left(1 - 2a \cos x + a^2\right) \,\mathrm{d}x && (\lvert a \rvert \ne 1) \\
& = \int_0^\pi\! \frac{\partial}{\partial a} \ln\left(1 - 2a \cos x + a^2\right) \,\mathrm{d}x \\
& = \int_0^\pi\! \frac{-2 \cos x + 2a}{1 - 2a \cos x + a^2} \,\mathrm{d}x \\
& = \frac1a \int_0^\pi\! \frac{-2a \cos x + 2a^2}{1 - 2a \cos x + a^2} \,\mathrm{d}x \\
& = \frac\pi a - \frac{1 - a^2}a \int_0^\pi\! \frac{1}{1 - 2a \cos x + a^2} \,\mathrm{d}x \\
& = \frac\pi a - \frac{1 - a^2}a \int_0^\pi\! \frac{1}{1 - 2a \left(2\cos^2 \frac{x}2 - 1\right) + a^2} \,\mathrm{d}x \\
& = \frac\pi a - \frac{1 - a^2}a \int_0^\pi\! \frac{1}{(a + 1)^2 - 4a\cos^2 \frac{x}2} \,\mathrm{d}x \\
& = \frac\pi a - \frac{1 - a^2}a \int_0^\pi\! \frac{\sec^2 \frac{x}2}{(a + 1)^2 \sec^2 \frac{x}2 - 4a} \,\mathrm{d}x && (\text{note that the integral becomes improper, which is justifiable} \\ & && \text{since the integral is absolutely convergent when } \lvert a \rvert \ne 1) \\
& = \frac\pi a - \frac{1 - a^2}a \int_0^\pi\! \frac{\sec^2 \frac{x}2}{(a + 1)^2 \tan^2 \frac{x}2 + (a + 1)^2 - 4a} \,\mathrm{d}x \\
& = \frac\pi a - \frac{1 - a^2}a \int_0^\pi\! \frac{\sec^2 \frac{x}2}{(a + 1)^2 \tan^2 \frac{x}2 + (a - 1)^2} \,\mathrm{d}x \\
& = \frac\pi a - \frac{2 - 2a^2}a \int_{x = 0}^{x = \pi}\! \frac{1}{(a + 1)^2 \tan^2 \frac{x}2 + (a - 1)^2} \,\mathrm{d}\!\left(\tan\frac{x}2\right) \\
& = \frac\pi a - \frac{2 - 2a^2}a \left[\frac1{(a - 1)(a + 1)} \arctan\left( \frac{a + 1}{a - 1} \tan \frac{x}2 \right) \right]_0^\pi \\
& = \frac\pi a + \frac{2}a \left[\arctan\left( \frac{a + 1}{a - 1} \tan \frac{x}2 \right) \right]_0^\pi \\
& = \frac\pi a + \frac{2}a \arctan\left( \frac{a + 1}{a - 1} \tan \frac{\pi}2 \right) \\
\end{aligned}$$

We cannot directly evaluate $\arctan \left(\frac{a + 1}{a - 1} \tan \frac{\pi}2 \right)$, but we can consider its left-sided [limit](limit%20of%20a%20function.md), which is justified by the definition of [improper Riemann integral](improper%20integral.md):

$$\begin{aligned}
\lim_{x \to \pi^-} \arctan\left(\frac{a + 1}{a - 1} \tan \frac{x}2\right) & = \frac{\pi}2 \operatorname{sgn}\left(\frac{a + 1}{a - 1}\right) && (\lvert a \rvert \ne 1) \\
& = \begin{cases} -\frac\pi2, & \lvert a \rvert < 1 \\
\frac\pi2, & \lvert a \rvert > 1 \end{cases}
\end{aligned}$$

Therefore the [derivative](derivative.md) of $f(a)$ with respect to $a$ is:

$$\begin{aligned}
\frac{\mathrm{d} }{\mathrm{d}a} f(a) & = \begin{cases} \frac\pi a - \frac\pi a, & \lvert a \rvert < 1 \\
\frac\pi a + \frac\pi a, & \lvert a \rvert > 1 \end{cases} \\
& = \begin{cases} 0, & \lvert a \rvert < 1 \\
\frac{2\pi}a, & \lvert a \rvert > 1 \end{cases}
\end{aligned}$$

[Integrate](integral.md) the both sides with respect to $a$ to get:

$$\begin{aligned}
f(a) & = \begin{cases} C_1, & \lvert a \rvert < 1 \\
2\pi \ln(-a) + C_2, & a < -1 \\
2\pi \ln a + C_3, & a > 1 \end{cases} \\
& = \begin{cases} C_1, & \lvert a \rvert < 1 \\
2\pi \ln \lvert a \rvert + C_2, & \lvert a \rvert > 1 \end{cases} && (f(a) \text{ is even})
\end{aligned}$$

$C_1 = 0$ follows from evaluating $f(0)$:

$$\begin{aligned}
f(0) & = C_1 \\
C_1 & = \int_0^\pi\! \ln\left(1 - 2(0) \cos x + 0^2\right) \,\mathrm{d}x \\
& = \int_0^\pi\! 0 \,\mathrm{d}x \\
& = 0
\end{aligned}$$

For $C_2$, we need to evaluate $f(a)$ for some $\lvert a \rvert > 1$, which is inconvenient to evaluate. Instead, we can reuse our existing results above using the properties of the [natural logarithm](natural%20logarithm.md) $\ln$:

$$\begin{aligned}
f(a) & = 2\pi \ln \lvert a \rvert + C_2 && (\lvert a \rvert > 1) \\
2\pi \lvert a \rvert + C_2 & = \int_0^\pi\! \ln\left(1 - 2a \cos{x} + a^2\right) \,\mathrm{d}x \\
& = \int_0^\pi\! \ln\left(\left(\frac1a\right)^2 - 2 \left(\frac1a\right) \cos x + 1\right) \,\mathrm{d}x + \int_0^\pi\! \ln a^2 \,\mathrm{d}x \\
& = f\left(\frac1a\right) + 2 \int_0^\pi\! \ln \lvert a \rvert \,\mathrm{d}x \\
& = 0 + 2\pi \ln \lvert a \rvert && \left( \left\lvert \frac1a \right\rvert < 1 \implies f\left(\frac1a\right) = 0 \right) \\
C_2 & = 0
\end{aligned}$$

The definition of $f(a)$ is complete except when $\lvert a \rvert = 1$:

$$f(a) = \begin{cases} 0, & \lvert a \rvert < 1 \\
2\pi \ln \lvert a \rvert, & \lvert a \rvert > 1 \end{cases}$$

Directly evaluating $f(1)$ and $f(-1)$ is possible with some difficulty:

$$\begin{aligned}
f(1) & = \int_0^\pi\! \ln\left(1 - 2 (1) \cos x + 1^2\right) \,\mathrm{d}x \\
& = \int_0^\pi\! \ln(2 - 2\cos x) \,\mathrm{d}x \\
& = \pi \ln2 + \int_0^\pi\! \ln(1 - \cos x) \,\mathrm{d}x \\
& = \pi \ln 2 +  \int_0^\pi \ln\left(1 - 1 + 2 \sin^2 \frac{x}2 \right) \,\mathrm{d}x \\
& = 2 \pi\ln2 + 2 \int_0^\pi\! \ln \left\lvert \sin \frac{x}2 \right\rvert \,\mathrm{d}x \\
& = 2 \pi\ln2 + 4 \int_0^{\frac\pi2}\! \ln \lvert \sin x \rvert \,\mathrm{d}x && (\text{substitution}) \\
\int_0^{\frac\pi2}\! \ln \lvert \sin x \rvert \,\mathrm{d}x & = \int_0^{\frac\pi2}\! \ln \lvert \cos x \rvert \,\mathrm{d}x && (\text{by symmetry}) \\
2 \int_0^{\frac\pi2}\! \ln \lvert \sin x \rvert \,\mathrm{d}x & = \int_0^{\frac\pi2}\! \ln \lvert \sin x \cos x \rvert \,\mathrm{d}x \\
& = -\frac\pi2 \ln 2 + \int_0^{\frac\pi2}\! \ln \lvert \sin 2x \rvert \,\mathrm{d}x \\
& = -\frac\pi2 \ln 2 + \frac12 \int_0^\pi\! \ln \lvert \sin x \rvert \,\mathrm{d}x && (\text{substitution}) \\
& = -\frac\pi2 \ln 2 + \int_0^{\frac\pi2}\! \ln \lvert \sin x \rvert \,\mathrm{d}x && (\text{by symmetry}) \\
\int_0^{\frac\pi2}\! \ln \lvert \sin x \rvert \,\mathrm{d}x & = -\frac\pi2 \ln 2 \\
f(1) & = 2\pi \ln 2 + 4 \left(-\frac\pi2 \ln 2\right) \\
& = 0 \\
f(-1) & = f(1) && (f(a) \text{ is even}) \\
& = 0
\end{aligned}$$

Finally:

$$f(a) = \begin{cases} 0, & \lvert a \rvert \le 1 \\
2\pi \ln \lvert a \rvert, & \lvert a \rvert > 1 \end{cases}$$

Directly integrating the integral is very difficult and will result in a very long expression, so using the Leibniz integral rule simplifies the evaluation significantly.

> [!tip] tips
>
> - takeaway ::@:: The Leibniz integral rule can turn [integrands](integrand.md) with the [natural logarithm](natural%20logarithm) $\ln$ into [fractions](fraction.md), which may be much easier to evaluate. Also, considering the [evenness](even%20and%20odd%20functions.md), [oddness](even%20and%20odd%20functions.md), and [symmetries](symmetry.md) of [functions](function%20(mathematics).md) helps a lot when evaluating integrals. <!--SR:!2025-08-18,393,308!2026-01-30,479,324-->

#### example 4: Green's theorem

Consider:

$\int_0^{2\pi}\! \sin \theta \cos(\sin \theta) \,\mathrm{d}\theta$

The above [integral](integral.md) has no [antiderivative](antiderivative.md) in terms of [elementary functions](elementary%20function.md). Introduce a new variable $a$ to parameterize the integral as:

$$f(a) = \int_0^{2\pi} a \sin \theta \cos (a \sin \theta) \,\mathrm{d}\theta$$

When $a = 1$, this is the original [integral](integral.md). Now we [differentiate](derivative.md) the parameterized integral with respect to $a$ using the Leibniz integral rule:

$$\begin{aligned}
\frac{\mathrm{d} }{\mathrm{d}a} f(a) & = \frac{\mathrm{d} }{\mathrm{d}a} \int_0^{2\pi} a \sin \theta \cos (a \sin \theta) \,\mathrm{d}\theta \\
& = \int_0^{2\pi} \frac{\partial}{\partial a} a \sin \theta \cos (a \sin \theta) \,\mathrm{d}\theta \\
& = \int_0^{2\pi}\! (a \cos \theta \cos(a \sin \theta) - a \sin \theta \cos \theta \sin(a \sin \theta)) \,\mathrm{d}\theta
\end{aligned}$$

Now, define a [vector field](vector%20field.md) on $\mathbb{R}^2$ by $\vec{F}(x, y) = (F_x(x, y), F_y(x, y)) = (a x \sin(a y),a \cos(a y))$. Furthermore, parameterize the [unit circle](unit%20circle.md) $S^1$ on $\mathbb{R}$ from $\theta$ by going around the circle in [counterclockwise orientation](curve%20orientation.md), given by $\vec{r}: [0, 2\pi] \to \mathbb{R}^2, \vec{r}(\theta) := (\cos \theta, \sin \theta)$. Then the [derivative](derivative.md) of the curve with respect to $\theta$ is $\dot{\vec{r} }(\theta) = (-\sin \theta, \cos \theta)$. Then we can convert the above integral into a [line integral](line%20integral.md) around a [simple closed curve](Jordan%20curve%20theorem.md):

$$\begin{aligned}
\frac{\mathrm{d} }{\mathrm{d}a} f(a) & = \int_0^{2\pi}\! (a \cos \theta \cos(a \sin \theta) - a \sin \theta \cos \theta \sin(a \sin \theta)) \,\mathrm{d}\theta \\
& = \int_0^{2\pi}\! (a \cos \theta \sin (a \sin \theta), a \cos(a \sin \theta)) \cdot (-\sin \theta, \cos \theta) \,\mathrm{d}\theta \\
& = \int_0^{2\pi} \vec{F}(\cos \theta, \sin \theta) \cdot \dot{\vec{r} }(\theta) \,\mathrm{d}\theta \\
& = \int_0^{2\pi} \vec{F}(\vec{r}(\theta)) \cdot \dot{\vec{r} }(\theta) \,\mathrm{d}\theta \\
& = \oint_{S^1}\! \vec{F}(\vec{r}) \cdot \,\mathrm{d}\vec{r} \\
& = \oint_{S^1}\! \left(F_x \,\mathrm{d}x + F_y \,\mathrm{d}y\right)
\end{aligned}$$

By [Green's theorem](Green's%20theorem.md), this equals the following [double integral](multiple%20integral.md) integrated over the [closed unit disk](unit%20disk.md) $\bar{D}_1$:

$$\begin{aligned}
\frac{\mathrm{d} }{\mathrm{d}a} f(a) & = \oint_{S^1}\! \left(F_x \,\mathrm{d}x + F_y \,\mathrm{d}y\right) \\
& = \iint_{\bar{D}_1}\! \left(\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}\right) \,\mathrm{d}A && (\text{Green's theorem}) \\
& = \iint_{\bar{D}_1}\! \left(0 - a^2 x \cos(ay) \right) \,\mathrm{d}A \\
& = -a^2 \iint_{\bar{D}_1}\! x \cos(ay) \,\mathrm{d}A \\
& = -a^2 \int_{-1}^1\! x \int_{-\sqrt{1 - x^2} }^{\sqrt{1 - x^2} }\! \cos(ay) \,\mathrm{d}y \,\mathrm{d}x \\
& = -a^2 \int_{-1}^1\! x \left[\frac1a \sin(ay)\right]_{y = -\sqrt{1 - x^2} }^{y = \sqrt{1 - x^2} } \,\mathrm{d}x \\
& = -2a \int_{-1}^1\! x \sin\left(a\sqrt{1 - x^2}\right) \,\mathrm{d}x \\
& = -2a \left(\int_{-1}^0\! x \sin\left(a\sqrt{1 - x^2}\right) \,\mathrm{d}x + \int_0^1\! x \sin\left(a\sqrt{1 - x^2}\right) \,\mathrm{d}x\right) \\
& = -2a \left(\int_1^0\! x \sin\left(a\sqrt{1 - x^2}\right) \,\mathrm{d}x + \int_0^1\! x \sin\left(a\sqrt{1 - x^2}\right) \,\mathrm{d}x\right) \\
& = 0
\end{aligned}$$

As the [derivative](derivative.md) of $f(a)$ with respect to $a$ is 0, $f(a)$ is a [constant function](constant%20function.md):

$$f(a) = \int 0 \,\mathrm{d}a = C$$

We can find that $C = 0$ by evaluating $f(a)$ at any point, and $a = 0$ is the most convenient to evaluate:

$$C = f(0) = \int_0^{2\pi} 0 \sin \theta \cos (0 \sin \theta) \,\mathrm{d}\theta = \int_0^{2\pi} 0 \,\mathrm{d}\theta = 0$$

Finally:

$$\int_0^{2\pi}\! \sin \theta \cos(\sin \theta) \,\mathrm{d}\theta = f(1) = C = 0$$

One may check that the [integral](integral.md) is indeed zero by considering the [symmetry](symmetry.md) of $\sin \theta$ from $0$ to $2 \pi$.

> [!tip] tips
>
> - takeaway ::@:: Advanced [integration](integral.md) techniques like [Green's theorem](Green's%20theorem.md) can be used in conjunction with the Leibniz integral rule. <!--SR:!2026-05-22,611,324!2025-02-22,267,344-->

#### other problems to solve

- integral 1: $\int _0 ^1 \! \frac {x - 1} {\ln x} \, \mathrm{d}x$ :@: $\int _0 ^1 \! \frac {x^a - 1} {\ln x} \, \mathrm{d}x$ <!--SR:!2025-03-14,113,312-->
- integral 2: $\int _0 ^{\frac \pi 2} \! \frac x {\tan x} \,\mathrm{d}x$ :@: $\int _0 ^{\frac \pi 2} \! \frac {\arctan (a \tan x)} {\tan x} \,\mathrm{d}x$ <!--SR:!2025-01-21,35,208-->
- integral 3: $\int _0 ^\infty \! \frac {\ln \left(1 + x^2\right)} {1 + x^2} \,\mathrm{d}x$ :@: $\int _0 ^\infty \! \frac {\ln \left(1 + a^2 x^2\right)} {1 + x^2} \,\mathrm{d}x$ <!--SR:!2025-07-08,264,268-->
- integral 4: $\int _0 ^1 \! (x \ln x)^n \,\mathrm{d}x \quad n \in \mathbb{N}_{\ge 0}$ :@: $\int _0 ^1 \! x^a (\ln x)^n \,\mathrm{d}x \quad n \in \mathbb{N}_{\ge 0}$ <!--SR:!2025-07-25,363,319-->
- [Dirichlet integral](Dirichlet%20integral.md): $\int _0 ^\infty \! \frac {\sin x} x \,\mathrm{d}x$ :@: $\int _0 ^\infty \! e^{-ax} \frac {\sin x} x \,\mathrm{d}x$ <!--SR:!2026-10-18,723,324-->

> [!info]- proof for integral 1
>
> $$\begin{aligned}
> f(a) & = \int _0 ^1 \! \frac {x^a - 1} {\ln x} \,\mathrm{d}x \\
> f'(a) & = \int _0 ^1 \! \frac \partial {\partial a} \frac {x^a - 1} {\ln x} \,\mathrm{d}x \\
> & = \int _0 ^1 \! \frac{(\ln x) x^a}{\ln x} \,\mathrm{d}x \\
> & = \int _0 ^1 \! x^a \,\mathrm{d}x \\
> & = \frac 1 {a + 1} \left[ x^{a + 1} \right] _{x = 0} ^{x = 1} \\
> & = \frac 1 {a + 1} \\
> f(a) & = \int ^a \! \frac 1 {\xi + 1} \,\mathrm{d}\xi \\
> & = \ln (a + 1) + C \\
> f(0) & = \ln(0 + 1) + C \\
> C & = \int _0 ^1 \! \frac {x^0 - 1} {\ln x} \,\mathrm{d}x \\
> & = \int _0 ^1 \! 0 \,\mathrm{d}x \\
> & = 0 \\
> f(a) & = \ln (a + 1) \\
> f(1) & = \ln (1 + 1) \\
> \int _0 ^1 \! \frac {x - 1} {\ln x} \,\mathrm{d}x & = \ln 2
> \end{aligned}$$

<!-- markdownlint MD028 -->

> [!info]- proof for integral 2
>
> $$\begin{aligned}
> f(a) & = \int _0 ^{\frac \pi 2} \! \frac {\arctan (a \tan x)} {\tan x} \,\mathrm{d}x \\
> f'(a) & = \int _0 ^{\frac \pi 2} \! \frac \partial {\partial a} \frac {\arctan (a \tan x)} {\tan x} \,\mathrm{d}x \\
> & = \int _0 ^{\frac \pi 2} \! \frac {\tan x} {\left( (a \tan x)^2 + 1 \right) \tan x} \,\mathrm{d}x \\
> & = \int _0 ^{\frac \pi 2} \! \frac 1 {a^2 \tan^2 x + 1} \, \mathrm{d}x \\
> & = \int _0 ^{\frac \pi 2} \! \frac {\sec^2 x} {\left( \tan^2 x + 1 \right) \left( a^2 \tan^2 x + 1 \right)} \,\mathrm{d}x \\
> & = \int _0 ^\infty \! \frac 1 {\left(x^2 + 1\right) \left(a^2 x^2 + 1\right)} \,\mathrm{d}x && (\text{change of variables } \tan x \mapsto x) \\
> & = \frac 1 {1 - a^2} \int _0 ^\infty \! \left( \frac 1 {x^2 + 1} - \frac {a^2} {a^2 x^2 + 1} \right) \,\mathrm{d}x \\
> & = \frac 1 {1 - a^2} [\arctan x - a \arctan ax] _{x = 0} ^{x = \infty} \\
> & = \frac 1 {1 - a^2} (1 - a) \frac \pi 2 && (\text{assume } a \ge 0) \\
> & = \frac \pi 2 \frac 1 {a + 1} \\
> f(a) & = \frac \pi 2 \int ^a \! \frac 1 {\xi + 1} \,\mathrm{d}\xi \\
> & = \frac \pi 2 \ln \lvert a + 1 \rvert + C \\
> f(0) & = \frac \pi 2 \ln \lvert 0 + 1 \rvert + C \\
> C & = \int _0 ^{\frac \pi 2} \! \frac {\arctan (0 \tan x)} {\tan x} \,\mathrm{d}x \\
> & = \int _0 ^{\frac \pi 2} \! 0 \,\mathrm{d}x \\
> & = 0 \\
> f(a) & = \frac \pi 2 \ln \lvert a + 1 \rvert \\
> f(1) & = \frac \pi 2 \ln \lvert 1 + 1 \rvert \\
> \int _0 ^{\frac \pi 2} \! \frac x {\tan x} \,\mathrm{d}x & = \frac \pi 2 \ln 2
> \end{aligned}$$

<!-- markdownlint MD028 -->

> [!info]- proof for integral 3
>
> $$\begin{aligned}
> f(a) & = \int _0 ^\infty \! \frac{\ln \left(1 + a^2 x^2\right)} {1 + x^2} \,\mathrm{d}x \\
> f'(a) & = \int _0 ^\infty \! \frac \partial {\partial a} \frac{\ln \left(1 + a^2 x^2\right)} {1 + x^2} \,\mathrm{d}x \\
> & = \int _0 ^\infty \! \frac {2ax^2} {\left(1 + a^2 x^2\right) \left(1 + x^2\right)} \,\mathrm{d}x \\
> & = \frac {2a} {a^2 - 1} \int _0 ^\infty \! \left( \frac 1 {1 + x^2} - \frac 1 {1 + a^2 x^2} \right) \,\mathrm{d}x \\
> & = \frac {2a} {a^2 - 1} \left[ \arctan x - \frac 1 a \arctan ax \right] _0 ^\infty \\
> & = \frac {2a} {a^2 - 1} \frac \pi 2 \left(1 - \frac 1 a\right) && (\text{assume } a \ge 0) \\
> & = \pi \frac {a} {(a + 1) (a - 1)} \frac {a - 1} a \\
> & = \pi \frac 1 {a + 1} \\
> f(a) & = \pi \int ^a \! \frac 1 {\xi + 1} \,\mathrm{d}\xi \\
> & = \pi \ln \lvert a + 1 \rvert + C \\
> f(0) & = \pi \ln \lvert 0 + 1 \rvert + C \\
> C & = \int _0 ^\infty \! \frac {\ln \left(1 + 0^2 x^2\right)} {1 + x^2} \,\mathrm{d}x \\
> & = \int _0 ^\infty \! 0 \,\mathrm{d}x \\
> & = 0 \\
> f(a) & = \pi \ln \lvert a + 1 \rvert \\
> f(1) & = \pi \ln \lvert 1 + 1 \rvert \\
> \int _0 ^\infty \! \frac {\ln \left(1 + x^2\right)} {1 + x^2} \,\mathrm{d}x & = \pi \ln 2
> \end{aligned}$$

<!-- markdownlint MD028 -->

> [!info]- proof for integral 4
>
> $$\begin{aligned}
> f(a) & = \int _0 ^1 \! x^a (\ln x)^n \,\mathrm{d}x && n \in \mathbb{N}_{\ge 0} \\
> & = \frac {\mathrm{d}^n} {\mathrm{d}a^n} \int _0 ^1 \! x^a \,\mathrm{d}x \\
> & = \frac {\mathrm{d}^n} {\mathrm{d}a^n} \left[ \frac {x^{a + 1} } {a + 1} \right]_{x = 0}^{x = 1} \\
> & = \frac {\mathrm{d}^n} {\mathrm{d}a^n} \frac 1 {a + 1} \\
> & = \frac {\mathrm{d}^{n - 1} } {\mathrm{d}a^{n - 1} } \frac {-1} {(a + 1)^2} \\
> & = \frac {\mathrm{d}^{n - 2} } {\mathrm{d}a^{n - 2} } \frac {(-1)(-2)} {(a + 1)^3} \\
> & = \frac{(-1)^n n!}{(a + 1)^{n + 1} } \\
> f(n) & = \frac {(-1)^n n!} {(n + 1)^{n + 1} } \\
> \int _0 ^1 \! (x \ln x)^n \,\mathrm{d}x & = \frac {(-1)^n n!} {(n + 1)^{n + 1} } \quad n \in \mathbb{N}_{\ge 0}
> \end{aligned}$$

<!-- markdownlint MD028 -->

> [!info]- proof for the [Dirichlet integral](Dirichlet%20integral.md)
>
> To solve the [Dirichlet integral](Dirichlet%20integral.md):
>
> $$\int_0^\infty\! \frac{\sin x}x \,\mathrm{d}x$$
>
> Define:
>
> $$f(a) := \int_0^\infty\! e^{-ax} \frac{\sin x}x \,\mathrm{d}x$$
>
> When $a = 0$, the integral is [conditionally convergent](conditional%20convergence.md), so it is not [Lebesgue integrable](Lebesgue%20integration.md), and the conditions of [Leibniz integral rule § measure theory statement](#measure%20theory%20statement) are not satisfied. Assuming $a > 0$ so that the integral is Lebesgue integrable for applying the Leibniz integral rule:
>
> $$\begin{aligned}
> f(a) & = \int_0^\infty e^{-ax} \frac{\sin x}x \,\mathrm{d}x \\
> f'(a) & = -\int_0^\infty e^{-ax} \sin x \,\mathrm{d}x \\
> & = -\left[-e^{-ax} \cos x\right]_0^\infty + a \int_0^\infty e^{-ax} \cos x \,\mathrm{d}x \\
> & = \left[e^{-ax} \cos x\right]_0^\infty + a \left[e^{-ax} \sin x\right]_0^\infty + a^2 \int_0^\infty e^{-ax} \sin x \,\mathrm{d}x \\
> & = \left[e^{-ax} \cos x\right]_0^\infty + a \left[e^{-ax} \sin x\right]_0^\infty - a^2 f'(a) \\
> & = \frac{\left[e^{-ax} \cos x\right]_0^\infty + a \left[e^{-ax} \sin x\right]_0^\infty}{1 + a^2} \\
> & = \frac{(0 - 1)+a(0 - 0)}{1 + a^2} \\
> & = -\frac{1}{1 + a^2} \\
> f(a) & = \int\! f'(\xi) \,\mathrm{d}\xi \\
> & = -\int\! \frac{1}{1 + \xi^2} \,\mathrm{d}\xi \\
> & = - \arctan a + C
> \end{aligned}$$
>
> Find $C$ by taking the [limit](limit%20of%20a%20function.md) at $\infty$:
>
> $$\begin{aligned}
> \lim_{a \to \infty} \lvert f(a) \rvert & = \lim_{a \to 0} \left\lvert \int_0^\infty e^{-ax} \frac{\sin x}x \,\mathrm{d}x \right\rvert \\
> & \le \lim_{a \to \infty} \int_0^\infty \left\lvert e^{-ax} \frac{\sin x}x \right\rvert \,\mathrm{d}x \\
> &= \lim_{a \to \infty} \int_0^\infty e^{-ax} \left\lvert \frac{\sin x}x \right\rvert \,\mathrm{d}x && \left(e^{-ax} \ge 0 \right) \\
> & \le \lim_{a \to \infty} \int_0^\infty e^{-ax} \,\mathrm{d}x && \left(\left\lvert \frac{\sin x}x \right\rvert \le 1\right) \\
> & = -\lim_{a \to \infty} \frac1a \left[e^{-ax}\right]_{x = 0}^{x = \infty} \\
> & = \lim_{a \to \infty} \frac1a \\
> & = 0 \\
> \lim_{a \to \infty} \lvert f(a) \rvert & = 0 && (0 \le \lvert f(a) \rvert \le 0) \\
> \lim_{a \to \infty} f(a) & = 0 \\
> \lim_{a \to \infty} (- \arctan a + C) & = 0\\
> -\frac\pi2 + C & = 0 \\
> C & = \frac\pi2
> \end{aligned}$$
>
> Hence:
>
> $$f(a) = -\arctan a + \frac\pi2 \qquad a > 0$$
>
> Now we need to prove that the original integral we want to solve equals $\lim_{a \to 0^+} f(a)$ to use the above expression. This is because even though $f(0)$ is the original integral by definition, $f(0) \not\equiv \lim_{a \to 0^+} f(a)$. We show that the original integral equals a [convergent](convergent%20series.md) integral:
>
> $$\begin{aligned}
> \int_0^\infty\! \frac{\sin x}x \,\mathrm{d}x & = \int_0^\infty\! \frac{\sin \frac{x}2 \cos \frac{x}2}{\frac{x}2} \,\mathrm{d}x \\
> & = 2 \int_0^\infty\! \frac{\sin x \cos x}{x} \,\mathrm{d}x && \left( \text{change of variables } \frac{x}2 \mapsto x \right) \\
> & = 2 \int_{x = 0}^{x = \infty} \frac{\sin x}x \,\mathrm{d}(\sin x) && (\text{substitution}) \\
> & = 2\left[ \frac{\sin^2 x}x \right]_{x = 0}^{x = \infty} - 2\int_{x = 0}^{x = \infty}\! \sin x \,\mathrm{d}\!\left(\frac{\sin x}x\right) && (\text{integration by parts}) \\
> & = - 2\int_0^\infty\! \frac{\sin x(x \cos x - \sin x)}{x^2} \,\mathrm{d}x \\
> & = - 2\int_0^\infty\! \frac{\sin x \cos x}x \,\mathrm{d}x + 2\int_0^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x \\
> & = -\int_0^\infty\! \frac{\sin x}x \,\mathrm{d}x + 2 \int_0^\infty \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x \\
> & = \int_0^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x
> \end{aligned}$$
>
> The resulting [integral](integral.md) is [absolutely convergent](absolute%20convergence.md). We can perform the same operation on $f(a)$:
>
> $$\begin{aligned}
> f(a) & = \int_0^\infty\! e^{-ax} \frac{\sin x}x \,\mathrm{d}x \\
> & = \int_0^\infty\! e^{-ax} \frac{\sin \frac{x}2 \cos \frac{x}2}{\frac{x}2} \,\mathrm{d}x \\
> & = 2 \int_0^\infty\! e^{-2ax} \frac{\sin x \cos x}x \,\mathrm{d}x && \left( \text{change of variables } \frac{x}2 \mapsto x \right) \\
> & = 2 \int_{x = 0}^{x = \infty}\! e^{-2ax} \frac{\sin x}x \,\mathrm{d}(\sin x) && (\text{substitution}) \\
> & = 2 \left[ e^{-2ax} \frac{\sin^2 x}x \right]_0^\infty - 2 \int_{x = 0}^{x = \infty}\! \sin x \,\mathrm{d}\!\left(e^{-2ax} \frac{\sin x}x\right) && (\text{integration by parts}) \\
> & = -2 \int_0^\infty\! \frac{\sin x \left(-2a e^{-2ax} x \sin x + e^{-2ax} x \cos x - e^{-2ax} \sin x\right)}{x^2} \,\mathrm{d}x \\
> & = 4a \int_0^\infty\! e^{-2ax} \frac{\sin^2 x}x \,\mathrm{d}x - 2 \int_0^\infty\! e^{-2ax} \frac{\sin x \cos x}{x} \,\mathrm{d}x + 2 \int_0^\infty e^{-2ax} \left( \frac{\sin x}x \right)^2 \,\mathrm{d}x \\
> & = - f(a) + 4a \int_0^\infty\! e^{-2ax} \frac{\sin^2 x}x \,\mathrm{d}x + 2 \int_0^\infty e^{-2ax} \left( \frac{\sin x}x \right)^2 \,\mathrm{d}x \\
> & = 2a \int_0^\infty\! e^{-2ax} \frac{\sin^2 x}x \,\mathrm{d}x + \int_0^\infty e^{-2ax} \left( \frac{\sin x}x \right)^2 \,\mathrm{d}x
> \end{aligned}$$
>
> The resulting [integrals](integral.md) are [convergent](convergent%20series.md). Now we take the right-sided [limit](limit%20of%20a%20function.md) of the above result at $0$ to show that it equals our original integral to be solved:
>
> $$\begin{aligned}
> \lim_{a \to 0^+} f(a) & = \lim_{a \to 0^+} \left( 2a \int_0^\infty\! e^{-2ax} \frac{\sin^2 x}x \,\mathrm{d}x + \int_0^\infty\! e^{-2ax} \left( \frac{\sin x}x \right)^2 \,\mathrm{d}x \right) \\
> & = \lim_{a \to 0^+} \left( 2a \int_0^\infty\! e^{-2x} \frac{\sin^2 \frac x a}x \,\mathrm{d}x + \int_0^\infty\! e^{-2ax} \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x \right) && (\text{change of variables } \lvert a \rvert x \mapsto x) \\
> & = \lim_{a \to 0^+} 2a \int_0^\infty\! e^{-2x} \frac{\sin^2 \frac x a}x \,\mathrm{d}x + \lim_{a \to 0^+} \int_0^\infty\! e^{-2ax} \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x && (\text{both integrals are convergent})
> \end{aligned}$$
>
> Evaluate the [limits](limit%20of%20a%20function.md) of two [integrals](integral.md) separately. For the first integral, it equals zero as $a \to 0^+$:
>
> $$\begin{aligned}
> 0 \le \left\lvert 2a \int_0^\infty\! e^{-2x} \frac{\sin^2 \frac x a}x \,\mathrm{d}x \right\rvert & = 2a \int_0^\infty\! \left\lvert e^{-2x} \frac{\sin^2 \frac{x}a}{x} \right\rvert \,\mathrm{d}x && (\text{assuming } a > 0) \\
> & = 2a \int_0^\infty\! e^{-2x} \frac{\sin^2 \frac{x}a}{x} \,\mathrm{d}x \\
> & = 2a \left(\int_0^a\! e^{-2x} \frac{\sin^2 \frac x a}{x} \,\mathrm{d}x + \int_a^1\! e^{-2x} \frac{\sin^2 \frac x a}{x} \,\mathrm{d}x + \int_1^\infty\! e^{-2x} \frac{\sin^2 \frac x a}{x} \,\mathrm{d}x \right) \\
> & \le 2a \left(\int_0^a\! \frac{\frac {x^2} {a^2} }{x} \,\mathrm{d}x + \int_a^1\! \frac{1}{x} \,\mathrm{d}x + \int_1^\infty\! e^{-2x} \,\mathrm{d}x \right) && (\text{replace integrands with larger integrands}) \\
> & = 2a \left(\frac12 - \ln a + \frac1{2 e^2} \right) \\
> 0 \le \lim_{a \to 0^+} \left\lvert 2a \int_0^\infty\! e^{-2x} \frac{\sin^2 \frac x a}x \,\mathrm{d}x \right\rvert & \le \lim_{a \to 0^+} 2a \left(\frac12 - \ln a + \frac1{2 e^2} \right) \\
> & = 0 \\
> \lim_{a \to 0^+} \left\lvert 2a \int_0^\infty\! e^{-2x} \frac{\sin^2 \frac x a}x \,\mathrm{d}x \right\rvert & = 0 \\
> \lim_{a \to 0^+} 2a \int_0^\infty\! e^{-2x} \frac{\sin^2 \frac x a}x \,\mathrm{d}x & = 0
> \end{aligned}$$
>
> For the second [integral](integral.md), we will prove that it equals $\int_0^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x$ as $a \to 0^+$ by the [dominated convergence theorem](dominated%20convergence%20theorem.md):
>
> $$\begin{aligned}
> \lim_{a \to 0^+} \int_0^\infty e^{-2ax} \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x & = \int_0^\infty \lim_{a \to 0^+} e^{-2ax} \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x && \left( \text{the integrand is dominated by } \left(\frac{\sin x}x\right)^2 \text{ on } (0, \infty) \text{ when } a > 0 \right) \\
> & = \int_0^\infty \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x
> \end{aligned}$$
>
> Alternatively, manipulate the second [integral](integral.md) algebraically:
>
> $$\begin{aligned}
> 0 \le \int_0^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x - \int_0^\infty\! e^{-2ax} \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x & = \int_0^\infty\! \left(1 - e^{-2ax}\right) \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x \\
> & = \int_0^{\frac1{\sqrt a} }\! \left(1 - e^{-2ax}\right) \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x + \int_{\frac1{\sqrt a} }^\infty\! \left(1 - e^{-2ax}\right) \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x \\
> & \le \int_0^{\frac1{\sqrt a} }\! \left(1 - e^{-2a \frac1{\sqrt a} }\right) \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x + \int_{\frac1{\sqrt a} }^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x && (\text{replace integrands with larger integrands, assuming } a > 0) \\
> & = \left(1 - e^{-2\sqrt a}\right) \int_0^{\frac1{\sqrt a} }\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x + \int_{\frac1{\sqrt a} }^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x \\
> 0 \le \lim_{a \to 0^+} \left( \int_0^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x - \int_0^\infty\! e^{-2ax} \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x \right) & \le \lim_{a \to 0^+} \left( \left(1 - e^{-2\sqrt a}\right) \int_0^{\frac1{\sqrt a} }\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x + \int_{\frac1{\sqrt a} }^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x \right) \\
> & = 0 + 0 && \left(\int_0^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x \text{ is convergent}\right) \\
> & = 0 \\
> \lim_{a \to 0^+} \left( \int_0^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x - \int_0^\infty\! e^{-2ax} \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x \right) & = 0 \\
> \lim_{a \to 0^+} \int_0^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x - \lim_{a \to 0^+} \int_0^\infty\! e^{-2ax} \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x & = 0 && (\text{both integrals are convergent}) \\
> \lim_{a \to 0^+} \int_0^\infty\! e^{-2ax} \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x & = \int_0^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x
> \end{aligned}$$
>
> Hence, add the above results to produce another expression for $f(a)$ as $a \to 0^+$:
>
> $$\lim_{a \to 0^+} f(a) = \int_0^\infty \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x$$
>
> Finally, evaluate the [limit](limit%20of%20a%20function.md) of $f(a)$ as $a \to 0^+$, equating both expressions of $f(a)$:
>
> $$\begin{aligned}
> \lim_{a \to 0^+} f(a) & = \lim_{a \to 0^+} f(a) \\
> \lim_{a \to 0^+} \left(-\arctan a + \frac\pi2\right) & = \int_0^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x \\
> \int_0^\infty\! \left(\frac{\sin x}x\right)^2 \,\mathrm{d}x & = \frac\pi2 \\
> \int_0^\infty\! \frac{\sin x}x \,\mathrm{d}x & = \frac\pi2
> \end{aligned}$$

<!-- markdownlint MD028 -->

> [!tip] tips
>
> - takeaway ::@:: The Leibniz integral rule can be used to simplify integrands, though be aware of the conditions. Also, [inequalities](inequality%20(mathematics).md) can be used to evaluate [integrals](integral.md) with [limits](limit%20of%20a%20function.md). <!--SR:!2025-02-02,252,288!2025-07-20,392,364-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Leibniz_integral_rule) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
