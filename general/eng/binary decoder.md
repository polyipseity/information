---
aliases:
  - binary decoder
  - binary decoders
tags:
  - flashcard/active/general/eng/binary_decoder
  - language/in/English
---

# binary decoder

<!-- | ![](../../archives/Wikimedia%20Commons/Question%20book-new.svg) | This article __needs additional citations for [verification](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)__. Please help [improve this article](https://en.wikipedia.org/wiki/Special:EditPage/Binary%20decoder) by [adding citations to reliable sources](https://en.wikipedia.org/wiki/Help:Referencing%20for%20beginners). Unsourced material may be challenged and removed._Find sources:_ ["Binary decoder"](https://www.google.com/search?as_eq=wikipedia&q=%22Binary+decoder%22) – [news](https://www.google.com/search?tbm=nws&q=%22Binary+decoder%22+-wikipedia&tbs=ar:1) __·__ [newspapers](https://www.google.com/search?&q=%22Binary+decoder%22&tbs=bkt:s&tbm=bks) __·__ [books](https://www.google.com/search?tbs=bks:1&q=%22Binary+decoder%22+-wikipedia) __·__ [scholar](https://scholar.google.com/scholar?q=%22Binary+decoder%22) __·__ [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Binary+decoder%22&acc=on&wc=on) _\(May 2009\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

In {@{[digital electronics](digital%20electronics.md)}@}, {@{a __binary decoder__}@} is {@{a [combinational logic](combinational%20logic.md) circuit that converts binary information from the n coded inputs to a maximum of 2<sup>n</sup> unique outputs}@}. They are used in {@{a wide variety of applications}@}, including {@{instruction decoding, data multiplexing and data demultiplexing, seven segment displays}@}, and as {@{[address decoders](address%20decoder.md) for [memory](memory.md) and [port-mapped I/O](port-mapped%20I_O.md)}@}. <!--SR:!2025-12-19,234,330!2026-03-02,290,330!2026-01-06,251,330!2026-02-21,281,330!2026-02-08,276,330!2026-02-02,272,330-->

There are {@{several types of binary decoders}@}, but in all cases a decoder is {@{an electronic circuit with multiple input and multiple output signals}@}, which {@{converts every unique combination of input states to a specific combination of output states}@}. In addition to {@{integer data inputs}@}, some decoders also have {@{one or more "enable" inputs}@}. When {@{the enable input is negated \(disabled\)}@}, {@{all decoder outputs are forced to their inactive states}@}. <!--SR:!2026-03-06,294,330!2026-02-01,271,330!2026-02-08,276,330!2026-02-01,271,330!2026-03-06,294,330!2026-02-07,276,330!2026-01-29,267,330-->

Depending on {@{its function}@}, a binary decoder will {@{convert binary information from n input signals to as many as 2<sup>n</sup> unique output signals}@}. Some decoders have {@{less than 2<sup>n</sup> output lines}@}; in such cases, {@{at least one output pattern may be repeated for different input values}@}. <!--SR:!2026-01-28,267,330!2025-12-19,234,330!2026-02-25,285,330!2026-03-01,289,330-->

A binary decoder is usually implemented as {@{either a stand-alone [integrated circuit](integrated%20circuit.md) \(IC\) or as part of a more complex IC}@}. In the latter case the decoder may be {@{synthesized by means of a [hardware description language](hardware%20description%20language.md)}@} such as {@{[VHDL](VHDL.md) or [Verilog](Verilog.md)}@}. {@{Widely used decoders}@} are often {@{available in the form of standardized ICs}@}. <!--SR:!2025-12-20,235,330!2026-01-06,251,330!2026-02-08,276,330!2026-02-06,275,330!2026-01-06,251,330-->

## types of decoders

### 1-of-n decoder

> {@{![A 2-to-4 line decoder](../../archives/Wikimedia%20Commons/Decoder%20Example.svg)}@}
>
> {@{A 2-to-4 line decoder}@} <!--SR:!2026-02-07,276,330!2026-01-11,255,330-->

{@{A 1-of-n binary decoder}@} has {@{n output bits}@}. This type of decoder asserts {@{exactly one of its n output bits, or none of them, for every integer input value}@}. {@{The "address" \(bit number\) of the activated output}@} is {@{specified by the integer input value}@}. For example, {@{output bit number 0 is selected}@} when {@{the integer value 0 is applied to the inputs}@}. <!--SR:!2026-02-07,276,330!2026-01-06,251,330!2026-02-01,271,330!2026-01-27,266,330!2026-02-01,270,330!2026-02-21,281,330!2026-01-31,269,330-->

Examples of this type of decoder include:

- A _3-to-8 line decoder_ ::@:: activates one of eight output bits for each input value from 0 to 7 — the range of integer values that can be expressed in three bits. Similarly, a _4-to-16 line decoder_ activates one of 16 outputs for each 4-bit input in the integer range \[0,15\]. <!--SR:!2026-02-05,274,330!2026-01-10,254,330-->
- A _BCD to decimal decoder_ ::@:: has ten output bits. It accepts an input value consisting of a [binary-coded decimal](binary-coded%20decimal.md) integer value and activates one specific, unique output for every input value in the range \[0,9\]. All outputs are held inactive when a non-decimal value is applied to the inputs. <!--SR:!2026-09-12,427,310!2026-03-01,289,330-->
- A [demultiplexer](demultiplexer.md#digital%20demultiplexers) ::@:: is a 1-of-n binary decoder that is used to route a data bit to one of its n outputs while all other outputs remain inactive. <!--SR:!2027-08-03,687,330!2026-01-29,268,330-->

### code translator

Code translators differ from {@{1-of-n decoders in that multiple output bits may be active at the same time}@}. An example of this is {@{a _seven-segment decoder_}@}, which converts {@{an integer into the combination of segment control signals needed to display the integer's value on a [seven-segment display](seven-segment%20display.md) digit}@}. <!--SR:!2026-01-11,255,330!2026-02-21,281,330!2026-02-25,285,330-->

One variant of seven-segment decoder is the _BCD to seven-segment decoder_, which translates a binary-coded decimal value into the corresponding segment control signals for input integer values 0 to 9. This decoder function is available in standard ICs such as the CMOS [4511](4511.md#4511%20BCD%20to%20seven-segment%20decoder).

### binary to unary decoder

A binary to unary decoder converts {@{each binary value to its associated [unary](unary%20coding.md) representation}@}. Unlike {@{the 1-of-n \(one-hot\) decoder, multiple output bits can be asserted for each input value}@}. These decoders can be used in {@{[DACs](digital-to-analog%20converter.md) where each bit is equally weighted}@}, and {@{circuits that require a binary [mask](mask%20(computing).md) or window}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2026-03-02,290,330!2026-01-30,268,330!2026-02-25,285,330!2026-02-02,272,330-->

## see also

>![Wiktionary logo](../../archives/Wikimedia%20Commons/Wiktionary-logo-en-v2.svg) Look up ___[decoder](https://en.wiktionary.org/wiki/decoder)___ in Wiktionary, the free dictionary.

- [Multiplexer](multiplexer.md)
- [One-hot](one-hot.md), ::@:: the format of the 1-of-n decoder's output \(or the unencoded output of a ring counter\) <!--SR:!2026-02-25,285,330!2026-03-06,294,330-->
- [Priority encoder](priority%20encoder.md)
- [Sum-addressed decoder](sum-addressed%20decoder.md)

## references

This text incorporates [content](https://en.wikipedia.org/wiki/binary_decoder) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. [US patent 5313300A](https://patents.google.com/patent/US5313300A/en), "Binary to unary decoder for a video digital to analog converter", issued 1992-08-10 <a id="^ref-1"></a>^ref-1

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Digital circuits](https://en.wikipedia.org/wiki/Category:Digital%20circuits)
