---
aliases:
  - list of mathematical pathologies
  - list of mathematical pathology
tags:
  - flashcard/active/special/list_of_mathematical_pathologies
  - language/in/English
---

# list of mathematical pathologies

## functions

### Cantor set: indicator function

- see: [Cantor set](../general/Cantor%20set.md)

<!-- list separator -->

- integrability
  - [Riemann integrability](../general/Riemann%20integral.md) ::@:: The function is Riemann integrable on $[0, 1]$. Pathologically, its set of points of discontinuity is the Cantor set, which is uncountably infinite but has [Lebesgue measure](../general/Lebesgue%20measure.md) zero.

### Dirichlet function

- see: [Dirichlet function](../general/Dirichlet%20function.md)

The [Dirichlet function](Dirichlet%20function.md) is {@{$$f(x \in \mathbb{R}) = \begin{cases} 1 & x\text{ rational} \\ 0 & x\text{ irrational} \end{cases}$$}@}.

- [continuity](../general/continuous%20function.md) and discontinuity ::@:: It is discontinuous at every [real](../general/real%20number.md).
  - global continuity or discontinuity ::@:: It is a [discontinuous function](../general/continuous%20function.md).
- integrability
  - [Riemann integrability](../general/Riemann%20integral.md) ::@:: The function is not Riemann integrable on any non-trivial [interval](../general/interval%20(mathematics).md). This is despite it being a [bounded function](../general/bounded%20function.md).
- [limit of a function](../general/limit%20of%20a%20function.md) ::@:: It has no limit at every [real](../general/real%20number.md).

### Volterra's function

- see: [Volterra's function](Volterra's%20function.md)

Volterra's function is constructed {@{using increasingly smaller modified copies of $f(x) = x^2 \sin(1 / x)$, mirrored and then placed on the removed intervals of [Smith–Volterra–Cantor set](Smith–Volterra–Cantor%20set.md)}@}.

- derivative
  - derivative integrability
    - derivative [Riemann integrability](../general/Riemann%20integral.md) ::@:: The derivative is not Riemann integrable on $[0, 1]$. Pathologically, the derivative exists everywhere and is [bounded](bounded%20function.md).

### empty function

- see: [function (mathematics)](../general/function%20(mathematics).md)

{@{Every [set](../general/set%20(mathematics).md) $X$ has the unique [function](../general/function%20(mathematics).md) $\varnothing \to X$}@} called the __empty function__.

- [continuity](../general/continuous%20function.md) and discontinuity ::@:: It is continuous and not discontinuous at every point of its [domain](../general/domain%20of%20a%20function.md) by [vacuous truth](../general/vacuous%20truth.md). It is neither continuous nor discontinuous at every [real](../general/real%20number.md).
  - global continuity or discontinuity ::@:: It is a [continuous function](../general/continuous%20function.md).
- [limit of a function](../general/limit%20of%20a%20function.md) ::@:: It has limit and it has no limit at every point of its [domain](../general/domain%20of%20a%20function.md) by [vacuous truth](../general/vacuous%20truth.md).

## topologies

### topologist's sine curve

- see: [topologist's sine curve](../general/topologist's%20sine%20curve.md)

#### functions related to the topologist's sine curve

##### $x^2 \sin(1 / x^2)$

The function is {@{$$f(x) = \begin{cases} x^2 \sin \frac 1 {x^2}, & x \ne 0 \\ 0, & x = 0 \end{cases}$$}@}.

- derivative ::@:: $$f'(x) = \begin{cases} 2x \sin \frac 1 {x^2} - \frac {2 \cos \frac 1 {x^2} } x, & x \ne 0 \\ 0, & x = 0 \end{cases}$$
  - derivative integrability
    - derivative [Riemann integrability](../general/Riemann%20integral.md) ::@:: The derivative is not Riemann integrable on any non-trivial interval containing 0, as it is [unbounded](../general/bounded%20function.md). The derivative is an example of an non-integrable function that has an [antiderivative](../general/antiderivative.md) everywhere.
