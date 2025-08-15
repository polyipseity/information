---
aliases:
  - 'A System View of Communications: from Signals to Packets'
  - 'A System View of Communications: from Signals to Packets index'
  - ELEC 1200
  - ELEC 1200 index
  - ELEC1200
  - ELEC1200 index
  - HKUST ELEC 1200
  - HKUST ELEC 1200 index
  - HKUST ELEC1200
  - HKUST ELEC1200 index
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1200
  - function/index
  - language/in/English
---

# index

- HKUST ELEC 1200
- name: A System View of Communications: from Signals to Packets

The content is in teaching order.

- grading
  - scheme
    - lab ×8: 0.25
      - lab checkpoint ×8: 0.1
      - post-lab quiz ×8: 0.15
        - A 5-minute individual quiz after each lab.
    - homework ×3: 0.1
    - midterm examination: 0.25
      - datetime: 2025-07-29T11:00:00+08:00/2025-07-29T11:50:00+08:00, PT50M
    - final examination: 0.4
      - datetime: 2025-08-08T10:00:00+08:00/2025-08-08T11:30:00+08:00, PT1H30M

## children

- [assignments](assignments/index.md)
- [questions](questions/index.md)

## week 1 lecture

- datetime: 2025-07-14T14:00:00+08:00/2025-07-14T16:50:00+08:00, PT2H50M
- topic: course introduction; signals; real world channels
- [ELEC 1200](index.md)
  - ELEC 1200 / motivation ::@:: to provide an overview of technologies for communication <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
  - ELEC 1200 / questions ::@:: How to build smart cities? How to convey information with signals, even with noise? How to detect and recover transmission errors? How to relay information over networks across the world? <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
  - ELEC 1200 / features ::@:: broad perspective \(cover all aspects of communication\), fundamental \(no prerequisite knowledge\), hands on \(e.g. labs\) <!--SR:!2025-08-21,15,290!2025-08-20,14,290-->
  - ELEC 1200 / logistics
  - ELEC 1200 / course intended learning outcomes \(CILOs\)
  - ELEC 1200 / parts ::@:: point-to-point communication \(one link\), channel sharing \(one link, many users\), network \(many links, many users\) <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
- [communications system](../../../../general/communications%20system.md) ::@:: It is a collection of individual telecommunications networks systems, relay stations, tributary stations, and terminal equipment usually capable of interconnection and interoperation to form an integrated whole. <!--SR:!2025-08-22,16,290!2025-08-21,14,290-->
  - communications system / basic ::@:: transmitter: source → compress → error correcting coding → bits to waveforms <br/> channel: + noise <br/> receiver: waveforms to bits → error correction → decompress → destination <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - communications system / ideal ::@:: Ideally, the received bits are always the same as the sent bits. But real world noise makes this impossible. <!--SR:!2025-08-20,14,290!2025-08-20,14,290-->
  - communications system / transmitter \(Tx\) ::@:: It converts a sequence of bits into a physical signal or waveform to be carried over a channel. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
  - communications system / channel ::@:: It carries a physical signal or waveform. It may be subject to noise due to various factors. <p> examples: air, copper wires, fiber optic cables <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
  - communications system / receiver \(Rx\) ::@:: It receives a physical signal or waveform and tries to convert it back into the original sequence of bits. <!--SR:!2025-08-22,15,290!2025-08-22,16,290-->
- [bit](../../../../general/bit.md) ::@:: It is the most basic unit of information in computing and digital communication. It represents a logical state with one of two possible values. <!--SR:!2025-08-21,15,290!2025-08-22,16,290-->
  - bit / notation ::@:: These values are most commonly represented as either "1" or "0", but other representations such as _true_/_false_, _yes_/_no_, _on_/_off_, or _+_/_−_ are also widely used. <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
  - bit / representation ::@:: It can be represented as two distinct states of a physical variable, e.g. current, light, voltage, etc. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
    - bit / representation / ease ::@:: There are only two states, so it is easy to use electronics to manipulate them, e.g. logic gates, orientation of tiny magnets to store bits, etc. <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
  - bit / sequence ::@:: It is a sequence of bits. Physically, they can be represented by holding the corresponding state of the physical variable for a fixed amount of time, called _bit time_, for each bit in the bit sequence. <p> The shorter the bit time, the faster we can transmit information. <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
- ELEC 1200
  - ELEC 1200 / cutting-edge technologies ::@:: 6G, artificial intelligence, big data, internet of things, etc. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
- bit
  - bit / sequence
    - bit / sequence / codeword ::@:: A single bit can only represent variables with two possible values. A combination of _n_ bits, called a _codeword_, can represent variables up to 2<sup>_n_</sup> possible values. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
- [binary number](../../../../general/binary%20number.md) ::@:: a method for representing numbers that uses only two symbols for the natural numbers: typically "0" \(zero\) and "1" \(one\) <!--SR:!2025-08-22,15,290!2025-08-22,15,290-->
  - binary number / to decimal number ::@:: $$x = \sum_{k = 0}^{N - 1} 2^k \cdot b_k \,,$$ where $b_{N - 1} b_{N - 2} \cdots b_1 b_0$ is the bit sequence. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
  - binary number / most significant bit \(MSB\) ::@:: The bit that represents $2^{N - 1}$. It may be the first bit \(big endian; usually the case when written\), and sometimes it is reversed \(little endian\). <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - binary number / least significant bit \(LSB\) ::@:: The bit that represents $2^0 = 1$. It may be the last bit \(big endian; usually the case when written\), and sometimes it is reversed \(little endian\). <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
- [ASCII](../../../../general/ASCII.md) ::@:: It is a character encoding standard for electronic communication, used by most computers today. <p> It is a 7-bit code, so there are 128 code points. Each unsigned integer maps to a character. But most of time we use an unsigned byte, which has 8 bits, to represent a character with the MSB set to 0. <p> \(__this course__: Treat it as a 8-bit code.\) <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
  - ASCII / full name ::@:: American Standard Code for Information Interchange <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
- bit
  - bit / sequence
    - bit / sequence / endianness ::@:: As mentioned above, a binary number can be represented by a sequence of bits. _Big endian_ means the MSB is transmitted first. _Little endian_ means the LSB is transmitted first. <!--SR:!2025-08-21,14,290!2025-08-22,16,290-->
    - bit / sequence / codewords ::@:: To represent a sequence of codeword, often the bits for each codeword is transmitted contagiously and sequentially in the same order as the original sequence of codeword. \(The ordering of codeword is independent from bit endianness.\) <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
- communications system
  - communications system / transmitter
  - communications system / channel
  - communications system / receiver
- [bit rate](../../../../general/bit%20rate.md) ::@:: It is the number of bits that are conveyed or processed per unit of time. <!--SR:!2025-08-20,14,290!2025-08-22,16,290-->
  - bit rate / importance ::@:: It is one of the most important _performance_ measure for a communications system. <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
  - bit rate / units ::@:: It is measured in bits per second \(bps\). Not to be confused with bytes per second \(Bps\)! <p> Metric prefixes may be added, e.g. 1000&nbsp;bps = 1&nbsp;kbps, 1000&nbsp;kbps = 1&nbsp;Mbps, 1000&nbsp;Mbps = 1&nbsp;Gbps, etc. <!--SR:!2025-08-20,14,290!2025-08-22,16,290-->
  - bit rate / bit time ::@:: bit rate = 1/\(bit time\) <p> So shorter bit times increases bit rate. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
- [byte](../../../../general/byte.md) ::@:: It is a unit of digital information that most commonly consists of eight bits. <!--SR:!2025-08-20,14,290!2025-08-21,15,290-->
- [signal](../../../../general/signal.md) ::@:: It is both the process and the result of transmission of data over some media accomplished by embedding some variation. <!--SR:!2025-08-22,16,290!2025-08-21,14,290-->
  - signal / classification ::@:: time: continuous time \(CT\), discrete time \(DT\) <br/> value: continuous valued \(analog\), discrete valued \(digital\) <!--SR:!2025-08-20,14,290!2025-08-22,15,290-->
- [discrete time and continuous time](../../../../general/discrete%20time%20and%20continuous%20time.md) ::@:: They are two alternative frameworks within which variables that evolve over time are modeled. <!--SR:!2025-08-22,16,290!2025-08-21,14,290-->
  - discrete time and continuous time / discrete time ::@:: It views values of variables as occurring at distinct, separate "points in time" <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - discrete time and continuous time / continuous time ::@:: It views variables as having a particular value only for an infinitesimally short amount of time. <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
- signal
  - signal / discrete time \(DT\) ::@:: The signal has a known value at discrete set of time points. <p> Transmitters and receivers often operate in DT for ease of \(digital\) processing. <!--SR:!2025-08-20,14,290!2025-08-21,14,290-->
  - signal / continuous time \(CT\) ::@:: The signal has a known value at all time points. <p> Channels often operate in CT, as channels are often physical. <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
- [sampling](../../../../general/sampling%20(signal%20processing).md) ::@:: It is the reduction of a continuous-time signal to a discrete-time signal. A common example is the conversion of a sound wave to a sequence of "samples". <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
  - sampling / receiver ::@:: Receiver in a communications system often sample the CT signal from the channel to obtain a DT signal for ease of processing. <!--SR:!2025-08-22,16,290!2025-08-22,15,290-->
  - sampling / sampling period and frequency ::@:: Sampling period $T_s$ is the time between each sample, often in seconds \(s\). Sampling frequency $F_s$ is the number of samples per unit of time, often in hertz \(Hz; samples per second\). They are reciprocals of each other: <p> sampling period = 1/\(sampling frequency\) <!--SR:!2025-08-21,15,290!2025-08-21,15,290-->
  - sampling / notation ::@:: CT signal: $x(t)$ <br/> DT signal: $x[n] = x(n T_s)$ \(__this course__: $x(n)$ instead of $x[n]$ is used.\) <br/> sampling frequency: $F_s$ <br/> sampling period: $T_s$ <!--SR:!2025-08-23,16,290!2025-08-21,14,290-->
  - sampling / number of samples ::@:: It is the total number of samples of a signal over a finite time window $T_w$. It can be calculated from the sampling period or frequency. <!--SR:!2025-08-22,16,290!2025-08-22,15,290-->
  - sampling / tradeoff ::@:: Higher sampling frequency decreases information loss from the original CT signal after conversion, but increases storage to store the DT signal. \(There are many other tradeoffs not mentioned here.\) <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
  - sampling / transmitters ::@:: Receivers often perform sampling. Transmitters often perform the "reverse" operation: convert a DT signal to CT signal. <p> This is often done by a hold circuit. For $x[n]$ in DT, its value is held between $x(n T_s)$ and $x((n + 1) T_s)$ in CT, where $T_s$ is the hold period \(of similar nature to sampling period\). <!--SR:!2025-08-22,15,290!2025-08-21,14,290-->
- bit
  - bit / sampling ::@:: A bit can be represented by a fixed number of samples in a DT signal, called _samples per bit_ \(SPB\). <!--SR:!2025-08-20,14,290!2025-08-22,16,290-->
    - bit / sampling / metrics ::@:: Using SPB, we can convert between metrics in terms of bits and those in terms of samples. <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
- [metric prefix](../../../../general/metric%20prefix.md) ::@:: It is a unit prefix that precedes a basic unit of measure to indicate a multiple or submultiple of the unit. All metric prefixes used today are decadic. Each prefix has a unique symbol that is prepended to any unit symbol. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
  - metric prefix / common prefixes ::@:: \(in increasing order of magnitude, each separated by 3 OoMs\) femto-/f ← pico-/p ← nano-/n ← micro-/μ ← milli-/m ← \(unit\) → kilo/k → mega/M → giga/G → tera/T → peta/P <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
- [waveform](../../../../general/waveform.md) ::@:: It of a signal is the shape of its graph as a function of time, independent of its time and magnitude scales and of any displacement in time. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - waveform / representations ::@:: sequence of values, sum of unit step functions, graph, verbal description <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
    - waveform / representations / verbal description ::@:: for communication between people <!--SR:!2025-08-22,16,290!2025-08-21,15,290-->
    - waveform / representations / graph ::@:: for waveform visualization <!--SR:!2025-08-20,14,290!2025-08-21,15,290-->
    - waveform / representations / sequence of values ::@:: for computers, e.g. MATLAB, Python, etc. <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
    - waveform / representations / sum of unit step functions ::@:: for mathematical analysis of signals when they pass through a channel <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
- [Heaviside step function](../../../../general/Heaviside%20step%20function.md) ::@:: It is a step function named after Oliver Heaviside, the value of which is zero for negative arguments and one for positive arguments. Different conventions concerning the value _H_\(0\) are in use. \(__this course__: _H_\(0\)&nbsp;=&nbsp;1\) <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - Heaviside step function / this course ::@:: \(__this course__: Use $$u(n) = \begin{cases} 0 & n < 0 \\ 1 & 0 \le n \,, \end{cases}$$ i.e. the function is 1 at time 0.\) <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
  - Heaviside step function / delay ::@:: To delay the step function by _d_ samples, use $u(n - d)$. \(Works for negative _d_ as well, which advances the function.\) <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
  - Heaviside step function / signal ::@:: It can be used to represent a binary signal, which can only take two values 0 and 1. <!--SR:!2025-08-21,15,290!2025-08-21,15,290-->
    - Heaviside step function / signal / construction ::@:: Assume the signal is 0 initially. Every time the signal changes from 0 to 1 at sample _d_, add $u(n - d)$. Every time the signal changes from 1 to 0 at sample _d_, subtract $u(n - d)$. <p> Note this means the step function must be added and subtracted alternatively in order for the signal to be binary \(either 0 or 1\). <!--SR:!2025-08-21,15,290!2025-08-21,14,290-->
- communications system
  - communications system / transmitter
  - communications system / channel
  - communications system / receiver
  - communications system / channel
    - communications system / channel / discrete time ::@:: Almost all channels are continuous time due to their physical nature. <p> However, assuming both the transmitter and receiver work in discrete time, we can treat the CT channel and conversions between CT and DT as a _black box_. Then the CT channel is simplified to be a DT channel. <!--SR:!2025-08-22,15,290!2025-08-21,15,290-->
- [mathematical model](../../../../general/mathematical%20model.md) ::@:: It is an abstract description of a concrete system using mathematical concepts and language. <!--SR:!2025-08-22,16,290!2025-08-22,15,290-->
  - mathematical model / signal ::@:: A mathematical model can be used to model the effect of a channel on the transmitted signal. <!--SR:!2025-08-21,14,290!2025-08-20,14,290-->
  - mathematical model / goodness ::@:: A good model should be accurate, i.e. its prediction is close to actual observations. It should also be simple. <!--SR:!2025-08-20,14,290!2025-08-20,14,290-->
  - mathematical model / motivation ::@:: It allows us to understand a system, predict its performance, and improve its performance. <!--SR:!2025-08-21,15,290!2025-08-21,15,290-->
- [communication channel](../../../../general/communication%20channel.md) ::@:: It refers either to a physical transmission medium such as a wire, or to a logical connection over a multiplexed medium such as a radio channel in telecommunications and computer networking. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
  - communication channel / effects ::@:: 5 primary effects \(that we will learn now\): attenuation \(decrease in amplitude\), blurring \(of transition\), delay, noise, offset <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
  = communication channel / attenuation, delay, offset ::@:: A very simple model to model attenuation, delay, and offset: $$y[n] = k \cdot x[n - d] + c \,,$$ where $k$ is amplitude scaling \(&lt; 1 for attenuation\), $d$ is delay, and $c$ is offset \(output signal when input signal is 0\). <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
  - communication channel / blurring ::@:: A bit sequence converted into a waveform requires instantaneous changes when the bit changes. However, physical limitations in electronics, mediums, sensors, transducers, etc., often the received waveform has this instantaneous change blurred. We say such a channel is _bandlimited_. <!--SR:!2025-08-21,15,290!2025-08-21,14,290-->
    - communication channel / blurring / graph ::@:: Graph the transmitted signal against a blurred received signal. We see when the transmitted signal changes _instantaneously_ due to a bit change, the received signal also changes but _gradually_, only approaching the desired signal after several samples. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
    - communication channel / blurring / samples per bit ::@:: Assuming only samples per bit \(SPB\) changes, i.e. the channel remains unchanged. Then we see the blurring effect remains the same in its transition speed. If the SPB is too low, then the received signal may not approach the desired signal enough before the bit changes again. <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
  - communication channel / modeling ::@:: The model mentioned above only handles attenuation, delay, and offset. How can we handle blurring? <p> If we assume the channel is _linear_ and _time-invariant_, making it a _linear time-invariant system_, then we can also model blurring with a _step response function_. This makes use that any input can be expressed as the sum of unit step functions. <p> \(__this course__: We will only talk about very simple step response functions.\) <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->

## week 1 tutorial

- datetime: 2025-07-15T11:00:00+08:00/2025-07-15T12:20:00+08:00, PT1H20M
- topic: lab logistics; lab 1, MATLAB
- ELEC 1200
  - ELEC 1200 / logistics
    - ELEC 1200 / logistics / labs ::@:: 4 checkpoints \(group of 2\) → post-lab quiz \(individual; 4 questions in 5 minutes; no backtracking\) → leave immediately <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
  - ELEC 1200 / lab 1 ::@:: Have fun with MATLAB!! <!--SR:!2025-08-20,14,290!2025-08-21,15,290-->
- [MATLAB](../../../../general/MATLAB.md) ::@:: It is a proprietary multi-paradigm programming language and numeric computing environment developed by MathWorks. MATLAB allows matrix manipulations, plotting of functions and data, implementation of algorithms, creation of user interfaces, and interfacing with programs written in other languages. <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
  - MATLAB / libraries ::@:: You must either add folders paths manually using the user interface, or use the `addpath(paths...)` function, so that files directly under those folders \(not recursive\) are considered by MATLAB when running our scripts. <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
  - MATLAB / variable names ::@:: Only digits, letters, and underscores `_` are allowed. Must start with a letter. Case sensitive. <!--SR:!2025-08-22,16,290!2025-08-21,15,290-->
  - MATLAB / statements ::@:: A newline or semicolon `;` separates each statement. Using only a newline \(no semicolon `;`\) displays the result of that statement each time it is run. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
  - MATLAB / vectors ::@:: `[x1 x2 ... xn]`, where `xi` are numbers or vectors. The result is that the numbers and vectors are concatenated together. You may use commas `,` to separate the `xi` without change in meaning. <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
  - MATLAB / matrices ::@:: You may use semicolons `;` to separate the `xi`, but then the elements on different sides of semicolons `;` are separated into different rows. This can be used to create matrices. Note the number of elements in all rows must be the same. <!--SR:!2025-08-21,15,290!2025-08-22,16,290-->
  - MATLAB / indexing ::@:: MATLAB uses 1-based indexing, i.e. the 1st element is indexed by 1. <p> `x(n)` gets the _n_-th element. `x(a:b)` gets the _a_-th element to the _b_-th element as a vector, both ends inclusive. If _a_ &gt; _b_, then the vector is empty. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - MATLAB / ranges ::@:: `a:b` is a range expression giving a vector from _a_ to _b_, both ends inclusive. If _a_ &gt; _b_, then the vector is empty. <p> `a:s:b` is also a range expression giving a vector from _a_ to _b_, both ends inclusive, with the 1st element being _a_ and adding _s_ each time to get the next element, until the element is outside _a_ and _b_ \(both ends inclusive\), then that and subsequent elements are not added. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
  - MATLAB / arithmetic operations ::@:: MATLAB supports many arithmetic operations, e.g. addition `+`, subtraction `-`, multiplication `*`, division `/`, etc. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
    - MATLAB / arithmetic operations / scalar ::@:: A scalar \(non-vector and non-matrix\) operated on other scalars produce the expected results. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
    - MATLAB / arithmetic operations / vector, matrix ::@:: A scalar \(non-vector and non-matrix\) operated on a vector or matrix cause each element of the vector or matrix to be operated with that scalar. <p> For element-wise operations, a vector or matrix must be operated on a vector or matrix of the same shape. If so, you should generally prepend a dot `.` to the arithmetic operators, e.g. <!-- `.+`, `.-`, -->`.*`, `./`, which ensures the operations performed are element-wise \(rather than some very weird advanced mathematical operations\). <!--SR:!2025-08-21,14,290!2025-08-22,15,290-->
    - MATLAB / arithmetic operations / division ::@:: Division involving two floats return a float. Otherwise, it returns the nearest integer. <!--SR:!2025-08-23,16,290!2025-08-21,14,290-->
  - MATLAB / plotting ::@:: MATLAB provides function to plot data and accompanying text. <!--SR:!2025-08-22,15,290!2025-08-22,15,290-->
    - MATLAB / plotting / data ::@:: `plot(x, y)`, `stem(x, y)` <p> By default, each plot creates a new diagram in a new figure. Run `hold on` after the first plot so that any new plots are drawn on the same last diagram of the last figure. Run `hold off` to restore the default behavior. <!--SR:!2025-08-21,15,290!2025-08-20,14,290-->
    - MATLAB / plotting / text ::@:: `xlabel(str)`, `ylabel(str)` <!--SR:!2025-08-21,15,290!2025-08-22,16,290-->
    - MATLAB / plotting / layout ::@:: By default, MATLAB draws one diagram per figure. Use `tiledlayout(m, n)` to draw a _m_-by-_n_ grid \(_m_ is number of rows and _n_ is number of columns\) in a new figure. Each grid cell contain one diagram. To use the next grid cell, run `nexttile`, then plot the data. \(For the first cell, run `nexttile` first before plotting.\) <!--SR:!2025-08-22,16,290!2025-08-22,16,290-->
  - MATLAB / iteration ::@:: start with `for var = vector`, end with `end` <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
  - MATLAB / conditionals ::@:: start with `if condition`, then optionally add multiple `elseif condition`, then optionally add one `else`, and end with `end` <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
  - MATLAB / debugging ::@:: There are buttons to do the following for debugging your code: add breakpoints, run to a specific line of code, show output, etc. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
  - MATLAB / functions ::@:: You can add functions, which accepts inputs and return outputs. Variables created are local to the function and do not leak out. <p> You can put functions in the same place as your code \(a script\), or you can put them in a separate file \(a function file\). The filename of a script must not be the name of any function inside, while that of a function file must be the name of the first function inside. <p> Before R2024a, script functions must be placed at the end. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - MATLAB / help ::@:: help button, `doc(function_name)`, `help(function_name)` <!--SR:!2025-08-21,14,290!2025-08-21,15,290-->
