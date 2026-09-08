---
aliases:
  - ELEC 4110 binary modulation
  - ELEC4110 binary modulation
  - binary modulation
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/binary_modulation
  - language/in/English
---

# binary modulation

{@{The simplest analytical model}@}, often called {@{the __binary channel__ or __binary symmetric channel with additive white Gaussian noise__ (__AWGN__)}@}, reduces {@{the whole communication link to a black box}@} that accepts {@{binary input symbols at the transmitter and produces binary output symbols at the receiver}@}. {@{All intermediate physical-layer details}@} – {@{propagation, multipath, fading, etc.}@} – are {@{absorbed into this single stochastic channel model}@}.

{@{The binary channel}@} is the baseline against which {@{coding gains, diversity techniques, or more complex modulation schemes}@} are measured.  In practice, {@{real systems}@} {@{deviate from this idealization}@} due to {@{multipath fading, colored noise, timing errors and non-binary signalling}@}; nevertheless, it remains {@{a standard model in communication theory}@}.

Here, {@{a _bit_ and a _symbol_}@} are {@{used interchangeably}@}. In {@{[_M_-ary transmission](M-ary%20transmission.md)}@}, {@{a _symbol_ can represent more than one _bit_}@} and should be {@{distinguished}@}.

## binary channel

{@{The transmitter}@} sends {@{a sequence of binary symbols $b_k \in \{0,1\}$}@}.  Each symbol occupies {@{a fixed duration $T$}@} and is represented by {@{a pulse waveform}@} {@{$$s(t) = \begin{cases} + A\,p(t), & b_k = 1\\[4pt] - A\,p(t), & b_k = 0 \end{cases}\qquad 0 \le t < T,$$}@} where

- $A>0$ ::@:: is the pulse amplitude, and
- $p(t)$ ::@:: is a _shaping pulse_ of unit energy (e.g., a rectangular or raised-cosine pulse). Here, we assume it is simply a unit rectangular pulse lasting for symbol time $T$.

{@{The transmitted signal}@} is thus {@{$$s_k(t) = \pm A\,p(t), \qquad 0 \le t < T \,.$$}@} {@{The channel}@} adds {@{white Gaussian noise $n(t)$ to the waveform}@}, yielding {@{the received continuous-time signal}@} {@{$$r(t)= s_k(t)+ n(t).   \tag{1}$$}@} Here {@{$n(t)$}@} is {@{a __Gaussian process__ \(_white_ noise\) with zero mean}@} and {@{autocorrelation function}@} {@{$$R_n(t_1, t_2)=E\{n(t_1) n^*(t_2)\}= \frac{N_0}{2}\,\delta(t_1 - t_2),$$}@} where {@{$N_0/2$}@} is {@{the two-sided power spectral density of the noise}@}. \(annotation: If {@{one-sided \(no negative frequencies\)}@}, then {@{the power spectral density is $N_0$}@}. This explains {@{the division by 2}@}.\)

## receiver

{@{The receiver}@} performs {@{a _matched filter_}@} (or equivalently, {@{an integral over one symbol period}@}) to {@{maximise the signal-to-noise ratio}@}: {@{$$V = \int_{0}^{T} r(t)\,dt.$$}@}

Because {@{$s_k(t)=\pm A\,p(t)$}@} and {@{$p(t)$}@} is {@{assumed to be a rectangular pulse of duration $T$}@}, {@{the deterministic part of $V$}@} equals {@{$$E[V|b_k=1]   = +AT,\qquad  E[V|b_k=0]   = -AT.$$}@}

{@{The random part}@} comes from {@{integrating the noise \(of two-sided power spectral density $N_0 / 2$\)}@}: {@{$$N_T=\int_{0}^{T} n(t)\,dt,$$}@} which is {@{a Gaussian random variable}@} with mean {@{$$E[N_T]=\int_{0}^{T} E[n(t)]\,dt = \int_{0}^{T} 0\,dt = 0,$$}@} and variance {@{$$\sigma^2_{n_T}=E[(N_T)^2]-[E(N_T)]^2 = \int_{0}^{T}\!\!\int_{0}^{T} E[n(t)n(s)]\,dt\,ds = \int_{0}^{T}\!\!\int_{0}^{T}\frac{N_0}{2}\,\delta(t-s)\,dt\,ds = \frac{N_0}{2}\,T.$$}@} Thus {@{$E[N_T]=0,\qquad \sigma^2_{n_T}= \frac{N_0}{2}\,T$}@}.

