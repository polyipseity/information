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

The __transfer function__ viewpoint compresses an LTI system into one rational function of $s$. Instead of re-solving the differential equation for every input, we identify the input-output relation once, then use poles, zeros, and interconnection algebra to predict behavior.

This builds on the Laplace-transform application story. Laplace transform turns the time-domain model into algebra; the transfer-function viewpoint interprets that algebra as the input-output law. The path: circuit or ODE model $\to$ zero-state Laplace equation $\to$ $H(s)$ or network parameters $\to$ poles/zeros and interconnection algebra $\to$ stability and response.

---

Flashcards for this section are as follows:

- What does the transfer-function viewpoint do? ::@:: It compresses an LTI system into $H(s)$ so poles, zeros, and block-diagram algebra replace re-solving the ODE for every input. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the path from a physical model to system interpretation? ::@:: Circuit or ODE $\to$ zero-state Laplace $\to$ $H(s)$ or network parameters $\to$ poles/zeros and interconnection $\to$ stability and response. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## definition of system and transfer functions

For a continuous-time LTI system under zero-state conditions:

$$H(s)=\frac{R(s)}{E(s)}=\mathcal{L}\{h(t)\}$$

where $e(t)$ is the input, $r(t)$ is the zero-state response, and $h(t)$ is the impulse response. Two equivalent readings: $H(s)$ is the zero-state input-output ratio in the Laplace domain, and it is also the Laplace transform of the impulse response.

For a single-port network (same port for excitation and response):

- Driving-point impedance: $H(s)=\frac{V_1(s)}{I_1(s)}$
- Driving-point admittance: $H(s)=\frac{I_1(s)}{V_1(s)}$

For a two-port network (different ports):

- Transfer impedance: $H(s)=\frac{V_2(s)}{I_1(s)}$
- Transfer admittance: $H(s)=\frac{I_2(s)}{V_1(s)}$
- Voltage transfer ratio: $H(s)=\frac{V_2(s)}{V_1(s)}$
- Current transfer ratio: $H(s)=\frac{I_2(s)}{I_1(s)}$

The name depends on the chosen excitation-response pair.

Resistor-divider example: $R_1$ and $R_2$ in series, input $V(s)$, loop current $I(s)$, output $V_2(s)$ across $R_2$. Then $\frac{I(s)}{V(s)}=\frac{1}{R_1+R_2}$ and $\frac{V_2(s)}{V(s)}=\frac{R_2}{R_1+R_2}$. The same circuit yields different transfer functions depending on which pair is chosen.

---

Flashcards for this section are as follows:

- What is the system function under zero-state conditions? ::@:: $H(s)=\frac{R(s)}{E(s)}=\mathcal{L}\{h(t)\}$, where $E(s)$ is the input transform, $R(s)$ is the zero-state output transform, and $h(t)$ is the impulse response. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What are the two equivalent readings of $H(s)$? ::@:: The zero-state input-output ratio in the Laplace domain, and the Laplace transform of the impulse response. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How do driving-point and transfer functions differ? ::@:: Driving-point uses same port for excitation and response; transfer uses different ports. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- For a single-port network, what are the two standard driving-point functions? ::@:: Driving-point impedance $\frac{V_1(s)}{I_1(s)}$ and driving-point admittance $\frac{I_1(s)}{V_1(s)}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- For a two-port network, what are the four standard transfer-function types? ::@:: Transfer impedance $\frac{V_2(s)}{I_1(s)}$, transfer admittance $\frac{I_2(s)}{V_1(s)}$, voltage transfer ratio $\frac{V_2(s)}{V_1(s)}$, and current transfer ratio $\frac{I_2(s)}{I_1(s)}$. <!--SR:!fsrs,2026-10-25T00:10:00.000Z,0,2.3065,2.11810397,1,1,0,1,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- In a series resistor divider with input $V(s)$ and output $V_2(s)$ across $R_2$, what are the driving-point admittance and voltage transfer ratio? ::@:: $\frac{I(s)}{V(s)}=\frac{1}{R_1+R_2}$ and $\frac{V_2(s)}{V(s)}=\frac{R_2}{R_1+R_2}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## dynamic circuits and one-port network functions

In the zero-state Laplace domain, dynamic circuits become transfer-function objects. Remove initial-condition sources first; initial conditions belong to the response, not to $H(s)$.

Passive-element impedances and admittances:

- $Z_R=R$, $Z_L=sL$, $Z_C=\frac{1}{sC}$
- $Y_R=\frac{1}{R}$, $Y_L=\frac{1}{sL}$, $Y_C=sC$

For a one-port network, the two basic functions are $Z(s)=\frac{V(s)}{I(s)}$ (driving-point impedance) and $Y(s)=\frac{I(s)}{V(s)}$ (driving-point admittance).

Mnemonic: impedance answers _voltage from current_; admittance answers _current from voltage_. Impedance suits series (shared current, voltages add); admittance suits parallel (shared voltage, currents add).

Series RLC example: $Z(s)=R+sL+\frac{1}{sC}$. If the output is the capacitor voltage, the transfer ratio is $\frac{V_C(s)}{V_{\text{in}}(s)}=\frac{\frac{1}{sC}}{R+sL+\frac{1}{sC}}=\frac{1}{LCs^2+RCs+1}$.

One-port functions and transfer ratios are not competing ideas. One-port functions describe the port seen by the source; transfer ratios describe how excitation distributes to an internal variable. The companion [Laplace transform](Laplace%20transform.md) note covers response calculation with initial conditions; this note covers zero-state network functions.

---

Flashcards for this section are as follows:

- What are the zero-state Laplace impedances and admittances of $R$, $L$, $C$? ::@:: $Z_R=R$, $Z_L=sL$, $Z_C=\frac{1}{sC}$; $Y_R=\frac{1}{R}$, $Y_L=\frac{1}{sL}$, $Y_C=sC$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does impedance suit series and admittance suit parallel? ::@:: Series: shared current, voltages add. Parallel: shared voltage, currents add. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- For a series RLC with output across the capacitor, what is $Z(s)$ and the transfer ratio? ::@:: $Z(s)=R+sL+\frac{1}{sC}$. $\frac{V_C(s)}{V_{\text{in}}(s)}=\frac{1}{LCs^2+RCs+1}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- When does a dynamic circuit become a transfer-function object in the Laplace domain? ::@:: After removing initial-condition source terms and working in the zero-state Laplace domain. The remaining algebra describes the intrinsic input-output law of the network rather than one particular total response. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## two-port descriptions and parameter matrices

A two-port network keeps both port voltages and currents visible. A scalar transfer function like $V_2/V_1$ works for one fixed excitation-response pair, but a matrix description handles loading, interconnection, and variable changes more flexibly.

Standard two-port parameter families:

- $z$-parameters: $\begin{bmatrix}V_1\\V_2\end{bmatrix}=\begin{bmatrix}z_{11}&z_{12}\\z_{21}&z_{22}\end{bmatrix}\begin{bmatrix}I_1\\I_2\end{bmatrix}$
- $y$-parameters: $\begin{bmatrix}I_1\\I_2\end{bmatrix}=\begin{bmatrix}y_{11}&y_{12}\\y_{21}&y_{22}\end{bmatrix}\begin{bmatrix}V_1\\V_2\end{bmatrix}$
- $ABCD$ (chain): $\begin{bmatrix}V_1\\I_1\end{bmatrix}=\begin{bmatrix}A&B\\C&D\end{bmatrix}\begin{bmatrix}V_2\\-I_2\end{bmatrix}$
- $h$-parameters: $\begin{bmatrix}V_1\\I_2\end{bmatrix}=\begin{bmatrix}h_{11}&h_{12}\\h_{21}&h_{22}\end{bmatrix}\begin{bmatrix}I_1\\V_2\end{bmatrix}$
- $g$-parameters: $\begin{bmatrix}I_1\\V_2\end{bmatrix}=\begin{bmatrix}g_{11}&g_{12}\\g_{21}&g_{22}\end{bmatrix}\begin{bmatrix}V_1\\I_2\end{bmatrix}$

Mnemonics: $z$ = voltages from currents (open-circuit). $y$ = currents from voltages (short-circuit). $h$ = mixed (voltage + current). $g$ = dual of $h$. $ABCD$ = chain parameters; matrices multiply in cascade order.

All describe the same physical network under the same sign convention. Choose the family that makes algebra, measurement, or interconnection easiest.

---

Flashcards for this section are as follows:

- Why use a two-port matrix instead of a scalar transfer ratio? ::@:: It keeps all four port variables visible, so loading, port choices, and interconnections can be handled without redefining the network. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What are the mnemonics for $z$, $y$, $h$, $g$, and $ABCD$? ::@:: $z$: voltages from currents. $y$: currents from voltages. $h$: mixed variables. $g$: dual of $h$. $ABCD$: chain parameters for cascades. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why are $ABCD$ parameters useful for cascades? ::@:: Cascaded two-ports multiply as matrices in cascade order. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What are the defining equations of the $z$-parameter and $y$-parameter descriptions? ::@:: $z$: $\begin{bmatrix}V_1\\V_2\end{bmatrix}=\begin{bmatrix}z_{11}&z_{12}\\z_{21}&z_{22}\end{bmatrix}\begin{bmatrix}I_1\\I_2\end{bmatrix}$. $y$: $\begin{bmatrix}I_1\\I_2\end{bmatrix}=\begin{bmatrix}y_{11}&y_{12}\\y_{21}&y_{22}\end{bmatrix}\begin{bmatrix}V_1\\V_2\end{bmatrix}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What are the defining equations of the $ABCD$, $h$, and $g$ parameter descriptions? ::@:: $ABCD$: $\begin{bmatrix}V_1\\I_1\end{bmatrix}=\begin{bmatrix}A&B\\C&D\end{bmatrix}\begin{bmatrix}V_2\\-I_2\end{bmatrix}$. $h$: $\begin{bmatrix}V_1\\I_2\end{bmatrix}=\begin{bmatrix}h_{11}&h_{12}\\h_{21}&h_{22}\end{bmatrix}\begin{bmatrix}I_1\\V_2\end{bmatrix}$. $g$: $\begin{bmatrix}I_1\\V_2\end{bmatrix}=\begin{bmatrix}g_{11}&g_{12}\\g_{21}&g_{22}\end{bmatrix}\begin{bmatrix}V_1\\I_2\end{bmatrix}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## obtaining transfer functions from circuit and differential-equation models

$H(s)$ bridges several descriptions:

- circuit diagram $\to$ $s$-domain equivalent model
- ODE $\to$ polynomial ratio
- interconnected blocks $\to$ combination rules

__from circuit diagrams.__

1. Choose excitation and response variables.
2. Draw the zero-state $s$-domain equivalent circuit.
3. Solve the algebraic equations.
4. Form $H(s)=\frac{R(s)}{E(s)}$.

Dynamic circuits produce rational functions whose poles encode time constants or oscillation modes.

__from differential equations.__

For an LCCDE $\sum_{k=0}^{n} a_k \frac{d^k r}{dt^k}=\sum_{j=0}^{m} b_j \frac{d^j e}{dt^j}$ with zero initial conditions, Laplace transform gives $\left(\sum_{k=0}^{n} a_k s^k\right)R(s)=\left(\sum_{j=0}^{m} b_j s^j\right)E(s)$, so:

$$H(s)=\frac{\sum_{j=0}^{m} b_j s^j}{\sum_{k=0}^{n} a_k s^k}$$

Derivatives become powers of $s$, so the ODE coefficients become polynomial coefficients. Initial conditions belong to the total response, not to $H(s)$.

Example: $\frac{d^2 r}{dt^2}+5\frac{dr}{dt}+6r=\frac{de}{dt}+2e$. With zero initial conditions, $(s^2+5s+6)R(s)=(s+2)E(s)$, so $H(s)=\frac{s+2}{(s+2)(s+3)}=\frac{1}{s+3}$ after reduction. The impulse response is $h(t)=e^{-3t}u(t)$. Pole-zero classification must use the reduced form.

---

Flashcards for this section are as follows:

- What are the three bridges $H(s)$ connects? ::@:: Circuit $\to$ $s$-domain model, ODE $\to$ polynomial ratio, blocks $\to$ combination rules. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- For the LCCDE $\sum a_k r^{(k)}=\sum b_j e^{(j)}$, what is $H(s)$? ::@:: $H(s)=\frac{\sum b_j s^j}{\sum a_k s^k}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why is the transfer function usually rational in $s$? ::@:: Derivatives become powers of $s$ in the Laplace domain. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why must initial conditions be excluded from $H(s)$? ::@:: $H(s)$ is the zero-state input-output law; initial conditions belong to the total response. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- For $r''+5r'+6r=e'+2e$, what is $H(s)$ and $h(t)$? ::@:: $H(s)=\frac{1}{s+3}$, $h(t)=e^{-3t}u(t)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the basic workflow for obtaining $H(s)=\frac{R(s)}{E(s)}$ from a circuit diagram? ::@:: Choose excitation and response variables, draw the zero-state $s$-domain equivalent circuit, solve the algebraic equations, then form $H(s)=\frac{R(s)}{E(s)}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- In the example $H(s)=\frac{s+2}{(s+2)(s+3)}$, why is $s=-2$ not a true pole or zero? ::@:: Because the factor $s+2$ cancels in the reduced form, so it is a removable common factor rather than a true pole or zero of the transfer function. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## poles, zeros, and pole-zero plots

