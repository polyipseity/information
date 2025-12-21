---
aliases:
  - COMP 2211 question
  - COMP 2211 questions
  - COMP2211 question
  - COMP2211 questions
  - HKUST COMP 2211 question
  - HKUST COMP 2211 questions
  - HKUST COMP2211 question
  - HKUST COMP2211 questions
tags:
  - flashcard/active/special/academia/HKUST/COMP_2211/questions
  - language/in/English
---

# questions

- HKUST COMP 2211

## introduction to artificial intelligence

> Q1. Which of the following best describes AI?
>
> 1. AI is the process of optimizing machine tasks using neural networks.
> 2. AI is the science of getting machines to act in a certain way without being explicitly programmed.
> 3. AI is a sentient robot.
> 4. AI is the science and engineering of making intelligent machines.
>
> - solution: {@{4}@}
> - explanation: {@{This definition is due to Alan Turing.}@} <!--SR:!2026-01-01,290,330!2025-12-22,282,330-->

<!-- markdownlint MD028 -->

> Q2. Who is (widely regarded as) the founder of artificial intelligence?
>
> 1. Alan Turing
> 2. John McCarthy
> 3. Frank Rosenblatt
> 4. Desmond <!-- ____ -->
>
> - solution: {@{1}@} <!--SR:!2025-12-27,286,330-->

<!-- markdownlint MD028 -->

> Q3. Which of the following is a Python library for machine learning?
>
> 1. Ditto
> 2. Sawk
> 3. Keras
> 4. Vulpix
>
> - solution: {@{3}@} <!--SR:!2028-11-20,1112,350-->

<!-- markdownlint MD028 -->

> Q4. Which of the following fields is not a foundation of AI (for now)?
>
> 1. Mathematics
> 2. Particle physics
> 3. Neurobiology
> 4. Cognition science
>
> - solution: {@{2}@} <!--SR:!2029-01-25,1166,350-->

<!-- markdownlint MD028 -->

> Q5. Which of the following is not (yet) an application of AI?
>
> 1. Gaming and entertainment
> 2. Speech recognition
> 3. Expert systems
> 4. Content mining
>
> - solution: {@{4}@}
> - explanation: {@{Too simple, simply hard code it...}@} <!--SR:!2028-12-08,1127,350!2029-02-03,1170,350-->

<!-- markdownlint MD028 -->

> Q6. Which of the following Python library is (allegedly) the easiest to use?
>
> 1. TensorFlow
> 2. PyTorch
> 3. Keras
> 4. scikit-learn
>
> - solution: {@{4}@} <!--SR:!2029-02-09,1175,350-->

<!-- markdownlint MD028 -->

> Q7. Which of the following is NOT a subclass of Neural Networks? (You are encouraged to do some web searching on these algorithms as they will appear in this course :P)
>
> 1. Multi-layer Perceptrons (MLP)
> 2. Convolutional Neural Network (CNN)
> 3. Minimax and Alpha-Beta Pruning
>
> - solution: {@{3}@} <!--SR:!2026-01-04,293,330-->

<!-- markdownlint MD028 -->

