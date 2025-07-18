---
aliases:
  - Chandrasekhar-Wentzel lemma
  - Chandrasekhar-Wentzel lemmas
  - Chandrasekhar–Wentzel lemma
  - Chandrasekhar–Wentzel lemmas
tags:
  - flashcard/active/general/eng/Chandrasekhar-Wentzel_lemma
  - language/in/English
---

# Chandrasekhar–Wentzel lemma

In {@{[vector calculus](vector%20calculus.md)}@}, {@{__Chandrasekhar–Wentzel lemma__}@} was derived by {@{[Subrahmanyan Chandrasekhar](Subrahmanyan%20Chandrasekhar.md) and [Gregor Wentzel](Gregor%20Wentzel.md) in 1965}@}, while {@{studying the stability of rotating liquid drop}@}.<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup> The lemma states that _if $\mathbf {S}$ is {@{a surface bounded by a simple closed contour $C$}@}, then_ {@{$$\mathbf {L} =\oint _{C}\mathbf {x} \times (d\mathbf {x} \times \mathbf {n} )=-\int _{\mathbf {S} }(\mathbf {x} \times \mathbf {n} )\nabla \cdot \mathbf {n} \ dS.$$}@}

Here $\mathbf {x}$ is {@{the position vector}@} and $\mathbf {n}$ is {@{the unit normal on the surface}@}. An immediate consequence is that if {@{$\mathbf {S}$ is a closed surface}@}, then {@{the line integral tends to zero}@}, leading to the result, {@{$$\int _{\mathbf {S} }(\mathbf {x} \times \mathbf {n} )\nabla \cdot \mathbf {n} \ dS=0,$$}@} or, in {@{index notation}@}, we have \(annotation: Consider {@{$L_i$}@}, which is {@{the component $i$ of $\mathbf L$ in index notation}@}.\) {@{$$\int _{\mathbf {S} }x_{j}\nabla \cdot \mathbf {n} \ dS_{k}=\int _{\mathbf {S} }x_{k}\nabla \cdot \mathbf {n} \ dS_{j}.$$}@} That is to say {@{the tensor $$T_{ij}=\int _{\mathbf {S} }x_{j}\nabla \cdot \mathbf {n} \ dS_{i}$$}@} defined {@{on a closed surface}@} is {@{always symmetric, i.e., $T_{ij}=T_{ji}$}@}.

## proof

Let us write {@{the vector in index notation}@}, but {@{[summation convention](Einstein%20notation.md) will be avoided \(annotation: i.e. not Einstein notation\)}@} throughout the proof. Then {@{the left hand side}@} can be written as \(annotation: Simply {@{trace the multiplications and additions performed}@} to {@{obtain the $i$ component of $\mathbf L$}@}.\) {@{$$L_{i}=\oint _{C}[dx_{i}(n_{j}x_{j}+n_{k}x_{k})+dx_{j}(-n_{i}x_{j})+dx_{k}(-n_{i}x_{k})].$$}@} Converting {@{the line integral to surface integral using [Stokes's theorem](Stokes's%20theorem.md)}@}, we get \(annotation: See {@{exterior derivatives}@}, and identify {@{2-forms with their dual 1-form}@}, e.g. {@{$dx_i \wedge dx_j \mapsto n_k \, \mathrm dS$}@}.\) {@{$$L_{i}=\int _{\mathbf {S} }\left\{n_{i}\left[{\frac {\partial }{\partial x_{j} } }(-n_{i}x_{k})-{\frac {\partial }{\partial x_{k} } }(-n_{i}x_{j})\right]+n_{j}\left[{\frac {\partial }{\partial x_{k} } }(n_{j}x_{j}+n_{k}x_{k})-{\frac {\partial }{\partial x_{i} } }(-n_{i}x_{k})\right]+n_{k}\left[{\frac {\partial }{\partial x_{i} } }(-n_{i}x_{j})-{\frac {\partial }{\partial x_{j} } }(n_{j}x_{j}+n_{k}x_{k})\right]\right\}\ dS.$$}@} Carrying out {@{the requisite differentiation and after some rearrangement}@}, we get \(annotation: Note that $x_i, x_j, x_k$ are {@{constants if the partial derivative is not differentiating with respect to it}@}, but $n_i, n_j, n_k$ are {@{not constants}@}. Also, a trick used is {@{$n_i \frac \partial {\partial x_*} n_i = \frac 1 2 \frac \partial {\partial x_*} n_i^2$ by the \(partial\) chain rule}@}.\) {@{$$L_{i}=\int _{\mathbf {S} }\left[-{\frac {1}{2} }x_{k}{\frac {\partial }{\partial x_{j} } }(n_{i}^{2}+n_{k}^{2})+{\frac {1}{2} }x_{j}{\frac {\partial }{\partial x_{k} } }(n_{i}^{2}+n_{j}^{2})+n_{j}x_{k}\left({\frac {\partial n_{i} }{\partial x_{i} } }+{\frac {\partial n_{k} }{\partial x_{k} } }\right)-n_{k}x_{j}\left({\frac {\partial n_{i} }{\partial x_{i} } }+{\frac {\partial n_{j} }{\partial x_{j} } }\right)\right]\ dS,$$}@} or, in other words, \(annotation; Obtained by {@{adding terms to the rightmost two integrands to make them contain $\frac {\partial n_i} {\partial x_i} + \frac {\partial n_j} {\partial x_j} + \frac {\partial n_k} {\partial x_k} = \nabla \cdot \mathbf n$}@} while {@{subtracting the same terms, applying the above trick, and then merging with the leftmost two integrands to make them contain $n_i^2 + n_j^2 + n_k^2 = \lvert \mathbf n \rvert^2$}@}.\) {@{$$L_{i}=\int _{\mathbf {S} }\left[{\frac {1}{2} }\left(x_{j}{\frac {\partial }{\partial x_{k} } }-x_{k}{\frac {\partial }{\partial x_{j} } }\right)|\mathbf {n} |^{2}-(x_{j}n_{k}-x_{k}n_{j})\nabla \cdot \mathbf {n} \right]\ dS.$$}@} And since {@{$|\mathbf {n} |^{2}=1$}@}, we have {@{$$L_{i}=-\int _{\mathbf {S} }(x_{j}n_{k}-x_{k}n_{j})\nabla \cdot \mathbf {n} \ dS,$$}@} thus {@{proving the lemma \(annotation: after combining the components $\mathbf L = \langle L_i, L_j, L_k \rangle$\)}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Chandrasekhar–Wentzel_lemma) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFChandrasekhar1965"></a> Chandrasekhar, S. \(1965\). "The Stability of a Rotating Liquid Drop". _Proceedings of the Royal Society of London A: Mathematical, Physical and Engineering Sciences_. __286__ \(1404\): 1–26. [doi](doi%20(identifier).md):[10.1098/rspa.1965.0127](https://doi.org/10.1098%2Frspa.1965.0127). <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFChandrasekharWali2001"></a> Chandrasekhar, S.; Wali, K. C. \(2001\). _A Quest for Perspectives: Selected Works of S. Chandrasekhar: With Commentary_. World Scientific. <a id="^ref-2"></a>^ref-2

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Vector calculus](https://en.wikipedia.org/wiki/Category:Vector%20calculus)
