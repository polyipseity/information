from collections import Counter, defaultdict
from collections.abc import Mapping, MutableMapping, MutableSequence, Set
from dataclasses import InitVar, dataclass, field
from typing import Self, TypeVar

_TExtendsFPNode = TypeVar("_TExtendsFPNode", bound="FPNode")
Database = Mapping[Set[str], int]
FPTable = Mapping[str, MutableSequence["FPNode"]]  # sorted by decreasing count


@dataclass(slots=True)
class FPNode:
    table: InitVar[FPTable]
    parent: Self | None
    count: int = 0
    children: MutableMapping[str, Self] = field(default_factory=dict[str, Self])

    class _ChildrenDict(dict[str, _TExtendsFPNode]):
        __slots__ = ("_node", "_table")

        def __init__(self, node: _TExtendsFPNode, table: FPTable) -> None:
            self._node = node
            self._table = table

        def __missing__(self, key: str) -> _TExtendsFPNode:
            self[key] = ret = type(self._node)(self._table, self._node)
            self._table[key].append(ret)
            return ret

    def __post_init__(self, table: FPTable) -> None:
        self.children = self._ChildrenDict(self, table)

    def __str__(self) -> str:
        children = self.children
        last_children_idx = len(children) - 1
        return f"{self.count}{''.join(f'\n{"\\-" if idx == last_children_idx else "|-"}{key}: {"\n".join(f"{'  ' if idx == last_children_idx else '| '}{line}" for line in str(child).splitlines())[2:]}' for idx, (key, child) in enumerate(children.items()))}"


def generate_FP_tree_and_table(
    database: Database,
    minimum_support: int,
    *,
    debug: bool = False,
) -> tuple[FPNode, FPTable]:
    count_table = defaultdict[str, int](int)
    for item_set, count in database.items():
        for item in item_set:
            count_table[item] += count
    if debug:
        print(f"count table: {dict(sorted(count_table.items()))}")
    table = dict(
        (item, [])
        for item, _ in sorted(
            filter(lambda item: item[1] >= minimum_support, count_table.items()),
            key=lambda item: (-item[1], item[0]),
        )
    )  # `dict` keeps insertion order
    table_keys = tuple(table.keys())
    if debug:
        print(f"header table: { ({key: count_table[key] for key in table_keys}) }")

    processed_database = defaultdict[tuple[str, ...], int](int)
    for item_set, count in database.items():
        processed_database[
            tuple(
                sorted(
                    frozenset(item_set).intersection(table_keys), key=table_keys.index
                )
            )
        ] += count
    if debug:
        _print_database(processed_database)

    tree = FPNode(table, None)
    for item_set, count in processed_database.items():
        node = tree
        node.count += count
        for item in item_set:
            node = node.children[item]
            node.count += count
    if debug:
        print(tree)

    return tree, table


def get_item_set(node: FPNode) -> tuple[tuple[str, ...], int]:
    item_set, count = list[str](), node.count
    while (parent := node.parent) is not None:
        item_set.append(
            next(
                item
                for item, child_node in parent.children.items()
                if child_node == node
            )
        )
        node = parent
    return tuple(item_set), count


def FP_tree_algorithm(
    database: Database,
    minimum_support: int,
    *,
    debug: bool = False,
    alternative: bool = False,
    return_empty: bool = True,
    condition: Set[str] = frozenset(),
) -> Database:
    ret = dict[Set[str], int]()

    tree, table = generate_FP_tree_and_table(database, minimum_support, debug=debug)
    for item, nodes in reversed(tuple(table.items())):
        if debug:
            _print_header(f"conditional FP-tree of {set(condition)} on '{item}'")
        conditional_database: dict[Set[str], int] = {
            frozenset(item_set[1:]): count
            for item_set, count in map(get_item_set, nodes)
        }
        if debug:
            _print_database(conditional_database)
        conditional_ret: Database = {
            frozenset({item}) | item_set: count
            for item_set, count in FP_tree_algorithm(
                conditional_database,
                minimum_support,
                debug=debug,
                alternative=alternative,
                return_empty=return_empty,
                condition=frozenset({item}) | condition,
            ).items()
        }
        if alternative:
            conditional_ret[frozenset({item})] = sum(conditional_database.values())
        if debug:
            _print_header(
                f"results for conditional FP-tree of {set(condition)} on '{item}'"
            )
            _print_database(conditional_ret, sort_key=True)
        ret.update(conditional_ret)
        pass

    if not alternative:
        ret[frozenset()] = tree.count

    if not condition:
        if return_empty:
            if tree.count >= minimum_support:
                ret[frozenset()] = tree.count
        else:
            try:
                del ret[frozenset()]
            except KeyError:
                pass

    return ret


_RAW_DATABASE = (
    "bcdp",
    "fjq",
    "ci",
    "ad",
    "cm",
    "bdf",
    "adf",
    "al",
    "cg",
    "ck",
    "fno",
    "ef",
    "fh",
    "bd",
)
_DATABASE: Database = Counter(frozenset(transaction) for transaction in _RAW_DATABASE)
_MINIMUM_SUPPORT = 2
_EXPECTED = {
    frozenset[str](): 14,
    frozenset({"f"}): 6,
    frozenset({"d"}): 5,
    frozenset({"c"}): 5,
    frozenset({"b", "d"}): 3,
    frozenset({"b"}): 3,
    frozenset({"a"}): 3,
    frozenset({"a", "d"}): 2,
    frozenset({"f", "d"}): 2,
}


def _print_header(header: str = ""):
    header_len = len(header)
    left = header_len // 2
    right = header_len - left
    print(f"{'=' * (32 - left)} {header} {'=' * (32 - right)}")


def _print_database(
    database: Database | Mapping[tuple[str, ...], int], *, sort_key: bool = False
):
    print(
        "\n".join(
            f"{tuple(sorted(key) if sort_key else key)}: {val}"
            for key, val in database.items()
        )
    )


if __name__ == "__main__":
    _print_header("database")
    _print_database(_DATABASE, sort_key=True)

    _print_header("normal")
    result = FP_tree_algorithm(_DATABASE, _MINIMUM_SUPPORT, debug=True)
    _print_header("results for normal")
    _print_database(result, sort_key=True)
    assert _EXPECTED == result

    _print_header("alternative")
    result = FP_tree_algorithm(
        _DATABASE, _MINIMUM_SUPPORT, alternative=True, debug=True
    )
    _print_header("results for alternative")
    _print_database(result, sort_key=True)
    assert _EXPECTED == result
