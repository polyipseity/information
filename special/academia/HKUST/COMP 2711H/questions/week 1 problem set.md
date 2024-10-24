---
aliases:
  - COMP 2711H week 1 problem set
  - COMP 2711H week 1 problem sets
  - COMP2711H week 1 problem set
  - COMP2711H week 1 problem sets
  - HKUST COMP 2711H week 1 problem set
  - HKUST COMP 2711H week 1 problem sets
  - HKUST COMP2711H week 1 problem set
  - HKUST COMP2711H week 1 problem sets
tags:
  - flashcard/active/special/academia/HKUST/COMP_2711H/questions/week_1_problem_set
  - language/in/English
---

# week 1 problem set

- HKUST COMP 2711H

## commutativity of addition and multiplication under the Peano axioms

For all natural numbers $a$ and $b$, prove that {{addition as defined in the (second-order formulation of) Peano axioms commutates, i.e. $$a + b = b + a$$. Then, given that addition associates (i.e. $(a + b) + c = a + (b + c)$) and commutates, prove that multiplication commutates, i.e. $$a \cdot b = b \cdot a$$}}. <!--SR:!2024-12-15,74,320-->

- strategy ::: Apply induction to prove commutativity for more specific cases. Then apply induction again to generalize the results. <!--SR:!2024-11-21,44,250!2024-10-30,36,300-->