> Q8. Which of the following is a made-up event by your bad guy TA in the history of AI (Let's say 1950–2022)?
>
> 1. IBM supercomputer Deep Blue beats chess champion, Garry Kasparov, in a 6-game match
> 2. Ian Goodfellow comes up with General Adversarial Networks
> 3. The second AI winter happened in 1987–1993
> 4. The natural language processing AI, ELIZA, passes the Turing test
>
> - solution: {@{4}@} <!--SR:!2026-01-05,294,330-->

<!-- markdownlint MD028 -->

> Q9. Which of the following is not an advantage for using Python for writing AI?
>
> 1. Python has many libraries for machine learning
> 2. Python is easy to learn
> 3. Python is a dynamically typed language
> 4. Python is popular and has a large community
>
> - solution: {@{3}@} <!--SR:!2028-10-30,1094,350-->

## Python fundamentals for artificial intelligence

> Q1. Which of the following defines a dictionary?
>
> 1. `["a", "b"]`
> 2. `["a": "b"]`
> 3. `{"a", "b"}`
> 4. `{"a": "b"}`
>
> - solution: {@{4}@} <!--SR:!2028-08-22,1038,350-->

<!-- markdownlint MD028 -->

> Q2. What does `print(len("hehehaha"))` output?
>
> - solution: {@{`8`}@} <!--SR:!2029-03-20,1206,350-->

<!-- markdownlint MD028 -->

> Q3. What does `print(len(r"\n Desmond is a good guy na!\n"))` output?
>
> - solution: {@{`30`}@}
> - explanation: {@{Notice the `r` before the string beginning.}@} <!--SR:!2029-01-13,1156,350!2029-05-18,1254,350-->

<!-- markdownlint MD028 -->

> Q4. Which of the following is not a mutable type?
>
> 1. Lists
> 2. Tuples
> 3. Dictionaries
> 4. Sets
>
> - solution: {@{2}@} <!--SR:!2028-09-09,1052,350-->

<!-- markdownlint MD028 -->

> Q5. Print a NumPy array of all zeros, with 3 rows and 5 columns.
>
> Your code should be at most one line.
>
> - solution: {@{`print(numpy.zeros((3, 5)))`}@} <!--SR:!2028-12-02,1122,350-->

<!-- markdownlint MD028 -->

> Q6. Recreate the following array in one line.
>
> ```Python
> array([[ 1,  2,  3,  4],
>        [ 5,  6,  7,  8],
>        [ 9, 10, 11, 12],
>        [13, 14, 15, 16]])
> ```
>
> - solution: {@{`numpy.arange(1, 17).reshape((4, 4))`}@} <!--SR:!2026-01-02,291,330-->

<!-- markdownlint MD028 -->

> Q7. What is the shape of the following array?
>
> ```Python
> array([[[ 1,  2,  3,  4],
>         [ 5,  6,  7,  8]],
>
>        [[ 9, 10, 11, 12],
>         [13, 14, 15, 16]],
>
>        [[ 9, 10, 11, 12],
>         [13, 14, 15, 16]]])
> ```
>
> - solution: {@{\(3, 2, 4\)}@} <!--SR:!2028-03-12,884,330-->

<!-- markdownlint MD028 -->

> Q8. Return the maximum value within a NumPy array `a`.
>
> - solution: {@{`numpy.max(a)`, `a.max()`}@} <!--SR:!2029-04-26,1234,350-->

<!-- markdownlint MD028 -->

> Q9. Return the minimum value within a NumPy array `a`.
>
> - solution: {@{`numpy.min(a)`, `a.min()`}@} <!--SR:!2026-01-03,292,330-->

<!-- markdownlint MD028 -->

> Q10. What is the output of the following code?
>
> ```Python
> import numpy as np
> a = np.array([[1, 2, 3, 4],
>               [5, 6, 7, 8]])
> print(a.transpose())
> ```
>
> - solution: {@{(newlines omitted) `[[1 5] [2 6] [3 7] [4 8]]`}@} <!--SR:!2025-12-17,277,330-->

<!-- markdownlint MD028 -->

> Q11. Suppose we have an array `M` of shape (4, 5, 6). Which of the following operations are valid?
>
> 1. `M + A`, where `A` is an array of shape (4, 5)
> 2. `M + B`, where `B` is an array of shape (4, 1)
> 3. `M + C`, where `C` is an array of shape (5, 3)
> 4. `M + D`, where `D` is an array of shape (5, 1)
>
> - solution: {@{4}@} <!--SR:!2029-05-03,1241,350-->

<!-- markdownlint MD028 -->

> Q12. What is the output of the following code?
>
> ```Python
> import numpy as np
> a = np.array([[2, 2, 1, 1], [1, 2, 3, 4]])
> b = np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
> print(a + b)
> ```
>
> - solution: {@{(newlines omitted) `[[3 5 6 8] [3 6 9 12]]`}@} <!--SR:!2025-12-21,281,330-->

<!-- markdownlint MD028 -->

> Q13. Which of the following functions correctly compares two integer arrays and returns "True" if and only if they have the same shape and entries?
>
> ```Python
> import numpy as np
> def A(a1, a2):
>   return a1 == a2
> def B(a1, a2):
>   return a1 - a2 == 0
> def C(a1, a2):
>   if a1.shape == a2.shape:
>     return (a1 == a2).all()
>   return False
> def D(a1, a2):
>   if a1.shape == a2.shape:
>     return a1 - a2 == 0
>   return False
> ```
>
> - solution: {@{C}@} <!--SR:!2028-11-29,1120,350-->

<!-- markdownlint MD028 -->

> Q14. Suppose we have an array `M` of shape (3, 4, 5). Which of the following operations are valid?
>
> 1. `M * A`, where `A` is an array of shape (3, 4)
> 2. `M * B`, where `B` is an array of shape (3, 1)
> 3. `M * C`, where `C` is an array of shape (4, 1)
> 4. `M * D`, where `D` is an array of shape (5, 1)
>
> - solution: {@{3}@} <!--SR:!2028-12-23,1140,350-->

<!-- markdownlint MD028 -->

> Q15. Suppose we have an array `M` of shape (22, 11). Which of the following operations are valid? Also, determine the shape of the array after the operation.
>
> 1. `np.dot(M, A)`, where `A` is an array of shape (11, 33)
> 2. `np.dot(B, M)`, where `B` is an array of shape (33, 11)
> 3. `np.dot(M, C)`, where `C` is an array of shape (22, 11)
> 4. `np.dot(D, M)`, where `D` is an array of shape (11, 33)
>
> - solution: {@{1}@} <!--SR:!2027-04-18,644,330-->

<!-- markdownlint MD028 -->

> Q16. In image processing, we often want to use a data type called "8-bit unsigned integer" (`numpy.uint8`), which is an integer ranging from 0–255; it represents the intensity of colors in an image. Create an array of shape (1920, 1080) with all 8-bit unsigned integers, with a value of 0.
>
> Your code should be at most one to two lines, and should not contain any loops.
>
> - solution: {@{`numpy.zeros((1920, 1080), dtype=numpy.uint8)`, `numpy.full((1920, 1080), fill_value=0, dtype=numpy.uint8)`}@} <!--SR:!2029-01-29,1167,350-->

<!-- markdownlint MD028 -->

> Q17. What is the output of the following code?
>
> ```Python
> import numpy as np
> a = np.array([[2, 2, 1, 1], [1, 2, 3, 4]])
> b = np.array([[22], [11]])
> print(a + b)
> ```
>
> - solution: {@{(newlines omitted) `[[24 24 23 23] [12 13 14 15]]`}@} <!--SR:!2028-01-03,845,330-->

<!-- markdownlint MD028 -->

> Q18. Consider the following code:
>
> ```Python
> from another_file import data
> import matplotlib.pyplot as plt
> plt.figure()
> plt.plot(data)
> plt.show()
> ```
>
> Which of the following best describes "pyplot"?
>
> 1. It is a function
> 2. It is a module
> 3. It is a package
> 4. It is a library
>
> - solution: {@{2}@} <!--SR:!2025-12-13,276,330-->

<!-- markdownlint MD028 -->

> Q19. What is the output of the following code?
>
> ```Python
> import numpy as np
> a = np.arange(1000).reshape(10, 10, 10)
> haha = a[(1,2,3), (4,5,6), (7,8,9)]
> print(haha)
> ```
>
> - solution: {@{`[147 258 369]`}@} <!--SR:!2027-12-11,818,330-->

<!-- markdownlint MD028 -->

> Q20. Return all values that are greater than or equal to the mean values in the array `a`.
>
> Your code should be at most one to two lines, and should not contain any loops.
>
> - solution: {@{`a[a >= numpy.average(a)]`, `a[a >= numpy.mean(a)]`}@} <!--SR:!2029-01-24,1164,350-->

<!-- markdownlint MD028 -->

> Q21. Return the second largest element of an array `a`.
>
> Your code should be at most one to two lines, and should not contain any loops. Hint: use `numpy.argsort`.
>
> - solution: {@{`a[numpy.argsort(a)[-2]]`}@} <!--SR:!2029-03-08,1197,350-->

<!-- markdownlint MD028 -->

> Q22. Desmond promises that 25% of the class (floored to the nearest integer) will get an A range in COMP2211. Assume in the following code, that `student[i]` scores `marks[i]` points. Complete the following function that returns an array of all students with an A range.
>
> Your code should be at most one to two lines, and should not contain any loops. Hint: the last question might help.
>
> - solution: {@{`students[numpy.argsort(marks)[-len(students) // 4:]]`}@} <!--SR:!2029-04-30,1238,350-->

<!-- markdownlint MD028 -->

> Q23. Using broadcasting magic, complete the following code snippet to print this NumPy array with shape (2211, 4):
>
> ```Python
> array([[0, 1, 2, 3],
>        [0, 1, 2, 3],
>        ...,
>        [0, 1, 2, 3]])
> ```
>
> This is your current code (cannot change):
>
> ```Python
> import numpy as np
> a = np.arange(4)
> ```
>
> Your code should be at most one to two lines, and should not contain any loops.
>
> - solution: {@{`print(a * np.ones((2211, 1), dtype=int))`, `print(a + np.zeros((2211, 1), dtype=int))`}@} <!--SR:!2029-02-01,1169,350-->

<!-- markdownlint MD028 -->

> Q24. Using broadcasting magic, complete the following code snippet to print this NumPy array with shape (2211, 4):
>
> ```Python
> array([[   0,    1,    2,    3],
>        [   1,    2,    3,    4],
>        ...,
>        [2210, 2211, 2212, 2213]])
> ```
>
> This is your current code (cannot change):
>
> ```Python
> import numpy as np
> a = np.arange(4)
> ```
>
> Your code should be at most one to two lines, and should not contain any loops.
>
> - solution: {@{`print(a + np.arange(2211).reshape((2211, 1)))`}@} <!--SR:!2028-11-10,1104,350-->

<!-- markdownlint MD028 -->

> Q25. Using broadcasting magic, complete the following code snippet to print this NumPy array with shape (2211, 4):
>
> ```Python
> array([[   0,    2,    4,    6],
>        [   4,    6,    8,   10],
>        ...,
>        [8840, 8842, 8844, 8846]])
> ```
>
> This is your current code (cannot change):
>
> ```Python
> import numpy as np
> a = np.arange(4)
> ```
>
> Your code should be at most one to two lines, and should not contain any loops.
>
> - solution: {@{`print(2 * a + 4 * np.arange(2211).reshape((2211, 1)))`}@} <!--SR:!2027-06-26,629,310-->

<!-- markdownlint MD028 -->

> Q26. What is the expected output of the following code?
>
> ```Python
> import numpy as np
> import time
> s = 999999999
> a = np.random.random((s, 1))
> b = np.random.random((1, s))
> def time1():
>   t1 = time.time()
>   np.dot(b, a)
>   t2 = time.time()
>   return t2 - t1
> def time2():
>   t1 = time.time()
>   res = 0
>   for i in range(s):
>       res += a[i, 0] * b[0, i]
>   t2 = time.time()
>   return t2 - t1
> print(time1() <= time2())
> ```
>
> - solution: {@{(almost always) `True`}@}
> - explanation: {@{`time1` performs an element-wise operation using pure Python while `time2` uses NumPy arrays to do the same thing, so `time2` is most likely faster.}@} <!--SR:!2028-10-28,1093,350!2028-03-21,892,330-->

<!-- markdownlint MD028 -->

> Q27. Get the minimum value of each row in a 2D array `a`. (For the sake of terminology, a row is a set of data that spans along the last dimension.)
>
> Your code should be at most one to two lines, and should not contain any loops. Hint: take a look at the "axis" argument that appears in many common NumPy functions.
>
> - solution: {@{`numpy.min(a, axis=1)`, `numpy.min(a, axis=-1)`}@} <!--SR:!2028-12-26,1141,350-->

<!-- markdownlint MD028 -->

> Q28. Which of the following returns "False"?
>
> 1. `3 ** 2 == 9`
> 2. `0.1 + 0.2 == 0.3`
> 3. `12.0 / 4.0 == 3.0`
> 4. `5 // 3 == 1`
>
> - solution: {@{2}@}
> - explanation: {@{To be fair, this question is unlikely to be tested... It is simply trying to show that `float`s have limited precision.}@} <!--SR:!2026-01-03,292,330!2025-12-31,290,330-->

<!-- markdownlint MD028 -->

> Q29. What is the output of the following code?
>
> ```Python
> import numpy as np
> haha = np.array([1, 2, 3])
> hehe = haha
> hehe[2] = 999
> print(haha)
> ```
>
> - solution: {@{`[1 2 999]`}@} <!--SR:!2026-01-01,290,330-->

<!-- markdownlint MD028 -->

> Q30. In machine learning, we often want to label our data with a 2D array with _N_ rows, where each data is a row of 0s and 1s, indicating whether the feature belongs in a certain category. This technique is known as _one-hot encoding_. Turn a 1D array of non-negative integers `a` into _one-hot encoding_. (For the sake of terminology, a row is a set that spans along the last dimension.)
>
> Your code should be at most five lines and should not contain any loops.
>
> - solution: {@{`(a[..., numpy.newaxis] == numpy.arange(len(a))).astype(int)`}@} <!--SR:!2026-12-09,525,310-->

<!-- markdownlint MD028 -->

> Q31. One task frequently appearing in machine learning is to compute the "distances" between different data points. A "data point" in this question has 3 different features represented by 3 floating point values. Suppose an array `X` of shape (2211, 3) holds 2211 data points (which is our training data set), and another array `T` of shape (300, 3) holds 300 data points (which is our test data set). Using broadcasting magic, compute the NumPy array `dists` of shape (2211, 300), where dists[i, j] is the distance between `X[i]` and `T[j]` for each `i` and `j`.
>
> For the sake of terminology, the distance between x = (x1, x2, x3) and y = (y1, y2, y3) is defined as the square root of (x1 - y1)^2 + (x2 - y2)^2 + (x3 - y3)^2.
>
> Your code should be at most five lines, and should not contain any loops. Try not to hard-code the numbers "2211" and "300" into your code.
>
> - solution: {@{`dists = numpy.sqrt(numpy.sum((X[..., numpy.newaxis, :] - T) ** 2, axis=-1))`}@} <!--SR:!2029-02-07,1174,350-->

<!-- markdownlint MD028 -->

> Q32. Are there any differences between the output from `print(str(a))` and `print(repr(a))`? Assume `a` is a NumPy array.
>
> - solution: {@{Yes. Try it out yourself!}@}
> - explanation: {@{The `repr` representation is used when you explicitly write `repr(a)` or if you are printing the value without `print` in interactive Python. Otherwise, the `str` representation is used. <p> In this file, we use the `str` representation if `print` is used, otherwise we use the `repr` representation. In exams, you should see what they ask for.}@} <!--SR:!2029-02-11,1177,350!2027-11-22,761,330-->

## naive Bayes classifier

> Q1. (simple) True or false: The naive Bayes classifier uses a labeled dataset.
>
> - solution: {@{true}@} <!--SR:!2026-01-04,293,330-->

<!-- markdownlint MD028 -->

> Q2. (simple) Which of the following are correct regarding the naive Bayes classifier?
>
> 1. The naive Bayes classifier is a clustering algorithm.
> 2. The naive Bayes classifier is uses a labeled dataset.
> 3. The naive Bayes classifier assumes independence of events (features).
>
> - solution: {@{2, 3}@} <!--SR:!2028-12-27,1142,350-->

<!-- markdownlint MD028 -->

> Q3. (medium) Consider a random bit string with length 4 (a bit string is a sequence of 0s and 1s, e.g. 0000 or 0101). What is the probability that it contains two consecutive 0s, given that the first bit is 0?
>
> - solution: {@{$$1/2 + 1/2 \times 1/4 = 5/8$$}@} <!--SR:!2025-12-28,287,330-->

<!-- markdownlint MD028 -->

> Q4. (advanced) On average, 1 in 1000 drivers drunk drives. A breath analyzer with an error rate of 5% (5% false positive, 5% false negative) is used to test if a driver is drunk driving. Police stop a driver at random and administer the breath analyzer, which reports that the driver is indeed drunk driving.
>
> Answer the following two questions.
>
> 1. Since the breath analyzer has an error rate of 5%, a student claims the probability that the driver is drunk driving should be 95%. Explain why this intuition is wrong.
> 2. Using Bayes Theorem, find the true probability that the driver is drunk driving, i.e. find $P( \text{ drunk driving } | \text{ reported drunk by breath analyzer } )$.
>
> - solution: {@{For 1, it neglects the base rate, i.e. 1 in 1000 drivers drunk drives (see base rate fallacy). <p> For 2, this is $$\frac {1 / 1000 \times 0.95} {(1 / 1000 \times 0.95) + (999 / 1000 \times 0.05)} \approx 1.87\% \,.$$}@} <!--SR:!2026-01-03,292,330-->

<!-- markdownlint MD028 -->

> Q5. (medium) If two events $E$ and $F$ are independent, then
>
> 1. $P(E \mid F) = P(F \mid E)$
> 2. $P(E \text{ and } F) = P(E) \times P(F)$
> 3. $P(E \mid F) = P(E)$
>
> - solution: {@{2, 3}@}
> - explanation: {@{1 holds when additionally, $P(E) = P(F)$.}@} <!--SR:!2028-03-17,849,330!2028-12-24,1140,350-->

<!-- markdownlint MD028 -->

> Q6. (medium)  Let $E_1, \cdots, E_n, B_1, \cdots, B_n$ be events. Denote the complement of an event $E$ by $E^c$. Which of the following formulas requires the independence assumption?
>
> 1. $P(B|E_1, \cdots, E_n) = \frac{ P(E_1 \cap \cdots \cap E_n|B)P(B) }{ P(E_1 \cap \cdots \cap E_n | B)P(B) + P(E_1 \cap \cdots \cap E_n | B^c)P(B^c) }$
> 2. $P(B_1 \cap \cdots \cap B_n|E) = \frac{ P(E | B_1 \cap \cdots \cap B_n)P(B_1 \cap \cdots \cap B_n) }{ P(E) }$
> 3. $P(B_1 \cap \cdots \cap B_n | E_1 \cap \cdots \cap E_n) = \frac{ P(B_1 \cap \cdots \cap B_n \cap E_1 \cap \cdots \cap E_n) }{ P(E_1 \cap \cdots \cap E_n) }$
>
> - solution: {@{none}@} <!--SR:!2029-02-23,1186,350-->

<!-- markdownlint MD028 -->

> Q7. (medium) Which of the following is a correct description of the Naive Bayes classifier?
>
> 1. The naive Bayes classifier assumes each _belief_ is independent.
> 2. The naive Bayes classifier assumes each piece of evidence contributes <!-- equally -->independently to the belief.
> 3. The naive Bayes classifier always predicts correct results.
> 4. None of the above
>
> - solution: {@{2}@} <!--SR:!2025-12-30,287,330-->

<!-- markdownlint MD028 -->

> Q8. (simple) True or false. There are $n$ different beliefs $B_1, B_2, \cdots, B_n$. If the pieces of evidence are independent, then the following formula gives us the probability of belief $B$ given the evidence. $$P(B|E_1 \cap \cdots \cap E_n) \overset ? = P(B) P(E_1|B) P(E_2|B) \cdots P(E_n|B)$$
>
> - solution: {@{false}@}
> - explanation: {@{The denominator, which is the probability of the evidence $P(E_1 \cap \cdots \cap E_n)$, has been removed to derive the right hand side of the above equation (but the left hand side is not updated). So the above equation does not hold (i.e. the left hand side does not equal the right hand side).}@} <!--SR:!2028-09-18,1060,350!2025-12-25,285,330-->

<!-- markdownlint MD028 -->

> Q9. (simple) Some people prefer to use the following formula to determine the most likely belief. $$\max_{i\in \{0, 1, \cdots, n\} } \left( \ln P(B_i) + \ln P(E_1 | B_i) + \cdots + P(E_n|B_i) \right)$$
>
> What is the motivation behind such a formula?
>
> - solution: {@{To avoid floating-point underflow.}@} <!--SR:!2028-12-09,1127,350-->

<!-- markdownlint MD028 -->

> Q10. (simple) State __one__ advantage and __one__ disadvantage of the naive Bayes classifier.
>
> - solution: {@{(for reference) It is easy to implement. But its accuracy is low for a small dataset.}@} <!--SR:!2028-12-03,1123,350-->

## _k_-nearest neighbors

> Q1. For KNN, the computational complexity during training is \_\_\_\_, while the computational complexity during test time is \_\_\_\_, where "n" is the number of samples. (If you don't know about big O notations, please watch [this](https://youtu.be/__vX2sjlpXU) YouTube video. If you still don't understand big O notations after watching the video, you may simply skip this question.)
>
> 1. O(n), O(n)
> 2. O(n^2), O(n)
> 3. O(n), O(1)
> 4. O(1), O(n)
>
> - solution: {@{4 (in a computation model where storage takes constant time)}@} <!--SR:!2029-01-19,1160,350-->

<!-- markdownlint MD028 -->

> Q2. Which of the followings is/are hyperparameters in the KNN algorithm? (In machine learning, a hyperparameter is a parameter whose value is used to control the learning process. They are determined before training, and cannot be inferred while fitting the machine to the training set because they refer to the model selection task, or algorithm hyperparameters, that in principle have no influence on the performance of the model but affect the speed and quality of the learning process. By contrast, the values of other parameters, which are often learnable, are derived via training.)
>
> 1. K
> 2. Distance metric
> 3. Number of samples
>
> - solution: {@{1, 2}@} <!--SR:!2025-12-31,290,330-->

<!-- markdownlint MD028 -->

> Q3. Suppose we have two points, A and B, in a Cartesian coordinate system, where the location of A is (1,5) and the location of B is (4,1). The L1 (Manhattan) distance between A and B is \_\_\_, and the L2 (Euclidean) distance between A and B is \_\_\_.
>
> - solution: {@{7, 5}@} <!--SR:!2026-01-05,294,330-->

<!-- markdownlint MD028 -->

> Q4. To select the best K for our problem, we often divide our data into the training set, validation set, and test set, and check the performance of some K on the validation set. Explain why we do this on the validation set but not the training or test set.
>
> - solution: {@{(for reference) If we were to do so on the training set, the optimal K would have been 1. If we were to do so on the test set, then it would have defeated the purpose of the test data – reflecting the performance of our model on unseen data.}@} <!--SR:!2029-04-05,1219,350-->

<!-- markdownlint MD028 -->

> Q5. Which of the following is TRUE about KNN?
>
> 1. It can only be used for classification.
> 2. It can only be used for regression.
> 3. It assumes that all data are of the same scale.
> 4. None of the above.
>
> - solution: {@{4}@}
> - explanation: {@{For 1 and 2, classification is an obvious use case. For regression, one way is taking the neighbor average weighted by inverse distances. For 3, while it does not require all data to be of the same scale, this would make the distance of each feature not considered with the same weight.}@} <!--SR:!2028-02-10,823,330!2026-06-06,395,310-->

<!-- markdownlint MD028 -->

> Q6. Match the following distance metrics with their applicable data: L1 distance can be used for \_\_\_, L2 distance can be used for \_\_\_, and Hamming distance can be used for \_\_\_.
>
> 1. continuous variable
> 2. categorical variable
>
> - solution: {@{1, 1, 2}@} <!--SR:!2029-01-30,1167,350-->

<!-- markdownlint MD028 -->

> Q7. Suppose we have performed D-fold validation on our data to help decide the best K, and we obtain an error rate for each K. How to choose the best K?
>
> - solution: {@{Choose the K with the lowest error rate.}@} <!--SR:!2028-08-11,1028,350-->

<!-- markdownlint MD028 -->

> Q8. KNN is a machine learning algorithm that can be used for classification problems, and image classification is a fundamental task in computer vision. However, the KNN classifier is seldom used for image classification in reality because it can be easily hacked. Suppose we define the L1 distance between two images as the summed pixel-wise absolute difference over all pixels. For example, consider two 2×2 images:
>
> |    |    |
> |:--:|:--:|
> | 15 | 87 |
> | 38 | 43 |
>
> |    |    |
> |:--:|:--:|
> | 72 | 11 |
> | 22 | 63 |
>
> According to the definition given above, the L1 distance between them should be |72−15|+|11−87|+|22−38|+|63−43|=169.
>
> Using the L1 distance metric and KNN classification algorithm, propose 2 ways to produce new images from <!-- a given image -->the first image, such that the produced images have the same L1 distances to <!-- the original image -->the first image as the second image.
>
> - solution: {@{One solution is masking out certain pixels in the first image such that the sum of masked out pixels equals the L1 distance. <p> Another solution is adjusting the brightness of the first image.}@}
> - explanation: {@{Look up adversarial machine learning, a relatively new field...}@} <!--SR:!2027-07-27,708,330!2029-02-12,1178,350-->

<!-- markdownlint MD028 -->

> Q9. Suppose you are given some training data, as shown below.
>
> | x  | y  | class |
> |:--:|:--:|:-----:|
> | −1 | 1  | −     |
> | 0  | 1  | +     |
> | 0  | 2  | −     |
> | 1  | −1 | −     |
> | 1  | 0  | +     |
> | 1  | 2  | +     |
> | 2  | 2  | −     |
> | 3  | 3  | +     |
>
> Assume we use the KNN classification algorithm with K=3 on new data (1,1). Which class will this new data be predicted as?
>
> - solution: {@{+}@} <!--SR:!2028-10-02,1071,350-->

## _k_-means clustering

> Q1. Which of the following description about K-means clustering is correct?
>
> 1. K-means clustering is a supervised learning algorithm
> 2. K-means clustering makes prediction by majority voting
> 3. The "K" in K-means clustering refers to the number of data points
> 4. K-means clustering achieves categorization of data points
>
> - solution: {@{4}@} <!--SR:!2026-01-02,291,330-->

<!-- markdownlint MD028 -->

> Q2. Arrange the following steps in order for the first iteration of K-means clustering.
>
> 1. Calculate the distances between each centroids and each points
> 2. Label each point according to its closest centroid
> 3. Choose K random points to be the initial centroids
> 4. Recompute the centroids according to the labelling
>
> - solution: {@{3 → 1 → 2 → 4}@} <!--SR:!2025-12-31,288,330-->

<!-- markdownlint MD028 -->

> Q3. In an iteration of K-means clustering, the data points with coordinates (9,7), (9,2) and (7,9) are labelled as "Category 1". What is the new position of the centroid for "Category 1"?
>
> - solution: {@{\(25/3, 6\)}@} <!--SR:!2025-12-20,280,330-->

<!-- markdownlint MD028 -->

> Q4. Compute the centroid of N data points, each with 2 coordinates (stored in a NumPy array `data` of shape (N, 2)).
>
> Your code should be at most one or two lines, and it should not contain any loops.
>
> - solution: {@{`numpy.average(data, axis=0)`, `numpy.mean(data, axis=0)`}@} <!--SR:!2025-12-28,287,330-->

<!-- markdownlint MD028 -->

> Q5. Suppose you are doing K-means clustering on 4 data points. In the following array, the `[i, j]`-th entry represents the distance of `data[i]` to `centroid[j]`. How should you properly label the data points?
>
> ```Python
> array([[0.28, 0.69, 0.50],
>        [0.61, 0.34, 0.54],
>        [0.18, 0.44, 0.81],
>        [0.78, 0.15, 0.10]])
> ```
>
> - solution: {@{0, 1, 0, 2}@} <!--SR:!2029-04-04,1218,350-->

<!-- markdownlint MD028 -->

> Q6. Label the data point according to their closest centroid, using an 2D NumPy array `dists`. In `dists`, the `[i, j]`-th entry represents the distance of `data[i]` to `centroid[j]`.
>
> Your code should be at most one or two lines, and it should not contain any loops. Hint: look at the `numpy.argmin` function.
>
> - solution: {@{`numpy.argmin(dists, axis=1)`, `numpy.argmin(dists, axis=-1)`}@} <!--SR:!2028-12-28,1142,350-->

<!-- markdownlint MD028 -->

> Q7. Suppose you have the following array where each row represents a data point with 3 coordinate points. Compute the Euclidean distance between the points and the centroid with coordinates (0.4, 0.5, 0.6).
>
> ```Python
> array([[0.89, 0.07, 0.43],
>        [0.31, 0.75, 0.51],
>        [0.52, 0.68, 0.28],
>        [ 0.9, 0.59, 0.65]])
> ```
>
> - solution: {@{0.67372101, 0.2805352, 0.38626416, 0.51048996}@} <!--SR:!2025-12-29,288,330-->

<!-- markdownlint MD028 -->

> Q8. Computes the Euclidean distance between the data points and the given centroid. The data points are stored in a 2D NumPy array `data` of shape (N, 3) while the (single) centroid is stored in `centroid` of shape (3,).
>
> Your code should be at most one or two lines, and it should not contain any loops. Hint: reviewing the last question of the self test on Python Fundamentals might help :D
>
> - solution: {@{`numpy.sqrt(numpy.sum((data - centroid) ** 2, axis=-1))`, `numpy.sqrt(numpy.sum((data - centroid) ** 2, axis=1))`}@} <!--SR:!2028-03-10,884,330-->

<!-- markdownlint MD028 -->

> Q9. Can K-means clustering under Euclidean distance produce any kind of cluster shapes?
>
> - solution: {@{No. The shape needs to be circles or ellipsoids.}@} <!--SR:!2025-12-30,289,330-->

<!-- markdownlint MD028 -->

> Q10. Which of the following is a widely-used application for K-means clustering?
>
> 1. Handwritten digit recognition
> 2. Enemy AIs in video games
> 3. Chat bots
> 4. Customer segmentation
>
> - solution: {@{4}@}
> - explanation: {@{It is the closest to clustering...}@} <!--SR:!2029-01-16,1158,350!2026-01-01,290,330-->

<!-- markdownlint MD028 -->

> Q11. Determine whether each of the following statements about K-means clustering is correct. If it is correct, then give a brief explanation. If it is incorrect, try to come up with an counterexample.
>
> 1. The centroids in K-means clustering (using Euclidean distance) always converges.
> 2. K-means clustering performs quickly on large datasets.
> 3. K-means clustering always minimizes the sum of inter-cluster distance.
> 4. K-means clustering is deterministic - i.e. it always produces the same result on the same dataset.
>
> - solution: {@{1. true (false if not using Euclidean distance, but ignore this for exams) <br/> 2. true <br/> 3. false, not necessarily global minimum, only local minimum <br/> 4. false (assuming initial centroids are initialized randomly, which is usually the case)}@} <!--SR:!2025-12-20,280,330-->

<!-- markdownlint MD028 -->

> Q12. Which of the following is definitely NOT a necessary preprocessing step for K-means clustering?
>
> 1. Perform standardization on all the features
> 2. Try to handle and remove outliers
> 3. Perform principal component analysis (PCA)
> 4. Shuffle the dataset
>
> - solution: {@{4}@} <!--SR:!2029-01-14,1157,350-->

<!-- markdownlint MD028 -->

> Q13. Suppose we have the following one-dimensional dataset with 10 data points, and we want to perform K-means clustering with K=2. We choose our initial centroids as 0 and 1. What are the centroid positions after one iteration of K-means clustering?
>
> ```Python
> array([0.02, 0.93, 0.45, 0.7, 0.41, 0.78, 0.03, 0.52, 0.59, 0.53])
> ```
>
> - solution: {@{centroid 0: \(0.02 + 0.45 + 0.41 + 0.03\)/4 = 0.2275 <br/> centroid 1: \(0.93 + 0.7 + 0.78 + 0.52 + 0.59 + 0.53\)/6 = 0.675}@} <!--SR:!2025-12-24,284,330-->

<!-- markdownlint MD028 -->

> Q14. We have _N_ data points each with _d_ features. Given a 2D array `data` of shape \(_N_, _d_\) and a 2D array `centroids` of shape \(_k_, _d_\), compute the new centroids using Euclidean distance.
>
> Try to not use any explicit Python loops. The solution below has 4 lines.
>
> - solution: <p> {@{`squared_dists = numpy.sum((centroids[..., numpy.newaxis, :] - data) ** 2, axis=-1)` <br/> `mins = numpy.argmin(squared_dists, axis=-2)` <br/> `min_mask = numpy.arange(len(centroids))[..., numpy.newaxis] == mins` <br/> `centroids = numpy.mean(numpy.repeat(data[numpy.newaxis, ...], len(centroids), axis=0), axis=-2, where=min_mask[..., numpy.newaxis])` <p> Note: This code will result in `nan`s if some centroids have no data points assigned to it. See if you can figure out a solution yourself...}@} <!--SR:!2027-07-03,632,310-->

## perceptron

> Q1. Which of the following statements is/are true about a perceptron?
>
> 1. It can only be used for linearly separable data (ignoring regression).
> 2. It should have exactly two inputs and one output.
> 3. One similarity between perceptron and KNN is that they both include learnable parameters.
> 4. Every parameter must be updated during an epoch.
>
> - solution: {@{1}@}
> - explanation: {@{Even if the activation function is nonlinear, the input to the activation function is linear. Unless you are doing regression, otherwise the nonlinear activation function cannot magically make the classification nonlinear.}@} <!--SR:!2029-01-15,1157,350!2025-12-26,285,330-->

<!-- markdownlint MD028 -->

> Q2. Which of the followings is/are true about a perceptron?
>
> 1. It belongs to an unsupervised learning algorithm.
> 2. It can be mathematically modeled as a vector dot product.
> 3. Its output is equivalent to the direct result of a weighted sum of the inputs plus a bias.
> 4. For a perceptron with n inputs and 1 output, there should be n+1 parameters, including bias.
>
> - solution: {@{2, 4}@} <!--SR:!2025-12-18,278,330-->

<!-- markdownlint MD028 -->

> Q3. Suppose we have a dataset with many data points, each with N features. Each feature is either positive (with value 1) or negative (with value -1). We say a data point is "positive" if it has more positive features than negative features, and "negative" otherwise. Design the weights, bias and activation function of a perceptron to classify positive data points from negative data points.
>
> - solution: {@{Actually you do not need to tune the weights and biases: leave the former at 1 and the latter at 0. Simply tune the activation function to behave as described above.}@} <!--SR:!2028-02-13,864,330-->

<!-- markdownlint MD028 -->

> Q4. Which of the following can be considered as hyperparameters for a perceptron?
>
> 1. choice of activation function
> 2. choice of learning rate
> 3. choice of having a bias term or not
> 4. choice of the number of inputs
>
> - solution: {@{1, 2, 3}@} <!--SR:!2025-12-28,287,330-->

<!-- markdownlint MD028 -->

> Q5. Suppose we use perceptron to learn on K training samples where each sample is represented in n-dimensional space. We stopped training after e epochs. How many arithmetic operations were done during training? Express it in terms of K, e and n. (arithmetic operations include both multiplication and addition, ignore the operations for parameter update and the operations in the activation function)
>
> - solution: {@{2eKn (remember to include the bias addition)}@} <!--SR:!2027-06-22,627,310-->

<!-- markdownlint MD028 -->

> Q6. You are given a perceptron with 2 inputs, and weight w = [1, 1] and bias = 2; the chosen activation function is the step function, where it returns 1 when x > 0 and 0 otherwise. Which of the following perceptron configurations have the same decision plane as the given perceptron?
>
> 1. w = [0.5, 0.5], bias = 1
> 2. w = [100, 100], bias = 200
> 3. w = [1, 1], bias = sqrt(2)
> 4. w = [-1, -1], bias = -2
>
> - solution: {@{1, 2, 4}@}
> - explanation: {@{Check if the weights and biases can be scaled together to get the original perceptron.}@} <!--SR:!2029-04-29,1237,350!2029-01-08,1151,350-->

<!-- markdownlint MD028 -->

> Q7. You are given the same perceptron as in the previous question. Which of the following perceptron configurations produce the same classification effect as the given perceptron?
>
> 1. w = [0.5, 0.5], bias = 1
> 2. w = [100, 100], bias = 200
> 3. w = [1, 1], bias = sqrt(2)
> 4. w = [-1, -1], bias = -2
>
> - solution: {@{1, 2}@}
> - explanation: {@{First, check if the decision boundary is the same, which is the same as the previous question. Second, check if the resulting classification is the same for the same side of the decision boundary. <p> 4 has the classification flipped because it has its parameters scaled by a negative number.}@} <!--SR:!2028-08-20,1036,350!2029-05-02,1240,350-->

## multilayer perceptron

> Q1. Which of the followings is/are true about MLP?
>
> 1. We can use MLP to classify data that is NOT linearly separable regardless of the number of layers and choice of the activation function. (Hint: Why is "regardless of" here?)
> 2. A deeper network guarantees better performance than shallow networks.
> 3. MLP is a feed-forward neural network designed to work exactly as human brains learn.
> 4. To use MLP for supervised learning, we always need to apply a suitable loss function at the end of the network.
>
> - solution: {@{4}@} <!--SR:!2029-04-28,1236,350-->

<!-- markdownlint MD028 -->

> Q2. Which of the followings is/are true about activation functions?
>
> 1. Both linear and non-linear activation functions are practical choices for MLP in real-world applications.
> 2. ReLU is generally a good choice of activation function for the final layer of the image classification problem.
> 3. Activation functions have to be continuous and differentiable at every point.
> 4. One problem with the sigmoid activation functions is that it may cause a vanishing gradient problem in the saturation zone.
>
> - solution: {@{4}@} <!--SR:!2026-01-05,294,330-->

<!-- markdownlint MD028 -->

> Q3. Suppose we have a Multi-Layer-Perceptron, those inputs are NumPy arrays of shape (32, 32) (unbatched shape), with the following structure summary. What is the total number of parameters in the network, including bias?
>
> ```shell
> _________________________________________________________________
>  Layer (type)                Output Shape              Param #
> =================================================================
>  flatten (Flatten)           (None, ????)
>
>  Layer_1 (Dense)             (None, 4096)
>
>  Layer_2 (Dense)             (None, 4096)
>
>  Layer_3 (Dense)             (None, 4096)
>
>  Layer_4 (Dense)             (None, 4096)
>
>  Layer_5 (Dense)             (None, 10)
>
> =================================================================
> Total params: ????????
> Trainable params:
> Non-trainable params:
> _________________________________________________________________
> ```
>
> - solution: {@{`flatten` → `Layer_1`: (32 \* 32) \* 4096 + 4096 = 4198400 <br/> `Layer_1` → `Layer_2`, `Layer_2` → `Layer_3`, `Layer_3` → `Layer_4`: 4096 \* 4096 + 4096 = 16781312 (for each in between layers) <br/> `Layer_4` → `Layer_5`: 4096 \* 10 + 10 = 40970 <br/> total params: 4198400 + 16781312 \* 3 + 40970 = 54583306}@} <!--SR:!2027-03-05,552,310-->

<!-- markdownlint MD028 -->

> Q4. Read the following code in python, which builds an MLP using the Keras library. What is the number of parameters in this network?
>
> ```Python
> from keras.models import Sequential
> from keras.layers import Dense, Dropout
> model = Sequential()
> model.add(Dense(1000, input_shape = (500,), activation='ReLU'))
> model.add(Dropout(0.6))
> model.add(Dense(400, activation='ReLU'))
> model.add(Dropout(0.6))
> model.add(Dense(10, activation='sigmoid'))
> ```
>
> - solution: {@{`Dropout(...)` can be ignored since they have no parameters. <br/> input → `Dense(1000, ...)`: 500 \* 1000 + 1000 = 501000 <br/> `Dense(1000, ...)` → `Dense(400, ...)`: 1000 \* 400 + 400 = 400400 <br/> `Dense(400, ...)` → `Dense(10, ...)`: 400 \* 10 + 10 = 4010 <br/> total params: 501000 + 400400 + 4010 = 905410}@} <!--SR:!2026-08-10,435,310-->

<!-- markdownlint MD028 -->

> Q5. Explain why activation functions have to be non-linear.
>
> - solution: {@{A MLP without activation functions is a linear transformation, so it can only separate linearly separable data. Activation functions are designed to make this not the case. However, if the activation function is linear, then the MLP is still a linear transformation, which defeats the purpose of activation functions. So they have to nonlinear for them to be useful in practice.}@} <!--SR:!2029-01-06,1150,350-->

<!-- markdownlint MD028 -->

> Q6. Which of the following is/are TRUE about back-propagation?
>
> 1. It transmits loss back through the network to adjust the inputs.
> 2. It transmits loss back through the network to adjust the weights.
> 3. It is based on the recursive use of the chain rule.
> 4. It is based on the recursive use of the Leibniz integral rule.
>
> - solution: {@{2, 3}@}
> - explanation: {@{Theoretically, you could do 1 for adversarial machine learning... an example is finding "bad" inputs (that look mostly indistinguishable to the original input) that cause the network to produce any classification you desire. And 4 is something completely unrelated...}@} <!--SR:!2026-01-04,293,330!2026-01-01,289,330-->

<!-- markdownlint MD028 -->

> Q7. Which of the followings is/are TRUE about over-fitting?
>
> 1. Over-fitting is a phenomenon when the network is too adapted to the training data and cannot generalize well to unseen test data.
> 2. Over-fitting is a phenomenon when the network performs too well on the test data such that the experimental results can not be correctly justified and hence make the model not reliable and trustworthy.
> 3. Considering from the point of view of the hyperplane for classification, overfitted models tend to have a more curvatured decision boundary than well-fitted model.
> 4. Considering from the point of view of the hyperplane for classification, overfitted models tend to have a less curvatured decision boundary than well-fitted model.
>
> - solution: {@{1, 3}@} <!--SR:!2029-03-31,1215,350-->

<!-- markdownlint MD028 -->

> Q8. Which of the followings is/are FALSE about avoiding over-fitting?
>
> 1. Reducing the number of layers in the network can help avoid over-fitting.
> 2. Adding a regularization term in the loss function can help avoid over-fitting.
> 3. Reducing the number of training data can help avoid over-fitting.
> 4. Reducing the number of training epochs can help avoid over-fitting.
>
> - solution: {@{3}@} <!--SR:!2027-10-15,783,330-->

<!-- markdownlint MD028 -->

> Q9. Suppose you built an MLP network to do binary classification, there is only one neuron in the last layer and say its output is z. the final output of your network y is given by:
>
> y = sigmoid(ReLU(z))
>
> You classify all inputs with a final value y >= 0.5 as positive. What is the problem with this network?
>
> - solution: {@{y is always >= 0.5, so the classification is always positive.}@} <!--SR:!2028-11-13,1106,350-->

<!-- markdownlint MD028 -->

> Q10. Perform backpropagation on the following equations to find $\frac {\partial e} {\partial a}$ and $\frac {\partial e} {\partial b}$.
>
> - $a = 2$
> - $b = 5$
> - $c = a \cdot b$
> - $d = b + 1$
> - $e = c \cdot d$
>
> Hint: Draw a graph of the above equations. Track the dependencies.
>
> - solution: {@{$$\begin{aligned} \frac {\partial e} {\partial a} & = \frac {\partial e} {\partial c} \frac {\partial c} {\partial a} = d \cdot b = (b + 1) \cdot b = 30 \\ \frac {\partial e} {\partial b} & = \frac {\partial e} {\partial c} \frac {\partial c} {\partial b} + \frac {\partial e} {\partial d} \frac {\partial d} {\partial b} = d \cdot a + c \cdot 1 = (b + 1) \cdot a + (a \cdot b) = 22 \end{aligned}$$}@} <!--SR:!2029-01-25,1165,350-->

<!-- markdownlint MD028 -->

> Q11. Given a MLP with all weights and biases set to 0 and all activation functions set to the sigmoid function, find its output.
>
> - solution: {@{0.5}@} <!--SR:!2028-08-25,1040,350-->

<!-- markdownlint MD028 -->

> Q12. Consider an MLP network with one input layer, one hidden layer and one output layer. The activation function for the output layer is softmax (to be followed with cross-entropy loss), and the activation function for the hidden layer is the step function. Please explain whether there will be a problem if we train this network using gradient descent and why.
>
> - solution: {@{The activation function, the step function, for the hidden layer has a derivative of 0 at every point it is defined (henceforth, assume the derivative is 0, even for the point where the derivative is undefined). So the calculated gradient for the hidden layer is always 0 no matter how large the error output is. Gradient descent never updates their weights.}@} <!--SR:!2028-12-25,1141,350-->

<!-- markdownlint MD028 -->

> Q13. Which of the followings is/are TRUE about weight updating during back-propagation?
>
> 1. Usually, the weights are initially set to 0
> 2. The updates are proportional to the loss
> 3. The updates are proportional to the output of the weight layer
> 4. The output layer weights are used when computing the loss of the hidden layer
>
> - solution: {@{2, 4}@} <!--SR:!2027-05-17,669,330-->

## digital image processing fundamentals

> Q1. (simple) An image has dimensions 100×200. What is the image coordinate of the bottom-right most pixel?
>
> 1. (100, 200)
> 2. (200, 100)
> 3. (99, 199)
> 4. (199, 99)
>
> - solution: {@{3}@}
> - explanation: {@{I mean... it is just a convention. It could be any other convention, depending on your context. <p> This convention is used in libraries processing images with NumPy arrays. So that explains why it is 0-based.}@} <!--SR:!2028-11-12,1105,350!2025-12-13,276,330-->

<!-- markdownlint MD028 -->

> Q2. (simple) Let $I$ be the pixel intensity for a pixel of a grayscale image. Consider applying the following operation to each pixel: $$I_\text{new} = \operatorname{floor}(0.5 \times I_{\text{old} })$$
>
> Which of the following is correct?
>
> 1. The resulting image will be pure black everywhere.
> 2. The resulting image will be darker.
> 3. The resulting image will be brighter.
> 4. No image can be formed.
>
> - solution: {@{2}@} <!--SR:!2025-12-27,286,330-->

<!-- markdownlint MD028 -->

> Q3. (medium) Let $P(x, y)$ denote the pixel intensity value at the image coordinate $(x, y)$. After applying the following transformation, the new pixel intensity at location $(x, y)$, denoted $P_{\text{new} }(x, y)$, is given by $$P_\text{new}(x, y) = P \left( \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix} \right) \,.$$
>
> Describe in words what transformation was applied.
>
> - solution: {@{The image is translated to the left (not right) and upwards (not downwards) each by 1 pixel.}@}
> - explanation: {@{While the transformation matrix describes a transformation to the right and downwards each by 1 pixel, notice that it is applied to the input coordinates instead of the output coordinates. <p> In general, the transformations are reversed if you apply it to the input coordinates instead of the output coordinates. For a simple example, consider $f(x) = x$. Then compare between $f_{\text{new} }(x) = f(x) + 1 = x + 1$ and $f_{\text{new} }(x + 1) = f(x) = x \implies f_{\text{new} }(x) = f(x - 1) = x - 1$.}@} <!--SR:!2027-10-25,763,310!2026-06-05,394,310-->

