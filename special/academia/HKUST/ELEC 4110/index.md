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
      - cheatsheet: 1, A4-sized, double-sided, handwritten

## children

- [M-ary transmission](M-ary%20transmission.md)
- [M-FSK](M-FSK.md)
- [M-PSK](M-PSK.md)
- [M-QAM](M-QAM.md)
- [assignments](assignments/index.md)
- [questions](questions.md)
- [transcludes/Fourier transform](transcludes/Fourier%20transform.md)

## week 1 lecture

- datetime: 2025-09-02T09:00:00+08:00/2025-09-02T10:20:00+08:00, PT1H20M
- topic: logistics; overview of digital communications; signal; analog signal
- ELEC 4110
  - ELEC 4110 / introduction ::@:: _Digital communications_ is one of the technologies enabling the _Information Age_. <!--SR:!2026-08-19,256,330!2026-08-09,247,330-->
  - ELEC 4110 / structure ::@:: The class is split into two major themes: first, the fundamentals of digital communication theory (chapters 1-6), then a systems-centric view of wireless networks starting from chapter 7 onward (cellular/5G focus). <!--SR:!2026-02-03,82,369!2026-02-08,86,369-->
    - ELEC 4110 / structure / lectures ::@:: In the early lectures we'll build the mathematical foundations; later we'll apply those concepts to real-world scenarios such as multi-user cellular architectures and 5G design principles.<p> The goal is not only to understand how a system operates but also why certain design choices are made, linking theory directly to practical engineering decisions. <!--SR:!2026-02-11,89,369!2026-02-16,93,369-->
  - ELEC 4110 / questions ::@:: What is information? What is signal? How to represent them? How to communicate them wirelessly? What are cellular networks? How have they evolved? <!--SR:!2025-12-09,61,310!2025-12-13,65,310-->
  - ELEC 4110 / instructor ::@:: - Professor Vincent: Hong Kong → HKU undergrad → 3 yrs at monopoly operator _Tandicom_ → chartered engineer path <br/> - PhD in the UK: peer-controversial (HK industry scarcity) → viewed as adventure, not guaranteed success <br/> - Post-PhD: Bell Labs US → realized academia's knowledge was superficial vs. depth needed for cutting-edge research/product development <!--SR:!2026-02-02,81,369!2026-02-15,92,369-->
    - ELEC 4110 / instructor / background ::@:: Vincent was born in Hong Kong, earned his undergraduate degree at the University of Hong Kong, and spent three years working for the monopoly operator _Tandicom_ where he gained early exposure to telecom operations and a clear career path toward chartered engineer status. <!--SR:!2026-02-16,93,369!2026-02-01,80,369-->
    - ELEC 4110 / instructor / PhD ::@:: He then pursued a PhD in the UK—a decision that was controversial among peers because the HK research landscape offers few industry opportunities; nevertheless, he viewed it as an adventure rather than a guaranteed success. <!--SR:!2026-02-17,94,369!2026-02-17,94,369-->
    - ELEC 4110 / instructor / post-PhD ::@:: After his doctorate, Vincent joined Bell Labs in the U.S., where he realized that much of what he thought he knew from academia was superficial compared to the depth required for cutting-edge research and product development. <!--SR:!2026-02-02,81,369!2026-02-04,83,369-->
    - ELEC 4110 / instructor / teaching ::@:: The instructor emphasizes the dual questions of "how" a system operates and "why" it is designed that way. While practical step-by-step explanations cover the former, addressing the latter requires a robust theoretical framework that translates engineering intuition into fundamental principles. He argues that both hands-on domain knowledge and deep theory are crucial for advancing wireless technology from maintenance to innovative design. <!--SR:!2026-02-17,94,369!2026-01-31,79,369-->
    - ELEC 4100 / instructor / academia ::@:: Vincent contrasts undergraduate studies—centered on absorbing existing knowledge and passing exams—with doctoral research, which involves creating new knowledge amid uncertainty and extended timelines. He recounts peers who lingered into their eighth year without a clear graduation path, highlighting the unpredictable nature of academic careers. <!--SR:!2026-02-01,80,369!2026-02-17,94,369-->
    - ELEC 4100 / instructor / industry ::@:: At Bell Labs, he observed an interview split into a morning "output" session testing presentation skills and an afternoon "input" phase evaluating rapid comprehension, underscoring the dual importance of communication and quick learning. <!--SR:!2026-02-11,89,369!2026-02-16,93,369-->
  - ELEC 4100 / tips ::@:: Students should preview posted notes yet depend mainly on live lectures for depth, taking concise, organized notes during class; they must cultivate both clear articulation of complex ideas (output) and rapid extraction of key information from new material (input); by viewing the course as a link between theory and industry practice, they gain a dual perspective essential for designing or evaluating future wireless systems. <!--SR:!2026-02-09,87,369!2026-02-08,86,369-->
    - ELEC 4110 / tips / asking questions ::@:: The lecturer contrasts presenting information with quickly grasping essential details, judging comprehension by whether students ask meaningful questions during new topics; a lack of questions can mean either perfect understanding or total confusion, underscoring the learner's active role in seeking clarity. He urges students to treat every lecture as practice for comprehension, encouraging focused questioning when uncertain and using external resources—while stressing that this cannot be automated and requires personal effort—to foster a culture of inquiry that benefits both individual learning and the classroom environment. <!--SR:!2026-02-05,84,369!2026-02-10,88,369-->
  - ELEC 4110 / grading
  - ELEC 4110 / coursework ::@:: homework, midterm examination, MATLAB simulation project, final examination <!--SR:!2026-02-08,86,369!2026-02-01,80,369-->
    - ELEC 4110 / coursework / examinations ::@::  The midterm covers the first half of the syllabus—digital communication theory. <p> The final exam spans all course material, including system-design scenarios, and may present complex formulas that will be supplied on the question sheet. Answers must show conceptual understanding and logical reasoning rather than lengthy algebraic work. The final exam emphasizes scenario-based questions requiring design and justification rather than rote definitions. <!--SR:!2026-01-31,79,369!2026-02-11,89,369-->
  - ELEC 4110 / prerequisites ::@:: linear system analysis \(Fourier transform, linear systems\), noise, stochastic processes, signal analysis \(sampling, signal models, signals\) <!--SR:!2025-12-11,63,310!2025-12-10,62,310-->
  - ELEC 4110 / materials ::@:: See lecture notes on Canvas. They are posted at least 1 lecture in advanced. There may be hand-written comments on the whiteboard as well. <!--SR:!2025-12-11,63,310!2026-08-10,250,330-->
  - ELEC 4110 / textbook
  - ELEC 4110 / mathematics ::@:: Mathematics is used to _precisely_ model signals for communications. However, the mathematics itself is not the final objective of this course. Instead, they are how and why communications work in practice. <p> In short, mathematics is the language to make things _precise_. But we need to _comprehend_ beyond the language of mathematics. <!--SR:!2026-08-05,246,330!2025-12-12,64,310-->
  - ELEC 4110 / intuition ::@:: Intuition built from domain knowledge—such as communication theory fundamentals—helps students anticipate system behavior and evaluate design trade-offs, guiding them toward viable solutions that meet specifications. The lecturer notes that intuition is only a rough guide; mathematics must be used to formalize and test these insights with precise predictions. Through exercises and projects that blend gut feeling with rigorous analysis, students strengthen this synergy, making it easier to approach novel exam problems. <!--SR:!2026-02-16,93,369!2026-02-01,80,369-->
  - ELEC 4110 / coursework
    - ELEC 4110 / coursework / project ::@:: The MATLAB group project requires teams to model a communication scenario—such as channel coding or modulation—and evaluate its performance metrics while clearly documenting assumptions, design choices, and results in a written report. These hands-on experiments reinforce theoretical concepts through data analysis and encourage peer collaboration that mirrors real-world engineering teamwork. The final deliverable consists of code, plots, and an explanatory narrative that connects simulation outcomes to the underlying theory. <!--SR:!2026-02-01,80,369!2026-02-07,85,369-->
    - ELEC 4110 / coursework / homework ::@:: Homework and problem sets evaluate quantitative skills with questions designed to minimize tedious algebra; solutions should emphasize key reasoning steps rather than lengthy derivations. The instructor will give feedback on conceptual clarity, methodological soundness, and correct theory application, while expecting students to submit clearly structured responses (e.g., numbered steps, annotated equations). Regular practice is crucial for mastering the transition from problem statement to analytical solution. <!--SR:!2026-02-17,94,369!2026-02-11,89,369-->
  - ELEC 4110 / culture ::@:: The lecturer stresses that while students won't be compelled to ask questions, cultivating curiosity is essential, and classroom Q&A sessions aim to normalize inquiry and lessen the stigma of uncertainty. By fostering this environment, the course seeks to improve individual understanding and collective knowledge sharing, boosting students' confidence in tackling new material and articulating their ideas. This culture of continuous learning aligns with industry expectations that value ongoing inquiry and skill development. <!--SR:!2026-02-12,89,369!2026-01-19,66,349-->
- [communication](../../../../general/communication.md) ::@:: It is commonly defined as the transmission of information. Its precise definition is disputed and there are disagreements about whether unintentional or failed transmissions are included and whether communication not only transmits meaning but also creates it. <!--SR:!2026-08-24,260,330!2026-08-18,255,330-->
  - communication / examples ::@:: molecular communication, short-range communication, telecommunication, etc. <!--SR:!2026-08-02,243,330!2025-12-10,63,310-->
  - communication / considerations ::@:: When implementing communication, there are many _practical_ considerations. <p> For example, using a physical string connected between two cups to communicate is impractical for many reasons. The distance between A and B shapes design goals: 10-km links differ fundamentally from meter-scale Bluetooth. <!--SR:!2025-12-12,64,310!2026-07-31,241,330-->
    - communication / considerations / historical comparison ::@:: Ancient smoke-fire signals transmitted a single bit across vast distances, marking an early form of digital communication. <p> Modern optical fibre now supports 10-km links with high data rates, low cost, and minimal noise—replacing older telephone cables that were expensive and suffered from poor quality due to limited media technology. <p> This progression from mechanical to electronic links illustrates how advances in media properties have expanded signal fidelity and reach, underscoring the fundamental role of medium characteristics in defining communication performance limits. <!--SR:!2026-02-11,89,369!2026-02-02,81,369-->
    - communication / considerations / attenuation ::@:: A simple mechanical telephone model transmits voice vibrations through a metal can and string, but energy lost to friction and air radiation caused rapid attenuation that limited its range to meters—showing why modern digital links require active amplification and low-loss media and revealing how physical losses bound channel capacity. <p> A historical intercom system in a Qing dynasty mansion used copper tubing as an acoustic guide to relay signals between rooms over a few metres, yet the same attenuation prevented scaling beyond building-scale distances. <p> Together these examples illustrate that engineering adapts medium properties—whether metal can, string, or copper waveguide—to meet specific application ranges while acknowledging fundamental limits imposed by physical loss mechanisms. <!--SR:!2026-02-05,84,369!2026-01-31,79,369-->
- [information](../../../../general/information.md) ::@:: It is an abstract concept that refers to something which has the power to inform. <!--SR:!2026-07-27,238,330!2026-08-22,259,330-->
  - information / signal processing ::@:: Information is represented by physical signals. <!--SR:!2026-08-07,247,330!2025-12-14,66,310-->
  - information / entropy ::@:: It of a random variable quantifies the average level of uncertainty or information associated with the variable's potential states or possible outcomes. <p> An important equation \(to be explained later\) to measure information entropy is: $$H(X) = -\sum_{X} p(X) \log_2 p(X) \,,$$ where $X$ is a discrete random variable with probability mass function $p(X)$. <!--SR:!2025-12-11,63,310!2026-08-03,244,330-->
- [signal processing](../../../../general/signal%20processing.md) ::@:: It is an electrical engineering subfield that focuses on analyzing, modifying and synthesizing signals, such as sound, images, potential fields, seismic signals, altimetry processing, and scientific measurements. <!--SR:!2026-08-31,266,330!2026-04-23,158,310-->
- [analog signal](../../../../general/analog%20signal.md) ::@:: It is any signal, typically a continuous-time signal, representing some other quantity, i.e., _analogous_ to another quantity. <!--SR:!2025-12-10,63,310!2026-08-16,255,330-->
  - analog signal / examples ::@:: ECG waveforms, voice recordings, etc. <!--SR:!2026-02-08,86,369!2026-02-05,84,369-->
  - analog signal / information ::@:: Information is encoded in measurable attributes such as amplitude, phase, or temporal shape; visualizing a waveform in the time domain instantly reveals its structure and shows how the signal’s form directly reflects the underlying content. <p> While entropy will formalize uncertainty in later courses, this course concentrates on intuitive signal interpretation. <!--SR:!2026-02-02,81,369!2026-02-02,81,369-->
- [time domain](../../../../general/time%20domain.md) ::@:: It is a representation of how a signal, function, or data set varies with time. It is used for the analysis of mathematical functions, physical signals or time series of economic or environmental data. <!--SR:!2025-12-10,62,310!2025-12-13,65,310-->
  - time domain / intuition ::@:: The signal is represented using a time function from zero time \(inclusive\) to infinite time \(exclusive\). Very visually intuitive. <!--SR:!2026-07-30,241,330!2026-08-11,251,330-->
- [periodic function](../../../../general/periodic%20function.md) ::@:: It is a function that repeats its values at regular intervals. <p> The length of the interval over which a periodic function repeats is called its __period__. Any function that is not periodic is called __aperiodic__. <!--SR:!2025-12-09,61,310!2025-12-15,67,310-->
  - periodic function / examples ::@:: For example, the trigonometric functions, which are used to describe waves and other repeating phenomena, are periodic. <!--SR:!2026-08-18,255,330!2026-08-08,246,330-->
  - periodic function / period ::@:: A positive number $T$ such that $f(t + T) = f(t)$ for all $t$. <!--SR:!2026-08-27,263,330!2026-08-12,250,330-->
  - periodic function / frequency ::@:: $f = 1 / T$ \(in hertz if $T$ is in second\) <!--SR:!2025-12-09,62,310!2025-12-15,67,310-->
  - periodic function / description ::@:: To describe the entire signal, describe a cycle suffices. <!--SR:!2026-08-09,249,330!2026-08-23,259,330-->
- [sine wave](../../../../general/sine%20wave.md) ::@:: It is a periodic wave whose waveform \(shape\) is the trigonometric sine function. <!--SR:!2025-12-09,61,310!2026-08-13,252,330-->
  - sine wave / sinusoid form ::@:: Sine waves of arbitrary phase and amplitude are called _sinusoids_ and have the general form: $$y(t)=A\sin(\omega t+\varphi )=A\sin(2\pi ft+\varphi )$$ where: <p> - $A$, _[amplitude](../../../../general/amplitude.md)_, the peak deviation of the function from zero. <br/> - $t$, the [real](../../../../general/real%20number.md) [independent variable](../../../../general/independent%20variable.md), usually representing [time](../../../../general/time.md) in [seconds](../../../../general/seconds.md). <br/> - $\omega$, _[angular frequency](../../../../general/angular%20frequency.md)_, the rate of change of the function argument in units of [radians per second](../../../../general/radians%20per%20second.md). <br/> - $f$, _[ordinary frequency](../../../../general/ordinary%20frequency.md)_, the _[number](../../../../general/real%20number.md)_ of oscillations \([cycles](../../../../general/turn%20(angle).md)\) that occur each second of time. <br/> - $\varphi$, _[phase](../../../../general/phase%20(waves).md)_, specifies \(in [radians](../../../../general/radian.md)\) where in its cycle the oscillation is at _t_ = 0. <!--SR:!2026-08-12,251,330!2026-08-21,258,330-->
  - sine wave / cosine wave ::@:: Since $$\begin{aligned} \sin x & = \cos(x - \pi / 2) \\ \cos x & = \sin(x + \pi / 2) \,, \end{aligned}$$ so any sine wave can be represented as a cosine wave with a shifted phase, and vice versa. <!--SR:!2025-12-12,64,310!2026-05-19,178,310-->
  - sine wave / description ::@:: To describe a sine wave, describe its amplitude $A$, angular frequency $\omega$, and phase $\phi$. <!--SR:!2026-08-16,255,330!2025-12-11,63,310-->
  - sine wave / significance ::@:: Grasping a sinusoid's key parameters—amplitude, frequency, and phase—is essential before tackling Fourier analysis or modulation concepts, because sinusoids form the building blocks for more complex signals central to communication theory. <p> Mastery of sinusoid representation provides the foundation needed to analyze channels, noise, and bandwidth throughout the course. <!--SR:!2026-02-06,85,369!2026-02-16,93,369-->
- [phasor](../../../../general/phasor.md) ::@:: It is a complex number representing a sinusoidal function whose amplitude _A_ and initial phase _θ_ are time-invariant and whose angular frequency _ω_ is fixed. <!--SR:!2026-08-26,262,330!2026-08-28,263,330-->
  - phasor / equation ::@:: $$s(t) = \Re(A \exp(j \phi) \exp(j \omega t)) = \Re(Z \exp(j \omega t)) \,.$$ $Z = A \exp(j \phi)$ is the _complex amplitude_, which incorporates both the amplitude and phase. <!--SR:!2025-12-10,63,310!2025-12-09,62,310-->
