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

- Boolean variable values ::@:: A Boolean variable takes only two values, such as 0/1, LOW/HIGH, or false/true. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- truth table purpose ::@:: A truth table lists the output for every possible input combination, so it makes the intended logic behavior explicit. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- number of truth-table rows for $n$ inputs ::@:: A complete truth table has $2^n$ rows for $n$ Boolean inputs. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## basic gates and laws

The core gates are NOT, AND, and OR. NOT inverts a value, AND is 1 only when all required inputs are 1, and OR is 1 when at least one required input is 1. Their algebraic forms are $X'$, $X\cdot Y$, and $X+Y$. The standard simplification laws are listed explicitly below.

- __exchange / commutative laws:__ $X+Y=Y+X$ and $X\cdot Y=Y\cdot X$
- __basic identity, complement, idempotence, and involution laws:__ $0+X=X$, $1+X=1$, $X'+X=1$, $X+X=X$, $0\cdot X=0$, $1\cdot X=X$, $X\cdot X=X$, $X\cdot X'=0$, and $(X')'=X$
- __associative laws:__ $(X+Y)+Z=X+(Y+Z)$ and $(X\cdot Y)\cdot Z=X\cdot(Y\cdot Z)$
- __distributive laws:__ $X\cdot(Y+Z)=X\cdot Y+X\cdot Z$ and $X+Y\cdot Z=(X+Y)(X+Z)$
- __DeMorgan's laws:__ $(X+Y)'=X'\cdot Y'$ and $(X\cdot Y)'=X'+Y'$

These laws are not abstract decoration; they let you simplify a logic expression before building it with gates.

---

Flashcards for this section are as follows:

- NOT gate action ::@:: NOT inverts its input, changing 0 to 1 and 1 to 0. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- AND gate action ::@:: AND outputs 1 only when all required inputs are 1. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- OR gate action ::@:: OR outputs 1 when at least one required input is 1. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- exchange and commutative laws in Boolean algebra ::@:: $X+Y=Y+X$ and $X\cdot Y=Y\cdot X$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- identity and complement laws: what are four key formulas? ::@:: $0+X=X$, $1+X=1$, $X'+X=1$, and $X\cdot X'=0$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- idempotence and involution laws: what are the key formulas? ::@:: $X+X=X$, $X\cdot X=X$, and $(X')'=X$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- DeMorgan's laws in one sentence ::@:: DeMorgan's laws convert complemented AND forms into OR forms and complemented OR forms into AND forms, which is useful for simplification and gate substitution. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- check: ignore-next-line[header_style]: acronym -->
## NAND and NOR gates

NAND and NOR are the complemented versions of AND and OR. Their formulas are $(X\cdot Y)'$ and $(X+Y)'$. They are important because each is a universal gate family: in principle an entire Boolean circuit can be built using only NAND gates or only NOR gates.

---

Flashcards for this section are as follows:

- NAND formula ::@:: The NAND of $X$ and $Y$ is $(X\cdot Y)'$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- NOR formula ::@:: The NOR of $X$ and $Y$ is $(X+Y)'$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why NAND and NOR matter in circuit design ::@:: Each is a universal gate family, so a complete Boolean circuit can be implemented using only NAND gates or only NOR gates. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## historical development

Boolean algebra is not just notation. George Boole (1815–1864) invented the subject, and Boolean logic later became one of the foundations of modern computer science. Claude Shannon's 1937 MIT master's thesis linked Boolean algebra to electronic telephone-switch circuits and helped establish binary digital electronics as a practical engineering design language.

---

Flashcards for this section are as follows:

- George Boole and Boolean algebra ::@:: George Boole invented Boolean algebra. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why Boolean logic matters historically ::@:: Boolean logic became one of the foundations of modern computer science. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- Claude Shannon's contribution to Boolean algebra in engineering ::@:: Shannon connected Boolean algebra to electronic switching circuits in his 1937 MIT master's thesis, helping establish binary digital electronics as a practical design tool. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- check: ignore-next-line[header_style]: acronym -->
## XOR, XNOR, and simplification

XOR reports inequality: it is 1 when two inputs differ. XNOR reports equality: it is 1 when two inputs match. Their standard formulas are $X\oplus Y=X'Y+XY'$ and $X\odot Y=XY+X'Y'=(X\oplus Y)'$. These gates emphasise that some behaviors are easier to express as relationships between inputs than as long sums of minterms. Simplification means rewriting a logically equivalent expression with fewer gates or cleaner structure. For example, $(A'B'+A'B)'=(A'(B'+B))'=(A'\cdot1)'=(A')'=A$.

---

Flashcards for this section are as follows:

- XOR meaning ::@:: XOR outputs 1 when the two inputs are different. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- XNOR meaning ::@:: XNOR outputs 1 when the two inputs are equal. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- XOR formula ::@:: $X\oplus Y=X'Y+XY'$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- XNOR formula ::@:: $X\odot Y=XY+X'Y'=(X\oplus Y)'$. <!-- check: ignore-line[two_sided_calc_warning]: formula flashcard --> <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why XOR and XNOR are useful in ELEC 1100 ::@:: They express difference or equality directly, which can be cleaner than expanding a long Boolean expression. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- simplification example: what does $(A'B'+A'B)'$ reduce to? ::@:: It reduces to $A$. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- logic simplification goal ::@:: Simplification keeps the same logic behavior while reducing gate count or making the circuit easier to build and debug. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## from robot specification to expression

The robot application makes Boolean algebra concrete. Sensor readings such as `L_Sensor` and `R_Sensor` define the input rows, and target motor commands such as `L_DIR` and `R_DIR` define the outputs. The correct workflow is specification first, then truth table, then Boolean expression, then simplification, and only then the gate-level circuit. If you skip the truth table, it is easy to wire a circuit that is neat but wrong.

---

Flashcards for this section are as follows:

- robot-control Boolean workflow ::@:: Start from the verbal specification, build the truth table, derive the Boolean expression, simplify it, and then implement it with gates. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- ELEC 1100 Boolean inputs and outputs in the robot example ::@:: Inputs are sensor states such as `L_Sensor` and `R_Sensor`, and outputs are control signals such as `L_DIR` and `R_DIR`. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why skipping the truth table is risky ::@:: Without the truth table you may build a tidy-looking circuit that does not actually match the required behavior. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
