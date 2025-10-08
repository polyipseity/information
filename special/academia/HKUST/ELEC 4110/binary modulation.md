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

{@{The simplest analytical model}@}, often called the {@{__binary channel__ or __binary symmetric channel with additive white Gaussian noise__ (__AWGN__)}@}, reduces {@{the whole communication link to a black box}@} that accepts {@{binary input symbols at the transmitter and produces binary output symbols at the receiver}@}. {@{All intermediate physical‑layer details}@} – {@{propagation, multipath, fading, etc.}@} – are {@{absorbed into this single stochastic channel model}@}.

{@{This simple binary channel model}@} underpins {@{many higher‑level analyses in digital communications}@}: it provides the baseline against which {@{coding gains, diversity techniques, or more complex modulation schemes}@} are measured.  In practice, {@{real systems}@} often {@{deviate from this idealization}@} due to {@{multipath fading, colored noise, timing errors and non‑binary signalling}@}; nevertheless, it remains {@{a cornerstone of communication theory}@}.

## bit error rate

In {@{digital communications}@} {@{the _bit error rate_ (BER)}@} is {@{one of the most common metrics}@} used to quantify {@{how reliably a transmitter–receiver pair can convey data over a noisy medium}@}.  

The following article develops {@{the BER expression for this simple model}@} from {@{first principles}@}, detailing the assumptions made about {@{the transmitted waveform, the receiver structure, the noise statistics}@} and finally the mathematical derivation of {@{the BER in terms of the Q‑function and signal energy}@}.

## binary channel

{@{The transmitter}@} sends {@{a sequence of binary symbols $b_k \in \{0,1\}$}@}.  Each symbol occupies {@{a fixed duration $T$}@} and is represented by {@{a pulse waveform}@} {@{$$s(t) = \begin{cases} + A\,p(t), & b_k = 1\\[4pt] - A\,p(t), & b_k = 0 \end{cases}\qquad 0 \le t < T,$$}@} where  

- $A>0$ ::@:: is the pulse amplitude, and
- $p(t)$ ::@:: is a _shaping pulse_ of unit energy (e.g., a rectangular or raised‑cosine pulse). Here, we assume it is simply a rectangular pulse lasting for symbol time $T$.

{@{The transmitted signal}@} is thus {@{$$s_k(t) = \pm A\,p(t), \qquad 0 \le t < T \,.$$}@} {@{The channel}@} adds {@{white Gaussian noise $n(t)$ to the waveform}@}, yielding {@{the received continuous‑time signal}@} {@{$$r(t)= s_k(t)+ n(t).   \tag{1}$$}@} Here {@{$n(t)$}@} is {@{a __Gaussian process__ with zero mean}@} and {@{autocorrelation function}@} {@{$$R_n(t_1, t_2)=E\{n(t_1) n(t_2)\}= \frac{N_0}{2}\,\delta(t_1 - t_2),$$}@} where {@{$N_0/2$}@} is {@{the two‑sided power spectral density of the noise}@}.

## receiver

{@{The receiver}@} performs {@{a _matched filter_}@} (or equivalently, {@{an integral over one symbol period}@}) to {@{maximise the signal‑to‑noise ratio}@}: {@{$$V = \int_{0}^{T} r(t)\,dt.$$}@}

Because {@{$s_k(t)=\pm A\,p(t)$}@} and {@{$p(t)$}@} is {@{assumed to be a rectangular pulse of duration $T$}@}, {@{the deterministic part of $V$}@} equals {@{$$E[V|b_k=1]   = +AT,\qquad  E[V|b_k=0]   = -AT.$$}@}

{@{The random part}@} comes from {@{integrating the noise}@}: {@{$$N_T=\int_{0}^{T} n(t)\,dt,$$}@} which is {@{a Gaussian random variable}@} with mean {@{$$E[N_T]=\int_{0}^{T} E[n(t)]\,dt = \int_{0}^{T} 0\,dt = 0,$$}@} and variance {@{$$\sigma^2_{n_T}=E[(N_T)^2]-[E(N_T)]^2 = \int_{0}^{T}\!\!\int_{0}^{T} E[n(t)n(s)]\,dt\,ds = \int_{0}^{T}\!\!\int_{0}^{T}\frac{N_0}{2}\,\delta(t-s)\,dt\,ds = \frac{N_0}{2}\,T.$$}@} Thus we obtain {@{$$E[N_T]=0,\qquad \sigma^2_{n_T}= \frac{N_0}{2}\,T.$$}@}

