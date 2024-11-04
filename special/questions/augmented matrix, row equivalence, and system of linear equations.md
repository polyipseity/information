---
aliases:
  - augmented matrix, row equivalence, and system of linear equations
tags:
  - date/2024/09/08
  - flashcard/active/special/questions/augmented_matrix__system_of_linear_equations__and_row_equivalence
  - language/in/English
  - question/mathematics/linear_algebra
---

# augmented matrix, row equivalence, and system of linear equations

- datetime: 2024-09-08T18:33:38+08:00

Here, we define a __system of linear equation__ to have at least 2 equations and 1 variable.

Suppose we have two __systems of linear equation__ with the same number of equations and the same number of variables. Then their augmented matrices have the same size. If the two augmented matrices are __row equivalent__, then the systems are equivalent, i.e. they have the same set of solution. However, the converse,  i.e. equivalent systems have row equivalent augmented matrices, is not true. Under a mild condition, the converse can become true. Find the mild condition by trying to prove the converse, and give an counterexample to the converse when the mild condition is not satisfied.

Note: The above still applies even if there are less than 2 equations and 1 variable. In particular, this still applies if there are no variables. This also applies if there are no equations, because there is only one unique "system" of linear equations with an unconstrained solution set.

## strategy

- Is the converse, equivalent systems have row equivalent augmented matrices true? ::: Intuitively, this is true... But actually this is false. So intuition does not work well if the question is asking if a general statement is correct. (This happened while designing this question, causing the question to be changed into this weird form.) <!--SR:!2024-11-09,44,290!2025-02-15,114,290-->
- manipulating augmented matrices ::: Treat augmented matrices as normal matrices, and see what you can do with it... <!--SR:!2025-01-18,92,290!2024-11-05,41,290-->
- proving the row equivalence of two matrices ::: If the (right) nullspaces of two matrices are equal, then their row spaces are equal as they are orthogonal complements of the nullspaces. Then, the matrices are row equivalent, because elementary row operations can generate all other bases in the row space given one basis. <!--SR:!2024-12-04,65,310!2024-12-07,67,310-->

## solution

Consider a system of linear equation of $m \ge 2$ equations and $n \ge 1$ variables:

$$\left\{ \begin{aligned}
& a_{1, 1} x_1 && + a_{1, 2} x_2 && + \cdots && + a_{1, n} x_n && = b_1    \\
& a_{2, 1} x_1 && + a_{2, 2} x_2 && + \cdots && + a_{2, n} x_n && = b_2    \\
& \vdots       && + \vdots       && + \ddots && + \vdots       && = \vdots \\
& a_{m, 1} x_1 && + a_{m, 2} x_2 && + \cdots && + a_{m, n} x_n && = b_m    \\
\end{aligned} \right.$$

Its augmented matrix is:

$$\begin{bmatrix}
a_{1, 1}                          & a_{1, 2}                          & \cdots                            & a_{1, n}                          & \bigm | & b_1                               \\
a_{2, 1}                          & a_{2, 2}                          & \cdots                            & a_{2, n}                          & \bigm | & b_2                               \\
\vphantom 0 \smash{\small \vdots} & \vphantom 0 \smash{\small \vdots} & \vphantom 0 \smash{\small \ddots} & \vphantom 0 \smash{\small \vdots} & \bigm | & \vphantom 0 \smash{\small \vdots} \\
a_{m, 1}                          & a_{m, 2}                          & \cdots                            & a_{m, n}                          & \bigm | & b_m                               \\
\end{bmatrix}$$

Treat the augmented matrix as a normal matrix. Then, we can write the solutions of the linear equation as:

$$\begin{bmatrix}
a_{1, 1} & a_{1, 2} & \cdots & a_{1, n} & b_1    \\
a_{2, 1} & a_{1, 2} & \cdots & a_{1, n} & b_2    \\
\vdots   & \vdots   & \ddots & \vdots   & \vdots \\
a_{m, 1} & a_{m, 2} & \cdots & a_{m, n} & b_m    \\
\end{bmatrix} \begin{bmatrix}
x_1    \\
x_2    \\
\vdots \\
x_n    \\
c      \\
\end{bmatrix} = \begin{bmatrix}
0      \\
0      \\
\vdots \\
0      \\
\end{bmatrix} \qquad c \in \mathbb R$$

Now consider two equivalent systems of linear equations. They have the same solution set. Rewrite the two systems into the above form. We want to prove that the (right) nullspace of the corresponding augmented matrix, treated as a normal matrix, are the same for two systems. Consider 3 cases: $c = -1$, $c \notin \set{0, -1}$, and $c = 0$.

When $c = -1$, the above form directly corresponds to the two systems. So both systems have the same set of solution vectors for the above form.

When $c \notin \set{0, -1}$, the above form corresponds to scaled versions of the two systems (the $b_k$ are scaled). So both systems still have the same set of solution vectors for the above form.

When $c = 0$, the above form corresponds to the corresponding homogeneous systems of the two systems. We need to consider 3 cases: both systems are originally homogeneous, one system is homogeneous and the other is inhomogeneous, and both systems are originally inhomogeneous.

If the two systems are originally both homogeneous, then equality is trivial.

It is impossible for a homogeneous system and an inhomogeneous one to be equivalent, so we do not need to consider this case. This is because a homogeneous system must have the zero solution while an inhomogeneous one must not.

If the two systems are originally both inhomogeneous, equality cannot be proved, so we need to introduce a mild condition. (This was the problem encountered while trying to prove the converse is true, which is not.) The mild condition is that __the two original systems of linear equations are consistent, or equivalently, have a _nonempty_ set of solution__. Then, we can prove it: Assume there exists two equivalent inhomogeneous systems, but their corresponding homogeneous systems are not equivalent. Then we can take any solution A from the _nonempty_ set of solution for the two equivalent inhomogeneous systems. Then also take a solution B that is a solution to one of the homogeneous system but not the other (this must exist because a homogeneous system must have the zero solution). Add the inhomogeneous solution A and the homogeneous solution B together to produce a new solution C for the two equivalent inhomogeneous systems. This creates a contradiction. The solution C could not have been a solution for both inhomogeneous systems, otherwise their corresponding homogeneous systems would have had the solution B. So we conclude that their corresponding homogeneous systems are also equivalent.

This proves that the (right) nullspace of the augmented matrix, treated as a normal matrix, are the same for two equivalent systems, under the mild condition that the systems are consistent. Then, this implies the row space of the augmented matrix are the same for both, since the row space is the (unique) orthogonal complement of the nullspace. Finally, since elementary row operations can generate all other bases of a row space from one basis, the augmented matrices are row equivalent. Q.E.D.

As for the counterexample, consider two inconsistent (and thus inhomogeneous) systems. They are equivalent as they have an empty solution set. Then, make the row spaces of the two systems different. A counterexample is:

$$\left\{ \begin{aligned}
& x && =  1 \\
& x && = -1 \\
\end{aligned} \right.
\qquad \text{ and } \qquad
\left\{ \begin{aligned}
& 0x && =  1 \\
& 0x && = -1 \\
\end{aligned} \right.$$

(See this for a different solution: [Arturo Magidin](https://math.stackexchange.com/a/111916), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), via Mathematics Stack Exchange.)
