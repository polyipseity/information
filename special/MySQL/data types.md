---
aliases:
  - data types
tags:
  - flashcard/special/MySQL/data_types
  - language/in/English
---

# data types

## common data types

- date and time data types ::: `DATE`, `DATETIME`, `TIME`, `TIMESTAMP`, `YEAR` <!--SR:!2025-01-24,339,310!2025-02-13,394,330-->
  - `DATE` ::: `YYYY-MM-DD` that ranges from `1000-01-01` to `9999-12-31`. <!--SR:!2025-01-04,364,330!2025-04-12,394,310-->
  - `DATETIME` ::: `YYYY-MM-DD hh:mm:ss[.fraction]` that ranges from `1000-01-01 00:00:00.000000` to `9999-12-31 23:59:59.499999`. <!--SR:!2025-03-10,411,330!2024-09-18,180,270-->
  - `TIME` ::: `hh[h]:mm:ss[.fraction]` that ranges from `-838:59:59.000000` to `838:59:59.000000`. <!--SR:!2025-03-31,431,330!2024-06-19,100,210-->
  - `TIMESTAMP` ::: `YYYY-MM-DD hh:mm:ss[.fraction]` UTC that ranges from `1970-01-01 00:00:01.000000` to `2038-01-19 03:14:07.499999`. <!--SR:!2024-11-21,328,330!2024-04-06,34,150-->
  - `YEAR` ::: `Y[YYY]` that ranges from `1901` to `2155`. <!--SR:!2025-01-04,363,330!2024-05-17,120,290-->
- numeric data types ::: `BIGINT`, `BIT`, `DECIMAL`, `DOUBLE`, `FLOAT`, `INT`, `INTEGER`, `MEDIUMINT`, `NUMERIC`, `SMALLINT`, `TINYINT` <!--SR:!2025-03-29,415,330!2024-04-14,134,270-->
  - floating-point data types ::: `FLOAT`, `DOUBLE`; inexact <!--SR:!2025-04-01,432,330!2025-05-20,457,330-->
    - `FLOAT` ::: Likely [single-precision floating-point format](../../general/single-precision%20floating-point%20format.md). <!--SR:!2025-05-21,458,330!2025-04-13,427,330-->
    - `DOUBLE` ::: Likely [double-precision floating-point format](../../general/double-precision%20floating-point%20format.md). <!--SR:!2024-11-28,334,330!2025-04-29,440,330-->
  - integer data types ::: `TINYINT`, `SMALLINT`, `INT`, `INTEGER`, `MEDIUMINT`, `BIGINT` <!--SR:!2025-01-09,368,330!2025-03-09,410,330-->
    - `TINYINT` ::: Signed is from -2<sup>7</sup> to 2<sup>7</sup> - 1 and unsigned is from 0 to 2<sup>8</sup> - 1. <!--SR:!2024-10-03,269,310!2025-03-01,407,330-->
    - `SMALLINT` ::: Signed is from -2<sup>15</sup> to 2<sup>15</sup> - 1 and unsigned is 0 to 2<sup>16</sup> - 1. <!--SR:!2025-02-27,405,330!2024-12-31,361,330-->
    - `INT`, `INTEGER` ::: Signed is from -2<sup>23</sup> to 2<sup>23</sup> - 1 and unsigned is from 0 to 2<sup>24</sup> - 1. <!--SR:!2025-04-08,422,330!2024-07-07,196,290-->
    - `MEDIUMINT` ::: Signed is from -2<sup>31</sup> to 2<sup>31</sup> - 1 and unsigned is from 0 to 2<sup>32</sup> - 1. <!--SR:!2024-09-07,201,290!2025-01-28,381,330-->
    - `BIGINT` ::: Signed is from -2<sup>63</sup> to 2<sup>63</sup> - 1 and unsigned is from 0 to 2<sup>64</sup> - 1. <!--SR:!2024-09-26,277,310!2025-04-06,422,330-->
- string data types ::: `BINARY`, `BLOB`, `CHAR`, `ENUM`, `SET`, `TEXT`, `VARBINARY`, `VARCHAR` <!--SR:!2024-10-20,281,310!2024-08-05,205,290-->
  - `BINARY`, `VARBINARY` ::: Binary strings. Length of the former is fixed and of the latter is variable. <!--SR:!2024-12-13,346,330!2025-05-16,454,330-->
    - `BINARY` ::: Up to 2<sup>8</sup> - 1 bytes of fixed-size binary string. <!--SR:!2025-02-18,398,330!2025-01-21,376,330-->
    - `VARBINARY` ::: Up to 2<sup>16</sup> - 1 bytes of binary string. Shared among columns in a row. <!--SR:!2025-02-28,406,330!2025-01-06,325,310-->
  - `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, `LONGBLOB` ::: Unindexed prefix-indexable long binary strings. <!--SR:!2025-04-05,421,330!2025-03-08,409,330-->
    - `TINYBLOB` ::: Up to 2<sup>8</sup> - 1 bytes of binary string. <!--SR:!2024-08-30,243,310!2025-03-28,414,330-->
    - `BLOB` ::: Up to 2<sup>16</sup> - 1 bytes of binary string. <!--SR:!2025-04-12,426,330!2025-02-23,402,330-->
    - `MEDIUMBLOB` ::: Up to 2<sup>24</sup> - 1 bytes of binary string. <!--SR:!2024-09-12,253,310!2025-01-31,385,330-->
    - `LONGBLOB` ::: Up to 2<sup>32</sup> - 1 bytes of binary string. <!--SR:!2024-07-11,135,290!2024-09-30,266,310-->
  - `CHAR`, `VARCHAR` ::: Strings. Length of the former is fixed and of the latter is variable. <!--SR:!2025-02-12,393,330!2024-12-02,299,310-->
    - `CHAR` ::: Up to 2<sup>8</sup> - 1 bytes of fixed-size string. <!--SR:!2024-12-09,342,330!2024-10-01,268,310-->
    - `VARCHAR` ::: Up to 2<sup>16</sup> - 1 bytes of string. Shared among columns in a row. <!--SR:!2025-03-27,428,330!2025-04-18,432,330-->
  - `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, `LONGTEXT` ::: Unindexed prefix-indexable long strings. <!--SR:!2024-10-08,271,310!2024-10-26,286,310-->
    - `TINYTEXT` ::: Up to 2<sup>8</sup> - 1 bytes of string. <!--SR:!2024-09-07,192,310!2025-03-23,424,330-->
    - `TEXT` ::: Up to 2<sup>16</sup> - 1 bytes of string. <!--SR:!2024-05-07,116,290!2025-04-25,437,330-->
    - `MEDIUMTEXT` ::: Up to 2<sup>24</sup> - 1 bytes of string. <!--SR:!2025-02-22,401,330!2024-12-08,341,330-->
    - `LONGTEXT` ::: Up to 2<sup>32</sup> - 1 bytes of string. <!--SR:!2024-06-14,182,290!2024-04-16,56,290-->