{@{The decision statistic $V$}@} conditioned on {@{the transmitted bit}@} is {@{Gaussian}@}: {@{$$V|b_k=1 \sim \mathcal N(AT,\,\sigma^2_{n_T}),\qquad V|b_k=0 \sim \mathcal N(-AT,\,\sigma^2_{n_T}).$$}@} The receiver makes {@{a hard decision}@} by comparing $V$ with {@{a threshold $V_{\!th}$}@}: {@{$$\hat b_k = \begin{cases} 1,& V>0\\[4pt] 0,& V\le0 \end{cases}.$$}@} If {@{the threshold is zero}@}, because {@{the two symbols are mirror images about zero}@}, {@{a noise sample that flips the sign of $V$}@} causes {@{an error}@}. The threshold can also {@{be nonzero}@}.

## bit error rate

In {@{digital communications}@} {@{the _bit error rate_ (BER)}@} is {@{a standard metric}@} for quantifying {@{how reliably a transmitter–receiver pair can convey data over a noisy medium}@}.

Let {@{the prior probabilities}@} be {@{$$P(b_k=0)=p_0,\qquad P(b_k=1)=p_1,$$}@} with {@{$p_0+p_1=1$}@}. {@{The a-priori bit error probabilities}@} become {@{$$P_e^{(0)} = P(\hat b_k \neq 0 | b_k=0),\qquad P_e^{(1)} = P(\hat b_k \neq 1 | b_k=1).$$}@} {@{The overall BER}@} is {@{the weighted sum}@} {@{$$P_e = p_0\,P_e^{(0)} + p_1\,P_e^{(1)} \,.$$}@} We split {@{the analysis into two conditioned cases}@} to avoid {@{mixed-distribution integrals that are analytically intractable}@}.

### bit error rate with zero threshold

With {@{the hard decision rule}@} {@{$$\displaystyle \hat b_k=\begin{cases}1,& V>0\\[4pt]0,&V\le0\end{cases} \,,$$}@} {@{an error occurs}@} when $V$ has {@{opposite sign to the transmitted symbol}@}.

For {@{a transmitted '1'}@}: {@{$$P_e^{(1)} = P(N_T < -AT) = Q\!\left(\frac{AT}{\sigma_{n_T} }\right) = Q\!\left(\sqrt{\frac{2E_b}{N_0} }\right) \,,$$}@} where {@{$\sigma_{n_T}=\sqrt{\tfrac{N_0}{2}\,T}$}@} and {@{$E_b = A^2 T$}@} is {@{the signal energy per bit}@}.

For {@{a transmitted '0'}@}: {@{$$P_e^{(0)} = P(N_T > AT) = Q\!\left(\frac{AT}{\sigma_{n_T} }\right) = Q\!\left(\sqrt{\frac{2E_b}{N_0} }\right) \,,$$}@} the same expression.

Hence {@{the BER with arbitrary priors}@} is {@{$$\boxed{P_e = p_0\,Q\!\left(\sqrt{\tfrac{2E_b}{N_0} }\right)+p_1\,Q\!\left(\sqrt{\tfrac{2E_b}{N_0} }\right) = Q\!\left(\sqrt{\tfrac{2E_b}{N_0} }\right)} \,.$$}@} {@{The input bit probabilities}@} do not {@{affect the BER}@}.

### bit error rate with arbitrary threshold

If the receiver compares {@{$V$ to an arbitrary threshold $V_{\!th}\neq0$}@}, {@{the decision rule}@} becomes   {@{$$\displaystyle \hat b_k=\begin{cases}1,& V>V_{\!th}\\[4pt]0,&V\le V_{\!th}\end{cases} \,.$$}@}

For {@{a transmitted '1'}@} {@{the error event}@} is {@{$\{AT+N_T=V\le V_{\!th}\}$}@}, giving {@{$$P_e^{(1)} = Q\!\left(\frac{AT-V_{\!th} }{\sigma_{n_T} }\right).$$}@}

For {@{a transmitted '0'}@} {@{the error event}@} is {@{$\{-AT+N_T=V>V_{\!th}\}$}@}, giving
$$P_e^{(0)} = Q\!\left(\frac{AT+V_{\!th} }{\sigma_{n_T} }\right).$$

{@{The overall BER with priors $p_0,p_1$}@} is therefore {@{$$\boxed{P_e(V_{\!th})= p_0\,Q\!\left(\frac{AT+V_{\!th} }{\sigma_{n_T} }\right) +p_1\,Q\!\left(\frac{AT-V_{\!th} }{\sigma_{n_T} }\right)} \,.$$}@} {@{Setting $V_{\!th}=0$}@} recovers {@{the zero-threshold result above}@}.

### bit error rate insight

