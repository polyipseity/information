---
aliases:
  - feedforward neural network
  - feedforward neural networks
  - multilayer perceptron
  - multilayer perceptrons
tags:
  - flashcard/active/special/academia/HKUST/COMP_4211/feedforward_neural_network
  - language/in/English
---

<!-- check: ignore-file[two_sided_calc_warning]: concept note uses symbolic answers on QA cards -->

# feedforward neural network

A feedforward neural network (FNN), also called a multilayer perceptron (MLP), is the course's first genuinely deep model. It takes the basic pattern from earlier supervised learning — transform the input, then make a probabilistic prediction — and implements the transformation stage with many layers of simple computational units. If $a^{(0)}=x$ and each layer computes $z^{(\ell)}=(W^{(\ell)})^\top a^{(\ell-1)}+b^{(\ell)}$ followed by $a^{(\ell)}=g^{(\ell)}(z^{(\ell)})$, then the full network output is the repeated composition $a^{(L)}$. Information flows from the input layer, through hidden layers, to the output layer without cyclic dependence inside one forward pass.

This model is useful to read from two complementary viewpoints. As a function approximator, an FNN composes affine maps and nonlinear activation functions to represent complicated input-output relations that would be hard to engineer manually. As a probabilistic model, it serves as a learned feature extractor whose final layer defines a distribution over targets, just as logistic regression used a sigmoid or softmax output. In that sense, deep learning does not discard simpler models; it wraps them inside a learned representation map.

This shift is one of the main conceptual transitions from classical machine learning to deep learning in COMP 4211. Earlier models took the input features largely as given and focused on learning $P(y\mid x)$ directly. A deep feedforward network instead learns an intermediate representation $h=f(x)$ and then defines $P(y\mid h)$. Equivalently, the network learns both a feature map and a predictor on top of that feature map. The network therefore learns not only how to predict, but also how to construct the representation on which prediction should be based.

---

Flashcards for this section are as follows:

- overview ::@:: A feedforward neural network is a layered model that maps inputs to outputs by repeated affine-transform-plus-activation steps, such as $z^{(\ell)}=(W^{(\ell)})^\top a^{(\ell-1)}+b^{(\ell)}$ and $a^{(\ell)}=g^{(\ell)}(z^{(\ell)})$, without recurrent loops in one forward pass.
- feedforward neural network versus earlier models ::@:: Earlier models often used hand-crafted features, whereas an FNN learns the feature transformation jointly with the prediction rule.
- alternative name for feedforward neural networks ::@:: Feedforward neural networks are also commonly called multilayer perceptrons (MLPs). The name "multilayer" refers to having at least one hidden layer between input and output, and "perceptron" echoes the historical single-unit predecessor; despite the name, modern MLPs use smooth differentiable activations rather than the original threshold step function.
- deep-learning transition ::@:: In the deep-learning viewpoint, one first learns a representation $h=f(x)$ and then models the output distribution conditioned on that learned representation.
- simpler-model special case ::@:: If the learned representation is just the raw input or if there is no hidden layer, an FNN reduces to a familiar shallow model such as linear regression, logistic regression, or softmax regression.

## multilayer perceptron as function approximator

An FNN is best viewed as a parameterized composition of layer maps. If $\theta=\{W^{(\ell)},b^{(\ell)}\}_{\ell=1}^{L}$ and $\Psi_{\ell}(u)=g^{(\ell)}((W^{(\ell)})^\top u+b^{(\ell)})$, then the network computes $f_{\theta}(x)=\Psi_{L}\circ \Psi_{L-1}\circ \cdots \circ \Psi_{1}(x)$. During learning, the parameters are optimized so that $f_{\theta}(x)$ approximates some target function $f^{\ast}(x)$ or supports a final probabilistic head that predicts the desired label or response.

This function view clarifies how an FNN relates to simpler models. A linear model uses a fixed representation and a single affine map, such as $x\mapsto w^\top x+b$. Logistic and softmax regression still use one affine score map, but place a probabilistic output distribution on top of it. A feedforward network keeps the same final-head idea while replacing the fixed representation by a learned composition $x\mapsto a^{(L-1)}(x)$. Thus an FNN is often a _learned feature map plus a simple output model_.

