---
aliases:
  - iterated integral
  - iterated integrals
  - multidimensional integral
  - multidimensional integrals
  - multiple integral
  - multiple integrals
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/multiple_integrals
  - language/in/English
---

# multiple integrals

In this course the main reason for learning these facts is probabilistic: joint densities, region probabilities, and later change-of-variable arguments all rely on being able to integrate over rectangles and more general domains in $\mathbb{R}^n$. The basic picture is that one is no longer distributing probability mass along a line, but across areas, volumes, and higher-dimensional regions. Multiple integration is the language that turns that geometric mass picture into calculation.

---

Flashcards for this section are as follows:

- overview in $\mathbb{R}^n$ with geometric intuition ::@:: Multiple integrals are the multidimensional integration tools used to compute probabilities and expectations for joint densities over rectangles and more general regions in $\mathbb{R}^n$. In one variable, integration accumulates length-weighted height along an interval; in several variables, it accumulates volume-weighted height across a region, so probability mass is spread over areas, volumes, and higher-dimensional sets. <!--SR:!2026-05-07,15,290!2026-05-07,15,290-->

## rectangular Riemann integrals

Let $$Q=[a,b]=\prod_{j=1}^n [a_j,b_j]$$ be a rectangular set in $\mathbb{R}^n$. Its diameter is $$\operatorname{diam}(Q)=\sqrt{\sum_{j=1}^n (b_j-a_j)^2},$$ and its volume is $$\operatorname{Vol}(Q)=\prod_{j=1}^n (b_j-a_j).$$ If $f\colon Q\to\mathbb{R}$ is bounded, one partitions $Q$ into finitely many rectangular pieces $Q_\ell$ with pairwise disjoint interiors and union equal to $Q$.

The comparison with the one-dimensional case should be kept in mind from the start. In one variable, the basic region is an interval $[a,b]$, its size is the length $b-a$, and a partition cuts it into shorter intervals. In several variables, the basic region is a product of intervals, its size is measured by volume, and a partition cuts it into smaller rectangles or boxes. So the multidimensional theory is not a different philosophy; it is the same approximation idea with intervals replaced by boxes.

Each of the basic definitions has a geometric interpretation. A rectangular set is simply the multidimensional version of an interval: in two dimensions it is an axis-parallel rectangle, in three dimensions a box, and in higher dimensions the analogous product region. The volume is the amount of $n$-dimensional space inside that box, just as length is the amount of one-dimensional space in an interval. The diameter records the furthest separation of points in the box and is used as the mesh-size notion because it controls the worst geometric scale present in the partition.

For such a partition $Z_N=(Q_\ell)_{\ell=1}^N$, the lower sum is $$S_-(Z_N,f)=\sum_{\ell=1}^N \operatorname{Vol}(Q_\ell)\inf_{z\in Q_\ell}f(z),$$ and the upper sum is $$S_+(Z_N,f)=\sum_{\ell=1}^N \operatorname{Vol}(Q_\ell)\sup_{z\in Q_\ell}f(z).$$ The lower integral is the supremum of lower sums, the upper integral is the infimum of upper sums, and $f$ is Riemann-integrable on $Q$ when the two agree.

This is exactly the multidimensional analogue of one-dimensional Riemann integration. The only real change is that interval length is replaced by rectangle volume and the mesh size is measured by the largest diameter among the partition elements. In one dimension, lower and upper sums use short intervals and heights based on infima and suprema on those intervals; here the same construction is performed with boxes instead of intervals.

The lower and upper sums should be pictured as crude box-buildings under and over the graph of $f$. On each small rectangle $Q_\ell$, the lower sum uses the smallest height seen on that rectangle and the upper sum uses the largest one. So the lower sum is an inscribed approximation, the upper sum is a circumscribed approximation, and integrability means that once the partition is fine enough the two constructions trap a single limiting value.

The diameter matters because it controls the worst resolution of the partition. Even if most boxes are tiny, one large box can still hide substantial oscillation of the function. Requiring the maximum diameter to go to zero ensures that every piece of the partition becomes geometrically small.

---

