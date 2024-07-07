---
aliases:
  - eigenvalue
  - eigenvalue and eigenvector
  - eigenvalues
  - eigenvalues and eigenvectors
  - eigenvector
  - eigenvector and eigenvalue
  - eigenvectors
  - eigenvectors and eigenvalues
tags:
  - flashcard/general/eigenvalues_and_eigenvectors
  - language/in/English
---

# eigenvalues and eigenvectors

In [linear algebra](linear%20algebra.md), it is often important to {{know which [vectors](vector%20space.md) have their directions unchanged by a given [linear transformation](linear%20map.md)}}. An {{__eigenvector__ (/ˈaɪɡən-/ EYE-gən-) or __characteristic vector__}} is such a vector. More precisely, an eigenvector $\mathbf v$ of a linear transformation $T$ is {{a nonzero vector that is [scaled by a constant factor](scalar%20multiplication.md) $\lambda$ when the linear transformation is applied to it: $T \mathbf v = \lambda \mathbf v \quad \mathbf v \ne \mathbf 0$}}. The multiplying factor $\lambda$ is {{the corresponding __eigenvalue__, __characteristic value__, or __characteristic root__}}.

## definition

Consider {{a [linear transformation](linear%20map.md) $T$ and a nonzero [vector](vector%20space.md) $\mathbf v$}}. If {{applying $T$ simply scales $\mathbf v$ by a factor of $\lambda$, where $\lambda$ is a [scalar](scalar%20(mathematics).md)}}, then {{$\mathbf v$ is an eigenvector of $T$, and $\lambda$ is the corresponding eigenvalue}}. This relationship can be expressed as: {{$$T \mathbf v = \lambda \mathbf v$$}}.

For {{finite-[dimensional](dimension%20(vector%20space).md) [vector spaces](vector%20space.md)}}, there is {{a direct correspondence between _n_-by-_n_ [square matrices](square%20matrix.md) and linear transformations from an [_n_-dimensional](dimension.md) vector space into itself}}, given {{any [basis](basis%20(linear%20algebra).md) of the vector space}}. Hence, it is {{equivalent to define eigenvalues and eigenvectors using either the language of [matrices](matrix%20(mathematics).md), or the language of linear transformations}}. In this case, the above equation can be rewritten as: {{$$A \mathbf u = \lambda \mathbf u$$, where $A$ is the matrix representation of $T$ and $\mathbf u$ is the [coordinate vector](coordinate%20vector.md) of $\mathbf v$}}.

## overview

Eigenvalues and eigenvectors give rise to {{many closely related mathematical concepts}}, and {{the prefix _eigen-_ is applied liberally when naming them}}:

- __eigensystem__ of a linear transformation ::: the set of all eigenvectors of the linear transformation, each paired with its corresponding eigenvalue
- __eigenspace__ or __characteristic space__ of a eigenvalue of a linear transformation ::: the set of all eigenvectors of the linear transformation corresponding to the same eigenvalue, together with the zero vector
- __eigenbasis__ :::  the set of eigenvectors of a linear transformation that also forms a [basis](basis%20(linear%20algebra.md)) of the domain of the same linear transformation

## eigenvalues and eigenvectors of matrices

Eigenvalues and eigenvectors are often introduced to students in {{the context of [linear algebra](linear%20algebra.md) courses focused on [matrices](matrix%20(mathematics).md)}}. Furthermore, linear transformations over {{a finite-[dimensional](dimnsion%20(vector%20space).md) [vector space](vector%20space.md)}} can be represented {{using matrices, which is especially common in numerical and computational applications}}.

Consider _n_-dimensional vectors formed of {{a vertical list of _n_ scalars}}, such as the 2-dimensional vectors $$\mathbf x = \begin{bmatrix} 10 \\ -20 \end{bmatrix} \quad \text{ and } \quad \mathbf y = \begin{bmatrix} -1 \\ 2 \end{bmatrix}$$. These vectors are {{[scalar multiples](scalar%20multiplication.md) of each other, also called [parallel](parallel%20(geometry).md) or [collinear](collinearity.md)}}, because {{there is a [scalar](scalar%20(mathematics).md) $\lambda$ such that $$\mathbf x = \lambda \mathbf y$$}}. In this case, {{$\lambda = -10$}}.

