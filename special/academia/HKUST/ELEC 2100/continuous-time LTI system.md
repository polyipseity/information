---
aliases:
  - ELEC 2100 continuous-time LTI response
  - ELEC 2100 continuous-time LTI system
  - ELEC 2100 continuous-time response
  - ELEC2100 continuous-time LTI response
  - ELEC2100 continuous-time LTI system
  - HKUST ELEC 2100 continuous-time LTI response
  - HKUST ELEC 2100 continuous-time LTI system
  - LTI response
  - continuous-time LTI response
  - continuous-time LTI system
  - continuous-time response
  - impulse response
  - step response
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/continuous-time_LTI_system
  - language/in/English
---

# continuous-time LTI system

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

Continuous-time response analysis asks how a linear time-invariant system reacts to excitation in the time domain before transform methods are introduced. In ELEC 2100, this topic organizes response classifications, initial-state effects, impulse and step response, and the first response criteria that can be read directly from $h(t)$.

---

Flashcards for this section are as follows:

- What is the main question of the continuous-time LTI system note? ::@:: It asks how a continuous-time linear time-invariant system reacts to excitation directly in the time domain before transform methods are used. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- Why is continuous-time response analysis important early in ELEC 2100? ::@:: It organizes response classifications, initial-state effects, impulse and step response, and the first causality/stability tests that can be read directly from $h(t)$. <!--SR:!2026-04-12,4,290!2026-04-12,4,297-->

## time-domain analysis roadmap

The lecture opens by contrasting two modelling viewpoints. The __input-output description__ uses a single higher-order differential equation relating excitation and response directly. The __state-variable description__ uses several coupled first-order equations that also track internal variables. The time-domain treatment begins with the input-output viewpoint because it is the fastest route to direct response analysis.

The time-domain route is kept on purpose even though later transform methods are usually more convenient. Direct solution of differential equations is physically intuitive, keeps the meaning of initial conditions visible, and provides the conceptual foundation for later Laplace-transform methods. In other words, the course is not using time-domain analysis because it is always the shortest calculation, but because it teaches what the symbols mean mechanically and physically.

For a constant-coefficient input-output model such as $a_n r^{(n)}(t)+a_{n-1}r^{(n-1)}(t)+\cdots+a_0r(t)=b_m e^{(m)}(t)+b_{m-1}e^{(m-1)}(t)+\cdots+b_0e(t)$, the lecture recalls the classical decomposition $\text{complete solution} = \text{homogeneous solution} + \text{particular solution}$. Setting the excitation side to zero gives the homogeneous equation. Trying the exponential ansatz $r_h(t)=e^{st}$ leads to the characteristic polynomial $a_n s^n+a_{n-1}s^{n-1}+\cdots+a_0=0$, so the homogeneous solution is assembled from the characteristic roots. The particular solution captures how the external excitation forces the system and is chosen in a form matched to the input family. This is the differential-equation analogue of later zero-input and zero-state splitting.

---

Flashcards for this section are as follows:

- What is the difference between the input-output and state-variable viewpoints in the time-domain roadmap? ::@:: The input-output viewpoint uses one higher-order differential equation relating excitation and response directly, whereas the state-variable viewpoint uses several coupled first-order equations that also track internal variables. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- Why does the time-domain treatment begin with the input-output viewpoint? ::@:: Because it gives the fastest direct route to time-domain response analysis before the course moves to richer state-variable or transform-domain viewpoints. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- Why does the lecture still emphasize direct time-domain solution even though transforms are often more convenient? ::@:: Because direct solution is physically intuitive, keeps the meaning of initial conditions visible, and forms the conceptual foundation for later transform-domain methods. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- What is the standard constant-coefficient input-output model used in the classical time-domain method? ::@:: It is $a_n r^{(n)}(t)+a_{n-1}r^{(n-1)}(t)+\cdots+a_0r(t)=b_m e^{(m)}(t)+b_{m-1}e^{(m-1)}(t)+\cdots+b_0e(t)$. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- What exponential ansatz produces the characteristic equation in the homogeneous problem? ::@:: Substituting $r_h(t)=e^{st}$ into $a_n r^{(n)}(t)+\cdots+a_0r(t)=0$ gives the characteristic polynomial $a_n s^n+a_{n-1}s^{n-1}+\cdots+a_0=0$. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- What is the classical complete-solution decomposition for a constant-coefficient continuous-time differential equation? ::@:: It is $\text{complete solution}=\text{homogeneous solution}+\text{particular solution}$. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- What does the homogeneous solution represent physically? ::@:: It represents the system's natural modes, meaning the part of the motion caused by stored energy and intrinsic system dynamics. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- What does the particular solution represent physically? ::@:: It represents the part of the response forced by the external excitation. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## response classifications