<!-- markdownlint MD028 -->

> Q4. (medium) Consider the following 3 by 3 grayscale image, where $\times$ represents an unknown pixel intensity.
>
> $$\begin{array}{|c|c|c|}
>    \hline
>    \times & \times & \times \\ \hline
>    \times & 4      & \times \\ \hline
>    \times & \times & \times \\ \hline
>    \end{array}$$
>
> A __constant padding__ (with width 2 on each side) is applied. The intensity values at some pixels of the resulting image are shown below.
>
> $$\begin{array}{|c|c|c|c|c|c|c|}
>    \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & 0               & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & 0               & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & 4               & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & 0               & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \end{array}$$
>
> For each pixel, fill in the missing pixel intensity or mark the cell with a $\times$ if the pixel intensity cannot be determined.
>
> - solution: {@{$$\begin{array}{|c|c|c|c|c|c|c|} \hline 0 & 0 & 0      & 0      & 0      & 0 & 0 \\ \hline 0 & 0 & 0      & 0      & 0      & 0 & 0 \\ \hline 0 & 0 & \times & \times & \times & 0 & 0 \\ \hline 0 & 0 & \times & 4      & \times & 0 & 0 \\ \hline 0 & 0 & \times & \times & \times & 0 & 0 \\ \hline 0 & 0 & 0      & 0      & 0      & 0 & 0 \\ \hline 0 & 0 & 0      & 0      & 0      & 0 & 0 \\ \hline \end{array}$$}@} <!--SR:!2029-03-26,1211,350-->

