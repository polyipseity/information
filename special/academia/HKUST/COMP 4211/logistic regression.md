---
aliases:
  - binary logistic regression
  - logistic regression
  - logistic regressions
tags:
  - flashcard/active/special/academia/HKUST/COMP_4211/logistic_regression
  - language/in/English
---

<!-- check: ignore-file[two_sided_calc_warning]: concept note uses symbolic answers on QA cards -->

# logistic regression

Logistic regression is the course's first full classification model. It keeps the familiar affine score from linear regression, but instead of predicting an unconstrained real number directly, it maps that score through a sigmoid so the output can be interpreted as a probability for a binary class label. This makes it a discriminative probabilistic model: it learns $P(y\mid x)$ directly.

An important memory shortcut is that logistic regression reuses the linear model's score and then adds a probability link: score first, probability second. In symbols, linear regression uses $\hat y = w^\top x$ as a direct numeric prediction, while logistic regression uses $\hat p = \sigma(w^\top x)$ as a class-probability prediction. So the phrase "linear regression plus sigmoid" is a good geometric intuition, but the statistical model and loss change from Gaussian/squared-error style to Bernoulli/cross-entropy style.

That small modeling change has large consequences. Once outputs are probabilities, the natural training objective is no longer mean squared error but a likelihood-based loss, which in this case becomes cross entropy. The lecture uses logistic regression to introduce the broader pattern that classification often combines probability modeling, loss design, optimization, and evaluation under metrics that are not necessarily identical to the training objective.

This topic also uses logistic regression as a meeting point of several foundational ideas. It connects odds and log-odds to linear prediction, connects entropy and cross entropy to supervised learning, connects maximum likelihood to parameter estimation, and connects differentiation to practical training through gradient descent. By the end of the discussion, the binary model has already expanded into softmax regression and stochastic optimization, while the companion [classification](classification.md) note handles the evaluation metrics that sit beside the model rather than inside it.

---

Flashcards for this section are as follows:

- overview ::@:: Logistic regression is a discriminative probabilistic classifier that models $P(y\mid x)$ for binary labels by applying a sigmoid to an affine score.
- logistic regression versus linear regression ::@:: Linear regression uses $w^\top x$ as a direct numeric prediction, whereas logistic regression uses $\sigma(w^\top x)$ as a probability in $[0,1]$ and is typically trained with Bernoulli cross entropy.
- why logistic regression matters ::@:: Logistic regression introduces the general machine-learning pattern of combining a probabilistic output model, a likelihood-based loss, gradient-based optimization, and task-specific evaluation metrics.
- linear-plus-sigmoid memory view ::@:: A useful memory view is "linear score plus sigmoid link": keep $z=w^\top x$ from linear models, then convert it to probability by $p=\sigma(z)$.
- why this topic is foundational ::@:: This topic ties together log-odds, entropy, likelihood, gradient descent, softmax regression, and classification metrics in one coherent model family.

## binary logistic model and decision boundary

For binary classification, the data are pairs $(x_i,y_i)$ where $x_i \in \mathbb{R}^{D+1}$ is the augmented feature vector and $y_i \in \{0,1\}$ is the class label. Logistic regression chooses a real-valued score $z = w^\top x$ and then converts that score into a probability. In that sense, it keeps the linear scoring machinery from linear regression but changes the meaning of the output completely.

The logistic assumption is that the label distribution conditioned on the input is Bernoulli with parameter $\sigma(w^\top x)$, where $\sigma(z)=\frac{1}{1+e^{-z}}$ is the sigmoid. Therefore, $P(y=1\mid x,w)=\sigma(w^\top x)$ and $P(y=0\mid x,w)=1-\sigma(w^\top x)$. The model does not output a hard class immediately; it outputs a probability model from which a class decision can then be derived.

Because the sigmoid is monotone increasing, thresholding the probability at $0.5$ is equivalent to thresholding the score at $0$. So logistic regression is simultaneously a probabilistic classifier and a linear classifier. The probability surface is curved by the sigmoid, but the decision boundary itself is still the hyperplane $w^\top x = 0$.

This hyperplane interpretation is essential for geometric intuition. The weight vector $w$ is normal to the boundary, and changing the bias/intercept shifts the hyperplane without changing its orientation. So logistic regression is nonlinear only in the probability mapping, not in the separating surface itself.

---

Flashcards for this section are as follows:

- sigmoid function $\sigma(z)=\frac{1}{1+e^{-z}}$ ::@:: The sigmoid activation is $\sigma(z)=\frac{1}{1+e^{-z}}$.
- logistic class probability $P(y=1\mid x,w)=\sigma(w^\top x)$ ::@:: In binary logistic regression, $P(y=1\mid x,w)=\sigma(w^\top x)$ and $P(y=0\mid x,w)=1-\sigma(w^\top x)$.
- augmented feature vector in logistic regression ::@:: Writing the input as an augmented vector $x=(1,\tilde x^\top)^\top$ absorbs the intercept into $w$, so the score keeps the simple dot-product form $w^\top x$. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- hyperplane geometry of the logistic score ::@:: The surface $w^\top x=0$ is a hyperplane whose normal vector is $w$; changing the intercept shifts the hyperplane, while changing the non-bias weights changes its orientation.
- why sigmoid is useful for classification ::@:: The sigmoid converts any real-valued score into a number between $0$ and $1$, making it suitable as a binary class probability.
- binary labels in logistic regression ::@:: In the standard binary logistic-regression setup, the targets are encoded as $y \in \{0,1\}$ so the conditional model can be written as a Bernoulli distribution.

### link functions, sigmoid motivation, and alternatives

You asked a very good question: does any function from $\mathbb{R}$ to $[0,1]$ work? For binary classification, any such mapping can produce a score interpretable as a probability-like quantity, but not all choices are equally convenient for optimization and interpretation. In practice one usually wants a smooth monotone link, stable gradients, and a clean probabilistic model.

The sigmoid is preferred because it has several aligned advantages: it is smooth and monotone, it has a simple derivative $\sigma'(z)=\sigma(z)(1-\sigma(z))$, it yields the linear-logit identity $\log\frac{p}{1-p}=w^\top x$, and with Bernoulli likelihood it gives a convex objective for linear predictors. This combination makes both theory and implementation clean.

Common alternatives include the probit link $p=\Phi(z)$, the complementary log-log link $p=1-e^{-e^z}$, and other calibrated monotone squashing maps. They can be useful when tail behavior or domain assumptions suggest them, but they usually sacrifice at least one convenience of logistic regression (for example derivative simplicity or canonical generalized-linear-model interpretation).

---

Flashcards for this section are as follows:

- does any map to $[0,1]$ work for binary classification? ::@:: Any mapping from score to $[0,1]$ can define probability-like outputs, but practical links are chosen for smoothness, interpretability, and optimization behavior, not only range constraints.
- why sigmoid is preferred in logistic regression ::@:: Sigmoid is smooth and monotone, has derivative $\sigma'(z)=\sigma(z)(1-\sigma(z))$, gives linear logit $\log\frac{p}{1-p}=w^\top x$, and yields a convex Bernoulli negative log-likelihood for linear predictors.
- probit alternative ::@:: Probit classification uses $p=\Phi(w^\top x)$, where $\Phi$ is the standard normal cumulative distribution function.
- complementary-log-log alternative ::@:: Complementary log-log uses $p=1-e^{-e^{w^\top x}}$, which is asymmetric compared with the sigmoid link.

<!-- check: ignore-next-line[header_style]: Bernoulli is a proper noun -->
### Bernoulli output model, odds, and logit

The model can be written compactly as $p(y\mid x,w)=\operatorname{Bernoulli}(y\mid \sigma(w^\top x))$. Equivalently, for a single input $x$ with positive-class probability $p$, the Bernoulli law says $p(y\mid x,w)=p^y(1-p)^{1-y}$ with $p=\sigma(w^\top x)$. This compact expression is useful when deriving likelihood and cross entropy, because the cases $y=1$ and $y=0$ are handled at once.

The odds are defined as $\frac{p}{1-p}$, which can be interpreted as "how many times more likely class $1$ is than class $0$." For example, odds $=4$ means class $1$ is four times as likely as class $0$, while odds $=\frac{1}{4}$ means class $0$ is four times as likely as class $1$.

The logit is the logarithm of the odds, $\operatorname{logit}(p)=\log\frac{p}{1-p}$. Its motivation is twofold: it maps probabilities from $(0,1)$ to the whole real line and turns multiplicative odds changes into additive shifts. It is also exactly the inverse of the sigmoid. Indeed, if $p=\sigma(z)=\frac{1}{1+e^{-z}}$, then solving for $z$ gives $p(1+e^{-z})=1$, hence $pe^{-z}=1-p$, so $e^{-z}=\frac{1-p}{p}$ and therefore $z=\log\frac{p}{1-p}=\operatorname{logit}(p)$. In logistic regression, $\operatorname{logit}(p)=w^\top x$, so each feature contributes additively on the log-odds scale.

This creates a practical coefficient interpretation. Increasing feature $x_j$ by one unit changes log-odds by $w_j$ (holding other features fixed), so the odds are multiplied by $e^{w_j}$. Large positive scores imply large positive log-odds and therefore probabilities near $1$, while large negative scores imply probabilities near $0$. So odds answer the multiplicative question and logit answers the additive-linear question: odds say how much more likely class $1$ is, while logit says what linear score produced that odds ratio.

---

Flashcards for this section are as follows:

- Bernoulli form of logistic regression ::@:: Binary logistic regression assumes $p(y\mid x,w)=\operatorname{Bernoulli}(y\mid \sigma(w^\top x))$. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- Bernoulli likelihood in one formula ::@:: If $p=\sigma(w^\top x)$, then the binary-label likelihood can be written as $p(y\mid x,w)=p^y(1-p)^{1-y}$ for $y \in \{0,1\}$. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- odds ::@:: If $p=P(y=1\mid x,w)$, then odds are $\frac{p}{1-p}=\frac{P(y=1\mid x,w)}{P(y=0\mid x,w)}$, which quantifies relative likelihood of class $1$ versus class $0$.
- inverse-logit derivation: Given $p=\sigma(z)=\frac{1}{1+e^{-z}}$, solve for $z$ ::@:: Solving $p=\frac{1}{1+e^{-z}}$ gives $e^{-z}=\frac{1-p}{p}$ and hence $z=\log\frac{p}{1-p}$, so $\operatorname{logit}(p)=\sigma^{-1}(p)$ on $(0,1)$. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
- logit or log-odds ::@:: The logit is $\operatorname{logit}(p)=\log \frac{p}{1-p}$, which maps probabilities from $(0,1)$ to $\mathbb{R}$, linearizes multiplicative odds effects, and is exactly the inverse of the sigmoid link.
- why logistic regression is linear in the logit ::@:: Logistic regression satisfies $\log \frac{P(y=1\mid x,w)}{P(y=0\mid x,w)} = w^\top x$, so the log-odds are a linear function of the features.
- meaning of a large positive score ::@:: A large positive value of $w^\top x$ means the model assigns class $1$ odds far above $1$ and therefore predicts a probability near $1$. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- coefficient interpretation on odds scale ::@:: A one-unit increase in feature $x_j$ shifts log-odds by $w_j$, so the odds are multiplied by $e^{w_j}$ when other features are fixed.
- odds-versus-logit memory cue ::@:: Odds answer the multiplicative question $\frac{p}{1-p}$, while logit answers the additive-linear question $\log\frac{p}{1-p}=w^\top x$. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->

### worked probability and log-odds computation

Suppose a binary logistic model gives score $z = w^\top x = 1.386$. Then $p=P(y=1\mid x,w)=\sigma(1.386)=\frac{1}{1+e^{-1.386}}\approx 0.8$. The corresponding odds are $\frac{p}{1-p}=\frac{0.8}{0.2}=4$, and the log-odds are $\log 4 \approx 1.386$, matching the original score as expected.

If the score flips sign to $z=-1.386$, then $p\approx 0.2$, the odds become $\frac{0.2}{0.8}=\frac{1}{4}$, and the log-odds become $\log(1/4)=-1.386$. This simple pair is a good memory anchor: changing the sign of the score swaps the class odds reciprocally.

---

Flashcards for this section are as follows:

- worked sigmoid-logit example: If $z=1.386$, what are $p=\sigma(z)$, the odds, and the log-odds? ::@:: $p\approx 0.8$, odds $=\frac{0.8}{0.2}=4$, and log-odds $=\log 4\approx 1.386$.
- score-sign flip effect ::@:: Replacing $z$ by $-z$ replaces $p$ by $1-p$ and inverts the odds, so a score-sign flip swaps class preference.

<!-- check: ignore-next-line[header_style]: Bayes is a proper noun -->
### Bayes decision rule and thresholding

Once the conditional distribution is available, classification is done by point estimation: choose the action with the smallest conditional risk, or under zero-one loss equivalently choose the most probable label. The rule is $\hat y = \arg\max_y p(y\mid x,w)$. For the binary case, this means predicting class $1$ when $P(y=1\mid x,w) > P(y=0\mid x,w)$ and class $0$ otherwise. Because $P(y=1\mid x,w)=\sigma(w^\top x)$, this reduces to the threshold rule $\sigma(w^\top x) > 0.5$ in the equal-cost case.

For this course and its slides, the default exam/assignment convention is strict thresholding at $0.5$: predict class $1$ when $P(y=1\mid x,w)>0.5$ and class $0$ otherwise. Some textbooks and software use the variant $P(y=1\mid x,w)\ge 0.5$. These two conventions differ only on the exact tie case $P(y=1\mid x,w)=0.5$, but that tie-case rule should still be stated explicitly in exam-style work rather than being left implicit.

