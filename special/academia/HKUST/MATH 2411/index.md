---
aliases:
  - HKUST MATH 2411
  - HKUST MATH 2411 index
  - HKUST MATH2411
  - HKUST MATH2411 index
  - MATH 2411
  - MATH 2411 index
  - MATH2411
  - MATH2411 index
tags:
  - flashcard/active/special/academia/HKUST/MATH_2411/index
  - function/index
  - language/in/English
---

# index

- HKUST MATH 2411
- name: Applied Statistics

The content is in teaching order.

- grading schemes: take highest
  1. homework 10%, midterm exam 25%, final exam 65%
  2. homework 10%, midterm exam 0%, final exam 90%
- logistics
  - _R_, a programming language, is discussed and used in homework only.
  - homework: No late submissions.
  - midterm exam: No make-up exams.
    - datetime: 2024-10-20T14:00:00+08:00/2024-10-20T15:30:00+08:00
    - venue: Lecture Theater B (L1), Lecture Theater J (L2)
  - final exam: Make-up exam if absent due to special reasons, e.g. sick. Provide evidence.
- syllabus: descriptive statistics, probability theory, inferential statistics
  - syllabus / descriptive statistics: descriptive statistics
  - syllabus / probability theory: introduction to probability theory → discrete random variable, discrete probability distribution → continuous random variable, continuous probability distribution
  - syllabus / inferential statistics: estimation of parameters: point estimation, interval estimation → hypothesis testing → simple linear regression → other topics: goodness of fit test, etc.
- [assignments](assignments/)

## week 1 lecture

- datetime: 2024-09-02T10:30:00+08:00/2024-09-02T11:50:00+08:00
- course logistics
- [statistics](../../../../general/statistics.md)
  - statistics / definition (data) ::: a mathematical science that pertains to the _data_ collection, analysis, interpretation, explanation, and presentation
    - statistics / definition (data) / examples ::: Almost all fields of studies make use of data and statistics. _Statistical literacy_ has become a very important thing.
  - statistics / definition (decision making) ::: a method for processing and analyzing the collected data so as to help reduce the uncertainty inherent in _decision making_
    - statistics / definition (decision making) / examples ::: choosing the best medication, driving to work in the shortest time, marketing (and choosing good grade courses)
  - statistics / definition (inference) ::: the art and science of answering questions and exploring ideas through the processes of gathering data, describing data, and _making inferences_ about a population on the basis of a smaller sample
  - statistics / branches ::: descriptive statistics, inferential statistics
- [descriptive statistics](../../../../general/descriptive%20statistics.md) ::: data collection, summarization, and presentation
  - descriptive statistics / methodologies ::: graphical (e.g. box plot, histogram), numerical (e.g. sample mean, sample median, sample quartile, sample variance), tabular (e.g. frequency table)
  - descriptive statistics / steps ::: collect (e.g. sampling, surveying) → classify (e.g. grouping) → characterize (e.g. sample mean) → present (e.g. box plot, table)
- [inferential statistics](../../../../general/statistical%20inference.md) ::: statistical procedures that use data from an observed _sample_ to make a conclusion about a _population_
  - inferential statistics / key terms ::: _population_: a collection of all objects of interest, _sample_: an analyzed part of the _population_; _parameter_: a numerical measure describing a _population_, _statistic_: a numerical measure describing a _sample_
  - inferential statistics / reasons for sampling ::: cost-effectiveness, practicality
  - inferential statistics / procedures ::: analysis of variance, estimation of parameters, goodness of fit test, hypothesis testing, probability distribution, regression, ...
    - inferential statistics / procedures / analysis of variance ::: used to test the difference between two or more means
    - inferential statistics / procedures / estimation of parameters ::: estimate unknown parameters of a population based on a sample of the population
    - inferential statistics / procedures / goodness of fit test ::: test how well a hypothesized statistical model (distribution) fits the observed samples
    - inferential statistics / procedures / hypothesis testing ::: test a statement about the unknown parameters
    - inferential statistics / procedures / probability distribution ::: mathematical function that gives the probabilities of occurrence of possible outcomes for an experiment
    - inferential statistics / procedures / regression ::: estimate the relationships between a dependent variable (output) and one or more independent variables (inputs)
  - inferential statistics / example
    - inferential statistics / example / question ::: Sampling 100 products from a process, 3 are defective. Is the process acceptable if the long-term (true/real) defective rate should not exceed 1%?
    - inferential statistics / example / answer (Sampling 100 products from a process, 3 are defective. Is the process acceptable if the long-term (true/real) defective rate should not exceed 1%?) ::: Assume the true defective rate of the process is 1%. Calculate the _probability of 10 or more products being defective in a random sample of 100 products_: $$\begin{aligned} P(\text{defective} \ge 3) & = 1 - P(\text{defective} < 3) \\ & = 1 - \sum_{k = 0}^2 P(\text{defective} = k) \\ & = 1 - \sum_{k = 0}^2 \binom {100} k (0.01)^k (0.99)^{100 - k} \\ & \approx 0.0794 \end{aligned}$$. This suggests the actual process likely has a true defective rate exceeding 1%.
  - inferential statistics / -duction ::: induction: draw conclusions on the population from the statistics of a sample; deduction: characterize hypothetical samples of a population from its parameters
- [_R_](../../../../general/R%20(programming%20language).md) ::: a programming language for statistical computing and data visualization
  - _R_ / website ::: <https://r-project.org/>
  - _R_ / components ::: _R_, _R_ console, RStudio
  - _R_ / help commands ::: `help.start()`: general help, `help(<foo>)`, `?<foo>`: help about `<foo>`, `apropos("<foo>")`: list all functions containing the string `<foo>`, `example(<foo>)`: show an example of the function `<foo>`
- [descriptive statistics](../../../../general/descriptive%20statistics.md)
  - descriptive statistics / why ::: communicate data and support your reasoning from data
  - descriptive statistics / methodologies
  - descriptive statistics / steps
- [data](../../../../general/data.md) (singular: datum) ::: a collection of measurements and identifiers, which can take make many forms like numbers, strings, etc.
  - data / reason for summarizing ::: Data cannot inform us well without summarization. Also see [DIKW pyramid](../../../../general/DIKW%20pyramid.md) (data, knowledge, information, wisdom).
  - data / reading a table ::: Data are commonly listed in a table. Each column is a characteristic which we called a _variable_. Each row (except for the header) is a datum which we called an _observation_.
  - data / types of variables ::: _categorical/qualitative_: distinct categories or labels, and can be subdivided into _nominal_ if the categories cannot be ranked or _ordinal_ if they can be ranked; _quantitative_: numerical, and can be subdivided into _continuous_ if it arises from measurement or _discrete_ if it arises from counting
    - data / types of variables / importance ::: proper interpretation of data, proper selection of statistical analysis (e.g. not averaging nominal variables)
    - data / types of variables / note ::: Sometimes for data processing, categorical values are mapped to numbers. Do not mistake them for quantitative values!
- [descriptive statistics](../../../../general/descriptive%20statistics.md)
  - descriptive statistics / common measures ::: central tendency (location), variability (spread/dispersion)
    - central tendency ::: sample mean, sample median, trimmed sample mean, ...
    - variability ::: inter-quartile range, sample range, sample standard deviation, sample variance
  - sample mean ::: Suppose we have $n$ _samples_ of a random variable $x$, labeled $x_1, \ldots, x_n$. Then its _sample mean_ is $$\bar x = \frac 1 n \sum_{k = 1}^n x_n$$.
    - sample mean / _R_ ::: use `mean(...)`
  - sample median ::: Suppose we have $n$ _samples_ of a random variable $x$, labeled $x_1, \ldots, x_n$. They are sorted in increasing (or decreasing) order, i.e. $x_1 \le \ldots \le x_n$. Then its _sample median_ is $$\tilde x = \frac 1 2 \left(x_{\lfloor \frac {x + 1} 2 \rfloor} + x_ {\lceil \frac {x + 1} 2 \rceil} \right) = \begin{cases} x_{\frac {n + 1} 2} & \text{if }n\text{ is odd} \\ \frac 1 2 \left(x_{\frac x 2} + x_{\frac x 2 + 1} \right) & \text{if }n\text{ is even} \end{cases}$$.
  - sample mean vs sample median ::: The former is sensitive to outliers while the latter is not. This motivates trimming the outliers of the observations before calculating the former to reduce its sensitiveness to outliers (while still being more sensitive than the latter).
    - sample mean vs sample median / details ::: The former is used if the distribution is symmetric, unimodal and there are no outliers. Otherwise the latter is usually better.
    - sample mean vs sample median / trimmed (sample) mean ::: It is found by removing a certain percent of both the least and greatest values of the observations before computing its mean.
      - sample mean vs sample median / trimmed (sample) mean / notation (examples) ::: For example, $\bar x_{\operatorname{tr}(10)}$, called _10% trimmed mean_, is the mean after trimming the least 10% and greatest 10% of the observations.

