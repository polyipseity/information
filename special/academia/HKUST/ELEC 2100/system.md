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

---

Flashcards for this section are as follows:

- What is a system? ::@:: A system is a rule or device that maps an input signal to an output signal.
- Why is the systems viewpoint central in ELEC 2100? ::@:: It connects signal descriptions to later transform-based analysis of linear time-invariant systems.

## system meaning and communication context

The lecture begins with a broad viewpoint: a system is an integrated entity composed of interacting components that together perform a stable function. In the notation used on the slides, $e(t)$ denotes excitation and $r(t)$ denotes response. The central question is what the system does to the input signal: whether it amplifies, filters, delays, distorts, or otherwise transforms it.

This viewpoint is motivated by communication and signal-processing examples. A communication chain contains devices such as transmitters, channels, and receivers, each of which acts as a system on the signal it receives. The key idea is that useful information is carried by signals and shaped by systems at every stage of the chain.

The lecture also distinguishes signal theory from system theory. Signal theory studies the signals themselves; system theory studies how systems act on them. Likewise, system analysis asks for the output produced by a given system, whereas system synthesis asks how to design a system that achieves a desired behavior.

---

Flashcards for this section are as follows:

- What does the lecture mean by a system as an integrated entity? ::@:: It means a collection of interacting components that together perform a stable function.
- What do $e(t)$ and $r(t)$ denote in the lecture notation? ::@:: $e(t)$ denotes excitation or input, while $r(t)$ denotes response or output.
- What is the central systems question in this topic? ::@:: It is how the system transforms the input signal into the output signal.
- Why do communication examples belong in this systems topic? ::@:: They show that useful information is carried by signals and shaped by systems at every stage of a transmission chain.
- What is the difference between signal theory and system theory? ::@:: Signal theory studies the signals themselves, whereas system theory studies how systems act on signals.
- What is the difference between system analysis and system synthesis? ::@:: System analysis studies the output of a given system, whereas system synthesis designs a system to achieve desired behavior.

## communication-system milestones and modern technologies

The introductory communication slides make the systems viewpoint concrete by showing how electrical and electromagnetic signals carry messages over distance. One historical milestone is Samuel Morse's successful telegraph transmission in 1844, when the message _What hath God wrought!_ was sent from Washington, D.C. to the B&O Railroad Depot in Baltimore, Maryland, over a distance of about 40 miles or 64 km. Another milestone is Alexander Graham Bell's 1876 telephone transmission _Mr. Watson, come here, I want to see you._ These examples matter because they show that systems are not abstract boxes only; they are real engineered mechanisms that encode, carry, and recover messages.

The lecture then connects those early systems to modern communication technologies. The listed examples include fiber-optic communication, digital microwave links, satellite communication, cable systems, and mobile communication. This broad survey is pedagogically useful because it shows that the same system ideas survive even as the physical medium changes.

The mobile timeline is presented as a sequence of generations. The slides place 1G analog mobile systems in the 1980s, 2G systems such as TDMA and GSM in the early 1990s, 2.5G systems such as GPRS and EDGE in the late 1990s, 3G systems using CDMA from about 2000 onward, 4G systems using OFDMA and MIMO from about 2010 onward, and 5G systems from about 2019 onward with massive MIMO and NOMA. The horizon beyond that is labeled 6G.

The 5G slide also stresses the engineering targets that modern systems are expected to satisfy: high speed, wide bandwidth, high reliability, and low latency. In other words, the historical and modern examples are not decorative trivia. They explain why improved signal representations, processing methods, and system models matter: real communication systems are judged by what they can deliver under practical engineering constraints.

---

Flashcards for this section are as follows:

- What 1844 event is used as an early communication-system milestone? ::@:: Samuel Morse successfully transmitted the telegraph message _What hath God wrought!_ from Washington, D.C. to Baltimore in 1844.
- What distance is associated with Morse's 1844 telegraph example? ::@:: The slides describe the Washington-to-Baltimore transmission as about 40 miles or 64 km.
- What 1876 event is used as a telephone milestone? ::@:: Alexander Graham Bell's telephone transmission _Mr. Watson, come here, I want to see you._ is presented as a milestone in 1876.
- Why are the telegraph and telephone milestones pedagogically useful in this systems topic? ::@:: They show that systems are real engineered mechanisms for encoding, carrying, and recovering messages rather than merely abstract boxes.
- Which major modern communication technologies are highlighted in the introductory survey? ::@:: The survey highlights fiber-optic communication, digital microwave links, satellite communication, cable systems, and mobile communication.
- Why does the lecture survey multiple generations of communication technology? ::@:: It shows that the same core system ideas survive even when the physical medium and implementation technology change.
- How does the lecture place 1G mobile systems historically? ::@:: It places 1G analog mobile systems in the 1980s.
- How does the lecture place 2G and 2.5G mobile systems historically? ::@:: It places 2G systems such as TDMA and GSM in the early 1990s and 2.5G systems such as GPRS and EDGE in the late 1990s.
- How does the lecture place 3G and 4G mobile systems historically? ::@:: It places 3G systems using CDMA from about 2000 onward and 4G systems using OFDMA and MIMO from about 2010 onward.
- How does the lecture characterize 5G and the horizon beyond it? ::@:: It presents 5G from about 2019 onward with massive MIMO and NOMA, and labels 6G as the next horizon.
- What engineering targets are emphasized on the 5G slide? ::@:: The emphasized targets are high speed, wide bandwidth, high reliability, and low latency.
- Why are the modern communication examples more than historical decoration? ::@:: They explain why better signal representations, processing methods, and system models matter under real engineering performance constraints.

## continuous-time, discrete-time, and mathematical models

A continuous-time system acts on signals such as $x(t)$ and produces outputs such as $r(t)=H[e(t)]$. A discrete-time system acts on sequences such as $x[n]$ and produces outputs such as $y[n]=H[x[n]]$. In both cases the key abstraction is that the system is an operator acting on a signal, not just a formula in one variable.

The lecture emphasizes several common mathematical descriptions. Continuous-time systems are often modeled by differential equations. Discrete-time systems are often modeled by difference equations. Block diagrams and signal-flow-style structural diagrams provide another representation by showing how elementary operations are interconnected to build the whole system.

These descriptions matter because they are the first step toward analysis. Once a mathematical model has been written, one can ask how to compute the response under given excitation and initial conditions, and later how to interpret that response physically.

---

Flashcards for this section are as follows:

- What is a continuous-time system in operator form? ::@:: It is a system acting on signals such as $e(t)$, giving outputs such as $r(t)=H[e(t)]$.
- What is a discrete-time system in operator form? ::@:: It is a system acting on sequences such as $x[n]$, giving outputs such as $y[n]=H[x[n]]$.
- Why is the operator viewpoint useful? ::@:: It emphasizes that the system transforms whole signals or sequences, which makes block-diagram, convolution, and transform reasoning natural.
- What is the standard mathematical model for many continuous-time systems? ::@:: A differential equation.
- What is the standard mathematical model for many discrete-time systems? ::@:: A difference equation.
- What do block diagrams contribute beyond equations? ::@:: They show the structural interconnection of elementary operations inside the system.
- Why are mathematical models central to system analysis? ::@:: They let us compute responses under given excitation and initial conditions, and then interpret those responses physically.

## memoryless, dynamic, lumped, and distributed systems

A memoryless or instantaneous system produces its output at a given time using only the input at that same time. Algebraic input-output relations are the usual mathematical form of such systems. A resistor obeying $v_R(t)=Ri(t)$ is a standard example: the voltage depends only on the current at the same instant.

A dynamic system has memory, so its output depends on input values from other times as well. Capacitors, inductors, and other energy-storage elements lead to such systems. For example, a capacitor relation can be written in integral form, which shows that the present voltage depends on accumulated past current rather than only on the instantaneous input.

The lecture also distinguishes lumped-parameter and distributed-parameter systems. A lumped-parameter system depends only on time and is typically modeled by ordinary differential equations; low-frequency RLC circuits are the standard example. A distributed-parameter system depends on time and space variables and is modeled by partial differential equations; transmission lines and waveguides are typical examples.

These distinctions are conceptually different and should not be mixed. Memoryless versus dynamic asks whether the system stores information from other times. Lumped versus distributed asks whether the model depends only on time or on both time and spatial coordinates.

---

