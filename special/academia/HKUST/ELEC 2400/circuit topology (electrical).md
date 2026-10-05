---
aliases:
  - ELEC 2400 circuit topology (electrical)
  - ELEC2400 circuit topology (electrical)
  - HKUST ELEC 2400 circuit topology (electrical)
  - HKUST ELEC2400 circuit topology (electrical)
  - circuit topology
  - circuit topology (electrical)
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/circuit_topology_(electrical)
  - language/in/English
---

# circuit topology (electrical)

A circuit diagram is a two-dimensional picture of a circuit in standardized symbols. What it fixes is not the picture but which element terminals are joined, so two drawings that join the same terminals describe the same circuit, and every later argument about it, Kirchhoff's laws or an equivalence, is a statement about those joints.

The joints have names: node, branch, path, loop, and mesh. Counting them also predicts how many independent equations Kirchhoff's laws can supply.

---

Flashcards for this section are as follows:

- overview ::@:: A circuit diagram is a two-dimensional representation of a circuit in standardized symbols that fixes which element terminals are joined, and the joints it draws are the node, the branch, the path, the loop, and the mesh. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## circuit diagram

A circuit diagram is a graphical representation of a circuit, that is, of closed connections of circuit elements. The same circuit also exists as hardware, such as a printed circuit board; the diagram is the schematic used for analysis.

The straight stroke joining two elements is a wire and holds no element, so a run of wire between two joints counts as one node however many terminals tap onto it. Two wires that cross are joined only where a dot is drawn.

Each node carries a label, each element its voltage and current, and each source a source voltage and current of its own.

A diagram may be redrawn in any way, provided no existing connection is broken and no new one is made.

---

Flashcards for this section are as follows:

- overview ::@:: A circuit diagram is a graphical representation of a circuit: the closed connections of its elements, drawn with standardized symbols. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- schematic against hardware: a printed circuit board and a schematic circuit diagram of the same circuit; what is each? ::@:: The board is the physical hardware, and the schematic is the two-dimensional representation of its components and interconnections. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- wire run: a straight run of wire joins two joints and three more element terminals tap onto it along the way; how many nodes does the run form? ::@:: One: wire holds no element, so a wire joining a run counts as a single node. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- crossing without a dot: two wires cross in a diagram with no dot drawn at the crossing; are they connected? ::@:: No: a crossing is a connection only where a dot is drawn. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- redrawing a diagram: what two conditions must a redrawn circuit diagram preserve? ::@:: No existing connection is broken, and no new connection is made. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- diagram labels: which quantities are written on a circuit diagram? ::@:: A label on each node, the branch voltage and branch current of each element, and the source voltage and source current of each source. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## node

A node is an electrical joint connecting the terminals of two or more circuit elements, and every point of a wire run that carries no element between two joints belongs to the same node.

Because it is a joint of terminals, the current entering a node leaves it, and the wire segment itself contributes no voltage.

---

Flashcards for this section are as follows:

- overview ::@:: A node is an electrical joint connecting the terminals of two or more circuit elements. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- terminals per node: how many element terminals meet at a node? ::@:: Two or more; a single terminal alone is not a joint. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- wire inside a node: a wire segment lying between two joints carries no element; how does it bear on the node count? ::@:: It does not add a node: the whole wire run forms one node. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## branch

A branch consists of the two nodes between which a circuit element is inserted. Each element therefore occupies exactly one branch, so branches and elements are equally many.

A branch carries a branch voltage across it and a branch current through it, both drawn with reference directions chosen for the analysis.

---

Flashcards for this section are as follows:

- overview ::@:: A branch consists of two nodes between which a circuit element is inserted. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- branches against elements: a circuit of nine elements; how many branches does it have? ::@:: Nine: each element sits between exactly two nodes, so the two counts agree. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- quantities on a branch: which two quantities are associated with a branch, and how are they fixed? ::@:: The branch voltage across it and the branch current through it, both under reference directions chosen for the analysis. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## path

A path is a sequence of nodes from the starting node to the ending node. The nodes need not be distinct; the path is an ordered walk along branches.

The branch voltages may be summed term by term along a path, which is what makes the voltage law usable with a ground reference.

---

Flashcards for this section are as follows:

- overview ::@:: A path is a sequence of nodes proceeding from the starting node to the ending node. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- path and its nodes: must the nodes of a path all be different? ::@:: No: a path is an ordered walk, and only a loop imposes the no-repeat condition. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## loop and mesh

A loop is a closed path whose starting node is also its ending node and which passes no intermediate node twice. A mesh is a loop containing no other loop.

The distinction matters for counting: a two-mesh planar circuit has three loops, the two meshes and the loop around both, so meshes never outnumber loops. In the worked circuit of two parallel meshes that gives three loops and two meshes, while five elements joined in parallel give two nodes and five branches.

---

Flashcards for this section are as follows:

- overview ::@:: A loop is a closed path that returns to its starting node without passing an intermediate node more than once, and a mesh is a loop containing no other loop. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- loop against mesh: which condition turns a loop into a mesh? ::@:: It contains no other loop within it. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- counting meshes: a planar circuit drawn as two adjacent meshes; how many loops and how many meshes does it have? ::@:: Three loops: the two meshes plus the loop around both. Two meshes. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- counting nodes and branches: five elements joined in parallel between two rails; how many nodes and branches? ::@:: Two nodes and five branches, one branch per element. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- loop against path: both are sequences of nodes; which one imposes the return and the no-repeat condition? ::@:: The loop: its starting and ending nodes coincide and no intermediate node is passed twice. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
