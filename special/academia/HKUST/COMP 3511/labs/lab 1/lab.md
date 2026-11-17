---
aliases:
  - COMP 3511 lab 1
  - HKUST COMP 3511 lab 1
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/labs/lab_1/lab
  - language/in/English
---

# lab

- HKUST COMP 3511 lab 1
- parent: [lab 1](index.md)

## lab machine and Secure Shell

The laboratory machines run Linux, shared across the department, and none has a graphical desktop, so everything happens as text. Each is named `csl2wkXX.cse.ust.hk`, with `XX` from `01` to `45`, and takes connections from the campus network.

The Secure Shell (SSH) client wants three values: the host name, the port number `22`, and your university user name. The password is the one for your department account.

```bash
ssh <user name>@csl2wk21.cse.ust.hk
```

PuTTY is the usual Windows client and asks for those three values in a dialog; `ssh` in a terminal does the same on macOS and Linux. Files travel over that connection, so a program written on a desktop reaches the lab machine without another tool:

```bash
scp -r lab_demo <user name>@csl2wk21.cse.ust.hk:~/
```

The account's disk quota is small, so large files stay on the desktop.

---

Flashcards for this section are as follows:

- what a Secure Shell (SSH) client needs before it opens a session on a laboratory Linux machine ::@:: the host name, the port number, and the university user name
- port number the Secure Shell (SSH) service on a laboratory Linux machine listens on ::@:: `22`
- host name pattern of a laboratory Linux machine ::@:: `csl2wkXX.cse.ust.hk`, where `XX` runs from `01` to `45`
- Secure Shell (SSH) client used on Windows, and the command that replaces it on macOS or Linux ::@:: PuTTY, and the `ssh` command in a terminal
- command that copies a directory from a desktop into the home directory of a laboratory Linux machine ::@:: `scp -r <directory> <user name>@csl2wk21.cse.ust.hk:~/`

## shell, terminal, and prompt

The terminal takes typed input and shows output; the shell runs inside it. For each command the shell finds and runs the program that carries it out. The laboratory machines use `tcsh`, an enhanced version of the C shell `csh`, while most Linux distributions use `bash`.

Commands are programs, each with its own arguments; some print nothing, others several pages. Tab completes a partly written command or file name, and the arrow keys walk back through earlier ones.

The shell prints a prompt before each command and waits. The prompt is not part of the command; its text is a configuration choice, often the user name, machine name and working directory. One user's `tcsh` settings live in `~/.cshrc_user`.

---

Flashcards for this section are as follows:

- work of the terminal program in a Linux session ::@:: it takes typed input and shows the output
- work of the shell in a Linux session ::@:: it reads each command, finds the program that carries it out, and runs it
- default shell on the laboratory Linux machines, and the shell it extends ::@:: `tcsh`, an enhanced version of the C shell `csh`
- default shell on most Linux distributions ::@:: `bash`, the Bourne Again Shell
- key that completes a partly typed command or file name ::@:: Tab
- what the prompt of a shell session is ::@:: the text printed before each command, often the user name, the machine name and the working directory; never part of the command
- file that holds the shell settings of one `tcsh` user on the laboratory machine ::@:: `~/.cshrc_user`

## file system and working directory

Linux stores every file in one tree, starting at the root directory `/`. Your own files sit in your home directory, `~`, where a new shell starts. The shell tracks the directory you are in at that moment, called the working directory.

A path written from the root, such as `/home`, is absolute and names the same file from anywhere. A path written from the working directory is relative. In a relative path `.` is the working directory itself and `..` is its parent, so `../test.txt` is `test.txt` one level up.

`pwd` prints the absolute path of the working directory. `cd` changes it.

```bash
pwd
cd ..
cd /home
cd ~
```

`cd ..` moves up one level, `cd /home` reaches `/home` from anywhere, and `cd ~` returns to the home directory, as `cd` with no argument does. `cd .` stays put.

---

Flashcards for this section are as follows:

- directory an absolute path starts from ::@:: the root directory `/`, so the path names the same file from anywhere
- meaning of `.` and `..` in a relative path ::@:: `.` is the working directory itself, and `..` is its parent
- directory a new shell session starts in ::@:: the user's home directory, written `~`
- command that prints the absolute path of the working directory ::@:: `pwd`
- command that returns to the home directory from any working directory ::@:: `cd ~`, or `cd` with no argument
- file named by the relative path `../test.txt` ::@:: `test.txt` in the parent of the working directory
- what the working directory of a shell session is ::@:: the directory the shell sits in at that moment, from which relative paths are written

## everyday file commands

### listing and inspecting

`ls` prints the names in the working directory, or in the directory its path argument names, so `ls /home` lists the home directory at the root. Short options change the output: `-l` gives the detailed form with permissions, owner, size and date, `-h` makes sizes readable, and `-a` adds the hidden files, whose names begin with a dot.

Single-letter options stack, so `ls -al` is `ls -a -l`.

```bash
ls
ls -l
ls -lh
ls -a
ls /home
```

---

Flashcards for this section are as follows:

- what the option `-a` adds to the output of `ls` ::@:: the hidden files, whose names begin with a dot
- difference between `ls -l` and `ls -lh` ::@:: `-l` prints the detailed listing; `-lh` adds sizes a person can read
- way to write the short options `-a` and `-l` as one argument ::@:: `-al`, because single-letter options stack
- what `ls /home` lists ::@:: the contents of `/home`, wherever the working directory is
- what the detailed form `ls -l` shows for each entry ::@:: the permissions, the owner, the size, and the date

