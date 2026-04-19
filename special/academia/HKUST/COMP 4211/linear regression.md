---
aliases:
  - least squares regression
  - linear regression
  - linear regressions
  - ordinary least squares
tags:
  - flashcard/active/special/academia/HKUST/COMP_4211/linear_regression
  - language/in/English
---

<!-- check: ignore-file[two_sided_calc_warning]: concept note uses symbolic answers on QA cards -->

# linear regression

Linear regression is the course's first serious predictive model because it is simple enough to analyze exactly and rich enough to illustrate almost every recurring machine-learning theme: supervised learning, loss minimization, feature engineering, model capacity, generalization, hyperparameter selection, regularization, and probabilistic modeling. The task is to predict a real-valued response from a feature vector using an affine score.

Throughout the course, the convention is to write the model as $\hat y = w^\top x$ after augmenting the feature vector by setting $x_0 = 1$. This absorbs the bias term into the parameter vector $w = (w_0,w_1,\ldots,w_D)^\top$, so $w_0$ plays the role often denoted by $b$. The weights encode how strongly each feature contributes to the predicted response.

The word _linear_ refers to linearity in the parameters, not necessarily linearity in the raw input coordinates. Once the input is replaced by a feature map $\phi(x)$, the predictor still has the form $w^\top \phi(x)$, so the optimization remains a linear-regression problem even though the resulting function of the original input may be curved.

---

Flashcards for this section are as follows:

- overview ::@:: Linear regression predicts a real-valued target with an affine score such as $\hat y = w^\top x$, and in COMP 4211 it serves as the prototype for later machine-learning models. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- why linear regression matters early ::@:: Linear regression already exhibits the main machine-learning ideas of supervised learning, loss minimization, feature engineering, capacity control, regularization, and probabilistic interpretation. <!--SR:!2026-04-12,4,323!2026-04-12,4,284-->
- course convention for the intercept term ::@:: In this course the bias/intercept is included by augmenting the features with $x_0 = 1$, so the predictor is written compactly as $\hat y = w^\top x$. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- role of the weights ::@:: The entries of $w$ determine how strongly the corresponding features influence the predicted response. <!--SR:!2026-04-12,4,301!2026-04-12,4,284-->
- linear in parameters versus linear in raw input ::@:: A model can be nonlinear in the raw input yet still count as a linear model if it is linear in the transformed features or parameters. <!--SR:!2026-04-12,4,301!2026-04-12,4,270-->

## supervised regression setup and ordinary least squares

The supervised-regression training set is a collection of pairs $D = \{(x_i,y_i)\}_{i=1}^N$ where each $x_i \in \mathbb{R}^{D+1}$ is an augmented feature vector and each $y_i \in \mathbb{R}$ is a numerical response. The model predicts $y_i$ by $\hat y_i = w^\top x_i$, so learning means choosing $w$ to make the predicted responses close to the observed ones.

The lecture begins with the mean squared error $L(w) = \frac{1}{N}\sum_{i=1}^N (y_i - w^\top x_i)^2$. Each residual $y_i - w^\top x_i$ measures how far the prediction misses one example, and squaring makes large mistakes disproportionately expensive while preventing positive and negative errors from canceling each other out.

The optimization viewpoint is important. Linear regression is not merely a formula; it is an optimization problem over a space of candidate predictors. Ordinary least squares chooses the parameter vector whose predictions minimize the average squared residual over the training set.

Ordinary least squares is the most common fitting method for linear regression because it is mathematically clean, computationally convenient, and ties directly to Gaussian-noise maximum likelihood. But it is not the only one. A detailed comparison with weighted least squares, generalized least squares, least absolute deviations, ridge, and LASSO appears in the next subsection.

Another reason OLS is so prominent is that, under the squared-loss setup of this lecture, it often has a _closed-form_ or _analytic_ solution. Here that means the optimizer can be written explicitly by a finite sequence of algebraic operations, namely $\hat w = (X^\top X)^{-1}X^\top y$ when $X^\top X$ is invertible, instead of being defined only as the endpoint of an iterative search procedure. In everyday machine-learning language, "closed form" and "analytic solution" are often used almost interchangeably to mean "there is an explicit formula for the optimizer".

That situation is desirable but unusual. It is desirable because an explicit formula reveals how the solution depends on the data, avoids step-size tuning and convergence worries, and in the OLS case identifies the global optimum immediately. It is unusual because many machine-learning objectives are too complicated to solve exactly: the model may be nonlinear in the parameters, the loss may be nonsmooth, the constraints may be awkward, or the stationarity equations may simply not be solvable in a neat formula.

When no closed-form solution is available, one usually switches from exact algebra to numerical optimization. The common strategy is to compute gradients or subgradients and then use an iterative method such as gradient descent, stochastic gradient descent, momentum methods, Newton-type methods, coordinate descent, or other numerical solvers to approach an optimum. So OLS is pedagogically special: it lets the course show both a full analytic answer and the general optimization viewpoint in the same model.

---

Flashcards for this section are as follows:

- supervised regression data ::@:: In linear regression the training data are pairs $(x_i,y_i)$ with augmented feature vectors $x_i \in \mathbb{R}^{D+1}$ and real-valued targets $y_i \in \mathbb{R}$. <!--SR:!2026-04-12,4,284!2026-04-12,4,313-->
- prediction rule $\hat y_i = w^\top x_i$ ::@:: For each example $x_i$, linear regression predicts the response by the affine score $\hat y_i = w^\top x_i$. <!--SR:!2026-04-12,4,270!2026-04-12,4,323-->
- mean squared error $L(w)=\frac{1}{N}\sum_{i=1}^N (y_i-w^\top x_i)^2$ ::@:: The standard linear-regression objective is $L(w)=\frac{1}{N}\sum_{i=1}^N (y_i-w^\top x_i)^2$. <!--SR:!2026-04-12,4,301!2026-04-12,4,284-->
- why squared error is used ::@:: Squaring residuals prevents sign cancellation and penalizes large mistakes more strongly than small ones. <!--SR:!2026-04-12,4,323!2026-04-12,4,313-->
- ordinary least squares ::@:: Ordinary least squares chooses the parameter vector $w$ that minimizes the average squared residual over the training set. <!--SR:!2026-04-12,4,284!2026-04-12,4,301-->
- why OLS is the default linear-regression method ::@:: OLS is the most common linear-regression method because it is analytically simple, computationally convenient, and coincides with Gaussian maximum likelihood. <!--SR:!2026-04-12,4,313!2026-04-12,4,284-->
- closed-form OLS solution ::@:: Under the squared-loss setup, OLS often has the explicit solution $\hat w=(X^\top X)^{-1}X^\top y$ when $X^\top X$ is invertible. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- what closed-form or analytic solution means ::@:: A closed-form or analytic solution means the optimizer can be written explicitly by a finite sequence of algebraic operations instead of being found only by iterative search. <!--SR:!2026-04-12,4,323!2026-04-12,4,301-->
- why closed-form solutions are desirable ::@:: Closed-form solutions are desirable because they expose how the optimizer depends on the data, avoid convergence tuning, and in the OLS case identify the global optimum directly. <!--SR:!2026-04-12,4,313!2026-04-12,4,323-->
- why many machine-learning models do not have closed-form solutions ::@:: Closed-form solutions are often unavailable because the model may be nonlinear, the loss may be nonsmooth, or the optimality equations may be too hard to solve exactly. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- what to do when no closed-form solution exists ::@:: When no analytic solution exists, one usually uses numerical optimization such as gradient descent, stochastic gradient descent, Newton-type methods, or coordinate descent to approximate an optimum. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->
- optimization viewpoint ::@:: Linear regression should be viewed as an optimization problem over candidate predictors, not merely as a closed-form algebraic formula. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->

### other linear-regression fitting methods

Thinking of ordinary least squares as one member of a family is useful. The shared goal is still to fit a linear predictor, but the objective or assumptions change. Weighted least squares replaces the uniform average of squared residuals by a weighted one, so high-confidence examples count more heavily. Generalized least squares goes further by modeling error covariance explicitly, which matters when noise is correlated or has unequal variance across examples.

Other alternatives change the loss itself. Least absolute deviations minimizes $\sum_i |y_i-w^\top x_i|$, so it reacts less violently to outliers than OLS. Ridge regression adds an $L_2$ penalty and is especially helpful when features are strongly collinear or when one wants smoother, smaller coefficients. LASSO adds an $L_1$ penalty and can set some coefficients exactly to zero, effectively combining fitting with feature selection.

---

Flashcards for this section are as follows:

- weighted least squares ::@:: Weighted least squares minimizes a weighted sum of squared residuals so more reliable observations can influence the fit more strongly than less reliable ones. <!--SR:!2026-04-12,4,323!2026-04-12,4,313-->
- generalized least squares ::@:: Generalized least squares extends least squares to correlated or heteroscedastic noise by incorporating the error covariance structure into the fit. <!--SR:!2026-04-12,4,322!2026-04-12,4,313-->
- least absolute deviations ::@:: Least absolute deviations minimizes absolute residuals instead of squared residuals, making the fit more robust to outliers. <!--SR:!2026-04-12,4,323!2026-04-12,4,322-->
- ridge regression as a linear-regression method ::@:: Ridge regression is a linear-regression method that adds an $L_2$ penalty to shrink coefficients and stabilize ill-conditioned fits. <!--SR:!2026-04-12,4,301!2026-04-12,4,284-->
- LASSO as a linear-regression method ::@:: LASSO is a linear-regression method that adds an $L_1$ penalty, often producing sparse solutions with some coefficients exactly zero. <!--SR:!2026-04-12,4,323!2026-04-12,4,313-->

### one-feature least-squares fit

One of the lecture's first examples uses a single-input model $\hat y = w_0 + w_1 x_1$ on three data points. In that setting the prediction line must compromise among several observations rather than pass through every point automatically. The mean squared error objective becomes a concrete function of two unknowns, $w_0$ and $w_1$, and minimizing that function is the simplest illustration of how learning chooses parameters from data.

For data such as $(x_1,y) = (2,2), (4,3), (6,4)$, the residual terms are $2 - (w_0 + 2w_1)$, $3 - (w_0 + 4w_1)$, and $4 - (w_0 + 6w_1)$. The loss is the average of the squares of those three residuals. This toy example matters because it makes the abstract formula tangible: the weights are selected so that the fitted line balances all examples at once, not so that it memorizes one point at a time.

---

Flashcards for this section are as follows:

- one-feature fit setup ::@:: In the one-feature toy problem, linear regression fits a line $\hat y = w_0 + w_1x_1$ to the three points $(2,2)$, $(4,3)$, and $(6,4)$. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- why a line need not pass through every point ::@:: In general, least squares chooses the line that minimizes average squared residuals, so it balances all observations rather than forcing perfect interpolation. <!--SR:!2026-04-12,4,323!2026-04-12,4,301-->
- one-feature residuals ::@:: For $(x_1,y)=(2,2),(4,3),(6,4)$, the residuals are $2-(w_0+2w_1)$, $3-(w_0+4w_1)$, and $4-(w_0+6w_1)$. <!--SR:!2026-04-12,4,270!2026-04-12,4,313-->

### solving the toy problem by differentiation

For the same three points, the explicit objective is $L(w_0,w_1)=\frac{1}{3}\Bigl[(2-(w_0+2w_1))^2+(3-(w_0+4w_1))^2+(4-(w_0+6w_1))^2\Bigr]$.

The partial derivatives are $\frac{\partial L}{\partial w_0}=-\frac{2}{3}\Bigl[(2-(w_0+2w_1))+(3-(w_0+4w_1))+(4-(w_0+6w_1))\Bigr]$ and $\frac{\partial L}{\partial w_1}=-\frac{2}{3}\Bigl[2(2-(w_0+2w_1))+4(3-(w_0+4w_1))+6(4-(w_0+6w_1))\Bigr]$.

Setting both derivatives to zero gives two linear equations in $w_0$ and $w_1$. Solving them yields $w_0=1$ and $w_1=\tfrac{1}{2}$, so the fitted rule is $\hat y = 1 + \tfrac{1}{2}x_1$. In this particular example the line passes through all three points, so the training MSE becomes $0$.

---

Flashcards for this section are as follows:

- one-feature example objective: For $(x_1,y)=(2,2),(4,3),(6,4)$ and $\hat y=w_0+w_1x_1$, what is the MSE objective? ::@:: $L(w_0,w_1)=\frac{1}{3}\Bigl[(2-(w_0+2w_1))^2+(3-(w_0+4w_1))^2+(4-(w_0+6w_1))^2\Bigr]$. <!--SR:!2026-04-12,4,323!2026-04-12,4,313-->
- one-feature derivative conditions ::@:: The toy least-squares line is found by setting both partial derivatives $\frac{\partial L}{\partial w_0}$ and $\frac{\partial L}{\partial w_1}$ to zero. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- one-feature example solution: For $(x_1,y)=(2,2),(4,3),(6,4)$, what least-squares line is obtained? ::@:: Solving the first-order conditions gives $w_0=1$ and $w_1=\tfrac{1}{2}$, so $\hat y = 1 + \tfrac{1}{2}x_1$. <!--SR:!2026-04-12,4,313!2026-04-11,3,302-->
- why the one-feature example is useful ::@:: It makes least squares concrete by turning learning into an explicit calculus problem in two unknowns. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->

### gradient, matrix form, and the normal equation

For computation and notation, the lecture rewrites the training set using the design matrix $X$, whose row with index $i$ is $x_i^\top$, together with the target vector $y = (y_1,\ldots,y_N)^\top$. Then the fitted values become $Xw$, the residual vector becomes $y - Xw$, and the loss becomes $L(w) = \frac{1}{N}\lVert y - Xw\rVert_2^2$.

Differentiating this quadratic objective gives $\nabla L(w) = \frac{2}{N}(X^\top Xw - X^\top y)$. Setting the gradient to zero yields the normal equation $X^\top Xw = X^\top y$. When $X^\top X$ is invertible, the solution is $\hat w = (X^\top X)^{-1}X^\top y$.

This derivation explains why the lecture reviews calculus. The least-squares loss is a quadratic bowl in parameter space, so the gradient points uphill and the minimizer is found where the gradient vanishes. In one dimension this is the familiar rule "differentiate and set the derivative to zero"; in several dimensions the same idea is expressed through the gradient vector.

The closed-form ordinary least-squares solution is mathematically elegant, but it also teaches a more general lesson: machine learning often reduces to choosing parameters by minimizing a differentiable objective. Later models may lose the closed form, yet the optimization logic survives.

---

Flashcards for this section are as follows:

- design matrix ::@:: The design matrix $X$ is formed by stacking the row vectors $x_i^\top$, so each training example occupies one row. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- matrix loss $L(w)=\frac{1}{N}\lVert y-Xw\rVert_2^2$ ::@:: With design matrix $X$ and target vector $y$, the mean squared error becomes $L(w)=\frac{1}{N}\lVert y-Xw\rVert_2^2$. <!--SR:!2026-04-12,4,301!2026-04-12,4,270-->
- residual vector ::@:: In matrix form, the residual vector is $y - Xw$, namely observed targets minus fitted values. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- gradient of least squares ::@:: The gradient of the least-squares objective is $\nabla L(w)=\frac{2}{N}(X^\top Xw - X^\top y)$. <!--SR:!2026-04-12,4,313!2026-04-12,4,270-->
- normal equation $X^\top Xw = X^\top y$ ::@:: Setting the least-squares gradient to zero gives the normal equation $X^\top Xw = X^\top y$. <!--SR:!2026-04-12,4,322!2026-04-12,4,323-->
- ordinary least squares solution $\hat w = (X^\top X)^{-1}X^\top y$ ::@:: When $X^\top X$ is invertible, the least-squares minimizer is $\hat w = (X^\top X)^{-1}X^\top y$. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- why calculus appears in linear regression ::@:: Calculus enters because learning is posed as minimizing a differentiable loss, so the optimum is characterized by a zero gradient. <!--SR:!2026-04-12,4,284!2026-04-12,4,284-->
- quadratic bowl intuition ::@:: The least-squares objective is a quadratic bowl in parameter space, which is why the optimization landscape is especially clean for linear regression. <!--SR:!2026-04-12,4,323!2026-04-12,4,301-->

### derivation of the matrix gradient

The matrix formula is worth expanding once because it is the prototype for many later derivations. Starting from $L(w)=\frac{1}{N}(y-Xw)^\top(y-Xw)$, expand the quadratic to obtain $L(w)=\frac{1}{N}\bigl(y^\top y - 2y^\top Xw + w^\top X^\top Xw\bigr)$.

The easy terms are $y^\top y$ and $-2y^\top Xw$. The first does not depend on $w$ at all, so its derivative is $0$. The second is linear in $w$, so its derivative is simply $-2X^\top y$. The only term that usually feels mysterious to beginners is the quadratic expression $w^\top X^\top Xw$.

Write $A=X^\top X$ for a moment. Then $w^\top A w$ is a scalar, and entrywise it equals $\sum_{j=1}^{D+1}\sum_{k=1}^{D+1} a_{jk}w_jw_k$. To differentiate with respect to one coordinate $w_m$, collect every product containing $w_m$. The terms with $j=m$ contribute $\sum_k a_{mk}w_k$, and the terms with $k=m$ contribute $\sum_j a_{jm}w_j$. Therefore $\frac{\partial}{\partial w_m}(w^\top A w)=\sum_k a_{mk}w_k+\sum_j a_{jm}w_j=(Aw)_m+(A^\top w)_m$.

Now use the fact that $A=X^\top X$ is symmetric, so $A^\top=A$. Each coordinate derivative therefore becomes $2(Aw)_m$, and stacking all coordinates gives $\nabla_w(w^\top X^\top Xw)=2X^\top Xw$. A useful two-variable memory aid is to imagine $A=\begin{bmatrix}a&b\\ b&c\end{bmatrix}$ and $w=\begin{bmatrix}w_1\\ w_2\end{bmatrix}$, so that $w^\top A w = aw_1^2 + 2bw_1w_2 + cw_2^2$. Differentiating componentwise gives $2aw_1+2bw_2$ and $2bw_1+2cw_2$, which is exactly the vector $2Aw$.

Putting the pieces together gives $\nabla L(w)=\frac{1}{N}(2X^\top Xw - 2X^\top y)=\frac{2}{N}(X^\top Xw-X^\top y)$. This derivation is more than matrix gymnastics. It shows that the least-squares optimum is obtained by balancing two terms: $X^\top Xw$, which comes from the geometry of the design matrix, and $X^\top y$, which comes from how the targets correlate with the features.

---

Flashcards for this section are as follows:

- matrix expansion of least squares ::@:: The matrix least-squares objective expands as $L(w)=\frac{1}{N}\bigl(y^\top y - 2y^\top Xw + w^\top X^\top Xw\bigr)$. <!--SR:!2026-04-12,4,301!2026-04-12,4,284-->
- coordinatewise reason that $\nabla_w(w^\top A w)=(A+A^\top)w$ ::@:: Since $w^\top A w = \sum_{j,k} a_{jk}w_jw_k$, differentiating with respect to $w_m$ collects the terms where $j=m$ and where $k=m$, giving $(Aw)_m+(A^\top w)_m$. <!--SR:!2026-04-12,4,301!2026-04-12,4,323-->
- why the derivative of $w^\top X^\top Xw$ is $2X^\top Xw$ ::@:: Let $A=X^\top X$. Because $A$ is symmetric, $(A+A^\top)w = 2Aw$, so $\nabla_w(w^\top X^\top Xw)=2X^\top Xw$. <!--SR:!2026-04-12,4,301!2026-04-12,4,323-->
- two-variable memory aid for differentiating a quadratic form ::@:: If $A=\begin{bmatrix}a&b\\ b&c\end{bmatrix}$, then $w^\top A w = aw_1^2 + 2bw_1w_2 + cw_2^2$, so differentiating gives $[2aw_1+2bw_2,\ 2bw_1+2cw_2]^\top = 2Aw$. <!--SR:!2026-04-12,4,301!2026-04-12,4,270-->
- why the matrix derivation matters ::@:: The derivation shows that least squares balances feature geometry through $X^\top X$ against target-feature alignment through $X^\top y$. <!--SR:!2026-04-12,4,313!2026-04-12,4,270-->

### tiny normal-equation computation

For the same one-feature dataset, the augmented design matrix and target vector are $X=\begin{bmatrix}1&2\\1&4\\1&6\end{bmatrix}$ and $y=\begin{bmatrix}2\\3\\4\end{bmatrix}$.

Then $X^\top X = \begin{bmatrix}3&12\\12&56\end{bmatrix}$ and $X^\top y = \begin{bmatrix}9\\40\end{bmatrix}$. So the normal equation becomes $\begin{bmatrix}3&12\\12&56\end{bmatrix}\begin{bmatrix}w_0\\w_1\end{bmatrix}=\begin{bmatrix}9\\40\end{bmatrix}$, whose solution is again $w_0=1$ and $w_1=\tfrac{1}{2}$. This illustrates that the normal equation and the calculus-based derivation are the same method written at different levels of abstraction.

