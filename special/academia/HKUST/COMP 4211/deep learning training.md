---
aliases:
  - batch normalization
  - deep learning training
  - dropout
  - optimization algorithms
  - weight decay
tags:
  - flashcard/active/special/academia/HKUST/COMP_4211/deep_learning_training
  - language/in/English
---

<!-- check: ignore-file[two_sided_calc_warning]: concept note uses self-contained symbolic and comparison cards with all givens on the left-hand side -->

# deep learning training

Training a deep network is not just "run gradient descent on a bigger model." Once the course has introduced expressive feedforward networks, the next problem is training them reliably: deep models can overfit, optimize badly, and destabilize their own internal signals. Expressivity creates opportunity, but training methodology determines whether that opportunity is actually realized.

The lecture organizes the answer around four linked questions: how to regularize a large model, how to design better updates, how to change the global step size over time, and how to keep hidden activations numerically well behaved. These lead respectively to weight penalties and dropout, improved optimizers, learning-rate schedules, and batch normalization.

This note therefore treats deep-learning training as a coordinated design problem. The objective, update rule, schedule, and normalization layers interact, so concept pairs that look similar at first glance — especially L2 regularization versus weight decay, or Adam with L2 versus AdamW — must be separated carefully.

---

Flashcards for this section are as follows:

- overview ::@:: Deep-learning training must simultaneously control overfitting, improve optimization, stabilize activation and gradient scales, and choose how aggressively parameters move over time.
- four training questions ::@:: The lecture organizes deep-learning training around four linked questions: regularization, optimizer design, learning-rate scheduling, and normalization of hidden activations.
- why deep training is harder than fitting a shallow model ::@:: Deep models are harder to train because large parameter counts, anisotropic loss geometry, stochastic gradients, and drifting hidden-layer statistics all interact.
- coordinated-design viewpoint ::@:: Training deep networks well requires a coordinated design of objective, update rule, learning-rate schedule, and normalization layers rather than one isolated trick.
- why L2, weight decay, Adam, and batch normalization must be separated carefully ::@:: These techniques affect different parts of the training pipeline — loss, update rule, adaptive scaling, or hidden-layer statistics — so conflating them hides important practical differences.

## weight decay, bagging intuition, and dropout

The lecture begins regularization from three complementary angles: penalize large coefficients in the objective, shrink parameters directly in the update rule, or inject randomness into the architecture during training. These ideas are related but not identical. The most common confusion is to treat "L2 regularization," "weight decay," and "dropout" as if they were three versions of the same trick.

Regularization is also tied to geometry. It is not only about "preferring small weights"; it is about what counts as a "large" weight relative to feature scale. If the data geometry is badly unbalanced, then both the optimization path and the meaning of an L1 or L2 penalty become distorted. That is why the note starts with feature-scale effects before returning to dropout and subnetworks.

---

Flashcards for this section are as follows:

- three regularization levers in this lecture ::@:: The lecture regularizes deep networks by (i) penalty terms in the objective, (ii) direct parameter shrinkage in the update rule, and (iii) stochastic masking of subnetworks through dropout.
- why regularization and geometry are linked ::@:: The meaning of "large weight" depends on feature scale, so regularization strength and optimization geometry must be understood together rather than separately.
- why weight decay and dropout complement each other ::@:: Weight decay directly discourages large parameters, whereas dropout discourages brittle reliance on specific units or paths through the network.
- why L2 regularization, weight decay, and dropout should not be conflated ::@:: L2 regularization changes the loss, weight decay changes the update rule, and dropout changes the active architecture seen during training.

### feature scale, regularization geometry, and weight decay

To see why feature scale matters, first look at a simple squared-loss model $L(w)=\frac{1}{2N}\lVert Xw-y\rVert_2^2$. Its gradient is $\nabla_w L=\frac{1}{N}X^\top(Xw-y)$ and its Hessian is $H=\frac{1}{N}X^\top X$. If one column of $X$ is much larger in scale than another, then the eigenvalues of $H$ become highly uneven. Geometrically, the loss contours become elongated ellipses rather than roughly round bowls. Gradient descent then zig-zags: the learning rate must be small enough for the steep direction, so progress in the shallow direction becomes slow.

