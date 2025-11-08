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

{@{The simplest analytical model}@}, often called the {@{__binary channel__ or __binary symmetric channel with additive white Gaussian noise__ (__AWGN__)}@}, reduces {@{the whole communication link to a black box}@} that accepts {@{binary input symbols at the transmitter and produces binary output symbols at the receiver}@}. {@{All intermediate physical‑layer details}@} – {@{propagation, multipath, fading, etc.}@} – are {@{absorbed into this single stochastic channel model}@}. <!--SR:!2026-01-17,66,310!2026-01-04,55,310!2026-01-03,54,310!2025-12-21,43,290!2026-01-18,67,310!2026-01-14,63,310!2026-01-13,63,310-->

{@{This simple binary channel model}@} underpins {@{many higher‑level analyses in digital communications}@}: it provides the baseline against which {@{coding gains, diversity techniques, or more complex modulation schemes}@} are measured.  In practice, {@{real systems}@} often {@{deviate from this idealization}@} due to {@{multipath fading, colored noise, timing errors and non‑binary signalling}@}; nevertheless, it remains {@{a cornerstone of communication theory}@}. <!--SR:!2026-01-11,61,310!2026-01-17,66,310!2026-01-14,63,310!2026-01-11,61,310!2026-01-12,62,310!2026-01-13,63,310!2026-01-11,61,310-->

## binary channel

{@{The transmitter}@} sends {@{a sequence of binary symbols $b_k \in \{0,1\}$}@}.  Each symbol occupies {@{a fixed duration $T$}@} and is represented by {@{a pulse waveform}@} {@{$$s(t) = \begin{cases} + A\,p(t), & b_k = 1\\[4pt] - A\,p(t), & b_k = 0 \end{cases}\qquad 0 \le t < T,$$}@} where <!--SR:!2026-01-04,55,310!2026-01-07,58,310!2025-12-21,43,290!2026-01-15,64,310!2026-01-13,63,310-->

- $A>0$ ::@:: is the pulse amplitude, and <!--SR:!2026-01-15,64,310!2026-01-18,67,310-->
- $p(t)$ ::@:: is a _shaping pulse_ of unit energy (e.g., a rectangular or raised‑cosine pulse). Here, we assume it is simply a unit rectangular pulse lasting for symbol time $T$. <!--SR:!2026-01-13,63,310!2026-01-09,59,310-->

{@{The transmitted signal}@} is thus {@{$$s_k(t) = \pm A\,p(t), \qquad 0 \le t < T \,.$$}@} {@{The channel}@} adds {@{white Gaussian noise $n(t)$ to the waveform}@}, yielding {@{the received continuous‑time signal}@} {@{$$r(t)= s_k(t)+ n(t).   \tag{1}$$}@} Here {@{$n(t)$}@} is {@{a __Gaussian process__ with zero mean}@} and {@{autocorrelation function}@} {@{$$R_n(t_1, t_2)=E\{n(t_1) n(t_2)\}= \frac{N_0}{2}\,\delta(t_1 - t_2),$$}@} where {@{$N_0/2$}@} is {@{the two-sided power spectral density of the noise}@}. \(annotation: If {@{one-sided \(no negative frequencies\)}@}, then {@{the power spectral density is $N_0$}@}. This explains {@{the division by 2}@}.\) <!--SR:!2026-01-05,56,310!2026-01-04,55,310!2026-01-07,58,310!2026-01-13,63,310!2026-01-06,57,310!2026-01-12,62,310!2026-01-04,55,310!2026-01-15,64,310!2026-01-18,67,310!2026-01-06,57,310!2026-01-07,58,310!2026-01-12,62,310!2025-12-01,19,342!2025-12-01,19,342!2025-12-01,19,342-->

## receiver

{@{The receiver}@} performs {@{a _matched filter_}@} (or equivalently, {@{an integral over one symbol period}@}) to {@{maximise the signal‑to‑noise ratio}@}: {@{$$V = \int_{0}^{T} r(t)\,dt.$$}@} <!--SR:!2026-01-11,61,310!2026-01-04,55,310!2026-01-13,63,310!2026-01-10,60,310!2026-01-15,64,310-->

