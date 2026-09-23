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

A loadable kernel module (LKM) extends a running kernel's capabilities without recompiling the entire kernel. The kernel keeps core components — CPU scheduling, memory management — and links in additional services via modules at boot time or during runtime.

---

Flashcards for this section are as follows:

- overview ::@:: Extends a running kernel's capabilities at boot time or during runtime, without recompiling the entire kernel.
- LKM motivation ::@:: Linking services dynamically is preferable to adding features directly to the kernel, which would require recompiling the entire kernel every time a change was made.

## design

The modular approach resembles a layered design: each kernel section has a well-defined, protected interface. But it is more flexible because any module can call any other. It also resembles a microkernel in having a core with loadable extensions, but modules communicate through direct function calls rather than message passing, giving better performance.

For example, the kernel can have CPU scheduling and memory management built in, then add file system support through loadable modules. When a USB device is plugged in and the kernel lacks the driver, it can be loaded dynamically.

---

Flashcards for this section are as follows:

- modular approach versus layered ::@:: Both have well-defined interfaces, but the modular approach is more flexible: any module can call any other module, unlike strict layering where a layer only calls the one below.
- modular approach versus microkernel ::@:: Both have a minimal core with additional services, but modules communicate through direct function calls rather than message passing, giving better performance.
- runtime module loading ::@:: A kernel module such as a device driver can be loaded when a new device is detected (e.g., a USB device plugged in) and removed when no longer needed, without rebooting.

## Linux and LKMs <!-- check: ignore-line[header_style]: Linux is a proper noun, LKM is an acronym -->

Linux uses loadable kernel modules primarily for device drivers and file systems. Modules can be inserted and removed at runtime, letting Linux keep a monolithic architecture for performance while supporting a wide range of hardware without rebuilding the kernel.

---

Flashcards for this section are as follows:

- Linux use of LKMs ::@:: Linux uses LKMs for device drivers and file systems, inserting and removing them at runtime to keep monolithic performance with modular flexibility.