Flashcards for this section are as follows:

- rectangular set in $\mathbb{R}^n$ with intuition ::@:: A rectangular set has the form $Q=\prod_{j=1}^n [a_j,b_j]$; it is the multidimensional version of an interval, namely an axis-parallel rectangle in two dimensions, a box in three dimensions, and the analogous product region in higher dimensions. <!--SR:!2026-05-06,14,290!2026-05-07,15,290-->
- diameter of $Q=\prod_{j=1}^n[a_j,b_j]$ with intuition ::@:: The diameter is $\operatorname{diam}(Q)=\sqrt{\sum_{j=1}^n (b_j-a_j)^2}$, and it measures the largest geometric scale present in the box, so in a partition it tells you the worst remaining resolution. <!--SR:!2026-05-07,15,290!2026-05-08,16,290-->
- volume of $Q=\prod_{j=1}^n[a_j,b_j]$ with 1D comparison ::@:: The volume is $\operatorname{Vol}(Q)=\prod_{j=1}^n (b_j-a_j)$; it plays the role that length $b-a$ plays in one dimension, measuring how much $n$-dimensional space the rectangular region occupies. <!--SR:!2026-05-06,14,290!2026-05-08,16,290-->
- lower multiple Riemann sum for partition $Z_N=(Q_\ell)$ ::@:: The lower sum is $S_-(Z_N,f)=\sum_{\ell=1}^N \operatorname{Vol}(Q_\ell)\inf_{z\in Q_\ell}f(z)$. <!--SR:!2026-05-08,16,290!2026-05-06,14,290-->
- upper multiple Riemann sum for partition $Z_N=(Q_\ell)$ ::@:: The upper sum is $S_+(Z_N,f)=\sum_{\ell=1}^N \operatorname{Vol}(Q_\ell)\sup_{z\in Q_\ell}f(z)$. <!--SR:!2026-05-07,15,290!2026-05-08,16,290-->
- Riemann-integrability on a rectangular set $Q$ ::@:: A bounded function on a rectangular set is Riemann-integrable when the supremum of all lower sums equals the infimum of all upper sums. <!--SR:!2026-05-08,16,290!2026-05-06,14,290-->
- lower and upper sums using $\inf_{Q_\ell} f$ and $\sup_{Q_\ell} f$ as box heights ::@:: On each small rectangle, the lower sum uses the smallest height of $f$ and the upper sum uses the largest, so they give underestimates and overestimates of the total mass under the graph. <!--SR:!2026-05-07,15,290!2026-05-06,14,290-->
- why the maximum diameter controls the approximation ::@:: The partition norm uses the largest diameter because one coarse rectangle can still hide large oscillation; requiring the maximum diameter to shrink forces every rectangle to become genuinely small. <!--SR:!2026-05-06,14,290!2026-05-06,14,290-->
- comparison with the one-dimensional Riemann construction ::@:: In one dimension, a partition cuts an interval into short intervals and the sums use interval lengths; in several dimensions, a partition cuts a box into smaller boxes and the sums use their volumes, but the lower/upper approximation idea is exactly the same. <!--SR:!2026-05-07,15,290!2026-05-07,15,290-->

## iterated integrals on rectangles

If $f\colon Q\to\mathbb{R}$ is continuous on the rectangle $$Q=[a_1,b_1]\times\cdots\times[a_n,b_n],$$ then $f$ is Riemann-integrable and one may compute its integral as an iterated integral: $$\int_Q f(x)\,d^n x=\int_{a_1}^{b_1}\left(\int_{a_2}^{b_2}\cdots\left(\int_{a_n}^{b_n}f(x_1,\ldots,x_n)\,dx_n\right)\cdots dx_2\right)dx_1.$$ The integration is read from the inside out, so the innermost variable is integrated first while the outer variables are treated as constants.

Geometrically, in one dimension the integral of a nonnegative function is area under a curve; in two dimensions the double integral of a nonnegative function is volume under a surface over a planar base rectangle. Boundary faces do not contribute to volume, so one may replace closed intervals by half-open or open versions without changing the integral value.

