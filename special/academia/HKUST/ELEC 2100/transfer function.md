---
aliases:
  - ELEC 2100 transfer function
  - ELEC2100 transfer function
  - HKUST ELEC 2100 transfer function
  - system function
  - system function in Laplace domain
  - transfer function
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/transfer_function
  - language/in/English
---

# transfer function

- HKUST ELEC 2100

---

## overview and modeling role

This note uses the __system function__ or __transfer function__ viewpoint to compress an LTI system into one rational function of $s$. Instead of repeatedly solving the same differential equation for different inputs, we first identify the input-output relation of the system, then use poles, zeros, and interconnection algebra to predict behavior.

This builds on the Laplace-transform application story. Laplace transform converts the time-domain model into algebra, and the transfer-function viewpoint then interprets that algebra as the system's input-output law: how inputs map to outputs, how one-port and two-port descriptions work, how subsystems interconnect, and whether the dynamics are stable. The path is: circuit or differential-equation model $\to$ zero-state Laplace equation $\to$ $H(s)$ or a network-parameter description $\to$ poles/zeros and interconnection algebra $\to$ stability and response interpretation.

---

Flashcards for this section are as follows:

- What is the main purpose of the transfer-function viewpoint in ELEC 2100? ::@:: It compresses an LTI system into one function $H(s)$ so poles, zeros, and block-diagram algebra replace re-solving the differential equation for every input.
- How does the transfer-function viewpoint build on Laplace-transform applications? ::@:: Laplace transform converts the physical model into algebra in $s$; the transfer-function viewpoint then interprets that algebra as the system's input-output law, including poles, zeros, port descriptions, interconnections, and stability.
- What is the path from a physical model to $H(s)$ and then to system interpretation? ::@:: Circuit or differential-equation model $\to$ zero-state Laplace equation $\to$ $H(s)$ or a network-parameter description $\to$ poles/zeros and interconnection algebra $\to$ stability and response interpretation.

## definition of system and transfer functions

For a continuous-time LTI system under zero-state conditions, $H(s)=\frac{R(s)}{E(s)}=\mathcal{L}\{h(t)\}$, where $e(t)$ is the input, $r(t)$ is the zero-state response, and $h(t)$ is the impulse response.

This equation has two equivalent readings.

- $H(s)$ is the zero-state input-output ratio in the Laplace domain.
- $H(s)$ is the Laplace transform of the impulse response, so it completely characterizes the LTI system in zero-state analysis.

Several excitation-response pairs are standard.

For a single-port network, the excitation and response are at the same port.

- Driving-point impedance: $H(s)=\frac{V_1(s)}{I_1(s)}$.
- Driving-point admittance: $H(s)=\frac{I_1(s)}{V_1(s)}$.

For a two-port network, the excitation and response are at different ports.

- Transfer impedance: $H(s)=\frac{V_2(s)}{I_1(s)}$.
- Transfer admittance: $H(s)=\frac{I_2(s)}{V_1(s)}$.
- Voltage transfer ratio: $H(s)=\frac{V_2(s)}{V_1(s)}$.
- Current transfer ratio: $H(s)=\frac{I_2(s)}{I_1(s)}$.

So "transfer function" is the broad idea, while the specific name depends on which excitation-response pair is chosen.

A resistor-divider example makes this concrete. Suppose $R_1$ and $R_2$ are in series, the input voltage $V(s)$ is applied across the pair, the loop current is $I(s)$, and the output is the voltage $V_2(s)$ across $R_2$. Then the driving-point admittance is $\frac{I(s)}{V(s)}=\frac{1}{R_1+R_2}$, while the voltage transfer function is $\frac{V_2(s)}{V(s)}=\frac{R_2}{R_1+R_2}$.

So the same physical circuit can yield different transfer functions depending on which excitation-response pair is chosen.

---

Flashcards for this section are as follows:

- What is the ELEC 2100 definition of the system function under zero-state conditions? ::@:: $H(s)=\frac{R(s)}{E(s)}=\mathcal{L}\{h(t)\}$, where $E(s)$ is the input transform, $R(s)$ is the zero-state output transform, and $h(t)$ is the impulse response.
- What are the two equivalent readings of $H(s)=\frac{R(s)}{E(s)}=\mathcal{L}\{h(t)\}$? ::@:: As the zero-state input-output ratio in the Laplace domain, and as the Laplace transform of the impulse response.
- In circuit language, how do driving-point functions and transfer functions differ? ::@:: A driving-point function uses excitation and response at the same port; a transfer function uses excitation and response at different ports.
- What are the standard driving-point functions for a single-port network? ::@:: Driving-point impedance $\frac{V_1(s)}{I_1(s)}$ and driving-point admittance $\frac{I_1(s)}{V_1(s)}$.
- What are the standard transfer-function types for a two-port network? ::@:: Transfer impedance $\frac{V_2(s)}{I_1(s)}$, transfer admittance $\frac{I_2(s)}{V_1(s)}$, voltage transfer ratio $\frac{V_2(s)}{V_1(s)}$, and current transfer ratio $\frac{I_2(s)}{I_1(s)}$.
- In a series resistor divider with input $V(s)$, loop current $I(s)$, and output $V_2(s)$ across $R_2$, what are the driving-point admittance and voltage transfer ratio? ::@:: $\frac{I(s)}{V(s)}=\frac{1}{R_1+R_2}$ and $\frac{V_2(s)}{V(s)}=\frac{R_2}{R_1+R_2}$.

## dynamic circuits and one-port network functions

Dynamic circuits become transfer-function objects in the zero-state Laplace domain. The network function is defined after initial-condition sources are removed; nonzero initial conditions belong to the response problem, not to the transfer function itself. In that zero-state setting, the basic passive-element models are

- $Z_R(s)=R$, $Z_L(s)=sL$, $Z_C(s)=\dfrac{1}{sC}$;
- $Y_R(s)=\dfrac{1}{R}$, $Y_L(s)=\dfrac{1}{sL}$, $Y_C(s)=sC$.

This is the transfer-function version of dynamic-circuit analysis: the same $s$-domain model used for response solving can also describe the network intrinsically.

For a one-port network, the two most basic functions are the driving-point impedance $Z(s)=\frac{V(s)}{I(s)}$ and the driving-point admittance $Y(s)=\frac{I(s)}{V(s)}$.

Mnemonic: impedance answers _voltage from current_, while admittance answers _current from voltage_. Impedance suits series combinations because series elements share current and voltages add. Admittance suits parallel combinations because parallel branches share voltage and currents add.

A zero-state example is a series RLC one-port. Its driving-point impedance is $Z(s)=R+sL+\frac{1}{sC}$, so its driving-point admittance is $Y(s)=\frac{1}{R+sL+\frac{1}{sC}}$.

If the response variable is moved from the input port to one component, the same algebra becomes a transfer ratio. For example, if the output is the capacitor voltage in the series RLC loop, then $\frac{V_C(s)}{V_{\text{in}}(s)}=\frac{\frac{1}{sC}}{R+sL+\frac{1}{sC}}=\frac{1}{LCs^2+RCs+1}$.

One-port functions and transfer ratios are not competing ideas: one-port functions describe the port seen by the source, while transfer ratios describe how the network distributes excitation to an internal or output variable. The companion [Laplace transform](Laplace%20transform.md) note covers the full response calculation with initial conditions and inverse transform; this note covers the zero-state network functions from the same $s$-domain model.

---

Flashcards for this section are as follows:

