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

## services

An operating system provides an environment for program execution and offers services to programs and users. User-facing services include a __user interface__ (command-line, graphical, or touch-screen), __program execution__ (loading, running, terminating programs), __I/O operations__ (file or device I/O), __file-system manipulation__ (creating, deleting, reading, writing, searching files and directories, managing permissions), __communications__ between processes (shared memory or message passing, locally or over a network), and __error detection__ (the OS must constantly watch for errors in the CPU, memory, I/O devices, or user programs).

System-facing services ensure efficient operation: __resource allocation__ (CPU cycles, memory, file storage, I/O devices among concurrent jobs), __logging__ (tracking which users use how much of which resources), and __protection and security__ (protecting information in multiuser or networked systems: protection controls access to system resources, security requires user authentication and defends against invalid external access).

---

Flashcards for this section are as follows:

- user-facing OS services ::@:: User interface, program execution, I/O operations, file-system manipulation, communications, and error detection.
- system-facing OS services ::@:: Resource allocation, logging, and protection and security.
- file-system manipulation ::@:: Programs need to read, write, create, delete, and search files and directories, and manage permissions.
- communications: shared memory versus message passing ::@:: Processes may communicate via shared memory (direct access to a shared region) or message passing (the OS moves packets between processes, locally or over a network).
- error detection ::@:: The OS must constantly watch for errors in the CPU, memory, I/O devices, or user programs and take appropriate actions.
- protection versus security ::@:: Protection controls access to system resources among concurrent processes; security requires user authentication and defends against invalid external access attempts.
- resource allocation ::@:: When multiple users or jobs run concurrently, the OS allocates CPU cycles, memory, file storage, and I/O devices to each.
- logging ::@:: The OS tracks which users use how much and what kinds of computer resources.

## user interfaces

Most operating systems provide three types of user interface. A __command-line interface__ (CLI), or command interpreter, lets users type commands directly. The CLI is sometimes implemented in the kernel, sometimes by system programs. UNIX and Linux offer multiple shells (C shell, Bourne-Again shell, Korn shell), each fetching a command from the user, interpreting it, and executing it.

A __graphical user interface__ (GUI) uses a desktop metaphor with windows, icons, and mouse interaction. Invented at Xerox PARC in the early 1970s and first widely used in the Apple Macintosh (1984), GUIs now dominate personal computing. Most systems provide both CLI and GUI: Windows has a GUI with a CLI "Command" shell; Mac OS X has the Aqua GUI with UNIX shells underneath; Linux has CLI with optional GUI environments (KDE, GNOME).

__Touchscreen interfaces__ on mobile devices use gestures, virtual keyboards, and voice commands instead of a mouse.

---

Flashcards for this section are as follows:

- CLI ::@:: A command-line interface lets users type commands directly; shells in UNIX/Linux fetch, interpret, and execute them.
- GUI ::@:: A graphical user interface uses a desktop metaphor with windows, icons, and mouse interaction; invented at Xerox PARC, first widely used in the Apple Macintosh (1984).
- touchscreen interface ::@:: Touchscreen devices use gestures, virtual keyboards, and voice commands instead of a mouse.

## system programs

System programs, also called system utilities, provide a convenient environment for program development and execution. Some are simple user interfaces to system calls; others are considerably more complex. The view of the operating system seen by most users is defined by system programs, not the raw system calls.

System programs fall into several categories: __file management__ (create, delete, copy, rename, list files and directories), __status information__ (date, time, memory, disk space, number of users, performance data), __file modification__ (text editors, search and transformation commands), __programming-language support__ (compilers, assemblers, debuggers, interpreters), __program loading and execution__ (loaders, linkage editors, debugging systems), and __communications__ (virtual connections among processes, users, and systems — remote login, file transfer, email, web browsing).

__Background services__ launch at boot time. Some terminate after completing their tasks; others continue until the system halts — known as services, subsystems, or __daemons__ — providing disk checking, process scheduling, and error logging.

__Application programs__ are not part of the operating system: web browsers, word processors, spreadsheets, database systems, and games, launched by command line, mouse click, or touch.

---

Flashcards for this section are as follows:

- system programs ::@:: Programs shipping with the OS to provide a convenient development and execution environment; some wrap system calls, others are complex utilities.
- categories of system programs ::@:: File management, status information, file modification, programming-language support, program loading and execution, and communications.
- daemons ::@:: Background services that launch at boot and run until the system halts, providing disk checking, scheduling, and error logging.
- application programs versus system programs ::@:: Application programs (browsers, editors, games) are not part of the OS; system programs ship with it.

