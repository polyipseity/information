---
aliases:
  - Apriori algorithm
tags:
  - flashcard/general/Apriori_algorithm
  - language/in/English
---

# Apriori algorithm

## overview

To understand the Apriori algorithm, notice that {{for any database and two item sets _A_ and _B_ where $A \subseteq B$, then $\operatorname{supp}(A) \ge \operatorname{supp}(B)$}}. This is easily seen by considering that {{any transaction that satisfies _B_ contains all the items of _B_, so must also satisfy _A_, as it contains all the items of _A_ as a subset of _B_}}. This is called the {{_downward closure lemma_}}. <!--SR:!2024-04-09,42,290!2024-05-12,73,319!2024-04-28,62,310-->

Then the Apriori algorithm uses a {{"bottom up"}} approach. The frequent sets {{start from one item and then are extended one item at a time, called _candidate generation_}}. The generation can cover all possible frequent sets because of the downward closure lemma. Then, {{the candidates are tested against the support threshold and become the new frequent sets that are one item longer than the last generation}}. Repeat this process until {{there are no more candidates}}. The output is {{all frequent sets in all generations}}. <!--SR:!2024-05-01,64,319!2024-04-20,55,310!2024-03-17,28,270!2024-05-06,68,319!2024-04-14,50,310-->

Filtering the candidate is obvious, but candidate generation is not as obvious. For candidate generation, there are two steps: {{_join step_ and _prune step_}}. <!--SR:!2024-03-04,15,316-->

For _join step_, one first consider, from the previous generation of frequent sets, all possible pairs of sets that {{have a [symmetric difference](symmetric%20difference.md) of size 2, i.e. the set are the same except for 1 item, like $\set{1, 2, 3}$ and $\set{1, 20, 3}$}}. Then, for each pair, {{the union of the two sets is a new _possible_ candidate set, like $\set{1, 2, 3, 20}$ using the same example}}. <!--SR:!2024-05-13,74,319!2024-04-27,61,310-->

For _prune step_, confirm the _possible_ candidate sets. For each _possible_ candidate set, {{check that all subsets that are one item less in size than the possible candidate set are in the previous generation of frequent sets, like checking $\set{1, 2, 3}, \set{1, 2, 20}, \set{1, 3, 20}, \set{2, 3, 20}$ using the same example}}. One may note that {{two subsets are guaranteed to be in the previous generation frequent sets because of how we generated the _possible_ candidate set, so we can skip checking the two subsets}}. After checking, if the check passes, {{it is part of the candidate for the new generation, otherwise it is not}}. <!--SR:!2024-04-02,40,290!2024-04-30,64,319!2024-05-07,69,319-->

Note that the above is a slower variant of the Apriori algorithm. There is a much more common variant that is also faster, but {{that additionally requires all sets above be lexicographically ordered sets}}. With this additional requirement in mind, the difference is in {{the join step}}. First, we define the _prefix set_ of an ordered set of size _n_ as {{the first _n_-1 items of the ordered set, itself in an ordered set}}. Now the join step instead becomes {{by considering all possible pairs of sets that have the same prefix set, then the union of each pair is a _possible_ candidate set}}. <!--SR:!2024-04-12,44,316!2024-05-02,60,336!2024-03-04,15,316!2024-03-05,16,316-->

If we consider each set is directionally linked from itself to the new candidate sets it has generated, {{a tree-like structure}} appears, and the Apriori algorithm is similar to {{[breadth-first search](breadth-first%20search.md)}}. <!--SR:!2024-04-19,55,310!2024-05-05,67,319-->

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

