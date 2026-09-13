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

This note uses the __system function__ or __transfer function__ viewpoint to compress an LTI system into one rational function of $s$. Instead of repeatedly solving the same differential equation for different inputs, we first identify the intrinsic input-output relation of the system, then use poles, zeros, and interconnection algebra to predict behavior.

This is the natural continuation of Laplace-transform applications. Laplace transform converts the time-domain model into algebra, and the transfer-function viewpoint then asks what that algebra says about the system itself: how inputs are mapped to outputs, how one-port and two-port descriptions are organized, how subsystems interconnect, and whether the resulting dynamics are stable. The bridge can be summarized as circuit or differential-equation model $\to$ zero-state Laplace equation $\to$ $H(s)$ or a network-parameter description $\to$ poles/zeros and interconnection algebra $\to$ stability and response interpretation.

---

Flashcards for this section are as follows:

- What is the main purpose of the transfer-function viewpoint in ELEC 2100, in terms of $H(s)$? ::@:: It compresses an LTI system into one function $H(s)$ so the same system can be analyzed through poles, zeros, and block-diagram algebra instead of re-solving the full differential equation for every input.
- How does the transfer-function viewpoint continue the Laplace-transform application story after the model has been converted into algebra in $s$? ::@:: Laplace transform first converts the physical model into algebra in $s$, then the transfer-function viewpoint interprets that algebra as the intrinsic input-output law of the system, including poles, zeros, one-port or two-port descriptions, interconnections, and stability.
- What is the bridge from a physical model to $H(s)$ and then to qualitative system interpretation? ::@:: Circuit or differential-equation model $\to$ zero-state Laplace equation $\to$ $H(s)$ or a network-parameter description $\to$ poles/zeros and interconnection algebra $\to$ stability and response interpretation.

## definition of system and transfer functions

For a continuous-time LTI system under __zero-state__ conditions, $H(s)=\frac{R(s)}{E(s)}=\mathcal{L}\{h(t)\}$, where $e(t)$ is the input, $r(t)$ is the zero-state response, and $h(t)$ is the impulse response.

This equation should be read in two equivalent ways.

- __Input-output ratio__: $H(s)$ tells how the transformed response relates to the transformed excitation when initial conditions are zero.
- __Impulse-response transform__: $H(s)$ is the Laplace transform of the system's impulse response, so it completely characterizes an LTI system in zero-state analysis.

Several standard excitation-response choices are useful.

For a __single-port network__, the excitation and response are measured at the same port.

- Driving-point impedance: $H(s)=\frac{V_1(s)}{I_1(s)}$.
- Driving-point admittance: $H(s)=\frac{I_1(s)}{V_1(s)}$.

For a __two-port network__, the excitation and response are measured at different ports.

- Transfer impedance: $H(s)=\frac{V_2(s)}{I_1(s)}$.
- Transfer admittance: $H(s)=\frac{I_2(s)}{V_1(s)}$.
- Voltage transfer ratio: $H(s)=\frac{V_2(s)}{V_1(s)}$.
- Current transfer ratio: $H(s)=\frac{I_2(s)}{I_1(s)}$.

So "transfer function" is the broad idea, while the specific physical name depends on what excitation and response pair is chosen.

A simple resistor-divider example makes this concrete. Suppose $R_1$ and $R_2$ are in series, the input voltage $V(s)$ is applied across the whole pair, the loop current is $I(s)$, and the output is the voltage $V_2(s)$ across $R_2$. Then the driving-point admittance is $\frac{I(s)}{V(s)}=\frac{1}{R_1+R_2}$, while the voltage transfer function is $\frac{V_2(s)}{V(s)}=\frac{R_2}{R_1+R_2}$.

So the same physical circuit can yield different transfer functions depending on which excitation-response pair is chosen.

---

Flashcards for this section are as follows:

- What is the ELEC 2100 definition of the system function under zero-state conditions, written in terms of $R(s)$, $E(s)$, and $h(t)$? ::@:: $H(s)=\frac{R(s)}{E(s)}=\mathcal{L}\{h(t)\}$, where $E(s)$ is the input transform, $R(s)$ is the zero-state output transform, and $h(t)$ is the impulse response.
- What are the two equivalent ways to interpret the formula $H(s)=\frac{R(s)}{E(s)}=\mathcal{L}\{h(t)\}$? ::@:: As the zero-state input-output ratio in the Laplace domain and as the Laplace transform of the impulse response.
- In circuit language, how do driving-point functions and transfer functions differ in terms of measurement ports? ::@:: A driving-point function uses excitation and response measured at the same port, while a transfer function uses excitation and response measured at different ports.
- For a single-port network, what are the two standard driving-point functions in terms of $V_1(s)$ and $I_1(s)$? ::@:: Driving-point impedance $\frac{V_1(s)}{I_1(s)}$ and driving-point admittance $\frac{I_1(s)}{V_1(s)}$.
- For a two-port network, what are the standard transfer-function types in terms of $V_1(s)$, $V_2(s)$, $I_1(s)$, and $I_2(s)$? ::@:: Transfer impedance $\frac{V_2(s)}{I_1(s)}$, transfer admittance $\frac{I_2(s)}{V_1(s)}$, voltage transfer ratio $\frac{V_2(s)}{V_1(s)}$, and current transfer ratio $\frac{I_2(s)}{I_1(s)}$.
- In a series resistor divider with input $V(s)$, loop current $I(s)$, and output $V_2(s)$ across $R_2$, what are the driving-point admittance and the voltage transfer ratio? ::@:: $\frac{I(s)}{V(s)}=\frac{1}{R_1+R_2}$ and $\frac{V_2(s)}{V(s)}=\frac{R_2}{R_1+R_2}$.

## dynamic circuits and one-port network functions

Dynamic circuits become transfer-function objects after moving to the __zero-state__ Laplace domain. The intrinsic network function is defined after initial-condition sources are removed; nonzero initial conditions belong to the response problem, not to the definition of the transfer function itself. In that zero-state setting, the basic passive-element models are

- $Z_R(s)=R$, $Z_L(s)=sL$, $Z_C(s)=\dfrac{1}{sC}$;
- $Y_R(s)=\dfrac{1}{R}$, $Y_L(s)=\dfrac{1}{sL}$, $Y_C(s)=sC$.

This is the transfer-function version of dynamic-circuit analysis: the same $s$-domain model used for response solving can also be read as an intrinsic network description.

For a one-port network, the two most basic functions are the __driving-point impedance__ $Z(s)=\frac{V(s)}{I(s)}$ and the __driving-point admittance__ $Y(s)=\frac{I(s)}{V(s)}$.

Mnemonic: impedance answers _voltage from current_, while admittance answers _current from voltage_. Impedance is usually the natural description for series combinations because series elements share current and voltages add. Admittance is usually the natural description for parallel combinations because parallel branches share voltage and currents add.

A standard zero-state example is a series RLC one-port. Its driving-point impedance is $Z(s)=R+sL+\frac{1}{sC}$, so its driving-point admittance is $Y(s)=\frac{1}{R+sL+\frac{1}{sC}}$.

If the response variable is moved from the input port to one component, the same algebra becomes an ordinary transfer ratio. For example, if the output is the capacitor voltage in the series RLC loop, then $\frac{V_C(s)}{V_{\text{in}}(s)}=\frac{\frac{1}{sC}}{R+sL+\frac{1}{sC}}=\frac{1}{LCs^2+RCs+1}$.

So one-port functions and transfer ratios are not competing ideas: one-port functions describe the port seen by the source, while transfer ratios describe how that same network distributes excitation to an internal or output variable. The companion [Laplace transform](Laplace%20transform.md) note emphasizes the full response calculation with initial conditions and inverse transform; this note emphasizes the intrinsic zero-state network functions exposed by the same $s$-domain model.

---

Flashcards for this section are as follows:

- When does a dynamic circuit become a transfer-function or network-function object in the Laplace domain? ::@:: After moving to the zero-state Laplace domain and removing initial-condition source terms, so the remaining algebra describes the intrinsic input-output law of the network rather than one particular total response.
- What are the basic zero-state Laplace-domain impedances and admittances of $R$, $L$, and $C$? ::@:: $Z_R=R$, $Z_L=sL$, $Z_C=\frac{1}{sC}$, and equivalently $Y_R=\frac{1}{R}$, $Y_L=\frac{1}{sL}$, $Y_C=sC$.
- What is the mnemonic difference between driving-point impedance $Z(s)=V(s)/I(s)$ and driving-point admittance $Y(s)=I(s)/V(s)$? ::@:: Impedance answers _voltage from current_, so $Z(s)=V(s)/I(s)$. Admittance answers _current from voltage_, so $Y(s)=I(s)/V(s)$.
- Why is impedance usually the natural description for series one-port combinations, while admittance is usually the natural description for parallel one-port combinations? ::@:: In series, the current is common and voltages add, so impedances add directly. In parallel, the voltage is common and currents add, so admittances add directly.
- For a zero-state series RLC one-port, what are $Z(s)$ and the capacitor-voltage transfer function $V_C(s)/V_{\text{in}}(s)$? ::@:: $Z(s)=R+sL+\frac{1}{sC}$. <br/> If the output is the capacitor voltage, then $\dfrac{V_C(s)}{V_{\text{in}}(s)}=\dfrac{\frac{1}{sC}}{R+sL+\frac{1}{sC}}=\dfrac{1}{LCs^2+RCs+1}$.

## two-port descriptions and parameter matrices

A two-port network keeps both port voltages and currents visible instead of collapsing immediately to one scalar ratio. Scalar transfer functions such as $V_2/V_1$ or $I_2/I_1$ are often sufficient when one excitation-response pair is fixed, but a matrix description is more informative when loading, interconnection, or the choice of input/output variable may change.

The standard two-port parameter families are the following.

__impedance parameters__ ($z$-parameters) satisfy $\begin{bmatrix}V_1\\V_2\end{bmatrix}=\begin{bmatrix}z_{11}&z_{12}\\z_{21}&z_{22}\end{bmatrix}\begin{bmatrix}I_1\\I_2\end{bmatrix}$.

__admittance parameters__ ($y$-parameters) satisfy $\begin{bmatrix}I_1\\I_2\end{bmatrix}=\begin{bmatrix}y_{11}&y_{12}\\y_{21}&y_{22}\end{bmatrix}\begin{bmatrix}V_1\\V_2\end{bmatrix}$.

__transmission__ or __chain__ parameters ($ABCD$ parameters) satisfy $\begin{bmatrix}V_1\\I_1\end{bmatrix}=\begin{bmatrix}A&B\\C&D\end{bmatrix}\begin{bmatrix}V_2\\-I_2\end{bmatrix}$, using the common cascade convention with output current written as $-I_2$.

__hybrid parameters__ ($h$-parameters) satisfy $\begin{bmatrix}V_1\\I_2\end{bmatrix}=\begin{bmatrix}h_{11}&h_{12}\\h_{21}&h_{22}\end{bmatrix}\begin{bmatrix}I_1\\V_2\end{bmatrix}$.

__inverse-hybrid__ or __inverse transmission hybrid__ parameters ($g$-parameters) satisfy $\begin{bmatrix}I_1\\V_2\end{bmatrix}=\begin{bmatrix}g_{11}&g_{12}\\g_{21}&g_{22}\end{bmatrix}\begin{bmatrix}V_1\\I_2\end{bmatrix}$.

Brief mnemonics and usage cues help keep these straight.

- __z__: voltages from currents; useful when open-circuit reasoning is natural.
- __y__: currents from voltages; useful when short-circuit reasoning is natural.
- __h__: hybrid because one equation is voltage-based and the other current-based.
- __g__: the dual of $h$, swapping the mixed independent variables.
- __ABCD__: transmission or chain parameters; best for cascaded two-port networks because the matrices multiply directly in cascade order.

All of these descriptions refer to the same physical two-port network, provided the same sign convention is used. So the goal is not to memorize five unrelated theories, but to choose the parameter family that makes the algebra, measurement, or interconnection easiest.

---

Flashcards for this section are as follows:

- Why can a two-port matrix description be more useful than a single scalar transfer ratio? ::@:: Because it keeps all four port variables visible, so loading, port choices, and interconnection effects can be handled without redefining the network from scratch each time.
- What are the defining equations of the $z$-parameter and $y$-parameter descriptions of a two-port network? ::@:: $z$-parameters: $\begin{bmatrix}V_1\\V_2\end{bmatrix}=\begin{bmatrix}z_{11}&z_{12}\\z_{21}&z_{22}\end{bmatrix}\begin{bmatrix}I_1\\I_2\end{bmatrix}$. <br/> $y$-parameters: $\begin{bmatrix}I_1\\I_2\end{bmatrix}=\begin{bmatrix}y_{11}&y_{12}\\y_{21}&y_{22}\end{bmatrix}\begin{bmatrix}V_1\\V_2\end{bmatrix}$.
- What are the defining equations of the $ABCD$, $h$, and $g$ parameter descriptions of a two-port network? ::@:: $ABCD$: $\begin{bmatrix}V_1\\I_1\end{bmatrix}=\begin{bmatrix}A&B\\C&D\end{bmatrix}\begin{bmatrix}V_2\\-I_2\end{bmatrix}$. <br/> $h$: $\begin{bmatrix}V_1\\I_2\end{bmatrix}=\begin{bmatrix}h_{11}&h_{12}\\h_{21}&h_{22}\end{bmatrix}\begin{bmatrix}I_1\\V_2\end{bmatrix}$. <br/> $g$: $\begin{bmatrix}I_1\\V_2\end{bmatrix}=\begin{bmatrix}g_{11}&g_{12}\\g_{21}&g_{22}\end{bmatrix}\begin{bmatrix}V_1\\I_2\end{bmatrix}$.
- What are the quickest mnemonics for the common two-port parameter families $z$, $y$, $h$, $g$, and $ABCD$? ::@:: $z$: voltages from currents. <br/> $y$: currents from voltages. <br/> $h$: hybrid mixed variables. <br/> $g$: inverse hybrid, the dual mixed-variable form. <br/> $ABCD$: chain or transmission parameters for cascades.
- Why are $ABCD$ or transmission parameters especially useful for cascaded two-port networks? ::@:: Because with the standard $\begin{bmatrix}V_1\\I_1\end{bmatrix}=T\begin{bmatrix}V_2\\-I_2\end{bmatrix}$ convention, cascaded two-ports are represented by matrix multiplication in cascade order.

## obtaining transfer functions from circuit and differential-equation models

The system function is the main bridge among several continuous-time descriptions:

- circuit diagram $\to$ $s$-domain equivalent model;
- differential equation $\to$ algebraic polynomial ratio;
- interconnected blocks $\to$ algebraic combination rules.

__from circuit diagrams.__

The circuit route is conceptually simple.

1. Choose the excitation variable and response variable.
2. Draw the zero-state $s$-domain equivalent circuit.
3. Solve the resulting algebraic circuit equations.
4. Form $H(s)=\frac{R(s)}{E(s)}$.

The resistor-divider example above is the simplest case.  More interesting dynamic circuits produce rational functions whose poles encode the time constants or oscillation modes.

__from differential equations.__

Suppose the system satisfies a linear constant-coefficient differential equation $\sum_{k=0}^{n} a_k \frac{d^k r(t)}{dt^k}=\sum_{j=0}^{m} b_j \frac{d^j e(t)}{dt^j}$.  Under zero initial conditions, bilateral or unilateral Laplace transform gives $\left(\sum_{k=0}^{n} a_k s^k\right)R(s)=\left(\sum_{j=0}^{m} b_j s^j\right)E(s)$, so $H(s)=\frac{R(s)}{E(s)}=\frac{\sum_{j=0}^{m} b_j s^j}{\sum_{k=0}^{n} a_k s^k}$.

This is why the transfer function of an LTI system is usually a rational function of $s$: derivatives become powers of $s$, and the coefficients of the differential equation become the polynomial coefficients of numerator and denominator.

A useful caution is that __nonzero initial conditions belong to the total response, not to the intrinsic transfer function__.  The transfer function is defined from the zero-state input-output law.  Initial-condition terms should therefore be removed before defining $H(s)$.

