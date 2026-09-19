---
aliases:
  - ELEC 2100 system
  - ELEC 2100 systems
  - ELEC2100 system
  - ELEC2100 systems
  - HKUST ELEC 2100 system
  - HKUST ELEC 2100 systems
  - HKUST ELEC2100 system
  - HKUST ELEC2100 systems
  - system
  - systems
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/system
  - language/in/English
---

# system

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

A system maps an input signal to an output signal. This input-output viewpoint connects raw signal descriptions to later transform-based analysis of linear time-invariant systems.

This note covers general systems vocabulary: what a system is, how it is modeled, what properties mean, and how engineers classify systems before choosing a solution method. The response mechanics live in companion notes: `continuous-time LTI system.md` for continuous-time response analysis, `discrete-time LTI system.md` for the sample-by-sample analogue, and `convolution.md` for zero-state response machinery.

---

Flashcards for this section are as follows:

- What is a system in ELEC 2100? ::@:: A rule or device that maps an input signal to an output signal. <!--SR:!fsrs,2027-04-23T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-05-15T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-15T00:00:00.000Z-->
- What is the central systems question in this topic? ::@:: It is how the system transforms the input signal into the output signal: whether it amplifies, filters, delays, distorts, or transforms it. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why is the systems viewpoint central in ELEC 2100? ::@:: It connects signal descriptions to later transform-based analysis of linear time-invariant systems. <!--SR:!fsrs,2027-01-26T00:00:00.000Z,194,193.65488775,3.24197837,2,7,0,0,2026-07-16T00:00:00.000Z!fsrs,2027-04-18T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-09T00:00:00.000Z-->
- How does this note relate to the companion LTI notes? ::@:: This note covers core vocabulary and classification; `continuous-time LTI system.md`, `discrete-time LTI system.md`, and `convolution.md` cover the detailed response mechanics. <!--SR:!fsrs,2027-04-23T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-04-28T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-11T00:00:00.000Z-->

## system meaning and communication context

A system is an integrated entity whose interacting components perform a stable function together. In this note, $e(t)$ denotes excitation and $r(t)$ denotes response. The central question is what the system does to the input signal: whether it amplifies, filters, delays, distorts, or transforms it.

This viewpoint comes from communication and signal-processing examples. A communication chain contains devices such as transmitters, channels, and receivers, each acting as a system on the signal it receives. Information is carried by signals and shaped by systems at every stage.

Concrete examples drive the point home. Samuel Morse's 1844 telegraph transmission _What hath God wrought!_ and Alexander Graham Bell's 1876 telephone transmission _Mr. Watson, come here, I want to see you._ show that systems are engineered mechanisms for encoding, carrying, and recovering messages. Fiber-optic links, digital microwave links, satellite communication, cable systems, and mobile communication make the same point at larger scale.

The mobile-generation timeline also motivates the systems perspective. The progression runs from 1G analog systems in the 1980s through 2G and 2.5G systems in the 1990s, 3G systems around 2000, 4G systems around 2010, and 5G systems from about 2019 onward, with 6G as the next horizon. Modern systems target high speed, wide bandwidth, high reliability, and low latency, which explains why better signal models and system-analysis tools matter in practice.

Signal theory studies the signals themselves; system theory studies how systems act on them. System analysis asks for the output produced by a given system, whereas system synthesis designs a system to achieve a desired behavior.

---

Flashcards for this section are as follows:

- What do $e(t)$ and $r(t)$ denote? ::@:: $e(t)$ denotes excitation (input), and $r(t)$ denotes response (output). <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why do communication examples belong in a systems topic? ::@:: They show information is carried by signals and shaped by systems at every stage of a transmission chain. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What historical examples make the communication-systems viewpoint concrete? ::@:: Morse's 1844 telegraph transmission and Bell's 1876 telephone transmission show that systems are engineered mechanisms for carrying messages. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What broad mobile-generation sequence is used in the introductory systems survey? ::@:: The survey moves from 1G analog systems in the 1980s through 2G, 2.5G, 3G, 4G, and 5G from about 2019 onward, with 6G as the next horizon. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What modern engineering targets are emphasized in the communication-systems survey? ::@:: High speed, wide bandwidth, high reliability, and low latency are key modern communication-system targets. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the difference between signal theory and system theory? ::@:: Signal theory studies signals themselves; system theory studies how systems act on signals. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the difference between system analysis and system synthesis? ::@:: System analysis asks for the output of a given system; system synthesis designs a system to achieve desired behavior. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## continuous-time, discrete-time, and mathematical models

A continuous-time system acts on signals such as $x(t)$ and produces outputs such as $r(t)=H[e(t)]$. A discrete-time system acts on sequences such as $x[n]$ and produces outputs such as $y[n]=H[x[n]]$. In both cases the system is an operator acting on a signal, not just a formula in one variable.

Continuous-time systems are often modeled by differential equations. Discrete-time systems are often modeled by difference equations. Block diagrams and signal-flow diagrams show how elementary operations are interconnected.

Once a mathematical model is written, one can compute the response under given excitation and initial conditions, and later interpret that response physically.

---

Flashcards for this section are as follows:

- What is a continuous-time system in operator form? ::@:: A system acting on signals such as $e(t)$, giving outputs such as $r(t)=H[e(t)]$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is a discrete-time system in operator form? ::@:: A system acting on sequences such as $x[n]$, giving outputs such as $y[n]=H[x[n]]$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What are the standard mathematical models for continuous-time and discrete-time systems? ::@:: Differential equations for continuous-time, difference equations for discrete-time. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why are mathematical models central to system analysis? ::@:: They let us compute responses under given excitation and initial conditions, and then interpret those responses physically. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What do block diagrams contribute beyond equations? ::@:: They show the structural interconnection of elementary operations inside the system. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## memoryless, dynamic, lumped, and distributed systems

