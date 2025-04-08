---
aliases:
  - canonical projection
  - canonical projections
  - product
  - product (category theory)
  - product of morphism
  - product of morphisms
  - products
  - products (category theory)
  - products of morphism
  - products of morphisms
  - projection morphism
  - projection morphisms
tags:
  - flashcard/active/general/eng/product__category_theory_
  - language/in/English
---

# product

- Not to be confused with {@{[Product category](product%20category.md)}@}. <!--SR:!2026-01-01,269,330-->

In {@{[category theory](category%20theory.md)}@}, {@{the __product__ of two \(or more\) [objects](object%20(category%20theory).md) in a [category](category%20(mathematics).md)}@} is {@{a notion designed to capture the essence behind constructions in other areas of [mathematics](mathematics.md)}@} such as {@{the [Cartesian product](Cartesian%20product.md) of [sets](set%20(mathematics).md), the [direct product](direct%20product.md) of [groups](group%20(mathematics).md) or [rings](ring%20(mathematics).md), and the [product](product%20topology.md) of [topological spaces](topological%20space.md)}@}. Essentially, {@{the product of a [family](indexed%20family.md) of objects}@} is {@{the "most general" object which admits a [morphism](morphism.md) to each of the given objects}@}. <!--SR:!2026-01-19,286,330!2025-12-08,254,330!2025-10-08,189,310!2025-10-30,205,310!2025-04-09,67,310!2025-08-31,172,310-->

## definition

### product of two objects

Fix {@{a category $C$}@}. Let {@{$X_{1}$ and $X_{2}$ be objects of $C$}@}. {@{A product of $X_{1}$ and $X_{2}$}@} is {@{an object $X$, typically denoted $X_{1}\times X_{2}$}@}, {@{equipped with a pair of morphisms $\pi _{1}:X\to X_{1}$, $\pi _{2}:X\to X_{2}$ satisfying the following [universal property](universal%20property.md)}@}: <!--SR:!2025-12-29,269,330!2026-01-03,271,330!2025-12-03,250,330!2025-12-04,251,330!2025-11-09,229,330-->

- For every object $Y$ and every pair of morphisms $f_{1}:Y\to X_{1}$, $f_{2}:Y\to X_{2}$, ::@:: there exists a unique morphism $f:Y\to X_{1}\times X_{2}$ such that the following diagram [commutes](commutative%20diagram.md): <p> ![Universal property of the product](../../archives/Wikimedia%20Commons/CategoricalProduct-03.svg) <!--SR:!2025-08-11,154,310!2025-12-08,254,330-->

Whether a product {@{exists may depend on $C$ or on $X_{1}$ and $X_{2}$}@}. If {@{it does exist, it is unique [up to](up%20to.md) [canonical isomorphism](canonical%20isomorphism.md)}@}, because {@{of the universal property, so one may speak of _the_ product}@}. This has the following meaning: if {@{$X',\pi _{1}',\pi _{2}'$ is another product}@}, there {@{exists a unique isomorphism $h:X'\to X_{1}\times X_{2}$ such that $\pi _{1}'=\pi _{1}\circ h$ and $\pi _{2}'=\pi _{2}\circ h$}@}. <!--SR:!2026-01-11,279,330!2025-11-18,237,330!2025-12-26,266,330!2026-01-02,270,330!2026-01-15,283,330-->