This also hints at the relation to reproducing-kernel Hilbert space (RKHS) methods. A reproducing-kernel Hilbert space is a Hilbert space of functions where point evaluation is continuous and represented by inner products with kernel sections, so predictors can be written as $f(x)=\langle w,\phi(x)\rangle_{\mathcal H}$ or equivalently through kernel evaluations $k(x,x')$. In that setting, the feature map or kernel is fixed before fitting. An FNN plays a related role but with a crucial difference: the feature map itself, say $\phi_{\theta}(x)=a^{(L-1)}(x)$, is learned from data rather than fixed in advance. So the network is not merely fitting a linear predictor in a chosen feature space; it is also learning which feature space should be used.

The remaining subsections unpack the same model at three different resolutions: the local unit computation, the compact layerwise notation for forward propagation, and the expressivity story behind universal approximation and depth efficiency. In other words, this parent section sets the _function-approximation viewpoint_, and the subsections below handle the mechanics and consequences in more detail.

---

Flashcards for this section are as follows:

- function view of an FNN ::@:: An FNN defines a parameterized composition $f_{\theta}(x)=\Psi_{L}\circ \cdots \circ \Psi_{1}(x)$, where each layer map has the form $\Psi_{\ell}(u)=g^{(\ell)}((W^{(\ell)})^\top u+b^{(\ell)})$.
- learned feature map plus simple head ::@:: A feedforward neural network can be viewed as a learned feature map $x\mapsto a^{(L-1)}(x)$ followed by a comparatively simple output model on top of that learned representation.
- target function $f^{\ast}(x)$ ::@:: In the function-approximation viewpoint, the network parameters are learned so that $f_{\theta}(x)$ approximates a target function $f^{\ast}(x)$.
- shallow-model relation ::@:: Linear regression, logistic regression, and softmax regression are shallow special cases of the same general pattern: simple output heads on top of either the raw input or a fixed representation.
- reproducing-kernel Hilbert space (RKHS) contrast ::@:: In a reproducing-kernel Hilbert space (RKHS), predictors are linear in a fixed feature map or kernel representation, such as $f(x)=\langle w,\phi(x)\rangle_{\mathcal H}$; an FNN differs by learning the feature map $\phi_{\theta}(x)$ itself from data.

### units, layers, and nonlinear composition

A single unit accepts an input vector $x$, computes the affine transformation $z=W^\top x+b$, and then outputs $g(z)$ for some activation function $g$. The scalar or vector $z$ is often called the _net input_ or _pre-activation_. The learnable parameters are the incoming link weights and the bias.

This local computation is repeated layer after layer. The outputs of one layer become the inputs of the next layer, so the network composes many simple functions. From this perspective, a multilayer perceptron is not mysterious: it is a chain of affine maps interleaved with nonlinearities.

The role of the nonlinearity is decisive. If one removed $g$ and kept only affine maps, the composition of all layers would still be affine, no matter how deep the network was. For example, if $f_{1}(x)=A_{1}x+c_{1}$ and $f_{2}(u)=A_{2}u+c_{2}$, then $f_{2}(f_{1}(x))=A_{2}A_{1}x+(A_{2}c_{1}+c_{2})$, which is still affine. By induction, any finite composition of affine maps has the form $Ax+c$. So purely linear depth only refactorizes one affine map into many pieces; it does not create genuinely new nonlinear decision boundaries or nonlinear feature maps.

Nonlinear activations break that collapse. Once $g$ is nonlinear, the layer map $u\mapsto g(W^\top u+b)$ can bend, threshold, gate, or saturate different regions of the input space differently. That is what lets deep networks construct hierarchical representations instead of merely re-expressing one linear transformation in a more complicated notation.

---

Flashcards for this section are as follows:

- unit computation $z=W^\top x+b$ and $g(z)$ ::@:: A standard neural-network unit computes the pre-activation $z=W^\top x+b$ and then outputs $g(z)$.
- pre-activation or net input ::@:: The quantity $z=W^\top x+b$ is often called the pre-activation or net input of the unit.
- parameters of a standard neural-network unit: A unit computes $z=W^\top x+b$ and outputs $g(z)$. What are the learnable parameters and how many are there for a unit in a layer with $d$ inputs? ::@:: The learnable parameters are the incoming weight vector $W\in\mathbb{R}^d$ (one weight per input) and the scalar bias $b\in\mathbb{R}$, giving $d+1$ parameters in total. During training, gradient descent adjusts these parameters to minimize the overall network loss.
- why repeated local computation creates depth ::@:: Depth arises because each layer takes the previous layer's outputs as its inputs, producing a repeated composition of simple computations.
- affine-collapse proof ::@:: If $f_{1}(x)=A_{1}x+c_{1}$ and $f_{2}(u)=A_{2}u+c_{2}$, then $f_{2}(f_{1}(x))=A_{2}A_{1}x+(A_{2}c_{1}+c_{2})$, so composing affine maps still gives an affine map; induction extends this to any depth.
- why affine maps alone are insufficient ::@:: Without nonlinear activations, a multilayer stack of affine maps would still be just one affine map, so depth would be only a reparameterization rather than a source of new expressive power.
- what nonlinearity adds ::@:: A nonlinear activation lets different input regions be transformed differently, so the network can create curved decision boundaries and hierarchical feature maps.

### layerwise notation and forward propagation

Layerwise notation makes forward propagation compact and systematic. If $a^{(0)}=x$, $z^{(\ell)}=(W^{(\ell)})^\top a^{(\ell-1)}+b^{(\ell)}$, and $a^{(\ell)}=g^{(\ell)}(z^{(\ell)})$ for $\ell=1,\ldots,L$, then the network output is $f_{\theta}(x)=a^{(L)}$. This is the same idea as writing hidden vectors as $h^{(\ell)}$; here the notation $a^{(\ell)}$ emphasizes that these are the layer activations, while $z^{(\ell)}$ records the pre-activations before the nonlinearity.

This notation makes two ideas explicit. First, each layer transforms the representation from the previous layer. Second, the weights for the units in one layer are naturally grouped into one matrix, so forward propagation is not many unrelated scalar computations but one repeated matrix-plus-nonlinearity template. The same template appears in every layer, only with different dimensions and activation choices.

The worked forward-propagation examples are therefore less about memorizing one numeric network than about learning the computational rhythm: compute pre-activations, apply nonlinearities, pass the resulting activations to the next layer, and continue until the output layer is reached. The next subsection compresses that same rhythm into a short structural mnemonic.

---

Flashcards for this section are as follows:

- layerwise notation $a^{(0)}, z^{(\ell)}, a^{(\ell)}$ ::@:: In layerwise notation, $a^{(0)}=x$, each pre-activation is $z^{(\ell)}=(W^{(\ell)})^\top a^{(\ell-1)}+b^{(\ell)}$, and each activation is $a^{(\ell)}=g^{(\ell)}(z^{(\ell)})$.
- first hidden layer formula ::@:: A first hidden layer can be written as $z^{(1)}=(W^{(1)})^\top x+b^{(1)}$ and $a^{(1)}=g^{(1)}(z^{(1)})$.
- recursive forward propagation ::@:: Forward propagation applies the same pattern repeatedly: matrix mixing plus bias shift to get $z^{(\ell)}$, then activation to get $a^{(\ell)}$, then pass $a^{(\ell)}$ forward.
- why weight matrices are convenient ::@:: Matrix notation collects the weights of many units in one object, making forward propagation compact and efficient.
- computational rhythm of forward propagation ::@:: Forward propagation proceeds as pre-activation $\to$ activation $\to$ next layer, repeated until the final output is produced.

### repeated matrix-nonlinearity viewpoint

The whole network can be summarized as repeated application of one structural motif: _mix coordinates with a matrix, shift by a bias, bend coordinatewise with a nonlinearity, then repeat_. Writing $\Psi_{\ell}(u)=g^{(\ell)}((W^{(\ell)})^\top u+b^{(\ell)})$, the full forward pass is $f_{\theta}(x)=\Psi_{L}\circ\cdots\circ\Psi_{1}(x)$. This is the same forward-propagation view as above, but compressed into a structural mnemonic rather than unpacked layer by layer.

This viewpoint is useful for interpretation. The matrix $W^{(\ell)}$ mixes or recombines coordinates from the previous layer; the bias $b^{(\ell)}$ shifts thresholds or offsets; and the activation $g^{(\ell)}$ bends the geometry coordinatewise. A good memory cue is _mix, shift, bend, repeat_. The network becomes deep because it applies that same motif several times, so later layers operate not on raw coordinates but on already-transformed representations.

It also gives an intuition for hierarchy. The first layers often detect relatively simple directions or patterns, later layers recombine those patterns, and the last layers convert the final representation into task-specific scores. In symbols, $x \mapsto a^{(1)} \mapsto a^{(2)} \mapsto \cdots \mapsto a^{(L)}$ is a ladder of representations, not just a long algebraic expression.

---

Flashcards for this section are as follows:

- forward-pass mnemonic ::@:: A useful forward-pass mnemonic is _mix, shift, bend, repeat_: $W^{(\ell)}$ mixes coordinates, $b^{(\ell)}$ shifts thresholds, $g^{(\ell)}$ bends the representation, and the result is passed to the next layer.
- matrix interpretation in an FNN ::@:: The weight matrix recombines coordinates from the previous layer, so each new unit can detect a learned direction or pattern rather than copying a single old coordinate.
- hierarchy of representations ::@:: The repeated-map view makes it clear that depth means applying the same affine-plus-nonlinearity template to increasingly abstract intermediate representations.

### two-layer forward pass computed step by step

Consider a two-layer network with $x=\begin{bmatrix}1\\0\end{bmatrix}$, $W^{(1)}=\begin{bmatrix}2&-1\\1&3\end{bmatrix}$, $b^{(1)}=\begin{bmatrix}0.5\\0.5\end{bmatrix}$, activation $g^{(1)}=\operatorname{ReLU}$, $W^{(2)}=\begin{bmatrix}1\\-1\end{bmatrix}$, $b^{(2)}=0$, and identity output.

Layer 1 pre-activation: $(W^{(1)})^\top x+b^{(1)}=\begin{bmatrix}2\cdot 1+1\cdot 0\\-1\cdot 1+3\cdot 0\end{bmatrix}+\begin{bmatrix}0.5\\0.5\end{bmatrix}=\begin{bmatrix}2+0.5\\-1+0.5\end{bmatrix}=\begin{bmatrix}2.5\\-0.5\end{bmatrix}$. Layer 1 activation: $a^{(1)}=\operatorname{ReLU}\bigl(\begin{bmatrix}2.5\\-0.5\end{bmatrix}\bigr)=\begin{bmatrix}2.5\\0\end{bmatrix}$. The second unit receives a negative pre-activation and is switched off by ReLU — an explicit instance of a dead unit on this input.

Layer 2 pre-activation: $(W^{(2)})^\top a^{(1)}+b^{(2)}=\begin{bmatrix}1&-1\end{bmatrix}\begin{bmatrix}2.5\\0\end{bmatrix}+0=2.5$. Identity output gives $f_\theta(x)=2.5$.

---

Flashcards for this section are as follows:

- given $x=\begin{bmatrix}1\\0\end{bmatrix}$, $W^{(1)}=\begin{bmatrix}2&-1\\1&3\end{bmatrix}$, $b^{(1)}=\begin{bmatrix}0.5\\0.5\end{bmatrix}$, $g^{(1)}=\operatorname{ReLU}$, compute $z^{(1)}$ and $a^{(1)}$ ::@:: $z^{(1)}=(W^{(1)})^\top x+b^{(1)}=\begin{bmatrix}2\\-1\end{bmatrix}+\begin{bmatrix}0.5\\0.5\end{bmatrix}=\begin{bmatrix}2.5\\-0.5\end{bmatrix}$; $a^{(1)}=\operatorname{ReLU}(z^{(1)})=\begin{bmatrix}2.5\\0\end{bmatrix}$, so the second unit is switched off.
- continuing from $a^{(1)}=\begin{bmatrix}2.5\\0\end{bmatrix}$, $W^{(2)}=\begin{bmatrix}1\\-1\end{bmatrix}$, $b^{(2)}=0$, identity output, compute $z^{(2)}$ and the network output $f_\theta(x)$ ::@:: $z^{(2)}=(W^{(2)})^\top a^{(1)}+b^{(2)}=\begin{bmatrix}1&-1\end{bmatrix}\begin{bmatrix}2.5\\0\end{bmatrix}=2.5$; identity output gives $f_\theta(x)=2.5$.

### universal approximation and why depth still helps

The lecture states the universal-approximation idea in a specific classical form: with enough hidden units, a one-hidden-layer network with sigmoid-type nonlinearities can approximate any continuous target on a compact domain to arbitrary accuracy. In symbols, for continuous $f^{\ast}$ on compact $K$ and any $\varepsilon>0$, there exists a sufficiently wide shallow network $f_{\theta}$ such that $\sup_{x\in K}|f_{\theta}(x)-f^{\ast}(x)|<\varepsilon$. This is an existence statement about expressive power.

However, existence is not the same as efficiency. The theorem does not say the required shallow width is small, nor that the resulting model is easy to optimize from finite data. The slides emphasize that deeper networks may approximate some structured functions with exponentially fewer parameters because repeated nonlinear composition can reuse intermediate features.

This resolves a common confusion. Universal approximation does _not_ imply that shallow networks are always preferable. It says broad approximation is possible in principle, but says nothing about compactness, optimization ease, sample efficiency, or representational hierarchy. Depth helps especially when the target itself is compositionally structured.

---

Flashcards for this section are as follows:

- universal approximation statement ::@:: A one-hidden-layer sigmoid network is a universal approximator in the existence sense: for continuous $f^{\ast}$ on compact $K$ and any $\varepsilon>0$, some sufficiently wide shallow network can achieve $\sup_{x\in K}|f_{\theta}(x)-f^{\ast}(x)|<\varepsilon$.
- why universal approximation is not the end of the story ::@:: Universal approximation is only an existence statement and does not imply that shallow networks are the most efficient or easiest to train.
- why depth can reduce parameter count ::@:: Depth can exploit compositional structure by reusing intermediate features, so some targets that are representable by shallow networks may require far fewer parameters when represented deeply.
- shallow-versus-deep lesson ::@:: The practical value of depth is not just representability, but also parameter efficiency and more structured representation learning.

## initialization and activation functions

Weight initialization and activation choice determine whether forward activations and backward gradients remain numerically healthy as they move through many layers. Here _signal_ should be read rigorously as the scale of quantities such as the pre-activations $z_j^{(\ell)}$, activations $a_j^{(\ell)}$, and backpropagated error terms $\delta_j^{(\ell)}=\partial L/\partial z_j^{(\ell)}$. In practice one often summarizes this scale through statistics such as their mean, variance, or typical magnitude over random initialization and over a batch of inputs.

Even a well-designed objective can be hard to optimize if those forward quantities collapse toward zero, explode to huge magnitudes, or enter activation regions where the derivative is effectively unusable. That is why this topic treats initialization and activation functions as a linked design problem rather than as isolated implementation details. Initialization sets the typical scale of $z^{(\ell)}$ and $a^{(\ell)}$ at the start of training, while activation functions determine how those quantities are transformed and what gradient information survives backward propagation.

The architectural side of that story is the focus here. The training-side follow-through — dropout, Adam and AdamW, learning-rate schedules, and batch normalization — is developed in [deep learning training](deep%20learning%20training.md), which explains how these initialization and activation choices interact with optimization after the network structure has been fixed.

---

Flashcards for this section are as follows:

- rigorous meaning of signal ::@:: In deep-learning initialization discussions, _signal_ means the scale of forward pre-activations/activations and backward gradients, often summarized by statistics such as mean, variance, or typical magnitude across layers.
- why initialization matters ::@:: Initialization matters because forward activations and backward gradients can vanish if weights are too small and explode if weights are too large.
- activation-initialization linkage ::@:: Initialization and activation choice must work together so that activations and gradients remain numerically useful across depth.

### why initialization matters

Let $n_{\mathrm{in}}$ denote fan-in (the number of inputs feeding one unit in the current layer) and $n_{\mathrm{out}}$ denote fan-out (the number of outputs this layer sends to the next layer). Starting from $z_j^{(\ell)}=\sum_{i=1}^{n_{\mathrm{in}}} W_{ij}^{(\ell)} a_i^{(\ell-1)}+b_j^{(\ell)}$, assume for a heuristic derivation that $W_{ij}^{(\ell)}$ and $a_i^{(\ell-1)}$ are independent, centered, and identically distributed across $i$. Then $\mathbb{E}[z_j^{(\ell)}]\approx 0$ and $\operatorname{Var}(z_j^{(\ell)})=\operatorname{Var}\!\left(\sum_i W_{ij}^{(\ell)}a_i^{(\ell-1)}\right)+\operatorname{Var}(b_j^{(\ell)})\approx\sum_i\operatorname{Var}(W_{ij}^{(\ell)}a_i^{(\ell-1)})+\operatorname{Var}(b_j^{(\ell)})\approx n_{\mathrm{in}}\operatorname{Var}(W_{ij}^{(\ell)})\operatorname{Var}(a_i^{(\ell-1)})+\operatorname{Var}(b_j^{(\ell)})$. Ignoring small-bias variance at initialization gives the standard rule of thumb $\operatorname{Var}(z_j^{(\ell)})\approx n_{\mathrm{in}}\operatorname{Var}(W_{ij}^{(\ell)})\operatorname{Var}(a_i^{(\ell-1)})$.

So if $\operatorname{Var}(W_{ij}^{(\ell)})$ is too small, activation scale shrinks layer by layer; if it is too large, scale grows layer by layer. In both cases, deep optimization becomes difficult before training has meaningfully begun.

The lecture highlights two practical initialization schemes. Xavier initialization is designed for roughly symmetric activations such as sigmoid and tanh and uses variance of order $\frac{2}{n_{\mathrm{in}}+n_{\mathrm{out}}}$, for example $W_{ij}\sim \mathcal N\bigl(0,\frac{2}{n_{\mathrm{in}}+n_{\mathrm{out}}}\bigr)$ or $W_{ij}\sim \operatorname{Unif}\bigl[-\sqrt{\frac{6}{n_{\mathrm{in}}+n_{\mathrm{out}}}},\sqrt{\frac{6}{n_{\mathrm{in}}+n_{\mathrm{out}}}}\bigr]$. The normal form directly sets the target variance; the uniform form is chosen so $\operatorname{Var}(\operatorname{Unif}[-r,r])=r^2/3$ matches the same target variance, while also bounding draws so extremely large outliers are impossible. A useful mnemonic is that Xavier _balances both sides_ of the layer by averaging fan-in and fan-out.

The course slides also present a Xavier-style uniform rule $W_{ij}\sim\operatorname{Unif}\bigl[-\sqrt{1/n_{\mathrm{in}}},\sqrt{1/n_{\mathrm{in}}}\bigr]$. Relative to the standard Xavier formulas, this is likely a simplified or inconsistent convention; however, for assignments and examinations one should follow the course-stated convention when explicitly asked.

He (Kaiming) initialization is adapted to rectifier-style activations such as ReLU and uses a larger variance, typically $\operatorname{Var}(W_{ij})\approx \frac{2}{n_{\mathrm{in}}}$, for example $W_{ij}\sim \mathcal N\bigl(0,\frac{2}{n_{\mathrm{in}}}\bigr)$ or $W_{ij}\sim \operatorname{Unif}\bigl[-\sqrt{\frac{6}{n_{\mathrm{in}}}},\sqrt{\frac{6}{n_{\mathrm{in}}}}\bigr]$. The mnemonic here is _He for half-alive ReLUs_: because a ReLU often zeros out about half of its inputs, one compensates with a larger variance so surviving activations do not become too small. In the course material, He initialization is presented in its normal-variance form, which is the version to use by default in course calculations.

For both Xavier and He, the normal-distribution formulas are the direct variance-target statements. The uniform alternatives are variance-matched bounded surrogates. A common intuition is that in a normal distribution, values beyond roughly $3\sigma$ are rare, so a bounded initializer can be viewed as clipping unlikely tails while keeping a controlled spread; the exact interval is then chosen to match the target variance.

These schemes are best understood as attempts to keep the flow of information numerically balanced across layers rather than as arbitrary recipes to memorize. Xavier tries to preserve scale through a symmetric bottleneck, while He explicitly compensates for the one-sided gating effect of rectifiers.

---

Flashcards for this section are as follows:

- fan-in and fan-out ::@:: Fan-in $n_{\mathrm{in}}$ is the number of inputs feeding one unit in a layer, and fan-out $n_{\mathrm{out}}$ is the number of outputs that layer sends forward to the next layer.
- variance heuristic derivation ::@:: With $z_j^{(\ell)}=\sum_{i=1}^{n_{\mathrm{in}}}W_{ij}^{(\ell)}a_i^{(\ell-1)}+b_j^{(\ell)}$ and rough independence/zero-mean assumptions, $\operatorname{Var}(z_j^{(\ell)})\approx\sum_i\operatorname{Var}(W_{ij}^{(\ell)}a_i^{(\ell-1)})\approx n_{\mathrm{in}}\operatorname{Var}(W_{ij}^{(\ell)})\operatorname{Var}(a_i^{(\ell-1)})$ (plus a usually small bias-variance term).
- too-small initial weights ::@:: If initial weights are too small, the activation and gradient scales shrink from layer to layer until they become too weak to support useful learning.
- too-large initial weights ::@:: If initial weights are too large, the activation and gradient scales grow from layer to layer until they become too large for stable learning.
- Xavier initialization ::@:: Xavier initialization balances fan-in and fan-out with variance of order $\frac{2}{n_{\mathrm{in}}+n_{\mathrm{out}}}$, using either a normal form $\mathcal N\bigl(0,\frac{2}{n_{\mathrm{in}}+n_{\mathrm{out}}}\bigr)$ or a variance-matched uniform form with bounds $\pm\sqrt{\frac{6}{n_{\mathrm{in}}+n_{\mathrm{out}}}}$.
- Xavier mnemonic ::@:: A mnemonic for Xavier initialization is _balance both sides_: average fan-in and fan-out to keep scale stable across the layer.
- normal versus uniform initialization intuition ::@:: The normal variant directly sets a target variance, while the uniform variant chooses bounds so the variance matches that target and very large draws, typically more than three standard deviations away, are excluded by bounded support.
- normal-form versus bounded-uniform intuition for Xavier and He ::@:: For both Xavier and He, the normal form states the target variance directly; the uniform form is a variance-matched bounded surrogate often interpreted as clipping unlikely normal tails (roughly beyond the three-standard-deviation region) while keeping controlled spread.
- course-slide Xavier convention ::@:: The course slides list a Xavier-style uniform rule $\operatorname{Unif}\bigl[-\sqrt{1/n_{\mathrm{in}}},\sqrt{1/n_{\mathrm{in}}}\bigr]$; although this is likely a simplified or inconsistent variant, use the course-stated form in assignments or exams when explicitly requested.
- He initialization ::@:: He initialization for ReLU-like activations uses variance of order $\frac{2}{n_{\mathrm{in}}}$, commonly in normal form $\mathcal N\bigl(0,\frac{2}{n_{\mathrm{in}}}\bigr)$ (the form emphasized in this course), with a variance-matched uniform alternative also possible.
- He mnemonic ::@:: A mnemonic for He initialization is _half-alive ReLUs_: because rectifiers often keep only about half the inputs active, the variance is doubled relative to the naive $1/n_{\mathrm{in}}$ scaling.
- why initialization schemes exist ::@:: Initialization schemes are designed to preserve reasonable activation and gradient scale across layers rather than to provide arbitrary starting values.

### classical activations: sigmoid and tanh

The classical activation family in this topic refers to smooth, bounded, saturating functions that were dominant before rectifier-era defaults, especially sigmoid and tanh. The sigmoid activation has several equivalent forms: $\sigma(z)=\frac{1}{1+e^{-z}}=\frac{e^z}{1+e^z}=\frac{1+\tanh(z/2)}{2}$. It maps every real number to the interval $(0,1)$, so it is bounded, monotone increasing, and smooth. Its derivative is $\sigma'(z)=\sigma(z)(1-\sigma(z))$, which is at most $1/4$ and becomes very small when $z\gg 0$ or $z\ll 0$. A useful mnemonic is _sigmoid squashes to a probability_: it turns an unbounded score into a number between $0$ and $1$.

The hyperbolic tangent activation is the hyperbolic-trigonometric analogue of ordinary tangent, defined by $\tanh(z)=\frac{\sinh(z)}{\cosh(z)}$. It also has the useful exponential forms $\tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}=\frac{e^{2z}-1}{e^{2z}+1}=2\sigma(2z)-1$, so tanh is essentially a rescaled and recentered sigmoid. Its derivative is $\tanh'(z)=1-\tanh^2(z)=4\sigma(2z)(1-\sigma(2z))$. A mnemonic is _tanh is the zero-centered sigmoid_: it keeps the same saturation idea but shifts the range to $(-1,1)$ and makes the output sign-symmetric.

