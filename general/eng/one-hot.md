---
aliases:
  - one-cold
  - one-cold encoding
  - one-cold encodings
  - one-hot
  - one-hot encoding
  - one-hot encodings
tags:
  - flashcard/active/general/eng/one-hot
  - language/in/English
---

# one-hot

| {@{[Decimal](decimal.md)}@} | {@{[Binary](binary%20number.md)}@} | {@{[Unary](unary%20numeral%20system.md)}@} | {@{One-hot}@}  |
| --------------------------- | ---------------------------------- | ------------------------------------------ | -------------- |
| {@{0}@}                     | {@{000}@}                          | {@{00000000}@}                             | {@{00000001}@} |
| {@{1}@}                     | {@{001}@}                          | {@{00000001}@}                             | {@{00000010}@} |
| {@{2}@}                     | {@{010}@}                          | {@{00000011}@}                             | {@{00000100}@} |
| {@{3}@}                     | {@{011}@}                          | {@{00000111}@}                             | {@{00001000}@} |
| {@{4}@}                     | {@{100}@}                          | {@{00001111}@}                             | {@{00010000}@} |
| {@{5}@}                     | {@{101}@}                          | {@{00011111}@}                             | {@{00100000}@} |
| {@{6}@}                     | {@{110}@}                          | {@{00111111}@}                             | {@{01000000}@} |
| {@{7}@}                     | {@{111}@}                          | {@{01111111}@}                             | {@{10000000}@} | <!--SR:!2025-02-22,16,290!2025-02-20,14,290!2025-02-22,16,290!2025-02-20,14,290!2025-02-21,15,290!2025-02-20,14,290!2025-02-21,15,290!2025-02-21,15,290!2025-02-22,16,290!2025-02-20,14,290!2025-02-20,14,290!2025-02-22,16,290!2025-02-21,15,290!2025-02-20,14,290!2025-02-21,15,290!2025-02-21,15,290!2025-02-22,16,290!2025-02-20,14,290!2025-02-20,14,290!2025-02-22,16,290!2025-02-22,16,290!2025-02-22,16,290!2025-02-22,16,290!2025-02-20,14,290!2025-02-21,15,290!2025-02-21,15,290!2025-02-21,15,290!2025-02-22,16,290!2025-02-20,14,290!2025-02-22,16,290!2025-02-21,15,290!2025-02-20,14,290!2025-02-20,14,290!2025-02-20,14,290!2025-02-20,14,290!2025-02-21,15,290-->

