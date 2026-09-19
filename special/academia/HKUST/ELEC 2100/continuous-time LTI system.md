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

Continuous-time response analysis asks how a linear time-invariant (LTI) system reacts to excitation in the time domain, before transform methods are introduced. This note covers response classifications, initial-state effects, impulse and step response, and causality/stability tests readable from $h(t)$.

---

Flashcards for this section are as follows:

- What is the main question of this note? ::@:: How a continuous-time LTI system reacts to excitation in the time domain, before transform methods. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## time-domain analysis roadmap

The __input-output description__ uses a single higher-order differential equation relating excitation and response. The __state-variable description__ uses several coupled first-order equations that also track internal variables. The time-domain treatment starts with input-output because it is the fastest route to response analysis.

The time-domain route is kept even though later transform methods are usually more convenient. Direct solution of differential equations is physically intuitive, keeps initial conditions visible, and builds the foundation for Laplace-transform methods. The course uses time-domain analysis not because it is always the shortest calculation, but because it teaches what the symbols mean.

For a constant-coefficient input-output model such as $a_n r^{(n)}(t)+a_{n-1}r^{(n-1)}(t)+\cdots+a_0r(t)=b_m e^{(m)}(t)+b_{m-1}e^{(m-1)}(t)+\cdots+b_0e(t)$, the classical decomposition is $\text{complete solution} = \text{homogeneous solution} + \text{particular solution}$. Setting the excitation to zero gives the homogeneous equation. Trying $r_h(t)=e^{st}$ gives the characteristic polynomial $a_n s^n+a_{n-1}s^{n-1}+\cdots+a_0=0$, so the homogeneous solution is assembled from the characteristic roots. The particular solution captures how the external excitation forces the system and is chosen to match the input family. This is the differential-equation analogue of later zero-input and zero-state splitting.

---

Flashcards for this section are as follows:

- What is the difference between input-output and state-variable descriptions? ::@:: Input-output uses one higher-order differential equation relating excitation and response. State-variable uses several coupled first-order equations that also track internal variables. <!--SR:!fsrs,2027-09-07T00:00:00.000Z,406,405.65740649,1,2,7,0,0,2026-07-28T00:00:00.000Z!fsrs,2027-05-07T00:00:00.000Z,300,300.01984473,1,2,7,0,0,2026-07-11T00:00:00.000Z-->
- Why start with the input-output viewpoint? ::@:: It gives the fastest route to time-domain response analysis. <!--SR:!fsrs,2027-09-13T00:00:00.000Z,410,410.22837316,1,2,7,0,0,2026-07-30T00:00:00.000Z!fsrs,2027-04-05T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-05T00:00:00.000Z-->
- Why use time-domain analysis when transforms are often more convenient? ::@:: Because direct solution is physically intuitive, keeps initial conditions visible, and forms the foundation for transform methods. <!--SR:!fsrs,2027-09-01T00:00:00.000Z,401,401.07868927,1,2,7,0,0,2026-07-27T00:00:00.000Z!fsrs,2027-09-01T00:00:00.000Z,401,401.07868927,1,2,7,0,0,2026-07-27T00:00:00.000Z-->
- What is the standard constant-coefficient input-output model? ::@:: $a_n r^{(n)}(t)+a_{n-1}r^{(n-1)}(t)+\cdots+a_0r(t)=b_m e^{(m)}(t)+b_{m-1}e^{(m-1)}(t)+\cdots+b_0e(t)$. <!--SR:!fsrs,2027-05-12T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-12T00:00:00.000Z!fsrs,2027-09-13T00:00:00.000Z,410,410.22837316,1,2,7,0,0,2026-07-30T00:00:00.000Z-->
- What exponential form produces the characteristic equation? ::@:: Substituting $r_h(t)=e^{st}$ gives $a_n s^n+a_{n-1}s^{n-1}+\cdots+a_0=0$. <!--SR:!fsrs,2027-09-07T00:00:00.000Z,406,405.65740649,1,2,7,0,0,2026-07-28T00:00:00.000Z!fsrs,2027-05-02T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-10T00:00:00.000Z-->
- What is the classical complete-solution decomposition? ::@:: $\text{complete solution}=\text{homogeneous solution}+\text{particular solution}$. <!--SR:!fsrs,2027-05-28T00:00:00.000Z,317,317.09832588,1,2,7,0,0,2026-07-15T00:00:00.000Z!fsrs,2027-08-21T00:00:00.000Z,392,391.89755234,1,2,7,0,0,2026-07-25T00:00:00.000Z-->
- What does the homogeneous solution represent? ::@:: The system's natural modes — the motion caused by stored energy. <!--SR:!fsrs,2027-05-18T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-13T00:00:00.000Z!fsrs,2027-09-07T00:00:00.000Z,406,405.65740649,1,2,7,0,0,2026-07-28T00:00:00.000Z-->
- What does the particular solution represent? ::@:: The part of the response forced by the external excitation. <!--SR:!fsrs,2027-05-02T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-04-21T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-08T00:00:00.000Z-->

## response classifications

The lecture uses three classification pairs for system responses.

