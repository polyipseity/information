---
aliases:
  - Bioche rule
  - Bioche rules
  - Bioche's rule
  - Bioche's rules
tags:
   - flashcard/active/general/eng/Bioche_s_rules
   - language/in/English
---

# Bioche's rules

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

<!-- | ![](../../archives/Wikimedia%20Commons/Text%20document%20with%20red%20question%20mark.svg) | This article includes a [list of references](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources), [related reading](https://en.wikipedia.org/wiki/Wikipedia:Further%20reading), or [external links](https://en.wikipedia.org/wiki/Wikipedia:External%20links), __but its sources remain unclear because it lacks [inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing%20sources#Inline_citations)__. Please help [improve](https://en.wikipedia.org/wiki/Wikipedia:WikiProject%20Reliability) this article by [introducing](https://en.wikipedia.org/wiki/Wikipedia:When%20to%20cite) more precise citations. _\(June 2022\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

{@{__Bioche's rules__}@}, formulated by {@{the French mathematician [Charles Bioche](Charles%20Bioche.md)}@} \[[fr](fr_Charles%20Bioche.md)\] \(1859–1949\), are {@{rules to aid in the computation of certain [indefinite integrals](indefinite%20integral.md)}@} in which {@{the [integrand](integrand.md#terminology%20and%20notation) contains [sines](sine.md) and [cosines](cosine.md)}@}.

In the following, $f(t)$ is {@{a [rational expression](rational%20function.md) in $\sin t$ and $\cos t$}@}. In order to {@{calculate $\int f(t)\,dt$}@}, consider {@{the integrand $\omega (t)=f(t)\,dt$}@}. We consider {@{the behavior of this entire integrand, including the $dt$}@}, under {@{translation and reflections of the _t_ axis}@}. {@{The translations and reflections}@} are ones that {@{correspond to the symmetries and periodicities of the basic trigonometric functions}@}.

Bioche's rules state that:

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("0362", "ca84"),
  R"""
If $\omega (-t)=\omega (t)$ \(annotation: even symmetry around $x = 0$\), a good change of variables is $u=\cos t$.
If $\omega (\pi -t)=\omega (t)$ \(annotation: even symmetry around $x = \frac \pi 2$\), a good change of variables is $u=\sin t$.
If $\omega (\pi +t)=\omega (t)$ \(annotation: $\pi$-periodic\), a good change of variables is $u=\tan t$.
If two of the preceding relations both hold, a good change of variables is $u=\cos 2t$.
In all other cases, use $u=\tan(t/2)$ \(annotation: tangent half-angle substitution\).
""".strip().splitlines(),
)
```

<!--pytextgen generate section="0362"--><!-- The following content is generated at 2025-07-05T20:07:58.018509+08:00. Any edits will be overridden! -->

> 1. If $\omega (-t)=\omega (t)$ \(annotation: even symmetry around $x = 0$\), a good change of variables is $u=\cos t$.
> 2. If $\omega (\pi -t)=\omega (t)$ \(annotation: even symmetry around $x = \frac \pi 2$\), a good change of variables is $u=\sin t$.
> 3. If $\omega (\pi +t)=\omega (t)$ \(annotation: $\pi$-periodic\), a good change of variables is $u=\tan t$.
> 4. If two of the preceding relations both hold, a good change of variables is $u=\cos 2t$.
> 5. In all other cases, use $u=\tan(t/2)$ \(annotation: tangent half-angle substitution\).

<!--/pytextgen-->

<!--pytextgen generate section="ca84"--><!-- The following content is generated at 2025-07-05T20:07:58.075023+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←If $\omega (-t)=\omega (t)$ \(annotation: even symmetry around $x = 0$\), a good change of variables is $u=\cos t$.
- If $\omega (-t)=\omega (t)$ \(annotation: even symmetry around $x = 0$\), a good change of variables is $u=\cos t$.→::@::←If $\omega (\pi -t)=\omega (t)$ \(annotation: even symmetry around $x = \frac \pi 2$\), a good change of variables is $u=\sin t$.
- If $\omega (\pi -t)=\omega (t)$ \(annotation: even symmetry around $x = \frac \pi 2$\), a good change of variables is $u=\sin t$.→::@::←If $\omega (\pi +t)=\omega (t)$ \(annotation: $\pi$-periodic\), a good change of variables is $u=\tan t$.
- If $\omega (\pi +t)=\omega (t)$ \(annotation: $\pi$-periodic\), a good change of variables is $u=\tan t$.→::@::←If two of the preceding relations both hold, a good change of variables is $u=\cos 2t$.
- If two of the preceding relations both hold, a good change of variables is $u=\cos 2t$.→::@::←In all other cases, use $u=\tan(t/2)$ \(annotation: tangent half-angle substitution\).
- In all other cases, use $u=\tan(t/2)$ \(annotation: tangent half-angle substitution\).→::@::←_(end)_

<!--/pytextgen-->

Because {@{rules 1 and 2 involve flipping the _t_ axis}@}, they {@{flip the sign of _dt_}@}, and therefore {@{the behavior of _ω_ under these transformations differs from that of _ƒ_ by a sign}@}. Although {@{the rules could be stated in terms of _ƒ_}@}, stating them {@{in terms of _ω_ has a mnemonic advantage}@}, which is that we {@{choose the change of variables _u_\(_t_\) that has the same symmetry as _ω_}@}.

These rules can be, in fact, stated as {@{a [theorem](theorem.md)}@}: one shows<sup>[\[1\]](#^ref-1)</sup> that {@{the proposed change of variable reduces}@} \(if {@{the rule applies and if _f_ is actually of the form $f(t)={\frac {P(\sin t,\cos t)}{Q(\sin t,\cos t)} }$}@}\) to {@{the integration of a [rational function](rational%20function.md) in a new variable}@}, which can be calculated by {@{[partial fraction decomposition](partial%20fraction%20decomposition.md)}@}.

## case of polynomials

To {@{calculate the integral $\int \sin ^{p}(t)\cos ^{q}(t)dt$}@}, {@{Bioche's rules apply}@} as well.

- If _p_ \(annotation: $\sin$\) and _q_ \(annotation: $\cos$\) are odd, ::@:: one uses $u=\cos(2t)$;
- If _p_ \(annotation: $\sin$\) is odd and _q_ \(annotation: $\cos$\) even, ::@:: one uses $u=\cos(t)$;
- If _p_ \(annotation: $\sin$\) is even and _q_ \(annotation: $\cos$\) odd, ::@:: one uses $u=\sin(t)$;
- If not, ::@:: one is reduced to [linearization](linearization.md). \(annotation: Apply product-to-sum formulas.\)

## another version for hyperbolic functions

Suppose one is {@{calculating $\int g(\cosh t,\sinh t)dt$}@}.

If {@{Bioche's rules suggest calculating $\int g(\cos t,\sin t)dt$}@} by {@{$u=\cos(t)$ \(respectively, $\sin t,\tan t,\cos(2t),\tan(t/2)$\)}@}, in the case of {@{hyperbolic sine and cosine}@}, a good change of variable is {@{$u=\cosh(t)$ \(respectively, $\sinh(t),\tanh(t),\cosh(2t),\tanh(t/2)$\)}@}. \(annotation: In short, {@{drop the "h"s, apply the rules, and then add back the "h"s}@}.\) In {@{every case}@}, {@{the change of variable $u=e^{t}$}@} allows {@{one to reduce to a rational function}@}, this last change of variable being {@{most interesting in the fourth case \($u=\tanh(t/2)$\)}@}.

## examples

### example 1

As {@{a trivial example}@}, consider {@{$$\int \sin t\,dt.$$}@} Then {@{$f(t)=\sin t$ is an odd function}@}, but under {@{a reflection of the _t_ axis about the origin}@}, ω {@{stays the same}@}. That is, ω {@{acts like an even function}@}. This is the same as {@{the symmetry of the cosine, which is an even function}@}, so the mnemonic tells us to {@{use the substitution $u=\cos t$ \(rule 1\)}@}. Under {@{this substitution}@}, the integral becomes {@{$-\int du$}@}. {@{The integrand involving transcendental functions}@} has been {@{reduced to one involving a rational function \(a constant\)}@}. The result is {@{$-u+c=-\cos t+c$}@}, which is of course {@{elementary and could have been done without Bioche's rules}@}.

### example 2

The integrand in {@{$$\int {\frac {dt}{\sin t} }$$}@} has {@{the same symmetries as the one in example 1}@}, so we use {@{the same substitution $u=\cos t$}@}. So {@{$${\frac {dt}{\sin t} }=-{\frac {du}{\sin ^{2}t} }=-{\frac {du}{\ 1-\cos ^{2}t} }.$$}@} This transforms the integral into {@{$$\int -{\frac {du}{1-u^{2} } },$$}@} which can be {@{integrated using partial fractions}@}, since {@{${\frac {1}{1-u^{2} } }={\frac {1}{2} }\left({\frac {1}{1+u} }+{\frac {1}{1-u} }\right)$}@}. The result is that {@{$$\int {\frac {dt}{\sin t} }=-{\frac {1}{2} }\ln {\frac {1+\cos t}{1-\cos t} }+c.$$}@}

### example 3

Consider {@{$$\int {\frac {dt}{1+\beta \cos t} },$$}@} where {@{$\beta ^{2}<1$}@}. Although {@{the function _f_ is even}@}, {@{the integrand as a whole ω is odd}@}, so {@{it does not fall under rule 1}@}. It also {@{lacks the symmetries described in rules 2 and 3}@}, so we fall back to {@{the last-resort substitution $u=\tan(t/2)$}@}.

Using {@{$\cos t={\frac {1-\tan ^{2}(t/2)}{1+\tan ^{2}(t/2)} }$}@} and {@{a second substitution $v={\sqrt {\frac {1-\beta }{1+\beta } } }u$}@} leads to the result {@{$$\begin{aligned} \int {\frac {\mathrm {d} t}{1+\beta \cos t} } & = \int \frac 1 {1 + \beta \frac {1 - u^2} {1 + u^2} } \frac {2 \, \mathrm du} {1 + u^2} \\ & = \int \frac {2 \,\mathrm du} {(1 + \beta) + (1 - \beta) u^2} \\ & = \frac 2 {1 + \beta} \int \frac {\mathrm du} {1 + \left(\sqrt{\frac {1 - \beta} {1 + \beta} } u\right)^2} \\ & = \frac 2 {1 + \beta } \sqrt{\frac {1 + \beta} {1 - \beta} } \int \frac {\mathrm dv} {1 + v^2} \\ & ={\frac {2}{\sqrt {1-\beta ^{2} } } }\arctan \left[{\sqrt {\frac {1-\beta }{1+\beta } } }\tan {\frac {t}{2} }\right]+c \,. \end{aligned}$$}@}

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Bioche's_rules) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

> ![Wikiversity logo](../../archives/Wikimedia%20Commons/Wikiversity%20logo%202017.svg) Wikiversity has learning resources about ___[Bioche's rules](https://en.wikiversity.org/wiki/Bioche%27s%20rules)___

1. <a id="CITEREFVidiani1976"></a> Vidiani, L.G. \(October 1976\). ["Règles de Bioche"](https://web.archive.org/web/20220718014842/http://www.georges-vidiani.com/wp-content/uploads/2016/09/Bioche-MP-Octobre-19760001.pdf) \[Bioche's rules\] \(PDF\). _Revue de mathématiques et de sciences physiques_ \(in French\): 1–2. Archived from the original on 18 July 2022. Retrieved 10 June 2022. <a id="^ref-1"></a>^ref-1

- Zwillinger, _Handbook of Integration_, p. 108
- Stewart, _How to Integrate It: A practical guide to finding elementary integrals_, pp. 190−197.

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Integral calculus](https://en.wikipedia.org/wiki/Category:Integral%20calculus)
> - [Theorems in calculus](https://en.wikipedia.org/wiki/Category:Theorems%20in%20calculus)
