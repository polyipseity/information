---
aliases:
  - cumulative gain chart
  - cumulative gain charts
  - decile-wise lift chart
  - decile-wise lift charts
  - gain chart
  - gain charts
  - lift chart
  - lift charts
tags:
  - flashcard/active/special/lift_chart
  - language/in/English
---

# lift chart

A __lift chart__, also called {@{__cumulative gain chart__, or just __gain chart__}@}, is a chart that {@{visualizes the effect of a predictive [classification](../general/statistical%20classification.md) model}@}.

A __decile-wise lift chart__ is a variant of the lift chart that {@{visualizes the [lift](../general/association%20rule%20learning.md#lift) in the ten [deciles](../general/decile.md) of the data}@}.

## construction

To construct a lift chart, first select {@{an attribute as the outcome attribute to predict}@}. Then, {@{choose a possible value of that attribute as "success"}@}. The attribute is {@{usually discrete, but can be continuous if a "success" value can be defined at an endpoint of the attribute range}@}. Then, {@{choose a possible value of that attribute as "success". For continuous attributes, this means the closer a datum is to the "success" value, the more "successful" the data is}@}. Then have your model {@{predict the outcome attribute}@}. The prediction outcome is {@{usually discrete, but can be continuous if it can be ordered consistent with the discretized attribute, like the prediction outcome is a confidence of the attribute being the "success" value}@}. Now order the entire dataset {@{according to the predicted outcome, then the actual outcome, and then arbitrarily if there is still a tie. "Success" value must have the highest priority}@}. Finally, inspect the dataset {@{following the above order. Plot the cumulative number of observations that have the "success" value as the actual outcome (_y_-axis, labeled "cumulative") against the number of observations inspected (_x_-axis, labeled "# cases") using a curve graph. This is the _lift curve_}@}. Also plot {@{the _baseline curve_ representing the average performance of all possible classifiers, which is simply a line between the start of the lift curve and the end of the lift curve}@}.

> [!example] examples
>
> {@{A quick example}@} below.
>
> {@{![lift chart example](attachments/Pasted%20image%2020240322145601.png)}@}

### decile-wise

To construct a decile-wise lift chart, {@{follow the same [instructions above](#construction) up until before plotting}@}. Then, {@{split the data into ten equal portions called deciles, preserving order. The 1st decile is the first 10% of the dataset, and so on. If a decile split is in the middle of an observation, choose a splitting policy that fits your scenario best}@}. One possible way is to {@{weight the sample based on the split proportion}@}. Then, calculate {@{the global mean of the _actual_ outcome for the entire dataset, and the decile mean of the _actual_ outcome for each decile. For a boolean outcome attribute, you can consider the "success" value as 1 and the other value as 0}@}. Next, calculate {@{the decile mean divided by the global mean for each decile}@}. Finally, {@{plot the decile mean divided by the global mean (_y_-axis, label "decile mean/global mean") over the ten deciles (_x_-axis, label "deciles") in a bar chart}@}.

> [!example] examples
>
> {@{A quick example}@} below, using the same data as above.
>
> {@{![decile-wise lift chart example](attachments/Pasted%20image%2020240322164126.png)}@}

## interpretation

For the normal lift chart, the baseline curve represents {@{the average lift curve of all possible classifiers}@}. Consider {@{the area enclosed between the model curve and the baseline curve}@}. Treat {@{all enclosed areas above the baseline curve as positive and below the baseline curve as negative, which we will call the _signed area_ here}@}. Add {@{the signed areas together}@}. The larger the signed area, {@{the better the model at predicting the "success" value, and vice versa}@}.

For the decile-wise lift chart, the classifier is ideal when {@{the bars are maximum starting from the first decile, dropping off suddenly in one of the decile, and then zero for the rest of the deciles}@}.