The first split is __zero-input__ versus __zero-state__. If $L[r]=M[e]$, zero-input response sets $e=0$, so $L[r_{\mathrm{zi}}]=0$ with the original stored-energy conditions. Zero-state response sets the initial state to zero, so $L[r_{\mathrm{zs}}]=M[e]$. By linearity, $r(t)=r_{\mathrm{zi}}(t)+r_{\mathrm{zs}}(t)$.

The second split is __natural__ versus __forced__. Natural response captures the system's own modes; forced response captures what the external signal imposes. In constant-coefficient examples, natural response lines up with the homogeneous part and forced response with the particular part. But the terminology stays separate because one is organized around source and initial conditions and the other around modal interpretation.

The third split is __transient__ versus __steady-state__. This pair is about time behaviour. The transient part dies away during adjustment. The steady-state part remains after the transient has settled. A zero-state response can contain both.

These pairs answer different questions: zero-input vs zero-state asks what caused the response, natural vs forced asks which dynamical component it represents, and transient vs steady-state asks how it behaves over time.

---

Flashcards for this section are as follows:

- What is zero-input response? ::@:: Response when the external input is zero and only the system's initial stored energy remains. <!--SR:!fsrs,2027-05-02T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-10T00:00:00.000Z!fsrs,2027-05-23T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-14T00:00:00.000Z-->
- What is zero-state response? ::@:: Response when the initial state is zero and only the external excitation acts. <!--SR:!fsrs,2027-09-01T00:00:00.000Z,401,401.07868927,1,2,7,0,0,2026-07-27T00:00:00.000Z!fsrs,2027-05-07T00:00:00.000Z,300,300.01984473,1,2,7,0,0,2026-07-11T00:00:00.000Z-->
- What is zero-input response in the differential-equation viewpoint? ::@:: Solution of the homogeneous ODE with nonzero initial conditions. <!--SR:!fsrs,2027-09-03T00:00:00.000Z,401,401.07868927,1,2,7,0,0,2026-07-29T00:00:00.000Z!fsrs,2027-08-23T00:00:00.000Z,392,391.89755234,1,2,7,0,0,2026-07-27T00:00:00.000Z-->
- For $L[r]=M[e]$, what equations define $r_{\mathrm{zi}}$ and $r_{\mathrm{zs}}$? ::@:: $L[r_{\mathrm{zi}}]=0$ with stored-energy conditions; $L[r_{\mathrm{zs}}]=M[e]$ with zero initial conditions. <!--SR:!fsrs,2027-01-28T00:00:00.000Z,216,216.23934371,1.98030797,2,7,0,0,2026-06-26T00:00:00.000Z!fsrs,2027-09-12T00:00:00.000Z,410,410.22837316,1,2,7,0,0,2026-07-29T00:00:00.000Z-->
- How does linearity combine them? ::@:: $r(t)=r_{\mathrm{zi}}(t)+r_{\mathrm{zs}}(t)$. <!--SR:!fsrs,2027-08-13T00:00:00.000Z,382,382.34427331,1,2,7,0,0,2026-07-27T00:00:00.000Z!fsrs,2027-08-06T00:00:00.000Z,378,377.84950691,1,2,7,0,0,2026-07-24T00:00:00.000Z-->
- What is the difference between natural and forced response? ::@:: Natural response is the system's own modes; forced response is the part imposed by the external excitation. <!--SR:!fsrs,2027-04-16T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-07T00:00:00.000Z!fsrs,2027-06-13T00:00:00.000Z,330,329.81882824,1,2,7,0,0,2026-07-18T00:00:00.000Z-->
- Why keep zero-input/zero-state separate from natural/forced? ::@:: Zero-input vs zero-state classifies by source and initial conditions; natural vs forced classifies by dynamical interpretation. <!--SR:!fsrs,2027-08-26T00:00:00.000Z,396,396.49212694,1,2,7,0,0,2026-07-26T00:00:00.000Z!fsrs,2027-05-18T00:00:00.000Z,309,308.57643926,1,2,7,0,0,2026-07-13T00:00:00.000Z-->
- What is transient response? ::@:: The part that dies away during adjustment. <!--SR:!fsrs,2027-09-09T00:00:00.000Z,406,405.65740649,1,2,7,0,0,2026-07-30T00:00:00.000Z!fsrs,2027-09-01T00:00:00.000Z,401,401.07868927,1,2,7,0,0,2026-07-27T00:00:00.000Z-->
- What is steady-state response? ::@:: The long-time behaviour after the transient has settled. <!--SR:!fsrs,2027-04-21T00:00:00.000Z,287,287.11697064,1,2,7,0,0,2026-07-08T00:00:00.000Z!fsrs,2027-06-02T00:00:00.000Z,321,321.346657,1,2,7,0,0,2026-07-16T00:00:00.000Z-->
- Why can zero-state response contain both transient and steady-state parts? ::@:: Zero-state only means the response is caused by the external input, not that it is already at its long-time form. <!--SR:!fsrs,2027-08-21T00:00:00.000Z,392,391.89755234,1,2,7,0,0,2026-07-25T00:00:00.000Z!fsrs,2027-08-10T00:00:00.000Z,383,382.68390242,1,2,7,0,0,2026-07-23T00:00:00.000Z-->
- What question does each pair answer? ::@:: Zero-input vs zero-state: what caused it. Natural vs forced: which dynamical component. Transient vs steady-state: how it behaves over time. <!--SR:!fsrs,2027-09-01T00:00:00.000Z,401,401.07868927,1,2,7,0,0,2026-07-27T00:00:00.000Z!fsrs,2027-04-26T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-09T00:00:00.000Z-->

