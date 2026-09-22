---
aliases:
  - Computer Communication Networks
  - Computer Networks
  - ELEC 3120
  - ELEC 3120 index
  - ELEC3120
  - ELEC3120 index
  - HKUST ELEC 3120
  - HKUST ELEC 3120 index
  - HKUST ELEC3120
  - HKUST ELEC3120 index
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/index
  - function/index
  - language/in/English
---

# index

- HKUST ELEC 3120
- name: Computer Communication Networks
- credits: 3

---

ELEC 3120 is an introductory course in computer networks, emphasizing the performance and engineering tradeoffs behind network design and implementation. It covers congestion, flow, and error control; routing; addressing; naming; multicasting; switching; internetworking; and network security, with examples drawn mainly from the Internet. Grading rests on homework assignments, one semester-long project, one midterm examination, and one final examination.

## children

- [assignments/](assignments/index.md)
- [HTTP](HTTP.md)
- [Mathis equation](Mathis%20equation.md)
- [TCP congestion control](TCP%20congestion%20control.md)
- [TCP loss recovery](TCP%20loss%20recovery.md)
- [answering a question](answering%20a%20question.md)
- [bandwidth (computing)](bandwidth%20(computing).md)
- [computer network](computer%20network.md)
- [flow control (data)](flow%20control%20(data).md)
- [head-of-line blocking](head-of-line%20blocking.md)
- [network delay](network%20delay.md)
- [packet loss](packet%20loss.md)
- [sliding window protocol](sliding%20window%20protocol.md)
- [transmission medium](transmission%20medium.md)

## logistics

- prerequisites
    - COMP 1021 Python Programming
    - COMP 2011 (C++ Programming); strongly recommended but not enforced
- grading
    - homework assignments: 32%, four at 8% each
    - project: 20%, four checkpoints at 5% each
    - midterm examination: 20%
    - final examination: 30%
- grade promise
    - 90% and above is at least A-
    - 80% and above is at least B-
    - 70% and above is at least C-
    - 60% and above is at least D
    - a score above the median is at least B range, and the grade is never adjusted down
- late work
    - 4 free late days in total
    - a late day extends the deadline by 24 hours
    - beyond the four late days, each additional late day costs 20% of the assignment
    - from five late days onward an assignment scores no points
    - late days are counted at the end of the semester in the student's favour
    - extra late days are granted for a crisis or emergency, on request by email with the student's advisor copied
    - note: the lecture states a different penalty, 10% per assignment for extra late days and nothing accepted more than 48 hours late without a crisis
- assignment timing
    - released on a Friday and due on the Friday two weeks later, with a late deadline on the Sunday two weeks later
    - support in the instructor's Monday office hours and at other times from the teaching assistants
