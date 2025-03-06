---
aliases:
  - statements
tags:
  - flashcard/active/special/MySQL/statements
  - language/in/English
---

# statements

## common statements

- `ALTER TABLE table_name [alter_option[, ...]]` ::@:: Modify the table named `table_name` by the options `alter_option`. <!--SR:!2027-02-25,860,310!2025-05-12,451,330-->
- `CREATE DATABASE database_name` ::@:: Create a database named `database_name`. <!--SR:!2029-09-19,1702,350!2030-01-29,1807,350-->
- `CREATE TABLE table_name (create_definition, ...)` ::@:: Create the table named `table_name` defined by the definitions `create_definition`. <!--SR:!2026-02-19,594,299!2027-02-03,870,319-->
- `DELETE FROM table_name [WHERE where_expression]` ::@:: Delete rows from the table named `table_name`. Optionally filter rows for which `where_expression` is true. <!--SR:!2028-05-02,1281,339!2025-11-27,540,299-->
- `DESCRIBE table_name` ::@:: Show the table named `table_name`. <!--SR:!2025-07-09,399,299!2030-06-13,1926,359-->
- `INSERT INTO table_name (column_name[, ...]) VALUE[S] (value[, ...])[, ...]` ::@:: Add rows with the _n_-th `value` corresponding to the _n_-th column named `column_name` into the table named `table_name`. <!--SR:!2025-06-15,364,299!2027-11-27,1064,319-->
- `SELECT select_expression [FROM table_reference[, ...]] [WHERE where_expression] [ORDER BY order_by_expression [ASC | DESC]] [LIMIT {[offset,] count | count OFFSET offset}]` ::@:: Show rows from the tables named `table_reference` according to `select_expression`. Optionally filter rows for which `where_expression` is true. Optionally order rows by the `order_by_expression` in ascending order if unspecified or `ASC`, or descending if `DESC`. Optionally limit the number of rows to `count` starting from the 0-based `offset` if specified. <!--SR:!2025-12-03,540,299!2026-08-18,702,299-->
- `SHOW DATABASES` ::@:: Show databases. <!--SR:!2025-06-30,493,339!2030-03-07,1850,359-->
- `UPDATE table_name SET assignment[, ...] [WHERE where_expression]` ::@:: Update columns of rows with new values according to `assignment`s in the table `table_name`. Optionally filter rows for which `where_expression` is true. <!--SR:!2026-02-09,585,299!2027-09-05,929,279-->
- `USE database_name` ::@:: Use the database named `database_name` as the default database for sequent statements. <!--SR:!2030-03-31,1867,359!2030-03-28,1867,359-->

## common expressions

- `alter_option`
  - `ADD {INDEX | KEY} [USING {BTREE | HASH}] (key_part, ...)` ::@:: Add an index indexed by `key_part` using the specified algorithm. <!--SR:!2026-05-15,584,250!2025-05-21,458,330-->
- `create_definition`
  - `column_name column_definition` ::@:: Define a column named `column_name` with the definition `column_definition`. <!--SR:!2028-06-14,1300,330!2025-04-20,434,330-->
  - `{INDEX | KEY} [USING {BTREE | HASH}] (key_part, ...)` ::@:: An index indexed by `key_part` using the specified algorithm. <!--SR:!2026-05-17,639,299!2027-11-15,1056,319-->
  - `PRIMARY KEY [USING {BTREE | HASH}] (key_part, ...)` ::@:: A unique index indexed by `key_part`, which must be `NOT NULL` columns, using the specified algorithm. <!--SR:!2026-01-25,538,319!2026-05-01,605,319-->
- `select_expression`
  - `*` ::@:: Select all columns. <!--SR:!2025-07-06,497,339!2028-01-04,1189,339-->
  - `COUNT(expression)` ::@:: Number of selected non-`NULL` rows for `expression`. <!--SR:!2025-05-12,453,339!2027-04-09,901,319-->
- `table_reference`
  - `table_name [JOIN table_name...] [ON on_expression] [AND on_expression...]` ::@:: [`INNER JOIN`](join%20(SQL).md#inner%20join) _n_ tables named `table_name` joined by _n_ - 1 expressions `on_expression`. <!--SR:!2026-10-08,670,279!2026-06-09,666,299-->