That same scale mismatch changes the meaning of regularization. Suppose one rescales feature $x_j$ to $x_j'=s x_j$ and compensates so the prediction stays unchanged by setting $w_j'=w_j/s$. Then the predictive contribution $w_j x_j$ is unchanged, but the regularizers are not. The L2 term becomes $\frac{\lambda}{2}(w_j')^2=\frac{\lambda}{2}\frac{w_j^2}{s^2}$, and the L1 term becomes $\lambda|w_j'|=\lambda\frac{|w_j|}{|s|}$. So for the same predictive effect, a larger-scale feature can achieve that effect with a numerically smaller coefficient and is therefore penalized less by both L2 and L1. This is the concrete reason regularization depends on feature scale.

A tiny example makes the asymmetry obvious. If one feature is $x_2=100x_1$, then the same contribution can be written as $1\cdot x_1$ or $0.01\cdot x_2$. The L2 penalties of these equivalent predictive effects are proportional to $1^2=1$ versus $0.01^2=10^{-4}$, and the L1 penalties are proportional to $1$ versus $0.01$. Without normalization, both L2 and L1 implicitly favor the large-scale feature because it can "buy" the same prediction with a much smaller coefficient.

Against that background, the distinction between L2 regularization and weight decay must be stated precisely. L2 regularization is an _objective-level_ modification. A common convention is $\tilde L(\theta)=L(\theta)+\frac{\lambda}{2}\lVert\theta\rVert_2^2$, where the factor $\frac{1}{2}$ is included so that $\nabla_\theta \frac{\lambda}{2}\lVert\theta\rVert_2^2=\lambda\theta$. Weight decay, by contrast, is an _update-level_ rule: the optimizer explicitly shrinks the parameter vector at each step, for example $\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\nabla_\theta L(\theta_t)$.

Under plain gradient descent or plain stochastic gradient descent, these two viewpoints are equivalent up to the coefficient convention. If one optimizes $\tilde L(\theta)=L(\theta)+\frac{\lambda}{2}\lVert\theta\rVert_2^2$, then $\theta_{t+1}=\theta_t-\eta(\nabla_\theta L(\theta_t)+\lambda\theta_t)=(1-\eta\lambda)\theta_t-\eta\nabla_\theta L(\theta_t)$, which is exactly the standard weight-decay update. If instead one writes the penalty without the factor $\frac{1}{2}$, namely $\tilde L(\theta)=L(\theta)+\lambda\lVert\theta\rVert_2^2$, then the update becomes $\theta_{t+1}=(1-2\eta\lambda)\theta_t-\eta\nabla_\theta L(\theta_t)$. So the shrinkage effect is the same, but the numerical meaning of $\lambda$ differs by a factor of $2$.

This equivalence is fragile: it relies on using plain gradient descent without adaptive preconditioning, momentum coupling, or other history-dependent transformations. Once the optimizer changes the way gradients are rescaled, L2 regularization and weight decay are no longer the same operation. That is exactly the issue that later motivates AdamW.

---

Flashcards for this section are as follows:

- elongated loss geometry from uneven feature scales / $H=\frac{1}{N}X^\top X$ ::@:: If feature scales are very uneven, then the Hessian $H=\frac{1}{N}X^\top X$ becomes ill-conditioned, loss contours become elongated, and gradient descent must use a small learning rate for the steep direction, slowing progress in shallow directions.
- why uneven data gives uneven gradients / $\nabla_w L=\frac{1}{N}X^\top(Xw-y)$ ::@:: Because $\nabla_w L=\frac{1}{N}X^\top(Xw-y)$, a large-scale feature column contributes proportionally larger gradient magnitudes, so updates become unbalanced across coordinates.
- feature rescaling and L2 penalty / $x_j'=s x_j$, $w_j'=w_j/s$ ::@:: If $x_j'=s x_j$ and the same prediction is preserved by $w_j'=w_j/s$, then the L2 term becomes $\frac{\lambda}{2}(w_j')^2=\frac{\lambda}{2}\frac{w_j^2}{s^2}$, so a larger-scale feature is penalized less for the same predictive effect.
- feature rescaling and L1 penalty / $x_j'=s x_j$, $w_j'=w_j/s$ ::@:: If $x_j'=s x_j$ and $w_j'=w_j/s$, then the L1 term becomes $\lambda|w_j'|=\lambda\frac{|w_j|}{|s|}$, so L1 regularization also depends on feature scale.
- given two equivalent predictive effects $1\cdot x_1$ and $0.01\cdot x_2$ with $x_2=100x_1$, compare their L2 and L1 penalty magnitudes ::@:: The L2 magnitudes are $1^2=1$ versus $0.01^2=10^{-4}$, and the L1 magnitudes are $1$ versus $0.01$, so the large-scale feature is penalized far less for the same prediction.
- L2 regularization with factor $\frac{1}{2}$ / $\tilde L(\theta)=L(\theta)+\frac{\lambda}{2}\lVert\theta\rVert_2^2$ ::@:: L2 regularization is an objective-level modification: one optimizes $\tilde L(\theta)=L(\theta)+\frac{\lambda}{2}\lVert\theta\rVert_2^2$, whose penalty gradient is $\lambda\theta$.
- weight decay / update $\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\nabla_\theta L(\theta_t)$ ::@:: Weight decay is an update-level rule: the optimizer directly shrinks parameters by a multiplicative factor such as $(1-\eta\lambda)$ before or alongside the data-gradient step.
- L2 regularization versus weight decay ::@:: L2 regularization changes the loss by adding a penalty term, whereas weight decay changes the update rule by directly shrinking parameters; they are conceptually distinct even when they coincide under plain gradient descent.
- equivalence under plain gradient descent / factor $\frac{1}{2}$ convention ::@:: If $\tilde L(\theta)=L(\theta)+\frac{\lambda}{2}\lVert\theta\rVert_2^2$, then plain gradient descent gives $\theta_{t+1}=\theta_t-\eta(\nabla_\theta L(\theta_t)+\lambda\theta_t)=(1-\eta\lambda)\theta_t-\eta\nabla_\theta L(\theta_t)$, which is exactly weight decay.
- equivalence under plain gradient descent / no factor $\frac{1}{2}$ convention ::@:: If $\tilde L(\theta)=L(\theta)+\lambda\lVert\theta\rVert_2^2$, then plain gradient descent gives $\theta_{t+1}=\theta_t-\eta(\nabla_\theta L(\theta_t)+2\lambda\theta_t)=(1-2\eta\lambda)\theta_t-\eta\nabla_\theta L(\theta_t)$, so it is still weight decay but with a different coefficient convention.
- given scalar parameter $\theta_t=2$, learning rate $\eta=0.1$, regularization coefficient $\lambda=0.05$, and no data-gradient term, compare the plain-GD updates for (i) $\tilde L=L+\frac{\lambda}{2}\lVert\theta\rVert_2^2$ and (ii) $\tilde L=L+\lambda\lVert\theta\rVert_2^2$ ::@:: For (i), $\theta_{t+1}=(1-\eta\lambda)\theta_t=(1-0.005)\cdot 2=1.99$; for (ii), $\theta_{t+1}=(1-2\eta\lambda)\theta_t=(1-0.01)\cdot 2=1.98$.

### bagging intuition and subnetworks

Bagging reduces variance by training several models on perturbed datasets and then averaging or voting across them. If one tried to do this literally for a large neural network, the cost would be enormous: one would need many separately trained deep models. Dropout keeps the ensemble intuition but makes it cheap through parameter sharing.

The right object to imagine is a _subnetwork_. Once a dropout mask is sampled, only some units remain active, so the full network is replaced by an induced active subgraph for that minibatch. Different masks therefore correspond to different subnetworks. In that sense, dropout performs rough stochastic _subnetwork selection_ inside one shared super-network.

This is only an approximation to bagging, not an exact equality. Classical bagging uses independently trained models and often bootstrap-resampled datasets. Dropout instead shares parameters across subnetworks and reuses the same training run. So the best mental model is _cheap shared-parameter model averaging_, not "dropout literally equals bagging."

The phrase _complex co-adaptations_ explains what dropout is trying to prevent. A complex co-adaptation is a brittle dependency such as "unit $j$ only becomes useful when a very specific set of partner units is present." That makes the representation fragile: small architectural or data perturbations can destroy the useful pathway. By repeatedly removing random units, dropout forces features to remain useful under many different partner configurations. Features therefore become more robust and less reliant on one narrow internal conspiracy.

Stochastic gradient descent makes this intuition operational. On minibatch $\mathcal B_t$, one samples masks, runs forward propagation through the selected subnetwork, computes the minibatch loss, and updates the shared parameters that were active under that mask. On the next minibatch, the mask changes, so a different subnetwork is updated. Over many updates, dropout plus SGD behaves like rough stochastic ensemble training over many parameter-sharing subnetworks.

---

Flashcards for this section are as follows:

- bagging intuition for dropout ::@:: Bagging reduces variance by averaging multiple models, and dropout borrows that intuition by making many subnetworks contribute through one shared network.
- what subnetwork selection means in dropout ::@:: A dropout mask selects an active induced subgraph of the full network, so each minibatch trains one sampled subnetwork inside a larger shared super-network.
- why literal neural-network bagging is impractical ::@:: Training many independent deep networks would be too computationally expensive, which is why dropout uses parameter sharing instead of separate full models.
- why dropout is only an approximation to bagging ::@:: Dropout is only an approximation to bagging because the subnetworks share parameters, are trained inside one run, and are not independently fit on separate bootstrap datasets.
- complex co-adaptations in dropout ::@:: Complex co-adaptations are brittle dependencies in which a unit becomes useful only when a very specific set of partner units is also active; dropout discourages such fragile teamwork.
- how dropout and SGD create rough subnetwork bagging ::@:: On each minibatch, dropout samples a mask, trains the corresponding subnetwork by SGD on shared parameters, then resamples on the next minibatch, so repeated updates behave like rough stochastic subnetwork selection and approximate ensemble training.

### masking, minibatches, and test-time scaling

At each training step, each selected hidden layer is given a binary mask. If the keep probability is $q=1-p$ and $m^{(\ell)}\in\{0,1\}^{d_\ell}$ is a Bernoulli mask for layer $\ell$, then the masked activation is formed by elementwise multiplication. For vectors of the same shape, the Hadamard product is defined by $(u\odot v)_i=u_i v_i$, and elementwise division is $(u\oslash v)_i=u_i/v_i$. Using that notation, standard dropout writes $\tilde a^{(\ell)}=m^{(\ell)}\odot a^{(\ell)}$.

The crucial clarification is that dropout masks _unit activations_, not weights. The activated outputs of a layer are multiplied by the mask; the weight parameters themselves are not randomly set to zero. If layer $\ell+1$ uses pre-activation $z^{(\ell+1)}=(W^{(\ell+1)})^\top \tilde a^{(\ell)}+b^{(\ell+1)}$, then the mask acts on $a^{(\ell)}$, which is the output of the dropout-applied layer.

One can write the dropout procedure step by step:

1. choose which layers use dropout and which layers do not;
2. for each selected layer, sample an independent Bernoulli mask for eligible units;
3. multiply that layer's activated outputs by the mask, or by a scaled mask in inverted dropout;
4. run forward propagation through the resulting sampled subnetwork;
5. run backpropagation and update only the parameters on active paths for that minibatch;
6. repeat with fresh masks on the next minibatch;
7. at inference time, turn off dropout and use whichever scaling convention makes training-time and test-time activation magnitudes consistent.

The gradient effect is immediate from the chain rule. Under standard dropout, if a downstream pre-activation is $z_k=\sum_j w_{jk}\tilde a_j+b_k=\sum_j w_{jk}m_j a_j+b_k$, then $\frac{\partial L}{\partial w_{jk}}=\frac{\partial L}{\partial z_k}\frac{\partial z_k}{\partial w_{jk}}=\delta_k m_j a_j$. So when $m_j=0$, the corresponding weight gradient is exactly $0$. Likewise $\frac{\partial L}{\partial a_j}=m_j\sum_k w_{jk}\delta_k$, so a masked unit also sends no activation gradient backward on that step. In inverted dropout, the same derivation gives an extra factor $1/q$: $\frac{\partial L}{\partial w_{jk}}=\delta_k \frac{m_j}{q}a_j$ and $\frac{\partial L}{\partial a_j}=\frac{m_j}{q}\sum_k w_{jk}\delta_k$. The key point remains: if the unit is dropped, its local path contributes no gradient for that minibatch.

The lecture stresses that dropout is naturally paired with minibatch SGD. Each minibatch samples a fresh mask and therefore a fresh subnetwork. The optimizer is not following one fixed deterministic architecture; it is moving through parameter space while repeatedly changing which internal routes are active.

There is also an important test-time scaling issue. If dropout is used only during training, then at inference each surviving unit receives, on average, about $1/q=1/(1-p)$ times as many active inputs as it did during training. When $p=0.5$, that means roughly twice as many active inputs. Without compensation, the test-time signal would therefore be systematically too large.

There are two standard fixes, and the timing matters. In the _non-inverted_ convention, training uses $\tilde a^{(\ell)}=m^{(\ell)}\odot a^{(\ell)}$, and then _after training_ one scales the weights that come _after the output of the dropout-applied layer_. Concretely, if dropout is applied to layer $\ell$, then after training one replaces the next layer's weight matrix $W^{(\ell+1)}$ by $qW^{(\ell+1)}$. This scaling is not performed during training; it is a post-training inference fix for the connections leaving the dropout-applied layer.

In the _inverted-dropout_ convention, one does _not_ modify weights after training. Instead, during training one divides the kept activations directly by the keep probability: $\tilde a^{(\ell)}=(m^{(\ell)}\odot a^{(\ell)})\oslash q$. Because $\mathbb E[m_j]=q$, standard dropout gives $\mathbb E[m_j a_j]=q a_j$, whereas inverted dropout gives $\mathbb E[(m_j a_j)/q]=a_j$. So the expected activation already matches inference, and test time can use the original unmasked weights with no extra correction.

For a tiny numeric example, suppose one activation is $a_j=8$ and the dropout probability is $p=0.25$, so $q=0.75$. Under inverted dropout the unit is either dropped to $0$ with probability $0.25$, or kept as $8/0.75\approx 10.67$ with probability $0.75$. The expected value is $0.25\cdot 0+0.75\cdot 10.67\approx 8$, which is exactly the original activation level.

---

Flashcards for this section are as follows:

- Hadamard product and division ::@:: For same-shape vectors, the Hadamard product is $(u\odot v)_i=u_i v_i$ and elementwise division is $(u\oslash v)_i=u_i/v_i$.
- what dropout actually masks ::@:: Dropout masks unit activations, meaning the activated outputs of a layer are multiplied by a binary mask; it does not randomly zero weight parameters.
- dropout steps ::@:: A dropout training cycle is: choose dropout-applied layers, sample unit masks, multiply activations by masks, run forward propagation, backpropagate, update only active paths, then resample masks on the next minibatch.
- why masked units are not updated / $\partial L/\partial w_{jk}=\delta_k m_j a_j$ ::@:: If $z_k=\sum_j w_{jk}m_j a_j+b_k$, then $\frac{\partial L}{\partial w_{jk}}=\delta_k m_j a_j$, so when $m_j=0$ the corresponding weight gradient is exactly $0$.
- activation-gradient effect of dropout / $\partial L/\partial a_j=m_j\sum_k w_{jk}\delta_k$ ::@:: Because $\frac{\partial L}{\partial a_j}=m_j\sum_k w_{jk}\delta_k$, a masked unit also sends no activation gradient backward through that training step.
- why dropout is naturally paired with SGD ::@:: Dropout is naturally used with minibatch-based methods because a new mask pattern can be sampled for each minibatch update.
- standard dropout training formula and post-training fix / $\tilde a^{(\ell)}=m^{(\ell)}\odot a^{(\ell)}$ ::@:: Standard dropout trains with $\tilde a^{(\ell)}=m^{(\ell)}\odot a^{(\ell)}$, then _after training_ scales the next layer's weights leaving the dropout-applied layer, replacing $W^{(\ell+1)}$ by $qW^{(\ell+1)}$.
- which weights are modified in the non-inverted post-training fix ::@:: If dropout is applied to layer $\ell$, then the post-training scaling is applied to the weights _after the output of that layer_, namely the connections from layer $\ell$ to layer $\ell+1$.
- inverted dropout training formula and timing / $\tilde a^{(\ell)}=(m^{(\ell)}\odot a^{(\ell)})\oslash q$ ::@:: In inverted dropout, one divides the kept activations directly by $q=1-p$ during training, uses no post-training weight modification, and keeps the ordinary unmasked network at inference.
- why inverted dropout preserves expected activation / $\mathbb E\!\left[(m_j a_j)/q\right]=a_j$ ::@:: Because $\mathbb E[m_j]=q$, inverted dropout gives $\mathbb E\!\left[(m_j a_j)/q\right]=a_j$, so the expected activation already matches test-time inference.
- dropout can be applied layer by layer ::@:: Dropout is a layerwise design choice: some layers may use dropout while others do not.
- given activation $a_j=8$, dropout probability $p=0.25$, keep probability $q=0.75$, and inverted dropout, what values can the masked activation take and what is its expectation? ::@:: It becomes $0$ with probability $0.25$ or $8/0.75\approx 10.67$ with probability $0.75$, and the expectation is $8$.

## optimization algorithms for deep networks

The optimization problem is still "minimize loss over parameters," but deep networks make this harder than it sounds. The loss is high-dimensional, minibatch gradients are noisy, and different directions can have very different curvature. Vanilla minibatch SGD therefore remains the baseline, but it is only the beginning. If a minibatch gradient is $g_t=\frac{1}{B}\sum_{i\in\mathcal B_t}\nabla_\theta \ell_i(\theta_t)$, then basic SGD uses $\theta_{t+1}=\theta_t-\eta g_t$.

The lecture then studies how to modify this update. Momentum changes how the past influences the current direction. Adaptive learning-rate methods change how different coordinates are scaled. Adam combines both ideas, and AdamW decouples weight decay from that adaptive machinery. Separately, learning-rate schedules change the global step-size pattern over time. So optimizer design has two layers: _direction and preconditioning inside one step_, and _overall step-size policy across training_.

---

Flashcards for this section are as follows:

- SGD in deep learning / update $\theta_{t+1}=\theta_t-\eta g_t$ ::@:: If $g_t=\frac{1}{B}\sum_{i\in\mathcal B_t}\nabla_\theta \ell_i(\theta_t)$ is the minibatch gradient, then vanilla SGD updates by $\theta_{t+1}=\theta_t-\eta g_t$.
- why deep optimization is hard ::@:: Deep-learning optimization is hard because the loss landscape is high-dimensional, noisy, and often poorly conditioned.
- two layers of optimizer design ::@:: Optimizer design has an inner layer that changes direction or coordinatewise scaling inside one step, and an outer layer that changes the global learning rate across training.
- optimizer choice matters ::@:: Different optimizers can produce very different training behavior even when the model and data are unchanged.

### optimizer-state initialization

Before comparing update rules, it helps to distinguish _parameter initialization_ from _optimizer-state initialization_. Parameter initialization chooses the starting network weights $\theta_0$. Optimizer-state initialization chooses the extra memory variables used by the optimizer after $\theta_0$ has been set. These are different design choices.

Vanilla SGD has essentially no extra state beyond the current parameters, so after choosing $\theta_0$ it can start immediately. Momentum introduces a velocity state and typically initializes $v_0=0$. AdaGrad introduces an accumulator of squared gradients and usually initializes $s_0=0$. RMSProp also uses a squared-gradient accumulator, usually initialized at $0$ as well, though some implementations use a very small positive value. Adam uses both first- and second-moment states and almost always initializes $m_0=0$ and $v_0=0$.

These zero initializations are natural because they encode "no history yet." But they also explain why bias correction is needed in Adam: early moving averages underweight the true gradient history simply because the optimizer has not had enough time to accumulate it yet.

---

Flashcards for this section are as follows:

- parameter initialization versus optimizer-state initialization ::@:: Parameter initialization chooses the starting model weights $\theta_0$, whereas optimizer-state initialization chooses any extra memory variables such as velocity or moment accumulators.
- optimizer state for vanilla SGD ::@:: Vanilla SGD has essentially no extra optimizer state beyond the current parameter vector.
- momentum-state initialization ::@:: Momentum introduces a velocity state and typically initializes it as $v_0=0$.
- AdaGrad and RMSProp state initialization ::@:: AdaGrad and RMSProp use squared-gradient accumulators, typically initialized as $s_0=0$.
- Adam state initialization ::@:: Adam introduces first- and second-moment states and typically initializes them as $m_0=0$ and $v_0=0$.
- why zero state initialization matters in Adam ::@:: Zero initialization means the early moment estimates have not yet accumulated a full history, which is exactly why Adam needs bias correction in its first few steps.

### momentum and velocity-based updates

The lecture interprets momentum mechanically: think of the parameter vector as a particle moving through parameter space. Plain SGD reacts only to the current gradient. Classical momentum introduces a velocity state $v_t$ that carries memory from earlier steps. In one common form, $v_t=\beta v_{t-1}-\eta g_t$ and $\theta_{t+1}=\theta_t+v_t$, where $\beta\in(0,1)$ is the momentum coefficient.

This extra state reduces oscillation. Instead of zig-zagging sharply across a narrow valley, the optimization accumulates speed in directions where gradients are consistently aligned and damps directions where the sign keeps alternating. That is why momentum often accelerates learning and makes the optimization path smoother. The lecture notes that $\beta$ is often chosen around $0.5$, $0.9$, or $0.99$.

Adam also has a momentum-like piece, but it is written differently. Adam's first-moment estimate is $m_t=\beta_1 m_{t-1}+(1-\beta_1)g_t$. This looks like momentum because it is an exponentially weighted average of gradients, but it is not the same object as the classical velocity $v_t$. Classical momentum already includes the learning rate and is itself the step that gets added to the parameters. Adam's $m_t$ is a running average of gradients that is later bias-corrected and divided by an adaptive denominator before it becomes a step.

So the clean comparison is this: classical momentum stores a _velocity-like update state_, whereas Adam stores a _gradient-average state_. If one froze Adam's denominator at $1$ and ignored bias correction, Adam's first moment would resemble a normalized exponential-average version of momentum, but in the full Adam algorithm it is only one ingredient of the final update.

For a tiny numeric example, let $\beta=0.9$, previous velocity $v_{t-1}=-0.4$, current gradient $g_t=3$, learning rate $\eta=0.1$, and current parameter $\theta_t=5$. Then $v_t=0.9(-0.4)-0.1(3)=-0.66$, so $\theta_{t+1}=5-0.66=4.34$. If instead one tracks an Adam-style first moment with $\beta_1=0.9$, previous $m_{t-1}=0.6$, and the same gradient $g_t=3$, then $m_t=0.9(0.6)+0.1(3)=0.84$. That $0.84$ is not yet the parameter step; it still has to go through bias correction and adaptive scaling in Adam.

---

Flashcards for this section are as follows:

- momentum as particle analogy ::@:: Momentum treats the parameter vector as a particle whose motion depends not only on the current gradient but also on an accumulated velocity.
- classical momentum update equations / $v_t=\beta v_{t-1}-\eta g_t$, $\theta_{t+1}=\theta_t+v_t$ ::@:: In one common form, momentum uses $v_t=\beta v_{t-1}-\eta g_t$ and $\theta_{t+1}=\theta_t+v_t$, so the update mixes the current gradient with past velocity.
- why momentum reduces zig-zagging ::@:: Momentum smooths the update direction by averaging gradients over time, which reduces oscillation across steep narrow directions.
- classical momentum versus Adam first moment ::@:: Classical momentum stores a velocity-like step state $v_t$, whereas Adam stores a gradient-average state $m_t=\beta_1 m_{t-1}+(1-\beta_1)g_t$ that is later bias-corrected and adaptively rescaled.
- Adam first-moment formula ::@:: Adam's momentum-like component is $m_t=\beta_1 m_{t-1}+(1-\beta_1)g_t$, which is an exponentially weighted average of gradients rather than a full parameter-step vector.
- why Adam's first moment is not literally classical momentum ::@:: Adam's $m_t$ is not itself the final step because it must still be bias-corrected and divided by the adaptive denominator $\sqrt{\hat v_t}+\varepsilon$.
- typical momentum coefficients $0.5$, $0.9$, and $0.99$ ::@:: The lecture notes typical momentum hyperparameters such as $0.5$, $0.9$, and $0.99$.
- given $\beta=0.9$, previous velocity $v_{t-1}=-0.4$, gradient $g_t=3$, learning rate $\eta=0.1$, and parameter $\theta_t=5$, compute $v_t$ and $\theta_{t+1}$ for momentum SGD ::@:: We get $v_t=0.9(-0.4)-0.1(3)=-0.66$ and $\theta_{t+1}=5-0.66=4.34$.
- given $\beta_1=0.9$, previous Adam first moment $m_{t-1}=0.6$, and current gradient $g_t=3$, compute the new first moment $m_t$ ::@:: We get $m_t=0.9(0.6)+0.1(3)=0.84$.

### adaptive learning rates: AdaGrad and RMSProp

Adaptive learning-rate methods try to fix a different weakness of plain SGD: one global learning rate treats all coordinates as if they had the same gradient history. In practice, some coordinates repeatedly receive large gradients while others remain small or sparse. Adaptive methods therefore divide each coordinate by an estimate of its historical scale.

AdaGrad uses the cumulative squared-gradient accumulator $s_t=s_{t-1}+g_t\odot g_t$ and the update $\theta_{t+1}=\theta_t-\eta\,g_t\oslash(\sqrt{s_t}+\varepsilon)$. Coordinates that have accumulated many large gradients get larger $s_t$ and therefore smaller effective future steps. This is useful for sparse problems, but in long runs the ever-growing accumulator can shrink steps too aggressively.

RMSProp changes only one idea: instead of remembering all past squared gradients forever, it uses an exponentially decaying average, for example $s_t=\rho s_{t-1}+(1-\rho)g_t\odot g_t$. The original RMSProp paper places the numeric-stability constant _inside_ the square root, giving an update of the form $\theta_{t+1}=\theta_t-\eta\,g_t\oslash\sqrt{s_t+\varepsilon}$. Many later implementations write $\theta_{t+1}=\theta_t-\eta\,g_t\oslash(\sqrt{s_t}+\varepsilon)$ instead. Both versions aim at the same idea — adaptive scaling plus numeric stability — but the original paper's notation puts $\varepsilon$ inside the root. So AdaGrad has _infinite memory_ of squared gradients, while RMSProp has _fading memory_. That is why RMSProp usually avoids the severe long-run learning-rate collapse that AdaGrad can suffer.

The notation is already close to Adam. Adam will later use the same general denominator pattern, but with a second-moment estimate $v_t$ and a first-moment estimate $m_t$. This is one reason Adam's equations feel more uniform: momentum-like memory and adaptive scaling can both be expressed in the same elementwise tensor language.

The small constant $\varepsilon$ is not decorative. It provides numeric stability: if some coordinate has an extremely small accumulator, then division by $\sqrt{s_t}$ alone could create an enormous or undefined step. Adding $\varepsilon$ prevents division by zero and caps such explosive amplification. For RMSProp specifically, note again that the original paper writes this stabilization as $\sqrt{s_t+\varepsilon}$ rather than $\sqrt{s_t}+\varepsilon$.

For a small scalar comparison, suppose the current gradient is $g_t=3$, the learning rate is $\eta=0.1$, AdaGrad has previous accumulator $s_{t-1}=4$, and RMSProp has previous accumulator $s_{t-1}=4$ with $\rho=0.9$. Then AdaGrad gives $s_t=4+9=13$ and step magnitude $0.1\cdot 3/\sqrt{13}\approx 0.083$. RMSProp gives $s_t=0.9\cdot 4+0.1\cdot 9=4.5$ and step magnitude $0.1\cdot 3/\sqrt{4.5}\approx 0.141$. The example shows the conceptual difference: AdaGrad keeps shrinking more because it remembers the full past.

---

Flashcards for this section are as follows:

- AdaGrad idea / $s_t=s_{t-1}+g_t\odot g_t$, $\theta_{t+1}=\theta_t-\eta\,g_t\oslash(\sqrt{s_t}+\varepsilon)$ ::@:: AdaGrad accumulates squared gradients as $s_t=s_{t-1}+g_t\odot g_t$ and updates with $\theta_{t+1}=\theta_t-\eta\,g_t\oslash(\sqrt{s_t}+\varepsilon)$.
- weakness of AdaGrad ::@:: AdaGrad can shrink effective learning rates too aggressively because it keeps all historical squared gradients forever.
- RMSProp idea / $s_t=\rho s_{t-1}+(1-\rho)g_t\odot g_t$ ::@:: RMSProp uses an exponentially decaying average such as $s_t=\rho s_{t-1}+(1-\rho)g_t\odot g_t$, so it keeps adaptive scaling but forgets the extreme past.
- AdaGrad versus RMSProp ::@:: AdaGrad has full cumulative memory of squared gradients, whereas RMSProp keeps only an exponentially decaying memory, so RMSProp usually avoids over-shrinking the step size in long runs.
- why the denominator uses $\sqrt{s_t}+\varepsilon$ or $\sqrt{s_t+\varepsilon}$ ::@:: The square root converts squared-gradient scale back to gradient scale, and $\varepsilon$ provides numeric stability so tiny accumulators do not cause division by zero or huge steps; in the original RMSProp paper the stabilization is written as $\sqrt{s_t+\varepsilon}$, with $\varepsilon$ inside the square root.
- original RMSProp denominator placement ::@:: The original RMSProp paper writes the denominator as $\sqrt{s_t+\varepsilon}$, whereas many later implementations use $\sqrt{s_t}+\varepsilon$.
- how Adam relates to AdaGrad and RMSProp ::@:: Adam reuses the RMSProp-style idea of dividing by an adaptive second-moment estimate, but combines it with a momentum-like first-moment estimate in one uniform elementwise update rule.
- given scalar gradient $g_t=3$, learning rate $\eta=0.1$, AdaGrad previous accumulator $s_{t-1}=4$, and RMSProp previous accumulator $s_{t-1}=4$ with $\rho=0.9$, compare one AdaGrad step magnitude with one RMSProp step magnitude ::@:: AdaGrad gives $s_t=13$ and step magnitude $0.1\cdot 3/\sqrt{13}\approx 0.083$, while RMSProp gives $s_t=4.5$ and step magnitude $0.1\cdot 3/\sqrt{4.5}\approx 0.141$.

<!-- check: ignore-next-line[header_style]: preserve proper-noun optimizer names -->
### Adam and AdamW

Adam combines the momentum-like first moment and the adaptive second moment into one update. In standard elementwise notation, $m_t=\beta_1 m_{t-1}+(1-\beta_1)g_t$, $v_t=\beta_2 v_{t-1}+(1-\beta_2)(g_t\odot g_t)$, $\hat m_t=m_t/(1-\beta_1^t)$, $\hat v_t=v_t/(1-\beta_2^t)$, and $\theta_{t+1}=\theta_t-\eta\,\hat m_t\oslash(\sqrt{\hat v_t}+\varepsilon)$. One reason Adam feels algebraically neat is that its equations are highly uniform: every coordinate uses the same tensorwise recipe of _average gradients, average squared gradients, bias-correct, divide elementwise, then step_.

Bias correction appears because the moving averages start at zero. The clean derivation comes from unrolling the recursion. For the first moment, $$m_t=\beta_1^t m_0 + (1-\beta_1)\sum_{i=1}^{t} \beta_1^{t-i} g_i.$$ With the standard initialization $m_0=0$, this becomes $$m_t=(1-\beta_1)\sum_{i=1}^{t} \beta_1^{t-i} g_i.$$ The observed gradient weights therefore sum to $$ (1-\beta_1)\sum_{i=1}^{t} \beta_1^{t-i}=1-\beta_1^t. $$ Intuitively, the missing mass $\beta_1^t$ is the weight that would have sat on pre-history before step $1$, but because the moment state was initialized at zero, that missing history is replaced by an artificial zero contribution. If the gradients are drawn from a stationary distribution with mean $\mu$, then $$\mathbb E[m_t]=(1-\beta_1^t)\mu,$$ so dividing by $1-\beta_1^t$ gives the unbiased estimate $\hat m_t=m_t/(1-\beta_1^t)$. The same argument for the second moment gives $\hat v_t=v_t/(1-\beta_2^t)$.

So the thing being corrected is not some mysterious defect of exponential averaging itself; it is the startup bias introduced by initializing the moment states at zero. For example, if $m_0=v_0=0$ and the first scalar gradient is $g_1=2$ with $\beta_1=0.9$ and $\beta_2=0.999$, then $m_1=0.2$ and $v_1=0.004$ look artificially small. Bias correction gives $\hat m_1=2$ and $\hat v_1=4$, recovering the correct first-step scale.

The denominator $\sqrt{\hat v_t}+\varepsilon$ also has a clear intuition. The second-moment estimate $\hat v_t$ tracks typical squared gradient magnitude, so $\sqrt{\hat v_t}$ estimates a root-mean-square gradient scale for each coordinate. Coordinates that historically see large, noisy gradients receive smaller effective steps; quieter coordinates can move more. Again, $\varepsilon$ is there for numeric stability so very small denominators do not create undefined or explosive steps.

Adam can therefore be read as a uniform synthesis of earlier ideas: compared with classical momentum it keeps a first-moment average of gradients, and compared with RMSProp it keeps a second-moment denominator that rescales coordinates adaptively. But this same coupling creates a subtle regularization issue.

If one adds L2 regularization directly to the Adam objective, then one forms $g_t^{\text{L2}}=\nabla L(\theta_t)+\lambda\theta_t$ and feeds that combined gradient into both the first- and second-moment machinery. The penalty term $\lambda\theta_t$ is therefore divided by the same adaptive denominator as the data gradient. Coordinates with large historical gradients get large denominators and are regularized less strongly than coordinates with calmer histories. So Adam with L2 regularization does _not_ perform the same coordinatewise shrinkage as plain weight decay.

AdamW fixes this by decoupling the shrinkage from the adaptive gradient step. One keeps $g_t=\nabla L(\theta_t)$ inside the Adam moments, but updates parameters by $\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\,\hat m_t\oslash(\sqrt{\hat v_t}+\varepsilon)$. The multiplicative decay acts directly on the parameter, independent of the adaptive denominator. That is why AdamW is usually a better way to combine Adam with weight decay: the regularization strength stays interpretable and is not distorted by each coordinate's gradient history.

The non-equivalence is easiest to see coordinatewise. Suppose two coordinates currently both equal $1$, there is no data gradient, the learning rate is $\eta=0.1$, the regularization coefficient is $\lambda=0.2$, and Adam's adaptive denominators are $1$ and $100$. Under Adam with L2 regularization, the shrinkages are $0.1\cdot 0.2/1=0.02$ and $0.1\cdot 0.2/100=0.0002$, so the coordinates become $(0.98,0.9998)$. Under AdamW, both coordinates are multiplied by $1-0.1\cdot 0.2=0.98$, so both become $0.98$. AdamW is therefore better at implementing actual uniform relative decay across coordinates.

---

Flashcards for this section are as follows:

- Adam formulas ::@:: Adam uses $m_t=\beta_1 m_{t-1}+(1-\beta_1)g_t$, $v_t=\beta_2 v_{t-1}+(1-\beta_2)(g_t\odot g_t)$, $\hat m_t=m_t/(1-\beta_1^t)$, $\hat v_t=v_t/(1-\beta_2^t)$, and $\theta_{t+1}=\theta_t-\eta\,\hat m_t\oslash(\sqrt{\hat v_t}+\varepsilon)$.
- why Adam's equations feel uniform ::@:: Adam expresses momentum-like memory, adaptive scaling, bias correction, and the final step in one consistent elementwise tensor form, so the same update template applies coordinate by coordinate.
- why bias correction appears in Adam ::@:: Adam uses bias correction because the moment states start at zero, so after $t$ steps the observed-gradient weights sum only to $1-\beta^t$ and the missing weight $\beta^t$ is effectively assigned to the artificial zero initialization.
- bias-correction derivation for Adam first moment ::@:: Unrolling $m_t=\beta_1 m_{t-1}+(1-\beta_1)g_t$ with $m_0=0$ gives $m_t=(1-\beta_1)\sum_{i=1}^{t}\beta_1^{t-i}g_i$; if $\mathbb E[g_i]=\mu$, then $\mathbb E[m_t]=(1-\beta_1^t)\mu$, so dividing by $1-\beta_1^t$ yields the unbiased estimate $\hat m_t$.
- same bias-correction idea for Adam second moment ::@:: The same zero-initialization argument gives $\hat v_t=v_t/(1-\beta_2^t)$ because the second-moment weights also sum to only $1-\beta_2^t$ at step $t$.
- denominator intuition in Adam / $\sqrt{\hat v_t}+\varepsilon$ ::@:: The term $\sqrt{\hat v_t}$ estimates a root-mean-square gradient scale per coordinate, so historically noisy coordinates get smaller effective steps, and $\varepsilon$ supplies numeric stability.
- Adam versus classical momentum ::@:: Classical momentum stores a velocity-like step state, whereas Adam stores a first-moment average that is later bias-corrected and divided by an adaptive denominator.
- Adam versus RMSProp ::@:: RMSProp keeps only an adaptive second-moment denominator, whereas Adam adds a momentum-like first-moment average and bias correction on top of a similar denominator idea.
- Adam with L2 regularization ::@:: Adam with L2 regularization forms $g_t^{\text{L2}}=\nabla L(\theta_t)+\lambda\theta_t$ and feeds that combined gradient into the adaptive moments, so the penalty is scaled by the adaptive denominator.
- AdamW / decoupled update $\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\,\hat m_t\oslash(\sqrt{\hat v_t}+\varepsilon)$ ::@:: AdamW decouples weight decay from the adaptive gradient machinery by shrinking parameters directly with $(1-\eta\lambda)$ while leaving the Adam moments driven by the data gradient.
- why AdamW is better than Adam plus L2 for weight decay ::@:: AdamW is better because the decay strength is not weakened differently across coordinates by the adaptive denominator, so regularization remains a direct and interpretable parameter shrinkage.
- given $m_0=v_0=0$, scalar gradient $g_1=2$, $\beta_1=0.9$, and $\beta_2=0.999$, compute $m_1$, $v_1$, $\hat m_1$, and $\hat v_1$ in Adam ::@:: We get $m_1=0.2$, $v_1=0.004$, then $\hat m_1=0.2/(1-0.9)=2$ and $\hat v_1=0.004/(1-0.999)=4$.
- given two coordinates with current values $(1,1)$, learning rate $\eta=0.1$, regularization coefficient $\lambda=0.2$, no data gradient, and Adam-style adaptive denominators $(1,100)$, compare one update of Adam with L2 regularization versus AdamW ::@:: Adam with L2 shrinks the coordinates to $(1-0.1\cdot0.2/1,\,1-0.1\cdot0.2/100)=(0.98,0.9998)$, whereas AdamW multiplies both by $(1-0.1\cdot0.2)=0.98$, giving $(0.98,0.98)$.

## learning-rate schedules

Optimizers such as momentum, RMSProp, and Adam decide how to use the gradient _inside one step_. A learning-rate schedule decides how large those steps should be _across training time_. This matters because early training often benefits from larger exploratory moves, whereas later training usually benefits from smaller, more precise refinement steps.

So it is useful to separate two questions: _what direction should we move?_ and _how far should we move at this stage of training?_ Learning-rate schedules answer the second question.

---

Flashcards for this section are as follows:

- what a learning-rate schedule changes ::@:: A learning-rate schedule changes the global step size over training time, whereas the optimizer determines how the current gradient is transformed into a direction.
- why learning-rate schedules matter ::@:: Early training often benefits from larger exploratory steps, while late training usually benefits from smaller steps for fine-grained refinement.
- optimizer versus schedule ::@:: The optimizer answers how to use the gradient inside one step, and the schedule answers how large steps should be at different training stages.

### scheduled decay and exponential decay

The simplest schedules reduce the learning rate monotonically. In _scheduled_ or _step_ decay, one chooses milestones and drops the learning rate by a fixed factor when a milestone is reached. A convenient formula is $\eta_t=\eta_0\alpha^{m(t)}$, where $m(t)$ counts how many milestones have occurred and $\alpha\in(0,1)$ is the drop factor. The graph therefore looks like a staircase: flat plateaus followed by sudden downward jumps.

In _exponential decay_, one instead uses a smooth monotone formula such as $\eta_t=\eta_0\gamma^t$ with $\gamma\in(0,1)$, or equivalently $\eta_t=\eta_0 e^{-kt}$. The graph is no longer a staircase; it is a smooth downward curve that decays quickly at first and then gradually flattens.

These two schedules encode slightly different intuitions. Step decay says, "hold the current learning rate until progress suggests a discrete change of regime." Exponential decay says, "shrink continuously and smoothly throughout training." Neither is universally superior; the point is to recognize the graph shape and the training philosophy behind it.

For examples, if $\eta_0=0.1$, the milestone drop factor is $\alpha=0.1$, and milestones occur at epochs $10$ and $20$, then at epoch $17$ we have passed one milestone, so $\eta_{17}=0.1\cdot 0.1=0.01$. If instead exponential decay uses $\eta_t=0.1\cdot 0.9^t$, then $\eta_3=0.1\cdot 0.9^3=0.0729$.

---

Flashcards for this section are as follows:

- scheduled or step decay / $\eta_t=\eta_0\alpha^{m(t)}$ ::@:: In scheduled decay, the learning rate stays constant between milestones and drops by a fixed factor, for example $\eta_t=\eta_0\alpha^{m(t)}$.
- graph of scheduled decay ::@:: The graph of scheduled decay is a staircase: flat plateaus followed by sudden downward jumps at chosen milestones.
- exponential decay / $\eta_t=\eta_0\gamma^t$ or $\eta_t=\eta_0 e^{-kt}$ ::@:: Exponential decay shrinks the learning rate smoothly over time, for example as $\eta_t=\eta_0\gamma^t$ with $\gamma\in(0,1)$.
- graph of exponential decay ::@:: The graph of exponential decay is a smooth monotone downward curve that falls quickly at first and then gradually flattens.
- scheduled decay versus exponential decay ::@:: Scheduled decay uses discrete regime changes at chosen milestones, whereas exponential decay shrinks the learning rate continuously at every step.
- given initial learning rate $\eta_0=0.1$, step-decay factor $\alpha=0.1$, and milestones at epochs $10$ and $20$, what is $\eta_{17}$? ::@:: Because epoch $17$ is after one milestone but before the second, $\eta_{17}=0.1\cdot 0.1=0.01$.
- given exponential decay $\eta_t=0.1\cdot 0.9^t$, what is $\eta_3$? ::@:: We get $\eta_3=0.1\cdot 0.9^3=0.0729$.

### cosine annealing and warm restarts

Cosine annealing gives a smoother and more structured schedule. A standard form is $\eta_t=\eta_{\min}+\tfrac12(\eta_{\max}-\eta_{\min})(1+\cos(\pi t/T))$ for $0\le t\le T$. The learning rate starts at $\eta_{\max}$, decreases smoothly along a half-cosine curve, and reaches $\eta_{\min}$ at the end of the cycle. The graph therefore looks like a smooth arch descending from high to low rather than a staircase or simple exponential curve.

Warm restarts add periodic resets. Once a cosine cycle finishes, the learning rate is jumped back to a larger value and another cosine decay begins. The weights are _not_ reinitialized; only the learning rate schedule is restarted. Graphically, the schedule becomes a sequence of repeated cosine arches with sudden upward jumps between cycles.

The intuition is that a restart can help the optimizer leave a narrow local region while still reusing a good current solution. So warm restarts are not "start over from scratch"; they are "re-energize the step size while keeping the learned parameters."

For a small example, if $\eta_{\min}=0$, $\eta_{\max}=0.1$, and $T=10$, then at the midpoint $t=5$ we get $\eta_5=\tfrac12(0.1)(1+\cos(\pi/2))=0.05$.

---

Flashcards for this section are as follows:

- cosine annealing / $\eta_t=\eta_{\min}+\tfrac12(\eta_{\max}-\eta_{\min})(1+\cos(\pi t/T))$ ::@:: Cosine annealing decreases the learning rate smoothly along a half-cosine curve from $\eta_{\max}$ to $\eta_{\min}$ over one cycle.
- graph of cosine annealing ::@:: The graph of cosine annealing is a smooth descending half-cosine arch rather than a staircase or simple exponential curve.
- warm restart ::@:: In a warm restart, the learning rate is reset to a larger value while the learned weights are kept, so the optimizer gets a fresh large-step phase without restarting training from scratch.
- graph of cosine annealing with warm restarts ::@:: With warm restarts, the graph is a sequence of cosine arches separated by sudden upward jumps in the learning rate.
- why warm restarts can help ::@:: Warm restarts can help the optimizer escape a narrow local region by re-energizing the learning rate while keeping the current learned parameters.
- given cosine annealing with $\eta_{\min}=0$, $\eta_{\max}=0.1$, and $T=10$, what is the learning rate at the midpoint $t=5$? ::@:: We get $\eta_5=\tfrac12(0.1)(1+\cos(\pi/2))=0.05$.

## batch normalization

Batch normalization addresses another major deep-learning difficulty: the scale and distribution of activations can drift while training proceeds, and those scale changes make optimization harder. The lecture motivates normalization first at the data level, then generalizes it to hidden layers inside a network.

The practical recipe is simple: standardize activations using batch statistics, then restore flexibility with a learnable affine transformation. So batch normalization is not "force every hidden feature to stay permanently standardized." It is "standardize first so optimization is easier, then relearn the useful scale and offset." A good mnemonic is _center, scale, then relearn scale and shift_.

The lecture associates batch normalization with three practical benefits: faster training through better conditioning, less sensitivity to initialization because badly scaled activations are repeatedly renormalized, and a mild regularizing effect because minibatch statistics inject noise. Algebraically, the normalization step recenters activations toward mean $0$ and variance $1$ before the network relearns task-specific scale and shift.

---

Flashcards for this section are as follows:

- batch normalization purpose ::@:: Batch normalization stabilizes and accelerates training by controlling the scale and distribution of intermediate activations.
- how batch normalization works at a high level ::@:: It normalizes activations using minibatch statistics and then applies a learnable affine transformation so the network retains representational flexibility.
- why batch normalization is not just preprocessing ::@:: Unlike fixed input preprocessing, batch normalization acts inside the network during training and still leaves learnable scaling and shifting parameters.
- three practical benefits of batch normalization ::@:: Batch normalization can accelerate training, reduce initialization sensitivity, and add a regularizing effect because it improves conditioning while minibatch statistics inject mild noise.
- batch-normalization mnemonic ::@:: A useful batch-normalization mnemonic is _center, scale, then relearn scale and shift_.

### data normalization and scale mismatch

The lecture first revisits ordinary data normalization. If one input feature lies in $[0,1]$ while another lies in $[10,1000]$, then even a simple model has mismatched geometry. The loss contours become elongated, gradients become uneven, and one global learning rate is forced to respect the steepest direction.

This is not merely a cosmetic issue. A coefficient attached to a very large-scale feature can be numerically small while still creating a large predictive effect. So optimization and regularization both become harder to interpret. This is the raw-input version of the same feature-scale geometry issue discussed earlier in the regularization section. Standardizing each feature by its empirical mean and standard deviation makes the coordinates more comparable and reduces this avoidable anisotropy before the data even enters a deep model.

Batch normalization is the deep-learning analogue of extending that idea inward. If raw input normalization helps because later computations see better-scaled data, then hidden layers may benefit for the same reason.

---

Flashcards for this section are as follows:

- why feature-scale mismatch hurts training ::@:: Features on very different numeric scales create elongated loss contours and poorly balanced gradients, which slows optimization.
- why normalization helps before deep modeling ::@:: Standardizing raw features makes the optimization geometry more balanced before the data enters the network, reducing avoidable anisotropy.
- raw-input version of the feature-scale problem ::@:: Data normalization addresses at the input layer the same basic geometry problem that uneven feature scales cause for optimization and regularization more generally.
- valley-geometry intuition for scale mismatch ::@:: Feature-scale mismatch stretches the loss into a long narrow valley, so one global learning rate must be small enough for the steep direction and therefore becomes slow in the shallow direction.

### normalization inside deep models

The lecture then generalizes the normalization idea from raw inputs to hidden representations. A deep network is a stack of layers, and the output of one layer becomes the input to the next. So if normalization helps ordinary models by improving the scale of their inputs, one should also ask whether the same idea helps inside the model itself.

This motivation is often phrased using _internal covariate shift_: as earlier layers update, the distribution of inputs seen by later layers changes. In that language, each layer is trying to learn while the coordinate system of its own inputs keeps drifting. Batch normalization was introduced as a way to reduce that drift by normalizing layer inputs or pre-activations using minibatch statistics.

Even if one does not take the phrase "internal covariate shift" too literally, the practical lesson is the same: when hidden activations vary wildly in scale from layer to layer or from step to step, optimization becomes harder. Batch normalization keeps signals numerically better behaved, which can speed training, reduce initialization sensitivity, and help gradient flow.

Batch normalization is also a _layerwise_ choice. It can be applied separately to different layers, and one does not need to normalize every layer identically. Some layers may use batch normalization, others may not, depending on architecture and training design.

---

Flashcards for this section are as follows:

- why normalization should also happen inside deep networks ::@:: Since each layer acts as the input to later layers, hidden activations can benefit from normalization just as raw input features do.
- internal covariate shift ::@:: Internal covariate shift is the idea that as earlier layers update, the distribution of inputs seen by later layers drifts during training.
- modern practical motivation for batch normalization ::@:: Even beyond the internal-covariate-shift slogan, batch normalization helps because it keeps hidden activations numerically better behaved from layer to layer and step to step.
- why batch normalization helps optimization after the slogan ::@:: Whether or not one emphasizes internal covariate shift, batch normalization helps because controlling hidden-layer scale makes optimization and gradient flow more stable.
- batch normalization can be applied per layer ::@:: Batch normalization is a layerwise design choice: it can be added separately to some layers while other layers are left unchanged.

### standardization, learnable affine correction, and inference mode

The normalization step is performed separately for each normalized unit or channel inside a layer. If the minibatch values for one normalized scalar feature are $x_1,\ldots,x_B$, then batch normalization computes $\mu_{\mathcal B}=\frac{1}{B}\sum_{i=1}^{B}x_i$ and $\sigma_{\mathcal B}^2=\frac{1}{B}\sum_{i=1}^{B}(x_i-\mu_{\mathcal B})^2$. The course material teaches the most basic standardization rule, $\hat x_i^{\text{basic}}=\frac{x_i-\mu_{\mathcal B}}{\sqrt{\sigma_{\mathcal B}^2}}$, which has exact mean $0$ and variance $1$ on the minibatch when $\sigma_{\mathcal B}^2>0$. In practical implementations one usually adds a numeric-stability constant and writes $\hat x_i=\frac{x_i-\mu_{\mathcal B}}{\sqrt{\sigma_{\mathcal B}^2+\varepsilon}}$, then outputs $y_i=\gamma \hat x_i+\beta$. The $\varepsilon$ term is therefore a practical implementation refinement rather than the most basic classroom formula.

Using the course's basic formula, one can derive the standardized batch mean directly: $$\frac{1}{B}\sum_{i=1}^{B}\hat x_i^{\text{basic}} = \frac{1}{\sqrt{\sigma_{\mathcal B}^2}}\cdot \frac{1}{B}\sum_{i=1}^{B}(x_i-\mu_{\mathcal B})=0.$$ Likewise, the batch second moment is $$\frac{1}{B}\sum_{i=1}^{B}(\hat x_i^{\text{basic}})^2 = \frac{1}{\sigma_{\mathcal B}^2}\cdot \frac{1}{B}\sum_{i=1}^{B}(x_i-\mu_{\mathcal B})^2 = 1.$$ With the practical $\varepsilon$-adjusted formula, the mean is still $0$ but the variance becomes $$\frac{1}{B}\sum_{i=1}^{B}\hat x_i^2 = \frac{\sigma_{\mathcal B}^2}{\sigma_{\mathcal B}^2+\varepsilon}\approx 1,$$ so the implementation remains near-standardized while avoiding division-by-zero problems.

The learnable parameters $\gamma$ and $\beta$ are important. Pure standardization would force each normalized feature to have mean $0$ and variance $1$ at that point in the network. Batch normalization instead says: _first standardize for optimization, then relearn whatever scale and shift are useful for the task_. That is why batch normalization helps optimization without permanently removing representational freedom.

Their effect can also be derived cleanly. Since $y_i=\gamma \hat x_i+\beta$, $$\frac{1}{B}\sum_{i=1}^{B} y_i = \gamma\left(\frac{1}{B}\sum_{i=1}^{B}\hat x_i\right)+\beta = \beta,$$ and, ignoring the tiny $\varepsilon$ distortion, $$\operatorname{Var}_{\mathcal B}(y) \approx \gamma^2 \operatorname{Var}_{\mathcal B}(\hat x) \approx \gamma^2.$$ So $\beta$ restores a learned mean shift and $\gamma$ restores a learned scale. In particular, batch normalization can even represent identity-type behavior if training finds that no additional reshaping is desirable beyond stabilization.

The statistics used during training and after training must be distinguished carefully. During _training_, batch normalization uses the current minibatch statistics $\mu_{\mathcal B}$ and $\sigma_{\mathcal B}^2$, and it also updates running estimates such as $\mu_{\text{run}}$ and $\sigma^2_{\text{run}}$. During _inference_, it does _not_ recompute normalization from the current test example or test minibatch. Instead, it uses the running or dataset-level statistics accumulated from training. This is the operational meaning of switching batch normalization from training mode to inference mode.

One common running-stat update rule is $$\mu_{\text{run}} \leftarrow \rho\,\mu_{\text{run}} + (1-\rho)\mu_{\mathcal B}, \qquad \sigma^2_{\text{run}} \leftarrow \rho\,\sigma^2_{\text{run}} + (1-\rho)\sigma^2_{\mathcal B},$$ with momentum parameter $\rho\in(0,1)$. In inference mode, the layer then uses $$\hat x = \frac{x-\mu_{\text{run}}}{\sqrt{\sigma^2_{\text{run}}+\varepsilon}}$$ instead of the current minibatch statistics.

That distinction matters because the same network can behave numerically differently depending on mode. A batch-normalized model in training mode and the same model in inference mode are not identical computations with only a cosmetic flag change; they genuinely use different statistics.

For a tiny numeric example, suppose one normalized unit takes minibatch values $(2,4)$. Then $\mu_{\mathcal B}=3$ and $\sigma_{\mathcal B}^2=1$, so the standardized values are $(-1,1)$. If $\gamma=2$ and $\beta=0.5$, the outputs become $(-1.5,2.5)$. This shows the full pipeline: compute batch statistics, standardize, then apply the learnable affine correction.

---

Flashcards for this section are as follows:

- per-unit or per-channel normalization in batch normalization ::@:: Batch normalization standardizes each normalized unit or channel separately using minibatch mean and variance.
- basic course standardization formula in batch normalization ::@:: The most basic course formula is $\hat x_i^{\text{basic}}=(x_i-\mu_{\mathcal B})/\sqrt{\sigma_{\mathcal B}^2}$, i.e. no numeric-stability constant is included.
- practical implementation formula in batch normalization ::@:: Practical implementations usually use $\hat x_i=(x_i-\mu_{\mathcal B})/\sqrt{\sigma_{\mathcal B}^2+\varepsilon}$ so division by zero or tiny variance does not cause instability.
- why the normalized minibatch mean is zero / $\frac{1}{B}\sum_i \hat x_i^{\text{basic}}=0$ ::@:: Because $\hat x_i^{\text{basic}}=(x_i-\mu_{\mathcal B})/\sqrt{\sigma_{\mathcal B}^2}$, one has $\frac{1}{B}\sum_i \hat x_i^{\text{basic}}=\frac{1}{\sqrt{\sigma_{\mathcal B}^2}}\frac{1}{B}\sum_i(x_i-\mu_{\mathcal B})=0$.
- why the basic standardized minibatch variance is exactly one ::@:: With the basic course formula, $\frac{1}{B}\sum_i (\hat x_i^{\text{basic}})^2=\frac{1}{\sigma_{\mathcal B}^2}\frac{1}{B}\sum_i(x_i-\mu_{\mathcal B})^2=1$.
- why the practical standardized minibatch variance is only approximately one / $\frac{1}{B}\sum_i \hat x_i^2=\frac{\sigma_{\mathcal B}^2}{\sigma_{\mathcal B}^2+\varepsilon}$ ::@:: With the practical $\varepsilon$-adjusted formula, the second moment becomes $\frac{\sigma_{\mathcal B}^2}{\sigma_{\mathcal B}^2+\varepsilon}\approx 1$, so standardization stays near-unit while gaining numeric stability.
- role of $\gamma$ and $\beta$ ::@:: The learnable affine parameters $\gamma$ and $\beta$ restore flexibility after standardization by allowing the network to relearn an appropriate scale and shift.
- effect of affine correction on batch mean and scale ::@:: Since $y_i=\gamma\hat x_i+\beta$, the batch mean becomes $\beta$ and the batch variance becomes approximately $\gamma^2$, so the network can relearn useful offset and scale after normalization.
- which statistics are used during training ::@:: During training, batch normalization uses the current minibatch statistics $\mu_{\mathcal B}$ and $\sigma_{\mathcal B}^2$ and also updates running estimates for later inference.
- which statistics are used during inference ::@:: During inference, batch normalization uses running or dataset-level statistics accumulated from training rather than statistics from the current test example or test minibatch.
- running-statistics update in batch normalization ::@:: A common running update is $\mu_{\text{run}}\leftarrow \rho\mu_{\text{run}}+(1-\rho)\mu_{\mathcal B}$ and $\sigma^2_{\text{run}}\leftarrow \rho\sigma^2_{\text{run}}+(1-\rho)\sigma^2_{\mathcal B}$, after which inference normalizes with those running statistics.
- why inference should not use fresh minibatch statistics ::@:: Test-time normalization should use training-distribution statistics so predictions remain stable and do not depend on the accidental composition of a test minibatch.
- given minibatch values $(2,4)$ for one normalized unit, with $\gamma=2$ and $\beta=0.5$, compute the standardized values and the final batch-normalized outputs ::@:: The minibatch mean is $3$ and variance is $1$, so the standardized values are $(-1,1)$, and the final outputs are $(2\cdot(-1)+0.5,\,2\cdot1+0.5)=(-1.5,2.5)$.

### adaptive batch normalization under covariate shift

Batch normalization also has a useful domain-adaptation variant. Under _covariate shift_, the input distribution changes between source and target domains while the conditional task relationship is still similar enough that the learned features remain relevant. In such cases, one may want to keep most of the trained network but adapt the normalization statistics to the new domain.

_Adaptive batch normalization_ (often abbreviated AdaBN) follows this idea. Instead of retraining the whole model from scratch, one re-estimates batch-normalization statistics such as running means and variances on target-domain data while keeping the main learned weights fixed, or nearly fixed. The hope is that the model already knows useful representations, but the target domain has shifted the feature statistics enough that the old source-domain normalization is no longer ideal.

So adaptive batch normalization is one more reminder that batch-normalization statistics are part of the model's effective behavior. They are not just incidental bookkeeping values; changing them can change how the network interprets activations under a new domain.

---

Flashcards for this section are as follows:

- covariate shift ::@:: Covariate shift means the input distribution changes across domains while the task relationship remains similar enough that a source-trained model may still be useful after adaptation.
- adaptive batch normalization ::@:: Adaptive batch normalization re-estimates batch-normalization statistics on target-domain data while keeping most of the learned network parameters fixed.
- why adaptive batch normalization can help under covariate shift ::@:: If the main representations remain useful but the feature statistics have shifted, updating batch-normalization means and variances can align the model better with the target domain without full retraining.
- why batch-normalization statistics matter for domain adaptation ::@:: Batch-normalization statistics are part of the model's effective behavior, so changing them can change how the network interprets activations in a new domain.
