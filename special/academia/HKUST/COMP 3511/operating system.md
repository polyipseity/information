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

An operating system is the system software between a computer's hardware and everything running on it. It controls how applications and users share computing resources and hides the hardware behind a simple interface.

A computer system divides into four parts. _Hardware_ supplies the computing resources: central processing unit (CPU), memory and input/output (I/O) devices. _Application programs_ decide how those resources get used: editors, compilers, web browsers, databases, video games. The _operating system_ controls their use among applications and users. _Users_ may be people, machines, other computers or other devices.

Machine-language structure is hard for programs to use, especially for I/O, so the operating system supplies an abstraction. Programs and users work with photos, web pages, emails and files instead of bytes and blocks on devices. The operating system stands between them and the hardware. Linux, Unix, Microsoft Windows, macOS, iOS and Android all work this way.

---

Flashcards for this section are as follows:

- what an operating system is ::@:: System software controlling how applications and users share computing resources.
- four components of a computer system ::@:: The four components are hardware, the operating system, application programs, and users.
- the operating system as intermediary ::@:: The operating system stands between users or application software and the hardware, and hides the messy details behind a simple interface.
- abstraction over hardware ::@:: Programs and users work with photos, web pages, emails, and files, not bytes and blocks on devices.
- machine-language complexity ::@:: The machine-language structure of a computer is complicated for programs, especially for input/output (I/O), and the operating system hides it behind an abstraction.
- what application programs do ::@:: Application programs define how system resources are used to solve problems: editors, compilers, web browsers, databases, video games.
- who counts as a user ::@:: Users can be people, machines, other computers, or other devices.

## roles and goals

A modern computer holds many resources: processors, memory, timers, disks, mice, network interfaces and printers. The operating system hands them out in an orderly way. As a __resource allocator__ it manages hardware and software and settles conflicting requests so resources get used efficiently and fairly. As a __control program__ it runs other programs and stops errors and improper use of the computer.

Its goals pull in different directions. _User convenience_ means an environment where users or programmers run programs conveniently, safely, protected and efficiently. _Resource allocation_ means sharing resources out fairly and efficiently, whether hardware such as the CPU and main memory or software such as signals and locks. Someone using a machine of their own wants convenience, ease of use and performance; the operator of a shared machine wants its resources used efficiently and its users treated fairly.

---

Flashcards for this section are as follows:

- the operating system as resource allocator ::@:: The operating system as resource allocator manages hardware and software resources and decides between conflicting requests so they are used fairly and efficiently.
- the operating system as control program ::@:: The operating system as control program runs programs and stops errors and improper use of the computer.
- goals of an operating system ::@:: The goals are user convenience, so programmers can run programs safely and easily, and resource allocation in a fair and efficient way.
- user goals versus operator goals ::@:: A user of a private machine wants convenience, ease of use and performance. The operator of a shared machine wants resources used efficiently and fairly.

## composition

### kernel and system programs

No definition of an operating system is universally accepted. A good approximation is "everything a vendor ships when you order one", though what ships varies. One view takes that broad reading; the other names the single program always running on the computer, the __kernel__, which supplies the core functionality.

Beyond the kernel, a shipped operating system carries other software. __Middleware__ is a software framework giving application developers extra services such as databases, multimedia and graphics, common on mobile systems such as Apple's iOS and Google's Android. __System programs__ ship with the operating system but stay outside the kernel: shells, compilers, editors, file utilities. __Application programs__ are no part of it: word processors, browsers and app-store apps are the usual examples.

---

Flashcards for this section are as follows:

- definition of an operating system ::@:: No definition is universally accepted.
- vendor approximation ::@:: "Everything a vendor ships when you order an operating system" is a good approximation, though what ships varies.
- kernel ::@:: The one program always running on a computer, which supplies the core functions.
- middleware ::@:: Middleware is a software framework giving application developers extra services such as databases, multimedia and graphics; it is common on mobile systems such as Apple's iOS and Google's Android.
- what ships beyond the kernel ::@:: A shipped operating system also carries middleware, system programs and application programs. System programs ship outside the kernel, and application programs are no part of the system.