{@{The morphisms $\pi _{1}$ and $\pi _{2}$}@} are called {@{the __[canonical projections](canonical%20projection.md#canonical%20surjection)__ or __projection morphisms__}@}; the letter {@{$\pi$ alliterates with projection}@}. Given {@{$Y$ and $f_{1}$, $f_{2}$}@}, {@{the unique morphism $f$}@} is called {@{the __product of morphisms__ $f_{1}$ and $f_{2}$ and is denoted $\langle f_{1},f_{2}\rangle$}@}. <!--SR:!2025-12-14,257,330!2025-12-31,268,330!2026-01-09,277,330!2025-12-18,261,330!2025-11-07,227,330!2026-01-13,281,330-->

### product of an arbitrary family

Instead of {@{two objects}@}, we can {@{start with an arbitrary family of objects [indexed](index%20set.md) by a set $I$}@}. <!--SR:!2026-01-21,288,330!2025-11-22,241,330-->

Given {@{a family $\left(X_{i}\right)_{i\in I}$ of objects}@}, {@{a __product__ of the family}@} is {@{an object $X$ equipped with morphisms $\pi _{i}:X\to X_{i}$, satisfying the following universal property}@}: <!--SR:!2026-01-11,279,330!2025-11-13,233,330!2025-11-12,232,330-->

- For every object $Y$ and every $I$-indexed family of morphisms $f_{i}:Y\to X_{i}$, ::@::there exists a unique morphism $f:Y\to X$ such that the following diagrams commute for all $i\in I:$ <p> ![Universal product of the product](../../archives/Wikimedia%20Commons/Cat%20product.svg) <!--SR:!2025-09-18,175,310!2025-10-12,191,310-->

The product is denoted {@{$\prod _{i\in I}X_{i}$}@}. If {@{$I=\{1,\ldots ,n\}$}@}, then it is denoted {@{$X_{1}\times \cdots \times X_{n}$}@} and the product of morphisms is denoted {@{$\langle f_{1},\ldots ,f_{n}\rangle$}@}. <!--SR:!2025-11-17,236,330!2025-11-19,238,330!2025-10-07,188,310!2026-01-04,275,330-->

### equational definition

Alternatively, the product may be {@{defined through equations}@}. So, for example, for the binary product: <!--SR:!2025-12-13,256,330-->

- Existence of $f$ ::@:: is guaranteed by existence of the operation $\langle \cdot ,\cdot \rangle$. <!--SR:!2025-12-23,265,330!2025-12-11,254,330-->
- Commutativity of the diagrams above ::@:: is guaranteed by the equality: for all $f_{1},f_{2}$ and all $i\in \{1,2\}$, $\pi _{i}\circ \left\langle f_{1},f_{2}\right\rangle =f_{i}$ <!--SR:!2025-10-01,183,310!2025-10-13,192,310-->
- Uniqueness of $f$ ::@:: is guaranteed by the equality: for all $g:Y\to X_{1}\times X_{2}$, $\left\langle \pi _{1}\circ g,\pi _{2}\circ g\right\rangle =g$.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-09-14,181,310!2025-07-19,128,290-->

### as a limit

The product is {@{a special case of a [limit](limit%20(category%20theory).md)}@}. This may be seen by {@{using a [discrete category](discrete%20category.md) \(a family of objects without any morphisms, other than their identity morphisms\)}@} as {@{the [diagram](diagram%20(category%20theory).md) required for the definition of the limit}@}. {@{The discrete objects}@} will {@{serve as the index of the components and projections}@}. If we {@{regard this diagram as a functor}@}, it is {@{a functor from the index set $I$ considered as a discrete category}@}. {@{The definition of the product}@} then {@{coincides with the definition of the limit}@}, {@{$\{f\}_{i}$ being a [cone](cone%20(category%20theory).md)}@} and {@{projections being the limit \(limiting cone\)}@}. <!--SR:!2025-11-27,245,330!2025-12-04,251,330!2025-12-06,252,330!2025-04-09,67,310!2025-04-09,67,310!2025-12-31,271,330!2025-08-30,172,310!2025-04-09,67,310!2025-04-09,67,310!2025-09-20,177,310!2025-12-28,269,330-->

### universal property

Just as {@{the limit is a special case of the [universal construction](universal%20construction.md)}@}, {@{so is the product}@}. Starting with {@{the definition given for the [universal property of limits](limit%20(category%20theory).md#universal%20property)}@}, take {@{$\mathbf {J}$ as the discrete category with two objects}@}, so that {@{$\mathbf {C} ^{\mathbf {J} }$ is simply the [product category](product%20category.md) $\mathbf {C} \times \mathbf {C}$}@}. {@{The [diagonal functor](diagonal%20functor.md) $\Delta :\mathbf {C} \to \mathbf {C} \times \mathbf {C}$}@} assigns to {@{each object $X$ the [ordered pair](ordered%20pair.md) $(X,X)$ and to each morphism $f$ the pair $(f,f)$}@}. {@{The product $X_{1}\times X_{2}$ in $C$}@} is given by {@{a [universal morphism](universal%20morphism.md) from the functor $\Delta$ to the object $\left(X_{1},X_{2}\right)$ in $\mathbf {C} \times \mathbf {C}$}@}. This universal morphism consists of {@{an object $X$ (annotation: $X$ is also denoted $X_1 \times X_2$) of $C$ and a morphism $(X,X)\to \left(X_{1},X_{2}\right)$ which contains projections}@}. <!--SR:!2026-01-23,290,330!2025-11-11,231,330!2025-11-28,246,330!2025-11-24,242,330!2025-09-19,188,310!2026-01-20,287,330!2025-12-12,255,330!2025-12-27,267,330!2025-12-03,250,330!2025-12-09,255,330-->

## examples

In {@{the [category of sets](category%20of%20sets.md)}@}, {@{the product \(in the category theoretic sense\) is the Cartesian product}@}. Given {@{a family of sets $X_{i}$}@} the product is defined as {@{$$\prod _{i\in I}X_{i}:=\left\{\left(x_{i}\right)_{i\in I}:x_{i}\in X_{i}{\text{ for all } }i\in I\right\}$$ (annotation: all possible $I$-indexed tuples)}@} with {@{the canonical projections $$\pi _{j}:\prod _{i\in I}X_{i}\to X_{j},\quad \pi _{j}\left(\left(x_{i}\right)_{i\in I}\right):=x_{j}.$$ (annotation: extract the $j$-th component of the tuple)}@} Given {@{any set $Y$ with a family of functions $f_{i}:Y\to X_{i}$}@}, {@{the universal arrow $f:Y\to \prod _{i\in I}X_{i}$}@} is defined by {@{$f(y):=\left(f_{i}(y)\right)_{i\in I}$ (annotation: make a $I$-indexed tuple by evaluating the family of functions on the same argument)}@}. <!--SR:!2025-11-15,234,330!2025-12-29,270,330!2026-01-16,284,330!2025-12-15,258,330!2025-12-30,271,330!2025-05-18,82,270!2025-11-11,231,330!2026-01-05,276,330-->

Other examples:

- In the [category of topological spaces](category%20of%20topological%20spaces.md), the product ::@:: is the space whose underlying set is the Cartesian product and which carries the [product topology](product%20topology.md). The product topology is the [coarsest topology](coarsest%20topology.md) for which all the projections are [continuous](continuous%20function%20(topology).md#continuous%20functions%20between%20topological%20spaces). <!--SR:!2025-06-29,120,290!2025-07-25,130,290-->
- In the [category of modules](category%20of%20modules.md) over some ring $R$, the product ::@:: is the Cartesian product with addition defined componentwise and distributive multiplication. <!--SR:!2025-05-26,87,270!2025-07-13,120,270-->
- In the [category of groups](category%20of%20groups.md), the product ::@:: is the [direct product of groups](direct%20product%20of%20groups.md) given by the Cartesian product with multiplication defined componentwise. <!--SR:!2025-05-26,87,270!2025-08-16,158,310-->
- In the [category of graphs](graph%20homomorphism.md#structure%20of%20homomorphisms), the product ::@:: is the [tensor product of graphs](tensor%20product%20of%20graphs.md). <!--SR:!2025-05-28,88,270!2025-09-20,186,310-->
- In the [category of relations](category%20of%20relations.md), the product ::@:: is given by the [disjoint union](disjoint%20union.md). \(This may come as a bit of a surprise given that the category of sets is a [subcategory](subcategory.md) of the category of relations.\) (annotation: Intuitively, this is because relations are less restrictive than functions, so the product can be even "more generalized", considering that the disjoint union is "more general" than the Cartesian product.) <!--SR:!2025-09-19,176,310!2025-10-05,187,310-->
- In the category of [algebraic varieties](algebraic%20variety.md), the product ::@:: is given by the [Segre embedding](Segre%20embedding.md). <!--SR:!2025-06-28,120,290!2025-04-24,59,270-->
- In the category of [semi-abelian monoids](trace%20monoid.md), the product ::@:: is given by the [history monoid](history%20monoid.md). <!--SR:!2025-07-03,124,290!2025-06-17,93,250-->
- In the category of [Banach spaces](Banach%20spaces.md) and [short maps](short%20map.md), the product ::@:: carries the [_l_<sup>∞</sup>](l-infinity.md) norm.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-06-17,93,250!2025-09-28,191,310-->
- A [partially ordered set](partially%20ordered%20set.md) can be treated as a category, using the order relation as the morphisms. In this case the products and [coproducts](coproduct.md) ::@:: correspond to greatest lower bounds \([meets](meet%20(mathematics).md)\) and least upper bounds \([joins](join%20(mathematics).md)\). <!--SR:!2025-07-29,135,290!2025-06-16,92,250-->

## discussion

An example {@{in which the product does not exist}@}: In {@{the category of fields}@}, {@{the product $\mathbb {Q} \times F_{p}$ does not exist}@}, since {@{there is no field with homomorphisms to both $\mathbb {Q}$ and $F_{p}$}@}. <!--SR:!2025-12-03,250,330!2025-12-13,256,330!2025-12-02,249,330!2025-12-22,264,330-->

Another example: {@{An [empty product](empty%20product.md) \(that is, $I$ is the [empty set](empty%20set.md)\)}@} is {@{the same as a [terminal object](terminal%20object.md) (annotation: an empty product degenerates into requiring an unique morphism from every object)}@}, and {@{some categories, such as the category of [infinite groups](infinite%20group.md)}@}, {@{do not have a terminal object}@}: given {@{any infinite group $G$}@} there are {@{infinitely many morphisms $\mathbb {Z} \to G$, so $G$ cannot be terminal}@}. <!--SR:!2025-12-04,251,330!2025-12-31,272,330!2025-12-09,255,330!2025-10-06,187,310!2026-01-17,285,330!2025-07-07,125,290-->

If {@{$I$ is a set such that all products for families indexed with $I$ exist}@}, then one can {@{treat each product as a [functor](functor.md) $\mathbf {C} ^{I}\to \mathbf {C}$}@}.<sup>[\[3\]](#^ref-3)</sup> How {@{this functor maps objects is obvious}@}. Mapping of {@{morphisms is subtle}@}, because {@{the product of morphisms defined above does not fit}@}. First, consider {@{the binary product functor, which is a [bifunctor](bifunctor.md#bifunctors%20and%20multifunctors)}@}. For {@{$f_{1}:X_{1}\to Y_{1},f_{2}:X_{2}\to Y_{2}$}@} we should {@{find a morphism $X_{1}\times X_{2}\to Y_{1}\times Y_{2}$}@}. We {@{choose $\left\langle f_{1}\circ \pi _{1},f_{2}\circ \pi _{2}\right\rangle$}@}. This operation on morphisms is called {@{__Cartesian product of morphisms__}@}.<sup>[\[4\]](#^ref-4)</sup> Second, consider {@{the general product functor}@}. For {@{families $\left\{X\right\}_{i},\left\{Y\right\}_{i},f_{i}:X_{i}\to Y_{i}$}@} we should {@{find a morphism $\prod _{i\in I}X_{i}\to \prod _{i\in I}Y_{i}$}@}. We choose {@{the product of morphisms $\left\{f_{i}\circ \pi _{i}\right\}_{i}$}@}. <!--SR:!2025-12-05,251,330!2026-01-14,282,330!2025-10-07,188,310!2025-12-28,268,330!2025-10-02,195,310!2026-01-14,282,330!2025-12-30,270,330!2025-09-15,172,310!2025-06-13,112,290!2025-12-27,268,330!2025-11-16,235,330!2026-01-07,275,330!2025-09-17,174,310!2025-04-09,67,310-->

{@{A category where every finite set of objects has a product}@} is sometimes called {@{a __Cartesian category__}@}<sup>[\[4\]](#^ref-4)</sup> \(although some authors use this phrase to mean "{@{a category with all finite limits}@}"\). <!--SR:!2025-11-10,230,330!2026-01-22,289,330!2025-12-17,260,330-->

The product is {@{[associative](associative.md)}@}. Suppose {@{$C$ is a Cartesian category, product functors have been chosen as above, and $1$ denotes a terminal object of $C$}@}. We then have {@{[natural isomorphisms](natural%20isomorphism.md#natural%20isomorphism) $$\begin{aligned} & X\times (Y\times Z)\simeq (X\times Y)\times Z\simeq X\times Y\times Z, \\ & X\times 1\simeq 1\times X\simeq X, \\ & X\times Y\simeq Y\times X. \end{aligned}$$}@} These properties are {@{formally similar to those of a commutative [monoid](monoid.md)}@}; {@{a Cartesian category with its finite products}@} is {@{an example of a [symmetric monoidal category](symmetric%20monoidal%20category.md)}@}. <!--SR:!2026-01-01,272,330!2025-06-01,89,270!2025-09-18,184,310!2025-07-06,124,290!2025-11-08,228,330!2025-07-01,122,290-->

## distributivity

- Main article: [Distributive category](distributive%20category.md)

For {@{any objects $X,Y,{\text{ and } }Z$ of a category with finite products and coproducts}@}, there is {@{a [canonical](list%20of%20mathematical%20jargon.md#canonical) morphism $X\times Y+X\times Z\to X\times (Y+Z)$}@}, where {@{the plus sign here denotes the [coproduct](coproduct.md)}@}. To see this, note that {@{the universal property of the coproduct $X\times Y+X\times Z$ guarantees the existence of unique arrows filling out the following diagram \(the induced arrows are dashed\)}@}: <p> {@{![product—coproduct distributivity](../../archives/Wikimedia%20Commons/Product-Coproduct%20Distributivity%20SVG.svg)}@} <!--SR:!2025-11-21,240,330!2025-09-28,182,310!2025-12-24,264,330!2025-12-10,255,330!2025-05-24,85,270-->

{@{The universal property of the product $X\times (Y+Z)$}@} then {@{guarantees a unique morphism $X\times Y+X\times Z\to X\times (Y+Z)$ induced by the dashed arrows (annotation: the the dashed arrows are the unique projection morphisms) in the above diagram}@}. {@{A [distributive category](distributive%20category.md)}@} is one {@{in which this morphism is actually an isomorphism}@}. Thus in {@{a distributive category, there is the canonical isomorphism $$X\times (Y+Z)\simeq (X\times Y)+(X\times Z).$$}@} <!--SR:!2025-10-19,195,310!2025-05-25,86,270!2026-01-12,280,330!2026-01-08,276,330!2025-06-30,121,290-->

## see also

- [Coproduct](coproduct.md) – ::@:: the [dual](dual%20(category%20theory).md) of the product <!--SR:!2025-09-27,190,310!2026-01-13,281,330-->
- [Diagonal functor](diagonal%20functor.md) – ::@:: the [left adjoint](left%20adjoint.md) of the product functor. <!--SR:!2025-05-25,86,270!2025-08-02,123,250-->
- [Limit and colimits](limit%20(category%20theory).md) – ::@:: Mathematical concept <!--SR:!2026-01-03,274,330!2026-01-12,280,330-->
- [Equalizer](equaliser%20(mathematics).md) – ::@:: Set of arguments where two or more functions have the same value <!--SR:!2025-12-16,259,330!2026-01-10,278,330-->
- [Inverse limit](inverse%20limit.md) – ::@:: Construction in category theory <!--SR:!2025-12-07,253,330!2025-12-10,255,330-->
- [Cartesian closed category](Cartesian%20closed%20category.md) – ::@:: Type of category in category theory <!--SR:!2026-01-18,285,330!2026-01-07,275,330-->
- [Categorical pullback](categorical%20pullback.md) – ::@:: Most general completion of a commutative square given two morphisms with same codomain <!--SR:!2025-05-23,84,270!2025-06-12,111,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/product_(category_theory)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFLambek J., Scott P. J.1988"></a> Lambek J., Scott P. J. \(1988\). _Introduction to Higher-Order Categorical Logic_. Cambridge University Press. p. 304. <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFQiaochu Yuan2012"></a> Qiaochu Yuan \(June 23, 2012\). ["Banach spaces \(and Lawvere metrics, and closed categories\)"](https://qchu.wordpress.com/2012/06/23/banach-spaces-and-lawvere-metrics-and-closed-categories/). _Annoying Precision_. <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFLane1988"></a> Lane, S. Mac \(1988\). _Categories for the working mathematician_ \(1st ed.\). New York: Springer-Verlag. p. 37. [ISBN](ISBN%20(identifier).md) [0-387-90035-7](https://en.wikipedia.org/wiki/Special:BookSources/0-387-90035-7). <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFMichael Barr, Charles Wells1999"></a> Michael Barr, Charles Wells \(1999\). [_Category Theory – Lecture Notes for ESSLLI_](https://web.archive.org/web/20110413051026/http://www.let.uu.nl/esslli/Courses/barr/barrwells.ps). p. 62. Archived from [the original](http://www.let.uu.nl/esslli/Courses/barr/barrwells.ps) on 2011-04-13. <a id="^ref-4"></a>^ref-4

- <a id="CITEREFAdámekHorst HerrlichGeorge E. Strecker1990"></a> Adámek, Jiří; Horst Herrlich; George E. Strecker \(1990\). [_Abstract and Concrete Categories_](http://katmat.math.uni-bremen.de/acc/acc.pdf) \(PDF\). John Wiley & Sons. [ISBN](ISBN%20(identifier).md) [0-471-60922-6](https://en.wikipedia.org/wiki/Special:BookSources/0-471-60922-6).
- <a id="CITEREFBarrCharles Wells1999"></a> Barr, Michael; Charles Wells \(1999\). [_Category Theory for Computing Science_](https://web.archive.org/web/20160304031956/http://www.math.mcgill.ca/triples/Barr-Wells-ctcs.pdf) \(PDF\). Les Publications CRM Montreal \(publication PM023\). Archived from [the original](http://www.math.mcgill.ca/triples/Barr-Wells-ctcs.pdf) \(PDF\) on 2016-03-04. Retrieved 2016-03-21. Chapter 5.
- <a id="CITEREFMac Lane1998"></a> [Mac Lane, Saunders](Saunders%20Mac%20Lane.md) \(1998\). _[Categories for the Working Mathematician](Categories%20for%20the%20Working%20Mathematician.md)_. [Graduate Texts in Mathematics](Graduate%20Texts%20in%20Mathematics.md) __5__ \(2nd ed.\). Springer. [ISBN](ISBN%20(identifier).md) [0-387-98403-8](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98403-8).
- Definition 2.1.1 in <a id="CITEREFBorceux1994"></a> Borceux, Francis \(1994\). [_Handbook of categorical algebra_](https://archive.org/details/handbookofcatego0000borc/page/39). Encyclopedia of mathematics and its applications 50–51, 53 \[i.e. 52\]. Vol. 1. Cambridge University Press. p. [39](https://archive.org/details/handbookofcatego0000borc/page/39). [ISBN](ISBN%20(identifier).md) [0-521-44178-1](https://en.wikipedia.org/wiki/Special:BookSources/0-521-44178-1).

## external links

- [Interactive Web page](https://web.archive.org/web/20080916162345/http://www.j-paine.org/cgi-bin/webcats/webcats.php)which generates examples of products in the category of finite sets. Written by [Jocelyn Paine](https://web.archive.org/web/20081223001815/http://www.j-paine.org/).
- [Product](https://ncatlab.org/nlab/show/product) at the [_n_<!-- markdown separator -->Lab](nLab.md)

> <!-- hide <p> - [v](https://en.wikipedia.org/wiki/Template:Category%20theory) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Category%20theory) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3ACategory%20theory) <p>  <p>  <br/> -->
> __[Category theory](category%20theory.md)__
>
> | Key concepts                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | ----------------------------------------------------------:| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | __Key concepts__                                           | - [Category](category%20(mathematics).md)  <br/>     - [Abelian](abelian%20category.md) <br/>     - [Additive](additive%20category.md) <br/>     - [Concrete](concrete%20category.md) <br/>     - [Pre-abelian](pre-abelian%20category.md) <br/>     - [Preadditive](preadditive%20category.md) <br/>     - [Bicategory](bicategory.md) <p>  <p> - [Adjoint functors](adjoint%20functors.md) <br/> - [CCC](Cartesian%20closed%20category.md) <br/> - [Commutative diagram](commutative%20diagram.md) <br/> - [End](end%20(category%20theory).md) <br/> - [Exponential](exponential%20object.md) <br/> - [Functor](functor.md) <br/> - [Kan extension](Kan%20extension.md) <br/> - [Morphism](morphism.md) <br/> - [Natural transformation](natural%20transformation.md) <br/> - [Universal property](universal%20property.md) <br/> - [Yoneda lemma](Yoneda%20lemma.md) |
> | __[Universal constructions](universal%20construction.md)__ | __[Limits](limit%20(category%20theory).md)__ <br/> - [Terminal objects](initial%20and%20terminal%20objects.md) <br/> - [Products](product%20(category%20theory).md) <br/> - [Equalizers](equaliser%20(mathematics).md)  <br/>     - [Kernels](kernel%20(category%20theory).md) <p>  <p> - [Pullbacks](pullback%20(category%20theory).md) <br/> - [Inverse limit](inverse%20limit.md) <p> __[Colimits](colimit.md)__ <br/> - [Initial objects](initial%20and%20terminal%20objects.md) <br/> - [Coproducts](coproduct.md) <br/> - [Coequalizers](coequalizer.md)  <br/>     - [Cokernels and quotients](cokernel.md) <p>  <p> - [Pushout](pushout%20(category%20theory).md) <br/> - [Direct limit](direct%20limit.md)                                                                                                                                                     |
> | __[Algebraic categories](algebraic%20category.md)__        | - [Sets](category%20of%20sets.md) <br/> - [Relations](category%20of%20relations.md) <br/> - [Magmas](category%20of%20magmas.md#category%20of%20magmas) <br/> - [Groups](category%20of%20groups.md) <br/> - [Abelian groups](category%20of%20abelian%20groups.md) <br/> - [Rings](category%20of%20rings.md) \([Fields](category%20of%20rings.md#category%20of%20fields)\) <br/> - [Modules](category%20of%20modules.md) \([Vector spaces](category%20of%20modules.md#example%20the%20category%20of%20vector%20spaces)\)                                                                                                                                                                                                                                                                                                                                                  |
> | __Constructions on categories__                            | - [Free category](free%20category.md) <br/> - [Functor category](functor%20category.md) <br/> - [Kleisli category](Kleisli%20category.md) <br/> - [Opposite category](opposite%20category.md) <br/> - [Quotient category](quotient%20category.md) <br/> - [Product category](product%20category.md) <br/> - [Comma category](comma%20category.md) <br/> - [Subcategory](subcategory.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>
> | [Higher category theory](higher%20category%20theory.md) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | -------------------------------------------------------:| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | __Key concepts__                                        | - [Categorification](categorification.md) <br/> - [Enriched category](enriched%20category.md) <br/> - [Higher-dimensional algebra](higher-dimensional%20algebra.md) <br/> - [Homotopy hypothesis](homotopy%20hypothesis.md) <br/> - [Model category](model%20category.md) <br/> - [Simplex category](simplex%20category.md) <br/> - [String diagram](string%20diagram.md) <br/> - [Topos](topos.md)                                                                                                                                                |
> | __n-categories__                                        | __[Weak n-categories](weak%20n-category.md)__ <br/> - [Bicategory](bicategory.md) \([pseudofunctor](pseudo-functor.md)\) <br/> - [Tricategory](tricategory.md) <br/> - [Tetracategory](tetracategory.md) <br/> - [Kan complex](quasi-category.md) <br/> - [∞-groupoid](∞-groupoid.md) <br/> - [∞-topos](∞-topos.md) <p> __[Strict n-categories](strict%20n-category.md#strict%20higher%20categories)__ <br/> - [2-category](strict%202-category.md) \([2-functor](2-functor.md)\) <br/> - [3-category](3-category.md#strict%20higher%20categories) |
> | __[Categorified](categorification.md) concepts__        | - [2-group](2-group.md) <br/> - [2-ring](2-ring.md) <br/> - [_E<sub>n</sub>_-ring](en-ring.md) <br/> - \([Traced](traced%20monoidal%20category.md)\)\([Symmetric](symmetric%20monoidal%20category.md)\) [monoidal category](monoidal%20category.md) <br/> - [n-group](n-group%20(category%20theory).md) <br/> - [n-monoid](n-monoid.md)                                                                                                                                                                                                            |
>
> [![A simple triangular commutative diagram](../../archives/Wikimedia%20Commons/Commutative%20diagram%20for%20morphism.svg)](commutative%20diagram.md)
>
> - ![category icon](../../archives/Wikimedia%20Commons/Symbol%20category%20class.svg) __[Category](https://en.wikipedia.org/wiki/Category:Category%20theory)__
> - ![list icon](../../archives/Wikimedia%20Commons/Symbol%20list%20class.svg) __[Outline](outline%20of%20category%20theory.md)__
> - ![list icon](../../archives/Wikimedia%20Commons/Symbol%20list%20class.svg) __[Glossary](glossary%20of%20category%20theory.md)__

<!-- markdownlint MD028 -->

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Limits \(category theory\)](https://en.wikipedia.org/wiki/Category:Limits%20%28category%20theory%29)
