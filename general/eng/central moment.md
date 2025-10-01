---
aliases:
  - central moment
  - central moments
tags:
  - flashcard/active/general/eng/central_moment
  - language/in/English
---

# central moment

<!-- | ![](../../archives/Wikimedia%20Commons/Question%20book-new.svg) | This article __needs additional citations for [verification](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)__. Please help [improve this article](https://en.wikipedia.org/wiki/Special:EditPage/Central%20moment) by [adding citations to reliable sources](https://en.wikipedia.org/wiki/Help:Referencing%20for%20beginners). Unsourced material may be challenged and removed._Find sources:_ ["Central moment"](https://www.google.com/search?as_eq=wikipedia&q=%22Central+moment%22) – [news](https://www.google.com/search?tbm=nws&q=%22Central+moment%22+-wikipedia&tbs=ar:1) __·__ [newspapers](https://www.google.com/search?&q=%22Central+moment%22&tbs=bkt:s&tbm=bks) __·__ [books](https://www.google.com/search?tbs=bks:1&q=%22Central+moment%22+-wikipedia) __·__ [scholar](https://scholar.google.com/scholar?q=%22Central+moment%22) __·__ [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Central+moment%22&acc=on&wc=on) _\(September 2014\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

In {@{[probability theory](probability%20theory.md) and [statistics](statistics.md)}@}, {@{a __central moment__}@} is {@{a [moment](moment%20(mathematics).md) of a [probability distribution](probability%20distribution.md) of a [random variable](random%20variable.md) about the random variable's [mean](mean.md)}@}; that is, it is {@{the [expected value](expected%20value.md) of a specified integer power of the deviation of the random variable from the mean}@}. {@{The various moments}@} form {@{one set of values by which the properties of a probability distribution can be usefully characterized}@}. Central moments are used {@{in preference to ordinary moments}@}, computed {@{in terms of deviations from the mean instead of from zero}@}, because {@{the higher-order central moments relate only to the spread and shape of the distribution}@}, rather than {@{also to its [location](location%20parameter.md)}@}. <!--SR:!2026-01-11,266,330!2026-01-23,276,330!2026-08-03,414,310!2028-02-15,848,330!2026-01-28,280,330!2026-01-09,265,330!2025-12-26,253,330!2025-10-30,193,310!2026-10-10,462,310!2026-01-28,280,330-->

{@{Sets of central moments}@} can be defined for {@{both univariate and multivariate distributions}@}. <!--SR:!2027-11-09,773,330!2026-02-01,283,330-->

## univariate moments

{@{The _n_<!-- markdown separator -->th [moment](moment%20(mathematics).md) about the [mean](mean.md) \(or _n_<!-- markdown separator -->th __central moment__\) of a real-valued [random variable](random%20variable.md) _X_}@} is {@{the quantity _μ_<sub>_n_</sub> := E\[\(_X_ − E\[_X_\]\)<sup>_n_</sup>\]}@}, where {@{E is the [expectation operator](expected%20value.md)}@}. For {@{a [continuous](continuous%20probability%20distribution.md#absolutely%20continuous%20probability%20distribution) [univariate](univariate.md) [probability distribution](probability%20distribution.md) with [probability density function](probability%20density%20function.md) _f_\(_x_\)}@}, {@{the _n_<!-- markdown separator -->th moment about the mean _μ_}@} is <p> {@{$\mu _{n}=\operatorname {E} \left[(X-\operatorname {E} [X])^{n}\right]=\int _{-\infty }^{+\infty }(x-\mu )^{n}f(x)\,\mathrm {d} x$}@}.<sup>[\[1\]](#^ref-1)</sup> <p> For {@{random variables that have no mean, such as the [Cauchy distribution](Cauchy%20distribution.md)}@}, {@{central moments are not defined}@}. <!--SR:!2026-01-06,263,330!2027-11-22,783,330!2026-02-04,285,330!2026-11-28,496,310!2027-03-16,568,310!2026-02-07,288,330!2028-02-07,841,330!2026-02-17,294,330-->

{@{The first few central moments}@} have {@{intuitive interpretations}@}: <!--SR:!2026-01-07,263,330!2026-01-10,265,330-->

- The "zeroth" central moment _μ_<sub>0</sub> ::@:: is 1. <!--SR:!2026-01-05,262,330!2026-01-01,259,330-->
- The first central moment _μ_<sub>1</sub> ::@:: is 0 \(not to be confused with the first [raw moment](raw%20moment.md) or the [expected value](expected%20value.md) _μ_\). <!--SR:!2026-02-08,289,330!2027-12-18,803,330-->
- The second central moment _μ_<sub>2</sub> ::@:: is called the [variance](variance.md), and is usually denoted _σ_<sup>2</sup>, where σ represents the [standard deviation](standard%20deviation.md). <!--SR:!2026-01-08,264,330!2026-02-16,293,330-->
- The third and fourth central moments ::@:: are used to define the [standardized moments](standardized%20moment.md) which are used to define [skewness](skewness.md) and [kurtosis](kurtosis.md), respectively. <!--SR:!2026-02-16,293,330!2026-02-06,287,330-->

### properties

For {@{all _n_, the _n_<!-- markdown separator -->th central moment}@} is {@{[homogeneous](homogeneous%20function.md) of degree _n_: $$\mu _{n}(cX)=c^{n}\mu _{n}(X).\,$$}@} <!--SR:!2026-01-04,261,330!2025-12-25,252,330-->

{@{_Only_ for _n_ such that n equals 1, 2, or 3}@} do we have {@{an additivity property for random variables _X_ and _Y_ that are [independent](statistical%20independence.md)}@}: <p> {@{$\mu _{n}(X+Y)=\mu _{n}(X)+\mu _{n}(Y)\,$ provided _n_ ∈ {1, 2, 3}<!-- flashcard separator -->}@}. <!--SR:!2026-01-22,276,330!2027-12-16,801,330!2026-01-22,275,330-->

{@{A related functional that shares the translation-invariance and homogeneity properties with the _n_<!-- markdown separator -->th central moment}@}, but {@{continues to have this additivity property even when _n_ ≥ 4}@} is {@{the _n_<!-- markdown separator -->th [cumulant](cumulant.md) κ<sub>_n_</sub>\(_X_\)}@}. For {@{_n_ = 1, the _n_<!-- markdown separator -->th cumulant is just the [expected value](expected%20value.md)}@}; for {@{_n_ = either 2 or 3, the _n_<!-- markdown separator -->th cumulant is just the _n_<!-- markdown separator -->th central moment}@}; for {@{_n_ ≥ 4, the _n_<!-- markdown separator -->th cumulant}@} is {@{an _n_<!-- markdown separator -->th-degree monic polynomial in the first _n_ moments \(about zero\)}@}, and is {@{also a \(simpler\) _n_<!-- markdown separator -->th-degree polynomial in the first _n_ central moments}@}. <!--SR:!2026-01-29,281,330!2026-01-31,282,330!2026-02-03,285,330!2026-06-06,367,310!2027-11-24,771,330!2027-04-18,562,310!2026-12-31,515,310!2026-05-31,363,310-->

### relation to moments about the origin

Sometimes it is convenient to {@{convert moments about the origin to moments about the mean}@}. {@{The general equation for converting the _n_<!-- markdown separator -->th-order moment about the origin to the moment about the mean}@} is {@{$$\mu _{n}=\operatorname {E} \left[\left(X-\operatorname {E} [X]\right)^{n}\right]=\sum _{j=0}^{n}{n \choose j}(-1)^{n-j}\mu '_{j}\mu ^{n-j},$$}@} where {@{_μ_ is the mean of the distribution}@}, and {@{the moment about the origin is given by $$\mu '_{m}=\int _{-\infty }^{+\infty }x^{m}f(x)\,dx=\operatorname {E} [X^{m}]=\sum _{j=0}^{m}{m \choose j}\mu _{j}\mu ^{m-j}.$$}@} For {@{the cases _n_ = 2, 3, 4}@} — which are {@{of most interest because of the relations to [variance](variance.md), [skewness](skewness.md), and [kurtosis](kurtosis.md), respectively}@} — this formula becomes \(noting that {@{$\mu =\mu '_{1}$ and $\mu '_{0}=1$}@}\): <p> {@{$\mu _{2}=\mu '_{2}-\mu ^{2}\,$ which is commonly referred to as $\operatorname {Var} (X)=\operatorname {E} [X^{2}]-\left(\operatorname {E} [X]\right)^{2}$ <br/> $$\mu _{3}=\mu '_{3}-3\mu \mu '_{2}+2\mu ^{3}\,$$ <br/> $$\mu _{4}=\mu '_{4}-4\mu \mu '_{3}+6\mu ^{2}\mu '_{2}-3\mu ^{4}.\,$$ <p> ... and so on}@},<sup>[\[2\]](#^ref-2)</sup> following {@{[Pascal's triangle](Pascal's%20triangle.md)}@}, i.e. $$\mu _{5}=\mu '_{5}-5\mu \mu '_{4}+10\mu ^{2}\mu '_{3}-10\mu ^{3}\mu '_{2}+4\mu ^{5}.\,$$ because {@{$5\mu ^{4}\mu '_{1}-\mu ^{5}\mu '_{0}=5\mu ^{4}\mu -\mu ^{5}=5\mu ^{5}-\mu ^{5}=4\mu ^{5}$}@} <!--SR:!2026-01-28,280,330!2025-12-29,256,330!2026-02-16,246,270!2027-10-17,755,330!2025-12-20,73,190!2027-12-17,803,330!2026-01-10,266,330!2025-12-30,257,330!2026-06-06,350,290!2026-01-22,275,330!2026-05-10,331,290-->

The following sum is {@{a stochastic variable having a ___compound distribution___ $$W=\sum _{i=1}^{M}Y_{i},$$}@} where {@{the $Y_{i}$ are mutually independent random variables sharing the same common distribution}@} and {@{$M$ a random integer variable independent of the $Y_{k}$ with its own distribution}@}. {@{The moments of $W$}@} are obtained as {@{$$\operatorname {E} [W^{n}]=\sum _{i=0}^{n}\operatorname {E} \left[{M \choose i}\right]\sum _{j=0}^{i}{i \choose j}(-1)^{i-j}\operatorname {E} \left[\left(\sum _{k=1}^{j}Y_{k}\right)^{n}\right],$$}@} where {@{$\operatorname {E} \left[\left(\sum _{k=1}^{j}Y_{k}\right)^{n}\right]$ is defined as zero for $j=0$}@}. <!--SR:!2026-01-22,275,330!2026-08-02,413,310!2026-11-27,496,310!2026-02-02,284,330!2025-11-28,43,170!2025-12-31,258,330-->

### symmetric distributions

In {@{distributions that are [symmetric about their means](symmetric%20distribution.md) \(unaffected by being [reflected](reflection%20(mathematics).md) about the mean\)}@}, {@{all odd central moments equal zero whenever they exist}@}, because in {@{the formula for the _n_<!-- markdown separator -->th moment}@}, each term involving a value of _X_ less than the mean by a certain amount {@{exactly cancels out the term involving a value of _X_ greater than the mean by the same amount}@}. <!--SR:!2027-10-27,764,330!2027-12-15,802,330!2026-02-15,292,330!2026-02-15,292,330-->

## multivariate moments

For {@{a [continuous](continuous%20probability%20distribution.md#absolutely%20continuous%20probability%20distribution) [bivariate](joint%20probability%20distribution.md) [probability distribution](probability%20distribution.md) with [probability density function](probability%20density%20function.md) _f_\(_x_,_y_\)}@} {@{the \(_j_,_k_\) moment about the mean _μ_ = \(_μ_<sub>_X_</sub>, _μ_<sub>_Y_</sub>\)}@} is {@{$$\mu _{j,k}=\operatorname {E} \left[(X-\operatorname {E} [X])^{j}(Y-\operatorname {E} [Y])^{k}\right]=\int _{-\infty }^{+\infty }\int _{-\infty }^{+\infty }(x-\mu _{X})^{j}(y-\mu _{Y})^{k}f(x,y)\,dx\,dy.$$}@} <!--SR:!2026-02-09,290,330!2026-01-22,276,330!2027-12-09,795,330-->

## central moment of complex random variables

{@{The _n_<!-- markdown separator -->th central moment for a complex random variable _X_}@} is defined as <sup>[\[3\]](#^ref-3)</sup> {@{$$\alpha _{n}=\operatorname {E} \left[(X-\operatorname {E} [X])^{n}\right],$$}@} {@{The absolute _n_<!-- markdown separator -->th central moment of _X_}@} is defined as {@{$$\beta _{n}=\operatorname {E} \left[|(X-\operatorname {E} [X])|^{n}\right].$$}@} {@{The 2nd-order (annotation: absolute) central moment _β_<sub>2</sub>}@} is called {@{the [_variance_](complex%20random%20variable.md#variance%20and%20pseudo-variance) of _X_}@} whereas {@{the 2nd-order central moment _α_<sub>2</sub>}@} is {@{the [_pseudo-variance_](complex%20random%20variable.md#variance%20and%20pseudo-variance) of _X_}@}. <!--SR:!2026-01-30,281,330!2026-01-22,275,330!2026-01-02,259,330!2027-11-20,768,330!2025-10-28,191,310!2026-01-29,281,330!2026-01-22,276,330!2026-01-22,276,330-->

## see also

- [Standardized moment](standardized%20moment.md)
- [Image moment](image%20moment.md)
- [Normal distribution § Moments](normal%20distribution.md#moments)
- [Complex random variable](complex%20random%20variable.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/central_moment) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFGrimmett, GeoffreyStirzaker, David2009"></a> Grimmett, Geoffrey; Stirzaker, David \(2009\). _Probability and Random Processes_. Oxford, England: Oxford University Press. [ISBN](ISBN%20(identifier).md) [978-0-19-857222-0](https://en.wikipedia.org/wiki/Special:BookSources/978-0-19-857222-0). <a id="^ref-1"></a>^ref-1
2. ["Central Moment"](http://mathworld.wolfram.com/CentralMoment.html). <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFErikssonOllilaKoivunen2009"></a> Eriksson, Jan; Ollila, Esa; Koivunen, Visa \(2009\). "Statistics for complex random variables revisited". _2009 IEEE International Conference on Acoustics, Speech and Signal Processing_. pp. 3565–3568. [doi](doi%20(identifier).md):[10.1109/ICASSP.2009.4960396](https://doi.org/10.1109%2FICASSP.2009.4960396). [ISBN](ISBN%20(identifier).md) [978-1-4244-2353-8](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4244-2353-8). [S2CID](S2CID%20(identifier).md#S2CID) [17433817](https://api.semanticscholar.org/CorpusID:17433817). <a id="^ref-3"></a>^ref-3

| <!-- hide <p> - [v](https://en.wikipedia.org/wiki/Template:Theory%20of%20probability%20distributions) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Theory%20of%20probability%20distributions) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3ATheory%20of%20probability%20distributions) <p>  <p>  <br/> --> Theory of [probability distributions](probability%20distribution.md) |                                                                                                                          |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| ------------------------------------------------------------------------------------------------------------------------:|
| - [probability mass function](probability%20mass%20function.md) \(pmf\) <br/> - [probability density function](probability%20density%20function.md) \(pdf\) <br/> - [cumulative distribution function](cumulative%20distribution%20function.md) \(cdf\) <br/> - [quantile function](quantile%20function.md)                                                                                                          | ![log-logistic density function plot, without labels](../../archives/Wikimedia%20Commons/Loglogisticpdf%20no-labels.svg) |
| - [raw moment](raw%20moment.md) <br/> - [central moment](central%20moment.md) <br/> - [mean](expected%20value.md) <br/> - [variance](variance.md) <br/> - [standard deviation](standard%20deviation.md) <br/> - [skewness](skewness.md) <br/> - [kurtosis](kurtosis.md) <br/> - [L-moment](L-moment.md)                                                                                                              |                                                                                                                          |
| - [moment-generating function](moment-generating%20function.md) \(mgf\) <br/> - [characteristic function](characteristic%20function%20(probability%20theory).md) <br/> - [probability-generating function](probability-generating%20function.md) \(pgf\) <br/> - [cumulant](cumulant.md) <br/> - [combinant](combinant.md)                                                                                           |                                                                                                                          |

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Statistical deviation and dispersion](https://en.wikipedia.org/wiki/Category:Statistical%20deviation%20and%20dispersion)
> - [Moment \(mathematics\)](https://en.wikipedia.org/wiki/Category:Moment%20%28mathematics%29)
