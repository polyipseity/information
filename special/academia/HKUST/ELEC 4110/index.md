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

- [assignments](assignments/index.md)
- [questions](questions.md)

## week 1 lecture

- datetime: 2025-09-02T09:00:00+08:00/2025-09-02T10:20:00+08:00, PT1H20M
- topic: logistics; overview of digital communications; signal; analog signal
- ELEC 4110
  - ELEC 4110 / introduction ::@:: _Digital communications_ is one of the technologies enabling the _Information Age_.
  - ELEC 4110 / structure ::@:: The class is split into two major themes: first, the fundamentals of digital communication theory (chapters 1‑6), then a systems‑centric view of wireless networks starting from chapter 7 onward (cellular/5G focus).
    - ELEC 4110 / structure / lectures ::@:: In the early lectures we'll build the mathematical foundations; later we'll apply those concepts to real‑world scenarios such as multi‑user cellular architectures and 5G design principles.<p> The goal is not only to understand how a system operates but also why certain design choices are made, linking theory directly to practical engineering decisions.
  - ELEC 4110 / questions ::@:: What is information? What is signal? How to represent them? How to communicate them wirelessly? What are cellular networks? How have they evolved?
  - ELEC 4110 / instructor ::@:: - ProfessorVincent: Hong Kong → HKU undergrad → 3 yrs at monopoly operator _Tandicom_ → chartered engineer path <br/> - PhD in the UK: peer‑controversial (HK industry scarcity) → viewed as adventure, not guaranteed success <br/> - Post‑PhD: Bell Labs US → realized academia's knowledge was superficial vs. depth needed for cutting‑edge research/product development
    - ELEC 4110 / instructor / background ::@:: Vincent was born in Hong Kong, earned his undergraduate degree at the University of Hong Kong, and spent three years working for the monopoly operator _Tandicom_ where he gained early exposure to telecom operations and a clear career path toward chartered engineer status.
    - ELEC 4110 / instructor / PhD ::@:: He then pursued a PhD in the UK—a decision that was controversial among peers because the HK research landscape offers few industry opportunities; nevertheless, he viewed it as an adventure rather than a guaranteed success.
    - ELEC 4110 / instructor / post-PhD ::@:: After his doctorate, Vincent joined Bell Labs in the U.S., where he realized that much of what he thought he knew from academia was superficial compared to the depth required for cutting‑edge research and product development.
    - ELEC 4110 / instructor / teaching ::@:: The instructor emphasizes the dual questions of "how" a system operates and "why" it is designed that way. While practical step‑by‑step explanations cover the former, addressing the latter requires a robust theoretical framework that translates engineering intuition into fundamental principles. He argues that both hands‑on domain knowledge and deep theory are crucial for advancing wireless technology from maintenance to innovative design.
    - ELEC 4100 / instructor / academia ::@:: Vincent contrasts undergraduate studies—centered on absorbing existing knowledge and passing exams—with doctoral research, which involves creating new knowledge amid uncertainty and extended timelines. He recounts peers who lingered into their eighth year without a clear graduation path, highlighting the unpredictable nature of academic careers.
    - ELEC 4100 / instructor / industry ::@:: At Bell Labs, he observed an interview split into a morning "output" session testing presentation skills and an afternoon "input" phase evaluating rapid comprehension, underscoring the dual importance of communication and quick learning.
  - ELEC 4100 / tips ::@:: Students should preview posted notes yet depend mainly on live lectures for depth, taking concise, organized notes during class; they must cultivate both clear articulation of complex ideas (output) and rapid extraction of key information from new material (input); by viewing the course as a link between theory and industry practice, they gain a dual perspective essential for designing or evaluating future wireless systems.
    - ELEC 4110 / tips / asking questions ::@:: The lecturer contrasts presenting information with quickly grasping essential details, judging comprehension by whether students ask meaningful questions during new topics; a lack of questions can mean either perfect understanding or total confusion, underscoring the learner's active role in seeking clarity. He urges students to treat every lecture as practice for comprehension, encouraging focused questioning when uncertain and using external resources—while stressing that this cannot be automated and requires personal effort—to foster a culture of inquiry that benefits both individual learning and the classroom environment.
  - ELEC 4110 / grading
  - ELEC 4110 / coursework ::@:: homework, midterm examination, MATLAB simulation project, final examination
    - ELEC 4110 / coursework / examinations ::@::  The midterm covers the first half of the syllabus—digital communication theory. <p> The final exam spans all course material, including system‑design scenarios, and may present complex formulas that will be supplied on the question sheet. Answers must show conceptual understanding and logical reasoning rather than lengthy algebraic work. The final exam emphasizes scenario‑based questions requiring design and justification rather than rote definitions.
  - ELEC 4110 / prerequisites ::@:: linear system analysis \(Fourier transform, linear systems\), noise, stochastic processes, signal analysis \(sampling, signal models, signals\)
  - ELEC 4110 / materials ::@:: See lecture notes on Canvas. They are posted at least 1 lecture in advanced. There may be hand-written comments on the whiteboard as well.
  - ELEC 4110 / textbook
  - ELEC 4110 / mathematics ::@:: Mathematics is used to _precisely_ model signals for communications. However, the mathematics itself is not the final objective of this course. Instead, they are how and why communications work in practice. <p> In short, mathematics is the language to make things _precise_. But we need to _comprehend_ beyond the language of mathematics.
  - ELEC 4110 / intuition ::@:: Intuition built from domain knowledge—such as communication theory fundamentals—helps students anticipate system behavior and evaluate design trade‑offs, guiding them toward viable solutions that meet specifications. The lecturer notes that intuition is only a rough guide; mathematics must be used to formalize and test these insights with precise predictions. Through exercises and projects that blend gut feeling with rigorous analysis, students strengthen this synergy, making it easier to approach novel exam problems.
  - ELEC 4110 / coursework
    - ELEC 4110 / coursework / project ::@:: The MATLAB group project requires teams to model a communication scenario—such as channel coding or modulation—and evaluate its performance metrics while clearly documenting assumptions, design choices, and results in a written report. These hands‑on experiments reinforce theoretical concepts through data analysis and encourage peer collaboration that mirrors real‑world engineering teamwork. The final deliverable consists of code, plots, and an explanatory narrative that connects simulation outcomes to the underlying theory.
    - ELEC 4110 / coursework / homework ::@:: Homework and problem sets evaluate quantitative skills with questions designed to minimize tedious algebra; solutions should emphasize key reasoning steps rather than lengthy derivations. The instructor will give feedback on conceptual clarity, methodological soundness, and correct theory application, while expecting students to submit clearly structured responses (e.g., numbered steps, annotated equations). Regular practice is crucial for mastering the transition from problem statement to analytical solution.
  - ELEC 4110 / culture ::@:: The lecturer stresses that while students won't be compelled to ask questions, cultivating curiosity is essential, and classroom Q&A sessions aim to normalize inquiry and lessen the stigma of uncertainty. By fostering this environment, the course seeks to improve individual understanding and collective knowledge sharing, boosting students' confidence in tackling new material and articulating their ideas. This culture of continuous learning aligns with industry expectations that value ongoing inquiry and skill development.
