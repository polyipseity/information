---
aliases:
  - Apriori algorithm
tags:
  - flashcard/active/general/Apriori_algorithm
  - language/in/English
---

# Apriori algorithm

## overview

To understand the Apriori algorithm, notice that {{for any database and two item sets _A_ and _B_ where $A \subseteq B$, then $\operatorname{supp}(A) \ge \operatorname{supp}(B)$}}. This is easily seen by considering that {{any transaction that satisfies _B_ contains all the items of _B_, so must also satisfy _A_, as it contains all the items of _A_ as a subset of _B_}}. This is called the {{_downward closure lemma_}}. <!--SR:!2025-12-08,487,310!2024-12-31,232,319!2027-02-01,818,330-->

Then the Apriori algorithm uses a {{"bottom up"}} approach. The frequent sets {{start from one item and then are extended one item at a time, called _candidate generation_}}. The generation can cover all possible frequent sets because of the downward closure lemma. Then, {{the candidates are tested against the support threshold and become the new frequent sets that are one item longer than the last generation}}. Repeat this process until {{there are no more candidates}}. The output is {{all frequent sets in all generations}}. <!--SR:!2024-11-20,203,319!2026-10-06,728,330!2025-03-09,282,290!2025-03-01,299,339!2026-07-18,668,330-->

Filtering the candidate, called the {{_count step_}}, is obvious, but candidate generation is not as obvious. For candidate generation, there are two steps: {{_join step_ and _prune step_}}. <!--SR:!2024-12-21,224,336!2025-05-11,310,363-->

For _join step_, one first consider, from the previous generation of frequent sets, all possible pairs of sets that {{have a [symmetric difference](symmetric%20difference.md) of size 2, i.e. the set are the same except for 1 item, like $\set{1, 2, 3}$ and $\set{1, 20, 3}$}}. Then, for each pair, {{the union of the two sets is a new _possible_ candidate set, like $\set{1, 2, 3, 20}$ using the same example}}. <!--SR:!2025-01-03,235,319!2027-01-30,820,330-->

For _prune step_, confirm the _possible_ candidate sets. For each _possible_ candidate set, {{check that all subsets that are one item less in size than the possible candidate set are in the previous generation of frequent sets, like checking $\set{1, 2, 3}, \set{1, 2, 20}, \set{1, 3, 20}, \set{2, 3, 20}$ using the same example}}. One may note that {{two subsets are guaranteed to be in the previous generation frequent sets because of how we generated the _possible_ candidate set, so we can skip checking the two subsets}}. After checking, if the check passes, {{it is part of the candidate for the new generation, otherwise it is not}}. <!--SR:!2025-07-02,338,290!2024-11-19,203,319!2024-12-12,219,319-->

Note that the above is a slower variant of the Apriori algorithm. There is a much more common variant that is also faster, but {{that additionally requires all sets above be lexicographically ordered sets}}. With this additional requirement in mind, the difference is in {{the join step}}. First, we define the _prefix set_ of an ordered set of size _n_ as {{the first _n_-1 items of the ordered set, itself in an ordered set}}. Now the join step instead becomes {{considering all possible pairs of sets that have the same prefix set, then the union of each pair is a _possible_ candidate set}}. <!--SR:!2026-04-22,602,336!2025-02-03,277,356!2026-05-31,628,336!2026-08-14,685,336-->

If we consider each set is directionally linked from itself to the new candidate sets it has generated, {{a tree-like structure}} appears, and the Apriori algorithm is similar to {{[breadth-first search](breadth-first%20search.md)}}. <!--SR:!2026-10-05,727,330!2025-02-24,294,339-->

Creation of association rules from the frequent item sets is {{not covered by this algorithm}}. <!--SR:!2025-05-04,301,363-->

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

Below is a runnable example in [Python](Python%20(programming%20language).md).

[`Apriori algorithm.py`](attachments/Apriori%20algorithm.py):

