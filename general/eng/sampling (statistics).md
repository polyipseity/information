---
aliases:
  - sample
  - samples
  - sampling
tags:
  - flashcard/active/general/eng/sampling__statistics_
  - language/in/English
---

# sampling

In [statistics](statistics.md), [quality assurance](quality%20assurance.md), and [survey methodology](survey%20methodology.md), __sampling__ is {@{the selection of a subset or a __statistical sample__ (termed __sample__ for short) of individuals from within a [statistical population](statistical%20population.md) to estimate characteristics of the whole population}@}. The subset is {@{meant to reflect the whole population and statisticians attempt to collect samples that are representative of the population}@}. Sampling has {@{lower costs and faster data collection compared to recording data from the entire population}@}, and thus, it can {@{provide insights in cases where it is infeasible to measure an entire population}@}. <!--SR:!2028-06-11,1073,350!2027-01-03,586,310!2028-03-10,957,310!2028-08-17,1124,350-->

Each [observation](observation.md) measures {@{one or more properties \(such as weight, location, colour or mass\) of independent objects or individuals}@}. In {@{[survey sampling](survey%20sampling.md)}@}, weights can be {@{applied to the data to adjust for the sample design, particularly in [stratified sampling](stratified%20sampling.md)}@}. Results from {@{[probability theory](probability%20theory.md) and [statistical theory](statistical%20theory.md) are employed to guide the practice}@}. In business and medical research, sampling is widely used {@{for gathering information about a population}@}. [Acceptance sampling](acceptance%20sampling.md) is {@{used to determine if a production lot of material meets the governing [specifications](specification%20(technical%20standard).md)}@}. <!--SR:!2026-06-20,491,310!2029-09-14,1431,350!2029-08-31,1421,350!2028-11-16,1197,350!2029-05-18,1339,350!2026-03-31,141,407-->

## sampling frame

- see: [sampling frame](sampling%20frame.md)

In {@{the most straightforward case}@}, such as the sampling of {@{a batch of material from production \(acceptance sampling by lots\)}@}, it would be most desirable to {@{identify and measure every single item in the population and to include any one of them in our sample}@}. However, in {@{the more general case}@} this is {@{not usually possible or practical}@}. There is {@{no way to identify all rats}@} in {@{the set of all rats}@}. Where {@{voting is not compulsory}@}, there is {@{no way to identify which people will vote at a forthcoming election \(in advance of the election\)}@}. These imprecise populations are {@{not amenable to sampling in any of the ways below and to which we could apply statistical theory}@}. <!--SR:!2028-12-09,1214,350!2027-03-21,699,330!2028-09-19,1151,350!2028-09-26,1156,350!2028-05-18,1054,350!2029-01-01,1231,350!2027-10-11,638,411!2027-10-14,641,411!2027-10-15,642,411!2027-10-12,639,411-->

As a remedy, {@{we seek a [sampling frame](sampling%20frame.md) which has the property that we can identify every single element and include any in our sample}@}. The most straightforward type of frame is {@{a list of elements of the population (preferably the entire population) with appropriate contact information}@}. For example, in an [opinion poll](opinion%20poll.md), possible sampling frames include {@{an [electoral register](electoral%20roll.md) and a [telephone directory](telephone%20directory.md)}@}. <!--SR:!2027-04-07,664,290!2028-06-28,1083,350!2027-03-25,715,330-->

A __probability sample__ is {@{a sample in which every unit in the population has a chance (greater than zero) of being selected in the sample, and this probability can be accurately determined}@}. The combination of these traits makes it possible to {@{produce unbiased estimates of population totals, by weighting sampled units according to their probability of selection}@}. <!--SR:!2028-06-05,1068,350!2026-07-06,493,310-->

