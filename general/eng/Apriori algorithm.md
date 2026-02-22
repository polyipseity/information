---
aliases:
  - Apriori algorithm
tags:
  - flashcard/active/general/eng/Apriori_algorithm
  - language/in/English
---

# Apriori algorithm

## overview

To understand {@{the Apriori algorithm}@}, notice that for {@{any database and two item sets _A_ and _B_ in the database where $A \subseteq B$}@}, then {@{$\operatorname{supp}(A) \ge \operatorname{supp}(B)$}@}. This is easily seen by considering that {@{any transaction that satisfies _B_ contains all the items of _B_}@}, so must {@{also satisfy _A_, as it contains all the items of _A_ as a subset of _B_}@}. This is called the {@{_downward closure lemma_}@}. <!--SR:!2030-01-25,1509,310!2027-10-19,1022,339!2027-02-01,818,330!2026-04-24,99,386!2026-04-23,98,386!2026-04-22,97,386-->

Then the Apriori algorithm uses a {@{"bottom up"}@} approach. The frequent sets {@{start from one item and then are extended one item at a time, called _candidate generation_}@}. The generation can cover all possible frequent sets because of the downward closure lemma. Then, {@{the candidates are tested against the support threshold and become the new frequent sets that are one item longer than the last generation}@}. Repeat this process until {@{there are no more candidates}@}. The output is {@{all frequent sets in all generations}@}. <!--SR:!2027-05-04,895,339!2026-10-06,728,330!2028-04-18,1136,310!2028-12-25,1395,359!2026-07-18,668,330-->

Filtering the candidate, called the {@{_count step_}@}, is obvious, but candidate generation is not as obvious. For candidate generation, there are two steps: {@{_join step_ and _prune step_}@}. <!--SR:!2027-01-13,753,336!2029-08-09,1543,383-->

For _join step_, one first consider, from the previous generation of frequent sets, all possible pairs of sets that {@{have a [symmetric difference](symmetric%20difference.md) of size 2, i.e. the set are the same except for 1 item, like $\set{1, 2, 3}$ and $\set{1, 20, 3}$}@}. Then, for each pair, {@{the union of the two sets is a new _possible_ candidate set, like $\set{1, 2, 3, 20}$ using the same example}@}. <!--SR:!2027-01-25,752,319!2027-01-30,820,330-->

For _prune step_, confirm the _possible_ candidate sets. For each _possible_ candidate set, {@{check that all subsets that are one item less in size than the possible candidate set are in the previous generation of frequent sets, like checking $\set{1, 2, 3}, \set{1, 2, 20}, \set{1, 3, 20}, \set{2, 3, 20}$ using the same example}@}. One may note that {@{two subsets are guaranteed to be in the previous generation frequent sets because of how we generated the _possible_ candidate set, so we can skip checking the two subsets}@}. After checking, if the check passes, {@{it is part of the candidate for the new generation, otherwise it is not}@}. <!--SR:!2029-03-26,1363,310!2027-05-02,894,339!2027-08-07,968,339-->

Note that the above is a slower variant of the Apriori algorithm. There is a much more common variant that is also faster, but {@{that additionally requires all sets above be lexicographically ordered sets}@}. With this additional requirement in mind, the difference is in {@{the join step}@}. First, we define the _prefix set_ of an ordered set of size _n_ as {@{the first _n_−1 items of the ordered set, itself in an ordered set}@}. Now the join step instead becomes {@{considering all possible pairs of sets that have the same prefix set, then the union of each pair is a _possible_ candidate set}@}. <!--SR:!2026-04-22,602,336!2027-10-17,986,356!2026-05-31,628,336!2026-08-14,685,336-->

If we consider each set is directionally linked from itself to the new candidate sets it has generated, {@{a tree-like structure}@} appears, and the Apriori algorithm is similar to {@{[breadth-first search](breadth-first%20search.md)}@}. <!--SR:!2026-10-05,727,330!2027-11-19,998,339-->

Creation of association rules from the frequent item sets is {@{not covered by this algorithm}@}. <!--SR:!2029-06-07,1493,383-->

## the algorithm

Below is the algorithm of the ordered variant written in pseudo code:

```text
Apriori(T, ε)
    L_1 ← {large 1-item item sets}
    k ← 2
    while L_(k−1) is not empty
        C_k ← Apriori_gen(L_(k−1), k)
        for transactions t in T
            Dt ← {c in C_k : c ⊆ t}
            for candidates c in Dt
                count[c] ← count[c] + 1

        L_k ← {c in C_k : count[c] ≥ ε}
        k ← k + 1

    return Union(L_k)

Apriori_gen(L, k)
    result ← list()
    for all p ∈ L, q ∈ L where p_1 = q_1, p_2 = q_2, ..., p_(k-2) = q_(k-2) and p_(k-1) < q_(k-1)
        c = p ∪ {q_(k-1)}
        if u ∈ L for all u ⊆ c where |u| = k-1
            result.add(c)
    return result
```

### Python implementation

See [`Apriori algorithm.py`](attachments/Apriori%20algorithm.py) for a runnable example in [Python](Python%20(programming%20language).md).

## limitations

Candidate generation {@{spawns a large numbers of subsets, which is costly for computation}@}. Its bottom-up exploration nature means {@{finding any subset $S$ requires finding all its $2^{\lvert S \rvert} - 1$ proper subsets, including the [empty set](empty%20set.md), first}@}. <!--SR:!2029-04-10,1389,364!2028-12-12,1363,364-->

The algorithm also requires {@{scanning the database many times to check the candidates, reducing performance, especially if the database is input/output-bounded}@}. Therefore, the algorithm works best if {@{the database is permanently stored in the memory, which might not be practical for very large database}@}. <!--SR:!2026-12-14,780,344!2028-03-15,1151,364-->

Also, the time and space complexity of the algorithm is {@{very high: $O \left( 2^{\lvert D \rvert} \right)$, where $\lvert D \rvert$ is the horizontal width (number of items or columns) of the database}@}. <!--SR:!2030-05-13,1809,384-->

Common alternatives include {@{[Eclat algorithm](Eclat%20algorithm.md) and [FP-growth algorithm](FP-growth%20algorithm.md)}@}. <!--SR:!2026-10-16,698,343-->

The [Eclat algorithm](Eclat%20algorithm.md) is {@{generally faster than the Apriori algorithm, and might be slower when the database is large}@}. The [FP-growth algorithm](FP-growth%20algorithm.md) {@{outperforms both the Apriori and Eclat algorithms}@}, because it {@{does not generate and test candidates, uses a compact data structure}@}, and requires {@{only one (or two, depending on how you define "scan") database scan}@}. <!--SR:!2027-07-31,947,363!2031-11-06,2102,343!2026-03-01,19,352!2026-03-21,23,373-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Aprior_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
