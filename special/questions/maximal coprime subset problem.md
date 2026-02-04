---
aliases:
  - maximal coprime subset problem
tags:
  - date/2024/02/23
  - flashcard/active/special/questions/maximal_coprime_subset_problem
  - language/in/English
  - question/algorithm/dynamic_programming
---

# maximal coprime subset problem

- datetime: 2024-02-23T14:58:06.312+08:00

For a given $n \ge 1$, from the set of integers from 1 to $n$, find the subset such that all its elements are coprime and the sum of the elements are as large as possible.

## tips

- According to the [fundamental theorem of arithmetic](../../general/fundamental%20theorem%20of%20arithmetic.md), every integer greater than 1 can be represented uniquely as a product of [prime numbers](../../general/prime%20number.md).
- 1 is coprime with every integer.
- Two numbers are coprime with each other if they do not share any prime divisors.
  - Multiple numbers are coprime with each other if every prime number appears at most once in their divisors.
- Taking all the primes and 1 is not the right answer.
  - Let $n = 9$. Taking all the primes and 1 yields $\set{1, 2, 3, 5, 7}$, which has a sum of 18, but $\set{1, 4, 5, 7, 9}$ also has all its elements being coprime and has a sum of 26.
  - From the above example, one can see that multiplying primes instead of adding can yield a larger subset sum.
- If a subset with all its element being coprime does not use all the prime numbers in their divisors, one can always produce a subset also with all its element being coprime that has a larger subset sum by adding the missing prime numbers to the subset.
  - Let $n = 3$. $\set{1, 2}$ is worse than $\set{1, 2, 3}$.
- For a subset with all its element being coprime uses all the prime numbers in their divisors, one may be able to produce a subset also with all its element being coprime that has a larger subset sum by repeating the same prime number for a single number in the subset.
  - Let $n = 9$. $\set{1, 2, 3, 5, 7}$ is worse than $\set{1, 2 \cdot 2, 3 \cdot 3, 5, 7} = \set{1, 4, 5, 7, 9}$.

## strategy

- inspecting the maximal coprime subset problem, with $n$ given :@: Reinterpret the problem. Using the properties of coprime numbers, it turns out we only need to track the prime numbers used and the generated numbers. The problem can then be reinterpreted as: Given a set of prime numbers, find the way to multiply (prime numbers can be reused in the same multiplication step) and add them together to maximize the sum, subject to that the numbers after multiplication are not greater than $n$. <!--SR:!2028-02-15,798,250-->
- dynamic programming :@: The problem after reinterpretation can be recursively stated. Instead of producing several numbers by multiplication and then adding them at once, only produce one number by multiplication first. Then to maximize the remaining unused prime numbers, the solution is by solving the original problem but on the set of remaining unused prime number. <!--SR:!2026-09-21,476,250-->
- the algorithm :@: After recursively stating problem, the algorithm is a breadth-first search through the possible ways to choose the one number to be produced recursively. Optimizations will need to be applied to reduce the number of cases searched, however. <!--SR:!2029-05-16,1205,270-->
- relation to the longest path problem :@: The reinterpreted problem can be treated as a longest path problem. <p> Let the set of nodes be the power set of the set of prime numbers, which represents the prime numbers used. <p> A path from node A (with power set $A$) to node B (with power set $B$) corresponds to choosing the set of prime numbers $B - A$ and multiplying them together (prime numbers can be reused in the same multiplication step), with the constraint that the product of the multiplication is at least $1$ and not greater than $n$. (This also implies $A \subsetneq B$, and that the graph is acyclic.) The weight of that path is the chosen number. (By this definition, there can be multiple paths from node A to node B.) <p> The starting node is the empty set. The ending node is the whole set of prime numbers, as it is always possible to find a better solution if not the whole set is used. Then the longest path problem is apparent: Find the path from the starting node to the ending node such that the sum of weights along the path are maximized. <!--SR:!2028-05-15,850,250-->

## solution

