---
aliases:
  - classification
  - discriminative classification
  - generative classification
  - naive Bayes classification
tags:
  - flashcard/active/special/academia/HKUST/COMP_4211/classification
  - language/in/English
---

<!-- check: ignore-file[two_sided_calc_warning]: concept note uses symbolic answers on QA cards -->

# classification

After introducing logistic regression as a probabilistic classifier, the course explicitly organizes classification around _three_ viewpoints. The probabilistic viewpoint learns a posterior model $Q(y\mid x)$ and predicts by $\hat y=\arg\max_y Q(y\mid x)$. The optimization-based viewpoint starts from a score function such as $f(x)=w^\top x+b$ and minimizes an empirical surrogate risk such as $\frac{1}{N}\sum_{i=1}^N \phi\bigl(y_if(x_i)\bigr)$. The generative viewpoint models $P(y)$ together with $P(x\mid y)$ and then predicts by $\hat y=\arg\max_y P(y)P(x\mid y)$.

These three viewpoints answer slightly different mathematical questions. The probabilistic approach asks for calibrated posterior probabilities. The optimization approach asks for a decision rule that is easy to train numerically and yields a good boundary. The generative approach asks how each class produces its observations and then derives the classifier from that structural model. Each route therefore highlights a different trade-off between assumptions, interpretability, computational convenience, and robustness.

This note also sharpens a core distinction that recurs throughout machine learning: _error_ is the task-level quantity we ultimately care about, but _loss_ is often the smoother quantity we actually optimize. In symbols, one often wants low empirical misclassification rate $\frac{1}{N}\sum_i \mathbf{1}[\hat y_i\ne y_i]$, yet trains by minimizing a smoother objective such as cross entropy or another surrogate. The probabilistic approach emphasizes posterior modeling and Bayes decisions, the optimization approach emphasizes margins and surrogate losses, and the generative approach emphasizes priors, likelihoods, and posterior inference.

---

Flashcards for this section are as follows:

- overview with formulas ::@:: The note compares three classification viewpoints: probabilistic classification learns $Q(y\mid x)$ and predicts by $\hat y=\arg\max_y Q(y\mid x)$; optimization-based classification minimizes a surrogate risk such as $\frac{1}{N}\sum_i \phi(y_if(x_i))$; and generative classification models $P(y)$ together with $P(x\mid y)$ and predicts by $\hat y=\arg\max_y P(y)P(x\mid y)$.
- why the note insists on three viewpoints ::@:: The three-viewpoint split makes clear that classification can be approached by posterior modeling, by direct loss minimization on a score function, or by modeling how each class generates data.
- why this lecture matters ::@:: Comparing probabilistic, optimization-based, and generative approaches clarifies the trade-off between calibrated posterior modeling, direct decision-boundary fitting, and stronger structural assumptions about how data are generated.
- error versus loss as a core theme with formulas ::@:: In classification one ultimately cares about error rates such as $\frac{1}{N}\sum_i \mathbf{1}[\hat y_i\ne y_i]$, but training usually minimizes a smoother surrogate loss such as cross entropy or $\frac{1}{N}\sum_i \phi(y_if(x_i))$.

## probabilistic approach to classification

The probabilistic approach begins with posterior class probabilities rather than with a hard decision boundary. One learns a conditional distribution $Q(y\mid x)$, or ideally $P(y\mid x)$, and then predicts by choosing the action that is best under those probabilities. In multiclass problems this means $\hat y=\arg\max_y Q(y\mid x)$. In binary equal-cost problems it reduces to thresholding the posterior probability at $0.5$.

