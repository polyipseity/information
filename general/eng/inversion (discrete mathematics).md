---
aliases:
  - inversion
  - inversion (discrete mathematics)
  - inversions
  - inversions (discrete mathematics)
tags:
  - flashcard/active/general/eng/inversion__discrete_mathematics_
  - language/in/English
---

# inversion

> {@{![Permutation with one of its inversions highlighted.](../../archives/Wikimedia%20Commons/Inversion%20qtl1.svg)}@}
>
> {@{Permutation with one of its inversions highlighted}@}. An inversion may be denoted by {@{the pair of places \(2, 4\) or the pair of elements \(5, 2\)}@}. {@{The inversions of this permutation using element-based notation}@} are: {@{\(3, 1\), \(3, 2\), \(5, 1\), \(5, 2\), and \(5,4\)}@}. <!--SR:!2025-01-26,46,292!2025-02-23,68,312!2025-02-23,68,312!2025-01-31,45,292!2025-02-14,62,312-->

In {@{[computer science](computer%20science.md) and [discrete mathematics](discrete%20mathematics.md)}@}, {@{an __inversion__}@} in {@{a sequence is a pair of elements that are out of their natural [order](total%20order.md)}@}. <!--SR:!2025-02-13,61,312!2025-02-16,64,312!2025-02-16,64,312-->

## definitions

<!-- markdownlint-disable-next-line MD024 -->
### inversion