- [communication](../../../../general/communication.md) ::@:: It is commonly defined as the transmission of information. Its precise definition is disputed and there are disagreements about whether unintentional or failed transmissions are included and whether communication not only transmits meaning but also creates it.
  - communication / examples ::@:: molecular communication, short-range communication, telecommunication, etc.
  - communication / considerations ::@:: When implementing communication, there are many _practical_ considerations. <p> For example, using a physical string connected between two cups to communicate is impractical for many reasons. The distance between A and B shapes design goals: 10‑km links differ fundamentally from meter‑scale Bluetooth.
    - communication / considerations / historical comparison ::@:: Ancient smoke‑fire signals transmitted a single bit across vast distances, marking an early form of digital communication. <p> Modern optical fibre now supports 10‑km links with high data rates, low cost, and minimal noise—replacing older telephone cables that were expensive and suffered from poor quality due to limited media technology. <p> This progression from mechanical to electronic links illustrates how advances in media properties have expanded signal fidelity and reach, underscoring the fundamental role of medium characteristics in defining communication performance limits.
    - communication / considerations / attenuation ::@:: A simple mechanical telephone model transmits voice vibrations through a metal can and string, but energy lost to friction and air radiation caused rapid attenuation that limited its range to meters—showing why modern digital links require active amplification and low‑loss media and revealing how physical losses bound channel capacity. <p> A historical intercom system in a Qing dynasty mansion used copper tubing as an acoustic guide to relay signals between rooms over a few metres, yet the same attenuation prevented scaling beyond building‑scale distances. <p> Together these examples illustrate that engineering adapts medium properties—whether metal can, string, or copper waveguide—to meet specific application ranges while acknowledging fundamental limits imposed by physical loss mechanisms.
- [information](../../../../general/information.md) ::@:: It is an abstract concept that refers to something which has the power to inform.
  - information / signal processing ::@:: Information is represented by physical signals.
  - information / entropy ::@:: It of a random variable quantifies the average level of uncertainty or information associated with the variable's potential states or possible outcomes. <p> An important equation \(to be explained later\) to measure information entropy is: $$H(X) = -\sum_{X} p(X) \log_2 p(X) \,,$$ where $X$ is a discrete random variable with probability mass function $p(X)$.