More generally, one can use a threshold $\tau \in (0,1)$ and predict class $1$ when $P(y=1\mid x,w)>\tau$ (or $\ge \tau$, depending on the tie convention). This is common when class priors are imbalanced or when false-positive and false-negative costs are different. If the only nonzero costs are false-positive cost $C_{FP}$ and false-negative cost $C_{FN}$, then the conditional risks are $R(1\mid x)=C_{FP}P(y=0\mid x)$ and $R(0\mid x)=C_{FN}P(y=1\mid x)$. Predicting class $1$ is Bayes-optimal exactly when $R(1\mid x)<R(0\mid x)$, which is equivalent to $P(y=1\mid x)>\frac{C_{FP}}{C_{FP}+C_{FN}}$. The familiar $0.5$ rule is therefore just the equal-cost special case.

Because the sigmoid is monotone, the equal-cost Bayes rule $\sigma(w^\top x)>0.5$ reduces immediately to $w^\top x>0$. So this section does not introduce a new separating surface; it explains why the same hyperplane described earlier is the correct decision rule once one specifies a loss.

The lecture describes this prediction rule as the optimal Bayes classifier for the model because, once posterior probabilities are known, choosing the smaller conditional-risk action minimizes loss pointwise. The notation is worth stating explicitly. Here $x$ is the observed input, $a$ is the action or predicted class, $y$ is the unknown true class label, and $C(a,y)$ is the loss incurred when one predicts $a$ but the truth is $y$. The conditional risk is therefore $R(a\mid x)=\sum_y C(a,y)P(y\mid x)$, meaning the expected loss of action $a$ after conditioning on the observed input $x$.

Under zero-one loss $C(a,y)=\mathbf{1}[a\ne y]$, every wrong prediction costs $1$ and every correct prediction costs $0$. In the binary case this gives $R(\hat y=1\mid x)=P(y=0\mid x)$ and $R(\hat y=0\mid x)=P(y=1\mid x)$, because predicting class $1$ is wrong exactly on the event $y=0$, and predicting class $0$ is wrong exactly on the event $y=1$. So the Bayes action is to choose the larger posterior probability. In words: if the model says class $1$ is more probable than class $0$, then predicting $1$ makes the probability of being wrong as small as possible at that $x$.

This also clarifies why threshold changes are meaningful. The familiar $0.5$ rule is the equal-cost special case. If false positives and false negatives carry different costs, the Bayes-optimal threshold shifts away from $0.5$ according to those costs and possibly prior structure. So the threshold is not an arbitrary afterthought; it is the decision-theoretic summary of how one values different mistakes.

That does _not_ mean the global training objective is zero-one loss. The fitted model parameters are obtained by maximizing conditional likelihood (equivalently minimizing cross entropy), and then the Bayes decision rule is applied to the resulting posterior probabilities. Logistic regression therefore has two logically distinct layers: a probabilistic estimation layer that learns $P(y\mid x,w)$, and a decision layer that converts those probabilities into actions using the loss or cost structure of the task.

---

Flashcards for this section are as follows:

- point-estimation rule in logistic regression ::@:: Logistic prediction chooses the action with smallest conditional risk; under zero-one loss this becomes $\hat y=\arg\max_{y\in\{0,1\}} P(y\mid x,w)$, so binary prediction uses the larger posterior probability.
- threshold conventions at $0.5$ ::@:: In this course, the equal-cost convention is predict class $1$ when $P(y=1\mid x,w)>0.5$; many texts instead use $P(y=1\mid x,w)\ge 0.5$, so the only difference is how the exact tie case $P(y=1\mid x,w)=0.5$ is resolved.
- equal-cost Bayes rule in score form ::@:: Under equal costs, predicting class $1$ when $P(y=1\mid x,w)>0.5$ is equivalent to predicting class $1$ when $w^\top x>0$, because the sigmoid is monotone increasing.
- Bayes classifier remark with notation ::@:: Here $x$ is the observed input, $a$ is the action or predicted class, $y$ is the true class, $C(a,y)$ is the loss, and $R(a\mid x)=\sum_y C(a,y)P(y\mid x)$ is conditional risk; the Bayes classifier chooses the action with smallest conditional risk after seeing $x$. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- zero-one Bayes derivation in binary form with context ::@:: Under zero-one loss $C(a,y)=\mathbf{1}[a\ne y]$, predicting class $1$ is wrong exactly when $y=0$, so $R(1\mid x)=P(y=0\mid x)$; similarly $R(0\mid x)=P(y=1\mid x)$, hence Bayes prediction chooses the larger posterior probability.
- cost-sensitive Bayes threshold ::@:: If false-positive cost is $C_{FP}$ and false-negative cost is $C_{FN}$, then predict class $1$ when $C_{FP}P(y=0\mid x)<C_{FN}P(y=1\mid x)$, equivalently when $P(y=1\mid x)>\frac{C_{FP}}{C_{FP}+C_{FN}}$. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- estimation-versus-decision distinction ::@:: Logistic regression first fits posterior probabilities by likelihood or cross entropy, then converts them into class decisions by a Bayes rule determined by the chosen loss or cost structure.

## entropy, cross entropy, and maximum likelihood

This topic does not introduce cross entropy as an arbitrary formula to memorize. It first develops the information-theoretic background and fixes the role of each distribution symbol. We use $P$ for the unknown true data-generating distribution and $Q$ for the approximating model distribution. Entropy quantifies uncertainty under $P$, cross entropy quantifies coding cost when outcomes from $P$ are encoded as if they came from $Q$, and likelihood quantifies how strongly a model parameter explains observed data.

These ideas become the bridge from theory to supervised learning. The unknown real-world joint law is $P(x,y)$, while the learner proposes $Q(y\mid x)$. Better approximation means lower conditional cross entropy, not lower entropy of $P$ itself. The three formulas to keep straight are $H(P)=\mathbb{E}_{P}[-\log P]$, $H(P,Q)=\mathbb{E}_{P}[-\log Q]$, and $D_{\mathrm{KL}}(P\Vert Q)=\mathbb{E}_{P}[\log P-\log Q]$. The left slot tells who generates the data and the right slot tells whose log-probability gets charged.

The maximum-likelihood viewpoint states the same goal in product form: good parameters assign high probability to what was observed. Taking negative logarithms converts products into sums and leads to cross-entropy-like objectives that are differentiable and numerically stable to optimize. So the memory flow is: true distribution $P$ says what happens, model distribution $Q$ says what score we pay, and negative log-likelihood is the empirical version of that scoring rule.

---

Flashcards for this section are as follows:

- entropy intuition ::@:: Entropy measures the uncertainty of a distribution, while cross entropy measures the coding cost incurred when one uses the wrong distribution to represent outcomes.
- unknown true distribution versus learned model ::@:: In supervised learning, one imagines an unknown true distribution $P(x,y)$ and learns a model conditional distribution $Q(y\mid x)$ from sampled data. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- why likelihood matters ::@:: Likelihood measures how strongly a parameter choice explains the observed data, and taking negative logs turns it into an additive optimization objective. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- true-versus-model memory rule ::@:: Keep the full triad $H(P)=\mathbb{E}_{Z\sim P}[-\log P(Z)]$, $H(P,Q)=\mathbb{E}_{Z\sim P}[-\log Q(Z)]$, and $D_{\mathrm{KL}}(P\Vert Q)=\mathbb{E}_{Z\sim P}[\log P(Z)-\log Q(Z)]$: the first argument always generates and weights the data, while the second argument is the model being scored. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- left-slot right-slot memory cue ::@:: Read $H(P,Q)$ and $D_{\mathrm{KL}}(P\Vert Q)$ left-to-right as _generator then scorer_: $P$ says what outcomes actually occur, and $Q$ is the distribution whose log-probabilities are evaluated on those outcomes.

### entropy and uncertainty

If $X$ is a discrete random variable, its entropy is $H(X) = -\sum_x P(x)\log P(x) = \mathbb{E}_P[-\log P(X)]$. Entropy is larger when the distribution is more uncertain or more spread out. This is why a fair coin has less entropy than a fair die, and a fair die has less entropy than a uniformly chosen card from a $54$-card deck.

The clean mathematical intuition comes from the uniform case. If a distribution is uniform on $n$ outcomes, then $P(x)=\frac1n$ for each outcome and therefore $H(X)=-\sum_{k=1}^n \frac1n\log\frac1n = -n\cdot \frac1n\log\frac1n = \log n$. So a fair coin has entropy $\log 2$, a fair die has entropy $\log 6$, and a uniform choice from a $54$-card deck has entropy $\log 54$. Since $2<6<54$, one gets $\log 2<\log 6<\log 54$. More possible equally likely outcomes mean a larger average uncertainty.

The slide examples matter because they fix the interpretation. Entropy is not about the names of the outcomes but about how concentrated or diffuse the probability mass is. A distribution with many nearly equally likely outcomes has high uncertainty, whereas a distribution concentrated on a few outcomes has lower uncertainty.

Entropy is also a special case of cross entropy. If the approximating distribution equals the true one, then $H(P,P)= -\sum_x P(x)\log P(x)=H(P)$. This identity is a reliable memory anchor: same two arguments means no mismatch penalty.

---

Flashcards for this section are as follows:

- entropy formula ::@:: For a discrete random variable $X$, the entropy is $H(X) = -\sum_x P(x)\log P(x) = \mathbb{E}_P[-\log P(X)]$.
- entropy interpretation ::@:: Entropy measures how uncertain or unpredictable a distribution is.
- coin die card comparison: If the distributions are uniform on $2$, $6$, and $54$ outcomes, why is the entropy ordering $H_{\text{coin}}<H_{\text{die}}<H_{\text{deck}}$? ::@:: For a uniform distribution on $n$ outcomes, $H=-\sum_{k=1}^n \frac1n\log\frac1n=\log n$, so the three entropies are $\log 2$, $\log 6$, and $\log 54$; since $2<6<54$, one has $\log 2<\log 6<\log 54$.
- what raises entropy ::@:: Entropy rises when probability mass is spread more evenly across more possible outcomes.
- entropy as cross-entropy special case ::@:: Entropy is the special case $H(P)=H(P,P)$, namely cross entropy when the model distribution equals the true distribution. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->

### cross entropy and Kullback-Leibler divergence

Given a true distribution $P$ and an approximating distribution $Q$ on the same outcome space, the Kullback-Leibler divergence is $D_{\mathrm{KL}}(P\Vert Q)=\sum_x P(x)\log \frac{P(x)}{Q(x)}$. It is not symmetric, so it is not a geometric distance in the usual sense, but it is a precise mismatch measure for "true $P$ approximated by model $Q$."

Cross entropy is $H(P,Q)= -\sum_x P(x)\log Q(x)=\mathbb{E}_{x\sim P}[-\log Q(x)]$. At a single outcome $x$, the term $-\log Q(x)$ is the surprise or coding cost assigned by the model $Q$; averaging those costs under $P$ gives the average penalty paid when reality is governed by $P$ but one scores outcomes with $Q$. A practical memory rule is therefore: the first argument ($P$) supplies averaging weights, and the second argument ($Q$) supplies surprise terms inside the logarithm. This avoids the common swap mistake.

A second memory cue is to read formulas left-to-right as _source then scorer_: $P$ generates outcomes, and $Q$ is evaluated on those outcomes. This also explains the directionality of $D_{\mathrm{KL}}(P\Vert Q)$: swapping to $D_{\mathrm{KL}}(Q\Vert P)$ changes which distribution defines the averaging weights and therefore changes the optimization emphasis.

Entropy itself is the no-mismatch baseline $H(P)=\mathbb{E}_{P}[-\log P(X)]$, where reality is scored by its own probabilities. Cross entropy replaces the ideal scorer $P$ by the model scorer $Q$, and KL divergence measures exactly the extra penalty paid for that replacement: $D_{\mathrm{KL}}(P\Vert Q)=H(P,Q)-H(P)$. So entropy is the unavoidable uncertainty already in the data, and KL is the additional penalty for using the wrong model.

Support mismatch is a critical practical caveat: if there exists some $x$ with $P(x)>0$ but $Q(x)=0$, then $D_{\mathrm{KL}}(P\Vert Q)=+\infty$ and cross entropy is also driven to infinity at that point because $-\log Q(x)$ diverges. The model is then assigning impossible probability to an event that truly occurs, so the mismatch penalty becomes infinite.

Combining definitions yields $H(P,Q)=H(P)+D_{\mathrm{KL}}(P\Vert Q)$. Since $H(P)$ is constant with respect to model parameters in $Q$, minimizing cross entropy with respect to $Q$ is equivalent to minimizing $D_{\mathrm{KL}}(P\Vert Q)$.

It is often helpful to visualize how these quantities change as the approximating distribution moves while the true distribution stays fixed. A clean example uses normal distributions. Fix the true distribution as $P=\mathcal{N}(0,1)$ and first vary the approximating distribution only through its mean, taking $Q_\mu=\mathcal{N}(\mu,1)$.

In that case, the entropy of the true distribution is constant: $H(P)=\tfrac12\log(2\pi e)$. The Kullback-Leibler divergence becomes $D_{\mathrm{KL}}(P\Vert Q_\mu)=\frac{\mu^2}{2}$, which is a parabola in $\mu$ with minimum $0$ at $\mu=0$. Therefore the cross entropy is $H(P,Q_\mu)=H(P)+\frac{\mu^2}{2}$, which has the same parabola shape but shifted upward by the constant entropy $H(P)$. So, as the approximating mean drifts away from the true mean, KL and cross entropy rise quadratically, while entropy stays flat because the true distribution itself has not changed.