The first classification separates two questions that beginners often mix together. Memoryless versus dynamic asks whether the output at one instant depends only on the input at that same instant or also on values from other times. Lumped versus distributed asks whether the model depends only on time or on both time and space.

Test properties one at a time. The checklist: Does the rule use only the present value? Does it ask for future input? Does it preserve superposition? Does a shift at the input become the same shift at the output? Does bounded input stay bounded? Can the input be uniquely recovered?

---

Flashcards for this section are as follows:

- What are the two different classification axes introduced here? ::@:: Memoryless versus dynamic asks whether other times matter to the output, and lumped versus distributed asks whether the model depends only on time or also on spatial coordinates. <!--SR:!fsrs,2027-05-10T00:00:00.000Z,300,300.01984473,1,2,7,0,0,2026-07-14T00:00:00.000Z!fsrs,2027-04-23T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-10T00:00:00.000Z-->
- What checklist makes system-property testing safer? ::@:: Test one property question at a time: present-only dependence for memorylessness, future-input dependence for causality, superposition for linearity, shift-commutation for time invariance, bounded-input behavior for stability, and one-to-one recovery for invertibility. <!--SR:!fsrs,2027-04-07T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-07T00:00:00.000Z!fsrs,2027-06-06T00:00:00.000Z,321,321.346657,1,2,7,0,0,2026-07-20T00:00:00.000Z-->

### memorylessness

A system is memoryless if the output at time $t_0$ depends only on the input at $t_0$. Memorylessness excludes both past and future dependence. A dynamic system is any counterexample: its output at $t_0$ also depends on input values from other times. In a general linear kernel $y(t)=\int_{-\infty}^{\infty} h(t,\tau)x(\tau)\,d\tau$, memorylessness means $h(t,\tau)=a(t)\delta(t-\tau)$. In the LTI case this becomes $h(t)=K\delta(t)$.

A clean memoryless example is $y(t)=3x(t)$. The system simply scales the present input. The impulse-response form is $h(t)=3\delta(t)$, so $y=x*h$. Because the impulse response is concentrated entirely at zero delay, one input instant affects only the same output instant.

A clean counterexample is the causal averaging system $y(t)=\int_{-\infty}^{t} e^{-(t-\tau)}x(\tau)\,d\tau$. Its impulse response is $h(t)=e^{-t}u(t)$. One impulse at time $0$ creates an exponentially decaying tail for all later times, so past input values keep influencing the present output. That spreading over time is exactly what memory means.

Memoryless systems look only at the present sample; dynamic systems smear one input event across a time interval. A resistor is the basic memoryless intuition, while capacitors, inductors, and low-pass filters are the basic dynamic intuition.

Representative rules make the distinction concrete. The affine-delay rule $y(t)=2x(t-1)+1$, the even-part operator $\tfrac12\bigl(x(t)+x(-t)\bigr)$, the comparator $y[n]=\max\{x[n],x[n-1]\}$, and the scaled-index rule $y[n]=n\,x[2n]$ are all non-memoryless because they need a value other than the present sample. By contrast, $y(t)=\cos(x(t))$ is memoryless: it is nonlinear, but it still acts pointwise on the present sample only.

---

Flashcards for this section are as follows:

- What does memorylessness mean? ::@:: The output at time $t_0$ depends only on the input at time $t_0$; any system whose output also depends on other times is dynamic. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the kernel test for memorylessness? ::@:: In a linear kernel form $y(t)=\int h(t,\tau)x(\tau)\,d\tau$, memorylessness means $h(t,\tau)=a(t)\delta(t-\tau)$, and in the LTI case $h(t)=K\delta(t)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the memoryless example? ::@:: $y(t)=3x(t)$ with $h(t)=3\delta(t)$; the response is concentrated at zero delay. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the dynamic counterexample? ::@:: $y(t)=\int_{-\infty}^{t} e^{-(t-\tau)}x(\tau)\,d\tau$ with $h(t)=e^{-t}u(t)$; past input values keep affecting the present output. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Which examples are non-memoryless? ::@:: $y(t)=2x(t-1)+1$ uses a past sample, $\tfrac12(x(t)+x(-t))$ uses a reflected future sample, $\max\{x[n],x[n-1]\}$ compares with a past sample, and $n\,x[2n]$ uses a different index. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why is $y(t)=\cos(x(t))$ still memoryless? ::@:: It applies a pointwise map to the present sample only, even though the operation is nonlinear. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

### lumped and distributed viewpoints

The lecture also distinguishes lumped-parameter and distributed-parameter systems. A lumped system depends only on time and is typically modeled by ordinary differential equations; low-frequency RLC circuits are the standard example. A distributed system depends on time and space and is modeled by partial differential equations; transmission lines and waveguides are typical examples.

This classification is independent of memorylessness. A system can be lumped yet dynamic, because ordinary differential equations still describe time evolution with memory. The lumped/distributed split asks whether the state is concentrated into time-dependent variables or spread across both time and space.

---

Flashcards for this section are as follows:

- What is the lumped-versus-distributed distinction? ::@:: Lumped systems depend only on time and use ordinary differential equations; distributed systems depend on both time and space and use partial differential equations. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What are standard examples of lumped and distributed systems? ::@:: A low-frequency RLC circuit is lumped; a transmission line or waveguide is distributed. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## invertibility, linearity, and time invariance

A second cluster of classifications asks three questions. Invertibility asks whether the input can be recovered from the output. Linearity asks whether superposition holds. Time invariance asks whether a shift of the input produces the same shift of the output.

---

Flashcards for this section are as follows:

- How do invertibility, linearity, and time invariance differ? ::@:: Invertibility asks whether the input can be recovered, linearity asks whether add-and-scale operations commute with the system, and time invariance asks whether absolute clock time matters. <!--SR:!fsrs,2027-05-16T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-16T00:00:00.000Z!fsrs,2027-05-27T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-18T00:00:00.000Z-->

### invertibility

A system is invertible if different inputs produce different outputs, so an inverse system can recover the original input from the response. A system is non-invertible if different inputs collapse to the same output, making unique recovery impossible.

The comparison examples show several distinct failure modes. The affine-delay rule $y(t)=2x(t-1)+1$ is invertible because one can recover $x(t)=\frac{y(t+1)-1}{2}$. By contrast, $y(t)=\cos(x(t))$ is not invertible because many different inputs share the same cosine value, the even-part operator is not invertible because it discards the odd component, the comparator $\max\{x[n],x[n-1]\}$ is not invertible because different sequences can share the same maxima, and $y[n]=n\,x[2n]$ is not invertible because odd-index samples are discarded and the factor $n$ destroys information at $n=0$.

---

Flashcards for this section are as follows:

- What is invertibility? ::@:: A system is invertible if different inputs produce different outputs, so an inverse system can recover the input; it is non-invertible when different inputs collapse to the same output. <!--SR:!fsrs,2027-04-18T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-09T00:00:00.000Z!fsrs,2027-04-23T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-10T00:00:00.000Z-->
- What does non-invertible mean? ::@:: A system is non-invertible when different inputs collapse to the same output, so unique recovery is impossible. <!--SR:!fsrs,2027-04-28T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-11T00:00:00.000Z!fsrs,2027-05-22T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-17T00:00:00.000Z-->
- Which examples are invertible or non-invertible? ::@:: $y(t)=2x(t-1)+1$ is invertible via $x(t)=\frac{y(t+1)-1}{2}$; $\cos(x(t))$, the even-part operator, $\max\{x[n],x[n-1]\}$, and $n\,x[2n]$ are non-invertible. <!--SR:!fsrs,2027-06-06T00:00:00.000Z,321,321.346657,1,2,7,0,0,2026-07-20T00:00:00.000Z!fsrs,2027-04-23T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-10T00:00:00.000Z-->

### linearity

Linearity requires homogeneity and superposition. If $x_1$ produces $y_1$ and $x_2$ produces $y_2$, then a linear system must send $c_1x_1+c_2x_2$ to $c_1y_1+c_2y_2$. In operator form, $H[c_1x_1(t)+c_2x_2(t)]=c_1H[x_1(t)]+c_2H[x_2(t)]$. The practical test is "combine first, then pass through the system" versus "pass through the system first, then combine the outputs".

A clean linear example is $y(t)=2x(t)-x(t-1)$. In impulse-response form this is $h(t)=2\delta(t)-\delta(t-1)$, so $y=x*h$. The same fixed weighting of present and delayed inputs applies regardless of amplitudes or signal combinations, so superposition holds automatically.

A standard counterexample is $y(t)=x^2(t)$. Squaring is nonlinear. There is no single first-order impulse-response representation $y(t)=\int h(t,\tau)x(\tau)\,d\tau$, because every such representation is linear in $x$. The closest kernel viewpoint is higher-order: $y(t)=\iint \delta(t-\tau_1)\delta(t-\tau_2)x(\tau_1)x(\tau_2)\,d\tau_1d\tau_2$. The square creates cross terms, so the response to a sum is not the sum of the responses.

The intuition is that linear systems preserve add-and-scale structure. Double the input, the output doubles; add two inputs, the output is the sum. Nonlinear systems distort that bookkeeping, usually by creating mixing terms, clipping, saturation, or amplitude-dependent gain.

The comparison examples separate structure from surface appearance. The affine-delay rule $y(t)=2x(t-1)+1$ is not linear because the constant offset breaks homogeneity. The pointwise cosine rule and the max rule are nonlinear because they do not preserve superposition. By contrast, the even-part operator and the scaled-index rule $y[n]=n\,x[2n]$ are linear: averaging, fixed scaling, and reindexing preserve add-and-scale behavior even though other properties may fail.

---

Flashcards for this section are as follows:

- What is linearity? ::@:: A system is linear if $H[c_1x_1+c_2x_2]=c_1H[x_1]+c_2H[x_2]$ for arbitrary signals and constants. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the linear example? ::@:: $y(t)=2x(t)-x(t-1)$ with $h(t)=2\delta(t)-\delta(t-1)$; superposition holds. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the nonlinear counterexample? ::@:: $y(t)=x^2(t)$. No single first-order impulse response exists because any such representation is already linear. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Which examples fail superposition or homogeneity? ::@:: $y(t)=2x(t-1)+1$ fails homogeneity due to the constant offset, $y(t)=\cos(x(t))$ fails superposition due to pointwise nonlinearity, and $\max\{x[n],x[n-1]\}$ fails because maximum of sums does not equal sum of maxima. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Which examples are linear despite other failures? ::@:: $\tfrac12(x(t)+x(-t))$ (even-part operator) and $n\,x[2n]$ (scaled-index rule) are linear because averaging, fixed scaling, and reindexing still preserve superposition even though other system properties fail. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

### time invariance

A system is time invariant if, under the same initial-condition convention, its output is independent of the absolute time at which the input is applied. Equivalently, delaying the input merely delays the output by the same amount. In operator form, if $H[x(t)]=y(t)$, then time invariance requires $H[x(t-t_0)]=y(t-t_0)$. For a general linear kernel this means $h(t,\tau)=h(t-\tau)$.

A standard time-invariant example is $y(t)=x(t)-x(t-1)$. Its impulse response is $h(t)=\delta(t)-\delta(t-1)$. The system always forms the same present-minus-one-second-ago combination, no matter when the signal arrives, so shifting the input simply shifts the output.

