from collections.abc import Collection, Iterable, Mapping, MutableSequence, Sequence
from functools import reduce
from itertools import combinations
from operator import add

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
    all_frequent_sets: MutableSequence[Sequence[Sequence[str]]] = [
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
    print("=========ordered=========")
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

    print("========unordered========")
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