- When does a dynamic circuit become a transfer-function object in the Laplace domain? ::@:: In the zero-state Laplace domain, after initial-condition sources are removed, so the algebra describes the network's intrinsic input-output law rather than one particular total response.
- What are the zero-state Laplace-domain impedances and admittances of $R$, $L$, and $C$? ::@:: $Z_R=R$, $Z_L=sL$, $Z_C=\frac{1}{sC}$, and equivalently $Y_R=\frac{1}{R}$, $Y_L=\frac{1}{sL}$, $Y_C=sC$.
- What is the mnemonic for driving-point impedance vs. admittance? ::@:: Impedance answers _voltage from current_, so $Z(s)=V(s)/I(s)$. Admittance answers _current from voltage_, so $Y(s)=I(s)/V(s)$.
- Why does impedance suit series combinations and admittance suit parallel ones? ::@:: In series, current is common and voltages add, so impedances add directly. In parallel, voltage is common and currents add, so admittances add directly.
- For a zero-state series RLC one-port, what are $Z(s)$ and the capacitor-voltage transfer function $V_C(s)/V_{\text{in}}(s)$? ::@:: $Z(s)=R+sL+\frac{1}{sC}$. If the output is the capacitor voltage, then $\dfrac{V_C(s)}{V_{\text{in}}(s)}=\dfrac{\frac{1}{sC}}{R+sL+\frac{1}{sC}}=\dfrac{1}{LCs^2+RCs+1}$.

## two-port descriptions and parameter matrices

A two-port network keeps both port voltages and currents visible instead of collapsing to one scalar ratio. Scalar transfer functions such as $V_2/V_1$ or $I_2/I_1$ work when one excitation-response pair is fixed, but a matrix description handles loading, interconnection, or changes in input/output variable more flexibly.

The standard two-port parameter families are as follows.

Impedance parameters ($z$-parameters) satisfy $\begin{bmatrix}V_1\\V_2\end{bmatrix}=\begin{bmatrix}z_{11}&z_{12}\\z_{21}&z_{22}\end{bmatrix}\begin{bmatrix}I_1\\I_2\end{bmatrix}$.

Admittance parameters ($y$-parameters) satisfy $\begin{bmatrix}I_1\\I_2\end{bmatrix}=\begin{bmatrix}y_{11}&y_{12}\\y_{21}&y_{22}\end{bmatrix}\begin{bmatrix}V_1\\V_2\end{bmatrix}$.

Transmission or chain parameters ($ABCD$ parameters) satisfy $\begin{bmatrix}V_1\\I_1\end{bmatrix}=\begin{bmatrix}A&B\\C&D\end{bmatrix}\begin{bmatrix}V_2\\-I_2\end{bmatrix}$, using the common cascade convention with output current written as $-I_2$.

Hybrid parameters ($h$-parameters) satisfy $\begin{bmatrix}V_1\\I_2\end{bmatrix}=\begin{bmatrix}h_{11}&h_{12}\\h_{21}&h_{22}\end{bmatrix}\begin{bmatrix}I_1\\V_2\end{bmatrix}$.

Inverse-hybrid parameters ($g$-parameters) satisfy $\begin{bmatrix}I_1\\V_2\end{bmatrix}=\begin{bmatrix}g_{11}&g_{12}\\g_{21}&g_{22}\end{bmatrix}\begin{bmatrix}V_1\\I_2\end{bmatrix}$.

Mnemonics and usage cues:

- $z$: voltages from currents; useful for open-circuit reasoning.
- $y$: currents from voltages; useful for short-circuit reasoning.
- $h$: hybrid because one equation is voltage-based and the other current-based.
- $g$: the dual of $h$, swapping the mixed independent variables.
- $ABCD$: chain or transmission parameters; best for cascaded two-port networks because the matrices multiply directly in cascade order.

All of these descriptions refer to the same physical two-port network, provided the same sign convention is used. The goal is not to memorize five unrelated theories, but to choose the parameter family that makes the algebra, measurement, or interconnection easiest.

---

Flashcards for this section are as follows:

- Why can a two-port matrix description be more useful than a single scalar transfer ratio? ::@:: It keeps all four port variables visible, so loading, port choices, and interconnection effects can be handled without redefining the network.
- What are the defining equations of $z$-parameters and $y$-parameters? ::@:: $z$-parameters: $\begin{bmatrix}V_1\\V_2\end{bmatrix}=\begin{bmatrix}z_{11}&z_{12}\\z_{21}&z_{22}\end{bmatrix}\begin{bmatrix}I_1\\I_2\end{bmatrix}$. $y$-parameters: $\begin{bmatrix}I_1\\I_2\end{bmatrix}=\begin{bmatrix}y_{11}&y_{12}\\y_{21}&y_{22}\end{bmatrix}\begin{bmatrix}V_1\\V_2\end{bmatrix}$.
- What are the defining equations of $ABCD$, $h$, and $g$ parameters? ::@:: $ABCD$: $\begin{bmatrix}V_1\\I_1\end{bmatrix}=\begin{bmatrix}A&B\\C&D\end{bmatrix}\begin{bmatrix}V_2\\-I_2\end{bmatrix}$. $h$: $\begin{bmatrix}V_1\\I_2\end{bmatrix}=\begin{bmatrix}h_{11}&h_{12}\\h_{21}&h_{22}\end{bmatrix}\begin{bmatrix}I_1\\V_2\end{bmatrix}$. $g$: $\begin{bmatrix}I_1\\V_2\end{bmatrix}=\begin{bmatrix}g_{11}&g_{12}\\g_{21}&g_{22}\end{bmatrix}\begin{bmatrix}V_1\\I_2\end{bmatrix}$.
- What are the mnemonics for $z$, $y$, $h$, $g$, and $ABCD$? ::@:: $z$: voltages from currents. $y$: currents from voltages. $h$: hybrid mixed variables. $g$: inverse hybrid, the dual mixed-variable form. $ABCD$: chain or transmission parameters for cascades.
- Why are $ABCD$ parameters especially useful for cascaded two-port networks? ::@:: Because with the $\begin{bmatrix}V_1\\I_1\end{bmatrix}=T\begin{bmatrix}V_2\\-I_2\end{bmatrix}$ convention, cascaded two-ports multiply as matrices in cascade order.

## obtaining transfer functions from circuit and differential-equation models

The system function is the bridge among several continuous-time descriptions:

- circuit diagram $\to$ $s$-domain equivalent model;
- differential equation $\to$ algebraic polynomial ratio;
- interconnected blocks $\to$ algebraic combination rules.

__from circuit diagrams.__

The circuit route is straightforward.

1. Choose the excitation variable and response variable.
2. Draw the zero-state $s$-domain equivalent circuit.
3. Solve the resulting algebraic circuit equations.
4. Form $H(s)=\frac{R(s)}{E(s)}$.

The resistor-divider example above is the simplest case.  More interesting dynamic circuits produce rational functions whose poles encode time constants or oscillation modes.

__from differential equations.__

Suppose the system satisfies a linear constant-coefficient differential equation $\sum_{k=0}^{n} a_k \frac{d^k r(t)}{dt^k}=\sum_{j=0}^{m} b_j \frac{d^j e(t)}{dt^j}$.  Under zero initial conditions, bilateral or unilateral Laplace transform gives $\left(\sum_{k=0}^{n} a_k s^k\right)R(s)=\left(\sum_{j=0}^{m} b_j s^j\right)E(s)$, so $H(s)=\frac{R(s)}{E(s)}=\frac{\sum_{j=0}^{m} b_j s^j}{\sum_{k=0}^{n} a_k s^k}$.

This is why the transfer function of an LTI system is usually a rational function of $s$: derivatives become powers of $s$, and the coefficients of the differential equation become the polynomial coefficients of numerator and denominator.

Note that nonzero initial conditions belong to the total response, not to the transfer function.  The transfer function comes from the zero-state input-output law.  Initial-condition terms should be removed before defining $H(s)$.