## week 1 lecture 2

- datetime: 2024-09-04T10:30:00+08:00/2024-09-04T11:50:00+08:00
- [descriptive statistics](../../../../general/descriptive%20statistics.md)
  - sample [variance](../../../../general/variance.md) ::: Suppose we have $n$ _samples_ (with replacement) of a random variable $x$, labeled $x_1, \ldots, x_n$. Then its _unbiased sample variance_ is $$s^2_{n - 1} = \frac 1 {n - 1} \sum_{i = 1}^n (x_i - \bar x)^2$$. The _biased sample variance_, denoted $s^2_n$, replaces the factor $\frac 1 {n - 1}$ with $\frac 1 n$ in the above equation. Unless otherwise specified, the unbiased sample variance is used in this course.
    - sample [variance](../../../../general/variance.md) / dividing by $n - 1$ ::: $n - 1$ is also the _degree of freedom associated with the variance estimate_, which is the number of independent information pieces available for computing variability. Since $\bar x$ is usually the sample mean, which is determined from the sample mean, a degree of freedom is lost, as $\sum_{i = 1}^n (x_i - \bar x)$ is always forced to be zero. So the degree of freedom is $n - 1$. The original $n$ degrees of freedom comes from the $n$ observations being independent. This explains why dividing $n - 1$ instead of $n$ is _unbiased_. (If the $n$ observations are the entire population, then we divide by $n$ to get the _population variance_ instead.)
    - sample [variance](../../../../general/variance.md) / dividing by $n$ ::: However, if $\bar x$ is the population mean, then $\sum_{i = 1}^n (x_i - \bar x)$ is not forced to be zero, so the degree of freedom is still $n$ (from $n$ independent observations) instead. In this case, we divide by $n$ instead of $n - 1$ to get an _unbiased_ (sample/population) variance. This is regardless if the $n$ observations are a sample or the entire population.
    - sample variance / _R_ ::: use `var(...)`
  - sample standard deviation ::: It is the square root of the sample variance: $$s = \sqrt{s^2}$$. However, no matter if the sample variance is biased or unbiased, the resulting sample standard deviation is biased. This is because the square root is a concave function and introduces additional negative bias (smaller than the corresponding population parameter).
    - sample standard deviation / _R_ ::: use `sd(...)`
  - sample range ::: It is defined as $$\text{range} = \max\set{x_i} - \min\set{x_i}$$. It is useful for statistical quality control (e.g. finding unusual outliers caused by bad measurement).
  - inter-quartile range (IQR) ::: It is defined as the range of the middle 50% of the data, or equivalently the third (75%) quartile subtracted by the first (25%) quartile: $$\text{IQR} = Q_3 - Q_1$$. It is also a measure of data dispersion. It can also eliminate problems with outliers.
    - inter-quartile range / _R_ ::: use `IQR(...)`, not `iqr`
  - variability / characteristics (common to most or all measures of variability) ::: All measures must be nonnegative. Most measures (exceptions: inter-quartile range, trimmed variants of statistics, ...) are zero [iff](../../../../general/if%20and%20only%20if.md) all data are the same (i.e. no spread).
- [data presentation](../../../../general/data%20and%20information%20visualization.md) ::: A graphical summary can communicate information better as people prefers to look at them rather than numbers. The method of presentation depends on the data _nature_ and visualization _goals_.
  - data presentation / quantitative data ::: box plot, frequency table, histogram, line chart, scatter plot, ...
  - data presentation / categorical data ::: bar chart, frequency table, pie chart, ...
  - line chart ::: It visualizes the trend of data over time well. Good for time-series data like stock prices.
    - line chart / reading ::: Start from the x-axis, then to the line, and lastly to the y-axis.
    - line chart / _R_ ::: use `plot(...)`
  - frequency table (quantitative) ::: Data is grouped into numerically ordered non-overlapping _categories_ or _class intervals_. Then a _summary table_ is drawn based on the grouped data. This condenses the data and allows for quicker data interpretation.
    - frequency table (quantitative) / procedure ::: Decide the number of class intervals (usually 5 to 20). Divide the data into that many intervals (usually covering the data range evenly). Adjust the class interval boundaries to avoid overlapping (as endpoints are inclusive). Construct the summary table.
    - frequency table (quantitative) / table headers ::: class interval, class midpoint, frequency, relative frequency, ...
  - histogram ::: A bar chart based on the frequency table. The x-axis labels the class intervals while the y-axis labels the frequency or density (relative frequency).
    - histogram / _R_ ::: use `hist(...)`, or `histogram(...)` after importing `library(lattice)` (different style)