Flashcards for this section are as follows:

- What is a memoryless or instantaneous system? ::@:: It is a system whose output at a given time depends only on the input at that same time.
- Why is a resistor a standard memoryless example? ::@:: Because $v_R(t)=Ri(t)$ is an algebraic relation using the current at the same instant only.
- What is a dynamic system? ::@:: It is a system with memory, so its output depends on input values from other times as well.
- Why are capacitors and inductors associated with dynamic systems? ::@:: Because their behavior depends on stored energy and accumulated past input, not only on the present input value.
- What is a lumped-parameter system? ::@:: It is a system modeled as depending on time only, typically through ordinary differential equations.
- What is a distributed-parameter system? ::@:: It is a system whose model depends on both time and spatial variables, typically through partial differential equations.
- What is a standard lumped-parameter example in the lecture? ::@:: A low-frequency RLC circuit.
- What is a standard distributed-parameter example in the lecture? ::@:: A transmission line or waveguide.
- What is the difference between memoryless vs dynamic and lumped vs distributed? ::@:: Memoryless vs dynamic asks whether the system stores past information, whereas lumped vs distributed asks whether the model depends only on time or on both time and space.

## invertibility, linearity, and time invariance

A system is invertible if different inputs produce different outputs, so an inverse system can recover the original input from the response. A system is non-invertible if different inputs collapse to the same output, making unique recovery impossible. This is why system compensation is possible only when an appropriate inverse description exists.

Linearity is characterized by homogeneity and superposition. If $e_1$ produces $r_1$ and $e_2$ produces $r_2$, then a linear system must send $c_1e_1+c_2e_2$ to $c_1r_1+c_2r_2$. In operator form, the judgment condition is $H[c_1e_1(t)+c_2e_2(t)]=c_1H[e_1(t)]+c_2H[e_2(t)]$.

The same rule applies in both continuous and discrete time. The practical judgment method is therefore: first form the linear combination and pass it through the system, then separately pass each signal through the system and linearly combine the outputs, and compare the two results. If they agree for arbitrary choices of signals and constants, the system is linear; otherwise it is nonlinear. The lecture also notes an important caution: external excitation and nonzero-state effects must be handled separately, because a test contaminated by extra forcing or mismatched initial conditions does not isolate the system's intrinsic linearity.

The nonlinear example in the lecture is $r(t)=e^2(t)$. If $e_1(t)$ and $e_2(t)$ produce $r_1(t)=e_1^2(t)$ and $r_2(t)=e_2^2(t)$, then the output produced by the combined input $c_1e_1(t)+c_2e_2(t)$ is $H[c_1e_1(t)+c_2e_2(t)]=(c_1e_1(t)+c_2e_2(t))^2=c_1^2e_1^2(t)+2c_1c_2e_1(t)e_2(t)+c_2^2e_2^2(t)$,

whereas the linear combination of the separate outputs is only $c_1e_1^2(t)+c_2e_2^2(t)$ if one uses the same coefficients, or more structurally $c_1r_1(t)+c_2r_2(t)$. The mixed term $2c_1c_2e_1(t)e_2(t)$ shows immediately that the two results are not equal in general, so the system is nonlinear.

A system is time invariant if, under zero initial conditions, its output is independent of the time at which the input is applied; only the relative shape of the input matters. Equivalently, delaying the input by some amount merely delays the output by the same amount. For continuous-time systems this is the rule "shift first, then pass through the system = pass through the system first, then shift." In operator form, if $H[e(t)]=r(t)$, then time invariance requires $H[e(t-\tau)]=r(t-\tau)$.

For discrete-time systems the same principle applies with integer index shifts.

The lecture gives two complementary ways to think about this test. From a circuit viewpoint, one asks whether the component parameters themselves vary with time. From an equation viewpoint, one asks whether the coefficients of the describing equation vary with time. If the system law itself changes with time, then simply shifting the input cannot produce a pure shift of the output.

The lecture's examples illustrate the distinction. The derivative system $r(t)=\frac{d}{dt}e(t)$ is time invariant because the two test branches match exactly: shifting the input first gives $\frac{d}{dt}e(t-t_0)$, while differentiating first and then shifting the output also gives $r(t-t_0)=\frac{d}{dt}e(t-t_0)$. Since the results are identical, the derivative system is time invariant.