Thus {@{the decision statistic $V$}@} conditioned on {@{the transmitted bit}@} is {@{Gaussian}@}: {@{$$V|b_k=1 \sim \mathcal N(AT,\,\sigma^2_{n_T}),\qquad V|b_k=0 \sim \mathcal N(-AT,\,\sigma^2_{n_T}).$$}@} The receiver makes {@{a hard decision}@} by comparing $V$ with {@{a threshold $V_{\!th}$}@}: {@{$$\hat b_k = \begin{cases} 1,& V>0\\[4pt] 0,& V\le0 \end{cases}.$$}@} If {@{the threshold is zero}@}, because {@{the two symbols are mirror images about zero}@}, {@{a noise sample that flips the sign of $V$}@} causes {@{an error}@}. The threshold can also {@{be nonzero}@}.

## deriving bit error rate

Let {@{the prior probabilities}@} be {@{$$P(b_k=0)=p_0,\qquad P(b_k=1)=p_1,$$}@} with {@{$p_0+p_1=1$}@}. {@{The a‑priori bit error probabilities}@} are {@{no longer equal}@}; they become {@{$$P_e^{(0)} = P(\hat b_k \neq 0 | b_k=0),\qquad P_e^{(1)} = P(\hat b_k \neq 1 | b_k=1).$$}@} {@{The overall BER}@} is {@{the weighted sum}@} {@{$$P_e = p_0\,P_e^{(0)} + p_1\,P_e^{(1)} \,.$$}@}

### bit error rate with zero threshold

With {@{the hard decision rule}@} {@{$$\displaystyle \hat b_k=\begin{cases}1,& V>0\\[4pt]0,&V\le0\end{cases} \,,$$}@} {@{an error occurs}@} when $V$ has {@{opposite sign to the transmitted symbol}@}.

For {@{a transmitted '1'}@}: {@{$$P_e^{(1)} = P(N_T < -AT) = Q\!\left(\frac{AT}{\sigma_{n_T} }\right),$$}@} where {@{$\sigma_{n_T}=\sqrt{\tfrac{N_0}{2}\,T}$}@}. Thus {@{$$P_e^{(1)} = Q\!\left(\sqrt{\frac{2A^2T}{N_0} }\right) = Q\!\left(\sqrt{\frac{2E_b}{N_0} }\right) \,,$$}@} where {@{$E_b = A^2 T$}@} is {@{the signal \(excluding the noise\) power \(see below\)}@}.

For {@{a transmitted '0'}@}: {@{$$P_e^{(0)} = P(N_T > AT) = Q\!\left(\frac{AT}{\sigma_{n_T} }\right) = Q\!\left(\sqrt{\frac{2A^2T}{N_0} }\right) = Q\left(\sqrt {\frac{2E_b} {N_0} } \right) \,,$$}@} where {@{$E_b = A^2 T$}@} is {@{the signal \(excluding the noise\) power \(see below\)}@}.

Hence {@{the BER with arbitrary priors}@} is {@{$$\boxed{P_e = p_0\,Q\!\left(\sqrt{\tfrac{2E_b}{N_0} }\right)+p_1\,Q\!\left(\sqrt{\tfrac{2E_b}{N_0} }\right) = Q\!\left(\sqrt{\tfrac{2E_b}{N_0} }\right)} \,,$$}@}. Notice how {@{the input bit probabilities}@} do not {@{affect the BER}@}.

### bit error rate with arbitrary threshold

If the receiver compares {@{$V$ to an arbitrary threshold $V_{\!th}\neq0$}@}, {@{the decision rule}@} becomes   {@{$$\displaystyle \hat b_k=\begin{cases}1,& V>V_{\!th}\\[4pt]0,&V\le V_{\!th}\end{cases} \,.$$}@}

