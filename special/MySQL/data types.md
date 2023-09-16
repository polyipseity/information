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
		- {{`BINARY`}}: {{up to 2^8 - 1 bytes of fixed-size binary string}}
		- {{`VARBINARY`}}: {{up to 2^16 - 1 bytes of binary string; shared among columns in a row}}
	- {{`BLOB`}}: {{unindexed prefix-indexable long binary strings; includes `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, and `LONGBLOB`}}
		- {{`TINYBLOB`}}: {{up to 2<sup>8</sup> - 1 bytes of binary string}}
		- {{`BLOB`}}: {{up to 2<sup>16</sup> - 1 bytes of binary string}}
		- {{`MEDIUMBLOB`}}: {{up to 2<sup>24</sup> - 1 bytes of binary string}}
		- {{`LONGBLOB`}}: {{up to 2<sup>32</sup> - 1 bytes of binary string}}
	- {{`CHAR`, `VARCHAR`}}: {{strings; length of the former is fixed and of the latter is variable}}
		- {{`CHAR`}}: {{up to 2^8 - 1 bytes of fixed-size string}}
		- {{`VARCHAR`}}: {{up to 2^16 - 1 bytes of string; shared among columns in a row}}
	- {{`TEXT`}}: {{unindexed prefix-indexable long strings; includes `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, and `LONGTEXT`}}
		- {{`TINYTEXT`}}: {{up to 2<sup>8</sup> - 1 bytes of string}}
		- {{`TEXT`}}: {{up to 2<sup>16</sup> - 1 bytes of string}}
		- {{`MEDIUMTEXT`}}: {{up to 2<sup>24</sup> - 1 bytes of string}}
		- {{`LONGTEXT`}}: {{up to 2<sup>32</sup> - 1 bytes of string}} <!--SR:!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-17,1,230!2023-09-20,4,270!2023-09-17,1,230!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-19,3,250!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270!2023-09-20,4,270-->
