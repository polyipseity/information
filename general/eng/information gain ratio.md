---
aliases:
  - IGR
  - information gain ratio
  - normalized information gain
tags:
  - flashcard/active/general/eng/information_gain_ratio
  - language/in/English
---

# information gain ratio

## definition

The information gain ratio of an [attribute](feature%20(machine%20learning).md) $a$ on set a $T$ is defined as {@{$$\operatorname{IGR}(T, a) = \frac {\operatorname{IG}(T, a)} {\Eta(a)}$$, where $\operatorname{IG}(T, a)$ is the [information gain](information%20gain%20(decision%20tree).md) and $\Eta(a)$ is the [entropy](entropy%20(information%20theory).md) of $a$ in $T$}@}. Note that the latter entropy is also called {@{the split information of $a$, $\operatorname{SplitInformation}(a)$}@}, in this context. <!--SR:!fsrs,2032-08-12T00:00:00.000Z,2164,2164.24752053,1.98030797,2,10,0,0,2026-09-09T00:00:00.000Z!2032-03-08,2190,330-->

## advantages

Information gain ratio {@{makes [decision tree learning](decision%20tree%20learning.md) penalizes splitting on attributes with many possible values}@}. <!--SR:!fsrs,2030-01-22T00:00:00.000Z,1222,1221.87355897,4.74047837,2,10,0,0,2026-09-18T00:00:00.000Z-->

## disadvantages

Attributes with too many possible values {@{will never be considered over those with much lower ones}@}. <!--SR:!2032-08-12,2318,330-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/information_gain_ratio) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
