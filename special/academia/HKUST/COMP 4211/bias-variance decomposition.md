---
aliases:
  - bias-variance decomposition
  - bias-variance tradeoff
  - bias-variance tradeoffs
tags:
  - flashcard/active/special/academia/HKUST/COMP_4211/bias-variance_decomposition
  - language/in/English
---

# bias-variance decomposition

The bias-variance decomposition explains why model selection is difficult even when overfitting is already understood informally. In COMP 4211, the operational two-element view is global: after averaging over the random training set and over future test inputs, the learner-versus-regression-function error splits into __squared bias of the learning method + variance of the training method__. This course-level two-term decomposition does _not_ require fixing a particular input point $x$.

If one wants a finer classical refinement, one then freezes a test evaluation point $x$ and decomposes the pointwise target error into three pieces. In that refined pointwise view, the quantities become functions of $x$: total pointwise target error $T(x)$, irreducible noise $N(x)$, squared bias $B(x)$, and variance $V(x)$. So the key distinction is: the course's main two-term bookkeeping is global and input-averaged, while the three-term decomposition is pointwise and requires fixing $x$ first.

This decomposition provides the conceptual bridge from linear models to regularization, cross-validation, bagging, and boosting. It gives precise mathematical content to statements like "this model is too rigid" or "this model is too unstable": the first corresponds to high bias and the second to high variance. Instead of saying only that a model underfits or overfits, one can ask which source of error is dominating and then choose a remedy that targets that source.

It also reframes model selection more carefully. Training error almost always decreases as model capacity increases, but expected future error does not. The reason is that increasing capacity usually lowers bias and raises variance at the same time. The best model is therefore the one that balances these competing forces rather than the one that merely fits the observed sample most aggressively. In that sense, the decomposition is not only a theorem about squared error; it is also a design guide for choosing capacity, regularization strength, sample size strategy, and ensemble method.

---

Flashcards for this section are as follows:

- course two-term bias-variance decomposition used in COMP 4211: Under squared-error regression, with $\epsilon_{\mathrm{BV}}=\mathbb{E}_{X,S}[(f^*(X)-h_S(X))^2]$, what is the course's main two-element decomposition? ::@:: COMP 4211 mainly uses the global two-term decomposition $\epsilon_{\mathrm{BV}}=B+V$.
- meanings of $B$ and $V$ in the course two-term decomposition: In $\epsilon_{\mathrm{BV}}=B+V$, what do $B$ and $V$ mean? ::@:: $B=\mathbb{E}_X[(\bar h(X)-f^*(X))^2]$ is global squared bias of the learning method, and $V=\mathbb{E}_{X,S}[(h_S(X)-\bar h(X))^2]$ is global variance of the training method.
- refined pointwise three-term decomposition: After fixing a test evaluation point $x$, what is the refined three-element decomposition? ::@:: After fixing $x$, define $T(x)=\mathbb{E}_{S,Y\mid X=x}[(Y-h_S(x))^2]$, $N(x)=\operatorname{Var}(Y\mid X=x)$, $B(x)=(\bar h(x)-f^*(x))^2$, and $V(x)=\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$. Then $T(x)=N(x)+B(x)+V(x)$.
- why the bias-variance decomposition matters for model selection: With the course view $\epsilon_{\mathrm{BV}}=B+V$, why is minimizing training error $\hat\epsilon_S(h_S)$ alone not enough? ::@:: The course view $\epsilon_{\mathrm{BV}}=B+V$ shows that choosing the model with the lowest training error is not optimal: a high-complexity model may achieve $\hat\epsilon_S(h_S)\approx 0$ while still having large variance of the training method $V$, causing poor generalization. The ideal model balances bias and variance rather than trading all variance reduction for zero training error.
- design-guide interpretation of bias-variance decomposition: Given the course decomposition $\epsilon_{\mathrm{BV}}=B+V$, how does diagnosing high bias versus high variance guide model improvements? ::@:: High global squared bias $B$ suggests the model family is too restricted: remedies include using more expressive models, adding features, or weakening regularization. High global variance $V$ suggests the method is too sensitive to the random training set: remedies include simplifying the model, adding regularization, collecting more training data, or using ensemble/variance-reduction methods such as bagging. If one later refines to the pointwise three-term view, the irreducible noise term $N(x)$ is not controllable by model choice.

## bias and variance intuition

Bias and variance are properties of a _learning procedure_, not just of one fitted model. Imagine repeatedly drawing a fresh training set from the same population, fitting the same algorithm each time, and then evaluating the resulting predictor on future data. If the procedure performs poorly on most such repetitions, it has high bias. If its performance changes drastically from one repetition to another, it has high variance.

This distinction matches the familiar underfitting-versus-overfitting story, but it is more precise. A low-capacity model class usually has relatively few parameters and limited expressive power. Because it cannot bend enough to follow the real signal, different random training sets often produce similarly shaped predictors, so variance is low; but those predictors are systematically wrong, so bias is high. A high-capacity model class usually has more parameters and much greater expressive power. That flexibility lowers systematic misspecification, but when the number of effective parameters is large relative to available data, small random changes in the sampled points can change the fitted parameters a great deal. Then variance is high.

There are two especially useful intuition lenses. __Expressive-power view__: low capacity means the hypothesis class cannot represent many shapes, so the fitted predictor is forced to stay too simple even when the truth is more complicated; high capacity means the class can represent many shapes, so it can track the signal more closely. __Parameter-sensitivity view__: low capacity usually means fewer adjustable parameters, so sample noise does not move the fitted coefficients very far; high capacity usually means many parameters, so if data are few relative to parameter count, noise can change the estimated parameters substantially.

These are two descriptions of the same trade-off. High bias means the average learned predictor is systematically wrong because the model family is too restrictive. High variance means the procedure is too sensitive: changing the sampled dataset changes the fitted parameters and hence the fitted predictor substantially. The most memorable phrasing is therefore: high bias means _poor performance on most occasions_, while high variance means _different performance on different occasions_.

---

Flashcards for this section are as follows:

- high bias intuition ::@:: High bias means the learning procedure performs poorly on most training samples because its assumptions are systematically too restrictive or mismatched, so even the average fitted predictor is wrong.
- high variance intuition ::@:: High variance means the learned model changes too much across different training samples because it is overly sensitive to data fluctuations.
- underfitting and bias ::@:: Underfitting is typically associated with high bias because the model family is too simple to capture the signal.
- overfitting and variance ::@:: Overfitting is typically associated with high variance because the model adapts too strongly to accidental quirks in the training sample.
- low model capacity as limited expressive power in the bias-variance context: Here _model capacity_ means the richness of the hypothesis class (e.g., degree-$d$ polynomial regression has $d+1$ parameters so higher $d$ = more capacity). What does low capacity imply about bias and variance? ::@:: Low model capacity means the hypothesis class has limited expressive power — it can only represent a small family of shapes (e.g., degree-0 constant functions) — so even the best-fit predictor in that class may be systematically too simple to match the true signal, leading to high bias. At the same time, the restricted parameter count means different training sets produce similar fitted predictors, so variance is low.
- high model capacity as parameter sensitivity in the bias-variance context: High model capacity means many adjustable parameters or degrees of freedom relative to available data (e.g., a degree-9 polynomial with 10 coefficients fitted to 10 data points). What does this imply about bias and variance? ::@:: High capacity lowers bias because the hypothesis class can represent many shapes and approximate the true signal more closely. But when parameter count is large relative to dataset size, multiple parameter settings can fit the observed sample equally well, so random noise in the training data can push the fitted parameters substantially in different directions. Different random training sets then produce very different fitted predictors, meaning high variance of the training method; globally this is summarized by a large $V=\mathbb{E}_{X,S}[(h_S(X)-\bar h(X))^2]$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- two complementary views of capacity ::@:: The same bias-variance trade-off can be read as an expressive-power story (what shapes the model class can represent) and as a parameter-sensitivity story (how strongly random data perturb the fitted coefficients).
- why the bias-variance trade-off is hard to resolve ::@:: Reducing bias typically requires a richer model class (more capacity, more parameters, less regularization), which in turn tends to increase sensitivity to random training data and hence increase variance; conversely, reducing variance typically requires a simpler, more constrained model, which increases bias. Both cannot typically be minimized simultaneously by a single model choice.
- memorable operational wording for bias versus variance in the bias-variance decomposition ::@:: A useful one-line cue: high bias means _poor performance on most occasions_ (the average learned predictor is systematically wrong regardless of which training set is used), while high variance means _different performance on different occasions_ (the learned predictor changes substantially across different training sets).

