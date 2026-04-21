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

A system maps an input signal to an output signal. In ELEC 2100, this input-output viewpoint is the bridge between raw signal descriptions and later transform-based analysis of linear time-invariant systems.

This note keeps the general systems vocabulary in one place: what a system is, how it is modeled, what the main properties mean, and how engineers classify systems before committing to one detailed solution method. The heavier response mechanics are deliberately delegated to the companion notes: `continuous-time LTI system.md` develops continuous-time response analysis, `discrete-time LTI system.md` develops the sample-by-sample analogue, and `convolution.md` carries the zero-state response machinery.

---

Flashcards for this section are as follows:

- What is a system in ELEC 2100? ::@:: A system is a rule or device that maps an input signal to an output signal. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why is the systems viewpoint central in ELEC 2100? ::@:: It connects signal descriptions to later transform-based analysis of linear time-invariant systems. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- How should this `system` note be used relative to the companion LTI notes? ::@:: Use this note for the core vocabulary and classification language of systems, then use `continuous-time LTI system.md`, `discrete-time LTI system.md`, and `convolution.md` for the detailed response mechanics and calculation workflows. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## system meaning and communication context

The lecture begins with a broad viewpoint: a system is an integrated entity composed of interacting components that together perform a stable function. In the notation used on the slides, $e(t)$ denotes excitation and $r(t)$ denotes response. The central question is what the system does to the input signal: whether it amplifies, filters, delays, distorts, or otherwise transforms it.

This viewpoint is motivated by communication and signal-processing examples. A communication chain contains devices such as transmitters, channels, and receivers, each of which acts as a system on the signal it receives. The key idea is that useful information is carried by signals and shaped by systems at every stage of the chain.

The lecture makes that viewpoint concrete with historical and modern communication systems. Samuel Morse's 1844 telegraph transmission _What hath God wrought!_ and Alexander Graham Bell's 1876 telephone transmission _Mr. Watson, come here, I want to see you._ are used as reminders that systems are real engineered mechanisms for encoding, carrying, and recovering messages, not just anonymous boxes in a diagram. The later survey of fiber-optic links, digital microwave links, satellite communication, cable systems, and mobile communication makes the same point on a larger technological scale.

The mobile-generation timeline is also part of the systems motivation rather than a detached history note. The slides move from 1G analog systems in the 1980s through 2G and 2.5G systems in the 1990s, 3G systems around 2000, 4G systems around 2010, and 5G systems from about 2019 onward, with 6G named as the next horizon. The engineering targets attached to the modern systems survey are high speed, wide bandwidth, high reliability, and low latency, which explains why better signal models and better system-analysis tools matter in practice.

The lecture also distinguishes signal theory from system theory. Signal theory studies the signals themselves; system theory studies how systems act on them. Likewise, system analysis asks for the output produced by a given system, whereas system synthesis asks how to design a system that achieves a desired behavior.

---

Flashcards for this section are as follows:

- What does the lecture mean by a system as an integrated entity? ::@:: It means a collection of interacting components that together perform a stable function. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What do $e(t)$ and $r(t)$ denote in the lecture notation? ::@:: $e(t)$ denotes excitation or input, while $r(t)$ denotes response or output. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the central systems question in this topic? ::@:: It is how the system transforms the input signal into the output signal. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why do communication examples belong in this systems topic? ::@:: They show that useful information is carried by signals and shaped by systems at every stage of a transmission chain. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What historical examples are used to make the communication-systems viewpoint concrete? ::@:: The lecture highlights Morse's 1844 telegraph transmission and Bell's 1876 telephone transmission as early engineered systems for carrying messages over distance. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why are the telegraph, telephone, and later communication-technology examples more than decorative history? ::@:: They show that systems theory is motivated by real engineered mechanisms whose performance depends on how signals are encoded, transmitted, filtered, and recovered. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What broad mobile-generation sequence is used in the introductory systems survey? ::@:: The survey moves from 1G analog systems to 2G and 2.5G, then to 3G, 4G, and 5G, with 6G identified as the next horizon. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What modern engineering targets are emphasized in the communication-systems survey? ::@:: High speed, wide bandwidth, high reliability, and low latency are emphasized as key modern communication-system targets. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the difference between signal theory and system theory? ::@:: Signal theory studies the signals themselves, whereas system theory studies how systems act on signals. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the difference between system analysis and system synthesis? ::@:: System analysis studies the output of a given system, whereas system synthesis designs a system to achieve desired behavior. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## continuous-time, discrete-time, and mathematical models

A continuous-time system acts on signals such as $x(t)$ and produces outputs such as $r(t)=H[e(t)]$. A discrete-time system acts on sequences such as $x[n]$ and produces outputs such as $y[n]=H[x[n]]$. In both cases the key abstraction is that the system is an operator acting on a signal, not just a formula in one variable.

The lecture emphasizes several common mathematical descriptions. Continuous-time systems are often modeled by differential equations. Discrete-time systems are often modeled by difference equations. Block diagrams and signal-flow-style structural diagrams provide another representation by showing how elementary operations are interconnected to build the whole system.

These descriptions matter because they are the first step toward analysis. Once a mathematical model has been written, one can ask how to compute the response under given excitation and initial conditions, and later how to interpret that response physically.

---

Flashcards for this section are as follows:

- What is a continuous-time system in operator form? ::@:: It is a system acting on signals such as $e(t)$, giving outputs such as $r(t)=H[e(t)]$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is a discrete-time system in operator form? ::@:: It is a system acting on sequences such as $x[n]$, giving outputs such as $y[n]=H[x[n]]$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why is the operator viewpoint useful? ::@:: It emphasizes that the system transforms whole signals or sequences, which makes block-diagram, convolution, and transform reasoning natural. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the standard mathematical model for many continuous-time systems? ::@:: A differential equation. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the standard mathematical model for many discrete-time systems? ::@:: A difference equation. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What do block diagrams contribute beyond equations? ::@:: They show the structural interconnection of elementary operations inside the system. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why are mathematical models central to system analysis? ::@:: They let us compute responses under given excitation and initial conditions, and then interpret those responses physically. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## memoryless, dynamic, lumped, and distributed systems

A useful first classification is to separate two different questions that beginners often mix together. Memoryless versus dynamic asks whether the output at one instant depends only on the input at that same instant or also on values from other times. Lumped versus distributed asks whether the model depends only on time or on both time and space.

