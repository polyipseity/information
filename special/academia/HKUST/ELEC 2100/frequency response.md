---
aliases:
  - ELEC 2100 frequency response
  - ELEC 2100 frequency-domain system analysis
  - ELEC2100 frequency response
  - HKUST ELEC 2100 frequency response
  - frequency response
  - frequency-domain analysis of LTI systems
  - system frequency response
  - system function
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/frequency_response
  - language/in/English
---

# frequency response

- HKUST ELEC 2100

<!-- check: ignore-file[two_sided_calc_warning]: concept-focused prompts intentionally use descriptive wording rather than repeating every symbol on the left-hand side -->

---

Frequency response describes how an LTI system scales and phase-shifts each sinusoidal component of its input. Instead of repeated time-domain convolution, the output spectrum equals the input spectrum multiplied by the system function $H(\omega)$. Pair this note with [Fourier transform](Fourier%20transform.md) for transform pairs and derivations.

---

Flashcards for this section are as follows:

- What role does frequency response play in system analysis? ::@:: It lets you multiply $X(\omega)$ by $H(\omega)$ instead of convolving $x(t)$ with $h(t)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does frequency-response analysis come after Fourier-transform analysis? ::@:: Once signals are decomposed into frequency components, the next question is how a system scales and phases each component. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## time-domain and frequency-domain zero-state viewpoints

The zero-state response of an LTI system can be written two equivalent ways. Time domain: $y(t)=x(t)*h(t)$. Frequency domain: $Y(\omega)=H(\omega)X(\omega)$. The Fourier transform turns convolution into multiplication.

Convolution is more useful when support, overlap geometry, delays, and transient shape matter. Frequency response is more useful when you want to know which sinusoidal components are amplified, attenuated, or phase shifted. The bridge between the two is $H(\omega)=\mathcal{F}\{h(t)\}$.

If the question is "what does one impulse do in time?", think $h(t)$ and convolution. If the question is "what does the system do to each frequency component?", think $H(\omega)$ and multiplication.

---

Flashcards for this section are as follows:

- How are the time-domain and frequency-domain zero-state viewpoints related? ::@:: Same law, different coordinates: $y(t)=x*h$ versus $Y(\omega)=H(\omega)X(\omega)$. <!--SR:!fsrs,2027-07-31T00:00:00.000Z,369,369.34507636,1,2,7,0,0,2026-07-27T00:00:00.000Z!fsrs,2027-07-20T00:00:00.000Z,360,360.40803568,1,2,7,0,0,2026-07-25T00:00:00.000Z-->
- When is convolution more natural, when is frequency response more natural? ::@:: Convolution for support, overlap, delays, and transients; frequency response for amplification, attenuation, and phase shift of each component. <!--SR:!fsrs,2027-08-07T00:00:00.000Z,374,373.80149873,1,2,7,0,0,2026-07-29T00:00:00.000Z!fsrs,2026-11-15T05:03:02.449Z,163,162.63361781,1,2,5,0,0,2026-06-05T05:03:02.449Z-->
- What bridges convolution and frequency response? ::@:: $H(\omega)=\mathcal{F}\{h(t)\}$. <!--SR:!fsrs,2027-04-29T00:00:00.000Z,291,291.42724554,1,2,7,0,0,2026-07-12T00:00:00.000Z!fsrs,2027-08-12T00:00:00.000Z,378,378.25001087,1,2,7,0,0,2026-07-30T00:00:00.000Z-->

## complex exponentials as LTI eigenfunctions

If $x(t)=e^{j\omega t}$, then $y(t)=(h*x)(t)=\int_{-\infty}^{\infty}h(\tau)e^{j\omega(t-\tau)}\,d\tau=e^{j\omega t}\int_{-\infty}^{\infty}h(\tau)e^{-j\omega\tau}\,d\tau$. The integral depends on $\omega$ but not $t$, so $y(t)=H(\omega)e^{j\omega t}$, where $H(\omega)=\int_{-\infty}^{\infty}h(t)e^{-j\omega t}\,dt$.

Complex exponentials are eigenfunctions of LTI systems: the frequency is preserved, and only a complex scalar $H(\omega)$ is attached. For a general input $X(\omega)$, each spectral component is processed independently, giving $Y(\omega)=H(\omega)X(\omega)$.

---

Flashcards for this section are as follows:

- Why are complex exponentials eigenfunctions of an LTI system? ::@:: Input $e^{j\omega t}$ gives output $H(\omega)e^{j\omega t}$: same waveform, scaled by a complex scalar. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How do you derive the eigenfunction formula? ::@:: Write $y(t)=\int h(\tau)e^{j\omega(t-\tau)}\,d\tau$, factor out $e^{j\omega t}$, and the remaining integral is $H(\omega)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is $H(\omega)$? ::@:: The Fourier transform of $h(t)$: $H(\omega)=\int h(t)e^{-j\omega t}\,dt$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does $Y(\omega)=H(\omega)X(\omega)$ hold for arbitrary inputs? ::@:: Because $X(\omega)$ decomposes the signal into complex exponentials, each multiplied independently by $H(\omega)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why doesn't a frequency response change the frequency of a sinusoidal input? ::@:: Because each complex exponential is an eigenfunction, so the system only multiplies by a scalar instead of changing the oscillation rate. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## magnitude response and phase response

Write $H(\omega)=|H(\omega)|e^{j\phi(\omega)}$. A sinusoidal component $A\cos(\omega t+\theta)$ becomes $A|H(\omega)|\cos(\omega t+\theta+\phi(\omega))$. Magnitude response gives the gain at each frequency; phase response gives the phase shift.

A pure delay $t_0$ has $H(\omega)=e^{-j\omega t_0}$, so its phase is the straight line $-\omega t_0$. Approximately linear phase therefore behaves like an approximate delay. Phase matters because two systems with the same $|H(\omega)|$ can reshape a waveform differently if their phases differ.

Low-pass filters have large $|H(\omega)|$ near $\omega=0$ and small $|H(\omega)|$ for large $|\omega|$. High-pass filters do the reverse. Band-pass filters emphasize a middle range.

---

Flashcards for this section are as follows:

- If $H(\omega)=|H(\omega)|e^{j\phi(\omega)}$, what do magnitude and phase mean? ::@:: $|H(\omega)|$ is the gain at frequency $\omega$; $\phi(\omega)$ is the phase shift. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- If input is $A\cos(\omega t+\theta)$, what is the output? ::@:: $A|H(\omega)|\cos(\omega t+\theta+\phi(\omega))$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does approximately linear phase correspond to an approximate delay? ::@:: A delay $t_0$ has phase $-\omega t_0$, a straight line. Linear phase over a band means that band is delayed by roughly the same amount. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How do you distinguish low-pass, high-pass, and band-pass from $|H(\omega)|$? ::@:: Low-pass: gain near $\omega=0$. High-pass: gain away from $\omega=0$. Band-pass: gain in a middle range. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## ways to determine the system function

Three routes to $H(\omega)$:

1. Transform the impulse response: $H(\omega)=\mathcal{F}\{h(t)\}$.
2. Transform the differential equation ($a_n y^{(n)}+\cdots+a_0 y=b_m x^{(m)}+\cdots+b_0 x$): replace each derivative by $j\omega$ to get $H(\omega)=\frac{b_m(j\omega)^m+\cdots+b_0}{a_n(j\omega)^n+\cdots+a_0}$.
3. Circuit analysis: replace reactive elements by their impedances and solve for the output-to-input ratio.

---

Flashcards for this section are as follows:

- Three routes to $H(\omega)$? ::@:: Fourier transform of $h(t)$, transform the ODE and solve for $Y/X$, or analyze the circuit with impedances. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What system function follows from $a_n y^{(n)}+\cdots+a_0 y=b_m x^{(m)}+\cdots+b_0 x$? ::@:: $H(\omega)=\frac{b_m(j\omega)^m+\cdots+b_0}{a_n(j\omega)^n+\cdots+a_0}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does the ODE route give a polynomial in $j\omega$? ::@:: Each derivative $d^n/dt^n$ becomes $(j\omega)^n$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## first-order RC low-pass filter

The first-order RC low-pass filter has a resistor $R$ in series with a capacitor $C$, with the output taken across the capacitor. KVL gives $x(t)=v_R(t)+y(t)$, where $y(t)=v_C(t)$. Using $v_R=Ri$ and $i=C\,dy/dt$, the system equation is $RC\,dy/dt+y(t)=x(t)$.

