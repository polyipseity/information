---
aliases:
  - characteristic function
  - characteristic function (convex analysis)
  - characteristic functions
  - characteristic functions (convex analysis)
tags:
  - flashcard/active/general/eng/characteristic_function__convex_analysis_
  - language/in/English
---

# characteristic function

<!-- | ![](../../archives/Wikimedia%20Commons/Text%20document%20with%20red%20question%20mark.svg) | This article includes a [list of references](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources), [related reading](https://en.wikipedia.org/wiki/Wikipedia:Further%20reading), or [external links](https://en.wikipedia.org/wiki/Wikipedia:External%20links), __but its sources remain unclear because it lacks [inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#Inline%20citations)__. Please help [improve](https://en.wikipedia.org/wiki/Wikipedia:WikiProject%20Reliability) this article by [introducing](https://en.wikipedia.org/wiki/Wikipedia:When%20to%20cite) more precise citations. _\(October 2011\)__ \([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

In {@{the field of [mathematics](mathematics.md) known as [convex analysis](convex%20analysis.md)}@}, {@{the __characteristic function__ of a set}@} is {@{a [convex function](convex%20function.md) that indicates the membership \(or non-membership\) of a given element in that set}@}. It is similar to {@{the usual [indicator function](indicator%20function.md)}@}, and one can {@{freely convert between the two}@}, but {@{the characteristic function as defined below is better-suited to the methods of convex analysis}@}. <!--SR:!2025-03-28,66,310!2025-03-06,44,290!2025-02-15,33,270!2025-03-18,58,310!2025-03-27,65,310!2025-03-15,55,310-->

## definition

Let {@{$X$ be a [set](set%20(mathematics).md), and let $A$ be a [subset](subset.md) of $X$}@}. The __characteristic function__ of $A$ is the function {@{$$\chi _{A}:X\to \mathbb {R} \cup \{+\infty \}$$}@} taking {@{values in the [extended real number line](extended%20real%20number%20line.md) defined by $$\chi _{A}(x):={\begin{cases}0,&x\in A;\\+\infty ,&x\not \in A.\end{cases} }$$}@} <!--SR:!2025-03-21,60,310!2025-03-23,62,310!2025-03-17,57,310-->

## relationship with the indicator function

Let {@{$\mathbf {1} _{A}:X\to \mathbb {R}$}@} denote {@{the usual indicator function: $$\mathbf {1} _{A}(x):={\begin{cases}1,&x\in A;\\0,&x\not \in A.\end{cases} }$$}@} If one adopts the conventions that (annotation: the conventions are {@{related to arithmetic operations and infinities}@}) <!--SR:!2025-03-27,65,310!2025-03-22,61,310!2025-03-18,58,310-->

- (annotation: multiplication with positive infinity) ::@:: for any $a\in \mathbb {R} \cup \{+\infty \}$, $a+(+\infty )=+\infty$ and $a(+\infty )=+\infty$, except $0(+\infty )=0$; <!--SR:!2025-03-22,61,310!2025-03-29,67,310-->
- (annotation: division by 0) ::@:: ${\frac {1}{0} }=+\infty$; and <!--SR:!2025-03-17,57,310!2025-03-21,60,310-->
- (annotation: division by positive infinity) ::@:: ${\frac {1}{+\infty } }=0$; <!--SR:!2025-03-16,56,310!2025-03-24,63,310-->

then {@{the indicator and characteristic functions are related}@} by {@{the equations $$\mathbf {1} _{A}(x)={\frac {1}{1+\chi _{A}(x)} }$$ and $$\chi _{A}(x)=(+\infty )\left(1-\mathbf {1} _{A}(x)\right).$$}@} <!--SR:!2025-03-29,67,310!2025-03-27,65,310-->

## subgradient

{@{The [subgradient](subderivative.md) (annotation: i.e. subderivative, a generalization of the _derivative_ to convex functions at _non-differentiable points_) of $\chi _{A}(x)$ for a set $A$}@} is {@{the [tangent cone](tangent%20cone.md) (annotation: a generalization of _tangent space_ to a manifold to the case of certain spaces with _singularities_) of that set in $x$}@}. <!--SR:!2025-02-06,24,250!2025-02-05,23,250-->

## bibliography

This text incorporates [content](https://en.wikipedia.org/wiki/characteristic_function_(convex_analysis)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFRockafellar1997"></a> [Rockafellar, R. T.](R.%20Tyrrell%20Rockafellar.md) \(1997\) \[1970\]. _Convex Analysis_. Princeton, NJ: Princeton University Press. [ISBN](ISBN.md) [978-0-691-01586-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-691-01586-6).

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Convex analysis](https://en.wikipedia.org/wiki/Category:Convex%20analysis)