{@{The variance term $\sigma^2_{n_T}$}@} governs how much {@{the decision statistic $V$ can deviate from its mean value $\pm AT$}@} before {@{causing a bit error}@}. In {@{a binary antipodal system}@}, {@{the error probability}@} decays {@{exponentially with $\frac{E_b}{N_0}$}@}, because {@{the noise variance}@} scales {@{linearly with $T$}@} and {@{longer symbols}@} provide {@{more averaging}@}.

Mathematically, for {@{a fixed $E_b$}@}: {@{$$P_e = Q\!\left(\sqrt{\frac{2E_b}{N_0} }\right) \;\approx\; \sqrt{\frac {N_0} {2E_b} } \frac{1}{\sqrt{2 \pi } }\exp\!\left(-\frac{E_b}{N_0}\right)\quad (E_b/N_0 \gg 1) \,,$$}@} using {@{$Q(x) \approx \frac {\phi(x)} x = \frac 1 {x \sqrt{2\pi} } e^{-x^2 / 2} \qquad x > 0 \,.$$}@}

## signal energy

{@{The _signal energy_ \(excluding noise energy\) transmitted during one symbol}@} is {@{$$E_s = \int_{0}^{T} s_k^2(t)\,dt = A^2 \!\int_{0}^{T} p^2(t)\,dt = A^2 T \,,$$}@} since {@{$p(t)$}@} has {@{unit energy}@}.

With {@{non-equiprobable bits}@}, {@{the average energy per bit}@} is {@{$$E_b = p_0\,E_s^{(0)} + p_1\,E_s^{(1)} = (p_0+p_1) A^2 T = A^2 T,$$}@} because {@{both symbols}@} have {@{the same magnitude $A$ and duration $T$}@}. Thus {@{$$E_b = A^2 T.$$}@} If {@{the two antipodal signals}@} had {@{different amplitudes}@}, the expression would {@{involve $p_0$ and $p_1$ explicitly}@}.

## signal-to-noise ratio

{@{The _signal-to-noise ratio_ (SNR) _per bit_}@} is defined as {@{$$\boxed{\text{bSNR}_{\text{lin} } := \frac{E_b}{N_0} } \,.$$}@} {@{The noise PSD}@} uses {@{one-sided power $N_0$}@} rather than {@{two-sided power $N_0 / 2$}@}. Thus, {@{the BER for _zero threshold_}@} is {@{$$\boxed{\text{BER}=Q\!\left(\sqrt{\dfrac{2E_b}{N_0} }\right) = Q\!\left(\sqrt{2 \cdot \text{bSNR}_{\text{lin} } } \right) \qquad V_{\!th} = 0} \,.$$}@}

## using Q-function

{@{The _Q-function_}@} is {@{the tail probability of a standard normal random variable}@}: {@{$$Q(x)\;=\;\Pr\{Z > x\}\quad \text{with } Z\sim\mathcal N(0,1) \;=\;\frac{1}{\sqrt{2\pi} }\int_{x}^{\infty} e^{-t^{2}/2}\,\mathrm dt \,.$$}@} Most textbooks provide {@{a Q-table up to $x \approx 3$}@}; beyond that {@{entries become negligible}@}.

For {@{large positive arguments}@}: {@{$$Q(x)\approx \frac {\phi(x)} x = \frac{1}{\sqrt{2\pi}\,x}e^{-x^{2}/2} \,,$$}@} which is {@{asymptotically exact as $x\to\infty$}@}.

## using error function

{@{The Q-function}@} can be written in terms of {@{the _complementary_ error function $\operatorname{erfc}$}@}: {@{$$Q(x)=\frac12\,\operatorname{erfc}\!\left(\frac{x}{\sqrt{2} }\right) =\frac12-\frac12\,\operatorname{erf}\!\left(\frac{x}{\sqrt{2} }\right),$$}@} where {@{the ordinary error function}@} is {@{$$\operatorname{erf}(z)= \frac{2}{\sqrt{\pi} }\int_{0}^{z} e^{-t^2}\,dt.$$}@}

These identities are useful when {@{numerical tables or software libraries}@} provide {@{$\operatorname{erfc}$ rather than $Q$}@}. For example, {@{the BER using zero threshold}@}: {@{$$\boxed{\text{BER}= \frac12\,\operatorname{erfc}\!\left(\sqrt{\dfrac{E_b}{N_0} }\right)} \,,$$}@} and {@{the BER using arbitrary threshold}@}: {@{$$\boxed{\text{BER}(V_{\!th})= p_{0}\,\tfrac12\,\operatorname{erfc}\!\left(\dfrac{AT+V_{\!th} } {\sqrt{2\,\sigma^2_{n_T} } }\right) +p_{1}\,\tfrac12\,\operatorname{erfc}\!\left(\dfrac{AT-V_{\!th} } {\sqrt{2\,\sigma^2_{n_T} } }\right)} \,.$$}@}

