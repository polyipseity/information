---
aliases:
  - DFT
  - DFTs
  - discrete Fourier transform
  - discrete Fourier transforms
tags:
  - flashcard/active/special/audio_signal_processing/discrete_Fourier_transform
  - language/in/English
---

# discrete Fourier transform

- see: [general/discrete Fourier transform](../../general/discrete%20Fourier%20transform.md)

## definition

The discrete Fourier transform (DFT) {@{transforms a sequence of length $N$ into another sequence of length $N$}@}. It is defined by: {@{$$X[k] := \sum_{n = 0}^{N - 1} x[n] \cdot e^{-j 2\pi (k / N) n} = \sum_{n = 0}^{N - 1} x[n] \left(\cos(2 \pi (k / N) n) - j \sin(2 \pi (k / N) n) \right)$$}@}. <!--SR:!2025-07-13,260,330!2025-02-18,124,290-->

The inverse discrete Fourier transform (IDFT) is {@{the inverse of DFT (duh)}@}. It {@{recovers the the original signal of length $N$ given a sequence of length $N$ transformed by DFT}@}. It is defined by: {@{$$x[n] := \frac 1 N \sum_{k = 0}^{N - 1} X[k] \cdot e^{j 2\pi (k / N) n} = \frac 1 N \sum_{k = 0}^{N - 1} X[k] \left(\cos(2 \pi (k / N) n) + j \sin(2 \pi (k / N) n) \right)$$}@}. One can see the formula is {@{almost the same as DFT}@}, except that {@{a factor of $1 / N$ is added, the input and output sequences are swapped, and the sign of the exponent is negated}@}. <!--SR:!2025-08-10,283,330!2025-02-15,136,310!2024-12-10,77,270!2025-09-05,303,330!2025-08-20,291,330-->

The above formulas are {@{the most conventional way of writing them}@}. The only requirements for the formula of DFT and IDFT are that {@{the sign of the exponent is opposite (convention: $-$ for DFT, $+$ for IDFT) and the product of the two multiplication factors is $1 / N$ (convention: $1$ for DFT, $1 / N$ for IDFT)}@}. <!--SR:!2025-04-27,183,310!2025-09-04,302,330-->

## properties

### periodicity