### random training sets, empirical error, and generalization gap

To formalize these ideas, fix the notation carefully. The population distribution over input-target pairs is $\mathcal D$, so a fresh example means a random draw $(X,Y)\sim\mathcal D$. A training set of size $m$ is $S=\{(x_i,y_i)\}_{i=1}^m\sim \mathcal D^m$, meaning that the $m$ examples are sampled independently from $\mathcal D$ and the superscript $m$ denotes the product distribution. A hypothesis or predictor is a function $h\colon x\mapsto h(x)$. In the linear-model notation used elsewhere in this course, this is often just shorthand for $h_w(x)=w^\top\phi(x)$ after choosing a parameter vector $w$, so the hypothesis class is $\mathcal H=\{x\mapsto w^\top\phi(x):w\in\mathbb R^d\}$. When a learning algorithm is trained on the particular sample $S$, the resulting fitted predictor is denoted by $h_S$; the subscript reminds us that training-set randomness makes the fitted predictor itself random.

For any fixed hypothesis $h$, the empirical squared-error loss on sample $S$ is $\hat\epsilon_S(h)=\frac{1}{m}\sum_{i=1}^m (y_i-h(x_i))^2$, while the population or generalization error is $\epsilon(h)=\mathbb{E}_{(x,y)\sim\mathcal D}[(y-h(x))^2]$. The first quantity averages over the finite training sample, whereas the second averages over the full data-generating distribution. Applying this to the learned predictor gives the random quantity $\epsilon(h_S)=\mathbb{E}_{(x,y)\sim\mathcal D}[(y-h_S(x))^2]$.

Because $S$ is random, the learned function $h_S$ is random, so the empirical error $\hat\epsilon_S(h_S)$ and the generalization error $\epsilon(h_S)$ are random as well. Define the sample-specific random variable $\operatorname{Gap}(S)=\epsilon(h_S)-\hat\epsilon_S(h_S)$, called the _generalization gap_ for that particular training set. It measures how much worse the learned predictor performs on the population than on the sample it was trained on.

Course materials also distinguish this random one-run gap from its average over repeated resampling. The _expected generalization gap_ is $\operatorname{Gap}_{\mathrm{exp}}=\mathbb{E}_S[\operatorname{Gap}(S)]=\mathbb{E}_S[\epsilon(h_S)-\hat\epsilon_S(h_S)]$. Intuitively, $\operatorname{Gap}(S)$ is the single-experiment optimism penalty (one train/test split), whereas $\operatorname{Gap}_{\mathrm{exp}}$ is the long-run average optimism of the learning procedure across many possible training sets.

Equivalently, $\mathbb{E}_S[\epsilon(h_S)] = \mathbb{E}_S[\hat\epsilon_S(h_S)] + \operatorname{Gap}_{\mathrm{exp}}$. So expected test error equals expected training error plus expected generalization gap.

This point is easy to miss when one trains a model only once. The central object is not merely one fitted function, but a random procedure $S\mapsto h_S$ that maps random samples to predictors. Bias and variance are properties of that random procedure, not of one frozen fitted model viewed in isolation.

---

Flashcards for this section are as follows:

- notation $\mathcal D$ and $S\sim\mathcal D^m$: What do these symbols mean? ::@:: Here $\mathcal D$ is the population distribution over input-target pairs $(X,Y)$, and $S\sim\mathcal D^m$ means the training set $S=\{(x_i,y_i)\}_{i=1}^m$ contains $m$ independent draws from that distribution.
- learned hypothesis $h_S$ in the bias-variance setting ::@:: The notation $h_S$ denotes the predictor produced by the learning algorithm when trained on the specific training set $S$; because $S$ is a random draw from $\mathcal{D}^m$, the fitted predictor $h_S$ is also random, and properties such as bias and variance are defined by averaging over all possible values of $S$.
- linear-model meaning of hypothesis notation: In this course, how should one interpret $h(x)$ in a linear-feature model? ::@:: In the linear-feature setting, $h(x)$ is often just shorthand for $h_w(x)=w^\top\phi(x)$ after choosing parameters $w$, and the hypothesis class is $\mathcal H=\{x\mapsto w^\top\phi(x):w\in\mathbb R^d\}$.
- empirical squared-error notation: For a hypothesis $h$ and training set $S=\{(x_i,y_i)\}_{i=1}^m$, what is $\hat\epsilon_S(h)$? ::@:: The empirical squared error is $\hat\epsilon_S(h)=\frac{1}{m}\sum_{i=1}^m (y_i-h(x_i))^2$, a finite-sample average over the training set.
- generalization error notation: For a hypothesis $h$, what are $\epsilon(h)$ and $\epsilon(h_S)$? ::@:: The population or generalization error is $\epsilon(h)=\mathbb{E}_{(x,y)\sim\mathcal D}[(y-h(x))^2]$; for the learned predictor this becomes $\epsilon(h_S)=\mathbb{E}_{(x,y)\sim\mathcal D}[(y-h_S(x))^2]$.
- generalization error versus training error, concrete contrast: How does $\epsilon(h_S)$ differ from the empirical training error $\hat\epsilon_S(h_S)$? ::@:: $\epsilon(h_S)$ averages over fresh data from the population, while $\hat\epsilon_S(h_S)=\frac{1}{m}\sum_{i=1}^m(y_i-h_S(x_i))^2$ averages only over the training sample. A degree-9 polynomial fitted to 10 noisy points can have $\hat\epsilon_S(h_S)\approx 0$ yet large $\epsilon(h_S)$.
- sample-specific generalization gap notation: For a training set $S$, what is $\operatorname{Gap}(S)$? ::@:: The sample-specific generalization gap is $\operatorname{Gap}(S)=\epsilon(h_S)-\hat\epsilon_S(h_S)$, the amount by which population error exceeds training error for the predictor trained on that same $S$.
- expected generalization gap notation: What is $\operatorname{Gap}_{\mathrm{exp}}$? ::@:: The expected generalization gap is $\operatorname{Gap}_{\mathrm{exp}}=\mathbb{E}_S[\operatorname{Gap}(S)]=\mathbb{E}_S[\epsilon(h_S)-\hat\epsilon_S(h_S)]$, the average optimism penalty over repeated random training sets.
- expected-gap identity: How are $\mathbb{E}_S[\epsilon(h_S)]$, $\mathbb{E}_S[\hat\epsilon_S(h_S)]$, and $\operatorname{Gap}_{\mathrm{exp}}$ related? ::@:: They satisfy $\mathbb{E}_S[\epsilon(h_S)] = \mathbb{E}_S[\hat\epsilon_S(h_S)] + \operatorname{Gap}_{\mathrm{exp}}$, so expected test error equals expected training error plus expected generalization gap.
- generalization error versus generalization gap: define and distinguish: With $h_S$ the predictor trained on sample $S$, $\epsilon(h_S)=\mathbb{E}_{(X,Y)\sim\mathcal{D}}[(Y-h_S(X))^2]$ the generalization error, and $\hat\epsilon_S(h_S)=\frac{1}{m}\sum_i(y_i-h_S(x_i))^2$ the training error, what is the difference between the course bias-variance object and the expected generalization gap $\operatorname{Gap}_{\mathrm{exp}}=\mathbb{E}_S[\epsilon(h_S)-\hat\epsilon_S(h_S)]$? ::@:: The course bias-variance object is $\epsilon_{\mathrm{BV}}=\mathbb{E}_{X,S}[(f^*(X)-h_S(X))^2]=B+V$, which studies learner error relative to the true regression function and separates it into global squared bias and global training-method variance. The expected generalization gap $\operatorname{Gap}_{\mathrm{exp}}=\mathbb{E}_S[\epsilon(h_S)-\hat\epsilon_S(h_S)]$ instead measures how optimistic training error is as an estimate of fresh-data error. If one keeps noisy targets explicitly, the pointwise refinement is $T(x)=N(x)+B(x)+V(x)$; the gap is still a train-versus-test comparison, not a decomposition into bias and variance.