## optimization

For {@{a given modulation and noise model}@}, BER depends on {@{the receiver front–end filter $h(t)$ and on the decision threshold $\gamma$}@}. {@{Minimizing $P_{\text{e} }$}@} {@{proceeds in two stages}@}: {@{_fixed-filter optimization_}@} – for {@{a predetermined impulse response $h(t)$}@}, determine {@{the threshold $\gamma$ that gives the smallest BER}@}; and {@{_filter design optimization_}@} – search over {@{all admissible filters $h(t)$ \(an infinite–dimensional space\)}@} to find {@{the receiver that achieves the lowest possible BER}@}. Here we only consider {@{receivers modeled by a LTI system}@}; {@{non-linear receivers}@} can achieve {@{even lower BER}@}.

Assuming {@{both bits are equiprobable}@} and {@{the optimal threshold is chosen \(middle\)}@}, we also seek to {@{minimize the energy of each bit}@} while {@{maintaining the error rate}@}.

### bit error rate optimization

As above, {@{the overall BER with priors $p_0,p_1$}@} is {@{$$\boxed{P_e(V_{\!th})= p_0\,Q\!\left(\frac{V_{\!th} - s_{o0} }{\sigma_{n_T} }\right) +p_1\,Q\!\left(\frac{s_{o1} -V_{\!th} }{\sigma_{n_T} }\right)} \,,$$}@} where {@{$s_{o0}, s_{o1}$}@} are {@{the convolution of $h(t)$ with $s_0(t), s_1(t)$ after time $T$}@}. For {@{a unit pulse signal and an integrator}@}, {@{$s_{o0} = -AT, s_{o1} = AT$}@}. To {@{minimize}@}, {@{differentiate with respect to $V_{th}$ and set to zero}@}: {@{$$\begin{aligned} 0 & = \frac 1 {\sigma_{n_T} } \left(-p_0 \phi\!\left(\frac{V_{\!th} - s_{o0} }{\sigma_{n_T} }\right) + p_1 \phi\!\left(\frac{s_{o1} -V_{\!th} }{\sigma_{n_T} }\right) \right) \\ \frac {p_0} {p_1} & = \frac {\phi\!\left(\frac{s_{o1} - V_{\!th} }{\sigma_{n_T} }\right)} {\phi\!\left(\frac{V_{\!th} - s_{o0} }{\sigma_{n_T} }\right)} \\ & = \exp\left(\frac 1 {2 \sigma_{n_T}^2 } \left((V_{th} - s_{o0})^2 - (s_{o1} - V_{th})^2 \right)\right) \\ \ln \frac {p_0} {p_1} & = \frac 1 {2 \sigma_{n_T}^2 } (s_{o1} - s_{o0})(2V_{th} - (s_{o0} + s_{o1})) \\ V_{th} & = \frac {\sigma_{n_T}^2} {s_{o1} - s_{o0} } \ln \frac {p_0} {p_1} + \frac {s_{o0} + s_{o1} } 2 \,. \end{aligned}$$}@} So {@{the optimal threshold is}@}: {@{$$\boxed{V_{th} = \frac {\sigma_{n_T}^2} {s_{o1} - s_{o0} } \ln \frac {p_0} {p_1} + \frac {s_{o0} + s_{o1} } 2 } \,.$$}@} When {@{both bits are equiprobable}@}, {@{the first term vanishes}@} and {@{$V_{th} = \frac {s_{o0} + s_{o1} } 2$}@} is {@{halfway between $s_{o0}$ and $s_{o1}$}@}, giving {@{$$\boxed{P_e(V_{\!th})= Q\!\left(\frac{s_{o1} - s_{o0} }{2\sigma_{n_T} }\right) = Q\!\left(\sqrt{\frac{(s_{o1} - s_{o0})^2 }{4\sigma_{n_T}^2 } }\right)} \,.$$}@}

### filter optimization

Next, we find {@{the optimal filter $h(t)$}@}. Assume {@{both bits are _equiprobable_}@}. From {@{the BER formula for equiprobable bits}@}, we see {@{maximizing $\left\lvert \frac {s_{o0} - s_{o1} } {\sigma_{n_T} } \right\rvert$}@} or equivalently {@{$\rho := \frac {(s_{o0} - s_{o 1})^2} {\sigma_{n_T}^2}$}@} minimizes {@{$P_e$}@}.

