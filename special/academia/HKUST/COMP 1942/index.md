---
aliases:
  - COMP 1942
  - COMP 1942 index
  - COMP1942
  - COMP1942 index
  - HKUST COMP 1942
  - HKUST COMP 1942 index
  - HKUST COMP1942
  - HKUST COMP1942 index
tags:
  - flashcard/active/special/academia/HKUST/COMP_1942/index
  - function/index
  - language/in/English
---

# index

- HKUST COMP 1942
- name: Exploring and Visualizing Data

The content is in teaching order.

## week 1 lecture

- datetime: 2024-01-31T09:00:00+08:00/2024-01-31T10:30:00+08:00
- 6 major topics ::@:: association, clustering, classification, data warehouse, dimension reduction, web database <!--SR:!2025-02-23,224,250!2025-01-13,260,330-->
- association ::@:: Finding frequent _patterns_, e.g. frequent items and _item sets_, and _association rules_, e.g. the likelihood of A implying B. <!--SR:!2026-02-11,531,310!2026-11-10,719,330-->
- clustering ::@:: Finding all _clusters_, e.g. the clusters of items after graphing them in a 2D graph. <!--SR:!2027-02-01,818,330!2025-02-08,282,330-->
- classification ::@:: _Predict_ results given some input data, e.g. decision trees. <!--SR:!2025-11-06,462,310!2025-02-16,286,330-->
- data warehouse ::@:: Knowledge database containing _pre-computed_ results from data sources. <!--SR:!2026-11-20,771,330!2026-07-09,660,330-->
- dimension reduction ::@:: Reducing _dimensionality_ while minimizing _information loss_. One can visualize this by imagine many data points lying close to a line in a $xy$ graph. Then instead of representing each data point with two numbers, $x$ and $y$, we can represent each data point with one number representing the distance from the origin to the point on the line closest to the original data point. Information loss is the distance between the original point and the point on the line closest to the origin point. <!--SR:!2025-06-27,333,290!2027-03-19,853,330-->
- web database ::@:: Using data from the web, e.g. ranking webpages. <!--SR:!2025-02-05,278,330!2025-02-28,295,330-->
- [delimiter](../../../../general/delimiter.md) definition ::@:: The text each data point is separated by. For example, `column 1,column 2,column 3` is delimited by `,`. <!--SR:!2025-01-23,269,330!2025-01-13,261,330-->

## week 2 lecture 1

