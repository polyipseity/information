---
aliases:
  - second partial derivative test
  - second partial derivative tests
tags:
  - flashcard/active/general/eng/second_partial_derivative_test
  - language/in/English
---

# second partial derivative test

> {@{![polynomial described by the Hessian at a maximum point](../../archives/Wikimedia%20Commons/Hessian%20at%20maximum%20point.gif)}@}
>
> {@{![polynomial described by the Hessian at a minimum point](../../archives/Wikimedia%20Commons/Hessian%20at%20minimum%20point.gif)}@}
>
> {@{![polynomial described by the Hessian at a saddle point](../../archives/Wikimedia%20Commons/Hessian%20at%20saddle%20point.gif)}@}
>
> The Hessian {@{approximates the function at a critical point with a second-degree polynomial}@}. <!--SR:!2025-04-06,15,290!2025-04-05,14,290!2025-04-06,15,290!2025-04-07,16,290-->

In {@{[mathematics](mathematics.md)}@}, {@{the __second partial derivative test__}@} is {@{a method in [multivariable calculus](multivariable%20calculus.md) used to determine if a [critical point](critical%20point%20(mathematics).md) of a function is a [local minimum](maxima%20and%20minima.md), maximum or [saddle point](saddle%20point.md)}@}. <!--SR:!2025-04-06,15,290!2025-04-06,15,290!2025-04-06,15,290-->

## functions of two variables

Suppose that {@{_f_\(_x_, _y_\) is a differentiable [real function](real%20function.md) of two variables whose second [partial derivatives](partial%20derivative.md) exist and are [continuous](continuous%20function.md)}@}. {@{The [Hessian matrix](Hessian%20matrix.md) _H_ of _f_}@} is {@{the 2 × 2 matrix of partial derivatives of _f_}@}: {@{$$H(x,y)={\begin{bmatrix}f_{xx}(x,y)&f_{xy}(x,y)\\f_{yx}(x,y)&f_{yy}(x,y)\end{bmatrix} }.$$}@} (annotation: Some definitions {@{may have this matrix transposed, but the results are equivalent for a $C_2$ function}@}.\) Define {@{_D_\(_x_, _y_\) to be the [determinant](determinant.md) $$D(x,y)=\det(H(x,y))=f_{xx}(x,y)f_{yy}(x,y)-\left(f_{xy}(x,y)\right)^{2}$$ of _H_}@}. Finally, suppose that {@{\(_a_, _b_\) is a critical point of _f_, that is, that _f_<sub>_x_</sub>\(_a_, _b_\) = _f_<sub>_y_</sub>\(_a_, _b_\) = 0}@}. Then {@{the second partial derivative test asserts the following}@}:<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-04-05,14,290!2025-04-07,16,290!2025-04-05,14,290!2025-04-06,15,290!2025-04-06,15,290!2025-04-07,16,290!2025-04-07,16,290!2025-04-06,15,290-->

1. If _D_\(_a_, _b_\) \> 0 and _f<sub>xx</sub>_\(_a_, _b_\) \> 0 ::@:: then \(_a_, _b_\) is a local minimum of _f_. <!--SR:!2025-04-06,15,290!2025-04-06,15,290-->
2. If _D_\(_a_, _b_\) \> 0 and _f<sub>xx</sub>_\(_a_, _b_\) \< 0 ::@:: then \(_a_, _b_\) is a local maximum of _f_. <!--SR:!2025-04-07,16,290!2025-04-06,15,290-->
3. If _D_\(_a_, _b_\) \< 0 ::@:: then \(_a_, _b_\) is a [saddle point](saddle%20point.md) of _f_. <!--SR:!2025-04-06,15,290!2025-04-05,14,290-->
4. If _D_\(_a_, _b_\) = 0 ::@:: then the point \(_a_, _b_\) could be any of a minimum, maximum, or saddle point \(that is, the test is inconclusive\). <!--SR:!2025-04-07,16,290!2025-04-05,14,290-->

Sometimes {@{other equivalent versions of the test are used}@}. In {@{cases 1 and 2}@}, {@{the requirement that _f<sub>xx</sub>_ _f<sub>yy</sub>_ − _f<sub>xy</sub>_<sup>2</sup> is positive at \(_x_, _y_\)}@} {@{implies that _f<sub>xx</sub>_ and _f<sub>yy</sub>_ have the same sign there}@}. Therefore, {@{the second condition, that _f<sub>xx</sub>_ be greater \(or less\) than zero}@}, could {@{equivalently be that _f<sub>yy</sub>_ or tr\(_H_\) = _f<sub>xx</sub>_ + _f<sub>yy</sub>_ be greater \(or less\) than zero at that point}@}. <!--SR:!2025-04-06,15,290!2025-04-05,14,290!2025-04-05,14,290!2025-04-06,15,290!2025-04-07,16,290!2025-04-06,15,290-->

