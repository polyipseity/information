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

No single storage technology is fast, large and cheap at once, so a computer carries several and arranges them in a hierarchy. From the central processing unit (CPU) outwards the levels are registers, cache, main memory, nonvolatile memory, hard-disk drives, optical disk and magnetic tapes. They differ in speed, cost per unit, capacity and volatility. Registers, cache and main memory are volatile; every level below the main-memory boundary is not.

A small, fast, costly level near the CPU serves the current working set; a large, cheap level below holds everything else. Each level keeps only a fraction of the one below it, so the same bytes can sit at several levels at once. [cache (computing)](cache%20(computing).md) covers the copying that exploits this, and the access patterns that pay.

---

Flashcards for this section are as follows:

- what a memory hierarchy is ::@:: It orders a computer's storage devices into levels by speed, size and cost per unit, with the costliest and fastest nearest the central processing unit (CPU).
- what decides where a storage device sits in the hierarchy ::@:: Speed, size and cost per unit or per byte set each device's level in a memory hierarchy.
- what the levels closest to the central processing unit (CPU) are like ::@:: They are smaller and cost more per unit, but reach much faster.
- what the levels furthest from the central processing unit (CPU) are like ::@:: They hold more data at lower cost per unit, but take longer to reach.
- volatility as one of the level characteristics ::@:: Speed, size and cost per unit are not the whole of it: the levels also differ in whether they keep their contents without power.
- what the levels of the storage hierarchy are ::@:: The levels run registers, cache, main memory, nonvolatile memory, hard-disk drives, optical disk and magnetic tapes, from closest to the central processing unit (CPU) outwards.
- why storage is organized in a hierarchy ::@:: No single storage technology is fast, large and cheap at once, so a small fast level sits close to the central processing unit (CPU) and a large cheap one holds the bulk of the data.
- which levels are volatile ::@:: Registers, cache and main memory are volatile; nonvolatile memory, hard-disk drives, optical disks and magnetic tapes are not.
- how the contents of one level relate to the level below it ::@:: A higher level holds only a fraction of the level below it, serving the current working set while the level below keeps everything else.

## primary, secondary, and tertiary storage

Registers, cache and main memory are __primary storage__. Nonvolatile memory and hard-disk drives are __secondary storage__, and optical disk and magnetic tapes are __tertiary storage__. Only primary storage is volatile; everything below the main-memory boundary keeps its contents without power.

---

Flashcards for this section are as follows:

- which levels form primary, secondary and tertiary storage ::@:: Registers, cache and main memory are primary storage; nonvolatile memory and hard-disk drives secondary; optical disk and magnetic tape tertiary.

## main memory

Main memory is the only large storage medium the CPU reaches directly. It holds both programs and the data they work on. It is volatile, usually dynamic random-access memory (DRAM), and sits between the CPU and every level below; secondary storage is reached only through it.

Load and store are the basic operations on main memory, and each names a specific address. One address covers one byte, which makes main memory byte addressable.

Power loss wipes main memory, so the bootstrap program that runs first at power-on sits on electrically erasable programmable read-only memory (EEPROM).

---

Flashcards for this section are as follows:

- what main memory is ::@:: It is the only large storage medium the central processing unit (CPU) reaches directly, holding both programs and the data they work on.
- what technology main memory uses and whether it is volatile ::@:: It is usually dynamic random-access memory (DRAM) and is volatile, so power loss wipes it.
- what the basic operations on main memory are ::@:: They are the load and store instructions, each naming a specific address.
- what byte addressable means ::@:: It means one address covers one byte.
- reaching secondary storage ::@:: The central processing unit (CPU) reaches secondary storage only through main memory, the one large medium it reaches directly.
- what the bootstrap program is and where it is held ::@:: It runs first at power-on and is held on electrically erasable programmable read-only memory (EEPROM).

## secondary storage

Secondary storage adds the large non-volatile capacity that keeps data permanently; main memory is volatile and holds only what is in use. Its two most common devices are hard-disk drives (HDDs) and nonvolatile memory (NVM) devices, both storing programs and data.

Devices split into two classes by how they store bits. Mechanical storage covers HDDs, optical disks, holographic storage and magnetic tape, reached through mechanical access. Electrical storage covers flash memory, solid-state disks (SSDs), ferroelectric RAM (FRAM) and Nano RAM (NRAM), has no moving parts, and usually takes the name NVM.

Mechanical storage is generally larger and cheaper per byte; electrical storage is smaller, more reliable, faster and more expensive. In the hierarchy nonvolatile memory sits above hard-disk drives, and optical disk and magnetic tape further below.

---

Flashcards for this section are as follows:

- what secondary storage is ::@:: It is main memory's non-volatile extension, adding large capacity that keeps data permanently.
- what the common secondary-storage devices are ::@:: Hard-disk drives (HDDs) and nonvolatile memory (NVM) devices such as solid-state disks store both programs and data.
- why secondary storage is needed ::@:: Main memory is volatile and keeps nothing permanently, so secondary storage holds the programs and data not currently in use.
- which devices fall under mechanical and under electrical storage ::@:: Mechanical storage covers hard-disk drives, optical disks, holographic storage and magnetic tape, reached through mechanical access. Electrical storage covers flash memory, solid-state disks, ferroelectric RAM (FRAM) and Nano RAM (NRAM), has no moving parts, and usually goes by nonvolatile memory (NVM).
- mechanical versus electrical cost and capacity ::@:: Mechanical storage is generally larger and cheaper per byte than electrical storage.
- mechanical versus electrical reliability and speed ::@:: Electrical storage is smaller, more reliable, faster and more expensive than mechanical storage.

## storage characteristics and access times

The compiler manages registers, hardware manages cache, and the operating system manages main memory, solid-state disk and magnetic disk. Registers are backed by cache, cache by main memory, main memory by disk, solid-state disk by disk, and magnetic disk by disk or tape. Data moves between levels explicitly or implicitly.

Registers, cache and main memory are volatile; nonvolatile memory, hard-disk drives, optical disks and magnetic tapes are not.

| level | typical size | implementation technology | access time (ns) | bandwidth (MB/s) | managed by | backed by |
| --- | --- | --- | --- | --- | --- | --- |
| registers | under $1\text{ KB}$ | custom memory with multiple ports, CMOS | $0.25$-$0.5$ | $20\,000$-$100\,000$ | compiler | cache |
| cache | under $16\text{ MB}$ | on-chip or off-chip CMOS SRAM | $0.5$-$25$ | $5\,000$-$10\,000$ | hardware | main memory |
| main memory | under $64\text{ GB}$ | CMOS SRAM | $80$-$250$ | $1\,000$-$5\,000$ | operating system | disk |
| solid-state disk | under $1\text{ TB}$ | flash memory | $25\,000$-$50\,000$ | $500$ | operating system | disk |
| magnetic disk | under $10\text{ TB}$ | magnetic disk | $5\,000\,000$ | $20$-$150$ | operating system | disk or tape |

Access time climbs from a fraction of a nanosecond at the top to milliseconds at magnetic disk, while bandwidth falls the other way. The same span shows up in the commonly quoted latency figures:

- an L1 cache reference takes $0.5\text{ ns}$
- a branch mispredict $5\text{ ns}$
- an L2 cache reference $7\text{ ns}$
- a mutex lock or unlock $25\text{ ns}$
- a main memory reference $100\text{ ns}$
- compressing $1\text{ KB}$ with Zippy $3\,000\text{ ns}$
- sending $2\text{ KB}$ over a $1\text{ Gbps}$ network $20\,000\text{ ns}$
- reading $1\text{ MB}$ sequentially from memory $250\,000\text{ ns}$
- a round trip within the same datacenter $500\,000\text{ ns}$
- a disk seek $10\,000\,000\text{ ns}$
- reading $1\text{ MB}$ sequentially from disk $20\,000\,000\text{ ns}$
- sending a packet from California to the Netherlands and back $150\,000\,000\text{ ns}$, about $0.15\text{ s}$

The slowest entry takes about $300$ million times longer than the fastest.

---

Flashcards for this section are as follows:

- how movement between levels happens ::@:: Movement of data between levels of the storage hierarchy can be explicit or implicit.
- which component manages each level ::@:: Registers are managed by the compiler, cache by hardware, and main memory, solid-state disk and magnetic disk by the operating system.
- what each level is backed by ::@:: Registers are backed by cache, cache by main memory, main memory by disk, solid-state disk by disk, and magnetic disk by disk or tape.
- where the hierarchy becomes non-volatile ::@:: Every level below main memory, covering nonvolatile memory, hard-disk drives, optical disks and magnetic tapes, keeps its contents without power.
- access times across the levels: with registers at $0.25$-$0.5\text{ ns}$ and cache at $0.5$-$25\text{ ns}$, what do the remaining levels cost? ::@:: Main memory $80$-$250\text{ ns}$, solid-state disk $25\,000$-$50\,000\text{ ns}$, and magnetic disk $5\,000\,000\text{ ns}$.
- reference latency numbers: with an L1 cache reference at $0.5\text{ ns}$ and a main memory reference at $100\text{ ns}$, what do the disk and network figures come to? ::@:: A disk seek takes $10\,000\,000\text{ ns}$ and a packet sent from California to the Netherlands and back takes $150\,000\,000\text{ ns}$, about $0.15\text{ s}$.
