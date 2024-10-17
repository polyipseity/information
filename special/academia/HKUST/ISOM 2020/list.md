---
aliases:
  - Python list
  - Python lists
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2020/list
  - language/in/English
---

# Python list

A Python list is {{a collection of values, and you can treat it like a collective of variables}}. <!--SR:!2024-11-17,50,294-->

If you try to {{get the type of a list using `type(list)`}}, {{the returned type name is either `list` or `<class 'list'>`}}, regardless of {{the contents contained inside the list}}. <!--SR:!2024-11-14,49,294!2024-11-09,45,294!2024-12-05,66,314-->

## syntax

To define a list in Python, {{enclose all items in square brackets `[]` and separate each item by a comma `,`, like `[1, 2, "item", 4.2, "ok", 'hey', False]`}}. An empty list is {{allowed and created using `[]`, and can be expanded later}}. A trailing comma is {{allowed and optional after the last item (but not if there are no items, i.e. `[,]` is invalid)}}. Note that a list can {{contain items of different types (including lists) like the example just now, though usually it is more useful for them to be the same type}}. <!--SR:!2024-10-29,35,294!2024-10-26,32,294!2024-10-27,33,294!2024-11-06,39,294-->

ISOM 2020 note: Note that {{`(..., ...)`}} is {{creating a `tuple`, a type that is similar to a `list` but is immutable (not modifiable)}}. But you {{do not need to care or know about it}}.

## indexing

To {{access or replace the n-th item}}, simply write {{`sequence[n-1]`}}: <!--SR:!2024-11-28,61,314!2024-12-02,63,310-->

```Python
assert "asd"[2] == "d"
assert [39, "omg", 'asd', 3.4][2] == "asd"
```

Indices can be {{negative, in which case it counts from the back}}: <!--SR:!2024-11-18,51,294-->

```Python
assert "asd"[-1] == "d"
assert [39, "omg", 'asd', 3.4][-2] == "asd"
```

If {{the index (but not slicing) is out of range (regardless if it is positive or negative)}}, then {{an `IndexError` will be raised}}. <!--SR:!2024-10-25,31,294!2024-10-28,34,294-->

## manipulation

You can {{use the [indexing](#indexing) notation to replace the _n_-th item of a list}}. <!--SR:!2024-12-08,68,314-->

To {{add a new item (not replace existing items) to the back of a list}}, use {{`list.append(value)`}}. Its return value is {{nothing (`None`)}}. <!--SR:!2024-10-23,29,274!2024-12-01,62,314!2024-10-19,25,274-->

To {{remove an the _n_-th existing item}}. use {{`list.pop(index)`, with `index` being _n_ - 1}}. Note that `index` accepts {{numbers in the same ways as in the [indexing](#indexing) notation, i.e. negative indices are accepted and have the same meaning}}. Likewise, if {{the index is out of range or `list` is empty}}, then {{an `IndexError` will be raised}}. Not specifying {{the `index` is also okay (`list.pop()`), and `index` will be set to `-1` by default, meaning the last item will be removed}}. After removing the item, it will {{return the removed item}}. <!--SR:!2024-11-08,44,294!2024-10-31,37,294!2024-11-09,44,294!2024-11-30,61,314!2024-10-25,31,294!2024-12-07,67,314!2024-11-28,59,310-->

To {{concatenate/join two lists (or strings)}}, use {{the `+` operator}}. Note that {{the resulting list is different from the original 2 lists, i.e. modifying the resulting list will not modify the original 2 lists}}. Since {{`str`s cannot be modified}}, the above is irrelevant for strings. If {{the `+` operator is applied between different types}}, then {{a `TypeError` will be raised}}. <!--SR:!2025-01-08,83,336!2025-01-08,83,336!2025-01-08,83,336!2025-01-08,83,336!2025-01-08,83,336!2025-01-08,83,336-->

## length

{{The length (`int`) of a sequence, including but not limited to `list` and `str`}}, can be determined by {{`len(list)` (but not `list.len()`)}}. <!--SR:!2024-11-28,61,314!2024-12-06,66,314-->

## aggregate functions

Aggregate functions {{summarize a result from a list}}. <!--SR:!2024-10-28,34,294-->

- `max(list)` ::: Returns the maximum item. If `list` is empty, a `ValueError` is raised. If `list` consists of `float`s and `int`s only, the largest item (the originally leftmost one is returned if there are multiple largest items) will be returned, and no type conversion is done. If `list` consists of `str`s only, then the last string, ordered lexicographically (the originally leftmost one is returned if there are multiple first strings), is returned. If `list` mixes incompatible types (e.g. `int` and `str`), then a `TypeError` is raised. <!--SR:!2024-10-19,25,274!2024-10-27,33,274-->
- `min(list)` ::: Returns the maximum item. If `list` is empty, a `ValueError` is raised. If the `list` consists of `float`s and `int`s only, the smallest item (the originally leftmost one is returned if there are multiple largest items) will be returned, and no type conversion is done. If `list` consists of `str`s only, then the first string, ordered lexicographically (the originally leftmost one is returned if there are multiple first strings), is returned. If `list` mixes incompatible types (e.g. `int` and `str`), then a `TypeError` is raised. <!--SR:!2024-10-24,30,294!2024-11-09,44,294-->
- `sum(list)` ::: Returns the sum of elements in the list. If the `list` is empty, an `int`, `0`, is returned. If `list` consists of `float`s and `int`s only, the sum is returned. The return type is `float` if there is at least one `float` in `list`, otherwise the return type is `int`. If `list` contains incompatible types (e.g. `str`), then a `TypeError` is raised. <!--SR:!2024-10-23,28,274!2024-10-20,26,274-->

## search functions

- `val in list`, `val not in list` ::: Returns a `bool` indicating whether `val` is in `list`. Equality is compared using `==`, so `0.0 in [0]` is `True` instead of `False`. The `not in` operator simply inverts the `bool` returned by `in` operator.
- `list.count(val)` ::: Count the number of `val`s in `list`. Returns `0` if `val` is not found in the list. Equality is compared using `==`, so `[0, 0.0].count(0.0)` is `2` instead of `1`. <!--SR:!2024-11-17,40,316!2025-01-08,83,336-->
- `list.index(val)` ::: Returns the index of `val` in `list`. The index of the leftmost item is returned if there are multiple matching items. Raises `ValueError` if `val` is not found in the list. Equality is compared using `==`, so `[0, 0.0].index(0.0)` is `0` instead of `1`. <!--SR:!2025-01-08,83,336!2025-01-08,83,336-->
