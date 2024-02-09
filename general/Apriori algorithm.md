---
aliases:
  - Apriori algorithm
tags:
  - flashcards/general/Apriori_algorithm
  - languages/in/English
---

# Apriori algorithm

## overview

To understand the Apriori algorithm, notice that {{for any database and two item sets $A, B$ where $A \subseteq B$, then $\operatorname{supp}(A) \ge \operatorname{supp}(B)$}}. This is easily seen by considering that {{any transaction that satisfies $B$ contains all the items of $B$, so must also satisfy $A$, as it contains all the items of $A$ as a subset of $B$}}. This is called the {{_downward closure lemma_}}.

Then the Apriori algorithm uses a {{"bottom up"}} approach. The frequent sets {{start from one item and then are extended one item at a time, called _candidate generation_}}. The generation can cover all possible frequent sets because of the downward closure lemma. Then, {{the candidates are tested against the support threshold and become the new frequent sets that are one item longer than the last generation}}. Repeat this process until {{there are no more candidates}}. The output is {{all frequent sets in all generations}}.

Filtering the candidate is obvious, but candidate generation is not as obvious. For candidate generation, one first consider, from the previous generation of frequent sets, all possible pairs of sets that {{have a [symmetric difference](symmetric%20difference.md) of size 2, i.e. the set are the same except for 1 item, like $\set{1, 2, 3}$ and $\set{1, 20, 3}$}}. Then, for each pair, {{the union of the two sets is a new _possible_ candidate set, like $\set{1, 2, 3, 20}$ using the same example}}. Lastly, confirm the _possible_ candidate sets. For each _possible_ candidate set, {{check that all subsets that are one item less in size than the possible candidate set are in the previous generation of frequent sets, like checking $\set{1, 2, 3}, \set{1, 2, 20}, \set{1, 3, 20}, \set{2, 3, 20}$ using the same example}}. One may note that {{two subsets are guaranteed to be in the previous generation frequent sets because of how we generated the _possible_ candidate set, so we can skip checking the two subsets}}. After checking, if the check passes, {{it is part of the candidate for the new generation, otherwise it is not}}.

If we consider each set is directionally linked from itself to the new candidate sets it has generated, {{a tree-like structure}} appears, and the Apriori algorithm is similar to {{[breadth-first search](breadth-first%20search.md)}}.

Below is the algorithm written in pseudo code:

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

> [!example]- implementations
>
> Below is a runnable example in [Python](Python%20(programming%20language).md):
>
> ```Python
> from functools import reduce
> from itertools import combinations
> from operator import add
> from typing import AbstractSet, Collection, Mapping, Iterable
>
> columns = (
>     "name",
>     "likes Alice",
>     "likes Bob",
>     "likes Charles",
>     "likes David",
>     "likes Eve",
> )
> table = (
>     ("Alice", False, False, True, False, False),
>     ("Bob", True, False, True, False, True),
>     ("Charles", True, False, False, True, True),
>     ("David", True, False, True, True, True),
>     ("Eve", True, False, False, True, False),
> )
> transactions = tuple(
>     {columns[index]: content for index, content in enumerate(row[1:], start=1)}
>     for row in table
> )
>
> def count_item_set(
>     transactions: Iterable[Mapping[str, bool]], item_set: AbstractSet[str]
> ):
>     return sum(
>         1 for transaction in transactions if all(transaction[item] for item in item_set)
>     )
>
> def apriori_candidate_gen(previous_frequent_sets: Collection[AbstractSet[str]]):
>     candidates = (
>         set1 | set2
>         for set1, set2 in combinations(previous_frequent_sets, 2)
>         if len(set1 ^ set2) == 2
>     )
>     previous_frequent_sets2 = frozenset(previous_frequent_sets)
>     candidates = (
>         candidate
>         for candidate in candidates
>         if all((candidate - {item}) in previous_frequent_sets2 for item in candidate)
>     )
>     return tuple({frozenset(candidate): False for candidate in candidates})
>
> def apriori(transactions: Iterable[Mapping[str, bool]], support_threshold: int):
>     all_frequent_sets = [
>         tuple(
>             frozenset({column})
>             for column in columns[1:]
>             if count_item_set(transactions, {column}) >= support_threshold
>         )
>     ]
>     while frequent_set := all_frequent_sets[-1]:
>         candidate_sets = apriori_candidate_gen(frequent_set)
>         all_frequent_sets.append(
>             tuple(
>                 candidate_set
>                 for candidate_set in candidate_sets
>                 if count_item_set(transactions, candidate_set) >= support_threshold
>             )
>         )
>     return reduce(add, all_frequent_sets, ())
>
>
> assert (
>     "\n".join(str(", ".join(sorted(item_set))) for item_set in apriori(transactions, 2))
>     == """
> likes Alice
> likes Charles
> likes David
> likes Eve
> likes Alice, likes Charles
> likes Alice, likes David
> likes Alice, likes Eve
> likes Charles, likes Eve
> likes David, likes Eve
> likes Alice, likes Charles, likes Eve
> likes Alice, likes David, likes Eve
> """.strip()
> )
> ```

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Aprior_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
