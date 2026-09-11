---
aliases:
  - ELEC 1100 logic control
  - logic control
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/logic_control
  - language/in/English
---

# logic control

Logic control turns Boolean expressions into decision circuits. In ELEC 1100 it starts with the line-following truth table and expands into adders and memory, showing the difference between combinational behavior and stateful control.

## deriving motor-direction expressions

The line-following example shows how a truth table can be converted into compact expressions for motor-direction outputs. For the simple two-sensor controller, the simplified forms are $L_{\text{DIR}}=L'$ and $R_{\text{DIR}}=L+R'$. These expressions show the full design chain: specify behavior, build the truth table, derive expressions, simplify, and implement.

---

Flashcards for this section are as follows:

- derivation workflow ::@:: Specify behavior → truth table → Boolean expressions → simplify → implement with gates.
- ELEC 1100 line-following expressions ::@:: $L_{\text{DIR}}=L'$ and $R_{\text{DIR}}=L+R'$.
- pedagogical point ::@:: Shows how a verbal control rule becomes a truth table, then a Boolean expression, then a logic circuit.

## combinational control circuits

A combinational circuit's outputs depend only on current inputs; nothing is remembered from the past. The early robot-control design is combinational because direction signals are computed directly from present sensor readings.

---

Flashcards for this section are as follows:

- combinational logic ::@:: Outputs depend only on current inputs, with no stored state.
- why the early robot DIR controller is combinational ::@:: Direction outputs are computed directly from present sensor readings.
- combinational limitation ::@:: Cannot distinguish situations that produce the same sensor pattern.

## half adder and full adder

The half adder and full adder are standard examples of combinational design. A half adder accepts only two bits $A$ and $B$, so it works only when there is __no incoming carry__ from a previous column. Its outputs are sum $S=A\oplus B$ and carry $C=AB$. A full adder adds three inputs $A$, $B$, and $C_{\text{in}}$ and therefore handles the normal multi-bit case. Its sum output is $S=(A\oplus B)\oplus C_{\text{in}}$, and its carry output is 1 whenever at least two of the three inputs are 1, so $C_{\text{out}}=AB+AC_{\text{in}}+BC_{\text{in}}=(A\oplus B)C_{\text{in}}+AB$. Structurally, one half adder combines $A$ and $B$, a second adds $C_{\text{in}}$ to that partial sum, and an OR gate combines the two carry terms.

---

Flashcards for this section are as follows:

- half adder limitation ::@:: Works only when there is no incoming carry.
- half adder outputs ::@:: $S=A\oplus B$ and $C=AB$.
- full adder sum ::@:: $S=(A\oplus B)\oplus C_{\text{in}}$.
- full adder carry ::@:: $C_{\text{out}}=AB+AC_{\text{in}}+BC_{\text{in}}=(A\oplus B)C_{\text{in}}+AB$.
- when full adder is needed ::@:: Whenever the stage may receive a carry from the previous position.
- full adder from simpler blocks ::@:: Two half adders and one OR gate.

## cascading full adders and serial addition

Full adders can be chained to add multi-bit binary numbers. The usual connection is to feed each stage's $C_{\text{out}}$ into the next stage's $C_{\text{in}}$. Four chained stages make a 4-bit ripple-carry adder, and $n$ stages make an $n$-bit adder. One stage handles one bit position, and the carry propagates from the least significant side toward the most significant side.

A serial binary adder trades hardware for time. Instead of having one full adder per bit position, it reuses one full-adder core together with a 1-bit memory element that stores the previous carry. A clock pulse then steps the machine forward one bit position at a time. The clock synchronizes input reading and carry updates, making serial addition a sequential process.

---

Flashcards for this section are as follows:

- chaining full adders ::@:: Each stage's $C_{\text{out}}$ feeds the next stage's $C_{\text{in}}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- four chained adders ::@:: A 4-bit ripple-carry adder.
- serial adder memory ::@:: Stores the previous carry so one full-adder core can be reused for the next clocked bit position.
- serial adder clock ::@:: Synchronizes when each bit pair is processed and when the stored carry updates.

## sequential logic and memory

Memory is what makes a circuit sequential. A sequential circuit depends on both the current inputs and a stored state from earlier inputs. The serial adder is sequential because the saved carry from one clock step becomes the next step's $C_{\text{in}}$. Likewise, the robot project uses state variables such as `countBumper` to distinguish the start line from later `00` sensor patterns. Repeated patterns need memory if their meaning changes over time.

---

Flashcards for this section are as follows:

- sequential logic ::@:: Outputs depend on current inputs plus stored state from earlier events.
- why the serial adder is sequential ::@:: It reuses one adder stage while storing intermediate state between clocked steps.
- why the robot needs memory ::@:: The same sensor pattern can represent different situations, so stored state (e.g. `countBumper`) is needed.
- combinational vs sequential ::@:: Combinational: present inputs only. Sequential: present inputs plus remembered state.