Let {@{$\pi$ be a [permutation](permutation.md)}@}. There is {@{an __inversion__ of $\pi$ between $i$ and $j$}@} if {@{$i<j$ and $\pi (i)>\pi (j)$}@}. The inversion is indicated by {@{an ordered pair containing either the places $(i,j)$<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup> or the elements ${\bigl (}\pi (i),\pi (j){\bigr )}$}@}.<sup>[\[3\]](#^ref-3)</sup><sup>[\[4\]](#^ref-4)</sup><sup>[\[5\]](#^ref-5)</sup> <!--SR:!2025-02-23,68,312!2025-02-21,66,312!2025-02-23,68,312!2025-02-20,65,312-->

{@{The [inversion set](#example%20all%20permutations%20of%20four%20elements)}@} is {@{the set of all inversions}@}. {@{A permutation's inversion set using place-based notation}@} is {@{the same as the [inverse permutation's](permutation.md#definition) inversion set using element-based notation}@} with {@{the two components of each ordered pair exchanged}@}. Likewise, {@{a permutation's inversion set using element-based notation}@} is {@{the same as the inverse permutation's inversion set using place-based notation}@} with {@{the two components of each ordered pair exchanged}@}.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2025-02-19,67,310!2025-02-04,49,292!2025-02-23,68,312!2025-02-23,68,312!2025-02-13,61,312!2025-01-26,43,292!2025-02-16,64,312!2025-02-23,68,312-->

Inversions are usually defined for {@{permutations, but may also be defined for sequences}@}: Let {@{$S$ be a [sequence](sequence.md) \(or [multiset](multiset.md) permutation<sup>[\[7\]](#^ref-7)</sup>\)}@}. If {@{$i<j$ and $S(i)>S(j)$}@}, {@{either the pair of places $(i,j)$<sup>[\[7\]](#^ref-7)</sup><sup>[\[8\]](#^ref-8)</sup> or the pair of elements ${\bigl (}S(i),S(j){\bigr )}$}@}<sup>[\[9\]](#^ref-9)</sup> is {@{called an inversion of $S$}@}. <!--SR:!2025-02-16,64,312!2025-02-16,64,312!2025-02-20,65,312!2025-02-15,63,312!2025-02-16,64,312-->

For sequences, {@{inversions according to the element-based definition are not unique}@}, because {@{different pairs of places may have the same pair of values}@}. <!--SR:!2025-01-16,39,292!2025-02-23,68,312-->

### inversion number

{@{The __inversion number__ ${\mathtt {inv} }(X)$<sup>[\[10\]](#^ref-10)</sup>}@} of {@{a sequence $X=\langle x_{1},\dots ,x_{n}\rangle$}@}, is {@{the [cardinality](cardinality.md) of the inversion set}@}. It is {@{a common measure of sortedness \(sometimes called presortedness\) of a permutation<sup>[\[5\]](#^ref-5)</sup> or sequence}@}.<sup>[\[9\]](#^ref-9)</sup> The inversion number is {@{between 0 and ${\frac {n(n-1)}{2} }$ inclusive}@}. {@{A permutation and its inverse}@} have {@{the same inversion number}@}. <!--SR:!2025-02-15,63,312!2025-02-16,64,312!2025-02-01,46,292!2025-02-16,64,312!2025-02-15,63,312!2025-02-15,63,312!2025-02-23,68,312-->

For example {@{${\mathtt {inv} }(\langle 1,2,\dots ,n\rangle )=0$}@} since {@{the sequence is ordered}@}. Also, {@{when $n=2m$ is even}@}, {@{${\mathtt {inv} }(\langle m+1,m+2,\dots ,2m,1,2,\dots ,m\rangle )=m^{2}$}@} \(because {@{each pair $(1\leq i\leq m<j\leq 2m)$ is an inversion}@}\). This last example shows that {@{a set that is intuitively "nearly sorted" can still have a quadratic number of inversions}@}. <!--SR:!2025-01-27,47,292!2025-02-23,68,312!2025-02-23,68,312!2025-02-03,48,292!2025-02-23,68,312!2025-02-16,64,312-->

{@{The inversion number}@} is {@{the number of crossings in the arrow diagram of the permutation}@},<sup>[\[6\]](#^ref-6)</sup> {@{the permutation's [Kendall tau distance](Kendall%20tau%20distance.md) from the identity permutation}@}, and {@{the sum of each of the inversion related vectors defined below}@}. <!--SR:!2025-02-16,64,312!2025-02-02,47,292!2025-01-14,34,272!2025-02-23,68,312-->

{@{Other measures of sortedness}@} include {@{the minimum number of elements that can be deleted from the sequence to yield a fully sorted sequence}@}, {@{the number and lengths of sorted "runs" within the sequence}@}, {@{the Spearman footrule \(sum of distances of each element from its sorted position\)}@}, and {@{the smallest number of exchanges needed to sort the sequence}@}.<sup>[\[11\]](#^ref-11)</sup> {@{Standard [comparison sorting](comparison%20sort.md) algorithms}@} can be {@{adapted to compute the inversion number in time O\(_n_ log _n_\)}@}.<sup>[\[12\]](#^ref-12)</sup> <!--SR:!2025-02-16,64,312!2025-02-14,62,312!2025-02-21,66,312!2025-02-01,46,292!2025-02-23,68,312!2025-02-20,65,312!2025-02-19,64,312-->

### inversion related vectors

{@{Three similar vectors are in use}@} that {@{condense the inversions of a permutation into a vector that uniquely determines it}@}. They are often called {@{_inversion vector_ or _[Lehmer code](lehmer%20code.md)_}@}. \(A list of sources is found [here](https://en.wikiversity.org/wiki/Inversion%20(discrete%20mathematics)).\) <!--SR:!2025-02-22,67,312!2025-02-14,62,312!2025-02-16,64,312-->

This article uses {@{the term _inversion vector_ \($v$\) like [Wolfram](Wolfram%20Mathematica.md)}@}.<sup>[\[13\]](#^ref-13)</sup> {@{The remaining two vectors}@} are {@{sometimes called _left_ and _right inversion vector_}@}, but to {@{avoid confusion with the inversion vector}@} this article calls them {@{_left inversion count_ \($l$\) and _right inversion count_ \($r$\)}@}. Interpreted as {@{a [factorial number](factorial%20number%20system.md)}@} {@{the left inversion count gives the permutations reverse colexicographic}@},<sup>[\[14\]](#^ref-14)</sup> and {@{the right inversion count gives the lexicographic index}@}. <!--SR:!2025-02-23,68,312!2025-02-15,63,312!2025-02-23,68,312!2025-02-23,68,312!2025-02-23,68,312!2025-02-23,68,312!2025-01-19,11,212!2025-02-23,68,312-->

> {@{![Rothe diagram of \(2, 5, 4, 6, 3, 1\)](../../archives/Wikimedia%20Commons/Inversion%20example;%20Rothe%201.svg)}@}
>
> {@{Rothe diagram of \(2, 5, 4, 6, 3, 1\)}@} (annotation: Try to figure out {@{how one constructs the above Rothe diagram from the given sequence}@}.) <!--SR:!2025-02-04,49,292!2025-02-14,62,312!2025-01-27,48,292-->

__Inversion vector $v$:__ ::@:: With the _element-based_ definition $v(i)$ is the number of inversions whose _smaller_ \(right\) component is $i$.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2025-01-14,34,272!2025-01-14,34,272-->

- inversion vector, in words ::@:: $v(i)$ is the number of elements in $\pi$ greater than $i$ before $i$. <!--SR:!2025-03-13,71,272!2025-01-27,44,292-->
- inversion vector, symbolically ::@:: $$v(i)~~=~~\#\{k\mid k>i~\land ~\pi ^{-1}(k)<\pi ^{-1}(i)\}$$ <!--SR:!2025-01-14,34,272!2025-01-25,45,292-->

__Left inversion count $l$:__ ::@:: With the _place-based_ definition $l(i)$ is the number of inversions whose _bigger_ \(right\) component is $i$. <!--SR:!2025-02-17,52,252!2025-02-16,64,312-->

- left inversion count, in words ::@:: $l(i)$ is the number of elements in $\pi$ greater than $\pi (i)$ before $\pi (i)$. <!--SR:!2025-03-10,73,272!2025-02-16,64,312-->
- left inversion count, symbolically ::@:: $$l(i)~~=~~\#\left\{k\mid k<i~\land ~\pi (k)>\pi (i)\right\}$$ <!--SR:!2025-02-13,61,312!2025-02-17,52,252-->

__Right inversion count $r$, often called _[Lehmer code](lehmer%20code.md)_:__ ::@:: With the _place-based_ definition $r(i)$ is the number of inversions whose _smaller_ \(left\) component is $i$. <!--SR:!2025-03-28,79,272!2025-01-12,33,272-->

- right inversion count, in words ::@:: $r(i)$ is the number of elements in $\pi$ smaller than $\pi (i)$ after $\pi (i)$. <!--SR:!2025-01-26,43,292!2025-01-31,45,292-->
- right inversion count, symbolically ::@:: $$r(i)~~=~~\#\{k\mid k>i~\land ~\pi (k)<\pi (i)\}$$ <!--SR:!2025-02-04,49,292!2025-01-25,42,292-->

{@{Both $v$ and $r$}@} can be {@{found with the help of a [Rothe diagram](permutation.md#numbering%20permutations)}@}, which is {@{a [permutation matrix](permutation%20matrix.md)}@} with {@{the 1s represented by dots}@}, and {@{an inversion \(often represented by a cross\) in every position that has a dot to the right and below it}@}. $r(i)$ is the sum of inversions in row $i$ of the Rothe diagram, while $v(i)$ is the sum of inversions in column $i$. The permutation matrix of the inverse is the transpose, therefore $v$ of a permutation is $r$ of its inverse, and vice versa. <!--SR:!2025-02-16,64,312!2025-01-27,47,292!2025-01-19,40,292!2025-02-16,64,312!2025-02-03,48,292-->

## example: all permutations of four elements

> {@{![The six possible inversions of a 4-element permutation](../../archives/Wikimedia%20Commons/2-element%20subsets%20of%204%20elements;%20array,%20hexagonal.svg)}@}
>
> {@{The six possible inversions of a 4-element permutation}@} <!--SR:!2025-02-23,68,312!2025-02-02,47,292-->

{@{The following sortable table}@} shows {@{the 24 permutations of four elements \(in the $\pi$ column\)}@} with {@{their place-based inversion sets \(in the p-b column\), inversion related vectors \(in the $v$, $l$, and $r$ columns\), and inversion numbers \(in the \# column\)}@}. \({@{The columns with smaller print and no heading}@} are {@{reflections of the columns next to them}@}, and can be used to {@{sort them in [colexicographic order](lexicographic%20order.md#colexicographic%20order)}@}.\) <!--SR:!2025-02-13,61,312!2025-02-14,62,312!2025-01-27,44,292!2025-02-16,64,312!2025-02-14,62,312!2025-04-29,111,292-->

It can be seen that {@{$v$ and $l$ always have the same digits}@}, and that {@{$l$ and $r$ are both related to the place-based inversion set}@}. {@{The nontrivial elements of $l$}@} are {@{the sums of the descending diagonals of the shown triangle}@}, and {@{those of $r$}@} are {@{the sums of the ascending diagonals}@}. \({@{Pairs in descending diagonals}@} have {@{the right components 2, 3, 4 in common}@}, while {@{pairs in ascending diagonals}@} have {@{the left components 1, 2, 3 in common}@}.\) <!--SR:!2025-01-28,45,292!2025-02-22,67,312!2025-02-13,61,312!2025-02-15,63,312!2025-02-16,64,312!2025-01-25,42,292!2025-01-25,42,292!2025-01-16,39,292!2025-01-11,32,272!2025-02-23,68,312-->

{@{The default order of the table}@} is {@{reverse colex order by $\pi$, which is the same as colex order by $l$}@}. {@{Lex order by $\pi$ is the same as lex order by $r$}@}. <!--SR:!2025-02-23,68,312!2025-02-17,52,252!2025-02-23,68,312-->

> {@{__3-element permutations for comparison__}@}
>
> |                                                   | &nbsp;&nbsp;&nbsp;&nbsp;                                                                           | $\pi$               |                                    | $v$                                                                                 |                                                                                                    |                                                                                                    | $l$                                                                                 | p-b                                                                                            | $r$                                                                                 |                                                                                                    | \#                                 |
> |:-------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|:-------------------:|:----------------------------------:|:-----------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|:----------------------------------:|
> | __0__                                             | ![permutation matrix of \(1, 2, 3\)](../../archives/Wikimedia%20Commons/3-el%20perm%20matrix%200.svg) | __1&nbsp;2&nbsp;3__ | __<small>3&nbsp;2&nbsp;1</small>__ | <span style="color: red;">0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0</span></small> | <small><span style="color: red;">0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0</span> | ![inversion map of \(1, 2, 3\)](../../archives/Wikimedia%20Commons/3-el%20perm%20invset%2000.svg) | <span style="color: red;">0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0</span></small> | <span style="color: red;">0</span> |
> | <span style="background-color: #33eb2a;">1</span> | ![permutation matrix of \(2, 1, 3\)](../../archives/Wikimedia%20Commons/3-el%20perm%20matrix%201.svg) | __2&nbsp;1&nbsp;3__ | __<small>3&nbsp;1&nbsp;2</small>__ | <span style="color: red;">1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1</span></small> | <small><span style="color: red;">0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0</span> | ![inversion map of \(2, 1, 3\)](../../archives/Wikimedia%20Commons/3-el%20perm%20invset%2001.svg) | <span style="color: red;">1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1</span></small> | <span style="color: red;">1</span> |
> | <span style="background-color: #33eb2a;">2</span> | ![permutation matrix of \(1, 3, 2\)](../../archives/Wikimedia%20Commons/3-el%20perm%20matrix%202.svg) | __1&nbsp;3&nbsp;2__ | __<small>2&nbsp;3&nbsp;1</small>__ | <span style="color: red;">0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0</span></small> | <small><span style="color: red;">1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1</span> | ![inversion map of \(1, 3, 2\)](../../archives/Wikimedia%20Commons/3-el%20perm%20invset%2002.svg) | <span style="color: red;">0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0</span></small> | <span style="color: red;">1</span> |
> | 3                                                 | ![permutation matrix of \(3, 1, 2\)](../../archives/Wikimedia%20Commons/3-el%20perm%20matrix%203.svg) | __3&nbsp;1&nbsp;2__ | __<small>2&nbsp;1&nbsp;3</small>__ | <span style="color: red;">1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1</span></small> | <small><span style="color: red;">1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1</span> | ![inversion map of \(3, 1, 2\)](../../archives/Wikimedia%20Commons/3-el%20perm%20invset%2003.svg) | <span style="color: red;">2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2</span></small> | <span style="color: red;">2</span> |
> | 4                                                 | ![permutation matrix of \(2, 3, 1\)](../../archives/Wikimedia%20Commons/3-el%20perm%20matrix%204.svg) | __2&nbsp;3&nbsp;1__ | __<small>1&nbsp;3&nbsp;2</small>__ | <span style="color: red;">2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2</span></small> | <small><span style="color: red;">2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2</span> | ![inversion map of \(2, 3, 1\)](../../archives/Wikimedia%20Commons/3-el%20perm%20invset%2004.svg) | <span style="color: red;">1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1</span></small> | <span style="color: red;">2</span> |
> | <span style="background-color: #33eb2a;">5</span> | ![permutation matrix of \(3, 2, 1\)](../../archives/Wikimedia%20Commons/3-el%20perm%20matrix%205.svg) | __3&nbsp;2&nbsp;1__ | __<small>1&nbsp;2&nbsp;3</small>__ | <span style="color: red;">2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2</span></small> | <small><span style="color: red;">2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2</span> | ![inversion map of \(3, 2, 1\)](../../archives/Wikimedia%20Commons/3-el%20perm%20invset%2005.svg) | <span style="color: red;">2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2</span></small> | <span style="color: red;">3</span> | <!--SR:!2025-02-23,68,312-->

<!--
```Python
from itertools import permutations

def main():
    orig = tuple(range(1, 4))
    pers = tuple(tuple(reversed(z)) for z in permutations(reversed(orig)))
    p_mat_name = "../../archives/Wikimedia%20Commons/3-el%20perm%20matrix%20{:01d}.svg"
    p_invmap_name = "../../archives/Wikimedia%20Commons/3-el%20perm%20invset%20{:02d}.svg"

    def v(p):
        return tuple(sum(1 for j in p[: p.index(i)] if j > i) for i in orig)

    def l(p):
        return tuple(sum(1 for j in p[:i] if j > p[i]) for i in range(len(orig)))

    def r(p):
        return tuple(sum(1 for j in p[i + 1 :] if j < p[i]) for i in range(len(orig)))

    def str_vlr(nums, reverse=False, *, l=False):
        nums = list(map(str, nums))
        nums[0 if l else -1] = (
            f'<span style="opacity: 0.3;">{nums[0 if l else -1]}</span>'
        )
        return "&nbsp;".join(reversed(nums) if reverse else nums)

    print(
        R"""
| | | $\pi$ | | $v$ | | | $l$ | p-b | $r$ | | \# |
|-|-|-------|-|-----|-|-|-----|-----|-----|-|----|""".lstrip()
    )
    for idx, p in enumerate(pers):
        v0, l0, r0 = v(p), l(p), r(p)
        assert sum(v0) == sum(l0)
        assert sum(l0) == sum(r0)
        cells = (
            str(idx),
            f"![permutation matrix of \\({', '.join(map(str, p))}\\)]({p_mat_name.format(idx)})",
            f"__{'&nbsp;'.join(map(str, p))}__",
            f"__<small>{'&nbsp;'.join(map(str, reversed(p)))}</small>__",
            f'<span style="color: red;">{str_vlr(v0)}</span>',
            f'<small><span style="color: red;">{str_vlr(v0, True)}</span></small>',
            f'<small><span style="color: red;">{str_vlr(l0, True, l=True)}</span></small>',
            f'<span style="color: red;">{str_vlr(l0, l=True)}</span>',
            f"![inversion map of \\({', '.join(map(str, p))}\\)]({p_invmap_name.format(idx)})",
            f'<span style="color: red;">{str_vlr(r0)}</span>',
            f'<small><span style="color: red;">{str_vlr(r0, True)}</span></small>',
            f'<span style="color: red;">{sum(v0)}</span>',
        )
        print(Rf"| {' | '.join(cells)} |")

if __name__ == "__main__":
    main()
```
-->

|                                                    | &nbsp;&nbsp;&nbsp;&nbsp;                                                                               | $\pi$                      |                                           | $v$                                                                                        |                                                                                                           |                                                                                                           | $l$                                                                                        | p-b                                                                                               | $r$                                                                                        |                                                                                                           | \#                                 |
|:--------------------------------------------------:|:------------------------------------------------------------------------------------------------------:|:--------------------------:|:-----------------------------------------:|:------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|:----------------------------------:|
| __0__                                              | ![permutation matrix of \(1, 2, 3, 4\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2000.svg) | __1&nbsp;2&nbsp;3&nbsp;4__ | __<small>4&nbsp;3&nbsp;2&nbsp;1</small>__ | <span style="color: red;">0&nbsp;0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0&nbsp;0</span></small> | <small><span style="color: red;">0&nbsp;0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0&nbsp;0</span> | ![inversion map of \(1, 2, 3, 4\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2000.svg) | <span style="color: red;">0&nbsp;0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0&nbsp;0</span></small> | <span style="color: red;">0</span> |
| <span style="background-color: #33eb2a;">1</span>  | ![permutation matrix of \(2, 1, 3, 4\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2001.svg) | __2&nbsp;1&nbsp;3&nbsp;4__ | __<small>4&nbsp;3&nbsp;1&nbsp;2</small>__ | <span style="color: red;">1&nbsp;0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0&nbsp;1</span></small> | <small><span style="color: red;">0&nbsp;0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0&nbsp;0</span> | ![inversion map of \(2, 1, 3, 4\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2001.svg) | <span style="color: red;">1&nbsp;0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0&nbsp;1</span></small> | <span style="color: red;">1</span> |
| <span style="background-color: #33eb2a;">2</span>  | ![permutation matrix of \(1, 3, 2, 4\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2002.svg) | __1&nbsp;3&nbsp;2&nbsp;4__ | __<small>4&nbsp;2&nbsp;3&nbsp;1</small>__ | <span style="color: red;">0&nbsp;1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1&nbsp;0</span></small> | <small><span style="color: red;">0&nbsp;1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1&nbsp;0</span> | ![inversion map of \(1, 3, 2, 4\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2002.svg) | <span style="color: red;">0&nbsp;1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1&nbsp;0</span></small> | <span style="color: red;">1</span> |
| 3                                                  | ![permutation matrix of \(3, 1, 2, 4\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2003.svg) | __3&nbsp;1&nbsp;2&nbsp;4__ | __<small>4&nbsp;2&nbsp;1&nbsp;3</small>__ | <span style="color: red;">1&nbsp;1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1&nbsp;1</span></small> | <small><span style="color: red;">0&nbsp;1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1&nbsp;0</span> | ![inversion map of \(3, 1, 2, 4\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2003.svg) | <span style="color: red;">2&nbsp;0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0&nbsp;2</span></small> | <span style="color: red;">2</span> |
| 4                                                  | ![permutation matrix of \(2, 3, 1, 4\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2004.svg) | __2&nbsp;3&nbsp;1&nbsp;4__ | __<small>4&nbsp;1&nbsp;3&nbsp;2</small>__ | <span style="color: red;">2&nbsp;0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0&nbsp;2</span></small> | <small><span style="color: red;">0&nbsp;2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2&nbsp;0</span> | ![inversion map of \(2, 3, 1, 4\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2004.svg) | <span style="color: red;">1&nbsp;1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1&nbsp;1</span></small> | <span style="color: red;">2</span> |
| <span style="background-color: #33eb2a;">5</span>  | ![permutation matrix of \(3, 2, 1, 4\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2005.svg) | __3&nbsp;2&nbsp;1&nbsp;4__ | __<small>4&nbsp;1&nbsp;2&nbsp;3</small>__ | <span style="color: red;">2&nbsp;1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1&nbsp;2</span></small> | <small><span style="color: red;">0&nbsp;2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2&nbsp;0</span> | ![inversion map of \(3, 2, 1, 4\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2005.svg) | <span style="color: red;">2&nbsp;1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1&nbsp;2</span></small> | <span style="color: red;">3</span> |
| <span style="background-color: #33eb2a;">6</span>  | ![permutation matrix of \(1, 2, 4, 3\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2006.svg) | __1&nbsp;2&nbsp;4&nbsp;3__ | __<small>3&nbsp;4&nbsp;2&nbsp;1</small>__ | <span style="color: red;">0&nbsp;0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0&nbsp;0</span></small> | <small><span style="color: red;">1&nbsp;0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0&nbsp;1</span> | ![inversion map of \(1, 2, 4, 3\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2006.svg) | <span style="color: red;">0&nbsp;0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0&nbsp;0</span></small> | <span style="color: red;">1</span> |
| __7__                                              | ![permutation matrix of \(2, 1, 4, 3\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2007.svg) | __2&nbsp;1&nbsp;4&nbsp;3__ | __<small>3&nbsp;4&nbsp;1&nbsp;2</small>__ | <span style="color: red;">1&nbsp;0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0&nbsp;1</span></small> | <small><span style="color: red;">1&nbsp;0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0&nbsp;1</span> | ![inversion map of \(2, 1, 4, 3\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2007.svg) | <span style="color: red;">1&nbsp;0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0&nbsp;1</span></small> | <span style="color: red;">2</span> |
| 8                                                  | ![permutation matrix of \(1, 4, 2, 3\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2008.svg) | __1&nbsp;4&nbsp;2&nbsp;3__ | __<small>3&nbsp;2&nbsp;4&nbsp;1</small>__ | <span style="color: red;">0&nbsp;1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1&nbsp;0</span></small> | <small><span style="color: red;">1&nbsp;1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1&nbsp;1</span> | ![inversion map of \(1, 4, 2, 3\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2008.svg) | <span style="color: red;">0&nbsp;2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2&nbsp;0</span></small> | <span style="color: red;">2</span> |
| <span style="background-color: #ffbb00;">9</span>  | ![permutation matrix of \(4, 1, 2, 3\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2009.svg) | __4&nbsp;1&nbsp;2&nbsp;3__ | __<small>3&nbsp;2&nbsp;1&nbsp;4</small>__ | <span style="color: red;">1&nbsp;1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1&nbsp;1</span></small> | <small><span style="color: red;">1&nbsp;1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1&nbsp;1</span> | ![inversion map of \(4, 1, 2, 3\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2009.svg) | <span style="color: red;">3&nbsp;0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0&nbsp;3</span></small> | <span style="color: red;">3</span> |
| <span style="background-color: #ffbb00;">10</span> | ![permutation matrix of \(2, 4, 1, 3\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2010.svg) | __2&nbsp;4&nbsp;1&nbsp;3__ | __<small>3&nbsp;1&nbsp;4&nbsp;2</small>__ | <span style="color: red;">2&nbsp;0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0&nbsp;2</span></small> | <small><span style="color: red;">1&nbsp;2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2&nbsp;1</span> | ![inversion map of \(2, 4, 1, 3\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2010.svg) | <span style="color: red;">1&nbsp;2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2&nbsp;1</span></small> | <span style="color: red;">3</span> |
| 11                                                 | ![permutation matrix of \(4, 2, 1, 3\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2011.svg) | __4&nbsp;2&nbsp;1&nbsp;3__ | __<small>3&nbsp;1&nbsp;2&nbsp;4</small>__ | <span style="color: red;">2&nbsp;1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1&nbsp;2</span></small> | <small><span style="color: red;">1&nbsp;2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2&nbsp;1</span> | ![inversion map of \(4, 2, 1, 3\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2011.svg) | <span style="color: red;">3&nbsp;1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1&nbsp;3</span></small> | <span style="color: red;">4</span> |
| 12                                                 | ![permutation matrix of \(1, 3, 4, 2\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2012.svg) | __1&nbsp;3&nbsp;4&nbsp;2__ | __<small>2&nbsp;4&nbsp;3&nbsp;1</small>__ | <span style="color: red;">0&nbsp;2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2&nbsp;0</span></small> | <small><span style="color: red;">2&nbsp;0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0&nbsp;2</span> | ![inversion map of \(1, 3, 4, 2\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2012.svg) | <span style="color: red;">0&nbsp;1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1&nbsp;0</span></small> | <span style="color: red;">2</span> |
| <span style="background-color: #ffbb00;">13</span> | ![permutation matrix of \(3, 1, 4, 2\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2013.svg) | __3&nbsp;1&nbsp;4&nbsp;2__ | __<small>2&nbsp;4&nbsp;1&nbsp;3</small>__ | <span style="color: red;">1&nbsp;2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2&nbsp;1</span></small> | <small><span style="color: red;">2&nbsp;0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0&nbsp;2</span> | ![inversion map of \(3, 1, 4, 2\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2013.svg) | <span style="color: red;">2&nbsp;0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0&nbsp;2</span></small> | <span style="color: red;">3</span> |
| <span style="background-color: #33eb2a;">14</span> | ![permutation matrix of \(1, 4, 3, 2\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2014.svg) | __1&nbsp;4&nbsp;3&nbsp;2__ | __<small>2&nbsp;3&nbsp;4&nbsp;1</small>__ | <span style="color: red;">0&nbsp;2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2&nbsp;0</span></small> | <small><span style="color: red;">2&nbsp;1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1&nbsp;2</span> | ![inversion map of \(1, 4, 3, 2\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2014.svg) | <span style="color: red;">0&nbsp;2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2&nbsp;0</span></small> | <span style="color: red;">3</span> |
| 15                                                 | ![permutation matrix of \(4, 1, 3, 2\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2015.svg) | __4&nbsp;1&nbsp;3&nbsp;2__ | __<small>2&nbsp;3&nbsp;1&nbsp;4</small>__ | <span style="color: red;">1&nbsp;2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2&nbsp;1</span></small> | <small><span style="color: red;">2&nbsp;1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1&nbsp;2</span> | ![inversion map of \(4, 1, 3, 2\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2015.svg) | <span style="color: red;">3&nbsp;0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0&nbsp;3</span></small> | <span style="color: red;">4</span> |
| __16__                                             | ![permutation matrix of \(3, 4, 1, 2\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2016.svg) | __3&nbsp;4&nbsp;1&nbsp;2__ | __<small>2&nbsp;1&nbsp;4&nbsp;3</small>__ | <span style="color: red;">2&nbsp;2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2&nbsp;2</span></small> | <small><span style="color: red;">2&nbsp;2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2&nbsp;2</span> | ![inversion map of \(3, 4, 1, 2\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2016.svg) | <span style="color: red;">2&nbsp;2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2&nbsp;2</span></small> | <span style="color: red;">4</span> |
| <span style="background-color: #ffbb00;">17</span> | ![permutation matrix of \(4, 3, 1, 2\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2017.svg) | __4&nbsp;3&nbsp;1&nbsp;2__ | __<small>2&nbsp;1&nbsp;3&nbsp;4</small>__ | <span style="color: red;">2&nbsp;2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2&nbsp;2</span></small> | <small><span style="color: red;">2&nbsp;2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2&nbsp;2</span> | ![inversion map of \(4, 3, 1, 2\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2017.svg) | <span style="color: red;">3&nbsp;2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2&nbsp;3</span></small> | <span style="color: red;">5</span> |
| <span style="background-color: #ffbb00;">18</span> | ![permutation matrix of \(2, 3, 4, 1\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2018.svg) | __2&nbsp;3&nbsp;4&nbsp;1__ | __<small>1&nbsp;4&nbsp;3&nbsp;2</small>__ | <span style="color: red;">3&nbsp;0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0&nbsp;3</span></small> | <small><span style="color: red;">3&nbsp;0&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;0&nbsp;3</span> | ![inversion map of \(2, 3, 4, 1\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2018.svg) | <span style="color: red;">1&nbsp;1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1&nbsp;1</span></small> | <span style="color: red;">3</span> |
| 19                                                 | ![permutation matrix of \(3, 2, 4, 1\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2019.svg) | __3&nbsp;2&nbsp;4&nbsp;1__ | __<small>1&nbsp;4&nbsp;2&nbsp;3</small>__ | <span style="color: red;">3&nbsp;1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1&nbsp;3</span></small> | <small><span style="color: red;">3&nbsp;0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0&nbsp;3</span> | ![inversion map of \(3, 2, 4, 1\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2019.svg) | <span style="color: red;">2&nbsp;1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1&nbsp;2</span></small> | <span style="color: red;">4</span> |
| 20                                                 | ![permutation matrix of \(2, 4, 3, 1\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2020.svg) | __2&nbsp;4&nbsp;3&nbsp;1__ | __<small>1&nbsp;3&nbsp;4&nbsp;2</small>__ | <span style="color: red;">3&nbsp;0&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;0&nbsp;3</span></small> | <small><span style="color: red;">3&nbsp;1&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;1&nbsp;3</span> | ![inversion map of \(2, 4, 3, 1\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2020.svg) | <span style="color: red;">1&nbsp;2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2&nbsp;1</span></small> | <span style="color: red;">4</span> |
| <span style="background-color: #33eb2a;">21</span> | ![permutation matrix of \(4, 2, 3, 1\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2021.svg) | __4&nbsp;2&nbsp;3&nbsp;1__ | __<small>1&nbsp;3&nbsp;2&nbsp;4</small>__ | <span style="color: red;">3&nbsp;1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1&nbsp;3</span></small> | <small><span style="color: red;">3&nbsp;1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1&nbsp;3</span> | ![inversion map of \(4, 2, 3, 1\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2021.svg) | <span style="color: red;">3&nbsp;1&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;1&nbsp;3</span></small> | <span style="color: red;">5</span> |
| <span style="background-color: #ffbb00;">22</span> | ![permutation matrix of \(3, 4, 2, 1\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2022.svg) | __3&nbsp;4&nbsp;2&nbsp;1__ | __<small>1&nbsp;2&nbsp;4&nbsp;3</small>__ | <span style="color: red;">3&nbsp;2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2&nbsp;3</span></small> | <small><span style="color: red;">3&nbsp;2&nbsp;0&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;0&nbsp;2&nbsp;3</span> | ![inversion map of \(3, 4, 2, 1\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2022.svg) | <span style="color: red;">2&nbsp;2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2&nbsp;2</span></small> | <span style="color: red;">5</span> |
| __23__                                             | ![permutation matrix of \(4, 3, 2, 1\)](../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%2023.svg) | __4&nbsp;3&nbsp;2&nbsp;1__ | __<small>1&nbsp;2&nbsp;3&nbsp;4</small>__ | <span style="color: red;">3&nbsp;2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2&nbsp;3</span></small> | <small><span style="color: red;">3&nbsp;2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span></small> | <span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2&nbsp;3</span> | ![inversion map of \(4, 3, 2, 1\)](../../archives/Wikimedia%20Commons/4-el%20perm%20invset%2023.svg) | <span style="color: red;">3&nbsp;2&nbsp;1&nbsp;<span style="opacity: 0.3;">0</span></span> | <small><span style="color: red;"><span style="opacity: 0.3;">0</span>&nbsp;1&nbsp;2&nbsp;3</span></small> | <span style="color: red;">6</span> |

<!--
```Python
from itertools import permutations

def main():
    orig = tuple(range(1, 5))
    pers = tuple(tuple(reversed(z)) for z in permutations(reversed(orig)))
    p_mat_name = "../../archives/Wikimedia%20Commons/4-el%20perm%20matrix%20{:02d}.svg"
    p_invmap_name = "../../archives/Wikimedia%20Commons/4-el%20perm%20invset%20{:02d}.svg"

    def v(p):
        return tuple(sum(1 for j in p[: p.index(i)] if j > i) for i in orig)

    def l(p):
        return tuple(sum(1 for j in p[:i] if j > p[i]) for i in range(len(orig)))

    def r(p):
        return tuple(sum(1 for j in p[i + 1 :] if j < p[i]) for i in range(len(orig)))

    def str_vlr(nums, reverse=False, *, l=False):
        nums = list(map(str, nums))
        nums[0 if l else -1] = (
            f'<span style="opacity: 0.3;">{nums[0 if l else -1]}</span>'
        )
        return "&nbsp;".join(reversed(nums) if reverse else nums)

    print(
        R"""
| | | $\pi$ | | $v$ | | | $l$ | p-b | $r$ | | \# |
|-|-|-------|-|-----|-|-|-----|-----|-----|-|----|""".lstrip()
    )
    for idx, p in enumerate(pers):
        v0, l0, r0 = v(p), l(p), r(p)
        assert sum(v0) == sum(l0)
        assert sum(l0) == sum(r0)
        cells = (
            str(idx),
            f"![permutation matrix of \\({', '.join(map(str, p))}\\)]({p_mat_name.format(idx)})",
            f"__{'&nbsp;'.join(map(str, p))}__",
            f"__<small>{'&nbsp;'.join(map(str, reversed(p)))}</small>__",
            f'<span style="color: red;">{str_vlr(v0)}</span>',
            f'<small><span style="color: red;">{str_vlr(v0, True)}</span></small>',
            f'<small><span style="color: red;">{str_vlr(l0, True, l=True)}</span></small>',
            f'<span style="color: red;">{str_vlr(l0, l=True)}</span>',
            f"![inversion map of \\({', '.join(map(str, p))}\\)]({p_invmap_name.format(idx)})",
            f'<span style="color: red;">{str_vlr(r0)}</span>',
            f'<small><span style="color: red;">{str_vlr(r0, True)}</span></small>',
            f'<span style="color: red;">{sum(v0)}</span>',
        )
        print(Rf"| {' | '.join(cells)} |")

if __name__ == "__main__":
    main()
```
-->

## weak order of permutations

> {@{![Permutohedron of the [symmetric group](symmetric%20group.md) S<sub>4</sub>](../../archives/Wikimedia%20Commons/Symmetric%20group%204;%20permutohedron%203D;%20numbers.svg)}@}
>
> {@{Permutohedron of the [symmetric group](symmetric%20group.md) S<sub>4</sub>}@}

{@{The set of permutations on _n_ items}@} can be {@{given the structure of a [partial order](partially%20ordered%20set.md#partial%20order)}@}, called {@{the __weak order of permutations__}@}, which {@{forms a [lattice](lattice%20(order).md)}@}.

{@{The [Hasse diagram](hasse%20diagram.md)}@} of {@{the inversion sets ordered by the [subset](subset.md) relation}@} forms {@{the [skeleton](n-skeleton.md) of a [permutohedron](permutohedron.md)}@}.

If {@{a permutation is assigned to each inversion set using the place-based definition}@}, the resulting order of permutations is {@{that of the permutohedron}@}, where {@{an edge corresponds to the swapping of two elements with consecutive values}@}. This is {@{the weak order of permutations}@}. {@{The identity is its minimum}@}, and {@{the permutation formed by reversing the identity is its maximum}@}.

If {@{a permutation were assigned to each inversion set using the element-based definition}@}, the resulting order of permutations {@{would be that of a [Cayley graph](Cayley%20graph.md)}@}, where {@{an edge corresponds to the swapping of two elements on consecutive places}@}. {@{This Cayley graph of the symmetric group}@} is {@{similar to its permutohedron, but with each permutation replaced by its inverse}@}.

## see also

> ![Wikiversity logo](../../archives/Wikimedia%20Commons/Wikiversity%20logo%202017.svg)
>
> Wikiversity has learning resources about ___[Inversion \(discrete mathematics\)](https://en.wikiversity.org/wiki/Inversion%20%28discrete%20mathematics%29)___

- [factorial number system](factorial%20number%20system.md)
- [permutation graph](permutation%20graph.md)
- [transpositions, simple transpositions, inversions and sorting](permutation%20group.md#transpositions,%20simple%20transpositions,%20inversions%20and%20sorting)
- [Damerau–Levenshtein distance](Damerau–Levenshtein%20distance.md)
- [parity of a permutation](parity%20of%20a%20permutation.md)

__Sequences in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md):__

- [sequences related to factorial base representation](https://oeis.org/wiki/Index_to_OEIS:_Section_Fa#facbase)
- factorial numbers: [A007623](https://oeis.org/A007623) and [A108731](https://oeis.org/A108731)
- inversion numbers: [A034968](https://oeis.org/A034968)
- inversion sets of finite permutations interpreted as binary numbers: [A211362](https://oeis.org/A211362)   \(related permutation: [A211363](https://oeis.org/A211363)\)
- finite permutations that have only 0s and 1s in their inversion vectors: [A059590](https://oeis.org/A059590)   \(their inversion sets: [A211364](https://oeis.org/A211364)\)
- number of permutations of _n_ elements with _k_ inversions; Mahonian numbers: [A008302](https://oeis.org/A008302)   \(their row maxima; Kendall-Mann numbers: [A000140](https://oeis.org/A000140)\)
- number of connected labeled graphs with _n_ edges and _n_ nodes: [A057500](https://oeis.org/A057500)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/inversion_(discrete_mathematics)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. [Aigner 2007](#CITEREFAigner2007), pp. 27. <a id="^ref-1"></a>^ref-1
2. [Comtet 1974](#CITEREFComtet1974), pp. 237. <a id="^ref-2"></a>^ref-2
3. [Knuth 1973](#CITEREFKnuth1973), pp. 11. <a id="^ref-3"></a>^ref-3
4. [Pemmaraju & Skiena 2003](#CITEREFPemmarajuSkiena2003), pp. 69. <a id="^ref-4"></a>^ref-4
5. [Vitter & Flajolet 1990](#CITEREFVitterFlajolet1990), pp. 459. <a id="^ref-5"></a>^ref-5
6. [Gratzer 2016](#CITEREFGratzer2016), pp. 221. <a id="^ref-6"></a>^ref-6
7. [Bóna 2012](#CITEREFB%C3%B3na2012), pp. 57. <a id="^ref-7"></a>^ref-7
8. [Cormen et al. 2001](#CITEREFCormenLeisersonRivestStein2001), pp. 39. <a id="^ref-8"></a>^ref-8
9. [Barth & Mutzel 2004](#CITEREFBarthMutzel2004), pp. 183. <a id="^ref-9"></a>^ref-9
10. [Mannila 1985](#CITEREFMannila1985). <a id="^ref-10"></a>^ref-10
11. [Mahmoud 2000](#CITEREFMahmoud2000), pp. 284. <a id="^ref-11"></a>^ref-11
12. [Kleinberg & Tardos 2005](#CITEREFKleinbergTardos2005), pp. 225. <a id="^ref-12"></a>^ref-12
13. Weisstein, Eric W. ["Inversion Vector"](http://mathworld.wolfram.com/InversionVector.html) From [MathWorld](MathWorld.md)--A Wolfram Web Resource <a id="^ref-13"></a>^ref-13
14. Reverse colex order of finitary permutations \(sequence [A055089](https://oeis.org/A055089) in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)\) <a id="^ref-14"></a>^ref-14

### source bibliography

- <a id="CITEREFAigner2007"></a> Aigner, Martin \(2007\). "Word Representation". _A course in enumeration_. Berlin, New York: Springer. [ISBN](ISBN.md) [978-3642072536](https://en.wikipedia.org/wiki/Special:BookSources/978-3642072536).
- <a id="CITEREFBarthMutzel2004"></a> Barth, Wilhelm; [Mutzel, Petra](Petra%20Mutzel.md) \(2004\). ["Simple and Efficient Bilayer Cross Counting"](https://doi.org/10.7155%2Fjgaa.00088). _[Journal of Graph Algorithms and Applications](Journal%20of%20Graph%20Algorithms%20and%20Applications.md)_. __8__ \(2\): 179–194. [doi](digital%20object%20identifier.md):[10.7155/jgaa.00088](https://doi.org/10.7155%2Fjgaa.00088).
- <a id="CITEREFBóna2012"></a> [Bóna, Miklós](Miklós%20Bóna.md) \(2012\). "2.2 Inversions in Permutations of Multisets". _Combinatorics of permutations_. Boca Raton, FL: CRC Press. [ISBN](ISBN.md) [978-1439850510](https://en.wikipedia.org/wiki/Special:BookSources/978-1439850510).
- <a id="CITEREFComtet1974"></a> Comtet, Louis \(1974\). "6.4 Inversions of a permutation of \[n\]". [_Advanced combinatorics; the art of finite and infinite expansions_](https://archive.org/details/Comtet_Louis_-_Advanced_Coatorics). Dordrecht, Boston: D. Reidel Pub. Co. [ISBN](ISBN.md) [9027704414](https://en.wikipedia.org/wiki/Special:BookSources/9027704414).
- <a id="CITEREFCormenLeisersonRivestStein2001"></a> [Cormen, Thomas H.](Thomas%20H.%20Cormen.md); [Leiserson, Charles E.](Charles%20E.%20Leiserson.md); [Rivest, Ronald L.](Ron%20Rivest.md); [Stein, Clifford](Clifford%20Stein.md) \(2001\). _[Introduction to Algorithms](Introduction%20to%20Algorithms.md)_ \(2nd ed.\). MIT Press and McGraw-Hill. [ISBN](ISBN.md) [0-262-53196-8](https://en.wikipedia.org/wiki/Special:BookSources/0-262-53196-8).
- <a id="CITEREFGratzer2016"></a> [Gratzer, George](George%20Grätzer.md) \(2016\). "7-2 Basic objects". _Lattice theory. special topics and applications_. Cham, Switzerland: Birkhäuser. [ISBN](ISBN.md) [978-3319442358](https://en.wikipedia.org/wiki/Special:BookSources/978-3319442358).
- <a id="CITEREFKleinbergTardos2005"></a> Kleinberg, Jon; Tardos, Éva \(2005\). _Algorithm Design_. [ISBN](ISBN.md) [0-321-29535-8](https://en.wikipedia.org/wiki/Special:BookSources/0-321-29535-8).
- <a id="CITEREFKnuth1973"></a> Knuth, Donald \(1973\). "5.1.1 Inversions". _[The Art of Computer Programming](The%20Art%20of%20Computer%20Programming.md)_. Addison-Wesley Pub. Co. [ISBN](ISBN.md) [0201896850](https://en.wikipedia.org/wiki/Special:BookSources/0201896850).
- <a id="CITEREFMahmoud2000"></a> Mahmoud, Hosam Mahmoud \(2000\). "Sorting Nonrandom Data". _Sorting: a distribution theory_. Wiley-Interscience series in discrete mathematics and optimization. Vol. 54. Wiley-IEEE. [ISBN](ISBN.md) [978-0-471-32710-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-471-32710-3).
- <a id="CITEREFPemmarajuSkiena2003"></a> Pemmaraju, Sriram V.; Skiena, Steven S. \(2003\). "Permutations and combinations". _Computational discrete mathematics: combinatorics and graph theory with Mathematica_. Cambridge University Press. [ISBN](ISBN.md) [978-0-521-80686-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-80686-2).
- <a id="CITEREFVitterFlajolet1990"></a> Vitter, J.S.; Flajolet, Ph. \(1990\). "Average-Case Analysis of Algorithms and Data Structures". In [van Leeuwen, Jan](Jan%20van%20Leeuwen.md) \(ed.\). _Algorithms and Complexity_. Vol. 1 \(2nd ed.\). Elsevier. [ISBN](ISBN.md) [978-0-444-88071-0](https://en.wikipedia.org/wiki/Special:BookSources/978-0-444-88071-0).

### further reading

- <a id="CITEREFMargolius2001"></a> Margolius, Barbara H. \(2001\). "Permutations with Inversions". _Journal of Integer Sequences_. __4__.

### presortedness measures

- <a id="CITEREFMannila1985"></a> [Mannila, Heikki](Heikki%20Mannila.md) \(April 1985\). "Measures of presortedness and optimal sorting algorithms". _IEEE Transactions on Computers_. __C-34__ \(4\): 318–325. [doi](digital%20object%20identifier.md):[10.1109/tc.1985.5009382](https://doi.org/10.1109%2Ftc.1985.5009382).
- <a id="CITEREFEstivill-CastroWood1989"></a> Estivill-Castro, Vladimir; [Wood, Derick](Derick%20Wood.md) \(1989\). ["A new measure of presortedness"](https://doi.org/10.1016%2F0890-5401%2889%2990050-3). _Information and Computation_. __83__ \(1\): 111–119. [doi](digital%20object%20identifier.md):[10.1016/0890-5401\(89\)90050-3](https://doi.org/10.1016%2F0890-5401%2889%2990050-3).
- <a id="CITEREFSkiena1988"></a> Skiena, Steven S. \(1988\). "Encroaching lists as a measure of presortedness". _BIT_. __28__ \(4\): 755–784. [doi](digital%20object%20identifier.md):[10.1007/bf01954897](https://doi.org/10.1007%2Fbf01954897). [S2CID](Semantic%20Scholar.md#S2CID) [33967672](https://api.semanticscholar.org/CorpusID:33967672).