A short example shows reduction.  Suppose $\frac{d^2 r}{dt^2}+5\frac{dr}{dt}+6r=\frac{de}{dt}+2e$.  With zero initial conditions, $(s^2+5s+6)R(s)=(s+2)E(s)$, so $H(s)=\frac{R(s)}{E(s)}=\frac{s+2}{(s+2)(s+3)}=\frac{1}{s+3}$.  The cancelled factor $s+2$ is a removable common factor, not a true pole-zero pair.  So the true system function is $H(s)=\frac{1}{s+3}$ and the impulse response is $h(t)=e^{-3t}u(t)$.

Pole-zero classification must always use the reduced form.

---

Flashcards for this section are as follows:

- What are the three description bridges connected by $H(s)$? ::@:: Circuit diagram $\to$ $s$-domain equivalent model, differential equation $\to$ algebraic polynomial ratio, and interconnected blocks $\to$ algebraic combination rules.
- What is the workflow for obtaining $H(s)=\frac{R(s)}{E(s)}$ from a circuit diagram? ::@:: Choose excitation and response variables, draw the zero-state $s$-domain equivalent circuit, solve the algebraic equations, and form $H(s)=\frac{R(s)}{E(s)}$.
- For the general LCCDE $\sum_{k=0}^{n} a_k \frac{d^k r}{dt^k}=\sum_{j=0}^{m} b_j \frac{d^j e}{dt^j}$, what is the zero-state transfer function? ::@:: $H(s)=\frac{R(s)}{E(s)}=\frac{\sum_{j=0}^{m} b_j s^j}{\sum_{k=0}^{n} a_k s^k}$.
- Why is the transfer function usually rational in $s$? ::@:: Laplace transform converts derivatives into powers of $s$, so the differential equation becomes a polynomial relation between $R(s)$ and $E(s)$.
- Why must nonzero initial conditions be excluded from $H(s)$? ::@:: Because $H(s)$ is defined from the zero-state input-output law, while initial conditions belong to one particular total response.
- If $\frac{d^2 r}{dt^2}+5\frac{dr}{dt}+6r=\frac{de}{dt}+2e$, what transfer function and impulse response follow under zero initial conditions? ::@:: $(s^2+5s+6)R(s)=(s+2)E(s)$, so $H(s)=\frac{s+2}{(s+2)(s+3)}=\frac{1}{s+3}$ after reduction. $h(t)=e^{-3t}u(t)$.
- Why is $s=-2$ not a true pole or zero of the reduced $H(s)$? ::@:: Because $s+2$ cancels in the reduced form, making it a removable common factor.

## poles, zeros, and pole-zero plots

For pole-zero analysis, write the reduced rational transfer function in factored form $H(s)=K\frac{\prod_i (s-z_i)^{m_i}}{\prod_k (s-p_k)^{n_k}}$.

A zero at $s=z_0$ of multiplicity $m$ means the numerator contains $(s-z_0)^m$ after reduction.  A pole at $s=p_0$ of multiplicity $n$ means the denominator contains $(s-p_0)^n$ after reduction.

The course sketching convention:

- use $\circ$ for zeros;
- use $\times$ for poles;
- place them on the complex $s$-plane, with horizontal axis $\Re(s)$ and vertical axis $j\omega$;
- if multiplicity is greater than $1$, keep the same location and annotate the order rather than moving the point.

Examples:

- $H_1(s)=\frac{s+1}{(s+2)^2}$ has one zero at $s=-1$ of multiplicity $1$ and one pole at $s=-2$ of multiplicity $2$.
- $H_2(s)=\frac{(s+1)^3}{s+2}$ has one zero at $s=-1$ of multiplicity $3$ and one pole at $s=-2$ of multiplicity $1$.
- $H_3(s)=\frac{s+1}{s+2}$ has one simple zero and one simple pole.