- [spectral density](../../../../general/spectral%20density.md) ::@:: Fourier analysis shows that any physical signal can be decomposed into a distribution of frequencies over a continuous range, where some of the power may be concentrated at discrete frequencies. The statistical average of the energy or power of any type of signal (including noise) as analyzed in terms of its frequency content, is called its __spectral density__. <!--SR:!2026-02-16,93,369!2026-02-04,83,369-->
  - spectral density / one-sided vs. two-sided ::@:: Some textbooks plot a two-sided spectrum that includes negative frequencies, while others show only the positive side \(one-sided\). <p> Negative frequencies appear when a real sinusoid is represented as a sum of a positive-frequency term and its complex conjugate. <p> A one-sided spectrum omits this redundant component because it can be recovered by symmetry for real signals. <!--SR:!2026-02-07,85,369!2026-02-09,87,369-->
- periodic function
  - periodic function / arithmetic operation ::@:: Performing arithmetic operations between two periodic functions may _not_ yield a periodic function. This happens when their angular frequencies do not have a least common multiple \(LCM\). For example, this happens when one of angular frequency is _irrational_. <!--SR:!2025-12-10,62,310!2026-08-26,262,330-->
  - periodic function / aperiodic ::@:: If a function is not periodic, then it is _aperiodic_. This happens if a positive $T$ such that $s(t + T) = s(t)$ for all $t$ does not exist. <!--SR:!2025-12-09,62,310!2025-12-15,67,310-->
- [Fourier transform](../../../../general/Fourier%20transform.md) ::@:: It is an integral transform that takes a function as input, and outputs another function that describes the extent to which various frequencies are present in the original function. The output of the transform is a complex-valued function of frequency. <!--SR:!2026-02-02,81,369!2026-02-02,81,369-->
  - Fourier transform / [transclude](transcludes/Fourier%20transform.md)
  - Fourier transform / intuition ::@:: Any periodic waveform can be decomposed into an infinite sum of sinusoids (Fourier series). <p> Non-periodic signals are represented by the continuous-frequency Fourier transform, which also uses sinusoidal basis functions. <!--SR:!2026-02-01,80,369!2026-02-04,83,369-->
  - Fourier transform / real signals ::@:: For real signals each sinusoid contributes a positive-frequency term plus its complex conjugate at negative frequency; this explains the two-sided nature of the spectrum in the exponential form. <!--SR:!2026-02-08,86,369!2026-02-11,89,369-->
- periodic function
  - periodic function / aperiodic
    - periodic function / aperiodic / examples ::@:: Common aperiodic waveforms include step, impulse (Dirac delta), and triangular pulse. <p> These signals do not repeat over time but serve as fundamental building blocks for system analysis (e.g., impulse response). <!--SR:!2026-02-11,89,369!2026-01-31,79,369-->
