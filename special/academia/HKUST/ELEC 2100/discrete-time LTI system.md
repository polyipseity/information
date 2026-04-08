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

Discrete-time response analysis studies how an LTI system evolves sample by sample. In ELEC 2100, the main ideas are recursive difference-equation viewpoints, discrete-time impulse response, and the causality and stability criteria that can be read directly from $h[n]$ before z-transform methods are introduced.

The note is meant to be read in parallel with `continuous-time LTI system.md`, not in competition with it. The structural ideas are the same, but the medium changes: derivatives become differences, integrals become sums, exponentials in time become geometric sequences in index, and support conditions move from the real line to integer shifts.

---

Flashcards for this section are as follows:

- What is the main goal of the discrete-time LTI system note? ::@:: It is to understand how an LTI system evolves sample by sample through difference equations, discrete-time impulse response, and direct criteria on $h[n]$ before z-transform methods are introduced.
- Why is discrete-time response treated as its own topic instead of just copying the continuous-time story? ::@:: Because discrete-time systems are governed by recursive index relations and convolution sums, so the same ideas reappear in sample-by-sample rather than differential form.
- Why should `discrete-time LTI system.md` be read alongside `continuous-time LTI system.md`? ::@:: Because the two notes describe the same structural LTI ideas in different media: continuous time uses derivatives and integrals, while discrete time uses differences and sums.

## continuous-time and discrete-time parallels

The fastest way to organize this note is to keep the continuous-time analogue in view. A continuous-time LTI system is commonly modeled by a differential equation, its impulse response is obtained from a Dirac-impulse input, and zero-state response is computed by a convolution integral. A discrete-time LTI system is commonly modeled by a difference equation, its impulse response is obtained from a unit-sample input, and zero-state response is computed by a convolution sum.

The property tests line up just as neatly. In continuous time, causality means $h(t)=0$ for $t<0$ and BIBO stability is tied to absolute integrability of $h(t)$. In discrete time, causality means $h[n]=0$ for $n<0$ and BIBO stability is tied to absolute summability of $h[n]$. The same logic survives, but the measure of accumulation changes from an integral to a sum.

The response-shape analogy is equally important. A first-order continuous-time system often produces a one-sided exponential impulse response such as $e^{-at}u(t)$. A first-order discrete-time system often produces a one-sided geometric impulse response such as $a^n u[n]$. So the right memory cue is not that the formulas are unrelated, but that the discrete-time formula is the sample-by-sample analogue of exponential decay.

This is why the course keeps separate continuous-time and discrete-time notes instead of forcing them into one merged file. The conceptual map is shared, but the algebra, support language, and computational workflow are different enough that each medium deserves its own durable home.

---

Flashcards for this section are as follows:

- What is the quickest structural comparison between the two LTI notes? ::@:: Continuous time uses differential equations, Dirac-impulse responses, and convolution integrals, whereas discrete time uses difference equations, unit-sample responses, and convolution sums.
- How do the causality and BIBO stability tests compare in continuous time and discrete time? ::@:: Continuous time uses $h(t)=0$ for $t<0$ and absolute integrability of $h(t)$, whereas discrete time uses $h[n]=0$ for $n<0$ and absolute summability of $h[n]$.
- What is the right analogy between a first-order continuous-time impulse response and a first-order discrete-time impulse response? ::@:: A one-sided exponential such as $e^{-at}u(t)$ in continuous time corresponds structurally to a one-sided geometric sequence such as $a^n u[n]$ in discrete time.
- Why does ELEC 2100 keep separate continuous-time and discrete-time LTI notes instead of forcing one merged treatment? ::@:: Because the conceptual map is shared, but the algebra, support language, and computational workflow are different enough that each medium deserves its own durable explanation.

## difference-equation solution viewpoints

The lecture begins with discrete-time system equations. A difference equation is naturally recursive, so the present output sample is written in terms of past output samples and present or past input samples. This already suggests an iterative solution viewpoint: once enough initial data are known, one may compute the output one sample at a time.