1. definitions ::: For all natural numbers $a$ and $b$, $$\begin{aligned} a + 0 & = a && \text{definition 1} \\ a + S(b) & = S(a + b) && \text{definition 2} \\ a \cdot 0 & = 0 && \text{definition 3} \\ a \cdot S(b) & = a + a \cdot b && \text{definition 4} \end{aligned}$$. <!--SR:!2024-11-25,55,300!2024-12-16,75,320-->
2. commutativity of addition / lemma 1 (commutativity of definition 1) ::: Lemma 1 (commutativity of definition 1): $$0 + b = b$$ holds for all $b \in \mathbb N_0$. When $b = 0$, $0 + 0 = 0$ by definition 1. Assume the lemma holds for $b$. Consider $S(b)$: $$\begin{aligned} 0 + b & = b && \text{assumption} \\ S(0 + b) & = S(b) && S\text{ is a function} \\ 0 + S(b) & = S(b) && \text{definition 2} \end{aligned}$$. So the lemma holds for $S(a)$. By induction, the lemma is proved for all natural numbers. <!--SR:!2025-01-17,92,300!2024-11-08,39,280-->
3. commutativity of addition / lemma 2 (commutativity of definition 2) ::: Lemma 2 (commutativity of definition 2): $$S(a) + b = S(a + b)$$ holds for all $a, b \in \mathbb N_0$. Without loss of generality, fix $a$. When $b = 0$, $$\begin{aligned} S(a) + 0 & = S(a) && \text{definition 1} \\ & = S(a + 0) && \text{definition 1} \end{aligned}$$. So the lemma holds for $0$. Assume the lemma holds for $b$. Consider $S(b)$: $$\begin{aligned} S(a) + b & = S(a + b) && \text{assumption} \\ S(S(a) + b) & = S(S(a + b)) && S\text{ is a function} \\ S(a) + S(b) & = S(a + S(b)) && \text{definition 2} \end{aligned}$$. So the lemma holds for $S(b)$. By induction, the lemma is proved for all natural numbers. <!--SR:!2025-02-07,109,300!2024-12-13,72,320-->
4. commutativity of addition ::: Theorem: $$a + b = b + a$$ for all $a, b \in \mathbb N_0$. Without loss of generality, fix $a$. When $b = 0$, $$\begin{aligned} a + 0 & = a && \text{definition 1} \\ & = 0 + a && \text{lemma 1} \end{aligned}$$. So the theorem is proved for $0$. Assume the theorem is true for $b$. Consider $S(b)$: $$\begin{aligned} a + b & = b + a && \text{assumption} \\ S(a + b) & = S(b + a) && S\text{ is a function} \\ a + S(b) & = S(b) + a && \text{definition 2, lemma 2} \\  \end{aligned}$$. So the theorem is proved for $S(b)$. By induction, the theorem is proved for all natural numbers. <!--SR:!2024-12-12,71,320!2024-11-22,52,300-->
5. commutativity of multiplication / lemma 3 (commutativity of definition 3) ::: Lemma 3 (commutativity of definition 3): $$0 \cdot b = 0$$ for all $b \in \mathbb N_0$. When $b = 0$, $0 \cdot 0 = 0$ by definition 3. Assume the lemma is true for $b$. Consider $S(b)$: $$\begin{aligned} 0 \cdot S(b) & = 0 + 0 \cdot b && \text{definition 4} \\ & = 0 \cdot b && \text{lemma 1} \\ & = 0 && \text{assumption} \end{aligned}$$. So the lemma is true for $S(b)$. By induction, the lemma is true for all natural numbers. <!--SR:!2024-11-23,54,320!2025-01-23,98,300-->
6. commutativity of multiplication / lemma 4 (commutativity of definition 4) ::: Lemma 4 (commutativity of definition 4): $$S(a) \cdot b = b + a \cdot b$$ for all $a, b \in \mathbb N_0$. Without loss of generality, fix $a$. When $b = 0$, $$\begin{aligned} S(a) \cdot 0 & = 0 && \text{definition 3} \\ & = 0 + 0 && \text{definition 1} \\ & = 0 + a \cdot 0 && \text{definition 3} \end{aligned}$$. So the lemma is true for $0$. Assume the lemma is true for $b$. Consider $S(b)$: $$\begin{aligned} S(a) \cdot S(b) & = S(a) + S(a) \cdot b && \text{definition 4} \\ & = S(a) + (b + a \cdot b) && \text{assumption} \\ & = S(a) + b + a \cdot b && \text{addition associates} \\ & = a + S(b) + a \cdot b && \text{lemma 2, definition 2} \\  & = S(b) + a + a \cdot b && \text{addition commutates} \\ & = S(b) + a \cdot S(b) && \text{definition 4} \end{aligned}$$. So the lemma is true for $S(b)$. By induction, the lemma is true for all natural numbers. <!--SR:!2024-12-04,65,320!2025-02-18,117,300-->
7. commutativity of multiplication ::: Theorem: $$a \cdot b = b \cdot a$$ for all $a, b \in \mathbb N_0$. Without loss of generality, fix $a$. When $b = 0$, $$\begin{aligned} a \cdot 0 & = 0 && \text{definition 3} \\ & = 0 \cdot a && \text{lemma 3} \end{aligned}$$. So the theorem is true for $0$. Assume the theorem is true for $b$. Consider $S(b)$: $$\begin{aligned} a \cdot S(b) & = a + a \cdot b && \text{definition 4} \\ & = a + b \cdot a && \text{assumption} \\ & = S(b) \cdot a && \text{lemma 4} \end{aligned}$$. So the theorem is true for $S(b)$. By induction, the theorem is true for all natural numbers. Q.E.D. <!--SR:!2024-11-24,53,300!2024-12-10,71,320-->

## existence and uniqueness of quotient and remainder

Let $a, b \in \mathbb N_0$ and {{$b \ne 0$. Prove that there exists two natural numbers $q, r \in \mathbb N_0$ such that $$a = b \cdot q + r \qquad r < b$$. Then prove that $q, r$ are unique, i.e. there is only one possible pair of values $q, r$}}. (The associativity and commutativity of addition and multiplication are given. The distributive law is also given.) <!--SR:!2024-12-20,79,320-->

- strategy / existence ::: Use induction, as it is usually more suitable for proving existence. <!--SR:!2024-10-29,36,290!2024-12-10,70,320-->
- strategy / uniqueness ::: For uniqueness, prove by contradiction via the well-ordering principle. Assert the existence of a least natural number that admits two or more distinct pairs of quotient and remainder. Then reverse the process used in induction to prove the existence of a smaller natural number that admits two or more distinct pairs of quotient and remainder. <!--SR:!2025-02-13,113,300!2024-12-25,69,280-->

