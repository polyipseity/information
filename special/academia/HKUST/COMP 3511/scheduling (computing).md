---
aliases:
  - CPU scheduling
  - Scheduling (computing)
  - process scheduling
  - scheduler
  - scheduling
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/scheduling_(computing)
  - language/in/English
---

# scheduling (computing)

A processor runs one instruction stream at a time. A loaded system holds more ready work than processors, so central processing unit (CPU) scheduling picks which ready process runs next, and that choice divides processor time among the waiting work.

Multiprogramming keeps some process running at all times, which maximizes CPU utilization. When the processor goes idle, the operating system (OS) takes a process from the [ready queue](process%20(computing).md#ready%20queue%20and%20device%20queues) and hands it the processor. The CPU scheduler, also called the process scheduler or the short-term scheduler, chooses it.

A policy may use only what it knows: arrival order, next burst length, priority, or queue membership. The criteria that judge the choice disagree, so no policy is best in general.

---

Flashcards for this section are as follows:

- what CPU scheduling decides ::@:: Central processing unit (CPU) scheduling picks which ready process runs next, and so divides processor time among the waiting work.
- why multiprogramming needs a scheduler ::@:: Multiprogramming keeps some process running at all times to maximize central processing unit (CPU) utilization, so when the CPU goes idle something must choose the next ready process.
- names for the component that picks a ready process ::@:: The central processing unit (CPU) scheduler, also called the process scheduler or the short-term scheduler.
- what a scheduling policy decides from ::@:: Only what it is allowed to know: arrival order, next burst length, priority, or queue membership. The criteria that judge the choice disagree, so no single policy is best in general.

## scheduling basics

<!-- check: ignore-next-line[header_style]: CPU and I/O are acronyms -->
### CPU and I/O bursts

A process alternates between a CPU burst, a stretch of execution on the processor, and an input/output (I/O) burst, a stretch of waiting for a device request to finish.

Measured burst lengths have a long tail: many short bursts and a few very long ones. A CPU-bound program, one that computes most of the time, produces a few long bursts. An I/O-bound program waits on devices most of the time and produces many short bursts.

The shape decides which policy pays off. One tuned for many short bursts behaves badly when a few long bursts set the pace.

---

Flashcards for this section are as follows:

- what a CPU burst and an I/O burst are ::@:: A central processing unit (CPU) burst is a stretch of execution on the processor. An input/output (I/O) burst waits for a device request to finish, and a process alternates between the two.
- what measured CPU burst lengths look like ::@:: Many short bursts and a few very long ones, a distribution with a long tail. The frequency curve keeps that shape wherever burst lengths are measured.
- CPU-bound process burst pattern ::@:: A few long central processing unit (CPU) bursts, because the process computes rather than waits.
- I/O-bound process burst pattern ::@:: Many short central processing unit (CPU) bursts, because the process spends most of its time waiting for input/output (I/O).
- why burst distribution shapes policy choice ::@:: A policy tuned for many short bursts behaves badly when a few long bursts set the pace.

### scheduling criteria

CPU utilization is the fraction of time the processor is busy. Throughput counts the processes finished per unit time; short processes raise it.

Turnaround time runs from arrival to completion, so it is completion time minus arrival time. Waiting time is the span spent on the ready queue, and with a single CPU burst it equals turnaround time minus burst time. Response time runs from arrival to the first response, which under a scheduling algorithm comes at the end of the first run, not at its start. A process that waits until time 10 and then runs for 3 has a response time of 13, because nothing comes out of it until the run ends.

Turnaround and response time separate only when a process runs more than once. A job that finishes in one burst has the same turnaround and response time, since its first run is also its last. Every further run pushes the completion out while the response stays where the first run ended.

Fairness asks that each job gets an adequate share of the processor. It pulls against performance: a policy that minimizes average turnaround can still leave one job waiting far longer than another.

---

Flashcards for this section are as follows:

- CPU utilization as a criterion ::@:: The fraction of time that the central processing unit (CPU) is busy.
- throughput as a criterion ::@:: The number of processes completed per unit time. It favours short processes.
- turnaround time with a single CPU burst ::@:: Completion time minus arrival time in the ready queue. It equals waiting time plus the central processing unit (CPU) burst time.
- waiting time from turnaround time ::@:: The time a process spends on the ready queue. With one central processing unit (CPU) burst it is turnaround time minus burst time.
- response time ::@:: The time from arrival to the first response, which under a scheduling algorithm is the end of the process's first run rather than when that run starts.
- response time of a process that waits until time $10$ and then runs for $3$ ::@:: $13$, not $10$. The clock runs until the first run ends, because only then does the process respond.
- when turnaround and response time differ ::@:: Only when a process runs more than once. A single burst ends both at the same moment, and each further run lengthens turnaround while response stays fixed.
- fairness against performance ::@:: Fairness gives each job an adequate share of the central processing unit (CPU). Optimizing performance can leave one job waiting far longer than another, so the two measures disagree.
- a process arrives at time $3$, waits, and completes its only burst of $9$ time units at time $17$: turnaround time and waiting time? ::@:: Turnaround time is $17 - 3 = 14$ time units. Waiting time is $14 - 9 = 5$ time units.

### dispatcher and dispatch latency

The scheduler chooses a process, and the dispatcher hands it the processor. Dispatch performs a [context switch](process%20(computing).md#context%20switch) from the running process to the chosen one, switches to user mode, and jumps to the point in the chosen program where execution resumes.

Dispatch latency is the time the dispatcher takes to stop one process and start another. No useful work happens during it, so it is overhead. Linux reports context switches with vmstat; a busy machine shows hundreds per second.

---

Flashcards for this section are as follows:

- what the dispatcher does ::@:: Hands the processor to the process the scheduler chose. It switches context, switches to user mode, and jumps to the right place in the chosen program.
- dispatch latency ::@:: The time the dispatcher takes to stop one process and start another. It is overhead, because no useful work happens during it.
- where to count context switches on Linux ::@:: vmstat reports them, and a busy machine shows hundreds of context switches per second.

### preemptive and non-preemptive scheduling

Scheduling can be invoked in four situations. A running process switches to waiting, on an input/output (I/O) request or a wait call. A running process terminates. A running process switches to ready, on an interrupt. A waiting process switches to ready, when its I/O finishes or when a new process with higher priority arrives.

The first two are non-preemptive: the process gives up the processor by itself, when its burst ends. The last two are preemptive, because the processor is taken from a process that did not ask to leave it.

Preemption brings problems a cooperative policy never meets. A process can lose the processor while it updates shared data, while it is inside the kernel, or while the kernel runs something that must not be interrupted.

A preempted process keeps every resource it holds. [No preemption](deadlock%20(computer%20science).md#no%20preemption) is therefore a separate condition in deadlock prevention, one about resources, not about central processing unit (CPU) time.

---

Flashcards for this section are as follows:

- four occasions that invoke CPU scheduling ::@:: Running to waiting, for an input/output (I/O) request. Termination. Running to ready, for an interrupt. Waiting to ready, when input/output completes or a higher-priority process arrives.
- non-preemptive scheduling ::@:: The running process gives up the central processing unit (CPU) by itself, on an input/output (I/O) request or on termination. The scheduler never takes the processor away.
- preemptive scheduling ::@:: The central processing unit (CPU) is taken from a running process without its cooperation, when it moves to ready or a higher-priority process arrives.
- what preemption complicates ::@:: A process may be stopped while updating shared data, while inside the kernel, or while the kernel is in the middle of an activity that must not be interrupted.

### long-term, medium-term and short-term schedulers

Three schedulers work on three timescales. The short-term scheduler, also the CPU scheduler, picks among the processes already ready and runs on nearly every switch, so it fires every few milliseconds and must be fast. The long-term scheduler, or job scheduler, decides which jobs enter memory, which fixes the [degree of multiprogramming](process%20(computing).md#ready%20queue%20and%20device%20queues); it runs every few seconds or minutes and may take its time. A mainframe uses it to keep a mix of I/O-bound and CPU-bound work. The medium-term scheduler takes a process out of memory and brings it back later, which is swapping to disk, so the ready set shrinks without new work being admitted.

---

Flashcards for this section are as follows:

- short-term scheduler ::@:: The central processing unit (CPU) scheduler, which picks among processes already in the ready queue.
- long-term scheduler ::@:: The long-term scheduler decides which jobs are admitted to the system, so it fixes how many processes compete for the processor.
- medium-term scheduler ::@:: The medium-term scheduler moves a process out of memory and later back in, which changes how many processes are ready without admitting new work.
- other name for the long-term scheduler ::@:: The job scheduler.
- how often the short-term scheduler runs, against the long-term one ::@:: The short-term scheduler runs every few milliseconds and must be fast, while the long-term scheduler runs every few seconds or minutes and may be slow.
- what the medium-term scheduler does to memory ::@:: It swaps a process out to disk and later brings it back, so the count in memory falls without new work admitted.
- what the long-term scheduler looks for on a mainframe ::@:: A good process mix of input/output (I/O)-bound and central processing unit (CPU)-bound jobs.
- which scheduler runs most often ::@:: The short-term scheduler, on nearly every switch between processes.

## scheduling algorithms

### first-come, first-served scheduling

First-come, first-served (FCFS) scheduling serves processes in arrival order and never preempts, so a process keeps the processor until its current CPU burst ends. It is also called first-in, first-out (FIFO).

Arrival order alone decides the average waiting time. With bursts of 24, 3 and 3, all arriving at time 0, serving them in that order gives waiting times 0, 24 and 27, so $(0 + 24 + 27)/3 = 17$, and turnarounds 24, 27 and 30, so $(24 + 27 + 30)/3 = 27$. Serving the two short ones first gives waiting times 0, 3 and 6, so $(0 + 3 + 6)/3 = 3$, and turnarounds 3, 6 and 30, so $(3 + 6 + 30)/3 = 13$.

A short process stuck behind a long one suffers the convoy effect. That is what makes FCFS poor for short jobs and interactive use. A mix of one CPU-bound process and many I/O-bound processes fares badly too: the CPU-bound process holds the processor while the others queue behind it, so the devices sit idle.

---

Flashcards for this section are as follows:

- first-come, first-served rule ::@:: Processes run in arrival order and are never preempted. A process keeps the processor until its current central processing unit (CPU) burst ends.
- another name for first-come, first-served ::@:: First-in, first-out (FIFO), because the queue is served in the order processes joined it.
- first-come, first-served with bursts $24$, $3$ and $3$, all arriving at time $0$, served as $P_1, P_2, P_3$: average waiting time and average turnaround time? ::@:: Waiting times $0$, $24$ and $27$, average $(0 + 24 + 27)/3 = 17$. Completions at $24$, $27$ and $30$, so turnarounds average $(24 + 27 + 30)/3 = 27$.
- first-come, first-served with bursts $24$, $3$ and $3$, all arriving at time $0$, served as $P_2, P_3, P_1$: average waiting time and average turnaround time? ::@:: Waiting times $0$, $3$ and $6$, average $(0 + 3 + 6)/3 = 3$. Completions at $3$, $6$ and $30$, so turnarounds average $(3 + 6 + 30)/3 = 13$.
- convoy effect ::@:: A short process stuck behind a long one, waiting for the long burst to end. It makes first-come, first-served bad for short jobs and for interactive use.
- first-come, first-served with one CPU-bound process and many I/O-bound processes ::@:: The central processing unit (CPU)-bound process holds the processor while the input/output (I/O)-bound ones queue behind it, so the devices stay idle and device utilization falls.
- why first-come, first-served is poor for interactive use ::@:: First-come, first-served never preempts, so a process holds the processor until its burst ends. An interactive job cannot count on a share at regular intervals.

### shortest job first scheduling

Shortest job first (SJF) scheduling associates each process with the length of its next CPU burst and runs the shortest one next. It is non-preemptive, and it is optimal when every process is already available: no other non-preemptive schedule gives a smaller average waiting time. Staggered arrivals break that guarantee, because a non-preemptive schedule must finish whatever it has started. The name is loose: the quantity compared is the next burst, not the whole job.

Moving a short process ahead of a long one shortens the short process's wait by more than it lengthens the long one's wait, because the long process then waits behind a burst smaller than its own. The average falls.

The next burst length is unknown when the decision is made. Processes $P_1$ to $P_4$, with bursts 6, 8, 7 and 3 and arrivals 0, 2, 4 and 5, run as $P_1$, then $P_4$, then $P_3$, then $P_2$, for an average wait of 5. When every process has the same burst length, SJF gives what FCFS gives.

---

Flashcards for this section are as follows:

- shortest job first rule ::@:: Each process is associated with the length of its next central processing unit (CPU) burst, and the shortest runs next. It does not preempt.
- why shortest job first is optimal ::@:: Shortest job first yields the smallest average waiting time of any non-preemptive schedule when every process is already available; once arrivals stagger, a preemptive schedule can do better.
- argument for shortest job first optimality ::@:: Moving a short process ahead of a long one shortens the short one's wait by more than it lengthens the long one's wait, so the average falls.
- main weakness of shortest job first ::@:: The length of the next central processing unit (CPU) burst is unknown when the decision is made, so it must be predicted.
- shortest job first with $P_1$ arriving at $0$ needing $6$, $P_2$ at $2$ needing $8$, $P_3$ at $4$ needing $7$, $P_4$ at $5$ needing $3$: the run order and the average waiting time? ::@:: $P_1$ runs $0$ to $6$, $P_4$ runs $6$ to $9$, $P_3$ runs $9$ to $16$, $P_2$ runs $16$ to $24$. Waiting times are $0$, $14$, $5$ and $1$, so $(0 + 14 + 5 + 1)/4 = 5$.
- when shortest job first matches first-come, first-served ::@:: When every process has the same central processing unit (CPU) burst length, since no ordering can then improve the average.

### shortest remaining time first scheduling

Shortest remaining time first (SRTF) is preemptive SJF. When a process arrives, its burst is compared with the remaining time of the running process, and a shorter one takes the processor. The scheduler runs on an arrival as well as on a completion.

SRTF is optimal outright: no schedule, preemptive or not, gives a smaller average waiting time on the same arrivals, as long as a preemption costs nothing. It needs the same burst prediction, and it is harsher on long jobs: a steady supply of short arrivals can hold a long process off indefinitely.

Four processes of burst 8, 4, 9 and 5, arriving at 0, 1, 2 and 3, run as $P_1$ for one time unit, then $P_2$ to 5, then $P_4$ to 10, then $P_1$ to 17, then $P_3$ to 26. Waiting times are 9, 0, 15 and 2, so $(9 + 0 + 15 + 2)/4 = 6.5$.

---

Flashcards for this section are as follows:

- shortest remaining time first rule ::@:: Shortest remaining time first is preemptive shortest job first: a new arrival whose burst is shorter than the remaining time of the running process takes the central processing unit (CPU).
- shortest remaining time first against shortest job first ::@:: Shortest remaining time first is never worse on average waiting time, and it is optimal: no schedule, preemptive or not, beats it when a preemption costs nothing.
- starvation under shortest remaining time first ::@:: A steady supply of short arrivals can hold a long process off indefinitely, since it never becomes the shortest remaining burst.
- shortest remaining time first with $P_1$ arriving at $0$ needing $8$, $P_2$ at $1$ needing $4$, $P_3$ at $2$ needing $9$, $P_4$ at $3$ needing $5$: the average waiting time? ::@:: $P_1$ runs $0$ to $1$, $P_2$ $1$ to $5$, $P_4$ $5$ to $10$, $P_1$ $10$ to $17$, $P_3$ $17$ to $26$. Waiting times are $9$, $0$, $15$ and $2$, so $(9 + 0 + 15 + 2)/4 = 6.5$.

### round-robin scheduling

Round-robin (RR) scheduling adds preemption to FCFS. Each process receives at most a time quantum $q$ of the processor, usually 10 to 100 milliseconds, and a process whose quantum expires goes to the end of the ready queue, exactly as in FCFS. A process that finishes its burst early releases the processor at once. With $n$ ready processes each gets $1/n$ of the processor in chunks of at most $q$ time units, and none waits more than $(n-1)q$ time units.

A quantum larger than every burst turns RR into FCFS. A small one interleaves the processes until the schedule resembles processor sharing, where each of $n$ processes looks like it owns a processor running at $1/n$ speed. The quantum must also stay large against the context switch time, or the switches eat the time they divide. A rule of thumb puts 80 percent of CPU bursts below the quantum, because average turnaround improves when most processes finish inside one quantum.

Bursts of 24, 3 and 3, all arriving at 0, with a quantum of 4, run $P_1$ to 4, $P_2$ to 7, $P_3$ to 10, then $P_1$ in further slices of 4 until it ends at 30. Waiting times are 6, 4 and 7, so $(6 + 4 + 7)/3 = 5.67$, and turnarounds 30, 7 and 10, so $(30 + 7 + 10)/3 = 15.67$. The first runs end at 4, 7 and 10, so the response times are 4, 7 and 10 and average $(4 + 7 + 10)/3 = 7$. Counting a response from the start of the first run would give 0, 4 and 7 instead.

RR is not always better than FCFS. Ten jobs that all arrive at 0 and each need 100 time units under a quantum of 1 finish in the last round, so their completions run 991 to 1000 and average $(991 + \cdots + 1000)/10 = 995.5$. Running each to completion in turn completes them at 100, 200, …, 1000, which averages $(100 + \cdots + 1000)/10 = 550$. Response moves the opposite way, from 550 to 5.5, because every first run ends inside the first ten time units. Turnaround and response therefore disagree about the same change. The workload decides which matters: interactive work needs the quick first response, an equal-length batch needs the smaller turnaround.

---

Flashcards for this section are as follows:

- round-robin rule with a quantum $q$ for each process ::@:: Each process gets at most one time quantum $q$ of the central processing unit (CPU), usually 10 to 100 milliseconds. A process whose quantum expires goes to the end of the ready queue, exactly as in first-come, first-served.
- longest wait under round-robin with $n$ ready processes and a quantum $q$ ::@:: No process waits more than $(n-1)q$ time units.
- round-robin with a quantum $q$ larger than every burst ::@:: Round-robin then becomes first-come, first-served.
- round-robin with a quantum $q$ small against every burst, among $n$ ready processes ::@:: The processes interleave until the schedule resembles processor sharing, where each of the $n$ processes looks like it owns a processor running at $1/n$ speed.
- quantum against context switch time ::@:: The quantum must stay large against the context switch time, or the switches consume the time they divide.
- rule of thumb for choosing a quantum ::@:: About 80 percent of central processing unit (CPU) bursts should be shorter than the quantum, because average turnaround improves when most processes finish inside one quantum.
- round-robin with bursts $24$, $3$ and $3$ all arriving at $0$ and a quantum of $4$: average waiting time, average turnaround time and average response time? ::@:: Waiting times $6$, $4$ and $7$, average $(6 + 4 + 7)/3 = 5.67$. Completions at $30$, $7$ and $10$, turnarounds averaging $(30 + 7 + 10)/3 = 15.67$. First runs end at $4$, $7$ and $10$, so response averages $(4 + 7 + 10)/3 = 7$.
- round-robin against first-come, first-served for ten jobs arriving at $0$, each needing $100$ time units, with a quantum of $1$ ::@:: Completions run $991$ to $1000$, averaging $995.5$, against $100$, $200$, …, $1000$ averaging $550$. Response falls from $550$ to $5.5$ over the same change, so turnaround gets worse while response gets better.
- why round-robin suits interactive systems ::@:: Round-robin preempts on a timer, so each process gets a share at regular intervals and the first response comes quickly.

### priority scheduling

Priority scheduling gives each process a priority number and runs the highest priority first. The convention used here takes the smallest integer as the highest priority, so priority $1$ outranks priority $5$, and every worked example below reads the numbers that way. UNIX and Linux keep that end, with nice $-20$ above nice $19$, while Windows turns it round and lets the larger number win. Only the ordering carries meaning, so a rule about priority stays incomplete until it names its convention.

The shortest-job family is the special case, and the convention decides how it is written. Where smaller is higher, non-preemptive priority equal to the predicted next burst is SJF, and preemptive priority equal to the time remaining is SRTF. A source that calls the priority the inverse of the burst assumes the other convention, where a larger number wins and $1/t$ puts the shortest burst on top. Both spellings are one rule. Mixing conventions ranks long bursts first.

Priority can preempt on the arrival of a higher-priority process or wait for the running process to leave, and equal priorities are served in FCFS order.

The weakness is starvation: a low-priority process may never run while higher-priority work keeps arriving. Aging repairs it by raising the priority of a waiting process, which in practice needs a timer started whenever the process joins the ready queue.

Five processes arriving together, with bursts 10, 1, 2, 1 and 5 and priorities 3, 1, 4, 5 and 2, run as $P_2$, $P_5$, $P_1$, $P_3$, $P_4$. Waiting times are 0, 1, 6, 16 and 18, so $(0 + 1 + 6 + 16 + 18)/5 = 8.2$.

Priorities can also order queues instead of single processes, with round-robin inside each priority. Five processes of burst 4, 5, 8, 7 and 3, priorities 3, 2, 2, 1 and 3, all arriving at 0, run $P_4$ to 7, then $P_2$ and $P_3$ in two-unit slices to 16 and 20, then $P_1$ and $P_5$ in two-unit slices to 26 and 27. Waiting times are 22, 11, 12, 0 and 24, so $(22 + 11 + 12 + 0 + 24)/5 = 13.8$. A process preempted inside such a scheme keeps its remaining quantum, so it resumes with what the timer had left rather than a fresh slice.

---

Flashcards for this section are as follows:

- priority scheduling rule ::@:: Each process carries a priority number and the highest priority runs, with equal priorities served in first-come, first-served order.
- priority convention when priority $1$ and priority $5$ are compared ::@:: The smallest integer is the highest priority, so $1$ outranks $5$, and equal priorities are served in first-come, first-served order.
- which end of a priority range such as $-20$ to $19$ is the high end ::@:: UNIX and Linux take the smaller value as higher, so nice $-20$ outranks nice $19$. Windows takes the larger number as higher.
- when shortest job first becomes priority scheduling ::@:: Where smaller is higher, priority equal to the predicted next burst is non-preemptive shortest job first, and priority equal to the time remaining is shortest remaining time first.
- why the shortest-job priority is sometimes written $1/t$ ::@:: That spelling assumes the convention where a larger number wins, so $1/t$ puts the shortest burst on top. Under smaller-is-higher the same rule is priority equal to $t$.
- preemptive and non-preemptive priority scheduling ::@:: Either an arriving process of higher priority preempts the running one, or the running process keeps the central processing unit (CPU) until it leaves.
- shortest job first as a case of priority scheduling ::@:: Where a smaller number wins, its priority is the predicted next central processing unit (CPU) burst, since a short burst then outranks a long one. The same rule on the time that remains, in the preemptive form, is shortest remaining time first.
- starvation under priority scheduling ::@:: A low-priority process may never run while higher-priority work keeps arriving.
- aging as a remedy for starvation ::@:: The priority of a waiting process rises as time passes, so it eventually outranks the work ahead of it. In practice a timer starts whenever the process joins the ready queue.
- priority scheduling with bursts $10$, $1$, $2$, $1$ and $5$ and priorities $3$, $1$, $4$, $5$ and $2$, all arriving at $0$: the run order and the average waiting time? ::@:: $P_2$, then $P_5$, then $P_1$, then $P_3$, then $P_4$, because the smallest priority number runs first. Waiting times are $0$, $1$, $6$, $16$ and $18$, average $8.2$.
- priority scheduling with round-robin inside each priority: bursts $4$, $5$, $8$, $7$ and $3$ with priorities $3$, $2$, $2$, $1$ and $3$, all arriving at $0$, quantum $2$: the average waiting time? ::@:: $P_4$ runs $0$ to $7$. $P_2$ and $P_3$ alternate to finish at $16$ and $20$. $P_1$ and $P_5$ alternate to finish at $26$ and $27$. Waiting times are $22$, $11$, $12$, $0$ and $24$, so $(22 + 11 + 12 + 0 + 24)/5 = 13.8$.
- remaining quantum of a preempted process ::@:: A preempted process keeps the quantum it had left and resumes with that, rather than starting a fresh slice, so the timer counts only central processing unit (CPU) time actually used.

### next CPU burst estimation

Shortest job first and shortest remaining time first both need the length of the next CPU burst, which is unknown when the decision is made. Exponential averaging predicts it from earlier bursts.

Let $t_n$ be the actual length of the $n$-th CPU burst, let $\tau_n$ be the prediction made for it, and let $\alpha$ be a weight with $0 \le \alpha \le 1$. The prediction for the next burst is $\tau_{n+1} = \alpha t_n + (1 - \alpha)\tau_n$. Expanding the recursion gives $\tau_{n+1} = \alpha t_n + (1-\alpha)\alpha t_{n-1} + \cdots + (1-\alpha)^n \alpha t_0 + (1-\alpha)^{n+1}\tau_0$, so every past burst and the initial guess $\tau_0$ contribute, and each older burst counts a factor $(1-\alpha)$ less than the burst after it.

The weight sets sensitivity to the newest measurement. A larger $\alpha$ trusts the last burst more and forgets history faster; a smaller one smooths the series. At $\alpha = 0$ the prediction stays at $\tau_0$ forever, and at $\alpha = 1$ it is the last burst itself. The weight on history is $(1 - \alpha)$, and the two weights sum to one. The usual choice is $\alpha = 1/2$, where the initial guess carries a weight of $(1/2)^{10} = 1/1024$ after ten rounds, small enough to ignore.

Starting from $\tau_0 = 10$ with bursts 6, 4, 6, 4, 13, 13 and 13, the first prediction is $(1/2)(6) + (1/2)(10) = 8$, the second $(1/2)(4) + (1/2)(8) = 6$, and the series then runs 6, 5, 9, 11 and 12.

---

Flashcards for this section are as follows:

- exponential averaging with $t_n$ the actual $n$-th central processing unit (CPU) burst, $\tau_n$ its prediction and $0 \le \alpha \le 1$ ::@:: The next prediction is $\tau_{n+1} = \alpha t_n + (1-\alpha)\tau_n$.
- what the expanded form of $\tau_{n+1}$ shows ::@:: Every past burst and the initial guess $\tau_0$ contribute, and each older burst counts a factor $(1-\alpha)$ less than the burst after it.
- what $\alpha$ measures in exponential averaging ::@:: The sensitivity to the newest burst. A larger $\alpha$ follows the last measurement more closely and forgets history faster; a smaller $\alpha$ smooths the series.
- weight $0$ in exponential averaging ::@:: The prediction never moves from the initial guess $\tau_0$, since recent history carries no weight.
- weight $1$ in exponential averaging ::@:: Only the most recent burst counts, so the prediction is the last measured burst.
- how fast history fades at $\alpha = 1/2$ ::@:: The initial guess carries a weight of $(1/2)^{10} = 1/1024$ after ten rounds, small enough to ignore.
- prediction series from $\tau_0 = 10$ with bursts $6$, $4$, $6$, $4$, $13$, $13$ and $13$ ::@:: $(1/2)(6) + (1/2)(10) = 8$, then $(1/2)(4) + (1/2)(8) = 6$, and then $6$, $5$, $9$, $11$ and $12$.
- with $\tau_1 = 8$ as the prediction for a burst and a second burst $t_1 = 4$, both under $\alpha = 1/2$: the prediction $\tau_2$ for the third burst? ::@:: $\tau_2 = (1/2)(4) + (1/2)(8) = 6$.
- why shortest job first needs a prediction ::@:: The policy compares next burst lengths, and those lengths are unknown when the decision is made, so it must estimate them from earlier bursts.

## queue-based scheduling

### multilevel queue scheduling

Multilevel queue scheduling sorts processes into separate queues by type, and a process keeps its queue for life. Each queue runs whatever algorithm suits its work. The queues themselves are served by fixed priority, where a higher queue preempts a lower one, or by a time slice, for example 60, 20, 10 and 10 percent of the processor.

Assignment is static, so a compute-heavy process that starts in the background queue stays there. Under fixed priority a busy foreground queue can starve the background queue.

Two queues show the fixed-priority case: a foreground queue running round-robin with a quantum of 2, a background queue running first-come, first-served, and every foreground process outranking every background one. $A$ and $B$, of burst 5 and 3, arrive at 0 and 1 and are foreground; $C$, of burst 4, arrives at 2 and is background. $A$ runs to 2, $B$ to 4, $A$ to 6, $B$ to 7, $A$ to 8, and $C$ then runs to 12. Waiting times are 3, 3 and 6, so $(3 + 3 + 6)/3 = 4$.

---

Flashcards for this section are as follows:

- multilevel queue scheduling ::@:: Processes are partitioned into separate queues by type, each queue runs its own algorithm, and a process keeps its queue for its whole life.
- how the queues themselves are served ::@:: Either by fixed priority, where a higher queue preempts a lower one, or by a time slice, for example 60, 20, 10 and 10 percent of the processor.
- why multilevel queue assignment is inflexible ::@:: A process is assigned to a queue once and stays there, so a compute-heavy process that starts in a background queue never moves up.
- two queues in fixed priority, the foreground one round-robin with quantum $2$, the background one first-come, first-served: $A$ of burst $5$ arriving at $0$ and $B$ of burst $3$ arriving at $1$ are foreground, $C$ of burst $4$ arriving at $2$ is background: the average waiting time? ::@:: $A$ runs $0$ to $2$, $B$ to $4$, $A$ to $6$, $B$ to $7$, $A$ to $8$, then $C$ to $12$. Waiting times are $3$, $3$ and $6$, so $(3 + 3 + 6)/3 = 4$.
- starvation under multilevel queue scheduling ::@:: Under fixed priority a busy higher queue keeps every lower queue waiting, and a process cannot leave its queue, so waiting does not help it.

### multilevel feedback queue scheduling

A multilevel feedback queue (MLFQ) lets a process move between queues, which a multilevel queue forbids. A new process enters the top queue. A process that exhausts its quantum there drops to the next queue, and one that keeps exhausting quanta sinks to the bottom queue, which usually runs first-come, first-served. Only an arrival in the top queue preempts; a process already waiting in a lower queue does not.

An MLFQ is defined by five decisions: how many queues it has, which algorithm each queue runs, when a process is demoted, when it is promoted, and which queue a process enters when it needs service.

The arrangement approximates shortest remaining time first without knowing a burst length in advance. A short interactive job finishes inside one quantum at the top, while a CPU-heavy job falls to the bottom and leaves the upper queues to the short work. Aging fits as well: periodically moving every job back to the top queue stops a long job from starving ([multilevel feedback queue](multilevel%20feedback%20queue.md#starvation%20and%20aging)). BSD Unix, Solaris and Windows NT and later all use it. See [multilevel feedback queue](multilevel%20feedback%20queue.md) for the queue structure, a worked schedule and the variant with one quantum per queue.

---

Flashcards for this section are as follows:

- multilevel feedback queue scheduling ::@:: A multilevel queue that lets a process move between queues, so a new process enters the top queue and sinks as it exhausts its quanta.
- defining parameters of a multilevel feedback queue ::@:: The number of queues, the algorithm each queue runs, the demotion rule, the promotion rule, and the queue a process enters when it needs service.
- how a multilevel feedback queue approximates shortest remaining time first ::@:: A short job finishes inside one quantum at the top, and a central processing unit (CPU)-heavy job sinks to the bottom, so the upper queues stay available to short work without any burst length being known in advance.
- systems that use a multilevel feedback queue ::@:: BSD Unix, Solaris, and Windows NT and later.
- why a multilevel feedback queue needs no burst prediction ::@:: Demotion by exhausted quantum measures how much processor time a job has taken, so behaviour is observed rather than predicted.
- where a multilevel feedback queue takes its preemptions from ::@:: An arrival in the top queue. A process already waiting in a lower queue does not preempt anything.
- which algorithm the bottom queue of a multilevel feedback queue usually runs ::@:: First-come, first-served.
- how a multilevel feedback queue avoids starving the jobs it demoted ::@:: A periodic reshuffle moves every job back to the top queue, so a CPU-bound job that sank still gets served.

## thread and multiprocessor scheduling

### process-contention scope and system-contention scope

A modern operating system schedules kernel-level threads, not processes. User-level threads belong to a thread library, which maps them onto kernel-level threads through a [lightweight process](thread%20(computing).md#lightweight%20process) (LWP): an intermediate object that looks like a virtual processor on which the library runs user threads, with one LWP per kernel thread.

Which user-level thread runs on an available LWP is process-contention scope (PCS). The competition is inside one process. The thread library makes the choice, and it normally follows priorities the programmer set, because the library cannot adjust them. PCS preempts a running user thread for a higher-priority one in the same process.

Which kernel thread runs on a processor is system-contention scope (SCS), and the competition there is among every thread in the system. That is CPU scheduling. Systems with a one-to-one mapping, such as Windows, Linux and Solaris, skip user-level scheduling and use SCS alone.

---

Flashcards for this section are as follows:

- process-contention scope ::@:: The thread library chooses which user-level thread runs on an available lightweight process (LWP). Competition is inside one process, and the choice normally follows priorities the programmer set.
- system-contention scope ::@:: The operating system chooses which kernel thread runs on a processor, competing among every thread in the system. This is central processing unit (CPU) scheduling.
- who sets priority under process-contention scope ::@:: The programmer, through the thread library, which cannot adjust the priority itself.
- scope used by one-to-one threading systems ::@:: System-contention scope alone, since Windows, Linux and Solaris map every user thread to a kernel thread and leave no user-level scheduling to do.
- what a modern operating system schedules ::@:: Kernel-level threads rather than processes, since user-level threads belong to a thread library, which maps them onto kernel-level threads.
- what preempts a running user thread under process-contention scope ::@:: A higher-priority user-level thread in the same process. The thread library makes that choice, so the operating system is not involved.

### symmetric and asymmetric multiprocessing scheduling

Two arrangements of processors change scheduling, and the hardware comparison is in [multiprocessing](multiprocessing.md#multiprocessor%20systems). In asymmetric multiprocessing one master processor takes every scheduling decision, input/output (I/O) operation and system activity, and the other processors run only user code. One processor touching the kernel data structures removes the need to share them, but the master becomes a bottleneck.

In symmetric multiprocessing (SMP) each processor schedules itself. The ready queue may be common to all processors or private to each. A common queue lets two processors choose the same thread unless the choice is made safely. Every modern system is SMP, including Linux, Windows, macOS, Android and iOS.

---

Flashcards for this section are as follows:

- advantage and cost of asymmetric multiprocessing ::@:: Only one processor touches the kernel data structures, so they need no sharing. The master processor can become a bottleneck.
- risk of a common ready queue in symmetric multiprocessing ::@:: Two processors can choose the same thread unless the choice is made safely.
- which systems schedule with symmetric multiprocessing ::@:: Every modern system, including Linux, Windows, macOS, Android and iOS.

### load balancing and processor affinity

A symmetric multiprocessing system with private ready queues needs a way to even out the work. Push migration runs a periodic check and moves tasks off an overloaded processor. Pull migration lets an idle processor take a waiting task from a busy one. The Linux completely fair scheduler (CFS) does both.

Migration costs cache. The cache of a processor holds what the thread running there has touched, so moving a thread invalidates one cache and repopulates another. A thread's tendency to keep to the processor it ran on is its processor affinity. Soft affinity means the operating system tries to keep a thread where it is without promising it, and private ready queues give it for nothing. Hard affinity lets a process restrict itself to a set of processors, which the Linux system call `sched_setaffinity()` does.

Load balancing and affinity pull against each other. On a [non-uniform memory access](multiprocessing.md#non-uniform%20memory%20access) (NUMA) machine, where a processor reaches some main memory faster than the rest, the same tension appears between processors and memory.

---

Flashcards for this section are as follows:

- push migration ::@:: A periodic check on each processor that moves tasks from an overloaded processor to an idle or less busy one.
- pull migration ::@:: An idle processor takes a waiting task from a busy processor.
- which load balancing techniques the Linux completely fair scheduler (CFS) uses ::@:: Both push migration and pull migration.
- processor affinity ::@:: A thread's tendency to keep running on the processor it ran on before, because that processor's cache holds what the thread has touched.
- cost of migrating a thread ::@:: The cache of the old processor is invalidated and the new one repopulated, so memory access slows down afterwards.
- soft affinity against hard affinity ::@:: Soft affinity means the operating system tries to keep a thread on the same processor without promising it. Hard affinity lets a process restrict itself to a set of processors, which the Linux system call `sched_setaffinity()` does.
- why private ready queues give affinity for free ::@:: A thread stays on the processor whose queue it joined, so it keeps running where its cache contents are, with no affinity mechanism at all.
- tension between load balancing and affinity ::@:: Evening out the work moves threads between processors, and every move throws away the cache state that affinity was protecting.
- why non-uniform memory access (NUMA) complicates affinity ::@:: A processor reaches some parts of main memory faster than others, so a thread can be tied to a processor, to a part of memory, or to both.

### multicore scheduling

Several cores on one chip run faster and draw less power than several chips, and they complicate scheduling. A core that misses in its cache waits a long time for memory, a memory stall that leaves the core idle while it waits.

Chip multithreading (CMT) fills that idle time. One core carries several hardware threads, each with its own architectural state, meaning its own program counter and registers, and the operating system sees each as a logical processor. Intel calls this hyperthreading. A dual-core chip with two hardware threads per core presents four logical processors, and the UltraSPARC T3 presented 128, from 16 cores with 8 hardware threads each.

Scheduling then splits into two levels. The operating system decides which software thread, a kernel thread, runs on which logical processor, which is CPU scheduling. Each core then decides which hardware thread runs next on the physical core, often by round-robin.

---

Flashcards for this section are as follows:

- memory stall ::@:: Time a processor spends waiting for data from memory or cache, mostly after a cache miss. The core sits idle meanwhile, because the processor runs far faster than memory.
- chip multithreading ::@:: One core carries several hardware threads, each with its own program counter and registers, and each appears to the operating system as a logical processor. Intel calls it hyperthreading.
- logical processors presented by a dual-core chip with $2$ hardware threads per core, and by the UltraSPARC T3 with $16$ cores of $8$ hardware threads ::@:: The chip presents $4$ logical processors. The UltraSPARC T3 presents $128$.
- two levels of scheduling on a multithreaded multicore chip ::@:: The operating system picks a software thread, a kernel thread, for each logical processor, and each core picks which hardware thread runs next on the physical core.
- who chooses among hardware threads on a core ::@:: The core itself, typically by round-robin, without the operating system's involvement.
- why chip multithreading helps a stalled core ::@:: When one hardware thread stalls waiting for memory, the core switches to another and makes progress instead of idling.

## real-time scheduling

A real-time scheduler is judged on predictability rather than speed. A hard real-time system must complete every task by its deadline, and service after the deadline is worth as much as no service. A soft real-time system promises less: it prefers a critical process over non-critical ones, and a deadline may still slip. A preemptive priority-based scheduler gives soft real-time behaviour at best, since priority alone cannot guarantee a completion time.

The tasks are usually periodic, needing the processor at fixed intervals. A task has a processing time $t$, a deadline $d$ and a period $p$, with $0 \le t \le d \le p$, and its rate is $1/p$. Its share of the processor is $t/p$. A process may announce its deadline when it becomes runnable, and the scheduler admits it only if it can guarantee that deadline. Refusing admission is what makes a guarantee possible.

---

Flashcards for this section are as follows:

- hard real-time scheduling ::@:: Every task must be serviced by its deadline, and service after the deadline is worth as much as no service at all.
- soft real-time scheduling ::@:: Soft real-time scheduling guarantees only that a critical real-time process is preferred over non-critical ones, so a deadline may still be missed.
- why a preemptive priority scheduler gives only soft real-time behaviour ::@:: Priority decides the order of service but cannot guarantee a completion time, and only a guarantee serves a hard deadline.
- parameters of a periodic task with processing time $t$, deadline $d$ and period $p$ ::@:: They satisfy $0 \le t \le d \le p$. The rate is $1/p$, and the task's share of the processor is $t/p$.
- admission control in real-time scheduling ::@:: A process announces its deadline when it becomes runnable, and the scheduler admits it only if it can guarantee the deadline, refusing the process otherwise.
- a periodic task needs $20$ milliseconds of processing in each period of $50$ milliseconds: its rate and its share of the processor? ::@:: Rate $1/p = 1/50$ per millisecond. Share $t/p = 20/50 = 0.4$, so 40 percent of the processor.

### rate-monotonic scheduling

Rate-monotonic scheduling (RMS) gives each task a static priority taken from its period: the shorter the period, the higher the priority. A task needing the processor more often should win. RMS preempts. Its optimality holds among fixed-priority algorithms alone: if no assignment of permanent priorities can schedule a set, RMS cannot either. A rule that reconsiders priority while the system runs sits outside that class, and the next section gives one that schedules a set RMS fails on.

A utilisation test follows from the same argument. A set of $n$ periodic tasks is certainly schedulable when its total utilisation stays under $n(2^{1/n} - 1)$, which is $0.828$ for two tasks and falls toward $0.693$ as $n$ grows. The bound is sufficient, not necessary: a set above it may still meet every deadline, so a schedule that fails there is a real failure, while a schedule that succeeds is no contradiction.

With processing times 20 and 35 and periods 50 and 100, the shares are $20/50 = 0.4$ and $35/100 = 0.35$, 75 percent together. The first task runs 0 to 20, the second 20 to 50, the first again 50 to 70, and the second finishes its remaining 5 time units at 75, well before its deadline at 100. Every deadline is met.

Raising the load breaks it. With processing times 25 and 35 and periods 50 and 80, the shares are $25/50 = 0.5$ and $35/80 = 0.4375$, so $0.9375$ together, below 100 percent yet above the two-task bound of $0.828$. The first task runs 0 to 25, the second runs 25 to 50 with 10 time units left, the first runs 50 to 75, and the second finishes at 85, five time units past its deadline at 80. The processor still had $0.0625$ of its capacity unused, which a rule that reconsiders priority could have spent.

---

Flashcards for this section are as follows:

- rate-monotonic scheduling rule ::@:: Static priority from the period: the shorter the period, the higher the priority, and a task needing the processor more often wins.
- why rate-monotonic scheduling is called optimal ::@:: If a task set cannot be scheduled by it, no other algorithm that assigns static priorities can schedule that set either.
- what rate-monotonic optimality leaves out ::@:: Algorithms that change priority at run time, such as earliest deadline first, which schedule some sets that rate-monotonic scheduling fails on.
- utilisation bound of rate-monotonic scheduling for $n$ tasks ::@:: $n(2^{1/n} - 1)$, which is $0.828$ for two tasks and falls toward $0.693$ as $n$ grows. A set under it is certainly schedulable.
- whether the rate-monotonic bound is necessary ::@:: No, it is sufficient. A set above it may still meet every deadline, so a failure there proves only that the bound says nothing.
- why rate-monotonic scheduling can miss deadlines below 100 percent utilisation ::@:: Its priorities come from the periods alone, so utilisation under 1 does not imply a schedule; the spare capacity may sit in a gap no priority order can use.
- rate-monotonic scheduling on tasks of processing time $20$ and $35$ with periods $50$ and $100$ ::@:: Shares are $20/50 = 0.4$ and $35/100 = 0.35$, $75$ percent together. The schedule runs $0$ to $20$, $20$ to $50$, $50$ to $70$, then finishes the second task at $75$, so every deadline is met.
- rate-monotonic scheduling on tasks of processing time $25$ and $35$ with periods $50$ and $80$ ::@:: Shares are $25/50 = 0.5$ and $35/80 = 0.4375$, so $0.9375$ together, under $1$ but over the two-task bound of $0.828$. The second task finishes at $85$ and misses its deadline at $80$.
- which task wins under rate-monotonic scheduling ::@:: The task with the shortest period, which is the task with the highest rate of processor requests, regardless of how much processor time it needs.

### earliest deadline first

Earliest deadline first (EDF) makes priority dynamic: at each decision the ready task with the earliest deadline runs, and a newly runnable task can preempt. It needs neither periodic tasks nor a constant burst length, only that a task announce its deadline when it becomes runnable.

EDF is optimal among dynamic-priority algorithms, with no bound short of 100 percent: any task set whose total utilisation is at most 1 meets every deadline, which is exactly what rate-monotonic scheduling cannot promise. The set that missed a deadline above therefore meets every deadline here. In practice that bound is unreachable, because context switches and interrupt handling consume processor time.

On the same two tasks, of processing time 25 and 35 with periods 50 and 80, the first runs 0 to 25, the second runs 25 to 60, the first runs 60 to 85, and the second runs 85 to 120 for its next period. Every deadline is met.

---

Flashcards for this section are as follows:

- earliest deadline first rule ::@:: Priority is dynamic: at each decision the ready task with the earliest deadline runs, and a newly runnable task can preempt.
- what earliest deadline first requires of a task ::@:: Only that the task announce its deadline when it becomes runnable. The tasks need not be periodic and need not use a constant burst length.
- theoretical utilization bound of earliest deadline first ::@:: Any task set whose total utilization is at most 100 percent meets every deadline, and no tighter bound exists. That makes earliest deadline first optimal among dynamic-priority algorithms.
- why earliest deadline first beats rate-monotonic scheduling on two tasks using $0.9375$ of the processor ::@:: Both tasks together use $0.9375$ of the processor, under 1 but over the rate-monotonic bound of $0.828$. Rate-monotonic scheduling misses a deadline, and earliest deadline first meets every one.
- why the earliest deadline first bound is unreachable in practice ::@:: Context switches and interrupt handling consume processor time, so some capacity is lost before any task runs.
- earliest deadline first on tasks of processing time $25$ and $35$ with periods $50$ and $80$ ::@:: The schedule runs $0$ to $25$, $25$ to $60$, $60$ to $85$, then $85$ to $120$ for the second task's next period, so every deadline is met.
- how earliest deadline first differs from rate-monotonic scheduling ::@:: Rate-monotonic scheduling fixes a static priority from the period, while earliest deadline first recomputes priority from the deadline at each decision.

## starvation and fairness

Starvation is a process waiting while others keep going ahead of it, for as long as the system runs. It belongs to the policy, not to one unlucky schedule: any rule that prefers some work can hold the rest off indefinitely.

---

Flashcards for this section are as follows:

- starvation ::@:: A process waiting indefinitely while other work keeps taking the processor ahead of it, a property of the scheduling policy rather than of one schedule.

### starvation by policy

| policy | starves | the process that waits |
| --- | --- | --- |
| first-come, first-served | no | none; an arrival joins the back and is reached in turn |
| shortest job first | yes | a long burst, while shorter ones keep arriving |
| shortest remaining time first | yes | the same long burst, and a short preempting job makes it worse |
| round-robin | no | none; every ready process gets a quantum within $n$ turns |
| priority scheduling | yes | the lowest priority, while higher-priority work keeps arriving |
| multilevel queue, fixed priority | yes | every process in a lower queue, while a higher queue has work |
| multilevel feedback queue | without a boost | a CPU-bound process that sank to the bottom queue |
| rate-monotonic scheduling | beyond its utilisation bound | the longest-period task, whose low priority leaves it no slot |
| earliest deadline first | under overload | the task with the latest deadline, though every task runs below full utilisation |

---

Flashcards for this section are as follows:

- policies that cannot starve a process ::@:: First-come, first-served and round-robin, since each serves every ready process after a bounded number of turns.
- policies that can starve a process ::@:: Shortest job first, shortest remaining time first, priority scheduling, fixed-priority multilevel queue, multilevel feedback queue without a boost, and rate-monotonic scheduling past its utilisation bound.
- why round-robin cannot starve a process ::@:: The queue rotates after each quantum, so a process waits at most one quantum for each ready process ahead of it, whatever the other processes do.

### removing starvation

Aging raises the priority of a waiting process until it outranks the work ahead, which turns a fixed priority into a moving one. A periodic reshuffle in a multilevel feedback queue returns every job to the top queue, so work that sank is served again. The rotating quantum of round-robin caps the wait at one quantum per process ahead, so it needs neither remedy.

Being optimal and being fair are separate. Shortest remaining time first gives the lowest average waiting time of any policy here, and it also holds a long burst off longest, so a scheduler can win on the average and lose on the worst case.

---

Flashcards for this section are as follows:

- why shortest remaining time first can be optimal and still unfair ::@:: Shortest remaining time first gives the lowest average waiting time of the policies here, and it holds a long burst off for as long as short work keeps arriving.

## algorithm evaluation

Choosing a policy needs criteria before numbers. A requirement is usually one measure optimized under a constraint on another: maximize CPU utilization subject to a response time of at most 300 milliseconds, or maximize throughput subject to average turnaround time growing linearly with total execution time.

Deterministic modeling applies a policy to one fixed workload and reports exact figures. Five processes arriving at time 0 with bursts 10, 29, 3, 7 and 12 show how far the figures spread. FCFS gives waiting times 0, 10, 39, 42 and 49, averaging $(0 + 10 + 39 + 42 + 49)/5 = 28$. SJF gives 0, 3, 10, 20 and 32, averaging $65/5 = 13$, and RR with a quantum of 10 gives 0, 32, 20, 23 and 40, averaging $115/5 = 23$. The numbers come quickly, but they describe that workload alone, and no single fixed workload stands for a real system.

Queueing models describe the machine as a network of servers, each with its own queue: the processor with the ready queue, the I/O system with its device queues. Little's law relates the steady-state queue length $n$, the arrival rate $\lambda$ and the average time $W$ a job spends in what was counted, by $n = \lambda W$. It holds for any policy and any arrival distribution, but it says nothing about which average $W$ is until the count is named.

CPU scheduling has several candidates, and which set gets counted decides between them. Count the processes waiting in the ready queue, leaving out the one running, and $W$ is the waiting-time criterion: seven processes arriving per second with 14 in the ready queue gives $W = n/\lambda = 14/7 = 2$ seconds of waiting. Count every process in the system, the running one included, and the length rises by one while $W$ becomes the turnaround time, waiting plus service. Neither count yields response time, which ends at the first run and so depends on how the policy slices the work. Three different averages come out of the same law, and the report is only as precise as the quantity it counted.

The models need arrival and service rates, and only a few distributions stay tractable, with assumptions that often do not hold in practice.

Simulation programs a model of the machine and advances a clock, changing device, process and scheduler state as it goes and collecting statistics. The workload comes from a random number generator over a chosen distribution, or from a trace file recorded on a real system. Simulation is more accurate than a queueing model and safer than experimenting on a running machine.

Implementation runs the candidate policy on real work. It is the most general approach, but writing a scheduler costs money and risks new bugs, and the environment that produced the measurements keeps changing. Systems expose tunable parameters instead, and the Portable Operating System Interface (POSIX), Java and Windows all provide interfaces that set the priority of a process or thread, which helps that program rather than the system as a whole.

---

Flashcards for this section are as follows:

- first step in choosing a policy toward maximum central processing unit (CPU) utilization under a $300$ millisecond response time ::@:: Fixing the criteria: one measure optimized under a constraint on another.
- deterministic modeling ::@:: Applying a policy to one fixed workload and reporting exact figures for it, such as average waiting time.
- five processes arriving at time $0$ with bursts $10$, $29$, $3$, $7$ and $12$: average waiting time under first-come, first-served, under shortest job first, and under round-robin with a quantum of $10$? ::@:: Waiting times $0$, $10$, $39$, $42$ and $49$ under first-come, first-served, averaging $140/5 = 28$. $0$, $3$, $10$, $20$ and $32$ under shortest job first, averaging $65/5 = 13$. $0$, $32$, $20$, $23$ and $40$ under round-robin, averaging $115/5 = 23$.
- limits of deterministic modeling ::@:: Deterministic modeling needs exact inputs and describes only those inputs, and no single fixed workload stands for a real system, whose work changes.
- queueing model of a computer system ::@:: A network of servers, each with a queue of waiting processes: the processor with its ready queue and the input/output (I/O) system with its device queues. Arrival and service rates give utilization, average queue length and average wait.
- Little's law for average queue length $n$, average arrival rate $\lambda$ and average time $W$ in the counted set ::@:: $n = \lambda W$ in steady state. It holds for any scheduling policy and any arrival distribution.
- what $W$ becomes in Little's law when the ready queue alone is counted ::@:: The waiting-time criterion: the time a process spends queued and not running, which is what CPU scheduling calls waiting time.
- what $W$ becomes in Little's law when every process in the system is counted ::@:: The turnaround time, waiting plus service, because the running process adds one to the counted length.
- why Little's law does not directly give response time ::@:: Response time ends at the first run and depends on how the policy slices the work, while the law only relates a counted length to the time jobs spend in that set.
- $7$ processes arrive per second and $14$ wait in the ready queue, the running one excluded: the average waiting time from Little's law? ::@:: $W = n/\lambda = 14/7 = 2$ seconds of waiting. Had the 14 counted every process in the system, the same calculation would give the turnaround time instead.
- limits of queueing models ::@:: Only a few distributions stay mathematically tractable, and the assumptions that make the models solvable are often unrealistic.
- simulation as an evaluation method ::@:: A program models the machine and advances a clock, collecting performance statistics as device, process and scheduler state change.
- two sources of simulation workload ::@:: A random number generator over a chosen probability distribution, or a trace file recording the events of a real system.
- implementation as an evaluation method ::@:: The candidate policy runs on real work in a real system. It is the most flexible and general method, and it costs the effort of writing a scheduler and the risk of new bugs.
- how real systems avoid replacing the scheduler ::@:: They expose tunable parameters, and interfaces such as the Portable Operating System Interface (POSIX), Java and Windows let a program set the priority of a process or thread, which helps that program rather than the system as a whole.
- simulation against a queueing model and against implementation ::@:: Simulation is more accurate than a queueing model and safer than experimenting on a running machine.