- [signal processing](../../../../general/signal%20processing.md) ::@:: It is an electrical engineering subfield that focuses on analyzing, modifying and synthesizing signals, such as sound, images, potential fields, seismic signals, altimetry processing, and scientific measurements.
- [analog signal](../../../../general/analog%20signal.md) ::@:: It is any signal, typically a continuous-time signal, representing some other quantity, i.e., _analogous_ to another quantity.
  - analog signal / examples ::@:: ECG waveforms, voice recordings, etc.
  - analog signal / information ::@:: Information is encoded in measurable attributes such as amplitude, phase, or temporal shape; visualizing a waveform in the time domain instantly reveals its structure and shows how the signal’s form directly reflects the underlying content. <p> While entropy will formalize uncertainty in later courses, this course concentrates on intuitive signal interpretation.
- [time domain](../../../../general/time%20domain.md) ::@:: It is a representation of how a signal, function, or data set varies with time. It is used for the analysis of mathematical functions, physical signals or time series of economic or environmental data.
  - time domain / intuition ::@:: The signal is represented using a time function from zero time \(inclusive\) to infinite time \(exclusive\). Very visually intuitive.
- [periodic function](../../../../general/periodic%20function.md) ::@:: It is a function that repeats its values at regular intervals. <p> The length of the interval over which a periodic function repeats is called its __period__. Any function that is not periodic is called __aperiodic__.
  - periodic function / examples ::@:: For example, the trigonometric functions, which are used to describe waves and other repeating phenomena, are periodic.
  - periodic function / period ::@:: A positive number $T$ such that $f(t + T) = f(t)$ for all $t$.
  - periodic function / frequency ::@:: $f = 1 / T$ \(in hertz if $T$ is in second\)
  - periodic function / description ::@:: To describe the entire signal, describe a cycle suffices.
- [sine wave](../../../../general/sine%20wave.md) ::@:: It is a periodic wave whose waveform \(shape\) is the trigonometric sine function.
  - sine wave / sinusoid form ::@:: Sine waves of arbitrary phase and amplitude are called _sinusoids_ and have the general form: $$y(t)=A\sin(\omega t+\varphi )=A\sin(2\pi ft+\varphi )$$ where: <p> - $A$, _[amplitude](../../../../general/amplitude.md)_, the peak deviation of the function from zero. <br/> - $t$, the [real](../../../../general/real%20number.md) [independent variable](../../../../general/independent%20variable.md), usually representing [time](../../../../general/time.md) in [seconds](../../../../general/seconds.md). <br/> - $\omega$, _[angular frequency](../../../../general/angular%20frequency.md)_, the rate of change of the function argument in units of [radians per second](../../../../general/radians%20per%20second.md). <br/> - $f$, _[ordinary frequency](../../../../general/ordinary%20frequency.md)_, the _[number](../../../../general/real%20number.md)_ of oscillations \([cycles](../../../../general/turn%20(angle).md)\) that occur each second of time. <br/> - $\varphi$, _[phase](../../../../general/phase%20(waves).md)_, specifies \(in [radians](../../../../general/radian.md)\) where in its cycle the oscillation is at _t_ = 0.
  - sine wave / cosine wave ::@:: Since $$\begin{aligned} \sin x & = \cos(x - \pi / 2) \\ \cos x & = \sin(x + \pi / 2) \,, \end{aligned}$$ so any sine wave can be represented as a cosine wave with a shifted phase, and vice versa.
  - sine wave / description ::@:: To describe a sine wave, describe its amplitude $A$, angular frequency $\omega$, and phase $\phi$.
  - sine wave / significance ::@:: Grasping a sinusoid's key parameters—amplitude, frequency, and phase—is essential before tackling Fourier analysis or modulation concepts, because sinusoids form the building blocks for more complex signals central to communication theory. <p> Mastery of sinusoid representation provides the foundation needed to analyze channels, noise, and bandwidth throughout the course.
- [phasor](../../../../general/phasor.md) ::@:: It is a complex number representing a sinusoidal function whose amplitude _A_ and initial phase _θ_ are time-invariant and whose angular frequency _ω_ is fixed.
  - phasor / equation ::@:: $$s(t) = \Re(A \exp(j \phi) \exp(j \omega t)) = \Re(Z \exp(j \omega t)) \,.$$ $Z = A \exp(j \phi)$ is the _complex amplitude_, which incorporates both the amplitude and phase.
- [spectral density](../../../../general/spectral%20density.md) ::@:: Fourier analysis shows that any physical signal can be decomposed into a distribution of frequencies over a continuous range, where some of the power may be concentrated at discrete frequencies. The statistical average of the energy or power of any type of signal (including noise) as analyzed in terms of its frequency content, is called its __spectral density__.
  - spectral density / one-sided vs. two-sided ::@:: Some textbooks plot a two‑sided spectrum that includes negative frequencies, while others show only the positive side \(one‑sided\). <p> Negative frequencies appear when a real sinusoid is represented as a sum of a positive‑frequency term and its complex conjugate. <p> A one‑sided spectrum omits this redundant component because it can be recovered by symmetry for real signals.
