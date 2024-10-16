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
    - venue: LT-B (L1), LT-J (L2)
  - final exam: Make-up exam if absent due to special reasons, e.g. sick. Provide evidence.
- syllabus: descriptive statistics, probability theory, inferential statistics
  - syllabus / descriptive statistics: descriptive statistics
  - syllabus / probability theory: introduction to probability theory → discrete random variable, discrete probability distribution → continuous random variable, continuous probability distribution
  - syllabus / inferential statistics: estimation of parameters: point estimation, interval estimation → hypothesis testing → simple linear regression → other topics: goodness of fit test, etc.

## week 1 lecture

- time: 2024-09-02T10:30:00+08:00/2024-09-02T11:50:00+08:00
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

- time: 2024-09-02T10:30:00+08:00/2024-09-02T11:50:00+08:00
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
  - [skewness](../../../../general/skewness.md) ::: Intuitively for graphs, a distribution is left-skewed if its tail is on the left, and vice versa for right-skewed. Otherwise, it is unskewed. Intuitively for numbers, a distribution is left-skewed if its mean is on the left of (smaller than) its median, and vice versa for right-skewed. Otherwise, it is unskewed. (But actually, said intuition is very very wrong sometimes... See the item below.)
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

- time: 2024-09-06T09:30:00+08:00/2024-09-06T10:20:00+08:00
- unscheduled

## week 2 lecture 1

- time: 2024-09-09T10:30:00+08:00/2024-09-09T11:50:00+08:00
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
