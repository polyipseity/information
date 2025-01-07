---
aliases:
  - PCA
  - PCAs
  - principal component
  - principal component analysis
  - principal components
tags:
  - flashcard/active/general/eng/principal_component_analysis
  - language/in/English
---

# principal component analysis

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## overview

PCA is most commonly used when {@{many of the variables are highly correlated with each other and it is desirable to reduce the number of variables (e.g. accuracy, efficiency)}@}. PCA allows us to {@{reduce the number of dimensions in the data set while minimizing information loss}@}. <!--SR:!2025-06-06,274,330!2025-05-14,256,330-->

## intuition

PCA can be thought of {@{fitting an (hyper)[ellipsoid](ellipsoid.md) (a (hyper)[sphere](sphere.md) that are scaled differently along different axes) to the data}@}, where each axis {@{of the ellipsoid (which are perpendicular to each other) represents a principal component}@}. The axis {@{length represents the variance of the data along that axis}@}. Axes with the least length means {@{the data does not differ much in said axis}@}, thus removing said axes {@{reduces dimensionality while minimizing information loss}@}. <!--SR:!2025-01-23,164,310!2025-10-07,346,290!2026-04-11,484,310!2025-04-13,230,330!2025-01-31,170,310-->

## computing PCA using the covariance method

The following is a detailed description of PCA using {@{the covariance method as opposed to the correlation method}@}. <!--SR:!2025-01-11,152,310-->

The goal is to {@{transform a given data set __X__ of dimension _p_ to another data set __Y__ of dimension _l_, where $p \ge l$}@}. Equivalently, matrix __Y__ is {@{the [Karhunen–Loève transform](Kosambi–Karhunen–Loève%20theorem.md) (KLT) of matrix __X__}@}: {@{$$\mathbf{Y} = \mathbb{KLT}\{\mathbf{X}\}$$}@} <!--SR:!2026-06-01,524,310!2025-06-29,293,330!2025-05-29,267,330-->

```Python
# pytextgen generate data
from asyncio import gather
from itertools import chain
from pytextgen.util import Result
steps = """
organize the data set
calculate the empirical mean
calculate the deviations from the mean
find the covariance matrix
find the eigenvectors and eigenvalues of the covariance matrix
rearrange the eigenvectors and eigenvalues
compute the cumulative variance for each eigenvector
select a subset of the eigenvectors as the new basis vectors
project the data (deviations from the mean) onto the new basis
""".strip().splitlines()
return chain(
  await memorize_seq(
      __env__.cwf_sects("f123", "dd23"),
      steps,
  ),
  (
    Result(
      location=loc,
      text=step,
    ) for loc, step in zip(__env__.cwf_sects(
      "23aa", "d123", "f2f3", "a290", "f735", "ef78", "dd01", "c123", "f098",
    ), steps, strict=True)
  ),
)
```

<!--pytextgen generate section="f123"--><!-- The following content is generated at 2024-11-12T13:56:48.800677+08:00. Any edits will be overridden! -->

> 1. organize the data set
> 2. calculate the empirical mean
> 3. calculate the deviations from the mean
> 4. find the covariance matrix
> 5. find the eigenvectors and eigenvalues of the covariance matrix
> 6. rearrange the eigenvectors and eigenvalues
> 7. compute the cumulative variance for each eigenvector
> 8. select a subset of the eigenvectors as the new basis vectors
> 9. project the data (deviations from the mean) onto the new basis

<!--/pytextgen-->