> [!example]- implementations
>
> Below is a runnable example of both variants in [Python](Python%20(programming%20language).md):
>
> ```Python
> from functools import reduce
> from itertools import combinations
> from operator import add
> from typing import Collection, Iterable, Mapping, Sequence
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
> transaction_columns = columns[1:]
> transactions = tuple(
>     {columns[index]: content for index, content in enumerate(row[1:], start=1)}
>     for row in table
> )
>
>
> def format_sets(sets: Iterable[Iterable[str]]):
>     return "\n".join(str(", ".join(sorted(item_set))) for item_set in sets)
>
>
> def count_item_set(
>     transactions: Iterable[Mapping[str, bool]], item_set: Collection[str]
> ):
>     return sum(
>         1 for transaction in transactions if all(transaction[item] for item in item_set)
>     )
>
>
> def apriori_candidate_gen_unordered(
>     previous_frequent_sets: Collection[Collection[str]],
>     *,
>     debug: bool = False,
> ) -> Collection[Collection[str]]:
>     previous_frequent_sets2 = frozenset(
>         frozenset(previous_frequent_set)
>         for previous_frequent_set in previous_frequent_sets
>     )
>     candidates = (
>         set1 | set2
>         for set1, set2 in combinations(previous_frequent_sets2, 2)
>         if len(set1 ^ set2) == 2
>     )
>     if debug:
>         candidates = tuple(candidates)
>         print(f"C_1 = {candidates}")
>     candidates = (
>         candidate
>         for candidate in candidates
>         if all((candidate - {item}) in previous_frequent_sets2 for item in candidate)
>     )
>     if debug:
>         candidates = tuple(candidates)
>         print(f"C_2 = {candidates}")
>     ret = tuple({frozenset(candidate): False for candidate in candidates})
>     return ret
>
>
> def apriori_candidate_gen_ordered(
>     previous_frequent_sets: Sequence[Sequence[str]],
>     *,
>     debug: bool = False,
> ) -> Sequence[Sequence[str]]:
>     candidates = (
>         (*set1, set2[-1])
>         for set1, set2 in combinations(previous_frequent_sets, 2)
>         if set1[:-1] == set2[:-1] and set1[-1] != set2[-1]
>     )
>     if debug:
>         candidates = tuple(candidates)
>         print(f"C_1 = {candidates}")
>     previous_frequent_sets2 = frozenset(previous_frequent_sets)
>     candidates = (
>         candidate
>         for candidate in candidates
>         if (
>             all(
>                 (*candidate[:idx], *candidate[idx + 1 :]) in previous_frequent_sets2
>                 for idx, _ in enumerate(candidate)
>             )
>         )
>     )
>     if debug:
>         candidates = tuple(candidates)
>         print(f"C_2 = {candidates}")
>     return tuple(candidates)
>
>
> def apriori(
>     columns: Iterable[str],
>     transactions: Collection[Mapping[str, bool]],
>     support_threshold: int,
>     ordered: bool,
>     *,
>     debug: bool = False,
> ) -> Sequence[Sequence[Sequence[str]]]:
>     if debug:
>         columns = tuple(columns)
>         print(f"C = {columns}")
>     all_frequent_sets: Sequence[Sequence[Sequence[str]]] = [
>         tuple(
>             (column,)
>             for column in columns
>             if count_item_set(transactions, {column}) >= support_threshold
>         )
>     ]
>     if debug:
>         print(f"L = {all_frequent_sets[-1]}")
>     while frequent_set := all_frequent_sets[-1]:
>         candidate_sets = (
>             apriori_candidate_gen_ordered
>             if ordered
>             else apriori_candidate_gen_unordered
>         )(frequent_set, debug=debug)
>         next_candidate_sets = tuple(
>             tuple(candidate_set)
>             for candidate_set in candidate_sets
>             if count_item_set(transactions, candidate_set) >= support_threshold
>         )
>         if debug:
>             print(f"L = {next_candidate_sets}")
>         all_frequent_sets.append(next_candidate_sets)
>     return tuple(all_frequent_sets)
>
>
> if __name__ == "__main__":
>     result = format_sets(
>         reduce(
>             add,
>             map(tuple, apriori(transaction_columns, transactions, 2, True, debug=True)),
>             (),
>         )
>     )
>     print(f"=========ordered=========\n{result}")
>     expected_str = """
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
>     assert expected_str == result
>
>     unordered_result = format_sets(
>         reduce(
>             add,
>             map(
>                 tuple, apriori(transaction_columns, transactions, 2, False, debug=True)
>             ),
>             (),
>         )
>     )
>     print(f"========unordered========\n{unordered_result}")
>     assert frozenset(expected_str.splitlines()) == frozenset(
>         unordered_result.splitlines()
>     )
> ```

## limitations

Candidate generation {{spawns a large numbers of subsets, which is costly for computation}}. Its bottom-up exploration nature means {{finding any subset $S$ requires finding all its $2^{\lvert S \rvert} - 1$ proper subsets first}}. <!--SR:!2024-03-12,18,324!2024-03-13,19,324-->

The algorithm also requires {{scanning the database many times to check the candidates, reducing performance, especially if the database is input/output-bounded}}. Therefore, the algorithm works best if {{the database is permanently stored in the memory, which might not be practical for very large database}}. <!--SR:!2024-03-11,17,324!2024-03-10,16,324-->

Also, the time and space complexity of the algorithm is {{very high: $O \left( 2^{\lvert D \rvert} \right)$, where $\lvert D \rvert$ is the horizontal width (number of items or columns) of the database}}. <!--SR:!2024-03-12,18,324-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Aprior_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