## decomposition of expected squared error

To match the course convention, start with the learning-method error against the true regression function rather than the noisy target itself. Define $\epsilon_{\mathrm{BV}}=\mathbb{E}_{X,S}[(f^*(X)-h_S(X))^2]$, where $X\sim\mathcal D_X$ is a fresh random test input, $S\sim\mathcal D^m$ is the random training set, $h_S$ is the predictor trained on $S$, and $f^*(x)=\mathbb{E}[Y\mid X=x]$ is the true regression function. This is already a global quantity: no particular input point $x$ is being frozen.

Now define the average predictor $\bar h(x)=\mathbb{E}_S[h_S(x)]$. Add and subtract $\bar h(X)$ inside the square: $f^*(X)-h_S(X)=\bigl(f^*(X)-\bar h(X)\bigr)+\bigl(\bar h(X)-h_S(X)\bigr)$. After squaring and taking expectation over both $X$ and $S$, one obtains a global squared-bias term $B=\mathbb{E}_X[(\bar h(X)-f^*(X))^2]$, a global variance term $V=\mathbb{E}_{X,S}[(h_S(X)-\bar h(X))^2]$, and a cross term.

That cross term is zero because for each fixed random input $X$, the factor $f^*(X)-\bar h(X)$ is constant with respect to the training-set randomness, while $\mathbb{E}_S[\bar h(X)-h_S(X)\mid X]=0$ by definition of $\bar h$. Therefore the course two-element decomposition is simply $\epsilon_{\mathrm{BV}}=B+V$.

This is the decomposition emphasized in COMP 4211. It does not require fixing an input point, and its two terms are already the two quantities of practical interest for model selection: global squared bias of the learning method and global variance of the training method.

If one wants to keep the randomness of the target $Y$ itself explicit, then one moves to a different, more refined object: fix a test evaluation point $x$ and study $T(x)=\mathbb{E}_{S,Y\mid X=x}[(Y-h_S(x))^2]$. That pointwise refinement produces the three functions $N(x)$, $B(x)$, and $V(x)$ discussed below.

---

Flashcards for this section are as follows:

- average predictor $\bar h(x)$: What is it? ::@:: The average predictor is $\bar h(x)=\mathbb{E}_S[h_S(x)]$, the mean prediction obtained by averaging the learned predictor over all possible training sets.
- target mean function $f^*(x)$: What is it? ::@:: The target mean function is $f^*(x)=\mathbb{E}[Y\mid X=x]$, the regression function that gives the conditional mean target at input $x$.
- course two-term decomposition without fixing an input point: Using $\bar h(x)=\mathbb{E}_S[h_S(x)]$ and $f^*(x)=\mathbb{E}[Y\mid X=x]$, what quantity does COMP 4211 decompose, and what is the resulting formula? ::@:: COMP 4211 decomposes the global learner-versus-regression-function error $\epsilon_{\mathrm{BV}}=\mathbb{E}_{X,S}[(f^*(X)-h_S(X))^2]$ and obtains $\epsilon_{\mathrm{BV}}=B+V$, where $B=\mathbb{E}_X[(\bar h(X)-f^*(X))^2]$ is global squared bias and $V=\mathbb{E}_{X,S}[(h_S(X)-\bar h(X))^2]$ is global variance of the training method.
- why the course two-term decomposition does not require fixing $x$ ::@:: The course two-term decomposition is already defined after averaging over the random future input $X$, so it is a global summary of the learning method; its terms $B$ and $V$ are scalars, not functions of a fixed evaluation point.
- what is being decomposed: with $\epsilon_{\mathrm{BV}}=\mathbb{E}_{X,S}[(f^*(X)-h_S(X))^2]$ and $\operatorname{Gap}_{\mathrm{exp}}=\mathbb{E}_S[\epsilon(h_S)-\hat\epsilon_S(h_S)]$, what is the course bias-variance object and how does it differ from expected generalization gap? ::@:: The course decomposition expands $\epsilon_{\mathrm{BV}}=\mathbb{E}_{X,S}[(f^*(X)-h_S(X))^2]$ into $B+V$. This differs from the expected generalization gap $\operatorname{Gap}_{\mathrm{exp}}=\mathbb{E}_S[\epsilon(h_S)-\hat\epsilon_S(h_S)]$, which measures the average optimism of training error as an estimate of fresh-data error.
- why training error $\hat\epsilon_S(h_S)$ can mislead about generalization, with concrete example: Even if the course bookkeeping focuses on $\epsilon_{\mathrm{BV}}=B+V$, why can low training error still be misleading, and what is a concrete example? ::@:: Training error is optimistic because the learned predictor $h_S$ is chosen to fit the specific training set $S$; it does not account for how $h_S$ would change if $S$ were different. A concrete example: a degree-9 polynomial fitted to 10 noisy data points will interpolate all training points exactly (training error $\approx 0$), yet its predictions on new points can be wildly wrong because the 10 coefficients react strongly to sample noise in the training values. The variance term $V$ is large even though training error is near zero, so training error is a poor proxy for generalization.

### algebra of the decomposition

The course algebra is easiest if we derive the global two-term formula first. Work with the random test input $X$ directly rather than freezing a specific $x$. Start from $f^*(X)-h_S(X)=\bigl(f^*(X)-\bar h(X)\bigr)+\bigl(\bar h(X)-h_S(X)\bigr)$. After squaring and taking $\mathbb{E}_{X,S}$, define the global squared-bias term $B=\mathbb{E}_X[(\bar h(X)-f^*(X))^2]$, the global variance term $V=\mathbb{E}_{X,S}[(h_S(X)-\bar h(X))^2]$, and the cross term $C=\mathbb{E}_{X,S}[(f^*(X)-\bar h(X))(\bar h(X)-h_S(X))]$. Then $\epsilon_{\mathrm{BV}}=B+2C+V$.

Now cancel the cross term. Condition on the random input $X$: $C=\mathbb{E}_X[(f^*(X)-\bar h(X))\,\mathbb{E}_S[\bar h(X)-h_S(X)\mid X]]$. The inner expectation is $\bar h(X)-\mathbb{E}_S[h_S(X)\mid X]=0$ by definition of $\bar h$. Hence $C=0$, so the course two-element decomposition is $\epsilon_{\mathrm{BV}}=B+V$.

Only after this global derivation do we refine to a pointwise three-term formula. Fix a test evaluation point $x$ and define $T(x)=\mathbb{E}_{S,Y\mid X=x}[(Y-h_S(x))^2]$. Add and subtract $\bar h(x)$, then add and subtract $f^*(x)$. The same double-centering idea now yields $T(x)=N(x)+B(x)+V(x)$, where $N(x)=\operatorname{Var}(Y\mid X=x)$, $B(x)=(\bar h(x)-f^*(x))^2$, and $V(x)=\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$.

So the algebra comes in two levels. Global course level: decompose learner error relative to $f^*(X)$ into $B+V$ without fixing an input point. Refined pointwise level: after fixing $x$, decompose the total target error $T(x)$ into $N(x)+B(x)+V(x)$.

---

Flashcards for this section are as follows:

- bias-variance algebra — global two-term derivation: Let $\epsilon_{\mathrm{BV}}=\mathbb{E}_{X,S}[(f^*(X)-h_S(X))^2]$, $\bar h(x)=\mathbb{E}_S[h_S(x)]$, $B=\mathbb{E}_X[(\bar h(X)-f^*(X))^2]$, and $V=\mathbb{E}_{X,S}[(h_S(X)-\bar h(X))^2]$. What is the key expansion, and why does the cross term vanish? ::@:: Add and subtract $\bar h(X)$: $f^*(X)-h_S(X)=\bigl(f^*(X)-\bar h(X)\bigr)+\bigl(\bar h(X)-h_S(X)\bigr)$. Squaring gives $\epsilon_{\mathrm{BV}}=B+2C+V$ with $C=\mathbb{E}_{X,S}[(f^*(X)-\bar h(X))(\bar h(X)-h_S(X))]$. Conditioning on $X$ gives $C=\mathbb{E}_X[(f^*(X)-\bar h(X))\,\mathbb{E}_S[\bar h(X)-h_S(X)\mid X]]$, and the inner expectation is $0$ by definition of $\bar h$. Hence $\epsilon_{\mathrm{BV}}=B+V$.
- pointwise refinement after fixing $x$: After the global course derivation, how is the refined pointwise quantity defined, and what does it become? ::@:: Fix a test evaluation point $x$ and define $T(x)=\mathbb{E}_{S,Y\mid X=x}[(Y-h_S(x))^2]$. Then the double-centering argument gives $T(x)=N(x)+B(x)+V(x)$, where $N(x)=\operatorname{Var}(Y\mid X=x)$, $B(x)=(\bar h(x)-f^*(x))^2$, and $V(x)=\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$.
- double-centering intuition for the two levels of decomposition: Why does centering $f^*(X)-h_S(X)$ around $\bar h(X)$ yield $B+V$, while centering $Y-h_S(x)$ around $\bar h(x)$ and then $f^*(x)$ yields $T(x)=N(x)+B(x)+V(x)$? ::@:: The same centering trick is used twice but on different objects: globally, centering $f^*(X)-h_S(X)$ around $\bar h(X)$ yields the course two-term formula $B+V$; pointwise, centering $Y-h_S(x)$ first around $\bar h(x)$ and then around $f^*(x)$ yields the refined three-term formula $T(x)=N(x)+B(x)+V(x)$.

### two-term view and refined three-term view

This note uses two distinct levels of notation on purpose.

First, the refined pointwise three-term notation requires fixing a test evaluation point $x$. Then define:

- $T(x)=\mathbb{E}_{S,Y\mid X=x}[(Y-h_S(x))^2]$: total expected squared target error at the fixed evaluation point $x$.
- $N(x)=\operatorname{Var}(Y\mid X=x)=\mathbb{E}_{Y\mid X=x}[(Y-f^*(x))^2]$: irreducible noise at $x$.
- $B(x)=(\bar h(x)-f^*(x))^2$: pointwise squared bias at $x$.
- $V(x)=\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$: pointwise variance of the training method at $x$.

With this notation, the refined pointwise decomposition is $T(x)=N(x)+B(x)+V(x)$. Every symbol here depends on the fixed evaluation point $x$, so this is not yet the course's main two-term formula.

Second, the course two-term decomposition is global and does _not_ require fixing an input point. Average the pointwise bias and variance over the random input $X\sim\mathcal D$ and define $B=\mathbb{E}_X[B(X)]$ and $V=\mathbb{E}_X[V(X)]$. Then COMP 4211 works mainly with $\epsilon_{\mathrm{BV}}=B+V$.

This is the distinction that matters most pedagogically. The two-term course view is about the input-averaged learning method: global squared bias plus global variance of the training method. The refined three-term view is about one fixed input point $x$ and explicitly exposes the extra irreducible-noise term $N(x)$.

If one averages the refined pointwise decomposition over $X$, one gets $\mathbb{E}_X[T(X)]=\mathbb{E}_X[N(X)]+B+V$. So the global two-term course formula is not "two terms at a fixed $x$"; rather, it is the input-averaged bias-variance part of the story. For this course, that two-element decomposition is the main operational viewpoint.

---

Flashcards for this section are as follows:

- notation $T(x)$, $N(x)$, $B(x)$, and $V(x)$ in the refined pointwise view: After fixing a test evaluation point $x$, what do these four symbols mean? ::@:: $T(x)=\mathbb{E}_{S,Y\mid X=x}[(Y-h_S(x))^2]$ is total expected squared target error at the fixed point $x$; $N(x)=\operatorname{Var}(Y\mid X=x)$ is irreducible noise; $B(x)=(\bar h(x)-f^*(x))^2$ is pointwise squared bias; and $V(x)=\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$ is pointwise variance of the training method.
- refined pointwise three-term decomposition: After fixing the evaluation point $x$, what is the formula for $T(x)$ in terms of $N(x)$, $B(x)$, and $V(x)$? ::@:: After fixing the evaluation point $x$, the refined pointwise decomposition is $T(x)=N(x)+B(x)+V(x)$.
- course two-term decomposition from the pointwise quantities: How are the course-level quantities $B$ and $V$ obtained, and what formula does COMP 4211 emphasize? ::@:: Average the pointwise bias and variance over the random input $X$: $B=\mathbb{E}_X[B(X)]$ and $V=\mathbb{E}_X[V(X)]$. COMP 4211 mainly emphasizes the global two-term formula $\epsilon_{\mathrm{BV}}=B+V$.
- why the two-term view does not require fixing $x$ but the three-term view does ::@:: The course two-term view is already input-averaged, so $B$ and $V$ are global scalars describing the learning method. The refined three-term view exposes $N(x)$, $B(x)$, and $V(x)$ at one specific evaluation point, so it requires fixing $x$ first.
- relation between the pointwise three-term view and the course two-term view: If $T(x)=N(x)+B(x)+V(x)$ pointwise, what identity is obtained after averaging over the random input $X$? ::@:: Averaging the pointwise identity $T(x)=N(x)+B(x)+V(x)$ over $X$ gives $\mathbb{E}_X[T(X)]=\mathbb{E}_X[N(X)]+B+V$. So the course two-term formula keeps the input-averaged bias and variance, while the pointwise refinement additionally exposes irreducible noise.
- course scope reminder for this topic ::@:: For COMP 4211, the main operational bookkeeping is the global two-element decomposition $\epsilon_{\mathrm{BV}}=B+V$; the pointwise three-term formula $T(x)=N(x)+B(x)+V(x)$ is a refinement used only when one wants to separate out irreducible noise at a fixed input point. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## illustrations with model capacity

The standard visual illustration uses polynomial regression on repeatedly resampled datasets from a smooth target curve. Imagine a graph with three ingredients: a smooth true function, a cloud of noisy sampled points around it, and many fitted curves obtained by repeatedly drawing a training set and fitting a polynomial of fixed degree $d$. Looking across many such fits reveals whether the learning procedure is mainly biased or mainly variable.

Model capacity is closely tied to both expressive power and parameter count. In one variable, a degree-$d$ polynomial has $d+1$ coefficients, so increasing $d$ increases the number of adjustable parameters. Low capacity means fewer parameters and limited expressive power: the model cannot represent many shapes. High capacity means more parameters and much richer expressive power: the model can represent many shapes, but when data are limited relative to parameter count, random noise in the sampled points can move those parameters substantially.

This is the key capacity intuition. If parameter count is small relative to data size, each noisy observation has limited leverage on the fit, so different random samples often produce similar fitted parameters. If parameter count is large relative to data size, many different parameter settings can fit the observed sample well, so sample noise can push the fitted coefficients in noticeably different directions.

For example, if $d=0$, the model class contains only constant functions. Different sampled training sets lead to broadly similar fitted functions, so variance is low, but the average fit is far from the true nonlinear curve, so bias is high. If $d=1$, the model can tilt but still cannot bend, so bias remains substantial on a curved truth. If $d=9$, the story flips: the class is expressive enough to approximate the underlying curve closely, but because it has many coefficients relative to the available data, the fitted curve changes dramatically from one random sample to another, so variance is high.

An intermediate choice such as $d=3$ gives the best compromise in the classic picture. It is flexible enough to track the broad trend but not so flexible that every noisy point can twist the parameters strongly. This is the visual origin of the U-shaped validation/test-error curve: as capacity increases, bias tends to decrease, variance tends to increase, and the best generalization performance occurs somewhere in between.

---