The __iterative method__ is therefore the most direct computational approach. It is especially suitable for computers because the difference equation itself is a recursion. Its limitation is that it may generate numerical values without giving a clean closed-form expression for the whole sequence.

The __classical time-domain method__ parallels the continuous-time story. For a linear recursion such as $a_0y[n]+a_1y[n-1]+\cdots+a_Ny[n-N]=b_0x[n]+b_1x[n-1]+\cdots+b_Mx[n-M]$, one splits the response into a homogeneous part and a particular part, solves the homogeneous recursion from its characteristic equation, chooses a particular form compatible with the input, and then determines constants from initial conditions. The lecture also reminds students that zero-input and zero-state viewpoints still apply, and that the zero-state part may later be obtained by convolution sum. A z-transform route is previewed as the later transform-domain alternative.

---

Flashcards for this section are as follows:

- Why is a difference equation naturally suited to iterative solution? ::@:: Because it is already a recursion, so once enough initial data are known one can compute the output sample by sample.
- What is the main advantage of the iterative method for discrete-time systems? ::@:: It is straightforward and especially suitable for computer calculation.
- What is the main limitation of the iterative method? ::@:: It may produce output values without yielding a clean analytical expression for the full sequence.
- What general linear difference-equation form underlies the classical discrete-time method? ::@:: A standard form is $a_0y[n]+a_1y[n-1]+\cdots+a_Ny[n-N]=b_0x[n]+b_1x[n-1]+\cdots+b_Mx[n-M]$.
- How does the classical time-domain method for difference equations parallel the continuous-time method? ::@:: It splits the response into homogeneous and particular parts, solves the homogeneous recursion from the characteristic equation, picks a particular form compatible with the input, and then determines constants from initial conditions.
- Do zero-input and zero-state viewpoints still apply to difference equations? ::@:: Yes; zero-input still comes from stored initial conditions, and zero-state still comes from the external input with zero initial state.
- What later transform-domain method is previewed for discrete-time response? ::@:: The z-transform method, followed by inverse transform to recover $y[n]$.

## mapping the response labels to difference-equation solutions

The response labels should be mapped just as explicitly in discrete time as in continuous time. Suppose the input-output model is $a_0y[n]+a_1y[n-1]+\cdots+a_Ny[n-N]=b_0x[n]+b_1x[n-1]+\cdots+b_Mx[n-M]$. The classical algebraic split is $y[n]=y_h[n]+y_p[n]$, where $y_h$ solves the homogeneous recursion and $y_p$ is one particular solution of the forced recursion. This is the solving-method split.

The physical/source-based split is $y[n]=y_{\mathrm{zi}}[n]+y_{\mathrm{zs}}[n]$.

Here the mapping is direct:

- __Zero-input response__ $y_{\mathrm{zi}}[n]$: solve the homogeneous difference equation with the actual initial samples and set the input to zero.
- __Zero-state response__ $y_{\mathrm{zs}}[n]$: solve the forced difference equation with zero initial samples.
- __Natural response__: homogeneous-mode content.
- __Forced response__: content tied to the forcing pattern.

The same important caveat appears here too: $y_{\mathrm{zs}}[n]$ is generally not just the particular solution $y_p[n]$. A convenient particular solution may fail to satisfy the zero initial conditions, so one often needs a homogeneous correction term, namely $y_{\mathrm{zs}}[n]=y_p[n]+y_{h,\mathrm{corr}}[n]$, where $y_{h,\mathrm{corr}}$ is chosen so that the total zero-state response starts from the required zero stored state. Thus $y_h+y_p$ and $y_{\mathrm{zi}}+y_{\mathrm{zs}}$ are again two different decompositions answering two different questions.

There is also the asymptotic split into transient and steady-state parts. When the recursion is stable and the input is sustained, the homogeneous-mode content often decays, so the transient part is usually tied to homogeneous terms and the steady-state part is usually tied to the long-time part of the particular solution. But this is an eventual-time description, not a literal identity valid at every index.

