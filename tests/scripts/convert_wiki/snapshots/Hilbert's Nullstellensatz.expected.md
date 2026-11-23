In [mathematics](mathematics.md), __Hilbert's Nullstellensatz__ \(German for "theorem of zeros" or, more literally, "zero-locus-theorem"\) is a theorem that establishes a fundamental relationship between [geometry](geometry.md) and [algebra](algebra.md). It was proven by [David Hilbert](David%20Hilbert.md) in his second major paper on [invariant theory](invariant%20theory.md) in 1893 \(following his seminal 1890 paper in which he proved [Hilbert's basis theorem](Hilbert's%20basis%20theorem.md)\) and became a foundational result of [algebraic geometry](algebraic%20geometry.md).

There are several formulations of the Nullstellensatz, the most elementary of which deal with conditions for the existence of solutions to systems of multivariate polynomial equations over an algebraically closed field \(such as the complex numbers $\mathbb{C}$\). The __weak Nullstellensatz__ is a [corollary](corollary.md) \(or a [lemma](lemma%20(mathematics).md), depending which is proved first\) of the Nullstellensatz which can be stated as follows.<sup>[\[1\]](#^ref-1)</sup> Consider a [system of polynomial equations](system%20of%20polynomial%20equations.md)

$$\begin{cases} f_1(x_1, \dots, x_n) = 0 \\ \vdots \\ f_m(x_1, \ldots, x_n) = 0 \end{cases}$$

in the variables $x_1, \dots, x_n\in K$, where $f_1, \dots, f_m \in K[X_1, \dots, X_n]$ are [multivariate polynomials](multivariate%20polynomial.md#multivariate%20polynomial) over an [algebraically closed field](algebraically%20closed%20field.md) $K$. If the system does _not_ have a solution $(a_1, \dots, a_n) \in K^n$, then there is an "algebraic reason" for this situation: namely, this occurs precisely when there exist polynomials $g_1, \dots, g_m \in K[X_1, \dots, X_n]$ such that

$$g_1 f_1 + \cdots + g_m f_m = 1.$$

Since the expression on the left-hand side must evaluate to 0 at any $(a_1, \dots, a_n)$ that solves the system of equations, it is obvious from the inconsistency that no solution can exist if this condition holds. Informally, the \(weak\) Nullstellensatz asserts that in the absence of such an inconsistency, a solution to the system of equations must exist.

The full Nullstellensatz is the following refinement: If $f\in K[X_1,\dots,X_n]$ is a polynomial such that every solution of the system of equations is also a solution of

$$f(x_1, \dots, x_n) = 0,$$

then there is a similar type of "algebraic reason" for this occurrence: this occurs precisely when there exist a natural number $r$ and polynomials $g_1, \dots, g_m$ such that

$$f^r = g_1 f_1 + \cdots + g_m f_m.$$

## formulations

Let _k_ be a [field](field%20(mathematics).md) \(such as the [rational numbers](rational%20number.md)\) and _K_ be an algebraically closed [field extension](field%20extension.md) of _k_ \(such as the [complex numbers](complex%20number.md)\). Consider the [polynomial ring](polynomial%20ring.md) $k[X_1, \ldots, X_n]$ and let $J$ be an [ideal](ideal%20(ring%20theory).md) in this ring. The [algebraic set](algebraic%20set.md) $\mathrm V(J)$ defined by this ideal consists of all $n$-tuples $a = (a_1, \dots, a_n)$ in $K^n$ such that $f(a) = 0$ for all $f\in J$. Hilbert's Nullstellensatz states that if $p$ is a polynomial in $k[X_1, \ldots, X_n]$ that vanishes on the algebraic set $\mathrm V(J)$, i.e., $p(a) = 0$ for all $a \in \mathrm V(J)$, then there exists a [natural number](natural%20number.md) $r$ such that $p^r\in J$.<sup>[\[2\]](#^ref-2)</sup>

With the notation common in algebraic geometry, the Nullstellensatz can be formulated as

$$\hbox{I}(\hbox{V}(J))=\sqrt{J}$$

for every ideal $J$ in $K[X_1,...,X_n]$ with $K$ algebraically closed. Here, $\sqrt{J}$ denotes the [_radical_](radical%20of%20an%20ideal.md) of $J$ \($p\in\sqrt{J}$ [if and only if](if%20and%20only%20if.md) $\exists r\in\mathbb{N},\ p^r \in J$\), $\mathrm{I} (U)$ is the _vanishing ideal_ of $U$ \(the set of polynomials that vanish at the points in $U$\), and $\mathrm{V} (J)$ is the _zero locus_ of $J$ \(the set of points at which the polynomials in $J$ vanish\). The assertion that $\hbox{I}(\hbox{V}(J))\subseteq\sqrt{J}$ is equivalent to the first formulation above with $k = K$ algebraically closed, while the opposite inclusion is a straightforward consequence of the definitions.

An immediate corollary is the __weak Nullstellensatz__: If $J$ is a proper ideal in $k[X_1, \ldots, X_n]$, then $\mathrm{V} (J)$ is nonempty, i.e., for every algebraically closed extension $K\supseteq k$, there exists a common zero in $K^n$ for all the polynomials in the ideal $J$.<sup>[\[3\]](#^ref-3)</sup> This is the reason for the name of the theorem, the full version of which can be proved easily from the 'weak' form using the [Rabinowitsch trick](Rabinowitsch%20trick.md). The assumption of considering common zeros in an algebraically closed field is essential here; for example, the elements of the proper ideal $(X^2+1)$ in $\R[X]$ do not have a common zero in $\R$.

Specializing to the case of a single polynomial when $K=\mathbb{C}$ and $n=1$, one immediately recovers a restatement of the [fundamental theorem of algebra](fundamental%20theorem%20of%20algebra.md): A polynomial $P$ in $\mathbb{C}[X]$ has a root in $\mathbb{C}$ if and only if $\deg P\neq 0$. For this reason, the \(weak\) Nullstellensatz applied to $K=\mathbb{C}$ can be thought of as a generalization of the fundamental theorem of algebra to systems of multivariable polynomial equations.<sup>[\[4\]](#^ref-4)</sup>

Taking _K_ to be algebraically closed, the Nullstellensatz establishes an order-reversing [bijective](bijective.md) correspondence between the algebraic sets in $K^n$ and the [radical ideals](radical%20ideal.md) of $K[X_1, \ldots, X_n]$. In fact, more generally, one has a [Galois connection](Galois%20connection.md) between subsets of the space and subsets of the algebra, where "[Zariski closure](Zariski%20closure.md)" and "radical of the ideal generated" are the [closure operators](closure%20operator.md).

As a particular example, consider an algebraic set consisting of a single point $a = (a_1, \dots, a_n) \in K^n$. Then $\mathrm{I} (\{a\}) = (X_1 - a_1, \ldots, X_n - a_n)$ is a maximal ideal. Conversely, every [maximal ideal](maximal%20ideal.md) of the polynomial ring $K[X_1,\ldots,X_n]$ \(note that $K$ is algebraically closed\) is of the form $(X_1 - a_1, \ldots, X_n - a_n)$ for some $a_1,\ldots,a_n \in K$. This characterization of maximal ideals of polynomial rings over algebraically closed fields is another common formulation of the weak Nullstellensatz. As another example of this correspondence and a consequence of the Nullstellensatz, one can show that an algebraic subset $W$ in _$$K^n$$_ is [irreducible](irreducible%20space.md) \(in the Zariski topology\) if and only if $\mathrm{I} (W)$ is a [prime ideal](prime%20ideal.md).

More generally, for any ideal $J$ in $K[X_1,...,X_n]$,

$$\sqrt{J} = \bigcap_{\mathfrak{m}\supseteq J} \mathfrak{m} = \bigcap_{(a_1,\dots, a_n) \in \mathrm{V} (J)} (X_1 - a_1, \dots, X_n - a_n),$$

where the first intersection is taken over maximal ideals $\mathfrak{m} \subsetneq K[X_1,...,X_n]$. This relationship is yet another common formulation of the Nullstellensatz. \(The first equality actually holds for ideals in any [Jacobson ring](Jacobson%20ring.md), including any finitely generated algebra over a field, while the second equality holds for algebraically closed _K_.\)

## proofs

There are many known proofs of the theorem. Some are [non-constructive](constructive%20proof.md), such as the first one. Others are constructive, as based on [algorithms](algorithm.md) for expressing 1 or _p<sup>r</sup>_ as a [linear combination](linear%20combination.md) of the generators of the ideal.

### using Zariski's lemma

[Zariski's lemma](Zariski's%20lemma.md) asserts that if a field is [finitely generated](finitely%20generated%20algebra.md) as an [associative algebra](associative%20algebra.md) over a field _K_, then it is a [finite field extension](finite%20field%20extension.md#definition%20and%20notation) of _K_ \(that is, it is also finitely generated as a [vector space](vector%20space.md)\). If $K$ is an algebraically closed field and $\mathfrak{m}$ is a maximal ideal of the ring of polynomials $K[X_1,\ldots,X_n]$, then Zariski's lemma implies that $K[X_1,\ldots,X_n]/ \mathfrak{m}$ is a finite field extension of $K$, and thus, by algebraic closure, must be _K_. From this, it follows that there is an $a = (a_1,\dots,a_n)\in K^n$ such that $X_i-a_i\in\mathfrak{m}$ for $i=1,\dots, n$. In other words,

$$\mathfrak{m} \supseteq \mathfrak{m}_a=(X_1 - a_1, \ldots, X_n - a_n)$$

for some $a = (a_1,\dots,a_n)\in K^n$. But $\mathfrak{m}_a$ is clearly maximal, so $\mathfrak{m}=\mathfrak{m}_a$. This is the weak Nullstellensatz: every maximal ideal of $K[X_1,\ldots,X_n]$ for algebraically closed _K_ is of the form $\mathfrak{m}_a=(X_1 - a_1, \ldots, X_n - a_n)$ for some $a = (a_1,\dots,a_n)\in K^n$. Because of this close relationship, some texts refer to Zariski's lemma as the weak Nullstellensatz or as the 'algebraic version' of the weak Nullstellensatz.<sup>[\[5\]](#^ref-5)</sup><sup>[\[6\]](#^ref-6)</sup>

The full Nullstellensatz can also be proved directly from Zariski's lemma without employing the Rabinowitsch trick. Here is a sketch of a proof using this lemma.<sup>[\[7\]](#^ref-7)</sup>

Let $A = K[X_1, \ldots, X_n]$ for algebraically closed field $K$, and let $J$ be an ideal of $A$ and $V=\mathrm{V}(J)$ be the common zeros of $J$ in $K^n$. Recall that $\mathrm{I}(V)$ is radical, and therefore $\sqrt{J} \subseteq \mathrm{I}(V)$, where $\mathrm{I}(V)$ is the ideal of polynomials in $A$ vanishing on $V$. To show the opposite inclusion, let $f \not\in \sqrt{J}$. Then $f \not\in \mathfrak{p}$ for some prime ideal $\mathfrak{p} \supseteq J$ in _A_. Let $R = (A/\mathfrak{p}) [1/\bar{f}]$, where $\bar{f}$ is the image of $f$ under the natural map $A \to A/\mathfrak{p}$, and $\mathfrak{m}$ be a maximal ideal in $R$. By Zariski's lemma, $R/\mathfrak{m}$ is a finite extension of $K$, and thus, is $K$ since $K$ is algebraically closed. Let $x_i$ be the images of $X_i$ under the natural map $A \to A/\mathfrak{p}\to R \to R/\mathfrak{m}\cong K$. It follows that, by construction, $x = (x_1, \ldots, x_n) \in V$ but $f(x) \ne 0$, so $f \notin \mathrm{I}(V)$.

### using resultants

The following constructive proof of the weak form is one of the oldest proofs \(the strong form results from the [Rabinowitsch trick](Rabinowitsch%20trick.md), which is also constructive\).

The [resultant](resultant.md) of two polynomials depending on a variable _x_ and other variables is a polynomial in the other variables that is in the ideal generated by the two polynomials, and has the following properties: if one of the polynomials is [monic](monic%20polynomial.md) in _x_, every zero \(in the other variables\) of the resultant may be extended into a common zero of the two polynomials.

The proof is as follows.

If the ideal is [principal](principal%20ideal.md), generated by a non-constant polynomial _p_ that depends on _x_, one chooses arbitrary values for the other variables. The [fundamental theorem of algebra](fundamental%20theorem%20of%20algebra.md) asserts that this choice can be extended to a zero of _p_.

In the case of several polynomials $p_1,\ldots, p_n$, a linear change of variables allows to suppose that $p_1$ is monic in the first variable _x_. Then, one introduces $n-1$ new variables $u_2, \ldots, u_n$, and one considers the resultant

$$R=\operatorname{Res}_x(p_1,u_2p_2+\cdots +u_np_n).$$

As _R_ is in the ideal generated by $p_1,\ldots, p_n$, the same is true for the coefficients in _R_ of the [monomials](monomial.md) in $u_2, \ldots, u_n$. So, if 1 is in the ideal generated by these coefficients, it is also in the ideal generated by $p_1,\ldots, p_n$. On the other hand, if these coefficients have a common zero, this zero can be extended to a common zero of $p_1,\ldots, p_n$, by the above property of the resultant.

This proves the weak Nullstellensatz by induction on the number of variables.

### using Gröbner bases

A [Gröbner basis](Gröbner%20basis.md) is an algorithmic concept that was introduced in 1973 by [Bruno Buchberger](Bruno%20Buchberger.md). It is presently fundamental in [computational geometry](computational%20geometry.md). A Gröbner basis is a special generating set of an ideal from which most properties of the ideal can easily be extracted. Those that are related to the Nullstellensatz are the following:

- An ideal contains 1 if and only if its [reduced Gröbner basis](reduced%20Gröbner%20basis.md#reduced) \(for any [monomial ordering](monomial%20ordering.md)\) is 1.
- The number of the common zeros of the polynomials in a Gröbner basis is strongly related to the number of [monomials](monomial.md) that are [irreducibles](Gröbner%20basis.md#reduction) by the basis. Namely, the number of common zeros is infinite if and only if the same is true for the irreducible monomials; if the two numbers are finite, the number of irreducible monomials equals the numbers of zeros \(in an algebraically closed field\), counted with multiplicities.
- With a [lexicographic monomial order](lexicographic%20order.md), the common zeros can be computed by solving iteratively [univariate polynomials](univariate%20polynomial.md#univariate) \(this is not used in practice since one knows better algorithms\).
- Strong Nullstellensatz: a power of _p_ belongs to an ideal _I_ if and only the [saturation](Gröbner%20basis.md#saturation) of _I_ by _p_ produces the Gröbner basis 1. Thus, the strong Nullstellensatz results almost immediately from the definition of the saturation.

## generalizations

The Nullstellensatz is subsumed by a systematic development of the theory of [Jacobson rings](Jacobson%20ring.md), which are those rings in which every radical ideal is an intersection of maximal ideals. Given Zariski's lemma, proving the Nullstellensatz amounts to showing that if _k_ is a field, then every finitely generated [_k_-algebra](K-algebra.md) _R_ \(necessarily of the form $R = k[t_1,\cdots,t_n]/I$\) is Jacobson. More generally, one has the following theorem:

&nbsp;&nbsp;&nbsp;&nbsp; Let $R$ be a Jacobson ring. If $S$ is a finitely generated [_R_-algebra](R-algebra.md), then $S$ is a Jacobson ring. Furthermore, if $\mathfrak{n}\subseteq S$ is a maximal ideal, then $\mathfrak{m} := \mathfrak{n} \cap R$ is a maximal ideal of $R$, and $S/\mathfrak{n}$ is a finite extension of $R/\mathfrak{m}$.<sup>[\[8\]](#^ref-8)</sup>

Other generalizations proceed from viewing the Nullstellensatz in [scheme-theoretic](scheme%20(mathematics).md) terms as saying that for any field _k_ and nonzero finitely generated _k_-algebra _R_, the morphism $\mathrm{Spec} \, R \to \mathrm{Spec} \, k$ admits a [section](section%20(category%20theory).md) étale-locally \(equivalently, after [base change](base%20change%20(scheme%20theory).md#base%20change%20and%20descent) along $\mathrm{Spec} \, L \to \mathrm{Spec} \, k$ for some finite field extension $L/k$\). In this vein, one has the following theorem:

&nbsp;&nbsp;&nbsp;&nbsp; Any [faithfully flat](faithfully%20flat%20morphism.md) morphism of schemes $f: Y \to X$ [locally of finite presentation](glossary%20of%20algebraic%20geometry.md#finite%20presentation) admits a _quasi-section_, in the sense that there exists a faithfully flat and locally [quasi-finite](quasi-finite%20morphism.md) morphism $g: X' \to X$ locally of finite presentation such that the base change $f': Y \times_X X' \to X'$ of $f$ along $g$ admits a section.<sup>[\[9\]](#^ref-9)</sup> Moreover, if $X$ is [quasi-compact](quasi-compact%20morphism.md) \(resp. quasi-compact and [quasi-separated](quasi-separated%20morphism.md)\), then one may take $X'$ to be affine \(resp. $X'$ affine and $g$ quasi-finite\), and if $f$ is [smooth](smooth%20morphism.md) surjective, then one may take $g$ to be [étale](étale%20morphism.md).<sup>[\[10\]](#^ref-10)</sup>

[Serge Lang](Serge%20Lang.md) gave an extension of the Nullstellensatz to the case of infinitely many generators:

&nbsp;&nbsp;&nbsp;&nbsp; Let $\kappa$ be an [infinite cardinal](infinite%20cardinal.md) and let $K$ be an algebraically closed field whose [transcendence degree](transcendence%20degree.md) over its [prime subfield](prime%20subfield.md#case%20of%20fields) is strictly greater than $\kappa$. Then for any set $S$ of cardinality $\kappa$, the polynomial ring $A = K[x_i]_{i \in S}$ satisfies the Nullstellensatz, i.e., for any ideal $J \sub A$ we have that $\sqrt{J} = \hbox{I} (\hbox{V} (J))$.<sup>[\[11\]](#^ref-11)</sup>

## effective Nullstellensatz

In all of its variants, Hilbert's Nullstellensatz asserts that some polynomial _g_ belongs or not to an ideal generated, say, by _f_<sub>1</sub>, ..., _f<sub>k</sub>_; we have _g_ = _f<sup> r</sup>_ in the strong version, _g_ = 1 in the weak form. This means the existence or the non-existence of polynomials _g_<sub>1</sub>, ..., _g<sub>k</sub>_ such that _g_ = _f_<sub>1</sub>_g_<sub>1</sub> + ... + _f<sub>k</sub>g<sub>k</sub>_. The usual proofs of the Nullstellensatz are not constructive, non-effective, in the sense that they do not give any way to compute the _g<sub>i</sub>_.

It is thus a rather natural question to ask if there is an effective way to compute the _g<sub>i</sub>_ \(and the exponent _r_ in the strong form\) or to prove that they do not exist. To solve this problem, it suffices to provide an upper bound on the total degree of the _g<sub>i</sub>_: such a bound reduces the problem to a finite [system of linear equations](system%20of%20linear%20equations.md) that may be solved by usual [linear algebra](linear%20algebra.md) techniques. Any such upper bound is called an __effective Nullstellensatz__.

A related problem is the __ideal membership problem__, which consists in testing if a polynomial belongs to an ideal. For this problem also, a solution is provided by an upper bound on the degree of the _g<sub>i</sub>_. A general solution of the ideal membership problem provides an effective Nullstellensatz, at least for the weak form.

In 1925, [Grete Hermann](Grete%20Hermann.md) gave an upper bound for ideal membership problem that is doubly exponential in the number of variables. In 1982 Mayr and Meyer gave an example where the _g<sub>i</sub>_ have a degree that is at least double exponential, showing that every general upper bound for the ideal membership problem is doubly exponential in the number of variables.

Since most mathematicians at the time assumed the effective Nullstellensatz was at least as hard as ideal membership, few mathematicians sought a bound better than double-exponential. In 1987, however, [W. Dale Brownawell](W.%20Dale%20Brownawell.md) gave an upper bound for the effective Nullstellensatz that is simply exponential in the number of variables.<sup>[\[12\]](#^ref-12)</sup> Brownawell's proof relied on analytic techniques valid only in [characteristic](characteristic%20(algebra).md) 0, but, one year later, [János Kollár](János%20Kollár.md) gave a purely algebraic proof, valid in any characteristic, of a slightly better bound.

In the case of the weak Nullstellensatz, Kollár's bound is the following:<sup>[\[13\]](#^ref-13)</sup>

&nbsp;&nbsp;&nbsp;&nbsp; Let _f_<sub>1</sub>, ..., _f<sub>s</sub>_ be polynomials in _n_ ≥ 2 variables, of total degree _d_<sub>1</sub> ≥ ... ≥ _d<sub>s</sub>_. If there exist polynomials _g<sub>i</sub>_ such that _f_<sub>1</sub>_g_<sub>1</sub> + ... + _f<sub>s</sub>g<sub>s</sub>_ = 1, then they can be chosen such that $$\deg(f_ig_i) \le \max(d_s,3)\prod_{j=1}^{\min(n,s)-1}\max(d_j,3).$$

&nbsp;&nbsp;&nbsp;&nbsp; This bound is optimal if all the degrees are greater than 2.

If _d_ is the maximum of the degrees of the _f<sub>i</sub>_, this bound may be simplified to

$$\max(3,d)^{\min(n,s)}.$$

An improvement due to M. Sombra is<sup>[\[14\]](#^ref-14)</sup>

$$\deg(f_ig_i) \le 2d_s\prod_{j=1}^{\min(n,s)-1}d_j.$$

His bound improves Kollár's as soon as at least two of the degrees that are involved are lower than 3.

## projective Nullstellensatz

We can formulate a certain correspondence between homogeneous ideals of polynomials and algebraic subsets of a projective space, called the __projective Nullstellensatz__, that is analogous to the affine one. To do that, we introduce some notations. Let $R = k[t_0, \ldots, t_n]$. The homogeneous ideal,

$$R_+ = \bigoplus_{d \geqslant 1} R_d$$

is called the _maximal homogeneous ideal_ \(see also [irrelevant ideal](irrelevant%20ideal.md)\). As in the affine case, we let: for a subset $S \subseteq \mathbb{P}^n$ and a homogeneous ideal $I$ of $R$,

$$\begin{aligned} \operatorname{I}_{\mathbb{P}^n}(S) &= \{ f \in R_+ \mid f = 0 \text{ on } S \}, \\ \operatorname{V}_{\mathbb{P}^n}(I) &= \{ x \in \mathbb{P}^n \mid f(x) = 0 \text{ for all } f \in I \}. \end{aligned}$$

By $f = 0 \text{ on } S$ we mean: for every homogeneous coordinates $(a_0 : \cdots : a_n)$ of a point of $S$ we have $f(a_0,\ldots, a_n)=0$. This implies that the homogeneous components of $f$ are also zero on $S$ and thus that $\operatorname{I}_{\mathbb{P}^n}(S)$ is a homogeneous ideal. Equivalently, $\operatorname{I}_{\mathbb{P}^n}(S)$ is the homogeneous ideal generated by homogeneous polynomials $f$ that vanish on $S$. Now, for any homogeneous ideal $I \subseteq R_+$, by the usual Nullstellensatz, we have:

$$\sqrt{I} = \operatorname{I}_{\mathbb{P}^n}(\operatorname{V}_{\mathbb{P}^n}(I)),$$

and so, like in the affine case, we have:<sup>[\[15\]](#^ref-15)</sup>

&nbsp;&nbsp;&nbsp;&nbsp; There exists an order-reversing one-to-one correspondence between proper homogeneous radical ideals of $R$ and subsets of $\mathbb{P}^n$ of the form $\operatorname{V}_{\mathbb{P}^n}(I)$. The correspondence is given by $\operatorname{I}_{\mathbb{P}^n}$ and $\operatorname{V}_{\mathbb{P}^n}$.

## Analytic Nullstellensatz \(Rückert’s Nullstellensatz\)

The Nullstellensatz also holds for the [germs](germ%20(mathematics).md) of holomorphic functions at a point of complex _n_-space $\Complex^n$. Precisely, for each open subset $U \subseteq \Complex^n$, let $\mathcal{O}_{\Complex^n}(U)$ denote the ring of holomorphic functions on _U_; then $\mathcal{O}_{\Complex^n}$ is a _[sheaf](sheaf%20(mathematics).md)_ on $\Complex^n$. The [stalk](stalk%20(sheaf).md) $\mathcal{O}_{\Complex^n, 0}$ at, say, the origin can be shown to be a [Noetherian](Noetherian%20ring.md) [local ring](local%20ring.md) that is a [unique factorization domain](unique%20factorization%20domain.md).

If $f \in \mathcal{O}_{\Complex ^n, 0}$ is a germ represented by a [holomorphic function](holomorphic%20function.md) $\widetilde{f}: U \to \Complex$, then let $V_0(f)$ be the [equivalence class](equivalence%20class.md) of the set

$$\left \{ z \in U \mid \widetilde{f}(z) = 0 \right\},$$

where two subsets $X, Y \subseteq \Complex^n$ are considered equivalent if $X \cap U = Y \cap U$ for some neighborhood _U_ of 0. Note $V_0(f)$ is independent of a choice of the representative $\widetilde{f}$. For each ideal $I \subseteq \mathcal{O}_{\Complex^n,0}$, let $V_0(I)$ denote $V_0(f_1) \cap \dots \cap V_0(f_r)$ for some generators $f_1, \ldots, f_r$ of $I$. It is well-defined; i.e., is independent of a choice of the generators.

For each subset $X \subseteq \Complex ^n$, let

$$I_0(X) = \left \{ f \in \mathcal{O}_{\Complex^n,0} \mid V_0(f) \supset X \right \}.$$

It is easy to see that $I_0(X)$ is an ideal of $\mathcal{O}_{\Complex ^n, 0}$ and that $I_0(X) = I_0(Y)$ if $X \sim Y$ in the sense discussed above.

The __analytic Nullstellensatz__ then states:<sup>[\[16\]](#^ref-16)</sup> for each ideal $I \subseteq \mathcal{O}_{\Complex ^n, 0}$,

$$\sqrt{I} = I_0(V_0(I))$$

where the left-hand side is the [radical](radical%20of%20an%20ideal.md) of $I$.

## formal Nullstellensatz

In classical algebraic geometry, the zero locus \('variety'\) operation \($V$\) is applied to subsets of the ring of polynomials over an algebraically closed field, while the vanishing ideal operation \($I$\) is applied to subsets of affine $n$-space, whose points are in one-to-one correspondence with the maximal ideals of the polynomial ring by the weak Nullstellensatz \(see above\). In [scheme theory](scheme%20(mathematics).md), $V$ and $I$ are generalized and redefined so that they could be applied to subsets of arbitrary commutative \(unital\) rings and their _prime_ spectra, respectively. In particular, for any [commutative ring](commutative%20ring.md) _A_, its set of prime ideals \([prime spectrum](spectrum%20of%20a%20ring.md)\) $\mathrm{Spec}\ A$, and subsets $S\subset A$ and $X\subset \mathrm{Spec}\ A$, we set <p> &nbsp;&nbsp;&nbsp;&nbsp; $\mathbb{V}(S) = \{\mathfrak{p}\in \mathrm{Spec}\ A \mid \mathfrak{p}\supset S\}$ and $\mathbb{I}(X)=\bigcap_{\mathfrak{p}\in X} \mathfrak{p}$. <p> Then for any ideal $J\triangleleft A$, a formal analogue of Hilbert's Nullstellensatz holds:

$$\mathbb{I}(\mathbb{V}(J)) = \bigcap_{\mathfrak{p}\in\mathbb{V}(J)}\mathfrak{p}= \bigcap_{\mathfrak{p}\in\mathrm{Spec}\ A,\ \mathfrak{p}\supset J}\mathfrak{p}=\sqrt{J},$$

where the last equality follows from a standard property of prime ideals from commutative algebra.<sup>[\[17\]](#^ref-17)</sup> In analogy to zero loci in the classical theory, the $\mathbb{V}(S)$ are used to define the closed sets in the [Zariski topology](Zariski%20topology.md) of $\mathrm{Spec}\ A$.<sup>[\[6\]](#^ref-6)</sup>

## see also

- [Artin–Tate lemma](Artin–Tate%20lemma.md)
- [Combinatorial Nullstellensatz](combinatorial%20Nullstellensatz.md#combinatorial%20Nullstellensatz)
- [Differential Nullstellensatz](differential%20Nullstellensatz.md#differential%20Nullstellensatz)
- [Real radical](real%20radical.md)
- [Restricted power series\#Tate algebra](restricted%20power%20series.md#Tate%20algebra), an analog of Hilbert's Nullstellensatz holds for Tate algebras.
- [Krivine–Stengle Positivstellensatz](Krivine–Stengle%20Positivstellensatz.md)
- [Weierstrass Nullstellensatz](Weierstrass%20Nullstellensatz.md)

## notes

1. <a id="CITEREFTao2007"></a> Tao, Terence \(2007-11-26\). ["Hilbert's nullstellensatz"](https://terrytao.wordpress.com/2007/11/26/hilberts-nullstellensatz/). _What's new_. Retrieved 2025-09-25. <a id="^ref-1"></a>^ref-1
2. [Zariski–Samuel](#CITEREFZariski–Samuel), Ch. VII, Theorem 14. <a id="^ref-2"></a>^ref-2
3. _Proof:_ If the polynomials in _J_ have no common zero in $K^n$, then $\mathrm{V}(J) = \emptyset$, and $p(a)=0$ for all $a\in \mathrm{V}(J)$ is vacuously true for any $p\in k[X_1,\dots,X_n]$, including the constant polynomial 1, so by the strong Nullstellensatz, we have $1^r\in J$, for some natural number _r_, but that means $1\in J$, and so _J_ must be the whole polynomial ring $k[X_1,\dots,X_n]$, Q.E.D. <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFCoxLittleO’Shea2015"></a> [Cox, David A.](David%20A.%20Cox.md); [Little, John](John%20B.%20Little%20(mathematician).md); [O’Shea, Donal](Donal%20O'Shea.md) \(2015\). [_Ideals, Varieties, and Algorithms: An Introduction to Computational Algebraic Geometry and Commutative Algebra_](https://link.springer.com/10.1007/978-3-319-16721-3). Undergraduate Texts in Mathematics. Cham: Springer International Publishing. [doi](doi%20(identifier).md):[10.1007/978-3-319-16721-3](https://doi.org/10.1007%2F978-3-319-16721-3). [ISBN](ISBN%20(identifier).md) [978-3-319-16720-6](https://en.wikipedia.org/wiki/Special:BookSources/978-3-319-16720-6). <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFPatilStorch2010"></a> Patil, Dilip P.; Storch, Uwe \(2010\). _Introduction to Algebraic Geometry and Commutative Algebra_. World Scientific. [ISBN](ISBN%20(identifier).md) [978-9814307581](https://en.wikipedia.org/wiki/Special:BookSources/978-9814307581). <a id="^ref-5"></a>^ref-5
6. <a id="CITEREFReid1995"></a> Reid, Miles \(1995\). _Undergraduate commutative algebra_. London Mathematical Society student texts. Cambridge ; New York: Cambridge University Press. [ISBN](ISBN%20(identifier).md) [978-0-521-45255-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-45255-7). <a id="^ref-6"></a>^ref-6
7. [Atiyah–Macdonald](#CITEREFAtiyah–Macdonald), Ch. 7, Exercise 7.14. <a id="^ref-7"></a>^ref-7
8. <a id="CITEREFEmerton"></a> Emerton, Matthew. ["Jacobson rings"](http://www.math.uchicago.edu/~emerton/pdffiles/jacobson.pdf) \(PDF\). [Archived](https://web.archive.org/web/20220725071929/http://www.math.uchicago.edu/~emerton/pdffiles/jacobson.pdf) \(PDF\) from the original on 2022-07-25. <a id="^ref-8"></a>^ref-8
9. [EGA](éléments%20de%20géométrie%20algébrique.md) §IV.17.16.2. <a id="^ref-9"></a>^ref-9
10. EGA §IV.17.16.3\(ii\). <a id="^ref-10"></a>^ref-10
11. <a id="CITEREFLang1952"></a> Lang, Serge \(1952\). ["Hilbert's Nullstellensatz in Infinite-Dimensional Space"](https://www.jstor.org/stable/2031893). _[Proc. Am. Math. Soc.](Proc.%20Am.%20Math.%20Soc..md)_ __3__ \(3\): 407–410. [doi](doi%20(identifier).md):[10.2307/2031893](https://doi.org/10.2307%2F2031893). [JSTOR](JSTOR%20(identifier).md#content) [2031893](https://www.jstor.org/stable/2031893). <a id="^ref-11"></a>^ref-11
12. <a id="CITEREFBrownawell1987"></a> Brownawell, W. Dale \(1987\), "Bounds for the degrees in the Nullstellensatz", _[Ann. of Math.](Ann.%20of%20Math..md)_, __126__ \(3\): 577–591, [doi](doi%20(identifier).md):[10.2307/1971361](https://doi.org/10.2307%2F1971361), [JSTOR](JSTOR%20(identifier).md#content) [1971361](https://www.jstor.org/stable/1971361), [MR](MR%20(identifier).md) [0916719](https://mathscinet.ams.org/mathscinet-getitem?mr=0916719) <a id="^ref-12"></a>^ref-12
13. <a id="CITEREFKollár1988"></a> Kollár, János \(1988\), ["Sharp Effective Nullstellensatz"](https://web.archive.org/web/20140303174253/https://www.math.ucdavis.edu/~deloera/MISC/BIBLIOTECA/trunk/Kollar/kollarnullstellen.pdf) \(PDF\), _[Journal of the American Mathematical Society](Journal%20of%20the%20American%20Mathematical%20Society.md)_, __1__ \(4\): 963–975, [doi](doi%20(identifier).md):[10.2307/1990996](https://doi.org/10.2307%2F1990996), [JSTOR](JSTOR%20(identifier).md#content) [1990996](https://www.jstor.org/stable/1990996), [MR](MR%20(identifier).md) [0944576](https://mathscinet.ams.org/mathscinet-getitem?mr=0944576), archived from [the original](http://www.math.ucdavis.edu/~deloera/MISC/BIBLIOTECA/trunk/Kollar/kollarnullstellen.pdf) \(PDF\) on 2014-03-03, retrieved 2012-10-14 <a id="^ref-13"></a>^ref-13
14. <a id="CITEREFSombra1999"></a> Sombra, Martín \(1999\), "A Sparse Effective Nullstellensatz", _[Advances in Applied Mathematics](Advances%20in%20Applied%20Mathematics.md)_, __22__ \(2\): 271–295, [arXiv](ArXiv%20(identifier).md):[alg-geom/9710003](https://arxiv.org/abs/alg-geom/9710003), [doi](doi%20(identifier).md):[10.1006/aama.1998.0633](https://doi.org/10.1006%2Faama.1998.0633), [MR](MR%20(identifier).md) [1659402](https://mathscinet.ams.org/mathscinet-getitem?mr=1659402), [S2CID](S2CID%20(identifier).md#S2CID) [119726673](https://api.semanticscholar.org/CorpusID:119726673) <a id="^ref-14"></a>^ref-14
15. This formulation comes from Milne, Algebraic geometry  and differs from [Hartshorne 1977](#CITEREFHartshorne1977), Ch. I, Exercise 2.4 <a id="^ref-15"></a>^ref-15
16. [Huybrechts](#CITEREFHuybrechts), Proposition 1.1.29. <a id="^ref-16"></a>^ref-16
17. <a id="CITEREFGathmann2022"></a> Gathmann, Andreas \(2022\). [_Algebraic Geometry \(course notes\)_](https://dn710302.ca.archive.org/0/items/gathmann-notes-2002-version/Gathmann%20notes%20%282022%2C%20updated%20April%202026%29.pdf) \(PDF\). TU Kaiserslautern. <a id="^ref-17"></a>^ref-17

## references

- <a id="CITEREFAlmira2007"></a> Almira, Jose María \(2007\). ["Nullstellensatz revisited"](http://www.seminariomatematico.polito.it/rendiconti/65-3/365.pdf) \(PDF\). _[Rend. Semin. Mat. Univ. Politec. Torino](Rend.%20Semin.%20Mat.%20Univ.%20Politec.%20Torino.md)_. __65__ \(3\): 365–369.
- <a id="CITEREFAtiyah–Macdonald"></a> [Atiyah, M.F.](Michael%20Atiyah.md); [Macdonald, I.G.](Ian%20G.%20Macdonald.md) \(1994\). [_Introduction to Commutative Algebra_](Introduction%20to%20Commutative%20Algebra.md). Addison-Wesley. [ISBN](ISBN%20(identifier).md) [0-201-40751-5](https://en.wikipedia.org/wiki/Special:BookSources/0-201-40751-5).
- <a id="CITEREFEisenbud1999"></a> [Eisenbud, David](David%20Eisenbud.md) \(1999\). _Commutative Algebra With a View Toward Algebraic Geometry_. Graduate Texts in Mathematics. Vol. 150. New York: Springer-Verlag. [ISBN](ISBN%20(identifier).md) [978-0-387-94268-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-94268-1).
- <a id="CITEREFHartshorne1977"></a> [Hartshorne, Robin](Robin%20Hartshorne.md) \(1977\), _[Algebraic Geometry](Algebraic%20Geometry%20(book).md)_, [Graduate Texts in Mathematics](Graduate%20Texts%20in%20Mathematics.md), vol. 52, New York: Springer-Verlag, [ISBN](ISBN%20(identifier).md) [978-0-387-90244-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-90244-9), [MR](MR%20(identifier).md) [0463157](https://mathscinet.ams.org/mathscinet-getitem?mr=0463157)
- <a id="CITEREFHilbert1893"></a> [Hilbert, David](David%20Hilbert.md) \(1893\). ["Ueber die vollen Invariantensysteme"](https://resolver.sub.uni-goettingen.de/purl?PPN235181684_0042). _[Mathematische Annalen](Mathematische%20Annalen.md)_. __42__ \(3\): 313–373. [doi](doi%20(identifier).md):[10.1007/BF01444162](https://doi.org/10.1007%2FBF01444162).
- <a id="CITEREFHuybrechts"></a> [Huybrechts, Daniel](Daniel%20Huybrechts.md) \(2005\). _Complex Geometry: An Introduction_. Springer. [ISBN](ISBN%20(identifier).md) [3-540-21290-6](https://en.wikipedia.org/wiki/Special:BookSources/3-540-21290-6).
- <a id="CITEREFMukai2003"></a> [Mukai, Shigeru](Shigeru%20Mukai.md) \(2003\). _An Introduction to Invariants and Moduli_. Cambridge studies in advanced mathematics. Vol. 81. William Oxbury \(trans.\). p. 82. [ISBN](ISBN%20(identifier).md) [0-521-80906-1](https://en.wikipedia.org/wiki/Special:BookSources/0-521-80906-1).
- <a id="CITEREFZariski–Samuel"></a> [Zariski, Oscar](Oscar%20Zariski.md); [Samuel, Pierre](Pierre%20Samuel.md) \(1960\). _Commutative algebra. Volume II_. Berlin. [ISBN](ISBN%20(identifier).md) [978-3-662-27753-9](https://en.wikipedia.org/wiki/Special:BookSources/978-3-662-27753-9).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Polynomials](https://en.wikipedia.org/wiki/Category:Polynomials)
> - [Theorems in algebraic geometry](https://en.wikipedia.org/wiki/Category:Theorems%20in%20algebraic%20geometry)
