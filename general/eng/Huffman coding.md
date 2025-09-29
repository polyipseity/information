---
aliases:
  - Huffman code
  - Huffman codes
  - Huffman coding
  - Huffman codings
  - Huffman encoding
  - Huffman encodings
tags:
  - flashcard/active/general/eng/Huffman_coding
  - language/in/English
---

# Huffman coding

> {@{![this is an example of a Huffman tree](../../archives/Wikimedia%20Commons/Huffman%20tree%202.svg)}@}
>
> {@{Huffman tree generated}@} from {@{the exact frequencies of the text "this is an example of a huffman tree"}@}. {@{Encoding the sentence with this code}@} requires {@{135 \(or 147\) bits}@}, as opposed to {@{288 \(or 180\) bits if 36 characters of 8 \(or 5\) bits were used}@} \(This assumes that {@{the code tree structure is known to the decoder and thus does not need to be counted as part of the transmitted information}@}\). {@{The frequencies and codes of each character}@} are shown in the accompanying table.
>
> | __Char__ | __Freq__ | __Code__ |
> | -------- | -------- | -------- |
> | space    | 7        | 111      |
> | a        | 4        | 010      |
> | e        | 4        | 000      |
> | f        | 3        | 1101     |
> | h        | 2        | 1010     |
> | i        | 2        | 1000     |
> | m        | 2        | 0111     |
> | n        | 2        | 0010     |
> | s        | 2        | 1011     |
> | t        | 2        | 0110     |
> | l        | 1        | 11001    |
> | o        | 1        | 00110    |
> | p        | 1        | 10011    |
> | r        | 1        | 11000    |
> | u        | 1        | 00111    |
> | x        | 1        | 10010    | <!--SR:!2026-09-17,490,310!2027-12-06,792,330!2025-11-23,277,330!2028-11-16,1128,350!2026-10-25,508,310!2025-11-15,270,330!2026-02-06,309,290!2025-12-01,284,330-->

