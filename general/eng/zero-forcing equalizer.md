---
aliases:
  - ZFE
  - ZFEs
  - zero-forcing equaliser
  - zero-forcing equalisers
  - zero-forcing equalizer
  - zero-forcing equalizers
tags:
  - flashcard/active/general/eng/zero-forcing_equalizer
  - language/in/English
---

# zero-forcing equalizer

{@{The __zero-forcing equalizer__}@} is {@{a form of linear [equalization](equalization%20(communications).md) [algorithm](algorithm.md) used in [communication systems](telecommunications.md)}@} which {@{applies the inverse of the [frequency response](frequency%20response.md) of the channel}@}. {@{This form of equalizer}@} was first proposed by {@{[Robert Lucky](Robert%20Lucky.md)}@}. <!--SR:!2025-11-27,67,310!2026-07-19,246,330!2026-07-12,241,330!2026-08-04,259,330!2025-11-27,67,310-->

{@{The zero-forcing equalizer}@} applies {@{the inverse of the channel frequency response to the received signal}@}, to {@{restore the signal after the channel}@}.<sup>[\[1\]](#^ref-1)</sup> It has {@{many useful applications}@}. For example, it is studied heavily for {@{[IEEE 802.11n](IEEE%20802.11n.md) \(MIMO\)}@} where {@{knowing the channel allows recovery of the two or more streams}@} which will be {@{received on top of each other on each antenna}@}. {@{The name _zero-forcing_}@} corresponds to {@{bringing down the [intersymbol interference](intersymbol%20interference.md) \(ISI\) to zero}@} in {@{a noise-free case}@}. {@{This will be useful}@} when {@{ISI is significant compared to noise}@}. <!--SR:!2026-07-20,247,330!2026-07-10,239,330!2026-07-14,242,330!2026-07-29,255,330!2026-07-30,255,330!2026-07-12,241,330!2026-07-16,244,330!2026-07-13,241,330!2026-07-19,246,330!2026-08-06,260,330!2026-08-03,258,330!2026-07-06,236,330-->

For {@{a channel with [frequency response](frequency%20response.md) $F(f)$}@} {@{the zero-forcing equalizer $C(f)$}@} is constructed by {@{$C(f)=1/F(f)$}@}. Thus {@{the combination of channel and equalizer}@} gives {@{a flat frequency response and linear phase $F(f)C(f)=1$}@}. <!--SR:!2026-07-14,242,330!2026-07-29,255,330!2026-07-09,238,330!2026-07-02,232,330!2026-07-24,251,330-->

In {@{reality}@}, {@{zero-forcing equalization}@} {@{does not work in most applications}@}, for {@{the following reasons}@}: <!--SR:!2026-07-29,255,330!2026-07-07,237,330!2026-07-12,241,330!2026-07-04,234,330-->

1. Even though {@{the channel impulse response has finite length}@}, {@{the impulse response of the equalizer}@} needs to {@{be infinitely long}@} \(annotation: {@{The inverse of an casual FIR filter}@} is {@{an IRR filter}@}.\)
2. At {@{some frequencies}@} {@{the received signal may be weak}@}. To {@{compensate}@}, {@{the magnitude of the zero-forcing filter \("gain"\)}@} {@{grows very large}@}. As a consequence, {@{any noise added after the channel}@} gets {@{boosted by a large factor}@} and destroys {@{the overall signal-to-noise ratio}@}. Furthermore, the channel may have {@{zeros in its frequency response}@} that {@{cannot be inverted at all}@}. \({@{Gain \* 0}@} still {@{equals 0}@}\). <!--SR:!2025-11-21,62,310!2026-07-29,255,330!2025-11-22,63,310!2026-07-30,255,330!2026-08-07,261,330!2026-08-09,263,330!2026-07-07,237,330!2026-07-27,253,330!2025-11-27,67,310!2026-07-22,249,330!2025-11-27,67,310!2026-07-12,241,330!2026-07-18,246,330!2026-07-29,255,330!2026-07-17,245,330!2026-07-05,235,330!2025-11-27,67,310-->

{@{This second item \(annotation: noise amplification and zeros\)}@} is {@{often the more limiting condition}@}. {@{These problems are addressed}@} in {@{the linear [MMSE](minimum%20mean-square%20error.md) equalizer}@}<sup>[\[2\]](#^ref-2)</sup> by {@{making a small modification to the denominator of $C(f)$}@}: {@{$C(f)=1/(F(f)+k)$}@}, where k is {@{related to the channel response and the signal [SNR](signal-to-noise%20ratio.md)}@}. <!--SR:!2025-11-27,67,310!2026-07-29,255,330!2025-11-27,67,310!2026-07-28,254,330!2025-11-27,67,310!2025-11-20,61,310!2025-11-22,63,310-->

## algorithm

If {@{the channel response \(or [channel transfer function](transfer%20function.md)\) for a particular channel}@} is {@{H\(s\)}@} then {@{the input signal}@} is {@{multiplied by the [reciprocal](multiplicative%20inverse.md) of it}@}. This is intended to {@{remove the effect of channel from the received signal}@}, in particular {@{the [intersymbol interference](intersymbol%20interference.md) \(ISI\)}@}. <!--SR:!2026-08-04,259,330!2025-11-27,67,310!2026-07-15,243,330!2026-07-07,237,330!2026-07-07,237,330!2026-07-11,240,330-->

{@{The zero-forcing equalizer}@} {@{removes all ISI}@}, and is {@{ideal when the channel is noiseless}@}. However, when {@{the channel is noisy}@}, the zero-forcing equalizer will {@{amplify the noise greatly at frequencies _f_}@} where {@{the channel response H\(j2π<!-- markdown separator -->_f_\) has a small magnitude}@} \(i.e. {@{near zeroes of the channel}@}\) in the attempt to {@{invert the channel completely}@}. {@{A more balanced linear equalizer}@} in this case is {@{the __[minimum mean-square error](minimum%20mean-square%20error.md) equalizer__}@}, which {@{does not usually eliminate ISI completely}@} but instead {@{minimizes the total power of the noise and ISI components in the output}@}. <!--SR:!2026-07-07,237,330!2026-07-23,250,330!2025-11-27,67,310!2026-07-21,248,330!2026-07-13,241,330!2025-11-27,67,310!2025-11-21,62,310!2025-11-20,61,310!2026-07-12,241,330!2025-11-20,61,310!2026-07-24,251,330!2026-07-03,233,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/zero-forcing_equalizer) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFJon Mark and Weihua Zhuang2003"></a> Jon Mark and Weihua Zhuang \(2003\). "Ch. 4". _Wireless Communications and Networking_. Prentice Hall. p. 139. [ISBN](ISBN%20(identifier).md) [0-13-040905-7](https://en.wikipedia.org/wiki/Special:BookSources/0-13-040905-7). <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFJon Mark and Weihua Zhuang2003"></a> Jon Mark and Weihua Zhuang \(2003\). "Ch. 4". _Wireless Communications and Networking_. Prentice Hall. p. 143. [ISBN](ISBN%20(identifier).md) [0-13-040905-7](https://en.wikipedia.org/wiki/Special:BookSources/0-13-040905-7). <a id="^ref-2"></a>^ref-2

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Filter theory](https://en.wikipedia.org/wiki/Category:Filter%20theory)
