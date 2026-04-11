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

The bias-variance decomposition explains why model selection is difficult even when overfitting is already understood informally. Generalization error is not a single monolithic quantity: under squared-error regression, the expected prediction error can be split into terms that reflect systematic misspecification, sensitivity to the random training set, and irreducible randomness in the data-generating process. In compact form, expected squared test error becomes _noise + squared bias + variance_.

This decomposition provides the conceptual bridge from linear models to regularization, cross-validation, bagging, and boosting. It gives precise mathematical content to statements like "this model is too rigid" or "this model is too unstable": the first corresponds to high bias and the second to high variance. Instead of saying only that a model underfits or overfits, one can ask which source of error is dominating and then choose a remedy that targets that source.

It also reframes model selection more carefully. Training error almost always decreases as model capacity increases, but expected future error does not. The reason is that increasing capacity usually lowers bias and raises variance at the same time. The best model is therefore the one that balances these competing forces rather than the one that merely fits the observed sample most aggressively. In that sense, the decomposition is not only a theorem about squared error; it is also a design guide for choosing capacity, regularization strength, sample size strategy, and ensemble method.

---

Flashcards for this section are as follows:

- overview with formula ::@:: Under squared-error regression, the bias-variance decomposition writes expected prediction error as _noise + squared bias + variance_, separating irreducible randomness from the two error sources controlled by model choice. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- two main controllable sources ::@:: In the decomposition, bias reflects systematic misspecification and variance reflects sensitivity to the random training set, while the noise term is irreducible. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- why this decomposition matters for model selection ::@:: This decomposition explains why the best model is not the one with lowest training error, but the one with the best balance between bias and variance. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- design-guide interpretation ::@:: The decomposition acts as a design guide: high bias suggests more expressive models or weaker regularization, whereas high variance suggests simpler models, stronger regularization, more data, or variance-reduction methods such as bagging. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## bias and variance intuition

Bias and variance are properties of a _learning procedure_, not just of one fitted model. Imagine repeatedly drawing a fresh training set from the same population, fitting the same algorithm each time, and then evaluating the resulting predictor on future data. If the procedure performs poorly on most such repetitions, it has high bias. If its performance changes drastically from one repetition to another, it has high variance.

This distinction matches the familiar underfitting-versus-overfitting story, but it is more precise. A low-capacity model class usually has relatively few parameters and limited expressive power. Because it cannot bend enough to follow the real signal, different random training sets often produce similarly shaped predictors, so variance is low; but those predictors are systematically wrong, so bias is high. A high-capacity model class usually has more parameters and much greater expressive power. That flexibility lowers systematic misspecification, but when the number of effective parameters is large relative to available data, small random changes in the sampled points can change the fitted parameters a great deal. Then variance is high.

There are two especially useful intuition lenses. __Expressive-power view__: low capacity means the hypothesis class cannot represent many shapes, so the fitted predictor is forced to stay too simple even when the truth is more complicated; high capacity means the class can represent many shapes, so it can track the signal more closely. __Parameter-sensitivity view__: low capacity usually means fewer adjustable parameters, so sample noise does not move the fitted coefficients very far; high capacity usually means many parameters, so if data are few relative to parameter count, noise can change the estimated parameters substantially.

These are two descriptions of the same trade-off. High bias means the average learned predictor is systematically wrong because the model family is too restrictive. High variance means the procedure is too sensitive: changing the sampled dataset changes the fitted parameters and hence the fitted predictor substantially. The most memorable phrasing is therefore: high bias means _poor performance on most occasions_, while high variance means _different performance on different occasions_.

---

Flashcards for this section are as follows:

- high bias intuition ::@:: High bias means the learning procedure performs poorly on most training samples because its assumptions are systematically too restrictive or mismatched, so even the average fitted predictor is wrong. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- high variance intuition ::@:: High variance means the learned model changes too much across different training samples because it is overly sensitive to data fluctuations. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- underfitting and bias ::@:: Underfitting is typically associated with high bias because the model family is too simple to capture the signal. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- overfitting and variance ::@:: Overfitting is typically associated with high variance because the model adapts too strongly to accidental quirks in the training sample. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- low capacity as limited expressive power ::@:: Low model capacity means the hypothesis class has limited expressive power, so even the best-fit predictor may be systematically too simple to match the true signal. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- high capacity as parameter sensitivity ::@:: High model capacity usually means many adjustable parameters or degrees of freedom, so when data are limited relative to parameter count, small sample noise can move the fitted parameters substantially and create high variance. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- two complementary views of capacity ::@:: The same bias-variance trade-off can be read as an expressive-power story (what shapes the model class can represent) and as a parameter-sensitivity story (how strongly random data perturb the fitted coefficients). <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- why the trade-off is hard ::@:: Reducing bias often requires a richer model class, but richer models can increase variance. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- memorable operational wording ::@:: A useful memory cue is: high bias means poor performance on most occasions, while high variance means different performance on different occasions. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### random training sets, empirical error, and generalization gap

To formalize these ideas, fix the notation carefully. The population distribution over input-target pairs is $\mathcal D$, so a fresh example means a random draw $(X,Y)\sim\mathcal D$. A training set of size $m$ is $S=\{(x_i,y_i)\}_{i=1}^m\sim \mathcal D^m$, meaning that the $m$ examples are sampled independently from $\mathcal D$ and the superscript $m$ denotes the product distribution. A hypothesis or predictor is a function $h\colon x\mapsto h(x)$. In the linear-model notation used elsewhere in this course, this is often just shorthand for $h_w(x)=w^\top\phi(x)$ after choosing a parameter vector $w$, so the hypothesis class is $\mathcal H=\{x\mapsto w^\top\phi(x):w\in\mathbb R^d\}$. When a learning algorithm is trained on the particular sample $S$, the resulting fitted predictor is denoted by $h_S$; the subscript reminds us that training-set randomness makes the fitted predictor itself random.

For any fixed hypothesis $h$, the empirical squared-error loss on sample $S$ is $\hat\epsilon_S(h)=\frac{1}{m}\sum_{i=1}^m (y_i-h(x_i))^2$, while the population or generalization error is $\epsilon(h)=\mathbb{E}_{(x,y)\sim\mathcal D}[(y-h(x))^2]$. The first quantity averages over the finite training sample, whereas the second averages over the full data-generating distribution. Applying this to the learned predictor gives the random quantity $\epsilon(h_S)=\mathbb{E}_{(x,y)\sim\mathcal D}[(y-h_S(x))^2]$.

Because $S$ is random, the learned function $h_S$ is random, so the empirical error $\hat\epsilon_S(h_S)$ and the generalization error $\epsilon(h_S)$ are random as well. Define the sample-specific random variable $\operatorname{Gap}(S)=\epsilon(h_S)-\hat\epsilon_S(h_S)$, called the _generalization gap_ for that particular training set. It measures how much worse the learned predictor performs on the population than on the sample it was trained on.

