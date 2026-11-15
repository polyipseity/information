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

ELEC 3120 is an introductory course in computer networks. It covers the performance and engineering tradeoffs behind network design and implementation, with examples drawn mainly from the Internet.

## children

- [assignments/](assignments/index.md)
- [tutorials/](tutorials/index.md)
- [CUBIC TCP](CUBIC%20TCP.md)
- [Domain Name System](Domain%20Name%20System.md)
- [Dynamic Adaptive Streaming over HTTP](Dynamic%20Adaptive%20Streaming%20over%20HTTP.md)
- [Git](Git.md)
- [HTTP](HTTP.md)
- [IP address](IP%20address.md)
- [Mathis equation](Mathis%20equation.md)
- [TCP congestion control](TCP%20congestion%20control.md)
- [TCP loss recovery](TCP%20loss%20recovery.md)
- [acknowledgement (data networks)](acknowledgement%20(data%20networks).md)
- [adaptive bitrate streaming](adaptive%20bitrate%20streaming.md)
- [agent execution loop](agent%20execution%20loop.md)
- [answering a question](answering%20a%20question.md)
- [anycast](anycast.md)
- [bandwidth (computing)](bandwidth%20(computing).md)
- [bandwidth-delay product](bandwidth-delay%20product.md)
- [buffer-based rate adaptation](buffer-based%20rate%20adaptation.md)
- [computer network](computer%20network.md)
- [congestion collapse](congestion%20collapse.md)
- [congestion control](congestion%20control.md)
- [context window](context%20window.md)
- [fair queuing](fair%20queuing.md)
- [fairness measure](fairness%20measure.md)
- [flow control (data)](flow%20control%20(data).md)
- [go-back-N ARQ](go-back-N%20ARQ.md)
- [head-of-line blocking](head-of-line%20blocking.md)
- [language model access](language%20model%20access.md)
- [max-min fairness](max-min%20fairness.md)
- [media segmentation](media%20segmentation.md)
- [`midterm examination cheatsheet.pdf`](midterm%20examination%20cheatsheet.pdf)
- [`midterm examination cheatsheet.typ`](midterm%20examination%20cheatsheet.typ)
- [network calculus](network%20calculus.md)
- [network delay](network%20delay.md)
- [packet loss](packet%20loss.md)
- [plan mode](plan%20mode.md)
- [progressive download](progressive%20download.md)
- [project instructions](project%20instructions.md)
- [prompt engineering](prompt%20engineering.md)
- [round-trip time](round-trip%20time.md)
- [selective repeat ARQ](selective%20repeat%20ARQ.md)
- [sliding window protocol](sliding%20window%20protocol.md)
- [stop-and-wait ARQ](stop-and-wait%20ARQ.md)
- [token bucket](token%20bucket.md)
- [transmission control protocol](transmission%20control%20protocol.md)
- [transmission medium](transmission%20medium.md)
- [transport layer](transport%20layer.md)
- [user datagram protocol](user%20datagram%20protocol.md)
- [vibe coding](vibe%20coding.md)
- [video bitrate](video%20bitrate.md)
- [video on demand](video%20on%20demand.md)
- [worse is better](worse%20is%20better.md)

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
    - note: the lecture states a different penalty, 10% per assignment for extra late days, and nothing accepted more than 48 hours late without a crisis
- assignment timing
    - released on a Friday and due on the Friday two weeks later, with a late deadline on the Sunday two weeks later
    - support at the instructor's Monday office hours, and from the teaching assistants at other times
