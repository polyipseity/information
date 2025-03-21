---
aliases:
  - Stirling number
  - Stirling numbers
tags:
  - flashcard/active/general/eng/Stirling_number
  - language/in/English
---

# Stirling number

In [mathematics](mathematics.md), __Stirling numbers__ {@{arise in a variety of [analytic](mathematical%20analysis.md) and [combinatorial](combinatorics.md) problems}@}. They are named after {@{[James Stirling](James%20Stirling%20(mathematician).md)}@}, who {@{introduced them in a purely algebraic setting in his book _Methodus differentialis_ (1730)}@}.<sup>[\[1\]](#^ref-1)</sup> They were {@{rediscovered and given a combinatorial meaning by Masanobu Saka in 1782}@}.<sup>[\[2\]](#^ref-2)</sup>

{@{Two different sets of numbers}@} bear this name: {@{the [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md) and the [Stirling numbers of the second kind](Stirling%20numbers%20of%20the%20second%20kind.md)}@}. Additionally, {@{[Lah numbers](Lah%20number.md)}@} are {@{sometimes referred to as Stirling numbers of the third kind}@}. Each kind is detailed in {@{its respective article, this one serving as a description of relations between them}@}.

A common property of all three kinds is that {@{they describe coefficients relating three different sequences of polynomials that frequently arise in combinatorics}@}. Moreover, all three can be {@{defined as the number of partitions of _n_ elements into _k_ non-empty subsets}@}, where {@{each subset is endowed with a certain kind of order (no order, cyclical, or linear)}@}.

## notation

- see: [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md) and [Stirling numbers of the second kind](Stirling%20numbers%20of%20the%20second%20kind.md)

{@{Several different notations for Stirling numbers}@} are in use. {@{Ordinary (signed) __Stirling numbers of the first kind__}@} are commonly denoted: {@{$$s(n,k)\,.$$}@}

{@{__Unsigned Stirling numbers of the first kind__}@}, which count {@{the number of [permutations](permutation.md) of _n_ elements with _k_ disjoint [cycles](cyclic%20permutation.md)}@}, are denoted: {@{$${\biggl [}{n \atop k}{\biggr ]}=c(n,k)=|s(n,k)|=(-1)^{n-k}s(n,k)\,$$}@}

{@{__Stirling numbers of the second kind__}@}, which count {@{the number of ways to partition a set of _n_ elements into _k_ nonempty subsets}@}:<sup>[\[3\]](#^ref-3)</sup> {@{$${\biggl \{}{\!n\! \atop \!k\!}{\biggr \} }=S(n,k)=S_{n}^{(k)}\,$$}@}

[Abramowitz and Stegun](Abramowitz%20and%20Stegun.md) use {@{an uppercase $S$ and a [blackletter](blackletter.md) ${\mathfrak {S} }$, respectively}@}, for {@{the first and second kinds of Stirling number}@}. {@{The notation of brackets and braces, in analogy to [binomial coefficients](binomial%20coefficient.md)}@}, was {@{introduced in 1935 by [Jovan Karamata](Jovan%20Karamata.md) and promoted later by [Donald Knuth](Donald%20Knuth.md)}@}, though {@{the bracket notation conflicts with a common notation for [Gaussian coefficients](Gaussian%20binomial%20coefficient.md)}@}.<sup>[\[4\]](#^ref-4)</sup> The mathematical motivation for this type of notation, as well as additional Stirling number formulae, may be found on the page for [Stirling numbers and exponential generating functions](Stirling%20numbers%20and%20exponential%20generating%20functions%20in%20symbolic%20combinatorics.md).

{@{Another infrequent notation}@} is {@{$s_{1}(n,k)$ and $s_{2}(n,k)$}@}.

## expansions of falling and rising factorials

Stirling numbers express {@{coefficients in expansions of [falling and rising factorials](falling%20and%20rising%20factorials.md) (also known as the Pochhammer symbol) as polynomials}@}.

That is, {@{the __falling factorial__, defined as $\ (x)_{n}=x(x-1)\ \cdots (x-n+1)\ ,$}@} is {@{a polynomial in _x_ of degree _n_ whose expansion is $$(x)_{n}\ =\ \sum _{k=0}^{n}\ s(n,k)\ x^{k}{\ }$$}@} with {@{(signed) Stirling numbers of the first kind as coefficients}@}.

Note that {@{$\ (x)_{0}\equiv 1\ ,$ by convention}@}, because {@{it is an [empty product](empty%20product.md)}@}. {@{The notations $\ x^{\underline {n} }{\ }$ for the falling factorial and $\ x^{\overline {n} }{\ }$ for the rising factorial}@} are also often used.<sup>[\[5\]](#^ref-5)</sup> (Confusingly, {@{the Pochhammer symbol that many use for _falling_ factorials}@} is {@{used in [special functions](special%20functions.md) for _rising_ factorials}@}.)

Similarly, {@{the __rising factorial__, defined as $\ x^{(n)}\ =\ x(x+1)\ \cdots (x+n-1)\ ,$}@} is {@{a polynomial in _x_ of degree _n_ whose expansion is $$x^{(n)}\ =\ \sum _{k=0}^{n}\ {\biggl [}{n \atop k}{\biggr ]}\ x^{k}\ =\ \sum _{k=0}^{n}\ (-1)^{n-k}\ s(n,k)\ x^{k}\ ,$$}@} with {@{unsigned Stirling numbers of the first kind as coefficients}@}. One of these expansions can be {@{derived from the other}@} by {@{observing that $\ x^{(n)}=(-1)^{n}(-x)_{n}~.$}@}

{@{Stirling numbers of the second kind}@} express {@{the reverse relations}@}: {@{$$\ x^{n}\ =\ \sum _{k=0}^{n}\ S(n,k)\ (x)_{k}{\ }$$ and $$\ x^{n}\ =\ \sum _{k=0}^{n}\ (-1)^{n-k}\ S(n,k)\ x^{(k)}~.$$}@}

## as change of basis coefficients

Considering {@{the set of [polynomials](polynomial.md) in the (indeterminate) variable _x_ as a vector space}@}, {@{each of the three sequences $$x^{0},x^{1},x^{2},x^{3},\dots \quad (x)_{0},(x)_{1},(x)_{2},\dots \quad x^{(0)},x^{(1)},x^{(2)},\dots$$}@} is {@{a [basis](basis%20(linear%20algebra).md)}@}. That is, {@{every polynomial in _x_ can be written as a sum $a_{0}x^{(0)}+a_{1}x^{(1)}+\dots +a_{n}x^{(n)}$ for some unique coefficients $a_{i}$ (similarly for the other two bases)}@}. The above relations then {@{express the [change of basis](change%20of%20basis.md) between them, as summarized in the following [commutative diagram](commutative%20diagram.md)}@}: <p> {@{![commutative diagram of Stirling numbers as changes of basis](../../archives/Wikimedia%20Commons/Stirling%20numbers%20as%20polynomial%20basis%20changes.png)}@} <p> {@{The coefficients for the two bottom changes}@} are {@{described by the [Lah numbers](#Lah%20numbers) below}@}. Since {@{coefficients in any basis are unique}@}, one can {@{define Stirling numbers this way, as the coefficients expressing polynomials of one basis in terms of another}@}, that is, {@{the unique numbers relating $x^{n}$ with falling and rising factorials as above}@}.

Falling factorials define, {@{up to scaling, the same polynomials as [binomial coefficients](binomial%20coefficient.md#binomial%20coefficients%20as%20polynomials)}@}: {@{${\binom {x}{k} }=(x)_{k}/k!$}@}. {@{The changes between the standard basis $\textstyle x^{0},x^{1},x^{2},\dots$ and the basis ${\binom {x}{0} },{\binom {x}{1} },{\binom {x}{2} },\dots$}@} are {@{thus described by similar formulas: $$x^{n}=\sum _{k=0}^{n}{\biggl \{}{\!n\! \atop \!k\!}{\biggr \} }k!{\binom {x}{k} }\quad {\text{and} }\quad {\binom {x}{n} }=\sum _{k=0}^{n}{\frac {s(n,k)}{n!} }x^{k} \,.$$}@}

### example

{@{Expressing a polynomial in the basis of falling factorials}@} is {@{useful for calculating sums of the polynomial evaluated at consecutive integers}@}. Indeed, {@{the sum of falling factorials up to _n_ (exclusive) with fixed _k_}@} can expressed as {@{another falling factorial (for $k\neq -1$) $$\sum _{0\leq i<n}(i)_{k}={\frac {(n)_{k+1} }{k+1} }$$}@} (annotation: The above {@{suspiciously looks like definite integration of _i<sup>k</sup>_ from 0 to _n_... but with discrete summation}@}.) This can be proved by {@{[induction](mathematical%20induction.md)}@}.

For example, {@{the sum of fourth powers of integers up to _n_ (this time with _n_ included)}@}, is: {@{$${\begin{aligned}\sum _{i=0}^{n}i^{4}&=\sum _{i=0}^{n}\sum _{k=0}^{4}{\biggl \{}{\!4\! \atop \!k\!}{\biggr \} }(i)_{k}=\sum _{k=0}^{4}{\biggl \{}{\!4\! \atop \!k\!}{\biggr \} }\sum _{i=0}^{n}(i)_{k}=\sum _{k=0}^{4}{\biggl \{}{\!4\! \atop \!k\!}{\biggr \} }{\frac {(n{+}1)_{k+1} }{k{+}1} }\\[10mu]&={\biggl \{}{\!4\! \atop \!1\!}{\biggr \} }{\frac {(n{+}1)_{2} }{2} }+{\biggl \{}{\!4\! \atop \!2\!}{\biggr \} }{\frac {(n{+}1)_{3} }{3} }+{\biggl \{}{\!4\! \atop \!3\!}{\biggr \} }{\frac {(n{+}1)_{4} }{4} }+{\biggl \{}{\!4\! \atop \!4\!}{\biggr \} }{\frac {(n{+}1)_{5} }{5} }\\[8mu]&={\frac {1}{2} }(n{+}1)_{2}+{\frac {7}{3} }(n{+}1)_{3}+{\frac {6}{4} }(n{+}1)_{4}+{\frac {1}{5} }(n{+}1)_{5}\,.\end{aligned} }$$}@} Here the Stirling numbers can be computed from {@{their definition as the number of partitions of 4 elements into _k_ non-empty unlabeled subsets}@}.

In contrast, {@{the sum $\sum _{i=0}^{n}i^{k}$ in the standard basis}@} is {@{given by [Faulhaber's formula](Faulhaber's%20formula.md), which in general is more complicated}@}.

## as inverse matrices

{@{The Stirling numbers of the first and second kinds}@} can be {@{considered inverses of one another}@}: {@{$$\sum _{j=k}^{n}s(n,j)S(j,k)=\sum _{j=k}^{n}(-1)^{n-j}{\biggl [}{n \atop j}{\biggr ]}{\biggl \{}{\!j\! \atop \!k\!}{\biggr \} }=\delta _{n,k}$$ and $$\sum _{j=k}^{n}S(n,j)s(j,k)=\sum _{j=k}^{n}(-1)^{j-k}{\biggl \{}{\!n\! \atop \!j\!}{\biggr \} }{\biggl [}{j \atop k}{\biggr ]}=\delta _{n,k},$$}@} where {@{$\delta _{nk}$ is the [Kronecker delta](kronecker%20delta.md)}@}. These two relationships may be {@{understood to be matrix inverse relationships}@}. That is, let {@{_s_ be the [lower triangular matrix](triangular%20matrix.md) of (signed) Stirling numbers of the first kind, whose matrix elements $s_{nk}=s(n,k).\,$}@} {@{The [inverse](invertible%20matrix.md) of this matrix}@} is {@{_S_, the [lower triangular matrix](triangular%20matrix.md) of (unsigned) Stirling numbers of the second kind, whose entries are $S_{nk}=S(n,k).$}@} Symbolically, this is written {@{$$s^{-1}=S\,.$$}@} Although {@{_s_ and _S_ are infinite, so calculating a product entry involves an infinite sum}@}, the matrix multiplications {@{work because these matrices are lower triangular, so only a finite number of terms in the sum are nonzero}@}.

## Lah numbers

- see: [Lah numbers](Lah%20number.md)

{@{The Lah numbers $L(n,k)={n-1 \choose k-1}{\frac {n!}{k!} }$}@} are {@{sometimes called Stirling numbers of the third kind}@}.<sup>[\[6\]](#^ref-6)</sup> By convention, {@{$L(0,0)=1$ and $L(n,k)=0$ if $n<k$ or $k=0<n$}@}.

These numbers are {@{coefficients expressing falling factorials in terms of rising factorials and vice versa}@}: {@{<p> $x^{(n)}=\sum _{k=0}^{n}L(n,k)(x)_{k}\quad$ and $\quad (x)_{n}=\sum _{k=0}^{n}(-1)^{n-k}L(n,k)x^{(k)}.$}@}

As above, this means they {@{express the change of basis between the bases $(x)_{0},(x)_{1},(x)_{2},\cdots$ and $x^{(0)},x^{(1)},x^{(2)},\cdots$, completing the diagram}@}. In particular, {@{one formula is the inverse of the other}@}, thus: {@{$$\sum _{j=k}^{n}(-1)^{j-k}L(n,j)L(j,k)=\delta _{n,k}.$$}@}

Similarly, {@{composing the change of basis from $x^{(n)}$ to $x^{n}$ with the change of basis from $x^{n}$ to $(x)_{n}$}@} gives {@{the change of basis directly from $x^{(n)}$ to $(x)_{n}$}@}: {@{$$L(n,k)=\sum _{j=k}^{n}{\biggl [}{n \atop j}{\biggr ]}{\biggl \{}{\!j\! \atop \!k\!}{\biggr \} },$$}@} and similarly for other compositions. In {@{terms of matrices}@}, if {@{$L$ denotes the matrix with entries $L_{nk}=L(n,k)$ and $L^{-}$ denotes the matrix with entries $L_{nk}^{-}=(-1)^{n-k}L(n,k)$}@}, then {@{one is the inverse of the other: $L^{-}=L^{-1}$}@}. Composing {@{the matrix of unsigned Stirling numbers of the first kind with the matrix of Stirling numbers of the second kind}@} gives {@{the Lah numbers: $L=|s|\cdot S$}@}.

[Enumeratively](enumerative%20combinatorics.md), $\left\{ {\!n\! \atop \!k\!}\right\},\left[{n \atop k}\right],L(n,k)$ can be defined as {@{the number of partitions of _n_ elements into _k_ non-empty unlabeled subsets, where each subset is endowed with no order, a [cyclic order](cyclic%20order.md), or a linear order, respectively}@}. In particular, this {@{implies the inequalities: $${\biggl \{}{\!n\! \atop \!k\!}{\biggr \} }\leq {\biggl [}{n \atop k}{\biggr ]}\leq L(n,k).$$}@}

## inversion relations and the Stirling transform

For {@{any pair of sequences, $\{f_{n}\}$ and $\{g_{n}\}$}@}, related by {@{a finite sum Stirling number formula given by $$g_{n}=\sum _{k=0}^{n}\left\{ {\begin{matrix}n\\k\end{matrix} }\right\}f_{k},$$ for all integers $n\geq 0$}@}, we have {@{a corresponding [inversion formula](generating%20function%20transformation.md#inversion%20relations%20and%20generating%20function%20identities) for $f_{n}$ given by $$f_{n}=\sum _{k=0}^{n}\left[{\begin{matrix}n\\k\end{matrix} }\right](-1)^{n-k}g_{k}.$$}@} {@{The lower indices}@} could be {@{any integer between $0$ and $n$}@}.

{@{These inversion relations between the two sequences}@} translate into {@{functional equations between the sequence [exponential generating functions](generating%20function.md) given by the [Stirling (generating function) transform](Stirling%20transform.md)}@} as {@{$${\widehat {G} }(z)={\widehat {F} }\left(e^{z}-1\right)$$ and $${\widehat {F} }(z)={\widehat {G} }\left(\log(1+z)\right).$$}@} (annotation: The change of basis from $G$ to $F$ uses {@{$\left\{ \begin{matrix} n \\ k \end{matrix} \right\}$, while that from $F$ to $G$ uses $s(n, k)$}@}. The above two relations can be {@{derived from each other by replacing $z$ with $e^z - 1$ or $\ln (1 + z)$}@}.)

For {@{$D=d/dx$}@}, {@{the [differential operators](differential%20operator.md) $x^{n}D^{n}$ and $(xD)^{n}$}@} are {@{related by the following formulas}@} for {@{all integers $n\geq 0$}@}:<sup>[\[7\]](#^ref-7)</sup> {@{$${\begin{aligned}(xD)^{n}&=\sum _{k=0}^{n}S(n,k)x^{k}D^{k}\\x^{n}D^{n}&=\sum _{k=0}^{n}s(n,k)(xD)^{k}=(xD)_{n}=xD(xD-1)\ldots (xD-n+1)\end{aligned} }$$}@}

{@{Another pair of "_inversion_" relations involving the [Stirling numbers](Stirling%20number.md)}@} relate {@{the [forward differences](finite%20difference.md) and the ordinary $n^{th}$ [derivatives](derivative.md) of a function, $f(x)$}@}, which is {@{analytic for all $x$}@} by the formulas<sup>[\[8\]](#^ref-8)</sup> {@{$${\frac {1}{k!} }{\frac {d^{k} }{dx^{k} } }f(x)=\sum _{n=k}^{\infty }{\frac {s(n,k)}{n!} }\Delta ^{n}f(x)$$ <br/> $${\frac {1}{k!} }\Delta ^{k}f(x)=\sum _{n=k}^{\infty }{\frac {S(n,k)}{n!} }{\frac {d^{n} }{dx^{n} } }f(x).$$}@}

## similar properties

__Table of similarities__ (not really a table anymore...)

- __[Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md)__ vs. __[Stirling numbers of the second kind](Stirling%20numbers%20of%20the%20second%20kind.md)__
- recurrence relation ::@:: $$\left[{n+1 \atop k}\right]=n\left[{n \atop k}\right]+\left[{n \atop k-1}\right]$$ <p> vs. <p> $$\left\{ {n+1 \atop k}\right\}=k\left\{ {n \atop k}\right\}+\left\{ {n \atop k-1}\right\}$$
- summation ::@:: $$\sum _{k=0}^{n}\left[{n \atop k}\right]=n!$$ <p> vs. <p> $$\sum _{k=0}^{n}\left\{ {n \atop k}\right\}=B_{n}$$, where $B_{n}$ is the n-th [Bell number](Bell%20number.md)
- polynomial summation ::@:: $$\sum _{k=0}^{n}\left[{n \atop k}\right]x^{k}=x^{(n)}$$, where $\{x^{(n)}\}_{n\in \mathbb {N} }$ is the [rising factorials](falling%20and%20rising%20factorials.md) <p> vs. <p> $$\sum _{k=0}^{n}\left\{ {n \atop k}\right\}x^{k}=T_{n}(x)$$, where $\{T_{n}\}_{n\in \mathbb {N} }$ is the [Touchard polynomials](Touchard%20polynomials.md)
- special cases ::@:: $$\left[{n \atop 0}\right]=\delta _{n},\ \left[{n \atop n-1}\right]={\binom {n}{2} },\ \left[{n \atop n}\right]=1$$ <p> vs. <p> $$\left\{ {n \atop 0}\right\}=\delta _{n},\ \left\{ {n \atop n-1}\right\}={\binom {n}{2} },\ \left\{ {n \atop n}\right\}=1$$
- increment by binomial coefficient ::@:: $$\left[{n+1 \atop k+1}\right]=\sum _{j=k}^{n}\left[{n \atop j}\right]{\binom {j}{k} }$$ <p> vs. <p> $$\left\{ {n+1 \atop k+1}\right\}=\sum _{j=k}^{n}{\binom {n}{j} }\left\{ {j \atop k}\right\}$$ (annotation: Choose _n_ - _j_ elements from _n_ + 1 elements to form a maybe empty partition. Add the 1 element to ensure it is nonempty. Partition the remaining _j_ elements into _k_ partitions.)
- increment by combinatorial argument ::@:: $$\left[{\begin{matrix}n+1\\k+1\end{matrix} }\right]=\sum _{j=k}^{n}{\frac {n!}{j!} }\left[{j \atop k}\right]$$ (annotation: Permutate _n_ − _k_ elements from _n_ elements to a partition with linear order. Add the 1 element to make the partition a cycle. Partition the remaining _k_ elements into _m_ cycles.) <p> vs. <p> $$\left\{ {n+1 \atop k+1}\right\}=\sum _{j=k}^{n}(k+1)^{n-j}\left\{ {j \atop k}\right\}$$ \(annotation: Each summation term finds the number given that the $j + 1$-th element is _not_ in a partition with any element before it _and_ elements after the $j + 1$-th are in a partition with any element before it. The uniqueness is easily seen. The completeness is seen by considering the maximum of the minimums of the partitions.\)
- increment by summing up to _k_ ::@:: $$\left[{n+k+1 \atop n}\right]=\sum _{j=0}^{k}(n+j)\left[{n+j \atop j}\right]$$ <p> vs. <p> $$\left\{ {n+k+1 \atop k}\right\}=\sum _{j=0}^{k}j\left\{ {n+j \atop j}\right\}$$
- partition then choose partitions ::@:: $$\left[{n \atop l+m}\right]{\binom {l+m}{l} }=\sum _{k}{\binom {n}{k} }\left[{k \atop l}\right]\left[{n-k \atop m}\right]$$ (annotation: Choose _k_ elements from _n_ elements. Partition _k_ elements into the chosen _l_ cycles. Partition the remaining _n_ − _k_ elements into the unchosen _m_ cycles.) <p> vs. <p> $$\left\{ {n \atop l+m}\right\}{\binom {l+m}{l} }=\sum _{k}{\binom {n}{k} }\left\{ {k \atop l}\right\}\left\{ {n-k \atop m}\right\}$$ (annotation: Choose _k_ elements from _n_ elements. Partition _k_ elements into the chosen _l_ partitions. Partition the remaining _n_ − _k_ elements into the unchosen _m_ partitions.)
- asymptote for growing _k_ ::@:: $$\left[{n+k \atop k}\right]{\underset {k\to \infty }{\sim } }{\frac {k^{2n} }{2^{n}n!} }.$$ <p> vs. <p> $$\left\{ {n+k \atop k}\right\}{\underset {k\to \infty }{\sim } }{\frac {k^{2n} }{2^{n}n!} }$$
- exponential generating function for fixed _k_ ::@:: $$\sum _{n=k}^{\infty }\left[{n \atop k}\right]{\frac {x^{n} }{n!} }={\frac {(-\log(1-x))^{k} }{k!} }.$$ <p> vs. <p> $$\sum _{n=k}^{\infty }\left\{ {n \atop k}\right\}{\frac {x^{n} }{n!} }={\frac {(e^{x}-1)^{k} }{k!} }$$
- explicit formula ::@:: $$\left[{n \atop k}\right]=\sum _{0\leq i_{1}<\ldots <i_{n-k}<n}i_{1}i_{2}\cdots i_{n-k}.$$ <p> vs. <p> $$\left\{ {n \atop k}\right\}=\sum _{\begin{array}{c}c_{1}+\ldots +c_{k}=n-k\\c_{1},\ldots ,\ c_{k}\ \geq \ 0\end{array} }1^{c_{1} }2^{c_{2} }\cdots k^{c_{k} }$$

See the specific articles for details.

## symmetric formulae

Abramowitz and Stegun give {@{the following symmetric formulae that relate the Stirling numbers of the first and second kind}@}.<sup>[\[9\]](#^ref-9)</sup>

- symmetric formulae ::@:: $$\left[{n \atop k}\right]=\sum _{j=n}^{2n-k}(-1)^{j-k}{\binom {2n-k}{j} }{\binom {j-1}{k-1} }\left\{ {j-k \atop j-n}\right\}$$ and $$\left\{ {n \atop k}\right\}=\sum _{j=n}^{2n-k}(-1)^{j-k}{\binom {2n-k}{j} }{\binom {j-1}{k-1} }\left[{j-k \atop j-n}\right]$$

## Stirling numbers with negative integral values

The Stirling numbers can be {@{extended to negative integral values, but not all authors do so in the same way}@}.<sup>[\[10\]](#^ref-10)</sup><sup>[\[11\]](#^ref-11)</sup><sup>[\[12\]](#^ref-12)</sup> Regardless of {@{the approach taken}@}, it is worth noting that {@{Stirling numbers of first and second kind are connected by the relations}@}: {@{$${\biggl [}{n \atop k}{\biggr ]}={\biggl \{}{\!-k\! \atop \!-n\!}{\biggr \} }\quad {\text{and} }\quad {\biggl \{}{\!n\! \atop \!k\!}{\biggr \} }={\biggl [}{-k \atop -n}{\biggr ]}$$}@} when {@{_n_ and _k_ are nonnegative integers}@}. So we have the following table for $\left[{-n \atop -k}\right]$:

| _n_\\_k_ | __−1__ | __−2__ | __−3__ | __−4__ | __−5__ |
| --------:| ------:| ------:| ------:| ------:| ------:|
| __−1__   | 1      | 1      | 1      | 1      | 1      |
| __−2__   | 0      | 1      | 3      | 7      | 15     |
| __−3__   | 0      | 0      | 1      | 6      | 25     |
| __−4__   | 0      | 0      | 0      | 1      | 10     |
| __−5__   | 0      | 0      | 0      | 0      | 1      |

Donald Knuth<sup>[\[12\]](#^ref-12)</sup> defined the more general Stirling numbers by {@{extending a [recurrence relation](Stirling%20numbers%20of%20the%20second%20kind.md#recurrence%20relation) to all integers}@}. In this approach, $\left[{n \atop k}\right]$ and $\left\{ {\!n\! \atop \!k\!}\right\}$ are {@{zero if _n_ is negative and _k_ is nonnegative, or if _n_ is nonnegative and _k_ is negative}@}, and so we have, for {@{_any_ integers _n_ and _k_}@}, {@{$${\biggl [}{n \atop k}{\biggr ]}={\biggl \{}{\!-k\! \atop \!-n\!}{\biggr \} }\quad {\text{and} }\quad {\biggl \{}{\!n\! \atop \!k\!}{\biggr \} }={\biggl [}{-k \atop -n}{\biggr ]}.$$}@}

On the other hand, for {@{positive integers _n_ and _k_}@}, David Branson<sup>[\[11\]](#^ref-11)</sup> defined {@{$\left[{-n \atop -k}\right]\!,$ $\left\{ {\!-n\! \atop \!-k\!}\right\}\!,$ $\left[{-n \atop k}\right]\!,$ and $\left\{ {\!-n\! \atop \!k\!}\right\}$ (but not $\left[{n \atop -k}\right]$ or $\left\{ {\!n\! \atop \!-k\!}\right\}$)}@}. In this approach, one has {@{the following extension of the [recurrence relation](Stirling%20numbers%20of%20the%20second%20kind.md#recurrence%20relation) of the Stirling numbers of the first kind}@}: $${\biggl [}{-n \atop k}{\biggr ]}={\frac {(-1)^{n+1} }{n!} }\sum _{i=1}^{n}{\frac {(-1)^{i+1} }{i^{k} } }{\binom {n}{i} } \,.$$

For example, $\left[{-5 \atop k}\right]={\frac {1}{120} }{\Bigl (}5-{\frac {10}{2^{k} } }+{\frac {10}{3^{k} } }-{\frac {5}{4^{k} } }+{\frac {1}{5^{k} } }{\Bigr )}.$ This leads to the following table of values of $\left[{n \atop k}\right]$ for negative integral _n_.

| _k_\\_n_ | __0__                  | __1__                     | __2__                         | __3__                            | __4__                                |
|:--------:|:----------------------:|:-------------------------:|:-----------------------------:|:--------------------------------:|:------------------------------------:|
| __−1__   | 1                      | 1                         | 1                             | 1                                | 1                                    |
| __−2__   | $${\tfrac {-1}{2} }$$  | $${\tfrac {-3}{4} }$$     | $${\tfrac {-7}{8} }$$         | $${\tfrac {-15}{16} }$$          | $${\tfrac {-31}{32} }$$              |
| __−3__   | $${\tfrac {1}{6} }$$   | $${\tfrac {11}{36} }$$    | $${\tfrac {85}{216} }$$       | $${\tfrac {575}{1296} }$$        | $${\tfrac {3661}{7776} }$$           |
| __−4__   | $${\tfrac {-1}{24} }$$ | $${\tfrac {-25}{288} }$$  | $${\tfrac {-415}{3456} }$$    | $${\tfrac {-5845}{41472} }$$     | $${\tfrac {-76111}{497664} }$$       |
| __−5__   | $${\tfrac {1}{120} }$$ | $${\tfrac {137}{7200} }$$ | $${\tfrac {12019}{432000} }$$ | $${\tfrac {874853}{25920000} }$$ | $${\tfrac {58067611}{1555200000} }$$ |

In this case {@{$\sum _{n=1}^{\infty }\left[{-n \atop -k}\right]=B_{k}$}@} where {@{$B_{k}$ is a [Bell number](Bell%20number.md)}@}, and so one may {@{define the negative Bell numbers by $\sum _{n=1}^{\infty }\left[{-n \atop k}\right]=:B_{-k}$}@}.

For example, this produces $\sum _{n=1}^{\infty }\left[{-n \atop 1}\right]=B_{-1}={\frac {1}{e} }\sum _{j=1}^{\infty }{\frac {1}{j\cdot j!} }={\frac {1}{e} }\int _{0}^{1}{\frac {e^{t}-1}{t} }dt=0.4848291\dots$, generally $B_{-k}={\frac {1}{e} }\sum _{j=1}^{\infty }{\frac {1}{j^{k}j!} }$.

## see also

- [Bell polynomials](Bell%20polynomials.md)
- [Catalan number](Catalan%20number.md)
- [cycles and fixed points](cycles%20and%20fixed%20points.md)
- [Pochhammer symbol](falling%20and%20rising%20factorials.md)
- [polynomial sequence](polynomial%20sequence.md)
- [Touchard polynomials](Touchard%20polynomials.md)
- [Stirling permutation](Stirling%20permutation.md)

## citations

This text incorporates [content](https://en.wikipedia.org/wiki/Stirling_number) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. [Mansour & Schork 2015](#CITEREFMansourSchork2015), p. 5. <a id="^ref-1"></a>^ref-1
2. [Mansour & Schork 2015](#CITEREFMansourSchork2015), p. 4. <a id="^ref-2"></a>^ref-2
3. Ronald L. Graham, Donald E. Knuth, Oren Patashnik \(1988\) _[Concrete Mathematics](Concrete%20Mathematics.md)_, Addison-Wesley, Reading MA. [ISBN](ISBN.md) [0-201-14236-8](https://en.wikipedia.org/wiki/Special:BookSources/0-201-14236-8), p. 244. <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFKnuth1992"></a> Knuth, Donald E. \(1992\). ["Two Notes on Notation"](https://www.jstor.org/stable/2325085). _American Mathematical Monthly_. __99__ \(5\): 403–422. [doi](digital%20object%20identifier.md):[10.2307/2325085](https://doi.org/10.2307%2F2325085). [JSTOR](JSTOR.md) [2325085](https://www.jstor.org/stable/2325085) – via JSTOR. <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFAigner2007"></a> Aigner, Martin \(2007\). "Section 1.2 - Subsets and binomial coefficients". [_A Course in Enumeration_](https://archive.org/details/courseenumeratio00aign_007). Springer. pp. [561](https://archive.org/details/courseenumeratio00aign_007/page/n563). [ISBN](ISBN.md) [978-3-540-39032-9](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-39032-9). <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFSándorCrstici2004"></a> Sándor, Jozsef; Crstici, Borislav \(2004\). [_Handbook of Number Theory II_](https://books.google.com/books?id=B2WZkvmFKk8C&dq=%22Stirling+numbers+of+the+third+kind%22&pg=PA464). [Kluwer Academic Publishers](Springer%20Science+Business%20Media.md#history). p. 464. [ISBN](ISBN.md) [9781402025464](https://en.wikipedia.org/wiki/Special:BookSources/9781402025464). <a id="^ref-6"></a>^ref-6
7. _Concrete Mathematics_ exercise 13 of section 6. Note that this formula immediately implies the first positive-order Stirling number transformation given in the main article on [generating function transformations](generating%20function%20transformation.md#derivative%20transformations). <a id="^ref-7"></a>^ref-7
8. <a id="CITEREFOlverLozierBoisvertClark2010"></a> Olver, Frank; Lozier, Daniel; Boisvert, Ronald; Clark, Charles \(2010\). ["NIST Handbook of Mathematical Functions"](https://www.nist.gov/publications/nist-handbook-mathematical-functions). _NIST Handbook of Mathematical Functions_. \(Section 26.8\) <a id="^ref-8"></a>^ref-8
9. <a id="CITEREFGoldbergNewmanHaynsworth1972"></a> Goldberg, K.; Newman, M; Haynsworth, E. \(1972\), "Stirling Numbers of the First Kind, Stirling Numbers of the Second Kind", in Abramowitz, Milton; Stegun, Irene A. \(eds.\), _Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables, 10th printing_, New York: Dover, pp. 824–825 <a id="^ref-9"></a>^ref-9
10. <a id="CITEREFLoeb1992"></a> Loeb, Daniel E. \(1992\) \[Received 3 Nov 1989\]. ["A generalization of the Stirling numbers"](https://doi.org/10.1016%2F0012-365X%2892%2990318-A). _Discrete Mathematics_. __103__ \(3\): 259–269. [doi](digital%20object%20identifier.md):[10.1016/0012-365X\(92\)90318-A](https://doi.org/10.1016%2F0012-365X%2892%2990318-A). <a id="^ref-10"></a>^ref-10
11. <a id="CITEREFBranson1994"></a> Branson, David \(August 1994\). ["An extension of Stirling numbers"](http://www.fq.math.ca/Scanned/34-3/branson.pdf) \(PDF\). _The Fibonacci Quarterly_. [Archived](https://web.archive.org/web/20110827132927/http://www.fq.math.ca/Scanned/34-3/branson.pdf) \(PDF\) from the original on 2011-08-27. Retrieved Dec 6, 2017. <a id="^ref-11"></a>^ref-11
12. D.E. Knuth, 1992. <a id="^ref-12"></a>^ref-12

## references

- <a id="CITEREFRosen2018"></a> Rosen, Kenneth H., ed. \(2018\), _Handbook of Discrete and Combinatorial Mathematics_, CRC Press, [ISBN](ISBN.md) [978-1-5848-8780-5](https://en.wikipedia.org/wiki/Special:BookSources/978-1-5848-8780-5)
- <a id="CITEREFMansourSchork2015"></a> Mansour, Toufik; Schork, Mathias \(2015\), _Commutation Relations, Normal Ordering, and Stirling Numbers_, CRC Press, [ISBN](ISBN.md) [978-1-4665-7989-7](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4665-7989-7)

## further reading

- <a id="CITEREFAdamchik1997"></a> Adamchik, Victor \(1997\). ["On Stirling Numbers and Euler Sums"](http://www-2.cs.cmu.edu/~adamchik/articles/stirling.pdf) \(PDF\). _Journal of Computational and Applied Mathematics_. __79__: 119–130. [doi](digital%20object%20identifier.md):[10.1016/s0377-0427\(96\)00167-7](https://doi.org/10.1016%2Fs0377-0427%2896%2900167-7). [Archived](https://web.archive.org/web/20041214001155/http://www-2.cs.cmu.edu/~adamchik/articles/stirling.pdf) \(PDF\) from the original on 2004-12-14.
- <a id="CITEREFBenjaminPrestonQuinn2002"></a> Benjamin, Arthur T.; Preston, Gregory O.; Quinn, Jennifer J. \(2002\). ["A Stirling Encounter with Harmonic Numbers"](https://math.hmc.edu/benjamin/wp-content/uploads/sites/5/2019/06/A-Stirling-EnCOUNTer.pdf) \(PDF\). _Mathematics Magazine_. __75__ \(2\): 95–103. [CiteSeerX](CiteSeerX.md) [10.1.1.383.722](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.383.722). [doi](digital%20object%20identifier.md):[10.2307/3219141](https://doi.org/10.2307%2F3219141). [JSTOR](JSTOR.md) [3219141](https://www.jstor.org/stable/3219141). [Archived](https://web.archive.org/web/20200910121921/https://math.hmc.edu/benjamin/wp-content/uploads/sites/5/2019/06/A-Stirling-EnCOUNTer.pdf) \(PDF\) from the original on 2020-09-10.
- <a id="CITEREFBoyadzhiev2012"></a> Boyadzhiev, Khristo N. \(2012\). ["Close encounters with the Stirling numbers of the second kind"](http://www.maa.org/sites/default/files/pdf/upload_library/2/Boyadzhiev-2013.pdf) \(PDF\). _Mathematics Magazine_. __85__ \(4\): 252–266. [arXiv](ArXiv.md):[1806.09468](https://arxiv.org/abs/1806.09468). [doi](digital%20object%20identifier.md):[10.4169/math.mag.85.4.252](https://doi.org/10.4169%2Fmath.mag.85.4.252). [S2CID](Semantic%20Scholar.md#S2CID) [115176876](https://api.semanticscholar.org/CorpusID:115176876). [Archived](https://web.archive.org/web/20150905120358/http://www.maa.org/sites/default/files/pdf/upload_library/2/Boyadzhiev-2013.pdf) \(PDF\) from the original on 2015-09-05.
- <a id="CITEREFComtet1970"></a> Comtet, Louis \(1970\). ["Valeur de _s_\(_n_, <!-- markdown separator -->_k_\)"](http://www.techniques-ingenieur.fr/page/af202niv10002/permutations.html#2.2). _Analyse Combinatoire, Tome Second_ \(in French\): 51.
- <a id="CITEREFComtet1974"></a> Comtet, Louis \(1974\). [_Advanced Combinatorics: The Art of Finite and Infinite Expansions_](https://archive.org/details/Comtet_Louis_-_Advanced_Coatorics). Dordrecht-Holland/Boston-U.S.A.: Reidel Publishing Company. [ISBN](ISBN.md) [9789027703804](https://en.wikipedia.org/wiki/Special:BookSources/9789027703804).
- <a id="CITEREFHsien-Kuei Hwang1995"></a> Hsien-Kuei Hwang \(1995\). ["Asymptotic Expansions for the Stirling Numbers of the First Kind"](http://citeseer.ist.psu.edu/577040.html). _Journal of Combinatorial Theory, Series A_. __71__ \(2\): 343–351. [doi](digital%20object%20identifier.md):[10.1016/0097-3165\(95\)90010-1](https://doi.org/10.1016%2F0097-3165%2895%2990010-1).
- <a id="CITEREFKnuth1992"></a> [Knuth, D.E.](Donald%20Knuth.md) \(1992\), "Two notes on notation", _Amer. Math. Monthly_, __99__ \(5\): 403–422, [arXiv](ArXiv.md):[math/9205211](https://arxiv.org/abs/math/9205211), [doi](digital%20object%20identifier.md):[10.2307/2325085](https://doi.org/10.2307%2F2325085), [JSTOR](JSTOR.md) [2325085](https://www.jstor.org/stable/2325085), [S2CID](Semantic%20Scholar.md#S2CID) [119584305](https://api.semanticscholar.org/CorpusID:119584305)
- <a id="CITEREFMiksa1956"></a> Miksa, Francis L. \(January 1956\). "Stirling numbers of the first kind: 27 leaves reproduced from typewritten manuscript on deposit in the UMT File". _Mathematical Tables and Other Aids to Computation: Reviews and Descriptions of Tables and Books_. __10__ \(53\): 37–38. [JSTOR](JSTOR.md) [2002617](https://www.jstor.org/stable/2002617).
- <a id="CITEREFMiksa1972"></a> Miksa, Francis L. \(1972\) \[1964\]. ["Combinatorial Analysis, Table 24.4, Stirling Numbers of the Second Kind"](http://www.convertit.com/Go/ConvertIt/Reference/AMS55.ASP). In Abramowitz, Milton; Stegun, Irene A. \(eds.\). _Handbook of Mathematical Functions \(with Formulas, Graphs and Mathematical Tables\)_. 55. U.S. Dept. of Commerce, National Bureau of Standards, Applied Math. p. 835.
- <a id="CITEREFMitrinović1959"></a> Mitrinović, Dragoslav S. \(1959\). ["Sur les nombres de Stirling de première espèce et les polynômes de Stirling"](http://pefmath2.etf.bg.ac.rs/files/23/23.pdf) \(PDF\). _Publications de la Faculté d'Electrotechnique de l'Université de Belgrade, Série Mathématiques et Physique_ \(in French\) \(23\): 1–20. [ISSN](ISSN.md) [0522-8441](https://search.worldcat.org/issn/0522-8441). [Archived](https://web.archive.org/web/20090617034106/http://pefmath2.etf.bg.ac.rs/files/23/23.pdf) \(PDF\) from the original on 2009-06-17.
- <a id="CITEREFO'ConnorRobertson1998"></a> O'Connor, John J.; Robertson, Edmund F. \(September 1998\). ["James Stirling \(1692–1770\)"](https://mathshistory.st-andrews.ac.uk/Biographies/Stirling/).
- <a id="CITEREFSixdeniersPensonSolomon2001"></a> Sixdeniers, J. M.; Penson, K. A.; Solomon, A. I. \(2001\). ["Extended Bell and Stirling Numbers From Hypergeometric Exponentiation"](http://www.cs.uwaterloo.ca/journals/JIS/VOL4/SIXDENIERS/bell.pdf) \(PDF\). _Journal of Integer Sequences_. __4__: 01.1.4. [arXiv](ArXiv.md):[math/0106123](https://arxiv.org/abs/math/0106123). [Bibcode](bibcode.md):[2001JIntS...4...14S](https://ui.adsabs.harvard.edu/abs/2001JIntS...4...14S).
- <a id="CITEREFSpivey2007"></a> Spivey, Michael Z. \(2007\). ["Combinatorial sums and finite differences"](https://doi.org/10.1016%2Fj.disc.2007.03.052). _Discrete Math_. __307__ \(24\): 3130–3146. [CiteSeerX](CiteSeerX.md) [10.1.1.134.8665](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.134.8665). [doi](digital%20object%20identifier.md):[10.1016/j.disc.2007.03.052](https://doi.org/10.1016%2Fj.disc.2007.03.052).
- <a id="CITEREFSloane "A008275""></a> [Sloane, N. J. A.](Neil%20Sloane.md) \(ed.\). ["Sequence A008275 \(Stirling numbers of first kind\)"](https://oeis.org/A008275). _The [On-Line Encyclopedia of Integer Sequences](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)_. OEIS Foundation.
- <a id="CITEREFSloane "A008277""></a> [Sloane, N. J. A.](Neil%20Sloane.md) \(ed.\). ["Sequence A008277 \(Stirling numbers of 2nd kind\)"](https://oeis.org/A008277). _The [On-Line Encyclopedia of Integer Sequences](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)_. OEIS Foundation.