- credit: [btilly](https://stackoverflow.com/a/5395528), [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/), via Stack Overflow

1. Take the primes from 1 to $n$ in reverse order.
2. Start with an empty set that tracks the used prime numbers. Additionally, track the subset sum. The initial number to be added to the subset is 1 and thus the subset sum is 1.
3. We perform a breadth-first search. At each step, generate the children tracking sets by adding another number to the subset. The number to be added is less than or equal to $n$, must be divisible by the currently greatest unused prime number, and only uses the currently unused prime numbers. The same prime number can be repeated. For each number satisfying the above criteria, generate a child, adding the new prime numbers to the tracking set and update the subset sum. If the new tracking set has appeared before in the tree, only keep the tracking set with the larger subset sum.
    - Note that we do not need to check whether the new number to be added has appeared before. This is because the greatest prime factors of previous numbers must not appear in the prime factors of the new number.
4. Recursively repeat the above step until the tracking set has all the prime numbers, at which point it has no children.
5. From the tracking set with no children, find the one with the greatest subset sum.
6. Follow from the tracking set to the tree root, collecting the numbers to be added to the subset by subtracting the child subset sum from the parent subset sum. The resulting subset is the right answer.

### solution implementations

[Python](../../general/Python.md)

```Python
from itertools import chain
from timeit import timeit
from typing import NamedTuple


def get_primes_less_than(n: int):
    sieve = [True] * (n // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :@: i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return tuple(
        chain((2,) if n > 2 else (), (2 * i + 1 for i in range(1, n // 2) if sieve[i]))
    )


def factorize_n_integers(n: int):
    primes = get_primes_less_than(int(n // 2))
    ret = list[tuple[int, ...]]()
    for k in range(n + 1):
        factors = list[int]()
        for prime in primes:
            if k <= 1:
                break
            while k % prime == 0:
                k //= prime
                factors.append(prime)
        if k >= 2:
            factors.append(k)
        ret.append(tuple(factors))
    return tuple(ret)


def the_algorithm(n: int):
    if n <= 0:
        return ()

    primes = frozenset(get_primes_less_than(n + 1))
    n_factorizations = tuple(map(frozenset, factorize_n_integers(n + 1)))

    class Node(NamedTuple):
        sum: int
        parent: "Node | None"

    initial_node = Node(1, None)
    node_queue, end_nodes = {frozenset[int](): initial_node}, list[
        Node
    ]()  # It is important that `node_queue` preserves insertion order.
    while node_queue:
        used_primes, node = next(iter(node_queue.items()))
        del node_queue[used_primes]
        unused_primes = primes - used_primes
        if not unused_primes:
            end_nodes.append(node)
            continue
        greatest_unused_prime = max(unused_primes)
        for new_num in range(greatest_unused_prime, n + 1, greatest_unused_prime):
            new_num_factorization = n_factorizations[new_num]
            if not new_num_factorization.issubset(unused_primes):
                continue
            new_used_primes, new_sum = (
                used_primes | new_num_factorization,
                node.sum + new_num,
            )
            if new_sum > node_queue.get(new_used_primes, initial_node).sum:
                node_queue[new_used_primes] = Node(new_sum, node)

    ret, cur_node = list[int](), max(end_nodes, key=lambda node: node.sum)
    while cur_node:
        prev_node, cur_node = cur_node, cur_node.parent
        ret.append(prev_node.sum - (cur_node.sum if cur_node else 0))
    ret.sort()
    return tuple(ret)


def test():
    assert tuple(map(the_algorithm, range(101))) == eval(
        """(
        (),
        (1,),
        (1, 2),
        (1, 2, 3),
        (1, 2, 3),
        (1, 3, 4, 5),
        (1, 3, 4, 5),
        (1, 3, 4, 5, 7),
        (1, 3, 5, 7, 8),
        (1, 5, 7, 8, 9),
        (1, 5, 7, 8, 9),
        (1, 5, 7, 8, 9, 11),
        (1, 5, 7, 8, 9, 11),
        (1, 5, 7, 8, 9, 11, 13),
        (1, 5, 7, 8, 9, 11, 13),
        (1, 7, 8, 11, 13, 15),
        (1, 7, 11, 13, 15, 16),
        (1, 7, 11, 13, 15, 16, 17),
        (1, 7, 11, 13, 15, 16, 17),
        (1, 7, 11, 13, 15, 16, 17, 19),
        (1, 7, 11, 13, 15, 16, 17, 19),
        (1, 5, 11, 13, 16, 17, 19, 21),
        (1, 5, 11, 13, 16, 17, 19, 21),
        (1, 5, 11, 13, 16, 17, 19, 21, 23),
        (1, 5, 11, 13, 16, 17, 19, 21, 23),
        (1, 11, 13, 16, 17, 19, 21, 23, 25),
        (1, 11, 13, 16, 17, 19, 21, 23, 25),
        (1, 7, 11, 13, 16, 17, 19, 23, 25, 27),
        (1, 11, 13, 17, 19, 23, 25, 27, 28),
        (1, 11, 13, 17, 19, 23, 25, 27, 28, 29),
        (1, 11, 13, 17, 19, 23, 25, 27, 28, 29),
        (1, 11, 13, 17, 19, 23, 25, 27, 28, 29, 31),
        (1, 7, 11, 13, 17, 19, 23, 25, 27, 29, 31, 32),
        (1, 7, 11, 13, 17, 19, 23, 25, 27, 29, 31, 32),
        (1, 7, 11, 13, 17, 19, 23, 25, 27, 29, 31, 32),
        (1, 11, 13, 17, 19, 23, 27, 29, 31, 32, 35),
        (1, 11, 13, 17, 19, 23, 27, 29, 31, 32, 35),
        (1, 11, 13, 17, 19, 23, 27, 29, 31, 32, 35, 37),
        (1, 11, 13, 17, 19, 23, 27, 29, 31, 32, 35, 37),
        (1, 11, 13, 17, 19, 23, 27, 29, 31, 32, 35, 37),
        (1, 11, 13, 17, 19, 23, 27, 29, 31, 32, 35, 37),
        (1, 11, 13, 17, 19, 23, 27, 29, 31, 32, 35, 37, 41),
        (1, 11, 13, 17, 19, 23, 27, 29, 31, 32, 35, 37, 41),
        (1, 11, 13, 17, 19, 23, 27, 29, 31, 32, 35, 37, 41, 43),
        (1, 13, 17, 19, 23, 27, 29, 31, 35, 37, 41, 43, 44),
        (1, 13, 17, 19, 23, 27, 29, 31, 35, 37, 41, 43, 44),
        (1, 13, 17, 19, 23, 27, 29, 31, 35, 37, 41, 43, 44),
        (1, 13, 17, 19, 23, 27, 29, 31, 35, 37, 41, 43, 44, 47),
        (1, 13, 17, 19, 23, 27, 29, 31, 35, 37, 41, 43, 44, 47),
        (1, 13, 17, 19, 23, 25, 27, 29, 31, 37, 41, 43, 44, 47, 49),
        (1, 13, 17, 19, 23, 25, 27, 29, 31, 37, 41, 43, 44, 47, 49),
        (1, 13, 19, 23, 25, 29, 31, 37, 41, 43, 44, 47, 49, 51),
        (1, 11, 19, 23, 25, 29, 31, 37, 41, 43, 47, 49, 51, 52),
        (1, 11, 19, 23, 25, 29, 31, 37, 41, 43, 47, 49, 51, 52, 53),
        (1, 11, 19, 23, 25, 29, 31, 37, 41, 43, 47, 49, 51, 52, 53),
        (1, 19, 23, 29, 31, 37, 41, 43, 47, 49, 51, 52, 53, 55),
        (1, 19, 23, 29, 31, 37, 41, 43, 47, 49, 51, 52, 53, 55),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 49, 52, 53, 55, 57),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 49, 52, 53, 55, 57),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 49, 52, 53, 55, 57, 59),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 49, 52, 53, 55, 57, 59),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 49, 52, 53, 55, 57, 59, 61),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 49, 52, 53, 55, 57, 59, 61),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 49, 52, 53, 55, 57, 59, 61),
        (1, 13, 17, 23, 29, 31, 37, 41, 43, 47, 49, 53, 55, 57, 59, 61, 64),
        (1, 11, 17, 23, 29, 31, 37, 41, 43, 47, 49, 53, 57, 59, 61, 64, 65),
        (1, 11, 17, 23, 29, 31, 37, 41, 43, 47, 49, 53, 57, 59, 61, 64, 65),
        (1, 11, 17, 23, 29, 31, 37, 41, 43, 47, 49, 53, 57, 59, 61, 64, 65, 67),
        (1, 11, 17, 23, 29, 31, 37, 41, 43, 47, 49, 53, 57, 59, 61, 64, 65, 67),
        (1, 11, 17, 19, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 64, 65, 67, 69),
        (1, 11, 17, 19, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 64, 65, 67, 69),
        (1, 11, 17, 19, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 64, 65, 67, 69, 71),
        (1, 11, 17, 19, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 64, 65, 67, 69, 71),
        (1, 11, 17, 19, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 64, 65, 67, 69, 71, 73),
        (1, 11, 17, 19, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 64, 65, 67, 69, 71, 73),
        (1, 11, 17, 19, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 64, 65, 67, 69, 71, 73),
        (1, 11, 17, 19, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 64, 65, 67, 69, 71, 73),
        (1, 17, 19, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 65, 67, 69, 71, 73, 77),
        (1, 17, 19, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 65, 67, 69, 71, 73, 77),
        (1, 17, 19, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 65, 67, 69, 71, 73, 77, 79),
        (1, 17, 19, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 65, 67, 69, 71, 73, 77, 79),
        (1, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 65, 67, 71, 73, 77, 79, 81),
        (1, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 65, 67, 71, 73, 77, 79, 81),
        (1, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 65, 67, 71, 73, 77, 79, 81, 83),
        (1, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 65, 67, 71, 73, 77, 79, 81, 83),
        (1, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 67, 71, 73, 77, 79, 81, 83, 85),
        (1, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 67, 71, 73, 77, 79, 81, 83, 85),
        (1, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 67, 71, 73, 77, 79, 81, 83, 85),
        (1, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 67, 71, 73, 77, 79, 81, 83, 85),
        (1, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 67, 71, 73, 77, 79, 81, 83, 85, 89),
        (1, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 64, 67, 71, 73, 77, 79, 81, 83, 85, 89),
        (1, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 81, 83, 85, 88, 89, 91),
        (1, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 81, 83, 85, 88, 89, 91),
        (1, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 81, 83, 85, 88, 89, 91),
        (1, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 81, 83, 85, 88, 89, 91),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 81, 83, 88, 89, 91, 95),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 81, 83, 88, 89, 91, 95),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 81, 83, 88, 89, 91, 95, 97),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 81, 83, 88, 89, 91, 95, 97),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 81, 83, 88, 89, 91, 95, 97),
        (1, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 81, 83, 88, 89, 91, 95, 97),
)"""
    )


if __name__ == "__main__":
    print(timeit(test, number=100) / 100)
```
