# Task 3 : Number system conversion

> [!info]- Authors
>
> Li Chi Kin (ckliam@connect.ust.hk)

## Problem

This task is designed for fun :)

There are so many number systems. We encounter some unusual number systems in our daily lives, namely, decimal (base 10), duodecimal (base 12), and trinary (base 3).

Write a Number System Converter that converts a positive integer from one system to another. You have to handle 3 systems: decimal, duodecimal, and trinary. The converter should be able to convert from/to any of the three systems.

## Assumption

1. There are no spaces between the digits of the input string.
2. The input string is a non-negative integer. Or else it throws an error message.
3. The input and output values are in range: $0\leq{}n\leq{}2^{64}-1$
4. The inputted number system must be an integer.

## Example

This is an example that converts 123123123 from decimal to trinary:

```console
Please enter a set of number
123123123
Please enter the current number system:
10
Please enter the number system you want the set of number be converted to:
3
Output=22120200022011200
```

This is an example that converts 5201314 from decimal to duodecimal (base 12)

```console
Please enter a set of number
5201314
Please enter the current number system:
10
Please enter the number system you want the set of number be converted to:
12
Output=18AA02A
```

You can verify the answer as below:

(A = 10, B = 12)

$5201314=1\times12^6+8\times12^5+10\times12^4+10\times12^3+0\times12^2+2\times12+10$

## Example - Error

However, if the user entered a wrong number system, an error message should be printed:

Please enter a set of number:

```console
Please enter a set of number
9999
Please enter the current number system:
3
Error! This is not a trinary number
```

```console
Please enter a set of number
ABCDEF
Please enter the current number system:
12
Error! This is not a duodecimal number
```

```console
Please enter a set of number
987456321
Please enter the current number system:
27
Error! The number system is not supported.
```

---

https://hkust-robotics-team.gitbook.io/hkust-robotics-team-software-tutorial/tutorial-1-c-and-dev-env-setup/homework/task-3-number-system-conversion