- [Heaviside step function](../../../../general/Heaviside%20step%20function.md) ::@:: It is a step function named after Oliver Heaviside, the value of which is zero for negative arguments and one for positive arguments. Different conventions concerning the value _H_\(0\) are in use. \(__this course__: _H_\(0\)&nbsp;=&nbsp;1\) <!--SR:!2026-08-14,253,330!2026-07-25,237,330-->
- [Dirac delta function](../../../../general/Dirac%20delta%20function.md) ::@:: It is a [generalized function](../../../../general/generalized%20function.md) on the [real numbers](../../../../general/real%20numbers.md), whose value is zero everywhere except at zero, and whose [integral](../../../../general/integral.md) over the entire real line is equal to one. Thus it can be [represented heuristically](../../../../general/heuristic.md) as $$\delta (x)={\begin{cases}0,&x\neq 0\\{\infty },&x=0\end{cases} }$$ such that $$\int _{-\infty }^{\infty }\delta (x)dx=1.$$ <!--SR:!2026-07-24,236,330!2026-08-10,250,330-->
- [ramp function](../../../../general/ramp%20function.md) ::@:: It is a unary real function, whose graph is shaped like a ramp. It can be expressed by numerous definitions, for example "0 for negative inputs, output equals input for non-negative inputs". <!--SR:!2025-12-14,66,310!2026-07-16,228,330-->
- [rectangular function](../../../../general/rectangular%20function.md) ::@:: It is defined as $$\operatorname {rect} \left({\frac {t}{a} }\right)=\Pi \left({\frac {t}{a} }\right)=\left\{ {\begin{array}{rl}0,&{\text{if } }|t|>{\frac {a}{2} }\\{\frac {1}{2} },&{\text{if } }|t|={\frac {a}{2} }\\1,&{\text{if } }|t|<{\frac {a}{2} }.\end{array} }\right.$$ Alternative definitions of the function define $\operatorname {rect} \left(\pm {\frac {1}{2} }\right)$ to be 0, or undefined. <!--SR:!2025-12-13,65,310!2026-02-04,89,270-->
- [triangular function](../../../../general/triangular%20function.md) ::@:: It is a function whose graph takes the shape of a triangle. Often this is an isosceles triangle of height 1 and base 2 in which case it is referred to as _the_ triangular function. <!--SR:!2025-12-15,67,310!2026-08-25,261,330-->
- analog signal
  - analog signal / basic operations ::@:: amplitude transformations: $As(t) + B$; $A$ scales the range about the horizontal axis and $B$ shifts vertically <br/> time reversal: $s(-t)$ \(special case of time scaling when $a = -1$\) <br/> time scaling: $s(at)$; compressed if $\lvert a \rvert > 1$ or expanded if $\lvert a \rvert < 1$ <br/> time shifting: $x(t - a)$; delayed \(moved towards the _right_\) by $a$ <!--SR:!2025-12-14,66,310!2025-12-09,62,310-->
- [digital signal](../../../../general/digital%20signal.md) ::@:: It is a signal that represents data as a sequence of discrete values; at any given time it can only take on, at most, one of a finite number of values. <p> \(__this course__: Both values and time are discrete for a digital signal. This is different from the definition used above.\) <!--SR:!2025-12-10,63,310!2026-08-15,254,330-->
  - digital signal / vs. analog signal ::@:: This _contrasts_ with an analog signal, which represents continuous values; at any given time it represents a real number within an infinite set of values. <p> \(__this course__: Both values and time are continuous for an analog signal. This is different from the definition used above.\) <!--SR:!2025-12-09,61,310!2025-12-15,67,310-->
- [analog-to-digital converter](../../../../general/analog-to-digital%20converter.md) \(ADC\) ::@:: It is a system that converts an analog signal, such as a sound picked up by a microphone or light entering a digital camera, into a digital signal. <!--SR:!2026-07-30,241,330!2026-08-15,254,330-->
  - analog-to-digital converter / steps ::@:: sampling → quantization <!--SR:!2025-12-10,63,310!2025-12-14,66,310-->
    - analog-to-digital converter / steps / sampling ::@:: Continuous time is converted into discrete time by repeated _sampling_ at a fixed time interval. <p> This limits _bandwidth_. According to the _Nyquist–Shannon sampling theorem_, _perfect reconstruction_ is possible if $B < f_s / 2$, where $B$ is the bandwidth of the continuous time signal and $f_s$ is the sample rate. <!--SR:!2026-09-01,267,330!2026-05-13,164,310-->
    - analog-to-digital converter / steps / quantization ::@:: Continuous value is converted into discrete value by converting them into _n_-bit numbers. <p> This produces _quantization error_, as continuous value has \(uncountably\) infinite possible values while _n_-bit numbers have finite possible values. Thus this process is _irreversible_ in general. <!--SR:!2026-08-20,257,330!2025-12-10,62,310-->
- [Nyquist–Shannon sampling theorem](../../../../general/Nyquist–Shannon%20sampling%20theorem.md) ::@:: It is an essential principle for digital signal processing linking the frequency range of a signal and the sample rate required to avoid a type of distortion called aliasing. The theorem states that the sample rate must be at least twice the bandwidth of the signal to avoid aliasing. <!--SR:!2025-12-12,64,310!2025-12-09,61,310-->
  - Nyquist–Shannon sampling theorem / applications ::@:: Enables technologies like TDMA in GSM and other digital communication schemes; without it, time-division multiplexing would lose information irrecoverably. <p> The theorem underpins all modern DSP because it guarantees that a continuous-time bandlimited signal can be fully captured by discrete samples. <!--SR:!2026-02-04,83,369!2026-02-11,89,369-->
- analog-to-digital converter
  - analog-to-digital converter / bit depth ::@:: Fewer bits → coarser signal levels → larger quantization noise; more bits → finer signal levels → smaller distortion. <p> The trade-off between storage/computation cost and signal fidelity is central to digital audio/video design. In consumer devices (phones, TVs), manufacturers choose sampling rates and bit depths that balance perceptual quality with power/size constraints. <!--SR:!2026-02-05,84,369!2026-02-16,93,369-->

## week 1 lecture 2

- datetime: 2025-09-04T09:00:00+08:00/2025-09-04T10:20:00+08:00, PT1H20M
- topic: digital signal; magnetic tape; digital audio; digital video; public switched telephone network; amplifier; data transmission; regenerator; frequency domain; amplitude spectrum; phase spectrum
- analog signal
- digital signal
  - digital signal / discrete-time signal ::@:: Only the time axis is sampled (discrete), but the amplitude may still be continuous \(or not\); these are not yet digital signals. <!--SR:!2026-02-10,88,369!2026-02-10,88,369-->
- analog-to-digital converter
- Nyquist–Shannon sampling theorem
- analog-to-digital converter
  - analog-to-digital converter / bit depth
    - analog-to-digital converter / bit depth / effects ::@:: The error introduced equals the difference between the original sample and its nearest quantization level; the worst-case error is half the step size $\Delta / 2$. <p> Increasing the number of bits halves $\Delta$ (e.g., moving from 3 to 4 bits doubles the number of levels), thereby reducing the maximum quantization error by a factor of two. <!--SR:!2026-02-16,93,369!2026-02-16,93,369-->
- [signal-to-noise ratio](../../../../general/signal-to-noise%20ratio.md) \(SNR, S/N\) ::@:: It is a measure used in science and engineering that compares the level of a desired signal to the level of background noise. SNR is defined as the ratio of signal power to noise power, often expressed in decibels. <!--SR:!2026-02-06,85,369!2026-02-16,93,369-->
  - signal-to-noise ratio / formula ::@:: $$\text{SNR} = \frac {\text{signal (without noise) power} } {\text{noise power} } \,.$$ However, it is often expressed in decibels \(dB\) instead: $$\text{SNR}_{\text{dB} } = 10 \log_{10} \text{SNR} \,.$$ 0 dB means same the signal has the same power as noise. Every 10&nbsp;dB increase in SNR multiplies the signal power by 10, so that 10&nbsp;dB means 10 times, 20&nbsp;dB means 100 times, 30&nbsp;dB means 1000 times, etc. <!--SR:!2026-02-06,85,369!2026-02-15,92,369-->
    - signal-to-noise ratio / formula / amplitude ::@:: When we work with signal amplitudes rather than powers, the definition of SNR is still based on power. <p> Because electrical power is proportional to the square of voltage (or current), converting this amplitude ratio into decibels uses a factor of 20 instead of 10: $$\boxed{\;\text{SNR}_{\text{dB} }=20\,\log_{10}\!\left(\frac{A_{\text{signal} } }{A_{\text{noise} } }\right)\;} \,.$$ <p> This formula is equivalent to the power-based expression $10\log_{10}(\text{SNR})$ because $(A_{\text{signal} }/A_{\text{noise} })^2 = \text{SNR}$. Thus, a 10-fold increase in amplitude ratio corresponds to a 100-fold increase in \(power\) SNR. <!--SR:!2026-02-06,85,369!2026-01-11,59,349-->
  - signal-to-noise ratio / quantization ::@:: Under common assumptions—input is a sinusoid, noise uniformly distributed over $[-\Delta/2,\;\Delta/2]$—the SNR improves roughly $6.02\,\text{dB}$ per added bit: $$\text{SNR}_{\text{dB} } \approx 6.02\,n + C$$ where $n$ is bits per sample and $C$ depends on the signal shape \(for sine wave, $C = 20 \log_{10}\left(\sqrt{3 / 2}\right) \approx 1.761$\). <p> This rule of thumb guides how many bits are needed for a target audio or communication quality. Note real signals like speech have different dynamic ranges, so the actual SNR may deviate from this simple estimate. <!--SR:!2026-01-09,61,349!2025-12-20,41,329-->
    - signal-to-noise ratio / quantization / examples ::@:: High-fidelity audio (CD) requires about 16 bits/sample to achieve an SNR sufficient for music listening; the standard sampling rate is 44.1 kHz, exceeding twice the audible bandwidth (~20 kHz). <p> Telephony uses only 8 bits/sample at a lower sampling rate (8 kHz), yielding a lower SNR that is adequate for voice but noticeably poorer than CD audio. <!--SR:!2026-02-06,85,369!2026-02-02,81,369-->
- analog-to-digital converter
  - analog-to-digital converter / bit depth
    - analog-to-digital converter / bit depth / examples ::@:: In digital communications, the receiver's analog-to-digital converter must preserve the signal-to-noise ratio needed by the modulation scheme; higher-order constellations demand more bits. <p> Typical design practice employs 10–12 bits for the ADC path when high-order modulations (e.g., 64-QAM, 256-QAM) are used to maintain acceptable error rates. <!--SR:!2026-02-10,88,369!2026-02-17,94,369-->
- signal-to-noise ratio
  - signal-to-noise ratio / dynamic range \(DR\) ::@:: It—the ratio between maximum and minimum signal amplitudes—affects how many quantization levels are required to achieve a given SNR for non-sinusoidal inputs. <!--SR:!2026-02-17,94,369!2026-02-01,80,369-->
- [digital-to-analog converter](../../../../general/digital-to-analog%20converter.md) \(DAC\) ::@:: It is a system that converts a digital signal into an analog signal. <!--SR:!2025-12-09,62,310!2026-07-29,240,330-->
  - digital-to-analog converter / reverse ::@:: An analog-to-digital converter \(ADC\) performs the reverse function. <!--SR:!2026-08-13,251,330!2026-08-01,242,330-->
  - digital-to-analog converter / steps ::@:: reconstruction → lowpass filter <!--SR:!2025-12-14,66,310!2026-09-02,268,330-->
    - digital-to-analog converter / steps / reconstruction ::@:: Discrete time is converted into continuous time. <p> Each incoming B-bit word is translated to a voltage level via a pre-computed table (e.g., for 4 bits → 16 levels). The "zero-order hold" (a simple capacitor) holds that voltage constant until the next sample arrives, creating a staircase waveform. <!--SR:!2026-07-28,239,330!2026-06-12,186,310-->
    - digital-to-analog converter / steps / lowpass filter ::@:: Discrete value is converted into continuous value. Holding the sampled value until the next sample yields a continuous-time signal with discrete value. Applying lowpass filter smoothens the signal and make it continuous-valued as well. <p> The lowpass filter frequency cutoff is usually half the sample rate due to the _Nyquist–Shannon sampling theorem_.  If the original signal does not have frequencies higher than this cutoff, the only remaining error is quantization noise. <!--SR:!2026-07-26,237,330!2026-08-11,251,330-->
- analog signal
  - analog signal / disadvantages ::@:: ADC/DAC chips sit at the interface between noisy analog front-ends and high-speed digital logic. <p> They must be shielded against clock-switching noise, power-gating glitches, and substrate coupling—all of which can corrupt the analog signal path. <p> High-resolution, high-sampling-rate devices are expensive, sometimes export-controlled, and require careful PCB layout to maintain performance. <!--SR:!2026-02-06,85,369!2026-02-11,89,369-->
- digital signal
  - digital signal / advantages ::@:: It is _robust_ to degradation and noise, as small distortions of the waveform can be completely ignored. The mapping from waveform to bits introduces a decision threshold; only if noise pushes the signal past that threshold does an error occur. <!--SR:!2026-08-04,245,330!2026-08-10,248,330-->
  - digital signal / disadvantages ::@:: It cannot represent most physical signals _exactly_, as most of them are analog in nature. <!--SR:!2025-12-10,62,310!2026-08-08,248,330-->
  - digital signal / usage ::@:: Due to its robustness, it is used in storage and telecommunications. <!--SR:!2025-12-10,63,310!2025-12-12,64,310-->
    - digital signal / usage / storage ::@:: Analog storage (e.g., magnetic tape) degrades visibly over decades, while digital media (CDs, MP3s) retain fidelity for many years with negligible error. <!--SR:!2026-07-15,227,330!2026-07-20,232,330-->
    - digital signal / usage / telecommunications ::@:: Long-distance transmission cause path loss attenuation and thermal noise. If an analog signal is used, signal-to-noise ratio \(SNR\) decreases significantly at the receiver side, and may corrupt an analog waveform entirely. <p> If a digital signal is used, SNR remains sufficiently high due to its robustness to degradation and noise. As long as received bits are correctly interpreted, the information survives. <!--SR:!2025-12-13,65,310!2026-07-23,235,330-->
- [magnetic tape](../../../../general/magnetic%20tape.md) ::@:: It is a medium for magnetic storage made of a thin, magnetizable coating on a long, narrow strip of plastic film. It was developed in Germany in 1928, based on the earlier magnetic wire recording from Denmark. <!--SR:!2026-02-17,94,369!2026-02-09,87,369-->
  - magnetic tape / recording ::@:: A coil driven by an audio waveform induces a time-varying magnetic field that aligns microscopic magnetic domains on the tape; this alignment stores the signal as a pattern of magnetization. <!--SR:!2026-02-10,88,369!2026-02-08,86,369-->
  - magnetic tape / playback ::@:: During playback, the moving tape passes through a read head where the changing magnetization again induces a voltage in the coil, which is amplified to recover the audio waveform. <!--SR:!2026-02-11,89,369!2026-02-03,82,369-->
  - magnetic tape / degradation ::@:: The stored magnetization is not at its natural (minimum-energy) state; over time thermal agitation causes random domain flips that shift the recorded pattern. After decades of storage the tape's magnetic domains drift from their intended positions, so playback yields a distorted waveform and audible quality loss. <P> Thus, while analog tape offers compact physical storage, its fidelity degrades irreversibly with environmental noise and time. <!--SR:!2026-02-07,85,369!2026-02-17,94,369-->
- [digital audio](../../../../general/digital%20audio.md) ::@:: It is a representation of sound recorded in, or converted into, digital form. In digital audio, the sound wave of the audio signal is typically encoded as numerical samples in a continuous sequence. <!--SR:!2026-02-16,93,369!2026-02-14,91,369-->
  - digital audio / sampling rate ::@:: Human hearing tops out around 20 kHz; to satisfy the Nyquist criterion we sample at least twice this bandwidth. <p> CDs use a slightly higher rate of 44.1 kHz to give implementation margin, plus 16-bit quantization for high-fidelity representation. <!--SR:!2026-01-31,79,369!2026-02-07,85,369-->
  - digital audio / pulse-code modulation \(PCM\) ::@:: With two stereo channels, the raw data stream is 44.1 k × 16 bits × 2 ≈ 1.411 Mbps, yielding about 53 MB per five-minute track in uncompressed WAV form. <p> Pulse-code modulation (PCM) converts the analog waveform into a binary sequence; this digital representation is immune to gradual physical drift and can be stored as a stable file. <!--SR:!2026-02-11,89,369!2026-02-11,89,369-->
  - digital audio / formats ::@:: Lossless formats like WAV preserve every bit of the original PCM stream, whereas lossy codecs such as MP3 discard perceptually insignificant bits to reduce size by roughly an order of magnitude. <!--SR:!2026-02-05,84,369!2026-02-03,82,369-->
- [digital video](../../../../general/digital%20video.md) ::@:: It is an electronic representation of moving visual images (video) in the form of encoded digital data. This is in contrast to analog video, which represents moving visual images in the form of analog signals. <!--SR:!2026-02-17,94,369!2026-02-02,81,369-->
  - digital video / historical context ::@:: In the early 1990s, analog audio could be digitized into a manageable data rate; however, a two-hour movie would require many CD-size discs if encoded directly with PCM. <p> The missing ingredient was an efficient compression engine that exploits human visual perception (e.g., MPEG-1 for VCD). <!--SR:!2026-02-03,82,369!2026-02-17,94,369-->
  - digital video / compression ::@:: Once such lossy video codecs were available in the late 1990s, entire movies fit onto a single disc or cartridge, making digital video commercially viable. Subsequent generations (DVD, Blu-ray) introduced higher-order MPEG variants (MPEG-2, MPEG-4) to further reduce bitrate while maintaining acceptable visual quality. <p> This illustrates the trade-off: raw digitization gives robustness but enormous storage; compression reduces size at the cost of irreversibly discarding data. <!--SR:!2026-02-03,82,369!2026-02-10,88,369-->
- [public switched telephone network](../../../../general/public%20switched%20telephone%20network.md) \(PSTN\) ::@:: It is the aggregate of the world's telephone networks that are operated by national, regional, or local telephony operators. It provides infrastructure and services for public telephony. <!--SR:!2026-02-05,84,369!2026-02-11,89,369-->
  - public switched telephone network / medium ::@:: A typical PSTN call starts with a two-wire copper "local loop" that supplies 48 V for line power and carries the voice waveform to the switching office. For intercity or international links, the signal travels over long coaxial cables (often submarine) which act as transmission lines. <!--SR:!2026-02-16,93,369!2026-02-11,89,369-->
    - public switched telephone network / medium / loss ::@:: In an ideal lossless line, inductors and capacitors would preserve energy; real cables contain resistive elements that cause $I^2 R$ losses and therefore attenuation of the signal. <p> Thermal noise generated in these resistances adds a constant background power that does not diminish with distance, so as the signal attenuates the signal-to-noise ratio (SNR) degrades. <p> A minimum acceptable SNR imposes a hard limit on how far an analog voice signal can travel without regeneration. <!--SR:!2026-02-01,80,369!2026-02-12,89,369-->
    - public switched telephone network / medium / regeneration ::@:: Amplifiers can boost a weak received signal, but they also amplify the accompanying thermal noise unless perfect filtering is applied—an impractical ideal. <p> Consequently, while repeaters (signal regenerators) are used in telephone networks to restore both amplitude and shape, purely linear amplification cannot overcome the fundamental SNR ceiling set by cable losses. <!--SR:!2026-02-11,89,369!2026-02-15,92,369-->
    - public switched telephone network / medium / digital aspects ::@:: The need for intermediate regeneration points motivates digital switching: digitizing the signal at each node restores a clean waveform without cumulative noise. <!--SR:!2026-02-06,85,369!2026-02-16,93,369-->
- [amplifier](../../../../general/amplifier.md) ::@:: It is an electronic device that can increase the magnitude of a signal (a time-varying voltage or current). It is a two-port electronic circuit that uses electric power from a power supply to increase the amplitude (magnitude of the voltage or current) of a signal applied to its input terminals, producing a proportionally greater amplitude signal at its output. <!--SR:!2026-02-15,92,369!2026-02-10,88,369-->
  - amplifier / signal-to-noise ratio ::@:: An amplifier only boosts the received voltage; it also amplifies all existing noise, so the output SNR is never higher than the input SNR (and typically lower because of the amplifier's own noise figure). <!--SR:!2026-02-09,87,369!2026-02-09,87,369-->
    - amplifier / signal-to-noise ratio / implications ::@:: Therefore, adding a receiver-side amplifier cannot extend the usable link distance if the incoming SNR is already too low. The only practical way to increase range with a fixed power budget is to raise the transmitted power itself, which is limited by regulations and hardware capabilities. <!--SR:!2026-02-07,85,369!2026-01-31,79,369-->
- [data transmission](../../../../general/data%20transmission.md) ::@:: It is the transfer of data over a point-to-point or point-to-multipoint communication channel. <!--SR:!2026-02-14,91,369!2026-02-05,84,369-->
  - data transmission / analog ::@:: In an analog link any waveform distortion directly corrupts the conveyed information because the signal is continuous. <!--SR:!2026-02-05,84,369!2026-02-08,86,369-->
  - data transmission / digital ::@:: Digital links first perform A/D conversion (e.g., PCM), turning the waveform into a bitstream; the bits are then mapped onto a carrier such as on-off keying. <p> Distortions that still allow correct bit decision do not affect the recovered data: after decoding and DAC, the original waveform is reconstructed up to quantization noise. <p> Quantization noise depends only on the chosen bit resolution and is independent of channel length, so it can be controlled separately from propagation loss. <!--SR:!2026-02-11,89,369!2026-02-16,93,369-->
- [regenerator](../../../../general/regenerator%20(telecommunications).md) ::@:: It in a telecommunications context is a type of repeater that is used in copper line or optical fibre line transmission systems. The regeneration function involved also appears in other types of systems, e.g. computer networking systems. <!--SR:!2026-02-17,94,369!2026-01-31,79,369-->
  - regenerator / operation ::@:: A repeater receives a distorted but still decodable signal, recovers the bits, and retransmits a freshly regenerated clean waveform. <!--SR:!2026-02-15,92,369!2026-02-06,85,369-->
  - regenerator / use ::@:: This decode-and-forward operation breaks the cumulative degradation that would otherwise limit analog links; each stage can be as long as desired provided its input is above the decoding threshold. <p> By chaining multiple repeaters one can span arbitrarily long distances while preserving data integrity, assuming adequate power and bandwidth at each node. However, the data rate remains bounded by channel bandwidth and link quality. <!--SR:!2026-02-09,87,369!2026-02-10,88,369-->
- [data compression](../../../../general/data%20compression.md) ::@:: It is the process of encoding information using fewer bits than the original representation. Any particular compression is either lossy or lossless. <!--SR:!2026-02-03,82,369!2026-02-06,85,369-->
  - data compression / communications ::@:: While repeaters solve range, the data rate remains bounded by channel bandwidth and link quality. <p> To transmit more bits within the same bandwidth, the raw PCM bitstream must be compressed (lossless or lossy); otherwise the stream would be too large for storage or transmission. <p> Compression therefore becomes an essential part of any practical digital communication system. <!--SR:!2026-02-17,94,369!2026-02-17,94,369-->
- time domain
- [frequency domain](../../../../general/frequency%20domain.md) ::@:: It refers to the analysis of mathematical functions or signals with respect to frequency (and possibly phase), rather than time, as in time series. <!--SR:!2026-02-14,91,369!2026-02-04,83,369-->
  - frequency domain / vs. time domain ::@:: While a time-domain graph shows how a signal changes over time, a frequency-domain graph shows how the signal is distributed within different frequency bands over a range of frequencies. <!--SR:!2026-02-10,88,369!2026-02-01,80,369-->
  - frequency domain / sinusoids ::@:: A complex valued frequency-domain representation consists of both the magnitude and the phase of a set of sinusoids (or other basis waveforms) at the frequency components of the signal. <!--SR:!2026-02-03,82,369!2026-02-03,82,369-->
  - frequency domain / amplitude spectrum ::@:: Treat each sinusoid as a "LEGO block" characterized by three numbers: frequency $f_i$, amplitude $a_i$, and phase $\phi_i$. <p> Plotting all $a_i$ versus their corresponding $f_i$ yields the _amplitude spectrum_; this graph is just another way to list the LEGO parameters. <!--SR:!2026-02-17,94,369!2026-02-11,89,369-->
  - frequency domain / phase spectrum ::@:: Treat each sinusoid as a "LEGO block" characterized by three numbers: frequency $f_i$, amplitude $a_i$, and phase $\phi_i$. <p> Similarly, plotting each $\phi_i$ against $f_i$ produces the _phase spectrum_, completing a graphical description of the signal's spectral content. <!--SR:!2026-02-16,93,369!2026-02-06,85,369-->
  - frequency domain / spectrums ::@:: The amplitude spectrum tells how much energy is present at each frequency; the phase spectrum indicates the time shift of that component. With both graphs, one can reconstruct the original waveform via an inverse Fourier series or transform. <p> This two-graph approach replaces a raw list of parameters with a visual tool that is easier to interpret and compare across signals. <!--SR:!2026-02-06,85,369!2026-02-11,89,369-->
- spectral density
  - spectral density / one-sided vs. two-sided
    - spectral density / one-sided vs. two-sided / one-sided ::@:: If the building blocks of a signal are _chosen_ to be real sinusoids, the spectrum is naturally one-sided—only the positive side needs to be plotted. <!--SR:!2026-02-11,89,369!2026-02-02,81,369-->
    - spectral density / one-sided vs. two-sided / two-sided ::@:: _Choosing_ a compressed sinusoid (a complex exponential) to represent a signal forces the signal to be represented as two symmetric halves: a positive-frequency part and its conjugate negative-frequency counterpart. <!--SR:!2026-02-07,85,369!2026-02-07,85,369-->

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

## week 2 lecture

- datetime: 2025-09-09T09:00:00+08:00/2025-09-09T10:20:00+08:00, PT1H20M
- topic: time domain; frequency domain; spectrums; real sinusoid; complex sinusoid; Fourier transform; Parseval's theorem; Plancherel theorem; bandwidth; Nyquist–Shannon sampling theorem; wireless; analog transmission; digital transmission
- time domain
- frequency domain
  - frequency domain / amplitude spectrum
  - frequency domain / frequency spectrum
  - frequency domain / spectrums
- spectral density
  - spectral density / one-sided vs. two-sided
- sine wave
  - sine wave / complex sinusoids ::@:: A real sinusoid can be expressed as the sum of two opposite-frequency complex exponentials: $$\cos(\omega t)=\frac{e^{j\omega t}+e^{-j\omega t} }{2}, \qquad \sin(\omega t)=\frac{e^{j\omega t}-e^{-j\omega t} }{2j} \,.$$ These identities show that a single cosine or sine is equivalent to two complex sinusoids—one at +ω and one at –ω—with equal magnitude but opposite phase. <p> In contrast, the phasor representation bundles both amplitude and phase into one complex exponential, $A e^{j(\omega t+\theta)}$, which automatically accounts for the positive-frequency component while its conjugate provides the negative-frequency counterpart. <!--SR:!2026-02-16,93,369!2026-02-17,94,369-->
- phasor
  - phasor / equation
- Fourier transform
  - Fourier transform / definition ::@:: The Fourier transform of a complex-valued function $f(x)$ on the real line, is the complex valued function ${\widehat {f} }(\xi )$, defined by the integral $${\widehat {f} }(\xi )=\int _{-\infty }^{\infty }f(x)\ e^{-i2\pi \xi x}\,dx,\quad \forall \xi \in \mathbb {R} \,.$$ In this case $f(x)$ is \(Lebesgue\) integrable over the whole real line, i.e., the above integral converges to a continuous function ${\widehat {f} }(\xi )$ at all $\xi$ \(decaying to zero as $\xi \to \infty$\). <p> \(__this course__: __Important__. Prefer using the angular frequency one.\) <!--SR:!2026-02-09,87,369!2026-02-08,86,369-->
    - Fourier transform / definition / intuition ::@:: These integrals are conceptually "uncountable sums" that capture all sinusoidal components simultaneously. <!--SR:!2026-02-16,93,369!2026-02-08,86,369-->
    - Fourier transform / definition / angular frequency ::@:: The Fourier transform of a complex-valued function $f(x)$ on the real line, expressed with angular frequency $\omega$, is $${\widehat{f} }_{\!a}(\omega)=\int_{-\infty}^{\infty} f(x)\,e^{-i\,\omega x}\,\mathrm dx, \qquad \forall\,\omega\in\mathbb R \,.$$ <p> Here the kernel uses $e^{-i\omega x}$ rather than $e^{-i2\pi\xi x}$; consequently, $\omega=2\pi\xi$. <p> \(__this course__: __Important__. Prefer using the angular frequency one.\) <!--SR:!2026-02-27,103,385!2026-02-26,102,385-->
  - Fourier transform / inverse definition ::@:: First introduced in [Fourier's](../../../../general/Joseph%20Fourier.md) _Analytical Theory of Heat_., the corresponding inversion formula for "[sufficiently nice](../../../../general/Fourier%20inversion%20theorem.md#conditions%20on%20the%20function)" functions is given by the [Fourier inversion theorem](fourier%20inversion%20theorem.md), i.e., $$f(x)=\int _{-\infty }^{\infty }{\widehat {f} }(\xi )\ e^{i2\pi \xi x}\,d\xi ,\quad \forall \ x\in \mathbb {R} \,.$$ <!--SR:!2026-02-11,89,369!2026-02-11,89,369-->
    - Fourier transform / inverse definition / angular frequency ::@:: First introduced in [Fourier's](../../../../general/Joseph%20Fourier.md) _Analytical Theory of Heat_, the corresponding inversion formula for "sufficiently nice" functions is given by the Fourier inversion theorem, but expressed with angular frequency _ω_ instead of linear frequency _f_: $$f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\widehat f_a(\omega)\,e^{j\omega t}\,d\omega,\quad \forall\,t\in\mathbb R \,.$$ <p> Here the integration variable is now _ω_ \(radians / second\) rather than _f_ \(hertz\), changing the prefactor from 1 to $1/(2\pi)$. <p> \(__this course__: __Important__. Prefer using the angular frequency one.\) <!--SR:!2026-02-23,99,385!2026-02-25,101,385-->
  - Fourier transform / pair ::@:: The functions $f$ and ${\widehat {f} }$ are referred to as a __Fourier transform pair__. A common notation for designating transform pairs is: $$f(x)\ {\stackrel {\mathcal {F} }{\longleftrightarrow } }\ {\widehat {f} }(\xi ).$$ For example, the Fourier transform of the delta function is the constant function $1$: $$\delta (x)\ {\stackrel {\mathcal {F} }{\longleftrightarrow } }\ 1.$$ <!--SR:!2026-02-10,88,369!2026-02-05,84,369-->
- [Parseval's theorem](../../../../general/Parseval's%20theorem.md) ::@:: It usually refers to the result that the Fourier transform is unitary; loosely, that the sum (or integral) of the square of a function is equal to the sum (or integral) of the square of its transform. <!--SR:!2026-02-11,89,369!2026-02-11,89,369-->
  - Parseval's theorem / statement ::@:: Let _f_\(_x_\) and _g_\(_x_\) be integrable, and let _f̂_\(_ξ_\) and _ĝ_\(_ξ_\) be their Fourier transforms. If _f_\(_x_\) and _g_\(_x_\) are also [square-integrable](../../../../general/square-integrable.md), then the Parseval formula follows: $$\langle f,g\rangle _{L^{2} }=\int _{-\infty }^{\infty }f(x){\overline {g(x)} }\,dx=\int _{-\infty }^{\infty }{\widehat {f} }(\xi ){\overline { {\widehat {g} }(\xi )} }\,d\xi ,$$ where the bar denotes [complex conjugation](../../../../general/complex%20conjugation.md).  <p> Note the input $\xi$ in the second integral and its infinitesimal $\mathrm d\xi$ is linear frequency. For the input $\omega = 2\pi \xi$ and its infinitesimal $\mathrm d\omega = 2\pi \,\mathrm d\xi$, a factor of $1 / 2\pi$ appears outside the second integral. <!--SR:!2026-01-20,66,349!2026-02-05,84,369-->
- [Plancherel theorem](../../../../general/Plancherel%20theorem.md) ::@:: It is a result in harmonic analysis, proven by Michel Plancherel in 1910. It is a generalization of Parseval's theorem; often used in the fields of science and engineering, proving the unitarity of the Fourier transform. <!--SR:!2026-02-14,91,369!2026-02-11,89,369-->
  - Plancherel theorem / statement ::@:: The [Plancherel theorem](../../../../general/Plancherel%20theorem.md), which follows from the Parseval's theorem, states that $$\|f\|_{L^{2} }^{2}=\int _{-\infty }^{\infty }\left|f(x)\right|^{2}\,dx=\int _{-\infty }^{\infty }\left|{\widehat {f} }(\xi )\right|^{2}\,d\xi .$$  <p> Note the input $\xi$ in the second integral and its infinitesimal $\mathrm d\xi$ is linear frequency. For the input $\omega = 2\pi \xi$ and its infinitesimal $\mathrm d\omega = 2\pi \,\mathrm d\xi$, a factor of $1 / 2\pi$ appears outside the second integral. <!--SR:!2026-02-17,94,369!2026-02-04,83,369-->
- Fourier transform
  - Fourier transform / computation ::@:: Start with the definition and work through a few basic cases (impulse → flat spectrum; rectangular pulse → sinc). Once comfortable, use properties: linearity, time-shifting ($x(t-t_0)$ adds a phase factor $e^{-j2\pi ft_0}$), frequency scaling, and conjugation. <p> This mirrors how differentiation is learned: first principle → few examples → rules that let you avoid re-deriving each new function. <!--SR:!2026-02-05,84,369!2026-02-03,82,369-->
- [bandwidth](../../../../general/bandwidth%20(signal%20processing).md) ::@:: It is the difference between the upper and lower frequencies in a continuous band of frequencies. It is typically measured in unit of hertz (symbol Hz). <!--SR:!2026-02-05,84,369!2026-02-06,85,369-->
  - bandwidth / intuition ::@:: Bandwidth can be defined as the frequency range over which a signal's energy \(or magnitude\) is significant. <p> Bandwidth thus links the abstract spectral description with concrete hardware requirements. For example, we can say "keep enough frequencies so that only 1% of the total energy is lost". This is known as _energy bandwidth_. <!--SR:!2026-02-11,89,369!2026-01-31,79,369-->
  - bandwidth / subcategories ::@:: It may refer more specifically to two subcategories: _passband bandwidth_ and _baseband bandwidth_. <!--SR:!2026-02-17,94,369!2026-02-05,84,369-->
  - bandwidth / passband bandwidth ::@:: It is the difference between the upper and lower cutoff frequencies of, for example, a band-pass filter, a communication channel, or a signal spectrum. <!--SR:!2026-02-08,86,369!2026-02-05,84,369-->
  - bandwidth / baseband bandwidth ::@:: It is equal to the upper cutoff frequency of a low-pass filter or baseband signal, which includes a zero frequency. <!--SR:!2026-02-13,90,369!2026-02-17,94,369-->
  - bandwidth / computation ::@:: In practice, we may compute bandwidth according to hardware requirements using different methods, obtaining different bandwidths. <p> Some possible definitions are: energy bandwidth, 3 db bandwidth, zero-crossing bandwidth, etc. Each definition yields a different numerical value; always state which convention you are using when quoting a bandwidth. <!--SR:!2026-02-05,84,369!2026-02-11,89,369-->
    - bandwidth / computation / energy ::@:: The bandwidth that keeps enough frequencies such that only a certain percentage of total energy is lost. <!--SR:!2026-02-13,90,369!2026-02-07,85,369-->
    - bandwidth / computation / 3 dB ::@:: The width between points where the amplitude spectrum has dropped by 3 dB (half power) from its peak. <!--SR:!2026-02-17,94,369!2026-02-17,94,369-->
    - bandwidth / computation / zero-crossing ::@:: Use the first zero crossing of the amplitude spectrum as the cutoff, assuming the amplitude spectrum starts off nonzero at zero frequency. <!--SR:!2026-02-11,89,369!2026-02-06,85,369-->
- spectral density
  - spectral density / intuition ::@:: A waveform with sharp transitions (e.g., a rectangular pulse) needs high-frequency components to reproduce the discontinuity, so it has a broader spectrum. A smooth pulse concentrates most energy in lower frequencies, giving a narrower bandwidth. <p> Thus, by inspecting the time-domain shape you can guess whether its Fourier spectrum will be wide or narrow without explicit calculation. <!--SR:!2026-02-11,89,369!2026-01-31,79,369-->
- bandwidth
  - bandwidth / time–bandwidth tradeoff ::@:: For any signal, the product of pulse duration $T$ and bandwidth $W$ satisfies $T\,W \geqslant \text{constant}$. <p> Compressing a pulse in time (reducing $T$) forces an increase in its spectral width ($W$), often by roughly a factor of two. This trade-off underlies many engineering limits, such as the minimum achievable symbol duration for a given channel bandwidth. <!--SR:!2026-02-05,84,369!2026-02-11,89,369-->
  - In practice, if a signal is band-limited to $B$ Hz, then sampling at any rate greater than $2B$ samples per second guarantees perfect reconstruction (Nyquist–Shannon).
- Fourier transform
  - Fourier transform / computation
    - Fourier transform / computation / properties ::@:: Key properties—time shifting, scaling, modulation, convolution—allow you to manipulate spectra without re-deriving the full integral. Knowing these rules lets you compute transforms for many common signals quickly, rather than starting from the definition every time. <!--SR:!2026-02-11,89,369!2026-02-05,84,369-->
- Nyquist–Shannon sampling theorem
  - Nyquist–Shannon sampling theorem / frequency domain ::@:: sampling is pointwise multiplication in the time domain → sampling is convolution in the frequency domain <!--SR:!2026-02-11,89,369!2026-02-09,87,369-->
    - Nyquist–Shannon sampling theorem / frequency domain / mathematics ::@:: Sampling a continuous signal can be written as $$y(t)=x(t)\,\mathrm{III}_{T_s}(t),\qquad \mathrm{III}_{T_s}(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT_s) \,,$$ where the Dirac comb $\mathrm{III}_{T_s}$ has period $T_s=1/f_s$. In the frequency domain this multiplication becomes a convolution: $$Y(f)=X(f)*\frac{1}{T_s}\sum_{k=-\infty}^{\infty}\delta\!\left(f-\tfrac{k}{T_s}\right) =\frac{1}{T_s}\sum_{k=-\infty}^{\infty}X\!\bigl(f-kf_s\bigr) \,,$$ so the spectrum of $x(t)$ is replicated at every integer multiple of the sampling frequency $f_s$. <!--SR:!2025-12-20,41,329!2026-02-12,89,369-->
    - Nyquist–Shannon sampling theorem / frequency domain / conclusion ::@:: If the sampling period satisfies $$T_s \le \frac{1}{2B}\;\;\Longleftrightarrow\;\; f_s \ge 2B \,,$$ then the shifted copies of $X(f)$ produced by the Dirac comb do not overlap. <p> Consequently a low-pass filter that keeps only the baseband component can recover the original signal without loss. <!--SR:!2026-02-17,94,369!2026-02-05,84,369-->
- frequency domain
  - frequency domain / compression ::@:: In the time domain, every sample appears equally important; you cannot prune samples without potentially large errors. In the frequency domain, many sinusoid coefficients have negligible amplitude; discarding them loses little energy \(e.g., 1%\). <p> This selective pruning is the basis of audio/video codecs and other compression schemes that store only the "important" spectral components. <!--SR:!2026-02-01,80,369!2026-01-31,79,369-->
    - frequency domain / compression / examples ::@:: The human ear can perceive frequencies up to about 20 kHz. CDs use a sampling rate of 44.1 kHz, which is more than twice this limit, satisfying the Nyquist criterion while leaving a safety buffer for filter design. <p> With the additional margin, CD audio decoders can employ practical anti-aliasing filters whose transition bands are wide enough to be realized with stable digital or analog circuits, avoiding the instability of a perfect cutoff. <!--SR:!2026-02-14,91,369!2026-02-13,90,369-->
  - frequency domain / algorithms ::@:: Operations like filtering, modulation, or convolution become simple multiplications or scalings in the frequency domain. Many algorithms (e.g., FFT-based convolution) exploit this property to achieve orders of magnitude speedups over time-domain equivalents. <!--SR:!2026-02-04,83,369!2026-02-11,89,369-->
  - frequency domain / transfer function ::@:: Understanding a system's transfer function is straightforward when expressed as multiplication by its spectral response. <!--SR:!2026-02-08,86,369!2026-02-16,93,369-->
  - frequency domain / basis ::@:: The Fourier basis is one choice; wavelet transforms, Hadamard matrices, and other "lego" sets can provide sparser representations for specific signal types. <p> Selecting a basis that aligns with the signal's structure often yields even greater compression or easier processing than plain sinusoids \(Fourier basis\). <!--SR:!2026-02-17,94,369!2026-02-11,89,369-->
  - frequency domain / filters ::@:: In communications, additive white Gaussian noise occupies a broad frequency band, while useful signals are confined to specific subbands. A low-pass or band-pass filter can suppress out-of-band noise, yielding a cleaner signal even though in-band noise remains. <p> If two signals occupy distinct frequency ranges, the receiver can separate them using appropriate filtering—an operation impossible when only time-domain samples are considered because additive operations cannot be undone without additional information. <!--SR:!2026-02-12,89,369!2026-02-03,82,369-->
- [wireless](../../../../general/wireless.md) ::@:: It is the transfer of information (telecommunication) between two or more points without the use of an electrical conductor, optical fiber or other continuous guided medium for the transfer. The most common wireless technologies use radio waves. <!--SR:!2026-02-11,89,369!2026-01-31,79,369-->
  - wireless / historical motivation ::@:: Fixed-line infrastructure becomes prohibitively expensive in sparsely populated areas; wireless local loops provide a cost-effective alternative by eliminating the need for copper cabling from each home to the exchange. <!--SR:!2026-02-11,89,369!2026-02-16,93,369-->
  - wireless / Guglielmo Marconi ::@:: He achieved the first trans-Atlantic wireless telegraph, proving practical long-distance transmission; his work earned him the Nobel Prize and cemented the feasibility of wireless communication. <!--SR:!2026-02-06,85,369!2026-02-11,89,369-->
    - wireless / Guglielmo Marconi / Nikola Tesla ::@:: Nikola Tesla's early wireless experiments—oscillators, generators, filters, amplifiers—lay groundwork that later influenced long-distance telegraphy. <p> Thomas McCune's trans-Atlantic wireless telegraph project was built on many of Tesla's patents, sparking a protracted legal battle in which Tesla ultimately prevailed. <p> The episode illustrates how credit for foundational inventions can shift depending on legal outcomes and historical narrative. <!--SR:!2026-02-05,84,369!2026-02-11,89,369-->
    - wireless / Guglielmo Marconi / tests ::@:: McCune's team conducted trans-Atlantic wireless telegraph tests, using ships to explore how far radio waves could travel over the curved Earth where straight-line towers were ineffective. After initial failures, they discovered that certain frequencies were reflected by a layer of ionized plasma—the then unknown ionosphere—allowing signals to "bounce" across the Atlantic. This empirical finding foreshadowed modern satellite communications, which also rely on natural or artificial reflections to extend coverage beyond the horizon. <!--SR:!2026-02-11,89,369!2026-02-02,81,369-->
  - wireless / system ::@:: The system comprises three core components: transmitter, wireless channel, and receiver. <p> Engineers have design freedom for the transmitter and receiver (e.g., AM, FM modulation schemes), but not for the channel; it is dictated by physical propagation conditions. <!--SR:!2026-02-06,85,369!2026-02-05,84,369-->
    - wireless / system / channel ::@:: Different carrier frequencies (900 MHz vs. 28 GHz) exhibit distinct propagation physics, so each requires a tailored channel model. Because wireless channels vary widely, there is no universally optimal transmitter/receiver pair that works for every scenario. <p> This fact can be discouraging for novices (who must re-design for each new environment) but rewarding for experienced engineers who specialize in optimizing systems for specific channel conditions. <!--SR:!2026-02-17,94,369!2026-02-05,84,369-->
- data transmission
  - data transmission / analog
    - data transmission / analog / performance ::@:: Performance is measured by signal-to-noise ratio (SNR), comparing useful power to distortion/noise power. <!--SR:!2026-02-16,93,369!2026-02-06,85,369-->
  - data transmission / digital
    - data transmission / digital / performance ::@:: Two key performance metrics for digital links: bit error rate \(BER\), bitrate. <!--SR:!2026-02-10,88,369!2026-02-16,93,369-->
    - data transmission / digital / bit error rate \(BER\) ::@:: It is fraction of transmitted bits that are received incorrectly; a lower BER indicates higher reliability, with 0 being perfect and 0.5 representing maximum uncertainty. If BER is 1, flipping the bits will result in a BER of 0. <p> It reflects _reliability_ of data delivery. <!--SR:!2026-02-04,83,369!2026-02-02,81,369-->
    - data transmission / digital / bitrate ::@:: It is the number of correctly or incorrectly received bits per second, reflecting throughput or speed of data delivery. <!--SR:!2026-02-05,84,369!2026-02-03,82,369-->
    - data transmission / digital / "speed" ::@:: Does speed equals bandwidth? But speed cannot exceed the speed of light, right? <p> The truth is that both copper cables and optical fibers propagate signals at nearly the speed of light; the difference is negligible for everyday links. Propagation speed affects only _latency_ (the delay before the first bit arrives), not the maximum achievable bit-rate \(the "speed" we are talking about\). <!--SR:!2026-02-05,84,369!2026-02-04,83,369-->
    - data transmission / digital / tradeoffs ::@:: - __Bandwidth__: the width of spectrum a system occupies; licensed bandwidth directly correlates with cost because regulatory bodies assign radio frequencies on a paid basis. <br/> - __Power__: the transmit power is limited by regulations and also represents an economic resource (higher power requires more expensive hardware or higher operating costs). <p> Increasing bandwidth or power \(or both\) can increase bitrate or reliability \(or both\). <!--SR:!2026-02-16,93,369!2026-02-11,89,369-->

## week 2 lecture 2

- datetime: 2025-09-11T09:00:00+08:00/2025-09-11T10:20:00+08:00, PT1H20M
- topic: wireless; radio wave; carrier wave; additive white Gaussian noise; bit error rate; random variable; moment; normal distribution; independence; uncorrelatedness; multivariate normal distribution
- wireless
  - wireless / system
    - wireless / system / channel
  - wireless / channel ::@:: It is a physical medium that transmits signals between points; in wireless, it exhibits additional phenomena not present in wired links. <!--SR:!2026-02-15,92,369!2026-02-11,89,369-->
    - wireless / channel / general characteristics ::@:: Common impairments (present in both wired and wireless) include attenuation (loss of signal strength), thermal noise, filtering effects, intersymbol interference \(ISI\) that limit usable bandwidth. <!--SR:!2026-02-16,93,369!2026-02-17,94,369-->
    - wireless / channel / specific characteristics ::@:: Unique to wireless: _fading_—the received amplitude varies over time or with small spatial movements—and _time variation_—channel conditions can change over seconds or minutes. <p> These variations make reliable communication more challenging and motivate the need for adaptive modulation, coding, and diversity techniques. <!--SR:!2026-02-05,84,369!2026-02-17,94,369-->
- [radio wave](../../../../general/radio%20wave.md) ::@:: They are a type of electromagnetic radiation with the lowest frequencies and the longest wavelengths in the electromagnetic spectrum, typically with frequencies below 300 gigahertz \(GHz\) and wavelengths greater than 1 millimeter \(3⁄64 inch\), about the diameter of a grain of rice. <!--SR:!2026-02-11,89,369!2026-02-02,81,369-->
  - radio wave / frequency ::@:: They are a subset of the electromagnetic spectrum, spanning from kilohertz to gigahertz frequencies; they're defined by cycles per second (hertz). <p> The term _frequency_ is formally applied to periodic signals, but for practical purposes it extends to sinusoidal components of any signal. <!--SR:!2026-02-16,93,369!2026-02-11,89,369-->
  - radio wave / sharing ::@:: A single transmitter radiates over a range of frequencies; because radio waves propagate omnidirectionally, multiple users must share the spectrum carefully. <!--SR:!2026-02-17,94,369!2026-02-11,89,369-->
  - radio wave / regulation and licensing ::@:: Every country/region has an authority (e.g., Hong Kong's Communications Authority) that divides the entire spectrum into bands assigned to specific applications: AM/FM, TV, mobile, satellite, etc. <!--SR:!2026-02-08,86,369!2026-01-31,79,369-->
    - radio wave / regulation and licensing / mechanisms ::@:: Two main mechanisms allocate licensed spectrum: <p> - _Auctions_ – used when supply is scarce and demand high; operators bid for a lease typically lasting ~15 years. <br/> - _Assignments_ – direct allocation by application where demand is lower; involves lower fees and less competition. <!--SR:!2026-02-03,82,369!2026-02-11,89,369-->
    - radio wave / regulation and licensing / enforcement ::@:: Regulators also enforce compliance through spectrum monitoring and policing, detecting illegal transmitters (e.g., scammers using rogue base stations). <!--SR:!2026-02-14,91,369!2026-02-16,93,369-->
  - radio wave / ISM band ::@:: The International Mobile Satellite (ISM) band at 2.4 GHz and the 5 GHz band are designated for "instrumental, scientific and medical" use; devices operating here need no license. <p> Common consumer technologies—Wi-Fi, Bluetooth, wireless mice—operate in these bands, enabling low-cost, short-range communications. <p> Because unlicensed spectrum can be used by many users simultaneously, its chief concern is robustness to unpredictable interference rather than spectral efficiency. <!--SR:!2026-02-04,83,369!2026-02-11,89,369-->
    - radio wave / ISM band / Wi-Fi ::@:: Wi-Fi, operating in unlicensed ISM bands, prioritizes ease of deployment and cost over raw spectral efficiency; users accept lower throughput because they can freely set up networks without regulatory hurdles. <p> The "listen-before-talk" rule \(CSMA/CA\) in Wi-Fi forces devices to idle until the channel is clear, which yields high overhead and low spectral efficiency but guarantees coexistence with many other users. <!--SR:!2026-01-09,61,349!2026-02-16,93,369-->
  - radio wave / cellular bands ::@:: Cellular systems (4G/5G/6G) operate in licensed bands; their primary design objective is to maximize spectral efficiency—extracting the most bits per hertz while managing interference from a single authorized operator. <p> These differing priorities explain why cellular protocols emphasize advanced coding, scheduling, and interference management, whereas Wi-Fi focuses on simplicity and flexibility. <!--SR:!2026-02-06,85,369!2026-02-17,94,369-->
  - radio wave / propagation ::@:: For an isotropic radiator, power spreads uniformly over a spherical surface; received power equals transmit power times receiver aperture divided by $4\pi d^2$. <p> The geometry of the expanding sphere explains why received power falls off with the square of distance—no material loss (ohmic) is involved. <p> Even when beamforming concentrates energy in a narrow solid angle, the same geometric dilution applies; only the effective aperture changes. <!--SR:!2026-02-07,85,369!2026-02-17,94,369-->
    - radio wave / propagation / line-of-sight \(LOS\) ::@:: required for high-frequency signals (>10 GHz); signal travels straight, minimal reflection or diffraction. <!--SR:!2026-02-11,89,369!2026-02-16,93,369-->
    - radio wave / propagation / non-line-of-sight \(NLOS\) ::@:: lower-frequency signals can bend around obstacles via diffraction, reflection, scattering, enabling indoor coverage. <!--SR:!2026-02-02,81,369!2026-02-06,85,369-->
    - radio wave / propagation / multipath ::@:: Multipath propagation causes multiple delayed copies of the transmitted wave to arrive at the receiver, leading to constructive/destructive interference. <!--SR:!2026-02-13,90,369!2026-02-12,89,369-->
    - radio wave / propagation / path loss exponent ::@:: In indoor or urban environments, multipath causes the path loss to follow $L(d) \propto d^{-\alpha}$, where $\alpha$ (the path-loss exponent) can exceed 4 in dense settings. <p> Higher frequencies (e.g., mmWave at 28 GHz) have larger $\alpha$ and thus much smaller coverage radii than lower bands like 900 MHz. <p> Regulatory bodies rely on empirical field measurements to determine suitable frequency allocations that balance coverage, capacity, and interference constraints. <!--SR:!2026-02-17,94,369!2026-02-09,87,369-->
    - radio wave / propagation / path loss ::@:: Larger $\alpha$ shrinks cell radius, forcing operators to deploy more base stations and increasing capital expenditure. <p> However, by limiting signal reach, path loss reduces inter-cell interference, enabling dense spatial reuse and higher overall network capacity. Without any path loss (i.e., perfect propagation), a single transmitter could cover the entire globe, making the concept of cellular cells meaningless. <!--SR:!2026-01-11,47,349!2026-02-07,85,369-->
  - radio wave / regulation and licensing
    - radio wave / regulation and licensing / parameters ::@:: A spectrum license is defined by three key technical parameters: carrier frequency, allowable bandwidth, and power mask (maximum transmit power). <!--SR:!2026-02-04,83,369!2026-02-07,85,369-->
      - radio wave / regulation and licensing / parameters / carrier frequency ::@:: Center frequency of the frequency window of a band. It determines penetration, diffraction, and scattering characteristics; lower frequencies travel farther through walls and obstacles. <!--SR:!2026-02-17,94,369!2026-02-04,83,369-->
      - radio wave / regulation and licensing / parameters / bandwidth ::@:: Width of the frequency window of a band. <!--SR:!2026-02-16,93,369!2026-02-14,91,369-->
      - radio wave / regulation and licensing / parameters / transmit-power mask \(TPM\) ::@:: It sets a hard limit on transmit power and specifies required isolation from adjacent bands to avoid interference. It protects human receivers from excessive exposure and ensures adjacent-channel interference stays below acceptable thresholds. <!--SR:!2026-02-16,93,369!2026-02-01,80,369-->
- [carrier wave](../../../../general/carrier%20wave.md) ::@:: It is a periodic waveform (usually sinusoidal) that conveys information through a process called _modulation_. <!--SR:!2026-02-04,83,369!2026-02-17,94,369-->
  - carrier wave / carrier frequency ::@:: Low-frequency bands (e.g., ~2 GHz) have longer wavelengths (~15 cm), which are comparable to common obstacle sizes, enabling diffraction and robust non-line-of-sight \(NLOS\) reception. <p> High-frequency millimeter-wave bands (e.g., 28–30 GHz) have wavelengths in the millimeter range; obstacles much larger than this wavelength block signals, so line-of-sight \(LOS\) is almost mandatory. <!--SR:!2026-02-05,84,369!2025-12-20,41,329-->
    - carrier wave / carrier frequency / capacity ::@:: In a low-frequency band with limited spectral availability, allocating even 1 GHz of bandwidth can consume up to ~50% of the carrier's usable spectrum. <p> Higher frequency bands typically offer many gigahertz of contiguous spectrum, making large bandwidth allocations feasible and enabling very high data rates (e.g., 5G hotspots). <!--SR:!2026-02-12,89,369!2026-02-16,93,369-->
    - carrier wave / carrier frequency / exploit ::@:: In practice, operators therefore pair low-frequency "coverage" slices with high-frequency "capacity" slices to balance coverage breadth against peak throughput. <!--SR:!2026-02-17,94,369!2026-02-16,93,369-->
    - carrier wave / carrier frequency / cost ::@:: Scarce low-frequency bands are usually auctioned because demand far exceeds supply, driving up prices. <p> Abundant high-frequency bands are often assigned by regulators (or lightly auctioned) since the supply is ample and the propagation penalties reduce operator incentive to bid aggressively. <!--SR:!2026-02-09,87,369!2026-02-17,94,369-->
- radio wave
  - radio wave / regulation and licensing
    - radio wave / regulation and licensing / examples ::@:: 5G base stations operating around 5 GHz were installed close to an airport. The FAA argued that the out-of-band emissions could interfere with aircraft avionics at ~6 GHz, despite the transmitter's own TPM compliance. <p> This case underscores the need for cross-industry coordination when allocating spectrum near critical services. <!--SR:!2026-02-03,82,369!2026-02-03,82,369-->
- [transmitter](../../../../general/transmitter.md) ::@:: It is an electronic device which produces radio waves with an antenna with the purpose of signal transmission to a radio receiver. <!--SR:!2026-02-16,93,369!2026-02-17,94,369-->
  - transmitter / digital transmission ::@:: A digital transmitter takes a bitstream (e.g., 1&nbsp;000 bits) and converts it into an analog waveform that satisfies channel constraints. <p> The output must be band-limited to the licensed frequency range (band-pass signal). Modulation schemes (QAM, OFDM, etc.) map the digital data onto this analog carrier while maintaining spectral confinement. <!--SR:!2026-02-08,86,369!2026-02-06,85,369-->
- [radio receiver](../../../../general/radio%20receiver.md) ::@:: It is an electronic device that receives radio waves and converts the information carried by them to a usable form. It is used with an antenna. <!--SR:!2026-02-09,87,369!2026-02-16,93,369-->
  - radio receiver / digital transmission ::@:: The receiver observes a noisy version of the transmitted waveform and must recover the original bits. <p> The quality of recovery is measured by metrics such as bit error rate (BER) or frame error rate (FER). <!--SR:!2026-02-04,83,369!2026-02-13,90,369-->
- [frame](../../../../general/frame%20(networking).md) ::@:: It is a digital data transmission unit in computer networking and telecommunications. In packet switched systems, a frame is a simple container for a single network packet. In other telecommunications systems, a frame is a repeating structure supporting time-division multiplexing. <!--SR:!2026-02-16,93,369!2026-02-06,85,369-->
  - frame / typical structure ::@:: A typical frame starts with a preamble \(a known fixed sequence of bits\) used for synchronization and channel estimation, followed by a header that conveys modulation \(how to demodulate\), coding, and length information. <p> Finally, the payload carries user data; its integrity is ensured through error-correcting codes embedded in the header or as part of the payload itself. <!--SR:!2026-02-11,89,369!2026-02-05,84,369-->
  - frame / frame error rate \(FER\) ::@:: BER can theoretically be as high as 0.5 (worst case), while FER considers errors at the packet/frame level, which is more meaningful for practical protocols. <p> In the worst case BER can be 0.5, whereas FER can reach 1 because an entire corrupted frame cannot simply be flipped back to its original contents. <!--SR:!2026-02-16,93,369!2026-02-05,84,369-->
- [additive white Gaussian noise](../../../../general/additive%20white%20Gaussian%20noise.md) \(AWGN\) ::@:: It is a basic noise model used in information theory to mimic the effect of many random processes that occur in nature. <!--SR:!2026-02-01,80,369!2026-02-09,87,369-->
- [bit error rate](../../../../general/bit%20error%20rate.md) \(BER\) ::@:: The __bit error rate__ \(__BER__\) is the number of bit errors per unit time. The __bit error ratio__ \(also __BER__\) is the number of bit errors divided by the total number of transferred bits during a studied time interval. Bit error ratio is a unitless performance measure, often expressed as a percentage. <p> \(__this course__: __Important__. We use the _bit error ratio_, but we call it _bit error rate_. Funny, isn't it?\) <!--SR:!2026-02-11,89,369!2026-02-01,80,369-->
- ELEC 4110
  - ELEC 4110 / [binary modulation](binary%20modulation.md)
    - [§ binary modulation](binary%20modulation.md#binary%20modulation)
    - [§ binary channel](binary%20modulation.md#binary%20channel)
    - [§ receiver](binary%20modulation.md#receiver)
    - [§ bit error rate](binary%20modulation.md#bit%20error%20rate)
    - [§ bit error rate with zero threshold](binary%20modulation.md#bit%20error%20rate%20with%20zero%20threshold)
    - [§ bit error rate with arbitrary threshold](binary%20modulation.md#bit%20error%20rate%20with%20arbitrary%20threshold)
    - [§ signal energy](binary%20modulation.md#signal%20energy)
    - [§ signal-to-noise ratio](binary%20modulation.md#signal-to-noise%20ratio)
    - [§ using error function](binary%20mo2dulation.md#using%20error%20function)
- [random variable](../../../../general/random%20variable.md) (r.v.) ::@:: A __random variable__ (__r.v.__) is a mathematical function. Its _domain_ is the sample space. Its _range_ is a measurable space, usually a finite set of integers or the real numbers. The function need not be _injective_ (different samples need not map to different values). It is commonly denoted by capital letters, with its possible numerical values (also called __realizations__) by the same but lowercase letters. <p> A way to think about random variable is that it maps each outcome to a real number. <!--SR:!2026-02-15,92,369!2026-02-05,84,369-->
- [probability density function](../../../../general/probability%20density%20function.md) \(PDF, pdf\) ::@:: It of an _absolutely continuous_ random variable is a function whose value at any given sample \(or point\) in the sample space \(the set of possible values taken by the random variable\) can be interpreted as providing a _relative likelihood_ that the value of the random variable would be equal to that sample. <p> Probability density is the probability per unit length, in other words, the _absolute likelihood_ for a continuous random variable to take on any particular value is 0 since there is an infinite set of possible values to begin with. <p> It is commonly denoted $f_X(x)$ for an absolutely continuous random variable _X_. <!--SR:!2026-02-06,85,369!2026-02-17,94,369-->
- [cumulative distribution function](../../../../general/cumulative%20distribution%20function.md) (CDF, cdf) ::@:: A __cumulative distribution function__ (__CDF__, __cdf__) of a real-valued random variable _X_ is the probability that _X_ will take a value less than or equal to _x_. It is given by: $$F_X(x) = P(X \le x) \,.$$ The probability that _X_ will take a value in between \(_a_, _b_\], where _a_ < _b_, is $$P(a < X \le b) = F_X(b) - F_X(a) \,.$$ <!--SR:!2026-02-01,80,369!2026-01-09,61,349-->
- [moment](../../../../general/moment%20(mathematics).md) ::@:: The ___k_-th (population) moment__ (also called __raw moment__), which is about _the origin_ (not about _the mean_), of a random variable _X_ is defined by $$\operatorname E\left[X^k \right] \qquad k \in \mathbb N_{\ge 1} \,,$$ if _it exists_. (When _k_ = 0 (the "zeroth" moment), this always equal to 1, so we ignore it here.) <p> A _k_-th moment exists if $\operatorname E\left[\left\lvert X^k \right\rvert\right] < \infty$ (Lebesgue integrable). If the _n_-th moment exists _about any point_, so does the $(n - 1)$-th moment (and thus, all lower-order moments) _about every point_. <!--SR:!2026-02-17,94,369!2026-02-09,87,369-->
  - moment / population mean ::@:: The population mean is the 1st _raw_ moment. <!--SR:!2026-02-06,85,369!2026-02-06,85,369-->
- [central moment](../../../../general/central%20moment.md) ::@:: The ___k_-th (population) central moment__, which is about _the mean_ (not about _the origin_), of a random variable _X_ is defined by $$\operatorname E\left[(X - \operatorname E[X])^k\right] \qquad k \in \mathbb N_{\ge 1} \,,$$ if _it exists_. (When _k_ = 0 (the "zeroth" moment), this always equal to 1, so we ignore it here.) <p> A _k_-th central moment exists if $\operatorname E[\lvert X \rvert] < \infty$ and $\operatorname E\left[\left\lvert (X - \operatorname E[X])^k \right\rvert \right] < \infty$ (both Lebesgue integrable). If the _n_-th moment exists _about any point_ (including the value $\operatorname E[X]$), so does the $(n - 1)$-moment (and thus, all lower-order moments) _about every point_. <!--SR:!2026-01-09,57,329!2026-02-09,87,369-->
  - central moment / population variance ::@:: The population variance is the 2nd _central_ moment. <!--SR:!2026-02-08,86,369!2026-02-06,85,369-->
- [normal distribution](../../../../general/normal%20distribution.md) ::@:: The __normal distribution__ or __Gaussian distribution__ is important in statistics and is often used in the natural and social sciences to represent real-valued random variables whose distributions are not known. Their importance is partly due to the central limit theorem. It is denoted $\mathcal N(\mu, \sigma^2)$, where $\mu \in \mathbb R$ is the mean and $\sigma^2 \in \mathbb R_{> 0}$ is the variance. <p> \(When you see $\mathcal N(0, 100)$, do not mistake the 100 as the standard deviation! It is the variance.\) <!--SR:!2026-02-16,93,369!2026-02-11,89,369-->
  - normal distribution / probability _density_ function ::@:: For $X \sim \mathcal N(\mu, \sigma^2) \,,$ $$f(x) = \frac 1 {\sqrt{2\pi \sigma^2} } \exp\left(-\frac {(x - \mu)^2} {2 \sigma^2} \right) \,.$$ <!--SR:!2026-02-01,80,369!2026-01-31,79,369-->
  - normal distribution / mean ::@:: For $X \sim \mathcal N\left(\mu, \sigma^2 \right) \,,$ $$\operatorname E[X] = \mu \,.$$ To prove this, turn the additional $x$ in the integrand into $(x - \mu + \mu)$, apply linearity of integration (split into $(x - \mu)$ and $\mu$), and then substitute $t = \frac {x - \mu} {\sqrt {2 \sigma^2} }$. Then the expression should contain a Gaussian integral and an integral that has an odd function as the integrand. The former integral is $\sqrt \pi$ and the latter integral is 0 by symmetry. <!--SR:!2026-01-31,79,369!2026-02-06,85,369-->
  - normal distribution / variance ::@:: For $X \sim \mathcal N\left(\mu, \sigma^2\right) \,,$ $$\operatorname{Var}(X) = \sigma^2 \,.$$ To prove this, substitute $t = \frac {x - \mu} {\sqrt {2 \sigma^2} }$, then substitute $e^{-t^2}$, and finally apply integration by part. The resulting expression should contain an expression that is 0 and a Gaussian integral, which evaluates to $\sqrt \pi$. <!--SR:!2026-02-02,81,369!2026-02-07,85,369-->
  - normal distribution / shape ::@:: All normal distribution have the bell-shaped regardless of its parameters. Changing the mean simply translates the shape, while increasing the variance fattens (becomes wider) and flattens (the maximum value becomes lower) the shape. <!--SR:!2026-02-16,93,369!2026-02-05,84,369-->
  - normal distribution / standardization ::@:: Any normal distribution can be __standardized__ by defining the random variable $$Z = \frac {X - \mu} {\sigma} \qquad X = \sigma Z + \mu \,.$$ Further, $$z = \frac {x - \mu} \sigma$$ is also known as the __standard score__ of the data _x_. <p> After standardization, a standard normal table that provides $\Phi(z)$ for different values of _z_ may be used to evaluate the CDF of any normal distribution. (The table may not show negative values of _z_. In that case, you need to use the property of its CDF above.) <!--SR:!2026-02-03,82,369!2026-02-10,88,369-->
- [joint probability distribution](../../../../general/joint%20probability%20distribution.md) ::@:: Given [random variables](../../../../general/random%20variable.md) $X,Y,\ldots$, that are defined on the same [probability space](../../../../general/probability%20space.md), the __multivariate__ or __joint probability distribution__ for $X,Y,\ldots$ is a [probability distribution](../../../../general/probability%20distribution.md) that gives the probability that each of $X,Y,\ldots$ falls in any particular range or discrete set of values specified for that variable. <!--SR:!2026-02-14,91,369!2026-02-15,92,369-->
  - joint probability distribution / expressions ::@:: The joint probability distribution can be expressed in terms of a joint cumulative distribution function and either in terms of a joint probability density function (in the case of continuous variables) or joint probability mass function (in the case of discrete variables). <!--SR:!2026-02-13,90,369!2026-02-01,80,369-->
  - joint probability distribution / cumulative distribution function \(CDF\) ::@:: It gives the probability that both variables lie within specified ranges; it is analogous to the CDF for one variable but now two-dimensional. <p> If this joint CDF is smooth, its derivative with respect to both variables yields the _joint PDF_, which can be visualized as a surface or contour plot. A two-dimensional histogram approximates the joint PDF by counting samples in each bin; refining the bins (more data) leads closer to the true continuous density. <!--SR:!2026-02-11,89,369!2026-02-06,85,369-->
  - joint probability distribution / marginal distribution ::@:: It gives the probabilities for any one of the variables with no reference to any specific ranges of values for the other variables. <!--SR:!2026-02-06,85,369!2026-02-04,83,369-->
- [multivariate normal distribution](../../../../general/multivariate%20normal%20distribution.md) ::@:: It is a generalization of the one-dimensional (univariate) normal distribution to higher dimensions. One definition is that a random vector is said to be k-variate normally distributed if every linear combination of its k components has a univariate normal distribution. <!--SR:!2026-02-13,90,369!2026-02-09,87,369-->
  - multivariate normal distribution / names ::@:: multivariate normal distribution, multivariate Gaussian distribution, joint normal distribution <!--SR:!2026-02-17,94,369!2026-02-08,86,369-->
  - multivariate normal distribution / notation and parameters ::@:: $${\mathcal {N} }({\boldsymbol {\mu } },\,{\boldsymbol {\Sigma } })$$ where <p> ___μ___ ∈ __R__<sup>_k_</sup> — [location](../../../../general/location%20parameter.md) <br/> __Σ__ ∈ __R__<sup>_k_ × _k_</sup> — [covariance](../../../../general/covariance%20matrix.md) \([positive semi-definite matrix](../../../../general/positive%20semi-definite%20matrix.md)\) <!--SR:!2026-02-15,92,369!2026-02-12,89,369-->
  - multivariate normal distribution / probability distribution function \(PDF\) ::@:: $$(2\pi )^{-k/2}\det({\boldsymbol {\Sigma } })^{-1/2}\,\exp \left(-{\frac {1}{2} }(\mathbf {x} -{\boldsymbol {\mu } })^{\mathrm {T} }{\boldsymbol {\Sigma } }^{-1}(\mathbf {x} -{\boldsymbol {\mu } })\right) \,,$$ <br/> exists only when __Σ__ is [positive-definite](../../../../general/positive-definite%20matrix.md) <!--SR:!2026-02-06,85,369!2025-12-20,41,329-->
    - multivariate normal distribution / probability distribution function \(PDF\) / bivariate ::@:: Start with a random vector $X=[x_{1},x_{2}]^{\top}$ with mean $\mu=[\mu _{1},\mu _{2}]^{\top}$ and covariance matrix $$\Sigma=\begin{bmatrix} \sigma _{1}^{2} & \sigma _{12}\\[4pt] \sigma _{12} & \sigma _{2}^{2} \end{bmatrix} \,.$$ The determinant is $|\Sigma|=\sigma_{1}^{2}\sigma_{2}^{2}-\sigma_{12}^{2}$, and the inverse is $$\Sigma^{-1}= \frac{1}{|\Sigma|} \begin{bmatrix} \sigma _{2}^{2} & -\,\sigma _{12}\\[4pt] -\sigma _{12} & \sigma _{1}^{2} \end{bmatrix} \,.$$ Substituting these into the general formula gives the joint Gaussian PDF: $$f_{X}(x_{1},x_{2})=\frac{1}{2\pi\,\sqrt{\sigma_{1}^{2}\sigma_{2}^{2}-\sigma_{12}^{2} } }\exp\!\Bigl(-\frac{\sigma _{2}^{2}(x_{1}-\mu _{1})^{2}-2\sigma _{12}(x_{1}-\mu _{1})(x_{2}-\mu _{2})+\sigma _{1}^{2}(x_{2}-\mu _{2})^{2} }{2(\sigma_{1}^{2}\sigma_{2}^{2}-\sigma_{12}^{2})}\Bigr).$$ <p> It may also be written, using correlation coefficient $\rho = \frac {\sigma_{12} } {\sigma_1 \sigma_2}$, as $$f_X(x_1, x_2) = \frac {1} {2 \pi \sigma_1 \sigma_2 \sqrt{1 - \rho^2} } \exp\left(- \frac 1 {2(1 - \rho^2)} \left(\left(\frac {x_1 - \mu_1} {\sigma_1} \right)^2 + \left(\frac {x_2 - \mu_2} {\sigma_2} \right)^2 - \frac {2 \rho (x_1 - \mu_1) (x_2 - \mu_2)} {\sigma_1 \sigma_2} \right)\right) \,.$$ <!--SR:!2025-12-20,41,329!2025-12-20,41,329-->
- [independence](../../../../general/independence%20(probability%20theory).md) ::@:: Two events _A_ and _B_ are __independent__ iff $$P(A \cap B) = P(A) P(B) \,.$$ otherwise they are __dependent__. <p> Informally speaking, knowing either of the event has happened does not affect the probability of the other. <!--SR:!2026-02-10,88,369!2026-02-11,89,369-->
  - independence / equivalence ::@:: The following statements are equivalent: <ul> <li>_A_ and _B_ are independent.</li> <li>_A_ and _B_<sup>c</sup> are independent.</li> <li>_A_<sup>c</sup> and _B_ are independent.</li> <li>_A_<sup>c</sup> and _B_<sup>c</sup> are independent.</li> </ul> The above can be seen by seeing that the complement of an event is uniquely defined by the event. There is a one-to-one correspondence between a set and its complement (unless the sample space is the empty set, which is impossible for probability). <!--SR:!2026-02-10,88,369!2026-02-02,81,369-->
  - independence / vs. disjoint ::@:: Independent is not disjoint. End of story. <!--SR:!2026-02-11,89,369!2026-02-05,84,369-->
  - independence / pairwise independence ::@:: A finite set of events is __pairwise independent__ iff any two events from the set is _independent_. <p> Pairwise independence does NOT automatically imply _mutual independence_. <!--SR:!2026-02-17,94,369!2026-02-06,85,369-->
  - independence / mutual independence ::@:: A finite set of _n_ events is __mutually independent__ iff any 2 ≤ _k_ ≤ _n_ events from the set is _independent_. For the _independence_ of 2 ≤ _k_ events, this is simply: $$P\left(\bigcap_{i = 1}^k A_k \right) = \prod_{i = 1}^k A_k \,.$$ <p> Mutual independence automatically implies _pairwise independence_. However, note that the above statement must hold for all 2 ≤ _k_ ≤ _n_, not just _k_ = _n_. It is possible to create a sample space such that the set of three events _A_, _B_, and _C_ is independent but no pairs from the three events are _pairwise independent_. <!--SR:!2026-02-01,80,369!2026-02-06,85,369-->
- [uncorrelatedness](../../../../general/uncorrelatedness%20(probability%20theory).md) ::@:: In [probability theory](../../../../general/probability%20theory.md) and [statistics](../../../../general/statistics.md), two real-valued [random variables](../../../../general/random%20variable.md), $X$, $Y$, are said to be __uncorrelated__ if their [covariance](../../../../general/covariance.md), $\operatorname {cov} [X,Y]=\operatorname {E} [XY]-\operatorname {E} [X]\operatorname {E} [Y]$, is zero. If two variables are uncorrelated, there is no linear relationship between them. <!--SR:!2026-02-03,82,369!2026-02-05,84,369-->
  - uncorrelatedness / independence ::@:: If $X$ and $Y$ are independent, with finite second moments, then they are uncorrelated. However, not all uncorrelated variables are independent. <p> In particular, joint Gaussianity guarantees that zero covariance actually implies independence, bridging the two separability notions. <!--SR:!2026-02-11,89,369!2026-02-11,89,369-->
- [Markov's inequality](../../../../general/Markov's%20inequality.md) ::@:: In probability theory, it gives an upper bound on the probability that a non-negative random variable is greater than or equal to some positive constant. <p> It is tight in the sense that for each chosen positive constant, there exists a random variable such that the inequality is in fact an equality. <!--SR:!2026-02-06,85,369!2026-02-11,89,369-->
  - Markov's inequality / statement ::@:: If _X_ is a nonnegative random variable and _a_ \> 0, then the probability that _X_ is at least _a_ is at most the expectation of _X_ divided by _a_: $$\operatorname {P} (X\geq a)\leq {\frac {\operatorname {E} (X)}{a} }.$$ <!--SR:!2026-02-04,83,369!2026-02-17,94,369-->
- [Chebyshev's inequality](../../../../general/Chebyshev's%20inequality.md) ::@:: The probability that a random variable deviates from its mean by at least $k\sigma$ is at most $1/k^{2}$, where $k$ is any positive constant and $\sigma$, required to be finite non-zero (also implies finite expected value $\mu$), is the standard deviation (the square root of the variance): $$P(\lvert X - \mu \rvert \ge k \sigma) \le \frac 1 {k^2} \,.$$ <!--SR:!2026-02-11,89,369!2026-02-06,85,369-->
  - Chebyshev's inequality / proof for continuous random variable ::@:: This a proof for continuous random variable, but a similar one applies for discrete random variable: $$\begin{aligned} P(\lvert X - \mu \rvert \ge k \sigma) & = \int_{\lvert x - \mu \rvert \ge k \sigma} \! f(x) \,\mathrm{d}x \\ & \le \int_{\lvert x - \mu \rvert \ge k \sigma} \! \frac {(x - \mu)^2} {k^2 \sigma^2} f(x) \,\mathrm{d}x \\ & = \frac 1 {k^2 \sigma^2} \operatorname{Var}(X) \\ & = \frac 1 {k^2} \,. \end{aligned}$$ <!--SR:!2026-02-07,85,369!2026-02-02,81,369-->

## week 2 tutorial

- datetime: 2025-09-12T15:30:00+08:00/2025-09-12T16:20:00+08:00, PT50M
- topic: probability theory
- random variable
  - random variable / description ::@:: A real-valued random variable $X$ is described by its cumulative distribution function (CDF) $F_X(x)=P(X \le x)$ and, if it possesses a density, by the probability density function (PDF) $f_X(x)=dF_X(x)/dx$. <!--SR:!2026-02-01,75,381!2026-04-04,127,401-->
- joint probability distribution
  - joint probability distribution / independence ::@:: For two variables $X,Y$, the joint CDF $F_{XY}(x,y)=P(X \le x,\;Y \le y)$ factorizes into the product of marginals iff $X$ and $Y$ are independent. For multiple variables, they must be _mutually_ independent, and vice versa. <p> Independence can also be checked via the joint PDF: $f_{XY}(x,y)=f_X(x)f_Y(y)$. <!--SR:!2026-04-16,138,401!2026-04-05,128,401-->
- random variable
  - random variable / expectation ::@:: The expectation of a single variable follow from its PDF: $$\mathbb{E}\{X\}=\int x\,f_X(x)\,dx \,.$$ <!--SR:!2026-04-04,127,401!2026-04-11,133,401-->
  - random variable / variance ::@:: The variance of a single variable follow from its PDF: $$\operatorname{Var}\{X\}=\int (x-\mu)^2 f_X(x)\,dx \,.$$ <!--SR:!2026-04-04,127,401!2026-03-30,123,401-->
  - random variables / families ::@:: Each family is characterized by a small set of parameters (e.g., mean and variance for Gaussian). <!--SR:!2026-03-30,123,401!2026-04-13,135,401-->
    - random variables / families / discrete ::@:: Bernoulli, binomial, uniform (discrete), etc. <!--SR:!2026-01-31,74,381!2026-01-25,69,381-->
    - random variables / families / continuous ::@:: uniform, exponential, Gaussian (normal), chi-square, Rayleigh/Ricean, gamma, Nakagami, lognormal, etc. <!--SR:!2026-03-30,123,401!2026-04-04,127,401-->
- [central limit theorem](../../../../general/central%20limit%20theorem.md) (CLT) ::@:: It states that, under _appropriate conditions_, the distribution of a _normalized version of the sample mean_ converges to a _standard normal distribution_. This holds even if the original variables themselves are _not_ normally distributed. <!--SR:!2026-04-11,133,401!2026-04-09,132,401-->
  - central limit theorem / communication theory ::@:: In communication theory the Gaussian model dominates because of its role in modelling thermal noise and fading channels. Many non-Gaussian distributions can be approximated as Gaussian via the Central Limit Theorem. <!--SR:!2026-03-29,122,401!2026-03-29,122,401-->
- normal distribution
  - normal distribution / standardization
- [Q-function](../../../../general/Q-function.md) ::@:: It is the tail distribution function of the standard normal distribution. In other words, $Q(x)$ is the probability that a normal \(Gaussian\) random variable will obtain a value larger than $x$ standard deviations. Equivalently, $Q(x)$ is the probability that a standard normal random variable takes a value larger than $x$. <!--SR:!2026-03-30,123,401!2026-04-05,128,401-->
  - Q-function / probability ::@:: $$Q(x) := P[X > x] \implies P[X \le x] = 1 - Q(x) \,,$$ where $X$ follows a standard normal distribution, i.e. with mean 0 and standard deviation 1. <p> For a normal distribution $Y$ with mean $\mu_Y$ and standard deviation $\sigma_Y$ \(variance $\sigma_Y^2$\), we compute $$P[Y > y] = Q\left(\frac {y - \mu_Y} {\sigma_Y} \right) \implies P[Y \le y] = 1 - Q\left(\frac {y - \mu_Y} {\sigma_Y} \right) \,.$$ <!--SR:!2026-04-13,135,401!2026-04-10,133,401-->
  - Q-function / computation ::@:: There is no closed-form expression for it. A table of values or computers must be used. <p> In MATLAB, use the `qfunc(x)` function or `1 - normcdf(x)`. <!--SR:!2026-04-13,135,401!2026-04-08,131,401-->
- multivariate normal distribution
  - multivariate normal distribution / standard random vector ::@:: A __standard Gaussian random vector__ $\mathbf{w}\in\mathbb{R}^{n}$ is an $n$-dimensional random variable whose components are independent, zero-mean, unit-variance normal variables. Its probability density function is $$f_{\mathbf{w} }(\mathbf{w})=\frac{1}{(2\pi)^{\,n/2} }\exp\!\Bigl(-\tfrac12 \,\mathbf{w}^{T}\mathbf{w}\Bigr),$$ which shows that the joint distribution factorises into the product of \(n\) one-dimensional standard normal PDFs and that its covariance matrix equals the identity matrix. <!--SR:!2026-01-23,64,361!2026-01-08,52,361-->
  - multivariate normal distribution / random vector ::@:: A vector $\mathbf{x}\in\mathbb{R}^n$ is Gaussian if it equals a linear transformation of a standard normal vector $\mathbf w$ plus a shift $\mathbf b$: $$\mathbf{x}=A\mathbf{w}+b \,.$$ <p> Its _mean_ vector is $\mathbf b$. Its _covariance_ matrix is $$K=\operatorname{Cov}\{\mathbf{x}\}=AA^{T} \,.$$ <!--SR:!2026-03-30,123,401!2026-01-30,73,381-->
  - multivariate normal distribution / communications theory ::@:: These properties make Gaussian vectors convenient for modelling multiple-antenna channels. <!--SR:!2026-04-12,134,401!2026-04-05,128,401-->
- [sample mean](../../../../general/sample%20mean%20and%20covariance.md)
  - sample mean / equation ::@:: Given _N_ samples of a random variable _X_, its _sample mean_ is: $$\overline X = \frac 1 N \sum_{k = 1}^N X_k \,.$$ <!--SR:!2026-03-29,122,401!2026-04-05,128,401-->
  - sample mean / properties ::@:: It is _unbiased_: $\operatorname E[\overline X] = \mu_X$. It has a variance that is inversely proportional to the number of samples: $\operatorname{Var}(\overline X) = \frac {\sigma_X^2} N$. <!--SR:!2026-03-29,122,401!2026-04-07,130,401-->
- central limit theorem
  - central limit theorem / classical CLT ::@:: If $\overline {X_n}$ is the _sample mean_ of a random sample (sequence of _i.i.d._ random variables) of size $n$ taken from _any_ population with population mean $\mu_X$ and _finite_ variance $\sigma_X^2 < \infty$, then as $n \to \infty$, the random variable $\overline {X_n}$ _converges in distribution_ to $\mathcal N\left(\mu_X, \sigma_X^2 / n\right)$. The latter can be rewritten as $\overline {Z_n} = (\overline {X_n} - \mu_X) \sqrt{n / \sigma_X^2}$ _converges in distribution_ to $\mathcal N(0, 1)$. <!--SR:!2026-04-16,138,401!2026-04-15,137,401-->
- [law of large numbers](../../../../general/law%20of%20large%20numbers.md) ::@:: It is a mathematical law that states that the average of the results obtained from a large number of independent random samples converges to the true value, if it exists. More formally, the law of large numbers states that given a sample of independent and identically distributed values, the sample mean converges to the true mean. <!--SR:!2026-04-17,139,401!2026-04-12,134,401-->
  - law of large numbers / weak law ::@:: The __weak law of large numbers__ \(also called [Khinchin](../../../../general/Aleksandr%20Khinchin.md)'s law\) states that given a collection of [independent and identically distributed](../../../../general/independent%20and%20identically%20distributed%20random%20variables.md) \(iid\) samples from a random variable with finite mean, the sample mean [converges in probability](../../../../general/convergence%20in%20probability.md) to the expected value $${\overline {X} }_{n}\ {\overset {P}{\rightarrow } }\ \mu \qquad {\textrm {when} }\ n\to \infty .$$ That is, for any positive number _ε_, $$\lim _{n\to \infty }\Pr \!\left(\,|{\overline {X} }_{n}-\mu |<\varepsilon \,\right)=1.$$ <!--SR:!2026-01-08,52,361!2026-03-05,96,381-->
    - law of large numbers / weak law / interpretation ::@:: Interpreting this result, the weak law states that for any nonzero margin specified \(_ε_\), no matter how small, with a sufficiently large sample there will be a very high probability that the average of the observations will be close to the expected value; that is, within the margin. <!--SR:!2026-04-05,128,401!2026-03-29,122,401-->
  - law of large numbers / strong law ::@:: The __strong law of large numbers__ \(also called [Kolmogorov](../../../../general/Andrey%20Kolmogorov.md)'s law\) states that the sample average [converges almost surely](../../../../general/almost%20sure%20convergence.md#almost%20sure%20convergence) to the expected value $${\overline {X} }_{n}\ {\overset {\text{a.s.} }{\longrightarrow } }\ \mu \qquad {\textrm {when} }\ n\to \infty .$$ That is, $$\Pr \!\left(\lim _{n\to \infty }{\overline {X} }_{n}=\mu \right)=1.$$ <!--SR:!2026-04-17,139,401!2026-01-10,53,361-->
    - law of large numbers / strong law / interpretation ::@:: What this means is that, as the number of trials _n_ goes to infinity, the probability that the average of the observations converges to the expected value, is equal to one. The modern proof of the strong law is more complex than that of the weak law, and relies on passing to an appropriate sub-sequence. <!--SR:!2026-03-02,94,381!2026-01-28,72,381-->
  - law of large numbers / weak law
    - law of large numbers / weak law / proof using Chebyshev's inequality assuming finite variance ::@:: This proof uses the assumption of finite [variance](../../../../general/variance.md) $\operatorname {Var} (X_{i})=\sigma ^{2}$ \(for all $i$\). The independence of the random variables implies no correlation between them, and we have that $$\operatorname {Var} ({\overline {X} }_{n})=\operatorname {Var} ({\tfrac {1}{n} }(X_{1}+\cdots +X_{n}))={\frac {1}{n^{2} } }\operatorname {Var} (X_{1}+\cdots +X_{n})={\frac {n\sigma ^{2} }{n^{2} } }={\frac {\sigma ^{2} }{n} }.$$ The common mean μ of the sequence is the mean of the sample average: $$E({\overline {X} }_{n})=\mu .$$ Using [Chebyshev's inequality](../../../../general/Chebyshev's%20inequality.md) on ${\overline {X} }_{n}$ results in $$\operatorname {P} (\left|{\overline {X} }_{n}-\mu \right|\geq \varepsilon )\leq {\frac {\sigma ^{2} }{n\varepsilon ^{2} } }.$$ This may be used to obtain the following: $$\operatorname {P} (\left|{\overline {X} }_{n}-\mu \right|<\varepsilon )=1-\operatorname {P} (\left|{\overline {X} }_{n}-\mu \right|\geq \varepsilon )\geq 1-{\frac {\sigma ^{2} }{n\varepsilon ^{2} } }.$$ As _n_ approaches infinity, the expression approaches 1. And by definition of [convergence in probability](../../../../general/convergence%20in%20probability.md#convergence%20in%20probability), we have obtained $${\overline {X} }_{n}\ {\overset {P}{\rightarrow } }\ \mu \qquad {\textrm {when} }\ n\to \infty .$$ <!--SR:!2026-01-11,54,361!2026-03-08,99,381-->
- stochastic process
  - stochastic process / mean ::@:: Its mean function is $$\mu_X(t)=\mathbb{E}\{X(t)\} \,.$$ <!--SR:!2026-03-30,123,401!2026-04-14,136,401-->
  - stochastic process / autocorrelation ::@:: Its autocorrelation is $$R_X(t_1,t_2)=\mathbb{E}\{X(t_1)X^*(t_2)\} \,.$$ <!--SR:!2026-03-29,122,401!2026-03-30,123,401-->
  - stochastic process / cross-correlation ::@:: The cross-correlation of two processes $X,Y$ is $$R_{XY}(t_1,t_2)=\mathbb{E}\{X(t_1)Y^*(t_2)\} \,.$$ <!--SR:!2026-04-06,129,401!2026-03-29,122,401-->
- stationary process
  - stationary process / strict-sense stationary
    - stationary process / strict-sense stationary / implications ::@:: For a \(strictly\) stationary process its statistical properties \(e.g. moments\) are time-invariant. <!--SR:!2026-04-14,136,401!2026-04-15,137,401-->
  - stationary process / weak-sense stationary

## week 3 lecture

- datetime: 2025-09-16T09:00:00+08:00/2025-09-16T10:20:00+08:00, PT1H20M
- topic: random variable; stochastic process; white noise; additive white Gaussian noise; bit error rate; Q-function
- random variable
- [stochastic process](../../../../general/stochastic%20process.md) ::@:: It is a mathematical object usually defined as a family of random variables in a probability space, where the index of the family often has the interpretation of time. <!--SR:!2026-02-11,89,369!2026-02-05,84,369-->
- joint probability distribution
- moment
  - moment / description ::@:: A full joint distribution can yield all moments; the reverse is not true for general processes. <p> For Gaussian processes, first-order and second-order moments uniquely determine the entire process. <!--SR:!2026-01-31,79,369!2026-02-22,98,385-->
- [stationary process](../../../../general/stationary%20process.md) ::@:: It is a stochastic process whose statistical properties, such as mean and variance, do not change over time. More formally, the joint probability distribution of the process remains the same when shifted in time. This implies that the process is statistically consistent across different time periods. <!--SR:!2026-02-06,85,369!2026-02-16,93,369-->
  - stationary process / strict-sense stationary ::@:: Formally, let $\left\{X_{t}\right\}$ be a [stochastic process](../../../../general/stochastic%20process.md) and let $F_{X}(x_{t_{1}+\tau },\ldots ,x_{t_{n}+\tau })$ represent the [cumulative distribution function](../../../../general/cumulative%20distribution%20function.md) of the [unconditional](../../../../general/marginal%20distribution.md) \(i.e., with no reference to any particular starting value\) [joint distribution](../../../../general/joint%20distribution.md) of $\left\{X_{t}\right\}$ at times $t_{1}+\tau ,\ldots ,t_{n}+\tau$. Then, $\left\{X_{t}\right\}$ is said to be __strictly stationary__, __strongly stationary__ or __strict-sense stationary__ if $$F_{X}(x_{t_{1}+\tau },\ldots ,x_{t_{n}+\tau })=F_{X}(x_{t_{1} },\ldots ,x_{t_{n} })\quad {\text{for all } }\tau ,t_{1},\ldots ,t_{n}\in \mathbb {R} {\text{ and for all } }n\in \mathbb {N} _{>0}$$ Since $\tau$ does not affect $F_{X}(\cdot )$, $F_{X}$ is independent of time. <!--SR:!2026-02-16,93,369!2026-01-19,66,349-->
  - stationary process / weak-sense stationary ::@:: So, a [continuous time](../../../../general/continuous%20time.md#continuous%20time) [random process](../../../../general/random%20process.md) $\left\{X_{t}\right\}$ which is WSS has the following restrictions on its mean function $m_{X}(t)\triangleq \operatorname {E} [X_{t}]$ and [autocovariance](../../../../general/autocovariance.md) function $K_{XX}(t_{1},t_{2})\triangleq \operatorname {E} [(X_{t_{1} }-m_{X}(t_{1}))(X_{t_{2} }-m_{X}(t_{2}))]$: $${\begin{aligned}&m_{X}(t)=m_{X}(t+\tau )&&{\text{for all } }\tau ,t\in \mathbb {R} \\&K_{XX}(t_{1},t_{2})=K_{XX}(t_{1}-t_{2},0)&&{\text{for all } }t_{1},t_{2}\in \mathbb {R} \\&\operatorname {E} \left[{\lvert X_{t} \rvert}^{2}\right]<\infty &&{\text{for all } }t\in \mathbb {R} \end{aligned} }$$ <p> For Gaussian processes, strict-sense stationary and weak-sense stationary are equivalent. <p> \(__this course__: The instructor did not mention the last condition. Maybe omit it...?\) <!--SR:!2026-02-13,90,369!2025-12-17,41,329-->
- additive white Gaussian noise
  - additive white Gaussian noise / moments ::@:: - 1st moment: mean is usually zero → first-order moment trivial. <br/> - 2nd moment: autocovariance is $R_X(\tau)=\sigma^2\delta(\tau) = (N_0 / 2) \delta(\tau)$, where $\tau = t_2 - t_1$ is the time difference; power spectral density \(_Fourier transform_ of autocovariance\) $S_X(f) = \sigma^2 = N_0 / 2$ is flat (white). Knowing $\sigma^2 = N_0 / 2$ fully specifies the noise process. <!--SR:!2026-02-11,89,369!2026-02-03,82,369-->
- [white noise](../../../../general/white%20noise.md) ::@:: It is a random signal having equal intensity at different frequencies, giving it a constant power spectral density. <!--SR:!2026-02-16,93,369!2026-01-31,79,369-->
  - white noise / "most random" ::@:: The random process has an autocorrelation of 0 between any two distinct time. <p> In practice, pseudo-random generators are judged by how closely their empirical autocorrelation approximates this ideal delta shape. A small but non-zero correlation at short lags indicates some residual predictability; larger lags should show essentially zero correlation. <!--SR:!2026-02-04,83,369!2026-02-17,94,369-->
  - white noise / verification ::@:: Using a spectrum analyzer or oscilloscope, one can plot the PSD to verify flatness or compute autocorrelation directly from recorded data. <p> Deviations from a constant PSD (e.g., colored noise) signal that higher-order moments are influencing the process or that the assumption of stationarity is violated. <!--SR:!2026-02-05,84,369!2026-02-16,93,369-->
- additive white Gaussian noise
  - additive white Gaussian noise / thermal noise ::@:: In a resistor, countless electrons undergo random Brownian motion due to thermal agitation (temperature $T$). Each electron's movement contributes a tiny current; summing over all electrons produces a continuous voltage fluctuation. By the Central Limit Theorem \(CLT\), the sum of many independent microscopic contributions tends toward a Gaussian distribution, explaining why Johnson-Nyquist noise is modeled as white Gaussian. <!--SR:!2026-01-19,66,349!2026-02-17,94,369-->
  - additive white Gaussian noise / modeling ::@:: When modeling real systems, one must choose an appropriate representation (discrete vs continuous) to capture realistic temporal correlations. <p> For example, weather or lottery outcomes are discrete-time processes and inherently correlated over days, unlike the ideal continuous-time white noise model. <!--SR:!2026-02-16,93,369!2026-02-11,89,369-->
- ELEC 4110
  - ELEC 4110 / [binary modulation](binary%20modulation.md)
    - [§ binary channel](binary%20modulation.md#binary%20channel)
    - [§ receiver](binary%20modulation.md#receiver)
    - [§ bit error rate](binary%20modulation.md#bit%20error%20rate)
    - [§ bit error rate with zero threshold](binary%20modulation.md#bit%20error%20rate%20with%20zero%20threshold)
    - [§ bit error rate with arbitrary threshold](binary%20modulation.md#bit%20error%20rate%20with%20arbitrary%20threshold)
    - [§ bit error rate insight](binary%20modulation.md#bit%20error%20rate%20insight)
    - [§ using Q-function](binary%20modulation.md#using%20Q-function)

## week 3 lecture 2

- datetime: 2025-09-18T09:00:00+08:00/2025-09-18T10:20:00+08:00, PT1H20M
- topic: binary modulation optimization; bit error rate optimization; filter optimization
- ELEC 4110
  - ELEC 4110 / [binary modulation](binary%20modulation.md)
    - [§ bit error rate](binary%20modulation.md#bit%20error%20rate)
    - [§ bit error rate with zero threshold](binary%20modulation.md#bit%20error%20rate%20with%20zero%20threshold)
    - [§ bit error rate with arbitrary threshold](binary%20modulation.md#bit%20error%20rate%20with%20arbitrary%20threshold)
    - [§ bit error rate insight](binary%20modulation.md#bit%20error%20rate%20insight)
    - [§ using Q-function](binary%20modulation.md#using%20Q-function)
    - [§ optimization](binary%20modulation.md#optimization)
    - [§ bit error rate optimization](binary%20modulation.md#bit%20error%20rate%20optimization)
    - [§ filter optimization](binary%20modulation.md#filter%20optimization)
    - [§ response of LTI system to WSS random signal](binary%20modulation.md#response%20of%20LTI%20system%20to%20WSS%20random%20signal)

## week 3 tutorial

- datetime: 2025-09-19T15:30:00+08:00/2025-09-19T16:20:00+08:00, PT50M
- topic:

## week 4 lecture

- datetime: 2025-09-23T09:00:00+08:00/2025-09-23T10:20:00+08:00, PT1H20M
- topic: matched filter; correlator
- status: online
- [matched filter](../../../../general/matched%20filter.md) ::@:: The output of the __matched filter__ is given by correlating a known delayed signal, or _template_, with an unknown signal to detect the presence of the template in the unknown signal. This is equivalent to convolving the unknown signal with a conjugated time-reversed version of the template.
  - matched filter / optimality ::@:: The matched filter is the optimal linear filter for maximizing the signal-to-noise ratio \(SNR\) in the presence of additive stochastic noise.
- ELEC 4110
  - ELEC 4110 / [binary modulation](binary%20modulation.md)
    - [§ matched filter](binary%20modulation.md#matched%20filter)
    - [§ correlator](binary%20modulation.md#correlator)
    - [§ energy optimization](binary%20modulation.md#energy%20optimization)
- [signal modulation](../../../../general/signal%20modulation.md) ::@:: It is the process of varying one or more properties of a periodic waveform in electronics and telecommunication for the purpose of transmitting information.
- [non-return-to-zero](../../../../general/non-return-to-zero.md) ::@:: The line code is a binary code in which ones are represented by one significant condition, usually a positive voltage, while zeros are represented by some other significant condition, usually a negative voltage, with no other neutral or rest condition.
  - non-return-to-zero / bipolar ::@:: _One_ is represented by one physical level (usually a positive voltage), while _zero_ is represented by another level (usually a negative voltage). <p> \(__this course__: use the name "_antipodal signaling_"\)
    - non-return-to-zero / bipolar / signals ::@:: Note this is only one of the _possible_ implementations: $$\begin{aligned} s_0(t) & = -A && t \in [0, T] \\ s_1(t) & = A && t \in [0, T] \end{aligned}$$
  - non-return-to-zero / unipolar ::@:: _One_ is represented by a DC bias on the transmission line (conventionally positive), while _zero_ is represented by the absence of bias – the line at 0 volts or grounded. <p> \(__this course__: use the name "_non-return to zero_" \(NRZ\)\)
    - non-return-to-zero / unipolar / signals ::@:: Note this is only one of the _possible_ implementations: $$\begin{aligned} s_0(t) & = 0 && t \in [0, T] \\ s_1(t) & = A && t \in [0, T] \end{aligned}$$
- [amplitude-shift keying](../../../../general/amplitude-shift%20keying.md) \(ASK\) ::@:: It is a form of amplitude modulation that represents digital data as variations in the amplitude of a carrier wave. For example, if each symbol represents a single bit, then the carrier signal could be transmitted at nominal amplitude when the input value is 1, but transmitted at reduced amplitude or not at all when the input value is 0.
  - amplitude-shift keying / signals ::@:: Note this is only one of the _possible_ implementations: $$\begin{aligned} s_0(t) & = 0 && t \in [0, T] \\ s_1(t) & = A \cos(\omega t + \theta) && t \in [0, T] \end{aligned}$$ for some constant $\omega$ and $\theta$. Note we usually choose $\omega$ such that $\omega T$ is a multiple of $2\pi$ to ensure smooth phase transition between symbols.
- [phase-shift keying](../../../../general/phase-shift%20keying.md) \(PSK\) ::@:: It is a digital modulation process which conveys data by changing (modulating) the phase of a constant frequency carrier wave. The modulation is accomplished by varying the sine and cosine inputs at a precise time.
  - phase-shift keying / binary phase-shift keying \(BPSK\) ::@:: It is the simplest form of phase shift keying (PSK). It uses two phases which are separated by 180° and so can also be termed 2-PSK.
    - phase-shift keying / binary phase-shift keying / signals ::@:: Note this is only one of the _possible_ implementations: Note this is only one of the _possible_ implementations: $$\begin{aligned} s_0(t) & = -A \cos(\omega t + \theta) && t \in [0, T] \\ s_1(t) & = A \cos(\omega t + \theta) && t \in [0, T] \end{aligned}$$ for some constant $\omega$ and $\theta$. Note we usually choose $\omega$ such that $\omega T$ is a multiple of $2\pi$ to ensure smooth phase transition between symbols.
- [frequency-shift keying](../../../../general/frequency-shift%20keying.md) ::@:: It is a frequency modulation scheme in which digital information is encoded on a carrier signal by periodically shifting the frequency of the carrier between several discrete frequencies.
  - frequency-shift keying / signals ::@:: Note this is only one of the _possible_ implementations: Note this is only one of the _possible_ implementations: $$\begin{aligned} s_0(t) & = A \cos(\omega_1 t + \theta) && t \in [0, T] \\ s_1(t) & = A \cos(\omega_2 t + \theta) && t \in [0, T] \end{aligned}$$ for some constant $\omega_1$, $\omega_2$, and $\theta$. Note we usually choose $\omega_1$ and $\omega_2$ such that $\omega_1 \ne \omega_2$ and $\omega_1 T$ and $\omega_2 T$ are both multiples of $2\pi$ to ensure smooth phase transition between symbols.
- ELEC 4110
  - ELEC 4110 / [binary modulation](binary%20modulation.md)
    - [§ modulation schemes](binary%20modulation.md#modulation%20schemes)
    - [§ bipolar non-return-to-zero](binary%20modulation.md#bipolar%20non-return-to-zero)
    - [§ polar non-return-to-zero](binary%20modulation.md#polar%20non-return-to-zero)
    - [§ amplitude-shift keying](binary%20modulation.md#amplitude-shift%20keying)
    - [§ phase-shift keying](binary%20modulation.md#phase-shift%20keying)
    - [§ frequency-shift keying](binary%20modulation.md#frequency-shift%20keying)

---

__<big><big>Arrangement on Tue lecture (23/9)</big></big>__

> Dear students
>
> in view of the typhoon, let's do zoom lecture tomorrow at 9:00am. The physical lecture will resume on Thursday hopefully. Thanks
>
> \[redacted\]
>
> here is the zoom link
>
> \[redacted\]

---

> __<big><big>Zoom Recording and whiteboard for Tue Lecture (23/9)</big></big>__
>
> Hi Students
>
> Here is the whiteboard pdf \(in file\) and zoom recording. See you on Thursday.
>
> Recording:
>
> \[redacted\]

## week 4 lecture 2

- datetime: 2025-09-25T09:00:00+08:00/2025-09-25T10:20:00+08:00, PT1H20M
- topic: signal space; signal space motivation; signal space applications; geometric-domain representation; basis; coordinates; constellation diagram; Gram–Schmidt process
- ELEC 4110
  - ELEC 4110 / [signal space](signal%20space.md)
    - [§ motivation](signal%20space.md#motivation)
    - [§ applications](signal%20space.md#applications)
    - [§ receiver optimization](signal%20space.md#receiver%20optimization)
    - [§ M-ary modulation](signal%20space.md#M-ary%20modulation)
    - [§ geometric domain](signal%20space.md#geometric%20domain)
    - [§ basis](signal%20space.md#basis)
    - [§ coordinates](signal%20space.md#coordinates)
    - [§ definition](signal%20space.md#definition)
    - [§ energy](signal%20space.md#energy)
    - [§ constellation diagram](signal%20space.md#constellation%20diagram)
    - [§ Gram–Schmidt process](signal%20space.md#Gram–Schmidt%20process)

## week 4 tutorial

- datetime: 2025-09-26T15:30:00+08:00/2025-09-26T16:20:00+08:00, PT50M
- topic:

## week 5 lecture

- datetime: 2025-09-30T09:00:00+08:00/2025-09-30T10:20:00+08:00, PT1H20M
- topic: signal space algebraic properties; inner product; vector space; Gram–Schmidt process; signal space examples; binary modulation; binary channel; binary receiver; bit error rate
- ELEC 4110
  - ELEC 4110 / [signal space](signal%20space.md)
    - [§ properties](signal%20space.md#properties)
    - [§ algebraic properties](signal%20space.md#algebraic%20properties)
    - [§ inner product](signal%20space.md#inner%20product)
    - [§ geometric concepts](signal%20space.md#geometric%20concepts)
    - [§ coordinate representation](signal%20space.md#coordinate%20representation)
    - [§ orthogonality and orthonormality](signal%20space.md#orthogonality%20and%20orthonormality)
    - [§ linear transformations](signal%20space.md#linear%20transformations)
    - [§ linear independence](signal%20space.md#linear%20independence)
    - [§ triangle inequality](signal%20space.md#triangle%20inequality)
    - [§ Cauchy–Schwarz inequality](signal%20space.md#Cauchy–Schwarz%20inequality)
    - [§ Pythagorean relation](signal%20space.md#Pythagorean%20relation)
    - [§ Gram–Schmidt process](signal%20space.md#Gram–Schmidt%20process)
    - [§ examples](signal%20space.md#examples)
    - [§ sinusoidal examples](signal%20space.md#sinusoidal%20examples)
- ELEC 4110
  - ELEC 4110 / [binary modulation](binary%20modulation.md)
    - [§ binary channel](binary%20modulation.md#binary%20channel)
    - [§ receiver](binary%20modulation.md#receiver)
    - [§ bit error rate](binary%20modulation.md#bit%20error%20rate)

## week 5 lecture 2

- datetime: 2025-10-02T09:00:00+08:00/2025-10-02T10:20:00+08:00, PT1H20M
- topic: binary receiver; bit error rate; M-ary transmission; constellation diagram; M-PSK; M-QAM; M-FSK; optimal M-ary receiver; noise vector; minimum distance decision rule
- ELEC 4110
  - ELEC 4110 / [binary modulation](binary%20modulation.md)
    - [§ receiver](binary%20modulation.md#receiver)
    - [§ bit error rate](binary%20modulation.md#bit%20error%20rate)
- [_M_-ary transmission](../../../../general/M-ary%20transmission.md) ::@:: It is a type of digital modulation. Instead of sending one bit at a time as in binary, multiple messages, M, are sent. The binary data stream is divided into n tuples, where n = log₂ M bits. The signals can be represented as different frequencies, as in MFSK.
  - _M_-ary transmission / advantages ::@:: This type of transmission results in reduced channel _bandwidth_ \(compared to halving the symbol time, which doubles the bandwidth\) at the expense of higher bit error rates.
- ELEC 4110
  - ELEC 4110 / [_M_-ary transmission](M-ary%20transmission.md)
    - [§ background](M-ary%20transmission.md#background)
    - [§ energy and power](M-ary%20transmission.md#energy%20and%20power)
    - [§ bandwidth](M-ary%20transmission.md#bandwidth)
    - [§ digital modulation](M-ary%20transmission.md#digital%20modulation)
    - [§ signal space](M-ary%20transmission.md#signal%20space)
    - [§ constellation diagram](M-ary%20transmission.md#constellation%20diagram)
    - [§ modulation families](M-ary%20transmission.md#modulation%20families)
    - [§ M-PSK](M-ary%20transmission.md#M-PSK)
    - [§ M-QAM](M-ary%20transmission.md#M-QAM)
    - [§ M-FSK](M-ary%20transmission.md#M-FSK)
    - [§ optimal receiver](M-ary%20transmission.md#optimal%20receiver)
    - [§ channel](M-ary%20transmission.md#channel)
    - [§ noise vector](M-ary%20transmission.md#noise%20vector)
    - [§ minimum distance](M-ary%20transmission.md#minimum%20distance)

## week 5 tutorial

- datetime: 2025-10-03T15:30:00+08:00/2025-10-03T16:20:00+08:00, PT50M
- topic:

## week 6 lecture

- datetime: 2025-10-07T09:00:00+08:00/2025-10-07T10:20:00+08:00, PT1H20M
- status: unscheduled; public holiday: Day after Mid-Autumn Festival

## week 6 lecture 2

- datetime: 2025-10-09T09:00:00+08:00/2025-10-09T10:20:00+08:00, PT1H20M
- topic: minimum distance decision rule; energy optimization; M-ary transmission implementation; M-FSK; M-pSK; M-QAM
- ELEC 4110
  - ELEC 4110 / [_M_-ary transmission](M-ary%20transmission.md)
    - [§ minimum distance](M-ary%20transmission.md#minimum%20distance)
    - [§ error analysis for minimum distance](M-ary%20transmission.md#error%20analysis%20for%20minimum%20distance)
  - ELEC 4110 / [binary modulation](binary%20modulation.md)
    - [§ energy optimization](binary%20modulation.md#energy%20optimization)
  - ELEC 4110 / [_M_-ary transmission](M-ary%20transmission.md)
    - [§ implementation](M-ary%20transmission.md#implementation)
    - [§ complexity](M-ary%20transmission.md#complexity)
    - [§ constellation diagram](M-ary%20transmission.md#constellation%20diagram)
    - [§ M-FSK](M-ary%20transmission.md#M-FSK)
    - [§ M-PSK](M-ary%20transmission.md#M-PSK)
    - [§ M-QAM](M-ary%20transmission.md#M-QAM)
    - [§ peak-to-average power ratio](M-ary%20transmission.md#peak-to-average%20power%20ratio)

## week 6 tutorial

- datetime: 2025-10-10T15:30:00+08:00/2025-10-10T16:20:00+08:00, PT50M
- topic:

## week 7 lecture

- datetime: 2025-10-14T09:00:00+08:00/2025-10-07T10:20:00+08:00, PT1H20M
- status: canceled; sickness

---

> __<big><big>Cancellation of Lecture on 14 October (Tue)</big></big>__
>
> Dear students
>
> I am sorry that the lecture tomorrow \(14 October 09:00-10:20am\) will be cancelled due to a medical appointment that I cannot reschedule. The lecture will be resumed on Thursday. Thanks a lot
>
> \[redacted\]

## week 7 lecture 2

- datetime: 2025-10-16T09:00:00+08:00/2025-10-09T10:20:00+08:00, PT1H20M
- topic: ???
- ELEC 4110
  - ELEC 4110 / [M-ary transmission](M-ary%20transmission.md)
    - [§ effects of bandwidth and power](M-ary%20transmission.md#effects%20of%20bandwidth%20and%20power)
    - [§ decision regions](M-ary%20transmission.md#decision%20regions)
    - [§ maximum likelihood](M-ary%20transmission.md#maximum%20likelihood)

## week 7 tutorial

- datetime: 2025-10-17T15:30:00+08:00/2025-10-10T16:20:00+08:00, PT50M
- topic:

## week 8 lecture

- datetime: 2025-10-21T09:00:00+08:00/2025-10-07T10:20:00+08:00, PT1H20M
- topic:
- [channel capacity](../../../../general/channel%20capacity.md) ::@:: It in electrical engineering, computer science, and information theory, is the theoretical maximum rate at which information can be reliably transmitted over a communication channel.
- [Shannon–Hartley theorem](../../../../general/Shannon–Hartley%20theorem.md) ::@:: It tells the maximum rate at which information can be transmitted over a communications channel of a specified bandwidth in the presence of noise.
  - Shannon–Hartley theorem / noisy-channel coding theorem ::@:: It is an application of the noisy-channel coding theorem to the archetypal case of a continuous-time analog communications channel subject to Gaussian noise.
  - Shannon–Hartley theorem / conditions ::@:: The theorem establishes Shannon's channel capacity for such a communication link, a bound on the maximum amount of error-free information per time unit that can be transmitted with a specified bandwidth in the presence of the noise interference, assuming that the signal power is bounded, and that the Gaussian noise process is characterized by a known power or power spectral density.
  - Shannon–Hartley theorem / statement ::@:: It gives the maximum achievable data rate of a noisy channel: $$C=B\log_{2}\!\left(1+\frac{S}{N}\right)\quad(\text{bits/s}) \,,$$ where $B$ is the bandwidth (Hz), $S$ the average received signal power, and $N$ the noise power over that band.  The ratio $S/N$ is the linear signal-to-noise (or carrier-to-noise) ratio.  $C$ represents an upper bound on the net information rate—excluding any error-correction overhead—and holds for additive white Gaussian noise channels.
    - Shannon–Hartley theorem / statement / noise ::@:: For AWGN of _two-sided_ PSD $N_0 / 2$, this means its _one-sided_ PSD is $N_0$, which is the noise power per frequency. The noise power over the bandwidth $B$ is then $N = N_0 B$.
    - Shannon–Hartley theorem / statement / spectral efficiency ::@:: Rearranging the formula, we get _spectral efficiency_: $$\frac C B = \log_2\!\left(1+\frac{S}{N}\right)\quad(\text{bits/s/Hz}) \,.$$ We see to increase spectral efficiency, we have to increase the signal-to-noise power ratio $S / N$.
    - Shannon–Hartley theorem / statement / energy efficiency ::@:: Often, when discussing _energy efficiency_, we use SNR per symbol $E_s / N_0$ or _SNR per bit_ $E_b / N_0$. Using the latter, we have: $$\frac {E_b} {N_0} = \frac {ST_b} {N / B} = \frac B C \frac S N = \frac B C \left(2^{C / B} - 1 \right) \,.$$
    - Shannon–Hartley theorem / statement / Shannon limit ::@:: We want to find the minimum _SNR per bit_ $E_b / N_0$ for any useful bits to be transmitted. Using $$\frac {E_b} {N_0} = \frac B C \left(2^{C / B} - 1 \right) \,,$$ take the limit as $C / B \to 0$ \(approaching sending no data\), then we have $$\frac {E_b} {N_0} \to \frac 1 {\log_2 e} = \ln 2 \approx 0.693 \approx -1.59~\text{dB} \,.$$ That is, given AWGN noise of _two-sided_ PSD $N_0 / 2$, the above is the lowest SNR per bit possible for us to send any data through the channel.

## week 8 lecture 2

- datetime: 2025-10-23T09:00:00+08:00/2025-10-09T10:20:00+08:00, PT1H20M
- topic:

## week 8 tutorial

- datetime: 2025-10-24T15:30:00+08:00/2025-10-10T16:20:00+08:00, PT50M
- topic:

## aftermath

### total

- grades: ?/100
  - statistics: ?