These formulas immediately show their main theoretical characteristics. Both sigmoid and tanh are bounded, monotone, smooth, and saturating. Sigmoid is not zero-centered, whereas tanh is odd and zero-centered. Empirically, tanh usually trains a bit better than sigmoid in hidden layers because its outputs are centered around $0$, but both suffer from saturation: once $|z|$ is large, their derivatives are tiny, so gradient signals decay rapidly through depth.

The lecture's message is therefore nuanced: sigmoid and tanh are mathematically elegant and historically important, and sigmoid remains the standard output nonlinearity for Bernoulli models, but they are not the default hidden-layer choices for modern deep feedforward networks. A subtle but important point is that output-layer saturation is less problematic than hidden-layer saturation: at the output, vanishing derivative happens only once and often corresponds to small prediction error, so it can be a sign that the model is already close to the target rather than a deep-training bottleneck.

---

Flashcards for this section are as follows:

- sigmoid formula ::@:: The sigmoid activation can be written as $\sigma(z)=\frac{1}{1+e^{-z}}=\frac{e^z}{1+e^z}=\frac{1+\tanh(z/2)}{2}$, so it is a probability-squashing nonlinearity closely related to tanh.
- classical activation overview ::@:: Sigmoid and tanh are classical smooth bounded saturating activations: mathematically clean and still useful at output heads, but often harder to optimize in deep hidden stacks than rectifier-style alternatives.
- sigmoid derivative ::@:: The sigmoid derivative is $\sigma'(z)=\sigma(z)(1-\sigma(z))$, with maximum $1/4$, so gradients shrink strongly when $z$ is in saturation regions.
- sigmoid characteristics ::@:: Sigmoid is bounded, monotone, and smooth, but it is not zero-centered and it saturates strongly in the tails, which is why hidden-layer training can be slow.
- tanh formula and hyperbolic-trigonometric meaning ::@:: The hyperbolic tangent is defined as $\tanh(z)=\sinh(z)/\cosh(z)$ and can be written as $\frac{e^z-e^{-z}}{e^z+e^{-z}}=2\sigma(2z)-1$, so it is a recentered sigmoid-like activation.
- tanh derivative ::@:: The tanh derivative is $\tanh'(z)=1-\tanh^2(z)=4\sigma(2z)(1-\sigma(2z))$, so tanh also suffers saturation for large $|z|$.
- why tanh is often preferable to sigmoid ::@:: Tanh is zero-centered and odd, so hidden activations are often easier to optimize than with sigmoid, although tanh still saturates for large $|z|$.
- output-layer saturation nuance ::@:: Vanishing gradient at a sigmoid or tanh output unit is usually less concerning than in hidden layers, because it occurs only once and often means prediction error is already small.
- given $z=1$, compute and compare $\sigma(z)$, $\sigma'(z)$, $\tanh(z)$, and $\tanh'(z)$ ::@:: $\sigma(1)=\frac{1}{1+e^{-1}}\approx 0.731$, $\sigma'(1)=0.731(1-0.731)\approx 0.197$; $\tanh(1)\approx 0.762$, $\tanh'(1)=1-0.762^2\approx 0.419$; tanh has roughly twice the derivative at $z=1$, confirming it flows gradient better in the linear range than sigmoid.

### rectifier family: ReLU, leaky ReLU, parametric ReLU, ELU, and softplus

The rectifier family consists of activations that keep positive-side behavior close to identity while clipping or attenuating negative inputs. The word _rectifier_ comes from signal/electronics language: a rectifier turns signed inputs into mostly nonnegative outputs by suppressing negative parts. ReLU has several common equivalent forms: $\operatorname{ReLU}(z)=\max\{0,z\}=\frac{z+|z|}{2}=z\mathbf{1}[z>0]$ up to the value at $z=0$. It is piecewise linear, unbounded above, sparse on the negative side, and computationally simple. Its derivative is $1$ for $z>0$ and $0$ for $z<0$, while at $z=0$ it is not classically differentiable and implementations use a subgradient convention.

Its most important empirical advantage is that the derivative is constant on the positive side, which often leads to faster learning than with saturating activations. Its main weakness is the dead-neuron problem. When a unit remains in the negative half-space for all training examples, its output is always zero and its derivative is also zero, so it can stop learning entirely. A practical mitigation is to initialize biases to a small positive value so units start slightly on the active side instead of immediately falling into always-off behavior.

