---
aliases:
  - COMP 3511 memory hierarchy
  - memory hierarchy
  - storage hierarchy
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/memory_hierarchy
  - language/in/English
---

# memory hierarchy

No single storage technology is fast, large, and cheap at once, so a computer carries several at once and organizes them into a hierarchy. Levels near the CPU are fast but small and expensive per unit; levels further down are slower, larger, and cheaper.

The levels of the hierarchy differ in speed, cost per unit, capacity (size), and volatility. From top to bottom they are registers, cache, main memory, nonvolatile memory, hard-disk drives, optical disk, and magnetic tapes. Registers, cache, and main memory form primary storage; nonvolatile memory and hard-disk drives form secondary storage; optical disk and magnetic tapes form tertiary storage. Primary storage is volatile; everything below the main-memory boundary is non-volatile.

The hierarchy is a trade-off: a level nearer the CPU is smaller and more expensive but much faster, while a level further down holds more data more cheaply and takes longer to reach. Each level holds only a fraction of the level below it, so the same bytes can sit at several levels at once; the copying that exploits this, and the access patterns that make it pay, are covered in [cache (computing)](cache%20(computing).md).

---

Flashcards for this section are as follows:

- overview ::@:: The organization of a computer's storage devices into levels ordered by speed, size, and cost per unit, with the fastest and most expensive storage closest to the CPU.
- organizing criteria ::@:: Storage devices are organized in a hierarchy according to speed, size, and cost per unit or per byte.
- top of the hierarchy ::@:: The levels closest to the CPU are more expensive and smaller, but much faster.
- bottom of the hierarchy ::@:: Moving down the hierarchy, cost per unit decreases while access time and capacity increase.
- volatility as a characteristic ::@:: The levels also differ in volatility, the contrast being non-volatile disk against volatile memory.
- levels of the storage hierarchy ::@:: Registers, cache, main memory, nonvolatile memory, hard-disk drives, optical disk, and magnetic tapes, from closest to the CPU outwards.
- why storage is organized in a hierarchy ::@:: No single storage technology is fast, large, and cheap at once, so a faster, smaller, more expensive level sits close to the CPU and a slower, larger, cheaper level holds the bulk of the data.
- volatility across the levels ::@:: Registers, cache, and main memory are volatile storage, while nonvolatile memory, hard-disk drives, optical disks, and magnetic tapes are non-volatile.
- subset relationship between levels ::@:: A higher level holds only a fraction of the content of the level below it, so the fast level serves the current working set while the slower level retains everything else.

## primary, secondary, and tertiary storage

Registers, cache, and main memory form __primary storage__; nonvolatile memory and hard-disk drives form __secondary storage__; optical disk and magnetic tapes form __tertiary storage__. Primary storage is volatile; everything below the main-memory boundary is non-volatile.

---

Flashcards for this section are as follows:

- primary, secondary, and tertiary storage ::@:: Registers, cache, and main memory are primary storage; nonvolatile memory and hard-disk drives are secondary storage; optical disk and magnetic tapes are tertiary storage.

## main memory

Main memory is the only large storage medium the CPU can access directly, and it holds both programs and data, meaning instructions as well as the data they operate on. It is volatile, typically dynamic random-access memory (DRAM), and it sits between the CPU and every storage level below it: the CPU reaches secondary storage only indirectly.

Load and store are the basic operations on main memory, and they act on specific addresses. Main memory is byte addressable: each address refers to one byte.

That position has a price: main memory loses its contents when power is removed. The first program to run at power-on, the bootstrap program, is therefore held on electrically erasable programmable read-only memory (EEPROM) instead.

---

Flashcards for this section are as follows:

- main memory ::@:: The only large storage medium the CPU can access directly; it holds both programs and data, meaning instructions as well as data.
- main memory technology and volatility ::@:: Main memory is volatile and is typically dynamic random-access memory (DRAM), so it loses its contents when power is removed.
- load and store ::@:: The basic operations on main memory are the load and store instructions, which act on specific memory addresses.
- byte addressable ::@:: Main memory is byte addressable, meaning each address refers to one byte in memory.
- reaching secondary storage ::@:: The CPU accesses secondary storage indirectly, because main memory is the only large storage medium it can access directly.
- bootstrap program and EEPROM ::@:: The first program to run at computer power-on, held on electrically erasable programmable read-only memory (EEPROM).

## secondary storage

Secondary storage extends main memory with large non-volatile capacity that holds data permanently. It is needed because main memory is volatile and holds only what is currently in use. Its two most common devices are hard-disk drives (HDDs) and nonvolatile memory (NVM) devices, and both store programs and data.

Secondary-storage devices fall into two classes by how they store bits. Mechanical storage covers HDDs, optical disks, holographic storage, and magnetic tape. Electrical storage covers flash memory, solid-state disks (SSDs), FRAM, and NRAM, and is usually called NVM. A hard-disk drive is the mechanical case, reached through mechanical access, while a solid-state disk built from flash has no moving parts.