Property-testing exercises are easiest when those questions are tested one at a time rather than by one vague global impression. A durable checklist is: Does the rule use only the present value? Does it ask for future input? Does it preserve superposition? Does a shift at the input become the same shift at the output? Does bounded input stay bounded? Can the input be uniquely recovered? Keeping those questions separate prevents one proof idea from being mistakenly reused for a different property.

---

Flashcards for this section are as follows:

- What are the two different classification axes introduced here? ::@:: Memoryless versus dynamic asks whether other times matter to the output, whereas lumped versus distributed asks whether the model depends only on time or also on spatial coordinates. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What checklist makes system-property testing safer? ::@:: Test one property question at a time: present-only dependence for memorylessness, future-input dependence for causality, superposition for linearity, shift-commutation for time invariance, bounded-input behavior for stability, and one-to-one recovery for invertibility. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### memorylessness

A system is memoryless if the output at time $t_0$ depends only on the input value at that same time $t_0$. So memorylessness excludes both past-input dependence and future-input dependence: neither earlier nor later samples may influence the present output. A dynamic system is any counterexample: its output at $t_0$ also depends on input values from other times. In a general linear kernel description $y(t)=\int_{-\infty}^{\infty} h(t,\tau)x(\tau)\,d\tau$, memorylessness means the kernel is concentrated on the diagonal $\tau=t$, so it has the form $h(t,\tau)=a(t)\delta(t-\tau)$. In the LTI special case this collapses further to $h(t)=K\delta(t)$, because only zero delay is allowed.

A clean memoryless example is $y(t)=3x(t)$. The input-output equation says the system simply scales the present input. The impulse-response form is $h(t)=3\delta(t)$, so $y=x*h$. Because the impulse response is concentrated entirely at zero delay, one input instant affects only the same output instant.

A clean counterexample is the causal averaging-type system $y(t)=\int_{-\infty}^{t} e^{-(t-\tau)}x(\tau)\,d\tau$. Its impulse response is $h(t)=e^{-t}u(t)$. One impulse at time $0$ creates an exponentially decaying tail for all later times, so a past input value continues to influence the present output. That spreading over time is exactly what memory means.

The recall picture is simple: memoryless systems look only at the present sample, while dynamic systems smear one input event across a time interval. A resistor is therefore the basic memoryless intuition, while capacitors, inductors, and low-pass filters are the basic dynamic intuition.

Representative rules make the distinction concrete. The affine-delay rule $y(t)=2x(t-1)+1$, the even-part operator $\tfrac12\bigl(x(t)+x(-t)\bigr)$, the comparator $y[n]=\max\{x[n],x[n-1]\}$, and the scaled-index rule $y[n]=n\,x[2n]$ are all non-memoryless because they need a value other than the present sample. By contrast, $y(t)=\cos(x(t))$ is memoryless: it is nonlinear, but it still acts pointwise on the present sample only.

---

Flashcards for this section are as follows:

- What does memorylessness mean? ::@:: A system is memoryless if the output at time $t_0$ depends only on the input value at the same time $t_0$; any system whose output also depends on other times is dynamic. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What does the present-only clarification for memorylessness say? ::@:: Memoryless means the present output depends on the present input only, so both past-input dependence and future-input dependence are excluded. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the kernel test for memorylessness? ::@:: In a linear kernel form $y(t)=\int h(t,\tau)x(\tau)\,d\tau$, memorylessness means $h(t,\tau)=a(t)\delta(t-\tau)$, and in the LTI special case this becomes $h(t)=K\delta(t)$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the memoryless example $y(t)=3x(t)$ in impulse-response form? ::@:: Its impulse-response form is $h(t)=3\delta(t)$, so the response is concentrated at zero delay and the output uses only the present input. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the dynamic counterexample $y(t)=\int_{-\infty}^{t} e^{-(t-\tau)}x(\tau)\,d\tau$ in impulse-response form? ::@:: Its impulse-response form is $h(t)=e^{-t}u(t)$, so one input impulse creates a decaying tail and past input values keep affecting the present output. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the intuition behind memorylessness? ::@:: Memoryless means "look only at now"; dynamic means "an input now leaves a trace that survives into other times." <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Which example systems are not memoryless because they use other indices or times? ::@:: $y(t)=2x(t-1)+1$ uses a past sample, $\tfrac12(x(t)+x(-t))$ uses a reflected future sample, $\max\{x[n],x[n-1]\}$ compares with a past sample, and $n\,x[2n]$ uses a different index altogether, so none are memoryless. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why is $y(t)=\cos(x(t))$ still memoryless? ::@:: It applies a pointwise map to the present sample only, even though the cosine operation is nonlinear. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### lumped and distributed viewpoints

The lecture also distinguishes lumped-parameter and distributed-parameter systems. A lumped-parameter system depends only on time and is typically modeled by ordinary differential equations; low-frequency RLC circuits are the standard example. A distributed-parameter system depends on time and space variables and is modeled by partial differential equations; transmission lines and waveguides are typical examples.

This classification is independent of memorylessness. A system can be lumped yet dynamic, because ordinary differential equations still describe time evolution with memory. The point of the lumped/distributed split is not whether the system remembers the past, but whether its state is concentrated into time-dependent variables or spread across both time and space.

---

Flashcards for this section are as follows:

- What is the lumped-versus-distributed distinction? ::@:: Lumped systems depend only on time and are usually modeled by ordinary differential equations, whereas distributed systems depend on both time and space and are usually modeled by partial differential equations. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What are standard examples of lumped and distributed systems? ::@:: A low-frequency RLC circuit is a standard lumped example, whereas a transmission line or waveguide is a standard distributed example. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the intuition behind lumped versus distributed systems? ::@:: Lumped means the system state can be summarized by time-varying variables only; distributed means the state is spread across space as well as time. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## invertibility, linearity, and time invariance

A second cluster of classifications asks three different questions. Invertibility asks whether the input can be recovered from the output. Linearity asks whether superposition holds. Time invariance asks whether a shift of the input produces the same shift of the output.

---

Flashcards for this section are as follows:

- invertibility, linearity, and time invariance / comparison ::@:: Invertibility asks whether the input can be recovered, linearity asks whether add-and-scale operations commute with the system, and time invariance asks whether absolute clock time matters. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### invertibility