The amplitude-modulation system $r(t)=\cos(\omega_0 t)e(t)$ is time varying because the explicit time factor changes the system when the input is shifted. If the input is shifted first, the output becomes $\cos(\omega_0 t)e(t-t_0)$. If the original output is formed first and then shifted, one gets $r(t-t_0)=\cos(\omega_0 (t-t_0))e(t-t_0)$. These are different in general because $\cos(\omega_0 t)$ is not equal to $\cos(\omega_0(t-t_0))$, so the system is time varying.

---

Flashcards for this section are as follows:

- What does it mean for a system to be invertible? ::@:: Different inputs produce different outputs, so an inverse system can recover the original input from the output.
- What makes a system non-invertible? ::@:: Different inputs can produce the same output, making unique recovery of the original input impossible.
- What two properties define linearity? ::@:: Homogeneity and superposition.
- What is the operator-form linearity test? ::@:: A system is linear if $H[c_1e_1(t)+c_2e_2(t)]=c_1H[e_1(t)]+c_2H[e_2(t)]$ for arbitrary signals and constants.
- What is the practical judgment method for linearity? ::@:: Compare "linear-combine first, then pass through the system" with "pass through the system first, then linear-combine the outputs"; if they agree for arbitrary inputs and constants, the system is linear.
- Why must external excitation and nonzero-state effects be handled separately when testing linearity? ::@:: Because extra forcing or mismatched initial conditions can distort the comparison and prevent the test from isolating the system's intrinsic linear property.
- Why is the system $r(t)=e^2(t)$ nonlinear? ::@:: Because $H[c_1e_1+c_2e_2]=(c_1e_1+c_2e_2)^2$ contains the mixed term $2c_1c_2e_1e_2$, so it does not equal the corresponding linear combination of separate outputs in general.
- What does time invariance mean under zero initial conditions? ::@:: It means the output depends only on the relative shape of the input, so delaying the input merely delays the output by the same amount.
- What is the operator-form time-invariance test for a continuous-time system? ::@:: If $H[e(t)]=r(t)$, then time invariance requires $H[e(t-\tau)]=r(t-\tau)$.
- What are the two lecture viewpoints for judging time invariance? ::@:: From a circuit viewpoint, check whether component parameters vary with time; from an equation viewpoint, check whether the coefficients of the describing equation vary with time.
- Why is the derivative system $r(t)=\frac{d}{dt}e(t)$ time invariant? ::@:: Shifting the input first or differentiating first and then shifting both give the same result $\frac{d}{dt}e(t-t_0)$.
- Why is the system $r(t)=\cos(\omega_0 t)e(t)$ time varying under the shift test? ::@:: Shifting the input first gives $\cos(\omega_0 t)e(t-t_0)$, whereas shifting the original output gives $\cos(\omega_0(t-t_0))e(t-t_0)$, and these are not equal in general.
- Does the same linearity and time-invariance logic apply in discrete time? ::@:: Yes; the same superposition and shift tests apply, but with integer-index sequences instead of continuous-time signals.

## causality and stability

A causal system does not depend on future input values. This matters because a physically realizable real-time system cannot react before its input arrives. The lecture uses $r(t)=e(t)+e(t-2)$ as a causal example because it depends only on present and past input, and $r(t)=e(t)+e(t+2)$ as a noncausal example because it depends on future input.

The lecture also points out that causality is an implementation requirement for real-time systems. Noncausal systems are still useful in offline processing tasks such as signal compression, expansion, and voice processing, where future data may already be available in stored form.

The stability notion emphasized in the early systems material is bounded-input bounded-output stability. A system is BIBO stable if every bounded input produces a bounded output. This is the practical input-output stability criterion introduced before transform-domain methods are available.

---

Flashcards for this section are as follows:

- What is a causal system? ::@:: It is a system that does not depend on future input values.
- Why must a physically realizable real-time system be causal? ::@:: Because it cannot react before the input arrives.
- Why is $r(t)=e(t)+e(t-2)$ causal? ::@:: It depends only on present and past excitation.
- Why is $r(t)=e(t)+e(t+2)$ noncausal? ::@:: It depends on future excitation.
- Why can noncausal systems still be useful in practice? ::@:: In offline tasks such as compression, expansion, and voice processing, future data may already be available.
- What is BIBO stability? ::@:: A system is BIBO stable if every bounded input produces a bounded output.
- Why is BIBO stability important from an engineering perspective? ::@:: Engineers want systems whose outputs do not diverge when the inputs remain bounded.