The lecture uses three parallel classification pairs for system responses, and they should not be collapsed into one slogan.

The first split is __zero-input__ versus __zero-state__. If the system equation is written abstractly as $L[r]=M[e]$, then zero-input response is obtained by setting $e=0$, so $L[r_{\mathrm{zi}}]=0$ with the original stored-energy conditions retained. Zero-state response is obtained by setting the initial state to zero while keeping the forcing term, so $L[r_{\mathrm{zs}}]=M[e]$ with zero initial conditions. By linearity, the total response splits as $r(t)=r_{\mathrm{zi}}(t)+r_{\mathrm{zs}}(t)$.

The second split is __natural__ versus __forced__. The natural response emphasizes the system's own modes, while the forced response emphasizes what the external signal imposes. In many standard constant-coefficient examples, the natural response lines up with the homogeneous part and the forced response lines up with the particular part. Even so, the lecture keeps the terminology separate because one classification is organized around source and initial conditions and the other around modal interpretation.

The third split is __transient__ versus __steady-state__. This pair is about time behaviour rather than source. The transient part is the portion that dies away or changes significantly during the adjustment process. The steady-state part is the long-time behaviour that remains after the transient has settled. A zero-state response can therefore still contain both transient and steady-state pieces.

These three pairs answer different questions: zero-input vs zero-state asks what caused the response, natural vs forced asks which dynamical component it represents, and transient vs steady-state asks how it behaves as time evolves.

---

Flashcards for this section are as follows:

- What is the zero-input response? ::@:: It is the response produced when the external input is set to zero and only the system's initial stored energy remains. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the zero-state response? ::@:: It is the response produced when the initial state is set to zero and only the external excitation acts. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- What is the mathematical model for zero-input response in the differential-equation viewpoint? ::@:: It is the solution of the homogeneous differential equation with nonzero initial conditions. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- If the system equation is written as $L[r]=M[e]$, what equations define $r_{\mathrm{zi}}$ and $r_{\mathrm{zs}}$? ::@:: Zero-input response satisfies $L[r_{\mathrm{zi}}]=0$ with the original stored-energy conditions, while zero-state response satisfies $L[r_{\mathrm{zs}}]=M[e]$ with zero initial conditions. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- How does linearity combine zero-input and zero-state response? ::@:: It gives the additive split $r(t)=r_{\mathrm{zi}}(t)+r_{\mathrm{zs}}(t)$. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- What is the difference between natural response and forced response? ::@:: Natural response emphasizes the system's own modes, whereas forced response emphasizes the part imposed by the external excitation. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why does the lecture keep zero-input/zero-state separate from natural/forced even though they often line up in simple examples? ::@:: Because zero-input vs zero-state classifies response by source and initial conditions, whereas natural vs forced classifies response by dynamical interpretation. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- What is the transient response? ::@:: It is the part of the response that dies away or changes significantly during the adjustment process. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- What is the steady-state response? ::@:: It is the long-time behaviour that remains after the transient has settled. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why can a zero-state response still contain both transient and steady-state parts? ::@:: Because zero-state only says the response is caused by the external input, not that the response is already at its long-time form. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- What question does each of the three response-classification pairs answer? ::@:: Zero-input vs zero-state asks what caused the response, natural vs forced asks which dynamical component it represents, and transient vs steady-state asks how it behaves as time evolves. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->

## mapping the response labels to ODE solutions

The different labels are useful only if one can map them cleanly onto the ordinary-differential-equation solution pieces. Suppose the input-output model is $a_n r^{(n)}(t)+a_{n-1}r^{(n-1)}(t)+\cdots+a_0r(t)=b_m e^{(m)}(t)+b_{m-1}e^{(m-1)}(t)+\cdots+b_0e(t)$.

The classical ODE method writes the complete solution as $r(t)=r_h(t)+r_p(t)$, where $r_h$ is the homogeneous solution and $r_p$ is one particular solution of the forced equation. This split is mathematically convenient because it is exactly what the solving algorithm produces. But engineers also want a split by physical cause, and that is the zero-input/zero-state split.

The explicit mapping is as follows.

- __Zero-input response__ $r_{\mathrm{zi}}$: solve the homogeneous ODE with the __actual initial conditions__ and with the input set to zero. So $r_{\mathrm{zi}}$ is always a homogeneous-solution object.
- __Zero-state response__ $r_{\mathrm{zs}}$: solve the full forced ODE with __zero initial conditions__. This is the response caused only by the external excitation.
- __Particular solution__ $r_p$: any one solution of the forced ODE, chosen for algebraic convenience from the input family.
- __Natural response__: the part built from the system's natural modes, so it is made of homogeneous-solution terms.
- __Forced response__: the part tied to the forcing pattern, so it is represented by a particular solution.

