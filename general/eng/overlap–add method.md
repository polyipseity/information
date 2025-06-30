---
aliases:
  - overlap-add method
  - overlap-add methods
  - overlap–add method
  - overlap–add methods
tags:
  - flashcard/active/general/eng/overlap-add_method
  - language/in/English
---

# overlap–add method

- This article is about {@{the convolution method}@}. For {@{the "Weight, OverLap, Add" channelization method}@}, see {@{[Sampling the DTFT](discrete-time%20Fourier%20transform.md#sampling%20the%20DTFT)}@}. <!--SR:!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288-->

In {@{[signal processing](signal%20processing.md)}@}, {@{the __overlap–add method__}@} is {@{an efficient way to evaluate the discrete [convolution](convolution.md)}@} of {@{a very long signal $x[n]$ with a [finite impulse response](finite%20impulse%20response.md) \(FIR\) filter $h[n]$}@}: {@{$$y[n]=x[n]*h[n]\ \triangleq \ \sum _{m=-\infty }^{\infty }h[m]\cdot x[n-m]=\sum _{m=1}^{M}h[m]\cdot x[n-m] \,,$$}@} __<a id="math Eq.1">Eq.1</a>__ <p> where {@{$h[m]=0$ for $m$ outside the region $[1,M]$}@}.  This article uses {@{common abstract notations}@}, such as {@{$y(t)=x(t)*h(t)$, or $y(t)={\mathcal {H} }\{x(t)\}$}@}, in which it is understood that the functions should be thought of {@{in their totality, rather than at specific instants $t$}@} \(see {@{[Convolution\#Notation](convolution.md#notation)}@}\). <!--SR:!2025-07-01,4,270!2025-07-01,4,270!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,278-->

> {@{![Fig 1: A sequence of five plots depicts one cycle of the overlap-add convolution algorithm.](../../archives/Wikimedia%20Commons/Overlap-add%20algorithm.svg)}@}
>
> Fig 1: A sequence of {@{five plots depicts one cycle of the overlap-add convolution algorithm}@}. The first plot is {@{a long sequence of data to be processed with a lowpass FIR filter}@}. The 2nd plot is {@{one segment of the data to be processed in piecewise fashion}@}. The 3rd plot is {@{the filtered segment, including the filter rise and fall transients}@}. The 4th plot indicates {@{where the new data will be added with the result of previous segments}@}. The 5th plot is {@{the updated output stream}@}. The FIR filter is {@{a boxcar lowpass with $M=16$ samples}@}, the length of the segments is {@{$L=100$ samples}@} and the overlap is {@{15 samples}@}. <!--SR:!2025-07-01,4,288!2025-07-01,4,288!2025-07-10,10,270!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-02,4,278-->

The concept is to {@{divide the problem into multiple convolutions of $h[n]$}@} with {@{short segments of $x[n]$}@}: {@{$$x_{k}[n]\ \triangleq \ {\begin{cases}x[n+kL],&n=1,2,\ldots ,L\\0,&{\text{otherwise} },\end{cases} }$$}@} where {@{$L$ is an arbitrary segment length}@}. Then: {@{$$x[n]=\sum _{k}x_{k}[n-kL],\,$$}@} and $y[n]$ can be {@{written as a sum of short convolutions}@}:<sup>[\[1\]](#^ref-1)</sup> {@{$${\begin{aligned}y[n]=\left(\sum _{k}x_{k}[n-kL]\right)*h[n]&=\sum _{k}\left(x_{k}[n-kL]*h[n]\right)\\&=\sum _{k}y_{k}[n-kL],\end{aligned} }$$}@} where {@{the linear convolution $y_{k}[n]\ \triangleq \ x_{k}[n]*h[n]\,$}@} is {@{zero outside the region $[1,L+M-1]$}@}. And for {@{any parameter $N\geq L+M-1,\,$}@}<sup>[\[A\]](#^ref-A)</sup> it is equivalent to {@{the $N$-point [circular convolution](circular%20convolution.md) of $x_{k}[n]\,$ with $h[n]\,$ in the region $[1,N]$}@}.  The advantage is that {@{the circular convolution can be computed more efficiently than linear convolution}@}, according to {@{the [circular convolution theorem](discrete%20Fourier%20transform.md#circular%20convolution%20theorem%20and%20cross-correlation%20theorem)}@}: {@{$$y_{k}[n]\ =\ \scriptstyle {\text{IDFT} }_{N}\displaystyle (\ \scriptstyle {\text{DFT} }_{N}\displaystyle (x_{k}[n])\cdot \ \scriptstyle {\text{DFT} }_{N}\displaystyle (h[n])\ ) \,,$$}@} __<a id="math Eq.2">Eq.2</a>__ <p> where: <!--SR:!2025-07-01,4,288!2025-07-01,4,270!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,278!2025-07-01,4,288!2025-07-01,4,278!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-02,4,278!2025-07-01,4,278-->

- DFT<sub>N</sub> and IDFT<sub>N</sub> ::@:: refer to the [Discrete Fourier transform](discrete%20Fourier%20transform.md) and its inverse, evaluated over $N$ discrete points, and <!--SR:!2025-07-01,4,288!2025-07-01,4,288-->
- $L$ is customarily chosen ::@:: such that $N=L+M-1$ is an integer power-of-2, and the transforms are implemented with the [FFT](fast%20Fourier%20transform.md) algorithm, for efficiency. <!--SR:!2025-07-01,4,288!2025-07-01,4,278-->

## pseudocode

The following is {@{a [pseudocode](pseudocode.md) of the algorithm}@}: <!--SR:!2025-07-01,4,270-->

```pseudocode
(Overlap-add algorithm for linear convolution)
h = FIR_filter
M = length(h)
Nx = length(x)
N = 8 × 2^ceiling( log2(M) )     (8 times the smallest power of two bigger than filter length M.  See next section for a slightly better choice.)
step_size = N - (M-1)  (L in the text above)
H = DFT(h, N)
position = 0
y(1 : Nx + M-1) = 0

while position + step_size ≤ Nx do
    y(position+(1:N)) = y(position+(1:N)) + IDFT(DFT(x(position+(1:step_size)), N) × H)
    position = position + step_size
end
```

> __code flashcards__
>
> <pre>
> <span style="color:green;">(<i>Overlap-add algorithm for linear convolution</i>)</span>
> h = {@{FIR_filter}@}
> M = {@{length(h)}@}
> Nx = {@{length(x)}@}
> N = {@{8 × 2^ceiling( log2(M) )}@}     {@{<span style="color:green;">(8 times the smallest power of two bigger than filter length M.  See next section for a slightly better choice.)</span>}@}
> step_size = {@{N - (M-1)}@}  {@{<span style="color:green;">(L in the text above)</span>}@}
> H = {@{DFT(h, N)}@}
> {@{position}@} = 0
> {@{y(1&nbsp;: Nx + M-1)}@} = 0
>
> <b>while</b> {@{position + step_size ≤ Nx}@} <b>do</b>
>     {@{y(position+(1:N))}@} = {@{y(position+(1:N)) + IDFT(DFT(x(position+(1:step_size)), N) × H)}@}
>     position = {@{position + step_size}@}
> <b>end</b>
> </pre> <!--SR:!2025-07-01,4,288!2025-07-01,4,278!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-02,4,278-->

## efficiency considerations

> {@{![Fig 2: A graph of the values of N \(an integer power of 2\) that minimize the cost function ${\tfrac {N\left(\log _{2}N+1\right)}{N-M+1} }$](../../archives/Wikimedia%20Commons/FFT%20size%20vs%20filter%20length%20for%20Overlap-add%20convolution.svg)}@}
>
> Fig 2: A graph of {@{the values of N \(an integer power of 2\)}@} that {@{minimize the cost function ${\tfrac {N\left(\log _{2}N+1\right)}{N-M+1} }$}@} <!--SR:!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,278-->

When {@{the DFT and IDFT are implemented by the FFT algorithm}@}, the pseudocode above requires {@{about __N \(log<sub>2</sub>\(N\) + 1\)__ complex multiplications}@} for {@{the FFT, product of arrays, and IFFT}@}.<sup>[\[B\]](#^ref-B)</sup> Each iteration {@{produces __N-M+1__ output samples}@}, so {@{the number of complex multiplications per output sample}@} is about: {@{$${\frac {N(\log _{2}(N)+1)}{N-M+1} }.\,$$}@} __<a id="math Eq.3">Eq.3</a>__ <p> <!--SR:!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,270!2025-07-01,4,288-->

For example, when {@{$M=201$ and $N=1024$}@}, __[Eq.3](#math%20Eq.3)__ {@{equals $13.67$}@}, whereas {@{direct evaluation of __[Eq.1](#math%20Eq.1)__ \(annotation: applying the convolution definition directly\)}@} would {@{require up to $201$ complex multiplications per output sample}@}, the worst case being when {@{both $x$ and $h$ are complex-valued}@}. Also note that for {@{any given $M$}@}, __[Eq.3](#math%20Eq.3)__ has {@{a minimum with respect to $N$}@}. Figure 2 is a graph of {@{the values of $N$ that minimize __[Eq.3](#math%20Eq.3)__ for a range of filter lengths \($M$\)}@}. <!--SR:!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288-->

Instead of {@{__[Eq.1](#math%20Eq.1)__}@}, we can also consider {@{applying __[Eq.2](#math%20Eq.2)__ to a long sequence of length $N_{x}$ samples \(annotation: applying the circular convolution theorem and the FFT\)}@}. {@{The total number of complex multiplications}@} would be: {@{$$N_{x}\cdot (\log _{2}(N_{x})+1).$$}@} Comparatively, {@{the number of complex multiplications}@} required by the pseudocode algorithm is: {@{$$N_{x}\cdot (\log _{2}(N)+1)\cdot {\frac {N}{N-M+1} }.$$}@} <!--SR:!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,278!2025-07-01,4,288!2025-07-02,4,278-->

Hence {@{the _cost_ of the overlap–add method}@} scales almost as {@{$O\left(N_{x}\log _{2}N\right)$}@} while {@{the cost of a single, large circular convolution}@} is almost {@{$O\left(N_{x}\log _{2}N_{x}\right)$}@}. {@{The two methods are also compared}@} in {@{Figure 3, created by Matlab simulation}@}. {@{The contours}@} are {@{lines of constant ratio of the times it takes to perform both methods}@}. When {@{the overlap-add method is faster}@}, the ratio {@{exceeds 1}@}, and ratios as high as {@{3 are seen}@}. <!--SR:!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,278!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288-->

> {@{![Fig 3: Gain of the overlap-add method compared to a single, large circular convolution.](../../archives/Wikimedia%20Commons/Gain%20oa%20method.png)}@}
>
> Fig 3: Gain of {@{the overlap-add method compared to a single, large circular convolution \(annotation: created by MATLAB simulation\)}@}. The axes show {@{values of signal length N<sub>x</sub> and filter length N<sub>h</sub>}@}. <!--SR:!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288-->

## see also

- [Overlap–save method](overlap–save%20method.md)
- [Circular convolution\#Example](circular%20convolution.md#example)

## notes

1. A. This condition implies that {@{the $x_{k}$ segment}@} has {@{at least $M-1$ appended zeros}@}, which prevents {@{circular overlap of the output rise and fall transients}@}. <a id="^ref-A"></a>^ref-A
2. B. {@{Cooley–Tukey FFT algorithm for N=2<sup>k</sup>}@} needs {@{\(N/2\) log<sub>2</sub>\(N\)}@} – see {@{[FFT – Definition and speed](fast%20Fourier%20transform.md#definition)}@} <a id="^ref-B"></a>^ref-B <!--SR:!2025-07-01,4,288!2025-07-02,4,278!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288!2025-07-01,4,288-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/overlap–add_method) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFRabiner, Lawrence R.Gold, Bernard1975"></a> Rabiner, Lawrence R.; Gold, Bernard \(1975\). ["2.25"](https://archive.org/details/theoryapplicatio00rabi/page/63). _Theory and application of digital signal processing_. Englewood Cliffs, N.J.: Prentice-Hall. pp. [63–65](https://archive.org/details/theoryapplicatio00rabi/page/63). [ISBN](ISBN%20(identifier).md) [0-13-914101-4](https://en.wikipedia.org/wiki/Special:BookSources/0-13-914101-4). <a id="^ref-1"></a>^ref-1

## further reading

- <a id="CITEREFOppenheim, Alan V.Schafer, Ronald W.1975"></a> Oppenheim, Alan V.; Schafer, Ronald W. \(1975\). _Digital signal processing_. Englewood Cliffs, N.J.: Prentice-Hall. [ISBN](ISBN%20(identifier).md) [0-13-214635-5](https://en.wikipedia.org/wiki/Special:BookSources/0-13-214635-5).
- <a id="CITEREFHayes, M. Horace1999"></a> Hayes, M. Horace \(1999\). _Digital Signal Processing_. Schaum's Outline Series. New York: McGraw Hill. [ISBN](ISBN%20(identifier).md) [0-07-027389-8](https://en.wikipedia.org/wiki/Special:BookSources/0-07-027389-8).
- <a id="CITEREFSenobariFunningKeoghZhu2019"></a> Senobari, Nader Shakibay; Funning, Gareth J.; Keogh, Eamonn; Zhu, Yan; Yeh, Chin-Chia Michael; Zimmerman, Zachary; Mueen, Abdullah \(2019\). ["Super-Efficient Cross-Correlation \(SEC-C\): A Fast Matched Filtering Code Suitable for Desktop Computers"](https://www.cs.ucr.edu/~eamonn/SuperEfficientCrossCorrelation.pdf) \(PDF\). _Seismological Research Letters_. __90__ \(1\): 322–334. [doi](doi%20(identifier).md):[10.1785/0220180122](https://doi.org/10.1785%2F0220180122). [ISSN](ISSN%20(identifier).md) [0895-0695](https://search.worldcat.org/issn/0895-0695).

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Signal processing](https://en.wikipedia.org/wiki/Category:Signal%20processing)
> - [Transforms](https://en.wikipedia.org/wiki/Category:Transforms)
> - [Fourier analysis](https://en.wikipedia.org/wiki/Category:Fourier%20analysis)
> - [Numerical analysis](https://en.wikipedia.org/wiki/Category:Numerical%20analysis)
