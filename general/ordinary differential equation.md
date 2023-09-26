---
aliases:
  - ODE
  - ordinary differential equation
tags:
  - flashcards/general/ordinary_differential_equation
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# ordinary differential equation

## definitions

An [explicit](implicit%20function.md) ordinary differential equation of order _n_ has the form:

> {{__explicit ordinary differential equation of order _n___}}
>
> {{$F\left(x,y'(x),\ldots,y^{(n-1)}(x)\right)=y^{(n)}(x)$}}
>
> given
> - $x$, an [independent variable](dependent%20and%20independent%29variables.md)
> - $y(x)$, a [function](function%20(mathematics).md) of $x$
> - $y^{(d)}(x)$, [derivatives](derivative%20.md) of $y(x)$
> - $F$, a [formula](formula.md)

An [implicit](implicit%20function.md) ordinary differential equation of order _n_ has the form:

> {{__implicit ordinary differential equation of order _n___}}
>
> {{$F\left(x,y'(x),\ldots,y^{(n-1)}(x), y^{(n)}(x)\right)=0$}}
>
> given
> - $x$, an [independent variable](dependent%20and%20independent%29variables.md)
> - $y(x)$, a [function](function%20(mathematics).md) of $x$
> - $y^{(d)}(x)$, [derivatives](derivative%20.md) of $y(x)$
> - $F$, a [formula](formula.md)

### classifications

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_seq(
  e.cwf_sects('0d9f', 'ff12'),
  (
		'[autonomous](#^autonomous)',
		'[homogeneous](#^homogeneous)',
		'[linear](#^linear)',
		'[nonhomogeneous](#^nonhomogeneous)/inhomogeneous',
		'[nonlinear](#^nonlinear)',
  ),
)
```
%%

Ordinary differential equations are furthered classified:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="0d9f"--><!-- The following content is generated at 2023-09-26T08:47:40.039221+08:00. Any edits will be overridden! -->

> 1. [autonomous](#^autonomous)
> 2. [homogeneous](#^homogeneous)
> 3. [linear](#^linear)
> 4. [nonhomogeneous](#^nonhomogeneous)/inhomogeneous
> 5. [nonlinear](#^nonlinear)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="ff12"--><!-- The following content is generated at 2023-09-26T08:47:40.062051+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←[autonomous](#^autonomous)
2. [autonomous](#^autonomous)→:::←[homogeneous](#^homogeneous)
3. [homogeneous](#^homogeneous)→:::←[linear](#^linear)
4. [linear](#^linear)→:::←[nonhomogeneous](#^nonhomogeneous)/inhomogeneous
5. [nonhomogeneous](#^nonhomogeneous)/inhomogeneous→:::←[nonlinear](#^nonlinear)
6. [nonlinear](#^nonlinear)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

> [__autonomous__](autonomous%20system%20(mathematics).md) <a id="^autonomous"></a>^autonomous
>
> {{An ODE where $F$ does not depend on $x$ explicitly.}}

> [__homogeneous__](homogeneous%20differential%20equation.md) <a id="^homogeneous"></a>^homogeneous
>
> {{An [linear](#^linear) ODE where there are no constant terms ($r(x)=0$).}}

> [__linear__](linear%20differential%20equation.md) <a id="^linear"></a>^linear
>
> {{An ODE where $F$ can be written as a [linear combination](linear%20combination.md) of the derivatives of $y$ and the [coefficients](coefficient.md) are [continuous functions](continuous%20function.md) of $x$. The constant term $r(x)$ is also called the _source term_.}}

> [__nonhomogeneous__](homogeneous%20differential%20equation.md) <a id="^nonhomogeneous"></a>^nonhomogeneous
>
> {{An [linear](#^linear) ODE that is not [homogeneous](#^homogeneous).}}

> [__nonlinear__](nonlinear%20system.md#nonlinear%20differential%20equations) <a id="^nonlinear"></a>^nonlinear
>
> {{An ODE that is not [linear](#^linear).}}