- periodic function
  - periodic function / arithmetic operation ::@:: Performing arithmetic operations between two periodic functions may _not_ yield a periodic function. This happens when their angular frequencies do not have a least common multiple \(LCM\). For example, this happens when one of angular frequency is _irrational_.
  - periodic function / aperiodic ::@:: If a function is not periodic, then it is _aperiodic_. This happens if a positive $T$ such that $s(t + T) = s(t)$ for all $t$ does not exist.
- [Fourier transform](../../../../general/Fourier%20transform.md) ::@:: It is an integral transform that takes a function as input, and outputs another function that describes the extent to which various frequencies are present in the original function. The output of the transform is a complex-valued function of frequency.
  - Fourier transform / intuition ::@:: Any periodic waveform can be decomposed into an infinite sum of sinusoids (Fourier series). <p> Non‑periodic signals are represented by the continuous‑frequency Fourier transform, which also uses sinusoidal basis functions.
  - Fourier transform / real signals ::@:: For real signals each sinusoid contributes a positive‑frequency term plus its complex conjugate at negative frequency; this explains the two‑sided nature of the spectrum in the exponential form.
- periodic function
  - periodic function / aperiodic
    - periodic function / aperiodic / examples ::@:: Common aperiodic waveforms include step, impulse (Dirac delta), and triangular pulse. <p> These signals do not repeat over time but serve as fundamental building blocks for system analysis (e.g., impulse response).