A system is invertible if different inputs produce different outputs, so an inverse system can recover the original input from the response. A system is non-invertible if different inputs collapse to the same output, making unique recovery impossible. This is why compensation and equalization ideas require an appropriate inverse description.

A representative comparison set shows several distinct failure modes. The affine-delay rule $y(t)=2x(t-1)+1$ is invertible because one can recover $x(t)=\frac{y(t+1)-1}{2}$. By contrast, $y(t)=\cos(x(t))$ is not invertible because many different inputs share the same cosine value, the even-part operator is not invertible because it discards the odd component, the comparator $\max\{x[n],x[n-1]\}$ is not invertible because different sequences can share the same maxima, and $y[n]=n\,x[2n]$ is not invertible because odd-index samples are discarded and the factor $n$ destroys information at $n=0$.

---

Flashcards for this section are as follows:

- What is invertibility? ::@:: A system is invertible if different inputs produce different outputs, so an inverse system can recover the original input from the output. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What does non-invertible mean? ::@:: A system is non-invertible when different inputs can collapse to the same output, so unique recovery is impossible. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Which example systems are invertible or non-invertible in the comparison set? ::@:: $y(t)=2x(t-1)+1$ is invertible via $x(t)=\frac{y(t+1)-1}{2}$, whereas $\cos(x(t))$, the even-part operator, $\max\{x[n],x[n-1]\}$, and $n\,x[2n]$ are non-invertible because they merge distinct inputs into the same output in different ways. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### linearity

Linearity is characterized by homogeneity and superposition. If $x_1$ produces $y_1$ and $x_2$ produces $y_2$, then a linear system must send $c_1x_1+c_2x_2$ to $c_1y_1+c_2y_2$. In operator form, the judgment condition is $H[c_1x_1(t)+c_2x_2(t)]=c_1H[x_1(t)]+c_2H[x_2(t)]$. The practical test is therefore "combine first, then pass through the system" versus "pass through the system first, then combine the outputs".

A clean linear example is $y(t)=2x(t)-x(t-1)$. In impulse-response form this is $h(t)=2\delta(t)-\delta(t-1)$, so $y=x*h$. The same fixed weighting of present and delayed inputs applies no matter what amplitudes or signal combinations are used, so superposition holds automatically.

A standard counterexample is $y(t)=x^2(t)$. The input-output equation already shows that squaring is nonlinear. There is also no single first-order impulse-response representation $y(t)=\int h(t,\tau)x(\tau)\,d\tau$, because every such representation is linear in $x$. The closest kernel viewpoint is higher-order rather than ordinary impulse response: $y(t)=\iint \delta(t-\tau_1)\delta(t-\tau_2)x(\tau_1)x(\tau_2)\,d\tau_1d\tau_2$. The square creates cross terms, so the response to a sum is not the sum of the responses.

The intuition is that linear systems preserve add-and-scale structure. If you double the input, the output doubles; if you add two inputs, the output is the sum of the two outputs. Nonlinear systems distort that bookkeeping, usually by creating mixing terms, clipping, saturation, or amplitude-dependent gain.

The same comparison set is useful because it separates structure from surface appearance. The affine-delay rule $y(t)=2x(t-1)+1$ is not linear because the constant offset breaks homogeneity. The pointwise cosine rule and the max rule are nonlinear because they do not preserve superposition. By contrast, the even-part operator and the scaled-index rule $y[n]=n\,x[2n]$ are linear: averaging, fixed scaling, and reindexing still preserve add-and-scale behavior even though other properties may fail.

---

Flashcards for this section are as follows:

- What is linearity? ::@:: A system is linear if it satisfies homogeneity and superposition, meaning $H[c_1x_1+c_2x_2]=c_1H[x_1]+c_2H[x_2]$ for arbitrary signals and constants. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the linear example in input-output and impulse-response form? ::@:: Example: $y(t)=2x(t)-x(t-1)$. Impulse-response form: $h(t)=2\delta(t)-\delta(t-1)$, so the output is a fixed weighted sum of present and delayed inputs and superposition holds. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the nonlinear counterexample in input-output and impulse-response form? ::@:: Counterexample: $y(t)=x^2(t)$. There is no single first-order impulse response $h$ with $y(t)=\int h(t,\tau)x(\tau)\,d\tau$, because any such representation would already be linear; a nonlinear kernel description needs higher-order products such as $\iint \delta(t-\tau_1)\delta(t-\tau_2)x(\tau_1)x(\tau_2)\,d\tau_1d\tau_2$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the intuition behind linearity? ::@:: Linear means "add and scale outside or inside the system, and you get the same answer"; nonlinear means the system mixes amplitudes and creates extra interaction terms. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Which example systems fail superposition or homogeneity? ::@:: $y(t)=2x(t-1)+1$ fails homogeneity due to the constant offset, $y(t)=\cos(x(t))$ fails superposition due to pointwise nonlinearity, and $y[n]=\max\{x[n],x[n-1]\}$ fails superposition because maximum of sums does not equal sum of maxima. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Which example systems are linear despite other failures? ::@:: $y(t)=\tfrac12(x(t)+x(-t))$ (even-part operator) and $y[n]=n\,x[2n]$ (scaled-index rule) are linear because averaging, fixed scaling, and reindexing still preserve superposition even though other system properties fail. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### time invariance

A system is time invariant if, under the same initial-condition convention, its output is independent of the absolute time at which the input is applied. Equivalently, delaying the input merely delays the output by the same amount. In operator form, if $H[x(t)]=y(t)$, then time invariance requires $H[x(t-t_0)]=y(t-t_0)$. For a general linear kernel this means the kernel depends only on the time difference, not on the absolute clock: $h(t,\tau)=h(t-\tau)$.

A standard time-invariant example is $y(t)=x(t)-x(t-1)$. Its impulse response is $h(t)=\delta(t)-\delta(t-1)$. The system always forms the same present-minus-one-second-ago combination, no matter when the signal arrives, so shifting the input simply shifts the output.

A standard time-varying counterexample is $y(t)=\cos(\omega_0 t)x(t)$. In kernel form this is $h(t,\tau)=\cos(\omega_0 t)\delta(t-\tau)$. The explicit factor $\cos(\omega_0 t)$ depends on absolute time, so the system law itself changes with the clock. Shifting the input first gives $\cos(\omega_0 t)x(t-t_0)$, while shifting the original output gives $\cos(\omega_0(t-t_0))x(t-t_0)$, and these are not equal in general.

