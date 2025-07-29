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
  - ELEC 1200 / motivation ::@:: to provide an overview of technologies for communication
  - ELEC 1200 / questions ::@:: How to build smart cities? How to convey information with signals, even with noise? How to detect and recover transmission errors? How to relay information over networks across the world?
  - ELEC 1200 / features ::@:: broad perspective \(cover all aspects of communication\), fundamental \(no prerequisite knowledge\), hands on \(e.g. labs\)
  - ELEC 1200 / logistics
  - ELEC 1200 / course intended learning outcomes \(CILOs\)
  - ELEC 1200 / parts ::@:: point-to-point communication \(one link\), channel sharing \(one link, many users\), network \(many links, many users\)
- [communications system](../../../../general/communications%20system.md) ::@:: It is a collection of individual telecommunications networks systems, relay stations, tributary stations, and terminal equipment usually capable of interconnection and interoperation to form an integrated whole.
  - communications system / basic ::@:: transmitter: source → compress → error correcting coding → bits to waveforms <br/> channel: + noise <br/> receiver: waveforms to bits → error correction → decompress → destination
  - communications system / ideal ::@:: Ideally, the received bits are always the same as the sent bits. But real world noise makes this impossible.
  - communications system / transmitter \(Tx\) ::@:: It converts a sequence of bits into a physical signal or waveform to be carried over a channel.
  - communications system / channel ::@:: It carries a physical signal or waveform. It may be subject to noise due to various factors. <p> examples: air, copper wires, fiber optic cables
  - communications system / receiver \(Rx\) ::@:: It receives a physical signal or waveform and tries to convert it back into the original sequence of bits.
- [bit](../../../../general/bit.md) ::@:: It is the most basic unit of information in computing and digital communication. It represents a logical state with one of two possible values.
  - bit / notation ::@:: These values are most commonly represented as either "1" or "0", but other representations such as _true_/_false_, _yes_/_no_, _on_/_off_, or _+_/_−_ are also widely used.
  - bit / representation ::@:: It can be represented as two distinct states of a physical variable, e.g. current, light, voltage, etc.
    - bit / representation / ease ::@:: There are only two states, so it is easy to use electronics to manipulate them, e.g. logic gates, orientation of tiny magnets to store bits, etc.
  - bit / sequence ::@:: It is a sequence of bits. Physically, they can be represented by holding the corresponding state of the physical variable for a fixed amount of time, called _bit time_, for each bit in the bit sequence. <p> The shorter the bit time, the faster we can transmit information.
- ELEC 1200
  - ELEC 1200 / cutting-edge technologies ::@:: 6G, artificial intelligence, big data, internet of things, etc.
- bit
  - bit / sequence
    - bit / sequence / codeword ::@:: A single bit can only represent variables with two possible values. A combination of _n_ bits, called a _codeword_, can represent variables up to 2<sup>_n_</sp> possible values.
- [binary number](../../../../general/binary%20number.md) ::@:: a method for representing numbers that uses only two symbols for the natural numbers: typically "0" \(zero\) and "1" \(one\)
  - binary number / to decimal number ::@:: $$x = \sum_{k = 0}^{N - 1} 2^k \cdot b_k \,,$$ where $b_{N - 1} b_{N - 2} \cdots b_1 b_0$ is the bit sequence.
  - binary number / most significant bit \(MSB\) ::@:: The bit that represents $2^{N - 1}$. It may be the first bit \(big endian; usually the case when written\), and sometimes it is reversed \(little endian\).
  - binary number / least significant bit \(LSB\) ::@:: The bit that represents $2^0 = 1$. It may be the last bit \(big endian; usually the case when written\), and sometimes it is reversed \(little endian\).
- [ASCII](../../../../general/ASCII.md) ::@:: It is a character encoding standard for electronic communication, used by most computers today. <p> It is a 7-bit code, so there are 128 code points. Each unsigned integer maps to a character. But most of time we use an unsigned byte, which has 8 bits, to represent a character with the MSB set to 0. <p> \(__this course__: Treat it as a 8-bit code.\)
  - ASCII / full name ::@:: American Standard Code for Information Interchange
- bit
  - bit / sequence
    - bit / sequence / endianness ::@:: As mentioned above, a binary number can be represented by a sequence of bits. _Big endian_ means the MSB is transmitted first. _Little endian_ means the LSB is transmitted first.
    - bit / sequence / codewords ::@:: To represent a sequence of codeword, often the bits for each codeword is transmitted contagiously and sequentially in the same order as the original sequence of codeword. \(The ordering of codeword is independent from bit endianness.\)
- communications system
  - communications system / transmitter
  - communications system / channel
  - communications system / receiver
- [bit rate](../../../../general/bit%20rate.md) ::@:: It is the number of bits that are conveyed or processed per unit of time.
  - bit rate / importance ::@:: It is one of the most important _performance_ measure for a communications system.
  - bit rate / units ::@:: It is measured in bits per second \(bps\). Not to be confused with bytes per second \(Bps\)! <p> Metric prefixes may be added, e.g. 1000&nbsp;bps = 1&nbsp;kbps, 1000&nbsp;kbps = 1&nbsp;Mbps, 1000&nbsp;Mbps = 1&nbsp;Gbps, etc.
  - bit rate / bit time ::@:: bit rate = 1/\(bit time\) <p> So shorter bit times increases bit rate.
- [byte](../../../../general/byte.md) ::@:: It is a unit of digital information that most commonly consists of eight bits.
- [signal](../../../../general/signal.md) ::@:: It is both the process and the result of transmission of data over some media accomplished by embedding some variation.
  - signal / classification ::@:: time: continuous time \(CT\), discrete time \(DT\) <br/> value: continuous valued, discrete valued
- [discrete time and continuous time](../../../../general/discrete%20time%20and%20continuous%20time.md) ::@:: They are two alternative frameworks within which variables that evolve over time are modeled.
  - discrete time and continuous time / discrete time ::@:: It views values of variables as occurring at distinct, separate "points in time"
  - discrete time and continuous time / continuous time ::@:: It views variables as having a particular value only for an infinitesimally short amount of time.
- signal
  - signal / discrete time \(DT\) ::@:: The signal has a known value at discrete set of time points. <p> Transmitters and receivers often operate in DT for ease of \(digital\) processing.
  - signal / continuous time \(CT\) ::@:: The signal has a known value at all time points. <p> Channels often operate in CT, as channels are often physical.
- [sampling](../../../../general/sampling%20(signal%20processing).md) ::@:: It is the reduction of a continuous-time signal to a discrete-time signal. A common example is the conversion of a sound wave to a sequence of "samples".
  - sampling / receiver ::@:: Receiver in a communications system often sample the CT signal from the channel to obtain a DT signal for ease of processing.
  - sampling / sampling period and frequency ::@:: Sampling period $T_s$ is the time between each sample, often in seconds \(s\). Sampling frequency $F_s$ is the number of samples per unit of time, often in hertz \(Hz; samples per second\). They are reciprocals of each other: <p> sampling period = 1/\(sampling frequency\)
  - sampling / notation ::@:: CT signal: $x(t)$ <br/> DT signal: $x[n] = x(n T_s)$ \(__this course__: $x(n)$ instead of $x[n]$ is used.\) <br/> sampling frequency: $F_s$ <br/> sampling period: $T_s$
  - sampling / number of samples ::@:: It is the total number of samples of a signal over a finite time window $T_w$. It can be calculated from the sampling period or frequency.
  - sampling / tradeoff ::@:: Higher sampling frequency decreases information loss from the original CT signal after conversion, but increases storage to store the DT signal. \(There are many other tradeoffs not mentioned here.\)
  - sampling / transmitters ::@:: Receivers often perform sampling. Transmitters often perform the "reverse" operation: convert a DT signal to CT signal. <p> This is often done by a hold circuit. For $x[n]$ in DT, its value is held between $x(n T_s)$ and $x((n + 1) T_s)$ in CT, where $T_s$ is the hold period \(of similar nature to sampling period\).
- bit
  - bit / sampling ::@:: A bit can be represented by a fixed number of samples in a DT signal, called _samples per bit_ \(SPB\).
    - bit / sampling / metrics ::@:: Using SPB, we can convert between metrics in terms of bits and those in terms of samples.
- [metric prefix](../../../../general/metric%20prefix.md) ::@:: It is a unit prefix that precedes a basic unit of measure to indicate a multiple or submultiple of the unit. All metric prefixes used today are decadic. Each prefix has a unique symbol that is prepended to any unit symbol.
  - metric prefix / common prefixes ::@:: \(in increasing order of magnitude, each separated by 3 OoMs\) femto-/f ← pico-/p ← nano-/n ← micro-/μ ← milli-/m ← \(unit\) → kilo/k → mega/M → giga/G → tera/T → peta/P
