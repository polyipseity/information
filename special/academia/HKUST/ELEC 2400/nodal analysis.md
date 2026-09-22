---
aliases:
  - ELEC 2400 nodal analysis
  - ELEC2400 nodal analysis
  - HKUST ELEC 2400 nodal analysis
  - HKUST ELEC2400 nodal analysis
  - nodal analysis
  - node-voltage analysis
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/nodal_analysis
  - language/in/English
---

# nodal analysis

Nodal analysis solves a circuit by taking the node voltages as the unknowns and writing one Kirchhoff current law equation per node. It replaces the guesswork of combining resistors with a fixed procedure that works on any circuit, and it produces simultaneous equations rather than a chain of simplifications. A circuit as ordinary as a car's rear-window defroster has too many interconnected branches for series-parallel reduction, which is what the method is for.

For a circuit of $N$ nodes the unknowns are the $N - 1$ node voltages other than ground, and each voltage source adds one unknown or removes one equation. It is the method inside circuit simulators.

---

Flashcards for this section are as follows:

- overview ::@:: Nodal analysis takes the node voltages as unknowns and writes a current law equation at each node, producing $N - 1$ simultaneous equations for a circuit of $N$ nodes. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## procedure

For a circuit with $N$ nodes the procedure runs in order: pick a ground node and assign unknown voltages $V_a, V_b, \dots$ to the other $N - 1$ nodes; assign a reference direction to every branch; handle the $K$ voltage sources; write the current law equation at every node and supernode; and collect $N - 1 + K$ equations together with the node-voltage differences the sources impose.

The final steps are a check and a solve: confirm that equations and unknowns match in number, solve the linear system, which is matrix inversion in practice, and only then compute branch currents from the node voltages if they are wanted.

Only the first step is a choice; everything after it is forced by the circuit.

A two-node circuit with a $2\text{ A}$ source entering node $V_a$, a $1\text{ A}$ source leaving node $V_b$, resistors of $3\ \Omega$ and $2\ \Omega$ about $V_a$, and $1\ \Omega$ about $V_b$ gives $2 = \frac{V_a}{3} + \frac{V_a - V_b}{2}$, that is $5V_a - 3V_b = 12$, and $\frac{V_a - V_b}{2} = \frac{V_b}{1} + 1$, that is $V_a - 3V_b = 2$. Subtracting the second from the first leaves $4V_a = 10$, so $V_a = \frac{5}{2}\text{ V}$ and $V_b = \frac{1}{6}\text{ V}$, with $I_1 = \frac{1}{6}\text{ A}$, $I_2 = \frac{7}{6}\text{ A}$, and $I_3 = \frac{5}{6}\text{ A}$.

---

Flashcards for this section are as follows:

- overview ::@:: The procedure is to ground one node, assign unknown voltages to the rest, write a current law equation per node, check that equations and unknowns agree, solve, then compute branch currents if needed.
- unknown count: how many unknown node voltages does a circuit of $N$ nodes have? ::@:: $N - 1$: one node is grounded at $0\text{ V}$ and every other node takes an unknown.
- order of work: at which point in the procedure are branch currents computed? ::@:: Last, and only if wanted: the current law is written in node voltages, and currents follow from them once the voltages are known.
- consistency check: why check the number of equations against the number of unknowns before solving? ::@:: A mismatch means a node or a source was skipped, and the linear system would be under- or over-determined.
- non-listed step: how much of the procedure is a matter of choice? ::@:: Only the choice of reference node; the remaining equations are dictated by the circuit.
- two-node solve: a circuit has a $2\text{ A}$ source entering node $V_a$, a $1\text{ A}$ source leaving node $V_b$, $3\ \Omega$ and $2\ \Omega$ resistors about $V_a$, and $1\ \Omega$ about $V_b$; write the two node equations. ::@:: $2 = \frac{V_a}{3} + \frac{V_a - V_b}{2}$, giving $5V_a - 3V_b = 12$, and $\frac{V_a - V_b}{2} = \frac{V_b}{1} + 1$, giving $V_a - 3V_b = 2$.
- two-node solution: the equations $5V_a - 3V_b = 12$ and $V_a - 3V_b = 2$ describe a two-node circuit; find the node voltages and the three branch currents. ::@:: Subtracting gives $4V_a = 10$, so $V_a = \frac{5}{2}\text{ V}$ and $V_b = \frac{1}{6}\text{ V}$, with $I_1 = \frac{1}{6}\text{ A}$, $I_2 = \frac{7}{6}\text{ A}$, and $I_3 = \frac{5}{6}\text{ A}$.

## reference node