- see: [general/discrete Fourier transform § periodicity](../../general/discrete%20Fourier%20transform.md#periodicity)

The original sequence is {@{treated as $N$-periodic}@} by DFT. The transformed sequence is {@{also $N$-periodic}@}. Likewise, the DFT-transformed sequence is {@{treated as $N$-periodic}@} by IDFT. The recovered original sequence is {@{also $N$-periodic}@}. This is easily shown {@{directly from the definition}@}. <!--SR:!2025-06-27,247,330!2025-09-10,307,330!2025-08-04,278,330!2025-08-11,283,330!2024-11-17,69,346-->

### expressing the inverse DFT in terms of the DFT

- see: [general/discrete Fourier transform § expressing the inverse DFT in terms of the DFT](../../general/discrete%20Fourier%20transform.md#expressing%20the%20inverse%20DFT%20in%20terms%20of%20the%20DFT)

Note that the formulas for DFT and IDFT are {@{extremely similar}@}. Indeed, one can {@{write the IDFT in terms of the DFT}@}. <!--SR:!2025-08-04,278,330!2024-11-29,80,346-->

### linearity

- see: [general/discrete Fourier transform § linearity](../../general/discrete%20Fourier%20transform.md#linearity)

The DFT is {@{a linear transform}@}. That is, {@{$$\mathcal{F}(\{a x_n + b y_n\})_k= a \mathcal{F}(\{x_n\})_k + b \mathcal{F}(\{y_n\})_k$$ for any complex numbers $a$ and $b$}@}. This can be shown {@{directly from the definition}@}. <!--SR:!2025-07-30,267,346!2025-08-13,276,346!2024-11-19,71,346-->

### shift

- see: [general/discrete Fourier transform § shift theorem](../../general/discrete%20Fourier%20transform.md#shift%20theorem)

{@{Shifting the signal in the time domain to the right by $n_0$ samples}@} corresponds to {@{multiplying the signal in the frequency domain by $e^{-\frac{j 2\pi} N kn_0}$}@}. This can be shown {@{directly from the definition}@}. <!--SR:!2025-06-28,228,346!2025-04-19,174,326!2025-09-28,319,366-->

This shift from the time domain to the frequency domain has an intuitive interpretation. Interpret the argument (angle) of the complex number for each frequency as {@{its time offset}@}. Shifting a signal to the right (with warping) in the time domain {@{increases the time offset for all frequencies}@}. This means the complex number for each frequency is {@{multiplied (rotated) by $e^{-\frac {j 2\pi} N k n_0}$, changing its argument (angle) while keeping its modulus (length) unchanged}@}. This corresponds to {@{shifting its corresponding complex sinusoid in the time domain to the right (with warping)}@}. <!--SR:!2025-09-25,317,366!2025-03-25,155,326!2025-05-24,196,326!2025-05-21,195,326-->

By duality, {@{shifting the signal in the frequency to the right by $k_0$ samples}@} corresponds to {@{multiplying the signal in the time domain by $e^{\frac{j 2\pi} N n k_0}$ (notice there is no negative sign)}@}. This can also be shown {@{directly from the definition}@}. <!--SR:!2025-09-18,312,366!2024-12-09,76,306!2025-04-19,180,333-->

### symmetry

- see: [general/discrete Fourier transform § DFT of real and purely imaginary signals](../../general/discrete%20Fourier%20transform.md#DFT%20of%20real%20and%20purely%20imaginary%20signals)

If {@{the signal in the time domain is purely real}@}, then {@{the signal in the frequency domain is even conjugate symmetric, i.e. $$X[k] = X^*[-k]$$}@}. Interpreting this in {@{rectangular form}@}, {@{the real part is even symmetric while the imaginary part is odd symmetric (up to mod $2\pi$)}@}. Interpreting this in {@{polar form}@}, {@{the modulus (length) is even symmetric while the argument (angle) is odd symmetric (up to mod $2\pi$)}@}. <!--SR:!2024-12-06,86,346!2024-11-22,74,346!2024-11-18,70,346!2025-06-15,229,346!2025-07-12,250,346!2025-03-12,146,326-->

Furthermore, if {@{the signal in the time domain is _additionally_ even symmetric}@}, then {@{the frequency domain is _additionally_ even symmetric}@}. Interpreting this in {@{rectangular form}@}, {@{the real part is even symmetric while the imaginary part is always zero}@}. Interpreting this in {@{polar form}@}, {@{the modulus (length) is even symmetric while the argument (angle) is always an integer multiple of $\pi$}@}. <!--SR:!2024-11-27,79,346!2025-08-15,280,346!2025-06-16,229,346!2024-11-23,75,346!2024-12-01,82,346!2025-09-21,314,366-->

### convolution

- see: [general/discrete Fourier transform § circular convolution theorem](../../general/discrete%20Fourier%20transform.md#circular%20convolution%20theorem)

{@{Convoluting two signals in the time domain}@} corresponds to {@{multiplying the two signals in the frequency domain}@}. That is, {@{$$\mathcal{F}(x * y) = XY \qquad x * y = \mathcal{F}^{-1}(XY)$$}@}. This is also easily shown {@{from the definition}@}. <!--SR:!2025-09-22,315,366!2024-11-23,75,346!2025-09-14,308,366!2025-10-06,324,366-->

To understand this convolution theorem, imagine two $N$-length signals {@{decomposed into two linear combinations of complex sinusoids $e^{-\frac {j 2\pi} N kn}$ with different frequency indices $k$}@}. Convolution of the two signals can also be {@{expressed as the _sliding dot product_ of one signal and the other signal going backwards in time}@}. That means the complex sinusoids are {@{multiplied into terms like $A_0 A_1 \sum_{n = 0}^{N - 1} e^{\frac{j 2\pi} N k_0 n} e^{\frac{j 2\pi} N k_1 (n' - n)}$}@}. Notice said terms can be rewritten as: {@{$$\begin{aligned} A_0 A_1 \sum_{n = 0}^{N - 1} e^{\frac{j 2\pi} N k_0 n} e^{\frac{j 2\pi} N k_1 (n' - n)} & = A_0 A_1 e^{\frac{j 2\pi } N k_1 n'} \sum_{n = 0}^{N - 1} e^{\frac{j 2\pi} N k_0 n} e^{-\frac{j 2\pi} N k_1 n} \\ & = A_0 A_1 e^{\frac{j 2\pi } N k_1 n'} \sum_{n = 0}^{N - 1} e^{\frac{j 2\pi} N k_0 n} \left( e^{\frac{j 2\pi} N k_1 n} \right)^* \\ & = A_0 A_1 e^{\frac{j 2\pi } N k_1 n'} \left\langle e^{\frac{j 2\pi} N k_0 n}, e^{\frac{j 2\pi} N k_1 n} \right\rangle && (\text{using the dot product that is linear in the 1st argument}) \end{aligned}$$}@}. Intuitively ({@{__rigorous in this case__}@}; left as an exercise), the dot product {@{between two complex sinusoids of different frequency indices ($k_0 \ne k_1$) cancels out while that of the same frequency index ($k_0 = k_1$) has their amplitudes multiplied together ($A_0 A_1$; $e^{\frac{j 2\pi } N k_1 n'}$ modifies the phase only)}@}. So {@{the product of the two signals in the frequency domain is the DFT of their convolution in the time domain}@}. <!--SR:!2025-09-11,306,366!2025-05-01,196,346!2024-12-04,84,346!2024-11-18,70,346!2024-12-08,88,346!2025-08-06,273,346!2025-08-08,278,346-->

### energy conservation

- see: [general/discrete Fourier transform § The Plancherel theorem and Parseval's theorem](../../general/discrete%20Fourier%20transform.md#The%20Plancherel%20theorem%20and%20Parseval's%20theorem)

"Energy" is {@{conserved after applying DFT or IDFT on a signal, up to a factor of $1 / N$}@}. "Energy" here means {@{the squared length of the vector when the sequence of values in a signal is treated as a vector}@}. Mathematically, this is: {@{$$\sum_{n = 0}^{N - 1} \lvert x[n]\rvert^2 = \frac 1 N \sum_{k = 0}^{N - 1} \lvert X[k] \rvert^2$$}@}. <!--SR:!2024-11-23,72,353!2025-07-10,244,353!2025-08-19,279,353-->

## interpretation

Usually, the original sequence is {@{in the time domain, i.e. it represents the (complex) amplitude as a function of time}@}. Then, the transformed sequence is {@{in the frequency domain, i.e. it represents the (complex) amplitude as a function of frequency}@}. The $k$-th value of the transformed sequence represents a frequency of {@{$k / TN$ or $k f_s / N$}@}. That is, each value of the transformed value is separated by {@{$1 / TN$ (the reciprocal of the duration of the input sequence) or $f_s / N$ (the ratio of sampling frequency over the number of sequences)}@}. <!--SR:!2025-06-14,236,330!2025-03-30,162,310!2025-02-06,109,250!2025-06-12,218,310-->

Each element $x[n]$ in the original sequence represents {@{the (complex) amplitude at time $nT$}@}. Likewise, each element $X[k]$ in the transformed sequence represents {@{the (complex) amplitude of the complex sinusoid $\left(e^{j 2\pi (k / N) n} \right)$ of cycle frequency $k / N$ (__cycle frequency__: $k$ cycles of the complex sinusoid per $N$ sample; the __actual frequency__ is $k / TN$ or $k f_s / N$) in the original sequence}@}. This also shows a $N$-periodic discrete signal can always be represented by {@{the sum of $N$ complex sinusoidal components via DFT}@}. <!--SR:!2025-07-23,268,330!2025-02-23,120,250!2025-07-23,268,330-->

### components

DFT can also be treated as {@{a dot (scalar) product of the original sequence and a complex sinusoid of various frequencies}@}: {@{$$\begin{aligned} s_k[n] & := e^{j 2\pi (k / N) n} = \left(e^{-j 2\pi (k / N) n} \right)^* \\ X[k] & := \sum_{k = 0}^{N - 1} x[n] \cdot e^{-j 2\pi (k / N) n} = \sum_{k = 0}^{N - 1} x[n] \cdot s_k^*[n] = \langle x, s_k \rangle \end{aligned}$$}@}. This shows DFT can {@{extract the complex sinusoidal component of cycle frequency $k / N$ from the original signal}@}. Likewise, IDFT can also be treated as {@{a dot (scalar) product of the transformed sequence and a complex sinusoidal component (in the frequency domain) of cycle frequency $-k / N$}@}. <!--SR:!2025-04-12,171,310!2025-05-01,196,310!2025-04-03,165,310!2024-12-28,95,290-->

To see why DFT can extract complex sinusoidal components from any signal, consider {@{applying DFT on a complex sinusoid}@}. The complex sinusoid of cycle frequency $k_0 / N$ is defined as: {@{$$s_{k_0}[n] := e^{j 2\pi (k_0 / N) n} \qquad n = 0, \ldots, N - 1$$}@}. Applying DFT: {@{$$\begin{aligned} S_{k_0}[k] & := \sum_{n = 0}^{N - 1} s_{k_0}[n] \cdot e^{-j 2\pi (k / N) n} \\ & = \sum_{n = 0}^{N - 1} e^{j 2\pi (k_0 / N) n} \cdot e^{-j 2\pi (k / N) n} \\ & = \sum_{n = 0}^{N - 1} e^{j 2\pi ((k_0 - k) / N) n} \\ & = \frac {1 - e^{j 2\pi (k_0 - k)} } {1 - e^{j 2\pi ((k_0 - k) / N)} } && (\text{sum of geometric sequence when }k_0 \equiv k \pmod N) \end{aligned}$$}@}. When {@{$k_0 \not\equiv k \pmod N$}@}, then the numerator is {@{zero, nothing that $k_0 - k$ is an nonzero integer, so $e^{j 2\pi (k_0 - k)} = 1$}@}. The denominator is {@{nonzero, as $k_0 - k$ is not evenly divided by $N$, thus $e^{j 2\pi (k_0 - k)} \ne 1$}@}. Finally {@{$S_{k_0}[k] = 0$}@}. When {@{$k_0 \equiv k \pmod N$ (i.e. the difference is evenly divided by $N$)}@}, {@{the sum of geometric sequence cannot be applied and we need to go back up one step}@}. This is because {@{now both the numerator and denominator are both zero}@}, caused by that {@{the sum sequence is no longer a geometric sequence but a constant sequence instead}@}. In this case, it is {@{obvious that the each term of the sum in that previous step is $1$}@}, so {@{$S_{k_0}[k_0 + Nx] = N \quad x \in \mathbb Z$}@}. This also explains why {@{the transformed sequence is $N$-periodic}@}. When the complex sinusoid {@{has an (complex) amplitude of $A$}@}, then {@{the resulting value is also multiplied by $A$, i.e. $S_{k_0}[k_0 + Nx] = AN \quad x \in \mathbb Z$}@}. Likewise, IDFT have properties analogous to above. An important difference is {@{the resulting value becomes $s_{n_0}[-n_0 + Nx] = A \quad x \in \mathbb Z$ instead}@}. <!--SR:!2025-06-04,229,330!2025-07-23,268,330!2025-01-27,118,290!2025-03-01,135,290!2025-09-14,309,330!2025-09-06,303,330!2025-09-23,317,330!2025-03-27,159,310!2025-08-10,283,330!2025-07-13,260,330!2024-12-19,86,290!2025-08-22,292,330!2025-01-25,109,290!2025-07-06,254,330!2024-11-21,66,270!2025-04-03,165,310!2024-12-28,101,290-->

Another property of DFT is that {@{it is linear}@}. That is, {@{adding multiple signals together and applying DFT yields the same result as applying DFT on multiple signals individually and then adding the DFTs}@}. (This can be proved easily and left as an exercise.) With the above two properties, one can see {@{the sum of multiple complex sinusoids can be extracted using DFT}@}. Finally, one more thing to know (given here and not proven here) is that {@{any (discrete complex) signal of length $N$ can be exactly decomposed into $N$ complex sinusoids}@}. So this is why DFT can extract complex sinusoidal components from any (discrete complex) signal. For IDFT, {@{the same applies}@}. <!--SR:!2025-07-01,250,330!2025-09-21,316,330!2025-08-11,285,330!2025-09-20,315,330!2025-06-27,247,330-->

For {@{real sinusoids}@}, it is also easy to derive their DFT as {@{they can be written as a sum of 2 complex sinusoids with opposing frequencies}@}. For example, {@{a real cosine wave of cycle frequency $k_0 / N$: $$\cos_{k_0}[n] := A \cos(2\pi (k_0 / N) n) \qquad n = 0, \ldots, N - 1$$}@} can be written as {@{the weighted sum of 2 complex sinusoids with cycle frequency $k_0 / N$ and $-k_0 / N$: $$\cos_{k_0}[n] = A \cos(2\pi (k_0 / N) n) = \frac {A e^{j 2\pi (k_0 / N) n} } 2 + \frac {A e^{-j 2\pi (k_0 / N) n} } 2$$}@}. By linearity, the nonzero DFT values are {@{$$\begin{aligned} \operatorname{Cos}_{k_0}[k_0] & = \frac {AN} 2 \\ \operatorname{Cos}_{k_0}[-k_0] = \operatorname{Cos}_{k_0}[N - k_0] & = \frac {AN} 2 \end{aligned}$$}@}. For {@{a real sine wave of cycle frequency $k_0 / N$: $$\sin_{k_0}[n] := A \sin(2 \pi (k_0 / N) n) \qquad n = 0, \ldots, N - 1$$}@}, it can also be expressed as {@{the weighted sum of 2 complex sinusoids with cycle frequency $k_0 / N$ and $-k_0 / N$: $$\sin_{k_0}[n] := A \sin(2 \pi (k_0 / N) n) = \frac {A e^{j 2\pi (k_0 / N) n} } {2j} - \frac {A e^{-j 2\pi (k_0 / N) n} } {2j}$$}@}. By linearity, the nonzero DFT values are {@{$$\begin{aligned} \operatorname{Sin}_{k_0}[k_0] & = \frac {AN} {2j} = -j \frac {AN} 2 \\ \operatorname{Sin}_{k_0}[-k_0] = \operatorname{Sin}_{k_0}[N - k_0] & = -\frac {AN} {2j} = j \frac {AN} 2 \end{aligned}$$}@}. For IDFT, {@{the same applies}@}, except that {@{the nonzero IDFT values are divided by $N$ (no $N$ in the resulting values), and for a real sine wave (in the frequency domain), have their signs reversed}@}. <!--SR:!2025-06-14,236,330!2025-03-25,168,310!2025-02-27,147,310!2025-02-02,115,290!2025-04-03,165,310!2025-06-16,220,310!2025-01-06,90,250!2024-12-16,83,270!2025-02-08,123,290!2025-04-15,157,270-->

Note that if {@{you try to use Python to repeat the above mathematical proofs}@}, you may {@{find that the DFT is nonzero at more than 2 points}@}. A common mistake that causes the above is that {@{$k_0$ is not an integer}@}. However, even if the common mistake is fixed, {@{there may still be very tiny nonzero values apart from those 2 points}@}. This is because {@{decimal numbers in Python are represented by floating points, which cannot represent the decimal numbers exactly, which is called quantization error}@}. This is {@{not fixable, unfortunately}@}. <!--SR:!2025-09-08,305,330!2025-07-12,261,330!2025-06-08,232,330!2025-06-11,234,330!2025-08-11,283,330!2025-07-16,264,330-->

## spectrums

{@{The magnitude spectrum}@} is {@{the transformed signal under the modulus operation $\lvert X \rvert$ (length of the complex amplitude)}@}. For easier visualization, the magnitude may be {@{in logarithm scale}@}. The magnitude, intuitively, represents {@{the loudness of the complex sinusoid of a given frequency}@}. <!--SR:!2025-09-07,304,330!2025-08-19,288,330!2025-08-17,286,330!2025-03-29,170,310-->

{@{The phase spectrum}@} is {@{the transformed signal under the argument operation $\operatorname{arg}(X)$ (angle of the complex amplitude)}@}. The phase, intuitively, represents {@{the time offset of the complex sinusoid of a given frequency}@}. <!--SR:!2024-11-18,63,333!2025-09-03,292,353!2024-12-12,86,353-->

### decibel

- see: [general/decibel](../../general/decibel.md)

It is often more helpful to plot the magnitude spectrum in {@{a logarithmic scale to show small differences well}@}. {@{The decibel (dB)}@} is often used. The magnitude values can be converted into decibels using the following equation: {@{$$A_{\mathrm{dB} } = 20 \cdot \log_{10} (A_{\mathrm{abs} })$$}@}. <!--SR:!2025-06-01,221,353!2024-11-29,74,353!2024-12-02,79,353-->

### phase unwrapping

- see: [`np.unwrap`](https://numpy.org/doc/stable/reference/generated/numpy.unwrap.html)

To make the phase spectrum {@{less jumpy (more continuous)}@}, the phase may be {@{wrapped around $2\pi$ such that the difference from the previous phase is not more than $\pi$ (see [`np.unwrap`](https://numpy.org/doc/stable/reference/generated/numpy.unwrap.html))}@}. <!--SR:!2024-11-19,69,353!2024-11-29,76,353-->

## zero padding

Zero padding refers to {@{adding an arbitrary number of zero values to a signal in the time or frequency domain in the middle, assuming the indices are from $0$ to $N - 1$; or on both ends symmetrically, assuming the indices are centered around $0$}@}. This is the {@{_zero-centered_ variant}@}, which is {@{more natural with respect to the mathematics of DFT}@} and {@{can be applied to the frequency [spectrum](#spectrums) of a real signal (the other variant makes the originally real signal have imaginary components)}@}. The resulting phase (angle) spectrum of the signal is also {@{not offsetted}@}, allowing us to {@{obtain a very smooth phase spectrum after [unwrapping](#phase%20unwrapping)}@}. <!--SR:!2025-05-03,176,333!2025-07-27,258,353!2024-12-06,81,353!2025-06-01,199,333!2025-07-07,243,353!2025-07-15,250,353-->

The other variant is {@{the _causal_ variant}@}, which {@{adds an arbitrary number of zero values to a signal in the time or frequency domain at the end, assuming the indices are from $0$ to $N - 1$}@}. <!--SR:!2024-12-11,85,353!2024-12-02,77,353-->

The effect of {@{zero padding a signal in the time domain}@} is that {@{its corresponding DFT has its values interpolated such that it has the same number of values as the signal in the time domain, similar to scaling up an image}@}. Common reasons for zero padding the signal in the time domain include {@{interpolating the signal in the frequency domain and making the number of signal samples a power of two so that fast Fourier transform (FFT) can be applied to it}@}. <!--SR:!2025-06-09,221,353!2025-02-27,131,313!2025-06-10,225,353-->

By duality, zero padding a signal in the frequency domain corresponds to {@{interpolating the signal in the time domain}@}. <!--SR:!2025-08-16,277,353-->

Zero padding can {@{make the input size suitable}@} for {@{[fast Fourier transform](#fast%20Fourier%20transform) (FFT)}@}. It can also be used to {@{minimize the energy spread (the spread of values into adjacent frequencies in the frequency domain) of the resulting DFT}@} for {@{a signal made of a combination of sinusoidal waves}@}. <!--SR:!2024-11-18,65,353!2025-07-01,238,353!2025-05-19,189,333!2025-04-26,173,333-->

## fast Fourier transform

- see: [general/fast Fourier transform](../../general/fast%20Fourier%20transform.md)

Fast Fourier transform (__FFT__) is {@{a fast algorithm for computing the DFT of a signal}@}. It works by {@{breaking down DFT of a long signal into several DFTs of shorter signals recursively}@}. <!--SR:!2024-11-17,67,353!2025-08-16,276,353-->

Its time complexity, that is {@{how the running time grows with input size}@}, is {@{$O(n \log n)$, instead of $O(n^2)$ for DFT computed by its definition}@}. This means {@{for large input sizes, much time can be saved}@}. So in practice, {@{FFT is used over the traditional DFT}@}. <!--SR:!2024-12-10,84,353!2024-11-17,62,333!2025-07-24,257,353!2025-06-26,234,353-->

The most common form of FFT is {@{the Cooley–Tukey algorithm}@} that {@{divides the signal into 2 equal-length signals recursively}@}, so {@{it requires the input size to be a power of 2}@}. This can be fixed using {@{[zero padding](#zero%20padding)}@}. This algorithm also {@{has other variants that divide the signal into arbitrary many equal-length signals recursively}@}, but this will not be discussed here. <!--SR:!2025-06-05,218,353!2025-08-23,280,353!2025-07-12,247,353!2025-06-21,230,353!2025-08-07,267,353-->

Note that when {@{zero padding a signal for FFT}@}, it is important to {@{apply the zero-centered variant instead of the causal one}@}. (The reason is mentioned above already.) <!--SR:!2025-09-06,294,353!2024-12-09,83,353-->

Note that FFT is fundamentally {@{the same thing as DFT}@}, with the only difference being {@{how the values are actually computed}@}. <!--SR:!2025-07-22,260,353!2025-03-29,162,333-->