<!-- markdownlint MD028 -->

> Q5. (advanced) Consider the following 3 by 3 grayscale image, where $\times$ represents an unknown pixel intensity.
>
> $$\begin{array}{|c|c|c|}
>    \hline
>    \times & \times & \times \\ \hline
>    \times & 8      & 3      \\ \hline
>    \times & \times & \times \\ \hline
>    \end{array}$$
>
> A __reflection padding__ (with width 2 on each side) is applied. The intensity values at some pixels of the resulting image are shown below.
>
> $$\begin{array}{|c|c|c|c|c|c|c|}
>    \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & 9               & \hspace{0.25cm} & 5               & 4               & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & 8               & 3               & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & 9               & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \end{array}$$
>
> For each pixel, fill in the missing pixel intensity or mark the cell with a $\times$ if the pixel intensity cannot be determined.
>
> - solution: {@{$$\begin{array}{|c|c|c|c|c|c|c|} \hline 8      & \times & \times & 8      & 3      & 3      & 8      \\ \hline 5      & 9      & 9      & 5      & 4      & 4      & 5      \\ \hline 5      & 9      & 9      & 5      & 4      & 4      & 5      \\ \hline 8      & \times & \times & 8      & 3      & 3      & 8      \\ \hline \times & 9      & 9      & \times & \times & \times & \times \\ \hline \times & 9      & 9      & \times & \times & \times & \times \\ \hline 8      & \times & \times & 8      & 3      & 3      & 8      \\ \hline \end{array}$$}@} <!--SR:!2027-08-23,731,330-->

