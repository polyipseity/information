---
aliases:
  - statements
tags:
  - flashcards/special/MySQL/statements
---

# statements

## common statements

- {{`ALTER TABLE table_name [alter_option[, ...]]`}}: {{modify the table named `table_name` by the options `alter_option`}}
- {{`CREATE DATABASE database_name`}}: {{create a database named `database_name`}}
- {{`CREATE TABLE table_name (create_definition, ...)`}}: {{create the table named `table_name` defined by the definitions `create_definition`}}
- {{`DELETE FROM table_name [WHERE where_expression]`}}: {{delete rows from the table named `table_name`; maybe filter rows for which `where_expression` is true}}
- {{`DESCRIBE table_name`}}: {{show the table named `table_name`}}
- {{`INSERT INTO table_name (column_name[, ...]) VALUE[S] (value[, ...])[, ...]`}}: {{add rows with the _n_-th `value` corresponding to the _n_-th column named `column_name` into the table named `table_name`}}
- {{`SELECT select_expression [FROM table_reference[, ...]] [WHERE where_expression] [ORDER BY order_by_expression [ASC | DESC]] [LIMIT {[offset,] count | count OFFSET offset}]`}}: {{show rows from the tables named `table_reference` according to `select_expression`; maybe filter rows for which `where_expression` is true; maybe order rows by the `order_by_expression` in ascending order if unspecified or `ASC`, or descending if `DESC`; maybe limit the number of rows to `count` starting from the 0-based `offset` if specified}}
- {{`SHOW DATABASES`}}: {{show databases}}
- {{`UPDATE table_name SET assignment[, ...] [WHERE where_expression]`}}: {{update columns of rows with new values according to `assignment`s in the table `table_name`; maybe filter rows for which `where_expression` is true}}
- {{`USE database_name`}}: {{use the database named `database_name` as the default database for sequent statements}} <!--SR:!2024-01-14,90,310!2024-02-16,105,310!2024-01-09,87,310!2024-01-17,93,310!2023-12-19,67,299!2023-12-18,66,299!2024-01-12,91,319!2024-06-05,181,299!2023-12-20,65,299!2024-01-16,94,319!2024-01-05,84,319!2024-01-29,105,319!2024-06-11,181,299!2024-01-21,79,299!2024-02-23,112,319!2024-01-12,90,319!2023-12-21,66,299!2024-03-22,119,279!2024-01-15,91,319!2024-01-12,91,319-->

## common expressions

- `alter_option`
  - {{`ADD {INDEX | KEY} [USING {BTREE | HASH}] (key_part, ...)`}}: {{add an index indexed by `key_part` using the specified algorithm}}
- `create_definition`
  - {{`column_name column_definition`}}: {{define a column named `column_name` with the definition `column_definition`}}
  - {{`{INDEX | KEY} [USING {BTREE | HASH}] (key_part, ...)`}}: {{an index indexed by `key_part` using the specified algorithm}}
  - {{`PRIMARY KEY [USING {BTREE | HASH}] (key_part, ...)`}}: {{a unique index indexed by `key_part`, which must be `NOT NULL` columns, using the specified algorithm}}
- `select_expression`
  - {{`*`}}: {{select all columns}}
  - {{`COUNT(expression)`}}: {{number of selected non-`NULL` rows for `expression`}}
- `table_reference`
  - {{`table_name [JOIN table_name...] [ON on_expression] [AND on_expression...]`}}: {{[`INNER JOIN`](join%20(SQL).md#inner%20join) _n_ tables named `table_name` joined by _n_ - 1 expressions `on_expression`}} <!--SR:!2024-02-15,94,250!2024-02-18,107,310!2024-01-22,98,310!2024-02-11,100,310!2024-01-14,72,299!2024-01-28,104,319!2024-01-08,87,319!2024-01-10,89,319!2024-02-24,113,319!2024-01-06,85,319!2024-02-14,103,319!2024-01-11,89,319!2023-12-16,64,299!2023-12-30,75,299-->