If instead one fixes the true distribution at $P=\mathcal{N}(0,1)$ and varies only the approximating variance, taking $Q_\sigma=\mathcal{N}(0,\sigma^2)$, then $D_{\mathrm{KL}}(P\Vert Q_\sigma)=\log \sigma + \frac{1}{2\sigma^2}-\frac12$. This curve is minimized at $\sigma=1$, where the approximating variance matches the true variance. It blows up as $\sigma\to 0$ because the approximating distribution becomes too concentrated, and it also grows as $\sigma\to\infty$ because the approximation becomes too diffuse. Again, cross entropy has exactly the same shape as a function of $\sigma$, only shifted upward by the constant term $H(P)$.

So the graph intuition is: entropy is flat when the true distribution is fixed, KL is a nonnegative bowl-like mismatch curve with minimum at the correct approximation, and cross entropy is that same mismatch curve shifted upward by the true entropy baseline.

---

Flashcards for this section are as follows:

- Kullback-Leibler divergence with direction ::@:: The direction-specific divergence is $D_{\mathrm{KL}}(P\Vert Q)=\sum_x P(x)\log\frac{P(x)}{Q(x)}$, where $P$ supplies weights and $Q$ appears in the denominator as the approximating model. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- why direction in KL matters ::@:: Generally $D_{\mathrm{KL}}(P\Vert Q)\ne D_{\mathrm{KL}}(Q\Vert P)$ because swapping changes the expectation weights and therefore what kinds of mismatch are emphasized.
- cross entropy with source/scorer interpretation ::@:: $H(P,Q)=\mathbb{E}_{x\sim P}[-\log Q(x)]$ means outcomes are drawn from true/source $P$, each outcome is charged surprise $-\log Q(x)$ by the model, and those charges are averaged using the true frequencies from $P$.
- entropy-versus-cross-entropy-versus-KL ::@:: Entropy $H(P)=\mathbb{E}_{P}[-\log P]$ is the ideal self-scoring cost, cross entropy $H(P,Q)=\mathbb{E}_{P}[-\log Q]$ is the cost of scoring true data with model $Q$, and KL divergence $D_{\mathrm{KL}}(P\Vert Q)=H(P,Q)-H(P)$ is the extra mismatch penalty.
- relation $H(P,Q)=H(P)+D_{\mathrm{KL}}(P\Vert Q)$ ::@:: Since $H(P)=\mathbb{E}_{x\sim P}[-\log P(x)]$, one has $H(P,Q)-H(P)=\mathbb{E}_{x\sim P}\bigl[\log P(x)-\log Q(x)\bigr]=D_{\mathrm{KL}}(P\Vert Q)$. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- why minimizing cross entropy makes sense ::@:: Because $H(P)$ is constant with respect to model parameters, minimizing $H(P,Q)$ over $Q$ is equivalent to minimizing $D_{\mathrm{KL}}(P\Vert Q)$. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- support mismatch consequence ::@:: If some event has $P(x)>0$ but $Q(x)=0$, then $D_{\mathrm{KL}}(P\Vert Q)=+\infty$ and cross entropy also diverges there because the model assigns zero probability to an event that truly occurs, so $-\log Q(x)$ is infinite.
- do-not-swap memory cue with full formulas ::@:: Use the full cluster $H(P)=\mathbb{E}_{P}[-\log P]$, $H(P,Q)=\mathbb{E}_{P}[-\log Q]$, $D_{\mathrm{KL}}(P\Vert Q)=\mathbb{E}_{P}[\log P-\log Q]$: the expectation distribution is always the first argument, so the left slot is the generator and the right slot is the scorer.
- Gaussian mean-shift graph intuition: If $P=\mathcal{N}(0,1)$ and $Q_\mu=\mathcal{N}(\mu,1)$, what are the shapes of entropy, cross entropy, and KL divergence as functions of $\mu$? ::@:: The true entropy is constant, $H(P)=\tfrac12\log(2\pi e)$; the divergence is $D_{\mathrm{KL}}(P\Vert Q_\mu)=\mu^2/2$, a parabola minimized at $\mu=0$; and the cross entropy is $H(P,Q_\mu)=H(P)+\mu^2/2$, the same parabola shifted upward by the constant entropy baseline.
- Gaussian variance-mismatch graph intuition: If $P=\mathcal{N}(0,1)$ and $Q_\sigma=\mathcal{N}(0,\sigma^2)$, what shape does $D_{\mathrm{KL}}(P\Vert Q_\sigma)$ have as $\sigma$ varies? ::@:: One has $D_{\mathrm{KL}}(P\Vert Q_\sigma)=\log\sigma+\frac{1}{2\sigma^2}-\frac12$, which is minimized at $\sigma=1$, rises sharply as $\sigma\to 0$, and also grows as $\sigma\to\infty$; the cross entropy has the same shape, shifted upward by the constant entropy $H(P)$. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->

### conditional cross entropy: derivation, interpretation, and use

For supervised learning, predictions are conditional on observed features, so the natural mismatch measure should compare true and model conditional label distributions given the same input. For a fixed input $x$, the relevant per-input mismatch is the ordinary cross entropy between the true label law $P(Y\mid x)$ and the model label law $Q(Y\mid x)$: $H\bigl(P(Y\mid x),Q(Y\mid x)\bigr)=\sum_y P(y\mid x)(-\log Q(y\mid x))$. This says: hold the input fixed, then ask how expensive it is to encode the true label distribution at that input using the model's predicted probabilities.

Conditional cross entropy is then obtained by averaging those per-input cross entropies over the true input distribution: $\mathbb{E}_{X\sim P}\Bigl[H\bigl(P(Y\mid X),Q(Y\mid X)\bigr)\Bigr] = \sum_x P(x)\sum_y P(y\mid x)(-\log Q(y\mid x)) = \sum_{x,y}P(x,y)(-\log Q(y\mid x)) = \mathbb{E}_{(X,Y)\sim P}\bigl[-\log Q(Y\mid X)\bigr]$. So the derivation is literal: first define the cross entropy for each fixed input, then average those cross entropies using how often each input occurs. The inner term answers "how good is the classifier at this input?" and the outer expectation answers "how important is this input region overall?"

The equivalent joint-distribution decomposition should be read only after all symbols are defined. Here $P_{X,Y}$ is the true joint distribution of inputs and labels, so $P_{X,Y}(x,y)=P(x,y)$ is the real probability of seeing input-label pair $(x,y)$. The marginal $P_X$ is obtained by summing out labels, so $P_X(x)=\sum_y P(x,y)$. The symbol $Q_{Y\mid X}$ denotes the model conditional label distribution, so $Q(y\mid x)$ is the model's predicted probability of label $y$ after seeing input $x$. From these pieces one builds the _hybrid_ joint distribution $P_XQ_{Y\mid X}$ defined by $(P_XQ_{Y\mid X})(x,y)=P_X(x)Q(y\mid x)$. Intuitively, this hybrid joint keeps the real frequency of inputs but replaces the true label law at each input by the model's predicted label law.

Now compute its cross entropy with the true joint distribution: $H\bigl(P_{X,Y},P_XQ_{Y\mid X}\bigr) = -\sum_{x,y} P(x,y)\log \bigl(P_X(x)Q(y\mid x)\bigr) = -\sum_{x,y} P(x,y)\log P_X(x) - \sum_{x,y} P(x,y)\log Q(y\mid x)$.

The first term is exactly $H(P_X)$ because summing $P(x,y)$ over $y$ gives $P_X(x)$. The second term is exactly $H_P(Y\mid X;Q)=\mathbb{E}_{(X,Y)\sim P}[-\log Q(Y\mid X)]$. Therefore $H\bigl(P_{X,Y},P_XQ_{Y\mid X}\bigr)=H(P_X)+H_P(Y\mid X;Q)$.

This decomposition gives the right context for why conditional cross entropy suddenly appears in classification. The model does not choose which inputs occur, so the input-entropy term $H(P_X)$ is fixed. The trainable part is only the conditional cross-entropy term $H_P(Y\mid X;Q)$. So the decomposition is exactly into _input entropy plus conditional cross entropy_, and only the second term is something the classifier can improve. Minimizing conditional cross entropy therefore means minimizing the joint coding cost after stripping off the input-uncertainty part that the model cannot control anyway.

A tiny weighting example makes the per-input view concrete. Suppose there are two input regions $a$ and $b$ with $P_X(a)=0.9$ and $P_X(b)=0.1$, and suppose the per-input cross entropies are $H(P(Y\mid a),Q(Y\mid a))=0.2$ and $H(P(Y\mid b),Q(Y\mid b))=1.0$. Then the conditional cross entropy is $0.9\cdot 0.2+0.1\cdot 1.0=0.28$, so common inputs dominate the objective more strongly than rare ones.

Interpretation and use: conditional cross entropy naturally penalizes assigning low probability to true labels on frequent inputs, so it is the standard population objective for conditional probabilistic classifiers such as logistic and softmax regression. It is the natural quantity because the model controls $Q(Y\mid X)$, not the input marginal $P_X$; one should therefore measure only the label-prediction quality conditional on the given input. Empirical training loss is its finite-sample estimator.

---

Flashcards for this section are as follows:

- per-input cross entropy at fixed input $x$ ::@:: For a fixed input $x$, the label-prediction mismatch is $H\bigl(P(Y\mid x),Q(Y\mid x)\bigr)=\sum_y P(y\mid x)(-\log Q(y\mid x))$, which measures how costly it is to score the true label law at that input using model $Q$. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- conditional cross-entropy definition ::@:: The population conditional cross entropy is $H_P(Y\mid X;Q)=\mathbb{E}_{(X,Y)\sim P}\bigl[-\log Q(Y\mid X)\bigr]=\mathbb{E}_{X\sim P}\Bigl[H\bigl(P(Y\mid X),Q(Y\mid X)\bigr)\Bigr]$. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- conditional cross-entropy derivation (per-input to joint) ::@:: Start with the per-input cross entropy $H\bigl(P(Y\mid x),Q(Y\mid x)\bigr)$, average it by $P(x)$, and then use $P(x,y)=P(x)P(y\mid x)$ to obtain $\sum_{x,y}P(x,y)(-\log Q(y\mid x))=\mathbb{E}_{(X,Y)\sim P}[-\log Q(Y\mid X)]$.
- per-input interpretation with context ::@:: At each fixed input $x$, $H\bigl(P(Y\mid x),Q(Y\mid x)\bigr)$ measures label-distribution mismatch, and $P(x)$ tells how strongly that input region should influence total objective because common inputs should matter more than rare ones.
- hybrid-joint decomposition with notation and derivation ::@:: Here $P_{X,Y}(x,y)=P(x,y)$ is the true joint law of input-label pairs, $P_X(x)=\sum_y P(x,y)$ is the input marginal, $Q(y\mid x)$ is the model conditional label law, and $(P_XQ_{Y\mid X})(x,y)=P_X(x)Q(y\mid x)$ is the hybrid joint that keeps true input frequencies but replaces true label conditionals by model conditionals. Then $H(P_{X,Y},P_XQ_{Y\mid X})=-\sum_{x,y}P(x,y)\log(P_X(x)Q(y\mid x))=-\sum_{x,y}P(x,y)\log P_X(x)-\sum_{x,y}P(x,y)\log Q(y\mid x)=H(P_X)+H_P(Y\mid X;Q)$, so joint coding cost decomposes into input entropy plus conditional cross entropy, and only the second term is trainable. <!--SR:!2000-01-01,1,250!2026-04-10,3,250-->
- why conditional cross entropy is the natural objective ::@:: In a conditional classifier the learner controls $Q(Y\mid X)$ but not the input marginal $P_X$, so the right population objective is to average per-input label-prediction quality rather than to penalize the model for the distribution of inputs themselves.
- when conditional cross entropy is used ::@:: Use it whenever prediction is conditional ($Q(y\mid x)$), such as binary logistic regression, multiclass softmax regression, and other conditional probabilistic classifiers.
- anti-swap memory cue for conditional form ::@:: In $\mathbb{E}_{(X,Y)\sim P}[-\log Q(Y\mid X)]$, data are always sampled from true $P$ and model quality is always evaluated through $Q$ inside the logarithm. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- weighted-input example for conditional cross entropy ::@:: If $P_X(a)=0.9$, $P_X(b)=0.1$, and the per-input cross entropies are $0.2$ and $1.0$, then $H_P(Y\mid X;Q)=0.9\cdot 0.2+0.1\cdot 1.0=0.28$, so common inputs dominate the average more strongly than rare ones.

### likelihood and maximum likelihood

The likelihood section starts with a one-parameter toy model before returning to logistic regression. In the thumbtack setup, each throw is $X_i\in\{H,T\}$ with parameter $\theta=P(X=H)$. If the dataset has $m_H$ heads and $m_T$ tails, and observations are i.i.d. given $\theta$, then $L(\theta\mid D)=\prod_{i=1}^N P(X_i\mid \theta)=\theta^{m_H}(1-\theta)^{m_T}$.

It is helpful to interpret both sides explicitly. On the left, $L(\theta\mid D)$ means "likelihood as a function of parameter $\theta$ with observed data $D$ fixed." On the right, $\theta^{m_H}(1-\theta)^{m_T}$ comes from multiplying Bernoulli probabilities for each observation and grouping equal outcomes.

