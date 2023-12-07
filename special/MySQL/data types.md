---
aliases:
  - data types
tags:
  - flashcards/special/MySQL/data_types
---

# data types

## common data types

- {{date and time data types}}: {{`DATE`, `DATETIME`, `TIME`, `TIMESTAMP`, `YEAR`}}
  - {{`DATE`}}: {{`YYYY-MM-DD`; ranges from `1000-01-01` to `9999-12-31`}}
  - {{`DATETIME`}}: {{`YYYY-MM-DD hh:mm:ss[.fraction]`; ranges from `1000-01-01 00:00:00.000000` to `9999-12-31 23:59:59.499999`}}
  - {{`TIME`}}: {{`hh[h]:mm:ss[.fraction]`; ranges from `-838:59:59.000000` to `838:59:59.000000`}}
  - {{`TIMESTAMP`}}: {{`YYYY-MM-DD hh:mm:ss[.fraction]` UTC; ranges from `1970-01-01 00:00:01.000000` to `2038-01-19 03:14:07.499999`}}
  - {{`YEAR`}}: {{`Y[YYY]`; ranges from `1901` to `2155`}}
- {{numeric data types}}: {{`BIGINT`, `BIT`, `DECIMAL`, `DOUBLE`, `FLOAT`, `INT`, `INTEGER`, `MEDIUMINT`, `NUMERIC`, `SMALLINT`, `TINYINT`}}
  - {{floating-point data types}}: {{`FLOAT`, `DOUBLE`; inexact}}
    - {{`FLOAT`}}: {{likely [single-precision floating-point format](../../general/single-precision%20floating-point%20format.md)}}
    - {{`DOUBLE`}}: {{likely [double-precision floating-point format](../../general/double-precision%20floating-point%20format.md)}}
  - {{integer data types}}: {{`TINYINT`, `SMALLINT`, `INT`, `INTEGER`, `MEDIUMINT`, `BIGINT`}}
    - {{`TINYINT`}}: {{signed is from -2<sup>7</sup> to 2<sup>7</sup> - 1, unsigned is from 0 to 2<sup>8</sup> - 1}}
    - {{`SMALLINT`}}: {{signed is from -2<sup>15</sup> to 2<sup>15</sup> - 1, unsigned is 0 to 2<sup>16</sup> - 1}}
    - {{`INT`, `INTEGER`}}: {{signed is from -2<sup>23</sup> to 2<sup>23</sup> - 1, unsigned is from 0 to 2<sup>24</sup> - 1}}
    - {{`MEDIUMINT`}}: {{signed is from -2<sup>31</sup> to 2<sup>31</sup> - 1, unsigned is from 0 to 2<sup>32</sup> - 1}}
    - {{`BIGINT`}}: {{signed is from -2<sup>63</sup> to 2<sup>63</sup> - 1, unsigned is from 0 to 2<sup>64</sup> - 1}}
- {{string data types}}: {{`BINARY`, `BLOB`, `CHAR`, `ENUM`, `SET`, `TEXT`, `VARBINARY`, `VARCHAR`}}
  - {{`BINARY`, `VARBINARY`}}: {{binary strings; length of the former is fixed and of the latter is variable}}
    - {{`BINARY`}}: {{up to 2<sup>8</sup> - 1 bytes of fixed-size binary string}}
    - {{`VARBINARY`}}: {{up to 2<sup>16</sup> - 1 bytes of binary string; shared among columns in a row}}
  - {{`BLOB`}}: {{unindexed prefix-indexable long binary strings; includes `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, and `LONGBLOB`}}
    - {{`TINYBLOB`}}: {{up to 2<sup>8</sup> - 1 bytes of binary string}}
    - {{`BLOB`}}: {{up to 2<sup>16</sup> - 1 bytes of binary string}}
    - {{`MEDIUMBLOB`}}: {{up to 2<sup>24</sup> - 1 bytes of binary string}}
    - {{`LONGBLOB`}}: {{up to 2<sup>32</sup> - 1 bytes of binary string}}
  - {{`CHAR`, `VARCHAR`}}: {{strings; length of the former is fixed and of the latter is variable}}
    - {{`CHAR`}}: {{up to 2<sup>8</sup> - 1 bytes of fixed-size string}}
    - {{`VARCHAR`}}: {{up to 2<sup>16</sup> - 1 bytes of string; shared among columns in a row}}
  - {{`TEXT`}}: {{unindexed prefix-indexable long strings; includes `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, and `LONGTEXT`}}
    - {{`TINYTEXT`}}: {{up to 2<sup>8</sup> - 1 bytes of string}}
    - {{`TEXT`}}: {{up to 2<sup>16</sup> - 1 bytes of string}}
    - {{`MEDIUMTEXT`}}: {{up to 2<sup>24</sup> - 1 bytes of string}}
    - {{`LONGTEXT`}}: {{up to 2<sup>32</sup> - 1 bytes of string}} <!--SR:!2024-02-20,109,310!2024-01-16,92,310!2024-01-06,85,310!2024-03-14,98,290!2024-01-20,96,310!2023-12-21,48,290!2024-01-25,101,310!2024-01-14,41,210!2023-12-29,77,310!2023-12-21,26,190!2024-01-07,85,310!2023-12-17,65,290!2024-02-08,97,310!2024-04-14,134,270!2024-01-25,101,310!2024-02-18,107,310!2024-02-18,107,310!2024-02-11,100,310!2023-12-30,78,310!2024-02-14,103,310!2024-01-07,86,310!2024-01-20,96,310!2024-01-08,87,310!2024-01-19,95,310!2024-01-19,95,310!2024-01-05,84,310!2024-02-10,99,310!2023-12-23,68,290!2023-12-09,36,290!2024-01-13,89,310!2023-12-24,69,290!2024-02-09,98,310!2024-01-13,91,310!2024-01-13,71,290!2024-01-02,81,310!2024-02-17,106,310!2024-01-17,93,310!2024-01-10,88,310!2024-01-19,95,310!2024-02-16,105,310!2024-02-09,98,310!2024-01-20,96,310!2023-12-31,79,310!2024-02-08,97,310!2024-02-10,99,310!2024-01-18,94,310!2024-01-03,82,310!2024-01-12,90,310!2024-01-11,89,310!2024-01-08,86,310!2024-01-16,92,310!2024-02-07,96,310!2024-01-01,80,310!2024-01-07,86,310!2024-01-24,100,310!2024-02-11,100,310!2024-01-09,88,310!2024-01-14,92,310!2024-01-09,87,310!2024-01-23,99,310!2023-12-12,60,290!2024-02-13,102,310!2024-01-18,94,310!2024-01-01,80,310!2023-12-15,63,290!2024-02-20,109,310-->