---

Flashcards for this section are as follows:

- For the difference equation $a_0y[n]+a_1y[n-1]+\cdots+a_Ny[n-N]=b_0x[n]+b_1x[n-1]+\cdots+b_Mx[n-M]$, what are the two main complete-response decompositions? ::@:: The response may be written either as $y[n]=y_h[n]+y_p[n]$ in the classical solving-method split or as $y[n]=y_{\mathrm{zi}}[n]+y_{\mathrm{zs}}[n]$ in the source-based split.
- How is zero-input response mapped to difference-equation solution pieces? ::@:: Zero-input response is obtained by solving the homogeneous difference equation with the actual initial samples and with the input set to zero, so it is a homogeneous-solution object.
- How is zero-state response mapped to difference-equation solution pieces? ::@:: Zero-state response is obtained by solving the forced difference equation with zero initial samples, so it is the response caused only by the external input.
- How are natural response and forced response mapped in the discrete-time setting? ::@:: Natural response is homogeneous-mode content, whereas forced response is the content tied to the forcing pattern and represented by a particular solution plus any needed correction to satisfy the required initial-state condition.
- Why is zero-state response generally not just the particular solution $y_p[n]$ in a difference-equation problem? ::@:: Because a convenient particular solution may fail to satisfy the zero initial conditions, so a homogeneous correction is often needed.
- What is the standard correction formula relating zero-state response to a particular solution in discrete time? ::@:: It is $y_{\mathrm{zs}}[n]=y_p[n]+y_{h,\mathrm{corr}}[n]$, where $y_{h,\mathrm{corr}}$ is chosen so that the total response satisfies the required zero initial samples.
- Why are the decompositions $y=y_h+y_p$ and $y=y_{\mathrm{zi}}+y_{\mathrm{zs}}$ not contradictory? ::@:: They answer different questions: $y_h+y_p$ is the algebraic solving split, while $y_{\mathrm{zi}}+y_{\mathrm{zs}}$ is the physical split into stored-state and input-caused parts.
- How do transient and steady-state parts relate to the difference-equation pieces when the recursion is stable and the input is sustained? ::@:: The transient part is often tied to homogeneous-mode content that decays, while the steady-state part is often tied to the long-time part of the particular solution, but this is an asymptotic rather than an exact identity at every index.

## iterative method and recursion intuition

A recursive equation makes the memory structure visible immediately. For example, if $y[n]=0.9y[n-1]+u[n]$ and the initial state is $y[-1]=0$, then the output is computed step by step: $y[0]=1$, $y[1]=1.9$, $y[2]=2.71$, $y[3]=3.439$, and so on. Each new output sample contains a retained portion of the previous output together with the new forcing contribution.

This example is pedagogically useful because it shows what system memory means in discrete time. The coefficient $0.9$ says the system keeps $90\%$ of the previous output sample, so past information fades gradually rather than disappearing instantly. The unit-step input keeps injecting a fresh value of $1$ at every step, so the sequence builds up recursively.

The same recursion also hints at the eventual steady level. If a limiting value $y_{\infty}$ exists, it must satisfy the fixed-point equation $y_{\infty}=0.9y_{\infty}+1$, so $y_{\infty}=10$. The early samples therefore climb toward a level that is much larger than a single forcing step because the recursion keeps recycling past output.

The iterative method is therefore more than a bookkeeping trick. It makes the memory mechanism of the recursion visible, even when no closed-form solution has been written yet.

---

Flashcards for this section are as follows:

- Worked example: Given $y[n]=0.9y[n-1]+u[n]$ with $y[-1]=0$, what are the first four output samples $y[0]$, $y[1]$, $y[2]$, and $y[3]$? ::@:: Step 1: $y[0]=0.9y[-1]+u[0]=0.9(0)+1=1$. <br/> Step 2: $y[1]=0.9y[0]+u[1]=0.9(1)+1=1.9$. <br/> Step 3: $y[2]=0.9y[1]+u[2]=0.9(1.9)+1=2.71$. <br/> Step 4: $y[3]=0.9y[2]+u[3]=0.9(2.71)+1=3.439$.
- In the recursion $y[n]=0.9y[n-1]+u[n]$, what does the factor $0.9$ mean intuitively? ::@:: It means the system retains $90\%$ of the previous output sample, so past information fades gradually instead of disappearing at once.
- In the recursion $y[n]=0.9y[n-1]+u[n]$, why does the sequence build upward sample by sample? ::@:: Because each step keeps most of the previous output and adds a new forcing contribution of $1$ from the unit-step input.
- If the recursion $y[n]=0.9y[n-1]+u[n]$ approaches a steady value $y_{\infty}$, what equation determines that value and what does it give? ::@:: The fixed point satisfies $y_{\infty}=0.9y_{\infty}+1$, so $y_{\infty}=10$.
- Why is the iterative method useful even before a closed-form solution is known? ::@:: It makes the memory mechanism of the recursion visible and lets you compute the actual output sequence directly.

## discrete-time impulse response

The discrete-time unit impulse response $h[n]$ is the zero-state response to the input $\delta[n]$. As in continuous time, it is the basic response object from which later zero-state outputs are assembled, but here it is an ordinary sequence rather than a generalized function.

In direct-form block diagrams, one may often read $h[n]$ by feeding in $\delta[n]$ and tracking the branches. For the feedforward system $y[n]=x[n]+\frac{1}{2}x[n-1]$, replacing $x[n]$ by $\delta[n]$ gives $h[n]=\delta[n]+\frac{1}{2}\delta[n-1]$. The impulse response simply records what the unit sample does as it travels through the direct and delayed paths.

For recursive systems, a useful technique is the __equivalent initial-condition method__. Consider the causal system described by $y[n]-0.8y[n-1]=x[n]$. Under zero-state impulse excitation this becomes $h[n]-0.8h[n-1]=\delta[n]$. At $n=0$ this gives $h[0]-0.8h[-1]=1$, and zero state implies $h[-1]=0$, so $h[0]=1$. For $n>0$ the impulse term vanishes, so the recursion becomes homogeneous: $h[n]-0.8h[n-1]=0$. Trying the ansatz $h_h[n]=r^n$ gives the characteristic equation $r-0.8=0$, so $r=0.8$ and $h[n]=C(0.8)^n$ on the causal side. The initial sample fixes $C=1$, so $h[n]=(0.8)^n u[n]$.

The phrase __equivalent initial-condition method__ is important here. The impulse $\delta[n]$ acts only at the single sample $n=0$, so it does not keep forcing the system forever. Its role is to create the correct first sample of the impulse response. Once that initial sample has been created, every later index obeys the homogeneous recursion alone. That is why the impulse response of a causal first-order recursion is often a gated geometric sequence: the pulse input is converted into initial data, and the subsequent decay is generated entirely by the system's own recursion.

The homogeneous recursion can also be unpacked directly instead of only through the characteristic root. From $h[n]=0.8h[n-1]$ for $n>0$ and $h[0]=1$, one gets $h[1]=0.8$, $h[2]=0.8^2$, $h[3]=0.8^3$, and by induction $h[n]=0.8^n$ for all $n\ge 0$. The characteristic-root method compresses this pattern into one algebraic step, but the iteration makes the propagation law visible: each new sample is obtained by multiplying the previous one by the same decay factor.

This is the discrete-time counterpart of a standard continuous-time first-order impulse-response derivation. In continuous time, one studies an equation such as $h'(t)+ah(t)=\delta(t)$ with zero pre-initial state. The impulse acts only at $t=0$, and for $t>0$ the equation becomes homogeneous: $h'(t)+ah(t)=0$. Integrating across the initial instant converts the impulse into a jump condition, while in discrete time substituting $n=0$ converts the unit sample into the initial-value equation $h[0]-0.8h[-1]=1$. After that, the free evolution takes over: exponential decay $e^{-at}$ in continuous time, geometric decay $(0.8)^n$ in discrete time.

