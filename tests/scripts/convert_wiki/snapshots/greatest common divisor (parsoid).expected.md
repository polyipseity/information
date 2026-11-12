Largest integer that divides given integers

In [mathematics](mathematics.md), the __greatest common divisor__ \(__GCD__\), also known as __greatest common factor \(GCF\)__, of two or more [integers](integer.md), which are not all zero, is the largest positive integer that [divides](divides.md#definition) each of the integers. For two integers _x_, _y_, the greatest common divisor of _x_ and _y_ is denoted $\gcd (x,y)$. For example, the GCD of 8 and 12 is 4, that is, gcd\(8, 12\) = 4.<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup>

In the name "greatest common divisor", the adjective "greatest" may be replaced by "highest", and the word "divisor" may be replaced by "factor", so that other names include __highest common factor \(HCF\)__, etc.<sup>[\[3\]](#^ref-3)</sup><sup>[\[4\]](#^ref-4)</sup><sup>[\[5\]](#^ref-5)</sup><sup>[\[6\]](#^ref-6)</sup> Historically, other names for the same concept have included __greatest common measure__.<sup>[\[7\]](#^ref-7)</sup>

This notion can be extended to polynomials \(see _[Polynomial greatest common divisor](polynomial%20greatest%20common%20divisor.md)_\) and other [commutative rings](commutative%20ring.md) \(see _[§ In commutative rings](#in%20commutative%20rings)_ below\).

## overview

### definition

The _greatest common divisor_ \(GCD\) of [integers](integer.md) _a_ and _b_, at least one of which is nonzero, is the greatest [positive integer](positive%20integer.md) _d_ such that _d_ is a [divisor](divisor.md) of both _a_ and _b_; that is, there are integers _e_ and _f_ such that _a_ = _de_ and _b_ = _df_, and _d_ is the largest such integer. The GCD of _a_ and _b_ is generally denoted gcd\(_a_, _b_\).<sup>[\[8\]](#^ref-8)</sup>

When one of _a_ and _b_ is zero, the GCD is the absolute value of the nonzero integer: gcd\(_a_, 0\) = gcd\(0, _a_\) = \|_a_\|. This case is important as the terminating step of the [Euclidean algorithm](#Euclidean%20algorithm).

The above definition is unsuitable for defining gcd\(0, 0\), since there is no greatest integer _n_ such that 0 × _n_ = 0. However, zero is its own greatest divisor if _greatest_ is understood in the context of the divisibility relation, so gcd\(0, 0\) is commonly defined as 0. This preserves the usual identities for GCD, and in particular [Bézout's identity](Bézout's%20identity.md), namely that gcd\(_a_, _b_\) [generates](generating%20set%20of%20an%20ideal.md) the same [ideal](ideal%20(ring%20theory).md) as {_a_, _b_}.<sup>[\[9\]](#^ref-9)</sup><sup>[\[10\]](#^ref-10)</sup><sup>[\[11\]](#^ref-11)</sup> This convention is followed by many [computer algebra systems](computer%20algebra%20system.md).<sup>[\[12\]](#^ref-12)</sup> Nonetheless, some authors leave gcd\(0, 0\) undefined.<sup>[\[13\]](#^ref-13)</sup>

The GCD of _a_ and _b_ is their [greatest](greatest%20element.md) positive common divisor in the [preorder](preorder.md) relation of [divisibility](divisibility.md). This means that the common divisors of _a_ and _b_ are exactly the divisors of their GCD. This is commonly proved by using either [Euclid's lemma](Euclid's%20lemma.md), the [fundamental theorem of arithmetic](fundamental%20theorem%20of%20arithmetic.md), or the [Euclidean algorithm](Euclidean%20algorithm.md). This is the meaning of "greatest" that is used for the generalizations of the concept of GCD.

### example

The number 54 can be expressed as a product of two integers in several different ways:

$$54 \times 1 = 27 \times 2 = 18 \times 3 = 9 \times 6.$$

Thus the complete list of _divisors_ of 54 is 1, 2, 3, 6, 9, 18, 27, 54. Similarly, the divisors of 24 are 1, 2, 3, 4, 6, 8, 12, 24. The numbers that these two lists have _in common_ are the _common divisors_ of 54 and 24, that is,

$$1, 2, 3, 6.$$

Of these, the greatest is 6, so it is the _greatest common divisor_:

$$\gcd(54,24) = 6.$$

Computing all divisors of the two numbers in this way is usually not efficient, especially for large numbers that have many divisors. Much more efficient methods are described in _[§ Calculation](#calculation)_.

### coprime numbers

- Main article: [Coprime integers](coprime%20integers.md)

Two numbers are called relatively prime, or [coprime](coprime.md), if their greatest common divisor equals 1.<sup>[\[14\]](#^ref-14)</sup> For example, 9 and 28 are coprime.

### a geometric view

> !["Tall, slender rectangle divided into a grid of squares. The rectangle is two squares wide and five squares tall."](../../archives/Wikimedia%20Commons/24x60.svg)
>
> Ten 12×12 square tiles cover a 24×60 oblong: 12 is the GCD of 24 and 60.

For example, a 24-by-60 rectangular area can be divided into a grid of: 1-by-1 squares, 2-by-2 squares, 3-by-3 squares, 4-by-4 squares, 6-by-6 squares or 12-by-12 squares. Therefore, 12 is the greatest common divisor of 24 and 60. A 24-by-60 rectangular area can thus be divided into a grid of 12-by-12 squares, with two squares along one edge \(24/12 = 2\) and five squares along the other \(60/12 = 5\).

More generally, an _a_-by-_b_ rectangle can be covered with square tiles of side length _c_ only if _c_ is a common divisor of _a_ and _b_.

## applications

### reducing fractions

- Further information: [Irreducible fraction](irreducible%20fraction.md)

The greatest common divisor is useful for reducing [fractions](fraction.md) to the [lowest terms](irreducible%20fraction.md).<sup>[\[15\]](#^ref-15)</sup> For example, gcd\(42, 56\) = 14, therefore,

$$\frac{42}{56}=\frac{3 \cdot 14 }{ 4 \cdot 14}=\frac{3 }{ 4}.$$

### least common multiple

> ![Venn diagram of the factors of two positive integers _a_ and _b_ showing that _a_ × _b_ is the product of their lowest common multiple \(LCM\) and their greatest common divisor \(GCD\), by CMG Lee.](../../archives/Wikimedia%20Commons/Visual%20proof%20lcm%20gcd%20product.svg)
>
> Venn diagram of the factors of two positive integers _a_ and _b_ showing that _a_ × _b_ is the product of their least common multiple and their greatest common divisor

- Further information: [Least common multiple](least%20common%20multiple.md)

The least common multiple of two integers that are not both zero can be computed from their greatest common divisor, by using the relation

$$\operatorname{lcm}(a,b)=\frac{|a\cdot b|}{\operatorname{gcd}(a,b)}.$$

## calculation

### using prime factorizations

Greatest common divisors can be computed by determining the [prime factorizations](prime%20factorization.md) of the two numbers and comparing factors. For example, to compute gcd\(48, 180\), we find the prime factorizations 48 = 2<sup>4</sup> · 3<sup>1</sup> and 180 = 2<sup>2</sup> · 3<sup>2</sup> · 5<sup>1</sup>; the GCD is then 2<sup>min\(4,2\)</sup> · 3<sup>min\(1,2\)</sup> · 5<sup>min\(0,1\)</sup> = 2<sup>2</sup> · 3<sup>1</sup> · 5<sup>0</sup> = 12 The corresponding LCM is then 2<sup>max\(4,2\)</sup> · 3<sup>max\(1,2\)</sup> · 5<sup>max\(0,1\)</sup> = 2<sup>4</sup> · 3<sup>2</sup> · 5<sup>1</sup> = 720.

In practice, this method is only feasible for small numbers, as computing prime factorizations takes too long.

### euclid's algorithm

- Main article: [Euclidean algorithm](Euclidean%20algorithm.md)

The method introduced by [Euclid](Euclid.md) for computing greatest common divisors is based on the fact that, given two positive integers _a_ and _b_ such that _a_ \> _b_, the common divisors of _a_ and _b_ are the same as the common divisors of _a_ – _b_ and _b_.

So, Euclid's method for computing the greatest common divisor of two positive integers consists of replacing the larger number with the difference of the numbers, and repeating this until the two numbers are equal: that is their greatest common divisor.

For example, to compute gcd\(48,18\), one proceeds as follows:

$$\begin{aligned}\gcd(48,18)\quad&\to\quad \gcd(48-18, 18)= \gcd(30,18)\\ &\to \quad \gcd(30-18, 18)= \gcd(12,18)\\ &\to \quad \gcd(12,18-12)= \gcd(12,6)\\ &\to \quad \gcd(12-6,6)= \gcd(6,6).\end{aligned}$$

So gcd\(48, 18\) = 6.

This method can be very slow if one number is much larger than the other. So, the variant that follows is generally preferred.

### Euclidean algorithm

- Main article: [Euclidean algorithm](Euclidean%20algorithm.md)

> ![Animation showing an application of the Euclidean Algorithm to find the Great Common Divisor of 62 and 36 which is 2.](../../archives/Wikimedia%20Commons/The%20Great%20Common%20Divisor%20of%2062%20and%2036%20is%202.ogv)
>
> Animation showing an application of the Euclidean algorithm to find the greatest common divisor of 62 and 36, which is 2

A more efficient method is the _Euclidean algorithm_, a variant in which the difference of the two numbers _a_ and _b_ is replaced by the _remainder_ of the [Euclidean division](Euclidean%20division.md) \(also called _division with remainder_\) of _a_ by _b_.

Denoting this remainder as _a_ mod _b_, the algorithm replaces \(_a_, _b_\) with \(_b_, _a_ mod _b_\) repeatedly until the pair is \(_d_, 0\), where _d_ is the greatest common divisor.

For example, to compute gcd\(48,18\), the computation is as follows:

$$\begin{aligned}\gcd(48,18)\quad&\to\quad \gcd(18, 48\bmod 18)= \gcd(18, 12)\\ &\to \quad \gcd(12, 18\bmod 12)= \gcd(12,6)\\ &\to \quad \gcd(6,12\bmod 6)= \gcd(6,0).\end{aligned}$$

This again gives gcd\(48, 18\) = 6.

### Binary GCD algorithm

- Main article: [Binary GCD algorithm](Binary%20GCD%20algorithm.md)

The binary GCD algorithm is a variant of Euclid's algorithm that is specially adapted to the [binary representation](binary%20representation.md) of the numbers, which is used in most [computers](computers.md).

The binary GCD algorithm differs from Euclid's algorithm essentially by dividing by two every even number that is encountered during the computation. Its efficiency results from the fact that, in binary representation, testing parity consists of testing the right-most digit, and dividing by two consists of removing the right-most digit.

The method is as follows, starting with _a_ and _b_ that are the two positive integers whose GCD is sought.

1. If _a_ and _b_ are both even, then divide both by two until at least one of them becomes odd; let _d_ be the number of these paired divisions.
2. If _a_ is even, then divide it by two until it becomes odd.
3. If _b_ is even, then divide it by two until it becomes odd.Now, _a_ and _b_ are both odd and will remain odd until the end of the computation <p>
4. While _a_ ≠ _b_ do
    - If _a_ \> _b_, then replace _a_ with _a_ – _b_ and divide the result by two until _a_ becomes odd \(as _a_ and _b_ are both odd, there is, at least, one division by 2\).
    - If _a_ \< _b_, then replace _b_ with _b_ – _a_ and divide the result by two until _b_ becomes odd.

5. Now, _a_ = _b_, and the greatest common divisor is $2^d a$.

Step 1 determines _d_ as the highest power of 2 that divides _a_ and _b_, and thus their greatest common divisor. None of the steps changes the set of the odd common divisors of _a_ and _b_. This shows that when the algorithm stops, the result is correct. The algorithm stops eventually, since each steps divides at least one of the operands by at least 2. Moreover, the number of divisions by 2 and thus the number of subtractions is at most the total number of digits.

Example: \(_a_, _b_, _d_\) = \(48, 18, 0\) → \(24, 9, 1\) → \(12, 9, 1\) → \(6, 9, 1\) → \(3, 9, 1\) → \(3, 3, 1\) ; the original GCD is thus the product 6 of 2<sup>_d_</sup> = 2<sup>1</sup> and _a_ = _b_ = 3.

The binary GCD algorithm is particularly easy to implement and particularly efficient on binary computers. Its [computational complexity](computational%20complexity.md) is

$$O((\log a + \log b)^2).$$

The square in this complexity comes from the fact that division by 2 and subtraction take a time that is proportional to the number of [bits](bit.md) of the input.

The computational complexity is usually given in terms of the length _n_ of the input. Here, this length is _n_ = log _a_ + log _b_, and the complexity is thus <p> &nbsp;&nbsp;&nbsp;&nbsp; $$O(n^2)$$ . <p> ### Lehmer's GCD algorithm

- Main article: [Lehmer's GCD algorithm](Lehmer's%20GCD%20algorithm.md)

Lehmer's algorithm is based on the observation that the initial quotients produced by Euclid's algorithm can be determined based on only the first few digits; this is useful for numbers that are larger than a [computer word](word%20(computer%20architecture).md). In essence, one extracts initial digits, typically forming one or two computer words, and runs Euclid's algorithms on these smaller numbers, as long as it is guaranteed that the quotients are the same with those that would be obtained with the original numbers. The quotients are collected into a small 2-by-2 transformation matrix \(a matrix of single-word integers\) to reduce the original numbers. This process is repeated until numbers are small enough that the binary algorithm \(see below\) is more efficient.

This algorithm improves speed, because it reduces the number of operations on very large numbers, and can use hardware arithmetic for most operations. In fact, most of the quotients are very small, so a fair number of steps of the Euclidean algorithm can be collected in a 2-by-2 matrix of single-word integers. When Lehmer's algorithm encounters a quotient that is too large, it must fall back to one iteration of Euclidean algorithm, with a [Euclidean division](Euclidean%20division.md) of large numbers.

### other methods

> ![gcd \(1,X\) = Y \[Greatest common divisor of 1 and X = Y\]. Hatching at bottom indicates ellipses \(the dots go on infinitely\). [\[1\]](http://mathworld.wolfram.com/images/eps-gif/GreatestCommonDivisor_1000.gif)](../../archives/Wikimedia%20Commons/Greatest%20common%20divisor.png)
>
> [Thomae's function](thomae's%20function.md)

If _a_ and _b_ are both nonzero, the greatest common divisor of _a_ and _b_ can be computed by using [least common multiple](least%20common%20multiple.md) \(LCM\) of _a_ and _b_: <p> &nbsp;&nbsp;&nbsp;&nbsp; $$\gcd(a,b)=\frac{|a\cdot b|}{\operatorname{lcm}(a,b)}$$ , <p> but more commonly the LCM is computed from the GCD.

Using [Thomae's function](thomae's%20function.md) _f_,

$$\gcd(a,b) = a f\left(\frac b a\right),$$

which generalizes to _a_ and _b_ [rational numbers](rational%20number.md) or [commensurable](commensurability%20(mathematics).md) real numbers.

Keith Slavin has shown that for odd _a_ ≥ 1:

$$\gcd(a,b)=\log_2\prod_{k=0}^{a-1} (1+e^{-2i\pi k b/a})$$

which is a function that can be evaluated for complex _b_.<sup>[\[16\]](#^ref-16)</sup> Wolfgang Schramm has shown that

$$\gcd(a,b)=\sum\limits_{k=1}^a \exp (2\pi ikb/a) \cdot \sum\limits_{d\left| a\right.} \frac{c_d (k)}{d}$$

is an [entire function](entire%20function.md) in the variable _b_ for all positive integers _a_ where _c_<sub>_d_</sub>\(_k_\) is [Ramanujan's sum](ramanujan's%20sum.md).<sup>[\[17\]](#^ref-17)</sup>

### complexity

The [computational complexity](computational%20complexity.md) of the computation of greatest common divisors has been widely studied.<sup>[\[18\]](#^ref-18)</sup> If one uses the [Euclidean algorithm](Euclidean%20algorithm.md) and the elementary algorithms for multiplication and division, the computation of the greatest common divisor of two integers of at most _n_ [bits](bit.md) is _O_\(_n_<sup>2</sup>\).<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> This means that the computation of greatest common divisor has, up to a constant factor, the same complexity as the multiplication.

However, if a fast [multiplication algorithm](multiplication%20algorithm.md) is used, one may modify the Euclidean algorithm for improving the complexity, but the computation of a greatest common divisor becomes slower than the multiplication. More precisely, if the multiplication of two integers of _n_ bits takes a time of _T_\(_n_\), then the fastest known algorithm for greatest common divisor has a complexity _O_\(_T_\(_n_\) log _n_\). This implies that the fastest known algorithm has a complexity of _O_\(_n_ \(log _n_\)<sup>2</sup>\).

Previous complexities are valid for the usual [models of computation](models%20of%20computation.md), specifically [multitape Turing machines](Multitape%20Turing%20machine.md) and [random-access machines](random-access%20machine.md).

The computation of the greatest common divisors belongs thus to the class of problems solvable in [quasilinear time](quasilinear%20time.md#quasilinear%20time). _A fortiori_, the corresponding [decision problem](decision%20problem.md) belongs to the class [P](P%20(complexity).md) of problems solvable in polynomial time. The GCD problem is not known to be in [NC](NC%20(complexity).md), and so there is no known way to [parallelize](parallel%20algorithm.md) it efficiently; nor is it known to be [P-complete](p-complete.md), which would imply that it is unlikely to be possible to efficiently parallelize GCD computation. Shallcross et al. showed that a related problem \(EUGCD, determining the remainder sequence arising during the Euclidean algorithm\) is NC-equivalent to the problem of [integer linear programming](integer%20linear%20programming.md) with two variables; if either problem is in __NC__ or is __P-complete__, the other is as well.<sup>[\[19\]](#^ref-19)</sup> Since __NC__ contains [NL](NL%20(complexity).md), it is also unknown whether a space-efficient algorithm for computing the GCD exists, even for nondeterministic Turing machines.

Although the problem is not known to be in __NC__, parallel algorithms [asymptotically faster](asymptotically%20faster%20algorithm.md) than the Euclidean algorithm exist; the fastest known deterministic algorithm is by [Chor](Benny%20Chor.md) and [Goldreich](Oded%20Goldreich.md), which \(in the [CRCW-PRAM](CRCW-PRAM.md) model\) can solve the problem in _O_\(_n_<!-- markdown separator -->/log _n_\) time with _n_<sup>1+<!-- markdown separator -->_ε_</sup> processors.<sup>[\[20\]](#^ref-20)</sup> [Randomized algorithms](randomized%20algorithm.md) can solve the problem in _O_\(\(log _n_\)<sup>2</sup>\) time on $O\left(e^{\sqrt{n \log n} }\right)$ processors \(this is [superpolynomial](superpolynomial.md#superpolynomial%20time)\).<sup>[\[21\]](#^ref-21)</sup>

## properties

- For every positive integer _a_, gcd\(_a_, _a_\) = _a_.
- Every common divisor of _a_ and _b_ is a divisor of gcd\(_a_, _b_\).
- gcd\(_a_, _b_\), where _a_ and _b_ are not both zero, may be defined alternatively and equivalently as the smallest positive integer _d_ which can be written in the form _d_ = _a_<!-- markdown separator -->⋅<!-- markdown separator -->_p_ + _b_<!-- markdown separator -->⋅<!-- markdown separator -->_q_, where _p_ and _q_ are integers. This expression is called [Bézout's identity](Bézout's%20identity.md). Numbers _p_ and _q_ like this can be computed with the [extended Euclidean algorithm](extended%20Euclidean%20algorithm.md).
- gcd\(_a_, 0\) = \|_a_\|, for _a_ ≠ 0, since any number is a divisor of 0, and the greatest divisor of _a_ is \|_a_\|.<sup>[\[2\]](#^ref-2)</sup><sup>[\[5\]](#^ref-5)</sup> This is usually used as the base case in the Euclidean algorithm.
- If _a_ divides the product _b_<!-- markdown separator -->⋅<!-- markdown separator -->_c_, and gcd\(_a_, _b_\) = _d_, then _a_<!-- markdown separator -->/<!-- markdown separator -->_d_ divides _c_.
- If _m_ is a positive integer, then gcd\(_m_<!-- markdown separator -->⋅<!-- markdown separator -->_a_, _m_<!-- markdown separator -->⋅<!-- markdown separator -->_b_\) = _m_<!-- markdown separator -->⋅gcd\(_a_, _b_\).
- If _m_ is any integer, then gcd\(_a_ + _m_<!-- markdown separator -->⋅<!-- markdown separator -->_b_, _b_\) = gcd\(_a_, _b_\). Equivalently, gcd\(_a_ mod _b_,_b_\) = gcd\(_a_,_b_\).
- If _m_ is a positive common divisor of _a_ and _b_, then gcd\(_a_<!-- markdown separator -->/<!-- markdown separator -->_m_, _b_<!-- markdown separator -->/<!-- markdown separator -->_m_\) = gcd\(_a_, _b_\)/<!-- markdown separator -->_m_.
- If gcd\(_a_, _b_\) = _d_, then gcd\(_a_<!-- markdown separator -->/<!-- markdown separator -->_d_, _b_<!-- markdown separator -->/<!-- markdown separator -->_d_\) = 1.
- The GCD is a [commutative](commutativity.md) function: gcd\(_a_, _b_\) = gcd\(_b_, _a_\).
- The GCD is an [associative](associativity.md) function: gcd\(_a_, gcd\(_b_, _c_\)\) = gcd\(gcd\(_a_, _b_\), _c_\). Thus gcd\(_a_, _b_, _c_, ...\) can be used to denote the GCD of multiple arguments.
- The GCD is a [multiplicative function](multiplicative%20function.md) in the following sense: if _a_<sub>1</sub> and _a_<sub>2</sub> are relatively prime, then gcd\(_a_<sub>1</sub>⋅<!-- markdown separator -->_a_<sub>2</sub>, _b_\) = gcd\(_a_<sub>1</sub>, _b_\)⋅gcd\(_a_<sub>2</sub>, _b_\).
- gcd\(_a_, _b_\) is closely related to the [least common multiple](least%20common%20multiple.md) lcm\(_a_, _b_\): we havegcd\(_a_, _b_\)⋅lcm\(_a_, _b_\) = \|_a_<!-- markdown separator -->⋅<!-- markdown separator -->_b_\|. <p> This formula is often used to compute least common multiples: one first computes the GCD with Euclid's algorithm and then divides the product of the given numbers by their GCD.
- The following versions of [distributivity](distributivity.md) hold true:gcd\(_a_, lcm\(_b_, _c_\)\) = lcm\(gcd\(_a_, _b_\), gcd\(_a_, _c_\)\) <p> lcm\(_a_, gcd\(_b_, _c_\)\) = gcd\(lcm\(_a_, _b_\), lcm\(_a_, _c_\)\). <p>
- If we have the unique prime factorizations of _a_ = _p_<sub>1</sub><sup>_e_<sub>1</sub></sup>_p_<sub>2</sub><sup>_e_<sub>2</sub></sup> ⋅⋅⋅ _p_<sub>_m_</sub><sup>_e_<sub>_m_</sub></sup> and _b_ = _p_<sub>1</sub><sup>_f_<sub>1</sub></sup>_p_<sub>2</sub><sup>_f_<sub>2</sub></sup> ⋅⋅⋅ _p_<sub>_m_</sub><sup>_f_<sub>_m_</sub></sup> where _e_<sub>_i_</sub> ≥ 0 and _f_<sub>_i_</sub> ≥ 0, then the GCD of _a_ and _b_ isgcd\(_a_,_b_\) = _p_<sub>1</sub><sup>min\(_e_<sub>1</sub>,_f_<sub>1</sub>\)</sup>_p_<sub>2</sub><sup>min\(_e_<sub>2</sub>,_f_<sub>2</sub>\)</sup> ⋅⋅⋅ _p_<sub>_m_</sub><sup>min\(_e_<sub>_m_</sub>,_f_<sub>_m_</sub>\)</sup>. <p>
- It is sometimes useful to define gcd\(0, 0\) = 0 and lcm\(0, 0\) = 0 because then the [natural numbers](natural%20number.md) become a [complete](complete%20lattice.md) [distributive lattice](distributive%20lattice.md) with GCD as meet and LCM as join operation.<sup>[\[22\]](#^ref-22)</sup> This extension of the definition is also compatible with the generalization for commutative rings given below.
- In a [Cartesian coordinate system](Cartesian%20coordinate%20system.md), gcd\(_a_, _b_\) can be interpreted as the number of segments between points with integral coordinates on the straight [line segment](line%20segment.md) joining the points \(0, 0\) and \(_a_, _b_\).
- For non-negative integers _a_ and _b_, where _a_ and _b_ are not both zero, provable by considering the Euclidean algorithm in base _n_:<sup>[\[23\]](#^ref-23)</sup>gcd\(_n_<sup>_a_</sup> − 1, _n_<sup>_b_</sup> − 1\) = _n_<sup>gcd\(_a_,_b_\)</sup> − 1. <p>
- An [identity](identity%20(mathematics).md) involving [Euler's totient function](Euler's%20totient%20function.md): $$\gcd(a,b) = \sum_{k|a \text{ and }k|b} \varphi(k) .$$ <p>
- GCD Summatory function \(Pillai's arithmetical function\):

$\sum_{k=1}^n \gcd(k,n) = \sum_{d|n} d \varphi \left( \frac n d \right) =n\sum_{d|n}\frac{\varphi(d)}{d} =n\prod_{p|n}\left(1+\nu_p(n)\left(1-\frac{1}{p}\right)\right)$ where $\nu_p(n)$ is the _p_-adic valuation. \(sequence [A018804](https://oeis.org/A018804) in the [OEIS](On-Line%20Encyclopedia%20of%20Integer%20Sequences.md)\)

## probabilities and expected value

In 1972, James E. Nymann showed that _k_ integers, chosen independently and uniformly from {1, ..., _n_}, are coprime with probability 1/<!-- markdown separator -->_ζ_\(_k_\) as _n_ goes to infinity, where _ζ_ refers to the [Riemann zeta function](Riemann%20zeta%20function.md).<sup>[\[24\]](#^ref-24)</sup> \(See [coprime](coprime.md) for a derivation.\) This result was extended in 1987 to show that the probability that _k_ random integers have greatest common divisor _d_ is _d_<sup>−<!-- markdown separator -->_k_</sup>/ζ\(_k_\).<sup>[\[25\]](#^ref-25)</sup>

Using this information, the [expected value](expected%20value.md) of the greatest common divisor function can be seen \(informally\) to not exist when _k_ = 2. In this case the probability that the GCD equals _d_ is _d_<sup>−2</sup>/<!-- markdown separator -->_ζ_\(2\), so we have

$$\mathrm{E}( \mathrm{2} ) = \sum_{d=1}^\infty d (d^{-2}/\zeta(2)) = \frac{1}{\zeta(2)} \sum_{d=1}^\infty \frac{1}{d}.$$

This last summation is the [harmonic series](harmonic%20series%20(mathematics).md), which diverges. However, when _k_ ≥ 3, the expected value is well-defined, and by the above argument, it is

$$\mathrm{E}(k) = \sum_{d=1}^\infty d^{1-k} \zeta(k)^{-1} = \frac{\zeta(k-1)}{\zeta(k)}.$$

For _k_ = 3, this is approximately equal to 1.3684. For _k_ = 4, it is approximately 1.1106.

## in commutative rings

- See also: [Divisibility \(ring theory\)](divisibility%20(ring%20theory).md)

|                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![icon](../../archives/Wikimedia%20Commons/Question%20book-new.svg) | This section __needs [more citations](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)__. Please help [improve this section](https://en.wikipedia.org/wiki/Special:EditPage/Greatest%20common%20divisor) by [adding citations to reliable sources](https://en.wikipedia.org/wiki/Help:Referencing%20for%20beginners). Unsourced material may be challenged and [removed](https://en.wikipedia.org/wiki/Wikipedia:Verifiability#Burden_of_evidence). _\(August 2024\)_<!-- markdown separator -->_\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ |

The notion of greatest common divisor can more generally be defined for elements of an arbitrary [commutative ring](commutative%20ring.md), although in general there need not exist one for every pair of elements.<sup>[\[26\]](#^ref-26)</sup>

- If _R_ is a commutative ring, and _a_ and _b_ are in _R_, then an element _d_ of _R_ is called a _common divisor_ of _a_ and _b_ if it divides both _a_ and _b_ \(that is, if there are elements _x_ and _y_ in _R_ such that _d_·_x_ = _a_ and _d_·_y_ = _b_\).
- If _d_ is a common divisor of _a_ and _b_, and every common divisor of _a_ and _b_ divides _d_, then _d_ is called a _greatest common divisor_ of _a_ and _b_.

With this definition, two elements _a_ and _b_ may very well have several greatest common divisors, or none at all. If _R_ is an [integral domain](integral%20domain.md), then any two GCDs of _a_ and _b_ must be [associate elements](associate%20elements.md#divisibility,%20prime%20elements,%20and%20irreducible%20elements), since by definition either one must divide the other. Indeed, if a GCD exists, any one of its associates is a GCD as well.

Existence of a GCD is not assured in arbitrary integral domains. However, if _R_ is a [unique factorization domain](unique%20factorization%20domain.md) or any other [GCD domain](GCD%20domain.md), then any two elements have a GCD. If _R_ is a [Euclidean domain](euclidean%20domain.md) in which euclidean division is given algorithmically \(as is the case for instance when _R_ = _F_\[_X_\] where _F_ is a [field](field%20(mathematics).md), or when _R_ is the ring of [Gaussian integers](Gaussian%20integer.md)\), then greatest common divisors can be computed using a form of the Euclidean algorithm based on the division procedure.

The following is an example of an integral domain with two elements that do not have a GCD:

$$R = \mathbb{Z}\left[\sqrt{-3}\,\,\right],\quad a = 4 = 2\cdot 2 = \left(1+\sqrt{-3}\,\,\right)\left(1-\sqrt{-3}\,\,\right),\quad b = \left(1+\sqrt{-3}\,\,\right)\cdot 2.$$

The elements 2 and $1 + \sqrt{-3}$ are two [maximal common divisors](maximal%20common%20divisor.md) \(that is, any common divisor which is a multiple of 2 is associated to 2, the same holds for $1 + \sqrt{-3}$, but they are not associated, so there is no greatest common divisor of _a_ and _b_.

Corresponding to the Bézout property we may, in any commutative ring, consider the collection of elements of the form _pa_ + _qb_, where _p_ and _q_ range over the ring. This is the [ideal](ideal%20(ring%20theory).md) generated by _a_ and _b_, and is denoted simply \(_a_, _b_\). In a ring all of whose ideals are principal \(a [principal ideal domain](principal%20ideal%20domain.md) or PID\), this ideal will be identical with the set of multiples of some ring element _d_; then this _d_ is a greatest common divisor of _a_ and _b_. But the ideal \(_a_, _b_\) can be useful even when there is no greatest common divisor of _a_ and _b_. \(Indeed, [Ernst Kummer](Ernst%20Kummer.md) used this ideal as a replacement for a GCD in his treatment of [Fermat's Last Theorem](Fermat's%20Last%20Theorem.md), although he envisioned it as the set of multiples of some hypothetical, or _ideal_, ring element _d_, whence the ring-theoretic term.\)

## see also

- [Bézout domain](Bézout%20domain.md)
- [Lowest common denominator](lowest%20common%20denominator.md)
- [Unitary divisor](unitary%20divisor.md)

## notes

1. [Long \(1972](#CITEREFLong1972), p. 33\) <a id="^ref-1"></a>^ref-1
2. [Pettofrezzo & Byrkit \(1970](#CITEREFPettofrezzoByrkit1970), p. 34\) <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFKelley2004"></a> Kelley, W. Michael \(2004\). [_The Complete Idiot's Guide to Algebra_](https://books.google.com/books?id=K1hCltk-2RwC&pg=PA142). Penguin. p. 142. [ISBN](ISBN%20(identifier).md) [978-1-59257-161-1](https://en.wikipedia.org/wiki/Special:BookSources/978-1-59257-161-1).. <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFJones1999"></a> Jones, Allyn \(1999\). [_Whole Numbers, Decimals, Percentages and Fractions Year 7_](https://books.google.com/books?id=l-ItSuk-zngC&pg=PA16). Pascal Press. p. 16. [ISBN](ISBN%20(identifier).md) [978-1-86441-378-6](https://en.wikipedia.org/wiki/Special:BookSources/978-1-86441-378-6).. <a id="^ref-4"></a>^ref-4
5. [Hardy & Wright \(1979](#CITEREFHardyWright1979), p. 20\) <a id="^ref-5"></a>^ref-5
6. Some authors treat __greatest common denominator__ as synonymous with _greatest common divisor_. This contradicts the common meaning of the words that are used, as _[denominator](denominator.md)_ refers to [fractions](fraction%20(mathematics).md), and two fractions do not have any greatest common denominator \(if two fractions have the same denominator, one obtains a greater common denominator by multiplying all numerators and denominators by the same [integer](integer.md)\). <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFBarlowPeacockLardnerAiry1847"></a> [Barlow, Peter](Peter%20Barlow%20(mathematician).md); [Peacock, George](George%20Peacock.md); [Lardner, Dionysius](Dionysius%20Lardner.md); [Airy, Sir George Biddell](George%20Biddell%20Airy.md); [Hamilton, H. P.](Henry%20Hamilton%20(priest).md); Levy, A.; [De Morgan, Augustus](Augustus%20De%20Morgan.md); Mosley, Henry \(1847\). [_Encyclopaedia of Pure Mathematics_](https://books.google.com/books?id=3fIUAQAAMAAJ&pg=PA589). R. Griffin and Co. p. 589.. <a id="^ref-7"></a>^ref-7
8. Some authors use \(_a_, _b_\),<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup><sup>[\[5\]](#^ref-5)</sup> but this notation is often ambiguous. [Andrews \(1994](#CITEREFAndrews1994), p. 16\) explains this as: "Many authors write \(_a_, _b_\) for g.c.d.\(_a_, _b_\). We do not, because we shall often use \(_a_, _b_\) to represent a point in the Euclidean plane." <a id="^ref-8"></a>^ref-8
9. Thomas H. Cormen, _et al._, _Introduction to Algorithms_ \(2nd edition, 2001\) [ISBN](ISBN%20(identifier).md) [0262032937](https://en.wikipedia.org/wiki/Special:BookSources/0262032937), p. 852 <a id="^ref-9"></a>^ref-9
10. Bernard L. Johnston, Fred Richman, _Numbers and Symmetry: An Introduction to Algebra_ [ISBN](ISBN%20(identifier).md) [084930301X](https://en.wikipedia.org/wiki/Special:BookSources/084930301X), p. 38 <a id="^ref-10"></a>^ref-10
11. Martyn R. Dixon, _et al._, _An Introduction to Essential Algebraic Structures_ [ISBN](ISBN%20(identifier).md) [1118497759](https://en.wikipedia.org/wiki/Special:BookSources/1118497759), p. 59 <a id="^ref-11"></a>^ref-11
12. e.g., [Wolfram Alpha](Wolfram%20Alpha.md) [calculation](https://www.wolframalpha.com/input/?i=gcd%280%2C+0%29) and [Maxima](Maxima%20computer%20algebra%20system.md) <a id="^ref-12"></a>^ref-12
13. Jonathan Katz, Yehuda Lindell, _Introduction to Modern Cryptography_ [ISBN](ISBN%20(identifier).md) [1351133012](https://en.wikipedia.org/wiki/Special:BookSources/1351133012), 2020, section 9.1.1, p. 45 <a id="^ref-13"></a>^ref-13
14. <a id="CITEREFWeisstein"></a> Weisstein, Eric W. ["Greatest Common Divisor"](https://mathworld.wolfram.com/GreatestCommonDivisor.html). _mathworld.wolfram.com_. Retrieved 2020-08-30. <a id="^ref-14"></a>^ref-14
15. <a id="mwBKY"></a> ["Greatest Common Factor"](https://www.mathsisfun.com/greatest-common-factor.html). _<www.mathsisfun.com>_. Retrieved 2020-08-30. <a id="^ref-15"></a>^ref-15
16. <a id="CITEREFSlavin2008"></a> Slavin, Keith R. \(2008\). ["Q-Binomials and the Greatest Common Divisor"](http://www.integers-ejcnt.org/vol8.html). _INTEGERS: The Electronic Journal of Combinatorial Number Theory_. __8__. [University of West Georgia](University%20of%20West%20Georgia.md), [Charles University in Prague](Charles%20University%20in%20Prague.md): A5. Retrieved 2008-05-26. <a id="^ref-16"></a>^ref-16
17. <a id="CITEREFSchramm2008"></a> Schramm, Wolfgang \(2008\). ["The Fourier transform of functions of the greatest common divisor"](http://www.integers-ejcnt.org/vol8.html). _INTEGERS: The Electronic Journal of Combinatorial Number Theory_. __8__. [University of West Georgia](University%20of%20West%20Georgia.md), [Charles University in Prague](Charles%20University%20in%20Prague.md): A50. Retrieved 2008-11-25. <a id="^ref-17"></a>^ref-17
18. <a id="CITEREFKnuth1997"></a> [Knuth, Donald E.](Donald%20Knuth.md) \(1997\). _[The Art of Computer Programming](The%20Art%20of%20Computer%20Programming.md)_. Vol. 2: Seminumerical Algorithms \(3rd ed.\). Addison-Wesley Professional. [ISBN](ISBN%20(identifier).md) [0-201-89684-2](https://en.wikipedia.org/wiki/Special:BookSources/0-201-89684-2). <a id="^ref-18"></a>^ref-18
19. <a id="CITEREFShallcrossPanLin-Kriz1993"></a> Shallcross, D.; Pan, V.; Lin-Kriz, Y. \(1993\). ["The NC equivalence of planar integer linear programming and Euclidean GCD"](http://www.icsi.berkeley.edu/pubs/techreports/tr-92-041.pdf) \(PDF\). _34th IEEE Symp. Foundations of Computer Science_. pp. 557–564. [Archived](https://web.archive.org/web/20060905023143/http://www.icsi.berkeley.edu/pubs/techreports/tr-92-041.pdf) \(PDF\) from the original on 2006-09-05. <a id="^ref-19"></a>^ref-19
20. <a id="CITEREFChorGoldreich1990"></a> [Chor, B.](Benny%20Chor.md); Goldreich, O. \(1990\). "An improved parallel algorithm for integer GCD". _Algorithmica_. __5__ \(1–4\): 1–10. [doi](doi%20(identifier).md):[10.1007/BF01840374](https://doi.org/10.1007%2FBF01840374). [S2CID](S2CID%20(identifier).md#S2CID) [17699330](https://api.semanticscholar.org/CorpusID:17699330). <a id="^ref-20"></a>^ref-20
21. <a id="CITEREFAdlemanKompella1988"></a> Adleman, L. M.; Kompella, K. \(1988\). "Using smoothness to achieve parallelism". _20th Annual ACM Symposium on Theory of Computing_. New York. pp. 528–538. [doi](doi%20(identifier).md):[10.1145/62212.62264](https://doi.org/10.1145%2F62212.62264). [ISBN](ISBN%20(identifier).md) [0-89791-264-0](https://en.wikipedia.org/wiki/Special:BookSources/0-89791-264-0). [S2CID](S2CID%20(identifier).md#S2CID) [9118047](https://api.semanticscholar.org/CorpusID:9118047). <a id="^ref-21"></a>^ref-21
22. <a id="CITEREFMüller-HoissenWalther2012"></a> Müller-Hoissen, Folkert; Walther, Hans-Otto \(2012\). "Dov Tamari \(formerly Bernhard Teitler\)". In Müller-Hoissen, Folkert; Pallo, Jean Marcel; [Stasheff, Jim](Jim%20Stasheff.md) \(eds.\). _Associahedra, Tamari Lattices and Related Structures: Tamari Memorial Festschrift_. Progress in Mathematics. Vol. 299. Birkhäuser. pp. 1–40. [ISBN](ISBN%20(identifier).md) [978-3-0348-0405-9](https://en.wikipedia.org/wiki/Special:BookSources/978-3-0348-0405-9).. Footnote 27, p. 9: "For example, the natural numbers with _gcd_ \(greatest common divisor\) as meet and _lcm_ \(least common multiple\) as join operation determine a \(complete distributive\) lattice." Including these definitions for 0 is necessary for this result: if one instead omits 0 from the set of natural numbers, the resulting lattice is not complete. <a id="^ref-22"></a>^ref-22
23. <a id="CITEREFKnuthGrahamPatashnik1994"></a> [Knuth, Donald E.](Donald%20Knuth.md); [Graham, R. L.](Ronald%20Graham.md); Patashnik, O. \(March 1994\). _[Concrete Mathematics: A Foundation for Computer Science](Concrete%20Mathematics%5F%20A%20Foundation%20for%20Computer%20Science.md)_. [Addison-Wesley](Addison-Wesley.md). [ISBN](ISBN%20(identifier).md) [0-201-55802-5](https://en.wikipedia.org/wiki/Special:BookSources/0-201-55802-5). <a id="^ref-23"></a>^ref-23
24. <a id="CITEREFNymann1972"></a> Nymann, J. E. \(1972\). ["On the probability that _k_ positive integers are relatively prime"](https://doi.org/10.1016%2F0022-314X%2872%2990038-8). _[Journal of Number Theory](Journal%20of%20Number%20Theory.md)_. __4__ \(5\): 469–473. [Bibcode](bibcode%20(identifier).md):[1972JNT.....4..469N](https://scixplorer.org/abs/1972JNT.....4..469N). [doi](doi%20(identifier).md):[10.1016/0022-314X\(72\)90038-8](https://doi.org/10.1016%2F0022-314X%2872%2990038-8). <a id="^ref-24"></a>^ref-24
25. <a id="CITEREFChidambaraswamySitarmachandrarao1987"></a> Chidambaraswamy, J.; Sitarmachandrarao, R. \(1987\). ["On the probability that the values of _m_ polynomials have a given g.c.d."](https://doi.org/10.1016%2F0022-314X%2887%2990081-3) _Journal of Number Theory_. __26__ \(3\): 237–245. [doi](doi%20(identifier).md):[10.1016/0022-314X\(87\)90081-3](https://doi.org/10.1016%2F0022-314X%2887%2990081-3). <a id="^ref-25"></a>^ref-25
26. <a id="CITEREFLovett2015"></a> Lovett, Stephen \(2015\). "Divisibility in Commutative Rings". _Abstract Algebra: Structures and Applications_. Boca Raton: CRC Press. pp. 267–318. [ISBN](ISBN%20(identifier).md) [9781482248913](https://en.wikipedia.org/wiki/Special:BookSources/9781482248913). <a id="^ref-26"></a>^ref-26

## references

- <a id="CITEREFAndrews1994"></a> [Andrews, George E.](George%20Andrews%20(mathematician).md) \(1994\) \[1971\]. [_Number Theory_](https://books.google.com/books?id=eVwvvwZeBf4C). Dover. [ISBN](ISBN%20(identifier).md) [978-0-486-68252-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-68252-5).
- <a id="CITEREFHardyWright1979"></a> [Hardy, G. H.](G.%20H.%20Hardy.md); [Wright, E. M.](E.%20M.%20Wright.md) \(1979\). _[An Introduction to the Theory of Numbers](An%20Introduction%20to%20the%20Theory%20of%20Numbers.md)_ \(Fifth ed.\). Oxford: [Oxford University Press](Oxford%20University%20Press.md). [ISBN](ISBN%20(identifier).md) [978-0-19-853171-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-19-853171-5).
- <a id="CITEREFLong1972"></a> Long, Calvin T. \(1972\). _Elementary Introduction to Number Theory_ \(2nd ed.\). Lexington: [D. C. Heath and Company](D.%20C.%20Heath%20and%20Company.md). [LCCN](LCCN%20(identifier).md) [77171950](https://lccn.loc.gov/77171950).
- <a id="CITEREFPettofrezzoByrkit1970"></a> Pettofrezzo, Anthony J.; Byrkit, Donald R. \(1970\). _Elements of Number Theory_. Englewood Cliffs: [Prentice Hall](Prentice%20Hall.md). [LCCN](LCCN%20(identifier).md) [71081766](https://lccn.loc.gov/71081766).

## further reading

- [Donald Knuth](Donald%20Knuth.md). _[The Art of Computer Programming](The%20Art%20of%20Computer%20Programming.md)_, Volume 2: _Seminumerical Algorithms_, Third Edition. Addison-Wesley, 1997. [ISBN](ISBN%20(identifier).md) [0-201-89684-2](https://en.wikipedia.org/wiki/Special:BookSources/0-201-89684-2). Section 4.5.2: The Greatest Common Divisor, pp. 333–356.
- [Thomas H. Cormen](Thomas%20H.%20Cormen.md), [Charles E. Leiserson](Charles%20E.%20Leiserson.md), [Ronald L. Rivest](Ronald%20L.%20Rivest.md), and [Clifford Stein](Clifford%20Stein.md). _[Introduction to Algorithms](Introduction%20to%20Algorithms.md)_, Second Edition. MIT Press and McGraw-Hill, 2001. [ISBN](ISBN%20(identifier).md) [0-262-03293-7](https://en.wikipedia.org/wiki/Special:BookSources/0-262-03293-7). Section 31.2: Greatest common divisor, pp. 856–862.
- [Saunders Mac Lane](Saunders%20Mac%20Lane.md) and [Garrett Birkhoff](Garrett%20Birkhoff.md). _A Survey of Modern Algebra_, Fourth Edition. MacMillan Publishing Co., 1977. [ISBN](ISBN%20(identifier).md) [0-02-310070-2](https://en.wikipedia.org/wiki/Special:BookSources/0-02-310070-2). 1–7: "The Euclidean Algorithm."

## external links

- gcd\(x,y\) = y function graph: [https://www.desmos.com/calculator/6nizzenog5](https://www.desmos.com/calculator/6nizzenog5)

|                                                                              | <!-- - [v](https://en.wikipedia.org/wiki/Template:Number-theoretic%20algorithms) <br/> - [t](https://en.wikipedia.org/wiki/Template%20talk:Number-theoretic%20algorithms) <br/> - [e](https://en.wikipedia.org/wiki/Special:EditPage/Template%3ANumber-theoretic%20algorithms) --> [Number-theoretic](number%20theory.md) [algorithms](algorithm.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                   __[Primality tests](primality%20test.md)__ | - [AKS](AKS%20primality%20test.md) <br/> - [APR](Adleman–Pomerance–Rumely%20primality%20test.md) <br/> - [Baillie–PSW](Baillie–PSW%20primality%20test.md) <br/> - [Elliptic curve](elliptic%20curve%20primality.md) <br/> - [Pocklington](pocklington%20primality%20test.md) <br/> - [Fermat](fermat%20primality%20test.md) <br/> - [Lucas](lucas%20primality%20test.md) <br/> - _[Lucas–Lehmer](Lucas–Lehmer%20primality%20test.md)_ <br/> - _[Lucas–Lehmer–Riesel](Lucas–Lehmer–Riesel%20test.md)_ <br/> - _[Proth's theorem](proth's%20theorem.md)_ <br/> - _[Pépin's](pépin's%20test.md)_ <br/> - [Quadratic Frobenius](Quadratic%20Frobenius%20test.md) <br/> - [Solovay–Strassen](Solovay–Strassen%20primality%20test.md) <br/> - [Miller–Rabin](Miller–Rabin%20primality%20test.md)                                                                                                                                                                       |
|                               __[Prime-generating](generating%20primes.md)__ | - [Sieve of Atkin](Sieve%20of%20Atkin.md) <br/> - [Sieve of Eratosthenes](Sieve%20of%20Eratosthenes.md) <br/> - [Sieve of Pritchard](Sieve%20of%20Pritchard.md) <br/> - [Sieve of Sundaram](Sieve%20of%20Sundaram.md) <br/> - [Wheel factorization](wheel%20factorization.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                      __[Integer factorization](integer%20factorization.md)__ | - [Continued fraction \(CFRAC\)](continued%20fraction%20factorization.md) <br/> - [Dixon's](dixon's%20factorization%20method.md) <br/> - [Lenstra elliptic curve \(ECM\)](lenstra%20elliptic-curve%20factorization.md) <br/> - [Euler's](euler's%20factorization%20method.md) <br/> - [Pollard's rho](pollard's%20rho%20algorithm.md) <br/> - [_p_ − 1](pollard's%20p%20−%201%20algorithm.md) <br/> - [_p_ + 1](williams's%20p%20+%201%20algorithm.md) <br/> - [Quadratic sieve \(QS\)](quadratic%20sieve.md) <br/> - [General number field sieve \(GNFS\)](general%20number%20field%20sieve.md) <br/> - _[Special number field sieve \(SNFS\)](special%20number%20field%20sieve.md)_ <br/> - [Rational sieve](rational%20sieve.md) <br/> - [Fermat's](fermat's%20factorization%20method.md) <br/> - [Shanks's square forms](shanks's%20square%20forms%20factorization.md) <br/> - [Trial division](trial%20division.md) <br/> - [Shor's](Shor's%20algorithm.md) |
|                          __[Multiplication](multiplication%20algorithm.md)__ | - [Ancient Egyptian](Ancient%20Egyptian%20multiplication.md) <br/> - [Long](long%20multiplication.md#long%20multiplication) <br/> - [Karatsuba](karatsuba%20algorithm.md) <br/> - [Toom–Cook](Toom–Cook%20multiplication.md) <br/> - [Schönhage–Strassen](Schönhage–Strassen%20algorithm.md) <br/> - [Fürer's](Fürer's%20algorithm.md#further%20improvements)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| __[Euclidean](Euclidean%20division.md) [division](division%20algorithm.md)__ | - [Binary](binary%20division.md#binary%20division) <br/> - [Chunking](chunking%20(division).md) <br/> - [Fourier](fourier%20division.md) <br/> - [Goldschmidt](Goldschmidt%20division.md#Goldschmidt%20division) <br/> - [Newton-Raphson](Newton–Raphson%20division.md#Newton–Raphson%20division) <br/> - [Long](long%20division.md) <br/> - [Short](short%20division.md) <br/> - [SRT](SRT%20division.md#SRT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                            __[Discrete logarithm](discrete%20logarithm.md)__ | - [Baby-step giant-step](baby-step%20giant-step.md) <br/> - [Pollard rho](pollard's%20rho%20algorithm%20for%20logarithms.md) <br/> - [Pollard kangaroo](pollard's%20kangaroo%20algorithm.md) <br/> - [Pohlig–Hellman](Pohlig–Hellman%20algorithm.md) <br/> - [Index calculus](index%20calculus%20algorithm.md) <br/> - [Function field sieve](function%20field%20sieve.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                __[Greatest common divisor](greatest%20common%20divisor.md)__ | - [Binary](Binary%20GCD%20algorithm.md) <br/> - [Euclidean](Euclidean%20algorithm.md) <br/> - [Extended Euclidean](extended%20Euclidean%20algorithm.md) <br/> - [Lehmer's](Lehmer's%20GCD%20algorithm.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                            __[Modular square root](quadratic%20residue.md)__ | - [Cipolla](cipolla's%20algorithm.md) <br/> - [Pocklington's](pocklington's%20algorithm.md) <br/> - [Tonelli–Shanks](Tonelli–Shanks%20algorithm.md) <br/> - [Berlekamp](Berlekamp–Rabin%20algorithm.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                         __Other algorithms__ | - [Chakravala](chakravala%20method.md) <br/> - [Cornacchia](cornacchia's%20algorithm.md) <br/> - [Exponentiation by squaring](exponentiation%20by%20squaring.md) <br/> - [Integer square root](integer%20square%20root.md) <br/> - [Integer relation](integer%20relation%20algorithm.md) \([LLL](Lenstra–Lenstra–Lovász%20lattice%20basis%20reduction%20algorithm.md); [KZ](Korkine–Zolotarev%20lattice%20basis%20reduction%20algorithm.md)\) <br/> - [Modular exponentiation](modular%20exponentiation.md) <br/> - [Montgomery reduction](Montgomery%20reduction.md) <br/> - [Schoof](schoof's%20algorithm.md) <br/> - [Trachtenberg system](trachtenberg%20system.md)                                                                                                                                                                                                                                                                                          |
|                                                                              | - _Italics_ indicate that algorithm is for numbers of special forms                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

Retrieved from "[https://en.wikipedia.org/w/index.php?title=Greatest\_common\_divisor&oldid=1372179102](https://en.wikipedia.org/w/index.php?title=Greatest_common_divisor&oldid=1372179102)"
