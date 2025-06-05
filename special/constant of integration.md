---
aliases:
  - constant of integration
  - constants of integration
tags:
  - flashcard/active/special/constant_of_integration
  - language/in/English
---

# constant of integration

- see: [constant of integration](../general/constant%20of%20integration.md)

## absorption

A constant of integration can absorb {@{expressions such that the constant remains arbitrary}@}. For example, $C+1$ and $2C$ can be rewritten as $C$. It may be desirable to {@{absorb expressions aggressively as to reduce the complexity of expressions}@}. However, there are several pitfalls outlined below. <!--SR:!2029-12-31,1770,350!2028-06-12,1287,330-->

### restricted arbitrariness

Consider $\sin{C}$. It is tempting to {@{absorb $\sin{C}$ to become $C$}@}. Notice that {@{the [image](image%20(mathematics).md) of $\sin{C}$ is $[-1,1]$}@}. That means the resulting absorbed $C$ is {@{restricted to $[-1,1]$, which makes it no longer fully arbitrary}@}. To fix this, {@{either do not absorb such expressions or indicate the range of the absorbed $C$ like $C_{[-1,1]}$}@}. <!--SR:!2030-04-07,1846,350!2031-03-09,2106,350!2030-11-18,2020,350!2030-07-22,1929,350-->

### spurious invariants

Consider $\sin(x+C)$. It is tempting to {@{rewrite it as $\sin(x+C)=\sin{x}\cos{C}+\cos{x}\sin{C}=C\sin{x}+C\cos{x}$}@}. Notice that $C\sin{x}+C\cos{x}$ implies {@{the [coefficients](../general/coefficient%20(mathematics).md) of both terms are the same}@}. However, this should not be the case as {@{the two $C$-s are from $\sin{C}$ and $\cos{C}$, and $\sin{C}\ne\cos{C}$ in general}@}, so this invariant is spurious. To fix this, {@{use different symbols for the two constants like $\sin{x}\cos{C}+\cos{x}\sin{C}=C_1\sin{x}+C_2\cos{x}$}@}.  Also note that the example just now also suffers from {@{[restricted arbitrariness](#restricted%20arbitrariness)}@}. <!--SR:!2028-04-02,1233,330!2030-10-25,1996,350!2030-05-30,1888,350!2030-08-12,1946,350!2025-06-06,380,366-->