Poles and zeros at infinity must also be counted.  For a reduced rational function $H(s)=\frac{N(s)}{D(s)}$ with $n=\deg N$ and $m=\deg D$:

- if $m>n$ by $q$, then there are $q$ zeros at infinity;
- if $n>m$ by $q$, then there are $q$ poles at infinity;
- if $n=m$, there is neither a pole nor a zero at infinity.

So after reduction, a rational function has exactly $\max(n,m)$ poles and exactly $\max(n,m)$ zeros when multiplicity and the point at infinity are included.

This degree-counting viewpoint explains why low-pass-like systems often have zeros at infinity while differentiator-like systems can have poles at infinity.

---

Flashcards for this section are as follows:

- For pole-zero analysis, why must $H(s)$ be in reduced factored form? ::@:: Pole and zero classification requires cancelling all removable common factors first; otherwise a cancelled factor would be mistaken for a true pole or zero.
- In the course convention, how are poles, zeros, and multiplicities shown on the $s$-plane? ::@:: $\times$ for poles, $\circ$ for zeros, horizontal axis $\Re(s)$, vertical axis $j\omega$, and multiplicity shown by an order label at the same location.
- For $H_1(s)=\frac{s+1}{(s+2)^2}$, what are the finite zero, finite pole, and infinity behavior? ::@:: Zero at $s=-1$ (multiplicity 1). Pole at $s=-2$ (multiplicity 2). One zero at infinity since $\deg D>\deg N$ by 1.
- For $H_2(s)=\frac{(s+1)^3}{s+2}$, what are the finite zero, finite pole, and infinity behavior? ::@:: Zero at $s=-1$ (multiplicity 3). Pole at $s=-2$ (multiplicity 1). Two poles at infinity since $\deg N>\deg D$ by 2.
- How does degree counting determine poles or zeros at infinity for $H(s)=\frac{N(s)}{D(s)}$? ::@:: $\deg D>\deg N$ by $q$ gives $q$ zeros at infinity. $\deg N>\deg D$ by $q$ gives $q$ poles at infinity. Equal degrees give neither.
- How many poles and zeros total when multiplicity and infinity are included? ::@:: Exactly $\max(\deg N,\deg D)$ of each.

## interconnection of continuous-time systems

Once a subsystem is represented by $H(s)$, block-diagram algebra is straightforward.  At the signal-flow level, the canonical combinations are parallel, cascade, and feedback.  At the one-port network level, the canonical combinations are series and parallel, handled with impedance and admittance.

__series and parallel one-port combinations.__

If two one-port subnetworks are placed in series, the current is common and the voltages add, so $Z_{\text{eq}}(s)=Z_1(s)+Z_2(s)$. If two one-port subnetworks are placed in parallel, the voltage is common and the currents add, so $Y_{\text{eq}}(s)=Y_1(s)+Y_2(s)$.

This is why impedance works for series and admittance works for parallel.

__parallel connection.__

If the same input $E(s)$ drives two subsystems in parallel and the outputs are added, then $R(s)=E(s)H_1(s)+E(s)H_2(s)=E(s)[H_1(s)+H_2(s)]$, so $H(s)=H_1(s)+H_2(s)$.

__cascade connection.__

If the output of the first subsystem drives the second, then $R(s)=E(s)H_1(s)H_2(s)$, so $H(s)=H_1(s)H_2(s)$.

The same idea extends to two-port transmission descriptions. If two two-port networks with transmission matrices $T_1(s)$ and $T_2(s)$ are cascaded under a consistent sign convention, then the equivalent transmission matrix is $T_{\text{eq}}(s)=T_1(s)T_2(s)$.

So scalar cascade multiplies scalar transfer functions, while two-port cascade multiplies transmission matrices.

__negative feedback connection.__