A standard time-varying counterexample is $y(t)=\cos(\omega_0 t)x(t)$. In kernel form this is $h(t,\tau)=\cos(\omega_0 t)\delta(t-\tau)$. The factor $\cos(\omega_0 t)$ depends on absolute time, so the system law itself changes with the clock. Shifting the input first gives $\cos(\omega_0 t)x(t-t_0)$, while shifting the original output gives $\cos(\omega_0(t-t_0))x(t-t_0)$, and these are not equal in general.

The intuition is that a time-invariant system has no hidden calendar or clock. The same waveform meeting the same system tomorrow should produce the same output shape, just shifted. A time-varying system behaves as if its coefficients change with time.

The comparison examples produce contrasts. The affine-delay rule, the pointwise cosine rule, and the max rule are time invariant because shifting the input shifts exactly the same algebraic rule. The even-part operator is not time invariant because reflection is pinned to the origin, and $y[n]=n\,x[2n]$ is not time invariant because both the explicit factor $n$ and the index scaling refer to absolute sample location.

---

Flashcards for this section are as follows:

- What is time invariance? ::@:: If $H[x(t)]=y(t)$, then time invariance requires $H[x(t-t_0)]=y(t-t_0)$, so delaying the input merely delays the output by the same amount. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the intuition behind time invariance? ::@:: Time invariant means "same rule at every clock time"; time varying means the system itself changes while the signal is passing through it. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the kernel test for time invariance? ::@:: In a linear kernel description, time invariance means the kernel depends only on the difference $t-\tau$, so it can be written as $h(t-\tau)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the time-invariant example? ::@:: $y(t)=x(t)-x(t-1)$ with $h(t)=\delta(t)-\delta(t-1)$; shifting the input just shifts the output. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the time-varying counterexample? ::@:: $y(t)=\cos(\omega_0 t)x(t)$ with $h(t,\tau)=\cos(\omega_0 t)\delta(t-\tau)$; the coefficient depends on absolute time, so the shift test fails. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Which examples are time invariant? ::@:: $y(t)=2x(t-1)+1$ (affine delay), $y(t)=\cos(x(t))$ (pointwise cosine), and $\max\{x[n],x[n-1]\}$ (windowed maximum). <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Which examples are time varying? ::@:: The even-part operator $\tfrac12(x(t)+x(-t))$ because reflection is pinned to the origin, and $n\,x[2n]$ because the factor $n$ and index scaling refer to absolute sample location. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## causality and stability

A third cluster of properties asks whether the system can run in real time and whether it keeps bounded signals under control. Causality is the no-future-dependence property. Boundedness here means bounded-input bounded-output stability.

---

Flashcards for this section are as follows:

- What do causality and boundedness ask? ::@:: Causality asks whether future input is needed; boundedness asks whether bounded input always produces bounded output. <!--SR:!fsrs,2027-04-28T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-11T00:00:00.000Z!fsrs,2027-05-05T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-13T00:00:00.000Z-->

### causality

A causal system does not depend on future input values. This matters because a physically realizable real-time system cannot react before its input arrives. In a general linear kernel $y(t)=\int h(t,\tau)x(\tau)\,d\tau$, causality means $h(t,\tau)=0$ whenever $\tau>t$. In the LTI case, that becomes $h(t)=0$ for $t<0$.

A standard causal example is $y(t)=x(t)+x(t-2)$. Its impulse response is $h(t)=\delta(t)+\delta(t-2)$. The system uses the present value and a past value only, so it can be implemented in real time.

A standard noncausal counterexample is $y(t)=x(t+2)$. Its impulse response is $h(t)=\delta(t+2)$. The support at negative time means the output at time $t$ depends on an input value two seconds in the future, violating real-time causality.

The key idea is support geometry. If the impulse response reaches only zero delay and positive delays, the system is causal. If any part reaches into negative delay, the system asks for future information. Noncausal systems can still be useful offline, because stored data make the "future" available after the fact.

The comparison examples are useful here as well. The affine-delay rule, the pointwise cosine rule, and the max rule are causal because they use only present or past samples. The even-part operator is noncausal because $x(-t_0)$ can lie in the future relative to $t_0$, and $y[n]=n\,x[2n]$ is generally noncausal because for positive $n$ it asks for a future sample at index $2n$.

---

Flashcards for this section are as follows:

- What is causality? ::@:: A system is causal if the output at time $t$ depends only on input values at times $\tau\le t$ and never on future values. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the intuition behind causality? ::@:: Causal means the system can react only after information arrives; noncausal means some part of the rule reaches into the future. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the impulse-response test for causality? ::@:: In a linear kernel description, causality means $h(t,\tau)=0$ for $\tau>t$; for an LTI system this becomes $h(t)=0$ for negative time. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the causal example? ::@:: $y(t)=x(t)+x(t-2)$ with $h(t)=\delta(t)+\delta(t-2)$; uses only present and past input values. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the noncausal counterexample? ::@:: $y(t)=x(t+2)$ with $h(t)=\delta(t+2)$; negative-time support means the output depends on future input. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Which examples are causal? ::@:: $y(t)=2x(t-1)+1$ (affine delay), $y(t)=\cos(x(t))$ (pointwise cosine), and $\max\{x[n],x[n-1]\}$ (windowed maximum) are causal because they use only present or past samples. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Which examples are noncausal? ::@:: The even-part operator $\tfrac12(x(t)+x(-t))$ because $x(-t_0)$ can lie in the future, and $n\,x[2n]$ because for positive $n$ it asks for a future sample. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

### boundedness (BIBO stability)