This theorem is the rigorous reason that joint-density calculations may be performed one coordinate at a time when the domain is rectangular and the integrand is sufficiently regular.

The most useful interpretation is the slicing picture. In two variables, fixing $x_1$ turns the surface $z=f(x_1,x_2)$ into a one-variable curve in the $x_2$-direction. The inner integral computes the area of that slice. The outer integral then adds those slice-areas as $x_1$ moves across the base interval. So an iterated integral is not just a formal nesting of symbols; it is repeated accumulation of lower-dimensional quantities.

---

Flashcards for this section are as follows:

- iterated integral formula for continuous $f$ on rectangle $Q=\prod_{j=1}^n[a_j,b_j]$ ::@:: Then $\int_Q f(x)\,d^n x=\int_{a_1}^{b_1}\left(\int_{a_2}^{b_2}\cdots\left(\int_{a_n}^{b_n}f(x_1,\ldots,x_n)\,dx_n\right)\cdots dx_2\right)dx_1$, so the full value is obtained by integrating one variable at a time from the inside out. <!--SR:!2026-05-07,15,290!2026-05-07,15,290-->
- inside-out interpretation ::@:: In an iterated integral, the innermost variable is integrated first while all outer variables are treated as constants. <!--SR:!2026-05-07,15,290!2026-05-06,14,290-->
- geometric meaning of $\int f(x_1,x_2)\,d^2x$ for nonnegative $f$ ::@:: The double integral over a rectangle is the volume under the surface $z=f(x_1,x_2)$ above that base rectangle. <!--SR:!2026-05-08,16,290!2026-05-06,14,290-->
- why rectangular iterated integrals matter for joint densities ::@:: When a joint density is integrated over a rectangular set, the theorem justifies computing the probability by repeated one-variable integrations. <!--SR:!2026-05-07,15,290!2026-05-07,15,290-->
- slice interpretation of an iterated integral ::@:: In a double integral, the inner integral computes the area of one slice of the surface at fixed outer variable, and the outer integral then adds those slice-areas across the whole region. <!--SR:!2026-05-08,16,290!2026-05-08,16,290-->

<!-- check: ignore-next-line[header_style]: proper noun -->
## Fubini and improper multiple integrals

For sufficiently regular functions, the order of integration does not matter. In the appendix this is stated in the practical form: if $f\ge0$ or if the integral of $|f|$ exists over the rectangle, then the iterated integrals may be evaluated in any coordinate order. In two dimensions this is the familiar Fubini rule $$\int_{a_1}^{b_1}\left(\int_{a_2}^{b_2}f(x_1,x_2)\,dx_2\right)dx_1=\int_{a_2}^{b_2}\left(\int_{a_1}^{b_1}f(x_1,x_2)\,dx_1\right)dx_2.$$ More generally, one may permute the order of the coordinates in $\mathbb{R}^n$.

The appendix also records the improper versions. For functions on all of $\mathbb{R}^n$, one defines the integral by truncating to larger and larger boxes and taking limits. Likewise, one may integrate over half-infinite boxes such as $$(-\infty,b_1]\times\cdots\times(-\infty,b_n]$$ by truncating only the infinite sides. These are exactly the domains that appear when one computes joint cumulative distribution functions from joint densities.

The conceptual point behind Fubini's theorem is that one is measuring the same total mass in two different coordinate orders. If the mass is nonnegative, or if positive and negative parts are controlled by absolute integrability, then there is no ambiguity: slicing first in the $x_1$-direction and then in the $x_2$-direction must give the same total as slicing in the reverse order.

So the practical picture is: on rectangles, continuity gives existence; nonnegativity or absolute integrability lets one change order; and improper limits extend the same framework to tails and half-spaces. In probability terms, one may think of truncation as first computing mass in a large observation window and then letting that window expand until it captures the whole relevant region.

---

Flashcards for this section are as follows:

- Fubini on rectangles when $f\ge0$ or $|f|$ is integrable ::@:: Then the iterated integrals may be evaluated in any coordinate order. <!--SR:!2026-05-06,14,290!2026-05-06,14,290-->
- why nonnegativity or absolute integrability allows order exchange ::@:: The order of integration can be exchanged when nonnegativity or absolute integrability prevents cancellation problems and guarantees the iterated integrals all represent the same total mass. <!--SR:!2026-05-06,14,290!2026-05-06,14,290-->
- improper multiple integrals on $\mathbb{R}^n$ ::@:: One defines $\int_{\mathbb{R}^n} f(x)\,d^n x$ by truncating to larger and larger rectangles and taking the corresponding limit when it exists. <!--SR:!2026-05-08,16,290!2026-05-08,16,290-->
- half-infinite boxes $(-\infty,b_1]\times\cdots\times(-\infty,b_n]$ ::@:: Integrals over such sets are defined by truncating only the infinite sides and then taking limits. <!--SR:!2026-05-06,14,290!2026-05-08,16,290-->
- why half-infinite boxes encode events $\{X_1\le b_1,\ldots,X_n\le b_n\}$ ::@:: Half-infinite boxes are the natural domains for joint cumulative distribution functions, because events like $\{X_1\le b_1,\ldots,X_n\le b_n\}$ are exactly of that form. <!--SR:!2026-05-07,15,290!2026-05-08,16,290-->
- intuition for Fubini's theorem ::@:: Fubini says the same total mass is being counted in different slicing orders; if nonnegativity or absolute integrability removes ambiguity from cancellation, then all coordinate orders must agree. <!--SR:!2026-05-08,16,290!2026-05-06,14,290-->
- truncation intuition for improper multiple integrals ::@:: One first computes the mass inside a large finite observation window and then lets the window expand; if the values stabilize, that limiting total is the improper multiple integral. <!--SR:!2026-05-08,16,290!2026-05-06,14,290-->

## rectangle and cuboid calculations

The appendix includes two explicit calculations.

First, for $f(x_1,x_2)=x_1x_2^2$ on $[0,2]\times[0,1]$, one proceeds in short steps: (1) integrate in $x_2$ first while treating $x_1$ as a constant, so $\int_0^1 x_1x_2^2\,dx_2=x_1\left[\frac{x_2^3}{3}\right]_0^1=x_1/3$; (2) the double integral is therefore $\int_0^2 x_1/3\,dx_1$; (3) integrating in $x_1$ gives $\frac13\left[\frac{x_1^2}{2}\right]_0^2=\frac23$. So $$\int_{[0,2]\times[0,1]} f(x_1,x_2)\,d^2x=\frac23.$$ The point is that in the inner integral $x_1$ is treated as a constant.

Second, for $f(x_1,x_2,x_3)=\cos(x_1)x_2\exp(x_2x_3)$ on $[0,1]\times[2,3]\times[1,4]$, one again goes from the inside out: (1) integrate in $x_3$, obtaining $\cos(x_1)x_2\left[\frac1{x_2}\exp(x_2x_3)\right]_{x_3=1}^{x_3=4}=\cos(x_1)(e^{4x_2}-e^{x_2})$; (2) integrate this in $x_2$ to get $\cos(x_1)\left[\frac14 e^{4x_2}-e^{x_2}\right]_{x_2=2}^{x_2=3}$; (3) what remains is a constant multiple of $\int_0^1\cos(x_1)\,dx_1=[\sin(x_1)]_0^1$. Therefore $$\int_{[0,1]\times[2,3]\times[1,4]} f(x_1,x_2,x_3)\,d^3x=\left(\frac14 e^8(e^4-1)-(e-1)e^2\right)\sin(1).$$ The only subtle point is that dividing by $x_2$ during the inner antiderivative is legitimate because $x_2\in[2,3]$ never vanishes.

These examples are not just drill. They are the model for the later probability calculation strategy: identify which variables are currently being integrated, freeze the others as constants, and simplify step by step. The first example is intentionally simple so that the reader sees the mechanical slicing idea without extra algebraic noise; the second shows the same strategy in a less forgiving three-variable setting.

---

Flashcards for this section are as follows:

- calculate $\int_{[0,2]\times[0,1]} x_1x_2^2\,d^2x$ with brief steps ::@:: (1) Inner integral: $\int_0^1 x_1x_2^2\,dx_2=x_1\left[\frac{x_2^3}{3}\right]_0^1=x_1/3$. <br/> (2) Outer integral: $\int_0^2 x_1/3\,dx_1=\frac13\left[\frac{x_1^2}{2}\right]_0^2=\frac23$. So the value is $\frac23$. <!--SR:!2026-05-08,16,290!2026-05-07,15,290-->
- why $x_1$ is treated as constant in the first example ::@:: In the inner integral with respect to $x_2$, the variable $x_1$ is an outer variable and is therefore treated as a constant. <!--SR:!2026-05-06,14,290!2026-05-07,15,290-->
- calculate $\int_{[0,1]\times[2,3]\times[1,4]} \cos(x_1)x_2\exp(x_2x_3)\,d^3x$ with brief steps ::@:: (1) Integrate in $x_3$: $\cos(x_1)x_2\left[\frac1{x_2}e^{x_2x_3}\right]_{1}^{4}=\cos(x_1)(e^{4x_2}-e^{x_2})$. <br/> (2) Integrate in $x_2$: $\cos(x_1)\left[\frac14 e^{4x_2}-e^{x_2}\right]_{2}^{3}$. <br/> (3) Integrate in $x_1$: $\int_0^1\cos(x_1)\,dx_1=[\sin(x_1)]_0^1$, giving $\left(\frac14 e^8(e^4-1)-(e-1)e^2\right)\sin(1)$. <!--SR:!2026-05-06,14,290!2026-05-06,14,290-->
- why dividing by $x_2$ is legitimate in the cuboid example ::@:: The antiderivative with respect to $x_3$ introduces a factor $1/x_2$, and this is safe because on the domain one always has $x_2\in[2,3]$, so $x_2\neq0$. <!--SR:!2026-05-06,14,290!2026-05-07,15,290-->
- strategy behind the rectangle and cuboid calculations ::@:: The method is always the same: choose the current integration variable, freeze the outer variables as constants, simplify that one-variable integral, and then move outward one layer at a time. <!--SR:!2026-05-07,15,290!2026-05-06,14,290-->

<!-- check: ignore-next-line[header_style]: proper noun -->
## Jordan nullsets and Jordan-measurable sets

To integrate over non-rectangular domains, the appendix first isolates the right notion of "small boundary." A set $M\subseteq\mathbb{R}^n$ is a _Jordan nullset_ if for every $\varepsilon>0$ there exist finitely many rectangles covering $M$ whose total volume is less than $\varepsilon$. A bounded set $S\subseteq\mathbb{R}^n$ is _Jordan-measurable_ if its topological boundary $\partial S$ is a Jordan nullset.

The key examples are exactly the ones needed in calculus and probability. Every finite set is Jordan null because each point can be covered by a tiny rectangle. Every subset of a Jordan nullset is again Jordan null, and finite unions of Jordan nullsets are Jordan null. In $\mathbb{R}^n$, every $(n-1)$-dimensional rectangle is Jordan null because one can give it an arbitrarily thin thickness in the missing dimension. Also, if $f$ is continuous on a compact set $A$, then its graph $$\Gamma(f)=\{(x,f(x)):x\in A\}\subseteq\mathbb{R}^{n+1}$$ is Jordan null. Intuitively, uniform continuity lets one trap the graph inside finitely many very thin boxes.

It helps to compare this with the role of single points in one-dimensional integration. On the real line, changing a bounded function at one point does not change its Riemann integral because one point has no length. In higher dimensions, Jordan nullsets play the same role: they are the sets that occupy no genuine $n$-dimensional bulk. So they are negligible for volume-based integration even if they are geometrically visible.

The integrability criterion is then: if $Q\subseteq\mathbb{R}^n$ is a rectangle, $f\colon Q\to\mathbb{R}$ is bounded, and the set of discontinuities of $f$ is a Jordan nullset, then $f$ is Riemann-integrable on $Q$. So sparse discontinuities do not obstruct Riemann integration in higher dimensions.