The intuition is that a time-invariant system has no hidden calendar or clock. The same waveform meeting the same system tomorrow should produce the same output shape, just shifted. A time-varying system behaves as if its coefficients or operating mode are changing with time.

Again, the same comparison set is a useful source of contrasts. The affine-delay rule, the pointwise cosine rule, and the max rule are time invariant because shifting the input shifts exactly the same algebraic rule. The even-part operator is not time invariant because reflection is pinned to the origin, and $y[n]=n\,x[2n]$ is not time invariant because both the explicit factor $n$ and the index scaling refer to absolute sample location.

---

Flashcards for this section are as follows:

- What is time invariance? ::@:: A system is time invariant if delaying the input by $t_0$ simply delays the output by the same $t_0$, so $H[x(t-t_0)]=y(t-t_0)$ whenever $H[x(t)]=y(t)$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the kernel test for time invariance? ::@:: In a linear kernel description, time invariance means the kernel depends only on the difference $t-\tau$, so it can be written as a one-variable impulse response $h(t-\tau)$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the time-invariant example in input-output and impulse-response form? ::@:: Example: $y(t)=x(t)-x(t-1)$. Impulse-response form: $h(t)=\delta(t)-\delta(t-1)$. The same present-minus-delayed rule applies at every absolute time, so shifting the input just shifts the output. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the time-varying counterexample in input-output and impulse-response form? ::@:: Counterexample: $y(t)=\cos(\omega_0 t)x(t)$. Kernel form: $h(t,\tau)=\cos(\omega_0 t)\delta(t-\tau)$. Because the coefficient depends on absolute time, the system law changes with the clock and the shift test fails. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the intuition behind time invariance? ::@:: Time invariant means "same rule at every clock time"; time varying means the system itself changes while the signal is passing through it. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Which example systems are time invariant? ::@:: $y(t)=2x(t-1)+1$ (affine delay), $y(t)=\cos(x(t))$ (pointwise cosine), and $y[n]=\max\{x[n],x[n-1]\}$ (windowed maximum) are all time invariant because the same algebraic rule applies at every absolute time. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Which example systems are time varying due to origin pinning or explicit indexing? ::@:: The even-part operator $\tfrac12(x(t)+x(-t))$ is not time invariant because reflection is pinned to the origin, and $y[n]=n\,x[2n]$ is not time invariant because the explicit factor $n$ and index scaling $2n$ refer to absolute sample location. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## causality and stability

A third cluster of properties asks whether the system can run in real time and whether it keeps bounded signals under control. Causality is the no-future-dependence property. Boundedness here means bounded-input bounded-output stability.

---

Flashcards for this section are as follows:

- What do causality and boundedness ask? ::@:: Causality asks whether future input is needed, whereas boundedness asks whether bounded input always produces bounded output. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### causality

A causal system does not depend on future input values. This matters because a physically realizable real-time system cannot react before its input arrives. In a general linear kernel form $y(t)=\int h(t,\tau)x(\tau)\,d\tau$, causality means $h(t,\tau)=0$ whenever $\tau>t$. In the LTI special case, that becomes the familiar support condition $h(t)=0$ for $t<0$.

A standard causal example is $y(t)=x(t)+x(t-2)$. Its impulse response is $h(t)=\delta(t)+\delta(t-2)$. The system uses the present value and a past value only, so it can be implemented in real time.

A standard noncausal counterexample is $y(t)=x(t+2)$. Its impulse response is $h(t)=\delta(t+2)$. The support at negative time means the output at time $t$ depends on an input value two seconds in the future, so the system violates real-time causality.

The recall picture is support geometry. If the impulse response reaches only zero delay and positive delays, the system is causal. If any part reaches into negative delay, the system is asking for future information. Noncausal systems can still be useful offline, because stored data make the "future" available after the fact.

The same comparison examples are useful here as well. The affine-delay rule, the pointwise cosine rule, and the max rule are causal because they use only present or past samples. The even-part operator is noncausal because $x(-t_0)$ can lie in the future relative to $t_0$, and $y[n]=n\,x[2n]$ is generally noncausal because for positive $n$ it asks for a future sample at index $2n$.

---

Flashcards for this section are as follows:

- What is causality? ::@:: A system is causal if the output at time $t$ depends only on input values at times $\tau\le t$ and never on future input values. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the impulse-response test for causality? ::@:: In a linear kernel description, causality means $h(t,\tau)=0$ for $\tau>t$; for an LTI system this becomes $h(t)=0$ for negative time. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the causal example in input-output and impulse-response form? ::@:: Example: $y(t)=x(t)+x(t-2)$. Impulse-response form: $h(t)=\delta(t)+\delta(t-2)$. The system uses only present and past input values. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the noncausal counterexample in input-output and impulse-response form? ::@:: Counterexample: $y(t)=x(t+2)$. Impulse-response form: $h(t)=\delta(t+2)$. The negative-time support means the output depends on future input. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the intuition behind causality? ::@:: Causal means the system can react only after information arrives; noncausal means some part of the rule reaches into the future. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Which example systems are causal? ::@:: $y(t)=2x(t-1)+1$ (affine delay), $y(t)=\cos(x(t))$ (pointwise cosine), and $y[n]=\max\{x[n],x[n-1]\}$ (windowed maximum) are all causal because they use only present or past samples. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Which example systems are noncausal? ::@:: The even-part operator $\tfrac12(x(t)+x(-t))$ is noncausal because $x(-t_0)$ can lie in the future relative to positive time $t_0$, and $y[n]=n\,x[2n]$ is generally noncausal because for positive $n$ it asks for a future sample at index $2n$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### boundedness (BIBO stability)

The stability notion emphasized in the early systems material is bounded-input bounded-output stability. The rigorous definition is: if an input is bounded in magnitude, meaning there exists some finite constant $M_x$ such that $|x(t)|\le M_x$ for all $t$ or $|x[n]|\le M_x$ for all $n$, then the corresponding output must also be bounded in magnitude, meaning there exists some finite constant $M_y$ such that $|y(t)|\le M_y$ for all $t$ or $|y[n]|\le M_y$ for all $n$. The output bound may depend on the chosen input, but it must stay finite whenever the input stays finite. For LTI systems the key impulse-response test is absolute integrability: if $\int_{-\infty}^{\infty}|h(t)|\,dt<\infty$, then bounded inputs stay bounded.