<!--pytextgen generate section="dd23"--><!-- The following content is generated at 2024-11-12T13:56:48.838480+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←organize the data set <!--SR:!2025-10-12,330,290!2025-01-30,171,310-->
- organize the data set→::@::←calculate the empirical mean <!--SR:!2025-12-22,368,290!2025-12-04,356,290-->
- calculate the empirical mean→::@::←calculate the deviations from the mean <!--SR:!2025-07-25,312,330!2026-01-19,433,310-->
- calculate the deviations from the mean→::@::←find the covariance matrix <!--SR:!2025-02-03,176,310!2026-05-28,534,310-->
- find the covariance matrix→::@::←find the eigenvectors and eigenvalues of the covariance matrix <!--SR:!2025-10-05,316,290!2026-05-17,533,330-->
- find the eigenvectors and eigenvalues of the covariance matrix→::@::←rearrange the eigenvectors and eigenvalues <!--SR:!2025-03-08,186,270!2025-04-08,199,290-->
- rearrange the eigenvectors and eigenvalues→::@::←compute the cumulative variance for each eigenvector <!--SR:!2025-02-19,184,310!2025-01-20,147,290-->
- compute the cumulative variance for each eigenvector→::@::←select a subset of the eigenvectors as the new basis vectors <!--SR:!2025-04-13,218,290!2025-03-01,168,270-->
- select a subset of the eigenvectors as the new basis vectors→::@::←project the data (deviations from the mean) onto the new basis <!--SR:!2025-05-27,221,270!2025-01-13,158,310-->
- project the data (deviations from the mean) onto the new basis→::@::←_(end)_ <!--SR:!2025-01-31,172,310!2025-01-21,166,310-->

<!--/pytextgen-->

1. __<!--pytextgen generate section="23aa"--><!-- The following content is generated at 2024-06-11T22:43:08.251405+08:00. Any edits will be overridden! -->organize the data set<!--/pytextgen-->__
    - Suppose you have a set of {@{_n_ observations of _p_ variables}@}, and you want to {@{reduce the data set to only $l \le p$ variables}@}.
    - Make the matrix __X__ by {@{writing the _n_ observations $\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_n$ each as a row vector with _p_ elements}@}, and then {@{combine the row vectors vertically to make a _n_ × _p_ matrix}@}.
2. __<!--pytextgen generate section="d123"--><!-- The following content is generated at 2024-06-11T22:43:08.494067+08:00. Any edits will be overridden! -->calculate the empirical mean<!--/pytextgen-->__
    - Find {@{the mean vector __u__ of the _n_ observations}@}: {@{$$\mathbf{u} = \frac 1 n \sum_{i = 1}^n \mathbf{x}_i$$}@}. That is, each column of matrix __X__ is {@{summed up and divided by _n_ to make a 1 × _p_ row vector}@}.
3. __<!--pytextgen generate section="f2f3"--><!-- The following content is generated at 2024-06-11T22:43:08.364782+08:00. Any edits will be overridden! -->calculate the deviations from the mean<!--/pytextgen-->__
    - Subtract {@{the mean vector __u__ from each row of the data matrix __X__ to get another _n_ × _p_ matrix __B__}@}: {@{$$\mathbf{B} = \mathbf{X} - \mathbf{h} \mathbf{u}$$, where $\mathbf{h}$ is a _n_ × 1 column vector with all values 1 ($\mathbf{h}$ simply duplicates the mean vector __u__)}@}.
    - In some applications, each variable of matrix __B__ may be {@{scaled to have a variance equal to 1}@}. This affects {@{the calculated principal components}@}, but makes them {@{independent of the measurement units}@}.
4. __<!--pytextgen generate section="a290"--><!-- The following content is generated at 2024-06-11T22:43:08.535766+08:00. Any edits will be overridden! -->find the covariance matrix<!--/pytextgen-->__
    - Find {@{the _p_ × _p_ empirical [covariance matrix](covariance%20matrix.md) __C__ from matrix __B__}@}: {@{$$\mathbf{C} = \frac 1 {n - 1} \mathbf{B}^* \mathbf{B}$$}@}
    - $*$ is {@{the [conjugate transpose](conjugate%20transpose.md) operator}@}. If __B__ {@{consists of real numbers only}@}, which is true for most applications, then $*$ is {@{the same as the regular [transpose](transpose.md) $\intercal$}@}.
    - $n - 1$ is used instead of _n_ to calculate the covariance because of {@{[Bessel's correction](Bessel's%20correction.md)}@}.
