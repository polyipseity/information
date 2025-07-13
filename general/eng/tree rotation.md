---
aliases:
  - tree rotation
  - tree rotations
tags:
  - flashcard/active/general/eng/tree_rotation
  - language/in/English
---

# tree rotation

> {@{![Generic tree rotations.](../../archives/Wikimedia%20Commons/BinaryTreeRotations.svg)}@}
>
> {@{Generic tree rotations.}@} <!--SR:!2025-12-14,275,330!2025-12-19,278,330-->

In {@{[discrete mathematics](discrete%20mathematics.md)}@}, __tree rotation__ is {@{an operation on a [binary tree](binary%20tree.md) that changes the structure without interfering with the order of the elements}@}. A tree rotation {@{moves one node up in the tree and one node down}@}. It is used to {@{change the shape of the tree}@}, and in particular {@{to decrease its height by moving smaller subtrees down and larger subtrees up}@}, resulting in {@{improved performance of many tree operations}@}. <!--SR:!2025-11-16,253,330!2027-04-08,635,330!2025-12-31,287,330!2025-11-14,251,330!2025-11-28,262,330!2025-11-02,241,330-->

There exists {@{an inconsistency in different descriptions as to the definition of the __direction of rotations__}@}. Some say that {@{the direction of rotation reflects the direction that a node is moving upon rotation \(a left child rotating into its parent's location is a right rotation\)}@} while {@{others say that the direction of rotation reflects which subtree is rotating \(a left subtree rotating into its parent's location is a left rotation, the opposite of the former\)}@}. This article takes {@{the approach of the directional movement of the rotating node (annotation: the former one)}@}. <!--SR:!2025-10-19,229,330!2026-05-31,393,310!2025-11-22,257,330!2026-06-07,353,290-->

## illustration

> {@{![tree rotation](../../archives/Wikimedia%20Commons/Tree%20rotation.png)}@}
>
> {@{tree rotation}@} <!--SR:!2025-08-28,186,310!2025-12-05,268,330-->

<!-- markdownlint MD028 -->

> {@{![tree rotation animation](../../archives/Wikimedia%20Commons/Tree%20rotation%20animation%20250x250.gif)}@}
>
> {@{tree rotation animation}@} <!--SR:!2026-01-01,289,330!2026-01-07,294,330-->