Now consider the linear transformation of _n_-dimensional vectors defined by {{an _n_-by-_n_ matrix $A$}}, such as {{the scaling-by-negative-10 matrix}}: {{$$A = \begin{bmatrix} -10 & 0 \\ 0 & -10 \end{bmatrix}$$}}. Applying the linear transformation on a nonzero vector $\mathbf v$ to make a new vector $\mathbf w$ is represented by {{$$A \mathbf v = \mathbf w$$ or $$\begin{bmatrix} A_{11} & A_{12} & \cdots & A_{1n} \\ A_{21} & A_{22} & \cdots & A_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ A_{n1} & A_{n2} & \cdots & A_{nn} \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} = \begin{bmatrix} w_1 \\ w_2 \\ \vdots \\ w_n \end{bmatrix}$$}}, where for each row of $\mathbf w$: {{$$w_i = A_{i1} v_1 + A_{i2} v_2 + \cdots + A_{in} v_n = \sum_{k = 1}^n A_{ik} v_k$$}}. This operation is known as {{[matrix multiplication](matrix%20(mathematics).md#matrix%20multiplication)}}. For example, applying $A$ on $\mathbf y = \begin{bmatrix} -1 \\ 2 \end{bmatrix}$ is: {{$$\begin{aligned} A \mathbf y & = \mathbf w \\ \begin{bmatrix} -10 & 0 \\ 0 & -10 \end{bmatrix} \begin{bmatrix} -1 \\ 2 \end{bmatrix} & = \begin{bmatrix} 10 \\ -20 \end{bmatrix} \end{aligned}$$}}, so the result is {{$\mathbf w = \begin{bmatrix} 10 \\ - 20 \end{bmatrix} = \mathbf x$}}.

If it happens that the original {{nonzero}} $\mathbf v$ and the resulting $\mathbf w$ are {{scalar multiples}}, that is: {{$$A \mathbf{v} = \mathbf{w} = \lambda \mathbf{v} \quad \mathbf{v} \ne \mathbf{0}$$}}, then {{$\mathbf v$ is the __eigenvector__ of the linear transformation $A$ and the scale factor $\lambda$ is the __eigenvalue__ corresponding to that eigenvector}}. The above equation is {{the __eigenvalue equation__ for the linear transformation $A$}}. For the example above after applying $A$ on $\mathbf y$ to get $\mathbf x = -10 \mathbf y$, {{$\mathbf y$ is an eigenvector of the matrix $A$ and $\lambda = -10$ is the corresponding eigenvalue}}.

The eigenvalue equation can also be equivalently stated as {{$$(A - \lambda I) \mathbf v = \mathbf 0 \quad \text{ or } \quad (\lambda I - A) \mathbf v = \mathbf 0$$}}, where {{$I$ is the _n_-by-_n_ [identity matrix](identity%20matrix.md) and $\mathbf 0$ is the zero vector}}.

From the eigenvector equation, given a eigenvector with its corresponding eigenvalue, a new eigenvector {{associated with the same eigenvalue can be obtained by scaling the original eigenvector by an arbitrary nonzero scalar}}. The resulting eigenvector still respects the eigenvector equation as {{this is equivalent to multiplying both sides by the nonzero scalar}}.

### eigenvalues and the characteristic polynomial

- see: [characteristic polynomial](charateristic%20polynomial.md)

The rewritten eigenvalue equation with $\lambda I$ in front: {{$$(\lambda I - A) \mathbf v = \mathbf 0$$}} has {{a nonzero vector solution $\mathbf v$ [iff](if%20and%20only%20if.md) the [determinant](determinant.md) of the matrix $(\lambda I - A)$ is zero}}. Therefore, the eigenvalues $\lambda$ are {{that satisfy the equation $\det(\lambda I - A) = 0$}}. This equation is called {{the _characteristic equation_ or the _secular equation_ of $A$}}.

Using {{the [Leibniz formula for determinants](Leibniz%20formula%20for%20determinants.md)}}, the left-hand side of equation is {{a [polynomial](polynomial.md) function of the variable $\lambda$ and the [degree](degree%20of%20a%20polynomial.md) of this polynomial is $n$, the order of the matrix $A$}}. Its coefficients depend on {{the entries of $A$, except that its term of degree of $n$ is always $\lambda^n$, making the polynomial a [monic polynomial](monic%20polynomial.md)}}. If {{the eigenvalue equation with $A$ in front is used instead}}, then {{its term of degree of $n$ is always $(-1)^n \lambda^n$, making it monic only when $n$ is even}}. This polynomial is called {{the _characteristic polynomial_ of $A$}}. {{The monic polynomial}} will be used in the rest of this article.

{{The [fundamental theorem of algebra](fundamental%20theorem%20of%20algebra.md)}} implies that the characteristic polynomial of an _n_-by-_n_ [matrix](matrix%20(mathematics).md) $A$, being {{a (monic) polynomial of [degree](degree%20of%20a%20polynomial.md) _n_}}, can {{be [factored](factorization.md) into the product of _n_ linear terms}}: {{$$\det(\lambda I - A) = (\lambda - \lambda_1) (\lambda - \lambda_2) \cdots (\lambda_n - \lambda) = \prod_{i = 1}^n (\lambda - \lambda_i)$$}}, where {{each $\lambda_i$ may be [real](real%20number.md) but in general is a [complex number](complex%20number.md)}}. The scalars $\lambda_1, \lambda_2, \ldots, \lambda_n$ are {{the roots of the polynomial and all also eigenvalues of $A$}}. The eigenvalues may or may not {{be zero, or be all distinct}}. {{Plugging the eigenvalues back into the eigenvalue equation and solving them}} gives the corresponding eigenvalues.

If {{the entries of matrix $A$ are all [real numbers](real%20number.md)}}, then {{the coefficients of the characteristic polynomial are also all real numbers, but the eigenvalues may still have nonzero imaginary parts. Thus, the entires of the corresponding eigenvectors may also have nonzero imaginary parts}}. Similarly, {{eigenvalues and entries of their corresponding eigenvectors may be [irrational numbers](irrational%20number.md)}} even if {{all entries of $A$ are [rational numbers](rational%20number.md) or even [integers](integer.md)}}. However, if {{the entries of $A$ are all [algebraic numbers](algebraic%20number.md), which include the rationals}}, {{the eigenvalues and entries of their corresponding eigenvectors must also be algebraic numbers}}.

The non-real roots of a real [polynomial](polynomial.md) with real coefficients can be {{grouped into pairs of [complex conjugates](complex%20conjugate.md), which are two [complex numbers](complex%20number.md) having the same real part and imaginary parts of opposing sign}}. The eigenvectors associated with these complex eigenvalues are {{also complex and also appear in complex conjugate pairs}}. If {{the [degree](degree%20of%20a%20polynomial.md) is odd}}, then {{by the [intermediate value theorem](intermediate%20value%20theorem.md) (an odd-degree polynomial goes to infinity as the variable goes to infinity, but with opposing sign comparing the variable going to negative infinity and positive infinity), at least one of the roots is real}}. Therefore, {{any real matrix with odd order has at least one real eigenvalue, whereas a real matrix with even order may not have any real eigenvalues}}.

### algebraic multiplicity

Let $\lambda_i$ be an eigenvalue of an _n_-by-_n_ matrix $A$. The __algebraic multiplicity__ {{$\mu_A(λ_i)$ of the eigenvalue}} is {{its [multiplicity as a root](multiplicity%20(mathematics).md#multiplicity%20of%20a%20root%20of%20a%20polynomial) of the characteristic polynomial}}, that is, {{the largest integer $k$ such that $(\lambda − \lambda_i)^k$ [divides evenly](polynomial%2long%20division.md) that polynomial}}.

Suppose in the $n$ eigenvalues of an _n_-by-_n_ matrix, there are {{$d$ distinct eigenvalues with $1 \le d \le n$}}. The characteristic polynomial factorized into $n$ linear terms above may have {{some terms potentially repeating}}. Instead, said polynomial can also be written as {{the product of $d$ distinct terms each corresponding to a distinct eigenvalue and raised to the power of algebraic multiplicity}}: {{$$\det(\lambda I - A) = (\lambda - \lambda_1)^{\mu_A(\lambda_1)} (\lambda - \lambda_2)^{\mu_A(\lambda_2)} \cdots (\lambda - \lambda_d)^{\mu_A(\lambda_d)}$$}}.

If {{$d = n$}} then {{the right hand side is a product of $n$ distinct terms and is the same as the polynomial above}}. The size of each eigenvalue's algebraic multiplicity respect the following relations: {{$$\begin{aligned} 1 & \le \mu_A(\lambda_i) \le n \\ \mu_A & = \sum_{i = 1}^d \mu_A(\lambda_i) = n \end{aligned}$$}}.

If {{$\mu_A(\lambda_i) = 1$}}, then $\lambda_i$ is {{said to be a _simple eigenvalue_}}. If {{$\mu_A(\lambda_i)$ equals the geometric multiplicity of $\lambda_i$, $\gamma_A(\lambda_i)$}}, defined in upcoming sections, then $\lambda_i$ is {{said to be a _semisimple eigenvalue_}}.

### eigenspaces

Given {{a particular eigenvalue $\lambda$ of the _n_-by-_n_ matrix $A$}}, define the set $E$ to be {{all vectors $\mathbf v$ that satisfy the eigenvalue equation}}: {{$$E = \set{ \mathbf v : (\lambda I - A) \mathbf v = \mathbf 0 }$$}}. On one hand, this is {{precisely the [kernel](kernel%20(linear%20algebra).md) or nullspace of the matrix $(\lambda I - A)$}}. On the other hand, {{by definition, any _nonzero_ vector that satisfies the eigenvalue equation is an eigenvector of $A$ associated with $\lambda$}}. So, the set $E$ is {{the [union](union%20(set%20theory).md) of the zero vector and the set of all eigenvectors of $A$ associated with $\lambda$}}, and also equals {{the nullspace of the matrix $(\lambda I - A)$}}. $E$ is called {{the __eigenspace__ or __characteristic space__ of $A$ associated with eigenvalue $\lambda$}}. In general, $\lambda$ is {{a [complex number](complex%20number.md) and the eigenvectors are complex $n$ by 1 matrices}}. An important property of the nullspace is that {{it is a [linear subspace](linear%20subspace.md), so $E$ is a linear subspace of $\mathbb{C}^n$}}.

Because the eigenspace $E$ is {{a [linear subspace](linear%20subspace.md)}}, it is {{[closed](closure%20(mathematics).md) under [addition](addition.md) and [scalar multiplication](scalar%20multiplication.md)}}. That is, if {{two arbitrary vectors $\mathbf u$ and $\mathbf v$ belong to the set $E$ and $\alpha$ is an arbitrary [scalar](scalar%20(mathematics).md)}}, written {{$\mathbf u, \mathbf v \in E, \alpha \in \mathbb{F}(E)$}}, then {{$(\alpha \mathbf u + \mathbf v) \in E$ or equivalently $A(\alpha \mathbf u + \mathbf v) = \lambda (\alpha \mathbf u + \mathbf v)$}}. This can be checked {{using the [distributive property](distributive%20property.md) of matrix multiplication (for addition) and noting that multiplication of complex matrices by complex numbers is [commutative](commutative%20property.md) (for scalar multiplication)}}. As long as {{the resulting vector $(\alpha \mathbf u + \mathbf v)$ is not the zero vector $\mathbf 0$ (the zero vector belongs to $E$, however)}}, then it is also {{an eigenvector of $A$ associated with $\lambda$}}.

### geometric multiplicity

The __geometric multiplicity__ {{$\gamma_A(\lambda)$ of an eigenvalue $\lambda$}} is {{the [dimension](dimension%20(vector%20space).md) of the eigenspace $E$ associated with $\lambda$}}, or equivalently {{the maximum number of [linearly independent](linear%20independence.md) eigenvectors associated with $\lambda$}}. Because {{$E$ is also the nullspace of $(\lambda I - A)$}}, {{the geometric multiplicity is the dimension of nullspace of $(\lambda I - A)$}}, also called {{the _nullity_ of $(\lambda I - A)$}}, which {{relates to the dimension and rank of $(\lambda I - A)$ as}}: {{$$\gamma_A(\lambda) = n - \operatorname{rank}(\lambda I - A)$$}}.

## calculation

### classical method

#### eigenvalues

The eigenvalues of a matrix $A$ can be determined by {{finding the roots of the [characteristic polynomial](characteristic%20polynomial.md) ($\det(tI - A) = 0$)}}. This is {{easy for $2 \times 2$ matrices, but the difficulty increases rapidly with the size of the matrix}}. <!--SR:!2024-08-10,39,290!2024-09-11,68,310-->

#### eigenvectors

Once {{the (exact) values of an eigenvalue is known}}, the corresponding eigenvector can be {{calculated directly by finding nonzero solutions of the eigenvalue equation}}, which becomes {{a [system of linear equations](system%20of%20linear%20equations.md) with known coefficients}}. <!--SR:!2024-08-28,56,310!2024-07-16,20,250!2024-08-11,40,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/eigenvalues_and_eigenvectors) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
