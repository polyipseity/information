---
aliases:
  - HKUST PHYS 1314
  - HKUST PHYS 1314 index
  - HKUST PHYS1314
  - HKUST PHYS1314 index
  - Honors General Physics II
  - Honors General Physics II index
  - PHYS 1314
  - PHYS 1314 index
  - PHYS1314
  - PHYS1314 index
tags:
  - flashcard/active/special/academia/HKUST/PHYS_1314/index
  - function/index
  - language/in/English
---

# index

- HKUST PHYS 1314
- name: Honors General Physics II

The content is in teaching order.

- grading
  - scheme
    - homework: 0.15
    - midterm exam: 0.35
    - final exam: 0.5
- logistics

## children

- [assignments](assignments/)
- [questions](questions.md)

## assessments

## week 1 lecture

- datetime: 2025-02-03T09:00:00+08:00/2025-02-03T10:20:00+08:00
- topic: Introduction, Electric Charge and Electric Field
- course logistics
- [electric charge](../../../../general/electric%20charge.md) ::@:: positive/negative <br/> transferrable, via _electric current_ <br/> quantized, in multiples of the _elementary charge_ _e_ ≈ 1.602×10<sup>−19</sup>&nbsp;C
- [electroscope](../../../../general/electroscope.md) ::@:: It consists of a thin metal strip that is attached to a metallic rod. The metallic rod is contained in a glass window box and is electrically isolated from the supporting table.
  - electroscope / experiment ::@:: charged: Touching/almost touching it with a (positively or negatively) charged object, the metal strip deflects. <br/> uncharged: Grounding it with a metallic object, the metal strip is restored. <p> If the charged object touches it, charges are transferred to the metal strip, and like charges in the metal strip repel each other. Separately, the metal strip still deflects even if the charged object only almost touches it because this action can _induce_ electric charges.
- [Van de Graaff generator](../../../../general/Van%20de%20Graaff%20generator.md) ::@:: It uses the friction between a revolving belt and a pick-up brush to accumulate a net electric charge on the metal sphere.
  - Van de Graaff generator / experiment ::@:: When we place another metal sphere, grounded to the ground, next to the metal sphere of a running Van de Graaff generator, we can see periodic sparks between the two metal spheres and hear sounds. <p> Electric charges are flowing from the Van de Graaff generator to the other metal sphere through the air, which ionizes the air. This phenomenon is called _lightning_.
- [superposition principle](../../../../general/superposition%20principle.md) ::@:: It states that, for all linear systems, the net response caused by two or more stimuli is the sum of the responses that would have been caused by each stimulus individually.
  - superposition principle / total charge of a system ::@:: The total charge of a system is the summation of all individual charges.
  - superposition principle / electrostatic force ::@:: The electrostatic force on a test charge by a collection of charged objects is the vector sum over the electrostatic forces on the test charge by each charged object.
- [charge conservation](../../../../general/charge%20conservation.md) ::@:: In an _isolated_ (less accurately, _closed_) system the sum of positive and negative charges is constant.
- [Coulomb's law](../../../../general/Coulomb's%20law.md) ::@:: In a vacuum, $$\mathbf {F} _{1}={\frac {q_{1}q_{2} }{4\pi \varepsilon _{0} } }{ {\hat {\mathbf {r} } }_{12} \over {|\mathbf {r} _{12}|}^{2} }$$ where $\mathbf {r_{12}=r_{1}-r_{2} }$ is the [displacement vector](../../../../general/displacement%20vector.md) between the charges, ${\hat {\mathbf {r} } }_{12}$ a [unit vector](../../../../general/unit%20vector.md) pointing from $q_{2}$ to $q_{1}$, and $\varepsilon _{0} \approx 8.854 \times 10^{-12}~\mathrm{F/m}$ the [electric constant](../../../../general/electric%20constant.md) (a.k.a. _permittivity of the free space_).
  - Coulomb's law / experiment ::@:: Coulomb used the _torsion balance_ to study the effects of electric charges. It can measure very weak forces.
- [questions § Coulomb's law](questions.md#Coulomb's%20law)

## week 1 lecture 2

- datetime: 2025-02-05T09:00:00+08:00/2025-02-05T10:20:00+08:00
- topic: Electric Field II
- [hierarchy problem](../../../../general/hierarchy%20problem.md) ::@:: Why is gravity so weak compared to electromagnetic force (and weak force and strong force)?
  - hierarchy problem / example ::@:: Consider two double positively charged helium ions. The electrostatic repulsion between them is about 10<sup>39</sup> times stronger than gravity.
  - hierarchy problem / idea ::@:: Even though gravity is very weak, it is the only force that matters at macroscopic scale. This is because gravity always attract but electrostatic force cancels out as objects have a net charge of zero.
