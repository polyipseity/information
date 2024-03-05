---
aliases:
  - HKUST CIVL 1100 assignment I.1 submission
tags:
  - language/in/English
---

# HKUST CIVL 1100 assignment I.1 submission

CIVL 1100 Discovering Civil and Environmental Engineering

__Assignment I-1__: Civil and Structural Engineering 1

- Assigned: 20 February 2024 (Tue)
- Due date: <u>27 February 2024 (Tue) 11:59 pm</u>

1. NOTE 1. Submit your completed assignment online to Canvas. Submit your work in a <u>PDF</u> file. Late submission will not be accepted.
2. NOTE 2. Show your work with steps <u>clearly</u>. When appropriate, illustrate your work with diagrams and/or figures and write down any assumptions you made.
3. NOTE 3. Use the sign conventions taught in lectures. Take _g_ = 9.81 m/s<sup>2</sup> when necessary.

> Take up, right, and counterclockwise as positive, as taught in lectures.

## 1.1

A structural beam AC, supported as shown, is under an applied load of 3.5 kN. Point A is a pin support. Points B and C are connected with a cable, hanging over a smooth pulley. Neglect the self-weight of the beam. Determine the tension force in the cable and reactions at the support A.

![figure 1.1](attachments/Pasted%20image%2020240227230712.png)

> Let $T$ be the tension force in the cable. Let $R$ be the reaction at the support A. Let $\tau_\text{A}$ be the moment of the beam about A.
>
> $$\begin{aligned}
> \tau_\text{A} & = 0.75 T - (0.75 + 0.75) 3\,500 + (0.75 + 0.75 + 0.75) T \sin 30 \degree \\
> 0 & = 1.875 T - 5\,250 \\
> T & = 2\,800 \text{ N} \\
> \\
> F_{\text{net}} & = (R_x - T \cos 30 \degree, R_y + T + T \sin 30 \degree - 3\,500) \\
> (0, 0) & = \left( R_x - \frac {\sqrt 3} 2 T, R_y + \frac 3 2 T - 3\,500 \right) \\
> & = (R_x - 1\,400 \sqrt 3, R_y + 700) \\
> (R_x, R_y) & = \left( 1\,400 \sqrt 3 \text{ N}, -700 \text{ N} \right) \\
> \\
> (T, R_x, R_y) & = \left( 2\,800 \text{ N}, 1\,400 \sqrt 3 \text{ N}, -700 \text{ N} \right) \\
> & = (2\,800 \text{ N}, 2\,424.87 \text{ N (cor. to 6 sig. fig.)}, -700 \text{ N})
> \end{aligned}$$

## 1.2

A structural beam ABC is supported by a pin support at A and a roller support at B. Determine the reactions at these two supports under the two applied loads (100 kN and 200 kN) as shown in the figure.

If the roller support is moved from point B to point D which is at the middle of span AB, determine the support reactions again? Describe how the support reactions will change when the roller support moves from point B towards point A.

![figure 1.2](attachments/Pasted%20image%2020240227230747.png)