- [waveform](../../../../general/waveform.md) ::@:: It of a signal is the shape of its graph as a function of time, independent of its time and magnitude scales and of any displacement in time.
  - waveform / representations ::@:: sequence of values, sum of unit step functions, graph, verbal description
    - waveform / representations / verbal description ::@:: for communication between people
    - waveform / representations / graph ::@:: for waveform visualization
    - waveform / representations / sequence of values ::@:: for computers, e.g. MATLAB, Python, etc.
    - waveform / representations / sum of unit step functions ::@:: for mathematical analysis of signals when they pass through a channel
- [Heaviside step function](../../../../general/Heaviside%20step%20function.md) ::@:: It is a step function named after Oliver Heaviside, the value of which is zero for negative arguments and one for positive arguments. Different conventions concerning the value _H_\(0\) are in use.
  - Heaviside step function / this course ::@:: \(__this course__: Use $$u(n) = \begin{cases} 0 & n < 0 \\ 1 & 0 \le n \,, \end{cases}$$ i.e. the function is 1 at time 0.\)
  - Heaviside step function / delay ::@:: To delay the step function by _d_ samples, use $u(n - d)$. \(Works for negative _d_ as well, which advances the function.\)
  - Heaviside step function / signal ::@:: It can be used to represent a binary signal, which can only take two values 0 and 1.
    - Heaviside step function / signal / construction ::@:: Assume the signal is 0 initially. Every time the signal changes from 0 to 1 at sample _d_, add $u(n - d)$. Every time the signal changes from 1 to 0 at sample _d_, subtract $u(n - d)$. <p> Note this means the step function must be added and subtracted alternatively in order for the signal to be binary \(either 0 or 1\).
- communications system
  - communications system / transmitter
  - communications system / channel
  - communications system / receiver
  - communications system / channel
    - communications system / channel / discrete time ::@:: Almost all channels are continuous time due to their physical nature. <p> However, assuming both the transmitter and receiver work in discrete time, we can treat the CT channel and conversions between CT and DT as a _black box_. Then the CT channel is simplified to be a DT channel.
- [mathematical model](../../../../general/mathematical%20model.md) ::@:: It is an abstract description of a concrete system using mathematical concepts and language.
  - mathematical model / signal ::@:: A mathematical model can be used to model the effect of a channel on the transmitted signal.
  - mathematical model / goodness ::@:: A good model should be accurate, i.e. its prediction is close to actual observations. It should also be simple.
  - mathematical model / motivation ::@:: It allows us to understand a system, predict its performance, and improve its performance.
- [communication channel](../../../../general/communication%20channel.md) ::@:: It refers either to a physical transmission medium such as a wire, or to a logical connection over a multiplexed medium such as a radio channel in telecommunications and computer networking.
  - communication channel / effects ::@:: 5 primary effects \(that we will learn now\): attenuation \(decrease in amplitude\), blurring \(of transition\), delay, noise, offset
  = communication channel / attenuation, delay, offset ::@:: A very simple model to model attenuation, delay, and offset: $$y[n] = k \cdot x[n - d] + c \,,$$ where $k$ is amplitude scaling \(&lt; 1 for attenuation\), $d$ is delay, and $c$ is offset \(output signal when input signal is 0\).
  - communication channel / blurring ::@:: A bit sequence converted into a waveform requires instantaneous changes when the bit changes. However, physical limitations in electronics, mediums, sensors, transducers, etc., often the received waveform has this instantaneous change blurred. We say such a channel is _bandlimited_.
    - communication channel / blurring / graph ::@:: Graph the transmitted signal against a blurred received signal. We see when the transmitted signal changes _instantaneously_ due to a bit change, the received signal also changes but _gradually_, only approaching the desired signal after several samples.
    - communication channel / blurring / samples per bit ::@:: Assuming only samples per bit \(SPB\) changes, i.e. the channel remains unchanged. Then we see the blurring effect remains the same in its transition speed. If the SPB is too low, then the received signal may not approach the desired signal enough before the bit changes again.
  - communication channel / modeling ::@:: The model mentioned above only handles attenuation, delay, and offset. How can we handle blurring? <p> If we assume the channel is _linear_ and _time-invariant_, making it a _linear time-invariant system_, then we can also model blurring with a _step response function_. This makes use that any input can be expressed as the sum of unit step functions. <p> \(__this course__: We will only talk about very simple step response functions.\)

## week 1 tutorial

- datetime: 2025-07-15T11:00:00+08:00/2025-07-15T12:20:00+08:00, PT1H20M
- topic:

## week 1 lab

- datetime: 2025-07-15T14:00:00+08:00/2025-07-15T16:50:00+08:00, PT2H50M
- status: unscheduled

## week 1 lecture 2

- datetime: 2025-07-16T14:00:00+08:00/2025-07-16T15:50:00+08:00, PT1H50M
- topic: linear time invariant systems, transmitting data
- [linear time-invariant system](../../../../general/linear%20time-invariant%20system.md) \(LTI system\) ::@:: It is a system that produces an output signal from any input signal subject to the constraints of linearity and time-invariance; these terms are briefly defined in the overview below.
  - linear time-invariant system / system ::@:: \(__this course__: We consider a specific context. It is something that takes a waveform and produces a waveform, e.g. channels, etc.\)
  - linear time-invariant system / linearity ::@:: The relationship between the input and the output is a linear mapping. That is, the output for the sum of any two inputs is the sum of their two respective outputs: $$x(t) = x_1(t) + x_2(t) \implies y(t) = y_1(t) + y_2(t) \,.$$ This can be repeated applied to get the output for the sum of any number of inputs.
    - linear time-invariant system / linearity / homogeneity ::@:: The above property is also called _additivity_. _Homogeneity_ is related to additivity, where the two functions are the same: $$x'(t) = c \cdot x(t) \implies y'(t) = c \cdot y(t) \,,$$ for some constant $c$. When $c$ is an integer, it is a special case of additivity.
  - linear time-invariant system / time-invariant ::@:: It means that whether we apply an input to the system now or _T_ seconds from now, the output will be identical except for a time delay of _T_ seconds: $$x'(t) = x(t - T) \implies y'(t) = y(t - T) \,.$$
- [step response](../../../../general/step%20response.md) ::@:: It of a system in a given initial state consists of the time evolution of its outputs when its control inputs are Heaviside step functions.
  - step response / notation ::@:: \(__this course__: Use $s(n)$.\)
  - step response / LTI system ::@:: For LTI systems, the step response $s(n)$ can be used to find the output for any input. <p> Write the input as a sum of \(potentially scaled and/or delayed\) unit step functions. Then replace $u$ with $s$, i.e. replace $c \cdot u(n - d)$ with $c \cdot s(n - d)$. This makes use of the properties of LTI system.
  - step response / exponential ::@:: It can model amplitude scaling \(_k_ &lt; 1 for attenuation\), blurring \(_a_ &lt; 1\), and propagation delay \(_d_\): $$s(n) = k\left(1 - a^{n - d + 1}\right) u(n - d) \,.$$ <p> _k_ simply scales the resulting amplitude. _d_ simply delays \(for negative values, advances\) the response. _a_ &lt; 1 models the transition speed, with values closer to 1 slowing down the transition.
    - step response / exponential / _a_ ::@:: When _n_ = _d_ \(when the transition starts\), we see $$s(d) = k \left(1 - a^{d - d + 1}\right) u(d - d) = k (1 - a) \,.$$ So _theoretically_, $1 - a$ should be the amplitude of the output signal relative to the full amplitude when the transition starts. <p> In practice, noise makes this impractical to find _a_, as even small errors in _a_ can lead to drastic changes in the step response. Trial-and-error is needed.
  - step response / noise, offset ::@:: The step response does _not_ model noise and offset. For offset, we can simply add it to the output signal. For noise, probability will be needed and introduced later, but it is also linearly added to the signal.
- communication channel
  - communication channel / noise, offset ::@:: They are often introduced by the environment, e.g. other users, etc.
- [communication protocol](../../../../general/communication%20protocol.md) ::@:: It is a system of rules that allows two or more entities of a communications system to transmit information via any variation of a physical quantity.
  - communication protocol / importance ::@:: Using the same protocol for both the transmitter and the receiver allows the receiver to understand the transmitted data properly.
  - communication protocol / aspects ::@:: all aspects needed to communicate <p> examples: bit endianness \(LSB or MSB\), bit representation \(e.g. 0 is off and 1 is on\), bit time \(or SPB\), synchronization method, text encoding \(e.g. ASCII, Unicode\), training sequence