There is even a precise decay analogy. If one samples a continuous-time exponential $e^{-at}$ every $T_s$ seconds, the resulting sequence is $e^{-anT_s}=(e^{-aT_s})^n$. So the discrete recursion factor $0.8$ plays the role of a sampled exponential decay constant: it is exactly the per-sample multiplier analogous to $e^{-aT_s}$ in continuous time. The continuous-time pole location $-a$ becomes the discrete-time decay factor $e^{-aT_s}$ after sampling.

So the comparison should be remembered structurally rather than only formulaically:

- __Continuous time__: impulse at one instant $\to$ jump condition $\to$ homogeneous ODE for later times $\to$ exponential impulse response.
- __Discrete time__: impulse at one sample $\to$ initial-sample equation $\to$ homogeneous recursion for later indices $\to$ geometric impulse response.

The support factors also match in role. In continuous time, the causal exponential is written with $u(t)$ to suppress all pre-initial values. In discrete time, the gated geometric sequence uses $u[n]$ for the same reason. The only difference is the medium of propagation: continuous time evolves continuously through a differential law, whereas discrete time propagates sample to sample through multiplication by the recursion factor.

---

Flashcards for this section are as follows:

- What is the discrete-time unit impulse response $h[n]$? ::@:: It is the zero-state response of the system to the unit impulse input $\delta[n]$.
- Why is discrete-time impulse response structurally important? ::@:: Because once $h[n]$ is known, zero-state outputs can be built later through convolution sums.
- Worked example: For the feedforward system $y[n]=x[n]+\frac{1}{2}x[n-1]$, what is the unit impulse response? ::@:: Step 1: set the input to $x[n]=\delta[n]$. <br/> Step 2: substitute into the system equation to get $h[n]=\delta[n]+\frac{1}{2}\delta[n-1]$. <br/> Step 3: read this as one direct unit sample plus one delayed copy scaled by $1/2$.
- Why does the impulse response of $y[n]=x[n]+\frac{1}{2}x[n-1]$ have two shifted impulses? ::@:: Because the unit sample travels through a direct branch and a one-sample-delayed branch with gain $1/2$.
- What is the zero-state impulse-response equation for the causal system $y[n]-0.8y[n-1]=x[n]$? ::@:: It is $h[n]-0.8h[n-1]=\delta[n]$.
- How is the initial sample $h[0]$ found in the impulse-response equation $h[n]-0.8h[n-1]=\delta[n]$? ::@:: Set $n=0$ to get $h[0]-0.8h[-1]=1$; zero state gives $h[-1]=0$, so $h[0]=1$.
- Why does the equation $h[n]-0.8h[n-1]=\delta[n]$ become homogeneous for $n>0$? ::@:: Because the impulse is nonzero only at $n=0$, so for later indices the forcing term vanishes.
- Why is the trial form $h_h[n]=r^n$ natural for the homogeneous recursion $h[n]-0.8h[n-1]=0$? ::@:: A one-sample shift sends $r^n$ to $r^{n-1}$, which is the same shape multiplied by a constant. So geometric sequences are the discrete-time analogue of exponentials in ODEs: they reproduce themselves under shifts and are therefore natural candidates for constant-coefficient recursions.
- What characteristic equation is produced by the ansatz $h_h[n]=r^n$ in the recursion $h[n]-0.8h[n-1]=0$, and how should you think about it? ::@:: Substitute $h_h[n]=r^n$ to get $r^n-0.8r^{n-1}=0$. <br/> Factor out $r^{n-1}$ to obtain $r^{n-1}(r-0.8)=0$. <br/> For a nontrivial sequence this requires $r-0.8=0$, so $r=0.8$. <br/> Intuitively, the recursion asks for a sequence whose next sample is always $0.8$ times the previous one, and the geometric sequence $(0.8)^n$ is exactly that shape.
- Worked example: For the causal system $y[n]-0.8y[n-1]=x[n]$, what is the unit impulse response? ::@:: Step 1: set $x[n]=\delta[n]$ to get $h[n]-0.8h[n-1]=\delta[n]$. <br/> Step 2: at $n=0$, zero state gives $h[-1]=0$, so $h[0]=1$. <br/> Step 3: for $n>0$, the recursion becomes homogeneous: $h[n]-0.8h[n-1]=0$. <br/> Step 4: solve the homogeneous part with $h_h[n]=r^n$, giving $r-0.8=0$ and hence $h_h[n]=C(0.8)^n$. <br/> Step 5: by substituting the initial condition $h[0]=1$, this becomes $h[n]=(0.8)^n$ for $n\ge 0$; for $n<0$ we already know the zero-state response is $0$, so finally $h[n]=(0.8)^n u[n]$.
- In the first-order recursion example, what does the impulse $\delta[n]$ do conceptually? ::@:: It acts only at the single sample $n=0$, where it creates the initial sample of the impulse response; after that, the later samples evolve under the homogeneous recursion alone.
- How does direct iteration confirm the formula $h[n]=(0.8)^n u[n]$ in the first-order recursion example? ::@:: Starting from $h[0]=1$ and repeatedly applying $h[n]=0.8h[n-1]$ for $n>0$, one gets $h[1]=0.8$, $h[2]=0.8^2$, $h[3]=0.8^3$, and in general $h[n]=0.8^n$ for $n\ge 0$. This is the sample-by-sample version of exponential decay.
- What is the analogous continuous-time first-order impulse-response problem for the recursion example $h[n]-0.8h[n-1]=\delta[n]$? ::@:: It is a causal ODE such as $h'(t)+ah(t)=\delta(t)$, where the impulse acts only at the initial instant, creates a jump condition, and leaves a homogeneous equation for later times.
- How do the discrete-time and continuous-time first-order impulse-response derivations compare structurally? ::@:: In continuous time the impulse creates a jump condition and then a homogeneous ODE produces an exponential; in discrete time the unit sample creates the initial-sample equation and then a homogeneous recursion produces a geometric sequence.
- What is the precise decay analogy between the recursion factor $0.8$ and a continuous-time exponential? ::@:: Sampling a continuous-time exponential $e^{-at}$ at interval $T_s$ gives $(e^{-aT_s})^n$, so the discrete decay factor $0.8$ plays the same per-sample role as $e^{-aT_s}$ in continuous time.
- Why is the impulse response of the first-order causal recursion a gated geometric sequence? ::@:: The impulse acts only once to create the initial sample, the homogeneous recursion then multiplies by the same factor at each later step, and causality suppresses all negative-index values. So the response is geometric on $n\ge 0$ and zero on $n<0$, i.e. a gated geometric sequence.

