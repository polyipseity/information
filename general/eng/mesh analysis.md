---
aliases:
  - loop analysis
  - loop current
  - loop currents
  - mesh analysis
  - mesh current method
  - mesh current methods
tags:
  - flashcard/active/general/eng/mesh_analysis
  - language/in/English
---

# mesh analysis

- {@{"Loop current"}@} redirects here. For {@{the ocean current in the Gulf of Mexico}@}, see {@{[Loop Current](Loop%20Current.md)}@}. For {@{the electrical signalling scheme}@}, see {@{[current loop](current%20loop.md)}@}. <!--SR:!2025-06-05,62,310!2025-06-06,63,310!2025-06-10,67,328!2025-06-09,66,328!2025-06-16,70,328-->

> {@{![Figure 1: Essential meshes of the planar circuit labeled 1, 2, and 3.](../../archives/Wikimedia%20Commons/Mesh%20Analysis%20Example1%20TeX.svg)}@}
>
> Figure 1: {@{Essential meshes of the planar circuit labeled 1, 2, and 3}@}. {@{R<sub>1</sub>, R<sub>2</sub>, R<sub>3</sub>, 1/sC, and sL}@} represent {@{the [impedance](electrical%20impedance.md) of the [resistors](resistor.md), [capacitor](capacitor.md), and [inductor](inductor.md) values in the [s-domain](s-domain.md)}@}. {@{V<sub>s</sub> and I<sub>s</sub>}@} are {@{the values of the [voltage source](voltage%20source.md) and [current source](current%20source.md), respectively}@}. <!--SR:!2025-06-19,73,328!2025-05-31,58,310!2025-05-31,58,310!2025-06-05,62,310!2025-06-20,74,328!2025-06-16,70,328-->