Taking logs gives $\ell(\theta\mid D)=m_H\log \theta + m_T\log(1-\theta)$. The derivative is $\frac{d\ell}{d\theta}=\frac{m_H}{\theta}-\frac{m_T}{1-\theta}$, and setting it to zero yields $\theta^{\ast}=\frac{m_H}{m_H+m_T}$. The second derivative $\frac{d^2\ell}{d\theta^2}=-\frac{m_H}{\theta^2}-\frac{m_T}{(1-\theta)^2}<0$ on $(0,1)$ confirms a maximum.

The optimizer $\theta^{\ast}=\frac{m_H}{m_H+m_T}$ also matches direct intuition: the most likely probability of heads should be the observed portion of heads. The MLE formalism confirms that this intuitive frequency estimate is not only plausible but exactly optimal for this model.

There is also a useful balancing interpretation. If a candidate $\theta$ is larger than the observed head fraction $\frac{m_H}{N}$, then the model is trying to explain the data with too many expected heads and too few expected tails; if $\theta$ is smaller than $\frac{m_H}{N}$, it does the opposite. The maximum occurs exactly where the model's Bernoulli head rate matches the empirical head rate seen in the sample.

Consistency adds an asymptotic guarantee. If data are truly i.i.d. Bernoulli with parameter $\theta_0$, then $\hat\theta_{\mathrm{MLE}}=\frac{m_H}{N}$ with $N=m_H+m_T$ converges to $\theta_0$ as $N\to\infty$ by the law of large numbers (in probability, and in fact almost surely). Equivalently, the per-sample log-likelihood satisfies $\frac{1}{N}\ell(\theta\mid D)=\frac{m_H}{N}\log \theta + \frac{m_T}{N}\log(1-\theta) \to \theta_0\log \theta + (1-\theta_0)\log(1-\theta)$, whose unique maximizer is $\theta=\theta_0$. So as sample size grows, the empirical optimum and the population optimum line up.

This toy problem transfers directly to logistic regression: i.i.d. product likelihood, log transform to sums, optimize parameters by maximizing data probability under the model, and then reinterpret the result as minimizing negative log-likelihood.

---

Flashcards for this section are as follows:

- likelihood ::@:: The likelihood of a parameter value is the probability the model assigns to the observed dataset when that parameter value is used. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- maximum likelihood estimation ::@:: Maximum likelihood estimation chooses the parameter value that maximizes the likelihood of the observed data.
- why the i.i.d. assumption matters ::@:: Under the i.i.d. assumption, the likelihood of the full dataset factors into a product of per-example probabilities.
- thumbtack likelihood with lhs-rhs interpretation ::@:: $L(\theta\mid D)=\theta^{m_H}(1-\theta)^{m_T}$ means lhs is a function of unknown parameter $\theta$ with observed data $D$ fixed, while rhs is the i.i.d. Bernoulli product grouped by counts.
- thumbtack log-likelihood ::@:: The thumbtack log-likelihood is $\ell(\theta\mid D)=m_H\log \theta + m_T\log(1-\theta)$, equivalent to likelihood maximization because $\log(\cdot)$ is strictly increasing.
- thumbtack first-order condition ::@:: Setting $\frac{d\ell}{d\theta}=\frac{m_H}{\theta}-\frac{m_T}{1-\theta}=0$ gives $\theta^{\ast}=\frac{m_H}{m_H+m_T}$.
- thumbtack second-order check ::@:: Since $\frac{d^2\ell}{d\theta^2}=-\frac{m_H}{\theta^2}-\frac{m_T}{(1-\theta)^2}<0$ on $(0,1)$, the stationary point is a maximum.
- why the thumbtack MLE matches intuition ::@:: The MLE $\hat\theta=\frac{m_H}{m_H+m_T}$ equals the observed head proportion because any larger $\theta$ expects too many heads and any smaller $\theta$ expects too few, so the likelihood is maximized when model head rate matches empirical head rate. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
- thumbtack consistency as sample size grows ::@:: If $X_i\sim\mathrm{Bernoulli}(\theta_0)$ i.i.d., then $\hat\theta=\frac{m_H}{N}\to\theta_0$ as $N\to\infty$ by the law of large numbers, so the sample head fraction and the MLE both stabilize at the true parameter. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- per-sample log-likelihood limit ::@:: Since $\frac{1}{N}\ell(\theta\mid D)=\frac{m_H}{N}\log \theta+\frac{m_T}{N}\log(1-\theta)$ and $\frac{m_H}{N}\to\theta_0$, the large-sample objective converges to $\theta_0\log \theta+(1-\theta_0)\log(1-\theta)$, whose maximizer is the true parameter $\theta_0$.

## cross entropy for logistic regression

Now return to the binary classifier. For one training example $(x_i,y_i)$, let $z_i=w^\top x_i$ be the score and let $p_i=P(y_i=1\mid x_i,w)=\sigma(z_i)$ be the predicted positive-class probability. Because $y_i\in\{0,1\}$, the Bernoulli likelihood of the observed label can be written compactly as $P(y_i\mid x_i,w)=p_i^{y_i}(1-p_i)^{1-y_i}$. Taking the negative logarithm and expanding the product powers gives $\ell_i(w)=-\log P(y_i\mid x_i,w)=-\log\bigl(p_i^{y_i}(1-p_i)^{1-y_i}\bigr)=-\bigl(y_i\log p_i+(1-y_i)\log(1-p_i)\bigr)$.

This is the _per-example logistic loss_: the penalty attached to a single observed training pair $(x_i,y_i)$ under the current parameter vector $w$.

For a dataset of $N$ examples, the total negative log-likelihood is the sum of the per-example losses, and the dataset loss used in training is their average: $L(w)=\frac{1}{N}\sum_{i=1}^N \ell_i(w)= -\frac{1}{N}\sum_{i=1}^N \log P(y_i\mid x_i,w)= -\frac{1}{N}\sum_{i=1}^N \bigl(y_i\log p_i+(1-y_i)\log(1-p_i)\bigr)$.

So the per-example loss answers "how bad is the model on one training point?" while the dataset loss answers "what is the average badness over the whole sample?" This is exactly the objective written in the slides. Therefore, minimizing cross entropy is the same as maximizing the conditional likelihood of the observed labels under the logistic model.

The formula is also easy to interpret. If the true label is $1$, then the loss contributes $-\log p_i$, which is small only when $p_i$ is close to $1$. If the true label is $0$, then the contribution is $-\log (1-p_i)$, which is small only when $p_i$ is close to $0$. So the same predicted probability can be either good or disastrous depending on the true label.

This loss is usually called _binary cross entropy_ (BCE). It is the cross entropy between two Bernoulli distributions: the true binary-label distribution and the model's Bernoulli output distribution. In supervised learning, BCE is used for binary classification problems such as logistic regression and sigmoid-output neural networks. Conceptually, it is a special case of ordinary cross entropy, a special case of conditional cross entropy when labels are binary, and also the two-class special case of categorical cross entropy.

This is what "penalty for confident mistakes" really means. If $y_i=1$ and the model predicts $p_i=0.9$, then the loss is $-\log 0.9\approx 0.105$, which is small. But if $y_i=1$ and the model predicts $p_i=0.01$, then the loss becomes $-\log 0.01\approx 4.605$, which is huge. Symmetrically, if $y_i=0$ and the model predicts $p_i=0.1$, then the loss is $-\log 0.9\approx 0.105$, but if $y_i=0$ and the model predicts $p_i=0.99$, then the loss is $-\log 0.01\approx 4.605$. Confident correct predictions are rewarded with tiny loss, while confident incorrect predictions are punished very aggressively.

---

Flashcards for this section are as follows:

- per-example logistic loss with notation and derivation ::@:: For one example $(x_i,y_i)$ with score $z_i=w^\top x_i$ and predicted positive-class probability $p_i=\sigma(z_i)=P(y_i=1\mid x_i,w)$, the Bernoulli likelihood is $P(y_i\mid x_i,w)=p_i^{y_i}(1-p_i)^{1-y_i}$, so the per-example loss is $\ell_i(w)=-\log P(y_i\mid x_i,w)=-\log\bigl(p_i^{y_i}(1-p_i)^{1-y_i}\bigr)=-\bigl(y_i\log p_i+(1-y_i)\log(1-p_i)\bigr)$.
- dataset logistic loss with notation and derivation ::@:: For a dataset of $N$ training examples, the dataset loss is the average per-example loss $L(w)=\frac{1}{N}\sum_{i=1}^N \ell_i(w)=-\frac{1}{N}\sum_{i=1}^N \log P(y_i\mid x_i,w)=-\frac{1}{N}\sum_{i=1}^N \bigl(y_i\log p_i+(1-y_i)\log(1-p_i)\bigr)$, where the factor $1/N$ turns total loss into average loss per example.
- binary cross entropy definition and use: Given a true binary label distribution with parameter $y\in\{0,1\}$ (or Bernoulli mean $r$) and a model Bernoulli prediction $p$, what is binary cross entropy, what is it used for, and what is it a special case of? ::@:: Binary cross entropy is $-\bigl(y\log p+(1-y)\log(1-p)\bigr)$ in the observed-label form, or $-\bigl(r\log p+(1-r)\log(1-p)\bigr)$ for Bernoulli parameters. It is used for binary classification models such as logistic regression and sigmoid-output neural networks. It is the cross entropy between two Bernoulli distributions, hence a special case of ordinary cross entropy, of conditional cross entropy for binary labels, and of categorical cross entropy with two classes. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- why cross entropy equals negative log-likelihood ::@:: In logistic regression the Bernoulli label model makes the average negative log-likelihood exactly equal to the average cross-entropy loss.
- case $y_i=1$ in logistic loss ::@:: When the true label is $1$, the per-example cross entropy reduces to $-\log p_i$, so the loss is small only if the model gives the positive class high probability.
- case $y_i=0$ in logistic loss ::@:: When the true label is $0$, the per-example cross entropy reduces to $-\log (1-p_i)$, so the loss is small only if the model gives the positive class low probability.
- penalty for confident mistakes ::@:: Cross entropy punishes confident wrong predictions heavily because $-\log p_i$ and $-\log(1-p_i)$ become very large when the model assigns tiny probability to the true label.
- worked confident-mistake example for $y_i=1$ ::@:: If $y_i=1$, then predicting $p_i=0.9$ gives loss $-\log 0.9\approx 0.105$, but predicting $p_i=0.01$ gives loss $-\log 0.01\approx 4.605$, so a confident mistake is penalized far more than a mild error. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- worked confident-mistake example for $y_i=0$ ::@:: If $y_i=0$, then predicting $p_i=0.1$ gives loss $-\log 0.9\approx 0.105$, but predicting $p_i=0.99$ gives loss $-\log 0.01\approx 4.605$, so cross entropy strongly punishes assigning near-certainty to the wrong class.

### population risk versus empirical loss

The conditional cross entropy $\mathbb{E}_P[-\log Q(y\mid x)]$ is a population quantity defined with respect to the unknown true data-generating distribution. Since $P(x,y)$ is unavailable, the learner replaces that expectation by the empirical distribution of the sample. For training data $D=\{(x_i,y_i)\}_{i=1}^N$, define the empirical distribution by $\hat P_N = \frac{1}{N}\sum_{i=1}^N \delta_{(x_i,y_i)}$, where $\delta_{(x_i,y_i)}$ is a point mass at the observed pair $(x_i,y_i)$. This empirical measure gives each observed training example weight $1/N$.

For any test function $f(x,y)$, expectation under the empirical distribution is just the sample average: $\mathbb{E}_{\hat P_N}[f(X,Y)] = \frac{1}{N}\sum_{i=1}^N f(x_i,y_i)$. Applying this to $f(x,y)=-\log Q(y\mid x)$ gives $\mathbb{E}_{\hat P_N}[-\log Q(Y\mid X)] = \frac{1}{N}\sum_{i=1}^N -\log Q(y_i\mid x_i)$, which is exactly the usual training loss. So the factor $1/N$ is not an arbitrary normalization trick; it appears because the empirical distribution is itself an average of $N$ equally weighted point masses.

This also explains the large-sample intuition. If the data are i.i.d. from the true distribution $P$ and the loss function is integrable, then the law of large numbers gives $\mathbb{E}_{\hat P_N}[-\log Q(Y\mid X)] \to \mathbb{E}_{P}[-\log Q(Y\mid X)]$ as $N\to\infty$. In words, empirical averages become reliable approximations to true expectations when enough independent data are observed. That is why empirical risk minimization makes sense: the finite-sample objective is a consistent estimator of the population objective.

A tiny numerical example makes the averaging intuition concrete. Suppose the per-example negative log-likelihoods are $0.2$, $0.4$, $0.1$, and $1.3$. Then the empirical loss is $\frac{0.2+0.4+0.1+1.3}{4}=0.5$. The large value $1.3$ matters, but only through its contribution to the average, which is exactly how the empirical distribution weights observations.

This distinction is important conceptually. The theoretical goal is closeness to the true conditional distribution, but the practical optimization problem is built from finite data. The training objective is therefore an empirical estimate of the desired population cross entropy.

---

Flashcards for this section are as follows:

- population conditional cross entropy ::@:: The population objective is $\mathbb{E}_P[-\log Q(y\mid x)]$, where $P$ is the unknown true distribution and $Q$ is the learned conditional model. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- empirical distribution ::@:: For data $D=\{(x_i,y_i)\}_{i=1}^N$, the empirical distribution is $\hat P_N=\frac{1}{N}\sum_{i=1}^N \delta_{(x_i,y_i)}$, which assigns equal mass $1/N$ to each observed example.
- empirical expectation equals sample average ::@:: For any function $f$, one has $\mathbb{E}_{\hat P_N}[f(X,Y)] = \frac{1}{N}\sum_{i=1}^N f(x_i,y_i)$, so empirical risk is literally expectation under the empirical distribution. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- empirical approximation of conditional cross entropy ::@:: In practice, conditional cross entropy is estimated by $\mathbb{E}_{\hat P_N}[-\log Q(Y\mid X)] = \frac{1}{N}\sum_{i=1}^N -\log Q(y_i\mid x_i)$. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- why the factor $1/N$ appears ::@:: The factor $1/N$ appears because the empirical distribution gives each of the $N$ observed examples equal probability mass $1/N$, so its expectation is an average rather than a raw sum.
- consistency of empirical risk ::@:: If samples are i.i.d. from $P$, then by the law of large numbers the empirical average $\mathbb{E}_{\hat P_N}[f]$ converges to the population expectation $\mathbb{E}_P[f]$, so empirical conditional cross entropy consistently estimates the true population loss. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- why logistic training is empirical risk minimization ::@:: Logistic training is empirical risk minimization because it minimizes a sample-average loss under $\hat P_N$ in order to approximate minimization of the population loss under $P$.
- worked empirical-loss example ::@:: If the per-example losses are $0.2$, $0.4$, $0.1$, and $1.3$, then the empirical loss is their average $\frac{0.2+0.4+0.1+1.3}{4}=0.5$.
- why finite-sample loss is only an estimate ::@:: The training loss is only an estimate of the population objective because it is computed from finitely many observations; as $N\to\infty$, the sample average is expected to settle toward the true expectation. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->

## gradient descent for logistic regression

Unlike ordinary least squares, logistic regression does not yield a simple closed-form normal-equation solution. The loss is convex, but the sigmoid and logarithm make the stationary-point equations nonlinear in the parameters. So the lecture introduces gradient descent as the practical optimization method.

This section stays focused on the binary model. The key pattern to remember is that logistic regression already contains the whole output-layer training template: define a probabilistic prediction rule, convert negative log-likelihood into a loss, differentiate it, and update by gradients. A later section will show that the same template extends almost unchanged to multiclass softmax regression.

---

Flashcards for this section are as follows:

- why gradient descent is used in logistic regression ::@:: Logistic regression is trained numerically because its likelihood-based objective does not reduce to the simple normal-equation solution used in ordinary least squares. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- why no normal equation appears ::@:: Logistic regression lacks the least-squares-style normal equation because the stationarity condition is nonlinear in the weights. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- output-layer training template ::@:: The reusable pattern is: compute scores, transform them into a valid probability model, write the negative log-likelihood, differentiate it, and update by gradients; multiclass softmax later reuses exactly this template.

### gradient descent basics

For a scalar function $L(w)$, the derivative measures local slope and suggests how to change $w$ to reduce the function value. If $L'(w) > 0$, decreasing $w$ tends to reduce the loss; if $L'(w) < 0$, increasing $w$ tends to reduce the loss. This intuition leads to the update rule $w \leftarrow w - \alpha L'(w)$, where $\alpha$ is the step size or learning rate.

For vector parameters $w=(w_0,\ldots,w_D)^\top$, the derivative generalizes to the gradient $\nabla L(w)$. A first-order approximation explains the update direction: $L(w+\Delta w) \approx L(w)+\nabla L(w)^\top \Delta w$. If one chooses $\Delta w=-\alpha \nabla L(w)$, then the linearized change becomes $L(w+\Delta w)-L(w)\approx -\alpha\lVert \nabla L(w)\rVert^2 \le 0$. So the negative gradient is the direction that most immediately decreases the loss under this local approximation. Gradient descent therefore uses $w \leftarrow w - \alpha \nabla L(w)$. The lecture stresses that the learning rate is crucial: if it is too small, convergence is painfully slow; if it is too large, the optimization can oscillate or diverge.

A tiny scalar example is $L(w)=w^2$, whose derivative is $L'(w)=2w$. Gradient descent gives $w\leftarrow w-2\alpha w=(1-2\alpha)w$. So if $0<\alpha<1$, the iterate shrinks toward $0$, illustrating the basic idea that one repeatedly moves opposite the local slope.

The slides also make a practical remark that remains important in deep learning: gradient descent is not guaranteed to avoid every bad critical region. In more complicated objectives it can get stuck near local minima or saddle points. Even so, it often works well enough to be the workhorse training method.

---

Flashcards for this section are as follows:

- scalar gradient-descent update ::@:: For a scalar parameter, gradient descent updates by $w \leftarrow w - \alpha L'(w)$.
- vector gradient-descent update ::@:: For vector parameters, gradient descent updates by $w \leftarrow w - \alpha \nabla L(w)$ because the negative gradient is the local steepest-descent direction under the first-order approximation of the loss. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- why negative gradient is chosen ::@:: Since $L(w+\Delta w)\approx L(w)+\nabla L(w)^\top\Delta w$, choosing $\Delta w=-\alpha\nabla L(w)$ gives approximate change $-\alpha\lVert\nabla L(w)\rVert^2\le 0$, so the loss locally decreases.
- learning rate ::@:: The learning rate $\alpha$ controls how far each gradient-descent step moves in the descent direction, balancing progress against stability.
- too-small learning rate ::@:: If the learning rate is too small, convergence can be extremely slow.
- too-large learning rate ::@:: If the learning rate is too large, gradient descent can overshoot, oscillate, or fail to converge.
- local minima and saddle points ::@:: Gradient descent can in principle be slowed or trapped by local minima or saddle points, although it often works well in practice. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- scalar worked example ::@:: If $L(w)=w^2$, then $L'(w)=2w$ and the update becomes $w\leftarrow (1-2\alpha)w$, so repeated steps shrink $w$ toward $0$ when $0<\alpha<1$.

### chain-rule derivation and hand computation

To differentiate the logistic objective, the crucial identity is the derivative of the sigmoid: $\sigma'(z)=\sigma(z)(1-\sigma(z))$. Write the average loss as $L(w)=\frac{1}{N}\sum_{i=1}^N \ell_i(w)$ with $\ell_i(w)=-\bigl(y_i\log p_i+(1-y_i)\log(1-p_i)\bigr)$, $p_i=\sigma(z_i)$, and $z_i=w^\top x_i$. Then the chain rule factorizes the derivative into three local pieces:

$(1)$ score derivative $\frac{\partial z_i}{\partial w_j}=x_{i,j}$, <br/> $(2)$ sigmoid derivative $\frac{\partial p_i}{\partial z_i}=p_i(1-p_i)$, <br/> $(3)$ log-loss derivative $\frac{\partial \ell_i}{\partial p_i}= -\frac{y_i}{p_i}+\frac{1-y_i}{1-p_i}$.

Multiplying these pieces gives the coordinate gradient $\frac{\partial \ell_i}{\partial w_j}=\frac{\partial \ell_i}{\partial p_i}\frac{\partial p_i}{\partial z_i}\frac{\partial z_i}{\partial w_j}=\Bigl(-\frac{y_i}{p_i}+\frac{1-y_i}{1-p_i}\Bigr)p_i(1-p_i)x_{i,j}=(p_i-y_i)x_{i,j}$. The key memory rule is already visible: prediction minus target, then multiply by feature value. The next subsection rewrites the same simplification at the score level so the cancellation pattern can be seen more directly.

Averaging over $i$ yields the gradient component $\frac{\partial L(w)}{\partial w_j}=\frac{1}{N}\sum_{i=1}^N (p_i-y_i)x_{i,j} = -\frac{1}{N}\sum_{i=1}^N \bigl(y_i-\sigma(w^\top x_i)\bigr)x_{i,j}$. So the derivative of the average loss is just the average of the per-example derivatives.

Equivalently, if $p_i = \sigma(w^\top x_i)$, then $\nabla L(w)=\frac{1}{N}\sum_{i=1}^N (p_i-y_i)x_i$. The batch gradient-descent update can therefore be written as $w_j \leftarrow w_j + \alpha \frac{1}{N}\sum_{i=1}^N (y_i-p_i)x_{i,j}$. This formula has an appealing interpretation: the correction is driven by prediction error times feature value.

If the true label is $1$ but the predicted probability is too small, then $y_i-p_i > 0$, so features with positive $x_{i,j}$ push the corresponding weights upward. If the predicted probability is too large, the sign reverses. The update is therefore not a mysterious formula; it is an error-correction rule aligned with the data.

For hand computation, it helps to organize each gradient step as a small table. A practical workflow is: (1) write down the current parameter vector $w$ and all training pairs $(x_i,y_i)$, (2) compute each score $z_i=w^\top x_i$, (3) convert scores to probabilities $p_i=\sigma(z_i)$, (4) compute residuals $p_i-y_i$, (5) multiply each residual by the relevant feature value $x_{i,j}$ if computing one coordinate, or by the whole feature vector $x_i$ if computing the full gradient, (6) average those contributions over all examples to obtain $\nabla L(w)$, and only then (7) update by $w_{\text{new}}=w-\alpha\nabla L(w)$. In coordinate form, a good table uses columns $(x_i,y_i,z_i,p_i,p_i-y_i,(p_i-y_i)x_{i,0},\ldots,(p_i-y_i)x_{i,D})$ so that the average gradient can be read off by averaging each contribution column separately. This is much easier than trying to differentiate and update in one mental jump.

A tiny worked example illustrates the workflow. Take augmented inputs $x_1=(1,2)^\top$, $y_1=1$ and $x_2=(1,-1)^\top$, $y_2=0$, and start from $w=(0,0)^\top$. Then $z_1=z_2=0$, so $p_1=p_2=0.5$. The average gradient is $\nabla L(w)=\frac{1}{2}\Bigl((0.5-1)(1,2)^\top + (0.5-0)(1,-1)^\top\Bigr)=\frac{1}{2}\bigl((-0.5,-1)+(0.5,-0.5)\bigr)^\top=(0,-0.75)^\top$.

With learning rate $\alpha=0.1$, the update is $w_{\text{new}}=w-\alpha\nabla L(w)=(0,0)^\top-0.1(0,-0.75)^\top=(0,0.075)^\top$. The second weight becomes positive because, across these two examples, increasing the score with the second feature helps separate the labels better.

---

Flashcards for this section are as follows:

- sigmoid derivative ::@:: The sigmoid derivative is $\sigma'(z)=\sigma(z)(1-\sigma(z))$. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- coordinate logistic gradient with notation ::@:: For one example, let $z_i=w^\top x_i$, $p_i=\sigma(z_i)$, and $\ell_i(w)=-\bigl(y_i\log p_i+(1-y_i)\log(1-p_i)\bigr)$. Then the coordinate gradient is $\frac{\partial \ell_i}{\partial w_j}=(p_i-y_i)x_{i,j}$, so each weight coordinate sees the residual $p_i-y_i$ scaled by the corresponding feature value $x_{i,j}$.
- logistic-loss gradient vector ::@:: Writing $p_i=\sigma(w^\top x_i)$, the logistic-regression gradient is $\nabla L(w)=\frac{1}{N}\sum_{i=1}^N (p_i-y_i)x_i$, so each example contributes residual times feature vector.
- batch update for logistic regression ::@:: A batch gradient-descent update for logistic regression is $w_j \leftarrow w_j + \alpha \frac{1}{N}\sum_{i=1}^N (y_i-p_i)x_{i,j}$, equivalently $w\leftarrow w-\alpha\nabla L(w)$. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- why the update looks like error times input ::@:: Logistic-regression weight updates are driven by prediction error $(y_i-p_i)$ multiplied by the corresponding feature value, so they correct the score in the direction suggested by the data.
- effect when the model underpredicts class $1$ ::@:: If $y_i=1$ and $p_i$ is too small, then $(y_i-p_i)$ is positive, so positively valued features push the relevant weights upward.
- hand-computation workflow for one gradient step ::@:: Given current parameters $w$ and training pairs $(x_i,y_i)$, compute in order: (1) scores $z_i=w^\top x_i$, (2) probabilities $p_i=\sigma(z_i)$, (3) residuals $p_i-y_i$, (4) feature-weighted residuals $(p_i-y_i)x_{i,j}$ or vectors $(p_i-y_i)x_i$, (5) the average gradient $\nabla L(w)=\frac1N\sum_i (p_i-y_i)x_i$, and then (6) the update $w_{\text{new}}=w-\alpha\nabla L(w)$.
- worked logistic-gradient step ::@:: If $x_1=(1,2)^\top$, $y_1=1$, $x_2=(1,-1)^\top$, $y_2=0$, and $w=(0,0)^\top$, then $p_1=p_2=0.5$ and $\nabla L(w)=\frac12\bigl((0.5-1)(1,2)^\top+(0.5-0)(1,-1)^\top\bigr)=(0,-0.75)^\top$.
- worked logistic update from the tiny example ::@:: If $x_1=(1,2)^\top$, $y_1=1$, $x_2=(1,-1)^\top$, $y_2=0$, the current parameter is $w=(0,0)^\top$, and the learning rate is $\alpha=0.1$, then $z_1=z_2=0$, $p_1=p_2=0.5$, the average gradient is $\nabla L(w)=\frac12\bigl((0.5-1)(1,2)^\top+(0.5-0)(1,-1)^\top\bigr)=(0,-0.75)^\top$, and the update is $w_{\text{new}}=(0,0)^\top-0.1(0,-0.75)^\top=(0,0.075)^\top$. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->

### score-level cancellation and residual form

