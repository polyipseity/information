---
aliases:
  - SVM
  - SVMs
  - SVN
  - SVNs
  - support vector machine
  - support vector machines
  - support vector network
  - support vector networks
tags:
  - flashcard/active/general/eng/support_vector_machine
  - language/in/English
---

# support vector machine

## linear SVM

Any [hyperplane](hyperplane.md) (e.g. {@{any point for 1D, any line for 2D, any plane for 3D}@}) can be written as {@{the set of points $\mathbf{x}$ satisfying $$\mathbf{w}^\intercal \mathbf{x} - b = 0$$}@}. $\mathbf{w}$ is {@{the (not necessarily normalized) [normal vector](normal%20(geometry).md) to the hyperplane. $\frac b {\lVert \mathbf{w} \rVert}$ is the offset of the hyperplane from the origin in the direction of the normal vector $\mathbf{w}$}@}. This is like {@{the [Hesse normal form](Hesse%20normal%20form.md), except that the normal vector $\mathbf{w}$ may not be normalized}@}. <!--SR:!2025-12-11,406,310!2027-06-25,840,330!2025-06-20,240,270!2026-09-04,577,290-->

### hard-margin

If the training data is {@{[linearly separable](linear%20separability.md)}@}, we can {@{select 2 parallel [hyperplanes](hyperplane.md) that both separates the 2 classes of data in the training data}@}, such that {@{the distance between the 2 hyperplanes is as large as possible}@}. The region {@{bounded by these 2 hyperplanes is called the _margin_}@}, and {@{the _maximum-margin hyperplane_ is the hyperplane that lies halfway between them}@}. <!--SR:!2025-07-14,303,330!2026-01-17,353,250!2026-11-22,682,330!2027-06-30,837,330!2027-11-08,923,310-->

With a {@{normalized or standardized dataset}@}, the 2 hyperplanes can be described by {@{the equations}@}: {@{$$\mathbf{w}^\intercal \mathbf{x} - b = 1$$ with anything on or above this boundary is of class 1}@}, and {@{$$\mathbf{w}^\intercal \mathbf{x} - b = -1$$ with anything on or below this boundary is of class -1}@}. <!--SR:!2026-08-01,535,330!2028-08-09,1175,350!2027-12-09,987,350!2028-07-21,1163,350-->

Geometrically, the distance {@{between these 2 hyperplanes is $\frac 2 {\lVert \mathbf{w} \rVert}$}@}, so to maximize the distance, we want to {@{minimize $\lVert \mathbf{w} \rVert$}@}. The above distance is calculated {@{using the [distance from a point to a plane](distance%20from%20a%20point%20to%20a%20plane.md) equation}@}. To prevent data points from going through the margin, we add {@{the following constraints}@}: For each {@{data point $i$ with [feature vector](feature%20vector.md) $\mathbf{x}_i$ and label $y_i \in \set{-1, 1}$}@}, {@{$$\begin{cases} \mathbf{w}^\intercal \mathbf{x}_i - b \ge 1 & \text{if }y_i = 1 \\ \mathbf{w}^\intercal \mathbf{x}_i - b \le -1 & \text{if }y_i = -1 \end{cases}$$}@}. These constraints state that {@{all data points lie on the correct side of the margin}@}. The above constraints are usually rewritten as {@{$$y_i \left(\mathbf{w}^\intercal \mathbf{x}_i - b \right) \ge 1 \quad \text{for all }1 \le i \le n$$}@}. <!--SR:!2026-01-19,263,290!2026-07-28,586,330!2026-03-13,477,310!2027-10-24,951,350!2025-12-21,365,290!2026-12-24,649,310!2028-10-06,1224,350!2027-04-09,763,310-->

Put the above together to get the following {@{[quadratic programming](quadratic%20programming.md), which has efficient algorithms to compute the solution}@}: {@{$$\begin{align} & \underset{\mathbf{w},\;b}{\operatorname{minimize} } && \lVert \mathbf{w} \rVert^2_2 \\ & \text{subject to} && y_i \left(\mathbf{w}^\intercal \mathbf{x}_i - b \right) \geq 1 \quad \forall i \in \{1,\dots,n\} \end{align}$$}@}. <!--SR:!2027-05-26,765,290!2027-03-04,716,290-->

The {@{$\mathbf{w}$ and $b$ that solve this quadratic programming problem}@} determine the final classifier, {@{$$\mathbf{x} \mapsto \operatorname{sgn}\left(\mathbf{w}^\intercal \mathbf{x} - b \right)$$}@}, where $\operatorname{sgn}(*)$ is {@{the [sign function](sign%20function.md)}@}. <!--SR:!2026-10-10,647,330!2027-07-22,866,330!2025-07-15,303,330-->

An important consequence of the above description is that {@{the max-margin hyperplane is completely determined by $\mathbf{x}_i$ in the training data that lie closest to it}@}. These $\mathbf{x}_i$ are called {@{_support vectors_}@}. <!--SR:!2028-10-07,1224,350!2027-02-12,729,330-->

## nonlinear kernels

For [non-linearly separable](linear%20separability.md) data, {@{the data could be mapped into a higher-dimensional space in a non-linear way for easier separation by a hyperplane}@}. This transformed is done using {@{the [kernel trick](kernel%20method.md#mathematics%20the%20kernel%20trick)}@}. <!--SR:!2026-02-02,445,310!2028-03-01,1051,350-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/support_vector_machine) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
