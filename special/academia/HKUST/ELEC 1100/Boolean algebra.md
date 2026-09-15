---
aliases:
  - Boolean algebra
  - ELEC 1100 Boolean algebra
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/Boolean_algebra
  - language/in/English
---

# Boolean algebra

Boolean algebra is the algebra of discrete logic values. In ELEC 1100 it is the bridge between binary sensor readings and concrete gate-level control circuits for the robot.

## binary variables and truth tables

A Boolean variable takes only two values, usually written as 0 and 1, LOW and HIGH, or false and true. A truth table lists the output for every possible combination of the input variables, so a design problem starts by stating what the system should do for each input case. For $n$ inputs there are $2^n$ rows in the complete truth table.

---

Flashcards for this section are as follows:

- Boolean values ::@:: Two values: 0/1, LOW/HIGH, or false/true. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- truth table ::@:: Lists the output for every possible input combination. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- truth-table rows for $n$ inputs ::@:: $2^n$ rows. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## basic gates and laws

The core gates are NOT, AND, and OR. NOT inverts a value, AND is 1 only when all required inputs are 1, and OR is 1 when at least one required input is 1. Their algebraic forms are $X'$, $X\cdot Y$, and $X+Y$. The standard simplification laws are:

- __exchange / commutative laws:__ $X+Y=Y+X$ and $X\cdot Y=Y\cdot X$
- __basic identity, complement, idempotence, and involution laws:__ $0+X=X$, $1+X=1$, $X'+X=1$, $X+X=X$, $0\cdot X=0$, $1\cdot X=X$, $X\cdot X=X$, $X\cdot X'=0$, and $(X')'=X$
- __associative laws:__ $(X+Y)+Z=X+(Y+Z)$ and $(X\cdot Y)\cdot Z=X\cdot(Y\cdot Z)$
- __distributive laws:__ $X\cdot(Y+Z)=X\cdot Y+X\cdot Z$ and $X+Y\cdot Z=(X+Y)(X+Z)$
- __DeMorgan's laws:__ $(X+Y)'=X'\cdot Y'$ and $(X\cdot Y)'=X'+Y'$

These laws simplify logic expressions before building them with gates.

---

Flashcards for this section are as follows:

- NOT ::@:: Inverts: 0 → 1, 1 → 0. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- AND ::@:: Outputs 1 only when all inputs are 1. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- OR ::@:: Outputs 1 when at least one input is 1. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- commutative laws ::@:: $X+Y=Y+X$ and $X\cdot Y=Y\cdot X$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- identity and complement laws ::@:: $0+X=X$, $1+X=1$, $X'+X=1$, $X\cdot X'=0$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- idempotence and involution ::@:: $X+X=X$, $X\cdot X=X$, $(X')'=X$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- DeMorgan's laws ::@:: Convert complemented AND to OR and complemented OR to AND, useful for simplification and gate substitution. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- check: ignore-next-line[header_style]: acronym -->
## NAND and NOR gates

NAND and NOR are the complemented versions of AND and OR. Their formulas are $(X\cdot Y)'$ and $(X+Y)'$. Each is a universal gate: an entire Boolean circuit can be built from only NAND or only NOR gates.

---

Flashcards for this section are as follows:

- NAND ::@:: $(X\cdot Y)'$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- NOR ::@:: $(X+Y)'$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- NAND/NOR universality ::@:: Each is a universal gate; a complete circuit can use only NAND or only NOR gates. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## historical development

George Boole (1815–1864) invented the subject. Claude Shannon's 1937 MIT thesis linked Boolean algebra to electronic telephone-switch circuits, establishing binary digital electronics as a practical design language.

---

Flashcards for this section are as follows:

- George Boole ::@:: Invented Boolean algebra. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- Boolean logic significance ::@:: One of the foundations of modern computer science. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- Claude Shannon ::@:: Connected Boolean algebra to electronic switching circuits in his 1937 MIT thesis, establishing binary digital electronics. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- check: ignore-next-line[header_style]: acronym -->
## XOR, XNOR, and simplification

XOR reports inequality: it is 1 when two inputs differ. XNOR reports equality: it is 1 when two inputs match. Their standard formulas are $X\oplus Y=X'Y+XY'$ and $X\odot Y=XY+X'Y'=(X\oplus Y)'$. Some behaviors are easier to express as relationships between inputs than as long sums of minterms. Simplification rewrites a logically equivalent expression with fewer gates or cleaner structure. For example, $(A'B'+A'B)'=(A'(B'+B))'=(A'\cdot1)'=(A')'=A$.

---

Flashcards for this section are as follows:

- XOR ::@:: Outputs 1 when inputs differ. $X\oplus Y=X'Y+XY'$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- XNOR ::@:: Outputs 1 when inputs match. $X\odot Y=XY+X'Y'=(X\oplus Y)'$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- XOR/XNOR usefulness ::@:: Express difference or equality directly, cleaner than expanding long expressions. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- simplification example ::@:: $(A'B'+A'B)'$ reduces to $A$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- simplification goal ::@:: Same logic behavior with fewer gates or cleaner structure. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## from robot specification to expression

In the robot, `L_Sensor` and `R_Sensor` define input rows; `L_DIR` and `R_DIR` define outputs. The workflow is: specification → truth table → Boolean expression → simplify → gate-level circuit. Skipping the truth table risks a neat-looking circuit that does not match the required behavior.

---

Flashcards for this section are as follows:

- Boolean workflow ::@:: Specification → truth table → Boolean expression → simplify → implement with gates. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- robot inputs/outputs ::@:: Inputs: `L_Sensor`, `R_Sensor`. Outputs: `L_DIR`, `R_DIR`. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- skipping the truth table ::@:: Risk: a neat-looking circuit that does not match the required behavior. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