<!-- markdownlint MD028 -->

> Q6. (medium) Consider the following 3 by 3 grayscale image, where $\times$ represents an unknown pixel intensity.
>
> $$\begin{array}{|c|c|c|}
>    \hline
>    \times & \times & \times \\ \hline
>    \times & \times & 9      \\ \hline
>    \times & 6      & \times \\ \hline
>    \end{array}$$
>
> A replication padding (with width 2 on each side) is applied. The intensity values at some pixels of the resulting image are shown below.
>
> $$\begin{array}{|c|c|c|c|c|c|c|}
>    \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    4               & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & 5               & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & 9               & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & 6               & \hspace{0.25cm} & 7               & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} & \hspace{0.25cm} \\ \hline
>    \end{array}$$
>
> For each pixel, fill in the missing pixel intensity or mark the cell with a $\times$ if the pixel intensity cannot be determined.
>
> - solution: {@{$$\begin{array}{|c|c|c|c|c|c|c|} \hline 4      & 4      & 4      & \times & 5 & 5 & 5 \\ \hline 4      & 4      & 4      & \times & 5 & 5 & 5 \\ \hline 4      & 4      & 4      & \times & 5 & 5 & 5 \\ \hline \times & \times & \times & \times & 9 & 9 & 9 \\ \hline \times & \times & \times & 6      & 7 & 7 & 7 \\ \hline \times & \times & \times & 6      & 7 & 7 & 7 \\ \hline \times & \times & \times & 6      & 7 & 7 & 7 \\ \hline \end{array}$$}@} <!--SR:!2025-12-12,275,330-->

