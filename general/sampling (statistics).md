---
aliases:
  - sample
  - samples
  - sampling
tags:
  - flashcard/active/general/sampling__statistics_
  - language/in/English
---

# sampling

In [statistics](statistics.md), [quality assurance](quality%20assurance.md), and [survey methodology](survey%20methodology.md), __sampling__ is {@{the selection of a subset or a __statistical sample__ (termed __sample__ for short) of individuals from within a [statistical population](statistical%20population.md) to estimate characteristics of the whole population}@}. The subset is {@{meant to reflect the whole population and statisticians attempt to collect samples that are representative of the population}@}. Sampling has {@{lower costs and faster data collection compared to recording data from the entire population}@}, and thus, it can {@{provide insights in cases where it is infeasible to measure an entire population}@}. <!--SR:!2025-07-04,236,330!2025-05-27,189,310!2024-12-01,62,270!2025-07-19,247,330-->

Each [observation](observation.md) measures {@{one or more properties (such as weight, location, colour or mass) of independent objects or individuals}@}. In [survey sampling](survey%20sampling.md), {@{weights can be applied to the data to adjust for the sample design, particularly in [stratified sampling](stratified%20sampling.md)}@}. Results from {@{[probability theory](probability%20theory.md) and [statistical theory](statistical%20theory.md) are employed to guide the practice}@}. In business and medical research, sampling is widely used {@{for gathering information about a population}@}. [Acceptance sampling](acceptance%20sampling.md) is {@{used to determine if a production lot of material meets the governing [specifications](specification%20(technical%20standard).md)}@}. <!--SR:!2025-02-14,121,290!2024-12-04,73,310!2024-12-03,72,310!2025-08-07,263,330!2024-11-28,67,310-->

## sampling frame

- see: [sampling frame](sampling%20frame.md)

In {@{the most straightforward case, such as the sampling of a batch of material from production (acceptance sampling by lots)}@}, it would be {@{most desirable to identify and measure every single item in the population and to include any one of them in our sample}@}. However, in {@{the more general case this is not usually possible or practical}@}. There is {@{no way to identify all rats}@} in the set of all rats. Where voting is not compulsory, {@{there is no way to identify which people will vote at a forthcoming election (in advance of the election)}@}. These imprecise populations are {@{not amenable to sampling in any of the ways below and to which we could apply statistical theory}@}. <!--SR:!2025-08-13,267,330!2025-04-21,163,310!2025-07-26,253,330!2025-07-28,254,330!2025-06-28,230,330!2025-08-19,269,330-->

As a remedy, {@{we seek a [sampling frame](sampling%20frame.md) which has the property that we can identify every single element and include any in our sample}@}. The most straightforward type of frame is {@{a list of elements of the population (preferably the entire population) with appropriate contact information}@}. For example, in an [opinion poll](opinion%20poll.md), possible sampling frames include {@{an [electoral register](electoral%20roll.md) and a [telephone directory](telephone%20directory.md)}@}. <!--SR:!2024-12-13,66,270!2025-07-07,238,330!2025-04-09,167,310-->

A __probability sample__ is {@{a sample in which every unit in the population has a chance (greater than zero) of being selected in the sample, and this probability can be accurately determined}@}. The combination of these traits makes it possible to {@{produce unbiased estimates of population totals, by weighting sampled units according to their probability of selection}@}. <!--SR:!2025-07-03,234,330!2025-02-28,121,290-->

> [!example] example
>
> We want to estimate the total income of adults living in a given street. We visit each household in that street, identify all adults living there, and {@{randomly select one adult from each household. (For example, we can allocate each person a random number, generated from a [uniform distribution](continuous%20uniform%20distribution.md) between 0 and 1, and select the person with the highest number in each household.)}@} We then interview the selected person and find their income.
>
> People living on their own are {@{certain to be selected, so we simply add their income to our estimate of the total}@}. But {@{a person living in a household of two adults has only a one-in-two chance of selection}@}. To reflect this, when we come to such a household, we would {@{count the selected person's income twice towards the total}@}. (The person who _is_ selected from that household can be loosely viewed as {@{also representing the person who _isn't_ selected}@}.) <!--SR:!2025-07-11,241,330!2025-03-08,140,310!2024-11-30,69,310!2024-11-30,69,310!2025-09-01,280,330-->