Leaky ReLU and parametric ReLU address this by keeping a small nonzero slope on the negative side. The common general form is $g(z,\alpha)=\max\{0,z\}+\alpha\min\{0,z\}=\begin{cases}z,&z\ge 0,\\ \alpha z,&z<0,\end{cases}$ which can also be written as $\frac{1+\alpha}{2}z+\frac{1-\alpha}{2}|z|$. A small fixed $\alpha$ gives leaky ReLU and a learned $\alpha$ gives parametric ReLU. Their derivative is $1$ for $z>0$ and $\alpha$ for $z<0$; at $z=0$ they are not classically differentiable unless $\alpha=1$, so implementations again use a subgradient convention. A mnemonic is _leak a little gradient on the left_.

The slides also mention smooth rectifier variants. Softplus is $\zeta(z)=\log(1+e^z)=\log(1+e^{-z})+z$, so it is a smooth approximation to ReLU and an antiderivative of sigmoid because $\zeta'(z)=\sigma(z)$. ELU uses $\operatorname{ELU}_{\alpha}(z)=\begin{cases}z,&z>0,\\ \alpha(e^z-1),&z\le 0,\end{cases}$ so its derivative is $1$ on the positive side and $\alpha e^z$ on the negative side. Here $\alpha$ sets both the negative saturation floor ($\lim_{z\to-\infty}\operatorname{ELU}_{\alpha}(z)=-\alpha$) and the left-side slope near $0$ (approximately $\alpha$). A mnemonic is _ELU bends below zero toward a floor_: larger $\alpha$ means a deeper negative floor and steeper negative branch. ReLU, leaky ReLU, ELU, and softplus are all related by the same design goal: keep positive-side behavior close to identity while changing the negative side to trade off sparsity, smoothness, and gradient flow.

---

Flashcards for this section are as follows:

- rectifier family overview ::@:: The rectifier family keeps positive-side behavior close to identity while suppressing negative inputs; the term _rectifier_ means turning signed inputs into mostly nonnegative outputs by clipping or attenuating negatives.
- ReLU formula ::@:: ReLU can be written as $\operatorname{ReLU}(z)=\max\{0,z\}=\frac{z+|z|}{2}=z\mathbf{1}[z>0]$, so it is the canonical hard rectifier and the non-smooth relative of softplus.
- ReLU derivative and corner behavior ::@:: ReLU has derivative $1$ for $z>0$ and $0$ for $z<0$; at $z=0$ it is not classically differentiable, so implementations adopt a subgradient convention.
- why ReLU often learns faster ::@:: ReLU has constant positive-side slope and no positive-side saturation, which usually makes hidden-layer optimization easier than with sigmoid-like activations.
- dead-neuron problem ::@:: A ReLU neuron is dead when it stays in the zero-output region for all training examples and therefore receives no useful gradient updates.
- dead-neuron mitigation by bias initialization ::@:: A common mitigation for dead ReLUs is to initialize biases to small positive values so units start slightly active instead of immediately stuck on the zero side.
- general leaky-ReLU form ::@:: The rectifier family $g(z,\alpha)=\max\{0,z\}+\alpha\min\{0,z\}=\begin{cases}z,&z\ge 0,\\ \alpha z,&z<0,\end{cases}$ becomes leaky ReLU for fixed small $\alpha$ and parametric ReLU when $\alpha$ is learned.
- leaky or parametric ReLU derivative ::@:: Leaky and parametric ReLU have derivative $1$ for $z>0$ and $\alpha$ for $z<0$; at $z=0$ they are generally non-differentiable unless $\alpha=1$, so software uses a subgradient choice.
- softplus formula ::@:: Softplus can be written as $\zeta(z)=\log(1+e^z)=\log(1+e^{-z})+z$, so it is a smooth approximation to ReLU and an antiderivative of sigmoid.
- softplus derivative and sigmoid relation ::@:: Softplus is smooth with derivative $\zeta'(z)=\sigma(z)$, so it is directly linked to sigmoid while approximating ReLU.
- ELU formula, mnemonic, and $\alpha$ intuition ::@:: $\operatorname{ELU}_{\alpha}(z)=\begin{cases}z,&z>0,\\ \alpha(e^z-1),&z\le 0,\end{cases}$ with derivative $1$ for $z>0$ and $\alpha e^z$ for $z<0$; mnemonic: _bend below zero toward a floor_; $\alpha$ controls both the negative saturation level $-\alpha$ and the negative-side slope near zero.
- rectifier-family recall ::@:: ReLU, leaky ReLU, ELU, and softplus all keep an approximately identity positive side; they differ mainly in how they treat the negative side to balance sparsity, smoothness, and gradient flow.

### smooth and gated modern activations

The lecture briefly surveys modern smooth and gated activations. _Smooth_ here means continuously differentiable nonlinearities that avoid hard corners. _Gated_ means one branch multiplicatively modulates another branch, so the network can conditionally pass, attenuate, or amplify information instead of applying only one fixed pointwise transform.

SiLU, also called the sigmoid linear unit, takes the form $\operatorname{SiLU}(z)=z\sigma(z)=z\,\operatorname{softplus}'(z)$. So it multiplies a linear factor by a sigmoid gate. Its derivative is $\operatorname{SiLU}'(z)=\sigma(z)+z\sigma(z)(1-\sigma(z))$. A mnemonic is _self-gated linear unit_: the input gates itself.

Swish generalizes this to $\operatorname{Swish}_{\beta}(z)=z\sigma(\beta z)$ with fixed or learned $\beta$. Its derivative is $\sigma(\beta z)+\beta z\sigma(\beta z)(1-\sigma(\beta z))$. The special case $\beta=1$ is SiLU, so SiLU is one point in the Swish family.

Mish combines a linear factor with a tanh-transformed softplus term: $\operatorname{Mish}(z)=z\tanh(\operatorname{softplus}(z))$. Differentiating by product and chain rules gives $\operatorname{Mish}'(z)=\tanh(\operatorname{softplus}(z))+z\,\operatorname{sech}^2(\operatorname{softplus}(z))\sigma(z)$. A mnemonic is: softplus inside tanh, then multiplied by $z$.

GELU uses $\operatorname{GELU}(z)=z\Phi(z)$ where $\Phi$ is the Gaussian cumulative distribution function, so it can be read as a Gaussian-smoothed gate. Its derivative is $\Phi(z)+z\phi(z)$, where $\phi$ is the Gaussian density, and in practice one often remembers the approximation $\operatorname{GELU}(z)\approx \frac{z}{2}\bigl(1+\tanh(\sqrt{2/\pi}(z+0.044715z^3))\bigr)$. A useful logistic approximation for the Gaussian CDF is $\Phi(z)\approx\sigma(1.7z)$.

The most structurally interesting example in the slides is SwiGLU. In scalar notation one can write $\operatorname{SwiGLU}(z)=\operatorname{Swish}_{\beta}(w_1z+b_1)\cdot(w_2z+b_2)$, so there are five learnable scalar parameters in this form: $w_1,b_1,\beta,w_2,b_2$. By the product rule, $\frac{d}{dz}\operatorname{SwiGLU}(z)=w_1\operatorname{Swish}_{\beta}'(w_1z+b_1)(w_2z+b_2)+w_2\operatorname{Swish}_{\beta}(w_1z+b_1)$. A useful special case is $w_1=1$, $b_1=0$, $\beta=1$, $w_2=1$, $b_2=0$, where SwiGLU collapses to $\operatorname{Swish}(z)\cdot z=z^2\sigma(z)$.

Why can gating help? Multiplication lets one branch control the gain of another branch in an input-dependent way. This can support conditional computation, richer feature interactions, and easier routing of useful signal while suppressing nuisance components. That is one reason gated feedforward blocks (such as SwiGLU variants) are popular in strong transformer architectures.

The key lesson is not that one should memorize an ever-growing zoo of names. Rather, the lecture wants the student to notice the design pattern: modern activations often preserve gradient flow better, introduce smoothness, allow mild non-monotonicity, or add explicit multiplicative gating so the network can modulate information more flexibly.

---

Flashcards for this section are as follows:

- smooth and gated activation overview ::@:: Smooth activations are differentiable and avoid hard corners, while gated activations multiply branches so one branch can modulate the information flow of another.
- SiLU formula ::@:: SiLU can be written as $\operatorname{SiLU}(z)=z\sigma(z)=z\,\operatorname{softplus}'(z)$, so it is a self-gated linear activation closely related to Swish and softplus.
- SiLU derivative: SiLU is defined as $\operatorname{SiLU}(z)=z\sigma(z)$ where $\sigma(z)=\frac{1}{1+e^{-z}}$. Compute $\operatorname{SiLU}'(z)$ using the product rule. ::@:: By the product rule on $z\cdot\sigma(z)$: $\operatorname{SiLU}'(z)=1\cdot\sigma(z)+z\cdot\sigma'(z)=\sigma(z)+z\sigma(z)(1-\sigma(z))$, using $\sigma'(z)=\sigma(z)(1-\sigma(z))$. This can be factored as $\sigma(z)(1+z(1-\sigma(z)))=\sigma(z)(1+z-z\sigma(z))$.
- swish activation ::@:: Swish generalizes SiLU as $\operatorname{Swish}_{\beta}(z)=z\sigma(\beta z)$ with fixed or learned $\beta$; the case $\beta=1$ is exactly SiLU.
- Swish derivative: Swish is $\operatorname{Swish}_\beta(z)=z\sigma(\beta z)$ where $\sigma(t)=\frac{1}{1+e^{-t}}$. Compute $\operatorname{Swish}_\beta'(z)$ using the product rule. ::@:: By the product rule on $z\cdot\sigma(\beta z)$: $\operatorname{Swish}_\beta'(z)=\sigma(\beta z)+z\cdot\frac{d}{dz}\sigma(\beta z)=\sigma(\beta z)+z\cdot\beta\sigma(\beta z)(1-\sigma(\beta z))$. At $\beta=1$ this reduces to the SiLU derivative $\sigma(z)+z\sigma(z)(1-\sigma(z))$.
- Mish formula and derivative ::@:: Mish uses $\operatorname{Mish}(z)=z\tanh(\operatorname{softplus}(z))$ with derivative $\tanh(\operatorname{softplus}(z))+z\,\operatorname{sech}^2(\operatorname{softplus}(z))\sigma(z)$.
- GELU formula ::@:: GELU uses $\operatorname{GELU}(z)=z\Phi(z)$ and is often approximated by $\frac{z}{2}\bigl(1+\tanh(\sqrt{2/\pi}(z+0.044715z^3))\bigr)$, so it behaves like a Gaussian-smoothed gate.
- GELU derivative ::@:: The GELU derivative is $\operatorname{GELU}'(z)=\Phi(z)+z\phi(z)$, where $\phi$ is the Gaussian density.
- Gaussian-CDF logistic approximation ::@:: A useful approximation in deep-learning practice is $\Phi(z)\approx\sigma(1.7z)$.
- why gated activations are interesting ::@:: Gated activations are interesting because multiplicative control allows input-dependent gain modulation, which can improve conditional routing of information and represent richer feature interactions than a single fixed pointwise nonlinearity.
- SwiGLU with five learnable scalars ::@:: In scalar form, $\operatorname{SwiGLU}(z)=\operatorname{Swish}_{\beta}(w_1z+b_1)(w_2z+b_2)$ has five learnable parameters $(w_1,b_1,\beta,w_2,b_2)$.
- SwiGLU special-case collapse ::@:: If $w_1=1$, $b_1=0$, $\beta=1$, $w_2=1$, and $b_2=0$, then $\operatorname{SwiGLU}(z)=\operatorname{Swish}(z)z=z^2\sigma(z)$.
- SwiGLU derivative ::@:: For $\operatorname{SwiGLU}(z)=\operatorname{Swish}_{\beta}(w_1z+b_1)(w_2z+b_2)$, the derivative is $w_1\operatorname{Swish}_{\beta}'(w_1z+b_1)(w_2z+b_2)+w_2\operatorname{Swish}_{\beta}(w_1z+b_1)$.
- modern-activation design lesson ::@:: Many modern activations are designed to improve gradient flow, smoothness, mild non-monotonicity, or explicit information gating rather than merely to replace one formula with another.

