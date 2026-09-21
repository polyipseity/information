---
aliases:
  - ELEC 3120 checkpoint 4
  - ELEC3120 checkpoint 4
  - HKUST ELEC 3120 checkpoint 4
  - HKUST ELEC3120 checkpoint 4
tags:
  - date/2026/11/27
  - flashcard/active/special/academia/HKUST/ELEC_3120/assignments/checkpoint_4/index
  - language/in/English
---

# checkpoint 4

- HKUST ELEC 3120

---

- title: Checkpoint 4: Design your own algorithm!
- due: 2026-11-27T23:59:59+08:00
- points: \[missing\]
- submitting: \[missing\]

---

Tentative release: Monday 09/11

Tentative due date: 27/11 23:59

## late policy

- You have free 4 late days in total.
- You can use late days for assignments. A late day extends the deadline 24 hours.
- Once you have used all 4 late days, the penalty is 20% for each additional late day (5 days later there will be no points).
- Remember that any questions should go to Ed instead of emailing TAs or the professor.

## introduction

In this checkpoint, you need to finish two tasks based on __your own CP3 code__. So if you have not finished your CP3, you need to implement it at first (__we don't provide sample answer code__). We will add some regression tests for CP3 in CP4.

- Dr. Matt Mathis's hypothesis,
- Your own CCA.

## dr. Matt Mathis's hypothesis

### hypothesis

In Checkpoint 1, we asked you questions and you formed your own hypotheses. In this checkpoint, we are going to give you a hypothesis formulated by Dr. Matt Mathis: that TCP Reno implementations obey the following throughput equation: __throughput = (MSS/RTT)*(C/sqrt(p))__, where __C__ is a constant, __p__ is the loss probability, RTT is the round-trip time and MSS is 1400 bytes in our project. The following measurements will help you verify this hypothesis.

(Reference: DOI 10.1145/263932.264023)

### experiment

Use tcconfig (checkpoint 1) to adjust the loss probability __p__ on the sender node to different values.

```sh
sudo tcset eth0 --rate 10Mbps --delay 20ms --loss 0.01%
```

For different values of __p__, __transfer a large file__ and measure the duration of the transfer (make sure to adjust the file size so that your transfer takes at least a few seconds). Use the transfer duration and the file size to calculate the throughput. Repeat the same experiment 10 times for each loss probability. Create a line plot with __1/sqrt(p)__ on the x axis and throughput on the y axis. Do linear regression and include the regression line on the same plot.

### inference

Based on the results of your experiments, we ask that you answer the following questions:

- Using your linear regression, what value did you find for __C__?
- Compute the Pearson Correlation Coefficient between __1/sqrt(p)__ and the throughput that you measured.
- Does your data corroborate Dr. Mattis's hypothesis? Why or why not?

### hint

Due to the lack of the timeout retransmission, sometimes your program may stuck please try again.

## your own CCA

You now have the opportunity to design your own CCA with the goal of outperforming TCP Reno and you can modify anything you like.

- The metric is throughput (as measured by the time it takes to transfer a 1MB file).

### hints

- You can go through the lecture: Congestion Control and lecture: Advanced Congestion Control again.
- Due to the lack of the timeout retransmission, sometimes your program may stuck please try/submit again.
- __Test link: RTT = 200ms, the buffer size of the router is infinite. But the router will add extra delay Xms when the buffer depth exceeds N.__ For example, if N = 5 and there are currently 10 packets in the buffer, extra delay will be added for packets 6 through 10.

### how to test by yourself

#### tcconfig

You can simulate the link (bandwidth, latency and loss rate) by tcconfig.

```sh
sudo tcset eth0 --rate 10Mbps --delay 20ms --loss 0.01%
```

#### burst

You can simulate the burst traffic by starting an another file transfer between two VMs.

#### duplicate ACKs

You can manually send duplicate ACKs at your recevier to simulate the congestion scenarios.

## what to submit

Like the checkpoint 1, we have one assignment for the codes and one assignment for the report.

### codes

Your implementation should be in the following files: `foggy_function.cc`, `foggy_tcp.cc`, `foggy_function.h` and `foggy_tcp.h`. You can run the `submit.py` at the root of the project which will generate a `submit.zip` file including these four files, then submit the `submit.zip` file to Gradescope. The autograder will copy those four files you submitted to the starter codes and do the testing.

We will evaluate your CCA by autograder and use a leaderboard to show the results in real time.

### report

The report should include two parts: (1) Dr. Matt Mathis's hypothesis and (2) Your own CCA.

__Dr. Matt Mathis's hypothesis__:

- Create a line plot with __1/sqrt(p)__ on the x axis and throughput on the y axis.
- Do linear regression and include the regression line on the same plot.
- Using your linear regression, what value did you find for __C__?
- Compute the Pearson Correlation Coefficient between __1/sqrt(p)__ and the throughput that you measured.
- Does your data corroborate Dr. Matt Mathis's hypothesis? Why or why not?

__Your own CCA__:

In your report include a section called __Algorithm Proposal__. In this section, you should:

- Propose a new algorithm (or a modification to Reno) that improves its throughput. Provide a detailed algorithm description, including why your new algorithm will improve throughput relative to your Reno implementation.

In your report include a section called __Algorithm Evaluation__. In this section, you should:

- Provide data comparing your Reno implementation to your new algorithm completing a 1MB transfer.
- That means how long does it take for a single connection to transfer 1MB.

## attachments

- \[missing\]

## submission

- submission

## solution

- \[missing\]