{@{A condition implicit in the statement of the test}@} is that if {@{$f_{xx}=0$ or $f_{yy}=0$}@}, it {@{must be the case that $D(a,b)\leq 0$, and therefore only cases 3 or 4 are possible}@}. <!--SR:!2025-04-05,14,290!2025-04-07,16,290!2025-04-05,14,290-->

## functions of many variables

For {@{a function _f_ of three or more variables}@}, there is {@{a generalization of the rule shown above}@}. In this context, instead of {@{examining the determinant of the Hessian matrix}@}, one {@{must look at the [eigenvalues](eigenvalues%20and%20eigenvectors.md) of the Hessian matrix at the critical point}@}. The following test can be {@{applied at any critical point _a_ for which the Hessian matrix is [invertible](invertible%20matrix.md)}@}: <!--SR:!2025-04-07,16,290!2025-04-06,15,290!2025-04-07,16,290!2025-04-07,16,290!2025-04-06,15,290-->

1. If the Hessian is [positive definite](positive-definite%20matrix.md) \(equivalently, has all eigenvalues positive\) at _a_, ::@:: then _f_ attains a local minimum at _a_. <!--SR:!2025-04-07,16,290!2025-04-05,14,290-->
2. If the Hessian is negative definite \(equivalently, has all eigenvalues negative\) at _a_, ::@:: then _f_ attains a local maximum at _a_. <!--SR:!2025-04-05,14,290!2025-04-06,15,290-->
3. If the Hessian has both positive and negative eigenvalues ::@:: then _a_ is a saddle point for _f_ \(and in fact this is true even if _a_ is degenerate\). <!--SR:!2025-04-07,16,290!2025-04-05,14,290-->

