---
aliases:
  - MGF
  - MGFs
  - moment generating function
  - moment generating functions
  - moment-generating function
  - moment-generating functions
tags:
  - flashcard/active/general/eng/moment-generating_function
  - language/in/English
---

# moment-generating function

In {@{[probability theory](probability%20theory.md) and [statistics](statistics.md)}@}, {@{the __moment-generating function__}@} of {@{a real-valued [random variable](random%20variable.md) is an alternative specification of its [probability distribution](probability%20distribution.md)}@}. Thus, it provides {@{the basis of an alternative route to analytical results compared with working directly with [probability density functions](probability%20density%20function.md) or [cumulative distribution functions](cumulative%20distribution%20function.md)}@}. There are {@{particularly simple results}@} for {@{the moment-generating functions of distributions defined by the weighted sums of random variables}@}. However, {@{not all random variables have moment-generating functions}@}.

As {@{its name implies}@}, the moment-[generating function](generating%20function.md) can be {@{used to compute a distribution’s [moments](moment%20(mathematics).md)}@}: {@{the _n_<!-- markdown separator -->th moment about 0 is the _n_<!-- markdown separator -->th derivative of the moment-generating function, evaluated at 0}@}.

In addition to {@{real-valued distributions \(univariate distributions\)}@}, moment-generating functions can be {@{defined for vector- or matrix-valued random variables, and can even be extended to more general cases}@}.

The moment-generating function of a real-valued distribution {@{does not always exist, unlike the [characteristic function](characteristic%20function%20(probability%20theory).md)}@}. There are relations between {@{the behavior of the moment-generating function of a distribution and properties of the distribution}@}, such as {@{the existence of moments}@}.

## definition