Because {@{$s_k(t)=\pm A\,p(t)$}@} and {@{$p(t)$}@} is {@{assumed to be a rectangular pulse of duration $T$}@}, {@{the deterministic part of $V$}@} equals {@{$$E[V|b_k=1]   = +AT,\qquad  E[V|b_k=0]   = -AT.$$}@} <!--SR:!2026-01-17,66,310!2026-01-17,66,310!2026-01-11,61,310!2026-01-07,58,310!2026-01-05,56,310-->

{@{The random part}@} comes from {@{integrating the noise \(of two-sided power spectral density $N_0 / 2$\)}@}: {@{$$N_T=\int_{0}^{T} n(t)\,dt,$$}@} which is {@{a Gaussian random variable}@} with mean {@{$$E[N_T]=\int_{0}^{T} E[n(t)]\,dt = \int_{0}^{T} 0\,dt = 0,$$}@} and variance {@{$$\sigma^2_{n_T}=E[(N_T)^2]-[E(N_T)]^2 = \int_{0}^{T}\!\!\int_{0}^{T} E[n(t)n(s)]\,dt\,ds = \int_{0}^{T}\!\!\int_{0}^{T}\frac{N_0}{2}\,\delta(t-s)\,dt\,ds = \frac{N_0}{2}\,T.$$}@} Thus we obtain {@{$$E[N_T]=0,\qquad \sigma^2_{n_T}= \frac{N_0}{2}\,T.$$}@} <!--SR:!2026-01-04,55,310!2026-01-10,60,310!2026-01-12,62,310!2026-01-16,65,310!2026-01-13,63,310!2026-01-14,63,310!2025-12-19,39,290-->

Thus {@{the decision statistic $V$}@} conditioned on {@{the transmitted bit}@} is {@{Gaussian}@}: {@{$$V|b_k=1 \sim \mathcal N(AT,\,\sigma^2_{n_T}),\qquad V|b_k=0 \sim \mathcal N(-AT,\,\sigma^2_{n_T}).$$}@} The receiver makes {@{a hard decision}@} by comparing $V$ with {@{a threshold $V_{\!th}$}@}: {@{$$\hat b_k = \begin{cases} 1,& V>0\\[4pt] 0,& V\le0 \end{cases}.$$}@} If {@{the threshold is zero}@}, because {@{the two symbols are mirror images about zero}@}, {@{a noise sample that flips the sign of $V$}@} causes {@{an error}@}. The threshold can also {@{be nonzero}@}. <!--SR:!2026-01-11,61,310!2026-01-14,63,310!2026-01-15,64,310!2026-01-18,67,310!2026-01-07,58,310!2026-01-03,54,310!2026-01-06,57,310!2026-01-07,58,310!2026-01-09,59,310!2026-01-14,63,310!2026-01-12,62,310!2026-01-13,63,310-->

## bit error rate

In {@{digital communications}@} {@{the _bit error rate_ (BER)}@} is {@{one of the most common metrics}@} used to quantify {@{how reliably a transmitter–receiver pair can convey data over a noisy medium}@}. <!--SR:!2026-01-03,54,310!2026-01-06,57,310!2026-01-16,65,310!2026-01-11,61,310-->

The following section develops {@{the BER expression for this simple model}@} from {@{first principles}@}, detailing the assumptions made about {@{the transmitted waveform, the receiver structure, the noise statistics}@} and finally the mathematical derivation of {@{the BER in terms of the Q‑function and signal energy}@}. <!--SR:!2026-01-18,67,310!2026-01-17,66,310!2026-01-07,58,310!2026-01-03,54,310-->

Let {@{the prior probabilities}@} be {@{$$P(b_k=0)=p_0,\qquad P(b_k=1)=p_1,$$}@} with {@{$p_0+p_1=1$}@}. {@{The a‑priori bit error probabilities}@} are {@{no longer equal}@}; they become {@{$$P_e^{(0)} = P(\hat b_k \neq 0 | b_k=0),\qquad P_e^{(1)} = P(\hat b_k \neq 1 | b_k=1).$$}@} {@{The overall BER}@} is {@{the weighted sum}@} {@{$$P_e = p_0\,P_e^{(0)} + p_1\,P_e^{(1)} \,.$$}@} <!--SR:!2026-01-12,62,310!2026-01-06,57,310!2026-01-10,60,310!2026-01-12,62,310!2026-01-05,56,310!2026-01-14,63,310!2026-01-06,57,310!2026-01-11,61,310!2026-01-15,64,310-->