---

Flashcards for this section are as follows:

- tiny normal-equation computation: For $X=\begin{bmatrix}1&2\\1&4\\1&6\end{bmatrix}$ and $y=\begin{bmatrix}2\\3\\4\end{bmatrix}$, what are $X^\top X$ and $X^\top y$? ::@:: $X^\top X = \begin{bmatrix}3&12\\12&56\end{bmatrix}$ and $X^\top y = \begin{bmatrix}9\\40\end{bmatrix}$. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->

### normal equation as projection and the noninvertible case

The normal equation has a geometric interpretation that is often easier to remember than the algebra alone. If we write the residual vector as $r = y - Xw$, then the condition $X^\top Xw = X^\top y$ is equivalent to $X^\top r = 0$. That means the residual is orthogonal to every column of $X$, and hence orthogonal to the entire column space of the design matrix. So the fitted vector $Xw$ is the orthogonal projection of $y$ onto $\operatorname{col}(X)$.

It helps to begin with ordinary projection onto a single nonzero vector $a$. The projection of a vector $y$ onto the line spanned by $a$ is $\operatorname{proj}_{a}(y)=\frac{a^\top y}{a^\top a}a$. The numerator $a^\top y$ measures alignment with the direction $a$, while the denominator $a^\top a=\|a\|_2^2$ corrects for the fact that $a$ may not be a unit vector. If $a$ is doubled in length, the raw inner product also doubles, so one must divide by the squared length to recover the right coefficient on the direction itself.

The matrix formula is the same idea on a whole subspace. When the columns of $X$ are linearly independent, the orthogonal projection of $y$ onto $\operatorname{col}(X)$ is $\hat y = X\hat w = X(X^\top X)^{-1}X^\top y$. The factor $X^\top y$ collects the inner products between $y$ and the columns of $X$, but those raw inner products are not yet the correct coordinates unless the columns are orthonormal. The Gram matrix $X^\top X$ records column lengths and pairwise correlations, and multiplying by $(X^\top X)^{-1}$ removes that distortion. If the columns were already orthonormal, then $X^\top X = I$ and the projection would simplify to $XX^\top y$.

This projection viewpoint also explains what happens when $X^\top X$ is not invertible. Singularity occurs when the columns of $X$ are linearly dependent, for example when one feature duplicates another or is an exact multiple of it. In that case the inverse formula fails, but the least-squares problem still has minimizers because the objective depends on the fitted vector $Xw$, not on one uniquely determined coefficient vector.

For example, if the model uses both $x$ and $2x$ as separate features, then $w_1x + w_2(2x) = (w_1+2w_2)x$, so many different coefficient pairs produce the same prediction function. All least-squares minimizers still satisfy the normal equation. In the full-column-rank case the matrix pseudoinverse is exactly $X^{+}=(X^\top X)^{-1}X^\top$, so $\hat w=X^{+}y$ is just another way to write the ordinary least-squares formula. In the rank-deficient case, however, $(X^\top X)^{-1}$ does not exist, while the Moore-Penrose pseudoinverse $X^{+}$ still does exist and again gives the minimum-norm least-squares solution $\hat w = X^{+}y$.

So the correct correction to remember is this: $(X^\top X)^{-1}$ by itself is not the pseudoinverse and is not enough to map the target vector $y$ into coefficient space. One still needs the factor $X^\top$ on the right. In fact, the dimensions already reveal this: $(X^\top X)^{-1}$ is a square matrix in parameter space, whereas $y$ lives in data space, so the bridge from data space to parameter space is the factor $X^\top$.

---

Flashcards for this section are as follows:

- normal equation as orthogonality condition $X^\top(y-Xw)=0$ ::@:: The normal equation is equivalent to $X^\top(y-Xw)=0$, meaning the residual is orthogonal to every column of the design matrix. <!--SR:!2026-04-12,4,313!2026-04-12,4,270-->
- ordinary vector projection onto a nonunit vector ::@:: The projection of $y$ onto the line spanned by a nonzero vector $a$ is $\operatorname{proj}_{a}(y)=\frac{a^\top y}{a^\top a}a$. <!--SR:!2026-04-12,4,313!2026-04-12,4,284-->
- why ordinary vector projection divides by $a^\top a$ ::@:: The denominator $a^\top a=\|a\|_2^2$ corrects for the length of $a$, so the projection coefficient measures direction alignment rather than raw scale. <!--SR:!2026-04-12,4,313!2026-04-12,4,284-->
- projection intuition for least squares ::@:: Least squares chooses $Xw$ as the orthogonal projection of $y$ onto the column space $\operatorname{col}(X)$. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- projection matrix for full-column-rank linear regression ::@:: If the columns of $X$ are linearly independent, the projection of $y$ onto $\operatorname{col}(X)$ is $X(X^\top X)^{-1}X^\top y$. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- why $(X^\top X)^{-1}$ appears in the projection formula ::@:: The factor $X^\top y$ gives raw inner products with the columns of $X$, and $(X^\top X)^{-1}$ corrects for nonunit lengths and nonorthogonality among those columns. <!--SR:!2026-04-12,4,301!2026-04-12,4,284-->
- orthonormal-column special case ::@:: If the columns of $X$ are orthonormal, then $X^\top X=I$, so the projection simplifies to $XX^\top y$. <!--SR:!2026-04-12,4,313!2026-04-12,4,323-->
- why projection is a good memory aid ::@:: The projection viewpoint says linear regression finds the closest vector to $y$ among all vectors that can be written as $Xw$. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- when $X^\top X$ is singular ::@:: $X^\top X$ is singular when the columns of $X$ are linearly dependent, so the inverse formula cannot be used directly. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- redundant-feature example ::@:: If the model uses both $x$ and $2x$ as separate features, then many pairs $(w_1,w_2)$ yield the same prediction because $w_1x + w_2(2x) = (w_1+2w_2)x$. <!--SR:!2026-04-12,4,270!2026-04-12,4,301-->
- full-column-rank pseudoinverse formula ::@:: If $X$ has full column rank, then its pseudoinverse is $X^{+}=(X^\top X)^{-1}X^\top$, so $X^{+}y$ equals the usual ordinary least-squares solution. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- why the pseudoinverse is not just $(X^\top X)^{-1}$ ::@:: The pseudoinverse used in least squares is the pseudoinverse of $X$, not of $X^\top X$ alone, so in the full-column-rank case it is $(X^\top X)^{-1}X^\top$. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- dimension check for the pseudoinverse formula ::@:: $(X^\top X)^{-1}$ lives in parameter space, but $y$ lives in data space, so the factor $X^\top$ is needed to map data-space information into coefficient space before solving for $w$. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->
- pseudoinverse solution $\hat w = X^{+}y$ ::@:: When $X^\top X$ is not invertible, the Moore-Penrose pseudoinverse gives the minimum-norm least-squares solution $\hat w = X^{+}y$. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->

## polynomial features and model capacity

Plain linear regression can be too restrictive when the relationship between input and output is curved. The lecture's remedy is to keep the model linear in the parameters while replacing the raw input by a richer feature map $\phi(x)$. Then the predictor becomes $\hat y = w^\top \phi(x)$.

For polynomial regression, the transformed features can include powers and interaction terms. If $x = [1,x_1,x_2]^\top$ and degree $d = 2$, a typical mapping is $\phi(x) = [1,x_1,x_2,x_1^2,x_1x_2,x_2^2]^\top$. The predictor is still linear in the coefficients multiplying these features, but as a function of the original coordinates it is no longer a straight line or plane.

For $p$ input variables and degree $d$, the general rule is: include every monomial $x_1^{\alpha_1}\cdots x_p^{\alpha_p}$ whose exponents are nonnegative integers and whose total degree satisfies $\alpha_1+\cdots+\alpha_p\le d$. Then polynomial regression can be written compactly as $\hat y = \sum_{|\alpha|\le d} w_{\alpha}x^{\alpha}$, where $\alpha=(\alpha_1,\ldots,\alpha_p)$ is a multi-index, $|\alpha|=\alpha_1+\cdots+\alpha_p$, and $x^{\alpha}=x_1^{\alpha_1}\cdots x_p^{\alpha_p}$.

This formula also clarifies two easy-to-miss facts. First, ordinary linear regression is the special case $d=1$, because the only allowed monomials are the constant term and the first-order terms $x_1,\ldots,x_p$. Second, the bias term is just the zeroth-order monomial: it corresponds to $\alpha=(0,\ldots,0)$, so $x^{\alpha}=1$.

One good memory aid is: _write down every product of input coordinates whose total exponent budget is at most $d$, including the empty product $1$_. For degree $2$, that means constant terms, all first-order terms, all squares, and all pairwise interactions; for degree $3$, one adds cubic terms and products whose exponents sum to $3$.

This is the first important feature-engineering lesson of the course. A model may look more sophisticated not because the optimizer changed, but because the representation changed. The feature map determines what shapes the hypothesis class can express. In that sense, polynomial regression is an early example of a broader machine-learning pattern: first transform the input into useful features, then apply a simpler model on top. Neural networks can be viewed in the same high-level way. Their hidden layers learn a feature transform from raw input into a new representation, and the final layer is often just a classical linear model operating on those learned features.

---

Flashcards for this section are as follows:

- polynomial regression idea ::@:: Polynomial regression keeps the model linear in the parameters while using nonlinear features such as $1,x,x^2,\ldots,x^d$. <!--SR:!2026-04-12,4,313!2026-04-12,4,323-->
- feature map viewpoint ::@:: Polynomial regression is linear regression performed on transformed features $\phi(x)$ rather than on the raw input directly. <!--SR:!2026-04-12,4,284!2026-04-12,4,313-->
- general polynomial regression form ::@:: For $p$ variables and degree $d$, polynomial regression includes all monomials $x^{\alpha}=x_1^{\alpha_1}\cdots x_p^{\alpha_p}$ with $|\alpha|\le d$, so $\hat y = \sum_{|\alpha|\le d} w_{\alpha}x^{\alpha}$. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- how to remember the polynomial feature map ::@:: A good memory aid is to list every product of input coordinates whose total exponent count is at most $d$, including the empty product $1$. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- linear regression as a special case of polynomial regression ::@:: Ordinary linear regression is the degree-$1$ special case of polynomial regression, because the allowed monomials are only $1,x_1,\ldots,x_p$. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->
- bias as a zeroth-order term ::@:: In polynomial regression the bias is the zeroth-order monomial, corresponding to exponent vector $(0,\ldots,0)$ and feature value $1$. <!--SR:!2026-04-12,4,284!2026-04-12,4,301-->
- degree-2 feature map example ::@:: For $x = [1,x_1,x_2]^\top$, a degree-2 polynomial map can be $\phi(x) = [1,x_1,x_2,x_1^2,x_1x_2,x_2^2]^\top$. <!--SR:!2026-04-12,4,313!2026-04-12,4,284-->
- interaction term ::@:: A feature such as $x_1x_2$ is an interaction term because it allows the model to depend on how two coordinates vary together. <!--SR:!2026-04-12,4,322!2026-04-12,4,284-->
- why feature engineering matters ::@:: Feature engineering changes what functions the model can represent even when the optimization method remains the same. <!--SR:!2026-04-12,4,284!2026-04-12,4,313-->
- neural-network analogy for polynomial regression ::@:: Polynomial regression uses a hand-designed feature transform followed by a linear model, while a neural network can be viewed as learning the feature transform and then applying a final linear layer on top. <!--SR:!2026-04-12,4,301!2026-04-12,4,270-->
- linear in parameters ::@:: A polynomial regressor is still a linear model because it is linear in the coefficients multiplying the transformed features. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->