A short example shows how reduction matters.  Suppose $\frac{d^2 r}{dt^2}+5\frac{dr}{dt}+6r=\frac{de}{dt}+2e$.  With zero initial conditions, $(s^2+5s+6)R(s)=(s+2)E(s)$, so $H(s)=\frac{R(s)}{E(s)}=\frac{s+2}{(s+2)(s+3)}=\frac{1}{s+3}$.  The cancelled factor $s+2$ is a removable common factor, not a true pole-zero pair of the reduced transfer function.  Therefore the true system function is $H(s)=\frac{1}{s+3}$ and the impulse response is $h(t)=e^{-3t}u(t)$.

This example is important because pole-zero classification must always be done on the __reduced__ form.

---

Flashcards for this section are as follows:

- What are the three Chapter 5.3 description bridges connected by the system function $H(s)$? ::@:: Circuit diagram $\to$ $s$-domain equivalent model, differential equation $\to$ algebraic polynomial ratio, and interconnected blocks $\to$ algebraic combination rules.
- What is the basic workflow for obtaining a transfer function $H(s)=\frac{R(s)}{E(s)}$ from a circuit diagram? ::@:: Choose excitation and response variables → draw the zero-state $s$-domain equivalent circuit → solve the algebraic circuit equations → form $H(s)=\frac{R(s)}{E(s)}$.
- For the general LCCDE $\sum_{k=0}^{n} a_k \frac{d^k r}{dt^k}=\sum_{j=0}^{m} b_j \frac{d^j e}{dt^j}$, what is the zero-state transfer function? ::@:: $H(s)=\frac{R(s)}{E(s)}=\frac{\sum_{j=0}^{m} b_j s^j}{\sum_{k=0}^{n} a_k s^k}$.
- Why is the transfer function of an LTI differential-equation model usually rational in $s$? ::@:: Because Laplace transform converts derivatives into powers of $s$, so the differential equation becomes a polynomial relation between $R(s)$ and $E(s)$.
- Why must nonzero initial conditions be excluded when defining the intrinsic transfer function $H(s)$? ::@:: Because $H(s)$ is defined from the zero-state input-output law of the system itself, while nonzero initial conditions belong to the particular total response for one experiment, not to the intrinsic system description.
- If $\frac{d^2 r}{dt^2}+5\frac{dr}{dt}+6r=\frac{de}{dt}+2e$, what transfer function and impulse response should be obtained under zero initial conditions? ::@:: $(s^2+5s+6)R(s)=(s+2)E(s)$, so $H(s)=\frac{s+2}{(s+2)(s+3)}=\frac{1}{s+3}$ after reduction. <br/> Therefore $h(t)=e^{-3t}u(t)$.
- In the previous example, why is $s=-2$ not treated as a true pole or zero of the reduced $H(s)$? ::@:: Because the factor $s+2$ cancels in the reduced form, so it represents a removable common factor rather than a true pole or zero of the transfer function.

## poles, zeros, and pole-zero plots

For rigorous pole-zero analysis, first write the reduced rational transfer function in factored form $H(s)=K\frac{\prod_i (s-z_i)^{m_i}}{\prod_k (s-p_k)^{n_k}}$.

A __zero__ at $s=z_0$ of multiplicity $m$ means the numerator contains $(s-z_0)^m$ after reduction.  A __pole__ at $s=p_0$ of multiplicity $n$ means the denominator contains $(s-p_0)^n$ after reduction.

The course sketching convention is:

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

This degree-counting viewpoint is useful because it explains why low-pass-like systems often have zeros at infinity while differentiator-like systems can have poles at infinity.

---

Flashcards for this section are as follows:

- For pole-zero analysis, why must $H(s)$ first be written in reduced factored form? ::@:: Because pole and zero classification is defined only after all removable common factors are cancelled; otherwise a cancelled factor would be mistaken for a true pole or zero.
- In the course pole-zero plot convention, how should poles, zeros, and multiplicities be shown on the complex $s$-plane with axes $\Re(s)$ and $j\omega$? ::@:: Use $\times$ for poles and $\circ$ for zeros on the complex $s$-plane, with horizontal axis $\Re(s)$ and vertical axis $j\omega$, and indicate multiplicity by an order label or coincident mark at the same location rather than by moving the point.
- For $H_1(s)=\frac{s+1}{(s+2)^2}$, what are the finite zero, finite pole, multiplicities, and infinity behavior? ::@:: Finite zero: $s=-1$ of multiplicity $1$. <br/> Finite pole: $s=-2$ of multiplicity $2$. <br/> Since the denominator degree exceeds the numerator degree by $1$, there is one zero at infinity.
- For $H_2(s)=\frac{(s+1)^3}{s+2}$, what are the finite zero, finite pole, multiplicities, and infinity behavior? ::@:: Finite zero: $s=-1$ of multiplicity $3$. <br/> Finite pole: $s=-2$ of multiplicity $1$. <br/> Since the numerator degree exceeds the denominator degree by $2$, there are two poles at infinity.
- How does degree counting determine poles or zeros at infinity for a reduced rational $H(s)=\frac{N(s)}{D(s)}$? ::@:: If $\deg D>\deg N$ by $q$, then there are $q$ zeros at infinity. <br/> If $\deg N>\deg D$ by $q$, then there are $q$ poles at infinity. <br/> If the degrees are equal, there is neither.
- When multiplicity and the point at infinity are included for a reduced rational $H(s)=\frac{N(s)}{D(s)}$, how many poles and zeros are there in total? ::@:: Exactly $\max(\deg N,\deg D)$ poles and exactly $\max(\deg N,\deg D)$ zeros.

## interconnection of continuous-time systems

Once a subsystem is represented by $H(s)$, block-diagram algebra becomes simple.  At the signal-flow level, the canonical combinations are parallel, cascade, and feedback.  At the one-port network level, the canonical combinations are series and parallel, handled most cleanly with impedance and admittance.

__series and parallel one-port combinations.__

If two one-port subnetworks are placed in series, the current is common and the voltages add, so $Z_{\text{eq}}(s)=Z_1(s)+Z_2(s)$. If two one-port subnetworks are placed in parallel, the voltage is common and the currents add, so $Y_{\text{eq}}(s)=Y_1(s)+Y_2(s)$.

This is why impedance is the natural series language and admittance is the natural parallel language.

__parallel connection.__

If the same input $E(s)$ drives two subsystems in parallel and the outputs are added, then $R(s)=E(s)H_1(s)+E(s)H_2(s)=E(s)[H_1(s)+H_2(s)]$, so $H(s)=H_1(s)+H_2(s)$.

__cascade connection.__

If the output of the first subsystem drives the second, then $R(s)=E(s)H_1(s)H_2(s)$, so $H(s)=H_1(s)H_2(s)$.

The same idea extends to two-port transmission descriptions. If two two-port networks with transmission matrices $T_1(s)$ and $T_2(s)$ are cascaded under a consistent sign convention, then the equivalent transmission matrix is $T_{\text{eq}}(s)=T_1(s)T_2(s)$.

So scalar cascade multiplies scalar transfer functions, while two-port cascade multiplies transmission matrices.

__negative feedback connection.__

For the standard negative-feedback structure with forward path $H_1(s)$ and feedback path $H_2(s)$, the internal relations are $X_1(s)=E(s)-X_2(s)$, $R(s)=H_1(s)X_1(s)$, and $X_2(s)=H_2(s)R(s)$.  Substituting gives $R(s)=H_1(s)[E(s)-H_2(s)R(s)]$, so $R(s)[1+H_1(s)H_2(s)]=H_1(s)E(s)$, and therefore $H(s)=\frac{R(s)}{E(s)}=\frac{H_1(s)}{1+H_1(s)H_2(s)}$.

If the same loop uses __positive__ feedback instead, only the sign at the summing node changes, and the closed-loop transfer function becomes $H(s)=\frac{H_1(s)}{1-H_1(s)H_2(s)}$.

So the loop gain $H_1(s)H_2(s)$ is the decisive quantity: negative feedback pushes the characteristic denominator toward $1+H_1H_2$, while positive feedback pushes it toward $1-H_1H_2$.

