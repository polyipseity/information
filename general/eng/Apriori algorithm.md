---
aliases:
  - Apriori algorithm
tags:
  - flashcard/active/general/eng/Apriori_algorithm
  - language/in/English
---

# Apriori algorithm

## overview

To understand {@{the Apriori algorithm}@}, notice that for {@{any database and two item sets _A_ and _B_ in the database where $A \subseteq B$}@}, then {@{$\operatorname{supp}(A) \ge \operatorname{supp}(B)$}@}. This is easily seen by considering that {@{any transaction that satisfies _B_ contains all the items of _B_}@}, so must {@{also satisfy _A_, as it contains all the items of _A_ as a subset of _B_}@}. This is called the {@{_downward closure lemma_}@}.

Then the Apriori algorithm uses a {@{"bottom up"}@} approach. The frequent sets {@{start from one item and then are extended one item at a time, called _candidate generation_}@}. The generation can cover all possible frequent sets because of the downward closure lemma. Then, {@{the candidates are tested against the support threshold and become the new frequent sets that are one item longer than the last generation}@}. Repeat this process until {@{there are no more candidates}@}. The output is {@{all frequent sets in all generations}@}.

Filtering the candidate, called the {@{_count step_}@}, is obvious, but candidate generation is not as obvious. For candidate generation, there are two steps: {@{_join step_ and _prune step_}@}.

For _join step_, one first consider, from the previous generation of frequent sets, all possible pairs of sets that {@{have a [symmetric difference](symmetric%20difference.md) of size 2, i.e. the set are the same except for 1 item, like $\set{1, 2, 3}$ and $\set{1, 20, 3}$}@}. Then, for each pair, {@{the union of the two sets is a new _possible_ candidate set, like $\set{1, 2, 3, 20}$ using the same example}@}.

For _prune step_, confirm the _possible_ candidate sets. For each _possible_ candidate set, {@{check that all subsets that are one item less in size than the possible candidate set are in the previous generation of frequent sets, like checking $\set{1, 2, 3}, \set{1, 2, 20}, \set{1, 3, 20}, \set{2, 3, 20}$ using the same example}@}. One may note that {@{two subsets are guaranteed to be in the previous generation frequent sets because of how we generated the _possible_ candidate set, so we can skip checking the two subsets}@}. After checking, if the check passes, {@{it is part of the candidate for the new generation, otherwise it is not}@}.

Note that the above is a slower variant of the Apriori algorithm. There is a much more common variant that is also faster, but {@{that additionally requires all sets above be lexicographically ordered sets}@}. With this additional requirement in mind, the difference is in {@{the join step}@}. First, we define the _prefix set_ of an ordered set of size _n_ as {@{the first _n_−1 items of the ordered set, itself in an ordered set}@}. Now the join step instead becomes {@{considering all possible pairs of sets that have the same prefix set, then the union of each pair is a _possible_ candidate set}@}.

If we consider each set is directionally linked from itself to the new candidate sets it has generated, {@{a tree-like structure}@} appears, and the Apriori algorithm is similar to {@{[breadth-first search](breadth-first%20search.md)}@}.

Creation of association rules from the frequent item sets is {@{not covered by this algorithm}@}.

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

Candidate generation {@{spawns a large numbers of subsets, which is costly for computation}@}. Its bottom-up exploration nature means {@{finding any subset $S$ requires finding all its $2^{\lvert S \rvert} - 1$ proper subsets, including the [empty set](empty%20set.md), first}@}.

The algorithm also requires {@{scanning the database many times to check the candidates, reducing performance, especially if the database is input/output-bounded}@}. Therefore, the algorithm works best if {@{the database is permanently stored in the memory, which might not be practical for very large database}@}.

Also, the time and space complexity of the algorithm is {@{very high: $O \left( 2^{\lvert D \rvert} \right)$, where $\lvert D \rvert$ is the horizontal width (number of items or columns) of the database}@}.

Common alternatives include {@{[Eclat algorithm](Eclat%20algorithm.md) and [FP-growth algorithm](FP-growth%20algorithm.md)}@}.

The [Eclat algorithm](Eclat%20algorithm.md) is {@{generally faster than the Apriori algorithm, and might be slower when the database is large}@}. The [FP-growth algorithm](FP-growth%20algorithm.md) {@{outperforms both the Apriori and Eclat algorithms}@}, because it {@{does not generate and test candidates, uses a compact data structure}@}, and requires {@{only one (or two, depending on how you define "scan") database scan}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Aprior_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