### creating, copying, moving, removing

`mkdir` creates one or more directories. `touch` creates an empty file, or bumps the last-modified time of an existing one and leaves its contents alone. `cp` copies a file; a directory needs `-r` so the copy descends into it. `mv` renames and moves, since a rename is a move inside one directory. `rm` deletes files, `rmdir` deletes an empty directory, and `rm -r` deletes a directory with everything in it.

```bash
mkdir notes
touch notes/todo
cp notes/todo notes/old-todo
mv notes/old-todo notes/archive-todo
rm notes/archive-todo
rmdir notes
```

`rmdir notes` fails while `notes` holds a file: `rmdir` refuses a directory that would lose data. `rm -r` deletes without asking and cannot be undone. The shell expands `*` before `rm` runs, so `rm * -rf` hits the whole working directory.

---

Flashcards for this section are as follows:

- command that creates a directory, and the command that creates an empty file ::@:: `mkdir <directory>` creates the directory, and `touch <file>` creates the empty file
- option `cp` needs to copy a directory and its contents ::@:: `-r`, which copies recursively
- command that both renames and moves ::@:: `mv <source> <destination>`
- command that removes an empty directory, and the command that removes a directory with files in it ::@:: `rmdir <directory>` for an empty one, and `rm -r <directory>` for a full one
- what `touch` does to a file that already exists ::@:: it updates the last-modified time and leaves the contents alone
- who expands the `*` in `rm * -rf` before `rm` runs ::@:: the shell, which replaces `*` with every name in the working directory

### reading and editing a text file

Three commands print a text file: `cat` writes all at once, while `more` and `less` show one screen at a time. Two editors, `nano` and `vim`, both open the named file and create it when it does not exist.

`vim` starts in command mode, where every key is a command rather than text. `i` enters input mode at the cursor, `a` after the cursor, and `o` on a new line below. `Esc` goes back to command mode. There `:w` writes the file, `:q` quits, and `:wq` does both. `yy` copies a line, `dd` cuts one, and a number in front repeats the command, so `10yy` copies ten lines.

`nano` keeps its commands on screen instead of in modes: `Ctrl+O` writes the file out and `Ctrl+X` leaves the editor.

---

Flashcards for this section are as follows:

- which commands print a text file, and how their output differs ::@:: `cat` writes the whole file at once, while `more` and `less` show one screen at a time
- mode `vim` starts in, and what a key does there ::@:: command mode, where each key is a command rather than text
- key that returns `vim` to command mode from input mode ::@:: `Esc`
- `vim` command that writes the file and quits in one step ::@:: `:wq`
- `vim` keys that cut one line and copy one line ::@:: `dd` cuts a line, and `yy` copies it
- key that leaves the `nano` editor, and the key that writes its file out ::@:: `Ctrl+X` leaves, and `Ctrl+O` writes
- difference between the `vim` keys `i`, `a`, and `o` in command mode ::@:: `i` enters input mode at the cursor, `a` after the cursor, and `o` on a new line below
- effect of the number in front of a `vim` command such as `10yy` ::@:: it repeats the command that many times, so `10yy` copies ten lines

## manual pages

Every command has a manual page, and `man` prints it. `man ls` shows what `ls` is and what each of its options does. The page behaves like a file, so `q` leaves it.

Most commands also accept `--help`, which prints a usage line instead of a page.

```bash
man ls
ls --help
```

---

Flashcards for this section are as follows:

- command that prints the manual page of another command ::@:: `man <command>`, as in `man ls`
- argument that makes a command print a short usage summary instead of its manual page ::@:: `--help`
- key that leaves a manual page opened with `man` ::@:: `q`

## walkthrough in the home directory

One pass runs the whole cycle: make a directory, enter it, write a file, read it back, remove the directory. Run each command below at the prompt, in the home directory.

```bash
mkdir intro
cd intro
vim helloworld
```

In `vim`, `i` enters input mode; type `hello world`, press `Esc`, then `:wq` and Enter to write the file and close the editor.

```bash
cat helloworld
cd ..
rm -r intro
```

`cat` prints `hello world`, `cd ..` returns home, and `rm -r intro` deletes the directory with the file in it.

---

Flashcards for this section are as follows:

- keys that write a new file out of `vim` and leave the editor ::@:: `i` to enter input mode, then `Esc`, then `:wq` and Enter
- command that removes the directory `intro` together with the file inside it ::@:: `rm -r intro`
- command that prints the file `helloworld` ::@:: `cat helloworld`

### compiling and running a first C program

A C program is a text file like any other. `vim main.c` opens a new file; `:wq` leaves the editor once the source is typed.

```c
#include <stdio.h>

int main()
{
    printf("Hello, World!\n");
    return 0;
}
```

The compiler turns the source into an executable, and the shell runs it.

```bash
gcc main.c
./a.out
```

```text
Hello, World!
```

Without an option to name the output, the GNU Compiler Collection (GCC) writes `a.out`; `-o` chooses another name, so `gcc main.c -o main` produces `main`. The `./` in `./a.out` names the working directory, since the shell otherwise searches its path.

---

Flashcards for this section are as follows:

- what the GNU Compiler Collection (GCC) names its output when no output option is given ::@:: `a.out`
- option that names the executable file `gcc` writes ::@:: `-o <name>`, as in `gcc main.c -o main`
- meaning of the `./` in `./a.out` ::@:: the working directory, so `a.out` in it is the file that runs
- two commands that turn `main.c` into a running program, in order ::@:: `gcc main.c`, then `./a.out`