For {@{a transmitted '1'}@} {@{the error event}@} is {@{$\{AT+N_T=V\le V_{\!th}\}$}@}, giving {@{$$P_e^{(1)} = Q\!\left(\frac{AT-V_{\!th} }{\sigma_{n_T} }\right).$$}@}

For {@{a transmitted '0'}@} {@{the error event}@} is {@{$\{-AT+N_T=V>V_{\!th}\}$}@}, giving
$$P_e^{(0)} = Q\!\left(\frac{AT+V_{\!th} }{\sigma_{n_T} }\right).$$

{@{The overall BER with priors $p_0,p_1$}@} is therefore {@{$$\boxed{P_e(V_{\!th})= p_0\,Q\!\left(\frac{AT+V_{\!th} }{\sigma_{n_T} }\right) +p_1\,Q\!\left(\frac{AT-V_{\!th} }{\sigma_{n_T} }\right)} \,.$$}@} {@{Setting $V_{\!th}=0$}@} recovers {@{the zero‑threshold result above}@}.

## signal energy

{@{The _signal energy_ \(excluding noise energy\) transmitted during one symbol}@} is {@{$$E_s = \int_{0}^{T} s_k^2(t)\,dt = A^2 \!\int_{0}^{T} p^2(t)\,dt = A^2 T \,,$$}@} since {@{$p(t)$}@} has {@{unit energy \(assumed to be a rectangular pulse of duration $T$\)}@}.

With {@{non‑equiprobable bits}@} {@{the average energy per bit}@} is {@{$$E_b = p_0\,E_s^{(0)} + p_1\,E_s^{(1)} = (p_0+p_1) A^2 T = A^2 T,$$}@} because {@{both symbols}@} have {@{the same magnitude $A$ and duration $T$}@}. Thus, regardless of {@{the bit priors}@}, {@{$$E_b = A^2 T.$$}@} Note if {@{the two antipodal signals}@} had {@{different amplitudes}@}, the expression would {@{involve $p_0$ and $p_1$ explicitly}@}.

## signal-to-noise ratio

{@{The _signal‑to‑noise ratio_ (SNR) per bit}@} is then {@{$$\frac{E_b}{N_0/2} = \frac{AT^2}{N_0/2} = \frac{2A^2T}{N_0}.$$}@} Thus, {@{the BER for _zero threshold_ can be expressed compactly}@} as {@{$$\boxed{\text{BER}=Q\!\left(\sqrt{\dfrac{2E_b}{N_0} }\right) \qquad V_{\!th} = 0} \,.$$}@} It is {@{a classic result}@} for {@{binary antipodal signaling over an AWGN channel}@}.

## using error function

{@{The Q‑function}@} can be written in terms of {@{the _complementary_ error function $\operatorname{erfc}$}@}: {@{$$Q(x)=\frac12\,\operatorname{erfc}\!\left(\frac{x}{\sqrt{2} }\right) =\frac12-\frac12\,\operatorname{erf}\!\left(\frac{x}{\sqrt{2} }\right),$$}@} where {@{the ordinary error function}@} is {@{$$\operatorname{erf}(z)= \frac{2}{\sqrt{\pi} }\int_{0}^{z} e^{-t^2}\,dt.$$}@}

{@{These identities are useful}@} when {@{numerical tables or software libraries}@} provide {@{$\operatorname{erfc}$ rather than $Q$}@}. For example, the equation for {@{the BER using zero threshold}@}: {@{$$\boxed{\text{BER}= \frac12\,\operatorname{erfc}\!\left(\sqrt{\dfrac{E_b}{N_0} }\right)} \,,$$}@} and the equation for {@{the BER using arbitrary threshold}@}: {@{$$\boxed{\text{BER}(V_{\!th})= p_{0}\,\tfrac12\,\operatorname{erfc}\!\left(\dfrac{AT+V_{\!th} } {\sqrt{2\,\sigma^2_{n_T} } }\right) +p_{1}\,\tfrac12\,\operatorname{erfc}\!\left(\dfrac{AT-V_{\!th} } {\sqrt{2\,\sigma^2_{n_T} } }\right)} \,.$$}@}
