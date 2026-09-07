---
aliases:
  - ELEC 4110 M-FSK
  - ELEC4110 M-FSK
  - M-FSK
tags:
  - flashcard/active/special/academia/HKUST/ELEC_4110/M-FSK
  - language/in/English
---

# _M_-FSK

- see: [general/multiple frequency-shift keying](../../../../general/multiple%20frequency-shift%20keying.md)

{@{_Frequency shift keying_ (M-FSK)}@} assigns {@{$\log_2M$ bits to one of $M$ orthogonal carrier frequencies}@}. {@{Each symbol}@} is {@{a single tone at a distinct frequency}@}, making FSK {@{robust against amplitude fading and nonlinearities}@}—useful in {@{power-limited or distorted channels}@}. {@{Bandwidth grows linearly with $M$}@} because {@{each frequency needs its own spectral allocation}@}.

## waveforms

{@{The transmitted waveform for symbol index $m = 0, \ldots, M - 1$}@} is {@{a tone at one of $M$ frequencies}@}: {@{$$s_m(t)=A\,\cos \!\bigl(2\pi(f_c+\Delta f_m)t\bigr), \qquad 0\le t<T_s \,,$$}@} where {@{$f_c = n / T_s$ ($n$ a positive integer) and $\Delta f_m$ is the offset for symbol $m$}@}. {@{The offsets ensure orthogonality over $T_s$}@} (e.g., {@{$\Delta f_m=m\,\Delta f_{\min}$, $\Delta f_{\min} = 1 / T_s$}@}). {@{$A=\sqrt{2E/T_s}$}@} gives {@{each tone average energy $E$}@}.

## constellation

{@{The $M$-ary FSK constellation}@} is {@{$M$ distinct tones}@}, each at {@{a different frequency}@} (equivalently, {@{unit vectors in $M$-dimensional space}@}).

Assume {@{equiprobable symbols and AWGN}@}. In {@{a coherent receiver}@}, {@{the signal is correlated with every basis $\mathbf{e}_k$}@} and {@{the largest correlation is selected}@}. Each decision region is {@{all vectors whose inner product with one particular unit vector exceeds all others}@}—{@{$M$ orthogonal slices in $M$-dimensional Euclidean space}@}: {@{$$\bigl\{\,\mathbf{r}\;:\;\arg\max_{j \in \set{1, \ldots, M} } |\langle \mathbf{r},\mathbf{e}_j\rangle|^2 = k\bigr\}\,.$$}@}

## error analysis

Assume {@{_equiprobable_ bits and AWGN}@}. {@{The optimal detector}@} is {@{the minimum distance rule}@}.

Project onto {@{a _unnormalized_ basis $\set{s_m(t)}$ with $M$ symbols}@}. Suppose {@{waveform $s_k(t)$ is transmitted}@}. {@{The received signal coefficients}@} are: {@{$$\mathbf y_i = \begin{cases} E_s + n_i & \text{if}~i = k \\ n_i & \text{otherwise} \,, \end{cases}$$}@} where {@{$n_i$ are iid zero-mean normal with variance $\sigma^2 = E_s \frac {N_0} 2$}@}. The detector {@{subtracts $E_s / 2$ \(equal symbol energies\) and picks the maximum}@}: {@{$$y_i = \begin{cases} \frac {E_s} 2 + n_i & \text{if}~i = k \\ n_i - \frac {E_s} 2 & \text{otherwise} \,. \end{cases}$$}@}

