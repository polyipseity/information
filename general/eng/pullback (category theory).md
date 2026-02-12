---
aliases:
  - Cartesian square
  - Cartesian squares
  - cartesian square
  - cartesian squares
  - fiber product
  - fiber products
  - fibered product
  - fibered products
  - fibre product
  - fibre products
  - pullback
  - pullback (category theory)
  - pullbacks
  - pullbacks (category theory)
tags:
  - flashcard/active/general/eng/pullback__category_theory_
  - language/in/English
---

# pullback

- For other uses, see [pullback](pullback.md).
- "{@{Fiber product}@}" redirects here. For {@{the case of schemes}@}, see {@{[Fiber product of schemes](fiber%20product%20of%20schemes.md)}@}. <!--SR:!2029-09-19,1319,350!2028-12-23,1106,350!2029-04-23,1196,350-->

In {@{[category theory](category%20theory.md), a branch of [mathematics](mathematics.md)}@}, {@{a __pullback__ \(also called a __fiber product__, __fibre product__, __fibered product__ or __Cartesian square__\)}@} is {@{the [limit](limit%20(category%20theory).md) of a [diagram](diagram%20(category%20theory).md) consisting of two [morphisms](morphism.md) _f_ : _X_ → _Z_ and _g_ : _Y_ → _Z_ with a common codomain}@}. The pullback is written {@{_P_ = _X_ ×<sub>_f_, _Z_, _g_</sub> _Y_}@}. Usually {@{the morphisms _f_ and _g_ are omitted from the notation}@}, and then the pullback is written {@{_P_ = _X_ ×<sub>_Z_</sub> _Y_}@}. <!--SR:!2029-09-24,1323,350!2027-11-30,789,330!2028-01-09,822,330!2029-10-19,1343,350!2029-05-30,1229,350!2029-01-19,1128,350-->

The pullback comes {@{equipped with two natural morphisms _P_ → _X_ and _P_ → _Y_}@}. The pullback of two morphisms _f_ and _g_ {@{need not exist}@}, but {@{if it does, it is essentially uniquely defined by the two morphisms}@}. In {@{many situations}@}, _X_ ×<sub>_Z_</sub> _Y_ may intuitively be thought of as {@{consisting of pairs of elements \(_x_, _y_\) with _x_ in _X_, _y_ in _Y_, and _f_\(_x_\)  =  _g_\(_y_\)}@}. For {@{the general definition}@}, {@{a [universal property](universal%20property.md)}@} is used, which {@{essentially expresses the fact that the pullback}@} is {@{the "most general" way}@} to {@{complete the two given morphisms to a [commutative square](commutative%20diagram.md)}@}. <!--SR:!2029-03-01,1152,350!2029-01-02,1115,350!2027-10-16,755,330!2029-03-12,1163,350!2029-10-04,1331,350!2029-09-25,1324,350!2027-11-04,771,330!2028-01-12,772,330!2026-05-03,119,388!2026-05-02,118,388-->

{@{The [dual concept](dual%20(category%20theory).md) of the pullback}@} is {@{the _[pushout](pushout%20(category%20theory).md)_}@}. <!--SR:!2028-12-21,1105,350!2029-03-16,1167,350-->

## universal property

