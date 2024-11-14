---
aliases:
  - statements
tags:
  - flashcard/active/special/MySQL/statements
  - language/in/English
---

# statements

## common statements

- `ALTER TABLE table_name [alter_option[, ...]]` ::@:: Modify the table named `table_name` by the options `alter_option`.
- `CREATE DATABASE database_name` ::@:: Create a database named `database_name`.
- `CREATE TABLE table_name (create_definition, ...)` ::@:: Create the table named `table_name` defined by the definitions `create_definition`.
- `DELETE FROM table_name [WHERE where_expression]` ::@:: Delete rows from the table named `table_name`. Optionally filter rows for which `where_expression` is true.
- `DESCRIBE table_name` ::@:: Show the table named `table_name`.
- `INSERT INTO table_name (column_name[, ...]) VALUE[S] (value[, ...])[, ...]` ::@:: Add rows with the _n_-th `value` corresponding to the _n_-th column named `column_name` into the table named `table_name`.
- `SELECT select_expression [FROM table_reference[, ...]] [WHERE where_expression] [ORDER BY order_by_expression [ASC | DESC]] [LIMIT {[offset,] count | count OFFSET offset}]` ::@:: Show rows from the tables named `table_reference` according to `select_expression`. Optionally filter rows for which `where_expression` is true. Optionally order rows by the `order_by_expression` in ascending order if unspecified or `ASC`, or descending if `DESC`. Optionally limit the number of rows to `count` starting from the 0-based `offset` if specified.
- `SHOW DATABASES` ::@:: Show databases.
- `UPDATE table_name SET assignment[, ...] [WHERE where_expression]` ::@:: Update columns of rows with new values according to `assignment`s in the table `table_name`. Optionally filter rows for which `where_expression` is true.
- `USE database_name` ::@:: Use the database named `database_name` as the default database for sequent statements.

## common expressions

- `alter_option`
  - `ADD {INDEX | KEY} [USING {BTREE | HASH}] (key_part, ...)` ::@:: Add an index indexed by `key_part` using the specified algorithm.
- `create_definition`
  - `column_name column_definition` ::@:: Define a column named `column_name` with the definition `column_definition`.
  - `{INDEX | KEY} [USING {BTREE | HASH}] (key_part, ...)` ::@:: An index indexed by `key_part` using the specified algorithm.
  - `PRIMARY KEY [USING {BTREE | HASH}] (key_part, ...)` ::@:: A unique index indexed by `key_part`, which must be `NOT NULL` columns, using the specified algorithm.
- `select_expression`
  - `*` ::@:: Select all columns.
  - `COUNT(expression)` ::@:: Number of selected non-`NULL` rows for `expression`.
- `table_reference`
  - `table_name [JOIN table_name...] [ON on_expression] [AND on_expression...]` ::@:: [`INNER JOIN`](join%20(SQL).md#inner%20join) _n_ tables named `table_name` joined by _n_ - 1 expressions `on_expression`.
