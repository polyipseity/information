---
aliases:
  - HKUST CIVL 1100 assignment I.2 submission
tags:
  - language/in/English
---

# HKUST CIVL 1100 assignment I.2 submission

CIVL 1100 Discovering Civil and Environmental Engineering

__Assignment I-2__: Civil and Structural Engineering II

- Assigned: 27 February 2024 (Tue)
- Due date: <u>5 March 2024 (Tue) 11:59 pm</u>

1. NOTE 1. Submit your completed assignment online to Canvas. Submit your work in a <u>PDF</u> file. Late submission will not be accepted.
2. NOTE 2. Show your work with steps <u>clearly</u>. When appropriate, illustrate your work with diagrams and/or figures and write down any assumptions you made.
3. NOTE 3. Use the sign conventions taught in lectures. Take _g_ = 9.81 m/s<sup>2</sup> when necessary.

## 2.1

Use the method of joints to determine the axial forces in all members of the truss structure in Fig. 2.1, under the two applied loads as shown.

![figure 2.1](attachments/Pasted%20image%2020240305142548.png)

Fig. 2.1

At the end of calculation, summarize the forces in the members in a table like this one:

| Member | Force (kN) | Member | Force (kN) |
|:------:|:----------:|:------:|:----------:|
| _AB_   |            | _AG_   |            |
| _BC_   |            | _AF_   |            |
| _CD_   |            | _BF_   |            |
| _DE_   |            | _BE_   |            |
| _EF_   |            | _CE_   |            |
| _FG_   |            |        |            |

> Take up for vertical forces, right for horizontal forces, counterclockwise for moments, and tension as positive. Take down for vertical forces, left for horizontal forces, clockwise for moments, and compression as negative.
>
> Let $A = (0\text{ N}, A_y)$ be the reaction at the roller support. Let $C = (C_x, C_y)$ be the reaction at the pin support. Let $\tau_A$ be the moment about the roller support. Let $T_{XY}$ be the tensile force between joint $X$ and $Y$.
>
> Treating the truss structure as a rigid body:
>
> $$\begin{aligned}
> F_{\text{net}, x} & = 25\,000 + C_x \\
> 0 & = 25\,000 + C_x \\
> C_x & = -25\,000\text{ N} \\
> \\
> \tau_A & = -3 (25\,000) - 3 (75\,000) + 6 C_y \\
> 0 & = -300\,000 + 6 C_y \\
> C_y & = 50\,000\text{ N} \\
> \\
> F_{\text{net}, y} & = -75\,000 + A_y + C_y \\
> 0 & = -75\,000 + A_y + 50\,000 \\
> A_y & = 25\,000\text{ N} \\
> \\
> (A_y, C_x, C_y) & = (25\,000\text{ N}, -25\,000\text{ N}, 50\,000\text{ N}) \\
> \end{aligned}$$
>
> Assume forces in all members are tension, so take tension as positive. Now we draw a table of known and unknown forces of each joint:
>
> | forces\joints | A | B | C | D | E | F | G |
> |---------------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | known         | 1 | 0 | 2 | 0 | 0 | 1 | 1 |
> | unknown       | 3 | 4 | 3 | 2 | 4 | 4 | 2 |
>
> Solve for forces in the joints with 2 or less unknown forces, and then solve for forces in the new joints with 2 or less unknown forces, and so forth, until all forces in all joints are determined:
>
> $$\begin{aligned}
> \text{For joint }D \\
> (F_{\text{net}, x}, F_{\text{net}, y}) & = (-F_{DE} - F_{CD} \cos 45 \degree, -F_{CD} \sin 45 \degree) \\
> (0, 0) & = (-F_{DE} - F_{CD} \cos 45 \degree, -F_{CD} \sin 45 \degree) \\
> (0, F_{CD}) & = (-F_{DE} - F_{CD} \cos 45 \degree, 0) \\
> & = (-F_{DE}, 0) \\
> (F_{DE}, F_{CD}) & = (0\text{ N}, 0\text{ N}) \\
> & = (0\text{ kN}, 0\text{ kN}) \\
> \\
> \text{For joint }C \\
> (F_{\text{net}, x}, F_{\text{net}, y}) & = (C_x - F_{BC} + F_{CD} \cos 45 \degree, C_y + F_{CE} + F_{CD} \sin 45 \degree) \\
> (0, 0) & = (-25\,000 - F_{BC}, 50\,000 + F_{CE}) \\
> (F_{BC}, F_{CE}) & = (-25\,000\text{ N}, -50\,000\text{ N}) \\
> & = (-25\text{ kN}, -50\text{ kN}) \\
> \\
> \text{For joint }E \\
> (F_{\text{net}, x}, F_{\text{net}, y}) & = (-F_{EF} - F_{BE} \cos 45 \degree + F_{DE}, -F_{BE} \sin 45 \degree - F_{CE}) \\
> (0, 0) & = (-F_{EF} - F_{BE} \cos 45 \degree, -F_{BE} \sin 45 \degree + 50\,000) \\
> (0, F_{BE}) & = (-F_{EF} - F_{BE} \cos 45 \degree, 50\,000 \sqrt 2) \\
> & = (-F_{EF} - 50\,000, 50\,000 \sqrt 2) \\
> (F_{EF}, F_{BE}) & = (-50\,000\text{ N}, 50\,000 \sqrt 2\text{ N}) \\
> & \approx (-50\text{ kN}, 70.7\text{ kN}) \\
> \\
> \text{For joint }B \\
> (F_{\text{net}, x}, F_{\text{net}, y}) & = (-F_{AB} + F_{BE} \cos 45 \degree + F_{BC}, F_{BF} + F_{BE} \sin 45 \degree) \\
> (0, 0) & = (-F_{AB} + 50\,000 - 25\,000, F_{BF} + 50\,000) \\
> (F_{AB}, F_{BF}) & = (25\,000\text{ N}, -50\,000\text{ N}) \\
> & = (25\text{ kN}, -50\text{ kN}) \\
> \\
> \text{For joint }F \\
> (F_{\text{net}, x}, F_{\text{net}, y}) & = (-F_{FG} - F_{AF} \cos 45 \degree + F_{EF}, -75\,000 - F_{AF} \sin 45 \degree - F_{BF}) \\
> (0, 0) & = (-F_{FG} - F_{AF} \cos 45 \degree - 50\,000, -75\,000 - F_{AF} \sin 45 \degree + 50\,000) \\
> (0, F_{AF}) & = (-F_{FG} - F_{AF} \cos 45 \degree - 50\,000, -25\,000 \sqrt 2) \\
> & = (-F_{FG} + 25\,000 - 50\,000, -25\,000 \sqrt 2) \\
> (F_{FG}, F_{AF}) & = (-25\,000\text{ N}, -25\,000 \sqrt 2\text{ N}) \\
> & \approx (-25\text{ kN}, -35.4\text{ kN}) \\
> \\
> \text{For joint }A \\
> (F_{\text{net}, x}, F_{\text{net}, y}) & = (F_{AF} \cos 45 \degree + F_{AB}, A_y + F_{AG} + F_{AF} \sin 45 \degree) \\
> (0, 0) & = (-25\,000 + 25\,000, 25\,000 + F_{AG} - 25\,000) \\
> (0, F_{AG}) & = (0, 0) \\
> F_{AG} & = 0\text{ N} \\
> & = 0\text{ kN} \\
> \\
> \text{For joint }G\text{ as validation} \\
> (F_{\text{net}, x}, F_{\text{net}, y}) & = (25\,000 + F_{FG}, -F_{AG}) \\
> & = (25\,000 - 25\,000, 0) \\
> & = (0\text{ N}, 0\text{ N})
> \end{aligned}$$
>
> Hence the table of forces, with tension in the members as positive:
>
> | Member | Force (kN) | Member | Force (kN) |
> |:------:|:----------:|:------:|:----------:|
> | _AB_   | 25         | _AG_   | 0          |
> | _BC_   | -25        | _AF_   | -35.4      |
> | _CD_   | 0          | _BF_   | -50        |
> | _DE_   | 0          | _BE_   | 70.7       |
> | _EF_   | -50        | _CE_   | -50        |
> | _FG_   | -25        |        |            |