For the standard negative-feedback structure with forward path $H_1(s)$ and feedback path $H_2(s)$, the internal relations are $X_1(s)=E(s)-X_2(s)$, $R(s)=H_1(s)X_1(s)$, and $X_2(s)=H_2(s)R(s)$.  Substituting gives $R(s)=H_1(s)[E(s)-H_2(s)R(s)]$, so $R(s)[1+H_1(s)H_2(s)]=H_1(s)E(s)$, and therefore $H(s)=\frac{R(s)}{E(s)}=\frac{H_1(s)}{1+H_1(s)H_2(s)}$.

If the same loop uses __positive__ feedback instead, only the sign at the summing node changes, and the closed-loop transfer function becomes $H(s)=\frac{H_1(s)}{1-H_1(s)H_2(s)}$.

The loop gain $H_1(s)H_2(s)$ is the decisive quantity: negative feedback gives $1+H_1H_2$ in the denominator, while positive feedback gives $1-H_1H_2$.

These formulas turn complicated block diagrams into one closed-loop transfer function and make stability questions algebraic.

---

Flashcards for this section are as follows:

- What is the parallel-form equivalent transfer function? ::@:: $H(s)=H_1(s)+H_2(s)$.
- What are the one-port equivalent relations for series and parallel combinations? ::@:: Series: $Z_{\text{eq}}(s)=Z_1(s)+Z_2(s)$. Parallel: $Y_{\text{eq}}(s)=Y_1(s)+Y_2(s)$.
- What is the cascade-form equivalent transfer function? ::@:: $H(s)=H_1(s)H_2(s)$.
- For two cascaded two-port networks with transmission matrices $T_1(s)$ and $T_2(s)$, what is the equivalent transmission matrix? ::@:: $T_{\text{eq}}(s)=T_1(s)T_2(s)$, assuming the same sign convention throughout.
- Derive the negative-feedback closed-loop transfer function. ::@:: With $X_1=E-X_2$, $R=H_1X_1$, and $X_2=H_2R$, substitute to get $R=H_1(E-H_2R)$. Rearranging gives $R[1+H_1H_2]=H_1E$, so $H=\frac{H_1}{1+H_1H_2}$.
- What changes between negative and positive feedback in the closed-loop formula? ::@:: Only the sign in the denominator: negative feedback gives $\dfrac{H_1}{1+H_1H_2}$, positive feedback gives $\dfrac{H_1}{1-H_1H_2}$.
- Why is the feedback formula $\frac{H_1(s)}{1\pm H_1(s)H_2(s)}$ useful? ::@:: It converts a closed-loop block diagram into one transfer function whose poles can be studied directly for stability.

## stability of continuous-time systems

A continuous-time system is BIBO stable if every bounded input produces a bounded zero-state output.

The exact time-domain criterion is $\int_{-\infty}^{\infty}|h(t)|\,dt\le M$ for some finite constant $M$.  In words, the impulse response must be absolutely integrable.

In the $s$-domain, the equivalent criterion is that the ROC of $H(s)=\mathcal{L}\{h(t)\}$ includes the imaginary axis.  For causal rational systems, this reduces to the pole test:

- all poles strictly in the left half-plane $\Rightarrow$ stable;
- any pole in the right half-plane $\Rightarrow$ unstable;
- simple poles on the imaginary axis $\Rightarrow$ marginally stable (non-decaying oscillation or constant component);
- repeated poles on the imaginary axis $\Rightarrow$ unstable.

The pole-location intuition by case:

__single real pole.__

$H(s)=\frac{1}{s+\alpha}$ with $\alpha>0$ has pole at $-\alpha$ and $h(t)=e^{-\alpha t}u(t)$, so the response decays and the system is stable.

If the pole moves to the origin, the response becomes a constant and is only marginal.  If it moves to the right half-plane, the response grows exponentially and the system is unstable.

__complex-conjugate poles.__

For poles $-\alpha\pm j\omega_0$ with $\alpha>0$, $h(t)=e^{-\alpha t}\sin(\omega_0 t)u(t)$ or a similar damped sinusoid, so the oscillation decays and the system is stable.

