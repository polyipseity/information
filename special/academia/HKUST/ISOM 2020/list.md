---
aliases:
  - Python list
  - Python lists
tags:
  - flashcard/active/special/academia/HKUST/ISOM_2020/list
  - language/in/English
---

# Python list

A Python list is {@{a collection of values, and you can treat it like a collective of variables}@}. <!--SR:!2027-11-26,886,334-->

If you try to {@{get the type of a list using `type(list)`}@}, {@{the returned type name is either `list` or `<class 'list'>`}@}, regardless of {@{the contents contained inside the list}@}. <!--SR:!2027-10-23,870,334!2027-08-16,812,334!2029-05-23,1339,354-->

## syntax

To define a list in Python, {@{enclose all items in square brackets `[]` and separate each item by a comma `,`, like `[1, 2, "item", 4.2, "ok", 'hey', False]`}@}. An empty list is {@{allowed and created using `[]`, and can be expanded later}@}. A trailing comma is {@{allowed and optional after the last item (but not if there are no items, i.e. `[,]` is invalid)}@}. Note that a list can {@{contain items of different types (including lists) like the example just now, though usually it is more useful for them to be the same type}@}. <!--SR:!2026-12-31,645,334!2026-10-22,591,334!2030-12-20,1745,334!2027-03-12,696,334-->

ISOM 2020 note: Note that {@{`(..., ...)`}@} is {@{creating a `tuple`, a type that is similar to a `list` but is immutable (not modifiable)}@}. But you {@{do not need to care or know about it}@}. <!--SR:!2026-03-16,410,380!2026-04-04,426,380!2026-04-09,430,380-->

## indexing

To {@{access or replace the n-th item}@}, simply write {@{`sequence[n-1]`}@}: <!--SR:!2029-01-09,1236,354!2029-01-27,1243,350-->

```Python
assert "asd"[2] == "d"
assert [39, "omg", 'asd', 3.4][2] == "asd"
```

Indices can be {@{negative, in which case it counts from the back}@}: <!--SR:!2027-12-13,903,334-->

```Python
assert "asd"[-1] == "d"
assert [39, "omg", 'asd', 3.4][-2] == "asd"
```

If {@{the index (but not slicing) is out of range (regardless if it is positive or negative)}@}, then {@{an `IndexError` will be raised}@}. <!--SR:!2026-09-21,565,334!2026-12-07,625,334-->

## manipulation

You can {@{use the [indexing](#indexing) notation to replace the _n_-th item of a list}@}. <!--SR:!2029-07-27,1390,354-->

To {@{add a new item (not replace existing items) to the back of a list}@}, use {@{`list.append(value)`}@}. Its return value is {@{nothing (`None`)}@}. <!--SR:!2026-05-27,468,314!2029-02-07,1256,354!2030-12-30,1760,334-->

To {@{remove an the _n_-th existing item}@}. use {@{`list.pop(index)`, with `index` being _n_ − 1}@}. Note that `index` accepts {@{numbers in the same ways as in the [indexing](#indexing) notation, i.e. negative indices are accepted and have the same meaning}@}. Likewise, if {@{the index is out of range or `list` is empty}@}, then {@{an `IndexError` will be raised}@}. Not specifying {@{the `index` is also okay \(`list.pop()`\)}@}, and `index` will be {@{set to `-1` by default, meaning the last item will be removed}@}. After removing the item, it will {@{return the removed item}@}. <!--SR:!2027-07-30,795,334!2027-01-27,665,334!2027-06-29,782,334!2029-01-17,1240,354!2026-09-20,564,334!2028-06-18,992,334!2028-11-01,1176,350!2026-03-21,136,397-->

To {@{concatenate/join two lists (or strings)}@}, use {@{the `+` operator}@}. Note that {@{the resulting list is different from the original 2 lists, i.e. modifying the resulting list will not modify the original 2 lists}@}. Since {@{`str`s cannot be modified}@}, the above is irrelevant for strings. If {@{the `+` operator is applied between different types}@}, then {@{a `TypeError` will be raised}@}. <!--SR:!2031-03-20,1875,376!2031-03-27,1882,376!2031-04-19,1902,376!2031-04-29,1911,376!2031-04-11,1896,376!2031-04-24,1907,376-->

## length

{@{The length (`int`) of a sequence, including but not limited to `list` and `str`}@}, can be determined by {@{`len(list)` (but not `list.len()`)}@}. <!--SR:!2028-12-26,1223,354!2029-06-05,1348,354-->

## aggregate functions

Aggregate functions {@{summarize a result from a list}@}. <!--SR:!2026-12-16,634,334-->

- `max(list)` ::@:: Returns the maximum item. If `list` is empty, a `ValueError` is raised. If `list` consists of `float`s and `int`s only, the largest item (the originally leftmost one is returned if there are multiple largest items) will be returned, and no type conversion is done. If `list` consists of `str`s only, then the last string, ordered lexicographically (the originally leftmost one is returned if there are multiple first strings), is returned. If `list` mixes incompatible types (e.g. `int` and `str`), then a `TypeError` is raised. <!--SR:!2026-11-30,524,294!2026-04-01,389,294-->
- `min(list)` ::@:: Returns the maximum item. If `list` is empty, a `ValueError` is raised. If the `list` consists of `float`s and `int`s only, the smallest item (the originally leftmost one is returned if there are multiple largest items) will be returned, and no type conversion is done. If `list` consists of `str`s only, then the first string, ordered lexicographically (the originally leftmost one is returned if there are multiple first strings), is returned. If `list` mixes incompatible types (e.g. `int` and `str`), then a `TypeError` is raised. <!--SR:!2026-09-08,556,334!2027-07-21,786,334-->
- `sum(list)` ::@:: Returns the sum of elements in the list. If the `list` is empty, an `int`, `0`, is returned. If `list` consists of `float`s and `int`s only, the sum is returned. The return type is `float` if there is at least one `float` in `list`, otherwise the return type is `int`. If `list` contains incompatible types (e.g. `str`), then a `TypeError` is raised. <!--SR:!2026-04-27,444,314!2026-03-24,418,314-->

## search functions

- `val in list`, `val not in list` ::@:: Returns a `bool` indicating whether `val` is in `list`. Equality is compared using `==`, so `0.0 in [0]` is `True` instead of `False`. The `not in` operator simply inverts the `bool` returned by `in` operator. <!--SR:!2031-12-14,2105,400!2026-03-22,415,380-->
- `list.count(val)` ::@:: Count the number of `val`s in `list`. Returns `0` if `val` is not found in the list. Equality is compared using `==`, so `[0, 0.0].count(0.0)` is `2` instead of `1`. <!--SR:!2027-08-14,810,356!2031-04-05,1891,376-->
- `list.index(val)` ::@:: Returns the index of `val` in `list`. The index of the leftmost item is returned if there are multiple matching items. Raises `ValueError` if `val` is not found in the list. Equality is compared using `==`, so `[0, 0.0].index(0.0)` is `0` instead of `1`. <!--SR:!2031-03-31,1886,376!2031-03-19,1874,376-->