The reference node is called ground and set to $0\text{ V}$. It is commonly the node of lowest voltage, which makes the remaining node voltages positive and the arithmetic easier.

The choice does not change the circuit's behaviour; it renumbers the other nodes, as choosing sea level renumbers heights.

---

Flashcards for this section are as follows:

- overview ::@:: One node is chosen as ground, set to $0\text{ V}$, and commonly taken as the node of lowest voltage so that the other node voltages come out positive. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- freedom of choice: does moving the ground node change the circuit? ::@:: No: it renumbers the node voltages, since each is measured from the new reference, leaving every voltage difference unchanged.

## voltage sources in the nodal method

A voltage source connected to ground is no trouble: the node on its far side has a known voltage, so it drops out of the unknowns and one equation disappears.

A voltage source floating between two unknown nodes is harder, because the current law cannot express the current through it in node voltages. Two remedies exist. The recommended one labels that current as a new unknown $I_x, I_y, \dots$, which adds one unknown and keeps the simple current law at each node; the alternative groups the two terminals into a single supernode.

A source tied to ground solves in one equation. A $2\text{ A}$ source injecting at a node that carries a $4\ \Omega$ resistor to ground and a $4\ \Omega$ resistor to a $4\text{ V}$ source gives $2 = \frac{V_a}{4} + \frac{V_a - 4}{4}$, so $2V_a - 4 = 8$, $V_a = 6\text{ V}$, and $I_1 = 1.5\text{ A}$ in the branch carrying the current.

---

Flashcards for this section are as follows:

- overview ::@:: A voltage source tied to ground fixes a node voltage and removes an unknown; a floating voltage source is handled either by labelling its current a new unknown or by forming a supernode.
- why the extra unknown: why can the current through a floating voltage source not be written from the node voltages? ::@:: The current depends on the source's internal behaviour rather than on the node voltages across the surrounding resistors, so it is introduced as a separate unknown.
- grounded source: a voltage source sits between ground and one other node; what does that do to the unknowns and the equations? ::@:: The node takes the source's voltage as a known quantity, so the unknowns fall by one and one equation is dropped.
- one-node solve: a $2\text{ A}$ source injects at node $V_a$, which carries a $4\ \Omega$ resistor to ground and a $4\ \Omega$ resistor to a $4\text{ V}$ source; write the current-law equation and solve. ::@:: $2 = \frac{V_a}{4} + \frac{V_a - 4}{4}$, so $2V_a - 4 = 8$, $V_a = 6\text{ V}$, and the branch current is $I_1 = 1.5\text{ A}$.

## supernode

A supernode is the region formed by grouping the two terminals of a voltage source into one node. The current law is applied to the whole region, summing the currents entering and leaving it, while the source supplies one equation, the difference between the two node voltages it joins.

In a circuit of a $6\text{ V}$ source, a $2\text{ k}\Omega$ resistor, a $12\text{ V}$ source, a second $2\text{ k}\Omega$ resistor, and a $-4\text{ V}$ source, with $1\text{ k}\Omega$ and $2\text{ k}\Omega$ resistors to ground, the current $I_x$ through the $12\text{ V}$ source cannot be written in terms of $V_a$ and $V_b$. Grouping the source's terminals gives $I_1 = I_2 + I_x = I_2 + I_o + I_3$ and hence $\frac{6 - V_a}{2\text{ k}} = \frac{V_a}{1\text{ k}} + \frac{V_a + 12}{2\text{ k}} + \frac{V_a + 12 - (-4)}{2\text{ k}}$, so $V_a = -\frac{22}{5}\text{ V}$ and $I_o = \frac{V_a + 12}{2\text{ k}} = 3.8\text{ mA}$.

---

Flashcards for this section are as follows:

- overview ::@:: A supernode is the region enclosing a voltage source's two terminals, treated as one node for the current law while the source itself supplies the relation between the two node voltages.
- why a supernode: what problem does grouping a voltage source's terminals solve? ::@:: The current through the floating source is unknown, so the current law is applied to the enclosing region instead, where every remaining current is a resistor current expressible in node voltages.
- supernode equation: what equation does the voltage source still contribute once its terminals form a supernode? ::@:: The difference between the two node voltages, fixed by the source's value.
- worked supernode: in the circuit with a $6\text{ V}$ source at node $V_a$ through $2\text{ k}\Omega$, a $12\text{ V}$ source to $V_b$, resistors $1\text{ k}\Omega$ and $2\text{ k}\Omega$ to ground, and a $-4\text{ V}$ source beyond $V_b$ through $2\text{ k}\Omega$, what is $V_a$ and what is $I_o$? ::@:: $\frac{6 - V_a}{2\text{ k}} = \frac{V_a}{1\text{ k}} + \frac{V_a + 12}{2\text{ k}} + \frac{V_a + 12 - (-4)}{2\text{ k}}$ gives $V_a = -\frac{22}{5}\text{ V}$ and $I_o = \frac{V_a + 12}{2\text{ k}\Omega} = 3.8\text{ mA}$.

