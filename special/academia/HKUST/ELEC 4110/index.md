---
aliases:
  - Digital Communications and Wireless Systems
  - Digital Communications and Wireless Systems index
  - ELEC 4110
  - ELEC 4110 index
  - ELEC4110
  - ELEC4110 index
  - HKUST ELEC 4110
  - HKUST ELEC 4110 index
  - HKUST ELEC4110
  - HKUST ELEC4110 index
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110
  - function/index
  - language/in/English
---

# index

- HKUST ELEC 4110
- name: Digital Communications and Wireless Systems

The content is in teaching order.

- grading
  - scheme
    - homework ×3: 15%
    - midterm examination: 25%
    - project: 10%
    - final examination: 50%

## children

- [assignments](assignments/index.md)
- [questions](questions.md)

## week 1 lecture

- datetime: 2025-09-02T09:00:00+08:00/2025-09-02T10:20:00+08:00, PT1H20M
- topic: logistics; overview of digital communications; signal basics
- ELEC 4110
  - ELEC 4110 / instructor
  - ELEC 4110 / introduction ::@:: _Digital communications_ is one of the technologies enabling the _Information Age_. <!--SR:!2025-12-06,59,310!2025-12-05,58,310-->
  - ELEC 4110 / objectives ::@:: What is information? What is signal? How to represent them? How to communicate them wirelessly? What are cellular networks? How have they evolved? <!--SR:!2025-12-09,61,310!2025-12-13,65,310-->
  - ELEC 4110 / grading
  - ELEC 4110 / homework
  - ELEC 4110 / textbook
  - ELEC 4110 / materials ::@:: See lecture notes on Canvas. They are posted at least 1 lecture in advanced. There may be hand-written comments on the whiteboard as well. <!--SR:!2025-12-11,63,310!2025-12-03,57,310-->
  - ELEC 4110 / help
  - ELEC 4110 / prerequisites ::@:: linear system analysis \(Fourier transform, linear systems\), noise, stochastic processes, signal analysis \(sampling, signal models, signals\) <!--SR:!2025-12-11,63,310!2025-12-10,62,310-->
  - ELEC 4110 / mathematics ::@:: Mathematics is used to _precisely_ model signals for communications. However, the mathematics itself is not the final objective of this course. Instead, they are how and why communications work in practice. <p> In short, mathematics is the language to make things _precise_. But we need to _comprehend_ beyond the language of mathematics. <!--SR:!2025-12-02,56,310!2025-12-12,64,310-->
- [communication](../../../../general/communication.md) ::@:: It is commonly defined as the transmission of information. Its precise definition is disputed and there are disagreements about whether unintentional or failed transmissions are included and whether communication not only transmits meaning but also creates it. <!--SR:!2025-12-07,60,310!2025-12-06,59,310-->
  - communication / examples ::@:: molecular communication, short-range communication, telecommunication, etc. <!--SR:!2025-12-02,56,310!2025-12-10,63,310-->
  - communication / considerations ::@:: When implementing communication, there are many _practical_ considerations. For example, using a physical string connected between two cups to communicate is impractical for many reasons. <!--SR:!2025-12-12,64,310!2025-12-02,56,310-->
- [information](../../../../general/information.md) ::@:: It is an abstract concept that refers to something which has the power to inform. <!--SR:!2025-12-01,55,310!2025-12-06,59,310-->
  - information / signal processing ::@:: Information is represented by physical signals. <!--SR:!2025-12-03,57,310!2025-12-14,66,310-->
  - information / entropy ::@:: It of a random variable quantifies the average level of uncertainty or information associated with the variable's potential states or possible outcomes. <p> An important equation \(to be explained later\) to measure information entropy is: $$H(X) = -\sum_{X} p(X) \log_2 p(X) \,,$$ where $X$ is a discrete random variable with probability mass function $p(X)$. <!--SR:!2025-12-11,63,310!2025-12-02,56,310-->