1. setup ::: Without loss of generality, fix $b \ne 0$. Theorem: $$a = b \cdot q + r \qquad \exists q,r \in \mathbb N_0, r < b$$ for all $a, b \in \mathbb N_0$. <!--SR:!2024-11-19,50,300!2024-11-20,51,300-->
2. existence / lemma 1 ($<$ to $\le$) ::: Lemma 1 ($<$ to $\le$): $$r < b \rightarrow S(r) \le b \qquad b \ne 0$$. Define $r < b \equiv (r \le b) \land \lnot(r = b)$. Then, $$\begin{aligned} r < b & \rightarrow (r \le b) \land \lnot(r = b) \\ & \rightarrow (\exists x \in \mathbb N_0; r + x = b) \land \lnot (r + 0 = b) \\ & \rightarrow \exists x \ge 1; r + x = b && x\text{ exist even if }x = 0\text{ is eliminated, since }b \ne 0 \\ & \rightarrow \exists y \in \mathbb N_0; r + S(y) = b && x := S(y) \\ & \rightarrow \exists y \in \mathbb N_0; S(r + y) = b \\ & \rightarrow \exists y \in \mathbb N_0; S(r) + y = b \\ & \rightarrow S(r) \le b \end{aligned}$$. Thus it is proved. <!--SR:!2025-02-11,112,290!2024-12-14,73,320-->
3. existence / base case ::: When $a = 0$, $$\begin{aligned} 0 & = 0 + 0 && \text{addition} \\ & = b \cdot 0 + 0 && \text{multiplication} \end{aligned}$$. Then $q = 0, r = 0$. Validate that $r = 0 \le 1 \le b$. So the theorem is proved for $a = 0$. <!--SR:!2024-11-04,41,300!2024-12-15,74,320-->
4. existence / induction ::: Assuming the theorem is true for $a$. Consider $S(a)$: $$\begin{aligned} a & = b \cdot q + r && \text{assumption} \\ S(a) & = S(b \cdot q + r) && S\text{ is a function} \\ & = b \cdot q + S(r) && \text{addition} \\ & = \begin{cases} b \cdot q + b & \text{if }S(r) = b \\ b \cdot q + S(r) & \text{if }S(r) < b \end{cases} && \text{lemma 1} \\ & = \begin{cases} b \cdot S(q) + 0 & \text{if }S(r) = b \\ b \cdot q + S(r) & \text{if }S(r) < b \end{cases} && \text{addition, multiplication} \end{aligned}$$. Then $(q', r') = \begin{cases} (S(q), 0) &\text{if }S(r) = b \\ (q, S(r)) & \text{if }S(r) < b \end{cases}$. Validate that $r' < b$ for both cases. So the theorem is proved for $S(a)$. By induction, $q, r$ exists for all natural numbers $a$. <!--SR:!2025-01-23,98,300!2025-01-10,80,280-->
5. uniqueness / setup ::: Without loss of generality, fix $b \ne 0$. Assume there is an _nonempty_ set of natural numbers $A$ admitting two or more different values of the pair $(q, r)$. Let $a$ be the least natural number of $A$ by the well-ordering principle. <!--SR:!2024-12-14,73,320!2024-12-02,63,320-->
6. uniqueness / conclusion ($a = 0$) ::: Either $a = 0$ or a successor of a natural number. If $a = 0$, assume $0 = b \cdot q'' + r''$ for any $q'', r'' \in \mathbb N_0$ (its existence is established above). Then, $$\begin{aligned} 0 = b \cdot q'' + r'' & \rightarrow (0 \ge b \cdot q'') \land (0 \ge r'') && \text{definition of inequality} \\ & \rightarrow (b \cdot q'' = 0) \land (r'' = 0) && \text{0 is the least element of }\mathbb N_0 \\ & \rightarrow (q'' + d \cdot q'' = 0) \land (r'' = 0) && b \ne 0, b := S(d) \\ & \rightarrow (q'' \le 0) \land (r'' = 0) && \text{definition of inequality} \\ & \rightarrow (q'' = 0) \land (r'' = 0) && \text{0 is the least element of }\mathbb N_0  \end{aligned}$$. So $(q'', r'')$ is constrained to be the unique pair $(0, 0)$. This proves $(q, r)$ is unique when $a = 0$. So $a \ne 0$ or otherwise $a \notin A$. <!--SR:!2024-11-09,45,300!2024-12-10,71,320-->
7. uniqueness / conclusion ($a \ne 0$) ::: As $a \ne 0$, $a$ is a successor of another natural number $c$: $a := S(c), c \in \mathbb N_0$. Note that $c \notin A$ or otherwise $a$ would be not the least element of $A$, so $c$ has an unique $(q, r)$ (its existence is established above). Also, the $(q, r)$ pairs that $a$ admits cannot be $(0, 0)$, otherwise $a = 0$ by "direct" calculation. Then we construct a function that maps $(q', r')$ that $a = S(c)$ admits to $(q, r)$ that $c$ admits. If $r' \ne 0$, then: $$\begin{aligned} a & = b \cdot q' + r' \\ S(c) & = b \cdot q' + S(r'') && r' \ne 0, r' := S(r'') \\ S(c) & = S(b \cdot q' + r '') && \text{addition} \\ c & = b \cdot q' + r'' && S\text{ is injective} \\ (q', r') & \mapsto (q', r'') \end{aligned}$$. If $r' = 0$, then: $$\begin{aligned} a & = b \cdot q' + 0 \\ S(c) & = b \cdot S(q'') && \text{addition}, (q', r') \ne (0, 0), q' := S(q'') \\ S(c) & = b \cdot q'' + b && \text{multiplication} \\ S(c) & = b \cdot q'' + S(b') && b \ne 0, b := S(b') \\ S(c) & = S(b \cdot q'' + b') && \text{addition} \\ c & = b \cdot q'' + b' && S\text{ is injective} \\ (q', 0) & \mapsto (q'', b') \end{aligned}$$. The resulting function $$(q', r') \mapsto \begin{cases} (q', r'') && \text{if }r' \ne 0 \\ (q'', b') && \text{if }r' = 0 \end{cases} \quad \text{or} \quad \begin{cases} \quad (q', S(r'')) \mapsto (q', r'') \\ \quad (S(q''), 0) \mapsto (q'', b') \end{cases}$$ is injective because $S$ is a function, so $S(a) \ne S(b) \rightarrow a \ne b$. Since $a = S(c)$ admits two or more different $(q', r')$, this injective function maps to the two or more different $(q, r)$ that $c$ admits. But this contradicts that $c$ admits one unique $(q, r)$. So our original assumption that there is an _nonempty_ set of natural numbers that admits different $(q, r)$ is wrong, and such a set must be empty. Q.E.D. <!--SR:!2024-11-23,46,250!2024-12-08,61,280-->

## co-primality of consecutive Fibonacci numbers

Prove that {{any two consecutive elements of the Fibonacci sequence are relatively prime. The Fibonacci sequence is defined recursively as $F_0 = 0, F_1 = 1, F_n = F_{n - 2} + F_{n - 1}$}}. <!--SR:!2024-12-05,66,320-->

- strategy ::: Since the Fibonacci sequence is recursively defined, it is likely best to use induction. Contradiction can be used to prove the conditions for induction. <!--SR:!2024-12-03,64,320!2024-11-28,59,320-->

1. base case ::: $F_0 = 0, F_1 = 1, F_2 = 0 + 1 = 1, F_3 = 1 + 1 = 2, F_4 = 1 + 2 = 3$. $F_0$ and $F_1$, $F_1$ and $F_2$, and $F_2$ and $F_3$ are co-prime (in a weird way) because their common divisor only contains $1$. $F_3$ and $F_4$ are co-prime in a much more normal way, and we will start our induction here. <!--SR:!2024-11-30,61,320!2024-12-13,72,320-->
2. induction ::: Assume $F_n \ge 2$ and $F_{n + 1} \ge 2$ are co-prime. Consider $F_{n + 2} = F_n + F_{n + 1}$. If $F_{n + 1}$ is not co-prime with $F_{n + 2}$ then there is a common factor $a \ge 2$ that $a \mid F_{n + 1}, F_{n + 2}$. Then we can re-express $F_{n + 1} = ab, F_{n + 2} = ac$, where $b, c \in \mathbb N_0$, and $b < c$ because $F_{n + 1} < F_{n + 2}$. Now consider $F_n$: $$\begin{aligned} F_n + F_{n + 1} & = F_{n + 2} \\ F_n & = F_{n + 2} - F_{n + 1} \\ & = ac - ab \\ & = a(c - b) \end{aligned}$$. Since $a \ge 2$ and $c - b > 0$, that means $a \mid F_n$ also. But this would mean $F_n$ and $F_{n + 1}$ have a common divisor of $a \ge 2$ and thus are not co-prime. This creates a contradiction, and thus $F_{n + 1}$ and $F_{n + 2}$ must be co-prime if $F_n$ and $F_{n + 1}$ are co-prime. By induction, consecutive elements of the Fibonacci sequence are relatively prime. <!--SR:!2024-12-12,71,320!2024-12-14,73,320-->

## irrationality of square roots of prime numbers

We know that $\sqrt 2$ is irrational from [above](#irrationality%20of%20the%20square%20root%20of%202). Prove that {{$\sqrt 3$ is irrational. Then prove that $\sqrt 5$ is irrational. Finally, prove that $\sqrt p$ is irrational for all prime numbers $p$}}. <!--SR:!2024-11-02,39,300-->

- strategy ::: Prove by contradiction via infinite descent. Some properties of prime numbers should be important in the proof. <!--SR:!2025-02-18,117,300!2024-12-20,79,320-->

1. assumption ::: The assumption is always that square roots of prime numbers are rational and thus can be written as $a / b$ for $a, b \in \mathbb N_0$. <!--SR:!2024-12-14,74,320!2024-11-26,57,310-->
2. irrationality of $\sqrt 3$ ::: $$\begin{aligned} \sqrt 3 = \frac a b \\ 3 & = \frac {a^2} {b^2} \\ 3b^2 & = a^2 \\ & \rightarrow 3 \mid a^2 \\ & \rightarrow 3 \mid a && \text{3 is prime} \\ a & := 3c && c \in \mathbb N_0 \\ \\ 3b^2 & = 9c^2 \\ b^2 & = 3c^2 \\ b & := 3d && \text{similar to above} \\ \\ \sqrt 3 & = \frac a b = \frac {3c} {3d} = \frac c d \end{aligned}$$. So given a integral ratio to exactly express $\sqrt 3$, we can always make a integral ratio with smaller natural numbers to express the same number. But this would create an infinite descent of natural numbers. By contradiction, $\sqrt 3$ is not rational, i.e. irrational. <!--SR:!2024-12-19,78,320!2024-12-13,72,320-->
3. irrationality of $\sqrt 5$ ::: $$\begin{aligned} \sqrt 5 = \frac a b \\ 5 & = \frac {a^2} {b^2} \\ 5b^2 & = a^2 \\ & \rightarrow 5 \mid a^2 \\ & \rightarrow 5 \mid a && \text{5 is prime} \\ a & := 5c && c \in \mathbb N_0 \\ \\ 5b^2 & = 25c^2 \\ b^2 & = 5c^2 \\ b & := 5d && \text{similar to above} \\ \\ \sqrt 5 & = \frac a b = \frac {5c} {5d} = \frac c d \end{aligned}$$. So given a integral ratio to exactly express $\sqrt 5$, we can always make a integral ratio with smaller natural numbers to express the same number. But this would create an infinite descent of natural numbers. By contradiction, $\sqrt 5$ is not rational, i.e. irrational. <!--SR:!2024-11-23,53,300!2024-12-15,74,320-->
4. irrationality of $\sqrt p$ ::: $$\begin{aligned} \sqrt p = \frac a b \\ p & = \frac {a^2} {b^2} \\ pb^2 & = a^2 \\ & \rightarrow p \mid a^2 \\ & \rightarrow p \mid a && p\text{ is prime} \\ a & := pc && c \in \mathbb N_0 \\ \\ pb^2 & = p^2c^2 \\ b^2 & = pc^2 \\ b & := pd && \text{similar to above} \\ \\ \sqrt p & = \frac a b = \frac {pc} {pd} = \frac c d \end{aligned}$$. So given a integral ratio to exactly express $\sqrt p$, we can always make a integral ratio with smaller natural numbers to express the same number. But this would create an infinite descent of natural numbers. By contradiction, $\sqrt p$ is not rational, i.e. irrational. <!--SR:!2024-11-03,39,300!2024-12-20,79,320-->

## irrationality of square roots of non-perfect squares

We know that $\sqrt p$ is irrational from [above](#irrationality%20of%20square%20roots%20of%20prime%20numbers). Prove a even stronger result: {{the square root of any natural number $n$, i.e. $\sqrt n$, is either a natural number or irrational}}. <!--SR:!2024-11-28,59,310-->

- strategy ::: Prove by contradiction. Assume the rational fraction is in its most simplest form, i.e. co-prime. <!--SR:!2024-12-21,65,280!2024-11-12,47,300-->

1. assumption ::: The assumption is that square roots of natural numbers are rational and thus can be written as $a / b$ for $a, b \in \mathbb N_0$. $a$ and $b$ are co-prime. <!--SR:!2024-12-08,69,320!2024-12-17,76,320-->
2. proof ::: $\sqrt n = a / b$ implies $n = a^2 / b^2$, which implies $nb^2 = a^2$. If $b$ has a prime factor, then $a$ must have have it by this relation. However, since $a$ and $b$ are co-prime, their $\gcd(a, b) = 1$. So $b$ must not have any prime factors at all, as the least prime is 2. The only way this is possible is if $b = 1$. Then $n = a^2$. A solution for $n$ only exists if $n$ is a perfect square, as $a$ is an integer. Otherwise, this is impossible, meaning $\sqrt n$ is irrational by contradiction. And in the other case where $n$ is a perfect square, $b = 1$, so $\sqrt n = a / 1 = a$, an integer. So $\sqrt n$ is either a natural number or irrational. <!--SR:!2024-12-01,62,320!2024-10-30,34,280-->

## fundamental theorem of arithmetic (existence)

We say a natural number $n$ is prime if $\ge 2$ and it is impossible to write $n = a \cdot b$ where $1 < a, b < n$. Prove that {{every natural number $n \ge 2$ can be written as a product of prime numbers}}. <!--SR:!2024-12-16,75,320-->

- strategy ::: It is easier to prove this using contradiction than using induction. <!--SR:!2024-12-25,68,300!2024-10-29,26,280-->

1. assumption ::: Assume there exists a nonempty set of natural number not less than 2 $A$ that cannot be written as a product of prime numbers. Then by the well-ordering principle, there exists a least natural number $n \ge 2$ that cannot be written as a product of prime numbers. <!--SR:!2025-01-10,81,280!2024-11-28,57,300-->
2. construction ::: $n \ge 2$ is either prime or composite. If $n$ is a prime, then it is a product of itself, a prime number. So $n$ cannot be prime and is composite. Then there exists two natural numbers $1 < a, b < n$ such that $n = a \cdot b$. $a, b$ are both smaller than $n$, so they must not belong to $A$, or otherwise $n$ would not be the least natural number that cannot be written as a product of prime numbers. So $a$ and $b$ can be written as a product of prime numbers. But then this implies $n$ CAN be written as a product of prime numbers, as a product of two numbers that can be written as a product of prime numbers. <!--SR:!2024-11-10,41,300!2024-11-24,55,300-->
3. conclusion ::: That $n$ CAN be written as a product of prime numbers contradicts that $n$ belongs to the set of natural numbers $A$ that CANNOT be written as a product of prime numbers. By contradiction, the set $A$ must be empty, so every natural number $n \ge 2$ can be written as a product of prime numbers. <!--SR:!2024-12-05,66,320!2024-10-26,33,300-->

## closed knight's tour

Consider an 8×8 chessboard with a knight at the top right corner. Is it {{possible for us to move the knight in accordance with chess rules such that it visits every square in the board exactly once and then returns to the top right corner? What if we have a 9×9 chessboard?}} <!--SR:!2024-11-21,52,290-->

Note that a knight can move {{two squares vertically and one square horizontally, or two squares horizontally and one square vertically}}. <!--SR:!2024-12-05,65,310-->

- strategy ::: For 8×8, one will need to guess that the answer is yes and construct such a closed path... So good luck! But for 9×9, there is a simple way. Draw the move pattern of a knight and notice the checker pattern of a chessboard. <!--SR:!2024-11-22,53,300!2024-12-08,68,310-->
- possibility of _closed_ knight's tours ::: Let there be a _m_ × _n_ board with _m_ ≤ _n_. A _closed_ knight's tour is always possible unless _m_ and _n_ are both odd; _m_ = 1, 2, or 4; or _m_ = 3 and _n_ = 4, 6, or 8. <!--SR:!2024-10-28,28,240!2024-12-20,61,240-->
- possibility of knight's tours ::: Let there be a _m_ × _n_ board with _m_ ≤ _n_. A knight's tour (possibly _open_) is always possible unless _m_ = 1 or 2; _m_ = 3 and _n_ = 3, 5, or 6; or _m_ = 4 and _n_ = 4. <!--SR:!2024-11-04,35,280!2024-11-28,37,210-->

1. 8×8 chessboard ::: It is possible. Prove by constructing such a closed path... <!--SR:!2024-12-14,73,320!2024-12-14,74,320-->
2. 9×9 chessboard ::: It is impossible. If such a closed path exists, then the knight needs to move exactly 81 times to visit every square and go back to the starting position. Now, notice the checker pattern of the chessboard. In a move, a knight must go from a square to a square of different color (black to white, white to black). Without loss of generality, assume the starting position is white. After moving exactly 81 times, the ending position must be black. But this implies the starting position and the ending position cannot be the same after 81 moves. So the closed path does not exist. <!--SR:!2024-11-24,53,300!2024-11-11,47,300-->

## product of natural numbers cannot be lesser than the natural numbers themselves

Let {{$a, b \in \mathbb N$ and $b \ne 0$. Prove that $a \cdot b \ge a$}}. <!--SR:!2024-11-24,55,310-->

- strategy ::: Prove by induction. Use the definition of $\ge$. <!--SR:!2024-11-07,43,300!2024-12-14,73,320-->

1. base case ::: Without loss of generality, fix $a \in \mathbb N$. When $b = 1$. then $$a \cdot b = a \cdot 1 = a \cdot S(0) = a + a \cdot 0 = a + 0 = a$$. Thus the theorem is proved when $b = 1$. <!--SR:!2025-02-11,112,300!2024-12-07,68,320-->
2. induction ::: Assume $a \cdot b \ge a$ for some $b \in \mathbb N_{\ne 0}$. Consider $S(b)$: $$\begin{aligned} a \cdot S(b) & = a + a \cdot b \\ & \ge a \cdot b && \text{definition of }\ge \\ & \ge a && \text{transitivity of }\ge \end{aligned}$$. Thus if the theorem is true for $b$, then it is also true for $S(b)$. By induction, the theorem is true for all $b \in \mathbb N_{\ne 0}$. <!--SR:!2024-12-12,71,320!2024-12-15,74,320-->

## pigeonhole principle: distance and equilateral triangle

We have {{an equilateral triangle of side length 2. Amir chooses five points inside this triangle. Prove that two of the points have a distance of at most 1}}. <!--SR:!2024-10-31,37,300-->

- strategy ::: Think of a way to make "pigeonholes" for the 5 points... <!--SR:!2024-11-13,48,300!2024-12-09,70,320-->
- generalization ::: This can be applied to other shapes: Any two points on a circle, including the boundary, have a distance of at most its diameter. <!--SR:!2024-11-24,53,300!2024-12-19,78,320-->

1. solution ::: Split the equilateral triangle into 4 equal equilateral triangles of side length 1. Then any two points in the same equilateral triangle of side length 1, including the boundary, have a distance of at most 1. Put 5 points into the large equilateral triangle. By the pigeonhole principle, there are at least one equilateral triangle of side length 1 with two points on it. Thus there are at least two points that have a distance of at most 1. <!--SR:!2025-01-23,96,290!2024-11-25,39,300-->

## pigeonhole principle: birthday

Prove that {{there are 3 students in COMP 2711H whose birthday is on the same day of the month}}. We currently have 64 students. <!--SR:!2024-12-08,69,320-->

- strategy ::: A trivial application of the pigeonhole principle. Of course, if Amir wants you to prove the slightly more generalized pigeonhole principle, use induction, which will not be shown here. <!--SR:!2024-12-05,66,320!2024-12-06,67,320-->

1. solution ::: There are at most 31 days in a month. By the pigeonhole principle, there is at least a day with $\lceil 64 / 31 \rceil = 3$ students whose birthdays are on that day (ignoring the month).  (If Amir wants you to prove the slightly more generalized pigeonhole principle, use induction, which will not be shown here.) <!--SR:!2024-11-01,36,280!2024-10-30,37,300-->