- [Heaviside step function](../../../../general/Heaviside%20step%20function.md) ::@:: It is a step function named after Oliver Heaviside, the value of which is zero for negative arguments and one for positive arguments. Different conventions concerning the value _H_\(0\) are in use. \(__this course__: _H_\(0\)&nbsp;=&nbsp;1\)
- [Dirac delta function](../../../../general/Dirac%20delta%20function.md) ::@:: It is a [generalized function](../../../../general/generalized%20function.md) on the [real numbers](../../../../general/real%20numbers.md), whose value is zero everywhere except at zero, and whose [integral](../../../../general/integral.md) over the entire real line is equal to one. Thus it can be [represented heuristically](../../../../general/heuristic.md) as $$\delta (x)={\begin{cases}0,&x\neq 0\\{\infty },&x=0\end{cases} }$$ such that $$\int _{-\infty }^{\infty }\delta (x)dx=1.$$
- [ramp function](../../../../general/ramp%20function.md) ::@:: It is a unary real function, whose graph is shaped like a ramp. It can be expressed by numerous definitions, for example "0 for negative inputs, output equals input for non-negative inputs".
- [rectangular function](../../../../general/rectangular%20function.md) ::@:: It is defined as $$\operatorname {rect} \left({\frac {t}{a} }\right)=\Pi \left({\frac {t}{a} }\right)=\left\{ {\begin{array}{rl}0,&{\text{if } }|t|>{\frac {a}{2} }\\{\frac {1}{2} },&{\text{if } }|t|={\frac {a}{2} }\\1,&{\text{if } }|t|<{\frac {a}{2} }.\end{array} }\right.$$ Alternative definitions of the function define $\operatorname {rect} \left(\pm {\frac {1}{2} }\right)$ to be 0, or undefined.
- [triangular function](../../../../general/triangular%20function.md) ::@:: It is a function whose graph takes the shape of a triangle. Often this is an isosceles triangle of height 1 and base 2 in which case it is referred to as _the_ triangular function.
- analog signal
  - analog signal / basic operations ::@:: amplitude transformations: $As(t) + B$; $A$ scales the range about the horizontal axis and $B$ shifts vertically <br/> time reversal: $s(-t)$ \(special case of time scaling when $a = -1$\) <br/> time scaling: $s(at)$; compressed if $\lvert a \rvert > 1$ or expanded if $\lvert a \rvert < 1$ <br/> time shifting: $x(t - a)$; delayed \(moved towards the _right_\) by $a$
- [digital signal](../../../../general/digital%20signal.md) ::@:: It is a signal that represents data as a sequence of discrete values; at any given time it can only take on, at most, one of a finite number of values. <p> \(__this course__: Both values and time are discrete for a digital signal. This is different from the definition used above.\)
  - digital signal / vs. analog signal ::@:: This _contrasts_ with an analog signal, which represents continuous values; at any given time it represents a real number within an infinite set of values. <p> \(__this course__: Both values and time are continuous for an analog signal. This is different from the definition used above.\)
- [analog-to-digital converter](../../../../general/analog-to-digital%20converter.md) \(ADC\) ::@:: It is a system that converts an analog signal, such as a sound picked up by a microphone or light entering a digital camera, into a digital signal.
  - analog-to-digital converter / steps ::@:: sampling → quantization
    - analog-to-digital converter / steps / sampling ::@:: Continuous time is converted into discrete time by repeated _sampling_ at a fixed time interval. <p> This limits _bandwidth_. According to the _Nyquist–Shannon sampling theorem_, _perfect reconstruction_ is possible if $B < f_s / 2$, where $B$ is the bandwidth of the continuous time signal and $f_s$ is the sample rate.
    - analog-to-digital converter / steps / quantization ::@:: Continuous value is converted into discrete value by converting them into _n_-bit numbers. <p> This produces _quantization error_, as continuous value has \(uncountably\) infinite possible values while _n_-bit numbers have finite possible values. Thus this process is _irreversible_ in general.
- [Nyquist–Shannon sampling theorem](../../../../general/Nyquist–Shannon%20sampling%20theorem.md) ::@:: It is an essential principle for digital signal processing linking the frequency range of a signal and the sample rate required to avoid a type of distortion called aliasing. The theorem states that the sample rate must be at least twice the bandwidth of the signal to avoid aliasing.
  - Nyquist–Shannon sampling theorem / applications ::@:: Enables technologies like TDMA in GSM and other digital communication schemes; without it, time‑division multiplexing would lose information irrecoverably. <p> The theorem underpins all modern DSP because it guarantees that a continuous‑time bandlimited signal can be fully captured by discrete samples.
- analog-to-digital converter
  - analog-to-digital converter / bit depth ::@:: Fewer bits → coarser signal levels → larger quantization noise; more bits → finer signal levels → smaller distortion. <p> The trade‑off between storage/computation cost and signal fidelity is central to digital audio/video design. In consumer devices (phones, TVs), manufacturers choose sampling rates and bit depths that balance perceptual quality with power/size constraints.

## week 1 lecture 2

- datetime: 2025-09-04T09:00:00+08:00/2025-09-04T10:20:00+08:00, PT1H20M
- topic: digital signal; magnetic tape; digital audio; digital video; public switched telephone network; amplifier; data transmission; regenerator; frequency domain; amplitude spectrum; phase spectrum
- analog signal
- digital signal
  - digital signal / discrete-time signal ::@:: Only the time axis is sampled (discrete), but the amplitude may still be continuous \(or not\); these are not yet digital signals.
- analog-to-digital converter
- Nyquist–Shannon sampling theorem
- analog-to-digital converter
  - analog-to-digital converter / bit depth
    - analog-to-digital converter / bit depth / effects ::@:: The error introduced equals the difference between the original sample and its nearest quantization level; the worst‑case error is half the step size $\Delta / 2$. <p> Increasing the number of bits halves $\Delta$ (e.g., moving from 3 to 4 bits doubles the number of levels), thereby reducing the maximum quantization error by a factor of two.
- [signal-to-noise ratio](../../../../general/signal-to-noise%20ratio.md) \(SNR, S/N\) ::@:: It is a measure used in science and engineering that compares the level of a desired signal to the level of background noise. SNR is defined as the ratio of signal power to noise power, often expressed in decibels.
  - signal-to-noise ratio / formula ::@:: $$\text{SNR} = \frac {\text{signal (without noise) power} } {\text{noise power} } \,.$$ However, it is often expressed in decibels \(dB\) instead: $$\text{SNR}_{\text{dB} } = 10 \log_{10} \text{SNR} \,.$$ 0 dB means same the signal has the same power as noise. Every 10&nbsp;dB increase in SNR multiplies the signal power by 10, so that 10&nbsp;dB means 10 times, 20&nbsp;dB means 100 times, 30&nbsp;dB means 1000 times, etc.
    - signal-to-noise ratio / formula / amplitude ::@:: When we work with signal amplitudes rather than powers, the definition of SNR is still based on power. <p> Because electrical power is proportional to the square of voltage (or current), converting this amplitude ratio into decibels uses a factor of 20 instead of 10: $$\boxed{\;\text{SNR}_{\text{dB}}
   =20\,\log_{10}\!\left(\frac{A_{\text{signal}}}{A_{\text{noise}}}\right)\;}$$ <p> This formula is equivalent to the power‑based expression $10\log_{10}(\text{SNR})$ because $(A_{\text{signal}}/A_{\text{noise}})^2 = \text{SNR}$. Thus, a 10-fold increase in amplitude ratio corresponds to a 100‑fold increase in \(power\) SNR.
  - signal-to-noise ratio / quantization ::@:: Under common assumptions—input is a sinusoid, noise uniformly distributed over $[-\Delta/2,\;\Delta/2]$—the SNR improves roughly $6.02\,\text{dB}$ per added bit: $$\text{SNR}_{\text{dB}} \approx 6.02\,n + C$$ where $n$ is bits per sample and $C$ depends on the signal shape \(for sine wave, $C = 20 \log_{10}\left(\sqrt{3 / 2}\right) \approx 1.761$\). <p> This rule of thumb guides how many bits are needed for a target audio or communication quality. Note real signals like speech have different dynamic ranges, so the actual SNR may deviate from this simple estimate.
    - signal-to-noise ratio / quantization / examples ::@:: High‑fidelity audio (CD) requires about 16 bits/sample to achieve an SNR sufficient for music listening; the standard sampling rate is 44.1 kHz, exceeding twice the audible bandwidth (~20 kHz). <p> Telephony uses only 8 bits/sample at a lower sampling rate (8 kHz), yielding a lower SNR that is adequate for voice but noticeably poorer than CD audio.
- analog-to-digital converter
  - analog-to-digital converter / bit depth
    - analog-to-digital converter / bit depth / examples ::@:: In digital communications, the receiver's analog‑to‑digital converter must preserve the signal‑to‑noise ratio needed by the modulation scheme; higher‑order constellations demand more bits. <p> Typical design practice employs 10–12 bits for the ADC path when high‑order modulations (e.g., 64‑QAM, 256‑QAM) are used to maintain acceptable error rates.
- signal-to-noise ratio
  - signal-to-noise ratio / dynamic range \(DR\) ::@:: It—the ratio between maximum and minimum signal amplitudes—affects how many quantization levels are required to achieve a given SNR for non‑sinusoidal inputs.
- [digital-to-analog converter](../../../../general/digital-to-analog%20converter.md) \(DAC\) ::@:: It is a system that converts a digital signal into an analog signal.
  - digital-to-analog converter / reverse ::@:: An analog-to-digital converter \(ADC\) performs the reverse function.
  - digital-to-analog converter / steps ::@:: reconstruction → lowpass filter
    - digital-to-analog converter / steps / reconstruction ::@:: Discrete time is converted into continuous time. <p> Each incoming B‑bit word is translated to a voltage level via a pre‑computed table (e.g., for 4 bits → 16 levels). The "zero‑order hold" (a simple capacitor) holds that voltage constant until the next sample arrives, creating a staircase waveform.
    - digital-to-analog converter / steps / lowpass filter ::@:: Discrete value is converted into continuous value. Holding the sampled value until the next sample yields a continuous-time signal with discrete value. Applying lowpass filter smoothens the signal and make it continuous-valued as well. <p> The lowpass filter frequency cutoff is usually half the sample rate due to the _Nyquist–Shannon sampling theorem_. If the original signal does not have frequencies higher than this cutoff, the only remaining error is quantization noise.
- analog signal
  - analog signal / disadvantages ::@:: ADC/DAC chips sit at the interface between noisy analog front‑ends and high‑speed digital logic. <p> They must be shielded against clock‑switching noise, power‑gating glitches, and substrate coupling—all of which can corrupt the analog signal path. <p> High‑resolution, high‑sampling‑rate devices are expensive, sometimes export‑controlled, and require careful PCB layout to maintain performance.
- digital signal
  - digital signal / advantages ::@:: It is _robust_ to degradation and noise, as small distortions of the waveform can be completely ignored. The mapping from waveform to bits introduces a decision threshold; only if noise pushes the signal past that threshold does an error occur.
  - digital signal / disadvantages ::@:: It cannot represent most physical signals _exactly_, as most of them are analog in nature.
  - digital signal / usage ::@:: Due to its robustness, it is used in storage and telecommunications.
    - digital signal / usage / storage ::@:: Analog storage (e.g., magnetic tape) degrades visibly over decades, while digital media (CDs, MP3s) retain fidelity for many years with negligible error.
    - digital signal / usage / telecommunications ::@:: Long-distance transmission cause path loss attenuation and thermal noise. If an analog signal is used, signal-to-noise ratio \(SNR\) decreases significantly at the receiver side, and may corrupt an analog waveform entirely. <p> If a digital signal is used, SNR remains sufficiently high due to its robustness to degradation and noise. As long as received bits are correctly interpreted, the information survives.
- [magnetic tape](../../../../general/magnetic%20tape.md) ::@:: It is a medium for magnetic storage made of a thin, magnetizable coating on a long, narrow strip of plastic film. It was developed in Germany in 1928, based on the earlier magnetic wire recording from Denmark.
  - magnetic tape / recording ::@:: A coil driven by an audio waveform induces a time‑varying magnetic field that aligns microscopic magnetic domains on the tape; this alignment stores the signal as a pattern of magnetization.
  - magnetic tape / playback ::@:: During playback, the moving tape passes through a read head where the changing magnetization again induces a voltage in the coil, which is amplified to recover the audio waveform.
  - magnetic tape / degradation ::@:: The stored magnetization is not at its natural (minimum‑energy) state; over time thermal agitation causes random domain flips that shift the recorded pattern. After decades of storage the tape's magnetic domains drift from their intended positions, so playback yields a distorted waveform and audible quality loss. <P> Thus, while analog tape offers compact physical storage, its fidelity degrades irreversibly with environmental noise and time.
- [digital audio](../../../../general/digital%20audio.md) ::@:: It is a representation of sound recorded in, or converted into, digital form. In digital audio, the sound wave of the audio signal is typically encoded as numerical samples in a continuous sequence.
  - digital audio / sampling rate ::@:: Human hearing tops out around 20 kHz; to satisfy the Nyquist criterion we sample at least twice this bandwidth. <p> CDs use a slightly higher rate of 44.1 kHz to give implementation margin, plus 16‑bit quantization for high‑fidelity representation.
  - digital audio / pulse-code modulation \(PCM\) ::@:: With two stereo channels, the raw data stream is 44.1 k × 16 bits × 2 ≈ 1.411 Mbps, yielding about 53 MB per five‑minute track in uncompressed WAV form. <p> Pulse‑code modulation (PCM) converts the analog waveform into a binary sequence; this digital representation is immune to gradual physical drift and can be stored as a stable file.
  - digital audio / formats ::@:: Lossless formats like WAV preserve every bit of the original PCM stream, whereas lossy codecs such as MP3 discard perceptually insignificant bits to reduce size by roughly an order of magnitude.
- [digital video](../../../../general/digital%20video.md) ::@:: It is an electronic representation of moving visual images (video) in the form of encoded digital data. This is in contrast to analog video, which represents moving visual images in the form of analog signals.
  - digital video / historical context ::@:: In the early 1990s, analog audio could be digitized into a manageable data rate; however, a two‑hour movie would require many CD‑size discs if encoded directly with PCM. <p> The missing ingredient was an efficient compression engine that exploits human visual perception (e.g., MPEG‑1 for VCD).
  - digital video / compression ::@:: Once such lossy video codecs were available in the late 1990s, entire movies fit onto a single disc or cartridge, making digital video commercially viable. Subsequent generations (DVD, Blu‑ray) introduced higher‑order MPEG variants (MPEG‑2, MPEG‑4) to further reduce bitrate while maintaining acceptable visual quality. <p> This illustrates the trade‑off: raw digitization gives robustness but enormous storage; compression reduces size at the cost of irreversibly discarding data.
- [public switched telephone network](../../../../general/public%20switched%20telephone%20network.md) \(PSTN\) ::@:: It is the aggregate of the world's telephone networks that are operated by national, regional, or local telephony operators. It provides infrastructure and services for public telephony.
  - public switched telephone network / medium ::@:: A typical PSTN call starts with a two‑wire copper "local loop" that supplies 48 V for line power and carries the voice waveform to the switching office. For intercity or international links, the signal travels over long coaxial cables (often submarine) which act as transmission lines.
    - public switched telephone network / medium / loss ::@:: In an ideal lossless line, inductors and capacitors would preserve energy; real cables contain resistive elements that cause $I^2 R$ losses and therefore attenuation of the signal. <p> Thermal noise generated in these resistances adds a constant background power that does not diminish with distance, so as the signal attenuates the signal‑to‑noise ratio (SNR) degrades. <p> A minimum acceptable SNR imposes a hard limit on how far an analog voice signal can travel without regeneration.
    - public switched telephone network / medium / regeneration ::@:: Amplifiers can boost a weak received signal, but they also amplify the accompanying thermal noise unless perfect filtering is applied—an impractical ideal. <p> Consequently, while repeaters (signal regenerators) are used in telephone networks to restore both amplitude and shape, purely linear amplification cannot overcome the fundamental SNR ceiling set by cable losses.
    - public switched telephone network / medium / digital aspects ::@:: The need for intermediate regeneration points motivates digital switching: digitizing the signal at each node restores a clean waveform without cumulative noise.
- [amplifier](../../../../general/amplifier.md) ::@:: It is an electronic device that can increase the magnitude of a signal (a time-varying voltage or current). It is a two-port electronic circuit that uses electric power from a power supply to increase the amplitude (magnitude of the voltage or current) of a signal applied to its input terminals, producing a proportionally greater amplitude signal at its output.
  - amplifier / signal-to-noise ratio ::@:: An amplifier only boosts the received voltage; it also amplifies all existing noise, so the output SNR is never higher than the input SNR (and typically lower because of the amplifier's own noise figure).
    - amplifier / signal-to-noise ratio / implications ::@:: Therefore, adding a receiver‑side amplifier cannot extend the usable link distance if the incoming SNR is already too low. The only practical way to increase range with a fixed power budget is to raise the transmitted power itself, which is limited by regulations and hardware capabilities.
- [data transmission](../../../../general/data%20transmission.md) ::@:: It is the transfer of data over a point-to-point or point-to-multipoint communication channel.
  - data transmission / analog ::@:: In an analog link any waveform distortion directly corrupts the conveyed information because the signal is continuous.
  - data transmission / digital ::@:: Digital links first perform A/D conversion (e.g., PCM), turning the waveform into a bitstream; the bits are then mapped onto a carrier such as on‑off keying. <p> Distortions that still allow correct bit decision do not affect the recovered data: after decoding and DAC, the original waveform is reconstructed up to quantization noise. <p> Quantization noise depends only on the chosen bit resolution and is independent of channel length, so it can be controlled separately from propagation loss.
- [regenerator](../../../../general/regenerator%20(telecommunications).md) ::@:: It in a telecommunications context is a type of repeater that is used in copper line or optical fibre line transmission systems. The regeneration function involved also appears in other types of systems, e.g. computer networking systems.
  - regenerator / operation ::@:: A repeater receives a distorted but still decodable signal, recovers the bits, and retransmits a freshly regenerated clean waveform.
  - regenerator / use ::@:: This decode‑and‑forward operation breaks the cumulative degradation that would otherwise limit analog links; each stage can be as long as desired provided its input is above the decoding threshold. <p> By chaining multiple repeaters one can span arbitrarily long distances while preserving data integrity, assuming adequate power and bandwidth at each node. However, the data rate remains bounded by channel bandwidth and link quality.
- [data compression](../../../../general/data%20compression.md) ::@:: It is the process of encoding information using fewer bits than the original representation. Any particular compression is either lossy or lossless.
  - data compression / communications ::@:: While repeaters solve range, the data rate remains bounded by channel bandwidth and link quality. <p> To transmit more bits within the same bandwidth, the raw PCM bitstream must be compressed (lossless or lossy); otherwise the stream would be too large for storage or transmission. <p> Compression therefore becomes an essential part of any practical digital communication system.
- time domain
- [frequency domain](../../../../general/frequency%20domain.md) ::@:: It refers to the analysis of mathematical functions or signals with respect to frequency (and possibly phase), rather than time, as in time series.
  - frequency domain / vs. time domain ::@:: While a time-domain graph shows how a signal changes over time, a frequency-domain graph shows how the signal is distributed within different frequency bands over a range of frequencies.
  - frequency domain / sinusoids ::@:: A complex valued frequency-domain representation consists of both the magnitude and the phase of a set of sinusoids (or other basis waveforms) at the frequency components of the signal.
  - frequency domain / amplitude spectrum ::@:: Treat each sinusoid as a "LEGO block" characterized by three numbers: frequency $f_i$, amplitude $a_i$, and phase $\phi_i$. <p> Plotting all $a_i$ versus their corresponding $f_i$ yields the _amplitude spectrum_; this graph is just another way to list the LEGO parameters.
  - frequency domain / phase spectrum ::@:: Treat each sinusoid as a "LEGO block" characterized by three numbers: frequency $f_i$, amplitude $a_i$, and phase $\phi_i$. <p> Similarly, plotting each $\phi_i$ against $f_i$ produces the _phase spectrum_, completing a graphical description of the signal's spectral content.
  - frequency domain / amplitude and phase spectrum ::@:: The amplitude spectrum tells how much energy is present at each frequency; the phase spectrum indicates the time shift of that component. With both graphs, one can reconstruct the original waveform via an inverse Fourier series or transform. <p> This two‑graph approach replaces a raw list of parameters with a visual tool that is easier to interpret and compare across signals.
- spectral density
  - spectral density / one-sided vs. two-sided
    - spectral density / one-sided vs. two-sided / one-sided ::@:: If the building blocks of a signal are _chosen_ to be real sinusoids, the spectrum is naturally one‑sided—only the positive side needs to be plotted.
    - spectral density / one-sided vs. two-sided / two-sided ::@:: _Choosing_ a compressed sinusoid (a complex exponential) to represent a signal forces the signal to be represented as two symmetric halves: a positive‑frequency part and its conjugate negative‑frequency counterpart.

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
- topic:

## week 2 lecture 2

- datetime: 2025-09-11T09:00:00+08:00/2025-09-11T10:20:00+08:00, PT1H20M
- topic:

## week 2 tutorial

- datetime: 2025-09-12T15:30:00+08:00/2025-09-12T16:20:00+08:00, PT50M
- topic:

## week 3 lecture

- datetime: 2025-09-16T09:00:00+08:00/2025-09-16T10:20:00+08:00, PT1H20M
- topic:

## week 3 lecture 2

- datetime: 2025-09-18T09:00:00+08:00/2025-09-18T10:20:00+08:00, PT1H20M
- topic:

## week 3 tutorial

- datetime: 2025-09-19T15:30:00+08:00/2025-09-19T16:20:00+08:00, PT50M
- topic:

## week 4 lecture

- datetime: 2025-09-23T09:00:00+08:00/2025-09-23T10:20:00+08:00, PT1H20M
- topic:

## week 4 lecture 2

- datetime: 2025-09-25T09:00:00+08:00/2025-09-25T10:20:00+08:00, PT1H20M
- topic:

## week 4 tutorial

- datetime: 2025-09-26T15:30:00+08:00/2025-09-26T16:20:00+08:00, PT50M
- topic:

## week 5 lecture

- datetime: 2025-09-30T09:00:00+08:00/2025-09-30T10:20:00+08:00, PT1H20M
- topic:

## week 5 lecture 2

- datetime: 2025-10-02T09:00:00+08:00/2025-10-02T10:20:00+08:00, PT1H20M
- topic:

## week 5 tutorial

- datetime: 2025-10-03T15:30:00+08:00/2025-10-03T16:20:00+08:00, PT50M
- topic:

## aftermath

### total

- grades: ?/100
  - statistics: ?