Flashcards for this section are as follows:

- polynomial regression illustration of bias and variance: In the standard polynomial-regression demonstration where a smooth true function is estimated from noisy resampled training sets using degree-$d$ polynomials at various values of $d$, what general pattern do low-degree and high-degree models exhibit? ::@:: Low-degree models (e.g., $d=0$ or $d=1$) show high bias (the fitted curves cluster far from the true function, systematically underfitting the signal) but low variance (fitted curves from different training sets look similar to each other). High-degree models (e.g., $d=9$ on 10 points) show low bias on average but very high variance (fitted curves from different training sets vary wildly, diverging from each other even while the average may be close to the truth). An intermediate degree (e.g., $d=3$) achieves the best trade-off.
- model capacity and parameter count: In one-variable polynomial regression, how many coefficients does a degree-$d$ model have? ::@:: A degree-$d$ model has $d+1$ coefficients, so increasing model capacity also increases the number of adjustable parameters.
- low capacity versus high capacity intuition ::@:: Low capacity means limited expressive power and relatively few parameters, so the model is stable but can be systematically wrong; high capacity means rich expressive power and many parameters, so the model can match the signal better but also becomes more sensitive to sample noise.
- why parameter count relative to data matters ::@:: When parameter count is large relative to data size, many coefficient settings can fit the sample well, so random noise can move the fitted parameters strongly and produce high variance.
- why test or validation error has a U-shape as model capacity increases in the bias-variance setting ::@:: As model capacity increases (e.g., polynomial degree increases), global bias $B$ tends to decrease because the model class can represent the true signal more closely, but global variance of the training method $V$ tends to increase because more parameters react more strongly to sample noise. At low capacity, bias dominates and total test error is high; at intermediate capacity, bias and variance balance and test error is at its minimum; at high capacity, variance dominates and test error rises again, creating the characteristic U-shape. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- best model capacity choice in the bias-variance framework ::@:: The best model capacity is the one that balances the course-level two terms $B$ and $V$, not the one that minimizes training error $\hat\epsilon_S(h_S)$; richer models usually lower bias but raise variance, so the ideal capacity is the compromise that gives the smallest future prediction error. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- role of random noise in overfitting ::@:: A high-variance model can start fitting random noise in the sampled targets instead of the underlying signal.

### low-degree, high-degree, and intermediate fits

The low-degree case illustrates bias dominance. Because the hypothesis class is too rigid, even the average of many fitted models remains systematically wrong. The fitted parameters do not move much from one dataset to another, but that stability is not a virtue by itself: the model is stable because it cannot express the needed shape. It is _stable but wrong_.

The high-degree case illustrates variance dominance. Each individual training set can be fit extremely closely, and the average predictor may be near the truth, but the individual fitted curves vary wildly across training samples. This happens because the model has many adjustable coefficients, and when the sample is noisy or small relative to parameter count, those coefficients can swing sharply in response to tiny changes in the data. It is _expressive but unstable_.

The intermediate case illustrates why the trade-off is about procedures, not slogans. A model with enough flexibility to capture the main signal but not so much flexibility that it chases every fluctuation can achieve low expected generalization error. That is why one should think in terms of average performance over possible samples, not just one fitted curve.

This section is also a good place to connect the pictures back to the decomposition. In the low-degree case, the variance term is small and the squared-bias term dominates. In the high-degree case, the squared-bias term can be small while the variance term dominates. The intermediate case is the one where neither term overwhelms the other.

---

Flashcards for this section are as follows:

- low-degree picture ::@:: In the low-degree case, the fitted models look similar across datasets, which means low variance, but their average remains far from the true function, which means high bias.
- high-degree picture ::@:: In the high-degree case, the fitted models vary sharply across datasets, which means high variance, even though their average can track the true function fairly well.
- intermediate-capacity picture ::@:: An intermediate-capacity model can achieve low generalization error by keeping both bias and variance at moderate levels.
- method that is stable but wrong ::@:: A high-bias method is often stable across training sets yet systematically misses the true pattern.
- method that is expressive but unstable ::@:: A high-variance method can represent the target well on average but fluctuate too much from one sampled dataset to another because its many adjustable parameters react strongly to sample noise.
- which term dominates in each regime ::@:: In low-capacity regimes the squared-bias term usually dominates, in high-capacity regimes the variance term usually dominates, and intermediate capacity is where neither dominates too strongly.

### graph intuition: training error, validation error, and generalization gap

The model-capacity graphs attached to this topic should be read carefully. On the horizontal axis is model capacity or complexity. On the vertical axis is an error quantity such as training error, validation error, or test error. One picture usually overlays training and validation curves, while another picture shows repeated fitted curves for several capacity regimes.

The training-error curve typically slopes downward as capacity increases. This happens because a richer hypothesis class contains all simpler models plus additional ones, so it can fit the observed sample at least as well as before. In many pictures the training curve decreases almost monotonically.

The validation or test-error curve usually has a U-shape. On the left, capacity is too small, so the model underfits and both training and validation error are high. In the middle, the model is expressive enough to capture the main signal, so validation error reaches its minimum. On the right, capacity is so high that the model starts fitting sample-specific noise, so validation/test error rises even though training error keeps falling.

The generalization gap is the vertical distance between the training and validation/test curves at the same capacity value. On one fixed split this plotted quantity estimates the sample-specific random gap $\operatorname{Gap}(S)$. If one repeated the split or resampling procedure and averaged these vertical distances, that average would estimate $\operatorname{Gap}_{\mathrm{exp}}$. At low capacity this gap is often small because the model is too simple even to fit the training data strongly. As capacity increases, the gap often widens because the learner can fit the training sample more aggressively than it can fit new data. Graphically, this widening gap is one of the clearest visual signals of increasing variance.

Another common graphic shows many fitted curves from repeated resampling. A low-capacity panel shows many similar curves clustered together but far from the truth; a high-capacity panel shows curves spread wildly across the input range; an intermediate panel shows moderate spread and a reasonable average fit. These pictures and the error curves are two views of the same phenomenon: the curve panels show the variance directly as spread across fits, while the training/validation graph shows it indirectly through a widening generalization gap.

---

Flashcards for this section are as follows:

- what the axes mean in the capacity graph ::@:: In the standard capacity graph, the horizontal axis is model complexity or capacity and the vertical axis is an error quantity such as training, validation, or test error.
- training-error curve in the model-capacity graph: In the standard graph of training error and validation error versus model capacity, what shape does the training-error curve take and why? ::@:: Training error in a model-capacity graph typically decreases monotonically as model capacity increases, because a richer hypothesis class contains all simpler models plus additional ones, so it can fit the observed training sample at least as well as before; eventually a sufficiently expressive model can interpolate all training points and drive training error to nearly zero.
- why the validation/test curve is U-shaped ::@:: Validation or test error is often high at low capacity because of underfitting, lowest at intermediate capacity where bias and variance are balanced, and high again at large capacity because of overfitting.
- generalization-gap graph intuition ::@:: The generalization gap is the vertical difference between training and validation/test curves at the same capacity; it is often small at low capacity and larger at high capacity because high-capacity models fit training data more aggressively than new data.
- sample gap vs expected gap in graphs: If $\operatorname{Gap}(S)=\epsilon(h_S)-\hat\epsilon_S(h_S)$ and $\operatorname{Gap}_{\mathrm{exp}}=\mathbb{E}_S[\operatorname{Gap}(S)]$, how should a validation-curve gap be interpreted? ::@:: In one train/validation split, the plotted vertical distance estimates the sample-specific gap $\operatorname{Gap}(S)$; averaging that distance over repeated random splits estimates the expected generalization gap $\operatorname{Gap}_{\mathrm{exp}}$.
- two graph types in the polynomial-regression illustration: What is a repeated-fit graph, and how do the error-vs-capacity graph and repeated-fit graph show bias and variance together? ::@:: A repeated-fit graph overlays many fits from independently resampled training sets. In it, bias appears as the average fit's offset from the truth and variance as the spread across fits; in the error-vs-capacity graph, the same story appears indirectly through a U-shaped validation curve and a widening train-validation gap.

