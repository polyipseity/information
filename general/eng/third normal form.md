---
aliases:
  - 3NF
  - third normal form
tags:
  - flashcard/active/general/eng/third_normal_form
  - language/in/English
---

# third normal form

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## implementation

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("d93d", "3ffa"),
  (
    "No duplicated data. To deduplicate data, move them to a new table.",
    "Add a [primary key](primary%20key.md) column to each row. Auto-incrementing integer data types are recommended.",
    'Reference data from other tables using the primary key. The data referencing primary keys are called "[foreign keys](foreign%20key.md)", while other non-[primary key](primary%20key.md) data are called "logical keys".',
  ),
)
```

A good way to satisfy the third normal form is by following the below three rules, which works well with the [SQL](SQL.md) [`INNER JOIN`](join%20(SQL).md#inner%20join) clause:

<!--pytextgen generate section="d93d"--><!-- The following content is generated at 2025-04-18T00:40:29.994114+08:00. Any edits will be overridden! -->

> 1. No duplicated data. To deduplicate data, move them to a new table.
> 2. Add a [primary key](primary%20key.md) column to each row. Auto-incrementing integer data types are recommended.
> 3. Reference data from other tables using the primary key. The data referencing primary keys are called "[foreign keys](foreign%20key.md)", while other non-[primary key](primary%20key.md) data are called "logical keys".

<!--/pytextgen-->

<!--pytextgen generate section="3ffa"--><!-- The following content is generated at 2025-04-18T00:40:30.028585+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←No duplicated data. To deduplicate data, move them to a new table.
- No duplicated data. To deduplicate data, move them to a new table.→::@::←Add a [primary key](primary%20key.md) column to each row. Auto-incrementing integer data types are recommended.
- Add a [primary key](primary%20key.md) column to each row. Auto-incrementing integer data types are recommended.→::@::←Reference data from other tables using the primary key. The data referencing primary keys are called "[foreign keys](foreign%20key.md)", while other non-[primary key](primary%20key.md) data are called "logical keys".
- Reference data from other tables using the primary key. The data referencing primary keys are called "[foreign keys](foreign%20key.md)", while other non-[primary key](primary%20key.md) data are called "logical keys".→::@::←_(end)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/third_normal_form) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
