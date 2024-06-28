---
aliases:
  - IGR
  - information gain ratio
  - normalized information gain
tags:
  - flashcard/general/information_gain_ratio
  - language/in/English
---

# information gain ratio

## definition

The information gain ratio of an [attribute](feature%20(machine%20learning).md) $a$ on set a $T$ is defined as {{$$\operatorname{IGR}(T, a) = \frac {\operatorname{IG}(T, a)} {\Eta(a)}$$, where $\operatorname{IG}(T, a)$ is the [information gain](information%20gain%20(decision%20tree).md) and $\Eta(a)$ is the [entropy](entropy%20(information%20theory).md) of $a$ in $T$}}. Note that the latter entropy is also called {{the split information of $a$, $\operatorname{SplitInformation}(a)$}}, in this context. <!--SR:!2024-12-12,167,270!2024-10-11,121,290-->

## advantages

Information gain ratio {{makes [decision tree learning](decision%20tree%20learning.md) penalizes splitting on attributes with many possible values}}. <!--SR:!2024-08-08,77,270-->

## disadvantages

Attributes with too many possible values {{will never be considered over those with much lower ones}}. <!--SR:!2024-10-12,134,290-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/information_gain_ratio) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
