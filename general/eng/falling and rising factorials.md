---
aliases:
  - Pochhammer symbol
  - Pochhammer symbols
  - falling factorial
  - falling factorials
  - falling and rising factorial
  - falling and rising factorials
  - rising factorial
  - rising factorials
tags:
  - flashcard/active/general/eng/falling_and_rising_factorials
  - language/in/English
---

# falling and rising factorials

In [mathematics](mathematics.md), {@{the __falling factorial__}@} (sometimes called {@{the __descending factorial__,<sup>[\[1\]](#^ref-1)</sup> __falling sequential product__, or __lower factorial__}@}) is defined as {@{the polynomial $${\begin{aligned}(x)_{n}=x^{\underline {n} }&=\overbrace {x(x-1)(x-2)\cdots (x-n+1)} ^{n{\text{ factors} } }\\&=\prod _{k=1}^{n}(x-k+1)=\prod _{k=0}^{n-1}(x-k).\end{aligned} }$$}@} <!--SR:!2028-11-24,1159,350!2029-03-20,1251,350!2028-12-25,1183,350-->

{@{The __rising factorial__}@} (sometimes called {@{the __Pochhammer function__, __Pochhammer polynomial__, __ascending factorial__,<sup>[\[1\]](#^ref-1)</sup> __rising sequential product__, or __upper factorial__}@}) is defined as {@{$${\begin{aligned}(x)^{n}=x^{\overline {n} }&=\overbrace {x(x+1)(x+2)\cdots (x+n-1)} ^{n{\text{ factors} } }\\&=\prod _{k=1}^{n}(x+k-1)=\prod _{k=0}^{n-1}(x+k).\end{aligned} }$$}@} <!--SR:!2029-01-07,1195,350!2029-05-04,1285,350!2028-09-18,1106,350-->

The value of each is {@{taken to be 1 (an [empty product](empty%20product.md))}@} when {@{$n=0$}@}. These symbols are {@{collectively called __factorial powers__}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2029-04-29,1281,350!2029-01-23,1205,350!2029-01-11,1197,350-->

{@{The __Pochhammer symbol__}@}, introduced by {@{[Leo August Pochhammer](Leo%20August%20Pochhammer.md)}@}, is {@{the notation $(x)_{n}$, where _n_ is a [non-negative integer](natural%20number.md)}@}. It may represent {@{_either_ the rising or the falling factorial, with different articles and authors using different conventions}@}. Pochhammer himself actually {@{used $(x)_{n}$ with yet another meaning, namely to denote the [binomial coefficient](binomial%20coefficient.md) ${\tbinom {x}{n} }$}@}.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2029-06-01,1308,350!2026-04-25,364,290!2029-02-11,1221,350!2027-11-20,841,330!2029-01-18,1201,350-->

In this article, {@{the symbol $(x)_{n}$}@} is used to {@{represent the falling factorial}@}, and {@{the symbol $x^{(n)}$}@} is used {@{for the rising factorial}@}. These conventions are {@{used in [combinatorics](combinatorics.md)}@},<sup>[\[4\]](#^ref-4)</sup> although {@{[Knuth](Donald%20Knuth.md)'s underline and overline notations $x^{\underline {n} }$ and $x^{\overline {n} }$}@} are increasingly popular.<sup>[\[2\]](#^ref-2)</sup><sup>[\[5\]](#^ref-5)</sup> In {@{the theory of [special functions](special%20functions.md) (in particular the [hypergeometric function](hypergeometric%20function.md))}@} and in the standard reference work _[Abramowitz and Stegun](Abramowitz%20and%20Stegun.md)_, {@{the Pochhammer symbol $(x)_{n}$}@} is used to {@{represent the rising factorial}@}.<sup>[\[6\]](#^ref-6)</sup><sup>[\[7\]](#^ref-7)</sup> <!--SR:!2028-12-07,1169,350!2028-11-14,1152,350!2029-04-30,1281,350!2028-12-20,1180,350!2029-01-09,1196,350!2028-12-31,1188,350!2029-02-04,1215,350!2028-11-06,1147,350!2029-03-25,1255,350-->

When {@{$x$ is a positive integer}@}, {@{$(x)_{n}$}@} gives {@{the number of [_n_-permutations](permutation.md#k-permutations%20of%20n) (sequences of distinct elements) from an _x_-element set}@}, or equivalently {@{the number of [injective functions](injective%20function.md) from a set of size $n$ to a set of size $x$}@}. {@{The rising factorial $x^{(n)}$}@} gives {@{the number of [partitions](partition%20of%20a%20set.md) of an $n$-element set into $x$ ordered sequences (possibly empty)}@}.<sup>[\[a\]](#^ref-a)</sup> (annotation: Think of {@{the number of slots to insert an new element from the $n$ element into the $x$ ordered sequences after each step}@}.) <!--SR:!2029-02-09,1219,350!2029-02-05,1216,350!2029-06-14,1318,350!2027-11-03,843,330!2029-05-09,1289,350!2027-10-14,816,330!2028-05-21,936,330-->

## examples and combinatorial interpretation

{@{The first few falling factorials}@} are as follows: {@{$${\begin{alignedat}{2}(x)_{0}&&&=1\\(x)_{1}&&&=x\\(x)_{2}&=x(x-1)&&=x^{2}-x\\(x)_{3}&=x(x-1)(x-2)&&=x^{3}-3x^{2}+2x\\(x)_{4}&=x(x-1)(x-2)(x-3)&&=x^{4}-6x^{3}+11x^{2}-6x\end{alignedat} }$$}@} <!--SR:!2029-05-14,1292,350!2029-01-08,1195,350-->

{@{The first few rising factorials}@} are as follows: {@{$${\begin{alignedat}{2}x^{(0)}&&&=1\\x^{(1)}&&&=x\\x^{(2)}&=x(x+1)&&=x^{2}+x\\x^{(3)}&=x(x+1)(x+2)&&=x^{3}+3x^{2}+2x\\x^{(4)}&=x(x+1)(x+2)(x+3)&&=x^{4}+6x^{3}+11x^{2}+6x\end{alignedat} }$$}@} <!--SR:!2029-02-16,1225,350!2028-10-09,1123,350-->

{@{The coefficients that appear in the expansions}@} are {@{[Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md)}@} (see below). <!--SR:!2029-03-13,1246,350!2029-03-05,1239,350-->

When {@{the variable $x$ is a positive integer}@}, {@{the number $(x)_{n}$}@} is equal to {@{the number of [_n_-permutations from a set of _x_ items](permutation.md#k-permutations%20of%20n)}@}, that is, {@{the number of ways of choosing an ordered list of length _n_ consisting of distinct elements drawn from a collection of size $x$}@}. For example, {@{$(8)_{3}=8\times 7\times 6=336$}@} is {@{the number of different podiums—assignments of gold, silver, and bronze medals—possible in an eight-person race}@}. On the other hand, {@{$x^{(n)}$}@} is {@{"the number of ways to arrange $n$ flags on $x$ flagpoles"}@},<sup>[\[8\]](#^ref-8)</sup> where {@{all flags must be used and each flagpole can have any number of flags}@}. Equivalently, this is {@{the number of ways to partition a set of size $n$ \(the flags\) into $x$ distinguishable parts \(the poles\)}@}, with {@{a linear order on the elements assigned to each part \(the order of the flags on a given pole\)}@}. <!--SR:!2027-11-27,862,330!2029-01-15,1200,350!2027-12-03,814,330!2028-10-22,1134,350!2027-08-19,768,330!2028-09-22,1109,350!2029-03-03,1237,350!2026-11-01,536,310!2025-12-05,64,359!2026-01-15,95,380!2026-01-10,91,380-->

## properties

The rising and falling factorials are {@{simply related to one another}@}: {@{$${\begin{alignedat}{2}{(x)}_{n}&={(x-n+1)}^{(n)}&&=(-1)^{n}(-x)^{(n)},\\x^{(n)}&={(x+n-1)}_{n}&&=(-1)^{n}(-x)_{n}.\end{alignedat} }$$}@} (annotation: The middle expression is trivial to obtain, while the rightmost expression can be obtained by {@{negating the term inside parentheses and multiplying by $(-1)^n$ outside}@}.) <!--SR:!2028-11-23,1160,350!2029-06-09,1314,350!2029-02-25,1232,350-->

Falling and rising factorials of integers are {@{directly related to the ordinary [factorial](factorial.md)}@}: {@{$${\begin{aligned}n!&=1^{(n)}=(n)_{n},\\[6pt](m)_{n}&={\frac {m!}{(m-n)!} },\\[6pt]m^{(n)}&={\frac {(m+n-1)!}{(m-1)!} }.\end{aligned} }$$}@} <!--SR:!2029-05-15,1293,350!2028-10-13,1126,350-->

{@{Rising factorials of half integers}@} are {@{directly related to the [double factorial](double%20factorial.md)}@}: {@{$${\begin{aligned}\left[{\frac {1}{2} }\right]^{(n)}={\frac {(2n-1)!!}{2^{n} } },\quad \left[{\frac {2m+1}{2} }\right]^{(n)}={\frac {(2(n+m)-1)!!}{2^{n}(2m-1)!!} }.\end{aligned} }$$}@} <!--SR:!2027-08-07,764,330!2025-12-13,264,270!2026-05-14,345,250-->

The falling and rising factorials can be used to {@{express a [binomial coefficient](binomial%20coefficient.md)}@}: {@{$${\begin{aligned}{\frac {(x)_{n} }{n!} }&={\binom {x}{n} },\\[6pt]{\frac {x^{(n)} }{n!} } & = \binom {x+n-1} n = \left(\!\! \binom x n \!\!\right).\end{aligned} }$$}@} (annotation: The above is obvious, but the below is also {@{a multiset coefficient}@}.) Thus {@{many identities on binomial coefficients carry over to the falling and rising factorials}@}. <!--SR:!2029-06-18,1322,350!2027-11-12,850,330!2029-06-20,1323,350!2027-08-23,785,330-->

The rising and falling factorials are {@{well defined in any [unital](ring%20(mathematics).md) [ring](ring%20(mathematics).md)}@}, and therefore $x$ can be {@{taken to be, for example, a [complex number](complex%20number.md), including negative integers, or a [polynomial](polynomial.md) with complex coefficients, or any [complex-valued function](complex%20analysis.md)}@}. <!--SR:!2029-02-28,1236,350!2027-10-27,837,330-->

### real numbers and negative _n_

The falling factorial can be {@{extended to [real](real%20number.md) values of $x$ using the [gamma function](gamma%20function.md)}@} provided {@{$x$ and $x+n$ are real numbers that are not negative integers}@}: {@{$$(x)_{n}={\frac {\Gamma (x+1)}{\Gamma (x-n+1)} }\ ,$$}@} and so can the rising factorial: {@{$$x^{(n)}={\frac {\Gamma (x+n)}{\Gamma (x)} }\ .$$}@} <!--SR:!2028-12-21,1180,350!2029-01-28,1209,350!2027-11-11,849,330!2027-07-12,756,330-->

### calculus

Falling factorials appear in {@{multiple [differentiation](derivative.md) of simple power functions}@}: {@{$$\left({\frac {\mathrm {d} }{\mathrm {d} x} }\right)^{n}x^{a}=(a)_{n}\cdot x^{a-n}.$$}@} <!--SR:!2029-05-13,1292,350!2027-09-22,798,330-->

The rising factorial is also integral to {@{the definition of the [hypergeometric function](hypergeometric%20function.md): The hypergeometric function}@} is defined for {@{$|z|<1$ by the [power series](power%20series.md)}@} {@{$${}_{2}F_{1}(a,b;c;z)=\sum _{n=0}^{\infty }{\frac {a^{(n)}b^{(n)} }{c^{(n)} } }{\frac {z^{n} }{n!} }$$}@} provided that {@{$c\neq 0,-1,-2,\ldots$}@}. Note, however, that {@{the hypergeometric function literature typically uses the notation $(a)_{n}$ for rising factorials}@}. <!--SR:!2027-08-23,772,330!2026-02-23,120,250!2026-08-18,493,310!2025-11-20,24,367!2025-11-21,25,367-->

## connection coefficients and identities

Falling and rising factorials are {@{closely related to [Stirling numbers](Stirling%20number.md)}@}. Indeed, expanding the product {@{reveals [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md)}@}: {@{$${\begin{aligned}(x)_{n}&=\sum _{k=0}^{n}s(n,k)x^{k}\\&=\sum _{k=0}^{n}{\begin{bmatrix}n\\k\end{bmatrix} }(-1)^{n-k}x^{k}\\x^{(n)}&=\sum _{k=0}^{n}{\begin{bmatrix}n\\k\end{bmatrix} }x^{k}\\\end{aligned} }$$}@} (annotation: The change of basis from the falling factorials uses {@{signed while that from the rising factorials uses unsigned}@}.) <!--SR:!2029-03-09,1242,350!2026-11-16,551,310!2027-10-09,819,330!2026-04-25,365,290-->

And the inverse relations {@{uses [Stirling numbers of the second kind](Stirling%20numbers%20of%20the%20second%20kind.md)}@}: {@{$${\begin{aligned}x^{n}&=\sum _{k=0}^{n}{\begin{Bmatrix}n\\k\end{Bmatrix} }(x)_{k}\\&=\sum _{k=0}^{n}{\begin{Bmatrix}n\\k\end{Bmatrix} }(-1)^{n-k}x^{(k)}.\end{aligned} }$$}@} (annotation: The change of basis to the falling factorials uses {@{unsigned and that to the rising factorials uses signed}@}.) <!--SR:!2029-02-03,1216,350!2027-08-17,653,270!2027-07-22,634,270-->

The falling and rising factorials are {@{related to one another through the [Lah numbers](Lah%20number.md) $L(n,k)={\binom {n-1}{k-1} }{\frac {n!}{k!} }$}@}:<sup>[\[9\]](#^ref-9)</sup> {@{$${\begin{aligned}x^{(n)}&=\sum _{k=0}^{n}L(n,k)(x)_{k}\\(x)_n&=\sum _{k=0}^{n}L(n,k)(-1)^{n-k}x^{(k)}\end{aligned} }$$}@} (annotation: The change of basis to the falling factorials {@{use unsigned while that to the rising factorials uses signed}@}.) <!--SR:!2028-11-22,1159,350!2026-06-07,389,290!2026-03-18,143,310-->

Since {@{the falling factorials are a basis for the [polynomial ring](polynomial%20ring.md)}@}, one can {@{express the product of two of them as a [linear combination](linear%20combination.md) of falling factorials}@}:<sup>[\[10\]](#^ref-10)</sup> {@{$$(x)_{m}(x)_{n}=\sum _{k=0}^{m}{\binom {m}{k} }{\binom {n}{k} }k!\cdot (x)_{m+n-k}\ .$$}@} {@{The coefficients ${\tbinom {m}{k} }{\tbinom {n}{k} }k!$}@} are {@{called _connection coefficients_}@}, and have a combinatorial interpretation as {@{the number of ways to identify (or "glue together") _k_ elements each from a set of size _m_ and a set of size _n_}@}. <!--SR:!2027-03-22,613,310!2026-06-12,274,270!2026-05-27,281,250!2026-10-19,529,310!2029-05-25,1301,350!2029-06-10,1315,350-->

There is also a connection formula for {@{the ratio of two rising factorials}@} given by {@{$${\frac {x^{(n)} }{x^{(i)} } }=(x+i)^{(n-i)},\quad {\text{for } }n\geq i.$$}@} <!--SR:!2028-11-28,1164,350!2027-08-14,768,330-->

Additionally, we can {@{expand generalized exponent laws and negative rising and falling powers}@} through the following identities:<sup>[\[11\]](#^ref-11)</sup><sup>[\[52\]](#^ref-52)</sup> <!--SR:!2029-01-16,1201,350-->

- generalized exponent law for falling factorial ::@:: $$(x)_{m+n}=(x)_{m}(x-m)_{n}=(x)_{n}(x-n)_{m}$$ <!--SR:!2029-06-21,1324,350!2029-03-19,1250,350-->
- generalized exponent law for rising factorial ::@:: $$x^{(m+n)}=x^{(m)}(x+m)^{(n)}=x^{(n)}(x+n)^{(m)}$$ <!--SR:!2028-11-21,1158,350!2028-11-29,1165,350-->
- negative rising factorial ::@:: $$x^{(-n)}={\frac {\Gamma (x-n)}{\Gamma (x)} }={\frac {(x-n-1)!}{(x-1)!} }={\frac {1}{(x-n)^{(n)} } }={\frac {1}{(x-1)_{n} } }={\frac {1}{(x-1)(x-2)\cdots (x-n)} }$$ <!--SR:!2028-04-27,905,290!2026-11-15,550,310-->
- negative falling factorial ::@:: $$(x)_{-n}={\frac {\Gamma (x+1)}{\Gamma (x+n+1)} }={\frac {x!}{(x+n)!} }={\frac {1}{(x+n)_{n} } }={\frac {1}{(x+1)^{(n)} } }={\frac {1}{(x+1)(x+2)\cdots (x+n)} }$$ <!--SR:!2026-06-14,396,290!2025-11-07,242,270-->

Finally, {@{[duplication](multiplication%20theorem.md) and [multiplication formulas](multiplication%20theorem.md)}@} for {@{the falling and rising factorials}@} provide {@{the next relations}@}: \(annotation: 4 items: {@{multiplication formula for falling factorial, multiplication formula for rising factorial, multiplication formula for rising factorial in its base, duplication formula for rising factorial}@}\) <!--SR:!2028-05-29,941,330!2025-11-26,23,369!2025-11-26,23,369!2025-11-27,24,369-->

- multiplication formula for falling factorial ::@:: $$(x)_{k+mn}=(x)_{k} m^{mn}\prod _{j=0}^{m-1}\left({\frac {x-k-j}{m} }\right)_{n}\,,{\text{for } }m\in \mathbb {N}$$ (annotation: $(x)_k$ produces the initial $k$ terms. The product symbol and its formula produces the remaining $mn$ terms, though all divided by $m$. The $m^{mn}$ undivides said terms.) <!--SR:!2026-11-11,546,310!2025-12-06,260,270-->
- multiplication formula for rising factorial ::@:: $$x^{(k+mn)}=x^{(k)}m^{mn}\prod _{j=0}^{m-1}\left({\frac {x+k+j}{m} }\right)^{(n)},{\text{for } }m\in \mathbb {N}$$ (annotation: $x^{(k)}$ produces the initial $k$ terms. The product symbol and its formula produces the remaining $mn$ terms, though all divided by $m$. The $m^{mn}$ undivides said terms.) <!--SR:!2026-06-04,386,290!2026-10-31,535,310-->
- multiplication formula for rising factorial in its base ::@:: $$(ax+b)^{(n)}=x^{n}\prod _{j=0}^{n-1}\left(a+{\frac {b+j}{x} }\right),{\text{for } }n\in \mathbb {\mathbb N}$$ (annotation: Split $x^n$ into $n$ $x$ and multiply each of it into each $\left(a + \frac {b + j} x \right)$ to get $(ax + b + j)$.) <!--SR:!2028-02-17,857,290!2025-12-14,265,270-->
- duplication formula for rising factorial ::@:: $$(2x)^{(2n)}=2^{2n}x^{(n)}\left(x+{\frac {1}{2} }\right)^{(n)}.$$ (annotation: Simply apply the multiplication formula for rising factorial with $(k, m, n) = (0, 2, n)$.) <!--SR:!2026-11-05,540,310!2027-11-21,842,330-->

## relation to umbral calculus

The falling factorial occurs in {@{a formula which represents [polynomials](polynomial.md)}@} using {@{the forward [difference operator](recurrence%20relation.md#difference%20operator) $\Delta f(x){\stackrel {\mathrm {def} }{=} }f(x{+}1)-f(x),$}@} and {@{which is formally similar to [Taylor's theorem](taylor's%20theorem.md):$$f(x)=\sum _{n=0}^{\infty }{\frac {\Delta ^{n}f(0)}{n!} }(x)_{n}.$$}@} <!--SR:!2028-12-24,1182,350!2029-01-24,1206,350!2025-12-12,264,270-->

In {@{this formula and in many other places}@}, {@{the falling factorial $(x)_{n}$ in the calculus of [finite differences](finite%20difference.md)}@} plays {@{the role of $x^{n}$ in differential calculus}@}. Note for instance {@{the similarity of $\Delta (x)_{n}=n(x)_{n-1}$ to ${\frac {\textrm {d} }{ {\textrm {d} }x} }x^{n}=nx^{n-1}$}@}. <!--SR:!2029-06-03,1309,350!2027-11-05,845,330!2028-10-03,1118,350!2027-11-22,843,330-->

A similar result holds for {@{the rising factorial and the backward difference operator}@}. <!--SR:!2027-08-19,781,330-->

{@{The study of analogies of this type}@} is known as {@{[umbral calculus](umbral%20calculus.md)}@}. {@{A general theory covering such relations, including the falling and rising factorial functions}@}, is given by {@{the theory of [polynomial sequences of binomial type](binomial%20type.md) and [Sheffer sequences](Sheffer%20sequence.md)}@}. Falling and rising factorials are {@{Sheffer sequences of binomial type}@}, as shown by the relations: {@{$${\begin{aligned}(a+b)_{n}&=\sum _{j=0}^{n}{\binom {n}{j} }(a)_{n-j}(b)_{j}\\[6pt](a+b)^{(n)}&=\sum _{j=0}^{n}{\binom {n}{j} }a^{(n-j)}b^{(j)}\end{aligned} }$$}@} where the coefficients are {@{the same as those in the [binomial theorem](binomial%20theorem.md)}@}. <!--SR:!2029-05-10,1290,350!2027-09-04,794,330!2029-06-04,1310,350!2026-11-09,544,310!2028-12-02,1165,350!2028-04-02,886,290!2029-01-10,1196,350-->

Similarly, {@{the generating function of Pochhammer polynomials (the sequence of $(x)_n$)}@} then {@{amounts to the umbral exponential}@}, {@{$$\sum _{n=0}^{\infty }(x)_{n}{\frac {t^{n} }{n!} }=\left(1+t\right)^{x},$$}@} since {@{$$\operatorname {\Delta } _{x}\left(1+t\right)^{x}=t\cdot \left(1+t\right)^{x}.$$}@} (annotation: $\Delta_x$ is {@{the forward difference operator}@}.) <!--SR:!2026-10-26,536,310!2026-06-06,400,290!2027-07-14,628,270!2028-10-26,1137,350!2029-02-26,1233,350-->

## alternative notations

An alternative notation for {@{the rising factorial}@} {@{$$x^{\overline {m} }\equiv (x)_{+m}\equiv (x)_{m}=\overbrace {x(x+1)\ldots (x+m-1)} ^{m{\text{ factors} } }\quad {\text{for integer } }m\geq 0$$}@} and for {@{the falling factorial}@} {@{$$x^{\underline {m} }\equiv (x)_{-m}=\overbrace {x(x-1)\ldots (x-m+1)} ^{m{\text{ factors} } }\quad {\text{for integer } }m\geq 0$$}@} goes back to {@{A. Capelli (1893) and L. Toscano (1939), respectively}@}.<sup>[\[2\]](#^ref-2)</sup> {@{Graham, Knuth, and Patashnik}@}<sup>[\[11\]](#^ref-11)</sup><sup>[\[47\]](#^ref-47)</sup> propose to pronounce these expressions as {@{"$x$ to the $m$ rising" and "$x$ to the $m$ falling", respectively}@}. <!--SR:!2029-03-17,1249,350!2029-03-18,1250,350!2029-03-26,1256,350!2029-05-22,1299,350!2026-03-08,351,290!2028-01-15,886,330!2029-02-13,1222,350-->

An alternative notation for {@{the rising factorial $x^{(n)}$}@} is {@{the less common $(x)_{n}^{+}$. When $(x)_{n}^{+}$}@} is used to denote the rising factorial, {@{the notation $(x)_{n}^{-}$}@} is typically used for {@{the ordinary falling factorial, to avoid confusion}@}.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2029-05-12,1291,350!2029-01-27,1210,350!2029-02-22,1230,350!2029-01-20,1204,350-->

## generalizations

The Pochhammer symbol has a generalized version called {@{the [generalized Pochhammer symbol](generalized%20Pochhammer%20symbol.md), used in multivariate [analysis](mathematical%20analysis.md)}@}. There is also {@{a [_q_-analogue](q-analog.md), the [_q_-Pochhammer symbol](q-Pochhammer%20symbol.md)}@}. <!--SR:!2027-12-29,870,330!2027-09-18,794,330-->

For {@{any fixed arithmetic function $f:\mathbb {N} \rightarrow \mathbb {C}$ and symbolic parameters _x_, _t_}@}, {@{related generalized factorial products}@} of the form {@{$$(x)_{n,f,t}:=\prod _{k=1}^{n-1}\left(x+{\frac {f(k)}{t^{k} } }\right)$$}@} (annotation: Note that {@{$k$ starts from 1 and ends at $n - 1$}@}.) may be studied from {@{the point of view of the classes of generalized [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md)}@} defined by {@{the following coefficients of the powers of _x_ in the expansions of (_x_)<sub>_n_,_f_,_t_</sub>}@} and then by {@{the next corresponding triangular recurrence relation}@}: <!--SR:!2027-01-25,573,310!2029-01-29,1210,350!2025-12-06,260,270!2027-11-20,857,330!2027-10-25,824,330!2028-10-23,1135,350!2026-01-30,361,347-->

- generalized [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md) defined by the coefficients of the powers of _x_ in the expansions of (_x_)<sub>_n_,_f_,_t_</sub> ::@:: $$\left[{\begin{matrix}n\\k\end{matrix} }\right]_{f,t}=\left[x^{k - 1}\right](x)_{n,f,t}$$ <!--SR:!2026-11-12,547,310!2028-01-14,845,330-->
- generalized [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md) defined by a corresponding triangular recurrence relation ::@:: $$\left[{\begin{matrix}n\\k\end{matrix} }\right]_{f,t}=\frac {f(n-1)} {t^{n - 1} }\left[{\begin{matrix}n-1\\k\end{matrix} }\right]_{f,t}+\left[{\begin{matrix}n-1\\k-1\end{matrix} }\right]_{f,t}+\delta _{n,0}\delta _{k,0}$$ (annotation: Notice that the ordinary unsigned [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md) also satisfies the above recurrence, but with $f(n) := n$ and $t = 1$ always. The signed one has $f(n) := -n$ and $t = 1$ always.) <!--SR:!2025-12-13,265,270!2027-06-19,610,270-->

These coefficients satisfy {@{a number of analogous properties to those for the [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md)}@} as well as {@{recurrence relations and functional equations related to the _f_-harmonic numbers}@},<sup>[\[12\]](#^ref-12)</sup> {@{$$F_{n}^{(r)}(t):=\sum _{k\leq n}{\frac {t^{k} }{f(k)^{r} } }\,.$$}@} <!--SR:!2026-11-10,545,310!2027-01-17,554,270!2025-11-22,258,250-->

## see also

- [Pochhammer _k_-symbol](pochhammer%20k-symbol.md)
- [Vandermonde identity](vandermonde's%20identity.md)

## references

1. (a) Here the parts are distinct; for example, when _x_ = _n_ = 2, the (2)<sup>(2)</sup> = 6 partitions are $(12,-)$, $(21,-)$, $(1,2)$, $(2,1)$, $(-,12)$, and $(-,21)$, where − denotes an empty part. <a id="^ref-a"></a>^ref-a

This text incorporates [content](https://en.wikipedia.org/wiki/falling_and_rising_factorials) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. [Steffensen, J.F.](Johan%20Frederik%20Steffensen.md) (17 March 2006). _Interpolation_ (2nd ed.). Dover Publications. p. 8. [ISBN](ISBN.md) [0-486-45009-0](https://en.wikipedia.org/wiki/Special:BookSources/0-486-45009-0). — A reprint of the 1950 edition by Chelsea Publishing. <a id="^ref-1"></a>^ref-1
2. [Knuth, D.E.](Donald%20Knuth.md) _[The Art of Computer Programming](The%20Art%20of%20Computer%20Programming.md)_. Vol. 1 (3rd ed.). p. 50. <a id="^ref-2"></a>^ref-2
3. [Knuth, D.E.](Donald%20Knuth.md) (1992). "Two notes on notation". _[American Mathematical Monthly](The%20American%20Mathematical%20Monthly.md)_. __99__ (5): 403–422. [arXiv](ArXiv.md):[math/9205211](https://arxiv.org/abs/math/9205211). [doi](digital%20object%20identifier.md):[10.2307/2325085](https://doi.org/10.2307%2F2325085). [JSTOR](JSTOR.md) [2325085](https://www.jstor.org/stable/2325085). [S2CID](Semantic%20Scholar.md#S2CID) [119584305](https://api.semanticscholar.org/CorpusID:119584305). The remark about the Pochhammer symbol is on page 414. <a id="^ref-3"></a>^ref-3
4. [Olver, P.J.](Peter%20J.%20Olver.md) (1999). _Classical Invariant Theory_. Cambridge University Press. p. 101. [ISBN](ISBN.md) [0-521-55821-2](https://en.wikipedia.org/wiki/Special:BookSources/0-521-55821-2). [MR](Mathematical%20Reviews.md) [1694364](https://mathscinet.ams.org/mathscinet-getitem?mr=1694364). <a id="^ref-4"></a>^ref-4
5. Harris; Hirst; Mossinghoff (2008). _Combinatorics and Graph Theory_. Springer. ch. 2. [ISBN](ISBN.md) [978-0-387-79710-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-79710-6). <a id="^ref-5"></a>^ref-5
6. Abramowitz, Milton; Stegun, Irene A., eds. (December 1972) [June 1964]. [_Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables_](Abramowitz%20and%20Stegun.md). [National Bureau of Standards](National%20Institute%20of%20Standards%20and%20Technology.md) [Applied Mathematics](applied%20mathematics.md) Series. Vol. 55. Washington, DC: [United States Department of Commerce](United%20States%20Department%20of%20Commerce.md). p. 256 eqn. 6.1.22. [LCCN](Library%20of%20Congress%20Control%20Number.md) [64-60036](https://lccn.loc.gov/64-60036). <a id="^ref-6"></a>^ref-6
7. Slater, Lucy J. (1966). _Generalized Hypergeometric Functions_. Cambridge University Press. Appendix I. [MR](Mathematical%20Reviews.md) [0201688](https://mathscinet.ams.org/mathscinet-getitem?mr=0201688). — Gives a useful list of formulas for manipulating the rising factorial in (_x_)<sub>_n_</sub> notation. <a id="^ref-7"></a>^ref-7
8. Feller, William. _An Introduction to Probability Theory and Its Applications_. Vol. 1. Ch. 2. <a id="^ref-8"></a>^ref-8
9. ["Introduction to the factorials and binomials"](http://functions.wolfram.com/GammaBetaErf/Factorial/introductions/FactorialBinomials/05/). _Wolfram Functions Site_. <a id="^ref-9"></a>^ref-9
10. Rosas, Mercedes H. (2002). "Specializations of MacMahon symmetric functions and the polynomial algebra". _Discrete Math_. __246__ (1–3): 285–293. [doi](digital%20object%20identifier.md):[10.1016/S0012-365X(01)00263-1](https://doi.org/10.1016%2FS0012-365X%2801%2900263-1). [hdl](Handle%20System.md):[11441/41678](https://hdl.handle.net/11441%2F41678). <a id="^ref-10"></a>^ref-10
11. [Graham, Ronald L.](Ronald%20Graham.md); [Knuth, Donald E.](Donald%20Knuth.md) & [Patashnik, Oren](Oren%20Patashnik.md) (1988). _[Concrete Mathematics](Concrete%20Mathematics.md)_. Reading, MA: Addison-Wesley. pp. 47, 48, 52. [ISBN](ISBN.md) [0-201-14236-8](https://en.wikipedia.org/wiki/Special:BookSources/0-201-14236-8). <a id="^ref-11"></a>^ref-11
12. Schmidt, Maxie D. (2018). "Combinatorial identities for generalized Stirling numbers expanding _f_-factorial functions and the _f_-harmonic numbers". _Journal of Integer Sequences_. __21__ (2) 18.2.7. [arXiv](ArXiv.md):[1611.04708v2](https://arxiv.org/abs/1611.04708v2). [MR](Mathematical%20Reviews.md) [3779776](https://mathscinet.ams.org/mathscinet-getitem?mr=3779776). <a id="^ref-12"></a>^ref-12

## external links

- [Weisstein, Eric W.](Eric%20W.%20Weisstein.md) ["Pochhammer Symbol"](https://mathworld.wolfram.com/PochhammerSymbol.html). _[MathWorld](MathWorld.md)_.