- office hours: by appointment, usually Monday afternoon, Rm 2441 (<https://calendar.app.google/XTU8qeeYFiUHh3qv7>)
- questions: Ed rather than email to the instructor or the teaching assistants (<https://edstem.org/au/courses/41196/discussion>)
- submissions and feedback: Gradescope, reachable through Canvas (<https://www.gradescope.com/courses/1384476>)
- website: <https://www.foggynetwork.com>
- academic integrity
    - generative AI tools are encouraged, but nothing may be copied and pasted; submissions are checked for similarity and for generated text
    - project code must be the student's own work apart from the starter code, standard libraries, and packages named in the handout; posting it publicly and using posted code are both violations
    - the material may be discussed with others, but the submission must be the student's own, and code should be written only after going over the discussion again
- accommodations: students registered with the Special Education Needs office bring their accommodations sheet to the instructor for signature, or email a copy
- written answers: state the answer, its evidence, and a warrant for each piece of evidence; see [answering a question](answering%20a%20question.md)
- sections
    - lecture: L1
        - L1: LTL, CYT Bldg; MondayT13:30:00/MondayT14:50:00, FridayT09:00:00/FridayT10:20:00
    - tutorials: T2
        - T1: Rm 5583, Lift 29-30; MondayT15:00:00/MondayT15:50:00
        - T2: Rm 2504, Lift 25-26; FridayT15:00:00/FridayT15:50:00
- note: the lecture and tutorial schedule is tentative; lecture topics, tutorial topics, the midterm, and assignment and project dates may change
- note: all times are Hong Kong time

## overview

- official course outline
    - congestion, flow, and error control
    - routing, addressing, and naming
    - multicasting and switching
    - internetworking
    - network security
- course parts
    - Internet basics: what makes the Internet work, from where the data goes and where domain names come from, to loss, corruption, and why some networks are slow or fast
    - understanding the network: what makes the Internet better, from content delivery and the versions of HTTP to privacy and the effect of network structure on application performance
- protocols covered: ARP, IP, ICMP, IPSec, OSPF, RIP, NAT, MAC, VLAN, TCP, UDP, QUIC, RTP, RTCP, SDP, DHCP, DNS, SMTP, FTP, IMAP, SSH, PPPoE, MPLS, RPC, HTTP, HTTPS
- course structure
    - four homework assignments
    - one semester-long project in four checkpoints, built in one or teams of two
    - one midterm examination and one final examination
- teaching order: from the top of the Internet and its services down to the bits on the wires
- project path
    - [sliding window protocol](sliding%20window%20protocol.md)
    - [TCP loss recovery](TCP%20loss%20recovery.md)
    - [flow control (data)](flow%20control%20(data).md)
    - [TCP congestion control](TCP%20congestion%20control.md)
    - [Mathis equation](Mathis%20equation.md)
- notes
    - the project implements TCP in C++ for a client and a server, each in its own VirtualBox virtual machine, with Vagrant for the environment and `tcconfig` for the link conditions

## week 1 lecture 1

- datetime: 2026-09-04T09:00:00+08:00/2026-09-04T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: network transmission and performance
- [transmission medium](transmission%20medium.md)
    - [§ media](transmission%20medium.md#media)
    - [§ data encoding](transmission%20medium.md#data%20encoding)
    - [§ what the medium determines](transmission%20medium.md#what%20the%20medium%20determines)
- [computer network](computer%20network.md)
    - [§ the parts of a network](computer%20network.md#the%20parts%20of%20a%20network)
    - [§ the Internet](computer%20network.md#the%20internet)
- [bandwidth (computing)](bandwidth%20(computing).md)
    - [§ units](bandwidth%20(computing).md#units)
- [network delay](network%20delay.md)
    - [§ pipe model](network%20delay.md#pipe%20model)
    - [§ transmission delay](network%20delay.md#transmission%20delay)
    - [§ propagation delay](network%20delay.md#propagation%20delay)
    - [§ packet delay](network%20delay.md#packet%20delay)
    - [§ throughput and latency](network%20delay.md#throughput%20and%20latency)
- [packet loss](packet%20loss.md)
    - [§ error rates](packet%20loss.md#error%20rates)
    - [§ causes of random loss](packet%20loss.md#causes%20of%20random%20loss)
- [answering a question](answering%20a%20question.md)
    - [§ the three parts](answering%20a%20question.md#the%20three%20parts)

## week 1 tutorial 1

- datetime: 2026-09-04T15:00:00+08:00/2026-09-04T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- status: unscheduled

## week 2 lecture 1

- datetime: 2026-09-07T13:30:00+08:00/2026-09-07T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: the Web
- [HTTP](HTTP.md)
    - [§ client-server model](HTTP.md#client-server%20model)
    - [§ request and response messages](HTTP.md#request%20and%20response%20messages)
    - [§ persistent connections](HTTP.md#persistent%20connections)
    - [§ pipelining](HTTP.md#pipelining)
    - [§ HTTP/2](HTTP.md#http2)
    - [§ HTTP/3](HTTP.md#http3)
- [head-of-line blocking](head-of-line%20blocking.md)
    - [§ application-layer HOL blocking in HTTP](head-of-line%20blocking.md#application-layer%20hol%20blocking%20in%20http)
    - [§ transport-layer HOL blocking in TCP](head-of-line%20blocking.md#transport-layer%20hol%20blocking%20in%20tcp)
    - [§ fixes across protocol generations](head-of-line%20blocking.md#fixes%20across%20protocol%20generations)

## week 2 lecture 2

- datetime: 2026-09-11T09:00:00+08:00/2026-09-11T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: the Web, continued

## week 2 tutorial 1

- datetime: 2026-09-11T15:00:00+08:00/2026-09-11T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: coding recap; compiling and debugging C++ code

## week 3 lecture 1

- datetime: 2026-09-14T13:30:00+08:00/2026-09-14T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: video streaming

## week 3 lecture 2

- datetime: 2026-09-18T09:00:00+08:00/2026-09-18T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: video streaming, continued

## week 3 tutorial 1

- datetime: 2026-09-18T15:00:00+08:00/2026-09-18T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: introduction to checkpoint 1

## week 4 lecture 1

- datetime: 2026-09-21T13:30:00+08:00/2026-09-21T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: transport model

## week 4 lecture 2

- datetime: 2026-09-25T09:00:00+08:00/2026-09-25T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: TCP basics

## week 4 tutorial 1

- datetime: 2026-09-25T15:00:00+08:00/2026-09-25T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: coding advanced; Visual Studio Code, Copilot, and Cursor

## week 5 lecture 1

- datetime: 2026-09-28T13:30:00+08:00/2026-09-28T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: congestion control

## week 5 lecture 2

- datetime: 2026-10-02T09:00:00+08:00/2026-10-02T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: congestion control, continued
- ELEC 3120 / [homework 1](assignments/homework%201/index.md)
- ELEC 3120 / [checkpoint 1](assignments/checkpoint%201/index.md)

## week 5 tutorial 1

- datetime: 2026-10-02T15:00:00+08:00/2026-10-02T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: introduction to checkpoint 2

## week 6 lecture 1

- datetime: 2026-10-05T13:30:00+08:00/2026-10-05T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: queue management

## week 6 lecture 2

- datetime: 2026-10-09T09:00:00+08:00/2026-10-09T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: IP and DNS
- ELEC 3120 / [checkpoint 2](assignments/checkpoint%202/index.md)

## week 6 tutorial 1

- datetime: 2026-10-09T15:00:00+08:00/2026-10-09T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: review of homework 1

## week 7 lecture 1

- datetime: 2026-10-12T13:30:00+08:00/2026-10-12T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: BGP

## week 7 lecture 2

- datetime: 2026-10-16T09:00:00+08:00/2026-10-16T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: midterm review
- ELEC 3120 / [homework 2](assignments/homework%202/index.md)

## week 7 tutorial 1

- datetime: 2026-10-16T15:00:00+08:00/2026-10-16T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: using network tools; ping, iperf, traceroute, and Wireshark

## week 8 lecture 1

- datetime: 2026-10-19T13:30:00+08:00/2026-10-19T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- status: public holiday: day following Chung Yeung Festival

## week 8 lecture 2

- datetime: 2026-10-23T09:00:00+08:00
- venue: \[missing\]
- status: unscheduled; midterm examination
- [§ midterm examination](#midterm%20examination)

## week 8 tutorial 1

- datetime: 2026-10-23T15:00:00+08:00/2026-10-23T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: project Q&A

## week 9 lecture 1

- datetime: 2026-10-26T13:30:00+08:00/2026-10-26T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: BGP, continued

## week 9 lecture 2

- datetime: 2026-10-30T09:00:00+08:00/2026-10-30T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: the Internet architecture

## week 9 tutorial 1

- datetime: 2026-10-30T15:00:00+08:00/2026-10-30T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: review of homework 2

## week 10 lecture 1

- datetime: 2026-11-02T13:30:00+08:00/2026-11-02T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: local area network

## week 10 lecture 2

- datetime: 2026-11-06T09:00:00+08:00/2026-11-06T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: distance vector
- ELEC 3120 / [homework 3](assignments/homework%203/index.md)

## week 10 tutorial 1

- datetime: 2026-11-06T15:00:00+08:00/2026-11-06T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: introduction to checkpoint 3

## week 11 lecture 1

- datetime: 2026-11-09T13:30:00+08:00/2026-11-09T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: link layer challenge

## week 11 lecture 2

- datetime: 2026-11-13T09:00:00+08:00/2026-11-13T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: wireless and mobile networks
- ELEC 3120 / [checkpoint 3](assignments/checkpoint%203/index.md)

## week 11 tutorial 1

- datetime: 2026-11-13T15:00:00+08:00/2026-11-13T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: review of homework 3

## week 12 lecture 1

- datetime: 2026-11-16T13:30:00+08:00/2026-11-16T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: new networks

## week 12 lecture 2

- datetime: 2026-11-20T09:00:00+08:00/2026-11-20T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: datacenter network
- ELEC 3120 / [homework 4](assignments/homework%204/index.md)

## week 12 tutorial 1

- datetime: 2026-11-20T15:00:00+08:00/2026-11-20T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: introduction to checkpoint 4

## week 13 lecture 1

- datetime: 2026-11-23T13:30:00+08:00/2026-11-23T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: network security

## week 13 lecture 2

- datetime: 2026-11-27T09:00:00+08:00/2026-11-27T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: advanced topics in networking
- ELEC 3120 / [checkpoint 4](assignments/checkpoint%204/index.md)

## week 13 tutorial 1

- datetime: 2026-11-27T15:00:00+08:00/2026-11-27T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: review of homework 4 and final review

## week 14 lecture 1

- datetime: 2026-11-30T13:30:00+08:00/2026-11-30T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: final review

## week 14 tutorial 1

- datetime: 2026-12-04T15:00:00+08:00/2026-12-04T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- status: no class

## midterm examination

- datetime: 2026-10-23T09:00:00+08:00
- venue: \[missing\]
- scope: all prior content
- format:
    - calculator: \[missing\]
    - cheatsheet: \[missing\]
    - open book: \[missing\]
    - open notes: \[missing\]
    - questions: \[missing\]
- grade: \[missing\]
- statistics: \[missing\]
- breakdown: \[missing\]
- note: tentative; the start time is fixed without a stated end time
- report: \[missing\]

## final examination

- datetime: \[missing\]
- venue: \[missing\]
- scope: \[missing\]
- format:
    - calculator: \[missing\]
    - cheatsheet: \[missing\]
    - open book: \[missing\]
    - open notes: \[missing\]
    - questions: \[missing\]
- grade: \[missing\]
- statistics: \[missing\]
- breakdown: \[missing\]
- note: falls in the December 7-19, 2026 examination period, to be announced
- report: \[missing\]