The right interpretation is that a Jordan nullset is too thin to affect volume. A lower-dimensional boundary may still be geometrically visible, but it occupies no genuine $n$-dimensional bulk. That is why changing a function on such a set does not alter the integral: the region where the ambiguity lives has no volume to contribute. Jordan measurability is therefore the condition that the boundary of a region is negligible enough that the interior volume is well defined from the Riemann point of view.

From this one gets the useful corollary for integration over regions. If $A$ is bounded and Jordan-measurable and $f\colon A\to\mathbb{R}$ is bounded with Jordan-null discontinuity set $D_f$, then $f$ is Riemann-integrable over $A$. The proof is short: extend the problem to a surrounding rectangle $Q$ and consider $\mathbf{1}_A f$. Every discontinuity of $\mathbf{1}_A f$ lies either in $D_f$ or on the boundary $\partial A$, so the discontinuity set is contained in $D_f\cup\partial A$. Both pieces are Jordan null, hence their union is Jordan null, and the rectangle criterion then implies that $\mathbf{1}_Af$ is Riemann-integrable on $Q$.

---

Flashcards for this section are as follows:

- Jordan nullset in $\mathbb{R}^n$ ::@:: A set $M\subseteq\mathbb{R}^n$ is a Jordan nullset if for every $\varepsilon>0$ it can be covered by finitely many rectangles whose total volume is less than $\varepsilon$. <!--SR:!2026-05-06,14,290!2026-05-07,15,290-->
- Jordan-measurable set $S\subseteq\mathbb{R}^n$ ::@:: A bounded set $S\subseteq\mathbb{R}^n$ is Jordan-measurable if its boundary $\partial S$ is a Jordan nullset. <!--SR:!2026-05-08,16,290!2026-05-08,16,290-->
- finite subsets of $\mathbb{R}^n$ are Jordan null ::@:: Every finite subset of $\mathbb{R}^n$ is Jordan null because each point can be covered by an arbitrarily small rectangle. <!--SR:!2026-05-07,15,290!2026-05-07,15,290-->
- $(n-1)$-dimensional rectangles in $\mathbb{R}^n$ are Jordan null ::@:: Each can be thickened into a genuine $n$-dimensional rectangle with arbitrarily small volume. <!--SR:!2026-05-06,14,290!2026-05-06,14,290-->
- graph $\Gamma(f)=\{(x,f(x)):x\in A\}$ of a continuous function on compact $A$ ::@:: It is Jordan null in the ambient higher-dimensional space. <!--SR:!2026-05-07,15,290!2026-05-08,16,290-->
- integrability criterion when the discontinuity set $D_f$ is Jordan null ::@:: If a bounded function on a rectangle is discontinuous only on a Jordan nullset, then it is Riemann-integrable on that rectangle. <!--SR:!2026-05-07,15,290!2026-05-08,16,290-->
- intuition for Jordan nullsets as sets of $n$-dimensional volume $0$ ::@:: A Jordan nullset is too thin to carry any genuine $n$-dimensional volume, so changing a bounded function only on such a set does not change the multiple integral. <!--SR:!2026-05-08,16,290!2026-05-07,15,290-->
- comparison with one-dimensional negligible sets such as a single point in $\mathbb{R}$ ::@:: In one variable, a single point is negligible because it has no length; in higher dimensions, Jordan nullsets are the analogous negligible sets because they have no genuine $n$-dimensional volume. <!--SR:!2026-05-06,14,290!2026-05-07,15,290-->
- intuition for Jordan-measurability via the boundary $\partial S$ ::@:: A bounded set is Jordan-measurable when its boundary is negligible enough that the region has a well-defined volume from the Riemann point of view. <!--SR:!2026-05-08,16,290!2026-05-08,16,290-->
- corollary for bounded Jordan-measurable $A$ with proof idea ::@:: If $A$ is bounded and Jordan-measurable and $f$ is bounded with Jordan-null discontinuity set $D_f$, then $f$ is Riemann-integrable over $A$ because every discontinuity of $\mathbf{1}_Af$ lies in $D_f\cup\partial A$, and this union is Jordan null. <!--SR:!2026-05-07,15,290!2026-05-06,14,290-->