Explicitly, {@{a pullback of the morphisms $f$ and $g$}@} consists of {@{an [object](object%20(category%20theory).md) $P$ and two morphisms $p_{1}:P\rightarrow X$ and $p_{2}:P\rightarrow Y$}@} for which {@{the diagram <p> &emsp; ![categorical pullback commutative diagram](../../archives/Wikimedia%20Commons/Categorical%20pullback.svg) <p> [commutes](commutative%20diagram.md)}@}. Moreover, {@{the pullback \(_P_, _p_<sub>1</sub>, _p_<sub>2</sub>\) must be [universal](universal%20property.md) with respect to this diagram}@}.<sup>[\[1\]](#^ref-1)</sup> That is, {@{for any other such triple \(_Q_, _q_<sub>1</sub>, _q_<sub>2</sub>\) where _q_<sub>1</sub> : _Q_ → _X_ and _q_<sub>2</sub> : _Q_ → _Y_ are morphisms with _f_ _q_<sub>1</sub> = _g_ _q_<sub>2</sub>}@}, there {@{must exist a unique _u_ : _Q_ → _P_ such that $$p_{1}\circ u=q_{1},\qquad p_{2}\circ u=q_{2}.$$}@} This situation is illustrated in {@{the following commutative diagram. <p> &emsp; ![categorical pullback universal property commutative diagram](../../archives/Wikimedia%20Commons/Categorical%20pullback%20%28expanded%29.svg)}@} <p> As with {@{all universal constructions}@}, a pullback, {@{if it exists, is unique up to [isomorphism](isomorphism.md)}@}. In fact, given {@{two pullbacks \(_A_, _a_<sub>1</sub>, _a_<sub>2</sub>\) and \(_B_, _b_<sub>1</sub>, _b_<sub>2</sub>\) of the same [cospan](cospan.md#cospans) _X_ → _Z_ ← _Y_}@}, there is {@{a unique isomorphism between _A_ and _B_ respecting the pullback structure}@}. <!--SR:!2029-10-18,1342,350!2027-02-04,541,310!2029-03-06,1157,350!2028-05-04,851,330!2028-05-02,895,330!2029-09-17,1317,350!2029-10-10,1336,350!2029-03-02,1153,350!2027-07-28,694,330!2029-01-25,1133,350!2028-04-08,876,330-->

## pullback and product

The pullback is {@{similar to the [product](product%20(category%20theory).md), but not the same}@}. One may obtain the product by {@{"forgetting" that the morphisms _f_ and _g_ exist, and forgetting that the object _Z_ exists}@}. One is then left with {@{a [discrete category](discrete%20category.md) containing only the two objects _X_ and _Y_, and no arrows between them}@}. This discrete category may be used as {@{the index set to construct the ordinary binary product}@}. Thus, the pullback can be thought of as {@{the ordinary \(Cartesian\) product, but with additional structure}@}. Instead of {@{"forgetting" _Z_, _f_, and _g_}@}, one can also {@{"trivialize" them by specializing _Z_ to be the [terminal object](terminal%20object.md) \(assuming it exists\)}@}. _f_ and _g_ are {@{then uniquely determined and thus carry no information}@}, and {@{the pullback of this cospan can be seen to be the product of _X_ and _Y_}@}. <!--SR:!2029-03-22,1173,350!2029-03-29,1180,350!2027-02-06,542,310!2029-03-27,1178,350!2027-12-26,810,330!2029-09-23,1322,350!2027-11-13,776,330!2026-09-03,431,310!2029-10-13,1338,350-->

## examples

### commutative rings

> {@{![The category of commutative rings admits pullbacks.](../../archives/Wikimedia%20Commons/Pullback%20commutative%20rings.svg)}@}
>
> {@{The category of commutative rings admits pullbacks}@}. <!--SR:!2027-11-20,782,330!2028-01-14,811,330-->

In {@{the [category of commutative rings](category%20of%20commutative%20rings.md#category%20of%20commutative%20rings) \(with identity\)}@}, the pullback is called {@{the fibered product}@}. Let {@{_A_, _B_, and _C_ be [commutative rings](commutative%20ring.md) \(with identity\) and _α_ : _A_ → _C_ and _β_ : _B_ → _C_ \(identity preserving\) [ring homomorphisms](ring%20homomorphism.md)}@}. Then {@{the pullback of this diagram exists}@} and is given by {@{the [subring](subring.md) of the [product ring](product%20ring.md) _A_ × _B_}@} defined by {@{$$A\times _{C}B=\left\{(a,b)\in A\times B\;{\big |}\;\alpha (a)=\beta (b)\right\}$$}@} along with {@{the morphisms $$\beta '\colon A\times _{C}B\to A,\qquad \alpha '\colon A\times _{C}B\to B$$}@} given by {@{$\beta '(a,b)=a$ and $\alpha '(a,b)=b$ for all $(a,b)\in A\times _{C}B$}@}. We then have {@{$$\alpha \circ \beta '=\beta \circ \alpha '.$$}@} <!--SR:!2026-07-06,355,290!2027-08-03,699,330!2027-06-03,540,270!2029-10-15,1340,350!2028-08-28,936,330!2028-09-12,948,330!2027-04-11,561,310!2027-06-21,666,330!2029-03-08,1159,350-->

### groups and modules

In {@{complete analogy to the example of commutative rings above}@}, one can show that {@{all pullbacks exist}@} in {@{the [category of groups](category%20of%20groups.md) and in the [category of modules](category%20of%20modules.md) over some fixed ring}@}. <!--SR:!2026-07-03,386,310!2029-10-20,1344,350!2026-05-13,335,290-->

### sets

In {@{the [category of sets](category%20of%20sets.md)}@}, {@{the pullback of functions _f_ : _X_ → _Z_ and _g_ : _Y_ → _Z_ always exists}@} and is given by {@{the set $$X\times _{Z}Y=\{(x,y)\in X\times Y|f(x)=g(y)\}=\bigcup _{z\in f(X)\cap g(Y)}f^{-1}[\{z\}]\times g^{-1}[\{z\}],$$}@} together with {@{the [restrictions](restriction%20(mathematics).md) of the [projection maps](projection%20map.md) _π_<sub>1</sub> and _π_<sub>2</sub> to _X_ ×<sub>_Z_</sub> _Y_}@}. <!--SR:!2029-09-18,1318,350!2029-05-12,1215,350!2026-02-21,281,290!2027-12-05,792,330-->

Alternatively one may view {@{the pullback in __Set__ asymmetrically}@}: {@{$$X\times _{Z}Y\cong \coprod _{x\in X}g^{-1}[\{f(x)\}]\cong \coprod _{y\in Y}f^{-1}[\{g(y)\}]$$}@} where {@{$\coprod$ is the [disjoint union](disjoint%20union.md) of sets}@} \(the involved sets are {@{not disjoint on their own unless _f_ resp. _g_ is [injective](injective.md)}@}\). In the first case, the projection _π_<sub>1</sub> {@{extracts the _x_ index while _π_<sub>2</sub> forgets the index, leaving elements of _Y_}@}. <!--SR:!2029-03-15,1166,350!2027-06-02,615,290!2028-09-06,944,330!2026-12-27,512,310!2027-11-25,772,330-->

This example motivates {@{another way of characterizing the pullback}@}: as {@{the [equalizer](equaliser%20(mathematics).md) of the morphisms _f_ ∘ _p_<sub>1</sub>, _g_ ∘ _p_<sub>2</sub> : _X_ × _Y_ → _Z_ where _X_ × _Y_ is the [binary product](product%20(category%20theory).md) of _X_ and _Y_ and _p_<sub>1</sub> and _p_<sub>2</sub> are the natural projections}@}. This shows that {@{pullbacks exist in any category with binary products and equalizers}@}. In fact, by {@{the [existence theorem for limits](existence%20theorem%20for%20limits.md#existence%20of%20limits)}@}, {@{all finite limits exist in a category with binary products and equalizers}@}; equivalently, {@{all finite limits exist in a category with terminal object and pullbacks}@} \(by the fact that {@{binary product is equal to pullback on the terminal object}@}, and that {@{an equalizer is a pullback involving binary product}@}\). <!--SR:!2029-09-20,1318,350!2026-02-21,249,270!2028-09-10,947,330!2028-12-27,1110,350!2027-01-02,493,310!2026-03-07,289,290!2028-12-28,1058,310!2026-08-18,423,310-->

#### graphs of functions

{@{A specific example of a pullback}@} is given by the {@{graph of a function}@}. Suppose that {@{$f\colon X\to Y$ is a function}@}. {@{The _graph_ of _f_}@} is {@{the set $$\Gamma _{f}=\{(x,f(x))\colon x\in X\}\subseteq X\times Y.$$}@} The graph can be reformulated as {@{the pullback of _f_ and the identity function on _Y_}@}. By definition, this pullback is {@{$$X\times _{f,Y,1_{Y} }Y=\{(x,y)\colon f(x)=1_{Y}(y)\}=\{(x,y)\colon f(x)=y\}\subseteq X\times Y,$$}@} and this {@{equals $\Gamma _{f}$}@}. <!--SR:!2029-10-03,1330,350!2029-03-04,1155,350!2029-01-09,1120,350!2029-07-06,1254,350!2029-06-07,1237,350!2027-03-27,537,310!2028-06-06,875,330!2027-10-12,751,330-->

### fiber bundles

Another example of a pullback comes from {@{the theory of [fiber bundles](fiber%20bundle.md)}@}: given {@{a bundle map _π_ : _E_ → _B_ and a [continuous map](continuous%20map.md) _f_ : _X_ → _B_}@}, the pullback \(formed in {@{the [category of topological spaces](category%20of%20topological%20spaces.md) with [continuous maps](continuous%20function%20(topology).md#continuous%20functions%20between%20topological%20spaces)}@}\) {@{_X_ ×<sub>_B_</sub> _E_}@} is {@{a fiber bundle over _X_ called the [pullback bundle](pullback%20bundle.md)}@}. {@{The associated commutative diagram}@} is {@{a morphism of fiber bundles}@}. This is also the case in {@{the category of differentiable manifolds}@}. A special case is {@{the pullback of two fiber bundles _E_<sub>_1_</sub>, _E_<sub>2</sub> → _B_}@}. In this case {@{_E_<sub>1</sub> × _E_<sub>2</sub>}@} is {@{a fiber bundle over _B × B_}@}, and {@{pulling back along the diagonal map _B_ → _B × B_}@} gives {@{a space homeomorphic \(diffeomorphic\) to _E_<sub>1</sub> ×<sub>_B_</sub> _E_<sub>2</sub>}@}, which is {@{a fiber bundle over _B_}@}. {@{The pullback of two smooth transverse maps into the same [differentiable manifold](differentiable%20manifold.md)}@} is {@{also a differentiable manifold}@}, and {@{the [tangent space](tangent%20space.md) of the pullback}@} is {@{the pullback of the tangent spaces along the differential maps}@}. <!--SR:!2028-09-27,1036,350!2027-02-07,543,310!2027-12-31,800,330!2026-03-24,297,290!2027-05-21,606,290!2027-07-11,682,330!2026-03-10,290,290!2026-03-21,294,290!2027-06-25,669,330!2029-03-30,1181,350!2029-10-10,1336,350!2027-11-24,785,330!2026-05-19,287,250!2027-02-15,548,310!2026-12-01,436,270!2026-02-25,252,270!2026-03-25,298,290!2027-03-23,534,310-->

### preimages and intersections

{@{[Preimages](preimage.md#inverse%20image) of sets under functions}@} can be {@{described as pullbacks as follows}@}: <!--SR:!2029-04-22,1195,350!2028-11-25,1085,350-->

Suppose {@{_f_ : _A_ → _B_, _B_<sub>0</sub> ⊆ _B_}@}. Let {@{_g_ be the [inclusion map](inclusion%20map.md) _B_<sub>0</sub> ↪ _B_}@}. Then {@{a pullback of _f_ and _g_ \(in __Set__\)}@} is given by {@{the preimage _f_<sup>−1</sup>\[_B_<sub>0</sub>\]}@} together with {@{the inclusion of the preimage in _A_ <p> &emsp; _f_<sup>−1</sup>\[_B_<sub>0</sub>\] ↪ _A_ <p> and the restriction of _f_ to _f_<sup>−1</sup>\[_B_<sub>0</sub>\] <p> &emsp; _f_<sup>−1</sup>\[_B_<sub>0</sub>\] → _B_<sub>0</sub>}@}. <!--SR:!2029-09-23,1321,350!2029-09-10,1312,350!2029-07-15,1263,350!2029-03-09,1160,350!2027-04-06,558,310-->

Because of {@{this example}@}, in {@{a general category}@} {@{the pullback of a morphism _f_ and a [monomorphism](monomorphism.md) _g_}@} can be thought of as {@{the "preimage" under _f_ of the [subobject](subobject.md) specified by _g_}@}. Similarly, {@{pullbacks of two monomorphisms}@} can be thought of as {@{the "intersection" of the two subobjects}@}. <!--SR:!2029-03-13,1164,350!2028-12-10,1097,350!2027-02-13,546,310!2027-05-29,612,290!2029-03-14,1165,350!2026-07-04,353,290-->

### least common multiple

Consider {@{the multiplicative [monoid](monoid.md) of positive [integers](integer.md) __Z__<sub>+</sub> as a category with one object (annotation: morphisms are the positive integers; composition of morphisms is multiplication)}@}. In this category, {@{the pullback of two positive integers _m_ and _n_}@} is {@{just the pair $\left({\frac {\operatorname {lcm} (m,n)}{m} },{\frac {\operatorname {lcm} (m,n)}{n} }\right)$}@}, where {@{the numerators are both the [least common multiple](least%20common%20multiple.md) of _m_ and _n_}@}. The same pair is {@{also the pushout}@}. <!--SR:!2026-09-28,451,310!2028-07-25,908,330!2029-03-03,1154,350!2027-02-01,513,310!2027-11-11,762,330-->

## properties

- In {@{any category with a [terminal object](terminal%20object.md) _T_}@}, {@{the pullback _X_ ×<sub>_T_</sub> _Y_}@} is {@{just the ordinary [product](product%20(category%20theory).md) _X_ × _Y_}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2027-02-25,480,394!2027-02-15,473,394!2027-02-26,481,394-->

- {@{[Monomorphisms](monomorphism.md)}@} are {@{stable under pullback}@}: if {@{the arrow _f_ in the diagram is monic}@}, then so is {@{the arrow _p_<sub>2</sub>}@}. Similarly, if {@{_g_ is monic, then so is _p_<sub>1</sub>}@}.<sup>[\[3\]](#^ref-3)</sup> \(annotation: {@{_p_<sub>2</sub> and _p_<sub>1</sub>}@} are {@{respectively arrows opposite to _f_ or _g_ in the commutative diagram}@}.\) <!--SR:!2027-02-19,476,394!2027-02-17,474,394!2027-02-18,475,394!2027-02-08,466,394!2027-02-20,476,394!2027-02-06,465,394!2027-02-02,461,394-->

- {@{[Isomorphisms](isomorphism.md)}@} are {@{also stable}@}, and hence, for example, {@{_X_ ×<sub>_X_</sub> _Y_ ≅ _Y_ for any map _Y_ → _X_}@} \(where {@{the implied map _X_ → _X_ is the identity}@}\). <!--SR:!2027-03-04,486,394!2027-03-02,485,394!2027-03-05,487,394!2027-02-26,482,394-->

- In {@{an [abelian category](abelian%20category.md) all pullbacks exist}@},<sup>[\[4\]](#^ref-4)</sup> and they {@{preserve [kernels](kernel%20(category%20theory).md), in the following sense}@}: {@{if <p> ![categorical pullback commutative diagram](../../archives/Wikimedia%20Commons/Categorical%20pullback.svg) <p> is a pullback diagram}@}, then {@{the induced morphism ker\(_p_<sub>2</sub>\) → ker\(_f_\) is an isomorphism}@},<sup>[\[5\]](#^ref-5)</sup> and so is {@{the induced morphism ker\(_p_<sub>1</sub>\) → ker\(_g_\)}@}. {@{Every pullback diagram}@} thus {@{gives rise to a commutative diagram of the following form}@}, where {@{all rows and columns are [exact](exact%20sequence.md)}@}: {@{$${\begin{array}{ccccccc}&&&&0&&0\\&&&&\downarrow &&\downarrow \\&&&&L&=&L\\&&&&\downarrow &&\downarrow \\0&\rightarrow &K&\rightarrow &P&\rightarrow &Y\\&&\parallel &&\downarrow &&\downarrow \\0&\rightarrow &K&\rightarrow &X&\rightarrow &Z\end{array} }$$}@} Furthermore, in {@{an abelian category}@}, {@{if _X_ → _Z_ is an epimorphism, then so is its pullback _P_ → _Y_}@}, and {@{symmetrically: if _Y_ → _Z_ is an epimorphism, then so is its pullback _P_ → _X_}@}.<sup>[\[6\]](#^ref-6)</sup> In these situations, {@{the pullback square is also a pushout square}@}.<sup>[\[7\]](#^ref-7)</sup> <!--SR:!2029-03-28,1179,350!2028-09-28,960,330!2026-10-03,238,250!2026-05-18,286,250!2029-02-21,1144,350!2028-09-13,949,330!2027-12-12,800,330!2026-12-07,495,310!2026-03-05,293,310!2028-04-29,893,330!2027-05-11,567,310!2028-02-19,800,330!2026-03-29,114,387-->

- There is {@{a natural isomorphism \(_A_<!-- markdown separator -->×<sub>_C_</sub>_B_\)×<sub>_B_</sub> _D_ ≅ _A_<!-- markdown separator -->×<sub>_C_</sub>_D_}@}. Explicitly, this means:
  - if maps _f_ : _A_ → _C_, _g_ : _B_ → _C_ and _h_ : _D_ → _B_ are given and
  - the pullback of _f_ and _g_ is given by _r_ : _P_ → _A_ and _s_ : _P_ → _B_, and
  - the pullback of _s_ and _h_ is given by _t_ : _Q_ → _P_ and _u_ : _Q_ → _D_ ,
  - then the pullback of _f_ and _gh_ is given by _rt_ : _Q_ → _A_ and _u_ : _Q_ → _D_. <!--SR:!2026-02-25,249,270-->

  Graphically this means that {@{two pullback squares, placed side by side and sharing one morphism}@}, form {@{a larger pullback square when ignoring the inner shared morphism}@}. {@{$${\begin{array}{ccccc}Q&{\xrightarrow {t} }&P&{\xrightarrow {r} }&A\\\downarrow _{u}&&\downarrow _{s}&&\downarrow _{f}\\D&{\xrightarrow {h} }&B&{\xrightarrow {g} }&C\end{array} }$$}@} <!--SR:!2027-02-07,465,394!2027-02-01,461,394!2027-02-27,483,394-->

- {@{Any category with pullbacks and products}@} {@{has equalizers}@}. <!--SR:!2029-06-02,1232,350!2026-05-21,340,290-->

## weak pullbacks

{@{A __weak pullback__ of a [cospan](span%20(category%20theory).md) _X_ → _Z_ ← _Y_}@} is {@{a [cone](cone%20(category%20theory).md) over the cospan that is only [weakly universal](weakly%20universal%20property.md)}@}, that is, {@{the mediating morphism _u_ : _Q_ → _P_ above is not required to be unique}@}. <!--SR:!2029-10-14,1339,350!2026-09-16,443,310!2029-01-14,1124,350-->

## see also

- [Pullbacks in differential geometry](pullback%20(differential%20geometry).md)
- [Equijoin](relational%20algebra.md#%CE%B8-join%20and%20equijoin) in [relational algebra](relational%20algebra.md)
- [Fiber product of schemes](fiber%20product%20of%20schemes.md)

## notes

1. Mitchell, p. 9 <a id="^ref-1"></a>^ref-1
2. Adámek, p. 197. <a id="^ref-2"></a>^ref-2
3. Mitchell, p. 9 <a id="^ref-3"></a>^ref-3
4. Mitchell, p. 32 <a id="^ref-4"></a>^ref-4
5. Mitchell, p. 15 <a id="^ref-5"></a>^ref-5
6. Mitchell, p. 34 <a id="^ref-6"></a>^ref-6
7. Mitchell, p. 39 <a id="^ref-7"></a>^ref-7

## references

This text incorporates [content](https://en.wikipedia.org/wiki/pullback_(category_theory)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- Adámek, Jiří, [Herrlich, Horst](Horst%20Herrlich.md), & Strecker, George E.; \(1990\). [_Abstract and Concrete Categories_](http://katmat.math.uni-bremen.de/acc/acc.pdf) \(4.2MB PDF\). Originally publ. John Wiley & Sons. [ISBN](ISBN%20(identifier).md) [0-471-60922-6](https://en.wikipedia.org/wiki/Special:BookSources/0-471-60922-6). \(now free on-line edition\).
- [Cohn, Paul M.](Paul%20Cohn.md); _Universal Algebra_ \(1981\), D. Reidel Publishing, Holland, [ISBN](ISBN%20(identifier).md) [90-277-1213-1](https://en.wikipedia.org/wiki/Special:BookSources/90-277-1213-1) _\(Originally published in 1965, by Harper & Row\)_.
- <a id="CITEREFMitchell1965"></a> Mitchell, Barry \(1965\). _Theory of Categories_. Academic Press.

## external links

- [Interactive web page](https://web.archive.org/web/20080916162345/http://www.j-paine.org/cgi-bin/webcats/webcats.php) which generates examples of pullbacks in the category of finite sets. Written by Jocelyn Paine.
- [pullback](https://ncatlab.org/nlab/show/pullback) at the [_n_<!-- markdown separator -->Lab](nLab.md)

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
