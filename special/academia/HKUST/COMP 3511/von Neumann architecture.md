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

The von Neumann architecture is the stored-program design an operating system has to manage: processing units, a memory holding both instructions and data, and input/output mechanisms, all joined by a common bus. Because one memory holds both code and data, the hardware sees only a stream of addresses, and a program must be in memory before it can run.

---

Flashcards for this section are as follows:

- overview ::@:: The stored-program design, in which a central processing unit, a memory holding both instructions and data, and input/output mechanisms are connected through a common bus.
- stored-program architecture ::@:: Instructions and data must both be stored in memory, so a program has to be brought into memory before it can be executed.
- memory as an address stream ::@:: The processor and its memory management unit see only a stream of memory addresses and do not know how they were generated, nor whether they refer to instructions or to data.
- main components ::@:: A central processing unit with an arithmetic-logic unit and processor registers, a control unit with an instruction register and a program counter, memory holding data and instructions along with caches, external secondary storage, and input/output mechanisms.

## computer system organization

A computer system has one or more CPU cores and several device controllers on a common bus that gives access to shared memory. Each controller manages one device type and has its own local buffer, so CPUs and devices run concurrently and compete for memory cycles on the bus.

The worked example arranges those parts around buses. The processor, its cache, and main memory meet at a bridge/memory controller that joins the PCI bus, and the graphics controller, a SCSI controller, an IDE disk controller, and an expansion bus interface hang off that same PCI bus. Devices attach below their controllers: a monitor under the graphics controller, disks on the SCSI and IDE buses, and a keyboard, parallel port, and serial port on the expansion bus.

---

Flashcards for this section are as follows:

- computer-system operation ::@:: One or more CPU cores and several device controllers are connected through a common bus that provides access to shared memory.
- device controller ::@:: Hardware that manages one type of device and has its own local buffer.
- concurrent execution ::@:: The CPUs and the device controllers execute concurrently and therefore compete for memory cycles through the shared bus.
- a system architecture with I/O ::@:: The processor, its cache, and main memory meet at a bridge/memory controller on the PCI bus, where the graphics controller, a SCSI controller, an IDE disk controller, and an expansion bus interface also sit, with devices attached below their controllers.

## instruction execution cycle

An instruction-execution cycle fetches an instruction from memory or cache into the instruction register, then decodes it. Decoding may fetch operands from memory or cache into data registers. The instruction executes on those operands, and the result may be written back to memory or cache.

---

Flashcards for this section are as follows:

- instruction execution cycle ::@:: The instruction is fetched from memory or cache into the instruction register, decoded, its operands may be fetched into data registers, the instruction is executed on the operands, and the result may be written back to memory or cache.

### processor registers

The CPU contains an arithmetic-logic unit (ALU) and processor registers, namely the program counter (PC), accumulator (AC), memory address register (MAR), and memory data register (MDR); the control unit contains the instruction register (IR) and the program counter. The PC holds the address of the instruction to fetch, the IR the instruction being decoded, and the MAR and MDR the address and data of a memory access. The ALU carries out the operation while the AC holds an operand and receives the result, and the control unit sequences the fetch, decode, fetch-data, execute, and write-back steps.

---

Flashcards for this section are as follows:

- program counter ::@:: The processor register holding the address of the instruction to be fetched; the control unit contains it as well.
- instruction register ::@:: The register that holds the instruction that has been fetched and is being decoded.
- memory address register and memory data register ::@:: The memory address register holds the address used for a memory access, and the memory data register holds the data read from or written to that address.
- arithmetic-logic unit and accumulator ::@:: The arithmetic-logic unit carries out the instruction's arithmetic and logic operations, and the accumulator holds an operand and receives the result.

### interrupts

When a device needs attention its controller raises an interrupt. The CPU saves its state and transfers control to a handler, which services the device and returns. Because the CPU does not wait for the device, computation and input/output overlap.

---

Flashcards for this section are as follows:

- interrupts ::@:: A device controller raises an interrupt when a device needs attention, the CPU saves its state and transfers control to a handler, and later resumes, which lets computation and input/output overlap.

## input and output subsystem

The basic input/output hardware is the buses, the device controllers, and the devices.

---

Flashcards for this section are as follows:

- input/output hardware elements ::@:: Buses, device controllers and the devices themselves.

### device drivers and kernel services

The kernel module controlling a device is a device driver. Drivers hide the differences between controllers, so the system-call interface can handle a few basic categories of hardware. Above them the kernel's input/output subsystem provides I/O scheduling, buffering, caching, spooling, device reservation, and error handling.

---

Flashcards for this section are as follows:

- device driver ::@:: The kernel module that controls a device and hides the differences between device controllers, so the system-call interface can handle a few basic categories of hardware.
- kernel input/output services ::@:: I/O scheduling, buffering, caching, spooling, device reservation and error handling.

### programmed I/O and direct memory access

Moving data between a device and main memory is either done by the CPU itself, in programmed I/O, or offloaded to a direct memory access controller. Programmed I/O is synchronous because the CPU performs the transfer; direct memory access is asynchronous because a DMA controller does instead.

---

Flashcards for this section are as follows:

- programmed I/O ::@:: The CPU itself performs the work of moving data between a device and main memory; the synchronous style of transfer.
- direct memory access ::@:: The work of moving data between a device and main memory is offloaded to a DMA controller; the asynchronous style of transfer.
- synchronous versus asynchronous transfer ::@:: Programmed I/O is synchronous because the CPU performs the transfer, whereas direct memory access is asynchronous because it is offloaded to a DMA controller.
