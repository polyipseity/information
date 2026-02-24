---
aliases:
  - Cooley–Tukey FFT algorithm
  - Cooley–Tukey FFT algorithms
  - Cooley–Tukey algorithm
  - Cooley–Tukey algorithms
tags:
  - flashcard/active/general/eng/Cooley-Tukey_FFT_algorithm
  - language/in/English
---

# Cooley–Tukey FFT algorithm

{@{The __Cooley–Tukey algorithm__}@}, named after {@{[J. W. Cooley](James%20Cooley.md) and [John Tukey](John%20Tukey.md)}@}, is {@{the most common [fast Fourier transform](fast%20Fourier%20transform.md) \(FFT\) algorithm}@}. It re-expresses {@{the [discrete Fourier transform](discrete%20Fourier%20transform.md) \(DFT\) of an arbitrary [composite](composite%20number.md) size $N=N_{1}N_{2}$}@} in terms of {@{_N_<sub>1</sub> smaller DFTs of sizes _N_<sub>2</sub>, [recursively](recursion.md)}@}, to reduce {@{the computation time to O\(_N_ log _N_\) for highly composite _N_ \([smooth numbers](smooth%20number.md)\)}@}. Because of {@{the algorithm's importance}@}, {@{specific variants and implementation styles}@} have become {@{known by their own names}@}, as described below. <!--SR:!2026-11-21,292,330!2026-11-16,287,330!2026-10-14,269,330!2026-10-06,263,330!2026-11-16,290,330!2026-10-28,276,330!2026-10-27,270,330!2026-09-26,254,330!2026-09-03,235,330-->

Because the Cooley–Tukey algorithm breaks {@{the DFT into smaller DFTs}@}, it can be combined {@{arbitrarily with any other algorithm for the DFT}@}. For example, {@{[Rader's](Rader's%20FFT%20algorithm.md) or [Bluestein's](Bluestein's%20FFT%20algorithm.md#Bluestein's%20algorithm) algorithm}@} can be used to handle {@{large prime factors that cannot be decomposed by Cooley–Tukey}@}, or {@{the [prime-factor algorithm](Prime-factor%20FFT%20algorithm.md)}@} can be exploited for {@{greater efficiency in separating out [relatively prime](relatively%20prime.md) factors}@}. <!--SR:!2026-10-22,270,330!2026-10-27,270,330!2026-11-10,281,330!2026-11-19,290,330!2026-09-24,252,330!2026-10-06,263,330-->

{@{The algorithm, along with its recursive application}@}, was invented by {@{[Carl Friedrich Gauss](Carl%20Friedrich%20Gauss.md)}@}. Cooley and Tukey {@{independently rediscovered and popularized it 160 years later}@}. <!--SR:!2026-10-04,261,330!2026-10-22,270,330!2026-10-21,269,330-->

## history

This algorithm, including its recursive application, was invented around 1805 by [Carl Friedrich Gauss](Carl%20Friedrich%20Gauss.md), who used it to interpolate the trajectories of the [asteroids](asteroid.md) [Pallas](2%20Pallas.md) and [Juno](3%20Juno.md), but his work was not widely recognized \(being published only posthumously and in [Neo-Latin](Neo-Latin.md)\).<sup>[\[1\]](#^ref-1)</sup><sup>[\[2\]](#^ref-2)</sup> Gauss did not analyze the asymptotic computational time, however. Various limited forms were also rediscovered several times throughout the 19th and early 20th centuries.<sup>[\[2\]](#^ref-2)</sup> FFTs became popular after [James Cooley](James%20Cooley.md) of [IBM](International%20Business%20Machines.md) and [John Tukey](John%20Tukey.md) of [Princeton](Princeton%20University.md) published a paper in 1965 reinventing<sup>[\[2\]](#^ref-2)</sup> the algorithm and describing how to perform it conveniently on a computer.<sup>[\[3\]](#^ref-3)</sup>

Tukey reportedly came up with the idea during a meeting of President Kennedy's Science Advisory Committee discussing ways to detect [nuclear-weapon tests](nuclear%20testing.md) in the [Soviet Union](Soviet%20Union.md) by employing seismometers located outside the country. These sensors would generate seismological [time series](time%20series.md). However, analysis of this data would require fast algorithms for computing DFTs due to the number of sensors and length of time. This task was critical for the ratification of the proposed nuclear test ban so that any violations could be detected without need to visit Soviet facilities.<sup>[\[4\]](#^ref-4)</sup><sup>[\[5\]](#^ref-5)</sup> Another participant at that meeting, [Richard Garwin](Richard%20Garwin.md) of IBM, recognized the potential of the method and put Tukey in touch with Cooley. However, Garwin made sure that Cooley did not know the original purpose. Instead, Cooley was told that this was needed to determine periodicities of the spin orientations in a 3-D crystal of [helium-3](helium-3.md). Cooley and Tukey subsequently published their joint paper, and wide adoption quickly followed due to the simultaneous development of [Analog-to-digital converters](analog-to-digital%20converter.md) capable of sampling at rates up to 300 [kHz](hertz.md).

The fact that Gauss had described the same algorithm \(albeit without analyzing its asymptotic cost\) was not realized until several years after Cooley and Tukey's 1965 paper.<sup>[\[2\]](#^ref-2)</sup> Their paper cited as inspiration only the work by [I. J. Good](I.%20J.%20Good.md) on what is now called the [prime-factor FFT algorithm](Prime-factor%20FFT%20algorithm.md) \(PFA\);<sup>[\[3\]](#^ref-3)</sup> although Good's algorithm was initially thought to be equivalent to the Cooley–Tukey algorithm, it was quickly realized that PFA is a quite different algorithm \(working only for sizes that have [relatively prime](relatively%20prime.md) factors and relying on the [Chinese remainder theorem](chinese%20remainder%20theorem.md), unlike the support for any composite size in Cooley–Tukey\).<sup>[\[6\]](#^ref-6)</sup>

## the radix-2 DIT case

{@{A __radix-2__ decimation-in-time \(__DIT__\) FFT}@} is {@{the simplest and most common form of the Cooley–Tukey algorithm}@}, although {@{highly optimized Cooley–Tukey implementations}@} typically use {@{other forms of the algorithm}@} as described below. {@{Radix-2 DIT}@} divides {@{a DFT of size _N_}@} into {@{two interleaved DFTs \(hence the name "radix-2"\) of size _N_<!-- markdown separator -->/2}@} with {@{each recursive stage}@}. <!--SR:!2026-11-02,276,330!2026-11-03,274,330!2026-09-21,249,330!2026-11-10,281,330!2026-11-14,285,330!2026-11-05,276,330!2026-11-11,282,330!2026-11-20,294,330-->

{@{The discrete Fourier transform \(DFT\)}@} is defined by the formula: {@{$$X_{k}=\sum _{n=0}^{N-1}x_{n}e^{-{\frac {2\pi i}{N} }nk},$$}@} where $n$ is {@{an [integer](integer.md) ranging from 0 to $N-1$}@}. <!--SR:!2026-10-24,272,330!2026-11-10,281,330!2026-10-30,273,330-->

{@{Radix-2 DIT}@} first computes {@{the DFTs of the even-indexed inputs $(x_{2m}=x_{0},x_{2},\ldots ,x_{N-2})$}@} and of {@{the odd-indexed inputs $(x_{2m+1}=x_{1},x_{3},\ldots ,x_{N-1})$}@}, and then combines {@{those two results to produce the DFT of the whole sequence}@}. This idea can then be {@{performed [recursively](recursion.md)}@} to reduce {@{the overall runtime to O\(_N_ log _N_\)}@}. {@{This simplified form}@} assumes that _N_ is {@{a [power of two](power%20of%20two.md)}@}; since {@{the number of sample points _N_}@} can usually be {@{chosen freely by the application}@} \(e.g. by changing {@{the sample rate or window, zero-padding, etcetera}@}\), this is often {@{not an important restriction}@}. <!--SR:!2026-11-13,284,330!2026-10-23,271,330!2026-10-27,267,330!2026-11-17,291,330!2026-11-01,272,330!2026-10-30,270,330!2026-10-24,273,330!2026-11-20,291,330!2026-11-05,276,330!2026-10-07,263,330!2026-09-13,241,330!2026-11-05,276,330-->

{@{The radix-2 DIT algorithm}@} rearranges {@{the DFT of the function $x_{n}$ into two parts}@}: a sum over {@{the even-numbered indices $n={2m}$}@} and {@{a sum over the odd-numbered indices $n={2m+1}$}@}: {@{$$X_{k}=\sum _{m=0}^{N/2-1}x_{2m}e^{-{\frac {2\pi i}{N} }(2m)k}+\sum _{m=0}^{N/2-1}x_{2m+1}e^{-{\frac {2\pi i}{N} }(2m+1)k}$$}@} <!--SR:!2026-11-17,288,330!2026-09-20,248,330!2026-11-02,273,330!2026-11-10,281,330!2026-08-10,197,310-->

One can factor {@{a common multiplier $e^{-{\frac {2\pi i}{N} }k}$ out of the second sum}@}, as shown in the equation below. It is then clear that {@{the two sums}@} are {@{the DFT of the even-indexed part $x_{2m}$ and the DFT of odd-indexed part $x_{2m+1}$}@} of the function $x_{n}$. Denote {@{the DFT of the ___E___<!-- markdown separator -->ven-indexed inputs $x_{2m}$}@} by $E_{k}$ and {@{the DFT of the odd-indexed inputs $x_{2m+1}$}@} by $O_{k}$ and we obtain: {@{$$X_{k}=\underbrace {\sum \limits _{m=0}^{N/2-1}x_{2m}e^{-{\frac {2\pi i}{N/2} }mk} } _{ {\text{DFT of even-indexed part of } }x_{n} }{}+e^{-{\frac {2\pi i}{N} }k}\underbrace {\sum \limits _{m=0}^{N/2-1}x_{2m+1}e^{-{\frac {2\pi i}{N/2} }mk} } _{ {\text{DFT of odd-indexed part of } }x_{n} }=E_{k}+e^{-{\frac {2\pi i}{N} }k}O_{k}\qquad {\text{ for } }k=0,\dots ,{\frac {N}{2} }-1.$$}@} <!--SR:!2026-09-04,236,330!2026-09-28,256,330!2026-11-12,292,330!2026-11-15,289,330!2026-11-18,289,330!2026-10-26,266,330-->

Note that {@{the equalities hold for $n=0,\dots ,N-1$}@}, but {@{the crux}@} is that {@{$E_{k}$ and $O_{k}$}@} are calculated {@{in this way for $n=0,\dots ,{\frac {N}{2} }-1$ only}@}. Thanks to {@{the [periodicity of the complex exponential](list%20of%20trigonometric%20identities.md#shifts%20and%20periodicity)}@}, {@{$X_{k+{\frac {N}{2} } }$}@} is also {@{obtained from $E_{k}$ and $O_{k}$}@}: {@{$${\begin{aligned}X_{k+{\frac {N}{2} } }&=\sum \limits _{m=0}^{N/2-1}x_{2m}e^{-{\frac {2\pi i}{N/2} }m(k+{\frac {N}{2} })}+e^{-{\frac {2\pi i}{N} }(k+{\frac {N}{2} })}\sum _{m=0}^{N/2-1}x_{2m+1}e^{-{\frac {2\pi i}{N/2} }m(k+{\frac {N}{2} })}\\&=\sum _{m=0}^{N/2-1}x_{2m}e^{-{\frac {2\pi i}{N/2} }mk}e^{-2\pi mi}+e^{-{\frac {2\pi i}{N} }k}e^{-\pi i}\sum _{m=0}^{N/2-1}x_{2m+1}e^{-{\frac {2\pi i}{N/2} }mk}e^{-2\pi mi}\\&=\sum _{m=0}^{N/2-1}x_{2m}e^{-{\frac {2\pi i}{N/2} }mk}-e^{-{\frac {2\pi i}{N} }k}\sum _{m=0}^{N/2-1}x_{2m+1}e^{-{\frac {2\pi i}{N/2} }mk}\\&=E_{k}-e^{-{\frac {2\pi i}{N} }k}O_{k}\end{aligned} }$$}@} <!--SR:!2026-11-05,276,330!2026-10-26,266,330!2026-10-28,271,330!2026-08-04,192,310!2026-11-03,282,330!2026-10-09,265,330!2026-11-23,294,330!2026-08-11,193,310-->

We can rewrite {@{$X_{k}$ and $X_{k+{\frac {N}{2} } }$}@} as: {@{$${\begin{aligned}X_{k}&=E_{k}+e^{-{\frac {2\pi i}{N} }{k} }O_{k}\\X_{k+{\frac {N}{2} } }&=E_{k}-e^{-{\frac {2\pi i}{N} }{k} }O_{k}\end{aligned} }$$}@} This result, expressing {@{the DFT of length _N_ recursively in terms of two DFTs of size _N_<!-- markdown separator -->/2}@}, is the core of {@{the radix-2 DIT fast Fourier transform}@}. The algorithm {@{gains its speed}@} by re-using {@{the results of intermediate computations to compute multiple DFT outputs}@}. Note that {@{final outputs are obtained}@} by {@{a +/− combination of $E_{k}$ and $O_{k}\exp(-2\pi ik/N)$}@}, which is simply {@{a size-2 DFT \(sometimes called a [butterfly](butterfly%20diagram.md) in this context\)}@}; when this is {@{generalized to larger radices below}@}, {@{the size-2 DFT}@} is replaced by {@{a larger DFT \(which itself can be evaluated with an FFT\)}@}. <!--SR:!2026-11-14,293,330!2026-10-25,265,330!2026-11-03,274,330!2026-10-26,275,330!2026-08-27,228,330!2026-11-03,274,330!2026-09-29,257,330!2026-11-08,280,330!2026-10-28,271,330!2026-11-03,274,330!2026-10-22,271,330!2026-11-17,288,330-->

> {@{![Data flow diagram for _N_=8: a decimation-in-time radix-2 FFT breaks a length-_N_ DFT into two length-_N_<!-- markdown separator -->/2 DFTs followed by a combining stage consisting of _N_<!-- markdown separator -->/2 size-2 DFTs called "butterfly" operations \(so called because of the shape of the data-flow diagrams\).](../../archives/Wikimedia%20Commons/DIT-FFT-butterfly.svg)}@}
>
> {@{Data flow diagram}@} for {@{_N_=8}@}: {@{a decimation-in-time radix-2 FFT}@} breaks {@{a length-_N_ DFT into two length-_N_<!-- markdown separator -->/2 DFTs}@} followed by {@{a combining stage consisting of _N_<!-- markdown separator -->/2 size-2 DFTs}@} called {@{"butterfly" operations}@} \(so called because of {@{the shape of the data-flow diagrams}@}\). <!--SR:!2026-10-27,276,330!2026-11-01,272,330!2026-11-08,279,330!2026-10-11,267,330!2026-10-23,266,330!2026-10-26,269,330!2026-11-09,288,330!2026-11-14,285,330-->

This process is an example of {@{the general technique of [divide and conquer algorithms](divide%20and%20conquer%20algorithm.md)}@}; in {@{many conventional implementations}@}, however, {@{the explicit recursion}@} is avoided, and instead one traverses {@{the computational tree in [breadth-first](breadth-first%20search.md) fashion}@}. <!--SR:!2026-11-08,279,330!2026-11-14,285,330!2026-11-01,275,330!2026-10-28,268,330-->

The above re-expression of {@{a size-_N_ DFT as two size-_N_<!-- markdown separator -->/2 DFTs}@} is sometimes called {@{the __[Danielson](G.%20C.%20Danielson.md)–[Lanczos](Cornelius%20Lanczos.md)__ [lemma](lemma%20(mathematics).md)}@}, since {@{the identity was noted by those two authors in 1942}@}<sup>[\[7\]](#^ref-7)</sup> \(influenced by {@{[Runge's](Carl%20David%20Tolmé%20Runge.md) 1903 work}@}<sup>[\[2\]](#^ref-2)</sup>\). They applied {@{their lemma in a "backwards" recursive fashion}@}, repeatedly {@{_doubling_ the DFT size until the transform spectrum converged}@} \(although they apparently didn't realize {@{the [linearithmic](linearithmic.md#quasilinear%20time) \[i.e., order _N_ log _N_\] asymptotic complexity they had achieved}@}\). {@{The Danielson–Lanczos work}@} predated {@{widespread availability of [mechanical or electronic computers](history%20of%20computing%20hardware.md)}@} and required {@{[manual calculation](human%20computer.md) \(possibly with mechanical aids such as [adding machines](adding%20machine.md)\)}@}; they reported {@{a computation time of 140 minutes}@} for {@{a size-64 DFT operating on [real inputs](fast%20Fourier%20transform.md#FFT%20algorithms%20specialized%20for%20real%20or%20symmetric%20data) to 3–5 significant digits}@}. {@{Cooley and Tukey's 1965 paper}@} reported {@{a running time of 0.02 minutes}@} for {@{a size-2048 complex DFT on an [IBM 7094](IBM%207094.md#IBM%207094)}@} \(probably in {@{36-bit [single precision](floating%20point.md), ~8 digits}@}\).<sup>[\[3\]](#^ref-3)</sup> {@{Rescaling the time}@} by {@{the number of operations}@}, this corresponds roughly to {@{a speedup factor of around 800,000}@}. \(To put {@{the time for the hand calculation}@} in perspective, {@{140 minutes for size 64}@} corresponds to an average of {@{at most 16 seconds per floating-point operation}@}, around {@{20% of which are multiplications}@}.\) <!--SR:!2026-11-04,276,330!2026-10-27,275,330!2026-11-02,281,330!2026-10-03,260,330!2026-10-10,266,330!2026-09-15,243,330!2026-11-08,279,330!2026-11-05,276,330!2026-09-18,246,330!2026-11-12,283,330!2026-11-14,285,330!2026-10-25,273,330!2026-11-12,283,330!2026-11-05,276,330!2026-11-15,286,330!2026-10-06,263,330!2026-10-28,268,330!2026-10-30,273,330!2026-11-13,284,330!2026-09-28,256,330!2026-10-07,263,330!2026-11-06,280,330!2026-11-02,273,330-->

### pseudocode

In {@{[pseudocode](pseudocode.md)}@}, {@{the below procedure}@} could be written:<sup>[\[8\]](#^ref-8)</sup> <!--SR:!2026-11-20,291,330!2026-10-21,269,330-->

<pre>
<i>X</i><sub>0,...,<i>N</i>−1</sub> ← <b>ditfft2</b>(<i>x</i>, <i>N</i>, <i>s</i>):             <i>DFT of (x</i><sub>0</sub>, <i>x<sub>s</sub></i>, <i>x</i><sub>2<i>s</i></sub>, ..., <i>x</i><sub>(<i>N</i>-1)<i>s</i></sub>):
    <b>if</b> <i>N</i> = 1 <b>then</b>
        <i>X</i><sub>0</sub> ← <i>x</i><sub>0</sub>                                     <i>trivial size-1 DFT base case</i>
    <b>else</b>
        <i>X</i><sub>0,...,<i>N</i>/2−1</sub> ← <b>ditfft2</b>(<i>x</i>, <i>N</i>/2, 2<i>s</i>)             <i>DFT of (x</i><sub>0</sub>, <i>x</i><sub>2<i>s</i></sub>, <i>x</i><sub>4<i>s</i></sub>, ..., <i>x</i><sub>(<i>N</i>-2)<i>s</i></sub>)
        <i>X<sub>N</sub></i><sub>/2,...,<i>N</i>−1</sub> ← <b>ditfft2</b>(<i>x</i>+s, <i>N</i>/2, 2<i>s</i>)           <i>DFT of (x<sub>s</sub></i>, <i>x<sub>s</sub></i><sub>+2<i>s</i></sub>, <i>x<sub>s</sub></i><sub>+4<i>s</i></sub>, ..., <i>x</i><sub>(<i>N</i>-1)<i>s</i></sub>)
        <b>for</b> k = 0 to (N/2)-1 <b>do</b>                      <i>combine DFTs of two halves:</i>
            p ← <i>X<sub>k</sub></i>
            q ← exp(−2π<i>i</i>/<i>N</i> <i>k</i>) <i>X<sub>k</sub></i><sub>+<i>N</i>/2</sub>
            <i>X<sub>k</sub></i> ← p + q
            <i>X<sub>k</sub></i><sub>+<i>N</i>/2</sub> ← p − q
        <b>end for</b>
    <b>end if</b>
</pre>

> [!info]- code
>
> ```pseudocode
> X0,...,N−1 ← ditfft2(x, N, s):             DFT of (x0, xs, x2s, ..., x(N-1)s):
>     if N = 1 then
>         X0 ← x0                                     trivial size-1 DFT base case
>     else
>         X0,...,N/2−1 ← ditfft2(x, N/2, 2s)             DFT of (x0, x2s, x4s, ..., x(N-2)s)
>         XN/2,...,N−1 ← ditfft2(x+s, N/2, 2s)           DFT of (xs, xs+2s, xs+4s, ..., x(N-1)s)
>         for k = 0 to (N/2)-1 do                      combine DFTs of two halves:
>             p ← Xk
>             q ← exp(−2πi/N k) Xk+N/2
>             Xk ← p + q
>             Xk+N/2 ← p − q
>         end for
>     end if
> ```

<!-- markdownlint MD028 -->

> __code flashcards__
>
> <pre>
> {@{<i>X</i><sub>0,...,<i>N</i>−1</sub>}@} ← {@{<b>ditfft2</b>(<i>x</i>, <i>N</i>, <i>s</i>)}@}:             {@{<i>DFT of (x</i><sub>0</sub>, <i>x<sub>s</sub></i>, <i>x</i><sub>2<i>s</i></sub>, ..., <i>x</i><sub>(<i>N</i>-1)<i>s</i></sub>):}@}
>     {@{<b>if</b> <i>N</i> = 1}@} <b>then</b>
>         {@{<i>X</i><sub>0</sub> ← <i>x</i><sub>0</sub>}@}                                     {@{<i>trivial size-1 DFT base case</i>}@}
>     <b>else</b>
>         {@{<i>X</i><sub>0,...,<i>N</i>/2−1</sub>}@} ← {@{<b>ditfft2</b>(<i>x</i>, <i>N</i>/2, 2<i>s</i>)}@}             {@{<i>DFT of (x</i><sub>0</sub>, <i>x</i><sub>2<i>s</i></sub>, <i>x</i><sub>4<i>s</i></sub>, ..., <i>x</i><sub>(<i>N</i>-2)<i>s</i></sub>)}@}
>         {@{<i>X<sub>N</sub></i><sub>/2,...,<i>N</i>−1</sub>}@} ← {@{<b>ditfft2</b>(<i>x</i>+s, <i>N</i>/2, 2<i>s</i>)}@}           {@{<i>DFT of (x<sub>s</sub></i>, <i>x<sub>s</sub></i><sub>+2<i>s</i></sub>, <i>x<sub>s</sub></i><sub>+4<i>s</i></sub>, ..., <i>x</i><sub>(<i>N</i>-1)<i>s</i></sub>)}@}
>         {@{<b>for</b> k = 0 to (N/2)-1}@} <b>do</b>                      {@{<i>combine DFTs of two halves:</i>}@}
>             p ← {@{<i>X<sub>k</sub></i>}@}
>             q ← {@{exp(−2π<i>i</i>/<i>N</i> <i>k</i>) <i>X<sub>k</sub></i><sub>+<i>N</i>/2</sub>}@}
>             {@{<i>X<sub>k</sub></i> ← p + q}@}
>             {@{<i>X<sub>k</sub></i><sub>+<i>N</i>/2</sub> ← p − q}@}
>         <b>end for</b>
>     <b>end if</b>
> </pre> <!--SR:!2026-11-04,283,330!2026-10-08,264,330!2026-11-10,284,330!2026-10-31,271,330!2026-11-04,275,330!2026-08-15,194,310!2026-11-19,290,330!2026-11-19,290,330!2026-11-04,278,330!2026-08-05,192,310!2026-10-24,264,330!2026-08-22,201,310!2026-10-29,272,330!2026-11-02,282,330!2026-10-29,269,330!2026-08-09,191,310!2026-10-28,276,330!2026-04-02,104,290-->

Here, {@{__`ditfft2`__\(_x_,_N_,1\)}@}, computes {@{_X_=DFT\(_x_\) [out-of-place](in-place%20algorithm.md) by a radix-2 DIT FFT}@}, where _N_ is {@{an integer power of 2}@} and _s_=1 is {@{the [stride](stride%20of%20an%20array.md) of the input _x_ [array](array%20data%20structure.md)}@}. {@{_x_+_s_}@} denotes {@{the array starting with _x<sub>s</sub>_}@}. <!--SR:!2026-10-12,268,330!2026-11-13,287,330!2026-10-16,271,330!2026-10-25,265,330!2026-10-27,267,330!2026-10-31,271,330-->

\(The results are in {@{the correct order in _X_}@} and no further {@{[bit-reversal permutation](bit-reversal%20permutation.md) is required}@}; the often-mentioned {@{necessity of a separate bit-reversal stage}@} only arises for {@{certain in-place algorithms}@}, as described below.\) <!--SR:!2026-10-10,266,330!2026-08-28,229,330!2026-11-04,275,330!2026-11-09,280,330-->

{@{High-performance FFT implementations}@} make {@{many modifications to the implementation}@} of such an algorithm compared to {@{this simple pseudocode}@}. For example, one can use {@{a larger base case than _N_=1}@} to amortize {@{the overhead of recursion}@}, {@{the [twiddle factors](twiddle%20factor.md) $\exp[-2\pi ik/N]$}@} can be {@{precomputed}@}, and {@{larger radices}@} are often used for {@{[cache](cache%20(computing).md) reasons}@}; {@{these and other optimizations together}@} can improve {@{the performance by an order of magnitude or more}@}.<sup>[\[8\]](#^ref-8)</sup> \(In many textbook implementations {@{the [depth-first](depth-first.md) recursion}@} is {@{eliminated in favor of a nonrecursive [breadth-first](breadth-first.md) approach}@}, although {@{depth-first recursion}@} has been argued to have {@{better [memory locality](memory%20locality.md)}@}.<sup>[\[8\]](#^ref-8)</sup><sup>[\[9\]](#^ref-9)</sup>\) {@{Several of these ideas}@} are described in further detail below. <!--SR:!2026-09-28,256,330!2026-11-23,294,330!2026-11-04,275,330!2026-10-27,275,330!2026-10-29,269,330!2026-11-03,275,330!2026-11-04,275,330!2026-11-01,272,330!2026-10-28,276,330!2026-11-20,292,330!2026-11-10,281,330!2026-11-02,276,330!2026-11-06,285,330!2026-09-26,254,330!2026-10-08,264,330!2026-11-07,281,330-->

## idea

> {@{![The basic step of the Cooley–Tukey FFT for general factorizations can be viewed as re-interpreting a 1d DFT as something like a 2d DFT.](../../archives/Wikimedia%20Commons/Cooley-tukey-general.png)}@}
>
> {@{The basic step}@} of the Cooley–Tukey FFT for {@{general factorizations}@} can be viewed as re-interpreting {@{a 1d DFT as something like a 2d DFT}@}. {@{The 1d input array of length _N_ = _N_<sub>1</sub>_N_<sub>2</sub>}@} is reinterpreted as {@{a 2d _N_<sub>1</sub>×<!-- markdown separator -->_N_<sub>2</sub> matrix stored in [column-major order](column-major%20order.md)}@}. One performs {@{smaller 1d DFTs along the _N_<sub>2</sub> direction}@} \(the {@{non-contiguous}@} direction\), then multiplies by {@{phase factors \(twiddle factors\)}@}, and finally performs {@{1d DFTs along the _N_<sub>1</sub> direction}@}. {@{The transposition step}@} can be performed in {@{the middle, as shown here, or at the beginning or end}@}. This is done {@{recursively for the smaller transforms}@}. <!--SR:!2026-09-28,256,330!2026-11-13,284,330!2026-09-27,255,330!2026-10-29,269,330!2026-10-21,270,330!2026-09-11,243,330!2026-10-17,272,330!2026-09-03,235,330!2026-11-04,275,330!2026-11-06,280,330!2026-09-19,247,330!2026-10-26,266,330!2026-11-22,293,330-->

More generally, {@{Cooley–Tukey algorithms}@} recursively {@{re-express a DFT of a composite size _N_ = _N_<sub>1</sub>_N_<sub>2</sub>}@} as:<sup>[\[10\]](#^ref-10)</sup> <!--SR:!2026-09-23,251,330!2026-09-20,248,330-->

1. \(annotation: time domain\) ::@:: Perform _N_<sub>1</sub> DFTs of size _N_<sub>2</sub>. <!--SR:!2026-11-14,285,330!2026-10-30,273,330-->
2. \(annotation: twiddle\) ::@:: Multiply by complex [roots of unity](roots%20of%20unity.md) \(often called the [twiddle factors](twiddle%20factor.md)\). <!--SR:!2026-11-10,281,330!2026-10-24,264,330-->
3. \(annotation: frequency domain\) Perform _N_<sub>2</sub> DFTs of size _N_<sub>1</sub>.

Typically, {@{either _N_<sub>1</sub> or _N_<sub>2</sub>}@} is {@{a small factor \(_not_ necessarily prime\)}@}, called {@{the __radix__}@} \(which can {@{differ between stages of the recursion}@}\). If {@{_N_<sub>1</sub> is the radix}@}, it is called {@{a __decimation in time__ \(DIT\) algorithm}@}, whereas if {@{_N_<sub>2</sub> is the radix}@}, it is {@{__decimation in frequency__ \(DIF, also called the Sande–Tukey algorithm\)}@}. {@{The version presented above}@} was {@{a radix-2 DIT algorithm}@}; in {@{the final expression}@}, {@{the phase multiplying the odd transform}@} is {@{the twiddle factor}@}, and {@{the +/- combination \(_butterfly_\) of the even and odd transforms}@} is {@{a size-2 DFT}@}. \({@{The radix's small DFT}@} is sometimes known as {@{a [butterfly](butterfly%20(FFT%20algorithm).md)}@}, so-called because of {@{the shape of the [dataflow diagram](dataflow%20diagram.md) for the radix-2 case}@}.\) <!--SR:!2026-11-12,283,330!2026-11-10,281,330!2026-11-05,279,330!2026-11-10,281,330!2026-11-18,289,330!2026-10-15,270,330!2026-11-06,285,330!2026-11-16,287,330!2026-11-05,276,330!2026-11-23,294,330!2026-11-03,274,330!2026-10-27,275,330!2026-11-11,285,330!2026-11-10,284,330!2026-09-22,250,330!2026-10-25,274,330!2026-11-11,282,330!2026-11-05,284,330-->

## variations

There are {@{many other variations}@} on the Cooley–Tukey algorithm. {@{__Mixed-radix__ implementations}@} handle {@{composite sizes with a variety of \(typically small\) factors in addition to two}@}, usually \(but not always\) employing {@{the O\(_N_<sup>2</sup>\) algorithm for the prime base cases of the recursion}@} \(it is also possible to employ {@{an _N_ log _N_ algorithm for the prime base cases}@}, such as {@{[Rader](Rader's%20FFT%20algorithm.md)'s or [Bluestein](Bluestein's%20FFT%20algorithm.md#Bluestein's%20algorithm)'s algorithm}@}\). {@{[Split radix](Split-radix%20FFT%20algorithm.md)}@} merges {@{radices 2 and 4}@}, exploiting the fact {@{that the first transform of radix 2}@} requires {@{no twiddle factor}@}, in order to achieve what was {@{long the lowest known arithmetic operation count for power-of-two sizes}@},<sup>[\[10\]](#^ref-10)</sup> although {@{recent variations}@} achieve {@{an even lower count}@}.<sup>[\[11\]](#^ref-11)</sup><sup>[\[12\]](#^ref-12)</sup> \(On {@{present-day computers}@}, performance is determined {@{more by [cache](CPU%20cache.md) and [CPU pipeline](CPU%20pipeline.md) considerations}@} than by {@{strict operation counts}@}; {@{well-optimized FFT implementations}@} often employ {@{larger radices and/or hard-coded base-case transforms of significant size}@}.<sup>[\[13\]](#^ref-13)</sup>\). <!--SR:!2026-10-14,269,330!2026-11-02,276,330!2026-11-14,285,330!2026-10-08,264,330!2026-11-18,289,330!2026-09-30,258,330!2026-11-02,273,330!2026-11-13,284,330!2026-09-06,238,330!2026-11-02,281,330!2026-10-01,259,330!2026-11-02,273,330!2026-11-13,284,330!2026-09-19,247,330!2026-10-06,263,330!2026-11-01,275,330!2026-09-21,249,330!2026-08-26,227,330-->

Another way of {@{looking at the Cooley–Tukey algorithm}@} is that it re-expresses {@{a size _N_ one-dimensional DFT as an _N_<sub>1</sub> by _N_<sub>2</sub> two-dimensional DFT \(plus twiddles\)}@}, where {@{the output matrix is [transposed](transpose.md)}@}. {@{The net result of all of these transpositions}@}, for {@{a radix-2 algorithm}@}, corresponds to {@{a bit reversal of the input \(DIF\) or output \(DIT\) indices}@}. If, instead of using {@{a small radix}@}, one employs {@{a radix of roughly √_N_ and explicit input/output matrix transpositions}@}, it is called {@{a [four-step FFT](four-step%20FFT.md) algorithm}@} \(or {@{_six-step_, depending on the number of transpositions}@}\), initially proposed to {@{improve memory locality}@},<sup>[\[14\]](#^ref-14)</sup><sup>[\[15\]](#^ref-15)</sup> e.g. for {@{cache optimization or [out-of-core](out-of-core.md) operation}@}, and was later shown to be an {@{optimal [cache-oblivious algorithm](cache-oblivious%20algorithm.md)}@}.<sup>[\[16\]](#^ref-16)</sup> <!--SR:!2026-11-12,283,330!2026-10-15,270,330!2026-10-05,262,330!2026-11-10,290,330!2026-11-11,290,330!2026-11-03,274,330!2026-09-07,239,330!2026-11-11,290,330!2026-11-18,289,330!2026-11-09,280,330!2026-11-04,275,330!2026-10-20,268,330!2026-10-28,268,330-->

{@{The general Cooley–Tukey factorization}@} rewrites {@{the indices _k_ and _n_}@} as {@{$k=N_{2}k_{1}+k_{2}$ and $n=N_{1}n_{2}+n_{1}$, respectively}@}, where {@{the indices _k_<sub>a</sub> and _n_<sub>a</sub> run from 0.._N_<sub>a</sub>-1 \(for _a_ of 1 or 2\)}@}. That is, it re-indexes {@{the input \(_n_\) and output \(_k_\)}@} as {@{_N_<sub>1</sub> by _N_<sub>2</sub> two-dimensional arrays}@} in {@{[column-major](column-major%20order.md) and [row-major order](row-major%20order.md), respectively}@}; {@{the difference between these indexings}@} is {@{a transposition}@}, as mentioned above. When this re-indexing is substituted {@{into the DFT formula for _nk_}@}, {@{the $N_{1}n_{2}N_{2}k_{1}$ cross term vanishes}@} \({@{its exponential is unity}@}\), and {@{the remaining terms}@} give {@{$$X_{N_{2}k_{1}+k_{2} }=\sum _{n_{1}=0}^{N_{1}-1}\sum _{n_{2}=0}^{N_{2}-1}x_{N_{1}n_{2}+n_{1} }e^{-{\frac {2\pi i}{N_{1}N_{2} } }\cdot (N_{1}n_{2}+n_{1})\cdot (N_{2}k_{1}+k_{2})}$$}@} <br/> {@{$=\sum _{n_{1}=0}^{N_{1}-1}\left[e^{-{\frac {2\pi i}{N_{1}N_{2} } }n_{1}k_{2} }\right]\left(\sum _{n_{2}=0}^{N_{2}-1}x_{N_{1}n_{2}+n_{1} }e^{-{\frac {2\pi i}{N_{2} } }n_{2}k_{2} }\right)e^{-{\frac {2\pi i}{N_{1} } }n_{1}k_{1} }$}@} <br/> {@{$$=\sum _{n_{1}=0}^{N_{1}-1}\left(\sum _{n_{2}=0}^{N_{2}-1}x_{N_{1}n_{2}+n_{1} }e^{-{\frac {2\pi i}{N_{2} } }n_{2}k_{2} }\right)e^{-{\frac {2\pi i}{N_{1}N_{2} } }n_{1}(N_{2}k_{1}+k_{2})} \,.$$}@} where {@{each inner sum}@} is {@{a DFT of size _N_<sub>2</sub>}@}, {@{each outer sum}@} is {@{a DFT of size _N_<sub>1</sub>}@}, and {@{the \[...\] bracketed term}@} is {@{the twiddle factor}@}. <!--SR:!2026-10-06,263,330!2026-11-04,275,330!2026-11-11,285,330!2026-10-11,267,330!2026-08-04,191,310!2026-11-05,276,330!2026-09-25,253,330!2026-10-30,270,330!2026-10-30,270,330!2026-10-25,265,330!2026-08-20,199,310!2026-10-27,267,330!2026-09-26,254,330!2026-11-10,289,330!2026-05-06,115,290!2026-10-10,222,270!2026-10-13,268,330!2026-11-02,276,330!2026-05-19,150,310!2026-10-01,259,330!2026-09-30,258,330!2026-10-26,266,330-->

{@{An arbitrary radix _r_ \(as well as mixed radices\)}@} can be employed, as was shown by {@{both Cooley and Tukey<sup>[\[3\]](#^ref-3)</sup> as well as Gauss \(who gave examples of radix-3 and radix-6 steps\)}@}.<sup>[\[2\]](#^ref-2)</sup> {@{Cooley and Tukey originally assumed}@} that {@{the radix butterfly required O\(_r_<sup>2</sup>\) work}@} and hence reckoned {@{the complexity for a radix _r_}@} to be {@{$O\!\left(r^2 \frac N r \log_r N\right) = O\!\left(\frac {N \log_2(N) \,r} {\log_2 r} \right)$}@}; from calculation of {@{values of _r_<!-- markdown separator -->/log<sub>2</sub>_r_}@} for {@{integer values of _r_ from 2 to 12}@} {@{the optimal radix is found to be 3}@} \({@{the closest integer to _[e](e%20(mathematical%20constant).md)_}@}, which {@{minimizes _r_<!-- markdown separator -->/log<sub>2</sub>_r_}@}\).<sup>[\[3\]](#^ref-3)</sup><sup>[\[17\]](#^ref-17)</sup> This analysis was {@{erroneous, however}@}: {@{the radix-butterfly}@} is {@{also a DFT and can be performed via an FFT algorithm}@} in {@{O\(_r_ log _r_\) operations}@}, hence {@{the radix _r_}@} actually {@{cancels in the complexity $O\!\left(r \log(r) \frac N r \log_r N\right)$}@}, and {@{the optimal _r_}@} is determined by {@{more complicated considerations}@}. In practice, {@{quite large _r_ \(32 or 64\)}@} are important in order to effectively exploit {@{e.g. the large number of [processor registers](processor%20register.md) on modern processors}@},<sup>[\[13\]](#^ref-13)</sup> and even {@{an unbounded radix $r = \sqrt N$}@} also {@{achieves O\(_N_ log _N_\) complexity}@} and has {@{theoretical and practical advantages for large _N_ as mentioned above}@}.<sup>[\[14\]](#^ref-14)</sup><sup>[\[15\]](#^ref-15)</sup><sup>[\[16\]](#^ref-16)</sup> <!--SR:!2026-09-25,253,330!2026-10-31,271,330!2026-11-15,289,330!2026-11-15,289,330!2026-10-25,265,330!2026-09-05,237,330!2026-10-27,267,330!2026-11-01,275,330!2026-11-17,288,330!2026-11-01,272,330!2026-10-12,268,330!2026-11-09,280,330!2026-10-29,269,330!2026-10-31,271,330!2026-10-21,264,330!2026-10-25,268,330!2026-11-10,284,330!2026-10-29,272,330!2026-10-06,263,330!2026-10-31,279,330!2026-10-24,264,330!2026-11-16,287,330!2026-09-22,250,330!2026-11-23,294,330-->

## data reordering, bit reversal, and in-place algorithms

Although {@{the abstract Cooley–Tukey factorization}@} of the DFT, above, applies {@{in some form to all implementations of the algorithm}@}, {@{much greater diversity}@} exists in {@{the techniques for ordering and accessing the data at each stage of the FFT}@}. Of {@{special interest}@} is the problem of devising {@{an [in-place algorithm](in-place%20algorithm.md)}@} that overwrites {@{its input with its output data using only O\(1\) auxiliary storage}@}. <!--SR:!2026-10-31,271,330!2026-09-14,242,330!2026-11-19,293,330!2026-11-22,293,330!2026-10-17,272,330!2026-10-13,268,330!2026-11-11,282,330-->

{@{The best-known reordering technique}@} involves {@{explicit __bit reversal__ for in-place radix-2 algorithms}@}. {@{[Bit reversal](bit-reversal%20permutation.md)}@} is {@{the [permutation](permutation.md) where the data at an index _n_}@}, written in {@{[binary](binary%20numeral%20system.md) with digits _b_<sub>4</sub>_b_<sub>3</sub>_b_<sub>2</sub>_b_<sub>1</sub>_b_<sub>0</sub>}@} \(e.g. {@{5 digits for _N_=32 inputs}@}\), is transferred to {@{the index with reversed digits _b_<sub>0</sub>_b_<sub>1</sub>_b_<sub>2</sub>_b_<sub>3</sub>_b_<sub>4</sub>}@}. Consider {@{the last stage of a radix-2 DIT algorithm}@} like the one presented above, where the output is written {@{in-place over the input}@}: when {@{$E_{k}$ and $O_{k}$ are combined}@} with {@{a size-2 DFT}@}, {@{those two values}@} are {@{overwritten by the outputs}@}. However, {@{the two output values}@} should go in {@{the first and second _halves_ of the output array}@}, corresponding to {@{the _most_ significant bit _b_<sub>4</sub> \(for _N_=32\)}@}; whereas {@{the two inputs $E_{k}$ and $O_{k}$}@} are {@{interleaved in the even and odd elements}@}, corresponding to {@{the _least_ significant bit _b_<sub>0</sub>}@}. Thus, in order to get {@{the output in the correct place}@}, {@{_b_<sub>0</sub> should take the place of _b_<sub>4</sub>}@} and the index becomes {@{_b_<sub>0</sub>_b_<sub>4</sub>_b_<sub>3</sub>_b_<sub>2</sub>_b_<sub>1</sub>}@}. And for {@{next recursive stage}@}, {@{those 4 least significant bits}@} will become {@{_b_<sub>1</sub>_b_<sub>4</sub>_b_<sub>3</sub>_b_<sub>2</sub>}@}, If you include {@{all of the recursive stages of a radix-2 DIT algorithm}@}, {@{_all_ the bits}@} must be {@{reversed}@} and thus one must {@{pre-process the input \(_or_ post-process the output\)}@} with {@{a bit reversal to get in-order output}@}. \(If {@{each size-_N_<!-- markdown separator -->/2 subtransform}@} is to {@{operate on contiguous data}@}, {@{the DIT _input_}@} is {@{pre-processed by bit-reversal}@}.\) Correspondingly, if you {@{perform all of the steps in reverse order}@}, you obtain {@{a radix-2 DIF algorithm with bit reversal}@} in {@{post-processing \(or pre-processing, respectively\)}@}. <!--SR:!2026-11-20,294,330!2026-11-20,291,330!2026-10-06,263,330!2026-11-17,289,330!2026-10-06,263,330!2026-11-07,281,330!2026-10-24,272,330!2026-10-26,274,330!2026-10-30,270,330!2026-11-04,275,330!2026-11-05,276,330!2026-09-16,244,330!2026-05-17,149,310!2026-10-29,272,330!2026-11-21,293,330!2026-10-13,268,330!2026-10-06,263,330!2026-10-30,270,330!2026-11-14,288,330!2026-09-29,257,330!2026-11-15,294,330!2026-11-13,284,330!2026-11-15,286,330!2026-11-21,292,330!2026-11-01,275,330!2026-11-23,294,330!2026-10-25,274,330!2026-10-24,267,330!2026-11-15,286,330!2026-10-16,271,330!2026-10-26,274,330!2026-11-01,275,330!2026-11-20,291,330!2026-09-30,258,330!2026-11-14,288,330!2026-11-16,290,330!2026-05-19,150,310-->

{@{The [logarithm](logarithm.md) \(log\)}@} used in this algorithm is {@{a base 2 logarithm}@}. <!--SR:!2026-10-25,268,330!2026-11-22,293,330-->

The following is {@{pseudocode for iterative radix-2 FFT algorithm}@} implemented {@{using bit-reversal permutation}@}.<sup>[\[18\]](#^ref-18)</sup> <!--SR:!2026-10-05,262,330!2026-11-01,272,330-->

<pre>
<b>algorithm</b> iterative-fft <b>is</b>
    <b>input:</b> Array <i>a</i> of <i>n</i> complex values where n is a power of 2.
    <b>output:</b> Array <i>A</i> the DFT of a.

    bit-reverse-copy(a, A)
    <i>n</i> ← <i>a</i>.length
    <b>for</b> <i>s</i> = 1 <b>to</b> log(<i>n</i>) <b>do</b>
        <i>m</i> ← 2<sup><i>s</i></sup>
        <i>ω</i><sub><i>m</i></sub> ← exp(−2π<i>i</i>/<i>m</i>)
        <b>for</b> <i>k</i> = 0 <b>to</b> <i>n</i>-1 <b>by</b> <i>m</i> <b>do</b>
            <i>ω</i> ← 1
            <b>for</b> <i>j</i> = 0 <b>to</b> <i>m</i>/<i>2</i> – 1 <b>do</b>
                <i>t</i> ← <i>ω</i> <i>A</i>[<i>k</i> + <i>j</i> + <i>m</i>/2]
                <i>u</i> ← <i>A</i>[<i>k</i> + <i>j</i>]
                <i>A</i>[<i>k</i> + <i>j</i>] ← <i>u</i> + <i>t</i>
                <i>A</i>[<i>k</i> + <i>j</i> + <i>m</i>/2] ← <i>u</i> – <i>t</i>
                <i>ω</i> ← <i>ω</i> <i>ω</i><sub><i>m</i></sub>

    <b>return</b> <i>A</i>
</pre>

> [!info]- code
>
> ```pseudocode
> algorithm iterative-fft is
>     input: Array a of n complex values where n is a power of 2.
>     output: Array A the DFT of a.
>
>     bit-reverse-copy(a, A)
>     n ← a.length
>     for s = 1 to log(n) do
>         m ← 2s
>         ωm ← exp(−2πi/m)
>         for k = 0 to n-1 by m do
>             ω ← 1
>             for j = 0 to m/2 – 1 do
>                 t ← ω A[k + j + m/2]
>                 u ← A[k + j]
>                 A[k + j] ← u + t
>                 A[k + j + m/2] ← u – t
>                 ω ← ω ωm
>
>     return A
> ```

<!-- markdownlint MD028 -->

> __code flashcards__
>
> <pre>
> <b>algorithm</b> {@{iterative-fft}@} <b>is</b>
>     <b>input:</b> {@{Array <i>a</i> of <i>n</i> complex values where n is a power of 2.}@}
>     <b>output:</b> {@{Array <i>A</i> the DFT of a.}@}
>
>     {@{bit-reverse-copy(a, A)}@}
>     <i>n</i> ← {@{<i>a</i>.length}@}
>     {@{<b>for</b> <i>s</i> = 1 <b>to</b> log(<i>n</i>)}@} <b>do</b>
>         <i>m</i> ← {@{2<sup><i>s</i></sup>}@}
>         {@{<i>ω</i><sub><i>m</i></sub> ← exp(−2π<i>i</i>/<i>m</i>)}@}
>         {@{<b>for</b> <i>k</i> = 0 <b>to</b> <i>n</i>-1 <b>by</b> <i>m</i>}@} <b>do</b>
>             {@{<i>ω</i> ← 1}@}
>             {@{<b>for</b> <i>j</i> = 0 <b>to</b> <i>m</i>/<i>2</i> – 1}@} <b>do</b>
>                 {@{<i>t</i> ← <i>ω</i> <i>A</i>[<i>k</i> + <i>j</i> + <i>m</i>/2]}@}
>                 {@{<i>u</i> ← <i>A</i>[<i>k</i> + <i>j</i>]}@}
>                 {@{<i>A</i>[<i>k</i> + <i>j</i>] ← <i>u</i> + <i>t</i>}@}
>                 {@{<i>A</i>[<i>k</i> + <i>j</i> + <i>m</i>/2] ← <i>u</i> – <i>t</i>}@}
>                 {@{<i>ω</i> ← <i>ω</i> <i>ω</i><sub><i>m</i></sub>}@}
>
>     <b>return</b> {@{<i>A</i>}@}
> </pre> <!--SR:!2026-11-06,280,330!2026-11-13,292,330!2026-11-09,288,330!2026-11-04,275,330!2026-09-27,255,330!2026-10-31,274,330!2026-10-23,266,330!2026-11-03,274,330!2026-10-23,271,330!2026-10-31,274,330!2026-05-18,150,310!2026-09-29,257,330!2026-10-24,272,330!2026-10-15,270,330!2026-11-02,273,330!2026-11-07,281,330!2026-08-14,193,310-->

{@{The bit-reverse-copy procedure}@} can be {@{implemented as follows}@}. <!--SR:!2026-10-01,259,330!2026-11-02,276,330-->

<pre>
<b>algorithm</b> bit-reverse-copy(<i>a</i>,<i>A</i>) <b>is</b>
    <b>input:</b> Array <i>a</i> of <i>n</i> complex values where n is a power of 2.
    <b>output:</b> Array <i>A</i> of size <i>n</i>.

    <i>n</i> ← <i>a</i>.length
    <b>for</b> <i>k</i> = 0 <i>to</i> <i>n</i> – 1 <b>do</b>
        <i>A</i>[rev(k)] := <i>a</i>[k]
</pre>

> [!info]- code
>
> ```pseudocode
> algorithm bit-reverse-copy(a,A) is
>     input: Array a of n complex values where n is a power of 2.
>     output: Array A of size n.
>
>     n ← a.length
>     for k = 0 to n – 1 do
>         A[rev(k)] := a[k]
> ```

<!-- markdownlint MD028-->

> __code flashcards__
>
> <pre>
> <b>algorithm</b> {@{bit-reverse-copy(<i>a</i>,<i>A</i>)}@} <b>is</b>
>     <b>input:</b> {@{Array <i>a</i> of <i>n</i> complex values where n is a power of 2.}@}
>     <b>output:</b> {@{Array <i>A</i> of size <i>n</i>.}@}
>
>     <i>n</i> ← {@{<i>a</i>.length}@}
>     {@{<b>for</b> <i>k</i> = 0 <i>to</i> <i>n</i> – 1}@} <b>do</b>
>         {@{<i>A</i>[rev(k)] := <i>a</i>[k]}@}
> </pre> <!--SR:!2026-10-30,279,330!2026-11-06,285,330!2026-11-21,292,330!2026-11-22,293,330!2026-10-24,273,330!2026-11-09,280,330-->

Alternatively, {@{some applications \(such as convolution\)}@} work {@{equally well on bit-reversed data}@}, so one can perform {@{forward transforms, processing, and then inverse transforms}@} all without {@{bit reversal}@} to produce {@{final results in the natural order}@}. <!--SR:!2026-10-26,269,330!2026-10-01,259,330!2026-09-27,255,330!2026-11-03,274,330!2026-10-06,263,330-->

{@{Many FFT users}@}, however, prefer {@{natural-order outputs}@}, and {@{a separate, explicit bit-reversal stage}@} can have {@{a non-negligible impact on the computation time}@},<sup>[\[13\]](#^ref-13)</sup> even though {@{bit reversal}@} can be {@{done in O\(_N_\) time and has been the subject of much research}@}.<sup>[\[19\]](#^ref-19)</sup><sup>[\[20\]](#^ref-20)</sup><sup>[\[21\]](#^ref-21)</sup> Also, while {@{the permutation}@} is {@{a bit reversal in the radix-2 case}@}, it is more generally {@{an arbitrary \(mixed-base\) digit reversal}@} for {@{the mixed-radix case}@}, and {@{the permutation algorithms}@} become {@{more complicated to implement}@}. Moreover, it is desirable on {@{many hardware architectures}@} to re-order {@{intermediate stages of the FFT algorithm}@} so that they operate on {@{consecutive \(or at least more localized\) data elements}@}. To these ends, {@{a number of alternative implementation schemes}@} have been devised for the Cooley–Tukey algorithm that do not require {@{separate bit reversal}@} and/or involve {@{additional permutations at intermediate stages}@}. <!--SR:!2026-09-10,242,330!2026-10-25,273,330!2026-11-04,275,330!2026-10-14,269,330!2026-11-02,276,330!2026-11-16,290,330!2026-11-10,281,330!2026-09-11,239,330!2026-11-10,289,330!2026-11-18,292,330!2026-11-12,283,330!2026-11-11,282,330!2026-10-24,267,330!2026-11-03,274,330!2026-09-17,245,330!2026-10-06,263,330!2026-11-07,281,330!2026-10-22,265,330-->

{@{The problem is greatly simplified}@} if it is {@{__out-of-place__}@}: {@{the output array}@} is distinct {@{from the input array}@} or, equivalently, {@{an equal-size auxiliary array is available}@}. {@{The __Stockham auto-sort__ algorithm}@}<sup>[\[22\]](#^ref-22)</sup><sup>[\[23\]](#^ref-23)</sup> performs {@{every stage of the FFT out-of-place}@}, typically writing {@{back and forth between two arrays}@}, transposing {@{one "digit" of the indices with each stage}@}, and has been especially {@{popular on [SIMD](SIMD.md) architectures}@}.<sup>[\[23\]](#^ref-23)</sup><sup>[\[24\]](#^ref-24)</sup> Even {@{greater potential SIMD advantages \(more consecutive accesses\)}@} have been proposed for {@{the __Pease__ algorithm}@},<sup>[\[25\]](#^ref-25)</sup> which also reorders {@{out-of-place with each stage}@}, but this method requires {@{separate bit/digit reversal and O\(_N_ log _N_\) storage}@}. One can also directly apply the {@{Cooley–Tukey factorization definition}@} with {@{explicit \([depth-first](depth-first%20search.md)\) recursion and small radices}@}, which produces {@{natural-order out-of-place output}@} with {@{no separate permutation step \(as in the pseudocode above\)}@} and can be argued to have {@{[cache-oblivious](cache-oblivious%20algorithm.md) locality benefits}@} on {@{systems with [hierarchical memory](cache%20(computing).md)}@}.<sup>[\[9\]](#^ref-9)</sup><sup>[\[13\]](#^ref-13)</sup><sup>[\[26\]](#^ref-26)</sup> <!--SR:!2026-11-12,286,330!2026-10-16,271,330!2026-11-01,280,330!2026-10-24,264,330!2026-11-08,280,330!2026-11-11,291,330!2026-11-03,274,330!2026-10-09,265,330!2026-11-09,281,330!2026-11-05,276,330!2026-11-05,276,330!2026-11-10,281,330!2026-11-19,290,330!2026-10-12,268,330!2026-11-09,288,330!2026-11-12,283,330!2026-09-23,251,330!2026-11-17,291,330!2026-11-18,292,330!2026-10-23,271,330-->

{@{A typical strategy for in-place algorithms}@} without {@{auxiliary storage and without separate digit-reversal passes}@} involves {@{small matrix transpositions \(which swap individual pairs of digits\) at intermediate stages}@}, which can be combined with {@{the radix butterflies}@} to reduce {@{the number of passes over the data}@}.<sup>[\[13\]](#^ref-13)</sup><sup>[\[27\]](#^ref-27)</sup><sup>[\[28\]](#^ref-28)</sup><sup>[\[29\]](#^ref-29)</sup><sup>[\[30\]](#^ref-30)</sup> <!--SR:!2026-11-12,291,330!2026-10-28,268,330!2026-11-17,288,330!2026-09-24,252,330!2026-11-11,285,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Cooley–Tukey_FFT_algorithm) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFGauss1866"></a> [Gauss, Carl Friedrich](Carl%20Friedrich%20Gauss.md) \(1866\). ["Theoria interpolationis methodo nova tractata"](https://babel.hathitrust.org/cgi/pt?id=uc1.c2857678;view=1up;seq=279) \[Theory regarding a new method of interpolation\]. _Nachlass_ \(Unpublished manuscript\). Werke \(in Latin and German\). Vol. 3. Göttingen, Germany: Königlichen Gesellschaft der Wissenschaften zu Göttingen. pp. 265–303. <a id="^ref-1"></a>^ref-1
2. Heideman, M. T., D. H. Johnson, and [C. S. Burrus](C.%20Sidney%20Burrus.md), "[Gauss and the history of the fast Fourier transform](https://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=1162257)," IEEE ASSP Magazine, 1, \(4\), 14–21 \(1984\) <a id="^ref-2"></a>^ref-2
3. <a id="CITEREFCooleyTukey1965"></a> Cooley, James W.; Tukey, John W. \(1965\). ["An algorithm for the machine calculation of complex Fourier series"](https://doi.org/10.2307%2F2003354). _[Math. Comput.](Mathematics%20of%20Computation.md)_ __19__ \(90\): 297–301. [doi](doi%20(identifier).md):[10.2307/2003354](https://doi.org/10.2307%2F2003354). [JSTOR](JSTOR%20(identifier).md#content) [2003354](https://www.jstor.org/stable/2003354). <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFCooleyLewisWelch1967"></a> Cooley, James W.; Lewis, Peter A. W.; Welch, Peter D. \(1967\). ["Historical notes on the fast Fourier transform"](http://www.ece.ucdavis.edu/~bbaas/281/papers/CooleyLewisWelch.1967.HistNotesFFT.pdf) \(PDF\). _IEEE Transactions on Audio and Electroacoustics_. __15__ \(2\): 76–79. [CiteSeerX](CiteSeerX%20(identifier).md) [10.1.1.467.7209](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.467.7209). [doi](doi%20(identifier).md):[10.1109/tau.1967.1161903](https://doi.org/10.1109%2Ftau.1967.1161903). <a id="^ref-4"></a>^ref-4
5. Rockmore, Daniel N., _Comput. Sci. Eng._ __2__ \(1\), 60 \(2000\). [The FFT — an algorithm the whole family can use](http://www.cs.dartmouth.edu/~rockmore/cse-fft.pdf) Special issue on "top ten algorithms of the century "<a id="CITEREFBarry A. Cipra"></a> Barry A. Cipra. ["The Best of the 20th Century: Editors Name Top 10 Algorithms"](https://web.archive.org/web/20090407080904/http://amath.colorado.edu/resources/archive/topten.pdf) \(PDF\). _SIAM News_. __33__ \(4\). Archived from [the original](http://amath.colorado.edu/resources/archive/topten.pdf) \(PDF\) on 2009-04-07. Retrieved 2009-03-31. <a id="^ref-5"></a>^ref-5
6. James W. Cooley, Peter A. W. Lewis, and Peter W. Welch, "Historical notes on the fast Fourier transform," _Proc. IEEE_, vol. __55__ \(no. 10\), p. 1675–1677 \(1967\). <a id="^ref-6"></a>^ref-6
7. Danielson, G. C., and C. Lanczos, "Some improvements in practical Fourier analysis and their application to X-ray scattering from liquids," _J. Franklin Inst._ __233__, 365–380 and 435–452 \(1942\). <a id="^ref-7"></a>^ref-7
8. S. G. Johnson and M. Frigo, "[Implementing FFTs in practice](http://cnx.org/content/m16336/)," in _Fast Fourier Transforms_ \(C. S. Burrus, ed.\), ch. 11, Rice University, Houston TX: Connexions, September 2008. <a id="^ref-8"></a>^ref-8
9. <a id="CITEREFSingleton1967"></a> Singleton, Richard C. \(1967\). ["On computing the fast Fourier transform"](https://doi.org/10.1145%2F363717.363771). _Commun. ACM_. __10__ \(10\): 647–654. [doi](doi%20(identifier).md):[10.1145/363717.363771](https://doi.org/10.1145%2F363717.363771). [S2CID](S2CID%20(identifier).md#S2CID) [6287781](https://api.semanticscholar.org/CorpusID:6287781). <a id="^ref-9"></a>^ref-9
10. Duhamel, P., and M. Vetterli, "Fast Fourier transforms: a tutorial review and a state of the art," _Signal Processing_ __19__, 259–299 \(1990\) <a id="^ref-10"></a>^ref-10
11. Lundy, T., and J. Van Buskirk, "A new matrix approach to real FFTs and convolutions of length 2<sup>_k_</sup>," _Computing_ __80__, 23–45 \(2007\). <a id="^ref-11"></a>^ref-11
12. Johnson, S. G., and M. Frigo, "[A modified split-radix FFT with fewer arithmetic operations](http://www.fftw.org/newsplit.pdf)," _IEEE Trans. Signal Process._ __55__ \(1\), 111–119 \(2007\). <a id="^ref-12"></a>^ref-12
13. <a id="CITEREFFrigoJohnson2005"></a> Frigo, M.; Johnson, S. G. \(2005\). ["The Design and Implementation of FFTW3"](http://www.fftw.org/fftw-paper-ieee.pdf) \(PDF\). _Proceedings of the IEEE_. __93__ \(2\): 216–231. [Bibcode](bibcode%20(identifier).md):[2005IEEEP..93..216F](https://ui.adsabs.harvard.edu/abs/2005IEEEP..93..216F). [CiteSeerX](CiteSeerX%20(identifier).md) [10.1.1.66.3097](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.66.3097). [doi](doi%20(identifier).md):[10.1109/JPROC.2004.840301](https://doi.org/10.1109%2FJPROC.2004.840301). [S2CID](S2CID%20(identifier).md#S2CID) [6644892](https://api.semanticscholar.org/CorpusID:6644892). <a id="^ref-13"></a>^ref-13
14. Gentleman W. M., and G. Sande, "Fast Fourier transforms—for fun and profit," _Proc. AFIPS_ __29__, 563–578 \(1966\). <a id="^ref-14"></a>^ref-14
15. Bailey, David H., "FFTs in external or hierarchical memory," _J. Supercomputing_ __4__ \(1\), 23–35 \(1990\) <a id="^ref-15"></a>^ref-15
16. M. Frigo, C. E. Leiserson, H. Prokop, and S. Ramachandran. Cache-oblivious algorithms. In _Proceedings of the 40th IEEE Symposium on Foundations of Computer Science_ \(FOCS 99\), p.285-297. 1999. [Extended abstract at IEEE](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=814600), [at Citeseer](http://citeseer.ist.psu.edu/307799.html). <a id="^ref-16"></a>^ref-16
17. Cooley, J. W., P. Lewis and P. Welch, "The Fast Fourier Transform and its Applications", _IEEE Trans on Education_ __12__, 1, 28–34 \(1969\) <a id="^ref-17"></a>^ref-17
18. <a id="CITEREFCormenLeisersonRivestStein2009"></a> Cormen, Thomas H.; Leiserson, Charles; Rivest, Ronald; Stein, Clifford \(2009\). _Introduction to algorithms_ \(3rd ed.\). Cambridge, Mass.: MIT Press. pp. 915–918. [ISBN](ISBN%20(identifier).md) [978-0-262-03384-8](https://en.wikipedia.org/wiki/Special:BookSources/978-0-262-03384-8). <a id="^ref-18"></a>^ref-18
19. <a id="CITEREFKarp1996"></a> Karp, Alan H. \(1996\). "Bit reversal on uniprocessors". _SIAM Review_. __38__ \(1\): 1–26. [CiteSeerX](CiteSeerX%20(identifier).md) [10.1.1.24.2913](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.24.2913). [doi](doi%20(identifier).md):[10.1137/1038001](https://doi.org/10.1137%2F1038001). [JSTOR](JSTOR%20(identifier).md#content) [2132972](https://www.jstor.org/stable/2132972). <a id="^ref-19"></a>^ref-19
20. <a id="CITEREFCarterGatlin1998"></a> Carter, Larry; Gatlin, Kang Su \(1998\). "Towards an optimal bit-reversal permutation program". _Proceedings 39th Annual Symposium on Foundations of Computer Science \(Cat. No.98CB36280\)_. pp. 544–553. [CiteSeerX](CiteSeerX%20(identifier).md) [10.1.1.46.9319](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.46.9319). [doi](doi%20(identifier).md):[10.1109/SFCS.1998.743505](https://doi.org/10.1109%2FSFCS.1998.743505). [ISBN](ISBN%20(identifier).md) [978-0-8186-9172-0](https://en.wikipedia.org/wiki/Special:BookSources/978-0-8186-9172-0). [S2CID](S2CID%20(identifier).md#S2CID) [14307262](https://api.semanticscholar.org/CorpusID:14307262). <a id="^ref-20"></a>^ref-20
21. <a id="CITEREFRubioGómezDrouiche2002"></a> Rubio, M.; Gómez, P.; Drouiche, K. \(2002\). "A new superfast bit reversal algorithm". _International Journal of Adaptive Control and Signal Processing_. __16__ \(10\): 703–707. [doi](doi%20(identifier).md):[10.1002/acs.718](https://doi.org/10.1002%2Facs.718). [S2CID](S2CID%20(identifier).md#S2CID) [62201722](https://api.semanticscholar.org/CorpusID:62201722). <a id="^ref-21"></a>^ref-21
22. Originally attributed to Stockham in W. T. Cochran _et al._, [What is the fast Fourier transform?](https://dx.doi.org/10.1109/PROC.1967.5957), _Proc. IEEE_ vol. 55, 1664–1674 \(1967\). <a id="^ref-22"></a>^ref-22
23. P. N. Swarztrauber, [FFT algorithms for vector computers](https://dx.doi.org/10.1016/S0167-8191(84)90413-7), _Parallel Computing_ vol. 1, 45–63 \(1984\). <a id="^ref-23"></a>^ref-23
24. <a id="CITEREFSwarztrauber1982"></a> Swarztrauber, P. N. \(1982\). ["Vectorizing the FFTs"](https://archive.org/details/parallelcomputat0000unse/page/51). In Rodrigue, G. \(ed.\). _Parallel Computations_. New York: Academic Press. pp. [51–83](https://archive.org/details/parallelcomputat0000unse/page/51). [ISBN](ISBN%20(identifier).md) [978-0-12-592101-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-12-592101-5). <a id="^ref-24"></a>^ref-24
25. <a id="CITEREFPease1968"></a> Pease, M. C. \(1968\). ["An adaptation of the fast Fourier transform for parallel processing"](https://doi.org/10.1145%2F321450.321457). _J. ACM_. __15__ \(2\): 252–264. [doi](doi%20(identifier).md):[10.1145/321450.321457](https://doi.org/10.1145%2F321450.321457). [S2CID](S2CID%20(identifier).md#S2CID) [14610645](https://api.semanticscholar.org/CorpusID:14610645). <a id="^ref-25"></a>^ref-25
26. <a id="CITEREFFrigoJohnson"></a> Frigo, Matteo; Johnson, Steven G. ["FFTW"](http://www.fftw.org/). A free \([GPL](GNU%20General%20Public%20License.md)\) C library for computing discrete Fourier transforms in one or more dimensions, of arbitrary size, using the Cooley–Tukey algorithm <a id="^ref-26"></a>^ref-26
27. <a id="CITEREFJohnsonBurrus1984"></a> Johnson, H. W.; Burrus, C. S. \(1984\). "An in-place in-order radix-2 FFT". _Proc. ICASSP_: 28A.2.1–28A.2.4. <a id="^ref-27"></a>^ref-27
28. <a id="CITEREFTemperton1991"></a> Temperton, C. \(1991\). "Self-sorting in-place fast Fourier transform". _SIAM Journal on Scientific and Statistical Computing_. __12__ \(4\): 808–823. [doi](doi%20(identifier).md):[10.1137/0912043](https://doi.org/10.1137%2F0912043). <a id="^ref-28"></a>^ref-28
29. <a id="CITEREFQianLuAnTolimieri1994"></a> Qian, Z.; Lu, C.; An, M.; Tolimieri, R. \(1994\). "Self-sorting in-place FFT algorithm with minimum working space". _IEEE Transactions on Signal Processing_. __52__ \(10\): 2835–2836. [Bibcode](bibcode%20(identifier).md):[1994ITSP...42.2835Q](https://ui.adsabs.harvard.edu/abs/1994ITSP...42.2835Q). [doi](doi%20(identifier).md):[10.1109/78.324749](https://doi.org/10.1109%2F78.324749). <a id="^ref-29"></a>^ref-29
30. <a id="CITEREFHegland1994"></a> Hegland, M. \(1994\). "A self-sorting in-place fast Fourier transform algorithm suitable for vector and parallel processing". _Numerische Mathematik_. __68__ \(4\): 507–547. [CiteSeerX](CiteSeerX%20(identifier).md) [10.1.1.54.5659](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.54.5659). [doi](doi%20(identifier).md):[10.1007/s002110050074](https://doi.org/10.1007%2Fs002110050074). [S2CID](S2CID%20(identifier).md#S2CID) [121258187](https://api.semanticscholar.org/CorpusID:121258187). <a id="^ref-30"></a>^ref-30

## external links

- <a id="CITEREFChernenko"></a> ["Fast Fourier transform - FFT"](http://www.librow.com/articles/article-10). _Cooley-Tukey technique_. Article. 10. A simple, pedagogical radix-2 algorithm in C++
- <a id="CITEREFBorgerding2022"></a> ["KISSFFT"](https://github.com/mborgerding/kissfft). [GitHub](GitHub.md). 11 February 2022. A simple mixed-radix Cooley–Tukey implementation in C
- [Dsplib](https://github.com/Dsplib) on [GitHub](GitHub.md)
- <a id="CITEREFBakhurin"></a> ["Radix-2 Decimation in Time FFT Algorithm"](https://web.archive.org/web/20171031023423/http://en.dsplib.org/content/fft_dec_in_time.html). Archived from [the original](http://en.dsplib.org/content/fft_dec_in_time.html) on October 31, 2017. <a id="CITEREFБахурин"></a> ["Алгоритм БПФ по основанию два с прореживанием по времени"](http://ru.dsplib.org/content/fft_dec_in_time/fft_dec_in_time.html) \(in Russian\).
- <a id="CITEREFBakhurin"></a> ["Radix-2 Decimation in Frequency FFT Algorithm"](https://web.archive.org/web/20171114115729/http://en.dsplib.org/content/fft_dec_in_freq.html). Archived from [the original](http://en.dsplib.org/content/fft_dec_in_freq.html) on November 14, 2017. <a id="CITEREFБахурин"></a> ["Алгоритм БПФ по основанию два с прореживанием по частоте"](http://ru.dsplib.org/content/fft_dec_in_freq/fft_dec_in_freq.html) \(in Russian\).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [FFT algorithms](https://en.wikipedia.org/wiki/Category:FFT%20algorithms)
> - [Divide-and-conquer algorithms](https://en.wikipedia.org/wiki/Category:Divide-and-conquer%20algorithms)
