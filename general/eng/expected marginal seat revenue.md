---
aliases:
  - EMSR
  - EMSRs
  - expected marginal seat revenue
  - expected marginal seat revenues
tags:
  - flashcard/active/general/eng/expected_marginal_seat_revenue
  - language/in/English
---

# expected marginal seat revenue

<!-- | ![](../../archives/Wikimedia%20Commons/Edit-clear.svg) | This article __may be too technical for most readers to understand__. Please [help improve it](https://en.wikipedia.org/w/index.php?title=Expected_marginal_seat_revenue&action=edit) to [make it understandable to non-experts](https://en.wikipedia.org/wiki/Wikipedia:Make%20technical%20articles%20understandable), without removing the technical details. _\(November 2010\)__\([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance%20template%20removal)\)_ | -->

{@{__Expected Marginal Seat Revenue__ \(__EMSR__\)}@} and is {@{a very popular [heuristic](heuristic.md) in [Revenue Management](revenue%20management.md)}@}. There are {@{two versions}@}: {@{EMSRa<sup>[\[1\]](#^ref-1)</sup> and EMSRb}@},<sup>[\[2\]](#^ref-2)</sup> both of which were introduced by {@{[Peter Belobaba](Peter%20Belobaba.md)}@}. Both methods are for {@{_n_-class, static, single-resource problems}@}. Because {@{the models are static}@} {@{some assumptions apply}@}: classes are {@{indexed in such a way that the fare for the highest class, $r_{1}$}@}, is {@{higher than the fare for the next highest class, $r_{2}$, so $r_{1}$ \> $r_{2}$ \> ... \> $r_{n}$}@}; {@{demand arrives \(annotation: order of arrival\)}@} in {@{a strict low to high order in stages that are indexed with _j_ as well}@}; {@{demand for class _j_}@} is {@{distributed with cdf $F_{j}(x)$}@}. For {@{simplicity}@} it is also assumed that {@{demand, capacity and the distributions are continuous}@}, although it is {@{not very difficult to drop this assumption}@}. <!--SR:!2025-09-30,64,310!2025-10-02,66,310!2025-09-29,63,310!2025-10-03,67,310!2025-09-20,56,310!2025-09-30,64,310!2025-10-03,67,310!2025-10-01,65,310!2025-09-29,63,310!2025-10-01,65,310!2025-10-01,65,310!2025-09-29,63,310!2025-09-29,63,310!2025-09-30,64,310!2026-05-15,238,330!2026-05-06,230,330!2025-10-03,67,310-->

## EMSRa

{@{EMSRa}@} is {@{the first version that Belobaba devised}@}. The idea behind the heuristic is to {@{add the protection limits}@} that are {@{calculated by applying [Littlewood's rule](Littlewood's%20rule.md) to successive classes}@}. Suppose that we are {@{in stage _j+1_}@} and we want to {@{calculate how much capacity we need to protect for stages _j, j-1,..., 1_}@}. Then we are actually {@{calculating protection limit $y$<sub>j</sub>}@}. To do so we consider {@{every class in _j, j-1,..., 1_}@} and {@{compare that class, indexed with _k_, with _j+1_ in isolation}@}. For {@{every combination of _k_ and _j+1_}@} we compute {@{the protection level for that class with [Littlewood's rule](Littlewood's%20rule.md)}@}: {@{$$P(D_{k}>y_{k}^{j+1})={\frac {r_{j+1} }{r_{k} } }$$}@} {@{The idea of EMSRa}@} then is to add {@{all these protection limits to get the protection limit for $y_{j}$}@}. {@{$$y_{j}=\sum _{k=1}^{j}y_{k}^{j+1}$$}@} <!--SR:!2025-09-29,63,310!2025-09-30,64,310!2025-09-21,57,310!2025-10-02,66,310!2025-09-20,56,310!2025-10-03,67,310!2025-09-29,63,310!2025-10-03,67,310!2025-09-30,64,310!2025-09-20,56,310!2025-12-27,114,290!2025-10-02,66,310!2025-09-21,57,310!2026-02-18,166,310!2025-09-29,63,310-->

However, there is {@{a problem with this method}@} because {@{it does not take the statistical averaging effect into account}@}. Suppose, for example, that {@{classes _1_ to _j_ have the same fare _r_}@}, then EMSRa will {@{calculate the protection limit for $y_{j+1}$}@} with {@{$$P(D_{k}>y_{k}^{j+1})={\frac {r_{j+1} }{r} }$$}@} However, because {@{the fare for all these classes is the same}@} they {@{should be aggregated}@}. EMSRa will {@{calculate protection limits that are too conservative}@}. In other words, it will {@{reserve too many seats for the higher fares}@}, thereby {@{rejecting too many low fare bookings}@}. Although {@{having equal fares is not realistic}@} this will {@{also happen if the difference between fares is small}@}. Therefore {@{EMSRb was invented}@}. <!--SR:!2025-09-22,58,310!2026-05-08,232,330!2025-10-02,66,310!2025-09-29,63,310!2025-09-29,63,310!2025-09-29,63,310!2026-05-17,240,330!2025-09-22,58,310!2025-09-29,63,310!2025-10-01,65,310!2025-10-03,67,310!2026-05-16,239,330!2026-05-14,237,330-->

## EMSRb

{@{One of the most widely used RM heuristics}@} is {@{EMSRb}@}. It is {@{simple and produces under certain conditions close to optimal results}@}. Belobaba reports {@{studies in which both EMSRa and EMSRb were compared}@}. He shows that {@{EMSRb}@} is {@{consistently within 0.5 percent of the optimal solution}@}, while {@{EMSRa under certain conditions}@} can {@{deviate more than 1.5 percent from the optimal solution}@}. However, with {@{mixed order of arrival and frequent re-optimization}@} {@{both methods perform well}@}.<sup>[\[3\]](#^ref-3)</sup> There is also {@{study by Polt that shows mixed results}@}.<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2025-09-29,63,310!2025-09-30,64,310!2025-09-20,56,310!2025-09-30,64,310!2025-09-21,57,310!2025-10-01,65,310!2025-10-02,66,310!2025-09-29,63,310!2025-09-29,63,310!2025-09-21,57,310!2025-09-29,63,310-->

EMSRb is also {@{based on an approximation that compares two classes}@}, but it {@{does take the statistical averaging effect into account}@}. Instead of {@{aggregating protection levels, as EMSRa does}@}, it {@{aggregates demand}@}. Suppose we are again {@{in stage $j+1$}@} and we want to {@{calculate the protection limit $y$<sub>j</sub>}@}. Then first {@{all future demand for classes _j, j-1,…, 1_ is aggregated}@}: {@{$$S_{j}=\sum _{k=1}^{j}D_{k}$$}@} and {@{the weighted revenues are calculated}@}: {@{$${\overline {r} }_{j}={\frac {\sum _{k=1}^{j}r_{k}\cdot {\bar {D_{k} } } }{\sum _{k=1}^{j}{\bar {D_{k} } } } }$$ \(annotation: where $\bar D_k$ is the mean of the demand\)}@} Then, again with {@{Littlewood’s rule}@}, {@{the protection limit for classes _j_ and higher}@} is calculated such that: {@{$$P(S_{j}>y_{j})={\frac {r_{j+1} }{ {\overline {r} }_{j} } }$$}@} Rearranging gives: <!--SR:!2025-09-29,63,310!2026-05-09,233,330!2025-09-29,63,310!2025-09-22,58,310!2025-10-01,65,310!2026-05-10,234,330!2025-09-29,63,310!2025-09-29,63,310!2025-10-02,66,310!2025-09-29,63,310!2025-09-22,58,310!2025-10-03,67,310!2025-09-29,63,310-->

> {@{__EMSR Littlewood's rule__}@}
>
> {@{$$y_{j}^{\star }=F_{j}^{-1}\left(1-{\frac {r_{j+1} }{ {\overline {r} }_{j} } }\right)$$}@} <!--SR:!2025-09-29,63,310!2025-10-01,65,310-->

{@{$y_{j}^{\star }$}@} is {@{the optimal protection limit}@}, {@{$F_{j}(x)$}@} is {@{a [continuous distribution](continuous%20distribution.md#absolutely%20continuous%20probability%20distribution) used to model the demand}@}. Usually {@{demand is considered to be independent}@} and {@{distributed normally with a mean $\mu_j$ and a variance $\sigma_j$}@}. Using that the protection limits can be calculated as: {@{$$y_{j}=\mu _{j}+z_{\alpha }\cdot \sigma _{j}$$}@} with {@{the mean and variance of the demand}@} to come as {@{$\mu _{j}=\sum _{k=1}^{j}\mu _{k}$ and $\sigma _{j}^{2}=\sum _{k=1}^{j}\sigma _{k}^{2}$ respectively}@}. {@{$z_{\alpha }$}@} is {@{calculated with the inverse of the normal distribution $z_{\alpha }=\phi ^{-1}(1-{\frac {r_{j+1} }{ {\overline {r} }_{j} } })$}@}. This is {@{done for each j}@}, giving {@{the protection limit for every class}@}. <!--SR:!2025-10-02,66,310!2026-05-13,237,330!2025-09-22,58,310!2025-09-29,63,310!2025-09-29,63,310!2026-05-07,231,330!2026-05-13,236,330!2025-09-21,57,310!2025-09-29,63,310!2025-09-29,63,310!2025-09-29,63,310!2025-09-20,56,310!2025-09-29,63,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/expected_marginal_seat_revenue) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Belobaba, P. P., Air Travel Demand and Airline Seat Inventory Management. Flight Transportation Laboratory. Cambridge, MIT. PhD, 1987 <a id="^ref-1"></a>^ref-1
2. Belobaba, P. P., Optimal vs. heuristic methods for nested seat allocation. Presentation at ORSA/TIMS Joint National Meeting, 1992 <a id="^ref-2"></a>^ref-2
3. Belobaba, P. P., Optimal vs. heuristic methods for nested seat allocation. Presentation at ORSA/TIMS Joint National Meeting, 1992 <a id="^ref-3"></a>^ref-3
4. Polt, S., Back to the roots: New results on leg optimization. In 1999 AGIFORS Reservations and Yield Management Study Group Symposium, London, UK, 1999 <a id="^ref-4"></a>^ref-4

## see also

- [Yield management](yield%20management.md)
- [Littlewood's rule](Littlewood's%20rule.md)

> [Category](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Pricing](https://en.wikipedia.org/wiki/Category:Pricing)