The previous subsection already derived the gradient coordinatewise. This subsection revisits the same result at the score level, because the algebraic cancellation here is the reusable pattern that reappears in softmax layers and neural-network backpropagation. For one example with score $z_i=w^\top x_i$, probability $p_i=\sigma(z_i)$, and loss $\ell_i(w)=-\bigl(y_i\log p_i + (1-y_i)\log(1-p_i)\bigr)$, differentiating with respect to $z_i$ gives $\frac{\partial \ell_i}{\partial z_i} = -\Bigl(y_i\frac{1}{p_i}\frac{\partial p_i}{\partial z_i} + (1-y_i)\frac{1}{1-p_i}\frac{\partial(1-p_i)}{\partial z_i}\Bigr) = -\Bigl(y_i\frac{1}{p_i}p_i(1-p_i) - (1-y_i)\frac{1}{1-p_i}p_i(1-p_i)\Bigr) = p_i-y_i$.

Then use $\frac{\partial z_i}{\partial w}=x_i$ to get $\nabla_w\ell_i = (p_i-y_i)x_i$. Averaging over examples yields $\nabla L(w)=\frac{1}{N}\sum_{i=1}^N (p_i-y_i)x_i$. So this subsection does not introduce a new formula; it isolates the reusable cancellation pattern that also reappears in softmax layers and neural-network backpropagation.

This algebraic collapse from a longer expression to $(p_i-y_i)x_i$ is more than cosmetic. It says logistic regression behaves like a calibrated residual model: _predicted probability minus observed label_, scaled by the input features.

---

Flashcards for this section are as follows:

- one-example logistic score-derivative identity ::@:: For one example, differentiating Bernoulli cross entropy with respect to the score $z_i=w^\top x_i$ gives $\frac{\partial \ell_i}{\partial z_i}=p_i-y_i$.
- why the gradient simplifies so cleanly ::@:: The simplification comes from combining the sigmoid derivative $p_i(1-p_i)$ with the logarithmic derivatives in cross entropy, causing many terms to cancel and leaving the clean residual form $p_i-y_i$.
- residual-form interpretation after score differentiation ::@:: Once $\frac{\partial \ell_i}{\partial z_i}=p_i-y_i$ is known, using $\frac{\partial z_i}{\partial w}=x_i$ gives $\nabla_w\ell_i=(p_i-y_i)x_i$, so the residual tells how much the model overpredicts or underpredicts the positive class and $x_i$ converts that scalar correction into a parameter-space direction.

### convexity and Hessian structure

Logistic regression has no closed-form minimizer like ordinary least squares, but its objective is still convex. Start from the gradient $\nabla L(w)=\frac{1}{N}\sum_{i=1}^N (p_i-y_i)x_i$, where $p_i=\sigma(w^\top x_i)$. Since only $p_i$ depends on $w$, differentiating once more gives $\nabla^2 L(w)=\frac{1}{N}\sum_{i=1}^N \nabla p_i\, x_i^\top$. Now $\nabla p_i = \sigma'(w^\top x_i)x_i = p_i(1-p_i)x_i$, so $\nabla^2 L(w)=\frac{1}{N}\sum_{i=1}^N p_i(1-p_i)x_ix_i^\top = \frac{1}{N}X^\top R X$, where $R$ is a diagonal matrix with entries $r_i=p_i(1-p_i)\in(0,\tfrac14]$. To verify positive semidefiniteness, take any vector $v$ and compute $v^\top \nabla^2 L(w) v = \frac{1}{N}\sum_{i=1}^N p_i(1-p_i)(x_i^\top v)^2 \ge 0$. So the Hessian is positive semidefinite and the loss is convex in $w$. The curvature is largest when $p_i=0.5$, because then $p_i(1-p_i)=\tfrac14$, and it becomes small when $p_i$ is near $0$ or $1$. This matches the intuition that the loss bends most strongly when the classifier is uncertain and flattens when the sigmoid is saturated.

This matters operationally: any stationary point is a global minimizer, so optimization concerns are about speed and conditioning rather than about bad local minima. Numerical methods are still needed, but the geometry is much nicer than in many nonconvex deep models.

---

Flashcards for this section are as follows:

- logistic-regression Hessian form ::@:: The Hessian of logistic cross entropy is $\nabla^2 L(w)=\frac{1}{N}\sum_i p_i(1-p_i)x_ix_i^\top = \frac{1}{N}X^\top R X$ with $R_{ii}=p_i(1-p_i)$.
- Hessian derivation for logistic loss: Starting from $\nabla L(w)=\frac1N\sum_i (p_i-y_i)x_i$ with $p_i=\sigma(w^\top x_i)$, derive the Hessian ::@:: Since only $p_i$ depends on $w$, differentiate once more: $\nabla^2L(w)=\frac1N\sum_i \nabla p_i\,x_i^\top$. Using $\nabla p_i=\sigma'(w^\top x_i)x_i=p_i(1-p_i)x_i$ gives $\nabla^2L(w)=\frac1N\sum_i p_i(1-p_i)x_ix_i^\top=\frac1N X^\top R X$ with $R_{ii}=p_i(1-p_i)$.
- why logistic loss is convex: Given $\nabla^2L(w)=\frac1N\sum_i p_i(1-p_i)x_ix_i^\top$, why is it positive semidefinite? ::@:: For any vector $v$, $v^\top\nabla^2L(w)v=\frac1N\sum_i p_i(1-p_i)(x_i^\top v)^2\ge 0$ because $p_i(1-p_i)\ge 0$ and squares are nonnegative; therefore the Hessian is positive semidefinite and the loss is convex.
- curvature intuition from $p_i(1-p_i)$ ::@:: The curvature factor $p_i(1-p_i)$ is largest at $p_i=0.5$ and small near $p_i=0$ or $1$, so logistic loss bends most strongly when the classifier is uncertain and flattens when the sigmoid saturates. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- optimization implication of convex logistic loss ::@:: Convexity implies any stationary point is globally optimal, so training focuses on efficient numerical convergence rather than escaping local minima.

### batch and stochastic gradient descent

Batch gradient descent uses all $N$ examples to compute each update. This gives the exact full gradient, but it can be expensive when the dataset is large. At the opposite extreme, the _per-sample_ gradient for one example $i$ is $g_i=(p_i-y_i)x_i$, which is the gradient contribution from that single training pair. If one updates using only one such example at a time, one gets the single-example version of stochastic gradient descent.

The lecture therefore introduces stochastic gradient descent in its more practical minibatch form: choose a subset $B \subseteq \{1,\ldots,N\}$ and update using only the examples in that subset. The method is called _stochastic_ because the index $i$ in the single-example case, or the minibatch $B$ in the minibatch case, is chosen randomly. As a result, the update direction is itself a random vector: it is a noisy estimate of the full gradient rather than the exact full gradient.

The resulting update has the same form as batch descent except that the sum runs over $B$ and is normalized by $|B|$ instead of $N$. When $|B|=1$, the method becomes single-example stochastic gradient descent. When $|B|$ is moderate, one gets minibatch gradient descent, which balances noisy but cheap updates against stable but expensive full-gradient steps. So the comparison is:

- per-sample gradient: cheapest, most noisy;
- batch gradient descent: most expensive, no sampling noise;
- stochastic/minibatch gradient descent: random but cheaper gradient estimates that trade exactness for speed.

---

Flashcards for this section are as follows:

- batch gradient descent ::@:: Batch gradient descent computes each update using all $N$ training examples.
- why batch updates can be costly ::@:: Batch updates can be expensive because each step requires a pass through the full dataset.
- per-sample versus batch versus stochastic gradients: If the per-example logistic gradient is $g_i=(p_i-y_i)x_i$, how do per-sample, batch, and stochastic-gradient updates compare? ::@:: A per-sample update uses one $g_i$ from one training example; batch gradient descent uses the full average $\frac1N\sum_{i=1}^N g_i$; stochastic gradient descent uses a random example or a random minibatch $B$ to form $\frac1{|B|}\sum_{i\in B} g_i$, so minibatches are just the practical multi-example form of stochastic gradient descent.
- why stochastic gradient descent is stochastic ::@:: Stochastic gradient descent is stochastic because the example index $i$ or minibatch $B$ used at each step is chosen randomly, so the update direction is a random vector and only a noisy estimate of the full gradient.
- stochastic gradient descent and minibatches ::@:: Stochastic gradient descent updates parameters using randomly chosen data rather than the whole dataset; the single-example case uses one training pair, and the minibatch case uses a small random subset $B$ with update $\frac{1}{|B|}\sum_{i\in B}(y_i-p_i)x_{i,j}$. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->

### l2 regularization in logistic regression

Just as ridge regression stabilizes linear regression, $L_2$ regularization stabilizes logistic regression. The regularized objective becomes $L_{\mathrm{reg}}(w)=L(w)+\frac{\lambda}{2}\lVert w\rVert_2^2$. The new term discourages large weights, which can otherwise make the model overly sensitive to fluctuations in the training sample.

The factor $\frac12$ is worth comparing with the linear-regression convention used elsewhere in the course notes. In the linear-regression note, ridge was written as $J(w)+\lambda\lVert w\rVert_2^2$, whose gradient contributes $2\lambda w$. Here logistic regression uses $L(w)+\frac{\lambda}{2}\lVert w\rVert_2^2$, whose gradient contributes only $\lambda w$. So the extra factor $\frac12$ is not a new kind of regularization; it is only a bookkeeping convention chosen to cancel the derivative of the square and make the gradient formula cleaner. One can move between the two conventions by rescaling $\lambda$.

Differentiating the penalty makes the algebra explicit: because $\lVert w\rVert_2^2=\sum_j w_j^2$, one has $\frac{\partial}{\partial w_j}\frac{\lambda}{2}\lVert w\rVert_2^2 = \frac{\lambda}{2}\cdot 2w_j = \lambda w_j$, so in vector form $\nabla_w\bigl(\frac{\lambda}{2}\lVert w\rVert_2^2\bigr)=\lambda w$. Consequently, the update becomes a combination of data fit and weight shrinkage. In coordinate form, one can write $w_j \leftarrow w_j + \alpha \Bigl(\frac{1}{|B|}\sum_{i\in B}(y_i-p_i)x_{i,j} - \lambda w_j\Bigr)$. The regularizer therefore pulls weights toward zero on every step. The geometric intuition is unchanged across conventions: regardless of whether one writes $\lambda\lVert w\rVert_2^2$ or $\frac{\lambda}{2}\lVert w\rVert_2^2$, the penalty still makes large weights expensive and nudges the model toward smoother, smaller-norm parameter vectors.

Another useful intuition is to read the objective as a tug-of-war. The data-fit term tries to move the classifier toward whatever weights best explain the observed labels, while the $L_2$ term pulls the weight vector back toward the origin. Larger $\lambda$ means the shrinkage force is stronger, so the fitted decision boundary becomes less sensitive to sample noise and extreme feature directions.

---

Flashcards for this section are as follows:

- L2-regularized logistic objective ::@:: The $L_2$-regularized logistic objective is $L_{\mathrm{reg}}(w)=L(w)+\frac{\lambda}{2}\lVert w\rVert_2^2$.
- why L2 regularization helps logistic regression ::@:: $L_2$ regularization discourages large weights, which helps reduce overfitting and stabilizes the classifier. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- why logistic notes use $\frac{\lambda}{2}\lVert w\rVert_2^2$: If logistic regression uses $L_{\mathrm{reg}}(w)=L(w)+\frac{\lambda}{2}\lVert w\rVert_2^2$ while the linear-regression note uses $J(w)+\lambda\lVert w\rVert_2^2$, what is the difference? ::@:: The factor $\frac12$ is only a convention to cancel the derivative of the square: $\nabla\bigl(\frac{\lambda}{2}\lVert w\rVert_2^2\bigr)=\lambda w$, whereas $\nabla\bigl(\lambda\lVert w\rVert_2^2\bigr)=2\lambda w$. The regularization geometry is the same after rescaling $\lambda$.
- gradient derivation for logistic L2 regularization: If the penalty term is $\frac{\lambda}{2}\lVert w\rVert_2^2=\frac{\lambda}{2}\sum_j w_j^2$, what gradient does it contribute? ::@:: Differentiating coordinatewise gives $\frac{\partial}{\partial w_j}\frac{\lambda}{2}\sum_k w_k^2 = \lambda w_j$, so the vector gradient is $\nabla_w\bigl(\frac{\lambda}{2}\lVert w\rVert_2^2\bigr)=\lambda w$.
- regularized logistic update ::@:: A regularized update can be written as $w_j \leftarrow w_j + \alpha \Bigl(\frac{1}{|B|}\sum_{i\in B}(y_i-p_i)x_{i,j} - \lambda w_j\Bigr)$.
- why regularization is called weight decay ::@:: The term $-\alpha \lambda w_j$ shrinks weights toward zero at each step, which is why $L_2$ regularization is often described as weight decay. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- tug-of-war intuition for logistic L2 regularization ::@:: The data-fit term pulls weights toward values that explain the labels, while the $L_2$ term pulls the weight vector back toward the origin; larger $\lambda$ means stronger shrinkage toward smaller-norm solutions.

### why the intercept is usually not regularized

In many implementations, the $L_2$ penalty is applied to slope coefficients but not to the intercept term. The reason mirrors linear regression: shrinking the intercept does not control local boundary complexity in the same way shrinking directional weights does. The intercept mainly shifts the decision boundary parallel to itself, while the non-bias weights control orientation and margin sensitivity to features.

