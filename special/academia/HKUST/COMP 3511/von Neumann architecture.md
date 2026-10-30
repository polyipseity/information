---
aliases:
  - COMP 3511 von Neumann architecture
  - stored-program computer
  - von Neumann architecture
  - von Neumann model
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/von_Neumann_architecture
  - language/in/English
---

# von Neumann architecture

The von Neumann architecture is the stored-program design an operating system manages. Processing units, memory holding instructions and data, and input/output mechanisms meet on a common bus. One memory holds both, so the hardware sees only a stream of addresses. A program must be in memory to run.

---

Flashcards for this section are as follows:

- what the von Neumann architecture is ::@:: A stored-program design: a central processing unit, memory holding instructions and data, and input/output mechanisms share a common bus.
- what a stored-program architecture requires ::@:: Instructions and data both sit in memory, so a program must be loaded to run.
- what the processor sees of memory ::@:: The processor and its memory management unit see only a stream of addresses, without knowing how each was generated or whether it points at an instruction or data.
- parts of a von Neumann machine ::@:: A central processing unit with an arithmetic-logic unit and registers, a control unit with an instruction register and a program counter, memory for data and instructions with caches, external secondary storage, and input/output mechanisms.

## computer system organization

A computer system has one or more central processing unit (CPU) cores and several device controllers on a shared bus that reaches memory. Each controller manages one kind of device and keeps a local buffer. CPUs and devices run at once and compete for memory cycles on the bus.

The processor, its cache, and main memory meet at a bridge/memory controller on the PCI bus; the graphics controller, a SCSI controller, an IDE disk controller, and an expansion bus interface hang off it. Devices attach below their controllers: a monitor under the graphics controller, disks on the SCSI and IDE buses, a keyboard, parallel port, and serial port on the expansion bus.

---

Flashcards for this section are as follows:

- how the parts of a computer system connect ::@:: One or more central processing unit (CPU) cores and several device controllers share a common bus that reaches shared memory.
- device controller ::@:: The hardware that manages one type of device and keeps a local buffer.
- concurrent execution ::@:: Central processing units (CPUs) and device controllers run at once, competing for memory cycles on the shared bus.
- how the parts of a machine with input/output (I/O) connect ::@:: The processor, its cache, and main memory meet at a bridge/memory controller on the PCI bus. The graphics controller, a SCSI controller, an IDE disk controller, and an expansion bus interface sit on that bus. Each device attaches below its controller.

## instruction execution cycle

An instruction-execution cycle fetches an instruction from memory or cache into the instruction register and decodes it. Decoding may fetch operands from memory or cache into data registers. The instruction runs on those operands, and the result may go back to memory or cache.

---

Flashcards for this section are as follows:

- instruction execution cycle ::@:: An instruction is fetched from memory or cache into the instruction register and decoded. Its operands may be fetched into data registers, the instruction runs on them, and the result may be written back to memory or cache.

### processor registers

A CPU carries an arithmetic-logic unit (ALU) and processor registers: program counter (PC), accumulator (AC), memory address register (MAR), and memory data register (MDR). Its control unit holds the instruction register (IR) and the program counter. The PC keeps the address of the instruction to fetch, the IR the instruction being decoded, and the MAR and MDR the address and data of one memory access. The ALU does the operation, the AC holds an operand and takes the result, and the control unit steps through fetch, decode, fetch data, execute, and write-back.

---

Flashcards for this section are as follows:

- program counter ::@:: The processor register holding the address of the instruction to fetch; the control unit holds it too.
- instruction register ::@:: The register holding the fetched instruction while it is decoded.
- memory address register and memory data register ::@:: The MAR holds the address of a memory access, the MDR the data read from or written to it.
- arithmetic-logic unit and accumulator ::@:: The arithmetic-logic unit does an instruction's arithmetic and logic operations, and the accumulator holds an operand and receives the result.

### interrupts

When a device needs attention, its controller raises an interrupt. The CPU saves its state and jumps to a handler, which services the device and returns. The CPU does not wait for the device, so computation and input/output overlap.

---

Flashcards for this section are as follows:

- interrupts ::@:: A device controller raises an interrupt when its device needs attention. The central processing unit (CPU) saves its state, transfers control to a handler that services the device, and later resumes, so computation and input/output overlap.

## input and output subsystem

Input/output hardware is the buses, the device controllers, and the devices themselves.

---

Flashcards for this section are as follows:

- what input/output hardware consists of ::@:: The buses, the device controllers, and the devices themselves.

### device drivers and kernel services

A device driver is the kernel module controlling one device. Drivers hide the differences between controllers, so the system-call interface needs only a few hardware categories. Above the drivers, the kernel's input/output subsystem handles input/output (I/O) scheduling, buffering, caching, spooling, device reservation, and error handling.

Spooling holds output for a device that cannot interleave data, such as a printer. It queues whole jobs on disk and feeds them to the slow device one at a time, so concurrent programs can write without waiting for the printer. A buffer holds bytes in transit; a spool holds jobs until the device is free.

---

Flashcards for this section are as follows:

- device driver ::@:: The kernel module controlling a device. It hides the differences between controllers, so the system-call interface needs only a few hardware categories.
- what the kernel's input/output subsystem provides ::@:: Input/output (I/O) scheduling, buffering, caching, spooling, device reservation, and error handling.
- spooling ::@:: Holding output for a device that cannot interleave data (such as a printer) in a disk queue, feeding it one job at a time so concurrent programs need not wait for the slow device.
- how spooling differs from buffering ::@:: A buffer holds bytes in transit; a spool holds whole jobs in a queue until a non-interleaving device is free.

### programmed I/O and direct memory access

Data moves between a device and main memory through the CPU itself, in programmed I/O, or through a direct memory access (DMA) controller. Programmed I/O is synchronous because the CPU does the transfer; direct memory access is asynchronous because a DMA controller does.

---

Flashcards for this section are as follows:

- programmed input/output (I/O) ::@:: The central processing unit (CPU) itself moves data between a device and main memory; a synchronous style of transfer.
- direct memory access ::@:: A DMA controller moves data between a device and main memory instead of the central processing unit (CPU), the asynchronous style of transfer.
- synchronous versus asynchronous transfer ::@:: Programmed input/output (I/O) is synchronous because the central processing unit (CPU) does the transfer, while direct memory access (DMA) is asynchronous because a controller does.