### activation comparison: theoretical and empirical characteristics

The activation families above can be compared along a few common axes. Theoretically, one can ask whether the function is bounded or unbounded, monotone or mildly non-monotone, smooth or piecewise smooth, zero-centered or strictly positive on most of its range, and whether its derivative saturates toward $0$. Empirically, one asks whether it trains easily, whether it suffers from dead units, whether it is computationally cheap, and whether it tends to perform well in modern architectures.

Sigmoid and tanh are smooth and bounded, but both saturate strongly. Tanh is usually easier to optimize than sigmoid because it is zero-centered, but both are vulnerable to vanishing gradients in deep hidden stacks. ReLU is computationally cheap and empirically robust, with excellent positive-side gradient flow, but it is non-smooth and can create dead units. Leaky ReLU and parametric ReLU trade a tiny amount of sparsity for more reliable negative-side gradient flow. ELU and softplus provide smoother behavior, but the empirical gain over ReLU is often modest relative to the extra cost; in many practical hidden-layer settings, softplus is still not as strong as ReLU-family defaults in speed/accuracy trade-offs.

SiLU, Swish, Mish, and GELU are smooth and often mildly non-monotone. Theoretically, that means they can preserve gradient flow while still suppressing some negative inputs more gently than a hard rectifier. Empirically, SiLU and GELU are especially popular in modern deep architectures because they often outperform plain ReLU when optimization budgets and hardware permit. SwiGLU goes further by using explicit multiplicative gating, which is one reason it appears in strong transformer feedforward blocks.

So there is no universally best activation. A compact memory rule is: _sigmoid and tanh are classical smooth saturators; ReLU and its relatives are hard rectifiers; SiLU, GELU, and SwiGLU are modern smooth or gated defaults_.

---

Flashcards for this section are as follows:

- activation-comparison axes ::@:: Common activation-comparison axes are bounded versus unbounded, monotone versus mildly non-monotone, smooth versus piecewise smooth, zero-centered versus not, saturation behavior, computational cost, and empirical training behavior.
- classical smooth saturators versus rectifiers ::@:: Sigmoid and tanh are bounded smooth saturating activations, whereas ReLU-family activations are mostly unbounded hard rectifiers with better positive-side gradient flow.
- ReLU-family tradeoff ::@:: ReLU is cheap and empirically strong but can create dead units; leaky ReLU and parametric ReLU trade a small negative slope for more reliable gradient flow.
- softplus empirical caveat ::@:: Although softplus is a smooth ReLU approximation, many practical hidden-layer setups still find ReLU-family activations stronger in training speed or final performance.
- modern smooth-or-gated tradeoff ::@:: SiLU, Swish, Mish, GELU, and SwiGLU are smoother or more strongly gated than ReLU and often perform better in modern deep models, though usually with more computation.

### vanishing-gradient problem