Below, we split {@{the analysis into two conditioned cases}@}. Then we avoid dealing with {@{mixed‑distribution integrals that are analytically intractable}@}. <!--SR:!2026-01-04,55,310!2026-01-05,56,310-->

### bit error rate with zero threshold

With {@{the hard decision rule}@} {@{$$\displaystyle \hat b_k=\begin{cases}1,& V>0\\[4pt]0,&V\le0\end{cases} \,,$$}@} {@{an error occurs}@} when $V$ has {@{opposite sign to the transmitted symbol}@}. <!--SR:!2026-01-18,67,310!2026-01-03,54,310!2026-01-07,58,310!2026-01-06,57,310-->

For {@{a transmitted '1'}@}: {@{$$P_e^{(1)} = P(N_T < -AT) = Q\!\left(\frac{AT}{\sigma_{n_T} }\right),$$}@} where {@{$\sigma_{n_T}=\sqrt{\tfrac{N_0}{2}\,T}$}@}. Thus {@{$$P_e^{(1)} = Q\!\left(\sqrt{\frac{2A^2T}{N_0} }\right) = Q\!\left(\sqrt{\frac{2E_b}{N_0} }\right) \,,$$}@} where {@{$E_b = A^2 T$}@} is {@{the signal \(excluding the noise\) power \(see below\)}@}. <!--SR:!2026-01-13,63,310!2026-01-16,65,310!2025-12-24,43,290!2026-01-12,62,310!2026-01-18,67,310!2026-01-08,58,310-->

For {@{a transmitted '0'}@}: {@{$$P_e^{(0)} = P(N_T > AT) = Q\!\left(\frac{AT}{\sigma_{n_T} }\right) = Q\!\left(\sqrt{\frac{2A^2T}{N_0} }\right) = Q\left(\sqrt {\frac{2E_b} {N_0} } \right) \,,$$}@} where {@{$E_b = A^2 T$}@} is {@{the signal \(excluding the noise\) power \(see below\)}@}. <!--SR:!2026-01-11,61,310!2025-12-19,39,290!2026-01-17,66,310!2026-01-18,67,310-->

Hence {@{the BER with arbitrary priors}@} is {@{$$\boxed{P_e = p_0\,Q\!\left(\sqrt{\tfrac{2E_b}{N_0} }\right)+p_1\,Q\!\left(\sqrt{\tfrac{2E_b}{N_0} }\right) = Q\!\left(\sqrt{\tfrac{2E_b}{N_0} }\right)} \,.$$}@} Notice how {@{the input bit probabilities}@} do not {@{affect the BER}@}. <!--SR:!2026-01-11,61,310!2025-12-26,44,290!2026-01-13,63,310!2026-01-12,62,310-->

### bit error rate with arbitrary threshold

If the receiver compares {@{$V$ to an arbitrary threshold $V_{\!th}\neq0$}@}, {@{the decision rule}@} becomes   {@{$$\displaystyle \hat b_k=\begin{cases}1,& V>V_{\!th}\\[4pt]0,&V\le V_{\!th}\end{cases} \,.$$}@} <!--SR:!2026-01-04,55,310!2026-01-03,54,310!2026-01-13,63,310-->

For {@{a transmitted '1'}@} {@{the error event}@} is {@{$\{AT+N_T=V\le V_{\!th}\}$}@}, giving {@{$$P_e^{(1)} = Q\!\left(\frac{AT-V_{\!th} }{\sigma_{n_T} }\right).$$}@} <!--SR:!2026-01-14,63,310!2026-01-18,67,310!2026-01-15,64,310!2026-01-10,60,310-->

For {@{a transmitted '0'}@} {@{the error event}@} is {@{$\{-AT+N_T=V>V_{\!th}\}$}@}, giving
$$P_e^{(0)} = Q\!\left(\frac{AT+V_{\!th} }{\sigma_{n_T} }\right).$$ <!--SR:!2026-01-05,56,310!2026-01-12,62,310!2026-01-14,63,310-->