> Let $R_\text{A}$ be the reaction at the support A. Let $R_\text{B}$ be the reaction at the support B. Let $\tau_\text{B}$ be the moment of the beam about B.
>
> $$\begin{aligned}
> \tau_\text{B} & = 1 \cdot 200\,000 \cos 30 \degree + 3 \cdot 100\,000 - (3 + 1) R_{\text{A}, y} \\
> 0 & = 100\,000 \sqrt 3 + 300\,000 - 4 R_{\text{A}, y} \\
> R_{\text{A}, y} & = \left(25\,000 \sqrt 3 + 75\,000\right) \text{ N} \\
> \\
> F_\text{net} & = (R_{\text{A}, x} - 200\,000 \cos 30 \degree, R_{\text{A}, y} + R_\text{B} - 100\,000 - 200\,000 \sin 30 \degree) \\
> (0, 0) & = (R_{\text{A}, x} - 100\,000 \sqrt 3, R_{\text{A}, y} + R_\text{B} - 200\,000) \\
> & = \left( R_{\text{A}, x} - 100\,000 \sqrt 3, \left(25\,000 \sqrt 3 + 75\,000\right) + R_\text{B} - 200\,000 \right) \\
> & = \left( R_{\text{A}, x} - 100\,000 \sqrt 3, R_\text{B} - 125\,000 + 25\,000 \sqrt 3 \right) \\
> (R_{\text{A}, x}, R_\text{B}) & = \left(100\,000 \sqrt 3 \text{ N}, \left( 125\,000 - 25\,000 \sqrt 3 \right) \text{ N} \right) \\
> \\
> (R_{\text{A}, x}, R_{\text{A}, y}, R_\text{B}) & = \left(100\,000 \sqrt 3 \text{ N}, \left(25\,000 \sqrt 3 + 75\,000\right) \text{ N}, \left( 125\,000 - 25\,000 \sqrt 3 \right) \text{ N} \right) \\
> & = (173\,205 \text{ N (cor. to 6 sig. fig.)}, 118\,301 \text{ N (cor. to 6 sig. fig.)}, 81698.7 \text{ N (cor. to 6 sig. fig.)})
> \end{aligned}$$
>
> If the roller support is moved from point B to point D... Let $R_\text{D}$ be the reaction at the support D.
>
> $$\begin{aligned}
> \tau_\text{B} & = 1 \cdot 200\,000 \cos 30 \degree + 3 \cdot 100\,000 - (3 + 1) R_{\text{A}, y} - 2 R_{\text{D}} \\
> 0 & = 100\,000 \sqrt 3 + 300\,000 - 4 R_{\text{A}, y} - 2 R_{\text{D}} \\
> 2 R_{\text{A}, y} + R_{\text{D}} & = \left(50\,000 \sqrt 3 + 150\,000\right) \text{ N} \\
> \\
> F_\text{net} & = (R_{\text{A}, x} - 200\,000 \cos 30 \degree, R_{\text{A}, y} + R_\text{D} - 100\,000 - 200\,000 \sin 30 \degree) \\
> (0, 0) & = (R_{\text{A}, x} - 100\,000 \sqrt 3, R_{\text{A}, y} + R_\text{D} - 200\,000) \\
> & = \left( R_{\text{A}, x} - 100\,000 \sqrt 3, \left(50\,000 \sqrt 3 + 150\,000\right) - R_{\text{A}, y} - 200\,000 \right) \\
> & = \left( R_{\text{A}, x} - 100\,000 \sqrt 3, -R_{\text{A}, y} - 50\,000 + 50\,000 \sqrt 3 \right) \\
> (R_{\text{A}, x}, R_{\text{A}, y}) & = \left(100\,000 \sqrt 3 \text{ N}, \left( 50\,000 \sqrt 3 - 50\,000 \right) \text{ N} \right) \\
> \\
> 2 R_{\text{A}, y} + R_{\text{D}} & = 50\,000 \sqrt 3 + 150\,000 \\
> R_{\text{D}} & = \left(-50\,000 \sqrt 3 + 250\,000\right) \text{ N} \\
> \\
> (R_{\text{A}, x}, R_{\text{A}, y}, R_\text{D}) & = \left(100\,000 \sqrt 3 \text{ N}, \left( 50\,000 \sqrt 3 - 50\,000 \right) \text{ N}, \left(-50\,000 \sqrt 3 + 250\,000\right) \text{ N} \right) \\
> & = (173\,205 \text{ N (cor. to 6 sig. fig.)}, 36\,602.5 \text{ N (cor. to 6 sig. fig.)}, 163\,397 \text{ N (cor. to 6 sig. fig.)})
> \end{aligned}$$
>
> From above, we can deduce that as the roller support moves from point B towards point A, the pin support reaction remains the same in the $x$-axis and decreases in the $y$-axis (becomes more downwards), while the roller reaction increases (becomes more upward).