## mapping the response labels to ODE solutions

The labels are useful only if one can map them onto ODE solution pieces. Suppose the input-output model is $a_n r^{(n)}(t)+a_{n-1}r^{(n-1)}(t)+\cdots+a_0r(t)=b_m e^{(m)}(t)+b_{m-1}e^{(m-1)}(t)+\cdots+b_0e(t)$.

The classical ODE method writes the complete solution as $r(t)=r_h(t)+r_p(t)$, where $r_h$ is the homogeneous solution and $r_p$ is one particular solution. This split is what the solving algorithm produces. But engineers also want a split by physical cause — the zero-input/zero-state split.

The mapping:

- __Zero-input response__ $r_{\mathrm{zi}}$: solve the homogeneous ODE with the __actual initial conditions__ and input set to zero. Always a homogeneous-solution object.
- __Zero-state response__ $r_{\mathrm{zs}}$: solve the full forced ODE with __zero initial conditions__. Response caused only by the external excitation.
- __Particular solution__ $r_p$: any one solution of the forced ODE, chosen for algebraic convenience.
- __Natural response__: built from the system's natural modes (homogeneous-solution terms).
- __Forced response__: tied to the forcing pattern (a particular solution).

The key point is that $r_{\mathrm{zs}}$ is generally __not__ equal to $r_p$. A particular solution usually does not satisfy zero initial conditions. So the zero-state response is often written as $r_{\mathrm{zs}}(t)=r_p(t)+r_{h,\mathrm{corr}}(t)$, where $r_{h,\mathrm{corr}}$ is a homogeneous correction chosen so that $r_{\mathrm{zs}}(0^-)=r'_{\mathrm{zs}}(0^-)=\cdots=r^{(n-1)}_{\mathrm{zs}}(0^-)=0$.

This is the mapping that often causes confusion. The particular solution represents the forcing pattern, but zero-state response is the physically correct forced response under zero stored energy, so it may need an extra homogeneous term to enforce the initial-state requirement.

The complete response can be written two ways: $r(t)=r_h(t)+r_p(t)=r_{\mathrm{zi}}(t)+r_{\mathrm{zs}}(t)$. They are not contradictory; they answer different questions. The first is the mathematician's "how do I solve the ODE?" split. The second is the engineer's "what part came from stored energy?" split.

One more mapping: when the system is stable and the input is sustained, the homogeneous-mode content usually dies out, so the transient is often made of homogeneous terms while the steady-state is often the long-time part of $r_p$. But this is asymptotic, not an identity at every time. That is why the note keeps transient/steady-state separate from homogeneous/particular and zero-input/zero-state.

Summary of label purposes:

- __homogeneous/particular__: solve the ODE
- __zero-input/zero-state__: separate stored energy from external excitation
- __natural/forced__: identify modal content vs forcing pattern
- __transient/steady-state__: what dies out vs what persists

---

Flashcards for this section are as follows:

- What are the two main complete-response decompositions? ::@:: $r(t)=r_h(t)+r_p(t)$ (classical ODE method) or $r(t)=r_{\mathrm{zi}}(t)+r_{\mathrm{zs}}(t)$ (source-based engineering split). <!--SR:!fsrs,2027-04-10T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-06T00:00:00.000Z!fsrs,2027-09-12T00:00:00.000Z,410,410.22837316,1,2,7,0,0,2026-07-29T00:00:00.000Z-->
- How are zero-input, zero-state, natural, and forced responses mapped to ODE pieces? ::@:: Zero-input: homogeneous ODE with actual initial conditions. Zero-state: full forced ODE with zero initial conditions. Natural: homogeneous-solution terms. Forced: particular solution. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How is zero-input response mapped to ODE pieces? ::@:: Solve the homogeneous ODE with the actual initial conditions and input set to zero. Always a homogeneous-solution object. <!--SR:!fsrs,2027-07-27T00:00:00.000Z,369,368.83580909,1,2,7,0,0,2026-07-23T00:00:00.000Z!fsrs,2027-08-06T00:00:00.000Z,378,377.84950691,1,2,7,0,0,2026-07-24T00:00:00.000Z-->
- How is zero-state response mapped to ODE pieces? ::@:: Solve the full forced ODE with zero initial conditions. Response caused only by the external excitation. <!--SR:!fsrs,2027-09-14T00:00:00.000Z,410,410.22837316,1,2,7,0,0,2026-07-31T00:00:00.000Z!fsrs,2027-09-08T00:00:00.000Z,406,405.65740649,1,2,7,0,0,2026-07-29T00:00:00.000Z-->
- How are natural and forced responses mapped to ODE pieces? ::@:: Natural response is built from homogeneous-solution terms (the system's natural modes). Forced response is represented by a particular solution tied to the forcing pattern. <!--SR:!fsrs,2027-04-16T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-07T00:00:00.000Z!fsrs,2027-08-26T00:00:00.000Z,396,396.49212694,1,2,7,0,0,2026-07-26T00:00:00.000Z-->
- Why is zero-state response generally not equal to $r_p$? ::@:: A particular solution usually does not satisfy zero initial conditions, so a homogeneous correction is often needed. <!--SR:!fsrs,2027-06-08T00:00:00.000Z,326,325.58679272,1,2,7,0,0,2026-07-17T00:00:00.000Z!fsrs,2027-05-12T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-12T00:00:00.000Z-->
- What is the correction formula for zero-state response? ::@:: $r_{\mathrm{zs}}(t)=r_p(t)+r_{h,\mathrm{corr}}(t)$, where $r_{h,\mathrm{corr}}$ enforces $r_{\mathrm{zs}}(0^-)=r'_{\mathrm{zs}}(0^-)=\cdots=r^{(n-1)}_{\mathrm{zs}}(0^-)=0$. <!--SR:!fsrs,2027-04-16T00:00:00.000Z,283,282.79716409,1,2,7,0,0,2026-07-07T00:00:00.000Z!fsrs,2027-09-12T00:00:00.000Z,410,410.22837316,1,2,7,0,0,2026-07-29T00:00:00.000Z-->
- What initial-condition equations must the homogeneous correction satisfy? ::@:: $r_{\mathrm{zs}}(0^-)=r'_{\mathrm{zs}}(0^-)=\cdots=r^{(n-1)}_{\mathrm{zs}}(0^-)=0$. <!--SR:!fsrs,2027-05-07T00:00:00.000Z,300,300.01984473,1,2,7,0,0,2026-07-11T00:00:00.000Z!fsrs,2027-08-26T00:00:00.000Z,396,396.49212694,1,2,7,0,0,2026-07-26T00:00:00.000Z-->
- Why are $r=r_h+r_p$ and $r=r_{\mathrm{zi}}+r_{\mathrm{zs}}$ not contradictory? ::@:: They answer different questions: mathematical ODE-solving vs physical source-based split. <!--SR:!fsrs,2027-08-21T00:00:00.000Z,392,391.89755234,1,2,7,0,0,2026-07-25T00:00:00.000Z!fsrs,2027-06-13T00:00:00.000Z,330,329.81882824,1,2,7,0,0,2026-07-18T00:00:00.000Z-->
- How do transient and steady-state relate to ODE pieces when the system is stable? ::@:: The transient is often made of homogeneous-mode terms that die out; the steady-state is often the long-time part of $r_p$. But this is asymptotic, not an identity at every time. <!--SR:!fsrs,2027-09-12T00:00:00.000Z,410,410.22837316,1,2,7,0,0,2026-07-29T00:00:00.000Z!fsrs,2027-09-12T00:00:00.000Z,410,410.22837316,1,2,7,0,0,2026-07-29T00:00:00.000Z-->
- What is the motivation for keeping all these labels? ::@:: They answer different questions: how to solve the ODE, what caused the response, what modal content is present, and what dies out vs persists. <!--SR:!fsrs,2027-09-12T00:00:00.000Z,410,410.22837316,1,2,7,0,0,2026-07-29T00:00:00.000Z!fsrs,2027-09-07T00:00:00.000Z,406,405.65740649,1,2,7,0,0,2026-07-28T00:00:00.000Z-->

## zero-input and zero-state solution logic

For zero-input response, the input is zero, so the equation is homogeneous. The solution contains only the homogeneous part, with coefficients set by the initial conditions. Under ordinary (nonimpulsive) excitation, state variables satisfy continuity conditions — capacitor voltage and inductor current cannot jump. Zero-input response answers: if the stored energy were released with no forcing, what motion would result?

For zero-state response, initial conditions are zero but the equation stays active with the excitation. The solution generally contains both a particular part and a homogeneous part. The homogeneous-looking piece is not a contradiction: it is the transient needed so the total forced response starts from zero stored energy. If one guesses $r_p$, the correction $r_{h,\mathrm{corr}}$ ensures the total begins from zero.

Zero-state analysis is the practical default because in many systems engineers care about how external signals are processed, not stored energy. Convolution computes the zero-state response directly from the input and impulse response. Starting from rest means no hidden initial energy contaminates the input-output relation.

---

Flashcards for this section are as follows:

- How is zero-input response solved? ::@:: Set the input to zero, solve the homogeneous equation, determine coefficients from initial conditions. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does zero-input solution contain only the homogeneous part? ::@:: No forcing term remains when the excitation is removed. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Under ordinary excitation, what continuity conditions hold at the initial instant? ::@:: Capacitor voltage and inductor current are continuous. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How is zero-state response solved before convolution? ::@:: Set initial conditions to zero, keep the forced equation, solve for the response satisfying those constraints. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why can zero-state solution contain a homogeneous-looking term? ::@:: A transient piece is needed so the total forced response satisfies zero initial conditions. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the role of the homogeneous correction in zero-state response? ::@:: It ensures $r_p+r_{h,\mathrm{corr}}$ satisfies the required zero initial conditions. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the physical motivation for zero-input response? ::@:: It shows the motion produced only by stored energy, with no external forcing. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the physical motivation for zero-state response? ::@:: It isolates the response caused only by the external excitation under zero stored energy. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does the lecture emphasize zero-state response for engineering systems? ::@:: In many systems engineers care about how external signals are processed, not stored energy. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does convolution become the practical tool for zero-state response? ::@:: It computes the zero-state output directly from the input and impulse response without solving the full differential equation each time. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## state continuity and jump discontinuities

Capacitor voltage and inductor current are state variables because they store electric and magnetic energy. Under ordinary finite excitation, they cannot change abruptly: a capacitor resists instantaneous voltage change, and an inductor resists instantaneous current change.

This follows from the constitutive relations. For a capacitor, $i_C(t)=C\frac{dv_C(t)}{dt}$.

Integrating across $[0^-,0^+]$ gives $\int_{0^-}^{0^+}i_C(t)\,dt=C\bigl(v_C(0^+)-v_C(0^-)\bigr)$. If $i_C(t)$ is finite and nonimpulsive, the left integral is $0$, so $v_C(0^+)=v_C(0^-)$. Capacitor voltage is continuous unless the current contains an impulse.

For an inductor, $v_L(t)=L\frac{di_L(t)}{dt}$.

Integrating gives $\int_{0^-}^{0^+}v_L(t)\,dt=L\bigl(i_L(0^+)-i_L(0^-)\bigr)$. If $v_L(t)$ is finite and nonimpulsive, $i_L(0^+)=i_L(0^-)$. Inductor current is continuous unless the voltage contains an impulse.

An impulse can change this. Because an impulse has finite area in zero time, it can inject a finite change into a state variable. If $i_C(t)=A\delta(t)$, then $C\bigl(v_C(0^+)-v_C(0^-)\bigr)=A$, so $v_C(0^+)-v_C(0^-)=\frac{A}{C}$.

Likewise, if $v_L(t)=B\delta(t)$, then $L\bigl(i_L(0^+)-i_L(0^-)\bigr)=B$, so $i_L(0^+)-i_L(0^-)=\frac{B}{L}$.

The intuition: state continuity comes from finite energy-storage laws. Jumps occur only when the forcing is singular enough to overcome that rule in zero time.

---

Flashcards for this section are as follows:

- Why are capacitor voltage and inductor current state variables? ::@:: They store the system's electric and magnetic energy. <!--SR:!fsrs,2027-08-20T00:00:00.000Z,392,391.89755234,1,2,7,0,0,2026-07-24T00:00:00.000Z!fsrs,2027-04-26T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-09T00:00:00.000Z-->
- Why are they usually continuous? ::@:: A capacitor resists instantaneous voltage change; an inductor resists instantaneous current change. <!--SR:!fsrs,2027-08-15T00:00:00.000Z,387,387.29485933,1,2,7,0,0,2026-07-24T00:00:00.000Z!fsrs,2027-08-26T00:00:00.000Z,396,396.49212694,1,2,7,0,0,2026-07-26T00:00:00.000Z-->
- How does integrating $i_C(t)=C\frac{dv_C(t)}{dt}$ across $[0^-,0^+]$ prove continuity? ::@:: It gives $C\bigl(v_C(0^+)-v_C(0^-)\bigr)=\int_{0^-}^{0^+}i_C(t)\,dt$; if the current is finite and nonimpulsive, the integral is $0$, so $v_C(0^+)=v_C(0^-)$. <!--SR:!fsrs,2027-09-03T00:00:00.000Z,401,401.07868927,1,2,7,0,0,2026-07-29T00:00:00.000Z!fsrs,2027-08-06T00:00:00.000Z,378,377.84950691,1,2,7,0,0,2026-07-24T00:00:00.000Z-->
- How does integrating $v_L(t)=L\frac{di_L(t)}{dt}$ across $[0^-,0^+]$ prove continuity? ::@:: It gives $L\bigl(i_L(0^+)-i_L(0^-)\bigr)=\int_{0^-}^{0^+}v_L(t)\,dt$; if the voltage is finite and nonimpulsive, $i_L(0^+)=i_L(0^-)$. <!--SR:!fsrs,2027-08-02T00:00:00.000Z,373,373.34672418,1,2,7,0,0,2026-07-25T00:00:00.000Z!fsrs,2027-08-11T00:00:00.000Z,382,382.34427331,1,2,7,0,0,2026-07-25T00:00:00.000Z-->
- When can a state variable jump? ::@:: When an impulse excitation injects a finite change in zero time. <!--SR:!fsrs,2027-09-09T00:00:00.000Z,406,405.65740649,1,2,7,0,0,2026-07-30T00:00:00.000Z!fsrs,2027-08-28T00:00:00.000Z,396,395.78179232,1,2,7,0,0,2026-07-28T00:00:00.000Z-->
- Why can an impulse create a jump? ::@:: It concentrates finite area into zero time, making it singular enough to change a stored-energy variable instantaneously. <!--SR:!fsrs,2027-08-26T00:00:00.000Z,396,396.49212694,1,2,7,0,0,2026-07-26T00:00:00.000Z!fsrs,2027-04-10T00:00:00.000Z,278,278.46760619,1,2,7,0,0,2026-07-06T00:00:00.000Z-->
- If $i_C(t)=A\delta(t)$, what is the capacitor voltage jump? ::@:: $v_C(0^+)-v_C(0^-)=A/C$. <!--SR:!fsrs,2027-05-12T00:00:00.000Z,304,304.30256839,1,2,7,0,0,2026-07-12T00:00:00.000Z!fsrs,2027-08-11T00:00:00.000Z,382,382.34427331,1,2,7,0,0,2026-07-25T00:00:00.000Z-->
- If $v_L(t)=B\delta(t)$, what is the inductor current jump? ::@:: $i_L(0^+)-i_L(0^-)=B/L$. <!--SR:!fsrs,2027-06-02T00:00:00.000Z,321,321.346657,1,2,7,0,0,2026-07-16T00:00:00.000Z!fsrs,2027-08-11T00:00:00.000Z,382,382.34427331,1,2,7,0,0,2026-07-25T00:00:00.000Z-->
- What is the key lesson? ::@:: State continuity is the ordinary rule from energy-storage laws; jumps are exceptional singular-forcing events. <!--SR:!fsrs,2027-05-07T00:00:00.000Z,300,300.01984473,1,2,7,0,0,2026-07-11T00:00:00.000Z!fsrs,2027-09-12T00:00:00.000Z,410,410.22837316,1,2,7,0,0,2026-07-29T00:00:00.000Z-->

## impulse response and step response

The __unit impulse response__ $h(t)$ is the zero-state response to $\delta(t)$. For LTI systems, the response to a shifted impulse lets us build responses to more complicated signals by superposition and time shifting.

The __unit step response__ $g(t)$ is the zero-state response to $u(t)$. It is often easier to visualize because a step is a practical switching input.

The two are closely related: the step is the accumulated impulse, $u(t)=\int_{-\infty}^{t}\delta(\tau)\,d\tau$, equivalently $\delta(t)=\frac{d}{dt}u(t)$. The operator viewpoint gives one derivation: for a constant-coefficient LTI operator $H$, $H[\delta]=H\!\left[\frac{d}{dt}u\right]=\frac{d}{dt}H[u]=\frac{d}{dt}g(t)$, so $h(t)=\frac{d}{dt}g(t)$.

The convolution derivation: since $g(t)=(u*h)(t)$, write $g(t)=\int_{-\infty}^{\infty}u(\tau)h(t-\tau)\,d\tau$. Because $u(\tau)=0$ for $\tau<0$, this becomes $g(t)=\int_{0}^{\infty}h(t-\tau)\,d\tau$. Substituting $\lambda=t-\tau$ gives $g(t)=\int_{-\infty}^{t}h(\lambda)\,d\lambda$.

For causal systems, $h(\lambda)=0$ for $\lambda<0$, so $g(t)=\int_{0}^{t}h(\lambda)\,d\lambda$ for $t\ge 0$.

The reverse also holds: differentiating $g(t)=\int_{-\infty}^{t}h(\lambda)\,d\lambda$ recovers $h(t)$. So impulse response and step response are integral and derivative versions of the same zero-state information.

The ODE viewpoint: if $L[r]=M[e]$, then $L[h]=M[\delta]$ and $L[g]=M[u]$, both with zero initial conditions. So $h$ and $g$ are the zero-state solutions of two specific forcing problems.

Impulse response measures reaction to a concentrated instant of excitation. Step response measures how the system accumulates or settles when the input is switched on and kept on.

---

Flashcards for this section are as follows:

- What is the unit impulse response $h(t)$? ::@:: The zero-state response to $\delta(t)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the unit step response $g(t)$? ::@:: The zero-state response to $u(t)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the relation between step and impulse? ::@:: $u(t)=\int_{-\infty}^{t}\delta(\tau)\,d\tau$, so $g(t)=\int_{-\infty}^{t}h(\tau)\,d\tau$ and $h(t)=\frac{d}{dt}g(t)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does $h(t)=\frac{d}{dt}g(t)$ for constant-coefficient LTI? ::@:: Because $\delta(t)=\frac{d}{dt}u(t)$ and the LTI operator commutes with differentiation. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How is $g(t)=\int_{-\infty}^{t}h(\tau)\,d\tau$ derived from convolution? ::@:: From $g=u*h$, reduce to $\tau\ge 0$, substitute $\lambda=t-\tau$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- For causal systems, how does the step-response integral simplify? ::@:: $g(t)=\int_{0}^{t}h(\lambda)\,d\lambda$ for $t\ge 0$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What equations do $h(t)$ and $g(t)$ satisfy? ::@:: $L[h]=M[\delta]$ and $L[g]=M[u]$, both with zero initial conditions. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## typical impulse responses and what they mean

Several elementary impulse responses should be memorized.

For a scalar multiplier $r(t)=ae(t)$: $h(t)=a\delta(t)$. The system simply scales the input by $a$.

For a differentiator $r(t)=\frac{d}{dt}e(t)$: $h(t)=\delta'(t)$. The impulse derivative appears because differentiation is a singular operation in the time domain.

For an integrator $r(t)=\int_{-\infty}^{t} e(\tau)\,d\tau$: $h(t)=u(t)$. A unit impulse produces a unit step, matching the intuition that integration accumulates area.

For a delay element $r(t)=e(t-\tau_0)$: $h(t)=\delta(t-\tau_0)$. The system shifts the impulse without reshaping it.

Memorize these as a family: scaling changes impulse weight, differentiation raises the singular order, integration accumulates into a step, and delay shifts in time.

---

Flashcards for this section are as follows:

- Impulse response of $r(t)=ae(t)$? ::@:: $h(t)=a\delta(t)$ — scales input by gain $a$. <!--SR:!fsrs,2027-05-23T00:00:00.000Z,313,312.84164192,1,2,7,0,0,2026-07-14T00:00:00.000Z!fsrs,2027-08-28T00:00:00.000Z,396,395.78179232,1,2,7,0,0,2026-07-28T00:00:00.000Z-->
- Impulse response of $r(t)=\frac{d}{dt}e(t)$? ::@:: $h(t)=\delta'(t)$ — differentiation is singular. <!--SR:!fsrs,2027-08-12T00:00:00.000Z,383,382.68390242,1,2,7,0,0,2026-07-25T00:00:00.000Z!fsrs,2027-06-13T00:00:00.000Z,330,329.81882824,1,2,7,0,0,2026-07-18T00:00:00.000Z-->
- Impulse response of $r(t)=\int_{-\infty}^{t} e(\tau)\,d\tau$? ::@:: $h(t)=u(t)$ — a unit impulse becomes a unit step. <!--SR:!fsrs,2027-09-01T00:00:00.000Z,401,401.07868927,1,2,7,0,0,2026-07-27T00:00:00.000Z!fsrs,2027-05-28T00:00:00.000Z,317,317.09832588,1,2,7,0,0,2026-07-15T00:00:00.000Z-->
- Impulse response of $r(t)=e(t-\tau_0)$? ::@:: $h(t)=\delta(t-\tau_0)$ — shifts the impulse without reshaping. <!--SR:!fsrs,2027-09-12T00:00:00.000Z,410,410.22837316,1,2,7,0,0,2026-07-29T00:00:00.000Z!fsrs,2027-07-31T00:00:00.000Z,373,373.34672418,1,2,7,0,0,2026-07-23T00:00:00.000Z-->
- What family pattern connects these examples? ::@:: Scaling changes weight, differentiation raises singular order, integration accumulates into a step, delay shifts in time. <!--SR:!fsrs,2027-06-02T00:00:00.000Z,321,321.346657,1,2,7,0,0,2026-07-16T00:00:00.000Z!fsrs,2027-07-28T00:00:00.000Z,369,368.83580909,1,2,7,0,0,2026-07-24T00:00:00.000Z-->

## causality and stability from the impulse response

The impulse response reveals two core properties.

The system is __causal__ iff $h(t)=0$ for $t<0$. If the system reacts before the impulse is applied, it uses future information, violating causality. In the convolution formula $r_{\mathrm{zs}}(t)=\int_{-\infty}^{\infty}e(\tau)h(t-\tau)\,d\tau$, the condition $h(t-\tau)=0$ for $\tau>t$ forces the output at time $t$ to depend only on present and past input.

The system is __BIBO stable__ iff $\int_{-\infty}^{\infty} |h(t)|\,dt < \infty$. The bound: if $|e(t)|\le M$, then $|r_{\mathrm{zs}}(t)|\le M\int_{-\infty}^{\infty}|h(\lambda)|\,d\lambda$. So finite total absolute area of $h$ forces every bounded input to produce a bounded output. If the integral diverges, bounded inputs can make the output blow up.

These tests let you read system properties directly from $h(t)$.

---

Flashcards for this section are as follows:

- Causality condition? ::@:: $h(t)=0$ for $t<0$. <!--SR:!fsrs,2027-08-26T00:00:00.000Z,396,396.49212694,1,2,7,0,0,2026-07-26T00:00:00.000Z!fsrs,2027-05-02T00:00:00.000Z,296,295.72812302,1,2,7,0,0,2026-07-10T00:00:00.000Z-->
- Why does $h(t)\neq 0$ for $t<0$ imply noncausality? ::@:: The system would react before the impulse is applied, requiring future information. <!--SR:!fsrs,2027-09-07T00:00:00.000Z,406,405.65740649,1,2,7,0,0,2026-07-28T00:00:00.000Z!fsrs,2027-09-07T00:00:00.000Z,406,405.65740649,1,2,7,0,0,2026-07-28T00:00:00.000Z-->
- BIBO stability condition? ::@:: $\int_{-\infty}^{\infty}|h(t)|\,dt<\infty$. <!--SR:!fsrs,2027-04-05T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-05T00:00:00.000Z!fsrs,2027-08-21T00:00:00.000Z,392,391.89755234,1,2,7,0,0,2026-07-25T00:00:00.000Z-->
- Why does absolute integrability guarantee BIBO stability? ::@:: Convolution with a bounded input uses weights with finite total absolute mass, so the output cannot grow without bound. <!--SR:!fsrs,2027-06-13T00:00:00.000Z,330,329.81882824,1,2,7,0,0,2026-07-18T00:00:00.000Z!fsrs,2027-04-05T00:00:00.000Z,274,274.1280869,1,2,7,0,0,2026-07-05T00:00:00.000Z-->
- What inequality proves this? ::@:: If $|e(t)|\le M$, then $|r_{\mathrm{zs}}(t)|\le M\int_{-\infty}^{\infty}|h(\lambda)|\,d\lambda$. <!--SR:!fsrs,2027-08-26T00:00:00.000Z,396,396.49212694,1,2,7,0,0,2026-07-26T00:00:00.000Z!fsrs,2027-09-07T00:00:00.000Z,406,405.65740649,1,2,7,0,0,2026-07-28T00:00:00.000Z-->
- Why are these tests useful? ::@:: They infer major system properties from one signal instead of testing many inputs. <!--SR:!fsrs,2027-09-09T00:00:00.000Z,406,405.65740649,1,2,7,0,0,2026-07-30T00:00:00.000Z!fsrs,2027-08-17T00:00:00.000Z,387,387.29485933,1,2,7,0,0,2026-07-26T00:00:00.000Z-->

## second-order response patterns from characteristic roots

The same second-order behavior can be read from the time-domain characteristic equation of an RLC-type model, $s^2+\frac{R}{L}s+\frac{1}{LC}=0$. Define $\alpha=\frac{R}{2L}$ (damping coefficient) and $\omega_0=\frac{1}{\sqrt{LC}}$ (natural frequency); the roots are $p_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$. For $R,L,C>0$, $\alpha>0$ and the real part of every root is at most $-\alpha<0$: underdamped ($\alpha<\omega_0$) the square root is imaginary so the real part is exactly $-\alpha$; critically damped ($\alpha=\omega_0$) the repeated root is $-\alpha$; overdamped ($\alpha>\omega_0$) $\sqrt{\alpha^2-\omega_0^2}<\alpha$ so both roots remain negative. The only exception is $R=0$, where $\alpha=0$ and roots fall on the imaginary axis.

Four response classes:

- __Underdamped__: $\alpha<\omega_0$ — complex-conjugate roots with negative real part, decaying oscillation.
- __Critically damped__: $\alpha=\omega_0$ — repeated root at $-\alpha<0$, boundary between oscillatory and non-oscillatory.
- __Overdamped__: $\alpha>\omega_0$ — two distinct real negative roots, non-oscillatory decay with two time scales.
- __Undamped__: $R=0\Rightarrow\alpha=0$, imaginary-axis roots, sustained oscillation.

Learn this mapping now — it prevents confusion when the same roots appear as poles in the $s$-domain.

---

Flashcards for this section are as follows:

- For $s^2+\frac{R}{L}s+\frac{1}{LC}=0$, define $\alpha$, $\omega_0$, and the roots. ::@:: $\alpha=\frac{R}{2L}$ (damping), $\omega_0=\frac{1}{\sqrt{LC}}$ (natural frequency), $p_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$. For $R,L,C>0$, all roots have negative real part. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- $\alpha<\omega_0$: ? ::@:: Underdamped — decaying oscillation. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- $\alpha=\omega_0$: ? ::@:: Critically damped — repeated root at $-\alpha$, boundary case. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- $\alpha>\omega_0$: ? ::@:: Overdamped — two distinct real negative roots. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What gives sustained oscillation? ::@:: Undamped case $R=0$, $\alpha=0$, roots on the imaginary axis. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## impulse-response case studies

The examples below show how to interpret impulse response structurally.

First example: the input splits into two branches before the integrator — one direct, one delayed by $T$ into the negative summer. With $\delta(t)$ as input, the integrator receives $\delta(t)-\delta(t-T)$, so $h(t)=u(t)-u(t-T)$, a unit-height rectangular pulse on $0\le t<T$. The impulse turns the integrator on at $t=0$, and the delayed negative impulse turns it off at $t=T$.

Second example: $h(t)=e^{-2t}u(t)$. Causality: $u(t)$ makes $h(t)=0$ for $t<0$. Stability: $\int_{0}^{\infty}e^{-2t}\,dt=1/2<\infty$. These examples show how the general tests are applied in practice.

---

Flashcards for this section are as follows:

- Worked example: Input splits into direct and delayed-by-$T$ branches before an integrator. With input $\delta(t)$, what is $h(t)$? ::@:: The integrator receives $\delta(t)-\delta(t-T)$, so $h(t)=u(t)-u(t-T)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does $h(t)=u(t)-u(t-T)$ make sense? ::@:: The impulse at $t=0$ turns the integrator on; the delayed negative impulse at $t=T$ turns it off, giving a rectangular pulse of width $T$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Worked example: $h(t)=e^{-2t}u(t)$ — is it causal? ::@:: Yes: $u(t)$ makes $h(t)=0$ for $t<0$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Worked example: $h(t)=e^{-2t}u(t)$ — is it stable? ::@:: Yes: $\int_{0}^{\infty}e^{-2t}\,dt=1/2<\infty$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What do these examples teach? ::@:: Read impulse response structurally: branch delays and signs shape the waveform; causality and stability are checked from support and total area. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
