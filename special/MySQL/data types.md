---
aliases:
  - data types
tags:
  - flashcard/active/special/MySQL/data_types
  - language/in/English
---

# data types

## common data types

- date and time data types ::@:: `DATE`, `DATETIME`, `TIME`, `TIMESTAMP`, `YEAR`
  - `DATE` ::@:: `YYYY-MM-DD` that ranges from `1000-01-01` to `9999-12-31`.
  - `DATETIME` ::@:: `YYYY-MM-DD hh:mm:ss[.fraction]` that ranges from `1000-01-01 00:00:00.000000` to `9999-12-31 23:59:59.499999`.
  - `TIME` ::@:: `hh[h]:mm:ss[.fraction]` that ranges from `-838:59:59.000000` to `838:59:59.000000`.
  - `TIMESTAMP` ::@:: `YYYY-MM-DD hh:mm:ss[.fraction]` UTC that ranges from `1970-01-01 00:00:01.000000` to `2038-01-19 03:14:07.499999`.
  - `YEAR` ::@:: `Y[YYY]` that ranges from `1901` to `2155`.
- numeric data types ::@:: `BIGINT`, `BIT`, `DECIMAL`, `DOUBLE`, `FLOAT`, `INT`, `INTEGER`, `MEDIUMINT`, `NUMERIC`, `SMALLINT`, `TINYINT`
  - floating-point data types ::@:: `FLOAT`, `DOUBLE`; inexact
    - `FLOAT` ::@:: Likely [single-precision floating-point format](../../general/single-precision%20floating-point%20format.md).
    - `DOUBLE` ::@:: Likely [double-precision floating-point format](../../general/double-precision%20floating-point%20format.md).
  - integer data types ::@:: `TINYINT`, `SMALLINT`, `INT`, `INTEGER`, `MEDIUMINT`, `BIGINT`
    - `TINYINT` ::@:: Signed is from -2<sup>7</sup> to 2<sup>7</sup> - 1 and unsigned is from 0 to 2<sup>8</sup> - 1.
    - `SMALLINT` ::@:: Signed is from -2<sup>15</sup> to 2<sup>15</sup> - 1 and unsigned is 0 to 2<sup>16</sup> - 1.
    - `INT`, `INTEGER` ::@:: Signed is from -2<sup>23</sup> to 2<sup>23</sup> - 1 and unsigned is from 0 to 2<sup>24</sup> - 1.
    - `MEDIUMINT` ::@:: Signed is from -2<sup>31</sup> to 2<sup>31</sup> - 1 and unsigned is from 0 to 2<sup>32</sup> - 1.
    - `BIGINT` ::@:: Signed is from -2<sup>63</sup> to 2<sup>63</sup> - 1 and unsigned is from 0 to 2<sup>64</sup> - 1.
- string data types ::@:: `BINARY`, `BLOB`, `CHAR`, `ENUM`, `SET`, `TEXT`, `VARBINARY`, `VARCHAR`
  - `BINARY`, `VARBINARY` ::@:: Binary strings. Length of the former is fixed and of the latter is variable.
    - `BINARY` ::@:: Up to 2<sup>8</sup> - 1 bytes of fixed-size binary string.
    - `VARBINARY` ::@:: Up to 2<sup>16</sup> - 1 bytes of binary string. Shared among columns in a row.
  - `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, `LONGBLOB` ::@:: Unindexed prefix-indexable long binary strings.
    - `TINYBLOB` ::@:: Up to 2<sup>8</sup> - 1 bytes of binary string.
    - `BLOB` ::@:: Up to 2<sup>16</sup> - 1 bytes of binary string.
    - `MEDIUMBLOB` ::@:: Up to 2<sup>24</sup> - 1 bytes of binary string.
    - `LONGBLOB` ::@:: Up to 2<sup>32</sup> - 1 bytes of binary string.
  - `CHAR`, `VARCHAR` ::@:: Strings. Length of the former is fixed and of the latter is variable.
    - `CHAR` ::@:: Up to 2<sup>8</sup> - 1 bytes of fixed-size string.
    - `VARCHAR` ::@:: Up to 2<sup>16</sup> - 1 bytes of string. Shared among columns in a row.
  - `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, `LONGTEXT` ::@:: Unindexed prefix-indexable long strings.
    - `TINYTEXT` ::@:: Up to 2<sup>8</sup> - 1 bytes of string.
    - `TEXT` ::@:: Up to 2<sup>16</sup> - 1 bytes of string.
    - `MEDIUMTEXT` ::@:: Up to 2<sup>24</sup> - 1 bytes of string.
    - `LONGTEXT` ::@:: Up to 2<sup>32</sup> - 1 bytes of string.