## linear time-invariant systems and response transfer

Linear time-invariant systems are the central class in the course because their structure allows responses to be transferred systematically from known cases to new ones. If an LTI system in zero state sends $x_1(t)$ to $y_1(t)$, then shifted and linearly combined versions of $x_1$ produce the corresponding shifted and linearly combined versions of $y_1$.

The lecture also highlights differential and integral characteristics of LTI systems. If an LTI system maps an input to an output, then differentiating or integrating the input produces the correspondingly differentiated or integrated output, provided the relevant zero-state setting is preserved. This is one of the first hints that LTI systems interact cleanly with convolution and transforms.

A standard lecture example starts from the known zero-state pair $x_1(t)=e^{-t}u(t)$ and $y_1(t)=\cos(3t)u(t)$. Since $\frac{d}{dt}x_1(t)=-e^{-t}u(t)+\delta(t)$, the corresponding zero-state response is $\frac{d}{dt}y_1(t)=-3\sin(3t)u(t)+\delta(t)$. The same example also uses impulse sampling to simplify singular terms. Because $e^{-t}\delta(t)=\delta(t)$, the inputs $-e^{-t}u(t)+e^{-t}\delta(t)$ and $-e^{-t}u(t)+\delta(t)$ are actually the same singular-signal combination at the switching instant, so they produce the same zero-state response.

---

Flashcards for this section are as follows:

- Why are LTI systems central in the course? ::@:: Because known responses can be transferred systematically to shifted and linearly combined inputs.
- What is the response-transfer principle for an LTI system? ::@:: If an LTI system maps $x_1$ to $y_1$, then shifted and linearly combined versions of $x_1$ map to the corresponding shifted and linearly combined versions of $y_1$.
- What are the differential and integral characteristics of LTIs? ::@:: Differentiating or integrating the input produces the correspondingly differentiated or integrated output under the matching zero-state setting.
- What known pair is used in the lecture's LTI response-transfer example? ::@:: The lecture uses $x_1(t)=e^{-t}u(t)$ and $y_1(t)=\cos(3t)u(t)$.
- What response corresponds to the differentiated input $\frac{d}{dt}x_1(t)=-e^{-t}u(t)+\delta(t)$ in the lecture example? ::@:: The corresponding zero-state response is $\frac{d}{dt}y_1(t)=-3\sin(3t)u(t)+\delta(t)$.
- Why does the identity $e^{-t}\delta(t)=\delta(t)$ matter in the LTI example? ::@:: It shows that only the multiplier value at the switching instant matters in the impulse term.
- Why do $-e^{-t}u(t)+e^{-t}\delta(t)$ and $-e^{-t}u(t)+\delta(t)$ produce the same response? ::@:: Because $e^{-t}\delta(t)=\delta(t)$ makes the impulse terms identical.

## representation methods for linear time-invariant systems

This part asks a practical question: how does one obtain the response of a signal passing through an LTI system? Several representations are useful rather than one single universal method. For continuous-time systems, one may use differential equations derived from physical laws, system functions obtained through Laplace transformation, unit impulse responses, or structural descriptions such as block diagrams. These are different views of the same underlying system.

The continuous-time circuit example is an RLC network driven by an excitation $e(t)$, with the capacitor voltage $v_C(t)$ taken as the output and the inductor current $i_L(t)$ treated as an internal variable. This setup matters because it cleanly separates the quantity we want to observe from the internal quantity that we later eliminate. The constitutive relations are not just formulas to memorize; they encode physical storage behavior. For the capacitor, $i_C(t)=C\frac{dv_C(t)}{dt}$ says that current is proportional to how fast the capacitor voltage changes, so a capacitor resists sudden voltage changes. For the inductor, $v_L(t)=L\frac{di_L(t)}{dt}$ says that voltage is proportional to how fast the inductor current changes, so an inductor resists sudden current changes.