At low frequency the capacitor follows the input, so the output tracks the source. At high frequency the rapid oscillation demands large capacitor current, creating a bigger resistor drop and leaving less voltage across $C$. The capacitor smooths fast variation.

In the frequency domain, impedance division gives $H(\omega)=\frac{1/(j\omega C)}{R+1/(j\omega C)}=\frac{1}{1+j\omega RC}$. With $\alpha=1/(RC)$, this becomes $H(\omega)=\frac{\alpha}{\alpha+j\omega}$, with $|H(\omega)|=\frac{1}{\sqrt{1+(\omega RC)^2}}$ and $\phi(\omega)=-\operatorname{atan2}(\omega,\alpha)$.

The phase is $0$ at $\omega=0$ and becomes more negative as frequency increases. Near DC ($|\omega|\ll\alpha$), $\phi(\omega)\approx -\omega RC$, which is approximately a delay of $RC$ seconds. The group delay is $-d\phi/d\omega=RC/(1+(\omega RC)^2)$, close to $RC$ near the origin and smaller at higher frequency.

At $\omega=0$ the gain is $1$ (DC passes unchanged). As $|\omega|\to\infty$ the gain tends to $0$. The $3\text{ dB}$ cutoff is where $|H(\omega_c)|=1/\sqrt{2}$, giving $\omega_c=1/(RC)=\alpha$. Larger $RC$ means slower charging and a narrower passband.

The RC filter has $|H(\omega)|$ that decays smoothly and never reaches zero at any finite frequency. Its phase is continuous and nonzero. The ideal low-pass filter has $H_{\mathrm{LP}}(\omega)=1$ for $|\omega|<\omega_c$ and $0$ outside, with zero phase in the symmetric form. The RC filter is causal and realizable but only gradually selective; the ideal filter has perfect sharpness but requires a two-sided sinc impulse response and is therefore noncausal.

---

Flashcards for this section are as follows:

- What is the RC low-pass filter circuit? ::@:: Resistor $R$ in series with capacitor $C$, output across $C$. KVL gives $RC\,dy/dt+y=x$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How do you derive the RC filter's differential equation from KVL? ::@:: Write $x(t)=v_R(t)+y(t)$, use $v_R=Ri$ and $i=C\,dy/dt$, substitute to get $RC\,dy/dt+y=x$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does the RC circuit behave as a low-pass filter? ::@:: At low frequency the capacitor follows the input; at high frequency the rapid oscillation demands large capacitor current, creating more resistor drop and leaving less voltage across $C$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What frequency response does impedance division give? ::@:: $H(\omega)=\frac{1}{1+j\omega RC}$, with $|H(\omega)|=\frac{1}{\sqrt{1+(\omega RC)^2}}$ and $\phi(\omega)=-\operatorname{atan2}(\omega,1/RC)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is the cutoff frequency? ::@:: $\omega_c=1/(RC)$, where $|H|=1/\sqrt{2}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How does $RC$ affect behavior? ::@:: Larger $RC$: slower time response, narrower passband. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does the RC filter approximate a delay near DC? ::@:: Because $\phi(\omega)\approx -\omega RC$ when $|\omega|\ll 1/(RC)$, which is the phase of a delay of $RC$ seconds. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why is the RC filter only an approximate delay, not exact? ::@:: A pure delay has exactly linear phase $-\omega t_0$ for all frequencies. The RC filter has $\phi(\omega)=-\operatorname{atan2}(\omega,\alpha)$, which is only approximately linear near the origin. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What group delay does the RC filter have? ::@:: $-d\phi/d\omega=RC/(1+(\omega RC)^2)$, close to $RC$ near the origin and smaller at higher frequency. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-10-25T00:10:00.000Z,0,2.3065,2.11810397,1,1,0,1,2026-10-25T00:00:00.000Z-->
- How does the RC filter differ from an ideal low-pass filter? ::@:: RC: causal, realizable, gradual roll-off, continuous phase. Ideal: brick-wall $|H|$, zero phase, noncausal sinc impulse response. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Worked example: $R=2\text{ k}\Omega$, $C=0.5\,\mu\text{F}$. What is $\omega_c$? ::@:: $RC=10^{-3}\text{ s}$, so $\omega_c=10^3\text{ rad/s}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->

## ideal low-pass, high-pass, and band-pass filters

