---
aliases:
  - test data set
  - test data sets
  - test dataset
  - test datasets
  - testing data set
  - testing data sets
  - testing dataset
  - testing datasets
  - training data set
  - training data sets
  - training dataset
  - training datasets
  - training, validation, and test data set
  - training, validation, and test data sets
  - training, validation, and test dataset
  - training, validation, and test datasets
  - validation data set
  - validation data sets
  - validation dataset
  - validation datasets
tags:
  - flashcard/general/training__validation__and_test_data_sets
  - language/in/English
---

# training, validation, and test data sets

{{The model is initially fit}} on a __training data set__, which is {{a set of samples to adjust the model parameters (e.g. weights between [neurons](artificial%20neuron.md) in [neural networks](neural%20network%20(machine%20learning).md))}}. <!--SR:!2024-06-29,11,270!2024-06-30,12,270-->

Subsequently, {{the fitted model is used to predict samples}} in a second data set called the __validation data set__. The validation data set provides {{an unbiased evaluation of a model fit on the training data set}}, so that {{[hyperparameters](hyperparameter%20(machine%20learning).md) (e.g. number of layers and layer widths in [neural networks](neural%20network%20(machine%20learning).md)) can be tuned}}. <!--SR:!2024-07-05,17,290!2024-06-28,10,270!2024-06-30,12,270-->

Finally, the __test data set__ is {{a data set used to provide an unbiased evaluation of the _final_ model fit on the training data set}}. <!--SR:!2024-07-01,13,270-->

When the model is put into actual use, the data provided is called the {{__new data set__}} and {{do not contain the actual values of attributes being predicted to compare against}}. <!--SR:!2024-07-02,14,290!2024-07-12,17,250-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/training,_validation,_and_test_data_sets) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