- [signal processing](../../../../general/signal%20processing.md) ::@:: It is an electrical engineering subfield that focuses on analyzing, modifying and synthesizing signals, such as sound, images, potential fields, seismic signals, altimetry processing, and scientific measurements. <!--SR:!2025-12-08,61,310!2025-11-16,40,290-->
- [analog signal](../../../../general/analog%20signal.md) ::@:: It is any signal, typically a continuous-time signal, representing some other quantity, i.e., _analogous_ to another quantity. <!--SR:!2025-12-10,63,310!2025-12-04,58,310-->
- [time domain](../../../../general/time%20domain.md) ::@:: It is a representation of how a signal, function, or data set varies with time. It is used for the analysis of mathematical functions, physical signals or time series of economic or environmental data. <!--SR:!2025-12-10,62,310!2025-12-13,65,310-->
  - time domain / intuition ::@:: The signal is represented using a time function from zero time \(inclusive\) to infinite time \(exclusive\). Very visually intuitive. <!--SR:!2025-12-01,55,310!2025-12-03,57,310-->
- [periodic function](../../../../general/periodic%20function.md) ::@:: It is a function that repeats its values at regular intervals. <p> The length of the interval over which a periodic function repeats is called its __period__. Any function that is not periodic is called __aperiodic__. <!--SR:!2025-12-09,61,310!2025-12-15,67,310-->
  - periodic function / examples ::@:: For example, the trigonometric functions, which are used to describe waves and other repeating phenomena, are periodic. <!--SR:!2025-12-06,59,310!2025-12-05,58,310-->
  - periodic function / period ::@:: A positive number $T$ such that $f(t + T) = f(t)$ for all $t$. <!--SR:!2025-12-07,60,310!2025-12-05,58,310-->
  - periodic function / frequency ::@:: $f = 1 / T$ \(in hertz if $T$ is in second\) <!--SR:!2025-12-09,62,310!2025-12-15,67,310-->
  - periodic function / description ::@:: To describe the entire signal, describe a cycle suffices. <!--SR:!2025-12-03,57,310!2025-12-07,60,310-->
- [sine wave](../../../../general/sine%20wave.md) ::@:: It is a periodic wave whose waveform \(shape\) is the trigonometric sine function. <!--SR:!2025-12-09,61,310!2025-12-04,58,310-->
  - sine wave / sinusoid form ::@:: Sine waves of arbitrary phase and amplitude are called _sinusoids_ and have the general form: $$y(t)=A\sin(\omega t+\varphi )=A\sin(2\pi ft+\varphi )$$ where: <p> - $A$, _[amplitude](../../../../general/amplitude.md)_, the peak deviation of the function from zero. <br/> - $t$, the [real](../../../../general/real%20number.md) [independent variable](../../../../general/independent%20variable.md), usually representing [time](../../../../general/time.md) in [seconds](../../../../general/seconds.md). <br/> - $\omega$, _[angular frequency](../../../../general/angular%20frequency.md)_, the rate of change of the function argument in units of [radians per second](../../../../general/radians%20per%20second.md). <br/> - $f$, _[ordinary frequency](../../../../general/ordinary%20frequency.md)_, the _[number](../../../../general/real%20number.md)_ of oscillations \([cycles](../../../../general/turn%20(angle).md)\) that occur each second of time. <br/> - $\varphi$, _[phase](../../../../general/phase%20(waves).md)_, specifies \(in [radians](../../../../general/radian.md)\) where in its cycle the oscillation is at _t_ = 0. <!--SR:!2025-12-04,58,310!2025-12-06,59,310-->
  - sine wave / cosine wave ::@:: Since $$\begin{aligned} \sin x & = \cos(x - \pi / 2) \\ \cos x & = \sin(x + \pi / 2) \,, \end{aligned}$$ so any sine wave can be represented as a cosine wave with a shifted phase, and vice versa. <!--SR:!2025-12-12,64,310!2025-11-22,45,290-->
  - sine wave / description ::@:: To describe a sine wave, describe its amplitude $A$, angular frequency $\omega$, and phase $\phi$. <!--SR:!2025-12-04,58,310!2025-12-11,63,310-->
- [phasor](../../../../general/phasor.md) ::@:: It is a complex number representing a sinusoidal function whose amplitude _A_ and initial phase _θ_ are time-invariant and whose angular frequency _ω_ is fixed. <!--SR:!2025-12-07,60,310!2025-12-08,61,310-->
  - phasor / equation ::@:: $$s(t) = \Re(A \exp(j \phi) \exp(j \omega t)) = \Re(Z \exp(j \omega t)) \,.$$ $Z = A \exp(j \phi)$ is the _complex amplitude_, which incorporates both the amplitude and phase. <!--SR:!2025-12-10,63,310!2025-12-09,62,310-->
