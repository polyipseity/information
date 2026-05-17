---
aliases:
  - 1 connected
  - 1 connected space
  - 1 connected spaces
  - 1 simply connected
  - 1 simply connected space
  - 1 simply connected spaces
  - 1-connected
  - 1-connected space
  - 1-connected spaces
  - 1-simply connected
  - 1-simply connected space
  - 1-simply connected spaces
  - multiply connected
  - multiply connected space
  - multiply connected spaces
  - multiply-connected
  - multiply-connected space
  - multiply-connected spaces
  - non-simply connected
  - non-simply connected space
  - non-simply connected spaces
  - non-simply-connected
  - non-simply-connected space
  - non-simply-connected spaces
  - simply connected
  - simply-connected
  - simply connected space
  - simply connected spaces
  - simply-connected space
  - simply-connected spaces
tags:
  - flashcard/active/general/eng/simply_connected_space
  - language/in/English
---

# simply connected space

In {@{[topology](topology.md)}@}, {@{a [topological space](topological%20space.md) is called __simply connected__ \(or __1-connected__, or __1-simply connected__<sup>[\[1\]](#^ref-1)</sup>\)}@} if it is {@{[path-connected](path-connected.md#path%20connectedness) \(annotation: 0-connected\)}@} and {@{every [path](path%20(topology).md) between two points can be continuously transformed into any other such path while preserving the two endpoints in question}@}. Intuitively, this corresponds to {@{a space that has no disjoint parts and no holes that go completely through it}@}, because {@{two paths going around different sides of such a hole cannot be continuously transformed into each other}@}. {@{The [fundamental group](fundamental%20group.md) of a topological space}@} is {@{an indicator of the failure for the space to be simply connected}@}: {@{a path-connected topological space is simply connected}@} if and only if {@{its fundamental group is trivial}@}. <!--SR:!fsrs,2029-09-29T00:00:00.000Z,1199,1198.87680538,1,2,9,0,0,2026-06-18T00:00:00.000Z!2029-05-31,1115,350!2029-06-24,1134,350!2026-07-08,290,330!fsrs,2029-09-06T09:22:21.128Z,1181,1180.83166378,1,2,9,0,0,2026-06-13T09:22:21.128Z!fsrs,2029-08-19T01:35:29.370Z,1168,1168.38706892,1,2,9,0,0,2026-06-08T01:35:29.370Z!2029-04-07,1072,350!2026-07-01,284,330!2026-06-30,283,330!fsrs,2029-10-09T00:00:00.000Z,1206,1206.48213635,1,2,9,0,0,2026-06-21T00:00:00.000Z-->

## definition and equivalent formulations

> {@{![This shape represents a set that is _not_ simply connected, because any loop that encloses one or more of the holes cannot be contracted to a point without exiting the region.](../../archives/Wikimedia%20Commons/Runge%20theorem.svg)}@}
>
> This shape represents {@{a set that is _not_ simply connected}@}, because {@{any loop that encloses one or more of the holes cannot be contracted to a point without exiting the region}@}. <!--SR:!fsrs,2029-08-05T05:30:04.225Z,1157,1156.92457827,1,2,9,0,0,2026-06-05T05:30:04.225Z!fsrs,2029-11-03T00:00:00.000Z,1225,1225.46601476,1,2,9,0,0,2026-06-27T00:00:00.000Z!fsrs,2028-08-10T00:00:00.000Z,778,777.80280131,2.49272837,2,9,0,0,2026-06-24T00:00:00.000Z-->

{@{A [topological space](topological%20space.md) $X$ is called simply connected}@} if {@{it is path-connected}@} and {@{any [loop](loop%20(topology).md) in $X$ defined by $f:S^{1}\to X$ can be contracted to a point}@}: there exists {@{a continuous map $F:D^{2}\to X$ such that $F$ restricted to $S^{1}$ is $f$ \(annotation: if a hole is enclosed, such a _continuous_ map $F$ does not exist\)}@}. Here, {@{$S^{1}$ and $D^{2}$}@} denotes {@{the [unit circle](unit%20circle.md) and closed [unit disk](unit%20disk.md) in the [Euclidean plane](Euclidean%20space.md) \(annotation: note that $S^1$ is the boundary of $D^2$\)}@} respectively. <!--SR:!fsrs,2029-07-31T05:29:48.087Z,1152,1151.62722346,1,2,9,0,0,2026-06-05T05:29:48.087Z!fsrs,2029-08-07T05:29:48.856Z,1159,1159.34014939,1,2,9,0,0,2026-06-05T05:29:48.856Z!fsrs,2029-09-18T03:38:19.442Z,1191,1191.26470738,1,2,9,0,0,2026-06-15T03:38:19.442Z!fsrs,2028-08-02T00:00:00.000Z,773,772.81357058,2.49272837,2,9,0,0,2026-06-21T00:00:00.000Z!fsrs,2029-08-03T05:29:45.564Z,1155,1155.09404231,1,2,9,0,0,2026-06-05T05:29:45.564Z!fsrs,2029-09-24T00:00:00.000Z,1195,1195.07164214,1,2,9,0,0,2026-06-17T00:00:00.000Z-->

{@{An equivalent formulation}@} is this: {@{$X$ is simply connected}@} if and only if {@{it is path-connected}@}, and whenever {@{$p:[0,1]\to X$ and $q:[0,1]\to X$ are two paths \(that is, continuous maps\) with the same start and endpoint \($p(0)=q(0)$ and $p(1)=q(1)$\)}@}, then {@{$p$ can be continuously deformed into $q$ while keeping both endpoints fixed}@}. Explicitly, there exists {@{a [homotopy](homotopy.md) $F:[0,1]\times [0,1]\to X$}@} such that {@{$F(x,0)=p(x)$ and $F(x,1)=q(x)$ \(annotation: the second argument of $F$ controls how the path is "interpolated" between $p$ and $q$\)}@}. <!--SR:!fsrs,2029-10-08T00:00:00.000Z,1206,1206.48213635,1,2,9,0,0,2026-06-20T00:00:00.000Z!fsrs,2029-07-31T05:29:43.633Z,1152,1152.1900919,1,2,9,0,0,2026-06-05T05:29:43.633Z!2026-07-05,287,330!fsrs,2029-08-07T05:29:41.706Z,1159,1159.34014939,1,2,9,0,0,2026-06-05T05:29:41.706Z!fsrs,2029-09-06T08:42:43.265Z,1181,1180.83166378,1,2,9,0,0,2026-06-13T08:42:43.265Z!fsrs,2029-08-01T05:30:05.280Z,1153,1153.21435638,1,2,9,0,0,2026-06-05T05:30:05.280Z!fsrs,2029-09-13T14:05:10.456Z,1187,1187.45608877,1,2,9,0,0,2026-06-14T14:05:10.456Z-->

{@{A topological space $X$ is simply connected}@} if and only if {@{$X$ is path-connected}@} and {@{the [fundamental group](fundamental%20group.md) of $X$ at each point is trivial}@}, i.e. {@{consists only of the [identity element](identity%20element.md)}@}. Similarly, {@{$X$ is simply connected}@} if and only if for {@{all points $x,y\in X$}@}, {@{the set of [morphisms](morphism.md) $\operatorname {Hom} _{\Pi (X)}(x,y)$ in the [fundamental groupoid](fundamental%20groupoid.md) of $X$}@} has {@{only one element}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2026-07-03,285,330!2029-04-26,1088,350!fsrs,2029-08-03T05:29:29.114Z,1155,1155.09404231,1,2,9,0,0,2026-06-05T05:29:29.114Z!fsrs,2029-09-06T08:42:45.537Z,1181,1180.83166378,1,2,9,0,0,2026-06-13T08:42:45.537Z!2029-06-02,1117,350!fsrs,2029-08-06T05:30:10.273Z,1158,1157.92961471,1,2,9,0,0,2026-06-05T05:30:10.273Z!fsrs,2029-08-10T00:58:32.476Z,1161,1160.74715681,1,2,9,0,0,2026-06-06T00:58:32.476Z!2029-02-23,1031,350-->

In {@{[complex analysis](complex%20analysis.md)}@}: {@{an open subset $X\subseteq \mathbb {C}$ is simply connected}@} if and only if {@{both $X$ and its complement in the [Riemann sphere](Riemann%20sphere.md) are connected}@}. The set of {@{complex numbers with imaginary part strictly greater than zero and less than one \(annotation: excludes the $\infty$ point in the Riemann sphere\)}@} furnishes an example of {@{an unbounded, connected, open subset of the plane whose complement is not connected \(annotation: in the Euclidean plane but not the Riemann sphere\)}@}. It is {@{nevertheless simply connected \(annotation: the complement contains the $\infty$ point and thus connected in the Riemann sphere\)}@}. {@{A relaxation of the requirement that $X$ be connected}@} leads to {@{an exploration of open subsets of the plane with connected extended complement \(annotation: the word "extended" simply means in the Riemann sphere\)}@}. For example, {@{a \(not necessarily connected\) open set has a connected extended complement}@} exactly when {@{each of its connected components is simply connected}@}. <!--SR:!fsrs,2029-10-09T00:00:00.000Z,1206,1206.48213635,1,2,9,0,0,2026-06-21T00:00:00.000Z!fsrs,2029-08-05T05:29:51.095Z,1157,1156.92457827,1,2,9,0,0,2026-06-05T05:29:51.095Z!2029-05-15,1103,350!fsrs,2029-09-29T00:00:00.000Z,1199,1198.87680538,1,2,9,0,0,2026-06-18T00:00:00.000Z!2029-02-22,1030,350!2026-07-08,289,330!fsrs,2029-09-18T03:38:17.754Z,1191,1191.26470738,1,2,9,0,0,2026-06-15T03:38:17.754Z!fsrs,2029-07-29T05:29:32.512Z,1150,1150.15794126,1,2,9,0,0,2026-06-05T05:29:32.512Z!fsrs,2029-09-08T08:42:46.369Z,1183,1183.23052139,1,2,9,0,0,2026-06-13T08:42:46.369Z!fsrs,2029-08-01T05:29:44.715Z,1153,1153.21435638,1,2,9,0,0,2026-06-05T05:29:44.715Z-->

## informal discussion

Informally, {@{an object in our space is simply connected}@} if it {@{consists of one piece and does not have any "holes" that pass all the way through it}@}. For example, {@{neither a doughnut nor a coffee cup \(with a handle\)}@} is simply connected, but {@{a hollow rubber ball}@} is simply connected. In {@{two dimensions}@}, {@{a circle}@} is not simply connected, but {@{a disk and a line}@} are. {@{Spaces that are [connected](connected%20space.md) but not simply connected}@} are called {@{__non-simply connected__ or __multiply connected__}@}. <!--SR:!fsrs,2029-10-04T00:00:00.000Z,1203,1202.68030072,1,2,9,0,0,2026-06-19T00:00:00.000Z!fsrs,2029-09-19T02:41:50.096Z,1191,1191.26470738,1,2,9,0,0,2026-06-16T02:41:50.096Z!fsrs,2029-11-01T00:00:00.000Z,1222,1221.67255456,1,2,9,0,0,2026-06-28T00:00:00.000Z!2029-03-25,1061,350!2029-06-01,1116,350!2026-07-02,285,330!fsrs,2029-10-09T00:00:00.000Z,1206,1206.48213635,1,2,9,0,0,2026-06-21T00:00:00.000Z!2026-07-07,288,330!fsrs,2029-08-02T05:29:46.509Z,1154,1153.64404968,1,2,9,0,0,2026-06-05T05:29:46.509Z-->

> {@{![A [sphere](sphere.md) is simply connected because every loop can be contracted \(on the surface\) to a point.](../../archives/Wikimedia%20Commons/P1S2all.jpg)}@}
>
> {@{A [sphere](sphere.md) is simply connected}@} because {@{every loop can be contracted \(on the surface\) to a point}@}. <!--SR:!fsrs,2029-08-15T08:13:21.879Z,1165,1164.5679841,1,2,9,0,0,2026-06-07T08:13:21.879Z!2029-06-22,1133,350!2029-04-02,1069,350-->

The definition rules out {@{only [handle](handle%20decomposition.md)-shaped holes}@}. {@{A sphere \(or, equivalently, a rubber ball with a hollow center\)}@} is {@{simply connected}@}, because {@{any loop on the surface of a sphere can contract to a point}@} even though {@{it has a "hole" in the hollow center}@}. {@{The stronger condition, that the object has no holes of any dimension}@}, is called {@{[contractibility](contractible%20space.md)}@}. <!--SR:!fsrs,2029-10-10T00:00:00.000Z,1206,1206.48213635,1,2,9,0,0,2026-06-22T00:00:00.000Z!fsrs,2029-07-31T05:30:07.042Z,1152,1151.77871624,1,2,9,0,0,2026-06-05T05:30:07.042Z!2029-06-16,1128,350!fsrs,2029-11-10T00:00:00.000Z,1229,1229.25786194,1,2,9,0,0,2026-06-30T00:00:00.000Z!fsrs,2029-07-31T05:29:49.900Z,1152,1152.1900919,1,2,9,0,0,2026-06-05T05:29:49.900Z!2029-05-05,1093,350!fsrs,2029-09-07T08:42:43.935Z,1182,1182.2404257,1,2,9,0,0,2026-06-13T08:42:43.935Z-->

## examples

> {@{![A torus is not a simply connected surface.](../../archives/Wikimedia%20Commons/Torus%20cycles.png)}@}
>
> {@{A torus}@} is {@{not a simply connected surface}@}. {@{Neither of the two colored loops shown here}@} can be {@{contracted to a point without leaving the surface}@}. {@{A [solid torus](solid%20torus.md) is also not simply connected}@} because {@{the purple loop cannot contract to a point without leaving the solid}@}. <!--SR:!2026-07-08,290,330!2029-06-03,1117,350!2029-06-04,1118,350!2026-07-06,287,330!2029-05-09,1097,350!fsrs,2029-09-19T02:41:51.456Z,1191,1191.26470738,1,2,9,0,0,2026-06-16T02:41:51.456Z!fsrs,2029-08-03T05:30:06.081Z,1155,1155.09793684,1,2,9,0,0,2026-06-05T05:30:06.081Z-->

- {@{The [Euclidean plane](Euclidean%20space.md) $\mathbb {R} ^{2}$}@} is {@{simply connected}@}, but {@{$\mathbb {R} ^{2}$ minus the origin $(0,0)$ is not}@}. If {@{$n>2$}@}, then {@{both $\mathbb {R} ^{n}$ and $\mathbb {R} ^{n}$ minus the origin are simply connected}@}.
- Analogously: {@{the [_n_-dimensional sphere](n-sphere.md) $S^{n}$}@} is {@{simply connected if and only if $n\geq 2$}@}.
- {@{Every [convex subset](convex%20subset.md)}@} of {@{$\mathbb {R} ^{n}$ is simply connected}@}.
- {@{A [torus](torus.md), the \(elliptic\) [cylinder](cylinder%20(geometry).md)}@}, {@{the [Möbius strip](Möbius%20strip.md), the [projective plane](projective%20plane.md) and the [Klein bottle](Klein%20bottle.md)}@} are {@{not simply connected}@}.
- {@{Every [topological vector space](topological%20vector%20space.md)}@} is {@{simply connected}@}; this includes {@{[Banach spaces](Banach%20space.md) and [Hilbert spaces](Hilbert%20space.md)}@}.
- For {@{$n\geq 2$}@}, {@{the [special orthogonal group](special%20orthogonal%20group.md) $\operatorname {SO} (n,\mathbb {R} )$ \(annotation: orthogonal $n \times n$ matrices of determinant 1\) is not simply connected}@} and {@{the [special unitary group](special%20unitary%20group.md) $\operatorname {SU} (n)$ \(annotation: unitary $n \times n$ matrices of determinant 1\) is simply connected}@}.
- {@{The one-point compactification of $\mathbb {R}$ \(annotation: an example is [projectively extended real line](projectively%20extended%20real%20line.md)\)}@} is {@{not simply connected \(even though $\mathbb {R}$ is simply connected\)}@}.
- {@{The [long line](long%20line%20(topology).md) $L$ \(annotation: _uncountable_ number of line segments joined together\)}@} is {@{simply connected}@}, but {@{its compactification, the extended long line $L^{*}$}@} is {@{not \(since it is not even path connected \(annotation: "too long" to be covered by a path, which is a continuous image of an interval\)\)}@}. <!--SR:!2029-05-01,1089,350!fsrs,2029-07-29T05:29:52.496Z,1150,1150.15794126,1,2,9,0,0,2026-06-05T05:29:52.496Z!fsrs,2029-09-07T08:42:42.252Z,1182,1181.81509617,1,2,9,0,0,2026-06-13T08:42:42.252Z!fsrs,2029-10-09T00:00:00.000Z,1206,1206.48213635,1,2,9,0,0,2026-06-21T00:00:00.000Z!fsrs,2029-08-04T05:29:59.092Z,1156,1156.07446747,1,2,9,0,0,2026-06-05T05:29:59.092Z!2029-04-12,1077,350!2026-07-04,286,330!fsrs,2029-08-05T05:29:39.487Z,1157,1156.51559272,1,2,9,0,0,2026-06-05T05:29:39.487Z!fsrs,2029-10-15T00:00:00.000Z,1210,1210.28222352,1,2,9,0,0,2026-06-23T00:00:00.000Z!2026-07-04,285,330!2029-03-12,1048,350!2026-07-05,286,330!fsrs,2029-08-03T05:29:42.788Z,1155,1154.64628353,1,2,9,0,0,2026-06-05T05:29:42.788Z!fsrs,2029-08-02T05:29:55.535Z,1154,1153.67668351,1,2,9,0,0,2026-06-05T05:29:55.535Z!2026-07-06,288,330!fsrs,2028-07-13T14:04:39.663Z,760,760.32462426,2.49272837,2,9,0,0,2026-06-14T14:04:39.663Z!2029-04-25,1087,350!fsrs,2029-10-04T00:00:00.000Z,1203,1202.68030072,1,2,9,0,0,2026-06-19T00:00:00.000Z!2029-05-03,1091,350!fsrs,2029-07-29T05:30:03.452Z,1150,1150.33930012,1,2,9,0,0,2026-06-05T05:30:03.452Z!2029-06-03,1118,350!2026-07-07,289,330!2028-06-30,784,330!fsrs,2029-10-31T00:00:00.000Z,1222,1221.67255456,1,2,9,0,0,2026-06-27T00:00:00.000Z-->

## properties

{@{A surface \(two-dimensional topological [manifold](manifold.md)\) is simply connected}@} if and only if {@{it is connected}@} and {@{its [genus](genus%20(mathematics).md) \(the number of handles of the surface\) is 0}@}. <!--SR:!fsrs,2029-07-31T05:29:47.222Z,1152,1151.62722346,1,2,9,0,0,2026-06-05T05:29:47.222Z!2026-07-01,284,330!fsrs,2029-07-30T05:29:57.406Z,1151,1150.73228091,1,2,9,0,0,2026-06-05T05:29:57.406Z-->

{@{A universal cover of any \(suitable\) space $X$}@} is {@{a simply connected space which maps to $X$ via a [covering map](covering%20map.md)}@}. <!--SR:!2029-06-25,1135,350!2029-03-06,1042,350-->

If {@{$X$ and $Y$ are [homotopy equivalent](homotopy%20equivalent.md#homotopy%20equivalence)}@} and {@{$X$ is simply connected, then so is $Y$}@}. <!--SR:!fsrs,2029-10-09T00:00:00.000Z,1206,1206.48213635,1,2,9,0,0,2026-06-21T00:00:00.000Z!fsrs,2029-07-30T05:29:59.964Z,1151,1150.73228091,1,2,9,0,0,2026-06-05T05:29:59.964Z-->

{@{The image of a simply connected set under a continuous function}@} {@{need not be simply connected}@}. Take for example {@{the complex plane under the exponential map \(annotation: $z \mapsto e^z$\)}@}: the image is {@{$\mathbb {C} \setminus \{0\}$, which is not simply connected}@}. <!--SR:!fsrs,2029-08-02T05:30:09.012Z,1154,1153.64404968,1,2,9,0,0,2026-06-05T05:30:09.012Z!fsrs,2029-09-09T08:42:41.534Z,1184,1183.64577796,1,2,9,0,0,2026-06-13T08:42:41.534Z!fsrs,2029-08-05T05:30:01.510Z,1157,1156.51559272,1,2,9,0,0,2026-06-05T05:30:01.510Z!fsrs,2029-09-06T08:42:44.985Z,1181,1180.83166378,1,2,9,0,0,2026-06-13T08:42:44.985Z-->

{@{The notion of simple connectedness}@} is important in {@{[complex analysis](complex%20analysis.md)}@} because of the following facts: <!--SR:!2029-06-06,1120,350!2026-07-09,290,330-->

- {@{The [Cauchy's integral theorem](Cauchy's%20integral%20theorem.md)}@} states that if {@{$U$ is a simply connected open subset of the [complex plane](complex%20number.md) $\mathbb {C}$}@}, and {@{$f:U\to \mathbb {C}$ is a [holomorphic function](holomorphic%20function.md)}@}, then {@{$f$ has an [antiderivative](antiderivative%20(complex%20analysis).md) $F$ on $U$}@}, and {@{the value of every [line integral](line%20integral.md) in $U$ with integrand $f$}@} depends {@{only on the end points $u$ and $v$ of the path, and can be computed as $F(v)-F(u)$}@}. The integral thus {@{does not depend on the particular path connecting $u$ and $v$}@},
- {@{The [Riemann mapping theorem](Riemann%20mapping%20theorem.md)}@} states that {@{any non-empty open simply connected subset of $\mathbb {C}$ \(except for $\mathbb {C}$ itself\)}@} is {@{[conformally equivalent](conformal%20map.md) \(annotation: exists a function that locally preserves angles, but not necessarily lengths\) to the [unit disk](unit%20disk.md)}@}. <!--SR:!fsrs,2029-08-06T05:29:53.905Z,1158,1157.92961471,1,2,9,0,0,2026-06-05T05:29:53.905Z!2028-10-20,905,330!fsrs,2029-08-10T00:58:33.271Z,1161,1160.74715681,1,2,9,0,0,2026-06-06T00:58:33.271Z!fsrs,2029-09-24T00:00:00.000Z,1195,1195.07164214,1,2,9,0,0,2026-06-17T00:00:00.000Z!fsrs,2029-08-03T05:29:38.262Z,1155,1154.64628353,1,2,9,0,0,2026-06-05T05:29:38.262Z!2029-06-05,1119,350!fsrs,2029-10-08T00:00:00.000Z,1206,1206.48213635,1,2,9,0,0,2026-06-20T00:00:00.000Z!fsrs,2029-09-07T09:22:22.530Z,1182,1182.2404257,1,2,9,0,0,2026-06-13T09:22:22.530Z!fsrs,2029-10-09T00:00:00.000Z,1206,1206.48213635,1,2,9,0,0,2026-06-21T00:00:00.000Z!2027-06-17,484,390-->

{@{The notion of simple connectedness}@} is also a crucial condition in {@{the [Poincaré conjecture](Poincaré%20conjecture.md)}@}. <!--SR:!2026-07-02,285,330!fsrs,2029-08-04T05:30:07.884Z,1156,1156.07446747,1,2,9,0,0,2026-06-05T05:30:07.884Z-->

## see also

- [Deformation retract](deformation%20retract.md) ::@:: – Continuous, position-preserving \(annotation: in the subspace\) mapping from a topological space into a subspace <!--SR:!fsrs,2029-10-26T00:00:00.000Z,1218,1217.87747351,1,2,9,0,0,2026-06-26T00:00:00.000Z!fsrs,2029-09-19T02:41:52.432Z,1191,1191.26470738,1,2,9,0,0,2026-06-16T02:41:52.432Z-->
- [Locally simply connected space](locally%20simply%20connected%20space.md)
- [n-connected space](n-connected%20space.md)
- [Unicoherent space](unicoherent%20space.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/simply_connected_space) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. ["n-connected space in nLab"](https://ncatlab.org/nlab/show/n-connected+space). _ncatlab.org_. Retrieved 2017-09-17. <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFRonald2006"></a> Ronald, Brown \(June 2006\). _Topology and Groupoids_. Academic Search Complete. North Charleston: CreateSpace. [ISBN](ISBN%20(identifier).md) [1419627228](https://en.wikipedia.org/wiki/Special:BookSources/1419627228). [OCLC](OCLC%20(identifier).md#OCLC) [712629429](https://search.worldcat.org/oclc/712629429). <a id="^ref-2"></a>^ref-2

- <a id="CITEREFSpanier1994"></a> Spanier, Edwin \(December 1994\). _Algebraic Topology_. Springer. [ISBN](ISBN%20(identifier).md) [0-387-94426-5](https://en.wikipedia.org/wiki/Special:BookSources/0-387-94426-5).
- <a id="CITEREFConway1986"></a> Conway, John \(1986\). _Functions of One Complex Variable I_. Springer. [ISBN](ISBN%20(identifier).md) [0-387-90328-3](https://en.wikipedia.org/wiki/Special:BookSources/0-387-90328-3).
- <a id="CITEREFBourbaki2005"></a> Bourbaki, Nicolas \(2005\). _Lie Groups and Lie Algebras_. Springer. [ISBN](ISBN%20(identifier).md) [3-540-43405-4](https://en.wikipedia.org/wiki/Special:BookSources/3-540-43405-4).
- <a id="CITEREFGamelin2001"></a> Gamelin, Theodore \(January 2001\). _Complex Analysis_. Springer. [ISBN](ISBN%20(identifier).md) [0-387-95069-9](https://en.wikipedia.org/wiki/Special:BookSources/0-387-95069-9).
- <a id="CITEREFJoshi1983"></a> Joshi, Kapli \(August 1983\). _Introduction to General Topology_. New Age Publishers. [ISBN](ISBN%20(identifier).md) [0-85226-444-5](https://en.wikipedia.org/wiki/Special:BookSources/0-85226-444-5).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Algebraic topology](https://en.wikipedia.org/wiki/Category:Algebraic%20topology)
> - [Properties of topological spaces](https://en.wikipedia.org/wiki/Category:Properties%20of%20topological%20spaces)
