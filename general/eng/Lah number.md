---
aliases:
  - Lah number
  - Lah numbers
  - Stirling number of the 3rd kind
  - Stirling number of the third kind
  - Stirling numbers of the 3rd kind
  - Stirling numbers of the third kind
  - signed Lah number
  - signed Lah numbers
  - signed Stirling number of the 3rd kind
  - signed Stirling number of the third kind
  - signed Stirling numbers of the 3rd kind
  - signed Stirling numbers of the third kind
  - unsigned Lah number
  - unsigned Lah numbers
  - unsigned Stirling number of the 3rd kind
  - unsigned Stirling number of the third kind
  - unsigned Stirling numbers of the 3rd kind
  - unsigned Stirling numbers of the third kind
tags:
  - flashcard/active/general/eng/Lah_number
  - language/in/English
---

# Lah number

In [mathematics](mathematics.md), the __(signed and unsigned) Lah numbers__ are {@{[coefficients](coefficient.md) expressing [rising factorials](falling%20and%20rising%20factorials.md) in terms of [falling factorials](falling%20and%20rising%20factorials.md) and vice versa}@}. They were discovered by {@{[Ivo Lah](Ivo%20Lah.md) in 1954}@}.<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup> Explicitly, {@{the unsigned Lah numbers $L(n,k)$}@} are given by {@{the formula involving the [binomial coefficient](binomial%20coefficient.md) $$L(n,k)={n-1 \choose k-1}{\frac {n!}{k!} }$$ for $n\geq k\geq 1$}@}. <!--SR:!2025-09-12,227,310!2025-03-29,109,290!2025-12-01,308,330!2025-11-30,307,330-->

