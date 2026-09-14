---
aliases:
  - ELEC 2100 discrete-time LTI response
  - ELEC 2100 discrete-time LTI system
  - ELEC 2100 discrete-time response
  - ELEC2100 discrete-time LTI response
  - ELEC2100 discrete-time LTI system
  - HKUST ELEC 2100 discrete-time LTI response
  - HKUST ELEC 2100 discrete-time LTI system
  - discrete-time LTI response
  - discrete-time LTI system
  - discrete-time response
  - discrete-time unit impulse response
  - unit impulse response sequence
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/discrete-time_LTI_system
  - language/in/English
---

# discrete-time LTI system

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

Discrete-time response analysis studies how an LTI system evolves sample by sample. The main ideas are recursive difference equations, discrete-time impulse response, and causality/stability criteria readable directly from $h[n]$.

This note parallels `continuous-time LTI system.md`: derivatives become differences, integrals become sums, exponentials become geometric sequences, and support moves from the real line to integers.

---

Flashcards for this section are as follows:

- What are the main tools in discrete-time response analysis? ::@:: Difference equations, impulse response $h[n]$, and direct causality/stability tests on $h[n]$.
- Do zero-input and zero-state viewpoints still apply to difference equations? ::@:: Yes; zero-input still comes from stored initial samples, and zero-state still comes from the external input with zero initial state.
- What later transform-domain method is previewed for discrete-time response? ::@:: The z-transform method, followed by inverse transform to recover $y[n]$.

## continuous-time and discrete-time parallels

A continuous-time LTI system uses differential equations, Dirac-impulse responses, and convolution integrals. A discrete-time LTI system uses difference equations, unit-sample responses, and convolution sums.

Causality and stability follow the same logic: $h(t)=0$ for $t<0$ and absolute integrability become $h[n]=0$ for $n<0$ and absolute summability.

First-order systems show the structural match: the exponential $e^{-at}u(t)$ corresponds to the geometric sequence $a^n u[n]$.

---

Flashcards for this section are as follows:

- How do the two LTI frameworks compare structurally? ::@:: Continuous time uses differential equations and convolution integrals; discrete time uses difference equations and convolution sums. Causality and stability tests follow the same pattern with sums replacing integrals.
- What is the first-order impulse-response analogy between continuous and discrete time? ::@:: The exponential $e^{-at}u(t)$ corresponds to the geometric sequence $a^n u[n]$.
- Why does ELEC 2100 keep separate continuous-time and discrete-time LTI notes? ::@:: Because the algebra, support language, and computational workflow are different enough that each medium deserves its own treatment, even though the conceptual map is shared.

## difference-equation solution viewpoints

A difference equation expresses the current output in terms of past outputs and current/past inputs. This recursive structure suggests two solution approaches.

The __iterative method__ computes the output sample by sample. It is straightforward and computer-friendly, but may not give a closed-form expression.

The __classical time-domain method__ splits the response into homogeneous and particular parts, solves the homogeneous recursion via its characteristic equation, picks a particular form matching the input, and determines constants from initial conditions. The zero-state part can also be obtained by convolution sum.

---

Flashcards for this section are as follows:

- What are the two main solution approaches for difference equations? ::@:: The iterative method computes sample by sample (good for computers, no closed form). The classical method splits into homogeneous and particular parts, matching the continuous-time approach.
- What is the standard linear difference-equation form? ::@:: $a_0y[n]+a_1y[n-1]+\cdots+a_Ny[n-N]=b_0x[n]+b_1x[n-1]+\cdots+b_Mx[n-M]$.
- Why is a difference equation naturally suited to iterative solution? ::@:: Because it is already a recursion: once enough initial data are known, one can compute the output sample by sample.

## mapping the response labels to difference-equation solutions

The same response labels apply in discrete time. For $a_0y[n]+a_1y[n-1]+\cdots+a_Ny[n-N]=b_0x[n]+b_1x[n-1]+\cdots+b_Mx[n-M]$:

- __Zero-input response__ $y_{\mathrm{zi}}[n]$: homogeneous solution with actual initial samples, input set to zero.
- __Zero-state response__ $y_{\mathrm{zs}}[n]$: forced solution with zero initial samples.
- __Natural response__: homogeneous-mode content.
- __Forced response__: content tied to the forcing pattern.

The solving-method split $y=y_h+y_p$ and the source-based split $y=y_{\mathrm{zi}}+y_{\mathrm{zs}}$ answer different questions.

Key caveat: $y_{\mathrm{zs}}[n]$ is generally not just $y_p[n]$. A particular solution may not satisfy zero initial conditions, so a homogeneous correction is often needed: $y_{\mathrm{zs}}[n]=y_p[n]+y_{h,\mathrm{corr}}[n]$.