Bounded-input bounded-output stability means: if the input is bounded in magnitude (there exists a finite $M_x$ with $|x(t)|\le M_x$ for all $t$ or $|x[n]|\le M_x$ for all $n$), then the output is also bounded in magnitude (there exists a finite $M_y$ with $|y(t)|\le M_y$ for all $t$ or $|y[n]|\le M_y$ for all $n$). The output bound may depend on the input, but it must stay finite whenever the input stays finite. For LTI systems the impulse-response test is absolute integrability: if $\int_{-\infty}^{\infty}|h(t)|\,dt<\infty$, then bounded inputs stay bounded.

A standard stable example is $y(t)=\int_{-\infty}^{t} e^{-(t-\tau)}x(\tau)\,d\tau$. Its impulse response is $h(t)=e^{-t}u(t)$. Since $\int_{-\infty}^{\infty}|h(t)|\,dt=1$, any bounded input $|x(t)|\le M$ produces $|y(t)|\le M\int |h(t)|dt=M$. The system has finite total memory weight, so it cannot amplify a bounded input into an unbounded output.

A standard unstable counterexample is the integrator $y(t)=\int_{-\infty}^{t}x(\tau)\,d\tau$, whose impulse response is $h(t)=u(t)$. The input $x(t)=u(t)$ is bounded by $1$, yet the output is $y(t)=tu(t)$, which grows without bound. The problem is that $h(t)$ has infinite area, so the system can keep accumulating bounded input forever.

The intuition is that boundedness asks whether the system maps every finite-amplitude box of admissible inputs into some finite-amplitude box of outputs. The output bound does not need to equal the input bound, but it must exist. For LTI systems this becomes a total-memory-weight question: a decaying impulse response forgets enough of the past to keep the output under control, whereas an integrator never lets go of past input.

The comparison examples add several quick recognition patterns, including non-LTI ones. The affine-delay rule, the pointwise cosine rule, the even-part operator, and the max rule are all BIBO stable because bounded inputs stay bounded under those operations. The nonlinear memoryless rule $y[n]=e^{x[n]}$ is also BIBO stable: if $|x[n]|\le M$, then $-M\le x[n]\le M$, so $e^{-M}\le y[n]\le e^{M}$. By contrast, the time-varying rule $y[n]=(n+1)x[n]$ is not BIBO stable, because the bounded input $x[n]\equiv 1$ produces the unbounded sequence $y[n]=n+1$. The integrator is likewise not BIBO stable for the same accumulation reason.

---

Flashcards for this section are as follows:

- What is BIBO stability? ::@:: A system is BIBO stable if every bounded input produces a bounded output: whenever $|x(t)|\le M_x$ for all $t$ or $|x[n]|\le M_x$ for all $n$, there exists a finite $M_y$ with $|y(t)|\le M_y$ or $|y[n]|\le M_y$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the LTI impulse-response test for BIBO stability? ::@:: Absolute integrability: if $\int_{-\infty}^{\infty}|h(t)|\,dt<\infty$, then bounded inputs stay bounded. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the stable example? ::@:: $y(t)=\int_{-\infty}^{t} e^{-(t-\tau)}x(\tau)\,d\tau$ with $h(t)=e^{-t}u(t)$; its total impulse-response area is finite. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the unstable counterexample? ::@:: The integrator $y(t)=\int_{-\infty}^{t}x(\tau)\,d\tau$ with $h(t)=u(t)$; the bounded input $x(t)=u(t)$ produces the unbounded ramp $y(t)=tu(t)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the intuition behind BIBO stability? ::@:: Every finite-amplitude input box maps into some finite-amplitude output box; the output bound may change with the input but must remain finite. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the nonlinear stable example? ::@:: $y[n]=e^{x[n]}$ is BIBO stable because $|x[n]|\le M$ implies $e^{-M}\le y[n]\le e^{M}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the time-varying unstable example? ::@:: $y[n]=(n+1)x[n]$ is not BIBO stable because the bounded input $x[n]\equiv 1$ gives $y[n]=n+1$, which is unbounded. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## linear time-invariant systems and response transfer

Linear time-invariant systems are the main class in the course because their structure lets one transfer known responses to new inputs systematically. If an LTI system in zero state sends $x_1(t)$ to $y_1(t)$, then shifted and linearly combined versions of $x_1$ produce the corresponding shifted and linearly combined versions of $y_1$.

This structural cleanliness explains why differentiation, integration, convolution, and transform methods work well for LTIs. Under matching zero-state assumptions, one may often move these operations through the system instead of recomputing the response from scratch. The detailed worked examples belong in `continuous-time LTI system.md` and `convolution.md`; this section keeps only the high-level transfer principle.

---

Flashcards for this section are as follows:

- Why are LTI systems central in the course? ::@:: Because known responses can be transferred systematically to shifted and linearly combined inputs. <!--SR:!fsrs,2027-04-12T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-08T00:00:00.000Z!fsrs,2027-05-05T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-13T00:00:00.000Z-->
- What is the response-transfer principle? ::@:: If an LTI system maps $x_1$ to $y_1$, then shifted and linearly combined versions of $x_1$ map to the corresponding shifted and linearly combined versions of $y_1$. <!--SR:!fsrs,2027-05-21T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-16T00:00:00.000Z!fsrs,2027-04-07T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-07T00:00:00.000Z-->
- What broad operator behaviors make LTI systems especially tractable? ::@:: Linearity and time invariance let known responses be shifted and recombined systematically, and under zero-state assumptions they also let differentiation, integration, convolution, and transform methods interact cleanly with the system. <!--SR:!fsrs,2027-05-26T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-17T00:00:00.000Z!fsrs,2027-05-15T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-15T00:00:00.000Z-->
- Where should the detailed worked response-transfer examples for LTIs be studied? ::@:: Use `continuous-time LTI system.md` and `convolution.md` for the detailed examples; this note keeps only the high-level transfer principle. <!--SR:!fsrs,2027-05-05T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-13T00:00:00.000Z!fsrs,2027-04-28T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-11T00:00:00.000Z-->