Course materials also distinguish this random one-run gap from its average over repeated resampling. The _expected generalization gap_ is $\operatorname{Gap}_{\mathrm{exp}}=\mathbb{E}_S[\operatorname{Gap}(S)]=\mathbb{E}_S[\epsilon(h_S)-\hat\epsilon_S(h_S)]$. Intuitively, $\operatorname{Gap}(S)$ is the single-experiment optimism penalty (one train/test split), whereas $\operatorname{Gap}_{\mathrm{exp}}$ is the long-run average optimism of the learning procedure across many possible training sets.

Equivalently, $\mathbb{E}_S[\epsilon(h_S)] = \mathbb{E}_S[\hat\epsilon_S(h_S)] + \operatorname{Gap}_{\mathrm{exp}}$. So expected test error equals expected training error plus expected generalization gap.

This point is easy to miss when one trains a model only once. The central object is not merely one fitted function, but a random procedure $S\mapsto h_S$ that maps random samples to predictors. Bias and variance are properties of that random procedure, not of one frozen fitted model viewed in isolation.

---

Flashcards for this section are as follows:

- notation $\mathcal D$ and $S\sim\mathcal D^m$: What do these symbols mean? ::@:: Here $\mathcal D$ is the population distribution over input-target pairs $(X,Y)$, and $S\sim\mathcal D^m$ means the training set $S=\{(x_i,y_i)\}_{i=1}^m$ contains $m$ independent draws from that distribution. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- learned hypothesis $h_S$ ::@:: The notation $h_S$ means the learned predictor depends on the particular training set $S$ used for learning, so it is a random function when $S$ is random. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- linear-model meaning of hypothesis notation: In this course, how should one interpret $h(x)$ in a linear-feature model? ::@:: In the linear-feature setting, $h(x)$ is often just shorthand for $h_w(x)=w^\top\phi(x)$ after choosing parameters $w$, and the hypothesis class is $\mathcal H=\{x\mapsto w^\top\phi(x):w\in\mathbb R^d\}$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- empirical squared-error notation: For a hypothesis $h$ and training set $S=\{(x_i,y_i)\}_{i=1}^m$, what is $\hat\epsilon_S(h)$? ::@:: The empirical squared error is $\hat\epsilon_S(h)=\frac{1}{m}\sum_{i=1}^m (y_i-h(x_i))^2$, a finite-sample average over the training set. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- generalization error notation: For a hypothesis $h$, what are $\epsilon(h)$ and $\epsilon(h_S)$? ::@:: The population or generalization error is $\epsilon(h)=\mathbb{E}_{(x,y)\sim\mathcal D}[(y-h(x))^2]$; for the learned predictor this becomes $\epsilon(h_S)$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- sample-specific generalization gap notation: For a training set $S$, what is $\operatorname{Gap}(S)$? ::@:: The sample-specific generalization gap is $\operatorname{Gap}(S)=\epsilon(h_S)-\hat\epsilon_S(h_S)$, the amount by which population error exceeds training error for the predictor trained on that same $S$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- expected generalization gap notation: What is $\operatorname{Gap}_{\mathrm{exp}}$? ::@:: The expected generalization gap is $\operatorname{Gap}_{\mathrm{exp}}=\mathbb{E}_S[\operatorname{Gap}(S)]=\mathbb{E}_S[\epsilon(h_S)-\hat\epsilon_S(h_S)]$, the average optimism penalty over repeated random training sets. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- expected-gap identity: How are $\mathbb{E}_S[\epsilon(h_S)]$, $\mathbb{E}_S[\hat\epsilon_S(h_S)]$, and $\operatorname{Gap}_{\mathrm{exp}}$ related? ::@:: They satisfy $\mathbb{E}_S[\epsilon(h_S)] = \mathbb{E}_S[\hat\epsilon_S(h_S)] + \operatorname{Gap}_{\mathrm{exp}}$, so expected test error equals expected training error plus expected generalization gap. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- why $\epsilon(h_S)$ is random ::@:: Generalization error is random because the fitted predictor $h_S$ depends on the random training set. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## decomposition of expected squared error

The formal derivation studies expected test error over the randomness of the training set. Define $\epsilon = \mathbb{E}_S\mathbb{E}_{(X,Y)\sim \mathcal D}[(Y-h_S(X))^2]$, where the outer expectation averages over all possible training sets and the inner expectation averages over a fresh test example from the population. This is different from the expected generalization gap $\operatorname{Gap}_{\mathrm{exp}}=\mathbb{E}_S[\epsilon(h_S)-\hat\epsilon_S(h_S)]$: the decomposition below expands $\mathbb{E}_S[\epsilon(h_S)]$, and $\operatorname{Gap}_{\mathrm{exp}}$ is obtained by subtracting $\mathbb{E}_S[\hat\epsilon_S(h_S)]$ afterward. It is helpful to first freeze the input value $x$ and study the pointwise quantity $\operatorname{Err}(x)=\mathbb{E}_S\mathbb{E}_{Y\mid X=x}[(Y-h_S(x))^2]$.

Now define the average predictor $\bar h(x)=\mathbb{E}_S[h_S(x)]$ and the target mean function $f^{\ast}(x)=\mathbb{E}[Y\mid X=x]$. The key trick is to add and subtract $\bar h(x)$ inside the square, writing $Y-h_S(x)=\bigl(Y-\bar h(x)\bigr)+\bigl(\bar h(x)-h_S(x)\bigr)$. After squaring and taking expectation, the result becomes $\operatorname{Err}(x)=\mathbb{E}_{S,Y\mid x}\bigl[(Y-\bar h(x))^2\bigr] + 2\mathbb{E}_{S,Y\mid x}\bigl[(Y-\bar h(x))(\bar h(x)-h_S(x))\bigr] + \mathbb{E}_{S,Y\mid x}\bigl[(\bar h(x)-h_S(x))^2\bigr]$.

The middle term vanishes, so one gets the coarse two-part expression $\operatorname{Err}(x)=\mathbb{E}_{Y\mid x}[(Y-\bar h(x))^2] + \mathbb{E}_S[(h_S(x)-\bar h(x))^2]$. The second term is already the variance term: it measures how much the learned predictor fluctuates around its average when the training set changes.

To refine the first term further, add and subtract the target mean function $f^{\ast}(x)$: $Y-\bar h(x)=\bigl(Y-f^{\ast}(x)\bigr)+\bigl(f^{\ast}(x)-\bar h(x)\bigr)$. Squaring and averaging again yields $\mathbb{E}_{Y\mid x}[(Y-\bar h(x))^2]=\mathbb{E}_{Y\mid x}[(Y-f^{\ast}(x))^2] + (\bar h(x)-f^{\ast}(x))^2$, because the corresponding cross term is zero.