First, we generalize {@{$\sigma_{n_T}^2$ to arbitrary filter $h(t)$ and _WSS process_ \(not necessarily _white noise_!\) with power spectrum $S_{xx}(f)$}@}: {@{$$\begin{aligned} \sigma_{n_T}^2 & = \operatorname E\left[\left(\int_{-\infty}^\infty \! h(T - \tau) n(\tau) \,\mathrm d\tau\right)^2 \right] - \operatorname E\left[\int_{-\infty}^\infty \! h(T - \tau) n(\tau) \,\mathrm d\tau \right] \\ & = \operatorname{E} \left[\int_{\mathbb R^2} \! h(T - \tau_1) h(T - \tau_2) n(\tau_1) n(\tau_2) \,\mathrm d(\tau_1, \tau_2) \right] \\ & = \int_{\mathbb R^2} \! h(T - \tau_1) h(T - \tau_2) \operatorname E[n(\tau_1) n(\tau_2)] \,\mathrm d(\tau_1, \tau_2) \\ & = \int_{\mathbb R^2} \! h(T - \tau_1) h(T - \tau_2) r_{xx}(\tau_1 - \tau_2) \,\mathrm d(\tau_1, \tau_2) \,, \end{aligned}$$}@} which we simplify using {@{the Fourier transform}@} and that {@{the Fourier transform of the \(WSS\) autocorrelation function $r_{xx}(t)$}@} is {@{the power spectral density $S_{xx}(f)$}@}: {@{$$\begin{aligned} \sigma_{n_T}^2 & = \int_{\mathbb R^2} \! h(T - \tau_1) h(T - \tau_2) r_{xx}(\tau_1 - \tau_2) \,\mathrm d(\tau_1, \tau_2) \\ & = \int_{\mathbb R} h(\tau_1) \int_{\mathbb R} h(\tau_1 - \tau_2) r_{xx}(\tau_2) \,\mathrm d\tau_2 \,\mathrm d\tau_1 \\ & = \int_{\mathbb R} h(\tau_1) \int_{\mathbb R} H(f) S_{xx}(f) e^{j 2\pi f \tau_1} \,\mathrm df \,\mathrm d\tau_1 \\ & = \int_{\mathbb R} H(f) S_{xx}(f) \int_{\mathbb R} h(\tau_1) e^{j 2\pi f \tau_1} \,\mathrm d\tau_1 \,\mathrm df \\ & = \int_{\mathbb R} H(f) S_{xx}(f) \overline{H(f)} \,\mathrm df \\ & = \int_{\mathbb R} \lvert H(f) \rvert^2 S_{xx}(f) \,\mathrm df \,. \end{aligned}$$}@} We assumed {@{$h(t)$ is real \(thus $\overline{h(t)} = h(t)$\)}@}. Thus {@{$$\boxed{\sigma_{n_T}^2 = \int_{-\infty}^\infty \lvert H(f) \rvert^2 S_{xx}(f) \,\mathrm df} \,.$$}@}

Now, also {@{generalizing the numerator}@} to {@{arbitrary $h(t)$}@}: {@{$$\begin{aligned} \rho = \frac {(s_{o0} - s_{o1})^2} {\sigma_{n_T}^2} & = \frac {\left(\int_{-\infty}^\infty h(T - \tau) s_1(\tau) \,\mathrm d\tau - \int_{-\infty}^\infty h(T - \tau) s_0(\tau) \,\mathrm d\tau \right)^2} {\sigma_{n_T}^2} \\ & = \frac {\left(\int_{-\infty}^\infty h(T - \tau) (s_1(\tau) - s_0(\tau)) \,\mathrm d\tau \right)^2} {\sigma_{n_T}^2} \,. \end{aligned}$$}@} Defining {@{$g(t) := s_1(t) - s_0(t)$}@}, we want to minimize {@{$$\frac {((h * g)(T))^2} {\sigma_{n_T}^2} \,.$$}@} Applying {@{the Fourier transform}@}: {@{$$\frac {((h * g)(T))^2} {\int_{\mathbb R} \lvert H(f) \rvert^2 S_{xx}(f) \,\mathrm df} = \frac {(\int_{\mathbb R} H(f)G(f) e^{j2\pi f T} \,\mathrm df)^2 } {\int_{\mathbb R} \lvert H(f) \rvert^2 S_{xx}(f) \,\mathrm df } \,.$$}@} Applying {@{the Cauchy–Schwarz inequality $(\mathbf x \cdot \mathbf y)^2 \le \lVert \mathbf x \rVert_2^2 \lVert \mathbf y \rVert_2^2$}@} \(treating {@{functions as infinite-dimensional vectors}@}\) gives {@{an upper bound for $\rho$}@}: {@{$$\begin{aligned} \rho = \frac {(s_{o0} - s_{o1})^2} {\sigma_{n_T}^2} & = \frac {\left(\int_{\mathbb R} H(f)G(f) e^{j2\pi f T} \,\mathrm df\right)^2 } {\int_{\mathbb R} \lvert H(f) \rvert^2 S_{xx}(f) \,\mathrm df } \\ & = \frac {\left(\int_{\mathbb R} \left ({H(f)} \sqrt{S_{xx}(f)} \right) \left( G(f) e^{j2\pi f T} / \sqrt{S_{xx}(f)} \right) \,\mathrm df\right)^2 } {\int_{\mathbb R} \lvert H(f) \rvert^2 S_{xx}(f) \,\mathrm df } \\ & \le \frac {\left(\int_{\mathbb R} \lvert H(f) \rvert^2 S_{xx}(f) \,\mathrm df \right) \left(\int_{\mathbb R} \lvert G(f)\rvert^2 / S_{xx}(f) \,\mathrm df \right) } {\int_{\mathbb R} \lvert H(f) \rvert^2 S_{xx}(f) \,\mathrm df } \\ & = \int_{\mathbb R} \frac {\lvert G(f) \rvert^2} {S_{xx}(f)} \,\mathrm df \,. \end{aligned}$$}@}