<!-- markdownlint MD028 -->

> Q7. (medium) Consider the following grayscale image.
>
> $$\begin{array}{|c|c|c|}
>      \hline
>      0   & 247 & 186 \\ \hline
>      247 & 196 & 210 \\ \hline
>      198 & 196 & 255 \\ \hline
>     \end{array}$$
>
> For each pixel intensity value $I$, the following algorithm is applied. $$I_{\text{new} } = \text{floor} \left( \frac{ I-I_{\text{min} } }{I_{\text{max} }-I_{\text{min} } } \times 255 \right)$$
>
> 1. Write down the resulting pixel intensities at each coordinate.
> 2. Desmond is not satisfied with the above algorithm. Name another algorithm which can produce better results.
>
> - solution: {@{For 1, the image remains unchanged. <p> For 2, we can use histogram equalization instead of contrast stretching as used here.}@} <!--SR:!2028-12-10,1128,350-->

<!-- markdownlint MD028 -->

> Q8. (medium) Describe the effect of gamma correction on an image with $\gamma < 1$.
>
> Note: Without context, $\gamma$ as described above is most likely the _decoding value_, but we are doing _encoding_. One could argue this is confusing, but this is the current convention (unfortunately).
>
> - solution: {@{The image becomes darker.}@} <!--SR:!2027-01-21,557,310-->

<!-- markdownlint MD028 -->

> Q9. (medium) Image thresholding is applied to an RGB image with threshold 0. Which of the following best describes the resulting image?
>
> 1. The resulting image is pure black everywhere.
> 2. The resulting image is pure white everywhere.
> 3. The resulting image is the same as the original image.
> 4. The resulting image consists of pure black and pure white, and no other colors.
>
> - solution: {@{2}@}
> - explanation: {@{This depends on your definition of the threshold function. The threshold function used in this course is 255 if larger than or _equal to_ the threshold.}@} <!--SR:!2025-12-24,284,330!2026-12-10,526,310-->

<!-- markdownlint MD028 -->

> Q10. (simple) What is the advantage of using Otsu's <!-- osu!: Haha Hehe Desmond GOOD guy --> method for image thresholding compared to the regular image thresholding algorithm?
>
> - solution: {@{The result is reproducible.}@} <!--SR:!2025-12-25,285,330-->

## convolutional neural network

> Q1. Which of the followings is/are TRUE about the convolutional layer in CNN?
>
> 1. The number of weights depends on the depth of the input volume.
> 2. The number of biases is equal to the number of filters.
> 3. The total number of parameters depends on the stride.
> 4. The total number of parameters depends on the padding.
>
> - solution: {@{1, 2}@} <!--SR:!2028-01-23,849,330-->

<!-- markdownlint MD028 -->

> Q2. Which of the following statements claims certain advantages of convolutional layers compared to dense layers in computer vision tasks is/are TRUE?
>
> 1. Convolution itself is a non-linear operation and brings more non-linearity and stronger expressiveness to the network.
> 2. Convolutional layers usually have more parameters compared to dense layers assuming the same input; hence it has stronger expressiveness.
> 3. Convolution preserves spatial context while dense layers will lose spatial context by flattening everything.
> 4. Convolutional layers are more similar to how the human visual system works, where different areas of the brain are activated by different levels of features.
>
> - solution: {@{3, 4}@} <!--SR:!2025-12-12,275,330-->

<!-- markdownlint MD028 -->

> Q3. Suppose we have a conventional CNN architecture: input 32\*32\*3 RGB image, first convolutional layer has 256 3\*3 filters, followed by a 2\*2 (non-overlapping) max pooling layer, followed by convolutional layer with 128 3\*3 filters, followed by another 2\*2 (non-overlapping) max pooling layer, followed by convolutional layer with 64 3\*3 filters, then a 2\*2 (non-overlapping) max pooling layer, then a flattening layer, a dense layer with 1000 neurons, and output layer with 10 neurons. What is the total number of parameters in the network, including bias, assuming no padding is done for any convolutional layer?
>
> - solution: {@{input shape to flattening layer: 32\*32\*3 → 30\*30\*256 → 15\*15\*256 → 13\*13\*128 → 6\*6\*128 → 4\*4\*64 → 2\*2\*64 <br/> total params: (3\*3\*3 \* 256 + 256) + (3\*3\*256 \* 128 + 128) + (3\*3\*128 \* 64 + 64) + (2\*2\*64 \* 1000 + 1000) + (1000 \* 10 + 10) = 643010}@} <!--SR:!2028-03-16,888,330-->

<!-- markdownlint MD028 -->

> Q4. You are given a dataset of 10×10 grayscale images. Your goal is to build a classifier that will classify all images into 5 classes. You decide to choose one approach from MLP and CNN:
>
> 1. __MLP configuration__: the input is flattened into a 100-dimensional vector, followed by a fully-connected layer with 5 neurons
> 2. __CNN configuration__: the input is directly given to a convolutional layer with five 10×10 filters
>
> Explain which method is better and why?
>
> - solution: {@{Actually they are the same thing. The mathematical operations are the same.}@} <!--SR:!2029-05-01,1239,350-->