In {@{those cases not listed above \(annotation: e.g. the Hessian matrix is not invertible\)}@}, {@{the test is inconclusive}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-04-06,15,290!2025-04-05,14,290-->

For {@{functions of three or more variables}@}, the _determinant_ of the Hessian {@{does not provide enough information to classify the critical point}@}, because {@{the number of jointly sufficient second-order conditions is equal to the number of variables}@}, and {@{the sign condition on the determinant of the Hessian is only one of the conditions}@}. Note that in {@{the one-variable case}@}, the Hessian condition {@{simply gives the usual [second derivative test](second%20derivative%20test.md#second-derivative%20test%20(single%20variable))}@}. <!--SR:!2025-04-05,14,290!2025-04-06,15,290!2025-04-05,14,290!2025-04-06,15,290!2025-04-07,16,290!2025-04-07,16,290-->

In {@{the two variable case}@}, {@{$D(a,b)$ and $f_{xx}(a,b)$}@} are {@{the principal [minors](minor%20(linear%20algebra).md) of the Hessian}@}. {@{The first two conditions listed above on the signs of these minors}@} are {@{the conditions for the positive or negative definiteness of the Hessian}@}. For {@{the general case of an arbitrary number _n_ of variables}@}, there are {@{_n_ sign conditions on the _n_ principal minors of the Hessian matrix}@} that {@{together are equivalent to positive or negative definiteness of the Hessian \([Sylvester's criterion](Sylvester's%20criterion.md)\)}@}: for {@{a local minimum}@}, {@{all the principal minors need to be positive}@}, while for {@{a local maximum}@}, {@{the minors with an odd number of rows and columns need to be negative and the minors with an even number of rows and columns need to be positive}@}. See {@{[Hessian matrix\#Bordered Hessian](Hessian%20matrix.md#bordered%20Hessian)}@} for {@{a discussion that generalizes these rules to the case of equality-constrained optimization}@}. <!--SR:!2025-04-05,14,290!2025-04-06,15,290!2025-04-07,16,290!2025-04-06,15,290!2025-04-07,16,290!2025-04-07,16,290!2025-04-07,16,290!2025-04-05,14,290!2025-04-05,14,290!2025-04-05,14,290!2025-04-07,16,290!2025-04-07,16,290!2025-04-06,15,290!2025-04-05,14,290-->

## examples

> {@{![critical points of $z = f(x, y) = (x + y) \left(xy + xy^2\right)$](../../archives/Wikimedia%20Commons/Second%20partial%20derivative%20test.png)}@}
>
> {@{Critical points}@} of $f(x,y)=(x+y)(xy+xy^{2})$ {@{maxima \(red\) and saddle points \(blue\)}@}. <!--SR:!2025-05-01,29,270!2025-04-05,14,290!2025-04-06,15,290-->

To {@{find and classify the critical points of the function}@} <p> &emsp; $z=f(x,y)=(x+y)(xy+xy^{2})$, <p> we first {@{set the partial derivatives <p> &emsp; ${\frac {\partial z}{\partial x} }=y(2x+y)(y+1)$ and ${\frac {\partial z}{\partial y} }=x\left(3y^{2}+2y(x+1)+x\right)$ <p> equal to zero}@} and {@{solve the resulting equations simultaneously to find the four critical points}@} <p> &emsp; $(0,0),(0,-1),(1,-1)$ and $\left({\frac {3}{8} },-{\frac {3}{4} }\right)$. <!--SR:!2025-04-05,14,290!2025-04-07,16,290!2025-04-06,15,290-->

In order to {@{classify the critical points}@}, we {@{examine the value of the determinant _D_\(_x_, _y_\) of the Hessian of _f_ at each of the four critical points}@}. We have $${\begin{aligned}D(a,b)&=f_{xx}(a,b)f_{yy}(a,b)-\left(f_{xy}(a,b)\right)^{2}\\&=2b(b+1)\cdot 2a(a+3b+1)-(2a+2b+4ab+3b^{2})^{2}.\end{aligned} }$$ Now we {@{plug in all the different critical values we found to label them}@}; we have $$D(0,0)=0;~~D(0,-1)=-1;~~D(1,-1)=-1;~~D\left({\frac {3}{8} },-{\frac {3}{4} }\right)={\frac {27}{128} }.$$ Thus, the second partial derivative test indicates that {@{_f_\(_x_, _y_\) has saddle points at \(0, −1\) and \(1, −1\) and has a local maximum at $\left({\frac {3}{8} },-{\frac {3}{4} }\right)$ since $f_{xx}=-{\frac {3}{8} }<0$}@}. At {@{the remaining critical point \(0, 0\) the second derivative test is insufficient}@}, and one {@{must use higher order tests or other tools to determine the behavior of the function at this point}@}. \(In fact, one can show that {@{_f_ takes both positive and negative values in small neighborhoods around \(0, 0\)}@} and so {@{this point is a saddle point of _f_}@}.\) <!--SR:!2025-04-07,16,290!2025-04-07,16,290!2025-04-05,14,290!2025-04-05,14,290!2025-04-05,14,290!2025-05-09,38,290!2025-04-07,16,290!2025-04-07,16,290-->

## notes

1. [Stewart 2005](#CITEREFStewart2005), [p. 803](https://books.google.com/books?id=eNHhKxXCJaEC&pg=PA803). <a id="^ref-1"></a>^ref-1
2. Kurt Endl/Wolfgang Luh: _Analysis II_. Aula-Verlag 1972, 7th edition 1989, [ISBN](ISBN%20(identifier).md) [3-89104-455-0](https://en.wikipedia.org/wiki/Special:BookSources/3-89104-455-0), pp. 248-258 \(German\) <a id="^ref-2"></a>^ref-2

## references

This text incorporates [content](https://en.wikipedia.org/wiki/second_partial_derivative_test) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFStewart2005"></a> [Stewart, James](James%20Stewart%20(mathematician).md) \(2005\). _Multivariable Calculus: Concepts & Contexts_. Brooks/Cole. [ISBN](ISBN%20(identifier).md) [0-534-41004-9](https://en.wikipedia.org/wiki/Special:BookSources/0-534-41004-9).

## external links

- [_Relative Minimums and Maximums_](http://tutorial.math.lamar.edu/Classes/CalcIII/RelativeExtrema.aspx) - Paul's Online Math Notes - Calc III Notes \(Lamar University\)
- <a id="CITEREFWeisstein"></a> [Weisstein, Eric W.](Eric%20W.%20Weisstein.md) ["Second Derivative Test"](https://mathworld.wolfram.com/SecondDerivativeTest.html). _[MathWorld](MathWorld.md)_.

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Multivariable calculus](https://en.wikipedia.org/wiki/Category:Multivariable%20calculus)