## integrating over subsets of rectangles

Suppose $A\subseteq Q$ where $Q$ is a rectangle and $f\colon A\to\mathbb{R}$ is bounded. The appendix defines integration over $A$ by extending $f$ arbitrarily outside $A$ and integrating the indicator-weighted function $$\mathbf{1}_A(x)f(x)$$ over the ambient rectangle $Q$. Thus $$\int_A f(x)\,d^n x:=\int_Q \mathbf{1}_A(x)f(x)\,d^n x$$ whenever the right-hand side is Riemann-integrable.

This definition becomes useful because the discontinuities of $\mathbf{1}_Af$ come only from two sources: discontinuities of $f$ inside $A$ and the boundary of $A$ itself. Therefore, if $A$ is bounded and Jordan-measurable and $f$ is bounded with a Jordan-null discontinuity set, then $f$ is Riemann-integrable over $A$. This is the precise mechanism behind integrating over regions bounded by curves or surfaces rather than only over rectangles.

The indicator function should be read as an on/off switch. Inside the target region $A$ it leaves the function unchanged; outside $A$ it kills the contribution completely. So one replaces "integrate over a curved region" by "integrate over a big rectangle, but turn the integrand off outside the region of interest."

In probability language, this is the step that lets one interpret $$P[(X,Y)\in A]=\int_A f_{X,Y}(x,y)\,d^2x$$ for a joint density and a non-rectangular event region $A$.

---

Flashcards for this section are as follows:

- integrating $\int_A f(x)\,d^n x$ over a subset $A\subseteq Q$ ::@:: One defines it by integrating the indicator-weighted function $\mathbf{1}_A f$ over the ambient rectangle $Q$, provided that function is Riemann-integrable. <!--SR:!2026-05-08,16,290!2026-05-06,14,290-->
- why multiplying by $\mathbf{1}_A$ isolates the region $A$ ::@:: Multiplying by $\mathbf{1}_A$ forces the integrand to contribute only on $A$, so integrating over the ambient rectangle is equivalent to integrating over the region itself. <!--SR:!2026-05-08,16,290!2026-05-06,14,290-->
- corollary for bounded Jordan-measurable $A$ ::@:: If $A$ is bounded and Jordan-measurable and $f$ is bounded with a Jordan-null discontinuity set, then $f$ is Riemann-integrable over $A$ because the discontinuities of $\mathbf{1}_Af$ lie inside $D_f\cup\partial A$, which is still Jordan null. <!--SR:!2026-05-08,16,290!2026-05-07,15,290-->
- probability meaning of $P[(X,Y)\in A]$ for a joint density $f_{X,Y}$ ::@:: The probability of a non-rectangular event region $A$ is computed by $P[(X,Y)\in A]=\int_A f_{X,Y}(x,y)\,d^2x$. <!--SR:!2026-05-06,14,290!2026-05-07,15,290-->
- indicator-function intuition for the factor $\mathbf{1}_A$ ::@:: The factor $\mathbf{1}_A$ acts like an on/off gate: it keeps the integrand inside the region of interest and turns it off outside, so integration over a curved domain is reduced to integration over a rectangle with a gated integrand. <!--SR:!2026-05-08,16,290!2026-05-08,16,290-->

## variable-bound regions and probability calculations

A standard planar domain has the form $$A=\{(x_1,x_2):x_1\in[a_1,b_1],\ x_2\in[u(x_1),v(x_1)]\},$$ where $u$ and $v$ are sufficiently regular and satisfy $u(x_1)\le v(x_1)$. Then $$\int_A f(x_1,x_2)\,d^2x=\int_{a_1}^{b_1}\left(\int_{u(x_1)}^{v(x_1)} f(x_1,x_2)\,dx_2\right)dx_1.$$ More generally, in $\mathbb{R}^n$ one may integrate over regions described by nested variable bounds, integrating from the inside out exactly as the bounds are specified.

