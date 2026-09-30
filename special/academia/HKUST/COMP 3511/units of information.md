---
aliases:
  - COMP 3511 units of information
  - binary prefix
  - storage units
  - storage units and notation
  - units of information
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/units_of_information
  - language/in/English
---

# units of information

The basic unit of storage is the bit, which holds 0 or 1; all other storage is built from collections of bits. A byte is 8 bits and, on most computers, the smallest convenient chunk of storage: most computers have an instruction to move a byte but not one to move a bit.

A word is an architecture's native unit of data, made up of one or more bytes. A computer with 64-bit registers and 64-bit addressing typically has 64-bit (8-byte) words and executes many operations on a word rather than a byte at a time.

Computer storage, and most throughput, is measured in bytes and collections of bytes. Network measurements are the exception: they use bits per second, such as Mb/s or Gb/s, because networks move data a bit at a time.

---

Flashcards for this section are as follows:

- bit ::@:: The basic unit of computer storage, holding one of two values, 0 and 1; all other storage is built from collections of bits.
- byte ::@:: 8 bits and, on most computers, the smallest convenient chunk of storage: most have an instruction to move a byte but not a bit.
- word ::@:: A given computer architecture's native unit of data, made up of one or more bytes; a computer with 64-bit registers and addressing typically has 64-bit (8-byte) words and operates on a word rather than a byte at a time.
- storage in bytes versus networks in bits ::@:: Computer storage and most throughput are measured in bytes and collections of bytes, while network measurements use bits per second such as Mb/s or Gb/s, because networks move data a bit at a time.

## binary and decimal prefixes

A size prefix names a multiple of the byte, and there are two families of them. A __decimal__ prefix is a power of $1{,}000$: a kilobyte (kB) is $1{,}000$ bytes, a megabyte (MB) is $1{,}000^2$ bytes, a gigabyte (GB) is $1{,}000^3$ bytes, a terabyte (TB) is $1{,}000^4$ bytes, and a petabyte (PB) is $1{,}000^5$ bytes. A __binary__ prefix is instead a power of $1{,}024$, which is $2^{10}$: a kibibyte (KiB) is $1{,}024$ bytes, a mebibyte (MiB) is $1{,}024^2$ bytes, a gibibyte (GiB) is $1{,}024^3$ bytes, a tebibyte (TiB) is $1{,}024^4$ bytes, and a pebibyte (PiB) is $1{,}024^5$ bytes.

The two families are written apart. The decimal symbols are kB, MB, GB, TB, and PB, and only the kilo prefix is lowercase, because the SI prefix for $1000$ is a lowercase k; the binary symbols are KiB, MiB, GiB, TiB, and PiB, from IEC 60027-2 and ISO/IEC 80000-13, which pair a two-letter prefix with the byte symbol. Capitalizing the kilo symbol, as in KB, is common but is not the recommended decimal symbol, so a bare kB or MB is ambiguous in practice: the decimal and binary values of a prefix differ by about $2$ percent at kilo and by more further up.

Manufacturers often round a decimal symbol off, calling a megabyte 1 million bytes and a gigabyte 1 billion. This course writes kB, MB, and GB and means the $1{,}024$-based quantities by them.

---

Flashcards for this section are as follows:

- decimal prefixes: how many bytes is $1$ kB, and how do the larger ones scale? ::@:: $1{,}000$ bytes is a kilobyte (kB), $1{,}000^2$ bytes is a megabyte (MB), $1{,}000^3$ bytes is a gigabyte (GB), $1{,}000^4$ bytes is a terabyte (TB), and $1{,}000^5$ bytes is a petabyte (PB).
- binary prefixes: how many bytes is $1$ KiB, and how do the larger ones scale? ::@:: $1{,}024 = 2^{10}$ bytes is a kibibyte (KiB), $1{,}024^2$ bytes is a mebibyte (MiB), $1{,}024^3$ bytes is a gibibyte (GiB), $1{,}024^4$ bytes is a tebibyte (TiB), and $1{,}024^5$ bytes is a pebibyte (PiB).
- prefix symbols: kB or KB, and what do KiB, MiB, and GiB mean? ::@:: The decimal symbols are kB, MB, GB, TB, and PB with a lowercase SI prefix k, so KB is common but not the recommended decimal symbol and a bare kB or MB is ambiguous in practice; the binary symbols are KiB, MiB, GiB, TiB, and PiB, from IEC 60027-2 and ISO/IEC 80000-13.
- rounded manufacturer figures ::@:: Manufacturers often round these off: a megabyte is said to be 1 million bytes and a gigabyte 1 billion bytes.
- this course: are its kB, MB, and GB the $1{,}000$-based or the $1{,}024$-based quantities? ::@:: This course writes kB, MB, and GB and means the $1{,}024$-based quantities by them.