In the above example, {@{not everybody has the same probability of selection; what makes it a probability sample is the fact that each person's probability is known}@}. When {@{every element in the population _does_ have the same probability of selection}@}, this is {@{known as an 'equal probability of selection' (EPS) design}@}. Such designs are also referred to as {@{'self-weighting' because all sampled units are given the same weight}@}. <!--SR:!2025-08-17,268,330!2024-11-29,68,310!2025-07-15,245,330!2025-06-23,227,330-->

Probability sampling includes: {@{[simple random sampling](simple%20random%20sample.md), [systematic sampling](systematic%20sampling.md), [stratified sampling](stratified%20sampling.md), probability-proportional-to-size sampling, and [cluster](cluster%20sampling.md) or [multistage sampling](multistage%20sampling.md)}@}. These various ways of probability sampling have two things in common: <!--SR:!2024-12-05,66,270-->

1. (probability sampling) every element ::@:: Every element has a known nonzero probability of being sampled and <!--SR:!2025-08-13,264,330!2025-07-03,235,330-->
2. (probability sampling) at some point ::@:: involves random selection at some point. <!--SR:!2025-09-05,283,330!2025-02-16,122,290-->

### nonprobability sampling

- see: [nonprobability sampling](nonprobability%20sampling.md)

__Nonprobability sampling__ is {@{any sampling method where some elements of the population have _no_ chance of selection (these are sometimes referred to as 'out of coverage'/'undercovered')}@}, or {@{where the probability of selection cannot be accurately determined}@}. It involves {@{the selection of elements based on assumptions regarding the population of interest, which forms the criteria for selection}@}. Hence, because {@{the selection of elements is nonrandom}@}, nonprobability sampling {@{does not allow the estimation of sampling errors}@}. These conditions give rise to {@{[exclusion bias](selection%20bias.md), placing limits on how much information a sample can provide about the population}@}. Information about {@{the relationship between sample and population is limited}@}, making it difficult to {@{extrapolate from the sample to the population}@}. <!--SR:!2025-04-25,173,310!2024-12-02,71,310!2025-05-23,186,310!2025-07-10,241,330!2025-04-18,172,310!2025-05-29,188,290!2025-08-17,270,330!2025-07-18,246,330-->

> [!example] example
>
> We visit every household in a given street, and interview the first person to answer the door. In any household with more than one occupant, this is {@{a nonprobability sample}@}, because {@{some people are more likely to answer the door (e.g. an unemployed person who spends most of their time at home is more likely to answer than an employed housemate who might be at work when the interviewer calls)}@} and {@{it's not practical to calculate these probabilities}@}. <!--SR:!2024-11-29,68,310!2025-05-09,188,310!2025-04-20,173,310-->

Nonprobability sampling methods include {@{[convenience sampling](convenience%20sampling.md), [quota sampling](quota%20sampling.md), and [purposive sampling](nonprobability%20sampling.md)}@}. In addition, nonresponse effects {@{may turn _any_ probability design into a nonprobability design if the characteristics of nonresponse are not well understood}@}, since {@{nonresponse effectively modifies each element's probability of being sampled}@}. <!--SR:!2025-09-04,282,330!2025-01-17,90,270!2025-08-10,262,330-->

## errors in sample surveys

- see: [sampling error](sampling%20error.md)

Survey results are {@{typically subject to some error}@}. Total errors can be classified into {@{sampling errors and non-sampling errors}@}. The term "error" here includes {@{systematic biases as well as random errors}@}. <!--SR:!2025-07-25,252,330!2025-03-21,149,310!2025-08-27,278,330-->

### sampling errors and biases

Sampling errors and biases are {@{induced by the sample design}@}. They include {@{selection bias and random sampling errors}@}: <!--SR:!2025-08-03,259,330!2025-08-02,259,330-->

- [selection bias](selection%20bias.md) ::@:: When the true selection probabilities differ from those assumed in calculating the results. <!--SR:!2025-06-29,232,330!2025-08-01,258,330-->
- [random sampling error](sampling%20error.md) ::@:: Random variation in the results due to the elements in the sample being selected at random. <!--SR:!2025-08-14,265,330!2024-12-01,70,310-->

### non-sampling errors

- see: [non-sampling error](non-sampling%20error.md)

Non-sampling errors are other errors which can impact final survey estimates, caused by problems in data collection, processing, or sample design. Such errors may include {@{over-coverage, under-coverage, measurement error, processing error, participation bias, etc.}@}: <!--SR:!2025-01-29,106,290-->

- over-coverage ::@:: inclusion of data from outside of the population <!--SR:!2024-12-01,70,310!2024-12-03,72,310-->
- under-coverage ::@:: sampling frame does not include elements in the population <!--SR:!2025-05-17,193,310!2025-08-16,269,330-->
- measurement error ::@:: e.g. when respondents misunderstand a question, or find it difficult to answer <!--SR:!2025-06-06,206,310!2024-11-29,68,310-->
- processing error ::@:: mistakes in data coding <!--SR:!2025-08-26,275,330!2025-08-18,270,330-->
- [non-response or participation bias](participation%20bias.md) ::@:: failure to obtain complete data from all selected individuals <!--SR:!2025-05-30,207,330!2025-08-03,259,330-->

After sampling, {@{a review is held of the exact process followed in sampling, rather than that intended}@}, in order to {@{study any effects that any divergences might have on subsequent analysis}@}. <!--SR:!2025-03-29,140,290!2025-05-28,187,310-->

A particular problem involves {@{_non-response_}@}. Two major types of non-response exist: {@{unit non-response and item non-response}@}. <!--SR:!2024-11-28,67,310!2025-08-22,272,330-->

- unit non-response ::@:: lack of completion of any part of the survey <!--SR:!2025-07-14,243,330!2025-09-11,288,330-->
- item non-response ::@:: submission or participation in survey but failing to complete one or more components/questions of the survey <!--SR:!2025-04-11,166,310!2025-08-24,276,330-->

In [survey sampling](survey%20sampling.md), many of the individuals identified as part of the sample {@{may be unwilling to participate, not have the time to participate ([opportunity cost](opportunity%20cost.md)), or survey administrators may not have been able to contact them}@}. In this case, there is {@{a risk of differences between respondents and nonrespondents, leading to biased estimates of population parameters}@}. This is often addressed by {@{improving survey design, offering incentives, and conducting follow-up studies which make a repeated attempt to contact the unresponsive and to characterize their similarities and differences with the rest of the frame}@}. The effects can also be mitigated by {@{weighting the data (when population benchmarks are available) or by imputing data based on answers to other questions}@}. Non-response is {@{particularly a problem in internet sampling}@}. Reasons for this problem may include {@{improperly designed surveys, over-surveying (or survey fatigue), and the fact that potential participants may have multiple e-mail addresses, which they do not use anymore or do not check regularly}@}. <!--SR:!2024-12-04,73,310!2025-01-18,92,270!2024-12-22,73,270!2025-09-02,281,330!2025-06-23,226,330!2025-08-27,276,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/sampling_(statistics)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
