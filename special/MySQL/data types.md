---
aliases:
  - data types
tags:
  - flashcards/special/MySQL/data_types
  - languages/in/English
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
    - {{`LONGTEXT`}}: {{up to 2<sup>32</sup> - 1 bytes of string}} <!--SR:!2024-02-20,109,310!2025-02-13,394,330!2025-01-04,364,330!2024-03-14,98,290!2025-03-10,411,330!2024-03-22,67,270!2025-03-31,431,330!2024-03-11,37,190!2024-11-21,328,330!2024-03-03,23,150!2025-01-04,363,330!2024-05-17,120,290!2025-03-29,415,330!2024-04-14,134,270!2025-04-01,432,330!2024-02-18,107,310!2024-02-18,107,310!2025-04-13,427,330!2024-11-28,334,330!2025-04-29,440,330!2025-01-09,368,330!2025-03-09,410,330!2024-10-03,269,310!2025-03-01,407,330!2025-02-27,405,330!2024-12-31,361,330!2025-04-08,422,330!2024-07-07,196,290!2024-02-19,53,270!2025-01-28,381,330!2024-09-26,277,310!2025-04-06,422,330!2024-10-20,281,310!2024-08-05,205,290!2024-12-13,346,330!2024-02-17,106,310!2025-02-18,398,330!2025-01-21,376,330!2025-02-28,406,330!2024-02-16,105,310!2025-04-05,421,330!2025-03-08,409,330!2024-08-30,243,310!2025-03-28,414,330!2025-04-12,426,330!2025-02-23,402,330!2024-09-12,253,310!2025-01-31,385,330!2024-02-27,47,290!2024-09-30,266,310!2025-02-12,393,330!2024-12-02,299,310!2024-12-09,342,330!2024-10-01,268,310!2025-03-27,428,330!2025-04-18,432,330!2024-10-08,271,310!2024-10-26,286,310!2024-02-28,48,290!2025-03-23,424,330!2024-05-07,116,290!2025-04-25,437,330!2025-02-22,401,330!2024-12-08,341,330!2024-06-14,182,290!2024-02-20,109,310-->