{@{A correct decision}@} requires {@{$\frac {E_s} 2 + n_k$ exceeds all $n_i - \frac {E_s} 2$}@}: {@{$$\begin{aligned} P_{ek} & = 1 - \frac 1 {\sqrt{\pi E_s N_0} } \int_{-\infty}^\infty \left(1-Q\left(\frac {y_k + E_s / 2} {\sqrt{E_s N_0 / 2} }\right)\right)^{M - 1} \exp\left(-\frac {(y_k - E_s / 2)^2} {E_s N_0}\right) \,\mathrm dy_k \\ & = 1 - \frac 1 {\sqrt{\pi E_s N_0} } \int_{-\infty}^\infty \left(1-Q\left(\frac {y_k'} {\sqrt{E_s N_0 / 2} }\right)\right)^{M - 1} \exp\left(-\frac {(y_k' - E_s)^2} {E_s N_0}\right) \,\mathrm dy_k' \\ & = 1 - \frac 1 {\sqrt{\pi E_s N_0} } \int_{-\infty}^\infty \left(1-Q\left(\frac {y_k'} {\sqrt{E_s N_0 / 2} }\right)\right)^{M - 1} \exp\left(-\frac {\left(\frac {y_k'} {\sqrt{E_s N_0 / 2} } - \sqrt{\frac {2E_s} {N_0} } \right)^2} 2\right) \,\mathrm dy_k' \,. \end{aligned}$$}@} Substituting {@{$y_k'' = \frac {y_k'} {\sqrt{E_s N_0 / 2} } = \frac {y_k + E_s / 2} {\sqrt{E_s N_0 / 2} }$}@} gives {@{$$P_{ek} = 1 - \frac 1 {\sqrt{2\pi} } \int_{-\infty}^\infty (1-Q(y_k''))^{M - 1} \exp\left(-\frac {\left(y_k'' - \sqrt{\frac {2E_s} {N_0} } \right)^2} 2\right) \,\mathrm dy_k'' \,,$$}@} or equivalently {@{$$\boxed{P_{ek} = 1 - \frac 1 {\sqrt{2\pi} } \int_{-\infty}^\infty \left(1-Q\left(x + \sqrt{\frac {2 E_s} {N_0} } \right)\right)^{M - 1} \exp\left(-\frac {x^2} 2\right) \,\mathrm dx} \,.$$}@} The space is scaled by {@{$\frac 1 {\sqrt{E_s N_0 / 2} }$}@} so {@{all variables have unit variance}@}. {@{The noise on other coordinates}@} must not exceed {@{$x + \sqrt{\frac {2E_s} {N_0} }$}@}, giving the formula above.

Since {@{the signal set is geometrically symmetric}@}, {@{$P_{ei} = P_{ek}$ for all $i$}@} and {@{the symbol error probability}@} is {@{$$P_{eM} = \frac 1 M \sum_{1 \le i \le M} P_{ei} = P_{ek} \,.$$}@}

From {@{the symbol error formula}@}: {@{$$\boxed{P_{eM} = 1 - \frac 1 {\sqrt{2\pi} } \int_{-\infty}^\infty \left(1-Q\left(x + \sqrt{\frac {2 E_s} {N_0} } \right)\right)^{M - 1} \exp\left(-\frac {x^2} 2\right) \,\mathrm dx} \,,$$}@} {@{raising $\frac {E_s} {N_0}$}@} decreases {@{$P_{eM}$}@}, while {@{raising $M$}@} increases it. With {@{_bit_ energy $E_b$}@} and {@{$E_s = E_b \log_2 M$}@}, fixing {@{$\frac {E_b} {N_0}$}@}: {@{raising $M$}@} raises {@{$P_{eM}$}@} when {@{$\frac {E_b} {N_0}$ is low and lowers it when high}@}. As {@{$M \to \infty$}@}, if {@{$\frac {E_b} {N_0}$ exceeds about −1.59&nbsp;dB}@} ({@{the _Shannon limit_}@}: {@{$1 / \log_2 e = \ln 2 \approx 0.693$}@}), then {@{$P_{eM} \to 0$}@}; otherwise {@{$P_{eM} \to 1$}@}.

### bit error probability

{@{_Bit errors_}@} differ from {@{_symbol_ errors}@}. With {@{geometric symmetry}@}, on {@{a symbol error the other $M - 1$ symbols are equally likely}@} so {@{about half the bits are wrong on average}@}: {@{$$\boxed{P_e \approx \frac 1 2 P_{eM} } \,.$$}@}

For {@{a precise derivation}@} with {@{$k = \log_2 M$}@}, the probability of {@{$n$-bit errors per symbol}@} is {@{$\binom k n \frac {P_{eM} } {M - 1}$}@}. {@{The average error bits per symbol}@} is: {@{$$\sum_{n = 1}^k n \binom k n \frac {P_{eM} } {M - 1} = \frac {P_{eM} } {M - 1} \sum_{n = 1}^k n \binom k n = \frac {P_{eM} } {M - 1} \sum_{n = 1}^k \frac {k!} {(n - 1)! (k - n)!} \,$$}@} giving {@{the _bit_ error probability}@}: {@{$$\begin{aligned} P_e & = \frac {P_{eM} } {M - 1} \frac 1 k \sum_{n = 1}^k \frac {k!} {(n - 1)! (k - n)!} \\ & = \frac {P_{eM} } {M - 1} \sum_{n = 1}^k \frac {(k - 1)!} {(n - 1)! ((k - 1) - (n - 1))!} \\ & = \frac {P_{eM} } {M - 1} \sum_{n = 1}^k \binom {k - 1} {n - 1} = \frac {P_{eM} } {M - 1} \sum_{n = 0}^{k - 1} \binom {k - 1} n \\ & = \frac {P_{eM} } {M - 1} (1 + 1)^{k - 1} = \frac {P_{eM} } {M - 1} \frac M 2 \,. \end{aligned}$$}@} Thus {@{$$\boxed{P_e = \frac {P_{eM} } {M - 1} \frac M 2 = \frac {P_{eM} } 2 \frac M {M - 1} } \,.$$}@} As {@{$M \to \infty$}@}, {@{$P_e \to P_{eM} / 2$}@}.

### symbol error probability bounds

{@{Exact $P_{eM}$ evaluation}@} requires {@{multi-dimensional integrals}@}. {@{The union bound}@} replaces {@{this with a sum over pairwise error events}@}: {@{$$P_{eM} \leq \frac 1 M \sum_{m=1}^{M}\sum_{\substack{k=1\\k\neq m} }^{M} P(s_k \mid s_m) \,,$$}@} assuming {@{_equiprobable_ symbols}@}.

For {@{M-FSK}@}, {@{the pairwise error probability}@} is: {@{$$\boxed{P(s_k \mid s_m) = Q\left(\frac {\sqrt{2E_s} } {2\sqrt{N_0 / 2} } \right) = Q\left(\sqrt{\frac {E_s} {N_0} } \right) }$$}@} by considering {@{projections on the normalized basis}@}: {@{$d = \sqrt{2E_s}$, $\sigma_n^2 = N_0 / 2$}@}. This holds for {@{all $k \ne m$}@}, so {@{the symbol error upper bound}@} is: {@{$$\boxed{P_{eM} \le (M - 1) Q\left(\sqrt{\frac {E_s} {N_0} } \right)} \,,$$}@} \(annotation: This can also be obtained from {@{the upper bound in [M-ary transmission § error analysis for minimum distance](M-ary%20transmission.md#error%20analysis%20for%20minimum%20distance)}@}.\) and {@{bit error upper bound}@}: {@{$$\boxed{P_{eB} = \frac M {2(M - 1)} P_{eM} \le \frac M 2 Q\left(\sqrt{\frac {E_s} {N_0} } \right)} \,.$$}@} Using the approximation {@{$Q(x) \le \frac 1 2 e^{-x^2 / 2}$}@} (accurate for {@{$x \ge 3$}@}, different from the binary modulation approximation): {@{$$Q(x) \le \frac 1 2 e^{-x^2 / 2} \,,$$}@} the above is usually rewritten as {@{$$\boxed{P_{eB} \approx \frac M 4 \exp\left(\frac {E_s} {2N_0} \right) = \frac M 4 \exp\left(\frac {kE_b} {2N_0} \right) } \,.$$}@}

{@{The _bit_ error union bound}@} is {@{exact for $M = 2$}@} and {@{tight for moderate-to-high SNR with small $M$}@}.

### error analysis using simulation

{@{Simulations are more common}@} in practice. Because {@{the bit error rate is small}@}, {@{simulations must run long enough}@} to converge {@{on a reliable estimate}@}. They show {@{the union bound is a good approximation in most cases}@}. \(We cannot know {@{_a priori_}@} whether {@{the bound is tight}@}.\)