Thus {@{$$\boxed{\rho \le \int_{\mathbb R} \frac {\lvert G(f) \rvert^2} {S_{xx}(f)} \,\mathrm df } \,.$$}@} The bound is {@{the _maximum signal-to-noise ratio_ \(SNR\)}@}. Equality is achieved {@{if and only if $$H_{\text{opt} }(f) \sqrt{S_{xx}(f)} = C \overline{\frac {G(f) e^{j 2\pi fT} } { \sqrt{S_{xx}(f)} } } \implies \boxed{H_{\text{opt} }(f) = C \frac {\overline {G(f) e^{j 2\pi f T} } } {S_{xx}(f)} = C \frac {G^*(f) e^{-j 2\pi f T} } {S_{xx}(f)} }$$}@} for {@{some arbitrary complex number $C$}@}. The optimal filter weights {@{each frequency component proportionally with the signal difference}@} and {@{inversely with the noise PSD}@}. We assumed only that {@{the noise is a WSS process that _may or may not_ be white noise}@} and that it is {@{_Gaussian_ (needed for the Q-function)}@}.

In the _special case_ that {@{the noise is white noise}@}, {@{$S_{xx}(f) = N_0 / 2$ is a _constant_}@}, so {@{the optimal filter}@} has the Fourier transform {@{$$H_{\text{opt} }(f) = C G^*(f) e^{-j 2\pi f T}$$}@} for {@{some arbitrary complex number $C$}@} which {@{absorbs the constant denominator}@}. In the time domain, {@{the optimal filter}@} is {@{a _matched filter_}@}: {@{$$\boxed{h_{\text{opt} }(t) = \overline {g(-(t - T))} = g^*(T - t)} \,.$$}@} This flips {@{$g(t)$ across $t = 0$}@}, shifts {@{it to the right by $T$}@}, and takes {@{its conjugate}@}. Further, as {@{$\rho = \frac {(s_{o0} - s_{o1})^2} {\sigma_{n_T}^2} = \int_{\mathbb R} \frac {\lvert G(f) \rvert^2} {S_{xx}(f)} \,\mathrm df$}@} and noise has {@{constant (two-sided) PSD $S_{xx}(f) = N_0 / 2$}@}, so {@{$$\boxed{\rho = \frac {(s_{o0} - s_{o1})^2} {\sigma_{n_T}^2} = \frac {2E_g} {N_0} } \,.$$}@}

#### response of LTI system to WSS random signal

Given {@{a zero-mean WSS random signal with power spectrum $S_{xx}(f)$ \(not necessary Gaussian\)}@}, {@{the response of a LTI system with impulse response $h(t)$}@} is also {@{a zero-mean WSS random signal}@}.

We derived above that {@{$$\begin{aligned} \sigma_{n_T}^2 & = \int_{\mathbb R} h(\tau_1) \int_{\mathbb R} h(\tau_1 - \tau_2) r_{xx}(\tau_2) \,\mathrm d\tau_2 \,\mathrm d\tau_1 \,, \end{aligned}$$}@} which can be {@{derived more simply via Fourier transform}@} by noting {@{two convolutions}@}: {@{$$\begin{aligned} \sigma_{n_T}^2 & = \int_{\mathbb R} h(\tau_1) \int_{\mathbb R} h(\tau_1 - \tau_2) r_{xx}(\tau_2) \,\mathrm d\tau_2 \,\mathrm d\tau_1 \\ & = \int_{\mathbb R} h(\tau_1) (h * r_{xx})(\tau_1) \,\mathrm d\tau_1 \\ & = ((h(-t)) * (h * r_{xx}))(0) \\ & = \int_{-\infty}^\infty H^*(f) H(f) S_{xx}(f) e^{j 2 \pi f 0} \,\mathrm df \\ & = \int_{-\infty}^\infty \lvert H(f) \rvert^2 S_{xx}(f) \,\mathrm df \,. \end{aligned}$$}@} We assumed {@{$h(t)$ is real \(thus $\overline{h(t)} = h(t)$\)}@}. Thus {@{$$\boxed{\sigma_{n_T}^2 = \int_{-\infty}^\infty \lvert H(f) \rvert^2 S_{xx}(f) \,\mathrm df} \,.$$}@}