## causality and stability from discrete-time impulse response

The discrete-time impulse response also provides direct tests for two core system properties.

A discrete-time LTI system is __causal__ if and only if $h[n]=0$ for $n<0$. This is the sample-by-sample analogue of the continuous-time rule. If the impulse response had nonzero values at negative indices, the system would be reacting before the input sample arrived.

A discrete-time LTI system is __BIBO stable__ if the impulse response is absolutely summable, meaning $\sum_{n=-\infty}^{\infty}|h[n]|<\infty$. This is the discrete counterpart of absolute integrability in continuous time. The standard estimate is $|y[n]|=\left|\sum_{m=-\infty}^{\infty}x[m]h[n-m]\right|\le \sum_{m=-\infty}^{\infty}|x[m]|\,|h[n-m]|\le B\sum_{k=-\infty}^{\infty}|h[k]|$ whenever $|x[m]|\le B$. The intuition is the same: if the total absolute weight assigned to all shifted impulse contributions is finite, then bounded inputs cannot accumulate into unbounded outputs.

The geometric example $h[n]=a^n u[n]$ shows both tests cleanly. The sequence is one-sided, so it is causal. Its absolute sum is $\sum_{n=-\infty}^{\infty}|h[n]|=\sum_{n=0}^{\infty}|a|^n$, which equals $1/(1-|a|)$ when $|a|<1$ and diverges when $|a|\ge 1$. Therefore the system is stable exactly when the geometric tail decays fast enough to have finite total weight.