In {@{[computer science](computer%20science.md) and [information theory](information%20theory.md)}@}, {@{a __Huffman code__}@} is {@{a particular type of optimal [prefix code](prefix%20code.md) that is commonly used for [lossless data compression](lossless%20compression.md)}@}. {@{The process of finding or using such a code}@} is {@{__Huffman coding__}@}, {@{an algorithm developed by [David A. Huffman](David%20A.%20Huffman.md) while he was a [Sc.D.](Doctor%20of%20Science.md) student at [MIT](Massachusetts%20Institute%20of%20Technology.md)}@}, and published in {@{the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes"}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-11-24,278,330!2025-11-15,271,330!2025-11-21,276,330!2028-09-11,1076,350!2028-08-05,1046,350!2026-11-02,515,310!2028-02-27,892,330-->

The output from Huffman's algorithm can be viewed as {@{a [variable-length code](variable-length%20code.md) table for encoding a source symbol \(such as a character in a file\)}@}. The algorithm derives this table from {@{the estimated probability or frequency of occurrence \(_weight_\) for each possible value of the source symbol}@}. As in {@{other [entropy encoding](entropy%20coding.md) methods}@}, {@{more common symbols are generally represented using fewer bits than less common symbols}@}. Huffman's method can be {@{efficiently implemented}@}, finding a code in {@{time [linear](time%20complexity.md#linear%20time) to the number of input weights if these weights are sorted}@}.<sup>[\[2\]](#^ref-2)</sup> However, although {@{optimal among methods encoding symbols separately (symbols are encoded into integral, as opposed to fractional, numbers of bits)}@}, Huffman coding {@{[is not always optimal](#optimality) among all compression methods}@} - it is {@{replaced with [arithmetic coding](arithmetic%20coding.md)<sup>[\[3\]](#^ref-3)</sup> or [asymmetric numeral systems](asymmetric%20numeral%20systems.md)<sup>[\[4\]](#^ref-4)</sup> if a better compression ratio is required}@}. <!--SR:!2027-06-24,703,330!2028-02-12,880,330!2025-11-30,283,330!2025-11-05,262,330!2025-12-07,289,330!2026-12-11,547,310!2025-12-01,284,330!2028-11-05,1119,350!2027-04-22,665,330-->

## history

In {@{1951, [David A. Huffman](David%20A.%20Huffman.md) and his [MIT](Massachusetts%20Institute%20of%20Technology.md) [information theory](information%20theory.md) classmates}@} were {@{given the choice of a term paper or a final [exam](exam.md)}@}. {@{The professor, [Robert M. Fano](Robert%20Fano.md)}@}, assigned {@{a [term paper](term%20paper.md) on the problem of finding the most efficient binary code}@}. Huffman, {@{unable to prove any codes were the most efficient}@}, was {@{about to give up and start studying for the final}@} when {@{he hit upon the idea of using a frequency-sorted [binary tree](binary%20tree.md) and quickly proved this method the most efficient}@}.<sup>[\[5\]](#^ref-5)</sup> <!--SR:!2026-09-28,488,310!2027-09-09,769,330!2025-11-14,269,330!2026-10-12,499,310!2025-11-27,281,330!2028-08-13,1052,350!2025-11-17,272,330-->

In doing so, {@{Huffman outdid Fano}@}, who {@{had worked with [Claude Shannon](Claude%20Shannon.md) to develop a similar code}@}. {@{Building the tree from the bottom up guaranteed optimality}@}, unlike {@{the top-down approach of [Shannon–Fano coding](Shannon–Fano%20coding.md)}@}. <!--SR:!2025-11-04,261,330!2025-11-19,274,330!2025-12-08,290,330!2027-06-09,703,330-->

## terminology

Huffman coding uses {@{a specific method for choosing the representation for each symbol}@}, resulting in {@{a [prefix code](prefix%20code.md) \(sometimes called "prefix-free codes"}@}, that is, {@{the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol}@}\). Huffman coding is {@{such a widespread method for creating prefix codes}@} that {@{the term "Huffman code" is widely used as a synonym for "prefix code" even when such a code is not produced by Huffman's algorithm}@}. <!--SR:!2025-11-25,279,330!2025-12-02,285,330!2027-05-31,695,330!2025-11-05,261,330!2025-11-29,282,330-->

## problem definition

<!-- ![](https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/50px-Question_book-new.svg.png) -->
<!-- -->
<!-- This article __needs additional citations for [verification](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)__. Please help [improve this article](https://en.wikipedia.org/wiki/Special:EditPage/Huffman%20coding) by adding citations to reliable sources. Unsourced material may be challenged and removed._Find sources:_ ["Huffman coding"](https://www.google.com/search?as_eq=wikipedia&q=%22Huffman+coding%22) – [news](https://www.google.com/search?tbm=nws&q=%22Huffman+coding%22+-wikipedia&tbs=ar:1) __·__ [newspapers](https://www.google.com/search?&q=%22Huffman+coding%22&tbs=bkt:s&tbm=bks) __·__ [books](https://www.google.com/search?tbs=bks:1&q=%22Huffman+coding%22+-wikipedia) __·__ [scholar](https://scholar.google.com/scholar?q=%22Huffman+coding%22) __·__ [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Huffman+coding%22&acc=on&wc=on) _\(December 2021\)_ _\(Learn how and when to remove this message\)_ -->

> ![Constructing a Huffman Tree](../../archives/Wikimedia%20Commons/HuffmanCodeAlg.png)
>
> {@{Constructing a Huffman Tree}@} <!--SR:!2027-09-14,774,330-->

### informal description

__Given__ ::@:: A set of symbols and their weights \(usually [proportional](proportionality%20(mathematics).md) to probabilities\). <!--SR:!2027-12-04,791,330!2025-10-26,255,330-->

__Find__ ::@:: A [prefix-free binary code](prefix%20code.md) \(a set of codewords\) with minimum [expected](expected%20value.md) codeword length \(equivalently, a tree with minimum [weighted path length from the root](weighted%20path%20length%20from%20the%20root.md)\). <!--SR:!2027-04-27,669,330!2027-05-08,678,330-->

### formalized description

__Input__.

- Alphabet $A=(a_{1},a_{2},\dots ,a_{n})$, ::@:: which is the symbol alphabet of size $n$. <!--SR:!2025-11-22,276,330!2025-11-17,272,330-->
- Tuple $W=(w_{1},w_{2},\dots ,w_{n})$, ::@:: which is the tuple of the \(positive\) symbol weights \(usually proportional to probabilities\), i.e. $w_{i}=\operatorname {weight} \left(a_{i}\right),\,i\in \{1,2,\dots ,n\}$. <!--SR:!2028-09-27,1089,350!2025-11-12,268,330-->

__Output__.

- Code $C\left(W\right)=(c_{1},c_{2},\dots ,c_{n})$, ::@:: which is the tuple of \(binary\) codewords, where $c_{i}$ is the codeword for $a_{i},\,i\in \{1,2,\dots ,n\}$. <!--SR:!2027-08-22,762,330!2027-06-27,714,330-->

__Goal__.

- Let $L\left(C\left(W\right)\right)=\sum _{i=1}^{n}{w_{i}\operatorname {length} \left(c_{i}\right)}$ be the weighted path length of code $C$. Condition: ::@:: $L\left(C\left(W\right)\right)\leq L\left(T\left(W\right)\right)$ for any code $T\left(W\right)$. <!--SR:!2027-08-25,760,330!2025-11-21,276,330-->

### example

We give an example of {@{the result of Huffman coding for a code with five characters and given weights}@}. We will {@{not verify that it minimizes _L_ over all codes}@}, but we will {@{compute _L_ and compare it to the [Shannon entropy](entropy%20(information%20theory).md) _H_ of the given set of weights}@}; the result is {@{nearly optimal}@}. <!--SR:!2025-12-02,285,330!2028-08-01,1043,350!2025-11-18,273,330!2025-10-25,253,330-->

|                        |                                                                                        |       |       |       |       |       |                    |
|:----------------------:|:--------------------------------------------------------------------------------------:|:-----:|:-----:|:-----:|:-----:|:-----:|:------------------:|
| __Input \(_A_, _W_\)__ | Symbol \(_a_<sub>_i_</sub>\)                                                           | a     | b     | c     | d     | e     | __Sum__            |
|                        | Weights \(_w_<sub>_i_</sub>\)                                                          | 0.10  | 0.15  | 0.30  | 0.16  | 0.29  | = 1                |
| __Output _C___         | Codewords \(_c_<sub>_i_</sub>\)                                                        | `010` | `011` | `11`  | `00`  | `10`  |                    |
|                        | Codeword length \(in bits\) <br/> \(_l_<sub>_i_</sub>\)                                | 3     | 3     | 2     | 2     | 2     |                    |
|                        | Contribution to weighted path length <br/> \(_l_<sub>_i_</sub> _w_<sub>_i_</sub>\)     | 0.30  | 0.45  | 0.60  | 0.32  | 0.58  | _L_\(_C_\) = 2.25  |
| __Optimality__         | Probability budget <br/> \(2<sup>-_l_<sub>_i_</sub></sup>\)                            | 1/8   | 1/8   | 1/4   | 1/4   | 1/4   | = 1.00             |
|                        | Information content (in bits) <br/> \(−log<sub>2</sub> _w_<sub>_i_</sub>\) ≈           | 3.32  | 2.74  | 1.74  | 2.64  | 1.79  |                    |
|                        | Contribution to entropy <br/> \(-_w_<sub>_i_</sub> log<sub>2</sub> _w_<sub>_i_</sub>\) | 0.332 | 0.411 | 0.521 | 0.423 | 0.518 | _H_\(_A_\) = 2.205 |

For {@{any code that is _biunique_}@}, meaning that {@{the code is [_uniquely decodeable_](variable-length%20code.md#uniquely%20decodable%20codes)}@}, {@{the sum of the probability budgets across all symbols is always less than or equal to one}@}. In this example, {@{the sum is strictly equal to one}@}; as a result, {@{the code is termed a _complete_ code}@}. If {@{this is not the case}@}, one can {@{always derive an equivalent code by adding extra symbols \(with associated null probabilities\)}@}, to {@{make the code complete while keeping it _biunique_}@}. <!--SR:!2028-09-19,1082,350!2028-11-15,1127,350!2026-10-13,499,310!2025-11-06,263,330!2027-10-15,804,330!2028-09-20,1083,350!2028-01-10,818,330!2025-11-20,275,330-->

As {@{defined by [Shannon \(1948\)](A%20Mathematical%20Theory%20of%20Communication.md)}@}, {@{the information content _h_ \(in bits\) of each symbol _a_<sub>i</sub> with non-null probability}@} is {@{$$h(a_{i})=\log _{2}{1 \over w_{i} }.$$}@} {@{The [entropy](entropy%20(information%20theory).md) _H_ \(in bits\)}@} is {@{the weighted sum, across all symbols _a_<sub>_i_</sub> with non-zero probability _w_<sub>_i_</sub>, of the information content of each symbol}@}: {@{$$H(A)=\sum _{w_{i}>0}w_{i}h(a_{i})=\sum _{w_{i}>0}w_{i}\log _{2}{1 \over w_{i} }=-\sum _{w_{i}>0}w_{i}\log _{2}{w_{i} }.$$}@} \(Note: {@{A symbol with zero probability has zero contribution to the entropy}@}, since {@{$\lim _{w\to 0^{+} }w\log _{2}w=0$}@}. So for simplicity, {@{symbols with zero probability can be left out of the formula above}@}.\) <!--SR:!2026-03-26,345,290!2025-12-11,292,330!2025-10-27,255,330!2025-12-06,288,330!2026-03-23,343,290!2027-12-04,827,330!2028-10-01,1091,350!2025-11-23,277,330!2025-10-22,254,330-->

As {@{a consequence of [Shannon's source coding theorem](Shannon's%20source%20coding%20theorem.md)}@}, the entropy is {@{a measure of the smallest codeword length that is theoretically possible for the given alphabet with associated weights}@}. In this example, the weighted average codeword length is {@{2.25 bits per symbol}@}, only {@{slightly larger than the calculated entropy of 2.205 bits per symbol}@}. So {@{not only is this code optimal in the sense that no other feasible code performs better}@}, but {@{it is very close to the theoretical limit established by Shannon}@}. <!--SR:!2028-09-09,1073,350!2027-08-01,736,330!2025-12-07,289,330!2028-09-01,1067,350!2025-11-15,271,330!2025-10-23,251,330-->

In general, {@{a Huffman code need not be unique}@}. Thus {@{the set of Huffman codes for a given probability distribution}@} is {@{a non-empty subset of the codes minimizing $L(C)$ for that probability distribution}@}. \(However, for {@{each minimizing codeword length assignment}@}, there exists {@{at least one Huffman code with those lengths}@}.\) <!--SR:!2028-08-21,1058,350!2025-10-26,253,330!2025-10-18,250,330!2025-10-25,254,330!2025-11-11,268,330-->

## basic technique

### compression

> ![Visualisation of the use of Huffman coding to encode the message "A\_DEAD\_DAD\_CEDED\_A\_BAD\_BABE\_A\_BEADED\_ABACA\_BED".](../../archives/Wikimedia%20Commons/Huffman%20coding%20visualisation.svg)
>
> {@{Visualisation of the use of Huffman coding to encode the message "A\_DEAD\_DAD\_CEDED\_A\_BAD\_BABE\_A\_BEADED\_ABACA\_BED"}@}. In {@{steps 2 to 6}@}, the letters are {@{sorted by increasing frequency}@}, and {@{the least frequent two at each step are combined and reinserted into the list}@}, and {@{a partial tree is constructed}@}. The final tree in step 6 is {@{traversed to generate the dictionary in step 7}@}. Step 8 {@{uses it to encode the message}@}. <!--SR:!2025-10-31,258,330!2025-11-25,279,330!2025-11-13,268,330!2027-09-04,768,330!2028-09-12,1075,350!2025-11-08,265,330!2025-10-21,253,330-->

<!-- markdownlint MD028 -->

> {@{![Huffman coding example](../../archives/Wikimedia%20Commons/Huffman%20coding%20example.svg)}@}
>
> A source generates {@{4 different symbols $\{a_{1},a_{2},a_{3},a_{4}\}$ with probability $\{0.4;0.35;0.2;0.05\}$}@}. A binary tree is {@{generated from left to right}@} taking {@{the two least probable symbols and putting them together to form another equivalent symbol having a probability that equals the sum of the two symbols}@}. The process is {@{repeated until there is just one symbol}@}. The tree can then {@{be read backwards, from right to left, assigning different bits to different branches}@}. The final Huffman code is:
>
> | __Symbol__ | __Code__  |
> | ---------- | --------- |
> | {@{a1}@}   | {@{0}@}   |
> | {@{a2}@}   | {@{10}@}  |
> | {@{a3}@}   | {@{110}@} |
> | {@{a4}@}   | {@{111}@} |
>
> {@{The standard way to represent a signal made of 4 symbols}@} is by {@{using 2 bits/symbol}@}, but {@{the [entropy](entropy%20(information%20theory).md) of the source is 1.74 bits/symbol}@}. If {@{this Huffman code is used to represent the signal}@}, then {@{the average length is lowered to 1.85 bits/symbol}@}; it is {@{still far from the theoretical limit}@} because {@{the probabilities of the symbols are different from negative powers of two}@}. <!--SR:!2025-11-23,277,330!2028-08-07,1048,350!2028-07-22,1035,350!2025-10-27,254,330!2025-12-11,292,330!2025-11-12,268,330!2025-11-24,278,330!2025-12-13,294,330!2025-10-24,252,330!2025-11-20,275,330!2027-05-04,674,330!2025-12-07,289,330!2025-11-20,275,330!2028-11-01,1116,350!2025-12-08,290,330!2028-07-17,1030,350!2026-10-19,504,310!2025-11-09,266,330!2025-11-15,271,330!2025-10-18,251,330!2027-06-29,708,330-->

The technique works by {@{creating a [binary tree](binary%20tree.md) of nodes}@}. These can be stored in {@{a regular [array](array%20(data%20type).md)}@}, the size of which {@{depends on the number of symbols, $n$}@}. A node can be {@{either a [leaf node](tree%20(abstract%20data%20type).md#terminology) or an [internal node](tree%20(abstract%20data%20type).md#terminology)}@}. Initially, {@{all nodes are leaf nodes}@}, which contain {@{the __symbol__ itself, the __weight__ \(frequency of appearance\) of the symbol and optionally, a link to a __parent__ node which makes it easy to read the code \(in reverse\) starting from a leaf node}@}. Internal nodes {@{contain a __weight__, links to __two child nodes__ and an optional link to a __parent__ node}@}. As {@{a common convention}@}, {@{bit '0' represents following the left child and bit '1' represents following the right child}@}. A finished tree has {@{up to $n$ leaf nodes and $n-1$ internal nodes}@}. {@{A Huffman tree that omits unused symbols}@} {@{produces the most optimal code lengths}@}. <!--SR:!2028-09-28,1089,350!2025-10-17,250,330!2025-11-02,259,330!2025-11-19,274,330!2027-05-14,682,330!2026-04-03,351,290!2025-11-14,270,330!2028-11-21,1132,350!2025-11-21,276,330!2028-08-11,1051,350!2025-12-02,285,330!2025-11-01,259,330-->

The process begins with {@{the leaf nodes containing the probabilities of the symbol they represent}@}. Then, the process {@{takes the two nodes with smallest probability}@}, and {@{creates a new internal node having these two nodes as children}@}. The weight of the new node is {@{set to the sum of the weight of the children}@}. We then {@{apply the process again, on the new internal node and on the remaining nodes \(i.e., we exclude the two leaf nodes\)}@}, we {@{repeat this process until only one node remains}@}, which is {@{the root of the Huffman tree}@}. <!--SR:!2028-10-31,1116,350!2025-11-20,275,330!2028-11-11,1124,350!2025-12-13,294,330!2027-11-30,824,330!2025-11-07,263,330!2025-11-25,279,330-->

{@{The simplest construction algorithm}@} uses {@{a [priority queue](priority%20queue.md) where the node with lowest probability is given highest priority}@}: <!--SR:!2028-08-31,1067,350!2026-09-22,482,310-->

1. Create {@{a leaf node for each symbol}@} and {@{add it to the priority queue}@}.
2. While {@{there is more than one node}@} in the queue:
    1. {@{Remove the two nodes of highest priority \(lowest probability\)}@} from the queue
    2. Create {@{a new internal node with these two nodes as children}@} and with {@{probability equal to the sum of the two nodes' probabilities}@}.
    3. {@{Add the new node}@} to the queue.
3. The remaining node is {@{the root node and the tree is complete}@}. <!--SR:!2025-10-30,257,330!2027-11-13,774,330!2025-10-17,250,330!2028-10-26,1111,350!2028-09-06,1071,350!2025-11-29,282,330!2025-10-23,255,330!2025-12-08,290,330-->

Since {@{efficient priority queue data structures require O\(log _n_\) time per insertion}@}, and {@{a tree with _n_ leaves has 2<!-- markdown separator -->_n_<!-- markdown separator -->−1 nodes}@}, this algorithm operates in {@{O\(_n_ log _n_\) time, where _n_ is the number of symbols}@}. <!--SR:!2028-08-10,1050,350!2028-08-14,1053,350!2026-09-20,484,310-->

If {@{the symbols are sorted by probability}@}, there is {@{a [linear-time](time%20complexity.md#linear%20time) \(O\(_n_\)\) method to create a Huffman tree using two [queues](queue%20(abstract%20data%20type).md)}@}, the first one {@{containing the initial weights \(along with pointers to the associated leaves\), and combined weights \(along with pointers to the trees\) being put in the back of the second queue}@}. This assures that {@{the lowest weight is always kept at the front of one of the two queues}@}: <!--SR:!2025-10-20,252,330!2028-08-28,1065,350!2026-10-22,506,310!2025-11-07,264,330-->

1. Start with {@{as many leaves as there are symbols}@}.
2. Enqueue {@{all leaf nodes into the first queue}@} \(by {@{probability in increasing order so that the least likely item is in the head of the queue}@}\).
3. While {@{there is more than one node}@} in the queues:
    1. Dequeue {@{the two nodes with the lowest weight by examining the fronts of both queues}@}. (annotation: It is possible that {@{the two nodes are from the same queue}@}, so {@{the first two nodes of each queue should be inspected}@}.)
    2. Create {@{a new internal node, with the two just-removed nodes as children \(either node can be either child\)}@} and {@{the sum of their weights as the new weight}@}.
    3. Enqueue {@{the new node into the rear of}@} the second queue.
4. The remaining node is {@{the root node; the tree has now been generated}@}. <!--SR:!2025-10-21,253,330!2025-10-31,257,330!2025-12-07,289,330!2025-10-24,251,330!2025-11-29,282,330!2025-10-18,251,330!2026-10-21,505,310!2027-02-25,562,310!2027-05-09,678,330!2028-10-25,1111,350!2025-12-08,290,330-->

Once {@{the Huffman tree has been generated}@}, it is {@{traversed to generate a dictionary which maps the symbols to binary codes as follows}@}: <!--SR:!2025-10-28,255,330!2027-12-10,831,330-->

1. {@{Start with current node}@} set to the root.
2. If {@{node is not a leaf node}@}, label {@{the edge to the left child as _0_ and the edge to the right child as _1_}@}. Repeat {@{the process at both the left child and the right child}@}. <!--SR:!2025-11-27,281,330!2025-11-06,262,330!2028-09-16,1079,350!2025-11-11,266,330-->

{@{The final encoding of any symbol}@} is then read by {@{a concatenation of the labels on the edges along the path from the root node to the symbol}@}. <!--SR:!2025-10-21,253,330!2027-02-26,564,310-->

In many cases, {@{time complexity is not very important in the choice of algorithm here}@}, since {@{_n_ here is the number of symbols in the alphabet}@}, which is {@{typically a very small number \(compared to the length of the message to be encoded\)}@}; whereas {@{complexity analysis concerns the behavior when _n_ grows to be very large}@}. <!--SR:!2025-10-19,251,330!2025-12-12,293,330!2025-11-09,264,330!2027-06-08,702,330-->

It is generally beneficial to {@{minimize the variance of codeword length}@}. For example, {@{a communication buffer}@} receiving {@{Huffman-encoded data may need to be larger}@} to {@{deal with especially long symbols if the tree is especially unbalanced}@}. To {@{minimize variance}@}, {@{simply break ties between queues by choosing the item in the first queue}@}. This modification will {@{retain the mathematical optimality of the Huffman coding}@} while {@{both minimizing variance and minimizing the length of the longest character code}@}. <!--SR:!2025-10-25,254,330!2028-01-09,818,330!2025-11-12,268,330!2025-11-16,272,330!2026-12-08,544,310!2025-12-11,292,330!2026-11-23,529,310!2025-11-08,24,371-->

### decompression

Generally speaking, {@{the process of decompression}@} is {@{simply a matter of translating the stream of prefix codes to individual byte values}@}, usually by {@{traversing the Huffman tree node by node as each bit is read from the input stream}@} \(reaching a leaf node {@{necessarily terminates the search for that particular byte value}@}\). Before {@{this can take place}@}, however, {@{the Huffman tree must be somehow reconstructed}@}. In {@{the simplest case, where character frequencies are fairly predictable}@}, the tree can {@{be preconstructed \(and even statistically adjusted on each compression cycle\)}@} and thus {@{reused every time, at the expense of at least some measure of compression efficiency}@}. Otherwise, {@{the information to reconstruct the tree must be sent a priori}@}. A naive approach might be to {@{prepend the frequency count of each character to the compression stream}@}. Unfortunately, {@{the overhead in such a case could amount to several kilobytes}@}, so {@{this method has little practical use}@}. If {@{the data is compressed using [canonical encoding](canonical%20Huffman%20code.md)}@}, the compression model can be {@{precisely reconstructed with just $B\cdot 2^{B}$ bits of information \(where _B_ is the number of bits per symbol\)}@}. Another method is {@{to simply prepend the Huffman tree, bit by bit, to the output stream}@}. For example, assuming that {@{the value of 0 represents a parent node and 1 a leaf node}@}, whenever {@{the latter is encountered}@} {@{the tree building routine simply reads the next 8 bits to determine the character value of that particular leaf}@}. The process {@{continues recursively until the last leaf node is reached}@}; at that point, {@{the Huffman tree will thus be faithfully reconstructed}@}. The overhead using such a method {@{ranges from roughly 2 to 320 bytes \(assuming an 8-bit alphabet\)}@}. {@{Many other techniques}@} are possible as well. In any case, since {@{the compressed data can include unused "trailing bits"}@} the decompressor {@{must be able to determine when to stop producing output}@}. This can be accomplished by {@{either transmitting the length of the decompressed data along with the compression model}@} or {@{by defining a special code symbol to signify the end of input \(the latter method can adversely affect code length optimality, however\)}@}. <!--SR:!2025-10-20,252,330!2025-12-01,284,330!2026-10-04,492,310!2028-09-10,1075,350!2028-11-04,1119,350!2025-11-11,267,330!2028-10-14,1102,350!2025-11-22,276,330!2028-02-21,888,330!2025-11-10,265,330!2027-05-13,682,330!2025-11-18,273,330!2025-11-14,270,330!2026-10-05,493,310!2026-08-20,469,310!2025-10-26,254,330!2025-11-09,265,330!2028-07-29,1040,350!2027-08-17,746,330!2025-11-04,260,330!2025-11-08,264,330!2027-08-24,759,330!2028-10-19,1106,350!2025-11-19,274,330!2025-11-18,273,330!2027-08-19,755,330!2025-11-13,269,330-->

## main properties

{@{The probabilities used}@} can be {@{generic ones for the application domain that are based on average experience, or they can be the actual frequencies found in the text being compressed}@}. This requires that {@{a [frequency table](frequency%20(statistics).md) must be stored with the compressed text}@}. See {@{the [Decompression](#decompression) section above}@} for {@{more information about the various techniques employed for this purpose}@}. <!--SR:!2025-10-23,255,330!2025-12-02,285,330!2027-07-11,725,330!2028-01-20,863,330!2028-11-06,1120,350-->

### optimality

- see: [arithmetic coding § Huffman coding](arithmetic%20coding.md#Huffman%20coding)

Huffman's original algorithm is {@{optimal for a symbol-by-symbol coding with a known input probability distribution, i.e., separately encoding unrelated symbols in such a data stream}@}. However, it is {@{not optimal when the symbol-by-symbol restriction is dropped}@}, or {@{when the [probability mass functions](probability%20mass%20function.md) are unknown}@}. Also, if {@{symbols are not [independent and identically distributed](independent%20and%20identically%20distributed%20random%20variables.md)}@}, {@{a single code may be insufficient for optimality}@}. {@{Other methods such as [arithmetic coding](arithmetic%20coding.md)}@} often {@{have better compression capability}@}. <!--SR:!2025-11-10,266,330!2028-08-24,1061,350!2027-10-24,795,330!2025-11-21,276,330!2025-11-30,283,330!2025-12-08,290,330!2025-11-28,281,330-->

Although {@{both aforementioned methods can combine an arbitrary number of symbols}@} for {@{more efficient coding and generally adapt to the actual input statistics}@}, {@{arithmetic coding does so without significantly increasing its computational or algorithmic complexities}@} \(though {@{the simplest version is slower and more complex than Huffman coding}@}\). {@{Such flexibility}@} is {@{especially useful when input probabilities are not precisely known or vary significantly within the stream}@}. However, Huffman coding is {@{usually faster}@} and arithmetic coding was {@{historically a subject of some concern over [patent](patent.md) issues}@}. Thus {@{many technologies have historically avoided arithmetic coding in favor of Huffman and other prefix coding techniques}@}. As of {@{mid-2010}@}, {@{the most commonly used techniques for this alternative to Huffman coding}@} have {@{passed into the public domain as the early patents have expired}@}. <!--SR:!2028-10-07,1096,350!2028-08-30,1066,350!2028-10-30,1115,350!2028-11-13,1125,350!2027-10-24,810,330!2028-08-22,1060,350!2025-10-26,254,330!2025-10-22,254,330!2027-04-11,592,310!2027-07-09,716,330!2025-11-08,264,330!2028-07-28,1040,350-->

For {@{a set of symbols with a uniform probability distribution and a number of members which is a [power of two](power%20of%20two.md)}@}, Huffman coding is {@{equivalent to simple binary [block encoding](block%20code.md), e.g., [ASCII](ASCII.md) coding}@}. This reflects the fact that {@{compression is not possible with such an input, no matter what the compression method}@}, i.e., {@{doing nothing to the data is the optimal thing to do}@}. <!--SR:!2025-11-23,277,330!2028-11-10,1123,350!2027-06-08,632,310!2026-02-12,123,387-->

Huffman coding is {@{optimal among all methods}@} in any case where {@{each input symbol is a known independent and identically distributed random variable having a probability that is [dyadic](dyadic%20distribution.md)}@}. {@{Prefix codes, and thus Huffman coding in particular}@}, tend to {@{have inefficiency on small alphabets}@}, where {@{probabilities often fall between these optimal \(dyadic\) points}@}. {@{The worst case for Huffman coding}@} can happen when {@{the probability of the most likely symbol far exceeds 2<sup>−1</sup> = 0.5}@}, making {@{the upper limit of inefficiency unbounded}@}. <!--SR:!2025-10-20,252,330!2025-12-06,288,330!2025-12-07,289,330!2028-01-09,856,330!2028-10-12,1100,350!2025-11-10,266,330!2028-08-12,1051,350!2025-11-29,282,330-->

There are {@{two related approaches for getting around this particular inefficiency while still using Huffman coding}@}. {@{Combining a fixed number of symbols together \("blocking"\)}@} often {@{increases \(and never decreases\) compression}@}. As {@{the size of the block approaches infinity}@}, Huffman coding {@{theoretically approaches the entropy limit, i.e., optimal compression}@}.<sup>[\[6\]](#^ref-6)</sup> However, {@{blocking arbitrarily large groups of symbols is impractical}@}, as {@{the complexity of a Huffman code is linear in the number of possibilities to be encoded}@}, a number that is {@{exponential in the size of a block}@}. This {@{limits the amount of blocking that is done in practice}@}. <!--SR:!2025-10-29,256,330!2025-12-12,293,330!2027-10-28,762,330!2028-08-19,1058,350!2025-11-16,271,330!2027-09-26,776,330!2025-11-24,278,330!2025-11-14,270,330!2025-11-02,260,330-->

{@{A practical alternative, in widespread use}@}, is {@{[run-length encoding](run-length%20encoding.md)}@}. This technique {@{adds one step in advance of entropy coding}@}, specifically {@{counting \(runs\) of repeated symbols, which are then encoded}@}. For {@{the simple case of [Bernoulli processes](Bernoulli%20process.md)}@}, {@{[Golomb coding](Golomb%20coding.md)}@} is {@{optimal among prefix codes for coding run length}@}, a fact proved {@{via the techniques of Huffman coding}@}.<sup>[\[7\]](#^ref-7)</sup> A similar approach is taken by {@{fax machines using [modified Huffman coding](modified%20Huffman%20coding.md)}@}. However, run-length coding is {@{not as adaptable to as many input types as other compression technologies}@}. <!--SR:!2025-12-12,293,330!2025-11-11,267,330!2028-09-03,1069,350!2025-12-08,290,330!2027-04-16,660,330!2028-10-18,1105,350!2027-11-21,783,330!2025-12-07,289,330!2026-08-14,455,310!2025-12-06,288,330-->

## variations

{@{Many variations of Huffman coding}@} exist,<sup>[\[8\]](#^ref-8)</sup> some of which {@{use a Huffman-like algorithm}@}, and others of which {@{find optimal prefix codes \(while, for example, putting different restrictions on the output\)}@}. Note that, {@{in the latter case}@}, the method {@{need not be Huffman-like, and, indeed, need not even be [polynomial time](time%20complexity.md#polynomial%20time)}@}. <!--SR:!2025-10-26,254,330!2028-09-13,1077,350!2028-09-05,1070,350!2025-12-12,293,330!2028-08-27,1063,350-->

### _n_-ary Huffman coding

{@{The ___n_-ary Huffman__ algorithm}@} uses {@{the {0, 1,..., _n_ − 1} alphabet to encode message and build an _n_-ary tree}@}. This approach was {@{considered by Huffman in his original paper}@}. The same algorithm applies as {@{for binary \($n=2$\) codes}@}, except {@{that the _n_ least probable symbols are taken together, instead of just the 2 least probable}@}. Note that for {@{_n_ greater than 2}@}, {@{not all sets of source words can properly form an _n_-ary tree for Huffman coding}@}. In these cases, {@{additional 0-probability place holders must be added}@}. This is because {@{the tree must form an _n_ to 1 contractor}@};<!-- <sup>\[_[clarification needed](https://en.wikipedia.org/wiki/Wikipedia:Please%20clarify)_\]</sup> --> for {@{binary coding, this is a 2 to 1 contractor}@}, and {@{any sized set can form such a contractor}@}. If {@{the number of source words is congruent to 1 modulo _n_<!-- markdown separator -->−1}@}, then {@{the set of source words will form a proper Huffman tree}@}. <!--SR:!2028-08-06,1047,350!2028-09-14,1078,350!2025-12-11,292,330!2025-10-30,256,330!2025-11-26,280,330!2027-07-15,728,330!2025-12-08,290,330!2025-11-16,272,330!2025-11-17,272,330!2025-11-26,280,330!2025-12-07,289,330!2028-08-18,1056,350!2025-12-01,284,330-->

### adaptive Huffman coding

{@{A variation called __[adaptive Huffman coding](adaptive%20Huffman%20coding.md)__}@} involves {@{calculating the probabilities dynamically based on recent actual frequencies in the sequence of source symbols}@}, and {@{changing the coding tree structure to match the updated probability estimates}@}. It is {@{used rarely in practice}@}, since {@{the cost of updating the tree makes it slower than optimized [adaptive arithmetic coding](arithmetic%20coding.md#adaptive%20arithmetic%20coding)}@}, which is {@{more flexible and has better compression}@}. <!--SR:!2025-11-15,271,330!2025-10-17,249,330!2025-12-13,294,330!2025-12-08,290,330!2025-11-03,261,330!2025-10-19,251,330-->

### Huffman template algorithm

Most often, {@{the weights}@} used in implementations of Huffman coding represent {@{numeric probabilities}@}, but {@{the algorithm given above does not require this}@}; it requires {@{only that the weights form a [totally ordered](total%20order.md) [commutative monoid](monoid.md#commutative%20monoid)}@}, meaning {@{a way to order weights and to add them}@}. {@{The __Huffman template algorithm__}@} enables one to {@{use any kind of weights \(costs, frequencies, pairs of weights, non-numerical weights\)}@} and {@{one of many combining methods \(not just addition\)}@}. Such algorithms can {@{solve other minimization problems}@}, such as {@{minimizing $\max _{i}\left[w_{i}+\mathrm {length} \left(c_{i}\right)\right]$}@}, a problem first {@{applied to circuit design}@}. <!--SR:!2025-12-13,294,330!2028-03-03,1118,350!2025-12-12,293,330!2025-11-10,267,330!2025-11-30,283,330!2025-12-12,293,330!2026-10-06,494,310!2025-11-03,260,330!2026-08-19,470,310!2026-09-12,476,310!2025-10-25,253,330-->

### length-limited Huffman coding/minimum variance Huffman coding

{@{__Length-limited Huffman coding__}@} is {@{a variant where the goal is still to achieve a minimum weighted path length}@}, but {@{there is an additional restriction that the length of each codeword must be less than a given constant}@}. {@{The [package-merge algorithm](package-merge%20algorithm.md)}@} {@{solves this problem with a simple [greedy](greedy%20algorithm.md) approach very similar to that used by Huffman's algorithm}@}. Its time complexity is {@{$O(nL)$, where $L$ is the maximum length of a codeword}@}. No algorithm is {@{known to solve this problem in [$O(n)$ or $O(n\log n)$](big%20O%20notation.md#orders%20of%20common%20functions) time}@}, unlike {@{the presorted and unsorted conventional Huffman problems, respectively}@}. <!--SR:!2028-09-10,1074,350!2027-04-17,661,330!2025-11-12,267,330!2026-09-07,474,310!2026-10-11,499,310!2027-08-13,742,330!2028-11-07,1121,350!2027-10-28,798,330-->

### Huffman coding with unequal letter costs

In {@{the standard Huffman coding problem}@}, it is assumed that {@{each symbol in the set that the code words are constructed from has an equal cost to transmit}@}: {@{a code word whose length is _N_ digits will always have a cost of _N_, no matter how many of those digits are 0s, how many are 1s, etc.}@} When {@{working under this assumption}@}, {@{minimizing the total cost of the message and minimizing the total number of digits}@} are the same thing. <!--SR:!2025-11-21,276,330!2027-08-09,747,330!2025-11-25,279,330!2025-10-21,253,330!2025-11-13,269,330-->

{@{_Huffman coding with unequal letter costs_}@} is {@{the generalization without this assumption}@}: {@{the letters of the encoding alphabet may have non-uniform lengths, due to characteristics of the transmission medium}@}. An example is {@{the encoding alphabet of [Morse code](Morse%20code.md)}@}, where {@{a 'dash' takes longer to send than a 'dot', and therefore the cost of a dash in transmission time is higher}@}. The goal is {@{still to minimize the weighted average codeword length}@}, but it is no longer {@{sufficient just to minimize the number of symbols used by the message}@}. No algorithm is {@{known to solve this in the same manner or with the same efficiency as conventional Huffman coding}@}, though {@{it has been solved by [Richard M. Karp](Richard%20M.%20Karp.md)}@}<sup>[\[9\]](#^ref-9)</sup> whose solution {@{has been refined for the case of integer costs by Mordecai J. Golin}@}.<sup>[\[10\]](#^ref-10)</sup> <!--SR:!2025-12-13,294,330!2025-11-22,276,330!2027-07-06,721,330!2025-11-18,273,330!2025-11-28,281,330!2027-05-30,694,330!2028-09-02,1068,350!2025-11-10,219,270!2027-06-30,682,290!2026-12-27,559,310-->

### Optimal alphabetic binary trees \(Hu–Tucker coding\)

In {@{the standard Huffman coding problem}@}, it is assumed that {@{any codeword can correspond to any input symbol}@}. In {@{the alphabetic version}@}, {@{the alphabetic order of inputs and outputs must be identical}@}. Thus, for example, {@{$A=\left\{a,b,c\right\}$}@} could not be assigned {@{code $H\left(A,C\right)=\left\{00,1,01\right\}$}@}, but instead should be {@{assigned either $H\left(A,C\right)=\left\{00,01,1\right\}$ or $H\left(A,C\right)=\left\{0,10,11\right\}$}@}. This is also known as {@{the __Hu–Tucker__ problem}@}, after {@{[T. C. Hu](T.%20C.%20Hu.md) and [Alan Tucker](Alan%20Tucker.md)}@}, the authors of {@{the paper presenting the first [$O(n\log n)$-time](time%20complexity.md#quasilinear%20time) solution to this optimal binary alphabetic problem}@},<sup>[\[11\]](#^ref-11)</sup> which has {@{some similarities to Huffman algorithm, but is not a variation of this algorithm}@}. {@{A later method, the [Garsia–Wachs algorithm](Garsia–Wachs%20algorithm.md)}@} of {@{[Adriano Garsia](Adriano%20Garsia.md) and [Michelle L. Wachs](Michelle%20L.%20Wachs.md) \(1977\)}@}, uses {@{simpler logic to perform the same comparisons in the same total time bound}@}. {@{These optimal alphabetic binary trees}@} are often {@{used as [binary search trees](binary%20search%20tree.md)}@}.<sup>[\[12\]](#^ref-12)</sup> <!--SR:!2025-11-15,270,330!2025-11-30,283,330!2025-11-13,269,330!2025-11-26,280,330!2025-10-20,252,330!2025-11-20,275,330!2028-10-20,1106,350!2025-11-29,282,330!2025-12-11,292,330!2026-02-13,315,290!2025-11-17,272,330!2026-10-07,494,310!2026-10-02,462,270!2027-06-27,679,290!2027-07-01,720,330!2028-10-02,1092,350-->

### the canonical Huffman code

- see: [canonical Huffman code](canonical%20Huffman%20code.md)

If {@{weights corresponding to the alphabetically ordered inputs are in numerical order}@}, the Huffman code has {@{the same lengths as the optimal alphabetic code}@}, which {@{can be found from calculating these lengths}@}, rendering {@{Hu–Tucker coding unnecessary}@}. {@{The code resulting from numerically \(re-\)ordered input}@} is sometimes called {@{the _canonical Huffman code_}@} and is {@{often the code used in practice, due to ease of encoding/decoding}@}. {@{The technique for finding this code}@} is sometimes called {@{__Huffman–Shannon–Fano coding__}@}, since {@{it is optimal like Huffman coding, but alphabetic in weight probability}@}, like {@{[Shannon–Fano coding](Shannon–Fano%20coding.md)}@}. {@{The Huffman–Shannon–Fano code}@} corresponding to the example is $\{000,001,01,10,11\}$, which, having {@{the same codeword lengths as the original solution, is also optimal}@}. But {@{in _canonical Huffman code_}@}, the result is $\{110,111,00,01,10\}$. (annotation: The difference between these two is that in the former, {@{the alphabets are \(re-\)assigned codes in decreasing bit lengths, and then in alphabetical order}@}. In the latter, {@{the alphabets are \(re-\)assigned codes in increasing bit lengths, and then in alphabetical order}@}.) <!--SR:!2027-04-17,665,330!2025-12-08,290,330!2027-02-26,574,310!2028-02-23,889,330!2025-11-24,278,330!2025-10-23,255,330!2025-11-18,273,330!2025-11-19,274,330!2027-08-30,764,330!2026-05-21,358,290!2025-11-06,262,330!2025-11-19,274,330!2026-04-16,343,290!2027-05-18,685,330!2031-06-08,2102,329!2026-10-08,502,329-->

## applications

{@{[Arithmetic coding](arithmetic%20coding.md) and Huffman coding}@} produce {@{equivalent results — achieving entropy}@} — when {@{every symbol has a probability of the form 1/2<sup>_k_</sup>}@}. In other circumstances, {@{arithmetic coding can offer better compression than Huffman coding}@} because — {@{intuitively — its "code words" can have effectively non-integer bit lengths}@}, whereas {@{code words in prefix codes such as Huffman codes can only have an integer number of bits}@}. Therefore, {@{a code word of length _k_ only}@} {@{optimally matches a symbol of probability 1/2<sup>_k_</sup> and other probabilities are not represented optimally}@}; whereas {@{the code word length in arithmetic coding}@} can be {@{made to exactly match the true probability of the symbol}@}. This difference is {@{especially striking for small alphabet sizes}@}.<!-- <sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> --> <!--SR:!2028-11-02,1117,350!2028-11-19,1130,350!2025-11-27,281,330!2025-12-13,294,330!2027-08-15,751,330!2028-10-15,1102,350!2025-10-25,252,330!2027-06-19,708,330!2025-11-14,270,330!2025-12-07,289,330!2025-11-07,263,330-->

{@{Prefix codes}@} nevertheless {@{remain in wide use}@} because of {@{their simplicity, high speed, and [lack of patent coverage](arithmetic%20coding.md#history%20and%20patents)}@}. They are often {@{used as a "back-end" to other compression methods}@}. {@{[Deflate](deflate.md) \([PKZIP](PKZIP.md)'s algorithm\)}@} and {@{multimedia [codecs](codec.md) such as [JPEG](JPEG.md) and [MP3](MP3.md)}@} have {@{a front-end model and [quantization](quantization%20(signal%20processing).md) followed by the use of prefix codes}@}; these are {@{often called "Huffman codes"}@} even though {@{most applications use pre-defined variable-length codes rather than codes designed using Huffman's algorithm}@}. <!--SR:!2025-11-09,265,330!2028-07-26,1038,350!2028-09-22,1084,350!2028-08-17,1055,350!2025-11-28,281,330!2025-12-07,289,330!2026-11-04,516,310!2028-07-31,1042,350!2028-10-17,1103,350-->

## references

> ![Wikimedia Commons logo](../../archives/Wikimedia%20Commons/Commons-logo.svg)
>
> Wikimedia Commons has media related to ___[Huffman coding](https://commons.wikimedia.org/wiki/Category:Huffman%20coding)___.

This text incorporates [content](https://en.wikipedia.org/wiki/Huffman_coding) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. [Huffman, D.](David%20A.%20Huffman.md) \(1952\). ["A Method for the Construction of Minimum-Redundancy Codes"](http://compression.ru/download/articles/huff/huffman_1952_minimum-redundancy-codes.pdf) \(PDF\). _[Proceedings of the IRE](Proceedings%20of%20the%20IEEE.md)_. __40__ \(9\): 1098–1101. [doi](digital%20object%20identifier.md):[10.1109/JRPROC.1952.273898](https://doi.org/10.1109%2FJRPROC.1952.273898). <a id="^ref-1"></a>^ref-1
2. [Van Leeuwen, Jan](Jan%20van%20Leeuwen.md) \(1976\). ["On the construction of Huffman trees"](http://www.staff.science.uu.nl/~leeuw112/huffman.pdf) \(PDF\). _ICALP_: 382–410. Retrieved 2014-02-20. <a id="^ref-2"></a>^ref-2
3. Ze-Nian Li; Mark S. Drew; Jiangchuan Liu \(2014-04-09\). [_Fundamentals of Multimedia_](https://books.google.com/books?id=R6vBBAAAQBAJ). Springer Science & Business Media. [ISBN](ISBN.md) [978-3-319-05290-8](https://en.wikipedia.org/wiki/Special:BookSources/978-3-319-05290-8). <a id="^ref-3"></a>^ref-3
4. [J. Duda, K. Tahboub, N. J. Gadil, E. J. Delp, _The use of asymmetric numeral systems as an accurate replacement for Huffman coding_](https://ieeexplore.ieee.org/document/7170048), Picture Coding Symposium, 2015. <a id="^ref-4"></a>^ref-4
5. Huffman, Ken \(1991\). ["Profile: David A. Huffman: Encoding the "Neatness" of Ones and Zeroes"](http://www.huffmancoding.com/my-uncle/scientific-american). _[Scientific American](Scientific%20American.md)_: 54–58. <a id="^ref-5"></a>^ref-5
6. Gribov, Alexander \(2017-04-10\). "Optimal Compression of a Polyline with Segments and Arcs". [arXiv](ArXiv.md):[1604.07476](https://arxiv.org/abs/1604.07476) \[[cs.CG](https://arxiv.org/archive/cs.CG)\]. <a id="^ref-6"></a>^ref-6
7. Gallager, R.G.; van Voorhis, D.C. \(1975\). "Optimal source codes for geometrically distributed integer alphabets". _[IEEE Transactions on Information Theory](IEEE%20Transactions%20on%20Information%20Theory.md)_. __21__ \(2\): 228–230. [doi](digital%20object%20identifier.md):[10.1109/TIT.1975.1055357](https://doi.org/10.1109%2FTIT.1975.1055357). <a id="^ref-7"></a>^ref-7
8. Abrahams, J. \(1997-06-11\). "Code and parse trees for lossless source encoding". Written at Arlington, VA, USA. _Proceedings. Compression and Complexity of SEQUENCES 1997 \(Cat. No.97TB100171\)_. Division of Mathematics, Computer & Information Sciences, [Office of Naval Research](Office%20of%20Naval%20Research.md) \(ONR\). Salerno: [IEEE](Institute%20of%20Electrical%20and%20Electronics%20Engineers.md). pp. 145–171. [CiteSeerX](CiteSeerX.md) [10.1.1.589.4726](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.589.4726). [doi](digital%20object%20identifier.md):[10.1109/SEQUEN.1997.666911](https://doi.org/10.1109%2FSEQUEN.1997.666911). [ISBN](ISBN.md) [0-8186-8132-2](https://en.wikipedia.org/wiki/Special:BookSources/0-8186-8132-2). [S2CID](Semantic%20Scholar.md#S2CID) [124587565](https://api.semanticscholar.org/CorpusID:124587565). <a id="^ref-8"></a>^ref-8
9. [Karp, Richard M.](Richard%20M.%20Karp.md) \(1961-01-31\). ["Minimum-redundancy coding for the discrete noiseless channel"](https://ieeexplore.ieee.org/document/1057615?arnumber=1057615). _IRE Transactions on Information Theory_. __7__ \(1\). IEEE: 27–38. [doi](digital%20object%20identifier.md):[10.1109/TIT.1961.1057615](https://doi.org/10.1109%2FTIT.1961.1057615) – via IEEE. <a id="^ref-9"></a>^ref-9
10. Golin, Mordekai J. \(January 1998\). ["A Dynamic Programming Algorithm for Constructing Optimal Prefix-Free Codes with Unequal Letter Costs"](https://page.mi.fu-berlin.de/rote/Papers/pdf/A+dynamic+programming+algorithm+for+constructing+optimal+prefix-free+codes+for+unequal+letter+costs.pdf) \(PDF\). _IEEE Transactions on Information Theory_. __44__ \(5\) \(published 1998-09-01\): 1770–1781. [doi](digital%20object%20identifier.md):[10.1109/18.705558](https://doi.org/10.1109%2F18.705558). [S2CID](Semantic%20Scholar.md#S2CID) [2265146](https://api.semanticscholar.org/CorpusID:2265146). Retrieved 2024-09-10. <a id="^ref-10"></a>^ref-10
11. [Hu, T. C.](T.%20C.%20Hu.md); [Tucker, A. C.](Alan%20Tucker.md) \(1971\). "Optimal Computer Search Trees and Variable-Length Alphabetical Codes". _SIAM Journal on Applied Mathematics_. __21__ \(4\): 514. [doi](digital%20object%20identifier.md):[10.1137/0121057](https://doi.org/10.1137%2F0121057). [JSTOR](JSTOR.md) [2099603](https://www.jstor.org/stable/2099603). <a id="^ref-11"></a>^ref-11
12. [Knuth, Donald E.](Donald%20Knuth.md) \(1998\), "Algorithm G \(Garsia–Wachs algorithm for optimum binary trees\)", _The Art of Computer Programming, Vol. 3: Sorting and Searching_ \(2nd ed.\), Addison–Wesley, pp. 451–453. See also History and bibliography, pp. 453–454. <a id="^ref-12"></a>^ref-12

## bibliography

- [Thomas H. Cormen](Thomas%20H.%20Cormen.md), [Charles E. Leiserson](Charles%20E.%20Leiserson.md), [Ronald L. Rivest](Ron%20Rivest.md), and [Clifford Stein](Clifford%20Stein.md). _[Introduction to Algorithms](Introduction%20to%20Algorithms.md)_, Second Edition. MIT Press and McGraw-Hill, 2001. [ISBN](ISBN.md) [0-262-03293-7](https://en.wikipedia.org/wiki/Special:BookSources/0-262-03293-7). Section 16.3, pp. 385–392.

## external links

- [Huffman coding in various languages on Rosetta Code](http://rosettacode.org/wiki/Huffman_coding)
- [Huffman codes \(python implementation\)](https://gist.github.com/jasonrdsouza/1c9c895f43497d15eb2e)
- [A visualization of Huffman coding](https://www.tinyray.com/huffman)