This route is exemplified by [logistic regression](logistic%20regression.md) and its multiclass [softmax extension](logistic%20regression.md#softmax-regression). The key idea is _probabilities first, decisions second_. Parameters are fitted by likelihood or cross entropy so that the predicted distribution matches the observed labels as well as possible, and only afterward does one turn those probabilities into a class label by an argmax or threshold rule. The logistic-regression note develops this discriminative probabilistic viewpoint in full detail; this section places it inside the broader classification taxonomy.

This separation is useful because it cleanly distinguishes the estimation layer from the decision layer. The estimation layer learns posterior probabilities. The decision layer converts those probabilities into actions according to the chosen loss, threshold, or cost structure. So the same fitted probabilistic model can support different deployment rules without retraining the parameters.

The main strength of the probabilistic approach is that its scores have direct meaning: they can be interpreted, calibrated, thresholded, and used in cost-sensitive decisions. The main limitation is that good classification depends on learning the posterior probabilities well; unlike a generative model, this route does not explicitly explain how features are produced inside each class.

---

Flashcards for this section are as follows:

- probabilistic approach to classification ::@:: The probabilistic approach learns posterior class probabilities such as $Q(y\mid x)$ or $P(y\mid x)$ directly and then predicts by choosing the action that is best under those probabilities.
- multiclass posterior decision rule ::@:: In probabilistic multiclass classification, prediction is $\hat y=\arg\max_y Q(y\mid x)$, meaning choose the class with largest posterior probability.
- binary equal-cost threshold in the probabilistic approach ::@:: In binary equal-cost classification, the probabilistic decision rule predicts class $1$ when $Q(y=1\mid x)>0.5$ and class $0$ otherwise.
- probabilities first, decisions second ::@:: In the probabilistic approach, parameters are learned by likelihood or cross entropy to produce posterior probabilities first, and only then are those probabilities converted into actions by thresholding or argmax.
- estimation layer versus decision layer in probabilistic classification ::@:: The estimation layer learns posterior probabilities $Q(y\mid x)$, while the decision layer converts them into actions according to the chosen threshold or loss structure.
- why probabilistic classification is useful ::@:: Probabilistic classification is useful because posterior scores can be interpreted, thresholded, calibrated, and adapted to different cost structures without retraining the model.

### worked posterior-decision calculations

The simplest worked example is multiclass argmax. If a model outputs class probabilities $Q(y=1\mid x)=0.15$, $Q(y=2\mid x)=0.70$, and $Q(y=3\mid x)=0.15$, then the prediction is class $2$ because it has the largest posterior probability.

Binary thresholding shows the decision-theoretic layer more clearly. Suppose $Q(y=1\mid x)=0.42$ and $Q(y=0\mid x)=0.58$. Under equal costs, the threshold is $0.5$, so one predicts class $0$. But if false-negative cost is $C_{FN}=3$ and false-positive cost is $C_{FP}=1$, then the Bayes-optimal threshold becomes $\frac{C_{FP}}{C_{FP}+C_{FN}}=\frac14$. Since $0.42>0.25$, the same posterior probabilities now lead to class $1$. So the posterior model stays fixed while the action changes with the cost structure.

---

Flashcards for this section are as follows:

- worked multiclass posterior-decision example with full givens: If $Q(y=1\mid x)=0.15$, $Q(y=2\mid x)=0.70$, and $Q(y=3\mid x)=0.15$, what class is predicted? ::@:: Predict class $2$ because it has the largest posterior probability.
- worked binary posterior-threshold example with full givens: If $Q(y=1\mid x)=0.42$ and $Q(y=0\mid x)=0.58$, what is the prediction under equal costs? ::@:: Under equal costs the threshold is $0.5$, so predict class $0$ because $0.42<0.5$.
- worked cost-sensitive posterior-threshold example with full givens: If $Q(y=1\mid x)=0.42$, false-positive cost is $C_{FP}=1$, and false-negative cost is $C_{FN}=3$, what class is Bayes-optimal? ::@:: The threshold is $\frac{C_{FP}}{C_{FP}+C_{FN}}=\frac14$, and since $0.42>0.25$, predict class $1$.
- why the same posterior can yield different actions ::@:: A fixed posterior model can produce different optimal class decisions when the threshold or cost structure changes, because decision-making is separate from probability estimation.

## zero-one loss and empirical risk minimization

The optimization approach starts from a score function rather than from an explicit posterior model. Labels are encoded as $y\in\{-1,1\}$, the score is $f_{w,b}(x)=w^\top x+b$, and prediction is $\hat y = \operatorname{sign}(f_{w,b}(x))$. Unlike the logistic-regression note, the slides keep the intercept $b$ explicit instead of absorbing it into an augmented coordinate.

The direct task-level objective is the empirical zero-one risk. For one example, $L_{0/1}(y,\hat y)=\mathbf{1}(y\ne \hat y)$. For a dataset $\{(x_i,y_i)\}_{i=1}^N$, the empirical error is $R_{0/1}(w,b)=\frac{1}{N}\sum_{i=1}^N \mathbf{1}\bigl[y_i\ne \operatorname{sign}(w^\top x_i+b)\bigr]$. Minimizing this quantity is empirical risk minimization with respect to classification error itself.

This objective is attractive precisely because it is mathematically faithful to the task: every mistake costs $1$ and every correct decision costs $0$. But that same faithfulness creates an optimization problem. The objective changes only when a point crosses the decision boundary, so it is too discontinuous and too flat for ordinary gradient descent. The next subsections make that statement precise by rewriting the loss in terms of the margin.

---

Flashcards for this section are as follows:

- optimization-view linear classifier with score ::@:: In the optimization view, the score is $f_{w,b}(x)=w^\top x+b$ and the classifier is $\hat y=\operatorname{sign}(f_{w,b}(x))$ for labels encoded as $\{-1,1\}$.
- zero-one empirical risk formula ::@:: The empirical zero-one risk is $R_{0/1}(w,b)=\frac{1}{N}\sum_{i=1}^N \mathbf{1}\bigl[y_i\ne\operatorname{sign}(w^\top x_i+b)\bigr]$.
- empirical risk minimization ::@:: Empirical risk minimization means minimizing the average training loss or training error over the observed dataset.
- explicit bias term in the optimization approach ::@:: In this linear-classifier formulation, the intercept is written explicitly as $b$ rather than absorbed through the convention $x_0=1$.
- why zero-one loss is attractive ::@:: Zero-one loss is attractive because it measures exactly whether the classifier is correct or incorrect on each example.
- why direct error minimization is hard ::@:: Zero-one error is the right task-level quantity, but it is too discontinuous and too flat to optimize conveniently by gradient descent.

### sign function and margin formulation

The sign function is the simplest hard-decision rule: $\operatorname{sign}(z)=1$ if $z>0$, $\operatorname{sign}(z)=0$ if $z=0$, and $\operatorname{sign}(z)=-1$ if $z<0$. For classification with labels in $\{-1,1\}$, the decision is determined entirely by the sign of the score $z=w^\top x+b$.

Without the margin shorthand, zero-one loss is naturally written by cases: $L_{0/1}(y,z)=1$ if $(y=1\text{ and }z\le 0)$ or $(y=-1\text{ and }z\ge 0)$, and $L_{0/1}(y,z)=0$ otherwise. The margin removes that split. Define $m=yz$. If $y=1$, then $m=z$; if $y=-1$, then $m=-z$. Therefore both error cases collapse into the single condition $m\le 0$, so $L_{0/1}(y,z)=\mathbf{1}(yz\le 0)=\mathbf{1}(m\le 0)$.

The tie case is worth stating explicitly. In this course, zero-one loss is defined by the convention $\mathbf{1}(m\le 0)$, so a margin of exactly $0$ counts as loss $1$. Equivalently, a point exactly on the boundary is treated as _not correctly classified_. Other conventions exist, such as $\mathbf{1}(m<0)$ or a separate tie-handling rule, so one should not assume the boundary convention is universal across textbooks.

This one-variable reformulation is mathematically useful. A positive margin $m>0$ means the score has the same sign as the label, so the example is classified correctly. A zero margin $m=0$ means the point lies exactly on the decision boundary or tie case. A negative margin $m<0$ means the score has the wrong sign, so the point is misclassified. The magnitude $|m|$ then measures how far the example sits from the boundary in signed-score units.

The margin is also useful because it lets many losses be written as one scalar function $\phi(m)$ instead of two label-dependent cases. For example, hinge loss is $\max\{0,1-yz\}$ instead of "if $y=1$ use $\max(0,1-z)$, if $y=-1$ use $\max(0,1+z)$". Likewise the scaled logistic surrogate can be written as $\frac{1}{\log 2}\log(1+e^{-yz})$ instead of splitting into $\frac{1}{\log 2}\log(1+e^{-z})$ for $y=1$ and $\frac{1}{\log 2}\log(1+e^{z})$ for $y=-1$. So the margin turns label-specific casework into a single reusable horizontal axis.

---

Flashcards for this section are as follows:

- sign function ::@:: The sign function satisfies $\operatorname{sign}(z)=1$ for $z>0$, $\operatorname{sign}(z)=0$ for $z=0$, and $\operatorname{sign}(z)=-1$ for $z<0$.
- score in a linear classifier ::@:: In a linear classifier, the score is $z=w^\top x+b$, and the predicted class is determined by the sign of that score.
- margin formulation and meaning ::@:: If $z=w^\top x+b$, then zero-one loss is $L_{0/1}(y,z)=\mathbf{1}(yz\le 0)$. Here $yz>0$ means correct classification, $yz=0$ means boundary or tie, and $yz<0$ means misclassification.
- course convention for zero margin ::@:: In this course, zero-one loss is written as $\mathbf{1}(yz\le 0)$, so a margin of exactly $0$ counts as loss $1$; other texts may instead use conventions such as $\mathbf{1}(yz<0)$ or a separate tie rule.
- why the margin removes case splits ::@:: Writing losses as functions of the margin $m=yz$ turns label-dependent cases such as $\max(0,1-z)$ for $y=1$ and $\max(0,1+z)$ for $y=-1$ into one formula $\max(0,1-yz)$.
- why the margin is useful ::@:: The margin $yz$ summarizes both correctness and confidence, which is why many surrogate losses are written as functions of $yz$.

### worked margin computation

Suppose a data point has label $y=-1$ and score $z=w^\top x+b=0.7$. Then the predicted class is $\hat y=\operatorname{sign}(0.7)=+1$, so the prediction is wrong. The margin is $m=yz=(-1)(0.7)=-0.7<0$, which encodes the same conclusion in one number.

If we change the score to $z=-0.7$, then $\hat y=\operatorname{sign}(-0.7)=-1$, so the prediction becomes correct, and the margin becomes $m=yz=(-1)(-0.7)=0.7>0$. If we instead use $z=-0.05$, then $m=0.05>0$: the prediction is still correct, but only barely, so a tiny perturbation could flip the sign. This is why the margin carries more information than raw correctness alone.

During training, one should therefore read margins in layers: a negative margin means the point is currently on the wrong side of the boundary, a small positive margin means it is just barely rescued, and a large positive margin means the classifier is correct with a comfortable buffer.

---

Flashcards for this section are as follows:

- worked margin sign check with full interpretation: If $y=-1$ and $z=0.7$, what are $\hat y=\operatorname{sign}(z)$ and $yz$, and what do they mean? ::@:: $\hat y=+1$, so the prediction is wrong, and $yz=(-1)(0.7)=-0.7<0$, confirming a misclassified point.
- worked margin comparison with full givens: If $y=-1$, compare the cases $z=-0.7$ and $z=-0.05$ ::@:: For $z=-0.7$, the margin is $yz=0.7$, so the point is correctly classified with comfortable positive margin; for $z=-0.05$, the margin is only $0.05$, so the point is still correct but fragile because a tiny perturbation could flip the sign.
- margin-based training diagnostic ::@:: Watching how $yz$ moves from negative to positive gives richer feedback than raw correctness because it tracks both sign and confidence.

### why zero-one loss resists gradient descent

The lecture gives both an intuitive and a formal reason. Intuitively, if one perturbs the weights slightly, the predicted labels often do not change at all, so the empirical error remains exactly the same. A function that stays flat under small perturbations cannot provide a useful local descent direction.

Formally, write the margin loss as $\phi_{0/1}(m)=\mathbf{1}(m\le 0)$ with $m=yz$. Then $\phi_{0/1}(m)=1$ for $m<0$ and $\phi_{0/1}(m)=0$ for $m>0$, so $\phi'_{0/1}(m)=0$ whenever $m\ne 0$, and the derivative is undefined at $m=0$. For one example with $m_i=y_i(w^\top x_i+b)$, the chain rule gives $\nabla_w L_{0/1}^{(i)} = \phi'_{0/1}(m_i)\,y_i x_i$. Therefore $\nabla_w L_{0/1}^{(i)}=0$ whenever $m_i\ne 0$ and is undefined only on the boundary $m_i=0$.

The same problem appears at the dataset level: the empirical zero-one risk is a sum of flat pieces separated by discontinuous jumps when examples cross the boundary. If a margin moves from $-0.2$ to $-0.01$, the loss stays $1$. If it moves from $0.2$ to $5$, the loss stays $0$. Gradient descent wants local slope information, but zero-one loss only reports boundary crossings, not incremental improvement away from the boundary. That is why one replaces it by smoother surrogates.

---

Flashcards for this section are as follows:

- intuitive problem with zero-one loss ::@:: Small parameter changes often leave all predicted labels unchanged, so the empirical zero-one loss stays flat and provides no local signal.
- derivative of margin-form zero-one loss ::@:: If $\phi_{0/1}(m)=\mathbf{1}(m\le 0)$, then $\phi'_{0/1}(m)=0$ for $m\ne 0$ and is undefined at $m=0$.
- gradient problem for one example ::@:: For one example with margin $m_i=y_i(w^\top x_i+b)$, the chain rule gives $\nabla_w L_{0/1}^{(i)}=\phi'_{0/1}(m_i)\,y_i x_i$, so the gradient is $0$ whenever $m_i\ne 0$ and undefined on the boundary.
- why gradient descent fails on zero-one loss ::@:: Gradient descent fails on zero-one loss because the objective is flat away from boundary crossings, so local derivatives do not reveal gradual improvement.
- why a surrogate is needed ::@:: A surrogate loss is needed because classification error itself is too discontinuous or flat to optimize effectively by gradient-based methods.

## surrogate losses

To make optimization possible, one replaces zero-one loss with a surrogate that is smoother or at least more informative for gradient- or subgradient-based methods. The general margin-based surrogate objective is $L_\phi(w,b)=\frac{1}{N}\sum_{i=1}^N \phi\bigl(m_i\bigr)$ with $m_i=y_i(w^\top x_i+b)$. Instead of optimizing the discontinuous indicator $\mathbf{1}(m_i\le 0)$ directly, one chooses a function $\phi$ that still punishes negative or small margins but yields useful derivatives.

The slides stress two qualitative desiderata. First, $\phi$ should ideally be convex, so optimization is better behaved. Second, it is desirable for $\phi$ to upper-bound the zero-one loss pointwise: if $\phi(m)\ge \mathbf{1}(m\le 0)$ for every margin $m$, then the empirical error satisfies $\frac{1}{N}\sum_i \mathbf{1}(m_i\le 0)\le \frac{1}{N}\sum_i \phi(m_i)=L_\phi(w,b)$. In that sense, minimizing surrogate risk also pushes down an upper envelope of the true error.

The margin-based viewpoint unifies all of this. A large positive margin means the classifier is correct with room to spare; a negative margin means it is wrong. Good surrogate losses are therefore designed to be decreasing functions of $m$: large when $m$ is negative, moderate when $m$ is near $0$, and small when $m$ is large and positive.

There is also a common normalization convention behind many textbook surrogate losses. Since the course uses zero-one loss $\mathbf{1}(m\le 0)$ and therefore assigns loss $1$ at the boundary $m=0$, it is conventional to define or scale surrogate losses so that $\phi(0)=1$ as well. This makes the surrogate curve line up with zero-one loss at the decision boundary. Hinge loss already satisfies $\max(0,1-0)=1$, exponential loss satisfies $e^0=1$, and squared-margin loss satisfies $(1-0)^2=1$. The logistic surrogate needs the extra factor $1/\log 2$ because the unscaled logistic-regression loss gives $\log(1+e^0)=\log 2$ at $m=0$.

The lecture lists several canonical surrogates: logistic loss, hinge loss, exponential loss, and squared loss. They are not interchangeable, but they all provide usable optimization signals where zero-one loss is flat. This is exactly the role logistic regression's cross-entropy loss played in the previous lecture.

---

Flashcards for this section are as follows:

- surrogate loss idea ::@:: A surrogate loss replaces the zero-one loss with an objective of the form $L_\phi(w,b)=\frac{1}{N}\sum_i \phi\bigl(y_i(w^\top x_i+b)\bigr)$ that is easier to optimize while still encouraging correct classification.
- why surrogates are needed ::@:: Surrogate losses are needed because the zero-one loss is too flat for gradient-based optimization.
- upper-bound rationale for surrogates ::@:: If $\phi(m)\ge \mathbf{1}(m\le 0)$ for every margin $m$, then empirical error $\frac{1}{N}\sum_i \mathbf{1}(m_i\le 0)$ is bounded above by surrogate risk $\frac{1}{N}\sum_i \phi(m_i)$.
- margin in linear classification ::@:: For a binary label $y\in\{-1,1\}$ and score $z=w^\top x+b$, the product $yz$ is the signed margin: large positive values indicate confident correct classification.
- common boundary normalization convention ::@:: It is conventional to define or scale a margin surrogate so that $\phi(0)=1$, matching the course convention that zero-one loss also equals $1$ at the boundary $m=0$.
- what surrogate losses have in common ::@:: Surrogate losses are usually decreasing functions of the margin, so they become small for confidently correct predictions and large when the classifier has small or negative margin.

### convex upper bounds and margin shaping

The slides explicitly ask for convex approximations to zero-one loss. A real-valued function $f$ is convex if the line segment between any two points on its graph lies above or on the graph, equivalently if $f(tx_1+(1-t)x_2)\le tf(x_1)+(1-t)f(x_2)$ for all $t\in[0,1]$. Convexity matters because it makes optimization much more manageable and reduces the risk of pathological local behavior.

There is also a visual intuition. If one draws the graph of a convex function, then any straight chord joining two points on the graph stays above the curve. So the curve bends downward or stays flat, never arching upward above its secant lines. This matters in optimization because a bowl-shaped objective gives a much cleaner landscape than a wildly wavy one: moving downhill is less likely to encounter misleading local geometry.

The upper-bound requirement is also conceptually important. For the main examples, the pointwise comparison can be written explicitly. If $m\le 0$, then hinge loss satisfies $\max(0,1-m)\ge 1$; scaled logistic loss satisfies $\frac{1}{\log 2}\log(1+e^{-m})\ge \frac{1}{\log 2}\log 2 = 1$ because the function is decreasing and equals $1$ at $m=0$; exponential loss satisfies $e^{-m}\ge 1$; and squared-margin loss satisfies $(1-m)^2\ge 1$. If $m>0$, then zero-one loss is $0$ while all of these surrogates remain nonnegative. So each one upper-bounds $\mathbf{1}(m\le 0)$.

Margin shaping is the second reason these surrogates matter. Zero-one loss treats all positive margins identically and all negative margins identically. A surrogate can be more informative: it may continue rewarding larger positive margins, may penalize slightly negative margins differently from extremely negative ones, and may encode whether unit margin or only sign correctness is the desired notion of safety. So different surrogates represent different geometric preferences even when they agree on the sign convention.

---

Flashcards for this section are as follows:

- convexity definition ::@:: A function is convex if $f(tx_1+(1-t)x_2)\le tf(x_1)+(1-t)f(x_2)$ for all $t\in[0,1]$ and all relevant points $x_1,x_2$.
- visual intuition for convexity ::@:: Visually, a function is convex when every straight chord between two points on its graph lies above or on the graph, so the curve has a bowl-like rather than arching-upward shape.
- why convexity is desirable in surrogate losses ::@:: Convex surrogate losses are easier to optimize and behave more predictably than highly discontinuous nonconvex objectives such as zero-one loss.
- why the surrogate should upper-bound zero-one loss ::@:: If the surrogate loss upper-bounds zero-one loss, then minimizing the surrogate also pushes down an upper envelope of the true classification error.
- pointwise upper-bound check at negative margins ::@:: If $m\le 0$, then hinge gives $\max(0,1-m)\ge 1$, scaled logistic gives $\frac{1}{\log 2}\log(1+e^{-m})\ge 1$, exponential gives $e^{-m}\ge 1$, and squared-margin loss gives $(1-m)^2\ge 1$, so each upper-bounds zero-one loss on the error side.
- margin shaping ::@:: Surrogate losses often keep decreasing as the positive margin grows, so they reward not only correctness but also confidence.

### common surrogate losses

Let $m=yz$ denote the margin. Then the main surrogates can be compared directly on the same horizontal axis.

The unscaled logistic-regression loss is $\tilde\phi_{\log}(m)=\log(1+e^{-m})$. It is exactly the binary logistic-regression or Bernoulli cross-entropy loss written in margin form. Indeed, if $r\in\{0,1\}$ is the original label, $z$ is the score, $p=\sigma(z)$, and $y=2r-1\in\{-1,1\}$, then $-\bigl(r\log p+(1-r)\log(1-p)\bigr)=\log(1+e^{-yz})=\log(1+e^{-m})$. The slides scale this to $\phi_{\log}(m)=\frac{1}{\log 2}\log(1+e^{-m})$ so that $\phi_{\log}(0)=1$ and the curve becomes a pointwise upper bound of zero-one loss. This scaling does _not_ change the optimizer, because multiplying an objective by a positive constant leaves its argmin unchanged: $\arg\min_w \sum_i \phi_{\log}(m_i)=\arg\min_w \sum_i \tilde\phi_{\log}(m_i)$.

Its derivative is $\phi_{\log}'(m)=-\frac{1}{\log 2}\frac{1}{1+e^{m}}=-\frac{\sigma(-m)}{\log 2}$, so the penalty decays smoothly rather than shutting off abruptly.

The hinge loss is $\phi_{\mathrm{hinge}}(m)=\max\{0,1-m\}$. It is piecewise linear: $\phi_{\mathrm{hinge}}(m)=1-m$ for $m<1$ and $0$ for $m\ge 1$. Its subgradient is $-1$ for $m<1$, $0$ for $m>1$, and the interval $[-1,0]$ at $m=1$. This is why hinge loss explicitly demands a unit margin before the penalty vanishes.

The exponential loss is $\phi_{\exp}(m)=e^{-m}$ with derivative $\phi_{\exp}'(m)=-e^{-m}$. It penalizes negative margins very aggressively because the penalty grows exponentially as $m$ decreases.

The squared loss can also be written in margin form. Starting from the regression-style expression $(y-z)^2$ with $y\in\{-1,1\}$, one gets $(y-z)^2 = y^2-2yz+z^2 = 1-2m+m^2 = (1-m)^2$ because $y^2=1$ and $z^2=(yz)^2=m^2$. Its derivative is $-2(1-m)$. This makes it mathematically usable, but less natural for classification, because it keeps penalizing margins larger than $1$ and is minimized at $m=1$ rather than by simply pushing the margin upward indefinitely.

Each surrogate therefore encodes a different learning bias. Logistic loss behaves probabilistically and smoothly, hinge loss emphasizes achieving a unit margin, exponential loss strongly amplifies badly wrong examples, and squared loss treats classification as a numeric target-matching problem on the signed score.

---

Flashcards for this section are as follows:

- logistic surrogate and logistic-regression BCE relation ::@:: If $r\in\{0,1\}$, $y=2r-1\in\{-1,1\}$, score is $z$, and $p=\sigma(z)$, then binary cross entropy is $-\bigl(r\log p+(1-r)\log(1-p)\bigr)=\log(1+e^{-yz})$. The slides use the scaled version $\frac{1}{\log 2}\log(1+e^{-yz})$, which equals $1$ at margin $0$ and has the same minimizer because it differs only by a positive constant factor.
- why scaled logistic loss is used in the classification note ::@:: Scaling $\log(1+e^{-m})$ by $1/\log 2$ makes the loss equal to $1$ at $m=0$, so it becomes a pointwise upper bound of zero-one loss while remaining equivalent to ordinary logistic-regression cross entropy for optimization.
- derivative of scaled logistic loss ::@:: If $\phi_{\log}(m)=\frac{1}{\log 2}\log(1+e^{-m})$, then $\phi_{\log}'(m)=-\frac{1}{\log 2}\frac{1}{1+e^m}=-\frac{\sigma(-m)}{\log 2}$.
- hinge loss interpretation with subgradient ::@:: Hinge loss is $\phi_{\mathrm{hinge}}(m)=\max\{0,1-m\}$; it is $1-m$ for $m<1$, $0$ for $m>1$, and has subgradient interval $[-1,0]$ at $m=1$, so it becomes zero only after a unit margin is achieved.
- exponential loss interpretation with derivative ::@:: Exponential loss is $\phi_{\exp}(m)=e^{-m}$ with derivative $-e^{-m}$, so it punishes negative margins very strongly because the penalty grows exponentially as $m$ decreases.
- squared loss in margin form ::@:: For labels $y\in\{-1,1\}$ and score $z$, the regression-style squared loss satisfies $(y-z)^2=(1-yz)^2=(1-m)^2$ with $m=yz$, so it can be viewed as a margin-based surrogate, although it is less natural because it is minimized at $m=1$ rather than simply rewarding larger and larger positive margins.
- why different surrogates lead to different classifiers ::@:: Different surrogate losses weight margins and mistakes differently, so they can lead to different fitted decision boundaries and training dynamics.

### worked margin-to-loss comparison

Using one margin value across different losses makes their behavior concrete. Let $m=yz=2$ (confidently correct). Then $L_{0/1}=\mathbf{1}(2\le 0)=0$, hinge loss is $\max(0,1-2)=0$, scaled logistic loss is $\frac{1}{\log 2}\log(1+e^{-2})\approx 0.183$, the unscaled logistic-regression loss is $\log(1+e^{-2})\approx 0.127$, exponential loss is $e^{-2}\approx 0.135$, and squared-margin loss is $(1-2)^2=1$. So zero-one and hinge already consider the example fully satisfactory, while logistic and exponential still reward pushing the margin larger, and squared loss reveals why it is less natural as a classification surrogate.

Now let $m=yz=-1$ (wrong side of the boundary). Then $L_{0/1}=1$, hinge loss is $\max(0,1-(-1))=2$, scaled logistic loss is $\frac{1}{\log 2}\log(1+e)\approx 1.895$, the unscaled logistic-regression loss is $\log(1+e)\approx 1.313$, exponential loss is $e\approx 2.718$, and squared-margin loss is $(1-(-1))^2=4$. This side-by-side view shows the different optimization pressure: exponential is the most aggressive on negative margins, hinge is linear, and logistic is smoother.

The explicit scaled-versus-unscaled logistic comparison is important. The two values differ by the constant factor $1/\log 2$, so they measure the same shape in different units. Therefore they produce identical minimizers even though their numerical values differ.

---

Flashcards for this section are as follows:

- surrogate comparison at positive margin with scaled logistic: If $m=yz=2$, what are the zero-one, hinge, scaled logistic, unscaled logistic-regression, exponential, and squared-margin losses? ::@:: $L_{0/1}=0$, hinge $=\max(0,1-2)=0$, scaled logistic $=\frac{1}{\log 2}\log(1+e^{-2})\approx 0.183$, unscaled logistic-regression loss $=\log(1+e^{-2})\approx 0.127$, exponential $=e^{-2}\approx 0.135$, and squared-margin loss $=(1-2)^2=1$.
- surrogate comparison at negative margin with scaled logistic: If $m=yz=-1$, what are the zero-one, hinge, scaled logistic, unscaled logistic-regression, exponential, and squared-margin losses? ::@:: $L_{0/1}=1$, hinge $=\max(0,1-(-1))=2$, scaled logistic $=\frac{1}{\log 2}\log(1+e)\approx 1.895$, unscaled logistic-regression loss $=\log(1+e)\approx 1.313$, exponential $=e\approx 2.718$, and squared-margin loss $=(1-(-1))^2=4$.
- why the scaled-versus-unscaled logistic comparison matters ::@:: The classification-note logistic loss and the logistic-regression BCE have the same shape and differ only by the positive factor $1/\log 2$, so they are optimization-equivalent even though their numeric values differ.
- why the numeric comparison matters ::@:: The same margin can produce very different penalties under different surrogates, which explains differences in training dynamics and robustness.

### loss versus error

Once a surrogate is introduced, the course distinguishes sharply between _error_ and _loss_. For margins $m_i=y_i(w^\top x_i+b)$, empirical classification error is $\widehat{\operatorname{err}}(w,b)=\frac{1}{N}\sum_{i=1}^N \mathbf{1}(m_i\le 0)$, while empirical surrogate loss is $\widehat L_\phi(w,b)=\frac{1}{N}\sum_{i=1}^N \phi(m_i)$. Error only cares about whether each margin is on the correct side of $0$; loss also cares about _how far_ each point is from the boundary according to the chosen surrogate.

That difference means there is no monotone implication between the two quantities. Loss can decrease while error stays unchanged or even increases, and error can decrease while loss increases.

For example, suppose the scaled logistic surrogate is used. If the margins change from $(0.1,0.2)$ to $(2,3)$, then error stays $0$ in both cases because all margins are positive, but the average loss drops sharply because the positive margins become much larger. Conversely, if the margins change from $(10,-0.1)$ to $(0.01,0.01)$, then error improves from $\frac12$ to $0$, yet the average scaled logistic loss increases: one badly wrong point is fixed, but one formerly extremely confident correct point becomes almost ambiguous.

The opposite phenomenon can also occur. If the margins change from $(10,-10)$ to $(-0.01,-0.01)$, then average logistic loss decreases dramatically because the extremely negative margin $-10$ is no longer catastrophic, yet error worsens from $\frac12$ to $1$ because both points end up on the wrong side of the boundary. So loss and error answer genuinely different questions.

This is directly parallel to the regression case, where one optimizes a training objective but cares about future performance. In classification, surrogate loss is the smooth optimization target and error is the task-level decision metric. Regularization can improve both test loss and test error by preventing the classifier from chasing accidental patterns in the training data too aggressively, but the two curves need not move in lockstep.

---

Flashcards for this section are as follows:

- empirical error versus empirical surrogate loss ::@:: If margins are $m_i=y_i(w^\top x_i+b)$, then empirical error is $\widehat{\operatorname{err}}(w,b)=\frac{1}{N}\sum_i \mathbf{1}(m_i\le 0)$, while empirical surrogate loss is $\widehat L_\phi(w,b)=\frac{1}{N}\sum_i \phi(m_i)$; error counts wrong signs only, whereas loss also measures confidence through the chosen surrogate.
- training loss versus training error ::@:: Training loss measures the surrogate objective on the training set, whereas training error measures the actual misclassification rate on the training set.
- test loss versus test error ::@:: Test loss measures the surrogate objective on unseen data, whereas test error measures the fraction of unseen examples that are misclassified.
- counterexample where error improves but loss worsens ::@:: Using scaled logistic loss, margins can move from $(10,-0.1)$ to $(0.01,0.01)$, changing error from $\frac12$ to $0$ while increasing average loss because one formerly very confident correct point becomes almost ambiguous.
- counterexample where loss improves but error worsens ::@:: Using scaled logistic loss, margins can move from $(10,-10)$ to $(-0.01,-0.01)$, changing error from $\frac12$ to $1$ while decreasing average loss because the surrogate heavily rewards removing an extreme negative margin even though both points become slightly wrong.
- role of regularization in classification ::@:: Regularization can improve test loss and test error by reducing overfitting to peculiarities of the training data.

### calibration and threshold choice

Even with the same trained classifier score, operational performance can change dramatically depending on the decision threshold. This is most visible when classes are imbalanced or when false positives and false negatives have asymmetric costs. A threshold of $0.5$ is only one convention, not a universal optimum.

For probabilistic scores, one can tune the threshold on a validation set to optimize a target metric such as recall, precision, or $F_1$. This reinforces a key lecture principle: optimizing the training surrogate and choosing the deployment decision rule are related but distinct stages.

---

Flashcards for this section are as follows:

- why threshold tuning matters ::@:: Different decision thresholds on the same score model can trade precision against recall, especially under class imbalance.
- why threshold $0.5$ is not always optimal ::@:: A $0.5$ threshold is conventional but may be suboptimal when class priors or error costs are asymmetric.
- training versus deployment distinction ::@:: Minimizing training loss and selecting an operating threshold are separate design decisions that should both be validated.

## performance metrics for classification

Classification quality is evaluated by metrics that summarize confusion-matrix behavior, not only by the training loss. A model may be trained with cross entropy but judged by accuracy, precision, recall, and $F_1$, depending on the deployment objective.

The notation should be read carefully. For binary classification, we treat one class as the positive class and the other as the negative class. Then $TP$ means _true positive_ (true label positive, predicted positive), $FP$ means _false positive_ (true label negative, predicted positive), $TN$ means _true negative_ (true label negative, predicted negative), and $FN$ means _false negative_ (true label positive, predicted negative).

For multiclass classification, let $M_{a,b}$ denote the number of examples whose _true_ class is $a$ and whose _predicted_ class is $b$. So row index $a$ always refers to truth, and column index $b$ always refers to prediction. Diagonal entries $M_{c,c}$ are correct predictions, row sums $\sum_b M_{a,b}$ are supports of true class $a$, and column sums $\sum_a M_{a,b}$ are counts of predictions made as class $b$.

The first memory rule is: _loss trains parameters, metrics evaluate decisions_. The second memory rule is: _confusion matrix first, formulas second_. Once counts are clear, metric formulas become transparent.

---

Flashcards for this section are as follows:

- training loss versus evaluation metric ::@:: A classifier is often trained by minimizing cross entropy but evaluated by metrics such as accuracy, precision, recall, and $F_1$, so training objective and evaluation summary are distinct.
- metric-design memory rule ::@:: A practical memory rule is _loss trains probabilities, metrics evaluate thresholded decisions_.
- confusion-first memory rule ::@:: Compute metrics from confusion counts first; then formulas become bookkeeping rather than memorization.

### confusion matrix and accuracy

For binary classification, the confusion matrix tracks true positives ($TP$), false positives ($FP$), true negatives ($TN$), and false negatives ($FN$). Here $TP+TN+FP+FN$ is the total number of evaluated examples, and $TP+TN$ is the number predicted correctly. Therefore accuracy is $\frac{TP+TN}{TP+TN+FP+FN}$, the fraction of all predictions that are correct.

For multiclass classification with $C$ classes, let $M_{a,b}$ be the number of examples whose true class is $a$ and predicted class is $b$. Then the diagonal sum $\sum_{c=1}^C M_{c,c}$ counts all correctly classified examples, while the double sum $\sum_{a=1}^C\sum_{b=1}^C M_{a,b}$ counts all evaluated examples. So multiclass accuracy is diagonal mass divided by total mass: $\frac{\sum_{c=1}^C M_{c,c}}{\sum_{a=1}^C\sum_{b=1}^C M_{a,b}}$.

Accuracy is easy to read and communicate, but it can be misleading under class imbalance. So it should be paired with class-sensitive metrics such as precision, recall, and $F_1$.

---

Flashcards for this section are as follows:

- binary confusion matrix entries with meanings ::@:: Binary confusion counts are $TP$ (true positive), $FP$ (false positive), $TN$ (true negative), and $FN$ (false negative), where "true/false" compares prediction against the real label and "positive/negative" refers to the predicted class.
- binary accuracy formula with notation meaning ::@:: Binary accuracy is $\frac{TP+TN}{TP+TN+FP+FN}$ because $TP+TN$ counts correct predictions and $TP+TN+FP+FN$ counts all evaluated examples.
- multiclass confusion matrix notation with row-column roles ::@:: In multiclass settings, $M_{a,b}$ denotes the number of examples whose true class is $a$ and predicted class is $b$, so rows are true classes, columns are predicted classes, and diagonal entries are correct predictions.
- multiclass accuracy formula with interpretation ::@:: Multiclass accuracy is $\frac{\sum_{c=1}^C M_{c,c}}{\sum_{a=1}^C\sum_{b=1}^C M_{a,b}}$ because the numerator sums all correct diagonal counts and the denominator sums all examples in the confusion matrix.
- why accuracy may be misleading ::@:: Accuracy can look high on imbalanced data even when minority-class detection is poor.

### precision, recall, and F1: intuition and mnemonics

Precision measures prediction purity: among predicted positives, how many are truly positive? Recall measures coverage: among actual positives, how many were found? Their binary formulas are $P=\frac{TP}{TP+FP}$ and $R=\frac{TP}{TP+FN}$.

Useful mnemonics are: _precision = predicted-positive purity_ (the denominator uses predicted positives), and _recall = real-positive recovery_ (the denominator uses real positives). These two metrics usually trade off through threshold choice.

The $F_1$ score combines precision and recall by harmonic mean: $F_1=\frac{2PR}{P+R}=\frac{2TP}{2TP+FP+FN}$. Harmonic mean of two numbers $a$ and $b$ is defined as $\frac{2}{\frac{1}{a}+\frac{1}{b}}=\frac{2ab}{a+b}$, which is always less than or equal to both the arithmetic mean $\frac{a+b}{2}$ and the geometric mean $\sqrt{ab}$. This property makes harmonic mean appropriate for $F_1$ because one weak component drags the score down strongly, so high $F_1$ requires balance, not one-sided excellence.

---

Flashcards for this section are as follows:

- precision formula and denominator meaning ::@:: Precision is $P=\frac{TP}{TP+FP}$ because the denominator $TP+FP$ counts all examples predicted positive, so precision asks what fraction of predicted positives were actually positive.
- recall formula and denominator meaning ::@:: Recall is $R=\frac{TP}{TP+FN}$ because the denominator $TP+FN$ counts all truly positive examples, so recall asks what fraction of real positives were successfully found.
- F1 formula from precision and recall with purpose ::@:: $F_1=\frac{2PR}{P+R}$ is the harmonic mean of precision and recall, so it is high only when both are high.
- F1 formula from confusion counts with notation ::@:: In binary classification, $F_1=\frac{2TP}{2TP+FP+FN}$, where $TP$ is true positives, $FP$ false positives, and $FN$ false negatives.
- why F1 is harmonic mean with definition ::@:: Harmonic mean of $a$ and $b$ is $\frac{2ab}{a+b}$; it is always less than or equal to both arithmetic mean and geometric mean, so one weak metric pulls $F_1$ down strongly, requiring balance between precision and recall.
- precision-recall trade-off intuition ::@:: Lowering threshold usually increases recall and decreases precision, while raising threshold usually increases precision and decreases recall.

### multiclass precision, recall, and F1

For class $c$ in a multiclass confusion matrix $M$, treat class $c$ as positive and all other classes as negative. Then $M_{c,c}$ is the number of correctly predicted class-$c$ examples. The column sum $\sum_a M_{a,c}$ is the total number of examples predicted _as_ class $c$, while the row sum $\sum_b M_{c,b}$ is the total number of examples whose true label _is_ class $c$. Therefore the one-vs-rest definitions are $P_c=\frac{M_{c,c}}{\sum_a M_{a,c}}$, $R_c=\frac{M_{c,c}}{\sum_b M_{c,b}}$, and $F1_c=\frac{2P_cR_c}{P_c+R_c}$.

To summarize across classes:

- **macro averaging** computes unweighted class averages: $\text{macro }P=\frac{1}{C}\sum_{c=1}^C P_c$, $\text{macro }R=\frac{1}{C}\sum_{c=1}^C R_c$, $\text{macro }F_1=\frac{1}{C}\sum_{c=1}^C F1_c$. Each class contributes equally regardless of its size.
- **weighted macro averaging** weights each class by its support $n_c=\sum_{b=1}^C M_{c,b}$, which is the number of true examples from class $c$. The formula is $\text{weighted }P=\frac{1}{\sum_c n_c}\sum_c n_c P_c$, and similarly for recall and $F_1$. Classes with more examples therefore have proportionally more influence.
- **micro averaging** aggregates all one-vs-rest counts into global totals before applying formulas: define global true positives as $TP_{\text{global}}=\sum_c M_{c,c}$, global false positives as $FP_{\text{global}}=\sum_{c}\sum_{b\neq c} M_{b,c}$ (every non-diagonal entry in column $c$), and global false negatives as $FN_{\text{global}}=\sum_{c}\sum_{b\neq c} M_{c,b}$ (every non-diagonal entry in row $c$). Then micro precision is $P_{\text{micro}}=\frac{TP_{\text{global}}}{TP_{\text{global}}+FP_{\text{global}}}$, micro recall is $R_{\text{micro}}=\frac{TP_{\text{global}}}{TP_{\text{global}}+FN_{\text{global}}}$, and micro $F_1$ combines them as $\frac{2P_{\text{micro}}R_{\text{micro}}}{P_{\text{micro}}+R_{\text{micro}}}$. Crucially, in single-label multiclass we have $FP_{\text{global}}=FN_{\text{global}}$, so $P_{\text{micro}}=R_{\text{micro}}=\frac{TP_{\text{global}}}{N}$, and the harmonic mean of two equal numbers equals that number itself, giving micro $F_1=P_{\text{micro}}=R_{\text{micro}}$. This treats every individual prediction equally, not every class equally.

For single-label multiclass classification, micro precision = micro recall = micro $F_1$ = accuracy $= \frac{TP_{\text{global}}}{N}$. This identity is a useful exam memory cue because it provides a quick sanity check: if you compute micro $F_1$ and get a different value from accuracy, something is wrong.

---

Flashcards for this section are as follows:

- multiclass per-class precision formula with denominator meaning ::@:: With confusion matrix $M$, class-$c$ precision is $P_c=\frac{M_{c,c}}{\sum_a M_{a,c}}$ because the denominator is the total number of examples predicted as class $c$ (column $c$ total).
- multiclass per-class recall formula with denominator meaning ::@:: With confusion matrix $M$, class-$c$ recall is $R_c=\frac{M_{c,c}}{\sum_b M_{c,b}}$ because the denominator is the total number of true class-$c$ examples (row $c$ total).
- multiclass per-class F1 formula with setup ::@:: For class $c$, first compute one-vs-rest precision $P_c$ and recall $R_c$, then set $F1_c=\frac{2P_cR_c}{P_c+R_c}$.
- macro averaging definition with meaning ::@:: Macro metrics compute unweighted class averages: $\text{macro }F_1=\frac{1}{C}\sum_c F1_c$, so each class contributes equally regardless of size.
- weighted macro averaging definition with support ::@:: Weighted macro metrics weight each class by its support $n_c=\sum_b M_{c,b}$ (the number of true examples from class $c$), giving formula $\text{weighted }F_1=\frac{1}{\sum_c n_c}\sum_c n_c\,F1_c$.
- micro averaging definition with meaning ::@:: Micro metrics first compute global $TP_{\text{global}}=\sum_c M_{c,c}$, $FP_{\text{global}}=\sum_c\sum_{b\neq c}M_{b,c}$, and $FN_{\text{global}}=\sum_c\sum_{b\neq c}M_{c,b}$, then apply the binary formulas. In single-label multiclass, every misclassified example appears as an off-diagonal entry once in a column (as $FP$) and once in a row (as $FN$), so $FP_{\text{global}}=FN_{\text{global}}$. This gives $P_{\text{micro}}=R_{\text{micro}}=\frac{TP_{\text{global}}}{N}$, and harmonic mean of two equal numbers equals that number, so micro $F_1 = P_{\text{micro}} = R_{\text{micro}}$.
- single-label multiclass identity with explanation ::@:: In single-label multiclass, each example has exactly one true class and one predicted class, so every prediction either contributes to a diagonal element $M_{c,c}$ (correct, counted in global $TP$) or to exactly one off-diagonal element (incorrect). Every misclassification appears once in a column ($FP$) and once in a row ($FN$), so $FP_{\text{global}}=FN_{\text{global}}$. With this equality, micro precision $= \frac{TP}{TP+FP} = \frac{TP}{N}$, micro recall $= \frac{TP}{TP+FN} = \frac{TP}{N}$, and micro $F_1$ (the harmonic mean of two equal numbers) equals that same value $= \frac{TP}{N} =$ accuracy.

### worked metric computations

Binary worked example (same imbalance scenario): if $TP=5$, $FN=5$, $FP=0$, and $TN=90$, then accuracy is $95\%$, precision is $1$, recall is $0.5$, and $F_1=\frac{2}{3}$. So high accuracy can coexist with weak minority-class recall.

Multiclass worked example: let $M=\begin{bmatrix}40&2&3\\4&30&6\\1&5&29\end{bmatrix}$. Total samples are $120$ and diagonal sum is $99$, so accuracy is $\frac{99}{120}=0.825$. Per-class metrics are approximately $P_1=0.889, R_1=0.889, F1_1=0.889$; $P_2=0.811, R_2=0.750, F1_2=0.779$; and $P_3=0.763, R_3=0.829, F1_3=0.795$. Macro $F_1$ is approximately $\frac{0.889+0.779+0.795}{3}\approx 0.821$, and micro $F_1$ equals accuracy $0.825$.

---

Flashcards for this section are as follows:

- binary worked-metrics example with full givens: If $TP=5$, $FN=5$, $FP=0$, and $TN=90$, compute accuracy, precision, recall, and $F_1$ ::@:: Accuracy $=\frac{TP+TN}{TP+TN+FP+FN}=\frac{95}{100}=0.95$; precision $=\frac{TP}{TP+FP}=\frac{5}{5}=1$; recall $=\frac{TP}{TP+FN}=\frac{5}{10}=0.5$; and $F_1=\frac{2PR}{P+R}=\frac{2\cdot 1\cdot 0.5}{1+0.5}=\frac{2}{3}\approx 0.667$.
- binary worked-example interpretation mnemonic: If $TP=5$, $FN=5$, $FP=0$, and $TN=90$, what is the key takeaway? ::@:: Accuracy is high ($95\%$) but recall is only $50\%$, so the classifier is _precise but not sensitive_ on the positive class.
- multiclass worked-accuracy example with full givens: Given $M=\begin{bmatrix}40&2&3\\4&30&6\\1&5&29\end{bmatrix}$, compute multiclass accuracy ::@:: Total is $120$, diagonal sum is $99$, so accuracy is $\frac{99}{120}=0.825$.
- multiclass worked per-class metrics with full givens: Given $M=\begin{bmatrix}40&2&3\\4&30&6\\1&5&29\end{bmatrix}$, compute $(P_2,R_2,F1_2)$ for class $2$ (1-based) ::@:: Column-2 sum is $2+30+5=37$, row-2 sum is $4+30+6=40$, so $P_2=\frac{30}{37}\approx0.811$, $R_2=\frac{30}{40}=0.75$, and $F1_2=\frac{2P_2R_2}{P_2+R_2}\approx0.779$.
- multiclass worked macro/micro relation with full givens: Given $M=\begin{bmatrix}40&2&3\\4&30&6\\1&5&29\end{bmatrix}$ with single-label classes, what are macro $F_1$ (approx) and micro $F_1$? ::@:: Per-class $F_1$ values are about $0.889,0.779,0.795$, so macro $F_1\approx\frac{0.889+0.779+0.795}{3}=0.821$; micro $F_1$ equals accuracy in single-label multiclass, so micro $F_1=0.825$.

## discriminative versus generative classification

Classification algorithms can be split into two families by what they learn. A _discriminative_ model learns a rule that maps features directly to labels — either by modeling the posterior $P(y\mid x)$ (as logistic regression does) or by fitting a decision boundary through a score function and a surrogate loss. Either way, the model asks: _given these features, which class is most likely?_ It never tries to explain where the features came from.

A _generative_ model takes a different route. Instead of going straight from features to labels, it first models how each class generates its features: what is the prior $P(y)$ (how common is each class?), and what does the feature distribution $P(x\mid y)$ look like inside each class? The joint law then factors as $P(x,y)=P(y)P(x\mid y)$. Once these pieces are learned, the posterior $P(y\mid x)$ is derived through Bayes' rule. The model asks: _how might each class have produced this example?_

The two families have complementary strengths. Discriminative models are often simpler to train and can achieve strong accuracy directly because they focus all capacity on the decision boundary. Generative models require stronger assumptions about data structure but can be more data-efficient, handle missing features naturally, and produce interpretable likelihood scores. The lecture introduces Naive Bayes as the cleanest generative example.

---

Flashcards for this section are as follows:

- discriminative classifier definition ::@:: A discriminative classifier maps features to labels by modeling $P(y\mid x)$ directly or by fitting a decision boundary through a score function. It never explains how each class generates data.
- generative classifier definition ::@:: A generative classifier models how each class produces features by learning $P(y)$ and $P(x\mid y)$, then derives the posterior $P(y\mid x)$ using Bayes' rule.
- why discriminative versus generative matters ::@:: Discriminative models focus capacity on the decision boundary (often simpler and more accurate), while generative models require structural assumptions but can be more data-efficient and interpretable.
- discriminative models in this note ::@:: In this note, both probabilistic classification (for example logistic regression) and optimization-based surrogate-loss methods are discriminative because they learn a direct feature-to-label mapping without modeling the full data-generation process.

<!-- check: ignore-next-line[header_style]: Bayes is a proper noun -->
### Bayes-rule classification from a generative model

A generative classifier has two learned components: the class prior $P(y=c)$, which quantifies how likely class $c$ is before seeing any features, and the class-conditional density $P(x\mid y=c)$, which describes how feature vectors are distributed inside class $c$. Given a new input $x$, the posterior probability of class $c$ follows from Bayes' rule, $P(y=c\mid x)=\frac{P(y=c)\,P(x\mid y=c)}{P(x)}$.

Here $P(x)=\sum_{c'} P(y=c')\,P(x\mid y=c')$ is the marginal likelihood, obtained by marginalizing over all possible classes. It acts as a normalizing constant: it ensures the posterior probabilities sum to $1$ across classes.

Crucially, $P(x)$ is the same regardless of which class $c$ we are considering. When comparing two classes $c_1$ and $c_2$, the ratio $\frac{P(y=c_1\mid x)}{P(y=c_2\mid x)}=\frac{P(y=c_1)\,P(x\mid y=c_1)}{P(y=c_2)\,P(x\mid y=c_2)}$ does not depend on $P(x)$ at all. Therefore one compares unnormalized scores $s_c=P(y=c)\,P(x\mid y=c)$ and predicts by $\hat y=\arg\max_c\,s_c=\arg\max_c\,P(y=c)\,P(x\mid y=c)$.

This decomposition is conceptually revealing. The prior $P(y=c)$ captures class frequencies before the feature vector is observed, while $P(x\mid y=c)$ captures what features tend to look like inside class $c$. A rare class can still win if its likelihood $P(x\mid y=c)$ is much larger for the observed input.

---

Flashcards for this section are as follows:

- Bayes-rule posterior formula for classification with notation ::@:: In a generative classifier, the posterior is $P(y=c\mid x)=\frac{P(y=c)\,P(x\mid y=c)}{P(x)}$, where $P(x)=\sum_{c'}P(y=c')P(x\mid y=c')$ is the marginal likelihood.
- why the normalizing constant $P(x)$ can be ignored and what rule remains ::@:: $P(x)$ is identical for every candidate class, so it cancels in pairwise comparisons; therefore prediction can use unnormalized scores and the argmax rule simplifies to $\hat y=\arg\max_c\,P(y=c)\,P(x\mid y=c)$.
- what the prior and class-conditional each capture ::@:: The prior $P(y)$ captures how common each class is, while $P(x\mid y)$ describes what features typically look like inside each class.
- why a rare class can still win ::@:: A rare class with small prior $P(y)$ can still have the largest posterior if its class-conditional likelihood $P(x\mid y)$ is much larger than competing classes for the observed input.

### posterior log-score decomposition

In practice, multiplying many small probabilities can cause numerical underflow, so generative classifiers are often implemented in log form. Since the logarithm is monotone, $\arg\max_c\,f(c)=\arg\max_c\,\log f(c)$ for any positive $f$. Applying $\log$ to the unnormalized score gives $\log\bigl[P(y=c)\,P(x\mid y=c)\bigr]=\log P(y=c)+\log P(x\mid y=c)$, so the classification rule becomes $\hat y=\arg\max_c\,\bigl[\log P(y=c)+\log P(x\mid y=c)\bigr]$.

This additive decomposition separates two contributions: the _log-prior_ $\log P(y=c)$ encodes how common class $c$ is, and the _log-likelihood_ $\log P(x\mid y=c)$ encodes how well the observed features fit class $c$. Because the log function compresses large numbers, log-scores are more numerically stable: they replace products of many small probabilities by sums of negative numbers, which avoids the underflow that arises when computing $P(y=c)\prod_{j=1}^D P(x_j\mid y=c)$ for many features.

The decomposition also makes the prior-versus-evidence trade-off visible. A rare class with small prior $P(y=c)$ has a large negative log-prior, but it can still win if its log-likelihood is much larger (less negative) than competing classes. Conversely, when all classes have similar log-likelihoods, the prior dominates: the most common class wins.

---

Flashcards for this section are as follows:

- log-score form of Bayes classification and why it is valid ::@:: Since $\log$ is monotone, maximizing $f(c)$ and maximizing $\log f(c)$ give the same class. Applying $\log$ to $P(y=c)P(x\mid y=c)$ yields $\log P(y=c)+\log P(x\mid y=c)$, so the rule becomes $\hat y=\arg\max_c[\log P(y=c)+\log P(x\mid y=c)]$.
- why log-scores avoid numerical underflow ::@:: Multiplying many small probabilities can underflow to zero, but summing their logs keeps values in a manageable range.
- log-prior versus log-likelihood contributions ::@:: The log-prior $\log P(y=c)$ encodes class prevalence, and the log-likelihood $\log P(x\mid y=c)$ encodes how well features fit class $c$; the classification rule sums both terms.
- prior-dominance scenario ::@:: When all classes have similar log-likelihoods, the prior term dominates: the most common class wins.

## naive Bayes and conditional independence

**Notation.** Throughout this section, $x=(x_1,x_2,\ldots,x_D)$ denotes a _feature vector_ with $D$ components. Each $x_j$ is the value of the $j$-th feature. For example, in a spam filter, $x_1$ might be the word count for "free", $x_2$ for "money", and so on. The variable $y$ denotes a _class label_ — the category we want to predict, such as $y\in\{\text{spam},\text{not-spam}\}$. When we write $P(x\mid y=c)$, we mean the probability of observing the entire feature vector $x$ given that the true class is $c$.

The lecture's main generative example is Naive Bayes. Its logic has two main parts. First, without additional structure the full class-conditional model $P(x\mid y=c)$ becomes combinatorially huge. Second, conditional independence given the class label replaces that huge joint model by a factored one, making parameter estimation and prediction tractable.

The word _naive_ refers to the independence assumption itself: once the class $y=c$ is known, the model treats the features $x_1,\ldots,x_D$ as independent. That assumption is usually false in reality, but it can still work well because it dramatically reduces parameter count and because classification depends on relative class scores rather than on perfectly faithful joint feature modeling.

---

Flashcards for this section are as follows:

- notation reminder: feature vector and class label ::@:: In Naive Bayes, $x=(x_1,\ldots,x_D)$ is a feature vector with $D$ components, each $x_j$ is the value of the $j$-th feature, and $y$ is a class label such as spam or not-spam.
- why it is called naive with detail ::@:: The model is called naive because it assumes all features are independent once the class is known, which is much stronger than reality — in practice, features are usually correlated.
- why Naive Bayes can still work despite wrong assumption ::@:: Even though the independence assumption is crude, Naive Bayes can perform well because (1) it drastically reduces the number of parameters, and (2) classification only requires comparing relative scores, so biases may cancel across classes.

### parameter explosion without conditional independence

For discrete-valued features, the unrestricted class-conditional model is combinatorially expensive. The key counting argument is as follows.

Each feature $x_j$ can take $K_j$ distinct values. The full joint distribution $P(x\mid y=c)$ must assign a probability to every possible combination $(x_1,x_2,\ldots,x_D)$. In general there are $K_1\times K_2\times\cdots\times K_D$ combinations, and therefore that many minus $1$ free parameters (one less because all probabilities must sum to $1$, so the last one is determined).

For binary features ($K_j=2$ for all $j$), there are $2^D$ possible configurations and therefore $2^D-1$ free parameters per class. The "$-1$" arises from the normalization constraint: $\sum_x P(x\mid y=c)=1$, so once $2^D-1$ probabilities are chosen, the last one is forced.

**Simple example with $D=1$.** Suppose there is a single binary feature $x_1\in\{0,1\}$. The full joint $P(x_1\mid y=c)$ has $2^1=2$ possible outcomes: $(0)$ and $(1)$. We need $2^1-1=1$ free parameter, say $P(x_1=0\mid y=c)=p$. Then $P(x_1=1\mid y=c)=1-p$ is determined. For each class we estimate one parameter, so with $C$ classes the total is $C$ parameters.

**Scaling to $D=20$.** With $D=20$ binary features, there are $2^{20}=1{,}048{,}576$ possible configurations, requiring $1{,}048{,}575$ free parameters per class. With $C$ classes, the total is $C\times 1{,}048{,}575$ parameters — far too many to estimate reliably from typical datasets. The parameter count grows _exponentially_ with the number of features, which makes the full joint model intractable in high dimensions.

The lecture uses this counting argument to justify the independence assumption. The point is not merely elegance; it is feasibility. Without additional structure, generative modeling of high-dimensional inputs becomes statistically and computationally intractable.

---

Flashcards for this section are as follows:

- why $2^D-1$ instead of $2^D$ with normalization explanation ::@:: The full joint over $D$ binary features has $2^D$ possible outcomes. Because probabilities must sum to $1$, only $2^D-1$ are free — the last one is determined by normalization.
- worked $D=1$ example ::@:: With one binary feature $x_1\in\{0,1\}$, the joint $P(x_1\mid y=c)$ has $2$ outcomes and $2^1-1=1$ free parameter: choose $P(x_1=0\mid y=c)=p$, then $P(x_1=1\mid y=c)=1-p$.
- parameter count scaling for $D=20$ ::@:: With $D=20$ binary features, the full joint needs $2^{20}-1=1{,}048{,}575$ free parameters per class, which grows exponentially with $D$.
- why unrestricted generative models become impractical ::@:: The number of parameters in a full joint distribution grows exponentially with the number of features, making estimation difficult in high dimensions.
- why conditional independence is introduced ::@:: Conditional independence replaces an exponentially large joint model by a factored model with only $D$ small one-feature tables per class.

### naive Bayes factorization and prediction

Under the Naive Bayes assumption, the class-conditional distribution factorizes as $P(x\mid y=c,\theta)=\prod_{j=1}^D P(x_j\mid y=c,\theta_{jc})$. This means that, once the class label is known, each feature contributes independently to the likelihood. The model does _not_ claim unconditional independence of features; only conditional independence given the class.

Prediction then uses Bayes' rule in factored form. One computes posterior scores proportional to $P(y=c)\prod_{j=1}^D P(x_j\mid y=c,\theta_{jc})$ and chooses the class with the largest score. In practice, one often works with log-scores to turn the product into a sum and avoid numerical underflow.

---

Flashcards for this section are as follows:

- conditional versus unconditional independence ::@:: Naive Bayes assumes independence of features only after conditioning on the class label, not unconditional independence of the features themselves.
- naive Bayes factorization with parameters ::@:: The Naive Bayes factorization is $P(x\mid y=c,\theta)=\prod_{j=1}^D P(x_j\mid y=c,\theta_{jc})$.
- naive Bayes prediction score ::@:: Naive Bayes predicts by comparing class scores proportional to $P(y=c)\prod_{j=1}^D P(x_j\mid y=c,\theta_{jc})$.
- why log-scores are useful in Naive Bayes ::@:: Log-scores turn products of many probabilities into sums, which are numerically more stable and easier to compute.

### parameter estimation for discrete naive Bayes

Once the Naive Bayes structure is fixed, we must estimate its parameters from a training dataset $D=\{(x_i,y_i)\}_{i=1}^N$. The parameters are: (1) the class prior $\pi_c=P(y=c)$ for each class $c$, and (2) the conditional feature probabilities $\mu_{jck}=P(x_j=k\mid y=c)$ for each feature position $j$, each class $c$, and each possible feature value $k$.

**Likelihood and log-likelihood.** The _likelihood_ of the dataset is the probability of observing all $N$ examples under the model parameters $\theta$. Assuming examples are independent given the parameters, the likelihood is $p(D\mid\theta)=\prod_{i=1}^N p(x_i,y_i\mid\theta)$. Using the chain rule, $p(x_i,y_i\mid\theta)=p(y_i\mid\theta)\,p(x_i\mid y_i,\theta)$, where $p(y_i\mid\theta)=\pi_{y_i}$ and, under the Naive Bayes assumption, $p(x_i\mid y_i,\theta)=\prod_{j=1}^D \mu_{j,y_i,x_{ij}}$. Therefore $p(D\mid\theta)=\prod_{i=1}^N \pi_{y_i}\prod_{j=1}^D \mu_{j,y_i,x_{ij}}$.

The _log-likelihood_ is the logarithm of the likelihood. Since $\log$ is monotone, maximizing the likelihood is equivalent to maximizing the log-likelihood $\ell(\theta)=\log p(D\mid\theta)=\sum_{i=1}^N \log p(x_i,y_i\mid\theta)$. Taking logarithms turns products into sums, which is exactly what makes maximum-likelihood estimation easy to analyze here.

**Expanding the log-likelihood for Naive Bayes.** Substituting the factorized model gives $\ell(\theta)=\sum_{i=1}^N\log\bigl[\pi_{y_i}\prod_{j=1}^D \mu_{j,y_i,x_{ij}}\bigr]$. Applying $\log(ab)=\log a+\log b$ and $\log(\prod_j a_j)=\sum_j\log a_j$ yields $\ell(\theta)=\sum_{i=1}^N\bigl[\log\pi_{y_i}+\sum_{j=1}^D\log\mu_{j,y_i,x_{ij}}\bigr]$, which rearranges to $\ell(\theta)=\underbrace{\sum_{i=1}^N\log\pi_{y_i}}_{\text{prior term}}+\underbrace{\sum_{i=1}^N\sum_{j=1}^D\log\mu_{j,y_i,x_{ij}}}_{\text{feature-conditional term}}$. The prior and conditional-feature pieces therefore separate cleanly.

**Maximum-likelihood estimates.** For the class prior, the MLE is the observed class frequency $\hat\pi_c = \frac{n_c}{N}$, where $n_c = \sum_{i=1}^N \mathbf{1}(y_i=c)$ counts how many training examples belong to class $c$.

This is simply the empirical class frequency. In practice, one may replace this MLE by another modeling choice, such as (1) an _informative prior_ if domain knowledge suggests some classes are more common, (2) a _Laplace-smoothed prior_ $\hat\pi_c=\frac{n_c+\alpha}{N+\alpha C}$ to avoid zero-frequency issues, or (3) an _equal prior_ $\hat\pi_c=\frac{1}{C}$ if the training set is unbalanced but one wants all classes treated as equally likely.

For the conditional feature probabilities, the MLE is the relative frequency within each class, $\hat\mu_{jck}=\frac{n_{jck}}{n_c}$, where $n_{jck}=\sum_{i=1}^N\mathbf{1}(y_i=c)\,\mathbf{1}(x_{ij}=k)$ counts how many class-$c$ examples have feature $j$ taking value $k$.

This makes the computational appeal of Naive Bayes especially clear. Once the independence assumption is accepted, estimation becomes a matter of counting: count class sizes $n_c$, count within-class feature-value frequencies $n_{jck}$, and divide. There is no iterative optimization to solve.

---

Flashcards for this section are as follows:

- what is likelihood with full derivation ::@:: The likelihood is $p(D\mid\theta)=\prod_{i=1}^N p(x_i,y_i\mid\theta)$ by independence of examples. Step 1: apply chain rule $p(x_i,y_i\mid\theta)=p(y_i\mid\theta)p(x_i\mid y_i,\theta)$. Step 2: substitute $p(y_i\mid\theta)=\pi_{y_i}$ and apply Naive Bayes factorization $p(x_i\mid y_i,\theta)=\prod_{j=1}^D \mu_{j,y_i,x_{ij}}$. Step 3: combine to get $p(D\mid\theta)=\prod_{i=1}^N \pi_{y_i}\prod_{j=1}^D \mu_{j,y_i,x_{ij}}$. Higher likelihood means the data are more probable under the model.
- what is log-likelihood with derivation ::@:: The log-likelihood is $\ell(\theta)=\log p(D\mid\theta)$. Step 1: substitute the likelihood $\ell(\theta)=\log\bigl[\prod_{i=1}^N p(x_i,y_i\mid\theta)\bigr]$. Step 2: use $\log(\prod_i a_i)=\sum_i\log a_i$ to get $\ell(\theta)=\sum_{i=1}^N\log p(x_i,y_i\mid\theta)$. Taking the log turns products into sums, making optimization easier.
- Naive Bayes log-likelihood expansion with full derivation ::@:: Start from $\ell(\theta)=\sum_i\log p(x_i,y_i\mid\theta)$. Step 1: substitute Naive Bayes factorization $\ell(\theta)=\sum_i\log\bigl[\pi_{y_i}\prod_j\mu_{j,y_i,x_{ij}}\bigr]$. Step 2: apply $\log(ab)=\log a+\log b$ to get $\ell(\theta)=\sum_i\bigl[\log\pi_{y_i}+\log(\prod_j\mu_{j,y_i,x_{ij}})\bigr]$. Step 3: apply $\log(\prod_j)=\sum_j\log$ to get $\ell(\theta)=\sum_i\log\pi_{y_i}+\sum_i\sum_j\log\mu_{j,y_i,x_{ij}}$. The first sum depends only on the prior; the second only on feature-conditional parameters.
- prior estimate in Naive Bayes with reasoning ::@:: The class-prior MLE is $\hat\pi_c = \frac{n_c}{N}$, where $n_c=\sum_{i=1}^N\mathbf{1}(y_i=c)$. This is the fraction of training examples in class $c$ — it treats the observed frequency as the best estimate of the prior belief.
- prior estimate alternatives ::@:: Alternative priors include: informative priors from domain knowledge, Laplace-smoothed priors $\hat\pi_c=\frac{n_c+\alpha}{N+\alpha C}$ to avoid zero-frequency issues, or equal priors $\hat\pi_c=\frac{1}{C}$ when the training set is unbalanced but one believes classes should be equally likely.
- conditional-feature estimate in Naive Bayes with derivation ::@:: The conditional-feature MLE is $\hat\mu_{jck}=\frac{n_{jck}}{n_c}$, where $n_{jck}=\sum_{i=1}^N\mathbf{1}(y_i=c)\mathbf{1}(x_{ij}=k)$. This is the fraction of class-$c$ examples whose feature $j$ takes value $k$ — a within-class relative frequency.
- why Naive Bayes training reduces to counting ::@:: Under conditional independence, Naive Bayes parameter estimation is purely a counting problem: count class sizes $n_c$, count within-class feature-value frequencies $n_{jck}$, and divide. There is no iterative optimization to solve.

<!-- check: ignore-next-line[header_style]: Laplace is a proper noun -->
### Laplace smoothing and zero-frequency handling

Pure frequency estimates can fail catastrophically when a feature value never appears in one class during training. If $n_{jck}=0$ for some feature-class pair, then $\hat\mu_{jck}=\frac{n_{jck}}{n_c}=0$. This means the entire likelihood product for that class becomes zero: $P(y=c)\prod_j P(x_j\mid y=c)=0$ whenever the test sample contains that feature value, regardless of how informative all other features are.

**Pseudocounts.** A _pseudocount_ is an artificial count added to the observed frequencies before computing probabilities. It simulates having seen additional hypothetical examples. The idea is to pretend we have already observed each possible feature value at least $\alpha$ times in each class, so that no probability estimate is exactly zero.

**Laplace smoothing.** For a feature with $K_j$ discrete values, the Laplace-smoothed estimate is $\hat\mu_{jck}^{(\alpha)}=\frac{n_{jck}+\alpha}{n_c+\alpha K_j}$ with $\alpha>0$. Here $\alpha$ is the pseudocount per feature value. The numerator adds $\alpha$ to the observed count $n_{jck}$, and the denominator adds $\alpha K_j$ to the total count $n_c$ to maintain normalization: $\sum_{k=1}^{K_j}\hat\mu_{jck}^{(\alpha)}=\frac{\sum_k(n_{jck}+\alpha)}{n_c+\alpha K_j}=\frac{n_c+\alpha K_j}{n_c+\alpha K_j}=1$.

**Intuitive interpretation.** With $\alpha=1$ (standard Laplace smoothing), we pretend to have seen each feature value exactly once more than actually observed. This ensures every probability is at least $\frac{1}{n_c+K_j}>0$. As $n_c$ grows large, the smoothed estimate $\hat\mu_{jck}^{(\alpha)}\to\frac{n_{jck}}{n_c}$, so smoothing matters most when data are sparse.

Smoothing introduces a small bias toward uniformity but often lowers variance and improves generalization, especially when the dataset is modest relative to feature dimensionality.

---

Flashcards for this section are as follows:

- zero-frequency failure mode with consequence ::@:: Without smoothing, if $n_{jck}=0$ then $\hat\mu_{jck}=0$. This forces the entire likelihood $P(y=c)\prod_j P(x_j\mid y=c)$ to zero whenever the test sample contains feature value $k$, regardless of other features.
- what is a pseudocount with intuition ::@:: A pseudocount is an artificial count $\alpha$ added to observed frequencies. With $\alpha=1$ we pretend to have seen each feature value exactly once more than observed, ensuring no probability is exactly zero.
- Laplace-smoothed estimate with normalization derivation ::@:: The smoothed estimate is $\hat\mu_{jck}^{(\alpha)}=\frac{n_{jck}+\alpha}{n_c+\alpha K_j}$. Normalization check: $\sum_k\hat\mu_{jck}^{(\alpha)}=\frac{\sum_k(n_{jck}+\alpha)}{n_c+\alpha K_j}=\frac{n_c+K_j\alpha}{n_c+\alpha K_j}=1$ because $\sum_k n_{jck}=n_c$ and there are $K_j$ terms each adding $\alpha$.
- why smoothing helps Naive Bayes ::@:: Smoothing avoids brittle zero probabilities, introduces a small bias toward uniformity, and usually improves robustness on sparse or limited training data.
- smoothing limit as data grows ::@:: As $n_c\to\infty$, $\hat\mu_{jck}^{(\alpha)}=\frac{n_{jck}+\alpha}{n_c+\alpha K_j}\to\frac{n_{jck}}{n_c}$, so smoothing has most effect when data are sparse.

### worked Naive Bayes posterior computation

Consider two classes with priors $P(y=1)=0.4$ and $P(y=0)=0.6$, and two binary features under the Naive Bayes assumption. Suppose for an input $x=(x_1=1,x_2=0)$ we have $P(x_1=1\mid y=1)=0.9$, $P(x_2=0\mid y=1)=0.8$, $P(x_1=1\mid y=0)=0.3$, and $P(x_2=0\mid y=0)=0.7$.

Then unnormalized class scores are $s_1=0.4\cdot 0.9\cdot 0.8=0.288$ and $s_0=0.6\cdot 0.3\cdot 0.7=0.126$. So the posterior comparison predicts class $1$ because $s_1>s_0$. Normalizing gives $P(y=1\mid x)=\frac{0.288}{0.288+0.126}\approx 0.696$ and $P(y=0\mid x)\approx 0.304$.

---

Flashcards for this section are as follows:

- worked Naive Bayes class-score computation with full givens: With priors $P(y=1)=0.4$, $P(y=0)=0.6$, $P(x_1=1\mid y=1)=0.9$, $P(x_2=0\mid y=1)=0.8$, $P(x_1=1\mid y=0)=0.3$, $P(x_2=0\mid y=0)=0.7$, compute unnormalized scores for $x=(1,0)$ ::@:: $s_1=P(y=1)\cdot P(x_1=1\mid y=1)\cdot P(x_2=0\mid y=1)=0.4\cdot 0.9\cdot 0.8=0.288$; $s_0=P(y=0)\cdot P(x_1=1\mid y=0)\cdot P(x_2=0\mid y=0)=0.6\cdot 0.3\cdot 0.7=0.126$.
- worked Naive Bayes prediction decision with derivation: Given scores $s_1=0.288$ and $s_0=0.126$, what class is predicted? ::@:: Since $s_1=0.288>s_0=0.126$, predict class $1$ by the argmax rule $\hat y=\arg\max_c\,P(y=c)\prod_j P(x_j\mid y=c)$.
- worked Naive Bayes posterior normalization with steps: Using scores $s_1=0.288$ and $s_0=0.126$, compute $P(y=1\mid x)$ ::@:: First compute $P(x)=s_1+s_0=0.288+0.126=0.414$. Then $P(y=1\mid x)=\frac{s_1}{P(x)}=\frac{0.288}{0.414}\approx 0.696$ and $P(y=0\mid x)\approx 0.304$.
- why unnormalized-score comparison works ::@:: Posterior class prediction uses unnormalized scores $P(y=c)P(x\mid y=c)$ because the normalization constant $P(x)$ is identical across candidate classes and cancels in pairwise comparisons.
