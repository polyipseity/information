---
aliases:
  - 3NF
  - third normal form
tags:
  - flashcards/general/third_normal_form
  - languages/in/English
---

# third normal form

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```

%%

## implementation

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_seq(
  e.cwf_sects("d93d", "3ffa"),
  (
    "No duplicated data. To deduplicate data, move them to a new table.",
    "Add a [primary key](primary%20key.md) column to each row. Auto-incrementing integer data types are recommended.",
    'Reference data from other tables using the primary key. The data referecing primary keys are called "[foreign keys](foreign%20key.md)", while other non-[primary key](primary%20key.md) data are called "logical keys".',
  ),
)
```

%%

A good way to satisfy the third normal form is by following the below three rules, which works well the [SQL](SQL.md) [`INNER JOIN`](join%20(SQL).md#inner%20join) clause:

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d93d"--><!-- The following content is generated at 2023-09-11T22:15:48.171895+08:00. Any edits will be overridden! -->

> 1. No duplicated data. To deduplicate data, move them to a new table.
> 2. Add a [primary key](primary%20key.md) column to each row. Auto-incrementing integer data types are recommended.
> 3. Reference data from other tables using the primary key. The data referecing primary keys are called "[foreign keys](foreign%20key.md)", while other non-[primary key](primary%20key.md) data are called "logical keys".

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3ffa"--><!-- The following content is generated at 2023-09-11T22:15:48.183823+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←No duplicated data. To deduplicate data, move them to a new table.
2. No duplicated data. To deduplicate data, move them to a new table.→:::←Add a [primary key](primary%20key.md) column to each row. Auto-incrementing integer data types are recommended.
3. Add a [primary key](primary%20key.md) column to each row. Auto-incrementing integer data types are recommended.→:::←Reference data from other tables using the primary key. The data referecing primary keys are called "[foreign keys](foreign%20key.md)", while other non-[primary key](primary%20key.md) data are called "logical keys".
4. Reference data from other tables using the primary key. The data referecing primary keys are called "[foreign keys](foreign%20key.md)", while other non-[primary key](primary%20key.md) data are called "logical keys".→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/third_normal_form) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