### regularization, cross-validation, and sample size

The decomposition connects directly to model-selection tools. Cross-validation helps estimate which capacity or regularization strength gives the best expected generalization performance. Instead of trusting training error, one compares models on held-out data and looks for the capacity region where validation error is smallest. In the language of the decomposition, cross-validation is a practical way to estimate where the bias-variance balance is most favorable.

Regularization changes the optimization problem so that large or unstable parameter values become expensive. In ridge-style regularization, for example, one minimizes a penalized objective such as training loss plus $\lambda\|w\|_2^2$. Increasing $\lambda$ usually raises bias somewhat because the fitted model is pulled toward simpler parameter values, but it often lowers variance because the parameters become less sensitive to random sample noise. Moderate regularization can therefore improve validation/test performance, while excessive regularization can underfit.

Sample size is the third major control knob. As more data are collected, each individual noisy observation has less leverage on the fitted parameters, so the learned predictor usually fluctuates less across resampled datasets. In the language of graphs, more data often narrows the generalization gap and flattens the variance-heavy right side of the validation curve. So one can fight variance not only by shrinking the model, but also by supplying more information.

For a fixed model class and the same learning procedure, this sample-size effect is mainly a variance effect, not a bias effect. Intuitively, more data make the fitted model _more stable around the same average learner_ rather than changing the structural assumptions of the learner itself. So variance often falls noticeably as sample size grows, whereas bias usually stays roughly the same unless one also changes the hypothesis class, features, or regularization.

One should also connect this to the training curve itself. As sample size increases, the empirical training error often rises slightly because the learner must fit a larger, more diverse, and more representative sample, so memorizing idiosyncrasies becomes harder. At the same time, expected generalization error often falls because the fitted model is less sample-sensitive and the empirical distribution is closer to the population distribution. These two movements together shrink the generalization gap. The broad interpretation is that with more data, training error becomes a more honest estimate of future error: the learner fits the observed sample less aggressively, but what it learns transfers better.

These three tools affect the decomposition in different ways. Cross-validation does not itself change bias or variance; it estimates which setting gives the best trade-off. Regularization usually moves the model toward higher bias and lower variance. More data usually reduces variance without requiring the model class itself to become simpler.

---

Flashcards for this section are as follows:

- why cross-validation helps with bias-variance trade-off ::@:: Cross-validation helps select model complexity or regularization strength by estimating expected generalization performance on held-out data rather than relying on training error.
- regularization effect on bias and variance: What does increasing $\lambda$ in a penalty such as training loss $+\lambda\|w\|_2^2$ usually do? ::@:: Regularization usually increases bias somewhat but decreases variance, which can improve generalization when variance was the bigger problem.
- danger of over-regularization ::@:: Too much regularization can raise bias so much that the model underfits and generalization worsens.
- effect of more data on variance ::@:: Increasing sample size usually reduces variance because the learned model fluctuates less across different sampled training sets.
- effect of more data on bias versus variance: For a fixed model class and learning rule, what usually changes when sample size increases? ::@:: For a fixed model class and the same learning procedure, increasing sample size usually reduces variance because the fitted model becomes more stable across resampled datasets, while bias remains roughly constant because the learner's structural assumptions have not changed.
- more-data graph intuition ::@:: More data often narrows the generalization gap because each noisy sample point has less influence on the fitted parameters.
- more-data effect on training error, generalization error, and gap ::@:: As sample size increases, training error often rises slightly because the model must fit a larger and more representative sample, expected generalization error often decreases because the learner becomes more stable, and the generalization gap shrinks because training performance becomes a more honest reflection of future performance.
- interpretation of the whole more-data picture ::@:: More data usually make the learner less able to memorize quirks of one sample and more able to capture repeatable structure, so training fit may look a bit worse while future performance improves and the train-test gap narrows.
- what cross-validation does and does not do ::@:: Cross-validation does not itself change bias or variance; it estimates which model complexity or regularization strength gives the best expected trade-off on held-out data.

<!-- check: ignore-next-line[header_style]: PAC is a standard acronym -->
### PAC learning viewpoint

PAC stands for _probably approximately correct_. The central idea is to replace a decomposition identity by a finite-sample guarantee. Instead of asking how expected error splits into noise, bias, and variance, PAC learning asks whether, after observing enough training examples, the learner will _probably_ output a hypothesis whose generalization error is _approximately_ small.

More concretely, one usually fixes two tolerances: an accuracy tolerance $\epsilon>0$ and a failure probability $\delta>0$. A learning procedure is PAC-style if, once the sample size is large enough, it outputs a hypothesis whose true generalization error is at most $\epsilon$ with probability at least $1-\delta$. So "approximately correct" refers to error at most $\epsilon$, and "probably" refers to confidence at least $1-\delta$.

The relation to what we have already learned is direct. Bias-variance decomposition explains _why_ generalization can be hard and which components of error are dominating; PAC learning gives a more worst-case, sample-complexity-oriented language for _when_ generalization should be expected from finite data. Model capacity matters in both viewpoints. In bias-variance language, high capacity can increase variance. In PAC language, a richer hypothesis class usually requires more samples to guarantee small generalization error. So both viewpoints say the same broad thing in different dialects: capacity, data size, and generalization are tightly linked.

PAC theory is also more guarantee-oriented than decomposition-oriented. The decomposition here is exact but specialized to squared loss in regression and is most useful diagnostically. PAC statements are usually broader but looser: they do not split error into bias and variance, but they explain why more data and smaller or better-controlled hypothesis classes improve the chance of good generalization.

---

Flashcards for this section are as follows:

- PAC meaning: What does PAC stand for, and in one sentence, what is the goal of PAC learning theory? ::@:: PAC stands for _probably approximately correct_. The goal of PAC learning is to give rigorous finite-sample guarantees: a hypothesis class is PAC-learnable if there exists an algorithm that, for any target function and any distribution over inputs, given enough samples $m$, returns with probability at least $1-\delta$ a hypothesis with generalization error at most $\epsilon$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- PAC interpretation with $\epsilon$ and $\delta$: What do "approximately correct" and "probably" mean in PAC learning? ::@:: "Approximately correct" means the learned hypothesis has generalization error at most $\epsilon$, and "probably" means this happens with probability at least $1-\delta$ once the sample size is large enough.
- PAC learning relation to bias-variance decomposition ::@:: Bias-variance decomposition explains why generalization error arises and what components dominate, whereas PAC learning gives finite-sample, worst-case-style guarantees about when a learner will probably generalize well.
- model capacity in PAC versus bias-variance language ::@:: In bias-variance language, high capacity can raise variance; in PAC language, a richer hypothesis class usually requires more samples to guarantee small generalization error.

### modern scaling-law remark

Modern large language model results provide an instructive empirical analogue of the sample-size and capacity story. Empirically, language-model loss often improves as a rough power law when one increases model size, training data, and total training compute over broad regimes. So the high-level statement "more parameters, more data, and more compute often improve performance" is broadly true as an empirical scaling-law observation.

But that statement needs two corrections. First, the relevant resource is not literally "GPU power" as a theoretical variable; it is more accurate to speak of total training compute, often measured in floating-point operations or an equivalent compute budget. Faster or larger GPU clusters matter mainly because they allow one to spend more compute or finish that compute budget sooner.

Second, model capacity is not an unconditional monotone good. The Chinchilla result argues that many large language models were undertrained: too many parameters for the amount of data they saw under a fixed compute budget. In that compute-limited regime, simply making the model larger is not always optimal. One must balance parameter count and number of training tokens. So the right statement is: scaling helps, but the optimal capacity depends on the task, the data regime, the optimization budget, and the compute constraint.

This is closely related to the ideas in this note. Increasing model size can reduce bias by making the model class more expressive. Increasing data can reduce variance and improve sample efficiency. Increasing compute can let optimization run further or support larger models and datasets. But finite-budget trade-offs remain: the best capacity is situation-dependent rather than universally "as large as possible".

---

Flashcards for this section are as follows:

- LLM scaling-law empirical claim: Is it broadly true that more parameters, data, and compute usually help LLMs? ::@:: Broadly yes: loss often follows a rough power-law improvement with model size, data, and compute. But bigger is not automatically better; the best parameter count still depends on the data and compute budget.
- GPU power versus compute in scaling-law language ::@:: The more precise variable is total training compute rather than GPU power itself; GPUs matter because they provide the hardware needed to realize a larger compute budget or shorter wall-clock time.
- Chinchilla-style correction to naive scaling: Under a fixed compute budget, what is the Chinchilla correction? ::@:: Scale parameters and training tokens together, not parameters alone. An oversized model with too little data is undertrained; matching model size to data and compute works better.
- relation between LLM scaling laws and bias-variance ideas ::@:: Larger models can reduce bias by increasing expressiveness, more data can reduce variance and improve generalization, and more compute supports larger effective training budgets; but the best capacity remains situation-dependent rather than universally maximal.

### classification remark

The classic decomposition is derived most cleanly for least-squares regression because squared loss expands quadratically, so after centering, the cross terms cancel. For zero-one classification loss, the loss is $\mathbf 1[\hat y_S(x)\neq y]$, which contains a discontinuous thresholding decision rather than a smooth square. That thresholding step is exactly what breaks the same clean algebra: one cannot simply expand an indicator into "noise + squared bias + variance" with the same cancellation trick.

This point is easier to understand operationally. In classification there are really two layers: first estimate something like a score or probability, and then convert it into a hard class label by thresholding or argmax. Small changes in predicted probabilities can leave squared probability error almost unchanged but still flip the predicted class near a decision boundary. For example, if the true class probability is $\eta(x)=0.49$, then predicted probabilities $0.48$ and $0.50$ are both very close in squared-probability terms, but one lies below the $0.5$ threshold and the other lies above it, so the induced class prediction can change abruptly. That discontinuity is why zero-one classification error does not admit the same neat decomposition.

However, if classification is phrased probabilistically, one can recover a close analogue. In binary classification, let $\eta(x)=P(Y=1\mid X=x)$ be the true class probability and let $\hat p_S(x)$ be the probability predicted by the learner trained on sample $S$. Then the expected squared probability error $\mathbb{E}_S[(\hat p_S(x)-\eta(x))^2]$ decomposes as $\bigl(\mathbb{E}_S[\hat p_S(x)]-\eta(x)\bigr)^2 + \mathbb{E}_S\bigl[(\hat p_S(x)-\mathbb{E}_S[\hat p_S(x)])^2\bigr]$, that is, squared bias plus variance for probability estimation.

So the key clarification is: in regression, the decomposition is about squared prediction error of the target itself; in classification, the closest clean analogue is usually about squared error of _probability estimates_, not about zero-one accuracy directly. The same bias-variance intuition still transfers: capacity can make probability estimates systematically wrong (bias) or highly sample-sensitive (variance). What changes is the mathematical object one decomposes.

---

Flashcards for this section are as follows:

- why the classical derivation lives in regression rather than zero-one classification ::@:: The standard derivation works in regression because squared loss is quadratic, so centering produces cross terms that can cancel; zero-one classification loss uses an indicator after thresholding or argmax, so the same algebraic expansion does not go through.
- threshold intuition for why zero-one loss resists the same decomposition ::@:: In classification, small changes in predicted probability can flip the hard class label near a decision boundary, so zero-one loss changes discontinuously even when squared probability error changes only slightly.
- probabilistic classification analogue: If $\eta(x)=P(Y=1\mid X=x)$ is the true class probability and $\hat p_S(x)$ is the learner's predicted probability, what is the decomposition of $\mathbb{E}_S[(\hat p_S(x)-\eta(x))^2]$? ::@:: One has $\mathbb{E}_S[(\hat p_S(x)-\eta(x))^2] = (\mathbb{E}_S[\hat p_S(x)]-\eta(x))^2 + \mathbb{E}_S[(\hat p_S(x)-\mathbb{E}_S[\hat p_S(x)])^2]$, so squared probability estimation error itself has a bias-variance decomposition.
- what is and is not being decomposed in classification ::@:: The clean algebra here does not decompose zero-one classification accuracy itself; the closest clean analogue usually decomposes squared error of estimated class probabilities instead.
- lesson beyond regression ::@:: Even when the exact decomposed quantity changes from target values to class probabilities, the same bias-variance intuition about systematic error and sample sensitivity still applies.

## ensemble learning

Ensemble learning means combining several predictors into one composite predictor. The individual components are often called _base learners_, meaning the individual models inside the combination. A _weak learner_ is a base learner that may be only slightly better than a trivial baseline such as random guessing, but can still be useful when combined with others. The final combined model is the _ensemble_.

The bias-variance viewpoint gives a natural motivation. If one learner is too unstable, average several of them to reduce variance. If one learner is too weak or too biased, build a stronger one by combining many simple learners strategically. This creates the conceptual split between bagging and boosting. Bagging primarily targets variance: train many models on perturbed datasets and aggregate them. Boosting primarily targets bias: train models sequentially so each new model focuses on the errors that previous models left behind.

In regression, an ensemble predictor is often an average such as $\hat f_{\mathrm{ens}}(x)=\frac{1}{B}\sum_{b=1}^B h_b(x)$. In classification, it is often a majority vote or a weighted vote, or probability averaging followed by thresholding. The key point is that the ensemble is not one monolithic learner; it is a combination of many learned components.

It is helpful to separate the mechanics from the effect. Mechanically, bagging changes the _data seen by each learner_ and then averages the answers; boosting changes the _importance of training examples across rounds_ and then adds the learners stage by stage. Effect-wise, bagging mainly makes a noisy learner more stable, while boosting mainly makes a weak learner more expressive. A good memory cue is therefore: _bagging = parallel averaging for stability_; _boosting = sequential correction for strength_.

The detailed procedures, formulas, and concrete examples are developed in the dedicated bagging and boosting subsections below to avoid repeating near-identical material at two hierarchy levels.

---

Flashcards for this section are as follows:

- what ensemble learning means ::@:: Ensemble learning means combining several base learners into one predictor so the final model can be more stable or more expressive than any single component.
- base learner versus weak learner ::@:: A base learner is one component model inside an ensemble; a weak learner is a deliberately simple base learner that may be only slightly better than a trivial baseline but can still be powerful when combined with others.
- decomposition as design guide ::@:: The bias-variance viewpoint helps diagnose whether a method needs more flexibility, more stability, or both.
- bagging versus boosting intuition ::@:: Mechanically, bagging trains learners in parallel on perturbed datasets and averages them, while boosting trains learners sequentially so each new learner corrects earlier mistakes; bagging mainly adds stability, whereas boosting mainly adds strength.

### bagging as variance reduction

Bagging stands for _bootstrap aggregating_. A _bootstrap sample_ is a dataset sampled _with replacement_ from the original training set, so some original examples may appear multiple times and others may be omitted in a given resample. If one draws $B$ bootstrap samples $S^{(1)},\ldots,S^{(B)}$, trains the same base learning algorithm on each one, and then combines the resulting predictors, one obtains a bagged model.

In regression, the usual rule is averaging: $\hat f_{\mathrm{bag}}(x)=\frac{1}{B}\sum_{b=1}^B h_{S^{(b)}}(x)$. In classification, the usual rule is majority vote or probability averaging followed by thresholding.

The intuition is easiest to phrase in words before formulas: take an unstable learner, expose it to many slightly different versions of the data, and then average away the idiosyncratic parts. Each individual learner sees a noisy view of the training set, so each produces a slightly different answer. The common signal tends to survive the averaging, while the sample-specific wiggles partly cancel.

The procedure can be written as a short recipe. (1) Draw many bootstrap samples from the training set. (2) Train the same base learner on each bootstrap sample independently. (3) Collect all predictions on a new input $x$. (4) Aggregate them by averaging for regression or by voting/probability averaging for classification. The important structural feature is that the learners are trained in parallel and combined only at the end.