A standard stable example is $y(t)=\int_{-\infty}^{t} e^{-(t-\tau)}x(\tau)\,d\tau$. Its impulse response is $h(t)=e^{-t}u(t)$. Since $\int_{-\infty}^{\infty}|h(t)|\,dt=1$, any bounded input $|x(t)|\le M$ produces $|y(t)|\le M\int |h(t)|dt=M$. The system has finite total memory weight, so it cannot amplify a bounded input into an unbounded output.

A standard unstable counterexample is the integrator $y(t)=\int_{-\infty}^{t}x(\tau)\,d\tau$, whose impulse response is $h(t)=u(t)$. The input $x(t)=u(t)$ is bounded by $1$, yet the output is $y(t)=tu(t)$, which grows without bound. The problem is that $h(t)$ has infinite area, so the system can keep accumulating bounded input forever.

The rigorous intuition is that boundedness asks whether the system maps every finite-amplitude "box" of admissible inputs into some finite-amplitude "box" of outputs. The bound on the output does not need to equal the bound on the input, but it must exist. For LTI systems this becomes a total-memory-weight question: a decaying impulse response forgets enough of the past to keep the output under control, whereas an integrator never really lets go of past input, so even a bounded signal can accumulate into an ever-growing output.

The same comparison examples add several quick recognition patterns, including non-LTI ones. The affine-delay rule, the pointwise cosine rule, the even-part operator, and the max rule are all BIBO stable because bounded inputs stay bounded under those operations. The nonlinear memoryless rule $y[n]=e^{x[n]}$ is also BIBO stable: if $|x[n]|\le M$, then $-M\le x[n]\le M$, so $e^{-M}\le y[n]\le e^{M}$. By contrast, the time-varying rule $y[n]=(n+1)x[n]$ is not BIBO stable, because the bounded input $x[n]\equiv 1$ produces the unbounded sequence $y[n]=n+1$. The integrator is likewise not BIBO stable for the same accumulation reason.

---

Flashcards for this section are as follows:

- What is the rigorous definition of BIBO stability? ::@:: A system is BIBO stable if whenever there exists a finite constant $M_x$ with $|x(t)|\le M_x$ for all $t$ or $|x[n]|\le M_x$ for all $n$, there also exists a finite constant $M_y$ such that $|y(t)|\le M_y$ for all $t$ or $|y[n]|\le M_y$ for all $n$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the LTI impulse-response test for BIBO stability? ::@:: For an LTI system, a key sufficient and standard recognition test is absolute integrability of the impulse response: if $\int_{-\infty}^{\infty}|h(t)|\,dt<\infty$, then bounded inputs stay bounded. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the stable example in input-output and impulse-response form? ::@:: Example: $y(t)=\int_{-\infty}^{t} e^{-(t-\tau)}x(\tau)\,d\tau$. Impulse-response form: $h(t)=e^{-t}u(t)$. Its total impulse-response area is finite, so bounded inputs give bounded outputs. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the unstable counterexample in input-output and impulse-response form? ::@:: Counterexample: $y(t)=\int_{-\infty}^{t}x(\tau)\,d\tau$. Impulse-response form: $h(t)=u(t)$. The bounded input $x(t)=u(t)$ produces the unbounded ramp $y(t)=tu(t)$, so the system is not BIBO stable. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the rigorous intuition behind BIBO stability? ::@:: BIBO stability means every finite-amplitude input cage is sent into some finite-amplitude output cage; the output bound may change with the input, but it must remain finite. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the nonlinear stable example? ::@:: The non-LTI system $y[n]=e^{x[n]}$ is BIBO stable because $|x[n]|\le M$ implies $-M\le x[n]\le M$, hence $e^{-M}\le y[n]\le e^{M}$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the time-varying unstable example? ::@:: The non-LTI system $y[n]=(n+1)x[n]$ is not BIBO stable because the bounded input $x[n]\equiv 1$ gives $y[n]=n+1$, which is unbounded. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Which systems are BIBO stable in the comparison set? (affine delay, bounded cosine, averaging, windowed maximum, bounded exponential, integrator, $(n+1) \cdot$) ::@:: $y(t)=2x(t-1)+1$ (affine delay), $y(t)=\cos(x(t))$ (bounded cosine), $\tfrac12(x(t)+x(-t))$ (averaging), $\max\{x[n],x[n-1]\}$ (windowed maximum), and $y[n]=e^{x[n]}$ (bounded exponential when bounded inputs given) are all BIBO stable. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Which systems are not BIBO stable in the comparison set? (affine delay, bounded cosine, averaging, windowed maximum, bounded exponential, integrator, $(n+1) \cdot$) ::@:: The integrator $y(t)=\int_{-\infty}^{t}x(\tau)\,d\tau$ with impulse response $h(t)=u(t)$ is not BIBO stable because the bounded input $x(t)=u(t)$ produces the unbounded output $y(t)=tu(t)$. Similarly, $y[n]=(n+1)x[n]$ is not BIBO stable because the bounded input $x[n]\equiv 1$ produces the unbounded output $y[n]=n+1$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## linear time-invariant systems and response transfer

Linear time-invariant systems are the central class in the course because their structure lets one transfer known responses to new inputs systematically. If an LTI system in zero state sends $x_1(t)$ to $y_1(t)$, then shifted and linearly combined versions of $x_1$ produce the corresponding shifted and linearly combined versions of $y_1$.

The same structural cleanliness explains why differentiation, integration, convolution, and transform methods work so well for LTIs. Under the matching zero-state assumptions, one may often move these operations through the system instead of recomputing the response from scratch. The detailed worked examples belong in `continuous-time LTI system.md` and `convolution.md`; this section keeps only the high-level transfer principle.

---

Flashcards for this section are as follows:

- Why are LTI systems central in the course? ::@:: Because known responses can be transferred systematically to shifted and linearly combined inputs. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the response-transfer principle for an LTI system? ::@:: If an LTI system maps $x_1$ to $y_1$, then shifted and linearly combined versions of $x_1$ map to the corresponding shifted and linearly combined versions of $y_1$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What broad operator behaviors make LTI systems especially tractable? ::@:: Linearity and time invariance let known responses be shifted and recombined systematically, and under zero-state assumptions they also let differentiation, integration, convolution, and transform methods interact cleanly with the system. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Where should the detailed worked response-transfer examples for LTIs be studied in this course? ::@:: Use `continuous-time LTI system.md` and `convolution.md` for the detailed examples; this note keeps only the high-level transfer principle. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## representation methods for linear time-invariant systems