### worked polynomial-feature constructions

For a single scalar input, the degree-2 mapping is especially simple: if the raw input is $x$, then the transformed feature vector is $\phi(x)=[1,x,x^2]^\top$. A predictor with coefficients $(w_0,w_1,w_2)$ therefore takes the form $\hat y = w_0 + w_1x + w_2x^2$. For example, if $(w_0,w_1,w_2)=(1,-3,2)$ and $x=2$, then $\hat y = 1 - 6 + 8 = 3$.

For two input variables, the lecture's mapping $\phi(x)=[1,x_1,x_2,x_1^2,x_1x_2,x_2^2]^\top$ shows how curvature and interaction enter together. If $x=[1,2,3]^\top$, then the transformed feature vector becomes $[1,2,3,4,6,9]^\top$. The linear optimizer now chooses coefficients in this richer space, but the resulting predictor can represent curved surfaces in the original coordinates.

---

Flashcards for this section are as follows:

- scalar degree-2 example: If $\phi(x)=[1,x,x^2]^\top$, $(w_0,w_1,w_2)=(1,-3,2)$, and $x=2$, what is $\hat y$? ::@:: The prediction is $\hat y = 1 - 3\cdot 2 + 2\cdot 2^2 = 3$. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->
- two-variable degree-2 feature map example: If $x=[1,2,3]^\top$, what is $\phi(x)$ for degree $2$? ::@:: The transformed vector is $\phi(x)=[1,2,3,4,6,9]^\top$. <!--SR:!2026-04-12,4,284!2026-04-12,4,284-->

## hypothesis space, capacity, and generalization

The lecture formalizes model flexibility through the _hypothesis space_: the set of all functions the learner is allowed to choose from. When the polynomial degree grows, the hypothesis space becomes larger, because the model can represent more complicated curves. In that sense, higher degree means higher capacity.

Capacity must be judged against the real goal of machine learning. Training performance matters, but only as a proxy. What we truly care about is how well the learned predictor works on future data drawn from the same underlying data-generating process. This is the idea of _generalization_.

The slides emphasize that training and test data are assumed to be independent and identically distributed samples from the same population. Under that assumption, training error and test error are related, but not identical. Training error usually improves as the model becomes more flexible because the learner can fit the observed sample more closely. Test error behaves differently because it reflects how much of that fit captures genuine pattern rather than noise.

Two parts of the i.i.d. assumption matter. _Identically distributed_ means the future cases we care about come from the same population as the training cases, so performance on held-out data is actually relevant to deployment. _Independent_ means one example does not secretly reveal another, so the evaluation is not contaminated by leakage. If either part fails, then a low validation or test error may stop meaning what we hoped it meant.

The effect of hypothesis-space size on error should therefore be read in layers. In the most general sense, enlarging the hypothesis space can only help the learner fit the observed data, because the old functions are still available and new ones are added. So training error usually stays the same or decreases as the hypothesis space grows. Validation and test error behave differently: with too small a space the model underfits and all held-out errors remain high, but with too large a space the learner begins fitting sample-specific noise, so validation and test error can rise even while training error keeps falling. The goal of model selection is to find the part of this capacity scale where held-out error is smallest, not where training error is smallest.

---

Flashcards for this section are as follows:

- hypothesis space ::@:: The hypothesis space is the set of all functions a learning algorithm is allowed to choose as its solution. <!--SR:!2026-04-12,4,270!2026-04-12,4,313-->
- model capacity ::@:: Model capacity is the expressive size or flexibility of the hypothesis space. <!--SR:!2026-04-12,4,270!2026-04-12,4,313-->
- generalization ::@:: Generalization is the ability of the learned model to perform well on future data drawn from the same underlying data-generating process. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- iid assumption for train and test data ::@:: Training and test data are usually assumed to be independent and identically distributed samples from the same population. <!--SR:!2026-04-12,4,313!2026-04-12,4,323-->
- why the iid assumption matters ::@:: If train, validation, and deployment data do not come from the same population or are not independent, then held-out error may no longer predict future performance reliably. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- effect of larger hypothesis space on training error ::@:: As the hypothesis space grows, training error usually stays the same or decreases because the learner has more candidate functions available. <p> In the course material, training error is always non-increasing as capacity increases. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->
- effect of larger hypothesis space on validation and test error ::@:: Validation and test error often first decrease and then increase as capacity grows, because extra flexibility eventually starts fitting noise rather than signal. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->

### small hypothesis spaces in practice

Simple examples make the definition less abstract. If the hypothesis space is all constant functions, then the learner may only choose a horizontal line such as $\hat y = c$. If the hypothesis space is all affine functions in one input, then the learner may choose any line $\hat y = w_0 + w_1x$. If the hypothesis space is all degree-$2$ polynomials, then the learner may choose any parabola $\hat y = w_0 + w_1x + w_2x^2$.

These examples show why capacity is really about _available shapes_. A constant-function class cannot bend at all, a line can tilt but not curve, and a quadratic model can bend once. Enlarging the hypothesis space means giving the learner more ways to explain the same training sample.

---

Flashcards for this section are as follows:

- constant-function hypothesis space example ::@:: If the hypothesis space contains only constant functions, the learner can choose only predictors of the form $\hat y = c$. <!--SR:!2026-04-12,4,313!2026-04-12,4,284-->
- affine one-feature hypothesis space example ::@:: If the hypothesis space is all affine functions of one variable, the learner can choose any line $\hat y = w_0 + w_1x$. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- quadratic hypothesis space example ::@:: If the hypothesis space is all degree-$2$ polynomials in one variable, the learner can choose any parabola $\hat y = w_0 + w_1x + w_2x^2$. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->
- intuitive meaning of larger hypothesis space ::@:: A larger hypothesis space means the learner has more possible shapes available for fitting the data. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->

### iid train-test assumption and implications

The i.i.d. assumption is not just a technical convenience; it is the bridge from sample performance to real-world performance. If the test set is drawn from the same distribution as the future inputs, then its error is a sensible estimate of how the deployed model will behave. If the distribution shifts, then even a perfectly measured test error can become misleading.

For example, imagine training a housing-price model on one city and testing it on the same city's recent sales. That is close to the intended setting. But if deployment later moves to a different city or a different economic period, the population has changed. Likewise, if nearly duplicated records leak from training into validation, the apparent generalization error becomes too optimistic because the evaluation is no longer independent.

---

Flashcards for this section are as follows:

- identically distributed part of iid ::@:: The identically distributed part means train, validation, test, and future deployment cases are sampled from the same population. <!--SR:!2026-04-12,4,322!2026-04-12,4,313-->
- independent part of iid ::@:: The independent part means one example does not leak information about another, so evaluation is not artificially easy. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- implication of distribution shift ::@:: If the deployment population differs from the training and test population, a low held-out error may fail to predict real deployment performance. <!--SR:!2026-04-12,4,284!2026-04-12,4,301-->
- implication of data leakage ::@:: If validation examples are not independent of training examples, the reported validation error is usually too optimistic. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->

### underfitting and overfitting

When the model capacity is too small, the learner cannot capture even the underlying signal. Both training and test error remain high; this is underfitting. When the capacity becomes too large, the learner can begin fitting accidental fluctuations specific to the training set. Training error keeps falling, but test error rises because the model has adapted to noise that will not repeat on new data.

This is why the familiar test-error curve is U-shaped as capacity increases. At first, increasing capacity helps because the model can represent more of the true pattern. After a certain point, further flexibility hurts because variance dominates the benefit. Later lectures make this bias-variance story explicit, but the phenomenon is already visible in the lecture-1 pictures.

---

Flashcards for this section are as follows:

- underfitting ::@:: Underfitting occurs when model capacity is too small, so both training and held-out error remain high because the model cannot represent the main signal. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- overfitting ::@:: Overfitting occurs when capacity is too large, so training error can keep decreasing while held-out error worsens due to fitting sample-specific noise. <!--SR:!2026-04-12,4,323!2026-04-12,4,313-->
- why the test-error curve is often U-shaped ::@:: As capacity increases, test error often falls first (better signal fit) and later rises (greater sensitivity to noise), producing a U-shaped curve. <!--SR:!2026-04-12,4,313!2026-04-12,4,284-->
- bias-variance preview from the capacity curve ::@:: The underfitting-to-overfitting transition is an early manifestation of the bias-variance tradeoff discussed in later lectures. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->

### training error, test error, and the capacity curve

The capacity curve in the slides should be read carefully. At the low-capacity end, both training and test error are high because the model is too simple. At intermediate capacity, test error reaches its minimum because the model is expressive enough to capture the main signal without reacting too strongly to sample-specific noise. At high capacity, training error may become extremely small while test error worsens.

This picture also explains why it is dangerous to compare two models only by training MSE. A degree-20 polynomial can easily beat a degree-14 polynomial on the training set, yet still be the worse predictor for future cases. In the lecture's phrasing, the better model is the one that will be applied to future data, so test-like performance, not training fit, should drive the choice.

---

Flashcards for this section are as follows:

- U-shaped test-error curve ::@:: As model capacity increases, test error often first decreases and then increases, producing the familiar U-shaped generalization curve. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- why low training error can mislead ::@:: A model can have very low training error yet poor generalization because it may have learned training-set noise instead of the underlying pattern. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- capacity sweet spot ::@:: The best capacity is usually an intermediate one that balances expressiveness against sensitivity to noise. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->

### capacity comparison: degree 14 versus degree 20

The slides explicitly compare polynomial models such as degree $14$ and degree $20$ on the same noisy sample. The degree-$20$ model contains the degree-$14$ model as a special case and also has extra freedom to wiggle between observed data points. Because of that extra flexibility, the degree-$20$ curve can push the training MSE lower by chasing tiny sample-specific fluctuations that the degree-$14$ model ignores.

