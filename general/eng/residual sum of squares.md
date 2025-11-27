---
aliases:
  - RSS
  - RSSs
  - SSE
  - SSEs
  - SSR
  - SSRs
  - residual sum of squares
  - residual sums of squares
  - sum of squared estimate of errors
  - sum of squared residuals
  - sums of squared estimate of errors
  - sums of squared residuals
tags:
  - flashcard/active/general/eng/residual_sum_of_squares
  - language/in/English
---

# residual sum of squares

<!-- | ![](../../archives/Wikimedia%20Commons/Question%20book-new.svg) | This article __needs additional citations for [verification](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)__. Please help [improve this article](https://en.wikipedia.org/wiki/Special:EditPage/Residual%20sum%20of%20squares) by [adding citations to reliable sources](https://en.wikipedia.org/wiki/Help:Referencing%20for%20beginners). Unsourced material may be challenged and removed._Find sources:_["Residual sum of squares"](https://www.google.com/search?as_eq=wikipedia&q=%22Residual+sum+of+squares%22) – [news](https://www.google.com/search?tbm=nws&q=%22Residual+sum+of+squares%22+-wikipedia&tbs=ar:1) __·__ [newspapers](https://www.google.com/search?&q=%22Residual+sum+of+squares%22&tbs=bkt:s&tbm=bks) __·__ [books](https://www.google.com/search?tbs=bks:1&q=%22Residual+sum+of+squares%22+-wikipedia) __·__ [scholar](https://scholar.google.com/scholar?q=%22Residual+sum+of+squares%22) __·__ [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Residual+sum+of+squares%22&acc=on&wc=on) _\(April 2013\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

In {@{[statistics](statistics.md)}@}, {@{the __residual sum of squares__ \(__RSS__\), also known as the __sum of squared residuals__ \(__SSR__\) or the __sum of squared estimate of errors__ \(__SSE__\)}@}, is {@{the [sum](summation.md) of the [squares](square%20(algebra).md) of [residuals](errors%20and%20residuals.md) \(deviations predicted from actual empirical values of data\)}@}. It is a measure of {@{the discrepancy between the data and an estimation model}@}, such as {@{a [linear regression](linear%20regression.md)}@}. A small RSS indicates {@{a tight fit of the model to the data}@}. It is used as {@{an [optimality criterion](optimality%20criterion.md) in parameter selection and [model selection](model%20selection.md)}@}. <!--SR:!2029-03-02,1186,350!2029-02-02,1165,350!2028-09-12,1051,350!2029-01-24,1159,350!2029-03-08,1191,350!2025-12-09,267,330!2028-12-29,1138,350-->

In general, {@{[total sum of squares](total%20sum%20of%20squares.md) = [explained sum of squares](explained%20sum%20of%20squares.md) + residual sum of squares}@}. For {@{a proof of this in the multivariate [ordinary least squares](ordinary%20least%20squares.md) \(OLS\) case}@}, see {@{[partitioning in the general OLS model](explained%20sum%20of%20squares.md#partitioning%20in%20the%20general%20ordinary%20least%20squares%20model)}@}. <!--SR:!2025-12-31,284,330!2025-12-30,283,330!2027-12-04,819,330-->

## one explanatory variable

In {@{a model with a single explanatory variable}@}, RSS is given by:<sup>[\[1\]](#^ref-1)</sup> {@{$$\operatorname {RSS} =\sum _{i=1}^{n}(y_{i}-f(x_{i}))^{2}$$}@} where {@{_y_<sub>_i_</sub> is the _i_<sup>th</sup> value of the variable to be predicted, _x_<sub>_i_</sub> is the _i_<sup>th</sup> value of the explanatory variable, and $f(x_{i})$ is the predicted value of _y_<sub>_i_</sub> \(also termed ${\hat {y_{i} } }$\)}@}. In {@{a standard linear simple [regression model](regression%20analysis.md#regression%20models)}@}, {@{$y_{i}=\alpha +\beta x_{i}+\varepsilon _{i}\,$}@}, where {@{$\alpha$ and $\beta$ are [coefficients](coefficient.md), _y_ and _x_ are the [regressand](dependent%20and%20independent%20variables.md#dependent%20variable) and the [regressor](dependent%20and%20independent%20variables.md#statistics%20synonyms), respectively, and ε is the [error term](errors%20and%20residuals.md)}@}. {@{The sum of squares of residuals is the sum of squares of ${\widehat {\varepsilon \,} }_{i}$}@}; that is {@{$$\operatorname {RSS} =\sum _{i=1}^{n}({\widehat {\varepsilon \,} }_{i})^{2}=\sum _{i=1}^{n}(y_{i}-({\widehat {\alpha \,} }+{\widehat {\beta \,} }x_{i}))^{2}$$}@} where {@{${\widehat {\alpha \,} }$ is the estimated value of the constant term $\alpha$ and ${\widehat {\beta \,} }$ is the estimated value of the slope coefficient $\beta$}@}. <!--SR:!2025-12-15,272,330!2025-12-20,276,330!2027-11-15,803,330!2026-01-07,290,330!2026-01-06,289,330!2025-12-24,278,330!2027-05-30,674,330!2025-12-10,268,330!2028-11-16,1104,350-->

## matrix expression for the OLS residual sum of squares

{@{The general regression model with _n_ observations and _k_ explanators}@}, {@{the first of which (annotation: the first explanator) is a constant unit vector whose coefficient is the regression intercept}@}, is {@{$$y=X\beta +e$$}@} where {@{_y_ is an _n_ × 1 vector of dependent variable observations}@}, {@{each column of the _n_ × _k_ matrix _X_ is a vector of observations on one of the _k_ explanators}@}, {@{$\beta$ is a _k_ × 1 vector of true coefficients}@}, and {@{_e_ is an _n_ × 1 vector of the true underlying errors}@}. {@{The [ordinary least squares](ordinary%20least%20squares.md) estimator for $\beta$}@} is {@{$$\begin{aligned} & X{\hat {\beta } }=y \iff \\ & X^{\operatorname {T} }X{\hat {\beta } }=X^{\operatorname {T} }y\iff \\ & {\hat {\beta } }=(X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }y \,. \end{aligned}$$}@} \(annotation: Note that {@{$\left(X^{\operatorname T} X\right)^{-1} X^{\operatorname T}$ is a pseudoinverse of $X$}@}. In general, {@{$\left(X^{\operatorname T} X\right)^{-1} = X^{-1} \left(X^{\operatorname T}\right)^{-1}$ only holds when $X$ is an invertible square matrix}@}, so {@{$X \left(X^{\operatorname T} X\right)^{-1} X^{\operatorname T} \ne I$ in the below equations}@}.\) The residual vector {@{${\hat {e} }=y-X{\hat {\beta } }=y-X(X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }y$}@}; so the residual sum of squares is: {@{$$\operatorname {RSS} ={\hat {e} }^{\operatorname {T} }{\hat {e} }=\|{\hat {e} }\|^{2} \,,$$}@} \(equivalent to {@{the square of the [norm](norm%20(mathematics).md) of residuals}@}\). In full: {@{$$\operatorname {RSS} =y^{\operatorname {T} }y-y^{\operatorname {T} }X(X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }y=y^{\operatorname {T} }[I-X(X^{\operatorname {T} }X)^{-1}X^{\operatorname {T} }]y=y^{\operatorname {T} }[I-H]y \,,$$}@} where {@{_H_ is the [hat matrix](projection%20matrix.md), or the projection matrix in linear regression}@}. <!--SR:!2027-10-28,787,330!2026-09-25,469,310!2027-12-29,824,330!2028-08-19,1032,350!2028-01-25,845,330!2026-01-10,292,330!2027-02-14,545,310!2025-12-25,279,330!2026-04-28,346,290!2026-04-18,336,290!2026-01-09,291,330!2026-01-02,285,330!2026-09-02,371,250!2026-12-27,532,310!2026-12-18,420,387!2026-02-05,145,327!2026-08-12,295,367-->

## relation with Pearson's product-moment correlation

{@{The [least-squares regression line](least%20squares.md)}@} is given by {@{$$y=ax+b \,,$$}@} where {@{$b={\bar {y} }-a{\bar {x} }$ and $a={\frac {S_{xy} }{S_{xx} } }$}@}, where {@{$S_{xy}=\sum _{i=1}^{n}({\bar {x} }-x_{i})({\bar {y} }-y_{i})$ and $S_{xx}=\sum _{i=1}^{n}({\bar {x} }-x_{i})^{2}.$}@} Therefore, {@{$${\begin{aligned}\operatorname {RSS} &=\sum _{i=1}^{n}(y_{i}-f(x_{i}))^{2}=\sum _{i=1}^{n}(y_{i}-(ax_{i}+b))^{2}=\sum _{i=1}^{n}(y_{i}-ax_{i}-{\bar {y} }+a{\bar {x} })^{2}\\[5pt]&=\sum _{i=1}^{n}(a({\bar {x} }-x_{i})-({\bar {y} }-y_{i}))^{2}=a^{2}S_{xx}-2aS_{xy}+S_{yy}=S_{yy}-aS_{xy}=S_{yy}\left(1-{\frac {S_{xy}^{2} }{S_{xx}S_{yy} } }\right)\end{aligned} }$$}@} where {@{$S_{yy}=\sum _{i=1}^{n}({\bar {y} }-y_{i})^{2}.$}@} <!--SR:!2026-12-19,531,310!2029-01-17,1153,350!2026-02-19,296,290!2027-01-04,541,310!2026-10-20,402,250!2027-10-18,781,330-->

{@{The [Pearson product-moment correlation](Pearson%20correlation%20coefficient.md)}@} is given by {@{$r={\frac {S_{xy} }{\sqrt {S_{xx}S_{yy} } } };$}@} therefore, {@{$\operatorname {RSS} =S_{yy}(1-r^{2}).$}@} <!--SR:!2028-09-17,1056,350!2026-08-15,344,270!2026-05-20,259,210-->

## see also

- [Akaike information criterion\#Comparison with least squares](Akaike%20information%20criterion.md#comparison%20with%20least%20squares)
- [Chi-squared distribution\#Applications](chi-squared%20distribution.md#applications)
- [Degrees of freedom \(statistics\)\#Sum of squares and degrees of freedom](degrees%20of%20freedom%20(statistics).md#sum%20of%20squares%20and%20degrees%20of%20freedom)
- [Errors and residuals in statistics](errors%20and%20residuals.md)
- [Lack-of-fit sum of squares](lack-of-fit%20sum%20of%20squares.md)
- [Mean squared error](mean%20squared%20error.md)
- [Reduced chi-squared statistic](reduced%20chi-squared%20statistic.md), RSS per degree of freedom
- [Squared deviations](squared%20deviations%20from%20the%20mean.md)
- [Sum of squares \(statistics\)](partition%20of%20sums%20of%20squares.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/residual_sum_of_squares) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFArchdeacon, Thomas J.1994"></a> Archdeacon, Thomas J. \(1994\). _Correlation and regression analysis : a historian's guide_. University of Wisconsin Press. pp. 161–162. [ISBN](ISBN.md) [0-299-13650-7](https://en.wikipedia.org/wiki/Special:BookSources/0-299-13650-7). [OCLC](OCLC.md#OCLC) [27266095](https://search.worldcat.org/oclc/27266095). <a id="^ref-1"></a>^ref-1

- <a id="CITEREFDraperSmith1998"></a> Draper, N.R.; Smith, H. \(1998\). _Applied Regression Analysis_ \(3rd ed.\). John Wiley. [ISBN](ISBN.md) [0-471-17082-8](https://en.wikipedia.org/wiki/Special:BookSources/0-471-17082-8).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Least squares](https://en.wikipedia.org/wiki/Category:Least%20squares)
> - [Errors and residuals](https://en.wikipedia.org/wiki/Category:Errors%20and%20residuals)