These formulas are high-value tools because they turn complicated block diagrams into one closed-loop transfer function and make stability questions algebraic.

---

Flashcards for this section are as follows:

- What is the equivalent transfer function in parallel form when the same input $E(s)$ drives two subsystems $H_1(s)$ and $H_2(s)$? ::@:: $H(s)=H_1(s)+H_2(s)$.
- What are the equivalent one-port relations $Z_{\text{eq}}(s)$ for series combination and $Y_{\text{eq}}(s)$ for parallel combination? ::@:: For series one-port networks, $Z_{\text{eq}}(s)=Z_1(s)+Z_2(s)$. <br/> For parallel one-port networks, $Y_{\text{eq}}(s)=Y_1(s)+Y_2(s)$.
- What is the equivalent transfer function in cascade form when the output of $H_1(s)$ drives $H_2(s)$? ::@:: $H(s)=H_1(s)H_2(s)$.
- If two two-port networks are cascaded and described by transmission matrices $T_1(s)$ and $T_2(s)$, what is the equivalent transmission matrix? ::@:: $T_{\text{eq}}(s)=T_1(s)T_2(s)$, provided the same transmission-parameter sign convention is used throughout.
- Derive the standard negative-feedback closed-loop transfer function in terms of $X_1(s)$, $X_2(s)$, $H_1(s)$, and $H_2(s)$. ::@:: With $X_1=E-X_2$, $R=H_1X_1$, and $X_2=H_2R$, substitute to get $R=H_1(E-H_2R)$. <br/> Rearranging gives $R[1+H_1H_2]=H_1E$, so $H=\frac{R}{E}=\frac{H_1}{1+H_1H_2}$.
- What changes between the negative-feedback closed-loop formula $\dfrac{H_1}{1+H_1H_2}$ and the positive-feedback version for the same loop? ::@:: Only the sign in the denominator changes: negative feedback gives $\dfrac{H_1}{1+H_1H_2}$, while positive feedback gives $\dfrac{H_1}{1-H_1H_2}$.
- Why is the feedback formula $\frac{H_1(s)}{1\pm H_1(s)H_2(s)}$ so important? ::@:: Because it turns a closed-loop block diagram into one algebraic transfer function whose poles can then be studied directly for stability and response behavior.

## stability of continuous-time systems

A continuous-time system is __BIBO stable__ if every bounded input produces a bounded zero-state output.

The exact time-domain criterion is $\int_{-\infty}^{\infty}|h(t)|\,dt\le M$ for some finite constant $M$.  In words, the impulse response must be absolutely integrable.

In the $s$-domain, the equivalent criterion is that the ROC of $H(s)=\mathcal{L}\{h(t)\}$ includes the imaginary axis.  For __causal rational__ systems, this reduces to the familiar pole test:

- all poles strictly in the left half-plane $\Rightarrow$ stable;
- any pole in the right half-plane $\Rightarrow$ unstable;
- simple poles on the imaginary axis $\Rightarrow$ marginally stable (non-decaying oscillation or constant component);
- repeated poles on the imaginary axis $\Rightarrow$ unstable.

The pole-location intuition is worth memorizing by case.

__single real pole.__

For $H(s)=\frac{1}{s+\alpha}$ with $\alpha>0$, the pole is at $-\alpha$ and $h(t)=e^{-\alpha t}u(t)$, so the response decays and the system is stable.

If the pole moves to the origin, the response becomes a constant and is only marginal.  If the pole moves to the right half-plane, the response grows exponentially and the system is unstable.

__complex-conjugate poles.__

For poles $-\alpha\pm j\omega_0$ with $\alpha>0$, $h(t)=e^{-\alpha t}\sin(\omega_0 t)u(t)$ or a similar damped sinusoid form, so the oscillation decays and the system is stable.

If the poles lie exactly on the imaginary axis $\pm j\omega_0$, the oscillation is sustained rather than decaying, so the system is only marginal.  If they move into the right half-plane, the oscillation grows and the system is unstable.

__repeated poles.__

For a repeated left-half-plane pole, $H(s)=\frac{1}{(s+\alpha)^2} \quad\Longleftrightarrow\quad h(t)=t e^{-\alpha t}u(t)$, which still decays because the exponential term dominates the polynomial factor.  So repeated poles in the strict left half-plane can still be stable.