## linkers and loaders

Source code is compiled into __relocatable object files__ designed to be loaded at any physical memory location. A __linker__ combines these object files into a single binary executable, along with libraries if needed. A __loader__ brings the executable from secondary storage into memory for execution. __Relocation__ assigns final addresses to program parts and adjusts code and data to match.

Modern operating systems do not link libraries into executables statically. Instead, __dynamically linked libraries__ (DLLs on Windows, shared objects on Linux) are loaded when needed and shared by all programs using the same version. Object files and executables have standard formats (machine code and symbol tables), so the operating system knows how to load and start them.

---

Flashcards for this section are as follows:

- linker ::@:: Combines relocatable object files into a single binary executable, along with libraries if needed.
- loader ::@:: Brings an executable from secondary storage into memory for execution.
- relocation ::@:: Assigns final addresses to program parts and adjusts code and data to match.
- dynamically linked libraries ::@:: Libraries loaded at runtime and shared by all programs using the same version, rather than statically linked into each executable.
- relocatable object file ::@:: A compiled file designed to be loaded at any physical memory location, before the linker combines it with others into an executable.

## design and implementation

Designing an operating system starts with defining goals and specifications. __User goals__ include convenience, ease of learning and use, reliability, safety, and speed. __System goals__ include ease of design, implementation, and maintenance, along with flexibility, reliability, error-freedom, and efficiency.

An important principle is separating __policy__ from __mechanism__. Mechanisms specify how to do things; policies decide what will be done. A timer is a mechanism for CPU protection; the timer duration is a policy decision. Separating them lets the same mechanism support different policies without modification.

Early operating systems were written in assembly. Most modern kernels use C or C++, with the lowest levels possibly still in assembly. High-level languages make operating systems easier to port, faster to write, more compact, and easier to debug. The only possible disadvantages — reduced speed and increased storage — are not major issues on today's hardware.

---

Flashcards for this section are as follows:

- user goals for an OS ::@:: Convenience, ease of learning and use, reliability, safety, and speed.
- system goals for an OS ::@:: Ease of design, implementation, and maintenance, along with flexibility, reliability, error-freedom, and efficiency.
- policy versus mechanism ::@:: Mechanisms specify how to do things; policies decide what will be done. Separating them allows the same mechanism to support different policies without modification.
- timer as mechanism, duration as policy ::@:: A timer construct is a mechanism for CPU protection; the timer duration for a particular user is a policy decision.
- high-level language implementation ::@:: Most modern kernels use C or C++, making them easier to port, faster to write, more compact, and easier to debug, with negligible performance cost on contemporary hardware.

## structure

Operating systems vary in internal structure. A __simple structure__ (such as MS-DOS) has no well-defined architecture: interfaces and functionality are not separated, and application programs can access I/O directly. MS-DOS was written for the Intel 8088 with no dual mode and no hardware protection. It is single-tasking: the shell is invoked at boot, and running a program loads it into memory, overwriting everything except the kernel. When the program exits, the shell reloads.

__FreeBSD__, a Unix variant, demonstrates multitasking. On login, the shell calls `fork()` to create a new process, then `exec()` to load a program. The shell either waits for the process to terminate or continues accepting user commands. The OS provides CPU scheduling, process coordination, and memory management to support multiprogramming.

A __monolithic kernel__ places all OS functionality into a single binary in one address space. Traditional UNIX follows this structure, with the kernel consisting of everything below the system-call interface and above the physical hardware. UNIX separates into two parts: the kernel and system programs. The kernel contains signal handling, terminal handling, I/O, file systems, CPU scheduling, memory management, and device drivers. Monolithic kernels have a performance advantage from minimal overhead, but are hard to modify because changes in one part affect others. Their speed keeps them in use in UNIX, Linux, and Windows.

The __layered approach__ divides the OS into layers, each built on lower ones. Layer 0 is the hardware; layer _N_ is the user interface. Each layer consists of data structures and functions invokable by higher layers, which in turn invoke lower layers. __Information hiding__ means a layer does not need to know how lower-layer operations are implemented — only what they do. This simplifies building and debugging from the lowest layer up, but adds traversal overhead and makes layer boundaries hard to define. Few OSes use a pure layered approach; the trend is toward fewer layers with more functionality.

A __microkernel__ removes nonessential components from the kernel, implementing them as user-level programs in separate address spaces. It provides only process management, memory management, and IPC. Microkernels are easier to extend, port, and debug, but suffer performance overhead from message passing between address spaces. Windows NT originally used a layered microkernel but performed worse than Windows 95; later versions moved more functions into the kernel.