- datetime: 2024-02-05T09:00:00+08:00/2024-02-05T10:30:00+08:00
- [association rule learning § support](../../../../general/association%20rule%20learning.md#support)
- support definition ::@:: We use "the number of transactions containing $X$" definition here. <!--SR:!2028-03-18,1165,350!2027-03-08,804,330-->
- [association rule learning § confidence](../../../../general/association%20rule%20learning.md#confidence)
- [association rule learning § lift](../../../../general/association%20rule%20learning.md#lift)
- [association rule learning § naive algorithms](../../../../general/association%20rule%20learning.md#naive%20algorithms)

## week 2 lecture 2

- datetime: 2024-02-07T09:00:00+08:00/2024-02-07T10:30:00+08:00
- [association rule learning § naive algorithms](../../../../general/association%20rule%20learning.md#naive%20algorithms)
- [Apriori algorithm § overview](../../../../general/Apriori%20algorithm.md#overview)

## week 3 lecture

- datetime: 2024-02-14T09:00:00+08:00/2024-02-14T10:30:00+08:00
- [Apriori algorithm § overview](../../../../general/Apriori%20algorithm.md#overview)
- [Apriori algorithm § the algorithm](../../../../general/Apriori%20algorithm.md#the%20algorithm)
- [Apriori algorithm § limitations](../../../../general/Apriori%20algorithm.md#limitations)
- [FP-growth algorithm § overview](../../../../general/FP-growth%20algorithm.md#overview)

## week 4 lecture 1

- datetime: 2024-02-19T09:00:00+08:00/2024-02-19T10:30:00+08:00
- [FP-growth algorithm § FP-tree](../../../../general/FP-growth%20algorithm.md#FP-tree)
- [FP-growth algorithm § growth](../../../../general/FP-growth%20algorithm.md#growth)
  - FP-growth algorithm growth step ::@:: We use the slightly modified algorithm, never return an empty item set, and use the growth shortcut. <!--SR:!2027-03-21,831,351!2027-01-15,735,347-->
- [FP-growth algorithm § growth shortcut](../../../../general/FP-growth%20algorithm.md#growth%20shortcut)
- project phase 1
  - deadline: 2024-02-21T09:00:00+08:00

## week 4 tutorial

- datetime: 2024-02-19T18:00:00+08:00/2024-02-19T19:00:00+08:00
- optional
- topic: helping students who encountered problems of using XLMiner in our CSE lab and using XLMiner outside CSE Lab
- [Analytics Solver usage § installation](../../../Analytic%20Solver%20usage.md#installation)

## week 4 lecture 2

- datetime: 2024-02-21T09:00:00+08:00/2024-02-21T10:30:00+08:00
- [FP-growth algorithm § growth](../../../../general/FP-growth%20algorithm.md#growth)
- [FP-growth algorithm § growth shortcut](../../../../general/FP-growth%20algorithm.md#growth%20shortcut)
- [FP-growth algorithm § complexity](../../../../general/FP-growth%20algorithm.md#complexity)
- [cluster analysis § applications](../../../../general/cluster%20analysis.md#applications)

## week 5 lecture 1

- datetime: 2024-02-26T09:00:00+08:00/2024-02-26T10:30:00+08:00
- [_k_-means clustering § standard algorithm (naive _k_-means)](../../../../general/k-means%20clustering.md#standard%20algorithm%20(naive%20_k_-means))
- [_k_-means clustering § initialization methods](../../../../general/k-means%20clustering.md#initialization%20methods)
- [_k_-means clustering § discussion](../../../../general/k-means%20clustering.md#discussion)
- [_k_-means clustering § variations](../../../../general/k-means%20clustering.md#variations)
  - _k_-means clustering variations ::@:: We only teach original _k_-means, sequential _k_-means and forgetful sequential _k_-means. <!--SR:!2027-07-16,939,371!2027-10-10,1008,371-->

## week 5 tutorial

- datetime: 2024-02-26T18:00:00+08:00/2024-02-26T19:00:00+08:00
- topic: using XLMiner for association rule mining
- [association rule learning § useful concepts](../../../../general/association%20rule%20learning.md#useful%20concepts)
- [association rule learning § algorithms](../../../../general/association%20rule%20learning.md#algorithms)
- [Analytics Solver usage § usage](../../../Analytic%20Solver%20usage.md#usage)
- [Analytics Solver usage § input formats](../../../Analytic%20Solver%20usage.md#input%20formats)

## week 5 lecture 2

- datetime: 2024-02-28T09:00:00+08:00/2024-02-28T10:30:00+08:00
- [_k_-means clustering § variations](../../../../general/k-means%20clustering.md#variations)
- [Analytics Solver usage § random seed](../../../Analytic%20Solver%20usage.md#random%20seed)
- [hierarchial clustering](../../../../general/hierarchical%20clustering.md)
- [hierarchial clustering § cluster linkage](../../../../general/hierarchical%20clustering.md#cluster%20linkage)
  - cluster linkage ::@:: We only teach single-linkage, centroid linkage, complete-linkage, group average linkage (unweighted average linkage), median linkage, McQuitty's method (weighted average linkage), and Ward's method (minimum increase of sum of squares). <!--SR:!2025-04-11,240,291!2027-07-13,933,367-->
- [hierarchial clustering § agglomerative clustering](../../../../general/hierarchical%20clustering.md#agglomerative%20clustering)

## week 6 lecture 1

- datetime: 2024-03-04T09:00:00+08:00/2024-03-04T10:30:00+08:00
- [hierarchial clustering § cluster linkage](../../../../general/hierarchical%20clustering.md#cluster%20linkage)
- [hierarchial clustering § agglomerative clustering](../../../../general/hierarchical%20clustering.md#agglomerative%20clustering)
- [hierarchial clustering § divisive clustering](../../../../general/hierarchical%20clustering.md#divisive%20clustering)
  - divisive clustering ::@:: We prefer divisive clustering to stop after a certain amount of clusters are created instead of using the [dendrogram](../../../../general/dendrogram.md). <!--SR:!2025-08-05,332,311!2025-02-07,234,347-->
- [hierarchial clustering § monothetic clustering](../../../../general/hierarchical%20clustering.md#monothetic%20clustering)
- [hierarchial clustering § chi-squared monothetic clustering](../../../../general/hierarchical%20clustering.md#chi-squared%20monothetic%20clustering)

## week 6 tutorial

- datetime: 2024-03-04T18:00:00+08:00/2024-03-04T19:00:00+08:00
- topic: how to do in-class exercise 2 (FP-tree) and additional exercise (FP-tree)
- [FP-growth algorithm § overview](../../../../general/FP-growth%20algorithm.md#overview)
- Jaccard's coefficient for binary data ::@:: [Jaccard index § similarity of asymmetric binary attributes](../../../../general/Jaccard%20index.md#similarity%20of%20asymmetric%20binary%20attributes) <!--SR:!2025-11-07,386,377!2026-03-02,501,397-->
- matching coefficient for binary data ::@:: [simple matching coefficient](../../../../general/simple%20matching%20coefficient.md) <!--SR:!2026-02-23,494,397!2026-03-09,508,397-->

## week 6 lecture 2

- datetime: 2024-03-06T09:00:00+08:00/2024-03-06T10:30:00+08:00
- [hierarchial clustering § agglomerative clustering](../../../../general/hierarchical%20clustering.md#agglomerative%20clustering)
- [hierarchial clustering § chi-squared monothetic clustering](../../../../general/hierarchical%20clustering.md#chi-squared%20monothetic%20clustering)
- [statistical classification § application domains](../../../../general/statistical%20classification.md#application%20domains)
  - similarities and differences between classification and clustering ::@:: They are both data analysis. The difference is that classification has a target attribute or variable while clustering does not. <!--SR:!2025-05-18,317,371!2026-03-25,509,327-->
- [statistical classification § algorithms](../../../../general/statistical%20classification.md#application%20algorithms)
  - statistical classification algorithms ::@:: We only teach decision tree, bayesian classifier, and nearest neighbor classifier. <!--SR:!2025-04-12,281,351!2027-02-12,804,351-->
- [entropy](../../../../general/entropy%20(information%20theory).md)
  - entropy base ::@:: We use base 2. <!--SR:!2025-03-13,245,347!2025-08-07,381,367-->

## week 7 lecture 1

- datetime: 2024-03-11T09:00:00+08:00/2024-03-11T10:30:00+08:00
- [entropy](../../../../general/entropy%20(information%20theory).md)
- decision tree format ::@:: All nodes show the percentage of actual labels in that decision nodes. The internal nodes show the attribute being split on. The terminal nodes show the predicted label. Arrows point from top to bottom, and each is labelled with an inequality operating on the attribute, which decides whether an sample being predicted should go through said arrow. <!--SR:!2026-06-09,556,357!2025-09-25,322,317-->
- [decision tree learning § algorithms](../../../../general/decision%20tree%20learning.md#algorithms)
  - decision tree learning algorithms ::@:: We only teach ID3 algorithm, C4.5 algorithm, and CART. <!--SR:!2025-07-22,366,371!2025-01-27,225,347-->
- [ID3 § algorithm](../../../../general/ID3%20algorithm.md#algorithm)
- [information gain § general definition](../../../../general/information%20gain%20(decision%20tree).md#general%20definition)
- [conditional entropy § definition](../../../../general/conditional%20entropy.md#definition)
- [ID3 § properties](../../../../general/ID3%20algorithm.md#properties)
- [C4.5 § algorithm](../../../../general/C4.5%20algorithm.md#algorithm)
  - split information of an attribute ::@:: It can be the entropy of the attribute in the entire set or the set of the decision node. The former is preferred. <!--SR:!2026-04-21,530,340!2025-06-08,322,360-->
- [information gain ratio § definition](../../../../general/information%20gain%20ratio.md#definition)
- [classification and regression tree § algorithm](../../../../general/classification%20and%20regression%20tree.md#algorithm)
- [decision tree learning § Gini impurity](../../../../general/decision%20tree%20learning.md#Gini%20impurity)

## week 7 tutorial

- datetime: 2024-03-11T18:00:00+08:00/2024-03-11T19:00:00+08:00
- topic: using XLMiner for _k_-means and hierarchical clustering
- [_k_-means clustering § standard algorithm (naive _k_-means)](../../../../general/k-means%20clustering.md#standard%20algorithm%20(naive%20_k_-means))
- [hierarchial clustering](../../../../general/hierarchical%20clustering.md)
- [hierarchial clustering § cluster linkage](../../../../general/hierarchical%20clustering.md#cluster%20linkage)
- [hierarchial clustering § agglomerative clustering](../../../../general/hierarchical%20clustering.md#agglomerative%20clustering)
- [hierarchial clustering § divisive clustering](../../../../general/hierarchical%20clustering.md#divisibe%20clustering)
- [Analytics Solver usage § usage](../../../Analytic%20Solver%20usage.md#usage)

## week 7 lecture 2

- datetime: 2024-03-13T09:00:00+08:00/2024-03-13T10:30:00+08:00
- [confusion matrix](../../../../general/confusion%20matrix.md)
  - confusion matrix format ::@:: Each row represents an actual class while each column represents a predicted class. <!--SR:!2026-02-05,464,320!2025-02-10,211,340-->
- [confusion matrix § error report](../../../../general/confusion%20matrix.md#error%20report)
- [lift chart](../../../lift%20chart.md)
- [lift chart § construction](../../../lift%20chart.md#construction)
- [lift chart § interpretation](../../../lift%20chart.md#interpretation)
- [lift chart § decile-wise](../../../lift%20chart.md#decile-wise)
- other classification performance measures ::@:: We will teach F1-score, precision, recall, specificity, and more later. <!--SR:!2025-11-24,447,331!2025-01-16,216,347-->
- [Analytics Solver usage § decision tree](../../../Analytic%20Solver%20usage.md#decision%20tree)

## week 8 lecture 1

- datetime: 2024-03-18T09:00:00+08:00/2024-03-18T10:30:00+08:00
- [Analytics Solver usage § decision tree](../../../Analytic%20Solver%20usage.md#decision%20tree)
- midterm exam format voting
  - bonus question (+10%, max 100%): no
  - cheatsheet: 1 sheet of A4-sized paper, double-sided
  - difficulty: 80% straight forward, 20% not straight forward but easy
  - duration: 70 minutes
  - datetime: 2024-03-25T09:05:00+08:00/2024-03-25T10:15:00+08:00
  - types: 80% long questions, 20% multiple choice questions
- [Bayes' theorem](../../../../general/Bayes'%20theorem.md)
  - [§ statement of theorem](../../../../general/Bayes'%20theorem.md#statement%20of%20theorem)
  - [§ Bayes' theorem for 3 events](../../../../general/Bayes'%20theorem.md#Bayes'%20theorem%20for%203%20events)
- [naive Bayes classifier](../../../../general/naive%20Bayes%20classifier.md)
  - [§ probabilistic model](../../../../general/naive%20Bayes%20classifier.md#probabilistic%20model)
  - [§ constructing a classifier from the probability model](../../../../general/naive%20Bayes%20classifier.md#constructing%20a%20classifier%20from%20the%20probability%20model)
- [conditional probability § Kolmogorov definition](../../../../general/conditional%20probability.md#Kolmogorov%20definition)
- homework 1
  - deadline: 2024-03-20T09:00:00+08:00

## week 8 tutorial

- datetime: 2024-03-18T18:00:00+08:00/2024-03-18T19:00:00+08:00
- topic: fundamental matrix operations
- [matrix](../../../../general/matrix%20(mathematics).md)
  - [§ addition, scalar multiplication, subtraction and transposition](../../../../general/matrix%20(mathematics).md#addition,%20scalar%20multiplication,%20subtraction%20and%20transposition)
  - [§ matrix multiplication](../../../../general/matrix%20(mathematics).md#matrix%20multiplication)
  - [§ linear equations](../../../../general/matrix%20(mathematics).md#linear%20equations)
- [determinant](../../../../general/determinant.md)
  - [§ two by two matrices](../../../../general/determinant.md#two%20by%20two%20matrices)
  - [§ 3 × 3 matrices](../../../../general/determinant.md#3%20×%203%20matrices)

## week 8 lecture 2

- datetime: 2024-03-20T09:00:00+08:00/2024-03-20T10:30:00+08:00
- [matrix](../../../../general/matrix%20(mathematics).md)
  - [§ addition, scalar multiplication, subtraction and transposition](../../../../general/matrix%20(mathematics).md#addition,%20scalar%20multiplication,%20subtraction%20and%20transposition)
  - [§ matrix multiplication](../../../../general/matrix%20(mathematics).md#matrix%20multiplication)
  - [§ linear equations](../../../../general/matrix%20(mathematics).md#linear%20equations)
- [determinant](../../../../general/determinant.md)
  - [§ two by two matrices](../../../../general/determinant.md#two%20by%20two%20matrices)
  - [§ 3 × 3 matrices](../../../../general/determinant.md#3%20×%203%20matrices)
- [naive Bayes classifier § probabilistic model](../../../../general/naive%20Bayes%20classifier.md#probabilistic%20model)
- [_k_-nearest neighbors algorithm § algorithm](../../../../general/k-nearest%20neighbors%20algorithm.md#algorithm)
- project phase 2
  - content
    - data: original data, steps to transform data, transformed data
    - models: 5 models
      - model: data used, model parameters, model type
  - deadline: 2024-04-17T09:00:00+08:00
- project phase 3
  - content
    - project phase 2: copy and paste
    - results
      - results for each model in layman's language
        - at least 2 raw outputs
        - (for decision tree models) give and draw the tree
        - observations
        - 2 records from the test dataset to illustrate the prediction process
        - conclusion
      - summary of 5 model results
        - choose the best model, or choose multiple models based on the situation
        - conclusion
  - deadline: 2024-04-29T09:00:00+08:00

## week 9 lecture 1

- datetime: 2024-03-25T09:00:00+08:00/2024-03-25T10:30:00+08:00
- midterm exam
  - bonus question (+10%, max 100%): no
  - cheatsheet: 1 sheet of A4-sized paper, double-sided
  - difficulty: 80% straight forward, 20% not straight forward but easy
  - duration: 70 minutes
  - datetime: 2024-03-25T09:05:00+08:00/2024-03-25T10:15:00+08:00
  - types: 80% long questions, 20% multiple choice questions

## week 9 tutorial

- datetime: 2024-03-25T18:00:00+08:00/2024-03-25T19:00:00+08:00
- topic: reducing the number of categories; using XLMiner for classification (decision tree)
- [Analytics Solver usage § category reduction](../../../Analytic%20Solver%20usage.md#category%20reduction)
- [decision tree learning § algorithms](../../../../general/decision%20tree%20learning.md#algorithms)
- [Analytics Solver usage](../../../Analytic%20Solver%20usage.md)
  - [§ decision tree](../../../Analytic%20Solver%20usage.md#decision%20tree)
  - [§ partitioning](../../../Analytic%20Solver%20usage.md#partitioning)
  - [§ common parameters](../../../Analytic%20Solver%20usage.md#common%20parameters)
  - [§ rescaling](../../../Analytic%20Solver%20usage.md#rescaling)

## week 9 lecture 2

- datetime: 2024-03-27T09:00:00+08:00/2024-03-27T10:30:00+08:00
- optional
- midterm exam checking: _/100
  - mean: 70.14 (provided)
  - standard deviation: 16.57 (provided)
  - low: 16.5 (provided)
  - high: 100 (provided)

## week 10 lecture 1

- datetime: 2024-04-01T09:00:00+08:00/2024-04-01T10:30:00+08:00
- status: midterm break, public holiday: Easter Monday

## week 10 tutorial

- datetime: 2024-04-01T18:00:00+08:00/2024-04-01T19:00:00+08:00
- status: midterm break, public holiday: Easter Monday

## week 10 lecture 2

- datetime: 2024-04-03T09:00:00+08:00/2024-04-03T10:30:00+08:00
- status: midterm break

## week 11 lecture 1

- datetime: 2024-04-08T09:00:00+08:00/2024-04-08T10:30:00+08:00
- final exam format voting
  - bonus question (+10%, max 100%): no
  - cheatsheet: 1 sheet of A4-sized paper, double-sided
  - difficulty: 80% straight forward, 20% not straight forward but easy
  - duration: 150 minutes
  - datetime: 2024-05-18T16:30:00+08:00/2024-05-18T19:00:00+08:00
  - types: 100% short or long questions, 0% multiple choice questions
- [neural network](../../../../general/neural%20network%20(machine%20learning).md)
  - [§ artificial neurons](../../../../general/neural%20network%20(machine%20learning).md#artificial%20neurons)
- [artificial neuron](../../../../general/artificial%20neuron.md)
  - [§ basic structure](../../../../general/artificial%20neuron.md#basic%20structure)
  - [§ types of activation functions](../../../../general/artificial%20neuron.md#types%20of%20activation%20function)
  - [§ step function](../../../../general/artificial%20neuron.md#step%20function)
    - step function threshold ::@:: _θ_ = 0 <!--SR:!2026-03-28,526,397!2026-05-10,562,397-->
  - [§ rectifier](../../../../general/artificial%20neuron.md#rectifier)
  - [§ sigmoid](../../../../general/artificial%20neuron.md#sigmoid)
    - sigmoid function variants ::@:: [logistic function](../../../../general/logistic%20function.md) with _L_ = 1, _k = 1_, and _x_<sub>0</sub> = 0: $$y = \frac L {1 + e^{-k(u - x_0)} } = \frac 1 {1 + e^{-u} }$$ <p> [hyperbolic tangent](../../../../general/hyperbolic%20functions.md) ($\tanh$): $$y = \frac {\sinh u} {\cosh u} = \frac {e^u - e^{-u} } {e^u + e^{-u} } = \frac {e^{2u} - 1} {e^{2u} + 1}$$ <!--SR:!2026-01-25,418,337!2025-03-21,204,357-->
- [perceptron](../../../../general/perceptron.md)
  - [§ steps](../../../../general/perceptron.md#steps)
    - perceptron stopping conditions ::@:: We can limit the maximum number of epochs, i.e. number of passes over the entire training dataset. We can also prematurely stop the training when the percentage error reaches below a threshold. <!--SR:!2025-04-08,220,357!2025-05-24,273,377-->
    - perceptron error trends ::@:: Generally, the error decreases, increasingly slowly. Eventually, the error stops decreasing. <!--SR:!2026-03-23,522,397!2026-01-24,473,397-->
  - [§ convergence of one perceptron on a linearly separable dataset](../../../../general/perceptron.md#convergence%20of%20one%20perceptron%20on%20a%20linearly%20separable%20dataset)
- [multilayer perceptron](../../../../general/multilayer%20perceptron.md)
- [Analytics Solver usage](../../../Analytic%20Solver%20usage.md): neural network

## week 11 tutorial

- datetime: 2024-04-08T18:00:00+08:00/2024-04-08T19:00:00+08:00
- topic: using XLMiner for classification (naive Bayes classifier, nearest neighbor classifier)
- [Analytics Solver usage](../../../Analytic%20Solver%20usage.md): naive Bayes classifier, nearest neighbor classifier

## week 11 lecture 2

- datetime: 2024-04-10T09:00:00+08:00/2024-04-10T10:30:00+08:00
- [recurrent neural network](../../../../general/recurrent%20neural%20network.md)
  - basic RNN ::@:: [§ Elman networks and Jordan networks](../../../../general/recurrent%20neural%20network.md#Elman%20networks%20and%20Jordan%20networks) <!--SR:!2025-01-18,154,337!2025-11-07,386,377-->
  - [§ long short-term memory](../../../../general/recurrent%20neural%20network.md#long%20short-term%20memory)
  - [§ gated recurrent unit](../../../../general/recurrent%20neural%20network.md#gated%20recurrent%20unit)
- [convolutional neural network](../../../../general/convolutional%20neural%20network.md)
  - convolutional neural network application ::@:: image similarity search <!--SR:!2026-10-28,667,357!2026-04-05,533,397-->
- [support vector machine](../../../../general/support%20vector%20machine.md)
  - [§ linear SVM](../../../../general/support%20vector%20machine.md#linear%20SVM)
  - [§ hard-margin](../../../../general/support%20vector%20machine.md#hard-margin)

## week 12 lecture 1

- datetime: 2024-04-15T09:00:00+08:00/2024-04-15T10:30:00+08:00
- [support vector machine](../../../../general/support%20vector%20machine.md)
  - [§ hard-margin](../../../../general/support%20vector%20machine.md#hard-margin)
  - [§ nonlinear kernels](../../../../general/support%20vector%20machine.md#nonlinear%20kernels)
- accuracy ::@:: [accuracy and precision § in binary classification](../../../../general/accuracy%20and%20precision.md#in%20binary%20classification) <!--SR:!2025-05-23,249,357!2025-06-11,260,357-->
- [precision and recall](../../../../general/precision%20and%20recall.md), [sensitivity and specificity § sensitivity](../../../../general/sensitivity%20and%20specificity.md#sensitivity)
- F-measure ::@:: [F-score § definition](../../../../general/F-score.md#definition) <!--SR:!2025-10-20,368,377!2025-07-19,313,377-->
- [sensitivity and specificity § specificity](../../../../general/sensitivity%20and%20specificity.md#specificity)
- [false positives and false negatives](../../../../general/false%20positives%20and%20false%20negatives.md)
- [training, validation, and test data sets](../../../../general/training,%20validation,%20and%20test%20data%20sets.md)
  - new data set ::@:: The data set to be predicted that does not have the actual values of the predicted attributes to compare against. Essentially, the model is being put into practical use. <!--SR:!2025-08-07,332,377!2025-07-20,318,377-->

## week 12 lab

- datetime: 2024-04-15T18:00:00+08:00/2024-04-15T19:00:00+08:00
- topic: using XLMiner for classification (neural network)
- [Analytics Solver usage](../../../Analytic%20Solver%20usage.md): neural network

## week 12 lecture 2

- datetime: 2024-04-17T09:00:00+08:00/2024-04-17T10:30:00+08:00
- [principal component analysis](../../../../general/principal%20component%20analysis.md)
  - [§ overview](../../../../general/principal%20component%20analysis.md#overview)
  - [§ intuition](../../../../general/principal%20component%20analysis.md#intuition)
  - [§ computing PCA using the covariance method](../../../../general/principal%20component%20analysis.md#computing%20PCA%20using%20the%20covariance%20method)
    - § computing PCA using the covariance method > matrix __X__ ::@:: The matrix __X__ taught in lesson uses the symbol __Y__, and is transposed: $\mathbf{Y} = \mathbf{X}^\intercal$. <!--SR:!2025-12-03,405,377!2026-03-23,522,397-->
    - § computing PCA using the covariance method > covariance matrix __C__ ::@:: The matrix __C__ taught in lesson uses the symbol __Σ__, and divides by _n_ instead of $n - 1$. <!--SR:!2025-11-02,380,377!2025-07-30,322,377-->
    - § computing PCA using the covariance method > eigenvalues and eigenvectors ::@:: The [classical method](../../../../general/eigenvalues%20and%20eigenvectors.md#classical%20method) is used to calculate. The eigenvalues _λ_ are found using $\det(\mathbf{\Sigma} - \lambda \mathbf{I})$ instead of $\det(\lambda \mathbf{I} - \mathbf{\Sigma})$. The eigenvectors are normalized. <!--SR:!2025-07-14,313,377!2025-04-15,236,357-->
      - [eigenvalues and eigenvectors § classical method](../../../../general/eigenvalues%20and%20eigenvectors.md#classical%20method)
        - eigenvalues and eigenvectors § classical method > eigenvector ::@:: The eigenvector is calculated from the eigenvalue using $(\mathbf{\Sigma} - \lambda \mathbf{I}) \mathbf{x} = \mathbf{0}$ instead of $\mathbf{\Sigma} \mathbf{x} = \lambda \mathbf{x}$. <!--SR:!2026-03-28,526,397!2025-08-18,342,377-->
    - § computing PCA using the covariance method > eigenvector matrix ::@:: The eigenvector matrix uses the symbol __Φ__. Instead of selecting a subset of the eigenvectors as the basis vectors first, the whole matrix is kept, and then the redundant coordinates are only discarded after transforming the original data. <!--SR:!2025-09-13,340,377!2025-03-22,205,357-->
    - § computing PCA using the covariance method > cumulative variance ::@:: Cumulative variance is ignored. So the step about computing the cumulative variance is ignored. Instead, the number of dimensions to be reduced to is specified beforehand instead of being chosen using the ignored step. <!--SR:!2025-04-04,217,357!2026-04-29,482,337-->
    - § computing PCA using the covariance method > data transformation ::@:: Also, instead of transforming the mean-subtracted data using $\mathbf{T} = \mathbf{B} \mathbf{\Phi}$, the original data $\mathbf{Y} = \mathbf{X}^\intercal$ is transformed, and in a different way: $\mathbf{T}' = \mathbf{\Phi}^\intercal \mathbf{Y}$. Each column instead of each row of $\mathbf{T}'$ is a data point. Even more specifically, the data points are transformed one by one: $\mathbf{T}'_i = \mathbf{\Phi}^\intercal \mathbf{Y}_i$. <!--SR:!2025-02-19,181,337!2025-02-02,166,337-->
- [Analytics Solver usage](../../../Analytic%20Solver%20usage.md): principal components
- [data warehouse](../../../../general/data%20warehouse.md)
  - data warehouse > application ::@:: [online analytical processing](../../../../general/online%20analytical%20processing.md) (OLAP), used by many corporations <!--SR:!2026-02-23,494,388!2026-10-06,640,388-->
  - data warehouse > advantage ::@:: data warehouses can speed up queries on a database <!--SR:!2026-03-28,462,337!2025-08-05,327,377-->

## week 13 lecture 1

- datetime: 2024-04-22T09:00:00+08:00/2024-04-22T10:30:00+08:00
- [principal component analysis § computing PCA using the covariance method](../../../../general/principal%20component%20analysis.md#computing%20PCA%20using%20the%20covariance%20method)
- project phase 3: see above
- [fact table § examples](../../../../general/fact%20table.md) ::@:: see the transactional fact table example <!--SR:!2025-04-29,231,357!2025-12-17,418,377-->
- data cube ::@:: [OLAP cube](../../../../general/OLAP%20cube.md) <!--SR:!2026-03-28,526,397!2026-04-05,533,397-->
  - [§ operations](../../../../general/OLAP%20cube.md#operations)
    - data cube > operations ::@:: drill down, rollup <!--SR:!2025-09-14,357,377!2026-03-23,522,397-->

## week 13 tutorial

- datetime: 2024-04-22T18:00:00+08:00/2024-04-22T19:00:00+08:00
- optional
- topic: questions about XLMiner
- [Analytics Solver usage](../../../Analytic%20Solver%20usage.md)

## week 13 lecture 2

- datetime: 2024-04-24T09:00:00+08:00/2024-04-24T10:30:00+08:00
- [online analytical processing § aggregations](../../../../general/online%20analytical%20processing.md#aggregations)
- [materialized view](../../../../general/materialized%20view.md)
  - [§ algorithms](../../../../general/materialized%20view.md#algorithms)
  - [§ terminology](../../../../general/materialized%20view.md#terminology)
  - [§ greedy algorithm](../../../../general/materialized%20view.md#greedy%20algorithm)
- web database ranking considerations ::@:: When searching for something using a search engine, apart from matching terms, incoming and outgoing links are also considered. <!--SR:!2025-07-31,327,377!2026-03-28,526,397-->
- [HITS algorithm](../../../../general/HITS%20algorithm.md)
  - [§ steps](../../../../general/HITS%20algorithm.md#steps)
    - HITS algorithm variant ::@:: It does not matter because we only use the recursive expressions to calculate the new authority and hub values. <!--SR:!2025-11-07,386,377!2026-02-23,494,397-->
    - HITS algorithm termination ::@:: Terminate the HITS algorithm when after rounding the values to a certain number of digits, the values have not changed. <!--SR:!2025-12-14,416,388!2026-12-21,743,408-->
  - [§ in detail](../../../../general/HITS%20algorithm.md#in%20detail)
  - [§ authority update rule](../../../../general/HITS%20algorithm.md#authority%20update%20rule)
  - [§ hub update rule](../../../../general/HITS%20algorithm.md#hub%20update%20rule)
  - [§ normalization](../../../../general/HITS%20algorithm.md#normalization)
    - HITS algorithm normalization ::@:: Normalization is done after each iteration. We use the [taxicab norm](../../../../general/norm%20(mathematics).md#taxicab%20norm%20or%20Manhattan%20norm). The normalized vector length is the number of pages instead of 1. <!--SR:!2025-06-13,288,377!2025-10-20,368,377-->
- [PageRank](../../../../general/PageRank.md)
  - [§ algorithm](../../../../general/PageRank.md#algorithm)
    - PageRank self-links ::@:: Self-links are considered. <!--SR:!2026-10-13,690,408!2026-07-28,627,408-->
    - PageRank initialization ::@:: We initialize all PageRank values to 1 instead of 1 divided by number of pages. <!--SR:!2025-12-17,418,377!2025-06-16,290,377-->
    - PageRank termination ::@:: Terminate the PageRank algorithm when after rounding the values to a certain number of digits, the values have not changed. <!--SR:!2026-03-10,509,408!2026-07-01,612,408-->
  - [§ simplified algorithm](../../../../general/PageRank.md#simplified%20algorithm)
  - [§ damping factor](../../../../general/PageRank.md#damping%20factor)
    - PageRank damping factor variation ::@:: We use the "wrong" algorithm in the original paper, where the PageRank is added $1 - d$ instead of $\frac {1 - d} N$. <!--SR:!2026-03-02,501,397!2025-05-19,269,377-->

## week 14 lecture

- datetime: 2024-04-29T09:00:00+08:00/2024-04-29T10:30:00+08:00
- [PageRank § simplified algorithm](../../../../general/PageRank.md#simplified%20algorithm)
- [materialized view § greedy algorithm](../../../../general/materialized%20view.md#greedy%20algorithm)
- [Bayes' theorem](../../../../general/Bayes'%20theorem.md)
  - [§ statement of theorem](../../../../general/Bayes'%20theorem.md#statement%20of%20theorem)
  - [§ Bayes' theorem for 3 events](../../../../general/Bayes'%20theorem.md#Bayes'%20theorem%20for%203%20events)
- [conditional probability § Kolmogorov definition](../../../../general/conditional%20probability.md#Kolmogorov%20definition)
- Bayesian belief network ::@:: [Bayesian network](../../../../general/Bayesian%20network.md) <!--SR:!2027-01-03,754,408!2026-06-15,597,408-->
  - [§ graphical model](../../../../general/Bayesian%20network.md#graphical%20model)
- [conditional dependence](../../../../general/conditional%20dependence.md)
- [conditional independence](../../../../general/conditional%20independence.md)
  - [§ conditional independence of events](../../../../general/conditional%20independence.md#conditional%20independence%20of%20events)
  - [§ proof of the equivalent definition](../../../../general/conditional%20independence.md#proof%20of%20the%20equivalent%20definition)
- [conditional probability table](../../../../general/conditional%20probability%20table.md)
  - conditional probability table format ::@:: The row headers are the input variables. The column headers are the output variables. (mnemonic: ↗) <!--SR:!2025-08-07,210,289!2025-03-08,191,349-->
- [chain rule (probability)](../../../../general/chain%20rule%20(probability).md)
  - [§ two events](../../../../general/chain%20rule%20(probability).md#two%20events)
  - [§ finitely many events](../../../../general/chain%20rule%20(probability).md#finitely%20many%20events)

## week 14 tutorial

- datetime: 2024-04-29T18:00:00+08:00/2024-04-29T19:00:00+08:00
- topic: using XLMiner for PCA
- [Analytics Solver usage](../../../Analytic%20Solver%20usage.md): principal components

## week 15 lecture 1

- datetime: 2024-05-06T09:00:00+08:00/2024-05-06T10:30:00+08:00
- [Bayes' theorem](../../../../general/Bayes'%20theorem.md)
  - [§ statement of theorem](../../../../general/Bayes'%20theorem.md#statement%20of%20theorem)
  - [§ Bayes' theorem for 3 events](../../../../general/Bayes'%20theorem.md#Bayes'%20theorem%20for%203%20events)
- [Bayesian belief network](../../../../general/Bayesian%20network.md)
  - [§ graphical model](../../../../general/Bayesian%20network.md#graphical%20model)
  - Bayesian belief network inference setup ::@:: Identify the node for which the conditional probability is calculated. Then identify all node parents and children, whether direct or indirect. Discard conditions that are conditionally independent of the calculated probability (search for "_d_-separation"). <!--SR:!2025-11-23,394,337!2025-05-28,254,357-->
  - Bayesian belief network inference process ::@:: Decompose joint probabilities into separate probabilities if they are conditionally independent of each other. Apply Bayes' theorem (for 3 events) to invert the conditional probability so that the resulting conditional probabilities follow the network arrows. Use the probability chain rule if necessary. Sum up over all possible values of a node (recursively) if necessary. Finally, substitute the known probabilities to calculate the results. <!--SR:!2026-03-09,492,357!2025-02-05,171,337-->
  - Bayesian belief network inference answering ::@:: Also calculate the complement of the conditional probability (which is _usually_ done by subtracting from 1). Compare the 2 conditional probabilities, and state that the higher conditional probability is the most likely outcome. <!--SR:!2026-03-23,522,397!2025-04-10,231,357-->
- [conditional dependence](../../../../general/conditional%20dependence.md)
- [conditional independence § conditional independence of events](../../../../general/conditional%20independence.md#conditional%20independence%20of%20events)
- [chain rule (probability)](../../../../general/chain%20rule%20(probability).md)
  - [§ two events](../../../../general/chain%20rule%20(probability).md#two%20events)
  - [§ finitely many events](../../../../general/chain%20rule%20(probability).md#finitely%20many%20events)
- common core requirements ::@:: mathematical models, quantitative data, quantitative methods <!--SR:!2025-05-30,258,357!2026-02-23,494,397-->
- other topics
  - association thresholding ::@:: Instead of thresholding by frequency, we can threshold by number of frequent item sets found, which may be easier to choose. <!--SR:!2025-06-03,278,377!2025-01-27,161,337-->
  - [clustering high-dimensional data § subspace clustering](../../../../general/clustering%20high-dimensional%20data.md#subspace%20clustering) ::@:: By removing some dimensions of the data, more interesting clusters may be found. It mitigates [curse of dimensionality](../../../../general/curse%20of%20dimensionality.md), where [distances between different pairs of points become similar](../../../../general/curse%20of%20dimensionality.md#distance%20function). <!--SR:!2026-03-10,455,337!2025-06-18,293,377-->
  - ensemble of classifiers ::@:: We can output the prediction based on the majority prediction of the classifiers. <!--SR:!2025-08-24,347,377!2025-05-28,256,357-->
  - data warehouse questions ::@:: How to create the data warehouse over different types of data, such as a graph? <!--SR:!2026-01-23,472,397!2025-10-17,386,377-->
  - [word-sense disambiguation](word-sense%20disambiguation.md) ::@:: How to disambiguate between different entities of the same name on the Internet? <!--SR:!2026-01-25,474,397!2026-01-22,471,397-->
  - social networks ::@:: How are people connected? <!--SR:!2026-03-10,509,397!2026-02-23,494,397-->
  - privacy issues ::@:: How to preserve data privacy while data mining? Minimize information loss while protect individual privacy. <!--SR:!2026-01-09,458,397!2025-09-09,336,377-->
  - graph data ::@:: How to analyze graphs? <!--SR:!2026-01-29,478,397!2026-02-09,487,397-->
  - decision making
  - data streams ::@:: How to data mine over real-time and possibly unbounded data streams? <!--SR:!2026-05-02,556,397!2025-06-27,298,377-->
  - chatbot
  - picture description
  - generative AI
    - [???](https://youtu.be/F0cAPC7rOkw), [???](https://youtu.be/B8O77NEDTnQ)
- next lecture: guest lecture by Prof. Dan Xu
- homework 2
  - deadline: 2024-05-08T09:00:00+08:00

## week 15 tutorial

- datetime: 2024-05-06T18:00:00+08:00/2024-05-06T19:00:00+08:00
- topic: how to do in-class exercise 5 (Bayesian classifier)
- [Bayes' theorem](../../../../general/Bayes'%20theorem.md)
  - [§ statement of theorem](../../../../general/Bayes'%20theorem.md#statement%20of%20theorem)
  - [§ Bayes' theorem for 3 events](../../../../general/Bayes'%20theorem.md#Bayes'%20theorem%20for%203%20events)
- [conditional probability § Kolmogorov definition](../../../../general/conditional%20probability.md#Kolmogorov%20definition)
- [Bayesian belief network](../../../../general/Bayesian%20network.md)
  - [§ graphical model](../../../../general/Bayesian%20network.md#graphical%20model)
- [conditional dependence](../../../../general/conditional%20dependence.md)
- [conditional independence § conditional independence of events](../../../../general/conditional%20independence.md#conditional%20independence%20of%20events)
- [conditional probability table](../../../../general/conditional%20probability%20table.md)
- [chain rule (probability)](../../../../general/chain%20rule%20(probability).md)
  - [§ two events](../../../../general/chain%20rule%20(probability).md#two%20events)
  - [§ finitely many events](../../../../general/chain%20rule%20(probability).md#finitely%20many%20events)

## week 15 lecture 2

- datetime: 2024-05-08T09:00:00+08:00/2024-05-08T10:30:00+08:00
- optional
- guest lecture
  - speaker: Prof. Dan Xu
  - topics
    - open world visual learning
    - cross-model language—image contrastive pretraining (CLIP)
    - CLIP model for recognition, detection, and segmentation via similarity and distillation

## assessments

- midterm examination
  - bonus question (+10%, max 100%): no
  - cheatsheet: 1 sheet of A4-sized paper, double-sided
  - difficulty: 80% straight forward, 20% not straight forward but easy
  - duration: 70 minutes
  - datetime: 2024-03-25T09:05:00+08:00/2024-03-25T10:15:00+08:00
  - types: 80% long questions, 20% multiple choice questions
  - report
    - Very very tight time limit. Do the paper as-if you do not have enough time.
      - handle midterm examination time limit ::@:: Do any midterm paper as if you do not have enough time. <!--SR:!2025-04-26,137,422!2025-04-23,134,422-->
- final examination
  - bonus question (+10%, max 100%): no
  - cheatsheet: 1 sheet of A4-sized paper, double-sided
  - difficulty: 80% straight forward, 20% not straight forward but easy
  - duration: 150 minutes
  - datetime: 2024-05-18T16:30:00+08:00/2024-05-18T19:00:00+08:00
  - types: 100% short or long questions, 0% multiple choice questions
  - report
    - Time is much more lenient.
      - handle final examination time limit ::@:: While not as important, it is still a good idea to do any final paper as if you do not have enough time. <!--SR:!2025-04-27,138,422!2025-04-25,136,422-->