- periodic function
  - periodic function / arithmetic operation ::@:: Performing arithmetic operations between two periodic functions may _not_ yield a periodic function. This happens when their angular frequencies do not have a least common multiple \(LCM\). For example, this happens when one of angular frequency is _irrational_. <!--SR:!2025-12-10,62,310!2025-12-07,60,310-->
  - periodic function / aperiodic ::@:: If a function is not periodic, then it is _aperiodic_. This happens if a positive $T$ such that $s(t + T) = s(t)$ for all $t$ does not exist. <!--SR:!2025-12-09,62,310!2025-12-15,67,310-->
- [Heaviside step function](../../../../general/Heaviside%20step%20function.md) ::@:: It is a step function named after Oliver Heaviside, the value of which is zero for negative arguments and one for positive arguments. Different conventions concerning the value _H_\(0\) are in use. \(__this course__: _H_\(0\)&nbsp;=&nbsp;1\) <!--SR:!2025-12-04,58,310!2025-11-30,54,310-->
- [Dirac delta function](../../../../general/Dirac%20delta%20function.md) ::@:: It is a [generalized function](../../../../general/generalized%20function.md) on the [real numbers](../../../../general/real%20numbers.md), whose value is zero everywhere except at zero, and whose [integral](../../../../general/integral.md) over the entire real line is equal to one. Thus it can be [represented heuristically](../../../../general/heuristic.md) as $$\delta (x)={\begin{cases}0,&x\neq 0\\{\infty },&x=0\end{cases} }$$ such that $$\int _{-\infty }^{\infty }\delta (x)dx=1.$$ <!--SR:!2025-11-30,54,310!2025-12-03,57,310-->
- [ramp function](../../../../general/ramp%20function.md) ::@:: It is a unary real function, whose graph is shaped like a ramp. It can be expressed by numerous definitions, for example "0 for negative inputs, output equals input for non-negative inputs". <!--SR:!2025-12-14,66,310!2025-11-30,54,310-->
- [rectangular function](../../../../general/rectangular%20function.md) ::@:: It is defined as $$\operatorname {rect} \left({\frac {t}{a} }\right)=\Pi \left({\frac {t}{a} }\right)=\left\{ {\begin{array}{rl}0,&{\text{if } }|t|>{\frac {a}{2} }\\{\frac {1}{2} },&{\text{if } }|t|={\frac {a}{2} }\\1,&{\text{if } }|t|<{\frac {a}{2} }.\end{array} }\right.$$ Alternative definitions of the function define $\operatorname {rect} \left(\pm {\frac {1}{2} }\right)$ to be 0, or undefined. <!--SR:!2025-12-13,65,310!2025-11-07,33,270-->
- [triangular function](../../../../general/triangular%20function.md) ::@:: It is a function whose graph takes the shape of a triangle. Often this is an isosceles triangle of height 1 and base 2 in which case it is referred to as _the_ triangular function. <!--SR:!2025-12-15,67,310!2025-12-07,60,310-->
- analog signal
  - analog signal / basic operations ::@:: amplitude transformations: $As(t) + B$; $A$ scales the range about the horizontal axis and $B$ shifts vertically <br/> time reversal: $s(-t)$ \(special case of time scaling when $a = -1$\) <br/> time scaling: $s(at)$; compressed if $\lvert a \rvert > 1$ or expanded if $\lvert a \rvert < 1$ <br/> time shifting: $x(t - a)$; delayed \(moved towards the _right_\) by $a$ <!--SR:!2025-12-14,66,310!2025-12-09,62,310-->

## week 1 lecture 2

- datetime: 2025-09-04T09:00:00+08:00/2025-09-04T10:20:00+08:00, PT1H20M
- topic: signal basics
- analog signal
- [digital signal](../../../../general/digital%20signal.md) ::@:: It is a signal that represents data as a sequence of discrete values; at any given time it can only take on, at most, one of a finite number of values. <p> \(__this course__: Both values and time are discrete for a digital signal. This is different from the definition used above.\) <!--SR:!2025-12-10,63,310!2025-12-04,58,310-->
  - digital signal / vs. analog signal ::@:: This _contrasts_ with an analog signal, which represents continuous values; at any given time it represents a real number within an infinite set of values. <p> \(__this course__: Both values and time are continuous for an analog signal. This is different from the definition used above.\) <!--SR:!2025-12-09,61,310!2025-12-15,67,310-->
- [analog-to-digital converter](../../../../general/analog-to-digital%20converter.md) \(ADC\) ::@:: It is a system that converts an analog signal, such as a sound picked up by a microphone or light entering a digital camera, into a digital signal. <!--SR:!2025-12-01,55,310!2025-12-04,58,310-->
  - analog-to-digital converter / steps ::@:: sampling → quantization <!--SR:!2025-12-10,63,310!2025-12-14,66,310-->
    - analog-to-digital converter / steps / sampling ::@:: Continuous time is converted into discrete time by repeated _sampling_ at a fixed time interval. <p> This limits _bandwidth_. According to the _Nyquist–Shannon sampling theorem_, _perfect reconstruction_ is possible if $B < f_s / 2$, where $B$ is the bandwidth of the continuous time signal and $f_s$ is the sample rate. <!--SR:!2025-12-08,61,310!2025-11-30,54,310-->
    - analog-to-digital converter / steps / quantization ::@:: Continuous value is converted into discrete value by converting them into _n_-bit numbers. <p> This produces _quantization error_, as continuous value has \(uncountably\) infinite possible values while _n_-bit numbers have finite possible values. Thus this process is _irreversible_ in general. <!--SR:!2025-12-06,59,310!2025-12-10,62,310-->
- [Nyquist–Shannon sampling theorem](../../../../general/Nyquist–Shannon%20sampling%20theorem.md) ::@:: It is an essential principle for digital signal processing linking the frequency range of a signal and the sample rate required to avoid a type of distortion called aliasing. The theorem states that the sample rate must be at least twice the bandwidth of the signal to avoid aliasing. <!--SR:!2025-12-12,64,310!2025-12-09,61,310-->
- [digital-to-analog converter](../../../../general/digital-to-analog%20converter.md) \(DAC\) ::@:: It is a system that converts a digital signal into an analog signal. <!--SR:!2025-12-09,62,310!2025-12-01,55,310-->
  - digital-to-analog converter / reverse ::@:: An analog-to-digital converter \(ADC\) performs the reverse function. <!--SR:!2025-12-05,58,310!2025-12-02,56,310-->
  - digital-to-analog converter / steps ::@:: reconstruction → lowpass filter <!--SR:!2025-12-14,66,310!2025-12-08,61,310-->
    - digital-to-analog converter / steps / reconstruction ::@:: Discrete time is converted into continuous time. Usually, this is done by holding the sampled value until the next sample. <!--SR:!2025-12-01,55,310!2025-12-08,61,310-->
    - digital-to-analog converter / steps / lowpass filter ::@:: Discrete value is converted into continuous value. Holding the sampled value until the next sample yields a continuous-time signal with discrete value. Applying lowpass filter smoothens the signal and make it continuous-valued as well. <p> The lowpass filter frequency cutoff is usually half the sample rate due to the _Nyquist–Shannon sampling theorem_. <!--SR:!2025-12-01,55,310!2025-12-03,57,310-->
- digital signal
  - digital signal / advantages ::@:: It is _robust_ to degradation and noise, as small distortions of the waveform can be completely ignored. <!--SR:!2025-12-02,56,310!2025-12-05,58,310-->
  - digital signal / disadvantages ::@:: It cannot represent most physical signals _exactly_, as most of them are analog in nature. <!--SR:!2025-12-10,62,310!2025-12-03,57,310-->
  - digital signal / usage ::@:: Due to its robustness, it is used in storage and telecommunications. <!--SR:!2025-12-10,63,310!2025-12-12,64,310-->
    - digital signal / usage / storage ::@:: Consider audio tape \(analog\) vs. CD \(digital\). <!--SR:!2025-11-30,54,310!2025-11-30,54,310-->
    - digital signal / usage / telecommunications ::@:: Long-distance transmission cause path loss attenuation and thermal noise. If an analog signal is used, signal-to-noise ratio \(SNR\) decreases significantly at the receiver side. If a digital signal is used, SNR remains sufficiently high due to its robustness to degradation and noise. <!--SR:!2025-12-13,65,310!2025-11-30,54,310-->

## week 1 tutorial

- datetime: 2025-09-05T15:30:00+08:00/2025-09-05T16:20:00+08:00, PT50M
- status: unscheduled

---

> __<big><big>Welcome to ELEC4110</big></big>__
>
> Dear students
>
> Welcome to the class. I have uploaded the notes and reference materials on canvas. Tutorial will start on week 2. Look forward to meeting you on 2 Sept 09:00am.
>
> Cheers
>
> \[redacted\]

## aftermath

### total

- grades: ?/100
  - statistics: ?
