# Task 1 : String input calculator

> [!info]- Authors
>
> Li Chi Kin (ckliam@connect.ust.hk)

## Problem

Imagine this: You're facing a straightforward math problem which only consists of four basic operations. But wait, you're not in the mood to crunch the numbers. Here's what I think you'd do: Open Google, input the entire expression in the search box, and click enter. After a blink moment, _viola_! You get the answer!

![](Pasted%20image%2020230830184041.png)

In this assignment, you have to create a similar calculator that only deals with 2 operations: addition (+) and subtraction (-). In the Extra level, you must create an upgraded version that deals with all 4 operations and parentheses.

### Assumption

The following assumptions are allowed to be applied in the EXTRA LEVEL.

1. There are no spaces between values and operators in the user string input e.g. 1+2+3-4, 2-9-8-7
2. If the value is a number, it must be a non-negative integer. E.g. there is no 5+-9--7+10
3. Although all input numbers are non-negative, the intermediate results and/or the final result might be negative
4. The input numbers, intermediate results and the final result is in range: $-2^{63}\leq{}n\leq2^{63}-1$
5. If the string input contains any characters other than numbers (0-9) or operators(+-), the program throws an error message
6. The maximum length of the input string is 200 characters.

### Example

```
Please input a math equation:
1+2+3
Output:
6
```

```console
Please input a math equation:
56-79+2365-89666
Output:
-87324
```

```console
Please input a math equation:
h+e+l+l+o
Output:
ERROR! The string input is not supported!!
```

## EXTRA LEVEL

Math is not only restricted by the 2 simple operations. There are multiplication (\*) and division(/) (not to mention complicated operations like integration(∫), etc. ). In this Extra level, your task is to create a calculator that supports all 4 basic operations(+-*/) and parentheses.

(Hint keywords: stack, postfix notation)

### Extra Assumption for Extra level

The following assumptions are applied in the EXTRA LEVEL only.

1. There are no spaces between values and operators in the user string input e.g. 1+2+3-4, 2-9-8-7
2. If the value is a number, it must be a non-negative integer. E.g. there is no 5+-9--7+10
3. Although all input numbers are non-negative, the intermediate results and/or the final result might be negative
4. The input numbers, intermediate results and the final result is in range: $-2^{63}\leq{}n\leq2^{63}-1$
5. If the string input contains any characters other than numbers (0-9) or operators (+-*/()), the program throws an error message
6. If the number of '(' does not match with the number of ')',  the program throws the same error message as above.
7. There must be a operator (+-*/()) before and after '(' and ')' unless the '(', ')' is in the front or back of the expression.
8. The / is integer division. So, 22/7 = 3 instead of 3.14
9. The maximum length of the input string is 200 characters.

```console
Please input a math equation:
1*6+9*8-6*7 // A string from user input
Output:
36 // program output
```

```console
Please Please input a math equation:
((1+9)*(6+9)) // A string from user input
Output:
150 // program output
```

---

https://hkust-robotics-team.gitbook.io/hkust-robotics-team-software-tutorial/tutorial-1-c-and-dev-env-setup/homework/task-1-string-input-calculator