The ideal low-pass filter has $H_{\mathrm{LP}}(\omega)=\operatorname{rect}(\omega/(2\omega_c))$. Using duality on the $\operatorname{rect}\leftrightarrow\operatorname{sinc}_{\pi}$ pair gives $h_{\mathrm{LP}}(t)=\frac{\sin(\omega_c t)}{\pi t}$. The kernel extends over all time, so the filter is noncausal.

The ideal high-pass filter is the complement: $H_{\mathrm{HP}}(\omega)=1-H_{\mathrm{LP}}(\omega)$, giving $h_{\mathrm{HP}}(t)=\delta(t)-\frac{\sin(\omega_c t)}{\pi t}$. The memory rule is "identity minus low-pass".

For an ideal band-pass filter centered at $\omega_0$ with half-bandwidth $\omega_c$: $H_{\mathrm{BP}}(\omega)=\operatorname{rect}((\omega-\omega_0)/(2\omega_c))+\operatorname{rect}((\omega+\omega_0)/(2\omega_c))$, passing $\omega_0-\omega_c<|\omega|<\omega_0+\omega_c$. Frequency-shifting the low-pass kernel gives $h_{\mathrm{BP}}(t)=2\cos(\omega_0 t)\,\frac{\sin(\omega_c t)}{\pi t}=\frac{\sin((\omega_0+\omega_c)t)-\sin((\omega_0-\omega_c)t)}{\pi t}$. The cosine places the passband around $\pm\omega_0$; the sinc envelope sets the channel width.

Summary: low-pass gives sinc, high-pass gives impulse minus sinc, band-pass gives modulated sinc. Ideal filters have perfect frequency selection but noncausal impulse responses. Practical first-order circuits are causal and realizable but only gradually selective.

---

Flashcards for this section are as follows:

- For an ideal low-pass filter with cutoff $\omega_c$, what are $H(\omega)$ and $h(t)$? ::@:: $H_{\mathrm{LP}}(\omega)=\operatorname{rect}(\omega/(2\omega_c))$, $h_{\mathrm{LP}}(t)=\sin(\omega_c t)/(\pi t)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- How do you derive the ideal LP impulse response from the rect-sinc pair? ::@:: Start from $\operatorname{rect}(t/\tau)\longleftrightarrow \tau\operatorname{sinc}_{\pi}(\omega\tau/(2\pi))$. Apply duality, choose $\tau=2\omega_c$, divide by $2\pi$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What is $h(t)$ for an ideal high-pass filter? ::@:: $\delta(t)-\sin(\omega_c t)/(\pi t)$, from the "identity minus low-pass" rule. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does the ideal HP impulse response contain both $\delta(t)$ and a sinc term? ::@:: Because the high-pass equals identity minus low-pass, so its kernel is the impulse minus the low-pass kernel. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What are $H(\omega)$ and $h(t)$ for an ideal band-pass filter centered at $\omega_0$ with half-bandwidth $\omega_c$? ::@:: $H_{\mathrm{BP}}=\operatorname{rect}((\omega-\omega_0)/(2\omega_c))+\operatorname{rect}((\omega+\omega_0)/(2\omega_c))$, passing $\omega_0-\omega_c<|\omega|<\omega_0+\omega_c$. $h_{\mathrm{BP}}(t)=2\cos(\omega_0 t)\sin(\omega_c t)/(\pi t)$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why does the ideal BP impulse response look like cosine times sinc? ::@:: Because an ideal BP filter is a low-pass rectangle shifted away from the origin. Frequency shifting becomes multiplication by $\cos(\omega_0 t)$ in time. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Quick memory rule for ideal filters? ::@:: Low-pass: sinc. High-pass: impulse minus sinc. Band-pass: modulated sinc. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why can't ideal filters be realized? ::@:: Their impulse responses extend over all time (noncausal). <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- What time-frequency tradeoff do ideal filters illustrate? ::@:: Perfect sharpness in frequency requires infinite spread in time. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why is the cutoff the "half-power point"? ::@:: At $\omega_c$, $|H|^2=1/2$, so output power is half the passband value. Amplitude ratio is $1/\sqrt{2}$. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
- Why are ideal filters standards of comparison rather than hardware models? ::@:: They show the frequency-domain limit of perfect selection, while realizable circuits must trade sharpness for causality and finite order. <!--SR:!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z!fsrs,2026-11-02T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-25T00:00:00.000Z-->
