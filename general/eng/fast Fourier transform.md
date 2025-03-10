---
aliases:
  - FFT
  - FFTs
  - fast Fourier transform
  - fast Fourier transforms
tags:
  - flashcard/active/general/eng/fast_Fourier_transform
  - language/in/English
---

# fast Fourier transform

A __fast Fourier transform__ (__FFT__) is {@{an [algorithm](algorithm.md) that computes the [discrete Fourier Transform](discrete%20Fourier%20transform.md) (DFT) of a sequence, or its inverse (IDFT)}@}. {@{[Fourier analysis](Fourier%20analysis.md)}@} {@{converts a signal from its original domain (often time or space) to a representation in the [frequency domain](frequency%20domain.md) and vice versa}@}. The DFT is obtained by {@{decomposing a [sequence](sequence.md) of values into components of different frequencies}@}. This operation is {@{useful in many fields}@}, but {@{computing it directly from the definition is often too slow to be practical}@}. An FFT {@{rapidly computes such transformations}@} by {@{[factorizing](matrix%20decomposition.md) the [DFT matrix](DFT%20matrix.md) into a product of [sparse](sparse%20matrix.md) (mostly zero) factors}@}. As a result, it manages to {@{reduce the [complexity](computational%20complexity%20theory.md) of computing the DFT from $O(n^{2})$, which arises if one simply applies the definition of DFT, to $O(n\log n)$, where _n_ is the data size}@}. The difference in speed can {@{be enormous, especially for long data sets where _n_ may be in the thousands or millions}@}. In {@{the presence of [round-off error](round-off%20error.md)}@}, many FFT algorithms are {@{much more accurate than evaluating the DFT definition directly or indirectly}@}. There are {@{many different FFT algorithms based on a wide range of published theories}@}, from {@{simple [complex-number arithmetic](complex%20number.md) to [group theory](group%20theory.md) and [number theory](number%20theory.md)}@}.

## algorithms

### Cooley–Tukey algorithm

- see: [Cooley–Tukey FFT algorithm](Cooley–Tukey%20FFT%20algorithm.md)

{@{By far the most commonly used FFT}@} is {@{the Cooley–Tukey algorithm}@}. This is {@{a [divide-and-conquer algorithm](divide-and-conquer%20algorithm.md)}@} that {@{[recursively](recursion.md) breaks down a DFT of any [composite](composite%20number.md) size $n=n_{1}n_{2}$ into $n_{1}$ smaller DFTs of size $n_{2}$}@}, along with {@{$O(n)$ multiplications by complex [roots of unity](root%20of%20unity.md) traditionally called [twiddle factors](twiddle%20factor.md)}@} (after Gentleman and Sande, 1966).

This method (and the general idea of an FFT) was {@{popularized by a publication of Cooley and Tukey in 1965}@}, but it was later discovered that those two authors had {@{independently re-invented an algorithm known to [Carl Friedrich Gauss](Carl%20Friedrich%20Gauss.md) around 1805}@} (and {@{subsequently rediscovered several times in limited forms}@}).

The best known use of the Cooley–Tukey algorithm is {@{to divide the transform into two pieces of size n/2 at each step, and is therefore limited to power-of-two sizes}@}, but {@{any factorization can be used in general (as was known to both Gauss and Cooley/Tukey)}@}. These are called {@{the _radix-2_ and _mixed-radix_ cases, respectively (and other variants such as the [split-radix FFT](Split-radix%20FFT%20algorithm.md) have their own names as well)}@}. Although {@{the basic idea is recursive}@}, most traditional implementations {@{rearrange the algorithm to avoid explicit recursion}@}. Also, because {@{the Cooley–Tukey algorithm breaks the DFT into smaller DFTs}@}, it can {@{be combined arbitrarily with any other algorithm for the DFT, such as those described below}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/fast_Fourier_transform) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