- [scientific law](../../../../general/scientific%20law.md) ::@:: They are scientific generalizations based on _empirical observations_ of physical behavior. This highlights the _observational nature_ of the physical science.
- [electric field](../../../../general/electric%20field.md) ::@:: a vector field that associates to each point in space the force per unit of charge exerted on an infinitesimal test charge at rest at that point
  - electric field / experiment ::@:: We can "observe" the electric field by deflecting an electric beam. An electric beam are emitted electrons that pass through two plates electrodes with a potential difference. <p> The larger the potential difference, the more the electro beam deflects. Reversing the polarity of the potential difference leads to the electro beam being deflected the other way. <p> This shows the space between the plates are being permeated with a physical quantity that acts on charged particles, which should also be a vector.
  - electric field / calculation ::@:: $$\mathbf {E} _{1}(\mathbf {r} _{0})={\frac {\mathbf {F} _{01} }{q_{0} } }={\frac {q_{1} }{4\pi \varepsilon _{0} } }{ {\hat {\mathbf {r} } }_{01} \over {|\mathbf {r} _{01}|}^{2} }={\frac {q_{1} }{4\pi \varepsilon _{0} } }{\mathbf {r} _{01} \over {|\mathbf {r} _{01}|}^{3} }$$ where $\mathbf {E} _{1}(\mathbf {r} _{0})$ is the component of the electric field at $q_{0}$ due to $q_{1}$. <p> Make use of the superposition principle when there are multiple electric charges. <p> For continuous charge distribution, we replace the summation with a line, surface, or volume integral, and the charge with charge density (resp. per length, per area, per volume) instead.
  - electric field / visualization ::@:: As it is a vector field, we can visualize it as many arrows representing the vector at certain positions in a region of space. <p> For a positively charged particle, the surrounding arrows diverge outwards (positive divergence). For a negatively charged particle, the surrounding arrows converge inwards (negative divergence).
  - electric field / approximation ::@:: We can approximate electric fields in some situations. <p> For concreteness, consider two equal positively charged particles $q_1, q_2$ at distance $d$ from each other. The electric field at very far away from the two charged particles (the distance from the middle of the two particles $D$ is $D \gg d$) is approximately the same as that generated by one positively charged particle with double the charge located at the middle of $q_1$ and $q_2$. <p> Another example is similar to above, but with a line charge instead, which at far away distance approximately looks like a point charge. Make use of symmetry when trying to work out this example.
  - electric field / interpretation ::@:: What is the electric field? Humans cannot detect it, but some other animals can. <p> Maxwell believed that electromagnetic fields are stress and strains in a medium that called _ether_, which permeates throughout the universe. But special relativity had forced us to abandon this idea. <p> Our current interpretation (at least in this course) is that it is a vector field determined by physical laws.

## week 1 tutorial

- datetime: 2025-02-05T18:00:00+08:00/2025-02-05T18:50:00+08:00
- topic: differential calculus
- [differential calculus](../../../../general/differential%20calculus.md)
  - differential calculus / [differential form](../../../../general/differential%20form.md) ::@:: No need to go too formal into its mathematical treatment for physics at this stage... <p> Treat $\mathrm dx$ as an infinitesimal amount. Then $f' = \frac {\mathrm df} {\mathrm dx}$. <p> $\mathrm d^2 x$ is an infinitesimal area. $\mathrm d^3 x$ is an infinitesimal volume.
- [gradient](../../../../general/gradient.md) ::@:: It of a scalar-valued differentiable function $f$ of several variables is the vector field (or vector-valued function) $\nabla f$ whose value at a point $p$ gives the direction and the rate of fastest increase.
  - gradient / definition ::@:: You have a 3D scalar field $\varphi$. Gather its partial derivatives along the Cartesian axes to get the gradient vector field. <p> Mathematically, the gradient is $\nabla \varphi(x, y, z) = \left. \frac {\partial \varphi} {\partial x} \right|_{(x, y, z)} \vec x + \left. \frac {\partial \varphi} {\partial y} \right|_{(x, y, z)} \vec y + \left. \frac {\partial \varphi} {\partial z} \right|_{(x, y, z)} \vec z$. Using infinitesimals, we have $\mathrm d\varphi = \frac {\partial \varphi} {\partial x} \mathrm dx + \frac {\partial \varphi} {\partial y} \mathrm dy + \frac {\partial \varphi} {\partial z} \mathrm dz$.