- bit
  - bit / decoding ::@:: To decode a bit, we need to make use of sub-sampling, thresholding, and training sequence.
    - bit / decoding / thresholding ::@:: Assume the transmitted data is binary. Then a threshold is decided, for which the data is 1 if the signal is greater than or _equal to_ the threshold, and otherwise 0. <p> A good threshold is $c + k / 2$, where _c_ is the offset and _k_ is the amplitude.
    - bit / decoding / sub-sampling ::@:: A bit is sent using SPB number of samples. This technique means we only consider a subset of the samples for each bit. <p> Due to blurring of transition, we often use the last sample of a bit to ensure the output is far above or below the threshold.
    - bit / decoding / training sequence ::@:: The receiver needs to know _c_ and _k_, but these two parameters may change over time. <p> This sequence allows the receiver to estimate _c_ and _k_. It is known to both the transmitter and receiver in advance, and cannot carry data. <p> A simple training sequence is simply sending the bit 1 for some time, and then send the bit 0 for some time.
      - bit / decoding / training sequence / estimation ::@:: _c_ and _k_ is estimated from the training sequence. A good choice is to set _c_ as the minimum of the step response, and _k_ as the difference between the minimum and maximum.
      - bit / decoding / training sequence / pulse width ::@:: It is the time or number of samples the bit 1 is sent in our simple training sequence. <p> Shorter pulse width means more time to transmit data, as less time is used on the training sequence. Longer pulse width means better _c_ and _k_ estimation. The pulse width is set based on _a_ of the \(assumed\) exponential step response so that the output signal is very close the actual maximum before the pulse stops. \(_a_ closer to 1 means the pulse width should be longer.\)
        - bit / decoding / training sequence / pulse width / calculation ::@:: Assuming the output signal is $$y(n) = c + k\left(1 - a^{n + 1}\right) \,.$$ \(Offset the signal so that delay $d$ is not needed.\) Then we solve for $n$ such that $$y(n) > c + b k \implies 1 - a^{n + 1} > b \,,$$ where $b$ is the desired amplitude relative to full amplitude \(often 0.9\). \(__this course__: The lecture slides say $n + 1$ is the pulse width...\)
- [asynchronous communication](../../../../general/asynchornous%20communication.md) ::@:: It is transmission of data, generally without the use of an external clock signal, where data can be transmitted intermittently rather than in a steady stream.
  - asynchronous communication / motivation ::@:: If the data is transmitted in a steady stream, we just need to keep the clock of both the transmitter and receiver synchronous. <p> But what if it is not? Then we simply also transmit signals used for timing, e.g. framing, etc.
- [frame](../../../../general/frame%20(networking).md) ::@:: It is a digital data transmission unit in computer networking and telecommunications.
  - frame / features ::@:: A frame typically includes frame synchronization features consisting of a sequence of bits or symbols that indicate to the receiver the beginning \(__this course__: _start bits_\) and end \(__this course__: _stop bits_\) of the payload data within the stream of symbols or bits it receives. <p> Note that a frame includes the start and stop bits apart from the data bits.
  - frame / start bits ::@:: The start bit\(s\) is chosen to be either 0 or 1 such that the output signal should be different from the output idle channel; otherwise there is no way to distinguish the start of a frame from idleness. Typically, the bit is 1 because the idle channel usually represents 0.
  - frame / data block ::@:: The number of bits in a data block should in the protocol, agreed in advanced by the transmitter and receiver. <p> example: RS-232 used in PCs usually uses 8 data bits
    - frame / data block / padding, splitting ::@:: The number of bits to transmit may not be a multiple of the number of data bits in a data block. This can be fixed by padding \(add 0s to the end\) and splitting \(split the bits into multiple data blocks inside multiple data frames\).
  - frame / stop bits ::@:: To detect a start bit after the end of a frame, we add stop bits, which is the same as the idle channel; otherwise we cannot distinguish the start bit of the next frame from the stop bits.
    - frame / stop bits / tradeoff ::@:: More stop bits means more time to process a data block in a frame before receiving the next frame. It reduces the data transmission rate because more bits are used on the stop bits.
- ELEC 1200
  - ELEC 1200 / protocol ::@:: We can consider the protocol to be used in our lab from the transmitter and receiver perspective separately.
    - ELEC 1200 / protocol / transmitter ::@:: training sequence <br/> frames: 1 start bit, 1280 \(160 bytes\) of data bits, 1 stop bit
    - ELEC 1200 / protocol / receiver ::@:: training sequence: find _c_ and _k_ <br/> sub-sampling: SPB1, i.e. the last sample of a bit <br/> frame: skip 1 start bit, read 1280 bits as data

## week 1 tutorial 2

- datetime: 2025-07-17T11:00:00+08:00/2025-07-17T12:20:00+08:00, PT1H20M
- topic:

## week 1 lab 2

- datetime: 2025-07-17T14:00:00+08:00/2025-07-17T16:50:00+08:00, PT2H50M
- topic: introduction to MATLAB
- status: attendance
- assignment: [lab 1](assignments/lab%201/index.md)
- questions: [post lab quiz 1 derivative](questions/post%20lab%20quiz%201%20derivative.md)

## week 1 lab 3

- datetime: 2025-07-18T10:00:00+08:00/2025-07-18T12:50:00+08:00, PT2H50M
- topic:
- status: attendance
- assignment: [lab 2](assignments/lab%202/index.md)
- questions: [post lab quiz 2 derivative](questions/post%20lab%20quiz%202%20derivative.md)

## week 1 lecture 3