The variance-reduction logic is easiest to see in the idealized independent case. If $h_1(x),\ldots,h_B(x)$ had common variance $\sigma^2$ and were independent, then $\operatorname{Var}\Bigl(\frac{1}{B}\sum_{b=1}^B h_b(x)\Bigr)=\frac{\sigma^2}{B}$. A more realistic correlated-error formula is $\operatorname{Var}\Bigl(\frac{1}{B}\sum_{b=1}^B h_b(x)\Bigr)=\rho\sigma^2 + \frac{1-\rho}{B}\sigma^2$ when the base learners share common variance $\sigma^2$ and pairwise correlation $\rho$. This formula shows two things at once: averaging helps most when the base learners are unstable _and_ not too strongly correlated.

That is why bagging is especially useful for unstable learners such as decision trees. Those learners change noticeably when the training set changes, so there is variance available to average away. If all learners made exactly the same errors, averaging would do almost nothing.

Concrete examples help fix the idea. In regression, one might bag deep decision trees for house-price prediction: one tree may split heavily on a few atypical sales, while another bootstrap sample may omit some of those sales and split differently. Averaging many trees produces a smoother and more stable price estimate. In classification, one might bag trees for medical diagnosis or spam filtering: each tree may overreact to particular cases, but majority vote is less erratic than any single tree.

The everyday survey analogy captures the same idea. If one repeats a noisy estimation procedure many times and averages the answers, the final answer fluctuates less than any single run.

---

Flashcards for this section are as follows:

- bootstrap sample in bagging: What is it? ::@:: A bootstrap sample is drawn with replacement from the original training set, so some examples can appear multiple times while others may be absent in a given resample.
- bagging regression formula: If bootstrap samples are $S^{(1)},\ldots,S^{(B)}$, what is $\hat f_{\mathrm{bag}}(x)$? ::@:: In regression, bagging forms the ensemble prediction $\hat f_{\mathrm{bag}}(x)=\frac{1}{B}\sum_{b=1}^B h_{S^{(b)}}(x)$ by averaging predictions from models trained on bootstrap samples.
- bagging prediction rule in classification ::@:: In classification, bagging usually combines models by majority vote or by averaging class probabilities and then predicting the largest or thresholded probability.
- bagging intuition in words ::@:: Bagging takes an unstable learner, trains it on many slightly different bootstrap versions of the data, and averages the resulting predictions so sample-specific quirks partly cancel while common signal remains.
- bagging procedure steps ::@:: A standard bagging workflow is: (1) draw many bootstrap samples, (2) train the same base learner on each sample independently, (3) evaluate all learners on a new input, and (4) aggregate by averaging, voting, or probability averaging.
- idealized variance reduction in bagging: If $B$ base predictions are independent and each has variance $\sigma^2$, what is the variance of their average? ::@:: If $B$ base predictions were independent and each had variance $\sigma^2$, then averaging them would give variance $\sigma^2/B$, which shows why aggregation reduces instability.
- correlated-error variance formula for bagging: If common variance is $\sigma^2$ and pairwise correlation is $\rho$, what is $\operatorname{Var}(\frac{1}{B}\sum_{b=1}^B h_b)$? ::@:: If bagged base learners have common variance $\sigma^2$ and pairwise correlation $\rho$, then $\operatorname{Var}(\frac{1}{B}\sum_{b=1}^B h_b)=\rho\sigma^2+\frac{1-\rho}{B}\sigma^2$, so bagging helps most when base learners are unstable but not too strongly correlated.
- bagging tax-survey analogy ::@:: Bagging is like repeating a noisy survey-based estimate many times and averaging the answers so the final estimate fluctuates less.
- when bagging is most useful ::@:: Bagging is most useful for unstable base learners whose predictions vary noticeably across resampled datasets.
- concrete bagging examples ::@:: Typical bagging examples are averaging many decision trees for house-price regression or using majority vote across many trees for classification tasks such as spam filtering or diagnosis.

### boosting as bias reduction

Boosting takes the opposite strategy from bagging. Instead of training many learners independently on perturbed datasets, it trains learners _sequentially_. The current ensemble is built one stage at a time, and each new learner is chosen to focus on what the existing ensemble still gets wrong.

In the common weighted-example view, boosting begins with equal weights on the training examples and a chosen base learning algorithm. After each round, examples that were misclassified or poorly fitted receive more weight, so the next learner is forced to focus on those hard cases. After several rounds, the final predictor is a weighted combination such as $F_T(x)=\sum_{t=1}^T \alpha_t h_t(x)$, with final classification often given by $\operatorname{sign}(F_T(x))$ in binary problems.

The core intuition is corrective rather than averaging-based. A weak learner may get the easy cases right and miss the hard cases. Boosting then tells the next learner: spend more effort where the current ensemble is still bad. Repeating this stagewise correction builds a decision rule that can represent patterns no single weak learner could capture alone. A good memory cue is: _bagging asks many noisy experts and averages them_; _boosting trains one new expert to fix the current committee's mistakes_.

The procedure can also be summarized as a short recipe. (1) Start with equal example weights, or equivalently start with residuals defined by the current weak ensemble. (2) Train a weak learner on the current weighted data or residual signal. (3) Give that learner a coefficient showing how much it should influence the ensemble. (4) Update the example weights or residuals so the next learner focuses on what is still wrong. (5) Repeat for several rounds and add all learners into one stagewise model.

This strategy primarily combats bias because it progressively builds a richer decision rule from simpler pieces. A weak learner by itself may be only slightly better than naive guessing, but stagewise combination can turn many such weak rules into one strong rule. In AdaBoost the emphasis shift is implemented by changing example weights. In gradient boosting the new learner is trained to fit the residual or negative gradient left by the current ensemble. XGBoost is an efficient regularized implementation of gradient-boosted trees.

Concrete examples are helpful here too. In AdaBoost for binary classification, the base learners are often decision stumps, each of which makes only one simple split. Any one stump is weak, but a weighted sum of many stumps can carve out a much more accurate classifier. In gradient boosting for regression, one might predict house prices by fitting a shallow tree to residual errors after each round; each new tree corrects what the previous ensemble still misses. XGBoost is a widely used industrial-strength implementation of this stagewise residual-fitting idea.

There is an important caveat: although boosting is often described as bias reduction, aggressive boosting can also overfit if allowed to chase noise too strongly. So the decomposition gives guidance, not an excuse to boost forever.

---

Flashcards for this section are as follows:

- initial weighting in boosting ::@:: Boosting typically begins by assigning equal weights to all training examples before any learner is trained.
- why weights are increased on mistakes ::@:: Boosting raises the weights of misclassified or poorly fitted examples so later learners focus on cases the current ensemble still handles badly.
- final form of a boosting model: What does a stagewise additive model $F_T(x)$ look like? ::@:: A boosting model is a weighted combination such as $F_T(x)=\sum_{t=1}^T \alpha_t h_t(x)$ of a sequence of base learners trained in successive rounds.
- what a weak learner means in boosting ::@:: A weak learner is a base learner that may be only slightly better than naive guessing, but boosting can combine many such learners into a strong ensemble.
- boosting intuition in words ::@:: Boosting works sequentially: after one learner makes mistakes, the next learner is pushed to focus on those hard cases, so the ensemble gradually corrects its own residual errors and becomes stronger.
- boosting procedure steps ::@:: A standard boosting workflow is: (1) initialize equal example weights or residuals, (2) train a weak learner, (3) assign it a stage weight, (4) update weights or residuals to emphasize current mistakes, and (5) repeat to build a stagewise additive model.
- examples of boosting methods with meanings ::@:: AdaBoost reweights examples to emphasize mistakes, gradient boosting fits new learners to residuals or negative gradients left by the current ensemble, and XGBoost is an efficient regularized implementation of gradient-boosted trees.
- concrete boosting examples ::@:: Typical boosting examples are AdaBoost combining many decision stumps for binary classification and gradient-boosted trees that successively fit residuals for tabular regression or classification.
- boosting caveat ::@:: Although boosting is often used to reduce bias, excessive boosting can still overfit if the ensemble is allowed to chase noise too aggressively.
