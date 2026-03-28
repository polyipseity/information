---
aliases:
  - COMP 4211
  - COMP 4211 index
  - COMP4211
  - COMP4211 index
  - HKUST COMP 4211
  - HKUST COMP 4211 index
  - HKUST COMP4211
  - HKUST COMP4211 index
  - Machine Learning
  - Machine Learning index
tags:
  - flashcard/active/special/academia/HKUST/COMP_4211/index
  - function/index
  - language/in/English
---

# index

- HKUST COMP 4211
- name: Machine Learning
- credits: 3

---

COMP 4211 is an undergraduate machine learning course at HKUST covering linear models, classification, bias-variance tradeoffs, neural networks, optimization, convolutional and recurrent networks, transformers, and selected generative and classical methods. The lectures emphasize conceptual frameworks, models, principles, and algorithms, while tutorials bridge theory and practice through demonstrations and hands-on coding.

Prerequisites: COMP 2211 and one of ELEC 2600, IEDA 2520, IEDA 2540, MATH 2411, MATH 2421, or MATH 2431. Exclusion: COMP 5212.

The published learning outcomes are to understand learning-from-data issues and the major types of machine learning tasks; explain the principles underlying a variety of machine learning algorithms; apply a variety of machine learning algorithms to data; and evaluate and compare different machine learning algorithms according to common performance criteria.

Materials are distributed through the course OneDrive folder and Canvas, with lecture recordings released on Canvas when available. This public note tracks the `L1` lecture and `T1` tutorial schedule; official contact information should be checked in the syllabus or Canvas rather than duplicated here. The note also records the workload rules that affect study planning, including the requirement to complete all 4 written assignments and exactly 6 hands-on assignments.

<!--
Source schedule snapshot saved for future agents (from the course information and inspected slide dump in `.tmp`).

Week 1: 2026-02-03 L00 course introduction and L01 linear regression. 2026-02-05 T01 Colab, Python, NumPy. 2026-02-05 L01 linear regression with polynomial regression, overfitting, validation, and regularization. Workload reminder: pick only 6 HAs and do all 4 WAs.

Week 2: 2026-02-10 L02.1 logistic regression with cross entropy, likelihood, and gradient descent; WA1 out. 2026-02-12 L02.1 logistic regression with softmax, performance metrics, and probabilistic formulation of linear regression; T02 PyTorch basics and linear regression; HA1 out.

Week 3: 2026-02-17 and 2026-02-19 Chinese New Year.

Week 4: 2026-02-24 L02.2 other approaches to classification. 2026-02-26 L03 bias-variance decomposition. 2026-02-26 T03 Pandas, sklearn, logistic regression.

Week 5: 2026-03-03 L04 feedforward neural networks; HA1 due. 2026-03-05 L04/L05 with TensorFlow Playground; T04 FNN in PyTorch; WA1 due; HA2 out; WA2 out.

Week 6: 2026-03-10 L05 fundamental issues in deep learning and optimization algorithms. 2026-03-12 L06 convolutional neural networks. 2026-03-12 T05 CNN in PyTorch and computation at the convolutional layer.

Week 7: 2026-03-17 L06 convolutional neural networks; HA2 due; HA3/HA4 out. 2026-03-19 L07 recurrent neural networks; T06 RNN in PyTorch and seq2seq; WA2 due.

Week 8: 2026-03-24 L07 recurrent neural networks with attention in RNN; HA3/HA4 due. 2026-03-26 class cancelled due to midterm. 2026-03-28 midterm 14:00-16:00, coverage L01-L05, venue Rooms 4619 and 4620.

Week 9: 2026-03-31 L08 transformer models with demo code and self-attention in PyTorch; HA5 out; WA3 (L6-L8) out. 2026-04-02 L08 transformer models; T07 BERT in PyTorch; mid-term break follows.

Week 10: 2026-04-14 HA5 due and HA6/HA7 out. 2026-04-16 WA3 due.

Week 11: 2026-04-21 HA6/HA7 due.

Weeks 12-13: 2026-04-28, 2026-04-30, 2026-05-05, and 2026-05-07 remain placeholders in the public notes.

Final examination: 2026-05-21 from 12:30 to 15:30 at Tsang Shiu Tim Art Hall, Atrium.

Assignment policy reminders.

Written assignments may use GenAI only with full disclosure of use and prompts.

AI-generated code is prohibited for hands-on assignments.