Using the stated reference directions, the network equations become the KVL relation $e(t)=L\frac{di_L(t)}{dt}+v_C(t)$ and the node equation $i_L(t)=\frac{v_C(t)}{R}+C\frac{dv_C(t)}{dt}$. It is helpful to organize the derivation as a two-step elimination problem. First rewrite the model as two coupled first-order equations: $\frac{di_L(t)}{dt}=\frac{e(t)-v_C(t)}{L}$ and $\frac{dv_C(t)}{dt}=\frac{i_L(t)}{C}-\frac{v_C(t)}{RC}$. Then eliminate the internal current $i_L(t)$ by differentiating the second equation and substituting into the first. This yields $LC\frac{d^2v_C(t)}{dt^2}+\frac{L}{R}\frac{dv_C(t)}{dt}+v_C(t)=e(t)$, or equivalently $\frac{d^2v_C(t)}{dt^2}+\frac{1}{RC}\frac{dv_C(t)}{dt}+\frac{1}{LC}v_C(t)=\frac{1}{LC}e(t)$.

The final equation should then be interpreted, not merely written down. It is linear because no nonlinear products of state variables or inputs appear. It is time invariant because all coefficients are constants. It is second order because the highest derivative is second order. This is why the example is useful pedagogically: it shows how physical laws, topology, elimination, and structural interpretation all connect.

Block diagrams provide a second continuous-time representation. The main elementary blocks are adders, multipliers, scalar multipliers, differentiators, integrators, and time-delay elements. An adder is usually drawn as a summing node such as a small circle or a block marked with $\Sigma$; incoming branches may be marked with plus or minus signs to show whether a signal is added or subtracted, and the explicit algebra is $r(t)=e_1(t)+e_2(t)$ or $r(t)=e_1(t)-e_2(t)$. A multiplier is usually drawn as a block or node marked by $\times$ or another product label, and its explicit algebra is $r(t)=e_1(t)e_2(t)$, which is why it is generally nonlinear.

A scalar multiplier is the same operation as a gain element, so the terminology matters. A **gain block** is the dedicated block whose inside label is the gain value, for example a block marked $a$ meaning $r(t)=ae(t)$. A **branch coefficient** means the same gain is written directly on the signal line rather than inside a separate block, again meaning $r(t)=ae(t)$. A **triangle-style gain symbol** is an amplifier-like triangle carrying the gain label; it still means $r(t)=ae(t)$. These are three drawing conventions for the same scalar-multiplication operation, not three different system elements. A differentiator is drawn as a block labeled $\frac{d}{dt}$ with explicit relation $r(t)=\frac{d}{dt}e(t)$, an integrator as a block labeled $\int$ with relation $r(t)=\int_{-\infty}^{t}e(\tau)\,d\tau$, and a time-delay element as a block labeled by the delay $\tau$ or by an expression such as $e(t-\tau)$, meaning $r(t)=e(t-\tau)$.

The discrete-time analogue uses difference equations and block diagrams built from scalar multipliers, adders, and unit-delay elements $z^{-1}$. The scalar multiplier again has multiple acceptable drawing styles: a gain block with coefficient $a$, a branch coefficient written on the sequence line, or a triangle-style gain symbol. In every case the explicit algebra is $y[n]=ax[n]$. The unit-delay element is drawn as a block labeled $z^{-1}$ because, in the z-transform domain, delaying a sequence by one sample corresponds to multiplication by $z^{-1}$. Its explicit time-domain relation is $y[n]=x[n-1]$. Operationally, it behaves like a shift register: it outputs the previous sample while the new sample is shifted in.

The feedforward discrete-time example without feedback is a relation such as $y[n]=\frac{1}{2}x[n]+\frac{1}{2}x[n-1]$. To draw it, split the input into two branches, send one branch directly to an adder, send the other branch through one unit-delay block and a scalar multiplier, and then add the two branches. Because no past output is fed back, the structure is feedforward.

The comparison between backward and forward first-order difference equations is also important. A backward form such as $y[n]=x[n]+ay[n-1]$ is drawn with a feedback branch containing one delay element, because the present output depends on the previous output. A forward form such as $y[n+1]=x[n]+ay[n]$ may represent a similar algebraic relationship after index shifting, but the backward form is preferred for implementation because it expresses the present output in terms of already available values.