{@{__Mesh analysis__ \(or the __mesh current method__\)}@} is {@{a [circuit analysis](circuit%20analysis.md) method for [planar circuits](planar%20graph.md)}@}. Planar circuits are {@{circuits that can be drawn on a [plane surface](plane%20(mathematics).md) with no [wires](wire.md) crossing each other}@}. {@{A more general technique, called __loop analysis__ \(with the corresponding network variables called __loop currents__\)}@} can be {@{applied to any circuit, planar or not}@}<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup>. Mesh analysis and loop analysis both {@{make systematic use of [Kirchhoff’s voltage law](Kirchhoff's%20circuit%20laws.md)}@} to {@{arrive at a set of equations guaranteed to be solvable if the circuit has a solution}@}.<sup>[\[1\]](#^ref-1)</sup> Mesh analysis is {@{usually easier to use when the circuit is planar, compared to loop analysis}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-06-17,71,328!2025-06-13,67,310!2025-06-19,73,328!2025-06-05,62,310!2025-06-06,63,310!2025-06-05,62,310!2025-06-06,63,310!2025-06-18,72,328-->

## mesh currents and essential meshes

> ![Figure 2: Circuit with mesh currents labeled as I<sub>1</sub>, I<sub>2</sub>, and I<sub>3</sub>.](../../archives/Wikimedia%20Commons/Mesh%20Analysis%20Example2%20TeX.svg)
>
> Figure 2: {@{Circuit with mesh currents labeled as I<sub>1</sub>, I<sub>2</sub>, and I<sub>3</sub>}@}. The arrows {@{show the direction of the mesh current}@}. <!--SR:!2025-05-31,58,310!2025-06-16,70,328-->

Mesh analysis works by {@{arbitrarily assigning mesh currents in the essential meshes \(also referred to as independent meshes\)}@}. An essential mesh is {@{a loop in the circuit that does not contain any other loop}@}. Figure 1 {@{labels the essential meshes with one, two, and three}@}.<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2025-05-16,43,290!2025-06-10,67,328!2025-06-16,70,328-->

{@{A mesh current}@} is {@{a current that loops around the essential mesh and the equations are solved in terms of them}@}. A mesh current {@{may not correspond to any physically flowing current}@}, but {@{the physical currents are easily found from them}@}.<sup>[\[2\]](#^ref-2)</sup> It is usual practice to {@{have all the mesh currents loop in the same direction}@}. This helps {@{prevent errors when writing out the equations}@}. The convention is to {@{have all the mesh currents looping in a [clockwise](clockwise.md) direction}@}.<sup>[\[3\]](#^ref-3)</sup> Figure 2 shows {@{the same circuit from Figure 1 with the mesh currents labeled}@}. <!--SR:!2025-06-16,70,328!2025-05-16,43,290!2025-06-11,65,310!2025-05-16,43,290!2025-05-31,58,310!2025-06-06,63,310!2025-06-19,73,328!2025-06-12,66,310-->

{@{Solving for mesh currents}@} instead of {@{directly applying [Kirchhoff's current law](Kirchhoff's%20circuit%20laws.md#Kirchhoff's%20current%20law%20(KCL)) and [Kirchhoff's voltage law](Kirchhoff's%20circuit%20laws.md#Kirchhoff's%20voltage%20law%20(KVL))}@} can {@{greatly reduce the amount of calculation required}@}. This is because {@{there are fewer mesh currents than there are physical branch currents}@}. In figure 2 for example, there are {@{six branch currents but only three mesh currents}@}. <!--SR:!2025-06-06,63,310!2025-06-18,72,328!2025-05-31,58,310!2025-06-19,73,328!2025-06-20,74,328-->

## setting up the equations

Each mesh {@{produces one equation}@}. These equations are {@{the sum of the [voltage drops](voltage%20drop.md) in a complete loop of the mesh current}@}.<sup>[\[3\]](#^ref-3)</sup> For {@{problems more general than those including [current](current%20source.md) and [voltage sources](voltage%20source.md)}@}, the [voltage drops](voltage%20drop.md) will be {@{the [impedance](electrical%20impedance.md) of the [electronic component](electronic%20component.md) multiplied by the mesh current in that loop}@}.<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2025-06-21,75,328!2025-06-10,64,310!2025-06-18,72,328!2025-06-12,66,310-->

If {@{a [voltage source](voltage%20source.md) is present within the mesh loop}@}, {@{the [voltage](voltage.md) at the source}@} is {@{either added or subtracted depending on if it is a [voltage drop](voltage%20drop.md) or a voltage rise in the direction of the mesh current}@}. For {@{a [current source](current%20source.md) that is not contained between two meshes}@} \(for example, {@{the current source in essential mesh 1 in the circuit above}@}\), the mesh current will {@{take the positive or negative value of the [current source](current%20source.md) depending on if the mesh current is in the same or opposite direction of the [current source](current%20source.md)}@}.<sup>[\[3\]](#^ref-3)</sup> The following is {@{the same circuit from above with the equations needed to solve for all the currents in the circuit}@}. {@{$${\begin{cases}{\text{Mesh 1: } }I_{1}=I_{s}\\{\text{Mesh 2: } }-V_{s}+R_{1}(I_{2}-I_{1})+{\frac {1}{sC} }(I_{2}-I_{3})=0\\{\text{Mesh 3: } }{\frac {1}{sC} }(I_{3}-I_{2})+R_{2}(I_{3}-I_{1})+sLI_{3}=0\\\end{cases} }\,$$}@} \(annotation: circuit for reference: ![circuit for reference](../../archives/Wikimedia%20Commons/Mesh%20Analysis%20Example2%20TeX.svg)\) <!--SR:!2025-05-31,58,310!2025-06-06,63,310!2025-06-11,65,310!2025-06-05,62,310!2025-06-17,71,328!2025-05-31,58,310!2025-09-11,134,308!2025-05-26,49,308-->

Once {@{the equations are found}@}, {@{the [system of linear equations](system%20of%20linear%20equations.md)}@} can be {@{solved by using any technique to solve [linear equations](linear%20equation.md)}@}. <!--SR:!2025-06-05,62,310!2025-06-05,62,310!2025-05-31,58,310-->

## special cases

There are {@{two special cases in mesh current}@}: {@{currents containing a supermesh and currents containing [dependent sources](dependent%20source.md)}@}. <!--SR:!2025-06-21,75,328!2025-06-17,71,328-->

### supermesh

> {@{![Figure 3: Circuit with a supermesh.](../../archives/Wikimedia%20Commons/Mesh%20Analysis%20Example3%20TeX.svg)}@}
>
> Figure 3: {@{Circuit with a supermesh}@}. Supermesh occurs because {@{the current source is in between the essential meshes}@}. <!--SR:!2025-06-20,74,328!2025-05-31,58,310!2025-06-16,70,328-->

{@{A supermesh occurs}@} when {@{a [current source](current%20source.md) is contained between two essential meshes}@}. The circuit is {@{first treated as if the [current source](current%20source.md) is not there}@}. This leads to {@{one equation that incorporates two mesh currents}@}. Once {@{this equation is formed}@}, {@{an equation is needed that relates the two mesh currents with the [current source](current%20source.md)}@}. This will be {@{an equation where the [current source](current%20source.md) is equal to one of the mesh currents minus the other}@}. The following is {@{a simple example of dealing with a supermesh}@}.<sup>[\[2\]](#^ref-2)</sup> {@{$${\begin{cases}{\text{Mesh 1, 2: } }-V_{s}+R_{1}I_{1}+R_{2}I_{2}=0\\{\text{Current source: } }I_{s}=I_{2}-I_{1}\end{cases} }\,$$}@} \(annotation: circuit for reference: ![circuit for reference](../../archives/Wikimedia%20Commons/Mesh%20Analysis%20Example3%20TeX.svg)\) <!--SR:!2025-06-16,70,328!2025-06-21,75,328!2025-06-05,62,310!2025-05-31,58,310!2025-06-06,63,310!2025-06-17,71,328!2025-05-20,46,290!2025-08-23,115,290!2025-05-26,49,308-->

### dependent sources

- See also: ::@:: [Dependent source](dependent%20source.md) <!--SR:!2025-05-31,58,310!2025-05-31,58,310-->

> {@{![Figure 4: Circuit with dependent source](../../archives/Wikimedia%20Commons/Mesh%20Analysis%20Example4%20TeX.svg)}@}
>
> Figure 4: {@{Circuit with dependent source}@}. I<sub>x</sub> is the current upon which the dependent source depends. <!--SR:!2025-05-16,43,290!2025-06-17,71,328-->

{@{A dependent source}@} is {@{a [current source](current%20source.md) or [voltage source](voltage%20source.md) that depends on the [voltage](voltage.md) or [current](electric%20current.md) of another [element](electronic%20component.md) in the circuit}@}. When {@{a dependent source is contained within an essential mesh}@}, {@{the dependent source should be treated like an independent source}@}. After {@{the mesh equation is formed}@}, {@{a dependent source equation is needed}@}. This equation is {@{generally called a constraint equation}@}. This is {@{an equation that relates the dependent source's variable to the [voltage](voltage.md) or [current](electric%20current.md) that the source depends on in the circuit}@}. The following is {@{a simple example of a dependent source}@}.<sup>[\[2\]](#^ref-2)</sup> {@{$${\begin{cases}{\text{Mesh 1: } }-V_{s}+R_{1}I_{1}+R_{3}(I_{1}-I_{2})=0\\{\text{Mesh 2: } }R_{2}I_{2}+3I_{x}+R_{3}(I_{2}-I_{1})=0\\{\text{Dependent variable: } }I_{x}=I_{1}-I_{2}\end{cases} }\,$$}@} \(annotation: circuit for reference: ![circuit for reference](../../archives/Wikimedia%20Commons/Mesh%20Analysis%20Example4%20TeX.svg)\) <!--SR:!2025-06-20,74,328!2025-06-06,63,310!2025-05-31,58,310!2025-06-18,72,328!2025-05-31,58,310!2025-06-17,71,328!2025-05-31,58,310!2025-05-16,43,290!2025-06-15,69,328!2025-08-01,93,288-->

## see also

- [Ohm's law](Ohm's%20law.md)
- [Analysis of resistive circuits](analysis%20of%20resistive%20circuits.md)
- [Nodal analysis](nodal%20analysis.md)
- [Kirchhoff's circuit laws](Kirchhoff's%20circuit%20laws.md)
- [Source transformation](source%20transformation.md)
- [Topology \(electrical circuits\)](topology%20(electrical%20circuits).md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/mesh_analysis) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Hayt, William H., & Kemmerly, Jack E. \(1993\). _Engineering Circuit Analysis_ \(5th ed.\), New York: McGraw Hill. <a id="^ref-1"></a>^ref-1
2. Nilsson, James W., & Riedel, Susan A. \(2002\). _Introductory Circuits for Electrical and Computer Engineering_. New Jersey: Prentice Hall. <a id="^ref-2"></a>^ref-2
3. Lueg, Russell E., & Reinhard, Erwin A. \(1972\). _Basic Electronics for Engineers and Scientists_ \(2nd ed.\). New York: International Textbook Company. <a id="^ref-3"></a>^ref-3
4. Puckett, Russell E., & Romanowitz, Harry A. \(1976\). _Introduction to Electronics_ \(2nd ed.\). San Francisco: John Wiley and Sons, Inc. <a id="^ref-4"></a>^ref-4

## external links

- [Mesh current method](http://www.allaboutcircuits.com/vol_1/chpt_10/3.html)
- [Online three-mesh problem solver](http://www.catc.ac.ir/mazlumi/mesh.php)

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Electrical engineering](https://en.wikipedia.org/wiki/Category:Electrical%20engineering)
> - [Electronic engineering](https://en.wikipedia.org/wiki/Category:Electronic%20engineering)
> - [Electrical circuits](https://en.wikipedia.org/wiki/Category:Electrical%20circuits)
> - [Electronic circuits](https://en.wikipedia.org/wiki/Category:Electronic%20circuits)
> - [Electronic design](https://en.wikipedia.org/wiki/Category:Electronic%20design)
