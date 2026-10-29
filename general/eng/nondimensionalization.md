---
aliases:
  - nondimensionalization
tags:
  - flashcard/active/general/eng/nondimensionalization
  - language/in/English
---

# nondimensionalization

|                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :-----------------------------------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![icon](../../archives/Wikimedia%20Commons/Question%20book-new.svg) | This article __needs [more citations](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)__. Please help [improve this article](https://en.wikipedia.org/wiki/Special:EditPage/Nondimensionalization) by [adding citations to reliable sources](https://en.wikipedia.org/wiki/Help:Referencing%20for%20beginners). Unsourced material may be challenged and [removed](https://en.wikipedia.org/wiki/Wikipedia:Verifiability#Burden_of_evidence). <br/> _Find sources:_ ["Nondimensionalization"](https://www.google.com/search?as_eq=wikipedia&q=%22Nondimensionalization%22) – [news](https://www.google.com/search?tbm=nws&q=%22Nondimensionalization%22+-wikipedia&tbs=ar:1) __·__ [newspapers](https://www.google.com/search?&q=%22Nondimensionalization%22&tbs=bkt:s&tbm=bks) __·__ [books](https://www.google.com/search?tbs=bks:1&q=%22Nondimensionalization%22+-wikipedia) __·__ [scholar](https://scholar.google.com/scholar?q=%22Nondimensionalization%22) __·__ [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Nondimensionalization%22&acc=on&wc=on) _\(June 2025\)_<!-- markdown separator -->_\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ |

{@{__Nondimensionalization__}@} is {@{the partial or full removal of [physical dimensions](dimensional%20analysis.md) from an [equation](mathematical%20equation.md) involving [physical quantities](physical%20quantity.md) by a suitable [substitution of variables](substitution%20of%20variables.md)}@}.<sup>[\[1\]](#^ref-1)</sup> This technique can {@{simplify and [parameterize](parametric%20equation.md) problems}@} where {@{[measured](measurement.md) units are involved}@}. It is closely related to {@{[dimensional analysis](dimensional%20analysis.md)}@}. In some {@{physical [systems](system.md), the term ___scaling___}@} is used {@{interchangeably with _nondimensionalization_, in order to suggest that certain quantities are better measured relative to some appropriate unit}@}. {@{These units}@} refer to {@{quantities [intrinsic](https://en.wiktionary.org/wiki/intrinsic) to the system, rather than units such as [SI](International%20System%20of%20Units.md) units}@}. {@{Nondimensionalization}@} is not the same as converting {@{[extensive quantities](intensive%20and%20extensive%20properties.md) in an equation to intensive quantities}@}, since the latter procedure {@{results in variables that still carry units}@}.

{@{Nondimensionalization}@} can also recover {@{[characteristic properties](characteristic%20property.md) of a system}@}. For example, if a system has {@{an intrinsic [resonance frequency](resonance.md), [length](length.md), or [time constant](time%20constant.md)}@}, {@{nondimensionalization can recover these values}@}. The technique is especially useful for {@{systems that can be described by [differential equations](differential%20equation.md)}@}. One important use is in {@{the analysis of [control systems](control%20system.md)}@}. {@{One of the simplest characteristic units}@} is {@{the [doubling time](doubling%20time.md) of a system experiencing [exponential growth](exponential%20growth.md)}@}, or conversely {@{the [half-life](half-life.md) of a system experiencing [exponential decay](exponential%20decay.md)}@}.

{@{Many illustrative examples of nondimensionalization}@} originate from {@{simplifying differential equations}@}. This is because {@{a large body of physical problems can be formulated in terms of differential equations}@}. Consider the following:

- [List of dynamical systems and differential equations topics](list%20of%20dynamical%20systems%20and%20differential%20equations%20topics.md)
- [List of partial differential equation topics](list%20of%20partial%20differential%20equation%20topics.md)
- [Differential equations of mathematical physics](differential%20equations%20of%20mathematical%20physics.md)

Although {@{nondimensionalization is well adapted for these problems}@}, it is {@{not restricted to them}@}. {@{An example of a non-differential-equation application}@} is {@{dimensional analysis}@}; another example is {@{[normalization](normalization%20(statistics).md) in [statistics](statistics.md)}@}.

{@{[Measuring devices](measuring%20instrument.md)}@} are {@{practical examples of nondimensionalization occurring in everyday life}@}. Measuring devices are {@{calibrated relative to some known unit}@}. {@{Subsequent measurements}@} are {@{made relative to this standard}@}. Then, {@{the [absolute value](absolute%20value.md) of the measurement}@} is {@{recovered by scaling with respect to the standard}@}.

## rationale

Suppose {@{a [pendulum](pendulum.md)}@} is {@{swinging with a particular [period](frequency.md) _T_}@}. For such a system, it is {@{advantageous to perform calculations relating to the swinging relative to _T_}@}. In some sense, this is {@{normalizing the measurement with respect to the period}@}.

{@{Measurements made relative to an intrinsic property of a system}@} will apply to {@{other systems which also have the same intrinsic property}@}. It also allows one to compare {@{a common property of different implementations of the same system}@}. {@{Nondimensionalization}@} determines {@{in a systematic manner the __characteristic units__ of a system to use}@}, without {@{relying heavily on prior knowledge of the system's intrinsic properties}@} \(one should not confuse {@{characteristic units of a _system_ with [natural units](natural%20units.md) of _nature_}@}\). In fact, {@{nondimensionalization}@} can suggest {@{the parameters which should be used for analyzing a system}@}. However, it is necessary to start with {@{an equation that describes the system appropriately}@}.

## nondimensionalization steps

To {@{nondimensionalize a system of equations}@}, one must {@{do the following}@}: (annotation: 5 items: {@{identification of variables, substitution}@}, {@{division by the coefficient of the highest order term, definition of characteristic units, rewriting in dimensionless form}@})

1. (annotation: identification of variables) ::@:: Identify all the independent and dependent variables;
2. (annotation: substitution) ::@:: Replace each of them with a quantity scaled relative to a characteristic unit of measure to be determined;
3. (annotation: division by the coefficient of the highest order term) ::@:: Divide through by the coefficient of the highest order polynomial or derivative term;
4. (annotation: definition of characteristic units) ::@:: Choose judiciously the definition of the characteristic unit for each variable so that the coefficients of as many terms as possible become 1;
5. (annotation: rewriting in dimensionless form) ::@:: Rewrite the system of equations in terms of their new dimensionless quantities.

{@{The last three steps (annotation: division by the coefficient of the highest order term, definition of characteristic units, rewriting in dimensionless form)}@} are {@{usually specific to the problem where nondimensionalization is applied}@}. However, {@{almost all systems}@} require {@{the first two steps to be performed}@}.

### conventions

There are no {@{restrictions on the variable names used to replace "_x_" and "_t_"}@}. However, they are {@{generally chosen so that it is convenient and intuitive to use for the problem at hand}@}. For example, if "_x_" {@{represented mass}@}, {@{the letter "_m_"}@} might be {@{an appropriate symbol to represent the dimensionless mass quantity}@}.

In this article, t{@{he following conventions}@} have been used: (annotation: {@{_t_ and $\tau$}@} are {@{independent}@}, {@{_x_ and $\chi$}@} are {@{dependent}@})

- _t_ ::@:: – represents the independent variable – usually a time quantity. Its nondimensionalized counterpart is $\tau$.
- _x_ ::@:: – represents the [dependent variable](dependent%20and%20independent%20variables.md) – can be mass, voltage, or any measurable quantity. Its nondimensionalized counterpart is $\chi$.

{@{A subscript 'c' added to a quantity's variable name}@} is used to denote {@{the characteristic unit used to scale that quantity}@}. For example, if {@{_x_ is a quantity}@}, then {@{_x_<sub>c</sub>}@} is {@{the characteristic unit used to scale it}@}.

As an illustrative example, consider {@{a first order differential equation with [constant coefficients](constant%20coefficients.md#basic%20terminology)}@}: {@{$$a{\frac {dx}{dt} }+bx=Af(t).$$}@}

1. (annotation: previous step equation: {@{$$a{\frac {dx}{dt} }+bx=Af(t)$$}@}) In this equation {@{the independent variable here is _t_}@}, and {@{the dependent variable is _x_}@}.
2. (annotation: previous step equation: {@{$$a{\frac {dx}{dt} }+bx=Af(t)$$}@}) Set {@{$x=\chi x_{\text{c} },\ t=\tau t_{\text{c} }$}@}. This results in the equation {@{$$a{\frac {x_{\text{c} } }{t_{\text{c} } } }{\frac {d\chi }{d\tau } }+bx_{\text{c} }\chi =Af(\tau t_{\text{c} })\ {\stackrel {\mathrm {def} }{=} }\ AF(\tau ).$$}@}
3. (annotation: previous step equation: {@{$$a{\frac {x_{\text{c} } }{t_{\text{c} } } }{\frac {d\chi }{d\tau } }+bx_{\text{c} }\chi =Af(\tau t_{\text{c} })\ {\stackrel {\mathrm {def} }{=} }\ AF(\tau )$$}@}) {@{The coefficient of the highest ordered term}@} is {@{in front of the first derivative term}@}. {@{Dividing by this}@} gives {@{$${\frac {d\chi }{d\tau } }+{\frac {bt_{\text{c} } }{a} }\chi ={\frac {At_{\text{c} } }{ax_{\text{c} } } }F(\tau ).$$}@}
4. (annotation: previous step equation: {@{$${\frac {d\chi }{d\tau } }+{\frac {bt_{\text{c} } }{a} }\chi ={\frac {At_{\text{c} } }{ax_{\text{c} } } }F(\tau )$$}@}) {@{The coefficient in front of $\chi$}@} only {@{contains one characteristic variable _t_<sub>c</sub>}@}, hence it is {@{easiest to choose to set this to unity first}@}: (annotation: ... {@{$${\frac {bt_{\text{c} } }{a} }=1\Rightarrow t_{\text{c} }={\frac {a}{b} }.$$}@} Subsequently, {@{$${\frac {At_{\text{c} } }{ax_{\text{c} } } }={\frac {A}{bx_{\text{c} } } }=1\Rightarrow x_{\text{c} }={\frac {A}{b} }.$$}@})

|                                                                               |                               |
| ----------------------------------------------------------------------------- | ----------------------------- |
| $${\frac {bt_{\text{c} } }{a} }=1\Rightarrow t_{\text{c} }={\frac {a}{b} }.$$ | <a id="math 1"></a> __\(1\)__ |

Subsequently,

|                                                                                                                           |                               |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| $${\frac {At_{\text{c} } }{ax_{\text{c} } } }={\frac {A}{bx_{\text{c} } } }=1\Rightarrow x_{\text{c} }={\frac {A}{b} }.$$ | <a id="math 2"></a> __\(2\)__ |

1. (annotation: previous step equations: {@{$${\frac {bt_{\text{c} } }{a} }=1\Rightarrow t_{\text{c} }={\frac {a}{b} }$$ and $${\frac {At_{\text{c} } }{ax_{\text{c} } } }={\frac {A}{bx_{\text{c} } } }=1\Rightarrow x_{\text{c} }={\frac {A}{b} }$$}@}) {@{The final dimensionless equation}@} in this case becomes {@{completely independent of any parameters with units}@}: {@{$${\frac {d\chi }{d\tau } }+\chi =F(\tau ).$$}@}

### substitutions

Suppose {@{for simplicity that a certain system is characterized by two variables}@} – {@{a dependent variable _x_ and an independent variable _t_}@}, where _x_ is {@{a [function](function%20(mathematics).md) of _t_}@}. Both {@{_x_ and _t_ represent quantities with units}@}. To {@{scale these two variables}@}, assume there are {@{two intrinsic units of measurement _x_<sub>c</sub> and _t_<sub>c</sub> with the same units as _x_ and _t_ respectively}@}, such that these conditions hold: {@{$$\tau ={\frac {t}{t_{\text{c} } } }\Rightarrow t=\tau t_{\text{c} }$$ <br/> $$\chi ={\frac {x}{x_{\text{c} } } }\Rightarrow x=\chi x_{\text{c} }.$$}@} {@{These equations are used}@} to {@{replace _x_ and _t_ when nondimensionalizing}@}. If {@{differential operators are needed to describe the original system}@}, their {@{scaled counterparts become dimensionless differential operators}@}.

#### differential operators

Consider the relationship {@{$$t=\tau t_{\text{c} }\Rightarrow dt=t_{\text{c} }d\tau \Rightarrow {\frac {d\tau }{dt} }={\frac {1}{t_{\text{c} } } }.$$}@} {@{The dimensionless differential operators with respect to the independent variable}@} becomes {@{$${\frac {d}{dt} }={\frac {d\tau }{dt} }{\frac {d}{d\tau } }={\frac {1}{t_{\text{c} } } }{\frac {d}{d\tau } }\Rightarrow {\frac {d^{n} }{dt^{n} } }=\left({\frac {d}{dt} }\right)^{n}=\left({\frac {1}{t_{\text{c} } } }{\frac {d}{d\tau } }\right)^{n}={\frac {1}{ {t_{\text{c} } }^{n} } }{\frac {d^{n} }{d\tau ^{n} } }.$$}@}

#### forcing function

If {@{a system has a [forcing function](forcing%20function%20(differential%20equations).md) $f(t)$}@} then {@{$$f(t)=f(\tau t_{\text{c} })=f(t(\tau ))=F(\tau ).$$}@} Hence, {@{the new forcing function $F$}@} is made to be {@{dependent on the dimensionless quantity $\tau$}@}.

## linear differential equations with constant coefficients

### first order system

Consider {@{the differential equation for a first order system}@}: {@{$$a{\frac {dx}{dt} }+bx=Af(t).$$}@} {@{The derivation of the characteristic units}@} to __[Eq. 1](#math%201)__ and __[Eq. 2](#math%202)__ for this system gave {@{$$t_{\text{c} }={\frac {a}{b} },\ x_{\text{c} }={\frac {A}{b} }.$$}@}

### second order system

{@{A second order system}@} has the form {@{$$a{\frac {d^{2}x}{dt^{2} } }+b{\frac {dx}{dt} }+cx=Af(t).$$}@}

#### substitution step

(annotation: the equation: {@{$$a{\frac {d^{2}x}{dt^{2} } }+b{\frac {dx}{dt} }+cx=Af(t)$$}@}) Replace {@{the variables _x_ and _t_ with their scaled quantities}@}. The equation becomes {@{$$a{\frac {x_{\text{c} } }{ {t_{\text{c} } }^{2} } }{\frac {d^{2}\chi }{d\tau ^{2} } }+b{\frac {x_{\text{c} } }{t_{\text{c} } } }{\frac {d\chi }{d\tau } }+cx_{\text{c} }\chi =Af(\tau t_{\text{c} })=AF(\tau ).$$}@} This new equation is {@{not dimensionless}@}, although all {@{the variables with units are isolated in the coefficients}@}. {@{Dividing by the coefficient of the highest ordered term}@}, the equation becomes {@{$${\frac {d^{2}\chi }{d\tau ^{2} } }+t_{\text{c} }{\frac {b}{a} }{\frac {d\chi }{d\tau } }+{t_{\text{c} } }^{2}{\frac {c}{a} }\chi ={\frac {A{t_{\text{c} } }^{2} }{ax_{\text{c} } } }F(\tau ).$$}@} Now it is necessary to determine {@{the quantities of _x_<sub>c</sub> and _t_<sub>c</sub> so that the coefficients become normalized}@}. Since {@{there are two free parameters}@}, {@{at most only two coefficients can be made to equal unity}@}.

#### determination of characteristic units

Consider {@{the variable _t_<sub>c</sub>}@}: (annotation: 2 items: {@{normalizing the first order term, normalizing the zeroth order term}@})

1. If $t_{\text{c} }={\frac {a}{b} }$ ::@:: the first order term is normalized.
2. If $t_{\text{c} }={\sqrt {\frac {a}{c} } }$ ::@:: the zeroth order term is normalized.

Both {@{substitutions are valid}@}. However, for {@{pedagogical reasons, the latter substitution (annotation: normalizing the zeroth order term) is used for second order systems}@}. {@{Choosing this substitution}@} allows {@{_x_<sub>c</sub> to be determined by normalizing the coefficient of the forcing function}@}: {@{$$1={\frac {At_{\text{c} }^{2} }{ax_{\text{c} } } }={\frac {A}{cx_{\text{c} } } }\Rightarrow x_{\text{c} }={\frac {A}{c} }.$$}@} {@{The differential equation}@} becomes {@{$${\frac {d^{2}\chi }{d\tau ^{2} } }+{\frac {b}{\sqrt {ac} } }{\frac {d\chi }{d\tau } }+\chi =F(\tau ).$$}@} {@{The coefficient of the first order term}@} is {@{unitless}@}. Define {@{$$2\zeta \ {\stackrel {\mathrm {def} }{=} }\ {\frac {b}{\sqrt {ac} } }.$$}@} {@{The factor 2 is present}@} so that {@{the solutions can be parameterized in terms of _ζ_}@}. In {@{the context of mechanical or electrical systems}@}, {@{_ζ_}@} is {@{known as the [damping ratio](damping%20ratio.md#damping%20ratio)}@}, and is {@{an important parameter required in the analysis of [control systems](control%20system.md)}@}. {@{2<!-- markdown separator -->_ζ_}@} is also {@{known as the [linewidth](linewidth.md#line%20broadening%20and%20shift) of the system}@}. {@{The result of the definition}@} is {@{the [universal oscillator equation](harmonic%20oscillator.md#universal%20oscillator%20equation)}@}. {@{$${\frac {d^{2}\chi }{d\tau ^{2} } }+2\zeta {\frac {d\chi }{d\tau } }+\chi =F(\tau ).$$}@}

### higher order systems

{@{The general _n_<!-- markdown separator -->th order linear differential equation with constant coefficients}@} has the form: {@{$$a_{n}{\frac {d^{n} }{dt^{n} } }x(t)+a_{n-1}{\frac {d^{n-1} }{dt^{n-1} } }x(t)+\ldots +a_{1}{\frac {d}{dt} }x(t)+a_{0}x(t)=\sum _{k=0}^{n}a_{k}{\big (}{\frac {d}{dt} }{\big )}^{k}x(t)=Af(t).$$}@} {@{The function _f_\(_t_\)}@} is known as {@{the [forcing function](forcing%20function%20(differential%20equations).md)}@}.

If {@{the differential equation only contains real \(not complex\) coefficients}@}, then {@{the properties of such a system}@} behaves as {@{a mixture of first and second order systems only}@}. This is because {@{the [roots](root%20of%20a%20function.md) of its [characteristic polynomial](characteristic%20polynomial.md)}@} are {@{either [real](real%20number.md), or [complex conjugate](complex%20conjugate.md) pairs}@}. Therefore, understanding {@{how nondimensionalization applies to first and second ordered systems}@} allows {@{the properties of higher order systems to be determined through [superposition](superposition%20principle.md)}@}. (annotation: {@{The total solution $x(t)$}@} combines {@{linearly via superposition}@}, where each {@{real root $r_i$ contributes a first-order term $c_i e^{r_i t}$}@} and each {@{complex conjugate pair $\alpha \pm i\beta$ contributes a second-order oscillatory term $e^{\alpha t}(C_1 \cos \beta t + C_2 \sin \beta t)$}@}.)

{@{The number of free parameters in a nondimensionalized form of a system}@} {@{increases with its order}@}. For this reason, {@{nondimensionalization is rarely used for higher order differential equations}@}. {@{The need for this procedure}@} has also been {@{reduced with the advent of [symbolic computation](symbolic%20computation.md)}@}.

### examples of recovering characteristic units

{@{A variety of systems}@} can be {@{approximated as either first or second order systems}@}. These include {@{mechanical, electrical, fluidic}@}, {@{caloric, and torsional systems}@}. This is because {@{the fundamental physical quantities involved within each of these examples}@} are {@{related through first and second order derivatives}@}.

#### mechanical oscillations

> {@{![A mass/spring/damper system drawn in [Inkscape](https://en.wikipedia.org/wiki/Inkscape) by [Ilmari Karonen](//commons.wikimedia.org/wiki/User:Ilmari_Karonen). [SVG](https://en.wikipedia.org/wiki/SVG) original available at [Image:Mass-Spring-Damper.svg](//commons.wikimedia.org/wiki/File:Mass-Spring-Damper.svg) or at [\[1\]](http://vyznev.net/misc/Mass-Spring-Damper.svg).](../../archives/Wikimedia%20Commons/Mass-Spring-Damper.png)}@}
>
> {@{A mass attached}@} to {@{a spring and a damper}@}.

Suppose we have {@{a mass attached to a spring and a damper}@}, which {@{in turn are attached to a wall}@}, and {@{a force acting on the mass along the same line}@}. Define (annotation: 6 items: {@{$x$, $t$, $f$, $m$, $B$, $k$}@})

- $x$ ::@:: = displacement from equilibrium \[m\]
- $t$ ::@:: = time \[s\]
- $f$ ::@:: = external force or "disturbance" applied to system \[kg⋅m⋅s<sup>−2</sup>\]
- $m$ ::@:: = mass of the block \[kg\]
- $B$ ::@:: = damping constant of [dashpot](dashpot.md) \[kg⋅s<sup>−1</sup>\]
- $k$ ::@:: = force constant of spring \[kg⋅s<sup>−2</sup>\]

Suppose {@{the applied force is a sinusoid _F_ = _F_<sub>0</sub> cos\(_ωt_\)}@}, {@{the differential equation that describes the motion of the block}@} is {@{$$m{\frac {d^{2}x}{dt^{2} } }+B{\frac {dx}{dt} }+kx=F_{0}\cos(\omega t)$$}@} {@{Nondimensionalizing this equation the same way as described under [§ Second order system](#second%20order%20system)}@} yields {@{several characteristics of the system}@}:

- The intrinsic unit _x_<sub>c</sub> ::@:: corresponds to the distance the block moves per unit force $$x_{\text{c} }={\frac {F_{0} }{k} }.$$
- The characteristic variable _t_<sub>c</sub> ::@:: is equal to the period of the oscillations $$t_{\text{c} }={\sqrt {\frac {m}{k} } }$$
- The dimensionless variable 2<!-- markdown separator -->_ζ_ ::@:: corresponds to the linewidth of the system. $$2\zeta ={\frac {B}{\sqrt {mk} } }$$
- _ζ_ itself ::@:: is the [damping ratio](damping%20ratio.md#damping%20ratio)

#### electrical oscillations

##### first-order series RC circuit

For {@{a series [RC](RC%20circuit.md) attached to a [voltage source](power%20supply.md)}@} {@{$$R{\frac {dQ}{dt} }+{\frac {Q}{C} }=V(t)\Rightarrow {\frac {d\chi }{d\tau } }+\chi =F(\tau )$$}@} with substitutions {@{$$Q=\chi x_{\text{c} },\ t=\tau t_{\text{c} },\ x_{\text{c} }=CV_{0},\ t_{\text{c} }=RC,\ F=V.$$}@} {@{The first characteristic unit}@} corresponds to {@{the total [charge](electric%20charge.md) in the circuit}@}. {@{The second characteristic unit}@} corresponds to {@{the [time constant](time%20constant.md) for the system}@}.

##### second-order series RLC circuit

For {@{a series configuration of _R_, _C_, _L_ components}@} where _Q_ is {@{the charge in the system}@} {@{$$L{\frac {d^{2}Q}{dt^{2} } }+R{\frac {dQ}{dt} }+{\frac {Q}{C} }=V_{0}\cos(\omega t)\Rightarrow {\frac {d^{2}\chi }{d\tau ^{2} } }+2\zeta {\frac {d\chi }{d\tau } }+\chi =\cos(\Omega \tau )$$}@} with the substitutions {@{$$Q=\chi x_{\text{c} },\ t=\tau t_{\text{c} },\ \ x_{\text{c} }=CV_{0},\ t_{\text{c} }={\sqrt {LC} },\ 2\zeta =R{\sqrt {\frac {C}{L} } },\ \Omega =t_{\text{c} }\omega .$$}@} {@{The first variable}@} corresponds to {@{the maximum charge stored in the circuit}@}. {@{The resonance frequency}@} is given by {@{the reciprocal of the characteristic time}@}. {@{The last expression}@} is {@{the linewidth of the system}@}. {@{The Ω}@} can be considered as {@{a normalized forcing function frequency}@}.

### quantum mechanics

#### quantum harmonic oscillator

{@{The [Schrödinger equation](Schrödinger%20equation.md)}@} for {@{the one-dimensional time independent [quantum harmonic oscillator](quantum%20harmonic%20oscillator.md)}@} is {@{$$\left(-{\frac {\hbar ^{2} }{2m} }{\frac {d^{2} }{dx^{2} } }+{\frac {1}{2} }m\omega ^{2}x^{2}\right)\psi (x)=E\psi (x).$$}@} {@{The modulus square of the [wavefunction](wavefunction.md) \|_ψ_\(_x_\)\|<sup>2</sup>}@} represents {@{probability density that, when integrated over _x_, gives a dimensionless probability}@}. Therefore, \|_ψ_\(_x_\)\|<sup>2</sup> has {@{units of inverse length}@}. To {@{nondimensionalize this}@}, it must be {@{rewritten as a function of a dimensionless variable}@}. To do this, we substitute {@{$${\tilde {x} }\equiv {\frac {x}{x_{\text{c} } } },$$}@} where {@{_x_<sub>c</sub> is some [characteristic length](characteristic%20length.md) of this system}@}. This gives us {@{a dimensionless wave function ${\tilde {\psi } }$}@} defined via {@{$$\psi (x)=\psi ({\tilde {x} }x_{\text{c} })=\psi (x({\tilde {x} }))={\tilde {\psi } }({\tilde {x} }).$$}@} {@{The differential equation}@} then becomes {@{$$\left(-{\frac {\hbar ^{2} }{2m} }{\frac {1}{x_{\text{c} }^{2} } }{\frac {d^{2} }{d{\tilde {x} }^{2} } }+{\frac {1}{2} }m\omega ^{2}x_{\text{c} }^{2}{\tilde {x} }^{2}\right){\tilde {\psi } }({\tilde {x} })=E\,{\tilde {\psi } }({\tilde {x} })\Rightarrow \left(-{\frac {d^{2} }{d{\tilde {x} }^{2} } }+{\frac {m^{2}\omega ^{2}x_{\text{c} }^{4} }{\hbar ^{2} } }{\tilde {x} }^{2}\right){\tilde {\psi } }({\tilde {x} })={\frac {2mx_{\text{c} }^{2}E}{\hbar ^{2} } }{\tilde {\psi } }({\tilde {x} }).$$}@} To make {@{the term in front of ${\tilde {x} }^{2}$ dimensionless}@}, set {@{$${\frac {m^{2}\omega ^{2}x_{\text{c} }^{4} }{\hbar ^{2} } }=1\Rightarrow x_{\text{c} }={\sqrt {\frac {\hbar }{m\omega } } }.$$}@} {@{The fully nondimensionalized equation}@} is {@{$$\left(-{\frac {d^{2} }{d{\tilde {x} }^{2} } }+{\tilde {x} }^{2}\right){\tilde {\psi } }({\tilde {x} })={\tilde {E} }{\tilde {\psi } }({\tilde {x} }),$$}@} where we have defined {@{$$E\equiv {\frac {\hbar \omega }{2} }{\tilde {E} }.$$}@} {@{The factor in front of ${\tilde {E} }$}@} is {@{in fact \(coincidentally\) the [ground state](ground%20state.md) energy of the harmonic oscillator}@}. Usually, {@{the energy term is not made dimensionless}@} as we are {@{interested in determining the energies of the [quantum states](quantum%20state.md)}@}. Rearranging {@{the first equation, the familiar equation for the harmonic oscillator}@} becomes {@{$${\frac {\hbar \omega }{2} }\left(-{\frac {d^{2} }{d{\tilde {x} }^{2} } }+{\tilde {x} }^{2}\right){\tilde {\psi } }({\tilde {x} })=E{\tilde {\psi } }({\tilde {x} }).$$}@}

## statistical analogs

- Main article: ::@:: [Normalization \(statistics\)](normalization%20(statistics).md)

In {@{[statistics](statistics.md)}@}, {@{the analogous process}@} is usually {@{dividing a difference \(a distance\) by a scale factor \(a measure of [statistical dispersion](statistical%20dispersion.md)\), which yields a dimensionless number}@}, which is called {@{_[normalization](normalization%20(statistics).md)_}@}. Most often, this is dividing {@{[errors or residuals](errors%20and%20residuals%20in%20statistics.md) by the [standard deviation](standard%20deviation.md) or sample standard deviation}@}, respectively, yielding {@{[standard scores](standard%20score.md) and [studentized residuals](studentized%20residual.md)}@}.

## see also

- [Buckingham π theorem](Buckingham%20π%20theorem.md)
- [Dimensionless number](dimensionless%20number.md)
- [Natural units](natural%20units.md)
- [System equivalence](system%20equivalence.md)
- [RLC circuit](RLC%20circuit.md)
- [RL circuit](RL%20circuit.md)
- [RC circuit](RC%20circuit.md)
- [Logistic equation](logistic%20map.md)
- [Per-unit system](per-unit%20system.md)

## notes

## references

This text incorporates [content](https://en.wikipedia.org/wiki/nondimensionalization) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFHolmes2009"></a> Holmes, Mark H. \(2009\). [_Introduction to the Foundations of Applied Mathematics_](https://www.google.com/books/edition/Introduction_to_the_Foundations_of_Appli/2AS6cZQELgkC). Springer. pp. 25–33. [ISBN](ISBN%20(identifier).md) [978-0-387-87749-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-87749-5). <a id="^ref-1"></a>^ref-1

## external links

- [Analysis of differential equation models in biology: a case study for clover meristem populations](http://www.royalsociety.org.nz/publications/journals/nzja/1998/059/) \(Application of nondimensionalization to a problem in biology\).
- [Course notes for Mathematical Modelling and Industrial Mathematics](https://web.archive.org/web/20050306141857/http://www.maths.bath.ac.uk/~masjde/MSc/CourseNotes/MA50176.pdf) _Jonathan Evans, Department of Mathematical Sciences, [University of Bath](University%20of%20Bath.md)_. \(see Chapter 3\).
- [Scaling of Differential Equations](https://hplgit.github.io/scaling-book/doc/pub/book/pdf/scaling-book-4screen-sol.pdf) _Hans Petter Langtangen, Geir K. Pedersen, Center for Biomedical Computing, Simula Research Laboratory and Department of Informatics, [University of Oslo](University%20of%20Oslo.md)_.

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Dimensional analysis](https://en.wikipedia.org/wiki/Category:Dimensional%20analysis)