<!-- markdownlint MD028 -->

> Q5. The ImageNet competition was launched in 2010. Before 2012, image features were commonly manually engineered. In 2012, AlexNet used convolutional layers to significantly improve its performance, and CNNs became popular.
>
> Explain why CNNs can improve performance on image classification.
>
> - solution: {@{(for reference) Convolutional layers automates feature engineering on a large scale and are likely much better than humans at extracting image features.}@} <!--SR:!2025-12-27,286,330-->

<!-- markdownlint MD028 -->

> Q6. Which of the followings is/are FALSE about pooling layers?
>
> 1. It is used to reduce the size of the feature maps so that it speeds up the computation of the network.
> 2. It is applied after convolution and ReLU (activation functions attached to convolutional layers) operations.
> 3. It is not a differentiable operation.
> 4. The number of learnable parameters in a pooling layer is the same as the filter size.
>
> - solution: {@{3, 4}@} <!--SR:!2029-03-30,1214,350-->

<!-- markdownlint MD028 -->

> Q7. Name 3 hyperparameters in pooling layers.
>
> - solution: {@{pooling operation, pool size, stride}@} <!--SR:!2028-10-19,1086,350-->

<!-- markdownlint MD028 -->

> Q8. Which of the followings is/are FALSE about the idea of the dropout?
>
> 1. The dropout rate p is a hyperparameter to be considered when designing the model.
> 2. It is designed as a way to avoid over-fitting.
> 3. A dropout rate of 0.5 means half of the neuron output will be set to 0.
> 4. The higher the dropout rate, the better the model performance.
>
> - solution: {@{3, 4}@}
> - explanation: {@{For 3, the implementation of dropout in Keras (by extension, TensorFlow) uses a random mask, which is not guaranteed to turn off 50% of neurons. Theoretically, its randomness could mean none of the neurons are turned off. Other libraries may use a different implementation (e.g. guaranteeing 50% of the neurons are turned off), but ignore this for the examinations. <p> This is likely tested in the examinations...}@} <!--SR:!2028-09-02,1047,350!2029-01-13,1155,350-->

## minimax & alpha–beta pruning

> Q1. Which of the following games can we (theoretically) apply minimax to?
>
> 1. Monopoly
> 2. Connect 4
> 3. Poker
> 4. Contract bridge
>
> - solution: {@{2}@}
> - explanation: {@{The minimax algorithm as taught in the course only applies to deterministic, perfect information, and zero-sum games. <p> There may be extensions of minimax algorithm that apply to more games, but ignore this for the examinations...}@} <!--SR:!2028-09-08,1051,350!2027-12-30,791,330-->

<!-- markdownlint MD028 -->

> Q2. Which of the following tree-search algorithms is minimax based on?
>
> 1. breadth-first search
> 2. depth-first search
> 3. Dijkstra's
> 4. Bellman-Ford
>
> - solution: {@{2}@} <!--SR:!2029-05-04,1242,350-->

<!-- markdownlint MD028 -->

> Q3. Determine whether each of the following statements is true or false.
>
> 1. We should apply minimax on Black Jack.
> 2. We should apply minimax on Chinese Chess.
> 3. Alpha–beta pruning is guaranteed to speed up the minimax algorithm.
> 4. We can use GPU to speed up the minimax algorithm.
>
> - solution: {@{1. false, not perfect information <br/> 2. false, theoretically possible, but practically too many nodes in the game tree <br/> 3. false <br/> 4. false, because GPUs are only good at matrix multiplication (Actually, true would also make sense, considering GPGPUs (general-purpose graphical processing units)...)}@} <!--SR:!2026-01-02,291,330-->

## ethics of artificial intelligence

> Q1. Match the European Union Principles with the given Common Grounds by completing the following table with numbers.
>
> __Seven European Union Principles__
>
> 1. human agency and oversight
> 2. technical robustness and safety
> 3. privacy and data governance
> 4. transparency
> 5. diversity, non-discrimination and fairness
> 6. societal and environmental well-being
> 7. accountability
>
> __Common Grounds__
>
> 1. autonomy
> 2. beneficence
> 3. non-maleficence
> 4. justice
> 5. explicability
>
> - solution: {@{1, 3, 1, 5, 4, 2, 1}@} <!--SR:!2026-04-04,127,250-->

<!-- markdownlint MD028 -->

> Q2. (simple) Which of the following are potential harms that AI systems may cause?
>
> 1. Obtaining people's personal information without their consent.
> 2. Producing wrong predictions due to model implementation issues.
> 3. Obscuring the legal responsibilities.
>
> - solution: {@{1, 2, 3}@} <!--SR:!2028-11-09,1103,350-->

<!-- markdownlint MD028 -->

> Q3. (simple) Which of the following is NOT one of the 5 fundamental principles of AI as mentioned in the lectures?
>
> 1. Autonomy
> 2. Justice
> 3. Non-maleficence
> 4. Benevolence
>
> - solution: {@{4}@} <!--SR:!2029-05-11,1248,350-->

<!-- markdownlint MD028 -->

> Q4. (medium) One of the problems with setting principles for AI is that the principles may conflict with each other. With regards to the collection of healthcare data, which 2 principles have a conflict?
>
> - solution: {@{__Autonomy__ and __beneficence__. The former says people should have control over their use of data, but people not agreeing to their data being used means healthcare models based on said healthcare data is less accurate, which harms the society.}@} <!--SR:!2028-12-29,1143,350-->

<!-- markdownlint MD028 -->

> Q5. (medium) State __two__ ways to reduce the chances of introducing an unfair bias in an AI system.
>
> - solution: {@{(for reference) Ensure the training data used for the model is free from bias. <br/> Performing regular tests and audits. <br/> Ensure that the training data includes some samples from minority groups.}@} <!--SR:!2029-03-01,1191,350-->

<!-- markdownlint MD028 -->

> Q6. (medium) State __one__ advantage and __one__ disadvantage of using AI systems for resume screening.
>
> - solution: {@{(for reference) Advantages are it increases productivity and is cheaper for companies. <p> Disadvantages are it may be biased based on gender or biased against minorities. There is also a lack of transparency (on why a person is hired or not hired).}@} <!--SR:!2025-12-12,275,330-->

## introduction to reinforcement learning

> Q1. Which of the following are components of reinforced learning?
>
> 1. Actions
> 2. Testing data
> 3. Training data
>
> - solution: {@{1}@}
> - explanation: {@{The 6 (major) components are agent, environment, observations, actions, rewards, and policy.}@} <!--SR:!2028-11-21,1113,350!2027-03-15,567,310-->

<!-- markdownlint MD028 -->

> Q2. (medium) An animal trainer is trying to train a monkey to perform tricks in a circus. Give an example of what each of the following 6 components may refer to in training the monkey.
>
> 1. Agent
> 2. Environment
> 3. Observations
> 4. Actions
> 5. Rewards
> 6. Policy
>
> - solution: {@{1. the monkey <br/> 2. circus/training room <br/> 3. what the monkey observes <br/> 4. tricks performable by the monkey <br/> 5. food <br/> 6. a way to perform tricks as to get the most food (which, to the trainer, means a way to perform tricks elegantly)}@} <!--SR:!2027-01-29,485,270-->

<!-- markdownlint MD028 -->

> Q3. (simple) Which of the following describes a Markov chain?
>
> 1. The future is independent of the past, given the present.
> 2. The present captures information about the future.
> 3. Once the present is known, history may be thrown away.
>
> - solution: {@{1, 3}@} <!--SR:!2028-11-27,1118,350-->

<!-- markdownlint MD028 -->

> Q4. (medium) Consider a Markov chain with processes $X_0, X_1, X_2, \cdots$. Match each term with each definition.
>
> 1. __definition 1__: the value of $X_t$.
> 2. __definition 2__: the set of values that each $X_t$ can take.
> 3. __definition 3__: a particular set of values for $X_0, X_1, X_2, \cdots$.
>
> <!-- list separator -->
>
> 1. The __trajectory__ (also called __path__) of a Markov chain is...
> 2. The __state__ of a Markov chain at time $t$ is...
> 3. The __state space__ of a Markov chain is...
>
> - solution: {@{1. definition 3 <br/> 2. definition 1 <br/> 3. definition 2}@} <!--SR:!2025-12-30,289,330-->

<!-- markdownlint MD028 -->

> Q5. (medium) Consider a Markov chain with processes $X_0, X_1, X_2, \cdots$. Which of the following is correct?
>
> 1. $X_0$ is a probability.
> 2. $X_0$ is a random variable.
> 3. $X_0$ is an event.
> 4. $X_0$ is a state.
> 5. None of the above.
>
> - solution: {@{2}@} <!--SR:!2029-03-24,1209,350-->

<!-- markdownlint MD028 -->

> Q6. (medium) Consider a Markov chain with processes $X_0, X_1, X_2, \cdots, X_N$ and states $S_0, S_1, S_2, \cdots, S_N$. Which of the following must be correct?
>
> 1. $P(X_0=S_0)>0$
> 2. $P(X_0=S_0) + P(X_1=S_1) + \cdots + P(X_N = S_N) = 1$
> 3. $P(X_0=S_0) + P(X_1=S_0) + \cdots + P(X_N = S_0) = 1$
> 4. $P(X_0=S_0) + P(X_0=S_1) + \cdots + P(X_0 = S_N) = 1$
>
> - solution: {@{4}@} <!--SR:!2028-10-01,1071,350-->

<!-- markdownlint MD028 -->

> Q7. (medium) Let $X_0, X_1, X_2, \cdots$ be the processes of a Markov chain with a state space $S_0, S_1, S_2, \cdots, S_N$. A student makes the following claim regarding Markov chains.
>
> > In general, $P(X_t = S_0)$ is independent of the values the previous processes $X_1, X_2, \cdots, X_{t-1}$ take.
>
> Do you agree with the student's claim? Justify your answer.
>
> - solution: {@{No. <p> For a Markov chain, the state at time $t$ is independent of the values previous processes $X_1, X_2, \cdots, X_{t - 2}$ take. But it _may_ (or _may not_) depend on $X_{t - 1}$.}@} <!--SR:!2025-12-19,279,330-->