If the poles lie exactly on the imaginary axis $\pm j\omega_0$, the oscillation is sustained, so the system is only marginal.  If they move into the right half-plane, the oscillation grows and the system is unstable.

__repeated poles.__

A repeated left-half-plane pole, $H(s)=\frac{1}{(s+\alpha)^2} \quad\Longleftrightarrow\quad h(t)=t e^{-\alpha t}u(t)$, still decays because the exponential dominates the polynomial.  So repeated poles in the strict left half-plane can still be stable.

But repeated poles on the imaginary axis are different.  At the origin, $\frac{1}{s^2}\longleftrightarrow t u(t)$, which grows without bound.  So repeated poles on the imaginary axis are unstable rather than marginal.

The course summary:

- __stable__: all poles strictly in the LHP;
- __unstable__: any RHP pole, or any repeated pole on the imaginary axis;
- __marginally stable__: only simple poles on the imaginary axis and no RHP poles.

A useful application is feedback stabilization.  Suppose the open-loop subsystem is $G(s)=\frac{1}{(s-1)(s+2)}$, which is unstable because of the right-half-plane pole $s=1$.  Place it in standard negative feedback with constant gain $k$.  The closed-loop transfer function is $H(s)=\frac{G(s)}{1+kG(s)}=\frac{1}{(s-1)(s+2)+k}=\frac{1}{s^2+s+k-2}$.  The poles are $p_{1,2}=\frac{-1\pm\sqrt{9-4k}}{2}$.  For both poles in the left half-plane, $k>2$.

So negative feedback can move poles from an unstable open-loop position into a stable closed-loop position.

---

Flashcards for this section are as follows:

- What is the time-domain BIBO stability criterion? ::@:: The impulse response must be absolutely integrable: $\int_{-\infty}^{\infty}|h(t)|dt\le M$ for some finite $M$.
- What is the $s$-domain stability criterion for $H(s)=\mathcal{L}\{h(t)\}$? ::@:: The ROC must include the imaginary axis.
- For a causal rational system, what pole-location test gives asymptotic BIBO stability? ::@:: All poles must lie strictly in the left half-plane.
- How do simple vs. repeated poles on the imaginary axis differ in stability? ::@:: Simple poles on the imaginary axis give marginally stable non-decaying behavior; repeated poles give unbounded growth and are unstable.
- For a single real pole at $s=-\alpha$ with $\alpha>0$, what impulse response and stability result? ::@:: $H(s)=\frac{1}{s+\alpha}$ gives $h(t)=e^{-\alpha t}u(t)$, which decays, so the system is stable.
- For complex-conjugate poles $-\alpha\pm j\omega_0$, what time-domain behavior? ::@:: A damped sinusoid such as $e^{-\alpha t}\sin(\omega_0 t)u(t)$; stable when $\alpha>0$, marginal on the imaginary axis, unstable in the RHP.
- Why is $H(s)=\frac{1}{(s+\alpha)^2}$ stable but $\frac{1}{s^2}$ unstable? ::@:: In the LHP the exponential decay dominates the polynomial factor, so $t e^{-\alpha t}$ still decays. On the imaginary axis there is no decaying exponential, so $t u(t)$ grows without bound.
- Summarize the stable/unstable/marginally stable classification. ::@:: Stable: all poles strictly in the LHP. Unstable: any RHP pole or any repeated pole on the imaginary axis. Marginally stable: only simple poles on the imaginary axis and no RHP poles.
- If $G(s)=\frac{1}{(s-1)(s+2)}$ is in negative feedback with gain $k$, what is the closed-loop transfer function? ::@:: $H(s)=\frac{G(s)}{1+kG(s)}=\frac{1}{s^2+s+k-2}$.
- What are the closed-loop poles and what condition on $k$ stabilizes the system? ::@:: $p_{1,2}=\frac{-1\pm\sqrt{9-4k}}{2}$, stable when $k>2$.
