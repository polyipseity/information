---
aliases:
  - Game of Nim
  - Nim
  - game of Nim
tags:
  - flashcard/active/general/eng/Nim
  - language/in/English
---

# Nim

- This article is about {@{the mathematical game of strategy}@}. For the programming language, see [Nim (programming language)](Nim%20(programming%20language).md).<!-- For other uses, see [Nim (disambiguation)](NIM.md).--> <!--SR:!2029-08-10,1381,361-->

__Nim__ is {@{a [mathematical](mathematical%20game.md) [game of strategy](strategy%20game.md) in which two players take turns removing (or "nimming") objects from distinct heaps or piles}@}. On each turn, {@{a player must remove at least one object}@}, and may {@{remove any number of objects provided they all come from the same heap or pile}@}. Depending on the version being played, the goal of the game is {@{either to avoid taking the last object or to take the last object}@}. <!--SR:!2027-11-19,788,321!2026-03-27,150,321!2025-11-24,317,341!2025-11-28,25,380-->

Nim is {@{fundamental to the [Sprague–Grundy theorem](Sprague–Grundy%20theorem.md)}@}, which {@{essentially says that every [impartial game](impartial%20game.md) is equivalent to a nim game with a single pile}@}. <!--SR:!2029-08-31,1398,361!2029-08-23,1392,361-->

## history

