---
aliases:
  - sinusoidal model
  - sinusoidal models
tags:
  - flashcard/active/general/eng/sinusoidal_model
  - language/in/English
---

# sinusoidal model

<!-- | ![](../../archives/Wikimedia%20Commons/Question%20book-new.svg) | This article __needs additional citations for [verification](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)__. Please help [improve this article](https://en.wikipedia.org/wiki/Special:EditPage/Sinusoidal%20model) by [adding citations to reliable sources](https://en.wikipedia.org/wiki/Help:Referencing%20for%20beginners). Unsourced material may be challenged and removed._Find sources:_ ["Sinusoidal model"](https://www.google.com/search?as_eq=wikipedia&q=%22Sinusoidal+model%22) – [news](https://www.google.com/search?tbm=nws&q=%22Sinusoidal+model%22+-wikipedia&tbs=ar:1) __·__ [newspapers](https://www.google.com/search?&q=%22Sinusoidal+model%22&tbs=bkt:s&tbm=bks) __·__ [books](https://www.google.com/search?tbs=bks:1&q=%22Sinusoidal+model%22+-wikipedia) __·__ [scholar](https://scholar.google.com/scholar?q=%22Sinusoidal+model%22) __·__ [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Sinusoidal+model%22&acc=on&wc=on) _\(February 2008\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

In {@{[statistics](statistics.md), [signal processing](signal%20processing.md), and [time series analysis](time%20series%20analysis.md)}@}, a {@{__sinusoidal model__}@} is used to {@{approximate a sequence _Y<sub>i</sub>_ to a [sine](sine.md) function}@}: {@{$$Y_{i}=C+\alpha \sin(\omega T_{i}+\phi )+E_{i}$$}@} where {@{_C_ is constant defining a [mean](mean.md) level, α is an [amplitude](amplitude.md) for the [sine](sine.md), ω is the [angular frequency](angular%20frequency.md), _T<sub>i</sub>_ is a time variable, φ is the [phase-shift](phase-shift.md#phase%20shift), and _E<sub>i</sub>_ is the error sequence}@}. <!--SR:!2026-05-23,253,330!2025-09-22,67,310!2026-06-07,265,330!2026-06-17,273,330!2025-10-08,29,290-->

This sinusoidal model can be fit using {@{[nonlinear least squares](nonlinear%20least%20squares.md)}@}; to {@{obtain a good fit}@}, routines may {@{require good starting values for the unknown parameters}@}. {@{Fitting a model with a single sinusoid}@} is {@{a special case of [spectral density estimation](spectral%20density%20estimation.md) and [least-squares spectral analysis](least-squares%20spectral%20analysis.md)}@}. <!--SR:!2026-06-07,264,330!2026-04-27,232,330!2026-05-07,241,330!2026-06-04,263,330!2025-09-19,64,310-->

## good starting values

### good starting value for the mean

{@{A good starting value for _C_}@} can be obtained by {@{calculating the [mean](mean.md) of the data}@}. If {@{the data show a [trend](trend%20estimation.md), i.e., the assumption of constant location is violated}@}, one can {@{replace _C_ with a linear or quadratic [least squares](least%20squares.md) fit}@}. That is, the model becomes {@{$$Y_{i}=(B_{0}+B_{1}T_{i})+\alpha \sin( \omega T_{i}+\phi )+E_{i}$$}@} or {@{$$Y_{i}=(B_{0}+B_{1}T_{i}+B_{2}T_{i}^{2})+\alpha \sin( \omega T_{i}+\phi )+E_{i}$$}@} <!--SR:!2026-01-16,151,310!2026-05-17,249,330!2026-05-06,240,330!2025-09-20,65,310!2026-05-30,259,330!2026-06-03,262,330-->

### good starting value for frequency

{@{The starting value for the frequency}@} can be obtained from {@{the dominant frequency in a [periodogram](periodogram.md)}@}. {@{A [complex demodulation](complex%20demodulation.md) phase plot}@} can be used to {@{refine this initial estimate for the frequency}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> <!--SR:!2026-06-06,264,330!2026-05-21,252,330!2026-05-18,250,330!2025-09-22,67,310-->

### good starting values for amplitude

{@{The [root mean square](root%20mean%20square.md) of the detrended data}@} can be {@{scaled by the square root of two to obtain an estimate of the sinusoid amplitude}@}. \(annotation: This is because {@{the squared amplitude of a sinusoid is 2 times its mean square}@}.\) {@{A complex demodulation amplitude plot}@} can be used to {@{find a good starting value for the amplitude}@}. In addition, this plot can indicate {@{whether or not the amplitude is constant over the entire range of the data or if it varies}@}. If {@{the plot is essentially flat, i.e., zero slope}@}, then it is {@{reasonable to assume a constant amplitude in the non-linear model}@}. However, if {@{the slope varies over the range of the plot}@}, one may need to adjust the model to be: {@{$$Y_{i}=C+(B_{0}+B_{1}T_{i})\sin( \omega T_{i}+\phi )+E_{i}$$}@} <!--SR:!2025-09-21,66,310!2026-05-13,246,330!2026-05-22,253,330!2026-05-16,248,330!2026-06-05,263,330!2026-06-16,272,330!2026-05-12,245,330!2026-06-12,269,330!2026-05-02,237,330!2025-11-06,84,365-->

That is, one may {@{replace α with a function of time}@}. {@{A linear fit}@} is specified in the model above, but this can be {@{replaced with a more elaborate function if needed}@}. <!--SR:!2026-04-26,231,330!2026-06-16,272,330!2025-09-19,64,310-->

## model validation

As with {@{any [statistical model](statistical%20model.md)}@}, the fit should be {@{subjected to graphical and quantitative techniques of [model validation](model%20validation.md)}@}. For example, {@{a [run sequence plot](run%20sequence%20plot.md)}@} to check for {@{significant shifts in location, scale, start-up effects and [outliers](outliers.md)}@}. {@{A [lag plot](lag%20plot.md)}@} can be used to {@{verify the [residuals](errors%20and%20residuals%20in%20statistics.md) are independent}@}. {@{The outliers}@} also {@{appear in the lag plot}@}, and {@{a [histogram](histogram.md) and [normal probability plot](normal%20probability%20plot.md)}@} to check for {@{skewness or other non-[normality](normal%20distribution.md) in the residuals}@}. <!--SR:!2025-09-21,66,310!2025-09-18,63,310!2026-04-28,233,330!2026-05-23,254,330!2025-09-20,65,310!2026-06-11,268,330!2026-05-26,255,330!2026-05-24,254,330!2026-05-19,251,330!2026-06-18,274,330-->

## extensions

A different method consists in {@{transforming the non-linear regression to a linear regression thanks to a convenient integral equation}@}. Then, there is {@{no need for initial guess and no need for iterative process}@} : the fitting is {@{directly obtained}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2026-05-04,238,330!2025-09-18,63,310!2026-05-22,252,330-->

## see also

- [Pitch detection algorithm](pitch%20detection%20algorithm.md)
- [Spectral density estimation § Single tone](spectral%20density%20estimation.md#single%20tone)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/sinusoidal_model) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. The method is explained in the chapter "Generalized sinusoidal regression" pp.54-63 in the paper: [\[1\]](https://fr.scribd.com/doc/14674814/Regressions-et-equations-integrales) <a id="^ref-1"></a>^ref-1

## external links

- [Beam deflection case study](http://www.itl.nist.gov/div898/handbook/eda/section4/eda425.htm)

![Public Domain](../../archives/Wikimedia%20Commons/PD-icon.svg) This article incorporates [public domain material](Copyright%20status%20of%20works%20by%20the%20federal%20government%20of%20the%20United%20States.md) from the [National Institute of Standards and Technology](https://www.nist.gov/)

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Regression with time series structure](https://en.wikipedia.org/wiki/Category:Regression%20with%20time%20series%20structure)
> - [Regression models](https://en.wikipedia.org/wiki/Category:Regression%20models)