We also prove that {@{the LTI response mean}@} is zero when {@{the WSS random signal has zero mean}@}: since {@{a WSS has constant mean $m$}@}, {@{the response mean is $m H(0)$}@}, which vanishes when {@{$m = 0$}@}.

### matched filter

For {@{equiprobable bits and white noise}@}, given {@{the input difference $g(t)$}@}, {@{the optimal filter}@} is {@{$$\boxed{h_{\text{opt} }(t) = \overline {g(-(t - T))} = g^*(T - t)} \,.$$}@} It is interpreted as {@{flipping $g(t)$ across $t = 0$}@}, shifting {@{it right by $T$}@}, and taking {@{its conjugate}@}. This is {@{a _matched filter_}@}.

When {@{$s_0(t), s_1(t)$ are readily available}@} but {@{$g(t) = s_1(t) - s_0(t)$ is not}@}, use {@{linearity of convolution}@}: create {@{a matched filter for each}@}: {@{$$h_0(t) := s_0^*(T - t) \qquad h_1(t) := s_1^*(T - t) \,,$$}@} then {@{subtract the outputs}@}. Mathematically {@{equivalent to the single-filter form}@}.

#### correlator

{@{Implementing a matched filter}@} requires {@{flipping, shifting, and conjugating}@}, which can be avoided by noting {@{the convolution at time $T$ simplifies}@}: {@{$$\begin{aligned} (h * y)(T) & = \int_{\mathbb R} s^*(T - (T - t)) y(t) \,\mathrm dt \\ & = \int_{\mathbb R} s^*(t) y(t) \,\mathrm dt \\ & = \int_0^T s^*(t) y(t) \,\mathrm dt \,, \end{aligned}$$}@} where {@{the last equality uses the support of $s^*(t)$ being $[0, T]$}@}. This is {@{the cross-correlation of $y$ and $s$ at $t = 0$}@}. {@{A _correlator receiver_}@} passes through {@{$\otimes$ \(with additional input $s(t)$\) and then an integrator over $[0, T]$}@}: {@{$$(y \star s)(0) = \int_{-\infty}^\infty y(t) s^*(t) \,\mathrm dt = \int_0^T y(t) s^*(t) \,\mathrm dt \,.$$}@} Again, we can use {@{two correlators instead of one}@}.

### energy optimization

Assuming {@{white Gaussian noise and optimal (midpoint) threshold}@}, {@{the overall BER with priors $p_0 = p_1 = 0.5$}@} is {@{$$\boxed{P_e(V_{\!th})= Q\!\left(\frac{s_{o1} - s_{o0} }{2\sigma_{n_T} }\right) = Q\!\left(\sqrt{\frac{(s_{o1} - s_{o0})^2 }{4\sigma_{n_T}^2 } }\right)} \,.$$}@} Defining {@{the _energy per bit_ of the signal difference $g(t) = s_1(t) - s_0(t)$}@}: {@{$$\begin{aligned} E_g & := \int_0^T (s_1(t) - s_0(t))^2 \,\mathrm dt \\ & = \int_0^T (s_1(t))^2 \,\mathrm dt + \int_0^T (s_0(t))^2 \,\mathrm dt - 2 \int_0^T s_0(t) s_1(t) \,\mathrm dt \\ & = E_0 + E_1 - 2 \sqrt{E_0 E_1} \rho_{01} \,, \end{aligned}$$}@} where {@{$\rho_{01} := \frac 1 {\sqrt{E_0 E_1} } \int_0^T s_0(t) s_1(t) \,\mathrm dt$}@} is {@{the _normalized_ cross-correlation of $s_0(t)$ and $s_1(t)$}@} \("normalized" means {@{must be between −1 and 1, inclusive}@}\). Thus: {@{$$\boxed{E_g = E_0 + E_1 - 2 \sqrt{E_0 E_1} \rho_{01} } \,.$$}@}

