---
aliases:
  - ELEC 2400 mesh analysis
  - ELEC2400 mesh analysis
  - HKUST ELEC 2400 mesh analysis
  - HKUST ELEC2400 mesh analysis
  - loop analysis
  - mesh analysis
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/mesh_analysis
  - language/in/English
---

# mesh analysis

Mesh analysis solves a circuit by taking a circulating current in each mesh as the unknown and writing one voltage law equation per mesh. It is the voltage-law counterpart of nodal analysis, and needs the circuit to be drawable on a plane with no branch crossing another.

Its unknowns are currents, so a branch shared by two meshes carries the difference of their currents. For the same circuit it never needs fewer equations than nodal analysis, and usually more.

---

Flashcards for this section are as follows:

- overview ::@:: Mesh analysis takes one circulating current per mesh as the unknown and writes one voltage law equation per mesh, giving $b - n + 1$ equations for a planar circuit of $b$ branches and $n$ nodes. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## planar circuits

Mesh analysis applies when a circuit of $n$ nodes and $b$ branches can be laid out on a plane with no crossing of branches, that is, when it is a planar graph. There are then $b - (n - 1)$ independent voltage law equations related to loop or mesh currents.

Meshes and loops are treated the same way, so a chosen loop need not be a mesh when a source makes a mesh inconvenient.

---

Flashcards for this section are as follows:

- overview ::@:: Mesh analysis applies to planar circuits, those that can be drawn on a plane with no crossing branches, and rests on $b - (n - 1)$ independent voltage law equations. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- planarity: what geometric property must a circuit have for mesh analysis to apply? ::@:: It must be drawable on a plane without any branch crossing another, making it a planar graph.
- independent equations: a planar circuit has $b$ branches and $n$ nodes; how many independent voltage law equations exist? ::@:: $b - (n - 1)$, one fewer than the number of branches less the independent nodes.
- loops against meshes: in applying the method, must every chosen loop be a mesh? ::@:: No: loops and meshes are treated the same way, and a loop other than a mesh may be chosen when that is more convenient.

## procedure

Assign loops or meshes with their loop or mesh currents. An element $R_i$ in only one loop, carrying $I_j$, drops $I_j R_i$; one in two loops, carrying $I_j$ and $I_k$, drops $(I_j \pm I_k) R_i$, the sign following the directions of the two currents.

The equations are the voltage law round each mesh in turn, and the $b - n + 1$ of them are solved for the mesh currents. In a worked two-mesh circuit of a $12\text{ V}$ source, a $3\text{ V}$ source, and resistors of $3\text{ k}\Omega$, $6\text{ k}\Omega$, $3\text{ k}\Omega$, $2\text{ k}\Omega$, and $1\text{ k}\Omega$, the equations $12 - 3\text{ k} I_1 - 6\text{ k}(I_1 - I_2) - 3\text{ k} I_1 = 0$ and $3 + 2\text{ k} I_2 + 6\text{ k}(I_2 - I_1) + 1\text{ k} I_2 = 0$ reduce to $12\text{ k} I_1 - 6\text{ k} I_2 = 12$ and $6\text{ k} I_1 - 9\text{ k} I_2 = 3$, so $I_2 = 0.5\text{ mA}$ and $I_1 = 1.25\text{ mA}$.

---

Flashcards for this section are as follows:

- overview ::@:: The procedure assigns a circulating current to every mesh, expresses each resistor's voltage drop from the mesh currents through it, writes the voltage law round each mesh, and solves the resulting system.
- element in one mesh: a resistor $R_i$ lies in a single mesh whose current is $I_j$; what is the voltage drop across it? ::@:: $I_j R_i$.
- element in two meshes: a resistor $R_i$ lies in two meshes whose currents are $I_j$ and $I_k$; what is the voltage drop across it? ::@:: $(I_j \pm I_k) R_i$, with the sign fixed by the directions of the two currents.
- two-mesh result: the two meshes of the worked circuit give $12\text{ k} I_1 - 6\text{ k} I_2 = 12$ and $6\text{ k} I_1 - 9\text{ k} I_2 = 3$; find $I_1$ and $I_2$. ::@:: Eliminating $I_1$ gives $I_2 = 0.5\text{ mA}$ and back-substitution gives $I_1 = 1.25\text{ mA}$.

## shared elements

A branch shared by two meshes carries the difference of the mesh currents, $I_o = I_1 - I_2$ when both are taken in the same sense through it, and its voltage drop is $(I_j \pm I_k)R_i$.

