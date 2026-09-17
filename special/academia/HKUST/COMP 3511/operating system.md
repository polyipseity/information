---
aliases:
  - COMP 3511 operating system
  - OS
  - operating system
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/operating_system
  - language/in/English
---

# operating system

An operating system is the system software between a computer's hardware and everything running on it. It controls and coordinates the use of computing resources among applications and users, and hides the hardware's complications behind a simple interface. This note covers what an operating system does, the roles it plays, and how the kernel differs from the rest of what a vendor ships.

A computer system divides into four components. _Hardware_ provides the basic computing resources: CPU, memory, and I/O devices. _Application programs_ define how those resources are used to solve problems, and include editors, compilers, web browsers, databases, and video games. The _operating system_ controls and coordinates their use among applications and users. _Users_ may be people, machines, other computers, or other devices.

Machine-language structure is hard for programs to use, especially for I/O, so the operating system supplies an abstraction: programs and users work with photos, web pages, emails, and files instead of bytes and blocks on devices. It acts as an intermediary between users or application software and the hardware, as Linux, Unix, Microsoft Windows, macOS, iOS, and Android do.

---

Flashcards for this section are as follows:

- overview ::@:: An operating system (OS) is system software that controls and coordinates the use of computing resources among various applications and users.
- four components of a computer system ::@:: Hardware, the operating system, application programs, and users.
- operating system as intermediary ::@:: The operating system is an intermediary between users or application software and the hardware, hiding its complicated details behind a simple interface.
- abstraction over hardware ::@:: Programs and users work with photos, web pages, emails, and files rather than with bytes and blocks on devices.
- machine-language complexity ::@:: The machine-language structure of a computer is complicated for programs, especially for I/O, which is why the operating system hides it behind an abstraction.
- what application programs do ::@:: Application programs define how system resources are used to solve problems: editors, compilers, web browsers, databases, video games.
- who counts as a user ::@:: Users can be people, machines, other computers, or other devices.

## roles and goals

A modern computer holds many resources: processors, memory, timers, disks, mice, network interfaces, and printers. The operating system allocates them in an orderly and controlled way. As a __resource allocator__ it manages all resources, hardware and software, and decides between conflicting requests so that resources are used efficiently and fairly. As a __control program__ it controls the execution of programs and prevents errors and improper use of the computer.

The purposes of an operating system pull in different directions. _User convenience_ means providing an environment in which users or programmers can run programs conveniently, safely, protected, and efficiently. _Resource allocation_ means allocating resources fairly and efficiently, whether hardware such as the CPU and main memory or software such as signals and locks. Someone using a machine of their own cares about convenience, ease of use, and performance; the operator of a shared machine cares about using its resources efficiently and treating its users fairly.

---

Flashcards for this section are as follows:

- resource allocator ::@:: The operating system manages all resources, hardware and software, and decides between conflicting requests so resources are used efficiently and fairly.
- control program ::@:: The operating system controls the execution of programs and prevents errors and improper use of the computer.
- goals of an operating system ::@:: User convenience, an environment where programmers can run programs conveniently, safely, and efficiently, and resource allocation in a fair and efficient manner.
- user goals versus operator goals ::@:: A user of a private machine wants convenience, ease of use, and performance; the operator of a shared machine wants resources used efficiently and fairly.

## kernel and system programs

There is no universally accepted definition of an operating system. One good approximation is "everything a vendor ships when you order one", but what ships varies. One view takes that broad reading; the other identifies the operating system with the single program always running on the computer, the __kernel__, which provides the essential functionality.

Beyond the kernel, a shipped operating system includes other software. __Middleware__ is software frameworks that provide extra services to application developers, such as databases, multimedia, and graphics; it is popular on mobile systems such as Apple's iOS and Google's Android. __System programs__ ship with the operating system but are not part of the kernel: word processors, browsers, and compilers. __Application programs__ are not associated with the operating system at all; apps from app stores are the usual example.

---

Flashcards for this section are as follows:

- no universal definition ::@:: There is no universally accepted definition of an operating system.
- vendor approximation ::@:: "Everything a vendor ships when you order an operating system" is a good approximation, though what ships varies.
- kernel ::@:: The kernel is the one program always running on a computer, and it provides the essential functionality.
- middleware ::@:: Software frameworks providing extra services to application developers, such as databases, multimedia, and graphics; popular on mobile systems such as Apple's iOS and Google's Android.
- system programs ::@:: Programs that ship with the operating system but are not part of the kernel: word processors, browsers, compilers.
- application programs versus system programs ::@:: Application programs are not associated with the operating system at all, for example apps from app stores, whereas system programs ship with it.