> [!example] example
>
> We want to estimate the total income of adults living in a given street. We visit each household in that street, identify all adults living there, and {@{randomly select one adult from each household. (For example, we can allocate each person a random number, generated from a [uniform distribution](continuous%20uniform%20distribution.md) between 0 and 1, and select the person with the highest number in each household.)}@} We then interview the selected person and find their income.
>
> People living on their own are {@{certain to be selected, so we simply add their income to our estimate of the total}@}. But {@{a person living in a household of two adults has only a one-in-two chance of selection}@}. To reflect this, when we come to such a household, we would {@{count the selected person's income twice towards the total}@}. (The person who _is_ selected from that household can be loosely viewed as {@{also representing the person who _isn't_ selected}@}.) <!--SR:!2028-07-11,1096,350!2026-10-30,601,330!2028-05-25,976,330!2029-07-09,1379,350!2029-03-02,1278,350-->

In the above example, {@{not everybody has the same probability of selection}@}; {@{what makes it a probability sample}@} is the fact that {@{each person's probability is known}@}. When {@{every element in the population _does_ have the same probability of selection}@}, this is known as {@{an 'equal probability of selection' (EPS) design}@}. Such designs are also referred to as {@{'self-weighting' because all sampled units are given the same weight}@}. <!--SR:!2028-12-24,1225,350!2029-06-03,1349,350!2028-08-05,1117,350!2028-04-24,1036,350!2027-05-08,479,394!2027-02-17,435,394-->

Probability sampling includes: {@{[simple random sampling](simple%20random%20sample.md), [systematic sampling](systematic%20sampling.md), [stratified sampling](stratified%20sampling.md), probability-proportional-to-size sampling, and [cluster](cluster%20sampling.md) or [multistage sampling](multistage%20sampling.md)}@}. These various ways of probability sampling have two things in common: <!--SR:!2027-04-06,674,290-->

1. (probability sampling) every element ::@:: Every element has a known nonzero probability of being sampled and <!--SR:!2028-11-26,1201,350!2028-06-06,1069,350-->
2. (probability sampling) at some point ::@:: involves random selection at some point. <!--SR:!2029-03-20,1292,350!2026-06-26,495,310-->

### nonprobability sampling

- see: [nonprobability sampling](nonprobability%20sampling.md)

__Nonprobability sampling__ is {@{any sampling method where some elements of the population have _no_ chance of selection (these are sometimes referred to as 'out of coverage'/'undercovered')}@}, or {@{where the probability of selection cannot be accurately determined}@}. It involves {@{the selection of elements based on assumptions regarding the population of interest, which forms the criteria for selection}@}. Hence, because {@{the selection of elements is nonrandom}@}, nonprobability sampling {@{does not allow the estimation of sampling errors}@}. These conditions give rise to {@{[exclusion bias](selection%20bias.md), placing limits on how much information a sample can provide about the population}@}. Information about {@{the relationship between sample and population is limited}@}, making it difficult to {@{extrapolate from the sample to the population}@}. <!--SR:!2027-05-10,745,330!2029-09-02,1422,350!2027-08-05,803,330!2028-07-13,1098,350!2026-10-10,540,310!2027-06-28,758,310!2028-12-28,1229,350!2028-08-13,1122,350-->

> [!example] example
>
> We visit every household in a given street, and interview the first person to answer the door. In any household with more than one occupant, this is {@{a nonprobability sample}@}, because {@{some people are more likely to answer the door (e.g. an unemployed person who spends most of their time at home is more likely to answer than an employed housemate who might be at work when the interviewer calls)}@} and {@{it's not practical to calculate these probabilities}@}. <!--SR:!2029-06-20,1364,350!2027-08-09,814,330!2027-05-07,747,330-->

{@{Nonprobability sampling methods}@} include {@{[convenience sampling](convenience%20sampling.md), [quota sampling](quota%20sampling.md), and [purposive sampling](nonprobability%20sampling.md)}@}. In addition, {@{nonresponse effects}@} may {@{turn _any_ probability design into a nonprobability design}@} if {@{the characteristics of nonresponse are not well understood}@}, since {@{nonresponse effectively modifies each element's probability of being sampled}@}. <!--SR:!2029-03-10,1283,350!2027-07-27,672,270!2028-11-14,1192,350!2026-03-21,140,405!2026-03-20,139,405!2026-03-19,138,405-->

## errors in sample surveys

- see: [sampling error](sampling%20error.md)

Survey results are {@{typically subject to some error}@}. Total errors can be classified into {@{sampling errors and non-sampling errors}@}. The term "error" here includes {@{systematic biases as well as random errors}@}. <!--SR:!2028-09-16,1149,350!2026-12-21,640,330!2029-02-09,1262,350-->

### sampling errors and biases

Sampling errors and biases are {@{induced by the sample design}@}. They include {@{selection bias and random sampling errors}@}: <!--SR:!2028-10-26,1180,350!2028-10-23,1178,350-->

- [selection bias](selection%20bias.md) ::@:: When the true selection probabilities differ from those assumed in calculating the results. <!--SR:!2028-05-20,1056,350!2028-10-18,1174,350-->
- [random sampling error](sampling%20error.md) ::@:: Random variation in the results due to the elements in the sample being selected at random. <!--SR:!2028-12-02,1206,350!2029-08-01,1397,350-->

### non-sampling errors

- see: [non-sampling error](non-sampling%20error.md)

Non-sampling errors are other errors which can impact final survey estimates, caused by problems in data collection, processing, or sample design. Such errors may include {@{over-coverage, under-coverage}@}, {@{measurement error, processing error, participation bias, etc.}@}: <!--SR:!2028-06-08,913,290!2026-05-24,133,408-->

- over-coverage ::@:: inclusion of data from outside of the population <!--SR:!2029-07-26,1392,350!2029-09-05,1424,350-->
- under-coverage ::@:: sampling frame does not include elements in the population <!--SR:!2027-08-22,827,330!2028-12-25,1226,350-->
- measurement error ::@:: e.g. when respondents misunderstand a question, or find it difficult to answer <!--SR:!2027-11-07,884,330!2029-06-12,1357,350-->
- processing error ::@:: mistakes in data coding <!--SR:!2029-01-28,1251,350!2028-12-30,1230,350-->
- [non-response or participation bias](participation%20bias.md) ::@:: failure to obtain complete data from all selected individuals <!--SR:!2028-01-03,947,350!2028-10-21,1175,350-->

After sampling, {@{a review is held of the exact process followed in sampling, rather than that intended}@}, in order to {@{study any effects that any divergences might have on subsequent analysis}@}. <!--SR:!2026-10-21,571,310!2027-08-09,800,330-->

A particular problem involves {@{_non-response_}@}. Two major types of non-response exist: {@{unit non-response and item non-response}@}. <!--SR:!2029-05-24,1344,350!2029-01-10,1237,350-->

- unit non-response ::@:: lack of completion of any part of the survey <!--SR:!2028-07-25,1106,350!2029-04-13,1310,350-->
- item non-response ::@:: submission or participation in survey but failing to complete one or more components/questions of the survey <!--SR:!2027-03-29,717,330!2029-01-31,1256,350-->

In {@{[survey sampling](survey%20sampling.md)}@}, {@{many of the individuals identified as part of the sample}@} may be {@{unwilling to participate, not have the time to participate \([opportunity cost](opportunity%20cost.md)\)}@}, or {@{survey administrators may not have been able to contact them}@}. In this case, there is {@{a risk of differences between respondents and nonrespondents}@}, leading to {@{biased estimates of population parameters}@}. This is often addressed by {@{improving survey design, offering incentives, and conducting follow-up studies}@} which make a repeated attempt to {@{contact the unresponsive and to characterize their similarities and differences with the rest of the frame}@}. The effects can also be mitigated by {@{weighting the data \(when population benchmarks are available\) or by imputing data based on answers to other questions}@}. {@{Non-response}@} is {@{particularly a problem in internet sampling}@}. {@{Reasons for this problem}@} may include {@{improperly designed surveys, over-surveying \(or survey fatigue\)}@}, and the fact that potential participants may {@{have multiple e-mail addresses, which they do not use anymore or do not check regularly}@}. <!--SR:!2029-09-15,1431,350!2029-11-30,1419,310!2027-07-05,731,290!2028-03-17,927,330!2028-04-16,1028,350!2028-02-26,913,330!2028-02-23,739,417!2026-11-05,346,397!2028-01-31,719,417!2028-02-18,735,417!2028-03-05,749,417!2027-12-25,690,417!2028-02-09,727,417!2028-01-22,713,417-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/sampling_(statistics)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