---

Flashcards for this section are as follows:

- What impulse-response condition characterizes causality for a discrete-time LTI system? ::@:: The system is causal if and only if $h[n]=0$ for $n<0$.
- Why does a nonzero value of $h[n]$ at a negative index imply noncausality? ::@:: Because it means the system would respond before the corresponding input sample arrives.
- What impulse-response condition characterizes BIBO stability for a discrete-time LTI system? ::@:: The system is BIBO stable if $\sum_{n=-\infty}^{\infty}|h[n]|<\infty$.
- Why does absolute summability of $h[n]$ guarantee bounded-input bounded-output stability? ::@:: Because the total absolute weight of all shifted impulse contributions is finite, so bounded inputs cannot accumulate into an unbounded output.
- What convolution-sum inequality proves that absolute summability of $h[n]$ implies BIBO stability? ::@:: If $|x[m]|\le B$, then $|y[n]|=\left|\sum_m x[m]h[n-m]\right|\le B\sum_k |h[k]|$, so the output is uniformly bounded whenever the absolute sum of $h$ is finite.
- For $h[n]=a^n u[n]$, why is the system automatically causal? ::@:: Because the factor $u[n]$ makes the impulse response one-sided, so it vanishes for all negative indices.
- For $h[n]=a^n u[n]$, what absolute sum determines stability? ::@:: It is $\sum_{n=-\infty}^{\infty}|h[n]|=\sum_{n=0}^{\infty}|a|^n$, which is geometric.
- For $h[n]=a^n u[n]$, when is the system stable? ::@:: It is stable exactly when $|a|<1$, because only then does the geometric series of absolute values converge.

## causality, stability, and interconnection case studies

The summary slides include two useful discrete-time examples that sharpen the general criteria.

The first is the accumulator $y[n]=\sum_{k=-\infty}^{n}x[k]$. Feeding in the unit impulse gives $h[n]=\sum_{k=-\infty}^{n}\delta[k]=u[n]$. This immediately shows the system is causal, because $u[n]=0$ for $n<0$. It is not stable, because $\sum_{n=-\infty}^{\infty}|u[n]|$ diverges. The example is important because it shows that a system may be perfectly causal and still fail BIBO stability if its memory keeps accumulating forever without sufficient decay.

The second example is an interconnected LTI system in which the input first passes through $h_1[n]=(1/2)^n u[n+2]$, then splits into two parallel branches with $h_2[n]=\delta[n]$ and $h_3[n]=u[n-1]$, and the branch outputs are added. Structurally, the parallel part has impulse response $h_2[n]+h_3[n]$, so the whole system has impulse response $h[n]=h_1[n]*(h_2[n]+h_3[n])=h_1[n]+h_1[n]*u[n-1]$. The first term is just the original branch, while the second term is a running sum of shifted copies of $h_1[n]$: $(h_1*u[n-1])[n]=\sum_{m=-\infty}^{\infty}h_1[m]u[n-1-m]=\sum_{m=-2}^{n-1}\left(\frac12\right)^m$ whenever $n\ge -1$. Evaluating the geometric sum gives $\sum_{m=-2}^{n-1}(1/2)^m=8-2^{-(n-1)}$, so adding the direct term $h_1[n]=2^{-n}$ yields $h[n]=8-2^{-n}$ for $n\ge -1$. Together with the early samples this gives the explicit piecewise result $h[n]=0$ for $n<-2$, $h[-2]=4$, and $h[n]=8-2^{-n}$ for $n\ge -1$.