{@{Unsigned Lah numbers}@} have {@{an interesting meaning in [combinatorics](combinatorics.md)}@}: they {@{count the number of ways a [set](set%20(mathematics).md) of _n_ elements can be [partitioned](partition%20of%20a%20set.md) into _k_ nonempty linearly ordered [subsets](subset.md)}@}.<sup>[\[3\]](#^ref-3)</sup> Lah numbers are related to [Stirling numbers](Stirling%20number.md).<sup>[\[4\]](#^ref-4)</sup> (annotation: Indeed, there is a combinatorial way to interpret the formula for Lah numbers. First, {@{_n_! counts the number of ways to order _n_ items. Then, $\binom {n - 1} {k - 1}$ counts the number of ways to insert _k_ − 1 "walls" in between the _n_ items (_n_ − 1 slots) to make _k_ nonempty labelled partitions. Finally, dividing by _k_! makes the partitions unlabeled}@}.) <!--SR:!2025-08-13,203,310!2025-12-03,310,330!2025-05-25,157,310!2025-12-06,312,330-->

For {@{$n\geq 1$, the Lah number $L(n,1)$}@} is equal to {@{the [factorial](factorial.md) $n!$ in the interpretation above}@}, the only partition of {@{$\{1,2,3\}$ into 1 set can have its set ordered in 6 ways: $$\{(1,2,3)\},\{(1,3,2)\},\{(2,1,3)\},\{(2,3,1)\},\{(3,1,2)\},\{(3,2,1)\} \,.$$}@} {@{$L(3,2)$}@} is equal to {@{6, because there are six partitions of $\{1,2,3\}$ into two ordered parts: $$\{1,(2,3)\},\{1,(3,2)\},\{2,(1,3)\},\{2,(3,1)\},\{3,(1,2)\},\{3,(2,1)\} \,$$}@} {@{$L(n,n)$}@} is {@{always 1 because the only way to partition $\{1,2,\ldots ,n\}$ into $n$ non-empty subsets results in subsets of size 1, that can only be permuted in one way}@}. In {@{the more recent literature}@},<sup>[\[5\]](#^ref-5)</sup><sup>[\[6\]](#^ref-6)</sup> {@{[Karamata](Jovan%20Karamata.md)–[Knuth](Donald%20Knuth.md) style notation}@} has taken over. Lah numbers are now often {@{written as $$L(n,k)=\left\lfloor {n \atop k}\right\rfloor \,.$$}@} <!--SR:!2025-11-28,306,330!2025-12-06,312,330!2025-11-29,307,330!2025-12-02,309,330!2025-05-29,144,290!2025-12-10,316,330!2025-12-07,313,330!2025-12-03,310,330!2025-12-05,312,330!2025-11-23,302,330-->

## table of values

Below is a table of values for the Lah numbers:

| ___n___\\___k___ | __0__ | __1__   | __2__    | __3__    | __4__    | __5__   | __6__  | __7__ | __8__ | __9__ | __10__ |
|:----------------:| -----:| -------:| --------:| --------:| --------:| -------:| ------:| -----:| -----:| -----:| ------:|
| __0__            | 1     |         |          |          |          |         |        |       |       |       |        |
| __1__            | 0     | 1       |          |          |          |         |        |       |       |       |        |
| __2__            | 0     | 2       | 1        |          |          |         |        |       |       |       |        |
| __3__            | 0     | 6       | 6        | 1        |          |         |        |       |       |       |        |
| __4__            | 0     | 24      | 36       | 12       | 1        |         |        |       |       |       |        |
| __5__            | 0     | 120     | 240      | 120      | 20       | 1       |        |       |       |       |        |
| __6__            | 0     | 720     | 1800     | 1200     | 300      | 30      | 1      |       |       |       |        |
| __7__            | 0     | 5040    | 15120    | 12600    | 4200     | 630     | 42     | 1     |       |       |        |
| __8__            | 0     | 40320   | 141120   | 141120   | 58800    | 11760   | 1176   | 56    | 1     |       |        |
| __9__            | 0     | 362880  | 1451520  | 1693440  | 846720   | 211680  | 28224  | 2016  | 72    | 1     |        |
| __10__           | 0     | 3628800 | 16329600 | 21772800 | 12700800 | 3810240 | 635040 | 60480 | 3240  | 90    | 1      |

The row sums are $1,1,3,13,73,501,4051,37633,\dots$ (sequence [A000262](https://oeis.org/A000262) in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)).

## rising and falling factorials

Let {@{$x^{(n)}$ represent the [rising factorial](falling%20and%20rising%20factorials.md) $x(x+1)(x+2)\cdots (x+n-1)$ and let $(x)_{n}$ represent the [falling factorial](falling%20and%20rising%20factorials.md) $x(x-1)(x-2)\cdots (x-n+1)$}@}. The Lah numbers are {@{the coefficients that express each of these families of polynomials in terms of the other}@}. Explicitly, {@{$$x^{(n)}=\sum _{k=0}^{n}L(n,k)(x)_{k}$$and$$(x)_{n}=\sum _{k=0}^{n}(-1)^{n-k}L(n,k)x^{(k)}.$$}@} (annotation: The change of basis to the falling factorials uses {@{unsigned while that to the rising factorials uses signed}@}.) <!--SR:!2025-11-24,303,330!2025-12-10,316,330!2025-11-04,285,330!2025-09-13,228,310-->

For example, {@{$$x(x+1)(x+2)={\color {red}6}x+{\color {red}6}x(x-1)+{\color {red}1}x(x-1)(x-2)$$and$$x(x-1)(x-2)={\color {red}6}x-{\color {red}6}x(x+1)+{\color {red}1}x(x+1)(x+2),$$}@} where {@{the coefficients 6, 6, and 1 are exactly the Lah numbers $L(3,1)$, $L(3,2)$, and $L(3,3)$}@}. <!--SR:!2026-01-03,309,290!2025-12-04,311,330-->

## identities and relations

The Lah numbers {@{satisfy a variety of identities and relations}@}. <!--SR:!2025-11-14,294,330-->

In [Karamata](Jovan%20Karamata.md)–[Knuth](Donald%20Knuth.md) notation for [Stirling numbers](Stirling%20number.md) {@{$$L(n,k)=\sum _{j=k}^{n}\left[{n \atop j}\right]\left\{ {j \atop k}\right\}$$}@} where {@{$\left[{n \atop j}\right]$ are the [Stirling numbers of the first kind](Stirling%20numbers%20of%20the%20first%20kind.md) and $\left\{ {j \atop k}\right\}$ are the [Stirling numbers of the second kind](stirling%20numbers%20of%20the%20second%20kind.md)}@}. <!--SR:!2025-05-16,133,290!2025-11-07,288,330-->

- alternative ways to write the formula ::@::  $$L(n,k)={n-1 \choose k-1}{\frac {n!}{k!} }={n \choose k}{\frac {(n-1)!}{(k-1)!} }={n \choose k}{n-1 \choose k-1}(n-k)!$$ <!--SR:!2025-11-25,252,270!2025-08-28,215,310-->
- formula with square ::@:: $$L(n,k)={\frac {n!(n-1)!}{k!(k-1)!} }\cdot {\frac {1}{(n-k)!} }=\left({\frac {n!}{k!} }\right)^{2}{\frac {k}{n(n-k)!} }$$ <!--SR:!2025-03-26,97,270!2025-05-25,141,290-->
- recurrence formula derivation ::@:: $$k(k+1)L(n,k+1)=(n-k)L(n,k)$$, for $k>0$. <!--SR:!2025-06-26,134,230!2025-04-17,127,290-->

### recurrence relations

The Lah numbers satisfy {@{the recurrence relations $${\begin{aligned}L(n+1,k)&=(n+k)L(n,k)+L(n,k-1)\\&=k(k+1)L(n,k+1)+2kL(n,k)+L(n,k-1)\end{aligned} }$$}@} (annotation: The above can be derived combinatorically by {@{using the method of distinguished element}@}.) where {@{$L(n,0)=\delta _{n}$, the [Kronecker delta](kronecker%20delta.md), and $L(n,k)=0$ for all $k>n$}@}. <!--SR:!2025-11-19,252,270!2025-11-29,307,330!2025-12-04,311,330-->

### exponential generating function

- exponential generating function for fixed _k_ ::@:: $$\sum_{n\geq k}L(n,k){\frac {x^{n} }{n!} }={\frac {1}{k!} }\left({\frac {x}{1-x} }\right)^{k}$$ <!--SR:!2025-04-18,64,230!2025-06-19,134,230-->

### derivative of exp(1/_x_)

{@{The _n_-th [derivative](derivative.md) (including _n_ = 0) of the function $e^{\frac {1}{x} }$}@} can be {@{expressed with the Lah numbers}@}, as follows<sup>[\[7\]](#^ref-7)</sup> {@{$${\frac { {\textrm {d} }^{n} }{ {\textrm {d} }x^{n} } }e^{\frac {1}{x} }=(-x)^{-n}\sum _{k=0}^{n}{\frac {L(n,k)}{x^{k} } }\cdot e^{\frac {1}{x} }.$$}@} <!--SR:!2025-06-03,151,290!2025-03-19,92,270!2025-03-23,85,230-->

For example, $$\begin{aligned} {\frac {\textrm {d} }{ {\textrm {d} }x} }e^{\frac {1}{x} } & = -{\frac {1}{x^{2} } }\cdot e^{\frac {1}{x} } \\ {\frac { {\textrm {d} }^{2} }{ {\textrm {d} }x^{2} } }e^{\frac {1}{x} } & = {\frac {\textrm {d} }{ {\textrm {d} }x} }\left(-{\frac {1}{x^{2} } }e^{\frac {1}{x} }\right)=-{\frac {-2}{x^{3} } }\cdot e^{\frac {1}{x} }-{\frac {1}{x^{2} } }\cdot {\frac {-1}{x^{2} } }\cdot e^{\frac {1}{x} }=\left({\frac {2}{x^{3} } }+{\frac {1}{x^{4} } }\right)\cdot e^{\frac {1}{x} } \\ {\frac { {\textrm {d} }^{3} }{ {\textrm {d} }x^{3} } }e^{\frac {1}{x} } & ={\frac {\textrm {d} }{ {\textrm {d} }x} }\left(\left({\frac {2}{x^{3} } }+{\frac {1}{x^{4} } }\right)\cdot e^{\frac {1}{x} }\right)=\left({\frac {-6}{x^{4} } }+{\frac {-4}{x^{5} } }\right)\cdot e^{\frac {1}{x} }+\left({\frac {2}{x^{3} } }+{\frac {1}{x^{4} } }\right)\cdot {\frac {-1}{x^{2} } }\cdot e^{\frac {1}{x} }=-\left({\frac {6}{x^{4} } }+{\frac {6}{x^{5} } }+{\frac {1}{x^{6} } }\right)\cdot e^{\frac {1}{x} } \,. \end{aligned}$$

## link to Laguerre polynomials

{@{Generalized [Laguerre polynomials](Laguerre%20polynomials.md) $L_{n}^{(\alpha )}(x)$}@} are {@{linked to Lah numbers upon setting $\alpha =-1$}@} {@{$$n!L_{n}^{(-1)}(x)=\sum_{k=0}^{n}L(n,k)(-x)^{k}$$}@} This formula is {@{the default [Laguerre polynomial](Laguerre%20polynomials.md) in [umbral calculus](umbral%20calculus.md) convention}@}.<sup>[\[8\]](#^ref-8)</sup> <!--SR:!2025-04-12,114,290!2025-09-03,198,270!2025-03-19,82,230!2025-09-04,220,310-->

## practical application

In recent years, Lah numbers have been used {@{in [steganography](steganography.md) for hiding data in images}@}. Compared to {@{alternatives such as [DCT](discrete%20cosine%20transform.md), [DFT](discrete%20Fourier%20transform.md) and [DWT](discrete%20wavelet%20transform.md)}@}, it has {@{lower complexity of calculation—$O(n\log n)$—of their integer coefficients}@}.<sup>[\[9\]](#^ref-9)</sup><sup>[\[10\]](#^ref-10)</sup> {@{The Lah and Laguerre transforms}@} naturally arise in {@{the perturbative description of the [chromatic dispersion](dispersion%20(optics).md)}@}.<sup>[\[11\]](#^ref-11)</sup><sup>[\[12\]](#^ref-12)</sup> In Lah-Laguerre optics, such an approach tremendously speeds up optimization problems. <!--SR:!2025-12-07,313,330!2025-12-08,314,330!2025-11-23,302,330!2025-08-21,209,310!2025-12-09,315,330-->

## see also

- [Stirling numbers](Stirling%20number.md)
- [Pascal matrix](Pascal%20matrix.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Lah_number) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Lah, Ivo (1954). "A new kind of numbers and its application in the actuarial mathematics". _Boletim do Instituto dos Actuários Portugueses_. __9__: 7–15. <a id="^ref-1"></a>^ref-1
2. [John Riordan, _Introduction to Combinatorial Analysis_](https://books.google.com/books?id=zWgIPlds29UC), Princeton University Press (1958, reissue 1980) [ISBN](ISBN.md) [978-0-691-02365-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-691-02365-6) (reprinted again in 2002 by Dover Publications). <a id="^ref-2"></a>^ref-2
3. Petkovsek, Marko; Pisanski, Tomaz (Fall 2007). "Combinatorial Interpretation of Unsigned Stirling and Lah Numbers". _Pi Mu Epsilon Journal_. __12__ (7): 417–424. [JSTOR](JSTOR.md) [24340704](https://www.jstor.org/stable/24340704). <a id="^ref-3"></a>^ref-3
4. Comtet, Louis (1974). [_Advanced Combinatorics_](https://archive.org/details/Comtet_Louis_-_Advanced_Coatorics). Dordrecht, Holland: Reidel. p. [156](https://archive.org/details/Comtet_Louis_-_Advanced_Coatorics/page/n83). [ISBN](ISBN.md) [9789027703804](https://en.wikipedia.org/wiki/Special:BookSources/9789027703804). <a id="^ref-4"></a>^ref-4
5. Shattuck, Mark (2014). "Generalized r-Lah numbers". [arXiv](ArXiv.md):[1412.8721](https://arxiv.org/abs/1412.8721) [[math.CO](https://arxiv.org/archive/math.CO)]. <a id="^ref-5"></a>^ref-5
6. Nyul, Gábor; Rácz, Gabriella (2015-10-06). ["The r-Lah numbers"](https://www.sciencedirect.com/science/article/pii/S0012365X14001241). _Discrete Mathematics_. Seventh Czech-Slovak International Symposium on Graph Theory, Combinatorics, Algorithms and Applications, Košice 2013. __338__ (10): 1660–1666. [doi](digital%20object%20identifier.md):[10.1016/j.disc.2014.03.029](https://doi.org/10.1016%2Fj.disc.2014.03.029). [hdl](Handle%20System.md):[2437/213886](https://hdl.handle.net/2437%2F213886). [ISSN](ISSN.md) [0012-365X](https://search.worldcat.org/issn/0012-365X). <a id="^ref-6"></a>^ref-6
7. Daboul, Siad; Mangaldan, Jan; Spivey, Michael Z.; Taylor, Peter J. (2013). "The Lah Numbers and the nth Derivative of $e^{1 \over x}$". _Mathematics Magazine_. __86__ (1): 39–47. [doi](digital%20object%20identifier.md):[10.4169/math.mag.86.1.039](https://doi.org/10.4169%2Fmath.mag.86.1.039). [JSTOR](JSTOR.md) [10.4169/math.mag.86.1.039](https://www.jstor.org/stable/10.4169/math.mag.86.1.039). [S2CID](Semantic%20Scholar.md#S2CID) [123113404](https://api.semanticscholar.org/CorpusID:123113404). <a id="^ref-7"></a>^ref-7
8. Rota, Gian-Carlo; Kahaner, D; Odlyzko, A (1973-06-01). ["On the foundations of combinatorial theory. VIII. Finite operator calculus"](https://doi.org/10.1016%2F0022-247X%2873%2990172-8). _Journal of Mathematical Analysis and Applications_. __42__ (3): 684–760. [doi](digital%20object%20identifier.md):[10.1016/0022-247X(73)90172-8](https://doi.org/10.1016%2F0022-247X%2873%2990172-8). [ISSN](ISSN.md) [0022-247X](https://search.worldcat.org/issn/0022-247X). <a id="^ref-8"></a>^ref-8
9. Ghosal, Sudipta Kr; Mukhopadhyay, Souradeep; Hossain, Sabbir; Sarkar, Ram (2020). "Application of Lah Transform for Security and Privacy of Data through Information Hiding in Telecommunication". _Transactions on Emerging Telecommunications Technologies_. __32__ (2). [doi](digital%20object%20identifier.md):[10.1002/ett.3984](https://doi.org/10.1002%2Fett.3984). [S2CID](Semantic%20Scholar.md#S2CID) [225866797](https://api.semanticscholar.org/CorpusID:225866797). <a id="^ref-9"></a>^ref-9
10. ["Image Steganography-using-Lah-Transform"](https://in.mathworks.com/matlabcentral/fileexchange/78751-image-steganography-using-lah-transform). _MathWorks_. 5 June 2020. <a id="^ref-10"></a>^ref-10
11. Popmintchev, Dimitar; Wang, Siyang; Xiaoshi, Zhang; Stoev, Ventzislav; Popmintchev, Tenio (2022-10-24). ["Analytical Lah-Laguerre optical formalism for perturbative chromatic dispersion"](https://doi.org/10.1364%2FOE.457139). _[Optics Express](Optics%20Express.md)_. __30__ (22): 40779–40808. [Bibcode](bibcode.md):[2022OExpr..3040779P](https://ui.adsabs.harvard.edu/abs/2022OExpr..3040779P). [doi](digital%20object%20identifier.md):[10.1364/OE.457139](https://doi.org/10.1364%2FOE.457139). [PMID](PubMed.md#PubMed%20identifier) [36299007](https://pubmed.ncbi.nlm.nih.gov/36299007). <a id="^ref-11"></a>^ref-11
12. Popmintchev, Dimitar; Wang, Siyang; Xiaoshi, Zhang; Stoev, Ventzislav; Popmintchev, Tenio (2020-08-30). "Theory of the Chromatic Dispersion, Revisited". [arXiv](ArXiv.md):[2011.00066](https://arxiv.org/abs/2011.00066) [[physics.optics](https://arxiv.org/archive/physics.optics)]. <a id="^ref-12"></a>^ref-12

## external links

- The signed and unsigned Lah numbers are respectively (sequence [A008297](https://oeis.org/A008297) in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)) and (sequence [A105278](https://oeis.org/A105278) in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md))
