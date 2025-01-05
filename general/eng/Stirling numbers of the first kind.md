---
aliases:
  - signed Stirling number of the first kind
  - signed Stirling numbers of the first kind
  - unsigned Stirling number of the first kind
  - unsigned Stirling numbers of the first kind
  - Stirling number of the first kind
  - Stirling numbers of the first kind
tags:
  - flashcard/active/general/eng/Stirling_numbers_of_the_first_kind
  - language/in/English
---

# Stirling numbers of the first kind

In [mathematics](mathematics.md), especially {@{in [combinatorics](combinatorics.md)}@}, __Stirling numbers of the first kind__ {@{arise in the study of permutations}@}. In particular, {@{the unsigned Stirling numbers of the first kind}@} count {@{[permutations](permutation.md) according to their number of [cycles](cycles%20and%20fixed%20points.md) (counting [fixed points](fixed%20point%20(mathematics).md) as cycles of length one)}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-06-30,185,310!2025-01-22,68,310!2025-01-20,67,310!2025-01-20,67,310-->

{@{The Stirling numbers of the first and [second kind](Stirling%20numbers%20of%20the%20second%20kind.md)}@} can be {@{understood as inverses of one another when viewed as [triangular matrices](triangular%20matrix.md)}@}. This article is devoted to {@{specifics of Stirling numbers of the first kind}@}. {@{Identities linking the two kinds}@} appear in the article on [Stirling numbers](Stirling%20number.md). <!--SR:!2025-01-23,69,310!2025-01-20,67,310!2025-01-23,69,310!2025-01-20,67,310-->

## definitions

### definition by algebra

{@{Signed Stirling numbers of the first kind}@} are {@{the coefficients $s(n,k)$ in the expansion of the [falling factorial](falling%20and%20rising%20factorials.md) $$(x)_{n}=x(x-1)(x-2)\cdots (x-n+1)$$}@} into {@{powers of the variable $x$: $$(x)_{n}=\sum _{k=0}^{n}s(n,k)x^{k},$$}@} <!--SR:!2025-01-24,70,310!2025-05-17,136,290!2025-01-25,71,310-->

For example, $(x)_{3}=x(x-1)(x-2)=x^{3}-3x^{2}+2x$, leading to {@{the values $s(3,3)=1$, $s(3,2)=-3$, and $s(3,1)=2$}@}. <!--SR:!2025-01-20,67,310-->

{@{The unsigned Stirling numbers}@} may also be defined {@{algebraically as the coefficients of the [rising factorial](falling%20and%20rising%20factorials.md): $$x^{\overline {n} }=x(x+1)\cdots (x+n-1)=\sum _{k=0}^{n}\left[{n \atop k}\right]x^{k}$$}@}. <!--SR:!2025-01-26,72,310!2025-01-26,72,310-->

{@{The notations used on this page for Stirling numbers}@} are {@{not universal, and may conflict with notations in other sources}@}; {@{the square bracket notation $\left[{n \atop k}\right]$}@} is {@{also common notation for the [Gaussian coefficients](Gaussian%20binomial%20coefficient.md)}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-01-26,72,310!2025-01-20,67,310!2025-01-21,67,310!2025-01-20,67,310-->

### definition by permutation

Subsequently, it was discovered that {@{the absolute values $|s(n,k)|$ of these numbers are equal to the number of [permutations](permutation.md) of certain kinds}@}. These absolute values, which are known as {@{unsigned Stirling numbers of the first kind}@}, are often denoted {@{$c(n,k)$ or $\left[{n \atop k}\right]$}@}. They may be defined directly to be {@{the number of [permutations](permutation.md) of $n$ elements with $k$ disjoint [cycles](cyclic%20permutation.md)}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-01-20,67,310!2025-01-25,71,310!2025-08-03,210,310!2025-01-20,67,310-->

For example, of {@{the $3!=6$ permutations of three elements}@}, there is {@{one permutation with three cycles (the [identity permutation](permutation%20group.md#neutral%20element%20and%20inverses))}@}, given in {@{[one-line notation](permutation.md#cycle%20notation) by $123$ or in [cycle notation](permutation.md#cycle%20notation) by $(1)(2)(3)$}@}, {@{three permutations with two cycles ($132=(1)(23)$, $213=(12)(3)$, and $321=(13)(2)$)}@} and {@{two permutations with one cycle ($312=(132)$ and $231=(123)$)}@}. Thus {@{$\left[{3 \atop 3}\right]=1$, $\left[{3 \atop 2}\right]=3,$ and $\left[{3 \atop 1}\right]=2$}@}. These can be seen to {@{agree with the previous algebraic calculations of $s(n,k)$ for $n=3$}@}. <!--SR:!2025-01-20,67,310!2025-01-23,69,310!2025-07-30,207,310!2025-01-26,72,310!2025-01-23,69,310!2025-01-25,71,310!2025-01-20,67,310-->

For another example, the image at right shows that {@{$\left[{4 \atop 2}\right]=11$: the [symmetric group](symmetric%20group.md) on 4 objects}@} has {@{3 permutations of the form <p> $(\bullet \bullet )(\bullet \bullet )$ (having 2 orbits, each of size 2)}@}, <p> and {@{8 permutations of the form <p> $(\bullet \bullet \bullet )(\bullet )$ (having 1 orbit of size 3 and 1 orbit of size 1)}@}. <!--SR:!2025-01-24,70,310!2025-01-22,68,310!2025-01-19,67,310-->

These numbers can be calculated by {@{considering the orbits as [conjugancy classes](conjugacy%20class.md#properties)}@}. [Alfréd Rényi](Alfréd%20Rényi.md) observed that {@{the unsigned Stirling number of the first kind $\left[{n \atop k}\right]$}@} also counts {@{the number of permutations of size $n$ with $k$ left-to-right maxima}@}.<sup>[\[3\]](#^ref-3)</sup> (annotation: A left-to-right maximum in a permutation is {@{a number in the permutation that is greater all elements to its left}@}.) <!--SR:!2025-03-15,92,270!2025-01-26,72,310!2025-07-16,196,310!2025-05-15,139,290-->

### signs

{@{The signs of the signed Stirling numbers of the first kind}@} depend only on {@{the parity of _n_ − _k_. $$s(n,k)=(-1)^{n-k}\left[{n \atop k}\right].$$}@} <!--SR:!2025-01-19,67,310!2025-01-22,68,310-->

## recurrence relation

{@{The unsigned Stirling numbers of the first kind}@} follow {@{the [recurrence relation](recurrence%20relation.md) $$\left[{n+1 \atop k}\right]=n\left[{n \atop k}\right]+\left[{n \atop k-1}\right]$$ for $k>0$}@}, with {@{the boundary conditions $$\left[{0 \atop 0}\right]=1\quad {\text{and} }\quad \left[{n \atop 0}\right]=\left[{0 \atop n}\right]=0$$ for $n>0$}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-01-21,67,310!2025-01-24,70,310!2025-01-20,67,310-->

It follows immediately that {@{the signed Stirling numbers of the first kind}@} satisfy {@{the recurrence $$s(n+1,k)= -n\cdot s(n,k)+s(n,k-1) \,.$$}@} <!--SR:!2025-01-20,67,310!2025-04-19,119,290-->

> __Algebraic proof__
>
> We prove the recurrence relation using {@{the definition of Stirling numbers in terms of rising factorials}@}. {@{Distributing the last term of the product}@}, we have {@{$$x^{\overline {n+1} }=x(x+1)\cdots (x+n-1)(x+n)=n\cdot x^{\overline {n} }+x\cdot x^{\overline {n} }.$$}@} {@{The coefficient of $x^{k}$ on the left-hand side of this equation}@} is {@{$\left[{n+1 \atop k}\right]$}@}. {@{The coefficient of $x^{k}$ in $n\cdot x^{\overline {n} }$}@} is {@{$n\cdot \left[{n \atop k}\right]$}@}, while {@{the coefficient of $x^{k}$ in $x\cdot x^{\overline {n} }$}@} is {@{$\left[{n \atop k-1}\right]$}@}. Since {@{the two sides are equal as polynomials}@}, {@{the coefficients of $x^{k}$ on both sides must be equal, and the result follows}@}. <!--SR:!2025-01-26,72,310!2025-01-25,71,310!2025-07-20,198,310!2025-01-20,67,310!2025-01-25,71,310!2025-01-20,67,310!2025-01-19,67,310!2025-05-18,140,290!2025-01-20,67,310!2025-01-20,67,310!2025-01-21,67,310-->

<!-- markdownlint MD028 -->

> __Combinatorial proof__
>
> We prove the recurrence relation using {@{the definition of Stirling numbers in terms of permutations with a given number of cycles (or equivalently, [orbits](group%20action.md#orbits%20and%20stabilizers))}@}.
>
> Consider {@{forming a permutation of $n+1$ objects from a permutation of $n$ objects by adding a distinguished object}@}. There are {@{exactly two ways in which this can be accomplished}@}. We could do this by {@{forming a [singleton](singleton%20(mathematics).md) cycle, i.e., leaving the extra object alone}@}. This {@{increases the number of cycles by 1 and so accounts for the $\left[{n \atop k-1}\right]$ term in the recurrence formula}@}. We could also {@{insert the new object into one of the existing cycles}@}. Consider {@{an arbitrary permutation of $n$ objects with $k$ cycles, and label the objects $a_{1},\dots ,a_{n}$, so that the permutation is represented by $$\displaystyle \underbrace {(a_{1}\ldots a_{j_{1} })(a_{j_{1}+1}\ldots a_{j_{2} })\ldots (a_{j_{k-1}+1}\ldots a_{n})} _{k\ \mathrm {cycles} }.$$}@} To {@{form a new permutation of $n+1$ objects and $k$ cycles}@} one must {@{insert the new object into this array}@}. There are {@{$n$ ways to perform this insertion, inserting the new object immediately following any of the $a_{i}$ already present}@}. This {@{explains the $n\left[{n \atop k}\right]$ term of the recurrence relation}@}. These two cases {@{include all possibilities, so the recurrence relation follows}@}. <!--SR:!2025-05-14,138,290!2025-01-22,68,310!2025-01-25,71,310!2025-01-21,67,310!2025-01-22,68,310!2025-01-24,70,310!2025-01-19,67,310!2025-01-19,67,310!2025-01-23,69,310!2025-01-19,67,310!2025-07-03,186,310!2025-01-19,67,310-->

## table of values

Below is {@{a [triangular array](triangular%20array.md) of unsigned values for the Stirling numbers of the first kind}@}, similar in form to {@{[Pascal's triangle](Pascal's%20triangle.md)}@}. These values are {@{easy to generate using the recurrence relation in the previous section}@}. <!--SR:!2025-01-25,71,310!2025-01-20,67,310!2025-01-23,69,310-->

| __n__\\_k_ | __0__ | __1__  | __2__   | __3__   | __4__  | __5__  | __6__ | __7__ | __8__ | __9__ | __10__ |
| ----------:| -----:| ------:| -------:| -------:| ------:| -----: | ----: | ----: | ----: | ----: | -----: |
| __0__      | 1     |        |         |         |        |        |       |       |       |       |        |
| __1__      | 0     | 1      |         |         |        |        |       |       |       |       |        |
| __2__      | 0     | 1      | 1       |         |        |        |       |       |       |       |        |
| __3__      | 0     | 2      | 3       | 1       |        |        |       |       |       |       |        |
| __4__      | 0     | 6      | 11      | 6       | 1      |        |       |       |       |       |        |
| __5__      | 0     | 24     | 50      | 35      | 10     | 1      |       |       |       |       |        |
| __6__      | 0     | 120    | 274     | 225     | 85     | 15     | 1     |       |       |       |        |
| __7__      | 0     | 720    | 1764    | 1624    | 735    | 175    | 21    | 1     |       |       |        |
| __8__      | 0     | 5040   | 13068   | 13132   | 6769   | 1960   | 322   | 28    | 1     |       |        |
| __9__      | 0     | 40320  | 109584  | 118124  | 67284  | 22449  | 4536  | 546   | 36    | 1     |        |
| __10__     | 0     | 362880 | 1026576 | 1172700 | 723680 | 269325 | 63273 | 9450  | 870   | 45    | 1      |

## properties

### simple identities

Using {@{the [Kronecker delta](Kronecker%20delta.md)}@} one has, {@{$$\left[{n \atop 0}\right]=\delta _{n}$$}@} and {@{$\left[{0 \atop k}\right]=0$ if $k>0$, or more generally $\left[{n \atop k}\right]=0$ if _k_ > _n_}@}. Also {@{$$\left[{n \atop 1}\right]=(n-1)!,\quad \left[{n \atop n}\right]=1,\quad \left[{n \atop n-1}\right]={n \choose 2},$$}@} and {@{$$\left[{n \atop n-2}\right]={\frac {3n-1}{4} }{n \choose 3}\quad {\text{ and } }\quad \left[{n \atop n-3}\right]={n \choose 2}{n \choose 4}.$$}@} <!--SR:!2025-01-20,67,310!2025-01-26,72,310!2025-07-10,193,310!2025-01-20,67,310!2025-01-08,9,230-->

{@{Similar relationships involving the Stirling numbers}@} hold for {@{the [Bernoulli polynomials](Bernoulli%20polynomials.md)}@}. {@{Many relations for the Stirling numbers}@} shadow {@{similar relations on the [binomial coefficients](binomial%20coefficient.md)}@}. {@{The study of these 'shadow relationships'}@} is termed {@{[umbral calculus](umbral%20calculus.md) and culminates in the theory of [Sheffer sequences](Sheffer%20sequence.md)}@}. {@{Generalizations of the [Stirling numbers](Stirling%20number.md) of both kinds to arbitrary complex-valued inputs}@} may be {@{extended through the relations of these triangles to the [Stirling convolution polynomials](Stirling%20polynomials.md#Stirling%20convolution%20polynomials)}@}.<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2025-01-22,68,310!2025-07-17,197,310!2025-01-25,71,310!2025-01-24,70,310!2025-07-11,194,310!2025-01-23,69,310!2025-01-20,67,310!2025-05-19,138,290-->

> __Combinatorial proofs__
>
> These identities may be derived by {@{enumerating permutations directly}@}. For example, a permutation of _n_ elements with _n_ − 3 cycles must have one of the following forms:
>
> - _n_ − 6 fixed points and three two-cycles
> - _n_ − 5 fixed points, a three-cycle and a two-cycle, or
> - _n_ − 4 fixed points and a four-cycle.
>
> The three types may be enumerated as follows:
>
> - choose the six elements that go into the two-cycles, decompose them into two-cycles and take into account that the order of the three two-cycles is not important ::@:: $${n \choose 6}{6 \choose 2,2,2}{\frac 1 6}$$ <!--SR:!2025-01-19,67,310!2025-01-18,66,310-->
> - choose the five elements that go into the three-cycle and the two-cycle, choose the elements of the three-cycle and take into account that three elements generate two three-cycles ::@:: $${n \choose 5}{5 \choose 3}\times 2$$ <!--SR:!2025-07-16,196,310!2025-01-20,67,310-->
> - choose the four elements of the four-cycle and take into account that four elements generate six four-cycles ::@:: $${n \choose 4}\times 6.$$ <!--SR:!2025-01-19,67,310!2025-01-24,70,310-->
>
> Sum the three contributions to obtain ::@:: $${n \choose 6}{6 \choose 2,2,2}{\frac {1}{6} }+{n \choose 5}{5 \choose 3}\times 2+{n \choose 4}\times 6={n \choose 2}{n \choose 4}.$$ <!--SR:!2025-01-20,67,310!2025-03-06,93,270-->

Note that all the combinatorial proofs above {@{use either binomials or multinomials of $n$}@}. <!--SR:!2025-05-23,141,290-->

Therefore if {@{$p$ is prime}@}, then: {@{$$p\ |\left[{p \atop k}\right] \text{ for } 1<k<p \,.$$}@} <!--SR:!2025-07-18,196,310!2025-01-08,8,230-->

### expansions for fixed _k_

Since {@{the Stirling numbers are the coefficients of a polynomial with roots 0, 1, ..., _n_ − 1}@}, one has by {@{[Vieta's formulas](Vieta's%20formulas.md)}@} that {@{$$\left[{\begin{matrix}n\\n-k\end{matrix} }\right]=\sum _{0\leq i_{1}<\ldots <i_{k}<n}i_{1}i_{2}\cdots i_{k}.$$}@} <!--SR:!2025-01-26,72,310!2025-03-15,92,270!2025-01-19,53,250-->

In other words, {@{the Stirling numbers of the first kind}@} are {@{given by [elementary symmetric polynomials](elementary%20symmetric%20polynomial.md) evaluated at 0, 1, ..., _n_ − 1}@}.<sup>[\[5\]](#^ref-5)</sup> In this form, the simple identities given above take the form {@{$$\begin{aligned} \left[{\begin{matrix}n\\n-1\end{matrix} }\right]& =\sum _{i=0}^{n-1}i={\binom {n}{2} }, \\ \left[{\begin{matrix}n\\n-2\end{matrix} }\right]& =\sum _{i=0}^{n-1}\sum _{j=0}^{i-1}ij={\frac {3n-1}{4} }{\binom {n}{3} }, \\ \left[{\begin{matrix}n\\n-3\end{matrix} }\right] & =\sum _{i=0}^{n-1}\sum _{j=0}^{i-1}\sum _{k=0}^{j-1}ijk={\binom {n}{2} }{\binom {n}{4} }, \end{aligned}$$ and so on}@}. <!--SR:!2025-01-23,69,310!2025-01-22,68,310!2025-02-16,47,250-->

One may produce {@{alternative forms for the Stirling numbers of the first kind}@} with {@{a similar approach preceded by some algebraic manipulation}@}: since {@{$$(x+1)(x+2)\cdots (x+n-1)=(n-1)!\cdot (x+1)\left({\frac {x}{2} }+1\right)\cdots \left({\frac {x}{n-1} }+1\right),$$}@} it {@{follows from [Newton's formulas](newton's%20identities.md) that one can expand the Stirling numbers of the first kind in terms of [generalized harmonic numbers](harmonic%20number.md#generalized%20harmonic%20numbers)}@}. This yields {@{identities like $$\begin{aligned} \left[{n \atop 2}\right]& =(n-1)!\;H_{n-1}, \\ \left[{n \atop 3}\right]& ={\frac {1}{2} }(n-1)!\left[(H_{n-1})^{2}-H_{n-1}^{(2)}\right] \\ \left[{n \atop 4}\right]& ={\frac {1}{3!} }(n-1)!\left[(H_{n-1})^{3}-3H_{n-1}H_{n-1}^{(2)}+2H_{n-1}^{(3)}\right], \end{aligned}$$}@} where {@{_H_<sub>_n_</sub> is the [harmonic number](harmonic%20number.md) $H_{n}={\frac {1}{1} }+{\frac {1}{2} }+\ldots +{\frac {1}{n} }$}@} and {@{_H_<sub>_n_</sub><sup>(_m_)</sup> is the generalized harmonic number$$H_{n}^{(m)}={\frac {1}{1^{m} } }+{\frac {1}{2^{m} } }+\ldots +{\frac {1}{n^{m} } }.$$}@} These relations can be generalized to {@{give $${\frac {1}{(n-1)!} }\left[{\begin{matrix}n\\k+1\end{matrix} }\right]=\sum _{i_{1}=1}^{n-1}\sum _{i_{2}=i_{1}+1}^{n-1}\cdots \sum _{i_{k}=i_{k-1}+1}^{n-1}{\frac {1}{i_{1}i_{2}\cdots i_{k} } }={\frac {w(n,k)}{k!} }$$}@} where {@{_w_(_n_, _m_) is defined recursively in terms of the generalized harmonic numbers by $$w(n,m)=\delta _{m,0}+\sum _{k=0}^{m-1}(1-m)_{k}H_{n-1}^{(k+1)}w(n,m-1-k).$$}@} (Here {@{_δ_ is the [Kronecker delta function](Kronecker%20delta.md) and $(m)_{k}$ is the [Pochhammer symbol](falling%20and%20rising%20factorials.md)}@}.)<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2025-01-22,68,310!2025-01-23,69,310!2025-05-18,137,290!2025-01-24,70,310!2025-01-06,4,130!2025-01-17,65,310!2025-07-09,193,310!2025-01-12,34,210!2025-01-08,7,130!2025-01-29,74,329-->

For {@{fixed $n\geq 0$}@} {@{these weighted harmonic number expansions}@} are generated by {@{the generating function (annotation: the _condition_ is $n \ge 0$) $${\frac {1}{n!} }\left[{\begin{matrix}n+1\\k\end{matrix} }\right]=[x^{k}]\exp \left(-\sum _{m\geq 1}{\frac {H_{n}^{(m)} }{m} }(-x)^{m}\right),$$}@} where the notation $[x^{k}]$ means {@{extraction of the coefficient of $x^{k}$ from the following [formal power series](formal%20power%20series.md)}@} (see the non-exponential [Bell polynomials](bell%20polynomials.md) and section 3 of <sup>[\[7\]](#^ref-7)</sup>). <!--SR:!2025-01-20,67,310!2025-03-03,84,270!2025-01-19,16,150!2025-01-19,67,310-->

More generally, {@{sums related to these weighted harmonic number expansions of the Stirling numbers of the first kind}@} can be defined {@{through generalized zeta series [transforms of generating functions](generating%20function%20transformation.md#derivative%20transformations)}@}.<sup>[\[8\]](#^ref-8)</sup><sup>[\[9\]](#^ref-9)</sup> <!--SR:!2025-06-16,163,311!2025-01-30,75,329-->

One can also {@{"invert" the relations for these Stirling numbers given in terms of the $k$-order harmonic numbers}@} to {@{write the integer-order generalized harmonic numbers in terms of weighted sums of terms involving the Stirling numbers of the first kind}@}. For example, when $k=2,3$ the second-order and third-order harmonic numbers are given by $$\begin{aligned} (n!)^{2}\cdot H_{n}^{(2)} & =\left[{\begin{matrix}n+1\\2\end{matrix} }\right]^{2}-2\left[{\begin{matrix}n+1\\1\end{matrix} }\right]\left[{\begin{matrix}n+1\\3\end{matrix} }\right] \\ (n!)^{3}\cdot H_{n}^{(3)} & =\left[{\begin{matrix}n+1\\2\end{matrix} }\right]^{3}-3\left[{\begin{matrix}n+1\\1\end{matrix} }\right]\left[{\begin{matrix}n+1\\2\end{matrix} }\right]\left[{\begin{matrix}n+1\\3\end{matrix} }\right]+3\left[{\begin{matrix}n+1\\1\end{matrix} }\right]^{2}\left[{\begin{matrix}n+1\\4\end{matrix} }\right]. \end{aligned}$$ <!--SR:!2025-01-23,71,331!2025-04-11,113,289-->

More generally, one can {@{invert the [Bell polynomial](bell%20polynomials.md) generating function for the Stirling numbers expanded in terms of the $m$-order [harmonic numbers](harmonic%20number.md)}@} to obtain that {@{for integers $m\geq 2$ $$H_{n}^{(m)}=-m\times [x^{m}]\log \left(1+\sum _{k\geq 1}\left[{\begin{matrix}n+1\\k+1\end{matrix} }\right]{\frac {(-x)^{k} }{n!} }\right).$$}@} <!--SR:!2025-03-15,94,289!2025-01-28,26,291-->

### finite sums

Since permutations are partitioned by number of cycles, one has {@{$$\sum _{k=0}^{n}\left[{n \atop k}\right]=n!$$}@} The identity {@{$$\sum _{p=k}^{n}{\left[{n \atop p}\right]{\binom {p}{k} } }=\left[{n+1 \atop k+1}\right]$$}@} can be proved by {@{the techniques on the page [Stirling numbers and exponential generating functions](Stirling%20numbers%20and%20exponential%20generating%20functions%20in%20symbolic%20combinatorics.md)}@}. <!--SR:!2025-06-18,165,311!2025-01-15,33,251!2025-08-13,222,331-->

{@{The table in section 6.1 of _Concrete Mathematics_}@} provides {@{a plethora of generalized forms of finite sums involving the Stirling numbers}@}. Several particular finite sums relevant to this article include <!--SR:!2025-01-14,59,319!2025-02-13,84,339-->

- reversed increment by binomial coefficient ::@:: $$\left[{n \atop m}\right]=\sum _{k=m}^{n}\left[{n+1 \atop k+1}\right](-1)^{k-m}{\binom {k}{m} }$$ <!--SR:!2025-03-08,76,259!2025-02-13,61,279-->
- increment by combinatorial argument ::@:: $$\left[{n+1 \atop m+1}\right]=\sum _{k=m}^{n} \frac {n!} {k!} \left[{k \atop m}\right]$$  (annotation: Permutate _n_ − _k_ elements from _n_ elements to a partition with linear order. Add the 1 element to make the partition a cycle. Partition the remaining _k_ elements into _m_ cycles.) <!--SR:!2025-01-19,59,319!2025-05-07,129,299-->
- increment by summing up to _k_ ::@:: $$\left[{n + k +1 \atop n}\right]=\sum _{j=0}^{k}(n+j)\left[{n+j \atop j}\right]$$ <!--SR:!2025-01-27,58,279!2025-05-02,125,299-->
- partition then choose partitions ::@:: $$\left[{n \atop l+m}\right]{\binom {l+m}{l} }=\sum _{k}{\binom {n}{k} }\left[{k \atop l}\right]\left[{n-k \atop m}\right]$$  (annotation: Choose _k_ elements from _n_ elements. Partition _k_ elements into the chosen _l_ cycles. Partition the remaining _n_ − _k_ elements into the unchosen _m_ cycles.) <!--SR:!2025-01-24,72,331!2025-01-24,72,335-->

Additionally, if {@{we define the [_second-order_ Eulerian numbers](eulerian%20number.md#eulerian%20numbers%20of%20the%20second%20kind) by the triangular recurrence relation <sup>[\[10\]](#^ref-10)</sup> $$\left\langle \!\!\left\langle {n \atop k}\right\rangle \!\!\right\rangle =(k+1)\left\langle \!\!\left\langle {n-1 \atop k}\right\rangle \!\!\right\rangle +(2n-1-k)\left\langle \!\!\left\langle {n-1 \atop k-1}\right\rangle \!\!\right\rangle ,$$}@} we {@{arrive at the following identity related to the form of the [Stirling convolution polynomials](Stirling%20polynomials.md#Stirling%20convolution%20polynomials) which can be employed to generalize both Stirling number triangles to arbitrary real, or complex-valued, values of the input $x$}@}: {@{$$\left[{x \atop x-n}\right]=\sum _{k=0}^{n}\left\langle \!\!\left\langle {n \atop k}\right\rangle \!\!\right\rangle {\binom {x+k}{2n} }.$$}@} <!--SR:!2025-01-13,8,151!2025-02-17,75,269!2025-01-23,22,231-->

Particular expansions of the previous identity lead to the following identities expanding the Stirling numbers of the first kind for the first few small values of $n:=1,2,3$: $${\begin{aligned}\left[{\begin{matrix}x\\x-1\end{matrix} }\right]&={\binom {x}{2} }\\\left[{\begin{matrix}x\\x-2\end{matrix} }\right]&={\binom {x}{4} }+2{\binom {x+1}{4} }\\\left[{\begin{matrix}x\\x-3\end{matrix} }\right]&={\binom {x}{6} }+8{\binom {x+1}{6} }+6{\binom {x+2}{6} }.\end{aligned} }$$

Software tools for {@{working with finite sums involving [Stirling numbers](Stirling%20number.md) and [Eulerian numbers](eulerian%20number.md)}@} are {@{provided by the [RISC Stirling.m package](http://www.risc.jku.at/research/combinat/software/ergosum/RISC/Stirling.html) utilities in _Mathematica_}@}. Other software packages for {@{_guessing_ formulas for sequences (and polynomial sequence sums) involving Stirling numbers and other special triangles}@} is {@{available for both [Mathematica](Wolfram%20Mathematica.md) and [Sage](SageMath.md) [here](https://github.com/maxieds/GuessPolynomialSequences) and [here](https://github.com/maxieds/sage-guess), respectively}@}.<sup>[\[11\]](#^ref-11)</sup> <!--SR:!2025-02-01,77,329!2025-01-12,57,309!2025-06-01,151,311!2025-01-24,72,331-->

### congruences

The following congruence identity may be proved via {@{a [generating function](generating%20function.md)-based approach}@}:<sup>[\[12\]](#^ref-12)</sup> $${\begin{aligned}\left[{\begin{matrix}n\\m\end{matrix} }\right]&\equiv {\binom {\lfloor n/2\rfloor }{m-\lceil n/2\rceil } }=[x^{m}]\left(x^{\lceil n/2\rceil }(x+1)^{\lfloor n/2\rfloor }\right)&&{\pmod {2} },\end{aligned} }$$ <!--SR:!2025-03-27,100,289-->

More recent results {@{providing [Jacobi-type J-fractions](generating%20function.md#Representation%20by%20continued%20fractions%20.28Jacobi-type%20J-fractions.29) that generate the [single factorial function](factorial.md) and [generalized factorial-related products](Pochhammer%20k-symbol.md)}@} lead to {@{other new congruence results for the Stirling numbers of the first kind}@}.<sup>[\[13\]](#^ref-13)</sup> For example, working modulo $2$ we can prove that $${\begin{aligned}\left[{\begin{matrix}n\\1\end{matrix} }\right]&\equiv {\frac {2^{n} }{4} }[n\geq 2]+[n=1]&&{\pmod {2} }\\\left[{\begin{matrix}n\\2\end{matrix} }\right]&\equiv {\frac {3\cdot 2^{n} }{16} }[n-1](n\geq 3)+[n=2]&&{\pmod {2} }\\\left[{\begin{matrix}n\\3\end{matrix} }\right]&\equiv 2^{n-7}(9n-20)[n-1](n\geq 4)+[n=3]&&{\pmod {2} }\\\left[{\begin{matrix}n\\4\end{matrix} }\right]&\equiv 2^{n-9}(3n-10)(3n-7)[n-1](n\geq 5)+[n=4]&&{\pmod {2} }\end{aligned} }$$ Where $[b]$ is the [Iverson bracket](iverson%20bracket.md). <!--SR:!2025-01-22,70,331!2025-01-23,71,331-->

and working modulo $3$ we can similarly prove that $${\begin{aligned}\left[{\begin{matrix}n\\m\end{matrix} }\right]&\equiv [x^{m}](x^{\lceil n/3\rceil }(x+1)^{\lceil (n-1)/3\rceil }(x+2)^{\lfloor n/3\rfloor }&&{\pmod {3} }\\&\equiv \sum _{k=0}^{m}{\binom {\lceil (n-1)/3\rceil }{k} }{\binom {\lfloor n/3\rfloor }{m-k-\lfloor n/3\rfloor } }2^{\lceil n/3\rceil +\lfloor n/3\rfloor -m+k}&&{\pmod {3} }\end{aligned} }$$

More generally, for fixed integers $h\geq 3$ if we define the ordered roots $$\left(\omega _{h,i}\right)_{i=1}^{h-1}:=\left\{\omega _{j}:\sum _{i=0}^{h-1}{\binom {h-1}{i} }{\frac {h!}{(i+1)!} }(-\omega _{j})^{i}=0,\ 1\leq j<h\right\},$$ then we may expand congruences for these Stirling numbers defined as the coefficients $$\left[{\begin{matrix}n\\m\end{matrix} }\right]=[R^{m}]R(R+1)\cdots (R+n-1),$$ in the following form where the functions, $p_{h,i}^{[m]}(n)$, denote fixed polynomials of degree $m$ in $n$ for each $h$, $m$, and $i$: $$\left[{\begin{matrix}n\\m\end{matrix} }\right]=\left(\sum _{i=0}^{h-1}p_{h,i}^{[m]}(n)\times \omega _{h,i}^{n}\right)[n>m]+[n=m]\qquad {\pmod {h} },$$ Section 6.2 of the reference cited above provides more explicit expansions related to these congruences for the $r$-order [harmonic numbers](harmonic%20number.md) and for the [generalized factorial products](pochhammer%20k-symbol.md), $p_{n}(\alpha ,R):=R(R+\alpha )\cdots (R+(n-1)\alpha )$.

### generating functions

A variety of identities may be derived by {@{manipulating the [generating function](generating%20function.md) (see [change of basis](Stirling%20number.md#as%20change%20of%20basis%20coefficients))}@}: {@{$$H(z,u)=(1+z)^{u}=\sum _{n=0}^{\infty }{u \choose n}z^{n} = \sum_{n = 0}^\infty \frac {z^n} {n!} u^{\underline n} =\sum _{n=0}^{\infty }{\frac {z^{n} }{n!} }\sum _{k=0}^{n}s(n,k)u^{k}=\sum _{k=0}^{\infty }u^{k}\sum _{n=k}^{\infty }{\frac {z^{n} }{n!} }s(n,k).$$}@} Using {@{the equality $$(1+z)^{u}=e^{u\log(1+z)}=\sum _{k=0}^{\infty }(\log(1+z))^{k}{\frac {u^{k} }{k!} },$$}@} it follows that {@{$$\sum _{n=k}^{\infty }s(n,k){\frac {z^{n} }{n!} }={\frac {(\log(1+z))^{k} }{k!} }$$}@} and {@{$$\sum _{n=k}^{\infty }\left[{n \atop k}\right]{\frac {z^{n} }{n!} }={\frac {(-\log(1-z))^{k} }{k!} }.$$}@}<sup>[\[1\]](#^ref-1)</sup> This identity is {@{valid for [formal power series](formal%20power%20series.md)}@}, and the sum {@{[converges](convergent%20series.md) in the [complex plane](complex%20plane.md) for |_z_| < 1}@}. <!--SR:!2025-01-31,76,329!2025-02-05,68,271!2025-06-13,163,311!2025-03-14,96,291!2025-02-04,67,271!2025-01-23,71,331!2025-01-23,71,331-->

Other identities arise by {@{exchanging the order of summation, taking derivatives, making substitutions for _z_ or _u_, etc.}@} For example, we may derive:<sup>[\[14\]](#^ref-14)</sup> $${\frac {\log ^{m}(1+z)}{1+z} }=m!\sum _{k=0}^{\infty }{\frac {s(k+1,m+1)\,z^{k} }{k!} },\qquad m=1,2,3,\ldots \quad |z|<1$$ or $$\sum _{n=i}^{\infty }{\frac {\left[{n \atop i}\right]}{n\,(n!)} }=\zeta (i+1),\qquad i=1,2,3,\ldots$$ and $$\sum _{n=i}^{\infty }{\frac {\left[{n \atop i}\right]}{n\,(v)_{n} } }=\zeta (i+1,v),\qquad i=1,2,3,\ldots \quad \Re (v)>0$$ where {@{$\zeta (k)$ and $\zeta (k,v)$ are the [Riemann zeta function](riemann%20zeta%20function.md) and the [Hurwitz zeta function](hurwitz%20zeta%20function.md) respectively}@}, and even evaluate this integral $$\int _{0}^{1}{\frac {\log ^{z}(1-x)}{x^{k} } }\,dx={\frac {(-1)^{z}\Gamma (z+1)}{(k-1)!} }\sum _{r=1}^{k-1}s(k-1,r)\sum _{m=0}^{r}{\binom {r}{m} }(k-2)^{r-m}\zeta (z+1-m),\qquad \Re (z)>k-1,\quad k=3,4,5,\ldots$$ where {@{$\Gamma (z)$ is the [gamma function](gamma%20function.md)}@}. There also exist {@{more complicated expressions for the zeta-functions involving the Stirling numbers}@}. One, for example, has $$\zeta (s,v)={\frac {k!}{(s-k)_{k} } }\sum _{n=0}^{\infty }{\frac {1}{(n+k)!} }\left[{n+k \atop n}\right]\sum _{l=0}^{n+k-1}\!(-1)^{l}{\binom {n+k-1}{l} }(l+v)^{k-s},\quad k=1,2,3,\ldots$$ This series {@{generalizes [Hasse](Helmut%20Hasse.md)'s series for the [Hurwitz zeta-function](hurwitz%20zeta%20function.md) (we obtain Hasse's series by setting _k_=1)}@}.<sup>[\[15\]](#^ref-15)</sup><sup>[\[16\]](#^ref-16)</sup> <!--SR:!2025-08-03,213,331!2025-08-02,212,331!2025-01-21,69,331!2025-01-20,68,331!2025-04-10,112,291-->

### asymptotics

The next estimate given in terms of the [Euler gamma constant](euler's%20constant.md) applies:<sup>[\[17\]](#^ref-17)</sup> ::@:: $$\left[{\begin{matrix}n+1\\k+1\end{matrix} }\right]{\underset {n\to \infty }{\sim } }{\frac {n!}{k!} }\left(\gamma +\ln n\right)^{k},\ {\text{ uniformly for } }k=o(\ln n).$$ <!--SR:!2025-01-19,28,211!2025-01-23,49,271-->

For fixed $n$ (growing $k$) we have the following estimate: ::@:: $$\left[{\begin{matrix}n+k\\k\end{matrix} }\right]{\underset {k\to \infty }{\sim } }{\frac {k^{2n} }{2^{n}n!} }.$$ <!--SR:!2025-04-17,106,251!2025-03-20,97,271-->

### explicit formula

It is well-known that {@{we don't know any one-sum formula for Stirling numbers of the first kind}@}. {@{A two-sum formula}@} can be obtained {@{using one of the [symmetric formulae for Stirling numbers](Stirling%20number.md#symmetric%20formulae) in conjunction with the explicit formula for [Stirling numbers of the second kind](Stirling%20numbers%20of%20the%20second%20kind.md)}@}. $$\left[{n \atop k}\right]=\sum _{j=n}^{2n-k}{\binom {2n-k}{j} }{\binom {j-1}{k-1} }\sum _{m=0}^{j-n}{\frac {(-1)^{m+n-k}m^{j-k} }{m!(j-n-m)!} }$$ <!--SR:!2025-01-22,70,331!2025-01-23,71,331!2025-04-24,136,311-->

As discussed earlier, by {@{[Vieta's formulas](Vieta's%20formulas.md)}@}, one get {@{$$\left[{\begin{matrix}n\\k\end{matrix} }\right]=\sum _{0\leq i_{1}<\ldots <i_{n-k}<n}i_{1}i_{2}\cdots i_{n-k}.$$}@} <!--SR:!2025-01-11,56,309!2025-01-08,20,269-->

The Stirling number _s(n,n-p)_ can be found from the formula<sup>[\[18\]](#^ref-18)</sup> $${\begin{aligned}s(n,n-p)&={\frac {1}{(n-p-1)!} }\sum _{0\leq k_{1},\ldots ,k_{p}:\sum _{1}^{p}mk_{m}=p}(-1)^{K}{\frac {(n+K-1)!}{k_{1}!k_{2}!\cdots k_{p}!~2!^{k_{1} }3!^{k_{2} }\cdots (p+1)!^{k_{p} } } },\end{aligned} }$$ where $K=k_{1}+\cdots +k_{p}.$ The sum is a sum over all [partitions](integer%20partition.md) of _p_.

Another exact nested sum expansion for these Stirling numbers is computed by {@{[elementary symmetric polynomials](elementary%20symmetric%20polynomial.md) corresponding to the coefficients in $x$ of a product of the form $(1+c_{1}x)\cdots (1+c_{n-1}x)$}@}. In particular, we see that {@{$${\begin{aligned}\left[{n \atop k+1}\right]&=[x^{k}](x+1)(x+2)\cdots (x+n-1)=(n-1)!\cdot [x^{k}](x+1)\left({\frac {x}{2} }+1\right)\cdots \left({\frac {x}{n-1} }+1\right)\\&=\sum _{1\leq i_{1}<\cdots <i_{k}<n}{\frac {(n-1)!}{i_{1}\cdots i_{k} } }.\end{aligned} }$$}@} {@{[Newton's identities](newton's%20identities.md) combined with the above expansions}@} may be used to {@{give an alternate proof of the weighted expansions involving the generalized [harmonic numbers](harmonic%20number.md) already [noted above](#expansions%20for%20fixed%20k)}@}. <!--SR:!2025-06-17,164,311!2025-01-17,19,231!2025-08-21,231,331!2025-01-08,20,271-->

### relations to natural logarithm function

{@{The _n_-th [derivative](derivative.md) of the _μ_-th power of the [natural logarithm](natural%20logarithm.md)}@} involves {@{the signed Stirling numbers of the first kind}@}: {@{$${\operatorname {d} ^{n}\!(\ln x)^{\mu } \over \operatorname {d} \!x^{n} }=x^{-n}\sum _{k=1}^{n}s(n,n+1-k)\mu ^{\underline {k} }(\ln x)^{\mu -k},$$}@} where {@{$\mu ^{\underline {i} }$ is the [falling factorial](falling%20and%20rising%20factorials.md), and $s(n,n+1-k)$ is the signed Stirling number}@}. <!--SR:!2025-03-30,103,289!2025-04-14,116,291!2025-01-18,13,171!2025-01-12,57,309-->

It can be proved by {@{using [mathematical induction](mathematical%20induction.md)}@}. <!--SR:!2025-01-22,70,331-->

### other formulas

Stirling numbers of the first kind appear in {@{the formula for [Gregory coefficients](Gregory%20coefficients.md)}@} and in {@{a finite sum identity involving [Bell numbers](Bell%20number.md)}@}<sup>[\[19\]](#^ref-19)</sup> <!--SR:!2025-08-04,214,331!2025-01-24,72,331-->

- the formula for [Gregory coefficients](Gregory%20coefficients.md) ::@:: $$n!G_{n}=\sum _{l=0}^{n}{\frac {s(n,l)}{l+1} }$$ <!--SR:!2025-02-05,68,271!2025-04-09,111,291-->
- a finite sum identity involving [Bell numbers](Bell%20number.md) ::@:: $$\sum_{j = 0}^n \binom n j k^{n - j} B_{j} = \sum_{i = 0}^k \left[k \atop i\right] (-1)^{k - i} B_{n+i} = \sum_{i = 0}^k s(k, i) B_{n + i}$$ <!--SR:!2025-01-14,24,191!2025-01-16,34,251-->

{@{Infinite series involving the finite sums with the Stirling numbers}@} often {@{lead to the special functions}@}. For example<sup>[\[14\]](#^ref-14)</sup><sup>[\[20\]](#^ref-20)</sup> $$\ln \Gamma (z)=\left(z-{\frac {1}{2} }\right)\!\ln z-z+{\frac {1}{2} }\ln 2\pi +{\frac {1}{\pi } }\sum _{n=1}^{\infty }{\frac {1}{n\cdot n!} }\!\sum _{l=0}^{\lfloor n/2\rfloor }\!{\frac {(-1)^{l}(2l)!}{(2\pi z)^{2l+1} } }\left[{n \atop 2l+1}\right]$$ and $$\Psi (z)=\ln z-{\frac {1}{2z} }-{\frac {1}{\pi z} }\sum _{n=1}^{\infty }{\frac {1}{n\cdot n!} }\!\sum _{l=0}^{\lfloor n/2\rfloor }\!{\frac {(-1)^{l}(2l+1)!}{(2\pi z)^{2l+1} } }\left[{n \atop 2l+1}\right]$$ or even $$\gamma _{m}={\frac {1}{2} }\delta _{m,0}+{\frac {(-1)^{m}m!}{\pi } }\!\sum _{n=1}^{\infty }{\frac {1}{n\cdot n!} }\!\sum _{k=0}^{\lfloor n/2\rfloor }{\frac {(-1)^{k} }{(2\pi )^{2k+1} } }\left[{2k+2 \atop m+1}\right]\left[{n \atop 2k+1}\right]\,$$ where {@{_γ_<sub>_m_</sub> are the [Stieltjes constants](Stieltjes%20constants.md) and _δ_<sub>_m_,0</sub> represents the [Kronecker delta function](Kronecker%20delta.md)}@}. Notice that this last identity immediately implies {@{relations between the [polylogarithm](polylogarithm.md) functions, the Stirling number exponential [generating functions](generating%20function.md) given above, and the Stirling-number-based power series for the generalized [Nielsen polylogarithm](http://mathworld.wolfram.com/NielsenGeneralizedPolylogarithm.html) functions}@}. <!--SR:!2025-02-01,77,329!2025-01-22,70,331!2025-07-31,211,331!2025-01-26,60,289-->

## generalizations

There are {@{many notions of _generalized Stirling numbers_ that may be defined (depending on application) in a number of differing combinatorial contexts}@}. In so much as {@{the Stirling numbers of the first kind}@} correspond to {@{the coefficients of the distinct polynomial expansions of the [single factorial function](factorial.md), $n!=n(n-1)(n-2)\cdots 2\cdot 1$}@}, we may {@{extend this notion to define triangular recurrence relations for more general classes of products}@}. <!--SR:!2025-02-02,78,329!2025-06-11,159,311!2025-01-22,70,331!2025-01-24,72,331-->

In particular, for {@{any fixed arithmetic function $f:\mathbb {N} \rightarrow \mathbb {C}$ and symbolic parameters $x,t$}@}, {@{related generalized factorial products}@} of the form {@{$$(x)_{n,f,t}:=\prod _{k=1}^{n-1}\left(x+{\frac {f(k)}{t^{k} } }\right)$$}@} (annotation: Note that {@{$k$ starts from 1 and ends at $n - 1$}@}.) may be studied from {@{the point of view of the classes of generalized Stirling numbers of the first kind}@} defined by the following coefficients of the powers of $x$ in the expansions of $(x)_{n,f,t}$ and then by the next corresponding triangular recurrence relation: <!--SR:!2025-01-24,72,331!2025-02-02,78,329!2025-04-04,108,291!2025-01-24,72,331!2025-01-31,76,329-->

- generalized [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md) defined by the coefficients of the powers of _x_ in the expansions of (_x_)<sub>_n_,_f_,_t_</sub> ::@:: $$\left[{\begin{matrix}n\\k\end{matrix} }\right]_{f,t}=\left[x^{k - 1}\right](x)_{n,f,t}$$ <!--SR:!2025-06-16,165,311!2025-03-19,95,289-->
- generalized [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md) defined by a corresponding triangular recurrence relation ::@:: $$\left[{\begin{matrix}n\\k\end{matrix} }\right]_{f,t}=\frac {f(n-1)} {t^{n - 1} }\left[{\begin{matrix}n-1\\k\end{matrix} }\right]_{f,t}+\left[{\begin{matrix}n-1\\k-1\end{matrix} }\right]_{f,t}+\delta _{n,0}\delta _{k,0}$$ (annotation: Notice that the ordinary unsigned [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md) also satisfies the above recurrence, but with $f(n) := n$ and $t = 1$ always. The unsigned one has $f(n) := -n$ and $t = 1$ always.) <!--SR:!2025-03-27,88,251!2025-01-09,54,309-->

These coefficients {@{satisfy a number of analogous properties to those for the Stirling numbers of the first kind}@} as well as {@{recurrence relations and functional equations related to the _f-harmonic numbers_}@}, {@{$$F_{n}^{(r)}(t):=\sum _{k\leq n} \frac {t^{k} } {f(k)^{r} } \,.$$}@}<sup>[\[21\]](#^ref-21)</sup> {@{One special case of these bracketed coefficients corresponding to $t\equiv 1$}@} allows us to {@{expand the multiple factorial, or [multifactorial](double%20factorial.md#generalizations) functions as polynomials in $n$}@}.<sup>[\[22\]](#^ref-22)</sup> <!--SR:!2025-04-12,114,291!2025-03-17,98,291!2025-02-18,76,269!2025-04-14,118,311!2025-01-09,54,309-->

{@{The [Stirling numbers](Stirling%20number.md) of both kinds, the [binomial coefficients](binomial%20coefficient.md), and the first and second-order [Eulerian numbers](eulerian%20number.md)}@} are all {@{defined by special cases of a triangular _super-recurrence_ of the form $$\left|{\begin{matrix}n\\k\end{matrix} }\right|=(\alpha n+\beta k+\gamma )\left|{\begin{matrix}n-1\\k\end{matrix} }\right|+(\alpha ^{\prime }n+\beta ^{\prime }k+\gamma ^{\prime })\left|{\begin{matrix}n-1\\k-1\end{matrix} }\right|+\delta _{n,0}\delta _{k,0},$$}@} for {@{integers $n,k\geq 0$ and where $\left|{\begin{matrix}n\\k\end{matrix} }\right|\equiv 0$ whenever $n<0$ or $k<0$}@}. In this sense, the form of the Stirling numbers of the first kind may also be generalized by {@{this parameterized super-recurrence for fixed scalars $\alpha ,\beta ,\gamma ,\alpha ^{\prime },\beta ^{\prime },\gamma ^{\prime }$ (not all zero)}@}. <!--SR:!2025-02-03,79,329!2025-08-18,229,331!2025-04-21,134,311!2025-01-23,71,331-->

## see also

- [Stirling numbers](Stirling%20number.md)
- [Stirling numbers of the second kind](Stirling%20numbers%20of%20the%20second%20kind.md)
- [Stirling polynomials](Stirling%20polynomials.md)
- [random permutation statistics](random%20permutation%20statistics.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Wilf, Herbert S. (1990). _Generatingfunctionology_. San Diego, CA, USA: Academic Press. p. 73. [ISBN](ISBN.md) [978-148324857-8](https://en.wikipedia.org/wiki/Special:BookSources/978-148324857-8). <a id="^ref-1"></a>^ref-1
2. Knuth, Donald E. (1992). ["Two Notes on Notation"](https://www.jstor.org/stable/2325085). _American Mathematical Monthly_. __99__ (5): 403–422 – via JSTOR. <a id="^ref-2"></a>^ref-2
3. Rényi, Alfred (1962). ["Théorie des éléments saillants d'une suite d'observations"](http://www.numdam.org/item/ASCFM_1962__8_2_7_0/). _Annales scientifiques de l'Université de Clermont. Mathématiques_. Tome 8 (2): 7–13. <a id="^ref-3"></a>^ref-3
4. See section 6.2 and 6.5 of _Concrete Mathematics_. <a id="^ref-4"></a>^ref-4
5. [Richard P. Stanley](Richard%20P.%20Stanley.md), _Enumerative Combinatorics, volume 1_ (2nd ed.). Page 34 of the [online version](http://math.mit.edu/~rstan/ec/ec1.pdf). <a id="^ref-5"></a>^ref-5
6. Adamchik, Victor (1997). ["On Stirling numbers and Euler sums"](https://scholar.archive.org/work/7dd3uhgmr5fb5cv63sas2uqmgq). _Journal of Computational and Applied Mathematics_. __79__ (1): 119–130. [doi](digital%20object%20identifier.md):[10.1016/S0377-0427(96)00167-7](https://doi.org/10.1016%2FS0377-0427%2896%2900167-7). [MR](Mathematical%20Reviews.md) [1437973](https://mathscinet.ams.org/mathscinet-getitem?mr=1437973). <a id="^ref-6"></a>^ref-6
7. Flajolet and Sedgewick (1995). ["Mellin transforms and asymptotics: Finite differences and Rice's integrals"](https://hal.inria.fr/inria-00074439/file/RR-2231.pdf) (PDF). _Theoretical Computer Science_. __144__ (1–2): 101–124. [doi](digital%20object%20identifier.md):[10.1016/0304-3975(94)00281-m](https://doi.org/10.1016%2F0304-3975%2894%2900281-m). <a id="^ref-7"></a>^ref-7
8. Schmidt, M. D. (30 October 2016). "Zeta Series Generating Function Transformations Related to Polylogarithm Functions and the _k_-Order Harmonic Numbers". [arXiv](ArXiv.md):[1610.09666](https://arxiv.org/abs/1610.09666) [[math.CO](https://arxiv.org/archive/math.CO)]. <a id="^ref-8"></a>^ref-8
9. Schmidt, M. D. (3 November 2016). "Zeta Series Generating Function Transformations Related to Generalized Stirling Numbers and Partial Sums of the Hurwitz Zeta Function". [arXiv](ArXiv.md):[1611.00957](https://arxiv.org/abs/1611.00957) [[math.CO](https://arxiv.org/archive/math.CO)]. <a id="^ref-9"></a>^ref-9
10. A table of the second-order Eulerian numbers and a synopsis of their properties is found in section 6.2 of _Concrete Mathematics_. For example, we have that $\sum _{k}\left\langle \!\!\left\langle {n \atop k}\right\rangle \!\!\right\rangle =(2n-1)(2n-3)\cdots 1=(2n-1)!!$. These numbers also have the following combinatorial interpretation: If we form all permutations of the [multiset](multiset.md) $\{1,1,2,2,\ldots ,n,n\}$ with the property that all numbers between the two occurrences of $k$ are greater than $k$ for $1\leq k\leq n$, then $\left\langle \!\!\left\langle {n \atop k}\right\rangle \!\!\right\rangle$ is the number of such permutations that have $k$ ascents. <a id="^ref-10"></a>^ref-10
11. Schmidt, M. D. (2016). "A Computer Algebra Package for Polynomial Sequence Recognition". [arXiv](ArXiv.md):[1609.07301](https://arxiv.org/abs/1609.07301) [[math.CO](https://arxiv.org/archive/math.CO)]. <a id="^ref-11"></a>^ref-11
12. Herbert Wilf, [Generatingfunctionology](https://www.math.upenn.edu/~wilf/gfologyLinked2.pdf), Section 4.6. <a id="^ref-12"></a>^ref-12
13. Schmidt, M. D. (2017). ["Jacobi-Type Continued Fractions for the Ordinary Generating Functions of Generalized Factorial Functions"](https://cs.uwaterloo.ca/journals/JIS/VOL20/Schmidt/schmidt14.html). _J. Integer Seq_. __20__ (3). [arXiv](ArXiv.md):[1610.09691](https://arxiv.org/abs/1610.09691). <a id="^ref-13"></a>^ref-13
14. Ia. V. Blagouchine (2016). "Two series expansions for the logarithm of the gamma function involving Stirling numbers and containing only rational coefficients for certain arguments related to _π_<sup>−1</sup>". _Journal of Mathematical Analysis and Applications_. __442__ (2): 404–434. [arXiv](ArXiv.md):[1408.3902](https://arxiv.org/abs/1408.3902). [doi](digital%20object%20identifier.md):[10.1016/j.jmaa.2016.04.032](https://doi.org/10.1016%2Fj.jmaa.2016.04.032). [S2CID](Semantic%20Scholar.md#S2CID) [119661147](https://api.semanticscholar.org/CorpusID:119661147). [arXiv](https://arxiv.org/abs/1408.3902) <a id="^ref-14"></a>^ref-14
15. Blagouchine, Iaroslav V. (2018). ["Three Notes on Ser's and Hasse's Representations for the Zeta-functions"](http://math.colgate.edu/~integers/vol18a.html). _INTEGERS: The Electronic Journal of Combinatorial Number Theory_. __18A__: 1–45. [arXiv](ArXiv.md):[1606.02044](https://arxiv.org/abs/1606.02044). [Bibcode](bibcode.md):[2016arXiv160602044B](https://ui.adsabs.harvard.edu/abs/2016arXiv160602044B). <a id="^ref-15"></a>^ref-15
16. See also some more interesting series representations and expansions mentioned in Connon's article: Connon, D. F. (2007). "Some series and integrals involving the Riemann zeta function, binomial coefficients and the harmonic numbers (Volume I)". [arXiv](ArXiv.md):[0710.4022](https://arxiv.org/abs/0710.4022) [[math.HO](https://arxiv.org/archive/math.HO)].. <a id="^ref-16"></a>^ref-16
17. These estimates are found in Section 26.8 of the _NIST Handbook of Mathematical Functions_. <a id="^ref-17"></a>^ref-17
18. Malenfant, Jerome (2011). "Finite, closed-form expressions for the partition function and for Euler, Bernoulli, and Stirling numbers". [arXiv](ArXiv.md):[1103.1585](https://arxiv.org/abs/1103.1585) [[math.NT](https://arxiv.org/archive/math.NT)]. <a id="^ref-18"></a>^ref-18
19. Komatsu, Takao; Pita-Ruiz, Claudio (2018). ["Some formulas for Bell numbers"](http://www.doiserbia.nb.rs/Article.aspx?ID=0354-51801811881K). _Filomat_. __32__ (11): 3881–3889. [doi](digital%20object%20identifier.md):[10.2298/FIL1811881K](https://doi.org/10.2298%2FFIL1811881K). [ISSN](ISSN.md) [0354-5180](https://search.worldcat.org/issn/0354-5180). <a id="^ref-19"></a>^ref-19
20. Ia. V. Blagouchine (2016). "Expansions of generalized Euler's constants into the series of polynomials in _π_<sup>−2</sup> and into the formal enveloping series with rational coefficients only". _Journal of Number Theory_. __158__ (2): 365–396. [doi](digital%20object%20identifier.md):[10.1016/j.jnt.2015.06.012](https://doi.org/10.1016%2Fj.jnt.2015.06.012). [arXiv](https://arxiv.org/abs/1501.00740) <a id="^ref-20"></a>^ref-20
21. Schmidt, Maxie D. (2016). "Combinatorial Identities for Generalized Stirling Numbers Expanding $f$-Factorial Functions and the $f$-Harmonic Numbers". [arXiv](ArXiv.md):[1611.04708](https://arxiv.org/abs/1611.04708) [[math.CO](https://arxiv.org/archive/math.CO)]. <a id="^ref-21"></a>^ref-21
22. Schmidt, Maxie D. (2010). ["Generalized j-Factorial Functions, Polynomials, and Applications"](https://cs.uwaterloo.ca/journals/JIS/VOL13/Schmidt/multifact.html). _J. Integer Seq_. __13__. <a id="^ref-22"></a>^ref-22

- [The Art of Computer Programming](The%20Art%20of%20Computer%20Programming.md)
- [Concrete Mathematics](Concrete%20Mathematics.md)
- M. Abramowitz, I. Stegun, ed. (1972). "§24.1.3. Stirling Numbers of the First Kind". _Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables_ (9th ed.). New York: Dover. p. 824.
- [Stirling numbers of the first kind, s(n,k)](https://planetmath.org/Stirlingnumbersofthefirstkind) at [PlanetMath](PlanetMath.md)..
- [Sloane, N. J. A.](Neil%20Sloane.md) (ed.). ["Sequence A008275 (Triangle read by rows of Stirling numbers of first kind)"](https://oeis.org/A008275). _The [On-Line Encyclopedia of Integer Sequences](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)_. OEIS Foundation.