A mesh current is not in general a branch current: it equals the branch current only where the branch lies in that mesh alone.

---

Flashcards for this section are as follows:

- overview ::@:: A branch shared by two meshes carries the difference of the mesh currents, $I_o = I_1 - I_2$, and its voltage drop is $(I_j \pm I_k)R_i$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- shared branch current: two mesh currents $I_1$ and $I_2$ pass through the same resistor in the same sense; what current does the branch carry? ::@:: $I_o = I_1 - I_2$.
- mesh against branch current: is a mesh current always the current in some branch? ::@:: No: it equals the branch current only where the branch lies in that mesh alone.
- worked shared branch: the worked two-mesh circuit has $I_1 = 1.25\text{ mA}$ and $I_2 = 0.5\text{ mA}$ through a shared $6\text{ k}\Omega$ resistor; what is $I_o$? ::@:: $I_o = I_1 - I_2 = 0.75\text{ mA}$.

## supermesh

A current source shared by two meshes blocks the voltage law, since the voltage across it is not known from the mesh currents. The remedy is a superloop or supermesh spanning both meshes, with the voltage law taken round the combined outline while the current source supplies the relation between the two mesh currents.

A current source on the outer boundary of a mesh cannot be handled this way at all, which is why mesh analysis is not preferred for circuits holding one.

Where the two meshes also share resistors, the combined loop closes once the current source's relation replaces it. A $4\text{ A}$ source spanning one mesh, a $3\text{ A}$ source separating the two, and resistors of $1\ \Omega$, $2\ \Omega$, $3\ \Omega$, and $2\ \Omega$ beside a $4\text{ V}$ and a $5\text{ V}$ source give $I - I_2 = 3\text{ A}$ and $4 + 1I + 2(I - 4) + 3(I - 3 - 4) + 2(I - 3) - 5 = 0$, so $8I = 36$ and $I = 4.5\text{ A}$.

---

Flashcards for this section are as follows:

- overview ::@:: A current source shared by two meshes is handled by a supermesh spanning both: the voltage law is taken round the combined outline and the source relates the two mesh currents.
- why a supermesh: why does a shared current source block the mesh method? ::@:: The voltage across the source is not known from the mesh currents, so the voltage law cannot be written round either mesh alone.
- supermesh relation: what does a shared $3\text{ A}$ current source contribute between $I$ and $I_2$ once a supermesh is defined? ::@:: The relation between the two mesh currents, for example $I - I_2 = 3\text{ A}$ for a $3\text{ A}$ source.
- boundary source: what difficulty arises when a current source lies on the outer boundary of a mesh? ::@:: That mesh cannot be treated by a superloop, since the source has no second mesh to pair with, so the method becomes awkward and nodal analysis is preferred.
- worked supermesh: a $4\text{ A}$ source spans two meshes separated by a $3\text{ A}$ source, with $1\ \Omega$, $2\ \Omega$, $3\ \Omega$, and $2\ \Omega$ resistors beside a $4\text{ V}$ and a $5\text{ V}$ source; find the mesh current $I$. ::@:: The current source gives $I - I_2 = 3\text{ A}$, and the combined loop gives $4 + 1I + 2(I - 4) + 3(I - 3 - 4) + 2(I - 3) - 5 = 0$, so $8I = 36$ and $I = 4.5\text{ A}$.

## against nodal analysis

Both methods give the same answer, so the choice is a matter of algebra. Nodal analysis needs $n - 1$ equations for $n$ nodes; mesh analysis needs $b - n + 1$ for $b$ branches, which is never fewer and usually more.

A circuit holding current sources is awkward for mesh analysis besides, which is why node voltages are the usual unknowns there.

---

Flashcards for this section are as follows:

- overview ::@:: Nodal analysis needs $n - 1$ equations and mesh analysis $b - n + 1$, so mesh analysis never needs fewer equations than nodal analysis. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- equation counts: a circuit has $n = 4$ nodes and $b = 6$ branches; how many equations does each method need? ::@:: Nodal analysis needs $n - 1 = 3$ and mesh analysis needs $b - n + 1 = 3$; mesh analysis never needs fewer and here needs the same.
- which to prefer: for a circuit of $n$ nodes and $b$ branches, which method generally needs fewer equations? ::@:: Nodal analysis, since $n - 1 \le b - n + 1$.