For a second-order system such as $y[n]=x[n]-3x[n-2]+5y[n-1]-6y[n-2]$, one may draw multiple structurally different but equivalent diagrams. The common implementation fact is that at least two delay elements are required, because the system depends on values two samples into the past. This is also reflected in the general linear difference-equation form $\sum_{k=0}^{N}a_k y[n-k]=\sum_{r=0}^{M}b_r x[n-r]$, whose order is the difference between the highest and lowest argument values of the dependent variable.

The general linear difference-equation form is

$\sum_{k=0}^{N}a_k y[n-k]=\sum_{r=0}^{M}b_r x[n-r]$.

The order of the difference equation is the difference between the highest and lowest argument values of the dependent variable appearing in the equation. This definition matches the practical memory requirement: the larger the spread in delayed output indices, the more memory elements are needed in implementation.

---

Flashcards for this section are as follows:

- What are the main ways to represent an LTI system when trying to obtain its response? ::@:: The main representations are differential equations, system functions via Laplace transformation, unit impulse responses, and structural descriptions such as block diagrams.
- Given an RLC circuit where the source $e(t)$ feeds an inductor $L$ in series, the node after the inductor is the output node with voltage $v_C(t)$, and a resistor $R$ and capacitor $C$ are both connected from that node to the reference line in parallel, with internal current $i_L(t)$ through the inductor, capacitor law $i_C(t)=C\frac{dv_C(t)}{dt}$, and inductor law $v_L(t)=L\frac{di_L(t)}{dt}$, what physical intuition do the constitutive relations encode and what topology equations are written before elimination? ::@:: The capacitor law says current tracks how fast capacitor voltage changes, so a capacitor resists sudden voltage change; the inductor law says voltage tracks how fast inductor current changes, so an inductor resists sudden current change; the topology equations are $e(t)=L\frac{di_L(t)}{dt}+v_C(t)$ and $i_L(t)=\frac{v_C(t)}{R}+C\frac{dv_C(t)}{dt}$.
- Given the same RLC circuit where the source $e(t)$ feeds an inductor $L$ in series, the output is the node voltage $v_C(t)$ after the inductor, and a resistor $R$ and capacitor $C$ are connected from that node to the reference line in parallel, with equations $e(t)=L\frac{di_L(t)}{dt}+v_C(t)$ and $i_L(t)=\frac{v_C(t)}{R}+C\frac{dv_C(t)}{dt}$, or equivalently $\frac{di_L(t)}{dt}=\frac{e(t)-v_C(t)}{L}$ and $\frac{dv_C(t)}{dt}=\frac{i_L(t)}{C}-\frac{v_C(t)}{RC}$, what equation results after eliminating $i_L(t)$, and what does it tell you structurally? ::@:: Eliminating $i_L(t)$ gives $LC\frac{d^2v_C(t)}{dt^2}+\frac{L}{R}\frac{dv_C(t)}{dt}+v_C(t)=e(t)$, equivalently $\frac{d^2v_C(t)}{dt^2}+\frac{1}{RC}\frac{dv_C(t)}{dt}+\frac{1}{LC}v_C(t)=\frac{1}{LC}e(t)$; this shows the system is linear, time invariant, and second order.
- How are the main continuous-time block-diagram elements drawn, what equations do they represent, and what do the terms gain block, branch coefficient, and triangle-style gain symbol mean? ::@:: An adder is drawn as a summing node or $\Sigma$ block and represents $r(t)=e_1(t)\pm e_2(t)$; a multiplier is drawn as a $\times$ or product block and represents $r(t)=e_1(t)e_2(t)$; a scalar multiplier represents $r(t)=ae(t)$ and may be drawn as a gain block with $a$ inside, as a branch coefficient written directly on the line, or as a triangle-style gain symbol; a differentiator represents $r(t)=\frac{d}{dt}e(t)$, an integrator represents $r(t)=\int_{-\infty}^{t}e(\tau)\,d\tau$, and a delay block represents $r(t)=e(t-\tau)$.
- How are the main discrete-time block-diagram elements drawn, what equations do they represent, and why is the delay labeled $z^{-1}$? ::@:: A discrete-time scalar multiplier represents $y[n]=ax[n]$ and may be drawn as a gain block, a branch coefficient, or a triangle-style gain symbol; the delay block represents $y[n]=x[n-1]$ and is labeled $z^{-1}$ because one-sample delay corresponds to multiplication by $z^{-1}$ in the z-transform domain.
- How is the feedforward example $y[n]=\frac{1}{2}x[n]+\frac{1}{2}x[n-1]$ drawn, and why is it called feedforward? ::@:: Split the input into two branches, send one directly to an adder, send the other through one delay and a scalar multiplier, then add the branches; it is feedforward because the output depends only on present and delayed input samples, not on delayed outputs.
- Why is the backward form $y[n]=x[n]+ay[n-1]$ preferred over the forward form $y[n+1]=x[n]+ay[n]$ for implementation? ::@:: The backward form expresses the present output in terms of already available values and is therefore naturally suited to causal implementation; its block diagram uses one delay in the feedback branch.
- What does the second-order example $y[n]=x[n]-3x[n-2]+5y[n-1]-6y[n-2]$ teach about realization and order? ::@:: It shows that multiple equivalent structural diagrams are possible, but at least two delay elements are required because the system depends on values two samples into the past; more generally the order of $\sum_{k=0}^{N}a_k y[n-k]=\sum_{r=0}^{M}b_r x[n-r]$ is determined by the spread of delayed output indices.