This part asks a practical question: how does one obtain the response of a signal passing through an LTI system? Several representations are useful rather than one single universal method. For continuous-time systems, one may use differential equations derived from physical laws, system functions obtained through Laplace transformation, unit impulse responses, or structural descriptions such as block diagrams. These are different views of the same underlying system.

The continuous-time circuit example is an RLC network driven by an excitation $e(t)$, with the capacitor voltage $v_C(t)$ taken as the output and the inductor current $i_L(t)$ treated as an internal variable. This setup matters because it cleanly separates the quantity we want to observe from the internal quantity that we later eliminate. The constitutive relations are not just formulas to memorize; they encode physical storage behavior. For the capacitor, $i_C(t)=C\frac{dv_C(t)}{dt}$ says that current is proportional to how fast the capacitor voltage changes, so a capacitor resists sudden voltage changes. For the inductor, $v_L(t)=L\frac{di_L(t)}{dt}$ says that voltage is proportional to how fast the inductor current changes, so an inductor resists sudden current changes.

Using the stated reference directions, the network equations become the KVL relation $e(t)=L\frac{di_L(t)}{dt}+v_C(t)$ and the node equation $i_L(t)=\frac{v_C(t)}{R}+C\frac{dv_C(t)}{dt}$. It is helpful to organize the derivation as a two-step elimination problem. First rewrite the model as two coupled first-order equations: $\frac{di_L(t)}{dt}=\frac{e(t)-v_C(t)}{L}$ and $\frac{dv_C(t)}{dt}=\frac{i_L(t)}{C}-\frac{v_C(t)}{RC}$. Then eliminate the internal current $i_L(t)$ by differentiating the second equation and substituting into the first. This yields $LC\frac{d^2v_C(t)}{dt^2}+\frac{L}{R}\frac{dv_C(t)}{dt}+v_C(t)=e(t)$, or equivalently $\frac{d^2v_C(t)}{dt^2}+\frac{1}{RC}\frac{dv_C(t)}{dt}+\frac{1}{LC}v_C(t)=\frac{1}{LC}e(t)$.

The final equation should then be interpreted, not merely written down. It is linear because no nonlinear products of state variables or inputs appear. It is time invariant because all coefficients are constants. It is second order because the highest derivative is second order. This is why the example is useful pedagogically: it shows how physical laws, topology, elimination, and structural interpretation all connect.

Block diagrams provide a second continuous-time representation. The main elementary blocks are adders, multipliers, scalar multipliers, differentiators, integrators, and time-delay elements. In this course, many single-input single-output operations are drawn with the same rectangular-block style and are distinguished by the label written inside the block. An adder is usually drawn as a summing node such as a small circle or a block marked with $\Sigma$; incoming branches may be marked with plus or minus signs to show whether a signal is added or subtracted, and the explicit algebra is $r(t)=e_1(t)+e_2(t)$ or $r(t)=e_1(t)-e_2(t)$. A multiplier is usually drawn as a block or node marked by $\times$ or another product label, and its explicit algebra is $r(t)=e_1(t)e_2(t)$, which is why it is generally nonlinear.

A scalar multiplier is the same operation as a gain element, so the terminology matters. A **gain block** is the dedicated rectangular block whose inside label is the gain value, for example a block marked $a$ meaning $r(t)=ae(t)$. A **branch coefficient** means the same gain is written directly on the signal line rather than inside a separate block, again meaning $r(t)=ae(t)$. A **triangle-style gain symbol** is an amplifier-like triangle carrying the gain label; it still means $r(t)=ae(t)$. These are three drawing conventions for the same scalar-multiplication operation, not three different system elements. In this course, the same box-style drawing is also reused for many other unary operations: a differentiator is drawn as a block labeled $\frac{d}{dt}$ with explicit relation $r(t)=\frac{d}{dt}e(t)$, an integrator as a block labeled $\int$ with relation $r(t)=\int_{-\infty}^{t}e(\tau)\,d\tau$, and a time-delay element as a block labeled by the delay $\tau$ or by an expression such as $e(t-\tau)$, meaning $r(t)=e(t-\tau)$. By contrast, common pointwise combination operations such as addition, subtraction, and multiplication are usually shown as small circular nodes with the relevant symbol inside.

The discrete-time analogue uses difference equations and block diagrams built from scalar multipliers, adders, and unit-delay elements $z^{-1}$. The scalar multiplier again has multiple acceptable drawing styles: a gain block with coefficient $a$, a branch coefficient written on the sequence line, or a triangle-style gain symbol. In every case the explicit algebra is $y[n]=ax[n]$. The unit-delay element is drawn as a block labeled $z^{-1}$ because, in the z-transform domain, delaying a sequence by one sample corresponds to multiplication by $z^{-1}$. Its explicit time-domain relation is $y[n]=x[n-1]$. Operationally, it behaves like a shift register: it outputs the previous sample while the new sample is shifted in.

Labeling conventions also matter. External input and output signals should normally be labeled explicitly by text such as $x(t)$, $r(t)$, $x[n]$, or $y[n]$ so the role of each arrow is unambiguous. Internal branch labels are helpful when a derivation needs them, but they are optional when the structure is already clear from context. If several block diagrams implement the same equation, they are all valid realizations; in practice, the simpler realization is usually preferred because it is easier to read and often uses fewer memory elements or fewer arithmetic operations.

The feedforward discrete-time example without feedback is a relation such as $y[n]=\frac{1}{2}x[n]+\frac{1}{2}x[n-1]$. To draw it, split the input into two branches, send one branch directly to an adder, send the other branch through one unit-delay block and a scalar multiplier, and then add the two branches. Because no past output is fed back, the structure is feedforward.

The comparison between backward and forward first-order difference equations is also important. A backward form such as $y[n]=x[n]+ay[n-1]$ is drawn with a feedback branch containing one delay element, because the present output depends on the previous output. The truly equivalent forward form is $y[n+1]=x[n+1]+ay[n]$. It is not a different system; it is the same recursion written one time step later, obtained by replacing $n$ with $n+1$ in the backward form. So the two forms are mathematically equivalent, but the backward form is preferred for implementation because it computes the present output $y[n]$ directly from quantities available at time $n$, whereas the forward form is phrased as the computation of the next output $y[n+1]$.