The subtle but very important point is that $r_{\mathrm{zs}}$ is generally __not__ equal to $r_p$ by itself. A particular solution usually does not satisfy the required zero initial conditions. Therefore the zero-state response is often written as $r_{\mathrm{zs}}(t)=r_p(t)+r_{h,\mathrm{corr}}(t)$, where $r_{h,\mathrm{corr}}$ is a homogeneous correction chosen so that $r_{\mathrm{zs}}(0^-)=r'_{\mathrm{zs}}(0^-)=\cdots=r^{(n-1)}_{\mathrm{zs}}(0^-)=0$.

This is the missing mapping that often causes confusion. The particular solution represents the forcing pattern, but the zero-state response is the physically correct forced response under zero stored energy, so it may need an additional homogeneous term to enforce the initial-state requirement.

Using this language, the complete response can be written in two equally valid ways: $r(t)=r_h(t)+r_p(t)=r_{\mathrm{zi}}(t)+r_{\mathrm{zs}}(t)$.

These are not contradictory decompositions; they answer different questions. The first is the mathematician's "how do I solve the ODE?" split. The second is the engineer's "what part came from stored energy and what part came from the input?" split.

There is one more useful mapping. When the system is stable and the input is sustained, the homogeneous-mode content usually dies out, so the transient part is often made of homogeneous terms, while the steady-state part is often represented by the long-time part of $r_p$. But this is an asymptotic statement, not an identity that always holds at every time instant. That is why the note keeps transient/steady-state separate from homogeneous/particular and zero-input/zero-state.

The motivation for all these labels is therefore simple:

- use __homogeneous/particular__ to solve the ODE,
- use __zero-input/zero-state__ to separate stored energy from external excitation,
- use __natural/forced__ to identify modal content versus forcing pattern,
- use __transient/steady-state__ to describe what dies out and what persists.

---

Flashcards for this section are as follows:

- For the input-output ODE $a_n r^{(n)}(t)+\cdots+a_0r(t)=b_m e^{(m)}(t)+\cdots+b_0e(t)$, what are the two main complete-response decompositions used in the note? ::@:: The complete response may be written either as $r(t)=r_h(t)+r_p(t)$ in the classical ODE method or as $r(t)=r_{\mathrm{zi}}(t)+r_{\mathrm{zs}}(t)$ in the source-based engineering split. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- How is zero-input response mapped to ODE solution pieces? ::@:: Zero-input response is obtained by solving the homogeneous ODE with the actual initial conditions and with the input set to zero, so it is always a homogeneous-solution object. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- How is zero-state response mapped to ODE solution pieces? ::@:: Zero-state response is obtained by solving the full forced ODE with zero initial conditions, so it is the response caused only by the external excitation. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- How are natural response and forced response mapped to ODE solution pieces? ::@:: Natural response is built from homogeneous-solution terms representing the system's natural modes, whereas forced response is represented by a particular solution tied to the forcing pattern. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- Why is zero-state response generally not equal to the particular solution $r_p$ by itself? ::@:: Because a particular solution usually does not satisfy the required zero initial conditions, so a homogeneous correction term is often needed. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What is the standard correction formula relating zero-state response to a particular solution? ::@:: It is $r_{\mathrm{zs}}(t)=r_p(t)+r_{h,\mathrm{corr}}(t)$, where $r_{h,\mathrm{corr}}$ is chosen so that all required initial conditions of $r_{\mathrm{zs}}$ are zero. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- What initial-condition equations must the homogeneous correction satisfy in the zero-state construction of an nth-order system? ::@:: It must enforce $r_{\mathrm{zs}}(0^-)=r'_{\mathrm{zs}}(0^-)=\cdots=r^{(n-1)}_{\mathrm{zs}}(0^-)=0$. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- Why are the decompositions $r=r_h+r_p$ and $r=r_{\mathrm{zi}}+r_{\mathrm{zs}}$ not contradictory? ::@:: They answer different questions: $r_h+r_p$ is the mathematical ODE-solving split, while $r_{\mathrm{zi}}+r_{\mathrm{zs}}$ is the physical source-based split into stored-energy and excitation-caused parts. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- How do transient and steady-state parts relate to the ODE pieces when the system is stable and the input is sustained? ::@:: The transient part is often made of homogeneous-mode terms that die out, while the steady-state part is often represented by the long-time part of the particular solution, but this is an asymptotic relationship rather than a universal identity at every time. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- What is the motivation for keeping homogeneous/particular, zero-input/zero-state, natural/forced, and transient/steady-state as separate labels? ::@:: They answer different questions respectively about how to solve the ODE, what caused the response, what modal content is present, and what dies out versus what persists. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->

## zero-input and zero-state solution logic

