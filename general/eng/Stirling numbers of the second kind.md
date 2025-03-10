---
aliases:
  - Stirling number of the second kind
  - Stirling numbers of the second kind
  - Stirling partition number
  - Stirling partition numbers
tags:
  - flashcard/active/general/eng/Stirling_numbers_of_the_second_kind
  - language/in/English
---

# Stirling numbers of the second kind

In [mathematics](mathematics.md), particularly in {@{[combinatorics](combinatorics.md)}@}, {@{a __Stirling number of the second kind__ (or __Stirling partition number__)}@} is {@{the number of ways to [partition a set](partition%20of%20a%20set.md) of _n_ objects into _k_ non-empty subsets}@} and is denoted by {@{$S(n,k)$ or $\textstyle \left\{ {n \atop k}\right\}$}@}.<sup>[\[1\]](#^ref-1)</sup> Stirling numbers of the second kind occur in {@{the field of [mathematics](mathematics.md) called [combinatorics](combinatorics.md) and the study of [partitions](integer%20partition.md)}@}. They are named {@{after [James Stirling](James%20Stirling%20(mathematician).md)}@}. <!--SR:!2025-12-05,309,330!2025-12-05,309,330!2025-12-12,316,330!2025-12-09,313,330!2025-08-28,213,310!2025-12-01,306,330-->

{@{The Stirling numbers of the [first](Stirling%20numbers%20of%20the%20first%20kind.md) and second kind}@} can be {@{understood as inverses of one another when viewed as [triangular matrices](triangular%20matrix.md)}@}. This article is {@{devoted to specifics of Stirling numbers of the second kind}@}. {@{Identities linking the two kinds}@} appear in the article on [Stirling numbers](Stirling%20number.md). <!--SR:!2025-11-27,303,330!2025-11-26,303,330!2025-11-26,303,330!2025-12-09,314,330-->

## definition

{@{The Stirling numbers of the second kind}@}, written {@{$S(n,k)$ or $\lbrace \textstyle {n \atop k}\rbrace$ or with other notations}@}, count {@{the number of ways to [partition](partition%20of%20a%20set.md) a [set](set%20(mathematics).md) of $n$ labelled objects into $k$ nonempty unlabelled subsets}@}. Equivalently, they count {@{the number of different [equivalence relations](equivalence%20relation.md) with precisely $k$ equivalence classes that can be defined on an $n$ element set}@}. In fact, there is {@{a [bijection](bijection.md) between the set of partitions and the set of equivalence relations on a given set}@}. Obviously, <p> {@{$\left\{ {n \atop n}\right\}=1$ for _n_ ≥ 0, and $\left\{ {n \atop 1}\right\}=1$ for _n_ ≥ 1}@}, <p> as {@{the only way to partition an _n_-element set into _n_ parts is to put each element of the set into its own part}@}, and {@{the only way to partition a nonempty set into one part is to put all of the elements in the same part}@}. Unlike {@{[Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md)}@}, they can be {@{calculated using a one-sum formula:<sup>[\[2\]](#^ref-2)</sup> $$\left\{ {n \atop k}\right\}={\frac {1}{k!} }\sum _{i=0}^{k}(-1)^{k-i}{\binom {k}{i} }i^{n}=\sum _{i=0}^{k}{\frac {(-1)^{k-i}i^{n} }{(k-i)!i!} }.$$}@} <!--SR:!2025-11-30,305,330!2025-11-20,298,330!2025-11-19,297,330!2025-12-11,315,330!2025-12-12,316,330!2025-12-03,307,330!2025-12-10,314,330!2025-11-08,287,330!2025-07-25,202,310!2025-05-25,126,250-->

{@{The Stirling numbers of the first kind}@} may be characterized as {@{the numbers that arise when one expresses powers of an indeterminate _x_ in terms of the [falling factorials](falling%20and%20rising%20factorials.md)<sup>[\[3\]](#^ref-3)</sup> $$(x)_{n}=x(x-1)(x-2)\cdots (x-n+1).$$}@} (In particular, {@{(_x_)<sub>0</sub> = 1 because it is an [empty product](empty%20product.md)}@}.) <!--SR:!2025-09-12,226,310!2025-11-26,303,330!2025-11-30,306,330-->

{@{Stirling numbers of the second kind}@} satisfy {@{the relation $$\sum _{k=0}^{n}\left\{ {n \atop k}\right\}(x)_{k}=x^{n}.$$}@} <!--SR:!2025-12-08,312,330!2025-03-31,100,270-->

## notation

{@{Various notations}@} have been used for {@{Stirling numbers of the second kind}@}. {@{The brace notation $\textstyle \lbrace {n \atop k}\rbrace$}@} was {@{used by Imanuel Marx and Antonio Salmeri in 1962 for variants of these numbers}@}.<sup>[\[4\]](#^ref-4)</sup><sup>[\[5\]](#^ref-5)</sup> This led {@{[Knuth](Donald%20Knuth.md) to use it, as shown here, in the first volume of _[The Art of Computer Programming](The%20Art%20of%20Computer%20Programming.md)_ (1968)}@}.<sup>[\[6\]](#^ref-6)</sup><sup>[\[7\]](#^ref-7)</sup> According to the third edition of _The Art of Computer Programming_, this notation was {@{also used earlier by [Jovan Karamata](Jovan%20Karamata.md) in 1935}@}.<sup>[\[8\]](#^ref-8)</sup><sup>[\[9\]](#^ref-9)</sup> {@{The notation _S_(_n_, _k_)}@} was used by {@{[Richard Stanley](Richard%20P.%20Stanley.md) in his book _[Enumerative Combinatorics](enumerative%20combinatorics.md)_ and also, much earlier, by many other writers}@}.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2025-11-29,303,330!2025-12-11,315,330!2025-11-29,305,330!2025-03-28,97,270!2025-09-11,224,310!2025-12-09,313,330!2025-12-12,316,330!2025-09-05,220,310-->

The notations used on this page for Stirling numbers are {@{not universal, and may conflict with notations in other sources}@}. <!--SR:!2025-09-02,217,310-->

## relation to Bell numbers

- see: [Bell number](Bell%20number.md)

Since {@{the Stirling number $\left\{ {n \atop k}\right\}$ counts set partitions of an _n_-element set into _k_ parts}@}, {@{the sum $$B_{n}=\sum _{k=0}^{n}\left\{ {n \atop k}\right\}$$ over all values of _k_}@} is {@{the total number of partitions of a set with _n_ members}@}. This number is {@{known as the _n_-th [Bell number](Bell%20number.md)}@}. <!--SR:!2025-12-01,307,330!2025-12-08,313,330!2025-11-07,286,330!2025-08-28,213,310-->

Analogously, {@{the [ordered Bell numbers](ordered%20Bell%20number.md)}@} can be computed from {@{the Stirling numbers of the second kind via $$a_{n}=\sum _{k=0}^{n}k!\left\{ {n \atop k}\right\}.$$}@}<sup>[\[10\]](#^ref-10)</sup> <!--SR:!2025-11-21,299,330!2025-05-09,139,290-->

## table of values

Below is {@{a [triangular array](triangular%20array.md) of values for the Stirling numbers of the second kind}@} (sequence {@{[A008277](https://oeis.org/A008277)}@} in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)): <!--SR:!2025-09-06,219,310!2025-05-25,76,250-->

| ___k___\\___n___ | __0__ | __1__ | __2__ | __3__ | __4__ | __5__ | __6__ | __7__ | __8__ | __9__ | __10__ |
| ----------------:| -----:| -----:| -----:| -----:| -----:| -----:| -----:| -----:| -----:| -----:| ------:|
| __0__            | 1     |       |       |       |       |       |       |       |       |       |        |
| __1__            | 0     | 1     |       |       |       |       |       |       |       |       |        |
| __2__            | 0     | 1     | 1     |       |       |       |       |       |       |       |        |
| __3__            | 0     | 1     | 3     | 1     |       |       |       |       |       |       |        |
| __4__            | 0     | 1     | 7     | 6     | 1     |       |       |       |       |       |        |
| __5__            | 0     | 1     | 15    | 25    | 10    | 1     |       |       |       |       |        |
| __6__            | 0     | 1     | 31    | 90    | 65    | 15    | 1     |       |       |       |        |
| __7__            | 0     | 1     | 63    | 301   | 350   | 140   | 21    | 1     |       |       |        |
| __8__            | 0     | 1     | 127   | 966   | 1701  | 1050  | 266   | 28    | 1     |       |        |
| __9__            | 0     | 1     | 255   | 3025  | 7770  | 6951  | 2646  | 462   | 36    | 1     |        |
| __10__           | 0     | 1     | 511   | 9330  | 34105 | 42525 | 22827 | 5880  | 750   | 45    | 1      |

As with {@{the [binomial coefficients](binomial%20coefficient.md)}@}, this table {@{could be extended to _k_ > _n_, but the entries would all be 0}@}. <!--SR:!2025-11-02,282,330!2025-11-28,304,330-->

## properties

### recurrence relation

Stirling numbers of the second kind {@{obey the recurrence relation $$\left\{ {n+1 \atop k}\right\}=k\left\{ {n \atop k}\right\}+\left\{ {n \atop k-1}\right\}\quad {\text{for} }\;0<k<n$$}@} with {@{initial conditions $$\left\{ {n \atop n}\right\}=1\quad {\text{ for} }\;n\geq 0\quad {\text{ and } }\quad \left\{ {n \atop 0}\right\}=\left\{ {0 \atop n}\right\}=0\quad {\text{ for } }n>0{\text{.} }$$}@} <!--SR:!2025-05-18,134,290!2025-12-06,310,330-->

For instance, the number 25 in column _k_ = 3 and row _n_ = 5 is given by 25 = 7 + (3×6), where 7 is the number above and to the left of 25, 6 is the number above 25 and 3 is the column containing the 6.

To prove this recurrence, observe that {@{a partition of the ⁠$n+1$⁠ objects into _k_ nonempty subsets either contains the ⁠$(n+1)$⁠-th object as a singleton or it does not}@}. The number of ways that the singleton is {@{one of the subsets is given by $$\left\{ {n \atop k-1}\right\}$$ since we must partition the remaining _n_ objects into the available ⁠$k-1$⁠ subsets}@}. In the other case {@{the ⁠$(n+1)$⁠-th object belongs to a subset containing other objects}@}. The number of ways is {@{given by $$k\left\{ {n \atop k}\right\}$$}@} since {@{we partition all objects other than the ⁠$(n+1)$⁠-th into _k_ subsets, and then we are left with _k_ choices for inserting object ⁠$n+1$}@}⁠. {@{Summing these two values}@} gives the desired result. <!--SR:!2025-12-10,314,330!2025-08-26,211,310!2025-12-10,314,330!2025-11-28,302,330!2025-11-25,303,330!2025-07-19,197,310-->

Another recurrence relation is {@{given by $$\left\lbrace {\begin{matrix}n\\k\end{matrix} }\right\rbrace ={\frac {k^{n} }{k!} }-\sum _{r=0}^{k-1}{\frac {\left\lbrace {\begin{matrix}n\\r\end{matrix} }\right\rbrace }{(k-r)!} }\,,$$}@} which follows from evaluating $\sum _{r=0}^{n}\left\{ {n \atop r}\right\}(x)_{r}=x^{n}$ at $x=k$. (annotation: The details are {@{$$\begin{aligned} \sum_{r = 0}^n \begin{Bmatrix} n \\ r \end{Bmatrix} (x)_r & = x^n \\ \sum_{r = 0}^n \begin{Bmatrix} n \\ r \end{Bmatrix} (k)_r & = k^n \\ \begin{Bmatrix} n \\ k \end{Bmatrix} (k)_k & = k^n - \sum_{r = 0}^{k - 1} \begin{Bmatrix} n \\ r \end{Bmatrix} (k)_r - \sum_{r = k + 1}^n \begin{Bmatrix} n \\ r \end{Bmatrix} (k)_r \\ \begin{Bmatrix} n \\ k \end{Bmatrix} k! & = k^n - \sum_{r = 0}^{k - 1} \begin{Bmatrix} n \\ r \end{Bmatrix} (k)_r && (k)_r = 0\text{ for }r > k \\ \begin{Bmatrix} n \\ k \end{Bmatrix} & = \frac {k^n} {k!} - \sum_{r = 0}^{k - 1} \begin{Bmatrix} n \\ r \end{Bmatrix} \frac 1 {(k - r)!} \,. \end{aligned}$$}@}) <!--SR:!2025-06-25,133,230!2025-03-26,95,270-->

### simple identities

Some simple identities include {@{$$\left\{ {n \atop n-1}\right\}={\binom {n}{2} }.$$}@} This is because {@{dividing _n_ elements into _n_ − 1 sets necessarily means dividing it into one set of size 2 and _n_ − 2 sets of size 1. Therefore we need only pick those two elements}@}; <!--SR:!2025-11-03,283,330!2025-11-18,296,330-->

and {@{$$\left\{ {n \atop 2}\right\}=2^{n-1}-1.$$}@} To see this, first note that {@{there are 2<sup>_n_</sup> _ordered_ pairs of complementary subsets _A_ and _B_}@}. In one case, {@{_A_ is empty, and in another _B_ is empty, so 2<sup>_n_</sup> − 2 ordered pairs of subsets remain}@}. Finally, since {@{we want _unordered_ pairs rather than _ordered_ pairs we divide this last number by 2}@}, giving the result above. <!--SR:!2025-07-10,186,310!2025-07-24,201,310!2025-11-26,303,330!2025-08-20,206,310-->

{@{Another explicit expansion of the recurrence-relation}@} gives {@{identities in the spirit of the above example}@}. <!--SR:!2025-11-21,299,330!2025-09-01,216,310-->

### identities

{@{The table in section 6.1 of _Concrete Mathematics_}@} provides {@{a plethora of generalized forms of finite sums involving the Stirling numbers}@}. Several particular finite sums relevant to this article include <!--SR:!2025-12-02,306,330!2025-09-03,218,310-->

- increment by binomial coefficient ::@:: $$\left\{ {n+1 \atop k+1}\right\}=\sum _{j=k}^{n}{n \choose j}\left\{ {j \atop k}\right\}$$ (annotation: Choose _n_ - _j_ elements from _n_ + 1 elements to form a maybe empty partition. Add the 1 element to ensure it is nonempty. Partition the remaining _j_ elements into _k_ partitions.) <!--SR:!2025-03-24,93,270!2025-09-05,219,310-->
- increment by combinatorial argument ::@:: $$\left\{ {n+1 \atop k+1}\right\}=\sum _{j=k}^{n}(k+1)^{n-j}\left\{ {j \atop k}\right\}$$ (annotation: Choose _n_ - _j_ elements from _n_ + 1 elements. They may be assigned to any of the _k_ + 1 partitions. Partition the remaining _j_ elements into _k_ partitions. Assign the extra element to ensure the the extra partition is nonempty.) <!--SR:!2025-03-17,93,270!2025-03-28,97,270-->
- increment by summing up to _k_ ::@:: $$\left\{ {n+k+1 \atop k}\right\}=\sum _{j=0}^{k}j\left\{ {n+j \atop j}\right\}$$ <!--SR:!2025-03-27,96,270!2025-10-03,218,270-->
- partition then choose partitions ::@:: $$\left\{ {n \atop \ell +m}\right\}{\binom {\ell +m}{\ell } }=\sum _{k}{\binom {n}{k} }\left\{ {k \atop \ell }\right\}\left\{ {n-k \atop m}\right\}$$ (annotation: Choose _k_ elements from _n_ elements. Partition _k_ elements into the chosen _l_ partitions. Partition the remaining _n_ − _k_ elements into the unchosen _m_ partitions.) <!--SR:!2025-05-25,144,290!2025-09-10,223,310-->

### explicit formula

{@{The Stirling numbers of the second kind}@} are given by the explicit formula: {@{$$\left\{ {n \atop k}\right\}={\frac {1}{k!} }\sum _{j=0}^{k}(-1)^{k-j}{k \choose j}j^{n}=\sum _{j=0}^{k}{\frac {(-1)^{k-j}j^{n} }{(k-j)!j!} }.$$}@}
This can be derived by {@{using [inclusion-exclusion](inclusion–exclusion%20principle.md) to count the surjections from _n_ to _k_ and using the fact that the number of such surjections is $k!\left\{ {n \atop k}\right\}$}@}. <!--SR:!2025-09-04,218,310!2025-06-23,144,250!2025-09-05,218,310-->

Additionally, this formula is {@{a special case of the _k_-th [forward difference](finite%20difference.md) of the [monomial](monomial.md) $x^{n}$ evaluated at _x_ = 0}@}: {@{$$\Delta ^{k}x^{n}=\sum _{j=0}^{k}(-1)^{k-j}{k \choose j}(x+j)^{n}.$$}@} Because {@{the [Bernoulli polynomials](Bernoulli%20polynomials.md) may be written in terms of these forward differences}@}, one {@{immediately obtains a relation in the [Bernoulli numbers](bernoulli%20number.md)}@}: {@{$$B_{m}(0) = \sum_{k = 0}^m \frac {(-1)^k} {k + 1} \left.\left(\Delta^k x^m\right)\right|_{x = 0} = \sum _{k=0}^{m}{\frac {(-1)^{k}k!}{k+1} }\left\{ {m \atop k}\right\}.$$}@} <!--SR:!2025-03-27,96,270!2025-05-20,121,250!2025-05-21,136,290!2025-05-21,139,290!2025-03-17,80,230-->

The evaluation of {@{incomplete exponential [Bell polynomial](Bell%20polynomials.md) _B_<sub>_n_,_k_</sub>(_x_<sub>1</sub>,_x_<sub>2</sub>,...) on the sequence of ones}@} equals {@{a Stirling number of the second kind: $$\left\{ {n \atop k}\right\}=B_{n,k}(1,1,\dots ,1) \,.$$}@} <!--SR:!2025-08-24,209,310!2025-03-23,92,270-->

Another explicit formula given in {@{the _NIST Handbook of Mathematical Functions_}@} is {@{$$\left\{ {n \atop k}\right\}=\sum _{\begin{array}{c}c_{1}+\ldots +c_{k}=n-k\\c_{1},\ldots ,\ c_{k}\ \geq \ 0\end{array} }1^{c_{1} }2^{c_{2} }\cdots k^{c_{k} } \,.$$}@} <!--SR:!2025-12-12,316,330!2025-04-12,56,230-->

### parity

{@{The [parity](parity%20(mathematics).md) of a Stirling number of the second kind}@} is {@{same as the parity of a related [binomial coefficient](binomial%20coefficient.md)}@}: <p> {@{$\left\{ {n \atop k}\right\}\equiv {\binom {z}{w} }\ {\pmod {2} },$ where $z=n-\left\lceil \displaystyle {\frac {k+1}{2} }\right\rceil ,\ w=\left\lfloor \displaystyle {\frac {k-1}{2} }\right\rfloor .$}@} This relation is specified by {@{mapping _n_ and _k_ coordinates onto the [Sierpiński triangle](Sierpiński%20triangle.md)}@}. <!--SR:!2025-07-15,191,310!2025-04-24,89,290!2025-06-01,130,250!2025-07-14,190,310-->

More directly, let {@{two sets contain positions of 1's in binary representations of results of respective expressions}@}: {@{$${\begin{aligned}\mathbb {A} :\ \sum _{i\in \mathbb {A} }2^{i}&=n-k,\\\mathbb {B} :\ \sum _{j\in \mathbb {B} }2^{j}&=\left\lfloor {\dfrac {k-1}{2} }\right\rfloor .\\\end{aligned} }$$}@} One can {@{mimic a [bitwise AND](bitwise%20operation.md#AND) operation by intersecting these two sets: $${\begin{Bmatrix}n\\k\end{Bmatrix} }\,{\bmod {\,} }2={\begin{cases}0,&\mathbb {A} \cap \mathbb {B} \neq \emptyset ;\\1,&\mathbb {A} \cap \mathbb {B} =\emptyset ;\end{cases} }$$}@} to {@{obtain the parity of a Stirling number of the second kind in [_O_(1)](Big%20O%20notation.md) time}@}. In {@{[pseudocode](pseudocode.md): $${\begin{Bmatrix}n\\k\end{Bmatrix} }\,{\bmod {\,} }2:=\left[\left(\left(n-k\right)\ \And \ \left(\left(k-1\right)\,\mathrm {div} \,2\right)\right)=0\right];$$}@} where {@{$\left[b\right]$ is the [Iverson bracket](Iverson%20bracket.md)}@}. <!--SR:!2025-03-25,107,290!2025-03-30,99,270!2025-09-13,226,310!2025-08-21,208,310!2025-05-23,124,250!2025-07-13,189,310-->

{@{The parity of a central Stirling number of the second kind $\textstyle \left\{ {2n \atop n}\right\}$ is odd}@} if and only if {@{$n$ is a [fibbinary number](fibbinary%20number.md), a number whose [binary representation](binary%20number.md) has no two consecutive 1s}@}.<sup>[\[11\]](#^ref-11)</sup> <!--SR:!2025-03-26,95,270!2025-06-18,104,290-->

### generating functions

For {@{a fixed integer _n_}@}, {@{the [ordinary generating function](generating%20function.md#Ordinary%20generating%20function%20(OGF)) for Stirling numbers of the second kind $\left\{ {n \atop 0}\right\},\left\{ {n \atop 1}\right\},\ldots$}@} is {@{given by $$\sum _{k=0}^{n}\left\{ {n \atop k}\right\}x^{k}=T_{n}(x),$$}@} where {@{$T_{n}(x)$ are [Touchard polynomials](Touchard%20polynomials.md)}@}. If {@{one sums the Stirling numbers against the falling factorial instead}@}, one can show the following identities, among others: {@{$$\sum _{k=0}^{n}\left\{ {n \atop k}\right\}(x)_{k}=x^{n}$$ and $$\sum _{k=0}^n\left\{ {n+1 \atop k + 1}\right\}(x)_k=(x + 1)^{n},$$}@} which has special case {@{$$\sum _{k=0}^{n}\left\{ {n \atop k}\right\}(n)_{k}=n^{n}.$$}@} <!--SR:!2025-12-11,315,330!2025-11-08,288,330!2025-08-02,209,310!2025-05-09,139,290!2025-05-24,142,290!2025-07-09,145,250!2025-03-30,99,270-->

For {@{a fixed integer _k_}@}, {@{the Stirling numbers of the second kind}@} have {@{rational ordinary generating function $$\sum _{n=k}^{\infty }\left\{ {n \atop k}\right\}x^{n-k}=\prod _{r=1}^{k}{\frac {1}{1-rx} }={\frac {1}{x^{k+1}(1/x)_{k+1} } }$$}@} and have {@{an [exponential generating function](generating%20function.md#Exponential%20generating%20function%20(EGF)) given by $$\sum _{n=k}^{\infty }\left\{ {n \atop k}\right\}{\frac {x^{n} }{n!} }={\frac {(e^{x}-1)^{k} }{k!} }.$$}@} <!--SR:!2025-08-04,211,310!2025-05-02,134,290!2025-04-30,56,210!2025-03-29,98,270-->

{@{A mixed bivariate generating function for the Stirling numbers of the second kind}@} is {@{$$\sum _{k=0}^{\infty }\sum _{n=k}^{\infty }\left\{ {n \atop k}\right\}{\frac {x^{n} }{n!} }y^{k} = \sum_{k = 0}^\infty \frac {\left(y\left(e^x - 1 \right)\right)^k} {k!} =e^{y(e^{x}-1)}.$$}@} <!--SR:!2025-03-29,98,270!2025-05-21,122,250-->

### lower and upper bounds

If {@{$n\geq 2$ and $1\leq k\leq n-1$}@}, then {@{$${\frac {1}{2} }(k^{2}+k+2)k^{n-k-1}-1\leq \left\{ {n \atop k}\right\}\leq {\frac {1}{2} }{n \choose k}k^{n-k}$$}@} <sup>[\[12\]](#^ref-12)</sup> <!--SR:!2025-03-25,94,270!2025-03-19,14,150-->

### asymptotic approximation

For {@{fixed value of $k$}@}, the asymptotic value of the Stirling numbers of the second kind as $n\rightarrow \infty$ is {@{given by $$\left\{ {n \atop k}\right\}{\underset {n\to \infty }{\sim } }{\frac {k^{n} }{k!} }.$$}@} <!--SR:!2025-04-28,132,290!2025-03-22,25,170-->

If {@{$n=o({\sqrt {k} })$ (where _o_ denotes the [little o notation](big%20O%20notation.md#little-o%20notation))}@} then {@{$$\left\{ {n+k \atop k}\right\}{\underset {k\to \infty }{\sim } }{\frac {k^{2n} }{2^{n}n!} }.$$}@}<sup>[\[13\]](#^ref-13)</sup> <!--SR:!2025-03-20,24,230!2025-05-22,123,250-->

{@{A uniformly valid approximation}@} also exists: for {@{all _k_ such that 1 < _k_ < _n_}@}, one has $$\left\{ {n \atop k}\right\}\sim {\sqrt {\frac {v-1}{v(1-G)} } }\left({\frac {v-1}{v-G} }\right)^{n-k}{\frac {k^{n} }{n^{k} } }e^{k(1-G)}\left({n \atop k}\right),$$ where {@{$v=n/k$, and $G\in (0,1)$ is the unique solution to $G=ve^{G-v}$}@}.<sup>[\[14\]](#^ref-14)</sup> Relative error is {@{bounded by about $0.066/n$}@}. <!--SR:!2025-07-12,188,310!2025-11-28,303,330!2025-05-20,121,250!2025-05-24,125,250-->

### unimodality

For {@{fixed $n$}@}, $\left\{ {n \atop k}\right\}$ is {@{unimodal, that is, the sequence increases and then decreases}@}. The maximum is {@{attained for at most two consecutive values of _k_}@}. That is, there is {@{an integer $k_{n}$ such that $$\left\{ {n \atop 1}\right\}<\left\{ {n \atop 2}\right\}<\cdots <\left\{ {n \atop k_{n} }\right\}\geq \left\{ {n \atop k_{n}+1}\right\}>\cdots >\left\{ {n \atop n}\right\}.$$}@} Looking at the table of values above, {@{the first few values for $k_{n}$}@} are {@{$0,1,1,2,2,3,3,4,4,4,5,\ldots$}@} <!--SR:!2025-11-25,303,330!2025-09-12,225,310!2025-12-04,308,330!2025-08-16,205,310!2025-09-09,222,310!2025-07-06,137,230-->

When {@{$n$ is large}@}, {@{$$k_{n}{\underset {n\to \infty }{\sim } }{\frac {n}{\log n} },$$}@} and {@{the maximum value of the Stirling number}@} can be {@{approximated with $$\log \left\{ {n \atop k_{n} }\right\}=n\log n-n\log \log n-n+O(n\log \log n/\log n).$$}@} <sup>[\[12\]](#^ref-12)</sup> <!--SR:!2025-08-29,214,310!2025-06-26,120,250!2025-05-24,139,290!2025-03-23,85,230-->

## applications

### moments of the Poisson distribution

If {@{_X_ is a [random variable](random%20variable.md) with a [Poisson distribution](Poisson%20distribution.md) with [expected value](expected%20value.md) λ}@}, then {@{its _n_-th [moment](moment%20(mathematics).md) is $$E(X^{n})=\sum _{k=0}^{n}\left\{ {n \atop k}\right\}\lambda ^{k}.$$}@} In particular, {@{the _n_-th moment of the Poisson distribution with expected value 1}@} is {@{precisely the number of [partitions of a set](partition%20of%20a%20set.md) of size _n_, i.e., it is the _n_-th [Bell number](Bell%20number.md) (this fact is [Dobiński's formula](Dobiński's%20formula.md))}@}. <!--SR:!2025-05-22,137,290!2025-05-23,138,290!2025-07-07,169,270!2025-03-28,97,270-->

### moments of fixed points of random permutations

Let {@{the random variable _X_ be the number of fixed points of a [uniformly distributed](discrete%20uniform%20distribution.md) [random permutation](random%20permutation.md) of a finite set of size _m_}@}. Then the _n_-th moment of _X_ is {@{$$E(X^{n})=\sum _{k=0}^{m}\left\{ {n \atop k}\right\}.$$ <p> __Note:__ The upper bound of summation is _m_, not _n_}@}. <!--SR:!2025-03-27,96,270!2025-03-25,94,270-->

In other words, {@{the _n_-th moment of this [probability distribution](probability%20distribution.md)}@} is {@{the number of partitions of a set of size _n_ into no more than _m_ parts}@}. This is proved in the article on [random permutation statistics](random%20permutation%20statistics.md#moments%20of%20fixed%20points), although the notation is a bit different. <!--SR:!2025-08-25,211,310!2025-06-24,145,250-->

### rhyming schemes

{@{The Stirling numbers of the second kind}@} can represent {@{the total number of [rhyme schemes](rhyme%20scheme.md) for a poem of _n_ lines}@}. {@{$S(n,k)$}@} gives {@{the number of possible rhyming schemes for _n_ lines using _k_ unique rhyming syllables}@}. As an example, for {@{a poem of 3 lines}@}, there is {@{1 rhyme scheme using just one rhyme (aaa), 3 rhyme schemes using two rhymes (aab, aba, abb), and 1 rhyme scheme using three rhymes (abc)}@}. <!--SR:!2025-12-01,305,330!2025-09-03,217,310!2025-12-06,310,330!2025-09-13,227,310!2025-12-12,316,330!2025-11-29,304,330-->

## variants

### _r_-Stirling numbers of the second kind

{@{The _r_-Stirling number of the second kind $\left\{ {n \atop k}\right\}_{r}$}@} counts {@{the number of partitions of a set of _n_ objects into _k_ non-empty disjoint subsets, such that the first _r_ elements are in distinct subsets}@}.<sup>[\[15\]](#^ref-15)</sup> These numbers {@{satisfy the recurrence relation $$\left\{ {n \atop k}\right\}_{r}=k\left\{ {n-1 \atop k}\right\}_{r}+\left\{ {n-1 \atop k-1}\right\}_{r}$$}@} Some combinatorial identities and a connection between these numbers and context-free grammars can be found in <sup>[\[16\]](#^ref-16)</sup>. <!--SR:!2025-06-24,120,250!2025-05-22,137,290!2025-05-20,135,290-->

### associated Stirling numbers of the second kind

{@{An _r_-associated Stirling number of the second kind}@} is {@{the number of ways to partition a set of _n_ objects into _k_ subsets, with each subset containing at least _r_ elements}@}.<sup>[\[17\]](#^ref-17)</sup> It is denoted by {@{$S_{r}(n,k)$}@} and obeys {@{the recurrence relation $$S_{r}(n+1,k)=k\ S_{r}(n,k)+{\binom {n}{r-1} }S_{r}(n-r+1,k-1)$$}@} (annotation: The first term {@{counts the number of ways to add an element to an existing partition, while the second term counts the number of ways to create a new partition with _r_ − 1 elements and the new element}@}.) <!--SR:!2025-04-01,63,270!2025-06-21,103,270!2025-12-07,311,330!2025-05-19,120,250!2025-05-24,139,290-->

{@{The 2-associated numbers}@} (sequence {@{[A008299](https://oeis.org/A008299)}@} in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)) appear elsewhere as {@{"Ward numbers" and as the magnitudes of the coefficients of [Mahler polynomials](Mahler%20polynomial.md)}@}. <!--SR:!2025-05-26,143,290!2025-06-25,121,250!2025-03-30,61,270-->

### reduced Stirling numbers of the second kind

Denote {@{the _n_ objects to partition by the integers 1, 2, ..., _n_}@}. Define {@{the reduced Stirling numbers of the second kind, denoted $S^{d}(n,k)$}@}, to be {@{the number of ways to partition the integers 1, 2, ..., _n_ into _k_ nonempty subsets such that all elements in each subset have pairwise distance at least _d_}@}. That is, for {@{any integers _i_ and _j_ in a given subset}@}, it is {@{required that $|i-j|\geq d$}@}. It has been shown that these numbers {@{satisfy $$S^{d}(n,k)=S(n-d+1,k-d+1),n\geq k\geq d$$ (hence the name "reduced")}@}.<sup>[\[18\]](#^ref-18)</sup> (annotation: This can be proved by {@{proving bases cases and their connections to the familiar Stirling numbers numbers of the second kind, derive a recurrence relation (simpler than you think, if you consider adding a last element _n_), and then prove by induction}@}.) Observe {@{(both by definition and by the reduction formula), that $S^{1}(n,k)=S(n,k)$, the familiar Stirling numbers of the second kind}@}. <!--SR:!2025-12-08,312,330!2025-11-30,304,330!2025-12-12,316,330!2025-07-11,187,310!2025-12-07,311,330!2025-05-28,128,250!2025-09-08,221,310!2025-11-20,299,330-->

## see also

- [Stirling number](Stirling%20number.md)
- [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md)
- [Bell number](Bell%20number.md) – ::@:: the number of partitions of a set with _n_ members <!--SR:!2025-12-12,316,330!2025-12-04,308,330-->
- [Stirling polynomials](Stirling%20polynomials.md)
- [twelvefold way](twelvefold%20way.md)
- learning materials related to [partition related number triangles](https://en.wikiversity.org/wiki/partition_related_number_triangles) at Wikiversity

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Ronald L. Graham, Donald E. Knuth, Oren Patashnik (1988) _[Concrete Mathematics](Concrete%20Mathematics.md)_, Addison–Wesley, Reading MA. [ISBN](ISBN.md) [0-201-14236-8](https://en.wikipedia.org/wiki/Special:BookSources/0-201-14236-8), p. 244. <a id="^ref-1"></a>^ref-1
2. ["Stirling Numbers of the Second Kind, Theorem 3.4.1"](https://discrete.openmathbooks.org/more/mdm/sec_adv-stirling.html). <a id="^ref-2"></a>^ref-2
3. Confusingly, the notation that combinatorialists use for _falling_ factorials coincides with the notation used in [special functions](special%20functions.md) for _rising_ factorials; see [Pochhammer symbol](falling%20and%20rising%20factorials.md). <a id="^ref-3"></a>^ref-3
4. Transformation of Series by a Variant of Stirling's Numbers, Imanuel Marx, _The American Mathematical Monthly_ __69__, #6 (June–July 1962), pp. 530–532, [JSTOR](JSTOR.md) [2311194](https://www.jstor.org/stable/2311194). <a id="^ref-4"></a>^ref-4
5. Antonio Salmeri, Introduzione alla teoria dei coefficienti fattoriali, _Giornale di Matematiche di Battaglini __90__ (1962), pp. 44–54._ <a id="^ref-5"></a>^ref-5
6. [Knuth, D.E.](Donald%20Knuth.md) (1992), "Two notes on notation", _Amer. Math. Monthly_, __99__ (5): 403–422, [arXiv](ArXiv.md):[math/9205211](https://arxiv.org/abs/math/9205211), [Bibcode](bibcode.md):[1992math......5211K](https://ui.adsabs.harvard.edu/abs/1992math......5211K), [doi](digital%20object%20identifier.md):[10.2307/2325085](https://doi.org/10.2307%2F2325085), [JSTOR](JSTOR.md) [2325085](https://www.jstor.org/stable/2325085), [S2CID](Semantic%20Scholar.md#S2CID) [119584305](https://api.semanticscholar.org/CorpusID:119584305) <a id="^ref-6"></a>^ref-6
7. Donald E. Knuth, _Fundamental Algorithms_, Reading, Mass.: Addison–Wesley, 1968. <a id="^ref-7"></a>^ref-7
8. p. 66, Donald E. Knuth, _Fundamental Algorithms_, 3rd ed., Reading, Mass.: Addison–Wesley, 1997. <a id="^ref-8"></a>^ref-8
9. Jovan Karamata, Théorèmes sur la sommabilité exponentielle et d'autres sommabilités s'y rattachant, _Mathematica_ (Cluj) __9__ (1935), pp, 164–178. <a id="^ref-9"></a>^ref-9
10. Sprugnoli, Renzo (1994), ["Riordan arrays and combinatorial sums"](http://dml.cz/bitstream/handle/10338.dmlcz/143149/CommentatMathUnivCarolRetro_54-2013-1_2.pdf) (PDF), _Discrete Mathematics_, __132__ (1–3): 267–290, [doi](digital%20object%20identifier.md):[10.1016/0012-365X(92)00570-H](https://doi.org/10.1016%2F0012-365X%2892%2900570-H), [MR](Mathematical%20Reviews.md) [1297386](https://mathscinet.ams.org/mathscinet-getitem?mr=1297386) <a id="^ref-10"></a>^ref-10
11. Chan, O-Yeat; Manna, Dante (2010), ["Congruences for Stirling numbers of the second kind"](http://www.oyeat.com/papers/stirling_final.pdf) (PDF), _Gems in Experimental Mathematics_, Contemporary Mathematics, vol. 517, Providence, Rhode Island: American Mathematical Society, pp. 97–111, [doi](digital%20object%20identifier.md):[10.1090/conm/517/10135](https://doi.org/10.1090%2Fconm%2F517%2F10135), [MR](Mathematical%20Reviews.md) [2731094](https://mathscinet.ams.org/mathscinet-getitem?mr=2731094) <a id="^ref-11"></a>^ref-11
12. Rennie, B.C.; Dobson, A.J. (1969). ["On stirling numbers of the second kind"](https://doi.org/10.1016%2FS0021-9800%2869%2980045-1). _[Journal of Combinatorial Theory](Journal%20of%20Combinatorial%20Theory.md)_. __7__ (2): 116–121. [doi](digital%20object%20identifier.md):[10.1016/S0021-9800(69)80045-1](https://doi.org/10.1016%2FS0021-9800%2869%2980045-1). [ISSN](ISSN.md) [0021-9800](https://search.worldcat.org/issn/0021-9800). <a id="^ref-12"></a>^ref-12
13. [L. C. Hsu](Leetsch%20C.%20Hsu.md), Note on an Asymptotic Expansion of the nth Difference of Zero, AMS Vol.19 NO.2 1948, pp. 273--277 <a id="^ref-13"></a>^ref-13
14. N. M. Temme, Asymptotic Estimates of Stirling Numbers, STUDIES IN APPLIED MATHEMATICS 89:233-243 (1993), Elsevier Science Publishing. <a id="^ref-14"></a>^ref-14
15. Broder, A. (1984). The r-Stirling numbers. Discrete Mathematics 49, 241-259 <a id="^ref-15"></a>^ref-15
16. Triana, J. (2022). r-Stirling numbers of the second kind through context-free grammars. Journal of automata, languages and combinatorics 27(4), 323-333 <a id="^ref-16"></a>^ref-16
17. L. Comtet, _Advanced Combinatorics_, Reidel, 1974, p. 222. <a id="^ref-17"></a>^ref-17
18. A. Mohr and T.D. Porter, _[Applications of Chromatic Polynomials Involving Stirling Numbers](https://web.archive.org/web/20120217060743/http://www.austinmohr.com/work/files/stirling.pdf)_, Journal of Combinatorial Mathematics and Combinatorial Computing __70__ (2009), 57–64. Archived from [the original](http://www.austinmohr.com/work/files/stirling.pdf) on 2012-02-17. <a id="^ref-18"></a>^ref-18

- Boyadzhiev, Khristo (2012). "Close encounters with the Stirling numbers of the second kind". _Mathematics Magazine_. __85__ (4): 252–266. [arXiv](ArXiv.md):[1806.09468](https://arxiv.org/abs/1806.09468). [doi](digital%20object%20identifier.md):[10.4169/math.mag.85.4.252](https://doi.org/10.4169%2Fmath.mag.85.4.252). [S2CID](Semantic%20Scholar.md#S2CID) [115176876](https://api.semanticscholar.org/CorpusID:115176876)..
- ["Stirling numbers of the second kind"](https://planetmath.org/StirlingNumbersOfTheSecondKind). _[PlanetMath](PlanetMath.md)_..
- [Weisstein, Eric W.](Eric%20W.%20Weisstein.md) ["Stirling Number of the Second Kind"](https://mathworld.wolfram.com/StirlingNumberoftheSecondKind.html). _[MathWorld](MathWorld.md)_.
- [Calculator for Stirling Numbers of the Second Kind](http://austinmohr.com/home/?page_id=431)
- [Set Partitions: Stirling Numbers](http://dlmf.nist.gov/26.8#vii)
- Jack van der Elsen (2005). _Black and white transformations_. Maastricht. [ISBN](ISBN.md) [90-423-0263-1](https://en.wikipedia.org/wiki/Special:BookSources/90-423-0263-1).