Therefore the full pointwise decomposition is $\operatorname{Err}(x)=\underbrace{\mathbb{E}_{Y\mid x}[(Y-f^{\ast}(x))^2]}_{\text{noise at }x} + \underbrace{(\bar h(x)-f^{\ast}(x))^2}_{\text{squared bias at }x} + \underbrace{\mathbb{E}_S[(h_S(x)-\bar h(x))^2]}_{\text{variance at }x}$. Since $f^{\ast}(x)=\mathbb{E}[Y\mid X=x]$, the first term is exactly $\operatorname{Var}(Y\mid X=x)$.

Finally, average over the input distribution to obtain the global decomposition $\epsilon = \mathbb{E}_X\bigl[\operatorname{Var}(Y\mid X)\bigr] + \mathbb{E}_X[(\bar h(X)-f^{\ast}(X))^2] + \mathbb{E}_X\mathbb{E}_S[(h_S(X)-\bar h(X))^2]$.

This formula has a complete interpretation. The noise term is the irreducible uncertainty already present in the target even if the true regression function were known exactly. The squared-bias term measures how far the _average_ learned predictor sits from the true regression function. The variance term measures how much the fitted predictor changes when the training set changes. Only the last two are directly controllable by model choice, regularization, or data usage.

---

Flashcards for this section are as follows:

- average predictor $\bar h(x)$: What is it? ::@:: The average predictor is $\bar h(x)=\mathbb{E}_S[h_S(x)]$, the mean prediction obtained by averaging the learned predictor over all possible training sets. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- target mean function $f^*(x)$: What is it? ::@:: The target mean function is $f^*(x)=\mathbb{E}[Y\mid X=x]$, the regression function that gives the conditional mean target at input $x$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- expected test error over random training sets: What quantity is decomposed when $\epsilon=\mathbb{E}_S\mathbb{E}_{(X,Y)\sim\mathcal D}[(Y-h_S(X))^2]$? ::@:: The decomposition studies $\epsilon=\mathbb{E}_S\mathbb{E}_{(X,Y)\sim\mathcal D}[(Y-h_S(X))^2]$, meaning average test error over both training-set randomness and a fresh test example. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- full pointwise bias-variance-noise decomposition: For fixed input $x$, what is $\mathbb{E}_{S,Y\mid x}[(Y-h_S(x))^2]$? ::@:: For fixed input $x$, the expected squared error is $\mathbb{E}_{S,Y\mid x}[(Y-h_S(x))^2]=\mathbb{E}_{Y\mid x}[(Y-f^*(x))^2]+(\bar h(x)-f^*(x))^2+\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$, i.e. noise + squared bias + variance. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- full interpretation of the decomposition: Interpret $\mathbb{E}_{Y\mid x}[(Y-f^*(x))^2]$, $(\bar h(x)-f^*(x))^2$, and $\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$ ::@:: In the decomposition, $\mathbb{E}_{Y\mid x}[(Y-f^*(x))^2]=\operatorname{Var}(Y\mid X=x)$ is irreducible noise, $(\bar h(x)-f^*(x))^2$ is squared bias of the average learner, and $\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$ is variance across training sets; only bias and variance are directly controlled by model choice. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- squared bias term $(\bar h(x)-f^*(x))^2$: What does it measure? ::@:: The squared bias at input $x$ is $(\bar h(x)-f^*(x))^2$, the squared distance between the average learned predictor and the true regression function. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- variance term $\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$: What does it measure? ::@:: The variance term is $\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$, which measures how much the learned predictor fluctuates across training sets. <!--SR:!2026-04-12,4,270!2026-04-11,3,250-->
- irreducible noise term $\mathbb{E}_{Y\mid x}[(Y-f^*(x))^2]=\operatorname{Var}(Y\mid X=x)$ ::@:: This noise term is randomness already present in the target given the input, so it cannot be removed even by an ideal learner. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- why training error can mislead ::@:: A model can have low training error yet poor generalization if the variance term is large. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### algebra of the decomposition

The algebra is easiest to follow if we name intermediate pieces explicitly. Start from $Y-h_S(x)=\bigl(Y-\bar h(x)\bigr)+\bigl(\bar h(x)-h_S(x)\bigr)$, where $\bar h(x)=\mathbb{E}_S[h_S(x)]$. After squaring and taking $\mathbb{E}_{S,Y\mid x}$, define $A(x)=\mathbb{E}_{Y\mid x}[(Y-\bar h(x))^2]$, $V(x)=\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$, and $C_1(x)=\mathbb{E}_{S,Y\mid x}[(Y-\bar h(x))(\bar h(x)-h_S(x))]$. Then $\operatorname{Err}(x)=A(x)+2C_1(x)+V(x)$.

Now cancel the first cross term in three short steps. First, condition on $S$: $C_1(x)=\mathbb{E}_S[(\bar h(x)-h_S(x))\mathbb{E}_{Y\mid x}[Y-\bar h(x)]]$. Second, use $f^*(x)=\mathbb{E}[Y\mid X=x]$ to get $\mathbb{E}_{Y\mid x}[Y-\bar h(x)]=f^*(x)-\bar h(x)$. Third, pull out the constant and center over $S$: $C_1(x)=(f^*(x)-\bar h(x))\mathbb{E}_S[\bar h(x)-h_S(x)]=(f^*(x)-\bar h(x))(\bar h(x)-\mathbb{E}_S[h_S(x)])=0$. So $\operatorname{Err}(x)=A(x)+V(x)$.

Next refine $A(x)$ by centering at $f^*(x)$: write $Y-\bar h(x)=\bigl(Y-f^*(x)\bigr)+\bigl(f^*(x)-\bar h(x)\bigr)$. After squaring and taking $\mathbb{E}_{Y\mid x}$, define $C_2(x)=\mathbb{E}_{Y\mid x}[(Y-f^*(x))(f^*(x)-\bar h(x))]$. Then $A(x)=\mathbb{E}_{Y\mid x}[(Y-f^*(x))^2]+2C_2(x)+(f^*(x)-\bar h(x))^2$. Since $f^*(x)-\bar h(x)$ is constant with respect to $Y$, one has $C_2(x)=(f^*(x)-\bar h(x))\mathbb{E}_{Y\mid x}[Y-f^*(x)]=0$.

Substituting back gives $\operatorname{Err}(x)=\mathbb{E}_{Y\mid x}[(Y-f^*(x))^2]+(\bar h(x)-f^*(x))^2+\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$. The proof is therefore a _double-centering argument_: center once around $\bar h(x)$ (learner randomness) and once around $f^*(x)$ (target randomness), and both cross terms vanish because each centered term has zero mean.

---

Flashcards for this section are as follows:

- algebra roadmap at fixed $x$: If $A(x)=\mathbb{E}_{Y\mid x}[(Y-\bar h(x))^2]$, $V(x)=\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$, and $C_1(x)=\mathbb{E}_{S,Y\mid x}[(Y-\bar h(x))(\bar h(x)-h_S(x))]$, how does $\operatorname{Err}(x)=\mathbb{E}_{S,Y\mid x}[(Y-h_S(x))^2]$ expand? ::@:: The first expansion is $\operatorname{Err}(x)=A(x)+2C_1(x)+V(x)$, obtained by adding and subtracting $\bar h(x)$ inside $Y-h_S(x)$. <!--SR:!2026-04-12,4,270!2026-04-11,3,250-->
- first cross-term cancellation in three steps: Why is $C_1(x)=0$? ::@:: Because $h_S(x)$ depends on $S$ but not on fresh $Y\mid X=x$, one gets $C_1(x)=\mathbb{E}_S[(\bar h(x)-h_S(x))\mathbb{E}_{Y\mid x}[Y-\bar h(x)]]=(f^*(x)-\bar h(x))\mathbb{E}_S[\bar h(x)-h_S(x)]$, and $\mathbb{E}_S[\bar h(x)-h_S(x)]=\bar h(x)-\mathbb{E}_S[h_S(x)]=0$. <!--SR:!2026-04-09,1,230!2026-04-12,4,270-->
- second centering definition: If $C_2(x)=\mathbb{E}_{Y\mid x}[(Y-f^*(x))(f^*(x)-\bar h(x))]$, how does $A(x)=\mathbb{E}_{Y\mid x}[(Y-\bar h(x))^2]$ expand? ::@:: The second expansion is $A(x)=\mathbb{E}_{Y\mid x}[(Y-f^*(x))^2]+2C_2(x)+(f^*(x)-\bar h(x))^2$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- second cross-term cancellation: Why is $C_2(x)=0$? ::@:: Since $f^*(x)-\bar h(x)$ is constant with respect to $Y$, one has $C_2(x)=(f^*(x)-\bar h(x))\mathbb{E}_{Y\mid x}[Y-f^*(x)]$, and $\mathbb{E}_{Y\mid x}[Y-f^*(x)]=0$ by definition of $f^*(x)=\mathbb{E}[Y\mid X=x]$. <!--SR:!2026-04-11,3,250!2026-04-11,3,250-->
- final pointwise decomposition from the two cancellations: What is $\operatorname{Err}(x)$ after using $C_1(x)=C_2(x)=0$? ::@:: One gets $\operatorname{Err}(x)=\mathbb{E}_{Y\mid x}[(Y-f^*(x))^2]+(\bar h(x)-f^*(x))^2+\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$, i.e. noise + squared bias + variance. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- double-centering intuition with explicit setup: In deriving $\operatorname{Err}(x)=\mathbb{E}_{S,Y\mid x}[(Y-h_S(x))^2]$ using centers $\bar h(x)=\mathbb{E}_S[h_S(x)]$ and $f^*(x)=\mathbb{E}[Y\mid X=x]$, why do both cross terms vanish? ::@:: The proof works by centering once around $\bar h(x)$ to isolate learner fluctuations and once around $f^*(x)$ to isolate target noise; each cross term then vanishes because centered terms have zero mean. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### two-term view and refined three-term view

There are two equivalent presentations of the same identity; introducing names makes the relation clearer. For fixed $x$, define $T(x)=\mathbb{E}_{Y\mid x}[(Y-\bar h(x))^2]$ (target-side dispersion around the average predictor), $N(x)=\mathbb{E}_{Y\mid x}[(Y-f^*(x))^2]$ (noise), $B^2(x)=(\bar h(x)-f^*(x))^2$ (squared bias), and $V(x)=\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$ (variance).

With this notation, the coarse two-term view is $\operatorname{Err}(x)=T(x)+V(x)$. The refined three-term view is $\operatorname{Err}(x)=N(x)+B^2(x)+V(x)$. The bridge between them is exactly $T(x)=N(x)+B^2(x)$, so the two-term formula is just the three-term formula with the first two terms grouped.

This grouping interpretation is important conceptually. In the two-term view, $T(x)$ answers "how far are outcomes and the average learner from each other on the target side?", while $V(x)$ answers "how unstable is the learner across training sets?". In the refined three-term view, $T(x)$ is unpacked into an irreducible part $N(x)$ and a controllable part $B^2(x)$.

Global forms are obtained by averaging over $X$. The coarse global form is $\mathbb{E}_{X,S,Y}[(Y-h_S(X))^2]=\mathbb{E}_X[T(X)]+\mathbb{E}_X[V(X)]$, while the refined global form is $\mathbb{E}_{X,S,Y}[(Y-h_S(X))^2]=\mathbb{E}_X[N(X)]+\mathbb{E}_X[B^2(X)]+\mathbb{E}_X[V(X)]$.

So the formulas are mathematically identical but pedagogically different: use the two-term view for a quick "target-side error versus learner instability" summary, and use the three-term view when you need to separate irreducible noise from controllable bias.

In words, the coarse two-term decomposition says: _expected generalization error = target-side error around the average learner + variance from training-set randomness_. The refined three-term decomposition says: _expected generalization error = irreducible noise + squared bias + variance_. The refined form is therefore just the coarse form with the first broad target-side term split into its unavoidable part and its controllable systematic-error part.

---

Flashcards for this section are as follows:

- notation map for the two views: If $T(x)=\mathbb{E}_{Y\mid x}[(Y-\bar h(x))^2]$, $N(x)=\mathbb{E}_{Y\mid x}[(Y-f^*(x))^2]$, $B^2(x)=(\bar h(x)-f^*(x))^2$, and $V(x)=\mathbb{E}_S[(h_S(x)-\bar h(x))^2]$, what are the two equivalent pointwise decompositions of $\operatorname{Err}(x)$? ::@:: They are $\operatorname{Err}(x)=T(x)+V(x)$ (coarse two-term) and $\operatorname{Err}(x)=N(x)+B^2(x)+V(x)$ (refined three-term). <!--SR:!2026-04-08,1,230!2026-04-12,4,270-->
- exact bridge identity between the two views: How are $T(x)$, $N(x)$, and $B^2(x)$ related? ::@:: The bridge is $T(x)=N(x)+B^2(x)$, i.e. target-side error around $\bar h(x)$ equals irreducible noise plus squared bias. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- global two-term decomposition with named pieces: Using $T(X)$ and $V(X)$, what is $\mathbb{E}_{X,S,Y}[(Y-h_S(X))^2]$? ::@:: The coarse global view is $\mathbb{E}_{X,S,Y}[(Y-h_S(X))^2]=\mathbb{E}_X[T(X)]+\mathbb{E}_X[V(X)]$. <!--SR:!2026-04-11,3,250!2026-04-11,3,250-->
- global refined decomposition with named pieces: Using $N(X)$, $B^2(X)$, and $V(X)$, what is $\mathbb{E}_{X,S,Y}[(Y-h_S(X))^2]$? ::@:: The refined global view is $\mathbb{E}_{X,S,Y}[(Y-h_S(X))^2]=\mathbb{E}_X[N(X)]+\mathbb{E}_X[B^2(X)]+\mathbb{E}_X[V(X)]$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- expected generalization error in words from the two-term view ::@:: In words, the coarse two-term view says expected generalization error equals target-side error around the average learner plus variance from training-set randomness. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- expected generalization error in words from the refined three-term view ::@:: In words, the refined three-term view says expected generalization error equals irreducible noise plus squared bias plus variance. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- when to use two-term versus refined three-term view ::@:: Use the two-term view for a quick summary of target-side error versus learner instability; use the refined three-term view when you need to separate irreducible noise from controllable squared bias. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## illustrations with model capacity

