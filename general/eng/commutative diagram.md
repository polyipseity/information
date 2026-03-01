---
aliases:
  - commutative diagram
  - commutative diagrams
  - diagram chasing
  - diagrammatic search
  - diagrammatic searches
tags:
  - flashcard/active/general/eng/commutative_diagram
  - language/in/English
---

# commutative diagram

> {@{![The commutative diagram used in the proof of the [five lemma](five%20lemma.md)](../../archives/Wikimedia%20Commons/5%20lemma.svg)}@}
>
> {@{The commutative diagram used in the proof of the [five lemma](five%20lemma.md)}@} <!--SR:!2029-10-22,1342,350!2029-10-23,1343,350-->

In {@{[mathematics](mathematics.md), and especially in [category theory](category%20theory.md)}@}, {@{a __commutative diagram__}@} is {@{a [diagram](diagram%20(category%20theory).md) such that all directed paths in the diagram with the same start and endpoints lead to the same result}@}.<sup>[\[1\]](#^ref-1)</sup> It is said that {@{commutative diagrams play the role in category theory}@} that {@{[equations](equations.md) play in [algebra](algebra.md)}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2029-04-22,1192,350!2029-05-12,1212,350!2029-01-21,1127,350!2029-07-30,1273,350!2029-02-15,1138,350-->

## description

A commutative diagram often consists of {@{three parts: (annotation: objects, morphisms, paths/composites)}@} <!--SR:!2029-03-11,1162,350-->

- [objects](object%20(category%20theory).md) \(also known as _vertices_\)
- [morphisms](morphism.md) \(also known as _arrows_ or _edges_\)
- paths or composites

### arrow symbols

In {@{algebra texts}@}, {@{the type of morphism}@} can be {@{denoted with different arrow usages}@}: <!--SR:!2029-06-25,1248,350!2029-05-26,1224,350!2028-10-07,1042,350-->

- A [monomorphism](monomorphism.md) ::@:: may be labeled with a $\hookrightarrow$<sup>[\[3\]](#^ref-3)</sup> or a $\rightarrowtail$.<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2026-08-12,368,290!2027-05-08,577,310-->
- An [epimorphism](epimorphism.md) ::@:: may be labeled with a $\twoheadrightarrow$. <!--SR:!2027-12-19,789,330!2026-07-31,330,250-->
- An [isomorphism](isomorphism.md) ::@:: may be labeled with a ${\overset {\sim }{\rightarrow } }$. <!--SR:!2029-10-24,1344,350!2029-07-31,1274,350-->
- The dashed arrow ::@:: typically represents the claim that the indicated morphism exists \(whenever the rest of the diagram holds\); the arrow may be optionally labeled as $\exists$. <!--SR:!2028-01-06,811,330!2029-04-21,1191,350-->
  - If the morphism is in addition unique, ::@:: then the dashed arrow may be labeled $!$ or $\exists !$. <!--SR:!2027-10-03,741,330!2029-09-26,1322,350-->
- If the morphism acts between two arrows \(such as in the case of [higher category theory](higher%20category%20theory.md)\), ::@:: it's called preferably a [natural transformation](natural%20transformation.md) and may be labelled as $\Rightarrow$ \(as seen below in this article\). <!--SR:!2029-08-17,1290,350!2027-05-17,635,330-->

{@{The meanings of different arrows}@} are {@{not entirely standardized}@}: {@{the arrows used for monomorphisms, epimorphisms, and isomorphisms}@} are {@{also used for [injections](injective%20function.md), [surjections](surjection.md), and [bijections](bijection.md)}@}, as well as {@{the cofibrations, fibrations, and weak equivalences in a [model category](model%20category.md)}@}. <!--SR:!2028-10-08,1042,350!2029-08-25,1296,350!2029-02-28,1151,350!2029-01-10,1119,350!2027-07-16,683,330-->

### verifying commutativity

{@{Commutativity makes sense}@} for {@{a [polygon](polygon.md) of any finite number of sides \(including just 1 or 2\)}@}, and a diagram is commutative {@{if every polygonal subdiagram is commutative}@}. <!--SR:!2029-06-05,1229,350!2028-11-22,1079,350!2028-10-28,1059,350-->

Note that {@{a diagram may be non-commutative}@}, i.e., {@{the composition of different paths in the diagram may not give the same result}@}. <!--SR:!2029-10-01,1326,350!2029-07-04,1252,350-->

## examples

### example 1

In {@{the left diagram, which expresses the [first isomorphism theorem](isomorphism%20theorems.md#first%20isomorphism%20theorem)}@}, {@{commutativity of the triangle}@} means that {@{$f={\tilde {f} }\circ \pi$}@}. In the right diagram, {@{commutativity of the square}@} means {@{$h\circ f=k\circ g$}@}. <!--SR:!2029-05-22,1222,350!2029-06-02,1231,350!2027-11-28,783,330!2029-10-08,1331,350!2029-09-17,1314,350-->

|                                                                                                                                                                                                                           |                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| ![The commutative diagram expressing the "first isomorphism theorem". It does not indicate which arrows are injective or surjective.](../../archives/Wikimedia%20Commons/First%20isomorphism%20theorem%20%28plain%29.svg) | ![a generic commutative square](../../archives/Wikimedia%20Commons/Commutative%20square.svg) |

### example 2

In order for {@{the diagram below to commute}@}, {@{three equalities must be satisfied}@}: <!--SR:!2028-12-05,1090,350!2029-03-02,1153,350-->

1. $r\circ h\circ g=H\circ G\circ l$
2. $m\circ g=G\circ l$
3. $r\circ h=H\circ m$

Here, since {@{the first equality follows from the last two}@}, it {@{suffices to show that \(2\) and \(3\) are true in order for the diagram to commute}@}. However, since {@{equality \(3\) generally does not follow from the other two}@}, it is {@{generally not enough to have only equalities \(1\) and \(2\) if one were to show that the diagram commutes}@}. <p> (annotation: the diagram) {@{![An example of a commutative diagram.](../../archives/Wikimedia%20Commons/CommutativeDiagramExample.svg)}@} <!--SR:!2029-10-19,1340,350!2029-05-15,1215,350!2029-07-02,1253,350!2029-03-12,1163,350!2029-09-15,1313,350-->

## diagram chasing

{@{__Diagram chasing__ \(also called __diagrammatic search__\)}@} is {@{a method of [mathematical proof](mathematical%20proof.md) used especially in [homological algebra](homological%20algebra.md)}@}, where one establishes {@{a property of some morphism by tracing the elements of a commutative diagram}@}. A proof by diagram chasing typically involves {@{the formal use of the properties of the diagram}@}, such as {@{[injective](injective.md) or [surjective](surjective.md) maps, or [exact sequences](exact%20sequence.md)}@}.<sup>[\[5\]](#^ref-5)</sup> {@{A [syllogism](syllogism.md) is constructed}@}, for which the graphical display of {@{the diagram is just a visual aid}@}. It follows that {@{one ends up "chasing" elements around the diagram}@}, until {@{the desired element or result is constructed or verified}@}. <!--SR:!2029-04-13,1183,350!2029-01-17,1125,350!2028-01-21,777,330!2028-01-28,831,330!2028-01-31,832,330!2029-04-11,1181,350!2029-05-03,1203,350!2029-02-22,1145,350!2028-12-24,1105,350-->

{@{Examples of proofs by diagram chasing}@} include those typically given for {@{the [five lemma](five%20lemma.md), the [snake lemma](snake%20lemma.md), the [zig-zag lemma](zig-zag%20lemma.md), and the [nine lemma](nine%20lemma.md)}@}. <!--SR:!2029-10-17,1338,350!2028-11-27,1083,350-->

## in higher category theory

- Main article: [Higher category theory](higher%20category%20theory.md)

In {@{higher category theory}@}, one considers {@{not only objects and arrows, but arrows between the arrows, arrows between arrows between arrows, and so on [ad infinitum](https://en.wiktionary.org/wiki/ad%20infinitum)}@}. For example, {@{the category of small categories __Cat__}@} is {@{naturally a 2-category}@}, with {@{[functors](functor.md) as its arrows and [natural transformations](natural%20transformation.md) as the arrows between functors}@}. In this setting, commutative diagrams {@{may include these higher arrows as well}@}, which are often {@{depicted in the following style: $\Rightarrow$}@}. For example, the following \(somewhat trivial\) diagram depicts {@{two categories __C__ and __D__, together with two functors F, G : __C__ → __D__ and a natural transformation α : F ⇒ G}@}: <p> {@{![A diagram depicting two functors and a natural transformation between them.](../../archives/Wikimedia%20Commons/2-commutative-diagram.svg)}@} <!--SR:!2029-10-12,1334,350!2029-08-10,1284,350!2028-12-23,1103,350!2029-06-09,1233,350!2027-05-11,631,330!2029-02-19,1142,350!2027-10-15,740,330!2029-02-24,1147,350!2029-07-01,1252,350-->

There are {@{two kinds of composition in a 2-category}@} \(called {@{__vertical composition__ and __horizontal composition__}@}\), and they may also be depicted via {@{[pasting diagrams](pasting%20diagrams.md) \(see [2-category\#Definition](2-category.md#definition) for examples\)}@}. <!--SR:!2027-06-07,653,330!2029-04-10,1180,350!2029-01-07,1117,350-->

## diagrams as functors

- Main article: [Diagram \(category theory\)](diagram%20(category%20theory).md)

{@{A commutative diagram in a category _C_}@} can be interpreted as {@{a [functor](functor.md) from an index category _J_ to _C_}@}; one calls the functor {@{a __[diagram](diagram%20(category%20theory).md)__}@}. <!--SR:!2029-09-09,1308,350!2027-06-04,594,310!2029-10-07,1330,350-->

More formally, a commutative diagram is {@{a visualization of a diagram indexed by a [poset category](posetal%20category.md)}@}. Such a diagram typically includes: {@{(annotation: nodes, arrows, commutativity)}@} <!--SR:!2027-06-23,665,330!2029-02-04,1127,350-->

- a node ::@:: for every object in the index category, <!--SR:!2029-10-06,1329,350!2029-05-04,1204,350-->
- an arrow ::@:: for a generating set of morphisms \(omitting identity maps and morphisms that can be expressed as compositions\), <!--SR:!2027-04-24,564,310!2028-01-23,777,330-->
- the commutativity of the diagram \(the equality of different compositions of maps between two objects\), ::@:: corresponding to the uniqueness of a map between two objects in a poset category. <!--SR:!2029-06-23,1246,350!2028-11-08,1066,350-->

Conversely, given {@{a commutative diagram}@}, it {@{defines a poset category}@}, where: {@{(annotation: objects, morphisms, uniqueness)}@} <!--SR:!2028-10-18,1051,350!2029-07-07,1258,350!2028-01-15,819,330-->

- the objects ::@:: are the nodes, <!--SR:!2029-04-20,1190,350!2029-03-21,1172,350-->
- there is a morphism between any two objects ::@:: if and only if there is a \(directed\) path between the nodes, <!--SR:!2029-02-14,1137,350!2029-06-13,1237,350-->
- with the relation that this morphism is unique ::@:: \(any composition of maps is defined by its domain and target: this is the commutativity axiom\). <!--SR:!2027-05-09,628,330!2029-10-13,1335,350-->

However, {@{not every diagram commutes}@} \({@{the notion of diagram}@} {@{strictly generalizes commutative diagram}@}\). As a simple example, the diagram of {@{a single object with an endomorphism \($f\colon X\to X$\)}@}, or {@{with two parallel arrows \($\bullet \rightrightarrows \bullet$, that is, $f,g\colon X\to Y$, sometimes called the [free quiver](free%20quiver.md)\), as used in the definition of [equalizer](equaliser%20(mathematics).md)}@} {@{need not commute}@}. Further, {@{diagrams may be messy or impossible to draw}@}, when {@{the number of objects or morphisms is large \(or even infinite\)}@}. <!--SR:!2028-06-24,883,330!2029-09-01,1302,350!2029-10-18,1339,350!2029-04-19,1189,350!2027-12-02,785,330!2029-10-14,1336,350!2026-07-09,125,399!2026-07-11,127,399-->

## see also

- [Mathematical diagram](mathematical%20diagram.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/commutative_diagram) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFWeisstein"></a> Weisstein, Eric W. ["Commutative Diagram"](http://mathworld.wolfram.com/CommutativeDiagram.html). _mathworld.wolfram.com_. Retrieved 2019-11-25. <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFMazzolaMilmeisterWeissmann2005"></a> Mazzola, Guerino; Milmeister, Gérard; Weissmann, Jody \(2005\). _Comprehensive Mathematics for Computer Scientists 2_. Springer. p. 140. [doi](doi%20(identifier).md):[10.1007/b138337](https://doi.org/10.1007%2Fb138337). [ISBN](ISBN%20(identifier).md) [978-3-540-26937-3](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-26937-3). <a id="^ref-2"></a>^ref-2
3. ["Maths - Category Theory - Arrow - Martin Baker"](https://www.euclideanspace.com/maths/discrete/category/principles/arrow/index.htm). _<www.euclideanspace.com>_. Retrieved 2019-11-25. <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFRiehl2016"></a> [Riehl, Emily](Emily%20Riehl.md) \(2016-11-17\). "1". [_Category Theory in Context_](https://math.jhu.edu/~eriehl/context.pdf) \(PDF\). Dover Publications. p. 11. <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFWeisstein"></a> Weisstein, Eric W. ["Diagram Chasing"](http://mathworld.wolfram.com/DiagramChasing.html). _mathworld.wolfram.com_. Retrieved 2019-11-25. <a id="^ref-5"></a>^ref-5

## bibliography

- <a id="CITEREFAdámekHorst HerrlichGeorge E. Strecker1990"></a> Adámek, Jiří; Horst Herrlich; George E. Strecker \(1990\). [_Abstract and Concrete Categories_](http://katmat.math.uni-bremen.de/acc/acc.pdf) \(PDF\). John Wiley & Sons. [ISBN](ISBN%20(identifier).md) [0-471-60922-6](https://en.wikipedia.org/wiki/Special:BookSources/0-471-60922-6). Now available as free on-line edition \(4.2MB PDF\).
- <a id="CITEREFBarrWells2002"></a> [Barr, Michael](Michael%20Barr%20(mathematician).md); [Wells, Charles](Charles%20Wells%20(mathematician).md) \(2002\). [_Toposes, Triples and Theories_](http://www.tac.mta.ca/tac/reprints/articles/12/tr12.pdf) \(PDF\). Springer. [ISBN](ISBN%20(identifier).md) [0-387-96115-1](https://en.wikipedia.org/wiki/Special:BookSources/0-387-96115-1). Revised and corrected free online version of _Grundlehren der mathematischen Wissenschaften \(278\)_ Springer-Verlag, 1983\).

## external links

- [Diagram Chasing](http://mathworld.wolfram.com/DiagramChasing.html) at [MathWorld](MathWorld.md)
- [WildCats](http://wildcatsformma.wordpress.com/) is a category theory package for [Mathematica](Mathematica.md). Manipulation and visualization of objects, [morphisms](morphism.md), categories, [functors](functor.md), [natural transformations](natural%20transformation.md).

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

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Homological algebra](https://en.wikipedia.org/wiki/Category:Homological%20algebra)
> - [Category theory](https://en.wikipedia.org/wiki/Category:Category%20theory)
> - [Mathematical proofs](https://en.wikipedia.org/wiki/Category:Mathematical%20proofs)
> - [Mathematical terminology](https://en.wikipedia.org/wiki/Category:Mathematical%20terminology)
> - [Diagrams](https://en.wikipedia.org/wiki/Category:Diagrams)