In {@{[digital circuits](digital%20circuits.md) and [machine learning](machine%20learning.md)}@}, {@{a __one-hot__}@} is {@{a group of [bits](bit.md) among which the legal combinations of values are only those with a single high \(1\) bit and all the others low \(0\)}@}.<sup>[\[1\]](#^ref-1)</sup> {@{A similar implementation in which all bits are '1' except one '0'}@} is sometimes called {@{__one-cold__}@}.<sup>[\[2\]](#^ref-2)</sup> In {@{[statistics](statistics.md)}@}, {@{[dummy variables](dummy%20variable%20(statistics).md)}@} represent {@{a similar technique for representing [categorical data](categorical%20data.md)}@}. <!--SR:!2025-02-21,15,290!2025-02-22,16,290!2025-02-20,14,290!2025-02-21,15,290!2025-02-22,16,290!2025-02-20,14,290!2025-02-21,15,290!2025-02-21,15,290-->

## applications

### digital circuitry

One-hot encoding is often used for {@{indicating the state of a [state machine](state%20machine.md)}@}. When {@{using [binary](binary%20number.md)}@}, {@{a [decoder](binary%20decoder.md) is needed to determine the state}@}. A one-hot state machine, {@{however, does not need a decoder}@} as {@{the state machine is in the _n_<!-- markdown separator -->th state if, and only if, the _n_<!-- markdown separator -->th bit is high}@}. <!--SR:!2025-02-21,15,290!2025-02-22,16,290!2025-02-20,14,290!2025-02-21,15,290!2025-02-21,15,290-->

{@{A [ring counter](ring%20counter.md) with 15 sequentially ordered states}@} is {@{an example of a state machine}@}. {@{A 'one-hot' implementation}@} would have {@{15 [flip flops](flip%20flop%20(electronics).md) chained in series}@} with {@{the Q output of each flip flop connected to the D input of the next and the D input of the first flip flop connected to the Q output of the 15th flip flop}@}. {@{The first flip flop in the chain}@} {@{represents the first state}@}, {@{the second represents the second state, and so on to the 15th flip flop, which represents the last state}@}. Upon {@{reset of the state machine}@} {@{all of the flip flops are reset to '0' except the first in the chain, which is set to '1'}@}. {@{The next clock edge arriving at the flip flops}@} {@{advances the one 'hot' bit to the second flip flop}@}. {@{The 'hot' bit advances in this way}@} {@{until the 15th state, after which the state machine returns to the first state}@}. <!--SR:!2025-02-21,15,290!2025-02-21,15,290!2025-02-22,16,290!2025-02-21,15,290!2025-03-03,19,250!2025-02-20,14,290!2025-02-20,14,290!2025-02-21,15,290!2025-02-21,15,290!2025-02-22,16,290!2025-02-22,16,290!2025-02-21,15,290!2025-02-22,16,290!2025-02-20,14,290-->

{@{An [address decoder](address%20decoder.md)}@} {@{converts from binary to one-hot representation}@}. {@{A [priority encoder](priority%20encoder.md)}@} {@{converts from one-hot representation to binary}@}. <!--SR:!2025-02-22,16,290!2025-02-20,14,290!2025-02-22,16,290!2025-02-22,16,290-->

#### comparison with other encoding methods

##### advantages

- Determining the state ::@:: has a low and constant cost of accessing one [flip-flop](flip-flop%20(electronics).md) <!--SR:!2025-02-20,14,290!2025-02-21,15,290-->
- Changing the state ::@:: has the constant cost of accessing two flip-flops <!--SR:!2025-02-21,15,290!2025-02-21,15,290-->
- (annotation: design) Easy to ::@:: design and modify <!--SR:!2025-02-21,15,290!2025-03-26,38,290-->
- (annotation: states) Easy to ::@:: detect illegal states <!--SR:!2025-02-21,15,290!2025-02-20,14,290-->
- Takes advantage of ::@:: an [FPGA](field-programmable%20gate%20array.md)'s abundant flip-flops <!--SR:!2025-02-20,14,290!2025-02-22,16,290-->
- Using a one-hot implementation ::@:: typically allows a state machine to run at a faster clock rate than any other encoding of that state machine<sup>[\[3\]](#^ref-3)</sup> <!--SR:!2025-02-20,14,290!2025-02-22,16,290-->

##### disadvantages

- Requires ::@:: more flip-flops than other encodings, making it impractical for [PAL](Programmable%20Array%20Logic.md) devices <!--SR:!2025-02-21,15,290!2025-02-17,11,270-->
- Many of the states ::@:: are illegal<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2025-02-22,16,290!2025-02-21,15,290-->

### natural language processing

In {@{[natural language processing](natural%20language%20processing.md)}@}, {@{a one-hot vector}@} is {@{a 1 × _N_ matrix \(vector\) used to distinguish each word in a vocabulary from every other word in the vocabulary}@}.<sup>[\[5\]](#^ref-5)</sup> The vector consists of {@{0s in all cells with the exception of a single 1 in a cell used uniquely to identify the word}@}. One-hot encoding ensures that {@{machine learning does not assume that higher numbers are more important}@}. For example, {@{the value '8' is bigger than the value '1'}@}, but {@{that does not make '8' more important than '1'}@}. The same is {@{true for words: the value 'laughter' is not more important than 'laugh'}@}. <!--SR:!2025-02-21,15,290!2025-02-22,16,290!2025-02-20,14,290!2025-02-20,14,290!2025-02-20,14,290!2025-02-20,14,290!2025-02-22,16,290!2025-02-22,16,290-->

### machine learning and statistics

In {@{machine learning}@}, one-hot encoding is {@{a frequently used method to deal with categorical data}@}. Because {@{many machine learning models need their input variables to be numeric}@}, {@{categorical variables need to be transformed in the pre-processing part}@}. <sup>[\[6\]](#^ref-6)</sup> <!--SR:!2025-02-21,15,290!2025-02-22,16,290!2025-02-22,16,290!2025-02-21,15,290-->

> {@{__Label Encoding__}@}
>
> | Food Name | {@{Categorical \#}@} | Calories |
> | --------- | -------------------- | -------- |
> | Apple     | {@{1}@}              | 95       |
> | Chicken   | {@{2}@}              | 231      |
> | Broccoli  | {@{3}@}              | 50       |
>
> {@{__One Hot Encoding__}@}
>
> | {@{Apple}@} | {@{Chicken}@} | {@{Broccoli}@} | Calories |
> | ----------- | ------------- | -------------- | -------- |
> | 1           | 0             | 0              | 95       |
> | 0           | 1             | 0              | 231      |
> | 0           | 0             | 1              | 50       | <!--SR:!2025-02-20,14,290!2025-02-21,15,290!2025-02-20,14,290!2025-02-22,16,290!2025-02-21,15,290!2025-02-21,15,290!2025-02-20,14,290!2025-02-20,14,290!2025-02-20,14,290-->

{@{Categorical data}@} can be {@{either [nominal](nominal%20number.md) or [ordinal](ordinal%20number.md)}@}.<sup>[\[7\]](#^ref-7)</sup> Ordinal data has {@{a ranked order for its values}@} and can {@{therefore be converted to numerical data through ordinal encoding}@}.<sup>[\[8\]](#^ref-8)</sup> An example of ordinal data would be {@{the ratings on a test ranging from A to F}@}, which could be {@{ranked using numbers from 6 to 1}@}. Since {@{there is no quantitative relationship between nominal variables' individual values}@}, using ordinal encoding can {@{potentially create a fictional ordinal relationship in the data}@}.<sup>[\[9\]](#^ref-9)</sup> Therefore, {@{one-hot encoding is often applied to nominal variables}@}, in order to {@{improve the performance of the algorithm}@}. <!--SR:!2025-02-22,16,290!2025-02-20,14,290!2025-02-22,16,290!2025-02-20,14,290!2025-02-21,15,290!2025-02-20,14,290!2025-02-22,16,290!2025-02-21,15,290!2025-02-22,16,290!2025-03-25,37,290-->

For {@{each unique value in the original categorical column}@}, {@{a new column is created in this method}@}. {@{These dummy variables}@} are then {@{filled up with zeros and ones \(1 meaning TRUE, 0 meaning FALSE\)}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> <!--SR:!2025-02-20,14,290!2025-02-20,14,290!2025-02-20,14,290!2025-02-21,15,290-->

Because {@{this process creates multiple new variables}@}, it is prone to {@{creating a 'big p' problem \(too many predictors\) if there are many unique values in the original column}@}. {@{Another downside of one-hot encoding}@} is that it {@{causes multicollinearity between the individual variables, which potentially reduces the model's accuracy}@}.<sup>\[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation%20needed)_\]</sup> <!--SR:!2025-02-22,16,290!2025-02-22,16,290!2025-02-21,15,290!2025-02-22,16,290-->

Also, if {@{the categorical variable is an output variable}@}, you may want to {@{convert the values back into a categorical form in order to present them in your application}@}.<sup>[\[10\]](#^ref-10)</sup> <!--SR:!2025-02-22,16,290!2025-02-22,16,290-->

In {@{practical usage}@}, this transformation is often directly performed by {@{a function that takes categorical data as an input and outputs the corresponding dummy variables}@}. An example would be {@{the dummyVars function of the Caret library in R}@}.<sup>[\[11\]](#^ref-11)</sup> <!--SR:!2025-02-22,16,290!2025-02-22,16,290!2025-02-22,16,290-->

## see also

- [Constant-weight code](constant-weight%20code.md) – ::@:: Method for encoding data in communications, where a constant number of bits are set <!--SR:!2025-02-20,14,290!2025-02-21,15,290-->
- [Two-out-of-five code](two-out-of-five%20code.md) – ::@:: Error-detection code for decimal digits, widely used in barcoding and at one time in telephone exchanges <!--SR:!2025-02-18,12,270!2025-03-24,37,290-->
- [Bi-quinary coded decimal](bi-quinary%20coded%20decimal.md) – ::@:: Numeral encoding scheme <!--SR:!2025-02-17,11,270!2025-02-22,16,290-->
- [Gray code](gray%20code.md) – ::@:: Ordering of binary values, used for positioning and error correction <!--SR:!2025-02-22,16,290!2025-02-20,14,290-->
- [Kronecker delta](Kronecker%20delta.md) – ::@:: Mathematical function of two variables; outputs 1 if they are equal, 0 otherwise <!--SR:!2025-02-20,14,290!2025-02-21,15,290-->
- [Indicator vector](indicator%20vector.md)
- [Serial decimal](serial%20decimal.md) – ::@:: computer numeric representation is one in which ten bits are reserved for each digit <!--SR:!2025-02-22,16,290!2025-02-18,12,270-->
- [Single-entry vector](single-entry%20vector.md) – ::@:: Concept in mathematics <!--SR:!2025-02-21,15,290!2025-02-20,14,290-->
- [Unary numeral system](unary%20numeral%20system.md) – ::@:: Base-1 numeral system <!--SR:!2025-02-20,14,290!2025-02-21,15,290-->
- [Uniqueness quantification](uniqueness%20quantification.md) – ::@:: Logical property of being the one and only object satisfying a condition <!--SR:!2025-03-27,39,290!2025-02-22,16,290-->
- [XOR gate](XOR%20gate.md) – ::@:: Logic gate <!--SR:!2025-02-21,15,290!2025-02-20,14,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/one-hot) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. <a id="CITEREFHarris2012"></a> Harris, David and Harris, Sarah \(2012-08-07\). _Digital design and computer architecture_ \(2nd ed.\). San Francisco, Calif.: Morgan Kaufmann. p. 129. [ISBN](ISBN%20(identifier).md) [978-0-12-394424-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-12-394424-5). <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFHarragGueliani2020"></a> Harrag, Fouzi; Gueliani, Selmene \(2020\). "Event Extraction Based on Deep Learning in Food Hazard Arabic Texts". [arXiv](ArXiv%20(identifier).md):[2008.05014](https://arxiv.org/abs/2008.05014). `{{[cite journal](https://en.wikipedia.org/wiki/Template:Cite%20journal)}}`: Cite journal requires `|journal=` \([help](https://en.wikipedia.org/wiki/Help:CS1%20errors#missing%20periodical)\) <a id="^ref-2"></a>^ref-2
3. Xilinx. ["HDL Synthesis for FPGAs Design Guide"](http://www.xilinx.com/txpatches/pub/documentation/xactstep6/hdlsynth.pdf). section 3.13: "Encoding State Machines". Appendix A: "Accelerate FPGA Macros with One-Hot Approach". 1995. <a id="^ref-3"></a>^ref-3
4. <a id="CITEREFCohen2002"></a> Cohen, Ben \(2002\). _Real Chip Design and Verification Using Verilog and VHDL_. Palos Verdes Peninsula, CA, US: VhdlCohen Publishing. p. 48. [ISBN](ISBN%20(identifier).md) [0-9705394-2-8](https://en.wikipedia.org/wiki/Special:BookSources/0-9705394-2-8). <a id="^ref-4"></a>^ref-4
5. <a id="CITEREFArnaudElbattahGignonDequen2021"></a> Arnaud, Émilien; Elbattah, Mahmoud; Gignon, Maxime; Dequen, Gilles \(August 2021\). [_NLP-Based Prediction of Medical Specialties at Hospital Admission Using Triage Notes_](https://ieeexplore.ieee.org/document/9565791). 2021 IEEE 9th International Conference on Healthcare Informatics \(ICHI\). [Victoria, British Columbia](Victoria,%20British%20Columbia.md). pp. 548–553. [doi](doi%20(identifier).md):[10.1109/ICHI52183.2021.00103](https://doi.org/10.1109%2FICHI52183.2021.00103). Retrieved 2022-05-22. <a id="^ref-5"></a>^ref-5
6. Brownlee, Jason. \(2017\). "Why One-Hot Encode Data in Machine Learning?". Machinelearningmastery. [https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/) <a id="^ref-6"></a>^ref-6
7. Stevens, S. S. \(1946\). “On the Theory of Scales of Measurement”. Science, New Series, 103.2684, pp. 677–680. [http://www.jstor.org/stable/1671815](http://www.jstor.org/stable/1671815). <a id="^ref-7"></a>^ref-7
8. Brownlee, Jason. \(2020\). "Ordinal and One-Hot Encodings for Categorical Data". Machinelearningmastery. [https://machinelearningmastery.com/one-hot-encoding-for-categorical-data//](https://machinelearningmastery.com/one-hot-encoding-for-categorical-data//) <a id="^ref-8"></a>^ref-8
9. Brownlee, Jason. \(2020\). "Ordinal and One-Hot Encodings for Categorical Data". Machinelearningmastery. [https://machinelearningmastery.com/one-hot-encoding-for-categorical-data//](https://machinelearningmastery.com/one-hot-encoding-for-categorical-data//) <a id="^ref-9"></a>^ref-9
10. Brownlee, Jason. \(2017\). "Why One-Hot Encode Data in Machine Learning?". Machinelearningmastery. [https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/) <a id="^ref-10"></a>^ref-10
11. Kuhn, Max. “dummyVars”. RDocumentation. [https://www.rdocumentation.org/packages/caret/versions/6.0-86/topics/dummyVars](https://www.rdocumentation.org/packages/caret/versions/6.0-86/topics/dummyVars) <a id="^ref-11"></a>^ref-11

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Digital electronics](https://en.wikipedia.org/wiki/Category:Digital%20electronics)
> - [1 \(number\)](https://en.wikipedia.org/wiki/Category:1%20%28number%29)
