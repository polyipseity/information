---
aliases:
  - method of moments
  - method of moments (statistics)
  - methods of moments
  - methods of moments (statistics)
tags:
  - flashcard/active/general/eng/method_of_moments__statistics_
  - language/in/English
---

# method of moments

<!-- | ![](../../archives/Wikimedia%20Commons/Question%20book-new.svg) | This article __needs additional citations for [verification](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)__. Please help [improve this article](https://en.wikipedia.org/wiki/Special:EditPage/Method%20of%20moments%20%28statistics%29) by [adding citations to reliable sources](https://en.wikipedia.org/wiki/Help:Referencing%20for%20beginners). Unsourced material may be challenged and removed._Find sources:_ ["Method of moments" statistics](https://www.google.com/search?as_eq=wikipedia&q=%22Method+of+moments%22+statistics) – [news](https://www.google.com/search?tbm=nws&q=%22Method+of+moments%22+statistics+-wikipedia&tbs=ar:1) __·__ [newspapers](https://www.google.com/search?&q=%22Method+of+moments%22+statistics&tbs=bkt:s&tbm=bks) __·__ [books](https://www.google.com/search?tbs=bks:1&q=%22Method+of+moments%22+statistics+-wikipedia) __·__ [scholar](https://scholar.google.com/scholar?q=%22Method+of+moments%22+statistics) __·__ [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Method+of+moments%22+statistics&acc=on&wc=on) _\(June 2020\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

- For {@{the technique used to prove [convergence in distribution](convergence%20of%20random%20variables.md#convergence%20in%20distribution)}@}, see {@{[Method of moments \(probability theory\)](method%20of%20moments%20(probability%20theory).md)}@}. <!--SR:!2025-09-01,186,310!2025-08-16,173,310-->

In {@{[statistics](statistics.md)}@}, {@{the __method of moments__}@} is {@{a method of [estimation](estimation.md) of population [parameters](statistical%20parameter.md)}@}. The same principle is used to {@{derive higher moments like skewness and kurtosis}@}. <!--SR:!2025-07-15,149,310!2025-03-21,64,310!2025-09-09,193,310!2025-03-22,65,310-->

It starts by {@{expressing the population [moments](moment%20(mathematics).md) \(i.e., the [expected values](expected%20value.md) of powers of the [random variable](random%20variable.md) under consideration\) as functions of the parameters of interest}@}. Those expressions are then {@{set equal to the sample moments}@}. {@{The number of such equations}@} is {@{the same as the number of parameters to be estimated}@}. Those equations are then {@{solved for the parameters of interest}@}. The solutions are {@{estimates of those parameters}@}. <!--SR:!2025-07-01,125,290!2025-08-23,178,310!2025-03-24,67,310!2025-03-16,60,310!2025-03-19,63,310!2025-03-22,65,310-->

The method of moments was introduced by {@{[Pafnuty Chebyshev](Pafnuty%20Chebyshev.md) in 1887}@} in {@{the proof of the [central limit theorem](central%20limit%20theorem.md)}@}. The idea of {@{matching empirical moments of a distribution to the population moments}@} dates back {@{at least to [Karl Pearson](Karl%20Pearson.md)}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-04-05,63,250!2025-05-22,104,290!2025-03-21,64,310!2025-08-14,171,310-->

## method

Suppose that {@{the parameter $\theta$ = \($\theta _{1},\theta _{2},\dots ,\theta _{k}$\)}@} {@{characterizes the [distribution](probability%20distribution.md) $f_{W}(w;\theta )$ of the random variable $W$}@}.<sup>[\[1\]](#^ref-1)</sup> Suppose {@{the first $k$ moments of the true distribution \(the "population moments"\) can be expressed as functions of the $\theta$s}@}: {@{$${\begin{aligned}\mu _{1}&\equiv \operatorname {E} [W]=g_{1}(\theta _{1},\theta _{2},\ldots ,\theta _{k}),\\[4pt]\mu _{2}&\equiv \operatorname {E} [W^{2}]=g_{2}(\theta _{1},\theta _{2},\ldots ,\theta _{k}),\\&\,\,\,\vdots \\\mu _{k}&\equiv \operatorname {E} [W^{k}]=g_{k}(\theta _{1},\theta _{2},\ldots ,\theta _{k}).\end{aligned} }$$}@} Suppose {@{a sample of size $n$ is drawn, resulting in the values $w_{1},\dots ,w_{n}$}@}. For {@{$j=1,\dots ,k$, let $${\widehat {\mu } }_{j}={\frac {1}{n} }\sum _{i=1}^{n}w_{i}^{j}$$}@} be {@{the _j_-th sample moment, an estimate of $\mu _{j}$}@}. The method of moments estimator for $\theta _{1},\theta _{2},\ldots ,\theta _{k}$ denoted by {@{${\widehat {\theta } }_{1},{\widehat {\theta } }_{2},\dots ,{\widehat {\theta } }_{k}$}@} is defined to be {@{the solution \(if one exists\) to the equations}@}:<sup>[\[2\]](#^ref-2)</sup> {@{$${\begin{aligned}{\widehat {\mu } }_{1}&=g_{1}({\widehat {\theta } }_{1},{\widehat {\theta } }_{2},\ldots ,{\widehat {\theta } }_{k}),\\[4pt]{\widehat {\mu } }_{2}&=g_{2}({\widehat {\theta } }_{1},{\widehat {\theta } }_{2},\ldots ,{\widehat {\theta } }_{k}),\\&\,\,\,\vdots \\{\widehat {\mu } }_{k}&=g_{k}({\widehat {\theta } }_{1},{\widehat {\theta } }_{2},\ldots ,{\widehat {\theta } }_{k}).\end{aligned} }$$}@} <!--SR:!2025-03-16,60,310!2025-03-11,56,310!2025-03-10,55,310!2025-03-19,63,310!2025-03-10,55,310!2025-03-13,58,310!2025-03-22,65,310!2025-03-17,61,310!2025-03-23,66,310!2025-03-22,65,310-->

{@{The method described here for single random variables}@} generalizes {@{in an obvious manner to multiple random variables}@} leading to {@{multiple choices for moments to be used}@}. Different choices {@{generally lead to different solutions}@}.<sup>[\[5\]](#^ref-5)</sup><sup>[\[6\]](#^ref-6)</sup> <!--SR:!2025-03-23,66,310!2025-03-18,62,310!2025-03-23,66,310!2025-03-12,57,310-->

## advantages and disadvantages

The method of moments is {@{fairly simple}@} and {@{yields [consistent estimators](consistent%20estimator.md) \(under very weak assumptions\)}@}, though {@{these estimators are often [biased](bias%20of%20an%20estimator.md)}@}. <!--SR:!2025-03-11,56,310!2025-07-17,150,310!2025-03-10,55,310-->

It is an alternative to {@{the [method of maximum likelihood](maximum%20likelihood%20estimation.md)}@}. <!--SR:!2025-03-15,59,310-->

However, in some cases {@{the likelihood equations may be intractable without computers}@}, whereas {@{the method-of-moments estimators can be computed much more quickly and easily}@}. Due to {@{easy computability}@}, method-of-moments estimates may be {@{used as the first approximation to the solutions of the likelihood equations}@}, and {@{successive improved approximations may then be found}@} by {@{the [Newton–Raphson method](Newton's%20method.md)}@}. In this way {@{the method of moments can assist in finding maximum likelihood estimates}@}. <!--SR:!2025-03-09,54,310!2025-03-12,57,310!2025-03-22,65,310!2025-03-17,61,310!2025-03-21,64,310!2025-09-05,185,310!2025-08-08,166,310-->

In some cases, {@{infrequent with large samples but less infrequent with small samples}@}, the estimates given by the method of moments are {@{outside of the parameter space}@} \(as shown in the example below\); it {@{does not make sense to rely on them then}@}. That problem {@{never arises in the method of [maximum likelihood](maximum%20likelihood%20estimation.md)}@}.<sup>[\[3\]](#^ref-3)</sup> Also, estimates by the method of moments are not {@{necessarily [sufficient statistics](sufficient%20statistic.md), i.e., they sometimes fail to take into account all relevant information in the sample}@}. <!--SR:!2025-09-08,192,310!2025-03-24,67,310!2025-03-24,67,310!2025-03-12,57,310!2025-03-12,57,310-->

When {@{estimating other structural parameters}@} \(e.g., {@{parameters of a [utility function](utility.md), instead of parameters of a known probability distribution}@}\), {@{appropriate probability distributions may not be known}@}, and {@{moment-based estimates may be preferred to maximum likelihood estimation}@}. <!--SR:!2025-03-16,60,310!2025-09-09,189,310!2025-06-12,120,290!2025-03-24,67,310-->

## alternative method of moments

The equations to be solved in the method of moments \(MoM\) are {@{in general nonlinear and there are no generally applicable guarantees that tractable solutions exist}@}.<!-- <sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> --> But there is {@{an alternative approach to using sample moments to estimate data model parameters}@} in terms of {@{known dependence of model moments on these parameters}@}, and this alternative requires {@{the solution of only linear equations or, more generally, tensor equations}@}. This alternative is referred to as {@{the Bayesian-Like MoM \(BL-MoM\)}@}, and it differs from the classical MoM in that {@{it uses optimally weighted sample moments}@}. Considering that {@{the MoM is typically motivated by a lack of sufficient knowledge about the data model}@} to {@{determine likelihood functions and associated _a posteriori_ probabilities of unknown or random parameters}@}, it is odd that {@{there exists a type of MoM that is _Bayesian-Like_}@}. But the particular meaning of _Bayesian-Like_ leads to {@{a problem formulation in which required knowledge of _a posteriori_ probabilities}@} is replaced with {@{required knowledge of only the dependence of model moments on unknown model parameters}@}, which is {@{exactly the knowledge required by the traditional MoM}@}.<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup><sup>[\[5\]](#^ref-5)</sup><sup>[\[6\]](#^ref-6)</sup><sup>[\[7\]](#^ref-7)</sup><sup>[\[8\]](#^ref-8)</sup><sup>[\[9\]](#^ref-9)</sup> The BL-MoM also uses {@{knowledge of _a priori_ probabilities of the parameters to be estimated, when available}@}, but {@{otherwise uses uniform priors}@}.<!-- <sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> --> <!--SR:!2025-08-30,184,310!2025-07-12,146,310!2025-08-25,180,310!2025-08-24,179,310!2025-03-13,58,310!2025-03-18,62,310!2025-03-21,64,310!2025-05-05,85,270!2025-06-28,125,290!2025-03-15,59,310!2025-03-24,67,310!2025-07-13,147,310!2025-09-09,193,310!2025-03-23,66,310-->

The BL-MoM has been reported on in only {@{the applied statistics literature in connection with parameter estimation and hypothesis testing}@} using {@{observations of stochastic processes for problems in Information and Communications Theory}@} and, in particular, {@{communications receiver design in the absence of knowledge of likelihood functions or associated _a posteriori_ probabilities}@}<sup>[\[10\]](#^ref-10)</sup> and references therein. In addition, {@{the restatement of this receiver design approach for stochastic process models}@} as an alternative to the classical MoM for any type of multivariate data is available in tutorial form at the university website.<sup>[\[11, page 11.4\]](#^ref-11)</sup> The applications in [\[10\]](#^ref-10) and references demonstrate {@{some important characteristics of this alternative to the classical MoM}@}, and a detailed list of relative advantages and disadvantages is given in [\[11, page 11.4\]](#^ref-11), but the literature is missing {@{direct comparisons in specific applications of the classical MoM and the BL-MoM}@}.<!-- <sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> --> <!--SR:!2025-03-11,56,310!2025-03-22,65,310!2025-03-13,58,310!2025-03-09,54,310!2025-08-15,172,310!2025-03-09,54,310-->

## examples

An example application of the method of moments is to {@{estimate polynomial probability density distributions}@}. In this case, {@{an approximating polynomial of order $N$ is defined on an interval $[a,b]$}@}. The method of moments then {@{yields a system of equations}@}, whose solution involves {@{the inversion of a [Hankel matrix](Hankel%20matrix.md)}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-03-18,62,310!2025-06-08,111,290!2025-03-10,55,310!2025-08-17,176,310-->

### proving the central limit theorem

<!-- | ![](../../archives/Wikimedia%20Commons/System-search.svg) | This section's __factual accuracy is [disputed](https://en.wikipedia.org/wiki/Wikipedia:Accuracy%20dispute)__. Relevant discussion may be found on the [talk page](https://en.wikipedia.org/wiki/Talk:Method%20of%20moments%20%28statistics%29#Chebyshev%20proof). Please help to ensure that disputed statements are [reliably sourced](https://en.wikipedia.org/wiki/Wikipedia:Reliable%20sources). _\(October 2024\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

Let {@{$X_{1},X_{2},\cdots$ be independent random variables with mean 0 and variance 1}@}, then let {@{$S_{n}:={\frac {1}{\sqrt {n} } }\sum _{i=1}^{n}X_{i}$}@}. We can compute {@{the moments of $S_{n}$ as $n \to \infty$ as $$E[S_{n}^{0}]=1,E[S_{n}^{1}]=0,E[S_{n}^{2}]=1,E[S_{n}^{3}]=0,\cdots$$}@} Explicit expansion shows that {@{$$E[S_{n}^{2k+1}]=0;\quad E[S_{n}^{2k}]={\frac { {\binom {n}{k} }{\frac {(2k)!}{2^{k} } } }{n^{k} } }={\frac {n(n-1)\cdots (n-k+1)}{n^{k} } }(2k-1)!!$$}@} where the numerator is {@{the number of ways to select $k$ distinct pairs of balls by picking one each from $2k$ buckets, each containing balls numbered from $1$ to $n$}@}. (annotation: Alternatively, {@{$\frac {(2k)!} {2^k k!}$ is the number of ways to pair up $2k$ buckets, and $P(n, k) = \binom n k k!$ is the number of ways to assign numbers from $1$ to $n$ to the $k$ pairs}@}. Multiplying them gives up the numerator.) At {@{the $n\to \infty$ limit}@}, {@{all moments converge to that of a standard normal distribution}@}. More analysis then show that {@{this convergence in moments imply a convergence in distribution}@}. <!--SR:!2025-03-18,62,310!2025-06-28,123,290!2025-03-24,67,310!2025-03-12,28,230!2025-07-11,134,290!2025-05-03,81,270!2025-08-09,167,310!2025-03-16,60,310!2025-06-13,115,290-->

{@{Essentially this argument}@} was published {@{by Chebyshev in 1887}@}.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2025-07-26,158,310!2025-05-21,103,290-->

### uniform distribution

Consider {@{the [uniform distribution](continuous%20uniform%20distribution.md) on the interval $[a,b]$, $U(a,b)$}@}. If $W\sim U(a,b)$ then we have {@{$$\mu _{1}=\operatorname {E} [W]={\frac {1}{2} }(a+b)$$ <br/> $$\mu _{2}=\operatorname {E} [W^{2}]={\frac {1}{3} }(a^{2}+ab+b^{2})$$}@} Solving these equations gives {@{$${\widehat {a} }=\mu _{1}-{\sqrt {3\left(\mu _{2}-\mu _{1}^{2}\right)} }$$ <br/> $${\widehat {b} }=\mu _{1}+{\sqrt {3\left(\mu _{2}-\mu _{1}^{2}\right)} }$$}@} Given {@{a set of samples $\{w_{i}\}$}@} we can {@{use the sample moments ${\widehat {\mu } }_{1}$ and ${\widehat {\mu } }_{2}$ in these formulae in order to estimate $a$ and $b$}@}. <!--SR:!2025-03-17,61,310!2025-07-13,148,310!2025-03-24,53,250!2025-03-19,63,310!2025-08-05,162,310-->

Note, however, that {@{this method can produce inconsistent results in some cases}@}. For example, {@{the set of samples $\{0,0,0,0,1\}$}@} results in {@{the estimate ${\widehat {a} }={\frac {1}{5} }-{\frac {2{\sqrt {3} } }{5} },{\widehat {b} }={\frac {1}{5} }+{\frac {2{\sqrt {3} } }{5} }$}@} even though {@{${\widehat {b} }<1$}@} and so {@{it is impossible for the set $\{0,0,0,0,1\}$ to have been drawn from $U({\widehat {a} },{\widehat {b} })$ in this case}@}. <!--SR:!2025-03-15,59,310!2025-03-23,66,310!2025-05-10,89,270!2025-08-17,174,310!2025-03-19,63,310-->

## see also

- [Generalized method of moments](generalized%20method%20of%20moments.md)
- [Decoding methods](decoding%20methods.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/method_of_moments_(statistics)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. [Kimiko O. Bowman](Kimiko%20O.%20Bowman.md) and L. R. Shenton, "Estimator: Method of Moments", pp 2092–2098, _Encyclopedia of statistical sciences_, Wiley \(1998\). <a id="^ref-1"></a>^ref-1
2. J. Munkhammar, L. Mattsson, J. Rydén \(2017\) "Polynomial probability distribution estimation using the method of moments". PLoS ONE 12\(4\): e0174573. [https://doi.org/10.1371/journal.pone.0174573](https://doi.org/10.1371/journal.pone.0174573) <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFFischer2011"></a> Fischer, Hans \(2011\). "4. Chebyshev's and Markov's Contributions". [_History of the central limit theorem : from classical to modern probability theory_](https://www.worldcat.org/oclc/682910965). New York: Springer. [ISBN](ISBN.md) [978-0-387-87857-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-87857-7). [OCLC](OCLC.md#OCLC) [682910965](https://search.worldcat.org/oclc/682910965). <a id="^ref-3"></a>^ref-3

### references needing to be wikified

- \[4\] Pearson, K. \(1936\), "Method of Moments and Method of Maximum Likelihood", _Biometrika_ 28\(1/2\), 35–59. <a id="^ref-4"></a>^ref-4
- \[5\] Lindsay, B.G. & Basak P. \(1993\). "Multivariate normal mixtures: a fast consistent method of moments", _Journal of the American Statistical Association_ __88__, 468–476. <a id="^ref-5"></a>^ref-5
- \[6\] Quandt, R.E. & Ramsey, J.B. \(1978\). "Estimating mixtures of normal distributions and switching regressions", _Journal of the American Statistical Association_ __73__, 730–752. <a id="^ref-6"></a>^ref-6
- \[7\] <https://real-statistics.com/distribution-fitting/method-of-moments/> <a id="^ref-7"></a>^ref-7
- \[8\] Hansen, L. \(1982\). "Large sample properties of generalized method of moments estimators", _Econometrica_ __50__, 1029–1054. <a id="^ref-8"></a>^ref-8
- \[9\] Lindsay, B.G. \(1982\). "Conditional score functions: some optimality results", _Biometrika_ __69__, 503–512. <a id="^ref-9"></a>^ref-9
- \[10\] Gardner, W.A., "Design of nearest prototype signal classifiers", _IEEE Transactions on Information Theory_ 27 \(3\), 368–372,1981 <a id="^ref-10"></a>^ref-10
- \[11\] [Cyclostationarity](https://cyclostationarity.com/) <a id="^ref-11"></a>^ref-11

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Probability distribution fitting](https://en.wikipedia.org/wiki/Category:Probability%20distribution%20fitting)
> - [Moment \(mathematics\)](https://en.wikipedia.org/wiki/Category:Moment%20%28mathematics%29)
