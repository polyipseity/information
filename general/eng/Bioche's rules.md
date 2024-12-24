---
aliases:
  - Bioche rule
  - Bioche rules
  - Bioche's rule
  - Bioche's rules
tags:
   - flashcard/active/general/Bioche_s_rules
   - language/in/English
---

# Bioche's rules

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## the rules

In the following, $f(t)$ is {@{a [rational expression](rational%20function.md) in $\sin t$ and $\cos t$}@}. To calculate $\int \! f(t) \,\mathrm{d}t$, consider $\omega(t)$, defined as {@{the integrand $\omega(t) = f(t) \,\mathrm{d}t$}@}.

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("0362", "ca84"),
  R"""
$\omega(t) = \omega(-t)$ _only_: Symmetry across $x = 0$, substitute $u = \cos t$.
$\omega(t) = \omega(\pi - t)$ _only_: Symmetry across $x = \frac \pi 2$, substitute $u = \sin t$.
$\omega(t) = \omega(\pi + t)$ _only_: $\pi$-periodic, substitute $u = \tan t$.
two preceding relations hold: Substitute $u = \cos 2t$.
otherwise: Substitute $u = \tan \frac t 2$.
""".strip().splitlines(),
)
```

<!--pytextgen generate section="0362"--><!-- The following content is generated at 2024-07-02T17:25:31.792720+08:00. Any edits will be overridden! -->

> 1. $\omega(t) = \omega(-t)$ _only_: Symmetry across $x = 0$, substitute $u = \cos t$.
> 2. $\omega(t) = \omega(\pi - t)$ _only_: Symmetry across $x = \frac \pi 2$, substitute $u = \sin t$.
> 3. $\omega(t) = \omega(\pi + t)$ _only_: $\pi$-periodic, substitute $u = \tan t$.
> 4. two preceding relations hold: Substitute $u = \cos 2t$.
> 5. otherwise: Substitute $u = \tan \frac t 2$.

<!--/pytextgen-->

<!--pytextgen generate section="ca84"--><!-- The following content is generated at 2024-07-02T17:25:31.891084+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←$\omega(t) = \omega(-t)$ _only_: Symmetry across $x = 0$, substitute $u = \cos t$.
- $\omega(t) = \omega(-t)$ _only_: Symmetry across $x = 0$, substitute $u = \cos t$.→::@::←$\omega(t) = \omega(\pi - t)$ _only_: Symmetry across $x = \frac \pi 2$, substitute $u = \sin t$.
- $\omega(t) = \omega(\pi - t)$ _only_: Symmetry across $x = \frac \pi 2$, substitute $u = \sin t$.→::@::←$\omega(t) = \omega(\pi + t)$ _only_: $\pi$-periodic, substitute $u = \tan t$.
- $\omega(t) = \omega(\pi + t)$ _only_: $\pi$-periodic, substitute $u = \tan t$.→::@::←two preceding relations hold: Substitute $u = \cos 2t$.
- two preceding relations hold: Substitute $u = \cos 2t$.→::@::←otherwise: Substitute $u = \tan \frac t 2$.
- otherwise: Substitute $u = \tan \frac t 2$.→::@::←_(end)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Bioche's_rules) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