- office hours: by appointment, usually Monday afternoon, Rm 2441 (<https://calendar.app.google/XTU8qeeYFiUHh3qv7>)
- questions: Ed rather than email to the instructor or the teaching assistants (<https://edstem.org/au/courses/41196/discussion>)
- submissions and feedback: Gradescope, reachable through Canvas (<https://www.gradescope.com/courses/1384476>)
- website: <https://www.foggynetwork.com>
- academic integrity
    - generative AI tools are encouraged, but nothing may be copied and pasted; submissions are checked for similarity and for generated text
    - project code must be the student's own work apart from the starter code, standard libraries, and packages named in the handout; posting it publicly and using posted code are both violations
    - the material may be discussed with others, but the submission must be the student's own, and code is written only after going over the discussion again
- accommodations: students registered with the Special Education Needs office bring their accommodations sheet to the instructor for signature, or email a copy
- written answers: state the answer, its evidence, and a warrant for each piece of evidence; see [answering a question](answering%20a%20question.md)
- sections
    - lecture: L1
        - L1: LTL, CYT Bldg; MondayT13:30:00/MondayT14:50:00, FridayT09:00:00/FridayT10:20:00
    - tutorials: T2
        - T1: Rm 5583, Lift 29-30; MondayT15:00:00/MondayT15:50:00
        - T2: Rm 2504, Lift 25-26; FridayT15:00:00/FridayT15:50:00
- note: the schedule is tentative; topics, the midterm, and assignment and project dates may change
- note: all times are Hong Kong time

## overview

- official course outline
    - congestion, flow, and error control
    - routing, addressing, and naming
    - multicasting and switching
    - internetworking
    - network security
- course parts
    - Internet basics: how the Internet works, from where data goes and where domain names come from, to loss, corruption, and differences in network speed
    - understanding the network: what makes the Internet better, from content delivery and the versions of HTTP to privacy and how network structure affects application performance
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
    - [§ bandwidth and latency](transmission%20medium.md#bandwidth%20and%20latency)
- [computer network](computer%20network.md)
    - [§ parts of a network](computer%20network.md#parts%20of%20a%20network)
    - [§ the Internet](computer%20network.md#the%20internet)
- [bandwidth (computing)](bandwidth%20(computing).md)
    - [§ units](bandwidth%20(computing).md#units)
- [network delay](network%20delay.md)
    - [§ pipe model](network%20delay.md#pipe%20model)
    - [§ transmission delay](network%20delay.md#transmission%20delay)
    - [§ propagation delay](network%20delay.md#propagation%20delay)
    - [§ packet delay](network%20delay.md#packet%20delay)
        - [§ round trip of a packet](network%20delay.md#round%20trip%20of%20a%20packet)
    - [§ throughput and latency](network%20delay.md#throughput%20and%20latency)
- [packet loss](packet%20loss.md)
    - [§ error rates](packet%20loss.md#error%20rates)
    - [§ causes of random loss](packet%20loss.md#causes%20of%20random%20loss)
- [answering a question](answering%20a%20question.md)
    - [§ answer, evidence, and warrant](answering%20a%20question.md#answer,%20evidence,%20and%20warrant)

## week 1 tutorial 1

- datetime: 2026-09-04T15:00:00+08:00/2026-09-04T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- status: unscheduled; no tutorial

## week 2 lecture 1

- datetime: 2026-09-07T13:30:00+08:00/2026-09-07T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: the Web
- [HTTP](HTTP.md)
    - [§ client-server model](HTTP.md#client-server%20model)
        - [§ state management](HTTP.md#state%20management)
    - [§ request and response messages](HTTP.md#request%20and%20response%20messages)
    - [§ persistent connections](HTTP.md#persistent%20connections)
        - [§ keep-alive in HTTP 1.0](HTTP.md#keep-alive%20in%20http%201.0)
        - [§ persistence as the default in HTTP 1.1](HTTP.md#persistence%20as%20the%20default%20in%20http%201.1)
    - [§ pipelining](HTTP.md#pipelining)
    - [§ HTTP/2](HTTP.md#http/2)
    - [§ HTTP/3](HTTP.md#http/3)
    - [§ version comparison](HTTP.md#version%20comparison)
- [head-of-line blocking](head-of-line%20blocking.md)
    - [§ application-layer HOL blocking in HTTP](head-of-line%20blocking.md#application-layer%20hol%20blocking%20in%20http)
    - [§ transport-layer HOL blocking in TCP](head-of-line%20blocking.md#transport-layer%20hol%20blocking%20in%20tcp)
    - [§ fixes across protocol generations](head-of-line%20blocking.md#fixes%20across%20protocol%20generations)

## week 2 lecture 2

- datetime: 2026-09-11T09:00:00+08:00/2026-09-11T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: the Web, continued; video streaming
- [answering a question](answering%20a%20question.md)
    - [§ explaining a plot](answering%20a%20question.md#explaining%20a%20plot)
- [video on demand](video%20on%20demand.md)
    - [§ on-demand video](video%20on%20demand.md#on-demand%20video)
    - [§ real-time video](video%20on%20demand.md#real-time%20video)
    - [§ live streaming](video%20on%20demand.md#live%20streaming)
- [progressive download](progressive%20download.md)
    - [§ client buffer](progressive%20download.md#client%20buffer)
    - [§ buffer occupancy](progressive%20download.md#buffer%20occupancy)
        - [§ bitrate against network capacity](progressive%20download.md#bitrate%20against%20network%20capacity)
    - [§ buffers against variability](progressive%20download.md#buffers%20against%20variability)
- [video bitrate](video%20bitrate.md)
    - [§ variable bitrate encoding](video%20bitrate.md#variable%20bitrate%20encoding)
- [adaptive bitrate streaming](adaptive%20bitrate%20streaming.md)
    - [§ matching quality to capacity](adaptive%20bitrate%20streaming.md#matching%20quality%20to%20capacity)

## week 2 tutorial 1

- datetime: 2026-09-11T15:00:00+08:00/2026-09-11T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: the model and the agent; the execution loop and its tools; model access
- [tutorial](tutorials/week%202%20tutorial%201/tutorial.md)
    - [§ model and agent](tutorials/week%202%20tutorial%201/tutorial.md#model%20and%20agent)
    - [§ execution loop](tutorials/week%202%20tutorial%201/tutorial.md#execution%20loop)
    - [§ tool set](tutorials/week%202%20tutorial%201/tutorial.md#tool%20set)
    - [§ model access in Hong Kong](tutorials/week%202%20tutorial%201/tutorial.md#model%20access%20in%20hong%20kong)
- [agent execution loop](agent%20execution%20loop.md)
    - [§ loop](agent%20execution%20loop.md#loop)
    - [§ core tool set](agent%20execution%20loop.md#core%20tool%20set)
- [vibe coding](vibe%20coding.md)
    - [§ git as a safety net](vibe%20coding.md#git%20as%20a%20safety%20net)
- [language model access](language%20model%20access.md)
    - [§ access routes](language%20model%20access.md#access%20routes)
    - [§ GitHub and the Student Developer Pack](language%20model%20access.md#github%20and%20the%20student%20developer%20pack)

## week 3 lecture 1

- datetime: 2026-09-14T13:30:00+08:00/2026-09-14T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: video streaming, continued
- [media segmentation](media%20segmentation.md)
    - [§ from custom protocols to HTTP](media%20segmentation.md#from%20custom%20protocols%20to%20http)
    - [§ chunking](media%20segmentation.md#chunking)
    - [§ advantages of HTTP](media%20segmentation.md#advantages%20of%20http)
- [adaptive bitrate streaming](adaptive%20bitrate%20streaming.md)
    - [§ algorithm inputs](adaptive%20bitrate%20streaming.md#algorithm%20inputs)
    - [§ algorithm output](adaptive%20bitrate%20streaming.md#algorithm%20output)
    - [§ placement in the pipeline](adaptive%20bitrate%20streaming.md#placement%20in%20the%20pipeline)
- [Dynamic Adaptive Streaming over HTTP](Dynamic%20Adaptive%20Streaming%20over%20HTTP.md)
    - [§ manifest](Dynamic%20Adaptive%20Streaming%20over%20HTTP.md#manifest)
    - [§ manifest contents](Dynamic%20Adaptive%20Streaming%20over%20HTTP.md#manifest%20contents)
    - [§ client-side selection](Dynamic%20Adaptive%20Streaming%20over%20HTTP.md#client-side%20selection)
- [buffer-based rate adaptation](buffer-based%20rate%20adaptation.md)
    - [§ one parameter](buffer-based%20rate%20adaptation.md#one%20parameter)
    - [§ rate curve](buffer-based%20rate%20adaptation.md#rate%20curve)
        - [§ reservoirs](buffer-based%20rate%20adaptation.md#reservoirs)
        - [§ discrete rates](buffer-based%20rate%20adaptation.md#discrete%20rates)
    - [§ Puffer study results](buffer-based%20rate%20adaptation.md#puffer%20study%20results)
- [worse is better](worse%20is%20better.md)
    - [§ tight integration and weak integration](worse%20is%20better.md#tight%20integration%20and%20weak%20integration)
    - [§ three reasons the simpler design won](worse%20is%20better.md#three%20reasons%20the%20simpler%20design%20won)

## week 3 lecture 2

- datetime: 2026-09-18T09:00:00+08:00/2026-09-18T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: transport model
- [transport layer](transport%20layer.md)
    - [§ limits of the network layer](transport%20layer.md#limits%20of%20the%20network%20layer)
    - [§ multiplexing and demultiplexing](transport%20layer.md#multiplexing%20and%20demultiplexing)
        - [§ ports](transport%20layer.md#ports)
    - [§ sockets](transport%20layer.md#sockets)
    - [§ service model](transport%20layer.md#service%20model)
    - [§ protocol family](transport%20layer.md#protocol%20family)
- [user datagram protocol](user%20datagram%20protocol.md)
    - [§ header](user%20datagram%20protocol.md#header)
        - [§ byte order](user%20datagram%20protocol.md#byte%20order)
        - [§ checksum](user%20datagram%20protocol.md#checksum)
    - [§ applications without recovery](user%20datagram%20protocol.md#applications%20without%20recovery)
    - [§ uses](user%20datagram%20protocol.md#uses)
- [stop-and-wait ARQ](stop-and-wait%20ARQ.md)
    - [§ sender rules](stop-and-wait%20ARQ.md#sender%20rules)
    - [§ receiver rules](stop-and-wait%20ARQ.md#receiver%20rules)
    - [§ transmission outcomes](stop-and-wait%20ARQ.md#transmission%20outcomes)
    - [§ timer choice](stop-and-wait%20ARQ.md#timer%20choice)
    - [§ sequence numbers](stop-and-wait%20ARQ.md#sequence%20numbers)
    - [§ throughput](stop-and-wait%20ARQ.md#throughput)
- [go-back-N ARQ](go-back-N%20ARQ.md)
    - [§ pipelining](go-back-N%20ARQ.md#pipelining)
    - [§ sender rules](go-back-N%20ARQ.md#sender%20rules)
    - [§ cumulative acknowledgement](go-back-N%20ARQ.md#cumulative%20acknowledgement)
    - [§ partial acknowledgement](go-back-N%20ARQ.md#partial%20acknowledgement)
    - [§ timers](go-back-N%20ARQ.md#timers)
    - [§ recovery](go-back-N%20ARQ.md#recovery)
    - [§ receiver rules](go-back-N%20ARQ.md#receiver%20rules)
- [selective repeat ARQ](selective%20repeat%20ARQ.md)
    - [§ sender rules](selective%20repeat%20ARQ.md#sender%20rules)
    - [§ partial acknowledgement](selective%20repeat%20ARQ.md#partial%20acknowledgement)
    - [§ receiver buffer](selective%20repeat%20ARQ.md#receiver%20buffer)
    - [§ sequence number space](selective%20repeat%20ARQ.md#sequence%20number%20space)
    - [§ stuck window](selective%20repeat%20ARQ.md#stuck%20window)
- [acknowledgement (data networks)](acknowledgement%20(data%20networks).md)
    - [§ basic acknowledgement](acknowledgement%20(data%20networks).md#basic%20acknowledgement)
    - [§ cumulative acknowledgement](acknowledgement%20(data%20networks).md#cumulative%20acknowledgement)
    - [§ cost of a gap](acknowledgement%20(data%20networks).md#cost%20of%20a%20gap)

## week 3 tutorial 1

- datetime: 2026-09-18T15:00:00+08:00/2026-09-18T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- status: unscheduled; no tutorial

## week 4 lecture 1

- datetime: 2026-09-21T13:30:00+08:00/2026-09-21T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: TCP basics
- [transmission control protocol](transmission%20control%20protocol.md)
    - [§ byte stream](transmission%20control%20protocol.md#byte%20stream)
    - [§ header](transmission%20control%20protocol.md#header)
        - [§ flag bits](transmission%20control%20protocol.md#flag%20bits)
        - [§ byte order](transmission%20control%20protocol.md#byte%20order)
    - [§ sequence numbers](transmission%20control%20protocol.md#sequence%20numbers)
        - [§ sequence space consumption](transmission%20control%20protocol.md#sequence%20space%20consumption)
        - [§ wraparound](transmission%20control%20protocol.md#wraparound)
        - [§ initial sequence number](transmission%20control%20protocol.md#initial%20sequence%20number)
    - [§ connection setup](transmission%20control%20protocol.md#connection%20setup)
        - [§ handshake numbers](transmission%20control%20protocol.md#handshake%20numbers)
        - [§ SYN loss](transmission%20control%20protocol.md#SYN%20loss)
    - [§ connection teardown](transmission%20control%20protocol.md#connection%20teardown)
        - [§ maximum segment lifetime](transmission%20control%20protocol.md#maximum%20segment%20lifetime)
        - [§ four segments](transmission%20control%20protocol.md#four%20segments)
        - [§ simultaneous close](transmission%20control%20protocol.md#simultaneous%20close)
        - [§ lost teardown segments](transmission%20control%20protocol.md#lost%20teardown%20segments)
        - [§ half close](transmission%20control%20protocol.md#half%20close)
        - [§ reset](transmission%20control%20protocol.md#reset)
    - [§ connection states](transmission%20control%20protocol.md#connection%20states)
        - [§ eleven states](transmission%20control%20protocol.md#eleven%20states)
        - [§ opening transitions](transmission%20control%20protocol.md#opening%20transitions)
        - [§ closing transitions](transmission%20control%20protocol.md#closing%20transitions)
        - [§ state diagram](transmission%20control%20protocol.md#state%20diagram)
        - [§ whole conversation](transmission%20control%20protocol.md#whole%20conversation)
- [round-trip time](round-trip%20time.md)
    - [§ one-way delay against round trip](round-trip%20time.md#one-way%20delay%20against%20round%20trip)
    - [§ measuring a round trip](round-trip%20time.md#measuring%20a%20round%20trip)
    - [§ smoothing](round-trip%20time.md#smoothing)
    - [§ deviation](round-trip%20time.md#deviation)
    - [§ timeout interval](round-trip%20time.md#timeout%20interval)
- [acknowledgement (data networks)](acknowledgement%20(data%20networks).md)
    - [§ selective acknowledgement](acknowledgement%20(data%20networks).md#selective%20acknowledgement)
    - [§ page fetch](acknowledgement%20(data%20networks).md#page%20fetch)
    - [§ later refinements](acknowledgement%20(data%20networks).md#later%20refinements)

## week 4 lecture 2

- datetime: 2026-09-25T09:00:00+08:00/2026-09-25T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: TCP basics, continued
- [flow control (data)](flow%20control%20(data).md)
    - [§ receive window](flow%20control%20(data).md#receive%20window)
    - [§ sending window](flow%20control%20(data).md#sending%20window)
- [bandwidth-delay product](bandwidth-delay%20product.md)
    - [§ pipe volume](bandwidth-delay%20product.md#pipe%20volume)
    - [§ window sizing](bandwidth-delay%20product.md#window%20sizing)
    - [§ round trip against one-way delay](bandwidth-delay%20product.md#round%20trip%20against%20one-way%20delay)
    - [§ congestion window](bandwidth-delay%20product.md#congestion%20window)
    - [§ ACK clocking](bandwidth-delay%20product.md#ACK%20clocking)

## week 4 tutorial 1

- datetime: 2026-09-25T15:00:00+08:00/2026-09-25T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: project history, branches, staging and commits; project instructions, plan mode, and the context window
- [tutorial](tutorials/week%204%20tutorial%201/tutorial.md)
    - [§ git](tutorials/week%204%20tutorial%201/tutorial.md#git)
    - [§ branch](tutorials/week%204%20tutorial%201/tutorial.md#branch)
    - [§ staging area](tutorials/week%204%20tutorial%201/tutorial.md#staging%20area)
    - [§ commit](tutorials/week%204%20tutorial%201/tutorial.md#commit)
    - [§ push](tutorials/week%204%20tutorial%201/tutorial.md#push)
    - [§ project instructions](tutorials/week%204%20tutorial%201/tutorial.md#project%20instructions)
    - [§ plan mode](tutorials/week%204%20tutorial%201/tutorial.md#plan%20mode)
    - [§ context window](tutorials/week%204%20tutorial%201/tutorial.md#context%20window)
    - [§ context curation](tutorials/week%204%20tutorial%201/tutorial.md#context%20curation)
    - [§ subscription region](tutorials/week%204%20tutorial%201/tutorial.md#subscription%20region)
- [Git](Git.md)
    - [§ project history](Git.md#project%20history)
    - [§ branch](Git.md#branch)
    - [§ staging area](Git.md#staging%20area)
    - [§ commit](Git.md#commit)
    - [§ push](Git.md#push)
- [project instructions](project%20instructions.md)
    - [§ instruction file](project%20instructions.md#instruction%20file)
    - [§ useful content](project%20instructions.md#useful%20content)
- [plan mode](plan%20mode.md)
    - [§ scope review](plan%20mode.md#scope%20review)
    - [§ planning threshold](plan%20mode.md#planning%20threshold)
- [context window](context%20window.md)
    - [§ capacity](context%20window.md#capacity)
    - [§ context curation](context%20window.md#context%20curation)

## week 5 lecture 1

- datetime: 2026-09-28T13:30:00+08:00/2026-09-28T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: congestion control
- [congestion control](congestion%20control.md)
    - [§ hidden capacity](congestion%20control.md#hidden%20capacity)
    - [§ costs of congestion](congestion%20control.md#costs%20of%20congestion)
    - [§ operating point](congestion%20control.md#operating%20point)
- [congestion collapse](congestion%20collapse.md)
    - [§ 1986 collapse](congestion%20collapse.md#1986%20collapse)
    - [§ repair in the end hosts](congestion%20collapse.md#repair%20in%20the%20end%20hosts)
- [network delay](network%20delay.md)
    - [§ queueing delay](network%20delay.md#queueing%20delay)

## week 5 lecture 2

- datetime: 2026-10-02T09:00:00+08:00/2026-10-02T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: congestion control, continued
- [TCP congestion control](TCP%20congestion%20control.md)
    - [§ congestion window](TCP%20congestion%20control.md#congestion%20window)
    - [§ slow start](TCP%20congestion%20control.md#slow%20start)
    - [§ congestion avoidance](TCP%20congestion%20control.md#congestion%20avoidance)
        - [§ sawtooth](TCP%20congestion%20control.md#sawtooth)
        - [§ AIMD convergence](TCP%20congestion%20control.md#aimd%20convergence)
    - [§ fast recovery](TCP%20congestion%20control.md#fast%20recovery)
    - [§ limits](TCP%20congestion%20control.md#limits)
    - [§ Reno state machine](TCP%20congestion%20control.md#reno%20state%20machine)
- [congestion control](congestion%20control.md)
    - [§ algorithm space](congestion%20control.md#algorithm%20space)
        - [§ convergence](congestion%20control.md#convergence)
    - [§ approaches](congestion%20control.md#approaches)
- [Mathis equation](Mathis%20equation.md)
    - [§ average window](Mathis%20equation.md#average%20window)
    - [§ high bandwidth problem](Mathis%20equation.md#high%20bandwidth%20problem)
- [CUBIC TCP](CUBIC%20TCP.md)
    - [§ window growth](CUBIC%20TCP.md#window%20growth)
    - [§ loss response](CUBIC%20TCP.md#loss%20response)
    - [§ long fat paths](CUBIC%20TCP.md#long%20fat%20paths)
- [fairness measure](fairness%20measure.md)
    - [§ Jain's fairness index](fairness%20measure.md#Jain's%20fairness%20index)
        - [§ expectation form](fairness%20measure.md#expectation%20form)
        - [§ variance form](fairness%20measure.md#variance%20form)
    - [§ two-flow split](fairness%20measure.md#two-flow%20split)
    - [§ limits of an index](fairness%20measure.md#limits%20of%20an%20index)
        - [§ equal demand](fairness%20measure.md#equal%20demand)
        - [§ unequal demand](fairness%20measure.md#unequal%20demand)
        - [§ low scores from two causes](fairness%20measure.md#low%20scores%20from%20two%20causes)
- ELEC 3120 / [homework 1](assignments/homework%201/index.md)
- ELEC 3120 / [checkpoint 1](assignments/checkpoint%201/index.md)

## week 5 tutorial 1

- datetime: 2026-10-02T15:00:00+08:00/2026-10-02T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- topic: prompt design for checkpoint 2; agent code review, packet capture and protocol dissection, and validation tests
- [tutorial](tutorials/week%205%20tutorial%201/tutorial.md)
    - [§ agent code review](tutorials/week%205%20tutorial%201/tutorial.md#agent%20code%20review)
    - [§ packet capture](tutorials/week%205%20tutorial%201/tutorial.md#packet%20capture)
    - [§ protocol dissector](tutorials/week%205%20tutorial%201/tutorial.md#protocol%20dissector)
    - [§ validation tests](tutorials/week%205%20tutorial%201/tutorial.md#validation%20tests)
- [prompt engineering](prompt%20engineering.md)
    - [§ specificity](prompt%20engineering.md#specificity)
    - [§ layered task prompt](prompt%20engineering.md#layered%20task%20prompt)

## week 6 lecture 1

- datetime: 2026-10-05T13:30:00+08:00/2026-10-05T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: queue management
- [max-min fairness](max-min%20fairness.md)
    - [§ mice and elephants](max-min%20fairness.md#mice%20and%20elephants)
    - [§ water filling](max-min%20fairness.md#water%20filling)
    - [§ work conservation](max-min%20fairness.md#work%20conservation)
- [fair queuing](fair%20queuing.md)
    - [§ per-flow queues](fair%20queuing.md#per-flow%20queues)
    - [§ packet sizes](fair%20queuing.md#packet%20sizes)
    - [§ virtual time](fair%20queuing.md#virtual%20time)
        - [§ virtual clock](fair%20queuing.md#virtual%20clock)
        - [§ earliest finish time](fair%20queuing.md#earliest%20finish%20time)
        - [§ comparison with CPU scheduling](fair%20queuing.md#comparison%20with%20CPU%20scheduling)
    - [§ approximation](fair%20queuing.md#approximation)
    - [§ weights](fair%20queuing.md#weights)

## week 6 lecture 2

- datetime: 2026-10-09T09:00:00+08:00/2026-10-09T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: queue management, continued
- [token bucket](token%20bucket.md)
    - [§ traffic envelope](token%20bucket.md#traffic%20envelope)
    - [§ burst size](token%20bucket.md#burst%20size)
    - [§ deployment](token%20bucket.md#deployment)
- [network calculus](network%20calculus.md)
    - [§ arrival curve](network%20calculus.md#arrival%20curve)
    - [§ service curve](network%20calculus.md#service%20curve)
    - [§ reading the gap](network%20calculus.md#reading%20the%20gap)
    - [§ worked bound](network%20calculus.md#worked%20bound)
- ELEC 3120 / [checkpoint 2](assignments/checkpoint%202/index.md)

## week 6 tutorial 1

- datetime: 2026-10-09T15:00:00+08:00/2026-10-09T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- status: unscheduled; no tutorial

## week 7 lecture 1

- datetime: 2026-10-12T13:30:00+08:00/2026-10-12T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: internet protocol
- [computer network](computer%20network.md)
    - [§ interconnection challenges](computer%20network.md#interconnection%20challenges)
- [IP address](IP%20address.md)
    - [§ IPv4](IP%20address.md#IPv4)
    - [§ masks](IP%20address.md#masks)
    - [§ IPv6](IP%20address.md#IPv6)
    - [§ obtaining an address](IP%20address.md#obtaining%20an%20address)

## week 7 lecture 2

- datetime: 2026-10-16T09:00:00+08:00/2026-10-16T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: domain name system
- [Domain Name System](Domain%20Name%20System.md)
    - [§ names instead of numbers](Domain%20Name%20System.md#names%20instead%20of%20numbers)
    - [§ hierarchical namespace](Domain%20Name%20System.md#hierarchical%20namespace)
        - [§ top-level domains](Domain%20Name%20System.md#top-level%20domains)
    - [§ zones](Domain%20Name%20System.md#zones)
        - [§ zone cuts and delegation](Domain%20Name%20System.md#zone%20cuts%20and%20delegation)
        - [§ root servers](Domain%20Name%20System.md#root%20servers)
    - [§ resolution](Domain%20Name%20System.md#resolution)
        - [§ caching](Domain%20Name%20System.md#caching)
    - [§ resource records](Domain%20Name%20System.md#resource%20records)
        - [§ record types](Domain%20Name%20System.md#record%20types)
        - [§ zone file syntax](Domain%20Name%20System.md#zone%20file%20syntax)
        - [§ delegation in the parent zone](Domain%20Name%20System.md#delegation%20in%20the%20parent%20zone)
    - [§ message format](Domain%20Name%20System.md#message%20format)
    - [§ indirection](Domain%20Name%20System.md#indirection)
- [anycast](anycast.md)
    - [§ mechanism](anycast.md#mechanism)
    - [§ root servers](anycast.md#root%20servers)
    - [§ trade-offs](anycast.md#trade-offs)
- ELEC 3120 / [homework 2](assignments/homework%202/index.md)

## week 7 tutorial 1

- datetime: 2026-10-16T15:00:00+08:00/2026-10-16T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- status: unscheduled; no tutorial

## week 8 lecture 1

- datetime: 2026-10-19T13:30:00+08:00/2026-10-19T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- status: public holiday: day following Chung Yeung Festival

<!-- check: ignore-next-line[session_next_lecture_remark]: verbatim midterm announcement; a major grading event is the rule's stated exception -->
## week 8 lecture 2

- datetime: 2026-10-23T09:00:00+08:00/2026-10-23T10:20:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- status: unscheduled; midterm examination
- [§ midterm examination](#midterm%20examination)

---

> __Midterm is coming!!!__
>
> Hi folks,
>
> Ta-da! The exciting midterm will come next Friday! Here are some logistics about the midterm.
>
> - The midterm will be held next Friday (23 Oct) from 9 am to 10:20 am.
> - The midterm will cover the contents for lectures 1-9 (application + trasnport).
> - The location is __LTL__! The lecture room we have every week. You must make sure the seat on either side of you is vacant.
> - You can bring one sheet of A4 paper as a cheat sheet. You can write/print on both sides.
> - You can bring a calculator to the test if you want.
>
> __Midterm review lecture:__ Last Friday, I distributed some copies of practice questions. I cannot upload it to Canvas, neither should you distribute it in any format. So please come to the lecture and pick up your copy. But remember, homework and slides are the best materials for the midterm. If you didn't pick it up, come to my office next Thursday.
>
> __Special office hours:__ Next week we will have a special office hours at 2-4pm, Thursday, at Room 2441. You are always welcome to shoot me an email to schedule another time, or post questions on Ed.
>
> Good luck! Please spread the word and make sure everyone come.
>
> \[redacted\]

## week 8 tutorial 1

- datetime: 2026-10-23T15:00:00+08:00/2026-10-23T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- status: unscheduled; no tutorial

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
- status: unscheduled; no tutorial

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
- status: unscheduled; no tutorial

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
- status: unscheduled; no tutorial

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
- status: unscheduled; no tutorial

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
- status: unscheduled; no tutorial

## week 14 lecture 1

- datetime: 2026-11-30T13:30:00+08:00/2026-11-30T14:50:00+08:00, PT1H20M
- venue: LTL, CYT Bldg
- topic: final review

## week 14 tutorial 1

- datetime: 2026-12-04T15:00:00+08:00/2026-12-04T15:50:00+08:00, PT50M
- venue: Rm 2504, Lift 25-26
- status: unscheduled; no tutorial

## midterm examination

- datetime: 2026-10-23T09:00:00+08:00/2026-10-23T10:20:00+08:00
- venue: LTL, CYT Bldg
- scope: lectures 1 to 9, application and transport
- format:
    - calculator: yes
    - cheatsheet: yes (one A4 sheet, both sides, written or printed)
        - [`midterm examination cheatsheet.pdf`](midterm%20examination%20cheatsheet.pdf)
        - [`midterm examination cheatsheet.typ`](midterm%20examination%20cheatsheet.typ)
    - open book: no
    - open notes: no
    - questions: 10 to 15 multiple choice questions and 3 to 5 long questions
- grade: \[missing\]
- statistics: \[missing\]
- breakdown: \[missing\]
- note: one seat on each side of the student stays vacant
- note: the review lecture on 2026-10-16 handed out practice questions on paper; they are not published to Canvas, and redistributing them is not allowed
- note: special office hours before the examination: 2026-10-22T14:00:00+08:00/2026-10-22T16:00:00+08:00, Rm 2441
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