The vanishing-gradient problem is a chain-rule effect. Let $L$ denote the scalar loss, let $a^{(\ell)}$ be the activation vector at layer $\ell$, let $W^{(\ell)}$ be the weight matrix mapping layer $\ell-1$ to $\ell$, and let $D^{(\ell)}=\operatorname{diag}(g'^{(\ell)}(z^{(\ell)}))$. For one layer, the chain rule gives $\nabla_{a^{(\ell-1)}}L = W^{(\ell)}D^{(\ell)}\nabla_{a^{(\ell)}}L$. Recursing from $\ell=L$ down to $1$ yields $\nabla_{a^{(0)}}L = \bigl(\prod_{\ell=1}^{L}(W^{(\ell)}D^{(\ell)})\bigr)\nabla_{a^{(L)}}L$, where the product is the ordered composition of layerwise Jacobian factors.

Now apply any submultiplicative norm (for example spectral norm): $\|AB\|\le\|A\|\|B\|$. Starting from $\|\nabla_{a^{(0)}}L\|=\|W^{(1)}D^{(1)}\cdots W^{(L)}D^{(L)}\nabla_{a^{(L)}}L\|$ and repeatedly applying submultiplicativity gives $\|\nabla_{a^{(0)}}L\|\le\bigl(\prod_{\ell=1}^{L}\|W^{(\ell)}\|\,\|D^{(\ell)}\|\bigr)\|\nabla_{a^{(L)}}L\|$. If typical factors are below $1$, this product can shrink roughly exponentially with depth.

This is especially severe for saturating activations. For sigmoid, $0<\sigma'(z)=\sigma(z)(1-\sigma(z))\le 1/4$, and in the tails the derivative is much smaller than $1/4$. So a deep product of sigmoid derivatives can become tiny very quickly. Tanh is less severe near $0$ because $\tanh'(0)=1$, but once $|z|$ is large, $\tanh'(z)=1-\tanh^2(z)$ also becomes tiny. In contrast, ReLU has derivative $1$ on the positive side, so it avoids this particular source of shrinkage there; its problem is different, namely zero derivative on the negative side.

For output units, the same saturation is usually less problematic: there is typically only one output nonlinearity factor rather than a long product across many hidden layers. In addition, near-correct predictions should contribute less gradient anyway. For example, with sigmoid cross entropy, $\partial \ell/\partial z=\sigma(z)-y$, so when the prediction already matches the label well, the gradient is intentionally small.

The practical interpretation is that optimization becomes front-heavy: later layers near the loss still move, but earlier layers change extremely slowly, so representation learning stalls. This can appear as long plateaus, sensitivity to learning-rate schedules, or a model that behaves like a shallow classifier on weak features. Better initialization, normalization, residual connections, and activations with healthier derivatives are all partly responses to this multiplicative-gradient bottleneck.

---

Flashcards for this section are as follows:

- vanishing-gradient chain-rule form with notation ::@:: Let $L$ be scalar loss, $a^{(\ell)}$ layer activations, $W^{(\ell)}$ layer weights, and $D^{(\ell)}=\operatorname{diag}(g'^{(\ell)}(z^{(\ell)}))$; then recursion of $\nabla_{a^{(\ell-1)}}L=W^{(\ell)}D^{(\ell)}\nabla_{a^{(\ell)}}L$ gives $\nabla_{a^{(0)}}L=\bigl(\prod_{\ell=1}^{L}(W^{(\ell)}D^{(\ell)})\bigr)\nabla_{a^{(L)}}L$.
- vanishing-gradient norm bound derivation ::@:: Using submultiplicativity $\|AB\|\le\|A\|\|B\|$ on $\|W^{(1)}D^{(1)}\cdots W^{(L)}D^{(L)}\nabla_{a^{(L)}}L\|$ repeatedly yields $\|\nabla_{a^{(0)}}L\|\le\bigl(\prod_{\ell=1}^{L}\|W^{(\ell)}\|\,\|D^{(\ell)}\|\bigr)\|\nabla_{a^{(L)}}L\|$.
- why sigmoid causes vanishing gradients ::@:: Sigmoid satisfies $0<\sigma'(z)=\sigma(z)(1-\sigma(z))\le 1/4$, and in saturation regions the derivative is much smaller, so repeated chain-rule multiplication can shrink gradients very quickly.
- tanh versus ReLU for vanishing gradients ::@:: Tanh can still vanish in saturation even though $\tanh'(0)=1$, whereas ReLU avoids positive-side shrinkage because its derivative is $1$ for $z>0$ but can die completely on the negative side.
- why output-layer vanishing is usually less problematic ::@:: Output-layer saturation is usually less severe than hidden-layer vanishing because there is typically only one output derivative factor, and small output gradients often mean prediction error is already small.
- practical meaning of vanishing gradients ::@:: Vanishing gradients make optimization front-heavy: late layers update while early representation layers barely move, causing slow learning, plateaus, and weak deep-feature formation.

## probabilistic outputs and loss functions

The hidden layers of an FNN produce a learned representation $h$, but prediction still happens through a probabilistic output layer (output head). In this sense an FNN generalizes earlier models rather than replacing them with something conceptually unrelated: the hidden network learns the representation, and the final head defines a probability model on top of that representation.

The lecture phrases this as follows: the first through second-last layers define the feature transformation $h=f(x)$, while the last layer defines $P(y\mid h)$. This decomposition is extremely useful because it separates _representation learning_ from _output modeling_. Different tasks can therefore share similar backbones while using different output units and losses: identity/linear output for Gaussian regression, sigmoid output for Bernoulli (logistic-regression-style) binary classification, and a layer of softmax output units for categorical (softmax-regression-style) multiclass classification.

The common training principle is negative log-likelihood. If the output head defines a model $p_{\theta}(y\mid h)$, then a single-example loss is $\ell(\theta;x,y)=-\log p_{\theta}(y\mid h(x))$. So regression, binary classification, and multiclass classification differ mainly in the chosen conditional distribution at the output layer. The hidden network learns the representation; the probabilistic head and its negative log-likelihood specify the loss, exactly extending the logistic-regression and softmax-regression losses studied earlier. For the shallow-model derivations behind the Bernoulli and softmax heads, see [logistic regression](logistic%20regression.md#softmax-regression).

---

Flashcards for this section are as follows:

- hidden representation ::@:: In an FNN, the hidden layers produce a learned representation $h$ that is then passed to a probabilistic output layer.
- representation-learning split ::@:: In the lecture's probabilistic view, the earlier layers learn $h=f(x)$ and the final layer defines the output distribution $P(y\mid h)$.
- same backbone, different heads ::@:: The same learned representation $h$ can be paired with different output distributions, such as Gaussian regression heads, Bernoulli sigmoid heads, or categorical softmax heads.
- FNN versus shallow probabilistic models ::@:: An FNN can be viewed as linear regression, logistic regression, or softmax regression applied after a learned feature transformation rather than directly on the raw input.
- probabilistic-head training principle ::@:: If the output head defines $p_{\theta}(y\mid h)$, then the standard single-example training loss is negative log-likelihood, $\ell(\theta;x,y)=-\log p_{\theta}(y\mid h(x))$.

### feature extractor and logits

To define a probabilistic model on the learned features, the network first computes logits $z=W^\top h+b$ at the last layer. Here $W$ and $b$ are the parameters of the prediction head rather than of the feature extractor. The logits are then interpreted by an appropriate output unit, depending on the type of target variable.

At this stage, the important structural idea is _where logits live_: they sit exactly at the interface between the learned representation and the probabilistic head. The same hidden representation $h$ can therefore feed a linear-Gaussian head for regression, a sigmoid head for binary classification, or a softmax head for multiclass classification. The next subsection then explains the two standard meanings of the word _logit_ in more detail.

---

Flashcards for this section are as follows:

- final affine head over learned representation ::@:: In an FNN, the logits are the last-layer affine outputs $z=W^\top h+b$, where the affine head acts on the learned representation $h$ rather than directly on the raw input.
- backbone versus head ::@:: The hidden network acts as a feature extractor or backbone, while the final affine map and output unit form the prediction head.
- logits as the bridge to prediction ::@:: Logits sit at the interface between representation learning and probabilistic prediction: they are the scores that the output unit converts into a conditional distribution.
- why the same representation can support different tasks ::@:: A learned representation $h$ can be paired with different output heads, so the same feature extractor can support regression or different kinds of classification.

### what a logit means

The simplest way to understand a logit is as a score before probability normalization. In binary logistic models, the score $z$ is literally the log-odds because $p=\sigma(z)$ implies $\log\frac{p}{1-p}=z$. This gives a direct odds interpretation: increasing $z$ by $1$ multiplies the odds by $e$. In multiclass softmax models, each $z_k$ is not itself a log-probability, but it differs from the log-probability by the same shared normalizing constant $\log\sum_c e^{z_c}$.

This is why logits are so reusable across models. Linear regression uses a raw affine score as the predicted mean. Logistic regression uses a raw affine score as a log-odds. Softmax regression uses raw affine scores as unnormalized log-probabilities, with class probabilities from normalization across classes. Also, softmax depends only on relative logits: adding the same constant to all class logits leaves probabilities unchanged. A feedforward neural network keeps the same head-level interpretation, but the raw score is now computed from learned features instead of directly from $x$.

---

Flashcards for this section are as follows:

- what a logit means ::@:: A logit is a pre-normalization score on the log-probability scale: in binary models it is the exact log-odds, and in softmax models it is an unnormalized log-probability score.
- binary logit identity ::@:: If $p=\sigma(z)$, then $\log\frac{p}{1-p}=z$, so the sigmoid-output score is literally the binary logit.
- binary logit odds-interpretation ::@:: In binary logistic models, increasing logit $z$ by $1$ multiplies odds $p/(1-p)$ by $e$, so logits measure additive changes on the log-odds scale.
- softmax-logit identity ::@:: In softmax, $\log p_k = z_k-\log\sum_c e^{z_c}$, so each class logit is an unnormalized log-probability differing from the true log-probability by a shared normalization term.
- softmax relative-score interpretation ::@:: Softmax probabilities depend on relative logits: adding the same constant to all $z_k$ does not change $p_k$, so only score differences matter.
- logits across simple and deep models ::@:: Linear regression, logistic regression, softmax regression, and feedforward neural networks all use raw affine scores; the deep model differs mainly because the features fed into the score are learned.

### linear-Gaussian output for regression

If the target $y$ is real-valued, the lecture uses a linear-Gaussian output unit. _Linear_ means the output activation is identity, $g_{\text{out}}(z)=z$, so the final score is passed through unchanged; _Gaussian_ means the conditional distribution is $y\mid x\sim\mathcal N(z,\sigma^2)$ with mean $z$ and variance $\sigma^2$.

Using $p(y\mid z)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\bigl(-\frac{(y-z)^2}{2\sigma^2}\bigr)$, one sample gives $-\log p(y\mid z)=\frac{(y-z)^2}{2\sigma^2}+\frac{1}{2}\log(2\pi\sigma^2)$. For a dataset, summing over $i$ gives $\mathcal L(\theta)=\sum_i\frac{(y_i-z_i)^2}{2\sigma^2}+\frac{N}{2}\log(2\pi\sigma^2)$. If $\sigma$ is fixed, the log term is constant and the scale $1/(2\sigma^2)$ is a positive constant, so minimizing negative log-likelihood is equivalent to minimizing squared-error-type objectives.

This explains common practical loss choices. Many implementations use per-sample loss $\ell_i=\frac{1}{2}(y_i-z_i)^2$: constants from the Gaussian likelihood are dropped because they do not change the minimizer, and the factor $1/2$ is chosen so $\partial\ell_i/\partial z_i=z_i-y_i$ has no extra factor $2$. If one used $(y_i-z_i)^2$ instead, gradients differ only by a constant factor, which can be absorbed into learning-rate tuning.

So squared-error losses are not arbitrary penalties pasted onto neural-network regression; they arise directly from a Gaussian probabilistic output model, exactly as in linear regression. The key deep-learning change is only that $z$ is produced from learned hidden features.

---

Flashcards for this section are as follows:

- linear-Gaussian output unit ::@:: For real-valued targets, the linear-Gaussian head assumes $y\mid x \sim \mathcal{N}(z,\sigma^2)$, so the last-layer score $z$ plays the role of the predicted mean.
- linear activation in linear-Gaussian head ::@:: In a linear-Gaussian output unit, the output activation is identity $g_{\text{out}}(z)=z$, so the network score is used directly as the Gaussian mean.
- linear-Gaussian loss derivation ::@:: From $p(y\mid z)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\bigl(-\frac{(y-z)^2}{2\sigma^2}\bigr)$, one sample gives $-\log p(y\mid z)=\frac{(y-z)^2}{2\sigma^2}+\frac{1}{2}\log(2\pi\sigma^2)$, and summing over data gives $\sum_i\frac{(y_i-z_i)^2}{2\sigma^2}+\frac{N}{2}\log(2\pi\sigma^2)$.
- why $\tfrac{1}{2}(y-z)^2$ is commonly used ::@:: With fixed $\sigma$, additive constants and positive scale factors from Gaussian NLL can be dropped, and using $\ell=\tfrac{1}{2}(y-z)^2$ is convenient because $\partial\ell/\partial z=z-y$ has no extra factor $2$.
- role of the logit in Gaussian regression head ::@:: In a Gaussian regression head, the logit $z$ is not a log-odds; it is simply the predicted mean score, just as in ordinary linear regression.

### sigmoid output for binary classification

For a single binary output variable $y\in\{0,1\}$, the network can define $P(y\mid x)=\operatorname{Ber}(y\mid \sigma(z))$ using a scalar logit $z$. Starting from the Bernoulli mass function $p(y\mid z)=\sigma(z)^y(1-\sigma(z))^{1-y}$, the per-sample negative log-likelihood is $-\log p(y\mid z)=-\bigl(y\log \sigma(z)+(1-y)\log(1-\sigma(z))\bigr)$, which is the familiar binary cross entropy.

This is exactly the same loss used in ordinary logistic regression. The only difference is that logistic regression uses $z=w^\top x+b$, whereas a feedforward network uses $z=W^\top h+b$ with a learned representation $h$. The meaning of the logit is unchanged: it is still the log-odds score $\log\frac{p}{1-p}$. For the shallow-model derivation and decision-theoretic interpretation, see [logistic regression](logistic%20regression.md).

The lecture makes an important distinction here. Sigmoid units are often a poor choice for hidden layers because they saturate across much of their domain and cause deep-chain vanishing gradients. Yet they are fine as output units, because this saturation appears only once and typically coincides with small prediction error. The output-gradient formula is explicit: $\frac{\partial \ell}{\partial z}=\sigma(z)-y$. So when prediction is already correct and confident, the sample should contribute little to the gradient. This is the same binary cross-entropy setup derived in the logistic-regression note.

---

Flashcards for this section are as follows:

- binary output model in an FNN ::@:: For one binary target, an FNN can use $P(y\mid x)=\operatorname{Ber}(y\mid \sigma(z))$ with scalar logit $z$.
- binary cross entropy from sigmoid output ::@:: From the Bernoulli model $p(y\mid z)=\sigma(z)^y(1-\sigma(z))^{1-y}$, the negative log-likelihood becomes $-\bigl(y\log \sigma(z)+(1-y)\log(1-\sigma(z))\bigr)$.
- sigmoid head versus logistic regression ::@:: A sigmoid output layer in an FNN uses exactly the same Bernoulli likelihood and binary cross-entropy loss as logistic regression; only the features defining $z$ change from raw $x$ to learned $h$.
- why sigmoid is acceptable at the output layer ::@:: Sigmoid is acceptable as an output unit because the negative log-likelihood supplies a useful supervised signal even though sigmoid is problematic as a hidden-layer activation.
- sigmoid output-gradient formula ::@:: For Bernoulli negative log-likelihood, the output-logit gradient is $\partial\ell/\partial z=\sigma(z)-y$, so near-correct predictions naturally contribute small gradient.
- interpretation of $\sigma(z)-y \approx 0$ ::@:: Having $\sigma(z)-y \approx 0$ means the output probability closely matches the true binary label.
- given binary label $y=1$ and logit $z=0.5$, compute the binary cross-entropy loss $-\log\sigma(z)$ ::@:: $\sigma(0.5)\approx 0.622$; loss $=-\log(0.622)\approx 0.476$.

### softmax output for multiclass classification

If $y$ can take one of $C$ values, the network uses a vector of logits $z=(z_1,\ldots,z_C)^\top$ and a softmax output layer to define class probabilities $p_k=P(y=k\mid x)=\frac{e^{z_k}}{\sum_{c=1}^C e^{z_c}}$. This produces a valid categorical distribution because all probabilities are nonnegative and sum to one.

For a general target distribution over classes $r=(r_1,\ldots,r_C)$ with $r_k\ge 0$ and $\sum_k r_k=1$, categorical negative log-likelihood is $\ell=-\sum_{k=1}^{C} r_k\log p_k$. The one-hot-label case is the special case $r=t$ with one nonzero entry: then $\ell=-\sum_k t_k\log p_k=-\log p_y=-z_y+\log\sum_{c=1}^{C} e^{z_c}$. This is exactly multiclass cross entropy, the same form derived in softmax-regression notes. Its output-logit gradient is $\partial\ell/\partial z_k=p_k-r_k$ (special case $p_k-t_k$).

Again, the difference from the simpler model is not the head but the representation feeding it. A deep classifier is a learned feature extractor followed by an ordinary softmax probabilistic head. For the shallow multiclass derivation, stability details, and one-step softmax calculations, see [logistic regression](logistic%20regression.md#softmax-regression).

---

Flashcards for this section are as follows:

- softmax output formula ::@:: For multiclass targets, the softmax head uses $P(y=k\mid x)=\frac{e^{z_k}}{\sum_{c=1}^C e^{z_c}}$.
- why softmax defines a categorical distribution ::@:: Softmax outputs are nonnegative and sum to one, so they define a valid categorical distribution over classes.
- multiclass cross entropy general and one-hot cases ::@:: For target distribution $r$, categorical NLL is $\ell=-\sum_{k=1}^{C} r_k\log p_k = -\sum_{c=1}^{C} r_c z_c + \log\sum_{c=1}^{C} e^{z_c}$; with one-hot $t$ this reduces to $-\log p_y=-z_y+\log\sum_{c=1}^{C} e^{z_c}$, the same as softmax regression.
- softmax output-gradient formula ::@:: For softmax cross entropy with general target $r$, $\partial\ell/\partial z_k=p_k-r_k$ (one-hot special case $p_k-t_k$). Note this expression is a vector of length $C$, the number of classes.
- deep-classifier interpretation ::@:: A deep multiclass classifier can be understood as a learned feature transformation followed by a softmax regression head.
- given logits $z=(1,2,0)$ and one-hot target $t=(0,1,0)$ (class $2$ is correct), compute the softmax probabilities and multiclass cross-entropy loss ::@:: $Z=e^1+e^2+e^0\approx 2.718+7.389+1.000=11.107$; $p_1\approx 0.245$, $p_2\approx 0.665$, $p_3\approx 0.090$; loss $=-\log(p_2)\approx 0.407$.

## backpropagation

Training requires gradients of the loss with respect to every parameter in the network. Backpropagation provides these gradients efficiently by repeatedly applying the chain rule from the output layer back toward earlier layers.

The key computational idea is reuse. Instead of differentiating every weight independently from scratch, one computes local error terms and reuses them as the backward pass moves through the network. This turns a seemingly impossible bookkeeping problem into a practical algorithm that modern frameworks can execute at scale. A useful stage mnemonic is _store, compare, blame, update_: store forward activations, compare prediction with target at the output, assign blame backward through the network, then update parameters using the resulting gradients.

Conceptually, backpropagation is not a new objective; it is the differentiation procedure that makes optimizing the objective feasible. It is the backward counterpart of the forward repeated-composition view: the forward pass applies layer maps left to right, while the backward pass applies local derivatives right to left. The subsections below unpack that idea in coordinate form, Jacobian form, and layer-specific formulas.

---

Flashcards for this section are as follows:

- backpropagation purpose ::@:: Backpropagation computes the gradients of the loss with respect to all network parameters efficiently.
- why backpropagation is efficient ::@:: It reuses intermediate derivative information instead of differentiating each parameter independently from scratch.
- backpropagation stage mnemonic ::@:: A useful mnemonic is _store, compare, blame, update_: store forward activations, compare prediction with target, send blame backward, then update parameters from the resulting gradients.
- backpropagation versus objective ::@:: Backpropagation is the gradient-computation procedure, not the loss function itself.
- why deep learning needs backpropagation ::@:: Without backpropagation, training multilayer networks by gradient-based methods would be computationally impractical.

### chain rule and local error signals

The lecture revisits the chain rule before introducing the network formulas. This is not mere review: backpropagation is essentially a structured application of the chain rule to a layered composition of functions. Each local derivative tells how a unit's output changes with its input, and the backward pass multiplies these local sensitivities along the paths that influence the loss.

The central idea is to define an error signal at each pre-activation, typically denoted by $\delta = \frac{\partial L}{\partial z}$. This definition is not arbitrary. The pre-activation $z$ is exactly the point where the incoming weighted sum meets the nonlinearity, so once $\delta$ is known, both kinds of needed gradients become local: gradients with respect to incoming weights and gradients with respect to earlier activations.

Suppose $z_j^{(\ell)}=\sum_i W_{ij}^{(\ell)}a_i^{(\ell-1)}+b_j^{(\ell)}$ and $a_j^{(\ell)}=g(z_j^{(\ell)})$. Then with $\delta_j^{(\ell)}=\frac{\partial L}{\partial z_j^{(\ell)}}$:

- weight derivative: $\frac{\partial L}{\partial W_{ij}^{(\ell)}}=\frac{\partial L}{\partial z_j^{(\ell)}}\frac{\partial z_j^{(\ell)}}{\partial W_{ij}^{(\ell)}}=\delta_j^{(\ell)}a_i^{(\ell-1)}$;
- bias derivative: $\frac{\partial L}{\partial b_j^{(\ell)}}=\frac{\partial L}{\partial z_j^{(\ell)}}\frac{\partial z_j^{(\ell)}}{\partial b_j^{(\ell)}}=\delta_j^{(\ell)}$;
- previous-activation derivative: $\frac{\partial L}{\partial a_i^{(\ell-1)}}=\sum_j \frac{\partial L}{\partial z_j^{(\ell)}}\frac{\partial z_j^{(\ell)}}{\partial a_i^{(\ell-1)}}=\sum_j W_{ij}^{(\ell)}\delta_j^{(\ell)}$.

So one local quantity ($\delta$) simultaneously controls (i) how to update incoming weights, (ii) how to update bias, and (iii) how to propagate sensitivity backward.

A quick scalar worked example: let $z=wa+b$ with $a=2$, $w=0.5$, $b=0.1$, and suppose from downstream we already have $\delta=\partial L/\partial z=-0.3$. Then $\partial L/\partial w=a\delta=2(-0.3)=-0.6$, $\partial L/\partial b=\delta=-0.3$, and $\partial L/\partial a=w\delta=0.5(-0.3)=-0.15$. This compactly shows the three outputs of one local chain-rule block.

---

Flashcards for this section are as follows:

- why the chain rule is central ::@:: Backpropagation is a repeated application of the chain rule to the layered composition defining the network.
- local error signal $\delta = \frac{\partial L}{\partial z}$ ::@:: A backpropagation error signal measures how sensitive the loss is to the pre-activation of a unit.
- weight-gradient derivation from local error ::@:: If $z_j^{(\ell)}=\sum_i W_{ij}^{(\ell)}a_i^{(\ell-1)}+b_j^{(\ell)}$ and $\delta_j^{(\ell)}=\partial L/\partial z_j^{(\ell)}$, then $\partial L/\partial W_{ij}^{(\ell)}=a_i^{(\ell-1)}\delta_j^{(\ell)}$.
- bias-gradient derivation from local error ::@:: With $z_j^{(\ell)}=\sum_i W_{ij}^{(\ell)}a_i^{(\ell-1)}+b_j^{(\ell)}$ and $\delta_j^{(\ell)}=\partial L/\partial z_j^{(\ell)}$, we get $\partial L/\partial b_j^{(\ell)}=\delta_j^{(\ell)}$ because $\partial z_j^{(\ell)}/\partial b_j^{(\ell)}=1$.
- backward-propagation derivation from local error ::@:: With the same notation, $\partial L/\partial a_i^{(\ell-1)}=\sum_j W_{ij}^{(\ell)}\delta_j^{(\ell)}$, so local errors are exactly the quantities needed to propagate blame backward.
- given $z=wa+b$ with $a=2$, $w=0.5$, and downstream $\delta=\partial L/\partial z=-0.3$, compute $\partial L/\partial w$, $\partial L/\partial b$, and $\partial L/\partial a$ ::@:: We get $\partial L/\partial w=a\delta=-0.6$, $\partial L/\partial b=\delta=-0.3$, and $\partial L/\partial a=w\delta=-0.15$.

### repeated transposed-Jacobian viewpoint

The repeated-composition viewpoint for the forward pass has a matching backward form. Let $\Psi_{\ell}:\mathbb R^{n_{\ell-1}}\to\mathbb R^{n_{\ell}}$ be the layer map, let $J_{\Psi_{\ell}}(a^{(\ell-1)})$ be its Jacobian at $a^{(\ell-1)}$, and let $\nabla_{a^{(\ell)}}L$ denote the gradient of loss with respect to activations at layer $\ell$. If $a^{(\ell)}=\Psi_{\ell}(a^{(\ell-1)})$ and loss is $L(a^{(L)},y)$, then chain rule gives $\nabla_{a^{(\ell-1)}}L = J_{\Psi_{\ell}}(a^{(\ell-1)})^\top \nabla_{a^{(\ell)}}L$. Thus the backward pass is repeated application of transposed local Jacobians from layer $L$ back to layer $1$.

For an affine-plus-activation layer, write $z^{(\ell)}=(W^{(\ell)})^\top a^{(\ell-1)}+b^{(\ell)}$ and $a^{(\ell)}=g^{(\ell)}(z^{(\ell)})$. Then the Jacobian factors into affine and activation parts. In vector form:

- local pre-activation error: $\delta^{(\ell)}=\nabla_{z^{(\ell)}}L = g'^{(\ell)}(z^{(\ell)})\odot \nabla_{a^{(\ell)}}L$;
- previous-layer gradient: $\nabla_{a^{(\ell-1)}}L = W^{(\ell)}\delta^{(\ell)}$;
- parameter gradients: $\nabla_{W^{(\ell)}}L=a^{(\ell-1)}(\delta^{(\ell)})^\top$ and $\nabla_{b^{(\ell)}}L=\delta^{(\ell)}$.

Mini matrix example: let $W=\begin{bmatrix}1&2\\0&1\end{bmatrix}$, $D=\operatorname{diag}(0.5,0.1)$, and upstream gradient $\nabla_{a^{(\ell)}}L=\begin{bmatrix}0.4\\-0.2\end{bmatrix}$. Then $\delta=D\nabla_{a^{(\ell)}}L=\begin{bmatrix}0.2\\-0.02\end{bmatrix}$ and $\nabla_{a^{(\ell-1)}}L=W\delta=\begin{bmatrix}0.16\\-0.02\end{bmatrix}$. This is the concrete transposed-Jacobian computation in coordinates.

This yields a natural forward/backward symmetry. Forward propagation says _matrix, bias, activation_; backward propagation says _activation derivative, weight transpose effect, repeat_. A good mnemonic is _forward: mix, shift, bend, repeat; backward: compare, slope, unmix, repeat_. The word _unmix_ is not literal matrix inversion; it means sending sensitivity information backward through the weight pattern that mixed coordinates in the forward pass.

This viewpoint also links directly to the existing $\delta$ formulas. The usual hidden-layer recursion is just the coordinate form of the transposed-Jacobian rule, so the "local error" story and the "matrix chain rule" story are two descriptions of the same algorithm.

---

Flashcards for this section are as follows:

- repeated transposed-Jacobian viewpoint ::@:: If $a^{(\ell)}=\Psi_{\ell}(a^{(\ell-1)})$, then backpropagation uses $\nabla_{a^{(\ell-1)}}L = J_{\Psi_{\ell}}(a^{(\ell-1)})^\top \nabla_{a^{(\ell)}}L$, so the backward pass is repeated application of transposed local Jacobians in reverse order.
- matrix form of local backpropagation ::@:: For one layer, the local error is $\delta^{(\ell)}=g'^{(\ell)}(z^{(\ell)})\odot \nabla_{a^{(\ell)}}L$ and the previous-layer gradient is $\nabla_{a^{(\ell-1)}}L=W^{(\ell)}\delta^{(\ell)}$.
- notation in the Jacobian viewpoint ::@:: In $\nabla_{a^{(\ell-1)}}L = J_{\Psi_{\ell}}(a^{(\ell-1)})^\top \nabla_{a^{(\ell)}}L$, $\Psi_{\ell}:\mathbb R^{n_{\ell-1}}\to\mathbb R^{n_{\ell}}$ is the layer map and $J_{\Psi_{\ell}}$ is its local Jacobian matrix.
- given $W=\begin{bmatrix}1&2\\0&1\end{bmatrix}$, $D=\operatorname{diag}(0.5,0.1)$, and upstream gradient $\nabla_{a^{(\ell)}}L=\begin{bmatrix}0.4\\-0.2\end{bmatrix}$, compute $\delta=D\nabla_{a^{(\ell)}}L$ and $\nabla_{a^{(\ell-1)}}L=W\delta$ ::@:: We get $\delta=\begin{bmatrix}0.2\\-0.02\end{bmatrix}$ and $\nabla_{a^{(\ell-1)}}L=\begin{bmatrix}0.16\\-0.02\end{bmatrix}$.
- forward-backward mnemonic ::@:: A useful symmetry mnemonic is _forward: mix, shift, bend, repeat; backward: compare, slope, unmix, repeat_.
- local-error view versus Jacobian view ::@:: The local-error recursion with $\delta$ and the repeated-transposed-Jacobian view are the same backpropagation algorithm written in coordinate form versus matrix form.

### output-layer derivatives

For the output layer, the lecture defines a local error term $\delta_k = \frac{\partial L}{\partial z_k}$ at each output pre-activation $z_k$. If $u_j$ is the activation feeding into output unit $k$ and $W_{kj}$ is the corresponding weight, then the gradient is $\frac{\partial L}{\partial W_{kj}} = u_j\delta_k$. The same local-error viewpoint also gives the bias gradient immediately, because the derivative of $z_k$ with respect to its bias is $1$.

This formula is important because it shows the general interpretation of a neural-network weight gradient: _input activation times local blame_. The previous layer tells how much signal arrived; the error term tells how strongly the current unit contributed to the final loss. The loss function and activation only determine the exact form of $\delta_k$.

Two common heads give standard closed forms. For sigmoid plus binary cross entropy, $\delta=\sigma(z)-y$. For softmax plus multiclass cross entropy with target distribution $r$, $\delta_k=p_k-r_k$.

A tiny numeric binary example: if $u=0.8$, $y=1$, and current output is $\hat y=0.7$, then $\delta=\hat y-y=-0.3$, so $\partial\ell/\partial W=u\delta=0.8(-0.3)=-0.24$ and $\partial\ell/\partial b=\delta=-0.3$. The negative sign means gradient descent increases both weight and bias, raising the logit toward the positive class.

---

Flashcards for this section are as follows:

- output-layer error term ::@:: At the output layer, a standard backpropagation error term is $\delta_k = \frac{\partial L}{\partial z_k}$.
- output-layer weight gradient ::@:: If $u_j$ feeds output unit $k$, then $\frac{\partial L}{\partial W_{kj}} = u_j\delta_k$.
- output-layer gradient interpretation ::@:: A neural-network output-layer weight gradient is _incoming activation times local blame_: the activation says how much signal arrived, and $\delta_k$ says how harmful or helpful that unit's pre-activation was for the loss.
- common output-layer delta formulas ::@:: For sigmoid plus binary cross entropy, $\delta=\sigma(z)-y$; for softmax plus multiclass cross entropy with target $r$, $\delta_k=p_k-r_k$.
- bias gradient at the output layer ::@:: Because $\partial z_k/\partial b_k=1$, the bias gradient at an output unit is just the local error: $\partial L/\partial b_k=\delta_k$.
- given binary output with incoming activation $u=0.8$, prediction $\hat y=0.7$, and label $y=1$, compute $\delta=\hat y-y$, $\partial\ell/\partial W=u\delta$, and $\partial\ell/\partial b$ ::@:: We get $\delta=-0.3$, $\partial\ell/\partial W=-0.24$, and $\partial\ell/\partial b=-0.3$.

### hidden-layer derivatives

Hidden layers are where backpropagation earns its name. A hidden unit does not influence the loss directly; it influences later units, which then influence the loss. Therefore, the hidden-layer error is computed recursively by propagating downstream errors backward through the connecting weights and multiplying by the derivative of the activation function.

In coordinates, if hidden unit $j$ at layer $\ell$ feeds units $k$ in layer $\ell+1$, then $\delta_j^{(\ell)}=g'(z_j^{(\ell)})\sum_k W_{jk}^{(\ell+1)}\delta_k^{(\ell+1)}$. The sum says how much downstream units blame this hidden activation, and the factor $g'(z_j^{(\ell)})$ converts that blame from activation space back to pre-activation space. This is exactly the intuition behind "error at a unit before the nonlinearity".

Vector form is often cleaner: $\delta^{(\ell)}=D^{(\ell)}\bigl(W^{(\ell+1)}\delta^{(\ell+1)}\bigr)$ where $D^{(\ell)}=\operatorname{diag}(g'^{(\ell)}(z^{(\ell)}))$. Once $\delta^{(\ell)}$ is known, hidden-layer gradients follow the same local template as output layers: $\nabla_{W^{(\ell)}}L=a^{(\ell-1)}(\delta^{(\ell)})^\top$ and $\nabla_{b^{(\ell)}}L=\delta^{(\ell)}$.

Worked hidden-unit example: suppose one hidden unit has outgoing weights to two downstream units equal to $2$ and $-1$, downstream errors are $0.3$ and $-0.1$, and local derivative is $g'(z_j)=0.25$. Then $\delta_j=0.25\bigl(2\cdot0.3+(-1)\cdot(-0.1)\bigr)=0.25(0.7)=0.175$. If one incoming activation is $a_i=0.8$, then $\partial L/\partial W_{ij}=a_i\delta_j=0.8\cdot0.175=0.14$, and $\partial L/\partial b_j=\delta_j=0.175$.

The resulting hidden error term can then be used exactly like an output-layer error term to compute gradients for earlier weights. The important conceptual lesson is that backpropagation is dynamic programming for derivatives. Once later-layer errors are known, earlier-layer errors are obtained by a recursive reuse formula rather than by restarting the differentiation from zero.

---

Flashcards for this section are as follows:

- why hidden layers need backward propagation ::@:: Hidden units affect the loss only indirectly through later layers, so their error signals must be computed from downstream error terms.
- hidden-layer backprop formula ::@:: If unit $j$ at layer $\ell$ feeds units $k$ in layer $\ell+1$, then $\delta_j^{(\ell)}=g'(z_j^{(\ell)})\sum_k W_{jk}^{(\ell+1)}\delta_k^{(\ell+1)}$.
- hidden-layer backprop idea ::@:: A hidden-layer error term is obtained by weighting downstream errors by the relevant outgoing weights and multiplying by the local activation derivative, so hidden blame is downstream blame pulled back through one layer.
- role of $g'(z_j)$ in hidden-layer backprop ::@:: The factor $g'(z_j)$ tells how strongly changes in the hidden pre-activation change that hidden unit's output.
- hidden-layer vector recursion and bias gradient ::@:: In vector form, $\delta^{(\ell)}=D^{(\ell)}(W^{(\ell+1)}\delta^{(\ell+1)})$, then $\nabla_{W^{(\ell)}}L=a^{(\ell-1)}(\delta^{(\ell)})^\top$ and $\nabla_{b^{(\ell)}}L=\delta^{(\ell)}$.
- given hidden unit with outgoing weights $(2,-1)$, downstream deltas $(0.3,-0.1)$, local derivative $g'(z_j)=0.25$, and incoming activation $a_i=0.8$, compute $\delta_j$, $\partial L/\partial W_{ij}$, and $\partial L/\partial b_j$ ::@:: We get $\delta_j=0.25(2\cdot0.3+(-1)\cdot(-0.1))=0.175$, then $\partial L/\partial W_{ij}=a_i\delta_j=0.14$ and $\partial L/\partial b_j=0.175$.
- backpropagation as derivative dynamic programming ::@:: Backpropagation is efficient because it reuses downstream derivative information recursively instead of recomputing every chain-rule path from scratch.

### algorithm and implementation notes

The lecture summarizes backpropagation as a two-stage algorithm performed for each training example or minibatch. First, run the forward pass and store needed pre-activations and activations. Second, compute output errors, propagate them backward through hidden layers, and assemble parameter gradients. A useful mnemonic is _forward, compare, backpropagate blame, accumulate gradients, update_.

How parameters are updated depends on batch size $B$:

- per-sample update (stochastic gradient descent in the strict sense): $B=1$;
- minibatch stochastic gradient descent: $1<B<N$;
- full-batch gradient descent: $B=N$ over the whole training set.

For a minibatch $\mathcal B$, a standard update is $\theta\leftarrow\theta-\eta\,\frac{1}{B}\sum_{i\in\mathcal B}\nabla_{\theta}\ell_i$. The division by $B$ is important: it keeps gradient scale more comparable across different batch sizes and makes learning-rate interpretation more stable. Some implementations use summed gradients instead; that is equivalent to averaging if one rescales $\eta$ by $1/B$.

The slides also connect the mathematics to implementation. Modern frameworks such as PyTorch and TensorFlow store parameters and activations in tensors for efficiency. A tensor is just a multidimensional array together with a shape: a one-dimensional tensor is a vector, a two-dimensional tensor is a matrix, and higher-order tensors represent structured batches of data such as images or sequences. For example, a minibatch of feature vectors might have shape $(B,D)$, a minibatch of images might have shape $(B,C,H,W)$, and a minibatch of token embeddings might have shape $(B,T,D)$. This is why deep-learning libraries can implement the forward and backward passes compactly and quickly: entire batches and layers are processed by bulk tensor operations rather than scalar loops.

The final practical lesson is interpretive as well as computational. Backpropagation is a bookkeeping system for blame assignment: the output compares prediction with target, each unit receives a local blame score, and the gradients tell how to change parameters so future blame is reduced. ReLU units are often easier to train than sigmoid and tanh units, deeper structure can help, but learning-rate tuning still remains important during training.

---

Flashcards for this section are as follows:

- two-stage backpropagation algorithm ::@:: Backpropagation proceeds by first running a forward pass to store activations and pre-activations, then a backward pass to compute output errors, propagate them backward, and assemble gradients.
- why SGD naturally pairs with backpropagation ::@:: Backpropagation provides the gradients needed by gradient-descent and stochastic-gradient-descent updates of network parameters.
- per-sample, minibatch, and full-batch updates ::@:: Per-sample SGD uses $B=1$, minibatch SGD uses $1<B<N$, and full-batch gradient descent uses $B=N$.
- averaged minibatch update rule ::@:: A common update is $\theta\leftarrow\theta-\eta\,\frac{1}{B}\sum_{i\in\mathcal B}\nabla_{\theta}\ell_i$, where averaging by $B$ keeps gradient scale more stable across batch sizes.
- why divide by batch size ::@:: Dividing minibatch gradients by $B$ avoids implicit scaling of update magnitude with batch size; using summed gradients is equivalent only if the learning rate is rescaled accordingly.
- tensors in deep-learning frameworks ::@:: Deep-learning frameworks store parameters and activations in tensors, meaning multidimensional arrays with shapes such as $(B,D)$, $(B,C,H,W)$, or $(B,T,D)$, so forward and backward computations can be carried out efficiently in bulk.
- what a 1-D and 2-D tensor represent ::@:: A 1-D tensor is a vector, a 2-D tensor is a matrix, and higher-order tensors store structured batches such as images, sequences, or feature maps.
- backpropagation interpretation ::@:: Backpropagation can be interpreted as systematic blame assignment: compare prediction with target at the output, assign local blame to each unit, and convert that blame into parameter gradients.
- practical demo lesson about activations ::@:: The lecture demonstrations suggest that ReLU units are often easier to learn than sigmoid or tanh units in deep feedforward networks.
- practical demo lesson about depth and learning rate ::@:: The demonstration slides emphasize that deeper structure can help but the learning rate still needs careful adjustment during training.