For zero-input response, the input is set to zero, so the system equation becomes homogeneous. The solution therefore contains only the homogeneous part, and the coefficients are determined by the initial conditions. In ordinary situations without impulsive excitation at the initial instant, the state variables satisfy continuity conditions such as capacitor-voltage continuity and inductor-current continuity. In other words, zero-input response answers the question: if the stored energy already present in the system were released with no further forcing, what motion would that energy produce?

For zero-state response, the initial conditions are set to zero, but the original system equation remains active because the external excitation is present. The solution now generally contains both a particular part and a homogeneous part. The homogeneous-looking piece that appears here is not a contradiction: it is the transient needed to satisfy the zero-initial-state constraints while the forced motion develops. If one first guesses a particular solution $r_p$, then the remaining homogeneous correction $r_{h,\mathrm{corr}}$ is chosen precisely so that the total forced response begins from zero stored energy.

The lecture stresses why zero-state analysis becomes the practical default. In many communication and electronic systems, engineers mainly care about how external signals are processed rather than about some previously stored internal energy. That is why convolution becomes central: it computes the zero-state response directly from the input and the impulse response. The motivation is practical system characterization: if the system starts from rest, then the input-output relation is not contaminated by hidden initial energy, so the response reveals the external signal-processing behaviour most cleanly.

---

Flashcards for this section are as follows:

- How is the zero-input response solved in the differential-equation viewpoint? ::@:: Set the input to zero, solve the homogeneous equation, and determine the coefficients from the initial conditions. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why does the zero-input solution contain only the homogeneous part? ::@:: Because once the external excitation is removed, no forcing term remains in the differential equation. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- Under ordinary nonimpulsive excitation, what continuity conditions are usually imposed at the initial instant? ::@:: State variables such as capacitor voltage and inductor current are usually continuous at the initial instant. <!--SR:!2026-04-12,4,297!2026-04-12,4,290-->
- How is the zero-state response solved conceptually before convolution is introduced? ::@:: Set the initial conditions to zero, keep the original forced equation, and solve for the response that satisfies those zero-state constraints. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- Why can the zero-state solution still contain a homogeneous-looking term? ::@:: Because a transient piece is often needed so the total forced response satisfies the zero initial conditions. <!--SR:!2026-04-12,4,297!2026-04-12,4,290-->
- If one first guesses a particular solution $r_p$ for the forced ODE, what is the role of the homogeneous correction in zero-state response? ::@:: The homogeneous correction is chosen so that $r_p+r_{h,\mathrm{corr}}$ satisfies the required zero initial conditions, turning an algebraic forced solution into the physically correct zero-state response. <!--SR:!2026-04-12,4,297!2026-04-12,4,290-->
- Why does the lecture emphasize zero-state response so strongly for engineering systems? ::@:: Because in many communication and electronic systems the main question is how an external signal is processed, not how previously stored internal energy evolves on its own. <!--SR:!2026-04-12,4,290!2026-04-12,4,270-->
- What is the physical motivation for zero-input response? ::@:: It isolates the motion caused solely by previously stored energy, showing what the system would do even if no new forcing were applied. <!--SR:!2026-04-12,4,297!2026-04-12,4,290-->
- What is the physical motivation for zero-state response? ::@:: It isolates the response caused solely by the external excitation under zero stored energy, which is the cleanest way to characterize how the system processes an input signal. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why does convolution become the practical tool for zero-state response? ::@:: It computes the zero-state output directly from the input and the impulse response without separately solving the full differential equation each time. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->

## state continuity and jump discontinuities

The note pauses to explain why initial conditions are usually written without jumps and when that rule fails. A capacitor voltage and an inductor current are state variables because they represent stored electric and magnetic energy. Under ordinary finite excitation, these variables cannot change abruptly: a capacitor resists instantaneous voltage change, and an inductor resists instantaneous current change.

The reason is visible directly from the constitutive relations. For a capacitor, $i_C(t)=C\frac{dv_C(t)}{dt}$.

Integrating across a tiny interval around the initial instant gives $\int_{0^-}^{0^+}i_C(t)\,dt=C\int_{0^-}^{0^+}\frac{dv_C(t)}{dt}\,dt=C\bigl(v_C(0^+)-v_C(0^-)\bigr)$.

If $i_C(t)$ is finite and nonimpulsive, then the left-hand integral over an infinitesimal interval is $0$, so $v_C(0^+)=v_C(0^-)$. Thus capacitor voltage is continuous unless the capacitor current contains an impulse.

For an inductor, $v_L(t)=L\frac{di_L(t)}{dt}$.

Integrating across the same initial interval gives $\int_{0^-}^{0^+}v_L(t)\,dt=L\int_{0^-}^{0^+}\frac{di_L(t)}{dt}\,dt=L\bigl(i_L(0^+)-i_L(0^-)\bigr)$.