With {@{white Gaussian noise}@}, {@{$\rho = \frac {(s_{o0} - s_{o1})^2} {\sigma_{n_T}^2} = \frac {2E_g} {N_0}$ applies}@}, so: {@{$$\boxed{P_e(V_{\!th})= Q\!\left(\sqrt{\frac{(s_{o1} - s_{o0})^2 }{4\sigma_{n_T}^2 } }\right) = Q\!\left(\sqrt {\frac {E_g} {2 N_0} } \right)} \,.$$}@} Later in {@{[signal space](signal%20space.md)}@}, we will see {@{$E_g$}@} is {@{the squared distance of the two signals in signal space}@}.

Continue to assume {@{white Gaussian noise}@}. In practice, {@{the actual bit energy is $E_0$ or $E_1$}@}, not {@{$E_g$}@}. The objective is to {@{minimize average bit energy $E_b$ while maximizing $E_g$}@}. With {@{equal bit energies $E_0 = E_1 = E_b$}@}, maximizing {@{$E_g$}@} requires {@{$\rho = -1$}@}, achieved by {@{setting $s_0(t) = -s_1(t)$}@}, yielding {@{$$\boxed{E_g = 4E_b \implies P_e(V_{th}) = Q\left(\sqrt {\frac {2 E_b} {N_0} } \right)} \,,$$}@} where the last equality {@{assumes AWGN of two-sided PSD $N_0 / 2$}@}. This matches the earlier BER expression for {@{binary _antipodal_ signaling over AWGN}@}. Common schemes: {@{_antipodal signaling_ and _PSK_}@}.

Assuming {@{_white_ Gaussian noise}@}, an alternative is {@{zero bit energy $E_0 = 0$}@}: the zero bit costs no energy, so {@{_average energy bit_ is $E_b = E_1 / 2$}@}, and {@{$$\boxed{E_g = 2E_b \implies P_e(V_{th}) = Q\left(\sqrt {\frac {E_b} {N_0} } \right)} \,,$$}@} where the last equality {@{assumes AWGN of two-sided PSD $N_0 / 2$}@}. Common schemes: {@{_NRZ_ and _ASK_}@}. The same equation holds for {@{equal bit energies with orthogonal signals $\rho = 0$}@}, e.g. {@{_FSK_}@}.

## modulation schemes

{@{_Signal modulation_}@} varies {@{a carrier waveform's amplitude, phase, or frequency}@} to {@{embed information for transmission}@}. The transmitted signal {@{$s(t)$ carries data through its modulated parameters}@} while {@{the receiver demodulates them to recover the bit pattern}@}.

### bipolar non-return-to-zero

In {@{bipolar NRZ \(__this course__: "_antipodal signaling_"\)}@}, binary digits are {@{two opposite voltage levels}@}, typically {@{$+A$ and $-A$}@}, held for {@{each bit interval $T$}@}: {@{$$s_0(t)= -A,\qquad s_1(t)=+A \qquad (t\in[0,T]) \,.$$}@}

### unipolar non-return-to-zero

{@{Unipolar NRZ \(__this course__: "_non-return to zero_"\)}@} represents {@{"1" as $+A$ and "0" as 0&nbsp;V}@}: {@{$$s_0(t)=0,\qquad s_1(t)=A\qquad (t\in[0,T]) \,.$$}@}

### amplitude-shift keying

{@{ASK}@} alters {@{the carrier's amplitude}@} while keeping {@{frequency and phase fixed}@}: {@{$$s_0(t)=0,\qquad s_1(t)=A\cos(\omega t+\theta) \qquad (t \in [0, T]) \,,$$}@} with {@{$\omega T$ an integer multiple of $2\pi$}@} for {@{smooth phase transitions}@}.

### phase-shift keying

{@{PSK}@} modulates {@{the carrier's phase while keeping amplitude and frequency constant}@}. {@{BPSK}@} uses {@{two phases $180^\circ$ apart}@}: {@{$$s_0(t)= +A\cos(\omega t+\theta), \qquad s_1(t)= -A\cos(\omega t+\theta) \qquad (t \in [0, T]) \,,$$}@} with {@{$\omega T$ an integer multiple of $2\pi$}@} for {@{smooth transitions and signal orthogonality}@}.

### frequency-shift keying

In {@{FSK}@}, data is encoded by switching {@{between discrete carrier frequencies}@}: {@{$$s_0(t)=A\cos(\omega_1 t+\theta), \qquad s_1(t)=A\cos(\omega_2 t+\theta) \qquad (t \in [0, T]) \,,$$}@} with {@{$\omega_1 \ne \omega_2$ and both $\omega_1 T$, $\omega_2 T$ integer multiples of $2\pi$}@} for {@{smooth phase transitions}@}.