- [descriptive statistics](../../../../general/descriptive%20statistics.md)
  - modality ::: It is the number of peaks (local modes) in the probability distribution. If there are no significant peaks, then it is _uniform_. If there are peaks, it may be _unimodal_ (1), _bimodal_ (2), ...; or _multimodal_ (>1) in general for multiple peaks.
    - [unimodaility](../../../../general/unimodality.md)
      - [§ unimodal probability distribution](../../../../general/unimodality.md#unimodal%20probability%20distribution)
    - [multimodal distribution](../../../../general/multimodal%20distribution.md)
  - [skewness](../../../../general/skewness.md) ::: Intuitively for graphs, a distribution is __left-skewed__ or __negative-skewed__ if _its tail is on the left_, and vice versa for __right-skewed__ or __positive-skewed__. Otherwise, it is __unskewed__. Intuitively for numbers, a distribution is left-skewed if its mean is on the left of (smaller than) its median, and vice versa for right-skewed. Otherwise, it is unskewed. (But actually, said intuition is very very wrong sometimes... See the item below.)
    - [skewness § relationship of mean and median](../../../../general/skewness.md#relationship%20of%20mean%20and%20median) ::: The above intuition is _usually_ correct if the distribution is unimodal. But in general, there are no direct relationships between skewness, mean, and median. Furthermore, an unskewed distribution is not necessarily symmetric. But its converse, a symmetric distribution is unskewed, is true.
  - percentile, quantile (not quartile) ::: percentile, quantile: the number for which a specified portion of the sample or population is _equal to or less than_ (e.g. 90th percentile = 0.90 quantile, which means the number 90% of the sample or population is equal to or less than)
  - quartile ::: 1st quartile/lower quartile (Q1) = 25th percentile/0.25 quantile, 2nd quartile/median (Q2) = 50th percentile/0.50 quantile, 3rd quartile/upper quartile (Q3) = 75th percentile/0.75 quantile
    - quartile / procedure ::: One would find the quartiles hard to define when the number of samples is not divisible by 4. In this case, there are many different ways to define them, and we will use the following equation (this is different from that in HKDSE): $$x(p) = \frac 1 2 \left(x_{\lfloor np + 0.5 \rfloor} + x_{\lceil np + 0.5 \rceil} \right) \qquad p = 0.25, 0.50, 0.75$$.
    - quartile / _R_ ::: use `quantile(...)`, not `quartile` (note that the procedure of `quantile` is different from discussed above)
  - extrema ::: 0th quartile/minimum (Q0) = 0th percentile/0.00 quantile, 4th quartile/maximum (Q4) = 100th percentile/1.00 quantile
- [data presentation](../../../../general/data%20and%20information%20visualization.md)
  - box plot ::: A box plot labels the least data that is not an outlier (instead of the value $Q_1 - 1.5 \cdot \text{IQR}$), the lower quartile (Q1), median (Q2), upper quartile (Q3), and the greatest data that is not an outlier (instead of the value $Q_3 + 1.5 \cdot \text{IQR}$) as lines; and outliers as dots (with "min" and "max" labels on 2 of them). Additional lines are added so that the lines of Q1 and Q3 forms a rectangle (box). (See that thing on Canvas grade stats...?)
    - box plot / outliers ::: They $x$ are points that are $x \le Q_1 - 1.5 \cdot \text{IQR}$ or $x \ge Q_3 + 1.5 \cdot \text{IQR}$. Usually they are far away from the majority of the data and are _likely_ produced by measurement errors. Assuming a normal distribution, outliers are expected to appear rarely (~0.007).
    - box plot / _R_ ::: use `boxplot(...)`

## week 1 tutorial

- datetime: 2024-09-06T09:30:00+08:00/2024-09-06T10:20:00+08:00
- unscheduled

## week 2 lecture 1

- datetime: 2024-09-09T10:30:00+08:00/2024-09-09T11:50:00+08:00
- [data presentation](../../../../general/data%20and%20information%20visualization.md)
  - sample size / _R_ ::: use `length(...)`
  - first _n_ observations / _R_ ::: use `head(...)`
  - scatter plot ::: Plots data that comes as pairs. Good for visualizing relationship between two variables (e.g. regression).
    - scatter plot / _R_ ::: use `plot(...)`
  - frequency table (categorical) ::: Categorical data is already pre-grouped. Then a _summary table_ is drawn based on the categories. This condenses the data and allows for quicker data interpretation.
    - frequency table (categorical) / table headers ::: \<variable name\>, count, cumulative count (if ordinal), percent, cumulative percent (if ordinal), ...
  - pie chart ::: A filled circle showing proportions of different categories.
    - pie chart / _R_ ::: use `pie(...)`
  - bar chart ::: Bars showing counts of different categories.
    - bar chart / _R_ ::: use `barplot(...)`
- [sampling](../../../../general/sampling%20(statistics).md) ::: The act of creating a _sample_ from a _population_. It can be mainly classified into _probability sampling_ and _non-probability sampling_.
  - sampling / [errors](../../../../general/sampling%20(statistics).md#errors%20in%20sample%20surveys) ::: It is very important to sample correctly. Some biases include survivorship bias (as demonstration, unlikely related in most statistics), selection bias, non-response bias (participation bias), and voluntary response bias.
    - sampling / errors / survivorship bias ::: (as demonstration, unlikely related in most statistics) A famous example: Many planes were flying through enemy territories. Some survived. Engineers found holes on some parts of the survived planes. So they decided to reinforce those parts. But this did not improve survival rates. The actual best parts to reinforce were those without holes on the survived planes, because this implied the other planes did not survive because of holes in said parts. Hence the name.
    - sampling / errors / selection bias ::: A sample of convenience, which probably makes certain subjects more likely than others to be sampled.
    - sampling / errors / non-response bias (participation bias) ::: For example, parents are less likely to answer a survey at 6 pm because they are busy with children and dinner.
    - sampling / errors / voluntary response bias ::: Websites for posting reviews are more likely to get responses from customers who had very bad or very good experiences.
    - [sampling § sampling errors and biases](../../../../general/sampling%20(statistics).md#sampling%20errors%20and%20biases)
    - [sampling § non-sampling errors](../../../../general/sampling%20(statistics).md#non-sampling%20errors)
  - [probability sampling](../../../../general/sampling%20(statistics).md#sampling%20frame) ::: It supports strong statistical inferences from a sample to the population, minimizing selection bias. It involves random selection: any individual has a nonzero probability being picked, and said probability can be determined.
    - probability sampling / examples ::: cluster sampling, simple random sampling, stratified sampling, systematic sampling, ...
    - probability sampling / simple random sampling ::: All individual in a population has equal probability of being selected.
    - probability sampling / systematic sampling ::: A _probabilistic_ method is used to select individuals of a population, such as sampling every third person.
    - probability sampling / stratified sampling ::: Individuals are split into groups based on certain characters. Then simple random sampling is applied on each group.
    - probability sampling / cluster sampling ::: Split the population into clusters and select some of the clusters (cannot select an individual in a cluster without selecting other in the same cluster).
  - [non-probability sampling](../../../../general/sampling%20(statistics).md#nonprobability%20sampling) ::: It supports weaker statistical inferences from a sample to the population. The advantage is that non-probability sampling may be more convenient in many contexts.
    - non-probability sampling / examples ::: convenience sampling, purposive sampling, voluntary response sampling, snowball sampling, ...
    - non-probability sampling / convenience sampling ::: Sampling whoever is most convenient to you, e.g. nearest people.
    - non-probability sampling / voluntary response sampling ::: Individuals in a population are made known of your sample and voluntarily decides to participate or not.
    - non-probability sampling / purposive sampling ::: A _non-probabilistic_ method is used to select individuals in a population.
    - non-probability sampling / snowball sampling ::: Some individuals of a population are sampled initially. Individuals sampled recruit other individuals for sampling. This recruitment chain continues indefinitely, hence snowballing.

## week 2 lecture 2

- datetime: 2024-09-11T10:30:00+08:00/2024-09-11T11:50:00+08:00
- [probability](../../../../general/probability.md)
  - probability / subject ::: __Probability__ is the study of randomness.
  - probability / event ::: A __probability__ of an uncertain outcome / event is the chance (or likelihood) that it will occur. It must be in between 0 and 1, inclusively.
- random experiment ::: A __random experiment__ is a process that generates observations, and its outcome cannot be known beforehand and is only known after its performance.
- sample space ::: A __sample space__ is a set of _all_ possible outcomes of a random experiment, often denoted by _S_. Each outcome is called  __sample point__, denoted by _s_.
  - sample space / set-builder notation ::: To describe sample spaces for a large or infinite sample points, we can use the set-builder notation (__statement__ or __rule method__). It has the form: $$\set{x \mid P(x)} \,.$$, where _x_ is an indeterminate and _P_(_x_) is a predicate on the indeterminate. An element is in the set iff _P_(_x_) is true.
- event ::: An __event__ is any subset of the sample space, often denoted by capital letters. The set of all events is the __event space__. Equivalently, it is the power set of the sample space.
- Venn diagram ::: A __Venn diagram__ is a graph that can illustrate relationships among events. A rectangle is often used to represent the _sample space_, while circles often represent _events_ we are interested in. The circles may overlap, or be inside of one another completely.
- set theory
  - set theory / union ::: The __union__ of two events _A_ and _B_ is the event that at least one of _A_ or _B_ occur, denoted by _A_ ∪ _B_. It is defined as: $$A \cup B = \set{s \mid s \in A \text{ or } s \in B} \,.$$
  - set theory / exhaustive ::: If the _union_ of several events is the sample space, the events are said to be __exhaustive__.
  - set theory / intersection ::: The __intersection__ of two events _A_ and _B_ is the even that both of _A_ and _B_ occur, denoted by _A_ ∩ _B_. It is defined as: $$A \cap B = \set{s \mid s \in A \text{ and } s \in B} \,.$$ A property: _A_ ∩ _B_ = _A_ iff _A_ is a subset of _B_ (_A_ ⊆ _B_).
  - set theory / disjoint ::: If two events have no common element, their intersection is an empty set Φ. The events are said to be __disjoint__. If a set of two or more events is __pairwise disjoint__, that is any two events from the set of events are _disjoint_, then the set of events are said to be __mutually exclusive__.
  - set theory / complement ::: The __complement__ of an event _A_ is the sample space excluding outcomes in event _A_, denoted $A^\complement, A^c, \overline A, A'$. Intuitively, it is the event that event _A_ does not occur. It is defined as $$A^\complement = \set{s \mid s \in S, s \notin A} \,.$$ Three properties: _S_<sup>c</sup> = Φ and Φ<sup>c</sup> = _S_, and an event and its complement must be _disjoint_.
  - set theory / difference ::: The __difference__ of two events _A_ and _B_ is the event that _A_ occurs but _B_ does not occur, denoted _A_ − _B_. It is defined as: $$A - B = \set{s \mid s \in A \text{ and } s \notin B} = A \cap B^\complement \,.$$
  - set theory / commutative laws ::: $$\begin{aligned} A \cup B & = B \cup A \\ A \cap B & = B \cap A \end{aligned}$$
  - set theory / associative laws ::: $$\begin{aligned} A \cup (B \cup C) & = (A \cup B) \cup C \\ A \cap (B \cap C) & = (A \cap B) \cap C \end{aligned}$$
  - set theory / distributive laws ::: $$\begin{aligned} A \cup (B \cap C) & = (A \cup B) \cap (A \cup C) \\ A \cap (B \cup C) & = (A \cup B) \cap (A \cup C) \end{aligned}$$
  - set theory / De Morgan's laws ::: $$\begin{aligned} (A \cup B)^\complement & = A^\complement \cap B^\complement \\ (A \cap B)^\complement & = A^\complement \cup B^\complement \\ \left(\bigcup_{k = 1}^n A_k \right)^\complement & = \bigcap_{k = 1}^n A_k^\complement \\ \left(\bigcap_{k = 1}^n A_k \right)^\complement & = \bigcup_{k = 1}^n A_k^\complement \end{aligned}$$

## week 2 tutorial

- datetime: 2024-09-13T09:30:00+08:00/2024-09-13T10:20:00+08:00

## week 3 lecture

- datetime: 2024-09-16T10:30:00+08:00/2024-09-16T11:50:00+08:00
- [probability axioms](../../../../general/probability%20axioms.md)
  - probability axioms / history ::: In 1933, a Russian mathematician named Andrei Nikolayevich Kolmogorov published the axiomatic structure of probability theory.
  - probability axioms / first axiom ::: The first axiom is __non-negativity__. The probability of any event in a sample space is nonnegative.
  - probability axioms / second axiom ::: The second axiom is __normalization__. The probability of the event that is the entire sample space is 1.
  - probability axioms / third axiom ::: The third axiom is __countable additivity__. For any _countable_ (finite or infinite) sequence of _mutually exclusive_ events, the probability of the union of them is the sum of their probabilities. <p> A set is _countable_ if it is finite or its element can be enumerated (has a one-to-one correspondence with the natural numbers). For example, the natural numbers are _countable_, while the real numbers or any nonempty intervals of it are not.
- probability measure ::: A __probability measure__, denoted _P_, is a real-valued function that assigns probabilities to events in a sample space. It is a __measure__, a mathematical abstraction of area, volume, probability, etc.
- probability axioms
  - probability axioms / probability of the empty set ::: The probability of the empty set is 0. Proof: $$\begin{aligned} P(\varnothing \cap \varnothing) & = P(\varnothing) + P(\varnothing) && \sigma\text{-additivity} \\ P(\varnothing) & = P(\varnothing) + P(\varnothing) \\ P(\varnothing) & = 0 \end{aligned}$$
  - probability axioms / finite additivity ::: It is just the first axiom limited to finite sequences. Proof: Append an infinite number of empty sets to the finite sequence to make it infinite. Then _countable additivity_ can be applied.
  - probability axioms / monotonicity ::: If _A_ is a subset of _B_ then _P_(_A_) ≤ _P_(_B_). Proof: $$\begin{aligned} P(A) + P(B - A) & = P(B) && A \subseteq B, \sigma\text{-additivity} \\ P(A) & \le P(B) && \text{non-negativity} \end{aligned}$$
  - probability axioms / numeric bound ::: The probability of any event is in between 0 and 1, inclusive. The lower bound is the non-negativity axiom, while the upper bound can be proved using the normalization axiom, monotonicity theorem, with the larger set being the sample space.
  - probability axioms / complement rule ::: The probability of the complement of any event is one minus the probability of that event. Proof: $$P\left(A^\complement \right) = P(S - A) = P(S) - P(A) = 1 - P(A)$$
  - probability axioms / additive law ::: The __additive law__ is: $$P(A \cup B) = P(A) + P(B) - P(A \cap B) \,.$$ When _A_ and _B_ are disjoint, then _P_(_A_ ∩ _B_) is 0 and the above degenerates into the finite additivity theorem. <p> The above is a special case of the [inclusion–exclusion principle](../../../../general/inclusion–exclusion%20principle.md), which can handle any countable number of events: $$\mathbb {P} \left(\bigcup _{i=1}^{n}A_{i}\right)=\sum _{k=1}^{n}\left((-1)^{k-1}\sum _{I\subseteq \{1,\ldots ,n\} \atop |I|=k}\mathbb {P} (A_{I})\right) \,.$$
- assignment
  - [assignment 1](assignments/assignent%201/index.md): 20/20, graded

## week 3 lecture 2

- datetime: 2024-09-18T10:30:00+08:00/2024-09-18T11:50:00+08:00
- public holiday: Day after Mid-Autumn Festival

## week 3 tutorial

- datetime: 2024-09-20T09:30:00+08:00/2024-09-20T10:20:00+08:00

## week 4 lecture

- datetime: 2024-09-23T10:30:00+08:00/2024-09-23T11:50:00+08:00

## week 4 lecture 2

- datetime: 2024-09-25T10:30:00+08:00/2024-09-25T11:50:00+08:00
- probability of an event in a sample space with _finite equally likely_ outcomes ::: If each outcome in a sample space is _equally likely_, then the probability of an event is the number of outcomes in the event divided by the number of outcomes in the sample space. This can be proved using the sigma-additivity axiom on an event.
  - probability of an event in a sample space with _finite equally likely_ oucomes / _R_ ::: `sample(x=<sample space>, size=<number of times to sample>, replace=<sample with/without replacement?>)`
- Simpson's paradox ::: An example: If a property is more likely to be present than not for both of two groups separately, this may still not be the case when the groups are combined.
- [combinatorial principles](../../../../general/combinatorial%20principles.md) ::: rule of sum, rule of product
  - [§ rule of sum](../../../../general/combinatorial%20principles.md#rule%20of%20sum) ::: The __rule of sum__ is an intuitive principle stating that if there are _a_ possible outcomes for an event (or ways to do something) and _b_ possible outcomes for another event (or ways to do another thing), and the two events cannot both occur (or the two things can't both be done), then there are _a + b_ total possible outcomes for the events (or total possible ways to do one of the things).
  - [§ rule of product](../../../../general/combinatorial%20principles.md#rule%20of%20product) ::: The rule of product is another intuitive principle stating that if there are _a_ ways to do something and _b_ ways to do another thing, then there are _a_ · _b_ ways to do both things.
- [permutation](../../../../general/permutation.md) ::: The number of ways to order _k_ things from _n_ things is $$P(n, k) = \frac {n!} {(n - k)!} \,.$$
  - permutation / circular permutation ::: If the ordering is circular, we need to divide the permutation by the size of the circle: $$\frac {P(n, k)} {k} = \frac {n!} {(n - k)! k} \,.$$
- [combination](../../../../general/combination.md) ::: The number of ways to select _k_ things from _n_ things, where the order of selection does not matter, is $$C(n, k) = \binom n k = \frac {n!} {(n - k)! k!} = \frac {P(n, k)} {k!} \,.$$
  - combination / partition ::: The number of ways to partition _n_ things into _r_ labelled partitions, where _k_<sub>_i_</sub> is the number of things in the _i_-th partition, is: $${n\choose k_1,k_2,\ldots,k_r} =\frac{n!}{k_1!k_2!\cdots k_r!} \,.$$ When there are only two partitions, this is the same as above, the number of ways to select _k_ things from _n_ things.

## week 4 tutorial

- datetime: 2024-09-27T09:30:00+08:00/2024-09-27T10:20:00+08:00

## week 5 lecture

- datetime: 2024-09-30T10:30:00+08:00/2024-09-30T11:50:00+08:00
- [conditional probability](../../../../general/conditional%20probability.md) ::: The __conditional probability__ of an event _A_ given that an event _B_, where _P_(_B_) > 0, has happened is: $$P(A \mid B) = \frac {P(A \cap B)} {P(B)} \,.$$ A property: $P(A \mid B) \ge P(A \cap B)$.
  - conditional probability / motivation ::: Knowing an event has happened may modify the probability of other events. Conditional probability can model this.
  - conditional probability / multiplicative rule ::: If _P_(_B_) > 0, then $$P(A \cap B) = P(A \mid B) P(B) \,.$$ This may be directly proved from the definition of conditional probability. Sometimes, the above is taken to be the definition of conditional probability instead (but not in this course).
  - conditional probability / conserved properties ::: Many other properties of probability hold under conditional probability. This can be easily seen by making the event that has happened to be the sample space instead. Example: $$\begin{aligned} P(A \mid B) & = 1 - P\left(A^\complement \mid B \right) \\ P(A \cup B \mid C) & = P(A \mid C) + P(B \mid C) - P(A \cap B \mid C) \\ P(A \cap B \mid C) & = P(A \mid B \cap C) P(B \mid C) \,. \end{aligned}$$ For the last example, if you reinterpret _C_ as the sample space, then $P(A \mid B \cap C)$ becomes $P(A \mid B)$.
- [chain rule](../../../../general/chain%20rule%20(probability).md) ::: generalization of the _multiplicative rule_
  - [chain rule § two events](../../../../general/chain%20rule%20(probability).md#two%20events) ::: This is the same as the _multiplicative rule_.
  - [chain rule § finitely many events](../../../../general/chain%20rule%20(probability).md#finitely%20many%20events) ::: $$\begin{aligned} \mathbb P(A_1 \cap \ldots \cap A_n) & = \mathbb P(A_1 \cap \ldots \cap A_{n - 1}) \mathbb P(A_n \mid A_1 \cap \ldots \cap A_{n - 1}) \\ & = \mathbb P(A_1) \mathbb P(A_2 \mid A_1) \ldots \mathbb P(A_n \mid A_1 \cap \ldots \cap A_{n - 1}) \\ & = \prod_{k = 1}^n \mathbb P(A_k \mid A_1 \cap \ldots A_{k - 1}) \\ & = \prod_{k = 1}^n \mathbb P\left(A_k \,\Bigg|\, \bigcap_{j = 1}^{k - 1} A_j \right) \end{aligned}$$
- [law of total probability](../../../../general/law%20of%20total%20probability.md#statement) ::: If $$\left\{{B_n : n = 1, 2, 3, \ldots}\right\}$$ is a _finite or countably infinite_ set of _mutually exclusive_ and _collectively exhaustive_ events $$P(A)=\sum_n P(A\mid B_n)P(B_n) \,,$$ where, for any $n$, if $P(B_n) = 0$, then these terms are simply omitted from the summation since $P(A\mid B_n)$ is finite. <p> The set of $B_n$ is also known as a __partition__ of the sample space.
- [Bayes' theorem](../../../../general/Bayes'%20theorem.md#statement%20of%20the%20theorem) ::: __Bayes' theorem__ relates _P_(_A_|_B_) to _P_(_B_|_A_). It states $$P(A \mid B) = \frac {P(B \mid A) P(A)} {P(B)} \qquad P(B) \ne 0 \,.$$ (The course also states _P_(_A_) ≠ 0, but this is not actually required.) Sometimes the theorem is stated in the form where the denominator is replaced using the law of total probability.
- supplementary examples
  - [randomized response](../../../../general/randomized%20response.md) :::  It allows respondents to respond to sensitive issues (such as criminal behavior or sexuality) while maintaining confidentiality. For example, we want to know about if a person has done something. We prepare two questions: one asking if the person has done something, the other asking if the person has NOT done something. We randomly choose one of the questions, the probability of which can be calculated (e.g. coin flip), to ask. <p> This is an application of Bayes' theorem.
  - the boy who cried wolf ::: We can apply Bayes' theorem to mathematically analyze this fable.
  - [Monty Hall problem](../../../../general/Month%20Hall%20problem.md)
- [independence](../../../../general/independence%20(probability%20theory).md) ::: Two events _A_ and _B_ are __independent__ iff $$P(A \cap B) = P(A) P(B) \,.$$ otherwise they are __dependent__. <p> Informally speaking, knowing either of the event has happened does not affect the probability of the other.
  - independence / equivalence ::: The following statements are equivalent: <ul> <li>_A_ and _B_ are independent.</li> <li>_A_ and _B_<sup>c</sup> are independent.</li> <li>_A_<sup>c</sup> and _B_ are independent.</li> <li>_A_<sup>c</sup> and _B_<sup>c</sup> are independent.</li> </ul> The above can be seen by seeing that the complement of an event is uniquely defined by the event. There is a one-to-one correspondence between a set and its complement (unless the sample space is the empty set, which is impossible for probability).
  - independence vs disjoint ::: Independent is not disjoint. End of story.
  - independence / pairwise independence ::: A finite set of events is __pairwise independent__ iff any two events from the set is _independent_. <p> Pairwise independence does NOT automatically imply _mutual independence_.
  - independence / mutual independence ::: A finite set of _n_ events is __mutually independent__ iff any 2 ≤ _k_ ≤ _n_ events from the set is _independent_. For the _independence_ of 2 ≤ _k_ events, this is simply: $$P\left(\bigcap_{i = 1}^k A_k \right) = \prod_{i = 1}^k A_k \,.$$ <p> Mutual independence automatically implies _pairwise independence_. However, note that the above statement must hold for all 2 ≤ _k_ ≤ _n_, not just _k_ = _n_. It is possible to create a sample space such that three events _A_, _B_, and _C_ are independent but none of the three events are _pairwise independent_.

## week 5 lecture 2

- datetime: 2024-10-02T10:30:00+08:00/2024-10-02T11:50:00+08:00
- [random variable](../../../../general/random%20variable.md) (r.v.) ::: A __random variable__ (__r.v.__) is a mathematical function. Its _domain_ is the sample space. Its _range_ is a measurable space, usually a finite set of integers or the real numbers. The function need not be _injective_ (different samples need not map to different values). It is commonly denoted by capital letters, with its possible numerical values (also called __realizations__) by the same but lowercase letters. <p> A way to think about random variable is that it maps each outcome to a real number.
  - random variable / motivation ::: How do we describe random process more mathematically? Random variables can do so.
  - random variable / notations ::: Some notations for a random variable _X_ on the sample space _S_: $$\begin{aligned} \set{X = x} & = \set{s \in S \mid X(s) = x} \\ \set{X \le x} & = \set{s \in S \mid X(s) \le x} \\ P(X = x) & = P(\set{X = x}) \\ P(X \le x) & = P(\set{X \le x}) \end{aligned}$$
  - random variable / types ::: There are two common types: _discrete_ random variables and _continuous_ random variables. If a random variable's range is _countable_ (finite or infinite), then the random variable is discrete. if a random variable's range is _uncountable_ and its _cumulative probability distribution_ (CDF) is _continuous everywhere_, then the random variable is continuous. <p> Other types not discussed here are _mixed_ random variables (a mix of discrete and continuous) and _singular_ random variables (neither discrete nor continuous).
- discrete random variable ::: A __discrete random variable__ has a _countable_ (finite or infinite) range.
  - [probability mass function](../../../../general/probability%20mass%20function.md) (PMF, pmf) ::: A __probability mass function__ (__PMF__, __pmf__) is a function that gives the probability that a _discrete random variable_ is exactly equal to some value. It is given by: $$p_X(x) = P(X = x) \,.$$ It is not defined for a continuous random variable. <p> The PMF has the following properties: $$\begin{aligned} \sum_x p_X(x) & = 1 \\ p_X(x) \ge 0 \,. \end{aligned}$$
- [cumulative distribution function](../../../../general/cumulative%20distribution%20function.md) (CDF, cdf) ::: A __cumulative distribution function__ (__CDF__, __cdf__) of a real-valued random variable _X_ is the probability that _X_ will take a value less than or equal to _x_. It is given by: $$F_X(x) = P(X \le x) \,.$$ The probability that _X_ will take a value in between \(_a_, _b_\], where _a_ < _b_, is $$P(a < X \le b) = F_X(b) - F_X(a) \,.$$
  - cumulative distribution function / properties ::: A CDF of any probability distribution _supported on the real numbers_ is a right-continuous monotone increasing function (a càdlàg function) $F: \mathbb R \rightarrow [0, 1]$ satisfying $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to +\infty} F(x) = 1$.
  - cumulative distribution function / existence and uniqueness ::: Every probability distribution _supported on the real numbers_, discrete, continuous, "mixed", as well as singular, is uniquely identified by its CDF. Thus, a CDF is defined for every probability distribution supported on the real numbers, even if its probability mass function (PMF) or probability density function (PDF) may be undefined.
  - cumulative distribution function / discrete random variable ::: The CDF of a discrete random variable is a non-decreasing step function.
- [expected value](../../../../general/expected%20value.md) ::: The __expected value__ (__population mean__, __first moment__) is a generalization of the weighted average. Informally, the expected value is the mean of the possible values a random variable can take, weighted by the probability of those outcomes. It is common denoted $E(X)$.
  - expected value / discrete random variable ::: The expected value of a discrete random variable is the weighted average of all possible outcomes $\mathcal X$: $$\operatorname E[X] = \sum_{x \in \mathcal X} x p(x) \,.$$ This is only defined if the sum converges absolutely, so it is possible for a discrete random variable to have a undefined expected value. <p> Also, $$\operatorname E[g(X)] = \sum_{x \in \mathcal X} g(x) p(x) \,.$$ for an arbitrary function $g(x)$.
  - expected value / linearity ::: An important property is its linearity: $$\begin{aligned} E(b) & = b \\ E(aX) & = a E(X) \\ E(aX + b) & = a E(x) + b \\ E(aX + bY) & = a E(x) + b E(Y) \,, \end{aligned}$$ where _a_, _b_ are constants and _X_, _Y_ are random variables _independent_ from each other, i.e. $$P(X \le x, Y \le y) = P(X \le x) P(Y \le y) \,.$$
- [variance](../../../../general/variance.md) ::: __Variance__ is the expected value of the squared deviation from the mean of a random variable. It is often represented by $\sigma ^{2}$, $s^{2}$, $\operatorname {Var} (X)$, $V(X)$, or $\mathbb {V} (X)$.
  - variance / discrete random variable ::: The variance fo a discrete random variable is $$\operatorname{Var}(X) = \sum_{x \in \mathcal X} \left((x - \mu)^2 p(x) \right) \,.$$ This is only defined if the sum exists, so it is possible for a discrete random variable to have undefined variance.
  - variance / properties ::: A well-known identity relating variance to expected value is $$\operatorname{Var}(X) = \operatorname E\left[X^2\right] - (\operatorname E[X])^2 = \operatorname E\left[X^2\right] - \mu^2 \,.$$ With this identity, the following properties can be proved: $$\begin{aligned} \operatorname{Var}(b) = 0 \\ \operatorname{Var}(aX) & = a^2 \operatorname{Var}(X) \\ \operatorname{Var}(aX + b) & = a^2 \operatorname{Var}(X) \\ \operatorname{Var}(aX + bY) & = a^2 \operatorname{Var}(X) + b^2 \operatorname{Var}(Y) \,, \end{aligned}$$ where _a_, _b_ are constants and _X_, _Y_ are random variables _independent_ from each other, i.e. $$P(X \le x, Y \le y) = P(X \le x) P(Y \le y) \,.$$
- assignment
  - [assignment 2](assignments/assignent%202/index.md): ?/20, graded

## week 5 tutorial

- datetime: 2024-10-04T09:30:00+08:00/2024-10-04T10:20:00+08:00

## week 6 lecture

- datetime: 2024-10-07T10:30:00+08:00/2024-10-07T11:50:00+08:00
- cumulative distribution function (CDF, cdf)
  - cumulative distribution function / continuous random variable ::: The CDF of a continuous random variable is a continuous monotone increasing function $F: \mathbb R \rightarrow [0, 1]$ satisfying $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to +\infty} F(x) = 1$.
- [probability density function](../../../../general/probability%20density%20function.md) (PDF, pdf) ::: The __probability density function__ (__PDF__, __pdf__) of an _absolutely continuous_ random variable is a function whose value at any given sample (or point) in the sample space (the set of possible values taken by the random variable) can be interpreted as providing a _relative likelihood_ that the value of the random variable would be equal to that sample. <p> Probability density is the probability per unit length, in other words, while the _absolute likelihood_ for a continuous random variable to take on any particular value is 0 since there is an infinite set of possible values to begin with. <p> It is common denoted $f_X(x)$ for an absolutely continuous random variable _X_.
  - probability density function / properties ::: A PDF is nonnegative at all points, and its integral over the entire real numbers exists and equals to 1.
  - probability density function / from and to cumulative distribution function ::: For an _absolutely continuous_ random variable _X_, $$\begin{aligned} f_X(x) & = \frac {\mathrm d} {\mathrm dx} F_X(x) \\ F_X(x) & = \int_{-\infty}^x \! f_X(x) \,\mathrm{d}x \,. \end{aligned}$$ <p> Note that the _absolute continuity_ of $F_X(x)$ is required for $f_X(x)$ to be defined, or otherwise differentiating $F_X(x)$ and then integrating the resulting $f_X(x)$ may yield a different $F_X(x)$.
  - probability density function / to and from cumulative distribution function ::: For a _Lebesgue-integrable_ function $f_X(x)$, $$\begin{aligned} F_X(x) & = \int_{-\infty}^x \! f_X(x) \,\mathrm{d}x  \\ f_X(x) & = \frac {\mathrm d} {\mathrm dx} F_X(x) && \text{if }f_X(x)\text{ is continuous at }x \,. \end{aligned}$$ <p> Note that if two Lebesgue-integrable functions differ from each other on measure zero, then the resulting $F_X(x)$ is the same. So the PDF cannot uniquely determine a CDF.
- expected value
  - expected value / continuous random variable ::: The expected value of a continuous random variable is the weighted average of all possible outcomes $\mathcal X$: $$\operatorname E[X] = \int_{-\infty}^{+\infty} \! x f(x) \,\mathrm{d}x = \int_{-\infty}^{+\infty} x \,\mathrm{d}F(x) \,.$$ This is only defined if the integral converges absolutely, so it is possible for a continuous random variable to have a undefined expected value. <p> Also, $$\operatorname E[g(X)] = \int_{-\infty}^{+\infty} \! g(x) f(x) \,\mathrm{d}x = \int_{-\infty}^{+\infty} g(x) \,\mathrm{d}F(x) \,.$$ for an arbitrary function $g(x)$.
- variance
  - variance / continuous random variable ::: The variance of a continuous random variable is $$\operatorname{Var}(X) = \int_{-\infty}^{+\infty} \! (x - \mu)^2 f(x) \,\mathrm{d}x = \int_{-\infty}^{+\infty} \! (x - \mu)^2 \,\mathrm{d}F(x) \,.$$ This is only defined if the integral exists, so it is possible for a continuous random variable to have undefined variance.
- [Chebyshev's inequality](../../../../general/Chebyshev's%20inequality.md) ::: The probability that a random variable deviates from its mean by at least $k\sigma$ is at most $1/k^{2}$, where $k$ is any positive constant and $\sigma$, required to be finite non-zero (also implies infinite expected value $\mu$), is the standard deviation (the square root of the variance): $$P(\lvert X - \mu \rvert \ge k \sigma) \le \frac 1 {k^2} \,.$$
  - Chebyshev's inequality / proof for continuous random variable ::: This a proof for continuous random variable, but a similar one applies for discrete random variable: $$\begin{aligned} P(\lvert X - \mu \rvert \ge k \sigma) & = \int_{\lvert x - \mu \rvert \ge k \sigma} \! f(x) \,\mathrm{d}x \\ & \le \int_{\lvert x - \mu \rvert \ge k \sigma} \! \frac {(x - \mu)^2} {k^2 \sigma^2} f(x) \,\mathrm{d}x \\ & = \frac 1 {k^2 \sigma^2} \operatorname{Var}(X) \\ & = \frac 1 {k^2} \,. \end{aligned}$$

## week 6 lecture 2

- datetime: 2024-10-09T10:30:00+08:00/2024-10-09T11:50:00+08:00
- [binomial distribution](../../../../general/binomial%20distribution.md) ::: The __binomial distribution__ with parameters _n_ and _p_ is the discrete probability distribution of the number of successes in a sequence of $n \in \mathbb N_0$ independent experiments, each asking a yes–no question, and each with its own Boolean-valued outcome: success (with probability $p \in [0, 1]$) or failure (with probability $q = 1 - p$). It is denoted $B(n, p)$.
  - binomial distribution / random variable ::: A single trial (_n_ = 1) is also known as a Bernoulli trial. Its random variable is: $$p(x) = \begin{cases} p & \text{for }x = 1 \\ 1 - p & \text{for }x = 0 \\ 0 & \text{otherwise} \,, \end{cases}$$ or sometimes more conveniently, $$p(x) = \begin{cases} p^x (1 - p)^{1 - x} & \text{for }x \in \set{0, 1} \\ 0 & \text{otherwise} \,. \end{cases}$$
  - binomial distribution / proof of being probability distribution ::: It is very easy to see that its probability mass function is nonnegative. To see that it sums up to 1, apply the binomial theorem in reverse.
  - binomial distribution / probability _mass_ function ::: For $X \sim B(n, p) \,,$ $$p_X(k) = \binom n k p^k (1 - p)^{n - k}\,.$$
  - binomial distribution / mean ::: For $X \sim B(n, p) \,,$ $$\operatorname E[X] = np \,.$$
  - binomial distribution / variance ::: For $X \sim B(n, p) \,,$ $$\operatorname{Var}(X) = np(1 - p) \,.$$
  - binomial distribution / _R_: evaluate PMF ::: `dbinom(<number of successes>, size=<number of trials>, prob=<success probability>)`
  - binomial distribution / _R_: evaluate CDF ::: `pbinom(<number of successes>, size=<number of trials>, prob=<success probability>)`
  - binomial distribution / _R_: realize ::: `rbinom(<number of successes>, size=<number of trials>, prob=<success probability>)`
- [Poisson distribution](../../../../general/Poisson%20distribution.md) ::: The __Poisson distribution__ is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time if these events occur with a known constant mean rate and independently of the time since the last event. It can also be used for the number of events in other types of intervals than time, and in dimension greater than 1 (e.g., number of events in a given area or volume). It is denoted $\operatorname{Pois}(\lambda)$, where $\lambda \in (0, \infty)$ is the expectation of number of events in a given interval.
  - Poisson distribution / probability _mass_ function ::: For $X \sim \operatorname{Pois}(\lambda) \,,$ $$p_X(k) = \begin{cases} e^{-\lambda} \frac {\lambda^k} {k!} & \text{for }x \in \mathbb N_0 \\ 0 & \text{otherwise} \,. \end{cases}$$
  - Poisson distribution / proof of being probability distribution ::: It is also very easy to see its probability mass function is nonnegative (in fact, positive). To see it sums up to 1, realize that the sum actually contains a Maclaurin expansion of $e^\lambda$.
  - Poisson distribution / mean ::: For $X \sim \operatorname{Pois}(\lambda) \,,$ $$\operatorname E[X] = \lambda \,.$$ To prove this, one will need to cancel _k_ in the denominator with the numerator in the sum when finding its expectation value.
  - Poisson distribution / variance ::: For $X \sim \operatorname{Pois}(\lambda) \,,$ $$\operatorname{Var}(X) = \lambda \,.$$ To prove this, one will need to cancel $k (k - 1)$ in the denominator with the numerator in the sum when finding its expectation value.
  - Poisson distribution / _R_: evaluate PMF ::: `dpois(<number of events>, lambda=<expectation value of number of events>)`
  - Poisson distribution / _R_: evaluate CDF ::: `ppois(<number of events>, lambda=<expectation value of number of events>)`
- [Poisson limit theorem](../../../../general/Poisson%20limit%20theorem.md) ::: The Poisson distribution may be used as an approximation to the binomial distribution, if $p_n$ is a sequence of real numbers in $[0, 1]$ such that the sequence $n p_n$ converges to a finite limit $\lambda$: $$\lim_{n \to \infty} \binom n k p_n^k (1 - p_n)^{n - k} = e^{-\lambda} \frac {\lambda^k} {k!} \,.$$. Informally, the Poisson distribution closely approximates the binomial distribution when _n_ is large.
- [continuous uniform distribution](../../../../general/continuous%20uniform%20distribution.md) ::: The __continuous uniform distribution__ describes uniform relative likelihood in between the interval _a_ and _b_ (both inclusive). It is denoted $U(a, b)$, where $-\infty < a < b < +\infty$.
  - continuous uniform distribution / probability _density_ function ::: For $X \sim U(a, b) \,,$ $$f(x) = \begin{cases} \frac 1 {b - a} & \text{for }a \le x \le b \\ 0 & \text{otherwise} \,. \end{cases}$$
  - continuous uniform distribution / proof of being probability distribution ::: It is extremely easy to see its probability density function is nonnegative and integrates up to 1 over the real numbers.
  - continuous uniform distribution / mean ::: For $X \sim U(a, b) \,,$ $$\operatorname E[X] = \frac {a + b} 2 \,.$$
  - continuous uniform distribution / variance ::: For $X \sim U(a, b) \,,$ $$\operatorname{Var}(X) = \frac {(b - a)^2} {12} \,.$$
- [normal distribution](../../../../general/normal%20distribution.md) ::: The __normal distribution__ or __Gaussian distribution__ is important in statistics and is often used in the natural and social sciences to represent real-valued random variables whose distributions are not known. Their importance is partly due to the central limit theorem. It is denoted $\mathcal N(\mu, \sigma^2)$, where $\mu \in \mathbb R$ is the mean and $\sigma^2 \in \mathbb R_{> 0}$ is the variance. <p> Note: When you see $\mathcal N(0, 100)$, do not mistake the 100 as the standard deviation! It is the variance. Almost screwed this up in the midterm examination...
  - normal distribution / probability _density_ function ::: For $X \sim \mathcal N(\mu, \sigma^2) \,,$ $$f(x) = \frac 1 {\sqrt{2\pi \sigma^2} } \exp\left(-\frac {(x - \mu)^2} {2 \sigma^2} \right) \,.$$
  - normal distribution / proof of being probability distribution ::: It is also very easy to see its probability density function is nonnegative (in fact, positive). To see it integrates up to 1 over the real numbers, integrate with respect to $t = \frac {x - \mu} {\sqrt 2 \sigma}$ first (substitution), then the resulting integral contains a Gaussian integral $\int_{-\infty}^\infty \! e^{-t^2} \,\mathrm{d}x$, which has no elementary antiderivative, but when evaluated over the real numbers, yields $\sqrt \pi$.
  - normal distribution / mean ::: For $X \sim \mathcal N\left(\mu, \sigma^2 \right) \,,$ $$\operatorname E[X] = \mu \,.$$ To prove this, turn the additional $x$ in the integrand into $(x - \mu + \mu)$, apply linearity of integration, and then substitute $t = \frac {x - \mu} {\sqrt 2 \sigma}$. Then the expression should contain a Gaussian integral and an integral that has an odd function as the integrand. The former integral is $\sqrt \pi$ and the latter integral is 0 by symmetry.
  - normal distribution / variance ::: For $X \sim \mathcal N\left(\mu, \sigma^2\right) \,,$ $$\operatorname{Var}(X) = \sigma^2 \,.$$ To prove this, substitute $t = \frac {x - \mu} {\sqrt 2 \sigma}$, then substitute $e^{-t^2}$, and finally apply integration by part. The resulting expression should contain an expression that is 0 and a Gaussian integral, which evaluates to $\sqrt \pi$.
  - normal distribution / shape ::: All normal distribution have the bell-shaped regardless of its parameters. Changing the mean simply translates the shape, while increasing the variance fattens (becomes wider) and flattens (the maximum value becomes lower) the shape.
  - normal distribution / examples ::: human height, one component of the velocity of a turbulent wind flow, Galton board
  - normal distribution / standard normal distribution ::: The __standard normal distribution__ has the mean, $\mu$, 0, and the variance, $\sigma^2$, 1. Its CDF is commonly denoted by $\Phi(z)$ while its PDF is commonly denoted by $\varphi(z)$. <p> A property of its CDF due to the even symmetry of its PDF: $$\Phi(-z) = 1 - \Phi(z) \,.$$
  - normal distribution / standardization ::: Any normal distribution can be __standardized__ by defining the random variable $$Z = \frac {X - \mu} {\sigma} \qquad X = \sigma Z + \mu \,.$$ Further, $$z = \frac {x - \mu} \sigma$$ is also known as the __standard score__ of the data _x_. <p> After standardization, a standard normal table that provides $\Phi(z)$ for different values of _z_ may be used to evaluate the CDF of any normal distribution. (The table may not show negative values of _z_. In that case, you need to use the property of its CDF above.)
  - normal distribution / _R_: evaluate CDF ::: `pnorm(<standard score>[, mean=<mean>][, sd=<standard deviation>])`

## week 6 tutorial

- datetime: 2024-10-11T09:30:00+08:00/2024-10-11T10:20:00+08:00
- public holiday: Chung Yeung Festival

## week 7 lecture

- datetime: 2024-10-14T10:30:00+08:00/2024-10-14T11:50:00+08:00
- [moment](../../../../general/moment%20(mathematics).md) ::: The ___k_-th (population) moment__ (also called __raw moment__), which is about _the origin_ (not about _the mean_), of a random variable _X_ is defined by $$\operatorname E\left[X^k \right] \qquad k \in \mathbb N_{\ge 1} \,,$$ if _it exists_. (When _k_ = 0 (the "zeroth" moment), this always equal to 1, so we ignore it here.) <p> A _k_-th moment exists if $\operatorname E\left[\left\lvert X^k \right\rvert\right] < \infty$ (Lebesgue integrable). If the _n_-th moment exists _about any point_, so does the $(n - 1)$-th moment (and thus, all lower-order moments) _about every point_.
  - moment / population mean ::: The population mean is the 1st _raw_ moment.
- [central moment](../../../../general/central%20moment.md) ::: The ___k_-th (population) central moment__, which is about _the mean_ (not about _the origin_), of a random variable _X_ is defined by $$\operatorname E\left[(X - \operatorname E[X])^k\right] \qquad k \in \mathbb N_{\ge 1} \,,$$ if _it exists_. (When _k_ = 0 (the "zeroth" moment), this always equal to 1, so we ignore it here.) <p> A _k_-th central moment exists if $\operatorname E[\lvert X \rvert] < \infty$ and $\operatorname E\left[\left\lvert (X - \operatorname E[X])^k \right\rvert \right] < \infty$ (both Lebesgue integrable). If the _n_-th moment exists _about any point_ (including the value $\operatorname E[X]$), so does the $(n - 1)$-moment (and thus, all lower-order moments) _about every point_.
  - central moment / population variance ::: The population variance is the 2nd _central_ moment.
  - standardized (central) moment ::: The ___k_-th standardized (central) moment__ is the _k_-th (central) moment that is standardized by dividing by $\sigma^k$, where $\sigma$ is the standard deviation. Mathematically, $$\tilde \mu_k = \frac {\mu_k} {\sigma^k} = \frac {\operatorname E\left[(X - \mu)^k \right]} {\operatorname E\left[(X - \mu)^2 \right]^{k / 2} } = \operatorname E\left[\left(\frac {X - \mu} \sigma \right)^k \right] \,.$$ <p> Hence, the 1st standardized central moment is 0, the 2nd standardized central moment is 1, the 3rd standardized central moment is the _skewness_, the 4th standardized central moment is the _kurtosis_, etc.
    - standardized central moment / skewness ::: __Skewness__ is the 3rd _standardized_ central moment: $$\tilde \mu_3 = \operatorname E\left[\left(\frac {X - \mu} \sigma\right)^3 \right] = \frac {\mu_3} {\sigma^3} \,.$$
    - standardized central moment / kurtosis ::: __Kurtosis__ is the 4th _standardized_ central moment: $$\tilde \mu_4 = \operatorname E\left[\left(\frac {X - \mu} \sigma\right)^4 \right] = \frac {\mu_4} {\sigma^4} \,.$$
- [skewness](../../../../general/skewness.md)
  - [skewness § relationship of mean and median](../../../../general/skewness.md#relationship%20of%20mean%20and%20median)
- [moment-generating function](../../../../general/moment-generating%20function.md) (MGF, mgf) ::: The __moment-generating function__ (__MGF__, __mgf__) of _a real-valued random variable_ is defined as $$M_X(t) = \operatorname E\left[e^{tX} \right] \,,$$ provided that _this expectation exists (and is finite) for $t$ in some open neighborhood (open interval) of 0_. Otherwise, the moment generating function does not exist (e.g. Cauchy distributions). <p> In this course, unless otherwise specified, we assume the MGF exists.
  - moment-generating function / use ::: Its primary use is finding the _k_-th raw moment of a real-valued random variable _X_. The _k_-th raw moment is obtained by evaluating the _k_-th derivative of its moment-generating function at 0: $$\operatorname E\left[X^k \right] = M_X^{(k)}(0) = \left[\frac {\mathrm d^k} {\mathrm dt^k} M_X(t) \right]\Bigr|_{t = 0} \qquad k \in \mathbb N_0 \,.$$ When _k_ = 0, the "zeroth" raw moment is always 1, and the above formula also gives 1. <p> The above can be proved by differentiating the expectation, assuming the interchange of the differentiation and expectation operator is legitimate.
  - moment-generating function / binomial distribution ::: For $X \sim B(n, p) \,,$ $$M_X(t) = \left(pe^t + 1 - p \right)^n \,.$$ To find the above function, merge $e^{tk}$ into $p^k$ and apply the binomial theorem in reverse.
  - moment-generating function / normal distribution ::: For $X \sim \mathcal N\left(\mu, \sigma^2 \right) \,,$ $$M_X(t) = \exp\left(\mu t + \frac {\sigma^2 t^2} 2 \right) \,.$$ To find the above function, merge $e^{tx}$ into $e^{-\frac {(x - \mu)^2} {2\sigma^2} }$, extracting the constants out and completing the square in the exponent to get a Gaussian integral $\int_{-\infty}^\infty \! e^{-x^2} \,\mathrm{d}x$, which yields $\sqrt \pi$. Another way to prove the above that may be easier is by finding the moment-generating function $M_Z(t)$ for the _standard_ normal distribution _Z_ first, then use the fact $X = \sigma Z + \mu$.

## week 7 lecture 2

- datetime: 2024-10-16T10:30:00+08:00/2024-10-16T11:50:00+08:00

## week 7 tutorial

- datetime: 2024-10-18T09:30:00+08:00/2024-10-18T10:20:00+08:00

## midterm exam

- datetime: 2024-10-20T14:00:00+08:00/2024-10-20T15:30:00+08:00, PT1H30M
- venue: Lecture Theater B (L1), Lecture Theater J (L2)
- report
  - When you see $\mathcal N(0, 100)$, do not mistake the 100 as the standard deviation! It is the variance. Almost screwed this up in the midterm examination...
  - Inputted $\binom {100} 1$ as 1 instead of 100 into the calculator when evaluating a binomial distribution...