{@{The overall BER with priors $p_0,p_1$}@} is therefore {@{$$\boxed{P_e(V_{\!th})= p_0\,Q\!\left(\frac{AT+V_{\!th} }{\sigma_{n_T} }\right) +p_1\,Q\!\left(\frac{AT-V_{\!th} }{\sigma_{n_T} }\right)} \,.$$}@} {@{Setting $V_{\!th}=0$}@} recovers {@{the zero‑threshold result above}@}. <!--SR:!2026-01-12,62,310!2025-12-19,39,290!2026-01-05,56,310!2026-01-10,60,310-->

### bit error rate insight

{@{The variance term $\sigma^2_{n_T}$}@} governs how much {@{the decision statistic $V$ can deviate from its mean value $\pm AT$}@} before {@{causing a bit error}@}. <!--SR:!2026-01-12,62,310!2026-01-16,65,310!2026-01-14,63,310-->

In {@{a binary antipodal system}@}, {@{the probability of error}@} is governed by {@{the tail probability of a Gaussian distribution}@}; hence it {@{decays exponentially with the ratio}@} {@{$\frac{A^2T}{N_0} = \frac{E_b}{N_0}$}@}. \(The ratio comes from {@{the approximation for large $x$ below}@}.\) Because {@{the noise variance}@} scales {@{linearly with the symbol duration $T$}@}, {@{longer symbols}@} provide {@{more averaging and reduce $\sigma^2_{n_T}$}@}, improving {@{reliability}@}. <!--SR:!2026-01-03,54,310!2026-01-11,61,310!2026-01-03,54,310!2025-12-19,39,290!2025-12-23,42,290!2026-01-10,60,310!2026-01-14,63,310!2026-01-06,57,310!2026-01-04,55,310!2026-01-13,63,310!2025-12-01,19,342-->

Mathematically, for {@{a fixed energy per bit $E_b$}@}, {@{the error probability}@} is {@{$$P_e = Q\!\left(\sqrt{\frac{2E_b}{N_0} }\right) \;\approx\; \sqrt{\frac {N_0} {2E_b} } \frac{1}{\sqrt{2 \pi } }\exp\!\left(-\frac{E_b}{N_0}\right)\quad (E_b/N_0 \gg 1) \,,$$}@} using the approximation: {@{$$Q(x) \approx \frac {\phi(x)} x = \frac 1 {x \sqrt{2\pi} } e^{-x^2 / 2} \qquad x > 0 \,.$$}@} This approximation is {@{asymptotically exact}@} as {@{$x \to \infty$}@}. Thus, improving {@{the signal-to-noise ratio}@} by {@{increasing transmit power or reducing noise spectral density}@} directly {@{translates into a steep reduction in BER}@}. <!--SR:!2026-01-06,57,310!2025-12-19,39,290!2025-12-11,33,270!2026-01-17,66,310!2026-01-10,60,310!2026-01-13,63,310!2026-01-16,65,310!2026-01-16,65,310!2026-01-07,58,310-->

## signal energy

{@{The _signal energy_ \(excluding noise energy\) transmitted during one symbol}@} is {@{$$E_s = \int_{0}^{T} s_k^2(t)\,dt = A^2 \!\int_{0}^{T} p^2(t)\,dt = A^2 T \,,$$}@} since {@{$p(t)$}@} has {@{unit energy \(assumed to be a rectangular pulse of duration $T$\)}@}. <!--SR:!2026-01-10,60,310!2026-01-16,65,310!2026-01-06,57,310!2026-01-07,58,310-->

With {@{non‑equiprobable bits}@} {@{the average energy per bit}@} is {@{$$E_b = p_0\,E_s^{(0)} + p_1\,E_s^{(1)} = (p_0+p_1) A^2 T = A^2 T,$$}@} because {@{both symbols}@} have {@{the same magnitude $A$ and duration $T$}@}. Thus, regardless of {@{the bit priors}@}, {@{$$E_b = A^2 T.$$}@} Note if {@{the two antipodal signals}@} had {@{different amplitudes}@}, the expression would {@{involve $p_0$ and $p_1$ explicitly}@}. <!--SR:!2026-01-11,61,310!2026-01-05,56,310!2026-01-12,62,310!2026-01-17,66,310!2026-01-10,60,310!2026-01-05,56,310!2026-01-11,61,310!2026-01-03,54,310!2026-01-05,56,310!2026-01-10,60,310-->

## signal-to-noise ratio