### system programs

System programs, also called system utilities, give a convenient environment for developing and running programs. Some are simple interfaces to system calls, others far more complex. Most users meet the operating system through them, not raw system calls.

System programs come in these categories:

- __file management__ (create, delete, copy, rename, list files and directories).
- __status information__ (date, time, memory, disk space, number of users, performance data).
- __file modification__ (text editors, search and transformation commands).
- __programming-language support__ (compilers, assemblers, debuggers, interpreters).
- __program loading and execution__ (loaders, linkage editors, debugging systems).
- __communications__ (virtual connections among processes, users, and systems: remote login, file transfer, email, web browsing).

__Background services__ start at boot. Some finish and exit; others run until the system halts and are called services, subsystems or __daemons__. They handle disk checking, process scheduling and error logging.

__Application programs__ are no part of the operating system. Browsers, word processors, spreadsheets, databases and games start from a command line, a mouse click or a touch.

---

Flashcards for this section are as follows:

- system programs ::@:: Programs that ship with the operating system and give a convenient environment for developing and running programs. Some wrap system calls; others are complex utilities.
- categories of system programs ::@:: The categories are file management, status information, file modification, programming-language support, program loading and execution, and communications.
- daemons ::@:: Background services that start at boot and run until the system halts, doing disk checking, process scheduling and error logging.
- application programs versus system programs ::@:: Application programs (browsers, word processors, games) are no part of the operating system. System programs ship with it, and editors are system programs.

### linkers and loaders

Source code compiles into __relocatable object files__, built to load at any physical memory address. A __linker__ joins them into one binary executable, adding libraries where needed. A __loader__ brings it from secondary storage into memory to run. __Relocation__ assigns final addresses to program parts and adjusts code and data to match.

Modern operating systems do not link libraries into executables at build time. __Dynamically linked libraries__ (DLLs on Windows, shared objects on Linux) load when needed, and every program using the same version shares one copy. Object files and executables share standard formats for machine code and symbol tables, so the operating system can load and start them.

---

Flashcards for this section are as follows:

- linker ::@:: A linker joins relocatable object files into one binary executable, adding libraries where needed.
- loader ::@:: A loader brings a program from storage into memory so the program can run.
- relocation ::@:: Relocation assigns final addresses to the parts of a program and adjusts code and data to match.
- dynamically linked libraries ::@:: Libraries that load at runtime and are shared by all programs using the same version, instead of being linked in when the program is built.
- relocatable object file ::@:: A compiled file that can sit at any memory address, before the linker joins it with others into one binary.

## modes and protection

The hardware keeps a mode bit saying whose code runs: 1 for user code, 0 for kernel code. Dual-mode operation rests on that bit. It shields the operating system and the hardware from user programs, and user programs from one another.

Some instructions are privileged, so only kernel code may issue them: input/output control, timer management and interrupt management. Writing the mode bit belongs there by definition, since user code that could change it would enter kernel mode at will. Issuing a privileged instruction in user mode is illegal, and the hardware traps to the operating system instead of carrying it out. A trap, or exception, is a software-generated interrupt, raised by an error such as an arithmetic fault or by a request such as a system call.