Variants of nim have been played since ancient times.<sup>[\[1\]](#^ref-1)</sup> The game is said to have originated in [China](china.md)—it closely resembles the Chinese game of _jiǎn-shízi_ (捡石子), or "picking stones"<sup>[\[2\]](#^ref-2)</sup>—but the origin is uncertain; the earliest European references to nim are from the beginning of the 16th century. Its current name was coined by [Charles L. Bouton](Charles%20L.%20Bouton.md) of [Harvard University](Harvard%20University.md), who also developed the complete theory of the game in 1901,<sup>[\[3\]](#^ref-3)</sup> but the origins of the name were never fully explained. The _[Oxford English Dictionary](Oxford%20English%20Dictionary.md)_ derives the name from the German verb _[nimm](wikt:nimm.md)_, meaning "take".

At the [1939 New York World's Fair](1939%20New%20York%20World's%20Fair.md) [Westinghouse](Westinghouse%20Electric%20Corporation.md) displayed a machine, the [Nimatron](nimatron.md), that played nim.<sup>[\[4\]](#^ref-4)</sup> From May 11 to October 27, 1940, only a few people were able to beat the machine in that six-month period; if they did, they were presented with a coin that said "Nim Champ".<sup>[\[5\]](#^ref-5)</sup> It was also one of the first-ever electronic computerized games. [Ferranti](ferranti.md) built a [nim-playing computer](nimrod%20(computer).md) which was displayed at the [Festival of Britain](Festival%20of%20Britain.md) in 1951. In 1952, Herbert Koppel, Eugene Grant and Howard Bailer, engineers from the W. L. Maxson Corporation, developed a machine weighing 23 kilograms (50 lb) which played nim against a human opponent and regularly won.<sup>[\[6\]](#^ref-6)</sup> A nim playing machine has been described made from [tinkertoys](tinkertoy.md).<sup>[\[7\]](#^ref-7)</sup>

The game of nim was the subject of [Martin Gardner](Martin%20Gardner.md)'s February 1958 [Mathematical Games column](List%20of%20Martin%20Gardner%20Mathematical%20Games%20columns.md) in _[Scientific American](Scientific%20American.md)_. A version of nim is played—and has symbolic importance—in the [French New Wave](French%20New%20Wave.md) film _[Last Year at Marienbad](Last%20Year%20at%20Marienbad.md)_ (1961).<sup>[\[8\]](#^ref-8)</sup>

## game play and illustration

Nim is typically played as {@{a [misère game](misère.md#misère%20game), in which the player to take the last object loses}@}. Nim can also be {@{played as a "normal play" game whereby the player taking the last object wins}@}. In either normal play or a misère game, when {@{there is exactly one heap with at least two objects}@}, {@{the player who takes next can easily win}@}. If {@{this removes either all or all but one objects from the heap that has two or more}@}, then {@{no heaps will have more than one object}@}, so {@{the players are forced to alternate removing exactly one object until the game ends}@}. If {@{the player leaves an even number of non-zero heaps (as the player would do in normal play)}@}, {@{the player takes last}@}; if {@{the player leaves an odd number of heaps (as the player would do in misère play)}@}, then {@{the other player takes last}@}. <!--SR:!2025-11-24,317,341!2025-11-23,316,341!2025-11-24,317,341!2025-11-10,305,341!2029-09-16,1412,361!2025-11-15,308,341!2028-04-12,969,341!2025-11-13,308,341!2025-11-23,316,341!2025-12-18,333,341!2025-11-09,304,341-->

The normal game is {@{between two players and is played with three heaps of any number of objects}@}. The two players {@{alternate taking any number of objects from any one of the heaps}@}. The goal is {@{to be the last to take an object}@}. In misère play, the goal is {@{instead to ensure that the opponent is forced to take the last remaining object}@}. <!--SR:!2026-12-18,612,341!2029-07-22,1365,361!2029-09-12,1408,361!2029-07-16,1360,361-->

The following example of a normal game is played between fictional players [Bob and Alice](Alice%20and%20Bob.md), who start with heaps of three, four and five objects.

| __Heap A__ | __Heap B__ | __Heap C__ | __Move__                                                                                       |
| ---------- | ---------- | ---------- | ---------------------------------------------------------------------------------------------- |
| 3          | 4          | 5          | Game begins                                                                                    |
| 1          | 4          | 5          | Bob takes 2 from A                                                                             |
| 1          | 4          | 2          | Alice takes 3 from C                                                                           |
| 1          | 3          | 2          | Bob takes 1 from B                                                                             |
| 1          | 2          | 2          | Alice takes 1 from B                                                                           |
| 0          | 2          | 2          | Bob takes entire A heap, leaving two 2s                                                        |
| 0          | 1          | 2          | Alice takes 1 from B                                                                           |
| 0          | 1          | 1          | Bob takes 1 from C leaving two 1s. (_In misère play he would take 2 from C leaving [0, 1, 0]_) |
| 0          | 0          | 1          | Alice takes 1 from B                                                                           |
| 0          | 0          | 0          | Bob takes entire C heap and wins                                                               |

## winning positions

The practical strategy to win at the game of nim is {@{for a player to get the other into one of the following positions}@}, and {@{every successive turn afterwards they should be able to make one of the smaller positions}@}. Only the last move {@{changes between misère and normal play}@}. <!--SR:!2025-11-24,317,341!2025-11-23,316,341!2025-11-08,304,341-->

| __2 heaps__ | __3 heaps__ | __4 heaps__     |
| ----------- | ----------- | --------------- |
| 1 1 \*      | 1 1 1 \*\*  | 1 1 1 1 \*      |
| 2 2         | 1 2 3       | 1 1 n n         |
| 3 3         | 1 4 5       | 1 2 4 7         |
| 4 4         | 1 6 7       | 1 2 5 6         |
| 5 5         | 1 8 9       | 1 3 4 6         |
| 6 6         | 2 4 6       | 1 3 5 7         |
| 7 7         | 2 5 7       | 2 3 4 5         |
| 8 8         | 3 4 7       | 2 3 6 7         |
| 9 9         | 3 5 6       | 2 3 8 9         |
| _n_ _n_     | 4 8 12      | 4 5 6 7         |
|             | 4 9 13      | 4 5 8 9         |
|             | 5 8 13      | _n_ _n_ _m_ _m_ |
|             | 5 9 12      | _n_ _n_ _n_ _n_ |

- \* Only valid for normal play.
- \*\* Only valid for misère.

For the generalisations, _n_ and _m_ can be {@{any value > 0, and they may be the same}@}. <!--SR:!2029-07-15,1359,361-->

## mathematical theory

Normal-play nim (or more precisely {@{the system of [nimbers](nimber.md)}@}) is {@{fundamental to the [Sprague–Grundy theorem](Sprague–Grundy%20theorem.md)}@}, which {@{essentially says that in normal play every [impartial game](impartial%20game.md) is equivalent to a nim heap that yields the same outcome}@} when {@{played in parallel with other normal play impartial games (see [disjunctive sum](disjunctive%20sum.md))}@}. <!--SR:!2025-11-18,311,341!2029-05-23,1309,350!2026-01-16,312,301!2027-10-25,794,301-->

While {@{all normal-play impartial games can be assigned a nim value}@}, that is {@{not the case under the misère convention}@}. {@{Only [tame games](genus%20theory.md#tame)}@} can be played using the same strategy as misère nim. <!--SR:!2029-09-17,1412,361!2026-12-07,603,341!2026-12-23,615,341-->

Nim is {@{a special case of a [poset game](poset%20game.md)}@} where {@{the [poset](partially%20ordered%20set.md) consists of disjoint [chains](total%20order.md) (the heaps)}@}. <!--SR:!2026-01-06,350,341!2026-12-31,622,341-->

The evolution graph of the game of nim with three heaps is {@{the same as three branches of the evolution graph of the [Ulam–Warburton automaton](Ulam–Warburton%20automaton.md)}@}.<sup>[\[9\]](#^ref-9)</sup> <!--SR:!2027-02-02,583,281-->

Nim has been {@{mathematically [solved](solved%20game.md) for any number of initial heaps and objects}@}, and {@{there is an easily calculated way to determine which player will win and which winning moves are open to that player}@}. <!--SR:!2025-11-11,306,341!2025-11-20,313,341-->

The key to the theory of the game is {@{the [binary](binary%20number.md) [digital sum](digital%20sum%20in%20base%20b.md) of the heap sizes}@}, i.e., {@{the sum (in binary), neglecting all carries from one digit to another}@}. This operation is {@{also known as "[bitwise xor](bitwise%20operation.md#XOR)" or "vector addition over [__GF__(2)](finite%20field.md)" (bitwise addition modulo 2)}@}. Within [combinatorial game theory](combinatorial%20game%20theory.md) it is usually called {@{the __nim-sum__, as it will be called here}@}. The nim-sum of _x_ and _y_ is written {@{_x_ ⊕ _y_ to distinguish it from the ordinary sum, _x_ + _y_}@}. An example of the calculation with heaps of size 3, 4, and 5 is as follows: <!--SR:!2028-07-20,996,341!2027-11-29,796,321!2028-09-11,1086,341!2029-05-24,1309,350!2025-11-29,26,380-->

```text
  Binary   Decimal

  011_2    3_10    Heap A
  100_2    4_10    Heap B
  101_2    5_10    Heap C
  ---
  010_2    2_10    The nim-sum of heaps A, B, and C, 3 ⊕ 4 ⊕ 5 = 2
```

An equivalent procedure, which is often easier to perform mentally, is to {@{express the heap sizes as sums of distinct [powers](exponentiation.md) of 2, cancel pairs of equal powers, and then add what is left}@}: <!--SR:!2027-12-11,866,330-->

```text
3 = 0 + 2 + 1 =     2   1      Heap A
4 = 4 + 0 + 0 = 4              Heap B
5 = 4 + 0 + 1 = 4       1      Heap C
--------------------------------------------------------------------
2 =                 2          What is left after canceling 1s and 4s
```

In normal play, the winning strategy is {@{to finish every move with a nim-sum of 0}@}. This is always possible if {@{the nim-sum is not zero before the move}@}. If {@{the nim-sum is zero}@}, then {@{the next player will lose if the other player does not make a mistake}@}. To find out which move to make, let X be {@{the nim-sum of all the heap sizes}@}. Find {@{a heap where the nim-sum of X and heap-size is less than the heap-size}@}; the winning strategy is {@{to play in such a heap, reducing that heap to the nim-sum of its original size with X}@}. In the example above, taking the nim-sum of the sizes is _X_ = 3 ⊕ 4 ⊕ 5 = 2. The nim-sums of the heap sizes A=3, B=4, and C=5 with X=2 are <!--SR:!2029-05-20,1306,350!2027-01-09,631,341!2027-01-02,624,341!2029-09-19,1414,361!2025-11-15,308,341!2025-12-10,327,341!2028-05-16,947,301-->

- _A_ ⊕ _X_ = 3 ⊕ 2 = 1 [Since (011) ⊕ (010) = 001]
- _B_ ⊕ _X_ = 4 ⊕ 2 = 6
- _C_ ⊕ _X_ = 5 ⊕ 2 = 7

The only heap that is reduced is heap A, so the winning move is to {@{reduce the size of heap A to 1 (by removing two objects)}@}. <!--SR:!2025-11-19,312,341-->

As a particular simple case, if {@{there are only two heaps left}@}, the strategy is to {@{reduce the number of objects in the bigger heap to make the heaps equal}@}. After that, no matter what move the opponent makes, the player can {@{make the same move on the other heap, guaranteeing that they take the last object}@}. <!--SR:!2029-06-19,1331,350!2029-05-24,1308,350!2029-09-22,1416,361-->

When {@{played as a misère game}@}, nim strategy is {@{different only when the normal play move would leave only heaps of size one}@}. In that case, the correct move is to {@{leave an odd number of heaps of size one (in normal play, the correct move would be to leave an even number of such heaps)}@}. <!--SR:!2029-08-14,1384,361!2028-05-17,997,341!2025-11-17,310,341-->

These strategies for normal play and a misère game are {@{the same until the number of heaps with at least two objects is exactly equal to one}@}. At that point, the next player {@{removes either all objects (or all but one) from the heap that has two or more}@}, so {@{no heaps will have more than one object (in other words, so all remaining heaps have exactly one object each)}@}, so {@{the players are forced to alternate removing exactly one object until the game ends}@}. In normal play, the player {@{leaves an even number of non-zero heaps, so the same player takes last}@}; in misère play, the player {@{leaves an odd number of non-zero heaps, so the other player takes last}@}. <!--SR:!2026-12-29,621,341!2026-12-06,603,341!2027-11-30,797,321!2025-11-16,309,341!2025-12-16,331,341!2029-05-13,1303,350-->

In a misère game with heaps of sizes three, four and five, the strategy would be applied like this:

| __A__ | __B__ | __C__ | __Nim-sum__                    | __Move__                                                                                                                                                                                  |
| ----- | ----- | ----- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3     | 4     | 5     | 010<sub>2</sub>=2<sub>10</sub> | I take 2 from A, leaving a sum of 000, so I will win.                                                                                                                                     |
| 1     | 4     | 5     | 000<sub>2</sub>=0<sub>10</sub> | You take 2 from C                                                                                                                                                                         |
| 1     | 4     | 3     | 110<sub>2</sub>=6<sub>10</sub> | I take 2 from B                                                                                                                                                                           |
| 1     | 2     | 3     | 000<sub>2</sub>=0<sub>10</sub> | You take 1 from C                                                                                                                                                                         |
| 1     | 2     | 2     | 001<sub>2</sub>=1<sub>10</sub> | I take 1 from A                                                                                                                                                                           |
| 0     | 2     | 2     | 000<sub>2</sub>=0<sub>10</sub> | You take 1 from C                                                                                                                                                                         |
| 0     | 2     | 1     | 011<sub>2</sub>=3<sub>10</sub> | The normal play strategy would be to take 1 from B, leaving an even number (2) heaps of size 1. For misère play, I take the entire B heap, to leave an odd number (1) of heaps of size 1. |
| 0     | 0     | 1     | 001<sub>2</sub>=1<sub>10</sub> | You take 1 from C, and lose.                                                                                                                                                              |

## proof of the winning formula

The soundness of the optimal strategy described above was demonstrated by {@{C. Bouton}@}. <!--SR:!2029-09-18,1413,361-->

__Theorem__. ::@:: In a normal nim game, the player making the first move has a winning strategy if and only if the nim-sum of the sizes of the heaps is not zero. Otherwise, the second player has a winning strategy. <!--SR:!2029-08-15,1385,361!2025-11-18,311,341-->

_Proof:_ Notice that {@{the nim-sum \(⊕\)}@} obeys {@{the usual [associative](associative%20property.md) and [commutative](commutative%20property.md) laws of addition \(+\)}@} and also satisfies {@{an additional property, _x_ ⊕ _x_ = 0}@}. <!--SR:!2028-06-02,952,330!2025-11-22,26,378!2025-11-22,26,378-->

Let {@{_x_<sub>1</sub>, ..., _x<sub>n</sub>_ be the sizes of the heaps before a move, and _y_<sub>1</sub>, ..., _y<sub>n</sub>_ the corresponding sizes after a move}@}. Let {@{_s_ = _x_<sub>1</sub> ⊕ ... ⊕ _x<sub>n</sub>_ and _t_ = _y_<sub>1</sub> ⊕ ... ⊕ _y<sub>n</sub>_}@}. If {@{the move was in heap _k_}@}, we have {@{_x<sub>i</sub>_ = _y<sub>i</sub>_ for all _i_ ≠ _k_, and _x<sub>k</sub>_ > _y<sub>k</sub>_}@}. By the properties of ⊕ mentioned above, we have {@{$${\begin{aligned}t&=0\oplus t\\&=s\oplus s\oplus t\\&=s\oplus (x_{1}\oplus \cdots \oplus x_{n})\oplus (y_{1}\oplus \cdots \oplus y_{n})\\&=s\oplus (x_{1}\oplus y_{1})\oplus \cdots \oplus (x_{n}\oplus y_{n})\\&=s\oplus 0\oplus \cdots \oplus 0\oplus (x_{k}\oplus y_{k})\oplus 0\oplus \cdots \oplus 0\\&=s\oplus x_{k}\oplus y_{k}\\[10pt](*)\quad t&=s\oplus x_{k}\oplus y_{k}\end{aligned} }$$}@} <!--SR:!2029-07-27,1369,361!2029-07-24,1367,361!2025-11-24,317,341!2025-12-10,288,290!2028-01-04,823,321-->

The theorem follows by {@{induction on the length of the game from these two lemmas}@}. <!--SR:!2029-08-25,1394,361-->

__Lemma 1__. ::@:: If _s_ = 0, then _t_ ≠ 0 no matter what move is made. <!--SR:!2029-03-31,1267,350!2025-11-08,304,341-->

_Proof of Lemma 1:_ ::@:: If there is no possible move, then the lemma is [vacuously true](vacuous%20truth.md) (and the first player loses the normal play game by definition). Otherwise, any move in heap _k_ will produce _t_ = _x<sub>k</sub>_ ⊕ _y<sub>k</sub>_ from (*). This number is nonzero, since _x<sub>k</sub>_ ≠ _y<sub>k</sub>_. <!--SR:!2025-11-23,316,341!2029-09-11,1407,361-->

__Lemma 2__. ::@:: If _s_ ≠ 0, it is possible to make a move so that _t_ = 0. <!--SR:!2025-11-24,317,341!2025-11-23,316,341-->

_Proof of Lemma 2:_ ::@:: Let _d_ be the position of the leftmost (most significant) nonzero bit in the binary representation of _s_, and choose _k_ such that the _d_-th bit of _x<sub>k</sub>_ is also nonzero. (Such a _k_ must exist, since otherwise the _d_-th bit of _s_ would be 0.) Then letting _y<sub>k</sub>_ = _s_ ⊕ _x<sub>k</sub>_, we claim that _y<sub>k</sub>_ < _x<sub>k</sub>_: all bits to the left of _d_ are the same in _x<sub>k</sub>_ and _y<sub>k</sub>_, bit _d_ decreases from 1 to 0 (decreasing the value by 2<sup>_d_</sup>), and any change in the remaining bits will amount to at most 2<sup>_d_</sup>−1. The first player can thus make a move by taking _x<sub>k</sub>_ − _y<sub>k</sub>_ objects from heap _k_, then $$\begin{aligned} t & = s \oplus x_k \oplus y_k && (\text{by }(*)) \\ & = s \oplus x_k \oplus (s \oplus x_k) \\ & = 0 \end{aligned}$$ <!--SR:!2027-11-07,781,321!2027-08-13,721,321-->

{@{The modification for misère play}@} is demonstrated by {@{noting that the modification first arises in a position that has only one heap of size 2 or more}@}. Notice that {@{in such a position _s_ ≠ 0}@}, and therefore {@{this situation has to arise when it is the turn of the player following the winning strategy}@}. The normal play strategy is {@{for the player to reduce this to size 0 or 1, leaving an even number of heaps with size 1}@}, and the misère strategy is {@{to do the opposite}@}. From that point on, {@{all moves are forced}@}. <!--SR:!2026-05-04,424,310!2026-12-30,622,341!2026-11-27,594,341!2025-11-24,317,341!2029-09-23,1417,361!2025-11-17,310,341!2029-05-30,1315,350-->

## variations

### the subtraction game

In another game which is commonly known as {@{nim (but is better called the [subtraction game](subtraction%20game.md))}@}, {@{an upper bound is imposed on the number of objects that can be removed in a turn}@}. Instead of {@{removing arbitrarily many objects}@}, a player can {@{only remove 1 or 2 or ... or _k_ at a time}@}. This game is commonly played in practice {@{with only one heap}@}. <!--SR:!2028-11-18,1141,341!2029-09-04,1401,361!2025-11-09,304,341!2029-09-29,1422,361!2029-09-05,1402,361-->

Bouton's analysis {@{carries over easily to the general multiple-heap version of this game}@}. The only difference is that {@{as a first step, before computing the nim-sums}@} we {@{must reduce the sizes of the heaps [modulo](modular%20arithmetic.md) _k_ + 1}@}. If {@{this makes all the heaps of size zero (in misère play)}@}, the winning move is {@{to take _k_ objects from one of the heaps}@}. In particular, in {@{ideal play from a single heap of _n_ objects}@}, the second player can win [if and only if](if%20and%20only%20if.md) <!--SR:!2028-10-20,1117,341!2027-12-28,819,321!2026-05-02,422,310!2026-08-17,511,330!2028-04-26,931,301!2028-11-06,1130,341-->

- 0 = _n_ (mod _k_ + 1) ::@:: (in normal play), or <!--SR:!2025-11-28,182,290!2025-11-22,315,341-->
- 1 = _n_ (mod _k_ + 1) ::@:: (in misère play). <!--SR:!2028-09-28,1101,341!2026-01-03,308,301-->

This follows from {@{calculating the [nim-sequence](Sprague–Grundy%20theorem.md) of _S_(1, 2, ..., _k_), $$0.123\ldots k0123\ldots k0123\ldots ={\dot {0} }.123\ldots {\dot {k} },$$}@} <!--SR:!2025-12-24,301,301-->

from which the strategy above follows by {@{the [Sprague–Grundy theorem](Sprague–Grundy%20theorem.md)}@}. <!--SR:!2029-09-13,1409,361-->

### the 21 game

- see ::@:: [21 (drinking game)](21%20(drinking%20game).md) <!--SR:!2025-12-04,321,341!2029-08-08,1380,361-->

The game "21" is played as {@{a misère game with any number of players who take turns saying a number}@}. The first player {@{says "1" and each player in turn increases the number by 1, 2, or 3, but may not exceed 21}@}; the player {@{forced to say "21" loses}@}. This can be modeled as {@{a subtraction game with a heap of 21 − _n_ objects}@}. The winning strategy for {@{the two-player version of this game is to always say a multiple of 4}@}; it is then {@{guaranteed that the other player will ultimately have to say 21}@}; so in the standard version, wherein {@{the first player opens with "1", they start with a losing move}@}. <!--SR:!2025-12-19,334,341!2029-08-27,1395,361!2025-11-12,307,341!2029-09-30,1423,361!2029-08-11,1382,361!2029-09-24,1418,361!2026-12-25,617,341-->

The 21 game can also be {@{played with different numbers, e.g., "Add at most 5; lose on 34"}@}. <!--SR:!2025-11-19,312,341-->

A sample game of 21 in which the second player follows the winning strategy:

| __Player__ | __Number__   |
| ---------- | ------------ |
| 1          | 1            |
| 2          | 4            |
| 1          | 5, 6 or 7    |
| 2          | 8            |
| 1          | 9, 10 or 11  |
| 2          | 12           |
| 1          | 13, 14 or 15 |
| 2          | 16           |
| 1          | 17, 18 or 19 |
| 2          | 20           |
| 1          | 21           |

### the 100 game

A similar version is the "100 game": {@{Two players start from 0 and alternately add a number from 1 to 10 to the sum. The player who reaches 100 wins}@}. The winning strategy is to {@{reach a number in which the digits are subsequent (e.g., 01, 12, 23, 34,...) and control the game by jumping through all the numbers of this sequence}@}. Once {@{a player reaches 89}@}, the opponent can {@{only choose numbers from 90 to 99, and the next answer can in any case be 100}@}. <!--SR:!2026-12-13,608,341!2025-11-17,310,341!2026-12-11,606,341!2029-09-01,1399,361-->

### a multiple-heap rule

- see ::@:: [Wythoff's game](Wythoff's%20game.md) <!--SR:!2025-12-05,322,341!2028-10-08,1108,341-->

In another variation of nim, besides {@{removing any number of objects from a single heap}@}, one is {@{permitted to remove the same number of objects from each heap}@}. <!--SR:!2025-11-21,314,341!2027-10-22,851,341-->

### circular nim

- see ::@:: [Kayles](Kayles.md) <!--SR:!2025-12-15,330,341!2025-11-20,313,341-->

Yet another variation of nim is {@{"circular nim", wherein any number of objects are placed in a circle}@} and {@{two players alternately remove one, two or three adjacent objects}@}. For example, starting with a circle of ten objects, <!--SR:!2025-11-19,312,341!2029-07-28,1370,361-->

```text
. . . . . . . . . .
```

three objects are taken in the first move

```text
_ . . . . . . . _ _
```

then another three

```text
_ . _ _ _ . . . _ _
```

then one

```text
_ . _ _ _ . . _ _ _
```

but then three objects cannot be taken out in one move.

### Grundy's game

In [Grundy's game](Grundy's%20game.md), another variation of nim, a number of objects are {@{placed in an initial heap and two players alternately divide a heap into two nonempty heaps of different sizes}@}. Thus, six objects may be {@{divided into piles of 5+1 or 4+2, but not 3+3}@}. Grundy's game can be played as {@{either misère or normal play}@}. <!--SR:!2026-04-21,417,321!2028-11-17,1140,341!2029-08-30,1398,361-->

### greedy nim

Greedy nim is a variation wherein {@{the players are restricted to choosing stones from only the largest pile}@}.<sup>[\[10\]](#^ref-10)</sup> It is {@{a finite [impartial game](impartial%20game.md)}@}. Greedy nim misère has {@{the same rules as greedy nim, but the last player able to make a move loses}@}. <!--SR:!2029-08-09,1380,361!2029-05-31,1315,350!2025-12-20,335,341-->

Let {@{the largest number of stones in a pile be _m_ and the second largest number of stones in a pile be _n_}@}. Let {@{_p_<sub>_m_</sub> be the number of piles having _m_ stones and _p_<sub>_n_</sub> be the number of piles having _n_ stones}@}. Then there is a theorem that {@{game positions with _p_<sub>_m_</sub> even are _P_ positions (winning positions for the _p_-revious player)}@}.<sup>[\[11\]](#^ref-11)</sup> This theorem can be shown by {@{considering the positions where _p_<sub>_m_</sub> is odd}@}. If {@{_p_<sub>_m_</sub> is larger than 1}@}, {@{all stones may be removed from this pile to reduce _p_<sub>_m_</sub> by 1 and the new _p_<sub>_m_</sub> will be even}@}. If {@{_p_<sub>_m_</sub> = 1 (i.e. the largest heap is unique)}@}, there are {@{two cases}@}: <!--SR:!2025-12-09,326,341!2025-11-16,309,341!2027-04-15,643,341!2029-08-13,1383,361!2026-01-07,351,341!2025-11-24,317,341!2025-11-18,311,341!2025-11-21,314,341-->

- If _p_<sub>_n_</sub> is odd, ::@:: the size of the largest heap is reduced to _n_ (so now the new _p_<sub>_m_</sub> is even). <!--SR:!2026-12-18,612,341!2027-10-03,824,330-->
- If _p_<sub>_n_</sub> is even, ::@:: the largest heap is removed entirely, leaving an even number of largest heaps. <!--SR:!2025-11-24,317,341!2028-10-31,1127,341-->

Thus, there exists {@{a move to a state where _p_<sub>_m_</sub> is even}@}. Conversely, if {@{_p_<sub>_m_</sub> is even, if any move is possible (_p_<sub>_m_</sub> ≠ 0)}@}, then {@{it must take the game to a state where _p_<sub>_m_</sub> is odd}@}. The final position of the game is {@{even (_p_<sub>_m_</sub> = 0)}@}. Hence, {@{each position of the game with _p_<sub>_m_</sub> even must be a _P_ position}@}. <!--SR:!2029-08-24,1393,361!2026-12-24,616,341!2029-07-18,1362,361!2025-11-14,307,341!2025-11-14,307,341-->

### index-_k_ nim

A generalization of multi-heap nim was called {@{"nim<sub>_k_</sub>" or "index-_k_" nim by [E. H. Moore](E.%20H.%20Moore.md)}@},<sup>[\[12\]](#^ref-12)</sup> who {@{analyzed it in 1910}@}. In index-_k_ nim, instead of {@{removing objects from only one heap}@}, players can {@{remove objects from at least one but up to _k_ different heaps}@}. The number of elements that may be removed {@{from each heap may be either arbitrary or limited to at most _r_ elements, like in the "subtraction game" above}@}. <!--SR:!2026-07-30,430,321!2028-09-28,1099,341!2026-12-28,620,341!2025-11-23,316,341!2026-12-14,608,341-->

The winning strategy is as follows: Like in ordinary multi-heap nim, one {@{considers the binary representation of the heap sizes (or heap sizes modulo _r_ + 1)}@}. In ordinary nim {@{one forms the XOR-sum (or sum modulo 2) of each binary digit, and the winning strategy is to make each XOR sum zero}@}. In the generalization to index-_k_ nim, {@{one forms the sum of each binary digit modulo _k_ + 1 (this is no longer the XOR-sum, but a generalization of it)}@}. <!--SR:!2028-02-29,905,301!2026-08-12,507,330!2026-12-06,602,341-->

Again, the winning strategy is {@{to move such that this sum is zero for every digit}@}. Indeed, the value thus computed is {@{zero for the final position}@}, and given {@{a configuration of heaps for which this value is zero}@}, {@{any change of at most _k_ heaps will make the value non-zero}@}. Conversely, given {@{a configuration with non-zero value}@}, one can {@{always take from at most _k_ heaps, carefully chosen, so that the value will become zero}@}. <!--SR:!2029-08-07,1379,361!2029-09-28,1421,361!2029-09-02,1400,361!2025-11-23,316,341!2028-10-15,1113,341!2026-03-19,387,310-->

### building nim

Building nim is {@{a variant of nim wherein the two players first construct the game of nim}@}. Given {@{_n_ stones and _s_ empty piles}@}, the players, {@{alternating turns, place exactly one stone into a pile of their choice}@}.<sup>[\[13\]](#^ref-13)</sup> Once {@{all the stones are placed}@}, {@{a game of Nim begins, starting with the next player that would move. This game is denoted _BN(n,s)_}@}. <!--SR:!2025-11-08,304,341!2025-11-23,316,341!2025-11-23,316,341!2029-04-03,1269,350!2025-12-17,332,341-->

### higher-dimensional nim

_n_-d nim is played on {@{a $k_{1}\times \dots \times k_{n}$ board}@}, whereon {@{any number of continuous pieces can be removed from any hyper-row}@}. The starting position is {@{usually the full board, but other options are allowed}@}.<sup>[\[14\]](#^ref-14)</sup> <!--SR:!2025-11-24,317,341!2025-11-23,316,341!2026-12-12,607,341-->

### graph nim

The starting board is {@{a disconnected graph}@}, and players {@{take turns to remove adjacent vertices}@}.<sup>[\[15\]](#^ref-15)</sup> <!--SR:!2029-08-28,1396,361!2025-12-11,328,341-->

### candy nim

Candy nim is {@{a version of normal-play nim in which players try to achieve two goals at the same time}@}: {@{taking the last object (in this case, candy) and taking the maximum number of candies by the end of the game}@}.<sup>[\[16\]](#^ref-16)</sup> <!--SR:!2029-09-06,1403,361!2025-11-22,315,341-->

## see also

- _[Android Nim](Android%20Nim.md)_
- [Chomp](chomp.md)
- [Dr. Nim](Dr.%20Nim.md)
- [Fibonacci nim](fibonacci%20nim.md)
- [fuzzy game](fuzzy%20game.md)
- [Hackenbush](Hackenbush.md)
- [Notakto](Notakto.md)
- [octal games](octal%20game.md)
- [Raymond Redheffer](Raymond%20Redheffer.md)
- [star (game theory)](star%20(game%20theory).md)
- [subtract a square](subtract%20a%20square.md)
- [Tri-nim](Tri-nim.md)
- [Turing Tumble](Turing%20Tumble.md)
- [zero game](zero%20game.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Nim) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Jorgensen, Anker Helms (2009), ["Context and driving forces in the development of the early computer game Nimbi"](http://muse.jhu.edu/journals/ieee_annals_of_the_history_of_computing/v031/31.3.jorgensen.html), _IEEE Annals of the History of Computing_, __31__ (3): 44–53, [doi](digital%20object%20identifier.md):[10.1109/MAHC.2009.41](https://doi.org/10.1109%2FMAHC.2009.41), [MR](Mathematical%20Reviews.md) [2767447](https://mathscinet.ams.org/mathscinet-getitem?mr=2767447), [S2CID](Semantic%20Scholar.md#S2CID) [2833693](https://api.semanticscholar.org/CorpusID:2833693), The two-person mathematical game nim, which many believe originated in China, is probably one of the oldest games in the world. <a id="^ref-1"></a>^ref-1
2. [Yaglom, I. M.](Isaak%20Yaglom.md) (2001), "Two games with matchsticks", in [Tabachnikov, Serge](Sergei%20Tabachnikov.md) (ed.), [_Kvant Selecta: Combinatorics, I, Volume 1_](https://books.google.com/books?id=yID37VIW-t8C&pg=PA1), Mathematical world, vol. 17, [American Mathematical Society](American%20Mathematical%20Society.md), pp. 1–8, [ISBN](ISBN.md) [9780821821718](https://en.wikipedia.org/wiki/Special:BookSources/9780821821718) <a id="^ref-2"></a>^ref-2
3. [Bouton, C. L.](Charles%20L.%20Bouton.md) (1901–1902), "Nim, _a game with a complete mathematical theory_", _[Annals of Mathematics](Annals%20of%20Mathematics.md)_, __3__ (14): 35–39, [doi](digital%20object%20identifier.md):[10.2307/1967631](https://doi.org/10.2307%2F1967631), [JSTOR](JSTOR.md) [1967631](https://www.jstor.org/stable/1967631) <a id="^ref-3"></a>^ref-3
4. Flesch, Rudolf (1951). _The Art of Clear Thinking_. New York: Harper and Brothers Publishers. p. 3. <a id="^ref-4"></a>^ref-4
5. Kellem, Betsy (2022-03-01). ["The Nimatron"](https://daily.jstor.org/the-nimatron/). _JSTOR Daily_. [Archived](https://web.archive.org/web/20230628121301/https://daily.jstor.org/the-nimatron/) from the original on 2023-06-28. Retrieved 2023-06-28. <a id="^ref-5"></a>^ref-5
6. Grant, Eugene F.; Lardner, Rex (August 2, 1952). ["The Talk of the Town – It"](http://www.newyorker.com/archive/1952/08/02/1952_08_02_018_TNY_CARDS_000236053). _[The New Yorker](The%20New%20Yorker.md)_. <a id="^ref-6"></a>^ref-6
7. Cohen, Harvey A. ["How to Construct NIM Playing Machine"](http://harveycohen.net/papers/80-Nim_Playing_Machine.pdf) (PDF). <a id="^ref-7"></a>^ref-7
8. Morrissette, Bruce (1968), "Games and game structures in Robbe-Grillet", _Yale French Studies_ (41): 159–167, [doi](digital%20object%20identifier.md):[10.2307/2929672](https://doi.org/10.2307%2F2929672), [JSTOR](JSTOR.md) [2929672](https://www.jstor.org/stable/2929672). Morrissette writes that [Alain Robbe-Grillet](Alain%20Robbe-Grillet.md), one of the screenwriters for the film, "thought he had invented" the game. <a id="^ref-8"></a>^ref-8
9. Khovanova, Tanya; Xiong, Joshua (2014). "Nim Fractals". [arXiv](ArXiv.md):[1405.5942](https://arxiv.org/abs/1405.5942) [[math.CO](https://arxiv.org/archive/math.CO)]. <a id="^ref-9"></a>^ref-9
10. _Winning Ways for your Mathematical Plays_. Vol. 4 vols. (2nd ed.). A K Peters Ltd. 2001.; Berlekamp, Elwyn R.; Conway, John Horton; Guy, Richard K. (2003-06-15). _vol. 1_. [ISBN](ISBN.md) [978-1-56881-130-7](https://en.wikipedia.org/wiki/Special:BookSources/978-1-56881-130-7).; Berlekamp, Elwyn R.; Conway, John Horton; Guy, Richard K. (2003-06-15). _vol. 2_. [ISBN](ISBN.md) [978-1-56881-142-0](https://en.wikipedia.org/wiki/Special:BookSources/978-1-56881-142-0).; Berlekamp, Elwyn R.; Conway, John Horton; Guy, Richard K. (2003-06-15). _vol. 3_. [ISBN](ISBN.md) [978-1-56881-143-7](https://en.wikipedia.org/wiki/Special:BookSources/978-1-56881-143-7).; Berlekamp, Elwyn R.; Conway, John Horton; Guy, Richard K. (2004-06-15). _vol. 4_. [ISBN](ISBN.md) [978-1-56881-144-4](https://en.wikipedia.org/wiki/Special:BookSources/978-1-56881-144-4). <a id="^ref-10"></a>^ref-10
11. Albert, M. H.; Nowakowski, R. J. (2004). ["Nim Restrictions"](http://www.emis.de/journals/INTEGERS/papers/eg1/eg1.pdf) (PDF). _Integers_: 2. <a id="^ref-11"></a>^ref-11
12. Moore, E. H. _A Generalization of the Game Called Nim_. [Annals of Mathematics 11 (3), 1910, pp. 93–94](https://www.jstor.org/stable/1967321) <a id="^ref-12"></a>^ref-12
13. Larsson, Urban; [Heubach, Silvia](Silvia%20Heubach.md); Dufour, Matthieu; Duchêne, Eric (2015). "Building Nim". [arXiv](ArXiv.md):[1502.04068](https://arxiv.org/abs/1502.04068) [[cs.DM](https://arxiv.org/archive/cs.DM)]. <a id="^ref-13"></a>^ref-13
14. ["1021 - 2D-Nim"](http://poj.org/problem?id=1021). Poj.org. Retrieved 2019-01-09. <a id="^ref-14"></a>^ref-14
15. Erickson, Lindsay Anne (2011). ["The Game of Nim on Graphs"](https://library.ndsu.edu/ir/handle/10365/32839). _North Dakota State University_. <a id="^ref-15"></a>^ref-15
16. Rubinstein-Salzedo, Simon (18 May 2018). "P Play in Candy Nim". [arXiv](ArXiv.md):[1805.07019](https://arxiv.org/abs/1805.07019) [[math.CO](https://arxiv.org/archive/math.CO)]. <a id="^ref-16"></a>^ref-16

## further reading

- W. W. Rouse Ball: _Mathematical Recreations and Essays_, The Macmillan Company, 1947.
- John D. Beasley: _The Mathematics of Games_, Oxford University Press, 1989.
- Elwyn R. Berlekamp, John H. Conway, and Richard K. Guy: _[Winning Ways for your Mathematical Plays](Winning%20Ways%20for%20Your%20Mathematical%20Plays.md)_, Academic Press, Inc., 1982.
- [Manfred Eigen](Manfred%20Eigen.md) and [Ruthild Winkler](Ruthild%20Winkler.md): _Laws of the Game_, Princeton University Press, 1981.
- Walter R. Fuchs: _Computers: Information Theory and Cybernetics_, Rupert Hart-Davis Educational Publications, 1971.
- G. H. Hardy and E. M. Wright: _An Introduction to the Theory of Numbers_, Oxford University Press, 1979.
- Edward Kasner and James Newman: _[Mathematics and the Imagination](Mathematics%20and%20the%20Imagination.md)_, Simon and Schuster, 1940.
- M. Kaitchik: _Mathematical Recreations_, W. W. Norton, 1942.
- Donald D. Spencer: _Game Playing with Computers_, Hayden Book Company, Inc., 1968.

## external links

- "[50-pound computer plays Nim](http://www.newyorker.com/archive/1952/08/02/1952_08_02_018_TNY_CARDS_000236053)" – _[The New Yorker](The%20New%20Yorker.md)_ - "Talk of the Town" August, 1952 (subscription required)
- [The hot game of Nim](https://web.archive.org/web/20080820154432/http://www.cut-the-knot.org/ctk/May2001.html) – Nim theory and connections with other games at [cut-the-knot](Alexander%20Bogomolny.md#Cut-the-Knot)
- [Nim](http://www.cut-the-knot.org/nim_st.shtml) and 2-dimensional [SuperNim](http://www.cut-the-knot.org/Games/SuperNim/SNim.shtml) at [cut-the-knot](Alexander%20Bogomolny.md#Cut-the-Knot)