When $f\equiv1$, these formulas recover geometry: in two dimensions $\int_A 1\,d^2x$ is the area of $A$, and in three dimensions the corresponding triple integral gives the volume of the region.

The geometric intuition is a sweep process. For each fixed outer variable, one draws the inner slice of the region and integrates over that slice. Then one sweeps those slice-values across the allowable outer range. In probability language, one is describing an event region one slice at a time.

The appendix gives two important examples. First, the region $$V=\{(x,y,z):0\le x\le1,\ 0\le y\le2x,\ 0\le z\le x+y\}$$ has volume $$\int_0^1\left(\int_0^{2x}\left(\int_0^{x+y}1\,dz\right)dy\right)dx=\frac43.$$ Second, if $(X,Y)$ has joint density $f_{X,Y}$ supported on $[0,1]^2$ and one wants $$P[X^2\le Y],$$ then the relevant region is $$A=\{(x,y):0\le x\le1,\ x^2\le y\le1\},$$ so $$P[X^2\le Y]=\int_0^1\left(\int_{x^2}^1 f_{X,Y}(x,y)\,dy\right)dx.$$ That example is the direct prototype for probability computations with joint densities over curved regions: first draw the event, then translate it into bounds, then integrate.

---

Flashcards for this section are as follows:

- region $A=\{(x_1,x_2):x_1\in[a_1,b_1],\ u(x_1)\le x_2\le v(x_1)\}$ ::@:: Then $\int_A f(x_1,x_2)\,d^2x=\int_{a_1}^{b_1}\left(\int_{u(x_1)}^{v(x_1)} f(x_1,x_2)\,dx_2\right)dx_1$. <!--SR:!2026-05-06,14,290!2026-05-06,14,290-->
- higher-dimensional nested-bound regions ::@:: In higher dimensions, one integrates over a region with nested variable bounds by reading the bounds from inside out and performing the corresponding iterated integral in that order. <!--SR:!2026-05-07,15,290!2026-05-07,15,290-->
- area and volume when $f\equiv1$ ::@:: The multiple integral measures geometric size: area in two dimensions and volume in three dimensions. <!--SR:!2026-05-06,14,290!2026-05-08,16,290-->
- calculate the volume of $V=\{(x,y,z):0\le x\le1,\ 0\le y\le2x,\ 0\le z\le x+y\}$ with brief steps ::@:: (1) Inner integral: $\int_0^{x+y}1\,dz=x+y$. <br/> (2) Next integral: $\int_0^{2x}(x+y)\,dy=\left[xy+\frac12 y^2\right]_0^{2x}=4x^2$. <br/> (3) Outer integral: $\int_0^1 4x^2\,dx=4\left[\frac{x^3}{3}\right]_0^1=\frac43$. So the volume is $\frac43$. <!--SR:!2026-05-07,15,290!2026-05-08,16,290-->
- region for $P[X^2\le Y]$ ::@:: If $(X,Y)$ has joint density on $[0,1]^2$, then the event $\{X^2\le Y\}$ corresponds to the region $A=\{(x,y):0\le x\le1,\ x^2\le y\le1\}$. <!--SR:!2026-05-06,14,290!2026-05-08,16,290-->
- probability of $X^2\le Y$ over $A=\{(x,y):0\le x\le1,\ x^2\le y\le1\}$ ::@:: One has $P[X^2\le Y]=\int_0^1\left(\int_{x^2}^1 f_{X,Y}(x,y)\,dy\right)dx$. <!--SR:!2026-05-07,15,290!2026-05-08,16,290-->
- why variable-bound regions matter for joint-density problems ::@:: Joint-density probability problems are usually solved by translating the event into a geometric region and then writing the corresponding iterated integral with the correct variable bounds. <!--SR:!2026-05-07,15,290!2026-05-08,16,290-->
- sweep interpretation for variable-bound regions ::@:: A variable-bound integral computes one slice of the region at a time and then sweeps those slice-contributions across the outer variable; probabilistically, this is the standard way to turn a curved event region into a formula. <!--SR:!2026-05-06,14,290!2026-05-08,16,290-->