This interconnection example is useful because it combines all three structural ideas from the time-domain LTI toolkit: series connection, parallel connection, and convolution with step-like sequences. It also shows that one should simplify block structure first and only then expand the resulting algebra.

---

Flashcards for this section are as follows:

- Worked example: Given the accumulator $y[n]=\sum_{k=-\infty}^{n}x[k]$, what is its unit impulse response? ::@:: Step 1: set $x[k]=\delta[k]$. <br/> Step 2: substitute into the running sum to get $h[n]=\sum_{k=-\infty}^{n}\delta[k]$. <br/> Step 3: this sum is $0$ for $n<0$ and $1$ for $n\ge 0$. <br/> Step 4: therefore $h[n]=u[n]$.
- Worked example: Why is the accumulator $y[n]=\sum_{k=-\infty}^{n}x[k]$ causal? ::@:: Step 1: compute the impulse response as $h[n]=u[n]$. <br/> Step 2: check negative indices: $u[n]=0$ for all $n<0$. <br/> Step 3: therefore the causality criterion is satisfied.
- Worked example: Why is the accumulator $y[n]=\sum_{k=-\infty}^{n}x[k]$ not BIBO stable? ::@:: Step 1: use $h[n]=u[n]$. <br/> Step 2: test absolute summability: $\sum_{n=-\infty}^{\infty}|h[n]|=\sum_{n=0}^{\infty}1$. <br/> Step 3: the sum diverges, so the impulse response is not absolutely summable and the system is not BIBO stable.
- What lesson does the accumulator example teach about causality and stability? ::@:: A system may be perfectly causal and still be unstable if its memory keeps accumulating forever without enough decay.
- Worked example: In the interconnected discrete-time LTI system where $h_1[n]=(1/2)^n u[n+2]$ is followed by a parallel split into $h_2[n]=\delta[n]$ and $h_3[n]=u[n-1]$, what is the overall impulse response before simplifying the sum? ::@:: Step 1: combine the parallel branch as $h_2[n]+h_3[n]=\delta[n]+u[n-1]$. <br/> Step 2: cascade with $h_1[n]$ to get $h[n]=h_1[n]*(h_2[n]+h_3[n])$. <br/> Step 3: distribute convolution to obtain $h[n]=h_1[n]*\delta[n]+h_1[n]*u[n-1]$. <br/> Step 4: use the identity property to simplify this to $h[n]=h_1[n]+h_1[n]*u[n-1]$.
- How is the running-sum term computed in the interconnected system with $h_1[n]=(1/2)^n u[n+2]$ and $u[n-1]$? ::@:: For $n\ge -1$, one gets $(h_1*u[n-1])[n]=\sum_{m=-2}^{n-1}(1/2)^m=8-2^{-(n-1)}$ by evaluating a finite geometric series.
- Worked example: In the interconnected discrete-time LTI system where $h_1[n]=(1/2)^n u[n+2]$, $h_2[n]=\delta[n]$, and $h_3[n]=u[n-1]$, what is the final overall impulse response? ::@:: Step 1: start from $h[n]=h_1[n]+(h_1*u[n-1])[n]$. <br/> Step 2: for $n\ge -1$, compute $(h_1*u[n-1])[n]=\sum_{m=-2}^{n-1}(1/2)^m=8-2^{-(n-1)}$. <br/> Step 3: add the direct term $h_1[n]=2^{-n}$ to get $h[n]=2^{-n}+8-2^{-(n-1)}=8-2^{-n}$ for $n\ge -1$. <br/> Step 4: at $n=-2$, only the direct term remains, so $h[-2]=4$. <br/> Step 5: for $n<-2$, both terms vanish, so $h[n]=0$.
- Why is the interconnection example a good structural review of the time-domain LTI toolkit? ::@:: Because it combines series connection, parallel connection, and convolution with a step-like sequence, showing that block structure should be simplified before the algebra is expanded.