5. __<!--pytextgen generate section="f735"--><!-- The following content is generated at 2024-06-11T22:43:08.179112+08:00. Any edits will be overridden! -->find the eigenvectors and eigenvalues of the covariance matrix<!--/pytextgen-->__
    - Compute {@{the _p_ × _p_ matrix __V__ of [eigenvectors](eigenvalues%20and%20eigenvectors.md) which [diagonalizes](diagonalizable%20matrix.md) the covariance matrix __C__ into its corresponding _p_ × _p_ [diagonal matrix](diagonal%20matrix.md) __D__ of [eigenvalues](eigenvalues%20and%20eigenvectors.md) (the eigenvalues are stored in the diagonals)}@}: {@{$$\mathbf{V}^{-1} \mathbf{C} \mathbf{V} = \mathbf{D}$$}@}.
    - Ensure the [eigenvectors](eigenvalues%20and%20eigenvectors.md) are {@{normalized so that their lengths are 1}@}.
    - The step would likely involve {@{a computer-based algorithm for [computing eigenvectors and eigenvalues](eigendecomposition%20of%20a%20matrix.md)}@}. For few dimensions, the eigenvalues may be [calculated directly](eigenvalues%20and%20eigenvectors.md#classical%20method).
6. __<!--pytextgen generate section="ef78"--><!-- The following content is generated at 2024-06-11T22:43:08.554349+08:00. Any edits will be overridden! -->rearrange the eigenvectors and eigenvalues<!--/pytextgen-->__
    - Sort {@{the columns of the eigenvector matrix __V__ and eigenvalue matrix __D__ in order of _decreasing_ eigenvalue}@}.
    - Make sure {@{the pairings between the 2 matrices are maintained}@}.
7. __<!--pytextgen generate section="dd01"--><!-- The following content is generated at 2024-06-11T22:43:08.410586+08:00. Any edits will be overridden! -->compute the cumulative variance for each eigenvector<!--/pytextgen-->__
    - The eigenvalues {@{represent the distribution of the data's variance among each of the eigenvector}@}. The cumulative variance _g_ for the _j_-th eigenvector is {@{simply the sum of the eigenvalues from the 1st to the _j_-th eigenvector}@}: {@{$$g_j = \sum_{i = 1}^j \mathbf{D}_{ii} \quad \forall j \in \set{1, \ldots, p}$$}@}
8. __<!--pytextgen generate section="c123"--><!-- The following content is generated at 2024-06-25T17:37:48.434481+08:00. Any edits will be overridden! -->select a subset of the eigenvectors as the new basis vectors<!--/pytextgen-->__
    - Use the cumulative variances as {@{a guide for choosing an appropriate value for the number of reduced dimensions _l_}@}. The goal is to {@{choose the smallest _l_ possible while ensuring the _l_-th cumulative variance _g<sub>l</sub>_ is reasonably high on a percentage basis}@}. For example, {@{one can choose the smallest _l_ such that $\frac {g_l} {g_p} \ge 0.9$}@}.
    - After choosing _l_ (or _l_ is given beforehand), only keep {@{the first _l_ columns of the eigenvector _V_ to make a _p_ × _l_ matrix __W__ and discard the rest}@}.
9. __<!--pytextgen generate section="f098"--><!-- The following content is generated at 2024-11-12T13:56:48.778590+08:00. Any edits will be overridden! -->project the data (deviations from the mean) onto the new basis<!--/pytextgen-->__
    - The projected data points are {@{the rows of the _n_ × _l_ matrix __T__}@}, computed by {@{$$\mathbf{T} = \mathbf{B} \mathbf{W}$$}@}. Note that {@{the deviations from the mean instead of the original data points are used}@}. Using the latter is {@{also acceptable as a variant}@}. <!--SR:!2025-04-06,227,330!2025-03-16,209,330!2025-05-03,247,330!2026-06-03,536,310!2025-05-31,252,290!2025-04-06,207,310!2025-03-01,182,310!2025-09-21,333,290!2025-02-15,176,290!2025-07-28,293,290!2025-04-21,219,310!2025-01-10,146,290!2025-03-13,179,270!2025-05-16,138,270!2026-07-18,557,310!2025-02-26,190,310!2025-01-21,164,310!2025-03-11,204,330!2025-08-14,285,290!2025-08-29,265,250!2025-12-07,401,310!2025-06-04,223,270!2025-06-08,274,330!2026-10-13,648,330!2025-05-11,206,270!2026-05-02,511,310!2026-06-23,553,310!2025-08-02,309,310!2026-02-13,423,310!2026-04-05,490,310!2025-02-02,141,250!2025-03-10,174,270!2025-05-11,206,270!2025-03-28,83,361!2025-03-27,82,361-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/principal_component_analysis) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
