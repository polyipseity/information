---
aliases:
  - mex
  - minimum excluded value
  - minimum excluded values
tags:
  - flashcard/active/general/eng/mex__mathematics_
  - language/in/English
---

# mex

In [mathematics](mathematics.md), {@{the __mex__ \("<!-- markdown separator -->__m__<!-- markdown separator -->inimum __ex__<!-- markdown separator -->cluded value"\)}@} of {@{a [subset](subset.md) of a [well-ordered](well-order.md) set is the smallest value from the whole set that does not belong to the subset}@}. That is, it is {@{the [minimum](maximum%20and%20minimum.md) value of the [complement set](complement%20(set%20theory).md)}@}. <!--SR:!2025-12-05,281,330!2025-10-31,253,330!2025-10-22,245,330-->

Beyond sets, {@{[subclasses](subclass%20(set%20theory).md) of well-ordered [classes](class%20(set%20theory).md) have minimum excluded values}@}. {@{Minimum excluded values of subclasses of the [ordinal numbers](ordinal%20number.md)}@} are {@{used in [combinatorial game theory](combinatorial%20game%20theory.md)}@} to {@{assign [nim-values](Sprague–Grundy%20theorem.md) to [impartial games](impartial%20game.md)}@}. According to {@{the [Sprague–Grundy theorem](Sprague–Grundy%20theorem.md)}@}, {@{the nim-value of a game position}@} is {@{the minimum excluded value of the class of values of the positions that can be reached in a single move from the given position}@}.<sup>[\[1\]](#^ref-1)</sup> <!--SR:!2025-11-27,275,330!2025-08-18,180,310!2025-10-24,247,330!2025-11-29,276,330!2026-08-15,457,310!2025-11-21,269,330!2025-12-09,235,270-->

{@{Minimum excluded values}@} are also {@{used in [graph theory](graph%20theory.md), in [greedy coloring](greedy%20coloring.md) algorithms}@}. These algorithms typically {@{choose an ordering of the vertices of a graph and choose a numbering of the available vertex colors}@}. They then {@{consider the vertices in order}@}, for {@{each vertex choosing its color to be the minimum excluded value of the set of colors already assigned to its neighbors}@}.<sup>[\[2\]](#^ref-2)</sup> <!--SR:!2025-11-01,254,330!2025-11-28,276,330!2027-07-17,724,330!2025-12-23,294,330!2026-08-13,447,310-->

## examples

The following examples all assume that {@{the given set is a subset of the class of [ordinal numbers](ordinal%20number.md)}@}: {@{$${\begin{array}{lcl}\operatorname {mex} (\emptyset )&=&0\\[2pt]\operatorname {mex} (\{1,2,3\})&=&0\\[2pt]\operatorname {mex} (\{0,2,4,6,\ldots \})&=&1\\[2pt]\operatorname {mex} (\{0,1,4,7,12\})&=&2\\[2pt]\operatorname {mex} (\{0,1,2,3,\ldots \})&=&\omega \\[2pt]\operatorname {mex} (\{0,1,2,3,\ldots ,\omega \})&=&\omega +1\end{array} }$$}@} where {@{_ω_ is the [limit ordinal](limit%20ordinal.md) for the natural numbers}@}. <!--SR:!2025-11-29,276,330!2025-11-27,275,330!2025-11-27,275,330-->

## game theory

In {@{the [Sprague–Grundy theory](Sprague–Grundy%20theorem.md)}@} {@{the minimum excluded ordinal is used to determine the [nimber](nimber.md) of a [normal-play](normal%20play%20convention.md) impartial game}@}. In such a game, {@{either player has the same moves in each position and the last player to move wins}@}. The nimber is {@{equal to 0 for a game that is lost immediately by the first player}@}, and is {@{equal to the mex of the nimbers of all possible next positions for any other game}@}. <!--SR:!2025-11-24,272,330!2025-12-05,281,330!2025-08-14,176,310!2025-12-15,289,330!2025-12-16,290,330-->

For example, in {@{a one-pile version of [Nim](Nim.md)}@}, the game starts with {@{a pile of _n_ stones}@}, and the player {@{to move may take any positive number of stones}@}. If {@{_n_ is zero stones}@}, {@{the nimber is 0 because the mex of the empty set of legal moves is the nimber 0}@}. If {@{_n_ is 1 stone}@}, {@{the player to move will leave 0 stones, and mex\({0}\) = 1}@}, gives {@{the nimber for this case}@}. If {@{_n_ is 2 stones}@}, {@{the player to move can leave 0 or 1 stones}@}, giving {@{the nimber 2 as the mex of the nimbers {0, 1}<!-- flashcard separator -->}@}. In general, {@{the player to move with a pile of _n_ stones can leave anywhere from 0 to _n_ − 1 stones}@}; the mex of {@{the nimbers {0, 1, …, _n_ − 1} is always the nimber _n_<!-- markdown separator -->}@}. {@{The first player wins in Nim}@} {@{if and only if the nimber is not zero}@}, so from this analysis we can conclude that {@{the first player wins if and only if the starting number of stones in a one-pile game of Nim is not zero}@}; the winning move is {@{to take all the stones}@}. <!--SR:!2025-11-24,272,330!2025-12-10,285,330!2025-10-22,245,330!2025-11-26,274,330!2025-11-22,270,330!2025-11-17,266,330!2025-11-23,272,330!2025-10-30,252,330!2025-11-18,267,330!2025-12-10,285,330!2025-10-30,252,330!2025-10-23,246,330!2025-08-09,182,310!2025-11-02,255,330!2025-10-31,253,330!2025-11-23,271,330!2025-11-26,274,330-->

If {@{we change the game so that the player to move can take up to 3 stones only}@}, then {@{with _n_ = 4 stones}@}, {@{the successor states have nimbers {1, 2, 3}, giving a mex of 0}@}. Since {@{the nimber for 4 stones is 0}@}, {@{the first player loses}@}. The second player's strategy is {@{to respond to whatever move the first player makes by taking the rest of the stones}@}. For {@{_n_ = 5 stones}@}, {@{the nimbers of the successor states of 2, 3, and 4 stones are the nimbers 2, 3, and 0 \(as we just calculated\)}@}; {@{the mex of the set of nimbers {0, 2, 3} is the nimber 1}@}, so {@{starting with 5 stones in this game is a win for the first player}@}. <!--SR:!2025-11-28,276,330!2025-11-25,273,330!2025-08-13,185,310!2025-10-21,244,330!2025-11-25,273,330!2026-09-03,473,310!2025-10-20,243,330!2025-11-22,271,330!2025-11-01,254,330!2026-08-28,467,310-->

{@{See [nimbers](nimber.md)}@} for {@{more details on the meaning of nimber values}@}. <!--SR:!2025-11-28,276,330!2025-12-22,293,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/mex_(mathematics)) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. [Conway, John H.](John%20Horton%20Conway.md) \(2001\). _[On Numbers and Games](On%20Numbers%20and%20Games.md)_ \(2nd ed.\). A.K. Peters. p. 124. [ISBN](ISBN.md) [1-56881-127-6](https://en.wikipedia.org/wiki/Special:BookSources/1-56881-127-6). <a id="^ref-1"></a>^ref-1
2. Welsh, D. J. A.; Powell, M. B. \(1967\). ["An upper bound for the chromatic number of a graph and its application to timetabling problems"](https://doi.org/10.1093%2Fcomjnl%2F10.1.85). _[The Computer Journal](The%20Computer%20Journal.md)_<!-- markdown separator -->. __10__ \(1\): 85–86. [doi](digital%20object%20identifier.md):[10.1093/comjnl/10.1.85](https://doi.org/10.1093%2Fcomjnl%2F10.1.85). <a id="^ref-2"></a>^ref-2