The lesson is not that degree $14$ is always better. It is that the comparison is meant to separate _training fit_ from _future usefulness_. On the pictured sample, the higher-degree curve is more oscillatory between data points, so it is more plausible that it has memorized noise rather than captured the underlying trend. A slightly simpler model with a little more training error can therefore still be the better predictor for future data.

This example is a useful mental check for all later deep-learning lectures. Whenever a model gains expressive power, one must ask not only _what can it fit?_ but also _what will it keep getting right on unseen data?_

---

Flashcards for this section are as follows:

- degree 14 versus degree 20 lesson ::@:: The degree-$20$ polynomial has more room to wiggle between training points than the degree-$14$ model, so it can reduce training MSE further by fitting sample-specific noise. <!--SR:!2026-04-12,4,284!2026-04-12,4,284-->
- why the degree 14 model can still win ::@:: A degree-$14$ model can have slightly higher training error yet lower future error if it captures the broad trend while the degree-$20$ model overreacts to noise. <!--SR:!2026-04-12,4,284!2026-04-12,4,270-->

## validation, cross-validation, and hyperparameter tuning

Polynomial degree is not estimated by the ordinary least-squares formula; it is a _hyperparameter_. The lecture therefore uses validation to choose it. The idea is to split the available labeled data into a training subset and a validation subset, fit the weights on the training part, and then compare candidate hyperparameter values on the validation part.

Operationally, the procedure is simple but important. Pick a list of candidate hyperparameter values, such as polynomial degrees $1,2,\ldots,20$ or regularization strengths $\lambda\in\{10^{-4},10^{-3},\ldots,10^1\}$. For each candidate, train the model only on the training subset, compute the validation error, and record the score. Then choose the hyperparameter with the best validation performance, refit the chosen model on the appropriate training data, and keep the test set untouched until the very end for final reporting.

This creates a trade-off. A larger training subset helps parameter estimation, but a larger validation subset gives a more reliable estimate of future performance. The hold-out method is simple and often sufficient, yet it has two weaknesses highlighted in the slides: it does not use all the data for fitting, and the resulting validation estimate can have high variance because it depends strongly on one particular split.

Cross-validation reduces that instability. In $k$-fold cross-validation, the dataset is partitioned into $k$ folds, the model is trained $k$ times, and each fold serves once as validation while the remaining $k-1$ folds serve as training data. Averaging the validation scores produces a more stable estimate of model quality when data are limited.

Cross-validation is not magic, however. It is computationally more expensive because the full training procedure is repeated many times. It also does not eliminate the need for a final untouched test set: if cross-validation is used to pick hyperparameters and its score is then reported as the final headline result, the estimate is still slightly optimistic because model selection has already looked at those folds.

---

Flashcards for this section are as follows:

- validation set ::@:: A validation set is a held-out subset used to choose hyperparameters such as polynomial degree without evaluating directly on the final test set. <!--SR:!2026-04-12,4,301!2026-04-12,4,284-->
- model selection by validation ::@:: To choose a hyperparameter, train candidate models on the training subset and pick the value with the smallest validation error. <!--SR:!2026-04-12,4,322!2026-04-12,4,313-->
- why degree is a hyperparameter ::@:: The polynomial degree is a hyperparameter because it controls the model family and is not directly solved for by ordinary least squares. <!--SR:!2026-04-12,4,313!2026-04-12,4,323-->
- practical validation workflow for hyperparameters ::@:: Choose several candidate hyperparameter values, train one model per candidate on the training subset, compare their validation errors, then keep the best-performing candidate and leave the test set untouched until final evaluation. <!--SR:!2026-04-12,4,323!2026-04-12,4,322-->
- training-versus-validation split trade-off ::@:: A larger training set helps fit parameters better, while a larger validation set gives a more reliable estimate of future performance. <!--SR:!2026-04-12,4,322!2026-04-12,4,301-->
- why a single hold-out split wastes data ::@:: A single hold-out split leaves some labeled examples out of training, so parameter estimation is based on less data than necessary. <!--SR:!2026-04-12,4,313!2026-04-12,4,284-->
- why a single hold-out score is unstable ::@:: A single hold-out validation score can change a lot from one split to another, so it may be a noisy estimate of future performance. <!--SR:!2026-04-12,4,322!2026-04-12,4,313-->
- cross-validation ::@:: In $k$-fold cross-validation, the data are split into $k$ parts and the training-validation cycle is repeated $k$ times so every fold serves once as validation. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- why cross-validation helps ::@:: Cross-validation gives a more stable estimate of generalization than a single hold-out split, especially when data are limited. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- why cross-validation is still not perfect ::@:: Cross-validation is more computationally expensive, and after using it for model selection one still wants a final untouched test set for unbiased reporting. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->

### hold-out and cross-validation weaknesses

Hold-out validation is weak mainly because it throws away training data and because one arbitrary split can be misleading. With small datasets, either weakness can dominate: the model may look worse simply because it had too little training data, or one lucky or unlucky validation split may distort the estimate.

Cross-validation repairs much of that problem by rotating the validation role across folds, but it introduces its own price. Training now happens $k$ times, which can be costly for large models. Moreover, cross-validation is best thought of as a tool for model selection, not as a substitute for a truly untouched final test set.

---

Flashcards for this section are as follows:

- two main weaknesses of hold-out validation ::@:: Hold-out validation uses less data for fitting and can produce a high-variance estimate because the answer depends strongly on one split. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- main computational weakness of cross-validation ::@:: Cross-validation is computationally expensive because the model must be retrained once per fold. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->
- why cross-validation still does not replace a final test set ::@:: After using cross-validation to choose hyperparameters, one still wants a final untouched test set because the cross-validation score has already influenced model selection. <!--SR:!2026-04-12,4,313!2026-04-12,4,322-->

## regularization and sparse models

Validation chooses among candidate model families, but regularization changes the optimization problem itself. The lecture's strategy is to begin with a richer hypothesis space, such as a high-degree polynomial model, and then penalize overly large coefficients so that unnecessary complexity becomes expensive.

With ridge regularization, the objective becomes $L(w,w_0)=\frac{1}{N}\sum_{i=1}^N (y_i-(w_0+w^\top \phi(x_i)))^2 + \lambda \lVert w\rVert_2^2$. The extra $L_2$ penalty is often called _weight decay_. It suppresses large coefficients smoothly, which makes the fitted function less wiggly and less sensitive to noise. In this form the bias term $w_0$ is typically excluded from the penalty. The reason is that shifting the whole predictor up or down does not create extra wiggliness or local complexity in the same way that large slope or higher-order coefficients do.

LASSO replaces the squared $L_2$ norm by the $L_1$ norm, giving a penalty of the form $\lambda\lVert w\rVert_1$. The slides stress the practical difference: ridge usually keeps all coefficients but shrinks them, whereas LASSO can drive some coefficients exactly to zero. That makes LASSO useful when one wants a sparse model that effectively discards unimportant features.

The geometric picture also explains why these methods behave differently; the detailed contour-line argument is developed in the dedicated subsection below.

Regularization strength is itself a hyperparameter. A very large $\lambda$ oversuppresses the model, while a very small $\lambda$ barely changes the fit. So the course's practical workflow is: add a regularizer to control complexity, then use validation or cross-validation to choose the right penalty strength. A useful intuition is to think of regularization as an extra _force_ in hypothesis space: the data-fit term tries to move the solution toward whatever function best matches the sample, while the regularizer pulls the solution back toward simpler regions of the hypothesis space, typically those with smaller coefficient norms.

---

Flashcards for this section are as follows:

- regularization idea ::@:: Regularization controls overfitting by adding a complexity penalty to the training objective rather than only switching to a smaller model family. <!--SR:!2026-04-12,4,323!2026-04-12,4,301-->
- why start with a large hypothesis space ::@:: One can start with a rich model class and then use regularization to suppress unnecessary complexity instead of fixing a small class in advance. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- ridge regression objective $L(w,w_0)=\frac{1}{N}\sum_{i=1}^N (y_i-(w_0+w^\top\phi(x_i)))^2 + \lambda\lVert w\rVert_2^2$ ::@:: Ridge regression adds an $L_2$ penalty: $L(w,w_0)=\frac{1}{N}\sum_{i=1}^N (y_i-(w_0+w^\top\phi(x_i)))^2 + \lambda\lVert w\rVert_2^2$. <!--SR:!2026-04-12,4,313!2026-04-12,4,323-->
- why the bias term is usually not regularized ::@:: The bias term is usually excluded from regularization because shifting the predictor up or down does not increase model complexity in the same way as large slope or higher-order coefficients. <!--SR:!2026-04-12,4,323!2026-04-12,4,301-->
- weight decay ::@:: Weight decay is another name for $L_2$ regularization because it discourages large coefficient magnitudes. <!--SR:!2026-04-12,4,284!2026-04-12,4,284-->
- effect of ridge regression ::@:: Ridge regression shrinks coefficients smoothly toward zero, which stabilizes the fit and reduces overfitting. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- LASSO idea with $\lambda\lVert w\rVert_1$ ::@:: LASSO uses an $L_1$ penalty $\lambda\lVert w\rVert_1$, encouraging sparse models by driving some coefficients exactly to zero. <!--SR:!2026-04-12,4,284!2026-04-12,4,284-->
- ridge versus LASSO ::@:: Ridge usually shrinks all coefficients, whereas LASSO can eliminate some coefficients entirely and thereby perform feature selection. <!--SR:!2026-04-12,4,284!2026-04-12,4,301-->
- why LASSO yields sparsity ::@:: The $L_1$ geometry has corners on the coordinate axes, so the optimum often lands where one or more weights are exactly zero. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- choosing $\lambda$ ::@:: The regularization strength $\lambda$ is itself a hyperparameter and is typically selected by validation or cross-validation. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- regularization as a force in hypothesis space ::@:: Regularization can be viewed as a force pulling the solution away from overly complex regions of hypothesis space and back toward simpler functions with smaller coefficient norms. <!--SR:!2026-04-12,4,313!2026-04-12,4,322-->

### interpreting l2 squared and l1 penalties

The penalty terms themselves deserve interpretation. The squared $L_2$ quantity is $\lVert w\rVert_2^2 = \sum_{j=1}^D w_j^2$, so it adds the squares of the coefficient magnitudes. Squaring makes large coefficients disproportionately expensive: doubling a coefficient multiplies its penalty contribution by $4$. That is why ridge especially discourages a few very large weights.