There is also a probabilistic interpretation. If one writes the score as $z=b+w^\top x$, then at the reference point $x=0$ the model predicts $P(y=1\mid x=0)=\sigma(b)$. So the intercept $b$ sets the baseline log-odds and baseline class probability before any feature contribution is added. Penalizing $b$ therefore does not mainly reduce boundary complexity; instead it pushes the baseline class probability back toward $0.5$, which can be undesirable when the real class balance is not near $50\%$.

This is especially relevant for class-imbalance settings. A nonzero intercept often needs to absorb baseline log-odds. Penalizing it too strongly can force the model toward an artificial prior of roughly $50\%$ positives, even when the true class frequency is very different.

---

Flashcards for this section are as follows:

- why the logistic intercept is often excluded from L2 penalty ::@:: The intercept is often unpenalized because it mainly sets baseline log-odds, whereas coefficient regularization is what controls boundary sensitivity to features.
- baseline-probability interpretation of the intercept ::@:: If the score is $z=b+w^\top x$, then at $x=0$ the model predicts $P(y=1\mid x=0)=\sigma(b)$, so the intercept sets the baseline log-odds and baseline class probability before feature effects are added.
- intercept regularization and class imbalance ::@:: Over-penalizing the intercept can distort baseline class probabilities, especially when the true positive rate is far from $50\%$. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->

## softmax regression

Softmax regression extends logistic regression from two classes to $C$ classes. Instead of one scalar score, it computes one score per class. For multiclass labels $y \in \{1,\ldots,C\}$, softmax regression assigns one weight vector $w_c$ to each class, forms scores $z_c = w_c^\top x$, and predicts class probabilities by $P(y=c\mid x,W)=\frac{e^{z_c}}{\sum_{k=1}^C e^{z_k}} = \frac{e^{w_c^\top x}}{\sum_{k=1}^C e^{w_k^\top x}}$. When the same softmax head is attached to learned hidden features rather than directly to raw input $x$, it becomes the multiclass output layer of a [feedforward neural network](feedforward%20neural%20network.md).

The index notation should be read very explicitly. The symbol $c$ means "the specific class whose probability we are computing." The symbol $k$ in the denominator is a dummy class index that runs over _all_ classes from $1$ to $C$. So the numerator isolates one class, while the denominator adds the evidence of every class so the result becomes a normalized probability.

An overarching computational intuition is to view the softmax parameter matrix as a stack of class-specific weight vectors. Let $W\in\mathbb{R}^{C\times D}$ with row index $c$ (class index) and column index $f$ (feature index), so $W_{c,f}$ is feature-$f$ weight for class $c$. For example $i$, input feature vector is $x_i=(x_{i,1},\ldots,x_{i,D})^\top$, and each class score is a row-vector inner product: $z_{i,c}=\sum_{f=1}^D W_{c,f}x_{i,f}=w_c^\top x_i$. Then compute probabilities $p_{i,c}=\frac{e^{z_{i,c}}}{\sum_{k=1}^C e^{z_{i,k}}}$, choose a target distribution $r_{i,c}$ over classes with $r_{i,c}\ge 0$ and $\sum_c r_{i,c}=1$, define one-example loss $\ell_i=-\sum_c r_{i,c}\log p_{i,c}$, and obtain row-gradient $\frac{\partial \ell_i}{\partial w_c}=(p_{i,c}-r_{i,c})x_i$. In the hard-label special case $r_{i,c}=t_{i,c}=\mathbf{1}[y_i=c]$, this reduces to $\ell_i=-\log p_{i,y_i}$. So the whole workflow is row-wise by class and coordinate-wise by feature.

The probability interpretation mirrors logistic regression: scores first, probabilities second. The score $z_c$ is evidence for class $c$, exponentiation converts evidence into positive weights, and normalization converts those weights into a categorical distribution that sums to $1$. A key identity is $\frac{P(y=c\mid x,W)}{P(y=d\mid x,W)} = e^{z_c-z_d}$, so only score differences matter.

There is also a strong inner-product interpretation. Since $z_c=w_c^\top x$, each class weight vector acts like a direction template in feature space, and the model prefers classes whose template has larger alignment (inner product) with the input representation. So one can remember softmax as _alignment competition_: each class computes an alignment score, and softmax turns those competing alignments into probabilities.

Geometrically, prediction still uses the largest score, so the decision boundary between classes $a$ and $b$ is $w_a^\top x = w_b^\top x$, equivalently $(w_a-w_b)^\top x=0$. Therefore softmax regression is still a linear classifier in input space: multiclass regions are separated by pairwise hyperplanes.

When $C=2$, softmax collapses to logistic regression by reparameterization. One has $P(y=1\mid x,W)=\frac{e^{w_1^\top x}}{e^{w_1^\top x}+e^{w_2^\top x}} = \frac{1}{1+e^{-(w_1-w_2)^\top x}} = \sigma((w_1-w_2)^\top x)$, so the binary softmax model is exactly logistic regression with parameter $w=w_1-w_2$. Intuitively, binary logistic regression is the two-class version of the same inner-product competition.

This derivation also explains a softmax invariance: adding the same vector $u$ to every class weight vector changes each score by the same amount $u^\top x$, which cancels in numerator and denominator. So softmax probabilities depend on relative scores, not absolute score offsets.