## representation methods for linear time-invariant systems

This part asks a practical question: how does one obtain the response of a signal passing through an LTI system? Several representations are useful rather than one universal method. For continuous-time systems, one may use differential equations derived from physical laws, system functions obtained through Laplace transformation, unit impulse responses, or structural descriptions such as block diagrams. These are different views of the same underlying system.

The continuous-time circuit example is an RLC network driven by an excitation $e(t)$, with the capacitor voltage $v_C(t)$ taken as the output and the inductor current $i_L(t)$ treated as an internal variable. This setup matters because it cleanly separates the quantity we want to observe from the internal quantity that we later eliminate. The constitutive relations are not just formulas to memorize; they encode physical storage behavior. For the capacitor, $i_C(t)=C\frac{dv_C(t)}{dt}$ says that current is proportional to how fast the capacitor voltage changes, so a capacitor resists sudden voltage changes. For the inductor, $v_L(t)=L\frac{di_L(t)}{dt}$ says that voltage is proportional to how fast the inductor current changes, so an inductor resists sudden current changes.

Using the stated reference directions, the network equations become the KVL relation $e(t)=L\frac{di_L(t)}{dt}+v_C(t)$ and the node equation $i_L(t)=\frac{v_C(t)}{R}+C\frac{dv_C(t)}{dt}$. A two-step elimination problem organizes the derivation. First rewrite the model as two coupled first-order equations: $\frac{di_L(t)}{dt}=\frac{e(t)-v_C(t)}{L}$ and $\frac{dv_C(t)}{dt}=\frac{i_L(t)}{C}-\frac{v_C(t)}{RC}$. Then eliminate the internal current $i_L(t)$ by differentiating the second equation and substituting into the first. This yields $LC\frac{d^2v_C(t)}{dt^2}+\frac{L}{R}\frac{dv_C(t)}{dt}+v_C(t)=e(t)$, or equivalently $\frac{d^2v_C(t)}{dt^2}+\frac{1}{RC}\frac{dv_C(t)}{dt}+\frac{1}{LC}v_C(t)=\frac{1}{LC}e(t)$.

The final equation should then be interpreted, not merely written down. It is linear because no nonlinear products of state variables or inputs appear. It is time invariant because all coefficients are constants. It is second order because the highest derivative is second order. This is why the example is useful pedagogically: it shows how physical laws, topology, elimination, and structural interpretation all connect.

Block diagrams provide a second continuous-time representation. The main elementary blocks are adders, multipliers, scalar multipliers, differentiators, integrators, and time-delay elements. In this course, many single-input single-output operations are drawn with the same rectangular-block style and are distinguished by the label inside the block. An adder is usually drawn as a summing node such as a small circle or a block marked with $\Sigma$; incoming branches may be marked with plus or minus signs to show whether a signal is added or subtracted, and the explicit algebra is $r(t)=e_1(t)+e_2(t)$ or $r(t)=e_1(t)-e_2(t)$. A multiplier is usually drawn as a block or node marked by $\times$ or another product label, and its explicit algebra is $r(t)=e_1(t)e_2(t)$, which is why it is generally nonlinear.

A scalar multiplier is the same operation as a gain element. A __gain block__ is the dedicated rectangular block whose inside label is the gain value, for example a block marked $a$ meaning $r(t)=ae(t)$. A __branch coefficient__ means the same gain is written directly on the signal line rather than inside a separate block, again meaning $r(t)=ae(t)$. A __triangle-style gain symbol__ is an amplifier-like triangle carrying the gain label; it still means $r(t)=ae(t)$. These are three drawing conventions for the same scalar-multiplication operation, not three different system elements. In this course, the same box-style drawing is reused for many other unary operations: a differentiator is drawn as a block labeled $\frac{d}{dt}$ with explicit relation $r(t)=\frac{d}{dt}e(t)$, an integrator as a block labeled $\int$ with relation $r(t)=\int_{-\infty}^{t}e(\tau)\,d\tau$, and a time-delay element as a block labeled by the delay $\tau$ or by an expression such as $e(t-\tau)$, meaning $r(t)=e(t-\tau)$. By contrast, common pointwise combination operations such as addition, subtraction, and multiplication are usually shown as small circular nodes with the relevant symbol inside.

The discrete-time analogue uses difference equations and block diagrams built from scalar multipliers, adders, and unit-delay elements $z^{-1}$. The scalar multiplier again has multiple acceptable drawing styles: a gain block with coefficient $a$, a branch coefficient written on the sequence line, or a triangle-style gain symbol. In every case the explicit algebra is $y[n]=ax[n]$. The unit-delay element is drawn as a block labeled $z^{-1}$ because, in the z-transform domain, delaying a sequence by one sample corresponds to multiplication by $z^{-1}$. Its explicit time-domain relation is $y[n]=x[n-1]$. Operationally, it behaves like a shift register: it outputs the previous sample while the new sample is shifted in.

Labeling conventions also matter. External input and output signals should normally be labeled explicitly by text such as $x(t)$, $r(t)$, $x[n]$, or $y[n]$ so the role of each arrow is unambiguous. Internal branch labels are helpful when a derivation needs them, but they are optional when the structure is already clear from context. If several block diagrams implement the same equation, they are all valid realizations; in practice, the simpler realization is usually preferred because it is easier to read and often uses fewer memory elements or fewer arithmetic operations.

The feedforward discrete-time example without feedback is a relation such as $y[n]=\frac{1}{2}x[n]+\frac{1}{2}x[n-1]$. To draw it, split the input into two branches, send one branch directly to an adder, send the other branch through one unit-delay block and a scalar multiplier, and then add the two branches. Because no past output is fed back, the structure is feedforward.