The standard visual illustration uses polynomial regression on repeatedly resampled datasets from a smooth target curve. Imagine a graph with three ingredients: a smooth true function, a cloud of noisy sampled points around it, and many fitted curves obtained by repeatedly drawing a training set and fitting a polynomial of fixed degree $d$. Looking across many such fits reveals whether the learning procedure is mainly biased or mainly variable.

Model capacity is closely tied to both expressive power and parameter count. In one variable, a degree-$d$ polynomial has $d+1$ coefficients, so increasing $d$ increases the number of adjustable parameters. Low capacity means fewer parameters and limited expressive power: the model cannot represent many shapes. High capacity means more parameters and much richer expressive power: the model can represent many shapes, but when data are limited relative to parameter count, random noise in the sampled points can move those parameters substantially.

This is the key capacity intuition. If parameter count is small relative to data size, each noisy observation has limited leverage on the fit, so different random samples often produce similar fitted parameters. If parameter count is large relative to data size, many different parameter settings can fit the observed sample well, so sample noise can push the fitted coefficients in noticeably different directions.

For example, if $d=0$, the model class contains only constant functions. Different sampled training sets lead to broadly similar fitted functions, so variance is low, but the average fit is far from the true nonlinear curve, so bias is high. If $d=1$, the model can tilt but still cannot bend, so bias remains substantial on a curved truth. If $d=9$, the story flips: the class is expressive enough to approximate the underlying curve closely, but because it has many coefficients relative to the available data, the fitted curve changes dramatically from one random sample to another, so variance is high.

An intermediate choice such as $d=3$ gives the best compromise in the classic picture. It is flexible enough to track the broad trend but not so flexible that every noisy point can twist the parameters strongly. This is the visual origin of the U-shaped validation/test-error curve: as capacity increases, bias tends to decrease, variance tends to increase, and the best generalization performance occurs somewhere in between.

---

Flashcards for this section are as follows:

- polynomial illustration of bias and variance ::@:: In the polynomial-regression picture, low-degree models show high bias and low variance, while high-degree models show low bias and high variance. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- model capacity and parameter count: In one-variable polynomial regression, how many coefficients does a degree-$d$ model have? ::@:: A degree-$d$ model has $d+1$ coefficients, so increasing model capacity also increases the number of adjustable parameters. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- low capacity versus high capacity intuition ::@:: Low capacity means limited expressive power and relatively few parameters, so the model is stable but can be systematically wrong; high capacity means rich expressive power and many parameters, so the model can match the signal better but also becomes more sensitive to sample noise. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- why parameter count relative to data matters ::@:: When parameter count is large relative to data size, many coefficient settings can fit the sample well, so random noise can move the fitted parameters strongly and produce high variance. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- why test error is U-shaped ::@:: As model capacity increases, bias typically falls while variance rises, so generalization error often first decreases and then increases. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- best capacity choice ::@:: The best model complexity is the one that minimizes expected generalization error, not necessarily the one that minimizes training error. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- role of random noise in overfitting ::@:: A high-variance model can start fitting random noise in the sampled targets instead of the underlying signal. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### low-degree, high-degree, and intermediate fits

The low-degree case illustrates bias dominance. Because the hypothesis class is too rigid, even the average of many fitted models remains systematically wrong. The fitted parameters do not move much from one dataset to another, but that stability is not a virtue by itself: the model is stable because it cannot express the needed shape. It is _stable but wrong_.

The high-degree case illustrates variance dominance. Each individual training set can be fit extremely closely, and the average predictor may be near the truth, but the individual fitted curves vary wildly across training samples. This happens because the model has many adjustable coefficients, and when the sample is noisy or small relative to parameter count, those coefficients can swing sharply in response to tiny changes in the data. It is _expressive but unstable_.

The intermediate case illustrates why the trade-off is about procedures, not slogans. A model with enough flexibility to capture the main signal but not so much flexibility that it chases every fluctuation can achieve low expected generalization error. That is why one should think in terms of average performance over possible samples, not just one fitted curve.

This section is also a good place to connect the pictures back to the decomposition. In the low-degree case, the variance term is small and the squared-bias term dominates. In the high-degree case, the squared-bias term can be small while the variance term dominates. The intermediate case is the one where neither term overwhelms the other.

---

Flashcards for this section are as follows:

- low-degree picture ::@:: In the low-degree case, the fitted models look similar across datasets, which means low variance, but their average remains far from the true function, which means high bias. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- high-degree picture ::@:: In the high-degree case, the fitted models vary sharply across datasets, which means high variance, even though their average can track the true function fairly well. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- intermediate-capacity picture ::@:: An intermediate-capacity model can achieve low generalization error by keeping both bias and variance at moderate levels. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- stable but wrong ::@:: A high-bias method is often stable across training sets yet systematically misses the true pattern. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- expressive but unstable ::@:: A high-variance method can represent the target well on average but fluctuate too much from one sampled dataset to another because its many adjustable parameters react strongly to sample noise. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- which term dominates in each regime ::@:: In low-capacity regimes the squared-bias term usually dominates, in high-capacity regimes the variance term usually dominates, and intermediate capacity is where neither dominates too strongly. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### graph intuition: training error, validation error, and generalization gap

The model-capacity graphs attached to this topic should be read carefully. On the horizontal axis is model capacity or complexity. On the vertical axis is an error quantity such as training error, validation error, or test error. One picture usually overlays training and validation curves, while another picture shows repeated fitted curves for several capacity regimes.

The training-error curve typically slopes downward as capacity increases. This happens because a richer hypothesis class contains all simpler models plus additional ones, so it can fit the observed sample at least as well as before. In many pictures the training curve decreases almost monotonically.

The validation or test-error curve usually has a U-shape. On the left, capacity is too small, so the model underfits and both training and validation error are high. In the middle, the model is expressive enough to capture the main signal, so validation error reaches its minimum. On the right, capacity is so high that the model starts fitting sample-specific noise, so validation/test error rises even though training error keeps falling.

The generalization gap is the vertical distance between the training and validation/test curves at the same capacity value. On one fixed split this plotted quantity estimates the sample-specific random gap $\operatorname{Gap}(S)$. If one repeated the split or resampling procedure and averaged these vertical distances, that average would estimate $\operatorname{Gap}_{\mathrm{exp}}$. At low capacity this gap is often small because the model is too simple even to fit the training data strongly. As capacity increases, the gap often widens because the learner can fit the training sample more aggressively than it can fit new data. Graphically, this widening gap is one of the clearest visual signals of increasing variance.

