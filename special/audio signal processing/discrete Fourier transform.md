---
aliases:
  - DFT
  - DFTs
  - discrete Fourier transform
  - discrete Fourier transforms
tags:
  - flashcard/special/audio_signal_processing/discrete_Fourier_transform
  - language/in/English
---

# discrete Fourier transform

- see: [general/discrete Fourier transform](../../general/discrete%20Fourier%20transform.md)

## definition

The discrete Fourier transform (DFT) {{transforms a sequence of length $N$ into another sequence of length $N$}}. It is defined by: {{$$X[k] := \sum_{n = 0}^{N - 1} x[n] \cdot e^{-j 2\pi (k / N) n} = \sum_{n = 0}^{N - 1} x[n] \left(\cos(2 \pi (k / N) n) - j \sin(2 \pi (k / N) n) \right)$$}}.

The inverse discrete Fourier transform (IDFT) is {{the inverse of DFT (duh)}}. It {{recovers the the original signal of length $N$ given a sequence of length $N$ transformed by DFT}}. It is defined by: {{$$x[n] := \frac 1 N \sum_{k = 0}^{N - 1} X[k] \cdot e^{j 2\pi (k / N) n} = \frac 1 N \sum_{k = 0}^{N - 1} X[k] \left(\cos(2 \pi (k / N) n) + j \sin(2 \pi (k / N) n) \right)$$}}. One can see the formula is {{almost the same as DFT}}, except that {{a factor of $1 / N$ is added, the input and output sequences are swapped, and the sign of the exponent is negated}}.

The above formulas are {{the most conventional way of writing them}}. The only requirements for the formula of DFT and IDFT are that {{the sign of the exponent is opposite (convention: $-$ for DFT, $+$ for IDFT) and the product of the two multiplication factors is $1 / N$ (convention: $1$ for DFT, $1 / N$ for IDFT)}}.

## properties

The original sequence is {{treated as $N$-periodic}} by DFT. The transformed sequence is {{also $N$-periodic}}. Likewise, the DFT-transformed sequence is {{treated as $N$-periodic}} by IDFT. The recovered original sequence is {{also $N$-periodic}}.

Note that the formulas for DFT and IDFT are extremely similar. Indeed, one can {{write the IDFT in terms of the DFT}}.

## interpretation

Usually, the original sequence is {{in the time domain, i.e. it represents the (complex) amplitude as a function of time}}. Then, the transformed sequence is {{in the frequency domain, i.e. it represents the (complex) amplitude as a function of frequency}}. The $k$-th value of the transformed sequence represents a frequency of {{$k / TN$ or $k f_s / N$}}. That is, each value of the transformed value is separated by {{$1 / TN$ (the reciprocal of the duration of the input sequence) or $f_s / N$ (the ratio of sampling frequency over the number of sequences)}}.

Each element $x[n]$ in the original sequence represents {{the (complex) amplitude at time $nT$}}. Likewise, each element $X[k]$ in the transformed sequence represents {{the (complex) amplitude of the complex sinusoidal component $\left(e^{-j 2\pi (k / N) n} \right)$ of cycle frequency $k / N$ ($k$ cycles of the original sequence per $N$ sample, the _actual_ frequency is $k / TN^2$ or $k f_s / N^2$) in the original sequence}}. This also shows a $N$-periodic discrete signal can always be represented by {{the sum of $N$ complex sinusoidal components via DFT}}.

### components

DFT can also be treated as {{a dot (scalar) product of the original sequence and a complex sinusoidal of various frequency}}: {{$$\begin{aligned} s_k[n] & := e^{j 2\pi (k / N) n} = \left(e^{-j 2\pi (k / N) n} \right)^* \\ X[k] & := \sum_{k = 0}^{N - 1} x[n] \cdot e^{-j 2\pi (k / N) n} = \sum_{k = 0}^{N - 1} x[n] \cdot s_k^*[n] = \langle x, s_k \rangle \end{aligned}$$}}. This shows DFT can {{extract the complex sinusoidal component of cycle frequency $k / N$ from the original signal}}. Likewise, IDFT can also be treated as {{a dot (scalar) product of the transformed sequence and a complex sinusoidal (in the frequency domain) of cycle frequency $-k / N$}}.