For a second-order system such as $y[n]=x[n]-3x[n-2]+5y[n-1]-6y[n-2]$, one may draw multiple structurally different but equivalent diagrams. The common implementation fact is that at least two delay elements are required, because the system depends on values two samples into the past. This is also reflected in the general linear difference-equation form $\sum_{k=0}^{N}a_k y[n-k]=\sum_{r=0}^{M}b_r x[n-r]$, whose order is the difference between the highest and lowest argument values of the dependent variable.

The general linear difference-equation form is

$\sum_{k=0}^{N}a_k y[n-k]=\sum_{r=0}^{M}b_r x[n-r]$.

The order of the difference equation is the difference between the highest and lowest argument values of the dependent variable appearing in the equation. This definition matches the practical memory requirement: the larger the spread in delayed output indices, the more memory elements are needed in implementation.

---

Flashcards for this section are as follows:

- What are the main ways to represent an LTI system when trying to obtain its response? ::@:: The main representations are differential equations, system functions via Laplace transformation, unit impulse responses, and structural descriptions such as block diagrams. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- Given an RLC circuit where the source $e(t)$ feeds an inductor $L$ in series, the node after the inductor is the output node with voltage $v_C(t)$, and a resistor $R$ and capacitor $C$ are both connected from that node to the reference line in parallel, with internal current $i_L(t)$ through the inductor, capacitor law $i_C(t)=C\frac{dv_C(t)}{dt}$, and inductor law $v_L(t)=L\frac{di_L(t)}{dt}$, what physical intuition do the constitutive relations encode and what topology equations are written before elimination? ::@:: The capacitor law says current tracks how fast capacitor voltage changes, so a capacitor resists sudden voltage change; the inductor law says voltage tracks how fast inductor current changes, so an inductor resists sudden current change; the topology equations are $e(t)=L\frac{di_L(t)}{dt}+v_C(t)$ and $i_L(t)=\frac{v_C(t)}{R}+C\frac{dv_C(t)}{dt}$. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- Given the same RLC circuit where the source $e(t)$ feeds an inductor $L$ in series, the output is the node voltage $v_C(t)$ after the inductor, and a resistor $R$ and capacitor $C$ are connected from that node to the reference line in parallel, with equations $e(t)=L\frac{di_L(t)}{dt}+v_C(t)$ and $i_L(t)=\frac{v_C(t)}{R}+C\frac{dv_C(t)}{dt}$, or equivalently $\frac{di_L(t)}{dt}=\frac{e(t)-v_C(t)}{L}$ and $\frac{dv_C(t)}{dt}=\frac{i_L(t)}{C}-\frac{v_C(t)}{RC}$, what equation results after eliminating $i_L(t)$, and what does it tell you structurally? ::@:: Eliminating $i_L(t)$ gives $LC\frac{d^2v_C(t)}{dt^2}+\frac{L}{R}\frac{dv_C(t)}{dt}+v_C(t)=e(t)$, equivalently $\frac{d^2v_C(t)}{dt^2}+\frac{1}{RC}\frac{dv_C(t)}{dt}+\frac{1}{LC}v_C(t)=\frac{1}{LC}e(t)$; this shows the system is linear, time invariant, and second order. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- How are the main continuous-time block-diagram elements drawn, what equations do they represent, and what do the terms gain block, branch coefficient, and triangle-style gain symbol mean? ::@:: An adder is drawn as a summing node or $\Sigma$ block and represents $r(t)=e_1(t)\pm e_2(t)$; a multiplier is drawn as a $\times$ or product block and represents $r(t)=e_1(t)e_2(t)$; a scalar multiplier represents $r(t)=ae(t)$ and may be drawn as a gain block with $a$ inside, as a branch coefficient written directly on the line, or as a triangle-style gain symbol; a differentiator represents $r(t)=\frac{d}{dt}e(t)$, an integrator represents $r(t)=\int_{-\infty}^{t}e(\tau)\,d\tau$, and a delay block represents $r(t)=e(t-\tau)$. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- How are the main discrete-time block-diagram elements drawn, what equations do they represent, and why is the delay labeled $z^{-1}$? ::@:: A discrete-time scalar multiplier represents $y[n]=ax[n]$ and may be drawn as a gain block, a branch coefficient, or a triangle-style gain symbol; the delay block represents $y[n]=x[n-1]$ and is labeled $z^{-1}$ because one-sample delay corresponds to multiplication by $z^{-1}$ in the z-transform domain. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- In this course, how are unary system operations usually drawn compared with common pointwise combination operations? ::@:: Many unary operations such as gain, delay, differentiation, and integration are drawn as labeled rectangular blocks, whereas common pointwise combination operations such as addition, subtraction, and multiplication are usually drawn as small circular nodes with the relevant symbol inside. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- What labels should definitely appear on a block diagram, and what labels may be omitted if the structure is already clear? ::@:: External input and output arrows should normally be labeled explicitly by text such as $x[n]$ and $y[n]$, while internal branch labels are optional when the structure is already clear. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- How is the feedforward example $y[n]=\frac{1}{2}x[n]+\frac{1}{2}x[n-1]$ drawn, and why is it called feedforward? ::@:: Split the input into two branches, send one directly to an adder, send the other through one delay and a scalar multiplier, then add the branches; it is feedforward because the output depends only on present and delayed input samples, not on delayed outputs. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- Why is the backward form $y[n]=x[n]+ay[n-1]$ preferred over the forward form $y[n+1]=x[n+1]+ay[n]$ for implementation? ::@:: The two forms are mathematically equivalent, because the forward form is obtained from the backward form by replacing $n$ with $n+1$. But $y[n]=x[n]+ay[n-1]$ is preferred for implementation because it computes the present output directly from the present input and the previously stored output, so it is already in the most convenient causal real-time form. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- How are $y[n]=x[n]+ay[n-1]$ and $y[n+1]=x[n+1]+ay[n]$ related? ::@:: They are the same first-order recursion written with different time indices. Replacing $n$ by $n+1$ in $y[n]=x[n]+ay[n-1]$ gives $y[n+1]=x[n+1]+ay[n]$, so the two equations are mathematically equivalent. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- What does the second-order example $y[n]=x[n]-3x[n-2]+5y[n-1]-6y[n-2]$ teach about realization and order? ::@:: It shows that multiple equivalent structural diagrams are possible, but at least two delay elements are required because the system depends on values two samples into the past; more generally the order of $\sum_{k=0}^{N}a_k y[n-k]=\sum_{r=0}^{M}b_r x[n-r]$ is determined by the spread of delayed output indices. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- If several block diagrams implement the same system equation, what design preference is usually best? ::@:: Multiple realizations may be equivalent, but the simpler one is usually preferred because it is easier to read and often uses fewer memory elements or arithmetic operations. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->