- datetime: 2025-07-18T14:00:00+08:00/2025-07-18T15:50:00+08:00, PT1H50M
- topic: inter-symbol interference, eye diagram; feedback model of the channel
- bit rate
- [bit error rate](../../../../general/bit%20error%20rate.md) \(BER\) ::@:: The __bit error rate__ \(__BER__\) is the number of bit errors per unit time. The __bit error ratio__ \(also __BER__\) is the number of bit errors divided by the total number of transferred bits during a studied time interval. Bit error ratio is a unitless performance measure, often expressed as a percentage. <p> \(__this course__: __Important__. We use the _bit error ratio_, but we call it _bit error rate_. Funny, isn't it?\)
  - bit error rate / objective ::@:: This should be \(reasonably\) low. This is done by setting a maximum limit on the average BER.
  - bit error rate / tradeoff ::@:: In general, BER increases as bit time decreases \(i.e. bit rate increases\). Usually, starting from the lowest possible bit time, BER is high, and decreases slowly at first, then decreases quickly, then decreases slowly again as it approaches zero, and then becomes \(practically\) zero. <p> More noise or less powerful signal \(less power for transmission\) also increases BER.
- linear time-invariant system
- step response
  - step response / LTI system
- [intersymbol interference](../../../../general/intersymbol%20interference.md) \(ISI\) ::@:: It is a form of distortion of a signal in which one symbol \(__this course__: one bit\) interferes with subsequent symbols \(__this course__: subsequent bits\). This is an unwanted phenomenon as the previous symbols have a similar effect as noise, thus making the communication less reliable.
  - intersymbol interference / bandlimited channels ::@:: As the channel is bandlimited, the output signal requires time to transit when the input bits changes in a bit sequence. <p> Bit errors occur when not enough time is given for this transition to cross the threshold before the next bit \(transmission\) is transmitted. <p> In framing, if bit errors occur at the start bits \(e.g. 1 received as 0\), then _synchronization errors_ occur, which may result in a frame being offsetted by several or many samples, or not received at all.
    - intersymbol interference / bandlimited channels / bit time ::@:: Shorter bit time means more past past symbols _interfere_ with the current symbol, leading to a larger variety of output responses when a bit is transmitted.
- [settling time](../../../../general/settling%20time.md) ::@:: It of a dynamical system such as an amplifier or other output device is the time elapsed from the application of an ideal instantaneous step input to the time at which the amplifier output has entered and remained within a specified error band.
  - settling time / this course ::@:: \(__this course__: Assume the transmitted bit changes from 0 to 1. It is the time or number of samples it takes for the response to get 90% of the way to the maximum amplitude. It can be calculated as: $$n_s = \frac {\ln 0.1} {\ln a} - 1 \,,$$ where _a_ is the parameter in exponential step response, and sample 0 is the first sample of a bit.\)
- intersymbol interference
  - intersymbol interference / response variety ::@:: Assuming only the bit time \(or SPB\) is changed, i.e. the channel remains unchanged. The the number of bits for the output signal remains the same. However, more previous bits may interfere with the current bit as each bit takes less sample. So the response variety increases, which depends on the starting sample position. <p> By symmetry, the response variety for transitions from 1 to 0 should be similar to transitions from 0 to 1.
  - intersymbol interference / solution ::@:: Either make the channel respond faster \(increase bandwidth\) or increase bit time \(or SPB\). <p> The former may require control over the channel and incur extra cost. The latter reduces bit rate.
- [eye diagram](../../../../general/eye%20pattern.md) ::@:: It is an oscilloscope display in which a digital signal from a receiver is repetitively sampled and applied to the vertical input \(_y-axis_\), while the data rate is used to trigger the horizontal sweep \(_x-axis_\).
  - eye diagram / name ::@:: It is so called because, for several types of coding, the pattern looks like a series of eyes between a pair of rails.
  - eye diagram / use ::@:: It can summarize the effect of intersymbol interference by showing all responses to bit 0 and 1 _simultaneously_. <p> \(__this course__: Overlay plots of 2\*SPB+1 samples \(both ends inclusive\), each of distance 2\*SPB samples.\)
  - eye diagram / measurements ::@:: eye \(the empty space in the middle, if any\): eye height, eye width
  - eye diagram / bit time ::@:: As bit time \(or SPB\) decreases, both the eye height and width decreases \(the eye begins to "closes"\), until it "closes" completely. <p> Shorter eye width means the exact sample to sub-sample a bit becomes more important. No eye means there is no sample to sub-sample to avoid any bit errors, i.e. BER cannot be zero.
- ELEC 1200
  - ELEC 1200 / protocol
- bit rate
- bit error rate
- intersymbol interference
- eye diagram
- [equalization](../../../../general/equalization%20(communications).md) ::@:: It is the reversal of distortion incurred by a signal transmitted through a channel. <p> It will cause the eye in the eye diagram to "open".
  - equalization / derivation ::@:: To derivate the formula to equalize the output signal, we need to model the output signal from the input signal, which usually gives a formula. Then, we invert the model to model the input signal from the output signal, which usually involves manipulating the original formula.
    - equalization / derivation / problem ::@:: Given a step response, it is hard to derive the reverse formula for equalization. <p> Either advanced mathematical techniques \(__this course__: not taught in this course\) are needed, or we can use an equivalent but _recursive_ model, which is amendable to elementary algebraic manipulation.
- mathematical model
  - mathematical model / equivalent models ::@:: There may be many equivalent models. That is, they make the same prediction for the same inputs. <p> The different equivalent models are useful in different situations.
  - mathematical model / recursive model ::@:: \(__this course__: A recursive model defines the $n$-th output sample in terms of \(one\) past samples. It also requires an initial starting sample at any $n$\)
- step response
  - step response / exponential
    - step response / exponential / recursive ::@:: An recursive but equivalent way to express the exponential step response: $$y(n) = a \cdot y(n - 1) + (1 - a) \cdot k \cdot x(n) \,,$$ where _k_ is the amplitude scaling and _a_ still has the same meaning as the original step response. An initial starting condition at any $n$ is also needed, e.g. $y(0) = c$ \($n$ does not need to be 0\). <p> The corresponding system implementing this model is known as a _feedback system_.
      - step response / exponential / recursive / interpretation ::@:: The above formula takes the weighted average of the last output sample and the scaled current input sample. <p> $a$ controls the weights, with $a = 0$ means the channel has no memory \(uses the scaled current input sample\) while $a = 1$ means the channel has infinite memory \(constant output and ignores input\).
    - step response / exponential / equivalency ::@:: To prove the step response is equivalent to and the recursive model, we prove the latter model is linear time-invariant \(additivity, homogeneity, time invariance\), and has the same step response. <p> The latter \(same step response\) can be proved by, given the same input samples, calculate the output samples for both models and observe that they are equal for all samples. A rigorous proof uses induction. \(__this course__: The rigorous proof is optional.\)

## week 2 lecture

- datetime: 2025-07-21T14:00:00+08:00/2025-07-21T16:50:00+08:00, PT2H50M
- topic: channel equalization; noise
- equalization
  - equalization / derivation
- step response
  - step response / exponential
    - step response / exponential / recursive
- equalization
  - equalization / exponential step response ::@:: Using the recursive model: $$y(n) + a \cdot y(n - 1) + (1 - a) \cdot k \cdot x(n) \,,$$ we can algebraically manipulate it to become: $$x(n) = \frac 1 k \frac 1 {1 - a} (y(n) - a \cdot y(n - 1)) \,.$$ And we can reverse the above algebraic manipulation as well.
    - equalization / exponential step response / interpretation ::@:: The equalizer is $$\begin{aligned} x(n) & = \frac 1 k \frac 1 {1 - a} (y(n) - a \cdot y(n - 1)) \\ & = \frac 1 k \frac 1 {1 - a} ((1 - a) \cdot y(n) + a y(n) - a \cdot y(n - 1)) \\ & = \frac 1 k \left(y(n) + \frac a {1 - a} (y(n) - y(n - 1)) \right) \,. \end{aligned}$$ We observe the $\frac 1 k$ outside simply undo the scaling. We also observe that the equalizer "boost" the transition by adding the change in output multiplied by $\frac a {1 - a}$, which is 0 when $a = 0$ \(no memory thus instantaneous response, so no need to "boost"\) and infinite when $a = 1$ \(infinite memory thus constant output, so need infinite "boost" \(but this will not work mathematically\)\).
    - equalization / exponential step response / parameters ::@:: Ideally, _k_ and _a_ should be the same as that as the channel. However, in practice, this needs to be estimated.
      - equalization / exponential step response / parameters / errors ::@:: Usually, _k_ can be estimated accurately. So we only consider estimation errors in _a_. <p> If equalization _a_ is larger than that of the channel, the equalizer is too aggressive and overshooting occurs. If equalization _a_ is smaller than that of the channel, the equalizer is too passive and it takes longer than optimal to respond to changes in the input signal. Otherwise, optimal result is obtained.
- eye diagram
  - eye diagram / equalization ::@:: Generally, after equalization, the eye usually opens \(sometimes even if the eye does not appear for the original eye diagram\). <p> Below, we split the effects of equalization on the eye diagram into with no noise and with noise.
    - eye diagram / equalization / no noise ::@:: With no noise and correct equalization _a_, we see the eye diagram is almost optimal \(instantaneous switching\). The eye is almost optimal. <p> If equalization _a_ is too high \(higher than that of the channel\), then overshooting occurs. Values beyond the normal output range is seen when the bit changes. <p> If equalization _a_ is too low, then it takes longer than optimal to respond to changes in the input signal. The eye in the eye diagram is not open as wide and high as it could be.
    - eye diagram / equalization / noise ::@:: With noise, most things are the same for no noise. However, the eye borders are much thicker, which reduces the eye height rather than increase it. <p> The eye borders are also very spiky. This is because the equalizer amplifies noise, as noise also causes changes in the output signal too! Errors in equalization _a_ would further magnify this noise.
- equalization
  - equalization / exponential step response
    - equalization / exponential step response / robustness ::@:: We see even if the equalization _a_ is not the same as the channel _a_, equalization still works, just not as optimal. This shows equalization is _robust_.
- communication channel
  - communication channel / noise
- [noise](../../../../general/noise%20(signal%20processing).md) ::@:: It is a general term for unwanted (and, in general, unknown) modifications that a signal may suffer during capture, storage, transmission, processing, or conversion.
  - noise / importance ::@:: It is very important in communications system. It is everywhere. Often, it looks like very random zig zag lines on a graph, a _random signal_. <p> If there were no noise, data transmission would only need very very little power, since no matter how weak the signal is, it can be distinguished and then amplified. Then we would make the signal strength as small as possible to save energy. <p> With noise, the signal-to-noise ratio becomes important, because a high enough value is needed to distinguish signal from noise. This determines a _minimum signal strength_ for decoding.
  - noise / sources ::@:: It is everywhere. It occurs naturally in nature. The most often source is _thermal noise_, e.g. atmosphere, devices, resistors, etc., as thermal noise disturbs electrons causing random voltages and emissions.
  - noise / statistics ::@:: While noise looks quite random for a few samples, we can collect statistics for a large number of samples. <p> We can create a _histogram_, plotting a percentage of sample around a sample value \(_y_-axis\) for each sample value \(_x_-axis\).
    - noise / statistics / probability density function ::@:: We can create a _histogram_, plotting a percentage of sample around a sample value \(_y_-axis\) for each sample value \(_x_-axis\). <p> By collecting more samples \(and making the histogram bars narrower\), it gets increasingly smooth. By also dividing the original histogram height by its original histogram width and let it be the new histogram height, this function approaches a _probability density function_ \(pdf\) $f_X(x)$. \(__this course__: The slides are missing "dividing the histogram height" to normalize the heights.\)
- [probability density function](../../../../general/probability%20density%20function.md) \(PDF, pdf\) ::@:: It of an _absolutely continuous_ random variable is a function whose value at any given sample \(or point\) in the sample space \(the set of possible values taken by the random variable\) can be interpreted as providing a _relative likelihood_ that the value of the random variable would be equal to that sample. <p> Probability density is the probability per unit length, in other words, the _absolute likelihood_ for a continuous random variable to take on any particular value is 0 since there is an infinite set of possible values to begin with. <p> It is commonly denoted $f_X(x)$ for an absolutely continuous random variable _X_.
  - probability density function / properties ::@:: It is always nonnegative \(__this course__: the slide uses "positive"\). The total area under the function is 1.
  - probability density function / probability ::@:: The probability that a sample lies in between $x_1$ \(exclusive\) and $x_2$ \(inclusive\) \(__this course__: the slide uses exclusive for both\) is the area under the function between $x_1$ and $x_2$. <p> In general, integration is required to find this area. \(__this course__: Our PDF consists of only simple shapes for which their areas have formulas.\)
- noise
  - noise / additive ::@:: There are many ways noise can modify the output signal. The simplest way is that the noise is added to the quiet output signal, thus the noise is _additive_, also called _additive noise_.
  - noise / effect ::@:: If the noise is large enough, the noisy output signal can fall on the wrong side of the threshold, so the bit is read wrongly.
- bit error rate
  - bit error rate / analysis ::@:: The BER can be calculated theoretically from a model of the channel. The model can be very complicated. \(__this course__: We consider a simple model.\)
    - bit error rate / simple model ::@:: The model simplifies the transmitter and receiver model even further. Now we only consider the input bits at the transmitter and the output bits at the receiver, and everything else in between is a black box called the _binary channel_.
      - bit error rate / simple model / assumptions ::@:: The simple model assumes additive white Gaussian noise \(AWGN\), no ISI, perfect synchronization \(i.e. the start bit cannot be read wrongly\), single sample sub-sampling \(one sample to decode one bit\). <p> The AWGN requirement can be relaxed easily. Others are harder. <p> The assumptions are important so that each bit only considers one sample and its error probability are independent of other bits \(no ISI\).
      - bit error rate / simple model / binary channel ::@:: Ideally, the input bit always equal the output bit. Whenever they are not equal, a _bit error_ occurs.
      - bit error rate / simple model / probability ::@:: The BER is: $$\begin{aligned} \text{BER} & = P(I = 0) P(O = 1 \mid I = 0) + P(I = 1) P(O = 0 \mid I = 1) \\ & = P(I = 0, O = 1) + P(I = 1, O = 0) \,, \end{aligned}$$ where $P(I = x)$ is the probability of the input bit being $x$, $P(I = x, O = y)$ is the probability of the input bit being $x$ and the output bit being $y$, and $P(O = y \mid I = x)$ is the _conditional_ probability of the output bit being $y$ given the input bit is $x$. <p> Since the bit is either 0 or 1, $P(I = 1)$ can be replaced with $1 - P(I = 0)$, and vice versa. $P(O = 1 \mid I = x)$ can be replaced with $1 - P(O = 0 \mid I = x)$ for fixed $x$, and vice versa.
      - bit error rate / simple model / this course ::@:: \(__this course__: We use simpler notations: $$\text{BER} = P_e = P[\text{IN} = 0] \cdot P_{e0} + P[\text{IN} = 1] \cdot P_{e1} \,,$$ where the meanings can be inferred from above.\)
      - bit error rate / simple model / error types ::@:: We see there are two types of errors: input bit is 0 but output bit is 1; and input bit is 1 but input bit is 0.
  - bit error rate / computation ::@:: We can compute the BER theoretically or empirically. <p> To calculate the BER empirically, simply observe a channel for some time, find the number of errors, and either divide by time for the rate or number of transmitted bits for the ratio. \(__this course__: __Important__. Remember "bit error rate" in this course is actually the _bit error ratio_.\)
  - bit error rate / simple model
    - bit error rate / simple model / factors ::@:: To find BER for this simple model, we need to know the input bit probabilities and the conditional error probabilities. <p> Often, the input bit probabilities are assumed equal.
  - bit error rate / factors ::@:: The input bit probabilities are controlled by the transmitter and data to be transmitted. The conditional error probabilities depends on noise level, threshold, transmit levels, etc.
- [power](../../../../general/power%20(physics).md) ::@:: It is the amount of energy transferred or converted per unit time. In the International System of Units, the unit of power is the watt, equal to one joule per second. Power is a scalar quantity.
  - power / energy, time ::@:: power = energy / time
  - power / usable time ::@:: usable time = energy / power consumption
  - power / batteries ::@:: They contain a fixed amount of energy. Often, it has a fixed voltage in volts \(V\) and a charge capacity in milliamp-ours \(mAh\). Multiply these two together to get its energy in millwatt-hours \(mWh\).
- [normal distribution](../../../../general/normal%20distribution.md) ::@:: It is important in statistics and is often used in the natural and social sciences to represent real-valued random variables whose distributions are not known. Their importance is partly due to the central limit theorem. It is denoted $\mathcal N(\mu, \sigma^2)$, where $\mu \in \mathbb R$ is the mean and $\sigma^2 \in \mathbb R_{> 0}$ is the variance. <p> \(When you see $\mathcal N(0, 100)$, do not mistake the 100 as the standard deviation!\)
  - normal distribution / applications ::@:: Brownian motion, transmission noise, voltage across a resistor, etc.
  - normal distribution / mean ::@:: Its average value over many samples. It is the central location of its PDF. <p> Changing it simply shifts the PDF.
  - normal distribution / standard deviation ::@:: A measure of how "spread out" the samples are. It measures how wide the PDF is. <p> It is the square root of variance. <p> Increasing it widens the PDF, and also flattens it so that the area under the PDF remains 1.
  - normal distribution / variance ::@:: Also a measure of how "spread out" the samples are. It also measures how wide the PDF is. <p> It is the square of standard deviation. <p> In signal processing, assuming mean of the noise is 0, it is also average power of the noise. <p> Increasing it widens the PDF, and also flattens it so that the area under the PDF remains 1.

## week 2 tutorial

- datetime: 2025-07-22T11:00:00+08:00/2025-07-22T12:20:00+08:00, PT1H20M
- topic:

## week 2 lab

- datetime: 2025-07-22T14:00:00+08:00/2025-07-22T16:50:00+08:00, PT2H50M
- topic: communication protocol, bit error rate \(BER\)
- status: attendance
- assignment: [lab 3](assignments/lab%203/index.md)
- questions: [post lab quiz 3 derivative](questions/post%20lab%20quiz%203%20derivative.md)

## week 2 lecture 2

- datetime: 2025-07-23T14:00:00+08:00/2025-07-23T15:50:00+08:00, PT1H50M
- topic: noise; error correcting codes
- normal distribution
- [Q-function](../../../../general/Q-function.md) ::@:: It is the tail distribution function of the standard normal distribution. In other words, $Q(x)$ is the probability that a normal \(Gaussian\) random variable will obtain a value larger than $x$ standard deviations. Equivalently, $Q(x)$ is the probability that a standard normal random variable takes a value larger than $x$.
  - Q-function / probability ::@:: $$Q(x) := P[X > x] \implies P[X \le x] = 1 - Q(x) \,,$$ where $X$ follows a standard normal distribution, i.e. with mean 0 and standard deviation 1. <p> For a normal distribution $Y$ with mean $\mu_Y$ and standard deviation $\sigma_Y$ \(variance $\sigma_Y^2$\), we compute $$P[Y > y] = Q\left(\frac {y - \mu_Y} {\sigma_Y} \right) \implies P[Y \le y] = 1 - Q\left(\frac {y - \mu_Y} {\sigma_Y} \right) \,.$$
  - Q-function / computation ::@:: There is no closed-form expression for it. A table of values or computers must be used. <p> In MATLAB, use the `qfunc(x)` function.
- bit error rate
  - bit error rate / simple model
    - bit error rate / simple model / error probabilities ::@:: The input probabilities are easy to find. The conditional error probabilities are slightly harder to find. Further assume bit 0 sends $r_{\text{min} }$ and bit 1 sends $r_{\text{max} }$ \(offset $r_{\text{min} }$ and scale $r_{\text{max} } - r_{\text{min} }$\). <p> Then, given the additive noise PDF $X$, the PDF for sending bit 0 is simply to offset the PDF by $r_{\text{min} }$, i.e. $r_{\text{min} } + X$. The conditional error rate $P_{e0}$ is the area of the PDF that crosses into the wrong side of the threshold. The same goes for sending bit 1 $P_{e1}$.
    - bit error rate / simple model / threshold ::@:: We see by increasing the threshold, the conditional error rate decreases for sending bit 0 but increases for sending bit 1, and vice versa. So there is a tradeoff. <p> There is a point in between \(not necessarily in the middle\) that minimizes the bit error rate, with BER increasing as we move away from it. This point can be found using the first derivative test.
    - bit error rate / simple model / special case ::@:: IF the input bits are equally likely, and the additive noise follows a normal distribution, then the optimal threshold is in the middle: $$T^* = \frac {r_{\text{min} } + r_{\text{max} } } 2 \,,$$ and its optimal BER is $$\text{BER}^* = Q\left(\frac {r_{\text{max} } - r_{\text{min} } } {2 \sigma} \right) \,.$$ <p> We see a larger signal difference means less BER. However, this means a higher transmission power is needed.
- power
  - power / signal ::@:: The power of a signal is its amplitude squared. If the signal takes on value $r$ with probability $p$, we can weight the amplitude squared: $$\text{power} = \sum_k p_k r_k^2 \,.$$ <p> For a quiet output signal with both bits equally likely, we have: $$\begin{aligned} \text{power} & = \frac 1 2 r_{\text{min} }^2 + \frac 1 2 r_{\text{max} }^2 \\ & = \left(\frac 1 4 r_{\text{min} }^2 + \frac 1 2 r_{\text{min} } r_{\text{max} } + \frac 1 4 r_{\text{max} }^2 \right) + \left(\frac 1 4 r_{\text{min} }^2 - \frac 1 2 r_{\text{min} } r_{\text{max} } + \frac 1 4 r_{\text{max} }^2 \right) \\ & = \left(\frac {r_{\text{min} } + r_{\text{max} } } 2 \right)^2 + \left(\frac {r_{\text{min} } - r_{\text{max} } } 2 \right)^2 \,, \end{aligned}$$ the last expression of which is _bias—variance decomposition_, because the first term is squared bias while the latter is variance \(squared standard deviation\).
    - power / signal / rigorous ::@:: \(__this course__: untaught\) We can use the expected value to rigorously express the power of a signal: $$\text{power} = \operatorname E\left[X^2 \right] \,,$$ where $X$ is the signal modeled as a random signal. The _bias—variance decomposition_ is simply the following well-known identity: $$\operatorname E\left[X^2\right] = \operatorname E[X]^2 + \operatorname E\left[(X - \mu_X)^2 \right] = \operatorname E[X]^2 + \operatorname{Var}(X) = \mu_X^2 + \sigma_X^2 \,.$$ <p> This also explains why the power of an unbiased \(mean 0\) noise signal is simply its variance.
- [signal-to-noise ratio](../../../../general/signal-to-noise%20ratio.md) \(SNR, S/N\) ::@:: It is a measure used in science and engineering that compares the level of a desired signal to the level of background noise. SNR is defined as the ratio of signal power to noise power, often expressed in decibels.
  - signal-to-noise ratio / formula ::@:: $$\text{SNR} = \frac {\text{signal (without noise) power} } {\text{noise power} } \,.$$ However, it is often expressed in decibels \(dB\) instead: $$\text{SNR}_{\text{dB} } = 10 \log_10 \text{SNR} \,.$$ 0 dB means same the signal has the same power as noise. Every 10&nbsp;dB increase in SNR multiplies the signal power by 10, so that 10&nbsp;dB means 10 times, 20&nbsp;dB means 100 times, 30&nbsp;dB means 1000 times, etc.
  - signal-to-noise ratio / factors ::@:: Mostly due to transmission distance. As transmission distance increases, the signal power at the receiver decreases and the noise power remains mostly constant. <p> Other factors include electronics quality, bit \(symbol\) rate, etc.
  - signal-to-noise ratio / typical values ::@:: A typical receiver requires a SNR of at least around 10&nbsp;dB to function. For a mobile phone, the minimum signal level is around 10<sup>−14</sup>&nbsp;W because the typical noise power is around 10<sup>−15</sup>&nbsp;W, which does not sound like a lot.
  - signal-to-noise ratio / bit error rate ::@:: For typical modulation schemes, increase in SNR decreases BER.
- [error correction code](../../../../general/error%20correction%20code.md) \(ECC\) ::@:: The sender encodes the message in a redundant way, most often by using \(_this_\). <p> It is used as part a technique called _channel coding_ used for controlling errors in data transmission over unreliable or noisy communication channels.
  - error correction code / motivation ::@:: Our protocol, including equalization, allows us to receive transmitted bits correctly for small errors. <p> But for large errors, we still receive the bits incorrectly, and we may not even know the bits are wrong! ECC can help detect errors \(e.g. error bursts of bounded length\) and possibly recover the data \(or if unrecoverable, tell the transmitter to retransmit the data\).
- [noisy-channel coding theorem](../../../../general/noisy-channel%20coding%20theorem.md) ::@:: It establishes that for any given degree of noise contamination of a communication channel, it is possible \(in theory\) to communicate discrete data \(digital information\) nearly error-free up to a computable maximum rate through the channel.
  - noisy-channel coding theorem / details ::@:: A noisy channel has a channel capacity _C_ determined by its noise \(which is determined by physical properties of the channel\). It is the _theoretical_ maximum rate in which useful information can be transmitted _almost_ error-free. Exceeding this channel capacity _R_ &gt; _C_, there is a minimum error rate that increases as _R_ increases further away from _C_. <p> However, the above does not tell us how to construct a code to achieve almost-error-free transmission.
  - noisy-channel coding theorem / history ::@:: This result was presented by Claude Shannon in 1948 and was based in part on earlier work and ideas of Harry Nyquist and Ralph Hartley.
- [block code](../../../../general/block%20code.md) ::@:: They are a large and important family of error-correcting codes that encode data in blocks. <p> It can also refer to any error-correcting code that acts on a block of $k$ bits of input data to produce $n$ bits of output data $(n,k)$. Consequently, the block coder is a _memoryless_ device.
  - block code / codeword ::@:: Previously, we have only considered codeword that simply contains the data bits. <p> Now using block code $(n, k)$, the codeword consists of $k$ _message bits_ and $n - k$ _extra bits_, so that each codeword is $n$ bits. The extra bits are derived deterministically from the message bits, so there is only 1 valid combination of extra bits for each combination of message bits. So such a codeword only has $2^k$ valid combinations, and all other combinations indicate a possible transmission error.
  - block code / code rate ::@:: It is simply the fraction of message bits per codeword: _k_/_n_. <p> The _gross bit rate_ is simply the number of bits sent per unit time, ignoring if the bits are useful or not. The _net bit rate_ is the number of _useful_ bits sent per unit time, which is obtained by multiplying the gross bit rate by the code rate.
- [parity bit](../../../../general/parity%20bit.md) ::@:: It is a bit added to a string of binary code. Parity bits are a simple form of error detecting code.
  - parity bit / details ::@:: We count the number of 1s in the message bits. The parity bit is derived based on the evenness or oddness of the number of 1s. This bit is then simply appended to the message to form a codeword. <p> This is an example of a $(k + 1, k)$ block code for _k_ message bits.
  - parity bit / even parity bit ::@:: The parity bit is 0 if the number of 1s is even, otherwise 1. Equivalently, the number of 1s in a valid codeword \(including the parity bit\) is even. \(__this course__: __Important__. We use this unless otherwise specified.\)
  - parity bit / odd parity bit ::@:: The parity bit is 0 if the number of 1s is odd, otherwise 1. Equivalently, the number of 1s in a valid codeword \(including the parity bit\) is odd. \(__this course__: __Important__. We do _not_ use this unless otherwise specified.\)
  - parity bit / usage ::@:: For each codeword, it can detect one-bit errors. However, it cannot correct the one-bit errors. This is because its minimum Hamming distance between any two valid codewords is 2. <p> Its main advantage is its high code rate.
- block code
  - block code / spaces ::@:: A space can be represented by a graph: a vertex for each combination of bits, and an edge between every two combination of bits that differ by exactly 1 bit. <p> We can consider the message space and codeword space. The former constructs the space based on the message bits only, while the latter constructs the space based on the entire codeword. As a result, the former contains only valid codewords, while the latter contains both valid and invalid codewords.
    - block code / spaces / intuition ::@:: For an analog signal, increasing SNR decreases BER. This is done by increasing the _distance_ between 0 and 1. <p> A similar idea is applied for block codes. We can _detect_ errors by adding extra bits to increase the distance between valid codewords in the codeword space. Sometimes, we can even _correct_ errors.
- [Hamming distance](../../../../general/Hamming%20distance.md) ::@:: It between two strings or vectors of equal length is the number of positions at which the corresponding symbols are different. In other words, it measures the minimum number of substitutions required to change one string into the other, or equivalently, the minimum number of errors that could have transformed one string into the other.
  - Hamming distance / history ::@:: \(Richard Hamming, 1950\)
- block code
  - block code / Hamming distance ::@:: The minimum Hamming distance $d$ between any two valid codewords in the _codeword space_ \(not _message space_\) determines the maximum of error bits so that we can detect or correct errors. <p> We can _either_ detect errors only _or_ detect and correct errors if possible. <p> If we only detect errors, we can do so with up to $d - 1$ error bits. <p> If we detect and correct errors, and we simply use the closest valid codeword, we can detect up to $\left\lceil \frac {d - 1} 2 \right\rceil$ error bits and correct \(correctly\) up to $\left\lfloor \frac {d - 1} 2 \right\rfloor$ error bits. Not that if we can correct, then we must be able to detect, but the converse is not true for even $d$. For even $d$, there are invalid codewords with equal distance to multiple valid codewords, so we can detect said errors but not correct them correctly always.
- [repetition code](../../../../general/repetition%20code.md) ::@:: It is one of the most basic linear error-correcting codes. In order to transmit a message over a noisy channel that may corrupt the transmission in a few places, the idea of the repetition code is to just repeat the message several times. The hope is that the channel corrupts only a minority of these repetitions.
  - repetition code / details ::@:: There is only 1 data bit. We repeated the data bits $n - 1$ times. This forms a $(n, 1)$ block code.
  - repetition code / Hamming distance ::@:: The minimum Hamming distance $d$ between any two valid codewords \(there are only 2\) is $n$. <p> Intuitively, if we want to detect errors, we can always do so unless all $n$ bits have flipped. If we want to correct errors, we are taking the _majority vote_, so we can always \(correctly\) do so when at most $\left\lfloor \frac {n - 1} 2 \right\rfloor$ have flipped. Note we must choose to _either_ detect errors only _or_ detect and correct errors if possible.
- assignment: [homework 1](assignments/homework%201/index.md)

## week 2 tutorial 2

- datetime: 2025-07-24T11:00:00+08:00/2025-07-24T12:20:00+08:00, PT1H20M
- topic:

## week 2 lab 2

- datetime: 2025-07-24T14:00:00+08:00/2025-07-24T16:50:00+08:00, PT2H50M
- topic: eye diagram, equalization
- status: attendance
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
    - block code / Hamming distance / notation ::@:: Sometimes the minimum Hamming distance between any two valid codewords are included as well: $(n, k, d)$ instead of simply $(n, k)$.
- repetition code
- parity bit
  - parity bit / details
  - parity bit / even parity bit
- block code
  - block code / \(8, 4\) block code ::@:: The 4 data bits $D_1, D_2, D_3, D_4$ are laid out in a 2-by-2 table in Z-order. The parity bits $P_1, P_2, P_3, P_4$ are appended to the table left and bottom edges as follows: $$\begin{bmatrix} D_1 & D_2 & P_1 \\ D_3 & D_4 & P_2 \\ P_3 & P_4 \end{bmatrix} \,.$$ The parity bits check the data bits on their corresponding column or row. <p> Note this is not the \[7, 4\] Hamming code or the \[8, 4\] Hamming code with an extra parity bit. However, the symmetry makes this code easier to learn, so this is why this code instead of the Hamming code is learnt instead. \(__this course__: As a codeword, the data bits come before the parity bits.\)
    - block code / \(8, 4\) block code / Hamming distance ::@:: Its minimum Hamming distance is 3. \(__this course__: Proof not required.\) <p> So we can _either_ detect up to 2 error bits _or_ correct up to 1 error bit.
    - block code / \(8, 4\) block code / syndrome bits ::@:: The syndrome bits are calculated when decoding a block code. For each column and row \(each set of parity bit and their corresponding data bits\), its syndrome bit is 0 if there is no parity error, or 1 if there is a parity error. Equivalently, the syndrome bit, when added to the column or row, "fixes" the parity of that column or row. \(__this course__: __Important__. We use _even_ parity for all parity checking, i.e. an even number of 1s is correct.\)
    - block code / \(8, 4\) block code / error detection ::@:: Assuming up to 2 data bits are flipped. <p> If all syndrome bits are 0, no errors are detected. Otherwise, there is an error, because flipping at most 2 data bits cannot make all syndrome bits 0.
    - block code / \(8, 4\) block code / error correction ::@:: Assuming up to 1 data bit is flipped. <p> If 1 syndrome bit is 1, that means its parity bit is flipped, because flipping a parity bit changes 1 syndrome bit. If 2 syndrome bits are 1, that means the data bit in the corresponding column and row is flipped, because flipping a data bit changes 2 syndrome bits.
  - block code / \(9, 4\) block code with parity bit ::@:: The 4 data bits $D_1, D_2, D_3, D_4$ are laid out in a 2-by-2 table in Z-order. The parity bits $P_1, P_2, P_3, P_4, P_5$ are appended to the table left and bottom edges as follows: $$\begin{bmatrix} D_1 & D_2 & P_1 \\ D_3 & D_4 & P_2 \\ P_3 & P_4 & P_5 \end{bmatrix} \,.$$ The first 4 parity bits check the data bits on their corresponding column or row. The last parity bit checks all previous 8 bits. <p> Note this is not the \[7, 4\] Hamming code or the \[8, 4\] Hamming code with an extra parity bit. However, the symmetry makes this code easier to learn, so this is why this code instead of the Hamming code is learnt instead. \(__this course__: As a codeword, the data bits come before the parity bits.\)
    - block code / \(9, 4\) block code with parity bit / Hamming distance ::@:: Its minimum Hamming distance is 4. In general, add an extra parity bit to a block code \(that does not already have an extra parity bit added\) increases the minimum Hamming distance by 1. \(__this course__: Proof not required.\) <p> So we can _either_ detect up to 3 error bits _or_ detect up to 2 error bits and correct up to 1 error bit.
    - block code / \(9, 4\) block code with parity bit / syndrome bits ::@:: The syndrome bits are calculated when decoding a block code. For each column and row \(each set of parity bit and their corresponding data bits\), its syndrome bit is 0 if there is no parity error, or 1 if there is a parity error. The same is done for the last parity bit $P_5$ but for all bits. Equivalently, the syndrome bit, when added to the column or row, "fixes" the parity of that column or row. \(__this course__: __Important__. We use _even_ parity for all parity checking, i.e. an even number of 1s is correct.\)
    - block code / \(9, 4\) block code with parity bit / error detection ::@:: Assuming up to 3 data bits are flipped. <p> The embedded \(8, 4\) block code \(i.e. ignoring the parity bit\) can detect up to 2 error bits. For exactly 3 error bits, the embedded block code itself may not detect an error, but the last parity bit must be able to detect it.
    - block code / \(9, 4\) block code with parity bit / error correction ::@:: Assuming up to 2 data bit is flipped. <p> Check if the last parity bit is wrong. If so, there is exactly 1 error bit, and the procedure is the same as the \(8, 4\) block code \(i.e. ignoring the parity bit\). Otherwise, we can detect up to 2 error bits \(but not correct it\), as the embedded \(8, 4\) block code itself \(i.e. ignoring the parity bit\) can detect up to 2 error bits.
- [music](../../../../general/music.md) ::@:: It is the arrangement of sound to create some combination of form, harmony, melody, rhythm, or otherwise expressive content.
  - music / signal ::@:: In music, most instruments produce a sinusoid of a fundamental frequency and its overtones. When there are multiple instruments, their sounds are simply added together. This forms the waveform of music. <p> Actually, the same is true for any waveform, not just music. That is, any waveform can be considered as a combination of sinusoids of various amplitudes, frequencies, and phases.
- [sine wave](../../../../general/sine%20wave.md) ::@:: It is a periodic wave whose waveform \(shape\) is the trigonometric sine function.
  - sine wave / sinusoid form ::@:: Sine waves of arbitrary phase and amplitude are called _sinusoids_ and have the general form: $$y(t)=A\sin(\omega t+\varphi )=A\sin(2\pi ft+\varphi )$$ where: <p> - $A$, _[amplitude](../../../../general/amplitude.md)_, the peak deviation of the function from zero. <br/> - $t$, the [real](../../../../general/real%20number.md) [independent variable](../../../../general/independent%20variable.md), usually representing [time](../../../../general/time.md) in [seconds](../../../../general/seconds.md). <br/> - $\omega$, _[angular frequency](../../../../general/angular%20frequency.md)_, the rate of change of the function argument in units of [radians per second](../../../../general/radians%20per%20second.md). <br/> - $f$, _[ordinary frequency](../../../../general/ordinary%20frequency.md)_, the _[number](../../../../general/real%20number.md)_ of oscillations \([cycles](../../../../general/turn%20(angle).md)\) that occur each second of time. <br/> - $\varphi$, _[phase](../../../../general/phase%20(waves).md)_, specifies \(in [radians](../../../../general/radian.md)\) where in its cycle the oscillation is at _t_ = 0. <p> \(__this course__: __Important__. We use cosine waves: $$A \cos(2\pi f t + \varphi) \,.$$\)
  - sine wave / cosine wave ::@:: Since $$\begin{aligned} \sin x & = \cos(x - \pi / 2) \\ \cos x & = \sin(x + \pi / 2) \,, \end{aligned}$$ so any sine wave can be represented as a cosine wave with a shifted phase, and vice versa. <p> \(__this course__: __Important__. We use cosine waves: $$A \cos(2\pi f t + \varphi) \,.$$\)
  - sine wave / discrete ::@:: We can consider a sine wave in discrete time by simply sampling the continuous sine wave. <p> We consider _N_ samples. Then the ordinary frequency $f$ is often replaced by _cycle frequency_ $k \in \set{0, 1, \ldots, \lfloor N / 2 \rfloor}$, and time $t$ is often replaced by discrete time index $n$: $$A \cos\left( 2 \pi \frac k N n + \varphi \right) \,.$$ The cycle frequency $k$ represents the number of \(co\)sine waves in _N_ samples. The period $T$ in samples is simply $N / k$. <p> Using $\frac k N n = ft$, the ordinary frequency $f$ is recovered as $$f = \frac k N \frac n t = \frac k N \frac 1 {T_s} = \frac k N F_s \,,$$ where $T_s$ is sampling period and $F_s = 1 / T_s$ is sampling frequency.
- [Fourier series](../../../../general/Fourier%20series.md) ::@:: It is an expansion of a periodic function into a sum of trigonometric functions.
  - Fourier series / forms ::@:: There are many forms to write the Fourier series: amplitude-phase form, exponential form, sine-cosine form. \(__this course__: We only teach the amplitude-phase form, and only scratch its surface.\)
  - Fourier series / amplitude-phase form ::@:: If the function $s(x)$ is real-valued then the Fourier series can also be represented as $$s_{N}(x)=A_{0}+\sum _{n=1}^{N}A_{n}\cos \left(2\pi {\tfrac {k}{P} }x-\varphi _{k}\right)$$ where $A_{n}$ is the amplitude and $\varphi _{n}$ is the phase shift of the $k^{th}$ harmonic \(positive shifts cosine to the right\). <p> \(__this course__: Since we are thinking in discrete time with $N$ samples, using $n / N = x / P$, and that cycle frequencies are up to $\lfloor N / 2 \rfloor$ we have: $$s_{N}(x) = A_0 + \sum_{n = 1}^{\lfloor N / 2 \rfloor} A_k \cos\left(2 \pi \frac k N n + \varphi_k \right) \,.$$ Notice we use the negated phase shift as well.\)
    - Fourier series / amplitude-phase form / interpretation ::@:: This means any discrete waveform with $N$ samples can be decomposed into $\lfloor N / 2 \rfloor + 1$ cosines. \(Though the first cosine has zero frequency and is really just a flat line.\) <p> $A_0$ is the _average level_, also known as the _DC offset_. $A_k$ is the amplitude of the cosine with cycle frequency $k$. $\varphi_k$ is the phase of the cosine with cycle frequency $k$, with positive values shifting to the right \(when $+ \varphi_k$ instead of $- \varphi_k$ is used\).
    - Fourier series / amplitude-phase form / amplitude spectrum ::@:: We can plot the $A_k$ amplitude against cycle frequency $k$. It can show the most important frequencies, which are frequencies with the largest amplitudes. <p> By keeping frequencies with the largest amplitudes, we can roughly recreate the waveform, with the original waveform fully recovered when all frequencies with nonzero amplitudes are kept.
    - Fourier series / amplitude-phase form / phase spectrum ::@:: We can also plot the $\varphi_k$ phase against cycle frequency $k$. <p> Combined with the amplitude spectrum, they describe the original discrete signal completely, i.e. the original signal can be fully recovered from them.
  - Fourier series / representation ::@:: It is one of way to represent the _Fourier transform_ of a signal.
- [integral transform](../../../../general/integral%20transform.md) ::@:: It is a type of transform that maps a function from its original function space into another function space via integration, where some of the properties of the original function might be more easily characterized and manipulated than in the original function space. The transformed function can generally be mapped back to the original function space using the _inverse transform_.
  - integral transform / examples ::@:: Fourier transform, Laplace transform, Z-transform, etc.
  - integral transform / motivation ::@:: Transforms are _invertible_, so no information is lost or gained using a transform or its inverse. So transforms give different views of the same signal. <p> These different views allow us to understand and manipulate the signal in other ways. Some signal manipulations may be \(much\) easier with these different views.
- [discrete Fourier transform](../../../../general/discrete%20Fourier%20transform.md) \(DFT\) ::@:: \(__this course__: optional\) <p> It takes _N_ samples and returns _N_ complex coefficients called _Fourier coefficients_.
  - discrete Fourier transform / definition ::@:: \(__this course__: optional\) <p> It transforms a sequence of _N_ complex numbers $\left\{\mathbf {x} _{n}\right\}:=x_{0},x_{1},\ldots ,x_{N-1}$ into another sequence of complex numbers, $\left\{\mathbf {X} _{k}\right\}:=X_{0},X_{1},\ldots ,X_{N-1}$, which is defined by: $$X_{k}=\sum _{n=0}^{N-1}x_{n}\cdot e^{-i2\pi {\tfrac {k}{N} }n} \,.$$
  - discrete Fourier transform / MATLAB ::@:: The function `fft` can be used to compute the DFT of a signal. \(The "FFT" in `fft` stands for "fast Fourier transform".\) <p> Note the indexing in MATLAB starts from 1, e.g. $X_0$ is `Xdft(1)`, where `Xdft` is `fft(x)`.
  - discrete Fourier transform / Fourier series ::@:: \(__this course__: optional\) <p> For a _real_ signal, we can compute its Fourier series using the DFT. In particular, we can get the amplitude spectrum and phase spectrum. <p>  For the amplitude spectrum: $$A_k = \begin{cases} \frac 1 N \lvert X_k \rvert & k = 0 \text{ or } \frac N 2 \\ \frac 2 N \lvert X_k \rvert & \text{otherwise} \,. \end{cases}$$ For the phase spectrum: $$\varphi_k = \angle X_k \,.$$
- [complex number](../../../../general/complex%20number.md) ::@:: \(__this course__: optional\) <p> It is an element of a number system that extends the real numbers with a specific element denoted _i_, called the imaginary unit and satisfying the equation $i^{2}=-1$; every complex number can be expressed in the form $a+bi$, where _a_ and _b_ are real numbers. <p> \(__this course__: This course follows electrical engineering convention and uses $j$ instead of $i$.\)
  - complex number / to polar coordinates ::@:: \(__this course__: optional\) <p> $$\begin{aligned} \lvert z \rvert & = \sqrt{a^2 + b^2} \\ \angle z & = \arctan(b / a) \,. \end{aligned}$$
  - complex number / from polar coordinates ::@:: \(__this course__: optional\) <p> $$\begin{aligned} a & = \lvert z \rvert \cos(\angle z) \\ b & = \lvert z \rvert \sin(\angle z) \,. \end{aligned}$$

## week 3 lecture

- datetime: 2025-07-28T14:00:00+08:00/2025-07-28T16:50:00+08:00, PT2H50M
- topic: filters, frequency response; time—frequency analysis, source coding; signal transmission multiplexing

## week 3 tutorial

- datetime: 2025-07-29T11:00:00+08:00/2025-07-29T12:20:00+08:00, PT1H20M
- status: unscheduled

## midterm examination

- datetime: 2025-07-29T11:00:00+08:00/2025-07-29T11:50:00+08:00, PT50M
- venue: Lecture Theater D, Academic Building
- format
  - calculator: no
  - cheatsheet: no
  - referencing: closed book
  - provided: \(none\)
  - questions: long questions ×4
- grades: ?/? → ?/?
  - statistics
    - timestamps: ? → ?
    - mean: ? → ?
    - standard deviation: ? → ?
    - low: ? → ?
    - lower quartile: ? → ?
    - median: ? → ?
    - upper quartile: ? → ?
    - high: ? → ?
    - distribution: ? → ?
- report: ?
- check: ?

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
>
## week 3 lab

- datetime: 2025-07-29T14:00:00+08:00/2025-07-29T16:50:00+08:00, PT2H50M
- status: unscheduled

## week 3 lecture 2

- datetime: 2025-07-30T14:00:00+08:00/2025-07-30T15:50:00+08:00, PT1H50M
- topic: signal transmission demultiplexing; introduction to networks
- assignment: [homework 2](assignments/homework%202/index.md)

## week 3 tutorial 2

- datetime: 2025-07-31T11:00:00+08:00/2025-07-31T12:20:00+08:00, PT1H20M
- topic:

## week 3 lab 2

- datetime: 2025-07-31T14:00:00+08:00/2025-07-31T16:50:00+08:00, PT2H50M
- topic: bit errors, signal-to-noise ratio
- status: attendance
- assignment: [lab 5](assignments/lab%205/index.md)
- questions: [post lab quiz 5 derivative](questions/post%20lab%20quiz%205%20derivative.md)

## week 3 lab 3

- datetime: 2025-08-01T10:00:00+08:00/2025-07-26T12:50:00+08:00, PT2H50M
- status: unscheduled

## week 3 lecture 3

- datetime: 2025-08-01T14:00:00+08:00/2025-08-01T15:50:00+08:00, PT1H50M
- topic: link layer; network layer

## week 4 lecture

- datetime: 2025-08-04T14:00:00+08:00/2025-08-04T16:50:00+08:00, PT2H50M
- topic: transport layer; application layer

## week 4 tutorial

- datetime: 2025-08-05T11:00:00+08:00/2025-08-05T12:20:00+08:00, PT1H20M
- topic:

## week 4 lab

- datetime: 2025-08-05T14:00:00+08:00/2025-08-05T16:50:00+08:00, PT2H50M
- topic: time—frequency analysis
- status: attendance
- assignment: [lab 6](assignments/lab%206/index.md)
- questions: [post lab quiz 6 derivative](questions/post%20lab%20quiz%206%20derivative.md)

## week 4 lecture 2

- datetime: 2025-08-06T14:00:00+08:00/2025-08-06T15:50:00+08:00, PT1H50M
- topic: questions & answers
- assignment: [homework 3](assignments/homework%203/index.md)

## week 4 tutorial 2

- datetime: 2025-08-07T11:00:00+08:00/2025-08-07T12:20:00+08:00, PT1H20M
- topic:

## week 4 lab 2

- datetime: 2025-08-07T14:00:00+08:00/2025-08-07T16:50:00+08:00, PT2H50M
- topic: frequency division multiplexing
- status: attendance
- assignment: [lab 7](assignments/lab%207/index.md)
- questions: [post lab quiz 7 derivative](questions/post%20lab%20quiz%207%20derivative.md)

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
  - provided: \(none\)
  - questions: long questions ×?
- grades: ?/? → ?/?
  - statistics
    - timestamps: ? → ?
    - mean: ? → ?
    - standard deviation: ? → ?
    - low: ? → ?
    - lower quartile: ? → ?
    - median: ? → ?
    - upper quartile: ? → ?
    - high: ? → ?
    - distribution: ? → ?
- report: ?
- check: ?

## aftermath

### total

- grades: ?/100
  - statistics: ?