{@{The right rotation operation}@} as shown in the adjacent image is performed {@{with _Q_ as the root and hence is a right rotation on, or rooted at, _Q_}@}. This operation results in {@{a rotation of the tree in the clockwise direction}@}. {@{The inverse operation}@} is {@{the left rotation, which results in a movement in a counter-clockwise direction}@} \(the left rotation shown above is {@{rooted at _P_}@}\). The key to understanding how a rotation functions is {@{to understand its constraints}@}. In particular {@{the order of the leaves of the tree \(when read left to right for example\) cannot change}@} \(another way to think of it is that {@{the order that the leaves would be visited in an in-order traversal must be the same after the operation as before}@}\). Another constraint is {@{the main property of a binary search tree}@}, namely that {@{all nodes in the right subtree are greater than the parent and all nodes in the left subtree are less than the [parent](tree%20(abstract%20data%20type).md)}@}. Notice that {@{the [right child](binary%20tree.md#right%20child) of a left child of the root of a sub-tree}@} \(for example node B in the diagram for the tree rooted at Q\) can {@{become the left child of the root}@}, that itself {@{becomes the right child of the "new" root in the rotated sub-tree}@}, without {@{violating either of those constraints}@}. As seen in the diagram, {@{the order of the leaves doesn't change}@}. The opposite operation also {@{preserves the order and is the second kind of rotation}@}. <!--SR:!2025-12-09,271,330!2025-12-15,276,330!2025-10-30,239,330!2026-01-06,293,330!2025-10-31,240,330!2025-12-26,284,330!2025-10-23,232,330!2026-11-02,507,310!2025-12-10,272,330!2025-12-15,276,330!2025-12-14,275,330!2025-11-03,242,330!2025-12-07,269,330!2026-02-24,305,290!2025-10-18,228,330!2025-12-23,281,330!2027-01-15,552,310-->

Assuming {@{this is a [binary search tree](binary%20search%20tree.md)}@}, as stated above, the elements must be {@{interpreted as variables that can be compared to each other}@}. {@{The alphabetic characters to the left}@} are {@{used as placeholders for these variables}@}. In the animation to the right, {@{capital alphabetic characters are used as variable placeholders}@} while {@{lowercase Greek letters are placeholders for an entire set of variables}@}. The circles {@{represent individual nodes and the triangles represent subtrees}@}. Each subtree could be {@{empty, consist of a single node, or consist of any number of nodes}@}. <!--SR:!2027-01-16,553,310!2026-06-11,399,310!2025-12-21,280,330!2025-11-21,256,330!2025-09-27,196,310!2025-11-25,259,330!2027-01-02,539,310!2027-01-03,545,310-->

## detailed illustration

> {@{![Pictorial description of how rotations are made.](../../archives/Wikimedia%20Commons/Tree%20Rotations.gif)}@}
>
> {@{Pictorial description of how rotations are made.}@} <!--SR:!2025-12-20,279,330!2025-12-28,285,330-->

When {@{a subtree is rotated}@}, {@{the subtree side upon which it is rotated increases its height by one node}@} while {@{the other subtree decreases its height}@}. This makes {@{tree rotations useful for rebalancing a tree}@}. <!--SR:!2025-12-08,270,330!2026-06-23,403,310!2025-12-27,283,330!2025-12-15,276,330-->

Consider the terminology of {@{__Root__ for the parent node of the subtrees to rotate}@}, {@{__Pivot__ for the node which will become the new parent node}@}, {@{__RS__ for the side of rotation and __OS__ for the opposite side of rotation}@}. For the root Q in the diagram above, __RS__ is C and __OS__ is P. Using these terms, the pseudo code for the rotation is: <!--SR:!2025-11-26,260,330!2025-10-30,238,330!2025-11-13,251,330-->

```pseudocode
let Pivot = Root.OS
Root.OS = Pivot.RS
Pivot.RS = Root
Root = Pivot
```

> __code flashcards__
>
> <pre>
> {@{let Pivot = Root.OS}@}
> {@{Root.OS = Pivot.RS}@}
> {@{Pivot.RS = Root}@}
> {@{Root = Pivot}@}
> </pre> <!--SR:!2025-10-17,227,330!2025-11-17,254,330!2025-12-19,230,270!2025-07-17,155,310-->

This is a {@{constant time}@} operation. <!--SR:!2025-10-22,231,330-->

The programmer must {@{also make sure that the root's parent points to the pivot after the rotation}@}. Also, the programmer should note that {@{this operation may result in a new root for the entire tree and take care to update pointers accordingly}@}. <!--SR:!2025-11-27,261,330!2025-11-30,263,330-->

## inorder invariance

The tree rotation renders {@{the [inorder traversal](tree%20traversal.md#inorder%20traversal) of the binary tree [invariant](invariant%20(mathematics).md#invariants%20in%20computer%20science)}@}. This implies {@{the order of the elements is not affected when a rotation is performed in any part of the tree}@}. Here are the inorder traversals of the trees shown above: <!--SR:!2025-08-11,175,310!2026-05-27,390,310-->

```text
Left tree: ((A, P, B), Q, C)        Right tree: (A, P, (B, Q, C))
```

Computing {@{one from the other is very simple}@}. The following is example [Python](python%20(programming%20language).md) code that performs that computation: <!--SR:!2026-01-02,290,330-->

```Python
def right_rotation(treenode):
    """Rotate the specified tree to the right."""
    left, Q, C = treenode
    A, P, B = left
    return (A, P, (B, Q, C))
```

> __code flashcards__
>
> <pre>
> <span></span><!-- <span class="k"> --><span style="color: #008000; font-weight: bold;">def</span> {@{<!-- <span class="nf"> --><span style="color: #0000FF;">right_rotation</span><!-- <span class="p"> --><span style="">(</span><!-- <span class="n"> --><span style="">treenode</span><!-- <span class="p"> --><span style="">):</span>}@}
> <!-- <span class="w"> --><span style="color: #bbbbbb;">    </span><!-- <span class="sd"> --><span style="color: #BA2121; font-style: italic;">"""{@{Rotate the specified tree to the right.}@}"""</span>
>     {@{<!-- <span class="n"> --><span style="">left</span><!-- <span class="p"> --><span style="">,</span> <!-- <span class="n"> --><span style="">Q</span><!-- <span class="p"> --><span style="">,</span> <!-- <span class="n"> --><span style="">C</span> <!-- <span class="o"> --><span style="color: #666666;">=</span> <!-- <span class="n"> --><span style="">treenode</span>}@}
>     {@{<!-- <span class="n"> --><span style="">A</span><!-- <span class="p"> --><span style="">,</span> <!-- <span class="n"> --><span style="">P</span><!-- <span class="p"> --><span style="">,</span> <!-- <span class="n"> --><span style="">B</span> <!-- <span class="o"> --><span style="color: #666666;">=</span> <!-- <span class="n"> --><span style="">left</span>}@}
>     {@{<!-- <span class="k"> --><span style="color: #008000; font-weight: bold;">return</span> <!-- <span class="p"> --><span style="">(</span><!-- <span class="n"> --><span style="">A</span><!-- <span class="p"> --><span style="">,</span> <!-- <span class="n"> --><span style="">P</span><!-- <span class="p"> --><span style="">,</span> <!-- <span class="p"> --><span style="">(</span><!-- <span class="n"> --><span style="">B</span><!-- <span class="p"> --><span style="">,</span> <!-- <span class="n"> --><span style="">Q</span><!-- <span class="p"> --><span style="">,</span> <!-- <span class="n"> --><span style="">C</span><!-- <span class="p"> --><span style="">))</span>}@}
> </pre> <!--SR:!2025-10-22,232,330!2025-12-02,265,330!2025-12-06,268,330!2025-11-08,246,330!2025-12-17,276,330-->

Another way of looking at it is:

Right rotation of node Q:

```pseudocode
Let P be Q's left child.
Set Q's left child to be P's right child.
[Set P's right-child's parent to Q]
Set P's right child to be Q.
[Set Q's parent to P]
```

Left rotation of node P:

```pseudocode
Let Q be P's right child.
Set P's right child to be Q's left child.
[Set Q's left-child's parent to P]
Set Q's left child to be P.
[Set P's parent to Q]
All other connections are left as-is.
```

There are {@{also _double rotations_}@}, which are {@{combinations of left and right rotations}@}. {@{A _double left_ rotation at X}@} can be defined to be {@{a right rotation at the right child of X followed by a left rotation at X}@}; similarly, {@{a _double right_ rotation at X}@} can be defined to be {@{a left rotation at the left child of X followed by a right rotation at X}@}. <!--SR:!2025-10-24,233,330!2025-09-26,194,310!2025-08-31,177,310!2027-01-08,545,310!2027-01-03,540,310!2025-11-09,247,330-->

Tree rotations are {@{used in a number of tree [data structures](data%20structure.md)}@} such as {@{[AVL trees](AVL%20tree.md), [red–black trees](red–black%20tree.md), [WAVL trees](WAVL%20tree.md), [splay trees](splay%20tree.md), and [treaps](treap.md)}@}. They require {@{only constant time because they are _local_ transformations}@}: they {@{only operate on 5 nodes, and need not examine the rest of the tree}@}. <!--SR:!2027-04-04,631,330!2026-12-14,527,310!2025-08-27,185,310!2025-09-12,196,310-->

## rotations for rebalancing

> {@{![Pictorial description of how rotations cause rebalancing in an AVL tree.](../../archives/Wikimedia%20Commons/Tree%20Rebalancing.gif)}@}
>
> {@{Pictorial description of how rotations cause rebalancing in an AVL tree.}@} <!--SR:!2026-12-15,528,310!2025-11-28,222,270-->

A tree can be {@{rebalanced using rotations}@}. After {@{a rotation}@}, {@{the side of the rotation increases its height by 1 whilst the side opposite the rotation decreases its height similarly}@}. Therefore, {@{one can strategically apply rotations to nodes whose left child and right child differ in height by more than 1}@}. {@{Self-balancing binary search trees}@} {@{apply this operation automatically}@}. A type of tree which uses this rebalancing technique is {@{the [AVL tree](AVL%20tree.md)}@}. <!--SR:!2025-08-30,189,310!2025-12-16,276,330!2025-12-03,266,330!2025-12-25,283,330!2025-11-15,252,330!2025-12-24,282,330!2025-12-23,281,330-->

## rotation distance

- Main article: [Rotation distance](rotation%20distance.md)

> __Unsolved problem in computer science__:
>
> _Can {@{the rotation distance between two binary trees be computed in polynomial time}@}?_
>
> [\(more unsolved problems in computer science\)](list%20of%20unsolved%20problems%20in%20computer%20science.md) <!--SR:!2025-11-18,255,330-->

{@{The [rotation distance](rotation%20distance.md) between any two binary trees with the same number of nodes}@} is {@{the minimum number of rotations needed to transform one into the other}@}. With this distance, {@{the set of _n_-node binary trees becomes a [metric space](metric%20space.md)}@}: {@{the distance is symmetric, positive when given two different trees, and satisfies the [triangle inequality](triangle%20inequality.md)}@}. <!--SR:!2025-07-31,166,310!2025-09-03,192,310!2025-12-31,288,330!2025-12-01,264,330-->

It is {@{an [open problem](open%20problem.md)}@} {@{whether there exists a [polynomial time](time%20complexity.md#polynomial%20time) [algorithm](algorithm.md) for calculating rotation distance}@}, though {@{several variants of the rotation distance problem admit polynomial time algorithms}@}.<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup><sup>[\[3\]](#^ref-3)</sup> <!--SR:!2025-10-20,230,330!2025-08-26,185,310!2025-11-08,231,290-->

{@{[Daniel Sleator](Daniel%20Sleator.md), [Robert Tarjan](Robert%20Tarjan.md) and [William Thurston](William%20Thurston.md)}@} showed that {@{the rotation distance between any two _n_-node trees \(for _n_ ≥ 11\) is at most 2<!-- markdown separator -->_n_<!-- markdown separator --> − 6}@}, and that {@{some pairs of trees are this far apart as soon as _n_ is sufficiently large}@}.<sup>[\[4\]](#^ref-4)</sup> {@{Lionel Pournin}@} showed that, {@{in fact, such pairs exist whenever _n_ ≥ 11}@}.<sup>[\[5\]](#^ref-5)</sup> <!--SR:!2026-02-02,293,290!2026-04-02,331,290!2026-08-05,432,310!2026-04-11,339,290!2026-11-10,512,310-->

## see also

- [AVL tree](AVL%20tree.md), [red–black tree](red–black%20tree.md), and [splay tree](splay%20tree.md), ::@:: kinds of [binary search tree](binary%20search%20tree.md) data structures that use rotations to maintain balance. <!--SR:!2025-08-21,128,310!2025-10-29,237,330-->
- [Associativity](associative%20property.md) of a binary operation ::@:: means that performing a tree rotation on it does not change the final result. <!--SR:!2025-11-10,248,330!2026-01-08,294,330-->
- The [Day–Stout–Warren algorithm](Day–Stout–Warren%20algorithm.md) ::@:: balances an unbalanced BST. <!--SR:!2027-01-19,556,310!2025-10-09,191,290-->
- [Tamari lattice](Tamari%20lattice.md), ::@:: a partially ordered set in which the elements can be defined as binary trees and the ordering between elements is defined by tree rotation. <!--SR:!2026-09-29,473,310!2025-11-24,226,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/tree_rotation) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFFordham2003"></a> Fordham, Blake \(2003\), "Minimal Length Elements of Thompson's Group F", _Geometriae Dedicata_, __99__ \(1\), Springer Science and Business Media LLC: 179–220, [doi](digital%20object%20identifier.md):[10.1023/a:1024971818319](https://doi.org/10.1023%2Fa%3A1024971818319), [ISSN](ISSN.md) [0046-5755](https://search.worldcat.org/issn/0046-5755) <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFBonninPallo1992"></a> Bonnin, André; Pallo, Jean-Marcel \(1992\), "A shortest path metric on unlabeled binary trees", _Pattern Recognition Letters_, __13__ \(6\), Elsevier BV: 411–415, [doi](digital%20object%20identifier.md):[10.1016/0167-8655\(92\)90047-4](https://doi.org/10.1016%2F0167-8655%2892%2990047-4), [ISSN](ISSN.md) [0167-8655](https://search.worldcat.org/issn/0167-8655) <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFPallo2003"></a> Pallo, Jean Marcel \(2003\), "Right-arm rotation distance between binary trees", _Information Processing Letters_, __87__ \(4\), Elsevier BV: 173–177, [doi](digital%20object%20identifier.md):[10.1016/s0020-0190\(03\)00283-7](https://doi.org/10.1016%2Fs0020-0190%2803%2900283-7), [ISSN](ISSN.md) [0020-0190](https://search.worldcat.org/issn/0020-0190) <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFSleatorTarjanThurston1988"></a> [Sleator, Daniel D.](Daniel%20Sleator.md); [Tarjan, Robert E.](Robert%20Tarjan.md); [Thurston, William P.](William%20Thurston.md) \(1988\), "Rotation distance, triangulations, and hyperbolic geometry", _[Journal of the American Mathematical Society](Journal%20of%20the%20American%20Mathematical%20Society.md)_, __1__ \(3\): 647–681, [doi](digital%20object%20identifier.md):[10.2307/1990951](https://doi.org/10.2307%2F1990951), [JSTOR](JSTOR.md#content) [1990951](https://www.jstor.org/stable/1990951), [MR](Mathematical%20Reviews.md) [0928904](https://mathscinet.ams.org/mathscinet-getitem?mr=0928904). <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFPournin2014"></a> Pournin, Lionel \(2014\), "The diameter of associahedra", _[Advances in Mathematics](Advances%20in%20Mathematics.md)_, __259__: 13–42, [arXiv](ArXiv.md):[1207.6296](https://arxiv.org/abs/1207.6296), [doi](digital%20object%20identifier.md):[10.1016/j.aim.2014.02.035](https://doi.org/10.1016%2Fj.aim.2014.02.035), [MR](Mathematical%20Reviews.md) [3197650](https://mathscinet.ams.org/mathscinet-getitem?mr=3197650). <a id="^ref-5"></a>^ref-5

## external links

- [The AVL Tree Rotations Tutorial](http://fortheloot.com/public/AVLTreeTutorial.rtf) \(RTF\) by John Hargrove

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Binary trees](https://en.wikipedia.org/wiki/Category:Binary%20trees)
> - [Search trees](https://en.wikipedia.org/wiki/Category:Search%20trees)