But repeated poles on the imaginary axis are different.  At the origin, for example, $\frac{1}{s^2}\longleftrightarrow t u(t)$, which grows without bound.  This is why repeated poles on the imaginary axis are classified as unstable rather than marginal.

The course summary is therefore:

- __stable__: all poles strictly in the LHP;
- __unstable__: any RHP pole, or any repeated pole on the imaginary axis;
- __marginally stable__: only simple poles on the imaginary axis and no RHP poles.

A good application example is feedback stabilization.  Suppose the open-loop subsystem is $G(s)=\frac{1}{(s-1)(s+2)}$, which is unstable because it has the right-half-plane pole $s=1$.  Now place it in standard negative feedback with constant gain $k$.  The closed-loop transfer function is $H(s)=\frac{G(s)}{1+kG(s)}=\frac{1}{(s-1)(s+2)+k}=\frac{1}{s^2+s+k-2}$.  The poles are $p_{1,2}=\frac{-1\pm\sqrt{9-4k}}{2}$.  For both poles to lie in the left half-plane, the feedback must satisfy $k>2$.

So negative feedback can move the poles from an unstable open-loop position into a stable closed-loop position.

---

Flashcards for this section are as follows:

- What is the exact time-domain BIBO stability criterion, written in terms of $h(t)$? ::@:: The impulse response must be absolutely integrable: $\int_{-\infty}^{\infty}|h(t)|dt\le M$ for some finite $M$.
- What is the equivalent $s$-domain stability criterion for $H(s)=\mathcal{L}\{h(t)\}$? ::@:: The ROC of $H(s)$ must include the imaginary axis.
- For a causal rational system, what pole-location test in the $s$-plane is equivalent to asymptotic BIBO stability? ::@:: All poles must lie strictly in the left half-plane.
- For poles on the imaginary axis, how do simple poles and repeated poles differ in stability classification? ::@:: Simple poles on the imaginary axis give marginally stable non-decaying behavior, while repeated poles on the imaginary axis give unbounded growth and are therefore unstable.
- For a single real pole at $s=-\alpha$ with $\alpha>0$, what impulse response and stability behavior result? ::@:: $H(s)=\frac{1}{s+\alpha}$ gives $h(t)=e^{-\alpha t}u(t)$, which decays to zero, so the system is stable.
- For complex-conjugate poles $-\alpha\pm j\omega_0$, what time-domain behavior should you expect? ::@:: A damped sinusoid such as $e^{-\alpha t}\sin(\omega_0 t)u(t)$ or $e^{-\alpha t}\cos(\omega_0 t)u(t)$; it is stable when $\alpha>0$, marginal on the imaginary axis, and unstable in the RHP.
- Why can a repeated pole in the left half-plane, such as $H(s)=\frac{1}{(s+\alpha)^2}$, still be stable, but a repeated pole on the imaginary axis, such as $\frac{1}{s^2}$, is unstable? ::@:: In the LHP the exponential decay dominates the polynomial factor, so terms like $t e^{-\alpha t}$ still decay. On the imaginary axis there is no decaying exponential, so terms like $t u(t)$ grow without bound.
- Summarize the stable / unstable / marginally stable classification for causal rational systems. ::@:: Stable: all poles strictly in the LHP. <br/> Unstable: any RHP pole or any repeated pole on the imaginary axis. <br/> Marginally stable: only simple poles on the imaginary axis and no RHP poles.
- If $G(s)=\frac{1}{(s-1)(s+2)}$ is placed in standard negative feedback with constant gain $k$, what is the closed-loop transfer function? ::@:: $H(s)=\frac{G(s)}{1+kG(s)}=\frac{1}{(s-1)(s+2)+k}=\frac{1}{s^2+s+k-2}$.
- For the previous feedback-stabilization example, what are the closed-loop poles and what condition on $k$ makes the system stable? ::@:: The poles are $p_{1,2}=\frac{-1\pm\sqrt{9-4k}}{2}$, and the closed-loop system is stable when $k>2$.