- [del](../../../../general/del.md) ::@:: We can treat $\nabla$ as an linear vector operator (but it is _not_ simply a vector as it has neither a magnitude nor a direction by itself): $\begin{bmatrix} \frac \partial {\partial x} & \frac \partial {\partial y} & \frac \partial {\partial z} \end{bmatrix}^\intercal$. Then it becomes clear $\nabla$ acts on a scalar, which in this case is $\varphi : \mathbb R^3 \to \mathbb R$, and returns its gradient $\nabla \varphi : \mathbb R^3 \to \mathbb R^3$. <p> This would make more sense later when we have the Laplace operator, which is $\nabla^2 = \nabla \cdot \nabla = \begin{bmatrix} \frac \partial {\partial x} & \frac \partial {\partial y} & \frac \partial {\partial z} \end{bmatrix}^\intercal \cdot \begin{bmatrix} \frac \partial {\partial x} & \frac \partial {\partial y} & \frac \partial {\partial z} \end{bmatrix}^\intercal = \begin{bmatrix} \frac {\partial^2} {\partial x^2} & \frac {\partial^2} {\partial y^2} & \frac {\partial^2} {\partial z^2} \end{bmatrix}^\intercal$. In this, we can see that the dot product works as expected.
- [gradient](../../../../general/gradient.md)
  - gradient / rules ::@:: The rules are quite similar to single-variable calculus. For example, let $\varphi(\vec r) = \vec r \cdot \vec r = \lVert \vec r \rVert^2 = r_1^2 + r_2^2 + r_3^2$. Then $\nabla \varphi(\vec r) = 2 \vec r = 2r_1 + 2r_2 + 2r_3$. Compare this with the derivative of $f(x) = x^2$ being $2x$.
- [divergence](../../../../general/divergence.md) ::@:: It is a vector operator that operates on a vector field, producing a scalar field giving the quantity of the vector field's source at each point. More technically, the divergence represents the volume density of the outward flux of a vector field from an infinitesimal volume around a given point.
  - divergence / definition ::@:: $\nabla \cdot \mathbf v = \begin{bmatrix} \frac \partial {\partial x} & \frac \partial {\partial y} & \frac \partial {\partial z} \end{bmatrix}^\intercal \cdot \begin{bmatrix} v_x & v_y & v_z \end{bmatrix}^\intercal = \frac {\partial v_x} {\partial x} + \frac {\partial v_y} {\partial y} + \frac {\partial v_z} {\partial z}$ <p> It looks like the dot product works as expected.
- [curl](../../../../general/curl%20(mathematics).md) ::@::  It is vector operator that describes the infinitesimal circulation of a vector field in three-dimensional Euclidean space. The curl at a point in the field is represented by a vector whose length and direction denote the magnitude and axis of the maximum circulation. The curl of a field is formally defined as the circulation density at each point of the field.
  - curl / definition ::@:: $\nabla \times \mathbf v = \begin{vmatrix} \mathbf x & \mathbf y & \mathbf z \\ \frac \partial {\partial x} & \frac \partial {\partial y} & \frac \partial {\partial z} \\ v_x & v_y & v_z \end{vmatrix} = \left\langle \frac {\partial v_z} {\partial y} - \frac {\partial v_y} {\partial z}, \frac {\partial v_x} {\partial z} - \frac {\partial v_z} {\partial x}, \frac {\partial v_y} {\partial x} - \frac {\partial v_x} {\partial y} \right\rangle$
- [del](../../../../general/del.md)
  - del / properties
    - del / properties / linearity ::@:: It is a linear vector operator. So $\nabla$, $\nabla \cdot$, and $\nabla \times$ distributes over addition and is homogenous under _scalar_ (scalar in this context are scalar fields) multiplication.
    - del / properties / product rules (easier) ::@:: These 4 rules are the easier ones: $$\begin{aligned} \nabla (fg) & = f \nabla g + g \nabla f \\ \nabla \cdot (f \mathbf v) & = f (\nabla \cdot \mathbf v) + \mathbf v \cdot (\nabla f) \\ \nabla \times (f \mathbf v) & = f (\nabla \times \mathbf v) - \mathbf v \times (\nabla f) \\ \nabla \cdot (\mathbf u \times \mathbf v) & = -\mathbf u \cdot (\nabla \times \mathbf v) + \mathbf v \cdot (\nabla \times \mathbf u) \end{aligned}$$
    - del / properties / product rules (harder) ::@:: These 2 rules are the harder ones: $$\begin{aligned} \nabla (\mathbf u \cdot \mathbf v) & = \mathbf u \times (\nabla \times \mathbf v) + (\mathbf u \cdot \nabla) \mathbf v + \mathbf v \times (\nabla \times \mathbf u) + (\mathbf v \cdot \nabla)\mathbf u \\ \nabla \times (\mathbf u \times \mathbf v) & = \mathbf u \, (\nabla \cdot \mathbf v) - (\mathbf u \cdot \nabla) \, \mathbf v - \mathbf v \, (\nabla \cdot \mathbf u) + (\mathbf v \cdot \nabla) \, \mathbf u \end{aligned}$$

## final examination

## aftermath

### total
