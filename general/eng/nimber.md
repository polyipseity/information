---
aliases:
  - Grundy number
  - Grundy numbers
  - nimber
  - nimbers
tags:
  - flashcard/active/general/eng/nimber
  - language/in/English
---

# nimber

- Not to be confused with {@{[Number](number.md)}@}. <!--SR:!2026-03-01,339,345-->

<!-- | ![](../../archives/Wikimedia%20Commons/Ambox%20important.svg) | hide__This article has multiple issues.__ Please help __[improve it](https://en.wikipedia.org/wiki/Special:EditPage/Nimber)__ or discuss these issues on the __[talk page](https://en.wikipedia.org/wiki/Talk:Nimber)__. _\([Learn how and when to remove these messages](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_| This article's __[lead section](https://en.wikipedia.org/wiki/Wikipedia:Manual%20of%20Style/Lead%20section) contains information that is not included elsewhere in the article__. _\(January 2019\)_ | <p>  <br/> | This article's [lead section](https://en.wikipedia.org/wiki/Wikipedia:Manual%20of%20Style/Lead%20section#Length) __may be too short to adequately [summarize](https://en.wikipedia.org/wiki/Wikipedia:Summary%20style) the key points__. _\(January 2019\)_ | | -->

In [mathematics](mathematics.md), {@{the __nimbers__, also called __Grundy numbers__}@}, are introduced in {@{[combinatorial game theory](combinatorial%20game%20theory.md)}@}, where they are {@{defined as the values of heaps in the game [Nim](Nim.md)}@}. The nimbers are {@{the [ordinal numbers](ordinal%20number.md) endowed with _nimber addition_ and _nimber multiplication_}@}, which are {@{distinct from [ordinal addition](ordinal%20arithmetic.md#addition) and [ordinal multiplication](ordinal%20arithmetic.md#multiplication)}@}. <!--SR:!2028-07-17,1013,353!2026-03-20,355,353!2026-02-27,336,345!2026-03-22,357,353!2026-03-22,357,353-->

Because of {@{the [Sprague–Grundy theorem](Sprague–Grundy%20theorem.md)}@} which {@{states that every [impartial game](impartial%20game.md) is equivalent to a Nim heap of a certain size}@}, nimbers {@{arise in a much larger class of impartial games}@}. They may also occur in {@{[partisan games](partisan%20game.md)}@} like {@{[Domineering](Domineering.md)}@}. <!--SR:!2030-05-02,1540,365!2030-05-29,1562,365!2026-03-18,353,353!2026-02-20,331,345!2029-04-10,1221,350-->

{@{The nimber addition and multiplication operations}@} are {@{associative and commutative}@}. Each nimber is {@{its own [additive inverse](additive%20inverse.md)}@}. In particular for {@{some pairs of ordinals, their nimber sum is smaller than either addend}@}.<sup>[\[1\]](#^ref-1)</sup> {@{The [minimum excludant](mex%20(mathematics).md) operation}@} is {@{applied to sets of nimbers}@}. <!--SR:!2026-02-22,333,345!2026-02-28,337,345!2027-08-08,679,325!2026-02-28,338,345!2028-11-07,1100,350!2029-04-28,1185,310-->

## uses

### Nim

- Main article: [Nim](Nim.md)

Nim is {@{a game in which two players take turns removing objects from distinct heaps}@}. As {@{moves}@} depend {@{only on the position and not on which of the two players is currently moving}@}, and where {@{the payoffs are symmetric}@}, Nim is {@{an impartial game}@}. On each turn, a player must {@{remove at least one object}@}, and may {@{remove any number of objects provided they all come from the same heap}@}. The goal of the game is {@{to be the player who removes the last object}@}. The nimber of a heap is {@{simply the number of objects in that heap}@}. Using {@{nim addition}@}, one can {@{calculate the nimber of the game as a whole}@}. The winning strategy is {@{to force the nimber of the game to 0 for the opponent's turn}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2028-11-04,1099,350!2027-12-15,779,330!2029-05-25,1256,350!2028-09-09,1054,350!2026-03-25,360,353!2029-05-03,1240,350!2027-04-29,638,325!2027-04-26,615,290!2026-03-01,339,345!2026-03-24,118,389!2026-03-23,117,389!2026-06-05,127,396-->

### Cram

- Main article: [Cram \(game\)](Cram%20(game).md)

Cram is {@{a game often played on a rectangular board}@} in which {@{players take turns placing dominoes either horizontally or vertically until no more dominoes can be placed}@}. {@{The first player that cannot make a move}@} loses. As {@{the possible moves for both players are the same}@}, it is {@{an impartial game and can have a nimber value}@}. For example, any board {@{that is an even size by an even size will have a nimber of 0}@}. Any board {@{that is even by odd will have a non-zero nimber}@}. Any {@{2 × _n_ board will have a nimber of 0 for all even _n_ and a nimber of 1 for all odd _n_}@}. <!--SR:!2026-03-24,359,353!2026-05-21,372,305!2030-05-15,1550,365!2028-01-04,857,345!2029-02-23,1185,350!2026-02-23,334,345!2026-02-19,330,345!2026-03-20,355,353-->

### Northcott's game

In {@{Northcott's game}@}, {@{<!-- pegs -->a token for each player are placed along a <!-- column -->row with a finite number of spaces}@}. Each turn each player must {@{move the piece <!-- up -->left or <!-- down -->right the column}@}, but may not {@{move past the other player's piece}@}. {@{Several <!-- columns -->rows are stacked together}@} to add complexity. {@{The player that can no longer make any moves}@} loses. Unlike {@{many other nimber related games}@}, {@{the number of spaces between the two tokens on each row}@} are {@{the sizes of the Nim heaps}@}. If your opponent {@{increases the number of spaces between two tokens}@}, just {@{decrease it on your next move}@}. Else, play {@{the game of Nim}@} and make {@{the Nim-sum of the number of spaces between the tokens on each row be 0}@}.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2026-03-18,353,353!2027-05-01,638,325!2028-03-08,842,330!2027-12-26,837,330!2029-06-02,1263,350!2028-07-05,999,353!2030-05-05,1543,365!2026-02-21,332,345!2030-04-28,1537,365!2027-04-26,634,325!2026-04-13,119,391!2026-05-05,121,393!2026-05-05,121,393-->

### Hackenbush

- Main article: [Hackenbush](Hackenbush.md)

Hackenbush is {@{a game invented by mathematician [John Horton Conway](John%20Horton%20Conway.md)}@}. It may be played on {@{any configuration of colored [line segments](line%20segment.md) connected to one another by their endpoints and to a "ground" line}@}. Players {@{take turns removing line segments}@}. {@{An impartial game version, thereby a game able to be analyzed using nimbers}@}, can be found by {@{removing distinction from the lines, allowing either player to cut any branch}@}. {@{Any segments reliant on the newly removed segment in order to connect to the ground line}@} are removed as well. In this way, {@{each connection to the ground can be considered a nim heap with a nimber value}@}. Additionally, {@{all the separate connections to the ground line}@} can {@{also be summed for a nimber of the game state}@}. <!--SR:!2026-03-19,354,353!2028-04-10,928,345!2029-02-02,1169,350!2028-04-16,932,345!2029-08-02,1306,350!2026-03-21,356,353!2029-05-11,1246,350!2030-04-21,1530,365!2027-06-27,697,330-->

## addition

{@{Nimber addition \(also known as __nim-addition__\)}@} can be used to {@{calculate the size of a single nim heap equivalent to a collection of nim heaps}@}. It is defined {@{recursively by $$\alpha \oplus \beta =\operatorname {mex} \!{\bigl (}\{\alpha '\oplus \beta :\alpha '<\alpha \}\cup \{\alpha \oplus \beta ':\beta '<\beta \}{\bigr )},$$}@} (annotation: Selecting $\alpha' < \alpha$ or $\beta' < \beta$ {@{can be interpreted as making a move from either $\alpha$ to $\alpha'$ or $\beta$ to $\beta'$}@}.) where {@{the [minimum excludant](mex%20(mathematics).md) mex\(_S_\) of a set _S_ of ordinals is defined to be the smallest ordinal that is _not_ an element of _S_}@}. <!--SR:!2026-03-21,356,353!2026-03-19,354,353!2029-07-05,1278,350!2026-03-05,342,345!2027-09-06,742,333-->

For {@{finite ordinals}@}, {@{the __nim-sum__ is easily evaluated on a computer}@} by {@{taking the [bitwise](bitwise%20operation.md) [exclusive or](exclusive%20or.md) \(XOR, denoted by ⊕\) of the corresponding numbers}@}. For example, the nim-sum of 7 and 14 {@{can be found by writing 7 as 111 and 14 as 1110}@}; the ones place {@{adds to 1}@}; the twos place {@{adds to 2, which we replace with 0}@}; the fours place {@{adds to 2, which we replace with 0}@}; the eights place {@{adds to 1}@}. So {@{the nim-sum is written in binary as 1001, or in decimal as 9}@}. <!--SR:!2030-04-22,1532,365!2027-03-31,624,333!2028-07-14,1007,353!2029-02-18,1181,350!2028-06-03,903,330!2027-12-10,824,330!2026-05-27,120,396!2026-06-05,127,396!2026-06-06,128,396-->

{@{This property of addition}@} follows from the fact that {@{both mex and XOR yield a winning strategy for Nim}@} and there {@{can be only one such strategy}@}; or it can be {@{shown directly by induction}@}: Let {@{_α_ and _β_ be two finite ordinals}@}, and assume that {@{the nim-sum of all pairs with one of them reduced is already defined}@}. The only number {@{whose XOR with _α_ is _α_ ⊕ _β_ is _β_, and vice versa}@}; thus {@{_α_ ⊕ _β_ is excluded \(annotation: see the definition of nimber addition above\)}@}. {@{$$\zeta :=\alpha \oplus \beta \oplus \gamma$$}@} On the other hand, for {@{any ordinal _γ_ \< _α_ ⊕ _β_}@}, \(annotation: This is trying to {@{prove that _α_ ⊕ _β_ is the mex}@}.\) {@{XORing _ξ_ with all of _α_, _β_ and _γ_}@} must lead to {@{a reduction for one of them}@} \(since {@{the leading 1 in _ξ_}@} must be {@{present in at least one of the three}@}\); since {@{$$\zeta \oplus \gamma =\alpha \oplus \beta >\gamma ,$$}@} (annotation: In words, it means {@{XORing _ξ_ with _γ_ must increase _γ_}@}, thus {@{XORing _ξ_ with all of _a_ and _β_ decrease either _a_ or _β_}@}.) we must have {@{either $${\begin{aligned}\alpha >\zeta \oplus \alpha &=\beta \oplus \gamma ,\\[4pt]\beta >\zeta \oplus \beta &=\alpha \oplus \gamma ;\end{aligned} }$$}@} thus {@{_γ_ is included \(annotation: see the definition of nimber addition above\)}@} as {@{either $${\begin{aligned}\alpha \oplus \beta & > \gamma = (\beta \oplus \gamma )\oplus \beta = (\zeta \oplus \alpha) \oplus \beta ,\\[4pt] \alpha \oplus \beta & > \gamma = \alpha \oplus (\alpha \oplus \gamma ) = \alpha \oplus (\zeta \oplus \beta) ;\end{aligned} }$$}@} and hence {@{_α_ ⊕ _β_ is the minimum excluded ordinal}@}. <!--SR:!2026-03-18,353,353!2026-08-25,404,290!2030-05-26,1560,365!2027-03-18,624,333!2026-03-26,330,290!2029-02-07,1173,350!2026-09-18,475,310!2026-03-23,358,353!2028-11-14,1106,350!2029-08-31,1329,350!2029-01-27,1166,350!2026-03-06,343,345!2028-05-03,881,330!2026-10-31,507,310!2028-06-15,893,290!2026-06-25,400,305!2026-03-19,354,353!2026-10-05,251,371!2026-04-19,124,391!2026-05-05,121,393!2026-03-28,83,373!2026-05-10,126,393-->

{@{Nimber addition}@} is {@{[associative](associative%20property.md) and [commutative](commutative%20property.md), with 0 as the additive [identity element](identity%20element.md)}@}. Moreover, {@{a nimber is its own [additive inverse](additive%20inverse.md)}@}.<sup>[\[4\]](#^ref-4)</sup> It follows that {@{_α_ ⊕ _β_ = 0 [if and only if](if%20and%20only%20if.md) _α_ = _β_}@}. <!--SR:!2026-11-16,519,310!2029-07-26,1299,350!2029-03-23,1193,353!2030-05-04,1542,365-->

## multiplication

{@{Nimber multiplication \(__nim-multiplication__\)}@} is defined {@{recursively by $$\alpha \,\beta =\operatorname {mex} \!{\bigl (}\{\alpha '\beta \oplus \alpha \,\beta '\oplus \alpha '\beta ':\alpha '<\alpha ,\beta '<\beta \}{\bigr )}.$$}@} <!--SR:!2026-03-01,339,345!2027-12-10,780,290-->

Nimber multiplication is {@{associative and commutative, with the ordinal 1 as the multiplicative [identity element](identity%20element.md)}@}. Moreover, {@{nimber multiplication [distributes over](distributive%20property.md) nimber addition}@}.<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2030-05-03,1541,365!2028-12-15,1131,350-->

Thus, except for {@{the fact that nimbers form a [proper class](class%20(set%20theory).md) and not a set}@}, {@{the class of nimbers forms a [ring](ring%20(mathematics).md)}@}. In fact, it {@{even determines an [algebraically closed field](algebraically%20closed%20field.md) of [characteristic](characteristic%20(algebra).md) 2}@}, with {@{the nimber multiplicative inverse of a nonzero ordinal _α_ given}@} by {@{$$\alpha ^{-1}=\operatorname {mex} (S),$$}@} where {@{_S_ is the smallest set of ordinals \(nimbers\)}@} such that <!--SR:!2026-02-27,337,345!2029-04-28,1181,310!2028-09-27,1067,350!2028-07-21,929,330!2026-12-17,540,330!2028-07-16,1008,353-->

1. mex(_S_), base ::@:: 0 is an element of _S_; <!--SR:!2027-09-09,743,330!2026-02-22,333,345-->
2. mex(_S_), induction ::@:: if 0 \< _α_<!-- markdown separator -->′ \< _α_ and _β'_ is an element of _S_, then ${\tfrac {1+(\alpha '\oplus \alpha )\beta '}{\alpha '} }$ is also an element of _S_. <!--SR:!2027-08-07,580,245!2027-09-22,595,250-->

For {@{all natural numbers _n_}@}, {@{the set of nimbers less than 2<sup>2<sup>_n_</sup></sup>}@} form {@{the [Galois field](finite%20field.md) GF\(2<sup>2<sup>_n_</sup></sup>\) of order 2<sup>2<sup>_n_</sup></sup>}@}. (TODO: What is this abstract nonsense?) Therefore, {@{the set of finite nimbers}@} is {@{isomorphic to the [direct limit](direct%20limit.md) as _n_ → ∞ of the fields GF\(2<sup>2<sup>_n_</sup></sup>\)}@}. This subfield is {@{not algebraically closed}@}, since {@{no field GF\(2<sup>_k_</sup>\) with _k_ not a power of 2 is contained in any of those fields, and therefore not in their direct limit}@}; for instance {@{the polynomial _x_<sup>3</sup> + _x_ + 1}@}, which {@{has a root in GF\(2<sup>3</sup>\)}@}, {@{does not have a root in the set of finite nimbers}@}. <!--SR:!2027-05-11,649,325!2029-01-19,1159,350!2026-02-18,330,345!2029-04-05,1217,350!2028-01-01,792,333!2028-12-23,1138,350!2027-01-14,515,313!2029-07-22,1295,350!2026-05-10,367,305!2026-03-02,339,345-->

Just as {@{in the case of nimber addition}@}, there is {@{a means of computing the nimber product of finite ordinals}@}. This is determined by the rules that <!--SR:!2026-03-01,339,345!2029-07-07,1280,350-->

1. The nimber product of a Fermat 2-power \(numbers of the form 2<sup>2<sup>_n_</sup></sup>\) with a smaller number ::@:: is equal to their ordinary product; <!--SR:!2027-05-12,648,325!2026-03-01,338,345-->
2. The nimber square of a Fermat 2-power _x_ \(annotation: numbers of the form 2<sup>2<sup>_n_</sup></sup>\) ::@:: is equal to 3<!-- markdown separator -->_x_/2 as evaluated under the ordinary multiplication of natural numbers. <!--SR:!2027-07-10,605,265!2027-01-15,516,313-->

{@{The smallest algebraically closed field of nimbers}@} is {@{the set of nimbers less than the ordinal _ω<sup>ω<sup>ω</sup></sup>_, where _ω_ is the smallest infinite ordinal}@}. It follows that {@{as a nimber, _ω<sup>ω<sup>ω</sup></sup>_ is [transcendental](transcendental%20number.md) over the field}@}.<sup>[\[5\]](#^ref-5)</sup> <!--SR:!2030-05-16,1551,365!2027-10-14,770,330!2027-11-02,743,290-->

> [!tip] tips
>
> - game theoretic interpretation ::@:: Unfortunately, there are no good game theoretic interpretations to _nim-multiplication_, unlike _nim-addition_ (which has the interpretation of combining two games). <p> Rather, it is best understood using abstract algebra. Nim-multiplication is an operation defined with respect to nim-addition in the same way as ordinary multiplication as an operation defined with respect to ordinary addition. <!--SR:!2026-03-03,345,357!2030-05-30,1578,377-->

## addition and multiplication tables

The following tables exhibit {@{addition and multiplication among the first 16 nimbers}@}. <!--SR:!2027-06-05,684,330-->

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD059 -->

This subset is {@{closed under both operations}@}, since {@{16 is of the form 2<sup>2<sup>_n_</sup></sup>}@}. \(If you prefer simple text tables, they are [here](https://en.wikipedia.org/w/index.php?title=Nimber&oldid=383699838).\) <!--SR:!2029-01-04,1148,350!2030-05-28,1562,365-->

<!-- markdownlint-restore -->

> {@{![nimber addition table among the first 16 nimbers](../../archives/Wikimedia%20Commons/Z2%5E4;%20Cayley%20table;%20binary.svg)}@}
>
> {@{Nimber addition}@} \(sequence {@{[A003987](https://oeis.org/A003987)}@} in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)\) <br/>
> This is also {@{the [Cayley table](cayley%20table.md) of [Z<sub>2</sub><sup>4</sup>](list%20of%20small%20groups.md#list%20of%20small%20abelian%20groups) – or the table of [bitwise](bitwise%20operation.md) [XOR](exclusive%20or.md) operations}@}. <br/>
> The small matrices show {@{the single digits of the binary numbers}@}. <!--SR:!2028-07-15,968,313!2029-02-16,1181,350!2027-10-01,657,285!2029-03-22,1193,353!2027-05-03,642,325-->

<!-- markdownlint MD028 -->

> {@{![nimber multiplication table among the first 16 nimbers](../../archives/Wikimedia%20Commons/Nimbers%200...15%20multiplication.svg)}@}
>
> {@{Nimber multiplication}@} \(sequence {@{[A051775](https://oeis.org/A051775)}@} in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)\) <br/>
> The nonzero elements form the [Cayley table](cayley%20table.md) of [Z<sub>15</sub>](list%20of%20small%20groups.md#list%20of%20small%20abelian%20groups). <br/>
> The small matrices are permuted binary [Walsh matrices](walsh%20matrix.md). <!--SR:!2027-01-14,551,310!2028-08-27,1042,350!2026-04-26,210,185-->

<!-- markdownlint MD028 -->

> {@{![nimber multiplication table among powers of two](../../archives/Wikimedia%20Commons/Nimber%20products%20of%20powers%20of%20two.svg)}@}
>
> {@{Nimber multiplication of [powers of two](power%20of%20two.md)}@} \(sequence {@{[A223541](https://oeis.org/A223541)}@} in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)\) <br/>
> {@{Calculating the nim-products of powers of two}@} is {@{a decisive point in the recursive algorithm of nimber-multiplication}@}. <!--SR:!2027-11-24,763,333!2026-12-12,528,310!2026-04-17,260,213!2027-10-14,794,345!2027-08-19,728,333-->

## see also

- [Surreal number](surreal%20number.md)

## notes

1. _Advances in computer games : 14th International Conference, ACG 2015, Leiden, the Netherlands, July 1-3, 2015, Revised selected papers_. Herik, Jaap van den,, Plaat, Aske,, Kosters, Walter. Cham. 2015-12-24. [ISBN](ISBN.md) [978-3319279923](https://en.wikipedia.org/wiki/Special:BookSources/978-3319279923). [OCLC](OCLC.md#OCLC) [933627646](https://search.worldcat.org/oclc/933627646). <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFAnany.2012"></a> Anany., Levitin \(2012\). _Introduction to the design & analysis of algorithms_ \(3rd ed.\). Boston: Pearson. [ISBN](ISBN.md) [9780132316811](https://en.wikipedia.org/wiki/Special:BookSources/9780132316811). [OCLC](OCLC.md#OCLC) [743298766](https://search.worldcat.org/oclc/743298766). <a id="^ref-2"></a>^ref-2
3. ["Theory of Impartial Games"](http://web.mit.edu/sp.268/www/nim.pdf) \(PDF\). Feb 3, 2009. <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFBrownGuy2021"></a> [Brown, Ezra](Ezra%20Brown.md); [Guy, Richard K.](Richard%20K.%20Guy.md) \(2021\). "2.5 Nim arithmetic and Nim algebra". _The Unity of Combinatorics_. Vol. 36 of The Carus Mathematical Monographs \(reprint ed.\). [American Mathematical Society](American%20Mathematical%20Society.md). p. 35. [ISBN](ISBN.md) [978-1-4704-6509-4](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4704-6509-4). <a id="^ref-4"></a>^ref-4
5. Conway 1976, p. 61. <a id="^ref-5"></a>^ref-5

## references

This text incorporates [content](https://en.wikipedia.org/wiki/nimber) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFConway1976"></a> [Conway, John Horton](John%20Horton%20Conway.md) \(1976\). [_On Numbers and Games_](On%20Numbers%20and%20Games.md). [Academic Press](Academic%20Press.md) Inc. \(London\) Ltd.
- <a id="CITEREFLenstra1978"></a> [Lenstra, H. W.](Hendrik%20Lenstra.md) \(1978\). _Nim multiplication_. Report IHES/M/78/211. Institut des hautes études scientifiques. [hdl](Handle%20System.md):[1887/2125](https://hdl.handle.net/1887%2F2125).
- <a id="CITEREFSchleicherStoll2004"></a> Schleicher, Dierk; Stoll, Michael \(2004\). "An Introduction to Conway's Games and Numbers". [arXiv](ArXiv.md):[math.DO/0410026](https://arxiv.org/abs/math.DO/0410026). which discusses games, [surreal numbers](surreal%20number.md), and nimbers.

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Combinatorial game theory](https://en.wikipedia.org/wiki/Category:Combinatorial%20game%20theory)
> - [Finite fields](https://en.wikipedia.org/wiki/Category:Finite%20fields)
> - [Ordinal numbers](https://en.wikipedia.org/wiki/Category:Ordinal%20numbers)