The gradient calculation makes ridge especially intuitive. If the data-fit term is denoted by $J(w,w_0)$, then ridge uses the objective $J(w,w_0)+\lambda\|w\|_2^2$. Because $\|w\|_2^2=\sum_j w_j^2$, differentiating coordinatewise gives $\frac{\partial}{\partial w_j}\lambda\|w\|_2^2 = 2\lambda w_j$, hence $\nabla_w\bigl(\lambda\|w\|_2^2\bigr)=2\lambda w$. So the full ridge gradient is $\nabla_w J(w,w_0)+2\lambda w$. The added term points straight back toward the origin, which is why ridge smoothly pulls every coefficient inward. The bias derivative from the regularizer is $0$ because $w_0$ is excluded from the penalty.

The $L_1$ quantity is $\lVert w\rVert_1 = \sum_{j=1}^D |w_j|$, the sum of absolute magnitudes. This still penalizes large coefficients, but only linearly rather than quadratically. In practice it is less focused on punishing a single large coefficient severely and more willing to make some coordinates exactly zero if that helps reduce the total objective.

For LASSO, the derivative story is slightly different because $|w_j|$ is not differentiable at $0$. When $w_j\neq 0$, one has $\frac{\partial}{\partial w_j}|w_j| = \operatorname{sign}(w_j)$, so away from zero the regularization gradient is $\lambda\operatorname{sign}(w_j)$ in each coordinate. At $w_j=0$, one uses a subgradient: any value in the interval $[-1,1]$ is allowed. In vector form, the optimality condition becomes $0 \in \nabla_w J(w,w_0) + \lambda\,\partial\|w\|_1$.

This abstract set-valued equation becomes much clearer when written coordinatewise. For each non-bias coefficient $w_j$, the optimality condition says

- if $w_j>0$, then $\frac{\partial J}{\partial w_j} = -\lambda$;
- if $w_j<0$, then $\frac{\partial J}{\partial w_j} = +\lambda$;
- if $w_j=0$, then $\frac{\partial J}{\partial w_j}\in[-\lambda,+\lambda]$.

So a nonzero coefficient survives only when the data-fit part of the objective pushes hard enough to balance the fixed LASSO slope magnitude $\lambda$. If the data-fit derivative for a coordinate falls strictly between $-\lambda$ and $+\lambda$, then zero is already an admissible optimum for that coordinate. This is the mathematical mechanism behind sparsity: there is a whole interval of gradients for which staying exactly at zero is optimal.

By contrast, ridge has only the single equality $\frac{\partial J}{\partial w_j}+2\lambda w_j=0$, so unless symmetry or the data itself forces $w_j=0$, the solution is usually merely small rather than exactly zero. LASSO is therefore better understood not just as "stronger shrinkage", but as a qualitatively different optimality rule with a threshold zone around zero.

In special settings this threshold picture becomes explicit. For example, with orthonormal features, LASSO acts like soft thresholding: each least-squares coefficient is pulled toward zero by an amount depending on $\lambda$, and coefficients whose magnitude is below the threshold collapse exactly to zero. Even when the design is not orthonormal, that soft-threshold intuition remains a good mental model for why LASSO performs feature selection.

---

Flashcards for this section are as follows:

- what $\lVert w\rVert_2^2$ means ::@:: The squared $L_2$ penalty is $\lVert w\rVert_2^2 = \sum_j w_j^2$, the sum of squared coefficient magnitudes. <!--SR:!2026-04-12,4,284!2026-04-12,4,301-->
- why squaring changes the ridge penalty ::@:: Squaring means large coefficients are punished disproportionately, so ridge strongly discourages a few very large weights. <!--SR:!2026-04-12,4,270!2026-04-12,4,270-->
- ridge regularization gradient ::@:: Since $\|w\|_2^2=\sum_j w_j^2$, differentiating gives $\nabla_w\bigl(\lambda\|w\|_2^2\bigr)=2\lambda w$. <!--SR:!2026-04-12,4,284!2026-04-12,4,301-->
- ridge gradient interpretation ::@:: The ridge term adds $2\lambda w$ to the data-fit gradient, so every coefficient feels a smooth pull directly toward zero. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- why the bias has no regularization gradient ::@:: Because the bias term $w_0$ is excluded from the penalty, the regularizer contributes $0$ to the derivative with respect to $w_0$. <!--SR:!2026-04-12,4,313!2026-04-12,4,284-->
- what $\lVert w\rVert_1$ means ::@:: The $L_1$ penalty is $\lVert w\rVert_1 = \sum_j |w_j|$, the sum of absolute coefficient magnitudes. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- why the l1 penalty feels different from l2 squared ::@:: The $L_1$ penalty grows linearly with coefficient size, which makes exact zeros more competitive than under a smooth squared penalty. <!--SR:!2026-04-12,4,313!2026-04-12,4,284-->
- LASSO gradient away from zero ::@:: For $w_j\neq 0$, the derivative of $\lambda|w_j|$ is $\lambda\operatorname{sign}(w_j)$, so LASSO applies a constant-magnitude pull toward zero on each nonzero coordinate. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- LASSO subgradient at zero ::@:: At $w_j=0$, $|w_j|$ is not differentiable, so LASSO uses a subgradient and any value in $[-\lambda,\lambda]$ is allowed for that coordinate. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->
- LASSO optimality condition ::@:: LASSO satisfies $0\in\nabla_w J(w,w_0)+\lambda\,\partial\|w\|_1$, which explains how a coefficient can remain exactly zero. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->
- coordinatewise LASSO optimality rule ::@:: For each coefficient, LASSO optimality says: if $w_j>0$, then $\frac{\partial J}{\partial w_j}=-\lambda$; if $w_j<0$, then $\frac{\partial J}{\partial w_j}=+\lambda$; if $w_j=0$, then $\frac{\partial J}{\partial w_j}\in[-\lambda,+\lambda]$. <!--SR:!2026-04-12,4,301!2026-04-12,4,284-->
- why LASSO creates exact zeros ::@:: A coefficient can stay exactly zero whenever the data-fit derivative lies inside the interval $[-\lambda,+\lambda]$, so LASSO has a whole threshold zone that favors sparsity. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- ridge versus LASSO optimality-condition difference ::@:: Ridge uses a smooth equality $\frac{\partial J}{\partial w_j}+2\lambda w_j=0$, whereas LASSO uses a threshold-type subgradient rule, which is why ridge usually shrinks and LASSO can delete coefficients. <!--SR:!2026-04-12,4,323!2026-04-12,4,301-->
- soft-thresholding intuition for LASSO ::@:: In orthonormal designs, LASSO behaves like soft thresholding: least-squares coefficients are pulled toward zero, and sufficiently small ones become exactly zero. <!--SR:!2026-04-12,4,284!2026-04-12,4,301-->

### ridge versus LASSO contour intuition

An especially useful picture is to view the unregularized least-squares objective as having elliptical level sets around its optimum. Regularization adds a preference for solutions inside a small norm ball. For ridge, that ball is circular in two dimensions; for LASSO, it is diamond shaped. The solution occurs where a loss ellipse first touches the constraint boundary.

Algebraically, the ridge level set $\lambda\|w\|_2^2=c$ becomes $w_1^2+w_2^2=c/\lambda$ in two dimensions, which is a circle centered at the origin. The LASSO level set $\lambda\|w\|_1=c$ becomes $|w_1|+|w_2|=c/\lambda$, which is a diamond with corners on the axes. Increasing $\lambda$ makes these low-penalty regions effectively tighter in the combined objective, so the optimizer is forced closer to the origin unless the data-fit term strongly resists that motion.

Because a circle has no corners, the ridge contact point is usually on a smooth part of the boundary, so coefficients are shrunk but rarely become exactly zero. A diamond has sharp corners lying on the coordinate axes. Ellipses frequently touch those corners first, which means one or more coefficients become exactly zero. That is the geometric reason LASSO performs feature selection more readily than ridge. The algebra tells the same story: ridge penalizes proportionally to coefficient size, while LASSO applies the same slope magnitude on each nonzero coordinate, making exact zeros easier to maintain.

---

Flashcards for this section are as follows:

- contour-line intuition for ridge and LASSO ::@:: Think of least-squares loss as ellipses and the regularizer as a norm ball; the optimum is where the smallest ellipse first touches the constraint boundary. <!--SR:!2026-04-12,4,284!2026-04-12,4,323-->
- algebraic form of ridge contour lines ::@:: In two dimensions, a ridge level set $\lambda\|w\|_2^2=c$ is $w_1^2+w_2^2=c/\lambda$, so its contour lines are circles centered at the origin. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->
- algebraic form of LASSO contour lines ::@:: In two dimensions, a LASSO level set $\lambda\|w\|_1=c$ is $|w_1|+|w_2|=c/\lambda$, so its contour lines are diamonds with corners on the axes. <!--SR:!2026-04-12,4,322!2026-04-12,4,313-->
- effect of increasing $\lambda$ on the regularized objective ::@:: A larger $\lambda$ makes low-norm regions more strongly preferred in the total objective, so the optimizer is pushed closer to the origin unless data fit strongly opposes it. <!--SR:!2026-04-12,4,284!2026-04-12,4,313-->
- why ridge usually keeps coefficients nonzero ::@:: Ridge uses a round $L_2$ constraint, so the tangency point is usually on a smooth arc rather than exactly on a coordinate axis. <!--SR:!2026-04-12,4,284!2026-04-12,4,313-->
- why LASSO often gives exact zeros ::@:: LASSO uses a diamond-shaped $L_1$ constraint whose corners lie on the axes, so tangency often occurs at a corner where some coefficients are exactly zero. <!--SR:!2026-04-12,4,322!2026-04-12,4,313-->
- practical consequence of ridge versus LASSO geometry ::@:: Ridge is usually better thought of as smooth shrinkage, whereas LASSO is shrinkage plus built-in feature selection. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->

### regularization behavior across $\lambda$

The lecture gives a concrete degree-$9$ polynomial example when the true target function is actually quadratic. If $\lambda$ is near $0$, the degree-$9$ polynomial overfits badly. If $\lambda$ is extremely large, the model is forced toward an almost flat function and underfits. With an intermediate value of $\lambda$, the learned curve recovers the correct broad quadratic shape without chasing every fluctuation.

The ridge-versus-LASSO geometry gives a second kind of example. Ridge prefers small but usually nonzero coefficients because the circular constraint does not naturally hit axes. LASSO's diamond-shaped geometry has corners on the coordinate axes, so the optimum often lands at a sparse point where some coefficients are exactly $0$.

---

Flashcards for this section are as follows:

- degree-9 regularization example ::@:: In the lecture's degree-$9$ polynomial example, very small $\lambda$ overfits, very large $\lambda$ underfits, and a medium $\lambda$ recovers the right broad shape. <!--SR:!2026-04-12,4,313!2026-04-12,4,323-->
- ridge-geometry example ::@:: Ridge's round geometry usually shrinks weights without setting them exactly to zero. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- LASSO-geometry example ::@:: LASSO's cornered $L_1$ geometry often makes the optimum land on an axis, so some coefficients become exactly zero. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->

## performance metrics for regression

The lecture separates the _training objective_ from the _evaluation metric_. In regression, the most common performance metric is the mean squared error, $\mathrm{MSE} = \frac{1}{N}\sum_{i=1}^N (y_i - \hat y_i)^2$. Unlike the training loss for a single example, MSE is an average over a dataset, so it can be used on the training set, validation set, or test set.

Because MSE squares the units of the target, it is sometimes harder to interpret directly. If the target is measured in meters, then the MSE is measured in square meters. That is why practitioners often report the root mean squared error, $\mathrm{RMSE} = \sqrt{\mathrm{MSE}}$, which returns the error to the same unit as the target variable.

The lecture also introduces the coefficient of determination, $R^2 = 1 - \frac{\sum_{i=1}^N (y_i - \hat y_i)^2}{\sum_{i=1}^N (y_i - \bar y)^2}$, where $\bar y = \frac{1}{N}\sum_{i=1}^N y_i$ is the sample mean. This compares the model against the baseline predictor that always outputs the mean target value. If the model achieves zero MSE, then $R^2 = 1$. If it does no better than always predicting $\bar y$, then $R^2 = 0$. If it performs even worse than that baseline, $R^2$ becomes negative.

For ordinary least squares there is also a useful orthogonality interpretation. If $e = y-\hat y$ is the residual vector, then the normal equation says $X^\top e = 0$. So the residuals are orthogonal to every feature column included in the design matrix. When an intercept is included, one of those columns is the all-ones vector, so the residuals additionally sum to zero. Even without an intercept, the sample inner products with the included regressors vanish at the least-squares solution.

---

Flashcards for this section are as follows:

- mean squared error metric ::@:: The mean squared error is $\mathrm{MSE} = \frac{1}{N}\sum_{i=1}^N (y_i - \hat y_i)^2$, the average squared prediction error over a dataset. <!--SR:!2026-04-12,4,313!2026-04-12,4,323-->
- why MSE can be used on validation and test sets ::@:: MSE is a dataset-level average error measure, so it can be computed on training, validation, or test data. <!--SR:!2026-04-12,4,313!2026-04-12,4,284-->
- RMSE ::@:: The root mean squared error is $\mathrm{RMSE} = \sqrt{\mathrm{MSE}}$, which restores the error to the same unit as the target variable. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- why RMSE is easier to interpret ::@:: RMSE is often easier to interpret than MSE because its unit matches the original response variable instead of squaring it. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- $R^2$ score formula ::@:: The coefficient of determination is $R^2 = 1 - \frac{\sum_{i=1}^N (y_i - \hat y_i)^2}{\sum_{i=1}^N (y_i - \bar y)^2}$, where $\bar y$ is the sample mean. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- meaning of $R^2 = 1$ ::@:: $R^2 = 1$ means the model predicts the targets perfectly, so the residual sum of squares is zero. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- meaning of $R^2 = 0$ ::@:: $R^2 = 0$ means the model performs no better than the baseline predictor that always outputs the mean target value. <!--SR:!2026-04-12,4,313!2026-04-12,4,322-->
- why $R^2$ can be negative ::@:: $R^2$ can be negative when the model performs worse than the mean-prediction baseline and therefore has an even larger residual sum of squares. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- OLS orthogonality interpretation of residuals ::@:: At the least-squares solution the residual vector $e=y-\hat y$ satisfies $X^\top e=0$, so it is orthogonal to every regressor included in the design matrix. <!--SR:!2026-04-12,4,301!2026-04-12,4,284-->

### mse and rmse interpretation

MSE is often best read as an average squared residual, not just as a formula. Squaring does two things at once: it removes sign cancellation and makes large mistakes dominate the score. That is good when large errors are especially undesirable, but it also means MSE can be sensitive to outliers.

RMSE keeps exactly the same model ranking as MSE because it is just a square root, but it is easier to explain to humans because it is back in the original unit of the target. If house-price error is measured in dollars, RMSE is also in dollars. So RMSE is usually the more interpretable headline metric, while MSE is often the more algebraically convenient optimization metric.

---

Flashcards for this section are as follows:

- intuitive meaning of MSE ::@:: MSE is the average squared residual, so it ignores error sign and makes large mistakes count more heavily than small ones. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- why MSE is sensitive to outliers ::@:: Because residuals are squared, a few large errors can dominate the MSE. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- why RMSE preserves model ranking ::@:: RMSE is just the square root of MSE, so it orders models the same way while being easier to interpret in the target's original unit. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->

### r squared intuition and alternative formulas

The $R^2$ score becomes easier to remember if you name the pieces. Let $\mathrm{TSS}=\sum_i (y_i-\bar y)^2$ be the total sum of squares, namely the total variation of the targets around their mean baseline. Let $\mathrm{RSS}=\sum_i (y_i-\hat y_i)^2$ be the residual sum of squares, namely the part still left unexplained after fitting the model. Let $\mathrm{ESS}=\sum_i (\hat y_i-\bar y)^2$ be the explained sum of squares, namely the amount of variation captured by the fitted values relative to the mean baseline. Then $R^2 = 1 - \mathrm{RSS}/\mathrm{TSS}$ says: start from the baseline variation in the targets and subtract the fraction that the model failed to explain.

The standard textbook interpretation now needs one important warning: the familiar decomposition $\mathrm{TSS}=\mathrm{ESS}+\mathrm{RSS}$ and the usual mean-baseline interpretation of $R^2$ assume that an intercept term is included in the model. When the model includes an intercept, OLS gives the decomposition $\mathrm{TSS}=\mathrm{ESS}+\mathrm{RSS}$. In that case $R^2 = \mathrm{ESS}/\mathrm{TSS}$ as well, so $R^2$ can be read as the fraction of total target variation explained by the fitted values. In simple linear regression with an intercept, this also matches the squared sample correlation between $y$ and $\hat y$.

The orthogonality condition $X^\top e=0$ provides the geometric intuition behind these identities. The residual component points in a direction orthogonal to the fitted subspace, so least squares decomposes the target vector into a fitted part plus an error part that cannot be improved by moving within the allowed hypothesis space. With an intercept this decomposition is centered around the mean baseline $\bar y$, which is why the common $R^2$ formulas line up so neatly.

---

Flashcards for this section are as follows:

- residual sum of squares and total sum of squares ::@:: In regression, $\mathrm{RSS}=\sum_i (y_i-\hat y_i)^2$ measures unexplained variation and $\mathrm{TSS}=\sum_i (y_i-\bar y)^2$ measures total variation around the mean. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- explained sum of squares ::@:: The explained sum of squares is $\mathrm{ESS}=\sum_i(\hat y_i-\bar y)^2$, which measures how much variation of the targets around the mean is captured by the fitted values. <!--SR:!2026-04-12,4,313!2026-04-12,4,323-->
- intuitive reading of $R^2 = 1-\mathrm{RSS}/\mathrm{TSS}$ ::@:: $R^2$ is one minus the unexplained fraction of total target variation, measured relative to the mean-prediction baseline. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- alternative $R^2$ formula with intercept ::@:: When an intercept is included, OLS gives $\mathrm{TSS}=\mathrm{ESS}+\mathrm{RSS}$, so $R^2 = \mathrm{ESS}/\mathrm{TSS}$ with $\mathrm{ESS}=\sum_i(\hat y_i-\bar y)^2$. <!--SR:!2026-04-12,4,270!2026-04-12,4,313-->
- intercept assumption behind the standard $R^2$ formulas ::@:: The usual mean-baseline interpretation of $R^2$ and the decomposition $\mathrm{TSS}=\mathrm{ESS}+\mathrm{RSS}$ assume that the regression model includes an intercept term. <!--SR:!2026-04-12,4,301!2026-04-12,4,301-->
- relation between OLS residuals and regressors ::@:: OLS residuals are orthogonal to all included regressors because the normal equation gives $X^\top(y-\hat y)=0$, regardless of whether an intercept is present. <!--SR:!2026-04-12,4,301!2026-04-12,4,313-->
- extra intercept consequence for residuals ::@:: If an intercept column is included in $X$, then $X^\top e=0$ implies the residuals sum to zero. <!--SR:!2026-04-12,4,284!2026-04-12,4,323-->

## probabilistic formulation of linear regression

The lecture's probabilistic upgrade begins by observing that the deterministic equation $y = w^\top x$ is often too rigid. Real outputs are influenced not only by the modeled features but also by unobserved causes, measurement error, and random fluctuations. So the model is rewritten as $y = w^\top x + \varepsilon$, where the noise term $\varepsilon$ captures the leftover variation.

To say this carefully, one treats the response $Y$ as a random variable: a numerical quantity whose value depends on the random outcome of the data-generating process. Likewise, the feature vector $X$ may be viewed as a random vector describing the observed input. For a particular training example we observe one realized pair $(x_i,y_i)$, but the probabilistic model is meant to describe the whole population-level relationship between the random variables $X$ and $Y$, not just one fixed dataset.

If one assumes $\varepsilon \sim \mathrm{N}(0,\sigma^2)$, then the conditional distribution of the response given the input becomes $p(y\mid x,\theta) = \mathrm{N}(y\mid \mu(x),\sigma^2)$ with mean $\mu(x) = w^\top x$. The point prediction is the mean of this Gaussian, namely $\hat y = \mu(x) = w^\top x$.

This interpretation is conceptually valuable because it turns regression from a single-number output rule into a conditional probability model. The model now says not only _where_ the response is centered, but also how much uncertainty surrounds that center through the variance parameter $\sigma^2$. In effect, the random variable $Y$ is modeled conditionally on the random input $X$: for each possible input value $x$, the model specifies a distribution for the output rather than just one hard answer.

Once the model is probabilistic, the optimization target also changes language. We are no longer merely "making errors small"; we are choosing parameters that make the observed outputs as probable as possible under the assumed conditional distribution. That means maximizing the likelihood $\prod_{i=1}^N p(y_i\mid x_i,\theta)$, or equivalently minimizing the average negative log-likelihood.

---

Flashcards for this section are as follows:

- Gaussian-noise interpretation $y = w^\top x + \varepsilon$ ::@:: Linear regression can be interpreted probabilistically by assuming $y = w^\top x + \varepsilon$ with Gaussian noise $\varepsilon \sim \mathrm{N}(0,\sigma^2)$. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- random variable in probabilistic linear regression ::@:: A random variable is a numerical quantity determined by the random data-generating process; in probabilistic linear regression, the response $Y$ is modeled as a random variable conditioned on the input $X$. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- why add a noise term ::@:: The noise term $\varepsilon$ captures unmodeled effects, measurement error, and other random variation not explained by the chosen features. <!--SR:!2026-04-12,4,284!2026-04-12,4,313-->
- conditional distribution of $y$ ::@:: Under the Gaussian-noise assumption, the conditional response model is $p(y\mid x,\theta) = \mathrm{N}(y\mid \mu(x),\sigma^2)$ with $\mu(x)=w^\top x$. <!--SR:!2026-04-12,4,284!2026-04-12,4,301-->
- point prediction from the probabilistic model ::@:: The point estimate in probabilistic linear regression is the Gaussian mean $\hat y = \mu(x)=w^\top x$. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- how random variables are used in the regression model ::@:: The probabilistic model describes the population-level relation between random input $X$ and random output $Y$ by specifying the conditional distribution of $Y$ given $X=x$. <!--SR:!2026-04-12,4,284!2026-04-12,4,322-->
- probabilistic objective in linear regression ::@:: In probabilistic linear regression, the parameters are chosen to maximize the conditional likelihood of the observed outputs, or equivalently to minimize average negative log-likelihood. <!--SR:!2026-04-12,4,313!2026-04-12,4,284-->

### likelihood objective and maximum likelihood

Assuming the training examples are conditionally independent given the parameters, the likelihood of the full dataset is $\mathcal{L}(\theta)=\prod_{i=1}^N p(y_i\mid x_i,\theta)$. Maximum likelihood estimation chooses the parameter value that makes the observed outputs most plausible under this model. Because products of many probabilities are awkward to optimize directly, one usually works with the log-likelihood $\log \mathcal{L}(\theta)=\sum_{i=1}^N \log p(y_i\mid x_i,\theta)$ instead.

Minimizing the average negative log-likelihood is the same optimization problem as maximizing the likelihood, but it is easier to connect to standard machine-learning losses. In this sense the probabilistic formulation is trying to optimize _fit to the observed data under the assumed noise model_, not just geometric distance in an abstract parameter space.

---

Flashcards for this section are as follows:

- likelihood of the regression dataset ::@:: Under conditional independence, the likelihood is $\mathcal{L}(\theta)=\prod_{i=1}^N p(y_i\mid x_i,\theta)$. <!--SR:!2026-04-12,4,284!2026-04-12,4,313-->
- maximum likelihood in words ::@:: Maximum likelihood chooses the parameters that make the observed outputs most plausible under the assumed probabilistic model. <!--SR:!2026-04-12,4,313!2026-04-12,4,322-->
- why use log-likelihood ::@:: Log-likelihood turns a product of conditional densities into a sum, which is easier to optimize and analyze. <!--SR:!2026-04-12,4,313!2026-04-12,4,323-->
- why negative log-likelihood is minimized ::@:: Minimizing negative log-likelihood is equivalent to maximizing likelihood, but it matches the usual loss-minimization language of machine learning. <!--SR:!2026-04-12,4,284!2026-04-12,4,284-->

### from Gaussian likelihood to least squares

Given independent training examples, parameter estimation can be formulated as minimizing the average negative log-likelihood, equivalently the cross entropy between the empirical data distribution and the model. For the Gaussian conditional model, the objective becomes $-\frac{1}{N}\sum_{i=1}^N \log p(y_i\mid x_i,\theta) = \frac{1}{N}\sum_{i=1}^N\Bigl[\frac{1}{2}\log(2\pi\sigma^2) + \frac{(y_i - w^\top x_i)^2}{2\sigma^2}\Bigr] = \frac{1}{2}\log(2\pi\sigma^2) + \frac{1}{2\sigma^2}\cdot\frac{1}{N}\sum_{i=1}^N (y_i - w^\top x_i)^2$.

This factorization makes the interpretation clearer. The outer factor $1/N$ says we are averaging the per-example loss over the dataset. Inside the brackets, the term $\frac{1}{2}\log(2\pi\sigma^2)$ is the Gaussian normalization penalty, while the term $\frac{(y_i - w^\top x_i)^2}{2\sigma^2}$ is the scaled squared residual for example $i$.

If $\sigma$ is treated as fixed, then the first term is constant and the scale factor $\frac{1}{2\sigma^2}$ is positive, so $\arg\min_w\Bigl[\frac{1}{2}\log(2\pi\sigma^2) + \frac{1}{2\sigma^2}\cdot\frac{1}{N}\sum_{i=1}^N (y_i - w^\top x_i)^2\Bigr] = \arg\min_w \frac{1}{N}\sum_{i=1}^N (y_i - w^\top x_i)^2$.

Therefore, minimizing the negative log-likelihood is equivalent to minimizing the mean squared error. This is the probabilistic justification for least squares emphasized at the end of the lecture.

Seen this way, least squares is not just an arbitrary algebraic criterion. Under a Gaussian noise assumption it is exactly the maximum-likelihood estimator, or equivalently the minimum-cross-entropy estimator, for the regression parameters. If $\sigma^2$ is also treated as unknown, the same framework additionally estimates the noise level; the optimizer for $w$ is still the ordinary least-squares solution, while the fitted variance becomes proportional to the residual sum of squares.

---

Flashcards for this section are as follows:

- average Gaussian negative log-likelihood with explicit $1/N$ ::@:: The Gaussian average negative log-likelihood can be written as $\frac{1}{N}\sum_i\Bigl[\frac{1}{2}\log(2\pi\sigma^2)+\frac{(y_i-w^\top x_i)^2}{2\sigma^2}\Bigr]$, which makes the dataset average explicit. <!--SR:!2026-04-12,4,313!2026-04-12,4,322-->
- interpretation of the inner Gaussian loss terms ::@:: In the per-example Gaussian negative log-likelihood, $\frac{1}{2}\log(2\pi\sigma^2)$ is the normalization term and $\frac{(y_i-w^\top x_i)^2}{2\sigma^2}$ is the scaled squared residual. <!--SR:!2026-04-12,4,284!2026-04-12,4,313-->
- why fixed $\sigma$ recovers least squares ::@:: If $\sigma$ is fixed, then $\arg\min_w\bigl[c + a\cdot \frac{1}{N}\sum_i (y_i-w^\top x_i)^2\bigr] = \arg\min_w \frac{1}{N}\sum_i (y_i-w^\top x_i)^2$ for constants $c$ and $a>0$, so Gaussian negative log-likelihood has the same minimizer as MSE. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- least squares as maximum likelihood ::@:: Under Gaussian output noise, ordinary least squares is the maximum-likelihood estimator for the regression weights. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- least squares as minimum cross entropy ::@:: The same Gaussian derivation shows that least squares can also be viewed as minimizing cross entropy between the empirical data and the conditional model. <!--SR:!2026-04-12,4,301!2026-04-12,4,284-->
- what happens if $\sigma^2$ is also estimated ::@:: If the Gaussian variance is unknown, the same maximum-likelihood framework still gives the ordinary least-squares weights and then sets the variance according to the residual size. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->

### deriving least squares from the Gaussian density

For one example, the Gaussian conditional density is $p(y\mid x,\theta)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\Bigl(-\frac{(y-w^\top x)^2}{2\sigma^2}\Bigr)$.

Taking the negative logarithm gives $-\log p(y\mid x,\theta)=\frac{1}{2}\log(2\pi\sigma^2)+\frac{(y-w^\top x)^2}{2\sigma^2}$.

Averaging over $N$ independent examples yields $-\frac{1}{N}\sum_{i=1}^N \log p(y_i\mid x_i,\theta)=\frac{1}{2}\log(2\pi\sigma^2)+\frac{1}{2N\sigma^2}\sum_{i=1}^N (y_i-w^\top x_i)^2$.

Now the key observation is simple: if $\sigma$ is fixed, then the first term is constant and the second term differs from MSE only by a positive scaling factor. So both objectives pick exactly the same minimizer. In other words, the probabilistic model is optimizing the same weights as OLS because under Gaussian noise the log-density decreases exactly in proportion to squared residual size.

---

Flashcards for this section are as follows:

- one-sample Gaussian negative log-likelihood ::@:: For one example with Gaussian output noise, $-\log p(y\mid x,\theta)=\frac{1}{2}\log(2\pi\sigma^2)+\frac{(y-w^\top x)^2}{2\sigma^2}$. <!--SR:!2026-04-12,4,301!2026-04-12,4,284-->
- dataset Gaussian objective ::@:: Averaging Gaussian negative log-likelihood over the dataset gives $\frac{1}{2}\log(2\pi\sigma^2)+\frac{1}{2N\sigma^2}\sum_{i=1}^N (y_i-w^\top x_i)^2$. <!--SR:!2026-04-12,4,313!2026-04-12,4,322-->
- why Gaussian likelihood penalizes squared residuals ::@:: In a Gaussian density the exponent is proportional to $-(y-w^\top x)^2$, so larger squared residuals directly reduce likelihood. <!--SR:!2026-04-12,4,313!2026-04-12,4,313-->
- why the Gaussian derivation is important ::@:: It shows that MSE is not arbitrary; it is the natural objective induced by a Gaussian conditional output model. <!--SR:!2026-04-12,4,270!2026-04-12,4,313-->

### likelihood derivation and cross entropy

The final slides stress a piece of course-wide vocabulary: the negative log-likelihood objective is also a cross-entropy objective. In the linear-regression setting, MSE appears as a special case of that more general probabilistic estimation principle.

This matters beyond the linear-regression setting. Later models change the conditional distribution from Gaussian to Bernoulli, categorical, or more complicated families, and the corresponding training objectives change with it. The regression case is the easiest place to see the template clearly: specify a probabilistic model, write down the negative log-likelihood, and then simplify it into an optimization objective.

---

Flashcards for this section are as follows:

- probabilistic training template ::@:: The general template is: specify a conditional probability model, write the negative log-likelihood, and simplify it into the training objective. <!--SR:!2026-04-12,4,313!2026-04-12,4,301-->
- cross-entropy viewpoint in linear regression ::@:: In Gaussian linear regression, minimizing negative log-likelihood is equivalent to minimizing a cross-entropy objective, which in turn reduces to MSE up to constants and positive scaling. <!--SR:!2026-04-12,4,301!2026-04-12,4,322-->
- why this derivation matters later ::@:: The probabilistic derivation of linear regression prepares the way for later models such as logistic regression, where changing the output distribution changes the loss function. <!--SR:!2026-04-12,4,284!2026-04-12,4,313-->