Two modes are the minimum. Several processors offer more. Intel processors carry four protection rings, ring 0 for the kernel and ring 3 for user code, leaving rings 1 and 2 for operating-system services that rarely use them. ARMv8 has seven modes. A machine that supports virtualization usually adds a mode for the virtual machine manager, which outranks a user process and ranks below the kernel. Moving between guests there costs a [machine switch](virtualization.md#machine%20switch).

---

Flashcards for this section are as follows:

- dual-mode operation ::@:: Keeping user code and kernel code in separate hardware modes, so the operating system and the hardware stay protected from user programs and user programs from one another.
- what the mode bit says ::@:: Whose code runs: 1 for user code, 0 for kernel code.
- privileged instruction ::@:: An instruction only kernel mode may issue, such as input/output control, timer management or interrupt management.
- why writing the mode bit is privileged ::@:: User code that could change it would enter kernel mode at will.
- what happens when user code issues a privileged instruction ::@:: The hardware treats it as illegal and traps to the operating system.
- trap or exception ::@:: A software-generated interrupt, raised by an error such as an arithmetic fault or by a request such as a system call.
- Intel protection rings ::@:: Four rings, ring 0 for the kernel and ring 3 for user code; rings 1 and 2 could hold operating-system services but rarely do.
- ARMv8 privilege modes ::@:: Seven modes, against Intel's four protection rings.
- privilege of the virtual machine manager's own mode ::@:: More than a user process and less than the kernel.

## services

An operating system runs programs and offers services to programs and users. Its user-facing services are:

- __user interface__ (command-line, graphical, or touch-screen).
- __program execution__ (loading, running, terminating programs).
- __I/O operations__ (file or device I/O).
- __file-system manipulation__ (creating, deleting, reading, writing, searching files and directories, managing permissions).
- __communications__ between processes (shared memory or message passing, locally or over a network).
- __error detection__ (the OS must watch constantly for errors in the CPU, memory, I/O devices, or user programs).

System-facing services keep the machine running efficiently:

- __resource allocation__ (CPU cycles, memory, file storage, I/O devices among concurrent jobs).
- __logging__ (tracking which users use how much of which resources).
- __protection and security__ (protecting information in multiuser or networked systems). Protection controls access to system resources. Security requires user authentication and defends against invalid external access.

---

Flashcards for this section are as follows:

- user-facing operating system (OS) services ::@:: The user-facing services are the user interface, program execution, input/output (I/O) operations, file-system manipulation, communications, and error detection.
- system-facing operating system (OS) services ::@:: The system-facing services are resource allocation, logging, and protection and security.
- file-system manipulation ::@:: Programs need to read, write, create, delete, and search files and directories, and manage permissions.
- communications: shared memory versus message passing ::@:: Processes may communicate through shared memory, a region both can read and write directly, or pass messages, where the operating system (OS) moves packets between them, locally or over a network.
- error detection ::@:: The operating system (OS) watches constantly for errors in the processor, memory, input/output (I/O) devices and user programs, and acts on them.
- protection versus security ::@:: Protection controls access to system resources among concurrent processes. Security requires user authentication and defends against outside attacks.
- resource allocation ::@:: When several users or jobs run at once, the operating system shares out processor cycles, memory, file storage and input/output (I/O) devices.
- logging ::@:: The operating system tracks which users use how much and what kinds of computer resources.

### user interfaces

Most operating systems offer three kinds of user interface. A __command-line interface__ (CLI), or command interpreter, lets users type commands directly. The CLI lives either in the kernel or in system programs. UNIX and Linux ship several shells: the C shell, the Bourne-Again shell and the Korn shell. Each fetches a command from the user, interprets it and executes it.

A __graphical user interface__ (GUI) works through a desktop metaphor: windows, icons and a mouse. Xerox PARC invented it in the early 1970s and the Apple Macintosh (1984) brought it to wide use; it now dominates personal computing. Most systems give both. Windows pairs a GUI with the "Command" shell, Mac OS X puts Aqua over UNIX shells, and Linux adds optional GUI environments such as KDE and GNOME to its CLI.

Mobile __touchscreen interfaces__ use gestures, a virtual keyboard and voice commands in place of a mouse.

---

Flashcards for this section are as follows:

- CLI ::@:: A command-line interface lets users type commands directly; UNIX and Linux shells fetch, interpret and execute each command.
- GUI ::@:: A graphical user interface works through a desktop metaphor of windows, icons and a mouse. Xerox PARC invented it in the early 1970s and the Apple Macintosh (1984) brought it to wide use.
- touchscreen interface ::@:: Mobile touchscreen devices use gestures, a virtual keyboard and voice commands in place of a mouse.

## design

### design goals

Design begins by fixing goals and specifications. __User goals__ are convenience, ease of learning and use, reliability, safety and speed. __System goals__ are ease of design, implementation and maintenance, plus flexibility, reliability, freedom from errors and efficiency.

The design also separates __policy__ from __mechanism__. A mechanism says how to do something; a policy decides what gets done. A timer is the mechanism for CPU protection; how long it runs is a policy decision. Separating the two lets one mechanism serve different policies unchanged.

Early operating systems were written in assembly; most modern kernels use C or C++, sometimes with the lowest levels still in assembly. A high-level language makes an operating system easier to port, quicker to write, more compact and easier to debug. It costs some speed and storage, but neither is a major issue on today's hardware.

---

Flashcards for this section are as follows:

- user goals for an operating system (OS) ::@:: The user goals are convenience, ease of learning and use, reliability, safety, and speed.
- system goals for an operating system (OS) ::@:: The system goals are ease of design, implementation, and maintenance, along with flexibility, reliability, error-freedom, and efficiency.
- policy versus mechanism ::@:: A mechanism says how to do something and a policy decides what gets done. Separating the two lets one mechanism serve different policies unchanged.
- timer as mechanism, duration as policy ::@:: A timer is a mechanism for processor protection. The timer duration for a given user is a policy decision.
- high-level language implementation ::@:: Most modern kernels use C or C++, which makes an operating system easier to port, quicker to write, more compact and easier to debug, at almost no cost in speed on today's hardware.

### structure

Operating systems differ in internal structure. A __simple structure__ such as MS-DOS has no well-defined architecture: interfaces and functionality are not separated, and application programs reach I/O directly. MS-DOS was written for the Intel 8088, which had no dual mode and no hardware protection. It runs one task at a time: the shell starts at boot, running a program loads it over everything but the kernel, and on exit the shell reloads.

__FreeBSD__, a Unix variant, does multitask. On login the shell calls `fork()` for a new process, `exec()` to load a program, and then either waits for that process or keeps taking commands. The OS supplies CPU scheduling, process coordination and memory management for multiprogramming.

A __monolithic kernel__ puts all OS functionality in one binary, in one address space. Traditional UNIX follows it: the kernel is everything below the system-call interface and above the hardware. UNIX thus splits into the kernel and system programs. The kernel holds signal handling, terminal handling, I/O, file systems, CPU scheduling, memory management and device drivers. Minimal overhead makes it fast, but a change in one part affects the others, so modification is hard. That speed keeps the design in UNIX, Linux and Windows.

The __layered approach__ cuts the OS into layers, each built on the ones below, from layer 0, the hardware, to layer _N_, the user interface. Each layer holds data structures and functions the layer above can invoke, and invokes the layer below. __Information hiding__ means a layer need not know how lower-layer operations are implemented, only what they do. Building and debugging from the bottom up gets simpler, but every call crosses more layers and the boundaries are hard to draw. Few systems use a pure layered approach; the trend runs to fewer layers carrying more functionality.

A __microkernel__ pulls the nonessential parts out of the kernel and runs them as user-level programs in their own address spaces. Process management, memory management and inter-process communication (IPC) stay. A microkernel is easier to extend, port and debug, but message passing between address spaces costs performance. Windows NT began as a layered microkernel and ran slower than Windows 95; later versions moved functions back into the kernel.

The __modular approach__ extends a running kernel at boot or at runtime with loadable kernel modules (LKMs). Core services stay in the kernel, and extra functionality such as device drivers and file systems is added on demand. As in a layered design, every module has a well-defined interface, but any module may call any other. As in a microkernel, the core stays minimal and there is no message-passing overhead. Linux uses LKMs for device drivers and file systems.

Few operating systems keep to one strict structure; __hybrid systems__ mix them. Linux is monolithic with modular extensions. Windows is largely monolithic, with subsystems (personalities) as user-mode processes and loadable kernel modules.

__Android__ is a layered, open-source mobile OS built on a modified Linux kernel. Its layers, from the bottom up:

- the Linux kernel (with power management for mobile).
- a __hardware abstraction layer__ (HAL) that abstracts the camera, GPS and sensors.
- __Bionic__ (Google's standard C library, replacing glibc).
- __native libraries__ (SQLite, OpenGL, webkit, SSL, media framework, surface manager).
- the __Android Runtime__ (ART), a virtual machine (VM) optimized for mobile.
- __Android frameworks__ (application program interfaces (APIs) for app development).
- __applications__. The __Java Native Interface__ (JNI) lets developers bypass the VM and reach hardware directly, at the cost of portability.

__macOS and iOS__ share the Darwin kernel environment, which pairs the Mach microkernel with the BSD UNIX kernel to form the XNU hybrid kernel. macOS adds the Aqua GUI, the Cocoa programming environment and core frameworks (QuickTime, OpenGL). iOS adds the Springboard touch interface, Cocoa Touch, media services and core services (cloud, databases), and runs on ARM instead of Intel.

---

Flashcards for this section are as follows:

- simple operating system (OS) structure ::@:: The structure has no clear architecture: interfaces and code are mixed, as in MS-DOS, which ran one task at a time with no dual mode or hardware protection.
- MS-DOS memory model ::@:: At boot the shell and kernel occupy memory, running a program overwrites everything but the kernel, and on exit the shell reloads.
- FreeBSD multitasking ::@:: The shell calls `fork()` to create a process and `exec()` to load a program. The operating system supplies processor scheduling, process coordination and memory management.
- monolithic kernel ::@:: A monolithic kernel holds all operating system (OS) code in one binary in one address space. It is fast, with little overhead, and hard to modify.
- UNIX kernel and system programs ::@:: UNIX separates into the kernel (everything below the system-call interface) and system programs (shells, compilers, utilities).
- layered approach ::@:: The operating system is divided into layers, from hardware (layer 0) to the user interface (layer N). Each layer uses the services below it and offers services to the layer above.
- information hiding in layered operating system (OS) ::@:: A layer need not know how lower-layer operations are implemented, only what they do, and the interface is the contract.
- microkernel ::@:: A minimal kernel providing only process management, memory management and inter-process communication (IPC). Other services run as user-level programs, which eases extension and costs message-passing overhead.
- loadable kernel module ::@:: A module that extends a running kernel at boot or runtime without recompilation, which keeps monolithic speed and adds modular flexibility.
- hybrid operating system ::@:: A hybrid system mixes several structures. Linux is monolithic with modular extensions, Windows is monolithic with subsystems and loadable modules, and macOS pairs the Mach microkernel with BSD.
- Android layered architecture ::@:: The layers run from bottom to top: Linux kernel, hardware abstraction layer (HAL), Bionic C library, native libraries (SQLite, OpenGL, webkit), Android Runtime (ART) virtual machine (VM), Android frameworks, applications.
- HAL (Android) ::@:: The hardware abstraction layer in Android, which abstracts the camera, GPS and sensors so applications see a consistent interface whatever the hardware.
- Bionic ::@:: Google's standard C library for Android, replacing the GNU C library (glibc) used in Linux systems.
- Java Native Interface (JNI) ::@:: Android developers can bypass the ART virtual machine and reach hardware directly, at the cost of portability.
- Darwin kernel ::@:: The hybrid XNU kernel in macOS and iOS, which combines the Mach microkernel (memory management, processor scheduling, inter-process communication (IPC)) with the BSD UNIX kernel. That kernel supplies the POSIX application program interface (API), networking, file systems and security.
- macOS versus iOS ::@:: Both share Darwin. macOS adds the Aqua graphical user interface (GUI) and Cocoa, and runs on Intel. iOS adds the Springboard touch interface and Cocoa Touch, on ARM.
- modular versus layered ::@:: A modular and a layered design both have well-defined interfaces, but in a modular one any module can call any other.
- modular versus microkernel ::@:: A modular and a microkernel design both have a minimal core with extensible services, but modules use direct calls instead of message passing.
