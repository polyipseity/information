---
aliases:
  - statements
tags:
  - flashcard/active/special/MySQL/statements
  - language/in/English
---

# statements

## common statements

- `ALTER TABLE table_name [alter_option[, ...]]` ::: Modify the table named `table_name` by the options `alter_option`. <!--SR:!2024-10-18,278,310!2025-05-12,451,330-->
- `CREATE DATABASE database_name` ::: Create a database named `database_name`. <!--SR:!2025-01-19,374,330!2025-02-17,397,330-->
- `CREATE TABLE table_name (create_definition, ...)` ::: Create the table named `table_name` defined by the definitions `create_definition`. <!--SR:!2026-02-19,594,299!2024-09-16,273,319-->
- `DELETE FROM table_name [WHERE where_expression]` ::: Delete rows from the table named `table_name`. Optionally filter rows for which `where_expression` is true. <!--SR:!2024-10-29,291,319!2025-11-27,540,299-->
- `DESCRIBE table_name` ::: Show the table named `table_name`. <!--SR:!2025-07-09,399,299!2025-03-04,413,339-->
- `INSERT INTO table_name (column_name[, ...]) VALUE[S] (value[, ...])[, ...]` ::: Add rows with the _n_-th `value` corresponding to the _n_-th column named `column_name` into the table named `table_name`. <!--SR:!2025-06-15,364,299!2024-12-28,334,319-->
- `SELECT select_expression [FROM table_reference[, ...]] [WHERE where_expression] [ORDER BY order_by_expression [ASC | DESC]] [LIMIT {[offset,] count | count OFFSET offset}]` ::: Show rows from the tables named `table_reference` according to `select_expression`. Optionally filter rows for which `where_expression` is true. Optionally order rows by the `order_by_expression` in ascending order if unspecified or `ASC`, or descending if `DESC`. Optionally limit the number of rows to `count` starting from the 0-based `offset` if specified. <!--SR:!2025-12-03,540,299!2026-08-18,702,299-->
- `SHOW DATABASES` ::: Show databases. <!--SR:!2025-06-30,493,339!2025-02-11,396,339-->
- `UPDATE table_name SET assignment[, ...] [WHERE where_expression]` ::: Update columns of rows with new values according to `assignment`s in the table `table_name`. Optionally filter rows for which `where_expression` is true. <!--SR:!2026-02-09,585,299!2025-02-18,333,279-->
- `USE database_name` ::: Use the database named `database_name` as the default database for sequent statements. <!--SR:!2025-02-18,400,339!2025-02-15,400,339-->

## common expressions

- `alter_option`
  - `ADD {INDEX | KEY} [USING {BTREE | HASH}] (key_part, ...)` ::: Add an index indexed by `key_part` using the specified algorithm. <!--SR:!2024-10-06,234,250!2025-05-21,458,330-->
- `create_definition`
  - `column_name column_definition` ::: Define a column named `column_name` with the definition `column_definition`. <!--SR:!2024-11-22,303,310!2025-04-20,434,330-->
  - `{INDEX | KEY} [USING {BTREE | HASH}] (key_part, ...)` ::: An index indexed by `key_part` using the specified algorithm. <!--SR:!2026-05-17,639,299!2024-12-24,331,319-->
  - `PRIMARY KEY [USING {BTREE | HASH}] (key_part, ...)` ::: A unique index indexed by `key_part`, which must be `NOT NULL` columns, using the specified algorithm. <!--SR:!2026-01-25,538,319!2026-05-01,605,319-->
- `select_expression`
  - `*` ::: Select all columns. <!--SR:!2025-07-06,497,339!2024-10-02,270,319-->
  - `COUNT(expression)` ::: Number of selected non-`NULL` rows for `expression`. <!--SR:!2025-05-12,453,339!2024-10-20,283,319-->
- `table_reference`
  - `table_name [JOIN table_name...] [ON on_expression] [AND on_expression...]` ::: [`INNER JOIN`](join%20(SQL).md#inner%20join) _n_ tables named `table_name` joined by _n_ - 1 expressions `on_expression`. <!--SR:!2024-12-06,240,279!2026-06-09,666,299-->