- [§ week 1 lab 2](#week%201%20lab%202)

## week 1 lab

- datetime: 2025-07-15T14:00:00+08:00/2025-07-15T16:50:00+08:00, PT2H50M
- status: unscheduled

## week 1 lecture 2

- datetime: 2025-07-16T14:00:00+08:00/2025-07-16T15:50:00+08:00, PT1H50M
- topic: linear time invariant systems, transmitting data
- [linear time-invariant system](../../../../general/linear%20time-invariant%20system.md) \(LTI system\) ::@:: It is a system that produces an output signal from any input signal subject to the constraints of linearity and time-invariance; these terms are briefly defined in the overview below. <!--SR:!2025-08-22,15,290!2025-08-22,16,290-->
  - linear time-invariant system / system ::@:: \(__this course__: We consider a specific context. It is something that takes a waveform and produces a waveform, e.g. channels, etc.\) <!--SR:!2025-08-22,15,290!2025-08-20,14,290-->
  - linear time-invariant system / linearity ::@:: The relationship between the input and the output is a linear mapping. That is, the output for the sum of any two inputs is the sum of their two respective outputs: $$x(t) = x_1(t) + x_2(t) \implies y(t) = y_1(t) + y_2(t) \,.$$ This can be repeated applied to get the output for the sum of any number of inputs. <!--SR:!2025-08-20,14,290!2025-08-21,15,290-->
    - linear time-invariant system / linearity / homogeneity ::@:: The above property is also called _additivity_. _Homogeneity_ is related to additivity, where the two functions are the same: $$x'(t) = c \cdot x(t) \implies y'(t) = c \cdot y(t) \,,$$ for some constant $c$. When $c$ is an integer, it is a special case of additivity. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
  - linear time-invariant system / time-invariant ::@:: It means that whether we apply an input to the system now or _T_ seconds from now, the output will be identical except for a time delay of _T_ seconds: $$x'(t) = x(t - T) \implies y'(t) = y(t - T) \,.$$ <!--SR:!2025-08-22,16,290!2025-08-22,15,290-->
- [step response](../../../../general/step%20response.md) ::@:: It of a system in a given initial state consists of the time evolution of its outputs when its control inputs are Heaviside step functions. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
  - step response / notation ::@:: \(__this course__: Use $s(n)$.\) <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
  - step response / LTI system ::@:: For LTI systems, the step response $s(n)$ can be used to find the output for any input. <p> Write the input as a sum of \(potentially scaled and/or delayed\) unit step functions. Then replace $u$ with $s$, i.e. replace $c \cdot u(n - d)$ with $c \cdot s(n - d)$. This makes use of the properties of LTI system. <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
  - step response / exponential ::@:: It can model amplitude scaling \(_k_ &lt; 1 for attenuation\), blurring \(_a_ &lt; 1\), and propagation delay \(_d_\): $$s(n) = k\left(1 - a^{n - d + 1}\right) u(n - d) \,.$$ <p> _k_ simply scales the resulting amplitude. _d_ simply delays \(for negative values, advances\) the response. _a_ &lt; 1 models the transition speed, with values closer to 1 slowing down the transition. <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
    - step response / exponential / _a_ ::@:: When _n_ = _d_ \(when the transition starts\), we see $$s(d) = k \left(1 - a^{d - d + 1}\right) u(d - d) = k (1 - a) \,.$$ So _theoretically_, $1 - a$ should be the amplitude of the output signal relative to the full amplitude when the transition starts. <p> In practice, noise makes this impractical to find _a_, as even small errors in _a_ can lead to drastic changes in the step response. Trial-and-error is needed. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - step response / noise, offset ::@:: The step response does _not_ model noise and offset. <p> For offset, we _ignore_ it when the step response is considered. Later, we can simply linearly add it to the output signal. <p> For noise, probability will be needed and introduced later, but it is also linearly added to the signal. <!--SR:!2025-08-19,12,270!2025-08-21,15,290-->
- communication channel
  - communication channel / noise, offset ::@:: They are often introduced by the environment, e.g. other users, etc. <!--SR:!2025-08-22,16,290!2025-08-21,15,290-->
- [communication protocol](../../../../general/communication%20protocol.md) ::@:: It is a system of rules that allows two or more entities of a communications system to transmit information via any variation of a physical quantity. <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
  - communication protocol / importance ::@:: Using the same protocol for both the transmitter and the receiver allows the receiver to understand the transmitted data properly. <!--SR:!2025-08-22,15,290!2025-08-22,16,290-->
  - communication protocol / aspects ::@:: all aspects needed to communicate <p> examples: bit endianness \(LSB or MSB\), bit representation \(e.g. 0 is off and 1 is on\), bit time \(or SPB\), synchronization method, text encoding \(e.g. ASCII, Unicode\), training sequence <!--SR:!2025-08-21,15,290!2025-08-21,15,290-->
- bit
  - bit / decoding ::@:: To decode a bit, we need to make use of sub-sampling, thresholding, and training sequence. <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
    - bit / decoding / offset ::@:: Normally, when we graph the output sign for _decoding_, the _offset_ is removed first so that zero signal corresponds to bit 0. \(__this course__: used in [midterm examination](#midterm%20examination)\) <p> Remember to adjust the threshold for this removal of offset. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - bit / decoding / thresholding ::@:: Assume the transmitted data is binary. Then a threshold is decided, for which the data is 1 if the signal is greater than or _equal to_ the threshold, and otherwise 0. <p> A good threshold is $c + k / 2$, where _c_ is the offset and _k_ is the amplitude. <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
    - bit / decoding / sub-sampling ::@:: A bit is sent using SPB number of samples. This technique means we only consider a subset of the samples for each bit. <p> Due to blurring of transition, we often use the last sample of a bit to ensure the output is far above or below the threshold. <!--SR:!2025-08-21,15,290!2025-08-22,16,290-->
    - bit / decoding / training sequence ::@:: The receiver needs to know _c_ and _k_, but these two parameters may change over time. <p> This sequence allows the receiver to estimate _c_ and _k_. It is known to both the transmitter and receiver in advance, and cannot carry data. <p> A simple training sequence is simply sending the bit 1 for some time, and then send the bit 0 for some time. <!--SR:!2025-08-22,16,290!2025-08-21,15,290-->
      - bit / decoding / training sequence / estimation ::@:: _c_ and _k_ is estimated from the training sequence. A good choice is to set _c_ as the minimum of the step response, and _k_ as the difference between the minimum and maximum. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
      - bit / decoding / training sequence / pulse width ::@:: It is the time or number of samples the bit 1 is sent in our simple training sequence. <p> Shorter pulse width means more time to transmit data, as less time is used on the training sequence. Longer pulse width means better _c_ and _k_ estimation. The pulse width is set based on _a_ of the \(assumed\) exponential step response so that the output signal is very close the actual maximum before the pulse stops. \(_a_ closer to 1 means the pulse width should be longer.\) <!--SR:!2025-08-22,16,290!2025-08-20,14,290-->
        - bit / decoding / training sequence / pulse width / calculation ::@:: Assuming the output signal is $$y(n) = c + k\left(1 - a^{n + 1}\right) \,.$$ \(Offset the signal so that delay $d$ is not needed.\) Then we solve for $n$ such that $$y(n) > c + b k \implies 1 - a^{n + 1} > b \,,$$ where $b$ is the desired amplitude relative to full amplitude \(often 0.9\). \(__this course__: The lecture slides say $n + 1$ is the pulse width...\) <!--SR:!2025-08-22,16,290!2025-08-22,15,290-->
- [asynchronous communication](../../../../general/asynchornous%20communication.md) ::@:: It is transmission of data, generally without the use of an external clock signal, where data can be transmitted intermittently rather than in a steady stream. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
  - asynchronous communication / motivation ::@:: If the data is transmitted in a steady stream, we just need to keep the clock of both the transmitter and receiver synchronous. <p> But what if it is not? Then we simply also transmit signals used for timing, e.g. framing, etc. <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
- [frame](../../../../general/frame%20(networking).md) ::@:: It is a digital data transmission unit in computer networking and telecommunications. <!--SR:!2025-08-22,16,290!2025-08-22,15,290-->
  - frame / features ::@:: A frame typically includes frame synchronization features consisting of a sequence of bits or symbols that indicate to the receiver the beginning \(__this course__: _start bits_\) and end \(__this course__: _stop bits_\) of the payload data within the stream of symbols or bits it receives. <p> Note that a frame includes the start and stop bits apart from the data bits. <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
  - frame / start bits ::@:: The start bit\(s\) is chosen to be either 0 or 1 such that the output signal should be different from the output idle channel; otherwise there is no way to distinguish the start of a frame from idleness. Typically, the bit is 1 because the idle channel usually represents 0. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - frame / data block ::@:: The number of bits in a data block should in the protocol, agreed in advanced by the transmitter and receiver. <p> example: RS-232 used in PCs usually uses 8 data bits <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
    - frame / data block / padding, splitting ::@:: The number of bits to transmit may not be a multiple of the number of data bits in a data block. This can be fixed by padding \(add 0s to the end\) and splitting \(split the bits into multiple data blocks inside multiple data frames\). <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
  - frame / stop bits ::@:: To detect a start bit after the end of a frame, we add stop bits, which is the same as the idle channel; otherwise we cannot distinguish the start bit of the next frame from the stop bits. <!--SR:!2025-08-20,14,290!2025-08-21,15,290-->
    - frame / stop bits / tradeoff ::@:: More stop bits means more time to process a data block in a frame before receiving the next frame. It reduces the data transmission rate because more bits are used on the stop bits. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
- ELEC 1200
  - ELEC 1200 / protocol ::@:: We can consider the protocol to be used in our lab from the transmitter and receiver perspective separately. <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
    - ELEC 1200 / protocol / transmitter ::@:: training sequence <br/> frames: 1 start bit, 1280 \(160 bytes\) of data bits, 1 stop bit <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
    - ELEC 1200 / protocol / receiver ::@:: training sequence: find _c_ and _k_ <br/> sub-sampling: SPB−1, i.e. the last sample of a bit <br/> frame: skip 1 start bit, read 1280 bits as data <!--SR:!2025-08-21,14,290!2025-08-20,14,290-->

## week 1 tutorial 2

- datetime: 2025-07-17T11:00:00+08:00/2025-07-17T12:20:00+08:00, PT1H20M
- topic: lab 2, characterizing and modeling a channel
- ELEC 1200
  - ELEC 1200 / equipment ::@:: An IR board with both a transmitter and receiver in a cardboard box. A paper ruler \(seriously...\) so that you can measure and control the distance between the board and the box. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - ELEC 1200 / lab 2 ::@:: study the channel → text to bit sequence → bit sequence to waveform → model the channel: attenuation _k_, blurring _a_, delay _d_, offset _c_ → change transmission distance, remodel the channel <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
- [mean squared error](../../../../general/mean%20squared%20error.md) \(MSE\) ::@:: It, of an estimator \(of a procedure for estimating an unobserved quantity\) measures the _average of the squares of the errors_—that is, the average squared difference between the estimated values and the actual value. <p> \(__this course__: For simplicity, we use the formula where the denominator is $n$, not $n - 1$.\) <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
- [§ week 1 lab 3](#week%201%20lab%203)

## week 1 lab 2

- datetime: 2025-07-17T14:00:00+08:00/2025-07-17T16:50:00+08:00, PT2H50M
- topic: introduction to MATLAB
- status: attendance
- [§ week 1 tutorial](#week%201%20tutorial)
- ELEC 1200
  - ELEC 1200 / lab 1
    - ELEC 1200 / lab 1 / Boolean to numeric conversion ::@:: A comparison returns 1 if it is true, 0 otherwise. <!--SR:!2025-08-23,16,290!2025-08-21,14,290-->
- assignment: [lab 1](assignments/lab%201/index.md)
- questions: [post lab quiz 1 derivative](questions/post%20lab%20quiz%201%20derivative.md)

## week 1 lab 3

- datetime: 2025-07-18T10:00:00+08:00/2025-07-18T12:50:00+08:00, PT2H50M
- topic: characterizing and modeling a channel
- status: attendance
- [§ week 1 tutorial 2](#week%201%20tutorial%202)
- ELEC 1200
  - ELEC 1200 / lab 2
    - ELEC 1200 / lab 2 / transmission distance, attenuation _k_ ::@:: Attenuation _k_ of a channel decreases as transmission distance increases. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
    - ELEC 1200 / lab 2 / channel parameters from graph ::@:: Assume there is a training sequence. Offset _c_ is the lowest signal level. Attenuation _k_ is the difference between the lowest and highest signal level. _a_ needs to be found via trial-and-error, with increasing _a_ means slower channel response. <!--SR:!2025-08-22,16,290!2025-08-21,14,290-->
- assignment: [lab 2](assignments/lab%202/index.md)
- questions: [post lab quiz 2 derivative](questions/post%20lab%20quiz%202%20derivative.md)

## week 1 lecture 3

- datetime: 2025-07-18T14:00:00+08:00/2025-07-18T15:50:00+08:00, PT1H50M
- topic: inter-symbol interference, eye diagram; feedback model of the channel
- bit rate
- [bit error rate](../../../../general/bit%20error%20rate.md) \(BER\) ::@:: The __bit error rate__ \(__BER__\) is the number of bit errors per unit time. The __bit error ratio__ \(also __BER__\) is the number of bit errors divided by the total number of transferred bits during a studied time interval. Bit error ratio is a unitless performance measure, often expressed as a percentage. <p> \(__this course__: __Important__. We use the _bit error ratio_, but we call it _bit error rate_. Funny, isn't it?\) <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - bit error rate / objective ::@:: This should be \(reasonably\) low. This is done by setting a maximum limit on the average BER. <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
  - bit error rate / tradeoff ::@:: In general, BER increases as bit time decreases \(i.e. bit rate increases\). Usually, starting from the lowest possible bit time, BER is high, and decreases slowly at first, then decreases quickly, then decreases slowly again as it approaches zero, and then becomes \(practically\) zero. <p> More noise or less powerful signal \(less power for transmission\) also increases BER. <!--SR:!2025-08-22,15,290!2025-08-22,16,290-->
- linear time-invariant system
- step response
  - step response / LTI system
- [intersymbol interference](../../../../general/intersymbol%20interference.md) \(ISI\) ::@:: It is a form of distortion of a signal in which one symbol \(__this course__: one bit\) interferes with subsequent symbols \(__this course__: subsequent bits\). This is an unwanted phenomenon as the previous symbols have a similar effect as noise, thus making the communication less reliable. <!--SR:!2025-08-21,15,290!2025-08-20,14,290-->
  - intersymbol interference / bandlimited channels ::@:: As the channel is bandlimited, the output signal requires time to transit when the input bits changes in a bit sequence. <p> Bit errors occur when not enough time is given for this transition to cross the threshold before the next bit \(transmission\) is transmitted. <p> In framing, if bit errors occur at the start bits \(e.g. 1 received as 0\), then _synchronization errors_ occur, which may result in a frame being offsetted by several or many samples, or not received at all. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
    - intersymbol interference / bandlimited channels / bit time ::@:: Shorter bit time means more past past symbols _interfere_ with the current symbol, leading to a larger variety of output responses when a bit is transmitted. <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
- [settling time](../../../../general/settling%20time.md) ::@:: It of a dynamical system such as an amplifier or other output device is the time elapsed from the application of an ideal instantaneous step input to the time at which the amplifier output has entered and remained within a specified error band. <!--SR:!2025-08-22,15,290!2025-08-21,15,290-->
  - settling time / this course ::@:: \(__this course__: Assume the transmitted bit changes from 0 to 1. It is the time or number of samples it takes for the response to get 90% of the way to the maximum amplitude. It can be calculated as: $$n_s = \frac {\ln 0.1} {\ln a} - 1 \,,$$ where _a_ is the parameter in exponential step response, and sample 0 is the first sample of a bit.\) <!--SR:!2025-08-21,15,290!2025-08-22,16,290-->
- intersymbol interference
  - intersymbol interference / response variety ::@:: Assuming only the bit time \(or SPB\) is changed, i.e. the channel remains unchanged. The the number of bits for the output signal remains the same. However, more previous bits may interfere with the current bit as each bit takes less sample. So the response variety increases, which depends on the starting sample position. <p> By symmetry, the response variety for transitions from 1 to 0 should be similar to transitions from 0 to 1. <!--SR:!2025-08-23,16,290!2025-08-21,14,290-->
  - intersymbol interference / solution ::@:: Either make the channel respond faster \(increase bandwidth\) or increase bit time \(or SPB\). <p> The former may require control over the channel and incur extra cost. The latter reduces bit rate. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
- [eye diagram](../../../../general/eye%20pattern.md) ::@:: It is an oscilloscope display in which a digital signal from a receiver is repetitively sampled and applied to the vertical input \(_y-axis_\), while the data rate is used to trigger the horizontal sweep \(_x-axis_\). <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
  - eye diagram / name ::@:: It is so called because, for several types of coding, the pattern looks like a series of eyes between a pair of rails. <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
  - eye diagram / use ::@:: It can summarize the effect of intersymbol interference by showing all responses to bit 0 and 1 _simultaneously_. <p> \(__this course__: Overlay plots of 2\*SPB+1 samples \(both ends inclusive\), each of distance 2\*SPB samples.\) <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
  - eye diagram / measurements ::@:: eye \(the empty space in the middle, if any\): eye height, eye width <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
  - eye diagram / bit time ::@:: As bit time \(or SPB\) decreases, both the eye height and width decreases \(the eye begins to "closes"\), until it "closes" completely. <p> Shorter eye width means the exact sample to sub-sample a bit becomes more important. No eye means there is no sample to sub-sample to avoid any bit errors, i.e. BER cannot be zero. <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
- ELEC 1200
  - ELEC 1200 / protocol
- bit rate
- bit error rate
- intersymbol interference
- eye diagram
- [equalization](../../../../general/equalization%20(communications).md) ::@:: It is the reversal of distortion incurred by a signal transmitted through a channel. <p> It will cause the eye in the eye diagram to "open". <!--SR:!2025-08-21,15,290!2025-08-22,15,290-->
  - equalization / derivation ::@:: To derivate the formula to equalize the output signal, we need to model the output signal from the input signal, which usually gives a formula. Then, we invert the model to model the input signal from the output signal, which usually involves manipulating the original formula. <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
    - equalization / derivation / problem ::@:: Given a step response, it is hard to derive the reverse formula for equalization. <p> Either advanced mathematical techniques \(__this course__: not taught in this course\) are needed, or we can use an equivalent but _recursive_ model, which is amendable to elementary algebraic manipulation. <!--SR:!2025-08-22,16,290!2025-08-22,16,290-->
- mathematical model
  - mathematical model / equivalent models ::@:: There may be many equivalent models. That is, they make the same prediction for the same inputs. <p> The different equivalent models are useful in different situations. <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
  - mathematical model / recursive model ::@:: \(__this course__: A recursive model defines the $n$-th output sample in terms of \(one\) past samples. It also requires an initial starting sample at any $n$\) <!--SR:!2025-08-23,16,290!2025-08-21,14,290-->
- step response
  - step response / exponential
    - step response / exponential / recursive ::@:: An recursive but equivalent way to express the exponential step response: $$y(n) = a \cdot y(n - 1) + (1 - a) \cdot k \cdot x(n) \,,$$ where _k_ is the amplitude scaling and _a_ still has the same meaning as the original step response. An initial starting condition at any $n$ is also needed, e.g. $y(0) = c$ \($n$ does not need to be 0\). <p> The corresponding system implementing this model is known as a _feedback system_. <!--SR:!2025-08-22,16,290!2025-08-21,15,290-->
      - step response / exponential / recursive / interpretation ::@:: The above formula takes the weighted average of the last output sample and the scaled current input sample. <p> $a$ controls the weights, with $a = 0$ means the channel has no memory \(uses the scaled current input sample\) while $a = 1$ means the channel has infinite memory \(constant output and ignores input\). <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
    - step response / exponential / equivalency ::@:: To prove the step response is equivalent to and the recursive model, we prove the latter model is linear time-invariant \(additivity, homogeneity, time invariance\), and has the same step response. <p> The latter \(same step response\) can be proved by, given the same input samples, calculate the output samples for both models and observe that they are equal for all samples. A rigorous proof uses induction. \(__this course__: The rigorous proof is optional.\) <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->

## week 2 lecture

- datetime: 2025-07-21T14:00:00+08:00/2025-07-21T16:50:00+08:00, PT2H50M
- topic: channel equalization; noise
- equalization
  - equalization / derivation
- step response
  - step response / exponential
    - step response / exponential / recursive
- equalization
  - equalization / exponential step response ::@:: Using the recursive model: $$y(n) + a \cdot y(n - 1) + (1 - a) \cdot k \cdot x(n) \,,$$ we can algebraically manipulate it to become: $$x(n) = \frac 1 k \frac 1 {1 - a} (y(n) - a \cdot y(n - 1)) \,.$$ And we can reverse the above algebraic manipulation as well. <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
    - equalization / exponential step response / interpretation ::@:: The equalizer is $$\begin{aligned} x(n) & = \frac 1 k \frac 1 {1 - a} (y(n) - a \cdot y(n - 1)) \\ & = \frac 1 k \frac 1 {1 - a} ((1 - a) \cdot y(n) + a y(n) - a \cdot y(n - 1)) \\ & = \frac 1 k \left(y(n) + \frac a {1 - a} (y(n) - y(n - 1)) \right) \,. \end{aligned}$$ We observe the $\frac 1 k$ outside simply undo the scaling. We also observe that the equalizer "boost" the transition by adding the change in output multiplied by $\frac a {1 - a}$, which is 0 when $a = 0$ \(no memory thus instantaneous response, so no need to "boost"\) and infinite when $a = 1$ \(infinite memory thus constant output, so need infinite "boost" \(but this will not work mathematically\)\). <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
    - equalization / exponential step response / parameters ::@:: Ideally, _k_ and _a_ should be the same as that as the channel. However, in practice, this needs to be estimated. <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
      - equalization / exponential step response / parameters / errors ::@:: Usually, _k_ can be estimated accurately. So we only consider estimation errors in _a_. <p> If equalization _a_ is larger than that of the channel, the equalizer is too aggressive and overshooting occurs. If equalization _a_ is smaller than that of the channel, the equalizer is too passive and it takes longer than optimal to respond to changes in the input signal. Otherwise, optimal result is obtained. <!--SR:!2025-08-20,14,290!2025-08-22,15,290-->
- eye diagram
  - eye diagram / equalization ::@:: Generally, after equalization, the eye usually opens \(sometimes even if the eye does not appear for the original eye diagram\). <p> Below, we split the effects of equalization on the eye diagram into with no noise and with noise. <!--SR:!2025-08-21,15,290!2025-08-20,14,290-->
    - eye diagram / equalization / no noise ::@:: With no noise and correct equalization _a_, we see the eye diagram is almost optimal \(instantaneous switching\). The eye is almost optimal. <p> If equalization _a_ is too high \(higher than that of the channel\), then overshooting occurs. Values beyond the normal output range is seen when the bit changes. <p> If equalization _a_ is too low, then it takes longer than optimal to respond to changes in the input signal. The eye in the eye diagram is not open as wide and high as it could be. <!--SR:!2025-08-21,15,290!2025-08-21,15,290-->
    - eye diagram / equalization / noise ::@:: With noise, most things are the same for no noise. However, the eye borders are much thicker, which reduces the eye height rather than increase it. <p> The eye borders are also very spiky. This is because the equalizer amplifies noise, as noise also causes changes in the output signal too! Errors in equalization _a_ would further magnify this noise. <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
- equalization
  - equalization / exponential step response
    - equalization / exponential step response / robustness ::@:: We see even if the equalization _a_ is not the same as the channel _a_, equalization still works, just not as optimal. This shows equalization is _robust_. <!--SR:!2025-08-21,14,290!2025-08-20,14,290-->
- communication channel
  - communication channel / noise
- [noise](../../../../general/noise%20(signal%20processing).md) ::@:: It is a general term for unwanted (and, in general, unknown) modifications that a signal may suffer during capture, storage, transmission, processing, or conversion. <!--SR:!2025-08-20,14,290!2025-08-21,15,290-->
  - noise / importance ::@:: It is very important in communications system. It is everywhere. Often, it looks like very random zig zag lines on a graph, a _random signal_. <p> If there were no noise, data transmission would only need very very little power, since no matter how weak the signal is, it can be distinguished and then amplified. Then we would make the signal strength as small as possible to save energy. <p> With noise, the signal-to-noise ratio becomes important, because a high enough value is needed to distinguish signal from noise. This determines a _minimum signal strength_ for decoding. <!--SR:!2025-08-21,14,290!2025-08-21,14,290-->
  - noise / sources ::@:: It is everywhere. It occurs naturally in nature. The most often source is _thermal noise_, e.g. atmosphere, devices, resistors, etc., as thermal noise disturbs electrons causing random voltages and emissions. <!--SR:!2025-08-22,16,290!2025-08-20,14,290-->
  - noise / statistics ::@:: While noise looks quite random for a few samples, we can collect statistics for a large number of samples. <p> We can create a _histogram_, plotting a percentage of sample around a sample value \(_y_-axis\) for each sample value \(_x_-axis\). <!--SR:!2025-08-21,15,290!2025-08-20,14,290-->
    - noise / statistics / probability density function ::@:: We can create a _histogram_, plotting a percentage of sample around a sample value \(_y_-axis\) for each sample value \(_x_-axis\). <p> By collecting more samples \(and making the histogram bars narrower\), it gets increasingly smooth. By also dividing the original histogram height by its original histogram width and let it be the new histogram height, this function approaches a _probability density function_ \(pdf\) $f_X(x)$. \(__this course__: The slides are missing "dividing the histogram height" to normalize the heights.\) <!--SR:!2025-08-22,16,290!2025-08-21,15,290-->
- [probability density function](../../../../general/probability%20density%20function.md) \(PDF, pdf\) ::@:: It of an _absolutely continuous_ random variable is a function whose value at any given sample \(or point\) in the sample space \(the set of possible values taken by the random variable\) can be interpreted as providing a _relative likelihood_ that the value of the random variable would be equal to that sample. <p> Probability density is the probability per unit length, in other words, the _absolute likelihood_ for a continuous random variable to take on any particular value is 0 since there is an infinite set of possible values to begin with. <p> It is commonly denoted $f_X(x)$ for an absolutely continuous random variable _X_. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - probability density function / properties ::@:: It is always nonnegative \(__this course__: the slide uses "positive"\). The total area under the function is 1. <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
  - probability density function / probability ::@:: The probability that a sample lies in between $x_1$ \(exclusive\) and $x_2$ \(inclusive\) \(__this course__: the slide uses exclusive for both\) is the area under the function between $x_1$ and $x_2$. <p> In general, integration is required to find this area. \(__this course__: Our PDF consists of only simple shapes for which their areas have formulas.\) <!--SR:!2025-08-21,14,290!2025-08-22,15,290-->
- noise
  - noise / additive ::@:: There are many ways noise can modify the output signal. The simplest way is that the noise is added to the quiet output signal, thus the noise is _additive_, also called _additive noise_. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
  - noise / effect ::@:: If the noise is large enough, the noisy output signal can fall on the wrong side of the threshold, so the bit is read wrongly. <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
- bit error rate
  - bit error rate / analysis ::@:: The BER can be calculated theoretically from a model of the channel. The model can be very complicated. \(__this course__: We consider a simple model.\) <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
    - bit error rate / simple model ::@:: The model simplifies the transmitter and receiver model even further. Now we only consider the input bits at the transmitter and the output bits at the receiver, and everything else in between is a black box called the _binary channel_. <!--SR:!2025-08-22,16,290!2025-08-22,15,290-->
      - bit error rate / simple model / assumptions ::@:: The simple model assumes additive white Gaussian noise \(AWGN\), no ISI, perfect synchronization \(i.e. the start bit cannot be read wrongly\), single sample sub-sampling \(one sample to decode one bit\). <p> The AWGN requirement can be relaxed easily. Others are harder. <p> The assumptions are important so that each bit only considers one sample and its error probability are independent of other bits \(no ISI\). <!--SR:!2025-08-22,15,290!2025-08-21,14,290-->
      - bit error rate / simple model / binary channel ::@:: Ideally, the input bit always equal the output bit. Whenever they are not equal, a _bit error_ occurs. <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
      - bit error rate / simple model / probability ::@:: The BER is: $$\begin{aligned} \text{BER} & = P(I = 0) P(O = 1 \mid I = 0) + P(I = 1) P(O = 0 \mid I = 1) \\ & = P(I = 0, O = 1) + P(I = 1, O = 0) \,, \end{aligned}$$ where $P(I = x)$ is the probability of the input bit being $x$, $P(I = x, O = y)$ is the probability of the input bit being $x$ and the output bit being $y$, and $P(O = y \mid I = x)$ is the _conditional_ probability of the output bit being $y$ given the input bit is $x$. <p> Since the bit is either 0 or 1, $P(I = 1)$ can be replaced with $1 - P(I = 0)$, and vice versa. $P(O = 1 \mid I = x)$ can be replaced with $1 - P(O = 0 \mid I = x)$ for fixed $x$, and vice versa. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
      - bit error rate / simple model / this course ::@:: \(__this course__: We use simpler notations: $$\text{BER} = P_e = P[\text{IN} = 0] \cdot P_{e0} + P[\text{IN} = 1] \cdot P_{e1} \,,$$ where the meanings can be inferred from above.\) <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
      - bit error rate / simple model / error types ::@:: We see there are two types of errors: input bit is 0 but output bit is 1; and input bit is 1 but input bit is 0. <!--SR:!2025-08-21,14,290!2025-08-22,16,290-->
  - bit error rate / computation ::@:: We can compute the BER theoretically or empirically. <p> To calculate the BER empirically, simply observe a channel for some time, find the number of errors, and either divide by time for the rate or number of transmitted bits for the ratio. \(__this course__: __Important__. Remember "bit error rate" in this course is actually the _bit error ratio_.\) <!--SR:!2025-08-22,16,290!2025-08-21,15,290-->
  - bit error rate / simple model
    - bit error rate / simple model / factors ::@:: To find BER for this simple model, we need to know the input bit probabilities and the conditional error probabilities. <p> Often, the input bit probabilities are assumed equal. <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
  - bit error rate / factors ::@:: The input bit probabilities are controlled by the transmitter and data to be transmitted. The conditional error probabilities depends on noise level, threshold, transmit levels, etc. <!--SR:!2025-08-20,14,290!2025-08-21,15,290-->
- [power](../../../../general/power%20(physics).md) ::@:: It is the amount of energy transferred or converted per unit time. In the International System of Units, the unit of power is the watt, equal to one joule per second. Power is a scalar quantity. <!--SR:!2025-08-21,15,290!2025-08-21,14,290-->
  - power / energy, time ::@:: power = energy / time <!--SR:!2025-08-22,16,290!2025-08-22,15,290-->
  - power / usable time ::@:: usable time = energy / power consumption <!--SR:!2025-08-22,16,290!2025-08-20,14,290-->
  - power / batteries ::@:: They contain a fixed amount of energy. Often, it has a fixed voltage in volts \(V\) and a charge capacity in milliamp-ours \(mAh\). Multiply these two together to get its energy in millwatt-hours \(mWh\). <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
- [normal distribution](../../../../general/normal%20distribution.md) ::@:: It is important in statistics and is often used in the natural and social sciences to represent real-valued random variables whose distributions are not known. Their importance is partly due to the central limit theorem. It is denoted $\mathcal N(\mu, \sigma^2)$, where $\mu \in \mathbb R$ is the mean and $\sigma^2 \in \mathbb R_{> 0}$ is the variance. <p> \(When you see $\mathcal N(0, 100)$, do not mistake the 100 as the standard deviation!\) <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - normal distribution / applications ::@:: Brownian motion, transmission noise, voltage across a resistor, etc. <!--SR:!2025-08-21,15,290!2025-08-20,14,290-->
  - normal distribution / mean ::@:: Its average value over many samples. It is the central location of its PDF. <p> Changing it simply shifts the PDF. <!--SR:!2025-08-20,14,290!2025-08-21,14,290-->
  - normal distribution / standard deviation ::@:: A measure of how "spread out" the samples are. It measures how wide the PDF is. <p> It is the square root of variance. <p> Increasing it widens the PDF, and also flattens it so that the area under the PDF remains 1. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - normal distribution / variance ::@:: Also a measure of how "spread out" the samples are. It also measures how wide the PDF is. <p> It is the square of standard deviation. <p> In signal processing, assuming mean of the noise is 0, it is also average power of the noise. <p> Increasing it widens the PDF, and also flattens it so that the area under the PDF remains 1. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->

## week 2 tutorial

- datetime: 2025-07-22T11:00:00+08:00/2025-07-22T12:20:00+08:00, PT1H20M
- topic: lab 2 review, lab 3, communication protocol, bit error rate
- ELEC 1200
  - ELEC 1200 / lab 2
  - ELEC 1200 / lab 3 ::@:: framing: split and pad, start bit, stop bit → find threshold from a graph → waveform to bit sequence → evaluate bit error rate against bit time <!--SR:!2025-08-22,16,290!2025-08-21,14,290-->
- [§ week 2 lab](#week%201%20lab)

## week 2 lab

- datetime: 2025-07-22T14:00:00+08:00/2025-07-22T16:50:00+08:00, PT2H50M
- topic: communication protocol, bit error rate \(BER\)
- status: attendance
- [§ week 3 tutorial](#week%203%20tutorial)
- ELEC 1200
  - ELEC 1200 / lab 3
    - ELEC 1200 / lab 3 / threshold ::@:: Assume there is a training sequence. A good threshold is the average of the lowest and highest signal level. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
    - ELEC 1200 / lab 3 / bit time, bit error rate ::@:: In general, bit error rate decreases as bit time increases. <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
    - ELEC 1200 / lab 3 / training sequence ::@:: The training sequence should be longer \(higher pulse width\) if the channel response is slower \(_a_ is higher\). <!--SR:!2025-08-21,15,290!2025-08-21,15,290-->
- assignment: [lab 3](assignments/lab%203/index.md)
- questions: [post lab quiz 3 derivative](questions/post%20lab%20quiz%203%20derivative.md)

## week 2 lecture 2

- datetime: 2025-07-23T14:00:00+08:00/2025-07-23T15:50:00+08:00, PT1H50M
- topic: noise; error correcting codes
- normal distribution
- [Q-function](../../../../general/Q-function.md) ::@:: It is the tail distribution function of the standard normal distribution. In other words, $Q(x)$ is the probability that a normal \(Gaussian\) random variable will obtain a value larger than $x$ standard deviations. Equivalently, $Q(x)$ is the probability that a standard normal random variable takes a value larger than $x$. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
  - Q-function / probability ::@:: $$Q(x) := P[X > x] \implies P[X \le x] = 1 - Q(x) \,,$$ where $X$ follows a standard normal distribution, i.e. with mean 0 and standard deviation 1. <p> For a normal distribution $Y$ with mean $\mu_Y$ and standard deviation $\sigma_Y$ \(variance $\sigma_Y^2$\), we compute $$P[Y > y] = Q\left(\frac {y - \mu_Y} {\sigma_Y} \right) \implies P[Y \le y] = 1 - Q\left(\frac {y - \mu_Y} {\sigma_Y} \right) \,.$$ <!--SR:!2025-08-20,14,290!2025-08-22,15,290-->
  - Q-function / computation ::@:: There is no closed-form expression for it. A table of values or computers must be used. <p> In MATLAB, use the `qfunc(x)` function. <!--SR:!2025-08-22,16,290!2025-08-20,14,290-->
- bit error rate
  - bit error rate / simple model
    - bit error rate / simple model / error probabilities ::@:: The input probabilities are easy to find. The conditional error probabilities are slightly harder to find. Further assume bit 0 sends $r_{\text{min} }$ and bit 1 sends $r_{\text{max} }$ \(offset $r_{\text{min} }$ and scale $r_{\text{max} } - r_{\text{min} }$\). <p> Then, given the additive noise PDF $X$, the PDF for sending bit 0 is simply to offset the PDF by $r_{\text{min} }$, i.e. $r_{\text{min} } + X$. The conditional error rate $P_{e0}$ is the area of the PDF that crosses into the wrong side of the threshold. The same goes the conditional error rate $P_{e1}$ for sending bit 1. <!--SR:!2025-08-21,14,290!2025-08-21,15,290-->
    - bit error rate / simple model / threshold ::@:: We see by increasing the threshold, the conditional error rate decreases for sending bit 0 but increases for sending bit 1, and vice versa. So there is a tradeoff. <p> There is a point in between \(not necessarily in the middle\) that minimizes the bit error rate, with BER increasing as we move away from it. This point can be found using the first derivative test. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
    - bit error rate / simple model / special case ::@:: IF the input bits are equally likely, and the additive noise follows a normal distribution, then the optimal threshold is in the middle: $$T^* = \frac {r_{\text{min} } + r_{\text{max} } } 2 \,,$$ and its optimal BER is $$\text{BER}^* = Q\left(\frac {r_{\text{max} } - r_{\text{min} } } {2 \sigma} \right) \,.$$ <p> We see a larger signal difference means less BER. However, this means a higher transmission power is needed. <!--SR:!2025-08-21,14,290!2025-08-21,14,290-->
- power
  - power / signal ::@:: The power of a signal is its amplitude squared. If the signal takes on value $r$ with probability $p$, we can weight the amplitude squared: $$\text{power} = \sum_k p_k r_k^2 \,.$$ <p> For a quiet output signal with both bits equally likely, we have: $$\begin{aligned} \text{power} & = \frac 1 2 r_{\text{min} }^2 + \frac 1 2 r_{\text{max} }^2 \\ & = \left(\frac 1 4 r_{\text{min} }^2 + \frac 1 2 r_{\text{min} } r_{\text{max} } + \frac 1 4 r_{\text{max} }^2 \right) + \left(\frac 1 4 r_{\text{min} }^2 - \frac 1 2 r_{\text{min} } r_{\text{max} } + \frac 1 4 r_{\text{max} }^2 \right) \\ & = \left(\frac {r_{\text{min} } + r_{\text{max} } } 2 \right)^2 + \left(\frac {r_{\text{min} } - r_{\text{max} } } 2 \right)^2 \,, \end{aligned}$$ the last expression of which is _bias—variance decomposition_, because the first term is squared bias while the latter is variance \(squared standard deviation\). <!--SR:!2025-08-21,15,290!2025-08-21,14,290-->
    - power / signal / rigorous ::@:: \(__this course__: untaught\) <p> We can use the expected value to rigorously express the power of a signal: $$\text{power} = \operatorname E\left[X^2 \right] \,,$$ where $X$ is the signal modeled as a random signal. <p> The _bias—variance decomposition_ is simply the following well-known identity: $$\operatorname E\left[X^2\right] = \operatorname E[X]^2 + \operatorname E\left[(X - \mu_X)^2 \right] = \operatorname E[X]^2 + \operatorname{Var}(X) = \mu_X^2 + \sigma_X^2 \,.$$ <p> This also explains why the power of an unbiased \(mean is 0\) noise signal is simply its variance. <!--SR:!2025-08-22,16,290!2025-08-22,15,290-->
- [signal-to-noise ratio](../../../../general/signal-to-noise%20ratio.md) \(SNR, S/N\) ::@:: It is a measure used in science and engineering that compares the level of a desired signal to the level of background noise. SNR is defined as the ratio of signal power to noise power, often expressed in decibels. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
  - signal-to-noise ratio / formula ::@:: $$\text{SNR} = \frac {\text{signal (without noise) power} } {\text{noise power} } \,.$$ However, it is often expressed in decibels \(dB\) instead: $$\text{SNR}_{\text{dB} } = 10 \log_{10} \text{SNR} \,.$$ 0 dB means same the signal has the same power as noise. Every 10&nbsp;dB increase in SNR multiplies the signal power by 10, so that 10&nbsp;dB means 10 times, 20&nbsp;dB means 100 times, 30&nbsp;dB means 1000 times, etc. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
  - signal-to-noise ratio / factors ::@:: Mostly due to transmission distance. As transmission distance increases, the signal power at the receiver decreases and the noise power remains mostly constant. <p> Other factors include electronics quality, bit \(symbol\) rate, etc. <!--SR:!2025-08-22,16,290!2025-08-21,15,290-->
  - signal-to-noise ratio / typical values ::@:: A typical receiver requires a SNR of at least around 10&nbsp;dB to function. For a mobile phone, the minimum signal level is around 10<sup>−14</sup>&nbsp;W because the typical noise power is around 10<sup>−15</sup>&nbsp;W, which does not sound like a lot. <!--SR:!2025-08-22,15,290!2025-08-21,14,290-->
  - signal-to-noise ratio / bit error rate ::@:: For typical modulation schemes, increase in SNR decreases BER. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
- [error correction code](../../../../general/error%20correction%20code.md) \(ECC\) ::@:: The sender encodes the message in a redundant way, most often by using \(_this_\). <p> It is used as part a technique called _channel coding_ used for controlling errors in data transmission over unreliable or noisy communication channels. <!--SR:!2025-08-20,14,290!2025-08-20,14,290-->
  - error correction code / motivation ::@:: Our protocol, including equalization, allows us to receive transmitted bits correctly for small errors. <p> But for large errors, we still receive the bits incorrectly, and we may not even know the bits are wrong! ECC can help detect errors \(e.g. error bursts of bounded length\) and possibly recover the data \(or if unrecoverable, tell the transmitter to retransmit the data\). <!--SR:!2025-08-20,14,290!2025-08-21,15,290-->
- [noisy-channel coding theorem](../../../../general/noisy-channel%20coding%20theorem.md) ::@:: It establishes that for any given degree of noise contamination of a communication channel, it is possible \(in theory\) to communicate discrete data \(digital information\) nearly error-free up to a computable maximum rate through the channel. <!--SR:!2025-08-20,14,290!2025-08-20,14,290-->
  - noisy-channel coding theorem / details ::@:: A noisy channel has a channel capacity _C_ determined by its noise \(which is determined by physical properties of the channel\). It is the _theoretical_ maximum rate in which useful information can be transmitted _almost_ error-free. Exceeding this channel capacity _R_ &gt; _C_, there is a minimum error rate that increases as _R_ increases further away from _C_. <p> However, the above does not tell us how to construct a code to achieve almost-error-free transmission. <!--SR:!2025-08-22,15,290!2025-08-22,16,290-->
  - noisy-channel coding theorem / history ::@:: This result was presented by Claude Shannon in 1948 and was based in part on earlier work and ideas of Harry Nyquist and Ralph Hartley. <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
- [block code](../../../../general/block%20code.md) ::@:: They are a large and important family of error-correcting codes that encode data in blocks. <p> It can also refer to any error-correcting code that acts on a block of $k$ bits of input data to produce $n$ bits of output data $(n,k)$. Consequently, the block coder is a _memoryless_ device. <!--SR:!2025-08-21,14,290!2025-08-21,15,290-->
  - block code / codeword ::@:: Previously, we have only considered codeword that simply contains the data bits. <p> Now using block code $(n, k)$, the codeword consists of $k$ _message bits_ and $n - k$ _extra bits_, so that each codeword is $n$ bits. The extra bits are derived deterministically from the message bits, so there is only 1 valid combination of extra bits for each combination of message bits. So such a codeword only has $2^k$ valid combinations, and all other combinations indicate a possible transmission error. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
  - block code / code rate ::@:: It is simply the fraction of message bits per codeword: _k_/_n_. <p> The _gross bit rate_ is simply the number of bits sent per unit time, ignoring if the bits are useful or not. The _net bit rate_ is the number of _useful_ bits sent per unit time, which is obtained by multiplying the gross bit rate by the code rate. <!--SR:!2025-08-22,16,290!2025-08-20,14,290-->
- [parity bit](../../../../general/parity%20bit.md) ::@:: It is a bit added to a string of binary code. Parity bits are a simple form of error detecting code. <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
  - parity bit / details ::@:: We count the number of 1s in the message bits. The parity bit is derived based on the evenness or oddness of the number of 1s. This bit is then simply appended to the message to form a codeword. <p> This is an example of a $(k + 1, k)$ block code for _k_ message bits. <!--SR:!2025-08-22,15,290!2025-08-22,16,290-->
  - parity bit / even parity bit ::@:: The parity bit is 0 if the number of 1s is even, otherwise 1. Equivalently, the number of 1s in a valid codeword \(including the parity bit\) is even. \(__this course__: __Important__. We use this unless otherwise specified.\) <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - parity bit / odd parity bit ::@:: The parity bit is 0 if the number of 1s is odd, otherwise 1. Equivalently, the number of 1s in a valid codeword \(including the parity bit\) is odd. \(__this course__: __Important__. We do _not_ use this unless otherwise specified.\) <!--SR:!2025-08-21,14,290!2025-08-20,14,290-->
  - parity bit / usage ::@:: For each codeword, it can detect one-bit errors. However, it cannot correct the one-bit errors. This is because its minimum Hamming distance between any two valid codewords is 2. <p> Its main advantage is its high code rate. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
- block code
  - block code / spaces ::@:: A space can be represented by a graph: a vertex for each combination of bits, and an edge between every two combination of bits that differ by exactly 1 bit. <p> We can consider the message space and codeword space. The former constructs the space based on the message bits only, while the latter constructs the space based on the entire codeword. As a result, the former contains only valid codewords, while the latter contains both valid and invalid codewords. <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
    - block code / spaces / intuition ::@:: For an analog signal, increasing SNR decreases BER. This is done by increasing the _distance_ between 0 and 1. <p> A similar idea is applied for block codes. We can _detect_ errors by adding extra bits to increase the distance between valid codewords in the codeword space. Sometimes, we can even _correct_ errors. <!--SR:!2025-08-22,16,290!2025-08-20,14,290-->
- [Hamming distance](../../../../general/Hamming%20distance.md) ::@:: It between two strings or vectors of equal length is the number of positions at which the corresponding symbols are different. In other words, it measures the minimum number of substitutions required to change one string into the other, or equivalently, the minimum number of errors that could have transformed one string into the other. <!--SR:!2025-08-21,14,290!2025-08-22,15,290-->
  - Hamming distance / history ::@:: \(Richard Hamming, 1950\) <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
- block code
  - block code / Hamming distance ::@:: The minimum Hamming distance $d$ between any two valid codewords in the _codeword space_ \(not _message space_\) determines the maximum of error bits so that we can detect or correct errors. <p> We can _either_ detect errors only _or_ detect and correct errors if possible. <p> If we only detect errors, we can do so with up to $d - 1$ error bits. <p> If we detect and correct errors, and we simply use the closest valid codeword, we can detect up to $\left\lceil \frac {d - 1} 2 \right\rceil$ error bits and correct \(correctly\) up to $\left\lfloor \frac {d - 1} 2 \right\rfloor$ error bits. Not that if we can correct, then we must be able to detect, but the converse is not true for even $d$. For even $d$, there are invalid codewords with equal distance to multiple valid codewords, so we can detect said errors but not correct them correctly always. <!--SR:!2025-08-22,15,290!2025-08-20,14,290-->
- [repetition code](../../../../general/repetition%20code.md) ::@:: It is one of the most basic linear error-correcting codes. In order to transmit a message over a noisy channel that may corrupt the transmission in a few places, the idea of the repetition code is to just repeat the message several times. The hope is that the channel corrupts only a minority of these repetitions. <!--SR:!2025-08-20,14,290!2025-08-21,15,290-->
  - repetition code / details ::@:: There is only 1 data bit. We repeated the data bit for $n - 1$ more times. This forms a $(n, 1)$ block code. <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
  - repetition code / Hamming distance ::@:: The minimum Hamming distance $d$ between any two valid codewords \(there are only 2\) is $n$. <p> Intuitively, if we want to detect errors, we can always do so unless all $n$ bits have flipped. If we want to correct errors, we are taking the _majority vote_, so we can always \(correctly\) do so when at most $\left\lfloor \frac {n - 1} 2 \right\rfloor$ have flipped. Note we must choose to _either_ detect errors only _or_ detect and correct errors if possible. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
- assignment: [homework 1](assignments/homework%201/index.md)

## week 2 tutorial 2

- datetime: 2025-07-24T11:00:00+08:00/2025-07-24T12:20:00+08:00, PT1H20M
- topic: lab 3 review, lab 4, eye diagram, equalization
- ELEC 1200
  - ELEC 1200 / lab 3
  - ELEC 1200 / lab 4 ::@:: eye diagram: bit time → eye diagram: sub-sampling point → equalization → equalization: bit error rate <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
- [§ week 2 lab 2](#week%202%20lab%202)

## week 2 lab 2

- datetime: 2025-07-24T14:00:00+08:00/2025-07-24T16:50:00+08:00, PT2H50M
- topic: eye diagram, equalization
- status: attendance
- [§ week 2 tutorial 2](#week%202%20tutorial%202)
- ELEC 1200
  - ELEC 1200 / lab 4
    - ELEC 1200 / lab 4 / eye diagram, sub-sampling index ::@:: If there is an eye in the eye diagram, you can sub-sampling any point in the eye and get 0 bit error rate. <p> In general, bit error rate is lowest around SPB−1. <!--SR:!2025-08-20,14,290!2025-08-22,15,290-->
- assignment: [lab 4](assignments/lab%204/index.md)
- questions: [post lab quiz 4 derivative](questions/post%20lab%20quiz%204%20derivative.md)

## week 2 lab 3

- datetime: 2025-07-25T10:00:00+08:00/2025-07-26T12:50:00+08:00, PT2H50M
- status: unscheduled

## week 2 lecture 3

- datetime: 2025-07-25T14:00:00+08:00/2025-07-25T15:50:00+08:00, PT1H50M
- topic: error correcting codes; frequency domain
- block code
  - block code / codeword
  - block code / Hamming distance
    - block code / Hamming distance / notation ::@:: Sometimes the minimum Hamming distance between any two valid codewords are included as well: $(n, k, d)$ instead of simply $(n, k)$. <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
- repetition code
- parity bit
  - parity bit / details
  - parity bit / even parity bit
- block code
  - block code / \(8, 4\) block code ::@:: The 4 data bits $D_1, D_2, D_3, D_4$ are laid out in a 2-by-2 table in Z-order. The parity bits $P_1, P_2, P_3, P_4$ are appended to the table left and bottom edges as follows: $$\begin{bmatrix} D_1 & D_2 & P_1 \\ D_3 & D_4 & P_2 \\ P_3 & P_4 \end{bmatrix} \,.$$ The parity bits check the data bits on their corresponding column or row. <p> Note this is not the \[7, 4\] Hamming code or the \[8, 4\] Hamming code with an extra parity bit. However, the symmetry makes this code easier to learn, so this is why this code instead of the Hamming code is learnt instead. <p> \(__this course__: As a codeword, the data bits come before the parity bits.\) <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
    - block code / \(8, 4\) block code / Hamming distance ::@:: Its minimum Hamming distance is 3. \(__this course__: Proof not required.\) <p> So we can _either_ detect up to 2 error bits _or_ correct up to 1 error bit. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
    - block code / \(8, 4\) block code / syndrome bits ::@:: The syndrome bits are calculated when decoding a block code. For each column and row \(each set of parity bit and their corresponding data bits\), its syndrome bit is 0 if there is no parity error, or 1 if there is a parity error. Equivalently, the syndrome bit, when added to the column or row, "fixes" the parity of that column or row. \(__this course__: __Important__. We use _even_ parity for all parity checking, i.e. an even number of 1s is correct.\) <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
    - block code / \(8, 4\) block code / error detection ::@:: Assuming up to 2 data bits are flipped. <p> If all syndrome bits are 0, no errors are detected. Otherwise, there is an error, because flipping at most 2 data bits cannot make all syndrome bits 0. <!--SR:!2025-08-20,14,290!2025-08-22,16,290-->
    - block code / \(8, 4\) block code / error correction ::@:: Assuming up to 1 data bit is flipped. <p> If 1 syndrome bit is 1, that means its parity bit is flipped, because flipping a parity bit changes 1 syndrome bit. If 2 syndrome bits are 1, that means the data bit in the corresponding column and row is flipped, because flipping a data bit changes 2 syndrome bits. <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
  - block code / \(9, 4\) block code with parity bit ::@:: The 4 data bits $D_1, D_2, D_3, D_4$ are laid out in a 2-by-2 table in Z-order. The parity bits $P_1, P_2, P_3, P_4, P_5$ are appended to the table left and bottom edges as follows: $$\begin{bmatrix} D_1 & D_2 & P_1 \\ D_3 & D_4 & P_2 \\ P_3 & P_4 & P_5 \end{bmatrix} \,.$$ The first 4 parity bits check the data bits on their corresponding column or row. The last parity bit checks all previous 8 bits. <p> Note this is not the \[7, 4\] Hamming code or the \[8, 4\] Hamming code with an extra parity bit. However, the symmetry makes this code easier to learn, so this is why this code instead of the Hamming code is learnt instead. <p> \(__this course__: As a codeword, the data bits come before the parity bits.\) <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
    - block code / \(9, 4\) block code with parity bit / Hamming distance ::@:: Its minimum Hamming distance is 4. In general, add an extra parity bit to a block code \(that does not already have an extra parity bit added\) increases the minimum Hamming distance by 1. \(__this course__: Proof not required.\) <p> So we can _either_ detect up to 3 error bits _or_ detect up to 2 error bits and correct up to 1 error bit. <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
    - block code / \(9, 4\) block code with parity bit / syndrome bits ::@:: The syndrome bits are calculated when decoding a block code. For each column and row \(each set of parity bit and their corresponding data bits\), its syndrome bit is 0 if there is no parity error, or 1 if there is a parity error. The same is done for the last parity bit $P_5$ but for all bits. Equivalently, the syndrome bit, when added to the column or row, "fixes" the parity of that column or row. \(__this course__: __Important__. We use _even_ parity for all parity checking, i.e. an even number of 1s is correct.\) <!--SR:!2025-08-22,16,290!2025-08-22,15,290-->
    - block code / \(9, 4\) block code with parity bit / error detection ::@:: Assuming up to 3 data bits are flipped. <p> The embedded \(8, 4\) block code \(i.e. ignoring the parity bit\) can detect up to 2 error bits. For exactly 3 error bits, the embedded block code itself may not detect an error, but the last parity bit must be able to detect it. <!--SR:!2025-08-21,14,290!2025-08-20,14,290-->
    - block code / \(9, 4\) block code with parity bit / error correction ::@:: Assuming up to 2 data bit is flipped. <p> Check if the last parity bit is wrong. If so, there is exactly 1 error bit, and the procedure is the same as the \(8, 4\) block code \(i.e. ignoring the parity bit\). Otherwise, we can detect up to 2 error bits \(but not correct it\), as the embedded \(8, 4\) block code itself \(i.e. ignoring the parity bit\) can detect up to 2 error bits. <!--SR:!2025-08-23,16,290!2025-08-19,12,270-->
- [music](../../../../general/music.md) ::@:: It is the arrangement of sound to create some combination of form, harmony, melody, rhythm, or otherwise expressive content. <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
  - music / signal ::@:: In music, most instruments produce a sinusoid of a fundamental frequency and its overtones. When there are multiple instruments, their sounds are simply added together. This forms the waveform of music. <p> Actually, the same is true for any waveform, not just music. That is, any waveform can be considered as a combination of sinusoids of various amplitudes, frequencies, and phases. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
- [sine wave](../../../../general/sine%20wave.md) ::@:: It is a periodic wave whose waveform \(shape\) is the trigonometric sine function. <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
  - sine wave / sinusoid form ::@:: Sine waves of arbitrary phase and amplitude are called _sinusoids_ and have the general form: $$y(t)=A\sin(\omega t+\varphi )=A\sin(2\pi ft+\varphi )$$ where: <p> - $A$, _[amplitude](../../../../general/amplitude.md)_, the peak deviation of the function from zero. <br/> - $t$, the [real](../../../../general/real%20number.md) [independent variable](../../../../general/independent%20variable.md), usually representing [time](../../../../general/time.md) in [seconds](../../../../general/seconds.md). <br/> - $\omega$, _[angular frequency](../../../../general/angular%20frequency.md)_, the rate of change of the function argument in units of [radians per second](../../../../general/radians%20per%20second.md). <br/> - $f$, _[ordinary frequency](../../../../general/ordinary%20frequency.md)_, the _[number](../../../../general/real%20number.md)_ of oscillations \([cycles](../../../../general/turn%20(angle).md)\) that occur each second of time. <br/> - $\varphi$, _[phase](../../../../general/phase%20(waves).md)_, specifies \(in [radians](../../../../general/radian.md)\) where in its cycle the oscillation is at _t_ = 0. <p> \(__this course__: __Important__. We use cosine waves: $$A \cos(2\pi f t + \varphi) \,.$$\) <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
  - sine wave / cosine wave ::@:: Since $$\begin{aligned} \sin x & = \cos(x - \pi / 2) \\ \cos x & = \sin(x + \pi / 2) \,, \end{aligned}$$ so any sine wave can be represented as a cosine wave with a shifted phase, and vice versa. <p> \(__this course__: __Important__. We use cosine waves: $$A \cos(2\pi f t + \varphi) \,.$$\) <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
  - sine wave / discrete ::@:: We can consider a sine wave in discrete time by simply sampling the continuous sine wave. <p> We consider _N_ samples. Then the ordinary frequency $f$ is often replaced by _cycle frequency_ $k \in \set{0, 1, \ldots, \lfloor N / 2 \rfloor}$, and time $t$ is often replaced by discrete time index $n$: $$A \cos\left( 2 \pi \frac k N n + \varphi \right) \,.$$ The cycle frequency $k$ represents the number of \(co\)sine waves in _N_ samples. The period $T$ in samples is simply $N / k$. <p> Using $\frac k N n = ft$, the ordinary frequency $f$ is recovered as $$f = \frac k N \frac n t = \frac k N \frac 1 {T_s} = \frac k N F_s \,,$$ where $T_s$ is sampling period and $F_s = 1 / T_s$ is sampling frequency. <!--SR:!2025-08-23,16,290!2025-08-19,12,270-->
- [Fourier series](../../../../general/Fourier%20series.md) ::@:: It is an expansion of a periodic function into a sum of trigonometric functions. <!--SR:!2025-08-22,15,290!2025-08-21,15,290-->
  - Fourier series / forms ::@:: There are many forms to write the Fourier series: amplitude-phase form, exponential form, sine-cosine form. \(__this course__: We only teach the amplitude-phase form, and only scratch its surface.\) <!--SR:!2025-08-22,15,290!2025-08-22,15,290-->
  - Fourier series / amplitude-phase form ::@:: If the function $s(x)$ is real-valued then the Fourier series can also be represented as $$s_{N}(x)=A_{0}+\sum _{n=1}^{N}A_{n}\cos \left(2\pi {\tfrac {k}{P} }x-\varphi _{k}\right)$$ where $A_{n}$ is the amplitude and $\varphi _{n}$ is the phase shift of the $k^{th}$ harmonic \(positive shifts cosine to the right\). <p> \(__this course__: Since we are thinking in discrete time with $N$ samples, using $n / N = x / P$, and that cycle frequencies are up to $\lfloor N / 2 \rfloor$ we have: $$s_{N}(x) = A_0 + \sum_{n = 1}^{\lfloor N / 2 \rfloor} A_k \cos\left(2 \pi \frac k N n + \varphi_k \right) \,.$$ Notice the phase shift is negated, but this is simply a matter of convention.\) <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
    - Fourier series / amplitude-phase form / interpretation ::@:: This means any discrete waveform with $N$ samples can be decomposed into $\lfloor N / 2 \rfloor + 1$ cosines. \(Though the first cosine has zero frequency and is really just a flat line.\) <p> $A_0$ is the _average level_, also known as the _DC offset_. $A_k$ is the amplitude of the cosine with cycle frequency $k$. $\varphi_k$ is the phase of the cosine with cycle frequency $k$, with positive values shifting to the left \(when $+ \varphi_k$ instead of $- \varphi_k$ is used\). <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
    - Fourier series / amplitude-phase form / amplitude spectrum ::@:: We can plot the $A_k$ amplitude against cycle frequency $k$. It can show the most important frequencies, which are frequencies with the largest amplitudes. <p> By keeping frequencies with the largest amplitudes, we can roughly recreate the waveform, with the original waveform fully recovered when all frequencies with nonzero amplitudes are kept. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
    - Fourier series / amplitude-phase form / phase spectrum ::@:: We can also plot the $\varphi_k$ phase against cycle frequency $k$. <p> Combined with the amplitude spectrum, they describe the original discrete signal completely, i.e. the original signal can be fully recovered from them. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - Fourier series / representation ::@:: It is one of way to represent the _Fourier transform_ of a signal. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
- [integral transform](../../../../general/integral%20transform.md) ::@:: It is a type of transform that maps a function from its original function space into another function space via integration, where some of the properties of the original function might be more easily characterized and manipulated than in the original function space. The transformed function can generally be mapped back to the original function space using the _inverse transform_. <!--SR:!2025-08-20,14,290!2025-08-20,14,290-->
  - integral transform / examples ::@:: Fourier transform, Laplace transform, Z-transform, etc. <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
  - integral transform / motivation ::@:: Transforms are _invertible_, so no information is lost or gained using a transform or its inverse. So transforms give different views of the same signal. <p> These different views allow us to understand and manipulate the signal in other ways. Some signal manipulations may be \(much\) easier with these different views. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
- [discrete Fourier transform](../../../../general/discrete%20Fourier%20transform.md) \(DFT\) ::@:: \(__this course__: optional\) <p> It takes _N_ samples and returns _N_ complex coefficients called _Fourier coefficients_. <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
  - discrete Fourier transform / definition ::@:: \(__this course__: optional\) <p> It transforms a sequence of _N_ complex numbers $\left\{\mathbf {x} _{n}\right\}:=x_{0},x_{1},\ldots ,x_{N-1}$ into another sequence of complex numbers, $\left\{\mathbf {X} _{k}\right\}:=X_{0},X_{1},\ldots ,X_{N-1}$, which is defined by: $$X_{k}=\sum _{n=0}^{N-1}x_{n}\cdot e^{-i2\pi {\tfrac {k}{N} }n} \,.$$ <!--SR:!2025-08-22,16,290!2025-08-20,14,290-->
  - discrete Fourier transform / MATLAB ::@:: The function `fft` can be used to compute the DFT of a signal. \(The "FFT" in `fft` stands for "fast Fourier transform".\) <p> Note the indexing in MATLAB starts from 1, e.g. $X_0$ is `Xdft(1)`, where `Xdft` is `fft(x)`. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - discrete Fourier transform / Fourier series ::@:: \(__this course__: optional\) <p> For a _real_ signal, we can compute its Fourier series using the DFT. In particular, we can get the amplitude spectrum and phase spectrum. <p>  For the amplitude spectrum: $$A_k = \begin{cases} \frac 1 N \lvert X_k \rvert & k = 0 \text{ or } \frac N 2 \\ \frac 2 N \lvert X_k \rvert & \text{otherwise} \,. \end{cases}$$ \(Note that if $N / 2$ is an non-integer, then it cannot equal $k$, which must be an integer\) <p> For the phase spectrum: $$\varphi_k = \angle X_k \,.$$ <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
- [complex number](../../../../general/complex%20number.md) ::@:: \(__this course__: optional\) <p> It is an element of a number system that extends the real numbers with a specific element denoted _i_, called the imaginary unit and satisfying the equation $i^{2}=-1$; every complex number can be expressed in the form $a+bi$, where _a_ and _b_ are real numbers. <p> \(__this course__: This course follows electrical engineering convention and uses $j$ instead of $i$.\) <!--SR:!2025-08-21,15,290!2025-08-20,14,290-->
  - complex number / to polar coordinates ::@:: \(__this course__: optional\) <p> $$\begin{aligned} \lvert z \rvert & = \sqrt{a^2 + b^2} \\ \angle z & = \arctan(b / a) \,. \end{aligned}$$ <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
  - complex number / from polar coordinates ::@:: \(__this course__: optional\) <p> $$\begin{aligned} a & = \lvert z \rvert \cos(\angle z) \\ bi & = i \lvert z \rvert \sin(\angle z) \,. \end{aligned}$$ <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->

## week 3 lecture

- datetime: 2025-07-28T14:00:00+08:00/2025-07-28T16:50:00+08:00, PT2H50M
- topic: filters, frequency response; time—frequency analysis, source coding; signal transmission multiplexing
- [filter](../../../../general/filter%20(signal%20processing).md) ::@:: It is a device or process that removes some unwanted components or features from a signal. <!--SR:!2025-08-23,16,290!2025-08-21,14,290-->
  - filter / intuition ::@:: Intuitively, the input may consists of various typical components. A filter lets most of some components pass through while blocking most of other components. <p> As a physical example, consider a physical filter. It may let all small particles \(e.g. water\) pass through while blocking most large particles \(e.g. insoluble substances\). <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
  - filter / components ::@:: In signal processing, these components are sinusoids of different frequencies. Any real discrete signal of _N_ samples can be described by $1 + \lfloor N / 2 \rfloor$ sinusoids \(with phase offset\), by its Fourier series. <p> Long time ago, we have used unit steps to represent the input signal. However, the output signal generally does not look like unit steps, so we do not use unit steps as the components. <!--SR:!2025-08-23,16,290!2025-08-21,14,290-->
- Fourier series
  - Fourier series / continuous time ::@:: The continuous Fourier series, where both the time and frequency domains are continuous, is simply the Fourier transform. \(__this course__: However, in this course...\) <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
    - Fourier series / continuous time / this course ::@:: \(__this course__: For simplicity, we "generalize" the Fourier series to the continuous time; that is, the original $$x[n] = \sum_{k = 0}^{\lfloor N / 2 \rfloor} A[k] \cos\left(2 \pi \frac k N n + \varphi[k] \right)$$ becomes $$x(t) = \int_0^\infty A(f) \cos(2 \pi f t + \varphi(f)) \,df \,.$$ We see $k$ is replaced by $f$ and $n / N$ is replaced by $t$.\) <!--SR:!2025-08-20,14,290!2025-08-20,14,290-->
- linear time-invariant system
- [frequency response](../../../../general/frequency%20response.md) ::@:: It of a system is the quantitative measure of the magnitude and phase of the output as a function of input frequency. <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
  - frequency response / effects ::@:: Assume the system is LTI. <p> For each sinusoid component of frequency $f$ in the input signal: $$x_f(t) = A(f) \cos(2\pi ft + \varphi(f)) \,,$$ the output signal is a sinusoid component of the same frequency $f$, but scaled by $S(f)$ and phase shifted by $\theta(f)$ \(positive shifts the sinusoid to the left\): $$y_f(t) = S(f) \cdot A(f) \cos(2\pi ft + \varphi(f) + \theta(f)) \,.$$ <p> Use linearity of LTI systems to split the input signal and then add the output signal. <!--SR:!2025-08-22,16,290!2025-08-22,16,290-->
  - frequency response / amplitude response ::@:: Usually we are more interested in the amplitude scaling than the phase shifts. This, which is simply the filter scaling function $S(f)$, can be plotted as a graph. <!--SR:!2025-08-23,16,290!2025-08-21,14,290-->
    - frequency response / amplitude response / types ::@:: From the amplitude response of a filter, there are 4 common types of filters \(there are others\): all-pass, low-pass, high-pass, and band-pass. <!--SR:!2025-08-20,14,290!2025-08-20,14,290-->
- [all-pass filter](../../../../general/all-pass%20filter.md) ::@:: It is a signal processing filter that passes all frequencies equally in gain, but changes the phase relationship among various frequencies. <!--SR:!2025-08-21,15,290!2025-08-21,15,290-->
  - all-pass filter / amplitude response ::@:: Ideally, its amplitude response is the same for all frequencies. That means all sinusoids are scaled equally. <!--SR:!2025-08-21,14,290!2025-08-21,14,290-->
  - all-pass filter / phase response ::@:: An all-pass filter that only scales is probably quite useless in practice. Its phase response is probably nontrivial so that it can be useful, i.e. the filter only modifies the sinusoid phases. <!--SR:!2025-08-22,16,290!2025-08-20,14,290-->
- [low-pass filter](../../../../general/low-pass%20filter.md) ::@:: It is a filter that passes signals with a frequency lower than a selected cutoff frequency and attenuates signals with frequencies higher than the cutoff frequency. <!--SR:!2025-08-21,15,290!2025-08-20,14,290-->
  - low-pass filter / amplitude response ::@:: Ideally, its amplitude response is some nonzero constant until a _cutoff frequency_ $f_{co}$, and then zero hence after. <p> So it emphasizes "bass" or low-frequency components. <p> \(__this course__: The ideal amplitude response is _nonzero_ at the cutoff frequency.\) <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
  - low-pass filter / graph ::@:: On a graph, you can observe that sudden jumps in the input generally become smoother in the output. <p> This is very similar to what we see in physical channels, where sudden jumps in the input requires time to transit in the output. Indeed, such channels are usually modeled by low-pass filters. <!--SR:!2025-08-22,16,290!2025-08-22,16,290-->
- [high-pass filter](../../../../general/high-pass%20filter.md) ::@:: It is an electronic filter that passes signals with a frequency higher than a certain cutoff frequency and attenuates signals with frequencies lower than the cutoff frequency. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - high-pass filter / amplitude response ::@:: Ideally, its amplitude response is some zero until a _cutoff frequency_ $f_{co}$, and then some nonzero constant hence after. <p> So it emphasizes "treble" or high-frequency components. <p> \(__this course__: The ideal amplitude response is _nonzero_ at the cutoff frequency.\) <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
  - high-pass filter / graph ::@:: On a graph, you can observe that sudden jumps in the input are emphasized in the output, while flat inputs approach zero in the output. <!--SR:!2025-08-21,14,290!2025-08-22,15,290-->
- [band-pass filter](../../../../general/band-pass%20filter.md) ::@:: It is a device that passes frequencies within a certain range and rejects \(attenuates\) frequencies outside that range. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
  - band-pass filter / amplitude response ::@:: Ideally, its amplitude response is zero until a _low frequency cutoff_ $f_{l}$, and then some nonzero constant until a _high frequency cutoff_ $f_{h}$, and then zero hence after. <p> So it emphasizes "midrange" or middle-frequency components. <p> Its _center frequency_ $f_{c}$ is simply their middle: $$f_c = (f_l + f_h) / 2 \,.$$ Its _bandwidth_ is $$\text{BW} = f_h - f_l \,.$$ <p> \(__this course__: The ideal amplitude responses are _nonzero_ at the 2 cutoff frequencies.\) <!--SR:!2025-08-21,14,290!2025-08-22,15,290-->
  - band-pass filter / graph ::@:: The effect on the graph generally depends on the filter parameters. It usually consists of a mix of effects from the low-pass and high-pass filter. <!--SR:!2025-08-22,15,290!2025-08-21,15,290-->
- frequency response
  - frequency response / vs. step response ::@:: Assume the system is LTI. Then, they are equivalent models, like how the exponential step response is equivalent to the recursive feedback model. <p> They are different ways to view the same thing, and more convenient in different contexts, like time domain signal and its corresponding frequency domain signal \(Fourier transform\). <!--SR:!2025-08-22,16,290!2025-08-21,14,290-->
- frequency response
  - frequency response / complex number ::@:: \(__this course__: optional\) <p> Above, we have split the frequency response into amplitude scaling and phase shifting. <p> But if we use phasors to represent sinusoids \(using complex numbers cleverly to represent \(co\)sine waves\), then the frequency response is more conveniently described as a complex function: $$H(f) = S(f) e^{j \theta (f)} \,.$$ <!--SR:!2025-08-20,14,290!2025-08-21,14,290-->
- [time–frequency analysis](../../../../general/time–frequency%20analysis.md) ::@:: It comprises those techniques that study a signal in both the time and frequency domains simultaneously, using various time–frequency representations. <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
  - time–frequency analysis / intuition ::@:: Above, we have considered transforming the entire signal in time to the frequency domain. <p> But what if we split the signal into multiple \(potentially overlapping\) parts, and then convert each to the frequency domain? Then we can find how short-term sinusoids of different frequencies change over time. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
- [spectrogram](../../../../general/spectrogram.md) ::@:: It is a visual representation of the spectrum of frequencies of a signal as it varies with time. <!--SR:!2025-08-21,15,290!2025-08-21,14,290-->
  - spectrogram / representation ::@:: The vertical axis represents frequency. The horizontal axis represents time. Some conventions have them reversed. \(__this course__: Use the above explicitly mentioned convention.\) <p> The color represents amplitude, with black usually representing almost zero amplitude, blue usually representing small amplitude, and red representing large amplitude. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
  - spectrogram / computation ::@:: Divide the signal in time into many frames. Each frame is typically 20—50&nbsp;ms long. Then, compute the amplitude spectrum for each frame. Finally, plot the amplitude spectrum, either as a 3D graph or a colored 2D graph. <p> Some notes regarding the amplitude. First, the logarithm of the amplitude is usually graphed instead to emphasize small differences between small amplitudes. Second, the logarithm of zero is undefined, so the amplitude usually either is floored \(__this course__: use floored\) or added by a very very small positive value added before taking its logarithm. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
  - spectrogram / speech ::@:: The basic unit of speech is phoneme, which is a distinct unit of sound that distinguish a word from another, e.g. "b", "er", "ey", "p", "z", etc. <p> Different phonemes produce different amplitude spectrums. So we can see them show up in the spectrogram. <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
- [data compression](../../../../general/data%20compression.md) ::@:: It is the process of encoding information using fewer bits than the original representation. Any particular compression is either lossy or lossless. <p> It is also known as __source coding__. <!--SR:!2025-08-21,14,290!2025-08-21,15,290-->
  - data compression / communications system ::@:: The transmitter _compresses_ the original data and sends the compressed data via the channel. The receiver _decompresses_ the received compressed data to recover either the original data \(lossless compression\) or data very close to the original data \(lossy compression\). <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
  - data compression / types ::@:: lossless, lossy <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - data compression / lossless ::@:: The output is _exactly_ the same as the input. It is used for naturally digital bit streams, e.g. datasets, documents, messages, etc. <p> examples: Huffman encoding, LZW, RAR files, ZIP files, etc. <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
  - data compression / lossy ::@:: The output is very "close" to the original data. It is used for naturally physical bit streams, e.g. audio, video, etc. <p> examples: MP3, MPEG-4, WMV, etc. <!--SR:!2025-08-22,16,290!2025-08-22,16,290-->
- [digital audio](../../../../general/digital%20audio.md) ::@:: It is a representation of sound recorded in, or converted into, digital form. In digital audio, the sound wave of the audio signal is typically encoded as numerical samples in a continuous sequence. <!--SR:!2025-08-20,14,290!2025-08-22,15,290-->
  - digital audio / data rate ::@:: data rate = sampling rate \* quantization bits \* channels <p> Data rate is in bits per second. Sampling rate is in Hz. Quantization bits are the number of bits to represent 1 sample in 1 channel. Channels are the number of independent audio signals. <!--SR:!2025-08-20,14,290!2025-08-21,14,290-->
  - digital audio / sampling rate ::@:: Common numbers are 44&nbsp;100 and 48&nbsp;000&nbsp;Hz. <!--SR:!2025-08-21,14,290!2025-08-20,14,290-->
  - digital audio / quantization bits ::@:: Common numbers are 16, 24, and 32 bits. <!--SR:!2025-08-22,16,290!2025-08-20,14,290-->
  - digital audio / channels ::@:: Common numbers are 1 \(monophonic\), 2 \(stereo\), 6 \(5.1 surround sound\), and 8 \(7.1 surround sound\). <!--SR:!2025-08-20,14,290!2025-08-20,14,290-->
  - digital audio / data rate
    - digital audio / data rate / compression ::@:: We see that storing audio takes a lot of space! So we usually do compression. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
  - digital audio / compression ::@:: Compression can be done by reducing the data rate or using a compression method. <p> Reducing the data rate usually degrades the audio significantly without reducing the size significantly, so a compression method is often used instead. <p> Lossless compression usually can only halve the original size, so lossy compression, e.g. MP3, is more often used to achieve about 0.1—0.2 of the original size. <!--SR:!2025-08-21,15,290!2025-08-21,14,290-->
- [MP3](../../../../general/MP3.md) ::@:: It is a audio coding format developed largely by the Fraunhofer Society in Germany under the lead of Karlheinz Brandenburg. It was designed to greatly reduce the amount of data required to represent audio, yet still sound like a faithful reproduction of the original uncompressed audio to most listeners. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
  - MP3 / history ::@:: Previous standards were produced by the MPEG \(Moving Pictures Experts Group\), set up by the ISO \(International Standards Organizations\), e.g. MPEG-1 \(1992\), MPEG-2 \(1994\), etc. <!--SR:!2025-08-22,16,290!2025-08-22,15,290-->
  - MP3 / acronym ::@:: It stands for "MPEG-1 Audio Layer III" or "MPEG-2 Audio Layer III". \(__this course__: "MPEG Audio Layer III"\) <!--SR:!2025-08-20,14,290!2025-08-22,15,290-->
  - MP3 / overview ::@:: It can achieve up to about 90% size reduction! This enables audio streaming and compact audio storage. <p> It makes use of human audio perceptions and _psychoacoustics_. <!--SR:!2025-08-22,16,290!2025-08-22,16,290-->
- [psychoacoustics](../../../../general/psychoacoustics.md) ::@:: It is the branch of psychophysics involving the scientific study of the perception of sound by the human auditory system. It is the branch of science studying the psychological responses associated with sound including noise, speech, and music. <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
  - psychoacoustics / human hearing frequency range ::@:: about \[20&nbsp;Hz, 20&nbsp;000&nbsp;Hz\] <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
  - psychoacoustics / human voice range ::@:: about \[500&nbsp;Hz, 2&nbsp;000&nbsp;Hz\] <p> Low frequencies are generally vowels while high frequencies are generally consonants. <!--SR:!2025-08-22,15,290!2025-08-21,15,290-->
  - psychoacoustics / human frequency sensitivity ::@:: more sensitive to mid-frequencies, which is about \[500&nbsp;Hz, 5&nbsp;000&nbsp;Hz\] <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
  - psychoacoustics / perceptual coding ::@:: Instead of trying to compress the bits faithfully \(lossless\), we try to compress the bits with loss in such a way that only very slightly affects how humans perceive the compressed audio. <p> This compression involves removing useless information and encoding remaining information efficiently. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
    - psychoacoustics / perceptual coding / useless information ::@:: remove sounds outside human hearing frequency range and _masked sounds_; and use mono for low-frequency components even in a stereo audio <!--SR:!2025-08-21,14,290!2025-08-22,16,290-->
    - psychoacoustics / perceptual coding / efficient encoding ::@:: apply integral transforms to work in the frequency domain, then apply _nonuniform quantization_ \(with loss\), and then apply lossless coding \(e.g. Huffman coding\) <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
- [auditory masking](../../../../general/auditory%20masking.md) ::@:: It occurs when the perception of one sound is affected by the presence of another sound. <p> The most common is a dominant tone masking sounds with frequencies near it. <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
  - auditory masking / definitions ::@:: auditory threshold: minimum signal level for a pure tone to be heard <br/> masking thershold: minimum signal level given a pure tone is present <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
  - auditory masking / perceptual coding ::@:: Masked sounds require less precision to be encoded faithfully to human ears. So the quantization is coarser, and less bits are needed to encode it. <!--SR:!2025-08-23,16,290!2025-08-21,14,290-->
- [quantization](../../../../general/quantization%20(signal%20processing).md) ::@:: It, in mathematics and digital signal processing, is the process of mapping input values from a large set \(often a continuous set\) to output values in a \(countable\) smaller set, often with a finite number of elements. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
  - quantization / signal ::@:: Analog signals typically have continuous values within a range, so they can take on infinitely many values. <p> But for digital storage, we need to use binary numbers to represent these values, which can take on finitely many values \(2<sup>_n_</sup> for _n_ bits\). Usually we simply divide the continuous signal range into 2<sup>_n_</sup> levels \(both ends inclusive\), and then _quantize_ the analog signal by converting each value to the closest level representable by binary numbers. <p> Clearly, this produces error, called _quantization_ or _rounding_ error. <!--SR:!2025-08-21,14,290!2025-08-20,14,290-->
  - quantization / resolution ::@:: It can be either measured as the number of bits used to store each sample \(higher is less error\) or the difference between consecutive levels \(lower is less error\). <p> Higher resolution reduces the quantization or rounding error at the cost of using more bits to store each sample. <!--SR:!2025-08-21,14,290!2025-08-22,16,290-->
- psychoacoustics
  - psychoacoustics / perceptual coding
    - psychoacoustics / perceptual coding / mono low-frequency ::@:: Most digital audio are stereo \(2 channels\), with a channel for each ear. Low frequency components, which are usually bass, can be not stored separately for each channel while not affecting the perception significantly. <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
    - psychoacoustics / perceptual coding / nonuniform quantization ::@:: Instead of using the same quantization resolution for all frequency components, different resolutions are used, e.g. lower resolution \(less bits\) for masked frequency components, etc. <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
- [signal transmission](../../../../general/signal%20transmission.md) ::@:: It \(sometimes abbreviated as "TX"\) is the process of sending or propagating an analog or digital signal via a medium that is wired, wireless, or fiber-optic. <!--SR:!2025-08-21,15,290!2025-08-21,14,290-->
  - signal transmission / channels ::@:: Signals are transmitted through a _channel_. Channels often operate _only_ in certain frequency ranges. They often suffer from distortion, interference, and noise. <!--SR:!2025-08-20,14,290!2025-08-22,15,290-->
  - signal transmission / radio waves ::@:: Radio waves have a wide range of frequencies, called the _radio spectrum_. \(__this course__: The definition used is zero to infinity, which should be more properly just _electromagnetic waves_.\) <!--SR:!2025-08-21,15,290!2025-08-22,16,290-->
  - signal transmission / spectrum crunch ::@:: While the radio spectrum is very wide, we also have many many many users wanting to use it! Further, radio waves generally cannot be confined to specific regions. If multiple users use the same frequency range, then there will be interference. <p> So frequency ranges need to be allocated and regulated by the government, but even then it is still very _crowded_. <!--SR:!2025-08-21,15,290!2025-08-20,14,290-->
  - signal transmission / mm-wave bands ::@:: They are in between about 30 and 300&nbsp;GHz, which are relatively less congested and have more bandwidth. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
  - signal transmission / protocols ::@:: simplex: one direction only; e.g. broadcasts, TVs, etc. <br/> half duplex: both directions possible, but one direction simultaneously; e.g. CB radio, walkie-talkies, etc. <br/> full duplex: both directions simultaneously; e.g. most modern communications nowadays, etc. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
  - signal transmission / allocation ::@:: The government allocates and regulates frequency ranges. It may sometimes sell ranges too. <p> Governments of different countries must coordinate together. <!--SR:!2025-08-20,14,290!2025-08-21,14,290-->
    - signal transmission / allocation / Hong Kong ::@:: This is done by the Office of the Communications Authority \(OFCA\). In general, you must obtain a license from it to use the radio spectrum. <p> It coordinates with the world authority International Telecommunications Union \(ITU\). <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
- [frequency sharing](../../../../general/frequency%20sharing.md) ::@:: It is the assignment to or use of the same radio frequency by two or more stations that are separated geographically or that use the frequency at different times. <p> \(__this course__: This course describes a different thing... See below.\) <!--SR:!2025-08-21,15,290!2025-08-21,15,290-->
  - frequency sharing / this course ::@:: \(__this course__: Multiple users share the same channel or frequency range. This is implemented using multiplexing \(combining multiple input signals into one signal\) and demultiplexing \(inverts multiplexing\).\) <!--SR:!2025-08-21,14,290!2025-08-22,16,290-->
- [baseband](../../../../general/baseband.md) ::@:: It is the range of frequencies occupied by a signal that has not been modulated to higher frequencies. They typically originate from transducers, converting some other variable into an electrical signal. <!--SR:!2025-08-20,14,290!2025-08-20,14,290-->
  - baseband / examples ::@:: Basically all signals before being modulated for transmission, or all signals after being demodulated after reception. <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
  - baseband / bandlimiting ::@:: Typically, for modulation later, the baseband signal should have confined frequency range around 0&nbsp;Hz, making it _bandlimited_. <p> A low-pass filter is often used to ensure this is the case. <!--SR:!2025-08-22,15,290!2025-08-22,15,290-->
- [multiplexing](../../../../general/multiplexing.md) ::@:: It is a method by which multiple analog or digital signals are combined into one signal over a shared medium. The aim is to share a scarce resource—a physical transmission medium. <!--SR:!2025-08-23,16,290!2025-08-21,14,290-->
  - multiplexing / types ::@:: 3 major types: frequency-division multiplexing, statistical multiplexing, time-division multiplexing, etc. <!--SR:!2025-08-20,14,290!2025-08-22,15,290-->
  - multiplexing / time-division multiplexing ::@:: Signals from different users are sent at different time slots, which are allocated to different users in advanced. <!--SR:!2025-08-21,14,290!2025-08-21,15,290-->
  - multiplexing / frequency-division multiplexing ::@: The radio spectrum is divided into frequency bands, where each frequency band is assigned to at most one user. \(A user can have multiple frequency bands.\) <p> Often, _modulation_ is used. The idea is we somehow shift the frequency components of the baseband signal to higher frequencies such that it is within the allocated frequency range. <!--SR:!2025-08-21,15,290-->
- [signal modulation](../../../../general/signal%20modulation.md) ::@:: It is the process of varying one or more properties of a periodic waveform in electronics and telecommunication for the purpose of transmitting information. <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
  - signal modulation / simpler explanation ::@:: It combines two signals to create a third signal \(__this course__: For simplicity, we consider _amplitude modulation_ \(AM\) only.\) <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
- [amplitude modulation](../../../../general/amplitude%20modulation.md) \(AM\) ::@:: It is a signal modulation technique used in electronic communication, most commonly for transmitting messages with a radio wave. In amplitude modulation, the instantaneous amplitude of the wave is varied in proportion to that of the message signal, such as an audio signal. <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
  - amplitude modulation / general form ::@:: In general form, a modulation process of a sinusoidal carrier wave may be described by the following equation: $$m(t)=A(t)\cdot \cos(\omega t+\phi (t)) \,,$$ where _A\(t\)_ represents the time-varying amplitude of the sinusoidal carrier wave and the cosine-term is the carrier at its angular frequenc $\omega$ \($\omega = 2\pi f$\), and the instantaneous phase deviation $\phi (t)$. <!--SR:!2025-08-20,14,290!2025-08-21,14,290-->
  - amplitude modulation / intuition ::@:: The carrier signal \(the signal that is not the baseband signal\), which is usually a cosine wave of fixed frequency, is within the allocated frequency range. <p> Then we vary the amplitude of the carrier using the baseband signal. Since the baseband signal is bandlimited, this will not result in frequency components that are very far away from the original carrier frequency, so the modulated signal stays within the allocated frequency range. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - amplitude modulation / simple case ::@:: We consider modulating a cosine wave of frequency $f$ in the most simple way. The carrier is a cosine wave of frequency $f_0$, which is typically much larger than $f$. <p> Then the most simple way to AM is: $$m(t) \cos(2\pi f t) \cos(2\pi f_0 t) \,.$$ Using trigonometric identities, we have: $$\begin{aligned} m(t) & = \cos(2\pi f t) \cos(2 \pi f_0 t) \\ & = \frac 1 2\left(\cos(2 \pi (f_0 - f) t) + \cos(2 \pi (f_0 + f) t) \right) \,. \end{aligned}$$ <p> So we see the modulated signal becomes two frequency components at $f_0 - f$ and $f_0 + f$. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
    - amplitude modulation / simple case / bandwidth ::@:: If the original signal has a bandwidth of $W$ \(frequencies are from 0 to $W$\), then the modulated sign has a bandwidth of $2W$ \(frequencies are from $f_0 - W$ to $f_0 + W$\). <p> Actually, the bandwidth is really the same, once you consider that for a real sinusoid signal of amplitude $A$, it has a \(complex\) sinusoid component of amplitude $A / 2$ at positive frequency $f$ and also at at _negative_ frequency $-f$. \(__this course__: Not mentioned. Ignore this paragraph.\) <!--SR:!2025-08-20,14,290!2025-08-23,16,290-->
    - amplitude modulation / simple case / linearity ::@:: Since a baseband signal can be approximated by adding multiple components of different frequencies, and modulation is a _linear_ operation, so we can perform the simple case analysis for each component, and then add the output results together to get the modulated signal. <!--SR:!2025-08-22,16,290!2025-08-21,15,290-->
  - amplitude modulation / frequency domain ::@:: For a positive component of frequency of $f$ and amplitude $A$ in the baseband signal, we see two corresponding components of the same amplitude $A_0 A / 2$ \(where $A_0$ is the carrier signal amplitude\) at frequency $f_0 - f$ and $f_0 + f$. <p> This is clear if you know negative frequencies and the properties of Fourier transform. That is, element-wise multiplication in time \(frequency\) domain corresponds to convolution in frequency \(time\) domain. \(__this course__: Not mentioned.\) <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
  - amplitude modulation / multiplexing ::@:: To use AM for multiplexing, the baseband signals should be bandlimited \(say a frequency range between 0 and $\text{BW}$\). The carrier signals should be separated by a frequency difference of more than $2\text{BW}$ to avoid overlapping between the modulated signals. <!--SR:!2025-08-21,15,290!2025-08-22,16,290-->
- multiplexing
  - multiplexing / guard bands ::@:: They are unused bands that are in between the modulated baseband signals. They help avoid interference even if there is leakage outside the theoretical bandwidth of baseband signals. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->

## week 3 tutorial

- datetime: 2025-07-29T11:00:00+08:00/2025-07-29T12:20:00+08:00, PT1H20M
- status: unscheduled

## week 3 lab

- datetime: 2025-07-29T14:00:00+08:00/2025-07-29T16:50:00+08:00, PT2H50M
- status: unscheduled

## week 3 lecture 2

- datetime: 2025-07-30T14:00:00+08:00/2025-07-30T15:50:00+08:00, PT1H50M
- topic: signal transmission demultiplexing; introduction to networks
- assignment: [homework 2](assignments/homework%202/index.md)
- signal transmission
  - signal transmission / radio waves
  - signal transmission / spectrum crunch
- multiplexing
  - multiplexing / types
  - multiplexing / frequency-division multiplexing
  - multiplexing / demultiplexing ::@:: Multiplexing modulates the individual baseband signals and then additively combine them to get the transmitted signal. Demultiplexing inverts this process: it recovers one of the baseband signal from the transmitted signal. <p> Two steps are needed: _channel selection_ and _demodulation_. <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
    - multiplexing / demultiplexing / channel selection ::@:: A band-pass filter is applied so that only frequencies within the own allocated frequency are kept. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
    - multiplexing / demultiplexing / demodulation ::@:: It reverses modulation. This is often done by _mixing_. <p> Often, the demodulation process itself, imperfect filters, and noise add high-frequency components outside the bandwidth to the demodulated signal, so we often add a low-pass filter to remove them. <!--SR:!2025-08-22,15,290!2025-08-21,15,290-->
- band-pass filter
  - band-pass filter / amplitude response
- [demodulation](../../../../general/demodulation.md) ::@:: It is the process of extracting the original information-bearing signal from a carrier wave. <!--SR:!2025-08-20,14,290!2025-08-21,15,290-->
  - demodulation / intuition ::@:: Modulation combines a baseband signal into a carrier signal to obtain a modulated signal. Demultiplexing inverts this: it recovers the baseband signal from the modulated signal. <!--SR:!2025-08-21,14,290!2025-08-22,16,290-->
- amplitude modulation
  - amplitude modulation / demodulation ::@:: 2 main methods: _envelope detector_, _product detector_ \(mixing\) <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
- [product detector](../../../../general/product%20detector.md) ::@:: It is a type of demodulator used for AM and SSB signals. Rather than converting the envelope of the signal into the decoded waveform like an envelope detector, the product detector takes the product of the modulated signal and a local oscillator, hence the name. <!--SR:!2025-08-22,15,290!2025-08-21,15,290-->
  - product detector / mathematical model ::@:: If _m_\(_t_\) is the original message, the AM signal can be shown to be $$\,x(t)=(C+m(t))\cos(\omega t).$$ Multiplying the AM signal _x_\(_t_\) by an oscillator at the same frequency as and in phase with the carrier yields $$\,y(t)=(C+m(t))\cos(\omega t)\cos(\omega t),$$ which can be re-written as $$\,y(t)=(C+m(t))\left({\tfrac {1}{2} }+{\tfrac {1}{2} }\cos(2\omega t)\right).$$ After filtering out the high-frequency component based around cos\(2ω<!-- markdown separator -->_t_\) and the DC component _C_, the original message will be recovered \(annotation: after multiplying by a factor of 2\). <p> \(__this course__: Assume $C = 0$.\) <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
  - product detector / signal loss ::@:: We see that we need to filter out the high-frequency components, which contains part of the signal but modulated \(with an amplitude a _quarter_ of the original signal for both components\). <p> This results in signal loss. Indeed, the baseband signal we have recovered is _half_ the original amplitude. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - product detector / local oscillator ::@:: The local oscillators at the transmitter and receiver should have the same frequency and synchronized \(same phase\). <p> We can consider the above mathematical model when the frequencies differ by $\Delta f$. Then we see the recovered message is modulated \(multiplied\) by a low-frequency cosine wave $\cos(2 \pi (\Delta f) t)$. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
- [direct-conversion converter](../../../../general/direct-conversion%20converter.md) \(DCR\) ::@:: It is a radio receiver design that demodulates the incoming radio signal using synchronous detection driven by a local oscillator whose frequency is identical to, or very close to the carrier frequency of the intended signal. <p> It uses a product detector. Many also uses a low-noise amplifier, which is a special amplifier that boost signal more than noise. <!--SR:!2025-08-22,15,290!2025-08-21,15,290-->
- [point-to-point](../../../../general/point-to-point%20(telecommunications).md) ::@:: It refers to a communications connection between two communication endpoints or nodes. An example is a telephone call, in which one telephone is connected with one other, and what is said by one caller can only be heard by the other. <p> \(__this course__: covered by the first part of this course\) <!--SR:!2025-08-22,16,290!2025-08-20,14,290-->
- [telecommunications network](../../../../general/telecommunications%20network.md) ::@:: It is a group of nodes interconnected by telecommunications links that are used to exchange messages between the nodes. <p> \(__this course__: to be covered by the last part of this course\) <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
  - telecommunications network / motivation ::@:: Point-to-point communications only allow 2 users \(nodes\). A network allows us to connect many users \(nodes\). <p> The simplest way is to add a point-to-point communication between every pair of user. But we would need $n(n - 1) = n^2 - n$ connections, which does not scale to billions of users. So actually, our telecommunications networks are not just networks, but often are _networks of networks_. <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
  - telecommunications network / infrastructure ::@:: _communication links_: copper, fiber, radio, satellite, etc.; has transmission rate \(bandwidth; a distinct concept from "bandwidth" as defined above\) <br/> _hosts_: end systems that need networking; billions of them nowadays <br/> internet service provider \(ISP\) <br/> _routers_: it forward packets \(chunks of data\) <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
  - telecommunications network / network of networks ::@:: The internet is loosely hierarchial. There are 3 tiers of ISPs: international/national \(tier 1\), regional \(tier 2\), and local \(tier 3\). <p> ISPs of lower tiers connect to higher tiers. Tier 1 ISPs peer with each other. Tier 2 ISPs may sometimes also peer with each other. <!--SR:!2025-08-22,15,290!2025-08-22,16,290-->
  - telecommunications network / transmission ::@:: Data needs to move through many layers to reach its destination. A _hop_ is a movement through _exactly_ one layer. <p> There are 3 major methods: _circuit switching_, _message switching_ \(__this course__; not mentioned\), and _packet switching_, with the last one almost always being used nowadays. <!--SR:!2025-08-21,14,290!2025-08-22,15,290-->
- [circuit switching](../../../../general/circuit%20switching.md) ::@:: It is a method of implementing a telecommunications network in which two network nodes establish a dedicated communications channel \(circuit\) through the network before the nodes may communicate. The circuit guarantees the full bandwidth of the channel and remains connected for the duration of the communication session. The circuit functions as if the nodes were physically connected as with an electrical circuit. <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
  - circuit switching / features ::@:: circuit-like performance \(i.e. guaranteed\), link bandwidth, no sharing, setup required before a "call", switch capacity <!--SR:!2025-08-23,16,290!2025-08-22,16,290-->
  - circuit switching / sharing ::@:: Network resources are divided into pieces using multiplexing, e.g. FDM, TDM, etc. <!--SR:!2025-08-22,15,290!2025-08-23,16,290-->
- [packet switching](../../../../general/packet%20switching.md) ::@:: It is a method of grouping data into short messages in fixed format, i.e. packets, that are transmitted over a digital network. It is the primary basis for data communications in computer networks worldwide. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
  - packet switching / features ::@:: Packets from different users share network resources, so they are not exclusive and resources are used as needed. Each packet use the full link bandwidth. No or minimal setup is needed. <!--SR:!2025-08-20,14,290!2025-08-22,16,290-->
  - packet switching / contention ::@:: Because different users share network resources, there may be too many packets using up network resources, causing _congestion_. Packets may need to be _queued_ or even _discarded_. <p> _store and forward_: complete packets move one hop at a time <!--SR:!2025-08-21,14,290!2025-08-22,16,290-->
  - packet switching / sharing ::@:: Since packets are sent without fixed pattern \(due to no or minimal setup in advanced\), and each packet uses the full link bandwidth, so _statistics_ are used to multiplex multiple packets _efficiently_, i.e. _statistical multiplexing_. <!--SR:!2025-08-22,15,290!2025-08-22,16,290-->
  - packet switching / advantages ::@:: When a user is _not_ using network resources, then the network resources is free for other users, i.e. resources are used _on-demand_. So more users can be accommodated \(with the downside that it is possible the shared resources are full when a new user wants to use it\). <p> In comparison, in circuit switching, when a user is _not_ using network resources, the allocated frequency slot and/or time slot cannot be used by other users \(but with the upside that users can use their allocated resources without fear of congestion\). <!--SR:!2025-08-22,16,290!2025-08-21,14,290-->
- telecommunications network
  - telecommunications network / edge ::@:: applications and hosts that use networking <!--SR:!2025-08-23,16,290!2025-08-20,14,290-->
  - telecommunications network / links ::@:: access networks, physical media, etc. \(may be wired or wireless\) <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - telecommunications network / core ::@:: interconnected routers, network of networks, etc. <!--SR:!2025-08-20,14,290!2025-08-20,14,290-->
  - telecommunications network / overview ::@:: users use protocols \(e.g. HTTP, TCP/IP, ethernet, etc.\) to communicate over the network of networks \(loosely hierarchical\) <!--SR:!2025-08-21,15,290!2025-08-23,16,290-->
- communication protocol
  - communication protocol / importance
  - communication protocol / aspects
- [abstraction layer](../../../../general/abstraction%20layer.md) ::@:: a way of hiding the working details of a subsystem. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
  - abstraction layer / networking ::@:: Networks are very complex, as we have seen above. Discussing them all at once is too much. <p> Abstraction layers organize networking into several layers \(_structured_\) so that we can discuss networking layer-by-layer. It also eases maintenance by _modularization_, since interaction between layers are usually standardized, so changes in a layer often does not affect layers. <p> A commonly used model is the _OSI model_. <!--SR:!2025-08-21,14,290!2025-08-22,16,290-->
  - abstraction layer / interactions ::@:: A layer is considered to be on top of another if it depends on it. Every layer can exist without the layers above it, and requires the layers below it to function. Frequently abstraction layers can be composed into a hierarchy of abstraction levels. <!--SR:!2025-08-22,16,290!2025-08-23,16,290-->
- [OSI model](../../../../general/OSI%20model.md) ::@:: It is a reference model developed by the International Organization for Standardization \(ISO\) that "provides a common basis for the coordination of standards development for the purpose of systems interconnection." <!--SR:!2025-08-23,16,290!2025-08-22,15,290-->
  - OSI model / the layers ::@:: \(lowest\) physical, data link, network, transport, session, presentation, application \(highest\) <p> \(__this course__: missing session and presentation\) <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - OSI model / physical ::@:: transmission and reception of raw bit streams over a physical medium <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->
  - OSI model / data link ::@:: transmission of data frames between two nodes connected by a physical layer <p> examples: Bluetooth \(802.11\), ethernet, etc. <!--SR:!2025-08-23,16,290!2025-08-23,16,290-->
  - OSI model / network ::@:: structuring and managing a multi-node network, including addressing, routing and traffic control <p> examples: IP addresses, routing protocols, etc. <!--SR:!2025-08-20,14,290!2025-08-22,15,290-->
  - OSI model / transport ::@:: reliable transmission of data segments between points on a network, including segmentation, acknowledgement and multiplexing <p> examples: TCP, UDP, etc. <!--SR:!2025-08-20,14,290!2025-08-21,14,290-->
  - OSI model / application ::@:: high-level protocols such as for resource sharing or remote file access <p> examples: DNS, FTP, HTTP, SMFTP, etc. <!--SR:!2025-08-22,16,290!2025-08-21,15,290-->
  - OSI model / implementation ::@:: Hosts often implement all layers. Links often implement only up to the network layer \(physical, data link, network\). So the remaining higher layers implemented by hosts but not links are often called _end-to-end layers_. <!--SR:!2025-08-23,16,290!2025-08-21,15,290-->

## week 3 tutorial 2

- datetime: 2025-07-31T11:00:00+08:00/2025-07-31T12:20:00+08:00, PT1H20M
- topic: lab 4 review, lab 5, signal-to-noise ratio, bit error rate
- ELEC 1200
  - ELEC 1200 / lab 4
  - ELEC 1200 / lab 5 ::@:: received signal distribution → bit error rate: transmission distance → bit error rate: threshold → bit error rate: bit time <!--SR:!2025-08-21,14,290!2025-08-23,16,290-->
- [§ week 3 lab 2](#week%203%20lab%202)

## week 3 lab 2

- datetime: 2025-07-31T14:00:00+08:00/2025-07-31T16:50:00+08:00, PT2H50M
- topic: bit errors, signal-to-noise ratio
- status: attendance
- [§ week 3 tutorial 2](#week%203%20tutorial%202)
- ELEC 1200
  - ELEC 1200 / lab 5
    - ELEC 1200 / lab 5 / transmission distance, SNR ::@:: Recall that increasing transmission distance decreases attenuation _k_. It turns out this is exactly the difference between _r_<sub>min</sub> \(when bit is 0\) and _r_<sub>max</sub> \(when bit is 1\). This decreases signal level. However, noise level remains mostly constant. so the signal-to-noise ratio decreases. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - ELEC 1200 / lab 5 / good SNR ::@:: In our experiment, a good SNR to ensure \(practically\) error free transmission is about 15&nbsp;dB. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - ELEC 1200 / lab 5 / threshold ::@:: Assuming the additive noise PDF is symmetric and unbiased. <p> If both bits are equally likely, the minimum bit error rate is achieved when the threshold is in the middle. If bit 0 is more likely, the optimal threshold increases. If bit 1 is more likely, the optimal threshold decreases <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - ELEC 1200 / lab 5 / bit time, noisy output PDF ::@:: With high bit time \(or SPB\), inter-symbol interference \(ISI\) is insignificant. So the noisy output PDF looks like two shifted copies of the noise PDF. With low bit time \(or SPB\), ISI is significant, and the noisy output PDF looks like a single hill-shaped PDF. So bit error rate increases. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - ELEC 1200 / lab 5 / bit time, theoretical/predicted bit error rate ::@:: As the predicted/theoretical bit error rate found using noise PDF does not depend on bit time \(or SPB\), changes in bit time could not affect it. This is because our calculation assumes inter-symbol interference \(ISI\) does not matter. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- assignment: [lab 5](assignments/lab%205/index.md)
- questions: [post lab quiz 5 derivative](questions/post%20lab%20quiz%205%20derivative.md)

## week 3 lab 3

- datetime: 2025-08-01T10:00:00+08:00/2025-07-26T12:50:00+08:00, PT2H50M
- status: unscheduled

## midterm examination

- datetime: 2025-08-01T11:00:00+08:00/2025-08-01T11:50:00+08:00, PT50M
- venue: Lecture Theater D, Academic Building
- format
  - calculator: no
  - cheatsheet: no
  - referencing: closed book
  - provided: \(none\)
  - questions: long questions ×4
- grades: 59/60
  - statistics
    - timestamps: 2025-08-03T22:00:00+08:00
    - mean: ? \(provided: 44\)
    - standard deviation: ? \(provided: 14\)
    - low: ?
    - lower quartile: ?
    - median: ?
    - upper quartile: ?
    - high: ?
    - distribution: ?
- report
  - stop bit \(−1\) ::@:: The stop bit of 1 frame out of 4 was written as 1 instead of 0. Mysterious... <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- check
  - datetime
    - 2025-08-04T10:00:00+08:00/2025-08-04T17:00:00+08:00, PT7H
    - 2025-08-05T10:00:00+08:00/2025-08-05T17:00:00+08:00, PT7H
    - 2025-08-06T10:00:00+08:00/2025-08-06T17:00:00+08:00, PT7H
  - venue: Room 2395, Academic Building \(lift 17, 18\)
  - report: \(none\)

---

> __<big><big>Midterm exam - 11 am on 29 July \(Tue\)</big></big>__
>
> Dear students,
>
> Please be reminded that we will have our midterm exam at 11 am next Tuesday \(29 July\) in LTD.
>
> Covers all materials up to lecture 11 \(inclusive\) <br/>
> Closed book and closed notes <br/>
> 4 questions \(NO MATLAB coding questions\) <br/>
> NO calculator, paper or electronic devices \(including smartwatch\) <br/>
> NO talking/discussing during the exam <br/>
> Seat number will be sent by email later \(not free seating\).
>
> Please bring your student ID card for attendance checking.
>
> Please go to LTD at least 5 minutes before the start time.
>
> Please find some review questions and answers => Midterm Exam - 11 am on 29 July 2025 \(Tue\)
>
> Please let me know if you have any questions.
>
> Thank you,
>
> \[redacted\]

---

> __<big><big>Midterm exam \(rescheduled\)</big></big>__
>
> Dear students,
>
> Due to the black rainstorm this morning, our midterm exam will be rescheduled to:
>
> Date: 1 August 2025 \(Fri\)
>
> Time: 11:00 am - 11:50 am \(same as before\)
>
> Venue: LTD \(same as before\)
>
> The seat number is also the same \(sent by email\).
>
> Please let us know if you have any question.
>
> Take care and stay safe!
>
> \[redacted\]

## week 3 lecture 3

- datetime: 2025-08-01T14:00:00+08:00/2025-08-01T15:50:00+08:00, PT1H50M
- topic: link layer; network layer
- OSI model
  - OSI model / the layers
  - OSI model / data link
- [data link layer](../../../../general/data%20link%20layer.md) ::@:: It is the second layer of the seven-layer OSI model of computer networking. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - data link layer / description ::@:: This layer is the protocol layer that transfers data between nodes on a network segment across the physical layer. It provides the functional and procedural means to transfer data between network entities and may also provide the means to detect and possibly correct errors that can occur in the physical layer. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - data link layer / terminology ::@:: There are _nodes_. There are _links_ between nodes, representing communication channels. A packet is a _frame_, which encapsulates a _datagram_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- OSI model
  - OSI model / packet ::@:: Data are often transmitted in a group of bits. Then, each layer, starting from the top to the bottom \(excluding the physical layer\) adds additional header or trailer information, forming a packet. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - OSI model / packet / names ::@:: application layer: message <br/> transport layer: segment <br/> network layer: datagram <br/> data link layer: frame <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- data link layer
  - data link layer / functions ::@:: error correction, error detection, framing, link access <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - data link layer / framing ::@:: Encapsulate _datagrams_, some data to be transferred, into _frames_ by adding _header_ and _trailer_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - data link layer / link access ::@:: If the communication medium is shared, it also manages channel access \(e.g. timing to avoid interference\). <br/> _MAC addresses_ \(different from _IP addresses_\) is used to identify packet source and destination. It detects or avoids collisions, and determines where frames start and end. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - data link layer / error detection ::@:: Errors are caused by transmission attenuation and noise. The receiver may _detect_ errors, and _requests_ the sender to _retransmit_ or _drop_ the frame. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - data link layer / error correction ::@:: Errors are caused by transmission attenuation and noise. The receiver may _detect_ errors and _correct_ them without frame retransmission or dropping. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - data link layer / implementation ::@:: It is often implemented in an _adapter_ using a _firmware_ \(a type of software\). <p> The sender performs framing and link access. The receiver performs extraction, error detection, and error correction. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - data link layer / shared communication medium ::@:: Multiple devices may be sharing a communication channel. If multiple frames are transmitted simultaneously, interference occurs. The frame is distorted and no one can decode it. <p> So link access also needs to manage channel access if the communication medium is shared to avoid multiple frames being transmitted \(avoid _collisions_\). <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- point-to-point
  - point-to-point / examples ::@:: dial-up access, ethernet switch and host, etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- telecommunications network
  - telecommunications network / examples ::@:: Wi-Fi \(802.11\), cabled ethernet, upstream hybrid fiber coaxial \(HFC\) cable, etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [channel access method](../../../../general/channel%20access%20method.md) ::@:: It allows more than two terminals connected to the same transmission medium to transmit over it and to share its capacity. Examples of shared physical media are wireless networks, bus networks, ring networks and point-to-point links operating in half-duplex mode. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - channel access method / ideal ::@:: There is a channel that has a capacity of _R_. When _M_ nodes are transmitting, each can transmit at an average of _R_/_M_. <p> It should be _fully decentralized_ \(e.g. no coordination, no synchronization, etc.\) and _simple_ to implement. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [media access control](../../../../general/media%20access%20control.md) \(MAC\) ::@:: It is the layer that controls the hardware responsible for interaction with the wired \(electrical or optical\) or wireless transmission medium. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - media access control / OSI model ::@:: The MAC sublayer and the logical link control \(LLC\) sublayer together make up the data link layer. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - media access control / types :@:: 3 major types: channel partitioning, random access, round-robin \("taking turns"\) <!--SR:!2025-08-18,4,310-->
  - media access control / channel partition ::@:: Simply divide the channel into multiple smaller independent "channels". An advantage is _collisions_ cannot happen. A problem is unused smaller "channels" go idle. <p> examples: frequency division multiple access \(FDMA\), time division multiple access \(TDMA\), etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - media access control / channel partition / time division multiple access \(TDMA\) ::@:: A _round_ is a period of time. Each round is divided into many _fixed-length time slots_. Each device gets a time slot for transmission. Unused time slots are idle. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - media access control / channel partition / frequency division multiple access \(FDMA\) ::@:: The channel is a spectrum. It is divided into _frequency bands_. Each devices gets a _fixed frequency band_. Unused frequency bands are idle. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - media access control / random access ::@:: Transmit anyway without explicitly avoiding collisions, but specify a method of collision _detection_ and _recovery_ \(e.g. delayed retransmissions\). <p> examples: CSMA, CSMA/CA, CSMA/CD, pure ALOHA, slotted ALOHA, etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [ALOHAnet](../../../../general/ALOHAnet.md) ::@:: It was a pioneering computer networking system developed at the University of Hawaii. ALOHAnet became operational in June 1971, providing the first public demonstration of a wireless packet data network. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - ALOHAnet / media access control ::@:: ALOHA random access \(ALOHA\), reservation ALOHA, slotted ALOHA, etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - ALOHAnet / slotted ALOHA ::@:: Each packet takes a fixed amount of time. Divide time into slots equal to this time. Packets are only transmitted only at the start of each slot. If a _collision_ occurs, all packets are lost. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - ALOHAnet / slotted ALOHA / advantages ::@:: If only a single node transmit continuously, the _full rate_ is used. It is still \(mostly\) _decentralized_ and _simple_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - ALOHAnet / slotted ALOHA / disadvantages ::@:: _Collisions_ waste slots. Clock _synchronization_ is needed. Unnecessarily idle time slots \(e.g. excludes where no devices need to send data\) are possible. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - ALOHAnet / slotted ALOHA / efficiency ::@:: \# of successful time slots divided by \# of all time slots \(including idle\) <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - ALOHAnet / slotted ALOHA / throughput ::@:: \# of success time slots divided by time interval <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - ALOHAnet / slotted ALOHA / analysis ::@:: Assume nodes are _independent_. Nodes have an _infinite queue_ to store data to be transmitted. If a node has an nonempty queue, it is _backlogged_. <p> We assume _n_ nodes want to transmit data, and each of these node has a probability of _p_ to transmit the data. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
      - ALOHAnet / slotted ALOHA / analysis / efficiency ::@:: In a given time slot, we find the probability that exactly one packet is transmitted, which gives the _efficiency_. It is given by: $$E = \binom n 1 \cdot p \cdot (1 - p)^{n - 1} = n \cdot p \cdot (1 - p)^{n - 1} \,.$$ <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
        - ALOHAnet / slotted ALOHA / analysis / efficiency / maximum ::@:: Differentiate it with respect to $p$ to find $p$ that maximizes $E$ for a fixed $n$: $$\begin{aligned} E & = n \cdot p \cdot (1 - p)^{n - 1} \\ E' & = n (1 - p)^{n - 1} - n(n - 1) p (1 - p)^{n - 2} \\ 0 & = n (1 - p)^{n - 1} - n(n - 1) p (1 - p)^{n - 2} \\ 0 & = (1 - p) - (n - 1) p \\ 0 & = 1 - np \\ p & = 1 / n \,. \end{aligned}$$ Then, we find the limit of $E$ as $n$ approaches infinity: $$\begin{aligned} E & = n \cdot p \cdot (1 - p)^{n - 1} \\ & = n \cdot \frac 1 n \cdot \left(1 - \frac 1 n\right)^{n - 1} \\ & = \frac {n} {n - 1} \left(1 - \frac 1 n \right)^n \,. \end{aligned}$$ The above expression approaches $e^{-1} = 1 / e \approx 0.368$ as $n$ approaches infinity. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - ALOHAnet / slotted ALOHA / transmission probability ::@:: We see that to maximize efficiency, the transmission probability should be $1 / n$, where $n$ is the number of nodes with data to transmit. <p> However, $n$ changes, so the optimal probability also changes. Either _coordination_ is required, or we try to estimate _p_ dynamically, increasing _p_ when collisions are too rare and decreasing _p_ when collisions are too frequent. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- OSI model
  - OSI model / the layers
  - OSI model / network
- [network layer](../../../../general/network%20layer.md) ::@:: It is __layer 3__. It is responsible for packet forwarding including routing through intermediate routers. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - network layer / functions ::@:: addressing, datagram, forwarding, routing <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - network layer / datagram ::@:: Encapsulate _segments_ into _datagrams_ by adding _headers_ and _trailers_. _Routers_ examines these headers to know where to _forward_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - network layer / addressing ::@:: IP \(Internet Protocol\) addresses are used to address the destination. The address identifies the destination so that _datagram networks_ \(e.g. internet\) responsible for sending the datagram or packet can know where to forward. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - network layer / forwarding ::@:: According to the header of a datagram, forward the datagram to the next router \(or destination\). <p> A _forwarding table_ is often used. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - network layer / routing ::@:: Before sending a datagram, determine the path to be taken by the datagram. This data is written to its header. <p> A possible way to model the network for routing is using _graphs_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - network layer / routing / difficulty ::@:: The problem is global, but information \(e.g. link distance\) is local. Further, the situation is dynamic due to changes and faults. It is also difficult to scale to very large networks; indeed, ISPs cooperate to deliver packets. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [graph](../../../../general/graph%20(discrete%20mathematics).md) ::@:: It is a structure consisting of a set of objects where some pairs of the objects are in some sense "related". <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - graph / terminology ::@:: The objects are represented by abstractions called _vertices_ \(also called _nodes_ or _points_\) and each of the related pairs of vertices is called an _edge_ \(also called _link_ or _line_\). <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - graph / diagram ::@:: Typically, a graph is depicted in diagrammatic form as a set of dots or circles for the vertices, joined by lines or curves for the edges. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - graph / network routing ::@:: The vertices are the _routers_. The edges are the _links_ between routers. Each edge has a _weight_, representing the cost of transmission. <p> The resulting graph is a _weighted undirected graph_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - graph / network routing / shortest path ::@:: We want to find the shortest paths starting from the current router to any other router, as to construct a forwarding table. <p> We need to use an _algorithm_, e.g. _Dijkstra's algorithm_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- network layer
  - network layer / routing
    - network layer / routing / nature ::@:: information: decentralized \(cost and topology of "nearby" routers known\), global \(all costs and topology known\) <br/> dynamic: dynamic \(routes change quickly\), static \(routes change slowly\) <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - network layer / routing / link state broadcast ::@:: A _net topology_ used. _Link state broadcast_ is used so that all nodes know all topology and costs. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [Dijkstra's algorithm](../../../../general/Dijkstra's%20algorithm.md) ::@:: A common algorithm for finding the shortest paths between nodes in a weighted graph. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Dijkstra's algorithm / network routing ::@:: The algorithm can be used to find shortest paths starting from a router to any other router. So a router can run this algorithm to find the shortest router to any \("nearby"\) other routers, and this gives a _forwarding table_. <p> A property of this algorithm is running _k_ iterations yields the shortest paths to the _k_ "nearest" routers. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Dijkstra's algorithm / algorithm ::@:: Say we are finding the shortest distance from the vertex _u_ to every other vertices. Start by initializing distances: $d(u) = 0, d(v) = \infty$. Create a priority queue containing all vertices in the graph, ordered by non-decreasing distance $d(v)$. While the priority queue is nonempty, extract the first vertex _v_. For each neighbor _n_ of the vertex _v_, assign $d(n) = \min\set{d(n), d(v) + w(v \rightarrow n)}$. Update the priority queue if needed. Repeat until the queue is empty. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Dijkstra's algorithm / correctness ::@:: To prove the correctness of Dijkstra's algorithm, notice that for a shortest path from _a_ to _z_: _a_ → ... → _y_ → _z_, this implies the path from _a_ to _y_ must also be the shortest between them: _a_ → ... → _y_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Dijkstra's algorithm / this course
    - Dijkstra's algorithm / this course / notation ::@:: \(__this course__: <p> $u$: source <br/> $c(x, y)$: edge weight between $x$ and $y$, or $\infty$ if the edge does not exist <br/> $D(v)$: current path cost from source to $v$ <br/> $p(v)$: predecessor node along current path from source to $v$ <br/> $N'$: set of nodes with known shortest paths\) <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Dijkstra's algorithm / this course / steps ::@:: \(__this course__: We can split the steps into _initialization_, _iteration_, and _extraction_.\) <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
      - Dijkstra's algorithm / this course / steps / initialization ::@:: Set $N' = \set{u}$. For all nodes $v$, set $D(v) = c(u, v)$, which is $\infty$ if there is no edge between $u$ and $v$. If there is an edge between $u$ and $v$, also set $p(v)$ to $u$; otherwise $p(v)$ is _undefined_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
      - Dijkstra's algorithm / this course / steps / iteration ::@:: The below steps are iterated until every node is in $N'$. <p> Find the node $w$ not in $N'$ that has the smallest $D(w)$. $w$ is added to $N'$. Then, for each node $v$ adjacent to $w$, if $D(w) + c(w, v) < D(v)$, update $D(v)$ to the smaller value and set $p(v) = w$. Otherwise, nothing happens. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
      - Dijkstra's algorithm / this course / steps / extraction ::@:: $D(v)$ gives the cost of the shortest path from $u$ to $v$. To find this shortest path, we build this path starting from its destination $v$. Then, prepend $p(w)$, where $w$ is the first node in the path. Repeat this until the first node in the path is $u$. <p> Perform the above steps to find the shortest paths for each destination node. The _forwarding table_ for each destination node is given by the link between the $u$ to the next node in the shortest path for the destination node. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Dijkstra's algorithm / this course / table ::@:: \(__this course__: A table may be used to represent running the algorithm cleanly: ![Dijkstra's algorithm using a table](attachments/Dijkstra's%20algorithm%20-%20table.png) <p> Observe that "step" starts from 0. We stop writing $D(n), p(n)$ when $n$ has been added to $N'$.\) <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [IP address](../../../../general/IP%20address.md) ::@:: It is a numerical label such as _192.0.2.1_ that is assigned to a device connected to a computer network that uses the Internet Protocol for communication. They serve two main functions: network interface identification, and location addressing. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - IP address / interface ::@:: It is _connection_ between host or router and its physical link. A host often has one, while routers have many. <p> Thus, a host often "has" one IP address while routers often "have" many IP addresses. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - IP address / IPv4 addresses ::@:: It has a size of 32 bits, which limits the address space to 4&nbsp;294&nbsp;967&nbsp;296 \(2<sup>32</sup>\) addresses. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - IP address / IPv4 addresses / notation ::@:: They are usually represented in _dot-decimal notation_, consisting of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., _192.0.2.1_. Each part represents a group of 8 bits \(an octet\) of the address. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - IP address / subnetworks ::@:: IP networks may be divided into subnetworks in both IPv4 and IPv6. For this purpose, an IP address is recognized as consisting of two parts: the _network prefix_ in the high-order bits and the remaining bits called the _rest field_, _host identifier_, or _interface identifier_ \(IPv6\), used for host numbering within a network. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - IP address / subnetworks / physical ::@:: Physically, a subnetwork connect devices that can physically reach each other without using the router. <p> So one could identify subnetworks by highlighting contagious networks not going through any routers. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [Classless Inter-Domain Routing](../../../../general/Classless%20Inter-Domain%20Routing.md) \(CIDR\) ::@:: It is a method for allocating IP addresses for IP routing. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Classless Inter-Domain Routing / CIDR notation ::@:: It is a compact representation of an IP address and its associated network mask. CIDR notation specifies an IP address, a slash \('/'\) character, and a decimal number. The decimal number is the count of consecutive leading _1_-bits \(from left to right\) in the network mask. Each 1-bit denotes a bit of the address range which must remain identical to the given IP address. The IP address in CIDR notation is always represented according to the standards for IPv4 or IPv6. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- IP address
  - IP address / IP address assignment ::@:: IP addresses are assigned to a host either dynamically as they join the network, or persistently by configuration of the host hardware or software. Persistent configuration is also known as using a __static IP address__. In contrast, when a computer's IP address is assigned each time it restarts, this is known as using a __dynamic IP address__. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - IP address / IP address assignment / static ::@:: The assignment is hardcoded by system administrators. <p> UNIX: `/etc/rc.config` <br/> Windows: control panel, settings <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - IP address / IP address assignment / dynamic ::@:: Dynamic IP addresses are assigned by network using Dynamic Host Configuration Protocol \(DHCP\). DHCP is the most frequently used technology for assigning addresses. It avoids the administrative burden of assigning specific static addresses to each device on a network. It also allows devices to share the limited address space on a network if only some of them are online at a particular time. Typically, dynamic IP configuration is enabled by default in modern desktop operating systems. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - IP address / IP address assignment / DHCP ::@:: The address assigned with DHCP is associated with a _lease_ and usually has an expiration period. If the lease is not renewed by the host before expiry, the address may be assigned to another device. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
      - IP address / IP address assignment / DHCP / overview ::@:: A host broadcasts "DHCP discover" message to all devices to find a DHCP server. A DHCP server, if any, responds with "DHCP offer" message \(while other hosts ignore\). The host requests an IP address by sending "DHCP request" message to the DHCP server. The DHCP server sends a IP address by responding with "DHCP acknowledgement" message. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - IP address / subnetworks
    - IP address / subnetworks / organizations ::@:: The ISP allocates a portion of its allocated subnetwork to each organization. This portion is allocated by simply using more bits for the network prefix. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - IP address / subnetworks / ISPs ::@:: The ICANN \(Internet Corporation for Assigned Names and Numbers\) allocates addresses, assigns domain names, manages DNS, and resolves disputes. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - IP address / IPv6 addresses ::@:: In IPv6, the address size was increased from 32 bits in IPv4 to 128 bits, thus providing up to 2<sup>128</sup> \(approximately 3.403×10<sup>38</sup>\) addresses. This is deemed sufficient for the foreseeable future. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - IP address / IPv6 addresses / datagram ::@:: Its datagram format also has a fixed-length 40-byte header, which helps with faster forwarding and processing. It also helps to facilitate quality of service \(QoS\). <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->

## week 4 lecture

- datetime: 2025-08-04T14:00:00+08:00/2025-08-04T16:50:00+08:00, PT2H50M
- topic: transport layer; application layer
- OSI model
  - OSI model / the layers
  - OSI model / transport
- [transport layer](../../../../general/transport%20layer.md) ::@:: It is a conceptual division of methods in the layered architecture of protocols in the network stack in the Internet protocol suite and the OSI model. The protocols of this layer provide end-to-end communication services for applications. It provides services such as connection-oriented communication, reliability, flow control, and multiplexing. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - transport layer / sender ::@:: Application _messages_ are broken up into _segments_ to be sent using the network layer. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - transport layer / receiver ::@:: _Segments_ are reassembled into application _messages_ to be processed by the application layer. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - transport layer / protocols ::@:: User Datagram Protocol \(UDP\), Transmission Control Protocol \(TCP\), etc. <p> The two protocols mentioned above are essentially all traffic on the internet nowadays. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - transport layer / protocols / UDP vs TCP ::@:: The former delivers packets unordered and unreliably, but it is easy to implement, as it is a simple extension of IP in the network layer. <p> The latter delivers packets in-order and reliably, and provides addition services, e.g. congestion control, flow control, etc. It is however much harder to implement and requires connection setup. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - transport layer / unavailable functions ::@:: no bandwidth guarantees, no delay guarantees <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - transport layer / vs. network layer ::@:: The former is often implemented by individual processes on hosts only. The latter is often implemented by firmware on hosts and routers. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - transport layer / functions ::@:: basic functions: error detection, multiplexing and demultiplexing; both UDP and TCP have them <br/> advanced functions: congestion control, connection management, flow control, reliability; TCP but not UDP not has them <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [Transmission Control Protocol](../../../../general/Transmission%20Control%20Protocol.md) \(TCP\) ::@:: It is one of the main protocols of the Internet protocol suite. It originated in the initial network implementation in which it complemented the Internet Protocol \(IP\). Therefore, the entire suite is commonly referred to as TCP/IP. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Transmission Control Protocol / characteristics ::@:: connection, oriented \(uses handshaking\), full duplex, ordered \(uses buffering\), point-to-point, reliable \(uses acknowledgements\) <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Transmission Control Protocol / additional services ::@:: congestion control, connection management, flow control, etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [Reliable Data Transfer](../../../../general/Reliable%20Data%20Transfer.md) \(RDT\) ::@:: It is a topic in computer networking concerning the transfer of data across unreliable channels. Unreliability is one of the drawbacks of packet switched networks such as the modern internet, as packet loss can occur for a variety of reasons, and delivery of packets is not guaranteed to happen in the order that the packets were sent. Therefore, in order to create long-term data streams over the internet, techniques have been developed to provide reliability, which are generally implemented in the transport layer of the internet protocol suite. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Reliable Data Transfer / teaching ::@:: In instructional materials, the topic is often presented in the form of theoretical example protocols which are themselves referred to as "RDT", in order to introduce students to the problems and solutions encountered in Transport layer protocols such as the Transmission Control Protocol. These sources often describe a pseudo-API and include Finite-state machine diagrams to illustrate how such a protocol might be implemented, as well as a version history. These details are generally consistent between sources, yet are often left uncited, so the origin of this theoretical RDT protocol is unclear. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Reliable Data Transfer / obstacles ::@:: Characteristics of the unreliable channel affect the protocol complexity, as different obstacles are presented. <p> There are 2 major types of obstacles: lost and out-of-order. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Reliable Data Transfer / obstacles / lost ::@:: queue overflow \(at switches\), repeated collisions, routing failures, uncorrectable bit errors, etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Reliable Data Transfer / obstacles / out-of-order::@:: datagram duplication, different paths taken, variable delays from queueing, etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Reliable Data Transfer / sender ::@:: The sender encapsulates each part of the message into a _segment_. The segment has a _sequence number_ to _identify_ it. Sent segments are saved to a _buffer_. <p> When acknowledgement \(ACK\) is received from the receiver, this segment is removed  from the buffer. Otherwise, the segment is retransmitted if ACK has not been received for some time. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Reliable Data Transfer / receiver ::@:: When the receiver receives the segment, acknowledgement \(ACK\) is sent with the identifying sequence number. The sequence number also ensures the application layer receives the message _in-order_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Reliable Data Transfer / stop-and-wait protocol ::@:: The sender sends the segment _n_ \(starting from 1\). Wait for its acknowledgement \(ACK\). Once ACK is received, increment _n_ by 1, and repeat the above.<p> When the receiver receives the segment _k_. It ACKs the segment with _k_. It also delivers the segment to the application layer. Repeat when it receives another segment. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Reliable Data Transfer / stop-and-wait protocol / packet loss ::@:: The above naive protocol is not resilient to packet loss. If any packet \(including the ACK packet\) is lost, transmission completely stops. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Reliable Data Transfer / stop-and-wait protocol / revised ::@:: The sender sends the segment _n_ \(starting from 1\). Wait for its acknowledgement \(ACK\). If too long has passed, send the same segment again. Once ACK is received, increment _n_ by 1, and repeat the above.<p> The receiver additionally _tracks_ the sequence number of the last received segment, called _m_. When the receiver receives the segment _k_. It _always_ ACKs the segment with _k_. Further, if _k_=_m_+1, deliver the segment to the application layer and update _m_=_k_. Otherwise, the segment is duplicated, thus discarded. It also delivers the packet to the application layer. Repeat when it receives another segment. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Reliable Data Transfer / throughput ::@:: It is the expected number of segments/packets sent per unt time. It is measured in segments/packets per unit time \(e.g. seconds\). <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Reliable Data Transfer / throughput / stop-and-wait protocol ::@:: This requires no packet loss for it to work. Then, its throughput is simply the reciprocal of the _round-trip time_, where the round-trip time is the expected amount of time between starting to send a segment and receiving its corresponding ACK packet. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Reliable Data Transfer / throughput / revised stop-and-wait protocol ::@:: Assume packet is lost with a _round-trip probability_ of _L_. We first find the _effective_ round-trip time _T_ using an algebraic equation: $$T = (1 - L) \cdot \text{RTT} + L \cdot (\text{RTO} + T) \,,$$ where RTO is _retransmission timeout_, the time for the sender to wait before retransmission. We have: $$\begin{aligned} T & = (1 - L) \cdot \text{RTT} + L \cdot (\text{RTO} + T) \\ (1 - L) T & = (1 - L) \cdot \text{RTT} + L \cdot \text{RTO} \\ T & = \text{RTT} + \frac L {1 - L} \text{RTO} \,. \end{aligned}$$ Finally, the throughput is the reciprocal of _T_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Reliable Data Transfer / throughput / retransmission timeout ::@:: We should choose _retransmission timeout_ \(RTO\) such that the probability of transmission is minimized. This happens if RTO &gt; RTT for a particular segment. However, RTT is _random_ in practice, so we need to use _empirical_ statistics to find the ideal RTO. <p> If we assume RTO is constant, then RTT only needs to be larger by an arbitrarily small number, thus RTT = RTO. Then, by the above formula: $$\begin{aligned} T^* & = \text{RTT} + \frac L {1 - L} \text{RTO} \\ & = \text{RTT} + \frac L {1 - L} \text{RTT} \\ & = \frac {\text{RTT} } {1 - L} \,. \end{aligned}$$ And thus the _optimal_ throughput is: $$\text{optimal throughput} = \frac {1 - L} {\text{RTT} } \,.$$ Note that if the RTT is not _optimal_, the throughput will be lower. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Reliable Data Transfer / stop-and-wait protocol
    - Reliable Data Transfer / stop-and-wait protocol / use ::@:: It is a very simple algorithm. <p> It is used when throughput is much less important compared to throughput, or if RTT is small \(e.g. same order of magnitude as the segment transmission time\). <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- OSI model
  - OSI model / the layers
  - OSI model / application
- [application layer](../../../../general/application%20layer.md) ::@:: It is an abstraction layer that specifies the shared communication protocols and interface methods used by hosts in a communications network. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - application layer / "hourglass" ::@:: There are many _network applications_ relying on a few protocols on the transport and network layer \(essentially everything uses the IP protocol\), which in turn may rely on many different types of _link technologies_ on the data link layer. So it looks like a "hourglass". <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - application layer / network applications ::@:: P2P file sharing, Voice over IP \(VoIP\), email, instant messaging, grid computing, video conferencing, web, etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - application layer / architectures ::@:: 3 major types: client–server, peer-to-peer \(P2P\), hybrid of both <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - application layer / architectures / client–server ::@:: The _server_ is _always online_. It often has a _fixed_ IP address. It may be run by a _server farm_. <p> The _client_ intermittently communicates with the server, but not with other clients directly. There can be many clients. Their IP addresses may be _dynamic_. <p> examples: DNS, FTP \(file server\), HTTP, HTTPS, SMTP \(email server\), Telnet \(remote terminal\), etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - application layer / architectures / peer-to-peer \(P2P\) ::@:: There is no "server". _Arbitrary_ hosts directly and intermittently communicate with each other. <p> It is highly _scalable_ but difficult to _manage_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - application layer / architectures / hybrid of both ::@:: Often, clients exchange information about each other using a central server \(client–server\). Once this is done, clients communicate with each other directly \(P2P\). <p> examples: Skype, instant messaging, etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [website](../../../../general/website.md) ::@:: It is any web page whose content is identified by a common domain name and is published on at least one web server. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - websites / objects ::@:: A website consists of many objects, which can be HTML files, audio, images \(e.g. JPEG\), videos, etc. Each object has a _URL_ address. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - websites / index ::@:: A website often has a base HTML file, called the _index_. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [URL](../../../../general/URL.md) ::@:: It is a reference to a resource that specifies its location on a computer network and a mechanism for retrieving it. <p> It consists of protocol prefix, domain name \(also _host name_\), directory path, and document name \(last 2 combined is _path name_\). <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [HTTP](../../../../general/HTTP.md) ::@:: It is an application layer protocol in the Internet protocol suite model for distributed, collaborative, hypermedia information systems. It is the foundation of data communication for the World Wide Web, where hypertext documents include hyperlinks to other resources that the user can easily access, for example by a mouse click or by tapping the screen in a web browser. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - HTTP / full name ::@:: Hypertext Transfer Protocol <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - HTTP / server ::@:: It receives requests and sends web objects. Its _port_ is typically 80. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - HTTP / server / cache ::@:: There may be _web caches_ acting as _proxy servers_. Clients requests from the proxy server instead of the _origin server_. The proxy server returns the requested web objects if cached; if not, request from the origin server, cache it, and returns the web object. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - HTTP / client ::@:: It requests web objects and "displays" them. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [Domain Name System](../../../../general/Domain%20Name%20System.md) \(DNS\) ::@:: It is a hierarchical and distributed name service that provides a naming system for computers, services, and other resources on the Internet or other Internet Protocol \(IP\) networks. <p> Essentially, this allows you to type meaningful domain names instead of hard-to-remember IP addresses to connect other computers. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Domain Name System / characteristics ::@:: application-layer protocol, distributed and hierarchical databases, internet-wide service, short messages \(thus primarily uses UDP\) <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Domain Name System / characteristics / decentralized ::@:: DNS is decentralized. So no servers have all name-to-IP mappings. <p> DNS is decentralized because they do not _scale_ well. A theoretical supercomputer for DNS has poor _manageability_ \(maintain mappings\), poor _performance_ \(location of the server\), and poor _reliability_ \(single point of failure\). <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Domain Name System / local ::@:: On a local network \(e.g. ISP, company\), there are _local name servers_. Every host on the local network is registered with _at least 2 authoritative servers_ that store the host's IP address and domain name. So local name servers can perform translation for local hosts. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Domain Name System / hierarchy ::@:: It is a hierarchical of servers: root name servers, top-level domain \(TLD\) servers, authoritative DNS servers \(local name servers\) <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Domain Name System / hierarchy / root name servers ::@:: Clients use them to find top-level domain servers. <p> As of 2025, there are 13 root name servers worldwide. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Domain Name System / hierarchy / top-level domain servers ::@:: They are responsible for top-level domains \(e.g. `.com`, `.edu`, `.net`, `.org`, etc.\) and country domains \(e.g. `.ca`, `.fr`, `.jp`, `.uk`, etc.\). <p> examples: `.com` \(Network Solutions\), `.edu` \(Educase\), etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
    - Domain Name System / hierarchy / authoritative DNS servers ::@:: They are usually directly below the top-level domain servers. They are specific to an ISP or organization. It is often maintained by the ISP or organization. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Domain Name System / request ::@:: A DNS request is _iterative_ and _recursive_. The client sends DNS requests to DNS servers starting from the root name servers, which either refers to a lower level DNS server and the client repeats the above steps, or translates the domain name if known. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
  - Domain Name System / cache ::@:: To reduce load, mappings are _cached_ for some time. <p> When a name server learns a mapping, it _caches_ it, which disappears after some time. This caching is often implemented in local name servers only, as responses from the root name servers are often cached by the client. <p> There is also a cache notify/update mechanism designed by a IETF working group \(dnsind\), e.g. RFC&nbsp;2136, etc. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->

## week 4 tutorial

- datetime: 2025-08-06T14:00:00+08:00/2025-08-06T15:20:00+08:00, PT1H20M
- topic: lab 6, time–frequency analysis
- status: rescheduled
- ELEC 1200
  - ELEC 1200 / lab 6 ::@:: speech signal → amplitude spectrum → speech signal approximation → channel frequency response <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [§ week 4 lab](#week%204%20lab)

---

> Dear All,
>
> Due to the Black Rainstorm Warning Signal again, we have to rearrange the tutorials and labs as follows:
>
> 1. Tutorial 6 will be postponed to 14:00, this Wednesday \(Aug. 6\). The original Q&amp;A will be continued after the tutorial.
> 2. Lab 6 will be postponed to 14:00-16:50, this Thursday \(Aug. 7\).
> 3. Lab 7 will be a take-home lab. Each student needs to submit an individual mini-report. You can find the template of mini-report on Canvas. The grading of Lab 7 will be based on the mini-report instead of the original check-points and quiz.
> 4. The schedule of Tutorial 7 keeps unchanged.
>
> Please let me know if you have any questions. Take care and be safe!
>
> Regards, <br/>
> \[redacted\]

## week 4 lab

- datetime: 2025-08-07T14:00:00+08:00/2025-08-07T16:50:00+08:00, PT2H50M
- topic: time—frequency analysis
- status: attendance, rescheduled
- [§ week 4 tutorial](#week%204%20tutorial)
- ELEC 1200
  - ELEC 1200 / lab 6
- assignment: [lab 6](assignments/lab%206/index.md)
- questions: [post lab quiz 6 derivative](questions/post%20lab%20quiz%206%20derivative.md)

---

> Dear All,
>
> Due to the Black Rainstorm Warning Signal again, we have to rearrange the tutorials and labs as follows:
>
> 1. Tutorial 6 will be postponed to 14:00, this Wednesday \(Aug. 6\). The original Q&amp;A will be continued after the tutorial.
> 2. Lab 6 will be postponed to 14:00-16:50, this Thursday \(Aug. 7\).
> 3. Lab 7 will be a take-home lab. Each student needs to submit an individual mini-report. You can find the template of mini-report on Canvas. The grading of Lab 7 will be based on the mini-report instead of the original check-points and quiz.
> 4. The schedule of Tutorial 7 keeps unchanged.
>
> Please let me know if you have any questions. Take care and be safe!
>
> Regards, <br/>
> \[redacted\]

## week 4 lecture 2

- datetime: 2025-08-06T14:00:00+08:00/2025-08-06T15:50:00+08:00, PT1H50M
- topic: questions & answers
- [§ week 4 tutorial](#week%204%20tutorial)
- assignment: [homework 3](assignments/homework%203/index.md)

---

> Dear All,
>
> Due to the Black Rainstorm Warning Signal again, we have to rearrange the tutorials and labs as follows:
>
> 1. Tutorial 6 will be postponed to 14:00, this Wednesday \(Aug. 6\). The original Q&amp;A will be continued after the tutorial.
> 2. Lab 6 will be postponed to 14:00-16:50, this Thursday \(Aug. 7\).
> 3. Lab 7 will be a take-home lab. Each student needs to submit an individual mini-report. You can find the template of mini-report on Canvas. The grading of Lab 7 will be based on the mini-report instead of the original check-points and quiz.
> 4. The schedule of Tutorial 7 keeps unchanged.
>
> Please let me know if you have any questions. Take care and be safe!
>
> Regards, <br/>
> \[redacted\]

## week 4 tutorial 2

- datetime: 2025-08-07T11:00:00+08:00/2025-08-07T12:20:00+08:00, PT1H20M
- topic: lab 7, signal transmission using frequency division multiplexing
- ELEC 1200
  - ELEC 1200 / lab 7 ::@:: modulation → demodulation → bandwidth estimation, carrier frequency estimation → multiplexing <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- [§ week 4 lab 2](#week%204%20lab%202)

## week 4 lab 2

- datetime: 2025-08-07T14:00:00+08:00/2025-08-07T16:50:00+08:00, PT2H50M
- topic: frequency division multiplexing
- status: attendance, canceled
- [§ week 4 tutorial 2](#week%204%20tutorial%202)
- ELEC 1200
  - ELEC 1200 / lab 7
- assignment: [lab 7](assignments/lab%207/index.md)
- questions: [post lab quiz 7 derivative](questions/post%20lab%20quiz%207%20derivative.md)
- assignment: [lab 7 mini report](assignments/lab%207%20mini%20report/index.md)

---

> Dear All,
>
> Due to the Black Rainstorm Warning Signal again, we have to rearrange the tutorials and labs as follows:
>
> 1. Tutorial 6 will be postponed to 14:00, this Wednesday \(Aug. 6\). The original Q&amp;A will be continued after the tutorial.
> 2. Lab 6 will be postponed to 14:00-16:50, this Thursday \(Aug. 7\).
> 3. Lab 7 will be a take-home lab. Each student needs to submit an individual mini-report. You can find the template of mini-report on Canvas. The grading of Lab 7 will be based on the mini-report instead of the original check-points and quiz.
> 4. The schedule of Tutorial 7 keeps unchanged.
>
> Please let me know if you have any questions. Take care and be safe!
>
> Regards, <br/>
> \[redacted\]

## week 4 lab 3

- datetime: 2025-08-08T10:00:00+08:00/2025-07-26T12:50:00+08:00, PT2H50M
- status: unscheduled

## week 4 lecture 3

- datetime: 2025-08-08T14:00:00+08:00/2025-08-08T15:50:00+08:00, PT1H50M
- status: unscheduled

## final examination

- datetime: 2025-08-08T10:00:00+08:00/2025-08-08T11:30:00+08:00, PT1H30M
- venue: Lecture Theater D, Academic Building
- format
  - calculator: no
  - cheatsheet: no
  - referencing: closed book
  - provided: Q-function table
  - questions: long questions ×6
- grades: 98/100
  - statistics
    - timestamps: 2025-08-10T22:00:00+08:00
    - mean: ? \(provided: 67\)
    - standard deviation: ? \(provided: 26\)
    - low: ?
    - lower quartile: ?
    - median: ?
    - upper quartile: ?
    - high: ? \(provided: 98\)
    - distribution: ?
- report
  - parity code vs. repetition code \(−2\) ::@:: Misread "\(5, 1\) repetition code" as "\(5, 1\) parity code". Thus two 1-point questions on the maximum number of detectable bit errors and correctable bit errors were wrong. <!--SR:!2025-08-18,4,310!2025-08-18,4,310-->
- check
  - datetime
    - 2025-08-11T10:00:00+08:00/2025-08-11T17:00:00+08:00, PT7H
    - 2025-08-12T10:00:00+08:00/2025-08-12T17:00:00+08:00, PT7H
  - venue: Room 2395, Academic Building \(lift 17, 18\)
  - report: \(none\)

---

> __<big><big>Final exam - 10 am tomorrow \(reminder\)</big></big>__
>
> Dear students,
>
> Please be reminded that we will have our final exam at 10 am tomorrow in LTD.
>
> Covers all course materials <br/>
> Closed book and closed notes <br/>
> 6 questions \(NO MATLAB coding questions\) <br/>
> NO calculator, paper or electronic devices \(including smartwatch\) <br/>
> NO talking/discussing during the exam <br/>
> Seat number: use the same seat number as in the midterm exam
>
> Please bring your student ID card for attendance checking.
>
> Please go to LTD at least 5 minutes before the start time.
>
> Please let me know if you have any questions.
>
> Thank you,
>
> \[redacted\]

## aftermath

### total

- grades: 98.78/100
  - statistics: ?
