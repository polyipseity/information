---
aliases:
  - ESS
  - ESSs
  - SSR
  - SSRs
  - explained sum of squares
  - explained sums of squares
  - model sum of squares
  - model sums of squares
  - sum of squares due to regression
  - sums of squares due to regression
tags:
  - flashcard/active/general/eng/explained_sum_of_squares
  - language/in/English
---

# explained sum of squares

<!-- | ![](../../archives/Wikimedia%20Commons/Text%20document%20with%20red%20question%20mark.svg) | This article includes a list of [general references](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#General%20references), but __it lacks sufficient corresponding [inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#Inline%20citations)__. Please help to [improve](https://en.wikipedia.org/wiki/Wikipedia:WikiProject%20Reliability) this article by [introducing](https://en.wikipedia.org/wiki/Wikipedia:When%20to%20cite) more precise citations. _\(December 2010\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

In {@{[statistics](statistics.md)}@}, {@{the __explained sum of squares__ \(__ESS__\), alternatively known as the __model sum of squares__ or __sum of squares due to regression__ \(__SSR__}@} – {@{not to be confused with the [residual sum of squares](residual%20sum%20of%20squares.md) \(RSS\) or sum of squares of errors}@}\), is {@{a quantity used in describing how well a model, often a [regression model](regression%20analysis.md), represents the data being modelled}@}. In particular, the explained sum of squares measures {@{how much variation there is in the modelled values}@} and this is {@{compared to the [total sum of squares](total%20sum%20of%20squares.md) \(TSS\), which measures how much variation there is in the observed data}@}, and to {@{the [residual sum of squares](residual%20sum%20of%20squares.md), which measures the variation in the error between the observed data and modelled values}@}. <!--SR:!2025-11-28,258,330!2027-08-08,725,330!2025-12-07,265,330!2026-10-26,488,310!2026-01-11,293,330!2026-12-12,525,310!2025-08-31,185,310-->

## definition

{@{The explained sum of squares \(ESS\)}@} is {@{the sum of the squares of the deviations of the predicted values from the mean value of a response variable, in a standard [regression model](regression%20analysis.md#regression%20models)}@} — for example, {@{_y_<sub>_i_</sub> = _a_ + _b_<sub>1</sub>_x_<sub>1<!-- markdown separator -->_i_</sub> + _b_<sub>2</sub>_x_<sub>2<!-- markdown separator -->_i_</sub> + ... + _ε_<sub>_i_</sub>}@}, where {@{_y_<sub>_i_</sub> is the _i_ <sup>th</sup> observation of the [response variable](dependent%20and%20independent%20variables.md#statistics%20synonyms), _x_<sub>_ji_</sub> is the _i_ <sup>th</sup> observation of the _j_ <sup>th</sup> [explanatory variable](dependent%20and%20independent%20variables.md#statistics%20synonyms)}@}, {@{_a_ and _b_<sub>_j_</sub> are [coefficients](coefficient.md)}@}, {@{_i_ indexes the observations from 1 to _n_}@}, and {@{_ε_<sub>_i_</sub> is the _i_<!-- markdown separator --> <sup>th</sup> value of the [error term](error%20term.md)}@}. In general, the greater {@{the ESS, the better the estimated model performs}@}. <!--SR:!2026-01-05,288,330!2026-11-18,515,310!2025-09-05,189,310!2026-12-30,537,310!2025-12-15,272,330!2025-12-16,272,330!2025-12-24,278,330!2025-10-01,196,310-->

If {@{${\hat {a} }$ and ${\hat {b} }_{i}$ are the estimated [coefficients](coefficient.md)}@}, then {@{$${\hat {y} }_{i}={\hat {a} }+{\hat {b} }_{1}x_{1i}+{\hat {b} }_{2}x_{2i}+\cdots \,$$}@} is {@{the _i_<sup> th</sup> predicted value of the response variable}@}. The ESS is then: {@{$${\text{ESS} }=\sum _{i=1}^{n}\left({\hat {y} }_{i}-{\bar {y} }\right)^{2}.$$}@} where {@{${\hat {y} }_{i}$ is the value estimated by the regression line}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-08-29,179,310!2025-11-01,236,330!2025-08-22,177,310!2025-11-20,252,330!2025-12-08,266,330-->

In {@{some cases \(see below\)}@}: {@{[total sum of squares](total%20sum%20of%20squares.md) \(TSS\) = explained sum of squares \(ESS\) + [residual sum of squares](residual%20sum%20of%20squares.md) \(RSS\)}@}. <!--SR:!2025-12-30,283,330!2025-12-31,284,330-->

## partitioning in simple linear regression

The following equality, stating that {@{the total sum of squares \(TSS\) equals the residual sum of squares \(=SSE: the sum of squared errors of prediction\) plus the explained sum of squares \(SSR: the sum of squares due to regression or explained sum of squares\)}@}, is {@{generally true in simple linear regression}@}: {@{$$\sum _{i=1}^{n}\left(y_{i}-{\bar {y} }\right)^{2}=\sum _{i=1}^{n}\left(y_{i}-{\hat {y} }_{i}\right)^{2}+\sum _{i=1}^{n}\left({\hat {y} }_{i}-{\bar {y} }\right)^{2}.$$}@} <!--SR:!2025-08-27,170,310!2025-12-20,276,330!2025-11-15,248,330-->

### simple derivation

{@{$${\begin{aligned}(y_{i}-{\bar {y} })=(y_{i}-{\hat {y} }_{i})+({\hat {y} }_{i}-{\bar {y} }).\end{aligned} }$$}@} {@{Square both sides and sum over all _i_}@}: {@{$$\sum _{i=1}^{n}(y_{i}-{\bar {y} })^{2}=\sum _{i=1}^{n}(y_{i}-{\hat {y} }_{i})^{2}+\sum _{i=1}^{n}({\hat {y} }_{i}-{\bar {y} })^{2}+\sum _{i=1}^{n}2({\hat {y} }_{i}-{\bar {y} })(y_{i}-{\hat {y} }_{i}).$$}@} Here is {@{how the last term above is zero from [simple linear regression](simple%20linear%20regression.md)}@}<sup>[\[2\]](#^ref-2)</sup> {@{$$\begin{aligned} {\hat {y_{i} } } & = {\hat {a} }+{\hat {b} }x_{i} \\ {\bar {y} } & = {\hat {a} }+{\hat {b} }{\bar {x} } \\ {\hat {b} } & = {\frac {\sum _{i=1}^{n}(x_{i}-{\bar {x} })(y_{i}-{\bar {y} })}{\sum _{i=1}^{n}(x_{i}-{\bar {x} })^{2} } } \end{aligned}$$}@} So, {@{$$\begin{aligned} {\hat {y_{i} } }-{\bar {y} } & = {\hat {b} }(x_{i}-{\bar {x} }) \\ y_{i}-{\hat {y} }_{i} & = (y_{i}-{\bar {y} })-({\hat {y} }_{i}-{\bar {y} })=(y_{i}-{\bar {y} })-{\hat {b} }(x_{i}-{\bar {x} }) \end{aligned}$$}@} Therefore, {@{$${\begin{aligned}&\sum _{i=1}^{n}2({\hat {y} }_{i}-{\bar {y} })(y_{i}-{\hat {y} }_{i})=2{\hat {b} }\sum _{i=1}^{n}(x_{i}-{\bar {x} })(y_{i}-{\hat {y} }_{i})\\[4pt]={}&2{\hat {b} }\sum _{i=1}^{n}(x_{i}-{\bar {x} })((y_{i}-{\bar {y} })-{\hat {b} }(x_{i}-{\bar {x} }))\\[4pt]={}&2{\hat {b} }\left(\sum _{i=1}^{n}(x_{i}-{\bar {x} })(y_{i}-{\bar {y} })-\sum _{i=1}^{n}(x_{i}-{\bar {x} })^{2}{\frac {\sum _{j=1}^{n}(x_{j}-{\bar {x} })(y_{j}-{\bar {y} })}{\sum _{j=1}^{n}(x_{j}-{\bar {x} })^{2} } }\right)\\[4pt]={}&2{\hat {b} }(0)=0\end{aligned} }$$}@} (annotation: The general strategy is {@{rewriting $\hat y_i$ in terms of $x_i$, $\overline x$, $y_i$, and/or $\overline y$}@}.) <!--SR:!2025-11-22,254,330!2026-01-10,292,330!2027-01-16,550,310!2025-08-26,169,310!2026-12-10,524,310!2026-03-17,318,290!2026-07-07,337,250!2027-01-06,540,310-->

## partitioning in the general ordinary least squares model

{@{The general regression model with _n_ observations and _k_ explanators}@}, the first of which (annotation: the first explanator) is {@{a constant unit vector whose coefficient is the regression intercept}@}, is {@{$$y=X\beta +e$$}@} where {@{_y_ is an _n_ × 1 vector of dependent variable observations}@}, {@{each column of the _n_ × _k_ matrix _X_ is a vector of observations on one of the _k_ explanators}@}, {@{$\beta$ is a _k_ × 1 vector of true coefficients}@}, and {@{_e_ is an _n_ × 1 vector of the true underlying errors}@}. {@{The [ordinary least squares](ordinary%20least%20squares.md) estimator for $\beta$}@} is {@{$${\hat {\beta } }=(X^{T}X)^{-1}X^{T}y.$$ (annotation: $X^T X$ is the covariance matrix of the _k_ explanators)}@} {@{The residual vector ${\hat {e} }$}@} is {@{$y-X{\hat {\beta } }=y-X(X^{T}X)^{-1}X^{T}y$}@}, so {@{the residual sum of squares ${\hat {e} }^{T}{\hat {e} }$}@} is, {@{after simplification, $$RSS=y^{T}y-y^{T}X(X^{T}X)^{-1}X^{T}y = y^T y - y^T \hat y.$$}@} Denote {@{as ${\bar {y} }$ the constant vector (annotation: a scalar duplicated _n_ times to become a _n_ × 1 vector) all of whose elements are the sample mean $y_{m}$ of the dependent variable values in the vector _y_}@}. Then the total sum of squares is {@{$$TSS=(y-{\bar {y} })^{T}(y-{\bar {y} })=y^{T}y-2y^{T}{\bar {y} }+{\bar {y} }^{T}{\bar {y} }.$$}@} The explained sum of squares, defined as {@{the sum of squared deviations of the predicted values from the observed mean of _y_}@}, is {@{$$ESS=({\hat {y} }-{\bar {y} })^{T}({\hat {y} }-{\bar {y} })={\hat {y} }^{T}{\hat {y} }-2{\hat {y} }^{T}{\bar {y} }+{\bar {y} }^{T}{\bar {y} }.$$}@} Using {@{${\hat {y} }=X{\hat {\beta } }$ in this, and simplifying to obtain ${\hat {y} }^{T}{\hat {y} } = (y^T X (X^T X)^{-1} X^T)(X (X^T X)^{-1} X^T y) = y^{T}X(X^{T}X)^{-1}X^{T}y = y^T \hat y$}@}, gives the result that {@{_TSS_ = _ESS_ + _RSS_ if and only if $y^{T}{\bar {y} }={\hat {y} }^{T}{\bar {y} }$}@}. The left side of this is {@{$y_{m}$ times the sum of the elements of _y_}@}, and {@{the right side is $y_{m}$ times the sum of the elements of ${\hat {y} }$}@}, so the condition is that {@{the sum of the elements of _y_ equals the sum of the elements of ${\hat {y} }$}@}, or equivalently that {@{the sum of the prediction errors \(residuals\) $y_{i}-{\hat {y} }_{i}$ is zero}@}. This can be seen to be true by {@{noting the well-known OLS property that the _k_ × 1 vector $X^{T}{\hat {e} }=X^{T}[I-X(X^{T}X)^{-1}X^{T}]y=0$}@}: since {@{the first column of _X_ is a vector of ones}@}, {@{the first element of this vector $X^{T}{\hat {e} }$ is the sum of the residuals and is equal to zero}@}. This proves that {@{the condition holds for the result that _TSS_ = _ESS_ + _RSS_}@}. <!--SR:!2025-11-30,259,330!2025-12-29,282,330!2025-09-29,194,310!2025-12-01,260,330!2025-11-08,242,330!2025-10-25,230,330!2025-08-27,181,310!2025-11-04,238,330!2025-09-12,160,250!2025-12-17,273,330!2025-09-15,184,310!2027-01-10,546,310!2025-10-06,199,310!2026-01-04,287,330!2025-11-14,247,330!2025-08-26,181,310!2025-12-20,227,270!2026-12-31,538,310!2026-11-20,507,310!2025-12-02,261,330!2026-01-12,294,330!2026-01-03,286,330!2025-08-29,171,310!2026-01-13,236,270!2025-08-20,164,310!2026-03-22,319,290!2025-08-16,171,310-->

In {@{linear algebra terms}@}, we have {@{$RSS=\|y-{\hat {y} }\|^{2}$, $TSS=\|y-{\bar {y} }\|^{2}$, $ESS=\|{\hat {y} }-{\bar {y} }\|^{2}$}@}. The proof can be simplified by {@{noting that ${\hat {y} }^{T}{\hat {y} }={\hat {y} }^{T}y$}@}. The proof is as follows: {@{$${\hat {y} }^{T}{\hat {y} }=y^{T}X(X^{T}X)^{-1}X^{T}X(X^{T}X)^{-1}X^{T}y=y^{T}X(X^{T}X)^{-1}X^{T}y={\hat {y} }^{T}y,$$}@} Thus, {@{$${\begin{aligned}TSS&=\|y-{\bar {y} }\|^{2}=\|y-{\hat {y} }+{\hat {y} }-{\bar {y} }\|^{2}\\&=\|y-{\hat {y} }\|^{2}+\|{\hat {y} }-{\bar {y} }\|^{2}+2\langle y-{\hat {y} },{\hat {y} }-{\bar {y} }\rangle \\&=RSS+ESS+2y^{T}{\hat {y} }-2{\hat {y} }^{T}{\hat {y} }-2y^{T}{\bar {y} }+2{\hat {y} }^{T}{\bar {y} }\\&=RSS+ESS-2y^{T}{\bar {y} }+2{\hat {y} }^{T}{\bar {y} }\end{aligned} }$$}@} which again gives the result that {@{_TSS_ = _ESS_ + _RSS_, since $(y-{\hat {y} })^{T}{\bar {y} }=0$}@}. <!--SR:!2025-12-14,271,330!2025-12-23,277,330!2025-09-04,188,310!2026-12-02,518,310!2025-10-20,202,270!2026-09-15,460,310-->

## see also

- [Sum of squares \(statistics\)](partition%20of%20sums%20of%20squares.md)
- [Lack-of-fit sum of squares](lack-of-fit%20sum%20of%20squares.md)
- [Fraction of variance unexplained](fraction%20of%20variance%20unexplained.md)

## notes

1. ["Sum of Squares - Definition, Formulas, Regression Analysis"](https://corporatefinanceinstitute.com/resources/knowledge/other/sum-of-squares/). _Corporate Finance Institute_. Retrieved 2020-06-11. <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFMendenhall2009"></a> Mendenhall, William \(2009\). _Introduction to Probability and Statistics_ \(13th ed.\). Belmont, CA: Brooks/Cole. p. 507. [ISBN](ISBN.md) [9780495389538](https://en.wikipedia.org/wiki/Special:BookSources/9780495389538). <a id="^ref-2"></a>^ref-2

## references

This text incorporates [content](https://en.wikipedia.org/wiki/explained_sum_of_squares) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- S. E. Maxwell and H. D. Delaney \(1990\), "Designing experiments and analyzing data: A model comparison perspective". Wadsworth. pp. 289–290.
- G. A. Milliken and D. E. Johnson \(1984\), "Analysis of messy data", Vol. I: Designed experiments. Van Nostrand Reinhold. pp. 146–151.
- B. G. Tabachnick and L. S. Fidell \(2007\), "Experimental design using ANOVA". Duxbury. p. 220.
- B. G. Tabachnick and L. S. Fidell \(2007\), "Using multivariate statistics", 5th ed. Pearson Education. pp. 217–218.

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Least squares](https://en.wikipedia.org/wiki/Category:Least%20squares)
