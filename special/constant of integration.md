---
aliases:
  - constant of integration
  - constants of integration
tags:
  - flashcard/special/constant_of_integration
  - language/in/English
---

# constant of integration

- see: [constant of integration](../general/constant%20of%20integration.md)

## absorption

A constant of integration can absorb {{expressions such that the constant remains arbitrary}}. For example, $C+1$ and $2C$ can be rewritten as $C$. It may be desirable to {{absorb expressions aggressively as to reduce the complexity of expressions}}. However, there are several pitfalls outlined below. <!--SR:!2025-02-25,389,330!2024-12-03,300,310-->

### restricted arbitrariness

Consider $\sin{C}$. It is tempting to {{absorb $\sin{C}$ to become $C$}}. Notice that {{the [image](image%20(mathematics).md) of $\sin{C}$ is $[-1,1]$}}. That means the resulting absorbed $C$ is {{restricted to $[-1,1]$, which makes it no longer fully arbitrary}}. To fix this, {{either do not absorb such expressions or indicate the range of the absorbed $C$ like $C_{[-1,1]}$}}. <!--SR:!2025-03-18,406,330!2025-05-26,462,330!2025-05-04,444,330!2025-04-10,424,330-->

### spurious invariants

Consider $\sin(x+C)$. It is tempting to {{rewrite it as $\sin(x+C)=\sin{x}\cos{C}+\cos{x}\sin{C}=C\sin{x}+C\cos{x}$}}. Notice that $C\sin{x}+C\cos{x}$ implies {{the [coefficients](../general/coefficient%20(mathematics).md) of both terms are the same}}. However, this should not be the case as {{the two $C$-s are from $\sin{C}$ and $\cos{C}$, and $\sin{C}\ne\cos{C}$ in general}}, so this invariant is spurious. To fix this, {{use different symbols for the two constants like $\sin{x}\cos{C}+\cos{x}\sin{C}=C_1\sin{x}+C_2\cos{x}$}}.  Also note that the example just now also suffers from {{[restricted arbitrariness](#restricted%20arbitrariness)}}. <!--SR:!2024-11-16,287,310!2025-04-28,439,330!2025-03-29,415,330!2025-04-14,428,330!2024-02-29,18,326-->