When the recursion is stable, the transient part (homogeneous terms) decays, leaving the steady-state part (long-time particular solution). This is an eventual-time description, not exact at every index.

---

Flashcards for this section are as follows:

- What are the two complete-response decompositions? ::@:: The solving-method split $y=y_h+y_p$ and the source-based split $y=y_{\mathrm{zi}}+y_{\mathrm{zs}}$.
- Why is $y_{\mathrm{zs}}[n]$ generally not just $y_p[n]$? ::@:: Because a particular solution may not satisfy zero initial conditions, so a homogeneous correction $y_{h,\mathrm{corr}}$ is needed: $y_{\mathrm{zs}}=y_p+y_{h,\mathrm{corr}}$.
- How is zero-input response mapped to difference-equation solution pieces? ::@:: Solve the homogeneous difference equation with the actual initial samples and set the input to zero; the result is a homogeneous-solution object.
- How is zero-state response mapped to difference-equation solution pieces? ::@:: Solve the forced difference equation with zero initial samples; the result is the response caused only by the external input.
- How are natural response and forced response mapped in discrete time? ::@:: Natural response is homogeneous-mode content, whereas forced response is the content tied to the forcing pattern.
- How do transient and steady-state parts relate to the difference-equation pieces when the recursion is stable? ::@:: The transient part is tied to homogeneous-mode content that decays, while the steady-state part is tied to the long-time part of the particular solution. This is an asymptotic description, not exact at every index.

## iterative method and recursion intuition

A recursive equation makes the memory structure visible. For $y[n]=0.9y[n-1]+u[n]$ with $y[-1]=0$: $y[0]=1$, $y[1]=1.9$, $y[2]=2.71$, $y[3]=3.439$. Each sample retains $90\%$ of the previous output plus a fresh input of $1$.

If a limiting value exists, it satisfies $y_{\infty}=0.9y_{\infty}+1$, giving $y_{\infty}=10$. The recursion recycles past output, so samples climb toward a level much larger than any single input step.

The iterative method makes the memory mechanism visible even without a closed-form solution.

---

Flashcards for this section are as follows:

- Worked example: Given $y[n]=0.9y[n-1]+u[n]$ with $y[-1]=0$, what are the first four output samples? ::@:: $y[0]=1$, $y[1]=1.9$, $y[2]=2.71$, $y[3]=3.439$.
- What does the factor $0.9$ mean in $y[n]=0.9y[n-1]+u[n]$? ::@:: The system retains $90\%$ of the previous output; past information fades gradually.
- What is the steady-state value of $y[n]=0.9y[n-1]+u[n]$? ::@:: $y_{\infty}=10$, from the fixed-point equation $y_{\infty}=0.9y_{\infty}+1$.
- In the recursion $y[n]=0.9y[n-1]+u[n]$, why does the sequence build upward sample by sample? ::@:: Because each step keeps most of the previous output and adds a new forcing contribution of $1$ from the unit-step input.
- Why is the iterative method useful even before a closed-form solution is known? ::@:: It makes the memory mechanism of the recursion visible and lets you compute the actual output sequence directly.

## discrete-time impulse response

The discrete-time unit impulse response $h[n]$ is the zero-state response to $\delta[n]$. It is an ordinary sequence (not a generalized function) from which zero-state outputs are built by convolution.

For direct-form systems, feed in $\delta[n]$ and track branches. For $y[n]=x[n]+\frac{1}{2}x[n-1]$, this gives $h[n]=\delta[n]+\frac{1}{2}\delta[n-1]$.

For recursive systems, use the __equivalent initial-condition method__. The impulse $\delta[n]$ acts only at $n=0$, creating the correct initial sample. After that, the homogeneous recursion takes over.

Example: $y[n]-0.8y[n-1]=x[n]$. Under impulse excitation: $h[n]-0.8h[n-1]=\delta[n]$. At $n=0$: $h[0]=1$ (since $h[-1]=0$). For $n>0$: $h[n]=0.8h[n-1]$, giving $h[n]=(0.8)^n u[n]$.

The structural comparison with continuous time:

|                 | Continuous time | Discrete time           |
| --------------- | --------------- | ----------------------- |
| Impulse creates | jump condition  | initial-sample equation |
| Free evolution  | homogeneous ODE | homogeneous recursion   |
| Result          | $e^{-at}$       | $(0.8)^n$               |

The decay factor $0.8$ is the sampled version of $e^{-aT_s}$: sampling $e^{-at}$ at interval $T_s$ gives $(e^{-aT_s})^n$.

---

Flashcards for this section are as follows:

- What is the discrete-time unit impulse response $h[n]$? ::@:: The zero-state response to input $\delta[n]$.
- Why is discrete-time impulse response structurally important? ::@:: Once $h[n]$ is known, zero-state outputs can be built later through convolution sums.
- Worked example: For $y[n]=x[n]+\frac{1}{2}x[n-1]$, what is $h[n]$? ::@:: $h[n]=\delta[n]+\frac{1}{2}\delta[n-1]$.
- Why does the impulse response of $y[n]=x[n]+\frac{1}{2}x[n-1]$ have two shifted impulses? ::@:: Because the unit sample travels through a direct branch and a one-sample-delayed branch with gain $1/2$.
- Worked example: For $y[n]-0.8y[n-1]=x[n]$, find $h[n]$. ::@:: $h[n]-0.8h[n-1]=\delta[n]$. At $n=0$: $h[0]=1$. For $n>0$: $h[n]=0.8h[n-1]$. Thus $h[n]=(0.8)^n u[n]$.
- Why is the trial form $h_h[n]=r^n$ natural for the homogeneous recursion? ::@:: A one-sample shift sends $r^n$ to $r^{n-1}$, which is the same shape multiplied by a constant. Geometric sequences reproduce themselves under shifts, just as exponentials reproduce themselves under derivatives.
- Why does the equation $h[n]-0.8h[n-1]=\delta[n]$ become homogeneous for $n>0$? ::@:: Because the impulse is nonzero only at $n=0$, so for later indices the forcing term vanishes.
- In the first-order recursion example, what does the impulse $\delta[n]$ do conceptually? ::@:: It acts only at the single sample $n=0$, creating the initial sample of the impulse response; after that, the later samples evolve under the homogeneous recursion alone.
- How does the discrete-time derivation compare to continuous time? ::@:: The impulse creates an initial condition, then the homogeneous recursion/ODE gives geometric/exponential decay. The factor $0.8$ corresponds to $e^{-aT_s}$ after sampling.
- How does direct iteration confirm $h[n]=(0.8)^n u[n]$? ::@:: Starting from $h[0]=1$ and applying $h[n]=0.8h[n-1]$, one gets $h[1]=0.8$, $h[2]=0.8^2$, and in general $h[n]=0.8^n$ for $n\ge 0$.
- What is the analogous continuous-time first-order impulse-response problem? ::@:: A causal ODE such as $h'(t)+ah(t)=\delta(t)$, where the impulse creates a jump condition and leaves a homogeneous equation for later times.

## causality and stability from discrete-time impulse response

Two core tests follow from $h[n]$:

- __Causality__: $h[n]=0$ for $n<0$. A nonzero value at negative indices means the system reacts before the input arrives.
- __BIBO stability__: $\sum_{n=-\infty}^{\infty}|h[n]|<\infty$ (absolute summability). If $|x[m]|\le B$, then $|y[n]|\le B\sum_k |h[k]|$, so bounded inputs stay bounded.

Example: $h[n]=a^n u[n]$ is causal (one-sided). It is stable when $|a|<1$, since $\sum_{n=0}^{\infty}|a|^n=1/(1-|a|)$.

---

Flashcards for this section are as follows:

- What conditions make a discrete-time LTI system causal and BIBO stable? ::@:: Causal: $h[n]=0$ for $n<0$. BIBO stable: $\sum|h[n]|<\infty$.
- When is $h[n]=a^n u[n]$ stable? ::@:: When $|a|<1$, since $\sum_{n=0}^{\infty}|a|^n=1/(1-|a|)$.

## causality, stability, and interconnection case studies

The accumulator $y[n]=\sum_{k=-\infty}^{n}x[k]$ has $h[n]=u[n]$. It is causal but not BIBO stable (the sum diverges). This shows causality alone does not guarantee stability.

An interconnected example: $h_1[n]=(1/2)^n u[n+2]$ followed by parallel branches $h_2[n]=\delta[n]$ and $h_3[n]=u[n-1]$. The overall response is $h[n]=h_1[n]+(h_1*u[n-1])[n]$. For $n\ge -1$, the running-sum term is $\sum_{m=-2}^{n-1}(1/2)^m=8-2^{-(n-1)}$. Adding $h_1[n]=2^{-n}$: $h[n]=8-2^{-n}$ for $n\ge -1$, $h[-2]=4$, $h[n]=0$ for $n<-2$.

This combines series, parallel, and convolution—simplify block structure before expanding the algebra.

---

Flashcards for this section are as follows:

- What is the accumulator's impulse response and stability? ::@:: $h[n]=u[n]$: causal but not BIBO stable (sum diverges).
- Worked example: For the interconnected system with $h_1[n]=(1/2)^n u[n+2]$, $h_2[n]=\delta[n]$, $h_3[n]=u[n-1]$, find $h[n]$. ::@:: $h[n]=h_1[n]+(h_1*u[n-1])[n]$. For $n\ge -1$: $h[n]=8-2^{-n}$. At $n=-2$: $h[-2]=4$. Otherwise: $h[n]=0$.