Write the reduced $H(s)$ in factored form: $H(s)=K\frac{\prod_i (s-z_i)^{m_i}}{\prod_k (s-p_k)^{n_k}}$.

A zero at $s=z_0$ of multiplicity $m$ means $(s-z_0)^m$ in the numerator after reduction. A pole at $s=p_0$ of multiplicity $n$ means $(s-p_0)^n$ in the denominator after reduction.

Sketching convention: $\circ$ for zeros, $\times$ for poles, on the $s$-plane ($\Re(s)$ horizontal, $j\omega$ vertical). For multiplicity $>1$, annotate the order at the same location.

Examples:

- $H_1(s)=\frac{s+1}{(s+2)^2}$: zero at $s=-1$ (order 1), pole at $s=-2$ (order 2).
- $H_2(s)=\frac{(s+1)^3}{s+2}$: zero at $s=-1$ (order 3), pole at $s=-2$ (order 1).
- $H_3(s)=\frac{s+1}{s+2}$: one simple zero, one simple pole.

Count poles and zeros at infinity. For $H(s)=\frac{N(s)}{D(s)}$ with $n=\deg N$, $m=\deg D$:

- $m>n$ by $q$: $q$ zeros at infinity
- $n>m$ by $q$: $q$ poles at infinity
- $n=m$: neither

Total: exactly $\max(n,m)$ poles and $\max(n,m)$ zeros (including multiplicity and infinity). Low-pass systems often have zeros at infinity; differentiator-like systems have poles at infinity.

---

Flashcards for this section are as follows:

- In the $s$-plane, how are poles and zeros drawn? ::@:: $\times$ for poles, $\circ$ for zeros, $\Re(s)$ horizontal, $j\omega$ vertical. Multiplicity shown by order label. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- For $H_1(s)=\frac{s+1}{(s+2)^2}$, what are the poles, zeros, and infinity behavior? ::@:: Zero at $s=-1$ (order 1), pole at $s=-2$ (order 2), one zero at infinity. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- For $H_2(s)=\frac{(s+1)^3}{s+2}$, what are the poles, zeros, and infinity behavior? ::@:: Zero at $s=-1$ (order 3), pole at $s=-2$ (order 1), two poles at infinity. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How does degree counting give poles/zeros at infinity? ::@:: $\deg D>\deg N$ by $q$ $\Rightarrow$ $q$ zeros at $\infty$. $\deg N>\deg D$ by $q$ $\Rightarrow$ $q$ poles at $\infty$. Equal $\Rightarrow$ neither. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How many poles and zeros total? ::@:: Exactly $\max(\deg N,\deg D)$ of each, counting multiplicity and infinity. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## interconnection of continuous-time systems

Block-diagram algebra with $H(s)$ is straightforward.

__series and parallel one-port combinations.__

Series: $Z_{\text{eq}}(s)=Z_1(s)+Z_2(s)$ (shared current, voltages add). Parallel: $Y_{\text{eq}}(s)=Y_1(s)+Y_2(s)$ (shared voltage, currents add).

__parallel connection.__

$H(s)=H_1(s)+H_2(s)$.

__cascade connection.__

$H(s)=H_1(s)H_2(s)$. For two-port cascade: $T_{\text{eq}}(s)=T_1(s)T_2(s)$.

__negative feedback connection.__

With forward path $H_1(s)$ and feedback path $H_2(s)$, the relations $X_1=E-X_2$, $R=H_1X_1$, $X_2=H_2R$ give:

$$H(s)=\frac{H_1(s)}{1+H_1(s)H_2(s)}$$

Positive feedback: change the sign to $H(s)=\frac{H_1(s)}{1-H_1(s)H_2(s)}$. The loop gain $H_1H_2$ is the decisive quantity.

These formulas turn closed-loop block diagrams into one transfer function and make stability questions algebraic.

---

Flashcards for this section are as follows:

- What is the parallel, cascade, and feedback transfer function? ::@:: Parallel: $H=H_1+H_2$. Cascade: $H=H_1H_2$. Negative feedback: $H=\frac{H_1}{1+H_1H_2}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- For one-port series and parallel, what are the equivalents? ::@:: Series: $Z_{\text{eq}}=Z_1+Z_2$. Parallel: $Y_{\text{eq}}=Y_1+Y_2$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What changes between negative and positive feedback? ::@:: The denominator sign: $1+H_1H_2$ for negative, $1-H_1H_2$ for positive. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Derive the negative-feedback closed-loop transfer function. ::@:: With $X_1=E-X_2$, $R=H_1X_1$, $X_2=H_2R$: substitute to get $R=H_1(E-H_2R)$, so $R[1+H_1H_2]=H_1E$, giving $H=\frac{H_1}{1+H_1H_2}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why is the feedback formula important? ::@:: It turns a closed-loop block diagram into one algebraic transfer function whose poles can be studied for stability and response. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## stability of continuous-time systems

A system is BIBO stable if every bounded input gives a bounded zero-state output.

Time-domain criterion: $\int_{-\infty}^{\infty}|h(t)|\,dt\le M$ for some finite $M$ (absolute integrability). $s$-domain criterion: the ROC of $H(s)$ includes the imaginary axis.

For causal rational systems, the pole test applies:

- All poles strictly in the LHP $\Rightarrow$ stable
- Any RHP pole $\Rightarrow$ unstable
- Simple poles on the imaginary axis $\Rightarrow$ marginally stable
- Repeated poles on the imaginary axis $\Rightarrow$ unstable

Pole-location intuition:

__single real pole.__ $H(s)=\frac{1}{s+\alpha}$, $\alpha>0$: pole at $-\alpha$, $h(t)=e^{-\alpha t}u(t)$, decays $\Rightarrow$ stable. At origin: constant $\Rightarrow$ marginal. In RHP: exponential growth $\Rightarrow$ unstable.

__complex-conjugate poles.__ $-\alpha\pm j\omega_0$, $\alpha>0$: damped sinusoid $\Rightarrow$ stable. On imaginary axis: sustained oscillation $\Rightarrow$ marginal. In RHP: growing oscillation $\Rightarrow$ unstable.

__repeated poles.__ LHP: $H(s)=\frac{1}{(s+\alpha)^2}\leftrightarrow h(t)=te^{-\alpha t}u(t)$, exponential dominates $\Rightarrow$ stable. Imaginary axis: $\frac{1}{s^2}\leftrightarrow tu(t)$, grows without bound $\Rightarrow$ unstable.

Summary: stable = all poles in LHP. Unstable = any RHP pole or repeated imaginary-axis pole. Marginally stable = only simple imaginary-axis poles, no RHP poles.

Feedback stabilization example: $G(s)=\frac{1}{(s-1)(s+2)}$ (unstable, RHP pole at $s=1$) in negative feedback with gain $k$ gives $H(s)=\frac{1}{s^2+s+k-2}$, poles $p_{1,2}=\frac{-1\pm\sqrt{9-4k}}{2}$. Stable when $k>2$.

---

Flashcards for this section are as follows:

- What is the time-domain BIBO criterion? ::@:: $\int_{-\infty}^{\infty}|h(t)|dt\le M$ for some finite $M$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the $s$-domain stability criterion? ::@:: The ROC includes the imaginary axis. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- For causal rational systems, what pole test gives BIBO stability? ::@:: All poles strictly in the LHP. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How do simple vs. repeated imaginary-axis poles differ? ::@:: Simple: marginally stable. Repeated: unstable. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why is $\frac{1}{(s+\alpha)^2}$ stable but $\frac{1}{s^2}$ unstable? ::@:: LHP: exponential dominates polynomial, $te^{-\alpha t}$ decays. Imaginary axis: no decay, $tu(t)$ grows. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Stable, unstable, and marginally stable classification? ::@:: Stable: all poles in LHP. Unstable: RHP pole or repeated imaginary-axis pole. Marginally stable: only simple imaginary-axis poles. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- If $G(s)=\frac{1}{(s-1)(s+2)}$ in negative feedback with gain $k$, what is $H(s)$ and the stability condition? ::@:: $H(s)=\frac{1}{s^2+s+k-2}$, stable when $k>2$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why must nonzero initial conditions be excluded when defining $H(s)$? ::@:: $H(s)$ is defined from the zero-state input-output law of the system; initial conditions belong to the particular total response, not to the intrinsic system description. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why must $H(s)$ be in reduced form before pole-zero classification? ::@:: Pole and zero classification is defined only after removable common factors are cancelled; otherwise a cancelled factor would be mistaken for a true pole or zero. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
