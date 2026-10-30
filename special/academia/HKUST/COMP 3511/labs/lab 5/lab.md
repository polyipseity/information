---
aliases:
  - COMP 3511 lab 5
  - HKUST COMP 3511 lab 5
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/labs/lab_5/lab
  - language/in/English
---

# lab

- HKUST COMP 3511 lab 5
- parent: [lab 5](index.md)

## scheduling criteria

A central processing unit (CPU) scheduler picks a process from the ready queue, and the dispatcher hands it the processor. Four quantities measure the cost.

Waiting time is how long a process sits in the ready queue. Turnaround time is completion minus arrival time, which for one CPU burst is waiting time plus burst time. Response time runs from arrival to the end of the first run, the delay an interactive program feels.

Fairness, the fourth, takes no number: every process gets a share of the processor. It conflicts with the other three. A schedule that finishes jobs fast can starve one; one fair to everybody may finish nothing fast.

---

Flashcards for this section are as follows:

- waiting time of a process ::@:: The time a process spends in the ready queue.
- turnaround time of a process ::@:: Its completion time minus its arrival time.
- turnaround time of a process with a single central processing unit (CPU) burst ::@:: Its waiting time plus its burst time.
- response time of a process ::@:: Arrival to the end of the first run; the clock stops when it finishes.
- which scheduling quantity an interactive program notices most ::@:: Response time, so interactive systems use round robin.
- what fairness in scheduling requires, and how it conflicts with performance ::@:: Every process gets a share of the processor, so optimising a measure such as turnaround time takes it from some process.

## switch points