## dependent sources

A dependent source adds no new difficulty, since the current law is still written in node voltages: the controlling quantity must be expressed in node voltages first, and the source's value then becomes part of an equation.

In the circuit of a $10\text{ V}$ source feeding a $2\ \Omega$ resistor that carries $I_1$ to node $V_a$, where a $3\text{ A}$ source injects, a $1\ \Omega$ resistor returns to ground, and a dependent source $2I_1$ sits in the returning branch, the current law at the node reads $I_1 + 3 = \frac{V_a - 2I_1}{1}$. Substituting $I_1 = \frac{10 - V_a}{2}$ gives $10 - V_a + 6 = 4V_a - 20$, so $V_a = 7.2\text{ V}$ and $I_1 = 1.4\text{ A}$.

---

Flashcards for this section are as follows:

- overview ::@:: A dependent source enters the node equations as an extra unknown that must be rewritten in node voltages, after which the system solves as before.
- controlling quantity first: why must the controlling quantity of a dependent source be written in node voltages before solving? ::@:: The controlling quantity is itself a function of the node voltages, so the equations hold more unknowns than they can determine until it is expressed that way.
- dependent source in a node equation: a $10\text{ V}$ source feeds a $2\ \Omega$ resistor carrying $I_1$ to node $V_a$, which also carries a $3\text{ A}$ source, a $1\ \Omega$ resistor, and a dependent source $2I_1$; write the current law and solve. ::@:: $I_1 + 3 = \frac{V_a - 2I_1}{1}$ with $I_1 = \frac{10 - V_a}{2}$ gives $10 - V_a + 6 = 4V_a - 20$, so $V_a = 7.2\text{ V}$ and $I_1 = 1.4\text{ A}$.

## counting the equations

With the current-variable remedy the count is $N - 1 + K$: one equation per node, one extra unknown per voltage source, and one equation per source expressing a node-voltage difference. With the supernode remedy it is $N - 1 - K$: each source merges two nodes and removes one equation, adding no unknown.

Either way the count must match the number of unknowns before the system is solved. The supernode route is shorter when a circuit holds many voltage sources.

---

Flashcards for this section are as follows:

- overview ::@:: The current-variable route yields $N - 1 + K$ equations for $N$ nodes and $K$ voltage sources, while the supernode route yields $N - 1 - K$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- equation count with current variables: a circuit has $N = 5$ nodes and $K = 2$ voltage sources; how many equations does the current-variable route give? ::@:: $N - 1 + K = 5 - 1 + 2 = 6$ equations, one unknown current added per source.
- equation count with supernodes: the same circuit of $N = 5$ nodes and $K = 2$ voltage sources; how many equations does the supernode route give? ::@:: $N - 1 - K = 5 - 1 - 2 = 2$: each source merges two nodes and removes an equation, adding no unknown.
- choosing between the routes: which route is shorter when a circuit holds many voltage sources? ::@:: The supernode route, which drops one equation per source instead of adding an unknown and an equation.

## nodal analysis in circuit simulation

SPICE, the Simulation Program with Integrated Circuit Emphasis, performs its simulations by nodal analysis. It was written in 1973 at the University of California, Berkeley by Laurence Nagel under Donald Pederson, and it computes node voltages, branch currents, and power for circuits of resistors, capacitors, inductors, operational amplifiers, diodes, and transistors.

Simulation lets an engineer study a circuit without building it. A commercial descendant, PSPICE, from Cadence Design Systems, is the variant used in laboratory work.

---

Flashcards for this section are as follows:

- overview ::@:: SPICE, the Simulation Program with Integrated Circuit Emphasis, simulates circuits by nodal analysis, computing node voltages, branch currents, and power without the circuit being built.
- acronym: what does SPICE stand for? ::@:: Simulation Program with Integrated Circuit Emphasis.
- origin: where, when, and by whom was SPICE developed? ::@:: In 1973 at the University of California, Berkeley by Laurence Nagel with his research advisor Donald Pederson.
- method inside SPICE: which analysis technique do SPICE simulations use? ::@:: Nodal analysis.
- commercial variant: which commercial descendant of SPICE is used in laboratory work? ::@:: PSPICE, from Cadence Design Systems.