Another common graphic shows many fitted curves from repeated resampling. A low-capacity panel shows many similar curves clustered together but far from the truth; a high-capacity panel shows curves spread wildly across the input range; an intermediate panel shows moderate spread and a reasonable average fit. These pictures and the error curves are two views of the same phenomenon: the curve panels show the variance directly as spread across fits, while the training/validation graph shows it indirectly through a widening generalization gap.

---

Flashcards for this section are as follows:

- what the axes mean in the capacity graph ::@:: In the standard capacity graph, the horizontal axis is model complexity or capacity and the vertical axis is an error quantity such as training, validation, or test error. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- training-error curve in the capacity graph ::@:: In a model-capacity graph, training error usually decreases as capacity increases because a richer hypothesis class can fit the observed sample at least as well as a simpler one. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- why the validation/test curve is U-shaped ::@:: Validation or test error is often high at low capacity because of underfitting, lowest at intermediate capacity where bias and variance are balanced, and high again at large capacity because of overfitting. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- generalization-gap graph intuition ::@:: The generalization gap is the vertical difference between training and validation/test curves at the same capacity; it is often small at low capacity and larger at high capacity because high-capacity models fit training data more aggressively than new data. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- sample gap vs expected gap in graphs: If $\operatorname{Gap}(S)=\epsilon(h_S)-\hat\epsilon_S(h_S)$ and $\operatorname{Gap}_{\mathrm{exp}}=\mathbb{E}_S[\operatorname{Gap}(S)]$, how should a validation-curve gap be interpreted? ::@:: In one train/validation split, the plotted vertical distance estimates the sample-specific gap $\operatorname{Gap}(S)$; averaging that distance over repeated random splits estimates the expected generalization gap $\operatorname{Gap}_{\mathrm{exp}}$. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- repeated-fit graph intuition ::@:: In repeated-fit graphs, low capacity appears as many similar but systematically wrong curves, high capacity appears as widely scattered curves, and intermediate capacity appears as moderate spread around the true trend. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- how the two graph types correspond ::@:: The repeated-fit panels show bias and variance directly through average position and spread of fitted curves, while the training/validation graph shows the same trade-off indirectly through the U-shaped validation curve and widening generalization gap. <!--SR:!2026-04-12,4,270!2026-04-11,3,250-->

### regularization, cross-validation, and sample size

The decomposition connects directly to model-selection tools. Cross-validation helps estimate which capacity or regularization strength gives the best expected generalization performance. Instead of trusting training error, one compares models on held-out data and looks for the capacity region where validation error is smallest. In the language of the decomposition, cross-validation is a practical way to estimate where the bias-variance balance is most favorable.

Regularization changes the optimization problem so that large or unstable parameter values become expensive. In ridge-style regularization, for example, one minimizes a penalized objective such as training loss plus $\lambda\|w\|_2^2$. Increasing $\lambda$ usually raises bias somewhat because the fitted model is pulled toward simpler parameter values, but it often lowers variance because the parameters become less sensitive to random sample noise. Moderate regularization can therefore improve validation/test performance, while excessive regularization can underfit.

Sample size is the third major control knob. As more data are collected, each individual noisy observation has less leverage on the fitted parameters, so the learned predictor usually fluctuates less across resampled datasets. In the language of graphs, more data often narrows the generalization gap and flattens the variance-heavy right side of the validation curve. So one can fight variance not only by shrinking the model, but also by supplying more information.

For a fixed model class and the same learning procedure, this sample-size effect is mainly a variance effect, not a bias effect. Intuitively, more data make the fitted model _more stable around the same average learner_ rather than changing the structural assumptions of the learner itself. So variance often falls noticeably as sample size grows, whereas bias usually stays roughly the same unless one also changes the hypothesis class, features, or regularization.

One should also connect this to the training curve itself. As sample size increases, the empirical training error often rises slightly because the learner must fit a larger, more diverse, and more representative sample, so memorizing idiosyncrasies becomes harder. At the same time, expected generalization error often falls because the fitted model is less sample-sensitive and the empirical distribution is closer to the population distribution. These two movements together shrink the generalization gap. The broad interpretation is that with more data, training error becomes a more honest estimate of future error: the learner fits the observed sample less aggressively, but what it learns transfers better.

These three tools affect the decomposition in different ways. Cross-validation does not itself change bias or variance; it estimates which setting gives the best trade-off. Regularization usually moves the model toward higher bias and lower variance. More data usually reduces variance without requiring the model class itself to become simpler.

---

Flashcards for this section are as follows:

- why cross-validation helps with bias-variance trade-off ::@:: Cross-validation helps select model complexity or regularization strength by estimating expected generalization performance on held-out data rather than relying on training error. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- regularization effect on bias and variance: What does increasing $\lambda$ in a penalty such as training loss $+\lambda\|w\|_2^2$ usually do? ::@:: Regularization usually increases bias somewhat but decreases variance, which can improve generalization when variance was the bigger problem. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- danger of over-regularization ::@:: Too much regularization can raise bias so much that the model underfits and generalization worsens. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- effect of more data on variance ::@:: Increasing sample size usually reduces variance because the learned model fluctuates less across different sampled training sets. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- effect of more data on bias versus variance: For a fixed model class and learning rule, what usually changes when sample size increases? ::@:: For a fixed model class and the same learning procedure, increasing sample size usually reduces variance because the fitted model becomes more stable across resampled datasets, while bias remains roughly constant because the learner's structural assumptions have not changed. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- more-data graph intuition ::@:: More data often narrows the generalization gap because each noisy sample point has less influence on the fitted parameters. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- more-data effect on training error, generalization error, and gap ::@:: As sample size increases, training error often rises slightly because the model must fit a larger and more representative sample, expected generalization error often decreases because the learner becomes more stable, and the generalization gap shrinks because training performance becomes a more honest reflection of future performance. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- interpretation of the whole more-data picture ::@:: More data usually make the learner less able to memorize quirks of one sample and more able to capture repeatable structure, so training fit may look a bit worse while future performance improves and the train-test gap narrows. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- what cross-validation does and does not do ::@:: Cross-validation does not itself change bias or variance; it estimates which model complexity or regularization strength gives the best expected trade-off on held-out data. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

<!-- check: ignore-next-line[header_style]: PAC is a standard acronym -->
### PAC learning viewpoint

PAC stands for _probably approximately correct_. The central idea is to replace a decomposition identity by a finite-sample guarantee. Instead of asking how expected error splits into noise, bias, and variance, PAC learning asks whether, after observing enough training examples, the learner will _probably_ output a hypothesis whose generalization error is _approximately_ small.

More concretely, one usually fixes two tolerances: an accuracy tolerance $\epsilon>0$ and a failure probability $\delta>0$. A learning procedure is PAC-style if, once the sample size is large enough, it outputs a hypothesis whose true generalization error is at most $\epsilon$ with probability at least $1-\delta$. So "approximately correct" refers to error at most $\epsilon$, and "probably" refers to confidence at least $1-\delta$.