A scheduler decides at two kinds of moment. In a non-preemptive decision the running process blocks or terminates. A [preemptive decision](../../scheduling%20(computing).md#preemptive%20and%20non-preemptive%20scheduling) is taken against it by the timer, a device, or an arriving process.

| from | to | what causes it | decision |
| --- | --- | --- | --- |
| running | waiting | the process requests input or output, or calls `wait()` | non-preemptive |
| running | terminated | the process finishes | non-preemptive |
| running | ready | the timer, when the quantum expires | preemptive |
| waiting | ready | the device, when the request completes | preemptive |
| new | ready | the arrival of a process with higher priority | preemptive |

---

Flashcards for this section are as follows:

- two events that cause a non-preemptive decision ::@:: The running process blocks for input or output, or it terminates.
- what moves a process from running to ready ::@:: The round-robin quantum expires, and the timer preempts it.
- what moves a process from waiting to ready ::@:: Its input or output request completes, and the device makes it runnable again.
- which arriving process can preempt a running process ::@:: A process with higher priority, as in shortest remaining time first or a multilevel feedback queue.

## scheduling algorithms

### first-come, first-served

First-come, first-served (FCFS), or first-in, first-out (FIFO), runs the process that arrived first and never preempts it. It needs no knowledge of burst lengths, is easy to implement, and suits bursts of similar length. Nothing about it is optimal: arrival order fixes the schedule, so the average waiting time is whatever that order produces, and one long burst near the front delays everyone behind it.

Four processes arrive together at time 0.

| process | arrival | burst |
| --- | --- | --- |
| P1 | 0 | 7 |
| P2 | 0 | 4 |
| P3 | 0 | 1 |
| P4 | 0 | 4 |

| start | end | process |
| --- | --- | --- |
| 0 | 7 | P1 |
| 7 | 11 | P2 |
| 11 | 12 | P3 |
| 12 | 16 | P4 |

Waiting times are 0, 7, 11 and 12, an average of $(0 + 7 + 11 + 12)/4 = 7.5$.

---

Flashcards for this section are as follows:

- first-come, first-served (FCFS) scheduling ::@:: The process that arrived first runs first, and nothing preempts it.
- other name of first-come, first-served scheduling ::@:: First-in, first-out (FIFO).
- waiting times of P1 to P4, bursts 7, 4, 1 and 4, arriving at 0, under first-come, first-served ::@:: P1 waits 0, P2 waits 7, P3 waits 11 and P4 waits 12, an average of 7.5.
- why a short process waits long under first-come, first-served ::@:: Nothing preempts the running process, so a short one behind a long one waits out the whole burst.
- why first-come, first-served is still used ::@:: It is easy to implement and suits bursts of similar length.
- burst information first-come, first-served (FCFS) scheduling needs ::@:: None: it runs whichever process arrived first.
- optimality of first-come, first-served (FCFS) scheduling ::@:: None: arrival order fixes the schedule, so the average waiting time is whatever that order produces.

### shortest job first

Shortest job first (SJF) gives each process the length of its next CPU burst and runs the shortest first. The version here is non-preemptive: a process that starts keeps the processor until its burst ends. When every process is already available, it gives the smallest average waiting time of any non-preemptive schedule, since moving a short burst ahead of a long one shortens the short wait more than it lengthens the long one. Once arrivals stagger, a non-preemptive schedule must finish what it started, and the argument fails.

All four arrive at time 0, so P3 runs first, then P2 and P4, which tie, then P1.

| start | end | process |
| --- | --- | --- |
| 0 | 1 | P3 |
| 1 | 5 | P2 |
| 5 | 9 | P4 |
| 9 | 16 | P1 |

Waiting times are 0, 1, 5 and 9 in the order the processes run, an average of $(0 + 1 + 5 + 9)/4 = 3.75$ against 7.5 for first-come, first-served.

---

Flashcards for this section are as follows:

- shortest job first (SJF) scheduling ::@:: Each process carries the length of its next central processing unit (CPU) burst; the shortest runs first.
- what the non-preemptive form of shortest job first does once a process starts ::@:: It keeps the processor until its current burst ends.
- waiting times of bursts 7, 4, 1 and 4 arriving at 0 under shortest job first ::@:: P3 waits 0, P2 waits 1, P4 waits 5 and P1 waits 9, an average of 3.75.
- optimality of shortest job first ::@:: Among non-preemptive schedules it gives the smallest average waiting time, when every process is already available; once arrivals stagger, a preemptive schedule can do better.
- how shortest job first breaks a tie between two processes of equal burst ::@:: By arrival: the process that arrived first runs first.
- what shortest job first needs that a real system cannot supply ::@:: The length of its next central processing unit (CPU) burst, before it runs.

### shortest remaining time first

Shortest remaining time first (SRTF) is the preemptive form of shortest job first. A new arrival with a shorter burst than the running process has left takes the processor. Preemption removes the non-preemptive restriction: when a switch costs nothing, no schedule gives a smaller average waiting time, whatever the arrivals. The four processes keep bursts of 7, 4, 1 and 4 and now arrive at 0, 2, 4 and 5.

| process | arrival | burst |
| --- | --- | --- |
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

| start | end | process | what decides the next block |
| --- | --- | --- | --- |
| 0 | 2 | P1 | P1 alone |
| 2 | 4 | P2 | 4 needed vs P1's 5 left |
| 4 | 5 | P3 | 1 needed vs P2's 2 left |
| 5 | 7 | P2 | P2's 2 left vs P4's 4, P1's 5 |
| 7 | 11 | P4 | P4's 4 left vs P1's 5 |
| 11 | 16 | P1 | P1 is the last process |

Completion times are 5 for P3, 7 for P2, 11 for P4 and 16 for P1, so waiting times are 0, 1, 2 and 9, an average of $(9 + 1 + 0 + 2)/4 = 3$. Under the non-preemptive rule they average $4$, since the first process runs its whole seven units first.

---

Flashcards for this section are as follows:

- shortest remaining time first (SRTF) scheduling ::@:: The preemptive form of shortest job first: an arrival with a shorter burst than the running process has left takes the processor.
- what makes P1 lose the processor at time 2, with bursts 7, 4, 1 and 4 arriving at 0, 2, 4 and 5 ::@:: P2 arrives needing 4 units, fewer than P1's 5 remaining.
- waiting times of bursts 7, 4, 1 and 4 arriving at 0, 2, 4 and 5 under shortest remaining time first ::@:: P1 waits 9, P2 waits 1, P3 waits 0 and P4 waits 2, an average of 3.
- completion time of the burst 7 process arriving at 0, when bursts 4, 1 and 4 arrive at 2, 4 and 5 under shortest remaining time first ::@:: 16, after it is preempted at 2 and resumes at 11.
- average waiting time of the four-process example under shortest remaining time first against the non-preemptive rule ::@:: 3 against 4, because the non-preemptive scheduler runs the first process's whole seven units first.
- optimality of shortest remaining time first (SRTF) scheduling ::@:: No schedule, preemptive or not, gives a smaller average waiting time here, when a preemption costs nothing.

### round robin

Round robin (RR) gives each process one time quantum, usually 10 to 100 milliseconds, and preempts it at the end of that quantum. The preempted process goes to the tail of the ready queue. With $n$ processes queued and a quantum of $q$, no process waits more than $(n - 1)q$ for another turn. No quantum is best: the quantum sets only how soon each process gets a first turn, and context switches pay for a short one.

A small quantum interleaves the processes so they appear to share the processor; one barely larger than a context switch spends more on switching than work.

| quantum | order of blocks | waiting times | average |
| --- | --- | --- | --- |
| 8 | P1, P2, P3, P4 | 0, 7, 11, 12 | 7.5 |
| 4 | P1, P2, P3, P4, P1 | 9, 4, 8, 9 | 7.5 |
| 2 | P1, P2, P3, P4, P1, P2, P4, P1 | 9, 7, 4, 9 | 7.25 |

A quantum of 8 exceeds every burst, so its row gives the first-come, first-served waiting times. At 4, P1 uses one quantum of its seven units, waits out the other three and completes at 16. At 2 the blocks interleave most finely.

| start | end | process |
| --- | --- | --- |
| 0 | 2 | P1 |
| 2 | 4 | P2 |
| 4 | 5 | P3 |
| 5 | 7 | P4 |
| 7 | 9 | P1 |
| 9 | 11 | P2 |
| 11 | 13 | P4 |
| 13 | 16 | P1 |

---

Flashcards for this section are as follows:

- round robin (RR) scheduling ::@:: Each process receives one time quantum, and a process still unfinished when it expires goes to the tail of the ready queue.
- typical time quantum of round robin (RR) scheduling ::@:: 10 to 100 milliseconds.
- bound on how long a process waits for the processor under round robin, with $n$ processes queued and a quantum of $q$ ::@:: At most $(n - 1)q$ time units.
- what a round robin quantum longer than every burst produces ::@:: The first-come, first-served schedule; nothing is ever preempted.
- what a very small round robin quantum costs ::@:: Context switches take a larger share of the time.
- waiting times of bursts 7, 4, 1 and 4 arriving at 0 under round robin with a quantum of 2 ::@:: P1 waits 9, P2 waits 7, P3 waits 4 and P4 waits 9, an average of 7.25.
- optimality of round robin (RR) scheduling ::@:: None: no quantum is best, because the quantum sets only how soon each process gets a first turn, and context switches cost.
- why a quantum of 8 and one of 4 give the same average waiting time in the four-process example ::@:: Both sets of waiting times, 0, 7, 11, 12 and 9, 4, 8, 9, sum to 30.

### priority scheduling

Priority scheduling puts an integer priority on each process and gives the processor to the highest priority, the smallest integer. It may be preemptive, taking the processor when a higher-priority process arrives, or non-preemptive. Processes of equal priority run in arrival order. The shortest-job family is a special case: non-preemptive priority whose number is the inverse of the predicted burst is shortest job first; the preemptive form, whose number is the inverse of what remains, is shortest remaining time first. An arrival then takes the processor when its remaining burst is the shorter. Outside that case the priorities decide the schedule, and the average waiting time follows.

The four processes keep their bursts and arrive together.

| process | priority | burst |
| --- | --- | --- |
| P1 | 4 | 7 |
| P2 | 1 | 4 |
| P3 | 2 | 1 |
| P4 | 3 | 4 |

| start | end | process |
| --- | --- | --- |
| 0 | 4 | P2 |
| 4 | 5 | P3 |
| 5 | 9 | P4 |
| 9 | 16 | P1 |

Waiting times are 9, 0, 4 and 5, an average of $(9 + 0 + 4 + 5)/4 = 4.5$.

A low-priority process can wait forever when the processor keeps going to higher-priority arrivals: that is [starvation](../../scheduling%20(computing).md#priority%20scheduling). Aging raises a waiting process's priority until it outranks its rivals.

---

Flashcards for this section are as follows:

- priority scheduling ::@:: Each process carries an integer priority, and the processor goes to the smallest integer.
- which process a priority scheduler runs first when the numbers differ ::@:: The one with the smallest integer, the highest priority.
- waiting times of bursts 7, 4, 1 and 4 with priorities 4, 1, 2 and 3 arriving at 0 under non-preemptive priority scheduling ::@:: 9, 0, 4 and 5, an average of 4.5.
- how priority scheduling orders two processes of equal priority ::@:: In arrival order, first-come, first-served.
- which scheduling algorithms are special cases of priority scheduling, and how each sets its priorities ::@:: Shortest job first, whose priority is the predicted next central processing unit (CPU) burst, so a short burst outranks a long one; and shortest remaining time first, whose priority is the inverse of what remains, in the preemptive form.
- optimality of priority scheduling ::@:: None of its own: the average waiting time follows from the priorities, and reaches the minimum only in the shortest-job case.
- whether priority scheduling preempts a running process ::@:: Either: the preemptive form takes the processor when a higher-priority process arrives, and the non-preemptive form leaves it running.

## multilevel feedback queue

A multilevel feedback queue (MLFQ) is several ready queues of different priority, and a process moves between them as it runs. Five rules set its behaviour: how many queues there are, which algorithm each runs, when a process is demoted or promoted, and which queue a new process enters. Nothing is guaranteed; another set of rules would suit another mix of jobs.

The arrangement here has three queues. Queue 0 runs round robin with a quantum of 2 milliseconds, queue 1 round robin with 4 milliseconds, and queue 2 first-come, first-served. A new process enters queue 0, and a queue is served only while every queue above it is empty.

A process that uses its whole quantum without finishing drops to the tail of the next queue down. A lower-queue process that a new arrival pushes aside keeps the unused part of its quantum, so it resumes with that much time.

Four processes arrive with these bursts.

| process | arrival | burst |
| --- | --- | --- |
| P1 | 0 | 7 |
| P2 | 1 | 1 |
| P3 | 4 | 1 |
| P4 | 6 | 3 |

| time | what happens | rule that decides it |
| --- | --- | --- |
| 0 | P1 arrives, enters queue 0 and runs | a new process enters the top queue |
| 1 | P2 joins the tail of queue 0; P1 keeps running | an arrival does not preempt a process in the same queue |
| 2 | P1 has used its 2 milliseconds and drops to queue 1; P2 runs | a quantum used up without finishing demotes the process |
| 3 | P2 finishes; P1 resumes in queue 1 | a queue is served only while the queues above it are empty |
| 4 | P3 arrives in queue 0 and preempts P1, which keeps 3 of its 4 milliseconds | an arrival in the top queue preempts a lower queue |
| 5 | P3 finishes; P1 resumes in queue 1 with 3 milliseconds left | a preempted process keeps the quantum it has left |
| 6 | P4 arrives in queue 0 and preempts P1, which has 2 milliseconds left | an arrival in the top queue preempts a lower queue |
| 8 | P4 has used its 2 milliseconds and goes to the tail of queue 1; P1 resumes | a quantum used up without finishing demotes the process |
| 10 | P1 has used its 4 milliseconds in queue 1 and drops to queue 2 | queue 1 gives one quantum of 4 milliseconds |
| 11 | P4 finishes its last millisecond; P1 runs in queue 2 | a queue is served only while the queues above it are empty |
| 12 | P1 finishes | the last process completes |

| start | end | process | queue |
| --- | --- | --- | --- |
| 0 | 2 | P1 | 0 |
| 2 | 3 | P2 | 0 |
| 3 | 4 | P1 | 1 |
| 4 | 5 | P3 | 0 |
| 5 | 6 | P1 | 1 |
| 6 | 8 | P4 | 0 |
| 8 | 10 | P1 | 1 |
| 10 | 11 | P4 | 1 |
| 11 | 12 | P1 | 2 |

Completion times are 12, 3, 5 and 11. Subtracting arrival and burst gives waiting times of 5, 1, 0 and 2, an average of 2.

---

Flashcards for this section are as follows:

- multilevel feedback queue (MLFQ) ::@:: Several ready queues of different priority, between which a process moves as it runs: one that uses little processor time stays high, one that uses a lot sinks.
- rules that define a multilevel feedback queue ::@:: The number of queues, each queue's algorithm, the demotion rule, the promotion rule, and where a new process enters.
- when a lower queue of a multilevel feedback queue (MLFQ) gets the processor ::@:: Only while every queue above it is empty.
- where a new process enters a multilevel feedback queue, and what that arrival preempts ::@:: The top queue; a process already running in a lower queue is preempted.
- whether an arrival preempts a process already running in the same queue of a multilevel feedback queue (MLFQ) ::@:: It does not; the new process joins the tail of that queue and the running one keeps the processor.
- what happens to a process that uses its whole quantum in a multilevel feedback queue ::@:: It drops to the tail of the next queue down.
- what a preempted process in a lower queue does with the rest of its quantum ::@:: It keeps the rest, so it resumes with the time left instead of a fresh quantum.
- waiting times of bursts 7, 1, 1 and 3 arriving at 0, 1, 4 and 6, with queues of 2 and 4 milliseconds and first-come, first-served ::@:: P1 waits 5, P2 waits 1, P3 waits 0 and P4 waits 2, an average of 2.
- why P1, burst 7 arriving at 0, finishes last despite starting first ::@:: Every arrival preempts it, and each finishes inside a quantum, so it resumes repeatedly and completes at 12.
- which process in the four-process example reaches the bottom queue, and why ::@:: P1, the only one whose burst exceeds the 2 and 4 milliseconds the upper queues give.
- optimality of a multilevel feedback queue (MLFQ) ::@:: None guaranteed: the schedule follows from the quanta and the demotion and promotion rules, and other settings suit other workloads.

### program specification

The scheduler to write takes one to four queues, the last first-come, first-served, and at most ten processes. The input table arrives sorted by arrival time, its first process arrives at time 0, and no two processes share an arrival time. The processor is never idle, and the Gantt chart holds at most 300 steps.

The program reads the table on standard input and writes the result on standard output, so redirection runs a test case.

```bash
./mlfq < input.txt > output.txt
```

Blank lines and lines starting with `#` are ignored. The output holds the parsed values, then the final Gantt chart. A run is checked against a sample with `diff`, whose side-by-side form reads more easily.

```bash
diff --side-by-side your-out1.txt sample-out1.txt
```

The `--suppress-common-lines` option hides the lines the two files share, so a correct run prints nothing.

---

Flashcards for this section are as follows:

- number of queues a multilevel feedback queue program has to support, and the algorithm of the last one ::@:: One to four queues, with the last running first-come, first-served.
- most processes one run of the multilevel feedback queue program handles ::@:: Ten.
- assumptions about the arrival times in the input table of the multilevel feedback queue program ::@:: The table is already sorted by arrival time, the first process arrives at time 0, and no two arrive together.
- why the multilevel feedback queue program sorts nothing ::@:: The input table already arrives in arrival order.
- how a test case reaches the multilevel feedback queue program, and where its result goes ::@:: Through standard input and standard output, as in `./mlfq < input.txt > output.txt`.
- two kinds of input line the multilevel feedback queue program ignores ::@:: Blank lines and lines that start with `#`.
- largest number of steps the Gantt chart of the multilevel feedback queue program holds ::@:: 300.
- command that compares a run against a sample output, and the option that hides shared lines ::@:: `diff --side-by-side your-out1.txt sample-out1.txt`, with `--suppress-common-lines` to print only the differences.
- what a preempted process must not lose in the multilevel feedback queue program ::@:: The unused part of its quantum, which it resumes with.
- order of the two parts of the output of the multilevel feedback queue (MLFQ) program ::@:: The parsed values, then the final Gantt chart.
