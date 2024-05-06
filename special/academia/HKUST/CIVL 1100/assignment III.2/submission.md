---
aliases:
  - HKUST CIVL 1100 assignment III.2 submission
tags:
  - date/2024/04/30/from
  - date/2024/05/01/to
  - language/in/English
---

# HKUST CIVL 1100 assignment III.2 submission

CIVL1100 Discovering Civil and Environmental Engineering

<!-- markdownlint-disable-next-line MD036 -->
__Assignment 6: Geotechnical Engineering II__

Assigned date: 29 Apr 2023; Due date: 6 May 2023, 23:59 pm

- Note 1. Submit your assignment electronically via CANVAS
- Note 2. Show your homework clearly. When appropriate, illustrate your work with diagrams, and/or figures.

---

## 6.1

A long sandy slope has a slope angle of 30°. The effective friction angle of the sand is 36° and the effective cohesion is zero. The saturated unit weight of the sand is γ<sub>sat</sub> = 19.8 kN/m<sup>3</sup>.

### 6.1.a

Evaluate the stability of the slope when it is dry.

> Assuming the slope is an infinite slope.
>
> <!-- $$\begin{aligned}
> \text{shear strength} & = c' + (\sigma_n - u_w) \tan \phi' \\
> & = 0 + (W_j \cos 30\degree - 0) \tan 36\degree && (W_j' = W_j) \\
> & = W_j \cos 30\degree \tan 36\degree\text{ N} \\
> \text{mobilized shear stress} & = W_j \sin 30\degree\text{ N} \\
> \text{factor of safety} & = \frac {\text{shear strength} } {\text{mobilized shear stress} } \\
> & = \frac {W_j \cos 30\degree \tan 36\degree} {W_j \sin 30\degree} \\
> & = \frac {\tan 36\degree} {\tan 30\degree} \\
> & = 1.25840857\text{ (cor to 9 sig. fig.)} \\
> & = 1.26\text{ (cor to 3 sig. fig.)} \\
> $$\end{aligned} -->
>
> $$\begin{aligned}
> \text{factor of safety} & = \frac {\tan \phi'} {\tan \alpha_\text{s} } \\
> & = \frac {\tan 36\degree} {\tan 30\degree} \\
> & = 1.25840857\text{ (cor to 9 sig. fig.)} \\
> & = 1.26\text{ (cor to 3 sig. fig.)} \\
> \\
> & \because \text{factor of safety} = 1.26 > 1 \\
> & \therefore \text{The slope is stable.}
> \end{aligned}$$

### 6.1.b

Evaluate the stability of the slope when the groundwater table is at the ground surface.

> $$\begin{aligned}
> \text{factor of safety} & = \frac {\gamma'} {\gamma_\text{sat} } \frac {\tan \phi'} {\tan \alpha_\text{s} } \\
> & = \frac {19.8 - 9.8} {19.8} \frac {\tan 36\degree} {\tan 30\degree} \\
> & = 0.635559885\text{ (cor to 9 sig. fig.)} \\
> & = 0.636\text{ (cor to 3 sig. fig.)} \\
> \\
> & \because \text{factor of safety} = 0.636 < 1 \\
> & \therefore \text{The slope is unstable.}
> \end{aligned}$$

### 6.1.c

List three key assumptions made in the infinite slope safety calculation method. State whether each of the assumptions would lead to a safe or unsafe design.

> The three assumptions are:
>
> - The slope has infinite length. The assumption would lead to an unsafe design. This is because an actual slope has edges (eventually ends), which introduces additional unconsidered edge effects that affect the slope safety.
> - The slip plane is parallel to the slope. The assumption would lead to a unsafe design. This is because actual sliding angle may be steeper or gentler, affecting the slope safety.
> - The effective cohesion is 0 Pa. The assumption would lead to a safe design. This is because the minimum cohesion of an actual slope is 0 Pa.

## 6.2

Which of the following regarding landslide risk is __<u>NOT TRUE</u>__?

- A. Frequent inspections of slopes do not decrease landslide risk
- B. Improving the stability of existing slopes reduces the probability of slope failure
- C. Implementing high technical standards reduces probability of slope failure
- D. Good land uses reduce risks by minimizing the possible consequences of potential landslides

> A

## 6.3

Hong Kong has a large number of slopes that require stabilisation. Which were the measures taken in the Landslip Prevention Programme to minimise the landslide risk?

- i. evaluated the risks of the slopes to be stabilised
- ii. prioritised the slopes in terms of their risks
- iii. depending on fund available, upgraded several hundreds of slopes per year
- iv. implemented a slope maintenance plan

Which of the following options is __<u>CORRECT</u>__?

- A. i and ii
- B. i and iii
- C. i, ii and iii
- D. all

> D