<!-- markdownlint MD028 -->

> Q8. (medium) A student makes the following claim regarding Markov chains.
>
> > In general, each state should only occur at most once.
>
> Using the definition of a Markov chain, justify or refute the student's claim.
>
> - solution: {@{No. <p> Simply consider a Markov chain with 1 state that always transit back to itself. Or consider that one can run a Markov chain infinitely many times, but a Markov chain (usually) has finitely many states, so by the pigeonhole principle, at least one state must repeat itself.}@} <!--SR:!2029-04-27,1235,350-->

<!-- markdownlint MD028 -->

> Q9. (advanced) Suppose a prize box contains five 1-dollar coins, five 2-dollar coins, and five 5-dollar coins. Coins are drawn one by one from the prize box. Let $$\begin{align*}
>     X_k &= \text{ the total amount drawn from the box after the }k^{\text{th} } \text{ draw} \\
>     M &= \text{ the sequence } \{ X_0, X_1, X_2, \cdots, X_{15} \}
>    \end{align*}$$
>
> For example, if the first coin drawn is a 5-dollar coin, we would have $X_0=0, X_1 = 5$.
>
> Is $M$ a Markov chain? Explain your answer.
>
> - solution: {@{No. <p> The key is to realize that knowing the entire state history (in this case, which additionally allows us to know how many of each coin has been drawn) allows us to make better predictions than knowing only the current state.}@} <!--SR:!2025-12-31,290,330-->

<!-- markdownlint MD028 -->

> Q10. (advanced) Suppose a prize box contains five 1-dollar coins, five 2-dollar coins, and five 5-dollar coins. Coins are drawn one by one from the prize box. Let $$\begin{align*}
>     X_k &= \text{ a tuple } (a, b, c) \text{, where } \\
>     a &= \text{ the total number of 1-dollar coins drawn after the } k^{\text{th} } \text{ draw} \\
>     b &= \text{ the total number of 2-dollar coins drawn after the } k^{\text{th} } \text{ draw} \\
>     c &= \text{ the total number of 5-dollar coins drawn after the } k^{\text{th} } \text{ draw} \\
>     M &= \text{ the sequence } \{ X_0, X_1, X_2, \cdots, X_{15} \}
>    \end{align*}$$
>
> For example, if we draw a 5-dollar coin followed by another 5-dollar coin, we would have $X_0=(0, 0, 0), X_1 = (0, 0, 1), X_2 = (0, 0, 2)$.
>
> Is $M$ a Markov chain? Explain your answer.
>
> - solution: {@{Yes. <p> The key is to realize that knowing the entire state history does not allow us to make better predictions than knowing only the current state. The key difference from the previous question is that the entire state history in the context of the previous Markov chain is encoded as the current state in the context of this Markov chain.}@} <!--SR:!2029-02-15,1180,350-->

<!-- markdownlint MD028 -->

> Q11. (simple) True or false: A transition probability matrix in a Markov chain must be a square matrix.
>
> - solution: {@{true}@}
> - explanation: {@{While technically you could have a non-square matrix, it would not be useful in practice, especially when you want to run the Markov chain multiple times.}@} <!--SR:!2029-02-06,1173,350!2025-12-23,283,330-->

<!-- markdownlint MD028 -->

> Q12. (medium) Consider the following _transition probability matrix_ describing the transition probabilities between processes $X_{t - 1}$ and $X_t$.
>
> $$\begin{array}{c c} & \begin{array}{c c c c c} S_0 & S_1 & S_2 & S_3 & S_4 \\ \end{array} \\
> \begin{array}{c c c c c}S_0\\S_1\\S_2\\S_3\\S_4 \end{array} &
> \left(
> \begin{array}{c c c c c}
>      a_{00} & a_{01} & a_{02} & a_{03} & a_{04} \\
>      a_{10} & a_{11} & a_{12} & a_{13} & a_{14} \\
>      a_{20} & a_{21} & a_{22} & a_{23} & a_{24} \\
>      a_{30} & a_{31} & a_{32} & a_{33} & a_{34} \\
>      a_{40} & a_{41} & a_{42} & a_{43} & a_{44} \\
> \end{array}
> \right)
> \end{array}$$
>
> Express $a_{21}$ in terms of
>
> - the probability function $P(\cdots)$
> - the states $S_0, S_1, S_2, S_3, S_4$
> - $X_{t - 1}$ and $X_t$
>
> <!-- list separator -->
>
> - solution: {@{$a_{21} = P(X_t = S_1 \mid X_{t - 1} = S_2)$}@}
> - explanation: {@{Usually, the _transition probability matrix_ is encoded as a _right/row stochastic matrix_, where each row adds up to 1. It is so called "right" because the probability distribution at the next step is computed by $\mathbf S_t = \mathbf S_{t - 1} \mathbf M$. <p> Another, but less common, way to encode it is as a _left/column stochastic matrix_, where each column adds up to 1. The next step probability distribution is computed by $\mathbf S_t =  \mathbf M \mathbf S_{t - 1}$. <p> Note: You should see in _value iteration_, we put the _right/row_ stochastic matrix $\mathbf M$ on the _left_ of the value vector $\mathbf V$ instead: $\mathbf M \mathbf V$. But this is because in value iteration, we are propagation the rewards _backwards_ instead of _forward_.}@} <!--SR:!2025-12-29,288,330!2027-02-06,489,270-->

<!-- markdownlint MD028 -->

> Q13. (advanced) Consider a Markov chain with a state space $\set{A, B, C}$. The following transition probability matrix $M$ describes the transition probabilities between two processes $X_t$ and $X_{t + 1}$, where $$M =
>     \begin{pmatrix}
>      a_{00} & a_{01} & a_{02} \\
>      a_{10} & a_{11} & a_{12} \\
>      a_{20} & a_{21} & a_{22} \\
>     \end{pmatrix}$$
>
> Prove that the transition probability matrix between $X_0$ and $X_2$ is given by $M^2$.
>
> Hint: Use the Markov property and the fact that for an event $E$, $$\begin{align*}
>     & P(E) \\
>      = & P(E|X_1 = A)P(X_1=A) + P(E|X_1 = B)P(X_1=B) + P(E|X_1 = C)P(X_1=C) \,.
>    \end{align*}$$ This formula was taught in the topic "Naive Bayes Classifier".
>
> - solution: {@{$$\begin{aligned} M^2_{s,t} & = \sum_{m = 0}^2 M_{s, m} M_{m, t} \\ & = \sum_{m = 0}^2 P(X_1 = m \mid X_0 = s) P(X_2 = t \mid X_1 = m) \\ & = P(X_2 = t \mid X_0 = s) \end{aligned}$$}@} <!--SR:!2027-10-21,778,330-->

<!-- markdownlint MD028 -->

> Q14. (medium) Given a typical _transition probability matrix_ $\mathbf M$, a (vertex-based) rewards $\mathbf R$, and a discount factor $\gamma \in (0, 1)$, how to compute the exact expected reward starting from state $s$, $V(s)$?
>
> - solution: {@{Solve for the exact solution for $\mathbf V$ in $$\mathbf V = \mathbf R + \gamma \mathbf M \mathbf V \,.$$ <p> Note: You should see in _value iteration_, we put the _right/row_ stochastic matrix $\mathbf M$ on the _left_ of the value vector $\mathbf V$ instead: $\mathbf M \mathbf V$. But this is because in value iteration, we are propagation the rewards _backwards_ instead of _forward_.}@} <!--SR:!2028-04-01,859,330-->

<!-- markdownlint MD028 -->

> Q15. (simple) State __one__ advantage and __one__ disadvantage of solving a Markov system algebraically.
>
> - solution: {@{(for reference) An advantage is that we get the _exact_ solution. <p> An disadvantage is that the time it takes to solve algebraically increases with the number of states.}@} <!--SR:!2027-05-15,667,330-->

<!-- markdownlint MD028 -->

> Q16. (medium) True or false: Consider a Markov chain with a state space $\{ S_1, S_2, \cdots, S_N \}$ and a discount factor $\gamma \in (0, 1)$. Each $V_1(S_1), V_1(S_2), \cdots, V_1(S_N)$ is finite. Then, using _value iteration_, $\lim_{n\to\infty} V_n(\text{state}_i)$ converges for any $\text{state}_i \in \text{state space}$.
>
> - solution: {@{true}@}
> - explanation: {@{If you want to prove this, consider the matrix function $\mathbf V_{t + 1}(\mathbf V_{t}) = \mathbf R + \gamma \mathbf M \mathbf V_t$ and look up the __contraction mapping theorem__ (also known as the [__Banach fixed-point theorem__](../../../../general/Banach%20fixed-point%20theorem.md)). But this is out of scope.}@} <!--SR:!2029-01-22,1163,350!2027-01-12,512,310-->

<!-- markdownlint MD028 -->

> Q17. (simple) Consider solving a Markov chain with state space $\{ S_1, S_2, \cdots, S_N \}$ by _value iteration_, with a threshold $\varepsilon$. Which of the following correctly describes the stopping condition?
>
> 1. $\max_{s\in \{ S_1, S_2, \cdots, S_N \} } | V_k(s) - V_{k-1}(s) | < \varepsilon$
> 2. $\max_{s_a, s_b \in \{ S_1, S_2, \cdots, S_N \} } | V_k(s_a) - V_{k}(s_b) | < \varepsilon$
> 3. $\max_{k\in \{ 1, 2, \cdots, N \} } | V_k(s) - V_{k-1}(s) | < \varepsilon$
> 4. $\max_{k\in \{ 1, 2, \cdots, N \} } | V_k(s_a) - V_{k}(s_b) | < \varepsilon$
>
> - solution: {@{1}@}
> - explanation: {@{There may be other ways to determining convergence. But 2, 3, and 4 are definitely not the "other ways" as they do not even make sense.}@} <!--SR:!2025-12-23,283,330!2029-03-25,1210,350-->

<!-- markdownlint MD028 -->

> Q18. (simple) State __one__ advantage and __one__ disadvantage of solving a Markov system by value iteration.
>
> - solution: {@{(for reference) An advantage is that we will converge to the optimal solution. <p> An disadvantage is that the time it takes to converge increases with the number of states and actions.}@} <!--SR:!2028-08-12,1029,350-->