If $v_L(t)$ is finite and nonimpulsive, then the left-hand integral is again $0$, so $i_L(0^+)=i_L(0^-)$. Thus inductor current is continuous unless the inductor voltage contains an impulse.

An ideal impulse excitation changes the situation. Because an impulse has finite area concentrated into zero time, it can inject a finite change into a state variable instantaneously. If the capacitor current is $i_C(t)=A\delta(t)$, then the jump formula becomes $C\bigl(v_C(0^+)-v_C(0^-)\bigr)=A$, so $v_C(0^+)-v_C(0^-)=\frac{A}{C}$.

Likewise, if the inductor voltage is $v_L(t)=B\delta(t)$, then $L\bigl(i_L(0^+)-i_L(0^-)\bigr)=B$, so $i_L(0^+)-i_L(0^-)=\frac{B}{L}$.

These equations show exactly how impulse area produces a finite state jump.

The right intuition is not merely "impulses make jumps." The deeper point is that state continuity comes from finite energy-storage laws, while jumps occur only when the forcing is singular enough to overcome that ordinary continuity rule in zero time.

---

Flashcards for this section are as follows:

- Why are capacitor voltage and inductor current treated as state variables? ::@:: Because they directly represent stored electric and magnetic energy and therefore determine part of the system's internal state. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- Why are capacitor voltage and inductor current usually continuous under ordinary excitation? ::@:: A capacitor resists instantaneous voltage change and an inductor resists instantaneous current change, so finite excitation does not change those state variables abruptly. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- How does integrating $i_C(t)=C\frac{dv_C(t)}{dt}$ across $[0^-,0^+]$ prove capacitor-voltage continuity under nonimpulsive current? ::@:: It gives $\int_{0^-}^{0^+}i_C(t)\,dt=C\bigl(v_C(0^+)-v_C(0^-)\bigr)$; if $i_C(t)$ is finite and nonimpulsive, the integral is $0$, so $v_C(0^+)=v_C(0^-)$. <!--SR:!2026-04-12,4,297!2026-04-12,4,290-->
- How does integrating $v_L(t)=L\frac{di_L(t)}{dt}$ across $[0^-,0^+]$ prove inductor-current continuity under nonimpulsive voltage? ::@:: It gives $\int_{0^-}^{0^+}v_L(t)\,dt=L\bigl(i_L(0^+)-i_L(0^-)\bigr)$; if $v_L(t)$ is finite and nonimpulsive, the integral is $0$, so $i_L(0^+)=i_L(0^-)$. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- When can a state variable have a jump discontinuity at the initial instant? ::@:: It can jump when an ideal impulse excitation injects a finite change in zero time. <!--SR:!2026-04-12,4,297!2026-04-12,4,290-->
- Why is an impulse able to create a jump while ordinary finite excitation usually cannot? ::@:: Because an impulse concentrates finite area into zero time, making it singular enough to change a stored-energy variable instantaneously. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- If the capacitor current is $i_C(t)=A\delta(t)$, what jump does the capacitor voltage undergo? ::@:: Integrating $i_C(t)=C\frac{dv_C}{dt}$ gives $C\bigl(v_C(0^+)-v_C(0^-)\bigr)=A$, so $v_C(0^+)-v_C(0^-)=A/C$. <!--SR:!2026-04-12,4,270!2026-04-12,4,290-->
- If the inductor voltage is $v_L(t)=B\delta(t)$, what jump does the inductor current undergo? ::@:: Integrating $v_L(t)=L\frac{di_L}{dt}$ gives $L\bigl(i_L(0^+)-i_L(0^-)\bigr)=B$, so $i_L(0^+)-i_L(0^-)=B/L$. <!--SR:!2026-04-12,4,270!2026-04-12,4,290-->
- What is the deeper lesson behind the jump-discontinuity discussion? ::@:: State continuity is the ordinary rule imposed by energy-storage laws, and jumps are exceptional singular-forcing events rather than the default behaviour. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->

## impulse response and step response

The __unit impulse response__ $h(t)$ is the zero-state response of the system when the excitation is the unit impulse $\delta(t)$. It is called fundamental because, for LTI systems, knowing the response to a shifted impulse lets us build the response to more complicated signals by superposition and time shifting.

The __unit step response__ $g(t)$ is the zero-state response when the excitation is the unit step $u(t)$. It is often easier to visualize experimentally because a step is a practical switching input rather than an idealized singular pulse.

The two are closely related because the step is the accumulated impulse: $u(t)=\int_{-\infty}^{t}\delta(\tau)\,d\tau$, equivalently $\delta(t)=\frac{d}{dt}u(t)$ in the generalized sense. The operator viewpoint therefore gives a first derivation: if $g(t)$ is the zero-state response to $u(t)$, then for a constant-coefficient LTI operator $H$ one has $H[\delta]=H\!\left[\frac{d}{dt}u\right]=\frac{d}{dt}H[u]=\frac{d}{dt}g(t)$. Since $H[\delta]=h(t)$ by definition, this gives $h(t)=\frac{d}{dt}g(t)$.