The comparison between backward and forward first-order difference equations is also important. A backward form such as $y[n]=x[n]+ay[n-1]$ is drawn with a feedback branch containing one delay element, because the present output depends on the previous output. The truly equivalent forward form is $y[n+1]=x[n+1]+ay[n]$. It is not a different system; it is the same recursion written one time step later, obtained by replacing $n$ with $n+1$ in the backward form. So the two forms are mathematically equivalent, but the backward form is preferred for implementation because it computes the present output $y[n]$ directly from quantities available at time $n$, whereas the forward form is phrased as the computation of the next output $y[n+1]$.

For a second-order system such as $y[n]=x[n]-3x[n-2]+5y[n-1]-6y[n-2]$, one may draw multiple structurally different but equivalent diagrams. At least two delay elements are required, because the system depends on values two samples into the past. This is also reflected in the general linear difference-equation form $\sum_{k=0}^{N}a_k y[n-k]=\sum_{r=0}^{M}b_r x[n-r]$, whose order is the difference between the highest and lowest argument values of the dependent variable.

The general linear difference-equation form is

$\sum_{k=0}^{N}a_k y[n-k]=\sum_{r=0}^{M}b_r x[n-r]$.

The order of the difference equation is the difference between the highest and lowest argument values of the dependent variable appearing in the equation. This matches the practical memory requirement: the larger the spread in delayed output indices, the more memory elements are needed in implementation.

---

Flashcards for this section are as follows:

- What are the main ways to represent an LTI system? ::@:: Differential equations, system functions via Laplace transformation, unit impulse responses, and block diagrams. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- In an RLC circuit where the source $e(t)$ feeds an inductor $L$ in series, the output is the capacitor voltage $v_C(t)$, and a resistor $R$ and capacitor $C$ are in parallel from that node to reference, what do the constitutive relations encode and what are the topology equations? ::@:: $i_C(t)=C\frac{dv_C(t)}{dt}$ means the capacitor resists sudden voltage change; $v_L(t)=L\frac{di_L(t)}{dt}$ means the inductor resists sudden current change; the topology equations are $e(t)=L\frac{di_L(t)}{dt}+v_C(t)$ and $i_L(t)=\frac{v_C(t)}{R}+C\frac{dv_C(t)}{dt}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What equation results after eliminating $i_L(t)$ from the RLC equations, and what does it tell you structurally? ::@:: $LC\frac{d^2v_C(t)}{dt^2}+\frac{L}{R}\frac{dv_C(t)}{dt}+v_C(t)=e(t)$, equivalently $\frac{d^2v_C(t)}{dt^2}+\frac{1}{RC}\frac{dv_C(t)}{dt}+\frac{1}{LC}v_C(t)=\frac{1}{LC}e(t)$; the system is linear, time invariant, and second order. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How are continuous-time block-diagram elements drawn? ::@:: An adder is a summing node ($r=e_1\pm e_2$); a multiplier is a $\times$ block ($r=e_1 e_2$); a scalar multiplier ($r=ae$) may be drawn as a gain block, branch coefficient, or triangle; differentiator ($r=\frac{d}{dt}e$), integrator ($r=\int_{-\infty}^{t}e(\tau)d\tau$), and delay ($r=e(t-\tau)$) are labeled blocks. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How are discrete-time block-diagram elements drawn? ::@:: A scalar multiplier is $y[n]=ax[n]$; the delay $y[n]=x[n-1]$ is labeled $z^{-1}$ because one-sample delay corresponds to $z^{-1}$ in the z-transform domain. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How are unary operations drawn compared with pointwise combination operations? ::@:: Unary operations (gain, delay, differentiation, integration) use labeled rectangular blocks; pointwise operations (addition, subtraction, multiplication) use small circular nodes. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What labels should definitely appear on a block diagram? ::@:: External input and output arrows should be labeled explicitly (e.g., $x[n]$ and $y[n]$); internal branch labels are optional when the structure is clear. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How is the feedforward example $y[n]=\frac{1}{2}x[n]+\frac{1}{2}x[n-1]$ drawn? ::@:: Split the input into two branches, send one directly to an adder, send the other through a delay and scalar multiplier, then add the branches; it is feedforward because the output depends only on present and delayed inputs. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How are $y[n]=x[n]+ay[n-1]$ and $y[n+1]=x[n+1]+ay[n]$ related? ::@:: They are the same recursion written one time step apart; replacing $n$ by $n+1$ in the backward form gives the forward form. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why is the backward form preferred for implementation? ::@:: It computes the present output directly from the present input and the previously stored output, so it is already in causal real-time form. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What does the second-order example teach about realization and order? ::@:: Multiple equivalent diagrams are possible, but at least two delay elements are required; more generally, the order of $\sum_{k=0}^{N}a_k y[n-k]=\sum_{r=0}^{M}b_r x[n-r]$ is determined by the spread of delayed output indices. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- If several block diagrams implement the same equation, which is best? ::@:: The simpler one, because it is easier to read and often uses fewer memory elements or arithmetic operations. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## system analysis viewpoints

The main analysis workflow is: build a mathematical model of the system, then analyze the response under a given input.

Two major model-building viewpoints are presented. The input-output description focuses only on the relationship between excitation and response and ignores internal system variables. It is especially natural for SISO systems, meaning single-input single-output systems: there is one input channel and one output channel, so one higher-order differential or difference equation can often relate them directly. The state-variable viewpoint tracks both the overall response and internal variables such as capacitor voltages or inductor currents. It is naturally suited to MIMO systems, meaning multiple-input multiple-output systems: there may be several input channels, several output channels, and several coupled internal variables, so one usually writes a set of coupled first-order equations instead of one single scalar equation.