The relation to what we have already learned is direct. Bias-variance decomposition explains _why_ generalization can be hard and which components of error are dominating; PAC learning gives a more worst-case, sample-complexity-oriented language for _when_ generalization should be expected from finite data. Model capacity matters in both viewpoints. In bias-variance language, high capacity can increase variance. In PAC language, a richer hypothesis class usually requires more samples to guarantee small generalization error. So both viewpoints say the same broad thing in different dialects: capacity, data size, and generalization are tightly linked.

PAC theory is also more guarantee-oriented than decomposition-oriented. The decomposition here is exact but specialized to squared loss in regression and is most useful diagnostically. PAC statements are usually broader but looser: they do not split error into bias and variance, but they explain why more data and smaller or better-controlled hypothesis classes improve the chance of good generalization.

---

Flashcards for this section are as follows:

- PAC meaning: What does PAC stand for? ::@:: PAC stands for _probably approximately correct_. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- PAC interpretation with $\epsilon$ and $\delta$: What do "approximately correct" and "probably" mean in PAC learning? ::@:: "Approximately correct" means the learned hypothesis has generalization error at most $\epsilon$, and "probably" means this happens with probability at least $1-\delta$ once the sample size is large enough. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- PAC learning relation to bias-variance decomposition ::@:: Bias-variance decomposition explains why generalization error arises and what components dominate, whereas PAC learning gives finite-sample, worst-case-style guarantees about when a learner will probably generalize well. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- model capacity in PAC versus bias-variance language ::@:: In bias-variance language, high capacity can raise variance; in PAC language, a richer hypothesis class usually requires more samples to guarantee small generalization error. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### modern scaling-law remark

Modern large language model results provide an instructive empirical analogue of the sample-size and capacity story. Empirically, language-model loss often improves as a rough power law when one increases model size, training data, and total training compute over broad regimes. So the high-level statement "more parameters, more data, and more compute often improve performance" is broadly true as an empirical scaling-law observation.

But that statement needs two corrections. First, the relevant resource is not literally "GPU power" as a theoretical variable; it is more accurate to speak of total training compute, often measured in floating-point operations or an equivalent compute budget. Faster or larger GPU clusters matter mainly because they allow one to spend more compute or finish that compute budget sooner.

Second, model capacity is not an unconditional monotone good. The Chinchilla result argues that many large language models were undertrained: too many parameters for the amount of data they saw under a fixed compute budget. In that compute-limited regime, simply making the model larger is not always optimal. One must balance parameter count and number of training tokens. So the right statement is: scaling helps, but the optimal capacity depends on the task, the data regime, the optimization budget, and the compute constraint.

This is closely related to the ideas in this note. Increasing model size can reduce bias by making the model class more expressive. Increasing data can reduce variance and improve sample efficiency. Increasing compute can let optimization run further or support larger models and datasets. But finite-budget trade-offs remain: the best capacity is situation-dependent rather than universally "as large as possible".

---

Flashcards for this section are as follows:

- LLM scaling-law claim: Is it broadly true that larger language models improve with more parameters, more data, and more compute? ::@:: Broadly yes as an empirical scaling-law statement: language-model loss often improves approximately as a power law with model size, dataset size, and total training compute over wide regimes. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- GPU power versus compute in scaling-law language ::@:: The more precise variable is total training compute rather than GPU power itself; GPUs matter because they provide the hardware needed to realize a larger compute budget or shorter wall-clock time. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- Chinchilla-style correction to naive scaling intuition ::@:: Scaling is not just "make the model larger": under a fixed compute budget, model size and number of training tokens must be balanced, and overly large models can be undertrained if data do not scale with them. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- relation between LLM scaling laws and bias-variance ideas ::@:: Larger models can reduce bias by increasing expressiveness, more data can reduce variance and improve generalization, and more compute supports larger effective training budgets; but the best capacity remains situation-dependent rather than universally maximal. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

### classification remark

The classic decomposition is derived most cleanly for least-squares regression because squared loss expands quadratically, so after centering, the cross terms cancel. For zero-one classification loss, the loss is $\mathbf 1[\hat y_S(x)\neq y]$, which contains a discontinuous thresholding decision rather than a smooth square. That thresholding step is exactly what breaks the same clean algebra: one cannot simply expand an indicator into "noise + squared bias + variance" with the same cancellation trick.

This point is easier to understand operationally. In classification there are really two layers: first estimate something like a score or probability, and then convert it into a hard class label by thresholding or argmax. Small changes in predicted probabilities can leave squared probability error almost unchanged but still flip the predicted class near a decision boundary. For example, if the true class probability is $\eta(x)=0.49$, then predicted probabilities $0.48$ and $0.50$ are both very close in squared-probability terms, but one lies below the $0.5$ threshold and the other lies above it, so the induced class prediction can change abruptly. That discontinuity is why zero-one classification error does not admit the same neat decomposition.

However, if classification is phrased probabilistically, one can recover a close analogue. In binary classification, let $\eta(x)=P(Y=1\mid X=x)$ be the true class probability and let $\hat p_S(x)$ be the probability predicted by the learner trained on sample $S$. Then the expected squared probability error $\mathbb{E}_S[(\hat p_S(x)-\eta(x))^2]$ decomposes as $\bigl(\mathbb{E}_S[\hat p_S(x)]-\eta(x)\bigr)^2 + \mathbb{E}_S\bigl[(\hat p_S(x)-\mathbb{E}_S[\hat p_S(x)])^2\bigr]$, that is, squared bias plus variance for probability estimation.

So the key clarification is: in regression, the decomposition is about squared prediction error of the target itself; in classification, the closest clean analogue is usually about squared error of _probability estimates_, not about zero-one accuracy directly. The same bias-variance intuition still transfers: capacity can make probability estimates systematically wrong (bias) or highly sample-sensitive (variance). What changes is the mathematical object one decomposes.

---

Flashcards for this section are as follows:

- why the classical derivation lives in regression rather than zero-one classification ::@:: The standard derivation works in regression because squared loss is quadratic, so centering produces cross terms that can cancel; zero-one classification loss uses an indicator after thresholding or argmax, so the same algebraic expansion does not go through. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- threshold intuition for why zero-one loss resists the same decomposition ::@:: In classification, small changes in predicted probability can flip the hard class label near a decision boundary, so zero-one loss changes discontinuously even when squared probability error changes only slightly. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- probabilistic classification analogue: If $\eta(x)=P(Y=1\mid X=x)$ is the true class probability and $\hat p_S(x)$ is the learner's predicted probability, what is the decomposition of $\mathbb{E}_S[(\hat p_S(x)-\eta(x))^2]$? ::@:: One has $\mathbb{E}_S[(\hat p_S(x)-\eta(x))^2] = (\mathbb{E}_S[\hat p_S(x)]-\eta(x))^2 + \mathbb{E}_S[(\hat p_S(x)-\mathbb{E}_S[\hat p_S(x)])^2]$, so squared probability estimation error itself has a bias-variance decomposition. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- what is and is not being decomposed in classification ::@:: The clean algebra here does not decompose zero-one classification accuracy itself; the closest clean analogue usually decomposes squared error of estimated class probabilities instead. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- lesson beyond regression ::@:: Even when the exact decomposed quantity changes from target values to class probabilities, the same bias-variance intuition about systematic error and sample sensitivity still applies. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

