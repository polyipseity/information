---
aliases:
  - branch current method
  - branch current methods
  - nodal analysis
  - node-voltage analysis
tags:
  - flashcard/active/general/eng/nodal_analysis
  - language/in/English
---

# nodal analysis

> {@{![Kirchhoff's current law is the basis of nodal analysis.](../../archives/Wikimedia%20Commons/KCL%20-%20Kirchhoff%27s%20circuit%20laws.svg)}@}
>
> {@{Kirchhoff's current law is the basis of nodal analysis.}@} <!--SR:!2025-03-20,4,286!2025-03-20,4,270-->

In {@{electric circuits analysis}@}, {@{__nodal analysis__, __node-voltage analysis__, or the __branch current method__}@} is {@{a method of determining the voltage \([potential difference](potential%20difference.md)\) between "[nodes](node%20(circuits).md)" \(points where elements or branches connect\) in an [electrical circuit](electrical%20circuit.md) in terms of the branch currents}@}. <!--SR:!2025-03-20,4,286!2025-03-20,4,270!2025-03-20,4,270-->

Nodal analysis is {@{essentially a systematic application of [Kirchhoff's current law](Kirchhoff's%20circuit%20laws.md) \(KCL\) for [circuit analysis](circuit%20analysis.md)}@}. Similarly, {@{[mesh analysis](mesh%20analysis.md) is a systematic application of Kirchhoff's voltage law \(KVL\)}@}. Nodal analysis writes {@{an equation at each [electrical node](node%20(circuits).md) specifying that the branch currents incident at a node must sum to zero \(using KCL\)}@}. The branch currents are {@{written in terms of the circuit node voltages}@}. As a consequence, {@{each branch constitutive relation must give current as a function of voltage}@}; {@{an [admittance](admittance.md) representation}@}. For instance, for {@{a resistor, I<sub>branch</sub> = V<sub>branch</sub> \* G}@}, where {@{G \(=1/R\) is the admittance \(conductance\) of the resistor}@}. <!--SR:!2025-03-20,4,286!2025-03-20,4,270!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,270!2025-03-20,4,270!2025-03-20,4,270!2025-03-20,4,286-->

Nodal analysis is {@{possible when all the circuit elements' branch constitutive relations have an admittance representation}@}. Nodal analysis produces {@{a compact set of equations for the network}@}, which can be {@{solved by hand if small, or can be quickly solved using linear algebra by computer}@}. Because of {@{the compact system of equations}@}, {@{many [circuit simulation](circuit%20simulation.md) programs \(e.g., [SPICE](SPICE.md)\)}@} use {@{nodal analysis as a basis}@}. When {@{elements do not have admittance representations}@}, {@{a more general extension of nodal analysis, [modified nodal analysis](modified%20nodal%20analysis.md), can be used}@}. <!--SR:!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,286-->

## procedure

1. \(annotation: label\) ::@:: Note all connected wire segments in the circuit. These are the _nodes_ of nodal analysis. <!--SR:!2025-03-20,4,270!2025-03-20,4,286-->
2. \(annotation: reference\) ::@:: Select one node as the [ground](ground%20(electricity).md) reference. The choice does not affect the element voltages \(but it does affect the nodal voltages\) and is just a matter of convention. Choosing the node with the most connections can simplify the analysis. For a circuit of _N_ nodes the number of nodal equations is _N_<!-- markdown separator -->−1. <!--SR:!2025-03-20,4,286!2025-03-20,4,286-->
3. \(annotation: variables\) ::@:: Assign a variable for each node whose voltage is unknown. If the voltage is already known, it is not necessary to assign a variable. <!--SR:!2025-03-20,4,286!2025-03-20,4,270-->
4. \(annotation: KCL\) ::@:: For each unknown voltage, form an equation based on Kirchhoff's Current Law \(i.e. add together all currents leaving from the node and mark the sum equal to zero\). The current between two nodes is equal to the voltage of the node where the current exits minus the voltage of the node where the current enters the node, both divided by the resistance between the two nodes. <!--SR:!2025-03-20,4,286!2025-03-20,4,270-->
5. \(annotation: supernode\) ::@:: If there are voltage sources between two unknown voltages, join the two nodes as a [supernode](supernode%20(circuit).md). The currents of the two nodes are combined in a single equation, and a new equation for the voltages is formed. <!--SR:!2025-03-20,4,286!2025-03-20,4,286-->
6. \(annotation: solving\) ::@:: Solve the system of [simultaneous equations](simultaneous%20equations.md) for each unknown voltage. <!--SR:!2025-03-20,4,286!2025-03-20,4,286-->

## examples

### basic case

> {@{![Basic example circuit with one unknown voltage, V<sub>1</sub>1.](../../archives/Wikimedia%20Commons/Nodal%20analysis.svg)}@}
>
> {@{Basic example circuit with one unknown voltage, V<sub>1</sub>.}@} <!--SR:!2025-03-20,4,286!2025-03-20,4,270-->

{@{The only unknown voltage in this circuit is $V_{1}$}@}. There are {@{three connections to this node and consequently three currents to consider}@}. {@{The direction of the currents in calculations}@} is {@{chosen to be away from the node}@}. <!--SR:!2025-03-20,4,270!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,286-->

1. Current through resistor $R_{1}$: $(V_{1}-V_{S})/R_{1}$
2. Current through resistor $R_{2}$: $V_{1}/R_{2}$
3. Current through current source $I_{S}$: $-I_{S}$

With {@{Kirchhoff's current law}@}, we get: {@{$${\frac {V_{1}-V_{S} }{R_{1} } }+{\frac {V_{1} }{R_{2} } }-I_{S}=0$$}@} This equation can be {@{solved with respect to V<sub>1</sub>}@}: {@{$$V_{1}={\frac {\left({\frac {V_{S} }{R_{1} } }+I_{S}\right)}{\left({\frac {1}{R_{1} } }+{\frac {1}{R_{2} } }\right)} }$$}@} Finally, {@{the unknown voltage can be solved by substituting numerical values for the symbols}@}. {@{Any unknown currents are easy to calculate}@} after {@{all the voltages in the circuit are known}@}. {@{$$V_{1}={\frac {\left({\frac {5{\text{ V} } }{100\,\Omega } }+20{\text{ mA} }\right)}{\left({\frac {1}{100\,\Omega } }+{\frac {1}{200\,\Omega } }\right)} }={\frac {14}{3} }{\text{ V} }$$}@} \(annotation: circuit for reference: ![circuit for reference](../../archives/Wikimedia%20Commons/Nodal%20analysis.svg)\) <!--SR:!2025-03-20,4,270!2025-03-20,4,270!2025-03-20,4,286!2025-03-20,4,270!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,270!2025-03-20,4,286-->

### supernodes

> {@{![In this circuit, V<sub>A</sub> is between two unknown voltages, and is therefore a supernode.](../../archives/Wikimedia%20Commons/Supernode%20in%20circuit%20analysis.svg)}@}
>
> In this circuit, {@{V<sub>A</sub> is between two unknown voltages, and is therefore a supernode}@}. <!--SR:!2025-03-20,4,286!2025-03-20,4,270-->

In this circuit, we {@{initially have two unknown voltages, V<sub>1</sub> and V<sub>2</sub>}@}. {@{The voltage at V<sub>3</sub> is already known to be V<sub>B</sub>}@} because {@{the other terminal of the voltage source is at ground potential}@}. <!--SR:!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,286-->

{@{The current going through voltage source V<sub>A</sub>}@} {@{cannot be directly calculated}@}. Therefore, {@{we cannot write the current equations for either V<sub>1</sub> or V<sub>2</sub>}@}. However, we know that {@{the same current leaving node V<sub>2</sub> must enter node V<sub>1</sub>}@}. Even though {@{the nodes cannot be individually solved}@}, we know that {@{the combined current of these two nodes is zero}@}. {@{This combining of the two nodes}@} is called {@{the [supernode](supernode%20(circuit).md) technique}@}, and it {@{requires one additional equation: V<sub>1</sub> = V<sub>2</sub> + V<sub>A</sub>}@}. <!--SR:!2025-03-20,4,286!2025-03-20,4,270!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,270!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,286-->

{@{The complete set of equations for this circuit}@} is: {@{$${\begin{cases}{\frac {V_{1}-V_{\text{B} } }{R_{1} } }+{\frac {V_{2}-V_{\text{B} } }{R_{2} } }+{\frac {V_{2} }{R_{3} } }=0\\V_{1}=V_{2}+V_{\text{A} }\\\end{cases} }$$}@} By substituting $$V_{2}={\frac {(R_{1}+R_{2})R_{3}V_{\text{B} }-R_{2}R_{3}V_{\text{A} } }{(R_{1}+R_{2})R_{3}+R_{1}R_{2} } }$$ \(annotation: circuit for reference: ![circuit for reference](../../archives/Wikimedia%20Commons/Supernode%20in%20circuit%20analysis.svg)\) <!--SR:!2025-03-20,4,270!2025-03-19,3,250-->

## matrix form for the node-voltage equation

In general, for {@{a circuit with $N$ nodes}@}, {@{the node-voltage equations obtained by nodal analysis}@} can be {@{written in a matrix form as derived in the following}@}. For {@{any node $k$, KCL states $\sum _{j\neq k}G_{jk}(v_{k}-v_{j})=0$}@} where {@{$G_{kj}=G_{jk}$ is the negative of the sum of the conductances between nodes $k$ and $j$ \(annotation: we take negative here so that the matrix below does not contain negative signs\), and $v_{k}$ is the voltage of node $k$}@}. This implies {@{$0=\sum _{j\neq k}G_{jk}(v_{k}-v_{j})=\sum _{j\neq k}G_{jk}v_{k}-\sum _{j\neq k}G_{jk}v_{j}=G_{kk}v_{k}-\sum _{j\neq k}G_{jk}v_{j}$}@} where {@{$G_{kk}$ is the sum of conductances connected to node $k$}@}. We note that {@{the first term contributes linearly to the node $k$ via $G_{kk}$}@}, while {@{the second term contributes linearly to each node $j$ connected to the node $k$ via $G_{jk}$ with a minus sign}@}. If {@{an independent current source/input $i_{k}$ is also attached to node $k$}@}, the above expression is {@{generalized to $i_{k}=G_{kk}v_{k}-\sum _{j\neq k}G_{jk}v_{j}$}@}. It is readily shown that {@{one can combine the above node-voltage equations for all $N$ nodes, and write them down in the following matrix form}@} {@{$${\begin{pmatrix}G_{11}&G_{12}&\cdots &G_{1N}\\G_{21}&G_{22}&\cdots &G_{2N}\\\vdots &\vdots &\ddots &\vdots \\G_{N1}&G_{N2}&\cdots &G_{NN}\end{pmatrix} }{\begin{pmatrix}v_{1}\\v_{2}\\\vdots \\v_{N}\end{pmatrix} }={\begin{pmatrix}i_{1}\\i_{2}\\\vdots \\i_{N}\end{pmatrix} }$$}@} or simply {@{$\mathbf {Gv} =\mathbf {i}$}@}. <!--SR:!2025-03-20,4,270!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,270!2025-03-20,4,286!2025-03-19,3,266!2025-03-20,4,270!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,286!2025-03-19,3,266!2025-03-20,4,270!2025-03-20,4,270!2025-03-20,4,286-->

{@{The matrix $\mathbf {G}$ on the left hand side of the equation is singular}@} since {@{it satisfies $\mathbf {G1} = \mathbf 0$ where $\mathbf {1}$ is an $N\times 1$ column matrix containing only 1s}@}. This corresponds to {@{the fact of current conservation, namely, $\sum _{k}i_{k}=0$, and the freedom to choose a reference node \(ground\)}@}. In practice, {@{the voltage at the reference node is taken to be 0}@}. Consider {@{it is the last node, $v_{N}=0$}@}. In this case, it is {@{straightforward to verify that the resulting equations for the other $N-1$ nodes remain the same}@}, and therefore {@{one can simply discard the last column as well as the last line of the matrix equation}@}. This procedure results in {@{a $(N-1)\times (N-1)$ dimensional non-singular matrix equation with the definitions of all the elements stay unchanged}@}. <!--SR:!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,270!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,286!2025-03-20,4,270!2025-03-20,4,286-->

## see also

- [Mesh analysis](mesh%20analysis.md)
- [Ybus matrix](Ybus%20matrix.md)
- [Topology \(electrical circuits\)](topology%20(electrical%20circuits).md)
- [Charge conservation](charge%20conservation.md)
- [Circuit diagram](circuit%20diagram.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/nodal_analysis) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- [P. Dimo](Paul%20Dimo.md) Nodal Analysis of Power Systems Abacus Press Kent 1975

## external links

> ![Wikiversity logo](../../archives/Wikimedia%20Commons/Wikiversity%20logo%202017.svg) Wikiversity has learning resources about ___[Nodal analysis](https://en.wikiversity.org/wiki/Nodal%20analysis)___

- [Branch current method](http://www.allaboutcircuits.com/vol_1/chpt_10/2.html)
- [Online four-node problem solver](http://www.catc.ac.ir/mazlumi/node.php)
- [Simple Nodal Analysis Example](http://jeffreyfreeman.me/nodal-analysis-tutorial/)

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Electronic circuits](https://en.wikipedia.org/wiki/Category:Electronic%20circuits)
> - [Electrical engineering](https://en.wikipedia.org/wiki/Category:Electrical%20engineering)
