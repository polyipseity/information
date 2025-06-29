---
aliases:
  - Carmichael function
  - Carmichael functions
tags:
  - flashcard/active/general/eng/Carmichael_function
  - language/in/English
---

# Carmichael function

> {@{![Carmichael _λ_ function: _λ_\(_n_\) for 1 ≤ _n_ ≤ 1000 \(compared to Euler _φ_ function\)](../../archives/Wikimedia%20Commons/CarmichaelLambda.svg)}@}
>
> {@{Carmichael _λ_ function: _λ_\(_n_\) for 1 ≤ _n_ ≤ 1000 \(compared to Euler _φ_ function\)}@} <!--SR:!2025-07-30,149,301!2026-02-13,304,290-->

In {@{[number theory](number%20theory.md), a branch of [mathematics](mathematics.md)}@}, the {@{__Carmichael function__ _λ_\(_n_\)}@} of {@{a [positive integer](natural%20number.md) _n_ is the smallest positive integer _m_ such that $$a^{m}\equiv 1{\pmod {n} }$$ holds for every integer _a_ [coprime](coprime%20integers.md) to _n_}@}. In {@{algebraic terms}@}, _λ_\(_n_\) is {@{the [exponent](torsion%20group.md) of the [multiplicative group of integers modulo _n_](multiplicative%20group%20of%20integers%20modulo%20n.md)}@}. As {@{this is a [finite abelian group](abelian%20group.md#finite%20abelian%20groups)}@}, there must {@{exist an element whose [order](cyclic%20group.md#definition%20and%20notation) equals the exponent, _λ_\(_n_\)}@}. Such an element is {@{called a __primitive _λ_-root modulo _n_<!-- markdown separator -->__}@}. <!--SR:!2025-12-15,276,330!2025-12-30,289,341!2025-07-04,135,301!2025-10-22,232,330!2026-03-15,332,301!2025-10-28,237,330!2026-01-07,296,341!2026-01-02,292,341-->

The Carmichael function is named after {@{the American mathematician [Robert Carmichael](Robert%20Daniel%20Carmichael.md) who defined it in 1910}@}.<sup>[\[1\]](#^ref-1)</sup> It is also known as {@{__Carmichael's λ function__, the __reduced totient function__, and the __least universal exponent function__}@}. <!--SR:!2025-07-06,131,290!2025-09-22,203,321-->

{@{The order of the multiplicative group of integers modulo _n_}@} is {@{_φ_\(_n_\), where _φ_ is [Euler's totient function](Euler's%20totient%20function.md)}@}. Since {@{the order of an element of a finite group divides the order of the group}@}, {@{_λ_\(_n_\) divides _φ_\(_n_\)}@}. The following table compares the first 36 values of _λ_\(_n_\) \(sequence {@{[A002322](https://oeis.org/A002322)}@} in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)\) and _φ_\(_n_\) \(in __bold__ if they are different; the _n_<!-- markdown separator -->s such that they are different are listed in [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md): [A033949](https://oeis.org/A033949)\). <!--SR:!2025-09-19,203,321!2026-02-17,328,341!2026-01-04,294,341!2026-02-16,327,341!2025-10-20,143,201-->

| _n_            | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8     | 9 | 10 | 11 | 12    | 13 | 14 | 15    | 16    | 17 | 18 | 19 | 20    | 21     | 22 | 23 | 24    | 25 | 26 | 27 | 28     | 29 | 30    | 31 | 32     | 33     | 34 | 35     | 36     |
| -------------- | - | - | - | - | - | - | - | ----- | - | -- | -- | ----- | -- | -- | ----- | ----- | -- | -- | -- | ----- | ------ | -- | -- | ----- | -- | -- | -- | ------ | -- | ----- | -- | ------ | ------ | -- | ------ | ------ |
| ___λ_\(_n_\)__ | 1 | 1 | 2 | 2 | 4 | 2 | 6 | __2__ | 6 | 4  | 10 | __2__ | 12 | 6  | __4__ | __4__ | 16 | 6  | 18 | __4__ | __6__  | 10 | 22 | __2__ | 20 | 12 | 18 | __6__  | 28 | __4__ | 30 | __8__  | __10__ | 16 | __12__ | __6__  |
| ___φ_\(_n_\)__ | 1 | 1 | 2 | 2 | 4 | 2 | 6 | __4__ | 6 | 4  | 10 | __4__ | 12 | 6  | __8__ | __8__ | 16 | 6  | 18 | __8__ | __12__ | 10 | 22 | __8__ | 20 | 12 | 18 | __12__ | 28 | __8__ | 30 | __16__ | __20__ | 16 | __24__ | __12__ |

## numerical examples

- {@{_n_ = 5}@}. {@{The set of numbers less than and coprime to 5}@} is {@{<!-- flashcard separator -->{1,2,3,4}<!-- flashcard separator -->}@}. Hence {@{Euler's totient function has value _φ_\(5\) = 4}@} and {@{the value of Carmichael's function, _λ_\(5\), must be a divisor of 4}@}. {@{The divisor 1 does not satisfy the definition of Carmichael's function}@} since {@{$a^{1}\not \equiv 1{\pmod {5} }$ except for $a\equiv 1{\pmod {5} }$}@}. {@{Neither does 2}@} since {@{$2^{2}\equiv 3^{2}\equiv 4\not \equiv 1{\pmod {5} }$}@}. Hence {@{_λ_\(5\) = 4}@}. Indeed, {@{$1^{4}\equiv 2^{4}\equiv 3^{4}\equiv 4^{4}\equiv 1{\pmod {5} }$}@}. {@{Both 2 and 3}@} are {@{primitive _λ_-roots modulo 5 and also [primitive roots](primitive%20root%20modulo%20n.md) modulo 5}@}.
- {@{_n_ = 8}@}. {@{The set of numbers less than and coprime to 8}@} is {@{<!-- flashcard separator -->{1,3,5,7}<!-- flashcard separator -->}@}. Hence {@{_φ_\(8\) = 4 and _λ_\(8\) must be a divisor of 4}@}. In fact {@{_λ_\(8\) = 2}@} since {@{$1^{2}\equiv 3^{2}\equiv 5^{2}\equiv 7^{2}\equiv 1{\pmod {8} }$}@}. {@{The primitive _λ_-roots modulo 8}@} are {@{3, 5, and 7}@}. There are {@{no primitive roots modulo 8}@}. <!--SR:!2026-01-26,311,341!2026-01-11,300,341!2025-12-28,285,330!2025-09-23,204,321!2025-07-18,144,301!2025-10-26,235,330!2026-02-02,317,341!2025-11-13,251,330!2025-09-21,204,321!2025-11-12,250,330!2026-01-05,295,341!2026-02-18,329,341!2026-02-21,331,341!2025-11-02,241,330!2026-01-09,298,341!2025-11-16,253,330!2025-09-12,199,321!2026-02-14,326,341!2025-09-16,204,321!2025-09-26,207,321!2026-02-14,326,341!2026-08-10,414,301-->

## recurrence for _λ_\(_n_\)

{@{The Carmichael lambda function of a prime power}@} can be {@{expressed in terms of the Euler totient}@}. {@{Any number that is not 1 or a prime power}@} can be {@{written uniquely as the product of distinct prime powers}@}, in which case {@{_λ_ of the product is the [least common multiple](least%20common%20multiple.md) of the _λ_ of the prime power factors}@}. Specifically, _λ_\(_n_\) is given by {@{the recurrence $$\lambda (n)={\begin{cases}\varphi (n)&{\text{if } }n{\text{ is 1, 2, 4, or an odd prime power,} }\\{\tfrac {1}{2} }\varphi (n)&{\text{if } }n=2^{r},\ r\geq 3,\\\operatorname {lcm} {\Bigl (}\lambda (n_{1}),\lambda (n_{2}),\ldots ,\lambda (n_{k}){\Bigr )}&{\text{if } }n=n_{1}n_{2}\ldots n_{k}{\text{ where } }n_{1},n_{2},\ldots ,n_{k}{\text{ are powers of distinct primes.} }\end{cases} }$$}@} {@{Euler's totient for a prime power, that is, a number _p_<sup>_r_</sup> with _p_ prime and _r_ ≥ 1}@}, is given by {@{$$\varphi (p^{r}){=}p^{r-1}(p-1).$$}@} (annotation: Consider {@{integers $1 \le n \le p^r$ such that $\gcd(n, p) = 1$}@}. There are {@{$p^r$ integers originally, and $p^r / p = p^{r - 1}$ integers share the prime factor $p$ with $p^r$}@}, so the above follows.) <!--SR:!2026-02-01,316,341!2025-11-17,254,330!2025-09-17,204,321!2026-01-27,312,341!2026-06-10,398,310!2025-07-08,135,290!2026-05-18,369,301!2026-02-24,334,341!2025-07-27,164,321!2025-11-15,252,330-->

## Carmichael's theorems

Carmichael proved {@{two theorems that, together}@}, establish that if {@{_λ_\(_n_\) is considered as defined by the recurrence of the previous section}@}, then {@{it satisfies the property stated in the introduction, namely that it is the smallest positive integer _m_ such that $a^{m}\equiv 1{\pmod {n} }$ for all _a_ relatively prime to _n_}@}. <!--SR:!2026-02-02,317,341!2025-09-12,200,321!2025-07-02,133,301-->

> Theorem 1 ::@:: — If _a_ is relatively prime to _n_ then $a^{\lambda (n)}\equiv 1{\pmod {n} }$.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-11-20,255,330!2025-08-31,189,310-->

This implies that {@{the order of every element of the multiplicative group of integers modulo _n_ divides _λ_\(_n_\)}@}. Carmichael calls {@{an element _a_ for which $a^{\lambda (n)}$ is the least power of _a_ congruent to 1 \(mod _n_\)}@} {@{a _primitive λ-root modulo n_}@}.<sup>[\[3\]](#^ref-3)</sup> \(This is {@{not to be confused with a [primitive root modulo _n_](primitive%20root%20modulo%20n.md)}@}, which Carmichael sometimes refers to as {@{a primitive $\varphi$-root modulo _n_}@}.\) <!--SR:!2025-07-21,146,301!2025-07-23,148,301!2026-02-17,328,341!2025-08-03,168,310!2026-02-25,335,341-->

> Theorem 2 ::@:: — For every positive integer _n_ there exists a primitive _λ_-root modulo _n_. Moreover, if _g_ is such a root, then there are $\varphi (\lambda (n))$ primitive _λ_-roots that are congruent to powers of _g_.<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2025-07-29,148,301!2026-07-04,423,321-->

If {@{_g_ is one of the primitive _λ_-roots guaranteed by the theorem}@}, then {@{$g^{m}\equiv 1{\pmod {n} }$ has no positive integer solutions _m_ less than _λ_\(_n_\)}@}, showing that {@{there is no positive _m_ \< _λ_\(_n_\) such that $a^{m}\equiv 1{\pmod {n} }$ for all _a_ relatively prime to _n_}@}. <!--SR:!2025-11-09,247,330!2026-02-14,325,341!2026-04-12,345,301-->

{@{The second statement of Theorem 2}@} does not imply that {@{all primitive _λ_-roots modulo _n_ are congruent to powers of a single root _g_}@}.<sup>[\[5\]](#^ref-5)</sup> For example, if {@{_n_ = 15}@}, then _λ_\(_n_\) = 4 while $\varphi (n)=8$ and $\varphi (\lambda (n))=2$. There are {@{four primitive _λ_-roots modulo 15}@}, namely {@{2, 7, 8, and 13 as $1\equiv 2^{4}\equiv 8^{4}\equiv 7^{4}\equiv 13^{4}$}@}. The roots 2 and 8 are {@{congruent to powers of each other and the roots 7 and 13 are congruent to powers of each other}@}, but {@{neither 7 nor 13 is congruent to a power of 2 or 8 and vice versa}@}. {@{The other four elements of the multiplicative group modulo 15}@}, namely {@{1, 4 \(which satisfies $4\equiv 2^{2}\equiv 8^{2}\equiv 7^{2}\equiv 13^{2}$\), 11, and 14}@}, are {@{not primitive _λ_-roots modulo 15}@}. <!--SR:!2026-02-02,317,341!2025-07-11,138,290!2025-08-27,185,310!2026-02-20,331,341!2026-07-02,385,301!2025-10-19,213,321!2025-08-26,182,310!2025-09-17,205,321!2025-08-28,172,281!2025-09-11,199,321-->

For a contrasting example, if {@{_n_ = 9}@}, then $\lambda (n)=\varphi (n)=6$ and $\varphi (\lambda (n))=2$. There are {@{two primitive _λ_-roots modulo 9}@}, namely {@{2 and 5}@}, each of which is {@{congruent to the fifth power of the other}@}. They are also {@{both primitive $\varphi$-roots modulo 9}@}. <!--SR:!2025-09-18,205,321!2026-02-14,326,341!2025-09-14,201,321!2025-07-29,166,321!2025-09-20,201,321-->

## properties of the Carmichael function

In this section, {@{an [integer](integer.md) $n$ is divisible by a nonzero integer $m$}@} if {@{there exists an integer $k$ such that $n=km$}@}. This is written as {@{$$m\mid n.$$}@} <!--SR:!2026-02-15,326,341!2025-11-10,229,321!2026-01-28,313,341-->

### a consequence of minimality of _λ_\(_n_\)

Suppose {@{_a<sup>m</sup>_ ≡ 1 \(mod _n_\) for all numbers _a_ coprime with _n_}@}. Then {@{_λ_\(_n_\) \| _m_}@}. <!--SR:!2026-02-24,334,341!2026-02-25,335,341-->

__Proof:__ If {@{_m_ = _kλ_\(_n_\) + _r_ with 0 ≤ _r_ \< _λ_\(_n_\)}@}, then {@{$$a^{r}=1^{k}\cdot a^{r}\equiv \left(a^{\lambda (n)}\right)^{k}\cdot a^{r}=a^{k\lambda (n)+r}=a^{m}\equiv 1{\pmod {n} }$$ for all numbers _a_ coprime with _n_}@}. It follows that {@{_r_ = 0 since _r_ \< _λ_\(_n_\) and _λ_\(_n_\) is the minimal positive exponent for which the congruence holds for all _a_ coprime with _n_}@}. <!--SR:!2025-11-18,255,330!2026-02-13,325,341!2026-02-01,316,341-->

### _λ_\(_n_\) divides _φ_\(_n_\)

This follows from {@{elementary [group theory](group%20theory.md)}@}, because {@{the exponent of any [finite group](finite%20group.md) must divide the order of the group}@}. {@{_λ_\(_n_\) is the exponent of the multiplicative group of integers modulo _n_}@} while {@{_φ_\(_n_\) is the order of that group}@}. In particular, {@{the two must be equal in the cases where the multiplicative group is cyclic}@} due to {@{the existence of a [primitive root](primitive%20root%20modulo%20n.md), which is the case for odd prime powers}@}. <!--SR:!2025-09-04,193,310!2026-01-08,297,341!2026-02-17,303,301!2025-08-01,151,301!2025-09-07,192,310!2026-02-07,277,290-->

We can thus view Carmichael's theorem as {@{a sharpening of [Euler's theorem](Euler's%20theorem.md)}@}. <!--SR:!2025-10-23,233,330-->

### divisibility

(divisibility) ::@:: $$a\,|\,b\Rightarrow \lambda (a)\,|\,\lambda (b)$$ <!--SR:!2026-02-23,333,341!2025-10-25,234,330-->

__Proof.__

By definition, for {@{any integer $k$ with $\gcd(k,b)=1$ \(and thus also $\gcd(k,a)=1$\)}@}, we have that {@{$b\,|\,(k^{\lambda (b)}-1)$}@} , and therefore {@{$a\,|\,(k^{\lambda (b)}-1)$}@}. This establishes that {@{$k^{\lambda (b)}\equiv 1{\pmod {a} }$ for all _k_ relatively prime to _a_}@}. (annotation: This is {@{missing a step proving that the set of all integers $k$ satisfying $\gcd(k, b) = 1$ covers all equivalence classes modulo $a$ of integers co-prime to $a$}@}. To see this is the case, {@{assume $a, b \ge 1$ ($\lambda(n)$ is defined for positive integers $n$ only) and fix an arbitrary integer $1 \le r < a$ satisfying $\gcd(r, a) = 1$}@}. It is _not_ {@{necessary that $\gcd(r, b) = 1$, but we can prove (and construct) that there is some integer $m$ satisfying $\gcd(ma + r, b) = 1$}@}. Factorize {@{$b$ into its $n$ prime factors $p_1, \ldots, p_n$ ($p_i \ge 2$), ignoring their exponents}@}. It suffices {@{to check that none of the prime factors $p_i$ divide $ma + r$ for some integer $m$}@}. If {@{$p_i \mid a$, then $p_i \nmid (ma + r)$ for every $m$ since $p_i \nmid r$ by $\gcd(r, a) = 1$}@}. Otherwise, if {@{$p_i \nmid a$, then either $p_i \mid r$ or $p_i \nmid r$}@}. If {@{$p_i \mid r$, then $p_i \nmid (ma + r)$ for every $p_i \nmid m$. Otherwise, if $p_i \nmid r$, then $p_i \nmid (ma + r)$ for every $p_i \mid m$}@}. Then {@{$m = \prod_{\substack{i \in \set{1, \ldots, n} \\ p_i \nmid r } } p_i$ makes $\gcd(ma + r, b) = 1$}@}.) By {@{the consequence of minimality proved above}@}, we have {@{$\lambda (a)\,|\,\lambda (b)$}@}. <!--SR:!2026-02-13,325,341!2026-01-14,300,341!2026-02-13,325,341!2025-12-10,226,270!2025-08-15,164,310!2025-07-19,144,301!2026-02-21,336,352!2026-02-09,326,352!2026-01-24,314,352!2025-10-15,214,332!2026-02-10,327,352!2026-02-15,331,352!2026-06-03,385,312!2026-01-28,317,352!2026-01-23,313,352-->

### composition

For {@{all positive integers _a_ and _b_}@} it holds that <p> {@{$\lambda (\mathrm {lcm} (a,b))=\mathrm {lcm} (\lambda (a),\lambda (b))$}@}. <p> This is {@{an immediate consequence of the recurrence for the Carmichael function}@}. <!--SR:!2025-09-15,203,321!2026-02-13,325,341!2025-07-09,136,290-->

### exponential cycle length

If {@{$r_{\mathrm {max} }=\max _{i}\{r_{i}\}$ is the biggest exponent in the prime factorization $n=p_{1}^{r_{1} }p_{2}^{r_{2} }\cdots p_{k}^{r_{k} }$ of _n_}@}, then {@{for all _a_ \(including those not coprime to _n_\) and all _r_ ≥ _r_<sub>max</sub>, $$a^{r}\equiv a^{\lambda (n)+r}{\pmod {n} }.$$}@} In particular, {@{for [square-free](square-free%20integer.md) _n_ \( _r_<sub>max</sub> = 1\), for all _a_ we have $$a\equiv a^{\lambda (n)+1}{\pmod {n} }.$$}@} <!--SR:!2025-09-15,202,321!2025-07-27,146,301!2025-11-21,239,321-->

> [!tip] tips
>
> - proof ::@:: Let $n = p_1^{r_1} \cdots p_k^{r_k}$ and $r \ge r_{\mathrm{max} } = \max_i\{r_i\}$. <p> Write $a^r = q_1^{s_1} \cdots q_l^{s_l}$ as a product of prime powers. Note $s_i \ge r \ge r_{\mathrm{max} }$. Consider $a^{\lambda(n) + r} = q_1^{\lambda (n) + {s_1} } \cdots q_l^{\lambda(n) + s_l}$. Consider each prime power separately. <p> If $q_i$ is coprime to $n$ (i.e. $q_i \ne p_j$ for all $j$), then $$q_i^{\lambda(n) + s_i} \equiv q_i^{s_i} \pmod n \,.$$ <p> If $q_i$ is not coprime to $n$, then $q_i = p_j$ for exactly one $j$. Let $x \equiv q_i^{\lambda(n) + s_i} \equiv p_j^{\lambda(n) + s_i} \pmod n$. By the Chinese remainder theorem, this has the same unique solution as $$\begin{aligned} x & \equiv p_j^{\lambda (n) + s_i} \pmod {n / p_j^{r_j} } \\ x & \equiv p_j^{\lambda (n) + s_i} \pmod {p_j^{r_j} } \,. \end{aligned}$$ Since $\left(n / p_j^{r_j}\right) \mid n \implies \lambda\left(n / p_j^{r_j}\right) \mid \lambda(n)$ and $\gcd\left(n / p_j^{r_j}, p_j^{r_j}\right) = 1$, the first equation becomes $x \equiv p_j^{s_i} \pmod {n / p_j^{r_j} }$. Since $s_i \ge r_{\mathrm{max} } \ge r_j \implies p_j^{r_j} \mid p_j^{s_i}$, the second equation becomes $x \equiv 0 \pmod {p_j^{r_j} }$. Now we have $$\begin{aligned} x & \equiv p_j^{s_i} \equiv q_i^{s_i} \pmod {n / p_j^{r_j} } \\ x & \equiv 0 \pmod {p_j^{r_j} } \,. \end{aligned}$$ By the Chinese remainder theorem, we have the following equation having the same unique solution: $$q_i^{\lambda(n) + s_i} \equiv x \equiv q_i^{s_i} \pmod n \,.$$ <p> The above shows $q_i^{\lambda (n) + s_i} \equiv q_i^{s_i} \pmod n$ for all $q_i$, so their product $a^r$ has $a^{\lambda(n) + r} \equiv a^r \pmod n$. QED. <!--SR:!2025-07-22,147,301!2025-08-23,165,270-->

### average value

For {@{any _n_ ≥ 16}@}:<sup>[\[6\]](#^ref-6)</sup><sup>[\[7\]](#^ref-7)</sup> $${\frac {1}{n} }\sum _{i\leq n}\lambda (i)={\frac {n}{\ln n} }e^{B(1+o(1))\ln \ln n/(\ln \ln \ln n)}$$ \(called {@{Erdős approximation}@} in the following\) with the constant $$B:=e^{-\gamma }\prod _{p\in \mathbb {P} }\left({1-{\frac {1}{(p-1)^{2}(p+1)} } }\right)\approx 0.34537$$ and {@{_γ_ ≈ 0.57721, the [Euler–Mascheroni constant](Euler's%20constant.md)}@}. <!--SR:!2026-03-16,287,301!2025-07-10,137,290!2026-03-04,321,301-->

The following table gives some overview {@{over the first 2<sup>26</sup> – 1 = 67108863 values of the _λ_ function}@}, for {@{both, the exact average and its Erdős-approximation}@}. <!--SR:!2026-03-16,328,301!2026-02-14,326,341-->

Additionally given is some overview over {@{the more easily accessible "logarithm over logarithm" values}@} {@{LoL\(_n_\) := ⁠ln _λ_\(_n_\)/ln _n_⁠}@} with <!--SR:!2025-09-16,203,321!2026-02-24,334,341-->

- LoL\(_n_\) \> ⁠4/5⁠ ::@:: ⇔ _λ_\(_n_\) \> _n_<sup>⁠4/5⁠</sup>. <!--SR:!2026-02-01,316,341!2026-02-13,325,341-->

There, the table entry in row number 26 at column

- % LoL \> ⁠4/5⁠   → 60.49

indicates that 60.49% \(≈ 40000000\) of the integers 1 ≤ _n_ ≤ 67108863 have {@{_λ_\(_n_\) \> _n_<sup>⁠4/5⁠</sup>}@} meaning that the majority of the _λ_ values is {@{exponential in the length _l_<!-- markdown separator --> := log<sub>2</sub>\(_n_\) of the input _n_, namely $$\left(2^{\frac {4}{5} }\right)^{l}=2^{\frac {4l}{5} }=\left(2^{l}\right)^{\frac {4}{5} }=n^{\frac {4}{5} }.$$}@} <!--SR:!2026-02-01,316,341!2025-08-14,159,270-->

| _ν_ | _n_ = 2<sup>_ν_</sup> – 1 | sum <br/> $\sum _{i\leq n}\lambda (i)$ | average <br/> ${\tfrac {1}{n} }\sum _{i\leq n}\lambda (i)$ | Erdős average | Erdős /exact average | LoL average | % LoL \> ⁠4/5⁠ | % LoL \> ⁠7/8⁠ |
| ---:| -------------------------:| --------------------------------------:| ----------------------------------------------------------:| -------------:| --------------------:| -----------:| --------------:| --------------:|
| 5   | 31                        | 270                                    | 8.709677                                                   | 68.643        | 7.8813               | 0.678244    | 41.94          | 35.48          |
| 6   | 63                        | 964                                    | 15.301587                                                  | 61.414        | 4.0136               | 0.699891    | 38.10          | 30.16          |
| 7   | 127                       | 3574                                   | 28.141732                                                  | 86.605        | 3.0774               | 0.717291    | 38.58          | 27.56          |
| 8   | 255                       | 12994                                  | 50.956863                                                  | 138.190       | 2.7119               | 0.730331    | 38.82          | 23.53          |
| 9   | 511                       | 48032                                  | 93.996086                                                  | 233.149       | 2.4804               | 0.740498    | 40.90          | 25.05          |
| 10  | 1023                      | 178816                                 | 174.795699                                                 | 406.145       | 2.3235               | 0.748482    | 41.45          | 26.98          |
| 11  | 2047                      | 662952                                 | 323.865169                                                 | 722.526       | 2.2309               | 0.754886    | 42.84          | 27.70          |
| 12  | 4095                      | 2490948                                | 608.290110                                                 | 1304.810      | 2.1450               | 0.761027    | 43.74          | 28.11          |
| 13  | 8191                      | 9382764                                | 1145.496765                                                | 2383.263      | 2.0806               | 0.766571    | 44.33          | 28.60          |
| 14  | 16383                     | 35504586                               | 2167.160227                                                | 4392.129      | 2.0267               | 0.771695    | 46.10          | 29.52          |
| 15  | 32767                     | 134736824                              | 4111.967040                                                | 8153.054      | 1.9828               | 0.776437    | 47.21          | 29.15          |
| 16  | 65535                     | 513758796                              | 7839.456718                                                | 15225.43      | 1.9422               | 0.781064    | 49.13          | 28.17          |
| 17  | 131071                    | 1964413592                             | 14987.40066                                                | 28576.97      | 1.9067               | 0.785401    | 50.43          | 29.55          |
| 18  | 262143                    | 7529218208                             | 28721.79768                                                | 53869.76      | 1.8756               | 0.789561    | 51.17          | 30.67          |
| 19  | 524287                    | 28935644342                            | 55190.46694                                                | 101930.9      | 1.8469               | 0.793536    | 52.62          | 31.45          |
| 20  | 1048575                   | 111393101150                           | 106232.8409                                                | 193507.1      | 1.8215               | 0.797351    | 53.74          | 31.83          |
| 21  | 2097151                   | 429685077652                           | 204889.9090                                                | 368427.6      | 1.7982               | 0.801018    | 54.97          | 32.18          |
| 22  | 4194303                   | 1660388309120                          | 395867.5158                                                | 703289.4      | 1.7766               | 0.804543    | 56.24          | 33.65          |
| 23  | 8388607                   | 6425917227352                          | 766029.1187                                                | 1345633       | 1.7566               | 0.807936    | 57.19          | 34.32          |
| 24  | 16777215                  | 24906872655990                         | 1484565.386                                                | 2580070       | 1.7379               | 0.811204    | 58.49          | 34.43          |
| 25  | 33554431                  | 96666595865430                         | 2880889.140                                                | 4956372       | 1.7204               | 0.814351    | 59.52          | 35.76          |
| 26  | 67108863                  | 375619048086576                        | 5597160.066                                                | 9537863       | 1.7041               | 0.817384    | 60.49          | 36.73          |

### prevailing interval

For {@{all numbers _N_ and all but _o_\(_N_\)<sup>[\[8\]](#^ref-8)</sup> positive integers _n_ ≤ _N_ \(a "prevailing" majority\)}@}: {@{$$\lambda (n)={\frac {n}{(\ln n)^{\ln \ln \ln n+A+o(1)} } }$$}@} with {@{the constant<sup>[\[7\]](#^ref-7)</sup> $$A:=-1+\sum _{p\in \mathbb {P} }{\frac {\ln p}{(p-1)^{2} } }\approx 0.2269688$$}@} <!--SR:!2026-06-05,380,301!2025-09-14,77,170!2025-08-23,152,261-->

### lower bounds

For {@{any sufficiently large number _N_ and for any Δ ≥ \(ln ln _N_\)<sup>3</sup>}@}, there are {@{at most $$N\exp \left(-0.69(\Delta \ln \Delta )^{\frac {1}{3} }\right)$$ positive integers _n_ ≤ _N_}@} such that {@{_λ_\(_n_\) ≤ _ne_<sup>−Δ</sup>}@}.<sup>[\[9\]](#^ref-9)</sup> <!--SR:!2025-07-17,35,150!2025-10-09,119,201!2025-10-20,196,281-->

### minimal order

For {@{any sequence _n_<sub>1</sub> \< _n_<sub>2</sub> \< _n_<sub>3</sub> \< ⋯ of positive integers, any constant 0 \< _c_ \< ⁠1/ln 2⁠, and any sufficiently large _i_}@}:<sup>[\[10\]](#^ref-10)</sup><sup>[\[11\]](#^ref-11)</sup> {@{$$\lambda (n_{i})>\left(\ln n_{i}\right)^{c\ln \ln \ln n_{i} }.$$}@} <!--SR:!2025-07-12,125,261!2025-07-20,38,150-->

### small values

For {@{a constant _c_ and any sufficiently large positive _A_, there exists an integer _n_ \> _A_}@} such that<sup>[\[11\]](#^ref-11)</sup> {@{$$\lambda (n)<\left(\ln A\right)^{c\ln \ln \ln A}.$$}@} Moreover, _n_ is {@{of the form $$n=\prod _{\substack{q\in \mathbb {P} \\ (q-1)|m} }q$$ for some square-free integer _m_ \< \(ln _A_\)<sup>_c_ ln ln ln _A_</sup>}@}.<sup>[\[10\]](#^ref-10)</sup> <!--SR:!2026-12-20,551,321!2025-07-08,123,261!2025-07-04,120,261-->

### image of the function

The set of values of the Carmichael function has {@{counting function<sup>[\[12\]](#^ref-12)</sup> $${\frac {x}{(\ln x)^{\eta +o(1)} } },$$}@} where {@{$$\eta =1-{\frac {1+\ln \ln 2}{\ln 2} }\approx 0.08607$$}@} <!--SR:!2025-11-06,188,241!2025-07-18,27,130-->

## use in cryptography

The Carmichael function is {@{important in [cryptography](cryptography.md)}@} due to {@{its use in the [RSA encryption algorithm](RSA%20(cryptosystem).md)}@}. <!--SR:!2025-11-19,255,330!2025-10-21,231,330-->

## proof of Theorem 1

For {@{_n_ = _p_, a prime}@}, Theorem 1 is {@{equivalent to Fermat's little theorem: $$a^{p-1}\equiv 1{\pmod {p} }\qquad {\text{for all } }a{\text{ coprime to } }p.$$}@} <!--SR:!2026-02-02,317,341!2026-02-23,333,341-->

For {@{prime powers _p_<sup>_r_</sup>, _r_ <!-- \> -->≥ 1}@}, if {@{$$a^{p^{r-1}(p-1)}=1+hp^{r}$$ holds for some integer _h_}@}, then {@{raising both sides to the power _p_}@} gives {@{$$a^{p^{r}(p-1)}=1+h'p^{r+1}$$ for some other integer $h'$}@}. (annotation: This proves {@{the induction step $a^{p^{r - 1} (p - 1)} \equiv 1 \pmod{p^r} \implies a^{p^r (p - 1)} \equiv 1 \pmod{p^{r + 1} }$}@}. To see why, consider {@{$\left(1 + hp^{r}\right)^p$ and its expansion}@}. Each term in the expansion is generated by {@{choosing a term in each of the _p_ $1 + hp^r$ and multiplying the _p_ terms}@}. If the expansion term {@{chooses 2 or more $hp^r$, then said expansion term is divisible by $p^{r + 1}$}@}. If the expansion term {@{chooses exactly 1 $hp^r$, note that there are _p_ such terms in the entire expansion, so adding these _p_ terms together results in a term that is divisible by $p^{r + 1}$}@}. What remains is {@{the expansion term that chooses all 1}@}.) By induction it follows that {@{$a^{\varphi (p^{r})}\equiv 1{\pmod {p^{r} } }$ for all _a_ relatively prime to _p_ and hence to _p_<sup>_r_</sup>}@}. This establishes {@{the theorem for _n_ = 4 or any odd prime power}@}. (annotation: Note we have not {@{proven that $\lambda(n) = \varphi\left(p^r\right)$ is minimal}@}. Indeed, {@{$n = 2^r$ where $r \ge 3$ has $\lambda\left(2^r\right) = \frac 1 2 \varphi\left(2^r\right)$ instead}@}. But this is okay because {@{Theorem 1 merely requires $a^{\lambda(n)} \equiv 1 \pmod n$ and does not say $\lambda(n)$ is minimal}@}. The missing part is {@{implied by Theorem 2 as it states the existence of a primitive _λ_-root modulo _n_, which implies the minimality of $\lambda(n)$}@}.) <!--SR:!2026-05-19,370,301!2026-06-04,379,301!2026-01-10,299,341!2026-09-10,462,310!2026-07-23,392,301!2025-12-29,288,341!2026-02-18,329,341!2025-11-11,230,321!2025-11-07,246,330!2026-02-22,332,341!2026-06-19,363,290!2026-01-08,297,341!2025-11-05,244,330!2026-01-03,293,341!2026-01-31,315,341!2025-11-06,245,330-->

### sharpening the result for higher powers of two

For {@{_a_ coprime to \(powers of\) 2}@} we have {@{_a_ = 1 + 2<!-- markdown separator -->_h_<sub>2</sub> for some integer _h_<sub>2</sub>}@}. (annotation: The reason {@{we cannot do the same for higher powers of odd primes is that _a_ would have had _multiple_ possible forms, one for each positive integer less than _p_: 1 + _ph_<sub>2</sub>, ..., (_p_ − 1) + _ph_<sub>2</sub>}@}.) Then, <p> {@{$a^{2}=1+4h_{2}(h_{2}+1)=1+8{\binom {h_{2}+1}{2} }=:1+8h_{3}$}@}, <p> where $h_{3}$ is an integer. With _r_ = 3, this is written {@{$$a^{2^{r-2} }=1+2^{r}h_{r}.$$}@} {@{Squaring both sides}@} gives {@{$$a^{2^{r-1} }=\left(1+2^{r}h_{r}\right)^{2}=1+2^{r+1}\left(h_{r}+2^{r-1}h_{r}^{2}\right)=:1+2^{r+1}h_{r+1},$$}@} where $h_{r+1}$ is an integer. It {@{follows by induction}@} that {@{$$a^{2^{r-2} }=a^{ {\frac {1}{2} }\varphi (2^{r})}\equiv 1{\pmod {2^{r} } }$$ for all $r\geq 3$ and all _a_ coprime to $2^{r}$}@}.<sup>[\[13\]](#^ref-13)</sup> <!--SR:!2025-09-13,200,321!2026-02-19,330,341!2025-11-11,233,290!2025-07-20,145,301!2025-12-12,226,270!2026-03-08,325,301!2026-05-20,371,301!2026-08-16,452,321!2026-10-13,488,326-->

### integers with multiple prime factors

By {@{the [unique factorization theorem](fundamental%20theorem%20of%20arithmetic.md)}@}, {@{any _n_ \> 1 can be written in a unique way as $$n=p_{1}^{r_{1} }p_{2}^{r_{2} }\cdots p_{k}^{r_{k} }$$}@} where {@{_p_<sub>1</sub> \< _p_<sub>2</sub> \< ... \< _p<sub>k</sub>_ are primes and _r_<sub>1</sub>, _r_<sub>2</sub>, ..., _r<sub>k</sub>_ are positive integers}@}. The results for prime powers establish that, {@{for $1\leq j\leq k$, $$a^{\lambda \left(p_{j}^{r_{j} }\right)}\equiv 1{\pmod {p_{j}^{r_{j} } } }\qquad {\text{for all } }a{\text{ coprime to } }n{\text{ and hence to } }p_{i}^{r_{i} }.$$}@} From this it follows that {@{$$a^{\lambda (n)}\equiv 1{\pmod {p_{j}^{r_{j} } } }\qquad {\text{for all } }a{\text{ coprime to } }n,$$ where, as given by the recurrence, $$\lambda (n)=\operatorname {lcm} {\Bigl (}\lambda \left(p_{1}^{r_{1} }\right),\lambda \left(p_{2}^{r_{2} }\right),\ldots ,\lambda \left(p_{k}^{r_{k} }\right){\Bigr )}.$$}@} From {@{the [Chinese remainder theorem](chinese%20remainder%20theorem.md)}@} one concludes that {@{$$a^{\lambda (n)}\equiv 1{\pmod {n} }\qquad {\text{for all } }a{\text{ coprime to } }n.$$}@} <!--SR:!2025-09-24,205,321!2025-09-12,200,321!2026-01-06,295,341!2025-10-02,182,270!2025-07-07,134,290!2026-02-12,324,341!2025-12-05,268,330-->

## see also

- [Carmichael number](Carmichael%20number.md)

## notes

1. <a id="CITEREFCarmichael1910"></a> Carmichael, Robert Daniel \(1910\). ["Note on a new number theory function"](https://doi.org/10.1090%2FS0002-9904-1910-01892-9). _Bulletin of the American Mathematical Society_. __16__ \(5\): 232–238. [doi](digital%20object%20identifier.md):[10.1090/S0002-9904-1910-01892-9](https://doi.org/10.1090%2FS0002-9904-1910-01892-9). <a id="^ref-1"></a>^ref-1
2. Carmichael \(1914\) p.40 <a id="^ref-2"></a>^ref-2
3. Carmichael \(1914\) p.54 <a id="^ref-3"></a>^ref-3
4. Carmichael \(1914\) p.55 <a id="^ref-4"></a>^ref-4
5. Carmichael \(1914\) p.56 <a id="^ref-5"></a>^ref-5
6. Theorem 3 in Erdős \(1991\) <a id="^ref-6"></a>^ref-6
7. Sándor & Crstici \(2004\) p.194 <a id="^ref-7"></a>^ref-7
8. Theorem 2 in Erdős \(1991\) 3. Normal order. \(p.365\) <a id="^ref-8"></a>^ref-8
9. Theorem 5 in Friedlander \(2001\) <a id="^ref-9"></a>^ref-9
10. Theorem 1 in Erdős \(1991\) <a id="^ref-10"></a>^ref-10
11. Sándor & Crstici \(2004\) p.193 <a id="^ref-11"></a>^ref-11
12. <a id="CITEREFFordLucaPomerance2014"></a> Ford, Kevin; Luca, Florian; Pomerance, Carl \(27 August 2014\). "The image of Carmichael's _λ_-function". _Algebra & Number Theory_. __8__ \(8\): 2009–2026. [arXiv](ArXiv.md):[1408.6506](https://arxiv.org/abs/1408.6506). [doi](digital%20object%20identifier.md):[10.2140/ant.2014.8.2009](https://doi.org/10.2140%2Fant.2014.8.2009). [S2CID](Semantic%20Scholar.md#S2CID) [50397623](https://api.semanticscholar.org/CorpusID:50397623). <a id="^ref-12"></a>^ref-12
13. Carmichael \(1914\) pp.38–39 <a id="^ref-13"></a>^ref-13

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Carmichael_function) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

- <a id="CITEREFErdősPomeranceSchmutz1991"></a> [Erdős, Paul](Paul%20Erdős.md); [Pomerance, Carl](Carl%20Pomerance.md); Schmutz, Eric \(1991\). ["Carmichael's lambda function"](https://doi.org/10.4064%2Faa-58-4-363-385). _Acta Arithmetica_. __58__ \(4\): 363–385. [doi](digital%20object%20identifier.md):[10.4064/aa-58-4-363-385](https://doi.org/10.4064%2Faa-58-4-363-385). [ISSN](ISSN.md) [0065-1036](https://search.worldcat.org/issn/0065-1036). [MR](Mathematical%20Reviews.md) [1121092](https://mathscinet.ams.org/mathscinet-getitem?mr=1121092). [Zbl](ZbMATH%20Open.md) [0734.11047](https://zbmath.org/?format=complete&q=an:0734.11047).
- <a id="CITEREFFriedlanderPomeranceShparlinski2001"></a> [Friedlander, John B.](John%20Friedlander.md); Pomerance, Carl; Shparlinski, Igor E. \(2001\). ["Period of the power generator and small values of the Carmichael function"](https://doi.org/10.1090%2Fs0025-5718-00-01282-5). _Mathematics of Computation_. __70__ \(236\): 1591–1605, 1803–1806. [doi](digital%20object%20identifier.md):[10.1090/s0025-5718-00-01282-5](https://doi.org/10.1090%2Fs0025-5718-00-01282-5). [ISSN](ISSN.md) [0025-5718](https://search.worldcat.org/issn/0025-5718). [MR](Mathematical%20Reviews.md) [1836921](https://mathscinet.ams.org/mathscinet-getitem?mr=1836921). [Zbl](ZbMATH%20Open.md) [1029.11043](https://zbmath.org/?format=complete&q=an:1029.11043).
- <a id="CITEREFSándorCrstici2004"></a> Sándor, Jozsef; Crstici, Borislav \(2004\). _Handbook of number theory II_. Dordrecht: Kluwer Academic. pp. 32–36, 193–195. [ISBN](ISBN.md) [978-1-4020-2546-4](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4020-2546-4). [Zbl](ZbMATH%20Open.md) [1079.11001](https://zbmath.org/?format=complete&q=an:1079.11001).
- Carmichael, Robert D. \[1914\]. _[The Theory of Numbers](https://gutenberg.org/ebooks/13693)_ at [Project Gutenberg](Project%20Gutenberg.md)

| <!-- hide- [v](https://en.wikipedia.org/wiki/Template:Totient) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Totient) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3ATotient) <p>  <br/> --> Totient function                                                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [Euler's totient function](Euler's%20totient%20function.md) _φ_\(_n_\) <br/> - [Jordan's totient function](Jordan's%20totient%20function.md) _J<sub>k</sub>_\(_n_\) <br/> - __Carmichael function__ \(reduced totient function\) _λ_\(_n_\) <br/> - [Nontotient](nontotient.md) <br/> - [Noncototient](noncototient.md) <br/> - [Highly totient number](highly%20totient%20number.md) <br/> - [Highly cototient number](highly%20cototient%20number.md) <br/> - [Sparsely totient number](sparsely%20totient%20number.md) |

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Modular arithmetic](https://en.wikipedia.org/wiki/Category:Modular%20arithmetic)
> - [Functions and mappings](https://en.wikipedia.org/wiki/Category:Functions%20and%20mappings)
