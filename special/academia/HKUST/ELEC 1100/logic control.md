---
aliases:
  - ELEC 1100 logic control
  - logic control
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/logic_control
  - language/in/English
---

# logic control

Logic control turns Boolean expressions into actual decision circuits. In ELEC 1100 it starts with the line-following truth table, then expands into adders and memory so students can see the difference between purely combinational behavior and stateful control.

## deriving motor-direction expressions

The line-following example shows how a truth table can be converted into compact expressions for motor-direction outputs. For the simple two-sensor controller, the simplified forms are $L_{\text{DIR}}=L'$ and $R_{\text{DIR}}=L+R'$. These expressions matter not because they are the only possible controller, but because they show the full design chain: specify behavior, build the truth table, derive expressions, simplify, and implement.

---

Flashcards for this section are as follows:

- logic-control derivation workflow ::@:: Specify the desired behavior, write the truth table, derive the Boolean expressions, simplify them, and then implement them with gates.
- ELEC 1100 line-following expression for $L_{\text{DIR}}$ and $R_{\text{DIR}}$ ::@:: $L_{\text{DIR}}=L'$ and $R_{\text{DIR}}=L+R'$.
- why the simple DIR expressions matter pedagogically ::@:: They demonstrate how a verbal control rule becomes a truth table, then a Boolean expression, then a real logic circuit.

## combinational control circuits

A combinational circuit's outputs depend only on the current input values. If the inputs change immediately, the output changes according to the circuit logic and nothing needs to be remembered from the past. The early robot-control design in ELEC 1100 is combinational because the direction signals are computed directly from the present sensor readings.

---

Flashcards for this section are as follows:

- combinational logic definition ::@:: A combinational circuit has outputs determined only by the current inputs, with no stored state from the past.
- why the early robot DIR controller is combinational ::@:: The motor-direction outputs are computed directly from the present line-sensor readings.
- main limitation of a purely combinational robot controller ::@:: It cannot distinguish different situations that produce the same current sensor pattern.

## half adder and full adder

The half adder and full adder are standard examples of combinational design. A half adder accepts only two bits $A$ and $B$, so it works only when there is __no incoming carry__ from a previous column. Its outputs are sum $S=A\oplus B$ and carry $C=AB$. A full adder adds three inputs $A$, $B$, and $C_{\text{in}}$ and therefore handles the normal multi-bit case. Its sum output is $S=(A\oplus B)\oplus C_{\text{in}}$, and its carry output is 1 whenever at least two of the three inputs are 1, so $C_{\text{out}}=AB+AC_{\text{in}}+BC_{\text{in}}=(A\oplus B)C_{\text{in}}+AB$. Structurally, one half adder first combines $A$ and $B$, a second half adder adds $C_{\text{in}}$ to that partial sum, and an OR gate combines the two carry terms. That is the standard mechanism when one stage must add both the current-column bits and an incoming carry.

---

Flashcards for this section are as follows:

- half adder limitation ::@:: A half adder works only when there is no incoming carry from a previous bit position.
- half adder with inputs $A$ and $B$: what are the sum and carry outputs? ::@:: A half adder outputs $S=A\oplus B$ and $C=AB$.
- full adder with inputs $A$, $B$, and $C_{\text{in}}$: what is the sum output? ::@:: $S=(A\oplus B)\oplus C_{\text{in}}$.
- full adder with inputs $A$, $B$, and $C_{\text{in}}$: what is the carry output? ::@:: $C_{\text{out}}=AB+AC_{\text{in}}+BC_{\text{in}}=(A\oplus B)C_{\text{in}}+AB$.
- when a full adder is needed instead of a half adder ::@:: A full adder is needed whenever the stage may receive a carry from the previous bit position.
- how a full adder is built from simpler blocks ::@:: It can be built from two half adders and one OR gate.

## cascading full adders and serial addition

Full adders can be chained to add multi-bit binary numbers. The usual connection is to feed each stage's $C_{\text{out}}$ into the next stage's $C_{\text{in}}$. Four chained stages make a 4-bit ripple-carry adder, and $n$ stages make an $n$-bit adder. This is the standard usage of the full adder: one stage handles one bit position, and the carry propagates from the least significant side toward the most significant side.

A serial binary adder trades hardware for time. Instead of having one full adder per bit position, it reuses one full-adder core together with a 1-bit memory element that stores the previous carry. A clock pulse then steps the machine forward one bit position at a time. The clock synchronizes when the next input bits are read and when the saved carry is updated, so serial addition is a sequential process rather than a purely combinational one.

---

Flashcards for this section are as follows:

- how full adders are chained in a multi-bit adder ::@:: Each stage's $C_{\text{out}}$ is connected to the next stage's $C_{\text{in}}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what four full adders in a row create ::@:: They create a 4-bit ripple-carry adder.
- why a serial binary adder needs memory ::@:: It must store the previous carry so one full-adder core can be reused for the next clocked bit position.
- why a serial binary adder needs a clock ::@:: The clock synchronizes when each new bit pair is processed and when the stored carry is updated.

## sequential logic and memory

Memory is what makes a circuit sequential. A sequential circuit depends on both the current inputs and a stored state from earlier inputs. The serial adder is sequential because the saved carry from one clock step becomes the next step's $C_{\text{in}}$. Likewise, the robot project uses state variables such as `countBumper` to distinguish the start line from later `00` sensor patterns. The main lesson is that repeated patterns need memory if their meaning changes over time.

---

Flashcards for this section are as follows:

- sequential logic definition ::@:: A sequential circuit depends on the current inputs together with stored state from earlier events.
- why the serial adder is sequential ::@:: It reuses one adder stage while storing intermediate state between clocked steps.
- why the robot project needs memory ::@:: The same current sensor pattern can represent different physical situations, so stored state such as `countBumper` is needed to tell them apart.
- combinational vs sequential summary ::@:: Combinational logic depends only on present inputs, while sequential logic depends on present inputs plus remembered state.