The lecture also contrasts time-domain and transform-domain solution methods. Time-domain analysis includes direct solution of differential equations, difference equations, and convolution integrals or sums. Transform-domain analysis introduces Fourier, Laplace, and z-transform viewpoints because they convert many system calculations into simpler algebraic forms.

The overall trajectory of the course follows these transitions repeatedly: from input-output description toward state-variable description, from time-domain analysis toward transform-domain analysis, and from continuous systems toward discrete systems. Throughout, the engineering preference is for systems that are linear, time invariant, causal, and stable.

---

Flashcards for this section are as follows:

- What are the two high-level tasks in system analysis? ::@:: Build a mathematical model of the system and then analyze the output response under a given input. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the input-output description viewpoint? ::@:: It focuses only on the relationship between excitation and response and ignores internal system variables. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why is the input-output viewpoint natural for SISO systems? ::@:: Because one nth-order differential or difference equation can often relate the single input and single output directly. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the state-variable viewpoint? ::@:: It tracks both the overall response and internal variables such as capacitor voltages or inductor currents. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why is the state-variable viewpoint useful for MIMO systems? ::@:: Because it naturally represents multiple interacting inputs, outputs, and internal variables through coupled first-order equations. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What do SISO and MIMO mean? ::@:: SISO means single-input single-output; MIMO means multiple-input multiple-output. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What belongs to time-domain analysis? ::@:: Direct solution of differential equations, difference equations, and convolution integrals or sums. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why are transform-domain methods introduced? ::@:: They convert many system calculations into simpler algebraic forms. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What transforms are highlighted? ::@:: Fourier, Laplace, and z-transform. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What overall transitions organize the course? ::@:: Input-output to state-variable description, time-domain to transform-domain analysis, and continuous systems to discrete systems. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What combination of system properties is preferred? ::@:: Linear, time-invariant, causal, and stable. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## time-domain analysis methods and differential-equation viewpoint

The time-domain treatment re-enters the systems topic from a more operational angle: once a model has been written, how does one actually obtain the response? The lecture first contrasts two time-domain modelling viewpoints. The __input-output description__ writes one higher-order differential or difference equation relating excitation and response directly. The __state-variable description__ writes several coupled first-order equations that also track internal variables. This note keeps that comparison at the roadmap level, while the companion LTI notes carry the detailed continuous-time and discrete-time calculations.

The reason the course still studies time-domain methods before leaning on transforms is conceptual rather than nostalgic. Direct solution keeps the role of initial conditions visible, preserves the physical meaning of stored energy, and makes later transform methods easier to interpret. The calculation may be longer, but the modeling logic is transparent.

At the roadmap level, the key split is the same in both continuous time and discrete time. The classical solver writes the response as homogeneous plus particular. The engineering viewpoint writes the same response as zero-input plus zero-state. Those decompositions are not rivals: homogeneous/particular tells you how to solve the equation, whereas zero-input/zero-state tells you what physically caused the response. In both settings, the zero-state part is the natural target of convolution, while the zero-input part is the natural target of initial-condition reasoning.

The durable organization of the course is therefore:

- use `system.md` for the language of properties, modelling viewpoints, and classification;
- use `continuous-time LTI system.md` for differential-equation response logic, impulse response, step response, and continuous-time causality/stability tests;
- use `discrete-time LTI system.md` for recursion logic, geometric impulse responses, and discrete-time causality/stability tests;
- use `convolution.md` when the zero-state response should be assembled directly from the impulse response.

---

Flashcards for this section are as follows:

- What is the difference between the input-output and state-variable viewpoints? ::@:: The input-output viewpoint writes one higher-order differential or difference equation relating excitation and response directly, whereas the state-variable viewpoint writes several coupled first-order equations that also track internal variables. <!--SR:!fsrs,2027-04-28T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-11T00:00:00.000Z!fsrs,2027-05-05T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-13T00:00:00.000Z-->
- Why does the time-domain roadmap begin with input-output description? ::@:: Because it is the most direct route to classical response calculation before the course moves to richer state-variable and transform-domain viewpoints. <!--SR:!fsrs,2027-05-26T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-17T00:00:00.000Z!fsrs,2027-04-23T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-10T00:00:00.000Z-->
- Why does the lecture still emphasize direct time-domain solution even though transform methods are often faster? ::@:: Because direct solution keeps initial conditions visible, offers clearer physical interpretation, and provides the conceptual basis for later transform-domain methods. <!--SR:!fsrs,2027-05-05T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-13T00:00:00.000Z!fsrs,2027-04-28T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-11T00:00:00.000Z-->
- Why are homogeneous/particular and zero-input/zero-state not competing decompositions? ::@:: Because homogeneous/particular is the solving-method split, whereas zero-input/zero-state is the physical source-of-response split. <!--SR:!fsrs,2027-05-26T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-17T00:00:00.000Z!fsrs,2027-06-12T00:00:00.000Z,326,325.58679272,1,2,7,0,0,2026-07-21T00:00:00.000Z-->
- What part of the response is the natural target of convolution? ::@:: The zero-state part, because it isolates the externally driven response under zero stored initial state. <!--SR:!fsrs,2027-04-07T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-07T00:00:00.000Z!fsrs,2027-05-10T00:00:00.000Z,300,300.01984473,1,2,7,0,0,2026-07-14T00:00:00.000Z-->
- How should the main response topics be distributed across the ELEC 2100 notes? ::@:: `system.md` keeps the vocabulary and modelling roadmap, `continuous-time LTI system.md` and `discrete-time LTI system.md` carry the detailed response logic, and `convolution.md` carries the zero-state assembly method. <!--SR:!fsrs,2027-04-23T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-04-18T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-09T00:00:00.000Z-->