## 2.2

Determine all support reactions for the three-hinged arch shown in Fig. 2.2.

![figure 2.2](attachments/Pasted%20image%2020240305142613.png)

Fig. 2.2

> Take up for vertical forces, right for horizontal forces, counterclockwise for moments, and tension as positive. Take down for vertical forces, left for horizontal forces, clockwise for moments, and compression as negative.
>
> Let $L = (L_x, L_y)$ and $\tau_L$ respectively be the reaction and moment at the left hinge. Let $R = (R_x, R_y)$ and $\tau_R$ respectively be the reaction and moment at the right hinge. Let $\tau_M$ be the moment at the middle hinge.
>
> Now, find the vertical reactions at the left and right support by considering the entire arch as a rigid body:
>
> $$\begin{aligned}
> \tau_L & = -2(300\,000) - 4(200\,000) - 5(150\,000) + 8 R_y \\
> 0 & = -2\,150\,000 + 8 R_y \\
> R_y & = 268\,750\text{ N} \\
> \\
> \tau_R & = -8 L_y + 6(300\,000) + 4(200\,000) + 3(150\,000) \\
> 0 & = -8 L_y + 3\,050\,000 \\
> L_y & = 381\,250\text{ N}
> \end{aligned}$$
>
> Now, find the horizontal reactions at the left and right support by consider the left arch and the right arch separaetly as two rigid bodies:
>
> $$\begin{aligned}
> & \text{Consider the left arch as a rigid body} \\
> \tau_M & = 2(300\,000) - 4 L_y + 3 L_x \\
> 0 & = 600\,000 - 1\,525\,000 + 3 L_x \\
> L_x & = \frac {925\,000} 3\text{ N} \\
> & = 308\,333\text{ N (cor. to 6 sig. fig.)} \\
> \\
> & \text{Consider the right arch as a rigid body} \\
> \tau_M & = -1(150\,000) + 4 R_y + 3 R_x \\
> 0 & = -150\,000 + 1\,075\,000 + 3 R_x \\
> R_x & = -\frac {925\,000} 3\text{ N} \\
> & = -308\,333\text{ N (cor. to 6 sig. fig.)}
> \end{aligned}$$
>
> We can validate the answer by checking whether the net force for the entire arch is zero:
>
> $$\begin{aligned}
> (F_{\text{net}, x}, F_{\text{net}, y}) & = \left( \frac {925\,000} 3 - \frac {925\,000} 3, 268\,750 + 381\,250 - 300\,000 - 200\,000 - 150\,000 \right) \\
> & = (0\text{ N}, 0\text{ N})
> \end{aligned}$$
>
> Hence, the answer is:
>
> $$(L_x, L_y, R_x, R_y) = (308\,333\text{ N (cor. to 6 sig. fig.)}, 381\,250\text{ N}, -308\,333\text{ N (cor. to 6 sig. fig.)}, 268\,750\text{ N})$$
