---
aliases:
  - auxiliary equation
  - auxiliary equations
  - characteristic equation
  - characteristic equation (calculus)
  - characteristic equations
tags:
  - flashcard/active/general/eng/characteristic_equation__calculus_
  - language/in/English
---

# characteristic equation (calculus)

In [mathematics](mathematics.md), the __characteristic equation__ or __auxiliary equation__ is {@{a $n$-th [degree](degree%20of%20a%20polynomial.md) [polynomial equation](algebraic%20equation.md) based on the general solution of a $n$-th [order](differential%20equation.md#equation%20order%20and%20degree) [differential equation](differential%20equation.md) or [difference equation](recurrence%20relation.md)}@}. A linear, homogeneous [ordinary differential equation](ordinary%20differential%20equation.md) {@{with constant coefficients (function coefficients do not work) $a_n,a_{n-1},\ldots,a_1,a_0$ and $y$ as the [dependent variable](dependent%20and%20independent%20variable.md) $$a_ny^{(n)}+a_{n-1}y^{(n-1)}+\cdots+a_1y'+a_0y=0$$ has a characteristic equation $$a_nr^n+a_{n-1}r^{n-1}+\cdots+a_1r+a_0=0$$}@}. This is a specific case of {@{applying the [Laplace transform](Laplace%20transform.md) where $r$ is in $s$-domain}@}. <!--SR:!2028-07-23,1236,310!2026-07-30,586,250!2025-07-26,203,327-->

> [!tip] tips
>
> - reason the [coefficients](coefficient.md) needs to be [constants](constant%20(mathematics).md) ::@:: The method assumes the solution is in the form of $y(x) = e^{rx}$, and when [differentiating](derivative.md) $y(x)$, the $r$ is assumed to be a constant. Any [functions](function%20(mathematics).md) of $x$ in the [coefficients](coefficient.md) would make the found $r$ dependent on $x$, making $r$ no longer a [constant](constant%20(mathematics).md). <!--SR:!2025-03-13,344,354!2028-08-03,1243,361-->

## formation of the general solution

After finding the [roots](zero%20of%20a%20function.md) of the characteristic equation, {@{the general solution to the [differential equation](differential%20equation.md) can be formed from the roots}@}. Given {@{there are $n$ roots (regardless of whether it is [repeated](multiplicity%20(mathematics).md#multiplicity%20of%20a%20root%20of%20a%20polynomial.md) or [complex](complex%20number.md)) corresponding to $n$ solutions $y_1(x),y_2(x),\ldots,y_{n-1}(x),y_n(x)$}@}, by {@{the [superposition principle](superposition%20princple.md)}@}, the general solution is {@{$$y(x)=y_1(x)+y_2(x)+\cdots+y_{n-1}(x)+y_n(x)$$}@}. <!--SR:!2028-02-02,1187,350!2025-11-28,501,310!2026-04-03,427,367!2026-03-30,423,367-->

### distinct real roots

For a distinct real root $r_n$, its corresponding solution is {@{$$y_n(x)=c_ne^{r_nx}$$}@}. <!--SR:!2026-10-26,761,330-->

### repeated real roots

For a root $r$ of [multiplicity](multiplicity%20(mathematics).md#multiplicity%20of%20a%20root%20of%20a%20polynomial.md) $k$, its corresponding solution is {@{$$y_1(x)+y_2(x)+\cdots+y_{k}(x)=c_1e^{rx}+xc_2e^{rx}+\cdots+x^{k-1}c_ke^{rx}$$}@}. <!--SR:!2025-05-25,359,290-->

### complex roots

For complex roots, they always come in [complex conjugate](complex%20conjugate.md) $r_1=a+bi$ and $r_2=a-bi$ with [reals](real%20number.md) $a$ and $b$, their corresponding solutions are {@{$$y_1(x)+y_2(x)=c_1e^{(a+bi)x}+c_2e^{(a-bi)x}$$}@}. Using {@{[Euler's formula](Euler's%20formula.md), they can be transformed as follows: $$\begin{aligned}y_1(x)+y_2(x)&=c_1e^{(a+bi)x}+c_2e^{(a-bi)x}\\&=c_1e^{ax}(\cos{bx}+i\sin{bx})+c_2e^{ax}(\cos{bx}-i\sin{bx})\\&=(c_1+c_2)e^{ax}\cos{bx}+i(c_1-c_2)e^{ax}\sin{bx}\end{aligned}$$}@} <!--SR:!2027-03-27,797,290!2025-06-19,180,327-->

Since {@{$y(x)$ is [real-valued](real-valued%20function.md)}@}, {@{$c_1+c_2$ must be [real](real%20number.md) and $c_1-c_2$ must be [imaginary](imaginary%20number.md) so that $y_1(x)$ and $y_2(x)$ are both [real-valued](real-valued%20function.md)}@}. Therefore, {@{$c_1=\frac{C_1}2+i\frac{C_2}2$ and $c_2=\frac{C_1}2-i\frac{C_2}2$ are [complex conjugate](complex%20conjugate.md), where $C_1$ and $C_2$ are arbitrary [reals](real%20number.md)}@}. Putting $c_1$ and $c_2$ into the above solution, we {@{obtain a solution without [imaginaries](imaginary%20number.md): $$\begin{aligned}y_1(x)+y_2(x)&=(c_1+c_2)e^{ax}\cos{bx}+i(c_1-c_2)e^{ax}\sin{bx}\\&=C_1e^{ax}\cos{bx}+C_2e^{ax}\sin{b}x\end{aligned}$$}@} <!--SR:!2025-11-21,531,310!2026-03-29,422,367!2025-12-13,316,347!2026-04-01,425,367-->

If the complex roots are [repeated](multiplicity%20(mathematics).md#multiplicity%20of%20a%20root%20of%20a%20polynomial.md), {@{multiply it by powers of $x$ similar to [repeated real roots](#repeated%20real%20roots)}@}. <!--SR:!2027-09-03,1068,350-->

## see also

- [Laplace transform applied to differential equations](Laplace%20transform%20applied%20to%20differential%20equations.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/characteristic_equation_(calculus)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