```Python
from functools import reduce
from itertools import combinations
from operator import add
from typing import Collection, Iterable, Mapping, Sequence

columns = (
    "name",
    "angus beef burger",
    "crab roe noodle",
    "lime juice",
    "mulberry juice",
    "roast duck",
    "scallop congee",
)
table = (
    ("Alice", False, True, False, False, True, True),
    ("Bob", False, True, False, False, True, True),
    ("Charles", True, True, False, False, False, True),
    ("David", True, True, True, True, False, False),
    ("Eve", True, False, True, False, True, False),
    ("Fiona", True, False, False, False, False, True),
    ("Grace", False, False, True, False, True, False),
)
support_threshold = 2
transaction_columns = columns[1:]
transactions = tuple(
    {columns[index]: content for index, content in enumerate(row[1:], start=1)}
    for row in table
)


def format_sets(sets: Iterable[Iterable[str]]):
    return "\n".join(str(", ".join(sorted(item_set))) for item_set in sets)


def count_item_set(
    transactions: Iterable[Mapping[str, bool]], item_set: Collection[str]
):
    return sum(
        1 for transaction in transactions if all(transaction[item] for item in item_set)
    )


def apriori_candidate_gen_unordered(
    previous_frequent_sets: Collection[Collection[str]],
    *,
    debug: bool = False,
) -> Collection[Collection[str]]:
    previous_frequent_sets2 = frozenset(
        frozenset(previous_frequent_set)
        for previous_frequent_set in previous_frequent_sets
    )
    candidates = (
        set1 | set2
        for set1, set2 in combinations(previous_frequent_sets2, 2)
        if len(set1 ^ set2) == 2
    )
    if debug:
        candidates = tuple(candidates)
        print(f"C_1 = {candidates}")
    candidates = (
        candidate
        for candidate in candidates
        if all((candidate - {item}) in previous_frequent_sets2 for item in candidate)
    )
    if debug:
        candidates = tuple(candidates)
        print(f"C_2 = {candidates}")
    ret = tuple({frozenset(candidate): False for candidate in candidates})
    return ret


def apriori_candidate_gen_ordered(
    previous_frequent_sets: Sequence[Sequence[str]],
    *,
    debug: bool = False,
) -> Sequence[Sequence[str]]:
    candidates = (
        (*set1, set2[-1])
        for set1, set2 in combinations(previous_frequent_sets, 2)
        if set1[:-1] == set2[:-1] and set1[-1] != set2[-1]
    )
    if debug:
        candidates = tuple(candidates)
        print(f"C_1 = {candidates}")
    previous_frequent_sets2 = frozenset(previous_frequent_sets)
    candidates = (
        candidate
        for candidate in candidates
        if (
            all(
                (*candidate[:idx], *candidate[idx + 1 :]) in previous_frequent_sets2
                for idx, _ in enumerate(candidate)
            )
        )
    )
    if debug:
        candidates = tuple(candidates)
        print(f"C_2 = {candidates}")
    return tuple(candidates)


def apriori(
    columns: Iterable[str],
    transactions: Collection[Mapping[str, bool]],
    support_threshold: int,
    *,
    ordered: bool = True,
    debug: bool = False,
) -> Sequence[Sequence[Sequence[str]]]:
    if debug:
        columns = tuple(columns)
        print(f"C = {tuple((column,) for column in columns)}")
    all_frequent_sets: Sequence[Sequence[Sequence[str]]] = [
        tuple(
            (column,)
            for column in columns
            if count_item_set(transactions, {column}) >= support_threshold
        )
    ]
    if debug:
        print(f"L = {all_frequent_sets[-1]}")
    while frequent_set := all_frequent_sets[-1]:
        candidate_sets = (
            apriori_candidate_gen_ordered
            if ordered
            else apriori_candidate_gen_unordered
        )(frequent_set, debug=debug)
        next_candidate_sets = tuple(
            tuple(candidate_set)
            for candidate_set in candidate_sets
            if count_item_set(transactions, candidate_set) >= support_threshold
        )
        if debug:
            print(f"L = {next_candidate_sets}")
        all_frequent_sets.append(next_candidate_sets)
    return tuple(all_frequent_sets)


if __name__ == "__main__":
    print(f"=========ordered=========")
    result = format_sets(
        reduce(
            add,
            map(
                tuple,
                apriori(
                    transaction_columns, transactions, support_threshold, debug=True
                ),
            ),
            (),
        )
    )
    print(result)
    expected_str = """
angus beef burger
crab roe noodle
lime juice
roast duck
scallop congee
angus beef burger, crab roe noodle
angus beef burger, lime juice
angus beef burger, scallop congee
crab roe noodle, roast duck
crab roe noodle, scallop congee
lime juice, roast duck
roast duck, scallop congee
crab roe noodle, roast duck, scallop congee
""".strip()
    assert expected_str == result

    print(f"========unordered========")
    unordered_result = format_sets(
        reduce(
            add,
            map(
                tuple,
                apriori(
                    transaction_columns,
                    transactions,
                    support_threshold,
                    ordered=False,
                    debug=True,
                ),
            ),
            (),
        )
    )
    print(unordered_result)
    assert frozenset(expected_str.splitlines()) == frozenset(
        unordered_result.splitlines()
    )
```

## limitations

Candidate generation {{spawns a large numbers of subsets, which is costly for computation}}. Its bottom-up exploration nature means {{finding any subset $S$ requires finding all its $2^{\lvert S \rvert} - 1$ proper subsets, including the [empty set](empty%20set.md), first}}. <!--SR:!2025-06-19,382,364!2025-03-20,288,344-->

The algorithm also requires {{scanning the database many times to check the candidates, reducing performance, especially if the database is input/output-bounded}}. Therefore, the algorithm works best if {{the database is permanently stored in the memory, which might not be practical for very large database}}. <!--SR:!2026-12-14,780,344!2025-01-18,243,344-->

Also, the time and space complexity of the algorithm is {{very high: $O \left( 2^{\lvert D \rvert} \right)$, where $\lvert D \rvert$ is the horizontal width (number of items or columns) of the database}}. <!--SR:!2025-05-27,363,364-->

Common alternatives include {{[Eclat algorithm](Eclat%20algorithm.md) and [FP-growth algorithm](FP-growth%20algorithm.md)}}. <!--SR:!2024-11-17,155,323-->

The [Eclat algorithm](Eclat%20algorithm.md) is {{generally faster than the Apriori algorithm, and might be slower when the database is large}}. The [FP-growth algorithm](FP-growth%20algorithm.md) {{outperforms both the Apriori and Eclat algorithms, because it does not generate and test candidates, uses a compact data structure, and requires only one (or two, depending on how you define "scan") database scan}}. <!--SR:!2024-12-26,200,343!2026-02-03,471,323-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Aprior_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