## system analysis viewpoints

The main analysis viewpoint is: first build a mathematical model of the system, then analyze the response under a given input. In other words, the workflow is model first, response second.

Two major model-building viewpoints are presented. The input-output description focuses only on the relationship between excitation and response and ignores internal system variables. It is especially natural for SISO systems, meaning single-input single-output systems: there is one input channel and one output channel, so one higher-order differential or difference equation can often relate them directly. The state-variable viewpoint tracks both the overall response and internal variables such as capacitor voltages or inductor currents. It is naturally suited to MIMO systems, meaning multiple-input multiple-output systems: there may be several input channels, several output channels, and several coupled internal variables, so one usually writes a set of coupled first-order equations instead of one single scalar equation.

The lecture also contrasts time-domain and transform-domain solution methods. Time-domain analysis includes direct solution of differential equations, difference equations, and convolution integrals or sums. Transform-domain analysis introduces Fourier, Laplace, and z-transform viewpoints because they convert many system calculations into simpler algebraic forms.

The overall trajectory of the course follows these transitions repeatedly: from input-output description toward state-variable description, from time-domain analysis toward transform-domain analysis, and from continuous systems toward discrete systems. Throughout, the engineering preference is for systems that are linear, time invariant, causal, and stable.

---

Flashcards for this section are as follows:

- What are the two high-level tasks in system analysis? ::@:: Build a mathematical model of the system and then analyze the output response under a given input. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the input-output description viewpoint? ::@:: It focuses only on the relationship between excitation and response and ignores internal system variables. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What does SISO mean? ::@:: It means single-input single-output, so the system has one input channel and one output channel. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why is the input-output viewpoint natural for SISO systems? ::@:: Because one nth-order differential or difference equation can often relate the single input and single output directly. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the state-variable viewpoint? ::@:: It tracks both the overall response and internal variables such as capacitor voltages or inductor currents. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What does MIMO mean? ::@:: It means multiple-input multiple-output, so the system may have several input channels and several output channels. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why is the state-variable viewpoint useful for MIMO systems? ::@:: Because it naturally represents multiple interacting inputs, outputs, and internal variables through coupled first-order equations. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What belongs to time-domain analysis? ::@:: Direct solution of differential equations, difference equations, and convolution integrals or sums. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why are transform-domain methods introduced? ::@:: They convert many system calculations into simpler algebraic forms. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What transform-domain viewpoints are highlighted in the lecture summary? ::@:: Fourier, Laplace, and z-transform viewpoints. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What overall transitions organize the course's systems analysis viewpoint? ::@:: From input-output to state-variable description, from time-domain to transform-domain analysis, and from continuous systems to discrete systems. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What combination of system properties is especially preferred from an engineering perspective? ::@:: Linear, time-invariant, causal, and stable behavior. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## time-domain analysis methods and differential-equation viewpoint

The time-domain treatment re-enters the systems topic from a more operational angle: once a model has been written, how does one actually obtain the response? The lecture first contrasts two time-domain modelling viewpoints. The **input-output description** writes one higher-order differential or difference equation relating excitation and response directly. The **state-variable description** writes several coupled first-order equations that also track internal variables. This note keeps that comparison at the roadmap level, while the companion LTI notes carry the detailed continuous-time and discrete-time calculations.

The reason the course still studies time-domain methods before leaning on transforms is conceptual rather than nostalgic. Direct solution keeps the role of initial conditions visible, preserves the physical meaning of stored energy, and makes later transform methods easier to interpret. The calculation may be longer, but the modeling logic is transparent.

At the roadmap level, the key split is the same in both continuous time and discrete time. The classical solver writes the response as homogeneous plus particular. The engineering viewpoint writes the same response as zero-input plus zero-state. Those decompositions are not rivals: homogeneous/particular tells you how to solve the equation, whereas zero-input/zero-state tells you what physically caused the response. In both settings, the zero-state part is the natural target of convolution, while the zero-input part is the natural target of initial-condition reasoning.

The durable organization of the course is therefore:

- use `system.md` for the language of properties, modelling viewpoints, and classification;
- use `continuous-time LTI system.md` for differential-equation response logic, impulse response, step response, and continuous-time causality/stability tests;
- use `discrete-time LTI system.md` for recursion logic, geometric impulse responses, and discrete-time causality/stability tests;
- use `convolution.md` when the zero-state response should be assembled directly from the impulse response.

---

Flashcards for this section are as follows:

- What is the difference between the input-output and state-variable viewpoints in the time-domain roadmap? ::@:: The input-output viewpoint writes one higher-order differential or difference equation relating excitation and response directly, whereas the state-variable viewpoint writes several coupled first-order equations that also track internal variables. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why does the time-domain roadmap begin with input-output description? ::@:: Because it is the most direct route to classical response calculation before the course moves to richer state-variable and transform-domain viewpoints. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why does the lecture still emphasize direct time-domain solution even though transform methods are often faster? ::@:: Because direct solution keeps initial conditions visible, offers clearer physical interpretation, and provides the conceptual basis for later transform-domain methods. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why are homogeneous/particular and zero-input/zero-state not competing decompositions? ::@:: Because homogeneous/particular is the solving-method split, whereas zero-input/zero-state is the physical source-of-response split. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What part of the response is the natural target of convolution in both continuous and discrete time? ::@:: The zero-state part, because it isolates the externally driven response under zero stored initial state. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- How should the main response topics be distributed across the ELEC 2100 notes? ::@:: `system.md` keeps the vocabulary and modelling roadmap, `continuous-time LTI system.md` and `discrete-time LTI system.md` carry the detailed response logic, and `convolution.md` carries the zero-state assembly method. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