Turnitin similarity scores above 40 incur penalty of (max{score-40,0}/60) x 100% of the item grade.

Final submission should keep a timestamped screenshot of the similarity score and upload it in Canvas comments.

Late penalty is 5% per day for up to 5 days with no extension into the study break. -->

The content is in teaching order.

## logistics

- grading
  - scheme
    - written assignments ×4: 12%; all four are required
    - hands-on assignments ×6: 18%; choose any 6 from the published list
    - midterm examination: 25%
    - final examination: 45%
- sections:
  - lecture: L1
    - L1: G002, CYT Building; TuesdayT13:30:00+08:00/TuesdayT14:50:00+08:00, ThursdayT13:30:00+08:00/ThursdayT14:50:00+08:00
  - tutorials: T1
    - T1: Room 2306, Academic Building (near Lifts 17–18); ThursdayT18:00:00+08:00/ThursdayT18:50:00+08:00
- office hours: after class or by appointment.
- note: L1 and L2 share the same course materials, grading scheme, and Piazza space; this note currently records the L1 lecture and T1 tutorial timeline.
- note: If a student misses the midterm with strong reasons and prior notice, the midterm weight is carried over to the final. Absence from the final examination causes automatic course failure unless prior departmental approval is obtained.
- note: All assignments are due by 23:59 on the due date. Late work is accepted for up to 5 days with a 5% penalty per day, but extensions into the study break are not allowed.

## children

- [assignments](assignments/index.md)
- [attachments/](attachments/)
- [questions/](questions/index.md)
- [bias-variance decomposition](bias-variance%20decomposition.md)
- [classification](classification.md)
- [deep learning training](deep%20learning%20training.md)
- [feedforward neural network](feedforward%20neural%20network.md)
- [linear regression](linear%20regression.md)
- [logistic regression](logistic%20regression.md)

## assignments

- written assignment 1
  - out: 2026-02-10T00:00:00+08:00
  - due: 2026-03-05T23:59:00+08:00
- hands-on assignment 1
  - out: 2026-02-12T00:00:00+08:00
  - due: 2026-03-03T23:59:00+08:00
- hands-on assignment 2
  - out: 2026-03-05T00:00:00+08:00
  - due: 2026-03-17T23:59:00+08:00
- written assignment 2
  - out: 2026-03-05T00:00:00+08:00
  - due: 2026-03-19T23:59:00+08:00
- hands-on assignments 3 and 4
  - out: 2026-03-17T00:00:00+08:00
  - due: 2026-03-24T23:59:00+08:00
- hands-on assignment 5
  - out: 2026-03-31T00:00:00+08:00
  - due: 2026-04-14T23:59:00+08:00
- written assignment 3
  - out: 2026-03-31T00:00:00+08:00
  - due: 2026-04-16T23:59:00+08:00
- hands-on assignments 6 and 7
  - out: 2026-04-14T00:00:00+08:00
  - due: 2026-04-21T23:59:00+08:00
- hands-on assignment selection note
  - requirement: choose exactly 6 hands-on assignments; additional submissions are not graded
  - recommendation: if COMP 2211 is the only machine-learning background, prioritize HA1, HA2, HA3, HA5, HA7, and HA8

## references

- Ian Goodfellow, Yoshua Bengio, and Aaron Courville, _Deep Learning_, MIT Press, 2016; the official site presents it as a free online textbook covering machine learning and deep learning foundations, regularization, optimization, convolutional networks, recurrent networks, and generative models.
- Kevin P. Murphy, _Probabilistic Machine Learning: An Introduction_, MIT Press, 2022; the companion site describes it as a rigorous introduction connecting classical machine learning and deep learning through probabilistic reasoning.
- Aston Zhang, Zachary C. Lipton, Mu Li, and Alexander J. Smola, _Dive into Deep Learning_, Cambridge University Press, 2023; the interactive site provides executable notebooks spanning linear regression, softmax regression, MLPs, CNNs, RNNs, transformers, BERT, optimization, computer vision, and GANs.
- Ethem Alpaydin, _Introduction to Machine Learning_, 4th edition, MIT Press, 2020.
- Kaare Brandt Petersen and Michael Syskind Pedersen, _The Matrix Cookbook_, Technical University of Denmark, version 2012-11-15; a desktop reference of matrix identities, relations, inverses, and derivatives.
- Marc Peter Deisenroth, A. Aldo Faisal, and Cheng Soon Ong, _Mathematics for Machine Learning_, Cambridge University Press, 2020; the companion site focuses on linear algebra, calculus, probability, optimization, linear regression, PCA, GMMs, and SVMs.