That contrast shapes the design: mechanical storage is generally larger and cheaper per byte, while electrical storage is smaller, more reliable, faster, and more expensive. In the hierarchy, nonvolatile memory sits above hard-disk drives, with optical disk and magnetic tape further below.

---

Flashcards for this section are as follows:

- secondary storage ::@:: The extension of main memory that provides large non-volatile storage capacity, holding data permanently.
- common secondary-storage devices ::@:: Hard-disk drives (HDDs) and nonvolatile memory (NVM) devices such as solid-state disks, providing storage for both programs and data.
- why secondary storage is needed ::@:: Main memory is volatile and cannot hold data permanently, so secondary storage supplies large non-volatile capacity for the programs and data not currently in use.
- mechanical versus electrical storage ::@:: Mechanical storage covers hard-disk drives, optical disks, holographic storage, and magnetic tape, reached through mechanical access; electrical storage covers flash memory, solid-state disks, FRAM, and NRAM, has no moving parts, and is usually called nonvolatile memory (NVM).
- mechanical versus electrical cost and capacity ::@:: Mechanical storage is generally larger and less expensive per byte than electrical storage.
- mechanical versus electrical reliability and speed ::@:: Electrical storage is more costly, smaller, more reliable, and faster than mechanical storage.

## storage characteristics and access times

Each level of storage is managed by a different component and backed by another. The compiler manages registers, hardware manages cache, and the operating system manages main memory, solid-state disk, and magnetic disk. Registers are backed by cache, cache by main memory, main memory by disk, solid-state disk by disk, and magnetic disk by disk or tape. Movement between levels can be explicit or implicit.

Volatility divides the same levels again: registers, cache, and main memory are volatile, and every level below main memory (nonvolatile memory, hard-disk drives, optical disks, and magnetic tapes) is not.

| level | typical size | implementation technology | access time (ns) | bandwidth (MB/s) | managed by | backed by |
| --- | --- | --- | --- | --- | --- | --- |
| registers | under $1\text{ KB}$ | custom memory with multiple ports, CMOS | $0.25$-$0.5$ | $20\,000$-$100\,000$ | compiler | cache |
| cache | under $16\text{ MB}$ | on-chip or off-chip CMOS SRAM | $0.5$-$25$ | $5\,000$-$10\,000$ | hardware | main memory |
| main memory | under $64\text{ GB}$ | CMOS SRAM | $80$-$250$ | $1\,000$-$5\,000$ | operating system | disk |
| solid-state disk | under $1\text{ TB}$ | flash memory | $25\,000$-$50\,000$ | $500$ | operating system | disk |
| magnetic disk | under $10\text{ TB}$ | magnetic disk | $5\,000\,000$ | $20$-$150$ | operating system | disk or tape |

The table shows the range in numbers: access time rises from a fraction of a nanosecond at the top of the hierarchy to milliseconds at the magnetic disk level, while bandwidth falls the other way. The same span appears in the commonly quoted latency figures: an L1 cache reference takes $0.5\text{ ns}$, a branch mispredict $5\text{ ns}$, an L2 cache reference $7\text{ ns}$, a mutex lock or unlock $25\text{ ns}$, a main memory reference $100\text{ ns}$, compressing $1\text{ KB}$ with Zippy $3\,000\text{ ns}$, sending $2\text{ KB}$ over a $1\text{ Gbps}$ network $20\,000\text{ ns}$, reading $1\text{ MB}$ sequentially from memory $250\,000\text{ ns}$, a round trip within the same datacenter $500\,000\text{ ns}$, a disk seek $10\,000\,000\text{ ns}$, reading $1\text{ MB}$ sequentially from disk $20\,000\,000\text{ ns}$, and sending a packet from California to the Netherlands and back $150\,000\,000\text{ ns}$, about $0.15\text{ s}$. The slowest entry on that list takes about $300$ million times longer than the fastest.

---

Flashcards for this section are as follows:

- explicit or implicit movement ::@:: Movement between levels of the storage hierarchy can be explicit or implicit.
- who manages each level ::@:: Registers are managed by the compiler, cache by hardware, and main memory, solid-state disk, and magnetic disk by the operating system.
- what each level is backed by ::@:: Registers are backed by cache, cache by main memory, main memory by disk, solid-state disk by disk, and magnetic disk by disk or tape.
- where the hierarchy becomes non-volatile ::@:: Every level below main memory (nonvolatile memory, hard-disk drives, optical disks, and magnetic tapes) is non-volatile, while registers, cache, and main memory are volatile.
- access times across the levels: with registers at $0.25$-$0.5\text{ ns}$ and cache at $0.5$-$25\text{ ns}$, what do the remaining levels cost? ::@:: Main memory $80$-$250\text{ ns}$, solid-state disk $25\,000$-$50\,000\text{ ns}$, and magnetic disk $5\,000\,000\text{ ns}$.
- reference latency numbers: with an L1 cache reference at $0.5\text{ ns}$ and a main memory reference at $100\text{ ns}$, what do the disk and network figures come to? ::@:: A disk seek takes $10\,000\,000\text{ ns}$ and a packet sent from California to the Netherlands and back takes $150\,000\,000\text{ ns}$, about $0.15\text{ s}$.