There is also the convolution derivation. Since $g(t)=(u*h)(t)$, one writes $g(t)=\int_{-\infty}^{\infty}u(\tau)h(t-\tau)\,d\tau$. Because $u(\tau)=0$ for $\tau<0$, this becomes $g(t)=\int_{0}^{\infty}h(t-\tau)\,d\tau$. Now substitute $\lambda=t-\tau$, so when $\tau=0$, $\lambda=t$, and when $\tau\to\infty$, $\lambda\to-\infty$. Therefore $g(t)=\int_{t}^{-\infty}h(\lambda)(-d\lambda)=\int_{-\infty}^{t}h(\lambda)\,d\lambda$.

If the system is causal, then $h(\lambda)=0$ for $\lambda<0$, so this reduces further to $g(t)=\int_{0}^{t}h(\lambda)\,d\lambda$ for $t\ge 0$.

The reverse derivation is just as useful. Starting from $g(t)=\int_{-\infty}^{t}h(\lambda)\,d\lambda$, differentiating with respect to $t$ recovers $h(t)$. So impulse response and step response are not unrelated test outputs; they are differential and integral versions of the same zero-state information.

The ODE viewpoint gives one more mapping. If the input-output model is $L[r]=M[e]$, then the impulse response satisfies $L[h]=M[\delta]$ with zero initial conditions, and the step response satisfies $L[g]=M[u]$ with zero initial conditions. Thus $h$ and $g$ are not just special signals passed through the system; they are the zero-state solutions of two specific forcing problems. The relation between them comes from the relation between $u$ and $\delta$.

The relation is important conceptually. The impulse response measures how the system reacts to a concentrated instant of excitation. The step response measures how the system accumulates or settles when the input is switched on and then kept on.

---

Flashcards for this section are as follows:

- What is the unit impulse response $h(t)$? ::@:: It is the zero-state response of the system to the unit impulse input $\delta(t)$. <!--SR:!2026-04-12,4,290!2026-04-12,4,290-->
- Why is the impulse response fundamental for LTI systems? ::@:: Because responses to shifted impulses can be transferred by time invariance and then superposed by linearity to build responses to more complicated inputs. <!--SR:!2026-04-12,4,297!2026-04-12,4,290-->
- What is the unit step response $g(t)$? ::@:: It is the zero-state response of the system to the unit step input $u(t)$. <!--SR:!2026-04-12,4,270!2026-04-12,4,290-->
- Why is the step response often easier to visualize experimentally than the impulse response? ::@:: A step is a practical switched input, whereas an impulse is an idealized singular pulse. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- What is the relation between the unit step and the unit impulse? ::@:: The step is the accumulated impulse: $u(t)=\int_{-\infty}^{t}\delta(\tau)\,d\tau$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Why does the operator viewpoint imply $h(t)=\frac{d}{dt}g(t)$ for a constant-coefficient LTI system? ::@:: Because $\delta(t)=\frac{d}{dt}u(t)$ and an LTI differential operator commutes with differentiation, so $h=H[\delta]=H[u']=(H[u])'=g'$. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- How are step response and impulse response related for an LTI system? ::@:: They satisfy $g(t)=\int_{-\infty}^{t}h(\tau)\,d\tau$ and, in the generalized-derivative sense, $h(t)=\frac{d}{dt}g(t)$. <!--SR:!2026-04-12,4,270!2026-04-12,4,290-->
- How is the step-response formula $g(t)=\int_{-\infty}^{t}h(\tau)\,d\tau$ derived from convolution? ::@:: Start from $g=u*h$, write $g(t)=\int_{-\infty}^{\infty}u(\tau)h(t-\tau)\,d\tau$, reduce the integral to $\tau\ge 0$, and then substitute $\lambda=t-\tau$ to get $g(t)=\int_{-\infty}^{t}h(\lambda)\,d\lambda$. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- If the system is causal, how does the step-response integral simplify? ::@:: Since $h(\lambda)=0$ for $\lambda<0$, the relation becomes $g(t)=\int_{0}^{t}h(\lambda)\,d\lambda$ for $t\ge 0$. <!--SR:!2026-04-12,4,270!2026-04-12,4,290-->
- Why does differentiating the step response recover the impulse response? ::@:: Because $g(t)=\int_{-\infty}^{t}h(\lambda)\,d\lambda$ is an accumulated-area formula, so in the generalized-derivative sense $\frac{d}{dt}g(t)=h(t)$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- If the input-output model is written as $L[r]=M[e]$, what equations do $h(t)$ and $g(t)$ satisfy? ::@:: The impulse response satisfies $L[h]=M[\delta]$ with zero initial conditions, while the step response satisfies $L[g]=M[u]$ with zero initial conditions. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- What is the intuitive difference between impulse response and step response? ::@:: Impulse response measures reaction to a concentrated instant of excitation, whereas step response measures how the system accumulates or settles after the input is switched on and kept on. <!--SR:!2026-04-12,4,297!2026-04-12,4,290-->

## typical impulse responses and what they mean

The note lists several elementary systems whose impulse responses should be recognized immediately.

For a scalar multiplier $r(t)=ae(t)$, the impulse response is $h(t)=a\delta(t)$. This says the system does nothing except scale the instantaneous input by $a$.

For a differentiator $r(t)=\frac{d}{dt}e(t)$, the impulse response is $h(t)=\delta'(t)$. The derivative of the impulse appears because differentiating the output of a shifted impulse produces the shifted derivative of the impulse. This is a useful reminder that ideal differentiation is a singular operation in the time domain.

For an integrator the input-output law is the accumulated-input relation $r(t)=\int_{-\infty}^{t} e(\tau)\,d\tau$. Its impulse response is $h(t)=u(t)$. A unit impulse therefore produces a unit step, which matches the intuition that integration accumulates the incoming area.

For a delay element $r(t)=e(t-\tau_0)$, the impulse response is $h(t)=\delta(t-\tau_0)$. The system does not reshape the impulse at all; it only shifts it to a later time.

These examples are worth memorizing as a family rather than as isolated formulas. Scaling keeps the impulse at the same instant but changes its weight, differentiation raises the singular order, integration turns the impulse into accumulated history, and delay moves the impulse in time without altering its shape.

---

Flashcards for this section are as follows:

- What is the impulse response of a scalar multiplier $r(t)=ae(t)$, and what does it mean physically? ::@:: Its impulse response is $h(t)=a\delta(t)$, meaning the system simply scales the input instant by the gain $a$. <!--SR:!2026-04-12,4,270!2026-04-12,4,290-->
- What is the impulse response of the differentiator $r(t)=\frac{d}{dt}e(t)$, and what does it tell you conceptually? ::@:: Its impulse response is $h(t)=\delta'(t)$, showing that ideal differentiation is a singular operation that reacts to how sharply the input changes. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- What is the impulse response of the integrator $r(t)=\int_{-\infty}^{t} e(\tau)\,d\tau$, and what intuition does it encode? ::@:: Its impulse response is $h(t)=u(t)$, meaning a unit impulse becomes a unit step because integration accumulates incoming area. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- What is the impulse response of the delay element $r(t)=e(t-\tau_0)$, and what does it mean physically? ::@:: Its impulse response is $h(t)=\delta(t-\tau_0)$, meaning the system preserves the impulse shape and only shifts it later in time. <!--SR:!2026-04-12,4,297!2026-04-12,4,290-->
- What family resemblance should be remembered across the standard impulse-response examples? ::@:: Scaling changes impulse weight, differentiation raises singular order, integration accumulates impulse area into a step, and delay shifts the impulse in time without reshaping it. <!--SR:!2026-04-12,4,270!2026-04-12,4,290-->

## causality and stability from the impulse response

For a continuous-time LTI system, the impulse response immediately reveals two core properties.

The system is __causal__ if and only if the impulse response vanishes before the excitation instant, namely $h(t)=0$ for $t<0$. The intuition is simple: if the system reacts before the impulse is applied, then it must be using future information, which violates causality. A causal impulse response starts at the excitation instant or later, never earlier. Equivalently, in the convolution formula $r_{\mathrm{zs}}(t)=\int_{-\infty}^{\infty}e(\tau)h(t-\tau)\,d\tau$, the condition $h(t-\tau)=0$ for $\tau>t$ forces the output at time $t$ to depend only on present and past input.

The system is __BIBO stable__ if its impulse response is absolutely integrable, that is, $\int_{-\infty}^{\infty} |h(t)|\,dt < \infty$. The standard bound is short and important: if $|e(t)|\le M$ for all $t$, then $|r_{\mathrm{zs}}(t)|=\left|\int_{-\infty}^{\infty}e(\tau)h(t-\tau)\,d\tau\right|\le \int_{-\infty}^{\infty}|e(\tau)|\,|h(t-\tau)|\,d\tau\le M\int_{-\infty}^{\infty}|h(\lambda)|\,d\lambda$. So finite total absolute area of $h$ forces every bounded input to produce a bounded output. If the total absolute mass diverges, bounded inputs can accumulate enough contribution to make the output blow up.

These tests are powerful because they turn abstract system properties into direct reading rules on one signal, $h(t)$.

---

Flashcards for this section are as follows:

- What impulse-response condition characterizes causality for a continuous-time LTI system? ::@:: The system is causal if and only if $h(t)=0$ for $t<0$. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- Why does a nonzero impulse response for $t<0$ imply noncausality? ::@:: Because it would mean the system reacts before the impulse is applied, which requires future information. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- What impulse-response condition characterizes BIBO stability for a continuous-time LTI system? ::@:: The system is BIBO stable if $\int_{-\infty}^{\infty}|h(t)|\,dt<\infty$. <!--SR:!2026-04-12,4,270!2026-04-12,4,297-->
- Why does absolute integrability of $h(t)$ guarantee bounded-input bounded-output stability? ::@:: Because convolution with a bounded input then uses weights whose total absolute mass is finite, so the output cannot grow without bound. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- What convolution inequality proves that absolute integrability of $h(t)$ implies BIBO stability? ::@:: If $|e(t)|\le M$, then $|r_{\mathrm{zs}}(t)|\le M\int_{-\infty}^{\infty}|h(\lambda)|\,d\lambda$, so the output is uniformly bounded whenever the integral is finite. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->
- Why are the causality and stability tests from $h(t)$ so important? ::@:: They let you infer major system properties directly from one signal instead of repeatedly testing many different inputs. <!--SR:!2026-04-12,4,297!2026-04-12,4,297-->

## impulse-response case studies

The summary examples reinforce that impulse response should be interpreted structurally, not just computed formally. In the first example, the input splits into two branches before the integrator: one branch goes directly into the positive summer input, and the other goes through a delay $T$ into the negative summer input. If the excitation is $\delta(t)$, then the signal entering the integrator is $\delta(t)-\delta(t-T)$. Integrating this gives $h(t)=u(t)-u(t-T)$, which is a unit-height rectangular pulse on $0\le t<T$. The picture is intuitive: the impulse turns the integrator on at $t=0$, and the delayed negative impulse turns it off again at $t=T$.

The later causality-and-stability example uses $h(t)=e^{-2t}u(t)$. Causality is immediate because the step factor makes the response zero for all $t<0$. Stability is also immediate because the exponential decays fast enough for the total absolute area to be finite: $\int_{-\infty}^{\infty}|h(t)|\,dt=\int_{0}^{\infty}e^{-2t}\,dt=1/2$. The example is simple, but it shows exactly how the general impulse-response tests are meant to be used in practice.

---

Flashcards for this section are as follows:

- Worked example: In the continuous-time system whose input splits into a direct positive branch and a delayed negative branch of delay $T$ before an integrator, what signal enters the integrator when the input is $\delta(t)$, and what impulse response follows? ::@:: Step 1: the direct positive branch contributes $\delta(t)$. <br/> Step 2: the delayed negative branch contributes $-\delta(t-T)$. <br/> Step 3: therefore the integrator input is $\delta(t)-\delta(t-T)$. <br/> Step 4: integrate term by term to get $h(t)=u(t)-u(t-T)$. <!--SR:!2026-04-12,4,290!2026-04-12,4,270-->
- Why does the impulse response $h(t)=u(t)-u(t-T)$ make intuitive sense for the delayed-subtraction-plus-integrator example? ::@:: The impulse at $t=0$ turns the integrator output on, and the delayed negative impulse at $t=T$ turns it off again, producing a rectangular pulse of width $T$. <!--SR:!2026-04-12,4,297!2026-04-12,4,270-->
- Worked example: Given $h(t)=e^{-2t}u(t)$, why is the system causal? ::@:: Step 1: inspect the support factor $u(t)$. <br/> Step 2: for every $t<0$, $u(t)=0$, so $h(t)=e^{-2t}u(t)=0$. <br/> Step 3: therefore the impulse response vanishes before the excitation instant, so the system is causal. <!--SR:!2026-04-12,4,270!2026-04-12,4,290-->
- Worked example: Given $h(t)=e^{-2t}u(t)$, why is the system stable? ::@:: Step 1: apply the BIBO stability test $\int_{-\infty}^{\infty}|h(t)|\,dt<\infty$. <br/> Step 2: since $u(t)$ kills the negative-time part, the integral reduces to $\int_{0}^{\infty}e^{-2t}\,dt$. <br/> Step 3: evaluate it as $[-\tfrac12 e^{-2t}]_{0}^{\infty}=\tfrac12$. <br/> Step 4: because the result is finite, the system is stable. <!--SR:!2026-04-12,4,290!2026-04-12,4,297-->
- What practical lesson do these continuous-time examples teach about impulse response? ::@:: They show that impulse response should be read structurally and physically: branch delays and signs shape the waveform, and causality/stability tests are checked directly from the support and total area of $h(t)$. <!--SR:!2026-04-12,4,290!2026-04-12,4,270-->
