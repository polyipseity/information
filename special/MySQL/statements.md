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
- {{`USE database_name`}}: {{use the database named `database_name` as the default database for sequent statements}} <!--SR:!2023-10-15,23,290!2023-10-18,26,290!2023-10-14,22,290!2023-10-15,23,290!2023-10-13,21,299!2023-10-08,16,279!2023-10-13,21,299!2023-10-07,15,279!2023-10-15,23,299!2023-10-14,22,299!2023-10-12,20,299!2023-10-16,24,299!2023-10-12,20,299!2023-10-17,25,299!2023-10-18,26,299!2023-10-14,22,299!2023-10-15,23,299!2023-11-18,43,279!2023-10-15,23,299!2023-10-13,21,299-->

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
  - {{`table_name [JOIN table_name...] [ON on_expression] [AND on_expression...]`}}: {{[`INNER JOIN`](join%20(SQL).md#inner%20join) _n_ tables named `table_name` joined by _n_ - 1 expressions `on_expression`}} <!--SR:!2023-11-13,38,250!2023-10-18,26,290!2023-10-16,24,290!2023-10-17,25,290!2023-10-17,25,299!2023-10-16,24,299!2023-10-12,20,299!2023-10-13,21,299!2023-10-18,26,299!2023-10-12,20,299!2023-10-17,25,299!2023-10-14,22,299!2023-10-08,16,279!2023-10-16,24,299-->