Let {@{$X$ be a [random variable](random%20variable.md) with [CDF](cumulative%20distribution%20function.md) $F_{X}$}@}. {@{The moment generating function \(mgf\) of $X$ \(or $F_{X}$\), denoted by $M_{X}(t)$}@}, is {@{$$M_{X}(t)=\operatorname {E} \left[e^{tX}\right]$$}@} provided {@{this [expectation](expected%20value.md) exists for $t$ in some open [neighborhood](neighborhood%20(mathematics).md) of 0}@}. That is, there is {@{an $h>0$ such that for all $t$ in $-h<t<h$, $\operatorname {E} \left[e^{tX}\right]$ exists}@}. If {@{the expectation does not exist in an open neighborhood of 0}@}, we say that {@{the moment generating function does not exist}@}.<sup>[\[1\]](#^ref-1)</sup>

In other words, {@{the moment-generating function of _X_}@} is {@{the [expectation](expected%20value.md) of the random variable $e^{tX}$}@}. More generally, when {@{$\mathbf {X} =(X_{1},\ldots ,X_{n})^{\mathrm {T} }$, an $n$-dimensional [random vector](random%20vector.md), and $\mathbf {t}$ is a fixed vector}@}, one {@{uses $\mathbf {t} \cdot \mathbf {X} =\mathbf {t} ^{\mathrm {T} }\mathbf {X}$ instead of $tX$}@}: {@{$$M_{\mathbf {X} }(\mathbf {t} ):=\operatorname {E} \left(e^{\mathbf {t} ^{\mathrm {T} }\mathbf {X} }\right).$$}@} {@{$M_{X}(0)$ always exists}@} and {@{is equal to 1}@}. However, {@{a key problem with moment-generating functions}@} is that {@{moments and the moment-generating function may not exist}@}, as {@{the integrals need not converge absolutely}@}. By contrast, {@{the [characteristic function](characteristic%20function%20(probability%20theory).md) or Fourier transform}@} {@{always exists \(because it is the integral of a bounded function on a space of finite [measure](measure%20(mathematics).md)\)}@}, and {@{for some purposes may be used instead}@}.

{@{The moment-generating function is so named}@} because {@{it can be used to find the moments of the distribution}@}.<sup>[\[2\]](#^ref-2)</sup> {@{The series expansion of $e^{tX}$}@} is {@{$$e^{t\,X}=1+t\,X+{\frac {t^{2}\,X^{2} }{2!} }+{\frac {t^{3}\,X^{3} }{3!} }+\cdots +{\frac {t^{n}\,X^{n} }{n!} }+\cdots .$$}@} Hence {@{$${\begin{aligned}M_{X}(t)=\operatorname {E} (e^{t\,X})&=1+t\operatorname {E} (X)+{\frac {t^{2}\operatorname {E} (X^{2})}{2!} }+{\frac {t^{3}\operatorname {E} (X^{3})}{3!} }+\cdots +{\frac {t^{n}\operatorname {E} (X^{n})}{n!} }+\cdots \\&=1+tm_{1}+{\frac {t^{2}m_{2} }{2!} }+{\frac {t^{3}m_{3} }{3!} }+\cdots +{\frac {t^{n}m_{n} }{n!} }+\cdots ,\end{aligned} }$$}@} where {@{$m_{n}$ is the $n$<!-- LaTeX separator -->th [moment](moment%20(mathematics).md)}@}. {@{Differentiating $M_{X}(t)$ $i$ times with respect to $t$ and setting $t=0$}@}, we {@{obtain the $i$<!-- LaTeX separator -->th moment about the origin, $m_{i}$; see [Calculations of moments](#calculations%20of%20moments) below}@}.

If {@{$X$ is a continuous random variable}@}, the following {@{relation between its moment-generating function $M_{X}(t)$ and the [two-sided Laplace transform](two-sided%20Laplace%20transform.md) of its probability density function $f_{X}(x)$ holds}@}: {@{$$M_{X}(t)={\mathcal {L} }\{f_{X}\}(-t),$$}@} since {@{the PDF's two-sided Laplace transform}@} is given as {@{$${\mathcal {L} }\{f_{X}\}(s)=\int _{-\infty }^{\infty }e^{-sx}f_{X}(x)\,dx,$$}@} and {@{the moment-generating function's definition expands \(by the [law of the unconscious statistician](law%20of%20the%20unconscious%20statistician.md)\)}@} to {@{$$M_{X}(t)=\operatorname {E} \left[e^{tX}\right]=\int _{-\infty }^{\infty }e^{tx}f_{X}(x)\,dx.$$}@} This is {@{consistent with the characteristic function of $X$ being a [Wick rotation](Wick%20rotation.md) of $M_{X}(t)$}@} when {@{the moment generating function exists}@}, as the characteristic function of a continuous random variable $X$ is {@{the [Fourier transform](Fourier%20transform.md) of its probability density function $f_{X}(x)$}@}, and in general when {@{a function $f(x)$ is of [exponential order](exponential%20order.md)}@}, {@{the Fourier transform of $f$ is a Wick rotation of its two-sided Laplace transform in the region of convergence}@}. See {@{[the relation of the Fourier and Laplace transforms](Fourier%20transform.md#Laplace%20transform)}@} for further information.

## examples

Here are {@{some examples of the moment-generating function and the characteristic function for comparison}@}. It can be seen that {@{the characteristic function is a [Wick rotation](Wick%20rotation.md) of the moment-generating function $M_{X}(t)$ when the latter exists}@}.

| Distribution                                                                                                                                                                                    | Moment-generating function $M_{X}(t)$                                                                               | Characteristic function $\varphi (t)$                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [Degenerate](degenerate%20distribution.md) $\delta _{a}$                                                                                                                                        | $e^{ta}$                                                                                                            | $e^{ita}$                                                                                                                               |
| [Bernoulli](Bernoulli%20distribution.md) $P(X=1)=p$                                                                                                                                             | $1-p+pe^{t}$                                                                                                        | $1-p+pe^{it}$                                                                                                                           |
| [Binomial](binomial%20distribution.md) $B(n,p)$                                                                                                                                                 | $\left(1-p+pe^{t}\right)^{n}$                                                                                       | $\left(1-p+pe^{it}\right)^{n}$                                                                                                          |
| [Geometric](geometric%20distribution.md) $(1-p)^{k}\,p$ \(unshifted\)                                                                                                                           | ${\frac {p}{1-(1-p)e^{t} } },~t<-\ln(1-p)$ \(shifted: multiply by $e^t$\)                                           | ${\frac {p}{1-(1-p)\,e^{it} } }$ \(shifted: multiply by $e^{it}$\)                                                                      |
| [Negative binomial](negative%20binomial%20distribution.md) $\operatorname {NB} (r,p)$                                                                                                           | $\left({\frac {p}{1-e^{t}+pe^{t} } }\right)^{r},~t<-\ln(1-p)$                                                       | $\left({\frac {p}{1-e^{it}+pe^{it} } }\right)^{r}$                                                                                      |
| [Poisson](Poisson%20distribution.md) $\operatorname {Pois} (\lambda )$                                                                                                                          | $e^{\lambda (e^{t}-1)}$                                                                                             | $e^{\lambda (e^{it}-1)}$                                                                                                                |
| [Uniform \(continuous\)](uniform%20distribution%20(continuous).md) $\operatorname {U} (a,b)$                                                                                                    | ${\frac {e^{tb}-e^{ta} }{t(b-a)} }$                                                                                 | ${\frac {e^{itb}-e^{ita} }{it(b-a)} }$                                                                                                  |
| [Uniform \(discrete\)](discrete%20uniform%20distribution.md) $\operatorname {DU} (a,b)$                                                                                                         | ${\frac {e^{at}-e^{(b+1)t} }{(b-a+1)(1-e^{t})} }$                                                                   | ${\frac {e^{ait}-e^{(b+1)it} }{(b-a+1)(1-e^{it})} }$                                                                                    |
| [Laplace](laplace%20distribution.md) $L(\mu ,b)$                                                                                                                                                | ${\frac {e^{t\mu } }{1-b^{2}t^{2} } },~\lvert t \rvert<1/b$                                                         | ${\frac {e^{it\mu } }{1+b^{2}t^{2} } }$                                                                                                 |
| [Normal](normal%20distribution.md) $N(\mu ,\sigma ^{2})$                                                                                                                                        | $e^{t\mu +{\frac {1}{2} }\sigma ^{2}t^{2} }$                                                                        | $e^{it\mu -{\frac {1}{2} }\sigma ^{2}t^{2} }$                                                                                           |
| [Chi-squared](chi-squared%20distribution.md) $\chi _{k}^{2}$                                                                                                                                    | $(1-2t)^{-{\frac {k}{2} } },~t<1/2$                                                                                 | $(1-2it)^{-{\frac {k}{2} } }$                                                                                                           |
| [Noncentral chi-squared](noncentral%20chi-squared%20distribution.md) $\chi _{k}^{2}(\lambda )$                                                                                                  | $e^{\lambda t/(1-2t)}(1-2t)^{-{\frac {k}{2} } }$                                                                    | $e^{i\lambda t/(1-2it)}(1-2it)^{-{\frac {k}{2} } }$                                                                                     |
| [Gamma](gamma%20distribution.md) $\Gamma (k,{\tfrac {1}{\theta } })$                                                                                                                            | $(1-t\theta )^{-k},~t<{\tfrac {1}{\theta } }$                                                                       | $(1-it\theta )^{-k}$                                                                                                                    |
| [Exponential](exponential%20distribution.md) $\operatorname {Exp} (\lambda )$                                                                                                                   | $\left(1-t\lambda ^{-1}\right)^{-1},~t<\lambda$                                                                     | $\left(1-it\lambda ^{-1}\right)^{-1}$                                                                                                   |
| [Beta](beta%20distribution.md)                                                                                                                                                                  | $1+\sum _{k=1}^{\infty }\left(\prod _{r=0}^{k-1}{\frac {\alpha +r}{\alpha +\beta +r} }\right){\frac {t^{k} }{k!} }$ | ${}_{1}F_{1}(\alpha ;\alpha +\beta ;i\,t)\!$ \(see [Confluent hypergeometric function](confluent%20hypergeometric%20function.md)\)      |
| [Multivariate normal](multivariate%20normal%20distribution.md) $N(\boldsymbol {\mu } ,\mathbf {\Sigma } )$                                                                                      | $e^{\mathbf {t} ^{\mathrm {T} }\left({\boldsymbol {\mu } }+{\frac {1}{2} }\mathbf {\Sigma t} \right)}$              | $e^{\mathbf {t} ^{\mathrm {T} }\left(i{\boldsymbol {\mu } }-{\frac {1}{2} }{\boldsymbol {\Sigma } }\mathbf {t} \right)}$                |
| [Cauchy](Cauchy%20distribution.md) $\operatorname {Cauchy} (\mu ,\theta )$                                                                                                                      | [Does not exist](indeterminate%20form.md)                                                                           | $e^{it\mu -\theta \lvert t \rvert}$                                                                                                     |
| [Multivariate Cauchy](multivariate%20Cauchy%20distribution.md#multivariate%20Cauchy%20distribution) $\operatorname {MultiCauchy} (\boldsymbol \mu ,\mathbf \Sigma )$<sup>[\[3\]](#^ref-3)</sup> | Does not exist                                                                                                      | $\!\,e^{i\mathbf {t} ^{\mathrm {T} }{\boldsymbol {\mu } }-{\sqrt {\mathbf {t} ^{\mathrm {T} }{\boldsymbol {\Sigma } }\mathbf {t} } } }$ |

> __flashcards__
>
> - [degenerate](degenerate%20distribution.md) $\delta _{a}$ ::@:: $M_X(t) = e^{ta}$, $\varphi_X(t) = e^{ita}$
> - [Bernoulli](Bernoulli%20distribution.md) $P(X=1)=p$ ::@:: $M_X(t) = 1-p+pe^{t}$, $\varphi_X(t) = 1-p+pe^{it}$
> - [binomial](binomial%20distribution.md) $B(n,p)$ ::@:: $M_X(t) = \left(1-p+pe^{t}\right)^{n}$, $\varphi_X(t) = \left(1-p+pe^{it}\right)^{n}$
> - [Poisson](Poisson%20distribution.md) $\operatorname {Pois} (\lambda )$ ::@:: $M_X(t) = e^{\lambda (e^{t}-1)}$, $\varphi_X(t) = e^{\lambda (e^{it}-1)}$
> - [uniform \(continuous\)](uniform%20distribution%20(continuous).md) $\operatorname {U} (a,b)$ ::@:: $M_X(t) = {\frac {e^{tb}-e^{ta} }{t(b-a)} }$, $\varphi_X(t) = {\frac {e^{itb}-e^{ita} }{it(b-a)} }$
> - [normal](normal%20distribution.md) $N(\mu ,\sigma ^{2})$ ::@:: $M_X(t) = e^{t\mu +{\frac {1}{2} }\sigma ^{2}t^{2} }$, $\varphi_X(t) = e^{it\mu -{\frac {1}{2} }\sigma ^{2}t^{2} }$
> - [multivariate normal](multivariate%20normal%20distribution.md) $N(\boldsymbol {\mu } ,\mathbf {\Sigma } )$ ::@:: $M_X(\mathbf t) = e^{\mathbf {t} ^{\mathrm {T} }\left({\boldsymbol {\mu } }+{\frac {1}{2} }\mathbf {\Sigma t} \right)}$, $\varphi_X(\mathbf t) = e^{\mathbf {t} ^{\mathrm {T} }\left(i{\boldsymbol {\mu } }-{\frac {1}{2} }{\boldsymbol {\Sigma } }\mathbf {t} \right)}$
> - examples of distribution without moment-generating function ::@:: [Cauchy](Cauchy%20distribution.md) $\operatorname {Cauchy} (\mu ,\theta )$, [multivariate Cauchy](multivariate%20Cauchy%20distribution.md#multivariate%20Cauchy%20distribution) $\operatorname {MultiCauchy} (\boldsymbol \mu , \mathbf \Sigma )$

## calculation

{@{The moment-generating function}@} is {@{the expectation of a function of the random variable}@}, it can be written as:

- For a discrete [probability mass function](probability%20mass%20function.md), ::@:: $M_{X}(t)=\sum _{i=0}^{\infty }e^{tx_{i} }\,p_{i}$
- For a continuous [probability density function](probability%20density%20function.md), ::@:: $M_{X}(t)=\int _{-\infty }^{\infty }e^{tx}f(x)\,dx$
- In the general case: ::@:: $M_{X}(t)=\int _{-\infty }^{\infty }e^{tx}\,dF(x)$, using the [Riemann–Stieltjes integral](Riemann–Stieltjes%20integral.md), and where $F$ is the [cumulative distribution function](cumulative%20distribution%20function.md). This is simply the [Laplace-Stieltjes transform](Laplace-Stieltjes%20transform.md) of $F$, but with the sign of the argument reversed.

Note that for {@{the case where $X$ has a continuous [probability density function](probability%20density%20function.md) $f(x)$}@}, {@{$M_{X}(-t)$ is the [two-sided Laplace transform](two-sided%20Laplace%20transform.md) of $f(x)$}@}. {@{$${\begin{aligned}M_{X}(t)&=\int _{-\infty }^{\infty }e^{tx}f(x)\,dx\\&=\int _{-\infty }^{\infty }\left(1+tx+{\frac {t^{2}x^{2} }{2!} }+\cdots +{\frac {t^{n}x^{n} }{n!} }+\cdots \right)f(x)\,dx\\&=1+tm_{1}+{\frac {t^{2}m_{2} }{2!} }+\cdots +{\frac {t^{n}m_{n} }{n!} }+\cdots ,\end{aligned} }$$}@} where {@{$m_{n}$ is the $n$<!-- LaTeX separator -->th [moment](moment%20(mathematics).md)}@}.

### linear transformations of random variables

If {@{random variable $X$ has moment generating function $M_{X}(t)$}@}, then {@{$\alpha X+\beta$ has moment generating function $M_{\alpha X+\beta }(t)=e^{\beta t}M_{X}(\alpha t)$}@} {@{$$M_{\alpha X+\beta }(t)=E[e^{(\alpha X+\beta )t}]=e^{\beta t}E[e^{\alpha Xt}]=e^{\beta t}M_{X}(\alpha t)$$}@}

### linear combination of independent random variables

If {@{$S_{n}=\sum _{i=1}^{n}a_{i}X_{i}$}@}, where {@{the _X_<sub>_i_</sub> are independent random variables and the _a_<sub>_i_</sub> are constants}@}, then {@{the probability density function for _S_<sub>_n_</sub> is the [convolution](convolution.md) of the probability density functions of each of the _X_<sub>_i_</sub>}@}, and the moment-generating function for _S_<sub>_n_</sub> is given by {@{$$M_{S_{n} }(t)=M_{X_{1} }(a_{1}t)M_{X_{2} }(a_{2}t)\cdots M_{X_{n} }(a_{n}t)\,.$$}@}

### vector-valued random variables

For {@{[vector-valued random variables](random%20vector.md) $\mathbf {X}$ with [real](real%20number.md) components}@}, the moment-generating function is given by {@{$$M_{X}(\mathbf {t} )=E\left(e^{\langle \mathbf {t} ,\mathbf {X} \rangle }\right)$$}@} where {@{$\mathbf {t}$ is a vector and $\langle \cdot ,\cdot \rangle$ is the [dot product](dot%20product.md)}@}.

## important properties

Moment generating functions are {@{positive and [log-convex](logarithmically%20convex%20function.md),<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> with _M_\(0\) = 1}@}.

{@{An important property of the moment-generating function}@} is that {@{it uniquely determines the distribution}@}. In other words, if {@{$X$ and $Y$ are two random variables and for all values of _t_, $$M_{X}(t)=M_{Y}(t),\,$$}@} then {@{$$F_{X}(x)=F_{Y}(x)\,$$ for all values of _x_ \(or equivalently _X_ and _Y_ have the same distribution\)}@}. This statement is {@{not equivalent to the statement "if two distributions have the same moments, then they are identical at all points."}@} This is because {@{in some cases, the moments exist and yet the moment-generating function does not}@}, because {@{the limit $$\lim _{n\rightarrow \infty }\sum _{i=0}^{n}{\frac {t^{i}m_{i} }{i!} }$$ may not exist}@}. {@{The [log-normal distribution](log-normal%20distribution.md)}@} is {@{an example of when this occurs}@}.

### calculations of moments

{@{The moment-generating function is so called}@} because if {@{it exists on an open interval around _t_ = 0}@}, then it is {@{the [exponential generating function](exponential%20generating%20function.md#Exponential%20generating%20function%20(EGF)) of the [moments](moment%20(mathematics).md) of the [probability distribution](probability%20distribution.md)}@}: {@{$$m_{n}=E\left(X^{n}\right)=M_{X}^{(n)}(0)=\left.{\frac {d^{n}M_{X} }{dt^{n} } }\right|_{t=0}.$$}@} That is, with {@{_n_ being a nonnegative integer}@}, {@{the _n_<!-- markdown separator -->th moment about 0 is the _n_<!-- markdown separator -->th derivative of the moment generating function, evaluated at _t_ = 0}@}.

## other properties

{@{[Jensen's inequality](Jensen's%20inequality.md)}@} provides {@{a simple lower bound on the moment-generating function}@}: {@{$$M_{X}(t)\geq e^{\mu t},$$ (annotation: $\operatorname E\left[e^{Xt}\right] \ge e^{E[X]t}$)}@} where {@{$\mu$ is the mean of _X_}@}.

The moment-generating function can be used {@{in conjunction with [Markov's inequality](Markov's%20inequality.md)}@} to {@{bound the upper tail of a real random variable _X_}@}. This statement is also called {@{the [Chernoff bound](Chernoff%20bound.md)}@}. Since {@{$x\mapsto e^{xt}$ is monotonically increasing for $t>0$}@}, we have {@{$$P(X\geq a)=P(e^{tX}\geq e^{ta})\leq e^{-at}E[e^{tX}]=e^{-at}M_{X}(t)$$}@} for {@{any $t>0$ and any _a_, provided $M_{X}(t)$ exists}@}. For example, when {@{_X_ is a standard normal distribution and $a>0$}@}, we can {@{choose $t=a$ and recall that $M_{X}(t)=e^{t^{2}/2}$}@}. This gives {@{$P(X\geq a)\leq e^{-a^{2}/2}$}@}, which is {@{within a factor of 1+_a_ of the exact value}@}.

{@{Various lemmas}@}, such as {@{[Hoeffding's lemma](Hoeffding's%20lemma.md) or [Bennett's inequality](Bennett's%20inequality.md)}@} provide {@{bounds on the moment-generating function in the case of a zero-mean, bounded random variable}@}.

When {@{$X$ is non-negative}@}, the moment generating function gives {@{a simple, useful bound on the moments}@}: {@{$$E[X^{m}]\leq \left({\frac {m}{te} }\right)^{m}M_{X}(t),$$}@} For {@{any $X,m\geq 0$ and $t>0$}@}.

This follows from {@{the inequality $1+x\leq e^{x}$}@} into which we can {@{substitute $x'=tx/m-1$ implies $tx/m\leq e^{tx/m-1}$ for any $x,t,m\in \mathbb {R}$}@}. Now, if {@{$t>0$ and $x,m\geq 0$}@}, this can be {@{rearranged to $x^{m}\leq (m/(te))^{m}e^{tx}$}@}. {@{Taking the expectation on both sides}@} {@{gives the bound on $E[X^{m}]$ in terms of $E[e^{tX}]$}@}.

As an example, consider {@{$X\sim {\text{Chi-Squared} }$ with $k$ degrees of freedom}@}. Then from the [examples](#examples) $M_{X}(t)=(1-2t)^{-k/2}$. Picking $t=m/(2m+k)$ and substituting into the bound: $$E[X^{m}]\leq (1+2m/k)^{k/2}e^{-m}(k+2m)^{m}.$$ We know that [in this case](chi-square%20distribution.md#noncentral%20moments) the correct bound is $E[X^{m}]\leq 2^{m}\Gamma (m+k/2)/\Gamma (k/2)$. To {@{compare the bounds}@}, we can {@{consider the asymptotics for large $k$}@}. Here the moment-generating function bound is $k^{m}(1+m^{2}/k+O(1/k^{2}))$, where the real bound is $k^{m}(1+(m^{2}-m)/k+O(1/k^{2}))$. The moment-generating function bound is thus {@{very strong in this case}@}.

## relation to other functions

{@{Related to the moment-generating function}@} are {@{a number of other [transforms](integral%20transform.md) that are common in probability theory}@}: (annotation: 3 listed below: {@{characteristic function, cumulant-generating function, probability generating function}@})

__[Characteristic function](characteristic%20function%20(probability%20theory).md)__

&emsp; {@{The [characteristic function](characteristic%20function%20(probability%20theory).md) $\varphi _{X}(t)$}@} is {@{related to the moment-generating function via $\varphi _{X}(t)=M_{iX}(t)=M_{X}(it)$}@}: the characteristic function is {@{the moment-generating function of _iX_ or the moment generating function of _X_ evaluated on the imaginary axis}@}. This function can also be viewed as {@{the [Fourier transform](Fourier%20transform.md) of the [probability density function](probability%20density%20function.md)}@}, which can therefore {@{be deduced from it by inverse Fourier transform}@}.

__[Cumulant-generating function](cumulant-generating%20function.md)__

&emsp; {@{The [cumulant-generating function](cumulant-generating%20function.md)}@} is defined as {@{the logarithm of the moment-generating function}@}; some instead define the cumulant-generating function as {@{the logarithm of the [characteristic function](characteristic%20function%20(probability%20theory).md)}@}, while others call this latter {@{the _second_ cumulant-generating function}@}.

__[Probability-generating function](probability-generating%20function.md)__

&emsp; {@{The [probability-generating function](probability-generating%20function.md)}@} is defined as {@{$G(z)=E\left[z^{X}\right].\,$}@} This immediately implies that {@{$G(e^{t})=E\left[e^{tX}\right]=M_{X}(t).\,$}@}

## see also

- [Characteristic function \(probability theory\)](characteristic%20function%20(probability%20theory).md)
- [Factorial moment generating function](factorial%20moment%20generating%20function.md)
- [Rate function](rate%20function.md)
- [Hamburger moment problem](Hamburger%20moment%20problem.md)

<!-- | ![](../../archives/Wikimedia%20Commons/Text%20document%20with%20red%20question%20mark.svg) | This article includes a list of [general references](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#General%20references), but __it lacks sufficient corresponding [inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#Inline%20citations)__. Please help to [improve](https://en.wikipedia.org/wiki/Wikipedia:WikiProject%20Reliability) this article by [introducing](https://en.wikipedia.org/wiki/Wikipedia:When%20to%20cite) more precise citations. _\(February 2010\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/moment-generating_function) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

### citations

1. <a id="CITEREFCasellaBerger1990"></a> Casella, George; Berger, Roger L. \(1990\). _Statistical Inference_. Wadsworth & Brooks/Cole. p. 61. [ISBN](ISBN%20(identifier).md) [0-534-11958-1](https://en.wikipedia.org/wiki/Special:BookSources/0-534-11958-1). <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFBulmer1979"></a> Bulmer, M. G. \(1979\). _Principles of Statistics_. Dover. pp. 75–79. [ISBN](ISBN%20(identifier).md) [0-486-63760-3](https://en.wikipedia.org/wiki/Special:BookSources/0-486-63760-3). <a id="^ref-2"></a>^ref-2
3. Kotz et al.<sup>\[_[full citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#What%20information%20to%20include)_\]</sup> p. 37 using 1 as the number of degree of freedom to recover the Cauchy distribution <a id="^ref-3"></a>^ref-3

### sources

- <a id="CITEREFCasellaBerger2002"></a> Casella, George; Berger, Roger \(2002\). _Statistical Inference_ \(2nd ed.\). Thomson Learning. pp. 59–68. [ISBN](ISBN%20(identifier).md) [978-0-534-24312-8](https://en.wikipedia.org/wiki/Special:BookSources/978-0-534-24312-8).

| <!-- hide <p> - [v](https://en.wikipedia.org/wiki/Template:Theory%20of%20probability%20distributions) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Theory%20of%20probability%20distributions) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3ATheory%20of%20probability%20distributions) <p>  <p>  <br/> --> Theory of [probability distributions](probability%20distribution.md) |                                                                                                                          |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| ------------------------------------------------------------------------------------------------------------------------:|
| - [probability mass function](probability%20mass%20function.md) \(pmf\) <br/> - [probability density function](probability%20density%20function.md) \(pdf\) <br/> - [cumulative distribution function](cumulative%20distribution%20function.md) \(cdf\) <br/> - [quantile function](quantile%20function.md)                                                                                                          | ![log-logistic density function plot, without labels](../../archives/Wikimedia%20Commons/Loglogisticpdf%20no-labels.svg) |
| - [raw moment](raw%20moment.md) <br/> - [central moment](central%20moment.md) <br/> - [mean](expected%20value.md) <br/> - [variance](variance.md) <br/> - [standard deviation](standard%20deviation.md) <br/> - [skewness](skewness.md) <br/> - [kurtosis](kurtosis.md) <br/> - [L-moment](L-moment.md)                                                                                                              |                                                                                                                          |
| - [moment-generating function](moment-generating%20function.md) \(mgf\) <br/> - [characteristic function](characteristic%20function%20(probability%20theory).md) <br/> - [probability-generating function](probability-generating%20function.md) \(pgf\) <br/> - [cumulant](cumulant.md) <br/> - [combinant](combinant.md)                                                                                           |                                                                                                                          |

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Moment \(mathematics\)](https://en.wikipedia.org/wiki/Category:Moment%20%28mathematics%29)
> - [Generating functions](https://en.wikipedia.org/wiki/Category:Generating%20functions)