The __modular approach__ uses loadable kernel modules (LKMs) to extend a running kernel at boot time or during runtime. Core services stay in the kernel; additional functionality — device drivers, file systems — is added dynamically. This resembles layered design in having well-defined interfaces but allows any module to call any other. It resembles microkernels in having a minimal core but avoids message-passing overhead. Linux uses LKMs for device drivers and file systems.

Few operating systems use a single, strictly defined structure. __Hybrid systems__ combine approaches: Linux is monolithic with modular extensions; Windows is largely monolithic but supports separate subsystems (personalities) as user-mode processes and loadable kernel modules.

__Android__ is a layered, open-source mobile OS built on a modified Linux kernel. Its architecture from bottom to top: the Linux kernel (with power management for mobile), a __hardware abstraction layer__ (HAL) that abstracts camera, GPS, and sensors, __Bionic__ (Google's standard C library, replacing glibc), __native libraries__ (SQLite, OpenGL, webkit, SSL, media framework, surface manager), the __Android Runtime__ (ART, a virtual machine optimized for mobile), __Android frameworks__ (APIs for app development), and __applications__. The __Java Native Interface__ (JNI) lets developers bypass the VM to access hardware directly, at the cost of portability.

__macOS and iOS__ share the Darwin kernel environment, which combines the Mach microkernel and the BSD UNIX kernel (the XNU hybrid kernel). macOS adds the Aqua GUI, Cocoa programming environment, and core frameworks (QuickTime, OpenGL). iOS adds the Springboard touch interface, Cocoa Touch, media services, and core services (cloud, databases), running on ARM rather than Intel.

---

Flashcards for this section are as follows:

- simple OS structure ::@:: No well-defined architecture; interfaces and functionality are not separated, as in MS-DOS, which was single-tasking with no dual mode or hardware protection.
- MS-DOS memory model ::@:: At boot, the shell and kernel occupy memory; running a program overwrites everything except the kernel; on exit, the shell reloads.
- FreeBSD multitasking ::@:: The shell calls `fork()` to create a process, `exec()` to load a program; the OS provides CPU scheduling, process coordination, and memory management.
- monolithic kernel ::@:: All OS functionality in a single binary running in one address space; fast due to minimal overhead but hard to modify.
- UNIX kernel and system programs ::@:: UNIX separates into the kernel (everything below the system-call interface) and system programs (shells, compilers, utilities).
- layered approach ::@:: The OS is divided into layers from hardware (layer 0) to user interface (layer N); each layer uses services from below and offers services above.
- information hiding in layered OS ::@:: A layer does not need to know how lower-layer operations are implemented, only what they do — the interface is the contract.
- microkernel ::@:: A minimal kernel providing only process management, memory management, and IPC; other services run as user-level programs, improving extensibility at the cost of message-passing overhead.
- loadable kernel module ::@:: A module that extends a running kernel at boot or runtime without recompilation, combining monolithic performance with modular flexibility.
- hybrid operating system ::@:: Combines multiple structures, such as Linux (monolithic with modular extensions), Windows (monolithic with subsystems and loadable modules), or macOS (Mach microkernel + BSD).
- Android layered architecture ::@:: From bottom: Linux kernel, HAL, Bionic C library, native libraries (SQLite, OpenGL, webkit), ART VM, Android frameworks, applications.
- HAL (Android) ::@:: The hardware abstraction layer in Android, abstracting camera, GPS, and sensors so applications see a consistent interface regardless of specific hardware.
- Bionic ::@:: Google's standard C library for Android, replacing the GNU C library (glibc) used in Linux systems.
- Java Native Interface (JNI) ::@:: Allows Android developers to bypass the ART virtual machine and access hardware directly, at the cost of portability.
- Darwin kernel ::@:: The hybrid XNU kernel in macOS and iOS combining Mach microkernel (memory management, CPU scheduling, IPC) and BSD UNIX kernel (POSIX API, networking, file system, security).
- macOS versus iOS ::@:: Both share Darwin; macOS adds Aqua GUI and Cocoa, iOS adds Springboard touch interface and Cocoa Touch, running on ARM instead of Intel.
- modular versus layered ::@:: Both have well-defined interfaces, but modules can call any other module, unlike strict layering.
- modular versus microkernel ::@:: Both have a minimal core with extensible services, but modules use direct calls rather than message passing.
