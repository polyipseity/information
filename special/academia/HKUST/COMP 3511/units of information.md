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

The bit holds 0 or 1 and is the basic unit of storage; bigger units are collections of bits. A byte is 8 bits and, on most computers, the smallest chunk the hardware can move: there is an instruction for a byte and none for a bit.

A word is an architecture's native unit of data, one or more bytes wide. A machine with 64-bit registers and 64-bit addressing usually has 64-bit (8-byte) words, and its instructions mostly work on a whole word.

Computer storage, and most throughput, is counted in bytes. Networks are the exception: Mb/s and Gb/s are bits per second, because a link carries data a bit at a time.

---

Flashcards for this section are as follows:

- bit: what does it hold, and what is built from it? ::@:: The bit holds 0 or 1, and every larger unit of storage is a collection of bits.
- byte: how many bits is it, and why is it the smallest unit most computers move? ::@:: A byte is 8 bits and, on most computers, the smallest chunk of storage: there is an instruction for a byte and none for a bit. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- word: what does it name in a given architecture? ::@:: The architecture's native unit of data, one or more bytes wide: a machine with 64-bit registers and addressing usually has 64-bit (8-byte) words and works on one at a time. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- storage in bytes versus networks in bits ::@:: Computer storage and most throughput are counted in bytes. Networks are measured in bits per second, such as Mb/s or Gb/s, because a link carries data a bit at a time. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

## binary and decimal prefixes

A size prefix names a multiple of the byte, and two families are in use. A __decimal__ prefix is a power of $1{,}000$: a kilobyte (kB) is $1{,}000$ bytes, a megabyte (MB) $1{,}000^2$, a gigabyte (GB) $1{,}000^3$, a terabyte (TB) $1{,}000^4$, and a petabyte (PB) $1{,}000^5$. A __binary__ prefix is a power of $1{,}024$, which is $2^{10}$: a kibibyte (KiB) is $1{,}024$ bytes, a mebibyte (MiB) $1{,}024^2$, a gibibyte (GiB) $1{,}024^3$, a tebibyte (TiB) $1{,}024^4$, and a pebibyte (PiB) $1{,}024^5$.

The two families have separate symbols: kB, MB, GB, TB, and PB for decimal, and KiB, MiB, GiB, TiB, and PiB for binary. Only the decimal kilo prefix is lowercase, because the SI prefix for $1000$ is a lowercase k. The binary symbols come from IEC 60027-2 and ISO/IEC 80000-13, which pair a two-letter prefix with the byte symbol. KB is common but is not the recommended decimal form. A bare kB or MB is ambiguous: the decimal and binary values of a prefix differ by about $2$ percent at kilo and by more further up.

Manufacturers often round: a megabyte is said to be 1 million bytes and a gigabyte 1 billion. In this course, kB, MB, and GB mean the $1{,}024$-based quantities.

---

Flashcards for this section are as follows:

- decimal prefixes: how many bytes is $1$ kB, and how do the larger ones scale? ::@:: A kilobyte (kB) is $1{,}000$ bytes, a megabyte (MB) $1{,}000^2$, a gigabyte (GB) $1{,}000^3$, a terabyte (TB) $1{,}000^4$, and a petabyte (PB) $1{,}000^5$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- binary prefixes: how many bytes is $1$ KiB, and how do the larger ones scale? ::@:: A kibibyte (KiB) is $1{,}024 = 2^{10}$ bytes, a mebibyte (MiB) $1{,}024^2$, a gibibyte (GiB) $1{,}024^3$, a tebibyte (TiB) $1{,}024^4$, and a pebibyte (PiB) $1{,}024^5$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- prefix symbols: which symbols does each family use? ::@:: The decimal family uses kB, MB, GB, TB, and PB, with only the SI prefix k lowercase; KB is common but is not the recommended form, and a bare kB or MB is ambiguous. The binary family uses KiB, MiB, GiB, TiB, and PiB, from IEC 60027-2 and ISO/IEC 80000-13. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- rounded manufacturer figures: how do manufacturers quote a megabyte and a gigabyte? ::@:: A megabyte is commonly said to be 1 million bytes and a gigabyte 1 billion. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- this course: are its kB, MB, and GB the $1{,}000$-based or the $1{,}024$-based quantities? ::@:: kB, MB, and GB written in this course mean the $1{,}024$-based quantities. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