## ensemble learning

Ensemble learning means combining several predictors into one composite predictor. The individual components are often called _base learners_, meaning the individual models inside the combination. A _weak learner_ is a base learner that may be only slightly better than a trivial baseline such as random guessing, but can still be useful when combined with others. The final combined model is the _ensemble_.

The bias-variance viewpoint gives a natural motivation. If one learner is too unstable, average several of them to reduce variance. If one learner is too weak or too biased, build a stronger one by combining many simple learners strategically. This creates the conceptual split between bagging and boosting. Bagging primarily targets variance: train many models on perturbed datasets and aggregate them. Boosting primarily targets bias: train models sequentially so each new model focuses on the errors that previous models left behind.

In regression, an ensemble predictor is often an average such as $\hat f_{\mathrm{ens}}(x)=\frac{1}{B}\sum_{b=1}^B h_b(x)$. In classification, it is often a majority vote or a weighted vote, or probability averaging followed by thresholding. The key point is that the ensemble is not one monolithic learner; it is a combination of many learned components.

It is helpful to separate the mechanics from the effect. Mechanically, bagging changes the _data seen by each learner_ and then averages the answers; boosting changes the _importance of training examples across rounds_ and then adds the learners stage by stage. Effect-wise, bagging mainly makes a noisy learner more stable, while boosting mainly makes a weak learner more expressive. A good memory cue is therefore: _bagging = parallel averaging for stability_; _boosting = sequential correction for strength_.

The detailed procedures, formulas, and concrete examples are developed in the dedicated bagging and boosting subsections below to avoid repeating near-identical material at two hierarchy levels.

---

Flashcards for this section are as follows:

- what ensemble learning means ::@:: Ensemble learning means combining several base learners into one predictor so the final model can be more stable or more expressive than any single component. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- base learner versus weak learner ::@:: A base learner is one component model inside an ensemble; a weak learner is a deliberately simple base learner that may be only slightly better than a trivial baseline but can still be powerful when combined with others. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- decomposition as design guide ::@:: The bias-variance viewpoint helps diagnose whether a method needs more flexibility, more stability, or both. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- bagging versus boosting intuition ::@:: Mechanically, bagging trains learners in parallel on perturbed datasets and averages them, while boosting trains learners sequentially so each new learner corrects earlier mistakes; bagging mainly adds stability, whereas boosting mainly adds strength. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

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

- bootstrap sample in bagging: What is it? ::@:: A bootstrap sample is drawn with replacement from the original training set, so some examples can appear multiple times while others may be absent in a given resample. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- bagging regression formula: If bootstrap samples are $S^{(1)},\ldots,S^{(B)}$, what is $\hat f_{\mathrm{bag}}(x)$? ::@:: In regression, bagging forms the ensemble prediction $\hat f_{\mathrm{bag}}(x)=\frac{1}{B}\sum_{b=1}^B h_{S^{(b)}}(x)$ by averaging predictions from models trained on bootstrap samples. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- bagging prediction rule in classification ::@:: In classification, bagging usually combines models by majority vote or by averaging class probabilities and then predicting the largest or thresholded probability. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- bagging intuition in words ::@:: Bagging takes an unstable learner, trains it on many slightly different bootstrap versions of the data, and averages the resulting predictions so sample-specific quirks partly cancel while common signal remains. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- bagging procedure steps ::@:: A standard bagging workflow is: (1) draw many bootstrap samples, (2) train the same base learner on each sample independently, (3) evaluate all learners on a new input, and (4) aggregate by averaging, voting, or probability averaging. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- idealized variance reduction in bagging: If $B$ base predictions are independent and each has variance $\sigma^2$, what is the variance of their average? ::@:: If $B$ base predictions were independent and each had variance $\sigma^2$, then averaging them would give variance $\sigma^2/B$, which shows why aggregation reduces instability. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- correlated-error variance formula for bagging: If common variance is $\sigma^2$ and pairwise correlation is $\rho$, what is $\operatorname{Var}(\frac{1}{B}\sum_{b=1}^B h_b)$? ::@:: If bagged base learners have common variance $\sigma^2$ and pairwise correlation $\rho$, then $\operatorname{Var}(\frac{1}{B}\sum_{b=1}^B h_b)=\rho\sigma^2+\frac{1-\rho}{B}\sigma^2$, so bagging helps most when base learners are unstable but not too strongly correlated. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- bagging tax-survey analogy ::@:: Bagging is like repeating a noisy survey-based estimate many times and averaging the answers so the final estimate fluctuates less. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- when bagging is most useful ::@:: Bagging is most useful for unstable base learners whose predictions vary noticeably across resampled datasets. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- concrete bagging examples ::@:: Typical bagging examples are averaging many decision trees for house-price regression or using majority vote across many trees for classification tasks such as spam filtering or diagnosis. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->

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

- initial weighting in boosting ::@:: Boosting typically begins by assigning equal weights to all training examples before any learner is trained. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- why weights are increased on mistakes ::@:: Boosting raises the weights of misclassified or poorly fitted examples so later learners focus on cases the current ensemble still handles badly. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- final form of a boosting model: What does a stagewise additive model $F_T(x)$ look like? ::@:: A boosting model is a weighted combination such as $F_T(x)=\sum_{t=1}^T \alpha_t h_t(x)$ of a sequence of base learners trained in successive rounds. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- what a weak learner means in boosting ::@:: A weak learner is a base learner that may be only slightly better than naive guessing, but boosting can combine many such learners into a strong ensemble. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- boosting intuition in words ::@:: Boosting works sequentially: after one learner makes mistakes, the next learner is pushed to focus on those hard cases, so the ensemble gradually corrects its own residual errors and becomes stronger. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- boosting procedure steps ::@:: A standard boosting workflow is: (1) initialize equal example weights or residuals, (2) train a weak learner, (3) assign it a stage weight, (4) update weights or residuals to emphasize current mistakes, and (5) repeat to build a stagewise additive model. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- examples of boosting methods with meanings ::@:: AdaBoost reweights examples to emphasize mistakes, gradient boosting fits new learners to residuals or negative gradients left by the current ensemble, and XGBoost is an efficient regularized implementation of gradient-boosted trees. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- concrete boosting examples ::@:: Typical boosting examples are AdaBoost combining many decision stumps for binary classification and gradient-boosted trees that successively fit residuals for tabular regression or classification. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- boosting caveat ::@:: Although boosting is often used to reduce bias, excessive boosting can still overfit if the ensemble is allowed to chase noise too aggressively. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
