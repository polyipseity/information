---
aliases:
  - Sylvester's criteria
  - Sylvester's criterion
  - Sylvester's criterions
  - Sylvester’s criteria
  - Sylvester’s criterion
  - Sylvester’s criterions
tags:
  - flashcard/active/general/eng/Sylvester_s_criterion
  - language/in/English
---

# Sylvester's criterion

In {@{mathematics}@}, {@{__Sylvester's criterion__}@} is {@{a [necessary and sufficient](necessary%20and%20sufficient%20condition.md) criterion to determine whether a [Hermitian matrix](Hermitian%20matrix.md) is [positive-definite](definite%20matrix.md)}@}. <!--SR:!2026-02-01,245,330!2026-02-22,261,330!2025-10-03,148,310-->

Sylvester's criterion states that {@{a _n_ × _n_ Hermitian matrix _M_ is positive-definite}@} {@{[if and only if](if%20and%20only%20if.md) all the following matrices have a positive [determinant](determinant.md):}@} <!--SR:!2026-03-27,287,330!2026-03-25,285,330-->

- the upper left 1-by-1 corner of _M_,
- the upper left 2-by-2 corner of _M_,
- the upper left 3-by-3 corner of _M_,
- ${}\quad \vdots$
- _M_ itself.

In other words, {@{all of the _leading_ [principal minors](principal%20minor.md) must be positive}@}. By {@{using appropriate permutations of rows and columns of _M_}@}, it can also be shown that {@{the positivity of _any_ nested sequence of _n_ principal minors of _M_ is equivalent to _M_ being positive-definite}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-11-09,173,310!2026-01-31,243,330!2026-02-03,246,330-->

An analogous theorem holds for {@{characterizing [positive-semidefinite](positive-semidefinite%20matrix.md) Hermitian matrices}@}, except that {@{it is no longer sufficient to consider only the _leading_ principal minors}@} as illustrated by the Hermitian matrix {@{$${\begin{pmatrix}0&0&-1\\0&-1&0\\-1&0&0\end{pmatrix} }\quad {\text{with eigenvectors} }\quad {\begin{pmatrix}0\\1\\0\end{pmatrix} },\quad {\begin{pmatrix}1\\0\\1\end{pmatrix} }\quad {\text{and} }\quad {\begin{pmatrix}1\\0\\-1\end{pmatrix} }.$$}@} {@{A Hermitian matrix _M_ is positive-semidefinite}@} {@{if and only if _all_ [principal minors](principal%20minor.md) of _M_ are nonnegative}@}.<sup>[\[2\]](#^ref-2)</sup><sup>[\[3\]](#^ref-3)</sup> <!--SR:!2026-03-26,286,330!2026-03-12,272,330!2026-03-22,282,330!2026-03-21,281,330!2026-03-08,268,330-->

## proof for the case of positive definite matrices

Suppose {@{$M_{n}$ is $n\times n$ Hermitian matrix $M_{n}^{\dagger }=M_{n}$}@}. Let {@{$M_{k},k=1,\ldots n$ be the leading principal minor matrices, i.e. the $k\times k$ upper left corner matrices}@}. It will be shown that if {@{$M_{n}$ is positive definite, then the principal minors are positive}@}; that is, {@{$\det M_{k}>0$ for all $k$}@}. <!--SR:!2026-02-09,252,330!2026-04-02,293,330!2026-03-11,271,330!2026-03-07,267,330-->

$M_{k}$ is {@{positive definite}@}. Indeed, choosing {@{$$x=\left({\begin{array}{c}x_{1}\\\vdots \\x_{k}\\0\\\vdots \\0\end{array} }\right)=\left({\begin{array}{c}{\vec {x} }\\0\\\vdots \\0\end{array} }\right)$$}@} we can notice that {@{$0<x^{\dagger }M_{n}x={\vec {x} }^{\dagger }M_{k}{\vec {x} }$}@}. Equivalently, {@{the eigenvalues of $M_{k}$ are positive}@}, and this {@{implies that $\det M_{k}>0$ since the determinant is the product of the eigenvalues}@}. <!--SR:!2026-03-25,285,330!2026-02-07,251,330!2026-02-21,260,330!2026-02-10,253,330!2026-04-01,292,330-->

To {@{prove the reverse implication}@}, we {@{use [induction](mathematical%20induction.md)}@}. {@{The general form of an $(n+1)\times (n+1)$ Hermitian matrix}@} is {@{$$M_{n+1}=\left({\begin{array}{cc}M_{n}&{\vec {v} }\\{\vec {v} }^{\dagger }&d\end{array} }\right)\qquad (*)\,,$$}@} where {@{$M_{n}$ is an $n\times n$ Hermitian matrix, ${\vec {v} }$ is a vector and $d$ is a real constant}@}. <!--SR:!2026-04-03,294,330!2026-03-21,281,330!2026-02-19,259,330!2026-03-31,291,330!2026-02-06,249,330-->

Suppose {@{the criterion holds for $M_{n}$}@}. Assuming that {@{all the principal minors of $M_{n+1}$ are positive}@} implies that {@{$\det M_{n+1}>0$, $\det M_{n}>0$, and that $M_{n}$ is positive definite by the inductive hypothesis}@}. Denote {@{$$x=\left({\begin{array}{c}{\vec {x} }\\x_{n+1}\end{array} }\right)$$}@} then {@{$$x^{\dagger }M_{n+1}x={\vec {x} }^{\dagger }M_{n}{\vec {x} }+x_{n+1}{\vec {x} }^{\dagger }{\vec {v} }+{\bar {x} }_{n+1}{\vec {v} }^{\dagger }{\vec {x} }+d|x_{n+1}|^{2}$$}@} \(annotation: To calculate the above, manipulate the block matrix {@{as if it is an ordinary matrix when multiplying}@}.\) By {@{completing the squares}@}, this last expression is equal to {@{$$\begin{aligned} & ({\vec {x} }^{\dagger }+{\vec {v} }^{\dagger }M_{n}^{-1}{\bar {x} }_{n+1})M_{n}({\vec {x} }+x_{n+1}M_{n}^{-1}{\vec {v} })-|x_{n+1}|^{2}{\vec {v} }^{\dagger }M_{n}^{-1}{\vec {v} }+d|x_{n+1}|^{2} \\ & =({\vec {x} }+{\vec {c} })^{\dagger }M_{n}({\vec {x} }+{\vec {c} })+|x_{n+1}|^{2}(d-{\vec {v} }^{\dagger }M_{n}^{-1}{\vec {v} }) \end{aligned}$$}@} \(annotation: The "squares" in the expression may {@{not be obvious}@}. It is easier to see the "squares" once {@{you remove the $M_n$ in the first term}@}. Then, the "squares" in the original expression is {@{actually $\operatorname{square}(\vec a) = {\vec a}^\dagger M_n \vec a$}@}. Finally try to see that {@{you just need to somehow introduce $M_n$ for the middle two terms}@}.\) where {@{${\vec {c} }=x_{n+1}M_{n}^{-1}{\vec {v} }$}@} \(note that {@{$M_{n}^{-1}$ exists because the eigenvalues of $M_{n}$ are all positive}@}.\) The first term is {@{positive by the inductive hypothesis}@}. We now {@{examine the sign of the second term}@}. By using {@{the [block matrix determinant formula](block%20matrix.md#block%20matrix%20operations) $$\det \left({\begin{array}{cc}A&B\\C&D\end{array} }\right)=\det A\det(D-CA^{-1}B)$$ on $(*)$}@} we obtain <p> &emsp; {@{$\det M_{n+1}=\det M_{n}(d-{\vec {v} }^{\dagger }M_{n}^{-1}{\vec {v} })>0$}@}, which {@{implies $d-{\vec {v} }^{\dagger }M_{n}^{-1}{\vec {v} }>0$}@}. <p> Consequently, {@{$x^{\dagger }M_{n+1}x>0$}@}. <!--SR:!2026-02-04,247,330!2026-03-16,276,330!2026-03-17,277,330!2026-03-16,276,330!2026-03-20,280,330!2026-02-02,245,330!2026-02-19,259,330!2025-12-10,151,270!2026-03-16,276,330!2026-03-21,281,330!2026-02-17,257,330!2026-03-20,280,330!2026-03-30,290,330!2026-03-24,284,330!2026-03-08,268,330!2026-01-31,244,330!2025-09-29,128,290!2026-07-24,335,290!2026-11-17,454,310!2026-02-02,246,330-->

## proof for the case of positive semidefinite matrices

Let {@{$M_{n}$ be an _n_ x _n_ Hermitian matrix}@}. Suppose {@{$M_{n}$ is semidefinite}@}. Essentially {@{the same proof as for the case that $M_{n}$ is strictly positive definite}@} shows that {@{all principal minors \(not necessarily the leading principal minors\) are non-negative}@}. <!--SR:!2026-02-18,258,330!2026-02-08,251,330!2026-03-12,272,330!2026-03-29,289,330-->

For {@{the reverse implication}@}, it {@{suffices to show that if $M_{n}$ has all non-negative principal minors}@}, then for {@{all _t\>0_, all leading principal minors of the Hermitian matrix $M_{n}+tI_{n}$ are strictly positive, where $I_{n}$ is the _n_<!-- markdown separator -->x<!-- markdown separator -->_n_ [identity matrix](identity%20matrix.md)}@}. Indeed, from {@{the positive definite case}@}, we would know that {@{the matrices $M_{n}+tI_{n}$ are strictly positive definite}@}. Since {@{the limit of positive definite matrices is always positive semidefinite}@}, we can {@{take $t\to 0$ to conclude}@}. <!--SR:!2026-04-03,294,330!2025-09-21,124,290!2026-02-16,256,330!2026-03-11,271,330!2026-03-23,283,330!2026-02-11,254,330!2026-03-29,289,330-->

To show this, let {@{$M_{k}$ be the _k_<!-- markdown separator -->th leading principal submatrix of $M_{n}$}@}. We know that {@{$q_{k}(t)=\det(M_{k}+tI_{k})$ is a polynomial in _t_}@}, related to {@{the characteristic polynomial $p_{M_{k} }$ via $$q_{k}(t)=(-1)^{k}p_{M_{k} }(-t).$$}@} We use {@{the identity in [Characteristic polynomial\#Properties](characteristic%20polynomial.md#properties)}@} to write {@{$$q_{k}(t)=\sum _{j=0}^{k}t^{k-j}\operatorname {tr} \left(\textstyle \bigwedge ^{j}M_{k}\right),$$}@} where {@{$\operatorname {tr} \left(\bigwedge ^{j}M_{k}\right)$ is the trace of the _j_<!-- markdown separator -->th exterior power of $M_{k}$ \(annotation: this uses the language of [exterior algebra](exterior%20algebra.md)\)}@}. <!--SR:!2026-02-12,255,330!2026-03-15,275,330!2025-12-20,190,270!2026-02-01,244,330!2025-11-10,146,250!2025-11-27,178,310-->

From {@{[Minor \(linear algebra\)\#Multilinear algebra approach](minor%20(linear%20algebra).md#multilinear%20algebra%20approach)}@}, we know that {@{the entries in the matrix expansion of $\bigwedge ^{j}M_{k}$ \(for _j \> 0_\)}@} are {@{just the minors of $M_{k}$}@}. In particular, {@{the diagonal entries are the principal minors of $M_{k}$}@}, which {@{of course are also principal minors of $M_{n}$, and are thus non-negative}@}. \(annotation: This is why {@{considering only the _leading_ principal minors is insufficient}@}.\) Since {@{the trace of a matrix is the sum of the diagonal entries}@}, it follows that {@{$$\operatorname {tr} \left(\textstyle \bigwedge ^{j}M_{k}\right)\geq 0.$$}@} Thus {@{the coefficient of $t^{k-j}$ in $q_{k}(t)$ is non-negative for all _j \> 0_}@}. For {@{_j = 0_, it is clear that the coefficient is 1}@}. In particular, {@{$q_{k}(t)>0$ for all _t \> 0_, which is what was required to show}@}. <!--SR:!2026-03-08,268,330!2026-02-20,259,330!2025-10-18,154,310!2026-03-22,282,330!2026-03-28,288,330!2026-02-07,250,330!2026-03-06,266,330!2026-02-02,245,330!2026-02-24,263,330!2026-02-05,248,330!2026-01-30,243,330-->

## notes

1. <a id="CITEREFHornJohnson1985"></a> Horn, Roger A.; Johnson, Charles R. \(1985\), _Matrix Analysis_, [Cambridge University Press](Cambridge%20University%20Press.md), [ISBN](ISBN%20(identifier).md) [978-0-521-38632-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-38632-6). See Theorem 7.2.5. <a id="^ref-1"></a>^ref-1
2. Carl D. Meyer, Matrix Analysis and Applied Linear Algebra. See section __7.6 Positive Definite Matrices__, page 566 <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFPrussing1986"></a> Prussing, John E. \(1986\), ["The Principal Minor Test for Semidefinite Matrices"](https://web.archive.org/web/20170107084552/http://prussing.ae.illinois.edu/semidef.pdf) \(PDF\), _Journal of Guidance, Control, and Dynamics_, __9__ \(1\): 121–122, [Bibcode](bibcode%20(identifier).md):[1986JGCD....9..121P](https://ui.adsabs.harvard.edu/abs/1986JGCD....9..121P), [doi](doi%20(identifier).md):[10.2514/3.20077](https://doi.org/10.2514%2F3.20077), archived from [the original](http://prussing.ae.illinois.edu/semidef.pdf) \(PDF\) on 2017-01-07, retrieved 2017-09-28 <a id="^ref-3"></a>^ref-3

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Sylvester's_criterion) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFGilbert1991"></a> Gilbert, George T. \(1991\), "Positive definite matrices and Sylvester's criterion", _[The American Mathematical Monthly](American%20Mathematical%20Monthly.md)_, __98__ \(1\), Mathematical Association of America: 44–46, [doi](doi%20(identifier).md):[10.2307/2324036](https://doi.org/10.2307%2F2324036), [ISSN](ISSN%20(identifier).md) [0002-9890](https://search.worldcat.org/issn/0002-9890), [JSTOR](JSTOR%20(identifier).md#content) [2324036](https://www.jstor.org/stable/2324036).
- <a id="CITEREFHornJohnson1985"></a> Horn, Roger A.; Johnson, Charles R. \(1985\), _Matrix Analysis_, [Cambridge University Press](Cambridge%20University%20Press.md), [ISBN](ISBN%20(identifier).md) [978-0-521-38632-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-38632-6). Theorem 7.2.5.
- <a id="CITEREFCarl D. Meyer2000"></a> Carl D. Meyer \(June 2000\), _Matrix Analysis and Applied Linear Algebra_, [SIAM](Society%20for%20Industrial%20and%20Applied%20Mathematics.md), [ISBN](ISBN%20(identifier).md) [0-89871-454-0](https://en.wikipedia.org/wiki/Special:BookSources/0-89871-454-0).

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Matrix theory](https://en.wikipedia.org/wiki/Category:Matrix%20theory)