To see why DFT can extract complex sinusoidal components from any signal, consider {{applying DFT on a complex sinusoidal}}. The complex sinusoidal of cycle frequency $k_0 / N$ is defined as: {{$$s_{k_0}[n] := e^{j 2\pi (k_0 / N) n} \qquad n = 0, \ldots, N - 1$$}}. Applying DFT: {{$$\begin{aligned} S_{k_0}[k] & := \sum_{n = 0}^{N - 1} s_{k_0}[n] \cdot e^{-j 2\pi (k / N) n} \\ & = \sum_{n = 0}^{N - 1} e^{j 2\pi (k_0 / N) n} \cdot e^{-j 2\pi (k / N) n} \\ & = \sum_{n = 0}^{N - 1} e^{j 2\pi ((k_0 - k) / N) n} \\ & = \frac {1 - e^{j 2\pi (k_0 - k)} } {1 - e^{j 2\pi ((k_0 - k) / N)} } && (\text{sum of geometric sequence when }k_0 \equiv k \pmod N) \end{aligned}$$}}. When {{$k_0 \not\equiv k \pmod N$}}, then the numerator is {{zero, nothing that $k_0 - k$ is an nonzero integer, so $e^{j 2\pi (k_0 - k)} = 1$}}. The denominator is {{nonzero, as $k_0 - k$ is not evenly divided by $N$, thus $e^{j 2\pi (k_0 - k)} \ne 1$}}. Finally {{$S_{k_0}[k] = 0$}}. When {{$k_0 \equiv k \pmod N$ (i.e. the difference is evenly divided by $N$)}}, {{the sum of geometric sequence cannot be applied and we need to go back up one step}}. This is because {{now both the numerator and denominator are both zero}}, caused by that {{the sum sequence is no longer a geometric sequence but a constant sequence instead}}. In this case, it is {{obvious that the each term of the sum in that previous step is $1$}}, so {{$S_{k_0}[k_0 + Nx] = N \quad x \in \mathbb Z$}}. This also explains why {{the transformed sequence is $N$-periodic}}. When the complex sinusoidal {{has an (complex) amplitude of $A$}}, then {{the resulting value is also multiplied by $A$, i.e. $S_{k_0}[k_0 + Nx] = AN \quad x \in \mathbb Z$}}. Likewise, IDFT have properties analogous to above. An important difference is {{the resulting value becomes $s_{n_0}[-n_0 + Nx] = A \quad x \in \mathbb Z$ instead}}.

Another property of DFT is that {{it is linear}}. That is, {{adding multiple signals together and applying DFT yields the same result as applying DFT on multiple signals individually and then adding the DFTs}}. (This can be proved easily and left as an exercise.) With the above two properties, one can see {{the sum of multiple complex sinusoidal can be extracted using DFT}}. Finally, one more thing to know (given here and not proven here) is that {{any (discrete complex) signal of length $N$ can be exactly decomposed into $N$ complex sinusoidal}}. So this is why DFT can extract complex sinusoidal from any (discrete complex) signal. For IDFT, {{the same applies}}.

For {{real sinusoidal}}, it is also easy to derive their DFT as {{they can be written as a sum of 2 complex sinusoidal with opposing frequencies}}. For example, {{a real cosine wave of cycle frequency $k_0 / N$: $$\cos_{k_0}[n] := A \cos(2\pi (k_0 / N) n) \qquad n = 0, \ldots, N - 1$$}} can be written as {{the weighted sum of 2 complex sinusoidal with cycle frequency $k_0 / N$ and $-k_0 / N$: $$\cos_{k_0}[n] = A \cos(2\pi (k_0 / N) n) = \frac {A e^{j 2\pi (k_0 / N) n} } 2 + \frac {A e^{-j 2\pi (k_0 / N) n} } 2$$}}. By linearity, the nonzero DFT values are {{$$\begin{aligned} \operatorname{Cos}_{k_0}[k_0] & = \frac {AN} 2 \\ \operatorname{Cos}_{k_0}[-k_0] = \operatorname{Cos}_{k_0}[N - k_0] & = \frac {AN} 2 \end{aligned}$$}}. For {{a real sine wave of cycle frequency $k_0 / N$: $$\sin_{k_0}[n] := A \sin(2 \pi (k_0 / N) n) \qquad n = 0, \ldots, N - 1$$}}, it can also be expressed as {{the weighted sum of 2 complex sinusoidal with cycle frequency $k_0 / N$ and $-k_0 / N$: $$\sin_{k_0}[n] := A \sin(2 \pi (k_0 / N) n) = \frac {A e^{j 2\pi (k_0 / N) n} } {2j} - \frac {A e^{-j 2\pi (k_0 / N) n} } {2j}$$}}. By linearity, the nonzero DFT values are {{$$\begin{aligned} \operatorname{Sin}_{k_0}[k_0] & = \frac {AN} {2j} = -j \frac {AN} 2 \\ \operatorname{Sin}_{k_0}[-k_0] = \operatorname{Sin}_{k_0}[N - k_0] & = -\frac {AN} {2j} = j \frac {AN} 2 \end{aligned}$$}}. For IDFT, {{the same applies}}, except that {{the nonzero IDFT values are divided by $N$ (no $N$ in the resulting values), and for a real sine wave (in the frequency domain), have their signs reversed}}.

Note that if {{you try to use Python to perform the above proofs}}, you may {{find that the DFT is nonzero at more than 2 points}}. A common mistake that causes the above is that {{$k_0$ is not an integer}}. However, even if the common mistake is fixed, {{there may still be very tiny nonzero values apart from those 2 points}}. This is because {{decimal numbers in Python are represented by floating points, which cannot represent the decimal numbers exactly, which is called quantization error}}. This is {{not fixable, unfortunately}}.

## spectrums

{{The magnitude spectrum}} is {{the transformed signal under the modulus operation $\lvert X \rvert$ (length of the complex amplitude)}}. For easier visualization, the magnitude may be {{in logarithm scale}}. The magnitude, intuitively, represents {{the loudness of the complex sinusoidal of a given frequency}}.

{{The phase spectrum}} is {{the transformed signal under the argument operation $\operatorname{arg}(X)$ (angle of the complex amplitude)}}. To make the phase spectrum {{less jumpy (more continuous)}}, the phase may be {{wrapped around $2\pi$ such that the difference from the previous phase is not more than $\pi$ (see [`np.unwrap`](https://numpy.org/doc/stable/reference/generated/numpy.unwrap.html))}}. The phase, intuitively, represents {{the time offset of the complex sinusoidal of a given frequency}}.
