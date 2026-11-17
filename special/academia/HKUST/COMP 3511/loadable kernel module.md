---
aliases:
  - LKM
  - kernel module
  - loadable kernel module
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/loadable_kernel_module
  - language/in/English
---

# loadable kernel module

A loadable kernel module (LKM) adds features to a running kernel without recompiling it. Central processing unit (CPU) scheduling and memory management stay in the core; other services arrive as modules at boot or at runtime.

---

Flashcards for this section are as follows:

- what a loadable kernel module does ::@:: It adds features to a running kernel at boot or at runtime, without recompiling it. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- why loadable kernel modules (LKMs) exist ::@:: Linking a service in dynamically beats adding it to the kernel, which means recompiling the whole kernel on every change. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

## design

The modular approach looks like a layered design, each kernel section with a well-defined, protected interface, but any module can call any other. It also resembles a microkernel, a small core with loadable extensions; modules call each other directly, which is faster than passing messages.

CPU scheduling and memory management stay built in; file system support arrives as loadable modules. When a USB device is plugged in and the kernel lacks its driver, the driver is loaded.

---

Flashcards for this section are as follows:

- modular approach versus layered design ::@:: Both give each kernel section a protected, well-defined interface, but any module may call any other; in strict layering a layer calls only the one below. <!--SR:!fsrs,2027-01-23T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-18T00:00:00.000Z!fsrs,2027-01-23T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-18T00:00:00.000Z-->
- modular approach versus microkernel ::@:: Both keep a small core with loadable extensions, but modules call each other by direct function call, which performs better than message passing. <!--SR:!fsrs,2027-01-23T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-18T00:00:00.000Z!fsrs,2027-01-23T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-18T00:00:00.000Z-->
- loading a kernel module at runtime ::@:: A device driver module loads when a new device appears, such as a USB device just plugged in, and unloads when it is no longer needed, without a reboot. <!--SR:!fsrs,2027-01-23T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-18T00:00:00.000Z!fsrs,2027-01-23T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-18T00:00:00.000Z-->

<!-- check: ignore-next-line[header_style]: Linux is a proper noun, LKM is an acronym -->
## Linux and LKMs

Linux loads modules mostly for device drivers and file systems, inserting and removing them at runtime. The kernel stays monolithic and fast, and still covers a wide range of hardware without a rebuild.

---

Flashcards for this section are as follows:

- what Linux uses loadable kernel modules (LKMs) for ::@:: Linux inserts and removes device drivers and file systems as modules at runtime. The kernel stays monolithic and fast across a wide range of hardware. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
