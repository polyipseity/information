---
aliases:
  - data types
tags:
  - flashcard/active/special/MySQL/data_types
  - language/in/English
---

# data types

## common data types

- date and time data types ::@:: `DATE`, `DATETIME`, `TIME`, `TIMESTAMP`, `YEAR` <!--SR:!2025-01-24,339,310!2025-02-13,394,330-->
  - `DATE` ::@:: `YYYY-MM-DD` that ranges from `1000-01-01` to `9999-12-31`. <!--SR:!2025-01-04,364,330!2025-04-12,394,310-->
  - `DATETIME` ::@:: `YYYY-MM-DD hh:mm:ss[.fraction]` that ranges from `1000-01-01 00:00:00.000000` to `9999-12-31 23:59:59.499999`. <!--SR:!2025-03-10,411,330!2026-01-16,485,270-->
  - `TIME` ::@:: `hh[h]:mm:ss[.fraction]` that ranges from `-838:59:59.000000` to `838:59:59.000000`. <!--SR:!2025-03-31,431,330!2025-01-16,211,210-->
  - `TIMESTAMP` ::@:: `YYYY-MM-DD hh:mm:ss[.fraction]` UTC that ranges from `1970-01-01 00:00:01.000000` to `2038-01-19 03:14:07.499999`. <!--SR:!2025-05-03,163,310!2025-03-20,186,170-->
  - `YEAR` ::@:: `Y[YYY]` that ranges from `1901` to `2155`. <!--SR:!2025-01-04,363,330!2025-09-17,483,310-->
- numeric data types ::@:: `BIGINT`, `BIT`, `DECIMAL`, `DOUBLE`, `FLOAT`, `INT`, `INTEGER`, `MEDIUMINT`, `NUMERIC`, `SMALLINT`, `TINYINT` <!--SR:!2025-03-29,415,330!2025-04-11,361,270-->
  - floating-point data types ::@:: `FLOAT`, `DOUBLE`; inexact <!--SR:!2025-04-01,432,330!2025-05-20,457,330-->
    - `FLOAT` ::@:: Likely [single-precision floating-point format](../../general/single-precision%20floating-point%20format.md). <!--SR:!2025-05-21,458,330!2025-04-13,427,330-->
    - `DOUBLE` ::@:: Likely [double-precision floating-point format](../../general/double-precision%20floating-point%20format.md). <!--SR:!2029-01-26,1520,350!2025-04-29,440,330-->
  - integer data types ::@:: `TINYINT`, `SMALLINT`, `INT`, `INTEGER`, `MEDIUMINT`, `BIGINT` <!--SR:!2025-01-09,368,330!2025-03-09,410,330-->
    - `TINYINT` ::@:: Signed is from -2<sup>7</sup> to 2<sup>7</sup> - 1 and unsigned is from 0 to 2<sup>8</sup> - 1. <!--SR:!2027-01-14,833,310!2025-03-01,407,330-->
    - `SMALLINT` ::@:: Signed is from -2<sup>15</sup> to 2<sup>15</sup> - 1 and unsigned is 0 to 2<sup>16</sup> - 1. <!--SR:!2025-02-27,405,330!2024-12-31,361,330-->
    - `INT`, `INTEGER` ::@:: Signed is from -2<sup>23</sup> to 2<sup>23</sup> - 1 and unsigned is from 0 to 2<sup>24</sup> - 1. <!--SR:!2025-04-08,422,330!2026-01-25,567,290-->
    - `MEDIUMINT` ::@:: Signed is from -2<sup>31</sup> to 2<sup>31</sup> - 1 and unsigned is from 0 to 2<sup>32</sup> - 1. <!--SR:!2026-11-25,809,310!2025-01-28,381,330-->
    - `BIGINT` ::@:: Signed is from -2<sup>63</sup> to 2<sup>63</sup> - 1 and unsigned is from 0 to 2<sup>64</sup> - 1. <!--SR:!2027-12-27,1187,330!2025-04-06,422,330-->
- string data types ::@:: `BINARY`, `BLOB`, `CHAR`, `ENUM`, `SET`, `TEXT`, `VARBINARY`, `VARCHAR` <!--SR:!2027-03-10,871,310!2026-03-22,594,290-->
  - `BINARY`, `VARBINARY` ::@:: Binary strings. Length of the former is fixed and of the latter is variable. <!--SR:!2024-12-13,346,330!2025-05-16,454,330-->
    - `BINARY` ::@:: Up to 2<sup>8</sup> - 1 bytes of fixed-size binary string. <!--SR:!2025-02-18,398,330!2025-01-21,376,330-->
    - `VARBINARY` ::@:: Up to 2<sup>16</sup> - 1 bytes of binary string. Shared among columns in a row. <!--SR:!2025-02-28,406,330!2025-01-06,325,310-->
  - `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, `LONGBLOB` ::@:: Unindexed prefix-indexable long binary strings. <!--SR:!2025-04-05,421,330!2025-03-08,409,330-->
    - `TINYBLOB` ::@:: Up to 2<sup>8</sup> - 1 bytes of binary string. <!--SR:!2026-09-21,752,310!2025-03-28,414,330-->
    - `BLOB` ::@:: Up to 2<sup>16</sup> - 1 bytes of binary string. <!--SR:!2025-04-12,426,330!2025-02-23,402,330-->
    - `MEDIUMBLOB` ::@:: Up to 2<sup>24</sup> - 1 bytes of binary string. <!--SR:!2026-11-04,783,310!2025-01-31,385,330-->
    - `LONGBLOB` ::@:: Up to 2<sup>32</sup> - 1 bytes of binary string. <!--SR:!2025-08-06,391,290!2027-11-14,1140,330-->
  - `CHAR`, `VARCHAR` ::@:: Strings. Length of the former is fixed and of the latter is variable. <!--SR:!2025-02-12,393,330!2028-06-11,1286,330-->
    - `CHAR` ::@:: Up to 2<sup>8</sup> - 1 bytes of fixed-size string. <!--SR:!2024-12-09,342,330!2027-11-24,1149,330-->
    - `VARCHAR` ::@:: Up to 2<sup>16</sup> - 1 bytes of string. Shared among columns in a row. <!--SR:!2025-03-27,428,330!2025-04-18,432,330-->
  - `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, `LONGTEXT` ::@:: Unindexed prefix-indexable long strings. <!--SR:!2027-01-25,839,310!2028-03-06,1227,330-->
    - `TINYTEXT` ::@:: Up to 2<sup>8</sup> - 1 bytes of string. <!--SR:!2026-12-09,823,330!2025-03-23,424,330-->
    - `TEXT` ::@:: Up to 2<sup>16</sup> - 1 bytes of string. <!--SR:!2025-04-09,335,290!2025-04-25,437,330-->
    - `MEDIUMTEXT` ::@:: Up to 2<sup>24</sup> - 1 bytes of string. <!--SR:!2025-02-22,401,330!2024-12-08,341,330-->
    - `LONGTEXT` ::@:: Up to 2<sup>32</sup> - 1 bytes of string. <!--SR:!2025-11-23,527,290!2026-01-03,466,290-->
