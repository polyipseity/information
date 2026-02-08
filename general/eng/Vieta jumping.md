---
aliases:
  - Vieta jumping
  - constant descent Vieta jumping
  - root flipping
  - standard Vieta jumping
tags:
  - flashcard/active/general/eng/Vieta_jumping
  - language/in/English
---

# Vieta jumping

In {@{[number theory](number%20theory.md)}@}, {@{__Vieta jumping__, also known as __root flipping__}@}, is {@{a [proof technique](mathematical%20proof.md)}@}. It is most often used for problems in which {@{a relation between two integers is given, along with a statement to prove about its solutions}@}. In particular, it can be used to produce {@{new solutions of a [quadratic](quadratic%20equation.md) [Diophantine equation](Diophantine%20equation.md) from known ones}@}. There exist multiple {@{variations of Vieta jumping}@}, all of which involve {@{the common theme of [infinite descent](infinite%20descent.md)}@} by finding {@{new solutions to an equation using [Vieta's formulas](Vieta's%20formulas.md)}@}. <!--SR:!2026-04-06,58,310!2026-04-03,55,310!2026-04-12,63,310!2026-02-09,16,290!2026-04-04,56,310!2026-04-06,57,310!2026-02-09,16,290!2026-02-09,16,290-->

## history

Vieta jumping is {@{a classical method}@} in the theory of {@{quadratic [Diophantine equations](Diophantine%20equations.md) and [binary quadratic forms](binary%20quadratic%20form.md)}@}. For example, it was used in the analysis of {@{the [Markov equation](Markov%20equation.md) back in 1879 and in the 1953 paper of Mills}@}.<sup>[\[1\]](#^ref-1)</sup>
In {@{1988, the method came to the attention to [mathematical olympiad](mathematical%20olympiad.md) problems}@} in the light of {@{the first olympiad problem to use it in a solution that was proposed for the [International Mathematics Olympiad](International%20Mathematics%20Olympiad.md)}@} and assumed to be {@{the most difficult problem on the contest}@}:<sup>[\[2\]](#^ref-2)</sup><sup>[\[3\]](#^ref-3)</sup> <!--SR:!2026-04-02,54,310!2026-04-03,55,310!2026-04-09,60,310!2026-02-09,16,290!2026-02-09,16,290!2026-02-09,16,290-->

&emsp; Let _a_ and _b_ be {@{positive integers such that _ab_ + 1 divides _a_<sup>2</sup> + _b_<sup>2</sup>}@}. Show that {@{${\frac {a^{2}+b^{2} }{ab+1} }$ is the square of an integer}@}.<sup>[\[4\]](#^ref-4)</sup> <!--SR:!2026-02-09,16,290!2026-02-09,16,290-->

{@{[Arthur Engel](Arthur%20Engel%20(mathematician).md)}@} wrote the following about {@{the problem's difficulty}@}: <!--SR:!2026-04-04,56,310!2026-04-02,54,310-->

&emsp; {@{Nobody of the six members of the Australian problem committee}@} could {@{solve it}@}. {@{Two of the members}@} were {@{husband and wife [George](George%20Szekeres.md) and [Esther Szekeres](Esther%20Szekeres.md)}@}, both {@{famous problem solvers and problem creators}@}. Since it was {@{a number theoretic problem}@} it was sent to {@{the four most renowned Australian number theorists}@}. They were asked to {@{work on it for six hours}@}. {@{None of them}@} could {@{solve it in this time}@}. {@{The problem committee}@} submitted it to {@{the jury of the XXIX IMO marked with a double asterisk}@}, which meant {@{a superhard problem, possibly too hard to pose}@}. After {@{a long discussion}@}, the jury finally had {@{the courage to choose it as the last problem of the competition}@}. {@{Eleven students}@} gave {@{perfect solutions}@}. <!--SR:!2026-04-03,55,310!2026-04-12,63,310!2026-04-11,62,310!2026-04-05,57,310!2026-02-09,16,290!2026-04-06,57,310!2026-04-02,54,310!2026-04-02,54,310!2026-02-09,16,290!2026-04-02,54,310!2026-02-09,16,290!2026-04-03,55,310!2026-04-10,61,310!2026-02-09,16,290!2026-04-12,63,310!2026-02-09,16,290!2026-02-09,16,290-->

Among {@{the eleven students receiving the maximum score for solving this problem}@} were {@{[Ngô Bảo Châu](Ngô%20Bảo%20Châu.md), [Ravi Vakil](Ravi%20Vakil.md), [Zvezdelina Stankova](Zvezdelina%20Stankova.md), and [Nicușor Dan](Nicușor%20Dan.md)}@}.<sup>[\[5\]](#^ref-5)</sup> {@{Emanouil Atanassov \(from Bulgaria\)}@} solved {@{the problem in a paragraph and received a special prize}@}.<sup>[\[6\]](#^ref-6)</sup> <!--SR:!2026-02-09,16,290!2026-04-12,63,310!2026-04-02,54,310!2026-02-09,16,290-->

## standard Vieta jumping

The concept of {@{__standard Vieta jumping__}@} is {@{a [proof by contradiction](proof%20by%20contradiction.md), and consists of the following four steps}@}:<sup>[\[7\]](#^ref-7)</sup> (annotation: 4 steps: {@{assumption → minimality → substitution → contradiction}@}) <!--SR:!2026-04-12,63,310!2026-04-03,55,310!2026-02-09,16,290-->

1. (annotation: assumption) ::@:: Assume toward a contradiction that some solution \(_a_<sub>1</sub>, _a_<sub>2</sub>, ...\) exists that violates the given requirements. <!--SR:!2026-04-11,62,310!2026-04-08,59,310-->
2. (annotation: minimality) ::@:: Take the minimal such solution according to some definition of minimality. <!--SR:!2026-04-12,63,310!2026-04-04,56,310-->
3. (annotation: substitution) ::@:: Replace some _a_<sub>i</sub> by a variable _x_ in the formulas, and obtain an equation for which _a_<sub>i</sub> is a solution. <!--SR:!2026-04-07,58,310!2026-02-09,16,290-->
4. (annotation: contradiction) ::@:: Using Vieta's formulas, show that this implies the existence of a smaller solution, hence a contradiction. <!--SR:!2026-04-03,55,310!2026-02-09,16,290-->

__Example__

{@{__Problem \#6 at IMO 1988__}@}: Let _a_ and _b_ be {@{positive integers such that _ab_ + 1 divides _a_<sup>2</sup> + _b_<sup>2</sup>}@}. Prove that {@{$\frac {a^2 + b^2} {ab + 1}$⁠ is a [perfect square](square%20number.md)}@}.<sup>[\[8\]](#^ref-8)</sup><sup>[\[9\]](#^ref-9)</sup> <!--SR:!2026-04-02,54,310!2026-04-03,55,310!2026-02-09,16,290-->

1. Fix some value _k_ that is {@{a non-square positive integer}@}. Assume there exist {@{positive integers \(_a_, _b_\) for which $k = \frac {a^2 + b^2} {ab + 1}$}@}.
2. Let \(_A_, _B_\) be {@{positive integers for which $k = \frac {A^2 + B^2} {AB + 1}$}@} and such that {@{_A_ + _B_ is minimized}@}, and {@{[without loss of generality](without%20loss%20of%20generality.md) assume _A_ ≥ _B_}@}.
3. Fixing {@{_B_}@}, replace {@{_A_ with the variable _x_}@} to yield {@{_x_<sup>2</sup> – \(_kB_\)_x_ + \(_B_<sup>2</sup> – _k_\) = 0}@}. We know that {@{one root of this equation is _x_<sub>1</sub> = _A_}@}. By {@{standard properties of quadratic equations}@}, we know that {@{the other root}@} satisfies {@{_x_<sub>2</sub> = _kB_ – _A_ and $x_2 = \frac {B^2 - k} {A}$}@}.
4. The first expression for _x_<sub>2</sub> shows that {@{_x_<sub>2</sub> is an integer}@}, while the second expression implies that {@{_x_<sub>2</sub> ≠ 0 since _k_ is not a perfect square}@}. From {@{$\frac {x_2^2 + B^2} {x_2 B + 1} = k > 0$}@} it further follows that {@{_x_<sub>2</sub>_B_ \> −1}@}, and hence {@{_x_<sub>2</sub> is a positive integer}@}. Finally, {@{_A_ ≥ _B_}@} implies that $x_2 = \frac {B^2 - k} {A} < \frac {B^2} {A} \le A$, hence {@{_x_<sub>2</sub> \< _A_}@}, and thus {@{_x_<sub>2</sub> + _B_ \< _A_ + _B_}@}, which {@{contradicts the minimality of _A_ + _B_}@}. <!--SR:!2026-04-03,55,310!2026-02-09,16,290!2026-02-09,16,290!2026-02-09,16,290!2026-04-03,55,310!2026-02-09,16,290!2026-02-09,16,290!2026-04-09,60,310!2026-02-09,16,290!2026-04-12,63,310!2026-03-20,41,290!2026-02-09,16,290!2026-04-03,55,310!2026-04-02,54,310!2026-03-05,29,270!2026-04-02,54,310!2026-03-19,40,290!2026-04-10,61,310!2026-04-02,54,310!2026-02-09,16,290!2026-02-09,16,290-->

## constant descent Vieta jumping

The method of {@{__constant descent Vieta jumping__}@} is used when we wish to prove {@{a statement regarding a constant _k_ having something to do with the relation between _a_ and _b_}@}. Unlike {@{standard Vieta jumping}@}, constant descent is not {@{a proof by contradiction, and it consists of the following four steps}@}:<sup>[\[10\]](#^ref-10)</sup> (annotation: 4 steps: {@{equality case → quadratic → smaller root → base case}@}) <!--SR:!2026-04-02,54,310!2026-04-12,63,310!2026-02-09,16,290!2026-02-09,16,290!2026-04-07,58,310-->

1. (annotation: equality case) ::@:: The equality case is proven so that it may be assumed that _a_ \> _b_. <!--SR:!2026-04-09,60,310!2026-04-07,58,310-->
2. (annotation: quadratic) ::@:: _b_ and _k_ are fixed and the expression relating _a_, _b_, and _k_ is rearranged to form a quadratic with coefficients in terms of _b_ and _k_, one of whose roots is _a_. The other root, _x_<sub>2</sub> is determined using Vieta's formulas. <!--SR:!2026-02-09,16,290!2026-02-09,16,290-->
3. (annotation: smaller root) ::@:: For all \(_a_, _b_\) above a certain base case, show that 0 \< _x_<sub>2</sub> \< _b_ \< _a_ and that _x_<sub>2</sub> is an integer. Thus, while maintaining the same _k_, we may replace \(_a_, _b_\) with \(_b_, _x_<sub>2</sub>\) and repeat this process until we arrive at the base case. <!--SR:!2026-02-09,16,290!2026-03-19,43,290-->
4. (annotation: base case) ::@:: Prove the statement for the base case, and as _k_ has remained constant through this process, this is sufficient to prove the statement for all ordered pairs. <!--SR:!2026-04-02,54,310!2026-04-02,54,310-->

__Example__

Let _a_ and _b_ be {@{positive integers}@} such that {@{_ab_ divides _a_<sup>2</sup> + _b_<sup>2</sup> + 1}@}. Prove that {@{3<!-- markdown separator -->_ab_ = _a_<sup>2</sup> + _b_<sup>2</sup> + 1}@}.<sup>[\[11\]](#^ref-11)</sup> <!--SR:!2026-02-09,16,290!2026-04-12,63,310!2026-02-09,16,290-->

1. If {@{_a_ = _b_}@}, {@{_a_<sup>2</sup> dividing 2<!-- markdown separator -->_a_<sup>2</sup> + 1}@} implies that {@{_a_<sup>2</sup> divides 1}@}, and hence {@{the positive integers _a_ = _b_ = 1, and 3\(1\)\(1\) = 1<sup>2</sup> + 1<sup>2</sup> + 1}@}. So, without {@{loss of generality, assume that _a_ \> _b_}@}.
2. For {@{any \(_a_, _b_\) satisfying the given condition}@}, let {@{$k = \frac {a^2 + b^2 + 1}{ab}$}@} and rearrange and substitute to get {@{_x_<sup>2</sup> − \(_kb_\)&hairsp;<!-- markdown separator -->_x_ + \(_b_<sup>2</sup> + 1\) = 0}@}. {@{One root to this quadratic}@} is _a_, so by {@{Vieta's formulas (annotation: $a + x_2 = kb$) the other root may be written}@} as follows: {@{$x_2 = kb - a = \frac {b^2 + 1}{a}$}@}.
3. The first equation shows that {@{_x_<sub>2</sub> is an integer}@} and the second that {@{it is positive}@}. Because {@{_a_ \> _b_ and they are both integers}@}, {@{_a_ ≥ _b_ + 1, and hence _ab_ ≥ _b_<sup>2</sup> + _b_}@}; As long as {@{_b_ \> 1, we always have _ab_ \> _b_<sup>2</sup> + 1}@}, and therefore {@{$x_2 = \frac {b^2 + 1}{a} < b$}@}. Thus, while {@{maintaining the same _k_}@}, we may replace {@{\(_a_, _b_\) with \(_b_, _x_<sub>2</sub>\)}@} and repeat {@{this process until we arrive at the base case}@}.
4. {@{The base case}@} we arrive at is the case where {@{_b_ = 1}@}. For {@{\(_a_, 1\) to satisfy the given condition}@}, _a_ must {@{divide _a_<sup>2</sup> + 2}@}, which implies that {@{_a_ divides 2, making _a_ either 1 or 2}@}. {@{The first case is eliminated}@} because {@{_a_ = _b_}@}. In {@{the second case}@}, {@{$k = \frac {a^2 + b^2 + 1} {ab} = \frac 6 2 = 3$}@}. As _k_ has {@{remained constant throughout this process of Vieta jumping}@}, this is {@{sufficient to show that for any \(_a_, _b_\) satisfying the given condition}@}, _k_ will {@{always equal 3}@}. <!--SR:!2026-04-09,60,310!2026-02-09,16,290!2026-04-10,61,310!2026-02-09,16,290!2026-04-06,57,310!2026-02-09,16,290!2026-02-09,16,290!2026-04-06,57,310!2026-04-11,62,310!2026-04-02,54,310!2026-03-19,43,290!2026-02-09,16,290!2026-04-12,63,310!2026-04-08,59,310!2026-03-19,43,290!2026-04-08,59,310!2026-04-03,55,310!2026-02-09,16,290!2026-03-20,41,290!2026-02-09,16,290!2026-04-03,55,310!2026-04-09,60,310!2026-04-07,58,310!2026-02-09,16,290!2026-04-12,63,310!2026-02-09,16,290!2026-02-09,16,290!2026-04-02,54,310!2026-04-11,62,310!2026-04-11,62,310!2026-04-03,55,310!2026-04-12,63,310-->

## geometric interpretation

Vieta jumping can be described in terms of {@{lattice points on [hyperbolas](hyperbolas.md) in the first quadrant}@}.<sup>[\[2\]](#^ref-2)</sup> {@{The same process of finding smaller roots}@} is used instead to find {@{lower lattice points on a hyperbola}@} while remaining {@{in the first quadrant}@}. The procedure is as follows: <!--SR:!2026-04-08,59,310!2026-04-07,58,310!2026-04-12,63,310!2026-04-12,63,310-->

1. From {@{the given condition}@} we obtain {@{the equation of a family of hyperbolas}@} that are {@{unchanged by switching _x_ and _y_}@} so that they are {@{symmetric about the line _y_ = _x_}@}.
2. Prove {@{the desired statement}@} for {@{the intersections of the hyperbolas and the line _y_ = _x_}@}.
3. Assume there is {@{some lattice point \(_x_, _y_\) on some hyperbola}@} and without {@{loss of generality _x_ \< _y_}@}. Then by {@{Vieta's formulas}@}, there is {@{a corresponding lattice point with the same _x_-coordinate}@} on {@{the other branch of the hyperbola}@}, and by {@{reflection through _y_ = _x_}@} {@{a new point on the original branch of the hyperbola}@} is obtained.
4. It is shown that this process {@{produces lower points on the same branch}@} and can be {@{repeated until some condition \(such as _x_ = 0\) is achieved}@}. Then by {@{substitution of this condition}@} into {@{the equation of the hyperbola}@}, {@{the desired conclusion}@} will be proven. <!--SR:!2026-04-03,55,310!2026-02-09,16,290!2026-02-09,16,290!2026-04-12,63,310!2026-04-08,59,310!2026-02-09,16,290!2026-04-08,59,310!2026-04-10,61,310!2026-02-09,16,290!2026-04-03,55,310!2026-02-09,16,290!2026-04-07,58,310!2026-02-09,16,290!2026-04-10,61,310!2026-02-09,16,290!2026-02-09,16,290!2026-02-09,16,290!2026-04-07,58,310-->

__Example__

This method can be applied to {@{__problem \#6 at IMO 1988__}@}: Let _a_ and _b_ be {@{positive integers such that _ab_ + 1 divides _a_<sup>2</sup> + _b_<sup>2</sup>}@}. Prove that {@{$\frac {a^2 + b^2} {ab + 1}$ is a perfect square}@}. <!--SR:!2026-04-03,55,310!2026-04-02,54,310!2026-02-09,16,290-->

1. Let {@{$\frac {a^2 + b^2} {ab + 1} = q$}@} and fix {@{the value of _q_}@}. If {@{_q_ = 1, _q_ is a perfect square as desired}@}. If {@{_q_ = 2}@}, then {@{\(_a_-_b_\)<sup>2</sup> = 2 and there is no integral solution _a_, _b_}@}. When {@{_q_ \> 2}@}, {@{the equation _x_<sup>2</sup> + _y_<sup>2</sup> − _qxy_ − _q_ = 0}@} defines {@{a hyperbola _H_ and \(_a_,_b_\) represents an integral lattice point on _H_}@}. <p> (annotation: For the equation: {@{$x^2 + y^2 - qxy - q = 0$}@}, {@{the discriminant}@} is: {@{$\Delta = B^2 - 4AC = (-q)^2 - 4(1)(1) = q^2 - 4$}@}. If {@{$\Delta > 0$}@}, {@{the curve is a _hyperbola_}@}. If {@{$\Delta = 0$}@}, {@{the curve is a _parabola_}@}. Finally, if {@{$\Delta < 0$}@}, {@{the curve is an _ellipse_}@}.)
2. If {@{\(_x_,_x_\)}@} is {@{an integral lattice point on _H_ with _x_ \> 0}@}, then {@{\(since _q_ is integral\) one can see that _x_ = 1}@}. {@{This proposition's statement}@} is then {@{true for the point \(_x_,_x_\)}@}.
3. (annotation: Rewrite _H_ to be {@{$y^2 - (qx)y +  \left(x^2 - q\right) = 0$}@}.) <p> Now let {@{_P_ = \(_x_, _y_\)}@} be {@{a lattice point on a branch _H_ with _x_, _y_ \> 0 and _x_ ≠ _y_}@} \(as the previous remark covers {@{the case _x_ = _y_}@}\). By {@{symmetry}@}, we can assume that {@{_x_ \< _y_ and that _P_ is on the higher branch of _H_}@}. By applying {@{Vieta's Formulas (annotation: $y + y' = qx$)}@}, {@{\(_x_, _qx_ − _y_\)}@} is {@{a lattice point on the lower branch of _H_}@}. Let {@{_y_′ = _qx_ − _y_}@}. From {@{the equation for _H_}@}, one sees that {@{1 + _x_ _y_′ \> 0}@}. Since {@{_x_ \> 0}@}, it follows that {@{_y_′ ≥ 0}@}. Hence the point \(_x_, _y_′\) is {@{in the first quadrant}@}. By {@{reflection}@}, {@{the point \(_y_′, _x_\)}@} is also {@{a point in the first quadrant on _H_}@}. Moreover from {@{Vieta's formulas, _yy_′ = _x_<sup>2</sup> - _q_}@}, and {@{$y' = \frac {x^2 - q} y$}@}⁠. Combining {@{this equation with _x_ \< _y_}@}, one can show that {@{_y_′ \< _x_}@}. {@{The new constructed point _Q_ = \(_y_′, _x_\)}@} is then in {@{the first quadrant, on the higher branch of _H_}@}, and with {@{smaller _x_,_y_-coordinates than the point _P_}@} we started with.
4. {@{The process in the previous step}@} can be repeated {@{whenever the point _Q_ has a positive _x_-coordinate}@}. However, since {@{the _x_-coordinates of these points}@} will form {@{a decreasing sequence of non-negative integers}@}, the process can {@{only be repeated finitely many times}@} before it produces {@{a point _Q_ = \(0, _y_\) on the upper branch of _H_}@}; by {@{substitution (annotation: onto the parabola equation defining _H_)}@}, {@{_q_ = _y_<sup>2</sup> is a square}@} as required. <!--SR:!2026-02-09,16,290!2026-02-09,16,290!2026-04-03,55,310!2026-04-09,60,310!2026-02-09,16,290!2026-04-12,63,310!2026-02-09,16,290!2026-04-10,61,310!2026-03-22,42,290!2026-02-09,16,290!2026-02-09,16,290!2026-04-02,54,310!2026-04-02,54,310!2026-04-04,56,310!2026-04-03,55,310!2026-02-09,16,290!2026-04-03,55,310!2026-04-02,54,310!2026-04-03,55,310!2026-03-19,43,290!2026-02-09,16,290!2026-04-11,62,310!2026-03-19,43,290!2026-02-09,16,290!2026-02-09,16,290!2026-04-08,59,310!2026-04-11,62,310!2026-04-11,62,310!2026-03-19,43,290!2026-02-09,16,290!2026-04-10,61,310!2026-03-19,43,290!2026-04-09,60,310!2026-04-02,54,310!2026-02-09,16,290!2026-02-09,16,290!2026-04-06,58,310!2026-02-09,16,290!2026-02-09,16,290!2026-04-03,55,310!2026-04-02,54,310!2026-04-12,63,310!2026-04-10,61,310!2026-04-09,60,310!2026-04-03,55,310!2026-04-02,54,310!2026-04-12,63,310!2026-02-09,16,290!2026-02-09,16,290!2026-04-05,57,310!2026-02-09,16,290!2026-02-09,16,290!2026-04-02,54,310!2026-04-03,55,310!2026-02-09,16,290-->

## see also

- [Vieta's formulas](Vieta's%20formulas.md)
- [Proof by contradiction](proof%20by%20contradiction.md)
- [Infinite descent](infinite%20descent.md)
- [Markov number](Markov%20number.md)
- [Apollonian gasket](Apollonian%20gasket.md)

## notes

This text incorporates [content](https://en.wikipedia.org/wiki/Vieta_jumping) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. [Mills 1953](#CITEREFMills1953). <a id="^ref-1"></a>^ref-1
2. <a id="CITEREFArthur Engel1998"></a> Arthur Engel \(1998\). [_Problem Solving Strategies_](https://books.google.com/books?id=IJLzBwAAQBAJ&pg=PA127). Problem Books in Mathematics. Springer. p. 127. [doi](doi%20(identifier).md):[10.1007/b97682](https://doi.org/10.1007%2Fb97682). [ISBN](ISBN%20(identifier).md) [978-0-387-98219-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-98219-9). <a id="^ref-2"></a>^ref-2
3. ["The Return of the Legend of Question Six"](https://www.youtube.com/watch?v=L0Vj_7Y2-xY). _[Numberphile](numberphile.md)_. August 16, 2016. [Archived](https://ghostarchive.org/varchive/youtube/20211220/L0Vj_7Y2-xY) from the original on 2021-12-20 – via [YouTube](YouTube.md). <a id="^ref-3"></a>^ref-3
4. ["International Mathematical Olympiad"](http://www.imo-official.org/problems.aspx). _<www.imo-official.org>_. Retrieved 29 September 2020. <a id="^ref-4"></a>^ref-4
5. ["Results of the 1988 International Mathematical Olympiad"](http://www.imo-official.org/year_individual_r.aspx?year=1988&column=total&order=desc). Imo-official.org. Retrieved 2013-03-03. <a id="^ref-5"></a>^ref-5
6. ["Individual ranking of Emanouil Atanassov"](https://www.imo-official.org/participant_r.aspx?id=1586). International Mathematical Olympiad. <a id="^ref-6"></a>^ref-6
7. <a id="CITEREFYimin Ge2007"></a> Yimin Ge \(2007\). ["The Method of Vieta Jumping"](http://georgmohr.dk/tr/tr09taltvieta.pdf) \(PDF\). _Mathematical Reflections_. __5__. <a id="^ref-7"></a>^ref-7
8. ["AoPS Forum – One of my favourites problems, yeah!"](https://artofproblemsolving.com/community/c6h57282). Artofproblemsolving.com. Retrieved 2023-01-08. <a id="^ref-8"></a>^ref-8
9. <a id="CITEREFK. S. Brown"></a> K. S. Brown. ["N = \(x^2 + y^2\)/\(1+xy\) is a Square"](http://www.mathpages.com/home/kmath334.htm). MathPages.com. Retrieved 2016-09-26. <a id="^ref-9"></a>^ref-9
10. ["AoPS Forum — Lemur Numbers"](https://artofproblemsolving.com/community/c6h278180). Artofproblemsolving.com. Retrieved 2023-01-08. <a id="^ref-10"></a>^ref-10
11. ["AoPS Forum – x\*y \| x^2+y^2+1"](https://artofproblemsolving.com/community/c6h40207). Artofproblemsolving.com. 2005-06-07. Retrieved 2023-01-08. <a id="^ref-11"></a>^ref-11

## external links

- [Vieta Root Jumping](https://brilliant.org/wiki/vieta-root-jumping/) at [Brilliant.org](Brilliant.org.md)
- <a id="CITEREFMills1953"></a> Mills, W. H. \(1953\). ["A system of quadratic Diophantine equations"](http://projecteuclid.org/euclid.pjm/1103051516). _Pacific J. Math_. __3__ \(1\): 209–220.

> [Categories](https://en.wikipedia.org/wiki/Help:Category):
>
> - [Number theory](https://en.wikipedia.org/wiki/Category:Number%20theory)
> - [Diophantine equations](https://en.wikipedia.org/wiki/Category:Diophantine%20equations)