## week 1 lecture 1

- datetime: 2026-02-03T13:30:00+08:00/2026-02-03T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: course introduction; linear regression
- [linear regression](linear%20regression.md)
  - linear regression / [§ supervised regression setup and ordinary least squares](linear%20regression.md#supervised%20regression%20setup%20and%20ordinary%20least%20squares)
  - linear regression / [§ other linear-regression fitting methods](linear%20regression.md#other%20linear-regression%20fitting%20methods)
  - linear regression / [§ one-feature least-squares fit](linear%20regression.md#one-feature%20least-squares%20fit)
  - linear regression / [§ solving the toy problem by differentiation](linear%20regression.md#solving-the-toy-problem-by-differentiation)
  - linear regression / [§ gradient, matrix form, and the normal equation](linear%20regression.md#gradient-matrix-form-and-the-normal-equation)
  - linear regression / [§ derivation of the matrix gradient](linear%20regression.md#derivation-of-the-matrix-gradient)
  - linear regression / [§ tiny normal-equation computation](linear%20regression.md#tiny-normal-equation-computation)
  - linear regression / [§ normal equation as projection and the noninvertible case](linear%20regression.md#normal-equation-as-projection-and-the-noninvertible-case)

## week 1 lecture 2

- datetime: 2026-02-05T13:30:00+08:00/2026-02-05T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: linear regression; polynomial regression; overfitting; validation; regularization
- [linear regression](linear%20regression.md)
  - linear regression / [§ polynomial features and model capacity](linear%20regression.md#polynomial%20features%20and%20model%20capacity)
  - linear regression / [§ worked polynomial-feature constructions](linear%20regression.md#worked-polynomial-feature-constructions)
  - linear regression / [§ hypothesis space, capacity, and generalization](linear%20regression.md#hypothesis%20space-capacity-and-generalization)
  - linear regression / [§ small hypothesis spaces in practice](linear%20regression.md#small%20hypothesis%20spaces%20in%20practice)
  - linear regression / [§ iid train-test assumption and implications](linear%20regression.md#iid%20train-test%20assumption%20and%20implications)
  - linear regression / [§ underfitting and overfitting](linear%20regression.md#underfitting-and-overfitting)
  - linear regression / [§ training error, test error, and the capacity curve](linear%20regression.md#training-error-test-error-and-the-capacity-curve)
  - linear regression / [§ capacity comparison: degree 14 versus degree 20](linear%20regression.md#capacity-comparison-degree-14-versus-degree-20)
  - linear regression / [§ validation, cross-validation, and hyperparameter tuning](linear%20regression.md#validation-cross-validation-and-hyperparameter-tuning)
  - linear regression / [§ hold-out and cross-validation weaknesses](linear%20regression.md#hold-out%20and%20cross-validation%20weaknesses)
  - linear regression / [§ regularization and sparse models](linear%20regression.md#regularization-and-sparse-models)
  - linear regression / [§ interpreting l2 squared and l1 penalties](linear%20regression.md#interpreting%20l2%20squared%20and%20l1%20penalties)
  - linear regression / [§ ridge versus LASSO contour intuition](linear%20regression.md#ridge%20versus%20LASSO%20contour%20intuition)
  - linear regression / [§ regularization behavior across $\lambda$](linear%20regression.md#regularization-behavior-across-lambda)

## week 1 tutorial

- datetime: 2026-02-05T18:00:00+08:00/2026-02-05T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- topic: Colab; Python; NumPy

## week 2 lecture 1

- datetime: 2026-02-10T13:30:00+08:00/2026-02-10T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: logistic regression; cross entropy; likelihood; gradient descent
- [logistic regression](logistic%20regression.md)
  - logistic regression / [§ binary logistic model and decision boundary](logistic%20regression.md#binary%20logistic%20model%20and%20decision%20boundary)
  - logistic regression / [§ Bernoulli output model, odds, and logit](logistic%20regression.md#Bernoulli%20output%20model-odds-and-logit)
  - logistic regression / [§ Bayes decision rule and thresholding](logistic%20regression.md#Bayes%20decision%20rule-and-thresholding)
  - logistic regression / [§ entropy, cross entropy, and maximum likelihood](logistic%20regression.md#entropy-cross%20entropy-and-maximum%20likelihood)
  - logistic regression / [§ entropy and uncertainty](logistic%20regression.md#entropy-and-uncertainty)
  - logistic regression / [§ cross entropy and Kullback-Leibler divergence](logistic%20regression.md#cross-entropy-and-kullback-leibler-divergence)
  - logistic regression / [§ likelihood and maximum likelihood](logistic%20regression.md#likelihood-and-maximum-likelihood)
  - logistic regression / [§ cross entropy for logistic regression](logistic%20regression.md#cross%20entropy%20for%20logistic%20regression)
  - logistic regression / [§ population risk versus empirical loss](logistic%20regression.md#population-risk-versus-empirical-loss)
  - logistic regression / [§ gradient descent basics](logistic%20regression.md#gradient-descent-basics)

## week 2 lecture 2

- datetime: 2026-02-12T13:30:00+08:00/2026-02-12T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: logistic regression; softmax; performance metrics; probabilistic formulation of linear regression
- [linear regression](linear%20regression.md)
  - linear regression / [§ performance metrics for regression](linear%20regression.md#performance%20metrics%20for%20regression)
  - linear regression / [§ mse and rmse interpretation](linear%20regression.md#mse%20and%20rmse%20interpretation)
  - linear regression / [§ r squared intuition and alternative formulas](linear%20regression.md#r%20squared%20intuition%20and%20alternative%20formulas)
  - linear regression / [§ probabilistic formulation of linear regression](linear%20regression.md#probabilistic%20formulation%20of%20linear%20regression)
  - linear regression / [§ likelihood objective and maximum likelihood](linear%20regression.md#likelihood%20objective%20and%20maximum%20likelihood)
  - linear regression / [§ from Gaussian likelihood to least squares](linear%20regression.md#from%20Gaussian%20likelihood%20to%20least%20squares)
  - linear regression / [§ deriving least squares from the Gaussian density](linear%20regression.md#deriving-least-squares-from-the-gaussian-density)
  - linear regression / [§ likelihood derivation and cross entropy](linear%20regression.md#likelihood%20derivation%20and%20cross%20entropy)
- [logistic regression](logistic%20regression.md)
  - logistic regression / [§ gradient descent for logistic regression](logistic%20regression.md#gradient-descent-for-logistic-regression)
  - logistic regression / [§ batch and stochastic gradient descent](logistic%20regression.md#batch-and-stochastic-gradient-descent)
  - logistic regression / [§ l2 regularization in logistic regression](logistic%20regression.md#l2-regularization-in-logistic-regression)
  - logistic regression / [§ softmax regression](logistic%20regression.md#softmax-regression)
  - logistic regression / [§ softmax cross entropy and gradient](logistic%20regression.md#softmax-cross-entropy-and-gradient)
- [classification](classification.md)
  - classification / [§ performance metrics for classification](classification.md#performance-metrics-for-classification)
  - classification / [§ confusion matrix and accuracy](classification.md#confusion-matrix-and-accuracy)
  - classification / [§ precision, recall, and F1: intuition and mnemonics](classification.md#precision-recall-and-f1-intuition-and-mnemonics)
  - classification / [§ multiclass precision, recall, and F1](classification.md#multiclass-precision-recall-and-f1)
  - classification / [§ worked metric computations](classification.md#worked-metric-computations)

## week 2 tutorial

- datetime: 2026-02-12T18:00:00+08:00/2026-02-12T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- topic: PyTorch basics; linear regression
- [linear regression](linear%20regression.md)
  - linear regression / [§ supervised regression setup and ordinary least squares](linear%20regression.md#supervised%20regression%20setup%20and%20ordinary%20least%20squares)
  - linear regression / [§ other linear-regression fitting methods](linear%20regression.md#other%20linear-regression%20fitting%20methods)
  - linear regression / [§ solving the toy problem by differentiation](linear%20regression.md#solving-the-toy-problem-by-differentiation)
  - linear regression / [§ gradient, matrix form, and the normal equation](linear%20regression.md#gradient-matrix-form-and-the-normal-equation)
  - linear regression / [§ tiny normal-equation computation](linear%20regression.md#tiny-normal-equation-computation)
  - linear regression / [§ normal equation as projection and the noninvertible case](linear%20regression.md#normal-equation-as-projection-and-the-noninvertible-case)
  - linear regression / [§ performance metrics for regression](linear%20regression.md#performance%20metrics%20for%20regression)

## week 3 lecture 1

- datetime: 2026-02-17T13:30:00+08:00/2026-02-17T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- status: public holiday: Chinese New Year

## week 3 lecture 2

- datetime: 2026-02-19T13:30:00+08:00/2026-02-19T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- status: public holiday: Chinese New Year

## week 3 tutorial

- datetime: 2026-02-19T18:00:00+08:00/2026-02-19T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- status: public holiday: Chinese New Year

## week 4 lecture 1

- datetime: 2026-02-24T13:30:00+08:00/2026-02-24T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: other approaches to classification
- [classification](classification.md)
  - classification / [§ probabilistic approach to classification](classification.md#probabilistic%20approach%20to%20classification)
  - classification / [§ worked posterior-decision calculations](classification.md#worked-posterior-decision-calculations)
  - classification / [§ zero-one loss and empirical risk minimization](classification.md#zero-one%20loss%20and%20empirical%20risk%20minimization)
  - classification / [§ sign function and margin formulation](classification.md#sign-function-and-margin-formulation)
  - classification / [§ why zero-one loss resists gradient descent](classification.md#why-zero-one-loss-resists-gradient-descent)
  - classification / [§ surrogate losses](classification.md#surrogate%20losses)
  - classification / [§ convex upper bounds and margin shaping](classification.md#convex-upper-bounds-and-margin-shaping)
  - classification / [§ common surrogate losses](classification.md#common-surrogate-losses)
  - classification / [§ loss versus error](classification.md#loss-versus-error)
  - classification / [§ discriminative versus generative classification](classification.md#discriminative%20versus%20generative%20classification)
  - classification / [§ Bayes-rule classification from a generative model](classification.md#Bayes-rule%20classification%20from%20a%20generative%20model)
  - classification / [§ posterior log-score decomposition](classification.md#posterior%20log-score%20decomposition)
  - classification / [§ naive Bayes and conditional independence](classification.md#naive%20Bayes%20and%20conditional%20independence)
  - classification / [§ parameter explosion without conditional independence](classification.md#parameter%20explosion%20without%20conditional%20independence)
  - classification / [§ naive Bayes factorization and prediction](classification.md#naive%20bayes%20factorization%20and%20prediction)
  - classification / [§ parameter estimation for discrete naive Bayes](classification.md#parameter%20estimation%20for%20discrete%20naive%20bayes)
  - classification / [§ Laplace smoothing and zero-frequency handling](classification.md#Laplace%20smoothing%20and%20zero-frequency%20handling)
  - classification / [§ worked Naive Bayes posterior computation](classification.md#worked%20naive%20bayes%20posterior%20computation)

## week 4 lecture 2

- datetime: 2026-02-26T13:30:00+08:00/2026-02-26T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: the bias-variance decomposition
- [bias-variance decomposition](bias-variance%20decomposition.md)
  - bias-variance decomposition / [§ bias and variance intuition](bias-variance%20decomposition.md#bias%20and%20variance%20intuition)
  - bias-variance decomposition / [§ random training sets, empirical error, and generalization gap](bias-variance%20decomposition.md#random-training-sets-empirical-error-and-generalization-gap)
  - bias-variance decomposition / [§ decomposition of expected squared error](bias-variance%20decomposition.md#decomposition%20of%20expected%20squared%20error)
  - bias-variance decomposition / [§ algebra of the decomposition](bias-variance%20decomposition.md#algebra-of-the-decomposition)
  - bias-variance decomposition / [§ two-term view and refined three-term view](bias-variance%20decomposition.md#two-term-view-and-refined-three-term-view)
  - bias-variance decomposition / [§ illustrations with model capacity](bias-variance%20decomposition.md#illustrations%20with%20model%20capacity)
  - bias-variance decomposition / [§ low-degree, high-degree, and intermediate fits](bias-variance%20decomposition.md#low-degree-high-degree-and-intermediate-fits)
  - bias-variance decomposition / [§ graph intuition: training error, validation error, and generalization gap](bias-variance%20decomposition.md#graph-intuition-training-error-validation-error-and-generalization-gap)
  - bias-variance decomposition / [§ regularization, cross-validation, and sample size](bias-variance%20decomposition.md#regularization-cross-validation-and-sample-size)
  - bias-variance decomposition / [§ PAC learning viewpoint](bias-variance%20decomposition.md#PAC-learning-viewpoint)
  - bias-variance decomposition / [§ modern scaling-law remark](bias-variance%20decomposition.md#modern-scaling-law-remark)
  - bias-variance decomposition / [§ classification remark](bias-variance%20decomposition.md#classification-remark)
  - bias-variance decomposition / [§ ensemble learning](bias-variance%20decomposition.md#ensemble%20learning)
  - bias-variance decomposition / [§ bagging as variance reduction](bias-variance%20decomposition.md#bagging-as-variance-reduction)
  - bias-variance decomposition / [§ boosting as bias reduction](bias-variance%20decomposition.md#boosting-as-bias-reduction)

## week 4 tutorial

- datetime: 2026-02-26T18:00:00+08:00/2026-02-26T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- topic: Pandas; scikit-learn; logistic regression
- [logistic regression](logistic%20regression.md)
  - logistic regression / [§ binary logistic model and decision boundary](logistic%20regression.md#binary%20logistic%20model%20and%20decision%20boundary)
- [classification](classification.md)
  - classification / [§ performance metrics for classification](classification.md#performance-metrics-for-classification)
  - classification / [§ confusion matrix and accuracy](classification.md#confusion-matrix-and-accuracy)

## week 5 lecture 1

- datetime: 2026-03-03T13:30:00+08:00/2026-03-03T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: feedforward neural networks
- [feedforward neural network](feedforward%20neural%20network.md)
  - feedforward neural network / [§ multilayer perceptron as function approximator](feedforward%20neural%20network.md#multilayer%20perceptron%20as%20function%20approximator)
  - feedforward neural network / [§ units, layers, and nonlinear composition](feedforward%20neural%20network.md#units-layers-and-nonlinear-composition)
  - feedforward neural network / [§ layerwise notation and forward propagation](feedforward%20neural%20network.md#layerwise-notation-and-forward-propagation)
  - feedforward neural network / [§ repeated matrix-nonlinearity viewpoint](feedforward%20neural%20network.md#repeated%20matrix-nonlinearity%20viewpoint)
  - feedforward neural network / [§ universal approximation and why depth still helps](feedforward%20neural%20network.md#universal-approximation-and-why-depth-still-helps)
  - feedforward neural network / [§ initialization and activation functions](feedforward%20neural%20network.md#initialization-and-activation-functions)
  - feedforward neural network / [§ why initialization matters](feedforward%20neural%20network.md#why-initialization-matters)
  - feedforward neural network / [§ classical activations: sigmoid and tanh](feedforward%20neural%20network.md#classical-activations-sigmoid-and-tanh)
  - feedforward neural network / [§ rectifier family: ReLU, leaky ReLU, parametric ReLU, ELU, and softplus](feedforward%20neural%20network.md#rectifier-family-relu-leaky-relu-parametric-relu-elu-and-softplus)
  - feedforward neural network / [§ smooth and gated modern activations](feedforward%20neural%20network.md#smooth-and-gated-modern-activations)
  - feedforward neural network / [§ activation comparison: theoretical and empirical characteristics](feedforward%20neural%20network.md#activation-comparison-theoretical-and-empirical-characteristics)
  - feedforward neural network / [§ vanishing-gradient problem](feedforward%20neural%20network.md#vanishing-gradient-problem)

## week 5 lecture 2

- datetime: 2026-03-05T13:30:00+08:00/2026-03-05T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: feedforward neural networks; fundamental issues in deep learning; TensorFlow Playground
- [deep learning training](deep%20learning%20training.md)
  - deep learning training / [§ weight decay, bagging intuition, and dropout](deep%20learning%20training.md#weight%20decay-bagging%20intuition-and-dropout)
  - deep learning training / [§ feature scale, regularization geometry, and weight decay](deep%20learning%20training.md#feature-scale-regularization-geometry-and-weight-decay)
  - deep learning training / [§ bagging intuition and subnetworks](deep%20learning%20training.md#bagging-intuition-and-subnetworks)
  - deep learning training / [§ masking, minibatches, and test-time scaling](deep%20learning%20training.md#masking-minibatches-and-test-time-scaling)
- [feedforward neural network](feedforward%20neural%20network.md)
  - feedforward neural network / [§ probabilistic outputs and loss functions](feedforward%20neural%20network.md#probabilistic%20outputs%20and%20loss%20functions)
  - feedforward neural network / [§ feature extractor and logits](feedforward%20neural%20network.md#feature-extractor-and-logits)
  - feedforward neural network / [§ what a logit means](feedforward%20neural%20network.md#what-a-logit-means)
  - feedforward neural network / [§ linear-Gaussian output for regression](feedforward%20neural%20network.md#linear-gaussian-output-for-regression)
  - feedforward neural network / [§ sigmoid output for binary classification](feedforward%20neural%20network.md#sigmoid-output-for-binary-classification)
  - feedforward neural network / [§ softmax output for multiclass classification](feedforward%20neural%20network.md#softmax-output-for-multiclass-classification)
  - feedforward neural network / [§ backpropagation](feedforward%20neural%20network.md#backpropagation)
  - feedforward neural network / [§ chain rule and local error signals](feedforward%20neural%20network.md#chain-rule-and-local-error-signals)
  - feedforward neural network / [§ repeated transposed-Jacobian viewpoint](feedforward%20neural%20network.md#repeated%20transposed-jacobian%20viewpoint)
  - feedforward neural network / [§ output-layer derivatives](feedforward%20neural%20network.md#output-layer-derivatives)
  - feedforward neural network / [§ hidden-layer derivatives](feedforward%20neural%20network.md#hidden-layer-derivatives)
  - feedforward neural network / [§ algorithm and implementation notes](feedforward%20neural%20network.md#algorithm-and-implementation-notes)

## week 5 tutorial

- datetime: 2026-03-05T18:00:00+08:00/2026-03-05T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- topic: feedforward neural networks in PyTorch
- [feedforward neural network](feedforward%20neural%20network.md)
  - feedforward neural network / [§ layerwise notation and forward propagation](feedforward%20neural%20network.md#layerwise-notation-and-forward-propagation)
  - feedforward neural network / [§ repeated matrix-nonlinearity viewpoint](feedforward%20neural%20network.md#repeated%20matrix-nonlinearity%20viewpoint)
  - feedforward neural network / [§ why initialization matters](feedforward%20neural%20network.md#why-initialization-matters)
  - feedforward neural network / [§ rectifier family: ReLU, leaky ReLU, parametric ReLU, ELU, and softplus](feedforward%20neural%20network.md#rectifier-family-relu-leaky-relu-parametric-relu-elu-and-softplus)
  - feedforward neural network / [§ activation comparison: theoretical and empirical characteristics](feedforward%20neural%20network.md#activation-comparison-theoretical-and-empirical-characteristics)
  - feedforward neural network / [§ vanishing-gradient problem](feedforward%20neural%20network.md#vanishing-gradient-problem)
  - feedforward neural network / [§ backpropagation](feedforward%20neural%20network.md#backpropagation)
  - feedforward neural network / [§ repeated transposed-Jacobian viewpoint](feedforward%20neural%20network.md#repeated%20transposed-jacobian%20viewpoint)
  - feedforward neural network / [§ algorithm and implementation notes](feedforward%20neural%20network.md#algorithm-and-implementation-notes)

## week 6 lecture 1

- datetime: 2026-03-10T13:30:00+08:00/2026-03-10T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: fundamental issues in deep learning; optimization algorithms
- [deep learning training](deep%20learning%20training.md)
  - deep learning training / [§ weight decay, bagging intuition, and dropout](deep%20learning%20training.md#weight%20decay-bagging%20intuition-and-dropout)
  - deep learning training / [§ feature scale, regularization geometry, and weight decay](deep%20learning%20training.md#feature-scale-regularization-geometry-and-weight-decay)
  - deep learning training / [§ optimization algorithms for deep networks](deep%20learning%20training.md#optimization%20algorithms%20for%20deep%20networks)
  - deep learning training / [§ optimizer-state initialization](deep%20learning%20training.md#optimizer-state-initialization)
  - deep learning training / [§ momentum and velocity-based updates](deep%20learning%20training.md#momentum-and-velocity-based-updates)
  - deep learning training / [§ adaptive learning rates: AdaGrad and RMSProp](deep%20learning%20training.md#adaptive-learning-rates-adagrad-and-rmsprop)
  - deep learning training / [§ Adam and AdamW](deep%20learning%20training.md#adam-and-adamw)
  - deep learning training / [§ learning-rate schedules](deep%20learning%20training.md#learning-rate-schedules)
  - deep learning training / [§ scheduled decay and exponential decay](deep%20learning%20training.md#scheduled-decay-and-exponential-decay)
  - deep learning training / [§ cosine annealing and warm restarts](deep%20learning%20training.md#cosine-annealing-and-warm-restarts)
  - deep learning training / [§ batch normalization](deep%20learning%20training.md#batch%20normalization)
  - deep learning training / [§ data normalization and scale mismatch](deep%20learning%20training.md#data-normalization-and-scale-mismatch)
  - deep learning training / [§ normalization inside deep models](deep%20learning%20training.md#normalization-inside-deep-models)
  - deep learning training / [§ standardization, learnable affine correction, and inference mode](deep%20learning%20training.md#standardization-learnable-affine-correction-and-inference-mode)
  - deep learning training / [§ adaptive batch normalization under covariate shift](deep%20learning%20training.md#adaptive-batch-normalization-under-covariate-shift)

## week 6 lecture 2

- datetime: 2026-03-12T13:30:00+08:00/2026-03-12T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: convolutional neural networks
- convolutional neural network note not yet published

## week 6 tutorial

- datetime: 2026-03-12T18:00:00+08:00/2026-03-12T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- topic: convolutional neural networks in PyTorch; computation at convolutional layers
- convolutional neural network note not yet published

## week 7 lecture 1

- datetime: 2026-03-17T13:30:00+08:00/2026-03-17T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: convolutional neural networks
- convolutional neural network note not yet published

## week 7 lecture 2

- datetime: 2026-03-19T13:30:00+08:00/2026-03-19T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: recurrent neural networks

## week 7 tutorial

- datetime: 2026-03-19T18:00:00+08:00/2026-03-19T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- topic: recurrent neural networks in PyTorch; sequence-to-sequence models

## week 8 lecture 1

- datetime: 2026-03-24T13:30:00+08:00/2026-03-24T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: recurrent neural networks; attention in recurrent neural networks

## week 8 lecture 2

- datetime: 2026-03-26T13:30:00+08:00/2026-03-26T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- status: no class

## week 8 tutorial

- datetime: 2026-03-26T18:00:00+08:00/2026-03-26T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- status: no class

## week 9 lecture 1

- datetime: 2026-03-31T13:30:00+08:00/2026-03-31T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: transformer models; self-attention in PyTorch

## week 9 lecture 2

- datetime: 2026-04-02T13:30:00+08:00/2026-04-02T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- topic: transformer models

## week 9 tutorial

- datetime: 2026-04-02T18:00:00+08:00/2026-04-02T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- topic: BERT in PyTorch

## week 10 lecture 1

- datetime: 2026-04-14T13:30:00+08:00/2026-04-14T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- status: unscheduled

## week 10 lecture 2

- datetime: 2026-04-16T13:30:00+08:00/2026-04-16T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- status: unscheduled

## week 10 tutorial

- datetime: 2026-04-16T18:00:00+08:00/2026-04-16T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- status: unscheduled

## week 11 lecture 1

- datetime: 2026-04-21T13:30:00+08:00/2026-04-21T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- status: unscheduled

## week 11 lecture 2

- datetime: 2026-04-23T13:30:00+08:00/2026-04-23T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- status: unscheduled

## week 11 tutorial

- datetime: 2026-04-23T18:00:00+08:00/2026-04-23T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- status: unscheduled

## week 12 lecture 1

- datetime: 2026-04-28T13:30:00+08:00/2026-04-28T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- status: unscheduled

## week 12 lecture 2

- datetime: 2026-04-30T13:30:00+08:00/2026-04-30T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- status: unscheduled

## week 12 tutorial

- datetime: 2026-04-30T18:00:00+08:00/2026-04-30T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- status: unscheduled

## week 13 lecture 1

- datetime: 2026-05-05T13:30:00+08:00/2026-05-05T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- status: unscheduled

## week 13 lecture 2

- datetime: 2026-05-07T13:30:00+08:00/2026-05-07T14:50:00+08:00, PT1H20M
- venue: G002, CYT Building
- status: unscheduled

## week 13 tutorial

- datetime: 2026-05-07T18:00:00+08:00/2026-05-07T18:50:00+08:00, PT50M
- venue: Room 2306, Academic Building (near Lifts 17–18)
- status: unscheduled

## midterm examination

- datetime: 2026-03-28T14:00:00+08:00/2026-03-28T16:00:00+08:00, PT2H
- venue: Rooms 4619 and 4620, Academic Building (near Lifts 31–32)
- format:
  - coverage: L01-L05

## final examination

- datetime: 2026-05-21T12:30:00+08:00/2026-05-21T15:30:00+08:00, PT3H
- venue: Tsang Shiu Tim Art Hall, Atrium

## aftermath

### total

- grades: 100/100
  - statistics: ?