{@{The _signal‑to‑noise ratio_ (SNR) per bit}@} is then {@{$$\frac{E_b}{N_0/2} = \frac{AT^2}{N_0/2} = \frac{2A^2T}{N_0}.$$}@} Thus, {@{the BER for _zero threshold_ can be expressed compactly}@} as {@{$$\boxed{\text{BER}=Q\!\left(\sqrt{\dfrac{2E_b}{N_0} }\right) \qquad V_{\!th} = 0} \,.$$}@} It is {@{a classic result}@} for {@{binary antipodal signaling over an AWGN channel}@}. <!--SR:!2026-01-14,63,310!2026-01-17,66,310!2026-01-06,57,310!2026-01-17,66,310!2026-01-13,63,310!2026-01-11,61,310-->

## using Q-function

{@{The _Q‑function_}@} is {@{the tail probability of a standard normal random variable}@}: {@{$$Q(x)\;=\;\Pr\{Z > x\}\quad \text{with } Z\sim\mathcal N(0,1) \;=\;\frac{1}{\sqrt{2\pi} }\int_{x}^{\infty} e^{-t^{2}/2}\,\mathrm dt \,.$$}@} It may be calculated by {@{using well‑tabulated Q‑functions}@} apart from {@{numerical integration or simulation}@}. However, most textbooks provide {@{a Q‑table up to $x \approx 3$}@}; beyond that, {@{entries become negligible}@}. <!--SR:!2026-01-15,64,310!2026-01-05,56,310!2026-01-03,54,310!2026-01-12,62,310!2026-01-11,61,310!2026-01-05,56,310!2026-01-04,55,310-->

For {@{large positive arguments}@}, $Q(x)$ can be approximated by {@{$$Q(x)\approx\frac{1}{\sqrt{2\pi}\,x}e^{-x^{2}/2} \,,$$}@} which is {@{asymptotically exact as $x\to\infty$}@}. {@{This approximation}@} simplifies {@{analytical work when deriving closed‑form BER expressions}@}. It shows the function is {@{a strictly decreasing function}@}: {@{larger thresholds}@} lead to {@{smaller tail probabilities}@}; it also {@{rapid decays}@} for {@{large $x$}@}. <!--SR:!2026-01-03,54,310!2026-01-16,65,310!2026-01-13,63,310!2026-01-16,65,310!2026-01-17,66,310!2026-01-16,65,310!2026-01-15,64,310!2026-01-15,64,310!2026-01-12,62,310!2026-01-16,65,310-->

## using error function

{@{The Q‑function}@} can be written in terms of {@{the _complementary_ error function $\operatorname{erfc}$}@}: {@{$$Q(x)=\frac12\,\operatorname{erfc}\!\left(\frac{x}{\sqrt{2} }\right) =\frac12-\frac12\,\operatorname{erf}\!\left(\frac{x}{\sqrt{2} }\right),$$}@} where {@{the ordinary error function}@} is {@{$$\operatorname{erf}(z)= \frac{2}{\sqrt{\pi} }\int_{0}^{z} e^{-t^2}\,dt.$$}@} <!--SR:!2026-01-06,57,310!2026-01-18,67,310!2026-01-17,66,310!2026-01-04,55,310!2026-01-03,44,270-->

{@{These identities are useful}@} when {@{numerical tables or software libraries}@} provide {@{$\operatorname{erfc}$ rather than $Q$}@}. For example, the equation for {@{the BER using zero threshold}@}: {@{$$\boxed{\text{BER}= \frac12\,\operatorname{erfc}\!\left(\sqrt{\dfrac{E_b}{N_0} }\right)} \,,$$}@} and the equation for {@{the BER using arbitrary threshold}@}: {@{$$\boxed{\text{BER}(V_{\!th})= p_{0}\,\tfrac12\,\operatorname{erfc}\!\left(\dfrac{AT+V_{\!th} } {\sqrt{2\,\sigma^2_{n_T} } }\right) +p_{1}\,\tfrac12\,\operatorname{erfc}\!\left(\dfrac{AT-V_{\!th} } {\sqrt{2\,\sigma^2_{n_T} } }\right)} \,.$$}@} <!--SR:!2026-01-15,64,310!2026-01-18,67,310!2026-01-18,67,310!2026-01-07,58,310!2025-12-25,44,290!2026-01-16,65,310!2025-12-10,32,270-->