For binary and multiclass evaluation after the probabilities are computed, see [classification](classification.md#performance-metrics-for-classification).

---

Flashcards for this section are as follows:

- softmax regression intuition ::@:: Softmax regression is the multiclass extension of logistic regression: for each class index $c\in\{1,\ldots,C\}$ it computes a score $z_c=w_c^\top x$, exponentiates those scores into positive weights, and normalizes them into a categorical distribution. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- overarching matrix-index intuition for softmax computation ::@:: View $W\in\mathbb{R}^{C\times D}$ as a stack of class-specific row vectors: top index $c$ is class, bottom index $f$ is feature. For example $i$, compute $z_{i,c}=\sum_{f=1}^D W_{c,f}x_{i,f}=w_c^\top x_i$, then $p_{i,c}=\frac{e^{z_{i,c}}}{\sum_k e^{z_{i,k}}}$, then use a target distribution $r_{i,c}$ with $\sum_c r_{i,c}=1$ to form $\ell_i=-\sum_c r_{i,c}\log p_{i,c}$ and gradient row $\partial \ell_i/\partial w_c=(p_{i,c}-r_{i,c})x_i$; the hard-label one-hot special case is $r_{i,c}=\mathbf{1}[y_i=c]$. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- interpretation of softmax terms with index meanings ::@:: In $P(y=c\mid x,W)=\frac{e^{z_c}}{\sum_k e^{z_k}}$, the index $c$ means the particular class being queried, while the index $k$ runs over all classes in the denominator. Thus $z_c$ is the evidence for class $c$, $e^{z_c}$ is its positive evidence mass, and $\sum_k e^{z_k}$ is the normalizer that forces all class probabilities to sum to $1$.
- relative-odds interpretation in softmax with index meanings ::@:: In $\frac{P(y=c\mid x,W)}{P(y=d\mid x,W)}=e^{z_c-z_d}$, the indices $c$ and $d$ denote two specific classes being compared, so the formula says that pairwise class odds depend only on score differences. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- inner-product interpretation of softmax with index meanings ::@:: Since $z_c=w_c^\top x$, where $c$ indexes the class and $w_c$ is that class's weight vector, each class competes through feature-template alignment, so larger inner product means stronger evidence for that class.
- decision-boundary interpretation in softmax with index meanings ::@:: Softmax predicts by largest score, so the boundary between two specific classes $a$ and $b$ is $w_a^\top x=w_b^\top x$, equivalently $(w_a-w_b)^\top x=0$; here $a$ and $b$ are class labels, not feature indices. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- logistic regression as the two-class special case of softmax: Show how $P(y=1\mid x,W)$ reduces to a sigmoid when $C=2$ ::@:: When there are only two classes, indexed by $1$ and $2$, one has $P(y=1\mid x,W)=\frac{e^{w_1^\top x}}{e^{w_1^\top x}+e^{w_2^\top x}}=\frac{1}{1+e^{-(w_1-w_2)^\top x}}=\sigma((w_1-w_2)^\top x)$, so logistic regression is exactly the two-class softmax case. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- softmax score-shift invariance with index meanings ::@:: Adding the same vector to every class weight vector $w_c$ shifts every score $z_c$ by the same amount, so softmax probabilities stay unchanged because only relative score differences matter. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->

### softmax cross entropy and gradient

The softmax loss is categorical cross entropy. For one example $x_i$ with scores $z_{i,c}=w_c^\top x_i$, probabilities $p_{i,c}=\frac{e^{z_{i,c}}}{\sum_k e^{z_{i,k}}}$, and target distribution $r_{i,c}$ satisfying $r_{i,c}\ge 0$ and $\sum_{c=1}^C r_{i,c}=1$, the one-example loss is $\ell_i(W)=-\sum_{c=1}^C r_{i,c}\log p_{i,c}$. In the hard-label special case $r_{i,c}=t_{i,c}=\mathbf{1}[y_i=c]$, this reduces to $\ell_i(W)=-\log p_{i,y_i}$, meaning the model is penalized only through the predicted probability of the true class.

Here the indexing should be read carefully. The index $i$ refers to the training example. The index $c$ refers to a class. When $c$ appears inside a sum such as $\sum_c$, it runs over classes; when we differentiate with respect to one class-specific score or weight vector, we hold that same class index $c$ fixed. The index $k$ inside $\sum_k$ is the dummy class index used for summing over all classes. The target vector $r_i$ need not be one-hot; it may be any class-probability distribution over the $C$ classes. In the hard-label special case, $r_i=t_i$ is one-hot, meaning exactly one coordinate equals $1$ and all other coordinates equal $0$, so $t_{i,c}=1$ if the true class of example $i$ is class $c$, and $t_{i,c}=0$ otherwise.

Using log-softmax gives a clean derivation. Since $\log p_{i,c}=z_{i,c}-\log\sum_{k=1}^C e^{z_{i,k}}$, one gets $\ell_i(W)=-\sum_c r_{i,c}z_{i,c}+\Bigl(\sum_c r_{i,c}\Bigr)\log\sum_{k=1}^C e^{z_{i,k}}=-\sum_c r_{i,c}z_{i,c}+\log\sum_{k=1}^C e^{z_{i,k}}$, because $\sum_c r_{i,c}=1$. In the one-hot special case this simplifies further to $\ell_i(W)=-z_{i,y_i}+\log\sum_{k=1}^C e^{z_{i,k}}$. The general mnemonic is therefore _weighted target scores up, logsumexp down_; for hard labels, this becomes _true-class score up, logsumexp down_.

Interpretation: the term $-\sum_c r_{i,c}z_{i,c}$ pushes up scores on classes that receive large target weight, while $\log\sum_k e^{z_{i,k}}$ pushes down excessive scores globally by penalizing large evidence across classes. So cross entropy is a score-separation objective, not only a probability formula. In the one-hot special case, all target mass sits on the true class, so the first term becomes just $-z_{i,y_i}$.

Differentiating with respect to the fixed class-score coordinate $z_{i,c}$ gives $\frac{\partial \ell_i}{\partial z_{i,c}}=-r_{i,c}+\frac{e^{z_{i,c}}}{\sum_k e^{z_{i,k}}}=p_{i,c}-r_{i,c}$. Then $z_{i,c}=w_c^\top x_i$ implies $\frac{\partial z_{i,c}}{\partial w_c}=x_i$, so $\frac{\partial \ell_i}{\partial w_c}=(p_{i,c}-r_{i,c})x_i$. Averaging over the dataset yields $\frac{\partial L(W)}{\partial w_c}=\frac{1}{N}\sum_{i=1}^N (p_{i,c}-r_{i,c})x_i$. In the one-hot special case, replace $r_{i,c}$ by $t_{i,c}=\mathbf{1}[y_i=c]$.

Comparison with the binary case is exact at the output layer and can be written as explicit parallel formulas.

- Binary logistic (one score): $\ell_i^{\text{bin}}=-\bigl(r_i\log p_i+(1-r_i)\log(1-p_i)\bigr)$, $\frac{\partial \ell_i^{\text{bin}}}{\partial s_i}=p_i-r_i$, $\frac{\partial \ell_i^{\text{bin}}}{\partial w}=(p_i-r_i)x_i$.
- Multiclass softmax (score vector): $\ell_i^{\text{soft}}=-\sum_c r_{i,c}\log p_{i,c}$, $\frac{\partial \ell_i^{\text{soft}}}{\partial z_{i,c}}=p_{i,c}-r_{i,c}$, $\frac{\partial \ell_i^{\text{soft}}}{\partial w_c}=(p_{i,c}-r_{i,c})x_i$.

This gives a precise memory template: _prediction minus target_ at the output coordinate, then times input for the parameter gradient. For hard labels, the targets become $y_i\in\{0,1\}$ in the binary case and $t_{i,c}=\mathbf{1}[y_i=c]$ in the multiclass case.

The binary-versus-softmax cross-entropy relation can also be derived explicitly. In the two-class case ($C=2$), write target distribution as $r_{i,1}=r_i$, $r_{i,2}=1-r_i$, and probabilities as $p_{i,1}=p_i$, $p_{i,2}=1-p_i$; then $\ell_i^{\text{soft}}=-\sum_{c=1}^2 r_{i,c}\log p_{i,c}=-\bigl(r_{i,1}\log p_{i,1}+r_{i,2}\log p_{i,2}\bigr)=-\bigl(r_i\log p_i+(1-r_i)\log(1-p_i)\bigr)=\ell_i^{\text{bin}}$. In the hard-label special case $r_i=y_i\in\{0,1\}$, this becomes the usual binary cross entropy.

So binary cross entropy is exactly the $C=2$ special case of categorical (softmax) cross entropy.

For implementation, use max-shifted logsumexp rather than naive exponentiation. The next subsection treats that numerical-stability step on its own so the probability model and the implementation trick stay conceptually separate.

---

Flashcards for this section are as follows:

- softmax cross-entropy definition with notation and index meanings ::@:: Here $i$ indexes the training example, $c$ indexes a class, and $k$ in the denominator runs over all classes. With scores $z_{i,c}=w_c^\top x_i$, probabilities $p_{i,c}=\frac{e^{z_{i,c}}}{\sum_k e^{z_{i,k}}}$, and target distribution $r_{i,c}$ satisfying $r_{i,c}\ge 0$ and $\sum_c r_{i,c}=1$, the one-example softmax cross entropy is $\ell_i(W)=-\sum_{c=1}^C r_{i,c}\log p_{i,c}$; the hard-label one-hot special case is $r_{i,c}=\mathbf{1}[y_i=c]$, which gives $\ell_i(W)=-\log p_{i,y_i}$. <!--SR:!2000-01-01,1,250!2026-04-10,3,250-->
- log-softmax derivation form of softmax loss with index meanings ::@:: Here $i$ indexes the example, $c$ indexes the class being summed, and $k$ runs over all classes in logsumexp. Using $\log p_{i,c}=z_{i,c}-\log\sum_k e^{z_{i,k}}$, one gets $\ell_i(W)=-\sum_c r_{i,c}z_{i,c}+\Bigl(\sum_c r_{i,c}\Bigr)\log\sum_k e^{z_{i,k}}=-\sum_c r_{i,c}z_{i,c}+\log\sum_k e^{z_{i,k}}$, since $\sum_c r_{i,c}=1$; the one-hot special case becomes $\ell_i(W)=-z_{i,y_i}+\log\sum_k e^{z_{i,k}}$.
- mnemonic for softmax cross entropy with index meanings ::@:: Here $i$ indexes the training example, $c$ indexes a class, and $k$ runs over all classes. The general mnemonic is _weighted target scores up, logsumexp down_: the term $-\sum_c r_{i,c}z_{i,c}$ rewards scores according to target weights $r_{i,c}$, while $\log\sum_k e^{z_{i,k}}$ penalizes globally inflated scores across all classes; in the one-hot special case, this reduces to _true-class score up, logsumexp down_.
- softmax score-gradient derivation with index meanings: If $\ell_i(W)=-\sum_c r_{i,c}\log p_{i,c}$ with $\log p_{i,c}=z_{i,c}-\log\sum_k e^{z_{i,k}}$, derive $\partial \ell_i/\partial z_{i,c}$ for one fixed class $c$ ::@:: Here $i$ indexes the example; $k$ is the dummy class index summed over all classes; and $c$ is the fixed class coordinate being differentiated. The target vector $r_i$ is a class-probability distribution, so $r_{i,c}\ge 0$ and $\sum_c r_{i,c}=1$; the one-hot special case is $r_{i,c}=\mathbf{1}[y_i=c]$. Rewrite as $\ell_i(W)=-\sum_c r_{i,c}z_{i,c}+\log\sum_k e^{z_{i,k}}$, then differentiate with respect to the fixed coordinate $z_{i,c}$ to get $\frac{\partial \ell_i}{\partial z_{i,c}}=-r_{i,c}+\frac{e^{z_{i,c}}}{\sum_k e^{z_{i,k}}}=p_{i,c}-r_{i,c}$.
- softmax weight-gradient derivation with index meanings: If $z_{i,c}=w_c^\top x_i$ and $\partial \ell_i/\partial z_{i,c}=p_{i,c}-r_{i,c}$, derive $\partial L/\partial w_c$ ::@:: Here $i$ indexes the example, $c$ is the fixed class index, $w_c$ is the full weight vector for class $c$, and $x_i$ is the full feature vector of example $i$. The target coordinate $r_{i,c}$ is the target probability assigned to class $c$ for example $i$, with one-hot special case $r_{i,c}=\mathbf{1}[y_i=c]$. Since $z_{i,c}=w_c^\top x_i$, one has $\frac{\partial z_{i,c}}{\partial w_c}=x_i$, so $\frac{\partial \ell_i}{\partial w_c}=(p_{i,c}-r_{i,c})x_i$ and thus $\frac{\partial L(W)}{\partial w_c}=\frac1N\sum_i (p_{i,c}-r_{i,c})x_i$.
- binary-versus-softmax cross-entropy relation with derivation ::@:: In the $C=2$ case, set target probabilities $r_{i,1}=r_i$ and $r_{i,2}=1-r_i$, and probabilities $p_{i,1}=p_i$, $p_{i,2}=1-p_i$. Then $-\sum_{c=1}^2 r_{i,c}\log p_{i,c}=-(r_i\log p_i+(1-r_i)\log(1-p_i))$, so binary cross entropy is exactly the two-class softmax cross entropy; the hard-label special case is $r_i=y_i\in\{0,1\}$.
- unified output-layer mnemonic across binary and multiclass with explicit formulas ::@:: Binary formulas are $\frac{\partial \ell_i}{\partial s_i}=p_i-r_i$ and $\frac{\partial \ell_i}{\partial w}=(p_i-r_i)x_i$; multiclass formulas are $\frac{\partial \ell_i}{\partial z_{i,c}}=p_{i,c}-r_{i,c}$ and $\frac{\partial \ell_i}{\partial w_c}=(p_{i,c}-r_{i,c})x_i$. The explicit comparison shows the same template: output residual = prediction minus target, then multiply by input; for hard labels, $r_i=y_i$ in binary classification and $r_{i,c}=\mathbf{1}[y_i=c]$ in multiclass classification. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->

### logsumexp and numeric stability in implementation

Naive softmax code can fail numerically. If one directly computes $e^{z_c}$ for large scores, overflow can occur. For example, with scores $z=[1000,1001,999]$, direct exponentials are outside normal floating-point range in many environments.

The stable trick is max-shifting. Let $m=\max(z)=1001$ and define shifted scores $\tilde z = z-m=[-1,0,-2]$. Then softmax is unchanged because the same constant is subtracted from all scores, and we compute probabilities as $p_c=\frac{e^{\tilde z_c}}{\sum_k e^{\tilde z_k}}$. Numerically, this gives approximately $p\approx[0.245,0.665,0.090]$.

The same idea stabilizes cross entropy through logsumexp: $\log\sum_k e^{z_k}=m+\log\sum_k e^{z_k-m}$. For the same example, $\log\sum_k e^{z_k}=1001+\log(e^{-1}+1+e^{-2})\approx 1001.408$. If the true class is class $2$, then one-example loss is $\ell=-z_2+\log\sum_k e^{z_k}=-1001+1001.408\approx 0.408$.

Implementation memory rule: _shift, softmax, and logsumexp_. First shift by max score, then compute probabilities and loss on shifted values, and finally use fused routines when available (such as log-softmax plus negative-log-likelihood) to reduce roundoff and duplicate work.

---

Flashcards for this section are as follows:

- stable softmax example with max-shift and index meanings: Given class scores $z_1=1000$, $z_2=1001$, and $z_3=999$, compute max-shifted scores and stable probabilities ::@:: Here the subscript $c\in\{1,2,3\}$ is the class index. With $m=\max\{z_1,z_2,z_3\}=1001$, shifted scores are $z_1-m=-1$, $z_2-m=0$, and $z_3-m=-2$, and stable softmax gives $p\approx\bigl[e^{-1},1,e^{-2}\bigr]/(e^{-1}+1+e^{-2})\approx[0.245,0.665,0.090]$.
- stable logsumexp example with index meanings: Given class scores $z_1=1000$, $z_2=1001$, and $z_3=999$, compute $\log\sum_k e^{z_k}$ using max-shift ::@:: Here $k$ runs over the classes $1,2,3$. Using $m=1001$, $\log\sum_k e^{z_k}=m+\log\sum_k e^{z_k-m}=1001+\log(e^{-1}+1+e^{-2})\approx 1001.408$. <!--SR:!2000-01-01,1,250!2026-04-11,4,270-->
- stable softmax-cross-entropy example with index meanings: Given class scores $z_1=1000$, $z_2=1001$, $z_3=999$, and true class index $2$ (1-based), compute the one-example loss stably ::@:: Here the subscript is the class index and $k$ in $\sum_k$ runs over all classes. First compute $\log\sum_k e^{z_k}=1001.408$ by max-shift; then $\ell=-z_2+\log\sum_k e^{z_k}=-1001+1001.408\approx 0.408$.
- numeric-stability implementation checklist for softmax regression ::@:: Use max-shifted softmax and logsumexp, and prefer fused log-softmax plus negative-log-likelihood routines to avoid overflow/underflow and reduce roundoff error.

### worked softmax calculations

To make by-hand computation reproducible, always specify all givens first: class weights, input vector, target information, and learning rate. Then compute in this order: scores $z$, probabilities $p$, target distribution $r$, residual vector $(p-r)$, classwise gradients, and updated weights. In the hard-label special case used below, the target distribution is one-hot.

Use the concrete setup $x=(1,0)^\top$, $w_1=(2,0)^\top$, $w_2=(1,0)^\top$, $w_3=(0,0)^\top$, true class $y=2$, and learning rate $\alpha=0.1$. This is the hard-label special case, so the target distribution is the one-hot vector $r=t=[0,1,0]$. Scores are $z=[2,1,0]$. Softmax probabilities are $p\approx[0.665,0.245,0.090]$, and residuals are $p-r=p-t\approx[0.665,-0.755,0.090]$.

Classwise gradients are therefore $\frac{\partial \ell}{\partial w_1}=0.665(1,0)^\top=(0.665,0)^\top$, $\frac{\partial \ell}{\partial w_2}=-0.755(1,0)^\top=(-0.755,0)^\top$, and $\frac{\partial \ell}{\partial w_3}=0.090(1,0)^\top=(0.090,0)^\top$. One step gives $w_1^{\text{new}}=(1.9335,0)^\top$, $w_2^{\text{new}}=(1.0755,0)^\top$, and $w_3^{\text{new}}=(-0.009,0)^\top$.

The same example also shows decision-boundary intuition. Class-$1$ versus class-$2$ boundary before update is $(w_1-w_2)^\top x=0$, with normal vector $(1,0)^\top$. After update, $w_1-w_2=(1.9335-1.0755,0)=(0.858,0)$, so the boundary orientation in this toy setup remains along the same axis while class-$2$ alignment has increased at the training point.

---

Flashcards for this section are as follows:

- worked softmax probability and loss example with index meanings: Given class scores $z_1=2$, $z_2=1$, $z_3=0$ and true class index $2$ (1-based), compute softmax probabilities and one-example cross entropy ::@:: Here the subscript gives the class index. Probabilities are approximately $p_1=0.665$, $p_2=0.245$, and $p_3=0.090$, and loss is $-\log p_2=-\log 0.245\approx 1.40$. <!--SR:!2026-04-11,4,270!2000-01-01,1,250-->
- worked softmax residual-vector example with index meanings: Given class probabilities $p_1=0.665$, $p_2=0.245$, $p_3=0.090$ and target distribution coordinates $r_1=0$, $r_2=1$, $r_3=0$ (the hard-label one-hot special case), compute $p-r$ and interpret signs ::@:: Here the subscript is the class index. The residual vector is $p-r=[0.665,-0.755,0.090]$; the true class coordinate $2$ has negative residual (push its score up), and the other class coordinates have positive residuals (push their scores down).
- worked softmax gradient example with full givens and index meanings: Given input $x=(1,0)^\top$, class weight vectors $w_1=(2,0)^\top$, $w_2=(1,0)^\top$, $w_3=(0,0)^\top$, target distribution $r=[0,1,0]$ (the hard-label one-hot special case corresponding to true class $y=2$), and probabilities $p_1=0.665$, $p_2=0.245$, $p_3=0.090$, compute one-example classwise gradients ::@:: Here the subscript on $w_c$, $p_c$, and $r_c$ is the class index $c$. With residuals $p-r=[0.665,-0.755,0.090]$, gradients are $\partial\ell/\partial w_1=(0.665,0)^\top$, $\partial\ell/\partial w_2=(-0.755,0)^\top$, and $\partial\ell/\partial w_3=(0.090,0)^\top$.
- worked softmax update example with full givens and index meanings: Given input $x=(1,0)^\top$, class weight vectors $w_1=(2,0)^\top$, $w_2=(1,0)^\top$, $w_3=(0,0)^\top$, true class $y=2$, and learning rate $\alpha=0.1$, perform one gradient-descent step ::@:: Here the subscript on $w_c$ identifies class $c$. Using gradients $(0.665,0)^\top$, $(-0.755,0)^\top$, and $(0.090,0)^\top$, updates are $w_1^{\text{new}}=(1.9335,0)^\top$, $w_2^{\text{new}}=(1.0755,0)^\top$, and $w_3^{\text{new}}=(-0.009,0)^\top$.
- worked boundary interpretation from updated weights with index meanings: Given updated class-1 and class-2 weight vectors $w_1^{\text{new}}=(1.9335,0)^\top$ and $w_2^{\text{new}}=(1.0755,0)^\top$, what is the class-1 versus class-2 boundary normal and what does it imply? ::@:: The subscripts $1$ and $2$ label the two classes being compared. The pairwise boundary normal is $w_1^{\text{new}}-w_2^{\text{new}}=(0.858,0)^\top$, so the boundary remains linear with orientation along the first feature axis in this toy setup.