## system analysis viewpoints

The main analysis viewpoint is: first build a mathematical model of the system, then analyze the response under a given input. In other words, the workflow is model first, response second.

Two major model-building viewpoints are presented. The input-output description focuses only on the relationship between excitation and response and ignores internal system variables. It is especially natural for SISO systems, meaning single-input single-output systems: there is one input channel and one output channel, so one higher-order differential or difference equation can often relate them directly. The state-variable viewpoint tracks both the overall response and internal variables such as capacitor voltages or inductor currents. It is naturally suited to MIMO systems, meaning multiple-input multiple-output systems: there may be several input channels, several output channels, and several coupled internal variables, so one usually writes a set of coupled first-order equations instead of one single scalar equation.

The lecture also contrasts time-domain and transform-domain solution methods. Time-domain analysis includes direct solution of differential equations, difference equations, and convolution integrals or sums. Transform-domain analysis introduces Fourier, Laplace, and z-transform viewpoints because they convert many system calculations into simpler algebraic forms.

The overall trajectory of the course follows these transitions repeatedly: from input-output description toward state-variable description, from time-domain analysis toward transform-domain analysis, and from continuous systems toward discrete systems. Throughout, the engineering preference is for systems that are linear, time invariant, causal, and stable.

---

Flashcards for this section are as follows:

- What are the two high-level tasks in system analysis? ::@:: Build a mathematical model of the system and then analyze the output response under a given input.
- What is the input-output description viewpoint? ::@:: It focuses only on the relationship between excitation and response and ignores internal system variables.
- What does SISO mean? ::@:: It means single-input single-output, so the system has one input channel and one output channel.
- Why is the input-output viewpoint natural for SISO systems? ::@:: Because one nth-order differential or difference equation can often relate the single input and single output directly.
- What is the state-variable viewpoint? ::@:: It tracks both the overall response and internal variables such as capacitor voltages or inductor currents.
- What does MIMO mean? ::@:: It means multiple-input multiple-output, so the system may have several input channels and several output channels.
- Why is the state-variable viewpoint useful for MIMO systems? ::@:: Because it naturally represents multiple interacting inputs, outputs, and internal variables through coupled first-order equations.
- What belongs to time-domain analysis? ::@:: Direct solution of differential equations, difference equations, and convolution integrals or sums.
- Why are transform-domain methods introduced? ::@:: They convert many system calculations into simpler algebraic forms.
- What transform-domain viewpoints are highlighted in the lecture summary? ::@:: Fourier, Laplace, and z-transform viewpoints.
- What overall transitions organize the course's systems analysis viewpoint? ::@:: From input-output to state-variable description, from time-domain to transform-domain analysis, and from continuous systems to discrete systems.
- What combination of system properties is especially preferred from an engineering perspective? ::@:: Linear, time-invariant, causal, and stable behavior.
